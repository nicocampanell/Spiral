# Engineering craft contract

The standard is the smallest complete idiomatic change with evidence of the promised behavior. Completeness includes affected consumers and failure paths; brevity alone is not quality. Use relevant installed stack guidance when that stack exists, including Vercel React best practices or Write Swift. Do not transplant framework rules into unrelated code.

## Shared engineering floors

1. **Read implementation and consumers.** Find existing components/helpers/services, their callers, public exports, relevant config, fixtures and tests. Reuse the house pattern before adding machinery. Before changing a shared contract, identify all affected consumers; update them in the owned scope or arrange a handoff.
2. **Keep scope complete and narrow.** Prefer existing code, then platform facilities, then installed dependencies. A new wrapper, abstraction, dependency, option or architecture needs a current requirement and a concrete reason. Avoid unrelated cleanup, clever compression and speculative generality. Keep validation and error handling when moving/merging code.
3. **Make state ownership clear.** Keep one authoritative source for mutable data; derive computable values. Represent genuinely exclusive workflow states explicitly rather than as contradictory flags, without creating a state machine for a trivial toggle. Respect cancellation, stale results, reentrancy and request/user isolation where they apply.
4. **Protect boundaries and data.** Validate untrusted input where it enters trusted code; enforce authentication/authorization at the real server boundary. Use the existing actionable error model. Never report success after a required write failed. Keep the prior valid data until its replacement/migration is confirmed; optional cache failure and durable-data loss are different decisions. Do not delete an old key after swallowing a failed new-key write.
5. **Fix causes and check behavior.** Reproduce a bug where possible, trace the failing path, test one supported hypothesis and check related occurrences. Test public outcomes, material edge/failure cases and integration seams; do not weaken assertions or write tests that merely repeat internal structure. Use proportional verification for trivial reversible edits, and report unavailable checks honestly.
6. **Pay for demonstrated costs.** Address known I/O waterfalls, repeated work, heavy transfer or poor algorithmic growth in the affected path. Parallelize only truly independent operations; preserve causal write ordering, isolation and error semantics. Introduce caching/memoization/concurrency for a named cost with valid invalidation/lifecycle rules, not as boilerplate. A performance claim needs a representative before/after measure and correctness gate.
7. **Treat usable semantics as implementation.** A working user flow includes its actual state feedback, accessible controls, error/recovery and data effects. Type checking, isolated unit tests and screenshots each prove different things. Return changed contracts/paths, actual checks/results and remaining gaps, not a list of tools that might be run.

## Web/client adapter

- Implement approved tokens, components and copy; resolve missing interface contracts before inventing client-side substitutes.
- Preserve native form/link/button behavior, labels, keyboard/focus, sensible autocomplete/inputmode and relevant accessible state announcements. Use the design craft state/content checks alongside the happy path.
- In React, derive values from authoritative state rather than mirroring them through effects. Put user-triggered work in the appropriate event flow, clean up subscriptions/async work, and keep stable identity where correctness requires it. Do not add memoization everywhere or suppress hydration warnings to hide an unexplained mismatch.
- Keep request-specific/user data out of shared SSR module state. Start independent I/O together where correct; avoid unnecessary client waterfalls, shipping server-only code/secrets and unused heavy packages. Reserve image geometry and load only needed font styles. Measure expensive interactions before adding complexity.
- For Swift/native, inspect actual compiler/deployment settings, use clear state ownership and appropriate value types, respect actor isolation/cancellation and re-check assumptions across suspension. Do not silence races with unsafe annotations/casts or block the UI just to remove a warning. Use the target platform's accessibility and lifecycle tools.

## Server/data adapter

- Enforce validation, authentication and object-level authorization at the actual mutation boundary; client validation is only feedback. Treat URL parameters, remote/provider results, uploads and persisted inputs according to their trust level. Do not leak secrets or private payloads in errors/logs.
- Preserve public response/error/persistence semantics and update affected consumers deliberately. Show response plus stored side-effect evidence for persistence claims. Test malformed/unauthorized requests, partial failure, duplicates and concurrent updates when those can corrupt data or repeat effects.
- Keep mutable per-user state isolated and caches keyed deliberately. Preserve atomicity or transactional behavior where required by the domain. Add idempotency/retry mechanisms for actual duplicate-effect risks, not a generic platform for every endpoint. Bound retries/timeouts and avoid retrying an uncertain non-idempotent write blindly.
- Keep previous valid records through migrations until the replacement is durably confirmed. Define recovery for interrupted changes. Never turn caught write errors into a success result or delete the only valid copy to make the new schema look clean.

## Review adapter

Prioritize correctness, contracts, data integrity, accessibility and demonstrated performance risk. Inspect the integrated actual version and current criteria. A style preference is not a demonstrated defect; an official example is not automatically safe. Re-run disputed checks and keep unrun/failed evidence visible. Do not invent a quota of findings, impose function-length thresholds or require a pattern such as SOLID to justify unnecessary rewrites. See [craft sources](craft-sources.md).
