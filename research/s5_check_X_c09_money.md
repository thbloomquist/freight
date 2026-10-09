# S5 check X: the money for C-09 (auditing truckload and LTL freight bills)

- **What this is:** new desk research for S5 in run 01. It tests the money chain behind C-09, the front-runner named on 2026-09-17 as a working bet:

  > **freight spend per customer × overcharge rate × share caught × share carriers actually credit × fee share − cost to serve = gross profit per customer**

  It then splits that profit into a one-off backlog and a recurring part, and sets it against the cost of winning a customer. It answers X1-X8 from the brief.
- **Scope:** US mid-sized manufacturers and wholesalers with 20-499 staff (95,579 firms, N-E17); truckload (TL) and less-than-truckload (LTL) bills only; the likely first product, an audit-only look-back paid from recoveries. LTL tariff rules and dispute windows are **not** redone; they are in `s5_check_T_ltl_carrier_position.md`.
- **Date:** 2026-09-17. All new sources were accessed on 2026-09-17.
- **Status:** input to S5. **It decides nothing.** Readings and model assumptions are labelled **[our call]**. The coordinator and the founders decide.
- **Labels:**
  - *verified*: read at the source (an official report, statute, filing, data file, or a vendor's own pricing page for "the stated price").
  - *assumed*: a search snippet, a vendor claim, a secondary summary, a blog, or memory. **Every vendor rate claim is *assumed*, even when the page was read in full.** Anecdotes are never turned into rates.
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
- **New sources** are N-X01 to N-X50 (§13). Earlier IDs keep their meaning (N-A25, N-A26, N-A32, N-D30, N-D31, N-E17, N-K22, N-R06, N-R14, N-R21, N-R22).

**Words used here:**
- **Pre-payment audit:** checking a carrier's bill against the rate agreement and shipment facts *before* paying it. An error is fixed by short-paying or holding the bill.
- **Post-payment audit (look-back):** checking bills already paid, then filing claims to get money back. **Recoveries** are the money that actually comes back.
- **Contingency fee:** the auditor is paid a share of what is recovered, and nothing if nothing comes back.
- **Recovery audit:** the same idea applied to all accounts-payable (AP) spend, not just freight. PRGX is the best-known firm.
- **Accessorial:** an extra-service charge on a freight bill (liftgate, residential delivery, detention, and so on).
- **Reweigh / reclass:** an LTL carrier re-measures a shipment after pickup and bills a higher weight or freight class.
- **Offset:** withholding money owed on a later bill to repay an overcharge. **Tolling agreement:** a written deal that pauses a legal time limit.
- **Cost of revenue (COR):** the direct cost of delivering the service (mostly auditor labour). **Gross margin** = (revenue − COR) ÷ revenue.
- **Float:** interest a payment processor earns on client money it holds between collecting and paying it out.
- **Exception rate:** the share of invoices that cannot be processed without a human stepping in. **Straight-through:** processed with no human touch.
- **SUSB:** Census Statistics of US Businesses. **CFS:** Commodity Flow Survey.
- **Gross profit per customer** here means fee revenue minus the direct cost to serve that customer. It excludes sales, marketing and overhead.

---

## 1. Summary

| Q | Headline | Best evidence | Label |
|---|---|---|---|
| **X1** Overcharge rate | **No neutral source measures overcharges as a share of private TL/LTL spend.** The neutral numbers that exist sit **well below vendors' 2-8%**. The federal post-payment audit, which runs *after* agencies' own pre-payment audits, issued overcharges of about **0.07%** of all federal transportation bills (2007-09, includes passenger travel). A GAO-reported recovery-audit rate on general purchases was **0.48%** for a new client, falling to about **0.1%** once fixes are in. Vendor freight claims: 2-8% of spend, and 5-10% of invoices "carry some kind of error". Several widely repeated statistics ("15% per the Journal of Business Logistics", "10% per NASSTRAC") have no traceable original | N-X01, N-X04, N-X23, N-X39 | neutral *verified*; rates in vendor copy *assumed*; 0.07% **[our calc]** |
| **X1** Caught | A professional first audit caught **72-78%** of the motor-freight and household-goods overcharge dollars that two audits in a row found (GSA, 1989-91) | N-X02 | *verified*; **[our calc]** |
| **X2** AP benchmarks | Recovery audits of general AP spend recover about **0.1%** of spend in the private sector and **0.03-0.05%** in the public sector (Texas LBB, 2005). Texas's own audit recovered **0.002%** of $57.6B. AP exception rate **14%** of invoices (Ardent, 2024 data); cost **$9.40** per invoice | N-X05, N-X16 | *verified* |
| **X3** Credited | Government post-audit overcharges were **81% collected by value** (GSA, 2007-09), but the rate by contractor ran **45-96%** by count. Collection falls with delay: under 10% lost if issued within 400 days, **about 35% lost after 800 days**. GSA has offset power and a 3-year window that a private shipper does not have. A 14101(b) contract can waive the 180-day rule entirely, in either direction | N-X01, N-X06, N-X07, N-X10 | *verified*; 81% **[our calc]** |
| **X4** Pricing | Freight contingency is **25-50%** (known); **50/50 is common for small shippers and parcel refunds**. Large buyers negotiate far lower: GSA paid **3.9%** plus about **$0.28 per bill** on first audits, and 26% on second audits (1989-91); Texas **13.5%**; DoD's recovery auditor **20%**; Medicare auditors **9.0-12.5%**. SMB shipping software with some audit features costs **$0-200 a month** (MyCarrier, Freightview). Cass earns about **$2.38 in fees per item** processed, or **$3.67** including float | N-X02, N-X05, N-X04, N-X19, N-X28, N-X32, N-X29, N-X30, N-X14 | *verified* (stated prices and filings); per-item **[our calc]** |
| **X5** Cost to serve | PRGX, the only public recovery-audit comparable, ran a **cost of revenue of 60-65%** of revenue (gross margin **35-39%**) and about **$107k revenue per employee** (2018). In 1987-88, GSA's audit programme cost, including carrier refunds, was **32-35%** of collections. **No time-per-invoice figure for freight audit was found** | N-X12, N-X13, N-X03 | *verified*; ratios **[our calc]** |
| **X6** Spend per shipper | SUSB 2022: receipts average **$12.3M** (manufacturers, 20-99 staff), **$72.0M** (manufacturers, 100-499), **$43.0M** (wholesalers, 20-99) and **$197.3M** (wholesalers, 100-499). Transportation costs a mean **3.68%** of sales (Establish Davis, 2016-20; 2.38-4.76% by industry). With a TL+LTL share of transportation cost set at 60% (manufacturers) and 40% (wholesalers), the average firm spends **$0.77M** on TL+LTL a year (range $0.34-1.32M). That is **the low end of the desk's $0.71-1.41M**, and most firms sit far below the mean | N-E17, N-X21, CFS via scan E | data *verified*; shares **[our call]**; spend **[our calc]** |
| **X7** Recurrence | Recovery rates fall after the first audit: PRG's 0.48% → about 0.1% once fixes are in (−79%); PRGX says "clients tend to resolve recurring transaction processing deficiencies", and that commercial (non-retail) audits run "every two to three years". **No freight-specific decay or audit-client churn figure was found.** The first-year backlog is capped by claim windows: 180 days to contest an LTL bill, 18 months to sue | N-X04, N-X13, N-X12, check T | *verified* (the rates are PRG's own) |
| **X8** Cost to win | Almost nothing public. PRGX: annuity-like audit services need "a relatively long sales cycle and a relatively high level of direct person-to-person contact". No CAC, and no referral commission rate for any freight or parcel audit firm, was found | N-X13, N-X34 | *verified* / not found |

**The model in one line (§10, [our calc] on [our call] inputs):** at central rates (1.5% overcharged × 70% caught × 80% credited = **0.84% of TL+LTL spend recovered**) and a 25% fee, a shipper **needs about $2.4M of TL+LTL spend a year** for the fee to reach $5k, and about **$0.68M** just to cover a lean automated cost to serve. At low rates (0.5% × 50% × 60% = 0.15% recovered), **no spend level covers the cost to serve**, and $5k needs $13M of spend. At high rates (3% × 85% × 90% = 2.3%), $5k needs $0.87M.

---

## 2. X1 · Overcharge and error rates on TL and LTL bills (H09-02)

### 2.1 Neutral sources: government audit programmes

| Source | What it measured | Numbers | Label |
|---|---|---|---|
| **GSA Office of Inspector General, audit of the postpayment audit process** (report A120169/Q/9/P14002, 2014-03-31; N-X01) | GSA's Transportation Audits Division audits federal transportation bills **after payment**, through contractors paid "based on a negotiated percentage" of what is collected. By law, agencies must already audit these bills before paying (31 U.S.C. 3726(a), N-X06) | The division covers "the estimated $16.3 billion in annual transportation bills paid by federal agencies", across air cargo, air passenger, household goods, motor freight, rail and ship. "For bills paid during 2007 to 2009 the Division issued overcharges of $33.1 million, of which, $6.3 million were written off as uncollectible." That is about $11M of overcharges a year, **0.068% of the annual bill total** **[our calc]**. Motor freight is not broken out | *verified*; ratio **[our calc]** |
| Same report | The two-tier design | "second tier contractors are finding additional overcharges missed by the first" | *verified* |
| **GAO/NSIAD-92-157, "GSA Transportation Audits: Contract Costs Can Be Reduced"** (1992-06-03; N-X02) | First versus second post-payment audit of the same bills | "from October 1989 through December 1991, GSA collected $10.2 million in overcharges related to motor carrier payments. About 22 percent of this amount was not identified until the second audit." For domestic household goods, "Twenty-eight percent of the overcharge amounts were not identified until the second audit." So one professional audit caught **78%** (motor) and **72%** (household goods) of what two audits found **[our calc]**, which is an upper bound on its true catch rate | *verified* (OCR text); **[our calc]** |
| **GAO/AFMD-89-47, "Transportation Audits: GSA's Accounting for Transportation Overcharges"** (1989-08-30; N-X03) | Collections | "From October 1986 through August 1988, GSA collected $100.8 million in transportation overcharges". The spend audited is not stated, so no rate can be computed | *verified* |
| **DOJ civil case against YRC Freight, Roadway and Yellow** (FreightWaves, 2019 and 2022-03-10; N-X11) | An LTL carrier's reweigh practice on DoD freight, 2005-2013 | Allegation: after reweighs the carriers billed "higher weights when ... they knew that the actual weights were lower" (DOJ, via search summary, *assumed*). The settlement was $6.85M. "An amount for the overcharges was never quantified publicly" (FreightWaves, *verified*). **An allegation and a settlement, not a rate** | mixed |
| **Texas Comptroller, recovery audit of state agency payables** (December 2010; N-X05) | All vendor payments, including freight | "Transactions totaling $57.6 billion have been analyzed, with $1.08 million recovered". "Freight overpaid" is one of eight recovery categories. The four smallest categories, freight among them, were each 0.4-1.0% of the $1.08M | *verified* |

**Not found:** DoD freight-payment audit results (the DoD Inspector General's PowerTrack reports returned 403), USTRANSCOM or DFAS rates, state transportation audit figures, and Canadian or UK public audits (§14).

### 2.2 Recovery-audit and SEC-filing figures

| Source | Figure | Label |
|---|---|---|
| **GAO testimony T-NSIAD-99-213** (1999; N-X04), on PRG's recovery audit of Defense Supply Center Philadelphia purchases | PRG "identified $29.3 million in overpayments made to suppliers on purchases of roughly $6 billion". "According to PRGI, its overpayment identification rate under the demonstration program is 0.48 percent of purchases reviewed, which is consistent with its experience with new private sector clients before corrective measures are implemented. PRGI told us that, as corrective measures are implemented, the overpayment rate typically drops to about 0.1 percent of purchases reviewed." | The GAO text is *verified*; **the rates are PRG's own claim**, so *assumed* as rates |
| **PRGX 10-K, FY2018** (N-X12) | "Although these entities correctly process the vast majority of payment transactions, errors occur in a small percentage of transactions." PRGX lists as competitors "Firms with specialized skills focused on recovery audit services for discrete sectors such as sales and use tax, telecom, freight or real estate." | *verified* |
| **EDGAR full-text search**, 10-K filings 2015-2026 containing both "freight audit" and "overcharges" | **0 hits.** No shipper's 10-K discloses a freight-audit recovery rate this way | *verified* (query run) |
| Cass FY2025 10-K (N-D30, re-read for Item 1) | No overcharge or recovery rate is disclosed | *verified* |

### 2.3 Vendor and blog figures (all *assumed*)

| Claim | Where | Note |
|---|---|---|
| "recoverable errors often range from 2% to 8% of freight spend" | N-A32 (known) | Consultant/blog |
| LTL 3-8% and TL 1-3% of spend recovered | N-A26 (known) | Consultant |
| "5 to 10 percent of freight and parcel invoices carry some kind of error"; a post-audit "can trim 3%-10%" | Tompkins Ventures, 2026-07-07 (N-X24) | A share of *invoices*, not of dollars |
| Recoveries "commonly land at 2-8 percent of audited freight spend" (no attribution). Figures like "up to 20 percent", "10 percent per NASSTRAC" and "15 percent per Journal of Business Logistics" are called "orphan attributions that vendor blogs quote from each other" | GingerControl, 2026 (N-X23) | A blog that audits other blogs' sources. Its own 2-8% is unattributed |
| "up to 15% of freight bills contain errors" (credited to the Journal of Business Logistics); "between 1% to 5% of all freight invoices contain errors" (credited to Supply Chain Dive) | Hatfield & Associates (N-X39) | Exactly the orphan pattern N-X23 describes |
| LTL: "8–12% of total LTL spend" (credited to an AFS report); Eller's own median "2–5% of annual LTL spend" | Eller Audit (N-X26) | Vendor |
| Automated programmes reduce visible errors to "below 1–2%" of invoices; "3–5% of annual freight spend" lost | Nuvocargo, 2026 (N-X25) | Vendor; no source |
| 3.8% of carrier invoices carry a billing variance, averaging $127 | Laneproof, 2026-03-23 (N-X27) | Broker side, not shipper side; vendor's pooled data |
| An article on LTL billing errors cites no rate at all | Foreign Policy Journal, 2026-08-26 (N-X40) | Confirms the gap |

### 2.4 By error type

**No neutral breakdown by error type exists for freight.** The closest neutral figure is general AP (Texas, N-X05): of $1.08M recovered, hotel tax 39.1%, duplicate payments 34.2%, statement review 12.9%, overpayments 10.5%, and four small categories including freight 0.4-1.0% each.

Vendor breakdowns (all *assumed*):

| Error type | Nuvocargo (N-X25), no source | Eller Audit (N-X26), LTL only |
|---|---|---|
| Duplicates | 2-4% of invoices, full invoice amount | — |
| Rate differs from contract | 10-15% of invoices, 3-15% of invoice total | Minimum charge applied when a waiver should apply: about 8% of shipments |
| Fuel surcharge | 12-18% of invoices, 2-8% of invoice total | Cap overage of 2-3 points on about 22% of shipments |
| Accessorials | Billed without a qualifying event: 5-10% of invoices, $75-500 each. Detention: 8-15% of invoices, $150-350 | 9-15% of annual accessorial billing disputable |
| Reweigh / reclass | 15-25% of LTL invoices, 5-30% of the invoice | Class errors: 4-6% of shipments, averaging $145 |
| Math | — | — |

**A carrier-side anchor already on file:** FedEx Freight's own filing puts dimensioner re-rating at about 0.8% of revenue (check T, *verified* there). Those are upward corrections the carrier made, not overcharges. They bound how much reweigh/reclass money is in play on LTL bills; they do not measure errors.

### 2.5 Pre-payment catch versus post-payment recovery

- **No source measures a pre-payment audit's catch rate** against a known total of errors.
- **What the evidence separates:**
  - After agencies' own pre-payment audits, the federal post-payment audit still issued overcharges of about 0.07% of all transportation bills (§2.1). The report does not split this by mode, so the motor-freight share is unknown. **That is the residual that a pre-payment audit leaves behind, not the gross error rate.**
  - One professional post-payment audit found 72-78% of the dollars that two audits found (N-X02).
  - PRGX: clients audit "closer to the time of the transaction to increase recovery yields" (N-X12, *verified*). Earlier is better for collection (§4).
  - A pre-payment audit turns a recovery into a bill never paid. That leaves no "recovery" to take a contingency share of, so the fee basis has to change (§5) **[our call]**.

### 2.6 Reading [our call]

- Every neutral figure found is **below 0.5% of spend**, but none measures **private TL/LTL bills at mid-sized shippers with no audit at all**, which is where C-09 plays. Two things pull the true rate up: federal bills had already been pre-audited, and general AP spend includes clean categories. Nothing public settles the rate between about 0.3% and 3%.
- **Vendor rates of 2-8% are best read as "what a contingency firm recovers from the worst-controlled accounts it chooses to take", not as a market average.** No source ties them to a sample.
- **H09-02 (1-3%) is not settled.** The evidence leans toward the low half of the range and makes the fail line ("measured under 0.5%") a live outcome, not a remote one.

---

## 3. X2 · General AP error and duplicate-payment benchmarks

| Benchmark | Figure | Source | Label |
|---|---|---|---|
| Private-sector recovery audit | "about 0.1 percent of a business' expenditures" | Texas Legislative Budget Board, Jan 2005, as quoted by the Comptroller (N-X05) | *verified* (as quoted) |
| Public-sector recovery audit | "between 0.03 and 0.05 percent" | Same | *verified* |
| Texas actual, 2006-10 | $1.08M recovered on $57.6B analysed = **0.0019%** **[our calc]**. The AP review "generated far less in recoveries than anticipated", and agencies were "doing an excellent job in managing their payables" | N-X05 | *verified* |
| New recovery-audit client versus mature | 0.48% of purchases, dropping to about 0.1% | PRG via GAO (N-X04) | *verified* that GAO reports it; rate *assumed* |
| Duplicate or erroneous payments | 0.8% (best), 1.5% (median), 2% (bottom) of the **number** of disbursements | APQC Open Standards Benchmarking, via a snippet. The APQC page returned 403 (N-X18) | *assumed* |
| Invoice exception rate | "dropped dramatically to 14% in 2024"; best-in-class 9.0% vs all others 22.0% | Ardent Partners, *AP Metrics that Matter in 2025*: 212 respondents, March-May 2024; 53% with revenue over $1B, 16% under $250M (N-X16) | *verified* (survey) |
| Exception rate, later wave | 18.4% | Ardent, Payables Place, January 2026 (N-X17) | *verified* (blog) |
| Cost to process one invoice | $9.40 average (N-X16); $9.84 (N-X17); APQC 2018 median $5.83, top quartile ≤ $2.07 (N-R14) | as listed | *verified* |
| Days to process | 9.2 average; best-in-class 3.1 vs all others 17.4 | N-X16 | *verified* |
| Straight-through share | 32.6% of invoices | N-X16 | *verified* |
| Medicare recovery auditors (a different domain, but a neutral contingency programme) | $1.03B of improper payments identified and $693.6M returned in the 3-year demonstration (**67%** **[our calc]**); fees "range from 9.0% to 12.5%" | CRS R40592, 2009-05-21 (N-X19) | *verified* |
| North Carolina statewide overpayment audit | PRGX holds the FY2024-2028 contract; "The third party shall be compensated only from funds recovered". The statute's categories include "miscalculated freight charges". No amounts are published on the page | NC Office of the State Controller (N-X20) | *verified* |

**Reading [our call]:** general AP recovery audits find about 0.1-0.5% of spend. Freight bills are error-prone on their own (carrier-built invoices, reweighs, accessorials), so a freight rate above the AP floor is plausible. **A freight rate 20-80 times the AP floor (the vendors' 2-8%) has no neutral support.**

---

## 4. X3 · Recovery conversion: what carriers actually credit

### 4.1 Evidence

| Source | Figure | Label |
|---|---|---|
| GSA OIG (N-X01): share of issued overcharges collected, by contractor, bills paid 2007-09 (**by count**) | Mid-South 96 / 92 / 96%; Commercial Traffic **45** / 63 / 66%; Parsifal 96 / 89 / 94% | *verified* |
| Same, by value | $33.1M issued, $6.3M written off → **81% collected** | **[our calc]** |
| Same: **delay destroys collection** | Contractors issued overcharges an average 260 days after payment (first tier) and 737 days (second tier). "Less than 10 percent of the overcharges were uncollected if the lag time was less than 400 days." At 600-799 days, "over 25 percent"; at 800 days or more, "nearly 35 percent" | *verified* |
| Same: process | "the provider has 60 days to dispute or protest"; the contractor then has 30 days to "allow the protest, which cancels the overcharge" or deny it | *verified* |
| Same: time limit | A 2010 board decision "reduced the statute of limitations for overcharge collection from 10 to 3 years"; $770,059 not covered by tolling agreements "were written off" | *verified* |
| **Why government collects well** | 31 U.S.C. 3726(d): "Not later than 3 years (excluding time of war) after the time a bill is paid, the Government may deduct from an amount subsequently due" (N-X06). GSA "offsets a payment" and notifies the carrier (41 CFR 102-118.615, 2024 rule, N-X08). **A private shipper can offset only against a carrier it still uses** **[our call]** | *verified* |
| GAO 1999 (N-X04) | Of $29.3M identified at DoD, "Collections by DOD as of June 1999 amounted to $2.6 million" (8.9% **[our calc]**), with vendors contesting | *verified* |
| Medicare (N-X19) | 67% returned; 22.5% of determinations appealed; 7.6% overturned in the provider's favour | *verified* |
| PRGX 10-K FY2018 (N-X12) | Risks include "the significant control that our clients have over assertion or acceptance of recovery audit claims against their suppliers" and "our dependency on clients to approve our claims on a timely basis". Clients accelerate audits "to increase recovery yields ... and reduce supplier abrasion" | *verified* |
| Laneproof (N-X27), brokers disputing carrier bills | "65% to 80%" of disputed dollars recovered is "healthy". Disputes filed within 5 business days recover 74%; after 15 or more days, 41%. Resolution target "under 14 days" | *assumed* (vendor, broker side) |
| Eller Audit (N-X26), LTL | Recovered share by category: class 70-82%, fuel cap 85-92%, accessorials 60-75%, minimum charge 75-88%. A "60–90 day claims window" is typical | *assumed* (vendor) |

### 4.2 Contract carriage waivers (49 U.S.C. 14101(b))

- **The statute:** a carrier "may enter into a contract with a shipper ... to provide specified services under specified rates and conditions". The parties may waive rights and remedies in writing but "may not waive the provisions governing registration, insurance, or safety fitness". "The exclusive remedy for any alleged breach of a contract ... shall be an action in an appropriate State court or United States district court, unless the parties otherwise agree" (N-X07, *verified*; the middle clause is paraphrased by the fetch tool).
- **What waiving does to audits:** a transportation-law webinar lists among the rights commonly waived "Statutory time limits for identifying overcharges and undercharges-180 day rule, 49 USC 13710" and "Overcharge, undercharge and duplicate payment regulations waived-49 CFR 378". It warns that "Waiver vitiates important time limit (e.g. $6 million dispute – post audit traps)" (N-X10, 2008, *verified*).
- **Reading [our call]:** a waiver does not by itself remove a shipper's audit rights. It replaces the federal 180-day window and the Part 378 claim procedure with **whatever the contract says, plus state contract law**. That can make the window longer (a years-long state limitation period) or shorter (a contract clause such as "claims within 90 days"), and it exposes the shipper to carriers' own back-billing. Truckload contracts and broker rate confirmations must be read one by one in the savings assessment. **No count of how often shipper contracts waive 13710 was found.**

### 4.3 Carriers' refusal practices

- **Found:** only the GSA protest mechanics (§4.1), the YRC reweigh allegation (§2.1), and vendor statements that LTL carriers answer within 30-90 days (*assumed*).
- **Not found:** any count of how often carriers refuse, or how they refuse (denying, going silent, or re-billing). LTL tariff rules on claims are in check T.

### 4.4 Reading [our call]

- For the model, the share credited is set at **60% (low), 80% (central) and 90% (high)**.
  - The central 80% sits just under GSA's 81%, which had offset power and a 3-year window.
  - The low 60% sits between GSA's weakest contractor (45-66%) and Medicare's 67%.
- **Speed matters more than any fee term.** Every source, neutral or vendor, shows collection falling as claims age, so a look-back of old bills collects less per dollar found than a monthly audit.

---

## 5. X4 · Pricing (H09-06)

### 5.1 Contingency shares

| Buyer / context | Share | Source | Label |
|---|---|---|---|
| Freight audit, general | 25-50% of recoveries | N-A25, N-A26 (known) | *assumed* |
| Freight post-audit firms | "Most post audit firms work on a contingency basis at 50% of overcharge claims filed and paid" | Search summary of Goodman-Reichwald-Dodge and similar pages. The firm's own page says "only a % of the money we collect for you" with no number (N-X38) | *assumed* |
| **Small and mid-sized shippers** | Contingency is "Less common, but favored by some small-to-medium sized businesses", splitting savings "at a pre-negotiated percentage (e.g., a 50/50 split)". "The most common pricing model among the major players in this industry is per-transaction." A contingency supplier "will likely have fewer analytical tools and customization" | Software Solutions Inc. white paper (N-X28) | *verified* that the vendor says it; *assumed* as market fact |
| Parcel refunds | "splits this amount with you, 50-50. This is our contingency fee for service" | Parcel Refund Services (N-X32) | *verified* (stated price) |
| Parcel refunds | "you pay a percentage of refunds recovered after credits are issued"; "Rate negotiable for high-volume accounts" | RefundPros (N-X33) | *verified* (stated terms, no %) |
| **Federal government, first post-payment audit, motor freight, 1989-91** | **3.9%** commission, plus a transaction fee per bill; "fees represented more than 75 percent of the payments GSA made to first auditors" | GAO 1992 (N-X02) | *verified* |
| Same, second audit | **26%** commission only | N-X02 | *verified* |
| Federal ceiling | "Payment to any contractor for audit services shall not exceed 50 percent of the overpayment identified by contract audit" (31 U.S.C. 3726(e)) | N-X06 | *verified* |
| DoD recovery audit, 1999 | "PRGI receives a fee of 20 percent of net collected funds" | N-X04 | *verified* |
| Texas state AP recovery audit | 13.5%, against an "industry average of 20 to 40 percent" (LBB, 2005). University contracts with PRG-Schultz: "50% of recovered amount" (1998-2005) | N-X05 | *verified* |
| Medicare recovery auditors | 9.0-12.5% | N-X19 | *verified* |
| PRGX's small competitors | "numerous smaller ... firms ... at low contingency rates"; risk of "commoditization of our services and the effects of rate reductions" | N-X12 | *verified* |

**Pattern [our call]:** the share falls as the buyer's size and bargaining power rise. It runs from 50% for small shippers and parcel refunds, through 20-40% for mid-to-large AP audits, down to 4-13% for governments with huge volumes. **A 25% share for mid-sized shippers sits below the small-shipper norm, not above it.**

**Look-back versus ongoing:** no source prices them differently. GSA's first versus second audit (3.9% vs 26%) is the only priced split, and there the harder, later work carried the higher share.

### 5.2 Per-invoice and per-item fees

| What | Figure | Source | Label |
|---|---|---|---|
| GSA post-payment transaction fee for data capture, fixed in 1989 contracts | Motor freight **$0.28** per bill; rail, water and pipeline $0.29; air $0.39 (1989 dollars) | GAO 1992 table (N-X02; OCR, some cells garbled) | *verified* |
| **Cass, FY2024** | Processing fees $82.671M and financial fees $43.297M across 35.729M transportation invoices plus 17.135M facility (utility and telecom) items = **$2.38 in fees per item**, of which processing is $1.56. Including net interest income of $67.787M (float), total revenue is **$3.67 per item**. Fees are **0.22%** of the $57.6B processed; total revenue **0.34%** | Cass Q4 2024 release (N-X14) | inputs *verified*; per-item **[our calc]** (transport and facility are not split) |
| Cass average transportation invoice | **$1,011** (2024); $1,055 (2025, from N-D30's 34.5M invoices and $36.4B) | N-X14, N-D30 | **[our calc]** |
| Payment-network fee charged to carriers | "For a sliding fee of 1-2 percent, depending on contract award, carriers are paid within several days" (U.S. Bank PowerTrack, DoD, 2002) | N-X37 | *verified* (article) |
| Vendors on per-invoice prices | "Vendors rarely publish numbers"; LTL invoices "typically price above clean truckload invoices" | Navix (N-X35) | *assumed* |

### 5.3 Subscriptions (SMB shipping software that includes some audit)

| Product | Stated price | Audit in plan? | Label |
|---|---|---|---|
| **MyCarrier** (LTL platform for small and mid-sized manufacturers and distributors) | Basic $0; Starter $60/month; Professional $200/month; Professional Plus custom. Add-ons at $10-30/month. "API/ERP Integrations & Invoice Hub: Contact for pricing" | Audit and payment are marketed ("Fast LTL Freight Audit and Payments") but not listed in the tier features read | *verified* (N-X30) |
| **Freightview** | "$149 / mo" for 0-50 shipments a month; "Call now" above that | Auditing is "not mentioned" on the pricing page; the product blog describes invoice auditing with overage limits (e.g. 3%) | price *verified* (N-X29); feature *assumed* |
| **FreightPOP** | All four tiers "Call for Quote"; Starter covers 350 freight shipments/month | "Carrier Invoice Audit" is a feature row, tier unclear. Third-party estimates of about $99/month for one user and $500-1,500/month for ten users | *verified* (N-X31); estimates *assumed* (N-X42) |
| **Loop** | "No published pricing"; aimed at "mid-market and enterprise shippers" | — | *assumed* (N-X36) |
| Freightgate | Not found | — | — |

### 5.4 Minimums

- **Not found as a stated minimum** at any audit firm.
- The only hints (all *assumed*): "over 500 invoices per month, a third-party audit provider typically recovers more than their fee" (search summary, N-X44); in-house audit "recommended below ~$500K annual freight spend", software payback "6-9 months above ~$2M in spend" (N-X23); first audit free (N-X26).

---

## 6. X5 · Cost to serve and margins of audit businesses

### 6.1 Public comparables

| Company / programme | Figure | Source | Label |
|---|---|---|---|
| **PRGX FY2018** | Revenue $171.8M; cost of revenue $104.8M = **61.0%** (gross margin **39.0%**). "COR as a percentage of revenue for Recovery Audit Services - Americas was 60.3% in 2018, 61.0% in 2017". About 1,600 employees → **$107k revenue per employee**. Operating income $7.4M (4.3%) | N-X12 | inputs *verified*; ratios **[our calc]** |
| **PRGX FY2009** | Gross margin $62.9M on revenue $179.6M = **35%**. "our recovery audit services business is subject to intense price pressure. Such price pressure could cause our profit margins to decline" | N-X13 (fetch-tool extraction) | *verified* |
| PRGX client base | "principally to large businesses"; commercial clients "typically Fortune 1000 companies ... with multi-billion dollars of purchase transactions to be audited" | N-X12 | *verified* |
| **GSA programme, FY1987-88** | Disbursements for "carrier refunds and contract audit services and administration" were $16.6M of $47.2M collected (FY87) and $17.4M of $53.6M (FY88, 11 months) = **32-35% of collections**. That is an upper bound on audit cost, because it includes refunds to carriers | N-X03 | *verified*; ratio **[our calc]** |
| GSA contractor staffing, 2008-10 | "12 of the 23 postpayment auditors with access to TARPS did not undergo background investigations". Required experience: "7 years general transportation experience and 4 years of specialized experience". Audits due "within 30 days from the contractor's receipt of invoice". GSA's page says the division reviews "over 12 million transportation invoices per year" (snippet) | N-X01; N-X09 | *verified*; the 12M is *assumed*. **An invoices-per-auditor ratio is not computed**: 23 is the count with system access, not total audit staff |
| **Cass** | 860 full-time and 156 part-time employees (2026-02-27), 68 of them at the bank. Total revenue $199.2M (FY2024) → about **$196k per head** | N-D30 (re-read); N-X14 | **[our calc]**; mixes years, and includes the bank and utility-bill processing |
| Trax, nVision | Aggregator figures conflict (Trax "$16.5M ARR" in 2021 vs "$157.9 million" with 529 employees elsewhere). nVision: "400+ full time employees outside of the United States" | N-X45 | *assumed*, unusable |

### 6.2 Time per invoice

- **Freight audit: not found.**
- **General AP (proxy):** $9.40 per invoice on average, $2.07 or less in APQC's top quartile; 32.6% straight-through; best-in-class teams process an invoice in 3.1 days versus 17.4 (§3).

### 6.3 Does success rate set margin under contingency pricing?

- **Directly: no study found.**
- **Indirect signs:**
  - GSA's switch to paying transaction fees on top of commissions was meant to make auditors "examine all documents carefully". GAO found no evidence it did, and 22-28% of overcharge dollars still surfaced only at the commission-only second audit (N-X02, *verified*).
  - PRGX's margin swings with rate pressure and with clients' willingness to assert claims (N-X12, N-X13).
- **Reading [our call]:** under a contingency fee the auditor carries the cost of every invoice checked and every dispute filed, while revenue depends on the rate found and the share credited. Margin is therefore roughly (rate × caught × credited × fee share) minus a cost per invoice and per dispute. §10 shows it turning negative at low rates.

### 6.4 Cost-to-serve assumptions used in §10 [our call]

| Item | Assumption | Anchor |
|---|---|---|
| Invoices per customer | TL+LTL spend ÷ $1,000 | Cass average transportation invoice $1,011 (**[our calc]**). LTL-heavy shippers will have more, smaller invoices |
| Processing (reading, rating, matching, storage) | $0.50 per invoice | Between GSA's 1989 data-capture fee ($0.28) and Cass's processing fees per item ($1.56, which include payment) |
| Dispute handling | $12 per disputed invoice (about 18 minutes at $40/hour loaded, including carrier follow-up) | No source. Rate reading only |
| Disputed share of invoices | Low 3%, central 6%, high 10% | Laneproof's 3.8% of invoices with a variance, and Tompkins's 5-10% with an error (both *assumed*) |
| Fixed per customer per year | $600 (rate-agreement upkeep, carrier contacts, reporting, support) | No source |
| One-off onboarding | $1,000 (data pull, loading rate agreements) | No source |
| **Human-heavy alternative** | Cost to serve = **60% of fee revenue** | PRGX's cost of revenue (N-X12, *verified*) |

---

## 7. X6 · Freight spend per mid-sized shipper

### 7.1 Receipts per firm (SUSB 2022)

The size bands (20-99 and 100-499 staff) come from N-E17, re-parsed today. They are *verified*; the per-firm figures are **[our calc]**.

| Group | Firms | Receipts | Receipts per firm |
|---|---|---|---|
| Manufacturers, 20-99 | 44,917 | $552.8B | **$12.3M** |
| Manufacturers, 100-499 | 12,392 | $892.0B | **$72.0M** |
| Wholesalers, 20-99 | 30,583 | $1,315.5B | **$43.0M** |
| Wholesalers, 100-499 | 7,687 | $1,516.7B | **$197.3M** |
| All 95,579 | 95,579 | $4,276.9B | **$44.7M** |

- **A data warning:** the finer-size file (N-X22) does not agree with these rows. Its 20-99 bands total 40,469 manufacturers with $703.5B of receipts, against 44,917 and $552.8B above. Its 100-499 bands match the firm count but not the receipts ($971.3B against $892.0B). The finer file is used below only for shape, with low confidence.
- **Within-band spread (finer file, shape only):** mean receipts run from $5.4M (manufacturers with 20-24 staff) to $173.5M (400-499). The mean is pulled up by the largest firms, so **the typical firm spends well below the averages below** **[our calc]**.

### 7.2 Transportation as a share of sales

| Source | Figure | Label |
|---|---|---|
| **Establish Davis Database, 2020** (published December 2021; N-X21): participating manufacturers, wholesalers and retailers; costs are "Inbound and outbound" | Average company, 2016-20: **transportation 3.68% of sales**, $35.78 per hundredweight; total logistics 8.39%. By industry (2000-20): electronics 2.38%, medical equipment 3.07%, pharmaceutical 3.13%, industrial equipment 3.29%, apparel 3.65%, automotive 3.75%, consumer goods 3.97%, building material 4.64%, food 4.76%. "The company size can affect the logistics costs with up to 50%"; larger companies have lower costs. Firms over $2B of revenue were not analysed separately | *verified* (the size chart is an image and was not read) |
| Consultancy guide | Wholesale/B2B distribution logistics (not only transport) "3–8%" | *assumed* (N-X43) |

### 7.3 TL / LTL / parcel split

| Source | Figure | Label |
|---|---|---|
| CSCMP State of Logistics 2025, via FreightWaves (N-K22, known) | 2024: truckload $387B, LTL $64B, private fleets $541.4B. For-hire TL+LTL is about 45% of all trucking cost **[our calc]** | *assumed* |
| CFS 2022, all shippers (scan E, *verified*) | By value: for-hire truck 44.8%, own trucks 23.0%, parcel 13.4%, customer pick-up 5.7% | *verified* |
| CFS 2022 by group (scan E) | Manufacturers mostly use for-hire trucks: machinery 79.0% of tons, plastics 69.7%, fabricated metal 62.6% (parcel 8.5% of value), furniture 59.9%. Durable-goods wholesalers: own trucks 43.1%, for-hire 29.6% of tons, parcel 23.0% of value. Nondurable wholesalers: own trucks 34.4%, for-hire 34.2% | *verified* |

**Inputs set [our call]:** TL+LTL as a share of a firm's transportation cost is 45 / **60** / 75% for manufacturers and 25 / **40** / 55% for wholesalers (low / central / high). The reasons: private fleets, customer pick-up and parcel are larger at wholesalers, and some inbound freight is paid inside supplier prices.

### 7.4 Spend bands [our calc]

Spend = receipts per firm × transportation % of sales (2.38 / 3.68 / 4.76%) × TL+LTL share.

| Group | Firms | Low | **Central** | High |
|---|---|---|---|---|
| Manufacturers 20-99 | 44,917 | $0.13M | **$0.27M** | $0.44M |
| Manufacturers 100-499 | 12,392 | $0.77M | **$1.59M** | $2.57M |
| Wholesalers 20-99 | 30,583 | $0.26M | **$0.63M** | $1.13M |
| Wholesalers 100-499 | 7,687 | $1.17M | **$2.90M** | $5.17M |
| **All 95,579, total** | | $32.3B | **$73.6B** | $125.7B |
| **Average per firm** | | $0.34M | **$0.77M** | $1.32M |

- **Cross-check against the desk:** the desk had $68-135B in total, or $0.71-1.41M per buyer (15-30% of $451B). The bottom-up central ($73.6B) lands at **the low end of the desk range**, and the bottom-up low sits below it.
- **Where the spend is:** 47% of firms are manufacturers with 20-99 staff, and their central TL+LTL spend is about $0.27M. Firms with 100-499 staff are 21% of the count and hold 57% of the central spend **[our calc]**.

---

## 8. X7 · Recurrence: backlog versus run-rate

| Evidence | Figure | Label |
|---|---|---|
| **Rates fall once fixes are in** | PRG: 0.48% of purchases for a new client, "typically drops to about 0.1 percent" after corrective measures (−79% **[our calc]**) | GAO reports it (*verified*); rate is PRG's (*assumed*) |
| Clients fix their own causes | "Over time, our clients tend to resolve recurring transaction processing deficiencies" (PRGX FY2009). "As the skills, experience and resources of our clients' internal recovery audit staffs improve, they will identify many overpayments themselves and reduce some of our audit recovery opportunities" (FY2018) | *verified* (N-X13, N-X12) |
| **Commercial audits are not annual** | Services to commercial clients "have tended to be either periodic (typically, every two to three years) or rotational in nature"; "revenues derived from a given commercial client may change markedly from year to year" | *verified* (N-X13) |
| Mature programmes recover less | N-A32 (known) | *assumed* |
| The first audit misses a lot | A second audit still found 22-28% of the overcharge dollars (N-X02). The GSA OIG says the second tier keeps finding overcharges (N-X01) | *verified* |
| Texas agencies fixed errors | "In cases where errors were made, the agencies involved implemented processes and procedures to correct them" | *verified* (N-X05) |
| Client retention | No churn figure. PRGX: top five clients were 35.4% of revenue (2018) and 29.9% (2009). "Most of our recovery audit contracts provide that the client may terminate the contract without cause ... by providing relatively short prior written notice". Clients may also move PRGX "from primary to secondary position" | *verified* (N-X12, N-X13) |
| **Freight-specific decay** | **Not found** | — |
| **Claim windows that cap the backlog** | LTL: 180 days to contest a bill (49 U.S.C. 13710(a)(3)); 18 months to sue (14705); some tariffs count from shipment, and XPO and R+L allow a corrected BOL within 30 days (check T, *verified*). Contract carriage: whatever the contract sets (§4.2). Federal: 3 years (N-X06) | *verified* |

**Reading [our call]:**
- **Why freight errors may decay less than AP duplicates:** duplicates are fixed inside the shipper's own AP system, but freight overcharges are created on the carrier's side on every shipment (reweighs, accessorials, fuel tables). A shipper can reduce them by fixing rate agreements, BOL accuracy and tendering rules, but cannot switch them off. No evidence tests this.
- **Backlog assumptions used in §10:**
  - Look-back depth is 0.5 / 1.0 / 1.5 years of bills (180 days, 12 months, 18 months).
  - Older claims collect less (N-X01's lag pattern), so the backlog equals 0.4× / 0.85× / 1.1× one year of run-rate recoveries.
  - Year-2 rates fall 40% as an illustrative central, against the −79% PRG pattern for general AP.
- **At central rates on $1M of spend** **[our calc]**:
  - the backlog is 46% of first-year recoveries ($7,140 of $15,540);
  - backlog plus year 1 is 75% of the two-year fee, if year 2 falls 40%.

---

## 9. X8 · The cost to win a customer

| Evidence | Figure | Label |
|---|---|---|
| Sales cycle | PRGX: "service offerings that are the most annuity-like in nature, such as a contract compliance audit, typically require a relatively long sales cycle and a relatively high level of direct person-to-person contact" | *verified* (N-X13) |
| Channels at the leader | Cass's Item 1 does not describe its sales channels, and gives no client count: "a varied client base", "not dependent on any one customer" | *verified* (N-D30 re-read) |
| Referral and partner programmes | LateShipment.com (parcel refunds): partners "receive considerable recurring compensation for any sales originating through them"; partner types are "Independent sales partners" and businesses "well connected with a growing network of retailers, bulk shippers or drop shippers". **No %.** 71lbs, Intelligent Audit and Parcel Refund Services show no partner terms (one page returned 404) | *verified* (N-X34, N-X50, N-X32) |
| ERP marketplaces | Freight apps with invoice audit are listed on NetSuite's marketplace (N-R21, known); no revenue-share terms were read | *assumed* |
| Government buying | Federal agencies may use "a prepayment audit contractor under GSA's multiple award schedule" (SIN 541211), and "third party payment providers generally provide the auditing service at no charge to the agency" (GSA page, via snippet) | *assumed* |
| CAC for any freight-audit firm | **Not found** | — |
| Benchmark already on file (parked) | Founder-led direct selling stays economic at about $5k or more a year per customer, with CAC payback of 12 months or less and gross retention of about 88% or better | `s0_check_A_ambition_economics.md` §A3 |

**Reading [our call]:**
- Contingency pricing removes the budget objection (N-X28: good for firms that lack "the budget to outsource"). It does not remove the time a controller needs to hand over invoices, rate agreements and PODs, or the worry about carrier relationships (PRGX: "supplier abrasion").
- The one channel with a proven revenue share on the web is parcel-refund resellers, and no rate is public. The CAC question stays with the S5 funnel (`5_log.md` §1).

---

## 10. Worked per-customer model [our calc]

### 10.1 Rate sets [our call]

| Set | Overcharged (% of TL+LTL spend) | Caught | Credited | **Recovered (% of spend)** | Disputed invoices | Backlog multiple | Anchors |
|---|---|---|---|---|---|---|---|
| **Low** | 0.5% | 50% | 60% | **0.15%** | 3% | 0.4× | H09-02's fail line; PRG's new-client rate on general purchases 0.48% (N-X04); GSA's weakest contractor collection 45-66% (N-X01) |
| **Central** | 1.5% | 70% | 80% | **0.84%** | 6% | 0.85× | Middle of the desk's 1-3%; first-audit catch 72-78% (N-X02); GSA 81% collected (N-X01) |
| **High** | 3.0% | 85% | 90% | **2.30%** | 10% | 1.1× | Top of the desk range, low end of vendors' 2-8%; vendor category credit rates 60-92% (N-X26) |

The cost to serve is the bottom-up set in §6.4: $0.50 per invoice, $12 per dispute and $600 a year fixed, plus $1,000 onboarding in the backlog line. There is one invoice per $1,000 of spend.

### 10.2 Table

Columns are TL+LTL spend a year × rate set. Money is rounded to the dollar.

| Row | $250k Low | $250k Central | $250k High | $1M Low | $1M Central | $1M High | $3M Low | $3M Central | $3M High |
|---|---|---|---|---|---|---|---|---|---|
| Overcharges on the bills | $1,250 | $3,750 | $7,500 | $5,000 | $15,000 | $30,000 | $15,000 | $45,000 | $90,000 |
| Caught by the audit | $625 | $2,625 | $6,375 | $2,500 | $10,500 | $25,500 | $7,500 | $31,500 | $76,500 |
| Credited by carriers = **recoveries** (run-rate) | $375 | $2,100 | $5,738 | $1,500 | $8,400 | $22,950 | $4,500 | $25,200 | $68,850 |
| Invoices a year | 250 | 250 | 250 | 1,000 | 1,000 | 1,000 | 3,000 | 3,000 | 3,000 |
| Disputes filed | 8 | 15 | 25 | 30 | 60 | 100 | 90 | 180 | 300 |
| **Fee at 20%** | $75 | $420 | $1,148 | $300 | $1,680 | $4,590 | $900 | $5,040 | $13,770 |
| **Fee at 25%** | $94 | $525 | $1,434 | $375 | $2,100 | $5,738 | $1,125 | $6,300 | $17,212 |
| **Fee at 35%** | $131 | $735 | $2,008 | $525 | $2,940 | $8,032 | $1,575 | $8,820 | $24,098 |
| Cost to serve, bottom-up **[our call]** | $815 | $905 | $1,025 | $1,460 | $1,820 | $2,300 | $3,180 | $4,260 | $5,700 |
| **Gross profit at 20%** | −$740 | −$485 | $122 | −$1,160 | −$140 | $2,290 | −$2,280 | $780 | $8,070 |
| **Gross profit at 25%** | −$721 | −$380 | $409 | −$1,085 | $280 | $3,438 | −$2,055 | $2,040 | $11,512 |
| **Gross profit at 35%** | −$684 | −$170 | $983 | −$935 | $1,120 | $5,732 | −$1,605 | $4,560 | $18,398 |
| Gross profit at 25%, PRGX-style cost (60% of fee, sourced) | $38 | $210 | $574 | $150 | $840 | $2,295 | $450 | $2,520 | $6,885 |
| **First-year backlog recoveries (one-off)** | $150 | $1,785 | $6,311 | $600 | $7,140 | $25,245 | $1,800 | $21,420 | $75,735 |
| Backlog cost, including $1,000 onboarding | $1,086 | $1,259 | $1,468 | $1,344 | $2,037 | $2,870 | $2,032 | $4,111 | $6,610 |
| **Backlog gross profit at 25%** | −$1,048 | −$813 | $110 | −$1,194 | −$252 | $3,441 | −$1,582 | $1,244 | $12,324 |
| Backlog gross profit at 35% | −$1,034 | −$634 | $741 | −$1,134 | $462 | $5,966 | −$1,402 | $3,386 | $19,897 |
| Year-2 recoveries if the rate falls 40% | $225 | $1,260 | $3,442 | $900 | $5,040 | $13,770 | $2,700 | $15,120 | $41,310 |
| Year-2 gross profit at 25% (rate −40%) | −$723 | −$518 | −$44 | −$1,091 | −$272 | $1,622 | −$2,073 | $384 | $6,068 |

**How to read the two cost lines:**
- The **bottom-up** line assumes a lean, mostly automated service. Its fixed $600 dominates small accounts.
- The **PRGX-style** line scales with revenue, so it can never go negative. It hides the fact that a human-heavy service would simply not take small accounts.

### 10.3 Freight spend at which the yearly fee reaches $5k, and gross break-even

TL+LTL spend a year, with the bottom-up cost; break-even means the run-rate fee covers the cost to serve **[our calc]**.

| Rate set | Recovered | $5k fee at 20% | $5k fee at 25% | $5k fee at 35% | Break-even at 20% | Break-even at 25% | Break-even at 35% |
|---|---|---|---|---|---|---|---|
| Low | 0.15% | $16.7M | $13.3M | $9.5M | never | never | never |
| **Central** | 0.84% | $3.0M | **$2.4M** | $1.7M | $1.3M | **$0.68M** | $0.35M |
| High | 2.30% | $1.1M | $0.87M | $0.62M | $0.21M | $0.15M | $0.10M |

"Never" means the per-invoice and per-dispute costs alone exceed the fee earned per dollar of spend.

### 10.4 What this means for the 95,579 firms [our calc, low confidence]

- **Mapping the central thresholds onto §7.4:**
  - Manufacturers with 20-99 staff (central spend about $0.27M) fall below break-even at 25%.
  - Wholesalers with 20-99 staff (about $0.63M) sit near break-even.
  - Both 100-499 groups clear it.
- **Using the finer SUSB bands for shape only:**
  - About **28,000 firms** (manufacturers with 100-499 staff, wholesalers with 50-499) have a mean central spend above $0.68M.
  - Only about **5,400** (manufacturers with 300-499 staff, wholesalers with 200-499) have a mean above $2.4M, where a 25% fee reaches $5k a year.
  - Means overstate the typical firm, so these counts are ceilings.
- **Fee pool re-cut on the bottom-up spend** (all firms, ignoring break-even): central $73.6B × 0.84% = $618M of recoveries a year. At 25% that is **$155M**, against the desk's central $209M at 20%. Low: $12M. High: $721M.

---

## 11. Numbers the web could not settle

Only interviews or the savings assessment on real invoices can measure these (assessment §6.1 in `5_validation.md`; kit blocks C and E):

1. **The overcharge rate on a mid-sized shipper's own TL and LTL bills** (H09-02), split by error type: duplicates, rate differs from the agreement, fuel, accessorials, reweigh/reclass, and math. No neutral private-sector figure exists. **This is the number that decides the model:** a move from 0.5% to 1.5% turns every column from loss to profit.
2. **Invoices per $1,000 of spend** for these shippers (LTL-heavy accounts may run 2-3× Cass's average), and the share of bills that arrive as PDF, EDI 210 or portal downloads. This sets the per-invoice cost.
3. **What share of flagged overcharges carriers credit**, and how fast, when the shipper is mid-sized, has no offset beyond future bills, and may buy TL through brokers. Test with dated claims from the assessment.
4. **Contract terms:** how many shippers' TL contracts or broker rate confirmations waive 13710, or set their own claim windows. Read the actual agreements.
5. **The real look-back depth:** how many months of paid invoices, rate agreements and PODs a shipper can actually produce (H09-07).
6. **Analyst minutes per dispute and per exception** on real bills, with AI reading. No public figure exists.
7. **Year-2 decay:** whether errors recur after the first findings are fixed. Only a repeat measurement over time answers this; S5 can at most ask what happened after any past audit.
8. **Which share is accepted** (H09-06), and whether a shipper already has a contingency firm on 50% (H09-01, H09-08).
9. **The TL+LTL share of each shipper's transportation cost** (private fleet, parcel, customer pick-up, freight inside supplier prices), which moves the spend bands by about 2×.
10. **CAC and sales-cycle length** for this buyer, from the S5 funnel (W1 metrics).

---

## 12. For the coordinator (not a call)

1. **The money chain is very sensitive to one unmeasured input.** Per-customer gross profit changes sign between an overcharge rate of 0.5% and 1.5% of TL+LTL spend, and no neutral source measures that rate for private shippers. Every neutral figure found (0.07% after federal pre-audits; 0.1-0.48% on general purchases) sits below the desk's 1-3%. **H09-02 leans against its upper half, and the fail line (under 0.5%) is a realistic outcome.** The savings assessment is the decisive test.
2. **The $5k-a-year benchmark needs about $2.4M of TL+LTL spend at central rates and a 25% fee.** That is roughly 3× the average firm in the 95,579 ($0.77M, the low end of the desk range), and it probably holds for only about 5,000 firms. At a lean automated cost, break-even needs about $0.68M. **An audit-only contingency product for the lower half of the segment (manufacturers with 20-99 staff, about 45,000 firms) does not pay at central rates** **[our calc]**.
3. **H09-06 (25% accepted) leans for, on price.** Small shippers are already offered 50/50 splits, and 25-50% is the freight norm. But 25% is also the share at which small accounts lose money in §10, so the evidence points to price *per account size* as a question for the founders, not to acceptance.
4. **Collection falls with delay.** Uncollected overcharges rose from under 10% to about 35% as issue lag went from under 400 to over 800 days (GSA), and PRGX's clients push audits "closer to the time of the transaction". A once-a-year look-back collects less per dollar found than a monthly or pre-payment audit. Pre-payment audit, though, leaves no recovery to take a share of, so the fee basis would have to change.
5. **Recurring revenue is thinner than the first year suggests.** On central inputs the backlog is about 46% of first-year recoveries. General recovery audits lose about 80% of their rate once fixes are in, and PRGX's commercial clients buy audits "every two to three years". No freight-specific decay was found; whether carrier-side errors recur more than AP duplicates is untested.
6. **Human-heavy contingency auditing is a 35-39% gross-margin business** (PRGX, over two decades), with rate pressure and clients' control over claims as the named risks. The public-sector buyers who pay 4-20% show where the price goes as volume and bargaining power rise.
7. **Evidence gaps that stay open:**
   - carrier refusal practices (H09-C4 is untested);
   - how often contracts waive the 180-day rule;
   - audit-client churn;
   - any CAC or referral commission rate in freight or parcel audit.
8. **Hypotheses the web touched:**
   - **H09-02** leans against the upper half.
   - **H09-05** (no budget line) leans for: contingency is chosen by SMBs for no out-of-pocket cost, per N-X28, a vendor.
   - **H09-06** leans for, on price.
   - **H09-08**: no evidence either way. SMB tools with some audit features cost $0-200 a month, and 50/50 contingency firms exist.
   - **H09-09, H09-10, H09-11 and H09-C1 to C4:** not answered by the web.

---

## 13. Sources

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-X01 | GSA Office of Inspector General, "Audit of the Postpayment Audit Process, Transportation Audits Division", report A120169/Q/9/P14002 | 2014-03-31 | https://www.gsaig.gov/sites/default/files/audit-reports/A120169_1.pdf | full (PDF text) | $16.3B bills; $33.1M issued / $6.3M written off; lag times; collection rates by contractor; lag vs uncollected; 60-day protest; tolling; staffing |
| N-X02 | GAO/NSIAD-92-157, "GSA Transportation Audits: Contract Costs Can Be Reduced" | 1992-06-03 | https://www.gao.gov/assets/nsiad-92-157.pdf | full (OCR PDF text; some table cells garbled) | $10.2M motor carrier collections; 22% / 28% found only at second audit; 3.9% and 26% commissions; transaction fees $0.28-0.39; fees >75% of first-audit payments |
| N-X03 | GAO/AFMD-89-47, "Transportation Audits: GSA's Accounting for Transportation Overcharges" | 1989-08-30 | https://www.gao.gov/assets/afmd-89-47.pdf | full (PDF text) | $100.8M collected FY87-88; disbursements $16.6M and $17.4M |
| N-X04 | GAO/T-NSIAD-99-213, "Recovery Auditing: Reducing Overpayments, Achieving Accountability, and the Government Waste Corrections Act of 1999" | 1999 | https://www.gao.gov/assets/t-nsiad-99-213.pdf | full (PDF text) | PRG at DoD: $29.3M on $6B; 0.48% → 0.1%; $2.6M collected; 20% fee |
| N-X05 | Texas Comptroller, "Administering Overpayment Recovery Audits in Texas", Report to the 82nd Legislature | 2010-12 | https://fmx.cpa.texas.gov/fm/audit/recovery/rpt2010/96-1242.pdf | full (PDF text) | $57.6B analysed, $1.08M recovered; LBB 0.1% / 0.03-0.05% / 20-40%; 13.5% contract; categories; PRG-Schultz 50% |
| N-X06 | 31 U.S.C. 3726 (Cornell LII) | current | https://www.law.cornell.edu/uscode/text/31/3726 | full (extraction) | (a) prepayment audit; (d) 3-year deduction; (e) 50% contractor cap |
| N-X07 | 49 U.S.C. 14101 (Cornell LII) | current | https://www.law.cornell.edu/uscode/text/49/14101 | extraction (partly verbatim) | (b)(1) contracts and waivers; (b)(2) remedy |
| N-X08 | Federal Register 2024-27552, FMR "Transportation Payment and Audit Regulations", final rule | 2024-11-26 | https://www.federalregister.gov/documents/full_text/text/2024/11/26/2024-27552.txt | full (API text) | Offset definition; 102-118.615 GSA offsets; no dollar figures |
| N-X09 | GSA, "Postpayment Audits" page and Directive 5450.39D (search summaries) | 2025 | https://origin-www.gsa.gov/buy-through-us/products-and-services/transportation-and-logistics-services/transportation-audits/postpayment-audits | blocked (403); snippet | "over 12 million transportation invoices per year"; 2025 delegation of audit authority to agencies |
| N-X10 | Transportation law webinar, "61 Good Reasons Not to Waive Federal Transportation ..." (transportationlaw.net) | 2008-04-15 | https://www.transportationlaw.net/webinars/DNA-2008.04.15%20-%2061%20Good%20Reasons%20Not%20to%20Waive.pdf | full (slide text) | 13710 and 49 CFR 378 among waived items; "post audit traps" |
| N-X11 | FreightWaves, "Yellow paying $6.8M to settle DOD overcharging claim"; "Gov't lawsuit against YRC shines light on LTL reweighing practices"; DOJ release (snippet only; page rendered empty) | 2022-03-10; 2018-19 | https://www.freightwaves.com/news/yellow-paying-6-8m-to-settle-dod-overcharging-claim ; https://www.freightwaves.com/news/ltl-suit-against-yrc-spotlights-reweighing-practices ; https://www.justice.gov/archives/opa/pr/freight-carriers-agree-pay-685-million-resolve-allegations-knowingly-presenting-false-claims | full (articles); DOJ snippet | $6.85M settlement; overcharge never quantified; reweigh allegation |
| N-X12 | PRGX Global, Form 10-K FY2018 | filed 2019 | https://www.sec.gov/Archives/edgar/data/1007330/000100733019000004/a201810kprgx.htm | full text downloaded and searched | Revenue, COR, Americas COR %, employees, client concentration, risks, competition |
| N-X13 | PRGX Global, Form 10-K FY2009 | filed 2010 | https://www.sec.gov/Archives/edgar/data/0001007330/000095012310029515/g22652e10vk.htm | partial (fetch-tool extraction of quoted passages) | Commercial audits periodic; clients resolve deficiencies; long sales cycle; price pressure; 35% gross margin |
| N-X14 | Cass Information Systems, Q4 and FY2024 earnings release (8-K Ex. 99.1) | 2025-01 | https://www.sec.gov/Archives/edgar/data/708781/000070878125000002/cass-20241231xexx991.htm | full (extraction) | Processing and financial fees, net interest income, invoice and dollar volumes |
| N-X15 | Cass, "Cass Reports Record Annual Net Income and EPS" (company news page) and search summary of the Q4 2025 release | 2026-01-22 | https://www.cassinfo.com/news/cass-reports-record-annual-net-income-and-eps | partial; Q4 volumes from snippet (*assumed*) | FY2025 net income $35.1M; Q4 2025 8.4M invoices (−6.1%), $9.2B |
| N-X16 | Ardent Partners, "Accounts Payable Metrics that Matter in 2025" (Pagero-hosted PDF) | 2025 | https://www.datocms-assets.com/80283/1744404602-ardent-partners-ap-metrics-that-matter-in-2025-pagero-final.pdf | full (PDF text) | 14% exception rate; 9.0% vs 22.0%; $9.40; 9.2 days; 3.1 vs 17.4 days; 32.6% straight-through; 212 respondents |
| N-X17 | Ardent Partners, Payables Place, "State of ePayables (Part Nine): AP Benchmarks and Best-in-Class Performance" | 2026-01 | https://payablesplace.ardentpartners.com/2026/01/state-of-epayables-part-nine-ap-benchmarks-and-best-in-class-performance/ | extraction | $9.84; 8.2 days; 18.4% exceptions |
| N-X18 | APQC, "Percentage of Duplicate Disbursements Processed" (403), via ExpensePoint snippet | undated | https://www.apqc.org/resource-library/resource-listing/percentage-duplicate-disbursements-processed | blocked; snippet (*assumed*) | 0.8% / 1.5% / 2% of disbursements |
| N-X19 | Congressional Research Service R40592, "Medicare's Recovery Audit Contractor (RAC) Program: Background and Issues" (EveryCRSReport) | 2009-05-21 | https://www.everycrsreport.com/reports/R40592.html | extraction | 9.0-12.5% fees; $1.03B identified; $693.6M returned; appeal rates |
| N-X20 | North Carolina Office of the State Controller, "Overpayment Audit and Recovery" | current | https://www.ncosc.gov/state-agency-resources/overpayment-audit-and-recovery | full (extraction) | PRGX FY2024-2028; paid only from recoveries; freight among categories |
| N-X21 | Establish Inc., "Logistics Cost and Service 2020: The Establish Davis Database" | published 2021-12 | https://static1.squarespace.com/static/57bf65a1c534a52224df643c/t/61bcda757d58a3178229263b/1639766645913/Logistics+Cost+and+Service+2020+Updated.pdf | full (PDF text; charts not read) | Transportation 3.68% of sales; by industry 2.38-4.76%; size effect up to 50% |
| N-X22 | Census, SUSB 2022, us_state_naics_detailedsizes_2022.txt | 2025 release | https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.txt | data download (*verified*); inconsistent with sector subtotals | Receipts per firm by detailed size band (shape only) |
| N-X23 | GingerControl, "Freight Invoice Audit: Where the 5-10% Billing Errors Hide (2026)" | 2026 | https://gingercontrol.com/blog/freight-invoice-audit-guide | extraction; blog (*assumed*) | Orphan attributions; Tompkins 5-10%; Ardent 14%; in-house below ~$500K |
| N-X24 | Tompkins Ventures, "Why Freight and Parcel Shipping Require Post-Auditing" | 2026-07-07 | https://tompkinsventures.com/why-freight-and-parcel-shipping-require-post-auditing/ | extraction; vendor (*assumed*) | 5-10% of invoices; 3-10% trim; contingency |
| N-X25 | Nuvocargo, "Freight Invoice Errors and Hidden Costs (2026 Guide)" | 2026 | https://www.nuvocargo.com/blog-posts/freight-invoice-errors-hidden-costs | extraction; vendor (*assumed*) | Error-type table; no primary sources |
| N-X26 | Eller Audit, "LTL Freight Audit: A Plain-English Guide for LTL Shippers" | current | https://www.elleraudit.com/ltl-freight-audit | extraction; vendor (*assumed*) | LTL error types; recovery by category; median 2-5% |
| N-X27 | Laneproof, "Freight Invoice Dispute Process: Step-by-Step Guide for Brokers" | 2026-03-23 | https://www.laneproof.com/blog/freight-invoice-dispute-process-guide | extraction; vendor (*assumed*) | 3.8% variance, $127; 65-80%; 74% vs 41% |
| N-X28 | Software Solutions Inc. (SSI), "Useful insights for procurement of freight audit and freight payment services" (white paper) | 2020-11 (upload) | https://ssui.com/wp-content/uploads/2020/11/SSI-freight-audit-rfp-white-paper.pdf | full (PDF text); vendor | Per-transaction common among majors; contingency for SMBs, e.g. 50/50; float pricing |
| N-X29 | Freightview, pricing page | current | https://www.freightview.com/pricing | full (extraction); stated price | $149/month for 0-50 shipments |
| N-X30 | MyCarrier, "2026 Pricing" | current | https://go.mycarrier.io/plans-and-pricing | full (extraction); stated price | $0 / $60 / $200 / custom; add-ons |
| N-X31 | FreightPOP, pricing page | current | https://www.freightpop.com/pricing | full (extraction) | Call for quote; tiers; "Carrier Invoice Audit" row |
| N-X32 | Parcel Refund Services, home page | current | https://www.parcelrefundservices.com/ | full (extraction); stated terms | 50-50 contingency |
| N-X33 | RefundPros, "Parcel Audit Services" | current | https://refundpros.com/parcel-audit-services/ | full (extraction) | % of refunds after credits; negotiable for volume |
| N-X34 | LateShipment.com, partners page | current | https://www.lateshipment.com/partners/ | full (extraction) | Partner types; "considerable recurring compensation"; no % |
| N-X35 | Navix, "How Much Does Freight Audit Cost? Pricing Models Explained" | current | https://www.navix.io/freight-audit-cost/ | full (extraction); vendor | Four models; "Vendors rarely publish numbers" |
| N-X36 | thirdfin.io, "Loop Freight Audit Review — Features, Pricing, Alternatives" | current | https://thirdfin.io/freight-audit/loop-freight-audit/ | extraction; third party (*assumed*) | No published pricing; mid-market and enterprise |
| N-X37 | Heavy Duty Trucking (truckinginfo.com), "PowerTrack Use Increases For MTMC Carrier Payments" | 2002-05-22 | https://www.truckinginfo.com/news/powertrack-use-increases-for-mtmc-carrier-payments | full (extraction) | Carriers pay 1-2% sliding fee |
| N-X38 | Goodman-Reichwald-Dodge, "Freight Post Audit Services", plus search summary | current | https://www.freightbillauditor.com/PostAuditServices | page extraction (no %); 50% from search summary (*assumed*) | "only a % of the money we collect"; filing deadlines |
| N-X39 | Hatfield & Associates, "The Shocking Truth About Freight Cost Recovery" | current | https://hatfieldandassociates.com/the-truth-about-freight-cost-recovery/ | extraction; vendor (*assumed*) | Orphan statistics (15%, 1-5%, 80%) |
| N-X40 | Foreign Policy Journal, "Freight Bill Audits: The Errors Most LTL Invoices Hide" | 2026-08-26 | https://www.foreignpolicyjournal.com/2026/08/26/freight-bill-audits-the-errors-most-ltl-invoices-hide/ | extraction | No rates cited |
| N-X41 | FreightCenter, "Freight Bill Audit" | current | https://www.freightcenter.com/freight-bill-audit/ | extraction | Error types audited; no pricing |
| N-X42 | ITQlick / SaaSworthy estimates of FreightPOP pricing (search summary) | 2026 | https://www.itqlick.com/freightpop/pricing | snippet (*assumed*) | About $99/month single user; $500-1,500 for ten users |
| N-X43 | Umbrex, "Logistics Cost as Percentage of Sales Guide" (search summary) | current | https://umbrex.com/resources/company-analysis/supply-chain-logistics/logistics-cost-as-percentage-of-sales/ | snippet (*assumed*) | Wholesale/B2B logistics 3-8% |
| N-X44 | Search summary of freight-audit buyer guides (locus.sh, Senvo, Racklify) on volume thresholds | 2026 | https://locus.sh/blogs/freight-audit-settlement-software-buyers-guide-2026/ | snippet (*assumed*; exact origin unclear) | "over 500 invoices per month" |
| N-X45 | Getlatka, Zippia and other aggregators on Trax and nVision (search summary) | various | https://getlatka.com/companies/trax-technologies | snippet (*assumed*) | Conflicting revenue and headcount |
| N-X46 | GSA, FY2023 Agency Financial Report | 2023-11 | https://www.gsa.gov/system/files/GSA_AFR_FY_2023_508_compliant_rev-1.pdf | full text searched | Transportation Audits is a special fund; no overcharge totals |
| N-X47 | TransAudit, "Pre Audit vs Post Audit" | current | https://transaudit.com/pre-audit-vs-post-audit/ | extraction; vendor | No figures; pre-audit "isn't designed to thoroughly capture these errors" |
| N-X48 | OpenEnvoy, "What You Didn't Know About Post-Audit and Second-Audit for Freight Invoices" | current | https://www.openenvoy.com/blog/what-you-didnt-know-about-post-audit-and-second-audit-for-freight-invoices | extraction; vendor | No figures |
| N-X49 | Business Solutions US, contingency invoice audits page | current | https://www.businesssolutionsus.com/feeds/service/small-parcel-contingency-audit-firms | extraction; vendor | No terms; "20-25% Avg Savings" claim |
| N-X50 | 71lbs, partners page | current | https://71lbs.com/partners | extraction | No partner terms shown |

**Earlier sources re-used:** N-A25, N-A26, N-A32 (check A); N-D30 (re-read Item 1: employees, clients, competition), N-D31 (check D); N-E17 (re-parsed today for receipts by size); N-K22 (check K); N-R06, N-R14, N-R21, N-R22 (check R); CFS mode shares from `s1_scan_E_shipper_side.md`; LTL windows and FedEx Freight's filing from `s5_check_T_ltl_carrier_position.md`.

---

## 14. Could not access, or not found

**Search limit reached:** this session's web-search budget (200 searches) ran out partway through X6. Later work used only direct fetches of known URLs and data downloads, so the searches marked † below were **planned but not run**.

**Blocked or unusable:**
- **DoD Inspector General reports** on PowerTrack and freight payments (dodig.mil and media.defense.gov, 403) and **DTIC** (apps.dtic.mil, 403). DoD freight audit rates were not read.
- **GSA's postpayment audit page** (403); the 12M invoices a year comes from a snippet.
- **APQC benchmark pages** (403).
- **SEC direct downloads** refuse requests without a declared contact in the user agent, so PRGX FY2009 and Cass FY2025 were read only through the fetch tool (partial). The Cass FY2025 segment note and fee lines were not reached.
- **Cass investor-relations release for FY2025** (timeout) and **Business Wire** (403).
- **The DOJ YRC press release** rendered empty.
- **The GAO 1992 table** of fee versus commission payments by mode is garbled in the OCR, so only the transaction-fee rows were used.
- **The SUSB detailed-sizes file** disagrees with the sector subtotals (§7.1).

**Searched, not found:**
- A neutral overcharge rate for **private-sector TL/LTL bills** (GAO, GSA OIG, academic "freight bill audit" searches). Only government post-audits and vendor copy were found.
- A **freight-specific breakdown by error type** from any neutral source.
- **EDGAR full-text hits** for "freight audit" plus "overcharges" in 10-Ks, 2015-2026: zero.
- **Per-invoice prices** for freight audit and payment in any public contract, GSA schedule price list, state award or university RFP award (three searches). Only the 1989 GSA transaction fee and Cass's disclosed fee totals were found.
- **Stated minimum spend or invoice volumes** at any freight audit firm.
- **Time per invoice audited** (manual or automated), and analyst staffing ratios at freight audit firms.
- **Revenue per employee** for Trax, nVision, CTSI-Global or Intelligent Audit from any reliable source.
- **Audit-client churn or retention** for any freight audit firm.
- **Carrier refusal rates**, or a count of shipper contracts that waive 49 U.S.C. 13710.
- **CAC or sales-cycle length** at any freight audit firm; **referral commission rates** for CPA firms, ERP resellers, banks or 3PLs.
- **Look-back versus ongoing** contingency shares.

**Not attempted, or cut by the search limit (†):**
- † Canadian (PSPC, Auditor General) and UK public freight audits.
- † GAO or inspector-general reports on DoD's Third Party Payment System after 2009.
- † Academic studies via Google Scholar or journal sites (the scholarly search connector was down this session).
- † CSCMP State of Logistics 2026 (the 2025 split is used via N-K22).
- † The IOFM duplicate-payment benchmark.
- BEA input-output use tables for truck transportation by industry (needs an API key or large workbook parsing; Establish Davis used instead).
- Gartner's 2026 Market Guide list and Peer Insights (login).
- Loop's and Freightgate's pricing (not public; no sign-up attempted).
