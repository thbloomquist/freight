# S4 check AE: what retailer deductions and fines cost small suppliers, how much is recoverable, and what recovering it costs (C-19)

- **What this is:** input to S4 step 7 (C22, the per-customer profit model and kill condition) for **C-19, retailer on-time-in-full (OTIF) fines and deductions, for suppliers with sales of $500M or less selling to big-box retailers**, run 01. It answers AE1-AE7 from the brief and feeds this chain, which the coordinator builds (not this file):

  > fee per customer = supplier's sales to big-box retailers × **non-trade deductions as % of those sales** × **share invalid (disputable and provable)** × **share actually recovered** × fee share
  >
  > gross profit = fee − cost to serve (deductions handled × minutes each × loaded wage + portal and retailer setup + fixed cost per customer)

- **Date:** 2026-09-22. Everything new here was accessed on 2026-09-22.
- **Status:** input only. **It decides nothing.** No price, segment, score or kill condition is set here. Every reading is **[our call]** and sits in §9, "For the coordinator (not a call)".
- **Labels:**
  - *verified*: read at the source (SEC filing page, court filing, government table, company press release for "what the company says"). Where a filing was read through a page-extraction tool rather than downloaded in full, this is said ("page extraction").
  - *assumed*: a vendor claim (always, even on the vendor's own page), an association figure read second-hand, a search snippet, a secondary summary or transcript, a blocked page.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
  - **Vendor figures are kept apart from neutral ones.** Vendors that sell deduction recovery are competitors of this card; their numbers are good for how retailers behave and poor for how big the gap is.
- **New source IDs:** N-AE01 to N-AE60 (§10). Earlier IDs keep their meaning: N-N29 (CRF 2018 survey), N-N12 (Lifetime Brands, check N), N-U01, N-U03, N-U09, N-U13, N-U24, N-U27, N-U29, N-U31 to N-U33 (check U), N-S13 (Uber Freight 0.16%, check S), N-AA27, N-AA28, N-AA40 (offshore rates and the 70.0% wage share, check AA).
- **Not redone here:** retailer rules, windows and evidence rules (check U §2); the buyer count of 15,000-55,000 (check U §3); the CRF 2018 survey (N-N29) and the Carixa slides citing CRF 2021/2023 (N-U28, N-U29); SPS's 10-K counts and the Q4 2025 call (N-U01, N-U31); Walmart's 31,196 supplier records and $412.4B (N-U03); the Uber Freight 0.16% figure (N-S13, re-read at its original here as N-AE51).
- **Hard rule kept:** SEC EDGAR refuses downloads without a declared contact in the User-Agent (tested once, HTTP 403 "Undeclared Automated Tool"). No contact was supplied. Filings were read through the WebFetch tool (EDGAR's per-note "R" pages) or through a public annual-report mirror. No identity was sent anywhere.

**Words used here:**
- **Deduction:** money a retailer takes off what it pays the supplier, instead of paying the invoice in full. **Chargeback / fine / penalty:** a deduction the retailer raises as a charge (for example an OTIF fine), sometimes billed first and deducted later.
- **Trade deduction:** a deduction for an agreed promotion (co-op advertising, markdowns, rebates, slotting). **Out of scope for C-19.** **Non-trade deduction:** shortages, pricing errors, late/early delivery, ASN, label and routing fines, damage and returns claims. The C-19 product works on these.
- **OTIF (on-time in-full):** the retailer's measure of whether each order arrived in its delivery window and in the full quantity. Walmart fines 3% of the cost of the non-compliant cases; McKinsey describes it as "3 percent of the purchase price", i.e. the supplier's invoice value (N-AE49).
- **ASN (advance ship notice):** the electronic packing list sent before the truck. **POD (proof of delivery):** the signed delivery receipt. **COGS:** cost of goods sold; in retailer fine rules it means the retailer's cost, which is the supplier's selling price.
- **Invalid deduction:** one the supplier can show is wrong (the goods did arrive, on time, at the agreed price). **Recovered:** the retailer actually paid it back.
- **Variable consideration:** the accounting term for money a supplier expects to lose to customers' deductions, rebates and returns; it is taken off revenue.
- **Schedule II:** the table at the back of a 10-K that shows how an allowance (reserve) was topped up and used during the year.
- **Big-box retailers:** Walmart (with Sam's Club), Target, Home Depot, Lowe's, Costco, Kroger, Amazon 1P (Amazon buying as a retailer).
- **Loaded wage:** hourly wage divided by 0.70, because wages are 70.0% of private employers' compensation cost (N-AA40).

---

## 1. Summary inputs table

"Sales" means the supplier's sales to the retailer(s) concerned unless marked otherwise.

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Non-trade deductions, % of sales** | **0.20%**: a real distributor ledger (home video into Walmart/Sam's/Best Buy, 2011-15) shows "Shipping Variances" of $54,048 on $27.0M invoiced; separately, OTIF fines alone 0.16% of COGS at Walmart | **0.25-0.5%**: CRF 2018 median ("¼ - ½ % of sales", 203 firms) | **1-1.5%**: CRF 2021 "up to 1% of sales"; Amazon shortage claims "1 to 3 percent of invoiced value" | low ledger *verified* (court exhibit), 0.16% *assumed*; CRF 2018 *verified* (CRF flag); high *assumed* | N-AE14, N-S13/N-AE51, N-N29, N-U29, N-AE42 |
| **OTIF fines alone, % of sales to that retailer** | **0%** at or above the retailer's threshold | **0.16%** of COGS, Walmart, in Uber Freight's customer base (Feb 2024) | **0.45-0.9%** from the rules at 70-85% on-time [our calc]; McKinsey: margins "cut by a full a percentage point" if no improvement (2018) | 0.16% *assumed* (interested party via Forbes); rules **[our calc]**; McKinsey *verified* at source (a consultancy estimate) | N-AE51, N-AE49, §8 |
| All deductions incl. trade, % of net sales (ceiling, out of scope) | **1.2%**: Lifetime Brands' "anticipated customer deductions" added in 2025 ($7.8M on $647.9M) | **7.0-8.6%**: Crown Crafts' "allowance for customer deductions" charged (FY2024-26), all types incl. co-op, rebates, returns | 10-20% of revenue (HighRadius, enterprise, incl. trade) | filings *verified* (EDGAR R pages / full PDF); rates **[our calc]**; HighRadius *assumed* | N-AE02 to N-AE04, N-AE31 |
| **Share invalid** (disputable and provable) | **5%** | **6-10%** of all deduction dollars (CRF 2018 median); 15% by CRF's Benchmarking Report as quoted by a vendor ("about 85% of them are merited") | **30%+** (vendor ranges "10-40%", some to 60%) | CRF 2018 *verified* (CRF flag); the rest *assumed* | N-N29, N-U29, N-AE40, N-AE22, N-AE38 |
| **Share recovered, of invalid deductions disputed** | **40%** of disputed deductions "won back" (SPS, vendor) | **60%** of invalid dollars "ultimately recovered" (CRF 2018; CRF 2021 via Carixa) | **89-97%** win rates (STAT, vendor) | CRF 2018 *verified* (CRF flag); vendors *assumed* | N-N29, N-U29, N-AE27, N-AE30 |
| Share of deductions suppliers dispute today | 20-30% "ever disputed" (SPS, vendor) | — | — | *assumed* | N-AE27 |
| **Deductions per supplier per year (count)** | **~800 disputes** (ClearChain: "200–600 disputes per quarter" for mid-market clients) | **~2,400 disputes** (same, top of range) | **~12,000 deductions** (a Walmart apparel distributor, "nearly 3,000 deductions per quarter"); enterprise ~132,000 (HighRadius, 11,000 a month) | all *assumed* (vendor); annualised **[our calc]** | N-AE34, N-AE32, N-AE31 |
| **Average deduction size** | **$75-225** recovered per dispute (implied by ClearChain's guarantee and volumes) | **$500** [our call] (Bissell wrote off "thousands of deductions under $500") | **$2,000** (HighRadius enterprise: $22M over ~11,000 a month, all types) | inputs *assumed*; ratios **[our calc]** | N-AE34, N-AE28, N-AE31 |
| **Minutes per deduction** | ~5 min triage with software **[our call]** | **8-15 min** to file one claim by hand (iNymbus studies); ~22 min per deduction resolved (HighRadius: 20 per analyst a day) | CRF Benchmarking Report as quoted: **$97** to "process, research, validate, dispute and clear" one deduction (≈ 2.9 hours at a collector's loaded rate [our calc]) | all *assumed* | N-AE32, N-AE31, N-AE40 |
| **Wages, BLS May 2025 (mean hourly)** | Offshore billed ~$12/h (check AA) | Bill and account collectors (43-3011) **$23.59** → **$33.70** loaded | Credit analysts (13-2041) **$48.49** → **$69.27** loaded | BLS *verified* (API); loaded **[our calc]**; offshore *assumed* | N-AE47, N-AA27, N-AA28 |
| **Big-box sales per supplier** | Walmart: median supplier record ≈ **$0.6-1.8M** a year (model) | Walmart: mean **$13.2M** per record ($412.4B ÷ 31,196) | Records above $50M of Walmart sales: **~1,200-1,500**; above $100M: ~600-700 | inputs *verified* (N-U03); distribution **[our calc]** on a lognormal **[our call]** | N-U03, §5 |
| Big-box share of sales at small public suppliers | 40% (Lifetime: Walmart+Amazon+Costco) | 48-66% (Hamilton Beach, Crown Crafts, Jakks) | 80% (Summer Infant: Amazon+Walmart+Target) | *verified* (filings) | N-AE02 to N-AE08 |
| **Suppliers big enough for a $5,000/yr fee at 25%** | Low leak (0.004% recoverable): needs ~$500M big-box sales → **~0 inside the segment** | Central (0.03% recoverable): needs **~$67M** → **~600-2,000 suppliers** | High (0.4% recoverable): needs **~$5M** → **~5,800-13,000** | **[our calc]** on the rows above | §5, §9 |
| **What vendors charge** | $0.40-0.70 per claim (iNymbus, snippet); $19.99/month (SPS, smallest Amazon 3P sellers) | **Contingency 15-35%** of recoveries (Eva 20%; Threecolts 15-25%; Vendormint 30%; OverDeduct "commonly 25–35%") | **Flat $5,000/month** (ClearChain); SupplyPike subscription "starting" $810/month (snippet) | *assumed* (vendor pages) | N-AE33 to N-AE37, N-AE20, N-AE55 |
| **Revenue per recovery customer** | SPS's divested Amazon 3P recovery base: **~$2,900 per customer a year** | SupplyPike: **≤ ~$38,000-50,000 per customer a year** | ClearChain list price: $60,000 a year | inputs *verified* (SPS releases) and *assumed* (customer counts, transcripts); per-customer **[our calc]** | N-AE17, N-AE21, N-AE22, N-AE34 |
| **Is the pool shrinking?** | Walmart eased OTIF from 98% to 90% on-time / 95% in-full (Feb 2024): fewer fines | Amazon: SPS's CFO, Q1 2026: "policy changes Amazon has made that reduce the amount we can recover for customers"; Amazon recovery "troughs somewhere in the middle of this year towards the end" | Target will fine a fifth dispute (amount not found); SPS sold its Amazon 3P recovery arm for $9.5M, booking a $23.5M loss | *assumed* (transcripts); Walmart threshold *assumed* (press); no measured before/after win rates exist | N-AE20, N-AE21, N-AE51, N-U13 |

**One-line reading [our call]:** neutral sources put the **recoverable** money at roughly **0.01-0.05% of a supplier's big-box sales** (non-trade deductions ¼-½% × 6-10% invalid × 60% recovered); vendors price and advertise as if it were **0.2-3%**. The whole card turns on which of these is true for a $20-200M supplier, and no neutral source measures it.

---

## 2. AE1 · Deduction and fine rates in suppliers' SEC filings

### 2.1 What was searched

- EDGAR full-text search (N-AE01) for "OTIF", "on-time in-full", "compliance fines", "compliance chargebacks", "non-compliance chargebacks", "retailer fines", "fill rate fines", "customer deductions", "vendor compliance", "routing guide", "late delivery" with "chargebacks", and "fines for late", 10-K/10-Q/8-K, mostly 2017-2026.
- **Result:** "on-time in-full" appears in 60 filings, almost all supply contracts in pharma and biotech exhibits; among consumer suppliers only Lifetime Brands' 10-Ks. "Retailer fines"/"OTIF fines" appear in five filings, all large companies (Energizer, Church & Dwight) or a lender deck. **No small or mid-sized supplier's filing was found that states an amount for OTIF fines, compliance chargebacks or shortages separately** from other deductions. Check N reached the same result for OTIF (N-N12); this check widens it to every non-trade term above.
- What filings do give: (a) a total "customer deductions" reserve or charge, which mixes trade and non-trade; (b) the share of sales to named big-box retailers.

### 2.2 Register of supplier filings

"Rate" = figure ÷ net sales for the same year **[our calc]**.

| # | Supplier (ticker), year | Net sales | Named big-box share of sales | Deduction figure, as disclosed | What it covers | Rate | Location | Label |
|---|---|---|---|---|---|---|---|---|
| F1 | **Crown Crafts (CRWS)**, infant and toddler products, FY ended 30 Mar 2025 | **$87,250K** (FY2024: $87,632K) | **Walmart 47%, Amazon 19%** of gross sales (FY2024: 42%, 19%); "top two customers represented approximately 66%" | "Allowance for customer deductions": **charged $7,480K** in FY2025, used $7,201K; FY2024 charged $6,139K | Returns and claims, "cooperative advertising, warehouse allowances, placement fees, volume rebates, coupons and discounts" — **mostly trade**; no split | **8.6%** FY2025; **7.0%** FY2024 | 10-K FY2025, Schedule II ("Valuation and Qualifying Accounts", 10-K p. 25); Note 2 (allowances); customers table in Item 1 and Note 4 | *verified* (full PDF, N-AE02) |
| F2 | Crown Crafts, FY ended 29 Mar 2026 | **$82,266K** | **Walmart 40%, Amazon 17%** | Allowance for customer deductions **charged $5,794K**, used $6,132K | As F1 | **7.0%** | 10-K FY2026: R12 (Schedule II), R16 (Note 4), R4 (statement of operations), R14 (Note 2) | *verified* (page extraction, N-AE03) |
| F3 | **Lifetime Brands (LCUT)**, kitchenware, FY2025 | **$647.9M** | Walmart 17%, Amazon 12%, Costco 11%, TJX 11% | "Allowance for anticipated customer deductions": **additions $7,833K** (2024: $3,837K; 2023: $6,900K) | "Contractual deductions for incentives and promotions … such as cooperative advertising, are recorded as a reduction to accounts receivable at the time of the sale", i.e. outside this allowance. So the allowance is the **non-contractual** part — closer to non-trade, but not labelled as such | **1.21%** (2025) | 10-K FY2025: R25 (Schedule II), R10 (policies), R11 (revenue note, net sales $647.9M); Item 1 "Customers" | *verified* (page extraction, N-AE04) |
| F4 | **Hamilton Beach Brands (HBB)**, small appliances, 2025 | **$606.9M** (2024: $654.7M) | Walmart 29%, Amazon 19%; five largest 62% | **No amount.** Variable consideration "includes returns and price concessions" | — | — | 10-K FY2025, Item 1 and critical accounting estimates | *verified* (full PDF, N-AE05) |
| F5 | **JAKKS Pacific (JAKK)**, toys, 2025 | ≈ **$572M** [our calc: $152,028K ÷ 26.6%] | **Target 26.6% ($152.0M), Walmart 26.1% ($149.2M)**; Amazon 10.0% in 2024 | **No amount.** Co-op allowances "range from 1% to 30% of gross sales" | Trade | — | 10-K FY2025: R12 (policies), R53 (major customers) | *verified* (page extraction, N-AE06) |
| F6 | **Owlet (OWLT)**, baby monitors, 2025 | **$105,708K** (2024: $78,056K) | Three largest customers **67%** of revenue and receivables (unnamed) | **No amount**; "anticipated sales returns, discounts, and allowances" | — | — | 10-K FY2025: R5, R9, R37 | *verified* (page extraction, N-AE07) |
| F7 | **Summer Infant (SUMR)**, 2021 | not read (extraction truncated) | **Amazon 38%, Walmart 24%, Target 18%** (2020: 33%, 28%, 17%) | No amount found | — | — | 10-K FY2021 | *verified* (page extraction, partial, N-AE08) |
| F8 | **Singing Machine (MICS)**, karaoke, FY ended 31 Mar 2023 | ≈ **$39.4M** [our calc: $5.0M ÷ 12.7%] | "top five customers" 89% of sales | "Our customers returned goods valued at approximately **$5.0 million or 12.7%** of our net sales"; "co-op promotion incentives of approximately **$2.3 million**" | Returns and co-op (trade); "late delivery" chargebacks are named as a risk without an amount | returns 12.7%; co-op ≈ 5.8% [our calc] | 10-K FY2023, Item 1A risk factors | *verified* (page extraction, N-AE09) |
| F9 | Funko (FNKO), Q4 2018 (contrast: large) | $233.2M (quarter) | — | Gross margin hit by "an increase in non-compliance chargebacks" | Non-trade, **no amount** | — | 8-K ex. 99.1, 28 Feb 2019 | *verified* (N-AE10) |
| F10 | Energizer (ENR), Q4 FY2020 (contrast: large) | $763.0M (quarter) | — | Volume "slightly offset by increased retailer fines and penalties due to the unprecedented demand spike" | Non-trade, **no amount** | — | 8-K press release, 12 Nov 2020 | *verified* (N-AE11) |

Also read, no usable figure: Once Upon a Farm 10-K 2025 ("Four customers … approximately 61% of our net sales"; no deduction amounts, N-AE56); Edible Garden 10-K 2025 (five customers 88.2% of revenue; a Meijer fixture programme of "approximately $800 thousand" paid "as a weekly deduction from our receivables" — trade, N-AE57); Alkaline Water Co. 10-K FY2023 and Scott's Liquid Gold 10-Q Q3 2022 (extractions truncated; no amounts, N-AE59, N-AE60).

### 2.3 A real contract term: who pays retailer chargebacks

- **Prestige Brands and GEODIS warehouse agreement** (effective 1 Oct 2024, filed as a 10-Q exhibit, N-AE12, *verified*): the 3PL (third-party warehouse) has "one hundred eighty (180) days from the date of Shipping Go-Live" to reach routing-guide compliance, during which the brand "bears sole responsibility for chargebacks"; after that, the 3PL is liable only above a threshold and up to an annual cap — **both amounts redacted**.
- **Why it matters [our call]:** part of a supplier's compliance-fine exposure is contractually passed to its 3PL or carrier. A recovery service may be disputing money the supplier would otherwise recharge to its warehouse.

### 2.4 Reading

- **Filings cannot give the non-trade rate.** They give a ceiling (all deductions, 7-9% of net sales at a Walmart-heavy supplier) and one closer proxy (Lifetime's non-contractual deductions, 1.2% of net sales in 2025; its additions were $3.8M in 2024 and $6.9M in 2023, but those years' net sales were not read, so no rate is given).
- **Filings do give big-box concentration**: 40-80% of sales at these small public suppliers, with Walmart alone at 17-47% (F1-F8). This feeds AE4.

---

## 3. AE2 · Court and bankruptcy records

### 3.1 What was searched

CourtListener's RECAP archive (free PDFs), by API (N-AE16): "OTIF" with Walmart and "fines"; "customer programs" with OTIF, chargebacks, compliance; "compliance chargebacks"; "non-compliance chargebacks"; "vendor compliance" with chargebacks; "shortage claims" Amazon; "deduction recovery" contingency; first-day declarations and customer-programs motions for Instant Brands, Tupperware, BowFlex, Del Monte Foods, Hearthside, Vintage Wine Estates, Tattooed Chef. Opinions search for the same terms.

**Result:** no supplier-versus-retailer deduction dispute with a remittance or deduction ledger was found. Most customer-programs motions of bankrupt suppliers (Tupperware, BowFlex, Del Monte) are listed in RECAP without the PDF. Two records carry usable numbers.

### 3.2 Record 1 — a real deduction ledger (home video into Walmart, Sam's Club and Best Buy)

**Miller v. ANConnect, LLC**, Adv. No. 18-50633 (Bankr. D. Del.), Doc 295, Declaration of Jay Maier with exhibits, filed 27 Feb 2023, page 250 of 266 (N-AE14, *verified*, full PDF). The page is the **"ALCHEMY STATEMENT SUMMARY — Anderson Merchandisers — 07/01/15 - 07/09/15 FINAL STATEMENT"**, "Inception to date" (inception 1 July 2011): the statement a distributor (Anderson Merchandisers, which sold into the retailers) gave the content owner (Alchemy). The retailers named on other pages are Walmart, Sam's Club and Best Buy ("Walmart represented 80% of the returns").

| Line (as printed) | Inception to date | % of sales invoiced [our calc] | Trade or non-trade [our call] |
|---|---|---|---|
| Sales invoiced, value | **$27,026,436.25** (3,252,126 units) | 100% | — |
| Returns | ($7,588,024.93) | 28.1% | returns (home video is return-heavy) |
| Marketing Rebates | ($5,551,248.94) | 20.5% | trade |
| **Shipping Variances** | **($54,048.32)** | **0.20%** | **non-trade (shortage/receiving differences)** |
| Chargebacks/Other | ($0.02) | 0.00% | non-trade |
| Appr Co-Op Marketing | ($569,579.20) | 2.11% | trade |
| Price Protection | ($127,798.25) | 0.47% | trade |

- The same exhibit set lists "OPEN SHORTAGE CLAIM DEDUCTIONS $(429.40)" at 9 July 2015 and an "Expedited Freight Chargeback 578,102.65" among the disputed items between the two companies (page 239) — a freight charge in the parties' own reconciliation, not shown to be a retailer fine.
- **Reading [our call]:** in the one real ledger found, **non-trade deductions were 0.2% of invoiced value over four years**, inside the low end of CRF's ¼-½% median. It is one old, atypical product line (DVDs, 2011-15, before Walmart's OTIF programme began in 2017), so it bounds nothing on its own.

### 3.3 Record 2 — a bankrupt big-box supplier's deduction programmes (Instant Brands, 2023)

**Instant Brands Acquisition Holdings Inc.**, Case 23-90716 (Bankr. S.D. Tex.), Doc 39, Declaration of Adam Hollerbach (chief restructuring officer) in support of first-day pleadings, filed 13 Jun 2023, pp. 69-72 (N-AE13, *verified*, full PDF). The company (Instant Pot, Pyrex, Corelle) sold "at more than 30 global retailers, including Walmart, Target, and Costco, as well as on eCommerce platforms, such as Amazon".

| Programme (as named) | What it covers (quoted) | Amount | Label |
|---|---|---|---|
| **Off-Invoice Allowances** | "(a) flat-rate and payment term discounts, (b) defective allowances, and (c) **other non-compliance charges (e.g., claim deductions, incorrect quantities, early or late shipments of Customer Products, etc.)**", funded "by deducting the relevant amounts directly from the Company's invoice" | "an average of approximately **$1.6 million per month**" in Q1 2023 (≈ $19M a year [our calc]) | *verified* |
| Retailer Promotions | co-op advertising, data, marketing, new distribution, via agreed invoice deductions | "approximately **$4.6 million**" in Q1 2023 | *verified* |
| Refund and Exchange Programs | "damaged, mislabeled, unused, or returned Customer Products" | "approximately **$150,000 per month**" in Q1 2023 | *verified* |
| All Customer Obligations | — | "approximately **$105 million**" in 2022 | *verified* |
| Scale reference | 2022 gross profit **$138.8M**; EBITDA $57.2M | — | *verified* |

- **The document states no net sales**, so no rate is computed; and it mixes non-compliance charges with payment-term discounts in one line. It does show, from a sworn filing, that **non-compliance charges for quantities and early/late shipments are deducted straight off invoices and are a standing monthly cost line at a big-box supplier.**

### 3.4 Other court documents read

- **JD Global Sales v. JEM D International** (D.N.J. 2:21-cv-19943), opinion of 23 Feb 2026 (N-AE15, *verified*): a produce broker sought by subpoena Walmart's "On Time and In Full ('OTIF') fulfillment requirements for Produce Suppliers/Vendors and all Monthly OTIF reports". No amounts.
- **Pegasus Integrated Consulting v. Rue 21** (S.D.N.Y. 2007) matched "compliance chargebacks", but the filings are scanned images with no text layer; not read (§11).

### 3.5 What the court route did not give

Share disputed, share recovered and days to resolution from a real ledger: **not found**.

---

## 4. AE3 · The invalid share and the recovery rate

### 4.1 Neutral and association sources

| Source | Figure (quoted) | What it is a share of | Label | ID |
|---|---|---|---|---|
| **CRF 2018 Customer Deduction Survey** (Attain Consulting for the Credit Research Foundation; 203 firms, 52% with sales ≤$500M) | "6–10% of all deduction dollars are invalid or disallowed … (median)"; "60% of all deduction dollars that are invalid or disallowed are ultimately recovered"; non-trade "Median is ¼ - ½ % of sales" | invalid: **all** deductions, trade included | *verified* (PDF read in check N; CRF flag) | N-N29 |
| CRF 2021 survey, via Carixa's slides (Aug 2023) | "up to 1% of sales"; "5-10%" invalid; "60%" recovered; "90-day median" | as above | *assumed* | N-U29 |
| **CRF Benchmarking Report, as quoted by Quadient** (an accounts-receivable software vendor, 29 Oct 2020) | "a single deduction costs a company approximately **$97** to process, research, validate, dispute and clear"; "90 days to resolve a deduction"; "only 60% of invalid deductions are actually recovered"; "5% to 15% of all invoices are affected by deductions, and about **85% of them are merited**" | per deduction; share of invoices | *assumed* (vendor quoting CRF; the report was not read) | N-AE40 |
| **McKinsey**, "Deliver on time or pay the fine" (6 Sep 2018) | "Walmart charges suppliers 3 percent of the purchase price for every order delivered early, late or incomplete"; "penalties could add up to **more than $5 billion a year** across the US, if the consumer packaged goods (CPG) sector doesn't improve its current delivery performance. Individual CPG players could see their margins cut by a full a percentage point" | a scenario, not a measurement | *verified* at source (consultancy estimate) | N-AE49 |
| McKinsey, "Defining 'on-time, in-full' in the consumer sector" (13 Jun 2019; survey of 24 retailers and CPG makers) | "only 4 percent of shipments to retailers arrive more than 12 hours late"; "about 25 percent of deliveries arrive more than two hours before their scheduled delivery appointment" | shipments | *verified* at source | N-AE50 |
| **Uber Freight, quoted in Forbes** (Steve Banker, 1 Feb 2024) | "in their customer base, Walmart suppliers are currently paying **0.16% of the cost of goods sold** in fines to Walmart"; "for many retailers, the fines are well in excess of $1 million per year" | OTIF fines ÷ goods sold to Walmart | *assumed* (an interested logistics provider; Forbes original read via the Wayback Machine; same figure as N-S13) | N-AE51 |
| An agency's Amazon guide (Tahiti North, 11 Jul 2026) | "shortage claims run 1 to 3 percent of invoiced value per year, and 5 to 10 percent for accounts with systemic ASN problems" (citing Wake Commerce); on win rates: "We will not hand you an industry win rate … because the published ones are marketing rather than measurement" | Amazon 1P invoiced value | *assumed* | N-AE42 |

**Other surveys:** Attain's 2015/2018/2020/2021 reports are free only after giving an email (not done); the 2020 COVID deck on RVCF's site returned 403; CRF's 2021 and 2023 reports go only to participants; APQC's cost-per-deduction benchmark sits behind Cloudflare; IOFM's whitepaper returned 403 (§11). OverDeduct, a vendor that compiled the public figures, concludes: "**No public industry-wide benchmark exists**; these are vendor and consultant estimates presented as ranges" (N-AE38, *assumed*).

### 4.2 Vendor figures (all *assumed*)

| Vendor | Figure (quoted) | ID |
|---|---|---|
| SPS Commerce / SupplyPike (article updated 3 Nov 2025) | "On average only **20-30%** of deductions are ever disputed by suppliers, yet an average **40%** of disputed deductions are won back"; Eagle Foods recovered "more than $400K in revenue previously lost to Walmart deductions" | N-AE27 |
| SupplyPike's founder at the SPS deal (Talk Business, Aug 2024) | "between **8% and 10%** of deductions are erroneous" | N-AE22 |
| SPS Revenue Recovery pages (read 2026-09-22) | "$2B+" recovered; "up to **75%** of eligible deductions reclaimed" (1P page); "up to 99%" (main page); Owlet "recovered **$1.4M in six months**" | N-AE26 |
| SupplyPike (search result, page not reachable) | "the average Walmart supplier loses **5.8%** of their invoices to deductions—some lose over 30%" (all types) | N-AE29 |
| STAT Recovery Services (release, 18 Jun 2026) | "more than **$1 billion** in supplier revenue" recovered for "500+ retail suppliers"; "**$500 billion** in analyzed supplier transactions"; win rates Walmart "97%", Target "93%", Amazon "89%"; 24-month historic audit | N-AE30 |
| HighRadius (15 Nov 2023; enterprise customers after automation) | invalid "about 5% – 10%"; deductions "between 10% – 20%" of revenue (trade included); "~11,000" deductions and "$22 million" a month per enterprise; "76% of them auto-write off up to $100"; 41 days to resolve; 20 resolved per analyst a day | N-AE31 |
| Glimpse (seed release, Apr 2025) | deductions "can drain up to 3 percent of a CPG brand's revenue"; "average return on investment of four to five times"; "more than 125 brands" (200+ by Mar 2026, N-U34) | N-AE39 |
| ClearChain (FAQ) | "94% chargeback win rate"; "$5M+ in recovered and protected revenue" across engagements | N-AE34 |
| Threecolts Margin Pro | "$360M+ saved for Amazon and Walmart vendors to date"; headline "Get 2-5% Revenue Back" | N-AE36 |
| Claimlane (6 Jul 2026, illustrative model) | €20M wholesaler: deductions "2 to 5% of gross sales", ~25% invalid, "60% of the invalid share" recovered = €90,000 a year | N-AE41 |
| HRG (search result) | proactive management recovers "an average of 60-70% of disputed amounts" | snippet, N-AE30 row note |

### 4.3 Cases that give both a recovered amount and a base

| Case | Recovered | Base | Implied rate [our calc] | Label |
|---|---|---|---|---|
| **Owlet** (SPS case) | $1.4M "in six months" (incl. "100% recovery on a $423.4k Amazon settlement", snippet) | Owlet's 2025 revenue **$105.7M**, three largest customers 67% (≈ $70.8M) (10-K, *verified*) | 1.3% of a year's revenue in six months; ≈ 2.0% of top-three-customer revenue in six months. **Likely a first-period catch-up of a backlog** [our call] | recovered *assumed*; base *verified* |
| **STAT** (aggregate) | >$1B | $500B "analyzed supplier transactions" | **0.2%** of transactions analysed | *assumed* |
| SupplyPike (aggregate) | "over $1 billion" by 24 Feb 2025 ("over $900 million" on 19 Dec 2024) | ">500 retail suppliers" (Aug 2024); founded Dec 2017 | ≈ $2M per supplier over ~7 years if spread evenly — not a rate | *assumed* |
| Chosen Foods (SPS, Q2 2026 call) | "approximately 30% of outstanding deductions" | no base | — | *assumed* |
| Bissell (SPS case) | "over $1 million"; "6,000 deductions under the previous write-off threshold recovered"; "99.98%" Walmart clear rate | no base | — | *assumed* |

### 4.4 Walmart OTIF specifically

- **Total fines:** no Walmart figure found. McKinsey's ">$5 billion a year" is a 2018 scenario for all US CPG (N-AE49); Forbes/Uber Freight: "over a billion dollars per year" for the lack of delivery compliance, and 0.16% of COGS in one provider's customer base (N-AE51).
- **Share reversed on dispute, share disputable:** **not found** from any source, vendor or neutral. SPS's OTIF dispute guides are qualitative ("Anything is fair game 13 months from the current date", N-AE54).
- **Sizes of single cases:** a Fortune 500 food and beverage shipper "avoided $220K in OTIF fines" at Walmart in Q1 2024 with a "4% increase in on-time cases" (Triumph, *assumed*, N-AE53).

---

## 5. AE4 · How much does a supplier sell to big-box stores?

### 5.1 Walmart's own anchor, modelled

- **Inputs (*verified*, check U):** 31,196 Walmart US supplier records, $412.4B of spend, FYE 2025 (N-U03). Mean **$13.2M per record** [our calc].
- **Caveats:** these are Dun & Bradstreet records summed over state pages (a supplier with several locations may appear more than once), and they include services suppliers, not only merchandise.
- **Model [our call]:** firm sizes follow a skewed curve (few giants, many small firms). We fit a lognormal curve with the verified mean and a spread (sigma) of 2.0 or 2.5. Sigma 2.5 better matches the fact that the largest suppliers sell about $10B+ a year to Walmart (P&G-scale); at sigma 2.5 the top 1% of records hold ~57% of the spend.

| Walmart sales per supplier record, per year | Records above it, sigma 2.0 | Records above it, sigma 2.5 |
|---|---|---|
| Median record | $1.79M | $0.58M |
| > $5M | 9,473 | 6,071 |
| > $10M | 6,076 | 3,977 |
| > $20M | 3,547 | 2,447 |
| > $50M | 1,496 | 1,166 |
| > $100M | 690 | 615 |
| > $200M (proxy for suppliers above the $500M sales cap) | 286 | 304 |

All counts **[our calc]** on verified inputs and a **[our call]** curve. The tail counts move little with sigma because the mean is fixed.

### 5.2 How much of a small supplier's sales go to big-box stores (filings, *verified*)

| Supplier | Big-box share | Walmart alone | Ratio big-box ÷ Walmart [our calc] |
|---|---|---|---|
| Crown Crafts FY2025 | Walmart + Amazon 66% | 47% | 1.4 |
| Hamilton Beach 2025 | Walmart + Amazon 48% | 29% | 1.7 |
| JAKKS 2025 | Target + Walmart 52.7% (+ Amazon 10% in 2024) | 26.1% | 2.0-2.4 |
| Lifetime Brands 2025 | Walmart + Amazon + Costco 40% | 17% | 2.4 |
| Summer Infant 2021 | Amazon + Walmart + Target 80% | 24% | 3.3 |

Median ratio ≈ **2**: a typical small supplier sells about twice as much to all big-box retailers as to Walmart alone **[our call on five cases]**.

### 5.3 Census cross-check: consumer-goods firms by size (SUSB 2022, *verified*)

Firms by enterprise receipts, 2022 (N-AE48). Consumer-goods manufacturing = NAICS 311, 312, 315, 316, 3256, 3352, 337, 339; consumer-goods wholesale = 4232, 4236, 4239, 4241, 4242, 4243, 4244, 4246, 4249 **[our call on the set]**. The $100M+ class is split at $500M using each sector's large-size table (manufacturing: 66.9% of $100M+ firms are under $500M; wholesale: 71.7%) **[our calc]**.

| Firm receipts (all customers) | Consumer-goods manufacturers | Consumer-goods wholesalers |
|---|---|---|
| All firms | 81,783 | 137,497 |
| ≥ $5M | 12,926 | 39,203 |
| ≥ $10M | 8,612 | 26,070 |
| ≥ $20M | 5,829 | 16,532 |
| ≥ $50M | 3,518 | 8,855 |
| $100-500M | ≈ 1,627 | ≈ 3,940 |

These are all firms in those industries, most of which do not sell direct to big-box retailers (wholesalers include foodservice and business-to-business distributors). They are a ceiling, and they agree in order of magnitude with §5.1: a few thousand firms have the size to sell tens of millions a year to big-box stores.

### 5.4 Count of suppliers large enough for a $5,000-a-year fee

A 25% fee reaches $5,000 when recoveries reach $20,000 a year. Big-box sales needed = $20,000 ÷ (non-trade % × invalid share × recovery share) **[our calc]**:

| Case (inputs from §1) | Recoverable, % of big-box sales | Big-box sales needed for $5,000 fee | Walmart-only count (ratio 1), in segment* | All-big-box count (ratio 2), in segment* |
|---|---|---|---|---|
| Low: 0.2% × 5% × 40% | 0.004% | **$500M** | ≈ 0 | ≈ 0 |
| **Central: 0.5% × 10% × 60%** | **0.03%** | **$66.7M** | **598-812** | **1,337-1,953** |
| Vendor aggregate (STAT: 0.2% recovered) | 0.2% | $10M | 3,674-5,790 | 5,767-9,187 |
| High: 1.5% × 30% × 90% | 0.405% | **$4.9M** | 5,767-9,187 | 8,421-13,239 |

\* Records above the threshold minus records above $200M of Walmart sales (a proxy for the $500M total-sales cap); ranges are sigma 2.5 to 2.0. All **[our calc]**; the ratio of 2 is **[our call]** from §5.2; suppliers that do not sell to Walmart at all are not counted (they would add some).

**Against check U's buyer count** (central ~29,000): at the central inputs, **about 5-7% of the buyers** could yield a $5,000 fee; at the high inputs, 30-45% **[our calc]**.

---

## 6. AE5 · Cost to serve

### 6.1 Wages (BLS OEWS, May 2025, national, all industries; *verified* via the BLS public API, N-AE47)

| Occupation (SOC code) | Employment | Mean hourly | Median hourly | Loaded mean (÷ 0.70) [our calc] |
|---|---|---|---|---|
| Bill and account collectors (43-3011) | 158,830 | **$23.59** | $22.61 | **$33.70** |
| Bookkeeping, accounting and auditing clerks (43-3031) | 1,373,680 | $25.75 | $24.36 | $36.79 |
| Credit analysts (13-2041) | 64,390 | **$48.49** | $40.15 | **$69.27** |
| Customer service representatives (43-4051) | 2,595,750 | $22.40 | — | $32.00 |
| Offshore back office (check AA, billed rate) | — | ~$12 (range $6-16) | — | — |

Employment counts match check S (N-S01). Deduction analysts are usually classed as collectors or credit analysts (check S §2.4).

### 6.2 Time and cost per deduction (all *assumed*)

| Source | Figure (quoted) | Reading [our calc] |
|---|---|---|
| iNymbus, study at a Walmart apparel distributor | "each deduction claim demanded **8 to 15 minutes** for manual completion"; "nearly 3,000 deductions per quarter"; "over 400 hours" | 400 h ÷ 3,000 = **8 minutes** each |
| iNymbus, Warner Bros study | "around 5 to 8 minutes for organization and 5 to 7 minutes for portal uploads" | 10-15 minutes |
| iNymbus | manual "**$5.28**" per claim vs "around $1" automated | $5.28 ≈ 9-13 minutes at $24-36 an hour |
| HighRadius (enterprise, after automation) | "Deductions resolved per analyst daily: **20**" | ≈ 22 minutes each in a 7.5-hour day |
| CRF Benchmarking Report, as quoted by Quadient | "approximately **$97** to process, research, validate, dispute and clear" | ≈ 2.9 h at $33.70 — a full cross-department cost (sales, logistics, AR), not one clerk's time |
| iNymbus pricing (search result) | "$0.40–$0.70 per claim" | automation price per claim |

**No source gives minutes to research a deduction and decide whether it is invalid** as distinct from filing it. That triage step is the one a software product would compress.

### 6.3 Deduction counts and sizes per supplier (all *assumed*)

| Source | Count | Size |
|---|---|---|
| ClearChain, "typical mid-market clients" ($5M+ retail revenue) | "**200–600 disputes per quarter**" = 800-2,400 a year | Its guarantee ("at least 3x your fee" of $5,000 a month = $15,000 a month) spread over 200-600 disputes a quarter gives **$75-225 recovered per dispute** [our calc] |
| iNymbus, Walmart apparel distributor | 3,000 deductions a quarter = 12,000 a year | — |
| iNymbus, video game distributor | "up to 1,500 Walmart chargebacks monthly" | — |
| HighRadius, enterprise | ~11,000 a month | $22M ÷ 11,000 = **~$2,000** each (all types) |
| Bissell (SPS) | "6,000 deductions under the previous write-off threshold" | under $500 |
| HighRadius | "76% of them auto-write off up to $100" | — |

### 6.4 Setup per retailer portal

- **Not found as effort (hours).** Vendors state onboarding times only: ClearChain launches disputes "within two weeks of onboarding", with an audit phase on "days 4–10"; Eva completes an initial analysis "within 48 hours of account access"; Threecolts asks "< 3 hours" of the client's time (all *assumed*, N-AE34 to N-AE36).
- Portals are reached with the supplier's credentials and bots, one retailer at a time (check S §2.4).

### 6.5 What vendors charge (all *assumed*)

| Vendor | Model | Minimum client | ID |
|---|---|---|---|
| Vendormint | 30% contingency | — | check U (N-U38) |
| Eva (eva.guru) | "Flat 20% commission on successfully recovered funds only"; no setup fee or minimum (its FAQ says 10%) | Amazon and Walmart vendors | N-AE35 |
| Threecolts Margin Pro | "Typical fee shares range from 15-25%, flexing with annual recovery volume and contract length" | "vendors selling **$1M+** annually through Amazon or Walmart" | N-AE36 |
| OverDeduct (market summary) | "commonly **25–35%** of the dollars actually recovered" | not stated | N-AE37 |
| ClearChain | "**Flat $5,000 per month**, month-to-month"; "no percentage of recoveries"; 3x guarantee; says contingency firms "take 20–30%", and a flat fee wins "once recoveries pass roughly $20K/month" | "roughly **$5M+ in retail revenue**" | N-AE34 |
| STAT | "performance-based fee model", "no upfront cost", "no subscription" (no % stated) | not stated | N-AE30 |
| SupplyPike / SPS | annual flat rate "based on the size of your business per retailer"; "starting" $810 a month; $99 a month for qualifying new Walmart suppliers (search results; pricing page timed out); moving small Amazon 3P take-rate customers to **$19.99 a month** (Q1 2026 call) | not stated | N-AE55, N-AE20 |
| iNymbus | per claim, "$0.40–$0.70" (search result) | not stated | N-AE33 |
| Glimpse | "pricing is scoped to your account" (search summary) | not stated | N-AE39 |

### 6.6 Revenue per recovery customer — what suppliers actually pay (AE6's benchmark)

| Business | Revenue | Customers | Per customer a year [our calc] | Labels |
|---|---|---|---|---|
| **SupplyPike** (1P, Walmart-first) | SPS: "approximately $8.0 million" in Aug-Dec 2024 (≈ $19M a year) and "approximately **$25.0 million**" in FY2025 | "more than **500** retail suppliers" (Aug 2024) | **≤ $38,000-50,000** (upper bound, because "more than 500") | revenue *verified* (SPS 8-K, N-AE17); count *assumed* (press, N-AE22) |
| **SPS's Amazon 3P recovery business** (sold 30 Jun 2026) | "reduce second-half 2026 revenue by about **$10.5 million**" (≈ $21M a year) | "approximately **7,300**" | **≈ $2,900** | *assumed* (call transcripts, N-AE21) |
| Carbon6 (1P ChargeGuard + 3P Seller Investigators + other seller tools) | "approximately **$40.0 million**" expected in FY2025 | not stated | — | *verified* (release, N-AE18) |
| SPS overall (all products) | ARPU about $14,350 | 46,900 1P customers | — | *verified* (N-U01) |
| ClearChain | $60,000 list | — | $60,000 | *assumed* |

**Reading [our call]:** the one 1P benchmark with a real revenue line (SupplyPike) collects on the order of **$40,000 a customer a year**. At a 25% share that would be the fee on ~$160,000 of recoveries a year per customer. At the central leak of 0.03% that needs ~$530M of big-box sales, so SupplyPike's customers are either larger than C-19's segment or leak far more than CRF's medians.

---

## 7. AE6 · Is the pool shrinking?

| Date | Change | Numbers found | Effect on the pool | Label | ID |
|---|---|---|---|---|---|
| 1 Feb 2024 | Walmart lowers OTIF goals from 98% (since Sep 2020) to **90% on-time and 95% in-full** | none on fines before and after | **fewer OTIF fines** at the largest retailer | *assumed* (Forbes; Walmart's announcement is on the supplier portal) | N-AE51 |
| 2024 | Walmart bills OTIF fines quarterly; a month's total under $1,000 waived | — | fewer small fines | *assumed* | N-U09 |
| Mid-2025 | Amazon: shortage disputes limited to 2 years of invoices (was 5); bulk disputes ended | — | smaller look-back; more line-level work | *assumed* | N-U24 |
| By 21 Nov 2025 | Target will fine a supplier that disputes the same deduction a fifth time | **fine amount not found** | caps re-disputing | *assumed* | N-U13 |
| Q4 2025 (12 Feb 2026) | SPS: revenue recovery at "the lower end" of expectations, citing "take rate model" and "Amazon policy changes" | — | — | *assumed* | N-U31 |
| **Q1 2026 (30 Apr 2026)** | SPS CFO: "The reduction in the guide is related to overall headwinds from the Amazon space tied to **policy changes Amazon has made that reduce the amount we can recover for customers**"; the Amazon recovery segment "continues on a negative trajectory. It probably troughs somewhere in the middle of this year towards the end of this year"; "The number of 1P customers was flat sequentially while the number of 3P customers declined by 400"; up to 4,000 small 3P customers expected to churn after a $19.99 monthly fee | guidance cut (amount not read); 3P −400 in a quarter | **Amazon pool shrinking, per the market leader** | *assumed* (Motley Fool transcript) | N-AE20 |
| **30 Jun 2026 (Q2 2026 call, 30 Jul)** | SPS sells the 3P recovery business: "cash payment of **$9.5 million**", "loss on sale of **$23.5 million**", "approximately 7,300 customers"; reasons: "the take rate revenue model and some of the policy changes in 3P we saw from Amazon"; "the 1P side of this business is much more attractive" | 3P ≈ $21M a year of revenue sold for $9.5M | the incumbent keeps 1P (this card's buyer) | release *verified* (N-U33); detail *assumed* (transcripts) | N-AE21 |
| 2026 | SPS says 1P revenue recovery outside Amazon will "continue to outpace overall company growth" | — | 1P non-Amazon pool not shrinking, per SPS | *assumed* | N-AE20 |

- **No source measures win rates or recoveries before and after any rule change.** The one agency that looked says the published win rates "run back to recovery-vendor marketing rather than measured data" (N-AE42).
- **Reading [our call]:** the evidence of shrinkage is concentrated at **Amazon** and at **Walmart OTIF**; Kroger tightened in 2025 (check U), which grows its pool. The market leader's own words are that Amazon's changes "reduce the amount we can recover".

---

## 8. AE7 · The OTIF fine arithmetic from the rules

Walmart's rule (check U): 3% of the cost of the **non-compliant cases**, charged when the supplier misses the goal (on-time 90% prepaid / 98% collect; in-full 95%). The "cost" is Walmart's cost, i.e. **the supplier's invoice value** (McKinsey: "3 percent of the purchase price", N-AE49).

**Fine as % of sales to Walmart ≈ (share of cases that fail) × 3%, if below the goal; else 0 for that metric** [our calc]:

| On-time performance (prepaid) | Cases failing | On-time fine, % of Walmart sales |
|---|---|---|
| 92% (above the 90% goal) | 8% | **0%** |
| 88% | 12% | **0.36%** |
| 85% | 15% | **0.45%** |
| 80% | 20% | 0.60% |
| 70% | 30% | **0.90%** |

- Add in-full failures the same way (below 95%). Target now also uses 3% of COGS (check U); Home Depot and Lowe's use 10% offsets on the late or missing value — a supplier at 85% on-time at Home Depot would pay ~1.5% of those sales [our calc on check U's assumed rates].
- **Observed level:** 0.16% of COGS at Walmart in Uber Freight's customer base (N-AE51) — consistent with most shippers sitting near or above the goal and paying on a minority of months [our call].
- **Small suppliers' actual OTIF levels:** **not found.** No public distribution of supplier OTIF scores exists; McKinsey's survey found only 4% of shipments more than 12 hours late (N-AE50), and Walmart's own goals have been 70% LTL / 85-87% truckload (2018-19) → 98% (2020) → 90%/95% (2024) (N-AE52), which suggests the median supplier sits in the high 80s to low 90s [our call].
- **Bound:** for a supplier near Walmart's goal, OTIF fines are **0-0.5% of Walmart sales**; the recoverable part is only the invalid fines inside that.

---

## 9. For the coordinator (not a call)

Everything here is **[our calc]** or **[our call]**. Nothing is decided.

### 9.1 The chain at three settings

| Setting | Non-trade % of big-box sales | Invalid share | Recovered share | Recoverable, % of sales | 25% fee, % of sales | Fee on $20M | Fee on $67M | Fee on $200M |
|---|---|---|---|---|---|---|---|---|
| Low | 0.2% | 5% | 40% | 0.004% | 0.001% | $200 | $670 | $2,000 |
| **Central** | **0.5%** | **10%** | **60%** | **0.03%** | **0.0075%** | **$1,500** | **$5,000** | **$15,000** |
| High | 1.5% | 30% | 90% | 0.405% | 0.101% | $20,250 | $67,500 | $202,500 |

- **The recoverable share of sales spans a factor of 100** between the low and high settings. Every neutral input sits at the low-to-central end; every vendor input at the high end.
- **Caution on the central setting:** CRF's "6-10% invalid" is a share of **all** deduction dollars, trade included (N-N29). Applying it only to non-trade deductions could be too high (if invalid deductions are mostly pricing and promotion errors, which C-19 excludes) or too low (shortage and OTIF claims may be invalid more often than promotions). No source splits it.

### 9.2 Worked example: one supplier at the central setting

A supplier selling **$66.7M a year** to big-box retailers (about $33M to Walmart at the ratio of 2).
1. Non-trade deductions: 0.5% × $66.7M = **$333,500** a year.
2. At $500 each: **667 deductions** a year to look at.
3. Invalid: 10% = 67 deductions, **$33,350**.
4. Recovered: 60% = **$20,010**.
5. Fee at 25%: **$5,003**.
6. Labour: triage 5 minutes on all 667 + 20 minutes to dispute each of the 67 = 78 hours.
   - at a US collector's loaded $33.70: **$2,622**;
   - at a credit analyst's loaded $69.27: **$5,390**;
   - offshore at $12: **$934**.
7. Before portal setup and fixed cost: **+$2,381** (collector), **−$387** (credit analyst), **+$4,069** (offshore).

### 9.3 The deciding ratio: average deduction size

Per deduction looked at, expected fee = size × invalid share × 60% × 25%; cost = (5 + invalid share × 20) minutes × wage. The **invalid share needed just to cover labour** [our calc]:

| Average deduction | US collector ($33.70) | US credit analyst ($69.27) | Offshore ($12) |
|---|---|---|---|
| $150 | 24.9% | never covers | 5.4% |
| $300 | 8.3% | 26.3% | 2.4% |
| **$500** | **4.4%** | **11.1%** | 1.4% |
| $1,000 | 2.0% | 4.5% | 0.7% |
| $2,000 | 1.0% | 2.1% | 0.3% |

- If most non-trade deductions are small (ClearChain's implied **$75-225 recovered per dispute**; Bissell's thousands "under $500"; HighRadius's 76% writing off ≤$100), **US-staffed review loses money on each deduction at CRF's invalid shares**. The model works when the service looks only at large deductions or uses offshore or automated triage.
- This is the same lesson as C-09's practice audit: **the count of items needing a human decides cost, the rate of provable errors decides revenue.**

### 9.4 What the market prices imply

- Vendor minimums: ClearChain ~$5M+ retail revenue at $60,000 a year; Threecolts $1M+ Amazon/Walmart sales at 15-25%; SupplyPike ~$40,000 a customer a year (§6.5-6.6).
- For those prices to pay suppliers back 3×, recoveries must be **roughly 1-4% of retail sales** for a $5-20M brand (ClearChain: 3 × $60,000 = $180,000 on $5-20M) — **30-120× the central neutral setting of 0.03%** [our calc].
- Three explanations, not tested here: (a) their customers are selected for high leakage (Amazon shortages, ASN problems — "5 to 10 percent for accounts with systemic ASN problems", N-AE42); (b) their recoveries include pricing and promotion deductions (trade, out of scope); (c) first-year recoveries include a backlog (Owlet's $1.4M in six months; STAT's 24-month look-back). **The S5 savings assessment is the only way to tell which** [our call].

### 9.5 Pool and the revenue floor, central setting

- Qualifying suppliers (≥ $66.7M big-box sales, ≤ $500M total): **~1,300-2,000** (ratio 2) or ~600-800 (Walmart only) (§5.4).
- Their fees run from $5,000 (at $66.7M) to ~$30,000 (at $400M); **a typical fee of ~$10,000** gives a **maximum pool of ~$13-20M a year** if every one signed [our calc on our call].
- The $2.5M revenue floor needs ~250 such customers, i.e. **~13-19% of all qualifying suppliers**; the $1M milestone ~100 customers (5-8%).
- At the high setting the pool is several times larger (thousands of suppliers at $5M+), which is the world vendors advertise.

### 9.6 Other design facts that bear on the model

- **Windows are short** (check U): Walmart AP chargebacks 15-30 days from posting, Lowe's ~15 days a month, Home Depot ~4 weeks for offsets, Amazon 30 days. A look-back sells little outside Amazon (2 years) and Walmart shortages (12 months). **Money comes from monitoring every month, which is also where the per-deduction labour cost falls.**
- **Part of the fine exposure belongs to 3PLs and carriers** by contract (the GEODIS clause, §2.3). A service that recharges those rather than disputing with the retailer is a second revenue path not modelled here.
- **Suppliers dispute only 20-30% of deductions today** (SPS, *assumed*). If true, the uncaptured invalid money exists; if CRF's 60% recovery holds, the service's job is mostly the 70-80% nobody looks at — the small ones, which are the ones that cost most per dollar (§9.3).

### 9.7 Numbers to capture at S5 (suggested, not a kit change)

1. A year of the supplier's deduction and chargeback lines per retailer (from the portals or the remittance/EDI 812-820 files): **count, dollar total, size distribution, reason code**.
2. The supplier's own list of what it disputed, what came back and when.
3. Big-box sales by retailer for the same year (to compute non-trade % of sales).
4. OTIF scorecards (monthly on-time and in-full %) and fines billed.
5. 3PL and carrier contracts: who pays compliance chargebacks.

---

## 10. Sources

Access: **full** = whole document downloaded and read or searched; **page extraction** = read through the WebFetch tool, which summarises long pages (quotes checked where given); **snippet** = search-result text only; **blocked** = refused.

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AE01 | SEC EDGAR full-text search (efts), ~20 queries | 2026-09-22 | https://efts.sec.gov/LATEST/search-index?q=%22on-time%20in-full%22&forms=10-K,10-Q | page extraction (hit lists); several queries returned HTTP 500 | Which filings mention OTIF, fines, chargebacks, customer deductions |
| N-AE02 | Crown Crafts, Form 10-K FY ended 30 Mar 2025 (copy on annualreports.com) | filed 2025-06-25 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_CRWS_2025.pdf | full PDF | Schedule II; Note 2 allowance text; Walmart 47%, Amazon 19%; net sales $87,250K / $87,632K |
| N-AE03 | Crown Crafts, Form 10-K FY ended 29 Mar 2026 (EDGAR R pages) | filed 2026-06-24 | https://www.sec.gov/Archives/edgar/data/25895/000143774926021496/R12.htm (also R4, R14, R16) | page extraction | Allowance charged $5,794K; net sales $82,266K; Walmart 40%, Amazon 17% |
| N-AE04 | Lifetime Brands, Form 10-K FY2025 (EDGAR R pages and main document) | filed 2026-03-12 | https://www.sec.gov/Archives/edgar/data/874396/000087439626000008/R25.htm (also R10, R11, lcut-20251231.htm) | page extraction | Anticipated customer deductions additions; net sales $647.9M; customer shares |
| N-AE05 | Hamilton Beach Brands Holding, Form 10-K FY2025 (copy on annualreports.com) | 2026 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_HBB_2025.pdf | full PDF | Revenue $606.9M; Walmart 29%, Amazon 19%; variable consideration text; no amounts |
| N-AE06 | JAKKS Pacific, Form 10-K FY2025 (EDGAR R pages) | filed 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1009829/000118518526000723/R53.htm (also R12) | page extraction | Target 26.6%, Walmart 26.1%; co-op 1-30% of gross sales |
| N-AE07 | Owlet, Form 10-K FY2025 (EDGAR R pages) | filed 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1816708/000181670826000018/R37.htm (also R5, R9) | page extraction | Revenue $105.7M; top three customers 67% |
| N-AE08 | Summer Infant, Form 10-K FY2021 | filed 2022-03-17 | https://www.sec.gov/Archives/edgar/data/1314772/000110465922034637/sumr-20220101x10k.htm | page extraction (partial) | Amazon 38%, Walmart 24%, Target 18% |
| N-AE09 | Singing Machine, Form 10-K FY2023 | filed 2023-07-14 | https://www.sec.gov/Archives/edgar/data/923601/000149315223024594/form10-k.htm | page extraction (partial) | Returns $5.0M (12.7%); co-op $2.3M; top five 89% |
| N-AE10 | Funko, 8-K exhibit 99.1 (Q4 2018 results) | 2019-02-28 | https://www.sec.gov/Archives/edgar/data/1704711/000156459019005468/fnko-ex991_6.htm | page extraction | "increase in non-compliance chargebacks" (no amount) |
| N-AE11 | Energizer, 8-K press release (Q4 FY2020) | 2020-11-12 | https://www.sec.gov/Archives/edgar/data/1632790/000163279020000082/enrpr93020.htm | page extraction | "increased retailer fines and penalties" (no amount) |
| N-AE12 | Prestige Brands – GEODIS Logistics warehouse agreement, 10-Q exhibit 10.3 | eff. 2024-10-01; filed 2024-11-07 | https://www.sec.gov/Archives/edgar/data/1295947/000129594724000032/exhibit103-prestigexam3t.htm | page extraction | Compliance-chargeback liability clause (cap and threshold redacted) |
| N-AE13 | Instant Brands, Declaration of Adam Hollerbach, Doc 39, Case 23-90716 (Bankr. S.D. Tex.) | 2023-06-13 | https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.39.0.pdf | full PDF | Customer programmes: off-invoice allowances incl. non-compliance ~$1.6M/month; $105M customer obligations 2022 |
| N-AE14 | Miller v. ANConnect, Adv. 18-50633 (Bankr. D. Del.), Doc 295, Declaration of Jay Maier with exhibits | 2023-02-27 | https://storage.courtlistener.com/recap/gov.uscourts.deb.173722/gov.uscourts.deb.173722.295.0.pdf | full PDF (text pages) | Alchemy statement summary: $27.0M invoiced; shipping variances $54,048 (0.20%) |
| N-AE15 | JD Global Sales v. JEM D International Partners, D.N.J. 2:21-cv-19943, Doc 146 (opinion) | 2026-02-23 | https://storage.courtlistener.com/recap/gov.uscourts.njd.487061/gov.uscourts.njd.487061.146.0.pdf | full PDF | Subpoena for Walmart monthly OTIF reports (no amounts) |
| N-AE16 | CourtListener RECAP and opinion search API, ~25 queries | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=r&q=%22OTIF%22%20Walmart | full (API results) | Case discovery; absence of supplier-retailer deduction ledgers |
| N-AE17 | SPS Commerce, 8-K exhibit 99.1, "SPS Commerce Acquires SupplyPike" | 2024-08-01 | https://www.sec.gov/Archives/edgar/data/1092699/000109269924000066/ex991.htm | page extraction | ~$8.0M revenue FY2024, ~$25.0M FY2025; price |
| N-AE18 | SPS Commerce, "SPS Commerce to Acquire Carbon6 Technologies" (GlobeNewswire) | 2025-01-02 | https://www.globenewswire.com/news-release/2025/01/02/3003735/12398/en/SPS-Commerce-to-Acquire-Carbon6-Technologies.html | page extraction | ~$40.0M FY2025 revenue expected; ChargeGuard (1P), Seller Investigators (3P) |
| N-AE19 | SPS Commerce, Form 10-Q Q3 2025 | filed 2025-11 | https://www.sec.gov/Archives/edgar/data/1092699/000109269925000064/spsc-20250930.htm | page extraction | No separate revenue or customer figures for SupplyPike/Carbon6 |
| N-AE20 | SPS Commerce Q1 2026 earnings call transcript (Motley Fool); Yahoo summary | 2026-04-30 | https://www.fool.com/earnings/call-transcripts/2026/04/30/sps-commerce-spsc-q1-2026-earnings-transcript/ | page extraction; secondary | Amazon policy "reduce the amount we can recover"; trough; $19.99 fee; 1P flat, 3P −400 |
| N-AE21 | SPS Commerce Q2 2026 earnings call transcripts (Motley Fool; Investing.com) | 2026-07-30 | https://www.fool.com/earnings/call-transcripts/2026/07/30/sps-commerce-spsc-q2-2026-earnings-call-transcript/ | page extraction; secondary | 3P sale $9.5M, loss $23.5M, 7,300 customers, $10.5M H2 revenue; Chosen Foods ~30%; Owlet $1.4M |
| N-AE22 | Talk Business & Politics, "Rogers-based SupplyPike acquired in a $206 million cash, stock deal" | 2024-08 | https://talkbusiness.net/2024/08/rogers-based-supplypike-acquired-in-a-206-million-cash-stock-deal/ | page extraction | ">500 retail suppliers"; ~100 employees; "8% and 10% of deductions are erroneous" |
| N-AE23 | Talk Business & Politics, "SupplyPike reveals revenue recovery team" | 2025-12 | https://talkbusiness.net/2025/12/supplypike-reveals-revenue-recovery-team/ | page extraction | 152 employees in Rogers; SPS Revenue Recovery formed |
| N-AE24 | SupplyPike, "SupplyPike's $1 Billion Milestone" (Wayback copy) | 2025-02-24 | https://web.archive.org/web/2025id_/https://www.supplypike.com/whats-new/supplypikes-1-billion-milestone | full (archived HTML) | ">$1 billion" recovered; Bissell ">$1 million", "win rate by 20%" |
| N-AE25 | SupplyPike, "SupplyPike: 2024 Unboxed" (Wayback copy) | 2024-12-19 | https://web.archive.org/web/2025id_/https://www.supplypike.com/whats-new/supplypike-2024-unboxed | full (archived HTML) | "over $900 million"; Home Depot, Lowe's, CVS added |
| N-AE26 | SPS Revenue Recovery product pages (main and 1P) | read 2026-09-22 | https://www.spscommerce.com/products/revenue-recovery/1p/ | page extraction | "$2B+"; "up to 75%"; Owlet $1.4M; retailers covered |
| N-AE27 | SPS Supply Chain Source, "The Impact of Retailer Deductions" | updated 2025-11-03 | https://www.spscommerce.com/community/articles/the-impact-of-retailer-deductions | page extraction | 20-30% disputed; 40% of disputed won; Eagle Foods $400K |
| N-AE28 | SPS, Bissell case study | undated | https://www.spscommerce.com/resources/bissell-case-study/ | page extraction | 6,000 deductions under the threshold; 99.98% clear rate |
| N-AE29 | SPS "Benchmarking Your Deductions: Walmart" (sign-in required) and SupplyPike Walmart page (search results) | — | https://www.spscommerce.com/community/unlock-your/benchmarking-your-deductions-walmart | blocked (sign-in); snippet | "5.8% of their invoices" (snippet only) |
| N-AE30 | STAT Recovery Services, press release (GlobeNewswire) | 2026-06-18 | https://www.globenewswire.com/news-release/2026/06/18/3314420/0/en/why-deduction-management-software-alone-leaves-millions-on-the-table-and-what-retail-suppliers-are-doing-instead.html | page extraction | $1B+, 500+ suppliers, $500B analysed, win rates; HRG 60-70% (search snippet from the same search) |
| N-AE31 | HighRadius Finsider, "Deductions Metrics that Matter" (V. Taneja) | 2023-11-15 | https://www.highradius.com/finsider/deduction-metrics-enterprises/ | page extraction | $22M and ~11,000 a month; 5-10% invalid; 10-20% of revenue; 76% auto-write-off ≤$100; 41 days; 20 a day |
| N-AE32 | iNymbus, chargeback management software page | read 2026-09-22 | https://www.inymbus.com/chargeback-management-software | page extraction | 8-15 min; 3,000 a quarter; 400 hours; $5.28 vs ~$1 |
| N-AE33 | iNymbus pricing (search results) | — | https://blog.inymbus.com/10-best-dispute-management-software-for-cpg | snippet | $0.40-0.70 per claim |
| N-AE34 | ClearChain, FAQ | read 2026-09-22 | https://useclearchain.com/faq | page extraction | $5,000 a month; 3x guarantee; $5M+ clients; 200-600 disputes a quarter; 94%; contingency 20-30% |
| N-AE35 | Eva, "Amazon Vendor Deductions Recovery" | read 2026-09-22 | https://eva.guru/services/vendor-funds-recovery/ | page extraction | 20% commission (10% in FAQ) |
| N-AE36 | Threecolts Margin Pro, vendor deduction recovery | read 2026-09-22 | https://www.threecolts.com/margin-pro/vendor-deduction-recovery | page extraction | 15-25%; $1M+ minimum; $360M+ |
| N-AE37 | OverDeduct, "7 best CPG & retail deduction recovery services" | 2026-08-08 | https://www.overdeduct.com/compare/best-cpg-retail-deduction-recovery-services | page extraction | "commonly 25–35%" |
| N-AE38 | OverDeduct, "How much do CPG brands lose to deductions?" | 2026-08-04 | https://www.overdeduct.com/benchmarks/cpg-deduction-benchmark | page extraction | Ranges; "No public industry-wide benchmark exists" |
| N-AE39 | Glimpse seed-round release (Food Industry Executive; search summary) | 2025-04 | https://foodindustryexecutive.com/2025/04/glimpse-secures-10m-to-automate-deduction-management-for-cpg-brands/ | snippet | "up to 3 percent"; 4-5x ROI; 125+ brands |
| N-AE40 | Quadient blog (N. Dwyer), citing the CRF Benchmarking Report | 2020-10-29 | https://www.quadient.com/en/blog/power-deductions | page extraction | $97 per deduction; 90 days; 60%; 85% merited |
| N-AE41 | Claimlane, "Deduction Management for Suppliers" | 2026-07-06 | https://www.claimlane.com/resources/blog/deduction-management-retail | page extraction | Illustrative €20M model |
| N-AE42 | Tahiti North, "Amazon Shortage Claim Disputes: 2026 Guide" (R. Antolin) | 2026-07-11 | https://tahitinorth.com/insights/amazon-shortage-claim-dispute-guide | page extraction | 1-3% of invoiced value (5-10% with ASN problems); win rates are "marketing" |
| N-AE43 | PR Newswire, "Attain Consulting Group Releases Report on Customer Deductions" | 2015 | https://www.prnewswire.com/news-releases/attain-consulting-group-releases-report-on-customer-deductions-300200008.html | page extraction | Survey history (CRF → Attain 2015); no figures |
| N-AE44 | Attain Consulting Group deck on RVCF site (COVID-era survey) | 2020 | https://www.rvcf.com/resource/resmgr/docs/Attain_Consulting_Group_COVI.pdf | blocked (403) | — |
| N-AE45 | APQC, cost per adjustment/deduction measure | — | https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/total-cost-perform-processes-process-1 | blocked (403 / Cloudflare) | Measure exists; values not read |
| N-AE46 | IOFM, "Understanding and Managing Customer Deductions" | — | https://www.iofm.com/ar/whitepapers/understanding-and-managing-customer-deductions | blocked (403) | — |
| N-AE47 | BLS OEWS May 2025 via public API v1 (series OEUN000000000000013204101/03/08, …043301101/03/08, …043303101/03/08, …043405101/03) | 2026 release | https://api.bls.gov/publicAPI/v1/timeseries/data/ | full (API) | Employment, mean and median hourly wages |
| N-AE48 | Census Bureau, SUSB 2022 by enterprise receipts size (6-digit NAICS; sector large sizes) | released 2025-04-10 | https://www2.census.gov/programs-surveys/susb/tables/2022/us_6digitnaics_rcptsize_2022.xlsx ; https://www2.census.gov/programs-surveys/susb/tables/2022/us_naicssector_large_rcptsize_2022.xlsx | full (XLSX) | Firm counts by receipts class |
| N-AE49 | McKinsey, "Deliver on time or pay the fine" (Kuntze, Martin, Regnier, Silva) (Wayback copy) | 2018-09-06 | https://www.mckinsey.com/capabilities/operations/our-insights/deliver-on-time-or-pay-the-fine-speed-and-precision-as-the-new-supply-chain-drivers | full (archived HTML) | ">$5 billion a year"; "3 percent of the purchase price"; one margin point |
| N-AE50 | McKinsey, "Defining 'on-time, in-full' in the consumer sector" (Wayback copy) | 2019-06-13 | https://www.mckinsey.com/capabilities/operations/our-insights/defining-on-time-in-full-in-the-consumer-sector | full (archived HTML) | 4% >12 h late; 25% >2 h early; survey of 24 |
| N-AE51 | Forbes, S. Banker, "Walmart Lowers Its Shipping Requirements, But Suppliers Still Struggle" (Wayback copy; original of N-S13) | 2024-02-01 | https://www.forbes.com/sites/stevebanker/2024/02/01/walmart-lowers-its-shipping-requirements-but-suppliers-still-struggle/ | full (archived HTML) | 90%/95% from 1 Feb 2024; 0.16% of COGS; "over a billion dollars per year" |
| N-AE52 | Supply Chain Dive (Mar 2019) and SupplyChainBrain (R. Bowman, 13 May 2019) on Walmart OTIF goals | 2019 | https://www.supplychaindive.com/news/walmart-on-time-in-full-87-suppliers/550083/ ; https://www.supplychainbrain.com/blogs/1-think-tank/post/29697-walmart-is-tightening-otif-requirements-can-suppliers-step-up-their-game | page extraction | 85% (2018) → 87% truckload, 70% LTL, in-full 95%/97.5% (2019) |
| N-AE53 | Triumph case ("Shipper avoids $220K in OTIF fines"); ODW Logistics case | 2024 | https://triumph.io/blog/shipper/shipper-avoids-220k-in-otif-fines/ ; https://www.odwlogistics.com/resources/retail-consolidation-reduces-otif-fines-to-0 | page extraction | $220K avoided in Q1 2024; OTIF to 98.5% |
| N-AE54 | SPS Supply Chain Source, "Disputing OTIF at Walmart" | — | https://www.spscommerce.com/community/articles/disputing-otif-at-walmart | page extraction | No figures; 13-month reach |
| N-AE55 | SupplyPike pricing (search results; pricing page timed out, HTTP 504) | — | https://www.supplypike.com/deductions/pricing ; https://www.softwaresuggest.com/supplypike | snippet | $810/month start; $99/month for new Walmart suppliers; flat rate per retailer by size |
| N-AE56 | Once Upon a Farm, Form 10-K FY2025 | filed 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1696556/000169655626000004/ofrm_10-k_2025.htm | page extraction | $240.7M net sales; four customers 61%; no deduction amounts |
| N-AE57 | Edible Garden, Form 10-K FY2025 | filed 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1809750/000147793226001867/edbl_10k.htm | page extraction | Five customers 88.2%; Meijer fixture deductions ~$800K |
| N-AE58 | Del Monte Foods first-day declaration (Doc 19, Bankr. D.N.J. 25-16984) and Tupperware first-day declaration (Doc 2, Bankr. D. Del.) | 2025-07-01; 2024-09-17 | https://storage.courtlistener.com/recap/gov.uscourts.njb.1128266/gov.uscourts.njb.1128266.19.0_3.pdf ; https://storage.courtlistener.com/recap/gov.uscourts.deb.194296/gov.uscourts.deb.194296.2.0_1.pdf | full PDF | No customer-programme amounts in the declarations |
| N-AE59 | Alkaline Water Co., Form 10-K FY2023 | filed 2023-08-17 | https://www.sec.gov/Archives/edgar/data/1532390/000106299323016652/form10k.htm | page extraction (truncated) | No amounts found |
| N-AE60 | Scott's Liquid Gold, Form 10-Q Q3 2022 | filed 2022-11-14 | https://www.sec.gov/Archives/edgar/data/88000/000095017022024986/slgd-20220930.htm | page extraction (truncated) | Net sales only; no amounts found |

Downloads are in the session scratchpad (`…/scratchpad/c19/`), not in the project folder.

---

## 11. Could not access, or not found

**Could not access:**
- **SEC EDGAR direct download**: HTTP 403 without a declared contact ("Undeclared Automated Tool"). Not overridden (hard rule). Filings were read through WebFetch, whose extraction of long main documents is **truncated** (Summer Infant, Singing Machine, Alkaline Water, Scott's Liquid Gold); per-note R pages worked. EDGAR full-text search returned HTTP 500 on several queries and EDGAR browse returned 503 once.
- **annualreports.com**: two PDFs downloaded (Crown Crafts FY2025, Hamilton Beach FY2025); then HTTP 429/503 and connection refused. Lifetime, JAKKS, Owlet, Honest, Zevia, Lifeway, Bridgford, Jewett-Cameron, Emerson Radio, Koss, Vita Coco, Laird, Coffee Holding, Hooker, Flexsteel not retrieved this way.
- **APQC** cost-per-deduction benchmark (Cloudflare 403); **IOFM** whitepaper and webinar pages (403); **Attain/RVCF** COVID survey deck (403); **Attain's survey reports** (email required, not given); **CRF 2021 and 2023 deduction survey reports** (participants only).
- **SPS "Benchmarking Your Deductions: Walmart"** deck (sign-in); **SupplyPike pricing page** (504); **G2 reviews**, **Inc. 5000 profile**, **Arkansas Business**, **5newsonline** (403); **Carbon6 blog** and **Woodridge** pages (404); **MIT DSpace** search (404).
- **Customer-programmes motions** of Tupperware, BowFlex and Del Monte: listed in RECAP without PDFs; claims-agent sites not tried.
- **Pegasus Integrated Consulting v. Rue 21** (S.D.N.Y. 2007): scanned images, no text layer; not OCR'd.

**Not found (searched, appears not to be public):**
- **Any small or mid-sized supplier's filing that states OTIF fines, compliance chargebacks or shortages as a separate amount.** Filings give totals (all deduction types) and customer concentration only.
- **A supplier-versus-retailer court record with a remittance or deduction ledger** showing share disputed, share recovered and days to resolution.
- **Walmart's total OTIF fines; the share of Walmart OTIF fines reversed on dispute; the share that is disputable.**
- **A public distribution of small suppliers' OTIF scores.**
- **Neutral counts of deductions per supplier and average deduction size**; minutes to research (as distinct from file) a deduction; **hours to set up a retailer portal.**
- **Target's fifth-dispute fine amount.**
- **Measured win rates or recoveries before and after any 2024-26 retailer rule change.**
- **SupplyPike's customer count after the acquisition**, and SPS's 1P revenue-recovery revenue as a separate line.
- **Instant Brands' 2022 net sales** in the court record (so no rate was computed for its $1.6M a month).
