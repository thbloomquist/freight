# S5 check AB: what audits of private shippers actually find and get back (C-09)

- **What this is:** new desk research for S5 in run 01, written for the C-09 working bet (checking and paying truckload and LTL freight bills for US manufacturers and distributors with 20-499 staff). It tests the two inputs the founders called the unknown in the per-customer chain:

  > fee = freight spend × **overcharge rate** × share caught × **share carriers credit** × fee share

  It answers AB1-AB5 from the brief.
- **Date:** 2026-09-17. Everything new here was accessed on 2026-09-17.
- **Status:** input to S5. **It decides nothing.** Every suggestion is **[our call]**.
- **Not redone here:** the neutral government figures, vendor 2-8% claims, GAO catch rate and GSA collection rates (`s5_check_X_c09_money.md` §2-§4, §8); LTL tariff and claim rules (`s5_check_T_ltl_carrier_position.md`); public wrong-bill anecdotes (`s5_check_Z_c09_voice.md` §3).
- **Labels:**
  - *verified*: read at the source (statute, court opinion, SEC filing page, government report, a vendor's own page for "what the vendor says").
  - *assumed*: a search snippet, a vendor claim or case study, a secondary summary, a forum anecdote or memory. **Every vendor case-study figure is *assumed* even when the page was read in full**; where a page was read in full this is said separately.
  - **[our calc]** = our arithmetic. **[our call]** = our judgement.
- **New source IDs:** N-AB01 to N-AB48 (§10). Earlier IDs keep their meaning (N-X01, N-X02, N-X04, N-X26, N-X27, N-Z04, N-T05, N-T36, N-J28, N-N30).

**Words used here:**
- **Found / identified:** the auditor says a charge was wrong. **Recovered / credited:** the money actually came back (a credit, refund or a bill the shipper never paid).
- **Pre-payment audit:** the bill is checked before payment; an error is short-paid or held, so nothing has to be collected back. **Post-payment audit (look-back):** paid bills are re-checked and claims are filed.
- **Savings:** in vendor copy this usually mixes overcharge recovery with rate renegotiation, mode shifts, consolidation and labour. **It is not the same number** and §2.3 shows the gap.
- **Dilution (factoring/ABL):** the share of invoice value a seller never collects because of credits, disputes and short pays.
- **Revenue adjustment (carrier accounting):** a downward correction to revenue already billed - the carrier-side mirror of a shipper recovery.

---

## 1. Summary

| Q | Headline | Best evidence | Label |
|---|---|---|---|
| **AB1** Cases with both numbers | **Only 6 freight cases were found that state both a spend base and an overcharge amount**, across roughly 20 vendor case libraries. Their implied recovered/identified rate is **0.80%, 0.87%, 1.00%, 2.60%, 2.92%, 4.23% of spend — median 1.80%** **[our calc]**. Five of the six are large shippers ($8.5M-$100M+ of spend); the only one plausibly inside C-09's segment ($22M-revenue chemical manufacturer) is also the highest, at 4.2% of a 24-month look-back. 30+ further cases publish an amount with no spend, or a "savings" percentage that is mostly rate renegotiation | N-AB01, N-AB02, N-AB08, N-AB15, N-AB17, N-Z04 | vendor cases *assumed*; rates **[our calc]** |
| **AB1** Bias | The register is a **selected sample of vendors' best results**, published to sell. Four of the six are first-year onboardings of a full freight-audit-and-payment programme at a large shipper, where a backlog and an unaudited history are being cleaned up at once | §2.4 | **[our call]** |
| **AB2** Neutral private evidence | **One neutral private-sector dataset exists and it is from 1977.** USDA surveyed 445 farm cooperatives: 34 that could report both numbers collected **$2.19M of overcharge claims against $486.4M of regulated transportation cost — 0.45%** (0.14% fruit and vegetables, 0.26% grain, 0.54% farm supplies). Auditors then charged "usually 50 percent" of recoveries. No modern academic, court, state, Canadian or UK study measures a private overcharge rate | N-AB31 | *verified* (report text) |
| **AB2** Semi-neutral | A JOC benchmark study of **77 shippers** (three-quarters above $1B of revenue) reported an average **invoice inaccuracy rate of 20.8%** - a share of *invoices*, self-reported, and the authors thought it low. A 40-year practitioner writing in *Logistics Management* (2022) puts **historic error rates at "1% for truck and rail and up to 10% for ocean"**. A second-level post-audit specialist (Trans Audit) says its own yield after FAP and internal audits is **0.5-1.5% of non-parcel spend** | N-AB33, N-AB34, N-AB08 | survey *verified* as reported; rates *assumed* |
| **AB2** Carrier-side filings | **FedEx Freight**, the largest LTL carrier, books all post-billing downward revenue corrections in one line: **$246M (FY2024), $119M (FY2025), $184M (FY2026) — 2.6%, 1.3% and 2.1% of revenue** **[our calc]**. That is every credit for every reason (incentives, service refunds, billing corrections), so it is an **upper bound** on what LTL customers get back after billing. ODFL's reserve for future billing corrections is far smaller: about **$1.3M, or 0.28% of gross receivables** at end-2025 | N-AB37, N-AB38 | *verified* (filing pages); ratios **[our calc]** |
| **AB3** Share credited | No neutral figure for private shippers exists. Vendor and adjacent figures cluster at **60-90%** for disputes filed promptly (broker-side 65-80%; LTL categories 60-92%; parcel refund claims 95% of *eligible* packages; one in-segment case 100% of $95K within 75 days), and fall to about **40-50%** when claims age. **Law caps the look-back:** the 10th Circuit held in 2021 that the 180-day limit in 49 U.S.C. 13710(a)(3)(B) is "not optional" - a class action over a decade-long, concealed LTL reweigh scheme was dismissed as time-barred | N-AB35, N-X27, N-X26, N-AB27, N-AB17 | court *verified*; rates *assumed* |
| **AB4** Recurrence | Every provider that splits first year from later years reports a **large fall**: Fortigo 7-12% first year vs 1-5% established; 5-15% on a new deployment vs 1-1.5% ongoing; A3 Freight Payment "around one-half of 1%" ongoing "because the audit provider should be correcting errors"; Loop's mid-market manufacturer cut linehaul overcharges **63.2%** in nine months; Great Dane's error-carrying invoices fell **7.8% → 3.6%** | N-AB09, N-AB11, N-AB16, N-AB15 | vendor *assumed*; the pattern is consistent |
| **AB5** Parcel (separate) | Parcel yields more and is not a guide to TL/LTL: $24M parcel spend → about **$800K (3.3%)** in a year, with $184K of refunds in one week; $29.3M parcel spend → "in excess of $150,000" (0.5%); refund-claim success **95% of eligible packages**. Ground money-back guarantees stay suspended at FedEx and UPS (earlier notes), so this pool is smaller than the cases suggest | N-AB26, N-AB27, N-J28, N-N30 | *assumed* |

**One-line reading [our call]:** the published private evidence is thin, selected and mostly large-shipper, and it brackets **recovered** money at roughly **0.8-3% of spend in a first audit year and well under 1% once a programme is running** - which is consistent with, not better than, check X's central set.

---

## 2. AB1 · Case-study register

### 2.1 Tier A - cases that state a spend base **and** an overcharge amount

"Implied rate" = amount ÷ spend for the period stated **[our calc]**. "Fit" is to C-09's segment (US manufacturer or distributor, 20-499 staff, TL/LTL): in / near / out.

| # | Firm type & industry | Size stated | Mode | Pre/post | Look-back | Amount, as worded | Found vs recovered | **Implied rate** | Fit | Source, label |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Multi-brand manufacturer of air distribution products (client of Intelligent Audit, FAP) | **$77M freight spend**, 330,896 shipments, 199+ carriers | TL + LTL | pre-payment FAP with dispute management | not stated (programme total) | "More than $2M in savings identified and recovered through structured auditing and dispute management" | mixed wording | **2.60%** | out (size) | N-AB01, *assumed*, read in full |
| A2 | High-volume North American manufacturer (Intelligent Audit) | **$65M freight spend**, 114,000 invoices, 100+ carriers | freight (TL/LTL implied) | pre-payment FAP | not stated | "$1.9M in savings identified and recovered through consistent audit and dispute management" | mixed | **2.92%** | out | N-AB02, *assumed*, read in full |
| A3 | Leading equipment manufacturer (US Bank Freight Payment, via *Inbound Logistics* 2018) | "spending more than **$100 million annually on freight**" | freight, ~24 DCs | pre-payment | one year | "In a single year, the company saw more than $800,000 from audit savings and $2.7 million in duplicate invoice savings" | savings (pre-pay, so prevented) | **≤0.80%** audit; **≤3.50%** with duplicates | out | N-AB08, *assumed* |
| A4 | Great Dane, trailer manufacturer (Loop) | "Loop audited **$8.5M in spend**" | LTL + FTL (parcel later) | pre-payment | 2023 | "Loop identified $73,725 in overcharges and stopped payment on these inaccurate invoices" | identified and prevented | **0.87%** | out (staff) | N-AB15, *assumed*, read in full |
| A5 | Family-owned US **specialty chemical manufacturer** (ValueXPA "margin drift diagnostic") | **revenue $22M**; freight 5.2% of revenue (up from 4.4%); ~$1.14M freight a year **[our calc]** | LTL + dedicated TL, 60% hazmat, 38 states | post-payment | **24 months** | Fuel-formula drift $58K + hazmat compounding $24K + minimum-charge creep $13K = **$95K**; "Total recovered: $95K cash" | found $95K → recovered $95K (**100%**) | **≈4.2%** of 24-month spend (≈8.3% of one year) **[our calc]** | **in** (probable; staff not stated) | N-AB17, *assumed*, read in full |
| A6 | "A medium enterprise", ~**$12M a year** (an AI-audit firm posting on Reddit) | $12M spend | not stated (duplicates and mismatches) | post-payment | 12 months | "~$120K … Vendor credits/reversals successfully recovered" | recovered | **1.00%** | out (size) | N-Z04 (check Z), *assumed* |

**Note on A4:** check X records this case as "$73K on $5.1M" (1.4%). The Loop page as it reads today says "Loop audited $8.5M in spend" and "identified $73,725 in overcharges" (N-AB15, read 2026-09-17), which gives 0.87%. The denominator has moved; the register uses the figure on the page today and flags the conflict.

**Derived fee anchor [our calc, assumption stated]:** Intelligent Audit publishes ROI alongside two of these. If ROI = (benefit − fee) ÷ fee, A1's fee was about **$171k (0.22% of spend)** and A2's about **$191k (0.29%)**; if ROI = benefit ÷ fee, 0.24% and 0.33%. Either way, **a full FAP programme at a $65-77M shipper is priced at roughly 0.2-0.3% of spend**, well under a contingency share of recoveries.

### 2.2 Tier B - an overcharge amount, but no spend base (rate not computable)

| # | Firm type | Amount, as worded | Found vs recovered | Period | Fit | Source, label |
|---|---|---|---|---|---|---|
| B1 | Manufacturing (ConData post-audit) | "$2.2M recovered from over billing pattern discovered" | recovered | not stated | out | N-AB24, *assumed* |
| B2 | Manufacturing (ConData) | "$425,000 in overpayments", historical payment audit, parcel + freight | recovered | not stated | out | N-AB24 |
| B3 | Manufacturing (ConData) | "$1.7 million in overpayments", export freight, contract gaps | recovered | not stated | out | N-AB24 |
| B4 | Manufacturing (ConData) | "$1.7M from misapplied freight charges", dimensional-weight errors | recovered | not stated | out | N-AB24 |
| B5 | Fortune 50 manufacturer (ConData) | "$25 million in hidden overpayments" | recovered | not stated | out | N-AB24 |
| B6 | Unnamed shipper (ICC Logistics) | "$475K recovered in 6 months from misclassifications and fuel surcharge errors" | recovered | 6 months | unknown | N-AB22, *assumed* |
| B7 | 3PL partner (ICC) | "$210K saved through a multi-modal LTL and FTL audit" | saved | not stated | out | N-AB22 |
| B8 | Manufacturer (ICC) | "$96K recovered from duplicate billing in the first audit cycle" | recovered | first cycle | unknown | N-AB22 |
| B9 | **Food distributor** (ICC) | "$78K recovered through a post-payment LTL audit" | recovered | not stated | **near** | N-AB22 |
| B10 | Mid-market **process (polymer) manufacturer** (Loop) | "$10,000 in overcharges" identified in the first nine months; overcharges then fell (linehaul −63.2%, fuel −23.3%, accessorial −13.5%) | identified | 9 months | **near** | N-AB16, *assumed*, read in full |
| B11 | Global fine-art dealer (FreightOptics) | "$37,714 in fuel surcharge overcharges were identified and recovered" in 1.5 months, plus "approximately $100,000 … from misaligned rates"; $400M **revenue** given, no freight spend | identified + recovered | 1.5 months + | out | N-AB19, *assumed*, read in full |
| B12 | Large distributor (Intelligent Audit) | "$1.9M in recoveries and prevented overcharges", ~120,000 freight invoices, TL and LTL, "150+ audit points" | mixed | not stated | out | N-AB04, *assumed* |
| B13 | Global manufacturer of electrical/industrial power management (Intelligent Audit) | "$10.4M in audit & recovery savings ($9.2M freight; $1.2M parcel)" annualised, plus $3.02M optimisation and $1.74M anomaly detection; ROI 1,906% | mixed | annualised | out | N-AB03, *assumed* |
| B14 | Global multi-brand manufacturer (Intelligent Audit, anomaly detection) | "$220,000 in new, unplanned spend" surfaced early (a new "Additional Classification Fee" on a non-authorised brokerage account) | prevented | ongoing | out | N-AB07, *assumed* |
| B15 | Specialty coffee retailer (enVista, *Inbound Logistics* 2019) | "recovered more than $420,000 in charges resulting from rating errors" | recovered | not stated | out | N-AB11, *assumed* |
| B16 | Global apparel company (CT Logistics) | "20% Accuracy Improvement: Reduced overpayments by $1.5M annually" | reduced | annual | out | N-AB28, *assumed* |
| B17 | Global medical device company (CT Logistics) | "15% reduction in duplicate payments and billing errors" | reduction | not stated | out | N-AB28 |
| B18 | International medical-device manufacturer (Data2Logistics, archived 2007 page) | "In less than one year, Data2Logistics recovered more than $500,000 in express freight charges" (pre-payment audit of express) | recovered | <1 year | out | N-AB29, *assumed* |
| B19 | Manufacturing client (Cass, parcel stories) | "$140,000 on late fees in a 14-month period … the client asked for and received a refund"; separately "$60,000" of misused-account charges refunded and rebilled | recovered | 14 months | out | N-AB30, *assumed* |
| B20 | Industrial-hose distributor, $42M revenue (ValueXPA) | "$315K in vendor overbilling" - **vendor invoices generally, not freight**; listed only to mark the boundary | recovered | not stated | out of scope | N-AB18, *assumed* |
| B21 | Global electrical distributor Rexel USA (AFS) | "recovered over $238,000" through a new LTL **freight claims** process in 15 months (loss/damage, not overcharge) plus $1.17M annualised parcel savings | recovered | 15 months | adjacent | N-AB26, *assumed* |
| B22 | Fast-fashion retailer (Intelligent Audit) | "$785K recovered in lost and damaged claims within 4 months"; "First refunds received within 30 days" | recovered | 4 months | adjacent (L&D) | N-AB07, *assumed* |

### 2.3 Tier C - "savings" with a size anchor (the conflation warning)

These are the numbers vendors publish most often. They are **not** overcharge recovery; most are rate renegotiation, mode shifts, consolidation or labour.

| # | Case | Size anchor | Savings claimed | What actually produced it | Source |
|---|---|---|---|---|---|
| C1 | Industrial manufacturer (FreightOptics) | $500M revenue; implied LTL spend about **$1.8M/yr** **[our calc]** from "$25,000 monthly = 16.5%" | $43k a month ($516k a year) | 4 contracted rates replacing third-party tariffs, plus removing supplemental insurance charges | N-AB20 |
| C2 | Industrial supply distributor (CT Logistics) | ~200,000 LTL shipments, **$40M spend** | "overall savings of 6%… $2.4M" | LTL contract optimisation | N-AB28 |
| C3 | Shipper with about **$100M spend** (RateLinx, *IL* 2018) | $100M | "$1 million" a year | restructuring LTL rates using invoice data | N-AB08 |
| C4 | Manufacturer (Data2Logistics, archived 2019) | implied LTL spend about **$1.67M** **[our calc]** | "$350K Annual Savings (21%)" | LTL bid | N-AB29 |
| C5 | Industrial manufacturer (Data2Logistics) | implied LTL spend about **$3.0M** **[our calc]** | "$575K Annual Savings (19%)" | LTL RFP | N-AB29 |
| C6 | Global medical equipment maker (Data2Logistics) | implied FTL spend about **$8.7M** **[our calc]** | "$1.3MM Annual Savings (15%)" | FTL RFP re-analysis | N-AB29 |
| C7 | Industrial distributor (Intelligent Audit) | thousands of LTL shipments a month | "13.2% reduction in total LTL freight spend"; "35% decrease in reclass-related disputes" | standardising NMFC classes across DCs | N-AB05 |
| C8 | Family-owned fastening and hardware distributor (AFS) | not stated | "14%" of transportation spend | carrier consolidation + renegotiation, with overcharge recovery bundled in | N-AB26 |
| C9 | Musco Family Olive Company (AFS) | not stated | ">10% on total transportation spend in first year" | managed transportation + TMS | N-AB26 |
| C10 | Ecolab (RateLinx) | 700k freight invoices a year | "reduced freight costs by 4.5%" | audit + carrier resolution services | search summary, *assumed* |

**The gap:** sourcing and network savings in Tier C run **4.5-21%** of the relevant spend; overcharge recovery in Tier A runs **0.8-4.2%**. A vendor quoting "we save 3-8%" is usually quoting Tier C **[our call]**.

### 2.4 Summary statistics **[our calc]** - and why they are biased

Tier A, freight only (n = 6):

| Cut | n | Values (% of spend) | Median | IQR |
|---|---|---|---|---|
| All freight cases | 6 | 0.80, 0.87, 1.00, 2.60, 2.92, 4.23 | **1.80%** | 0.87-2.92% |
| Pre-payment (prevented) | 4 | 0.80, 0.87, 2.60, 2.92 | 1.74% | - |
| Post-payment (cash back) | 2 | 1.00, 4.23 | 2.62% | - |
| Wording "recovered" only | 2 | 1.00, 4.23 | 2.62% | - |
| Wording mixes "identified and recovered" | 3 | 0.80 (savings), 2.60, 2.92 | 2.60% | - |
| **In segment** | 1 | 4.23 | - | - |
| Near segment | 0 | - | - | - |
| Out of segment | 5 | 0.80, 0.87, 1.00, 2.60, 2.92 | 1.00% | - |
| By mode: TL+LTL stated | 4 | 0.87, 2.60, 2.92, 4.23 | 2.76% | - |
| Parcel (kept separate, §6) | 2 | 0.51, 3.33 | 1.92% | - |

**This is a biased sample and should not be read as a market rate:**
1. **Selection.** Every Tier A case except A6 is published by the auditor to win business. Losing engagements, and audits that found nothing, are never published.
2. **Mixed wording.** Four of six say "savings" or "identified and recovered"; only A5 and A6 clearly report cash that came back. A3's figure is a pre-payment "savings" number, so nothing had to be collected.
3. **First-year effect.** A1-A4 are onboardings of a full audit-and-pay programme, where an unaudited history is cleaned at once. §5 shows the same providers quoting far lower ongoing rates.
4. **Denominator drift.** "Spend managed", "spend audited" and "annual freight spend" are used interchangeably; in A3 the denominator is "more than $100 million", so the rate is an upper bound.
5. **Size.** The median comes from shippers 10-100× larger than C-09's target. The one plausibly in-segment case is the outlier on the high side - and is also the least corroborated (the write-up reads like a templated marketing case; the firm publishes similar cases in four countries).

### 2.5 Vendor-level aggregate ratios (all *assumed*)

| Provider | Aggregate claim | What it implies **[our calc]** |
|---|---|---|
| ConData (post-audit specialist) | "$645M+ errors identified" (home page) and "$328M+ recovered" (post-audit page); also "$50B+ freight spend processed annually" and, on the post-audit page, "$645M+ Freight and parcel spend processed annually" | If both figures share a base, **51% of identified dollars were recovered**. The two pages label $645M inconsistently, so this is weak |
| ConData | "FAP providers achieve 98% accuracy at best under net-30 payment windows. We find the remaining 2%"; "50% of our revenue comes from clients who already have FAP providers" | A second-level post-audit lives on the 2% a pre-audit leaves |
| Trans Audit (post-audit, contingency, "45-year" history) | "Savings for non-parcel activity generally run between .5 to 1.5 percent, while savings for parcel can approach 5 percent"; ">$1 billion in benefits to its Clients"; look-back "up to five years" for payment errors, "six months to three years" for billing errors | The closest thing to a published **post-audit yield after somebody else has already audited**: 0.5-1.5% |
| CT Logistics | "FreitRater identifies gross savings between the billed amount and the paid amount, averaging about 3.2%" (blended; new clients save more) | A pre-payment catch rate on billed dollars |
| Intelligent Audit | audited "more than 1.1 billion shipments … more than $31 billion in transportation spend" (2021); "Clients typically save between 2 and 20% … with most saving about 5%" | Mixed savings, not recovery |
| CTSI-Global | "Most shippers … save 3 to 5 percent by reducing overcharges and duplicate payments" | Vendor |
| nVision Global | "5 to 9 percent" of annual transportation spend, plus "1 to 2 percent in duplicate payment protection" (2018); "9 and 12%" (2020); "8 to 12%" (2022) | The same vendor's number moves 5→12% across three years |
| AFS Logistics | "AFS' audit process typically identifies errors that account for up to 8% of clients' transportation expenses"; "State of LTL" quoted elsewhere at "8-12% of total LTL spend" pre-audit error rates | Vendor |
| Data2Logistics (archived 2019) | "our average recovery rate is 5% - 15%" | Vendor; the same page's cases are all sourcing savings |

---

## 3. AB2 · Neutral and semi-neutral evidence on private overcharge rates

### 3.1 The one neutral private-sector dataset found (1977 data)

**USDA, Economics, Statistics and Cooperatives Service, ESCS-87, "Cooperative Freight Bill Auditing" (1980), Miller & Brooks** (N-AB31; read in full as archived text; *verified*). A survey of 445 farm cooperatives (76.6% response), 1977 freight:

| Cooperative type | Reporting | Cost of regulated transportation | Freight bills | Collected from claims | **% of transport cost** | Per freight bill |
|---|---|---|---|---|---|---|
| Fruits and vegetables | 7 | $29.8M | 50,950 | $42,341 | **0.14%** | $0.83 |
| Grain | 6 | $66.8M | 101,325 | $176,500 | **0.26%** | $1.75 |
| Farm supplies | 14 | $359.0M | 543,540 | $1,921,874 | **0.54%** | $3.54 |
| Other | 7 | $30.8M | 72,980 | $52,762 | 0.17% | $0.17 |
| **Total** | **34** | **$486.4M** | **768,745** | **$2,193,447** | **0.45%** | **$2.86** |

Other findings, all *verified*:
- "The amount collected seems insignificant compared with the total cost of regulated transportation, just 0.45 percent, yet this represents over $2 million."
- Fees: "Freight bill auditors charge a percentage of the amount recovered on claims, usually 50 percent." Of 45 auditors, 30 charged 50%, three 40%, one 20%, one 10%, two a flat $35-79 a month.
- 46% of cooperatives had their bills audited in 1977; 60% of regulated cost was rail, 34% truck.
- Self-auditors reported "$82,654 saved due to preaudit of freight bills" on top of claims.
- Reported claims data were internally inconsistent (inside audits: "$1,959,130" filed vs "$2,923,533" collected), because different subsets answered each question - a warning about how badly this number is measured even when someone tries.
- Churn: only 4 of 45 auditors had served a cooperative more than 10 years; 20 for five years or less. 40% of auditors "did not report where and what the errors were", so the same errors kept recurring.

**Caveats [our call]:** 1977 was the regulated era (published tariffs, ICC), the mode mix is rail-heavy, and this is *collected*, not *found*. It is nonetheless the only neutral, per-shipper, private-sector measurement located, and it sits with every other neutral figure **below 0.5%**.

### 3.2 Surveys and practitioner statements with a stated method or standing

| Source | Figure | Method | Label |
|---|---|---|---|
| Journal of Commerce benchmark study "Driving Strategic Value Through Outsourcing", reported by FreightWaves/American Shipper, 2020-10-05 (N-AB33) | "Shipper respondents reported an average invoice inaccuracy rate of **20.8%**" - "a figure that seemed low to both Johnson and Lorenze" | 77 shippers, all modes, "nearly three-quarters of which generate $1 billion or more in annual revenue"; the article is sponsored content | *verified* that the study reports it; the rate is self-reported and is a share of **invoices**, not dollars |
| *Logistics Management*, "Freight Payment: What stage are you in?", 2022-01-05 (N-AB34) | "Post-audit firms have been financially successful because **historic error rates have been 1% for truck and rail and up to 10% for ocean**" | A practitioner column ("In 40 years in the industry…"); no data cited | *assumed* |
| Trans Audit in *Inbound Logistics*, 2018 (N-AB08) | Post-audit yield "**.5 to 1.5 percent**" non-parcel, "approach 5 percent" parcel, after FAP providers and internal audits | Vendor statement about its own book | *assumed* |
| A3 Freight Payment in *Inbound Logistics*, 2023 (N-AB09) | "ongoing savings on the audit itself generally are around **one-half of 1%**… The audit provider should be correcting errors" | Vendor | *assumed* |
| Transportation Insight, 2025 (N-AB43) | "between **3 and 6 percent of invoices** contain errors… **1 to 5 percent of total freight spend** recoverable" | Vendor blog | *assumed* |
| Trax, 2026 (N-AB44) | "error rates across enterprise shipping programs typically run between 5 and 12 percent of total freight spend" | Vendor blog, no source | *assumed*; an orphan statistic of the kind check X flagged |
| Search summary only, source page not located (N-AB47) | "Recovery rates on post-audit claims typically run **60-80%** versus nearly 100% for pre-audit catches" | unknown | *assumed*, unverifiable |

### 3.3 Courts, the Board, and public contracts

| Route | What was found | Label |
|---|---|---|
| **Southern Furniture Leasing, Inc. v. YRC Inc.**, 10th Cir. No. 19-3262, 2021-03-03 (N-AB35; PDF read in full) | A putative class action by LTL shippers: "Starting in September 2005, YRC eliminated negative reweigh corrections, resulting in overcharges. YRC did not, however, inform its customers about its revised reweigh policy." The scheme surfaced only when DOJ unsealed a qui tam complaint in December 2018. **Dismissed as time-barred**: "compliance with the 180-day time limit is not optional." The court distinguished *Grupp v. DHL* (2d Cir. 2014: the 180-day limit "cannot apply to a qui tam action under the [False Claims Act]") and declined to follow *Grocery Haulers* (S.D.N.Y. 2012, unpublished, fraud claims under §14704(a)(2)). No overcharge amount against spend is stated; the class alleged injury "far in excess of the $5,000,000" CAFA threshold | *verified* |
| CourtListener full-text search (N-AB36) | "freight audit" returns 20 opinions, "freight bill audit"/"freight auditing" 9. Almost all are **1980s-90s undercharge-era** suits, where auditors acted for bankrupt carriers *against* shippers (Delta Traffic Service, Milne Truck Lines, In re Bulldog Trucking). The direction we care about - a private shipper suing over overcharges - produced one modern case (Southern Furniture). Related but unread: *nVision Global v. Cardinal Health* (N.D. Ga. 2012; a per-transaction **fee** dispute, not overcharges), *Variety Wholesalers v. Salem Logistics* (N.C. App. 2011; FAP misappropriation), *Tenan v. StrategIQ Commerce* (2019; a sales commission), *Mastercraft Interiors v. ABF* (D. Md. 2004), *State v. DHL Express* (N.Y. 2010; fuel-surcharge false-claims) | search *verified*; opinions not read (§11) |
| Surface Transportation Board | No motor-carrier overcharge decisions stating amounts against spend were found; STB's published work in this area is rail demurrage and household-goods rates | not found |
| State / university freight audit contracts | The statutes exist (Texas Gov't Code ch. 2115; NC's programme naming "miscalculated freight charges"; Maine 5 M.R.S. §1622), but **no state publishes a freight-only result**. Texas's own AP recovery audit recovered $1.08M on $57.6B (0.002%) - already in check X | *verified* (statute pages, snippets) |
| Canada / UK public audits | Nothing found (§11) | not found |
| DoD / USTRANSCOM / DFAS post-2009 | DoD IG report D-2009-072 "Monitoring PowerTrack Payments for DoD Freight Transportation" exists but **every host blocked the download** (403 at media.defense.gov and dodig.mil, for both curl and the fetch tool). Same for DODIG-2013-083 | could not access |

### 3.4 Academic literature

An OpenAlex search of five phrasings ("freight bill audit", "freight audit and payment", "freight overcharge claims", "freight invoice errors", "transportation invoice audit") returned **no empirical study of private-sector freight overcharge rates**. The only on-topic items:
- **Miller & Brooks (1980)**, the USDA report in §3.1 (N-AB31).
- **Min, H. (2002), "Outsourcing Freight Bill Auditing and Payment Services", *International Journal of Logistics Research and Applications*** (N-AB32): a questionnaire survey of potential 3PL users about the *market* for outsourced auditing. The abstract contains no error or overcharge rate; the full text is paywalled.
- A 2012 book chapter titled "Freight Bill Auditing" (Wiley) - not read.

The widely quoted "15% per the Journal of Business Logistics" and "10% per NASSTRAC" appeared again in this sweep (N-AB52) with no traceable original, confirming check X §2.3.

### 3.5 Carrier-side filings: what carriers themselves book as post-billing corrections

This is the mirror image of a shipper recovery: money the carrier billed and later gave back.

| Carrier | Disclosure | Figures | **Ratio [our calc]** | Label |
|---|---|---|---|---|
| **FedEx Freight** (largest US LTL carrier), 10-K FY2026, filed 2026-08-05 (N-AB37) | Separate "allowance for revenue adjustments". Table: FY2026 beginning $2M, repurchases of previously factored receivables $63M, current-period provision **$101M**, write-offs $(102)M, ending $64M. Plus: "Excluded from the table above are adjustments to revenue recognized prior to the termination of the factoring agreement. These revenue adjustments were **$83 million in 2026, $111 million in 2025, and $235 million in 2024**." Provisions inside the table were $8M (FY2025) and $11M (FY2024) | Revenue $8,795M (FY2026), $8,892M (FY2025), $9,424M (FY2024) | Total revenue adjustments **$184M = 2.09%** (FY2026), **$119M = 1.34%** (FY2025), **$246M = 2.61%** (FY2024) of revenue | *verified* (XBRL pages via fetch tool); ratios **[our calc]** |
| Same, for contrast | Check T already records FedEx Freight's own estimate that dimensioners **added** "over $150 million … over fiscal years 2024 and 2025", about **0.8% of revenue** (N-T36) | - | Carriers add ~0.8% by re-measuring and give back 1.3-2.6% for all reasons | *verified* there |
| **Old Dominion Freight Line**, 10-K FY2025 (N-AB38) | "We also maintain an allowance for estimated revenue adjustments resulting from future billing corrections, customer allowances, money-back service guarantees and other miscellaneous revenue adjustments." Customer-receivable allowances $7,924k (2025) and $9,272k (2024); of which uncollectible-account allowance $6,596k and $6,375k | Gross customer receivables $479.9M (2025), $510.8M (2024); revenue $5,496M / $5,815M | Revenue-adjustment allowance ≈ **$1.33M = 0.28%** of gross receivables (2025) and **$2.90M = 0.57%** (2024); **0.02-0.05% of annual revenue** | *verified*; split and ratios **[our calc]** |
| **ArcBest**, 10-K FY2025 (N-AB39) | "Revenue adjustments occur due to freight bill rating or other billing adjustments." "The allowance for revenue adjustments is an estimate based on historical revenue adjustments and current information regarding trends and business changes." Schedule II, "Allowance for credit losses and revenue adjustments": 2025 beginning $8.257M, charged to costs $3.282M, charged to other accounts $2.223M, deductions $5.999M, ending $7.763M (2024: $1.693M charged to other accounts; 2023: $3.512M) | - | The reserve is small; ArcBest does not split billing corrections from credit losses | *verified* |

**What this does and does not show [our call]:** FedEx Freight's line is the only public, carrier-side, LTL-specific measure of post-billing give-backs, and it is **all causes combined** (volume incentives, guaranteed-service refunds, billing corrections). It therefore **caps** what LTL shippers as a group get credited at roughly 1-2.6% of carrier revenue, and it is *not* evidence that 1-2.6% of bills are wrong. The reserve-based numbers at ODFL and ArcBest measure only what is expected on receivables still open, so they are much smaller and are not comparable.

---

## 4. AB3 · Share credited when a private shipper (or its agent) disputes, and how long it takes

### 4.1 Evidence table

| Source | Setting | Share credited | Timing | Label |
|---|---|---|---|---|
| GSA OIG (N-X01, known) | Federal post-payment audit, with offset power and a 3-year window | **81% by value**; 45-96% by contractor | Uncollected rises from <10% (<400 days' lag) to ~35% (800+ days) | *verified* |
| USDA 1980 (N-AB31) | 34 cooperatives, 1977 | Not computable - claims filed and collected were reported by different subsets | - | *verified* that it is unusable |
| **ValueXPA specialty chemical case** (N-AB17) | In-segment, post-payment, 24-month look-back, three carriers | "Two of three carriers issued credits within **60 days** totalling $76K; the third negotiated a $19K credit plus a corrected go-forward formula. Total recovered: $95K" = **100% of found** | "$95K cash recovered within **75 days**" | *assumed* (vendor case) |
| Laneproof (N-X27, known) | Brokers disputing carrier bills | "65% to 80%" of disputed dollars is "healthy"; **74%** when filed within 5 business days, **41%** after 15+ days | target resolution "under 14 days" | *assumed* |
| Eller Audit (N-X26, known) | LTL categories | class 70-82%, fuel cap 85-92%, accessorials 60-75%, minimum charge 75-88% | "60-90 day claims window" | *assumed* |
| ConData (N-AB25) | Post-audit book | $328M+ "recovered" against $645M+ "errors identified" = **51%** if the bases match (labels inconsistent across pages) | - | *assumed*, weak |
| TransImpact (N-AB27) | **Parcel** refund claims for a global auto-parts distributor | "**95% refund-claim success rate on eligible packages**"; the previous auditor's bad claims drew "notices for false refund requests" from carriers | continuous | *assumed* |
| Search summary, source not located (N-AB47) | post- vs pre-audit | "60-80% versus nearly 100% for pre-audit catches" | - | *assumed* |
| CorePiper, "2026 State of Freight Claims" (N-AB42) | **Loss-and-damage** claims (not overcharges), mid-market shippers | LTL denial rate "50-60%", FTL "20-35%", parcel "30-45%"; "recovery rate (manual process) 35-45%"; "~30% of filed claims are abandoned before final payout … when the carrier slow-walks the process past the 60-day mark" | "average freight claim under manual processing takes 47 days"; LTL 60-90 days | *assumed* (vendor, no method published) |
| Intelligent Audit (N-AB07) | L&D claims programme | "First refunds received within 30 days" | 4 months to $785K | *assumed* |
| **ATRI**, "New Research Documents Substantial Financial and Safety Impacts from Truck Driver Detention", 2024-09-10 (N-AB41) | The mirror direction: **TL carriers billing shippers** for detention, 2023 driver and fleet survey | "While **94.5 percent of fleets charge detention fees, they are paid for fewer than 50 percent of those invoices**" | - | *verified* |
| Triumph Financial 10-K, via search summary (N-AB45) | Transportation factoring | "$249,288,000 and $254,970,000, respectively, of customer reserves associated with factored receivables which are held to settle any payment disputes or collection shortfalls" against about $1.0B of factored receivables | - | *assumed* (snippet). **No factoring "dilution" percentage for trucking was found** |
| 49 CFR Part 378 (check T, N-T05) | Motor-carrier overcharge, duplicate-payment and overcollection claims | Carrier must acknowledge in 30 days and "pay, decline to pay, or settle" within **60 days** | statutory | *verified* there |

### 4.2 What the law does to a look-back product

- **The 180-day rule bites hard.** 49 U.S.C. 13710(a)(3)(B) requires a shipper to contest charges within 180 days of receiving the bill. In *Southern Furniture* the 10th Circuit applied it to a court action over a concealed, decade-long reweigh scheme and affirmed dismissal: "compliance with the 180-day time limit is not optional" (N-AB35, *verified*). A private look-back that reaches back 12-24 months is therefore, for LTL bills not contested in time, **asking for a credit the carrier can simply refuse** - unless a contract under 49 U.S.C. 14101(b) sets different terms (check X §4.2).
- **A crude structural consequence [our calc, our call]:** on a 12-month look-back of evenly spread bills, only the most recent 6 months - about **half the dollars** - are still inside the 180-day window on day one of the audit; on a 24-month look-back, about a quarter. The model in check X does not separate this.
- **No offset.** Unlike GSA (31 U.S.C. 3726(d), 3 years), a private shipper can only offset against a carrier it still uses, and only if the contract allows.
- **A contingency auditor filing as agent** is allowed by Part 378 and by carrier tariffs (check T), so agency is not the obstacle; timing is.

### 4.3 TL vs LTL, direct carrier vs broker

| Distinction | What the evidence says | Label |
|---|---|---|
| **LTL, direct** | Corrections are carrier-initiated (reweigh, reclass, dimensioner) and land days to weeks after delivery; disputes run through tariff claim rules plus Part 378; the 180-day rule applies; FedEx Freight's give-backs are 1.3-2.6% of revenue | *verified* (check T, N-AB37, N-AB35) |
| **TL, direct** | Disputes are mostly accessorial (detention, layover, stop-offs) and run the *other* way: ATRI shows shippers pay fewer than half of detention invoices. Truckload rate errors are rarer per bill but larger | *verified* (N-AB41) |
| **Broker-billed (either mode)** | The counterparty is the broker, not the carrier: 19 of 21 public wrong-bill anecdotes were broker bills (check Z §3). Broker-side data (Laneproof) shows 65-80% of disputed dollars recovered when filed fast, 41% when filed late. Whether 13710/Part 378 reach a broker's invoice was **not** checked here | *assumed*; the statutory question is open |

### 4.4 Reading **[our call]**

1. **Speed dominates.** Every dataset in §4.1, neutral or vendor, shows the credited share falling with age: 74%→41% (broker, 5 vs 15 days), <10%→35% uncollected (GSA, 400 vs 800 days), and the legal cliff at 180 days for LTL.
2. **A pure look-back is the weakest version of this product.** It collects on the oldest dollars, which are exactly the ones carriers can refuse. Anything that moves toward monthly or pre-payment raises the credited share toward 90-100% - but then there is no "recovery" to take a share of, which is check X's fee-basis problem.
3. **The one in-segment case recovered 100%** of what it found, in 75 days, from three carriers, on *formula* errors (fuel index, hazmat compounding, minimum charge) with documentary proof. Error types that are arithmetic against a contract seem to be credited; judgement calls (class, reweigh, accessorial justification) are the ones vendors report at 60-82%.

---

## 5. AB4 · Recurrence: what happens after the first audit

| Evidence | Figure | Label |
|---|---|---|
| Fortigo, *IL* 2023 (N-AB09) | "First-year savings for customers switching from manual processes … can range from **7 to 12%**. Established customers typically see annual savings ranging from about **1 to 5%**" | *assumed* |
| Fortigo, *IL* 2022 (N-AB10) | first year "7 to 10%", established "1 to 4%" | *assumed* |
| Fortigo, *IL* 2019 (N-AB11) | "On a new freight bill audit deployment, companies often save between **5% and 15%** … On an ongoing basis … between **1% and 1.5%**" | *assumed* |
| A3 Freight Payment, *IL* 2023 (N-AB09) | "ongoing savings on the audit itself generally are around **one-half of 1%**. The reason it's generally not higher? The audit provider should be correcting errors, so more transactions proceed accurately and savings from mistakes decline over time" | *assumed* |
| CT Logistics, *IL* 2022 (N-AB10) | blended gross savings "**about 3.2%**"; "a new shipper client who has never engaged an outsourced FBAP provider usually saves more in its first few years" | *assumed* |
| Loop, mid-market process manufacturer (N-AB16) | After nine months: "Linehaul-related overcharges by **63.2%**", fuel discrepancies −23.3%, accessorial overcharges −13.5% | *assumed*, read in full |
| Loop, Great Dane (N-AB15) | invoices with errors **7.8% → 3.6%** | *assumed* |
| Intelligent Audit, LTL distributor (N-AB05) | "**35% decrease** in reclass-related disputes" after class standardisation | *assumed* |
| ValueXPA chemical case (N-AB17) | The fix is preventive - corrected formulas, quarterly re-validation - worth "0.6 points of recurring gross margin", i.e. the *recurring* value is prevention, not repeat recoveries | *assumed* |
| ConData (N-AB25) | "50% of our revenue comes from clients who already have FAP providers"; a second-level audit lives on "the remaining 2%" | *assumed* |
| Trans Audit (N-AB08) | Its whole business is the residue after FAP and internal audits: 0.5-1.5% non-parcel | *assumed* |
| USDA 1980 (N-AB31) | **44%** of auditors told the cooperative where and what the errors were, **40% did not**, "so as to cause concern that the same errors would continue"; retention: 20 of 45 auditor relationships were 5 years or less, only 4 above 10 years | *verified* |
| AFS national fashion retailer (N-AB26) | "For the last decade, the retailer has relied on AFS Parcel Audit" - long retention on the parcel side | *assumed* |
| PRG via GAO (N-X04, known) | 0.48% for a new client → "about 0.1 percent" once corrective measures are in (−79%) | GAO *verified*; rate is PRG's |

**Reading [our call]:** the consistent shape across an AP recovery auditor (−79%), three freight providers (first year 5-15% → ongoing 0.5-5%) and two AI-audit deployments (−63% of linehaul overcharges; error-carrying invoices halved) is a **year-2 fall of roughly 50-80%**, not the 40% used in check X §8. The counter-argument in check X - that carrier-side errors regenerate on every shipment - is supported by nothing found here, and the one in-segment case shows the opposite: the errors were *formula* faults that stopped once fixed.

---

## 6. AB5 · Parcel comparison (kept separate; do not mix into the model)

| Case / statement | Spend base | Amount | Rate | Label |
|---|---|---|---|---|
| National fashion retailer (AFS), 2022 page (N-AB26) | "Over 90% of its **$24 million** annual parcel spend goes through a single carrier" | "saved nearly **$800,000** on its parcel spend over a 12-month period"; "**$184,000** in refunds … in just one week" | **3.33%** **[our calc]** | *assumed* |
| B2B industrial distributor, $1.3B revenue (TransImpact) (N-AB27) | "**$29.3 million** in annual parcel spend" | "saved us in excess of **$150,000** in terms of cost reduction and increased freight revenue recovery" over a year | **0.51%** **[our calc]** | *assumed* |
| Global auto-parts distributor (TransImpact) (N-AB27) | not stated | "**95% refund-claim success rate on eligible packages**"; "5% reduction in total parcel spend" | - | *assumed* |
| Online furniture retailer (Intelligent Audit) (N-AB06) | ">$1 billion in transportation spend", 70M packages | "Two months in: **$135K** in recoverable billing errors identified" (North America parcel only) | denominator does not match the audited scope | *assumed* |
| ICC Logistics (N-AB23) | "a spend of several million dollars a year" | prior auditor averaged **$200 a month**; ICC found "well over $10,000" in the first month | shows how much auditor choice moves the number | *assumed* |
| ICC Logistics (N-AB23) | not stated | "$121,000 for just 5 months of service" after a new FedEx contract was mis-implemented (including a wrongly flagged late-delivery-refund waiver) | - | *assumed* |
| Cass (N-AB30) | not stated | "$140,000 on late fees in a 14-month period … the client asked for and received a refund"; "5% audit findings" on intra-European parcel | - | *assumed* |
| Contract-negotiation "savings" for contrast (TransImpact) (N-AB27) | $8M / $3.3M / $16M parcel spends | $1.9M / 22% / $3.1M | 22-24% - **all sourcing, not recovery** | *assumed* |
| Earlier notes (N-J28, N-N30) | - | FedEx reinstated money-back guarantees on listed express services from 2026-02-12, "all other FedEx® services will remain suspended"; UPS restored only air/international express | The late-delivery refund pool that drives parcel audit yields **does not exist for ground today** | *verified* / *assumed* |

**Why parcel does not transfer [our call]:** parcel yields come substantially from service-failure refunds and published-surcharge mismatches, both machine-checkable against one carrier's rules; TL/LTL has no service guarantee, fewer carriers per shipper, and a contract that has to be read. The two parcel rates here (0.51% and 3.33%) bracket the freight ones, which is itself a reason not to argue "parcel proves 5%".

---

## 7. Updated rate sets suggested for the model **[our call]**

Compare with check X §10.1 (overcharge 0.5 / 1.5 / 3%; caught 50 / 70 / 85%; credited 60 / 80 / 90%). Nothing here justifies raising the central case; two structural changes are suggested.

### 7.1 Overcharge rate (share of TL+LTL spend billed wrong in the carrier's favour, before catching anything)

| Set | Suggested | One-sentence support |
|---|---|---|
| Low | **0.5%** (unchanged) | The neutral cluster: USDA cooperatives *collected* 0.45% of regulated transport cost (N-AB31); a second-level post-audit specialist's whole book is 0.5-1.5% of non-parcel spend (N-AB08); an audit provider's ongoing yield is "one-half of 1%" (N-AB09); a 40-year practitioner puts historic truck error rates at 1% (N-AB34). |
| Central | **1.5%** (unchanged) | The six published cases recover or identify a median **1.80% of spend** (N-AB01, N-AB02, N-AB08, N-AB15, N-AB17, N-Z04) - but those are *post-catch, post-credit* results in selected best cases at large shippers, so the gross rate for a typical unaudited mid-sized shipper is not higher than the middle of the desk range. |
| High | **3.0%** (unchanged; 4% is defensible for a badly controlled account) | The only plausibly in-segment case recovered **4.2% of a 24-month spend** from three formula faults (N-AB17), and FedEx Freight's own all-cause give-backs reach 2.6% of revenue (N-AB37). |
| **New: year-2 decay** | **−50% central (−30% low, −80% high)**, replacing check X's flat −40% | Fortigo 7-12%→1-5%; 5-15%→1-1.5%; A3 "one-half of 1%" ongoing; Loop −63% of linehaul overcharges in nine months; Great Dane 7.8%→3.6% of invoices; PRG −79% on general AP (§5). |

### 7.2 Share carriers credit

| Set | Suggested | One-sentence support |
|---|---|---|
| Low | **50%** (was 60%) | Broker-side disputes filed late recover **41%** (N-X27); GSA's weakest contractor collected 45-66% (N-X01); ConData's own pages imply 51% of identified dollars recovered (N-AB25); L&D claims under manual processing recover 35-45% and ~30% are abandoned (N-AB42). |
| Central | **75%** (was 80%) | GSA's 81% came with statutory offset and a 3-year window that a private shipper does not have (N-X01); healthy broker-side recovery is 65-80% (N-X27); LTL categories run 60-92% (N-X26). |
| High | **90%** (unchanged) | Vendor category rates reach 85-92% (N-X26); parcel refund claims succeed on 95% of eligible packages (N-AB27); the one in-segment case was credited 100% within 75 days on formula errors (N-AB17); a pre-payment short-pay is credited by construction (N-AB15). |
| **New: time-bar factor on a look-back** | Multiply backlog recoveries by the share of bills still inside the claim window: **~0.5 for a 12-month look-back, ~0.25 for 24 months** (LTL, no contract waiver) **[our calc]** | 49 U.S.C. 13710(a)(3)(B) plus *Southern Furniture* (N-AB35): outside 180 days the carrier may simply refuse, and a court will not help. |

### 7.3 Two model-structure suggestions **[our call]**

1. **Split the backlog line by age**, not by a single multiple: dollars inside 180 days at the credited central rate, dollars outside it at the low rate or zero for LTL.
2. **Price the fee against a benchmark that exists**: a full FAP programme at a $65-77M shipper appears to cost **0.22-0.33% of spend** (§2.1, derived from published ROI). A 25% contingency share of central recoveries (0.84% of spend in check X) equals 0.21% of spend - the same order. That is a check on whether a contingency share is really "free money" from the buyer's side.

---

## 8. What the web could not settle

Only a savings assessment on a real shipper's invoices, or the interviews, can answer these:

1. **The overcharge rate on a 20-499-staff shipper's own TL and LTL bills.** One case (N-AB17) is the entire in-segment public record, and it is a vendor's.
2. **Found vs credited on those same bills**, by error type, with dates: how much of what an audit flags a carrier actually credits when the shipper is small, has no offset, and may buy TL through brokers.
3. **How much of a look-back is already time-barred** - i.e. what share of a real shipper's 12-24 months of bills is inside 180 days, and whether their contracts or rate confirmations change the window (49 U.S.C. 14101(b)).
4. **Whether broker-billed loads are covered by 13710/Part 378 at all**, which decides who the claim goes to and under which clock.
5. **Days from claim to credit**, per carrier, for a mid-sized shipper with no leverage.
6. **Year-2 behaviour on real accounts**: whether errors regenerate (carrier-side causes) or stop (formula fixes). Both stories are in the evidence; nothing tests them.
7. **Whether an in-segment shipper's own AP already catches part of this** before any auditor sees it.
8. **Factoring/ABL dilution for trucking receivables** - the carrier-side mirror - is not published anywhere found.
9. **What carriers do when they refuse**: deny, go silent, or re-bill (check X's H09-C4 remains untested).

---

## 9. For the coordinator (not a call)

1. **The public record is far thinner than the vendor noise suggests.** After about 50 web searches and ~120 page fetches across roughly 20 vendor case libraries, **six** freight cases state both a spend base and an overcharge amount. Their median implied rate is **1.80% of spend**, and they are the auditors' own best cases at shippers 10-100× bigger than C-09's target. Nothing found contradicts check X's reading that H09-02's upper half is unsupported.
2. **The single in-segment case is the strongest thing found for C-09 - and also the weakest evidence.** A $22M-revenue family-owned chemical manufacturer recovered $95K (≈4.2% of a 24-month spend, 100% of what was found, inside 75 days) from three formula faults: a fuel index the carrier had quietly swapped, a hazmat surcharge compounding on a surcharge, and a minimum charge raised without an amendment. It is a vendor write-up that reads as templated, but it describes exactly the failure mode C-09 is betting on: **nobody re-derives the formula, only the arithmetic**.
3. **The 180-day rule is a bigger constraint on a look-back than the cost to serve.** The 10th Circuit dismissed a class action over a concealed decade-long LTL reweigh scheme because the shipper had not contested within 180 days: "compliance with the 180-day time limit is not optional." An audit-only look-back sells the shipper the oldest, least collectable dollars. Suggest modelling the backlog in two age buckets (§7.3).
4. **Every provider that separates first year from later years reports a 50-85% fall.** Check X's −40% year-2 assumption looks generous, and a "fix it and it stops" pattern (Loop −63% of linehaul overcharges; Great Dane 7.8%→3.6% of invoices) argues the recurring line is thinner than the first year, which matters for anything sold as annuity revenue.
5. **Savings ≠ recovery, and vendors bank on the confusion.** Sourcing and network projects deliver 4.5-21% of spend in the same case libraries where overcharge recovery delivers 0.8-4.2%. Any interview answer of the form "our auditor saves us 5%" must be broken into recovery vs renegotiation before it is used.
6. **The carrier's own books cap the pool.** FedEx Freight - the biggest LTL carrier - gives back 1.3-2.6% of revenue in *all* post-billing revenue adjustments combined, while adding about 0.8% through dimensioners. Whatever the true overcharge rate is, the money LTL customers actually get credited sits inside that 1-2.6% band at the industry level.
7. **The share carriers credit should come down slightly in the model** (low 60%→50%, central 80%→75%): GSA's 81% rested on statutory offset and a 3-year window that no private shipper has, and the private analogues (broker disputes 41-80%, L&D 35-45%, ConData's implied 51%) sit lower.
8. **Two questions the desk cannot touch again**: DoD's post-2009 freight payment audit results (every host blocks the reports) and any factoring dilution rate for trucking. If either matters to the decision, they need a different route than the open web.

---

## 10. Sources

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-AB01 | Intelligent Audit case study, "Multi-Brand Manufacturer Achieves 1,071% ROI Across a $77M Freight Network" | undated | https://www.intelligentaudit.com/case-studies/multi-brand-manufacturer-achieves-1071-roi-across-a-77m-freight-network | full (page text) | $77M spend, 330,896 shipments, 199+ carriers, >$2M identified and recovered, ROI |
| N-AB02 | Intelligent Audit, "How a High-Volume North American Manufacturer Unlocked $1.9M in Freight Savings and 897% ROI" | undated | https://www.intelligentaudit.com/case-studies/how-a-high-volume-north-american-manufacturer-unlocked-1-9m-in-freight-savings-and-897-roi | full | $65M spend, 114,000 invoices, 100+ carriers, $1.9M, ROI |
| N-AB03 | Intelligent Audit, "Large Global Manufacturer Achieves $15.4M in Annualized Savings and an ROI of 1,906%" | undated | https://www.intelligentaudit.com/case-studies/large-global-manufacturer-achieves-15-4m-in-annualized-savings-and-an-roi-of-1-906 | full | $10.4M audit & recovery ($9.2M freight), optimisation and anomaly splits |
| N-AB04 | Intelligent Audit, "From Limited Insight and Control to $1.9M in Savings" | undated | https://www.intelligentaudit.com/case-studies/from-limited-insight-and-control-to-1-9m-in-savings | extraction (fetch tool) | ~120,000 invoices, TL/LTL, $1.9M recoveries and prevented overcharges |
| N-AB05 | Intelligent Audit, "Reducing LTL Spend Through Freight Class Accuracy and Audit Controls" | undated | https://www.intelligentaudit.com/case-studies/reducing-ltl-spend-through-freight-class-accuracy-and-audit-controls | full | 13.2% LTL spend reduction; 35% fewer reclass disputes |
| N-AB06 | Intelligent Audit, "From Limited Scope to Expanding Enterprise Partnership" | undated | https://www.intelligentaudit.com/case-studies/from-limited-scope-to-expanding-enterprise-partnership | full | >$1B spend, 70M packages, $135K identified in two months, $20M+ ROI value |
| N-AB07 | Intelligent Audit case-studies index and three further cases (anomaly detection $220K; L&D $785K in 4 months; $3M/week healthcare) | undated | https://www.intelligentaudit.com/case-studies | full (index) + 3 pages | titles, headline figures, claim timings |
| N-AB08 | *Inbound Logistics*, "Beyond Table Stakes: Freight Payment Clients Hold All the Cards" | 2018-10-08 | https://www.inboundlogistics.com/articles/beyond-table-stakes-freight-payment-clients-hold-all-the-cards/ | full | US Bank equipment manufacturer ($100M+, $800k audit + $2.7M duplicates); Trans Audit 0.5-1.5% and look-back windows; CTSI 3-5%; nVision 5-9% + 1-2%; RateLinx $100M client; DDC FPO error rates |
| N-AB09 | *Inbound Logistics*, "Beyond the Freight Bill Audit" | 2023-09-14 | https://www.inboundlogistics.com/articles/beyond-the-freight-bill-audit/ | full | A3 "one-half of 1%" ongoing and 5-20% spend-management savings; Fortigo 7-12% vs 1-5%; AFS "up to 8%" and the $500k FBAP threshold; CT 3-7% |
| N-AB10 | *Inbound Logistics*, "Freight Bill Audit & Payment: Savings in the Bag" | 2022-09-21 | https://www.inboundlogistics.com/articles/freight-bill-audit-payment-savings-in-the-bag/ | full | CT FreitRater 3.2% blended; Fortigo 7-10% vs 1-4%; A3 6%; IA 2-20% (most 5%), $31B audited; AFS Rexel $238k; US Bank $800M onboarded |
| N-AB11 | *Inbound Logistics*, "Freight Bill Audit & Payment: It's More Than The Money" | 2019-10-08 | https://www.inboundlogistics.com/articles/freight-bill-audit-and-payment-its-more-than-the-money/ | full | Cass 1-5%; Data2Logistics "5% to 15%"; Fortigo 5-15% new vs 1-1.5% ongoing; enVista coffee retailer $420k; IA 12-18%; AR Traffic accessorials 2-6% |
| N-AB12 | *Inbound Logistics*, "Mining Data Insights" | 2020-10-06 | https://www.inboundlogistics.com/articles/mining-data-insights/ | full | CT Logistics $500k client floor; enVista ~5%; nVision 9-12%; Sunset's critique of savings-share pricing; US Bank "up to 4%" on pre-payment |
| N-AB13 | *Inbound Logistics*, "Freight Payment and Auditing Services: Cash is King" | 2015-09-03 | https://www.inboundlogistics.com/articles/freight-payment-and-auditing-services-cash-is-king/ | full | duplicates 0.5-1.5% of transport spend; pre-audit 1-5%; 2-4% monthly; $4-10 per invoice |
| N-AB14 | *Inbound Logistics*, "Freight Payment and Auditing Services: Finding the Hidden Gold" | 2011-09-15 | https://www.inboundlogistics.com/articles/freight-payment-and-auditing-services-finding-the-hidden-gold/ | full | "two to four percent error rate" on manual entry, 10% international; 1.5-5% typical savings |
| N-AB15 | Loop, customer story, "Great Dane approves 98% of invoices with no touch on Loop" | undated | https://www.loop.com/customer-story/great-dane | extraction (fetch tool; page is JS-rendered) | $8.5M audited, $73,725 identified and payment stopped (2023), 7.8%→3.6% invoices with errors |
| N-AB16 | Loop, "Mid-Market Process Manufacturer finds 6% savings with Loop" | undated (engagement from early 2023) | https://www.loop.com/customer-story/mid-market-process-manufacturer-finds-6-savings-with-loop | extraction (fetch tool) | $10,000 overcharges in nine months; −63.2% linehaul, −23.3% fuel, −13.5% accessorial; $15k reweigh exposure; LTL/FTL; five carriers |
| N-AB17 | ValueXPA case study, "$22M Specialty Chemical Manufacturer Recovers $95K from Stale Freight Surcharge Formulas" | published 2026-04-28, updated 2026-05-12 | https://valuexpa.com/case-studies/us-specialty-chemical-manufacturer-freight-surcharge-recovery | full | revenue, freight % of revenue, 24-month scope, $58k/$24k/$13k findings, credits within 60 days, $95k in 75 days |
| N-AB18 | ValueXPA insights page (case list, incl. $42M hose distributor) | 2026 | https://valuexpa.com/insights/freight-billing-audit-3pl-manufacturers-teaxs | full | case titles and revenue anchors |
| N-AB19 | FreightOptics case study, global fine-art dealer | undated | https://www.freightoptics.com/case-studies/how-a-global-fine-art-dealer-uncovered-137k-in-overcharges-and-secured-3-5m-in-annual-freight-savings/ | full | $400M revenue; $37,714 fuel surcharge recovered in 1.5 months; ~$100k rate misalignment; $3.5M sourcing savings |
| N-AB20 | FreightOptics case study, industrial manufacturer | undated (bid concluded 2025) | https://www.freightoptics.com/case-studies/how-a-leading-industrial-manufacturer-transformed-its-supply-chain-unlocking-significant-savings-and-operational-excellence/ | full | $500M revenue; $25k/month LTL saving = 16.5%; $18k/month insurance; Epicor ERP integration |
| N-AB21 | FreightOptics case-studies index | undated | https://www.freightoptics.com/case-studies/ | full | case titles and headline figures (incl. parcel) |
| N-AB22 | ICC Logistics, "LTL & Truckload Audit Services, International Freight Audits" | undated | https://icclogistics.com/services/freight-audit/ltl-truckload-international/ | extraction (fetch tool) | four freight cases: $475k/6 months, $210k, $96k, $78k |
| N-AB23 | ICC Logistics, case-studies page | published 2023-01-24, updated 2026-08-24 | https://icclogistics.com/resources/case-studies/ | full | $121k over 5 months (FedEx contract audit); UPS auditor switch $200/month → >$10k in month 1; $100k annual recoveries; $14M global spend example |
| N-AB24 | ConData, case-studies index | undated | https://www.condata.com/case-studies | extraction (fetch tool) | seven post-audit cases with amounts ($2.2M, $425k, $2M+, $1.7M, $1.7M, $70k, $25M) |
| N-AB25 | ConData, home page and "Freight Post Audit" page | undated | https://www.condata.com/ ; https://www.condata.com/freight-post-audit | full | "$645M+ errors identified", "$50B+ freight spend processed annually", "$328M+ recovered", "98% accuracy … the remaining 2%", "50% of our revenue … already have FAP providers", contingency pricing |
| N-AB26 | AFS Logistics case studies: national fashion retailer (parcel), Rexel, fastener/hardware distributor, Musco, Feintool, Hatco, Mann Lake | pages dated 2022-05, updated 2025-10 | https://afs.net/case-studies/ and 8 case pages | full | $24M parcel spend/$800k/$184k week; Rexel $238k claims + $1.17M parcel; 14%, >10%, 33%, 22%/7% savings claims |
| N-AB27 | TransImpact case studies (11 pages read): freight-audit auto parts; B2B shipper; automotive manufacturer; retail fixtures; shoes/eyeglasses; medical technology; golf; Evriholder; Filters Fast; Kawasaki; Coastal Pet | undated | https://transimpact.com/case-studies/ | full | 95% refund-claim success; $29.3M/$150k; $8M/$1.9M; $3.3M/22%; $16M/$3.1M |
| N-AB28 | CT Logistics, "Success Stories" | undated | https://www.ctlogistics.com/advantages/success-stories | full | medical device 15% duplicate/error reduction; apparel $1.5M overpayments and $750k; manufacturer 12%/30%; industrial supply 200,000 LTL shipments, $40M, 6% |
| N-AB29 | Data2Logistics, archived case studies (snapshot 2007-02-05, page marked "Copyright 2003") and archived "Professional Services - case studies" (snapshot 2019-02-02) | 2003 / 2019 | https://web.archive.org/web/20070205220310id_/http://www.data2logistics.com/AboutUs/CaseStudies/case1.html (and case2-4); https://web.archive.org/web/20190202170630id_/http://data2logistics.com/global-services/professional-services/case-studies.aspx | full (archived text) | >$500k express recovery in <1 year; $1.7M/$2M/$250k mixed-savings cases; "average recovery rate is 5% - 15%"; RFP savings 10-33% incl. LTL 21%/19% and FTL 15% |
| N-AB30 | Cass Information Systems, parcel success stories; Toyota case study; customers page | undated | https://cassinfo.com/freight-resources/case-studies/parcel-audit-and-management ; .../toyota ; https://www.cassinfo.com/freight-audit-payment/customers | full | $140k late fees refunded; $110k inactive accounts; $60k misused account; "5% audit findings" intra-Europe; Toyota (no dollar figures) |
| N-AB31 | USDA, Economics, Statistics and Cooperatives Service, ESCS-87, **"Cooperative Freight Bill Auditing"**, Miller & Brooks | 1980 (1977 survey data) | https://archive.org/download/cooperativefreig87mill/cooperativefreig87mill_djvu.txt (AgEcon record 143693) | full (archived OCR text) | Table 7 (34 cooperatives, $486.4M, $2,193,447, 0.45%); fee structure "usually 50 percent"; audit coverage; auditor tenure; error reporting |
| N-AB32 | Hokey Min, "Outsourcing Freight Bill Auditing and Payment Services", *International Journal of Logistics Research and Applications* (abstract via OpenAlex) | 2002 | https://doi.org/10.1080/13675560210148687 | abstract only (full text paywalled) | survey of potential 3PL users; no error or overcharge rate |
| N-AB33 | FreightWaves / American Shipper, "New freight benchmark study brings shippers' payment practices into the light" (on the JOC study "Driving Strategic Value Through Outsourcing") | 2020-10-05 | https://www.freightwaves.com/news/new-freight-benchmark-study-brings-shippers-payment-practices-into-the-light | full | 77 shippers, ~75% above $1B revenue; 20.8% average invoice inaccuracy; 21.9% use bank-backed vendors; payment terms |
| N-AB34 | *Logistics Management*, "Freight Payment: What stage are you in?" | 2022-01-05 | https://www.logisticsmgmt.com/article/freight_payment_what_stage_are_you_in | full | "historic error rates have been 1% for truck and rail and up to 10% for ocean"; post-audit firms charge a percent of recovered funds |
| N-AB35 | **Southern Furniture Leasing, Inc. v. YRC Inc.**, 10th Cir. No. 19-3262 | 2021-03-03 | https://storage.courtlistener.com/pdf/2021/03/03/southern_furniture_leasing_v._yrc.pdf | full (PDF text) | negative-reweigh scheme from Sept 2005; DOJ qui tam unsealed Dec 2018; 180-day rule "not optional"; treatment of *Grupp* and *Grocery Haulers*; CAFA $5M allegation |
| N-AB36 | CourtListener search API (four queries: "freight audit"; "freight bill audit"/"freight auditing"; reweigh+overcharges+LTL; 13710+180 days) | accessed 2026-09-17 | https://www.courtlistener.com/api/rest/v4/search/?type=o&q=… | full (JSON) | case lists, dates, courts, snippets; undercharge-era dominance |
| N-AB37 | **FedEx Freight Holding Company, Inc., Form 10-K FY2026** (accounting policies R9, allowance detail R38, income statement R5) | filed 2026-08-05 (FY ended 2026-05-31) | https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/R9.htm (R38, R5) | extraction of XBRL report pages (fetch tool) | allowance for revenue adjustments table; "$83 million in 2026, $111 million in 2025, and $235 million in 2024"; revenues $8,795M/$8,892M/$9,424M |
| N-AB38 | **Old Dominion Freight Line, Form 10-K FY2025** (R2 balance sheet, R3 parentheticals, R4 income, R12 policies, R23 Schedule II) | filed 2026-02-24 | https://www.sec.gov/Archives/edgar/data/878927/000119312526067161/R3.htm (R2, R4, R12, R23) | extraction of XBRL report pages | allowances $7,924k/$9,272k; uncollectible allowance $6,596k/$6,375k; receivables $471.9M/$501.6M; revenue $5,496M/$5,815M; revenue-adjustment policy wording |
| N-AB39 | **ArcBest, Form 10-K FY2025** (R11 accounting policies, R24 Schedule II) | filed 2026-02-25 | https://www.sec.gov/Archives/edgar/data/894405/000110465926019699/R24.htm (R11) | extraction of XBRL report pages | "Revenue adjustments occur due to freight bill rating or other billing adjustments"; Schedule II amounts 2023-2025 |
| N-AB40 | SEC EDGAR full-text search (efts.sec.gov) queries: "revenue adjustments"+"less-than-truckload"; "allowance for revenue adjustments"; "freight audit"+"recoveries"; "freight overcharges" | accessed 2026-09-17 | https://efts.sec.gov/LATEST/search-index?q=… | extraction (fetch tool) | hit lists (ODFL, ArcBest, FedEx, Forward Air, Knight-Swift, Schneider, Universal; Elizabeth Arden, ExlService, Roadrunner, Cass); "freight overcharges" = 0 hits |
| N-AB41 | American Transportation Research Institute, "New Research Documents Substantial Financial and Safety Impacts from Truck Driver Detention" | 2024-09-10 | https://truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/ | full | detention in 39.3% of stops (2023); "94.5 percent of fleets charge detention fees, they are paid for fewer than 50 percent of those invoices" |
| N-AB42 | CorePiper, "The 2026 State of Freight Claims Report" | 2026-04-27 | https://corepiper.com/blog/state-of-freight-claims-2026/ | full; vendor, no method published | denial rates by mode; 47-day average resolution; ~30% of claims abandoned; manual recovery 35-45% |
| N-AB43 | Transportation Insight, "Freight Audit And Payment: Protecting Profit In Soft Rates" | 2025-09-17 | https://transportationinsight.com/resources/freight-audit-payment-protect-profit-soft-rates/ | full; vendor | 3-6% of invoices contain errors; 1-5% of spend recoverable |
| N-AB44 | Trax Technologies, "A Primer on Freight Audit Recovery" | 2026-07-20 | https://www.traxtech.com/blog/a-primer-on-freight-audit-recovery | full; vendor | "5 and 12 percent of total freight spend"; ">12 percent" without automation; $100M worked example |
| N-AB45 | Triumph Financial 10-K FY2022/FY2024 (via search summary only) | 2023-2025 | https://www.sec.gov/Archives/edgar/data/1539638/000162828025004879/tfin-20241231.htm | snippet (*assumed*) | customer reserves $249.3M/$255.0M on factored receivables; factored receivables ~$1.0B; no dilution rate |
| N-AB46 | Texas Comptroller, *Statewise*, "Recovery audit — A success story in two parts" | 2011 (Spring) | https://fmx.cpa.texas.gov/fm/statewise/archive/recovery_audit_11.php | full | $57.6B analysed / $1.08M recovered (AP); Medicaid: $12.79M identified and $12.55M recovered on $1.8B (98% of identified) |
| N-AB47 | Search summary asserting "recovery rates on post-audit claims typically run 60-80% versus nearly 100% for pre-audit catches" | 2026 | (origin page not located; candidates: amzprep.com, getclearlane.com - neither contained the sentence) | snippet only (*assumed*) | the 60-80% figure |
| N-AB48 | Search summary asserting a global manufacturer "recovered more than $7 million in the past two years with an 87% recovery rate" | 2026 | (origin not located on the Intelligent Audit pages checked) | snippet only (*assumed*) | an 87% share-credited claim that could not be verified |

**Earlier sources re-used:** N-X01, N-X02, N-X04 (check X: GSA OIG, GAO 1992, GAO 1999); N-X26, N-X27 (Eller Audit, Laneproof); N-Z04 (check Z: Reddit AI-audit firm, $120k on ~$12M); N-T05, N-T36 (check T: 49 CFR 378 timings; FedEx Freight dimensioner revenue); N-J28, N-N30 (checks J and N: FedEx and UPS money-back guarantee suspensions).

---

## 11. Could not access, or not found

| Target | What happened | Searches or routes tried |
|---|---|---|
| **DoD IG D-2009-072, "Monitoring PowerTrack Payments for DoD Freight Transportation"**, and DODIG-2013-083 | HTTP 403 from media.defense.gov and dodig.mil for both curl and the fetch tool | direct PDF, report landing page, oversight.gov, domain-limited search (gao.gov, dodig.mil, govinfo.gov, oversight.gov) |
| USTRANSCOM / DFAS Third Party Payment System audit results after 2009 | Only regulation text (DTR Part II, DoD FMR vol. 10 ch. 13) surfaced; no results | 2 searches |
| **SEC full documents** | sec.gov Archives returns 403 to any undeclared automated tool, and the rule forbids declaring a contact; the fetch tool truncates a 10-K before the financial statements. Worked around by reading the XBRL "R" report pages (N-AB37-N-AB39) | curl (403), fetch tool on main documents (truncated), FilingSummary.xml + R pages (worked) |
| Elizabeth Arden 10-K passages containing "freight audit" + "recoveries" (4 filings, FY2013-FY2016) | Hits confirmed by full-text search but the passage sits past the fetch tool's truncation point | EDGAR FTS (hits), fetch of FY2013 10-K (not reached) |
| EDGAR queries for factoring "dilution" and "short pay" | efts.sec.gov returned HTTP 500 twice | 2 queries |
| **CourtListener opinion texts** | Opinion pages return a bot challenge (HTTP 202, empty body) and the v4 clusters/opinions API needs a token. Only *Southern Furniture* had a free PDF mirror | curl, fetch tool, API |
| *nVision Global v. Cardinal Health* (2012), *Variety Wholesalers v. Salem Logistics* (2011), *Tenan v. StrategIQ* (2019), *Mastercraft v. ABF* (2004), *State v. DHL Express* (2010) | Identified but not read; the first is a per-transaction fee dispute, the second an FAP misappropriation case | CourtListener search + 1 web search |
| **Surface Transportation Board** decisions on motor-carrier overcharges | None found stating amounts against spend; STB's published material is rail demurrage and household-goods rates | 1 search |
| **Canadian or UK public-sector freight audits** | Nothing found | 1 search (Auditor General of Canada / NAO) |
| **Academic measurement of private overcharge rates** | None exists that could be found: OpenAlex across five phrasings returned one 1980 USDA report and one 2002 survey paper | OpenAlex API (5 queries), 2 web searches |
| **AgEcon Search PDF** of the USDA report | HTTP 403 (curl and fetch tool) | worked around via archive.org full text |
| **Reddit** | The search tool refuses reddit.com; reddit's JSON API returns 403 to this environment | 2 attempts |
| **Wayback CDX listings** for traxtech.com, tranzact.net, transportationinsight.com, usbank.com | HTTP 429 / "temporarily offline" | retried once; data2logistics.com and ctsi-global.com listings did work |
| enVista case studies; Green Mountain Technology case studies | 403 and connection failure | curl |
| Lojistic's "$14M parcel spend → $161,291 in eight months" | Quoted in a search summary but not present on the Lojistic FAQ page fetched; origin page not located, so excluded from the register | 1 search + 1 fetch |
| A source for "87% recovery rate" and "$7 million in the past two years" | Not found on any Intelligent Audit page checked | 1 targeted search + 3 fetches |
| Factoring or ABL **dilution rates for trucking receivables** | Only definitions and generic 5-10% ABL thresholds; nothing trucking-specific | 2 searches |
| **Carriers' own claim statistics** (how many overcharge claims they receive, allow or deny) | Nothing published by any carrier; the closest are the accounting lines in §3.5 | covered by 3 searches |
| A second in-segment case (US manufacturer or distributor, 20-499 staff, TL/LTL, spend and overcharges both stated) | Not found. About 20 vendor case libraries were opened (Cass, CTSI-Global, Trax, nVision, TranzAct, AFS, Transportation Insight, CT Logistics, RateLinx, ConData, ICC, Intelligent Audit, TransImpact, Loop, FreightOptics, Data2Logistics, Eller, Goodman-Reichwald-Dodge, Shipware, Green Mountain) | ~25 searches, ~120 fetches |
