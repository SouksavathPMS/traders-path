---
tags: [system]
---
# Style Guide · the mindset flow

Every lesson follows the same flow so the reader learns **how to think → what it is → how to act → why it works**.

| # | Block | Callout | Purpose |
|---|---|---|---|
| 1 | Mindset | `> [!mindset]` | The one idea to hold in your head before anything else |
| 2 | Concept | `## ...` sections | What it is, in plain words |
| 3 | Visual | `![[figure.en.svg]]` | Infographic or annotated chart — every lesson has at least one |
| 4 | Example | `> [!example]` | A concrete chart / candle / number |
| 5 | Action | `> [!action]` | Numbered steps: what to actually do |
| 6 | Why | `> [!why]` | The logic behind it (who is buying/selling and why) |
| 7 | Mistakes | `> [!warning]` | Common traps |
| 8 | Practice | `> [!practice]` | A task to do on a real chart + checklist |

## Bilingual rules
- One note per lesson. English block starts with `%% EN %%`, Thai block with `%% TH %%` (Obsidian hides these markers in reading view; the site builder uses them to split languages).
- English is the master. Thai mirrors it section for section.
- Keep trading terms in English inside Thai text on first use, with a Thai gloss: *แนวรับ (Support)*.
- Figures come in pairs: `name.en.svg` and `name.th.svg`, generated from one spec in `_tools/figures/`.

## Quiz blocks (checkpoints)
````
```quiz
Q: Question text
- wrong answer
* correct answer
- wrong answer
E: Explanation shown after answering
```
````

## Frontmatter
```yaml
id: "1.3"
phase: 1
status: stub | draft | done   # only "done" lessons are published on the site
tags: [phase1, candlestick]
```

---

# v2 · The deep-explanation layer (added Oct 2026)

**Why:** the first version of every lesson was written for someone who already trades. A reader who knows nothing should be able to follow *every* lesson without opening another tab. v2 adds a beginner layer **on top of** the existing content — nothing is deleted.

## The reader we write for
*"Smart, motivated, zero finance background, reading in their second language."* If a 16-year-old who has never opened a chart can't follow a paragraph, it needs one of the blocks below.

## New blocks (in this order inside a lesson)

| Block | Callout | Where | Rule |
|---|---|---|---|
| Plain words | `> [!eli5]` | right after `[!mindset]` | 3–6 sentences, **zero jargon**, no numbers needed. Explain *what problem this tool solves*. |
| Key terms | `> [!terms]` | right after `[!eli5]` | Every acronym and technical word used in the lesson, defined in one line each. Format: `- **Open interest (OI)** — how many contracts are still open…` Link earlier lessons: *(see 8.1)*. |
| Analogy | `> [!analogy]` | next to the hardest concept | One everyday picture (insurance, a thermostat, a shop, traffic). Say where the analogy **breaks**. |
| Walkthrough | `> [!walkthrough]` | after each formula or mechanism | Numbered steps with **small round numbers** a reader can verify on a phone calculator. Show every intermediate result. End with "So what?" — what the number means for a decision. |
| Across markets | `> [!market]` | where behaviour differs | One line each for Forex / Gold / Stocks / Crypto when the concept works differently there. |
| Risk warning | `> [!caution]` | leverage, options, crypto, news | What can go badly wrong and how big the loss can be. |
| Self-check | `> [!check]-` (folded) | end of each major section | 2–3 questions written as `**Q1.**`, `**Q2.**` (not `1.` — numbered lists break around nested answers); each answer inside a nested folded `> > [!answer]-`. |

Example of a folded self-check:

```markdown
> [!check]- Check your understanding
> **Q1.** A dealer is short calls and the market rises. Do they buy or sell futures?
> > [!answer]-
> > Buy. Their short calls gain delta as price rises, so they need more long futures to stay neutral.
```

## Quality bar for every lesson
- [ ] No acronym appears before it is spelled out (in this lesson or in `[!terms]`).
- [ ] At least **2 worked examples with numbers** (one simple, one realistic).
- [ ] At least **one figure per major section**; mechanisms get a diagram, price ideas get a candlestick chart.
- [ ] Every formula is followed by a `[!walkthrough]`.
- [ ] One `[!check]-` per major section.
- [ ] Thai mirrors **all** of the above (TH can be slightly longer; keep the English term in brackets on first use).
- [ ] The lesson still works if the reader skipped the previous phase: link back with *(see X.Y)* instead of assuming.

## Lessons upgraded to v2
Tracked in [[Lesson Audit]].
