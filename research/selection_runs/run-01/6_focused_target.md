# Run 01, S6 (working bet): the focused target, C-09

> **Stage S6 of `submarket_selection.md` §4, "Choose", opened early under option B. Written 2026-09-17.**
> **What happened:** on 2026-09-17 the founders chose **option B** from `6_decision.md` §4. That means naming a front-runner now and confirming it at S6 once S5's interviews are in. They named **C-09, checking and paying freight bills**, as the front-runner.
> **What this file is:**
> - the decision record (§1);
> - everything the run has learned about C-09, from `0_criteria.md` to `6_decision.md` (§2-§3);
> - the money model the interviews must check (§4);
> - who to interview and how to reach them (§5-§6);
> - what the interviews must find out (§7);
> - the backups and what is parked (§8);
> - the next steps (§9).
>
> **Status:** C-09 is a **working bet, not the final S6 choice.** S6's own entry condition is still S5's gate (`5_validation.md` §8), which is not met for any card. The final choice is made together after the S5 re-score.
> **New research for this file:** three web checks run on 2026-09-17, with sources N-X, N-Y and N-Z:
> - `research/s5_check_X_c09_money.md`: overcharge rates, pricing, margins, per-customer value;
> - `research/s5_check_Y_c09_reach.md`: who the buyers are, segments to sample, how to reach them;
> - `research/s5_check_Z_c09_voice.md`: what buyers and carriers already say in public.
>
> The letter W was skipped for the check names so they aren't confused with Axis W.
>
> **What the checks found, in four lines:**
> 1. **The margins hinge on one number the web can't supply:** the overcharge rate on a shipper's own bills. Every neutral figure sits below the desk's 1-3%. Check X's illustrative model breaks even at about $0.7M of truckload and LTL spend, but that result rests on a middle overcharge rate we chose ourselves (1.5%) and on cost-to-serve figures with no source. **It does not show C-09's margins are unacceptable, and the project has not set a margin threshold** (§4.3, 'How much of this is evidence').
> 2. **The person who checks the bills is usually in logistics, not AP,** and the practical size cut is freight spend (about $0.5-1M), not headcount (§5.3).
> 3. **The web answers documents and prices, not behaviour.** It also names an incumbent the hypotheses missed: the audit screens inside cheap LTL booking tools (§7.5).
> 4. **A panel is the only route likely to deliver 5 shipper interviews by early October.** Lists, warm introductions and a few in-window events come next. There is no gathering place for carrier billing staff (§6.2).
>
> **A second round (checks AA, AB and AC, §4.4) then sourced the cost to serve, the recovery evidence and real invoices:**
> 5. Machine reading costs cents; **people are the cost**, and where the review work is done moves break-even from $1.35M of spend to about $0.3M. *Superseded by D-23 (2026-10-08): C-09 is a software company with no analysts. The people cost is now the customer's own staff time, not ours, and the break-even is being re-derived in `handoff_c09_software_rerun.md`.*
> 6. Only six published cases give both a spend and an overcharge amount (median 1.8%, mostly large first-year programmes). The one neutral private measurement, from 1977, is 0.45%.
> 7. **The 180-day rule caps a look-back** ("compliance with the 180-day time limit is not optional", 10th Cir. 2021), so the audit should match the claim window and then run monthly.
> 8. **Real invoices are public in court records:** 101 ABF bills, 6 XPO invoices with their paperwork, and ~75 SEFL bills with the pricing agreement they should follow.
>
> **Nothing here is finalized.** The points to settle together are in §1.4.

## How to read this

- **Labels** (as in every run-01 file):
  - *verified*: read at the source;
  - *assumed*: a vendor claim, an association figure, a snippet, a secondary summary or a forum anecdote;
  - **[our calc]**: arithmetic;
  - **[our call]**: judgement.
- **Freight and finance words used here:**
  - **Truckload (TL):** one shipper's goods fill a whole trailer.
  - **LTL (less-than-truckload):** several shippers' pallets share one trailer, priced by freight class.
  - **Accessorial:** an extra-service charge on a freight bill, such as a liftgate, a residential delivery or waiting time (detention).
  - **BOL (bill of lading):** the shipping document signed at pickup.
  - **POD (proof of delivery):** the signed delivery receipt.
  - **PRO number:** the carrier's shipment ID.
  - **EDI 210:** the electronic freight invoice that larger carriers send.
  - **Contingency audit:** an outside firm checks bills already paid, claims the overcharges back, and keeps a share (25-50%) of what comes back. It is paid nothing if nothing is recovered. *D-23 (2026-10-08): C-09 is no longer modelled as a contingency audit firm. It is software that flags errors to the customer's own reviewers, who review and file the disputes (`software-initial-pitch.md` §1A).*
  - **FAP provider (freight audit and payment):** a firm that checks every bill *before* payment and then pays the carriers for the shipper, e.g. Cass or U.S. Bank.
  - **Look-back audit:** re-checking bills already paid, for overcharges still inside the claim windows.
  - **AP:** accounts payable, the team that pays suppliers' invoices.
  - **Controller:** the finance manager who runs accounting at a mid-sized firm.
  - **CAC (customer acquisition cost):** what it costs to win one customer.
  - **Gross profit per customer:** our fee from that customer minus the direct cost of serving them. *Under D-23 (2026-10-08) the direct cost is software only: reading, storage, support and licences. Review and dispute time is the customer's.*

---

## 1. The decision

### 1.1 Initial decision (the founders, 2026-09-17, verbatim)

> "We are going to go with option B, the front-runner is going to be: C-09.
>
> We need to conduct interviews, gather real numbers to determine if our margins are correct and if so how much profit we can glean from each customer.
>
> Mark this down in 6_focused_target.md, next steps as identified here and in the 6_decision.md document, along with any other relevant information from 0_criteria through 6_decision.md (all of the 1_, 2_, ... docs).
>
> Interviews will be focused on C-09 specific segments and customers, dig up information about who this might be and how they can be reached to schedule these specific interviews. Also what we need to glean from these interviews.
>
> Then spawn agents to see if you can find any more information to our questions, from specific forums or other sources. Just so we can go in with as much info as possible or see if our answers can be answered from the web as opposed to having to ask people."

**What option B says** (`6_decision.md` §4, Decision 1):

| Option | What it means | For | Against |
|---|---|---|---|
| **B. Name a front-runner now and still run S5 on all four** | A working bet that sets the order of outreach and which assessment runs first; confirmed at S6 | Gives focus, and the interviews can still prove you wrong | Some risk of pitching in interviews instead of listening (R15) |

### 1.2 Research for and against, part by part

| Part of the decision | For | Against | Reading **[our call]** |
|---|---|---|---|
| **(a) Name a front-runner before S5 ends (option B)** | Gives the outreach an order and puts C-09's savings assessment first, the single test that moves the most rows (`4_scorecard.md` §7 factor 9). Aulet's advice is to pursue a beachhead "until it proves not to work or is much less attractive than originally anticipated" (R16), which a working bet does. B still runs S5 on all four, so the desk's "cannot rank" finding (`4_scorecard.md` §8) is respected | Interviewers who have picked a favourite drift from "inquiry mode" into "advocacy mode" (R15) and hear what they hope to hear. S6's entry condition is the S5 gate, not a desk rank | **Supported, with one guard:** the interview rules in `5_interview_kit.md` §1 (past events only, no idea pitched, commitments counted, not compliments) are what stop a working bet from turning into advocacy. The 1-10 anchors (P-25) should be fixed before the first call for the same reason |
| **(b) C-09 as the front-runner** | The biggest prize: a central fee pool of $209M, 3-6 times any other finalist. The only clean pass on every knock-out. The strongest fee case (F1-F4 3.5, F5 1), with contingency audit an existing contract shape. The most open field (leaders at about 4-5% of trucking dollars each, aiming at enterprises). Two backups on the same product core (C-11, C-19). Cohen 10.0 with an audit-first product (`4_scorecard.md` §1-§4, `6_decision.md` §2) | The lowest Axis W of the four (55): paying carriers takes months. It's bought through finance, and check V found no place where these buyers gather. Funded AI rivals: Loop raised $95M in April 2026, and Cass's 10-K warns AI could make its offerings obsolete. The 1-3% overcharge rate and the spend base are our guesses. It is durable only in defensive shipper groups (`4_scorecard.md` §6.5) | **Supported as a working bet.** The case rests on two things S5 measures directly: the overcharge rate on one shipper's real invoices (H09-02), and whether a controller will share invoices with a startup and pay a share of recoveries (H09-05, H09-06, H09-07) |
| **(c) "Gather real numbers to determine if our margins are correct … how much profit … from each customer"** | S5 already includes a savings assessment on real data and a price test (`submarket_selection.md` §4 S5 steps 3-4; kit §6.1). R25: "success rate sets the margin" under outcome pricing, so margins can only be known from real recoveries. §4 below shows the desk model has **gaps a customer's numbers must fill**: the share of flagged overcharges carriers actually credit, the cost to serve, how much recurs after the first audit, and the cost to win a customer | Setting the fee per customer (F-7) and the fee share (F-8) were deferred to segment selection (Q6) on 2026-09-14 (`0_criteria.md` §6). Averages hide a very wide spread: per-shipper savings run $3.6k-33k a year (`3_factsheets.md` C-09 item 3) | **Supported as measurement.** Measuring the numbers is squarely S5 work; *setting* a price stays with Q6 unless the founders bring it forward (§1.4, point 4) |
| **(d) "Interviews will be focused on C-09 specific segments and customers"** | C-09 is flagged K2 = S, so it must be split into segments (`2_knockouts.md` §4.5). Sampling across its candidate segments now tells Q6 where the pain actually is. The strict durability test already says the segment must come from defensive shipper groups (`4_scorecard.md` §9.3). **P-23, if adopted, lets one shipper interview also count for C-11 and C-19** when their incident modules are done in full, so C-09-focused shipper interviews gather backup evidence cheaply | Option B as written runs S5 on all four finalists. Interviews on C-09 alone would move toward option C or D, which `6_decision.md` §4 flags as a process change (C) or as breaking S6's entry condition (D). Choosing a segment is Q6's job, not S5's | **Needs one clarification** (§1.4, point 1). Two readings: C-09 goes first and deepest while the other three still get their S5 coverage (B as written), or C-09 only (a process change, logged in `submarket_selection.md` §9). Both are workable; they differ in how much capacity goes to C-11, C-19 and C-20 |
| **(e) Web research before the interviews** | Cheap, and it can answer questions that don't need a person: rates, prices, public complaints, competitors, channels. It sharpens the probes | The Mom Test's point is that the evidence that counts is a specific past event and a commitment from the person who pays. Forums can't supply either. Online complaints skew negative and toward larger firms | **Supported for preparation.** Web findings are logged as desk evidence (*assumed* where anecdotal) and do not count toward the S5 gate (`5_interview_kit.md` §1.4). See §7.5 for what the web could and couldn't answer |

*Note (D-23, 2026-10-08):* row (b) above reads C-09's fee case as "contingency audit an existing contract shape". Since D-23, C-09 is software sold as a service, and its fee form (a share of recoveries or a subscription) is open until Q6. The S4 fee-feasibility scores are not re-scored here.

### 1.3 What doesn't change
- **The S5 gate for C-09** (`5_validation.md` §8):
  - 5 shipper interviews and 5 carrier interviews;
  - 3 costed incidents and 2 commitments on the shipper side;
  - a named data source with one interviewee willing to share it;
  - one savings assessment on real data.
- **The fee rule** in CLAUDE.md ("the fee has to come out of savings") and D-9 (C-08 demoted).
- **The frozen criteria** in `0_criteria.md`.
- **What stays deferred to Q6:** the entry side (F-5), the firm-size floor (F-6), the fee per customer (F-7) and the fee share (F-8).

### 1.4 Finalized decision

**We will make this together once research is done.** The points to settle:

| # | Point | Options | Suggested starting point **[our call]** |
|---|---|---|---|
| 1 | **Scope of S5 under B** | (a) C-09 first and deepest; C-11, C-19 and C-20 keep their S5 coverage (B as written) · (b) C-09 plus its two same-core backups (C-11, C-19) through P-23's shared shipper interviews; C-20 paused · (c) C-09 only, a process change | **(a) or (b).** (b) costs little extra, because the same shipper interview covers all three cards' incident modules. Pausing C-20 leaves the one card from the other family untested |
| 2 | **C-09's first product (the wedge)** | Audit-only look-back paid from recoveries (Axis W 65, Cohen 10.0) · audit and pay from day one (W 55, Cohen 1.00) | **Audit-only first**, with the payment half as a growth option (`6_decision.md` §4). S6 step 3 writes the wedge hypothesis at confirmation. **Decided 2026-10-03 (founders): audit only first.** Verbatim: "I have decided the first rendition will just be an audit machine, we can do payments later". Recorded with the evidence for and against in `software-initial-pitch.md` §1 |
| 3 | **D-14 to D-20** (`5_validation.md` §10) | Adopt, change or reject each | As suggested there. **P-25 (the 1-10 anchors) must be settled before the first interview** |
| 4 | **Per-customer profit** | Measure it at S5 and set the price at Q6 (as deferred) · bring F-7 and F-8 forward to now | **Measure now, price at Q6.** F-7 and F-8 were deferred on 2026-09-14 as "not a sub-market-selection decision" (`submarket_selection.md` §4 S0.3). Measuring doesn't reopen that, but setting a price would. **Settled in part 2026-09-22 (D-21, C22):** the desk model is now formal, and a kill condition is fixed before the measurement (§4.5). The price is still set at Q6 |
| 5 | **Changes to the C-09 interview kit from checks X, Y and Z** | Adopt, change or reject each: screen on 20-499 staff plus freight spend of $250k or more; the person who checks the bills (often logistics) as the primary interviewee, with the controller or CFO as the budget voice; the sampling grid (§5.3); the extra numbers and probes (§7.3, §7.6); the screener and messages (check Y §12-§13); LTL booking tools' audit screens added to the show-stopper test (§7.5) | **Adopt**, before the first outreach. None changes the gate or the frozen criteria |
| 6 | **Who does the review work: a software company or an audit firm (D-23)** | — | **Decided 2026-10-08 (founders).** Verbatim: "We have no analysts, this is a software company. A software as a service, we do no manual reviews here." The software flags the errors; the customer's own staff review them and file the disputes; help with filing comes later; the customer uploads its rate agreements and the software reads them. The rule is company-wide, so C-19 is flagged for the same re-run later. The kill test is re-run on this basis (`handoff_c09_software_rerun.md`); the frozen lines stay in force until the founders adopt new ones. Recorded in full, with the evidence for and against, in `software-initial-pitch.md` §1A |

---

## 2. C-09 on one page

| Item | What the run found | Where |
|---|---|---|
| **The job** | "Checking and paying truckload and LTL freight bills, for mid-sized manufacturers and distributors, handled today by accounts-payable clerks, contingency audit firms and, for larger shippers, audit-and-payment providers." The job statement: "Pay only what we owe, on time." | `1_candidates.md` C-09 |
| **Who pays, who uses** | Pays and decides: the shipper's finance team (controller, AP), with logistics co-deciding. Users: AP clerks and logistics coordinators; at carriers, billing clerks | `1_candidates.md`; `3_factsheets.md` item 7 |
| **Buyers** | 95,579 US manufacturers (57,309) and wholesalers (38,270) with 20-499 staff, *verified* (N-E17) | `3_factsheets.md` §2.2 |
| **Savings pool** | $0.34-3.2B a year: truckload plus LTL spend of $451B (*assumed*) × 15-30% mid-sized × 1-3% overpaid × 50-80% caught **[our call]** | item 2 |
| **Fee pool** | Central **$209M** (20% of the midpoint). Per shipper: saving $3.6k-33k a year; a 20% fee is $0.7k-6.7k; the average fee is about $2,200 | item 3; `6_decision.md` §1 |
| **Customers needed** | About 1,150 for the $2.5M floor (1.2% of buyers) at the central average **[our calc]** | `6_decision.md` §1 |
| **Scores (S4)** | Axis A 92.5 (A1 1, A2 1, A3 1, A4 0.5, A5 1, A6 1) · Axis W 55 (W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.5) | `4_scorecard.md` §2.1 |
| **Fee gate** | F1 1 · F2 1 · F3 1 · F4 0.5 · F5 1 = 3.5 + 1, the strongest of the five | `4_scorecard.md` §3 |
| **Cohen** | 1.00 as written (weak link: Liquid, meaning the ERP and bank change); **10.00 audit-first** | §4.2 |
| **Durability** | Knock-out K11 passes (Cass invoice count -10.5% in 2008-09, -6.4% in 2022-25). Strict test: **passes for defensive shipper groups only** (branded nondurables -1.1%, packaging -3.5%, agribusiness -3.7%, forest and paper -5.6%, consumer durables -7.4%, capital goods -7.7%, building materials -8.0%); **fails** for auto -16.5%, downstream metals -17.4%, homebuilders -20.1% | `2_knockouts.md` §4.3; `4_scorecard.md` §6.5 |
| **Dated triggers** | NMFC class dockets (2025-07-19; 2026-05-23) change LTL bills after pickup (*verified*). Payment fraud hit 76% of US firms in 2025 (AFP, association) | `4_scorecard.md` A3 |
| **Competition** | 16 named (Cass, U.S. Bank, Trax, nVision Global, CTSI-Global, Intelligent Audit, CT Logistics, Data2Logistics, RateLinx, TranzAct, enVista, Loop, Freehand, Freightgate, FreightPOP, MyCarrier). No dominance. "numerous small transportation bill audit firms" (Cass 10-K). Funded AI entrants: Loop ($95M Series C, April 2026). **Added by check Z:** Loop absorbed Data2Logistics (2025); LTL booking tools with invoice-audit screens (Freightview, MyCarrier, FreightPOP) already serve small and mid-sized manufacturers and distributors; mid-market audit pitches from Eller Audit, ValueXPA, Zero Down and US Tech Automations; Freehand ($75M) targets enterprises | `3_factsheets.md` item 9; check Z §7, §14 |
| **Dependencies** | A bank partner, for the paying half only | `6_decision.md` §1 |
| **Sides at S5** | Shippers: the paying side. Carriers: could buy from us (payment rail, faster payment), and are also the party that must accept audit short-pays | `5_validation.md` §2 |
| **Harder side** | The shipper side (*assumed*, S1) | `1_candidates.md` |
| **Family** | "Money back after shipping": C-09, C-10 (claims) and C-11 (LTL disputes) share one set of data (BOL, POD, invoice, rate, class) and one budget story (fees paid from recoveries). C-19 shares the buyer. C-12 (parcel audit, reserve list) shares the job | `3_factsheets.md` §2.2; `3_shortlist.md` §1 |

---

## 3. What each stage learned about C-09

| Stage and file | What it found for C-09 | What it means now |
|---|---|---|
| **S0** `0_criteria.md` | Floor $2.5M a year by year 5, stretch $10M; K5 size floor a $25M fee pool; weights A 20/10/25/15/15/15 and W 20/5/20/15/15/25; fee shares modelled at 10/20/35% as assumptions; F1-F4 cut at 3. Deferred to Q6: entry side, size floor, fee per customer, fee share. Check A's parked benchmark: direct selling stays economic at **about $5k or more a year per customer**, payback within 12 months, gross retention of about 88% or better (`research/s0_check_A_ambition_economics.md` §A3) | The $5k benchmark is the yardstick for §4's per-customer numbers. It is parked with F-7, not a rule |
| **S1** `1_candidates.md` | Card created from the grid (in-house AP clerks and job-specific audit firms × mid-sized shippers) and from R28's "invoice processing". Sub-market signs 4 of 5; channels unknown. Reefer freight of food makers merged in as a segment variable (M-2). C-09 and C-12 kept apart (different customers and competitors) | Channels were the one unknown from the start, and they still are (§6) |
| **S2** `2_knockouts.md` | **Passed every knock-out.** K2 = S, split by shipper industry. Invoices fell 10.5% (2008-09) and 6.4% (2022-25). Savings pool $0.34-3.2B, and one of seven cards clearing K5 even at a 10% share of the low end | Big enough under any fee share tested. Must be segmented |
| **S3a** `3a_unknowns.md` | Still a clean pass (with C-15, one of only two). Manufacturing's customer-survival flag is clear, but exits outnumber entries, so the pool shrinks slowly. C-12 parcel audit went to the reserve list ($12M central, or $25M on the floor reading) | Parcel audit is a growth option, not a backup |
| **S3b** `3_factsheets.md`, `3_shortlist.md` | Fact sheet written. Desk score A 92.5 / W 65 (W6 set to 0.5 against check R's 1, because of funded AI entrants and the bank partner). Shortlisted joint 2nd. Mid-sized shippers use "an AP clerk, a small audit firm, or nobody" (**[our call]**, no survey) | The mid-market gap rests on vendor and enterprise figures, and S5 must test it (H09-01, H09-08) |
| **S4** `4_scorecard.md` | W3 1 → 0.5, applying "score the job" (D-10, accepted). Fee gate strongest (3.5 + F5 1): "The row that makes C-09 hardest to build is the row that makes its fee easiest to charge." Cohen 1.00, or 10.00 audit-first. No show-stopper, "the most open field of the five". Strict durability conditional on shipper group (carried to Q6). A3 = 0.5 would drop C-09 to last. Deciding factor 6: the only card inside a money flow | The audit-first wedge is worth 10 points of W and ×10 on Cohen. S5 must ask: does a look-back on real invoices find 1-3%, and will a controller pay a startup a contingency? |
| **S4 decisions** | D-9: C-08 demoted, fee rule kept. D-11: four unranked to S5. D-12: C-09's carriers get 5 full interviews (they could buy from us). C19: no change to C-09 | The carrier side stays in C-09's gate |
| **S5 desk** `5_validation.md`, `5_interview_kit.md`, `5_log.md`, check V | 15 hypotheses (H09-01 to H09-11, H09-C1 to C4). Guides §5.1 (shippers) and §5.2 (carriers). Look-back audit protocol and price test (25% of credits, or $500 flat, or free). Recruiting: shipper finance ranked **5th of 7 sides** (panel plus Sales Navigator; no gathering place), carriers 2nd (FMCSA census). No interviews yet | The kit is ready. Recruiting the shipper side is the main practical risk |
| **S6 briefing** `6_decision.md` | For: biggest prize, strongest fee case, only card in the payment, most open field, same data as neighbours. Against: lowest W, funded AI rivals, hard to reach, guessed rate, durable only in steady industries. Backups C-11 and C-19; growth options C-10, C-12, paying carriers, payee checks (C-08's identity core). Risks: "whether shippers really overpay, and whether a controller will share invoices with a startup. One assessment tests both" | This file |

---

## 4. The money: are the margins right, and what is one customer worth?

### 4.1 The chain the interviews have to fill

> **Service basis, superseded by D-23 (2026-10-08).** The chain below, and every model in §4.2-§4.5, assumed an audit service: our own analysts reviewed flagged bills and we filed the disputes. Under D-23 the software flags the errors, and the **customer's own staff** review them and file. So the "cost to serve" rows lose their people line: of the old $1.12 per bill, $0.10 (machine reading) stays ours, and $1.02 becomes the customer's time **[our calc]**. The chain gains a link, **follow-through**: the share of flags the customer's staff actually work and file. The fee form (a share of recoveries or a subscription) is open until Q6. The model is re-derived in `handoff_c09_software_rerun.md`; the text below is kept as the record.

**Our fee from one customer = freight spend × overcharge rate × share we catch × share the carrier actually credits × our fee share.**
**Gross profit from that customer = our fee − the cost to serve them.**
**Whether the customer is worth winning = gross profit against the cost to win them (CAC), over how long they stay.**

| Link | Desk value | Label | What is missing | How S5 gets it |
|---|---|---|---|---|
| Freight spend per customer | Average $0.71-1.41M a year ($68-135B ÷ 95,579) | base *assumed*; average **[our calc]** | The spread by size and industry; the truckload / LTL / parcel split | Block A question (proposed, §7.3); check X |
| Overcharge rate | 1-3% (vendors claim 2-8%) | **[our call]** | Any neutral rate | **Savings assessment** (kit §6.1): flagged $ ÷ spend; check X |
| Share caught | 50-80% | **[our call]** | Everything | Assessment: what a careful re-rate finds against what the shipper already caught |
| **Share carriers actually credit** | **Not in the desk model** (it assumes every caught overcharge comes back) | gap | Everything | Assessment step 5 (still inside the windows?); what happened to flagged claims; check X |
| Fee share | Modelled 10/20/35%; the price test offers 25%; audit firms take 25-50% | *assumed* / **[our call]** | What a controller accepts from a startup | **Price test** (kit §6.1); check X |
| Cost to serve | Not modelled | gap | ~~Hours per customer per month; dispute follow-up time~~ *D-23:* our software cost per customer; the review and dispute hours are the customer's | Assessment: ~~"Also record the hours spent" (kit §6.1)~~ *D-23:* time the customer's reviewer on the flags |
| One-off against recurring | Not modelled | gap | How much of year one is backlog; whether errors fall once carriers know bills are checked | Interviews (block D); check X |
| Cost to win a customer | Not modelled; benchmark inside sales CAC $5k-15k (check A, Tunguz, *verified* as stated) | benchmark | Everything for this buyer | The recruiting funnel is the first proxy (`5_log.md` §1: founder hours and cash per held interview) |

### 4.2 A worked example **[our calc]** on the desk ranges

*Check X (§4.3) found the desk ranges optimistic: the neutral rates are lower, and it adds a credited share and a cost to serve. This example is kept as the desk's starting point.*

**One manufacturer spending $1M a year on truckload and LTL freight (close to the average):**
- Overcharged 2% = $20,000; we catch 65% = **$13,000 found**.
- If carriers credit all of it, a 25% fee = **$3,250 a year**. If they credit only 70% (an illustration, not a finding), the fee is **$2,275**.

**The same chain across three sizes and the desk's low, central and high rates:**

| Freight spend a year | Rate × caught | Found | Fee at 20% | Fee at 25% | Fee at 35% | Fee at 25% if 70% is credited |
|---|---|---|---|---|---|---|
| $250k | low 1% × 50% | $1,250 | $250 | $312 | $438 | $219 |
| $250k | central 2% × 65% | $3,250 | $650 | $812 | $1,138 | $569 |
| $250k | high 3% × 80% | $6,000 | $1,200 | $1,500 | $2,100 | $1,050 |
| **$1M** | low | $5,000 | $1,000 | $1,250 | $1,750 | $875 |
| **$1M** | **central** | **$13,000** | **$2,600** | **$3,250** | **$4,550** | **$2,275** |
| **$1M** | high | $24,000 | $4,800 | $6,000 | $8,400 | $4,200 |
| $3M | low | $15,000 | $3,000 | $3,750 | $5,250 | $2,625 |
| $3M | central | $39,000 | $7,800 | $9,750 | $13,650 | $6,825 |
| $3M | high | $72,000 | $14,400 | $18,000 | $25,200 | $12,600 |

**The freight spend at which one customer pays us $5k a year** (fee at 25%):

| Rates | If carriers credit 100% | If they credit 70% |
|---|---|---|
| Low (1% × 50%) | $4.0M | $5.7M |
| Central (2% × 65%) | $1.5M | $2.2M |
| High (3% × 80%) | $0.83M | $1.2M |

**What the example says:**
1. **At the desk's central rates, the average mid-sized shipper pays us about $2-3k a year, below check A's $5k benchmark for direct selling.** A customer clears $5k only above about $1.5-2.2M of freight spend, or if the real overcharge rate sits at the high end. So the interview has to capture each firm's freight spend, and the segment question (Q6) is partly a size question.
2. **The first year can be larger than later years.** A look-back can reach bills still inside the dispute windows: 180 days for billing disputes under 49 U.S.C. 13710(a)(3), and often counted from earlier dates in carrier tariffs (check T, *verified*). So year one can carry up to about half a year of backlog on top of the run-rate, **[our call]**, if the windows apply to the bill. Whether errors keep coming after carriers know bills are checked decides the recurring fee.
3. **Gross profit per customer is unknown until the hours are measured.** ~~An illustration only: if one customer takes 2 hours of analyst time a month at $40 an hour ($960 a year), the $1M central customer at 25% leaves about $2,300 of gross profit (about 70%) **[our calc on an assumed cost]**. Replace it with the hours recorded in the first assessment.~~ *Superseded by D-23 (2026-10-08): we employ no analysts, so there is no analyst time to cost. Our gross profit is the fee less software costs (reading, storage, support, licences), re-derived in `handoff_c09_software_rerun.md`.*
4. **The payback on winning that customer is the real test of "is a customer worth it".** At check A's inside-sales CAC of $5k-15k, a customer yielding $2,300 of gross profit a year takes about 2-6.5 years to pay back **[our calc]**, against the 12 months or less that check A's sources ask of SMB software. The ways out are larger shippers, a higher real rate, a cheap channel (partners, ERP marketplaces, referrals), or a lower cost of winning. Those are Q6 questions, but S5 collects the numbers.
5. **The company-level check:** $2.5M of revenue at about $2,600 a customer is about 960 customers. At the 10% company margin used as the planning value in check A §3, that yields the founders' $250k profit **[our calc]**.

### 4.3 What check X found (`research/s5_check_X_c09_money.md`, 2026-09-17)

> **Service basis, superseded by D-23 (2026-10-08).** The evidence on overcharge rates, recoveries and prices below still stands. The cost-to-serve comparisons (PRGX's human-heavy model; "lean automated cost to serve … $12 a dispute") assumed our own staff. Under D-23 those minutes are the customer's. Re-run: `handoff_c09_software_rerun.md`.

**The headline: the one input that decides the model has no neutral measurement for private shippers, and every neutral figure found sits below the desk's 1-3%.**

**Re-checked at the source here:** the GSA Inspector General report, GAO 1992, GAO 1999 and Establish Davis. The quoted figures match. PRGX's 10-K was not re-read, because SEC.gov refuses requests that don't declare a contact.

| Link in the chain | What the web shows | Label |
|---|---|---|
| **Overcharge rate** | **Federal post-payment audit:** $33.1M of overcharges issued on bills paid 2007-09, against about $16.3B a year of federal transportation bills. That is about **0.07% a year** [our calc]. It is the residue *after* agencies' own pre-payment audits, it includes air passenger bills, and the $16.3B is a FY2012 figure, so it is a floor, not a rate for C-09's shippers. **Recovery audit of general purchases:** 0.48% of purchases for a new client, falling to about 0.1% once fixes are in (PRG's own figure, reported by GAO 1999). **Vendors' 2-8%:** no traceable original; several widely quoted statistics are "orphan attributions that vendor blogs quote from each other" | GSA OIG A120169 and GAO T-NSIAD-99-213 *verified* (re-read here); rates in vendor copy *assumed* |
| **Share caught** | One professional audit found **78%** (motor freight) and **72%** (household goods) of the overcharge dollars that two audits in a row found (GSA, 1989-91) | GAO/NSIAD-92-157, *verified* (re-read here) |
| **Share credited** | GSA collected **81%** of overcharges by value (45-96% by contractor). **Delay destroys collection:** under 10% uncollected when issued within 400 days, over 25% at 600-799 days, nearly 35% at 800 days or more. GSA can deduct from later bills for 3 years; a private shipper can only offset against a carrier it still uses. **Truckload contracts under 49 U.S.C. 14101(b) can replace the 180-day rule** with the contract's own terms, in either direction | GSA OIG *verified* (re-read here); waiver reading **[our call]** |
| **Fee share** | 25-50% is the freight norm. **Small shippers are commonly offered 50/50** (vendor). Large buyers pay far less: GSA 3.9% plus $0.28 a bill on first audits (1989-91), DoD 20%, Texas 13.5%, Medicare auditors 9-12.5%. SMB shipping tools with some audit features cost $0-200 a month (MyCarrier $0/$60/$200; Freightview $149). Cass earns about $2.38 in fees per item processed | government *verified*; vendor *assumed*; stated prices *verified* |
| **Cost to serve** | PRGX, the only public recovery-audit comparable (human-heavy), ran a **gross margin of 35-39%** with about $107k of revenue per employee. **No time-per-invoice figure for freight audit exists publicly** | PRGX 10-K via check X (*verified* there, not re-read here) |
| **Freight spend per shipper** | Bottom-up (SUSB receipts × Establish Davis's **3.68%** of sales on transportation × a TL+LTL share [our call]): **central $0.77M a year**, at the low end of the desk's $0.71-1.41M. By group: manufacturers with 20-99 staff **$0.27M**; with 100-499 staff $1.59M; wholesalers with 20-99 staff $0.63M; with 100-499 staff $2.90M. Firms with 100-499 staff are 21% of the count and hold 57% of the spend | receipts and 3.68% *verified*; shares **[our call]**; spend **[our calc]** |
| **Recurrence** | General recovery-audit rates fall about 80% once fixes are in; PRGX's commercial clients buy audits "every two to three years". On check X's central inputs, the backlog is about 46% of first-year recoveries. No freight-specific decay figure | *verified* (PRGX, GAO); **[our calc]** |
| **Cost to win** | Not found. PRGX: annuity-like audits "require a relatively long sales cycle and a relatively high level of direct person-to-person contact" | *verified* via check X |

**Check X's per-customer model.**
- **Rates [our call]:** central 1.5% overcharged × 70% caught × 80% credited = **0.84% of TL+LTL spend recovered**. Low: 0.5% × 50% × 60% = 0.15%. High: 3% × 85% × 90% = 2.3%.
- **Lean automated cost to serve [our call, no source]:** $0.50 an invoice, $12 a dispute, $600 a year fixed, plus $1,000 of onboarding.

| TL+LTL spend a year | $250k | $1M | $3M |
|---|---|---|---|
| Recoveries a year (central) | $2,100 | $8,400 | $25,200 |
| Fee at 25% (central) | $525 | $2,100 | $6,300 |
| Cost to serve (central) | $905 | $1,820 | $4,260 |
| **Gross profit at 25%: low / central / high** | −$721 / **−$380** / $409 | −$1,085 / **$280** / $3,438 | −$2,055 / **$2,040** / $11,512 |

| Rates | Spend where a 25% fee covers the cost to serve | Spend where a 25% fee reaches $5k a year |
|---|---|---|
| Low (0.15% recovered) | never | $13.3M |
| **Central (0.84%)** | **$0.68M** | **$2.4M** |
| High (2.3%) | $0.15M | $0.87M |

**How much of this is evidence** (added 2026-09-17 after the founders asked for the sources and the math):

| Input | Value in the model | Source | Status |
|---|---|---|---|
| Receipts per firm | $12.3M / $72.0M / $43.0M / $197.3M | Census SUSB 2022 | *verified*, re-checked at the source |
| Transportation as a share of sales | 3.68% | Establish Davis 2020 (participating firms, which skew larger; the report says size moves costs "up to 50%", lower for larger firms) | *verified*, re-checked |
| TL+LTL share of transportation cost | 60% for manufacturers, 40% for wholesalers | Loosely anchored on CFS mode shares by value | **[our call]** |
| **Overcharge rate** | **1.5% (low 0.5%, high 3%)** | The midpoint of the desk's own 1-3% guess. **The neutral sources (0.07%, 0.1-0.48%) do not measure unaudited private truckload or LTL bills,** so they bound the rate without setting it | **[our call]** |
| Share caught | 70% | GAO 1992: one audit found 72-78% of what two audits found | anchored, *verified* |
| Share credited | 80% | GSA OIG: 81% collected by value, by a government with offset powers | anchored, *verified* |
| Fee share | 25% | The S5 price test's proposal | **[our call]** |
| Cost per invoice | $0.50 | Between GSA's 1989 data-capture fee ($0.28) and Cass's processing fee per item ($1.56), both for different services | **[our call]** |
| Cost per dispute; share of invoices disputed | $12; 6% | No source; vendor claims of 3.8-10% of invoices with errors | **[our call]** / *assumed* |
| **Fixed cost per customer** | **$600 a year** | **No source** | **[our call]** |
| Human-heavy alternative | Cost = 60% of the fee | PRGX 2018: cost of revenue $104.8M on revenue $171.8M = 61.0% | *verified*, re-checked |

**Which assumptions carry the result** [our calc] (fee 25%, 70% caught, 80% credited, 6% disputed):
- **The overcharge rate decides whether any customer covers variable cost.** Fee per dollar of spend = rate × 0.14. Variable cost per dollar = $1.22 per $1,000. So the contribution is positive only above an overcharge rate of **0.87%**.
- **The unsourced $600 fixed cost decides the small-firm result.** The typical 20-99-staff manufacturer ($272k of spend) makes these yearly gross profits:

  | Overcharge rate | Fixed cost $0 | Fixed cost $300 | Fixed cost $600 |
  |---|---|---|---|
  | 1.0% | +$49 | −$251 | −$551 |
  | 1.5% | +$239 | −$61 | −$361 |
  | 3.0% | +$811 | +$511 | +$211 |

**What this changes [our call]:**
1. **"Are our margins right?" becomes "at what overcharge rate and what customer size?"** On check X's illustrative inputs, a customer covers its cost above about $0.7M of TL+LTL spend and pays $5k a year above about $2.4M, and the typical 20-99-staff manufacturer (about $0.27M) would not cover the $600 a year of fixed cost. That fixed cost is unsourced: without it, the same customer contributes about $240 a year at the central rate [our calc]. The result is a sensitivity, not a finding. On check X's shape-only reading, about 28,000 firms clear break-even and about 5,400 reach $5k (ceilings, because means overstate the typical firm).
2. **The savings assessment is the decisive test, and H09-02's fail line (under 0.5%) is a realistic outcome,** not a remote one. A move from 0.5% to 1.5% flips every column from loss to profit.
3. **§4.2's desk example is optimistic.** At $1M of spend, the desk's central fee of $3,250 becomes $2,100 once a credited share is included, and about $280 of gross profit once a lean cost to serve is taken off.
4. **The fee pool still clears the K5 floor on the central case.** Re-cut bottom-up, it is central $155M at 25% (against the desk's $209M at 20%). The low case, $12M, would not clear it.
5. **Price and size go together.** 25% is below the 50/50 small shippers are already offered (so H09-06 leans for on acceptance), but on check X's unsourced cost inputs, small accounts would not cover their cost at 25%. Pricing by account size is an F-7 and F-8 question for Q6. S5 records the answers.
6. **Speed beats depth.** Collection falls as claims age, so a monthly audit collects more per dollar found than a once-a-year look-back. That bears on the wedge (§1.4, point 2), but a pre-payment audit leaves no recovery to take a share of.
7. **For the segment sampling (§5.2):** weight the interviews toward firms with 100-499 staff, where most of the spend is, and keep 1-2 small firms to test whether their rates are high enough.

---

### 4.4 The second round: checks AA, AB and AC (2026-09-17)

The founders asked for better numbers on the three inputs that decide the margin, and for example invoices. Three more checks ran.

- `research/s5_check_AA_c09_cost_to_serve.md`: what it costs to serve one customer.
- `research/s5_check_AB_c09_private_recoveries.md`: what audits of private shippers actually find and get back.
- `research/s5_check_AC_c09_example_invoices.md`: real invoices and the documents an audit checks them against.

**Re-checked at the source here:** the BLS clerk wage and compensation series, AWS Textract's page price, Saia's revenue per LTL shipment, the USDA 1980 co-operative survey, the Tenth Circuit's *Southern Furniture* opinion, and the ABF court exhibit, including re-doing one invoice's arithmetic. All match.

#### 4.4.1 Cost to serve, now sourced (check AA)

> **Service basis, superseded by D-23 (2026-10-08).** In the table below, the machine-reading row ($0.10) stays our cost. The human-review row ($0.55) and the dispute row ($9.30, about 15 minutes) are now the **customer's own staff time**, because the customer reviews and files. The fixed cost becomes the customer's onboarding time, plus our support and platform costs. Re-run: `handoff_c09_software_rerun.md`.

| Input | Check X guess | Sourced replacement (central) | What it rests on |
|---|---|---|---|
| Reading and matching one invoice packet by machine | part of $0.50 | **$0.10** ($0.005-0.50) | AWS Textract $0.01 a page and Azure $10 per 1,000 pages (*verified*); an LLM reading a 3-5 page packet costs $0.001-0.24 [our calc] |
| Human review of the packets that need it | not modelled | **$0.55** = 15% of packets × 6 minutes × $36.79 an hour | BLS May 2025 clerk mean $25.75 an hour, grossed up by the 70.0% wage share (*verified*); the share and the minutes are **[our call]** |
| **Per invoice, total** | $0.50 | **$0.65** ($0.035-4.20) | |
| Per dispute | $12 | **$9.30** (15 minutes) | Same wage. No public figure for minutes per overcharge dispute exists |
| Share of invoices disputed | 6% | **5%** | The only non-vendor figure: an SJ Consulting survey found LTL billing accuracy of 94-99%, about 97% on average (*assumed*, read through a secondary page) |
| Fixed per customer a year | $600 | **$400** ($150-1,100) | 100-250 accounts per SMB customer-success manager |
| Onboarding | $1,000 | **$400** ($110-1,500) | Hours still **[our call]** |
| **Invoices per $1,000 of spend** | 1.0 | **1.5** (1.0-2.9) | An LTL bill averages **$347.81** (Saia, FY2024, *verified*) against Cass's all-mode $1,011. An LTL-heavy shipper has about twice as many bills per dollar |

- **Machine reading is cheap; people are the cost.** $0.55 of the $0.65 is human review.
- **A fully manual audit does not fit a 25% fee.** Vendors put a manual audit at 8-13 minutes an invoice. At a US clerk's loaded wage that is about 1.1% of spend, against a central fee of 0.2%.
- **Margin benchmarks:** human-heavy recovery audit 35-45% (PRGX), outsourcers 35-38%, AI-native products 45-53%, AP software 60-86%.

#### 4.4.2 What audits actually recover (check AB)

- **Only six published cases give both a freight spend and an overcharge amount.** The implied rates are 0.80%, 0.87%, 1.00%, 2.60%, 2.92% and 4.23% of spend, a **median of 1.80%** [our calc]. **Five of the six are large shippers** ($8.5M-$100M+ of spend) in a first-year programme. The only one plausibly inside our segment (a $22M-revenue chemical maker) is the highest, at 4.2% of 24 months' spend, and it is a vendor's own write-up. This is a selected sample of vendors' best results.
- **The one neutral private measurement is from 1977.** USDA surveyed 445 farm co-operatives; the 34 that could report both numbers collected **$2,193,447 against $486.4M of regulated transport cost, "just 0.45 percent"** (*verified*). Auditors then charged "usually 50 percent" of recoveries.
- **Mature programmes yield less:** a post-audit specialist puts its own yield at 0.5-1.5% of non-parcel spend after other audits; another provider says ongoing savings are "around one-half of 1%". Every provider that splits year one from later years reports a large fall.
- **The carrier side caps it.** FedEx Freight, the largest LTL carrier, books all post-billing revenue give-backs in one line: **2.6% of revenue (FY2024), 1.3% (FY2025), 2.1% (FY2026)** [our calc on *verified* filings]. That is every credit for every reason, so it is a ceiling on what LTL customers get back, not a measure of billing errors.
- **Share credited:** 60-90% when disputes are filed promptly, 41-51% when they age. Check AB suggests lowering the model's central credited share from 80% to **75%**.
- **The law caps a look-back.** In *Southern Furniture Leasing v. YRC* (10th Cir., 2021) a class action over a concealed decade-long reweigh practice was dismissed as time-barred: **"compliance with the 180-day time limit is not optional"** (*verified*). On a 12-month look-back of evenly spread bills, only about the recent half is still inside that window on day one.

#### 4.4.3 Real invoices exist, in court records (check AC)

| Set | What it is | Why it matters |
|---|---|---|
| **101 ABF Freight bills**, 9 May to 9 Aug 2024, filed in a supplement maker's bankruptcy | A ready-made 3-month sample, with full rating detail: tariff, discount 89.5%, deficit weight, absolute minimum charge, fuel %, lumper, detention, reweigh authorisations, measured cube and rated dimensions | **I downloaded and checked it myself:** 107 pages, 6 bills attached twice, 29 reweigh notes, 40 minimum-charge adjustments, and invoice 150235531 reconciles to the cent |
| **6 XPO invoices** with their bills of lading and delivery receipts | Shows what a shipper holds end to end | Reweigh fees on 3 of 6, late fees on 4 of 6 |
| **~75 SEFL bills, plus that shipper's pricing agreement in three dated versions, plus its own overcharge worksheet** (3,645 invoices, $271,828.70 claimed) | The only public set where bills **and** the agreement they should follow are both available | One bill matches the agreement on discount (90.30%), FAK class 70 and the $55 liftgate |

- **What the invoices already tell us:** on all 57 ABF bills with the needed lines, fuel is charged on net linehaul only, never on accessorials. Detention was added on a corrected invoice with no arrival or departure times shown. 28% of bills carry a reweigh note.
- **Not public, and only obtainable from a shipper:** truckload invoices, carriers' base rate tables, the fuel table in force in a given week, weight and inspection certificates, detention timestamps, lumper receipts, AP payment records, and dispute and credit history. Check AC §9 turns these into a request list for interviews.
- **A caution from check AC:** the public shipper worksheet claims 22-25% of base freight, but it ignores a rate-increase clause and pallet exclusions in its own agreement. A look-back that does the same would overstate recoveries.

#### 4.4.4 The model with the second round's inputs [our calc]

> **Service basis, superseded by D-23 (2026-10-08).** This model costs our own reviewers (US and offshore) and a 25% contingency share. Under D-23 neither holds: there are no reviewers of ours, and the fee form is open. The table is kept as the record. The software-basis model is re-derived in `handoff_c09_software_rerun.md`, and its result will go in `4_kill_conditions.md` §2.5.

Central case: overcharge 1.5%, caught 70%, **credited 75%**, fee 25%, AI-heavy costs above, 1.5 invoices per $1,000.

| Truckload and LTL spend a year | $272k | $633k | $1.59M | $2.9M |
|---|---|---|---|---|
| Recoveries | $2,142 | $4,985 | $12,521 | $22,837 |
| Fee at 25% | $536 | $1,246 | $3,130 | $5,709 |
| Cost to serve (variable + $400 fixed) | $855 | $1,459 | $3,059 | $5,250 |
| **Gross profit a year** | **−$319** | **−$212** | **+$71** | **+$459** |

| Question | Answer |
|---|---|
| Break-even spend | **$1.35M** (check X said $0.68M) |
| Overcharge rate needed to cover variable cost | **1.27%** |
| The same with offshore reviewers ($0.28 an invoice) | Break-even **$303k**; rate needed **0.50%** |
| A 12-month look-back, collecting on only the half still inside the 180-day window | Fee of $0.98 per $1,000 of spend against a cost of $1.67. **It loses money at every size** |
| An ongoing programme at a mature 0.75% error rate, US costs | Loses money at 25%. It needs a share of about **45%** to break even, or offshore costs |

#### 4.4.5 The practice audit (run 2026-09-17)

The founders asked for it, so the look-back was rehearsed on the public ABF set: 101 real bills, $45,652.49, May-August 2024. Full record: `research/s5_practice_audit_public_invoices.md`.

| Check | Result |
|---|---|
| Does each bill add up? | **101 of 101.** Carrier arithmetic is not where the money is |
| Discount | 89.5% on every bill, applied to linehaul only. Consistent, but unverifiable without the agreement |
| Minimum charge | **38% of bills sit exactly on a $180 floor.** On those, a rate audit has almost nothing to bite on |
| Fuel base | Charged on net linehaul, never on extras, on every parsable bill. **No error** |
| Fuel level | 1.3-1.5 points **below** ABF's published table every week for 14 weeks, checked against the EIA diesel index. A consistent, favourable gap: a negotiated schedule or an older table, not an error |
| Accessorials | **$5,939.28, 13.0% of everything billed**, across ten types |
| Duplicates | None. Six repeated pages are an exhibit artifact. Three bills share a date and amount but are different shipments — a **false-positive trap** on minimum-charge accounts |
| Corrections | **26 bills (27% of dollars) carry a reweigh note**; 2 carry detention with no times printed |

**What it proved:**
- **Recoverable dollars provable from public documents: $0.**
- **Dollars carrying a line that needs a document only the shipper has: $27,710.64, 61% of the total.**
- **The audit is not arithmetic; it is matching each bill to the right version of the right agreement.** The SEFL set, the only public one with its pricing agreement, shows the same account billed at four different discounts and two liftgate prices.
- **Two numbers for the cost model:** this LTL-heavy account runs at **2.21 invoices per $1,000 of spend** (the model assumed 1.5), and **58% of its bills carry a line needing a document or a judgement** (the model assumed a person looks at 15%). Both make an LTL-heavy small shipper the most expensive kind of customer to serve.
- **A worked example now exists to show interviewees:** one real bill, public, walked through line by line (§3.2 of the practice-audit file).

#### 4.4.6 What this changes [our call]

> **Partly superseded by D-23 (2026-10-08).** Points 2 and 5 assume our own review labour (US against offshore; a 50/50 contingency to cover it). Under D-23 the customer's staff do the review, so offshore review is moot and the contingency logic no longer covers our labour. Points 1, 3, 4 and 6 still hold, with one change to point 3: LTL-heavy shippers now cost **the customer** more review time per dollar, and cost us more reading.

1. **The single most useful design change: audit inside the claim window, then run monthly.** A deep look-back pays to read bills it cannot collect on. Matching the audit depth to the 180-day window turns the same work positive.
2. **Where the review work is done matters more than any fixed cost.** US-staffed review needs a 1.27% overcharge rate; offshore review needs 0.50%. Whether shippers accept offshore handling of their invoices is an interview question.
3. **LTL-heavy shippers cost about twice as much to serve per dollar of spend**, because their bills are a third the size. That cuts against the LTL-heavy segments in §5.3's grid, and it is measurable in the assessment.
4. **First-year and ongoing revenue are different businesses.** 1-3% in year one against 0.5-1.5% later. The recurring fee is thinner than the first year suggests, and a 25% share may not survive it.
5. **The 50/50 contingency that small shippers are offered may be arithmetic, not greed.** At mature error rates and US labour, that is roughly what covers the work.
6. **Some of this can now be tested before any interview,** on the real public invoices in §4.4.3 (§9, step 6a).

### 4.5 The kill condition (2026-09-22, D-21 and C22)

> **Superseded 2026-10-09 (C29):** the founders adopted the software-basis kill condition, `4_kill_conditions.md` §2.5.12 ("Adopt the Kill/Cover/Pass lines"). The text below is kept for the record.
>
> **Basis superseded by D-23 (2026-10-08); re-run pending.** The frozen lines below were derived from our own review cost (Test 1's 1.3% is where US-staffed review covers its labour; the middle band relies on offshore review or a 45% share; Test 3 measures our review cost). Under D-23 those costs are the customer's. The re-run is briefed in `handoff_c09_software_rerun.md`. **The lines stay frozen until the founders adopt new ones** (then a `submarket_selection.md` §9 entry), and no look-back starts before then.

**What was decided.** After the practice audit, the founders asked whether C-09 had become unreasonable and whether to pivot. The reading given (`4_scorecard.md` §9.1, D-21) was: the desk has shown one design to be thin, a look-back on a contingency share to an LTL-heavy shipper under about $1.5M of spend with US review; it has not measured the one number the business depends on, the overcharge rate on a mid-sized shipper's own bills; and the three alternatives carry the same class of unmeasured doubt. The founders adopted a **kill condition** as a new S4 step (C22), for later runs and applied now to all four finalists.

**Evidence for a kill line rather than a pivot:** the neutral rates all sit under 0.5% but none measures our segment (check X §2.6); the six vendor cases inside or near the segment run 0.8-4.2% (check AB §2.1); the S4 finding that the unknowns are bigger than the gaps between cards (`4_scorecard.md` §7); and SJ Consulting's survey (large LTL shippers, over $8B of charges) that carrier billing accuracy averages 97% and about half of bills of lading are wrong on weight or description, which cuts against C-11's dispute case as much as against C-09 (`handoff.md` §5).
**Evidence against, kept on the record:** every input that moved in the second round and the practice audit moved against C-09 (§4.4.4-§4.4.6); the practice-audit stress inputs (2.21 invoices per $1,000, 58% of bills needing a human) sink the model at any plausible rate; and the fee-from-savings rule may be hard to satisfy at SMB scale on any card, since mature audits of anything recover 0.1-0.5%.

**The condition, in full:** `4_kill_conditions.md` §2.4. In short: **kill** if the first real assessment measures under 0.75% of in-window spend billed wrong and provable, or if 2 of the first 3 shippers refuse the rate agreement and paid invoices under NDA, or if the measured minutes and bill counts give negative gross profit at a $1.5M customer under both US and offshore wages. **Pass** at 1.3% or more with positive gross profit at US wages. **Conditional** between, with the condition named. The lines are frozen as of 2026-09-22; the founders decide on the evidence in `5_log.md` §7.

**What it changes here:** §9 step 6 (the first real look-back) is now the test that decides C-09, and the interview screen should favour shippers above about $1.5M of truckload and LTL spend with a truckload share (§5.3, §7.3). The price test adds a 45% share and a flat or per-invoice price beside the 25% contingency, and the guide asks whether offshore handling of invoices is acceptable. The kit is not yet changed (point 5 above).

## 5. Who to interview: C-09's customers and the segments to sample

### 5.1 The two sides

| Side | Who | Screen (kit §5.1-5.2) | Target | Why they matter |
|---|---|---|---|---|
| **Shippers (paying side)** | Controller, AP manager or logistics manager at a US manufacturer or distributor | About 100-499 staff; pays truckload or LTL bills itself (not through an FAP provider); the interviewee approves or processes those bills | 5 interviews, 3 costed incidents, 2 commitments, 1 data share, 1 assessment | They carry the overcharge, hold the data and pay the fee |
| **Carriers (second side)** | Billing lead or owner | US truckload or LTL carrier with 5-250 trucks; handles invoicing or collections | 5 interviews | For an audit-only product they are the party that must accept short-pays and credit claims (H09-C1, C4). For the paying half they could buy faster payment (H09-C2) |

**A mismatch to note [our call]:** the buyer count (95,579) covers firms with **20-499** staff, but the kit's screen starts at **100**. Sampling a couple of 20-99-staff firms would show whether the small end has the problem and the freight spend (§4.2) to be worth serving. That is an input to Q6's size floor (F-6), not a decision on it.

### 5.2 Candidate segments to sample (Q6 chooses; S5 only spreads the interviews)

| Split | Values | Why it matters for C-09 | Desk evidence |
|---|---|---|---|
| **Industry group** | Defensive (passes the strict durability test): food and beverage and other branded nondurables, containers and packaging, agribusiness, forest and paper, consumer durables, capital goods, building materials · Cyclical (fails): auto, downstream metals, homebuilding | If C-09 is chosen, the segment must come from the passing groups (`4_scorecard.md` §9.3). H09-11 tests whether the problem is as common there | `4_scorecard.md` §6.5 |
| **Manufacturer or distributor** | 57,309 manufacturers · 38,270 wholesalers (20-499 staff) | Distributors ship many small outbound orders (LTL-heavy); manufacturers ship inbound materials plus outbound truckloads | N-E17 |
| **Staff band** | 20-99 · 100-499 | Freight spend, and so the fee per customer (§4.2) | — |
| **Mode mix** | LTL-heavy · truckload-heavy · mixed with parcel | LTL bills carry the reweigh and reclass corrections that the NMFC dockets changed (H09-04), and they connect to C-11 | check T |
| **How bills are checked today** | Nothing · AP clerk match · TMS · a 3PL books and bills · yearly contingency audit | The incumbent to displace and the show-stopper test (H09-01, H09-08) | `3_factsheets.md` item 9 |
| **ERP** | NetSuite, SAP Business One, Epicor, Acumatica, Dynamics 365 Business Central, Sage, Infor, others | Data export and a possible channel (ERP app marketplaces list freight audit apps, N-R21) | check R |
| **Who pays the freight** | Outbound prepaid · inbound collect · both | Who receives the bill, and so who holds the data | — |
| **Sells to big-box retailers** | Yes / no | Lets the same interview cover C-19 under P-23 | kit §7.1 |

**A sampling grid for the 5-10 shipper interviews [our call]:**
- at least 3 from defensive groups and at least 1 from a cyclical group;
- at least 2 distributors and 2 manufacturers;
- at least 2 LTL-heavy;
- at least 1 firm with 20-99 staff;
- at least 1 firm that already uses a contingency auditor.

One interview can fill several cells.

### 5.3 What check Y found (`research/s5_check_Y_c09_reach.md`, 2026-09-17)

**Re-checked at the source here:** the providers' stated client sizes (*Inbound Logistics*, September 2017) and the Indiana Chamber CFO Roundtable dates. Both match.

**1. The person who checks freight bills usually works in logistics, not AP.**

| Who does the freight-bill work, in 47 public job postings at US manufacturers and distributors (LinkedIn Jobs, SimplyHired) | Postings |
|---|---|
| Logistics, transportation or shipping coordinator, analyst, specialist or manager | **22** |
| A role just for freight bills (freight bill coordinator, freight audit specialist, freight billing clerk) | **11** |
| AP clerk or specialist | 6 |
| Accountant or controller (mostly as the manager the role reports to) | 5 |
| Other | 3 |

- **Labels:** postings *verified*; tally **[our calc]**. The sample is biased toward firms big enough to post a role.
- **Who approves**, where postings say: logistics 4, accounting 1.
- **Who buys:** audit firms' case studies quote the **CFO** at small firms and **logistics, purchasing or supply-chain directors** at larger ones, but never a controller or AP manager (*assumed*, vendor).
- **Check Z's finding agrees:** the people reviewing audit features are mostly logistics roles (§7.5).
- **Reading [our call]:**
  - The fact sheet's "finance and AP (the controller), with logistics co-deciding" may put too much weight on finance.
  - Interview **the person who checks the bills** (often logistics), with the **controller or CFO as the budget voice**, and screen on the duty ("approves, checks or codes carrier invoices"), not the title.
  - This bears on H09-05 and H09-10.

**2. The real size cut is freight spend, and it is lower than any FAP provider's floor.**

| Provider | Stated client size | Label |
|---|---|---|
| Cass | "Annual freight volume per organization ranges from $40 million to over $2 billion" | current page, *verified* as its statement |
| CTSI-Global · Fortigo · A3 | "$10 million and $1 billion" · "at least $10 million" · "at least $20 million to $30 million" | 2017, *verified* here |
| Technical Traffic Consultants | "between about $5 million and $100 million" | 2017, *verified* here |
| Intelligent Audit · RateLinx | "at least $500,000" · "from those with about $500,000" | 2017, *verified* here |
| Contingency firms (Lojistic, ICC Logistics) | No minimum stated; paid only from recoveries | *verified* |

- **Nobody screens out on "uses an FAP provider".** No firm in the 20-499-staff bands averages anywhere near FAP floors ($10M+), so that exclusion rarely applies.
- **TMS use is rare below $25M of spend:** about 10-15% (Gartner, quoted 2015, dated).
- **The practical floor sits around $0.5-1M of freight spend,** where contingency and mid-market software say the numbers work. This is consistent with check X's central break-even of $0.68M.
- **Check Y's spend by band** [our calc, 1.6-3.2% of receipts]:
  - manufacturers with 20-99 staff: $0.19-0.39M;
  - manufacturers with 100-499 staff: $1.1-2.3M;
  - wholesalers with 20-99 staff: $0.68-1.4M;
  - wholesalers with 100-499 staff: $3.1-6.2M.
- **These agree with check X's central bands** ($0.27M / $1.59M / $0.63M / $2.90M).
- **Wholesale receipts include the resale value of goods,** so wholesalers' figures probably run high.

**3. Six candidate segments, all from groups that pass the strict durability test.** Mode mix is our tabulation of the 2022 CFS microdata (*verified* data, **[our calc]**; the weight cut-offs are proxies).

| # | Candidate segment | Firms, 20-99 / 100-499 staff | Durability | Mode mix | Evidence the job exists here | Lists and gatherings |
|---|---|---|---|---|---|---|
| **SG1** | LTL-heavy distributors: HVAC, plumbing, electrical, industrial MRO, fasteners | 3,124 / 954 | **Not tested:** no distributor group is on file in `4_scorecard.md` §9.3 | LTL and parcel; small local deliveries outbound | Freight billing clerk postings ("validate rates against approved contracts"); vendor cases at industrial and fastener distributors | NFDA 95 members, STAFDA 191, PTDA 131; NAED, ISA, PTDA, ASA, STAFDA, HARDI, AHR Expo (Oct-Feb) |
| **SG2** | Capital goods and consumer durables makers: machinery, electrical equipment, HVAC equipment, furniture, cabinets | 7,573 / 2,270 | Pass (-7.7%, -7.4%) | **LTL and parcel, almost no full loads** (1-3% of truck shipments at 20,000 lb or more) | Postings: "Match freight bills against carrier agreements"; vendor case: "$96K recovered from duplicate billing in the first audit cycle" (*assumed*) | Kentucky and South Carolina state databases (**the only free lists that show staff size**); FABTECH; ECI Connect; AHR Expo (1,744 exhibitors); KBIS |
| **SG3** | Food, beverage and household nondurables makers (grocery wholesalers as a variant) | 6,477 / 1,659 (+3,438 / 863) | Pass (-1.1%) | Mixed | Postings: "audit all invoices related to domestic freight shipments to verify rate accuracy"; vendor case: a food distributor, "$78K recovered through a post-payment LTL audit" (*assumed*) | Winter FancyFaire (public list), NGA Show, PLMA, ISSA, SupplySide Global, Dairy Forum |
| **SG4** | Containers, packaging and paper | 1,773 / 700 | Pass (-3.5%, -5.6%) | Truckload-heavier for paper; mixed for converted packaging | Postings: "Audit freight bills and work with carriers and distributors to correct improperly billed invoices" | Paperboard Packaging Council directory (126, with addresses); PACK EXPO (2,711 entries, Oct 18-21) |
| **SG5** | Building materials and forest products | 5,988 / 1,574 | Pass (-8.0%, at the line) | **Truckload-heavy** | Postings: "freight invoice reconciliation" (a concrete maker with 60+ staff at one plant) | World of Concrete (1,124), IBS, Roofing Expo; NAFCD + NBMDA (Nov 3-5) |
| **SG6** | Agribusiness: animal feed, grain milling, fertilizer, farm supplies | 1,681 / 614 | Pass (-3.7%) | **The most truckload-heavy** (feed 62% of truck shipments at 20,000 lb or more) | Thin (freight accruals; a CFO quoted in a vendor case) | IPPE (1,295, with an industry field); World Ag Expo; farm shows (Feb) |

- **Reading [our call]:**
  - The mode mix lines up with the durability groups: SG1 and SG2 are LTL-heavy, SG4 to SG6 truckload-heavy, SG3 mixed.
  - A sample from one side only would test only one family of billing errors.
- **Three screener variables that are not segments:**
  - **Prepay-and-add freight:** the supplier adds freight to its own invoice, so there is **no carrier bill to check**. Screen out firms that receive mostly this.
  - **Routing most LTL through a 3PL:** the 3PL handles disputes, which is C-11's picture. At most 2 of 10.
  - **ERP:** it decides how bills are pulled, not what the problem is. At most 2 per ERP. NetSuite appears most often among the smaller posting firms.

**4. The sampling grid [our call], which refines §5.2's grid.**
- **Rules:**
  - every slot in a passing group;
  - at most 2 per ERP;
  - at least 3 firms with no outside audit and at least 1 using a contingency firm;
  - at least 2 firms with 20-99 staff;
  - at most 2 routing most freight through a 3PL;
  - log the slot ID with each interview.

| Slot | Segment | Maker (M) or distributor (D) | Mode | Staff | Audit today | Priority |
|---|---|---|---|---|---|---|
| 1 | SG1 HVAC, plumbing or electrical distributor | D | LTL | 20-99 | none or in-house | **Core** |
| 2 | SG2 machinery or electrical-equipment maker | M | LTL | 100-499 | none or in-house | **Core** |
| 3 | SG3 food, beverage or household-products maker | M | mixed | 100-499 | any | **Core** |
| 4 | SG4 packaging converter or paper-products firm | M or D | TL-leaning | 100-499 | any | **Core** |
| 5 | SG5 building-materials or wood-products maker | M | TL | 20-99 or 100-499 | none or in-house | **Core** |
| 6 | SG1 industrial MRO, fastener or power-transmission distributor | D | LTL | 100-499 | **contingency firm** | Extended |
| 7 | SG6 feed, fertilizer or farm-supply firm | M or D | TL | any | any | Extended |
| 8 | SG2 furniture, cabinet or appliance maker | M | LTL + parcel | 20-99 | any | Extended |
| 9 | SG3 variant: grocery or foodservice distributor | D | mixed | 100-499 | any | Extended |
| 10 | Wild card: a firm on an FAP provider or TMS | any | any | 100-499 | FAP or TMS | Extended (the satisfaction contrast) |

**What the comparisons would show at Q6:**
- slots 1, 2 and 6 against 4, 5 and 7: LTL errors against truckload errors;
- slots 1, 6 and 9 against 2, 3 and 5: distributors against manufacturers;
- slots 1 and 8 against the rest: whether small firms have enough spend and pain;
- slots 6 and 10: satisfaction with today's providers.

**Size, with check X in mind [our call]:** on check X's illustrative inputs the 20-99-staff manufacturer would not cover its cost (§4.3; the cost inputs are unsourced), so the grid's two small-firm slots are there to test whether their real overcharge rate is high enough. They are not a bet that small firms are the segment.

**5. Suggested edits to the kit (not applied; the founders confirm, §1.4 point 5):**

| Where | Now | Suggested | Why |
|---|---|---|---|
| Kit §5.1 screen | "about 100-499 staff" | **20-499 staff and freight spend of $250k or more** (check Y screener Q2-Q3) | Spend is the real cut; 20-99-staff wholesalers reach it |
| Kit §5.1 interviewee | "controller, AP manager, logistics manager" | **Primary: whoever checks the bills (logistics coordinator, analyst or manager; freight-bill clerk). Budget voice: controller or CFO**; where a controller agrees, ask for 10 minutes with the logistics coordinator too | The 47 postings; check Z's reviewer roles |
| Kit §3.1 job table, C-09 row | "controllers / AP managers" | Add "logistics managers and coordinators" | Same |
| Kit §5.1 notes | defensive or cyclical recorded | Also record the slot ID and the mode label | The grid above |
| `5_log.md` §1 | channel rows | One row per channel in §6.2, with its segment | W1 evidence |

---

## 6. How to reach them and schedule the interviews

### 6.1 What check V already mapped (`research/s5_check_V_recruiting_channels.md` §1-§3, §8-§9)

| Side | Channel | Cost | First action | Label |
|---|---|---|---|---|
| **Shippers** | 1. **B2B research panel with a screener** ("approves or codes freight invoices"): Respondent $80 a B2B session, User Interviews $98, plus the incentive | ≈ $200-300 per held interview | Write a 5-question screener; price a 5-person study | prices *verified* (N-V17, N-V18) |
| Shippers | 2. **LinkedIn Sales Navigator** search for controllers and AP managers at firms named in exhibitor lists (STAFDA 191 exhibitors; PACK EXPO; HARDI) and state manufacturers' associations (50 of them, 59,000+ companies) | $119.99 a month | Pull 100 named firms | *verified* (N-V52, N-V56, N-V74) |
| Shippers | 3. **Events, as a second wave:** CSCMP roundtables (about 20 dated events 17 Sep-30 Oct), IOFM Fall (2-4 Nov, AP staff), AFP (8-11 Nov) | Event fees | Pick 2 roundtables inside the window | *verified* (N-V59, N-V38, N-V39) |
| **Carriers** | 1. **FMCSA census file:** 33,424 active interstate general-freight carriers with 10-199 trucks, 33,001 with an email | Free | Download a filtered extract (1-2 states); send 150 short research asks | *verified* (N-V32) |
| Carriers | 2. Phone the office and ask for billing or AR | Staff time | — | **[our call]** |
| Carriers | 3. Events: ATA MCE (17-20 Oct), F3 (27-28 Oct), SMC3 Jump Start (25-27 Jan 2027), Truckload 2027 (28 Feb-3 Mar) | Event fees | — | *verified* |

**Norms (check V §9):**
- **Incentives:** $75-100 for AP, billing or logistics staff; $150-200 for controllers and owners; or a charity donation.
- **Cold email:** replies run at 0.45-3.43% (*assumed*, vendor benchmarks), so five meetings can take hundreds of emails. Pair every list with a warmer route.
- **CAN-SPAM rules:** an accurate sender, a postal address, and a one-line opt-out.
- **A paid interview is weak evidence of reachability** (W1), so log paid and unpaid separately (`5_log.md` §1).

### 6.2 What check Y found: routes, dates, screener and messages

**Shipper routes, ranked [our call]** (check Y §10):

| Rank | Route | Why | Cost | Lead time | First action |
|---|---|---|---|---|---|
| 1 | **B2B panel with check Y's 8-question screener:** Respondent, User Interviews, or Great Question (which recruits from both) | All three filter by job title, industry and company size (*verified* pages). It's the only route likely to deliver 5 held shipper calls by early October. Log it as paid (weak W1 evidence) | $45-98 fee plus a $100-200 incentive = **$145-298 per held call, $725-1,490 for 5** [our calc] | Days | Run User Interviews' free audience estimator with the screener; launch slots 1-3 |
| 2 | **Named-firm lists by segment → Sales Navigator title search → short research email** | Free, segment by segment, so the log shows which segment answers. Ask for the logistics coordinator or manager as well as the controller | Free lists; Sales Navigator $119.99 a month | 1-3 weeks | Build 40 names for slots 1-2 from the NFDA list and the South Carolina directory (size filter) |
| 3 | **Warm introductions** through ERP resellers ("Acumatica has no direct sales team"; its partners earn referral fees), CPA firms with manufacturing and distribution practices (some are also NetSuite partners), and **MEP centres** (publicly funded advisers to small manufacturers) | They sit with controllers and owners, and a forwarded note gets opened. Response unknown | Free; the summary as thanks | 2-4 weeks | Send check Y's forwardable note (§13.5) to 2 resellers and 1 MEP centre in the same state as the rank-2 list |
| 4 | **Finance roundtables and ERP user meetings:** Indiana Chamber CFO Roundtable (Fort Wayne, **24 Sep**, free, no membership rule stated, *verified* here), Epicor regional user group (Fort Worth, 8 Oct), Community Summit NA for Dynamics users (11-15 Oct), SuiteWorld for NetSuite (25-28 Oct), ECI Connect (16-18 Nov), Acumatica Summit (24-27 Jan) | Face to face with the right roles. **Whether a non-customer may attend is unconfirmed**, except Indiana's page, which states no restriction | Free to about $2,195 plus travel | By date | Email the Fort Worth Epicor group and Community Summit organisers to ask about guest attendance |
| 5 | **Online communities:** listening only | Every rules page read bans surveys or promotion (Acumatica, Dynamics Communities, Sage, EpiUsers, SAP, CFO Leadership Council); Reddit's rules couldn't be read | Free | — | Read freight-invoice threads for wording; don't post |

**Carrier routes** (check Y §8, §10.8). **No billing or AR gathering for carriers exists;** go through the owner or office manager.

| Rank | Route | Dates | Label |
|---|---|---|---|
| 1 | **FMCSA census file** → email, then phone the office: ask for "whoever handles invoicing and collections" (check Y §13.7 has the email and a 20-second phone script) | — | *verified* (check V) |
| 2 | Local state trucking association meetings | Texas chapters 1-27 Oct; Pennsylvania 15 and 22 Oct; Texas Fall Meetings 10-12 Nov; Georgia 19-20 Nov | *verified* |
| 3 | Small-fleet shows | California Trucking Show 3-4 Oct (free); Broker Carrier Summit 27-28 Oct; Mid-West Truck & Trailer Show 5-6 Feb | *verified* |
| 4 | Back-office events | Trimble Insight 27-29 Sep (larger carriers' back offices; likely too soon); TCA webinar "The Streamlined Back Office" 8 Oct | *verified* |

**Dates in the first four weeks** (full calendar to 28 Feb in check Y §11):

| Dates | Event | Side | Note |
|---|---|---|---|
| 17 Sep-30 Oct | About 20 CSCMP roundtable events (check V) | Shippers | Small fees |
| 24 Sep | **Indiana Chamber CFO Roundtable**, Fort Wayne | Shippers (finance) | Free |
| 24-25 Sep | acuCONNECT (Acumatica, virtual) | Shippers (SG1, SG3) | — |
| 27-29 Sep | Trimble Insight, San Diego | Carriers | Larger fleets |
| 1 Oct | Made in Connecticut Manufacturing Summit, Hartford | Shippers (SG2, SG5) | $180-270 |
| 1-27 Oct | Texas Trucking Association chapter meetings | Carriers | — |
| 3-4 Oct | California Trucking Show, Ontario CA | Carriers | Free |
| 8 Oct | Texas Epicor user group, Fort Worth · TCA back-office webinar | Shippers (SG1, SG2) · carriers | Guest rules unconfirmed |
| 11-15 Oct | Community Summit NA (Dynamics), Nashville | Shippers | — |
| 15 Oct | Florida Epicor user group · Pennsylvania trucking chapter dinner | Shippers · carriers | — |
| 18-21 Oct | PACK EXPO, Chicago | Shippers (SG4) | Exhibitor list 2,711 |

**Later:**
- SuiteWorld, 25-28 Oct;
- Broker Carrier Summit and F3, 27-28 Oct;
- IOFM, 2-4 Nov;
- NAFCD + NBMDA, 3-5 Nov;
- AFP, 8-11 Nov;
- ECI Connect, 16-18 Nov;
- Indiana CFO Roundtable, 17 Nov;
- NITL Engage, 30 Nov-2 Dec;
- HARDI, 7-10 Dec;
- Acumatica Summit, 24-27 Jan;
- AHR Expo and SMC3 Jump Start, 25-27 Jan;
- IPPE, 26-28 Jan;
- Mid-West Truck & Trailer Show, 5-6 Feb.

**Ready to use in check Y:**
- **§12, the screener.** It has 8 questions:
  - industry and products;
  - staff;
  - freight spend;
  - the truckload / LTL / parcel split;
  - the person's part in freight bills;
  - the AP system;
  - who checks bills today;
  - who sends the bills.

  It includes qualifying rules and assigns a grid slot.
- **§13, the outreach messages.** There are seven variants: an LTL-heavy distributor, a manufacturer's controller, a short LinkedIn note for a logistics coordinator, a truckload-heavy logistics manager, a forwardable note for an introducer, a follow-up after an event, and a carrier email with a phone script. All follow the kit's rules: research framing, no product, 20-30 minutes, CAN-SPAM basics.
- **Neither is copied into the kit until the founders confirm** (§1.4 point 5).

### 6.3 Schedule **[our call]**, adapting `5_validation.md` §5.2 with C-09 first

| Week | Dates | C-09 work |
|---|---|---|
| 0 | 17-18 Sep | Settle §1.4 and D-14 to D-20 (P-25 before any call). Run User Interviews' audience estimator with check Y's screener; price 5 panel sessions. Build 40 names for slots 1-2 (NFDA list, South Carolina directory). Send the forwardable note to 2 ERP resellers and 1 MEP centre. Ask the Fort Worth Epicor group and Community Summit about guest attendance; register for the Indiana CFO Roundtable (24 Sep) if a founder can be in Fort Wayne. Pull the carrier extract (1-2 states, 10-199 trucks) |
| 1 | 21-25 Sep | Outreach wave 1: panel slots 1-3 live; research emails to the slot 1-2 list; carriers 100 emails plus office calls. Log every contact in `5_log.md` §1 with channel and segment |
| 2 | 28 Sep-2 Oct | Shipper interviews. **Ask the first willing shipper for 1-3 months of paid invoices** under a mutual NDA (D-18). Carrier interviews start |
| 3 | 5-9 Oct | Remaining interviews. **Run the look-back audit by hand** (kit §6.1) and record the hours. Price test. Early-stop rule if P-24 is adopted |
| 4 | 12-16 Oct | Close the log, re-score on 1-10 (§7 of `5_validation.md`), check the gate, and go to S6 confirmation (§9) |
| Extension (D-19) | to 11 Nov | If the shipper finance side is short: IOFM (2-4 Nov) and AFP (8-11 Nov) |

---

## 7. What the interviews must find out

### 7.1 The two questions that decide C-09 (`4_scorecard.md` §7.1)
1. **Does a look-back audit on one mid-sized shipper's real invoices find 1-3% overpaid?**
2. **Will a controller pay a contingency to a startup?** *D-23 (2026-10-08):* now, will a controller pay a software company (a share of recoveries or a subscription, both open until Q6; *2026-10-08: the founders chose a subscription*), **and will their own staff work the flags the software raises?** The second half is new: the two interview questions in `handoff_c09_software_rerun.md` §7 start on it.

### 7.2 What to learn, by theme

Hypotheses are from `5_validation.md` §3.1. "Counts against" is the line that would weaken the card.

| Theme | What we need to learn | H-IDs | Where in the interview | Counts against |
|---|---|---|---|---|
| **Is the problem real?** | How bills are checked today; a specific wrong bill in the last 12 months, with an amount, who caught it, and whether the money came back; whether LTL bills changed after the 2025 and 2026 class changes (unprompted) | H09-01, H09-03, H09-04 | Blocks B, C; card probe | 3 of 5 already use an FAP provider or a systematic pre-payment audit; fewer than 3 costed incidents; no change reported |
| **How much money per customer?** | Freight spend and invoice volume; the overcharge rate on real invoices; which types (duplicates, rate ≠ agreement, fuel, accessorials, reweigh or reclass); how much is still inside the windows; how much they think they miss today | H09-02 | Block A (spend, proposed), block D, **the savings assessment** | Measured rate under 0.5% |
| **Will they pay us, and how?** | Who signs off on recovering overcharges; whether a contingency needs a budget; the answer to 25% of credits, $500 flat, or free | H09-05, H09-06 | Card probe; **price test** at block G | Procurement or IT approval needed, or logistics owns it; every share refused |
| **Can we get the data?** | Invoice format (EDI 210 or PDF); where rate agreements and PODs live; how long a pull takes; willingness to share under NDA | H09-07 | Block E; block G | Rates live only in emails; PODs held only by carriers |
| **Who else is there?** | Whether an auditor or FAP provider is used, what it charges, what it misses, and how satisfied they are (the show-stopper test) | H09-08 | Block D | Satisfied users of one provider |
| **How hard is the paying half?** | What moving carrier payments to a third party would take (ERP, bank, approvals) | H09-09 | Card probe | Already on AP-automation rails where a switch is quick (this would *raise* W3) |
| **How do we reach them?** | Which channel produced the meeting, how fast, paid or not | H09-10 | `5_log.md` §1 funnel | Finance channels yield no meetings |
| **Which segment has it?** | Industry group, staff band, mode mix (for Q6) | H09-11 | Screen plus block C | Problem found only in auto, metals or homebuilding |
| **Carriers: will they cooperate?** | Short-pays and disputes (amount, reason, cost to chase); POD turnaround; factoring and quick-pay fees; experience with shippers' audit firms and payment providers | H09-C1 to C4 | Carrier guide §5.2 | Rare or cheap disputes; refusal of third-party payment; pushback on third-party audits |

### 7.3 Numbers to capture in every shipper interview (for §4)

Proposed additions to the C-09 guide are marked **new**. They are **not applied to `5_interview_kit.md`** until the founders confirm.

| Number | Why | Where |
|---|---|---|
| **new:** yearly freight spend, and the split across truckload, LTL and parcel (a band is fine: under $250k / $250k-1M / $1-3M / over $3M) | The first link in §4's chain, and the size question for Q6 | Block A |
| Freight invoices a month, and number of carriers used | Cost to serve; how many carriers accept disputes. *D-23:* our reading cost, and the customer's review workload | Block A |
| **new:** share of carrier invoices arriving as EDI against PDF or email | Data work per customer | Block E |
| The last wrong bill: amount, type, how caught, whether credited, days to credit | Costed incident; share credited | Block C |
| **new:** "Of the overcharges you disputed in the last year, roughly how many came back?" (a past event, not an opinion) | The share carriers actually credit | Block C |
| Hours a week spent checking and disputing freight bills | The saving in time, and today's cost | Block D |
| Today's audit spend: a contingency share or per-invoice fee, and the look-back period | Proven spend (W4); the price reference | Block D |
| The price-test answer: yes / yes at another price / no, and why | Fee share accepted | Block G |
| Days to pay carriers, and how (check, ACH, card) | The payment half (H09-09) | Card probe |
| **new (check X):** the claim clause in their truckload contracts or broker rate confirmations (for example "claims within 90 days"), read from the document in the assessment | A 14101(b) contract can replace the 180-day rule, which sets how deep a look-back can go | Assessment |
| **new (check X):** the oldest paid invoices, rate agreements and PODs they can actually pull | Look-back depth, and so the one-off backlog | Block E |
| **new (check X):** "Have you ever had freight bills audited before? What did it find, what did it cost, and what happened to errors afterwards?" | Recurrence after a first audit, and the prices shippers have really paid | Block D |
| **new (check X):** how soon after payment a wrong bill is usually noticed and disputed | Collection falls as claims age (GSA) | Block C |

**A ready-made request list.** Check AC §9 turns the documents an audit needs into asks the founders can use directly: three months of invoices with all pages, an AP payment export with bank details stripped, every version of each rate agreement with its effective dates, truckload rate confirmations, bills of lading, written authority to pull proofs of delivery and weight-and-inspection certificates from carrier portals, and dock or gate time logs.

**From the look-back audit (kit §6.1):**
- flagged $ by type;
- the recoverable share, still inside the windows;
- the measured overpayment rate;
- ~~**hours spent**, which is the first real cost-to-serve number.~~ *Superseded by D-23 (2026-10-08):* **the customer's reviewer's minutes per flag, timed**, and the share of flags they accept as real. Under D-23 these are the customer's workload, not our cost to serve. The method waits for the founders to adopt the re-run's look-back design (`handoff_c09_software_rerun.md` §5).

### 7.4 C-09's gate items (`5_validation.md` §8)

| Gate item | C-09 now |
|---|---|
| Shipper side: at least 5 interviews | 0 / 5 |
| Carrier side: 5 interviews | 0 / 5 |
| At least 3 costed incidents (shippers) | 0 / 3 |
| At least 2 commitments (shippers) | 0 / 2 |
| A named data source, plus 1 interviewee willing to share | named: invoices, rate agreements, PODs · willing 0 |
| A savings assessment on real data | not started |

### 7.5 What the web already answers (checks Z and X, 2026-09-17)

**The short answer to "can the web answer our questions instead of people?":** **for documents and prices, partly; for behaviour inside the segment, no.**
- First-hand buyer voice is nearly absent online.
- Reddit, G2, Gartner Peer Insights, TrustRadius and Glassdoor blocked access, and most search results are vendor content.
- On Reddit, 9 of the 15 relevant posts came from **people building or selling to these buyers**, and only 4 from buyers (check Z §1, §11.1).

**Re-checked at the source here:**
- Freightview's Capterra page: 4.7 from 743 reviews, with the three audit quotes below.
- U.S. Bank's carrier agreement (revision R 9.2020): the account-debit clause and the 1% base discount fee.

**Web findings do not count toward the S5 gate** (kit §1.4).

| H-ID | Can the web answer it? | What the web shows | Label |
|---|---|---|---|
| H09-01 How bills are checked | **Partly; leans supports** | ERP documentation (NetSuite, Business Central, Acumatica) assumes freight bills are keyed and matched by hand. Users build their own duplicate checks (Epicor) and adjust accruals to the billed cost. **A route H09-01 doesn't name:** the invoice-audit screen inside cheap LTL booking tools (Freightview: "Our A/P department uses the audit feature", building materials) | docs *verified* (check Z); reviews *assumed* |
| H09-02 Overpay 1-3% | **No**; neutral figures lean below | See §4.3 (check X). Two vendor cases fall at about 1.0-1.4% of spend | *assumed* |
| H09-03 Costed incidents | **No** | 21 public wrong-bill stories, 12 with amounts (e.g. "charged nearly $3,000 more"). **None confirmed inside the segment:** 19 of 21 are very small shippers billed later by **brokers** as "adjusted invoices" | *assumed* |
| H09-04 NMFC dockets | **Partly; mixed** | A 3PL desk's "single busiest week of 2025" was the week of 19 July, **with classes moving both up and down**; no first-hand report of more corrections on mid-sized shippers' bills | *assumed* |
| H09-05 Who decides | **No** | Nothing first-hand. The people reviewing audit features are mostly **logistics** roles (director of logistics, shipping manager), with some AP | *assumed* |
| H09-06 25% accepted | **Anchors yes, acceptance no** | Advertised contingency 20-35% and 30-50%; "first audit is free"; parcel firms with $50k-250k minimums. **New entrants market against contingency** ("a fee that shrinks if the error class is eliminated"; "client keeps 100%" at $2,500-4,000 a month) | vendor *assumed* |
| H09-07 Data within a week | **Partly; mixed** | Invoices arrive on paper, as PDF or image by email or portal, by EDI or as CSV. Users split multi-invoice PDFs by hand. Carrier bills often **arrive after the month closes**. Audit screens cover "only some" carriers. Nothing public says where rate agreements live | docs *verified*; rest *assumed* |
| **H09-08 Show-stopper** | **Partly; mixed** | **No provider is shown serving more than half the segment.** Enterprise FAP review bases are tiny: Trax 3.5 from 12, nVision 4.8 from 8, Cass and U.S. Bank 1 review each. **But H09-08 misses an incumbent:** LTL booking tools with an invoice-audit screen, marketed to "small to mid-sized manufacturers and distributors", with large satisfied bases: **Freightview 4.7 from 743 Capterra reviews, MyCarrier 4.7 from 108, FreightPOP 4.7 from 47.** Audit there is a secondary feature, criticised for coverage ("only shows some freight companies, not all the carriers we work with") and automation ("could be more intelligent and automated") | Freightview figures *verified* here; others *assumed* |
| H09-09 Payment switch | **No** | No shipper account of switch time. Payees resent pay-to-get-paid rails (AvidXchange on Trustpilot: 3.6 from 70, "They charge a fee to get paid") | *assumed* |
| H09-10 Reached via finance | **Partly; leans against** | Audit-feature reviewers and buyer posts sit mostly in logistics. The S5 funnel is the real test | *assumed* |
| H09-11 Defensive vs cyclical | **No** | 9 audit-feature reviews: building materials 3, construction 1, consumer goods 1, others; too thin | *assumed* |
| H09-C1 Short-pays | **Partly** | Short-pays found are by **brokers** ($300 held back on a $3,000 load); FAP carrier documents show reject queues ("Missing Documentation", "Out of Tolerance") | *assumed* / documents *verified* |
| H09-C2 Carriers pay for speed | **Fees yes; willingness no** | **U.S. Bank's carrier agreement (R 9.2020):** a "Discount Fee" with a **1% base rate** on each accelerated payment, rising with the prime rate and terms, plus a higher fee if the carrier exempts some shippers. "Carrier authorizes U.S. Bank to debit Carrier's account(s) in the event of an overpayment or error". Quick pay 1.5-5% and factoring 2-3.5% are typical (secondary) | agreement *verified* here; rest *assumed* |
| H09-C3 PODs fast | **Partly** | A POD texted within 15 minutes of delivery (the dispute was over receipt, not speed) | *assumed* |
| H09-C4 Resisting automated audit | **No** | Nothing found | — |

**What check Z changes [our call]:**
1. **The show-stopper test should also cover the audit screens in LTL booking tools** (Freightview, MyCarrier, FreightPOP), not only FAP providers and audit firms. That is a change to how H09-08 and kit block D are read; see the probes below.
2. **The broker may be the counterparty, not the carrier.** Where a shipper books LTL through a 3PL, corrections come from the broker as adjusted invoices. This is the same issue as C-11's H11-08.
3. **The buyer may sit in logistics as often as in finance** (H09-10). Log the role of every interviewee and who they say approves.
4. **Contingency is under attack in the category's marketing,** so the price test may be judged against "keep 100%" subscription offers.
5. **The field is crowded and consolidating.** Loop absorbed Data2Logistics in 2025, which makes check R's list of 16 out of date. Mid-market pitches come from Loop, Eller Audit (LTL contingency, first audit free), ValueXPA, Zero Down and US Tech Automations. Freehand ($75M) targets enterprises above $250M of freight spend. **Outreach will reach people who have been pitched before.**
6. **An adjacent controller pain surfaced:** freight bills arriving after month-end break landed cost and accruals. It is a finance job, separate from overcharges (a possible growth option, recorded only).

### 7.6 Sharper probes the online record suggests (proposed for the C-09 guide; not applied)

All ask about past events (the Mom Test), from check Z §13:

| # | Probe | H-ID |
|---|---|---|
| 1 | "The last carrier invoice you approved: what, if anything, was it compared with before it was paid, and where did that happen: the ERP, the booking tool, a spreadsheet?" | H09-01, H09-08 |
| 2 | (Only if they name a booking tool) "When did someone last open its invoice or audit screen? What did it flag, and which carriers weren't in it?" | H09-08, H09-07 |
| 3 | "Tell me about the last invoice that changed **after** delivery: how many days later, by how much, what reason was printed, and who noticed?" | H09-03 |
| 4 | "What has changed about your LTL invoices in the last 14 months, if anything? Any shipment billed at a different class than the BOL, higher **or lower**?" | H09-04 |
| 5 | "Which LTL shipments last year went through a broker or 3PL rather than direct? When one was corrected, who sent the new invoice, and what did you do?" | H09-03, H09-07 |
| 6 | "When a freight invoice last didn't match, who contacted the carrier, AP or shipping? How long did it take, and was the money credited or just expensed?" | H09-01, H09-10 |
| 7 | "Where is the rate agreement for your biggest carrier right now? When did you last need it, and how long did it take to find?" | H09-07 |
| 8 | "Has anyone offered to audit your freight bills for a share of what they recover? What happened next, and why did it go ahead or stop?" | H09-06, H09-05 |
| 9 | "The last time you sent an outside firm your invoices or contract rates, what did IT, legal or procurement ask for first, and how long did it take?" | H09-05 |
| 10 | "The last time you changed how you pay a group of vendors (ACH, card, an AP tool), how long from decision to first payment, and who signed?" | H09-09 |
| 11 | Carriers: "The last payment you got through a shipper's payment company or AP portal: what came off it, how many days did it take, and what did you have to sign up for?" | H09-C2, H09-C1 |
| 12 | Carriers: "The last time an outside auditor or payment company rejected or cut one of your invoices: what reason did they give, what did you send back, and how did it end?" | H09-C1, H09-C4 |

---

## 8. Backups, growth options, and what is parked

| Role | Card | Shares with C-09 | Status under option B |
|---|---|---|---|
| **Backup** | C-11 LTL class, reweigh and reclass disputes | Product core (proof and dispute), shipper data (LTL bills), much of the buyer | Still in S5 (point 1 in §1.4). Its NMFTA licence question (D-20) is still open |
| **Backup** | C-19 Retailer OTIF fines and deductions | Buyer (the controller at a manufacturer), recovery fee shape | Still in S5 (point 1 in §1.4) |
| **Other finalist** | C-20 Import entries | Nothing (the trade-paperwork family) | Still in S5 under B as written; paused under reading (b) or (c) |
| **Growth option** | C-10 Cargo claims (fact sheet, not shortlisted) | Same data and budget story; incumbents already bundle audit and claims | Not in S5 |
| **Growth option** | C-12 Parcel audit (reserve list) | The same job on parcel bills | Reserve; revived by S5-grade evidence lifting its pool over $25M (`3a_unknowns.md` §5.3) |
| **Growth option** | Paying carriers (C-09's own second half) | The payment flow (R41) | After an audit-first start (point 2 in §1.4) |
| **Growth option** | Payee checks before paying carriers (C-08's identity core) | The paying half; payment fraud hit 76% of US firms in 2025 | C-08 demoted under D-9; a growth idea only (`6_decision.md` §2) |
| **Parked** | The other 13 fact-sheet cards and the 14 reserve cards | — | S6 step 5 ("park everything else explicitly", with a revival trigger each) is done at S6 confirmation, not now |

---

## 9. Next steps

**From the founders' message, `6_decision.md` §4 and `5_validation.md` §5 and §10, in order.**

| # | Step | Who | By | Output |
|---|---|---|---|---|
| 1 | Settle §1.4 (S5 scope, wedge, D-14 to D-20, per-customer profit) | Founders, with Claude | 18 Sep | Decisions recorded here and in `5_validation.md` §10 |
| 2 | Confirm or reject the kit changes in §1.4 point 5: screen, interviewee, grid, numbers (§7.3), probes (§7.6), screener and messages (check Y §12-§13) | Founders | 18 Sep | `5_interview_kit.md` updated only after sign-off |
| 3 | Build the C-09 contact lists, following §6.2's ranked routes: panel, named-firm lists by segment, warm introducers, events; and carriers from the FMCSA extract. Keep names and contacts **outside** this folder (kit §1.3) | Founders | 18-21 Sep | Private lists; channel rows in `5_log.md` §1 |
| 4 | Outreach wave 1 to shippers and carriers | Founders | 21-25 Sep | Funnel counts in `5_log.md` §1 |
| 5 | Interviews, using the kit's rules and guides §5.1-5.2; note template within 24 hours | Founders | 28 Sep-9 Oct | `5_log.md` §2-§9 |
| **6a** | **Done 2026-09-17** (§4.4.5, `research/s5_practice_audit_public_invoices.md`): a practice look-back on the **public** court invoices (§4.4.3). The SEFL set is the only one with bills and the agreement together; the ABF set gives 101 bills for duplicate, fuel-base, minimum-charge and reweigh tests. It would time the work per invoice, test the method, and produce a worked example to show interviewees. **It cannot measure our segment's overcharge rate:** the shippers are not ours, and two of the three sets have no agreement to rate against | Claude, with the founders' go-ahead | before outreach | A method note and timings, to fold into kit §6.1 |
| 6 | Ask the first willing shipper for 1-3 months of paid invoices, rate agreements and PODs under a mutual NDA; run the look-back by hand; **record hours**. *D-23 (2026-10-08):* no look-back starts until the founders adopt the re-run's kill lines (`handoff_c09_software_rerun.md`). The suggested design has the shipper's own reviewer work the flags while timed; "record hours" means their minutes per flag | Founders (Claude can help build the spreadsheet method) | 5-9 Oct | Assessment result in `5_log.md` §7; §4's chain filled with real numbers |
| 7 | Price test at the close of each shipper interview (25% / $500 / free). *D-23:* the wording waits for the re-run, which models a share and a subscription side by side; no price is set before Q6. *2026-10-08: a subscription (C28); the kit's price test is rewritten (§6.1)* | Founders | 28 Sep-9 Oct | `5_log.md` §7 |
| 8 | Under option B: the other finalists' coverage per the answer to §1.4 point 1 | Founders | same window | `5_log.md` |
| 9 | Re-score on the 1-10 anchors and check the gate | Claude drafts, founders confirm | 12-16 Oct | `5_validation.md` §7.3 and §8 |
| 10 | **S6 confirmation:** keep or change the primary; backups and growth options; the wedge hypothesis (S6 step 3); where the hub is (step 4, with the entry side left to Q6); park the rest with triggers (step 5); sign-off with the deciding factors (step 6) | Founders, together with Claude | after step 9 | `6_decision.md` finalized; this file updated |
| 11 | **S7:** record the choice in CLAUDE.md "Answers / Decisions", with dated revisit triggers | Claude | after step 10 | CLAUDE.md |

---

## 10. Sources

- **Stage records:**
  - `0_criteria.md` §1-§6;
  - `1_candidates.md` C-09, M-2 and the C-09/C-12 split;
  - `2_knockouts.md` §2, §4.1, §4.3, §4.5;
  - `3a_unknowns.md` §2, §4.5, §5.3;
  - `3_factsheets.md` §2.2 (C-09, C-10);
  - `3_shortlist.md` §1-§6;
  - `4_scorecard.md` §1-§9;
  - `5_validation.md` §1-§10;
  - `5_interview_kit.md` §1-§8;
  - `5_log.md`;
  - `6_decision.md`.
- **Research files:**
  - `research/s0_check_A_ambition_economics.md` §A3, §3 (per-customer economics benchmarks);
  - `research/s3b_check_R_shipper_spend_jobs.md` §2.2;
  - `research/s5_check_T_ltl_carrier_position.md` §1 (dispute windows);
  - `research/s5_check_V_recruiting_channels.md` §1-§3, §8-§9;
  - new on 2026-09-17, first round: checks X, Y and Z (above);
  - new on 2026-09-17, second round: `research/s5_check_AA_c09_cost_to_serve.md` (cost to serve), `research/s5_check_AB_c09_private_recoveries.md` (what audits recover, and the 180-day limit), `research/s5_check_AC_c09_example_invoices.md` (real invoices, the field map and the document request list).
- **Process:** `submarket_selection.md` §4 S5-S7, §5.4, §7.
- **Method sources cited:** R15 (Aulet: inquiry mode), R16 (Aulet: pursue until disproven), R25 (CAMP; success rate sets margin), R28 (Bessemer: savings assessments), R35 (the Mom Test), R41 (Gurley: payment flow).
