# Run 01, S5: the evidence log

> **Stage S5 of `submarket_selection.md` §4. Opened 2026-09-16. Empty until the first interview.**
> **What this is:** the record of S5's primary evidence (§10, added 2026-09-22, tracks every model assumption from claimed to proven). It holds recruiting counts, the interview register, the hypothesis log in Aulet's format (R15), and the costed incidents, commitments, data sources, assessments and survey votes that the gate counts.
> **How to fill it:** use the counting rules in `5_interview_kit.md` §1.4 and the note template in §8. Update the gate tracker in `5_validation.md` §8 from the totals here.
> **Privacy:** use pseudonymous IDs only. Names, firms, contact details and raw customer files stay outside this folder (`5_interview_kit.md` §1.3).

**ID scheme.** `I-[card][side]-[nn]`:

| Code | Side |
|---|---|
| `09S` | C-09 shippers |
| `09C` | C-09 carriers |
| `11S` | C-11 shippers |
| `11W` | C-11 counterparty worker |
| `19S` | C-19 suppliers |
| `19W` | C-19 counterparty worker |
| `20B` | C-20 brokerages |
| `20I` | C-20 importers |

An interview that counts for two shipper cards (P-23, if adopted) keeps one ID and is listed under both.

---

## 1. Recruiting funnel (W1 evidence)

One row per side × channel, updated at each step. Log dead channels too: a channel that fails is W1 evidence. S5 step 1: "How easily people are recruited is itself evidence for reachability (W1)."

**Metrics** (from check V §10.3, **[our call]**):
- **Reached:** delivered and not bounced, or the call was answered.
- **Positive:** agreed to talk, or referred you to the right person.
- **Qualified held:** the meeting took place and the person met the screen.
- **Paid:** the interview came through a panel or expert network.
- **Cost:** fees + incentive + list or subscription cost, pro rata.

| Side | Channel | Paid? | Attempted | Reached | Replies | Positive | Booked | Held | Qualified held | First contact | First qualified meeting | Incentive $ | Cash cost $ | Referrals | Founder hours |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 09S | | | | | | | | | | | | | | | |
| 09C | | | | | | | | | | | | | | | |
| 11S | | | | | | | | | | | | | | | |
| 11W | | | | | | | | | | | | | | | |
| 19S | | | | | | | | | | | | | | | |
| 19W | | | | | | | | | | | | | | | |
| 20B | | | | | | | | | | | | | | | |
| 20I | | | | | | | | | | | | | | | |

**Per-side totals.** The W1 reading follows the rules in `5_validation.md` §7.2 (P-25).

| Side | Qualified held | Reply rate | Days to first qualified meeting | Top channel's share | Paid share | Cost per qualified interview | W1 reading |
|---|---|---|---|---|---|---|---|
| 09S | 0 | — | — | — | — | — | — |
| 09C | 0 | — | — | — | — | — | — |
| 11S | 0 | — | — | — | — | — | — |
| 19S | 0 | — | — | — | — | — | — |
| 20B | 0 | — | — | — | — | — | — |
| 20I | 0 | — | — | — | — | — | — |
| 11W | 0 | — | — | — | — | — | n/a (counterparty) |
| 19W | 0 | — | — | — | — | — | n/a (counterparty) |

**C-09 first-customer clock** *(founders, 2026-10-08: "we can mark how long it took to gain our first customer from beginning of outreach then we can use that number for further expansions")*:
- first outreach (date): —
- first paying customer, signed (date): —
- days elapsed: —
- founder hours to that date (the 09S rows' Founder hours column): —
- cash spent to that date (the 09S rows' Cash cost column): —

---

## 2. Interview register

| ID | Date | Card(s) | Side | Role | Staff band | Industry / type | Channel | Screen met | Costed incident | Commitment types | Notes § |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

---

## 3. Hypothesis log (R15's format)

The hypotheses and the rows they move are defined in `5_validation.md` §3. "Validated?" takes one of four values: **yes** · **with hesitancy** · **no** · **untested**. A finding needs a quote or number, the interview ID(s), and the date.

### 3.1 C-09 · Auditing and paying freight bills
| ID | Hypothesis (short) | Validated? | Finding | Next step |
|---|---|---|---|---|
| H09-01 | Bills are paid largely as billed; checking is manual or absent | untested | | |
| H09-02 | Overpaid 1-3% of truckload + LTL spend | untested | | Savings assessment (kit §6.1) |
| H09-03 | Recent costed overcharges are common | untested | | |
| H09-04 | The NMFC dockets added LTL corrections to their bills | untested | | |
| H09-05 | The controller decides; contingency needs no budget line | untested | | *D-23 (2026-10-08): a subscription is also modelled and would need a budget line; ask who approved the last software purchase (kit §5.1)* |
| H09-06 | A 25% share of recoveries is accepted | untested | | Price test (kit §6.1). *D-23: the price test waits for the re-run; the fee form (share or subscription) is modelled both ways, the price is Q6* |
| H09-07 | Invoices, agreements and PODs can be pulled within a week | untested | | |
| H09-08 | No audit-and-pay provider; any audit is a yearly contingency look-back | untested | | *D-23: also record any self-serve audit screen in use (Freightview, MyCarrier, FreightPOP) and when it was last cleared* |
| H09-09 | The paying half takes months; audit-first is adoptable now | untested | | |
| H09-10 | Reached through finance channels, not logistics | untested | | Funnel §1 |
| H09-11 | Defensive shipper groups feel it as much as cyclical ones | untested | | |
| H09-C1 | Carriers lose time and cash to short-pays and disputes | untested | | |
| H09-C2 | Carriers would be paid through a third-party rail, and pay for speed | untested | | |
| H09-C3 | Carriers produce PODs and invoices quickly | untested | | |
| H09-C4 | Carriers don't resist automated audit more than human audit | untested | | *D-23: in version 1 the shipper's own staff file the claims, so the test is whether carriers accept the shipper's software-prepared disputes (kit §5.2)* |
| H09-12 | Mid-sized shippers' staff will work a flagged-bill queue: they clear most flags within the claim window (*added 2026-10-08, D-23*) | untested | | The two "who works the flags" questions (kit §5.1); the timed look-back; a pilot |

### 3.2 C-11 · LTL class, reweigh and reclass disputes
| ID | Hypothesis (short) | Validated? | Finding | Next step |
|---|---|---|---|---|
| H11-01 | Corrections hit a meaningful share of small shippers' LTL shipments | untested | | Measured correction rate (kit §6.2) |
| H11-02 | Avoidable corrections are 2-5% of LTL spend | untested | | |
| H11-03 | Most corrections are accepted, or passed to the 3PL rep | untested | | |
| H11-04 | Dockets 2025-1 / 2026-1 raised corrections or confusion | untested | | |
| H11-05 | Disputes with evidence win credits in a meaningful share of cases | untested | | Dispute run (kit §6.2) |
| H11-06 | Shippers can get the carrier's inspection record within the window | untested | | Check T §3-4 |
| H11-07 | A contingency is accepted; a subscription over ~$150/month is not | untested | | Price test |
| H11-08 | Shippers booking via a 3PL can't dispute directly | untested | | |
| H11-09 | Small shippers don't hold ClassIT+; the licence cost matters | untested | | Check T §7 |
| H11-10 | Machinery and furniture shippers feel it as much as fabricated metals | untested | | |
| H11-11 | Origin evidence (per-pallet BOL dimensions, spec sheets) exists but isn't used | untested | | Kit §5.3 probe |
| H11-W1 | Carriers grant credits on third-party evidence at a similar rate | untested | | Worker interviews |
| H11-W2 | A correction rate can be stated from records, not feel | untested | | |
| H11-W3 | The evidence that wins and the windows that bite are known | untested | | |

### 3.3 C-19 · Retailer OTIF fines and deductions
| ID | Hypothesis (short) | Validated? | Finding | Next step |
|---|---|---|---|---|
| H19-01 | Fines and non-trade deductions arrive monthly; recent costed cases are common | untested | | |
| H19-02 | Non-trade deductions are ¼-½% of sales; 20-40% removable | untested | | Savings assessment (kit §6.3) |
| H19-03 | Small suppliers write off many deductions as not worth disputing | untested | | |
| H19-04 | Most still use no third-party tool; SPS/SupplyPike users are not all satisfied | untested | | Check U §5; show-stopper test |
| H19-05 | The 2024 retailer rule changes raised fines or workload | untested | | |
| H19-06 | Payer = saver; a ~25-30% contingency is accepted | untested | | Price test |
| H19-07 | PODs and carrier timestamps can be had within the window | untested | | |
| H19-08 | Portal / 812 / 820 exports can be shared | untested | | |
| H19-09 | The buyer population is ≥ 10,000 firms (Cohen's Plausible row) | untested | | Check U §4 |
| H19-10 | Reached through supplier communities or credit networks | untested | | Funnel §1 |
| H19-W1 | Retailers reverse invalid deductions at a known rate | untested | | Worker interviews |
| H19-W2 | Written rules and practice differ in known ways | untested | | |
| H19-W3 | Retailers don't block third-party portal access | untested | | |

### 3.4 C-20 · Import entries
| ID | Hypothesis (short) | Validated? | Finding | Next step |
|---|---|---|---|---|
| H20-01 | Classification and keying are 30-50% of entry time, and removable | untested | | Time study (kit §6.4) |
| H20-02 | De minimis and the refunds raised workload; brokers are capacity-bound | untested | | |
| H20-03 | Brokers keep the time saving rather than cutting price | untested | | F5 probe |
| H20-04 | Brokers would adopt a co-pilot that does not file | untested | | |
| H20-05 | Reasonable-care liability limits automated classification | untested | | |
| H20-06 | No ABI vendor's AI feature already satisfies them | untested | | Show-stopper test |
| H20-07 | A per-entry price well below labour cost is accepted | untested | | Price test |
| H20-08 | Brokerages are quick to reach (W1 = 1) | untested | | Funnel §1 |
| H20-09 | Small brokerages' entry volume held in 2022-23; tariff swings raise it | untested | | |
| H20-I1 | Small importers name costly entry incidents | untested | | |
| H20-I2 | Some importers would buy directly (self-file or a tool) | untested | | |
| H20-I3 | Importers have unclaimed IEEPA refunds | untested | | Refund look-back (kit §6.4) |

---

## 4. Costed incidents (gate item 2: ≥3 on the paying side)

| Card | ID | Month | What happened | Amount | Who paid | Outcome |
|---|---|---|---|---|---|---|
| | | | | | | |

---

## 5. Commitments (gate item 3: ≥2 on the paying side)

Types: 1 introduction · 2 data shared · 3 assessment agreed · 4 paid / signed.

| Card | ID | Date | Type | Detail (roles only) |
|---|---|---|---|---|
| | | | | |

---

## 6. Data sources (gate item 4: a named source + ≥1 interviewee willing to share)

| Card | Data source that would measure the saving | Form | Who holds it | Willing to share (IDs) |
|---|---|---|---|---|
| C-09 | | | | |
| C-11 | | | | |
| C-19 | | | | |
| C-20 | | | | |

---

## 7. Savings assessments and price tests (gate item 5; steps 3-4)

> *Note, 2026-10-08 (D-23):* for C-09 the "Hours spent" column now records **the customer reviewer's timed minutes** (per flag and to confirm the rules), not ours; we employ no reviewers. No C-09 look-back starts before the founders adopt the re-run's kill lines (`handoff_c09_software_rerun.md`). C-19's column is flagged for the same change.

| Card | ID | Data received | Measured result | Hours spent | Price offered | Answer | Reason if not done |
|---|---|---|---|---|---|---|---|
| C-09 | | | overpayment rate: | | | | |
| C-11 | | | correction rate: · disputes won: | | | | |
| C-19 | | | non-trade % of sales: · invalid share: | | | | |
| C-20 | | | minutes per entry: · removable share: | | | | |

---

## 8. Survey votes (step 5)

Points: 1st = 3, 2nd = 2, 3rd = 1. Keep interview votes and online votes apart; only interview votes come from screened people.

### 8.1 Shipper list (kit §7.1)
| Issue | Interview points | Online points | Split notes (role / size / LTL / big-box) |
|---|---|---|---|
| 1 Wrong freight bills (C-09) | 0 | 0 | |
| 2 LTL reweigh / reclass (C-11) | 0 | 0 | |
| 3 Retailer OTIF fines / deductions (C-19) | 0 | 0 | |
| 4 Rates | 0 | 0 | |
| 5 Tracking | 0 | 0 | |
| 6 Detention | 0 | 0 | |
| 7 Claims | 0 | 0 | |
| 8 Tariffs and customs | 0 | 0 | |
| 9 Fraud and theft | 0 | 0 | |
| 10 Spend visibility | 0 | 0 | |
| 11 Write-ins | — | — | |

### 8.2 Carrier list (kit §7.2)
| Issue | Points | Split notes |
|---|---|---|
| 1 Paid on time | 0 | |
| 2 Short-pays and disputes | 0 | |
| 3 Detention not paid | 0 | |
| 4 Loads and rates | 0 | |
| 5 Broker fraud | 0 | |
| 6 Insurance | 0 | |
| 7 Paperwork to get paid | 0 | |
| 8 Factoring fees | 0 | |
| 9 Drivers | 0 | |
| 10 Write-ins | — | |

### 8.3 Customs list (kit §7.3)
| Issue | Broker points | Importer points | Split notes |
|---|---|---|---|
| 1 Classification | 0 | 0 | |
| 2 Keying | 0 | 0 | |
| 3 Tariff changes | 0 | 0 | |
| 4 Refunds and corrections | 0 | 0 | |
| 5 Holds, exams, penalties | 0 | 0 | |
| 6 Staff | 0 | 0 | |
| 7 De minimis volume | 0 | 0 | |
| 8 Software cost | 0 | 0 | |
| 9 Getting paid, duty advances | 0 | 0 | |
| 10 ISF | 0 | 0 | |
| 11 Write-ins | — | — | |

---

## 9. Interview notes

One block per interview, from `5_interview_kit.md` §8, newest at the bottom.

*(none yet)*

---

## 10. Assumption register: measured values

*Added 2026-09-22.* One row per assumption in `handoff_s5_interviews.md` §6, where each one's questions and proving document are listed.
- **States:** unconfirmed → claimed (an interviewee's past event, with an amount) → proven (measured on the customer's own documents), or contradicted.
- **A kill test is decided only on proven values.**
- When a claim and a document disagree, record both.

### 10.1 C-09

| ID | Assumption | Desk value | Claimed (interview ID: value) | Proven (document or look-back: value) | State | Effect on the kill test |
|---|---|---|---|---|---|---|
| A09-01 | Share of in-window spend billed wrong, provable | 1.5% (our call) | | | unconfirmed | |
| A09-02 | ~~Share of real overcharges our audit catches~~ Share of real overcharges **the software flags** (D-23) | 70% | | | unconfirmed | |
| A09-03 | Share of disputed overcharges credited | 75% | | | unconfirmed | |
| A09-04 | ~~Fee share accepted~~ **Fee form and level** accepted: a share of recoveries or a subscription (D-23; price is Q6) | 25% | | | unconfirmed | |
| A09-05 | Invoices per $1,000 of spend | 1.5 | | | unconfirmed | |
| A09-06 | Share of invoices needing a person: under D-23 **the customer's workload**, counted as flags (false ones included) | 15% | | | unconfirmed | |
| A09-07 | Minutes per review; cost per dispute: under D-23 **the customer's minutes** per flag and per dispute | 6 min; $9.30 | | | unconfirmed | |
| A09-08 | Fixed cost per customer a year | $400 | | | unconfirmed | |
| A09-09 | Truckload + LTL spend of the customer | screen $1.5M+ | | | unconfirmed | |
| A09-10 | Share of a look-back inside the claim window | ~50% of 12 months | | | unconfirmed | |
| A09-11 | Shares agreement and invoices under NDA (Test 2) | — | | | unconfirmed | |
| ~~A09-12~~ | ~~Offshore review acceptable~~ | — | | | **moot (D-23, 2026-10-08)**: we employ no reviewers | |
| A09-13 | Errors fall after a first audit | mature 0.5-1.5% | | | unconfirmed | |
| A09-14 | Share via brokers / on minimum charge / reweighed | ABF: 38% / 28% | | | unconfirmed | |
| A09-15 | Follow-through: share of real flags the customer's staff work **and** file (*added 2026-10-08, D-23*) | 60%, dollar-weighted (our call; re-run 2026-10-08) | | | unconfirmed | Named condition of Test 1's middle band, settled in a pilot of at least one billing cycle (`4_kill_conditions.md` §2.5.8; re-run, proposed, not adopted) |
| A09-16 | The customer's hours a month for the queue, as capacity (*added 2026-10-08, D-23*) | capacity 20 h a month (our call); need ~12.5 h a month at $2M (our calc) | | | unconfirmed | Test 3 (`4_kill_conditions.md` §2.5.8; re-run, proposed, not adopted) |
| A09-17 | Self-serve onboarding: share of agreements the software reads unaided; customer's minutes to confirm the rules (*added 2026-10-08, D-23*) | 8 agreements × 60 min to confirm in year one (our call); shippers use 14-17 carriers | | | unconfirmed | Test 3 (`4_kill_conditions.md` §2.5.8; re-run, proposed, not adopted) |

### 10.2 C-19

| ID | Assumption | Desk value | Claimed (interview ID: value) | Proven (document or look-back: value) | State | Effect on the kill test |
|---|---|---|---|---|---|---|
| A19-01 | Non-trade deductions, share of big-box sales | 1.2% screened; CRF ¼-½%; ShopKo 0.33-0.46% | | | unconfirmed | |
| A19-02 | Share of those provably wrong, in window | 10%; pass needs ~18% at $50M | | | unconfirmed | |
| A19-03 | Share of wrong ones paid back | 60% | | | unconfirmed | |
| A19-04 | New-money share | unknown (S4.5 ran 100% and 50%) | | | unconfirmed | |
| A19-05 | Average deduction size; count per $1M | $500; ~10 | | | unconfirmed | |
| A19-06 | Minutes to check; to dispute | 5; 20 | | | unconfirmed | |
| A19-07 | Fixed cost incl. portals | $600 | | | unconfirmed | |
| A19-08 | Big-box sales and retailer mix | big-box ≈ 2 × Walmart | | | unconfirmed | |
| A19-09 | Screen yield (share at 1%+) | ~25% | | | unconfirmed | |
| A19-10 | Fee share accepted; what they pay today | 25%; SupplyPike ~$33-38k | | | unconfirmed | |
| A19-11 | Can export deductions; retailer allows third party (Test 2) | — | | | unconfirmed | |
| A19-12 | Invalid $ already lost to closed windows | unknown | | | unconfirmed | |
| A19-13 | Incumbent users not all satisfied | H19-11 | | | unconfirmed | |
| A19-14 | Fines chargeable to the 3PL or carrier | one contract | | | unconfirmed | |
| A19-15 | On-time and in-full % against target | unknown | | | unconfirmed | |

**C-19 screen tally (A19-09):** recruits asked: 0 · at 1% or more: 0 · yield: —

### 10.3 Our own assumptions

| ID | Assumption | Desk value | Measured | Source |
|---|---|---|---|---|
| A-X1 | Cost of winning one customer. *2026-10-08 (founders): for C-09, measured as the time from the first outreach to the first paying customer, then used for later customers (§1, the first-customer clock; `4_kill_conditions.md` §2.5.10 question 6)* | ~~$5-15k~~ bounds $0-10k (founders, 2026-10-08; `4_kill_conditions.md` §2.5.11) | | founder hours + recruiting spend per assessment agreed (§1) |
| A-X2 | Loaded wage for review work. *D-23 (2026-10-08): no longer our cost; for C-09 it is the customer's wage, a sensitivity only (their hours are treated as capacity, proposed); offshore struck* | US $33.70-36.79; posted $42-49; ~~offshore $12~~ | | job postings; timed hours |
| A-X3 | Machine cost per document | ~$0.10 | | software run on the look-back |
