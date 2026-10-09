# C-09's open questions: what the web answers, what it doesn't, and who to ask

> **Written 2026-10-07 for the founders.** It answers `C09-business-proposal.md` §8 as far as the web can, after an adversarial check. Where the web falls short, it points to people to ask.
> **Updated 2026-10-09 to the software-and-subscription strategy,** at the founders' request: "We have redefined this business strategy … Ensure these are updated to correspond with this." §0, new, lists every question still to answer before C-09 can be killed, covered or passed. Text that no longer fits the strategy has moved, word for word, to §13.
> **The ask of 2026-10-07, verbatim:** "find any web resources you can as to answers to these questions … If nothing is sufficient, then find contacts I can reach out to (as many as possible, as reliable as possible) … I want adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data."
> **Status: this document decides nothing.** No frozen line moves, no model number is changed, and none of the open decisions is taken. Claude contacted no one.
>
> **The strategy now** (decided by the founders on 2026-10-08 and 2026-10-09; `research/selection_runs/run-01/4_kill_conditions.md` §2.5, `software-initial-pitch.md` §1A):
> 1. **A software company, not an audit firm (D-23).** The software flags the bills that look wrong. The **customer's own staff** review the flags and file the disputes. We employ no analysts and do no manual review.
> 2. **A flat monthly subscription (C28),** sold as "a scoop off the top of the money they will make", not dependent on what comes back. The price is a Q6 decision.
> 3. **The look-back design is adopted:** capacity asked first, the software's rules run as scripts, the shipper's reviewer confirms the rules and works every flag while timed, then a pilot of at least one billing cycle.
> 4. **Kill Test 1 measures flagged dollars:** what the software flags and the shipper's reviewer accepts as wrong and provable.
> 5. **The cost of winning a customer is bounded at $0 to $10,000** until the first customer is timed. Test 1's lines are re-modelled at both bounds as **Kill / Cover / Pass** (§0.1).
> 6. **The Kill / Cover / Pass lines are adopted** (founders, 2026-10-09: "Adopt the Kill/Cover/Pass lines"; C29), with Tests 2 and 3. Look-backs may start once the data-handling rules (D-18) are settled. P-31 is deferred.
>
> **Labels**, as in every run-01 file:
> - *verified*: read at the source;
> - *assumed*: a vendor claim, an association figure, a self-report or a secondary summary;
> - **[our calc]**: our arithmetic;
> - **[our call]**: our judgement.

**Contents**
0. The outstanding questions: what we must still learn to Kill, Cover or Pass C-09
1. How this was done
2. The answer in one table
3. What the adversarial check threw out or narrowed
4. The money questions (A09-01, 02, 03, 13)
5. The claim window (A09-10)
6. The customer's own facts, and what audit firms and software charge (A09-04 to 09, 14 to 17)
7. The carrier side (H09-C1, C2, C4) and sharing documents (A09-11)
8. Facts for four decisions (D-15, D-16, D-18, D-19), not the decisions
9. New things the design should know about **[our call]**
10. Who to ask: the contacts
11. Inconsistencies found on the way, for you to confirm
12. Files
13. Superseded, kept for the record

---

## 0. The outstanding questions: what we must still learn to Kill, Cover or Pass C-09

*Added 2026-10-09 at the founders' request:* "I want the outstanding questions … look at the other docs to see more questions we would need answered to Kill, Cover, or Pass the kill test for this idea."

**This is the master list.** `research/selection_runs/run-01/5_interview_kit.md` §5.1 carries the same questions in interview order. `handoff_s5_interviews.md` §6.2 and `research/selection_runs/run-01/5_log.md` §10 track each number from *claimed* to *proven*.

### 0.1 How the test reads, in plain words

The kill test is measured on **the first real look-back**: one shipper's own bills from inside the claim window, checked against its own rate agreements (`4_kill_conditions.md` §2.5.8).

**Test 1 asks one thing:** of the shipper's freight spend still inside the claim window, what share does the software flag that the shipper's own reviewer accepts as billed wrong and provable? That share is the **flagged rate**. It is measured in **dollars**, not in shipments or bills.

Where the flagged rate lands against three lines decides the card. The lines depend on the shipper's size (`4_kill_conditions.md` §2.5.11, **[our calc]**; adopted by the founders on 2026-10-09, §2.5.12):

| Shipper's truckload + LTL spend a year | **Kill** under | **Cover** from | **Pass** from |
|---|---|---|---|
| $0.5M | 0.127% | 1.26% | 19.0% |
| $1M | 0.065% | 0.70% | 9.59% |
| **$1.5M** | **0.044%** | **0.51%** | **6.44%** |
| $2M | 0.034% | 0.42% | 4.86% |
| $3M | 0.023% | 0.32% | 3.29% |
| $5M | 0.015% | 0.25% | 2.03% |

What each line means, at a $1.5M shipper:
- **Kill (under 0.044%):** even a customer that cost nothing to win, with every unknown at its best, can't cover our first-year cost. C-09's S5 work stops.
- **Below Cover (0.044-0.51%):** at the middle values, even a free-to-win customer doesn't cover our first-year cost. C-09 continues only if a pilot shows the shipper's staff working the flags, and that can't reach the line below 0.31%.
- **Cover to Pass (0.51-6.44%):** a first customer pays for itself. Whether later customers do depends on what winning them really costs, read from the columns in §2.5.11 once the first customer has been timed.
- **Pass (6.44% or more):** the customer repays even $10,000 spent winning it, within 12 months.

**The same lines as a monthly subscription, at a $1.5M shipper** (`4_kill_conditions.md` §2.5.11). Our fee is a flat subscription. The model assumes a shipper would pay at most about a quarter of what it gets back, so that is the ceiling on the price, not a share we take:

| Line | Wrong billing found a year | Shipper gets back a month | Subscription that covers our costs, a month |
|---|---|---|---|
| Kill | about $660 | about $50 (every unknown at its best) | about $25 |
| Cover | about $7,700 | about $290 | about $72 |
| Pass | about $96,600 | about $3,620 | about $905 (it also repays $10,000 of winning cost within 12 months) |

If shippers would pay up to half of what they get back, the Cover and Pass lines halve, to about 0.26% and 3.2% at $1.5M.

**The other two tests** (`4_kill_conditions.md` §2.5.8):
- **Test 2, access:** the shipper uploads its rate agreements and paid invoices under a mutual NDA (non-disclosure agreement). **Kill** if 2 of the first 3 shippers decline. A "no" that names only a security certificate (SOC 2) is a cost question, not a refusal.
- **Test 3, the customer's hours:** the reviewer's minutes are timed in the look-back and set against the hours the shipper says it can give (20 a month if it gives no figure). **Kill** if the queue would need more than twice that, even counting only the flags the reviewer accepted. **Pass** if it fits, and our reading cost is at or under $0.50 a bill.

**Where the evidence points [our call]** (`4_kill_conditions.md` §2.5.8): at a $1.5M shipper, every flagged figure on file sits between Cover and Pass: government auditors flagged 1.66-3.37% (self-reported), and the vendors' six cases ran 0.8-4.2%. So the first look-back will most likely land in the middle band. (At $5M the Pass line falls to 2.03%, below the top of both ranges.) If it does, three things decide C-09: whether the shipper's staff work the flags (the pilot), whether the hours fit (Test 3), and what winning a customer really costs (the first-customer clock). The neutral figures under 0.5% (USDA's 0.45%, the federal 0.07%) measure money **collected**, which is a smaller and different thing from dollars flagged.

**Status: adopted.** The founders adopted these lines, with Tests 2 and 3, on 2026-10-09 ("Adopt the Kill/Cover/Pass lines"; `4_kill_conditions.md` §2.5.12, C29). The lines frozen on 2026-09-22 are struck through. **Look-backs may start** once the data-handling rules (D-18) are settled.

### 0.2 The founders' four questions, each placed

**1. "What % of cargo is overcharged"**
- **Sets:** A09-01, the flagged rate. **This is Test 1 itself.**
- **Measure it in dollars,** as a share of freight spend. Ask for the number of bills too, since a few large errors and many small ones read very differently.
- **Ask it this way** (the last time, with amounts):
  - "Tell me about the last freight bill that turned out to be wrong. How much, what kind of error, who caught it, and did the money come back?"
  - "In the last 12 months, how many bills turned out wrong, for how many dollars, against roughly what freight spend?"
- **Proven only by the look-back.** An interviewee's figure is a claim.

**2. "Who currently handles auditing this in your firm?"**
- **Sets three things:**
  - how bills are checked today (H09-01);
  - whether an audit firm, an audit-and-pay provider or a booking tool's audit screen is already used, and how satisfied they are. That is the **show-stopper test** (H09-08);
  - who would work our flag queue, which bears on follow-through and hours (A09-15, A09-16; H09-12).
- **Ask it this way:** "Who checks freight bills before they're paid? Walk me through the last one they checked: what did they compare it with, and how long did it take?" Then: "Does anyone else look at them: an outside firm, software, a booking tool's audit screen? What did it catch last time, and what did you pay for it?"

**3. "How much money a year do you think you are being overcharged?"**
- **Keep it, but log the answer as a belief,** never as a claim or a proof. "Do you think" gets a guess, not a past event (handoff §6.1, rules 1 and 5).
- **What it's for:** whether the "scoop off the top" pitch lands with this buyer, and how to read the price test.
- **Always follow with:** "What makes you say that?", then question 1's past-event version.
- **Compare it later with the look-back.** How far people over- or under-estimate is evidence in itself (handoff §6.1, rule 6).
- **Where it's logged:** in the interview notes (`5_log.md` §9), marked "belief". It never goes in §10's Claimed column.

**4. "How many audits have you submitted?"** Ask it both ways, because the words cover two different things:
- **(a) Disputes and claims filed with carriers:** "In the last 12 months, how many disputes or overcharge claims did you file with carriers, for how many dollars? How many came back, for how much, and how many days did it take? Tell me about the last one a carrier refused."
  - **Sets:** A09-03 (the share carriers credit); a baseline for follow-through (A09-15); a floor under A09-01.
- **(b) Outside audits of their bills:** "Have your freight bills ever been audited by an outside firm? When, what did it find in dollars against how much spend, and what happened to errors the year after?"
  - **Sets:** a neighbour figure for A09-01, and year-two decay (A09-13).

### 0.3 The full list, grouped by what each answer decides

**How to use it:**
- Every question is asked of the **shipper** unless marked. Experts are in §0.4.
- **"Ask it this way"** follows the interview rules (kit §1): the last time, a number with its unit and period, and a request to see the document.
- **"Web so far"** is this file's verdict (§2). **"Proven by"** is the only thing that moves a number to *proven* (`handoff_s5_interviews.md` §6.1).
- The founders' four are marked **F1-F4**.

#### A. Which row of the table applies: the shipper's size

The lines are read at the shipper's own spend, so these come first.

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| A1 | How much do you spend on freight? | "What did you pay carriers and brokers last year, split truckload, LTL and parcel? A band is fine: under $250k / $250k-1M / $1-3M / over $3M" | A09-09 | Which row of the Kill / Cover / Pass table | Narrowed: three real segment firms bought $1.5-1.9M a year, all bankrupt (§6 A09-09). Check AT: TL+LTL is about 1.1% of revenue at distributors and 2.6-3.8% at makers (central; wide ranges), so $1.5M of spend needs about $130M of revenue at a distributor and $40-60M at a maker **[our calc]** | The AP payment export with bank details removed, or the look-back's bills annualised |
| A2 | How many freight bills? | "How many freight invoices did you pay last month?" | A09-05 | Our reading cost; how many bills reach the customer's queue (Test 3) | Narrowed: 1.9-2.0 bills per $1,000 at LTL carriers' own averages (§6 A09-05) | The invoice count in the look-back |
| A3 | How much goes through brokers? | "What share of last year's freight was booked through a broker or 3PL? When one of those bills was corrected, who sent the new invoice?" | A09-14 | Which claim window applies: broker terms give 5-30 days, not 180 | Narrowed: 0-52% at six real shippers, median 15-17% (§6 A09-14) | Counts in the look-back |
| A4 | How many carriers? | "How many trucking companies did you pay last quarter? Which three took the most?" | A09-08, A09-17 | How many agreements the customer must upload and confirm (Test 3) | Narrowed: 14-17 carriers in 90 days at three real shippers; 6-9 make 80% of dollars (§6 A09-08) | The AP payment export |

#### B. Test 1's number: how much is billed wrong

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| B1 | **F1:** what share is overcharged? | §0.2, item 1 | A09-01 | **Test 1: Kill, Cover or Pass** | Narrowed: government auditors flagged 1.66-3.37% before payment, self-reported; no private mid-sized shipper is measured (§4) | **The look-back only** |
| B2 | **F3:** how much a year do you think? | §0.2, item 3 | a belief, not a number | Nothing directly: how the pitch lands and how to read the price test | — | Compared with the look-back afterwards |
| B3 | **F4 (b):** have outside firms audited you? | §0.2, item 4 (b) | A09-01, A09-13 | A neighbour for Test 1; renewal | Narrowed (§4 A09-13) | Their prior audit report |
| B4 | What kinds of error? | "On the last wrong bill: was it a duplicate, a rate that didn't match the agreement, the fuel percentage, an extra nobody agreed, a reweigh or reclass?" Offer the types only if they stall | A09-01 by type | Which checks the look-back must run. It runs the full set, since a weak set of checks reads low (`4_kill_conditions.md` §2.5.10, answer 4) | The practice audit proved $0 from public documents; 61% of dollars needed documents only the shipper holds | The look-back, by type |
| B5 | Do contracts set a claim window? | "Do your truckload contracts or broker rate confirmations have a claims clause, like 'claims within 90 days'? Can you show me one?" | A09-10 | In-window spend, which is what Test 1 divides by | **Answered** for direct LTL tariff freight (180 days; ODFL and ABF start at shipment); narrowed for contract and broker freight (§5) | The clause itself |
| B6 | How soon is a wrong bill noticed? | "The last wrong bill: how many days after paying did someone notice, and how many more before it was disputed?" | A09-10 | How much of a look-back is still collectable | Not on the web | Invoice and dispute dates |
| B7 | Minimum charges and reweighs | "On last month's LTL bills, how many sat on the carrier's minimum charge? How many carried a reweigh or inspection note?" | A09-14 | How much of the spend the checks can bite on | Only the ABF practice set: 38% on the minimum, 26 of 101 reweighed (§6 A09-14; §11 item 1) | Counts in the look-back |
| B8 | How far back can you pull? | "What are the oldest paid invoices, rate agreements and proofs of delivery you could pull today?" | A09-10, A09-11 | How deep the look-back goes; which agreement versions were in force | Not on the web | Files received |

#### C. Between Cover and Pass: do the flags turn into money?

Inside the middle band, C-09 continues only if a pilot shows the shipper's staff working enough of the flags (**follow-through**), and the carriers crediting them.

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| C1 | **F2:** who works a wrong bill? | "The last time a freight bill looked wrong, who at your company looked into it, how long did it take, and what happened to it?" | A09-15, A09-16; H09-12 | **The middle band's condition** | **Not answerable from the web:** follow-through is "not measured anywhere" (§6 A09-15) | A pilot of at least one billing cycle: the shipper's dispute log against the software's flags |
| C2 | **F4 (a):** how many disputes did you file? | §0.2, item 4 (a) | A09-03; a baseline for A09-15 | The credited share. The model's 75% is replaced once 5-10 of the pilot's disputes are decided | Narrowed: no private-shipper figure; 60-90% credited when prompt, 41-51% when old (*assumed*) (§4 A09-03) | Credit memos or the dispute log; the pilot's own outcomes |
| C3 | How many questioned bills got worked? | "Of the bills flagged or questioned last month, how many did someone actually work, and how many ended in a dispute?" | A09-15 | The middle band's condition | As C1 | The pilot |
| C4 | Is there an amount you don't chase? | "Is there an amount below which you don't bother disputing a freight bill? What was the last one you let go, and why?" | A09-15, dollar-weighted | How much flagged money is never chased | Narrowed: "Many shippers use a percentage or dollar threshold under which they won't dispute" (*verified* as reported); Freightview's example tolerance accepts bills up to 3% (LTL) or $50 (truckload) over (*verified*) (§6 A09-15) | The pilot's unworked flags, by size |
| C5 | Do you use a booking tool's audit screen? | "Do you book LTL in a tool such as Freightview or MyCarrier? When did someone last open its audit screen, what did it flag, and what tolerance is set?" | A09-15, A09-16; H09-08 | A live example of a queue being worked or left; the show-stopper | Narrowed: Freightview 4.7 from 743 reviews; its audit screen is a secondary feature, criticised for carrier coverage (check Z) | The screen, shown in the conversation |
| C6 | Who files, and how? | "When you last disputed a bill, who sent it, to whom, and how: email, the carrier's website, a form, or by paying less?" | A09-15; H09-C1 | Follow-through; the design: dispute through each carrier's channel, never by paying less | Narrowed: the large truckload carriers and brokers searched publish no self-serve dispute channel (check AQ §AQ3.2); nine of ten LTL rulebooks bar paying less than billed (§7) | The dispute log |

#### D. Which Pass column applies: the price, and the cost of winning a customer

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| D1 | What do you pay today? | "Does anyone audit your freight bills today: staff, an outside firm, software? What did you pay last year, and what came back?" | A09-04; H09-08 | What our subscription is compared with; the show-stopper | Narrowed: audit firms 23.23% / 38.61% of refunds (federal list); booking tools $0-253 a month for small tiers; one audit-software listing $2,500 a month per unit (§6 A09-04) | Their provider's invoice |
| D2 | Who approves software? | "The last time you bought software for logistics or AP, who approved it, out of which budget, and up to what amount could they sign alone?" | A09-04; H09-05 | Whether a subscription can be bought at all. A subscription needs a budget line | Narrowed: the smallest tool tiers sell on free trials and card billing; at a $2M shipper's volume, prices are by quote (check AQ §AQ4.2) | The purchase record or the signing policy |
| D3 | The price test (at the close only) | After the look-back offer, state the test price, then stop talking. Log "yes", "yes at a different price" (which?) or "no" (why?) | A09-04 | Whether shippers pay up to a quarter of what they get back (the lines assume it) or up to half (the lines halve) | — | **A signed agreement or letter of intent.** A spoken yes is only a claim |
| D4 | *Ours, not asked:* what did winning the customer cost? | The first-customer clock (`5_log.md` §1): from the first outreach to the first paying customer, with founder hours and cash | A-X1 | Which Pass column applies. The lines are read at the measured cost **before** the next look-back | Bounded at $0-$10,000 (founders, 2026-10-08) | The clock |

The test price for D3 is the founders' to set before the first close (D-15). The price itself is a Q6 decision.

#### E. Test 2: will they share the documents?

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| E1 | Will you share them under an NDA? | "If I asked for last month's paid freight invoices and your rate agreements, what format would they be in, and how long would it take to pull?" Then ask for them, under a mutual NDA | A09-11 | **Test 2:** kill if 2 of the first 3 decline | Narrowed (§7 A09-11) | Files received; count yes and no among the first 3 |
| E2 | Are your rates confidential? | "Which of your carriers' pricing agreements say the rates are confidential? Could you check the biggest one?" | A09-11 | Whether a "no" is a contract rather than reluctance; how the NDA is written | Narrowed: 2 of 10 LTL rulebooks make rates confidential (TForce Item 130, FedEx Freight Item 250); one negotiated contract carves out auditors (§7 A09-11) | The clause |
| E3 | What did IT ask for last time? | "The last time you sent an outside firm invoices or contract rates, what did IT, legal or procurement ask for first, and how long did it take?" | A09-11; H09-05 | Test 2's middle band: a "no" that names only SOC 2 is a cost question for S6 | Narrowed: no evidence that mid-sized shippers demand SOC 2 before uploading (check AQ §AQ5) | Their security questionnaire, if they have one |
| E4 | What do the bills look like? | "Where did last month's freight bills land: email, a carrier's website, EDI, paper, a 3PL? Can you show me one?" | A09-17; `software-initial-pitch.md` §14 | Our reading cost, against Test 3's $0.50-a-bill limit | Narrowed (check AJ) | One bill, shown |

#### F. Test 3: will the customer's hours fit?

| # | Question | Ask it this way | Sets | Decides | Web so far | Proven by |
|---|---|---|---|---|---|---|
| F1 | How many hours went on bills last month? | "How many hours did your team actually spend on freight bills last month? Who did it, and what did it push aside?" Ask about last month's actual hours, never "how many could you give it" | A09-16 | Test 3's baseline | **Not answerable from the web:** vendor-reported workloads only, from 5 hours a week for 200 bills to 15-20 hours a week (*assumed*) (§6 A09-16) | Timesheets, if they keep them |
| F2 | How many hours can you give the queue? | **Asked at the look-back, not in the interview:** "How many hours a month can your team give the flag queue?" Recorded before anything is timed | A09-16 | **Test 3's limit** (20 hours if they give no figure) | — | Recorded before the timed session (look-back step 1) |
| F3 | How many bills carry extras? | "On last month's bills, how many carried extras: liftgate, detention, lumper, a reweigh note?" | A09-06 | Flags per bill, so the size of the queue | Narrowed: extras are 8-9% of LTL dollars; on the practice account 58% of bills needed a person (§6 A09-06) | Count in the look-back |
| F4 | How long does a bill, and a dispute, take? | "Walk me through the last bill you approved: what did you compare it with, where, and how long did it take? And the last dispute: how long from noticing it to sending it?" | A09-07 | Minutes per flag and per dispute | Narrowed: no source times a pre-explained freight flag; a processing exception takes 15 minutes in one government estimate; a retail deduction about 52 minutes (§6 A09-07) | The shipper's reviewer, timed in the look-back |
| F5 | Where do your rate agreements live? | "Who keeps your carrier rate agreements, and in what form: PDF, spreadsheet, email, a carrier's website? How many carriers have one? When did one, or a fuel table, last change, and who updated it where?" | A09-08, A09-17 | Minutes to confirm the rules the software reads (desk: 8 agreements × 60 minutes) | **Not answerable from the web:** no completion rate for loading contracts; a strong table reader gets every cell right in only 69% of complex tables (§6 A09-17) | Timed in the look-back: agreements read correctly, corrections needed, minutes |
| F6 | *Ours, not asked:* what does reading cost? | Measured when the scripts run | A-X3 | Test 3's condition: at or under $0.50 a bill | About $0.10 a bill (check AA) | The look-back run |

#### G. Not a kill test, but S5 or S6 needs it

| # | Question | Ask it this way | Sets | Decides | Web so far |
|---|---|---|---|---|---|
| G1 | Are users of today's tools satisfied? | "If you use one: how satisfied are you, and what did it miss last time?" | H09-08 | The show-stopper: one vendor serving more than half the targets, satisfied | Partly: no provider is shown serving more than half; booking tools' audit screens are the incumbent the hypotheses missed (check Z) |
| G2 | What happened the year after an audit? | "If you've been audited before, what happened to errors in the year after?" | A09-13 | Renewal: under a subscription, falling finds mean less back for the same fee | Narrowed: no freight decay series (§4 A09-13) |
| G3 | Which industry? | The screen: industry and staff band | H09-11 | The Q6 carry-forward (steady or cyclical industries) | — |
| G4 | The carrier side (5 interviews, kit §5.2) | "Tell me about the last time a shipper paid less than you billed, or disputed an invoice." "When a shipper's own staff dispute a bill, what makes you accept or refuse it?" | H09-C1, H09-C4 | How the software should send disputes. H09-C4 matters again only once we help customers file; H09-C2 (faster payment) is parked | Rules answered; practice not (§7) |
| G5 | How documents get in | The twelve intake questions in `software-initial-pitch.md` §14 (where bills land, the accounting system, carrier logins, email forwarding) | — | The build order, not the kill test | — |

### 0.4 Questions for experts, not shippers

The web couldn't answer these. Contacts are counted in §10; the names are kept outside the project. **Log every answer as a claim about others,** never as proof.

| Who | The question | Number | Route (§10) |
|---|---|---|---|
| A transportation lawyer | "Does the 180-day rule bind contract-rate truckload freight and brokers' own invoices, and how often do shipper contracts waive it?" | A09-10 | 13 contacts at A or B, 8 lawyers at A; TLC's Q&A Forum takes one free question |
| An audit-firm principal | "The last mid-sized private shipper whose truckload and LTL bills you audited: what share of spend did you flag, and how much was credited?" Then the kit's expert variant: "Tell me about the last client whose own staff worked a flagged-bill queue: who did it, how long it took, and what got filed" | A09-01, A09-03, A09-15 | 4 contacts at A or B for A09-01, none at A. They will quote their own books |
| A data-privacy lawyer | "Can a mutual NDA require deleting the files after the assessment, backups included? Do shippers restrict a software vendor storing invoice data outside the US?" | D-18 | **No contacts:** never searched for. A gap to fill before real data arrives |
| Carrier credit or billing staff | "The last time a shipper disputed a bill and didn't pay it, did you revoke its discounts or charge the penalty? How often does that happen?" | H09-C1 | ATA's National Accounting & Finance Council; no named carrier billing manager is public |
| Government audit staff | Credited shares and how finds fall in later years | A09-03, A09-13 | GSA's Transportation Audits Division policy mailbox |

### 0.5 What no conversation can settle

Only the look-back and the pilot prove these, in the order the founders adopted (`4_kill_conditions.md` §2.5.8; kit §6.1):

| Step | What happens | What it proves |
|---|---|---|
| 1 | **Capacity first:** the shipper says how many hours a month it can give the queue, recorded before anything is timed | Test 3's limit (A09-16) |
| 2 | **The software's rules run as scripts** on the in-window bills and agreements, on the founders' local demo or a cheap cloud host. Raw files stay outside the project folder (D-18) | Bills per $1,000 (A09-05); flags per bill (A09-06); our reading cost (A-X3); in-window spend (A09-10); broker, minimum-charge and reweigh counts (A09-14) |
| 3 | **The shipper's reviewer confirms the rules** read from each agreement | Agreements read correctly, corrections, minutes (A09-17) |
| 4 | **The reviewer works every flag on screen while timed:** accept or reject. No one on our side judges a bill | **The flagged rate (Test 1)**; the share of flags accepted; minutes per flag (A09-07); the customer's hours a month (Test 3) |
| 5 | **The pilot,** at least one billing cycle: the software flags new bills as they arrive | Follow-through (A09-15); credits as they arrive (A09-03) |

**Also counted outside the look-back:** Test 2 from the files received among the first 3 shippers; the price only from a signed agreement; the cost of winning a customer from the first-customer clock.

**What it asks of the shipper [our calc]** (`4_kill_conditions.md` §2.5.10, answer 3): three months of bills at $1.5M of spend is about 560 bills. At about 10 minutes a flag, that is about 14 hours if 15% are flagged and about 54 hours if 58% are.

**The lines are adopted (2026-10-09), so look-backs may start** once the data-handling rules (D-18) are settled.

---

## 1. How this was done

| Step | Who | Output |
|---|---|---|
| **Research** | Three agents, each with its own questions. Each was told what earlier checks (X, Y, Z, AA-AL) had already found and must not redo | Checks **AM** (the leak and the recovery), **AN** (running the service, the customer's facts), **AO** (carriers, sharing documents, interview logistics), each ending in a **claim ledger**: one row per claim, with the quote, the source, what the number's percentage is "of", the population, the period, and where the figure first came from |
| **Adversarial check** | Three more agents, one per check. They saw only the ledger and the sources, never the researcher's reasoning, and **fetched every source again themselves** | One review file per check, with a verdict on each claim: KEEP-verified, KEEP-assumed, NARROW (keep a stated, smaller reading) or DISCARD. Every verdict carries its own quote. A doubt with no evidence behind it was logged as "concern, unproven" and changed nothing |
| **Coordinator re-check** | This chat | Every discard, and the claims behind each verdict, fetched again at the source (logged in each check's header). **All matched the reviewers** |
| **Contacts** | One finder agent, then one adversarial checker | Names in a private file **outside the project** (`~/Documents/personal/bio/freight_private/c09_contacts.md`); counts only in the project (§10) |

**Added 2026-10-09:** the rows for A09-15 to A09-17, and the software prices in §6, come from the checks of 2026-10-08 (AQ the customer's side, AR our cost, AS the market's prices), done the same way: research, then an adversarial review that fetched every source again, then a coordinator re-check (`4_kill_conditions.md` §2.5, header).

**What "coincidence" turned out to mean here.** The reviewers found three kinds:
- **One origin, many mouths.** A figure that looks confirmed by several sources really comes from one. The "25% of shipments re-rated" stories all trace to Old Dominion's own marketing paper; the "3.43% cold-email reply rate" traces to one vendor's report; the "20.8% of invoices wrong" and "two-thirds outsource" figures come from one sponsored 2020 survey.
- **Look-alikes.** Two numbers match but measure different things. The DoD freight figure (~1.5%) sits right on our model's 1.5% assumption, but it is an unverified summary across all modes, ocean included. The two "agreeing" per-bill prices ($2.31 and $2.36) are 8 years apart and in different units.
- **A partial list read as a whole.** A broker share of 74.9% came from a bankruptcy payment list that had been only partly extracted.

**The verdicts used in this document:**
- **Answered from the web:** a source we read settles it, usually law or published terms.
- **Narrowed:** bounds from neighbouring populations (government, large shippers, carriers' averages); our segment is still unmeasured.
- **Not answerable from the web:** only the customer's documents or a conversation can tell.

**The project's own rule still holds** (`handoff_s5_interviews.md` §6.1): a model number is *proven* only on a customer's own documents. The web can narrow these numbers. It cannot prove them.

---

## 2. The answer in one table

*Updated 2026-10-09:* the model values are now the software re-run's (`4_kill_conditions.md` §2.5.3), a column shows the test each one feeds, and A09-15 to A09-17 are added. The table as it stood on 2026-10-07 is in §13.2.

| ID | The question in plain words | Model value now | Test it feeds | **Verdict** | What survived the check (one line) |
|---|---|---|---|---|---|
| **A09-01** | How much of a mid-sized shipper's freight spend the software flags and its reviewer accepts as wrong and provable | **1.05% flagged** **[our call]** (the old 1.5% true rate × the old 70% catch) | **Test 1** | **Narrowed** | Government auditors, checking bills **before payment**, report flagging 1.7-3.4%; after payment almost nothing is left. No private mid-sized shipper is measured |
| A09-02 | Share of real overcharges one check catches | Inside the flagged rate: Test 1 measures flagged dollars, so no separate catch share is applied | Test 1 (the look-back must run the full set of checks) | **Narrowed** | Nothing replaces GAO 1992 (72-78%). What auditors flag varies 7× between firms on the same kind of bills |
| A09-03 | Share the carrier credits, and how fast | 75%, until 5-10 of the pilot's disputes are decided | Test 1's middle band | **Narrowed** | No private-shipper figure. Carriers *may* pay claims filed after 180 days, voluntarily |
| A09-04 | The price shippers accept | A flat monthly subscription, assumed to be at most **25% of what the shipper gets back** (a price ceiling); the level is Q6 | The lines are stated at that ceiling | **Narrowed** | Audit firms' public prices: **23.23%** / **38.61%** of refunds (CT Logistics' current federal list); booking tools $0-253 a month for small tiers (§6) |
| A09-05 | Invoices per $1,000 of spend | 1.5 | Our reading cost; the customer's flag count | **Narrowed** | LTL carriers' own 2025 averages: **1.9-2.0** (Old Dominion, ABF); lighter freight means more bills |
| A09-06 | Share of bills flagged (false flags included) | 15% | Test 3 | **Narrowed** | Only neighbours: accessorials (extra-service charges) 8-9% of LTL dollars; re-rates "25 to 30 percent" at some shippers (one carrier's paper) |
| A09-07 | The customer's minutes per flag and per dispute | 10 minutes a flag; disputes on 5% of bills at 30 minutes | Test 3 | **Narrowed**; dispute minutes **not answerable** | Federal per-bill prices bound an audit firm's clerk time at **at most 4.6-7.6 minutes** a bill. Minutes per TL/LTL dispute: not found |
| A09-08 | Carriers, agreements and onboarding | Our support $175 and hosting $60 a year, onboarding help $185-616 in year one; the customer confirms about 8 agreements × 60 minutes | Break-even; Test 3 | **Narrowed** | Real shippers paid **14-17 trucking firms** in 90 days; rates change yearly, fuel weekly; hours to load an agreement: not found |
| A09-09 | How much TL+LTL a segment firm buys | The line is read at the shipper's own spend; the kit screens for $1.5M+ | Which row of the table | **Narrowed** | Three new real payment lists: about **$1.5-1.9M a year** each, 0.9-4.8% of revenue. All are bankrupt firms |
| **A09-10** | The claim window | ~50% of a 12-month look-back; nearly all of a monthly cycle | Test 1's denominator (in-window spend) | **Answered** for direct LTL tariff freight (180 days); **Narrowed** for contract and broker freight | **Broker terms give 5-30 days, not 180.** Two big LTL carriers start the 180 days at shipment, not at the bill |
| **A09-11** | Will shippers upload agreements and invoices under an NDA | Test 2 | **Test 2** | **Narrowed** | **2 of 10 LTL rules tariffs make rates confidential** (TForce, FedEx Freight). A "no" may be a contract, not reluctance |
| A09-12 | Is review outside the US acceptable | — | — | **Moot** (D-23: we employ no reviewers) | The surviving question, storing invoice data outside the US, goes with D-18 (§6 A09-12) |
| A09-13 | How far first-year finds fall later | mature 0.5-1.5% | Renewal, not a kill test | **Narrowed** | No freight decay series; government programme totals can't be read as one |
| A09-14 | Share via brokers, on minimums, with reweighs | ABF: 38% on minimum, 26 of 101 reweighed | Test 1's reach; which claim window | **Narrowed** | Brokers took **0-52%** of trucking dollars at six real shippers (median ~15-17%) |
| **A09-15** | **Follow-through:** the share of real flags the customer's staff work and file | 60%, dollar-weighted **[our call]** | **Test 1's middle band** (the pilot) | **Not answerable from the web** | "Not measured anywhere". Shippers set thresholds below which they don't dispute; Freightview's example tolerance accepts bills up to 3% (LTL) or $50 (truckload) over (§6) |
| **A09-16** | **The customer's hours** a month for the queue (capacity) | Capacity 20 hours **[our call]**; need about 12.5 at a $2M shipper **[our calc]** | **Test 3** | **Not answerable from the web** | Vendor-reported workloads only: 5 hours a week for 200 bills to 15-20 hours a week (*assumed*) |
| **A09-17** | **Self-serve onboarding:** agreements the software reads correctly; the customer's minutes to confirm | 8 agreements × 60 minutes in year one **[our call]** | **Test 3** | **Not answerable from the web** | No completion rate for loading contracts. A strong table reader gets every cell right in only 69% of complex tables (*verified*) |
| H09-C1 | What carriers do when short-paid or disputed | — | The software's dispute route | Rules **answered**; practice **not answerable** | Nine of ten LTL tariffs bar short-paying; **five revoke all discounts** when an unpaid bill goes to collection or the credit period runs out; four charge 25-35% |
| H09-C2 | Would carriers pay for faster payment | — | Parked: version 1 is audit only | **Narrowed** | Brokers' quick-pay costs carriers 1.5-4%; whether a carrier billing the shipper directly would pay is unknown |
| H09-C4 | How carriers treat an outside firm's claims | — | Only once we help customers file | **Narrowed** | TForce bars agents from guarantee refunds; FedEx Freight may refuse at its discretion; the law still lets an agent file overcharge claims |
| D-15 | Facts: what others charge for assessments and pilots | — | — | **Narrowed** | Free first looks are the norm; no paid assessment price found; the **second** audit pass is priced **higher** |
| D-16 | Facts: incentives, gift rules, tax | — | — | Tax **answered**; norms **narrowed** | IRS reporting threshold **$2,000** a year per payee from 2026. Some firms ban gifts from *prospective* suppliers |
| D-18 | Facts: NDA templates and data handling | — | — | Templates **answered**; retention **narrowed** | An open mutual NDA exists (Common Paper), but by default it lets the receiver keep backup copies |
| D-19 | Facts: recruiting time and reply rates | — | — | **Narrowed** | Cold-sales reply rates 0.74-3.43% imply roughly **290-1,350 people contacted** for 5 interviews; no figure for research requests to finance or logistics staff |

**What this means in one sentence [our call]:** the web has added real prices, real shipper payment lists and hard contract and legal facts, but **not** the flagged rate on a mid-sized private shipper's own bills, nor whether its staff will work the flags, nor how many hours that takes. Only the look-back and the pilot measure those (§0.5).

---

## 3. What the adversarial check threw out or narrowed

**Totals** across the three checks: 218 claims.

| Check | KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|---|
| AM (74 claims) | 46 | 15 | 11 | 0 | 2 |
| AN (57) | 23 | 16 | 15 | 1 | 2 |
| AO (87) | 71 | 9 | 6 | 1 | 0 |

**The changes that matter**, most important first:

| What was claimed | What the check found | Effect |
|---|---|---|
| Government auditors flag **3.37%** of first billings (A09-01) | The auditors reported it themselves, and **one firm supplies 79% of it**. The other four firms come to **1.66%** **[our calc]**, re-checked against the GSA Inspector General's Table II | The "bracket around 1.5%" is weaker than it looked |
| DoD freight overpayments **≈1.49%** of payments (A09-01) | That was the higher of two years, covered ocean freight too, and was never verified by the DoD Inspector General. Both years together: **0.95-1.32%**. GSA later repaid $29.6M of its own wrong notices to one DoD vendor | A look-alike of our 1.5%, not a confirmation |
| Federal post-payment audits find **0.068%** (A09-01, from check X) | The base is estimated total federal transport spend, air passenger travel included, not the bills audited | A programme yield, not an error rate |
| Brokers took **0-74.9%** of trucking dollars (A09-14) | **Discarded**: two of the six lists were only partly extracted. On the full lists: **0-52.4%**, median 15-17% | Range cut by a third |
| CT Logistics charges **$2.31-3.88** per bill and **19.25% / 32%** of refunds (A09-04, A09-07) | That list expired in 2020. The current one (from May 2026) charges **$2.79 / $4.68** a bill and **23.23% / 38.61%**. A PDF bill falls in the dearer class | Prices about 21% higher |
| FedEx Freight charges **3%** for card payments (H09-C2) | **Discarded**: that item is in the tariff's Intra-Canada section | Only ABF's 2% remains, for US payers |
| A full-rate penalty would take a real ABF bill from $942 to **~$9,063** (H09-C1) | The arithmetic is right (9.6-9.8×), but the federal regulator said in 1997 such penalties must "bear a reasonable relationship" to collection costs | A ceiling on paper, not a likely cost |
| *Gaines* (4th Cir.) makes the 180-day rule for contract freight "unsettled" (A09-10) | *Gaines* decided only whether a federal court could hear a case. The 10th Circuit says the contract-carriage law "says nothing that contradicts" the 180-day rule | The law leans toward 180 days applying; the reason in AM was wrong |
| A state audit's agencies "rejected" **69%** of flagged dollars (A09-02) | The 69% includes errors the agencies had already fixed | Not a false-flag rate |
| "3.43% cold-email reply rate" from two vendors (D-19) | One origin (Instantly, 2026), repeated by another vendor; the rates count people contacted, not emails | One source, not two |

---

## 4. The money questions

### A09-01 · How much carriers bill wrongly, provably · **Narrowed**

**What survived (all from government shippers, none from our segment):**
- **Bills checked before payment:**
  - In FY2011, five contract auditors reported flagging **$3,846,770 on $114,216,991** of first billings: **3.37%** (*verified* as reported; GSA OIG A120060, Table II).
  - One firm (National Traffic Service) reported 4.67% on 57% of the billings. **The other four come to 1.66%** **[our calc]**.
  - These are "amounts saved due to identified overcharges": flagged, not credited, and self-reported. Household-goods moves are mixed in.
- **Across ten agencies, FY2006-11:** 5.0% flagged, 4.0% without the Navy (*verified* as reported).
- **Bills already paid:** DoD freight paid through PowerTrack, about **1-1.5%** "improper or duplicate", all modes, unverified. Federal post-payment audits issue about **$11M a year** against an estimated **$16.3B** of all federal transport spend.
- **Vendors** (*assumed*): 4.75% of 250,000 LTL invoices carry an error, by count (AFS); carrier billing accuracy "97%" (SJ Consulting, via a broker's repost).

**Worked example [our calc], to show what the numbers can and can't say** (updated 2026-10-09 to the adopted lines; the earlier versions are in §13.3 and §13.9):
- Take the four smaller government auditors' **1.66%** flagged.
- **Against the adopted lines** (`4_kill_conditions.md` §2.5.11, §2.5.12), it sits **between Cover and Pass**:
  - at a $1.5M shipper, above Cover (0.51%) and below Pass (6.44%);
  - at a $5M shipper, above Cover (0.25%) and below Pass (2.03%).
- **What that would mean:** at the middle values, a $1.5M customer that cost nothing to win would cover our first-year cost. It would not repay $10,000 of winning cost within a year. It falls just short even of the $2,500 column (1.99%).
- **Against the old 2026-09-22 lines** (superseded 2026-10-09), it would have sat above the 1.3% pass line.

But the inputs are government tender freight, self-reported, and flagged before payment. Our product is a look-back on a private shipper's paid bills. **This illustrates the range; it measures nothing.**

**Thrown out or narrowed:**
- the "neutral bracket" wording (these are the auditors' own reports);
- the DoD 1.49% as a single figure;
- the reading of the 0.068% as an error rate.

**Still to ask:** someone who has audited mid-sized private shippers' TL and LTL bills. How much did the last such audit find, as a share of spend, and how much was credited? (§0.4)

### A09-02 · Share one check catches · **Narrowed**
- Nothing replaces GAO 1992: one professional audit caught **72-78%** of what two audits found (*verified*).
- **New:**
  - in one year, five federal auditors flagged anywhere from **0.66% to 4.67%** of similar bills, a sevenfold spread (*verified*);
  - GSA **could not audit** DoD freight run through a 3PL (a third-party logistics firm) because "the shipper's rates are not available" (*verified*). An auditor without the rate agreement catches nothing. This is the same lesson as the practice audit.
- **Why this matters more now [our call]:** Test 1 measures what the software flags (the founders, 2026-10-08), so a weak set of checks would read low and could kill the card on its own. The look-back must run the full set of checks the product would ship, not a sketch (`4_kill_conditions.md` §2.5.10, answer 4).

### A09-03 · Share credited, and how fast · **Narrowed**
- No private-shipper credited share was found.
- **New:**
  - The Surface Transportation Board (STB, the federal freight regulator) says carriers *may* lawfully pay claims filed **after** the 180 days, voluntarily (*verified*).
  - Broker terms can bar the shipper from offsetting (deducting a disputed amount from a later payment).
  - A factoring trade body's training deck uses "under 3% dilution" for trucking only as an example. Dilution is invoice value a carrier never collects, for any reason.
- Part 378's timing is unchanged: the carrier must acknowledge a claim in 30 days and decide it in 60.
- **In the kill test:** the model's 75% is used until 5-10 of the pilot's disputes are decided; the measured share then replaces it (`4_kill_conditions.md` §2.5.8).

### A09-13 · How far first-year finds fall later · **Narrowed**
- No freight-specific decay series exists on the web.
- Government programme totals fell from about $47M collected (FY1987) to about $11M a year in notices (2007-09), but this can't be read as decay:
  - the two figures measure different things (cash collected before carrier refunds, against notices issued);
  - the 1998 pre-payment mandate was largely ignored (agency compliance 0-77%; GSA OIG 2013).
- The vendor pattern on file (falls of 50-85%, check AB) stands alone (*assumed*).
- **Under a subscription [our call]:** this is a renewal risk. If finds fall in year two, the shipper gets less back for the same monthly fee.

---

## 5. The claim window (A09-10)

| Kind of freight | What the texts say | Verdict |
|---|---|---|
| **Direct LTL, carrier-billed, under a tariff** | 49 U.S.C. 13710: the shipper must contest within **180 days of receiving the bill**. The STB calls this "a prerequisite to any sort of relief"; the 10th Circuit called it "not optional" (2021) (*verified*). **But two big LTL carriers' own tariffs start the 180 days at the shipment, not the bill:** ODFL Item 396, ABF Item 428 (*verified*) | **Answered** |
| **Contract (non-tariff) freight** | The 10th Circuit: the contract-carriage section "says nothing that contradicts" the 180-day limit. A contract may expressly waive it either way: one large shipper's terms **extend** clerical and duplicate claims to **18 months**; one broker's terms **shorten** disputes to **5 days**. **No count exists of how often contracts waive it** | **Narrowed** |
| **Broker-billed freight** | Part 378 covers only carriers. Whether 13710's 180 days reaches a broker's own invoice is untested in court. In practice **the broker's terms govern: 5 days, 30 days, 30 days, 30 days from an adjustment, and 30 business days** in five public terms aimed at small shippers (*verified*). Two of the five are word-for-word the same template | **Narrowed** |

**Worked example [our calc]** (bills spread evenly through a 12-month look-back):
- **Under 180 days from receipt:** about **49%** of the bills are still in the window if claims go in on day 0, and **41%** if they go in on day 30.
- **Under broker terms:** **1-12%**.
- **Under an 18-month contract clause:** **100%**.

**And the reviewer's added calculation** for a **monthly** checking cycle, with disputes filed 5 days after month end:
- **83%** of bills are still inside a 30-day broker window;
- **17%** are inside a 10-day window;
- **0%** are inside a 5-day window.

So **broker-billed freight with 5-10-day windows can only be caught by checking each bill as it arrives** **[our calc]**. The software's intake has to do this, and the customer's staff have to work those flags within days (§9 item 1).

**Still to ask (a transportation lawyer):** does the 180-day rule bind contract-rate truckload freight and broker invoices, and how often do shipper contracts waive it? (§0.4)

---

## 6. The customer's own facts, and what audit firms and software charge

Under D-23 the review is the customer's own work. So A09-05 to A09-08 and A09-15 to A09-17 describe the customer's workload and our reading cost, and A09-04's prices are what audit firms and software charge: benchmarks for the subscription level, which is a Q6 decision. The evidence found on 2026-10-07 is unchanged; the notes it carried are in §13.4.

### A09-04 · What audit firms and software charge · **Narrowed**

**Audit firms** (they do the checking and filing themselves):

| Price found | Who | Label |
|---|---|---|
| **23.23%** of motor-freight refunds (first post-payment audit), **38.61%** (second) | CT Logistics, current federal price list, contract year from 7 May 2026 | *verified* (stated ceiling price to government) |
| 10% / 25%, or $2.36 a bill | GMG, federal list 2011-16 (expired, no purchase found) | *verified*, old |
| 13.5-40% (nine bids); winner 20% | Virginia 2004 tender, **general accounts-payable recovery, not freight** | *verified*, neighbouring market |
| 50% | Parcel-first audit firms | *assumed* |

**Software** (check AS, 2026-10-08; `4_kill_conditions.md` §2.5.3, §2.5.5):
- **Booking tools with an audit screen** publish small monthly prices: Freightview $149 a month for up to 50 shipments, MyCarrier $0 / $60 / $200 a month, Kuebix $69 / $253 a month (*verified* list prices). A $2M shipper's 250 or so bills a month fall in tiers priced by quote.
- **One audit-software listing** publishes $2,500 a month per unit, with units scaling by volume (AuditRes; 0 ratings, no other web presence found).
- **Where the customer files, the published price is a subscription or flat fee;** where the vendor files, it is usually a share. No freight software was found where the customer files and the vendor takes a share (check AS, *verified* vendor pages; an absence in public pricing, not proof none exists).
- **New entrants market against contingency:** "client keeps 100%" at $2,500-4,000 a month (check Z, *assumed*).

**Reading [our call]:**
- the model assumes our subscription is at most a quarter of what the shipper gets back. At a $2M shipper at the middle values that is about **$197 a month** **[our calc]**, in the range of the small tiers above (`4_kill_conditions.md` §2.5.10, answer 1);
- what a mid-sized private shipper will **sign** is not public. The price test and a signed letter of intent measure it (§0.3, D3).
- **Something odd that is real:** both federal lists charge **more** for a second pass over the same bills.

### A09-05 · Invoices per $1,000 · **Narrowed**
- **The carriers' own 2025 figures:**
  - Old Dominion: **$492.01** of revenue per shipment, so 1,000 ÷ 492.01 = **2.03 bills per $1,000** **[our calc]**;
  - ABF: **$532.18**, or **1.88** (its average includes U-Pack household moves).
- **Shipments lighter than the carrier average** mean **more** bills per dollar. The ABF practice account ran 2.21.
- **Worked example [our calc]:** a shipper with **$2M of LTL-only spend** at Old Dominion's average gets about **4,060 bills a year**. The model assumed **3,000**, which mixes LTL with truckload. A shipper's own LTL/TL mix sets the real figure, and no public source gives it.
- **What it moves:** our reading cost, and how many bills pass through the customer's queue.

### A09-06 · Share of bills flagged · **Narrowed**
Only neighbouring measures:
- accessorials are **8.0-8.7%** of LTL dollars on a 3PL's $1.2B book (2023; the same white paper gives both figures);
- detention (a fee for keeping a driver waiting) occurs at **39.3%** of truck stops (ATRI, 2023);
- "some shippers report 25 to 30 percent" re-rated (traced to Old Dominion's own paper; *assumed*);
- 14-18.4% of accounts-payable invoices are exceptions (Ardent, *verified*; `4_kill_conditions.md` §2.5.3).

The practice audit's **58%** remains the only measurement on a real account. Every one of these bills is a flag the customer's staff must look at, false ones included (Test 3).

### A09-07 · The customer's minutes per flag and per dispute · **Narrowed** / **not answerable**
- **The federal per-bill prices bound an audit firm's clerk time** **[our calc]** (they bound no cost of ours):
  - $2.79 per EDI bill (EDI is the electronic invoice format bigger carriers send) ÷ $36.79 an hour = at most **4.6 minutes**;
  - **$4.68** per hard-copy or **PDF** bill = at most **7.6 minutes**;
  - both before overhead and margin, averaged across all bills;
  - at a $25-an-hour clerk, 6.7-11.2 minutes.
- Vendors claim 1.2-1.6 minutes a bill. One vendor's own sheet claims both 5 hours a week and "50 hours per week" saved (*assumed*, internally inconsistent).
- **Check AQ's neighbours** (`4_kill_conditions.md` §2.5.3): a processing exception takes 15 minutes in the Australian Tax Office's calculator (*verified*, 2016 estimates); a retail deduction about 52 minutes (CRF, an analogue); an ocean-freight dispute 60-150 minutes. **No source times a freight flag that arrives already explained.** The model uses 10 minutes a flag and 30 a dispute **[our call]**.
- **Minutes per TL/LTL dispute:** not found anywhere.
- **Proven only by timing the shipper's own reviewer** in the look-back (§0.5, step 4).

### A09-08 · Carriers, agreements and onboarding · **Narrowed**
- **Carriers per shipper:**
  - three real shippers paid **14-17 trucking firms** in 90 days;
  - the top three took 42-52% of dollars, and **6-9 firms** made up 80%.
- **How often prices change:**
  - each LTL carrier raises its general rates about **yearly** (ABF **5.9%**, June 2026);
  - contract renewals run all year;
  - fuel surcharge percentages move **weekly**, and the tables are reissued.
- **SMC3's CzarLite** (LTL base-rate software): listed at $800 in 2022, unit not stated. An agency paid SMC3 $8,764 a year for web access (check AR). Whether we need a licence per customer is unknown; the model assumes $0, checking against the customer's own agreements first.
- **Hours to load one rate agreement, and the price of rate-loading services:** not found.
- **Under D-23** the customer uploads its agreements and confirms the rules the software reads (A09-17). Our part is support (about $175 a year), hosting (about $60) and onboarding help ($185-616 in year one) (check AR; `4_kill_conditions.md` §2.5.3).

### A09-09 · How much TL+LTL a segment firm buys · **Narrowed**
- **Three new real payment lists** (*verified* filings; annualised from 90 days, **[our calc]**):

  | Firm | Revenue | Trucking spend a year |
  |---|---|---|
  | Latex-foam maker | $53M | about **$1.53M** |
  | Coatings maker | $45M | at least **$1.84M** |
  | Farm-supply distributor | $221M in 2021, falling to a $48M run-rate in 2022 | about **$1.91M** |

  That is **0.9-4.8% of revenue**, depending on which year's revenue is used.
- **All are bankrupt**, which may distort their spending.
- With check AD's nine small LTL shippers, that makes 12 real firms. The spread across 95,579 segment firms is still unknown.
- **What it moves:** which row of the Kill / Cover / Pass table applies (§0.1).
- **Check AT (2026-10-09), from 30 public firms' freight disclosures, two more bankruptcy payment lists and BEA's industry tables** (`research/s5_check_AT_c09_freight_spend_by_size.md`, with its adversarial review: 0 discarded, 2 narrowed). TL+LTL as a share of revenue, central (low-high) **[our calc]**:
  - distributors (SG1) **1.14%** (0.33-3.81%);
  - makers: SG2 2.57%, SG3 3.83%, SG4 3.24%, SG5 3.48%, SG6 about 3.85% (the review's figure; AT's 5.15% rested on one line that included warehousing).
  - **The guessed TL+LTL share of outbound freight does most of the work** (56-79% of every central), and most filings date from 2016-18 and leave out inbound freight.
  - **Revenue is a weak screen:** real firms of the same size range from $0.2M to $1.9M of trucking. Own trucks, collect terms and parcel pull it down.
  - **The pool:** about 7,900 firm-industry entries in the six segments sit between $1.5M and $10M of estimated spend (Census 2022; double-counted).

### A09-12 · Offshore review · **moot** (D-23)
We employ no reviewers, so where review happens is no longer our question. The evidence found is kept in §13.4. **The question that survives** is whether shippers let a software vendor **store or process** invoice data outside the US. It goes with data handling (D-18) and the data-privacy lawyer in §0.4.

### A09-14 · Brokers, minimums, reweighs · **Narrowed**
- **Brokers:** at six real shippers, brokers took **0% to 52.4%** of trucking dollars (65% at most), median **15-17%** **[our calc]** on court filings. **It is a property of each firm.**
- **Minimum charges:** only a proxy, "over 60 percent" of LTL shipments weigh under 500 lb (2012).
- **Reweighs:** only the ABF practice set (26 of 101 bills).

### A09-15 · Follow-through · **Not answerable from the web**
*Added 2026-10-09 from check AQ (2026-10-08; `4_kill_conditions.md` §2.5.3).*
- **Not measured anywhere.** The model's 60%, dollar-weighted, is **[our call]**.
- **Neighbours:**
  - exceptions that block payment get worked, in about 4 days (APQC, *assumed*);
  - "Many shippers use a percentage or dollar threshold under which they won't dispute"; complaints "abandoned because they didn't have the resources" (ocean freight, 2017, *verified* as reported);
  - Freightview's example tolerance accepts bills up to 3% (LTL) or $50 (truckload) over without review (*verified*);
  - retail suppliers write off deductions under a median $10-25 (CRF, *verified*, an analogue).
- **Proven only by the pilot:** one watched look-back reads 100% while someone watches, and credits take months.

### A09-16 · The customer's hours · **Not answerable from the web**
*Added 2026-10-09 from check AQ.*
- **Vendor-reported workloads only:** from 5 hours a week for 200 bills to 15-20 hours a week (*assumed*). No neutral figure.
- **The model [our calc]:** a $2M shipper needs about 12.5 hours a month at 15% of bills flagged, against an assumed capacity of 20 **[our call]**. At the practice audit's 58% it is about 30 hours; on an LTL-heavy account, about 45 (`4_kill_conditions.md` §2.5.4).
- **The hours are treated as capacity, not dollars** (the founders, 2026-10-08). The wage, $36.79 an hour, is a sensitivity only.

### A09-17 · Self-serve onboarding · **Not answerable from the web**
*Added 2026-10-09 from check AR.*
- **No completion rate for customers loading their own contracts** was found anywhere.
- A strong table reader gets every cell right in only **69%** of complex tables (PubTables-1M, *verified*), so the customer's confirmation step is needed.
- **Our help costs little either way:** $185 self-serve against $616 assisted, which moves payback at $2M only from 67 to 70 months. **Whether customers finish onboarding unaided matters more** (`4_kill_conditions.md` §2.5.6).

---

## 7. The carrier side, and sharing documents

### H09-C1 · Short-pays and disputes · rules **answered**, practice **not answerable**
- **The rules, from ten LTL carriers' published rulebooks (tariffs) plus Landstar's (*verified*):**
  - Nine of ten bar short-paying or offsetting in so many words.
  - **Five revoke all discounts:** Saia automatically when the credit period runs out, Estes after notice, and XPO, R+L and FedEx Freight when an unpaid bill goes to an outside collector.
  - **Four charge 25-35%** liquidated damages: SEFL, ABF, ODFL and AAA Cooper.
  - ODFL and AAA Cooper make the shipper pay **twice** if an intermediary fails to pay the carrier.
- **Worked example [our calc]:** a real ABF bill of **$942.02** carries an 89.5% discount. If all its discounts were revoked, it would become about **$9,063-9,245**, 9.6-9.8×. The STB said in 1997 that such charges must "bear a reasonable relationship" to the cost of collecting, so this is a ceiling written in tariffs, not a cost shown to be enforced.
- **Design reading [our call]:** the software should tell the customer's staff to dispute through each carrier's own channel and never to short-pay. FedEx Freight's rule says only that bills **not** disputed through its channels are due on terms; it doesn't say a dispute stops the penalty clock.
- **Practice** (how often carriers enforce these penalties, and what chasing costs them): not on the web (§0.4).

### H09-C2 · Paying for faster payment · **Narrowed** (parked in part)
- **What carriers pay today:**
  - brokers' quick-pay programmes cost carriers **1.5-4%** (RXO 2.5% and 4%, Werner 2.5% / 1.5%; *verified* published terms);
  - U.S. Bank: a **1%** base fee, plus a surcharge whenever the prime rate is above 6%. So **$25 on a $2,000 load is a floor.**
- **Going the other way:** ABF charges **payers** 2% for certain card payments.
- **Not answerable from the web:** whether a carrier that bills a shipper directly would pay to join a new payment rail. This is parked anyway, since version 1 is audit only.

### H09-C4 · Carriers and outside firms' claims · **Narrowed**
- **This matters once we help customers file.** In version 1 the shipper's own staff file the claims, so these limits on agents and third parties don't apply yet (D-23).
- **TForce** bars agents and third parties from requesting **guarantee refunds**, outright.
- **FedEx Freight** may refuse a third party's Money-Back Guarantee request "at the sole discretion of FedEx Freight", and gives some of its other guarantee refunds "upon request of the debtor only".
- **AAA Cooper:** claims "must be submitted by the responsible party".
- **XPO** wants the pricing agreement attached to a claim.
- **ODFL and TForce close a claim once settled**, so a second auditor can't reopen it.
- **The federal rule still lets an agent file overcharge claims** (49 CFR 378.2(f)).
- No carrier statement about audit firms as such was found.

### A09-11 · Sharing agreements and invoices · **Narrowed**
- **TForce Item 130** (*verified*, re-checked word for word):
  - pricing agreements "shall be held in strict confidence by all parties, including the agents of the customer";
  - the shipper must "notify any Third Party or auditor of the confidential nature of the rates".
  - So the rule **expects an auditor to see them, under confidentiality**.
- **FedEx Freight Item 250** allows disclosure only when "required by law". FedEx's parcel template also needs FedEx's consent **and** an NDA with FedEx.
- **The one negotiated contract read** (YRC–First Brands, Art. 23(e)) **carves out auditors** checking freight charges.
- **8 of 10** LTL rulebooks have no rate-confidentiality item.
- **Reading [our call]:**
  - a shipper's "no" in kill Test 2 may be **contractual**, not reluctance;
  - the NDA should be built so it meets carrier clauses like TForce's;
  - **so should our terms of service,** since the customer now uploads its agreements into our software;
  - and the interview should ask **which carriers' agreements carry a confidentiality clause** (§0.3, E2).

---

## 8. Facts for four decisions (not the decisions)

These feed D-15, D-16, D-18 and D-19 in `C09-business-proposal.md` §8.2. **They stay with you, to settle together.**

| Decision | Facts found | Label |
|---|---|---|
| **D-15:** prices for the assessment and pilots | **Free first looks are the norm:** 3PLs offer "100% free", "no cost, no obligation" freight-bill audits to win freight, and SMB audit software offers free trials. **No published price** was found for a paid one-off assessment or pilot, or for a look-back priced differently from ongoing work. Federal lists price the **second** pass higher. *Since 2026-10-08:* the founders plan the C-09 look-back free of charge; a test price for the subscription is still theirs to set before the first close (kit §6.1) | *verified* (stated offers) |
| **D-16:** incentives | **IRS:** from 2026, payments to one person of **$2,000** or more a year must be reported (adjusted for inflation from 2027); re-checked at irs.gov. **Gift rules:** some firms' supplier codes ban cash and cash equivalents from current **or prospective** suppliers (Flex, $25 cap) or cap non-cash gifts at $50 (DRiV), so a gift card can be refused. No mid-sized manufacturer's code was found. A commercial research firm offers $150 for a 60-minute industry interview | IRS *verified*; norms *assumed* |
| **D-18:** data handling | **Common Paper's mutual NDA** (free, CC BY 4.0) lets the receiver share with advisers on a need-to-know basis, **but by default lets it keep copies under its backup policies.** That clashes with "delete after the assessment" unless the cover page changes it. A published letter-of-authority template exists (Logistics Plus). Nacha (the US bank-transfer rules body) requires large users to make stored bank account numbers unreadable. No freight-audit firm's published retention period was found | *verified* |
| **D-19:** the time box | **Panels:** a first qualified applicant in 15-77 minutes, a first booked session in about 24 hours (vendor figures). **Cold outreach:** at sales benchmarks of 0.74-3.43% replies, **5 interviews need roughly 290-1,350 people contacted**, if half of the replies book **[our calc]**. Nothing measures *research* requests to finance, logistics or carrier staff | *assumed* (vendor benchmarks) |

**Flag (your rule on paid hours) [our call]:**
- Most per-invoice and audit-and-pay offers found are sold on **staff time saved**. Check AS's review counted time wording on 22 of 35 vendors' pages (`research/s5_check_AS_adversarial.md`).
- Our subscription must not be sold that way. Under D-23 the software asks the customer's staff for hours rather than cutting them, and the saving is recovered overcharges.
- So never pitch it as "saves your team time".

---

## 9. New things the design should know about **[our call]**

None of these is a decision. Each is listed with what it touches.
1. **Broker-billed freight needs checking on arrival.** Windows of 5-10 days defeat a monthly cycle (§5). *Touches:* the software's intake (`software-initial-pitch.md`), the look-back's in-window share (A09-10).
2. **Some carriers start the 180-day clock at shipment** (ODFL, ABF). *Touches:* in-window arithmetic.
3. **Carrier confidentiality clauses** (TForce, FedEx Freight) may stop a shipper from sharing. *Touches:* kill Test 2, the NDA (D-18), the interview's document ask.
4. **Short-paying can be expensive under some tariffs.** *Touches:* how disputes are filed (through carrier channels, not by withholding).
5. **Free first looks are the market norm.** *Touches:* D-15.
6. **A new entrant:** nShift Audit reaches general availability in October 2026 (*assumed*, from its own buyer's pack). *Touches:* the competitor map (`C09-business-proposal.md` §6).
7. **An auditor without the rate agreement catches nothing,** as GSA found on DoD's 3PL freight. This confirms the practice audit's lesson.

---

## 10. Who to ask: the contacts

**Names and contact details are kept outside the project** (`5_interview_kit.md` §1.3):
- `~/Documents/personal/bio/freight_private/c09_contacts.md`, the list;
- `~/Documents/personal/bio/freight_private/c09_contacts_review.md`, its adversarial review. **The review governs.**

This section gives counts and organisations only. **Claude contacted no one.** The expert questions to put to them are in §0.4.

**What survived the review:**
- **56 named people** (11 graded A, 35 B, 10 C) and **21 organisational routes**, every one confirmed on the page cited.
- **5 dropped:** one has left the role; one's evidence was misread (re-checked: the "$150,000 recovered" was lost sales avoided on one shipment, not an audit recovery); three had no published route and stale sources.
- **Tags trimmed on 25**, of whom 11 are now useful only for referrals.

**Grades:**
- **A:** role and route confirmed on an official page within 24 months, and expertise shown in their own work;
- **B:** role confirmed officially, but the route is generic or the page is older;
- **C:** a single secondary mention.

**Contacts per question after the review** (named people at grade A or B):

| Question | A+B | Who they mostly are | Weak spot |
|---|---|---|---|
| A09-01 the leak | 4 | audit-firm principals, a government audit office | **No A-grade contact.** Auditors will quote their own books |
| A09-02 share caught | 3 | audit firms | At the floor |
| A09-03 share credited | 8 | audit firms, government, carrier and payment side | — |
| A09-04 prices | 9 | audit firms, a university procurement office, analysts | What a **private** mid-sized shipper signed: only shippers know |
| A09-05 invoices per $1,000 | 3 | audit and payment staff | At the floor; only the shipper's own count proves it |
| A09-06 share needing a person | 4 | audit-firm operations | No A grade |
| A09-07 review minutes | 5 | audit firms, a government contractor | The customer's minutes per flag and per dispute come only from timing their own reviewer in the look-back |
| A09-08 fixed cost | 6 | audit firms, SMC3, procurement | — |
| **A09-09** how much a segment firm buys | **1** | a bank's freight-payment analytics team, via its press office | **Weakest.** Only shippers' payment files prove it |
| A09-10 claim windows | 13 | **transportation attorneys (8 at A)**, including counsel on both sides of *Gaines* and *Southern Furniture* | Best covered |
| A09-11 sharing under an NDA | 7 | attorneys, associations | Whether shippers *will* share: only shippers |
| A09-12 offshore review | 4 | audit firms with offshore centres, a procurement office | Moot under D-23; keep these contacts only for the data-storage question (D-18) |
| A09-13 first-year decay | 3 | audit firms, government | At the floor |
| A09-14 brokers, minimums, reweighs | 8 | audit firms, attorneys, SMC3, analysts | — |
| H09-C1 carriers and short-pays | 10 | carrier-side attorneys, carrier finance | No named carrier billing or credit manager is public |
| H09-C2 carriers and faster payment | 7 | payment providers (they sell early pay) | Conflict: they sell the thing |
| H09-C4 carriers and audit firms' claims | 5 | carrier-side attorneys and finance | Practice needs carriers' own staff |
| **D-18** data handling | **0** | — | **None.** All five candidates were transportation lawyers with no work on NDAs or data retention. A data-privacy lawyer was never searched for |

A09-15 to A09-17 (follow-through, the customer's hours, onboarding) were added after the contacts search, so no contact was searched for them. Shippers answer them; the audit-firm principals can give claims about their clients (§0.4).

**Shipper prospects, the people C-09 would sell to** (check AU, 2026-10-09; `research/s5_check_AU_c09_prospect_sizes.md` and its adversarial review):
- **The contacts above are experts, not customers.** Only four are shippers, and all four are far larger than the target or already use an audit-and-pay provider.
- **Check AU named 76 mid-sized shippers** in the six segments, 51 of them sized. The review re-checked 45 figures at the source and discarded none. It moved 5 firms out of their segment (2 into an excluded industry) and added 1 acquisition and 1 provider flag.
- **Recomputed on check AT's ratios [our calc]:** 26 independent firms sit at $1.5-10M of estimated TL+LTL spend (9 at $5-10M). 3 sit above $10M, where audit-and-pay providers say they start; 10 fall below $1.5M.
- **The names, routes and a ranked call list are kept outside the project:** `~/Documents/personal/bio/freight_private/c09_prospects.md`, `c09_prospects_review.md` (governs) and `c09_call_list.md`.

**The best free routes:**
- **The Transportation & Logistics Council (TLC) Q&A Forum.** Non-members may "submit one transportation-related question at no cost"; transportation attorneys review it. **[our call]:** use it on A09-10, the claim window for contract and broker-billed freight.
- **ATA's National Accounting & Finance Council** (its Credit & Collection study group), for carriers' view of short-pays and audit firms (H09-C1, C4).
- **GSA's Transportation Audits Division policy mailbox**, for government overcharge and credit figures (A09-01, 03, 13).
- **The University of Pittsburgh's purchasing office**, for its freight-audit RFP's pricing workbook and data-security assessment (A09-04, 12).
- **Shippers' and carriers' associations:** NITL (National Industrial Transportation League) and SMC3.
- **Dead websites:** NASSTRAC's now shows unrelated casino content, and AST&L's redirects elsewhere, so neither is usable as a route today.

**Events that put several contacts in one room:**

| Event | Dates | Where |
|---|---|---|
| TLC's online claims seminar | Oct 20-29, 2026 | Online |
| CONECT (with a freight audit-and-pay panel) | Oct 21-23, 2026 | Newport, RI |
| NITL Engage Policy Forum | Nov 30-Dec 2, 2026 | Washington, DC |
| SMC3 Jump Start | Jan 25-27, 2027 | Atlanta |

**Paid fallback:** expert networks. One self-serve marketplace publishes about **$840 for a 30-minute call** (*verified*, its own page), about 3-4 times a panel interview with incentive (check V). This bears on D-16.

**Before any outreach [our call]:**
1. **Many contacts sell audit services** and will pitch. Three of the audit firms also sell freight services (brokerage or LTL). Say plainly that it is research, and never pose as a buyer.
2. **Some email addresses are hidden by anti-spam scripts** on their pages. Click the link on the cited page; don't type the address from the list.
3. **The people who matter most aren't on the web.** Mid-sized shippers and carrier billing staff come from the referral ask at the end of each interview: "Who is the one person you would call with a question about a carrier bill?"

---

## 11. Inconsistencies found on the way, for you to confirm

These were found in existing files while mapping what was already known. **None has been changed, except item 8,** an arithmetic slip inside this file.

| # | Where | What differs | Source of each value |
|---|---|---|---|
| 1 | A09-14 reweighs | `C09-business-proposal.md` §8.1 says **26 of 101** bills carry a reweigh note; `handoff_s5_interviews.md` §6.2 says **28%** | Two counts of the same ABF bills: the practice audit §3 (26) and check AC §1.3 (28, by script). The minimum-charge counts also differ (43 vs 39 adjustments) |
| 2 | U.S. Bank 1% early-payment fee | Labelled *assumed* in `C09-business-proposal.md` §8.1 | Check Z §10.1 and `6_focused_target.md` §7.5 read the carrier agreement itself (revision R 9.2020), so *verified* for that revision; check AO's reviewer adds the prime-rate surcharge |
| 3 | A09-07 | Check AA §14 says no job posting states an invoice volume | Check Y §1.2 row 18 (Worldpac) states "approximately 2,500 carrier invoices per week" |
| 4 | Kit screen | `5_interview_kit.md` §5.1 still screens on **100-499** staff | The proposed screen (item 8 in §8.2) is 20-499 staff; partly applied |
| 5 | Credited share | Check X's model uses **80%** | `4_kill_conditions.md` §2.2 uses **75%** (check AB §7.2) |
| 6 | Kill Test 1's lines *(added 2026-10-08)* | The 1.3% and 0.75% lines were worked out for the overcharge rate **before** the 70% catch share (fee = rate × 0.70 × 0.75 × 0.25). Test 1 measures what the look-back **flags**. If the look-back catches about 70% of what is there, as one professional audit does (GAO 1992), the frozen lines in effect require about **1.86%** true overcharges to pass and **1.07%** to avoid the kill. Test 3, fed "the measured rate", would then apply the 70% a second time. If the look-back is taken to catch every provable error, the lines stand as derived | `4_kill_conditions.md` §2.3-§2.4; a question of definition for the founders. The lines themselves are frozen and unchanged. *Since D-23 (2026-10-08) the lines' whole basis is being re-run (`handoff_c09_software_rerun.md`), which carries this question into the new lines.* **Answered 2026-10-08 (founders): "Flagged."** Test 1 measures what the software flags and the reviewer accepts (`4_kill_conditions.md` §2.5.8, §2.5.10) |
| 7 | The customer's hours *(added 2026-10-09)* | The kit's "who works the flags" block (§5.1) says to ask about last month's **actual** hours, "never 'how many could you give it'". The adopted look-back design's step 1 (`4_kill_conditions.md` §2.5.8; kit §6.1) asks **how many hours a month the shipper can give** the queue, recorded before timing. Both are kept, each in its place (§0.3, F1 and F2). Confirm that this is what you intend | The kit's rule follows the interview discipline (kit §1); the look-back's question sets Test 3's limit |
| 8 | A09-07 in §2 *(added 2026-10-09)* | The 2026-10-07 answer table said "at most **4.4**-7.6 minutes"; §6 and this file's 2026-10-08 banner say **4.6** | $2.79 ÷ $36.79 an hour = 4.55 minutes **[our calc]**, so 4.6 is right. Corrected in §2 on 2026-10-09; the original row is in §13.2 |

---

## 12. Files

| What | File |
|---|---|
| The leak and the recovery: research, then review | `research/s5_check_AM_c09_leak_and_recovery.md`, `research/s5_check_AM_adversarial.md` |
| Running the service, the customer's facts: research, then review | `research/s5_check_AN_c09_service_and_customer.md`, `research/s5_check_AN_adversarial.md` |
| Carriers, sharing documents, interview logistics: research, then review | `research/s5_check_AO_c09_carriers_and_access.md`, `research/s5_check_AO_adversarial.md` |
| Contacts: method and counts, then review | `research/s5_check_AP_c09_contacts.md`, `research/s5_check_AP_adversarial.md` |
| Contacts with names (**outside the project**) | `~/Documents/personal/bio/freight_private/c09_contacts.md` |
| The customer's side, our cost, the market's prices (2026-10-08): research, then review | `research/s5_check_AQ_c09_customer_review.md`, `research/s5_check_AR_c09_software_cost.md`, `research/s5_check_AS_c09_market_models.md`, with `research/s5_check_AQ_adversarial.md`, `research/s5_check_AR_adversarial.md`, `research/s5_check_AS_adversarial.md` |
| The kill test on the software basis: the lines, the inputs, the founders' answers | `research/selection_runs/run-01/4_kill_conditions.md` §2.5 (§2.5.8 the tests, §2.5.10 the answers, §2.5.11 the Kill / Cover / Pass lines) |
| The questions in interview order, and the look-back method | `research/selection_runs/run-01/5_interview_kit.md` §5.1, §6.1 |
| The questions as first asked | `C09-business-proposal.md` §8 (the register as of 2026-10-08 is kept in its §13); `handoff_s5_interviews.md` §6.2 |

---

## 13. Superseded, kept for the record

*Added 2026-10-09.* Passages from this file that no longer fit the strategy, moved here **word for word** when the file was brought up to date (founders: "Clean rewrite + appendix"). They are kept so every change can be retraced. **Nothing here is current.**

### 13.1 From the header

The status line and the D-23 banner as they stood on 2026-10-08:

> **The ask, verbatim:** "find any web resources you can as to answers to these questions … If nothing is sufficient, then find contacts I can reach out to (as many as possible, as reliable as possible) … I want adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data."
> **Status: this document decides nothing.** No frozen line moves, no model number is changed, and none of the §8.2 decisions is taken. Claude contacted no one.
>
> **Update 2026-10-08: D-23, a software company, not an audit firm.** The founders decided that C-09 is software: it flags the bills, and the **customer's own staff** review them and file the disputes. We employ no analysts. The record is in `software-initial-pitch.md` §1A, and the kill test is re-run in `handoff_c09_software_rerun.md`. **The evidence below stays true; what changes is what some of it bears on:**
> - **A09-12 (offshore review) is moot.** We have no reviewers, onshore or offshore.
> - **A09-06 and A09-07 now measure the customer's workload,** not our cost: how many flags their staff must work, and for how long.
> - **The 4.6-7.6 minute bound** from federal per-bill prices (§6 A09-07) now bounds nothing of ours. It still describes what an audit firm's clerk time can cost.
> - **A09-04's public prices (23.23% / 38.61%, $2.79-4.68 a bill)** describe audit firms, a different business from ours. The fee form is now open: a share of recoveries or a subscription, modelled side by side in the re-run.
> - **H09-C4 is mostly moot for version 1.** The shipper files its own claims, so TForce's and FedEx Freight's limits on third parties don't bite. They matter again once we help with filing.
> - **A09-11 (sharing agreements) still matters:** the customer uploads its agreements into our software instead.

### 13.2 From §2: the answer table as of 2026-10-07

| ID | The question in plain words | Model value | **Verdict** | What survived the check (one line) |
|---|---|---|---|---|
| **A09-01** | How much of a mid-sized shipper's freight spend carriers bill wrongly, provably | 1.5% | **Narrowed** | Government auditors, checking bills **before payment**, report flagging 1.7-3.4%; after payment almost nothing is left. No private mid-sized shipper is measured |
| A09-02 | Share of real overcharges one audit catches | 70% | **Narrowed** | Nothing replaces GAO 1992 (72-78%). What auditors flag varies 7× between firms on the same kind of bills |
| A09-03 | Share the carrier credits, and how fast | 75% | **Narrowed** | No private-shipper figure. Carriers *may* pay claims filed after 180 days, voluntarily |
| A09-04 | The fee share shippers accept | 25% | **Narrowed** | Real public prices: **23.23%** (first motor-freight audit), **38.61%** (second), per CT Logistics' current federal list; parcel-first firms say 50% |
| A09-05 | Invoices per $1,000 of spend | 1.5 | **Narrowed** | LTL carriers' own 2025 averages: **1.9-2.0** (Old Dominion, ABF); lighter freight means more bills |
| A09-06 | Share of bills needing a person | 15% | **Narrowed** | Only neighbours: accessorials (extra-service charges) 8-9% of LTL dollars; re-rates "25 to 30 percent" at some shippers (one carrier's paper) |
| A09-07 | Minutes per review; cost per dispute | 6 min; $9.30 | **Narrowed**; dispute cost **not answerable** | Federal per-bill prices imply **at most 4.4-7.6 minutes** of clerk time a bill. Minutes per TL/LTL dispute: not found |
| A09-08 | Fixed cost per customer | $400/yr | **Narrowed** | Real shippers paid **14-17 trucking firms** in 90 days; rates change yearly, fuel weekly; hours to load an agreement: not found |
| A09-09 | How much TL+LTL a segment firm buys | screen $1.5M+ | **Narrowed** | Three new real payment lists: about **$1.5-1.9M a year** each, 0.9-4.8% of revenue. All are bankrupt firms |
| **A09-10** | The claim window | ~50% of a 12-month look-back | **Answered** for direct LTL tariff freight (180 days); **Narrowed** for contract and broker freight | **Broker terms give 5-30 days, not 180.** Two big LTL carriers start the 180 days at shipment, not at the bill |
| **A09-11** | Will shippers share agreements and invoices under an NDA | Test 2 | **Narrowed** | **2 of 10 LTL rules tariffs make rates confidential** (TForce, FedEx Freight). A "no" may be a contract, not reluctance |
| A09-12 | Is review outside the US acceptable | — | **Not answerable** *(moot under D-23, 2026-10-08: we employ no reviewers)* | Public buyers can forbid it (Ohio); nothing on private mid-sized shippers |
| A09-13 | How far first-year finds fall later | mature 0.5-1.5% | **Narrowed** | No freight decay series; government programme totals can't be read as one |
| A09-14 | Share via brokers, on minimums, with reweighs | ABF: 38% on minimum, 26 of 101 reweighed | **Narrowed** | Brokers took **0-52%** of trucking dollars at six real shippers (median ~15-17%) |
| H09-C1 | What carriers do when short-paid or disputed | — | Rules **answered**; practice **not answerable** | Nine of ten LTL tariffs bar short-paying; **five revoke all discounts** when an unpaid bill goes to collection or the credit period runs out; four charge 25-35% |
| H09-C2 | Would carriers pay for faster payment | — | **Narrowed** (parked in part: version 1 is audit only) | Brokers' quick-pay costs carriers 1.5-4%; whether a carrier billing the shipper directly would pay is unknown |
| H09-C4 | How carriers treat an outside audit firm's claims | — | **Narrowed** | TForce bars agents from guarantee refunds; FedEx Freight may refuse at its discretion; the law still lets an agent file overcharge claims |
| D-15 | Facts: what others charge for assessments and pilots | — | **Narrowed** | Free first looks are the norm; no paid assessment price found; the **second** audit pass is priced **higher** |
| D-16 | Facts: incentives, gift rules, tax | — | Tax **answered**; norms **narrowed** | IRS reporting threshold **$2,000** a year per payee from 2026. Some firms ban gifts from *prospective* suppliers |
| D-18 | Facts: NDA templates and data handling | — | Templates **answered**; retention **narrowed** | An open mutual NDA exists (Common Paper), but by default it lets the receiver keep backup copies |
| D-19 | Facts: recruiting time and reply rates | — | **Narrowed** | Cold-sales reply rates 0.74-3.43% imply roughly **290-1,350 people contacted** for 5 interviews; no figure for research requests to finance or logistics staff |

**What this means in one sentence [our call]:** the web has added real prices, real shipper payment lists and hard contract and legal facts, but **not** the overcharge rate on a mid-sized private shipper's own bills. That number is still measured only by the first real look-back, as `C09-business-proposal.md` §9 already says.

### 13.3 From §4: A09-01's worked example, and an old heading

**Worked example [our calc], to show what the numbers can and can't say:**
- Take the four smaller government auditors' **1.66%** flagged.
- ~~Apply our model's **75%** credited share: 1.66% × 0.75 ≈ **1.25%** of spend returned.~~
- ~~That sits just under the kill condition's **1.3% pass line** and well above its **0.75% kill line**.~~
- *Corrected 2026-10-08:* the step above compared different things. Kill Test 1 measures dollars **flagged** and provable, before any carrier credit (`4_kill_conditions.md` §2.4), so the credited share does not belong in the comparison. Flagged against flagged, **1.66% sits above the 1.3% pass line**, under either reading of the line in §11 item 6.

**Still to ask:** someone who has audited mid-sized private shippers' TL and LTL bills. How much did the last such audit find, as a share of spend, and how much was credited?

**A09-02 · Share one audit catches · **Narrowed****

### 13.4 From §6, then titled "Running the service, and the customer's own facts"

**6. Running the service, and the customer's own facts**

> *Note 2026-10-08 (D-23):* "running the service" here means the **service basis**: our analysts reviewing and filing. Under D-23 C-09 is software, so A09-06 and A09-07 below describe the customer's own workload, A09-12 is moot, and A09-04's prices are audit firms' prices. The evidence is unchanged.

**A09-04 · The fee share · **Narrowed****
- **Reading [our call]:** the model's 25% sits inside the range of public prices. What a mid-sized private shipper will **sign** is not public. That is what the price test and a signed letter of intent measure.

**A09-06 · Share of bills needing a person · **Narrowed****
The practice audit's **58%** remains the only measurement on a real account.

**A09-07 · Review minutes; dispute cost · **Narrowed** / **not answerable****
- **The federal per-bill prices bound the time** **[our calc]**:
- *Note 2026-10-08 (D-23):* these minutes are now the **customer's** time, not ours. The federal bound describes audit firms' clerk time and no longer bounds any cost of ours.

**A09-08 · Fixed cost per customer · **Narrowed****

**A09-12 · Offshore review · **Not answerable from the web****
- Ohio bars state service contracts performed outside the US without a signed waiver (*verified*).
- A 2005 survey of 158 US finance executives saw offshore outsourcing as a higher security risk. The often-quoted "76%" is **not in the archived article**, so it is unconfirmed.
- Nothing was found on private mid-sized shippers.
- *Note 2026-10-08 (D-23):* **moot.** We employ no reviewers, so where review happens is no longer our question. One related point may survive: whether shippers allow their invoice data to be **stored or processed** outside the US by a software vendor. That belongs with data handling (D-18) and the re-run's security question, not here.

### 13.5 From §7

- **Design reading [our call]:** dispute through each carrier's own channel, and don't advise customers to short-pay. FedEx Freight's rule says only that bills **not** disputed through its channels are due on terms; it doesn't say a dispute stops the penalty clock.

**H09-C4 · Carriers and outside audit firms · **Narrowed****
- *Note 2026-10-08 (D-23):* **mostly moot for version 1.** The shipper's own staff file the claims, so these limits on agents and third parties don't apply. They matter again once we help customers file.

### 13.6 From §8

| Decision | Facts found | Label |
|---|---|---|
| **D-15:** prices for the assessment and pilots | **Free first looks are the norm:** 3PLs offer "100% free", "no cost, no obligation" freight-bill audits to win freight, and SMB audit software offers free trials. **No published price** was found for a paid one-off assessment or pilot, or for a look-back priced differently from ongoing work. Federal lists price the **second** pass higher | *verified* (stated offers) |

**Flag (your rule on paid hours) [our call]:** most per-invoice and audit-and-pay offers found are sold on **staff time saved**. A contingency fee on recovered overcharges is not; a per-invoice price sold as "hours saved" would drift toward it. *Note 2026-10-08 (D-23):* the same holds for a software subscription. Under D-23 the software asks the customer's staff for hours rather than cutting them, so the saving stays recovered overcharges, as long as it is never pitched as "saves your team time".

### 13.7 From §10: three rows of the contacts table

| Question | A+B | Who they mostly are | Weak spot |
|---|---|---|---|
| A09-04 fee share | 9 | audit firms, a university procurement office, analysts | What a **private** mid-sized shipper signed: only shippers know |
| A09-07 review minutes | 5 | audit firms, a government contractor | ~~Dispute cost will come from timing our own look-back~~ *D-23: the customer's minutes per flag and per dispute come from timing their own reviewer in the look-back* |
| A09-12 offshore review | 4 | audit firms with offshore centres, a procurement office | Nobody has direct evidence of buyers' rules. *Moot under D-23 (2026-10-08); keep these contacts only for the data-storage question (D-18)* |

### 13.8 From §11 and §12

These were found in existing files while mapping what was already known. **None has been changed.**

| What | File |
|---|---|
| The questions themselves | `C09-business-proposal.md` §8; `handoff_s5_interviews.md` §6.2 |

### 13.9 Replaced when the founders adopted the new lines (2026-10-09, C29)

**From the header:**

> **The strategy now** (decided by the founders on 2026-10-08; …

> 5. **The cost of winning a customer is bounded at $0 to $10,000** until the first customer is timed. Test 1's lines are re-modelled at both bounds as **Kill / Cover / Pass** (§0.1). **They are proposed, not adopted,** so no look-back starts yet. P-31 is deferred.

**From §0.1:**

…(`4_kill_conditions.md` §2.5.11, **[our calc]**, proposed and not adopted):

**Status:** these lines are **proposed, not adopted.** The lines frozen on 2026-09-22 (`4_kill_conditions.md` §2.4) stay formally in force until the founders adopt new ones, and **no look-back starts before then.**

**From §0.5:**

**No look-back starts until the founders adopt new lines.**

**From §4, A09-01's worked example:**

…(updated 2026-10-09 to the proposed lines; the earlier versions are in §13.3):

- **Against the proposed lines** (`4_kill_conditions.md` §2.5.11), it sits **between Cover and Pass**:

- **Against the frozen 2026-09-22 lines,** still formally in force, it sits above the 1.3% pass line. Flagged dollars are compared with flagged dollars (the founders: "Flagged", §11 item 6).
