# Run 01, S0: the criteria sheet (frozen)

> **Frozen 2026-09-14** (S0 step 7). Every value comes from `submarket_selection.md` §4 S0, which records the founders' decisions verbatim with the research behind them (S0.1-S0.4). The evidence checks are `research/s0_check_A_ambition_economics.md`, `research/s0_check_B_structure_access.md`, `research/s0_check_C_durability.md` and `research/s0_check_D_fragmentation_incumbents.md`.
> **Gate:** this file exists, so candidates may now be scored (S0 output).
> **Changing it:** log the change and its reason in `submarket_selection.md` §9, then strike the old value through here and add the new one with its date. Never delete.

## 1. Ambition (S0 step 1; F-1 to F-4, F-12)

| Item | Run 01 value |
|---|---|
| Floor | $2.5M yearly revenue by year 5 |
| Stretch | $10M yearly revenue: an upside the market must allow. It is scored under A1 and A6, not used as a knock-out |
| Clock | 5 years, starting at product launch |
| Funding | Self-funded, with early revenue from paying design partners |
| "Profit" and "valuation" | Profit means the company's profit (the founders' personal take-home goal is at least $250K within 5-7 years). Valuation means the price another company would pay to buy it |
| K5 size floor | A candidate's yearly fee pool of about $25M or more: the $2.5M floor at a 10% market share **[our call]** |
| Expansion | Vertical first, then horizontal |

## 2. Team inventory and personal filter (S0 steps 2-3; F-15, F-16)

- Freight knowledge and contacts are limited today. Domain immersion comes after sub-market and segment selection, before the software is built. Until then, W2 will score low for every candidate.
- Personal filter: nothing is off the table, so K9 passes for every candidate.

## 3. Knock-outs (S0 step 4; `submarket_selection.md` §5.1)

Each candidate gets pass, fail or unknown at S2. Unknowns go forward flagged and are settled in S3. Until the entry side is chosen (Q6), the side-specific knock-outs K10 and K11 remove a card only if both sides fail (C11). *Run 01 note, 2026-09-15:* under this rule no card failed K10 or K11 Test 1, so both worked as pass-throughs. The founders may reconsider how they work (`submarket_selection.md` §9, T15).

| # | Test | Passes when |
|---|---|---|
| K1 | Distinct and internally alike | Members share needs, and the candidate clearly differs from its neighbours |
| K2 | One market on each side, and not too big | Same product, same sales process, and word of mouth on each side; not so big that buyers stop talking to each other. A fail means split the card. *Clarified 2026-09-15 (C12):* a card that is one market but too big for word of mouth is flagged S, and is split into segments at segment selection (Q6), because the project targets segments |
| K3 | Identifiable and reachable | We can name the buyers and reach them at an affordable cost |
| K4 | Measurable | Buyer counts and the savings pool can be estimated from named data |
| K5 | Big enough | A yearly fee pool of about $25M or more (fee potential, not headcount). *Desk rule added 2026-09-15 (C13):* pass if a 10% fee share of the savings range's low end reaches $25M; fail if a 35% share of its high end is clearly short; unknown in between. Within a few percent of $25M counts as "about", so it is unknown, leaning fail |
| K6 | Software can fix it | The target cost comes from information, coordination or paperwork, not from trucks, fuel or roads |
| K7 | Saving measurable and attributable | There is a countable outcome with a baseline, and customers would credit software for it |
| K8 | Someone can and will pay | A party holds a budget, sees the saving on its own P&L, and could buy from a startup |
| K9 | Team would commit | Passes the personal filter (every candidate passes in run 01) |
| K10 | Not in the "land of the giants" | The top 50 firms hold 75% of the side's revenue or less. Above 85% fails. Between 75% and 85% is unknown, and S3 settles it: fail if firms under 500 employees hold less than 20% of the side's revenue (Census SUSB). Use 6-digit industry codes where they exist. *Flagged for review 2026-09-15 (T15):* a pass-through at sub-market level in run 01 |
| K11 | Durable | **Test 1, no projected shrinking:** the BLS 10-year employment or output projection is 0 or higher; the census firm count in 2022 is at least the 2017 count; and no primary source shows a substitute doing the job at scale within 5 years of launch. Fail if two of the three point to decline. **Test 3, no drastic fall in the unit a fee would be counted on** (invoices, loads, customs entries, claims, detained stops): pass if it fell 13% or less from peak to trough in both 2008-09 and 2022-25, or rose; fail if it fell more than 20% in either; 13-20%, or no data, is unknown. *Flagged for review 2026-09-15 (T15):* Test 1 was a pass-through at sub-market level in run 01. *Practice added 2026-09-15 (C15):* see `submarket_selection.md` §5.1, K11 |
| — | Flag, not a knock-out | K11 Test 2, customer survival: the firm death rate against the economy's (Census BDS, 2009 and 2023), the entry rate against the exit rate, and the firm count. Recorded in S3 item 8 |

## 4. Weights (S0 step 5; F-13, F-14)

### Axis A, "is it worth winning?" (100 points)

| Row | Criterion | Weight |
|---|---|---|
| A1 | Savings pool and fee potential | 20 |
| A2 | Fit for automation | 10 |
| A3 | Pain and urgency (per side) | 25 |
| A4 | Fragmentation ~~(per side)~~ *(changed 2026-09-16, C19: scored on the side that would pay, not the better side; until the entry side is chosen, use the side the fact sheet names as the budget holder, and record the other side beside it)*. Top-50 share band: under 20% = 1, 20-80% = 0.5, over 80% = 0. Add 0.5, capped at 1, if firms under 20 employees hold 25% or more of the side's revenue | 15 |
| A5 | Frequency and recurrence | 15 |
| A6 | Expansion leverage: vertical first, then horizontal | 15 |
| ~~A7~~ | ~~Durability~~: now knock-out K11 | — |

### Axis W, "can we win?" (100 points)

| Row | Criterion | Weight |
|---|---|---|
| W1 | Access and cost to reach (per side) | 20 |
| W2 | Team knowledge and access | 5 |
| W3 | Whole product and time to value | 20 |
| W4 | Competition and substitutes. Do customers already pay for the job (a service firm, software or staff time)? Is today's software for it weak, legacy or missing? Both = 1, one = 0.5, neither = 0. The incumbent map (vendor count, the leader's share, service firms, how the job is done today) is recorded as evidence, not scored | 15 |
| W5 | Willingness to change (per side) | 15 |
| W6 | Time and resources to win | 25 |

**Balance check (R12): passes.** The long-term rows (A5 + A6) carry 30 points against 45 for the short-term rows (A1 + A3). Axis W holds the criteria about us.

## 5. Scales and rules (S0 step 6; confirmed 2026-09-14)

- **Scores:** 1 / 0.5 / 0 at the desk stage; 1-10 after the S5 interviews.
- **Adding up:** add weight × score within each axis. The two axes stay separate and are plotted, A going up and W going across, with bubble size showing fee potential.
- **Two sides:** per-side rows are scored for both the shipper side and the freight-company side; each axis total uses the better side (C5). *Changed 2026-09-16 (C19):* **A4 is the exception** and is scored on the side that would pay.
- **Show-stopper veto:** a show-stopper on any row drops the candidate. On W4 this includes one vendor already serving more than half the target customers for the job, with those customers satisfied (C10).
- **Checks after scoring:** Cohen's multiplicative score for each paying side; Gurley's 10-factor count for candidates that match buyers with sellers.
- **Fee feasibility (F1-F5):** a separate gate and plot marker. F1-F4 totalling 3 or more = a savings-share fee is plausible; 2-2.5 = plan a hybrid; below 2 = flag it.
- **Sensitivity (S4 step 5):** recompute the ranking with each founder's own split; with the first split, 40/45/15 (A1 40, A4 45, A6 15, all other rows 0); and with the strict durability test (an average revenue fall in downturns of 8% or less passes, above 13% fails).
- **Modelling assumptions, not decisions** (§10): a market share of 10% for the floor test, and 20% or 35% for the stretch; the fee share of savings modelled at 10%, 20% and 35%.
- *Added 2026-09-15 (C16-C18; adopted by the founders at S3b):*
  - **A3 at desk level:** 1 needs a dated rule, rule change or crisis that acts on the card's own job. Triggers that act on the whole market or on a neighbouring job, or that are still pending, score 0.5 (C17).
  - **Score the job:** each card's job is scored as its sentence defines it. Where the first product (the wedge) would change W3 or W6, the effect is recorded as a sensitivity (C18).
  - **The S3b cut:** S3b cuts to 4-6 by the sum of the two axes, at the first clear break (C16).
- *Added 2026-09-16 (C19-C21; adopted by the founders at S4):*
  - **A4 is scored on the paying side** (C19). Run 01 re-scored: C-08's A4 goes 1 → 0.5 and its Axis A 100 → 92.5; no other shortlisted card moves.
  - **Single-point dependencies** are recorded on the fact sheet (C20).
  - **S5 coverage depends on what each side is** (C21): full interviews on a side that could buy from us, documented position plus 1-2 interviews on a counterparty-only side.
- *Added 2026-09-22 (C22; adopted by the founders after the C-09 practice audit):*
  - **Every card going to S5 carries a per-customer profit model and a kill condition** (S4 step 7): three bands on the measured leak rate, on document access and on measured cost to serve, fixed before the S5 assessment and entered in the gate tracker. Run 01 applies it late, to the four finalists: `4_kill_conditions.md`.
- *Added 2026-09-22 (C23-C25; adopted by the founders after the S4 step 7 results, D-22):*
  - **The ceiling test** (C23): a card is eliminated at S4 step 7 only if it fails the per-customer test even with every unmeasured input at its most favourable value.
  - **Labour savings under the fee rule** (C24): a labour saving counts only where the customer shows it converts into cash, priced per unit as a stated share of the measured minutes. The founders also will not build software whose saving is cutting paid hours.
  - **S4.5 Profitability check** (C25): before S5, audit every public source on the per-customer model's deciding inputs and give a verdict: proven profitable, proven unprofitable, or not provable from the web. Bar: on *verified* or neutral inputs only, positive gross profit, a $5-15k acquisition cost repaid within 12 months, and enough such customers for $1M at a 10% share and $2.5M at no more than 35%. Run 01 applies it to C-19 first: `4_5_profitability.md`.
- *Added 2026-09-22 (C26-C27; adopted by the founders after S4.5 on C-19):*
  - **Screen before the savings assessment when the leak is concentrated** (C26). Run 01, C-19: the look-back runs on a recruit reporting non-trade deductions of 1% of sales or more. Screen yield and new-money share are recorded.
  - **C-19's pass line re-derived** (C27): ~~0.17%~~ → 0.22% of sales at a $50M supplier, on S4.5's 12-month payback bar, with a table by size. The kill line stays 0.05%.
- *Added 2026-10-09 (C29; adopted by the founders: "Adopt the Kill/Cover/Pass lines"):*
  - **C-09's kill condition re-set on the software basis** (D-23). Test 1: the flagged rate on in-window spend against Kill / Cover / Pass lines read at the shipper's size (at $1.5M: under 0.044% / 0.51% / 6.44% or more); between Kill and Pass, a pilot settles follow-through. Test 2 unchanged. Test 3: the customer's timed hours against its capacity. Replaces the 2026-09-22 lines: `4_kill_conditions.md` §2.5.12.

## 6. Deferred to segment selection (Q6)

- Which side to sell to first (F-5), and the firm-size floor (F-6).
- Fee per customer (F-7), fee share of savings (F-8), and the W1 channel rule (parked change 5).
- Whether our revenue swings with freight volume, which depends on the fee design (O-3).
