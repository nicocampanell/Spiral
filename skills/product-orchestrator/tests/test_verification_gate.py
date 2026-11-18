import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/verification_gate.py"


class VerificationGateTests(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "src").mkdir()
        (self.root / "src/app.txt").write_text("first build")
        (self.root / "evidence.log").write_text("observed result")
        self.contract = {"criteria_revision": "1", "required": ["save"], "inputs": ["src"]}
        self.save("contract.json", self.contract)
        self.report = {
            "snapshot": self.run_gate("snapshot", "contract.json", status=0).strip(),
            "reviewer": "reviewer-1",
            "checks": {"save": {
                "status": "pass",
                "evidence": "evidence.log",
                "sha256": self.run_gate("hash", "evidence.log", status=0).strip(),
            }},
        }

    def save(self, name, data):
        (self.root / name).write_text(json.dumps(data))

    def run_gate(self, *args, status):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), *args],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, status, result.stderr)
        return result.stdout + result.stderr

    def verify(self, status):
        self.save("report.json", self.report)
        return self.run_gate("check", "contract.json", "report.json", status=status)

    def test_current_report_passes_then_new_source_makes_it_stale(self):
        self.assertIn("PASS", self.verify(0))
        (self.root / "src/new.txt").write_text("uncommitted work")
        self.assertIn("Stale", self.verify(1))

    def test_criteria_edit_invalidates_prior_snapshot(self):
        self.contract["criteria_revision"] = "2"
        self.save("contract.json", self.contract)
        self.assertIn("Stale", self.verify(1))

    def test_requires_passing_results_and_current_evidence(self):
        entry = self.report["checks"]["save"]
        entry["status"] = "blocked"
        self.assertIn("did not pass", self.verify(1))
        entry["status"] = "pass"
        (self.root / "evidence.log").write_text("replaced output")
        self.assertIn("has changed", self.verify(1))
        (self.root / "evidence.log").unlink()
        self.assertIn("Required file missing", self.verify(1))
        self.report["checks"].clear()
        self.assertIn("cover exactly", self.verify(1))

    def test_rejects_paths_outside_project(self):
        self.assertIn("escapes project", self.run_gate("hash", "../outside", status=1))


if __name__ == "__main__":
    unittest.main()
