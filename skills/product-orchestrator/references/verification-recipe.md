# Reusable project verification

For substantial work, find the repository's maintained way to verify the real app. Reuse its tests and run commands. If this path cannot be reproduced by a fresh agent, save the smallest useful recipe in the existing test or development docs, or in `.product-orchestrator/verification.md`. Keep credentials and run outputs out of tracked files.

Record the exact setup and launch commands, safe environment and ready signal; how to isolate resources, migrate and seed disposable data; the core journey and meaningful failure case; how to observe success and persisted behavior; where evidence is saved; and how to stop only the resources started by this run. For a CLI or library, adapt the journey to its public entry point. Exercise setup, journey, evidence capture and cleanup once from an isolated state. Confirm the evidence survives cleanup. A recipe with blocked steps is a draft until those steps run.

## Maintain feature coverage

For multiple acceptance paths, keep a feature map next to the recipe. Map stable criterion IDs to the public entry point, fixture and environment, success and failure observations, evidence command or browser steps, and cleanup. Link existing tests and group shared setup. The map names coverage. A dated run records whether each affected check passed, failed or was blocked on the current artifact.

After a route, control, fixture, or dependency changes, trace the new entry point and drive the affected map entries from a clean setup. Distinguish stale steps, missing harness coverage and product defects. Repair the recipe when its steps drift, add targeted coverage if the harness misses a consequential behavior, and route defects to their owner. Re-run affected checks and retain their evidence after cleaning up the run's resources.

## Run the evidence gate

For substantial work, the lead saves a contract JSON under the run directory before verification. Review its coverage against the requirements and relevant artifact files. Example:

```json
{
  "criteria_revision": "r1",
  "required": ["core-save", "reject-invalid"],
  "inputs": ["src", "tests", "package.json", "docs/current-acceptance.md"]
}
```

Include the source, tests, lockfile, schema, config and criteria material relevant to the checks, including new files and uncommitted edits. Paths are relative to the project root. Prefer focused source directories so adding or deleting a file changes the snapshot. Keep generated logs, caches, secrets, scratch data and the report outside input directories. For external state, record the environment and version as evidence and reverify when it changes.

Use `python3 <skill-dir>/scripts/verification_gate.py` from the project root (or pass `--root <project>` before the subcommand):

1. Before running checks, the independent verifier runs `snapshot <contract.json>` and saves the returned token. The verifier also inspects the criteria and current artifact.
2. Run the checks and retain actual output. Use `hash <evidence-path>` to get each artifact's SHA-256. Save a report with the initial token, actual reviewer identity, and one check per required criterion. For an observation with a screenshot, describe the steps and result in the log and retain the screenshot as supporting evidence.
3. The lead collects the report from the assigned verifier through native collaboration and matches the agent identity and actual tool outcomes. Run `check <contract.json> <report.json>` before declaring verified and after any relevant change or resume before reusing a verdict. A nonzero exit holds the affected milestone. Preserve the old report and rerun checks on the current snapshot when needed.

```json
{
  "snapshot": "<token captured before verification>",
  "reviewer": "<assigned verifier ID>",
  "checks": {
    "core-save": {"status": "pass", "evidence": ".product-orchestrator/run/save.log", "sha256": "<hash>"},
    "reject-invalid": {"status": "pass", "evidence": ".product-orchestrator/run/invalid.log", "sha256": "<hash>"}
  }
}
```

Use the gate from an existing release or CI command where the project needs a mechanical stop. The script checks completeness and file identity. The lead still checks report provenance, scope and what the evidence demonstrates. For single-agent fallback, label reviewer independence unavailable and report it as a gap when independent approval is required.
