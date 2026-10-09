# Run 01, S4 step 7: per-customer profit and kill conditions

> **Stage S4 of `submarket_selection.md` §4, step 7 (added 2026-09-22 as C22). Applied to run 01 late, after S4 closed and before the first S5 interview.**
> **What this is:** for each finalist, a per-customer profit model built from the desk evidence, and a **kill condition** fixed before the S5 savings assessment runs. The kill condition names the measurement S5 makes, the line below which the card stops, and who decides.
> **Why it exists:** through S4 the scoring measured the size of the pool (A1, K5) and whether a fee was chargeable in principle (F1-F5). It never measured profit per customer. That row entered only at S6 for C-09 (`6_focused_target.md` §4.4) and it is the row that now hurts. The founders decided on 2026-09-22 to make it an S4 step for later runs and to run it now against all four finalists (`4_scorecard.md` §9.1, D-21).
> **Status:** C-09 done here (§2, lines frozen 2026-09-22). C-11, C-19 and C-20 were filled on 2026-09-22 by the chat briefed in `handoff.md` (§3-§5), using three new checks (AD, AE, AF) and real documents: court exhibits, bankruptcy payment lists, SEC filings, published price lists and CBP notices. §6 sets the four cards side by side and applies the founders' elimination rule of 2026-09-22; §7 is the decision record (D-22). **Decided by the founders the same day (§7.4): C-11 and C-20 are eliminated; C-19's lines are adopted and frozen; the focus is now C-09 and C-19.** *Later the same day:* C-19's look-back is run on a screened supplier (C26), and its pass line was re-derived from 0.17% to 0.22% at a $50M supplier (C27; §4.7). *2026-10-08:* C-09's model and kill condition re-run on the software basis (D-23) are in **§2.5, proposed and not adopted**; §2.4's lines stay frozen and in force until the founders adopt new ones.
> **Labels:** *verified* = read at the source; *assumed* = vendor, association, snippet or secondary; **[our calc]** = arithmetic; **[our call]** = judgement.
> **Nothing here re-scores a card.** The kill conditions are tests S5 will run. The lines are fixed now so that they are not tuned to the result (P1, "fix the rules before looking at candidates").

## 1. The step, as it applies to every card

**Purpose:** find out, before any interview, whether one customer of this card can pay us more than it costs to serve them, and write down the measurement that will settle it and the line at which the card stops.

**Steps:**
1. **Build the per-customer chain** from the fact sheet's fee unit (S3b item 10) and savings pool (item 2):
   - **Fee per customer** = unit volume per customer × leak or waste rate × share software removes × share actually realised (credited, collected or prevented) × fee share.
   - **Gross profit per customer** = fee − cost to serve (variable cost per unit + fixed cost per customer a year + onboarding, spread over the expected life).
   - Use the fee shares modelled at S0 (10 / 20 / 35%) plus the share the S5 price test will offer.
2. **Source every input** and label it. The leak rate needs the neutral evidence, the vendor claims and the carrier- or counterparty-side ceiling, each labelled. Cost to serve uses BLS wages grossed up to compensation, published machine-reading prices, and minutes per unit; where minutes come from vendors, say so (method: `research/s5_check_AA_c09_cost_to_serve.md`).
3. **Compute four numbers [our calc]:** the customer size at which gross profit is zero; the leak rate needed to cover variable cost at the modelled share; the same two with the cheapest allowed review labour; and the customer size at which the fee reaches check A's $5k-a-year benchmark for direct selling (`research/s0_check_A_ambition_economics.md` §A3). Compare the payback on winning a customer with check A's 12-month norm.
4. **Write the kill condition.** It must be:
   - **measurable in S5** by the savings assessment (`5_interview_kit.md` §6.1) or the data-access test, not by opinion;
   - **three-banded:** kill / conditional (with the condition named) / pass;
   - **fixed before the assessment runs**, and moved afterwards only through `submarket_selection.md` §9;
   - **owned:** the founders decide on the evidence in `5_log.md`, and the kill is recorded in the run's decision file.
5. **Enter it in the S5 gate tracker** (`5_validation.md` §8) as its own row. A card with no kill condition does not go to S5.

**Output:** this file. **Gate:** every card sent to S5 has a kill condition with a numeric line.

> **Note, 2026-10-08 (D-23):** the founders decided the company is a software company with no analysts and no manual review ("We have no analysts, this is a software company … we do no manual reviews here"; `software-initial-pitch.md` §1A). Steps 2-3 and Test 3 of the template assume **our own** review labour: "BLS wages … and minutes per unit", "the cheapest allowed review labour" and "measured minutes". Under D-23 no card's model may include our own review labour; the customer's staff review and file. A template adapted for software is to be proposed by the C-09 re-run as **P-31** (`handoff_c09_software_rerun.md` §4). Until the founders adopt it, this template stands as written.

**Template:**
```
Card | Fee unit | Chain (unit volume × leak × removed × realised × share − cost)
Inputs table: value | label | source
Four numbers: break-even size | rate to cover variable | both with cheapest labour | size for $5k
Kill condition:
  Test 1 (the leak): measured [rate] on [base] in the first assessment: kill < X | conditional X-Y | pass ≥ Y
  Test 2 (access): [documents] refused by N of the first M paying-side interviewees → kill
  Test 3 (cost, measured): gross profit at [reference size] from measured minutes and units: kill / conditional / pass
Verdict rule | Who decides | Where recorded
```

---

## 2. C-09 · Checking and paying truckload and LTL freight bills

> **Basis superseded by D-23 (2026-10-08, `software-initial-pitch.md` §1A).** The inputs, the four numbers and Tests 1 and 3 below cost **our own analysts' review** (US and offshore wages) and assume **we file the disputes**. Under D-23 the customer's staff review the flagged bills and file the disputes; we employ no analysts. The re-run is briefed in `handoff_c09_software_rerun.md` and is written as **§2.5** (2026-10-08, proposed, not adopted). **The lines in §2.4 stay frozen and in force until the founders adopt new lines** (then a `submarket_selection.md` §9 entry, C28); no look-back starts before then.

### 2.1 The chain

**Fee per customer** = truckload and LTL spend × overcharge rate × share caught × share carriers credit × fee share.
**Gross profit** = fee − (invoices × cost per invoice + disputes × cost per dispute + $400 fixed).

The model is the one in `6_focused_target.md` §4.4.4, built from checks X, AA and AB. It is restated here with the practice audit's stress inputs added.

### 2.2 Inputs

| Input | Central | Range | Label | Source |
|---|---|---|---|---|
| Overcharge rate (share of spend billed wrong in the carrier's favour) | 1.5% | 0.3-3% | **[our call]**; every neutral figure is under 0.5% | check X §2; check AB §2-§3: six vendor cases 0.8-4.2% (median 1.8%, five are large first-year programmes); USDA 1977 co-operatives 0.45% (*verified*); GSA post-payment 0.07% (*verified*, pre-audited bills); mature programmes 0.5-1.5% (*assumed*); FedEx Freight gives back 1.3-2.6% of revenue for all causes (*verified*, a ceiling) |
| Share caught | 70% | 50-80% | **[our call]** | GAO 1992: one professional audit found 72-78% of what two found (*verified*) |
| Share carriers credit | 75% | 41-90% | **[our call]** | check AB §4: 60-90% prompt, 41-51% aged (*assumed*); the 180-day rule, *Southern Furniture v. YRC* (*verified*) |
| Fee share | 25% | 10-50% | *assumed* | contingency firms 25-50%; small shippers often 50/50 (check X §5.1) |
| Invoices per $1,000 of spend | 1.5 | 1.0-2.9; **ABF account 2.21** | **[our calc]** | Saia LTL bill $347.81 (*verified*) against Cass all-mode $1,011; practice audit §5 |
| Share of invoices needing a human | 15% | **ABF account 58%** | **[our call]** | check AA; practice audit §5 |
| Minutes per human review | 6 | 3-13 | *assumed* (vendors put a full manual audit at 8-13) | check AA §AA3 |
| Loaded wage, US clerk | $36.79/h | — | *verified* (BLS May 2025 $25.75 × 1/0.70) | check AA |
| Loaded wage, offshore reviewer | $12/h | $6-16 | *assumed* | check AA §3.3 |
| Machine reading per invoice | $0.10 | $0.005-0.50 | *verified* prices, **[our calc]** per packet | check AA |
| Disputes per invoice, cost per dispute | 5%, $9.30 | — | *assumed* | check AA |
| Fixed cost per customer a year | $400 | $150-1,100 | *assumed* | check AA |
| Collectable share of a 12-month look-back | ~50% | — | **[our calc]** | 180 days of 365 (check AB §4.2) |

### 2.3 The four numbers [our calc]

Fee per $1,000 of in-window spend at the central chain (rate r × 0.70 × 0.75 × 0.25) = **$131.25 × r**, so $1.97 at 1.5%.

| Configuration | Cost per $1,000 | Break-even spend (fixed $400) | Rate to cover variable cost at 25% | Rate at a 45% share |
|---|---|---|---|---|
| Model central: 1.5 invoices, 15% human, US wages | $1.68 | **$1.35M** | **1.28%** | 0.71% |
| Same, offshore review | ≈$0.60 | **$0.3M** | **0.46-0.50%** | 0.27% |
| Practice-audit stress: 2.21 invoices, 58% human, US wages | $5.96 | never at 1.5% | 4.54% | 2.52% |
| Practice-audit stress, offshore review | $2.79 | never at 1.5% | 2.13% | 1.18% |

- **Spend at which the fee reaches $5k a year** (check A's direct-selling benchmark) at the central chain: **$2.5M**; at 3%: $1.3M; at 0.75%: $5.1M.
- **Payback:** at the model's $1.59M customer, gross profit is about $70 a year, so a $5-15k acquisition cost never pays back. At $2.9M spend, gross profit is about $460, payback over ten years. The customer only pays back at a rate near 3% or at spend above about $5M, which is FAP territory. This is the finding that makes the kill condition necessary.
- **Look-back:** a 12-month look-back collects on about half its dollars, and loses money at every size (`6_focused_target.md` §4.4.4). The product tested at S5 is therefore **audit inside the claim window, then monthly**.

### 2.4 The kill condition · ~~frozen 2026-09-22~~ superseded 2026-10-09 (C29)

> **Superseded 2026-10-09 (C29).** The founders adopted the software-basis kill condition (§2.5.12; verbatim: "Adopt the Kill/Cover/Pass lines"). The lines below are struck through and kept for the record.

**Measured in:** the first C-09 savings assessment (`5_interview_kit.md` §6.1) on one real shipper's paid truckload and LTL bills, rate agreements with dated versions, fuel schedules, BOLs and PODs, under a mutual NDA. At least three months of bills. Hours recorded.

**Definitions [our call]:**
- **In-window spend:** the billed dollars on bills still contestable on the day of the assessment, using 180 days from receipt (49 U.S.C. 13710) or the contract's own window if longer.
- **Measured overcharge rate:** dollars flagged as billed wrong in the carrier's favour **and provable from the documents held**, divided by in-window spend. Corrections that the documents show to be legitimate (the shipper's own BOL was wrong) are excluded. Dollars flagged but unprovable are recorded separately and not counted.
- If two assessments are available, weight by spend.

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Measured overcharge rate on in-window spend | ~~**under 0.75%**~~ | ~~0.75% to 1.3%. Continues only if the price test shows a share of 45% or more is accepted, or the interviewee accepts offshore handling of its invoices (kit question), or Test 3 shows measured cost well under the model~~ | ~~**1.3% or more**~~ |
| **2. Access** | The rate agreement and paid invoices, under a mutual NDA | ~~**2 of the first 3 paying-side interviewees decline**~~ | ~~1 of 3 declines~~ | ~~all 3 agree, or 1 declines and a replacement agrees~~ |
| **3. Cost, measured** | From the assessment's recorded minutes, bills per $1,000 and human-review share: gross profit at a $1.5M reference customer, 25% share, at the measured rate | ~~**negative under US and offshore wages**~~ | ~~negative under US wages, positive offshore~~ | ~~positive under US wages~~ |

**Why these lines [our call]:**
- **0.75%** is the midpoint of the mature-programme range (0.5-1.5%). Every provider that splits year one from later years reports a large fall, so a first assessment under 0.75% forecasts an ongoing rate near 0.3-0.4%, below the offshore floor of 0.46-0.50%. At 0.75% and US wages, even a 45% share only covers variable cost, leaving nothing for the $400 fixed cost or for winning the customer.
- **1.3%** is the rate at which US-staffed review covers its own labour at a 25% share (1.28%, rounded). Above it the design works as modelled; between the lines it works only with offshore review or a higher share, both of which the interviews test.
- **2 of 3 on access** because without the agreement the audit is arithmetic, and the practice audit showed arithmetic is already right: 101 of 101 bills reconciled, $0 provable. A product that cannot get the agreement does not exist (check AC §8; H09-07).
- **Test 3** exists because the practice audit's two stress inputs, 2.21 invoices per $1,000 and 58% of bills needing a human, would sink the model at any plausible rate. They came from one LTL-heavy account billed through a 3PL, so they are a stress case, not a finding. The assessment measures the real values.

**Verdict rule:**
- **Any kill → C-09 stops S5 work.** Its remaining conversations move to C-11 and C-19, which share its product core and buyer (P-24, applied). *(Note, 2026-09-22: C-11 was eliminated under D-22, §7.4, so in practice this now means C-19. The frozen lines are unchanged.)* C-09 keeps its fact sheet and stays an S6 backup. The kill and its evidence are recorded in `6_decision.md` §5 and `6_focused_target.md` §1.4.
- **Any conditional and no kill → C-09 continues**, but S6 cannot confirm it as primary until the named condition is met by the price test or a second assessment.
- **All pass → C-09 goes to the 1-10 re-score** with the measured inputs replacing the desk ranges in §4.4.4 of the focused-target file.

**Who decides:** the founders, together, on the evidence in `5_log.md` §7. ~~**The lines above are frozen as of 2026-09-22.**~~ **Superseded 2026-10-09 (C29, §2.5.12).** Moving them after a measurement needs a `submarket_selection.md` §9 entry with the reason.

**What the interviews must add for the test to run** (already in the kit and `6_focused_target.md` §7.3): freight spend by mode, the share of bills through brokers, the count on the minimum charge, the reweigh share, and whether offshore handling of invoices is acceptable.

### 2.5 Re-run on the software basis (D-23) · ~~**proposed 2026-10-08, not adopted**~~ **proposed 2026-10-08, adopted 2026-10-09 (C29)**

> **What this is.** C-09's per-customer model and kill condition, re-run for a software company: the software flags the bills, and the **customer's own staff** review the flags and file the disputes (D-23, `software-initial-pitch.md` §1A). Briefed in `handoff_c09_software_rerun.md`.
> **Status: ~~a proposal for the founders.~~ adopted by the founders on 2026-10-09 (C29, §2.5.12).** ~~§2.4's lines stay frozen and in force until the founders adopt new ones.~~ On adoption, §2.4 is struck through and a `submarket_selection.md` §9 entry is made (~~C28~~ C29): *done 2026-10-09.* ~~**No look-back starts before then.**~~ Look-backs may now start; the data-handling rules (D-18) are still needed before real data arrives. Nothing here sets a price or picks a fee form (Q6), re-scores a card, or puts our own analysts or any manual review into a model.
> **The founders' answers, 2026-10-08 (§2.5.10):** a subscription (C28), the customer's hours as capacity, the look-back design, and Test 1 on flagged dollars are decided. P-31 is deferred. ~~The acquisition cost is open for discussion~~ ~~The acquisition cost is deferred until the first customer is won and timed~~ The acquisition cost is set as bounds, $0 to $10,000, until the first customer is won and timed, and Test 1's lines are re-modelled at both (§2.5.11). ~~**The lines are not adopted.**~~ **Adopted 2026-10-09 (C29, §2.5.12):** "Adopt the Kill/Cover/Pass lines".
>
> **New evidence:** three checks, each followed by an adversarial review that fetched every source again:
> - **AQ, the customer's side:** `research/s5_check_AQ_c09_customer_review.md` and `research/s5_check_AQ_adversarial.md`;
> - **AR, our cost:** `research/s5_check_AR_c09_software_cost.md` and `research/s5_check_AR_adversarial.md`;
> - **AS, the market's prices and models:** `research/s5_check_AS_c09_market_models.md` and `research/s5_check_AS_adversarial.md`.
>
> **Arithmetic:** a model script kept in the session scratchpad, not in the project. It first reproduces §2.3's service-basis break-even ($1.36M against the recorded $1.35M, a rounding difference), then runs the chain below. Every figure marked **[our calc]** comes from it.

#### 2.5.1 What changed, in plain words

- **Before (§2.1-§2.4):** we read the bills, **our analysts** reviewed the flagged ones and filed the disputes, and we kept 25% of what came back. Our biggest cost was people: $1.02 of the $1.12 it cost us per bill.
- **Now (D-23):** the software reads every bill and flags the ones that look wrong. **The customer's own staff** look at each flag, accept or reject it, and file the disputes with the carrier. We employ no analysts.
- **So our cost falls to software:** reading, storage, hosting, support and any licence. At a $2M customer that is about **$0.18 a bill** all in, against $1.12 before **[our calc]**.
- **Two questions now decide the card:**
  1. Will the customer's staff work the flags? (*follow-through*, A09-15)
  2. Do the dollars they recover pay back what it cost us to win them as a customer within 12 months, at a share of those dollars a customer would hand over?

#### 2.5.2 The chain

**Recovered dollars a year, for the customer** = TL+LTL spend × flagged rate × follow-through × share credited.
- **Flagged rate:** the dollars on bills the software flags **and** the customer's reviewer accepts as billed wrong and provable from the documents, as a share of spend. It includes errors caught **before payment** (prevented, not refunded). This is what Test 1 measures. **It already contains the software's catch**, so the old "share caught" (70%) is no longer a separate link (§2.5.8, the definition question).
- **Follow-through:** the share of those flagged dollars that the staff actually dispute (or get corrected before payment). Dollar-weighted: a $3 fuel rounding nobody chases counts for less than a $70 reweigh.
- **Share credited:** the share the carrier credits or corrects. A correction before payment still needs the carrier to reissue the bill (nine of ten LTL rules tariffs bar short-paying; `C09-open-questions-evidence.md` §7), so the same share applies to errors prevented. Duplicates are the exception: they are simply not paid.

**Our revenue, two forms side by side** (no price is set; Q6):
- **(a) a share** of the recovered dollars;
- **(b) a subscription**, a fixed sum a month.

To compare them on one yardstick, the model uses a **value share**: what the customer hands over, as a share of what it recovers, whatever the form. Under (a) it is the share itself. Under (b) it is the subscription divided by the customer's recoveries. Central **25%** **[our call]**, the middle of what the market shows (§2.5.3). **The line in §2.5.8 is stated on this yardstick, so neither fee form chooses it.**

**Our cost per customer** = bills × (reading + storage) + hosting + support + any licence. The first year adds our onboarding help. **Reported separately:** platform costs (SOC 2) and the cost of winning the customer (customer acquisition cost, CAC).

**The customer's hours a month** = flags (false ones included) × minutes per flag + disputes × minutes per dispute, plus minutes to confirm the rules read from each agreement in the first year. **Treated as capacity, not dollars** **[our call]**, with the loaded wage shown only as a sensitivity. The reason: C24 counts labour as money only where it turns into cash, and these hours are the customer's cost of using the tool, not a saving we sell. **They enter only Test 3.**

**The bar: S4.5's 12-month payback** (`submarket_selection.md` §4 S4.5, as C27 used it). Gross profit in year one must at least equal the CAC. So the year-one revenue we need from one customer = CAC + our year-one cost. **This re-run uses that bar; it is not C-09's S4.5**, which has not been run.

#### 2.5.3 Inputs

| Input | Central | Range | Label | Source |
|---|---|---|---|---|
| **Customer's TL+LTL spend** (reference size) | **$1.5M** | $0.27-5M (table by size) | payments *verified*; annualised **[our calc]** | Three real segment firms bought $1.5-1.9M a year (bankruptcy payment lists; evidence file §6 A09-09). Check X's bands: $0.27M (manufacturers, 20-99 staff), $0.63M, $1.59M (manufacturers, 100-499), $2.90M (wholesalers, 100-499). The kit screens for $1.5M+ |
| Bills per $1,000 of spend | 1.5 | 1.5-2.21 | **[our calc]** | LTL carriers' own 2025 averages 1.88-2.03; the ABF account 2.21 (evidence file §6 A09-05). Drives our reading cost and the customer's flag count |
| **Flagged rate** (flagged, accepted, provable, in-window, plus prevented) | **1.05%** | 0.21-2.1% | **[our call]** | The old central 1.5% true overcharges × the old 70% catch. Neighbours: government pre-payment auditors flagged 1.66% (four firms) to 3.37% (all five; one firm is 79% of it), self-reported (*verified* as reported, evidence file §4); USDA 1977 co-operatives collected 0.45% (*verified*); vendors' six cases 0.8-4.2% (*assumed*) |
| **Follow-through** (A09-15) | **60%** | 30-100% | **[our call]**; **not measured anywhere** | Check AQ §AQ2: exceptions that block payment get worked, in about 4 days (APQC, *assumed*); small ones are let through. "Many shippers use a percentage or dollar threshold under which they won't dispute"; complaints "abandoned because they didn't have the resources" (ocean, 2017, *verified* as reported). Freightview's example tolerance auto-accepts bills up to 3% (LTL) or $50 (TL) over (*verified*). Retail suppliers write off deductions under a median $10-25 (CRF, *verified*, an analogue) |
| Share credited or corrected | 75% | 60-90% | **[our call]** | Check AB §4: 60-90% when prompt (*assumed*). Under a monthly cycle almost every bill is inside the 180-day window (evidence file §5) |
| **Value share** | **25%** | 9-50% | **[our call]** | Check AS: software that acts itself takes 9-35% (Lojistic's ladder 9-29%, *verified*; cloud tools 23-35%, *assumed*; chargeback tools 20-25%, *assumed*); audit firms that do all the work 23.23% / 38.61% (CT Logistics' federal list, *verified*); parcel-first firms and small shippers 50% (*assumed*). No software was found where the customer files and the vendor takes a share (§2.5.5) |
| Machine reading per bill | $0.10 | $0.005-0.50 | prices *verified*; **[our calc]** | check AA §9.1; check AJ §9 |
| Storage per bill, kept 7 years | $0.002 | — | *verified* price, **[our calc]** | check AA |
| Hosting, per customer a year | $60 | $36-184 | list prices *verified*; stack **[our call]** | check AR §AR1.3 and its review: a lean build with monitoring costs $3.6-6.0k a year, $36-60 a customer at 100; the median small software company spends about $184 a customer at 100 (SaaS Capital, *verified*) |
| Support, per customer a year | $175 | $60-291 | ticket cost *verified*; tickets a year **[our call]** | check AR §AR1.5: an email ticket $19.96-24.24 (MetricNet, IT desks); 3-12 tickets a year |
| Our onboarding help, first year | $400 | $185 (self-serve) - $616 (assisted) | **[our calc]** | check AR §AR1.5: 2-6 hours at $92-103 an hour. Help using the software, not checking the customer's rates for them (D-23) |
| Per-customer licence | $0 | up to $8,764 a year | **[our call]**; FEMA's price *verified* | check AR §AR3: an agency paid SMC3 $8,764 a year for CzarLite and RateWare web access (2019-21). Whether a SaaS needs one per customer is **unknown**; $0 means auditing against the customer's own agreement and the carriers' rate tools first (check AL) |
| SOC 2, company level | $16.5-68k a year | year one $29.5-58k | platform list prices *verified*; audit fees *assumed* | check AR §AR2. Reported separately, not per customer |
| **Cost of winning a customer (CAC)** | **$10,000** | $5-15k | *assumed* (benchmark) | S4.5's bar (check A §A3: inside sales $5-15k). Check AR §AR4.3 and its review: survey medians put CAC payback at 8 months for $1-5k a year and 14 months for $5-10k (Benchmarkit 2025, self-reported, *verified*), but the same report's cost ratio ($1.60-2.00 of sales and marketing per $1 of new revenue) implies about 25-31 months; one real SMB vertical firm, Weave, pays back in about 27-38 months **[our calc]** |
| Share of bills flagged (false flags included) | 15% | 5-58% | **[our call]** | Ardent: 14-18.4% of AP invoices are exceptions (*verified*); the ABF practice account 58% (check AK §6.3) |
| Minutes per flag | 10 | 6-15 | **[our call]** | check AQ §AQ1.3 and its review: the Australian Tax Office's calculator puts a processing exception at 15 minutes (*verified*, 2016 estimates); APQC × Ardent gives 7-14 minutes, but of **supplier-facing** time per AP problem, not review time **[our calc]** on *assumed* inputs; the old model's 6. No source times a pre-explained freight flag |
| Disputes, share of bills; minutes each | 5%; 30 | 15-60 minutes | *assumed*; **[our call]** | check AQ: ~52 minutes per retail deduction (CRF analogue), 60-150 per ocean dispute; LTL carriers offer batch tools (Estes, 20 at a time; check AK §5.2) |
| Agreements to confirm, first year; minutes each | 8; 60 | 6-9 carriers | **[our call]** | 6-9 carriers make 80% of a shipper's dollars (evidence file §6 A09-08). A strong table reader gets every cell right in only 69% of complex tables (PubTables-1M, *verified*; check AR §AR5.2), so the confirmation step is needed |
| **The customer's capacity** (A09-16) | **20 hours a month** | — | **[our call]** | About an hour a working day. Vendor-reported workloads run from 5 hours a week for 200 bills to 15-20 hours a week (check AQ §AQ2.3, *assumed*); no neutral figure |
| Loaded wage of the customer's staff | $36.79 an hour | — | *verified* (BLS ÷ 0.70) | check AA. **A sensitivity only** |

#### 2.5.4 Worked example: a $2M customer [our calc]

1. **Bills:** $2M × 1.5 per $1,000 = **3,000 a year**, 250 a month.
2. **Flagged and accepted:** 1.05% × $2M = **$21,000**.
3. **Worked and filed:** × 60% follow-through = $12,600.
4. **Credited:** × 75% = **$9,450 recovered a year.**
5. **Our cost:** reading 3,000 × $0.10 = $300, storage $6, hosting $60, support $175: **$541 a year**. The first year adds $400 of onboarding help: **$941**.
6. **What we need in year one to repay a $10,000 CAC within 12 months:** $10,000 + $941 = **$10,941**.
7. **Form (a), a share:** $10,941 ÷ $9,450 = **116% of what the customer recovers**. No share can do it. At a 25% share our revenue is $2,362 a year and our gross profit $1,821 (year one $1,421), so the CAC and the onboarding help pay back in about **69 months**.
8. **Form (b), a subscription:** $10,941 ÷ 12 = **$912 a month**. The customer would pay $10,941 to recover $9,450. For scale (check AS): booking tools with an audit screen publish $0-253 a month for their small tiers (MyCarrier, Kuebix, Freightview's 0-50-shipment tier); a $2M shipper's 250 bills a month fall in Freightview's "Call now" tier. One freight-audit listing publishes $2,500 a month per unit, with units scaling by volume (AuditRes, no ratings).
9. **The customer's hours:** 450 flags × 10 minutes = 75 hours; 150 disputes × 30 minutes = 75 hours; 8 agreements × 60 minutes = 8 hours in the first year. About **12.5 hours a month**, inside the 20-hour capacity. At the practice audit's 58% of bills flagged it is about 30 hours; on an LTL-heavy account (2.21 bills per $1,000) at 58%, about 45.
10. **Sensitivity, the hours as dollars:** 158 hours × $36.79 = **$5,813**, 62% of what the customer recovers.

**Reading [our call]:** at the central rate, **the customer's whole recovery does not repay a $10,000 CAC within a year, whatever the fee form.** Our cost to serve is no longer the obstacle. The cost of winning the customer, set against the dollars one customer recovers, is.

#### 2.5.5 The two fee forms side by side [our calc]

| | **(a) A share of recoveries** | **(b) A subscription** |
|---|---|---|
| Smallest level that repays a $10k CAC in 12 months, central rate (1.05%) | $1.5M: 153% · $2M: 116% · $3M: 78% · **$5M: 48%** of recoveries | **$905-950 a month** at every size from $1.5M to $5M; the customer recovers $7,088-23,625 a year |
| Same at the government auditors' highest flagged rate (3.37%) | $1.5M: 48% · $2M: 36% · **$3M: 24%** · $5M: 15% | unchanged; the customer recovers 2.1-6.7× it |
| Our break-even (running cost, no CAC) | spend of **$0.23M** at a 25% share | a subscription of **$23-83 a month** (our running cost ÷ 12, at $0.27-5M) |
| Our revenue depends on | the rate, follow-through and credits | none of the customer's results; it depends on renewal (churn of 10-20% of revenue a year at $1-10k a year, check AR §AR4.2) |
| What we must see to bill | each credit or corrected bill. **Check AS found almost no software where the customer files and the vendor takes a share.** The two partial exceptions: a parcel-audit firm whose customers request refunds themselves, which charges "a nominal contingency fee based on the recoverable refunds", and an R&D tax-credit service that charged 15% of credits it had identified while the business files its own return (both *verified* by the review). Where vendors state how they confirm a recovery, they read the counterparty's own record (the provider's bill, the next invoice, the remittance) or file themselves. Our software ingests every bill, including corrected and balance-due bills, so it sees part of that record **[our call]**. Fee feasibility F2-F3 (`submarket_selection.md` §5.4) | nothing |
| Budget line | none needed: said only by contingency sellers (check AQ §AQ4.3) | needed. The segment's smallest tool tiers sell on free trials and card billing (Freightview's 0-50-shipment tier); at a $2M shipper's volume, pricing is by quote (check AQ §AQ4.2 and its review) |
| What buyers have accepted | Miami-Dade County's 2026 telecom contract pays at least $24,700 a month plus 20% of 12 months of realized savings, but **"No performance-based or contingency fee shall apply to credits, refunds, or corrections resulting from billing discrepancies"**, because the county "already pays fixed or recurring fees" for that work. Ingham County, Michigan (2009) paid a $4,000 monthly fee **plus 50%** of recoveries (check AS §AS2.4 and its review, *verified*) | published monthly prices above |
| The fee rule (`CLAUDE.md`: "our fee can be a share of it") | meets it as written | ~~**the founders' question** (§2.5.10)~~ **meets it: the founders chose a subscription on 2026-10-08** (§2.5.10; C28) |

**Under the common 25% value share, the size thresholds in §2.5.6 are the same for both forms.** What differs is who carries the risk and whether we can count the money. Under (a) we carry the rate, follow-through and credit risk, and we must see the credits. Under (b) the customer carries them, and we carry renewal.

#### 2.5.6 The four numbers, adapted for software (proposed as P-31) [our calc]

1. **Break-even size** (our running cost covered, no CAC): **$0.23M** of spend at the central chain and a 25% value share, for either form. With every unmeasured input at its best: $0.02M. *On the service basis it was $1.35M.*
2. **Self-serve against assisted onboarding** (this replaces "the cheapest allowed review labour", which no longer exists):
   - $185 against $616 of our help in the first year (check AR);
   - payback at $2M: **67 against 70 months**; the line at $1.5M: 6.31% against 6.57%.
   - **Reading:** what onboarding costs us hardly moves the answer. Whether customers finish it unaided (A09-17) matters more, and nothing on the web measures that for loading contracts (check AR §AR5.1).
3. **One condition at a reference size, with a table by size.** The flagged rate at which the recovered dollars repay a $10,000 CAC within 12 months at a 25% value share: **6.44% at $1.5M**. The customer's hours must also fit its capacity (Test 3). Table:

   | Customer's TL+LTL spend | **Kill line** (every unmeasured input at its best) | Rate from which the middle band's condition can be met | **Pass line** (central; CAC $10k) | Pass with CAC $5k | Pass with CAC $15k | Pass with 100% follow-through | Pass counting a one-off in-window look-back in year one |
   |---|---|---|---|---|---|---|---|
   | $0.27M | 4.35% | 10.5% | 35.2% | 18.7% | 51.6% | 21.1% | 23.6% |
   | $0.5M | 2.35% | 5.71% | 19.0% | 10.2% | 27.9% | 11.4% | 12.8% |
   | $1M | 1.18% | 2.88% | 9.59% | 5.14% | 14.0% | 5.75% | 6.44% |
   | **$1.5M** | **0.78%** | **1.93%** | **6.44%** | 3.48% | 9.40% | 3.86% | 4.32% |
   | $2M | 0.59% | 1.46% | 4.86% | 2.64% | 7.08% | 2.92% | 3.26% |
   | $3M | 0.39% | 0.99% | 3.29% | 1.81% | 4.77% | 1.97% | 2.21% |
   | $5M | 0.24% | 0.61% | 2.03% | 1.14% | 2.92% | 1.22% | 1.36% |

   Between rows, interpolate in a straight line. The last four columns show how far the unmeasured inputs move the pass line. **Spend at which the central chain meets the 12-month bar: about $10.3M** ($5.5M at a $5k CAC, $15.2M at $15k), which is where audit-and-pay providers' own floors begin ($10M+, check Y).
4. **Spend at which our revenue reaches $5k a year** (check A's direct-selling line), either form at a 25% value share: **$4.23M** at the central rate, **$2.68M** at 1.66%, **$1.32M** at 3.37%.

**Payback at the central chain (CAC $10k plus onboarding help, 25% value share), in months:** $1M 157 · $1.5M 95 · $2M 69 · $3M 44 · $5M 25. At 3.37%: 37 · 24 · 18 · 12 · 7.

#### 2.5.7 The ceiling test (C23) and the revenue test

**Ceiling test.** Every unmeasured input at its most favourable value:
- the flagged rate at 3.37%, the highest non-vendor figure (all five government pre-payment auditors, self-reported);
- follow-through 100%;
- 90% credited;
- a 50% value share;
- a $5,000 CAC;
- the low cost case.

**C-09 passes from about $0.35M of spend upward** and fails below it. At the four smaller government auditors' 1.66%, it passes from about $0.71M. So, under C23, **C-09 is not eliminated: it stays alive on unknowns** (the rate, follow-through, and the cost of winning a customer). The typical 20-99-staff manufacturer (about $0.27M) fails even here.

**Revenue test** (beside the model, not a step-7 number; `4_kill_conditions.md` §3.5 and §4.4 method) at the central chain and a 25% value share:
- a $1.59M customer pays about **$1,880 a year**: $1M needs about **530 customers** and $2.5M about **1,330**, which is 2.6% and 6.6% of the ~20,000 manufacturers and wholesalers with 100-499 staff (check X §7.4);
- a $2.90M customer pays about **$3,430**: $1M needs about 290 and $2.5M about 730, which is 3.8% and 9.5% of the 7,687 wholesalers with 100-499 staff.
- **Reading [our call]:** the counts sit inside check A's 10% conservative share, but **each of those customers takes about 4-7 years to repay a $10k CAC** (3.8 years at $2.90M, 7.4 at $1.59M), while 10-20% of revenue churns away each year (check AR). The revenue would come at a loss on acquisition, as C-11's did on cost.

#### 2.5.8 The kill condition, re-derived [our call] · ~~**proposed, not adopted**~~ **adopted 2026-10-09 (C29)**, with Test 1's row from §2.5.11

**Measured in:**
- **the first C-09 look-back** on one shipper's in-window bills, with every agreement version, fuel tables, BOLs (bills of lading) and PODs (proofs of delivery), under a mutual NDA, at least three months of bills;
- **then a pilot of at least one full billing cycle** for follow-through (Test 1's middle band only).

The design is suggested below.

**Definitions [our call]:**
- **In-window spend:** as §2.4. Bills still contestable on the day: 180 days from receipt (49 U.S.C. 13710), the contract's own window if longer, and the broker's terms for broker-billed freight.
- **Measured flagged rate (Test 1):** the dollars on bills that the software flags **and** the shipper's reviewer accepts as billed wrong and provable from the documents held, on in-window bills, **including bills not yet paid** (errors prevented), divided by in-window spend.
  - Flags the reviewer rejects count in Test 3, not here.
  - Corrections the documents show to be legitimate are excluded.
  - Dollars flagged but unprovable are recorded separately and not counted.
- **The definition question (`C09-open-questions-evidence.md` §11 item 6), settled for these lines:** Test 1 measures **what the software flags** and the reviewer accepts. It does not measure the true overcharge rate. *Founders, 2026-10-08: "Flagged" (§2.5.10).*
  - The lines below are derived on flagged dollars, so the 70% catch share sits inside the measurement and is **not applied again anywhere**.
  - The true rate is neither needed nor measured.
- **The line applies at the shipper's own spend:** its in-window TL+LTL spend, annualised, read from the table in §2.5.6 and interpolated, as C27 does for C-19.
- **The 75% credited share** is used until 5-10 of the pilot's disputes are decided. The measured share then replaces it (as §4.7 does for C-19).

> *2026-10-08: the founders set the acquisition cost as bounds, $0 to $10,000. Test 1's lines are re-proposed in §2.5.11, which replaces the Test 1 row below if adopted.* *2026-10-09: adopted (C29, §2.5.12), so §2.5.11's Test 1 row replaces the one below, which is struck through.*

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Measured flagged rate on in-window spend | ~~**under the kill line at the shipper's size** (0.78% at $1.5M)~~ | ~~Between the lines. **Continues only if a pilot of at least one billing cycle shows enough follow-through.** The measured follow-through must reach the level at which, at the measured rate and credited share, the recovered dollars repay a $10,000 CAC within 12 months at a 25% value share. Or it must reach the higher value share the S5 price test shows a shipper accepting, never above 50%. *(At $1.5M this cannot be met below 1.93%, even at 100% follow-through.)*~~ | ~~**at or above the pass line at the shipper's size** (6.44% at $1.5M)~~ |
| **2. Access** | The rate agreements and paid invoices, uploaded under a mutual NDA | **2 of the first 3 paying-side interviewees decline** | 1 of 3 declines. **Or a decline names only a security certificate or questionnaire** (SOC 2): the condition is that the founders accept SOC 2's company-level cost at S6 | all 3 agree, or 1 declines and a replacement agrees |
| **3. The customer's hours, measured** | From the timed look-back: minutes per flag (all flags), flags per bill, the share of flags the reviewer accepts as real, and minutes to confirm the rules per agreement. Disputes at 5% of bills × 30 minutes unless timed. **The result:** the customer's hours a month at its own volume, against its capacity (the hours it said it could give, asked before the timed session; 20 if it gives no figure). **Also:** our machine-reading cost per bill | **over twice its capacity, even counting only the flags the reviewer accepted** | Over capacity as measured, but within it once the rejected flags are removed: continues only if the pilot shows that tolerances and grouping bring it within capacity. **Or** our reading cost is above $0.50 a bill (check AA's high case): continues only if the pilot finds a cheaper reading route | **within capacity as measured, and our reading cost at or under $0.50 a bill** |

**Why these lines [our call]:**
- **The kill line (0.78% at $1.5M)** is the rate below which **no customer of that size can repay even a $5,000 CAC within 12 months**, with every unmeasured input at its best: full follow-through, 90% credited, the customer handing over half of everything it recovers, and our low costs. That is C23's ceiling test, applied to the shipper measured. It lands near the old frozen 0.75% by coincidence. The old line came from mature-programme rates and offshore labour.
- **The pass line (6.44% at $1.5M)** is the rate at which the central chain repays a $10,000 CAC within 12 months: 60% follow-through, 75% credited, a 25% value share. That is S4.5's bar, as C27 applied it to C-19.
  - **It is above every figure on file.** Government pre-payment auditors flagged 1.66-3.37% (self-reported); the vendors' six cases ran 0.8-4.2%.
  - **So a pass would be a genuine surprise**, and a first look-back will most likely land in the middle band.
- **Why it sits so far above the old 1.3%:**
  - the old pass line asked only that our fee cover **our review labour**, with payback reported beside it ("a rate near 3% or spend above about $5M", §2.3);
  - this line includes the payback, as the handoff and C27 require;
  - and the old chain's 1.5% was true overcharges, about 1.05% flagged.
- **The middle band's condition is follow-through,** because one watched look-back cannot measure it: it reads 100% while someone watches, and credits take months. Only a pilot of at least one billing cycle can settle it (A09-15).
  - **The 50% cap** is the highest share documented for small shippers.
  - **The "can be met from" column** shows where the condition becomes reachable at all.
- **Test 2 stands as in §2.4.** Without the agreement, the software can check only arithmetic, and the practice audit found the arithmetic right on 101 of 101 bills.
  - **Carrier confidentiality clauses can make a "no" contractual, not reluctance.** TForce's Item 130 holds pricing agreements "in strict confidence by all parties, including the agents of the customer", and expects the shipper to tell its auditor. FedEx Freight's Item 250 allows disclosure only when "required by law" (evidence file §7 A09-11). The NDA and our terms should be written to meet such clauses.
  - **No evidence shows mid-sized shippers demanding SOC 2 before uploading** (check AQ §AQ5). Only FreightPOP states SOC 2 Type II, and Freightview's terms make the *user* warrant that an upload is "not confidential". So a security-only "no" is treated as a cost question, not a refusal.
- **Test 3 is where the customer's staff now decide the card.** A queue the customer cannot staff is let through or abandoned (check AQ §AQ2).
  - **Why twice capacity:** above it, even a perfectly tuned queue is too big.
  - **Why the 20-hour default:** it is about an hour a working day, in the range of the only workloads reported (vendor figures).
  - **What stays at desk values:** support and platform costs. One look-back can't measure them.
- **No double counting.** Test 1's lines use no hours, and the customer's hours enter only Test 3.
- **Neither fee form chooses the line.** It is stated in recovered dollars at a value share, and either form can be priced at that share (§2.5.5).

**Verdict rule** (as §2.4):
- **Any kill → C-09 stops S5 work.** Its conversations move to C-19. C-09 keeps its fact sheet and stays an S6 backup, and the kill is recorded in `6_decision.md` §5 and `6_focused_target.md` §1.4.
- **Any conditional and no kill → C-09 continues**, but S6 cannot confirm it as primary until the named condition is met.
- **All pass → C-09 goes to the 1-10 re-score**, with the measured inputs.

**Who decides:** the founders, together, on the evidence in `5_log.md` §7. ~~**Proposed 2026-10-08, not adopted.**~~ **Adopted 2026-10-09 (C29, §2.5.12).** On adoption:
- §2.4's lines are struck through, never deleted, with a `submarket_selection.md` §9 entry (~~C28~~ C29); *done 2026-10-09*;
- P-31 gets its own entry if it changes the template. *P-31 stays deferred, so no entry.*

~~**Suggested look-back design [our call], for the founders to adopt or not:**~~ **Look-back design, adopted by the founders 2026-10-08** ("The suggested design sounds good."):
1. **Capacity first.** Ask, and record before anything is timed, how many hours a month the shipper can give the queue (A09-16).
2. **Run the software's rules as scripts** on the shipper's in-window bills and agreements. The raw files stay outside the project folder (D-18).
3. **The shipper's own reviewer confirms the rules** read from each agreement. Record the minutes, and the corrections needed (A09-17).
4. **The shipper's own reviewer works every flag on screen while we time them:** accept as real, or reject. **No one on our side judges a bill** (D-23). This mirrors the product.
5. **Then the pilot.** For at least one billing cycle, the software flags new bills as they arrive. The shipper's dispute log against those flags gives follow-through, and credits are recorded as they arrive.

~~`5_interview_kit.md` §6.1 is rewritten only after the founders adopt this design.~~ Adopted 2026-10-08, and `5_interview_kit.md` §6.1 is rewritten to match. The founders plan the look-back free of charge, on a locally hosted demo or a cheap cloud host.

**What the interviews must add** (on top of §2.4's list):
- the hours a month the shipper can give the queue;
- whether a booking tool's audit screen is in use, and what tolerance is set;
- who files disputes, and through which channel (the large truckload carriers and brokers searched publish no self-serve dispute channel; one truckload shipper app has an in-app button for carrier-added accessorials; check AQ §AQ3.2 and its review);
- who approves a software subscription, and up to what amount.

#### 2.5.9 Desk verdict [our call]

- **Alive on unknowns.** C-09 passes the ceiling test from about $0.35M of spend.
- **D-23 removes the cost problem.** Our running cost falls from about $1.12 a bill plus $400 a year to about $0.10 a bill plus $235 a year. Break-even before acquisition cost falls from $1.35M of spend to about $0.23M.
- **It exposes an acquisition problem.** At the central rate, whatever the fee form, a customer cannot repay a $10k CAC within 12 months below about $10.3M of spend. At a $5k CAC the threshold is about $5.5M, and at $15k about $15.2M. Three unmeasured things could change that:
  - a much higher measured rate than any neutral figure;
  - larger customers, though audit-and-pay providers already start at about $10M;
  - a much cheaper way to win customers. Check A's rule: below about $5k a year per customer, direct selling stops paying, and a named channel is needed (inbound or search, a TMS or marketplace integration, a partner).

  Which of these to pursue is S6's and Q6's question, not this step's.
- **The customer's hours fit at central inputs** (about 12.5 hours a month at $2M), but not at the practice audit's 58% flag rate (30-45 hours). **The design's levers now protect follow-through, not our margin:** auto-clearing within tolerances, grouping by cause, and the highlighted screen.

#### 2.5.10 Open questions for the founders (answered 2026-10-08: 1-4 decided, 5 deferred, 6 set as bounds in §2.5.11)

| # | Question | Facts for it | Suggested **[our call]** |
|---|---|---|---|
| 1 | **Does a subscription meet the fee rule?** `CLAUDE.md`: "our fee can be a share of it" | `submarket_selection.md` §5.4 already names "a platform fee plus a success bonus" as a hybrid when F1-F4 fall to 2-2.5. C24 counts labour as money only where it turns into cash. Check AS: where the customer files, the market prices by subscription; no share-of-savings software where the customer files was found; one public buyer refused a share on billing-error credits. Under a share we must see each credit (F2-F3) | Yours. Any change needs a §9 entry |
| 2 | **The customer's hours: capacity or dollars?** | As capacity they are Test 3's limit. As dollars, the central $2M customer's 158 hours are worth $5,813, 62% of what it recovers | Capacity, with the wage as a sensitivity |
| 3 | **The look-back design** (§2.5.8) | One watched look-back can't measure follow-through; credits take months | The shipper's reviewer works the flags while timed, then a pilot of at least one billing cycle |
| 4 | **The definition question** (§11 item 6) | The old lines mixed a true-rate model with a flagged-rate measure | Test 1 measures what the software flags and the reviewer accepts; the lines are derived on that |
| 5 | **P-31** (the template, below) | §1's steps 2-3 assume our own review labour | Adopt for cards where the customer does the review |
| 6 | **The acquisition cost the line assumes** | The pass line at $1.5M is 3.48% / 6.44% / 9.40% at a $5k / $10k / $15k CAC. S4.5's bar uses $5-15k (inside sales). A self-serve or partner channel would cost less, but none is evidenced for this segment | Keep $10k (as C27) until a channel is evidenced |

**The founders' answers (2026-10-08), in decision-record format:**

| # | Initial decision (founders, verbatim) | For and against | Status |
|---|---|---|---|
| 1 | "A Subscription. We market it as a scoop off the top of the money they will make, but it will not be contingent on them actually making money." | **For:** where the customer files, the market prices by subscription (check AS), and we no longer need to see each credit to bill (F2-F3). 25% of a $2M shipper's central recoveries is about $197 a month, comparable to the $0-253 a month the segment's small tiers publish (a $2M shipper's volume is priced by quote) **[our calc]**. **Note [our call]:** the "scoop off the top" holds only where a customer recovers well above the subscription. At $1.5M, a subscription set at 25% of the central recoveries ($148 a month) is 52% of what the customer recovers at a 0.5% flagged rate, 88% at 0.3% and 131% at 0.2% **[our calc]**. That risk sits in the renewal (churn of 10-20% of revenue a year, check AR). Keeping the pitch true for each customer is a pricing question (Q6) | **Decided.** A subscription meets the fee rule (`submarket_selection.md` §5.4 and §9 C28; `CLAUDE.md`). The price stays a Q6 decision. The lines do not move: they are stated on the value share |
| 2 | "Capacity." | **For:** C24 counts labour as money only where it turns into cash, and the hours the tool adds turn into cash only through overtime or a hire. **Against:** capacity is self-reported; the pilot's follow-through is the check on it | **Decided.** As modelled in §2.5.2; no number changes |
| 3 | "The suggested design sounds good." | The timed session cannot measure follow-through, so the pilot follows it. **Time it asks of the shipper [our calc]:** three months of bills at $1.5M (about 560) at about 10 minutes a flag is about 14 hours at 15% flagged, and about 54 hours at 58% | **Decided.** The design in §2.5.8 is adopted, and `5_interview_kit.md` §6.1 is rewritten to match. No look-back starts before the lines are adopted |
| 4 | "Flagged" | A look-back cannot see what it misses, and a line on flagged dollars needs no catch share. **Guard [our call]:** the look-back runs the full set of checks the product would ship, not a sketch; a weak script reads low | **Decided.** Settles `C09-open-questions-evidence.md` §11 item 6: Test 1 measures what the software flags and the reviewer accepts (§2.5.8) |
| 5 | "Answer it later, make a note of this." | P-31 builds in answers 2 and 4 | **Deferred.** To settle before C-19's software re-run, which it would govern |
| 6 | "I dont think acquisition will cost anything, we are going to do direct outreach and meetings. Until we meet a design partner, it only costs time. Currently my time is unpaid, free look-back would occur on a locally hosted demo. Maybe it would be cloud hosted but this would be cheap. So this really is only going to be software costs, I think this will be much less than $5K. I will be doing everything, for free." Also: "Let me know if #6 doesn't make sense, this one is up for further discussion." | Below | ~~**Open, for discussion.**~~ **Deferred** (the follow-up below). The lines are not adopted until it is settled |
| 6, follow-up | "The initial customer is going to cost time, however once we have entered the space the amount of time will decrease as our network will grow. This money infusion will also allow us to hire people to handle new customer acquisition for us. Effectively, actually attributing a number to this is nebulous at best. Lets return to this sometime, we can mark how long it took to gain our first customer from beginning of outreach then we can use that number for further expansions." | **For:** no benchmark fits a founder-led start (check AR: the survey medians contradict their own cost ratios), so a figure measured on the first customer is better evidence. **Note [our call]:** one customer is one data point; founder hours and cash stay logged per channel in `5_log.md` §1, so later customers add points. **Catch [our call]:** no look-back starts before new lines are adopted, and the first customer is expected to come through a look-back, so the first look-back needs a stand-in figure, for the founders to choose | **Deferred, 2026-10-08.** Measured as the time from the first outreach to the first paying customer (`5_log.md` §1, the first-customer clock; §10.3 A-X1). P-32 is set aside with it |
| 6, bounds | "Mark these stand in figures as the upper and lower bounds, then we will adjust as we know more. THen we can model numbers around them, as we have done before." | — | **Decided, 2026-10-08:** $0 lower and $10,000 upper, adjusted as the first-customer clock and later customers report. Test 1's lines are re-modelled at both bounds in §2.5.11 (proposed) |

**Question 6: the facts for the discussion [our calc unless marked]:**
- **The lines move most at the low end.** At the 12-month bar, the central chain and a 25% value share:

  | Cash cost of winning a customer | Pass line at $1.5M | Kill line at $1.5M (every input at its best) | Spend from which the central chain passes |
  |---|---|---|---|
  | $0 | 0.51% | 0.04% | $0.62M |
  | $1,000 | 1.10% | 0.19% | $1.59M |
  | $2,500 | 1.99% | 0.41% | $3.05M |
  | $5,000 | 3.48% | 0.78% | $5.5M |
  | $10,000 (as proposed) | 6.44% | 0.78% | $10.3M |

  At $0, Test 1 kills only when there is almost nothing to find, and the card's fate moves to Test 3 and to the founders' own hours.
- **For the founders' view:** the first customers do cost little cash. There are no paid sellers, the demo runs locally, and reading costs cents a bill. S0 planned for "self-funded, with paying design partners".
- **What a $0 cost leaves out:**
  - **The founders' hours.** S0's floor of $2.5M a year needs about 1,330 customers at $1.59M of spend (about 530 for $1M), or about 730 at $2.90M, at the central chain and a 25% value share (§2.5.7). Churn of 10-20% a year means winning about 130-270 customers a year again at the $2.5M floor, with $1.59M customers.
  - **The take-home goal** (S0: at least $250k within 5-7 years). Unpaid time now is time the business is meant to pay for later.
  - **Some cash.** Panel interviews cost $145-298 each if used (check Y), and meetings may need travel.
- **Suggested [our call], proposed as P-32:** count the cash in dollars and the founders' hours as capacity, as answer 2 does for the customer's hours.

**P-32, proposed [our call], not applied** *(set aside with question 6 on 2026-10-08: the founders will time their first customer instead)*: in S4 step 7, while the founders sell unpaid:
- **the CAC in the lines is cash only:** what is spent per customer won;
- **the founders' hours are logged** per prospect and per customer won (outreach, meetings, look-back, onboarding, support), from the first outreach, in `5_log.md`;
- **the revenue test (§2.5.7) adds an hours check:** hours per customer won × the customers the S0 floor needs, plus churn replacement, must fit the founders' working hours in the 5-7 year window, or a named channel or hire must take over. From then on the CAC is cash again, and check A's $5-15k applies.

**P-31, proposed [our call]:** in S4 step 7, for a card where **the customer's own staff do the review** (software basis):
- **The chain is kept.** Our cost to serve is software only: reading, storage, hosting, support and licences. Platform costs and CAC are reported separately.
- **The customer's hours are capacity,** tested in Test 3, with the wage as a sensitivity.
- **The four numbers become:**
  1. the break-even size per fee form;
  2. the same with self-serve against assisted onboarding;
  3. one condition at a reference size, with a table by size: the leak rate at which the recovered dollars repay the CAC within 12 months at a stated value share;
  4. the size at which our revenue reaches $5k a year, per fee form.
- **Test 1's lines are stated in recovered dollars at a value share,** so that no fee form chooses them.
- **The kill line is the ceiling test** (C23) applied at the measured customer's size.

**The founders adopt P-31 or not. It is not applied to §1.** *Deferred by the founders, 2026-10-08: "Answer it later, make a note of this."*

#### 2.5.11 The acquisition cost as bounds, $0 to $10,000 (founders, 2026-10-08) · Test 1's lines re-proposed, ~~**not adopted**~~ **adopted 2026-10-09 (C29)**

**Initial decision (founders, verbatim):** "Mark these stand in figures as the upper and lower bounds, then we will adjust as we know more. THen we can model numbers around them, as we have done before."
- **Decided:** the bounds.
- ~~**Proposed [our call]:**~~ **Adopted 2026-10-09 (C29, §2.5.12):** Test 1's lines below. ~~If adopted, they~~ They replace Test 1's row in §2.5.8. Tests 2 and 3 are unchanged.

**The bounds:**
- **Lower, $0:** the first customer costs only the founders' unpaid time, and the cash is software (§2.5.10 question 6).
- **Upper, $10,000:** the middle of check A's $5-15k for inside sales, as C27 used it. It is what winning a customer costs once someone is paid to sell.
- **How they move:** the first-customer clock (`5_log.md` §1; §10.3 A-X1) and each later customer narrow them.
  - How the clock's time becomes a dollar figure is the founders' call, once it is measured.
  - The lines are then read from the table below at the new bounds, **before the next look-back**, never after the measurement they apply to (`submarket_selection.md` §10).

**Table by size [our calc].** The 12-month bar at a 25% value share, on the central chain unless marked. Interpolate in a straight line between rows and between columns.

| Customer's TL+LTL spend | **Kill line** (lower bound; every unmeasured input at its best) | Can be met from (lower bound; 100% follow-through) | Covers our first-year cost (lower bound; central) | Pass at $2,500 | Pass at $5,000 | Pass at $7,500 | **Pass line** (upper bound; central) |
|---|---|---|---|---|---|---|---|
| $0.27M | 0.234% | 1.34% | 2.23% | 10.5% | 18.7% | 26.9% | 35.2% |
| $0.5M | 0.127% | 0.76% | 1.26% | 5.71% | 10.2% | 14.6% | 19.0% |
| $1M | 0.065% | 0.42% | 0.70% | 2.92% | 5.14% | 7.37% | 9.59% |
| **$1.5M** | **0.044%** | **0.31%** | **0.51%** | 1.99% | 3.48% | 4.96% | **6.44%** |
| $2M | 0.034% | 0.25% | 0.42% | 1.53% | 2.64% | 3.75% | 4.86% |
| $3M | 0.023% | 0.19% | 0.32% | 1.06% | 1.81% | 2.55% | 3.29% |
| $5M | 0.015% | 0.15% | 0.25% | 0.69% | 1.14% | 1.58% | 2.03% |

The $5,000 and $10,000 columns match §2.5.6.

**At each bound [our calc]:**

| | Lower bound ($0) | Upper bound ($10,000) |
|---|---|---|
| Spend from which the central chain meets the 12-month bar | $0.62M | $10.3M |
| Payback, at $1.5M / $2M | 3.7 / 2.6 months | 95 / 69 months |
| Ceiling test (C23): alive from, at a 3.37% / 1.66% flagged rate | $0.02M / $0.04M | $0.68M / $1.38M |

**In subscription terms (C28), at a $1.5M shipper [our calc].**
- **The fee is a flat monthly subscription, not a cut** of what the shipper recovers.
- **The 25% "value share" is a ceiling:** the most a shipper is assumed to pay a month, as a share of what it gets back (the founders' "scoop off the top").
- **Each line asks:** at this much wrong billing, does a subscription that covers our costs stay that small a slice of what the shipper gets back?

| Line | Wrong billing found a year | Shipper gets back a month | Subscription that covers our costs, a month | Fee as a share of what the shipper gets back |
|---|---|---|---|---|
| Kill | about $660 | about $50 (every unmeasured input at its best) | about $25 (our lowest costs; $0 to win) | a half, the highest documented for small shippers |
| Covers our first-year cost | about $7,700 | about $290 | about $72 (running and setup; $0 to win) | a quarter |
| Pass | about $96,600 | about $3,620 | about $905 (also repays $10,000 spent winning the customer, within 12 months) | a quarter |

If shippers would pay up to half of what they get back, the "covers" and pass lines halve: about 0.26% and 3.2% at $1.5M.

**Test 1 with the bounds, ~~proposed [our call]~~ adopted 2026-10-09 (C29):**

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Measured flagged rate on in-window spend (definitions as §2.5.8) | **under the kill line at the shipper's size** (0.044% at $1.5M). Even a customer that costs nothing to win, with every unmeasured input at its best, cannot cover our first-year cost | Between the lines. **Continues only if a pilot of at least one billing cycle shows enough follow-through.** At the measured rate and credited share, the recovered dollars must cover our first-year cost within 12 months (the lower bound), at a 25% value share or the higher share the S5 price test shows accepted, never above 50%. *(At $1.5M this cannot be met below 0.31%; at 60% follow-through it needs 0.51%.)* **S6 cannot confirm C-09 as primary until the acquisition cost is measured** and the measured rate reaches the pass line read from the table at that cost | **at or above the pass line at the shipper's size** (6.44% at $1.5M). It repays even the upper bound within 12 months |

**Reading at $1.5M [our call]:**
- **Under 0.044%:** kill.
- **0.044-0.51%:** at central inputs, even a customer that costs nothing to win does not cover our first-year cost. C-09 continues only on the pilot's follow-through, which cannot reach the line below 0.31%.
- **0.51-6.44%:** a first customer pays for itself. Whether later customers do depends on the measured acquisition cost: read the column.
- **6.44% or more:** pass at either bound.

**What changes from §2.5.8:**
- **The kill line falls from 0.78% to 0.044%,** because the lower bound is $0 instead of $5,000.
- **Test 1 now kills only where there is almost nothing to find.** The first look-back is then decided mostly by Test 3 (the customer's hours) and by the pilot's follow-through.
- **The pass line is unchanged at 6.44%.**

#### 2.5.12 Adopted: C-09's kill condition (founders, 2026-10-09; C29)

**Initial decision (founders, verbatim):** "Adopt the Kill/Cover/Pass lines"

**What it adopts.** "Kill / Cover / Pass" is the founders' name for Test 1's three lines in §2.5.11. The open point it settles was listed as "Adopt the new lines (C29): the Kill / Cover / Pass lines and Tests 2-3" (`C09-business-proposal.md` §8.2 item 18). So the adoption covers the whole software-basis kill condition below **[our call, on the reading]**. The frozen §2.4 tests can't be applied under D-23: Test 3 there costs our own analysts' review. *If the founders meant Test 1 only, this record is narrowed.*

**The kill condition, as adopted:**
- **Measured in:** the first C-09 look-back (the design adopted 2026-10-08, §2.5.8), then a pilot of at least one billing cycle for follow-through.
- **Definitions:** as §2.5.8. In-window spend; the measured flagged rate (what the software flags **and** the shipper's reviewer accepts as billed wrong and provable, ÷ in-window spend); the line read at the shipper's own annualised TL+LTL spend, interpolated; the 75% credited share used until 5-10 of the pilot's disputes are decided. If two look-backs are available, weight by spend (§2.4).

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Measured flagged rate on in-window spend | **under the Kill line at the shipper's size** (0.044% at $1.5M) | Between the lines. **Continues only if a pilot of at least one billing cycle shows enough follow-through** for the recovered dollars to cover our first-year cost within 12 months, at a 25% value share or the higher share the S5 price test shows accepted, never above 50%. The **Cover** line is where that is met at 60% follow-through (0.51% at $1.5M); below 0.31% it can't be met at all. **S6 cannot confirm C-09 as primary until the acquisition cost is measured** and the rate reaches the pass line read at that cost (§2.5.11 columns) | **at or above the Pass line at the shipper's size** (6.44% at $1.5M): repays even a $10,000 acquisition cost within 12 months |
| **2. Access** | The rate agreements and paid invoices, uploaded under a mutual NDA | **2 of the first 3 paying-side interviewees decline** | 1 of 3 declines, or a decline names only a security certificate or questionnaire (SOC 2): the founders then weigh SOC 2's company-level cost at S6 | all 3 agree, or 1 declines and a replacement agrees |
| **3. The customer's hours** | From the timed look-back, the customer's hours a month at its own volume, against the capacity it gave before the session (20 a month if none); also our reading cost per bill | **over twice its capacity, even counting only the flags the reviewer accepted** | Over capacity as measured but within it once rejected flags are removed: continues only if the pilot shows tolerances and grouping bring it within capacity. Or our reading cost is above $0.50 a bill: continues only if the pilot finds a cheaper route | **within capacity as measured, and our reading cost at or under $0.50 a bill** |

**Test 1's lines by size** (from §2.5.11 **[our calc]**; interpolate between rows):

| Shipper's TL+LTL spend a year | **Kill** under | **Cover** from | **Pass** from |
|---|---|---|---|
| $0.27M | 0.234% | 2.23% | 35.2% |
| $0.5M | 0.127% | 1.26% | 19.0% |
| $1M | 0.065% | 0.70% | 9.59% |
| **$1.5M** | **0.044%** | **0.51%** | **6.44%** |
| $2M | 0.034% | 0.42% | 4.86% |
| $3M | 0.023% | 0.32% | 3.29% |
| $5M | 0.015% | 0.25% | 2.03% |

**Verdict rule** (as §2.5.8): any kill → C-09 stops S5 work, its conversations move to C-19, and it stays an S6 backup; any conditional and no kill → C-09 continues, but S6 cannot confirm it as primary until the named condition is met; all pass → the 1-10 re-score with the measured inputs. **Who decides:** the founders, together, on the evidence in `5_log.md` §7.

**How the lines move:** the $0-$10,000 bounds narrow as the first-customer clock reports (`5_log.md` §1). The lines are then read again from §2.5.11 **before the next look-back**, never after the measurement they apply to. Any other change goes through `submarket_selection.md` §9.

**For and against [our call], from the evidence already in §2.5:**
- **For:**
  - the lines are fixed before any look-back, so a result cannot be argued into a pass afterwards;
  - they rest on the founders' own answers of 2026-10-08 (a subscription, hours as capacity, the look-back design, Test 1 on flagged dollars, the $0-$10,000 bounds);
  - the frozen §2.4 lines can't be applied under D-23;
  - adoption lifts the block on look-backs.
- **Against, kept on the record:**
  - **the Pass line sits above every figure on file** (government auditors 1.66-3.37%, self-reported; vendor cases 0.8-4.2%), so a pass would be a surprise. The first look-back will most likely land between Cover and Pass, where the pilot, the customer's hours and the measured acquisition cost decide;
  - **at the $0 bound, Test 1 kills only when almost nothing is found.** Tests 2 and 3 and the pilot carry most of the weight;
  - **the lines assume a shipper pays up to a quarter of what it gets back.** If the price test shows up to half, Cover and Pass halve (about 0.26% and 3.2% at $1.5M). Only the conditional band uses the price test's share;
  - **one look-back is one shipper.**

**Finalized:** adopted by the founders on 2026-10-09. Logged as C29 in `submarket_selection.md` §9. §2.4's lines and §2.5.8's Test 1 row are struck through, never deleted.

**What this changes:**
- **Look-backs may now start.** Still needed first: D-18, the data-handling rules, before any real data arrives (no data-privacy lawyer has been found yet); P-25, the 1-10 scoring anchors, before any evidence; and a test price before the first close (D-15).
- **P-31 stays deferred**, so S4 step 7's template (§1) is unchanged.

---

## 3. C-11 · LTL class, reweigh and reclass disputes

**Plain words first.** An LTL (less-than-truckload) carrier can re-weigh (*reweigh*), re-measure or re-describe (*reclass*) a pallet after pickup, then send a higher bill plus a $15-55 fee (check T). The card's product finds the corrections that were wrong, proves them with the shipper's own paperwork, and disputes them. The fee is a share of what the carrier credits back.

### 3.1 The chain

**Fee per customer** = LTL shipments a year × share corrected × dollars added per correction × share wrong and provable × share credited × fee share.
**Gross profit** = fee − (shipments × machine check + corrections × review minutes + disputes × dispute minutes, at the loaded wage) − $400 fixed.

In C-09's terms, the "leak rate" is **wrong-and-provable corrections as a share of LTL spend** (shares corrected × dollars added × share wrong).

### 3.2 Inputs

| Input | Central | Range | Label | Source |
|---|---|---|---|---|
| **LTL spend of one small shipper** | **$94k a year** (median of 9 real firms) | $31k-389k | payments *verified*; annualised **[our calc]** | Bankruptcy Statements of Financial Affairs (payments in the 90 days before filing) of 9 small manufacturers and distributors, 2016-2026 (N-AD14 to N-AD22; one re-read at source 2026-09-22: Cycle Force Group paid Central Transport, Estes, ArcBest and XPO $95,835 in Jan-Apr 2021 on $14.3M of sales) |
| Same, as a share of the firm's sales | 0.7% | 0.2-4.6% | **[our calc]** | same |
| Average LTL spend per carrier customer (cross-check) | $64k | $64k-147k | inputs *verified*, **[our calc]** | FedEx Freight: 108,000 active customers, top 25 hold 21% of revenue (N-AD11) |
| Shipments per $1,000 of LTL spend | **2.7** | 2.2-3.2 | **[our calc]** on *verified* inputs | US LTL $52.8B on ~669,545 shipments a day (N-AD09); ABF court set 2.21; UPS Freight court set 2.61; Saia 2.88 |
| **Share of shipments corrected** | **15%** | 5-28% | **[our call]** | Yellow, 2006-07: 75,324 upward reweighs on "more than 1.5 million invoices" = 5.0% (DOJ complaint, W.D.N.Y. 1:08-cv-811, Doc 72 ¶73; re-read at source 2026-09-22; N-AD01, *verified* as alleged). UPS Freight bills in the Delphi bankruptcy: 48 of 169 = 28%, biased upward (N-AD07). ABF bills in the IN Holdings bankruptcy: 28 of 101 carry a reweigh note (this chat's recount, §3.3 below) |
| **Dollars added per correction** | **$72** | $15-145 | **[our calc]** on a *verified* bill | UPS Freight bill 174087550 (2008): declared 172 lb, reweighed 225 lb, class 100: +$54.07 re-rate and fuel, +$18 fee, **+41%** (N-AD07). Fees alone $15-55 (check T) |
| Corrections as a share of LTL spend, at the central inputs | **2.9%** | 0.8-5% | **[our calc]** | FedEx Freight's dimensioners: ~0.8% of revenue (N-T36, *verified*). The central case is generous against the only filed figure |
| **Share of corrections wrong and provable** | **20%** | 10-50% | **[our call]**; not measured anywhere | Carrier billing accuracy averages 97% and about half of bills of lading are wrong (SJ Consulting, *assumed*, primary not found). Shippers ODFL quotes went from ~25% re-rated to ~1% once they measured at the dock (N-AD27, *assumed*): the corrections were mostly their own errors |
| → wrong-and-provable corrections as a share of spend | **0.58%** | 0.18-1.4% | **[our calc]** | The one documented carrier-error pool: Yellow and Roadway withheld downward reweighs worth **0.18-0.54% of revenue** (N-AD01 with 10-K revenue, *verified* as alleged). The central case sits at its top |
| Share credited when disputed | **75%** | 60-90% | *assumed* | check AB §4 (prompt disputes); "70-82%" traced to a vendor's hypothetical, not a measurement (N-AD29) |
| Fee share | **30%** | 25-50% | *assumed* | S5 price test (`5_interview_kit.md` §6.2) |
| Machine check per shipment | $0.10 | — | **[our calc]** | check AA |
| Minutes to review one correction (pull the carrier's certificate, compare with the spec sheet) | **5** | 1-10 | **[our call]**; no source found | check AD §5 |
| Minutes per dispute filed | **15** | 5-45 | **[our call]**; no source found | check AA |
| Loaded wage, US / offshore | $36.79 / $12 per hour | — | *verified* BLS ÷ 0.70 / *assumed* | check AA (same as C-09) |
| Fixed cost per customer a year | $400 | $150-1,100 | *assumed* | check AA (same as C-09) |
| What the shipper can get free today | evidence capture free from a 3PL (LTLflow $0-300 a month; a $3,400 dimensioner at $0 at qualifying volume) | — | *verified* as stated | N-AD30 |

### 3.3 One more real document: the ABF bills, recounted for C-11 [our calc]

The 101 ABF Freight bills in *In re IN Holdings* (Bankr. C.D. Cal. 1:24-bk-11323, Doc 920, Exhibit 2; `research/s5_practice_audit_public_invoices.md`) were re-parsed for this step, bill by bill:

| What the bills show | Count | Money that could move |
|---|---|---|
| Bills with "Reweigh - See W&R certificate" | **28 of 101 (28%)** | — |
| …of which the carrier printed "Restore original weight" | 10 | none: the declared weight stood |
| …of which the bill sits on the $180 absolute minimum charge | 11 | none: a new weight cannot change a minimum-charge bill |
| …the rest, where a reweigh could have changed the price | **7 (7% of bills)** | at most the linehaul and fuel on bills worth $4,596, **10% of billed dollars** |
| Reweigh or inspection **fee** printed on any of the 101 bills | **0** | — |
| How the bills are rated | every bill is rated at the agreement's exception class 70 (58 bills) or at a minimum charge (43), whatever the product's NMFC class (100) | a reclass cannot move the price |

(The practice audit counted 26 reweigh notes and 9 restores. This recount keys each note to its freight-bill number and finds 28 and 10. The difference does not change the reading.)

**Reading [our call]:** on a real small-shipper account, corrections were **frequent but nearly weightless**. The pricing agreement fixed the class, minimum charges absorbed most reweighs, the carrier itself restored a third, and no fee was charged. At most 10% of the dollars were even exposed.

### 3.4 The four numbers [our calc]

Fee per $1,000 of LTL spend at the central chain = 2.7 × 15% × $72 × 20% × 75% × 30% = **$1.31**.

| Configuration | Variable cost per $1,000 | Break-even LTL spend (fixed $400) | Wrong-and-provable rate needed to cover variable cost (30% share) |
|---|---|---|---|
| **Central, US review** | $2.26 | **never** | **1.55% of spend** (2.9-8.6 times the documented 0.18-0.54% pool) |
| Central, offshore review | $0.92 | **$1.01M** (above every one of the nine real firms) | 0.37% |
| **Ceiling: every correction wrong and every dispute credited** | — | fee $8.75 per $1,000 | — |

- **LTL spend at which the fee reaches $5k a year:** **$3.8M** at the central chain; **$572k at the ceiling**. The largest of the nine real small shippers bought $389k.
- **At the median real shipper ($94k of LTL a year):** fee **$123 a year** against a cost to serve of $612 (US) or $486 (offshore). Gross profit **−$489 / −$363**. At the ceiling the same shipper pays $822, which leaves about $250 after offshore cost and never repays a $5k acquisition cost inside 12 months (about 20 years).
- **Adding extra-service charges** (the card's third kind of dispute: accessorials are 8.7-13% of LTL spend, and 3-5% of those lines are overbilled on vendor figures) raises the median shipper's fee to **$179-261 a year**. The answer does not change.

**Worked example [our calc].** Old World Timber, a reclaimed-wood maker with about $5.6M of sales, paid Estes and Saia $23,179 in the 90 days before its 2021 bankruptcy (N-AD18), so about **$94k of LTL a year**: the median. That is about 254 shipments. At 15% corrected, 38 corrections add $2,740 to its bills. If 20% of them were wrong and provable ($548) and the carriers credited 75% ($411), a 30% fee is **$123 a year**. Checking its 254 bills by machine costs $25, reviewing the 38 corrections at 5 minutes costs $117, filing 8 disputes costs $70, and the fixed cost is $400. **We would lose $489 a year on this customer at US wages**, before spending anything to win it.

### 3.5 Revenue test: $1M and $2.5M [our calc]

- **At the market level the money exists.** Small shippers buy an estimated $10.6-21.1B of LTL a year (20-40% of the $52.8B market; the shares are **[our call]** from S3b). At $1.31 per $1,000 that is a fee pool of **$14-28M**, so $1M would need 3.6-7.2% of all of it and $2.5M 9-18%.
- **But the customers who make up that pool lose money.** Every customer below about $1.0M of LTL spend loses money even with offshore review, and none of the nine real small shippers comes close. **The revenue would come with negative gross profit.**
- **In customers:** $1M at $123 a year is about **8,100 paying shippers**, and $2.5M is about **20,300**. At the ceiling's $822, 1,200 and 3,000. A fee that small can only be sold self-serve or through a partner. Check A's rule is "ARPA of about $5k or more, or a named scalable channel". The only channel in sight is the 3PLs, and they already give evidence capture away (N-AD30). A 3PL buyer would be a different paying side, and so a different card.

### 3.6 Does C-11 meet the fee rule as written?

- **The dispute half: in form, yes.** A credit is traced to a claim we filed (`4_scorecard.md` §3.1, F2 = 1). **In size, no customer inside the card's definition pays enough to cover its own cost** (§3.4).
- **The prevention half: no.** When the carrier was right, which is the usual case, declaring correctly at pickup saves only the $15-55 fee, and it **raises** the bill on every shipment the carrier would have missed (check AD §7). The market gives the tools away. A prevention product would be a subscription, not a share of a saving.

### 3.7 Desk verdict [our call] · **eliminated by the founders, 2026-09-22 (D-22, §7.4)**

**C-11 shows no viability as defined, on the desk evidence.** The finding does not rest on the unmeasured input: even if every correction were wrong and every dispute won, the median real small shipper would pay about $820 a year, and the central case loses money on every customer the card names. Under the founders' rule for this step ("absolutely eliminate any of the sub-market candidates that demonstrate no viability"), C-11 is **proposed for elimination** (§7, D-22). What would survive is the dispute logic as a **feature**: reweigh and reclass checks inside C-09's audit, which already reads the same LTL bills for larger shippers. That is S6's call, not this step's.

### 3.8 The kill condition (not adopted: C-11 was eliminated; kept for the record)

**Measured in:** the C-11 correction look-back (`5_interview_kit.md` §6.2): 90 days of one shipper's LTL invoices with original and corrected charges, the bills of lading, the carriers' certificates, and the shipper's spec sheets and packing slips.

**Definitions [our call]:**
- **Wrong-and-provable rate:** the dollars the carrier added through corrections that the shipper's own pre-pickup documents show to be wrong (the proof carriers accept, check T §3.2), divided by the shipper's LTL spend in the same 90 days. Corrections the documents show to be right are excluded.
- **Credited rate:** of the 3-5 claims filed in the look-back, the dollars credited within 60 days, divided by the dollars claimed.

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Wrong-and-provable rate on LTL spend | **under 0.4%** | 0.4% to 1.55%. Continues only if the shipper's LTL spend is over $1M and offshore review is accepted | **1.55% or more** |
| **2. Size** | The interviewee's LTL spend a year | **2 of the first 3 paying-side interviewees under $500k** | 1 of 3 under $500k | all 3 at $500k or more |
| **3. Credit** | Dollars credited ÷ dollars claimed on the look-back's claims | **under 40%** | 40-60% | 60% or more |

**Why these lines [our call]:**
- **0.4%** sits just above the offshore break-even rate (0.37%), inside the documented 0.18-0.54% carrier-error pool. Below it, no labour model covers the review.
- **1.55%** is the rate at which US-staffed review covers its own labour at a 30% share. It is roughly three to eight times the only documented carrier-error pool, so a pass would be a genuine surprise.
- **$500k** is where even the ceiling case (every correction wrong and won) first pays about $4.4k a year. Below it, no leak rate reaches check A's $5k line.
- **40%** matches the credited share of aged claims in check AB. Below it, the carriers' "sole discretion" (check T) is winning.

**Verdict rule:** any kill → C-11 stops. Any conditional and no kill → C-11 continues only as a module test inside C-09's assessments. All pass → C-11 goes to the 1-10 re-score. **Who decides:** the founders, on `5_log.md` §7.

---

## 4. C-19 · Retailer on-time-in-full fines and deductions

> **Flag, 2026-10-08 (D-23):** the founders' rule that we employ no analysts and do no manual review applies company-wide ("Yes, flag C-19 for later"; `software-initial-pitch.md` §1A). C-19's model below costs **our staff's** triage (5 minutes a deduction) and dispute (20 minutes an invalid one) at a US collector's loaded wage, so it needs the same re-run as C-09 before the two cards are compared at S6. That re-run is not briefed yet. **C-19's lines in §4.7 stay frozen and in force meanwhile.**

**Plain words first.** Big-box retailers (Walmart, Target, Home Depot, Lowe's, Costco, Kroger, Amazon buying as a retailer) take money off what they pay their suppliers. Some of it is for agreed promotions, which is *trade* and out of scope. The rest is *non-trade*: fines for late or short deliveries (OTIF, on time in full, usually 3% of the goods' cost), fines for missing or wrong advance ship notices (ASNs), and claims that goods never arrived (shortages). Some of these deductions are wrong. The product finds the wrong ones, assembles the proof (proof of delivery, carrier timestamps, ASNs) and disputes them inside each retailer's window. The fee is a share of what the retailer pays back.

### 4.1 The chain

**Fee per supplier** = sales to big-box retailers × non-trade deductions as a share of those sales × share invalid and provable × share recovered × fee share.
**Gross profit** = fee − (deductions × triage minutes + invalid deductions × dispute minutes, at the loaded wage) − fixed cost (including each retailer's portal).

The "leak rate", in C-09's terms, is **recovered invalid non-trade deductions as a share of big-box sales**. At the central inputs it is 0.5% × 10% × 60% = **0.03%**.

### 4.2 Inputs

| Input | Central | Range | Label | Source |
|---|---|---|---|---|
| **Non-trade deductions, share of big-box sales** | **0.5%** | 0.2-1.5% | central *verified* (CRF 2018 median "¼ - ½ % of sales", 203 firms; association flag); low *verified*; high *assumed* | N-N29. **Low, a real ledger:** "Shipping Variances" of $54,048.32 on $27,026,436.25 invoiced into Walmart, Sam's Club and Best Buy, 2011-15 = **0.20%** (*Miller v. ANConnect*, Bankr. D. Del. Adv. 18-50633, Doc 295, p. 250; re-read at source 2026-09-22; N-AE14). High: CRF 2021 "up to 1%" via a vendor's slides; Amazon shortages "1 to 3 percent" (agency) |
| OTIF fines alone | 0.16% of goods sold to Walmart | 0-0.9% | *assumed* (Uber Freight, via Forbes); rules **[our calc]** | N-AE51. From Walmart's rule: a supplier at 85-88% on time pays 0.36-0.45%; at or above the 90% goal, nothing (check AE §8) |
| **Share invalid and provable** | **10%** | 5-30% | central *verified* (CRF 2018: "6–10% of all deduction dollars are invalid", median; trade included) | N-N29; vendors 8-40% (N-AE22, N-AE40, *assumed*) |
| **Share recovered, of invalid deductions disputed** | **60%** | 40-90% | central *verified* (CRF 2018: "60% … are ultimately recovered"); range *assumed* (vendors) | N-N29; N-AE27, N-AE30 |
| → recovered, as a share of big-box sales | **0.03%** | 0.004-0.4% | **[our calc]** | STAT's aggregate: over $1B recovered on $500B of "analyzed supplier transactions" = 0.2% (*assumed*, N-AE30) |
| Fee share | **25%** | 15-35% | *assumed* | S5 price test (`5_interview_kit.md` §6.3); vendors 15-35% contingency (N-AE33 to N-AE37) |
| **Average non-trade deduction** | **$500** | $150-2,000 | **[our call]** | Bissell wrote off "thousands of deductions under $500"; one vendor's guarantee implies $75-225 recovered per dispute; an enterprise averages ~$2,000 (all *assumed*, N-AE28, N-AE34, N-AE31) |
| Minutes: triage every deduction / dispute an invalid one | **5 / 20** | 8-15 by hand per claim; 22 per deduction resolved (enterprise) | **[our call]** on *assumed* vendor timings | N-AE32, N-AE31 |
| Loaded wage: US collector / credit analyst / offshore | **$33.70** / $69.27 / $12 per hour | — | *verified* BLS May 2025 (43-3011 $23.59; 13-2041 $48.49) ÷ 0.70; offshore *assumed* | N-AE47; check AA |
| Fixed cost per supplier a year (2-3 retailer portals, credentials, support) | **$600** | $400-1,100 | **[our call]**; no source for portal hours | check AE §6.4 |
| **Big-box sales per supplier** | Walmart mean $13.2M per supplier record; median ~$0.6-1.8M | — | inputs *verified* (31,196 records, $412.4B); spread **[our calc]** on an assumed curve | N-U03; check AE §5.1 |
| Big-box ÷ Walmart sales, small public suppliers | **2** | 1.4-3.3 | *verified* filings (Crown Crafts, Hamilton Beach, JAKKS, Lifetime, Summer Infant); ratio **[our call]** | N-AE02 to N-AE08 |
| **What suppliers already pay for this** | SupplyPike: **≤ ~$38-50k a customer a year** | SPS's Amazon 3P base ~$2,900; ClearChain $60,000 list | SPS's stated expectation at the Aug 2024 purchase: SupplyPike to add "approximately $25.0 million" of 2025 revenue (*verified* release; **a forecast, not a result**); "more than 500" suppliers (*assumed*, press) | N-AE17, N-AE22, N-AE21, N-AE34 |

### 4.3 The four numbers [our calc]

Fee per $1M of big-box sales at the central chain = $1M × 0.5% × 10% × 60% × 25% = **$75**. At $500 a deduction that is 10 deductions to triage and 1 to dispute per $1M of sales.

| Configuration | Variable cost per $1M of sales | Break-even big-box sales (fixed $600) | Invalid share needed to cover variable cost (at 0.5% non-trade, $500 each) | Recovered share of sales that implies |
|---|---|---|---|---|
| **Central, US collector** | $39 | **$16.8M** | **4.4%** | 0.013% |
| Central, US credit analyst | $81 | never | 11.1% | 0.033% |
| Central, offshore | $14 | **$9.8M** | 1.4% | 0.004% |

- **Big-box sales at which the fee reaches $5k a year: $66.7M** at the central chain. At STAT's 0.2% recovered it is $10M; at the high setting, $4.9M.
- **Payback on winning a customer (a $10k acquisition cost), central chain:**

  | Supplier's big-box sales | Fee | Gross profit, US / offshore | Payback, US / offshore |
  |---|---|---|---|
  | $20M | $1,500 | $114 / $620 | 88 years / 16 years |
  | $66.7M | $5,002 | $1,780 / $3,469 | 5.6 / 2.9 years |
  | $100M | $7,500 | $2,968 / $5,500 | 3.4 / 1.8 years |
  | $200M | $15,000 | $6,537 / $11,600 | 18 / 10 months |

- **At STAT's 0.2% recovered**, a $20M supplier pays about $10,000 a year and leaves $6,770 of gross profit at US wages: payback in about 18 months. **The whole card turns on which world a $20-200M supplier lives in.**
- **The ratio that decides cost is the average deduction size** (check AE §9.3). At $150 a deduction, US review needs 25% of deductions invalid to cover its own labour. At $500 it needs 4.4%, and at $2,000 only 1%.

**Worked example [our calc].** A supplier sells $66.7M a year to big-box stores, about half of it to Walmart. At 0.5%, **$333,500** is deducted for non-trade reasons, about 667 deductions at $500. If 10% are invalid ($33,350) and 60% of those come back ($20,010), a 25% fee is **$5,003**. Triaging 667 deductions at 5 minutes and disputing 67 at 20 minutes takes 78 hours: $2,622 at a US collector's loaded wage. With $600 of fixed cost, **gross profit is $1,780 a year**, so a $10,000 acquisition cost takes about **5.6 years** to earn back (2.9 with offshore review). The same supplier at the rate vendors advertise (0.2% recovered) would pay about $33,000 a year.

### 4.4 Revenue test: $1M and $2.5M [our calc]

- **Suppliers big enough for a $5k fee at the central chain** (at least $66.7M of big-box sales, at most $500M of total sales): **about 600-2,000** (check AE §5.4). That is 2-7% of check U's ~29,000 buyers.
- At a typical fee of about $10k among them: **$1M needs about 100 customers (5-17% of those qualifying); $2.5M about 250 (13-42%).**
- **At STAT's 0.2%, about 5,800-9,200 suppliers qualify** and $2.5M needs 3-4% of them.
- **The only real revenue line in this market says suppliers do pay.** SPS expected SupplyPike to earn about $25M in 2025 from "more than 500" suppliers, **up to about $40-50k each**. At a 25% share that is the fee on about $160-200k of recoveries per customer. At the neutral central, those recoveries need about $530-670M of big-box sales. So SupplyPike's customers are larger than this card's, or leak far more than the survey medians, or include trade deductions (check AE §6.6, §9.4).

**Reading [our call]:**
- **$1M passes** at the central chain (5-17% of qualifying suppliers).
- **$2.5M is a stretch** (13-42%), and at US wages the qualifying customers pay back slowly.
- **At the vendors' observed rates, both pass easily.** The revenue test does not decide C-19; the measured rate does.

### 4.5 Does C-19 meet the fee rule as written?

**Yes.** A recovery is money paid back by the retailer, traced to a dispute we filed. The payer is the saver, and the fee is a share of it (`4_scorecard.md` §3.1: F1-F4 = 3.5, F5 = 1). Two cautions carried from check AE:
- **Part of the fine exposure may belong to the supplier's 3PL or carrier by contract.** The Prestige Brands-GEODIS agreement makes the warehouse liable for chargebacks above a threshold after 180 days (N-AE12, *verified*). A dispute may be chasing money the supplier could recharge.
- **Neutral recovery rates may not reach the segment's typical supplier.** That is the kill condition's job.

### 4.6 Desk verdict [our call]

**C-19 lives on an unknown.** At the neutral survey rates it is thin: $5k customers start at about $67M of big-box sales and pay back in 3-6 years. At the rates vendors report and charge for, it is strong. A real revenue line (SupplyPike's ~$25M expected in 2025, up to ~$40-50k per supplier) says suppliers pay large amounts for this today. No neutral source measures the rate for a $20-200M supplier; the S5 deduction look-back does.

### 4.7 The kill condition

**Measured in:** the C-19 deduction look-back (`5_interview_kit.md` §6.3) on one supplier's real deduction lines for at least one quarter and one retailer: the portal export or EDI 812/820 remittances, with the matching orders, ASNs, PODs and carrier appointment times for a sample. Hours recorded.

**Who is measured** (*added 2026-09-22, C26, from P-29; founders: "Yes screen recruits first."*):
- **Screen first.** Every C-19 recruit is asked, before the look-back, what share of its sales to big-box retailers comes back as non-trade deductions (OTIF and compliance fines, shortages).
- **The look-back runs on a supplier reporting 1% or more.** That is the upper tail that S4.5 found carries the business (`4_5_profitability.md` §3.5). In CRF 2021, about 25% of suppliers at $500M or less reported non-trade deductions above 1% of sales.
- **Two more numbers are recorded with the look-back:**
  - **the screen yield:** the share of recruits reporting 1% or more;
  - **the new-money share:** of the provable-invalid dollars, the share the supplier would not have recovered on its own, from its own dispute and recovery records for the same period.
- **Why:** on the neutral distribution, a look-back on a random small supplier would fall under the kill line about 64% of the time even if the business is real. It would be measuring the median supplier, not the business. The lines below are unchanged by this rule; C26 changes who is measured.

**Definitions [our call]:**
- **Provable-invalid rate:** the dollars of non-trade deductions (OTIF and compliance fines, shortages) that the supplier's own documents show to be wrong **and** that are still inside the retailer's dispute window on the day of the look-back, divided by the supplier's sales to that retailer over the same period. Trade deductions are excluded.
- **Out-of-window invalid dollars** are recorded separately. They show what is lost today (H19-03) but are not counted.
- The 60% recovery share is applied until dispute outcomes arrive. Once 5-10 disputes are decided, the measured recovery share replaces it.

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The leak** | Provable-invalid rate on sales to that retailer, **measured on a screened supplier** (C26) | **under 0.05%** (0.03% recovered) | 0.05% up to the pass line. Continues only if the supplier's big-box sales are $50M or more, or the average deduction is $1,000 or more, or offshore handling is accepted | ~~0.17% or more (0.10% recovered)~~ **0.22% or more at a $50M supplier** (0.13% recovered); at other sizes, the pass line in the table below (*changed 2026-09-22, C27*) |
| **2. Access** | Portal export or 812/820 remittances plus PODs, under a mutual NDA; and whether the retailer's terms allow a third party to act in its portal | **2 of the first 3 paying-side interviewees cannot or will not share, or the retailer's terms bar third-party access** | 1 of 3 cannot | all 3 share |
| **3. Cost, measured** | From recorded minutes, deduction count and average size: gross profit at a $50M big-box supplier, 25% share, at the measured rate | **negative under US and offshore wages** | negative at US wages, positive offshore | positive at US wages |

**Why these lines [our call]:**
- **0.05% found (0.03% recovered)** is the neutral survey central, and the kill line is unchanged. At it, a $5k fee needs about $67M of big-box sales and pays back in 3-6 years. For a screened supplier (non-trade deductions at 1.2% of sales, more items to triage), a $50M supplier at 0.05% loses about $780 a year at US wages, and offshore it takes about 6 years to repay a $10k acquisition cost.
- ~~**0.17% found (0.10% recovered)** is where a $20M big-box supplier, the middle of the segment, pays $5k a year at a 25% share. At that rate a $50M supplier yields about $8,600 of gross profit at US wages, paying back a $10k acquisition cost in about 14 months. It is half STAT's aggregate and a quarter of the vendor high.~~ *Superseded 2026-09-22 (C27, from P-30; founders: "Update according to P30 as well").* Its comparison rested on STAT's all-in 0.2%. STAT's own split puts deductions won at 0.03%, so that comparison no longer holds. Its test was a $5k fee, not payback. And it assumed an unscreened supplier.
- **0.22% found (0.13% recovered) at a $50M supplier** is the rate at which a screened supplier repays a $10k acquisition cost within 12 months at US wages. That is S4.5's profitability bar (`submarket_selection.md` §4 S4.5). It assumes non-trade deductions of 1.2% of sales (the one in-segment ledger, M Design Village), $500 each, 5 minutes triage, 20 minutes per dispute, 60% recovered, a 25% share and $600 fixed. At 0.22% that supplier yields about $10,060 of gross profit a year; at the old 0.17% it yields $6,870 and takes about 17.5 months to pay back. **The line rises because the test is now payback, not a $5k fee, and because a screened supplier costs more to serve.** No vendor aggregate is used.
- **The pass line by the supplier's own big-box sales [our calc]** (BLS collector wage; fixed with the line, before any measurement):

  | Big-box sales | Break-even (for reference) | **Pass line (12-month payback on $10k)** | With posted analyst pay ($45/h) | If deductions average $300 |
  |---|---|---|---|---|
  | $20M | 0.076% | **0.47%** | 0.52% | 0.57% |
  | $50M | 0.062% | **0.22%** | 0.25% | 0.29% |
  | $100M | 0.058% | **0.14%** | 0.16% | 0.19% |
  | $200M | 0.055% | **0.094%** | 0.12% | 0.15% |

  Between rows, interpolate in a straight line. The last two columns show how far measured wages or deduction sizes would move the line. Test 3 already measures both.
- **Test 2** because there are no open retailer APIs. Without exports, and with retailers pushing back on automated disputing (Target fines a fifth dispute; Amazon ended bulk disputes; check U §3), the product cannot run.
- **Test 3** because the average deduction size decides cost (§4.3), and no neutral figure for it exists.

**Verdict rule:**
- **Any kill → C-19 stops S5 work.** It keeps its fact sheet and stays an S6 backup. Its conversations move to C-09, which shares the buyer (the controller at a manufacturer).
- **Any conditional and no kill → C-19 continues**, but S6 cannot confirm it as primary until the condition is met.
- **All pass → C-19 goes to the 1-10 re-score** with the measured inputs.

**Who decides:** the founders, on `5_log.md` §7. **Adopted by the founders on 2026-09-22 (D-22, §7.4) and frozen as of that date.** Moving them after a measurement needs a `submarket_selection.md` §9 entry with the reason.

*S4.5 note, 2026-09-22 (`4_5_profitability.md` §3.5-§4):*
- The "vendor" 0.2% used in §4.2 and §4.3 is STAT's all-in figure. STAT's own split puts deductions won at 0.03%, the neutral central.
- On the CRF 2021 distributions, a look-back on a random small supplier would fall under the kill line about 64% of the time.
- Two proposals, P-29 and P-30, are recorded there. **Both were adopted the same day as C26 and C27**, and are applied in this section: screening, and the pass line.

**What the interviews must add** (check AE §9.7): a year of deduction lines per retailer (count, dollars, size distribution, reason code); what was disputed, won and when; big-box sales by retailer; monthly OTIF scorecards; and the 3PL and carrier contracts that say who pays chargebacks.

---

## 5. C-20 · Import entries, for small customs brokerages

**Plain words first.** Every formal import into the US needs an *entry* filed with Customs (CBP). A licensed customs broker's *entry writer* reads the importer's commercial invoice, picks a 10-digit tariff number for each product (*classification*), keys the lines into the broker's filing software, and files. The product modelled here is the S4 "co-pilot" wedge (`4_scorecard.md` §2.4): it reads the invoice, pre-fills the lines and suggests the tariff numbers; the broker checks and files in its own software. **The saving is the entry writer's minutes, not money coming back**, so the fee is a price per entry set as a share of the minutes saved.

### 5.1 The chain

**Fee per brokerage** = formal entries a year × minutes saved per entry × loaded wage per minute × fee share.
**Gross profit** = fee − (entries × machine cost per entry + fixed cost per customer).

There is no "leak rate" here: nothing is billed wrong. The input that plays its part is **minutes saved per entry**, and the one that plays the part of "share credited" is **whether the time saved becomes money** for the broker (§5.6, Test 3).

### 5.2 Inputs

| Input | Central | Range | Label | Source |
|---|---|---|---|---|
| Minutes saved per entry (keying plus classification lookup the co-pilot removes) | **8** | 3-20 | **[our call]** | Neutral: CBP's contractor puts a formal entry at "approximately 10 minutes" of filer time (N-AF08, *verified*); classifying a new simple product takes 2-4 minutes (a broker, quoted by CBP's contractor, N-AF08, *verified*). Vendors: 20-65 minutes manual, classification plus keying about 45-75% of it (N-AF45, N-AF46, *assumed*). Low = a third of the neutral 10 minutes; high = long or new-product entries |
| Loaded wage, entry writer | **$39.54/h = $0.659/min** | $26.74-54.53 | *verified* wage (BLS OEWS May 2025, 43-5011 in NAICS 4885, mean $27.68) ÷ 0.70 **[our calc]** | N-AF11; N-AA40 |
| Labour saved per entry | **$5.27** | $1.98-13.18 | **[our calc]** | minutes × $0.659 |
| Fee share of the labour saved | **25%** | 20-35% | *assumed* (S0 shares; no market precedent for a share of time saved) | `0_criteria.md` §5 |
| **Price per entry that results** | **$1.32** | $0.40-4.61 | **[our calc]** | |
| What the filing platforms already charge for the same AI | **$0-0.25 per entry** | CargoWise: AI Classification Assistant included in its $9.95 per entry since 1 Dec 2025; CustomsCity AI extraction 3-25¢, HTS search 2-25¢; Gaia $0.42-0.99 a credit | *verified* (published prices, re-checked 2026-09-22) | N-AF31-N-AF36 |
| What importers pay per extra tariff line (a ceiling on the value of a line's work) | $5 | $3.50 (FedEx) - $15 (Clearit) | *verified* (published) | N-AF19-N-AF21 |
| Machine cost per entry (reading 3-5 invoice pages, 1-3 model calls) | **$0.10** | $0.03-0.26 | prices *verified*, **[our calc]** per entry | N-AA02, N-AA12-N-AA17; check AF §10.5 |
| Human review by us | none | — | **[our call]**: the broker must review by law (19 CFR 111.28), so the co-pilot suggests and the broker decides | N-AF50 |
| Fixed cost per customer a year (loading the importer's product history, support) | **$600** | $400-1,100 | **[our call]**, C-09's anchor; no source found | check AA §6 |
| Formal entries a year, by brokerage size (if a pure brokerage) | 1-4 staff 1,500; **5-9 staff 6,300**; 10-14 staff ~10,900 | 1,300-54,000 | **[our calc]** from Census payroll ÷ a 50-60% labour share ÷ a $125-150 fee | N-AF12, N-AF13, N-AF21, N-AF24 |
| Filers of electronic formal entries | **2,336**, averaging 9,903 entries (23,133,408 in all) | — | *verified* (CBP, 90 FR 46624-46625, re-read at source 2026-09-22) | N-AF03 |
| Filers above 1,000 / 5,000 / 20,000 entries a year | ~1,200 / ~480 / ~120 | 890-1,610 / 320-670 / 90-165 | **[our call]** on the shape of the spread | check AF §2.5 |
| Entries filed outside the ten largest filers | 9.3-15.0M | top ten hold 35-60% | *assumed* (analyst summaries, one unsourced) | N-AF54-N-AF56 |

### 5.3 The four numbers [our calc]

Price per entry at the central chain = minutes × $0.659 × 25% = **$0.165 per minute saved**, so **$1.32** at 8 minutes.

| Configuration | Price per entry | Break-even entries a year | Minutes saved needed to cover variable cost (25% share) | Entries for $5k a year | Gross profit, 6,000-entry brokerage | Payback on a $5-15k acquisition cost |
|---|---|---|---|---|---|---|
| **Central: 8 minutes, 25%** | $1.32 | **493** | **0.6** | **3,794** | $6,708 | 9-27 months |
| Low: 3 minutes, 25% | $0.49 | 1,522 | 0.6 | 10,116 | $1,766 | 34-102 months |
| High: 20 minutes, 25% | $3.29 | 188 | 0.6 | 1,517 | $18,570 | 3-10 months |
| 8 minutes, 35% | $1.85 | 344 | 0.4 | 2,710 | $9,871 | 6-18 months |
| **Priced at the platforms' AI rate, $0.25** | $0.25 | 4,000 | — | 20,000 | $300 | never inside 12 months |

- **"Cheapest labour" does not apply the way it does for C-09:** we do no human review, so the variable cost is machine-only. With the $0.26 high machine cost, 1.6 minutes saved still covers it.
- **Cost is not the constraint; price is.** Covering variable cost needs well under a minute saved per entry. What decides C-20 is whether a broker pays a share of the time saved when its filing platform bundles the same AI at $0-0.25.
- **The $5k line** is reached by a 5-9-staff brokerage (about 6,300 entries) at the central chain, and missed by 1-4-staff brokerages (about 1,500 entries) unless about 20 minutes are saved per entry.

**Worked example [our calc].** A brokerage with 7 staff files about 6,300 formal entries a year. At 8 minutes saved per entry, its writers get back 840 hours a year, about half a person, worth 6,300 × $5.27 = $33,200 at loaded wages. A 25% share is **$8,300 a year**. Machine cost is 6,300 × $0.10 = $630, fixed cost $600, so **gross profit is about $7,070**, and a $10k acquisition cost pays back in about 17 months. If the broker's platform already does the extraction for 15¢ an entry, the broker will pay at most about 6,300 × $0.15 = $945 a year for the same thing, and the customer never pays back.

### 5.4 Revenue test: $1M and $2.5M [our calc]

Customers are counted in entries, because brokerages vary so much in size. At $1.32 per entry, **$1M needs about 760,000 entries a year** and **$2.5M about 1.9 million.**

| Case (entries outside the top ten, and the share of them in brokerages above break-even) | Price per entry | Revenue at a 10% share | Share needed for $1M | Share needed for $2.5M |
|---|---|---|---|---|
| Top ten hold 35%; 85% eligible (12.8M entries) | $1.32 | $1.69M | **5.9%** | **14.8%** |
| Top ten hold 50%; 70% eligible (8.1M) | $1.32 | $1.07M | **9.4%** | **23.4%** |
| Top ten hold 60%; 70% eligible (6.5M) | $1.32 | $0.86M | **11.7%** | **29.2%** |
| Same three, at $2.31 (10 minutes, 35%) | $2.31 | $1.50-2.95M | 3.4-6.7% | 8.5-16.7% |
| Same three, at the platforms' $0.25 | $0.25 | $0.16-0.32M | 31-62% | 78-154% (impossible) |

In customers: about 200 brokerages at an average $5k for $1M, 500 for $2.5M, against roughly 320-670 filers above 5,000 entries.

**Reading [our call]:**
- **$1M passes** at check A's conservative 10% share in two of three cases, and needs 12% in the third.
- **$2.5M needs 15-29% of the small and mid-sized brokers' entries** at the central price. That is inside check A's 10-35% band, so it is a stretch, not a knock-out.
- **Both fail outright if the price collapses to what the platforms charge.**

### 5.5 Does C-20 meet the fee rule as written?

**Not cleanly, and this is flagged for `submarket_selection.md` §9 rather than bent here** (as `handoff.md` §4 asks).
- The rule (CLAUDE.md, Constraints): "The fee has to come out of savings. A problem only qualifies if it has a cost we can measure and our fee can be a share of it."
- **Measurable:** yes. A time study measures minutes per entry before and after (`5_interview_kit.md` §6.4).
- **A share of it:** only if the per-entry price is **set and stated** as a share of the measured minutes, not as a usage price.
- **Is the saving money?** Only if the broker turns the minutes into cash: fewer paid hours, less overtime, or more entries with the same staff. The large brokers do (Expeditors: automation "to reduce the time required to file customs entries", with customs net revenue up 11.6% in 2025; C.H. Robinson: customs gross profit per transaction +26%; N-AF13, N-AF15, *verified*). **For small brokerages nothing public says either way.** Test 3 below measures it.
- **Proposed wording for §9 [our call], not applied:** "A labour saving counts as a saving under the fee rule only where the customer shows it converts into cash (hours not paid, work not turned away). Such a card is priced per unit as a stated share of the measured minutes." For the founders to accept, change or reject.

### 5.6 The kill condition (not adopted: C-20 was eliminated; kept for the record)

**Measured in:** the C-20 time study (`5_interview_kit.md` §6.4). An entry writer at each of the first three small brokerages (under 50 staff) prepares 3-5 real entries while being timed step by step. The 20 redacted entries give lines per entry and the classification lookups needed. The price test and the platform question are asked in the same visit.

**Definitions [our call]:**
- **Removable minutes per entry:** the minutes the timed writer spends reading the invoice, keying lines, and looking up tariff numbers for products not already in the importer's product history. Excluded: review, filing, correspondence, ISF.
- **Weighted** by each brokerage's entries a year.
- **Platform AI in use:** the brokerage's filing software already offers invoice extraction or classification suggestions **and** the writer uses it on the timed entries.

| Test | Measurement | Kill | Conditional | Pass |
|---|---|---|---|---|
| **1. The saving** | Removable minutes per entry, timed | **under 4 minutes** | 4 to 8 minutes. Continues only if Test 2 shows at least $1.00 per entry accepted, or the lines per entry show that a few long entries carry most of the work (a segment for Q6) | **8 minutes or more** |
| **2. Price against the platform's own AI** | Of the first 3 brokerages: is the platform's AI in use, and what per-entry price (or letter of intent) is accepted? | **2 of 3 use their platform's AI and refuse any price above $0.50 per entry** | 1 of 3 does, or the price accepted is $0.50-1.00 | **2 of 3 accept $1.00 per entry or more** (a letter of intent or a paid pilot) |
| **3. Does the saving become money?** | Of the first 3: in the last 12 months, did entry volume cause paid overtime, temporary staff, a hire, or work turned away or delayed? Would time saved change staffing or intake? | **2 of 3 say no to both**: the time saved is not cash, and the card fails the fee rule as written | 1 of 3 says no | **2 of 3 say yes** |

**Why these lines [our call]:**
- **4 minutes** is where a 25% share falls to $0.66 an entry. That is within three times of what CustomsCity charges for the same AI, and $5k a year then needs about 7,600 entries, so only the 10-plus-staff brokerages qualify, and $2.5M would need 30-58% of the small and mid-sized brokers' entries.
- **8 minutes** is where a 25% share reaches $1.32 an entry. At that price break-even is under 500 entries, a 5-9-staff brokerage passes $5k a year, and $1M needs 6-12% of the small and mid-sized brokers' entries.
- **$0.50 and $1.00 on price.** $0.50 is twice CustomsCity's dearest per-use AI price (25¢) and is the break-even price at about 1,500 entries. $1.00 gives $5k at 5,000 entries and $1M at 8-15% of the eligible entries.
- **Test 3** is the fee rule itself. If the saved minutes never become money, the broker is buying software, not sharing a saving. That may still be a business, but it is not the one CLAUDE.md describes.

**Verdict rule:**
- **Any kill → C-20 stops S5 work.** It keeps its fact sheet and stays an S6 backup. Nothing else on the shortlist shares its core, so its interview slots go back to the pool. A Test 3 kill is also recorded as a §9 question about the fee rule.
- **Any conditional and no kill → C-20 continues**, but S6 cannot confirm it as primary until the named condition is met.
- **All pass → C-20 goes to the 1-10 re-score** with the measured minutes and price.

**Who decides:** the founders, together, on the evidence in `5_log.md` §7. These lines are a proposal until the founders adopt them. Once adopted they are frozen, and moving them after a measurement needs a `submarket_selection.md` §9 entry.

**What the interviews must add** (the kit covers most of it; the last two are new asks): minutes by task, lines per entry, entries a year and staff, the filing software in use, whether its AI is switched on, and the last 12 months' overtime, temporary staff, hiring or turned-away work.

### 5.7 Why C-20 is not pursued (D-22, 2026-09-22)

**It was viable on paper.** At the central chain (8 minutes saved an entry, a 25% share, $1.32 an entry):
- break-even is under 500 entries a year;
- a brokerage with 5-9 staff (about 6,300 entries) pays about $8,300 a year, with about $7,000 of gross profit;
- a $10k acquisition cost pays back in about 17 months;
- $1M of revenue needs 6-12% of the small and mid-sized brokers' entries, and $2.5M needs 15-29%.

It was the only one of the four whose customer comes close to check A's 12-month payback at central inputs.

**Why the founders did not choose it:**
1. **The founders' own line.** Their words, 2026-09-22: "I dont care for creating software that cuts paid hours." C-20's saving *is* the entry writer's paid time. Its value to the broker exists only if the broker pays for fewer hours or does more work with the same staff (§5.5).
2. **The fee rule fits badly.** The saving is staff time, not money coming back. That is why §5.5 flagged it for `submarket_selection.md` §9, and why its Test 3 would have had to prove the time becomes cash.
3. **Price pressure from the platforms.** CargoWise includes an AI classification assistant at no extra charge, and CustomsCity sells AI invoice reading at 3-25¢ an entry, against the $1.32 the chain needs (§5.3).

Its evidence stays in this file and in check AF for later runs.

---

## 6. The four cards side by side, and the elimination test

### 6.1 The rule this section applies

The founders set it for this step, 2026-09-22 (verbatim in §7.1): eliminate any card that "demonstrate[s] no viability" in saving a customer money reliably enough to charge a fee that reaches $2.5M, or $1M, of revenue; keep any card whose doubt is an **unknown** until the unknown is measured.

**How it is applied here [our call]:**
- **Eliminate** only when a card fails **even at the most favourable end of every input nobody has measured** (the "ceiling test"). The failure must then rest on measured facts: customer size, published prices, wages.
- **Keep alive** when the card fails at the central inputs but passes somewhere inside the range of an unmeasured input. Its kill condition names that input and the line.
- **Two money tests per card:** per customer (break-even size, the $5k line, payback on a $5-15k acquisition cost against check A's 12-month norm), and the market ($1M and $2.5M against check A's 10% conservative share and 10-35% band).

### 6.2 The four numbers, side by side [our calc]

| | **C-09** freight-bill audit | **C-11** LTL correction disputes | **C-19** retailer deductions | **C-20** import-entry co-pilot |
|---|---|---|---|---|
| Customer's size measured in | TL+LTL spend a year | LTL spend a year | Big-box sales a year | Formal entries a year |
| Typical customer in the card's segment | $0.27-2.9M (bands, check X §7.4) | **$94k** (median of 9 real firms) | ~$20-200M | ~1,500-10,900 entries (1-14 staff) |
| Fee at the central chain | $1.97 per $1,000 | $1.31 per $1,000 | $75 per $1M | $1.32 per entry |
| **1. Break-even size, US labour** | $1.35M | **never** | $16.8M | 493 entries |
| **2. Leak needed to cover variable cost, US** | 1.28% overcharged | 1.55% wrong and provable | 4.4% of deductions invalid (0.013% of sales recovered) | 0.6 minutes saved |
| **3. Same two, cheapest labour** | $0.3M; 0.46-0.50% | $1.01M; 0.37% | $9.8M; 1.4% (0.004%) | not applicable (no human review by us) |
| **4. Size at which the fee reaches $5k** | $2.5M | **$3.8M** (ceiling: $572k) | $66.7M (vendor rates: $10M) | 3,794 entries |
| Payback on a $10k acquisition cost at a typical-to-large customer | ~22 years at $2.9M (gross profit ~$460) | never | 5.6 years (US) / 2.9 (offshore) at $66.7M | ~17 months at 6,300 entries (9 on a $5k cost) |
| **Market: $1M** | ~175 customers at $2.9M, ~3% of ~5,400 firms that size | ~8,100 customers, every one loss-making | ~100 customers, 5-17% of 600-2,000 qualifying | 6-12% of the small and mid-sized brokers' entries |
| **Market: $2.5M** | ~440, ~8% | ~20,300, every one loss-making | ~250, 13-42% | 15-29% |
| **Ceiling test** (every unmeasured input at its best) | passes (vendor cases 1.8% median; offshore) | **fails**: the median shipper pays ~$820 a year | passes (vendor aggregate 0.2%; $5k at $10M) | passes (20 minutes saved, 35%: $4.61 an entry) |
| Fee rule as written | meets it | dispute half meets it in form; prevention half does not | meets it | **not cleanly**: the saving is staff time (§5.5) |
| **Desk verdict [our call]** | **alive on an unknown**: the overcharge rate (§2.4, frozen) | **no viability: proposed for elimination** | **alive on an unknown**: the recoverable rate | **alive on unknowns**: minutes saved, price against built-in AI, and whether time becomes money |
| **Founders' decision (D-22, 2026-09-22)** | **focus** (front-runner, working bet unchanged) | **eliminated** | **focus**; kill lines adopted and frozen | **eliminated**: viable on paper, not pursued (§5.7) |

> **Note, 2026-10-08 (D-23):** rows 1-3 for C-09 and C-19 assume **our own** review labour ("US labour", "cheapest labour" meaning offshore reviewers). Under D-23 we employ no analysts, so those cells describe a service model the founders have ruled out. C-09's re-run (`handoff_c09_software_rerun.md`; written as §2.5, proposed 2026-10-08) replaces them for C-09; C-19's are flagged for the same re-run (§4 banner). The cells are kept as the record of the service-basis model.

### 6.3 What the side-by-side says [our call]

1. **Only C-11 fails the ceiling test, and it fails on customer size, not on a guessed rate.** The real small shippers in the bankruptcy files buy $31k-389k of LTL a year (median $94k). No correction rate, win rate or fee share turns that into $5k a year. The same finding shows in FedEx Freight's own average customer of $64k outside its top 25.
2. **The three recovery cards share one pattern.** At the neutral rates (GSA and USDA for freight bills, CRF for deductions) each is thin. At the rates vendors publish and charge for, each is healthy. **S5's savings assessments are the only way to tell which world the segment lives in,** which is why each kill line sits between the two.
3. **C-20 is the opposite case.** Its cost is trivial and its per-customer arithmetic works at the central chain. What can kill it is **price**: the filing platforms now bundle invoice extraction and classification at $0-25¢ an entry. The **fee rule** is its other risk: a labour saving is money only if the broker turns it into cash.
4. **None of the four is shown viable yet.** C-19 and C-20 pass the $1M market test at the central chain, and C-09 does too, but with a thin margin. None meets check A's 12-month payback on a $10k acquisition cost at the central inputs. C-20 comes closest, at about 17 months (9 on $5k).

---

## 7. Decision for the founders (D-22), in the decision-record format

### 7.1 Initial decision (the founders, 2026-09-22, verbatim)

> "The goal is to find out which of our sub-market candidates we could actually save money with our software, a reliable amount of money that we could charge so we can reach out $2.5M target(s). Or $1M revenue.
>
> We want to absolutely eliminate any of the sub-market candidates that demonstrate no viability in this sense, if there are unknowns then they will allow them to continue living until the unknowns are clarified.
>
> Use Extensive Web Search and real documents with pay statements found from reliable sources to demonstrate this arithmetic. Math!"

### 7.2 Research for and against, card by card

**C-11: eliminate?**
- **For eliminating:**
  - Nine real small manufacturers and distributors bought $31k-389k of LTL a year (median $94k), from sworn bankruptcy payment lists (N-AD14 to N-AD22).
  - At the median, the central fee is $123 a year and the customer loses money under US and offshore labour.
  - At the ceiling (every correction wrong, every dispute won) the median pays ~$820 a year and never repays a $5k acquisition cost inside 12 months.
  - The documented carrier-error pool is 0.18-0.54% of revenue (DOJ complaint against Yellow and Roadway). The US-labour line needs 1.55%.
  - On a real account (the ABF bills), corrections were frequent but nearly weightless: 28 of 101 bills reweighed; 10 restored by the carrier; 11 on the minimum charge; no fee on any bill.
  - Prevention saves mostly the $15-55 fee, can raise the bill, and 3PLs give the tools away (N-AD30).
- **Against eliminating:**
  - The nine firms were in distress (they ship less), and freight they booked through a 3PL or that customers paid (collect) is hidden, so spend is understated. But at three times the median, the ceiling fee is still ~$2.5k.
  - The share of corrections that are wrong is unmeasured.
  - The dispute logic has real value as a **feature** of C-09's audit for larger shippers, and a 3PL could aggregate many small shippers. Both are different products or paying sides.
- **Verdict [our call]:** the rule's "no viability" is met for the card as defined. Keep its evidence, and its dispute checks inside C-09's scope.

**C-19: keep alive?**
- **For:**
  - SupplyPike's expected ~$25M of 2025 revenue from 500+ suppliers (up to ~$40-50k each) shows suppliers pay for this at scale.
  - The fee rule is met cleanly.
  - At the vendor aggregate (0.2% recovered), a $10M supplier reaches $5k a year.
- **Against:**
  - At the neutral central (0.03% recovered), $5k customers start at $67M and pay back in 3-6 years.
  - Amazon's rule changes "reduce the amount we can recover" (SPS's CFO), and Walmart eased OTIF in 2024.
  - SPS now targets exactly this buyer.
- **Verdict [our call]:** alive on an unknown; the kill line in §4.7 decides.

**C-20: keep alive?**
- **For:**
  - Cost to serve is trivial, and break-even is under 500 entries.
  - A 7-staff brokerage pays ~$8k a year at the central chain.
  - $1M needs 6-12% of the small and mid-sized brokers' entries.
  - Large brokers show automation turning into capacity and higher profit per entry.
- **Against:**
  - CargoWise bundles an AI Classification Assistant at no extra charge; CustomsCity sells AI extraction at 3-25¢.
  - The neutral figure for a whole formal entry is ~10 minutes.
  - The saving is staff time, which meets the fee rule only if it becomes cash.
- **Verdict [our call]:** alive on unknowns; the kill lines in §5.6 decide. Flag the fee-rule question for `submarket_selection.md` §9.

**C-09:** no change. Its kill condition was frozen on 2026-09-22 (§2.4). §6.2 adds only its market test, which passes at the central chain with a thin margin.

### 7.3 Open points to settle together

| # | Point | Suggested starting point **[our call]** | Founders, 2026-09-22 |
|---|---|---|---|
| a | Eliminate C-11 as a standalone card? | **Yes.** Keep its fact sheet and evidence. Its reweigh and reclass checks stay inside C-09's audit scope | **C-11 eliminated; C-20 eliminated too** (§5.7) |
| b | C-09's verdict rule sends its conversations to "C-11 and C-19" if C-09 is killed (§2.4). With C-11 gone, that reads "C-19" | Amend the wording to C-19 only; the lines stay frozen | not answered; noted as a consequence in §2.4 |
| c | Adopt the proposed kill lines for C-19 (§4.7) and C-20 (§5.6), and C-11's (§3.8) if a is "no"? | Adopt as written; they freeze on adoption | **Yes**: C-19 adopted; C-11 and C-20 moot |
| d | C-20's fee-rule question: add wording to `submarket_selection.md` §9 (§5.5)? | Record it as proposal **P-28**, not applied, and let C-20's Test 3 answer it | **Yes** (with e; see §7.4 on what "yes" covers) |
| e | Make the ceiling test part of S4 step 7 for later runs: "a card fails step 7 only if it fails with every unmeasured input at its most favourable value" | Record it as proposal **P-27**, not applied | **Yes** (see §7.4) |
| f | C-11's S5 slots (5 paying-side interviews plus 1-2 workers) | Give them to C-09, favouring LTL-heavy shippers, so the reweigh checks are still tested | **Yes** |

**Process changes proposed** (*adopted 2026-09-22 as C23 and C24; see §7.4*):
- **P-27:** the ceiling test (point e).
- **P-28:** labour savings under the fee rule: "A labour saving counts as a saving under the fee rule only where the customer shows it converts into cash (hours not paid, work not turned away). Such a card is priced per unit as a stated share of the measured minutes." (point d)

### 7.4 Finalized decision

**The founders' decision, 2026-09-22 (verbatim):**

> "1. C-11 and C-20 are dead now. I dont care for creating software that cuts paid hours. Mention C-20's viability, but why it was not chosen for pursuit.
>
> 3. Yes
> 4. Yes
> 5. Yes
>
> Note that the focuses are now C-09 and C-19."

**What it means:**
- **C-11 is eliminated.** It fails the ceiling test on measured customer size (§3.7). Its reweigh and reclass checks remain part of C-09's audit scope.
- **C-20 is eliminated.** This is the founders' choice rather than a desk kill: it was viable on paper but is not pursued, for the reasons in §5.7.
- **C-19's kill lines (§4.7) are adopted and frozen** as of 2026-09-22. C-11's and C-20's lines are moot.
- **C-11's S5 slots go to C-09**, favouring LTL-heavy shippers, so the reweigh checks are still tested (point f).
- **The focus is now C-09 and C-19.** C-09 stays the front-runner as a working bet (option B, 2026-09-17), with its lines frozen (§2.4).
- **Not decided:**
  - Point b was not answered. Its consequence is noted in §2.4.
  - Where C-20's freed S5 slots go (5 broker and 5 importer interviews).
  - ~~**What "4. Yes" covers.** The founders agreed to P-27 and P-28. Whether that means writing them into `submarket_selection.md` §9 now (as C23 and C24) or keeping them recorded as proposals is to be confirmed. They are not yet written into §9.~~ **Settled the same day:** asked whether to write them in, the founders answered "4. Yes". **P-27 is adopted as C23 and P-28 as C24** (`submarket_selection.md` §9, §4 S4 step 7, §5.4).
  - Whether the founders' line on paid hours should become a rule for later runs (for example, a knock-out for cards whose saving is staff time). It is recorded here verbatim, not applied.

---

## 8. Sources

**§2 (C-09):** no new sources. Every figure comes from files already in the repository: `research/s5_check_X_c09_money.md` §2, §5, §10; `research/s5_check_AA_c09_cost_to_serve.md`; `research/s5_check_AB_c09_private_recoveries.md` §2-§4, §7; `research/s5_check_AC_c09_example_invoices.md` §8; `research/s5_practice_audit_public_invoices.md` §3, §5; `research/s0_check_A_ambition_economics.md` §A3; `research/selection_runs/run-01/6_focused_target.md` §4.4. Arithmetic in §2.3 is marked **[our calc]**; the model was re-run on 2026-09-22 and reproduces the recorded $1.35M break-even.

**§3-§7 (C-11, C-19, C-20; 2026-09-22):**
- **Three new checks, one per card**, each with its own source list and a list of what could not be found:
  - `research/s4_check_AD_c11_money.md` (N-AD01 to N-AD41): the DOJ reweigh complaint against Yellow and Roadway; the UPS Freight bills in the Delphi bankruptcy; nine small shippers' bankruptcy payment lists; carrier customer counts; SJ Consulting's LTL market tables; class-rate ratios; BLS wages; 3PL tool prices.
  - `research/s4_check_AE_c19_money.md` (N-AE01 to N-AE60): supplier 10-Ks (Crown Crafts, Lifetime Brands, Hamilton Beach, JAKKS and others); the *Miller v. ANConnect* deduction ledger; the Instant Brands first-day declaration; CRF surveys; SPS Commerce releases and calls; vendor prices; BLS wages; the Walmart supplier-size model.
  - `research/s4_check_AF_c20_money.md` (N-AF01 to N-AF63): CBP's entry-summary burden notice (90 FR 46624) and supporting statement; CBP's permitted-broker list; the low-value-shipment regulatory analysis; Census SUSB; BLS wages; published broker fee schedules (Clearit, Strix, FedEx, DHL, UPS SCS, two universities); CustomsCity, CargoWise and Gaia prices; Expeditors and C.H. Robinson filings; 19 U.S.C. 1592 and 1641.
- **Re-checked at the source in this chat (2026-09-22):**
  - the DOJ complaint ¶73 (75,324 upward and 42 downward reweighs; "more than 1.5 million invoices") and the Roadway figure of "$1 to $1.5 million in revenue per month";
  - Cycle Force Group's statement of financial affairs (Central Transport $46,009.50, Estes $22,906.60, ArcBest $17,859.64, XPO $9,059.65; 2020 revenue $14,349,516);
  - the *ANConnect* ledger ("Shipping Variances" $54,048.32 on $27,026,436.25) and the Instant Brands "Off-Invoice Allowances" of about $1.6M a month;
  - SPS's statement at the SupplyPike purchase that it expected about $25.0M of 2025 revenue (a forecast);
  - CBP's notice at 90 FR 46625 (2,336 respondents × 9,903 = 23,133,408 electronic formal entries, 5 minutes);
  - the regulatory analysis's "approximately 10 minutes" for a formal entry;
  - the permitted-broker list (2,407 rows);
  - CustomsCity's AI extraction prices (25¢ and 15¢ on its two smallest plans);
  - WiseTech's release on the CargoWise Value Packs (AI Classification Assistant included; no seat fees; from 1 December 2025).
- **One recount done here:** the 101 ABF Freight bills in *In re IN Holdings*, Bankr. C.D. Cal. 1:24-bk-11323, Doc 920, Exhibit 2 (https://storage.courtlistener.com/recap/gov.uscourts.cacb.1993985/gov.uscourts.cacb.1993985.920.0_1.pdf), re-parsed bill by bill for reweigh notes, restored weights, minimum charges, fees and rating class (§3.3). Parsing scripts and model scripts are in the session scratchpad, not in the project.
- **Arithmetic:** every figure marked **[our calc]** in §3-§6 comes from three short model scripts (one per card) using the inputs tables as written. The C-09 method was re-run first to check that it reproduces §2.3.

**§2.5 (C-09 re-run on the software basis, D-23; 2026-10-08):**
- **Three new checks, each followed by an adversarial review that fetched every source again:**
  - `research/s5_check_AQ_c09_customer_review.md` (N-AQ01 to N-AQ47) and `research/s5_check_AQ_adversarial.md`: minutes per exception (the Australian Tax Office's calculator; APQC; Ardent), exception rates, queue behaviour (tolerances, write-offs, abandonment), who files, carriers' and brokers' dispute channels, buying friction, security demands (FreightPOP's SOC 2 statement, Freightview's terms, the Pittsburgh RFP). 1 claim discarded, 15 narrowed;
  - `research/s5_check_AR_c09_software_cost.md` (N-AR01 to N-AR41) and `research/s5_check_AR_adversarial.md`: support cost per ticket (MetricNet), hosting list prices, SOC 2 platform prices, SMC3's licence (FEMA's award on USAspending; SMC3's pages; TMS vendors' documents), gross margin, churn and CAC benchmarks (Benchmarkit, SaaS Capital, OpenView, Xero, Weave), table- and contract-extraction accuracy. 0 discarded, 7 narrowed;
  - `research/s5_check_AS_c09_market_models.md` (N-AS01 to N-AS63) and `research/s5_check_AS_adversarial.md`: published prices of freight-audit software (Freightview, MyCarrier, FreightPOP, Kuebix, nShift, AuditRes, Lojistic), share-of-savings software in eight markets and how it confirms a recovery, the Miami-Dade contract with Tangoe, hours-saved wording. 0 discarded, 7 narrowed.
- **Re-checked at the source in this chat (2026-10-08):** MetricNet's email ticket cost ($24.24 average, $19.96 median); FEMA's SMC3 award ($8,764, 2019-20); Lightsail's $24 and $120 plans; Lojistic's ladder (29%; $99 + 19%; $389 + 9%; $5,959 + 0%); the Miami-Dade contract (agenda item 260241: $24,700 minimum monthly fees, Exhibit 1's bar on contingency fees for billing-discrepancy credits, the 20% cap); the Australian Tax Office's 15 and 20 minutes (Wayback copy; the live page refused access); FreightWaves 2017 on dispute thresholds and abandoned complaints; Freightview's 3% / $50 auto-accept example; and the discarded Gartner poll (Wayback copy: 263 participants, 8% / 38% / 28%).
- **Inputs already in the repository:** check AA §6 and §9.1; check AJ §9; check A §A3; check X §7.4; `C09-open-questions-evidence.md` §4-§7; `research/s5_practice_audit_public_invoices.md`; §2.2-§2.4 above.
- **Arithmetic:** one model script, kept in the session scratchpad and not in the project. It first reproduces §2.3's service-basis break-even ($1.36M against the recorded $1.35M), then computes every **[our calc]** in §2.5 from the inputs table as written.
