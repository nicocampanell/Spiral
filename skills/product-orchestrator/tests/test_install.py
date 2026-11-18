from pathlib import Path
import importlib.util
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", SOURCE / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.home = Path(self.temporary.name)
        (self.home / ".codex/agents").mkdir(parents=True)
        (self.home / ".codex/AGENTS.md").write_text("Existing memory and instructions.\n")
        (self.home / ".codex/agents/existing.toml").write_text("untouched")

    def test_preserves_guidance_and_existing_roles_and_is_idempotent(self):
        result = installer.install(self.home, SOURCE)
        self.assertEqual(len(result["agents"]), 8)
        guidance = (self.home / ".codex/AGENTS.md").read_text()
        self.assertTrue(guidance.startswith("Existing memory and instructions.\n"))
        self.assertEqual(guidance.count(installer.START), 1)
        self.assertEqual((self.home / ".codex/agents/existing.toml").read_text(), "untouched")
        self.assertEqual(installer.install(self.home, SOURCE)["changed_files"], 0)
        backup = Path(result["backup"]) / ".codex/AGENTS.md"
        self.assertEqual(backup.read_text(), "Existing memory and instructions.\n")

    def test_updates_only_managed_guidance_block(self):
        existing = "Before\n" + installer.START + "\nOld team\n" + installer.END + "\nAfter\n"
        (self.home / ".codex/AGENTS.md").write_text(existing)
        installer.install(self.home, SOURCE)
        actual = (self.home / ".codex/AGENTS.md").read_text()
        self.assertTrue(actual.startswith("Before\n"))
        self.assertTrue(actual.endswith("\nAfter\n"))
        self.assertNotIn("Old team", actual)

    def test_malformed_guidance_aborts_before_any_role_write(self):
        path = self.home / ".codex/AGENTS.md"
        path.write_text("Preserve me\n" + installer.START)
        with self.assertRaises(ValueError):
            installer.install(self.home, SOURCE)
        self.assertEqual(path.read_text(), "Preserve me\n" + installer.START)
        self.assertFalse((self.home / ".codex/agents/web-designer.toml").exists())

    def test_symlink_target_is_not_overwritten(self):
        outside = self.home / "keep.toml"
        outside.write_text("keep")
        (self.home / ".codex/agents/web-designer.toml").symlink_to(outside)
        with self.assertRaises(ValueError):
            installer.install(self.home, SOURCE)
        self.assertEqual(outside.read_text(), "keep")
        self.assertFalse((self.home / ".agents/skills/product-orchestrator").exists())

    def test_reversed_markers_abort_without_changes(self):
        path = self.home / ".codex/AGENTS.md"
        text = installer.END + installer.START
        path.write_text(text)
        with self.assertRaises(ValueError):
            installer.install(self.home, SOURCE)
        self.assertEqual(path.read_text(), text)
        self.assertFalse((self.home / ".codex/agents/web-designer.toml").exists())


if __name__ == "__main__":
    unittest.main()
