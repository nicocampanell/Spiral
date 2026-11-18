"""Validate verification evidence against a project contract and current files."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def project_path(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("Use a nonempty project-relative path")
    path = root
    for part in Path(name).parts:
        if part == "..":
            raise ValueError(f"Path escapes project: {name}")
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlinks are unsupported: {name}")
    return path


def digest(path):
    if not path.is_file():
        raise ValueError(f"Required file missing: {path}")
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def names(value, label):
    if not isinstance(value, list) or not value or any(
        not isinstance(item, str) or not item.strip() for item in value
    ) or len(value) != len(set(value)):
        raise ValueError(f"{label} must list unique nonempty strings")
    return value


def snapshot(root, contract):
    revision = contract["criteria_revision"]
    if not isinstance(revision, str) or not revision.strip():
        raise ValueError("criteria_revision must be a nonempty string")
    names(contract["required"], "required")
    files = {}
    for name in names(contract["inputs"], "inputs"):
        path = project_path(root, name)
        entries = sorted(path.rglob("*")) if path.is_dir() else [path]
        for entry in entries:
            if entry.is_symlink():
                raise ValueError(f"Symlink in verification inputs: {entry}")
            if not entry.is_dir():
                files[entry.relative_to(root).as_posix()] = digest(entry)
    if not files:
        raise ValueError("No artifact files were captured")
    payload = json.dumps({"contract": contract, "files": files}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def check(root, contract, report):
    if report["snapshot"] != snapshot(root, contract):
        raise ValueError("Stale artifact or criteria. Re-run affected verification.")
    reviewer = report["reviewer"]
    if not isinstance(reviewer, str) or not reviewer.strip():
        raise ValueError("Missing verifier identity")
    checks = report["checks"]
    if not isinstance(checks, dict) or checks.keys() != set(contract["required"]):
        raise ValueError("Evidence must cover exactly the required criteria")
    for criterion, entry in checks.items():
        if entry["status"] != "pass":
            raise ValueError(f"{criterion}: required check did not pass")
        path = project_path(root, entry["evidence"])
        if digest(path) != entry["sha256"] or path.stat().st_size == 0:
            raise ValueError(f"{criterion}: evidence is empty or has changed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("snapshot").add_argument("contract")
    commands.add_parser("hash").add_argument("evidence")
    verify = commands.add_parser("check")
    verify.add_argument("contract")
    verify.add_argument("report")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "hash":
            print(digest(project_path(root, args.evidence)))
            return 0
        contract = json.loads(project_path(root, args.contract).read_text())
        if args.command == "snapshot":
            print(snapshot(root, contract))
        else:
            report = json.loads(project_path(root, args.report).read_text())
            check(root, contract, report)
            print("PASS: required evidence matches the current artifact and criteria")
        return 0
    except (OSError, KeyError, TypeError, ValueError, AttributeError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
