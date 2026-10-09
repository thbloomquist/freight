# S4.5 check AH: what neutral studies, regulators and benchmark bodies say about retailer deductions and OTIF fines (C-19)

- **What this is:** one slice of the **S4.5 profitability check** for **C-19, retailer on-time-in-full (OTIF) fines and non-trade deductions, for suppliers with sales of $500M or less selling to big-box retailers**, run 01. The slice covers **neutral (non-vendor) sources only**: university research, regulators, associations and benchmark bodies, and retailers' own public statements. It feeds the per-customer model in `selection_runs/run-01/4_kill_conditions.md` §4:

  > recovered = big-box sales × **non-trade deductions %** × **invalid share** × **recovered share**; fee = 25%; cost = deductions × 5 min triage + invalid ones × 20 min dispute at $33.70/h (US) or $12/h (offshore), + $600 fixed.
  >
  > Frozen kill line (Test 1): provable invalid non-trade deductions **under 0.05%** of sales kills; **0.17% or more** passes.

- **Date:** 2026-09-22. Everything new here was accessed on 2026-09-22.
- **Status:** input only. **It decides nothing.** Every reading is **[our call]** and sits in §7, "For the coordinator (not a call)".
- **Labels:**
  - *verified*: read at the source (the survey report, the paper, the regulator's report, the retailer's words as reported at source). An association survey read at source is *verified* as "what the survey says", with a flag that the figures are **self-reported by respondents** and that the survey's owner (Attain Consulting Group) sells deduction consulting.
  - *assumed*: vendor figures (always); association or consultancy figures read second-hand; search-result snippets; summaries; anything blocked.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
  - **Vendor figures are kept apart.** They appear only in passing, marked *assumed*.
- **New source IDs:** N-AH01 to N-AH52 (§8).
- **Not redone here (cited by ID):** the CRF 2018 survey slides (N-N29); Carixa's slides citing CRF 2021 (N-U29); Quadient quoting the CRF Benchmarking Report's "$97" (N-AE40); McKinsey 2018 and 2019 (N-AE49, N-AE50); Uber Freight's 0.16% via Forbes (N-AE51); Walmart's OTIF goals 2017-2024 (N-AE52); retailer rules and windows (check U); the GAO report on PRG's recovery audit (N-X04) and PRGX's 10-K FY2018 (N-X12).
- **New here that replaces a second-hand figure:** the **primary CRF/Attain 2021 report** (N-AH01), previously known only through a vendor's slides (N-U29), and the **CRF 2023 survey results** (N-AH02), previously not seen at all. Both add a **split by company size** and the **full answer distributions**, which change how the model's central inputs read (§2.1, §7.1).
- **Hard rules kept:** public pages only; no forms, sign-ups or gated files (Attain's result pages ask for an email and were **not** used, N-AH10); no identity in any request (curl's default or a generic "Mozilla/5.0" user agent; no contact given anywhere). Downloads are in the session scratchpad (`…/scratchpad/c19_s45/ah/`), not the project.
- **Search budget:** the session's shared web-search budget ran out part-way through this check. After that, discovery used direct fetches and public APIs (MIT DSpace, OpenAlex, CRF's public media list). What this left unsearched is listed in §9.

**Words used here:**
- **Deduction / short-pay:** money a retailer takes off what it pays the supplier. **Chargeback / fine / penalty:** a deduction raised as a charge for breaking the retailer's rules.
- **Trade deduction:** for an agreed promotion, rebate, co-op advertising or markdown. **Out of scope.** **Non-trade deduction:** in CRF's survey wording, "compliance deductions and shortages while excluding returns, unsaleables and all trade related items" (N-AH01). This is C-19's pool.
- **Invalid deduction:** one the supplier shows to be wrong and "charges back" to the retailer. **Recovered:** the retailer pays it back.
- **OTIF (on-time in-full):** the share of ordered cases that arrive inside the delivery window and in the full quantity. Walmart fines 3% of the cost of the failing cases when a supplier is below its goal (check U). **Fill rate:** the in-full half alone.
- **ASN (advance ship notice):** the electronic packing list sent before the truck. **POD:** proof of delivery. **PO:** purchase order.
- **Execution-quality error:** an academic term (N-AH12) for breaking a retailer's rules on labels, packaging, paperwork or ASNs, as distinct from wrong price, quantity, quality or timing.
- **DDO (days deductions outstanding):** average open deduction dollars ÷ (annual deduction dollars ÷ 360).
- **Auto write-off threshold:** the size below which a supplier writes a deduction off without looking at it.
- **Post-audit / forensic audit claim:** a claim a retailer (or its recovery-audit firm, such as PRGX) raises months or years later for money it says the supplier still owes. The mirror image of C-19.
- **GCA:** the UK Groceries Code Adjudicator, which regulates the 14 largest UK grocers, Amazon included. **OGSCC:** Canada's Office of the Grocery Sector Code of Conduct. **UTP:** the EU's Unfair Trading Practices directive.
- **Band / midpoint mean:** survey answers come in bands ("¼-½% of sales"). A "midpoint mean" puts each respondent at the middle of its band and averages them **[our calc]**.
- **CRF:** the Credit Research Foundation, a US credit-management association. **Attain:** Attain Consulting Group, the deduction consultancy that has run CRF's deduction survey since 2015. **RVCF:** the Retail Value Chain Federation, a retail-compliance association.

---

## 1. Summary inputs table

Neutral sources only, unless a row says otherwise. "Sales" means the supplier's sales unless marked. "≤$500M" means respondents with annual revenue of $500M or less.

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Non-trade deductions, % of sales** (compliance + shortages) | **< 0.25%**: 46% of ≤$500M respondents (2021) | **¼-½%**: median of ≤$500M respondents, 2021 (all sizes: ½-1%). All sizes 2023: **1.1-2%** | **3.1-10%**: 14% of ≤$500M respondents (2021); 17% of all respondents above 5% (2023). Midpoint mean ≤$500M: **1.1%** | *verified* (CRF/Attain survey, self-reported); mean **[our calc]** | N-AH01, N-AH02; earlier N-N29 |
| Compliance chargebacks, % of invoice (RVCF founder) | 0.25% | average **0.4-0.8%** | 1.25% | *assumed* (association figure read second-hand) | N-AH07 |
| **OTIF fines, % of sales to that retailer** | 0% above the goal | **0.2-0.3%** implied by an in-full rate in the "low 90s" against a 98% goal (C.H. Robinson consolidator, 2021) [our calc]; observed 0.16% of COGS at Walmart (known, N-AE51) | **up to ~1.8%** implied by Walmart's own "40%" OTIF on food and consumables (Mar 2019) if every failing case was fined [our calc] | inputs *verified* (MIT capstone; Talk Business quoting Walmart); fines **[our calc]** from the 3% rule | N-AH18, N-AH25, N-AE51 |
| **Supplier OTIF performance** | Walmart's top 75 suppliers "as low as 10 percent", none at the 95% goal (2017); food and consumables "a dismal 40%" (Mar 2019) | "only 60% of the suppliers" reach Walmart DCs on time and in full (Walmart-sponsored MIT capstone, 2020); at Amazon "only about half" of POs arrive by the vendor's estimated date (2014) | Consolidator's fill rate "low 90s" vs 98% target, two suppliers at 83-84% (2021); only 4% of shipments >12 h late (McKinsey 2019, known) | *verified* (at source; point observations, not distributions) | N-AH24, N-AH25, N-AH17, N-AH20, N-AH18, N-AE50 |
| Share of suppliers below 90% / 95% OTIF | — | **not found** | — | — | §5, §9 |
| **Invalid share** (of **all** deduction dollars, trade included) | **< 1%**: 25% of ≤$500M respondents | **1.1-5%**: median of ≤$500M respondents (all sizes: 5.1-10%, 2021 and 2023) | **≥ 15%**: 43% of ≤$500M respondents. Midpoint mean ≤$500M: **13.9%** | *verified* (survey); mean **[our calc]** | N-AH01, N-AH02 |
| Invalid share, **compliance chargebacks only** (one account) | — | **16.5%** of one apparel account's year-to-date compliance chargeback dollars reversed after dispute (one retailer, 2026) | 51.6% of the dollars a 3PL chose to dispute (39 cases, 19 retailers, 2026) | *verified* (preprint read in full; not peer reviewed; author works at a 3PL) | N-AH16 |
| **Recovered share, of invalid dollars** | 10% or less: 10% of ≤$500M respondents | **70%**: median of ≤$500M respondents (all sizes 60%; >$500M 50%). Midpoint mean ≤$500M: 63% | 90-100%: 34% of ≤$500M respondents | *verified* (survey); mean **[our calc]** | N-AH01 |
| → **Recoverable, % of sales** (the three rows multiplied) | ~0.001% (low bands) | **~0.008%** at the ≤$500M medians; 0.034% at 2021 all-size medians; 0.07% at 2023 medians | **~0.10%** product of ≤$500M midpoint means; 0.2% at the ≤$500M upper quartiles | **[our calc]**; assumes the three answers are independent **[our call]** | §7.1 |
| **Cost per deduction processed** | $5.99 (lower quartile) | **$18.80** (median, all industries, n = 287, c. 2012 data) | $75.00 (upper quartile) | *verified* (CRF Benchmarking Report, public sample) | N-AH03; vendor-quoted $97 (N-AE40) |
| **Minutes per deduction** (all types, manual) | ~17 min (upper-quartile throughput, 6,756 a year per FTE) | **~52 min** (median 2,167 deductions a year per deduction FTE) | ~3.7 h (lower quartile, 509 a year) | throughput *verified*; minutes **[our calc]** at 1,880 productive hours a year **[our call]** | N-AH03 |
| Days to resolve | 27.5 days median, one 3PL's disputed cases (2026) | **30 days** to decide, **90 days** to final resolution (CRF 2021 medians); DDO 39 days | 105 days (older CRF edition) | *verified*; older edition *assumed* (snippet) | N-AH16, N-AH01, N-AH05 |
| **Deductions per $1M of sales** | ~6 (all types) | **~11 per $1M** (all types: median deductions per FTE ÷ median sales per FTE, c. 2012) | 13-32 compliance chargebacks per $1M (RVCF's 0.4-0.8% at $250-300 each) | CRF *verified*, RVCF *assumed*; ratios **[our calc]** | N-AH03, N-AH07 |
| **Average deduction size** | ~$3 per Amazon vendor-defect chargeback (2012: ~$1M on ~300,000 defects) | **$150-450** per PO incident in retailers' published fee schedules; RVCF: "$250-300 per occurrence" | ~$6,800 per case disputed by a 3PL (cases pool several deductions; Walmart ~$7,800) | schedules *verified* (papers); RVCF *assumed*; ratios **[our calc]** | N-AH19, N-AH12, N-AH14, N-AH07, N-AH16 |
| Auto write-off threshold (shows what small suppliers ignore) | — | **$10-25** median at ≤$500M (2021); $50-100 all sizes (2023) | $100-250 median in food, beverage and grocery (2023) | *verified* (survey) | N-AH01, N-AH02 |
| Share of suppliers hit by incorrect deductions (UK grocery) | 32% (2017) | — | 46% (2014) | *verified* (UK regulator's survey) | N-AH32 |
| Retailer-side recovery audit (mirror), % of supplier spend | — | 0.1% ("$1M for every $1B in supplier spend", PRGX marketing) | 0.48% for a new client (PRG via GAO, known) | PRGX *assumed* (vendor); GAO known | N-AH43, N-X04 |

**One-line reading [our call]:** the best neutral primary source, the CRF 2021 survey split by size, puts the **median ≤$500M supplier at about 0.01% recoverable**, below the model's neutral central of 0.03% and well below the 0.05% kill line. But the answers are **heavily skewed**: the averages across suppliers come to about **0.10%**, and roughly **one in five** small suppliers may sit above the 0.17% pass line (§7.1). No neutral source measures the **non-trade-specific** invalid share, which decides where a given supplier falls.

---

## 2. Associations and benchmark bodies

### 2.1 CRF/Attain, "Customer Deductions: 2021 Benchmark Survey" (N-AH01): the primary report

**What it is.** The report behind the "CRF 2021" figures that check U and check AE had only via a vendor's slides (N-U29). CRF first issued this survey in 1998 and repeats it about every three years. Attain Consulting Group has run it since 2015. **111 respondents**: 40 with revenue ≤$500M and 65 above. 70% manufacturers, 25% distributors. Food and beverage 20%, building supplies 18%, apparel 16%. The survey was endorsed and circulated by CRF, RVCF, BPCA, Credit Today and three vendors: HighRadius, IAB Solutions and Genpact. Posted publicly on CRF's site (no login, no form). *verified* (full PDF read), with two flags: the figures are self-reported, and Attain sells deduction consulting.

**Definitions (quoted):**
- Non-trade: "Non trade-related deductions were defined to include compliance deductions and shortages while excluding returns, unsaleables and all trade related items" (p. 10-11).
- Invalid: "what percent of total deduction dollars received are invalid or disallowed and charged back to your customers" (p. 11). **This is a share of all deductions, trade included.**
- Recovered: "what percent of these invalid or disallowed deduction dollars are ultimately recovered from customers" (p. 11).

**Headline medians (quoted, p. 10-11):**
- "The median response across all respondents was non trade deductions were ½ - 1% of sales. This is an increase from 2018 when the median was ¼ - ½% of sales."
- "For responding companies with annual revenue ≤ $500 million, the median for non trade-related deductions as a percent of sales was ¼ - ½%. However, for companies with annual revenue > $500 million, the median reported was ½ - 1%." The report adds that respondents were larger in 2021 than in 2018, which may explain part of the rise.
- Invalid: "the median of all respondents is 5.1-10%. This is consistent with the results of the 2018 survey."
- Recovered: "The median percent of invalid deduction dollars recovered is 60%" (≤$500M: **70%**; >$500M: 50%).
- Time: 30 days median to the initial decision, then 60 more to collect or write off, so "the median time from receipt of deduction until ultimate resolution is 90 days, or 3 months" (p. 8). "The median DDO reported across all respondents is 39 days" (p. 11).
- Auto write-off: "The median auto write-off tolerance for respondents with annual revenue ≤ $500 million was $10 - $25 compared $50 - $100 for those with annual revenue > $500 million" (p. 9).
- **Top non-trade deduction reasons**, by both count and dollars: 1 shortages, 2 early/late delivery, 3 fill rate; then EDI/ASN errors and transportation, freight or routing (p. 10).
- Trend: 32% of respondents reported deduction dollars as a percent of sales rising in the past 12 months, 22% falling and 39% unchanged (p. 12).

**The full answer distributions** (Section III, Q33, Q34, Q37; percent of respondents answering) *verified*; cumulative shares **[our calc]**:

*Q37. Non-trade deductions as % of annual sales*

| Band | All (2021) | **≤$500M** | >$500M | Food, bev., grocery |
|---|---|---|---|---|
| < 0.25% | 30.0% | **46.4%** | 19.5% | 30.8% |
| 0.25-0.5% | 17.1% | **10.7%** | 22.0% | 0.0% |
| 0.5-1% | 20.0% | **17.9%** | 22.0% | 23.1% |
| 1.1-2% | 7.1% | 7.1% | 7.3% | 7.7% |
| 2.1-3% | 7.1% | 3.6% | 9.8% | 0.0% |
| 3.1-5% | 12.9% | **10.7%** | 12.2% | 30.8% |
| 5.1-10% | 5.7% | 3.6% | 7.3% | 7.7% |
| > 10% | 0% | 0% | 0% | 0% |
| Median band | ½-1% | **¼-½%** (cumulative 57% at ½%) | ½-1% | ½-1% |
| Upper quartile | 2.1-3% (cumulative 74.3% at 2%) | **~1%** (cumulative 75.0% at 1%) | 2.1-3% | 3.1-5% |
| Midpoint mean [our calc] | 1.50% | **1.14%** | 1.68% | 2.16% |

*Q33. Invalid share of all deduction dollars*

| Band | All (2021) | **≤$500M** | >$500M |
|---|---|---|---|
| < 1% | 19.2% | **25.0%** | 15.9% |
| 1.1-5% | 30.1% | **28.6%** | 29.6% |
| 5.1-10% | 11.0% | 3.6% | 15.9% |
| 10.1-15% | 9.6% | 0.0% | 15.9% |
| 15.1-20% | 8.2% | **10.7%** | 6.8% |
| 20.1-30% | 9.6% | **17.9%** | 4.6% |
| 30.1-40% | 5.5% | 7.1% | 4.6% |
| 40.1-50% | 2.7% | 3.6% | 2.3% |
| > 50% | 4.1% | 3.6% | 4.6% |
| Median band | 5.1-10% (cumulative 49.3% at 5%) | **1.1-5%** (cumulative 53.6% at 5%) | 5.1-10% |
| Midpoint mean [our calc] | 12.5% | **13.9%** | 11.9% |

The ≤$500M answers are **split in two**: 54% say 5% or less, 43% say 15% or more, and almost nobody sits between.

*Q34. Share of invalid dollars ultimately recovered*

| Answer | All (2021) | **≤$500M** | >$500M |
|---|---|---|---|
| 90-100% | 18.9% | **34.5%** | 9.1% |
| 70-80% | 21.6% | 20.7% | 22.7% |
| 50-60% | 23.0% | 24.1% | 20.5% |
| 20-40% | 17.6% | 10.3% | 22.7% |
| 10% or less | 18.9% | 10.3% | 25.0% |
| Median | 60% | **70%** | 50% |
| Mean [our calc] | 53% | **63%** | 47% |

**Other answers that bear on the model** (Q40, Q57, Q58; ≤$500M column) *verified*:
- **48%** of ≤$500M respondents "are not actively tracking any deduction metrics"; 21% cannot track recoveries at all and 61% track them by hand. **Their answers above are therefore rough estimates** [our call].
- **3%** of ≤$500M respondents outsource any deduction task (21% of larger ones).
- Shortages as a share of non-trade dollars (Q38): 75% of ≤$500M respondents said under 10%. Yet shortages rank first by dollars in the "top 3" question. The two answers do not sit easily together, so the split of non-trade dollars by type is **not usable** [our call].

### 2.2 CRF "2023 Deduction Metrics Survey" (N-AH02)

**What it is.** A CRF forum panel deck (18 Mar 2024) presenting the 2023 edition of the same survey. The survey was launched in August 2023 as a collaboration of Attain, Carixa, CRF, IAB and RVCF, "from various perspectives including retailers". Charts were read from the slide images. No size split and no respondent count are shown. *verified* (public PDF on CRF's site); three of the five collaborators sell deduction services.

- **Non-trade deductions as % of sales:** "Median is 1.1 – 2% of sales. (2021 median was ½ - 1% and 2018 median was ¼ - ½%)". "17% reported > 5% of sales (this was 6% in 2021)" (slide 9). Distribution: < 0.25%: 25%; 0.25-0.5%: 8%; 0.6-1%: 13%; **1.1-2%: 19%**; 2.1-3%: 6%; 3.1-5%: 13%; 5.1-10%: 9%; > 10%: 8%. Midpoint mean ≈ **2.8%** [our calc, with "> 10%" put at 12.5%].
- **Invalid share of all deductions:** < 1%: 23%; 1.1-5%: 19%; **5.1-10%: 13% (median)**; 10.1-15%: 9%; 15.1-20%: 11%; 20.1-30%: 11%; 31-40%: 6%; 41-50%: 6%; > 50%: 2% (slide 11). Midpoint mean ≈ 13.5% [our calc].
- **Trend:** 47% of respondents said deduction dollars as a percent of sales rose in the past 12 months, against 34% in 2021 (slide 12).
- **Auto write-off threshold:** median $50-100 for all respondents (up from $25-50); **$100-250 in food, beverage and grocery** (slide 8).
- 18% track no deduction KPI at all (slide 10).
- **Recovery share:** not shown in the deck.

**Reading [our call]:** three editions show the median non-trade rate rising, ¼-½% (2018) → ½-1% (2021) → 1.1-2% (2023). But respondents grew larger over time, and the 2023 deck gives no size split. **Whether ≤$500M suppliers also moved up is unknown.**

### 2.3 CRF Benchmarking Report, public sample (N-AH03)

**What it is.** A sample company report from CRF's long-running A/R benchmarking study (report prepared 27 Apr 2012, posted on CRF's site in Dec 2017). It shows the peer quartiles for "All industries, # of companies = 287". The "firm's data" column is a fictional sample company. The peer figures appear to be real benchmark data of about 2012, but a sample could be illustrative. *verified* as what the document shows; the vintage and whether the data are real are **not confirmed**.

| Metric (CRF definition) | Lower quartile | **Median** | Upper quartile |
|---|---|---|---|
| Deductions processed per deduction-processing employee a year ("REMOVED during the year" ÷ deduction FTEs) | 509 | **2,167** | 6,756 |
| Deduction processing cost per deduction processed | $5.99 | **$18.80** | $75.00 |
| Deduction processing cost as % of sales | 0.0086% | **0.0200%** | 0.0540% |
| Cost per deduction employee a year | $35,106 | $42,884 | $58,000 |
| Sales per deduction employee | $82.3M | **$193.9M** | $537.6M |
| Open deductions as % of annual sales (a stock, not a flow) | 0.061% | 0.227% | 0.554% |
| Deduction turnover (count: (opening + new) ÷ closing) | 4.29 | 7.27 | 14.13 |

(The executive-summary page of the same sample shows a slightly different cost per deduction: $5.76 / $14.62 / $57.16. The detail table is used here.)

**Derived [our calc]:**
- **Minutes per deduction:** at 1,880 productive hours a year **[our call]**, the median throughput of 2,167 is **~52 minutes** per deduction. The upper quartile (6,756) is ~17 minutes; the lower quartile (509), ~3.7 hours. This covers **all** deduction types, handled by hand. The model's 5 minutes triage + 20 minutes per invalid one averages about 7 minutes per deduction at a 10% invalid share.
- **Deductions per $1M of sales:** 2,167 ÷ $193.9M ≈ **11 per $1M** (6.2 at the lower-quartile pair, 12.6 at the upper). These are ratios of medians, not a measured median.
- **Rough flow:** open deductions of 0.227% of sales × (7.27 − 1) new per open ≈ **1.4% of sales** in new deductions a year, all types. This assumes dollars turn over like counts **[our call]**, so it is order-of-magnitude only.
- **Cost check:** $42,884 ÷ 2,167 = $19.79 per deduction, consistent with the $18.80 median.
- **Against the vendor-quoted "$97"** (N-AE40, attributed to "CRF's Benchmarking Report"): the public sample's median is **about a fifth of that**. The $97 may come from a later edition or a different measure. It could not be traced.

### 2.4 Older CRF material

- **CRF Perspective, 3Q2015** (Caparon, N-AH04): "Using Credit Research Foundation (CRF) Survey results, Deductions negatively impact Accounts Receivables (A/R) somewhere between 1% and 5%." *verified* that the article says it; a share of A/R, not of sales.
- **The earlier "Customer Deductions: Impact on Receivables" edition** (N-AH05, ProQuest abstract seen only as a search snippet): "median level of deductions is now 5% of accounts receivable dollars outstanding", 105 days median to resolve, 280 respondents. Year not seen. *assumed*.
- The 2021 report puts open deductions at a median **½-1% of A/R for ≤$500M** respondents (3.1-5% for larger ones) (N-AH01, *verified*).

### 2.5 RVCF, SCDigest and other association figures (all second-hand)

| Source | Figure (quoted) | Label | ID |
|---|---|---|---|
| **RVCF founder Kim Zablocky, quoted by F. Curtis Barry & Co.** (a fulfilment consultancy; undated) | Retailer compliance "charges have ranged from 0.25%-1.25% of the invoice, the average is 0.4% to 0.8% of one percent"; "The average charge/deduction is $250-300 per occurrence, which could mean multiple deductions on a purchase order-invoice" | *assumed* | N-AH07 |
| RVCF 2012 member survey, via *Inbound Logistics* (Nov 2013) | "96 percent of retail members surveyed ... operate compliance programs that include assessments"; "Only 30 to 40 percent of retailers assess fees for the same non-compliance issues" | *assumed* | N-AH08 |
| RVCF/Auburn/Compliance Networks, "ASN Exposed" (2010), via Craig et al. | "A survey of 42 retailers found that 13 % of inbound shipments experienced ... an inaccurate ASN" | *assumed* (report not found) | N-AH12 |
| SCDigest Retail-Vendor Benchmark Study, via Forbes (Vitasek, 18 Jun 2019) | "only 35% of retailers say their compliance programs are primarily focused on supply chain improvement. In fact, a full 23% of retailers admit their programs are 'dollar-oriented.'" | *assumed* | N-AH09 |
| Business Wire survey (2007), via Chen | "67% of participants used chargebacks if the vendors failed to meet SLA requirements" (100 top retail and consumer-goods companies) | *assumed* | N-AH14 |
| **FMI/GMA joint industry report on unsaleables** (Nov 2005; adjacent pool, not C-19's) | "the average reported rate of unsaleables has grown from 0.75 percent to 1.06 percent in 2004"; "Invoice deductions are increasingly used for unsaleable cost recovery and reimbursement, sometimes without adequate documentation" | *verified* (full PDF) | N-AH11 |

**Derived [our calc]:** RVCF's 0.4-0.8% at $250-300 a chargeback implies **13-32 compliance chargebacks per $1M of sales** (0.6% ÷ $275 ≈ 22). The model assumes 10 per $1M (0.5% at $500).

**Where the vendors' "2-10% of revenue" comes from:** Craig et al. (N-AH12) cite it as "Chargebacks reduce supplier revenue by 2 % to 10 % annually (Zieger, 2003)". The source is a 2003 article in *Frontline Solutions*, a trade magazine. This is the earliest traceable origin found for a figure vendors still repeat. It is not a measurement, and it likely includes trade deductions [our call].

### 2.6 Blocked or gated

Attain's 2015, 2018 and 2021 result pages ask for an email before sending the PDF (checked on archived copies; not used, N-AH10). CRF's Deduction Benchmark Assessment Tool needs data entered in a form (not used). APQC, IOFM and the RVCF/Attain COVID deck were blocked in check AE (N-AE44 to N-AE46) and were not retried.

---

## 3. University and journal research

### 3.1 Peer-reviewed and working papers

| Study | Data | Figures (quoted) | Label | ID |
|---|---|---|---|---|
| **Craig, DeHoratius & Klabjan, "Execution Quality and Chargeback Penalties in Retail Supply Chains"** (Ohio State, Chicago Booth, Northwestern; working paper 12-58, published in *Journal of Operations Management*, 2020/21) | Supplier compliance manuals of **111 retailers**, revenue $0.5B to over $100B (36 department stores, 24 apparel, 17 household goods, 10 electronics) | 63 distinct fulfilment errors, **54 of them execution-quality** errors. Typical charges: "$25 plus $0.50 per affected unit"; "a fixed chargeback of $150"; "10 % of the PO cost"; "a flat fee of $450"; "$150 fixed charge for a missing or incorrect ASN". Model result (not data): the chargeback "deviates from the true cost of the error by between 38 % and 75 %, on average" | *verified* (full working paper) | N-AH12 |
| **Craig, DeHoratius, Jiang & Klabjan (2015)**, *JOM* 38(1), "Execution quality: an analysis of fulfillment errors at a retail distribution center" | One major retailer's distribution-center data | Per the same authors in N-AH12: "fulfillment errors associated with nearly 7 % of the POs of a large retailer"; "chargebacks for execution quality account for 60 % of the dollar value of all chargebacks issued by a retailer". Abstract: the majority of errors involve "documentation, bar coding, and retail ticketing" | abstract *verified*; figures *verified* as the authors' own restatement; the 2015 paper itself is paywalled | N-AH13 |
| Srinivasan, Kekre & Mukhopadhyay (1994), *Management Science*, via Craig et al. | An automotive maker's suppliers | "Shipping discrepancies" affect "12 % of supplier shipments on average"; the modelling assumes "approximately 10 % of purchase orders experience fulfillment errors" | *assumed* (second-hand) | N-AH12 |
| **Chen (Bucknell), "A review and analysis of service level agreements and chargebacks in the retail industry"**, *International Journal of Logistics Management* (2018) | Service-level documents from **73 US retailers'** websites | "Explicit chargebacks with financial penalties are not as prevalent as expected"; flat-fee chargebacks "can be as common as" variable ones. Examples: Big Lots "$250 plus up to 6% of the invoice amount" for a late PO; Pep Boys "5% of cost on items not shipped" below the fill-rate target; a bookseller $200 per short order; a drugstore "$150 penalty per purchase order" below 96% fill. "Fill-rate targets range from 80% to 100%, while more than half of the observations are 100%" | *verified* (author's manuscript, Wayback copy of the Bucknell repository) | N-AH14 |
| Chen (2017), Winter Simulation Conference, "Efficiency of non-compliance chargeback mechanisms" | Simulation | Results "offer counter-evidence to the accusation" that retailers use chargebacks as a revenue source (a model, no field data) | abstract *verified* | N-AH15 |
| **Kulshreshtha, "Big-Box Retail Does Not Kill Bad Products: An Empirical Case Study of Execution Failures in B2B Retail Compliance Chargebacks"** (Research Square preprint, posted 14 Sep 2026; author at ShipMonk, a 3PL) | **39 chargeback cases** logged by one 3PL's compliance team, Jan-Sep 2026, 19 retailers; plus one account's year-to-date ledger with one retailer | "$265,271.19 in chargebacks was requested; formal dispute reduced the finalized liability to $127,540.96, a 51.6 percent reduction". Median per-case reduction 50.4% (IQR 16.9-72.9%), from full reversal to full uphold. Walmart: 3 cases, $23,442.03 requested, 43.2% reduction; Amazon: 4 cases, $53,072.69, 46.5%. Median 27.5 days to resolve. **Single account**: "$64,592.70, of which $10,645.05 (16.5 percent) was reversed following dispute". Labelling and ticketing codes (44.2% of charged value) were "usually successfully" reversed with photos; ASN-accuracy and PO violations (45.4%) were "comparatively harder to dispute" | *verified* (full text via Research Square's public API); **not peer reviewed**; one provider; AI-assisted drafting disclosed | N-AH16 |

**Derived from N-AH16 [our calc]:**
- Average disputed case **$6,802** ($265,271 ÷ 39); Walmart $7,814 a case; Amazon $13,268. Cases pool several deductions, so these are **not** single-deduction sizes.
- The **16.5%** single-account figure is the only neutral-ish measurement found of the share of **compliance** chargeback dollars reversed. It is a share of **all** that account's charged dollars, not only the disputed ones. It is higher than CRF's median invalid × recovered share for all deductions (5.1-10% × 60% ≈ 3-6%). It comes from one apparel account and one retailer. C-19's main targets (OTIF, shortages) are not in its reason codes.
- The **51.6%** figure is a share of dollars the 3PL **chose to dispute**, so it overstates the share of all chargebacks that are wrong.

### 3.2 MIT theses and capstones (real company data)

| Thesis | Sponsor / data | Figures (quoted) | Label | ID |
|---|---|---|---|---|
| **Dasan Potty, Krishnan & Yu, "Increasing Supply Chain Visibility by Incentivizing Stakeholders to Use Blockchain"** (MIT SCM capstone, Jul 2020) | Walmart (sponsor; interviews with three Walmart teams, Oct 2019); context: small-pack / e-commerce deliveries | "only 60% of the suppliers have their shipments reach Walmart DCs on time and in full ... The majority of accountability in OTIF loss is due to shipments not arriving on time"; "only 75% of the shipments that are received at the warehouses had correct PO data". Quotes Bloomberg's "as low as 10 percent" (N-AH24). Its model's baseline OTIF of 0.664 and its penalty formula are **simulation settings, not data** | *verified* (full PDF via Wayback; DSpace blocks direct download); "60%" is unsourced within the text | N-AH17 |
| **Chhabria & Sia, "Designing Inventory Management Strategy for a Fill Rate of 98%"** (MIT SCM capstone, May 2022) | C.H. Robinson's retail consolidation DC; 13 suppliers, 2019-21 order data | "the fill rate metric has been around the low 90s % according to their biggest retailer. This is below the set target of 98% and has resulted in severe fines being charged by this retailer"; "These fines, which are in $ millions are then cascaded to C.H. Robinson"; supplier two's "fill rate was 84% in 2021 ... for supplier five, the fill rate was 83%" | *verified* (full PDF via Wayback) | N-AH18 |
| "Design and process solutions for decreasing vendor defects" (MIT thesis, 2013) | Amazon fulfilment centres | "Over the course of 2012, the project resulted in nearly 300,000 defects and nearly one million dollars in vendor chargebacks" → **~$3.3 per defect** [our calc] | abstract *verified*; full text restricted to MIT (HTTP 401) | N-AH19 |
| "Improving inbound visibility through shipment arrival modeling" (MIT thesis, 2014) | Amazon inbound | "only about half of the purchase orders actually arrives by these dates" (vendors' estimated delivery dates) | abstract *verified*; full text restricted | N-AH20 |

Other MIT theses found by the DSpace search (a 3PL FMCG forecasting thesis, 2023; ResMed channels, 2022; a fashion-retail alignment thesis, 2023; chemical-company service-level theses, 2016) mention OTIF but report no retailer fines (N-AH21, screened).

### 3.3 Auburn University RFID Lab with GS1 US

- **"Project Zipper"** (June 2017-July 2018; 5 retailers, 8 brands, 11 partner pairs, over 1 million items; apparel-led): "When RFID was not implemented, 69 percent of inbound orders (shipped from brands and received by their retailer partners) contained errors. These errors were revealed in picking, shipping, and receiving, resulting in inventory inaccuracies and potential costly chargebacks" (N-AH22, *verified* executive summary).
- **GS1 US, 4 May 2022:** "According to a recent Annual Retail Trade Survey by the U.S. Department of Commerce, industry faces more than $36 billion in claims annually" (N-AH23, *verified* that GS1 says it). The Census Bureau's Annual Retail Trade Survey does not, as far as we know, collect claims or chargebacks, so this attribution is **doubtful** [our call].

**Reading [our call]:** order-level data errors are common (69% of orders in apparel). This cuts both ways for C-19. Many shortage and ASN deductions may be **valid**, because the supplier's own paperwork is wrong. Equally, the retailer's receiving record may be wrong, which is the pool C-19 disputes. No study separates the two.

### 3.4 Other universities

- **University of Arkansas, Walton College Supply Chain Management Research Center:** its research list has no OTIF, fines, chargeback or deduction study (N-AH50, *verified* page). ScholarWorks search returned HTTP 403.
- **Arizona State** (Dale Rogers, via W.P. Carey Knowledge, Dec 2017): qualitative only (N-AH46).
- **Auburn's Brian Gibson** is quoted on retail compliance (N-AH09), but no Auburn chargeback study with rates was found.
- Georgia Tech, Penn State, Michigan State, Ohio State (other than Craig) and Tennessee: **not searched** after the search budget ran out (§9).
- OpenAlex title searches for "OTIF" return mainly Latin American lean-manufacturing case studies, with nothing on US retailer fines (N-AH51).

---

## 4. Regulators

### 4.1 UK Groceries Code Adjudicator (GCA)

**Tesco investigation report (26 Jan 2016; covering 25 Jun 2013 to 5 Feb 2015)** (N-AH29, *verified* full PDF). It found no totals or rates. The relevant findings:
- Delays arose from "deductions for alleged short deliveries (resulting from a practice commonly referred to as drop-and-drive), duplicate invoicing, deductions for unknown or unagreed items" (§7.5). "In 2014 35% of direct suppliers responding to the Survey said they had experienced delay in payments".
- **Short-delivery and service-level charges:** "Some suppliers experienced difficulties as a result of not receiving electronic proof of delivery notes from Tesco" (§27.1). "One supplier reported facing a 'constant fight' with Tesco about prospective deductions for service level charges which were usually successfully resisted by the supplier" (§27.3). "Tesco had unilaterally deducted a significant sum of money from a supplier for incorrect short delivery charges which took six months to be repaid" (§27.4).
- **Retailer-side audit claims (the mirror):** "More than one instance of Tesco making unilateral deductions for audit claims of over £1 million which were subsequently acknowledged as not being due" (§26.4(b)). Also "Tesco agreeing that audit claims which had been deducted were invalid but nonetheless refused to issue credit notes until the supplier agreed to review new claims" (§26.4(c)).
- **Cost to suppliers:** "Tesco account managers spent between 5% and 20% of their time seeking to resolve payment issues with Tesco" (§40.2).

**GCA annual surveys (share of UK direct grocery suppliers reporting each issue)** (N-AH30 to N-AH32, N-AH35; *verified*):

| Issue | 2014 | 2017 | 2024 | 2025 |
|---|---|---|---|---|
| Any Code issue | 79% | — | 33% | 30% |
| **Incorrect deductions from invoices** | **46%** | **32%** | — | — |
| Forensic auditing (retailer post-audit claims) | 45% | 12% | — | — |
| Delay in payments | 35% (Tesco report) | "highest concern" | 14% | 11% |
| Inadequate processes to resolve invoice discrepancies promptly | — | — | 21% | 17% |
| "Not allowing time (30 days) to challenge proposed invoice deductions, or deducting even if challenged" | — | — | 11% | 9% |
| "Delays in or not receiving payment when there are disagreements about deliveries, including drop and drive" | — | — | 11% | 9% |

- **Amazon** is the outlier among the 14 regulated retailers. Suppliers' "perceived Code compliance" scores were 59% (2023), 47% (2024) and 66% (2025), against "over 90%" for every other designated retailer in 2025 (Statutory Review, Apr 2026, ¶48, ¶71; N-AH35). 13% of Amazon's suppliers raised an issue with it in 2025 (N-AH30).
- **The GCA opened an investigation into Amazon** (20 Jun 2025) under paragraph 5 (no delay in payments). It covers "its processes for managing and escalating supplier concerns relating to deductions from payments, and its use of settlements of deductions in its commercial negotiations". It was still open in the 2025/26 annual report (16 Jul 2026) (N-AH33, *verified* news pages). **No findings or amounts are public yet.**
- A consultant quoted by *The Grocer* speaks for "a group of 12 fmcg companies with turnover ranging from £50m to £300m, several of which claim they are owed more than £1m by the online giant" (27 Jun 2025; N-AH34, *assumed*).

### 4.2 Canada

- **FHCP** (the manufacturers' association) to the Competition Bureau, Dec 2022 (N-AH36, *verified*): manufacturers "have been hit with millions of dollars of supply chain fines" for missing "order fulfilment targets unilaterally set by the grocer". Trade spend "rose from 25.3% to 28.2%" of gross sales in 2013-2017, against about 18% in the US. That figure is trade, so out of scope, but it is an upper bound on how much retailers take in total.
- *Globe and Mail*, 15 Apr 2022 (N-AH37): one supplier saw "a fivefold increase in fines from retailers since the pandemic began"; no amounts.
- **OGSCC** first public report (16 Jun 2026, covering Jan-May 2026): 9 issue submissions, with the commonest concerns including "disputed deductions and administrative fees" (N-AH38, search summary only, *assumed*). **No deduction amounts.**

### 4.3 Australia and the EU

- **ACCC Supermarkets Inquiry final report** (Feb 2025; N-AH39, *verified* full PDF). It lists the rebates and payments in Coles, Woolworths and Metcash trading agreements (volume, distribution, settlement, collaboration rebates and wastage), almost all trade. It recommends that large supermarkets "provide suppliers with an itemised account of all payments and deductions off invoices at the end of each financial year". **No non-trade rates.**
- **The Emerson review of the Food and Grocery Code** (Jun 2024; N-AH40): screened via a search summary only; no deduction figures were seen.
- **European Commission evaluation of the UTP directive** (1 Dec 2025; N-AH41, *verified*): "more than 4 500 investigations opened between 2021 and 2024"; "754 cases and €41.9 million in fines between 2022 and 2024". No supplier-deduction amounts.

### 4.4 United States

- **FTC staff report "Feeding America in a Time of Crisis"** (Mar 2024; N-AH27, *verified* full PDF):
  - "Walmart tightened its OTIF requirements in September 2020, requiring suppliers to achieve 98 percent OTIF compliance to avoid fines of 3 percent of the cost of goods."
  - "A review of contracts included in this study suggests that larger customers generally imposed more stringent OTIF requirements and penalties on their suppliers than smaller customers did."
  - Suppliers "shift[ed] product allocations to favor the buyers with OTIF policies".
  - But "Our study did not attempt to empirically evaluate the magnitude". **No fine amounts.** It cites McKinsey's Nov 2022 survey (N-AH28).
- **McKinsey, "Great service—but who's paying?"** (18 Nov 2022; survey of 35 senior leaders at 28 North American CPG companies, per the FTC; N-AH28, *verified* via Wayback):
  - "More than half of the CPG companies in our survey reported that retailers have tightened their on-time and in-full (OTIF) requirements by narrowing delivery windows and increasing fines for noncompliance."
  - "85 percent ... at least one core retail customer has shifted from 'requested' delivery dates to 'scheduled' or 'committed' delivery dates."
  - **No fine rate.**
- **SEC and Saks (2005-07)** (N-AH42): Saks "improperly collected up to $21.5 million from vendors during fiscal years 1999-2003" (AP via NBC, *verified* page). That was **markdown allowances**, which is trade and out of scope. It is the one US regulator-documented case of wrongful retailer deductions found. The SEC complaint PDF is a scan with no text layer, so it was not read.
- **FTC 2001/2003 slotting reports, GAO and USDA:** not reached after the search budget ran out (§9). Slotting is trade in any case.

---

## 5. Retailers' own statements and the distribution of supplier OTIF performance

### 5.1 What retailers have said (at source or as reported)

| Date | Statement | Source | Label | ID |
|---|---|---|---|---|
| 2017 (Walmart presentation to vendors, via Bloomberg, 12 Jul 2017) | "OTIF scores for Wal-Mart's top 75 suppliers -- including Procter & Gamble Co. and Unilever -- had been as low as 10 percent, according to Trainor's presentation. And not one had reached the 95 percent long-term target." The programme "aims to add $1 billion to revenue". "Items that are late or missing during a one-month period will incur a fine of 3 percent of their value." Walmart is "27 percent" of Clorox's sales | Bloomberg (M. Boyle), Wayback copy | *verified* (reported at source) | N-AH24 |
| Mar 2019 (as reported Sep 2020) | "Walmart reported in March 2019 OTIF shipments on food and consumables were still at a dismal 40%." | Talk Business & Politics (K. Souza, 3 Sep 2020) | *verified* page; the Walmart original was not seen | N-AH25 |
| Sep 2020 | 98% across all orders from 15 Sep 2020, fine 3% of COGS. Previous goals: GM 95%, food 97.5%, truckload prepaid 87%, collect 95%, LTL 70% | FreightWaves (M. Solomon, 11 Sep 2020); FTC (N-AH27) | *verified* | N-AH26 |
| 2019-20 (Walmart interviews) | "only 60% of the suppliers have their shipments reach Walmart DCs on time and in full" | MIT capstone sponsored by Walmart | *verified* (unsourced within the text) | N-AH17 |
| 2012-14 (Amazon) | about half of POs arrive by the vendor's estimated date; ~$1M of vendor chargebacks on ~300,000 defects in one programme year | MIT theses | abstracts *verified* | N-AH20, N-AH19 |

No retailer statement quantifies **total fines collected**, the **share of fines reversed on dispute**, or the **share of suppliers under the goal** (as check AE also found).

### 5.2 The distribution of supplier OTIF performance: what exists

**Not found:** any neutral or semi-neutral distribution of suppliers' OTIF scores, for example the share below 90% or 95%. What exists is a set of point observations (§5.1 and N-AE50, N-AE51). They do not describe the same population or year.

**Bounding fines from the rule (fine ≈ share of cases failing × 3%, when below the goal) [our calc]:**

| Observation | Cases failing | Implied fine, % of sales to that retailer | Caveat |
|---|---|---|---|
| Walmart food and consumables at 40% OTIF (Mar 2019) | 60% | **~1.8%** | Early in the programme; whether every failing case was fined is not known |
| Walmart's top 75 suppliers "as low as 10%" (2017) | up to 90% | up to 2.7% | Before fines began (Aug 2017); the worst cases only |
| Consolidator's fill rate "low 90s" vs a 98% target (2021) | ~7-9% short | **~0.2-0.3%** (in-full only) | One 3PL serving 13 suppliers; the fines were "$ millions" in total |
| Two suppliers at 83-84% fill (2021) | ~16-17% | ~0.5% | Same consolidator |
| Only 4% of shipments >12 h late (McKinsey 2019, N-AE50) | on-time failures in single digits | ~0-0.2% on-time part | A survey of 24 companies, not suppliers' scorecards |
| Observed: 0.16% of COGS in Uber Freight's Walmart customers (Feb 2024, N-AE51) | — | 0.16% | An interested party; already known |

**Reading [our call]:** Walmart's goals were loosened in 2024 to 90% on time and 95% in full (N-AE51). The more recent observations sit in the **0.15-0.5% of Walmart sales** range for OTIF fines, with 2019-era programme-start levels much higher. The **recoverable** part is only the invalid fines inside that range, which no source measures.

---

## 6. Retailer-side recovery audit (the mirror image)

- **PRGX's filings:** the FY2010 10-K discloses no overpayment rate, audited volume or reversal share, only "We process over 1.5 million client files each year" (N-AH44, *verified* page extraction). FY2018 was read in check X (N-X12) with the same result. **Not found in filings:** recovery as a percentage of client purchases.
- **PRGX marketing (vendor, *assumed*):** "$1M for every $1B in supplier spend" (**0.1%**); contingency "10-40% of recovered amounts"; "recover $1.8 billion in annual cash flow" for clients (N-AH43).
- **GAO on PRG** (known, N-X04): 0.48% of purchases for a new client, falling to about 0.1% once fixes are in. The Defense Department collected $2.6M of the $29.3M identified (8.9%).
- **Share of retailer claims later reversed:** **not found** as a rate. The evidence is anecdotal: the Tesco audit claims of over £1M later "acknowledged as not being due" (N-AH29). UK suppliers reporting forensic-audit issues fell from 45% to 12% once eight of ten retailers agreed to a "current year plus two" limit in 2014 (N-AH32).
- **CRF 2021** (N-AH01): 15% of respondents saw post-audit claims rise in the past 12 months (19% in 2018), 13% saw them fall and 72% saw no change. "69% of all respondents confirmed that most post audit claims are taken within 2 years."

**Reading [our call]:** the mirror industry runs at about **0.1% of purchases** after its first year. That is roughly the same order as the vendors' 0.2% (STAT, N-AE30) and **ten times** the ≤$500M median chain in §7.1. Retailer-side auditors pick large retailers with billions of purchases. Neither figure measures a small supplier's own deductions.

---

## 7. For the coordinator (not a call)

Everything here is **[our calc]** or **[our call]**. Nothing is decided.

### 7.1 The chain re-run on the best neutral primary (CRF 2021, ≤$500M)

| Setting | Non-trade % of sales | Invalid share | Recovered share | **Recoverable, % of sales** | Fee (25%) per $1M of sales |
|---|---|---|---|---|---|
| ≤$500M medians (band midpoints) | 0.375% | 3.05% | 70% | **0.008%** | $20 |
| ≤$500M low bands | 0.125% | 0.5-1% | 70% | ~0.001% | ~$2 |
| All-size medians, 2021 | 0.75% | 7.55% | 60% | 0.034% | $85 |
| All-size medians, 2023 (recovery kept at 60%) | 1.55% | 7.55% | 60% | 0.070% | $175 |
| **≤$500M midpoint means** (product of means, assuming independence) | 1.14% | 13.9% | 63% | **0.10%** | $250 |
| ≤$500M upper quartiles | ~1.0% | ~25% | 90% | 0.23% | $560 |
| *Model central (check AE; for comparison)* | *0.5%* | *10%* | *60%* | *0.03%* | *$75* |

**How many small suppliers clear the kill line?** A crude simulation takes the ≤$500M distributions (Q37 × Q33). It spreads answers uniformly within each band (lowest bands 0.02-0.25% and 0.1-1%) and treats the two answers as independent [our call]. It gives the "invalid found" rate, non-trade % × invalid share, before recovery. This is the kill test's measure, but on **all-deduction** invalid shares:

| Population | Under 0.05% (kill) | 0.05-0.17% (conditional) | **≥ 0.17% (pass)** | Median | 75th pct | 90th pct | Mean |
|---|---|---|---|---|---|---|---|
| ≤$500M, 2021 | **~64%** | ~18% | **~18%** | 0.023% | 0.10% | 0.39% | 0.16% |
| All sizes, 2023 (no size split) | ~46% | ~19% | ~35% | 0.064% | 0.33% | 1.05% | 0.38% |

**Caveats (all [our call]):**
- (a) Q33's invalid share covers **all** deduction dollars, trade included; the kill test counts non-trade only.
- (b) Independence is an assumption. Suppliers with heavy compliance deductions may also have more invalid ones, or fewer.
- (c) 48% of ≤$500M respondents track no deduction metrics, so their bands are estimates.
- (d) CRF's "invalid" means found and charged back **today**, before any product. C-19's pitch is that suppliers miss some.
- (e) Only 40 respondents are ≤$500M, so each is worth about 2.5 points.

### 7.2 What the neutral evidence says about each model input

| Model input (check AE central) | Neutral evidence | Direction for C-19 [our call] |
|---|---|---|
| Non-trade 0.5% of sales | ≤$500M median ¼-½% (2021); all sizes ½-1% (2021) → 1.1-2% (2023); RVCF 0.4-0.8% (second-hand); a long upper tail (14% of small firms at 3-10%) | Central **about right for 2021 small firms**; possibly low if the 2023 rise reached small firms (unknown) |
| Invalid 10% | ≤$500M median **1.1-5%**, mean ~14%, **bimodal** (54% at ≤5%, 43% at ≥15%); one 3PL account: 16.5% of compliance chargeback $ reversed | Central **high for the median small firm, low for the upper 40%**. The input is really two populations |
| Recovered 60% | ≤$500M median **70%** (mean 63%) | Slightly **favourable** |
| Recoverable 0.03% | ≤$500M median chain **~0.008%**; mean chain **~0.10%** | **The median small supplier is below the kill line; the average is above the conditional band** |
| $500 average deduction | Published fee schedules $150-450 per PO incident plus 3-10%-of-PO charges; RVCF "$250-300 per occurrence"; Amazon defect chargebacks ~$3; auto write-off thresholds $10-25 at ≤$500M | **$250-300 is better supported than $500** for compliance chargebacks. At $300, check AE §9.3 needs an 8.3% invalid share to cover US labour |
| 10 deductions per $1M | ~11 per $1M of **all** types (CRF c. 2012), so fewer if only non-trade are counted; 13-32 **compliance** chargebacks per $1M (RVCF, second-hand) | **Mixed.** The model's 10 sits inside the range. RVCF's figures imply more, and so more triage cost |
| 5 min triage / 20 min dispute | Manual benchmark ~52 min per deduction, all types (CRF median throughput); upper quartile ~17 min; a 3PL's disputes take a median 27.5 days elapsed | **No neutral support for 5 minutes.** It is a software assumption; manual practice is ~3-10× longer |
| Days to resolve | 30 days to decide, 90 to close (CRF 2021); DDO 39 days | Consistent with retailers' windows (check U) |

**Worked example at the ≤$500M median [our calc]:** $1M of big-box sales at 0.375% gives $3,750 of non-trade deductions: 7.5 deductions at $500 (12.5 at $300).
- Invalid at 3.05%: $114, of which 70% is recovered ($80), so the fee is **$20**.
- Cost at US collector wages, at $500 each: triage 7.5 × 5 min = $21.06, plus disputes 0.23 × 20 min = $2.57, so **$23.63**. **The fee does not cover labour at US wages.**
- Offshore ($12/h): $8.42 per $1M, leaving $11.6 per $1M. Break-even on the $600 fixed cost needs **~$52M** of big-box sales. A $5,000 fee needs **$250M**.
- At the ≤$500M **mean** chain (0.10% recovered; 22.8 deductions per $1M at $500; 13.9% invalid): fee $250 per $1M against ~$100 of US labour, leaving $150 per $1M. Break-even is **~$4M**; a $5,000 fee comes at **$20M**.

### 7.3 Can the desk prove C-19 profitable or unprofitable? [our call]

- **Not from neutral sources.** The neutral evidence brackets the recoverable rate for a ≤$500M supplier at **~0.01% (median) to ~0.10% (mean)**. The frozen kill line of 0.05% found (0.03% recovered) sits **inside** that bracket.
- **The shape matters more than the centre.** On the only size-split neutral data, roughly **three in five** small suppliers would fail Test 1 and roughly **one in five** would pass. The rest fall in the conditional band. The business, if there is one, is in **finding the upper tail**: suppliers with non-trade deductions of 1% of sales or more **and** a high invalid share. Food, beverage and grocery skews higher on non-trade (31% of respondents at 3.1-5% of sales) and on auto write-off thresholds ($100-250).
- **The decisive missing number** is the invalid share for **non-trade deductions alone** in a small supplier's own ledger. No neutral survey splits it. The one account-level measurement (16.5%, apparel, one retailer) is above the model's 10%. The CRF all-deduction median for small firms (1.1-5%) is below it. This matches the kill condition's own design: the S5 look-back measures exactly this.
- **Market-level signals point the same way as the tail reading.** Only 3% of ≤$500M respondents outsource any deduction task, and 48% track no metrics. The pool is under-served, but most small suppliers do not see enough money to act.
- **One source-quality point for the model:** the vendor-quoted "$97 per deduction" attributed to CRF (N-AE40) is **not** what CRF's public benchmark sample shows ($18.80 median). The vendor "2-10% of revenue" traces back to a 2003 trade-magazine article (§2.5).

---

## 8. Sources

Access: **full** = whole document downloaded and read or searched; **page extraction** = read through the WebFetch tool; **API** = public JSON interface; **snippet** = search-result text only; **blocked** = refused.

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AH01 | Attain Consulting Group for the Credit Research Foundation, "Customer Deductions: 2021 Benchmark Survey" (111 respondents) | Jul 2021 | https://www.crfonline.org/wp-content/uploads/2021/07/2021-Deduction-Benchmarks_final.pdf | full PDF | Definitions; medians by size; Q33, Q34, Q37, Q38, Q40, Q57, Q58 distributions; time, DDO, write-offs, top non-trade reasons, post-audit |
| N-AH02 | CRF panel, "Insights from the CRF Deductions Survey" (2023 Deduction Metrics Survey; Attain, Carixa, CRF, IAB, RVCF) | 18 Mar 2024 | https://www.crfonline.org/wp-content/uploads/2024/03/3-Deduction-survey-panel.pdf (duplicate: …/13-Deduction-survey-panel.pdf) | full PDF; charts read from rendered slides | Non-trade % distribution and median 1.1-2%; invalid distribution; trend; write-off thresholds; KPI tracking |
| N-AH03 | CRF, "Benchmarking Report — Company Report for: Sample Data Company" (all industries n = 287; prepared 27 Apr 2012) | posted Dec 2017 | https://www.crfonline.org/wp-content/uploads/2017/12/Sample.pdf | full PDF | Deduction metric quartiles and definitions |
| N-AH04 | C. Caparon, "Unlike Fine Wine, Deductions Do Not Grow Better With Age", Perspective by CRF | 3Q 2015 | https://www.crfonline.org/wp-content/uploads/2018/02/Unlike-Fine-Wine-Deductions-Do-Not-Get-Better-With-Age-3Q2015.pdf | full PDF | Deductions 1-5% of A/R |
| N-AH05 | "New CRF survey quantifies effects of deductions" (ProQuest record; CRF "Customer Deductions: Impact on Receivables") | not seen | https://www.proquest.com/docview/201277360 | snippet (page: redirect loop) | 5% of A/R; 105 days; 280 respondents |
| N-AH06 | CRF public media listing (WordPress API) and files screened: deduction automation deck (Mar 2024), IAB Perspective (Q2 2026), IAB CRF Expo 2019, Carixa post-audit note (Q2 2023) | 2019-2026 | https://www.crfonline.org/wp-json/wp/v2/media?search=deduction | API; full PDFs | Discovery; vendor pieces screened, not used |
| N-AH07 | F. Curtis Barry & Co., "How to Develop and Implement a Comprehensive Vendor Compliance Program" (quoting RVCF founder Kim Zablocky) | undated | https://www.fcbco.com/blog/develop-and-implement-vendor-compliance-program | page extraction | 0.25-1.25% of invoice, average 0.4-0.8%; $250-300 per occurrence |
| N-AH08 | *Inbound Logistics*, "Vendor Compliance: Setting Them Straight" | Nov 2013 | https://www.inboundlogistics.com/articles/vendor-compliance-setting-them-straight/ | page extraction | RVCF 2012: 96% of retailers run assessment programmes; 30-40% fee alignment |
| N-AH09 | Forbes, K. Vitasek, "Abusive Compliance Practices Hurt Retailers And Their Vendors" (Wayback copy) | 18 Jun 2019 | https://www.forbes.com/sites/katevitasek/2019/06/18/abusive-compliance-practices-hurt-retailers-and-their-vendors/ | full (archived HTML) | SCDigest benchmark: 35% and 23% |
| N-AH10 | Attain Consulting Group, 2015/2018/2021 survey result pages (Wayback copies) | 2015-2021 | https://attainconsultinggroup.com/2021-customer-deduction-benchmark-survey/ | page read; PDF gated by email, **not used** | Confirms gating only |
| N-AH11 | FMI and GMA, "Improving Unsaleables Management Business Practices — Joint Industry Recommendations" | Nov 2005 | https://www.fmi.org/docs/supply/gma_unsale.pdf | full PDF | Unsaleables 0.75% (1995) → 1.06% (2004); deductions for unsaleables |
| N-AH12 | N. Craig, N. DeHoratius, D. Klabjan, "Execution Quality and Chargeback Penalties in Retail Supply Chains" (Chicago Booth WP 12-58; SSRN 2637594; *JOM* 2020/21) | WP c. 2018-19 | https://dynresmanagement.com/uploads/3/5/2/7/35274584/chargebacks.pdf | full PDF | 111 retailers' manuals; charge examples; 7% of POs; 60% of chargeback $; Zieger 2-10%; Retail VCF 13% ASN; Srinivasan 12% |
| N-AH13 | N. Craig, N. DeHoratius, Y. Jiang, D. Klabjan, "Execution quality: An analysis of fulfillment errors at a retail distribution center", *JOM* 38(1): 25-40 | 2015 | https://doi.org/10.1016/j.jom.2015.07.007 | abstract (OpenAlex); paywalled | Error types; figures via N-AH12 |
| N-AH14 | C.-M. J. Chen, "A review and analysis of service level agreements and chargebacks in the retail industry", *IJLM* (author manuscript) | 2018 | https://web.archive.org/web/20240420063436/https://digitalcommons.bucknell.edu/cgi/viewcontent.cgi?article=2789&context=fac_journ | full PDF (Wayback; live repository 403) | 73 retailers; fee examples; fill-rate targets; 67% (Business Wire 2007) |
| N-AH15 | C.-M. J. Chen, "Efficiency of non-compliance chargeback mechanisms in retail supply chains", Winter Simulation Conference | 2017 | https://doi.org/10.1109/wsc.2017.8248056 | abstract (OpenAlex) | Model only |
| N-AH16 | A. Kulshreshtha, "Big-Box Retail Does Not Kill Bad Products: An Empirical Case Study of Execution Failures in B2B Retail Compliance Chargebacks", Research Square preprint rs-11001474 v1 | posted 14 Sep 2026 | https://www.researchsquare.com/article/rs-11001474/v1 | full text via public API | 39 cases: 51.6% reduction; tables by retailer; single-account 16.5%; 27.5 days |
| N-AH17 | V. Krishnan Dasan Potty & Z. Yu, "Increasing Supply Chain Visibility by Incentivizing Stakeholders to Use Blockchain", MIT SCM capstone (sponsor Walmart) | Jul 2020 | https://dspace.mit.edu/handle/1721.1/126391 (PDF via Wayback) | full PDF | 60% of suppliers OTIF; 75% correct PO data; model settings |
| N-AH18 | A. P. Chhabria & D. Sia, "Designing Inventory Management Strategy for a Fill Rate of 98%", MIT SCM capstone (sponsor C.H. Robinson) | May 2022 | https://dspace.mit.edu/handle/1721.1/142907 (PDF via Wayback) | full PDF | Fill rate low 90s vs 98%; fines "$ millions"; suppliers at 83-84% |
| N-AH19 | "Design and process solutions for decreasing vendor defects", MIT thesis (Amazon) | 2013 | https://dspace.mit.edu/handle/1721.1/81002 | abstract (DSpace API); full text 401 | ~300,000 defects, ~$1M chargebacks |
| N-AH20 | "Improving inbound visibility through shipment arrival modeling", MIT thesis (Amazon) | 2014 | https://dspace.mit.edu/handle/1721.1/90779 | abstract (DSpace API); full text 401 | About half of POs arrive by estimated date |
| N-AH21 | MIT DSpace search API, ~12 queries (OTIF, chargeback, fines, deductions, Walmart OTIF), and theses screened (1721.1/151229, /146694, /152447, /102022, /102029) | 2026-09-22 | https://dspace.mit.edu/server/api/discover/search/objects?query=OTIF | API | Discovery; no further fine data |
| N-AH22 | GS1 US and Auburn University RFID Lab, "EPC/RFID Retail Supply Chain Data Exchange Study" (Project Zipper) executive summary; press release 10 Oct 2018 | 2018 | https://documents.gs1us.org/adobe/assets/deliver/urn:aaid:aem:a8d86484-ffce-498d-8c59-fc1223437d58/Case-Study-Executive-Summary-EPC-RFID-Retail-Supply-Chain-Data-Exchange-Study.pdf | full PDF; release page extraction | 69% of inbound orders with errors; sample |
| N-AH23 | GS1 US, "New GS1 US Guideline Supports Retail Industry With Claims Compliance" | 4 May 2022 | https://www.gs1us.org/industries-and-insights/media-center/press-releases/new-gs1-us-guideline-supports-retail-industry-with-claims-compliance | page extraction | "$36 billion in claims" (doubtful attribution) |
| N-AH24 | Bloomberg, M. Boyle, "Fined for Arriving Early? Wal-Mart Puts Its Suppliers on Notice" (Wayback copy) | 12 Jul 2017 | https://www.bloomberg.com/news/articles/2017-07-12/fined-for-arriving-early-wal-mart-puts-its-suppliers-on-notice | full (archived HTML) | Top 75 "as low as 10 percent"; none at 95%; $1B; 3%; Clorox 27% |
| N-AH25 | Talk Business & Politics, K. Souza, "Walmart demands all suppliers comply with 98 percent on-time in-full shipment rule" | 3 Sep 2020 | https://talkbusiness.net/2020/09/walmart-demands-all-suppliers-comply-with-98-on-time-in-full-shipment-rule/ | page extraction (quotes checked) | Food and consumables 40% (Mar 2019) |
| N-AH26 | FreightWaves, M. Solomon, "Walmart tightens on-time, in-full requirements" | 11 Sep 2020 | https://www.freightwaves.com/news/walmart-tightens-on-time-in-full-requirements | page extraction | Goals before and after Sep 2020 |
| N-AH27 | FTC staff report, "Feeding America in a Time of Crisis: The United States Grocery Supply Chain and the COVID-19 Pandemic" | Mar 2024 | https://www.ftc.gov/system/files/ftc_gov/pdf/p162318supplychainreport2024.pdf | full PDF | OTIF section pp. 15-16; no amounts |
| N-AH28 | McKinsey, S. Lal & C. Regnier, "Great service—but who's paying?" (Wayback copy) | 18 Nov 2022 | https://www.mckinsey.com/capabilities/operations/our-insights/great-service-but-whos-paying | full (archived HTML) | >half tightened OTIF; 85% moved to scheduled dates |
| N-AH29 | Groceries Code Adjudicator, "Investigation into Tesco plc" | 26 Jan 2016 | https://assets.publishing.service.gov.uk/media/5a81a094ed915d74e33ff39b/GCA_Tesco_plc_final_report_26012016_-_version_for_download.pdf | full PDF | §7.5, §26.4, §27, §40.2 |
| N-AH30 | GCA / YouGov, "GCA Annual Survey 2025" (conference slides) | 2025 | https://assets.publishing.service.gov.uk/media/68dd577ec487360cc70ca001/YouGov_slides_-_GCA_Annual_conference_2025.pdf | full PDF | Issue shares 2024-2025; Amazon 13% |
| N-AH31 | GOV.UK, "GCA survey shows continued improved treatment of grocery suppliers" | 25 Jun 2025 | https://www.gov.uk/government/news/gca-survey-shows-continued-improved-treatment-of-grocery-suppliers | page extraction | Delay 14% → 11%; invoice discrepancies 21% → 17% |
| N-AH32 | GOV.UK, "Tacon marks end of first term with survey showing significant progress for groceries suppliers" | 26 Jun 2017 | https://www.gov.uk/government/news/tacon-marks-end-of-first-term-with-survey-showing-significant-progress-for-groceries-suppliers | page extraction | Forensic auditing 45% → 12%; incorrect deductions 46% → 32% |
| N-AH33 | GCA, Notice of Investigation (Amazon) and news; "GCA publishes 2025/26 annual report" | 20 Jun 2025; 16 Jul 2026 | https://assets.publishing.service.gov.uk/media/68550c16f812712f8458155c/Notice_of_Investigation.pdf ; https://www.gov.uk/government/news/gca-publishes-202526-annual-report | page extraction / search summary | Scope of the Amazon investigation; still open |
| N-AH34 | *The Grocer*, I. Quinn, "What's at stake in the GCA's investigation into Amazon?" | 27 Jun 2025 | https://www.thegrocer.co.uk/analysis-and-features/whats-at-stake-in-the-gcas-investigation-into-amazon/706205.article | page extraction | Consultant claims (12 FMCG firms; >£1m owed) |
| N-AH35 | Department for Business and Trade, "Statutory Review of the Groceries Code Adjudicator: 2022-2025" (deposited paper DEP2026-0269) | Apr 2026 | https://data.parliament.uk/DepositedPapers/Files/DEP2026-0269/Statutory_Review_of_the_Groceries_Code_Adjudicator.pdf | full PDF | Issue share 79% → 30%; Amazon 59/47/66% vs >90% |
| N-AH36 | FHCP, response to the Competition Bureau's market study of retail grocery | Dec 2022 | https://competition-bureau.canada.ca/en/how-we-foster-competition/consultations/response-food-health-consumer-products-canada-consultation-market-study-retail-grocery | page extraction | "millions of dollars of supply chain fines"; trade spend 25.3% → 28.2% |
| N-AH37 | *Globe and Mail*, S. Krashinsky Robertson, "Manufacturers raise concerns over grocery stores' fines amid supply chain disruptions" | 15 Apr 2022 | https://www.theglobeandmail.com/business/article-grocery-store-fines-supply-chain/ | page extraction | Fivefold increase (one supplier) |
| N-AH38 | OGSCC spring report on early implementation of the Canada Grocery Code (via Yahoo/CFIG) | 16 Jun 2026 | https://ca.finance.yahoo.com/news/ogscc-releases-spring-report-early-130000037.html | snippet | 9 submissions; disputed deductions among concerns |
| N-AH39 | ACCC, Supermarkets Inquiry 2024-25 final report | Feb 2025 (released 21 Mar 2025) | https://www.accc.gov.au/system/files/supermarkets-inquiry_1.pdf | full PDF (searched) | Deduction types (Table 6.2); itemised-deduction recommendation; no rates |
| N-AH40 | C. Emerson, Independent Review of the Food and Grocery Code of Conduct, final report | Jun 2024 | https://treasury.gov.au/publication/p2024-534717-final-report | snippet | Screened; no deduction figures seen |
| N-AH41 | European Commission (DG AGRI), "Commission carried out evaluation of the Directive on unfair trading practices" | 1 Dec 2025 | https://agriculture.ec.europa.eu/media/news/commission-carried-out-evaluation-directive-unfair-trading-practices-2025-12-01_en | page extraction | Investigations, cases, fines |
| N-AH42 | NBC News (AP), "Apparel suppliers, retailers at odds"; SEC complaint v. Saks (2007) | 24 Apr 2005; 2007 | https://www.nbcnews.com/id/wbna7592508 ; https://www.sec.gov/files/litigation/complaints/2007/comp20266.pdf | page extraction; SEC PDF scanned (no text) | Saks $21.5M improper markdown allowances (trade) |
| N-AH43 | PRGX, "Accounts Payable Recovery Audit Guide" and retail recovery page | read 2026-09-22 | https://www.prgx.com/guides/ap-recovery-audit-services-guide/ ; https://www.prgx.com/solutions/recovery-audit/retail-merchandise/ | page extraction | $1M per $1B (0.1%); 10-40% contingency; $1.8B a year (vendor) |
| N-AH44 | PRGX Global, Form 10-K FY2010 | filed 2011 | https://www.sec.gov/Archives/edgar/data/0001007330/000095012311025938/g26477e10vk.htm | page extraction | No rates disclosed; 1.5 million client files |
| N-AH45 | Modern Materials Handling / Supply Chain 24/7, S. Bolduc, "Keeping Pace with Walmart's On-Time Delivery Requirements" | 5 Feb 2018 | https://www.mmh.com/article/keeping_pace_with_walmarts_on_time_delivery_requirements | page extraction | Restates Bloomberg; LTL 36% goal |
| N-AH46 | ASU W.P. Carey Knowledge (Dec 2017) and Retail Dive (12 Jul 2017) on Walmart OTIF | 2017 | https://news.wpcarey.asu.edu/20171204-fined-arriving-early-walmart-puts-its-suppliers-notice ; https://www.retaildive.com/news/Walmart-supplier-fine-logistics-delivery-OTIF-risk/447038 | page extraction | Screened; restatements |
| N-AH47 | FMI news, A.T. Kearney data-synchronization case studies | 12 Jan 2003 | https://www.fmi.org/newsroom/news-archive/view/2003/01/12/… | page extraction | Screened; no deduction figures |
| N-AH48 | The Strategic Sourceror, "Understanding and improving retail-supplier relationships" (on the SCDigest study) | Feb 2016 | https://www.strategicsourceror.com/2016/02/understanding-and-improving-retail.html | page extraction | Screened; expectations only |
| N-AH49 | Weber Logistics, "How to Reduce Chargebacks in Your Vendor Compliance Program" (3PL white paper) | undated | https://www.weberlogistics.com/hs-fs/file-18466406.pdf | full PDF | Vendor examples only (10% late; $195/BOL; $10/carton ASN) |
| N-AH50 | University of Arkansas, Walton College SCMRC research list; ScholarWorks search | read 2026-09-22 | https://walton.uark.edu/initiatives/supply-chain-research/research.php | page extraction; ScholarWorks 403 | No OTIF or chargeback study listed |
| N-AH51 | OpenAlex and Semantic Scholar APIs (~20 queries; several rate-limited) | 2026-09-22 | https://api.openalex.org/works?filter=title.search:OTIF | API | Discovery of N-AH12 to N-AH16; OTIF literature screened |
| N-AH52 | QuickBox, "Vendor Compliance: How to Reduce Retail Chargebacks" | Jul 2026 | https://www.quickbox.com/blog/vendor-compliance-retail-chargebacks | page extraction | Screened: "5-15% of manufacturer invoices" as "industry estimates" (vendor, not used) |

**Earlier IDs used:** N-N29, N-U29, N-AE30, N-AE40, N-AE44 to N-AE46, N-AE49, N-AE50, N-AE51, N-AE52, N-X04, N-X12.

**Screened count:** 52 new IDs covering about 60 documents and pages, plus about 45 search queries and about 30 API queries.

---

## 9. Could not access, or not found

**Could not access:**
- **The web-search budget** shared by this session **ran out part-way through** this check. The following were therefore **not searched**:
  - the FTC's 2001 slotting workshop report and its 2003 slotting case-study report (trade in any case);
  - GAO and USDA ERS work on retailer fees;
  - public summaries from APQC, IOFM, Aberdeen and Hackett;
  - NACM *Business Credit* and Credit Congress decks;
  - *Journal of Business Logistics* and *IJPDLM* articles beyond what OpenAlex returned;
  - Georgia Tech, Penn State, Michigan State, Ohio State and Tennessee repositories;
  - the Canadian Competition Bureau's 2023 grocery report;
  - the GCA's Co-op investigation;
  - public statements by Kroger, Target, Home Depot, Lowe's and Costco quantifying OTIF compliance.
- **MIT DSpace** blocks direct PDF downloads behind a human-verification page. The two capstones were read from Wayback copies. The two Amazon theses' full texts are restricted to MIT (HTTP 401); only their abstracts were read.
- **SSRN** (403) for Chen 2016 and Craig et al.; alternative copies were used. The **2015 Craig et al. JOM paper** is paywalled; its figures come from the same authors' later paper.
- **Bucknell Digital Commons** (403); a Wayback copy was used. **UArk ScholarWorks** search (403).
- **Bloomberg** (paywall); a Wayback copy was used. **ProQuest** (redirect loop): only a search snippet of the older CRF edition.
- **Attain's survey PDFs** (2015, 2018, 2021) are behind an email form and were not used. The 2021 report was read instead from **CRF's public copy** (N-AH01), which has no gate.
- **The SEC complaint against Saks** (scanned, no text layer); not OCR'd because it concerns trade allowances.
- **The FMI/GMA unsaleables PDF** could not be read by the fetch tool (image-encoded); it was extracted locally.

**Not found (searched, appears not to be public):**
- **Any neutral distribution of suppliers' OTIF scores**, such as the share of suppliers below 90% or 95%, for Walmart or any other retailer. Only point observations exist (§5).
- **Any retailer's total OTIF or compliance fines collected**, or the share reversed on dispute.
- **The invalid share for non-trade deductions alone**, in any survey. CRF measures it across all deductions. The single account-level figure is one 3PL account (N-AH16).
- **The recovery share in the 2023 CRF survey**, and **any size split** in the 2023 survey.
- **A neutral average size for a single non-trade deduction.** What exists: published fee schedules, RVCF's second-hand "$250-300", and Amazon's ~$3 per defect chargeback.
- **Neutral minutes per non-trade deduction**, as distinct from all deduction processing.
- **PRGX's recovery rate as a percentage of client purchases** in its filings. **The share of retailer post-audit claims later reversed**, as a rate.
- **The original "ASN Exposed" report** (Retail VCF, Auburn, Compliance Networks, 2010), and **the SCDigest Retail-Vendor Benchmark Study** itself.
- **The source of the vendor-quoted "$97 per deduction"** attributed to CRF's Benchmarking Report.
- **Findings of the GCA's Amazon investigation** (still open as of 16 Jul 2026).
