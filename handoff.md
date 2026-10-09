# Handoff: kill conditions for C-11, C-19 and C-20 (run 01, S4 step 7)

> **Status: done 2026-09-22.** §3-§5 of `research/selection_runs/run-01/4_kill_conditions.md` are filled, with a side-by-side of the four cards (§6) and the founders' elimination decision, D-22, left open (§7). The lines are proposals until the founders adopt them.

> **Written 2026-09-22 for a fresh Claude Code chat.** Read `CLAUDE.md` first, then this file, then the files in §3. Do not start with web research; the desk evidence you need is already in the repository.
> **Your deliverable:** fill §3, §4 and §5 of `research/selection_runs/run-01/4_kill_conditions.md`, one section per card, in the format of §2 (C-09, the worked example), and update the four places listed in §6 below.
> **What you must not do:** re-score any card, change any threshold in C-09's section, make the S6 decision, contact anyone, or finalize anything on the founders' behalf. Decisions are theirs; you write the evidence and a suggested line, marked **[our call]**.

## 1. Where the project stands

- The project is choosing a freight sub-market where software can cut a measurable cost, so that a fee can be charged out of the saving (`CLAUDE.md`, "Constraints"). The process is S0-S7 in `submarket_selection.md` §4.
- Run 01 is at S5 (validation by interviews), with four finalists sent forward unranked: **C-09** checking and paying freight bills, **C-11** LTL class and reweigh disputes, **C-19** retailer on-time-in-full fines and deductions, **C-20** import entries. On 2026-09-17 the founders named C-09 the front-runner as a working bet (option B), not the final choice.
- No interview has happened. The S5 gate tracker (`5_validation.md` §8) reads zero on every item.

## 2. Why this step exists, and what the founders decided

Through S4 the scoring measured how big each card's savings pool is (A1, K5) and whether a share-of-savings fee is chargeable in principle (F1-F5). **It never measured whether one customer pays more than it costs to serve.** That question was first asked for C-09 at S6 (`6_focused_target.md` §4.4), and the answer, with a practice audit of 101 real carrier bills, was that at the desk's central rates a typical C-09 customer never pays back its acquisition cost. Every "money back" card in this run has come in under its desk estimate as evidence improved.

The founders' decision on 2026-09-22 (`4_scorecard.md` §9.1, D-21), verbatim:

> "Adopt the Kill Condition, this is going to be part of S4, for subsequent runs, but we are going to run it against all of our remaining candidates now. You will not run this on C-11, C-19, and C-20 but you will prep another Claude Code chat to do so with a handoff.md including the process and why this is relevant"

It is adopted as process change **C22** (`submarket_selection.md` §9; §4 S4 step 7). The point of a kill condition is Dolnicar's and the DPM's principle P1: fix the line **before** the measurement, so the result cannot be argued into a pass afterwards. It is relevant now because S5's savings assessments are about to produce the first real numbers, and without a line fixed today those numbers would be judged after the fact.

## 3. The step you are running (S4 step 7, C22)

Full text: `submarket_selection.md` §4 S4 step 7 and `4_kill_conditions.md` §1. In short, for each card:

1. **Build the per-customer chain** from the fact sheet's fee unit (S3b item 10) and savings pool (item 2): fee = unit volume per customer × leak or waste rate × share software removes × share actually realised × fee share; gross profit = fee − cost to serve. Use the S0 fee shares (10 / 20 / 35%) and the share the S5 price test offers for that card (`5_interview_kit.md` §6).
2. **Source and label every input** (*verified* / *assumed* / **[our calc]** / **[our call]**). The leak rate needs the neutral evidence, the vendor claims and the counterparty-side ceiling, each labelled. Cost to serve reuses check AA's method and inputs: BLS clerk wage $25.75 an hour grossed up to $36.79 loaded, offshore reviewer $12, machine reading about $0.10 a packet, minutes per unit from vendors where nothing better exists.
3. **Compute the four numbers [our calc]:** break-even customer size; the leak rate needed to cover variable cost at the modelled share; both with the cheapest allowed labour; the customer size at which the fee reaches **$5k a year** (check A's direct-selling benchmark, `research/s0_check_A_ambition_economics.md` §A3). State the payback on a $5-15k acquisition cost.
4. **Write the kill condition:** three bands (kill / conditional with the condition named / pass); measurable by that card's S5 savings assessment or data-access test; a verdict rule; who decides (the founders, on `5_log.md`); where the kill is recorded. Explain each line in a "Why these lines" block, as C-09's §2.4 does.
5. **Enter it in the gate tracker** (`5_validation.md` §8, the "Kill condition (C22)" row) and update `CLAUDE.md`.

Use C-09's §2 as the shape. Keep the same table columns so the four cards can be read side by side.

## 4. Inputs per card

Read the fact sheet and the scorecard rows first; they hold the unit, the pool and the fee-feasibility scores. Then the S5 check for the counterparty side and the hypotheses.

| Card | Fee unit and pool | Files to read | Known figures to start from | The doubt the model must expose |
|---|---|---|---|---|
| **C-11** LTL class, reweigh and reclass disputes | Disputed re-rates per shipment; the shipper wins back the difference | `3_factsheets.md` C-11; `4_scorecard.md` §2-§4 C-11 rows; `research/s5_check_T_ltl_carrier_position.md`; `5_validation.md` §3 H11-*, §4.1; `5_interview_kit.md` C-11 guide and assessment | FedEx Freight's dimensioner re-rating is about 0.8% of revenue (*verified*, check T), a ceiling on the money in play. Correction fees $15-55 per event. Per-buyer fee $89-781 a year on the desk (`4_scorecard.md` §9.2, P-19). The NMFTA class-data licence is a cost or a gate (D-20). **New, 2026-09-22:** SJ Consulting's survey of large LTL shippers (over $8B of charges) found carrier billing accuracy of 94-99%, average 97%, and that about half of bills of lading are wrong on weight or description, so most re-rates are the shipper's own error and are not winnable. Read via a broker's summary, so *assumed*: https://www.suntecktts.com/ltl-101-billing-accuracy/ and https://afs.net/blog/stats-incredible-common-ltl-invoice-errors/ | What share of re-rates is actually wrong and winnable, at what dollar value per win, and whether a shipper with a few hundred LTL shipments a year can ever reach $5k. Consider whether the value sits in prevention (declaring weight and class correctly at pickup) rather than disputes, and say what that does to the fee-from-savings fit |
| **C-19** retailer on-time-in-full fines and deductions | Deductions disputed and reversed per supplier | `3_factsheets.md` C-19; `4_scorecard.md`; `research/s5_check_U_retailer_position.md`; `5_validation.md` H19-*, §4.2; `5_interview_kit.md` C-19 guide | Fines about 3% of cost of goods, deducted first; dispute windows short and tightening since 2025; buyer count 15-55k (central 29k); 55% with no tool (*assumed*); SPS refocused on this buyer June 2026 (check U). C-19 was the cleanest fee case at S4 | The reversal rate a supplier can get on a valid dispute, what share of deductions are disputable at all, the per-supplier volume, and whether the retailers' rule changes shrink the pool. Also cost to serve per dispute, since each retailer has its own portal |
| **C-20** import entries | Entries filed per brokerage or importer; the saving is preparation cost per entry | `3_factsheets.md` C-20; `4_scorecard.md` (the helper-versus-filer wedge, 110 customers at the wedge, 2,365 buyers); `research/s3b_check_S_facility_fleet_trade_jobs.md`; `research/s5_check_V_recruiting_channels.md`; `5_validation.md` H20-* | Fee shape is per-entry, not a share of a recovery, so F1-F5 was read loosely at S4 ("the saving caps a per-entry price"). Only licensed brokers or self-filing importers may file | Whether a per-entry price on time saved satisfies the fee rule at all, the minutes saved per entry against what the helper costs to run, and whether 110 brokerage customers at that price reach the $2.5M floor. If the card cannot meet the fee rule as written, say so and flag it for `submarket_selection.md` §9 rather than bending the model |

If a card's leak rate has no neutral evidence at all, say so plainly and set the line from the cost side (the rate the card would need), as C-09's 1.3% was set.

## 5. Rules for this chat

- **One stage per chat, agent cap of about three.** Research agents are allowed for gaps the repository cannot fill, but read the repository first. Do not use Workflow or ultracode.
- **Agent briefs must forbid the user's email or any identity in HTTP request headers** (a prior incident with SEC EDGAR on 2026-09-17). Public sources only. No contacting any company or person.
- **Labels on every figure.** *verified* means read at the source. *assumed* means a vendor claim, an association figure, a snippet or a secondary summary. **[our calc]** is arithmetic. **[our call]** is judgement. Keep vendor figures separate from neutral ones.
- **Plain language.** The founders are new to freight. Define every acronym on first use, and give a worked example per card as C-09's §2.3 does.
- **Decision-record format.** Where a decision is needed, write the founders' words verbatim, then the evidence for and against, then leave the finalized decision to be made together. Never finalize it for them.
- **Stay in stage.** Do not set prices or pick segments; those are Q6. Do not re-score rows; that is the S5 re-score.
- **Keep it short in `CLAUDE.md`:** one work-log line, the documents index entry, and the Q5 status if it changes.

## 6. What to update when done

1. `research/selection_runs/run-01/4_kill_conditions.md` §3, §4, §5, and add any new sources to §6.
2. `research/selection_runs/run-01/5_validation.md` §8: the "Kill condition (C22)" row for the three cards.
3. `CLAUDE.md`: one line in the Work Log (date 2026-09-22 or later), and the Documents entry for `4_kill_conditions.md` if it changes.
4. `research/selection_runs/run-01/6_decision.md` §2: one sentence per card pointing at its kill condition, so the S6 briefing carries it.
5. Report back to the founders with: the four numbers per card side by side, the suggested lines with the reasons, any card that cannot meet the fee rule as written, and the open points for them to settle. Do not adopt the lines; they do.

## 7. Where the C-09 reasoning lives, for comparison

- The model and its inputs: `6_focused_target.md` §4.1-§4.4 and `research/s5_check_X_c09_money.md` §10, `research/s5_check_AA_c09_cost_to_serve.md`, `research/s5_check_AB_c09_private_recoveries.md` §7.
- The practice audit that supplied the stress inputs: `research/s5_practice_audit_public_invoices.md`.
- The kill condition and why each line sits where it does: `4_kill_conditions.md` §2.4.
- The decision and the evidence for and against: `4_scorecard.md` §9.1 D-21; `6_focused_target.md` §4.5.
