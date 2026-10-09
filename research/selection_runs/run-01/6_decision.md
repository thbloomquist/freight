**One thing first:** S6 is meant to come after S5, and S5 has only done its desk work. No interviews or savings assessments have run, `5_log.md` is empty, and none of the four cards has met the S5 gate. S4 also concluded that desk evidence can't rank these four. So everything below is desk evidence, and your first decision is when to choose.

## 1. The four candidates side by side

| | **C-09** Checking and paying freight bills | **C-11** LTL class disputes | **C-19** Retailer fines and deductions | **C-20** Import entries |
|---|---|---|---|---|
| Who would pay | The controller or accounts-payable team at mid-sized manufacturers and distributors | The shipping lead at small manufacturers and distributors | The CFO, controller or credit manager at suppliers to big-box stores | The owner of a small customs brokerage |
| Buyers | 95,579 | 235,684 | about 29,000 (15–55k) | 2,365 |
| Central fee pool | **$209M** | $62M | $33M | $54M |
| Average fee per buyer | ~$2,200/yr | ~$260/yr | ~$1,150/yr | ~$22,800/yr |
| **Customers needed for the $2.5M floor** | ~1,150 (1.2% of buyers) | ~9,500 (4.0%) | ~2,200 (7.6%) | ~110 (4.6%) |
| Axis A / Axis W (S4) | 92.5 / 55 | 92.5 / 62.5 | 82.5 / 62.5 | 92.5 / 65 |
| Fee gate (F1–F4 / F5) | 3.5 / 1 | 3.0 / 1 | 3.5 / 1 | 3.5 / **0.5** |
| Strict durability test | Passes for defensive shipper groups only | One of four industries fails, and the fee unit leans fail | **Clean pass** | Unknown, leaning fail |
| Ease of reaching buyers | Hard (no gathering place for the people who pay freight bills) | Middling | **Hardest** | **Easiest** (Customs publishes every brokerage) |
| Outside party it depends on | A bank partner, for the paying half | NMFTA's class-data licence | Retailer portals and retailers' dispute rules | Customs filing certification, for the filing half |

**Worked example for the "customers needed" row** (my arithmetic, central case at the modelled 20% fee share):
- **C-20:** $54M across 2,365 brokerages is about $22,800 each. $2.5M ÷ $22,800 ≈ 110 brokerages.
- **C-11:** $62M across 235,684 shippers is about $263 each. $2.5M ÷ $263 ≈ 9,500 shippers.

It's the same revenue floor with 86 times as many customers to sign. Cohen's check caught this and the scoring axes didn't.

---

## 2. What we learned about each card

### C-09 · Checking and paying truckload and LTL freight bills
Mid-sized manufacturers mostly pay carrier invoices as billed. (LTL, less-than-truckload, means several shippers' pallets share one trailer.) The job has two halves: check each bill against the agreed rate and the proof of delivery and recover overcharges, then pay the carriers.

**For it**
- **Biggest prize by far.** Its fee pool is 3–6 times any other card's. It's the only card that passed every knock-out with nothing left open.
- **Strongest fee case.** Contingency audit (the auditor keeps 25–50% of what it recovers) is already a standard contract. A recovery shows up as a credit memo you can trace. *Note 2026-10-08 (D-23): C-09 is now software, not an audit firm, so the fee form is open (a share of recoveries or a subscription), and with the customer filing, we no longer see the credit memos directly (§5.2).*
- **The only card that can sit inside the payment.** If we pay the carriers, the fee comes out of money that is already moving (R41: "if you bring the cash, you are king").
- **Most open field.** The two leaders each handle only about 4–5% of trucking dollars, and both aim at big companies.
- **Same data as its neighbours.** Bills of lading, proofs of delivery, invoices and rates also serve LTL disputes (C-11), cargo claims (C-10) and parcel audit (C-12).

**Against it**
- **Lowest Axis W (55).** Paying carriers takes months: ERP integration, a bank partner and signing up carriers.
- **Funded AI rivals are doing the same work.** Loop raised $95M in April 2026. Cass's own 10-K warns that AI could make its offerings obsolete.
- **Hard to reach.** It's bought through finance, not logistics, and check V found no place where these people gather. Interviews will probably have to come through paid panels.
- **The overcharge rate is our own guess.** We assume 1–3% of spend (vendors claim 2–8%), and the spend base itself is *assumed*.
- **Durable only in steady industries.** It passes the strict test for packaged goods, packaging, agribusiness and paper, and fails for auto, metals and homebuilding.

**Likely first product:** an audit-only look-back, with payments added later. That lifts Axis W from 55 to 65 and Cohen from 1 to 10.
**What S5 has to show:** does a look-back on one shipper's real invoices find 1–3% overpaid, and will a controller pay a startup a share of recoveries? *Note 2026-10-08 (D-23): and will the shipper's own staff work the flags the software raises, and pay for the software as a share or a subscription (§5.2).*

**Kill condition (frozen 2026-09-22):** `4_kill_conditions.md` §2. Kill under 0.75% and pass at 1.3% or more of in-window spend billed wrong and provable. §6 of that file adds its market test: $1M needs about 175 customers of ~$2.9M spend, with a thin margin at the central rate. *2026-10-08: the re-run on the software basis (D-23) is in `4_kill_conditions.md` §2.5, proposed and not adopted. Our cost per customer falls to software, but at the central rate a $2M shipper recovers less than it costs to win it within 12 months, whatever the fee form; proposed lines at a $1.5M shipper: kill under 0.78%, pass at 6.44%.* *2026-10-09 (C29): the founders adopted the software-basis condition, with the acquisition cost bounded at $0-$10k: at a $1.5M shipper, Kill under 0.044%, Cover 0.51%, Pass 6.44% (`4_kill_conditions.md` §2.5.12).*

### C-11 · LTL class, reweigh and reclass disputes
LTL carriers price by freight class (the NMFC tariff, run by NMFTA). After pickup, a carrier can reweigh or re-measure a shipment and rebill it, plus a $15–55 fee. Small shippers mostly just accept the new charge.

**For it**
- **Clearest forcing event of all 18 cards.** NMFTA's density dockets took effect 19 Jul 2025 and 23 May 2026. NMFTA itself warns of "billing surprises that hit weeks after pickup".
- **No standalone dispute tool was found**, while cheap shipping tools (from $149 a month) show these shippers do buy software.
- **Check T found the carriers' own rules help us.**
  - We may file disputes as the shipper's agent.
  - Carriers accept the shipper's paperwork from before pickup (a packing slip plus a spec sheet) as proof.
  - So a product that collects that evidence at pickup and files quickly fits their rules.

**Against it**
- **The money may be much smaller than assumed.**
  - FedEx Freight's filing puts all re-rating from its dimension scanners at about 0.8% of revenue.
  - The card assumes 2–5% is avoidable, and only part of that 0.8% is actually wrong.
- **Tiny fee per customer.** It needs about 9,500 customers to reach the floor.
- **Carriers hold the proof and have the final say.**
  - Scanner data is kept only 30 days after invoicing, and some tariff deadlines are short.
  - No neutral figure exists for how often corrections happen or how often disputes win.
- **NMFTA's licence could be a cost or a gate.** Nobody knows which, because terms for software serving many shippers aren't public. Only NMFTA can answer (D-20).
- **Weakest durability of the four.** LTL real revenue fell 25.7% in 2008–09, and fabricated metals fails the strict test.
- **It overlaps C-09**, since LTL bills are part of C-09's job.
- **Shippers who book through an LTL 3PL may not be able to dispute directly.**

**Likely first product:** collect evidence at pickup and file fast, not dispute after the fact.
**What S5 has to show:** do evidence-backed disputes win (at least 20% of the time), and what is the real correction rate?

**Kill condition (added 2026-09-22):** `4_kill_conditions.md` §3. Nine real small shippers in bankruptcy files bought a median of $94k of LTL a year. At that size the fee is about $123 a year at the central inputs, and about $820 even if every correction were wrong and won. **Eliminated by the founders on 2026-09-22** (D-22, `4_kill_conditions.md` §7.4).

### C-19 · Retailer on-time-in-full fines and deductions
Walmart, Target, Home Depot and others fine suppliers for late or incomplete deliveries, usually 3% of the goods' cost. They take the fine out of what they pay, and the supplier has to dispute to get it back.

**For it**
- **Cleanest on the checks.** The payer is the saver, since recoveries go back to revenue, and it's the only clean pass on the strict durability test.
- **The fee shape is proven.** Recovery firms already work for about 30% of what they recover.
- **The pain is growing.** Every dated rule change since January 2025 tightens the rules (Kroger, Target, Amazon), so A3 holds even under the strict reading.
- **The buyer count is now anchored.** Walmart publishes 31,196 supplier records, which puts the central count at about 29,000.
- **The gap is still open, but narrowing.** 55% of smaller suppliers used no deduction tool in 2023 (*assumed*), down from 70% in 2018.
- **Same buyer as C-09**, the controller at a manufacturer, so the two pair naturally.

**Against it**
- **Smallest prize.** Its $33M fee pool is barely over the $25M floor. The $10M stretch would need about 30% of all buyers, so growth has to come from neighbouring jobs.
- **Competitors are closing in on exactly this buyer.**
  - SPS Commerce already carries many suppliers' EDI (the electronic order and invoice feed).
  - In June 2026 it sold its Amazon-seller recovery business to focus on suppliers who sell to several retailers, which is this card's buyer.
  - Glimpse has raised $52M.
- **Retailers are pushing back on automated disputing.** Target fines a fifth or later dispute, Amazon ended bulk disputes, and Walmart's portal rejects carrier-generated delivery reports. High-volume disputing is exactly how a software entrant would work.
- **No open retailer APIs.** Access runs through the supplier's logins and bots, with separate setup for each retailer.
- **Short windows for delivery fines** (Home Depot about 4 weeks, Walmart 15–30 days). Back-claims on day one work mainly for shortages and invoice disputes.
- **Hardest to recruit.** The main events (CRF, RVCF, PLMA) fall in late October and November.

**Likely first product:** disputes only, starting where the windows are long.
**What S5 has to show:** are SPS users satisfied (that's the show-stopper test), and do 3 of 5 suppliers describe a recent fine with an amount?

**Kill condition (added 2026-09-22):** `4_kill_conditions.md` §4. At the neutral survey rates, a $5k-a-year customer starts at about $67M of big-box sales; at the rates vendors report, at about $10M. The lines, kill under 0.05% and pass at 0.17% or more of sales in provable invalid deductions, were **adopted and frozen on 2026-09-22** (D-22).

### C-20 · Import entries
Every import needs an entry filed with Customs: classify each product, work out the duty, and key in the invoice data. Small importers pay a broker $100–250 an entry, and the broker's staff do most of it by hand.

**For it**
- **The strongest dated triggers, acting on entries themselves:**
  - de minimis ended 29 Aug 2025, and informal entries tripled;
  - the Supreme Court ruled the IEEPA tariffs unlawful on 20 Feb 2026;
  - refunds on 53M+ entries opened 20 Apr 2026.
- **Easiest to reach.** Customs publishes every brokerage with an email address, and 14 regional associations meet monthly. It's the only card with W1 = 1.
- **The most office-heavy job of the 18**, with the best data connections.
- **Only about 110 customers needed for the floor.**
- **The broker is the hub.** Brokers sit between importers and Customs, so a helper tool for them "equips the hub" as S6 step 4 advises. As a helper that doesn't file, it scores Axis W 87.5 and Cohen 2.0, the best position on the whole S4 plot.

**Against it**
- **It isn't really a fee-from-savings business.**
  - The saving is broker labour, priced per entry (F5 = 0.5).
  - With 2,365 brokerages competing on price, the saving may get passed on to importers, which would leave us as just a usage cost.
  - That bends the CLAUDE.md fee rule rather than meeting it.
- **Crowded.** About 70 filing-software vendors (Descartes' NetCHB alone serves about 30% of brokers) plus AI classification tools. Consolidators could simply add the feature.
- **Low ceiling.** The $10M stretch needs about 18.5% of all brokerages. Durability is unknown, leaning fail, and some of today's volume is a tariff and refund spike.
- **Liability and certification limits.** Brokers' legal duty of care limits how far classification can be automated, and filing itself needs certification that takes months.
- **Nothing else on the shortlist shares its product core, data or buyers.** Backups would have to come from its own neighbouring jobs or from the reserve list (C-24 export documents, $12M).

**What S5 has to show:** will a small brokerage buy a helper that doesn't file, and does the broker keep the saving?

**Kill condition (added 2026-09-22):** `4_kill_conditions.md` §5. Cost to serve is trivial. Price is the risk, because the filing platforms now bundle the same AI at $0-25¢ an entry. **Eliminated by the founders on 2026-09-22** (D-22): viable on paper, but its saving is paid staff time, which the founders will not build for (`4_kill_conditions.md` §5.7).

### C-08 · Carrier vetting (demoted under D-9)
C-08 can't be the primary while the fee rule stands, because its saving is a theft that never happens. My own observation: its identity-checking core would fit C-09's paying half. Before paying a carrier, you'd check the payee is real, and payment fraud hit 76% of US firms in 2025. There the fee would ride on payments instead of on avoided theft, so it's a possible growth option if C-09 is chosen.

---

## 3. What matters most for the decision

1. **The unknowns are bigger than the gaps between cards.**
   - Every savings range rests on a removable share we guessed.
   - C-11's 2–5% already sits above FedEx's 0.8% figure, and C-09's 1–3% sits below what vendors claim.
   - One savings assessment on real data can move a card's A1 score a full band, which is more than any difference between cards (S4 factor 9).
2. **There are two families, and that shapes your backups.**
   - C-09, C-11 and C-19 are all "prove it and dispute it" jobs. They share a product core, shipper data and largely the same buyer.
   - Picking any one of them gives you two ready-made backups, plus claims (C-10) and parcel audit (C-12) as growth options.
   - C-20 stands alone.
3. **Size against cleanliness.**
   - C-09 is the biggest and messiest: hardest to build and reach, with funded rivals.
   - C-19 is the cleanest and the smallest, with rivals moving in.
   - C-11 and C-20 each carry one serious structural doubt: for C-11 the money and the customer count, for C-20 the fee shape and the ceiling.
4. **The first product matters more than the card.** C-20 swings 35 points of Axis W between "helper" and "filer", and C-09 swings 10 points between "audit only" and "audit and pay". At S6 you choose the card and the first product together.
5. **Moore, "big enough to matter, small enough to lead":**
   - C-09 matters most but is hardest to lead.
   - C-20 is easiest to lead (110 customers) but has the lowest ceiling.
   - C-19 is barely big enough.
   - C-11 has no leader to beat but needs thousands of customers.
6. **Aulet's three conditions.** All four were flagged at S2 as one market that is too big for word of mouth, so each needs a segment cut at Q6. C-20 has the strongest word of mouth (monthly broker meetings). C-19's different rules for each retailer strain "same product".
7. **S6 step 4 conflicts with an earlier decision of yours.** You deferred "which side to sell to first" (F-5) to segment selection. My suggestion: at S6, just record where the hub is (C-20: the broker; C-11: LTL 3PLs; C-09 and C-19: none found) and leave the entry side for Q6.

---

## 4. Your options

### Decision 1: when to choose

| Option | What it means | For | Against |
|---|---|---|---|
| **A. Run S5 first** | Settle D-14 to D-20, interview 21 Sep–16 Oct, then choose at S6 using the 1–10 re-score | The process as written. The savings assessments are the tests that move the most scores, and the early-stop proposal (P-24) would drop weak cards fast | About 4 weeks, 28–30 conversations and $2–4k |
| **B. Name a front-runner now and still run S5 on all four** | A working bet that sets the order of outreach and which assessment runs first; confirmed at S6 | Gives focus, and the interviews can still prove you wrong | Some risk of pitching in interviews instead of listening (R15) |
| **C. Choose now and cut S5 to the primary plus one backup** | A provisional S6 now, with S5 as confirm-or-kill (~15 conversations) | Roughly halves the interview load | Chooses on guessed ranges the desk said can't rank the cards. It's also a process change, logged in §9 |
| **D. Choose now and skip S5** | Commit on desk evidence alone | Fastest | Breaks S6's own entry condition and the "problem first" rule. Not one priced incident has been confirmed on any card |

**My suggestion: A,** or B if you want a working bet.

### Decision 2: the primary (now under B or C, or at S6 under A)

| Primary | Backups | Growth options | First-product bet | What you're betting on |
|---|---|---|---|---|
| **C-09** | C-11, C-19 | Claims (C-10), parcel audit (C-12), paying carriers, payee checks | Audit-only look-back, paid from recoveries *(2026-10-08, D-23: software the customer's staff use; fee form open)* | That the biggest prize is worth the hardest build and a race with funded AI rivals |
| **C-11** | C-09, C-19 | C-09, C-10, C-12 | Collect evidence at pickup and file fast | That corrections run well above FedEx's ~0.8%, that NMFTA's licence is a cost and not a gate, and that thousands of small shippers are cheap to reach |
| **C-19** | C-09, C-11 | More retailers, preventing fines, C-09 | Disputes only, long-window deductions first | That clean and durable beats small, and that you can reach small suppliers before SPS and Glimpse while retailers turn against bulk disputes |
| **C-20** | None on the shortlist; would come from the reserve list (C-24 export documents) | Refund look-back, forwarders, importers who file for themselves | A classification and data-entry helper that doesn't file | That an organised, cheap-to-reach market around a hub is worth a per-entry price and a lower ceiling |

**If you want a working bet (option B), my suggestion is C-09 with an audit-only first product.**
- **Why:** it keeps the biggest prize, the strongest fee case and the most open field, with C-11 and C-19 as backups on the same product core.
- **The risks:** whether shippers really overpay, and whether a controller will share invoices with a startup. One assessment tests both.
- **Runner-up:** C-20 as a helper tool, but only if you're willing to read the fee rule as "the saving caps a per-entry price".

The other S6 steps follow from Decision 2: park the other 13 fact-sheet cards and the 14 reserve cards, each with a trigger to revive it, then sign off with the deciding factors written down. I haven't changed any files. Once you decide, I'll record it in `6_decision.md` in your usual format: your decision word for word, the evidence for and against, and the final decision made together. If you pick A, D-14 to D-20 in `5_validation.md` §10 come next.

---

## 5. The founders' decision (2026-09-17)

**Initial decision (verbatim):**

> "We are going to go with option B, the front-runner is going to be: C-09.
>
> We need to conduct interviews, gather real numbers to determine if our margins are correct and if so how much profit we can glean from each customer."

The full message, the evidence for and against each part, and the points still to settle together are in **`6_focused_target.md` §1**. Its other sections cover everything the run has learned about C-09, the per-customer money model, who to interview and how to reach them, what the interviews must find out, and the next steps.

**Status:** C-09 is the **working bet under option B**, not the final S6 choice. S5 continues, and S6 is confirmed after the S5 re-score (`6_focused_target.md` §9, step 10). **Finalized decision:** we will make this together once research is done.

### 5.1 Update, 2026-09-22 (D-22)

- **C-11 and C-20 are eliminated** (`4_kill_conditions.md` §3.7, §5.7, §7.4).
- **The focus is now C-09 (front-runner, working bet unchanged) and C-19**, whose kill lines are adopted and frozen.
- The founders' words: "1. C-11 and C-20 are dead now. I dont care for creating software that cuts paid hours. … Note that the focuses are now C-09 and C-19."
- *S4.5, 2026-09-22 (C25):* **C-19 is "not provable from the web".** It is profitable only as a business built on the upper tail of suppliers, and the leading incumbent already serves a customer base about the size of that tail (`4_5_profitability.md` §3.6). C-09 has not been run through S4.5.
- *2026-09-22, later (C26, C27):* C-19's look-back runs on a supplier screened at 1% or more of sales in non-trade deductions, and its pass line is now 0.22% at a $50M supplier. The incumbents SupplyPike (SPS) and Glimpse, and where they may be vulnerable, are mapped in `4_5_profitability.md` §3.7.

### 5.2 Update, 2026-10-08 (D-23)

- **C-09 is a software company, not an audit firm.** The software flags the bills, and the customer's own staff review them and file the disputes. We employ no analysts. Founders' words: "We have no analysts, this is a software company. … THis is not an auditing firm but a software company." The full record is in `software-initial-pitch.md` §1A.
- **C-09's kill test is re-run on the software basis** (`handoff_c09_software_rerun.md`). ~~Its frozen lines stay in force until the founders adopt new ones.~~ *Re-run 2026-10-08; its lines adopted 2026-10-09 (C29, `4_kill_conditions.md` §2.5.12).*
- **The rule is company-wide.** C-19's model also costs our own staff's triage and dispute minutes, so it is **flagged for the same re-run later**, before the two cards are compared at S6.
