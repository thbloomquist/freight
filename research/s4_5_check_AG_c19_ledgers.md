# S4.5 check AG: real deduction documents for suppliers to big-box retailers (C-19)

- **What this is:** input to **S4.5, the profitability check**, for **C-19, retailer on-time-in-full (OTIF) fines and non-trade deductions, for suppliers with sales of $500M or less selling to big-box retailers**, run 01. This check's slice is **real transaction-level documents**: court and bankruptcy records, lender documents and receivables-finance disclosures that show actual deductions, chargebacks or dilution for real suppliers. The aim was to **measure** the rates in the per-customer model (`selection_runs/run-01/4_kill_conditions.md` §4.2-§4.3), not take them from surveys or vendors:

  > recovered = big-box sales × **non-trade deductions %** × **invalid share** × **recovered share**; fee = 25% of that; cost = deductions × 5 min triage + invalid ones × 20 min dispute, at $33.70/h (US collector) or $12/h (offshore), + $600 fixed.

- **Date:** 2026-09-22. Everything here was accessed on 2026-09-22.
- **Status:** input only. **It decides nothing.** No verdict, price, score or kill line is set or moved here. Readings are **[our call]** and sit in §7, "For the coordinator (not a call)".
- **Labels:**
  - *verified*: read at the source (a court PDF downloaded from CourtListener's free RECAP store, quoted with docket, document and page).
  - *assumed*: a vendor claim (always), a search snippet, a secondary summary, a blocked page.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
  - Vendor figures are kept apart from neutral ones. This check found almost none; it is about documents.
- **New source IDs:** N-AG01 to N-AG70 (§9).
- **Not redone here (cited by ID):** check AE (`s4_check_AE_c19_money.md`): the supplier 10-K register (Crown Crafts, Lifetime Brands, Hamilton Beach, JAKKS, Owlet, Summer Infant, Singing Machine; N-AE02 to N-AE09), the *Miller v. ANConnect* ledger (0.20% shipping variances, N-AE14), the Instant Brands first-day declaration (~$1.6M a month of off-invoice allowances, N-AE13), *JD Global v. JEM D* (N-AE15), the Prestige Brands-GEODIS chargeback clause (N-AE12), CRF 2018 (N-N29), McKinsey (N-AE49), Uber Freight's 0.16% (N-AE51). Check U (`s5_check_U_retailer_position.md`): retailer rules and dispute windows.
- **Hard rules kept:** no identity in any request. CourtListener's search API and its storage PDFs were called with plain curl (no user-agent contact, no account). SEC EDGAR full-text search was read only through the WebFetch tool. No portal, form or account was used. Downloads are in the session scratchpad (`…/scratchpad/c19_s45/ag/`), not in the project folder.

**Words used here:**
- **Deduction / chargeback:** money a retailer takes off what it pays the supplier. **Trade** deductions are for agreed promotions (co-op, markdowns, rebates, placement, "digital" fees) and are out of scope for C-19. **Non-trade** deductions are fines and claims: OTIF, late or early delivery, advance ship notice (ASN), label and routing fines, shortages, pricing errors. C-19 works on these.
- **Dilution:** a lender's word for everything that reduces an invoice between billing and cash: returns, credits, discounts, deductions of all kinds, write-offs. It is **always a mix of trade and non-trade**.
- **Borrowing base:** the amount an asset-based lender will advance against receivables and inventory. **Ineligible accounts / dilution reserve:** the parts of receivables the lender refuses to lend against, partly because of expected deductions.
- **DIP (debtor-in-possession) financing:** a loan to a company in Chapter 11; its **budget** is filed with the court. **MOR (monthly operating report):** the monthly financial report a Chapter 11 debtor files. **SOFA (statement of financial affairs):** a sworn bankruptcy form that states the debtor's gross revenue for the last two years.
- **First-day declaration:** the sworn statement a company files on the day it enters Chapter 11. **Customer programs motion:** the motion asking the court to let the company keep honoring customer deductions and allowances.
- **3PL:** third-party logistics provider (a contract warehouse). **RECAP:** CourtListener's free archive of federal court PDFs that someone has already bought from PACER.
- **Big-box retailers:** Walmart (with Sam's Club), Target, Home Depot, Lowe's, Costco, Kroger, Amazon buying as a retailer (1P).

---

## 1. Summary inputs table

"Sales" means the supplier's gross sales for the same period unless marked otherwise.

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Compliance fines a discount retailer collected from all its vendors, % of the retailer's sales** (the retailer side of the same money) | **0.24%** (ShopKo FY2016: $5.73M on $2,343M) | **0.29%** (FY2017: $6.55M on $2,286M) | **0.32%** (FY2018: $6.56M on $2,041M) | *verified* (sworn SOFA); rates **[our calc]** | N-AG63 |
| Same, as a share of what the retailer paid vendors (≈ the vendors' sales to it) | **0.33%** | **0.38-0.41%** | **0.46%** | **[our calc]** on an assumed merchandise cost of 70-75% of retail sales **[our call]**; sales include pharmacy and optical, so the rate on general-merchandise vendors is likely higher | N-AG63 |
| Mix of those fines by type (FY2016-18) | ASN audit 7.5-9.0% | early/late delivery **55-62%**; fill rate 9-24% (rising) | other "Vendor Penalties Chargebacks" 14-20% | *verified*; shares **[our calc]** | N-AG63 |
| **Non-trade chargebacks, % of sales (small supplier, measured)** | **0.20%**: *ANConnect* ledger, "Shipping Variances", home video into Walmart/Sam's/Best Buy, 2011-15 (already known) | **1.20%**: M Design Village, a ~$19-24M importer of nursery furniture selling to Walmart, Target, Amazon, Wayfair: "Chargebacks" $13,688.77 + "Amazon - Chargebacks" $14,382.18 on merchandise sales of $2,337,843.99, 18 Nov-31 Dec 2024 (holiday weeks, one period) | — | *verified* (court PDFs); rates **[our calc]**; "non-trade" is **[our call]** from the ledger's separate trade lines | N-AE14, N-AG09 |
| Same, Amazon line alone | — | **0.62%** of the supplier's **total** merchandise sales (Amazon's share of its sales is not stated, so the rate on Amazon sales is higher) | — | *verified*; **[our calc]** | N-AG09 |
| **OTIF fines at a large supplier in a supply crisis** | — | Revlon: OTIF "penalties which exceeded **$1.2 million in the month of May** alone" (2022) = **0.75%** of its average monthly global net sales in Q1 2022 | — | *verified*; rate **[our calc]**; Revlon is far above $500M and was short of stock | N-AG14 |
| OTIF and compliance fines from one 3PL failure (no sales base) | — | Just Play (toys, Walmart its largest customer): ~**$476,000** of "chargebacks" + a **$550,000 Walmart penalty**, 2019, recovered from the 3PL at trial | — | *verified* (appellee brief quoting trial testimony) | N-AG15, N-AG16 |
| **All-type deductions ("dilution"), % of gross sales** | **3.7-5.2%**: Instant Brands' ~$1.6M a month of off-invoice allowances (trade + non-compliance) ÷ the main US entity's gross revenue (an upper bound, see §3.3) | **5.2%**: M Design Village, every customer-related line (trade, returns, damages, chargebacks) | **20.0%**: E. Gluck (Armitron watches), January 2026, "Dilution" $617,793 on gross sales $3,088,967 (post-holiday month, in Chapter 11) | *verified*; rates **[our calc]** | N-AG10, N-AE13, N-AG09, N-AG03 |
| **Ineligible and dilution reserves, % of receivables** | **10.9%** (E. Gluck, forecast, 9 Jan 2026) | **12.8-17.5%** (E. Gluck, weekly forecasts, Jan-Feb 2026) | **23.8%** (E. Gluck, actual, 9 Jan 2026) | *verified*; **[our calc]** | N-AG02 |
| "Unapplied payments and chargebacks", % of receivables | — | **8.3%** (E. Gluck, aging at 31 Jan 2026: $721,267 of $8,733,520) | — | *verified*; **[our calc]** | N-AG03 |
| **Lender's normal-dilution threshold** (contract term, not a measurement) | — | **5.0%** of gross receivables, trailing 12 months, in two credit agreements (E. Gluck 2021; Corsicana Bedding 2022 DIP): above it the lender reserves | — | *verified* | N-AG06, N-AG29 |
| **Dilution by retailer** | — | **not found** in any public document (no filled borrowing base certificate with per-customer dilution was found) | — | — | §5 |
| **Deduction count and average size** | — | **not found** in any public document | — | — | §2, §8 |
| **Invalid, disputed and recovered shares** | — | **not found**. The only real dispute record is labour, not outcomes (next row) | — | — | §3.1 |
| **Hours spent disputing, one real case** | 8.0 h in Dec 2025 downloading Amazon remittance advices and "analyzed the AMZ Chargebacks" | **23.0 h in March 2026** for one Amazon dispute round (14.0 h investigating and building "the list of invoices to dispute", 6.0 h filing, 3.0 h follow-up), E. Gluck's turnaround advisers | + 3.0 h mixed; 4.5 h "AR reconcile - … chargebacks" in April | *verified* (fee statements); totals **[our calc]**; count and value of disputes not stated | N-AG07; CSV §2 |
| Contract caps and allowances seen in court records | 2% damage allowance off every invoice (Bed Bath & Beyond, 2011-15); 2% returns allowance (Costco, via Slam Brands, 2009-10) | J.C. Penney buyer allegedly promised to cap late-shipment and label chargebacks at **5% of invoice** (2002) | 3PL contracts split both ways: CaseStack disclaims "any chargebacks or other fees, fines, or penalties"; FitzMark paid them in the course of dealing | *verified*; the J.C. Penney promise is an allegation | N-AG18 to N-AG21 |

**One-line reading [our call]:** two sworn records now bracket the non-trade rate from both sides. **From the retailer's side**, ShopKo, a $2.0-2.3B discount chain, booked vendor compliance fines (early/late, fill rate, ASN, other chargebacks) of **0.24-0.32% of its sales, roughly 0.33-0.46% of what it bought**, inside CRF's ¼-½% median. **From a supplier's side**, the one small-supplier ledger that splits chargebacks from trade lines puts **non-trade chargebacks at about 1.2% of sales** for six holiday weeks, two to five times CRF's median and six times the older *ANConnect* ledger; everything else public is **all-type dilution (5-20% of sales)**, which mixes in trade, returns and damages and cannot be used for C-19. **No public document shows the invalid share, the recovered share, the deduction count or the average size**, so the decisive term in the kill test is still unmeasured.

---

## 2. Transaction-level datasets: what exists and what was built

**No public transaction-level list of retailer deductions was found** (no remittance advice, EDI 812/820 file, Retail Link or Vendor Central export, or deduction ledger with reason codes for a real supplier to a big-box retailer). The nearest things found, and what was extracted:

| Dataset | What it is | Rows | Real? | File |
|---|---|---|---|---|
| **E. Gluck adviser time entries on chargebacks** | Every time entry in the chief restructuring officer's fee statements that names chargebacks, remittances or disputes, Dec 2025-Apr 2026, with date, person, hourly rate, hours, amount, task and the text as filed, plus a flag (analysis / dispute preparation / filing / follow-up / mixed) **[our call on the flag]** | 28 | yes (*verified*, Docs 107, 133, 135, 156) | `…/scratchpad/c19_s45/ag/egluck_chargeback_time_entries.csv` |
| **M Design Village customer-deduction lines** | The P&L lines for sales, trade allowances, chargebacks, Amazon chargebacks, damages and returns for 18 Nov-31 Dec 2024, with our trade / non-trade tag **[our call]** | 15 | yes (*verified*, Doc 101 attaching the first MOR) | `…/scratchpad/c19_s45/ag/mdesign_pl_2024-11-18_to_12-31.csv` |
| **ShopKo vendor-fine income by type** | The retailer's sworn "non-business revenue" lines for early/late penalties, fill-rate penalties, ASN audit discrepancies, other vendor penalty chargebacks and accounts-payable audit income, three fiscal years, plus its sales | 21 | yes (*verified*, Doc 10) | `…/scratchpad/c19_s45/ag/shopko_vendor_fine_income_fy2016-2018.csv` |
| WYNIT distributor → vendor statement (Elevation Lab) | A consumer-electronics distributor's chargebacks to one of its vendors (returns, freight, currency fees), 2015-17; scanned, read by OCR | ~30 | yes, but **distributor-to-vendor, not retailer-to-supplier**; no non-compliance lines on this vendor | not extracted (out of scope) |

(Full folder: `/tmp/claude-1000/-home-teddyb-Documents-personal-bio-freight/6bedcea0-f02f-4f5b-807a-a6a445a1bd80/scratchpad/c19_s45/ag/`.)

**What the time-entry file shows [our calc]:**
- **December 2025:** 8.0 hours at $250/h by a senior analyst, five sessions of 1.5-2.0 h: "Downloaded the remittance advices from the Amazon portal and analyzed the AMZ Chargebacks". One 2.0 h entry at $500/h reconciles Amazon marketing budget against actual chargebacks "to determin reserve".
- **February 2026:** 11 entries of 0.5-1.0 h (9.5 h in all) of "Daily phone calls and emails regarding amazon sales, promo, chargebacks" — **mixed** with other work, so not counted.
- **March 2026, one dispute round with Amazon:** 23.0 hours, $9,150 at $300-550/h (blended ≈ **$398/h**):
  - 14.0 h investigating and building the list: 11.0 h by the analyst, "Reviewed the AMZ payables/ chargebacks by invoice by agreement and prepared the list of invoices to dispute" (and an update of it), and 3.0 h by the managing director, "Continued investigating on Amazon Chargebacks";
  - 6.0 h: "Filed disputes on Amazon Chargebacks" and "Searched and created copies of AMZ remittance advices for each disputed AMZ chargeback and submitted the disputes on the portal";
  - 3.0 h: following up and "Reviewed Amazon Feedback on Disputes".
- **April 2026:** 4.5 h "AR reconcile - AX issue chargebacks".
- **Not stated:** how many chargebacks were disputed, their value, or what Amazon paid back. So the file gives **time per round, not time per deduction** [our call].

---

## 3. AG1 · Bankruptcy records (suppliers to big-box retailers, and one retailer)

### 3.1 E. Gluck Corporation (Armitron watches; Bankr. S.D.N.Y. 25-12683, filed 1 Dec 2025) — the richest supplier record found

**Who:** "an importer of time pieces and accessories sold to Amazon, department stores, price clubs, mass merchants and off-price retailers" (Doc 64-2, p. 4). **Gross revenue $86,611,285 in 2024** and $65,169,671 for January-October 2025 (SOFA, Doc 29, p. 1) (*verified*, N-AG05). Inside the segment.

**Customer mix, actual sales in the six weeks to 9 Jan 2026** (Doc 64-2, p. 6, *verified*; shares **[our calc]**):

| Customer | Actual sales | Share |
|---|---|---|
| Amazon | $5,918,824 | 51.1% |
| Walmart | $885,785 | 7.7% |
| Ross, Nordstrom Rack, Burlington (off-price) | $1,774,019 | 15.3% |
| Macy's, Kohl's | $447,273 | 3.9% |
| International and other | $2,547,291 | 22.0% |
| **Total** | **$11,573,192** | 100% |

Big-box share (Amazon + Walmart) = **58.8%** **[our calc]**.

**Dilution and reserves** (all *verified*; rates **[our calc]**):

| Figure | Value | Location | Rate |
|---|---|---|---|
| January 2026 P&L: "Gross Sales" / "Dilution" / "Net Sales" | $3,088,967 / ($617,793) / $2,471,173 | Doc 100-1 (MOR), p. 4 | **dilution 20.0% of gross sales** |
| DIP forecast, 4 weeks to 6 Feb 2026: "Add: Sales" / "Less: Dilution" | $2,766,101 / $1,750,000 (weekly $650,000, $250,000, $250,000, $600,000) | Doc 64-2, p. 8 | 63% of the period's sales, or 17.4% of the $10,049,683 of receivables at the start: January is when holiday-season returns and credits land |
| Six weeks to 9 Jan 2026, variance: "Net Higher Dilution" | $280,371 more dilution than forecast | Doc 64-2, p. 5 | — |
| Borrowing base, "Ineligible & dilution reserves" on accounts receivable | actual 9 Jan 2026: $2,390,398 on $10,049,683; forecast: $1,860,000 on $17,014,967; weekly forecasts to 6 Feb: $1,483,151 on $8,613,447 … $843,618 on $6,565,784 | Doc 64-2, pp. 4, 6, 9 | **23.8%** actual; 10.9-17.5% forecast |
| Receivables aging at 31 Jan 2026: "Unapplied Payments and Chargebacks" / "Reserve for Returns & Allowances" | ($721,267) / ($2,041,627) on an aging balance of $8,733,520 | Doc 100-1, p. 1 | **8.3%** / 23.4% |
| Balance sheet at 31 Oct 2025: "Accrued sales, retruns and allowances" | ($3,300,000) on receivables of $10,377,231 | Doc 2, p. 17 | 31.8% |

**The lender's own terms** (Credit and Security Agreement with Israel Discount Bank, 22 Mar 2021, ratified in the DIP; Doc 64-1, *verified*, N-AG06):
- A dilution reserve may be set "to reflect the extent that Borrower's bad debt write-downs, discounts, returns, promotions, credits, credit memos and other cash reductions with respect to Accounts exceed **5.0% of the gross face amount** of such Accounts, as calculated on a trailing twelve month basis" (p. 58).
- Concentration: receivables from one customer count only up to 35% of eligible receivables, "except, that, such percentage shall be **fifty percent (50%)** for each of (i) Walmart, Inc. and its Affiliates, (ii) Amazon.com, Inc. and Affiliates and (iii) Costco Wholesale Corporation and its Affiliates" (p. 32).

**Reading [our call]:** E. Gluck's real dilution (20% of a January's gross sales; 24% of receivables reserved) is **four to five times the lender's 5% "normal" line**, but it is overwhelmingly returns, markdown allowances and holiday credits at department and off-price stores. **No line isolates OTIF, ASN, routing or shortage fines.** The one non-trade signal is the adviser time spent on Amazon chargebacks (§2).

### 3.2 M Design Village, LLC (nursery furniture importer; Bankr. D.N.J. 24-21406, filed 18 Nov 2024)

**Who:** a designer and importer "specializing in nursery and children's furniture" under the Oxford Baby and Soho Baby brands (p. 9). "The Products are sold to large brick and mortar retailers, such as Walmart, Target, Toys 'R' Us Canada, The Brick, City Furniture, Nebraska Furniture Mart, as well as specialty stores and major online retailers including, but not limited to, Amazon, Wayfair and Overstock" (Doc 101, Disclosure Statement, p. 10). Funded by a receivables factor (Versant). "Overnight, the Debtor again lost more than fifty (50%) percent of its sales" when Bed Bath & Beyond (buybuy BABY) liquidated in 2023. **Projected 2025 gross sales $23,713,253** (Exhibit C, p. 133). All *verified*, N-AG09.

**The first monthly operating report, 18 Nov-31 Dec 2024** (attached to Doc 101 as Doc 87, pp. 79-81 of 133, *verified*):

| Line (as printed) | Amount | % of merchandise sales **[our calc]** | Type **[our call]** |
|---|---|---|---|
| 5100 - Sales - Merchandise | $2,337,843.99 | 100% | sales (≈ **$19.4M a year** annualised **[our calc]**) |
| 5105 - Sales - Discount Allowance | ($50,939.35) | 2.18% | trade |
| 5110 - Sales - Terms Discount | ($31,773.54) | 1.36% | payment terms |
| **7516 - Chargebacks** | **$13,688.77** | **0.59%** | **non-trade (probable)** |
| **7534 - Amazon - Chargebacks** | **$14,382.18** | **0.62%** | **non-trade (probable)** |
| 7517 - Customer Promotions - Other | $24,707.16 | 1.06% | trade |
| 7524 - Digital Accrual Fee - Target | $33,999.49 | 1.45% | trade |
| 7525 - Walmart COOP | — | 0% | trade |
| 7518 - Product Damages | $16,570.70 | 0.71% | damage allowance |
| 7523 - Returned Merchandise; 7536 - Amazon - Returns; 7576 - Wayfair Returns | $13,005.43; $956.48; $3,254.58 | 0.74% together | returns |
| 7511 - Floor Model Display / Markdown; 7514 - Bad Debt / Payment Disputes | $752.85; $292.00 | 0.04% | trade; other |
| All customer-related lines | $121,609.64 | 5.20% | mixed |
| (cost reference) 7332 - EDI Expenses | $13,876.03 | 0.59% | — |

**Why "non-trade (probable)" [our call]:** the ledger books promotions, co-op, Target's digital fee, discounts, damages and returns on **separate** accounts, so the two chargeback accounts are most likely compliance, logistics and shortage chargebacks. The ledger does not say so, and nothing shows how many chargebacks there were, what share was invalid, or what was disputed.

**Limits [our call]:** one supplier; one six-week window that includes the holiday peak; booking date, not shipment date; a company in distress (late shipments are more likely); the Amazon line is a share of **total** sales, not of Amazon sales. The later monthly reports (Docs 104, 112, 126, 133, 148, 153) are **not on RECAP** (N-AG44), so no second period could be read.

### 3.3 Instant Brands (Bankr. S.D. Tex. 23-90716) — sister documents to N-AE13

- **SOFA of Instant Brands LLC** (Doc 432, pp. 20-21, *verified*, N-AG10): gross revenue "(Before Deductions and Exclusions)" **$524,423,763.92 in 2022**, $558,910,180.94 in 2021, and **$153,845,853.09 for 1 Jan-31 May 2023**.
- **The rate check AE could not compute [our calc]:** ~$1.6M a month of "Off-Invoice Allowances" (N-AE13) ÷ $30.77M a month of gross revenue in Jan-May 2023 = **5.2%**; ÷ 2022's $43.70M a month = **3.7%**.
  - **This is an upper bound on non-compliance charges, and a loose one.** The $1.6M line mixes "flat-rate and payment term discounts" and "defective allowances" with "other non-compliance charges" (N-AE13). The declaration speaks for all the debtors, while the SOFA is for one entity (the litigation trust puts company-wide revenue at "$1,035 million in 2019" and "$965 million in 2020", Doc 1385, p. 49, N-AG12), so the numerator may be wider than the denominator.
- **Not available:** the customer-programs motion (Doc 11) and its final order (Doc 80) are listed without PDFs; the claims agent's docket (Kroll) returned HTTP 403 (N-AG13). The schedules of the holding company (Doc 460) show no receivables (N-AG11).

### 3.4 Revlon (Bankr. S.D.N.Y. 22-10760) — OTIF fines in a supply crisis

- First-day declaration of the chief restructuring officer (Doc 30, *verified*, N-AG14): the company "is facing increasing penalties from its customers due to its inability to meet 'on-time, in full' ('OTIF') deliveries of its products, penalties which exceeded **$1.2 million in the month of May alone**" (¶ 118, p. 45); "retailers have begun imposing fines on the Company for failure to deliver products 'on time and in full'" (p. 5). Customers "range from well-known retailers such as Walmart, CVS, Target, Macy's, Amazon, Walgreens, TJ Maxx" (p. 19).
- Scale (same document): net sales **$2,078.7M in 2021**; **$479.6M in Q1 2022** (p. 8).
- **[our calc]:** $1.2M ÷ ($479.6M ÷ 3) = **0.75%** of an average month's global net sales. The fines come from retail customers, mostly in the US, whose share of sales is not stated here, so the rate on the fining customers' sales is higher.
- **Limits [our call]:** Revlon is four times the segment's $500M ceiling, and May 2022 was a month when it could not make enough product. It shows what OTIF fines reach **when a supplier fails to deliver**, not what a normal supplier pays. The customer-programs motion was not on RECAP (N-AG52).

### 3.5 Other bankrupt suppliers screened (no deduction figures)

| Debtor (court, case) | Sells to | Documents read | What they gave |
|---|---|---|---|
| KidKraft (Bankr. N.D. Tex. 24-80045) | Amazon, Walmart, Target | SOFA (Doc 159), schedules (Doc 161) | Receivables $4.79M face, $0.69M doubtful; no deduction lines (N-AG31) |
| Noble House Home Furnishings (Bankr. S.D. Tex. 23-90773) | Amazon, Wayfair, Target, Home Depot | first-day declaration (Doc 16), MOR (Doc 706) | none (N-AG32) |
| BowFlex (Bankr. D.N.J. 24-12364) | Amazon, Best Buy, Dick's | DIP motion (Doc 37), first-day declaration (Doc 44), interim DIP order (Doc 61) | "Dilution Reserve" defined for card receivables only; no amounts (N-AG33) |
| Basic Fun (Bankr. D. Del. 24-11432) | Walmart, Target, Amazon | combined plan and disclosure statement (Doc 221) | none (N-AG34) |
| Diamond Comic Distributors (Bankr. D. Md. 25-10308) | Walmart, Target, Amazon, Barnes & Noble | customer-programs motion (Doc 16), final DIP order (Doc 163) | obligations "de minimis"; no amounts (N-AG30) |
| Kid Brands (Bankr. D.N.J. 14-22582) | Walmart, Target, Toys "R" Us | final DIP order (Doc 504) | blank borrowing-base form; "dilution reserves" undefined in amount (N-AG35) |
| North Pacific Canners (Bankr. D. Or. 19-62584) | Walmart/Sam's, Costco | first-day declaration with credit agreement (Doc 16) | Sam's Club + Walmart receivables capped at 30% of eligible (N-AG36) |
| Corsicana Bedding (Bankr. N.D. Tex. 22-90016) | mattress retailers | DIP motion (Doc 13) | reserve "equal to 1.0% for each percentage (or portion thereof) that dilution exceeds 5.0%" (p. 172) (N-AG29) |
| GPMI Co. (Bankr. W.D. Ark. 22-00150); LDR Industries (Bankr. N.D. Ill. 14-32138); International Garden Products (Bankr. D. Del. 10-13207); Level 8 Apparel (Bankr. S.D.N.Y. 16-13164) | various; Home Depot/Lowe's (LDR, IGP), Costco (Level 8) | factoring agreement; cash-collateral motions; OCR of an affidavit | contract terms only; IGP's PDF has no text layer (N-AG37 to N-AG40) |

### 3.6 *Miller v. ANConnect* — sister documents to N-AE14

- Adversary 18-50633 docket searched for "shortage", "chargeback", "deductions", "dilution", "Walmart" (N-AG41): only Doc 295 (already used) carries the ledger. The joint pretrial order (Doc 358, 10 Jul 2026) confirms ANConnect "collected receivables from Walmart/Sam's Club, Best Buy" but gives no deduction amounts.
- The appeal appendix (D. Del. 1:24-cv-00243, Doc 20, 118 pages) holds SunTrust's 2015 credit memos on the content owner: "Alchemy experienced higher than normal 'deductions', or higher returns than anticipated", and "Actively managing sales dilution (returns)". **"Deductions" there means returns**, and the borrowing-base certificate in it is a blank form. Nothing on non-trade deductions.

### 3.7 The retailer side: ShopKo's sworn income from vendor fines (Bankr. D. Neb. 19-80075)

**Who:** ShopKo Stores Operating Co., a Midwestern discount general-merchandise chain with pharmacy and optical counters, in Chapter 11 from January 2019. Not on C-19's list of big-box retailers, but the same kind of buyer with the same kind of vendor rules. Its statement of financial affairs (Doc 10, signed by the chief executive officer, *verified*, N-AG63) lists every "non-business revenue" line for three fiscal years, **including the fines it collected from vendors**:

| Line (as printed, SOFA Part 1 Q2) | FY2016 (31 Jan 2016-28 Jan 2017) | FY2017 (29 Jan 2017-3 Feb 2018) | FY2018 (4 Feb 2018-5 Jan 2019) |
|---|---|---|---|
| Early/Late Penalties | $3,561,004.70 | $3,632,553.97 | $3,631,038.74 |
| Fill Rate Penalty | $528,991.66 | $1,371,322.92 | $1,538,303.07 |
| ASN Audit Discrepancy | $515,049.64 | $549,590.73 | $490,858.76 |
| Vendor Penalties Chargebacks | $1,123,160.57 | $992,268.89 | $897,873.08 |
| **Compliance fines, total [our calc]** | **$5,728,206.57** | **$6,545,736.51** | **$6,558,073.65** |
| A/P Internal Audit Income | $1,379,399.92 | $1,044,870.90 | $544,177.87 |
| A/P External Audit Income | $83,020.72 | $174,645.47 | $63,326.94 |
| Gross revenue from business (Part 1 Q1) | $2,343,117,696.34 | $2,285,632,876.45 | $2,040,947,487.93 (to 15 Jan 2019) |
| **Compliance fines ÷ sales [our calc]** | **0.244%** | **0.286%** | **0.321%** |
| Same ÷ an assumed purchase cost of 70% of sales **[our call]** | 0.35% | 0.41% | 0.46% |
| Accounts-payable audit income ÷ sales [our calc] | 0.062% | 0.053% | 0.030% |

Locations: sales, Doc 10 p. 16; fine lines, SOFA Part 1 Q2 attachment, pp. 27-31 of 937.

**What it shows [our call]:**
- **The first neutral, sworn measurement of the fine pool from the payer's side.** Summed over all of a $2B retailer's vendors, logistics compliance fines ran **0.24-0.32% of the retailer's sales, about 0.33-0.46% of its purchases**, rising each year. That sits inside CRF's ¼-½% median for non-trade deductions (N-N29) and above Uber Freight's 0.16% for Walmart OTIF fines alone (N-AE51).
- **Timing fines dominate:** early/late penalties were 55-62% of the total; fill-rate penalties grew from 9% to 24% as ShopKo tightened them; ASN audits 7-9%; other chargebacks 14-20%.
- **Limits:** the sales figure includes pharmacy and optical, whose suppliers are unlikely to be fined this way, so the rate on general-merchandise vendors is higher than shown; the lines are income booked, probably after any reversals; there is no split by vendor size, and nothing on how many fines were contested or reversed. **Shortage claims do not appear as a line** (they may sit inside the accounts-payable audit lines or be booked against cost of goods).
- **Only one retailer's statement in the RECAP index carries lines like these** (searches for "Fill Rate Penalty", "Vendor Penalties", "ASN Audit", "A/P Internal Audit Income", "vendor compliance" + "non-business revenue" and similar found ShopKo alone, N-AG70).

---

## 4. AG2 · Supplier-versus-logistics and supplier-versus-retailer suits

| Case | Parties and retailers | Figure or term (quoted) | Type | Label | ID |
|---|---|---|---|---|---|
| **Just Play, LLC v. FitzMark, Inc.**, S.D. Fla. 9:20-cv-80663; 11th Cir. 22-10235 | Toy maker v. its California 3PL; Walmart ("Walmart is Just Play's largest customer"), Target, Kohl's | Retailers "charge Just Play penalties (referred to as 'chargebacks') when their requirements are not complied with"; the damages expert testified to "Approximately **$476,000** in 'chargebacks,' customer penalties for FitzMark's failure to comply with shipping and labeling requirements, including delinquent or incomplete shipments" and a "**$550,000 Walmart penalty**"; "on occasions when Just Play incurred customer chargebacks, FitzMark deducted the amounts from FitzMark's invoices to Just Play"; jury award **$3,959,134** (appellee brief, Doc 29, pp. 13, 17, 28-30, 33) | non-trade (compliance and OTIF) | *verified* (brief quoting trial record); Just Play's sales not stated | N-AG15, N-AG16 |
| **Nazareth International v. J.C. Penney**, N.D. Tex. 3:04-cv-01265, Doc 31 (19 Jul 2005) | Supplier v. retailer | Alleged oral promise that J.C. Penney "would limit its chargebacks against future shipments, for late shipments or deficient UPS labels to **5 % of invoice**, and waive any other chargebacks" (p. 4) | non-trade cap (alleged) | *verified* (as an allegation) | N-AG18 |
| **Ion Audio v. Bed Bath & Beyond**, S.D.N.Y. 1:15-cv-08292, Doc 108 | Supplier v. retailer | "a damage allowance of **two percent (2%)** off each invoice, to be taken by BB&B as a deduction against invoices"; BB&B presented excess-damage claims "months, or even years, after the relevant fiscal year ended" (FY2011-15); volume rebates of 1-2.5% taken as "Volume Allowance Chargeback" (pp. 5-6, 17) | damages and trade | *verified* | N-AG19 |
| **Superwood v. Slam Brands**, W.D. Wash. 2:12-cv-01109, Doc 120 (findings of fact) | Factory v. importer selling to Costco, Target, Walmart | "a returns chargeback totaling **$37,000.00** for the Rylander items returned in excess of the **2% returns allowance**"; Costco markdowns for quality problems of $473,522.42; "less than 2000 were returned out of a total of roughly 26,000" (pp. 5, 19) | returns and markdowns | *verified* | N-AG20 |
| **CaseStack v. Korex**, N.D. Ill. 1:23-cv-00214, Doc 1-1 | 3PL v. household-products supplier; Walmart consolidation programme | 3PL terms: "in no event will CaseStack be liable for any chargebacks or other fees, fines, or penalties related to any missed pick-up or delivery appointment" (p. 25) | contract term | *verified* | N-AG21 |
| Age Group v. Regal Logistics, W.D. Wash. 2:07-cv-01303, Doc 74 | Apparel supplier v. 3PL | routing "protecting against future routing chargeback's" (no amount) | — | *verified* | N-AG22 |
| *Manty v. Elevation Lab*, Bankr. D. Minn. Adv. 18-04037 (WYNIT Distribution trustee) | Distributor v. vendor | Agreement makes vendors pay "refunds, price protection credits, non-compliance charges, advertising and marketing funds"; Exhibit B statement (OCR) shows returns, freight and currency chargebacks only; amount due $38,917.26 | distributor pass-through | *verified* (OCR) | N-AG23 |
| *Tattooed Chef* securities suit, C.D. Cal. 2:22-cv-09311, Doc 124 (¶¶ 77-79) | Frozen-food maker; Walmart, Trader Joe's, Albertsons, KeHE | Confidential witness (the only accounts-receivable specialist): "for a $100,000 payment there could be as much as **$25,000 in deductions**", mostly "discounts" and "promotions" | trade (out of scope) | *verified* (as a witness allegation) | N-AG26 |
| **Goped Ltd. v. Amazon.com**, D. Nev. 3:16-cv-00165, Doc 60 (order, 12 Feb 2018) | Scooter maker (Patmont) v. Amazon as 1P buyer | The vendor terms: a 2% damage allowance "for waiving its right to return damaged or defective goods"; 2% early-payment discount; 3% freight allowance; MDF/co-op of 5%, later 9%; and "Under the Chargebacks Agreements, Amazon could charge Patmont for **ten percent of the cost of any undelivered products**". The court found no evidence "that the chargebacks and penalties Amazon applied amounted to anything more than faithful execution of the parties' agreement" (pp. 2, 8) | non-trade rule (shortfall charge) plus trade terms | *verified* | N-AG66 |
| *In re Spectrum Brands Securities Litigation*, W.D. Wis. 3:19-cv-00347, Doc 14 (amended complaint) | Large supplier; Walmart, Home Depot, Lowe's ("40% of the Company's revenue") | Service-level agreements set "standards for delivery timing and 'fill rate'"; a former employee: "Penalties from major customers, including Home Depot, Walmart, and Lowe's, were **into the millions of dollars during 2017**", with "weekly fine-reduction meetings"; penalties applied below "90% fill rates" (pp. 8, 42, 61, 119) | non-trade (fill rate) | *verified* (as allegations); no exact amount | N-AG64 |
| *Primo Brands* securities suit, M.D. Fla. 8:25-cv-03328, Doc 82 | Water supplier | Daily "on time in full (OTIF) rates" reviewed after a merger (pp. 42, 56); no fine amounts | — | *verified* | N-AG65 |
| Groupon Goods v. EDO Trading, N.D. Ill. 1:22-cv-01609, Doc 1 | Online retailer v. vendor | Groupon's "Non-Compliance Chargeback Recovery" schedule: late drop-ship "10% of COGS + 1% of COGS per day late", missing tracking "10% of COGS", $5 a unit for wrong carrier account; $139,660 claimed for 27,932 shipments | fine schedule (not big-box) | *verified* | N-AG67 |
| Sound Around v. Friedman, S.D.N.Y. (Doc 320-52, expert report); Evolution Micro (Bankr. M.D. Fla., Amazon claim, Docs 84, 86) | Amazon | Vendor Central chargebacks and shortages described generally; Evolution Micro is an Amazon **3P** seller account balance ($118,273.89) | out of scope | *verified* | N-AG24, N-AG25 |

**Reading [our call]:**
- The **only** large non-trade dollar figures in court records come from **failures** (Just Play's 3PL collapse, Revlon's stock-out). They show that OTIF and compliance fines can reach hundreds of thousands of dollars in a few months at a Walmart supplier, **and that the money was recovered from the 3PL, not from the retailer**: a second recovery path (check AE §2.3, the GEODIS clause) now with a real case behind it.
- The contract terms seen (2% damage and returns allowances; an alleged 5% cap on late and label chargebacks; Amazon's 10% charge on undelivered goods) are **rules agreed in advance**. A court held Amazon's chargebacks to be "faithful execution of the parties' agreement" (Goped), so a dispute has to show the fine was **wrongly applied**, not that the rule is unfair.

---

## 5. AG3 · Receivables-finance disclosures (dilution)

- **What lenders write into contracts** (*verified*): a **5.0% trailing-twelve-month dilution threshold** (E. Gluck/IDB, 2021; Corsicana, 2022), and **higher concentration limits for Walmart, Amazon and Costco** (50% of eligible receivables at E. Gluck; Sam's Club + Walmart combined 30% at North Pacific Canners) because lenders treat them as the safest payers (N-AG06, N-AG29, N-AG36). These are **conventions, not measurements**.
- **SEC filings:** EDGAR full-text search for "dilution ratio" with "Walmart" returned 19 filings (Newell Brands, PetIQ, Phillips-Van Heusen, Pactiv, Murphy USA, Navistar and others), all **receivables purchase or credit agreements that define** "Dilution Ratio" or "Dilution Reserve" (read through WebFetch, N-AG47). A second search ("dilution" + "chargebacks" + "Walmart" + "borrowing base") returned 91 filings, mostly credit agreements and 10-K risk language (N-AG61). Two were opened (N-AG62):
  - **Zevia** (beverages; Walmart, Costco), amended Bank of America loan agreement, 15 May 2026: defines "Dilution Percent" as "bad debt write-downs or write-offs, discounts, returns, promotions, credits, credit memos and other dilutive items with respect to Accounts, divided by (b) gross sales", and caps Walmart/Sam's and Costco receivables at 25% of eligible each. **No value.**
  - **Tandy Brands Accessories** 10-K FY2011 (net sales $123.8M; "Walmart accounted for 48%"): "higher customer chargebacks" hurt the gifts segment's margin, and "increases in bad debt provisions and customer chargebacks" offset savings. **No amount.**
  
  **None reports a dilution value**; the monthly settlement or borrowing-base reports that carry the values are not filed.
- **Rating-agency methods and ABL field-exam write-ups:** only general pages were found (dilution = "the difference between the gross amount of invoices and the cash actually collected"; a common reserve "(Dilution % – Threshold) / (1 – Dilution %)"), with **no figures for suppliers to big-box retailers** (*assumed*, N-AG48).
- **Dilution by retailer (Walmart vs Target vs Amazon): not found anywhere public.** No filled borrowing-base certificate with a per-customer split was found; E. Gluck's is the only filled one and it reports one combined reserve.

---

## 6. Register of documents read or screened

"Read" = downloaded and searched in full; "screened" = searched for the terms without usable figures. Page numbers are PDF pages.

| # | Document | Supplier / parties | Period | Figure(s) | Where | Result |
|---|---|---|---|---|---|---|
| 1 | Doc 64-2, DIP forecast and borrowing base | E. Gluck | Dec 2025-Feb 2026 | dilution, reserves, sales by customer | pp. 4-9 | **used** |
| 2 | Doc 100, 100-1, MOR January 2026 | E. Gluck | Jan 2026 | dilution 20.0%; chargebacks in aging | 100-1 pp. 1, 4 | **used** |
| 3 | Doc 2, first-day declaration and balance sheet | E. Gluck | 31 Oct 2025 | accrued returns and allowances | p. 17 | **used** |
| 4 | Doc 29, SOFA | E. Gluck | 2023-25 | gross revenue | p. 1 | **used** |
| 5 | Doc 64-1, ratification and credit agreement | E. Gluck / IDB | 2021 | 5% dilution line; 50% concentration | pp. 32, 58 | **used** |
| 6 | Docs 107, 133, 135, 156, CRO fee statements | E. Gluck | Dec 2025-May 2026 | chargeback time entries | Doc 107 pp. 13-14, 17; Doc 133 pp. 9-10; Doc 135 pp. 12, 15; Doc 156 p. 10 | **used** (CSV) |
| 7 | Docs 3, 8-1, 32, 37, 64, 177 | E. Gluck | — | cash management, sale agreement, retention, interim DIP | — | screened |
| 8 | Doc 101 (with Doc 87 MOR) | M Design Village | 18 Nov-31 Dec 2024; 2025-29 projection | chargebacks, Amazon chargebacks, sales | pp. 10, 13, 79-81, 133 | **used** (CSV) |
| 9 | Doc 432, SOFA | Instant Brands LLC | 2021-May 2023 | gross revenue | pp. 20-21 | **used** |
| 10 | Doc 460, schedules | Instant Brands Acquisition Holdings | 2023 | — | — | screened |
| 11 | Doc 1385, litigation trust complaint | Instant Brands | 2019-21 | revenue $1,035M (2019), $965M (2020) | p. 49 | used (scale) |
| 12 | Doc 30, first-day declaration | Revlon | May 2022 | OTIF penalties > $1.2M | pp. 5, 8, 19, 45, 77-78 | **used** |
| 13 | 11th Cir. Docs 21, 29 | Just Play v. FitzMark | 2019 | $476K chargebacks; $550K Walmart penalty | Doc 29 pp. 13, 17, 28-30, 33; Doc 21 p. 22 | **used** |
| 14 | S.D. Fla. docket 9:20-cv-80663 | Just Play v. FitzMark | — | trial exhibits of chargebacks (ECF 214-66, 214-74) | — | **not on RECAP** |
| 15 | Doc 31 | Nazareth v. J.C. Penney | 2002 | 5% cap (alleged) | p. 4 | used |
| 16 | Doc 108 | Ion Audio v. Bed Bath & Beyond | FY2011-15 | 2% damage allowance; rebate tiers | pp. 5-6, 17 | used |
| 17 | Doc 120 | Superwood v. Slam Brands (Costco) | 2009-11 | 2% returns allowance; $37,000; markdowns $473,522 | pp. 5, 19 | used |
| 18 | Doc 1-1 | CaseStack v. Korex | 2023 | 3PL disclaims chargebacks | p. 25 | used |
| 19 | Doc 74 | Age Group v. Regal Logistics | 2007 | — | — | screened |
| 20 | Doc 1 (OCR of Exhibit B) | WYNIT trustee v. Elevation Lab | 2015-17 | distributor chargebacks | pp. 17-21 | screened |
| 21 | Doc 124 | Tattooed Chef securities suit | 2021-22 | up to 25% of a payment in (trade) deductions | pp. 43-44 | noted |
| 22 | Doc 320-52 | Sound Around v. Friedman | — | — | — | screened |
| 23 | Docs 84, 86 | Evolution Micro (Amazon 3P) | 2023 | — | — | screened |
| 24 | Doc 13 | Corsicana Bedding DIP motion | 2022 | 5% dilution line | p. 172 | used |
| 25 | Docs 16, 163 | Diamond Comic Distributors | 2025 | — | — | screened |
| 26 | Docs 159, 161 | KidKraft | 2024 | receivables only | — | screened |
| 27 | Docs 16, 706 | Noble House | 2023-25 | — | — | screened |
| 28 | Docs 37, 44, 61 | BowFlex | 2024 | — | — | screened |
| 29 | Doc 221 | Basic Fun | 2024 | — | — | screened |
| 30 | Doc 504 | Kid Brands | 2014 | — | — | screened |
| 31 | Doc 16 | North Pacific Canners | 2019 | 30% Sam's + Walmart cap | — | used (term) |
| 32 | Doc 9-1 | GPMI Co. | 2022 | — | — | screened |
| 33 | Doc 14-2 | LDR Industries | 2014 | — | — | screened |
| 34 | Doc 14-2 | International Garden Products | 2010 | — | — | no text layer |
| 35 | Doc 17 (OCR) | Level 8 Apparel (Costco) | 2016 | — | — | screened |
| 36 | Adv. 18-50633 Docs 221-1, 358; D. Del. Doc 20 | *Miller v. ANConnect* sister documents | 2014-16 | "deductions" = returns | appendix pp. ~17-60 | screened |
| 37 | Docs 75; 117-10 | Hain Celestial securities suit; Funko securities suit | 2016; 2019 | — | — | screened |
| 38 | Doc 16 | Diamond Comic customer programs | 2025 | — | — | screened |
| 39 | Adv. 25-01165 to 25-01169, Doc 1 | Bed Bath & Beyond plan administrator v. vendors (CHF, Himatsingka, Linon, Nishat Chunian, Tabletops) | 2023 | vendor agreements ("Collection Method: Chargeback") | — | screened |
| 40 | Doc 24; Doc 1 | National Christmas Products v. OJ Commerce; Taizhou Yuanda v. Z Outdoor Living | 2019-22 | — | — | screened |
| 41 | Doc 304-2; Doc 57-20 | Halperin v. Arawak IX; Midlab v. Wycoff | — | — | — | screened |
| 42 | Doc 1-1; Doc 209 | Emigrant v. Hanratty; Finkel v. WeVeel | — | irrelevant (tax liens; unrelated) | — | screened |
| 43 | EDGAR full-text hit list "dilution ratio" + Walmart | Newell, PetIQ, PVH, others | 2001-26 | definitions only | — | screened |
| 44 | EDGAR hit list "dilution" + "chargebacks" + "Walmart" + "borrowing base"; Zevia 2026 loan amendment; Tandy Brands 10-K FY2011 | Zevia; Tandy Brands; 89 others listed | 2002-26 | definitions; qualitative chargeback remarks | — | screened |
| 45 | OCR of Bon Worth v. Runway 7 opinion (Doc 62) | small retailer v. supplier | — | contract right to "non-compliance charges and allowances as chargebacks"; no amounts | — | screened |
| 46 | Doc 10, SOFA | ShopKo Stores Operating Co. (retailer) | FY2016-FY2018 | vendor fine income by type; sales | pp. 16, 27-31 | **used** (CSV) |
| 47 | Doc 60 | Goped v. Amazon.com | to 2016 | 10% charge on undelivered goods; allowances | pp. 2, 8 | used |
| 48 | Doc 14 | Spectrum Brands securities suit | 2017 | fill-rate penalties "into the millions" | pp. 8, 42, 61, 119 | used |
| 49 | Doc 82 | Primo Brands securities suit | 2024-25 | OTIF tracked; no amounts | pp. 42, 56 | screened |
| 50 | Doc 1 | Groupon Goods v. EDO Trading | 2021-22 | fine schedule; $139,660 | pp. 6-7, 39 | noted |
| 51 | Doc 1 (OCR) | Stiles v. Walmart (pro se supplier) | 2014 | asks Walmart to repay "false deductions made from the remittance from retail link"; no amounts | — | screened |
| 52 | Doc 1; Doc 8 (OCR); Doc 7-1 | QVC v. Interactive Group; Amcor v. CIT (Linens 'n Things settlement: two vendor chargebacks of $167,949.60 and $25,000 on GPS units); Pegasus v. Rue 21 | 2007-12 | single chargebacks; not big-box | — | screened |
| 53 | Doc 1-8; Doc 1 | Performance Food Group v. Valued; Smith v. Keurig Green Mountain | 2018-23 | distributor chargebacks; "penalties and vendor chargebacks owed to retailers" (no amount) | — | screened |

---

## 7. For the coordinator (not a call)

Everything here is **[our call]** or **[our calc]**. Nothing is decided.

1. **The retailer-side record confirms the neutral central for the size of the fine pool, and says nothing about its invalid share.** ShopKo's vendors paid compliance fines of 0.24-0.32% of ShopKo's sales, about **0.33-0.46% of their sales to it** (at an assumed 70-75% cost ratio). That is the CRF ¼-½% band from an independent, sworn source, and it is an average over all vendors, large and small. If a typical in-segment supplier's non-trade deductions are near **0.4% of sales** rather than the 0.5% central, the kill test's 0.05% "found" line needs **12.5%** of them to be provably invalid and the 0.17% pass line needs **42%** **[our calc]**. M Design Village's 1.2% (item 2) is then an above-average supplier, or a peak-season one.
2. **The first measured non-trade figure for an in-segment supplier is higher than the neutral central.** M Design Village's two chargeback accounts come to **1.20% of merchandise sales** over six holiday weeks. That is 2.4-4.8× CRF's ¼-½% median (N-N29) and 6× the *ANConnect* ledger (0.20%). Against the frozen kill test (`4_kill_conditions.md` §4.7, which measures the provable-invalid rate before recovery) **[our calc]**:
   - at CRF's 10% invalid: 1.20% × 10% = **0.12% found** (0.072% recovered at 60%), inside the 0.05-0.17% conditional band;
   - the invalid share that would reach the 0.17% pass line: 0.17 ÷ 1.20 = **14%**; the share that would fall to the 0.05% kill line: **4%**.
   
   **The chain cannot be completed from this document**, because it says nothing about the invalid share, and the supplier was in distress in its peak season.
3. **"Dilution" and "deductions" in public documents are almost always all types.** E. Gluck's 20% (January) and 24% reserve, Instant Brands' 3.7-5.2% and M Design's 5.2% are dominated by returns, damage allowances, promotions and discounts. **Any figure that does not split trade from non-trade should not enter the C-19 chain.** Where a split exists (M Design), non-trade chargebacks are about a quarter of all customer-related deductions (1.20 ÷ 5.20 **[our calc]**).
4. **Failures produce the big fines, and the 3PL paid them.** Just Play's ~$1.0M of chargebacks and Walmart penalty, and Revlon's >$1.2M in one month, came from warehouse collapse and stock-outs. In Just Play's case the money came back **from the 3PL** (first as invoice credits, then through a jury). This supports check AE's point that part of the pool is recoverable from 3PLs and carriers under contract, a path outside the retailer's dispute window.
5. **The only real dispute-labour record points to rounds of work, not minutes per item.** E. Gluck's advisers spent **23 hours on one Amazon dispute round** (14 h building the list, 6 h filing with remittance copies, 3 h follow-up). Without the count of chargebacks disputed it cannot test the model's 5 + 20 minutes, but it suggests the list-building step (matching remittances to invoices and agreements) is the heavy part, which is what software would take over.
6. **What would complete the measurement, from public records, if anyone wants to pay PACER fees (not done: PACER needs an account):** M Design Village's later monthly reports (Docs 104-153), which would give six more months of the same chargeback lines; Just Play's trial exhibits ECF 214-66 and 214-74 (the chargeback records); the customer-programs motions of Instant Brands (Doc 11), Revlon and E. Gluck. None of these gives the invalid share either. **The S5 look-back on one supplier's own deduction lines remains the only route to the decisive number** (as check AE §9.7 already says).
7. **Suggested wording if the figures are used:** "A $2B discount retailer's sworn filings show it collected vendor compliance fines of 0.24-0.32% of its sales in 2016-18 (ShopKo; *verified*); one in-segment supplier's books show non-trade chargebacks of about 1.2% of sales in six peak weeks (M Design Village, 2024; *verified*); neither shows how many were invalid."

---

## 8. Could not access, or not found

**Could not access:**
- **CourtListener search API:** throttled at 50 queries an hour; about 110 queries were run before the limit and about 36 after it cleared (N-AG70). Storage PDFs stayed available.
- **Documents listed on RECAP without PDFs** (only purchasable from PACER, which needs an account; not done): Instant Brands' customer-programs motion (Doc 11) and order (Doc 80); Revlon's customer-programs motion; E. Gluck's customer-obligations motion and later MORs; M Design Village's MORs after the first; Just Play's district-court trial exhibits (ECF 214-66, 214-74) and most of that docket; Tupperware, BowFlex and Del Monte customer-programs motions (already noted in check AE).
- **Kroll claims-agent docket for Instant Brands:** HTTP 403.
- **FTC grocery supply-chain report (2024):** the PDF URL tried returned 403 (curl) and 404 (WebFetch); not read.
- **Scanned PDFs without text:** International Garden Products cash-collateral motion (not OCR'd). Bon Worth v. Runway 7, Level 8 Apparel and one WYNIT exhibit were read by OCR.
- **Web search:** the session's web-search budget was used up during this check; the remaining work used CourtListener and direct document fetches only.

**Not found (searched, appears not to be public):**
- **Any transaction-level list of retailer deductions** (remittance advice, EDI 812/820, Retail Link or Vendor Central export, deduction ledger with reason codes) for a real supplier to a big-box retailer. Searched: RECAP full text for "remittance", "812", "shortage claims", "Vendor Central", "OTIF", "on-time in-full", "compliance chargebacks", "vendor compliance", "routing guide", "retailer fines", "fill rate" fines, "customer chargebacks", "Amazon - Chargebacks", "Walmart Chargebacks", "Target Chargebacks", and combinations with Walmart, Target, Amazon, Home Depot, Lowe's, Costco, Kroger.
- **A second retailer's sworn fine income.** Only ShopKo's statement of financial affairs in the RECAP index lists vendor fines as separate income lines; other retailer bankruptcies (Toys "R" Us, Sears, Bed Bath & Beyond, Big Lots, Rite Aid) were not found with such lines in the full-text index.
- **A filled borrowing-base certificate or field exam with dilution by retailer.**
- **Any document giving deduction counts, average deduction size, the invalid share, the share disputed, or the share recovered.**
- **A supplier-versus-big-box-retailer lawsuit over OTIF fines, shortages or compliance chargebacks with amounts** (the cases found involve J.C. Penney, Bed Bath & Beyond and Costco returns or allowances, or 3PLs).
- **Amazon Vendor Central shortage-claim litigation** with amounts.
- **SEC-filed values of a "dilution ratio"** for a consumer-goods supplier (only definitions are filed).

---

## 9. Sources

Access: **full** = PDF downloaded and searched; **OCR** = scanned PDF read by optical character recognition; **page extraction** = read through WebFetch; **listing** = docket or hit list only; **blocked** = refused.

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AG01 | CourtListener RECAP search API (type r and rd), ~110 queries; opinion search ~10 queries | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=r&q=… | listing | Case discovery; absence of deduction ledgers |
| N-AG02 | E. Gluck Corp., Bankr. S.D.N.Y. 25-12683, Doc 64-2, Exhibit B to Final DIP Order: CoMetrics four-week forecast and borrowing base | 2026-01-15 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.64.2.pdf | full | Sales by customer; dilution; ineligible and dilution reserves |
| N-AG03 | E. Gluck, Doc 100 and 100-1, MOR for January 2026 | 2026-02-24 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.100.1.pdf | full | Gross sales, dilution; AR aging with chargebacks |
| N-AG04 | E. Gluck, Doc 2, Rule 1007 declaration of the CFO with balance sheet | 2025-12-01 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.2.0.pdf | full | Business; accrued returns and allowances at 31 Oct 2025 |
| N-AG05 | E. Gluck, Doc 29, SOFA | 2025-12-15 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.29.0.pdf | full | Gross revenue 2023, 2024, 2025 YTD |
| N-AG06 | E. Gluck, Doc 64-1, Ratification and Amendment Agreement with the 2021 Credit and Security Agreement (Israel Discount Bank) | 2026-01-15 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.64.1.pdf | full | 5.0% dilution threshold; 50% concentration for Walmart, Amazon, Costco |
| N-AG07 | E. Gluck, Docs 107, 133, 135, 156 (and 177, 184 screened): monthly fee statements of CoMetrics Partners (CRO) and a successor firm | 2026-03-10 to 2026-09-15 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.135.0.pdf (and .107.0, .133.0, .156.0) | full | Time entries on Amazon chargebacks and disputes (CSV) |
| N-AG08 | E. Gluck, Docs 3, 8-1, 32, 37, 64 | 2025-12 to 2026-01 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.332494/gov.uscourts.nysb.332494.32.0.pdf (and others) | full | Screened; no further figures |
| N-AG09 | M Design Village, LLC, Bankr. D.N.J. 24-21406, Doc 101, Disclosure Statement (attaching Doc 87 MOR and Exhibit C projections) | 2025-02-14 | https://storage.courtlistener.com/recap/gov.uscourts.njb.1119534/gov.uscourts.njb.1119534.101.0.pdf | full | Customers; chargeback and trade lines; sales; projections (CSV) |
| N-AG10 | Instant Brands LLC, Bankr. S.D. Tex. 23-90716, Doc 432, SOFA | 2023-08-28 | https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.432.0.pdf | full | Gross revenue 2021, 2022, Jan-May 2023 |
| N-AG11 | Instant Brands, Doc 460, schedules (holding company) | 2023-08-29 | https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.460.0.pdf | full | Screened (setoff note lists "chargebacks") |
| N-AG12 | Instant Brands, Doc 1385, litigation trust complaint (Adv. 24-03232) | 2024-11-13 | https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.1385.0.pdf | full | Company revenue 2019-20 |
| N-AG13 | Kroll Restructuring Administration, Instant Brands docket | — | https://restructuring.ra.kroll.com/instantbrands/Home-DocketInfo | blocked (403) | — |
| N-AG14 | Revlon, Inc., Bankr. S.D.N.Y. 22-10760, Doc 30, Declaration of Robert M. Caruso (CRO) | 2022-06-16 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.312543/gov.uscourts.nysb.312543.30.0.pdf | full | OTIF penalties > $1.2M in May 2022; net sales; customers |
| N-AG15 | Just Play, LLC v. FitzMark, Inc., 11th Cir. 22-10235, Doc 29, Appellee's Brief | 2022-07-18 | https://storage.courtlistener.com/recap/gov.uscourts.ca11.77020/gov.uscourts.ca11.77020.29.0.pdf | full | Chargebacks ~$476K; Walmart penalty $550K; 3PL paid chargebacks; award |
| N-AG16 | Same, Doc 21, Appellant's Brief | 2022-05-18 | https://storage.courtlistener.com/recap/gov.uscourts.ca11.77020/gov.uscourts.ca11.77020.21.0_1.pdf | full | "Walmart is Just Play's largest customer" |
| N-AG17 | Just Play v. FitzMark, S.D. Fla. 9:20-cv-80663, docket listing | 2020-2022 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:17087466 | listing | Exhibits not on RECAP |
| N-AG18 | Nazareth International v. J.C. Penney, N.D. Tex. 3:04-cv-01265, Doc 31, Memorandum Opinion and Order | 2005-07-19 | https://storage.courtlistener.com/recap/gov.uscourts.txnd.137654/gov.uscourts.txnd.137654.31.0.pdf | full | Alleged 5% cap on late-shipment and label chargebacks |
| N-AG19 | Ion Audio v. Bed Bath & Beyond, S.D.N.Y. 1:15-cv-08292, Doc 108, Opinion and Order (Judge Kimba M. Wood) | 2019-04-02 | https://storage.courtlistener.com/recap/gov.uscourts.nysd.448929/gov.uscourts.nysd.448929.108.0.pdf | full | 2% damage allowance; rebate chargebacks; late claims |
| N-AG20 | Superwood v. Slam Brands, W.D. Wash. 2:12-cv-01109, Doc 120, Findings of Fact and Conclusions of Law | 2013-11-13 | https://storage.courtlistener.com/recap/gov.uscourts.wawd.185350/gov.uscourts.wawd.185350.120.0.pdf | full | Costco 2% returns allowance; $37,000 chargeback; markdowns |
| N-AG21 | CaseStack v. Korex, N.D. Ill. 1:23-cv-00214, Doc 1-1 (state complaint with logistics agreement) | 2023-01-13 | https://storage.courtlistener.com/recap/gov.uscourts.ilnd.425303/gov.uscourts.ilnd.425303.1.1.pdf | full | 3PL disclaims chargeback liability |
| N-AG22 | Age Group v. Regal Logistics, W.D. Wash. 2:07-cv-01303, Doc 74 | 2008-11-14 | https://storage.courtlistener.com/recap/gov.uscourts.wawd.145931/gov.uscourts.wawd.145931.74.0.pdf | full | Screened |
| N-AG23 | Manty v. Elevation Lab (WYNIT Distribution), Bankr. D. Minn. Adv. 18-04037, Doc 1 | 2018-04-02 | https://storage.courtlistener.com/recap/gov.uscourts.mnb.446967/gov.uscourts.mnb.446967.1.0.pdf | full + OCR | Pass-through of "non-compliance charges"; statement of account |
| N-AG24 | Sound Around v. Friedman, S.D.N.Y. 1:24-cv-01986, Doc 320-52 (expert report) | 2025-11-21 | https://storage.courtlistener.com/recap/gov.uscourts.nysd.617653/gov.uscourts.nysd.617653.320.52.pdf | full | Screened (qualitative) |
| N-AG25 | Evolution Micro, Bankr. M.D. Fla. 6:23-bk-04081, Docs 84, 86 | 2024 | https://storage.courtlistener.com/recap/gov.uscourts.flmb.1365635/gov.uscourts.flmb.1365635.84.0.pdf | full | Screened (Amazon 3P, out of scope) |
| N-AG26 | Mihaylov v. Tattooed Chef, C.D. Cal. 2:22-cv-09311, Doc 124, Second Amended Complaint | 2025-02-03 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.871364/gov.uscourts.cacd.871364.124.0.pdf | full | CW#2 on deductions (trade) |
| N-AG27 | Ferreira v. Funko, C.D. Cal. 2:20-cv-02319, Doc 117-10 | 2020 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.776006/gov.uscourts.cacd.776006.117.10.pdf | full | Same "non-compliance chargebacks" sentence as N-AE10; no amount |
| N-AG28 | In re Hain Celestial Securities Litigation, E.D.N.Y. 2:16-cv-04581, Doc 75 | 2017 | https://storage.courtlistener.com/recap/gov.uscourts.nyed.390004.75.0.pdf | full | Screened |
| N-AG29 | Corsicana Bedding, Bankr. N.D. Tex. 22-90016, Doc 13, DIP motion with credit agreement | 2022-06-25 | https://storage.courtlistener.com/recap/gov.uscourts.txnb.500218/gov.uscourts.txnb.500218.13.0_3.pdf | full | Dilution reserve above 5.0% |
| N-AG30 | Diamond Comic Distributors, Bankr. D. Md. 25-10308, Docs 16, 163 | 2025 | https://storage.courtlistener.com/recap/gov.uscourts.mdb.791767/gov.uscourts.mdb.791767.16.0.pdf | full | Screened |
| N-AG31 | KidKraft, Bankr. N.D. Tex. 24-80045, Docs 159, 161 | 2024-06-10 | https://storage.courtlistener.com/recap/gov.uscourts.txnb.516306/gov.uscourts.txnb.516306.161.0.pdf | full | Screened |
| N-AG32 | Noble House Home Furnishings, Bankr. S.D. Tex. 23-90773, Docs 16, 706 | 2023-25 | https://storage.courtlistener.com/recap/gov.uscourts.txsb.466137/gov.uscourts.txsb.466137.16.0_1.pdf | full | Screened |
| N-AG33 | BowFlex, Bankr. D.N.J. 24-12364, Docs 37, 44, 61 | 2024-03 | https://storage.courtlistener.com/recap/gov.uscourts.njb.1109943/gov.uscourts.njb.1109943.44.0.pdf | full | Screened |
| N-AG34 | Basic Fun, Bankr. D. Del. 24-11432, Doc 221 | 2024-09-27 | https://storage.courtlistener.com/recap/gov.uscourts.deb.193530/gov.uscourts.deb.193530.221.0.pdf | full | Screened |
| N-AG35 | Kid Brands, Bankr. D.N.J. 14-22582, Doc 504 | 2015-01-06 | https://storage.courtlistener.com/recap/gov.uscourts.njb.914498.504.0.pdf | full | Screened |
| N-AG36 | North Pacific Canners & Packers, Bankr. D. Or. 19-62584, Doc 16 | 2019-08-22 | https://storage.courtlistener.com/recap/gov.uscourts.orb.504589/gov.uscourts.orb.504589.16.0.pdf | full | Sam's + Walmart 30% concentration |
| N-AG37 | GPMI Co., Bankr. W.D. Ark. 2:22-bk-00150, Doc 9-1 | 2022-01 | https://storage.courtlistener.com/recap/gov.uscourts.arb.791758/gov.uscourts.arb.791758.9.1_1.pdf | full | Screened |
| N-AG38 | LDR Industries, Bankr. N.D. Ill. 14-32138, Doc 14-2 | 2014-09 | https://storage.courtlistener.com/recap/gov.uscourts.ilnb.1275734.14.2.pdf | full | Screened |
| N-AG39 | International Garden Products, Bankr. D. Del. 10-13207, Doc 14-2 | 2010-10 | https://storage.courtlistener.com/recap/gov.uscourts.deb.129852.14.2.pdf | no text layer | — |
| N-AG40 | Level 8 Apparel, Bankr. S.D.N.Y. 16-13164, Doc 17 | 2016-11 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.270471/gov.uscourts.nysb.270471.17.0.pdf | OCR | Screened |
| N-AG41 | Miller v. ANConnect, Adv. 18-50633, Docs 221-1, 358; D. Del. 1:24-cv-00243, Doc 20 (appendix) | 2022-26 | https://storage.courtlistener.com/recap/gov.uscourts.ded.85053/gov.uscourts.ded.85053.20.0.pdf | full | Sister documents; "deductions" = returns |
| N-AG42 | Emigrant Business Credit v. Hanratty, Bankr. S.D.N.Y. Adv. 24-04020, Doc 1-1 | 2024 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.325174/gov.uscourts.nysb.325174.1.1.pdf | full | Screened (irrelevant) |
| N-AG43 | Finkel v. WeVeel, Bankr. E.D. Pa. Adv. 14-00333, Doc 209 | — | https://storage.courtlistener.com/recap/gov.uscourts.paeb.444353/gov.uscourts.paeb.444353.209.0.pdf | full | Screened (irrelevant) |
| N-AG44 | M Design Village docket listing | 2024-25 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:69383361 | listing | Later MORs not on RECAP |
| N-AG45 | Halperin v. Arawak IX, Adv. 21-51412, Doc 304-2 | — | https://storage.courtlistener.com/recap/gov.uscourts.deb.186790/gov.uscourts.deb.186790.304.2.pdf | full | Screened |
| N-AG46 | Midlab v. Wycoff, D. Colo. 1:20-cv-03142, Doc 57-20 | 2021 | https://storage.courtlistener.com/recap/gov.uscourts.cod.201744/gov.uscourts.cod.201744.57.20.pdf | full | Screened |
| N-AG47 | SEC EDGAR full-text search, "dilution ratio" + "Walmart" (via WebFetch) | 2026-09-22 | https://efts.sec.gov/LATEST/search-index?q=%22dilution%20ratio%22%20%22Walmart%22&forms=10-K,10-Q,8-K | page extraction (hit list) | 19 agreements; no values |
| N-AG48 | Web pages on ABL field exams and dilution (Fundingo, Journal of Accountancy, Private Equity Bro, LCG Advisors; search results) | various | https://www.fundingo.com/understanding-borrowing-base-dilution-in-asset-based-lending/ | snippet | General definitions; no figures |
| N-AG49 | FTC, grocery supply-chain 6(b) report (2024) | 2024 | https://www.ftc.gov/system/files/ftc_gov/pdf/p162300supplychainreport2024.pdf | blocked (403/404) | — |
| N-AG50 | Web search: Amazon Vendor Central shortage-claim litigation (Amalytix, ChannelEngine, Wake Commerce, iNymbus, Reason Automation pages) | 2026-09-22 | https://www.wakecommerce.co.uk/blog/amazon-vendor-central-shortage-claims | snippet | No litigation found |
| N-AG51 | Web search: supplier suits against Walmart or Target over deductions (SPS, 8th & Walton, SupplyPike, iNymbus pages) | 2026-09-22 | https://www.spscommerce.com/community/articles/how-to-dispute-walmart-otif-chargebacks | snippet | No such suit found |
| N-AG52 | Revlon docket search, "customer programs" | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:63388582 | listing | Motion not on RECAP |
| N-AG53 | Instant Brands docket search | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:67494684 | listing | Docs 11, 80 not on RECAP |
| N-AG54 | E. Gluck docket search | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:71977586 | listing | Customer motion, later MORs not on RECAP |
| N-AG55 | Stuart's LLC v. Edelman (N.Y. Sup. Ct. 2018), CourtListener opinion page | 2018-04-09 | https://www.courtlistener.com/opinion/4486889/stuarts-llc-v-edelman/ | blocked (no text returned) | — |
| N-AG56 | Thrasio (Bankr. D.N.J. 24-11840); Careful Shopper v. TP-Link; Thimes v. TP-Link | various | https://www.courtlistener.com/api/rest/v4/search/?type=r&q=… | snippet | Amazon 3P; out of scope |
| N-AG57 | Goldberg (Bed Bath & Beyond plan administrator) v. CHF Industries, Himatsingka, Linon, Nishat Chunian, Tabletops, Bankr. D.N.J. Adv. 25-01165 to 25-01169 | 2025-04-22 | https://storage.courtlistener.com/recap/gov.uscourts.njb.1125339/gov.uscourts.njb.1125339.1.0_1.pdf | full | Screened (preference suits; vendor agreements) |
| N-AG58 | Bon Worth v. Runway 7 Fashions, S.D.N.Y. 1:17-cv-09712, Doc 62 | — | https://storage.courtlistener.com/recap/gov.uscourts.nysd.485179/gov.uscourts.nysd.485179.62.0.pdf | OCR | Contract right to "non-compliance charges and allowances as chargebacks"; no amounts |
| N-AG59 | National Christmas Products v. OJ Commerce, S.D. Fla. 0:22-cv-60897, Doc 24; Taizhou Yuanda v. Z Outdoor Living, W.D. Wis. 3:19-cv-00875, Doc 1 | 2019-22 | https://storage.courtlistener.com/recap/gov.uscourts.flsd.612940/gov.uscourts.flsd.612940.24.0.pdf | full | Screened |
| N-AG60 | Eastech Electronics v. E&S International (Costco), C.D. Cal. 2:07-cv-03204, Doc 211 | — | https://storage.courtlistener.com/recap/gov.uscourts.cacd.388937/gov.uscourts.cacd.388937.211.0.pdf | snippet | Not read |
| N-AG61 | SEC EDGAR full-text search, "dilution" + "chargebacks" + "Walmart" + "borrowing base" (via WebFetch) | 2026-09-22 | https://efts.sec.gov/LATEST/search-index?q=%22dilution%22%20%22chargebacks%22%20%22Walmart%22%20%22borrowing%20base%22&forms=10-K,10-Q,8-K | page extraction (hit list) | 91 filings; agreements and risk language |
| N-AG62 | Zevia PBC, 10-Q exhibit (First Amendment to Loan and Security Agreement, Bank of America), filed 2026-08-05; Tandy Brands Accessories, 10-K FY2011, filed 2011-09-01 | 2011; 2026 | https://www.sec.gov/Archives/edgar/data/1854139/000143774926025925/ex_993128.htm ; https://www.sec.gov/Archives/edgar/data/869487/000117184311002669/f10k_090111.htm | page extraction | "Dilution Percent" definition; 25% caps; Tandy's chargeback remarks, Walmart 48% |
| N-AG63 | ShopKo Stores Operating Co., LLC, Bankr. D. Neb. 19-80075, Doc 10, Statement of Financial Affairs (937 pages) | 2019-02-22 | https://storage.courtlistener.com/recap/gov.uscourts.nebraskab.174196/gov.uscourts.nebraskab.174196.10.0_2.pdf | full | Sales FY2016-18; vendor fine and audit income by type (CSV) |
| N-AG64 | In re Spectrum Brands Securities Litigation, W.D. Wis. 3:19-cv-00347, Doc 14, Amended Complaint | 2019 | https://storage.courtlistener.com/recap/gov.uscourts.wiwd.43718/gov.uscourts.wiwd.43718.14.0_3.pdf | full | Fill-rate SLAs; penalties "into the millions" in 2017 (allegations) |
| N-AG65 | City of Miami Fire Fighters' and Police Officers' Retirement Trust v. Primo Brands, M.D. Fla. 8:25-cv-03328, Doc 82, Amended Complaint | 2026-04-06 | https://storage.courtlistener.com/recap/gov.uscourts.flmd.450881/gov.uscourts.flmd.450881.82.0.pdf | full | OTIF tracking; no amounts |
| N-AG66 | Goped Ltd. v. Amazon.com, D. Nev. 3:16-cv-00165, Doc 60, Order | 2018-02-12 | https://storage.courtlistener.com/recap/gov.uscourts.nvd.114030/gov.uscourts.nvd.114030.60.0.pdf | full | Amazon 1P vendor terms; 10% charge on undelivered goods |
| N-AG67 | Groupon Goods v. EDO Trading, N.D. Ill. 1:22-cv-01609, Doc 1 | 2022-03-28 | https://storage.courtlistener.com/recap/gov.uscourts.ilnd.413679/gov.uscourts.ilnd.413679.1.0.pdf | full | Non-compliance chargeback schedule |
| N-AG68 | Stiles v. Walmart (E.D. Cal. 2:14-cv-02234, Doc 1, OCR); QVC v. Interactive Group (E.D. Pa. 2:12-cv-01761, Doc 1); Amcor v. CIT (S.D.N.Y. 1:08-cv-04508, Doc 8, OCR); Pegasus v. Rue 21 (S.D.N.Y., Doc 7-1); Performance Food Group v. Valued (N.D. Ill., Doc 1-8); Smith v. Keurig Green Mountain (N.D. Cal., Doc 1) | 2007-23 | https://storage.courtlistener.com/recap/gov.uscourts.caed.273003/gov.uscourts.caed.273003.1.0.pdf (and others) | full / OCR / snippet | Screened |
| N-AG69 | SEC EDGAR full-text search (via WebFetch): "shortage claims" + "Amazon" (0 hits); "chargebacks" + "OTIF" (1 hit: Triumph Financial investor deck, 8-K 2025-07-16, no figures) | 2026-09-22 | https://efts.sec.gov/LATEST/search-index?q=%22chargebacks%22%20%22OTIF%22&forms=10-K,10-Q,8-K | page extraction | Absence of filed amounts |
| N-AG70 | CourtListener RECAP search API, second batch after the rate limit cleared (~36 queries: OTIF, "on time in full", "Fill Rate Penalty", "Vendor Penalties", "ASN Audit", "A/P Internal Audit Income", "Vendor Chargebacks", "compliance chargeback", "Retail Link" deductions, "remittance advice", "Vendor Central" chargebacks, retailer SOFA terms, and others) | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/?type=r&q=%22Fill%20Rate%20Penalty%22 | listing | Found ShopKo, Goped, Spectrum, Groupon; confirmed absences |
