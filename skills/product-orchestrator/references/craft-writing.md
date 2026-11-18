# Product writing and Humanizer pass

Use Humanizer's structural editing ideas together with interface-writing practice. The goal is clear, specific writing in the product's voice, preserving what is true. Do not claim to detect authorship, evade detectors or make every brand casually conversational. This is an embedded pass: deliver the final copy or useful surface/state mapping, not a transcript of draft/rewrite steps.

## Write for this reader and action

- Read nearby copy, terminology, style guidance and a supplied voice sample first. Match the product's voice; adjust tone to the stakes. Keep errors/destructive/security copy calm and explicit. Warmth or personality must not obscure an instruction or consequence.
- Use concrete ordinary words, clear actors and direct actions. Prefer a concrete verb-first button such as “Save draft” or “Delete project” to “Let's go,” “OK” or an ambiguous “Yes.” Use one term per object/action across the flow; interface consistency can matter more than varied vocabulary.
- Preserve supported facts, names, numbers, units, dates, qualifications, uncertainty, citations and action consequences. Do not invent specificity, testimonials, first-person experience, human research, figures or claims about privacy/security/persistence to sound credible. Verify that a claim is supported before strengthening it.
- Preserve code, commands, URLs, identifiers, placeholders and localization syntax. Use complete templated sentences and proper pluralization, not concatenated fragments. Match the target format's typography; never smart-quote code or break variables. Preserve the existing voice sample's intentional punctuation.

## Remove AI-shaped filler

Look beyond a blacklist. Cut staged openers, redundant section summaries/closers, unsupported significance, generic sales language, vague borrowed authority, decorative bold/emoji labels and chat wrappers. State the point directly instead of repeatedly contrasting it with an alternative nobody proposed. Reduce forced triads, uniform sentence openings and dash-heavy cadence; keep real contrasts, meaningful lists and natural emphasis.

Read the complete passage, revise around its main point, then compare facts and qualifiers against the original. Read for cadence and comprehension. Do not replace weak claims with fabricated numbers, remove meaningful caveats, turn uncertainty into certainty or flatten all voice into short choppy sentences. Necessary repetition in interface labels is useful, not a writing defect.

## Complete product states

- Field labels persist after typing; placeholders supply examples, not the only name. Link text names its destination and remains meaningful in a screen-reader link list. Settings describe the enabled state without double negatives.
- Errors identify the actual problem and a usable correction/retry. Do not blame the person, joke about data loss or invent a network cause from an unknown failure. Put field-specific guidance beside the field and coordinate its accessible association/announcement with frontend.
- Distinguish first use, no results and failed loading. Give empty states orientation plus a relevant next action. Keep progress feedback accurate and non-repetitive. Confirm success only after the actual operation succeeded; saved locally, sent and durably synced are different claims.
- Destructive confirmations state the object and consequence and offer clearly named actions. Preserve domain-required notices and precision. A Humanizer pass cannot remove a legal, safety or data-loss qualification just because it sounds formal.
- Check copy against the real action/state, supported content lengths and localization. Source review can establish wording; rendered layout, announcements and backend behavior need their own checks.

## Return

For UI work, return final text keyed to surface/state or localization key, with only material assumptions/questions. For prose, return the revised passage with necessary source links. Keep an explanation only when the caller needs a factual or voice decision. The root lead writes canonical Notion material; specialists send proposed text.

Adapted from [Humanizer](https://github.com/blader/humanizer/blob/b48c832f0f809c1b5658edbb838c2521b72f2413/SKILL.md), the installed better-writing skill and [Vercel writing guidance](https://github.com/vercel-labs/writing-guidelines/blob/83e2316b034cf572400513538e4e4da01c4cc742/command.md). Conflicts and scope are recorded in [craft sources](craft-sources.md).
