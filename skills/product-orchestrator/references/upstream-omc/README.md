# Oh My Claude Code source snapshots

These reference snapshots come from [`dec7e4188c0e3de6b92fb3d734ee5c95326021ed`](https://github.com/yeachan-heo/oh-my-claudecode/tree/dec7e4188c0e3de6b92fb3d734ee5c95326021ed) and retain the upstream [MIT license](LICENSE).

| Local snapshot | Upstream file | What the Codex skill uses |
|---|---|---|
| [Team excerpts](team-excerpts.md.txt) | `skills/team/SKILL.md`, lines 95–201 and 504–537 | Staged delivery, explicit exit criteria, bounded repair, concrete lead and teammate handoffs |
| [Verifier](verifier.md.txt) | `agents/verifier.md` | Evidence tied to claims and an independent acceptance verdict |
| [Pipeline state](pipeline-state.ts.txt) | `src/hooks/team-pipeline/state.ts` | Source for the phase and repair design and for evaluating future state validation |
| [Verification ledger](verification-ledger.ts.txt) | `src/features/verification-ledger/ledger.ts` | Durable verdicts bound to work and reviewers, and an implementation reference for future provenance |

Use the [Codex task playbooks](../task-playbooks.md) and [communication contract](../communication.md) during delivery. The source excerpts and code are reference data from the Claude Code runtime.
