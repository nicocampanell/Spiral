# Model routing

Spiral's default is a stronger orchestrator and final reviewer, with lighter focused builders. These are task roles, not a promise of measured cost or quality gains.

The installed role defaults use the requested GPT-6.2 Astra lead and reviewer tier:

| Roles | Model | Reasoning |
|---|---|---|
| product-orchestrator, product-verifier | `gpt-6.2-astra` | `medium` |
| product-strategist, web-designer, mobile-designer, product-copywriter, frontend-engineer, backend-engineer | `gpt-6.1-terra` | `medium` |

Use the actual runtime allowlist/catalog, not a model name copied from a current web page into an older client. Recheck availability after client/account changes. If a configured model is unavailable, disclose it and use a supported comparable role or the selected model; do not silently misrepresent the tier.

A custom agent file sets a subagent's model. It does not switch the current main chat's model. Keep the main chat as lead when it already uses the desired stronger model. Where the CLI offers GPT-6.2 Astra, start a fresh lead with `codex -m gpt-6.2-astra -c model_reasoning_effort=medium`. In the app, choose GPT-6.2 Astra in the model picker. If the current chat uses another model and native delegation is available, it may delegate one coherent workstream to `product-orchestrator`, remaining the user liaison and canonical record owner; account for that extra slot rather than running two competing leads.

Use registered configurations when available. If falling back to a generic spawn, set supported model AND reasoning values together from this policy, unless the user gives a different instruction for that task. Use an isolated fork when the current runtime requires it for overrides. Do not override the user's explicit model choice or global configuration merely to satisfy a role name.

Promote a task only for a concrete reason such as repeated unproductive attempts, consequential architecture or conflicting evidence. Preserve attempt counts. Do not spawn every specialist at the strongest tier. Different personas on one model are complementary lenses, not independent model-family verification.

Official guidance: [Codex custom agents and configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents), [model selection](https://learn.chatgpt.com/docs/model-selection). Model availability comes from the local catalog; recommendations remain a starting point to evaluate on representative tasks.
