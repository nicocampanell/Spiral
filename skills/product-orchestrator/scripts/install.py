"""Install this skill and its native Codex roles, preserving existing guidance."""

from datetime import datetime, timezone
from pathlib import Path
import os
import tempfile
import tomllib


START = "<!-- product-orchestrator:start -->"
END = "<!-- product-orchestrator:end -->"


def install(home: Path, source: Path) -> dict:
    home, source = home.resolve(), source.resolve()
    roles = sorted((source / "agents").glob("*.toml"))
    names = []
    for role in roles:
        data = tomllib.loads(role.read_text())
        if any(not isinstance(data.get(k), str) or not data[k].strip()
               for k in ("name", "description", "developer_instructions")):
            raise ValueError(f"Invalid agent fields: {role.name}")
        if data["name"] != role.stem:
            raise ValueError(f"Agent name differs from filename: {role.name}")
        names.append(data["name"])
    if len(roles) != 8 or len(set(names)) != 8:
        raise ValueError("Expected eight unique role definitions")

    destination = home / ".agents/skills/product-orchestrator"
    planned = {}
    for item in source.rglob("*"):
        if item.is_file() and "__pycache__" not in item.parts and item.name != ".DS_Store":
            planned[destination / item.relative_to(source)] = item.read_bytes()
    for role in roles:
        planned[home / ".codex/agents" / role.name] = role.read_bytes()

    guidance = home / ".codex/AGENTS.md"
    original = guidance.read_text() if guidance.exists() else ""
    section = (source / "assets/AGENTS.section.md").read_text().strip()
    if original.count(START) != original.count(END) or original.count(START) > 1:
        raise ValueError("Malformed existing managed AGENTS.md section; preserve and inspect it")
    if START in original:
        a, b = original.index(START), original.index(END) + len(END)
        if original.index(END) < a:
            raise ValueError("Reversed AGENTS.md markers")
        updated = original[:a] + section + original[b:]
    else:
        updated = original + ("\n\n" if original else "") + section + "\n"
    planned[guidance] = updated.encode()

    changes = []
    for target, content in planned.items():
        if target.is_symlink():
            raise ValueError(f"Refusing to replace a symlink: {target}")
        if not target.exists() or target.read_bytes() != content:
            changes.append((target, content))
    backup = None
    if changes:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        backup = home / ".codex/backups/product-orchestrator" / stamp
        for target, _ in changes:
            if target.exists():
                saved = backup / target.relative_to(home)
                saved.parent.mkdir(parents=True, exist_ok=True)
                saved.write_bytes(target.read_bytes())
        for target, content in changes:
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as handle:
                    temporary = Path(handle.name)
                    handle.write(content)
                os.replace(temporary, target)
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
        assert all(target.read_bytes() == content for target, content in planned.items())
    return {"changed_files": len(changes), "skill": str(destination),
            "agents": names, "backup": str(backup) if backup and backup.exists() else None}


if __name__ == "__main__":
    import json
    print(json.dumps(install(Path.home(), Path(__file__).resolve().parents[1]), indent=2))
