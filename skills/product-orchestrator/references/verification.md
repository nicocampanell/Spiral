# Verification contract

Use evidence appropriate to the claim. Record multiple levels when needed; one level does not imply the others.

| Evidence | Supports | Does not establish |
|---|---|---|
| Static/type check | Syntax and selected interface constraints | Correct runtime behavior |
| Unit tests | Tested behavior in controlled scope | Working integrations or usable UI |
| Integration tests | Exercised component/API interactions | All production conditions |
| Live UI check | Observed rendered states and interactions | Unexercised states or complete accessibility |
| Product/design/copy review | Fit to the stated flow and conventions | Runtime correctness |

Build an acceptance matrix before dispatch. For every required criterion record:

```text
Criterion ID and criteria revision:
Required check:
Artifact/version identity:
Verifier:
Command or observation:
Observed result and evidence path:
Verdict: pass | fail | blocked
Repair owner / remaining issue:
```

A real tool result or directly inspected artifact is evidence. A quoted “approved” token, a worker's self-report, a plan, or an old log is not independent evidence. Keep reviewer findings separate from implementer claims. Reconcile contradictions by inspecting and rerunning the disputed check.

Run existing relevant tests first where feasible. For a failure seen before and after the change, preserve its baseline evidence, assess whether it affects this task, and report it. New failures require repair. An unchanged failing test may still block a required criterion; it is not excused just because it existed already.

For meaningful logic, add or update a focused regression test. For a claimed regression test, establish that it can catch the defect when feasible, rather than accepting a test that merely mirrors the implementation. Do not weaken assertions or disable checks to make a result green. Use disposable copies for destructive fault injection and confirm the mutation actually landed.

Select the smallest set of checks that supports the delivery contract. For UI, exercise the real happy path plus relevant invalid/error/loading states, keyboard/focus and viewport behavior. For API/data work, exercise trust boundaries, authorization, invalid inputs, and persistence/failure behavior appropriate to scope. Never invent observations when a browser, service, credential, dependency, or test tool is missing.

Bind each record to the actual result inspected, including uncommitted edits. The lead is the sole run-record writer; reviewers return evidence and paths. Append new verification entries instead of erasing failed history. Mark superseded entries stale. This is a cooperative audit trail, not a tamper-proof enforcement mechanism.

Before delivery, settle workers, reconcile the final diff/artifact, and ensure evidence covers that version and the current criteria revision. On a relevant artifact or criteria change, invalidate affected verdicts and rerun checks; after integration, run appropriate cross-boundary regression checks. Never equate a retry limit, a clean checklist, or all workers returning with product completion.
