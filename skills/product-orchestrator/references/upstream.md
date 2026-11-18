# Upstream basis and adaptation

This skill is an independently worded Codex adaptation of specific upstream contracts, not a reimplementation of their runtimes. Preserve these links when extending it so changes stay grounded in the source mechanisms.

Sources reviewed on 2026-11-12:

- oh-my-claudecode: `dec7e4188c0e3de6b92fb3d734ee5c95326021ed`
- cursor/plugins pstack: `ec569379616a4826b98f0f0a205dd3411b573611`

| This skill's part | Existing upstream basis | Adaptation |
|---|---|---|
| Delivery stages | [OMC team](https://github.com/yeachan-heo/oh-my-claudecode/blob/dec7e4188c0e3de6b92fb3d734ee5c95326021ed/skills/team/SKILL.md) | Preserve plan → requirements → execute → verify → fix; use Codex native agents |
| Scoped delegation and pilot | [pstack Orchestrate](https://github.com/cursor/plugins/blob/ec569379616a4826b98f0f0a205dd3411b573611/pstack/skills/poteto-mode/playbooks/orchestrate.md) | One active owner per path/coherent change; standalone task briefs; pilot before repeated fan-out |
| Dependency-aware feature work | [pstack Feature](https://github.com/cursor/plugins/blob/ec569379616a4826b98f0f0a205dd3411b573611/pstack/skills/poteto-mode/playbooks/feature.md) | Design/copy feed frontend; client/server agree interfaces before parallel implementation |
| Specialist contracts | [OMC agent definitions](https://github.com/yeachan-heo/oh-my-claudecode/tree/dec7e4188c0e3de6b92fb3d734ee5c95326021ed/agents) | Keep responsibility boundaries and deliverables; add requested product/copy/frontend/backend separation |
| Independent acceptance | [OMC verifier](https://github.com/yeachan-heo/oh-my-claudecode/blob/dec7e4188c0e3de6b92fb3d734ee5c95326021ed/agents/verifier.md), pstack Orchestrate | Reviewer checks current integrated artifact against original criteria; no self-approval |
| Evidence history | [OMC ledger](https://github.com/yeachan-heo/oh-my-claudecode/blob/dec7e4188c0e3de6b92fb3d734ee5c95326021ed/src/features/verification-ledger/ledger.ts), which credits pstack | Lead-owned per-run record; distinguish evidence levels and stale verdicts |
| Bounded repair | [OMC pipeline state](https://github.com/yeachan-heo/oh-my-claudecode/blob/dec7e4188c0e3de6b92fb3d734ee5c95326021ed/src/hooks/team-pipeline/state.ts), pstack Orchestrate | Three repair rounds; diagnose/replan after two without progress; exhaustion stays incomplete |
| Resume context | [pstack session pickup](https://github.com/cursor/plugins/blob/ec569379616a4826b98f0f0a205dd3411b573611/pstack/skills/poteto-mode/playbooks/session-pickup.md) | Save decisions, owners and evidence; reconcile actual files/agents on resume |

The [local pstack source snapshots](upstream-pstack/README.md) and [local OMC source snapshots](upstream-omc/README.md) include the procedures, role prompts, and state examples behind the adaptation. Use the [task playbooks](task-playbooks.md) and [verification recipe](verification-recipe.md) during delivery.

Do not carry over runtime guarantees without runtime code. OMC's actual task leases, hook continuation, approval provenance validation and locking are code. A Markdown role/record cannot enforce those controls. OMC's nominal Ralph iteration maximum auto-extends; this skill instead uses the team's explicit bounded repair pattern. pstack's fixed full-program lane count and Cursor-specific model/cloud/loop assumptions are not portable defaults.

Source inspection supports the design rationale; it does not establish which project performs best in real use. Upstream runtime tests and product-delivery performance were not executed in this study.
