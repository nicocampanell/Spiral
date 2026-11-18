# Codex task playbooks

Select one primary workflow from the request and the state of the actual repository. Add a supporting workflow when it gives the team a distinct result or check. Reuse familiar project commands and keep a small fix in chat. Consult the [local pstack snapshots](upstream-pstack/README.md) to study an upstream procedure or adapt this skill.

| Request | Primary workflow | Evidence or decision to return |
|---|---|---|
| Understand behavior, explain design, assess impact | Investigation | Entry point, implementation path, affected consumers, evidence and open questions |
| Fix a concrete defect | Bug fix | Original symptom or baseline, cause, focused change and replay |
| Shape and build an idea or change product behavior | Feature delivery | Confirmed criteria, resolved dependencies and verified core flow |
| Change internals or migrate a contract | Refactor and migration | Preserved behavior and verified caller or data cutover |
| Explore a hypothesis or choose an interface direction | Prototype | Distinct runnable alternatives where useful, tradeoffs and choice |
| Match a reference or check cross-surface fidelity | Visual parity | Comparable rendered states, intentional differences and findings |
| Diagnose slow, failing or intermittent behavior | Forensics or performance | Reproducible observation, controls, results and confidence |
| Establish or repair test instructions | Verification maintenance | Feature map, rerunnable setup and evidence from current entry points |
| Resume work or improve the workflow | Recall or skill evaluation | Reconciled handoff or an evaluated, scoped instruction change |

## Bind to the current environment

Inspect repository instructions, manifests and lockfiles, app entry points, existing tests and CI, local run commands and actual working changes. Record the chosen command, fixture and evidence level when those affect acceptance. Use Codex's available native agent transport and the [registered roles and model settings](model-routing.md). For rendered interfaces use an available browser or native simulator on the target platform. For APIs and CLIs use their ordinary entry points and existing test tools. A missing capability gets a concrete blocker and any useful lower-level evidence. Keep user-facing claims within the level observed.

For an unclear request, name the proposed outcome, affected user or caller, how to observe success, and the consequential choice still open. Ask about vision or materially different outcomes. Continue reversible investigation while that decision is pending. When a premise changes, update affected criteria and tasks, stop obsolete writers, and carry forward still-valid evidence.

## Investigation and bug fix

- Trace the actual entry point through implementation, data and adjacent callers. Corroborate the explanation with repository evidence or a safe local observation. For an impact assessment include compatibility consumers, migrations and affected checks. A read-only request ends with findings and uncertainty.
- For a behavior defect, record the observed symptom and reproduce it on the relevant surface with a safe fixture when possible. Separate competing causes with the smallest useful diagnostic. Change the source of the defect and exercise the same behavior again. Add a focused regression when existing checks would miss it. Capture baseline blockers and partial proof explicitly.

## Feature delivery, refactor and migration

- Use existing [discovery](product-discovery.md), [backend checkpoints](backend-architecture.md) and [verification](verification.md). Identify the existing contract, owners, states and affected surfaces before dispatch. Favor one end-to-end slice. Have dependent specialists agree on the contract before they implement in parallel.
- For a refactor, state what user and caller behavior must remain stable. For a migration, inventory consumers, data and rollout prerequisites. Sequence compatible additions, caller migration and removal of the old path using concrete usage and verification evidence. Exercise old data or callers where they remain supported. Record the reversible step or actual recovery path for consequential changes.
- Use [independent proposals](arena-and-learning.md) for genuinely uncertain decisions. Give each candidate the same brief and rubric and isolate competing implementations. For a partitioned review assign disjoint questions or surfaces and combine the findings against the same criteria. Run a representative pilot before repeating one pattern across multiple units.

## Prototype and visual parity

- Isolate the smallest prototype that tests an explicit product or interaction hypothesis. For a new interface or major redesign present two or three meaningfully different directions with real content or representative fixtures, accessibility implications and tradeoffs. Mark shortcuts and the decision each prototype supports. Wait for the project owner's direction before dependent production implementation.
- Capture the approved reference and the current rendered surface where available. Match route, device or viewport, state, content, theme, font and stable screenshot timing. Compare the resulting layout and interaction states, documenting accepted differences. A static check can establish asset or style changes. A rendered comparison requires visual evidence from the target surface.

## Forensics and performance

- Start with the user-visible symptom and an ordinary safe workload. Take a baseline on the relevant surface. Use available logs, timings, browser recordings or request correlation to identify the first boundary that behaves unexpectedly. Record the command, version, input, observed limit and evidence for discarded hypotheses. Redact credentials and personal payloads from retained evidence.
- For optimization define the workload, environment, metric, correctness assertions and iteration budget up front. Repeat the baseline and note its spread. Change one hypothesis per iteration and compare repeated measurements on the same workload. Keep a candidate only when improvement exceeds noise and correctness still passes. Record invalid runs and failed candidates alongside accepted changes. Avoid performance claims when workload, correctness or variance can't be established.

## Verification maintenance

Follow the [project recipe lifecycle](verification-recipe.md). Where the project has multiple acceptance paths, use a feature map with public entry points and observed outcomes. After a route, control, environment or fixture changes, distinguish recipe drift, missing harness coverage and a product failure. Rerun affected paths from clean setup, preserve evidence and clean up only run-owned resources.

## Recall, handoff and skill evaluation

- Restore context from the mapped project record, maintained local guidance and available authorized chat history. Verify artifact identity, current criteria, writer ownership and any active external job before relying on prior status. Preserve an unresolved handoff with the next check. Active-session coordination can continue with available tools.
- Use Skill Creator for instruction or agent changes. Freeze the rubric and scenarios before comparing versions. Inspect actual outputs and state whether the scenarios measure routing, execution, verification, or cost. Use [the learning workflow](arena-and-learning.md) to record a diagnosis, propose a scoped rule, and accept it after evidence supports it. Persist project lessons where a later run naturally looks.
