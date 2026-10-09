# Handoff: S5 interviews for C-09 and C-19 (run 01)

> **Written 2026-09-22 for a fresh Claude Code chat.** Read `CLAUDE.md` first, then this file, then the files in §10. The earlier `handoff.md` (kill conditions) is finished and is background only.
> **Your job:** help the founders run S5, the customer interviews and savings assessments, for the two cards still in play. That means:
> - getting the open decisions in §4 settled before the first call;
> - preparing recruiting and each interview;
> - turning notes into the evidence log;
> - proving or correcting every assumption in §6, with customer questions and documents;
> - running the look-backs on data the founders receive;
> - applying the frozen kill conditions;
> - keeping the gate tracker current;
> - at the end, drafting the 1-10 re-score for the founders to confirm.
>
> **What you must not do:**
> - contact anyone (the founders do all outreach and interviews);
> - move a frozen line, except through `submarket_selection.md` §9;
> - set prices or choose segments (that is Q6);
> - make any decision for the founders.

## 1. Where the project stands

- **The aim** (CLAUDE.md, "Constraints"): find a freight sub-market where software cuts a measurable cost and our fee is a share of that saving. The revenue floor is $2.5M a year, with $1M as a milestone. The process is S0-S7 in `submarket_selection.md` §4.
- **Run 01 is at S5.** Of the four finalists sent to S5 on 2026-09-16:
  - **C-09, checking and paying truckload and LTL freight bills,** is the front-runner, as a working bet (option B, 2026-09-17).
  - **C-19, retailer on-time-in-full (OTIF) fines and non-trade deductions,** is the second focus.
  - **C-11** (LTL correction disputes) and **C-20** (import entries) were **eliminated on 2026-09-22** (D-22). C-11 failed even with every unknown at its best; C-20 was viable on paper, but its saving is paid staff time, which the founders will not build for.
- **No interview has happened yet.** `5_log.md` is empty, and every gate item reads zero (`5_validation.md` §8).
- **Both cards have a frozen kill condition** (S4 step 7, `research/selection_runs/run-01/4_kill_conditions.md` ~~§2.4~~ §2.5.12 for C-09, adopted 2026-10-09 (C29), and §4.7 for C-19). Each names the measurement, the line, and who decides.
- **C-19 has also been through the new S4.5 profitability check** (`4_5_profitability.md`). Verdict: **not provable from the web**. On neutral evidence the typical small supplier is not a profitable customer; the business rests on a high-leak minority of suppliers. **C-09 has not been through S4.5.** The founders said the web was unlikely to settle it ("it seems like the estimates necessary for C-09 are unlikely").

## 2. What S5 is for, in the founders' words

- **Option B, 2026-09-17** (`6_decision.md` §5): "We are going to go with option B, the front-runner is going to be: C-09. We need to conduct interviews, gather real numbers to determine if our margins are correct and if so how much profit we can glean from each customer."
- **The elimination rule, 2026-09-22** (`4_kill_conditions.md` §7.1): "We want to absolutely eliminate any of the sub-market candidates that demonstrate no viability in this sense, if there are unknowns then they will allow them to continue living until the unknowns are clarified."
- **The focus, 2026-09-22** (D-22): "Note that the focuses are now C-09 and C-19."
- **Screen first, 2026-09-22** (C26): "Yes screen recruits first."

**What S5 has to settle, card by card:**
- **C-09:** does a real mid-sized shipper's own bills, checked against its own rate agreement, show enough provable overcharges to pay for the work? And will a controller hand over the agreement and pay a share?
- **C-19:** does a high-leak supplier's own deduction record show enough provably wrong deductions? How many recruits are high-leak? How much of the recovered money is new? And are SupplyPike's and Glimpse's customers satisfied?

## 3. The two cards at a glance

| | **C-09** freight-bill audit | **C-19** retailer deductions |
|---|---|---|
| Who pays | Controller or AP lead at US manufacturers and distributors, 20-499 staff; the person who checks the bills (often logistics) is the primary interviewee | CFO, controller, credit or deductions manager at US suppliers with $500M or less of sales that sell direct (1P) to Walmart, Target, Home Depot, Lowe's, Costco, Kroger or Amazon Vendor Central |
| Second side | **Carriers, who could buy from us:** 5 interviews (kit §5.2) | **Big-box retailers, counterparty only:** their documented position is done (`research/s5_check_U_retailer_position.md`), plus 1-2 interviews with people who work against retailers daily (kit §5.6) |
| Screen | The model says a customer pays only above about $1.5M of truckload and LTL spend, with a truckload share (`6_focused_target.md` §4.5). **C-11's slots now go to C-09, favouring LTL-heavy shippers** (D-22) | **Non-trade deductions as a share of big-box sales,** asked first (C26, kit §5.5). The look-back runs on a recruit at 1% or more; about 1 in 4 small suppliers should qualify (CRF 2021) |
| The savings assessment | Look-back audit on 1-3 months of paid invoices, **every version of the rate agreement**, fuel schedules, bills of lading and proofs of delivery, under a mutual NDA (kit §6.1) | Deduction look-back on at least one quarter and one retailer: portal export or EDI 812/820 remittances, with orders, ASNs (advance ship notices), proofs of delivery and appointment times (kit §6.3) |
| Price test | 25% of what is credited back / $500 flat / free (kit §6.1); the C-09 file also suggests testing a 45% share and a per-invoice price (`6_focused_target.md` §4.5). *D-23 (2026-10-08): C-09 is now software, and the fee form (a share of recoveries or a subscription) is open until Q6. The re-run models both side by side (`handoff_c09_software_rerun.md`); the test's wording waits for it*. *2026-10-08: the founders chose a subscription (C28); the kit's price test is rewritten (§6.1), with the amount left to the founders (D-15)* | 25% of recoveries / $500 flat / free (kit §6.3) |
| Key worry | Neutral overcharge rates are under 0.5%, and the model needs about 1.3% at US labour. The practice audit on 101 real bills proved $0 recoverable without the shipper's own documents. *D-23 (2026-10-08): the 1.3% came from our own US review cost; under D-23 that cost is the customer's staff time, and the line is being re-derived (`handoff_c09_software_rerun.md`). A new worry: whether the customer's staff actually work the flags* | The typical supplier recovers ~0.01% of sales. Only the high-leak minority pays, and SupplyPike (~500-550 customers) and Glimpse (200+ brands) may already serve it. *D-23 applies company-wide: C-19's model also costs our staff's triage and dispute minutes, so it is flagged for the same re-run later* |

## 4. Settle these with the founders before the first call

Present each in the decision-record format (their words verbatim, then evidence for and against, then "we decide together"). Don't settle them yourself.

| # | Open point | Where it is written | Note |
|---|---|---|---|
| 1 | **D-14:** adopt, park or reject P-23 to P-26 | `5_validation.md` §10.1-§10.2 | **P-25, the fixed 1-10 anchors, must be settled before any evidence arrives.** P-23 (one interview counting for two shipper cards) now matters only for C-09 and C-19 |
| 2 | **D-15:** prices for the assessments and pilots | `5_validation.md` §10.1; kit §6 | — |
| 3 | **D-16:** incentives and paid recruiting (suggested budget $2-4k, cap $10k) | `5_validation.md` §10.1 | C-19 and C-09's finance side are the hard ones to recruit |
| 4 | **D-17:** register for the 2026 3PL Study | same | Optional |
| 5 | **D-18:** data handling (mutual NDA first; raw files outside the project folder and deleted after; bank details removed at source) | same; kit §1.3 | Needed before any real data arrives |
| 6 | **D-19:** the time box | same | The planned window (21 Sep-16 Oct) has already slipped. Offer re-dated weeks. The C-19 events fall 26 Oct-11 Nov: CRF 26-28 Oct, RVCF 1-4 Nov, IOFM 2-4 Nov, AFP 8-11 Nov (check V) |
| 7 | D-20 (NMFTA licence question) | same | **Moot: C-11 is eliminated.** Record it as closed |
| 8 | **C-09 kit changes** from checks X, Y and Z: screen on 20-499 staff and $250k+ of freight spend; the bill-checker as primary interviewee; the sampling grid; the extra numbers and probes; screener and messages | `6_focused_target.md` §1.4 point 5, §7.3, §7.6 | **Partly applied:** the questions that test model numbers were added to the kit on 2026-09-22 at the founders' request (kit §5.1 "Assumption checks"; §6 below). The screen, interviewee, sampling grid, screener and messages still await a yes |
| 9 | **C-09's first product (the wedge):** audit-only first, or audit and pay | `6_focused_target.md` §1.4 point 2 | **Decided 2026-10-03 (founders): audit only first, payments later.** Verbatim: "I have decided the first rendition will just be an audit machine, we can do payments later". The price test offers audit only. See `software-initial-pitch.md` §1 |
| 10 | **Where C-20's freed slots go** (5 broker and 5 importer interviews) | `4_kill_conditions.md` §7.4 | Undecided: C-19 (hardest to recruit), C-09, or dropped |
| 11 | **C-09's frozen rule** says its conversations go to "C-11 and C-19" if C-09 is killed; with C-11 gone this means C-19 | `4_kill_conditions.md` §2.4 note | Point b of D-22, never answered. Confirm the wording |
| 12 | **D-23: a software company, not an audit firm** | `software-initial-pitch.md` §1A | **Decided 2026-10-08 (founders).** Verbatim: "We have no analysts, this is a software company. A software as a service, we do no manual reviews here." The software flags the errors; the **customer's own staff review them and file the disputes**; help with filing comes later; the customer uploads its rate agreements and the software reads them. The rule is company-wide, so **C-19 is flagged** for the same re-run later. **C-09's kill test is re-run** on this basis in a separate chat (`handoff_c09_software_rerun.md`). The frozen lines in §5 stay in force until the founders adopt new ones, and **no look-back starts before then**. In parallel, the founders ask existing contacts two questions (kit §5.1, "Who works the flags") |

## 5. The kill conditions (frozen; apply exactly as written)

> **C-09: basis superseded by D-23 (2026-10-08); ~~re-run pending~~ re-run proposed on 2026-10-08, ~~not adopted~~ adopted by the founders on 2026-10-09 (C29, `4_kill_conditions.md` §2.5.12): "Adopt the Kill/Cover/Pass lines" (`4_kill_conditions.md` §2.5).** In brief:
> - **Test 1:** what the software flags and the shipper's reviewer accepts. Kill under ~~0.78%~~ 0.044% (acquisition cost bounded at $0-$10k until the first customer is timed (`4_kill_conditions.md` §2.5.11)) and pass at 6.44% or more at a $1.5M shipper, with a table by size. In between, C-09 continues only if a pilot of at least one billing cycle shows enough follow-through.
> - **Test 2:** unchanged.
> - **Test 3:** the customer's timed hours against the hours it says it can give.
> - **The founders' answers, 2026-10-08** (`4_kill_conditions.md` §2.5.10): a subscription, hours as capacity, the look-back design (kit §6.1), and Test 1 on flagged dollars are decided. P-31 is deferred. The acquisition cost is ~~open~~ ~~deferred until the first customer is timed~~ bounded at $0-$10k until the first customer is timed (`4_kill_conditions.md` §2.5.11), ~~so the new lines are not adopted yet~~ and the new lines were adopted on 2026-10-09. **Apply §2.5.12 exactly as written.**
>
> ~~The founders adopt the new lines or not. Until then: The lines below were derived from our own review cost. Test 1's 1.3% is where US-staffed review covers its labour; the middle band relies on offshore review or a 45% share; Test 3 measures our cost at US and offshore wages. Under D-23 the review and dispute time is the customer's. The re-run is briefed in `handoff_c09_software_rerun.md`. **These lines stay frozen until the founders adopt new ones** (then a `submarket_selection.md` §9 entry). **No C-09 look-back starts before then.**~~
>
> **Adopted 2026-10-09 (C29).** The lines below are superseded and kept for the record. Apply `4_kill_conditions.md` §2.5.12. Look-backs may now start; the data-handling rules (D-18) are still needed before real data arrives.

**C-09** (`4_kill_conditions.md` §2.4, frozen 2026-09-22; *superseded 2026-10-09 by §2.5.12, C29*). Measured on the first real look-back of in-window spend. In-window means still contestable: 180 days from receipt, or the contract's own window if longer.

| Test | Kill | Conditional | Pass |
|---|---|---|---|
| 1. Overcharges billed wrong and provable, as a share of in-window spend | **under 0.75%** | 0.75-1.3%, with a named condition | **1.3% or more** |
| 2. Rate agreement and paid invoices under NDA | **2 of the first 3 shippers decline** | 1 of 3 declines | all 3 agree, or 1 declines and a replacement agrees |
| 3. Measured gross profit at a $1.5M customer, 25% share | **negative under US and offshore wages** | negative US, positive offshore | positive at US wages |

**C-19** (`4_kill_conditions.md` §4.7, frozen 2026-09-22; C26 and C27 the same day). Measured on a supplier screened at 1% or more of non-trade deductions. *D-23 (2026-10-08) flag: these lines also cost our own staff's triage and dispute minutes, so C-19 needs the same software-basis re-run before S6 compares the two cards. Not done yet; the lines stand as written until then.*

| Test | Kill | Conditional | Pass |
|---|---|---|---|
| 1. Provably wrong non-trade deductions still inside the dispute window, as a share of sales to that retailer | **under 0.05%** | 0.05% up to the pass line | **0.22% at a $50M supplier**; by size: $20M 0.47%, $100M 0.14%, $200M 0.094% (straight-line between rows) |
| 2. Portal export or 812/820 plus proofs of delivery under NDA; retailer terms allow a third party | **2 of the first 3 cannot or will not share, or the terms bar third parties** | 1 of 3 cannot | all 3 share |
| 3. Measured gross profit at a $50M supplier, 25% share | **negative under US and offshore wages** | negative US, positive offshore | positive at US wages |

**Also record for C-19** (C26):
- the **screen yield**: the share of recruits at 1% or more;
- the **new-money share**: of the provably wrong dollars, the part the supplier would not have recovered on its own.

**Verdict rules** (both cards): any kill stops the card's S5 work; any conditional without a kill lets it continue, but it can't be confirmed at S6 until the condition is met; all pass sends it to the re-score. **The founders decide** on the evidence in `5_log.md` §7. Record a kill in `6_decision.md` §5, and for C-09 also in `6_focused_target.md` §1.4.

## 6. The assumption register: every number we assumed, and how S5 proves it

*Added 2026-09-22 at the founders' request: "Ensure the relevant assumptions, and what we can ask to ensure we clarify and prove them, are tracked in the S5 handoff. I want to make absolutely sure these numbers are correct, by asking questions to the customers so we can prove this."*

### 6.1 How a number gets proven

Each assumption below moves through three states. Record the state in `5_log.md` §10.

| State | What it takes | How much weight it carries |
|---|---|---|
| **Claimed** | An interviewee states it, about a specific past event, with an amount and a date ("last quarter Walmart took $41k for late deliveries") | Supports a row (7-8 on the evidence ladder, `5_validation.md` §7.1). **Never enough on its own for a kill test** |
| **Proven** | Measured by us on the customer's own documents in the look-back (invoices, agreements, deduction exports, remittances, credit memos), or shown in a document the customer hands over | Decides the kill tests (9-10 on the ladder) |
| **Contradicted** | A document or measurement disagrees with the model value, or 3 or more interviewees give specific past events against it | Moves the model; record the gap between the claim and the document |

**Rules for asking, so the answers can be trusted** (kit §1, from the Mom Test):
1. **Ask about the last time, not "usually".** "Tell me about the last …" gets an event with an amount; "how often do you …" gets a guess.
2. **Ask for the number with its unit and period:** dollars, count, hours, over a named month or quarter.
3. **Ask to see it in the same conversation:** "Is that on a report you could show me or send under an NDA?"
4. **Write down the exact words and the figure,** with the interview ID.
5. **Never ask "would you" for a number.** Future intent is not evidence. The only exception is the price test, and a price counts only when signed (commitment type 3-4).
6. **When a claim and a document disagree, the document wins.** Record both: how far people over- or under-estimate is itself useful.

### 6.2 C-09 · Checking truckload and LTL freight bills

Model values from `4_kill_conditions.md` §2.2. "Kit" means the question is already in `5_interview_kit.md` §5.1 or §6.1; "new" means it is in the kit's assumption-check block, added 2026-09-22.

> **D-23 (2026-10-08): C-09 is software, not an audit service.** The software flags the errors; the customer's own staff review and file. So:
> - **A09-06 and A09-07** now measure **the customer's workload**: flags (false ones included) × minutes per flag, not our cost.
> - **A09-12 (offshore review) is moot.**
> - **A09-04** becomes the fee form and level.
> - **A09-02** is the share the software flags.
> - **Three new rows** are added: A09-15 (follow-through), A09-16 (the customer's hours), A09-17 (self-serve onboarding).
>
> Of the old $1.12 per bill, $0.10 (machine reading) stays ours, and $1.02 becomes the customer's time **[our calc]**. The model values themselves are re-derived in `handoff_c09_software_rerun.md`.

| ID | Assumption, in plain words | Model value now (label) | What it moves | Ask the customer | Document that proves it |
|---|---|---|---|---|---|
| **A09-01** | **Share of in-window spend the carriers billed wrongly, in their own favour, that the shipper's documents can prove** | **1.5%** (**[our call]**; neutral sources all under 0.5%; six vendor cases 0.8-4.2%) | **Test 1: kill under 0.75%, pass at 1.3%.** Everything else follows from it | Kit: "Tell me about the last freight bill that turned out to be wrong" (amount, type, how caught). New: "In the last 12 months, how many bills did you short-pay or dispute, and for roughly how many dollars in all?" New: "Have your bills ever been audited? What did it find, in dollars, and against how much spend?" | **The look-back** (kit §6.1): 1-3 months of paid invoices, **every version** of each rate agreement, fuel schedules, bills of lading and proofs of delivery. Only overcharges the documents prove count |
| **A09-02** | Share of the real overcharges ~~our audit catches~~ *(D-23: the software flags)* | 70% (**[our call]**; GAO: one professional audit found 72-78% of what two found) | The fee | New: "Of the wrong bills you found last year, how many did you catch before paying, and how many after?" | Compare our flagged list with the shipper's own dispute log for the same period. The overlap is an estimate, not full proof: say so |
| **A09-03** | Share of disputed overcharges the carrier actually credits | 75% (**[our call]**; 60-90% prompt, 41-51% aged, *assumed*) | The fee | New: "Of the bills you disputed in the last year, how many came back, for how much, and how many days did it take?" New: "Tell me about the last dispute a carrier refused. Why?" | The shipper's credit memos or dispute log. Also the outcome of any claims filed from the look-back (these can land after S5; log them when they do) |
| **A09-04** | ~~The fee share a shipper will accept~~ *D-23:* the fee form and level a shipper will accept (a share of recoveries or a subscription; the price is Q6) | 25% (price test; the conditional band also tests 45% and a per-invoice price). *D-23: both forms are modelled side by side in the re-run*. *2026-10-08: a subscription (C28), so this row is now the level* | The fee; Test 1's conditional band | Kit: "Does anyone audit your bills now? What do they charge?" Then the price test at the close (kit §6.1) | A signed assessment agreement or letter of intent. **A verbal yes is only a claim** |
| **A09-05** | Freight invoices per $1,000 of spend (LTL-heavy accounts have more, smaller bills) | 1.5 (**[our calc]**; the real ABF account: 2.21) | ~~Cost to serve; Test 3~~ *D-23:* our reading cost, and the customer's flag count | New: "How many freight invoices do you pay in a typical month? What's your freight spend a year, split truckload, LTL and parcel?" | The invoice count and total in the look-back sample; an AP payment export with bank details removed |
| **A09-06** | Share of invoices that need a person, not a machine. *D-23: the customer's workload, counted as flags (false ones included)* | 15% (**[our call]**; the real ABF account: 58%) | ~~Cost to serve; Test 3~~ *D-23:* the customer's review hours; the restated Test 3 | New: "On a typical month's bills, how many carry extras (liftgate, detention, lumper, a reweigh note)?" | Count in the look-back: bills with a line needing a document or a judgement |
| **A09-07** | Minutes of human review per invoice, and per dispute. *D-23: the customer's minutes per flag and per dispute* | 6 minutes per review, $9.30 per dispute (*assumed*; vendors 3-13 minutes) | ~~Cost to serve; Test 3~~ *D-23:* the customer's review hours; the restated Test 3 | New: "How many hours a week does your team spend checking and disputing freight bills, and for how many bills?" | ~~**Our own timed hours** in the look-back, per bill and per dispute~~ *D-23:* **the customer's reviewer, timed** in the look-back, per flag and per dispute (the suggested design, pending the founders) |
| **A09-08** | Fixed cost to serve one customer a year (loading agreements, fuel tables, carriers). *D-23: the customer uploads and confirms its agreements (see A09-17); our part is support and platform cost* | $400 (*assumed*). *D-23: re-derived in the re-run* | Break-even size; Test 3 | New: "How many carriers do you use? How many rate agreements, and how often do rates or fuel tables change?" | Hours recorded loading the shipper's agreements and fuel tables in the look-back |
| **A09-09** | The customer's truckload and LTL spend (break-even $1.35M with US review; $5k fee at $2.5M). *D-23: that break-even assumed our own reviewers; it is re-derived in the re-run* | Screen favours $1.5M+ with a truckload share (**[our call]**, `6_focused_target.md` §4.5) | Whether this customer can pay at all; Test 3's $1.5M reference | Screen: yearly freight spend by mode (bands: under $250k / $250k-1M / $1-3M / over $3M); share booked through a broker or 3PL | The AP payment export, or the look-back sample annualised |
| **A09-10** | Share of a look-back still inside the claim window (180 days, or the contract's own window) | ~50% of a 12-month look-back (**[our calc]**) | How much found money is collectable | New: "Do your truckload contracts or broker rate confirmations have a claims clause, like 'claims within 90 days'?" New: "How soon after paying do you usually notice a wrong bill?" | The clause in the contract or confirmation; invoice dates against the assessment date |
| **A09-11** | The shipper will share the rate agreement and paid invoices under NDA | Test 2 (2 of the first 3 declining kills) | **Test 2** | Kit: "If I asked for last month's paid freight invoices and the rate agreements, what format would they be in, and how long would it take to pull?" Then ask for them under a mutual NDA | Files received. Count yes and no among the first 3 |
| ~~**A09-12**~~ | ~~Offshore review of the shipper's invoice data is acceptable~~ | ~~Needed only in Test 1's conditional band~~ | ~~Test 1 condition; cost~~ | ~~New: "Would your company allow invoice data, under an NDA, to be reviewed by a team outside the US?"~~ | ~~A written yes or no (a policy, or an email)~~ **Moot under D-23 (2026-10-08):** we have no reviewers, offshore or otherwise |
| **A09-13** | First-year finds fall in later years (mature 0.5-1.5%) | *assumed* (vendors) | Whether revenue lasts past year one | New: "If you've been audited before, what happened to errors in the year after?" | A prior audit report, if they have one |
| **A09-14** | Share of bills through brokers, on the minimum charge, or carrying a reweigh | ABF account: 38% on the minimum charge; 28% with a reweigh note | How much of the spend an audit can bite on | New: "What share of your freight goes through a broker or 3PL?" | Counts in the look-back |
| **A09-15** *(new, D-23)* | **Follow-through:** the share of the software's real flags that the customer's staff actually work **and** file | ~~No value~~ Desk **60%**, dollar-weighted **[our call]**; no measurement exists (re-run, `4_kill_conditions.md` §2.5.3). The named condition of Test 1's middle band (proposed 2026-10-08, not adopted) | Recovered dollars; under a share of recoveries, our revenue | "The last time a freight bill looked wrong, who at your company looked into it, and how long did it take?" (`handoff_c09_software_rerun.md` §7) | **A pilot of at least one billing cycle:** the customer's dispute log against the software's flags. One watched look-back can't prove it, because it reads 100% under observation |
| **A09-16** *(new, D-23)* | **The customer's hours a month** for the flag queue, treated as capacity | ~~No value~~ Desk capacity **20 hours a month** **[our call]**. Need about 12.5 hours a month at a $2M shipper (15% of bills flagged, 10 minutes a flag, disputes 30 minutes) **[our calc]**; 30-45 at the practice audit's 58% (`4_kill_conditions.md` §2.5.4). Test 3 (proposed) | Whether the queue gets worked; the customer's net saving | "How many hours did your team spend on freight bills last month, and on what?" "Has anyone used an audit screen in your booking tool? When did they last clear it?" | Their own time records, or the timed look-back (minutes per flag × flags a month) |
| **A09-17** *(new, D-23)* | **Self-serve onboarding:** the share of rate agreements the software reads correctly unaided, and the customer's minutes to confirm the rules | ~~No value~~ Desk: **8 agreements × 60 minutes** to confirm in year one **[our call]**; our onboarding help $185-616 (check AR). No completion rate for loading contracts exists on the web, and a strong table reader gets every cell right in only 69% of complex tables (check AR §AR5) | Our support cost; whether customers get started | "Where is your biggest carrier's pricing agreement right now? What format is it in?" | Timed in the look-back: agreements read correctly, corrections needed, minutes to confirm |

### 6.3 C-19 · Retailer fines and non-trade deductions

Model values from `4_kill_conditions.md` §4.2 and §4.7, with S4.5's findings (`4_5_profitability.md` §3).

| ID | Assumption, in plain words | Model value now (label) | What it moves | Ask the customer | Document that proves it |
|---|---|---|---|---|---|
| **A19-01** | **Share of the supplier's big-box sales the retailers take for non-trade reasons** (fines and shortages, not promotions) | Screened recruits: **1.2%** (one real ledger, M Design Village, *verified*); CRF median for small suppliers ¼-½%; **the retailer side agrees on the average:** ShopKo's sworn bankruptcy filing shows vendor fines of 0.24-0.32% of its sales, about 0.33-0.46% of what it paid vendors (*verified*, N-AG63; re-read at source) | The screen (1% or more); the number of deductions; cost | Kit screen: "Roughly what share of your sales to big-box retailers comes back as non-trade deductions?" New: "Last quarter, how many dollars of fines and shortages did [retailer] take?" | Portal export or EDI 812/820 remittances for at least one quarter, sorted by reason code, divided by sales to that retailer from the supplier's own sales report |
| **A19-02** | **Share of those deductions the supplier's documents prove wrong,** still inside the dispute window | 10% (CRF, all deductions); **the pass line needs about 18% at a $50M supplier**; CRF small-supplier median 1-5%, with 43% at 15% or more | **Test 1: kill under 0.05% of sales, pass at 0.22% at $50M** (table by size) | Kit: "Tell me about the last OTIF fine or compliance deduction you got" (was it valid?). New: "Of last quarter's fines and shortages, how many were wrong, and how did you check?" | **The look-back** (kit §6.3): each deduction checked against the PO, ASN, proof of delivery and appointment time. Only document-backed wrong ones count |
| **A19-03** | Share of wrong deductions the retailer pays back when disputed | 60% (CRF all sizes; small suppliers 70%, *verified* survey) | The fee | New: "Of the deductions you disputed in the last 12 months, how many dollars came back, and how long did it take?" Kit: "the last one you didn't dispute: why not?" New: "Tell me about the last dispute a retailer denied" | Portal dispute statuses and the repayments on remittances. Also the outcomes of the 5-10 disputes filed from the look-back, which replace the 60% once decided |
| **A19-04** | **New money:** of the wrong deductions we find, the share the supplier would not have recovered on its own | Unknown; S4.5 ran 100% and 50% (C26) | Whether our fee is truly a share of a saving | New: "Which of these had you already disputed?" (asked on the look-back list). New: "Below what amount do you not bother disputing?" New: "Who disputes today, and how many a week?" | The supplier's own dispute log for the same period, set against our list of wrong deductions |
| **A19-05** | Average deduction size, and count per $1M of sales | $500 each, about 10 per $1M at 0.5% (**[our call]**; published fee schedules $150-450) | Cost per dollar of fee; Test 3 | New: "Roughly how many fines and shortages a month, and what does a typical one come to?" | The export's count and dollar spread |
| **A19-06** | Minutes to check each deduction, and to dispute a wrong one | 5 and 20 (**[our call]**; manual benchmark about 52 minutes all-in) | Cost; Test 3 | Kit: "Who works deductions, and how many hours a week?" New: "…and how many deductions do they handle in that time?" | **Our own timed hours** in the look-back |
| **A19-07** | Fixed cost per customer, including each retailer portal | $600 a year (**[our call]**) | Break-even; Test 3 | New: "Which retailer portals do you use? Can you add a third-party or sub-user? Has a retailer ever refused one?" | Setup hours recorded; the portal's user settings |
| **A19-08** | The supplier's big-box sales and retailer mix (it sets which pass line applies) | Big-box ≈ 2 × Walmart sales (**[our call]** on five filings) | Which row of the pass-line table applies | New: "Roughly what are your yearly sales to each big-box retailer?" | The supplier's sales-by-customer report for the look-back period |
| **A19-09** | **Screen yield:** the share of recruits at 1% or more | about 25% (CRF 2021, *verified* survey) | The cost of finding a customer; the revenue test | The screen question, asked of every recruit | The tally across all C-19 recruits (`5_log.md` §10) |
| **A19-10** | The fee share a supplier will accept, and what it pays today | 25% (price test); SupplyPike ~$33-38k a customer a year | The fee | New: "What do you pay today (software, a recovery firm, staff), and what came back last year?" Then the price test (kit §6.3) | A signed assessment agreement or letter of intent; an incumbent's invoice, if shown |
| **A19-11** | The supplier can export deductions, and the retailer's terms allow a third party | Test 2 | **Test 2** | Kit: "Could you export last quarter's deductions from the portal or the 812/820 remittances?" | Files received; the retailer's written terms, where readable |
| **A19-12** | Invalid dollars already lost to closed dispute windows | Unknown (Home Depot about 4 weeks, Lowe's about 15 days, Amazon 30 days) | What a look-back can still collect; the day-one value | Kit: "Have you ever lost a dispute because the window closed?" New: "Roughly how much in the last year?" | The look-back's out-of-window invalid dollars, recorded separately |
| **A19-13** | Incumbent users are not all satisfied (SupplyPike/SPS, Glimpse and others) | H19-11; Capterra 4.9 against complaints | **Show-stopper test** | Kit incumbent probes: what they paid, what came back, the last denied dispute, when they last thought about switching, the price at renewal | What they paid against what came back, from their own records if shown |
| **A19-14** | Part of the fines belongs to the supplier's 3PL or carrier by contract | *verified* in one contract (Prestige Brands-GEODIS) | Whether the dispute is with the retailer or with the 3PL | New: "Does your warehouse or carrier contract say who pays retailer chargebacks? Have you ever charged one back to them?" | The clause in the 3PL or carrier contract |
| **A19-15** | How often the supplier misses the retailer's on-time and in-full targets | Unknown; fines = failing share × 3% at Walmart | The size of the fine pool | New: "What were your on-time and in-full percentages at Walmart last month, and was a fine charged?" | The retailer scorecard |

### 6.4 Our own assumptions, which customers can't prove

These are checked from our side and recorded next to the register:

| ID | Assumption | Value now | How S5 checks it |
|---|---|---|---|
| A-X1 | The cost of winning one customer | $5-15k (check A) | Log founder hours and paid-recruiting spend per meeting and per assessment agreed (`5_log.md` §1). It is the first real estimate |
| A-X2 | Loaded wage for review work. *D-23 (2026-10-08): now the **customer's** wage, used only as a sensitivity; the re-run treats their hours as capacity. Offshore is moot (no reviewers of ours)* | US $33.70-36.79; posted $42-49; ~~offshore $12~~ | Job postings (check AI); ~~the look-back's timed hours convert at both wages~~ *D-23:* the customer reviewer's timed minutes, at their wage as a sensitivity |
| A-X3 | Machine cost per document | about $0.10 | Recorded when the look-back is run with software |


## 7. How to work each interview

**Before:**
- Check the recruit against the screen (§3).
- Prepare a one-page brief: which hypotheses this person can test (`5_validation.md` §3.1 for C-09, §3.3 for C-19), and which guide (kit §5.1-5.2 for C-09; §5.5-5.6 for C-19).
- For C-19, include the incumbent probes (kit §5.5, H19-11): what they pay, what came back, the last denied dispute, cancelling or switching, the price at renewal (`4_5_profitability.md` §3.7).

**Kit discipline** (kit §1, from R35's Mom Test):
- ask about past events with amounts, not opinions or future intent;
- never pitch before the incident module;
- record commitments by type.

**After** (founders write notes within 24 hours, kit §8). Turn them into:
- the interview register (`5_log.md` §2);
- the hypothesis log in R15's format (§3);
- costed incidents (§4), commitments (§5), data sources (§6);
- the survey votes (§8).

**Look-backs:**
- Run the method in kit §6.1 (C-09) or §6.3 (C-19) on the data received.
- Keep raw files outside the project folder (D-18).
- ~~Record hours spent: that is the first real cost-to-serve number.~~ *Superseded by D-23 (2026-10-08):* for C-09, time **the customer's reviewer** on the flags (minutes per flag, the share accepted as real, minutes to confirm the rules). That is their workload, not our cost to serve. **No C-09 look-back starts until the founders adopt the re-run's kill lines** (`handoff_c09_software_rerun.md`).
- Write the result to `5_log.md` §7, then compute the three kill tests.
- For C-09, the practice audit (`research/s5_practice_audit_public_invoices.md`) shows the method and its traps: minimum-charge accounts produce false duplicates, and fuel percentages need the contract's own table.

**Keep current:**
- the gate tracker (`5_validation.md` §8), after every interview;
- the funnel (`5_log.md` §1), after every outreach wave.

## 8. The gate, and what comes after

**The gate** (`5_validation.md` §8, per card):
- at least 5 paying-side interviews;
- the second side covered (C-09: 5 carrier interviews; C-19: at least 1 worker interview);
- at least 3 costed incidents;
- at least 2 commitments;
- a named data source plus at least 1 interviewee willing to share;
- a savings assessment on real data, or a written reason why not;
- the kill condition measured.

**If P-25 is adopted,** draft the 1-10 re-score (`5_validation.md` §7) for the founders to confirm. Then S6 confirms or changes the primary (`6_focused_target.md` §9, steps 9-11).

## 9. Working rules

- **One stage per chat. Agent cap about 3,** and ask before using more. No Workflow and no "ultracode".
- **Research agents only for gaps the repository can't fill.** Their briefs must forbid the user's email or any identity in HTTP headers, forms or queries (SEC EDGAR incident, 2026-09-17). Public sources only.
- **You contact no one.** Draft messages and lists; the founders send them. Contact lists live outside the project folder (kit §1.3).
- **Labels on every figure:**
  - *verified*: read at the source;
  - *assumed*: vendor, association, snippet or secondary;
  - **[our calc]**: arithmetic;
  - **[our call]**: judgement.
- **Money arguments rest on real documents, with the arithmetic shown** (memory: money evidence).
- **Plain language.** The founders are new to freight: define every acronym on first use, and give worked examples.
- **Decision-record format** for every decision. Never finalize one for them.
- **Stay in stage:** no prices, segments or entry side (Q6).
- **The founders won't build software whose saving is cutting paid hours.** Flag any idea that drifts there.
- **Frozen lines move only through `submarket_selection.md` §9,** and never after the measurement they apply to has been seen.
- **Keep `CLAUDE.md` short:** one work-log line per step, the documents index, and the Q5 status when it changes.

## 10. Files to read, in order

1. `CLAUDE.md` (project), then this file.
2. `research/selection_runs/run-01/5_validation.md`: §1-§3 (sides, hypotheses), §5 (plan), §7 (re-score rules), §8 (gate), §10 (open decisions).
3. `research/selection_runs/run-01/5_interview_kit.md`: §1 rules, §3 messages, §4 the common spine, §5.1-5.2 (C-09), §5.5-5.6 (C-19), §6.1 and §6.3 the assessments, §8 note template.
4. `research/selection_runs/run-01/4_kill_conditions.md`: §2 (C-09) and §4 (C-19), including the S4.5 note, C26 and C27. **Also `handoff_c09_software_rerun.md`** (D-23, 2026-10-08): C-09's kill test is being re-run as a software company in a separate chat, and the interview track there runs in parallel with yours. See also `software-initial-pitch.md` §1A.
5. `research/selection_runs/run-01/6_focused_target.md`: C-09's decision record (§1), money chain (§4), who to interview (§5), how to reach them (§6), what to find out (§7), next steps (§9).
6. `research/selection_runs/run-01/4_5_profitability.md`: C-19's audit, verdict and incumbents (§3.5-§3.7).
7. `research/selection_runs/run-01/5_log.md`: the empty log you will fill.
8. **Background, when needed:**
   - `research/s5_check_V_recruiting_channels.md` (channels, events, incentives);
   - `research/s5_check_Y_c09_reach.md` (C-09 segments, panels, screener, messages);
   - `research/s5_check_U_retailer_position.md` (retailer rules and windows);
   - `research/s5_check_AC_c09_example_invoices.md` §9 (the document request list);
   - `research/s5_practice_audit_public_invoices.md`.

## 11. What to update as you go

| When | Update |
|---|---|
| Each outreach wave | `5_log.md` §1 |
| Each interview | `5_log.md` §2-§6, §8, §9; the assumption results in `5_log.md` §10 (claimed values); `5_validation.md` §8 |
| Each look-back | `5_log.md` §7 and §10 (proven values); the kill-test results beside the card's condition in `4_kill_conditions.md` (as a dated result line, never by editing the lines) |
| A kill, or a decision | `6_decision.md` §5 (and `6_focused_target.md` §1.4 for C-09); `CLAUDE.md` work log |
| The re-score | `5_validation.md` §7.3 and §8; `CLAUDE.md` |
