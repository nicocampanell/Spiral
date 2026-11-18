# Product Orchestrator

A Codex-first product team adapted from OMC's staged team workflow and pstack's ownership, delegation, independent verification and repair contracts, shaped around product discovery and evidence-based delivery. [Upstream mapping](references/upstream.md) records the source basis and runtime limits.

## Use

Ask: `$product-orchestrator help me shape and build [product/feature] using its project Notion page [link]`.

For a rough idea, the lead interviews the project owner, challenges assumptions with relevant outside perspectives, and offers 2–3 distinct directions for a new interface or major redesign. After selection it builds autonomously, bringing them back for meaningful product changes and working milestones. The first-build bar is a coherent, polished core flow that works end to end. Each project has its own Notion home with nested vision, research, decision and delivery/verification documents, reusing existing equivalents. Existing approved tickets and small fixes skip rediscovery.

The native roles are `product-orchestrator`, `product-strategist`, `web-designer`, `mobile-designer`, `product-copywriter`, `frontend-engineer`, `backend-engineer`, and `product-verifier`. Responsive mobile websites go to web design; native iOS/Android goes to mobile design. The roster is available on demand, not a mandatory eight-agent team.

Use the [task router](references/task-playbooks.md) for investigation, bug fixes, feature delivery, migrations, prototypes, visual parity, performance, verification maintenance and recall. The [pstack source snapshots](references/upstream-pstack/README.md) and [OMC source snapshots](references/upstream-omc/README.md) ship locally with revision, path and license information.

## Individual craft floors

Each role contains concrete instructions, with deeper source-grounded references for [design](references/craft-design.md), [engineering](references/craft-engineering.md) and [writing/Humanizer](references/craft-writing.md). They cover consistent 8/4-unit spacing, restrained typography, semantic tokens, accessibility, complete interaction/error states, content resilience, meaningful tests, data integrity and clear copy that preserves facts. Existing coherent systems and approved identity remain authoritative; defaults are not quotas. [Source mapping](references/craft-sources.md) explains the local/GitHub sources and conflicting rules that were filtered out.

## Install or update

Run `python3 scripts/install.py` from this skill folder. It installs the skill at `~/.agents/skills/product-orchestrator`, copies the eight standalone TOML agents into `~/.codex/agents`, and adds/updates only its marked section of `~/.codex/AGENTS.md`. Existing changed files are backed up under `~/.codex/backups/product-orchestrator/`; unrelated agents and guidance are preserved. Malformed managed markers or symlink targets stop installation before any changes. Repeating the same install makes no changes.

Start a fresh chat/session to load updated roles. Existing sessions can use generic agents with the bundled role instructions as an explicit fallback. A fresh CLI lead can use `codex -m gpt-6.2-astra -c model_reasoning_effort=medium` where that model is available. In the app select GPT-6.2 Astra for the main chat. [Model routing](references/model-routing.md) describes the configured defaults and availability checks.

## Checks and limits

Run `python3 -m unittest discover -s tests -v` for installation preservation/idempotency checks. Role files use native TOML, inherit parent permissions, and do not grant independent read-only sandboxes. The skill uses Codex's existing agent transport; it does not implement a daemon, locking/leases or automatic crash resumption.

Notion uses a verified per-project destination and the local Composio CLI. The lead preserves existing page content, writes scoped decision/progress updates, and checks saved results. If destination/access is missing, the pending update remains local rather than being reported as synced. No Notion credentials or account defaults are bundled.

Initial planning scenarios passed both with and without the skill, so they do not establish an advantage over ordinary Codex. Source review and isolated execution exercises are sanity checks, not a reliability, cost or speed benchmark. Evaluate the team on representative real work before making stronger claims.
