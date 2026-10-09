# Run 01, S5: validation with primary evidence

> **Stage S5 of `submarket_selection.md` §4, "Validate with primary evidence". Opened 2026-09-16.**
> **Input:** the four unranked finalists sent by the founders at S4 (C-09, C-11, C-19, C-20; `4_scorecard.md` §9.1, D-11), S5's coverage rule C21 (D-12), the fact sheets (`3_factsheets.md`) and the frozen criteria (`0_criteria.md`).
> **Status: the desk half is done; the primary half has not started.**
> - **Done at the desk (2026-09-16):**
>   - the documented positions of the two counterparty-only sides, which C21 requires (checks T and U);
>   - C-19's buyer count and a current reading of its 2018 gap (check U);
>   - a recruiting map for every side (check V);
>   - the hypotheses, the interview kit, the evidence log, and the rules for the 1-10 re-score.
> - **Not done, and only the founders can do it:** recruiting, about 28-30 conversations, four savings assessments on real data, the price tests, and the re-score.
>
> **Files:** this file is the stage record. `5_interview_kit.md` holds the guides, messages, assessment protocols, prices and survey. `5_log.md` holds the evidence as it comes in.
> **Gate:** not met, since no primary evidence is held yet. See §8.
> **Nothing here is decided.** The decisions this file puts to the founders are in §10.

## How to read this

- **What S5 is for:** "confirm or kill the top candidates' problems, costs and payers with real people before committing" (`submarket_selection.md` §4 S5). Desk evidence narrowed the list; "talking to customers decides" (P7).
- **What the desk can and cannot add here.** The desk can lay out the counterparty sides' rules, count buyers, and find where people gather. It cannot say whether a controller will share invoices, whether a carrier credits a dispute we file, or what share of a cost is removable. `4_scorecard.md` §7 factor 9: "S5 step 3 — a savings assessment on one customer's real data — is the single measurement that would move more rows than any other."
- **Labels:**
  - *verified*: read at the source;
  - *assumed*: a vendor claim, an association figure, a snippet or a secondary summary;
  - **[our calc]**: arithmetic;
  - **[our call]**: judgement.
- **New research files** (sources N-T, N-U, N-V):
  - `research/s5_check_T_ltl_carrier_position.md` (C-11's counterparty);
  - `research/s5_check_U_retailer_position.md` (C-19's counterparty, buyer count, 2018 gap);
  - `research/s5_check_V_recruiting_channels.md` (every side).

---

## 1. At a glance

| Card | Paying side (5 interviews) | Second side and its type (C21) | The question S5 must answer first (`4_scorecard.md` §7.1) | Desk half |
|---|---|---|---|---|
| **C-09** Auditing and paying freight bills | Mid-sized manufacturers and distributors (controller, AP) | **Carriers: could buy from us** → 5 interviews | Does a look-back audit on one mid-sized shipper's real invoices find 1-3% overpaid? And will a controller pay a contingency to a startup? *D-23 (2026-10-08): C-09 is software, so add: will the shipper's own staff work the flags (H09-12)? The fee form, a share or a subscription, is modelled both ways* | Recruiting map (V) |
| **C-11** LTL class and reclass disputes | Small manufacturers and distributors that ship LTL (shipping lead) | **LTL carriers: counterparty-only** → documented position (T) + 1-2 worker interviews | Will an LTL carrier grant a credit on evidence we produce, when the carrier holds the measurement record? And what is the real correction rate? | Position (T), map (V) |
| **C-19** Retailer OTIF fines and deductions | Small and mid-sized suppliers to big-box retailers (CFO, controller, credit) | **Big-box retailers: counterparty-only** → documented position (U) + 1-2 worker interviews | Is the 2018 gap still open, or has SPS's SupplyPike closed it? And how many small and mid-sized suppliers are there? | Position, count and gap (U), map (V) |
| **C-20** Import entries | Small customs brokerages (owner, licensed broker) | **Importers: could buy from us** → 5 interviews | Would a small brokerage buy a co-pilot that does not file? And does the broker keep the labour saving? | Recruiting map (V) |

**Conversations:**
- 20 on the four paying sides (5 × 4);
- 10 on the two second sides that could buy from us (5 × 2);
- 2-4 with people who work against the two counterparties.

That is **32-34 at most, and about 28-30 if P-23 lets an interview count for two shipper cards** (§10). D-12 estimated "about 28-30".

---

## 2. Side types, card by card (C21: "Say on each card which of the two every side is, and why")

| Card | Side | Type | Why |
|---|---|---|---|
| C-09 | Mid-sized manufacturers and distributors | **Could buy from us: the paying side** | The shipper's cost falls and the shipper pays. A contingency audit needs no budget line (`3_factsheets.md` C-09 item 7). F5 = 1. *D-23 (2026-10-08): the shipper's own staff now review and file; a subscription, if chosen, would need a budget line* |
| C-09 | Truckload and LTL carriers | **Could buy from us** | The job includes *paying* carriers. A payment rail sits in the money flow (R41), and carriers already pay for faster payment through factoring and quick-pay fees. The carriers are also the party that must accept an audit's short-pays (§5 two-sided rule: "A candidate whose other side refuses to take part fails in practice") |
| C-11 | Small manufacturers and distributors shipping LTL | **Could buy from us: the paying side** | The shipper pays the correction and would pay us (item 7). F5 = 1 |
| C-11 | LTL carriers | **Counterparty-only** | They are the party being disputed. They hold the tariff and the reweigh and dimensioner record. The side is concentrated: top-50 share 82.9%, with 17.5% of receipts in firms under 500 staff (K10 rules it out). We would never sell dispute tools to them |
| C-19 | Small and mid-sized suppliers to big-box retailers | **Could buy from us: the paying side** | Recoveries return to the supplier's revenue, so the payer is the saver (item 7). F5 = 1 |
| C-19 | Big-box retailers | **Counterparty-only** | They set the rules and deduct first. The side is concentrated: warehouse clubs and supercenters top-4 95.6% (item 4). Five discovery calls with a top-4 retailer "sets a gate that cannot be met" (C21) |
| C-20 | Small customs brokerages | **Could buy from us: the paying side** | Only licensed brokers or self-filing importers may file. The brokerage owner already pays ABI software by use (item 7) |
| C-20 | Small importers | **Could buy from us** | They pay per entry today. They could self-file, or buy an adjacent recovery such as a refund look-back. Cohen's self-filing row (0.10) shows it is a weak buyer at present, which S5 tests rather than assumes (`4_scorecard.md` §4.2) |

**The carriers on C-19** also hold proof of delivery, but the S1 card names the retailer as the harder side and D-12 names the retailers as C-19's counterparty. The carriers enter S5 only as a source of evidence, asked about on the supplier side (H19-07) **[our call]**.

---

## 3. Hypotheses to test

Every hypothesis names:
- its desk basis;
- the scorecard rows it would move at the re-score (§7);
- how it is tested (a kit block, an assessment or a check file);
- what would count against it.

Outcomes are logged in `5_log.md` §3. Thresholds such as "3 of 5" follow the gate's own counts **[our call]**.

### 3.1 C-09 · Auditing and paying truckload and LTL bills

| ID | Hypothesis | Desk basis | Rows | Test | Against it |
|---|---|---|---|---|---|
| H09-01 | Mid-sized shippers pay truckload and LTL bills largely as billed. Checking is a manual AP match, a yearly contingency look-back, or nothing | Item 9: "pay as billed, a yearly contingency post-audit, or nothing" (*assumed*) | A2, W4 | Kit B, D | 3 of 5 already use an audit-and-pay provider or a systematic pre-payment audit |
| H09-02 | They overpay 1-3% of truckload plus LTL spend (vendors claim 2-8%) | Item 2, **[our call]** | A1, F4 | Assessment §6.1 | Measured rate under 0.5% |
| H09-03 | At least 3 of 5 describe a specific overcharge in the last 12 months, with an amount | — | A3, gate | Kit C | Fewer than 3 |
| H09-04 | The NMFC class dockets (2025-07-19; 2026-05-23) added LTL corrections to their bills | A3 = 1 rests on this (`4_scorecard.md` §2.3, §6.6) | A3 | Kit C probe (unprompted) | LTL shippers report no change |
| H09-05 | The controller decides, and a contingency arrangement needs no budget line | Item 7 (N-A26; **[our call]**) | K8, W5, F5 | Kit card probe | Procurement or IT approval needed; or logistics owns it. *D-23 (2026-10-08): a subscription is also modelled; it would need a budget line* |
| H09-06 | A 25% share of recoveries is accepted | Contingency firms take 25-50% (N-A25, N-A26, *assumed*) | F1, F2, fee share | Price test §6.1 | Every share refused. *D-23: the price test waits for the kill-test re-run (`handoff_c09_software_rerun.md`); under a share, we no longer see the credit memos the customer receives* |
| H09-07 | Invoices, rate agreements and PODs can be pulled within a week, in usable form | Item 5 plumbing | W3, F3 | Kit E | Rates live only in emails; PODs held only by carriers |
| H09-08 | No provider already serves them well. Where an auditor is used, it is a yearly look-back they are not fully satisfied with | Item 9: leaders about 4-5% each | W4, show-stopper | Kit D | Satisfied users of one provider |
| H09-09 | Moving carrier payment to a third party takes months (ERP, bank, approvals), while audit-first can start now | Item 7; W3 = 0.5 (D-10) | W3, W6, Cohen Liquid | Kit card probe | Already on AP-automation rails where a switch is quick → W3 up |
| H09-10 | They are reached through finance channels, not logistics ones | W1 = 0.5, "bought through finance" | W1 | Funnel (`5_log.md` §1) | Finance channels yield no meetings |
| H09-11 | Defensive shipper groups report the problem as often as cyclical ones | Strict durability test (`4_scorecard.md` §6.5, §9.3) | Q6 carry | Screen + Kit C | Problem found only in auto, metals or homebuilding |
| H09-C1 | Carriers lose time and cash to short-pays and disputes | — | A3 (carrier side), W5 | Kit C (§5.2) | Rare, or cheap to handle |
| H09-C2 | Carriers would be paid through a third-party rail, and already pay for faster payment | Factoring and quick-pay exist (item 9) | F5, A6 | Kit D (§5.2) | Refuse third-party payment |
| H09-C3 | Carriers produce PODs and invoices quickly when asked | — | W3 | Kit E (§5.2) | Days or weeks |
| H09-C4 | Carriers do not resist an automated audit more than a human one | §5 two-sided rule | W6, show-stopper | Kit probe (§5.2) | Carriers push back on third-party audits. *D-23: in version 1 the shipper's own staff file the claims, so carriers' third-party rules (TForce, FedEx Freight) matter less; the test becomes whether carriers accept the shipper's software-prepared disputes* |
| H09-12 | Mid-sized shippers' staff will work a flagged-bill queue: they clear most flags within the claim window (*added 2026-10-08, D-23*) | D-23 puts review and filing on the customer's staff; the job is "nobody has the time" today (`C09-business-proposal.md` §3.1) **[our call]** | Follow-through (A09-15), the customer's hours (A09-16); the kill test's Test 3 and middle band (proposed, re-run) | The two "who works the flags" questions (kit §5.1); the timed look-back; a pilot of at least one billing cycle | Nobody checks freight bills today and no one would own the queue; flags go unworked past the claim window |

### 3.2 C-11 · LTL class, reweigh and reclass disputes

| ID | Hypothesis | Desk basis | Rows | Test | Against it |
|---|---|---|---|---|---|
| H11-01 | Corrections hit a meaningful share (5% or more **[our call]**) of small shippers' LTL shipments | No neutral rate; K4 open (`3a_unknowns.md`) | K4, A1, F4 | Kit C count; assessment §6.2 | Measured under 2% |
| H11-02 | Avoidable corrections are 2-5% of LTL spend (vendors say 10-20%) | Item 2, **[our call]** | A1 | Assessment §6.2 | Under 1% |
| H11-03 | Most corrections are accepted, or handed to the 3PL rep | Item 9: "accept the correction, or ask the 3PL rep" | A2, W4 | Kit D | Shippers dispute routinely with a tool |
| H11-04 | Dockets 2025-1 and 2026-1 raised corrections or confusion | A3 = 1 (N-R02, N-R03) | A3 | Kit card probe (unprompted) | No change reported |
| H11-05 | Disputes backed by the shipper's origin documents (packing slip or invoice + pre-printed spec sheet) win credits in a meaningful share of cases. Record "wrong description" and "disputed measurement" separately | F2 = 1 on this basis; check T §9.1: these are the proof carriers name | F2, F3, A1 removable share | Dispute run §6.2; worker interviews | Under 20% of evidenced disputes won |
| H11-06 | Shippers (as bill-to party) can get the carrier's certificate and dimensioner record in time: within the 30-day Handbook 44 retention and the tariffs' shortest clocks | F3 = 0.5 ("the counterparty holds the evidence"); check T §1 rows 5-6 | F3, W3 | Check T §3-4; Kit E | Carriers do not share it, or only after the clocks run out |
| H11-07 | Shippers accept a contingency, and resist a subscription above about $150 a month | Saving $446-3,904 a year per shipper; tools from $149 a month (*assumed*) | Cohen Lucrative, W5 | Price test §6.2 | Nothing accepted |
| H11-08 | Shippers who book through a 3PL cannot dispute directly | Item 5: large 3PL networks | W1, W3, Q6 | Kit card probe | They can |
| H11-09 | Small shippers do not hold NMFTA's ClassIT+ licence, and its cost matters | C20 dependency | W3, W6 | Check T §7; Kit D | Licence is cheap and common |
| H11-10 | Machinery and furniture shippers report it as often as fabricated metals | Strict durability test fails fabricated metals | Q6 carry | Screen + Kit C | Only fabricated metals |
| H11-11 | Small shippers do not already list weight and dimensions for each pallet on the BOL, and have spec sheets for most products (so origin evidence exists but isn't used) | Check T §1 rows 2 and 4 (added at S5) | A1 removable share, W3, S6 wedge | Kit card probe (§5.3) | They already do both, or no spec sheets exist |
| H11-W1 | Carriers grant credits on evidence filed by a third party at a rate similar to disputes filed by the shipper or its 3PL | S4's question | F3, W6, show-stopper | Worker interview (§5.4) | Carriers ignore third-party disputes |
| H11-W2 | A correction rate can be stated from records, not feel | K4 open | K4, F4 | Worker interview | No one tracks it |
| H11-W3 | The evidence that wins, and the windows that bite, are known and match the tariffs | Check T | F3, W3 | Worker interview vs check T | Practice departs from the rules |

### 3.3 C-19 · Retailer OTIF fines and deductions

| ID | Hypothesis | Desk basis | Rows | Test | Against it |
|---|---|---|---|---|---|
| H19-01 | At least 3 of 5 describe a recent fine or non-trade deduction, with an amount | — | A3, gate | Kit C | Fewer than 3 |
| H19-02 | Non-trade deductions are ¼-½% of sales to the retailer, and 20-40% of them are removable | CRF median (*assumed*, association); share **[our call]** | A1, F4 | Assessment §6.3 | Under 0.1% of sales, or under 10% invalid |
| H19-03 | Small suppliers write off many deductions as not worth disputing | CRF 2018: 6% "just write off" (*assumed*) | A1, W4, Cohen Self-Aware | Kit C, D | They dispute nearly all |
| H19-04 | Most still use no third-party deduction tool or service, and users of SPS or SupplyPike are not all satisfied | CRF 2018: 70% used none; SPS bought SupplyPike (N-S10) | W4, show-stopper, W6 | Check U §5; Kit D | 3 of 5 use SPS or similar and are satisfied |
| H19-05 | The 2024 retailer rule changes raised fines or dispute work | A3 = 1 (N-S13, N-S12); A3 = 0.5 if easing counts (`4_scorecard.md` §6.6) | A3 | Check U §3; Kit probe | Fines fell, or nothing changed |
| H19-06 | The payer is the saver, and a 25-30% contingency is accepted | Recovery firms ~30% (N-S35, *assumed*) | F5, F1, F2, W5 | Price test §6.3 | Every share refused |
| H19-07 | PODs and carrier timestamps can be had inside the dispute window | Item 5 plumbing | F3, W3 | Kit E; check U §2 | Proof arrives after the window |
| H19-08 | Portal exports and 812/820 remittances can be shared | Item 5 | W3, F3 | Kit E | Refused, or not exportable |
| H19-09 | The buyer population is 10,000 firms or more | No count held (`4_scorecard.md` §4.2) | Cohen Plausible, W1 | Check U §4 | Under 10,000 |
| H19-10 | Suppliers are reached through supplier communities or credit networks | W1 = 0.5 | W1, W6 | Funnel | No channel yields meetings |
| H19-11 | Users of SupplyPike/SPS or Glimpse show discomfort with their tool: price rises, paying for denied disputes, retailers or deduction types not covered, missing evidence. *(Added 2026-09-22)* | SupplyPike's list roughly doubled to 2.5× from 2021 to 2023; Capterra complaints (denied disputes without escalation, gaps in coverage and backup documents), against a 4.9 rating (`4_5_profitability.md` §3.7) | W4, show-stopper, W6 | Kit §5.5 incumbent probes | 3 of 5 users satisfied, with no switching thought in the last year |
| H19-12 | At least 1 in 4 C-19 recruits reports non-trade deductions of 1% of sales or more (the screen yield). *(Added 2026-09-22, C26)* | CRF 2021: ~25% of suppliers at $500M or less above 1% (`4_5_profitability.md` §3.3) | Cohen Plausible, customer count, acquisition cost | Kit §5.5 screen | Under 1 in 10 |
| H19-W1 | Retailers reverse invalid deductions at a known rate when disputed with evidence | — | F2, F4 | Worker interview (§5.6) | Reversals rare whatever the evidence |
| H19-W2 | Written rules and actual practice differ in known, stable ways | Check U §2 | F3, W3 | Worker interview vs check U | Practice is unpredictable |
| H19-W3 | Retailers do not block third-party or bot access to supplier portals | C20 dependency (`4_scorecard.md` §7 factor 8) | W3, W6 | Worker interview; check U | Access is blocked or banned |

### 3.4 C-20 · Import entries

| ID | Hypothesis | Desk basis | Rows | Test | Against it |
|---|---|---|---|---|---|
| H20-01 | Classification and keying take 30-50% of entry-preparation time, and that share is removable. Preparation costs $40-100 an entry | Item 2 (World Bank $100; **[our call]**) | A1, A2, F4 | Time study §6.4 | Under 15% of the time |
| H20-02 | De minimis's end (29 Aug 2025) and the refund process (20 Apr 2026) raised workload, and brokers are short of capacity | A3 = 1 (N-S05, N-S06) | A3, W5 | Kit D | No change in work |
| H20-03 | Brokers keep a time saving (more clients or fewer hours) rather than cutting their price | F5 = 0.5 (`4_scorecard.md` §3.1) | F5 | Kit card probe | They expect to pass it into the entry price |
| H20-04 | Brokers would adopt a co-pilot that does not file | Wedge sensitivity: W 87.5 against 52.5 (`4_scorecard.md` §2.4) | W3, W6, Cohen Liquid and Eager-comparative | Kit card probe; price test | Only inside their filing software |
| H20-05 | Reasonable-care liability limits how far classification can be automated | W6 = 0.5 (licensing) | W3, W6 | Kit card probe | No concern |
| H20-06 | No ABI vendor's built-in AI already satisfies them | About 70 vendors; NetCHB about 30% of brokers **[our calc]** | W4, show-stopper, Cohen Eager-comparative | Kit D | Satisfied with a vendor feature |
| H20-07 | A per-entry price well below the labour saved is accepted | Brokers charge $100-250 an entry (*assumed*) | Cohen Lucrative, fee | Price test §6.4 | Refused |
| H20-08 | Brokerages are quick to reach | W1 = 1 (NCBFAA 1,500+ members) | W1 | Funnel | Slow, or few replies |
| H20-09 | Small brokerages' entry volume held through 2022-23, and tariff swings raise it | K11 open; strict test unknown-leaning-fail | K11 read | Kit D | Volumes fell more than 20% |
| H20-I1 | Small importers name costly entry incidents | — | A3 (importer side) | Kit C (§5.8) | None |
| H20-I2 | Some importers would buy directly: self-file, or a tool | Cohen self-filing row 0.10 | W5, Cohen | Kit D (§5.8) | All prefer the broker |
| H20-I3 | Importers hold unclaimed IEEPA refunds | CBP refunds opened 20 Apr 2026 (law-firm totals, *assumed*) | A6 | Refund look-back §6.4 | Already claimed by brokers |

---

## 4. Documented positions of the counterparty-only sides (C21)

### 4.1 C-11: LTL carriers (check T)

**Access.** Nine carrier rules tariffs were read at the source (Old Dominion, FedEx Freight, XPO, Estes, Saia, ArcBest/ABF, R+L, TForce Freight, Southeastern), along with the statute, 49 CFR Part 378, NIST Handbook 44 and NMFC item text from 2019-22. Most of the position is *verified*. The current NMFC rule text was not found.

**The position in eight lines:**

| Question | Desk answer | Label |
|---|---|---|
| The carrier's right to correct | NMFC Item 250100 (formerly Item 360) lets the carrier inspect, reweigh and correct the description. The bill of lading terms: "freight charges must be paid based upon the articles actually shipped". **No NMFC or federal rule sets what an inspection certificate must contain**, or requires photos | *verified* |
| What a correction costs | Re-rating, plus a **$15-55 fee** per correction. **Asymmetries:** R+L corrects weight upward only; ABF credits a reduction only above its $55 fee plus admin | *verified* |
| The proof carriers accept | **The shipper's own paperwork from before pickup:** "an invoice or packing slip along with a pre-printed specification sheet or catalog page" (Estes, SEFL, TForce). ODFL, R+L and Saia accept "conclusive documentary proof" at their own satisfaction or "sole discretion". TForce: a re-typed BOL "will NOT be accepted as proof". **No tariff names a scan, photo or third-party measurement as proof** | *verified* |
| Access to the carrier's record | Certificates and photos can be downloaded by **the bill-to party** (ODFL, XPO, TForce, R+L). Handbook 44: dimensioner data "available upon request by customer", but kept only **30 days after invoicing** | *verified* (Estes *assumed*) |
| Who may dispute | The shipper "or its authorized agent" (49 CFR 378.2(f)). A written claim with the freight bill; one claim can cover many shipments on the same issue. The carrier must acknowledge in 30 days and decide in 60, "citing tariff authority" | *verified* |
| Windows | Statute: 180 days each way (49 U.S.C. 13710(a)(3)); 18 months to sue (14705). **Tariffs count earlier:** some from shipment rather than receipt of the bill; a corrected BOL within 30 days (XPO, R+L); closed-claim rules (ODFL); arbitration clauses (XPO) | *verified* |
| How often, and how often won | **No neutral correction rate and no neutral win rate exist** (a second search, after S3a's). The one carrier-filed figure: FedEx Freight says dimensioners, used on over 90% of shipments, added over $150M across FY2024-25, **about 0.8% of revenue** [our calc]. That is all dimensioner re-rating, right or wrong, not a rate of wrong corrections. Vendor frequency claims span 4-39% of shipments and are unusable | *verified* / *assumed* |
| The NMFTA dependency | ClassIT+: a web seat costs $321-371 a year; the API for a small shipper or 3PL costs $2,967-3,924 a year. **Terms for a software provider serving many shippers are not public.** Three scenarios: one API licence covers all customers (a cost, about $4 per customer); each customer needs its own seat (41-417% of the per-shipper fee, close to a gate); third-party use barred (a gate) | prices *verified*; terms not found |

**What it means for the card [our call]:**
- **S4's question, "will an LTL carrier grant a credit on evidence we produce?", gets a split answer.**
  - We may file, as the shipper's agent.
  - Evidence we produce after the fact is unlikely to win, going by the tariff text: the freight is gone, and no tariff accepts a third-party measurement.
  - Evidence we **collect** from the shipper's own pre-pickup records, plus the carrier's certificate pulled within days, fits the carriers' own proof rules.
  - So C-11 reads as a **"capture evidence at origin, then file fast"** job rather than a "dispute after the fact" job. That is a wedge question for S6, recorded here per C18.
- **The disputes split into two kinds with different odds:**
  - "wrong item or description" reclasses, decided on documents and the NMFC text, where both sides see the evidence;
  - "disputed measurement" reweighs, decided at the carrier's discretion against a certificate the carrier made.
- **A1 carries a downward risk.** FedEx's bound suggests the reclass and reweigh money is of the order of 1% of LTL revenue at a large carrier, **at or below the low end of the card's 2-5% "avoidable" band.** And only part of that 1% is wrong. Extra-service charges are a separate, larger pool (AFS customer data: 8.7% of LTL spend, *assumed*). This makes H11-02 and the savings assessment the deciding tests for C-11.
- **F3 and F4 hold at 0.5; W3 and W6 hold but lean down; K4 stays open.** Corrections and credits are countable from carrier documents, but which corrections were wrong is not. The clocks are short and carriers keep discretion.
- **The NMFTA dependency is undecided between a cost and a gate.** Only NMFTA's licence terms decide it (D-20).

### 4.2 C-19: big-box retailers (check U)

**Access caveat.** Walmart, Target, Home Depot, Lowe's, Costco and Amazon publish their compliance manuals only behind supplier logins. Their rules below come from vendor, 3PL and consultancy guides (*assumed*, cross-checked where two sources agree). **Kroger's policy is public and was read in full** (*verified*).

**The position in six lines:**

| Question | Desk answer | Label |
|---|---|---|
| What is fined, and how much | Late and short deliveries, plus ASN, label and routing defects. **3% of the cost of the affected goods** is the common rate (Walmart, Target, Kroger). Home Depot and Lowe's take **10% offsets** plus flat fees ($250-1,000). Amazon charges 2-10% of cost | Kroger *verified*; the rest *assumed* |
| How it is collected | **Every retailer takes it out of what it pays the supplier.** The retailer acts first and the supplier disputes afterwards | Kroger *verified*; the rest *assumed* |
| Dispute windows | **From 48 business hours to 24 months, and the delivery fines have the short windows:** Home Depot about 4 weeks; Lowe's the 2nd-16th of each month; Walmart AP chargebacks 15-30 days; Amazon 30 days. Longer: Kroger 180 days (*verified*); Walmart shortages 12 months, general 24 months; Target 18 months; Amazon shortages 2 years. **Walmart's window for OTIF fines is unsettled** (vendors say 30 days, or no fixed window) | mostly *assumed* |
| What evidence wins | Signed BOL and POD, carrier and DC check-in times, appointment confirmations, ASNs. **Shifting:** Amazon no longer requires a POD and prefers unit-level receipt data; Walmart's AP dispute portal (APDP) rejects carrier-generated delivery reports | *assumed* |
| Direction since Jan 2025 | **Every dated rule change found tightens**, except Walmart's prepaid consolidation option (May 2026): Kroger's on-time bar 90% → 93% plus a new fee schedule (*verified*); Target's Perfect Order metrics (May 2025); Amazon's 2-year shortage cap and end of bulk disputes (2025); **Target's fines for disputing a fifth time or more** (by Nov 2025) | mixed |
| Pushback on automated disputing | Target's repeat-dispute fine and Amazon's end of bulk disputes both act on high-volume disputing, which is the method a software entrant would use | *assumed*; reading **[our call]** |

**What it means for the card [our call]:**
- **A3 firms up.** S4's caveat was that Walmart eased in 2024. The 2025 tightenings at Kroger, Target and Amazon are dated rules acting on this job, so A3 = 1 holds even under the strict reading.
- **Day-one back-claims are weaker than S3b assumed for delivery fines,** because their windows are short. They hold for shortages and invoice disputes. Check S's Home Depot "12 months" applies to invoice disputes, not to compliance offsets (a correction to `3_factsheets.md` C-19 item 7 / `4_scorecard.md` W3 evidence). W3 holds at 0.5.
- **The retailers are acting against automated disputing,** which leans W6 toward 0 and adds a second dependency to C20's record: the dispute rules themselves, as well as portal access.
- **What the 1-2 worker interviews must settle** (check U §6.2): Walmart's OTIF window in practice; the deduction mix (fines and shortages against pricing and promotions); what evidence wins per retailer; how often short windows are missed; the 2026 tool gap; the minimum client size recovery firms accept; how far the retailers' counter-moves cut win rates; whether carriers pay back fines they caused; and how many retailers a typical supplier sells to. All are in the kit (§5.6).

---

## 5. The plan

### 5.1 Recruiting (check V)

**Best channels per side** (check V §1; the ranking is check V's **[our call]**):

| Side | First channel | Backup | Cost | Desk difficulty |
|---|---|---|---|---|
| C-20 brokerages | **CBP's public permitted-broker list:** name, city, state, phone and email; free; updated quarterly. 14 regional broker associations meet monthly, with dated meetings from 23 Sep | NCBFAA's public broker search; r/CustomsBroker | Free | **Easiest.** One official list names every buyer. The limit is its size: 2,365 brokerages |
| C-09 carriers | **FMCSA census file:** 33,424 active interstate general-freight carriers with 10-199 trucks, 33,001 of them with an email **[our calc]** | Phone the office and ask for billing; ATA MCE (17-20 Oct), F3 (27-28 Oct) | Free | 2nd |
| C-11 LTL shippers | **Named-firm lists:** STAFDA's 191 exhibitors, FABTECH, PACK EXPO, state manufacturers' associations → "shipping / logistics manager" | About 20 local CSCMP roundtable events, 17 Sep-30 Oct; a B2B panel | Free; panel ≈ $200-300 an interview | 3rd. "Shipping manager" is not a uniform title |
| C-20 importers | **Ask every broker interviewee to introduce one small importer client** (an introduction is also a commitment) | ImportYeti's free bill-of-lading search; Amazon-seller communities | Free | 4th. Easy once broker interviews are under way |
| C-09 shipper finance | **A B2B research panel with a screener** ("approves or codes freight invoices") | LinkedIn Sales Navigator ($119.99 a month) on firms from exhibitor lists; IOFM (2-4 Nov), AFP (8-11 Nov) | Panel ≈ $200-300 an interview | 5th. No gathering place for people who pay freight bills was found |
| C-19 suppliers | **LinkedIn Sales Navigator title search:** deductions, customer compliance, retail compliance, credit manager + retailer names | A panel or pay-per-call network; CRF October Forum (26-28 Oct), RVCF (1-4 Nov), PLMA (15-17 Nov) | $119.99 a month; panel ≈ $280-410 an interview | **Hardest.** No list of suppliers by retailer, and the gathering places fall after the window |
| Counterparty workers | **Pay-per-call expert networks:** about $300 for a 30-minute AlphaSense call **[our calc]**; also Office Hours | Direct approach to recovery firms, LTL 3PLs and audit firms as organisations | ≈ $300 a call; avoid the big networks' annual minimums ($1,000-1,500 an hour, *assumed*) | Only 2-4 calls needed |

**Four findings that shape the plan:**
1. **Most events fall after a four-week window.** Of 37 dated event lines, 9 start by 14 Oct (check V §10.1). The window rests on lists, associations' monthly meetings and paid routes. Events are a second wave (D-19).
2. **Cold email alone is slow.** Vendor benchmarks put replies at 0.45-3.43% (*assumed*), so five meetings can take hundreds of messages. Every side therefore pairs a list with a warmer route.
3. **Paid interviews say little about reachability.** People take a paid research call more readily than a sales call, so a side filled through panels is weak W1 evidence (check V §10.2). The funnel log marks every interview as paid or unpaid (`5_log.md` §1), and the W1 reading rules in §7.2 use that split.
4. **Cash budget, if every side needed paid routes [our calc]:** about 34 × $200-300 ≈ $7-10k. Using the free lists for C-20, the carriers and C-11, and referrals for importers, puts it nearer **$2-4k**. The main paid items are C-19, the C-09 finance side and the counterparty workers (D-16).

### 5.2 Sequence [our call]

S5 is scheduled as four weeks, 21 Sep to 16 Oct 2026, inside Aulet's "at least a few weeks" (R15). The founders' capacity sets the real pace.

| Week | Dates | Work |
|---|---|---|
| 0 | 16-18 Sep | Founders decide D-14 to D-19 (§10). Fix the 1-10 re-score rules **before any evidence arrives** (P1: rules before candidates). Build contact lists from check V |
| 1 | 21-25 Sep | **Outreach wave 1 to all four paying sides and to the counterparty workers.** R15 says to start with the harder side: C-11's and C-19's harder sides are covered by checks T and U, and C-09's and C-20's harder sides are their paying sides (S1 cards). Log every contact (`5_log.md` §1) |
| 2 | 28 Sep-2 Oct | Paying-side interviews. Ask the first willing interviewee on each card for data (kit §6). Outreach to the second sides (C-09 carriers, C-20 importers). Worker interviews |
| 3 | 5-9 Oct | Remaining interviews. Run the four assessments by hand. Price tests. Apply the early-stop rule if adopted (P-24) |
| 4 | 12-16 Oct | Close the log. Re-score on the 1-10 scale (§7). Gate check (§8). Hand-off to S6 |

**If capacity binds:** finish the paying sides first, because every gate item is counted there. Then the worker interviews, then the second sides.

---

## 6. Savings assessments and price tests (steps 3-4)

The protocols are in `5_interview_kit.md` §6. In summary:

| Card | Assessment on real data | What it measures | Rows it moves | Proposed price (D-15) |
|---|---|---|---|---|
| C-09 | Look-back audit of 1-3 months of paid invoices | Overpayment rate; recoverable dollars | A1, F4, K5 share, W3 | 25% of credits recovered, or $500 flat; fallback free. *D-23 (2026-10-08): written for an audit service; the method and price test are rewritten after the founders adopt the re-run's look-back design (kit §6.1 banner)* |
| C-11 | 90-day correction look-back, plus 3-5 disputes filed | Correction rate (settles K4 for one customer); disputes won | A1, F2, F3, F4, K4 | 30% of credits won, or $150 flat; fallback free |
| C-19 | One quarter of one retailer's deductions, plus 5-10 disputes | Non-trade % of sales; invalid share; share lost to windows | A1, F4, W4, H19-03 | 25% of recoveries, or $500 flat; fallback free |
| C-20 | Timed study of 3-5 live entries plus 20 past entries | Minutes per entry; share spent on classification and keying | A1, A2, F4, W3 | LOI at $5 per entry for a pilot; fallback a free 50-entry pilot |

---

## 7. How the re-score works (step 7): proposed rules, to fix before interviews

S0 fixed the scale as "1-10 after the S5 interviews" (`0_criteria.md` §5) but not what each point means. Setting anchors after the evidence is in would let the scores drift toward a favourite, which P1 exists to prevent. These rules are proposal **P-25** **[our call]**.

### 7.1 The evidence ladder (every row)

| Score | Evidence needed |
|---|---|
| **9-10** | Measured on real customer data (an assessment, a dispute run, a time study), or backed by commitments of type 2-4, with no contrary interview |
| **7-8** | At least 3 interviews on the relevant side support it with specific past events (with an amount where the row is about cost), and at most 1 contradicts |
| **5-6** | Mixed: support and contradiction roughly balance, or the support is opinion or future intent only |
| **3-4** | At least 3 interviews on the relevant side contradict it with specific past events |
| **1-2** | Contradicted by real data, or a show-stopper found: a dominant vendor whose customers say they are satisfied; a counterparty that refuses evidence from a third party; no data access at all (R30) |
| **Desk only** | No S5 evidence touches the row. Convert the S4 score: **1 → 6, 0.5 → 4, 0 → 2**, and flag it. A tested and supported row (7+) then outranks an untested one |

### 7.2 Which evidence feeds which row

| Row | Main S5 evidence |
|---|---|
| A1 Savings pool | The measured rate from the assessment replaces the **[our call]** share in the fact sheet's range; interview incident amounts as a check |
| A2 Fit for automation | Job maps (kit block B): the costly steps are office work |
| A3 Pain and urgency | Costed incidents (gate count); the top-three vote rank; unprompted mentions of the dated triggers |
| A4 Fragmentation | Census data; not moved by interviews (desk only) unless the interviews show a different paying side |
| A5 Frequency | Kit block D frequency |
| A6 Expansion | Adjacent problems named unprompted; the importer refund look-back (C-20) |
| W1 Access | The recruiting funnel (`5_log.md` §1). **Reading rules, set before recruiting** (check V §10.3): W1 leans to 1 when ≥60% of qualified interviews come from one unpaid channel, the first meeting lands within 7 days, and the paid share is 0. W1 leans to 0 when the paid share is ≥50%, or no unpaid channel gets above 1 held meeting per 100 contacts. Otherwise it stays in the middle. On the 1-10 scale: "leans to 1" = 8-10, "middle" = 4-7, "leans to 0" = 1-3 |
| W2 Team | Unchanged until immersion (F-15): desk only |
| W3 Whole product | Data shared, in what form, and how long it took; the counterparty's evidence rules (checks T, U) |
| W4 Competition | Today's spend and tools (block D); satisfaction with any incumbent (show-stopper test) |
| W5 Willingness to change | Commitments; price-test answers |
| W6 Time and resources | Licence, bank and certification needs named in interviews; counterparty dependencies (checks T, U) |
| F1-F5 | Price-test answers (F1, F2); data and evidence access (F3); the measured rate's spread (F4); who pays and who keeps the saving (F5) |
| Cohen rows | Plausible from the buyer count; Self-Aware from the share who raise the problem unprompted; Liquid and Eager from commitments and price answers |

**Counterparty-only sides [our call], proposal P-26:**
- they are not scored on the per-side rows (A3, W1, W5), because C21 never interviews them as buyers;
- their documented position feeds F3, W3, W6 and the show-stopper check.

**Axis totals:** weight × score ÷ 10 per row, summed per axis (0-100). The rest of `0_criteria.md` §5 applies unchanged: the better side (A4 on the paying side, C19), the show-stopper veto, and F1-F4 cut lines scaled to the new scale **[our call]** (plausible at 30 of 40 or more; hybrid at 20-29; below 20 flag).

### 7.3 The re-score sheet (to fill at week 4)

| Row | Weight | C-09 S4 | C-09 S5 | C-11 S4 | C-11 S5 | C-19 S4 | C-19 S5 | C-20 S4 | C-20 S5 | Evidence links |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | 20 | 1 | | 1 | | 0.5 | | 1 | | |
| A2 | 10 | 1 | | 1 | | 1 | | 1 | | |
| A3 | 25 | 1 | | 1 | | 1 | | 1 | | |
| A4 | 15 | 0.5 | | 0.5 | | 0.5 | | 0.5 | | |
| A5 | 15 | 1 | | 1 | | 1 | | 1 | | |
| A6 | 15 | 1 | | 1 | | 1 | | 1 | | |
| **Axis A** | 100 | **92.5** | | **92.5** | | **82.5** | | **92.5** | | |
| W1 | 20 | 0.5 | | 0.5 | | 0.5 | | 1 | | |
| W2 | 5 | 0 | | 0 | | 0 | | 0 | | |
| W3 | 20 | 0.5 | | 0.5 | | 0.5 | | 0.5 | | |
| W4 | 15 | 1 | | 1 | | 1 | | 0.5 | | |
| W5 | 15 | 0.5 | | 1 | | 1 | | 1 | | |
| W6 | 25 | 0.5 | | 0.5 | | 0.5 | | 0.5 | | |
| **Axis W** | 100 | **55** | | **62.5** | | **62.5** | | **65** | | |
| F1-F4 | — | 3.5 | | 3.0 | | 3.5 | | 3.5 | | |
| F5 | — | 1 | | 1 | | 1 | | 0.5 | | |
| Cohen | — | 1.00 | | 1.00 | | 1.00 | | 0.08 | | |

S4 values are from `4_scorecard.md` §2.1 and §9.4.

---

## 8. Gate tracker (per finalist)

The gate as changed by C21 (`submarket_selection.md` §4 S5):

| Gate item | C-09 | C-11 | C-19 | C-20 |
|---|---|---|---|---|
| **Paying side:** at least 5 interviews | 0 / 5 | 0 / 5 | 0 / 5 | 0 / 5 |
| **Second side:** 5 interviews if it could buy from us; documented position + at least 1 worker interview if counterparty-only | 0 / 5 (carriers) | **Position: done** (check T; §4.1) · workers 0 / 1 | **Position: done** (check U; §4.2) · workers 0 / 1 | 0 / 5 (importers) |
| At least 3 costed incidents on the paying side | 0 / 3 | 0 / 3 | 0 / 3 | 0 / 3 |
| At least 2 commitments on the paying side | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 |
| A named data source + at least 1 interviewee willing to share | named: invoices, rate agreements, PODs · willing 0 | named: LTL invoices + BOLs + inspection records · willing 0 | named: portal export / EDI 812-820 + PODs · willing 0 | named: entries + commercial invoices · willing 0 |
| A savings assessment on real data, or a written reason why not | not started | not started | not started | not started |
| **Kill condition (C22, `4_kill_conditions.md`)** *(row added 2026-09-22)* | ~~written §2: leak < 0.75% kill, ≥ 1.3% pass; access 2 of 3 refuse; measured cost at $1.5M~~ **adopted 2026-10-09 (C29, `4_kill_conditions.md` §2.5.12): Kill / Cover / Pass at the shipper's size (at $1.5M: < 0.044% / 0.51% / ≥ 6.44% flagged); access 2 of 3 decline; the customer's hours over twice capacity** · **not yet measured** · *~~re-run pending~~ **re-run 2026-10-08 on the software basis (D-23), ~~proposed and not adopted~~ adopted 2026-10-09 (C29)** (`4_kill_conditions.md` §2.5): Test 1 kill under ~~0.78%~~ 0.044% (acquisition cost bounded at $0-$10k until the first customer is timed (`4_kill_conditions.md` §2.5.11)) and pass at 6.44% of in-window spend flagged and accepted, at a $1.5M shipper (table by size), with the middle band settled by follow-through in a pilot; Test 2 unchanged; Test 3 the customer's timed hours against capacity. ~~§2.4's lines stay frozen and in force until the founders adopt new ones.~~ §2.4's lines are struck through. Founders' answers 2026-10-08 (§2.5.10): a subscription, hours as capacity, the look-back design and Test 1 on flagged dollars are decided; P-31 is deferred; the acquisition cost is ~~open~~ ~~deferred until the first customer is timed~~ bounded at $0-$10k until the first customer is timed (`4_kill_conditions.md` §2.5.11), ~~so the new lines are not adopted yet~~; the founders adopted them on 2026-10-09: "Adopt the Kill/Cover/Pass lines"* | **C-11 eliminated 2026-09-22 (D-22)**: fails even at the ceiling (`4_kill_conditions.md` §3.7); lines not adopted | **adopted and frozen 2026-09-22 (D-22, §4.7)**: provable-invalid non-trade deductions < 0.05% of sales kill, ~~≥ 0.17% pass~~ **≥ 0.22% pass at a $50M supplier, table by size (C27)**; measured on a supplier screened at 1% or more of non-trade deductions (C26); access 2 of 3 refuse or retailer bars third parties; measured cost at a $50M supplier · not measured | **C-20 eliminated 2026-09-22 (D-22)**: viable on paper but not pursued; its saving is paid staff time (`4_kill_conditions.md` §5.7); lines not adopted |
| **Gate** | **not met** | **eliminated (D-22)** | **not met** | **eliminated (D-22)** |

*Update 2026-09-22 (D-22, `4_kill_conditions.md` §7.4):*
- **S5 now covers C-09 and C-19 only.**
- C-11's slots (5 paying-side interviews plus 1-2 workers) move to C-09, favouring LTL-heavy shippers.
- Where C-20's freed slots go (5 broker and 5 importer interviews) is not yet decided.

*Update 2026-09-22 (S4.5, C25; `4_5_profitability.md` §3.6):* **C-19 is "not provable from the web".** On neutral inputs the typical small supplier is not a profitable customer; the business rests on an upper tail of suppliers. Two measurements are proposed for C-19's look-back (P-29, not applied): screen recruits for non-trade deductions of 1% of sales or more, and record the screen yield and the share the supplier would not have recovered on its own.

---

## 9. What the desk half found

Desk evidence **does not change any score**: S5's re-score uses the 1-10 rules in §7 once primary evidence exists. It does change what the interviews must test, and it answers two of S4's desk questions.

### 9.1 C-19's two desk gaps (check U §4-§5)

**The buyer count: about 15,000-55,000 small and mid-sized suppliers sell direct to big-box retailers; central about 29,000** [our calc on [our call] factors].
- **Anchor:** Walmart publishes **31,196** US supplier records (Dun & Bradstreet, FYE 2025, *verified*), and says more than 60% are small businesses.
- **Adjustments [our call]:** double counting across states (× 0.75-1.0), suppliers in scope of delivery fines (× 0.6-0.9), a size cut to $500M of sales (× 0.85-0.95), and an uplift for suppliers of other retailers that don't sell to Walmart (× 1.3-2.0). **The uplift is the weakest factor.**
- **Cross-checks:** SPS Commerce's 46,900 1P customers (10-K, *verified*) and Census SUSB's 33,915 consumer-goods firms with 20-499 staff are consistent with the range. A 100,000+ count is not.
- **Cohen's Plausible row:**
  - The central count rounds to 10,000, so **C-19's Cohen score stays 1.00**, now on a published anchor instead of a judgement.
  - **It is a knife-edge.** Above 31,623 the row rounds to 100,000 and the score becomes 10.00, which is the upper ~42% of the range. The worker interviews' overlap question (how many retailers a client sells to) is what would move it.
- **Per buyer:** a central fee pool of $33M ÷ 28,766 ≈ **$1,150 a year**, consistent with S4's Lucrative row of $1,000 [our calc].

**The 2018 gap: still open, but narrowing.** Among suppliers with sales of $500M or less:

| Survey year | Use no third-party deduction technology | Label |
|---|---|---|
| 2018 | 70% | CRF PDF, *verified* (association flag) |
| 2021 | 65% | CRF survey shown on a deduction-software vendor's (Carixa) slide, *assumed* |
| 2023 | **55%** | same slide, *assumed* |

- **Caveats:** sample sizes are not shown; the respondents are credit professionals who chose to answer, so likely more automated than average; and "third-party technology" is broad.
- **SPS has not closed the gap.** Its disclosed recovery base is about **550** 1P customers (10-K, *verified*), about 1-3.5% of the buyer count [our calc]. **But it has aimed at it:** in June 2026 it sold its Amazon-seller recovery business (about 7,300 customers) to focus on "1P suppliers who operate multi-retailer trading relationships", which is this card's buyer. Its take-rate revenue came in at "the lower end" in Q4 2025, citing Amazon's policy changes (*assumed*: call transcript).
- **A new funded entrant:** Glimpse, $52M raised, "more than 200 retail brands" (*assumed*).
- **Reading [our call]:** W4 holds at 1 on the letter (most small suppliers still used no tool in 2023), but S4's sensitivity W4 = 0.5 is now closer. W6 leans toward 0: SPS is now aimed at this card's buyer, a funded entrant has arrived, and the retailers are acting against automated disputes. **H19-04 is the test,** and the show-stopper question is whether SPS users are satisfied.

### 9.2 Recruiting (check V)

See §5.1. Every paying side has a named first channel. **C-20 is the easiest side to reach and C-19 the hardest,** which matches their W1 scores of 1 and 0.5. The funnel log will test both, under the rules in §7.2.

### 9.3 C-11's counterparty (check T)

See §4.1. In short:
- **No neutral correction or win rate exists**, so K4 stays open. The savings assessment (kit §6.2) and the worker interviews are the only sources left.
- **The best new fact is a ceiling, not a floor:** FedEx Freight's filing puts dimensioner re-rating at about 0.8% of revenue over two years. It puts C-11's A1 at risk, because the card's savings range assumes 2-5% avoidable.
- **The carriers' own rules reward origin documents and punish late evidence,** which reframes the job toward capture at pickup.
- **The class-data licence is the one question only NMFTA can answer** (D-20).

### 9.4 Correction to earlier records

**Check U:** Home Depot's "12 months" in check S applies to invoice disputes, not to compliance offsets, whose window is about 4 weeks. This bears on the W3 evidence line for C-19 in `3_factsheets.md` (item 7) and `4_scorecard.md` §2.2. **The score is unchanged (W3 = 0.5).** Only the day-one back-claims argument is weaker for delivery fines, and it still holds for shortages and invoice disputes.

---

## 10. For the founders

### 10.1 Decisions (before the first call)

The default in each row is this file's suggestion **[our call]**.

| # | Decision | Default suggested here |
|---|---|---|
| **D-14** | **Process proposals P-23 to P-26** (§10.2): adopt, park or reject each. P-25 has to be settled before the first interview | Adopt all four |
| **D-15** | **Prices for the assessments and pilots** (§6; kit §6) | As proposed. Each is below the going service rate, and each has a free fallback so the data still arrives. *D-23 (2026-10-08): for C-09, "the going rate" now also means self-serve software prices (Freightview $149 a month for up to 50 shipments; check Z); the C-09 price test waits for the re-run* |
| **D-16** | **Incentives and paid recruiting** (§5.1; check V §8.2, §9.1) | $75-100 per call for staff; $150-200 for owners, controllers and deductions managers; or a charity donation. Use pay-per-call networks (about $300 a call) for the 2-4 counterparty workers, and a panel only where free routes fail (C-19, C-09 finance). **Budget about $2-4k, cap $10k.** No annual expert-network contracts |
| **D-17** | **Register for the 2026 3PL Study (R37)?** It sits behind a registration form (`submarket_selection.md` §4 S5, "Reading before interviewing") | Optional. It covers shippers and 3PLs in general, not these four jobs |
| **D-18** | **Data handling:** a mutual NDA before real data; raw files kept outside this folder and deleted after the assessment; bank details removed at source (kit §1.3) | Adopt |
| **D-19** | **Time box:** four weeks, ending 16 Oct 2026, with the paying sides first if capacity binds (§5.2) | Adopt. **If C-19 or the C-09 finance side is short at week 4,** extend those sides only, to 11 Nov: CRF (26-28 Oct), RVCF (1-4 Nov), IOFM (2-4 Nov) and AFP (8-11 Nov) all fall in that stretch (check V §1.1). The other cards are re-scored on time |
| **D-20** | **Ask NMFTA how a software provider may license NMFC class data for many shippers?** This is the one question that decides whether C-11's dependency is a cost or a gate (§4.1). It means contacting an outside body (classitplus@nmfta.org), so it is the founders' call. The agents were told not to contact anyone | Ask now, as a research question, without describing a product. It costs one email, and the answer settles a scenario the interviews cannot |

### 10.2 Process changes proposed (not applied)

| # | Proposal | Why |
|---|---|---|
| **P-23** | **One interview can count toward two shipper cards** (C-09, C-11, C-19) when the incident module for each card was completed in full | The three cards share a paying population: manufacturers and distributors. A furniture maker that ships LTL and sells to Home Depot is a valid interview for both C-11 and C-19. Without this, capacity goes to finding separate people for problems the same person has |
| **P-24** | **Early stop:** a card whose first 5 paying-side interviews produce no costed incident and no commitment stops S5 work, and its remaining conversations move to the other cards. The stop and its evidence are recorded as the kill. *2026-09-22:* the numeric stop lines now come from C22's kill conditions (`4_kill_conditions.md`); P-24's interview-count stop stays proposed | S5's purpose is to "confirm or kill". Running the second side of a card whose paying side has no costed problem spends capacity on a card the gate has already failed |
| **P-25** | **Fix the 1-10 anchors before interviews** (§7.1-7.2), including the desk-only conversion 1 → 6, 0.5 → 4, 0 → 2 | S0 set a 1-10 scale but no anchors. Setting them after the evidence would break P1, "fix the rules before looking at candidates" |
| **P-26** | **Counterparty-only sides are not scored on per-side rows.** Their documented position feeds F3, W3, W6 and the show-stopper check | C21 covers these sides by documented position, not buyer interviews, so their A3, W1 and W5 would have no evidence. Under the better-side rule (C5), an unscored side cannot win a row anyway |

---

## 11. Sources

- **Rules applied:**
  - `submarket_selection.md` §4 S5 (steps, gate, C21), §5 (the two-sided rule, scorecard, fee questions, checks), §9 (T4, T8, T10), §10 (interviews knob), §13 (interview log template);
  - `0_criteria.md` §4-§5.
- **Card evidence:**
  - `3_factsheets.md` (C-09, C-11, C-19, C-20);
  - `4_scorecard.md` §2-§4 (scores, fee reasoning, checks), §6.5-§6.6 (sensitivities), §7-§7.1 (deciding factors, what S5 must test), §9 (D-9 to D-13, C19 re-score);
  - `1_candidates.md` (roles and harder sides);
  - `3a_unknowns.md` (open unknowns).
- **Method sources:**
  - R15 (Aulet: primary research, inquiry mode, the hypothesis log format, "harder side first");
  - R35 (the Mom Test);
  - R18 (Ulwick: job map);
  - R38 (ATRI: top-three vote split by actor type);
  - R24 (Euclid: monetisation as discovery);
  - R28 (Bessemer: lightweight savings assessments);
  - R17 (Moore: pragmatists want references).
- **New desk research:** checks T, U and V (sources N-T, N-U, N-V; see each file's sources table).
