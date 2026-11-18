# pstack source snapshots

These thirteen selected files are included for local reading and source comparison under the accompanying [MIT license](LICENSE). The primary upstream revision is `35a90942a7f02e1ebbc2443643179815f2147954`. The source root for the paths below is the [pstack directory at that revision](https://github.com/cursor/plugins/tree/35a90942a7f02e1ebbc2443643179815f2147954/pstack).

| Local snapshot | Upstream path under pstack | Used in the Codex adaptation for |
|---|---|---|
| [Figure it out](figure-it-out.md.txt) | `skills/figure-it-out/SKILL.md` | Turning an open-ended task into an observable outcome |
| [Feature](feature.md.txt) | `skills/poteto-mode/playbooks/feature.md` | Keeping contract gates and dependencies visible during fan-out |
| [Orchestrate](orchestrate.md.txt) | `skills/poteto-mode/playbooks/orchestrate.md` at [`ec569379`](https://github.com/cursor/plugins/blob/ec569379616a4826b98f0f0a205dd3411b573611/pstack/skills/poteto-mode/playbooks/orchestrate.md) | A pilot, one owner per unit and evidence-based repair |
| [Bug fix](bug-fix.md.txt) | `skills/poteto-mode/playbooks/bug-fix.md` | Reproduction, diagnosis and replay |
| [Prototype](prototype.md.txt) | `skills/poteto-mode/playbooks/prototype.md` | Isolated, disposable experiments |
| [Visual parity](visual-parity.md.txt) | `skills/poteto-mode/playbooks/visual-parity.md` | Matching rendered states against a known reference |
| [Hillclimb](hillclimb.md.txt) | `skills/poteto-mode/playbooks/hillclimb.md` | Comparing bounded iterations on a fixed workload |
| [Benchmark checklist](benchmark-checklist.md.txt) | `skills/benchmark-checklist/SKILL.md` | Checking measurement validity and correctness |
| [Runtime forensics](runtime-forensics.md.txt) | `skills/poteto-mode/playbooks/runtime-forensics.md` | Using runtime evidence to distinguish causes |
| [Trace forensics](trace-forensics.md.txt) | `skills/poteto-mode/playbooks/trace-forensics.md` | Following a user action across execution boundaries |
| [Create verification](create-verification.md.txt) | `skills/create-verification-skill/SKILL.md` | Creating a repeatable setup, drive, evidence and teardown procedure |
| [Maintain verification](maintain-verification.md.txt) | `skills/maintain-verification-skill/SKILL.md` | Keeping feature coverage and entry points current |
| [Recall](recall.md.txt) | `skills/recall/SKILL.md` | Restoring evidence and decisions on a fresh run |

These are reference data. Use the [Codex task playbooks](../task-playbooks.md) for executable workflow decisions. Cursor commands, tool names, schedules, model names and permissions in the snapshots describe the upstream environment.
