# Spiral

Spiral is a Codex skill for taking a product idea from the first conversation to a working milestone.

## Why I built it

I wanted Codex to challenge my product ideas before building, bring in outside perspectives, and give me real alternatives to choose from. Once we agree on a direction, I want the team to work independently and bring me back when there’s a decision to make or something working I can try. I’d rather start with one polished flow and carry the lessons from building it into the next run.

## How it works

1. **Clarify the brief.** For a rough idea, the lead interviews you, challenges consequential assumptions, and brings in relevant research. For a major interface change, it asks you to choose among distinct directions. A specific fix can go directly to reproduction and replay.
2. **Build a working slice.** The lead owns the criteria and interfaces. It assigns scoped work to product, web or native mobile design, copy, frontend, and backend roles as needed. Backend work starts by tracing the existing system and reviewing consequential architectural choices before dependent edits.
3. **Verify and repair.** A separate verifier drives the integrated artifact against the current criteria. Failed checks return to the owner for bounded repair. The evidence script checks that required results belong to the recorded artifact and criteria.
4. **Carry forward what worked.** The lead records demonstrated lessons with the project. A mapped Notion project can hold nested documents for vision, research, decisions, and delivery evidence.

```mermaid
flowchart TD
    User["Product owner"] --> Lead["Codex lead"]
    Lead --> Discovery["Discovery and direction"]
    Discovery -->|Major interface choice| User
    Discovery -->|Confirmed brief| Team["Selected specialists"]
    Team --> Integrated["Integrated milestone"]
    Integrated --> Verifier["Independent verifier"]
    Verifier -->|Findings| Lead
    Lead -->|Scoped repairs| Team
    Verifier -->|Required checks pass| Review["Working milestone for review"]
    Review --> User
    Lead --> Records["Project notes and tested lessons"]
    Records -->|Context for the next run| Lead
```

The lead chooses from product strategy, web design, native mobile design, product copy, frontend engineering, backend engineering, and independent verification. Role instructions set concrete expectations for accessible interactions, state and error coverage, readable code, and copy that preserves meaning. [Roles](skills/product-orchestrator/references/personas.md) · [Task playbooks](skills/product-orchestrator/references/task-playbooks.md) · [Evidence recipe](skills/product-orchestrator/references/verification-recipe.md)

## Install

With Codex and Python 3.11 or newer, clone the repository and run the installer:

```sh
git clone https://github.com/nicocampanell/Spiral.git
cd Spiral
python3 skills/product-orchestrator/scripts/install.py
```

The installer registers eight Codex roles, installs the `product-orchestrator` skill, and updates its managed section in your Codex `AGENTS.md`. It backs up changed existing files. Start a fresh Codex session to load the roles.

In Codex, invoke `$product-orchestrator` with your brief. A mapped Notion workspace is optional. With no connection, the lead can use local project notes and evidence.

Models and native agent capabilities depend on your Codex host. The [model routing guide](skills/product-orchestrator/references/model-routing.md) explains the default tiers and fallbacks.

## Check the package

```sh
python3 -m unittest discover -s skills/product-orchestrator/tests -v
```

The tests cover installation, preservation of existing guidance, and evidence validation. The [evaluation scenarios](skills/product-orchestrator/evals/) cover routing, review, and role-specific craft.

## Roadmap

The current skill coordinates work during an active Codex session. Future work includes validated run-state transitions, recovery from interruptions, and optional release integrations. A separate evaluation track will compare representative work with and without Spiral.

## Sources

pstack informed task routing, scoped delegation, and the verification recipe. Oh My Claude Code informed the staged delivery and repair loop. The repository includes selected upstream sources with their original MIT notices. [pstack sources](skills/product-orchestrator/references/upstream-pstack/README.md) · [Oh My Claude Code sources](skills/product-orchestrator/references/upstream-omc/README.md)
