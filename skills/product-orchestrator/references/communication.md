# Team communication

Use Codex's available native collaboration tools. The workflow adds message meaning and authority boundaries, not a new transport or message server.

## Roster and brief

The orchestrator keeps task ID → role → actual agent ID → owned paths → dependency/status in the run record. Include the lead's address and any relevant peer addresses in the brief. Do not invent tool names, claim access to unrelated chats, or assume all siblings can communicate. When peer access is unavailable, the lead relays the question and response.

## Useful messages

Messages can be plain language; keep the task ID and action clear.

- **Ready:** dependencies have arrived; name the governing contract/criteria revision.
- **Question:** ask one concrete question, name the affected task/interface, and explain whether it blocks work.
- **Contract change:** describe the proposed difference and affected owners. The lead settles it and sends the governing decision to each affected agent before dependent edits proceed.
- **Blocked:** state the actual missing input/capability, evidence, and the smallest next action. Continue unrelated owned work if possible.
- **Handoff:** give current files/diff, decisions, remaining work, actual checks and used repair rounds. The lead confirms the old writer is stopped before assigning a new owner.
- **Ready for verification:** name the artifact, criterion IDs/revision, actual checks/results and known gaps. This means author work is ready to inspect, not accepted.

The lead can talk to all agents it coordinates and is accountable for unresolved messages. Specialists may clarify bounded facts directly with a named peer when supported. Copy the lead on decisions affecting shared contracts, scope, criteria, file ownership or another agent's deliverable. Peer conversation does not authorize either agent to edit the other's files.

## Lifecycle and disagreements

Use the runtime's message operation to steer a running agent. Use a turn-triggering follow-up to resume an idle one; a queued message alone may not restart it. Use waits while genuinely idle rather than polling repeatedly. A silent worker is not automatically a failed worker: inspect observed progress and request a concrete status before replacing it.

When advice conflicts, compare it against the current user outcome, platform conventions, established project patterns and observable evidence. Keep genuine tradeoffs visible; choose reversible implementation details yourself, and ask the user when the decision materially changes the product. A reviewer cannot vote away a reproduced failure, and a majority of specialist opinions does not establish user research.

At cancellation or scope change, notify all affected running agents and settle stale writes. If replacing a worker, preserve its artifacts and repair history, stop it, then transfer ownership. Do not let a late result silently replace a newer contract or approve an old criterion revision.
