# C-09 business proposal: checking freight bills for mid-sized shippers

> **Written 2026-10-02 for the founders to read and come back to; rewritten 2026-10-09 to the software-and-subscription strategy,** at the founders' request ("We have redefined this business strategy … Ensure these are updated to correspond with this"). It gathers in one place what run 01 has learned about the front-runner, C-09. Text that no longer fits the strategy has moved, word for word, to §13.
> **Status:** C-09 is a **working bet** (option B, chosen 2026-09-17), **not the final choice.** The final choice is made at S6, after the S5 interviews and re-score. **This document decides nothing.** It moves no frozen line and settles none of the open points in §8. Those stay with the founders, to be settled together later.
>
> **The strategy now** (decided by the founders on 2026-10-08 and 2026-10-09; `research/selection_runs/run-01/4_kill_conditions.md` §2.5, `software-initial-pitch.md` §1A):
> 1. **A software company, not an audit firm (D-23).** The software flags the bills that look wrong. The **customer's own staff** review the flags and file the disputes. We employ no analysts and do no manual review. Helping customers file comes later.
> 2. **A flat monthly subscription (C28),** sold as "a scoop off the top of the money they will make", not dependent on what comes back. The price is a Q6 decision.
> 3. **The look-back design is adopted:** capacity asked first, the software's rules run as scripts, the shipper's reviewer confirms the rules and works every flag while timed, then a pilot of at least one billing cycle.
> 4. **Kill Test 1 measures flagged dollars:** what the software flags and the shipper's reviewer accepts as wrong and provable.
> 5. **The cost of winning a customer is bounded at $0 to $10,000** until the first customer is timed.
> 6. **The kill test's new lines, Kill / Cover / Pass (§7), are adopted** (founders, 2026-10-09: "Adopt the Kill/Cover/Pass lines"; C29), with Tests 2 and 3. Look-backs may start once the data-handling rules (D-18) are settled. P-31 is deferred.
>
> **Labels**, as in every run-01 file:
> - *verified*: read at the source;
> - *assumed*: a vendor claim, an association figure or a secondary summary;
> - **[our calc]**: our arithmetic;
> - **[our call]**: our judgement.
>
> Freight words are defined on first use, and again in the glossary (§11).

**Contents**
1. Where the project stands
2. Why C-09 is the front-runner, and what counts against it
3. The pitch, and the money in one customer
4. How freight billing works, step by step, and where we come in
5. The software (a sketch, not a decision)
6. Who does this job today
7. The kill condition: how C-09 lives or dies
8. Open questions, stated and not settled
9. Your job
10. The alternative: C-19, in brief
11. Glossary
12. Sources
13. Superseded, kept for the record

---

## 1. Where the project stands

- **The aim:** find a freight sub-market where software cuts a cost we can measure, and charge a fee that comes out of the saving. For C-09 the fee is a flat monthly subscription, sold as "a scoop off the top of the money they will make" but not dependent on it (C28). The revenue floor is $2.5M a year (`CLAUDE.md`, Constraints).
- **The desk research is done. No customer has been interviewed.** The project is in **S5, validation by interviews.** As of 2026-10-09 the evidence log (`research/selection_runs/run-01/5_log.md`) records no interview, and every item on the S5 gate tracker reads zero.
- **How we got here:**

  | Stage | Cards left | What happened |
  |---|---|---|
  | S1 | 40 | The long list of candidates |
  | S2-S3 | 18, then 5 | Size, durability and fact-sheet checks |
  | S4 | 4 | C-08 (carrier fraud vetting) was demoted: its saving is risk avoided, which a share-of-savings fee cannot be charged on |
  | 2026-09-22 (D-22) | **2** | **C-11** (LTL billing disputes) was eliminated because it fails even with every unknown at its best. **C-20** (import entries) was eliminated because its saving is paid staff hours: "I dont care for creating software that cuts paid hours" |
  | 2026-10-08 (D-23, C28) | 2 | C-09 redefined as software sold by subscription, and its kill test re-run on that basis (lines proposed, not adopted) |
  | 2026-10-09 (C29) | 2 | C-09's new kill lines adopted: Kill / Cover / Pass by the shipper's size, with Tests 2 and 3 |

- **The two left:**
  - **C-09, checking truckload and LTL freight bills,** is the front-runner;
  - **C-19, retailer on-time-in-full fines and deductions,** is the second focus (§10).
- **The schedule has slipped.** The interview window was planned for 21 Sep to 16 Oct. As of 2 Oct no outreach had gone out. On 2026-10-08 the founders planned to put the two "who works the flags" questions to the contacts already found.
- **The live brief for the interview stage** is `handoff_s5_interviews.md`. The kill-test re-run briefed in `handoff_c09_software_rerun.md` is done: its lines are in `4_kill_conditions.md` §2.5, adopted on 2026-10-09 (§2.5.12). The earlier `handoff.md` (kill conditions for the other cards) is finished.
- **The questions still to answer** are listed in one place: `C09-open-questions-evidence.md` §0.

---

## 2. Why C-09 is the front-runner, and what counts against it

### 2.1 The case for it

| Reason | Detail | Label / source |
|---|---|---|
| **The biggest prize** | A central fee pool of **$209M a year**, 3-6 times any other finalist. **95,579** US manufacturers (57,309) and wholesalers (38,270) have 20-499 staff. *The pool was computed on the old basis, a 25% share of recoveries; it has not been re-run for a subscription* | pool **[our calc]** on *assumed* inputs; firm counts *verified* (Census) · `6_focused_target.md` §2 |
| **The cleanest record** | The only card to pass every knock-out test outright, with no unknowns carried forward | `2_knockouts.md`, `3a_unknowns.md` |
| **The fee fits the rule** | The saving is overcharges recovered: money that comes back to the shipper. Our subscription is sold against it, as "a scoop off the top of the money they will make", but it doesn't depend on it. The founders ruled on 2026-10-08 that a subscription meets the fee rule (C28). The price is a Q6 decision | `submarket_selection.md` §5.4, §9 C28; `4_kill_conditions.md` §2.5.10 |
| **Our cost is cents a bill** | Under the software model our running cost is about **$0.10 a bill plus $235 a year** per customer, so a customer covers its own running cost from about **$0.23M** of spend. Reading a bill by machine is cheap; the person reviewing it is the customer's own staff | **[our calc]** · `4_kill_conditions.md` §2.5.6, §2.5.9 |
| **The most open field** | No dominant player. The big audit-and-payment providers (Cass, U.S. Bank) start at about $10M+ of freight spend a year. Mid-sized shippers use "an AP clerk, a small audit firm, or nobody" | floors *assumed* (check Y); the mid-market gap **[our call]**, untested · `6_focused_target.md` §2-§3 |
| **It sits inside the payment** | It can grow into paying carriers for the shipper, and later into parcel audit and damage claims, which use the same documents | `6_decision.md` §2 |

### 2.2 The case against it, just as plainly

| Concern | Detail | Label / source |
|---|---|---|
| **The leak is unmeasured, and the neutral figures are low** | Under the proposed lines (§7), a $1.5M shipper needs **0.51%** of its in-window spend flagged for a customer won for free to cover our first-year cost, and **6.44%** to repay $10,000 of winning cost within a year. The figures that measure money **flagged** are all from audit firms: government pre-payment auditors 1.66-3.37% (self-reported); vendors' six cases 0.8-4.2% (median 1.8%), five of them large shippers in a first-year audit. The neutral figures measure money **collected**, a smaller thing, and are all under 0.5%: USDA's 1977 survey of farm co-operatives **0.45%**, federal post-payment audits about **0.07%** | USDA, GSA *verified*; vendor cases *assumed* · check X, check AB; `C09-open-questions-evidence.md` §4 |
| **The practice audit proved $0** | 101 real ABF Freight bills from a court record ($45,652.49). **Every bill added up.** 61% of the dollars carried a line that needs a document only the shipper holds | *verified* · `research/s5_practice_audit_public_invoices.md` |
| **Small LTL bills load the customer's staff** | The real account had **2.21 invoices per $1,000** of spend (the model assumes 1.5) and **58% of bills needing a person** (the model assumes 15%). Under D-23 those are flags in the customer's own queue: about **30 hours a month** at a $2M shipper at 58%, and about **45** on an LTL-heavy account, against the 20 hours a month we assume a shipper can give (kill Test 3) | **[our calc]** · `4_kill_conditions.md` §2.5.4 |
| **The cost of winning a customer now decides it** | At the middle values, a customer can't repay **$10,000** of winning cost within 12 months below about **$10.3M** of spend, whatever the price; that is where audit-and-pay providers' own floors begin. A customer won for **$0** pays for itself from about **$0.62M**. The founders expect early customers to cost only their own unpaid time, and will measure it on the first one | **[our calc]** · `4_kill_conditions.md` §2.5.9, §2.5.11 |
| **Head to head with self-serve tools** | Freightview (4.7 from 743 reviews, $149 a month for up to 50 shipments), MyCarrier and FreightPOP already give mid-sized shippers an audit screen their own staff work. Theirs compares the bill with the booking quote, not the rate agreement, and covers only loads booked through them | ratings *assumed*; prices *verified* (check AS) · `software-initial-pitch.md` §1A |
| **The hardest card to sell into** | The lowest "can we win it" score of the finalists (Axis W 55). The buyer is a finance team with no obvious gathering place, and a subscription needs a budget line, which a contingency fee does not | `4_scorecard.md`; `software-initial-pitch.md` §1A |
| **Funded rivals** | Loop raised $95M (April 2026) and absorbed Data2Logistics; Freehand raised $75M. Cass's own 10-K warns AI could make its offerings obsolete | *assumed* (press, filings) · check Z |
| **Durable only in steady industries** | Freight-bill counts fell 10.5% in 2008-09. The strict durability test passes only for steady shipper groups (food and other branded goods, packaging, paper, capital goods, building materials) and fails for auto, metals and homebuilding | *verified* (Cass) · `4_scorecard.md` §6.5 |

**Reading [our call]:**
- **Our own cost is no longer the problem.** The software reads a bill for cents.
- **The desk has not measured the numbers the business rests on:**
  - the flagged rate on a mid-sized shipper's own bills;
  - whether the shipper's staff will work the flags;
  - how many hours that takes them.

  Only the look-back and the pilot can.
- **The cost of winning each customer** matters more than our cost to serve, and the founders will measure it on the first one.

---

## 3. The pitch, and the money in one customer

### 3.1 The pitch

> **"Your trucking companies overcharge you on some of their bills, and nobody has the time to check them all. Our software checks every bill against your own rate agreements and shows your team the wrong ones, with the proof beside them, so they can dispute them inside the claim window."** **[our call]**, with no price in it (the price is Q6).

Never sell it as "saves your team time": the saving is recovered overcharges, not paid hours (the founders' rule, D-22). The software asks the customer's staff for some hours rather than cutting them.

- **Who buys:**
  - the **controller** (the finance manager at a mid-sized firm) or the **AP lead** (accounts payable, the team that pays suppliers' invoices);
  - at a US manufacturer or distributor with about 20-499 staff;
  - spending roughly **$1.5M or more** a year on truckload and LTL freight (the screen the kit uses, **[our call]**).
- **Who uses it:** the person who actually checks the bills, often in logistics rather than finance (check Y: 22 of 47 job postings put the job in logistics, 6 in AP). They work the flags and file the disputes; we don't.
- **What they get:**
  - money back they would not otherwise collect;
  - a flat monthly fee, not dependent on what comes back (C28; the price is Q6);
  - over time, carriers who know their bills are being checked.

### 3.2 The money chain

All figures are from the software re-run, `4_kill_conditions.md` §2.5 (proposed 2026-10-08, adopted 2026-10-09).

**Money recovered for the customer** = freight spend × **flagged rate** × **follow-through** × **share credited**.
- **Flagged rate:** the dollars on bills the software flags **and** the customer's reviewer accepts as billed wrong and provable, as a share of spend. It includes errors caught before payment. This is what kill Test 1 measures.
- **Follow-through:** the share of those flagged dollars the customer's staff actually dispute or get corrected.
- **Share credited:** the share the carrier credits or corrects.

**Our revenue** is a flat monthly subscription. The model assumes a shipper would pay **at most about a quarter of what it gets back** (the "value share", 25%). That is a ceiling on the price, the founders' "scoop off the top", not a share we take. If shippers would pay up to half, every line in §7 halves.

**Our cost per customer** = bills × (machine reading + storage) + hosting + support, plus our onboarding help in the first year. **Reported separately:** platform costs (a security certification, SOC 2, at $16.5-68k a year for the company) and the cost of winning the customer.

**The customer's own cost is their staff's hours:** flags (false ones included) × minutes per flag, plus disputes, plus confirming the rules the software read from their agreements. The founders treat these hours as **capacity**, not dollars: they decide whether the customer buys and whether the flags get worked (kill Test 3).

| Input | Middle value | Range | Label |
|---|---|---|---|
| Customer's truckload + LTL spend (reference) | $1.5M | $0.27-5M | payments *verified* (three real segment firms bought $1.5-1.9M a year) |
| Bills per $1,000 of spend | 1.5 | 1.5-2.21 | **[our calc]**; LTL carriers' own averages 1.88-2.03 |
| **Flagged rate** | **1.05%** | 0.21-2.1% | **[our call]**: the old 1.5% true rate × the old 70% catch |
| **Follow-through** | **60%** | 30-100% | **[our call]**; not measured anywhere |
| Share credited | 75% | 60-90% | **[our call]** |
| Price ceiling, as a share of what the shipper gets back | 25% | 9-50% | **[our call]**: software that acts itself takes 9-35%; audit firms 23-39%; small shippers' audit firms up to 50% |
| Machine reading per bill | $0.10 | $0.005-0.50 | prices *verified* (AWS Textract $0.01 a page), per bill **[our calc]** |
| Hosting; support (per customer a year) | $60; $175 | $36-184; $60-291 | list prices and ticket costs *verified*; volumes **[our call]** |
| Our onboarding help, first year | $400 | $185 (self-serve) - $616 (assisted) | **[our calc]** |
| Per-customer licence | $0 | up to $8,764 a year | **[our call]**; one agency's SMC3 price *verified* |
| **Cost of winning a customer** | **bounds $0 and $10,000** | — | founders, 2026-10-08; measured on the first customer |
| Share of bills flagged (false flags included) | 15% | 5-58% | **[our call]**; the real ABF account 58% |
| Minutes per flag; disputes | 10; 5% of bills at 30 minutes | 6-15; 15-60 | **[our call]** |
| Agreements to confirm in year one | 8 × 60 minutes | 6-9 carriers | **[our call]** |
| **The customer's capacity** | **20 hours a month** | — | **[our call]** |
| The customer's loaded wage | $36.79 an hour | — | *verified* (BLS); a sensitivity only |

### 3.3 Worked example **[our calc]**

**A shipper spends $2M a year on truckload and LTL freight.** The middle values above are guesses, not evidence (`4_kill_conditions.md` §2.5.4):

| Step | Amount |
|---|---|
| Bills a year | 3,000 (250 a month) |
| Flagged by the software and accepted by their reviewer: 1.05% | $21,000 |
| Worked and filed by their staff: 60% | $12,600 |
| Credited by the carriers: 75% | **$9,450 a year back to the shipper, about $788 a month** |
| Our subscription, at the ceiling of a quarter of that | **about $197 a month** ($2,362 a year) |
| Our running cost: reading $300, storage $6, hosting $60, support $175 | **$541 a year, about $45 a month**; plus $400 of onboarding help in year one |
| Our gross profit | **$1,821 a year** ($1,421 in year one) |

**Does the customer pay back what it cost to win?**
- **Won for $0** (the founders' own unpaid time): the onboarding help pays back in about **2.6 months**.
- **Won for $10,000:** about **69 months**. To repay $10,000 within 12 months, the subscription would have to be about **$912 a month**, more than the $788 a month the shipper gets back.

**The customer's hours:**
- 450 flags × 10 minutes = 75 hours a year, plus 150 disputes × 30 minutes = 75 hours. That is about **12.5 hours a month**, plus 8 hours confirming agreements in year one.
- That is inside the 20 hours a month assumed.
- At the practice audit's 58% of bills flagged it is about 30 hours; on an LTL-heavy account, about 45.
- **As dollars,** a sensitivity only: 158 hours × $36.79 = $5,813 a year, 62% of what the shipper gets back.

### 3.4 The same customer at other sizes, and at both bounds **[our calc]**

**Payback of the winning cost and onboarding help, in months** (middle values, the price at the 25% ceiling; `4_kill_conditions.md` §2.5.6, §2.5.11):

| Truckload + LTL spend a year | Won for $0 | Won for $10,000 | The same at a 3.37% flagged rate, won for $10,000 |
|---|---|---|---|
| $1M | — | 157 | 37 |
| $1.5M | 3.7 | 95 | 24 |
| $2M | 2.6 | 69 | 18 |
| $3M | — | 44 | 12 |
| $5M | — | 25 | 7 |

**The 12-month bar.** S4.5's test is that a customer repays its winning cost within 12 months. At the middle values:
- a customer won for $0 meets it from about **$0.62M** of spend;
- one won for $5,000 from about **$5.5M**;
- one won for $10,000 from about **$10.3M**.

**The ceiling test** (C23: every unmeasured input at its most favourable value). C-09 stays alive from about **$0.02M** of spend at the $0 bound and about **$0.68M** at the $10,000 bound, at a 3.37% flagged rate. At 1.66% the same figures are $0.04M and $1.38M. **So C-09 is not eliminated: it lives on unknowns.**

**The four numbers** (adapted for software as P-31, which the founders deferred on 2026-10-08):
1. **Break-even size**, our running cost covered before any winning cost: about **$0.23M** of spend.
2. **Self-serve against assisted onboarding:** $185 against $616 of our help; payback at $2M of 67 against 70 months. What onboarding costs us hardly matters; whether customers finish it does.
3. **The flagged rate that passes, by size:** the Kill / Cover / Pass table in §7.
4. **Spend at which our revenue reaches $5k a year** (about $417 a month): **$4.23M** at the middle rate, $2.68M at 1.66%, $1.32M at 3.37%.

**The revenue test** (`4_kill_conditions.md` §2.5.7):
- a $1.59M customer pays about **$1,880 a year** at the middle values;
- $1M of revenue needs about **530** such customers, and the $2.5M floor about **1,330**, which is 2.6% and 6.6% of the ~20,000 manufacturers and wholesalers with 100-499 staff;
- churn of 10-20% of revenue a year means winning a share of them again every year.

### 3.5 What the money says **[our call]**

1. **The flagged rate decides it.** It sets the money the shipper gets back, and so whether the subscription is a small scoop off the top or a cost. Nobody has measured it for mid-sized shippers.
2. **Winning the customer, not serving it, is the obstacle.** Our running cost is cents a bill. At $10,000 a customer, only very large shippers repay within a year; at $0, most shippers in the screen do. The first-customer clock measures which world we are in.
3. **Follow-through and the customer's hours decide whether the money is recovered.** A flag nobody works recovers nothing. So the software's job is to cut false flags and minutes per flag: tolerances that auto-clear small differences, flags grouped by cause, and the highlighted review screen (`software-initial-pitch.md` §7).
4. **Check inside the claim window, then monthly, and broker-billed bills as they arrive.** About half of a 12-month look-back is past the 180-day legal window. Broker terms give only 5-30 days, so those bills must be flagged and worked within days (`C09-open-questions-evidence.md` §5).
5. **Year one is bigger than later years.** Vendors report 1-3% in a first audit and 0.5-1.5% once a programme is mature (*assumed*). Under a subscription this is a **renewal risk**: the shipper gets less back for the same fee.
6. **The "scoop off the top" holds only where recoveries are well above the fee.** At $1.5M, a subscription set at a quarter of the middle recoveries is about **$148 a month**. If the shipper's flagged rate turned out to be 0.5%, that fee would be 52% of what it gets back; at 0.3%, 88%; at 0.2%, 131% (`4_kill_conditions.md` §2.5.10). Keeping the pitch true for each customer is a pricing question (Q6).

---

## 4. How freight billing works, step by step, and where we come in

### 4.1 The basic words

- **Shipper:** the company sending goods; our customer.
- **Carrier:** the trucking company.
- **Truckload (TL):** one shipper's goods fill a whole trailer, at a price per trip.
- **LTL (less-than-truckload):** several shippers' pallets share one trailer, moving through terminals. It is priced by weight and **freight class**, a number from 50 to 500 for how dense and hard to handle the goods are; a higher class costs more.
- **Broker or 3PL (third-party logistics provider):** a middleman who books carriers for the shipper and usually sends the bill itself.

### 4.2 The ten steps

| # | Step | What happens, in plain English | Where money leaks |
|---|---|---|---|
| 1 | **Rate agreement** | Shipper and carrier agree prices: a **discount** off the carrier's list price (81-90% on the public court bills, *verified*), a **minimum charge** per shipment, a **fuel surcharge** table (a percentage that moves weekly with the national diesel price), a price list for **accessorials** (extra services), and sometimes one flat class for all freight. **It is revised several times a year, and each version has an effective date** | The carrier's system bills with the wrong version, an old discount or an old fuel table |
| 2 | **Booking** | The shipper books a truck, directly or through a broker or 3PL | Broker-billed freight is harder to audit: the shipper sees the broker's price, not the carrier's |
| 3 | **Pickup** | The driver signs the **bill of lading (BOL)**: the shipper's own statement of weight, pallet count and what the goods are | The shipper's BOL is itself often wrong. One survey says about half are (*assumed*), so many later price rises are legitimate |
| 4 | **In transit (LTL)** | At a terminal the carrier may **reweigh or re-inspect** the shipment, issue a **weight and research (W&R) certificate**, and raise the price | Some reweighs are right; some aren't. **On the real ABF account, 26 of 101 bills (27% of dollars) carried a reweigh note** (*verified*) |
| 5 | **Delivery** | The receiver signs the **proof of delivery (POD)**. Extras may be added: a **liftgate** (a lift on the truck for docks without ramps), residential delivery, **detention** (a fee when the driver is kept waiting), a **lumper** (a crew paid to unload) | Extras billed that weren't done or weren't authorised. Detention appeared twice on the ABF account with no arrival or departure times printed |
| 6 | **Invoice** | The carrier sends a **freight bill**, as a PDF, on paper, or as an electronic **EDI 210** file, identified by its **PRO number** (the carrier's shipment ID) | Wrong discount, wrong fuel percentage, wrong class, duplicate bills, extras that shouldn't be there |
| 7 | **Check and approve** | Someone in logistics or AP glances at the bill. At most mid-sized firms, nobody prices it again against the agreement | **This is the gap**: nobody compares bill, agreement, BOL and POD |
| 8 | **Pay** | AP pays, typically within about 30 days | Money paid that wasn't owed |
| 9 | **Dispute** | The shipper pays less than billed or files an overcharge claim. **Federal law allows 180 days** (49 U.S.C. 13710). A federal appeals court called the deadline "not optional" (*Southern Furniture v. YRC*, 10th Cir. 2021, *verified*) | After 180 days the money is legally gone |
| 10 | **Credit** | The carrier issues a credit memo or a refund, or refuses | Prompt disputes are credited more often than old ones (60-90% against 41-51%, *assumed*) |

### 4.3 A real bill, line by line (*verified*, public court record)

**ABF Freight bill 150235531**, shipped 1 July 2024: 2 pallets, 1,837 lb. Rated at class 70 under the shipper's agreement, against the standard class of 100:

| Line | Amount | What it means | Can it be checked from the bill alone? |
|---|---|---|---|
| Linehaul, 18.37 cwt × $348.19 | $6,396.25 | The list price: hundredweight (cwt, units of 100 lb) × the rate | ✓ the arithmetic is right |
| Deficit weight, rated up to 2,000 lb | $567.55 | Billing at the next weight break because it is cheaper overall, in the shipper's favour | ✓ |
| Discount 89.5% | −$6,232.60 | The agreed discount off the list price | Arithmetic ✓. **Whether 89.5% is the agreed figure needs the agreement** |
| California compliance surcharge | $22.00 | A state surcharge on every bill | Needs the agreement |
| Lumper (unloading) | $149.10 | An unloading crew at delivery | Needs a receipt and an authorisation |
| Fuel surcharge 30.3% | $221.55 | 30.3% of the net linehaul ($731.20), not charged on the extras | Arithmetic ✓. **The right percentage needs the fuel table in force that week** |
| Dynamic discount | −$181.83 | A carrier programme | Appears in no public document |
| **Total** | **$942.02** | | The column adds up exactly ✓ |
| Note on the bill | "Reweigh - See W&R certificate" | The carrier reweighed it | **Can't be resolved without the certificate and the original BOL weight** |

**The lesson:** carriers' arithmetic is right. The money, if any, is in whether the right agreement version, fuel table, class and extras were applied, and **that can only be checked with the shipper's own documents.** The practice audit's other findings are summarised in §2.2: 38% of bills sat on a $180 minimum charge, and 13% of all dollars were accessorials.

### 4.4 Where we come in: steps 6 to 10, using the documents from steps 1, 3, 4 and 5

The software does the checking. The shipper's own staff decide and file (D-23).

1. **The customer uploads** its rate agreements (every version, with dates), fuel tables and price lists for extras. The software reads them, and the customer confirms the rules it found.
2. **The software reads** every invoice by machine, for cents a bill, and **prices it again:** what should it have cost under the agreement in force on the shipping date?
3. **It flags the exceptions:**
   - a wrong discount or an outdated agreement version;
   - a fuel percentage off the table;
   - a class different from the agreed one;
   - an extra without proof;
   - a reweigh to check against the BOL and the certificate;
   - a duplicate (matched on PRO number plus BOL, never on amount alone: on minimum-charge accounts, identical amounts on the same day are normal).
4. **The customer's own reviewer works the flags** in our software, with the evidence and any missing proof shown beside each one, and accepts or rejects each. We do no manual review.
5. **The customer files the disputes** with the carrier, through the carrier's own channel and never by paying less than billed, inside the claim window. The software shows each deadline and the proof. Helping customers file comes later.
6. **The software tracks** the disputes and the credits the customer records, and reports the money recovered. The customer pays a flat monthly subscription.

**The first product tested** (adopted by the founders 2026-10-08; `5_interview_kit.md` §6.1):
1. A free look-back on bills still inside the claim window, with the shipper's reviewer working the flags while timed.
2. Then a pilot of at least one billing cycle, flagging new bills as they arrive.
3. Then monthly checking, with broker-billed bills checked as they arrive.

The look-back proves whether the money exists; the pilot shows whether the shipper's staff work the flags. Taking over payment of the carriers is a later growth option, not part of the first product.

---

## 5. The software (a sketch, not a decision)

The project's rule is **problem first, solution second.** Nothing is built until all of these have happened:
- S6 confirms the card;
- Q6 picks the segment;
- the founders have done their freight immersion.

What C-09 would imply, **[our call]**:

| Part | What it does |
|---|---|
| **Document intake** | Takes in invoices (PDF, EDI 210, carrier portals) and the papers behind them (BOL, POD, W&R certificates) |
| **Contract library** | Holds each shipper's rate agreements, uploaded by the customer, with versions and effective dates, fuel tables and price lists for extras. The customer confirms the rules the software reads |
| **Re-pricing engine** | Prices every bill again from the agreement in force that day and compares the result with what was billed |
| **Exception queue** | Sends only the bills that need a person to **the customer's own reviewer**, with the evidence attached |
| **Dispute and claims tracker** | Shows each claim's deadline and proof. The customer files, and records credits and refusals. Help with filing comes later |
| **Reporting** | Shows the money recovered and gives the controller a monthly summary |

**Growth options**, all parked:
- **paying the carriers** for the shipper (needs a bank partner);
- **parcel audit** (card C-12, reserve list);
- **damage and loss claims** (C-10);
- **checking that the payee is genuine** (C-08's identity core).

**Decided by the founders:**
- **2026-10-03:** the first product is audit only; paying carriers comes later (§8.2, item 9). The software for it is sketched in `software-initial-pitch.md`.
- **2026-10-08, D-23:** C-09 is a software company, not an audit firm. The customer's staff review the flags and file the disputes; we employ no analysts. The customer uploads its rate agreements, the software reads them, and the customer confirms the rules (`software-initial-pitch.md` §1A).
- **2026-10-08, C28:** a flat monthly subscription.

---

## 6. Who does this job today

| Type | Examples | Who they serve | Label |
|---|---|---|---|
| **Freight audit and payment providers** | Cass, U.S. Bank, Trax, nVision Global, CTSI-Global, CT Logistics, RateLinx, TranzAct, enVista, Intelligent Audit | Mostly large shippers; size floors around $10M+ of spend | *assumed* (vendor pages; Cass 10-K *verified*) |
| **Small contingency audit firms** | "numerous small transportation bill audit firms" (Cass 10-K); mid-market pitches from Eller Audit, ValueXPA, Zero Down, US Tech Automations | Mid-sized and small shippers, often at a 50/50 split | *assumed* |
| **Funded AI entrants** | Loop ($95M Series C, April 2026; absorbed Data2Logistics in 2025), Freehand ($75M, enterprise focus) | Mostly large shippers today | *assumed* (press) |
| **LTL booking tools with audit screens** | Freightview (rated 4.7 from 743 reviews), MyCarrier, FreightPOP | Small and mid-sized manufacturers and distributors, **our segment.** **Our closest rivals:** self-serve tools where the customer's own staff work the audit screen. Theirs compares each bill with the booking quote, not the rate agreement, and covers only loads booked through them. The hypotheses missed them at first | *assumed* (reviews) · check Z |
| **Audit software where the customer approves the filing** | nShift Audit: general availability October 2026, price not yet published | Not yet known | *assumed* (its own buyer's pack) · check AS; `C09-open-questions-evidence.md` §9 |
| **Nobody** | An AP clerk matches the bill to a purchase order and pays it | The mid-market default, **[our call]**, untested | — |

**The S5 test:** if one vendor serves more than half the target customers and they are satisfied, that is a show-stopper. The booking tools' audit screens count. The interviews ask what each shipper uses today (`C09-open-questions-evidence.md` §0.3, G1).

---

## 7. The kill condition: how C-09 lives or dies

### 7.1 The lines in force (software basis): **adopted 2026-10-09**

**Adopted by the founders on 2026-10-09** (verbatim: "Adopt the Kill/Cover/Pass lines"; C29), with Tests 2 and 3. The record is `4_kill_conditions.md` §2.5.12.

From `4_kill_conditions.md` §2.5.8 and §2.5.11. They are measured on **the first real look-back** of one shipper's bills inside the claim window, with every version of its rate agreements, fuel tables, BOLs and PODs, under a mutual NDA (non-disclosure agreement), and then on **a pilot** of at least one billing cycle.

**Test 1, the leak:** what the software flags and the shipper's own reviewer accepts as wrong and provable, as a share of in-window spend. The line depends on the shipper's size:

| Shipper's truckload + LTL spend a year | **Kill** under | **Cover** from | **Pass** from |
|---|---|---|---|
| $0.5M | 0.127% | 1.26% | 19.0% |
| $1M | 0.065% | 0.70% | 9.59% |
| **$1.5M** | **0.044%** | **0.51%** | **6.44%** |
| $2M | 0.034% | 0.42% | 4.86% |
| $3M | 0.023% | 0.32% | 3.29% |
| $5M | 0.015% | 0.25% | 2.03% |

What each band means, at $1.5M:
- **Under Kill:** even a customer that cost nothing to win, with every unknown at its best, can't cover our first-year cost.
- **Kill to Cover:** at the middle values, even a free-to-win customer doesn't cover our first-year cost. C-09 continues only if the pilot shows the shipper's staff working the flags, and that can't reach the line below 0.31%.
- **Cover to Pass:** a first customer pays for itself. Whether later ones do depends on what winning them really costs. **S6 can't confirm C-09 until that cost is measured** and the rate reaches the Pass line at that cost.
- **Pass:** it repays even $10,000 of winning cost within 12 months.

**In monthly terms at $1.5M** (`4_kill_conditions.md` §2.5.11):

| Line | Shipper gets back a month | Subscription that covers our costs |
|---|---|---|
| Kill | about $50 | about $25 |
| Cover | about $290 | about $72 |
| Pass | about $3,620 | about $905 (also repays $10,000 of winning cost) |

**Test 2, access:** the rate agreements and paid invoices, uploaded under a mutual NDA.
- **Kill** if 2 of the first 3 shippers decline.
- **Conditional** if 1 of 3 declines, or if a "no" names only a security certificate (SOC 2). The condition is then that the founders accept SOC 2's company-level cost at S6.
- **Pass** if all 3 agree.

**Test 3, the customer's hours:** timed in the look-back, against the hours the shipper said it can give (20 a month if it gave no figure).
- **Kill** if the queue would need more than twice that, even counting only the flags the reviewer accepted.
- **Conditional** if it is over capacity as measured but within it once rejected flags are removed. It continues only if the pilot shows that tolerances and grouping bring it within capacity. It is also conditional if our reading cost is above $0.50 a bill: it continues only if the pilot finds a cheaper way to read the bills.
- **Pass** if it fits as measured and our reading cost is at or under $0.50 a bill.

**Why the lines sit there [our call]:**
- **Kill** is the ceiling test (C23) applied to the shipper measured: below it nothing could work, even at the $0 bound.
- **Cover** is where a free-to-win customer covers our first-year cost at the middle values.
- **Pass** is S4.5's 12-month payback bar at the $10,000 bound. It is above every figure on file, so a pass would be a genuine surprise, and the first look-back will most likely land between Cover and Pass. There, follow-through, the customer's hours and the measured winning cost decide.
- **The lines are stated against what the shipper gets back,** at a price ceiling of a quarter of it, so no price decision is built into them.

**Verdict:**
- **Any kill** stops C-09's S5 work. Its conversations move to C-19, and it stays an S6 backup.
- **A conditional with no kill** lets it continue, but S6 can't confirm it until the condition is met.
- **All pass** sends it to the 1-10 re-score, with the measured inputs.
- **The founders decide**, together, on the evidence in `5_log.md` §7.

**Adopted 2026-10-09:** the frozen lines in §7.2 are struck through in `4_kill_conditions.md` §2.4, and the change is logged as C29 in `submarket_selection.md` §9. **Look-backs may now start,** once the data-handling rules (D-18) are settled.

### 7.2 The old frozen lines: superseded 2026-10-09

**Frozen on 2026-09-22** for an audit service (`4_kill_conditions.md` §2.4): kill under 0.75%, pass at 1.3%. Their basis went with D-23, and the founders replaced them with §7.1 on 2026-10-09 (C29). They are kept word for word in §13.11, and struck through in `4_kill_conditions.md` §2.4.

---

## 8. Open questions, stated and not settled

> **The full list of questions, with how to ask each one, what proves it, the web's verdict so far and whom to ask:** `C09-open-questions-evidence.md` §0, the master list (2026-10-09). The web evidence on each, after an adversarial check, is in the rest of that file. It settles nothing here.

### 8.1 What the interviews must prove

A number counts as **proven** only when measured on the customer's own documents. What an interviewee says is a **claim**, never enough for a kill test. The register of every model number is in `handoff_s5_interviews.md` §6.2; results go in `5_log.md` §10. The register as this section held it on 2026-10-08 is kept word for word in §13.8.

**The ten questions that decide C-09** (the founders' own four marked F1-F4; IDs as in the register):

| # | The question | Sets | Decides |
|---|---|---|---|
| 1 | **F1:** "What % of cargo is overcharged?" Asked as the last wrong bill, and the last 12 months' wrong bills in dollars against spend | A09-01 | **Test 1:** Kill, Cover or Pass. Proven only by the look-back |
| 2 | How much do you spend on truckload, LTL and parcel a year, and how much goes through brokers? | A09-09, A09-14 | Which row of the Kill / Cover / Pass table applies; which claim window |
| 3 | **F2:** "Who currently handles auditing this in your firm?" Who looked into the last wrong bill, how long it took, what tool they used, and how satisfied they are | A09-15, A09-16; H09-08 | Follow-through (Test 1's middle band); the show-stopper |
| 4 | **F4:** "How many audits have you submitted?" Both the disputes and claims filed with carriers in 12 months (how many credited, how fast) and any outside audits (what they found, what happened the year after) | A09-03, A09-13 | The credited share; renewal |
| 5 | **F3:** "How much money a year do you think you are being overcharged?" Logged as a **belief**, followed by "What makes you say that?" | — | How the pitch lands; compared with the look-back later |
| 6 | Will you upload last month's invoices and your rate agreements under an NDA? Which carriers' agreements say the rates are confidential? | A09-11 | **Test 2** |
| 7 | How many hours did your team spend on freight bills last month? (And at the look-back: how many can you give the queue?) | A09-16 | **Test 3** |
| 8 | Where do your rate agreements live, in what form, for how many carriers, and how often do they change? | A09-08, A09-17 | Test 3 (onboarding time) |
| 9 | What do you pay today to check freight bills, and who approves a software subscription, up to what amount? | A09-04; H09-05 | Whether a subscription can be bought; the price test |
| 10 | Do your contracts or broker terms set a claims deadline, and how soon after paying do you notice a wrong bill? | A09-10 | In-window spend, which Test 1 divides by |

**The rules for asking** (kit §1, from *The Mom Test*):
1. Ask about **the last time**, not "usually".
2. Get the number with its unit and period.
3. Ask to see the document in the same conversation.
4. Write down the exact words and figures.
5. Never ask "would you…" for a number.
6. When a claim and a document disagree, **the document wins.**

**Our own numbers, which customers can't prove:**
- **the cost of winning a customer** (A-X1): bounded at $0-$10,000 and measured by the **first-customer clock**, from the first outreach to the first paying customer, with founder hours and cash logged per channel (`5_log.md` §1);
- **the customer's wage** (A-X2): no longer our cost; it values the customer's hours, as a sensitivity only;
- **machine cost per bill** (A-X3, about $0.10): recorded when the look-back's scripts run;
- **our support, hosting and platform costs:** desk values from the re-run (`4_kill_conditions.md` §2.5.3); one look-back can't measure them.

**The carrier side (5 interviews, kit §5.2):**
- how they handle a shipper who pays less than billed or disputes a bill, and what makes them accept or refuse a shipper's own dispute (H09-C1);
- how they treat an outside firm's claims (H09-C4). This matters only once we help customers file;
- whether they would pay for faster payment (H09-C2). Parked, since version 1 is audit only.

### 8.2 Decisions: what is settled, and what is still open

**Listed here, not settled.** Each open point will be taken in the decision-record format (your words verbatim, then the evidence for and against, then decided together). Where the files carry a suggestion, it is shown as **[our call], not decided.**

| # | Point | What it is | Where it is written | Status |
|---|---|---|---|---|
| 1 | **D-14:** P-23 to P-26 | Process proposals: one interview counting for two shipper cards (P-23); an early stop (P-24); **the 1-10 scoring anchors fixed before any evidence (P-25)**; counterparty sides off the per-side rows (P-26) | `5_validation.md` §10 | **Open.** P-25 must be settled before any evidence arrives |
| 2 | **D-15** | Prices for the savings assessment and pilots | `5_validation.md` §10.1; kit §6 | **Open in part.** The founders plan the look-back free (2026-10-08). A test price for the subscription is still theirs to set before the first close |
| 3 | **D-16** | Interview incentives and paid recruiting | `5_validation.md` §10.1 | **Open.** $2-4k, capped at $10k **[our call], not decided** |
| 4 | **D-17** | Register for the 2026 3PL Study | same | **Open.** Optional |
| 5 | **D-18** | Data handling: a mutual NDA first; raw files outside the project folder and deleted afterwards; bank details removed at source | same; kit §1.3 | **Open.** Needed before any real data arrives. No data-privacy lawyer has been found yet (`C09-open-questions-evidence.md` §0.4) |
| 6 | **D-19** | The time box for S5 | same | **Open.** The original window (21 Sep-16 Oct) has slipped; needs new dates |
| 7 | D-20 | The NMFTA licence question | same | Moot since C-11 was eliminated; to be recorded as closed |
| 8 | **C-09 kit changes** | Screen on 20-499 staff and $250k+ of freight spend; the bill-checker as the main interviewee; the sampling grid; the screener and messages | `6_focused_target.md` §1.4, §7.3, §7.6 | **Partly applied:** the assumption questions (2026-09-22), "who works the flags" (2026-10-08), and the founders' four and the Kill / Cover / Pass questions (2026-10-09). The screen still reads 100-499 staff |
| 9 | **C-09's first product** | Audit only, or audit plus paying the carriers | `6_focused_target.md` §1.4 point 2 | **Decided 2026-10-03: audit only** ("I have decided the first rendition will just be an audit machine, we can do payments later"); `software-initial-pitch.md` §1 |
| 10 | **C-20's freed interview slots** | 5 broker and 5 importer slots: to C-19, to C-09, or dropped | `4_kill_conditions.md` §7.4 | **Open** |
| 11 | **The wording of C-09's kill rule** | The frozen rule says a killed C-09's interviews go to "C-11 and C-19"; with C-11 gone that means C-19. The proposed rule already says C-19 | `4_kill_conditions.md` §2.4 note, §2.5.8 | **Open:** confirm the wording |
| 12 | **D-23: who does the review work** | An audit service or software | `software-initial-pitch.md` §1A | **Decided 2026-10-08: a software company** ("We have no analysts, this is a software company … they just review and file currently") |
| 13 | **The fee form (C28)** | Does a subscription meet the fee rule? | `4_kill_conditions.md` §2.5.10 item 1; `submarket_selection.md` §9 | **Decided 2026-10-08: a subscription** ("We market it as a scoop off the top of the money they will make, but it will not be contingent on them actually making money"). The price stays Q6 |
| 14 | **The customer's hours** | Capacity or dollars | §2.5.10 item 2 | **Decided 2026-10-08: "Capacity."** |
| 15 | **The look-back design** | The shipper's reviewer works the flags while timed, then a pilot | §2.5.10 item 3; kit §6.1 | **Decided 2026-10-08:** "The suggested design sounds good." |
| 16 | **What Test 1 measures** | True overcharges or flagged dollars | §2.5.10 item 4 | **Decided 2026-10-08: "Flagged"** |
| 17 | **The cost of winning a customer** | The figure the lines assume | §2.5.10 item 6; §2.5.11 | **Bounded 2026-10-08:** $0 and $10,000, adjusted as the first-customer clock reports ("Mark these stand in figures as the upper and lower bounds, then we will adjust as we know more") |
| 18 | **Adopt the new lines (C29)** | The Kill / Cover / Pass lines and Tests 2-3 in §7.1 | `4_kill_conditions.md` §2.5.8, §2.5.11, §2.5.12 | **Decided 2026-10-09: adopted** ("Adopt the Kill/Cover/Pass lines"). §2.4's frozen lines are struck through |
| 19 | **P-31** | The four numbers adapted for software, for the S4 template | §2.5.10 item 5 | **Deferred:** "Answer it later, make a note of this." To settle before C-19's software re-run |

**Also left for later, on purpose:** the price itself, the segment, and the minimum customer size are Q6 decisions, after the sub-market is confirmed. The old cells of this table are kept in §13.8.

---

## 9. Your job

**The split:**
- **The founders** decide everything and do every human contact: outreach, interviews and getting documents.
- **Claude** prepares, drafts, analyses, keeps the logs, runs the look-back's scripts and arithmetic and drafts the re-score for you to confirm. **No one on our side judges a bill** (D-23).
- **Claude contacts no one.**

**In order:**

1. **Settle what has to come before any evidence** (§8.2). The kill lines are adopted (item 18, 2026-10-09). Still to settle:
   - the scoring anchors (P-25);
   - data handling (D-18), including finding a data-privacy lawyer.
2. **Recruit, and start the first-customer clock** on the day of the first outreach (`5_log.md` §1). Log founder hours and cash per channel. Claude drafts messages and lists; you send them.
   - **C-09 shippers:** 5 interviews with a controller, AP lead or logistics manager at a US manufacturer or distributor, ideally $1.5M+ of truckload and LTL spend. A paid panel is the only route likely to deliver 5 quickly (check Y), then LinkedIn and warm introductions.
   - **C-09 carriers:** 5 billing leads at carriers with 5-250 trucks, found through the FMCSA carrier register (the federal list of registered carriers).
3. **Run the interviews** with the kit (`5_interview_kit.md` §5.1-5.2) and the question list (`C09-open-questions-evidence.md` §0): past events with amounts, no pitching before the incident questions. At the end, **ask for the documents under an NDA.** The real ABF bill in §4.3 is the show-and-tell.
4. **Write notes within 24 hours** and hand them over. Claude turns them into the evidence log, the hypothesis log and the assumption register.
5. **Run the look-back as adopted** (kit §6.1), free of charge, once the data-handling rules (D-18) are settled:
   1. ask how many hours a month the shipper can give the queue, and record it first;
   2. run the software's rules as scripts on its in-window bills and **every version** of its rate agreements, fuel schedules, BOLs and PODs, on your local demo or a cheap cloud host. Keep the raw files outside the project folder;
   3. the shipper's reviewer confirms the rules read from each agreement;
   4. the reviewer works every flag on screen while timed;
   5. then the pilot, for at least one billing cycle.
6. **Decide.** Apply the adopted lines to what was measured. Then come the 1-10 re-score and S6: confirm C-09, switch to C-19, or go back to the reserve list.

**The single most important result:** one real mid-sized shipper's bills, flagged by the software against its own agreements and worked by its own reviewer. That flagged rate, with the pilot's follow-through, decides whether C-09 is a business. Everything before it was estimating.

---

## 10. The alternative: C-19, in brief

**The pitch:** "Walmart, Target, Home Depot, Amazon and others deduct fines from what they pay you, for late or short deliveries, missing ship notices, and goods they say never arrived. Some of those fines are wrong. We find the wrong ones, attach the proof and dispute them before each retailer's window closes. You pay us only a share of what comes back."

**How it works:**
1. The retailer sends a purchase order.
2. The supplier ships and sends an **ASN (advance ship notice)**.
3. The truck must arrive inside its delivery appointment.
4. The retailer scores the delivery **OTIF (on time, in full)** and fines misses, about 3% of the goods' cost at Walmart.
5. The deductions appear in a remittance file (EDI 812/820) or the retailer's portal.
6. The supplier disputes within a short window: about 15 days at Lowe's, about 4 weeks at Home Depot, 30 days at Amazon.

We would come in at steps 5 and 6. The evidence chain uses the same delivery documents as C-09.

**Where it stands:**
- **S4.5 verdict: "not provable from the web"** (`4_5_profitability.md`).
- The typical small supplier recovers about **0.01%** of sales, which is not a profitable customer.
- A high-leak minority of about **260-1,300 suppliers** would each pay about **$35-52k a year** **[our calc]**.
- **The incumbent SupplyPike (owned by SPS) already has about 500-550 customers at about $33-38k each**, roughly the size of that minority. Glimpse reports 200+ brands.

**Its kill lines** (frozen, `4_kill_conditions.md` §4.7):
- measured on a supplier screened at **1% or more** of sales in non-trade deductions;
- **kill** if provably wrong deductions are under **0.05%** of sales;
- **pass** at **0.22%** for a $50M supplier;
- plus access and cost tests shaped like C-09's.

**Its big question:** are SupplyPike's and Glimpse's customers satisfied? Reviewers complain about denied disputes and coverage gaps, but SupplyPike rates 4.9 on Capterra.

**Not yet re-run as software.** The pitch and kill lines above are still on the service basis: a share of what comes back, with our own staff checking and disputing deductions. The founders' rule that we are a software company with no analysts applies to every card, and C-19 is flagged for the same re-run before S6 compares the two (`software-initial-pitch.md` §1A; `4_kill_conditions.md` §4 banner).

---

## 11. Glossary

| Term | Meaning |
|---|---|
| **3PL** | Third-party logistics provider: a firm that runs shipping or warehousing for others |
| **Accessorial** | An extra-service charge on a freight bill: liftgate, residential delivery, detention, lumper |
| **AP** | Accounts payable: the team that pays a company's bills |
| **ASN** | Advance ship notice: an electronic notice telling the retailer what is coming |
| **BOL** | Bill of lading: the shipping document signed at pickup, with the shipper's stated weight and goods |
| **Broker** | A middleman who books carriers for shippers and usually bills the shipper itself |
| **CAC** | Customer acquisition cost: what it costs to win one customer. For C-09, bounded at $0-$10,000 until the first customer is timed |
| **Capacity** | The hours a month a customer's staff can give the flag queue. Kill Test 3 sets the measured workload against it |
| **Carrier** | The trucking company that moves the freight |
| **Contingency audit** | An outside firm checks bills already paid, claims overcharges back, and keeps a share of what returns; paid nothing if nothing comes back. This is how audit firms work. It is not our model: we sell software for a flat monthly subscription |
| **Controller** | The finance manager who runs accounting at a mid-sized firm |
| **Cover line** | The middle of kill Test 1's three lines: the flagged rate from which a customer won for $0 covers our first-year cost (0.51% at $1.5M of spend) |
| **cwt** | Hundredweight: 100 lb, the unit LTL rates are quoted in |
| **Deficit weight** | Billing a light shipment at the next weight break when that is cheaper |
| **Detention** | A fee charged when a driver is kept waiting at pickup or delivery |
| **EDI 210** | The standard electronic freight invoice larger carriers send |
| **EDI 812 / 820** | Electronic credit and debit adjustments, and payment remittances, from retailers |
| **FAK** | "Freight all kinds": one agreed class applied to a range of goods |
| **FAP** | Freight audit and payment: a provider that checks every bill before payment and pays carriers for the shipper (Cass, U.S. Bank) |
| **First-customer clock** | The time, founder hours and cash from the first outreach to the first paying customer, logged in `5_log.md` §1. It replaces the $0-$10,000 bounds once measured |
| **Flagged rate** | The dollars on bills the software flags and the customer's reviewer accepts as wrong and provable, as a share of in-window spend. What kill Test 1 measures |
| **Follow-through** | The share of flagged dollars the customer's staff actually dispute or get corrected. Measured only in a pilot |
| **Freight class** | A number (50-500) for how dense and hard to handle goods are; higher costs more on LTL |
| **Fuel surcharge** | A percentage added to the bill, set weekly from a table tied to the national diesel price |
| **Gross profit per customer** | Our subscription revenue from a customer minus the direct cost of serving it: machine reading, storage, hosting and support |
| **Kill / Cover / Pass** | Kill Test 1's three proposed lines, by shipper size: below Kill nothing could work; from Cover a customer won for $0 covers our first-year cost; from Pass it repays even $10,000 of winning cost within 12 months |
| **Liftgate** | A lift on the back of a truck, for deliveries without a loading dock |
| **Linehaul** | The base transport charge, before discount, fuel and extras |
| **Look-back** | Re-checking bills already paid, for overcharges still inside the claim window. For C-09, the software's rules run on one shipper's bills while its own reviewer works the flags, timed |
| **LTL** | Less-than-truckload: several shippers' freight shares one trailer |
| **Lumper** | A crew paid to unload a truck at delivery |
| **Minimum charge** | The floor a bill can't go below, whatever the discount works out to |
| **NDA** | Non-disclosure agreement |
| **OTIF** | On time, in full: a retailer's delivery score; misses are fined |
| **Pilot** | At least one billing cycle after the look-back, in which the software flags new bills as they arrive and the shipper's dispute log shows follow-through |
| **POD** | Proof of delivery: the receiver's signed receipt |
| **PRO number** | The carrier's shipment ID, also the freight bill number |
| **Reweigh / W&R certificate** | The carrier re-weighs a shipment and issues a weight-and-research certificate, often raising the price |
| **SaaS** | Software as a service: software the customer uses online and pays for as it goes. C-09's model: the software flags the bills, the customer's own staff review and file, and the customer pays a flat monthly subscription |
| **Short-pay** | Paying less than the billed amount, to dispute part of it |
| **Subscription** | C-09's fee: a flat amount a month, not dependent on what the shipper recovers (C28). The price is a Q6 decision |
| **Truckload (TL)** | One shipper's goods fill a whole trailer |
| **Value share** | The model's assumed ceiling on the price: at most a quarter of what the shipper gets back. A ceiling, not a share we take |

---

## 12. Sources

All in this project; each holds its own primary sources and labels.
- **Where the project stands, and the S5 brief:** `CLAUDE.md`; `handoff_s5_interviews.md` (§3 the cards, §4 open decisions, §5 kill conditions, §6 assumption register).
- **The decision and C-09 in full:** `research/selection_runs/run-01/6_decision.md` §5; `research/selection_runs/run-01/6_focused_target.md` (§1 decision record, §2 one page, §4 money, §5-§7 interviews).
- **The money model and kill condition:** `research/selection_runs/run-01/4_kill_conditions.md` §2.5 (C-09 on the software basis: §2.5.3 inputs, §2.5.4 the $2M example, §2.5.8 the tests, §2.5.10 the founders' answers, §2.5.11 the Kill / Cover / Pass lines); §2.4 (the frozen lines); §4 (C-19), §7 (D-22).
- **D-23 and the software model:** `software-initial-pitch.md` §1A (the decision record) and the rest of that file (the software); `handoff_c09_software_rerun.md` (the re-run's brief, done).
- **The software re-run's evidence (2026-10-08):** `research/s5_check_AQ_c09_customer_review.md`, `research/s5_check_AR_c09_software_cost.md`, `research/s5_check_AS_c09_market_models.md`, and their adversarial reviews.
- **The open questions, the web's answers and the contacts:** `C09-open-questions-evidence.md` (§0, the master question list).
- **The practice audit and the real bill:** `research/s5_practice_audit_public_invoices.md` §3.
- **Money and documents checks:** `research/s5_check_X_c09_money.md`, `research/s5_check_AA_c09_cost_to_serve.md`, `research/s5_check_AB_c09_private_recoveries.md`, `research/s5_check_AC_c09_example_invoices.md`.
- **Reach and public voice:** `research/s5_check_Y_c09_reach.md`, `research/s5_check_Z_c09_voice.md`.
- **C-19:** `research/selection_runs/run-01/4_5_profitability.md`.
- **The interview tools:** `research/selection_runs/run-01/5_interview_kit.md`, `5_validation.md`, `5_log.md`.

---

## 13. Superseded, kept for the record

*Added 2026-10-09.* Passages from this file that no longer fit the strategy, moved here **word for word** when the file was rewritten (founders: "Clean rewrite + appendix"). They are kept so every change can be retraced. Old headings are shown in bold so they don't read as sections of this file. **Nothing here is current.**


### 13.1 From the header and §1

> **Written 2026-10-02 for the founders to read and come back to.** It gathers in one place what run 01 has learned about the front-runner, C-09.
>
> **Update 2026-10-08: D-23, a software company, not an audit firm.** The founders decided that C-09 is software sold as a service. The software catches the errors and raises them to the **customer's own reviewers**, who review the bills and file the disputes. We employ no analysts and do no manual review, and help with filing disputes comes later. The record, verbatim, is in `software-initial-pitch.md` §1A.
> - **Superseded:** the money model in §3 and the kill condition's basis in §7 were built for an audit service (our analysts review, we file, we keep 25%). They are struck through or marked "service basis" where they appear.
> - ~~**Pending:** the kill test is re-run on the software basis in `handoff_c09_software_rerun.md`.~~ **Re-run 2026-10-08, proposed and not adopted:** `research/selection_runs/run-01/4_kill_conditions.md` §2.5, summarised in §3.2 and §7 below. The frozen lines stay in force until the founders adopt new ones, and no look-back starts before then.
> - **The founders' answers, 2026-10-08** (`4_kill_conditions.md` §2.5.10): a subscription, hours as capacity, the look-back design, and Test 1 on flagged dollars are decided. P-31 is deferred. The acquisition cost is ~~open~~ ~~deferred until the first customer is timed~~ bounded at $0-$10k until the first customer is timed (`4_kill_conditions.md` §2.5.11), so the new lines are not adopted yet.

- **The aim:** find a freight sub-market where software cuts a cost we can measure, and charge a fee that is a share of the saving. The revenue floor is $2.5M a year (`CLAUDE.md`, Constraints).
- **The desk research is done. No customer has been interviewed.** The project is in **S5, validation by interviews.** The evidence log (`research/selection_runs/run-01/5_log.md`) is empty, and every item on the S5 gate tracker reads zero.
- **The schedule has slipped.** The interview window was planned for 21 Sep to 16 Oct. As of 2 Oct no outreach has gone out.
- **Also live (2026-10-08):** `handoff_c09_software_rerun.md`, the brief to re-run C-09's kill test as a software company (D-23).

### 13.2 From §2

| Reason | Detail | Label / source |
|---|---|---|
| **The biggest prize** | A central fee pool of **$209M a year**, 3-6 times any other finalist. **95,579** US manufacturers (57,309) and wholesalers (38,270) have 20-499 staff | pool **[our calc]** on *assumed* inputs; firm counts *verified* (Census) · `6_focused_target.md` §2 |
| **The fee fits the rule exactly** | ~~"Contingency audit" is already a normal contract in freight: an outside firm checks paid bills, claims the overcharges back, and keeps 25-50% of what comes back. Our fee would be a slice of refunded money. That is what "the fee has to come out of savings" means~~ *Superseded by D-23 (2026-10-08):* we are a software company, not an audit firm, so the contingency-audit contract is no longer our model. **The fee form is now open:** a share of recovered dollars or a subscription, modelled side by side in the re-run (`handoff_c09_software_rerun.md`). The saving is still recovered overcharges, so the fee can still come out of savings. Whether a subscription meets the fee rule ("our fee can be a share of it") is the founders' call; the price itself is Q6 | *assumed* (industry practice) · `4_scorecard.md` §3 (strongest fee case of the five, scored on the contingency basis) |

| Concern | Detail | Label / source |
|---|---|---|
| **Every new number moved against it** | The business needs carriers to overbill about **1.3%** of spend (§7). Every neutral measurement found is **under 0.5%**: USDA's 1977 survey of farm co-operatives found **0.45%**; federal post-payment audits find about **0.07%**. The only figures above 1% are vendors' own case studies, **0.8-4.2%** (median 1.8%), and five of the six are large shippers in a first-year audit | USDA, GSA *verified*; vendor cases *assumed* · check X, check AB |
| **Small LTL bills are expensive to serve** | The real account had **2.21 invoices per $1,000** of spend (the model assumed 1.5) and **58% of bills needing a person** (the model assumed 15%). ~~At those values the model loses money at any plausible overcharge rate~~ *Superseded by D-23 (2026-10-08):* that loss was the cost of **our** reviewers. Under the software model the person is the customer's own staff, so these values set the customer's workload (about 175 hours a year at a $2M shipper at 58%, **[our calc]**) and our machine-reading cost, not our labour. The re-run sets what they mean for the card | **[our calc]** · `4_kill_conditions.md` §2.3 |

**Reading [our call]:** the desk has shown that one design is thin: a deep look-back for a small, LTL-heavy shipper, ~~reviewed by US staff~~ *(superseded by D-23, 2026-10-08: under the software model the customer's own staff review the flags, so their hours, not ours, are what the "58% needing a person" row now measures)*. It has **not** measured the one number the business rests on, the overcharge rate on a mid-sized shipper's own bills. Only the interviews can.

### 13.3 §3, as it stood on 2026-10-08

**3. The pitch, and the money in one customer**

**3.1 The pitch**

> ~~**"Your trucking companies overcharge you on some of their bills, and nobody at your company has the time to catch it. Give us your bills and your rate agreements. We check every bill against what you agreed to pay and dispute the wrong ones with the carrier, inside the 180-day legal window. When money comes back, we keep 25% and you keep 75%. If nothing comes back, you pay nothing."**~~

*Superseded by D-23 (2026-10-08):* that pitch sold an audit service (we check, we dispute, we keep 25%). C-09 is now software, and the customer's own staff review and file. A software pitch, drafted **[our call]**, with no price in it (the price is Q6):

> **"Your trucking companies overcharge you on some of their bills, and nobody has the time to check them all. Our software checks every bill against your own rate agreements and shows your team the wrong ones, with the proof beside them, so they can dispute them inside the claim window."**

Never sell it as "saves your team time": the saving is recovered overcharges, not paid hours (the founders' rule, D-22).

- **Who buys:**
  - the **controller** (the finance manager at a mid-sized firm) or the **AP lead** (accounts payable, the team that pays suppliers' invoices);
  - at a US manufacturer or distributor with about 20-499 staff;
  - spending roughly **$1.5M or more** a year on truckload and LTL freight (the screen the model suggests, **[our call]**).
- **Who uses it:** the person who actually checks the bills, often in logistics rather than finance (check Y: 22 of 47 job postings put the job in logistics, 6 in AP). *Under D-23 this person works the flags and files the disputes; we do not.*
- **What they get:**
  - money back they would not otherwise collect;
  - ~~no fee unless something comes back;~~ *(superseded by D-23: the fee form is open, a share of recoveries or a subscription; see §3.2)* *2026-10-08: the founders chose a subscription, not contingent on recoveries; the price is Q6.*
  - over time, carriers who know their bills are being checked.

**3.2 The money chain**

**On the software basis (D-23, 2026-10-08).** The numbers are re-derived in ~~`handoff_c09_software_rerun.md`~~ `research/selection_runs/run-01/4_kill_conditions.md` §2.5 (proposed 2026-10-08, not adopted); this is the shape:
- **Money recovered for the customer** = freight spend × overcharge rate × share the software flags × **share of flags the customer's staff work and file (follow-through, A09-15)** × share the carrier credits, **plus** errors caught before payment (prevented rather than refunded).
- **Our revenue, two forms side by side:**
  - (a) a share of the money recovered;
  - (b) a subscription.

  Which form, and at what level, is Q6.
- **Our cost per customer:**
  - machine reading of every bill;
  - storage and hosting;
  - support, including help with self-serve onboarding;
  - any licence per customer;
  - plus platform costs (a security certification, development) and the cost of winning the customer ($5-15k on check A's benchmark), spread across customers.
- **The customer's own cost is their staff's hours:** flags (false ones included) × minutes per flag, plus disputes they file, plus confirming the rules the software read from their agreements. Those hours decide whether they buy and whether the flags get worked.

**Who now pays for what [our calc], from the service model's own numbers below:**
- Of the old **$1.12 a bill** of cost to serve, **$0.10 (machine reading) stays ours**.
- **$1.02 becomes the customer's own staff time:** a person on 15% of bills for 6 minutes ($0.55), plus disputes on 5% of bills at $9.30 ($0.47).
- The old **$400 fixed cost** becomes the customer's onboarding time (loading and confirming their agreements), plus our support and platform costs, which the re-run estimates.
- **At a $2M customer** (1.5 bills per $1,000, 6 minutes each, before disputes), the customer's staff need about **45 hours a year** if 15% of bills are flagged, and about **175 hours** at the practice audit's 58%.

**What the re-run found (2026-10-08; `4_kill_conditions.md` §2.4-§2.5 for the detail) [our calc]:**
- **A $2M customer, worked through:**
  - 3,000 bills a year;
  - 1.05% of spend flagged and accepted ($21,000);
  - 60% of that worked and filed by their staff, and 75% credited by the carriers, so **about $9,450 recovered a year**.
- **Our cost** is about **$541 a year** (reading $300, hosting $60, support $175, storage $6), plus $400 of onboarding help in the first year.
- **Our cost is no longer the problem; the cost of winning the customer is.** To repay a $10,000 acquisition cost within 12 months we would need $10,941 from this customer in year one. That is more than it recovers, so **no fee form can do it at this rate**:
  - a share would have to be 116%;
  - a subscription would have to be $912 a month.

  At a 25% share our revenue is about $2,360 a year, and the acquisition cost pays back in about 69 months.
- **Where it works [our calc]:**
  - at the government auditors' highest flagged rate (3.37%) the same customer pays back in about 18 months;
  - at the central rate, a customer needs about $10M of spend to pay back in 12 months.
- **The customer's hours:** about 12.5 hours a month at $2M, within the 20 hours we assume a shipper can give. At the practice audit's 58% of bills flagged it is 30-45 hours.
- **It stays alive:** with every unmeasured input at its best, it passes from about $0.35M of spend (the ceiling test, C23).

**The service basis, superseded by D-23 (2026-10-08).** Kept for the record; ~~the re-run is pending in `handoff_c09_software_rerun.md`~~ the re-run is in `4_kill_conditions.md` §2.5.

~~**Our fee from one customer = freight spend × overcharge rate × share we catch × share the carrier actually credits × our fee share.**~~
~~**Our gross profit from that customer = our fee − our cost to serve them.**~~
**Whether the customer is worth winning = that gross profit against what it costs to win them** (the customer acquisition cost, $5-15k on check A's benchmark). *This test still holds under D-23.*

| Link | Model value | Label |
|---|---|---|
| Overcharge rate (billed wrong in the carrier's favour, provable) | 1.5% | **[our call]**: every neutral figure is under 0.5% |
| Share we catch | 70% | **[our call]**: GAO 1992 found one professional audit catches 72-78% of what two find (*verified*) |
| Share the carrier credits | 75% | **[our call]**: 60-90% when disputed promptly, 41-51% when old (*assumed*) |
| ~~Our fee share~~ | ~~25%~~ | *assumed*: contingency firms take 25-50%. *Superseded by D-23: the fee form and level are open (share or subscription)*; *2026-10-08: a subscription; the level is Q6* |
| Invoices per $1,000 of spend | 1.5 | **[our calc]**: an LTL bill averages $347.81 at Saia (*verified*); the real ABF account ran 2.21 |
| Share of invoices needing a person | 15% | **[our call]**: the real ABF account ran 58% |
| Machine reading per invoice | $0.10 | prices *verified* (AWS Textract $0.01 a page), per invoice **[our calc]** |
| ~~Person reviewing~~ | ~~6 minutes at $36.79 an hour (US) or $12 (offshore)~~ | wage *verified* (BLS), minutes *assumed*. *Superseded by D-23: the person is the customer's own staff; the offshore option is moot* |
| ~~Disputes~~ | ~~5% of invoices, $9.30 each~~ | *assumed*. *Superseded by D-23: the customer files the disputes* |
| ~~Fixed cost per customer a year~~ | ~~$400~~ | *assumed*. *Superseded by D-23: the customer's onboarding time plus our support and platform costs* |

Source: `research/selection_runs/run-01/4_kill_conditions.md` §2.2.

**3.3 Worked example **[our calc]****

> **Service basis, superseded by D-23 (2026-10-08).** §3.3-§3.5 cost **our** reviewers and **our** dispute filing, at US or offshore wages. Under D-23 those are the customer's hours, and our cost is software (see the who-pays-what split in §3.2). The worked example, the four numbers and the readings are re-derived in `handoff_c09_software_rerun.md`. They are kept here, with the headline claims struck through, so the reasoning can be retraced.

**A shipper spends $2M a year on truckload and LTL freight.** Using the middle values above, which are guesses rather than evidence:

| Step | Amount |
|---|---|
| Carriers overbill 1.5% | $30,000 |
| We catch 70% of it | $21,000 |
| Carriers credit back 75% of what we dispute | **$15,750 returned to the shipper** |
| Our 25% fee | **$3,938** (the shipper keeps $11,812) |
| Our cost: about 3,000 invoices read by machine, 450 of them looked at by a person, 150 disputes, plus $400 fixed | about $3,745 |
| ~~**Our gross profit from this customer**~~ | ~~**about $190 a year**~~ |

~~A customer worth $190 a year never pays back the $5-15k it costs to win. **With offshore reviewers** the same customer leaves about **$2,250** a year, paying back in about 2-7 years.~~ *Superseded by D-23: $3,445 of the $3,745 cost was our people (reviews and disputes) and the $400 fixed; that work is now the customer's. Our profit on the software basis comes from the re-run.*

**3.4 The same customer at other sizes and rates **[our calc]****

Gross profit a year, at US review wages, with every other input at the middle value:

| Truckload and LTL spend a year | Overbilled 0.5% | Overbilled 1.5% | Overbilled 3% |
|---|---|---|---|
| $1M | −$1,416 | −$104 | +$1,865 |
| $2M | −$2,433 | +$193 | +$4,130 |
| $3M | −$3,449 | +$489 | +$6,395 |

(Our fee per $1,000 of spend is $131.25 × the overcharge rate. Our cost per $1,000 is $1.67 at US wages, plus $400 a year fixed.)

**The four numbers that sum it up** (`4_kill_conditions.md` §2.3), *service basis, superseded by D-23; re-derived in the re-run*:
1. ~~**Break-even customer size:** $1.35M of spend with US reviewers; about $0.3M offshore.~~
2. ~~**Overcharge rate needed just to cover the work:** 1.28% with US reviewers; 0.46-0.50% offshore.~~
3. **Spend at which our fee reaches $5k a year** (check A's level for selling direct): $2.5M at 1.5%; $1.3M at 3%; $5.1M at 0.75%. *These hold only for a 25% share; under a subscription our revenue no longer depends on spend.*
4. ~~**The stress case** from the practice audit (2.21 invoices per $1,000, 58% needing a person): **never profitable at 1.5%**, even offshore.~~ *Under D-23 the stress case is the customer's workload, about 175 hours a year at a $2M shipper.*

*Software basis (D-23), proposed as P-31 in `4_kill_conditions.md` §2.5.6 [our calc]:*
1. **Break-even size** (our running cost covered, before acquisition cost): **about $0.23M** of spend.
2. **Self-serve against assisted onboarding:** $185 against $616 of our help; payback at $2M of 67 against 70 months. Onboarding cost hardly matters; whether customers finish it does.
3. **The flagged rate at which a customer repays a $10,000 acquisition cost within 12 months**, at a 25% value share: **6.44% at $1.5M**, 4.86% at $2M, 2.03% at $5M.
4. **Spend at which our revenue reaches $5k a year:** $4.23M at the central rate, $1.32M at 3.37%. The same for both fee forms at a 25% value share.

**3.5 What the money says **[our call]****

1. **The whole business turns on the overcharge rate.** At 3% it is a real business; at 0.5% it loses money on every customer. Nobody has measured it for mid-sized shippers. *Still true under D-23: the overcharge rate sets the money the customer recovers, and so whether their hours and our fee are worth it.*
2. ~~**Where the review work is done matters more than any other cost.** Machine reading costs cents; the person costs dollars.~~ *Superseded by D-23: the person is the customer's own staff. The point that survives is that the software's job is cutting the share of bills a person must touch and the minutes each takes.*
3. **Audit inside the claim window, then monthly.** A 12-month look-back loses money at every size, because about half the bills are already past the 180-day legal window and can't be collected. *Under D-23 the window still decides what can be recovered; broker-billed freight with 5-10-day windows needs checking as each bill arrives (`C09-open-questions-evidence.md` §5).*
4. **Year one is bigger than later years.** Vendors report 1-3% in a first audit and 0.5-1.5% once a programme is mature (*assumed*). The ongoing fee is thinner than the first year suggests. *Under a subscription this becomes a renewal risk rather than a thinner fee.*
5. ~~**Shippers heavy on small LTL bills cost about twice as much to serve per dollar,** because their bills are a third the size.~~ *Superseded by D-23: they cost the customer's staff about twice as many flags per dollar; our own cost per bill is the $0.10 of machine reading.*

### 13.4 From §4: §4.4 as it stood

**4.4 Where we come in: steps 6 to 10, using the documents from steps 1, 3, 4 and 5**

1. **Load** each shipper's rate agreements (every version, with dates), fuel tables and price lists for extras.
2. **Read** every invoice by machine, for cents a bill, and **price it again:** what should it have cost under the agreement in force on the shipping date?
3. **Flag the exceptions:**
   - a wrong discount or an outdated agreement version;
   - a fuel percentage off the table;
   - a class different from the agreed one;
   - an extra without proof;
   - a reweigh to check against the BOL and the certificate;
   - a duplicate (matched on PRO number plus BOL, never on amount alone: on minimum-charge accounts, identical amounts on the same day are normal).
4. ~~**A person reviews the exceptions**, with the evidence. This is where the cost is.~~ *Superseded by D-23 (2026-10-08):* **the customer's own reviewer works the flags** in our software, with the evidence and any missing proof shown beside each one. We do no manual review.
5. ~~**File the disputes** with the carrier, inside the 180 days.~~ *Superseded by D-23:* **the customer files the disputes** with the carrier, inside the claim window. The software shows the deadline and the proof. Helping them file comes later.
6. ~~**Track the credits**, and charge our share of what actually comes back.~~ *Superseded by D-23:* **the software tracks the disputes and credits the customer records** and reports the money recovered. How we charge is open (a share or a subscription, Q6).

**The first product tested is an audit inside the 180-day window, then a monthly check before payment.** The first check, on bills paid in the last 180 days, proves the money exists. The monthly check catches errors before they are paid. Taking over payment of the carriers is a later growth option, not part of the first product.

### 13.5 From §5

What C-09 would imply, **[our call]**:

| Part | What it does |
|---|---|
| **Document intake** | Takes in invoices (PDF, EDI 210, carrier portals) and the papers behind them (BOL, POD, W&R certificates) |
| **Contract library** | Holds each shipper's rate agreements with versions and effective dates, fuel tables and price lists for extras |
| **Re-pricing engine** | Prices every bill again from the agreement in force that day and compares the result with what was billed |
| **Exception queue** | Sends only the bills that need a person to ~~a reviewer~~ **the customer's own reviewer** (D-23), with the evidence attached |
| **Dispute and claims tracker** | ~~Prepares claims, files them before the 180-day deadline, and records credits and refusals~~ *D-23:* shows each claim's deadline and proof; **the customer files**, and records credits and refusals. Help with filing comes later |
| **Fee and reporting** | Shows money recovered, ~~bills our share,~~ and gives the controller a monthly summary. *D-23: the fee form is open (share or subscription, Q6)*; *2026-10-08: a subscription (founders)* |

**Growth options**, all parked:
- **paying the carriers** for the shipper (needs a bank partner);
- **parcel audit** (card C-12, reserve list);
- **damage and loss claims** (C-10);
- **checking that the payee is genuine** (C-08's identity core).

**Decided 2026-10-03 (founders):** the first product is audit only; paying carriers comes later (§8.2, item 9). The software for it is sketched in `software-initial-pitch.md`.

**Decided 2026-10-08 (founders, D-23):** C-09 is a software company, not an audit firm. The customer's staff review the flags and file the disputes; we employ no analysts. The customer uploads its rate agreements, the software reads them, and the customer confirms the rules (`software-initial-pitch.md` §1A).

### 13.6 From §6

| Type | Examples | Who they serve | Label |
|---|---|---|---|
| **LTL booking tools with audit screens** | Freightview (rated 4.7 from 743 reviews), MyCarrier, FreightPOP | Small and mid-sized manufacturers and distributors, **our segment.** The hypotheses missed this at first. *Under D-23 these are our closest rivals: self-serve tools where the customer's own staff work the audit screen. Theirs compares each bill with the booking quote, not the rate agreement, and covers only loads booked through them* | *assumed* (reviews) · check Z |

**The S5 test:** if one vendor serves more than half the target customers and they are satisfied, that is a show-stopper. The interviews ask what each shipper uses today.

### 13.7 §7, as it stood on 2026-10-08

**7. The kill condition: how C-09 lives or dies**

> **Basis superseded by D-23 (2026-10-08); ~~re-run pending~~ re-run proposed on 2026-10-08, not adopted (`4_kill_conditions.md` §2.5).** These lines were derived for an audit service: Test 1's 1.3% is where **our** US review covers its cost, its middle band escapes through offshore review or a 45% share, and Test 3 measures **our** review cost. Under D-23 the review and the disputes are the customer's time. The kill test is re-run on the software basis in `handoff_c09_software_rerun.md`. **The lines below stay frozen and in force until the founders adopt new ones** (then a `submarket_selection.md` §9 entry), and **no look-back starts before then.**
>
> **The proposed new lines (2026-10-08, not adopted; `4_kill_conditions.md` §2.5.8), in brief:**
> - **Test 1, the leak:** what the software flags and the shipper's own reviewer accepts as wrong and provable, as a share of in-window spend. The line depends on the shipper's size:
>
>   | Shipper's spend | Kill under | Pass at or over |
>   |---|---|---|
>   | $1.5M | ~~0.78%~~ 0.044% | 6.44% |
>   | $2M | ~~0.59%~~ 0.034% | 4.86% |
>   | $5M | ~~0.24%~~ 0.015% | 2.03% |
>
>   **Between the lines, C-09 continues only if a pilot of at least one billing cycle shows the customer's staff working and filing enough of the flags.**
> - **Test 2, access:** as now. A "no" that names only a security certificate (SOC 2) is treated as a cost question, not a refusal.
> - **Test 3, the customer's hours:** timed in the look-back, against the hours the shipper says it can give.
>   - **Kill** if it would need more than twice those hours, even with false flags removed.
>   - **Pass** if it fits.
>
> **Why the pass line is so high:** it now includes repaying the cost of winning the customer within 12 months, which the old 1.3% did not. ~~The kill line is the rate below which no customer of that size could repay even a $5,000 acquisition cost within 12 months, with every unmeasured input at its best.~~ *2026-10-08: with the acquisition cost set as bounds ($0 to $10,000, `4_kill_conditions.md` §2.5.11), the kill line is the rate below which even a customer that costs nothing to win could not cover our first-year cost, with every unmeasured input at its best.*

**Frozen on 2026-09-22** (`4_kill_conditions.md` §2.4). The lines were fixed before any measurement, so the result can't be argued into a pass afterwards. They are measured on **the first real look-back** of one shipper's paid bills: at least three months, with every version of its rate agreements, fuel schedules, BOLs and PODs, under a mutual NDA (non-disclosure agreement), with our hours recorded.

| Test | Kill | Conditional | Pass |
|---|---|---|---|
| **1. The leak:** overcharges billed wrong and **provable from the documents**, as a share of spend still inside the claim window | **under 0.75%** | 0.75-1.3%; continues only if a 45% share is accepted, or offshore review is allowed, or measured cost is well under the model | **1.3% or more** |
| **2. Access:** the rate agreement and paid invoices under an NDA | **2 of the first 3 shippers decline** | 1 of 3 declines | all 3 agree (or 1 declines and a replacement agrees) |
| **3. Cost, measured:** gross profit at a $1.5M customer and a 25% share, from the look-back's own timings | **negative under US and offshore wages** | negative US, positive offshore | positive at US wages |

**Why the lines sit there:**
- **0.75%** is the middle of what mature audit programmes find (0.5-1.5%). A first audit below it predicts an ongoing rate under what even offshore review needs.
- **1.3%** is where US-staffed review covers its own cost at a 25% share.
- **2 of 3 on access:** without the agreement an audit is only arithmetic, and the arithmetic is already right.

**Verdict:**
- **Any kill** stops C-09's S5 work. Its interviews move to C-19, and it stays a backup.
- **A conditional with no kill** lets it continue, but it can't be confirmed until the condition is met.
- **All pass** sends it to the 1-10 re-score.
- **The founders decide**, together, on the evidence in `5_log.md` §7.

### 13.8 §8, as it stood on 2026-10-08 (the assumption register and the decisions table)

**8. Open questions, stated and not settled**

> **Web evidence on these questions, after an adversarial check, and people to ask (2026-10-07):** `C09-open-questions-evidence.md`. It settles nothing here.

**8.1 What the interviews must prove (the C-09 assumption register)**

Every model number in plain words. A number counts as **proven** only when measured on the customer's own documents. What an interviewee says is a **claim**, never enough for a kill test. Full register: `handoff_s5_interviews.md` §6.2.

| ID | What we assumed | Value now | What to ask (about the last time, with amounts) | What proves it |
|---|---|---|---|---|
| **A09-01** | **Share of in-window spend the carriers billed wrongly, provably** | **1.5%** **[our call]** | "Tell me about the last freight bill that turned out to be wrong." "In the last 12 months, how many bills did you dispute, and for how many dollars?" "Have your bills ever been audited? What did it find?" | **The look-back** on their invoices, agreements, fuel schedules, BOLs and PODs |
| A09-02 | Share of real overcharges ~~we catch~~ **the software flags** (D-23) | 70% | "Of the wrong bills you found last year, how many did you catch before paying?" | Our flagged list against their own dispute log |
| A09-03 | Share the carrier credits | 75% | "Of the bills you disputed last year, how many came back, for how much, how fast?" "Tell me about the last dispute a carrier refused" | Their credit memos or dispute log |
| A09-04 | ~~The fee share they'll accept~~ **The fee form and level they'll accept: a share or a subscription** (D-23) | ~~25% (also testing 45% and a per-invoice price)~~ *open; both forms modelled side by side in the re-run; price is Q6*; *2026-10-08: the founders chose a subscription, so this row is now the level a shipper accepts* | "Does anyone audit your bills now? What do they charge?" "What software do you pay for today, and who approved the budget?" Then the price test, once rewritten after the re-run | **A signed agreement or letter of intent.** A spoken yes is only a claim |
| A09-05 | Invoices per $1,000 of spend | 1.5 (real ABF account 2.21) | "How many freight invoices a month? What's your yearly spend, split truckload, LTL and parcel?" | Invoice count and total in the look-back |
| A09-06 | Share of invoices needing a person. *D-23: now the **customer's** workload, counted as flags (false ones included), not our cost* | 15% (ABF 58%) | "How many bills carry extras (liftgate, detention, lumper, a reweigh note)?" | Count in the look-back |
| A09-07 | Minutes per review, cost per dispute. *D-23: now the **customer's** minutes per flag and per dispute* | 6 min, $9.30 | "How many hours a week does your team spend checking and disputing bills, for how many bills?" | ~~**Our own timed hours** in the look-back~~ *D-23:* **the customer's reviewer, timed** in the look-back |
| A09-08 | Fixed cost per customer. *D-23: the customer's onboarding time plus our support and platform costs* | $400 a year | "How many carriers? How many rate agreements? How often do rates and fuel tables change?" | ~~Hours spent loading their agreements~~ *D-23:* the customer's minutes to upload and confirm their agreements (A09-17) |
| A09-09 | Their truckload and LTL spend | screen favours $1.5M+ | Spend by mode, in bands; share booked through brokers | Their AP payment export |
| A09-10 | Share of a look-back still inside the claim window | ~50% of 12 months | "Do your contracts have a claims clause, like 'within 90 days'?" "How soon after paying do you notice a wrong bill?" | The clause; invoice dates |
| **A09-11** | **They will share the agreement and invoices under an NDA** | Test 2 | "If I asked for last month's paid invoices and the rate agreements, what format would they be in?" Then ask | Files received: count yes and no among the first 3 |
| ~~A09-12~~ | ~~Offshore review is acceptable~~ | ~~needed only in Test 1's middle band~~ | ~~"Would your company allow invoice data, under an NDA, to be reviewed outside the US?"~~ | ~~A written yes or no~~ *Moot under D-23 (2026-10-08): we employ no reviewers, onshore or offshore* |
| A09-13 | First-year finds fall later | mature 0.5-1.5% *assumed* | "If you've been audited before, what happened to errors the year after?" | A prior audit report |
| A09-14 | Share through brokers, on minimum charges, with reweighs | ABF: 38% of bills on the minimum, 26 of 101 with a reweigh note | "What share of your freight goes through a broker or 3PL?" | Counts in the look-back |
| **A09-15** *(new, D-23)* | **Follow-through:** the share of real flags the customer's staff actually work **and** file | none yet | "The last time a freight bill looked wrong, who at your company looked into it, and how long did it take?" "What happened to it: was a dispute filed, and what came back?" | Their dispute log and credit memos over a pilot of at least one billing cycle; one watched look-back reads 100%, so it can't prove this |
| **A09-16** *(new, D-23)* | **The customer's hours:** the hours a month their staff can give the flag queue (capacity) | none yet; the desk puts the need at about 45-175 hours a year at a $2M shipper **[our calc]** | "Has anyone used an audit screen in your booking tool? When did they last clear it?" "Last month, how many hours went on checking freight bills, and by whom?" | Timesheets or the queue's own record in a pilot |
| **A09-17** *(new, D-23)* | **Self-serve onboarding:** the share of their rate agreements the software reads correctly, and the customer's minutes to confirm the rules | none yet | "When your last rate agreement or fuel table changed, who updated it where, and how long did it take?" | The look-back: agreements read without correction, and the customer's timed minutes to confirm |

**Our own numbers, which customers can't prove:**
- **the cost of winning a customer** ($5-15k): logged from founder hours and recruiting spend;
- **loaded wages**: checked against job postings. *Under D-23 a wage is no longer our cost; it values the customer's hours, as a sensitivity only;*
- **machine cost per document** (about $0.10): recorded when the look-back runs;
- *added under D-23:* **our support, storage and platform costs per customer**: estimated in the re-run (`handoff_c09_software_rerun.md`).

**The carrier side (5 interviews, kit §5.2):**
- how they handle a shipper who pays less than billed, and how they treat an audit firm's claims (H09-C1, C4). *Under D-23 the shipper files its own claims in version 1, so the audit-firm question matters only once we help with filing;*
- whether they would pay for faster payment (H09-C2). Carriers already pay 1% or more for early payment through U.S. Bank (*assumed*, check Z).

**The rules for asking** (kit §1, from *The Mom Test*):
1. Ask about **the last time**, not "usually".
2. Get the number with its unit and period.
3. Ask to see the document in the same conversation.
4. Write down the exact words and figures.
5. Never ask "would you…" for a number.
6. When a claim and a document disagree, **the document wins.**

**8.2 Decisions still to make before the first call**

**Listed here, not settled.** Each will be taken in the decision-record format (your words verbatim, then the evidence for and against, then decided together). Where the files already carry a suggestion, it is shown as **[our call], not decided.** *Update 2026-10-03: item 9 has since been decided by the founders (audit only first).* *Update 2026-10-08: item 12, D-23, has been decided by the founders (a software company, not an audit firm).*

| # | Open point | What it is | Where it is written | Suggestion on file |
|---|---|---|---|---|
| 1 | **D-14:** P-23 to P-26 | Process proposals: one interview counting for two shipper cards (P-23); an early stop (P-24); **the 1-10 scoring anchors fixed before any evidence (P-25)**; counterparty sides off the per-side rows (P-26) | `5_validation.md` §10 | P-25 must be settled before any evidence arrives |
| 2 | **D-15** | Prices for the savings assessment and pilots | `5_validation.md` §10.1; kit §6 | — |
| 3 | **D-16** | Interview incentives and paid recruiting | `5_validation.md` §10.1 | $2-4k, capped at $10k **[our call], not decided** |
| 4 | **D-17** | Register for the 2026 3PL Study | same | Optional |
| 5 | **D-18** | Data handling: a mutual NDA first; raw files outside the project folder and deleted afterwards; bank details removed at source | same; kit §1.3 | Needed before any real data arrives |
| 6 | **D-19** | The time box for S5 | same | The original window (21 Sep-16 Oct) has slipped; needs new dates |
| 7 | D-20 | The NMFTA licence question | same | Moot since C-11 was eliminated; to be recorded as closed |
| 8 | **C-09 kit changes** | Screen on 20-499 staff and $250k+ of freight spend; the bill-checker as the main interviewee; the sampling grid; the screener and messages | `6_focused_target.md` §1.4, §7.3, §7.6 | Partly applied (the assumption questions, 2026-09-22) |
| 9 | **C-09's first product** | Audit only, or audit plus paying the carriers | `6_focused_target.md` §1.4 point 2 | **Decided 2026-10-03 by the founders: audit only** ("I have decided the first rendition will just be an audit machine, we can do payments later"). See `software-initial-pitch.md` §1 |
| 10 | **C-20's freed interview slots** | 5 broker and 5 importer slots: to C-19, to C-09, or dropped | `4_kill_conditions.md` §7.4 | — |
| 11 | **The wording of C-09's kill rule** | It says a killed C-09's interviews go to "C-11 and C-19"; with C-11 gone that means C-19 | `4_kill_conditions.md` §2.4 note | Confirm the wording |
| 12 | **D-23: who does the review work** | An audit service (our analysts review and file) or software (the customer's staff review and file) | `software-initial-pitch.md` §1A | **Decided 2026-10-08 by the founders: a software company** ("We have no analysts, this is a software company … they just review and file currently"). The kill test is re-run in `handoff_c09_software_rerun.md`. Still open within it: whether a subscription meets the fee rule, and the fee form and price (Q6) |

**Also left for later, on purpose:** the price itself, the segment, and the minimum customer size are Q6 decisions, after the sub-market is confirmed.

### 13.9 §9, as it stood on 2026-10-08

**9. Your job**

**The split:**
- **The founders** decide everything and do every human contact: outreach, interviews and getting documents.
- **Claude** prepares, drafts, analyses, keeps the logs, runs the look-back arithmetic and drafts the re-score for you to confirm.
- **Claude contacts no one.**

**In order:**

1. **Settle the decisions in §8.2.** The scoring anchors (P-25) and data handling (D-18) have to come first.
2. **Recruit.** Claude drafts messages and lists; you send them.
   - **C-09 shippers:** 5 interviews with a controller, AP lead or logistics manager at a US manufacturer or distributor, ideally $1.5M+ of truckload and LTL spend. A paid panel is the only route likely to deliver 5 quickly (check Y), then LinkedIn and warm introductions.
   - **C-09 carriers:** 5 billing leads at carriers with 5-250 trucks, found through the FMCSA carrier register (the federal list of registered carriers).
3. **Run the interviews** with the kit (`5_interview_kit.md` §5.1-5.2): past events with amounts, no pitching before the incident questions. At the end, **ask for the documents under an NDA.** The real ABF bill in §4.3 is the show-and-tell.
4. **Write notes within 24 hours** and hand them over. Claude turns them into the evidence log, the hypothesis log and the assumption register.
5. **Get one shipper's real data:**
   - 1-3 months of paid bills;
   - **every version** of its rate agreements;
   - fuel schedules, BOLs and PODs.

   Keep the raw files outside the project folder. ~~Claude runs the look-back and times it, which gives the first real cost-to-serve number.~~ *Superseded by D-23 (2026-10-08):* Claude runs the look-back's arithmetic; the suggested design **[our call]**, for the founders to adopt in the re-run, is that **the shipper's own reviewer works the flags while timed**. That gives the first real figures for the customer's minutes per flag and the share of flags they accept. **No look-back starts until the founders have adopted the re-run's new lines.**
6. **Decide.** Apply the frozen kill lines (§7) to what was measured *(under D-23: the lines the founders adopt from the re-run)*. Then come the 1-10 re-score and S6: confirm C-09, switch to C-19, or go back to the reserve list.

**The single most important result:** one real mid-sized shipper's bills, checked against its own agreement. That provable overcharge rate decides whether C-09 is a business. Everything before it was estimating.

### 13.10 From §11 and §12

| Term | Meaning |
|---|---|
| **Contingency audit** | An outside firm checks bills already paid, claims overcharges back, and keeps a share of what returns; paid nothing if nothing comes back. *Since D-23 (2026-10-08) this is how audit firms work, not our model: we sell software* |
| **Gross profit per customer** | Our fee from a customer minus the direct cost of serving them. *Under D-23 that cost is software and support, not people reviewing bills* |
| **SaaS** | Software as a service: software the customer uses online and pays for as it goes. C-09's model since D-23: the software flags the bills, and the customer's own staff review and file |

- **The money model and kill condition:** `research/selection_runs/run-01/4_kill_conditions.md` §2 (C-09), §4 (C-19), §7 (D-22).
- **D-23 and the re-run (2026-10-08):** `software-initial-pitch.md` §1A (the decision record); `handoff_c09_software_rerun.md` (the brief to re-run the kill test as a software company).

### 13.11 Replaced when the founders adopted the new lines (2026-10-09, C29)

**From the header:**

> **The strategy now** (decided by the founders on 2026-10-08; …

> 5. **The cost of winning a customer is bounded at $0 to $10,000** until the first customer is timed. The kill test's new lines, **Kill / Cover / Pass** (§7), are **proposed, not adopted,** so no look-back starts yet. P-31 is deferred.

**From §1:**

- The kill-test re-run briefed in `handoff_c09_software_rerun.md` is done: its lines are in `4_kill_conditions.md` §2.5, proposed and not adopted.

**From §3.2:**

All figures are from the software re-run, `4_kill_conditions.md` §2.5 (proposed 2026-10-08, not adopted).

**From §7.1:**

**7.1 The proposed lines (software basis): proposed 2026-10-08, not adopted**

From `4_kill_conditions.md` §2.5.8 and §2.5.11.

**On adoption,** the frozen lines in §7.2 are struck through in `4_kill_conditions.md` §2.4 and a `submarket_selection.md` §9 entry is made (C29). **No look-back starts before then.**

**From §7.2, the whole subsection:**

**7.2 The frozen lines: formally in force, basis superseded**

**Frozen on 2026-09-22** (`4_kill_conditions.md` §2.4), before any measurement, so that a result can't be argued into a pass afterwards. They stay in force until the founders adopt new ones. **But their basis is gone:** they were derived for an audit service, where Test 1's 1.3% is where *our* US reviewers cover their cost, the middle band escapes through offshore review or a 45% share, and Test 3 measures *our* review cost. D-23 removed all three. Their reasoning is kept in §13.7.

| Test | Kill | Conditional | Pass |
|---|---|---|---|
| **1. The leak:** overcharges billed wrong and **provable from the documents**, as a share of spend still inside the claim window | **under 0.75%** | 0.75-1.3%; continues only if a 45% share is accepted, or offshore review is allowed, or measured cost is well under the model | **1.3% or more** |
| **2. Access:** the rate agreement and paid invoices under an NDA | **2 of the first 3 shippers decline** | 1 of 3 declines | all 3 agree (or 1 declines and a replacement agrees) |
| **3. Cost, measured:** gross profit at a $1.5M customer and a 25% share, from the look-back's own timings | **negative under US and offshore wages** | negative US, positive offshore | positive at US wages |

**From §8.2:**

| # | Point | What it is | Where it is written | Status |
|---|---|---|---|---|
| 18 | **Adopt the new lines (C29)** | The Kill / Cover / Pass lines and Tests 2-3 in §7.1 | `4_kill_conditions.md` §2.5.8, §2.5.11 | **Open. No look-back starts before adoption** |

**From §9:**

1. **Settle what has to come before any evidence** (§8.2):
   - adopt, or change, the new kill lines (item 18). No look-back starts before;
   - the scoring anchors (P-25);

5. **Run the look-back as adopted** (kit §6.1), free of charge, once the lines are adopted:
