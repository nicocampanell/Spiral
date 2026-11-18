# Backend architecture checkpoints

Use the relevant checkpoints for new backends and changes to API contracts, data ownership, persistence, identity, external integrations or deployment topology. For a local fix with no architectural impact, trace the affected path, check its contracts and run a focused verification. The lead resolves routine engineering decisions. Bring the project owner in when a decision changes the product, materially changes cost or operations, or depends on information only he can supply. Pause affected work at an unresolved checkpoint and continue independent work.

## 1. Map the actual system

Start read-only. Find the repository instructions, workspace boundary, manifests, lockfiles, runtime versions, CI and deployment definitions. Follow the current entry point through authentication, routing, domain logic, storage and any external effects. Read schema and migration history, affected callers, tests and existing decisions. Use file paths as evidence. When docs and code disagree, record the discrepancy and distinguish what is checked in from what is known to run in production. Inspect configuration names and examples without exposing secret values.

Record the actual stack, deployment shape, authoritative data stores, module owners, local run/test commands, and a baseline check where feasible. Label missing access and unverified assumptions. Classify the work as an extension, a migration or a new backend. An empty directory or inaccessible service does not establish the absence of an existing backend.

## 2. Decide the stack and review the design before dependent edits

Write a short architecture decision in the existing decision log or run record. Include the requirements that drive it, what you will reuse, the selected tools and why they fit, the strongest alternative for any consequential choice, and the evidence that would change the decision. The existing codebase, available team skills, hosting constraints and compatibility matter as much as benchmark numbers.

| Decision | Start here | Add or change when |
| --- | --- | --- |
| Runtime, framework and deployment | Extend the running application. For a new product with server needs, start with one deployable app and clear module boundaries. | A verified requirement calls for separate scaling, isolation, ownership or a different runtime. Check the target host's timeouts, concurrency, connection and filesystem limits. |
| Database and migrations | Reuse the authoritative store and migration tooling. For new durable relational data, evaluate a transactional relational store. SQLite can fit a single writer deployment with durable local storage. A managed relational service can fit shared access across instances if cost and operations fit. | The access pattern, concurrency, durability, or operations demand a different store. Name the source of truth and how to restore it. |
| Identity and storage | Use established identity/session controls. Use existing blob storage for files if local filesystem durability or instance sharing is insufficient. | A concrete access, privacy, retention, size or deployment requirement calls for a change. Evaluate who can access records and objects, and how deletion works. |
| Background work, cache and search | Keep the request path direct and bounded. Use the datastore's existing query/index capabilities and the platform's existing job tooling where suitable. | User flows need durable asynchronous work, measured contention needs a cache, or required search behavior exceeds the store. Specify delivery, retry, invalidation and failure behavior for anything added. |

Check official docs against the project's actual versions for any new dependency or provider choice. Compare maintenance, operational burden, cost, limits, portability, failure handling and local/CI support. Choose only the tools the design needs. Workload estimates should identify assumptions about peak traffic, data growth, latency and acceptable downtime or data loss. Avoid precision the brief cannot support.

Sketch one changed path from caller through the server to the source of truth and response, including any job or vendor boundary. Agree with affected owners on the request, result and error contracts, ownership and authorization checks, consistency needs, and behavior when operations fail or their outcome is unknown. Define data invariants and where they are enforced. For breaking releases or migrations, record compatibility during rollout, how prior data stays intact, rollback or forward recovery, and how success will be checked. For consequential boundaries, have an independent reviewer assess the design and resolve blocking gaps before dependent implementation starts. Record who reviewed and any remaining assumptions.

## 3. Prove a vertical slice

Implement one representative path through the actual entry point, authorization, business logic, storage and consumer. Run it against isolated local or test resources with representative data. Check the success path and the most important failure case, such as an invalid request, denied access, a duplicate write or a failed dependency. Confirm durable effects by reading them back. Use the existing test and migration tools. For a new backend, record a reproducible setup with pinned runtime and dependency versions, example configuration with placeholders, local dependencies, migration and test commands, and synthetic data where needed.

Capture the first measurements that address the project's bottleneck. Examples include query count and plans, representative response latency, connection demand, and memory or queue growth. Bound list sizes and external calls where the usage requires it. Check for unnecessary round trips, repeated queries and material input sizes before adding infrastructure. Record the workload alongside numbers. A local test gives evidence for that workload. If the slice exposes a bad assumption, revise the architecture decision and affected criteria, then rerun the relevant checks before extending the pattern.

## 4. Check integration and readiness

Have the verifier exercise current contracts and real persistence, plus material authorization, retries, concurrency and partial failures. For schema or deployment changes, rehearse with disposable representative data and check compatibility, interruption and recovery. Verify the expected deployment configuration and permissions, health signals and useful logs or metrics without sensitive data. Confirm who handles failures and where to find the runbook when the feature adds operational responsibility. Record evidence, gaps and the exact version reviewed. A failed or unrun required check holds the affected milestone. Production actions still follow the task's authorization.

Keep the architecture decision and diagrams in the repository's existing location when there is one. Link or summarize them in the project's Notion **Design & Decisions** document and put actual test and readiness evidence in **Delivery & Verification** when those documents are in use.
