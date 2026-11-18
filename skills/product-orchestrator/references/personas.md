# Registered specialist roles

The canonical role instructions are in the bundled TOML files below. Install them under `~/.codex/agents/` for cross-project use. Each is standalone: Codex reads `name`, `description`, and `developer_instructions`. File presence is not evidence of discovery in an already-running session. Use the actual role/tool inventory; fall back to a generic agent with the same instructions when necessary.

| Role | Canonical instructions | Boundary |
|---|---|---|
| Orchestrator | [product-orchestrator](../agents/product-orchestrator.toml) | Normally the main chat; coordinates every relevant specialist and owns final acceptance |
| Product | [product-strategist](../agents/product-strategist.toml) | User outcomes, missing decisions, scope and testable criteria |
| Web design | [web-designer](../agents/web-designer.toml) | Websites/web apps, including responsive mobile browser layouts |
| Mobile design | [mobile-designer](../agents/mobile-designer.toml) | Native iOS/Android navigation, gestures, safe areas, keyboard/device and accessibility states |
| Copy | [product-copywriter](../agents/product-copywriter.toml) | Exact text tied to real behavior; implementation owner integrates it |
| Frontend | [frontend-engineer](../agents/frontend-engineer.toml) | Existing web/native client stack, agreed contracts and complete interactions |
| Backend | [backend-engineer](../agents/backend-engineer.toml) | Server validation, API/persistence contracts and data integrity |
| Verification | [product-verifier](../agents/product-verifier.toml) | Separate read-only acceptance pass against current criteria and artifact |

Read the relevant TOML before dispatching a fallback. Inherit models and permissions unless explicitly configured otherwise. Role boundaries, including read-only review, are behavioral instructions; they do not create new sandbox guarantees. Designers normally supply direction and review rather than competing with the frontend owner for UI files. Only the lead accepts changes to scope, criteria and shared contracts.
