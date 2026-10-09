# S5 check AR, adversarial review

- **What this is:** an adversarial check of check AR's web evidence on our own cost per customer, SOC 2, the SMC3 licence and the SaaS benchmarks used to judge payback. Each claim was tested to see whether it breaks. No objection was invented: a claim that survives is reported as a result too.
- **File checked:** `research/s5_check_AR_c09_software_cost.md` (64 ledger rows C-AR01 to C-AR65, C-AR12 merged; §0 verdicts; body sections §AR1-§AR6; Coincidence watch). It was not edited. No other project file was read apart from `research/s5_check_AM_adversarial.md`, used for format only.
- **Date:** 2026-10-08. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.** It proposes no price and no fee form.
- **Searches used:** 9 of the 10 allowed. **Fetches made:** about 75: page and PDF downloads, 4 USAspending API calls (3 award records and 1 transactions query, public, no key), 1 fetch-tool read (Recurly, captcha on plain download), and one older Xero investor deck found by a search. Downloads are kept in the session scratchpad.
- **No identity was sent. Nobody was contacted.** A generic browser user-agent only. No logins, forms, quote requests, API keys or PACER. SEC EDGAR was not fetched; Xero and Weave were read on their own ASX and investor-relations copies.
- **Rows checked in full (all seven tests):** 45. These are the 40 load-bearing (Y) rows plus 5 N rows that feed a §0 figure or a coincidence (C-AR19, 53, 54, 60, 62).
  - **Sampled (at least the existence test), covering AR1-AR5:** 19 rows: C-AR02, 04, 08, 09, 11, 18, 23, 25, 29, 32, 33, 35, 36, 37, 38, 39, 52, 58, 59.
  - **Not checked:** none. C-AR12 was merged by the checked file and holds no claim.
- **How labels are used here:** **KEEP-verified** means the row's own sentence is true as written about its own population (an IT service desk, a survey's respondents, one federal buyer). Where that population is not our case, the "New label" column adds "*assumed* as a stand-in". **KEEP-assumed** means the number itself is a vendor figure, a secondary write-up, a snippet or our own judgement. **NARROW** states the smaller reading that survives.

**Words used here:**
- **Handle minute:** a minute an agent spends on a contact. MetricNet's cost per handle minute is the whole desk's cost divided by these minutes, so idle time and overhead are inside it.
- **MRR churn:** monthly recurring revenue lost from customers who leave, as a share of all MRR. **Logo churn:** customers who leave, as a share of customers. They are not the same number.
- **Subscription vs total gross margin:** subscription margin counts only the software revenue and its costs; total margin also counts services such as onboarding, which usually lose money.
- **Ratio-implied payback:** months of gross profit needed to repay the sales and marketing spent per $1 of new revenue (New CAC ratio ÷ gross margin × 12).
- **Look-alike:** two equal-looking numbers that measure different things.

---

## §0 Result in one table

**Row verdicts**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|
| 48 | 9 | 7 | **0** | 0 |

**No row is discarded.** Every quote that was re-fetched is in its source, word for word or nearly so (small differences listed in §5), and every [our calc] reproduces. What breaks is how some numbers are read:
- **Xero's 1.14% is revenue churn, not customer churn.** Xero's own glossary defines it as MRR lost from leaving subscribers (C-AR48).
- **The 8-month CAC payback median contradicts the same report's New CAC ratio.** That ratio implies about 25-31 months of gross profit for a company whose sales spend is all on new customers, close to Weave's ~31-33 (C-AR40).
- **"Small SaaS gross margin 77-85%" leaves out the same report's own small-company cut:** total margin 70% under $1M ARR and 74% at $1-5M (C-AR43).
- **The hosting range starts below the checked file's own build.** The median sub-$1M-ARR firm spends $18,360 a year on hosting, about 3-8 times the lean stack (C-AR64).
- **The SOC 2 totals count only cash paid to the platform, the auditor and the tester.** The same vendor page lists readiness, preparation and internal staff costs (C-AR20).
- **The invoice paper's 7% is a share of consistency checks, not of invoices** (C-AR61).

**Verdicts on the §0 question rows**

| Question | Proposed verdict | This review | Reason |
|---|---|---|---|
| AR1a support cost | Narrowed | **AGREE** | MetricNet's figures are exact and are fully loaded by MetricNet's own published method (§5). They come from internal IT desks with a peer group of unstated size and region. Vendor pages put B2B software tickets at $30-60 and 2.3 contacts per issue, but no source is given, so this is logged as a concern only (§4.1, §6 #11). The ticket count stays [our call]. |
| AR1b hosting per customer | Answered from the web (list prices), with our stack as the assumption | **AGREE for list prices only.** The per-customer range is a floor | The checked file's own build is $3.6-6.0k a year, not $2.4-6.0k: the $2.4k leaves out the tooling it says to add. Small SaaS firms report a median $18,360 a year on hosting (SaaS Capital, under $1M ARR) (§1 #4). |
| AR1c cost-of-revenue shares | Answered | **AGREE**, with one addition | SaaS Capital also books **DevOps** as cost of revenue: 10% of ARR and $28,950 at the median sub-$1M firm. §AR6 has no line for it (B4). |
| AR2 SOC 2 | Narrowed | **AGREE** | Platform list prices are exact. The totals exclude readiness, preparation, internal time and tools, which the same vendor page lists. Directory figures for specialist Type II audits run to about $45k, above the checked file's $30k ceiling (*assumed*, §6 #7). |
| AR3 SMC3 licence | Narrowed (multi-customer unit and price not answerable) | **AGREE** | Every quote is exact. The FEMA price is **one buyer's micro-purchase, renewed**: a single observation, not three (B8). One counter-search found no price; a reseller lists CzarLite with no price (§6 #13). |
| AR3b carriers' base tariffs | Narrowed | **AGREE** | The Saia snippet was not reproduced. SMC3 sells "SAIA 5700" as a data module, with four editions between 2025-10-01 and 2026-07-06 (§6 #12). |
| AR4a gross margin | Answered (for software in general) | **AGREE with the verdict; the small-company figures need correcting** | Benchmarkit 2025 by ARR: total margin 70% under $1M and 74% at $1-5M; subscription margin 77% at $1-5M. The report says margin "is typically a little lower" below $5M (§1 #3, B1). |
| AR4b churn | Answered as a range | **AGREE**, wording fix | Xero is MRR churn (§1 #2). The range still holds: Xero's ≈12.9% of MRR a year sits beside Weave's 89% GRR. |
| AR4c CAC and payback | Narrowed | **AGREE, and narrower** | The survey's 8- and 14-month medians contradict its own New CAC ratio, which implies 25-31 months (§1 #1). A KeyBanc/Sapphire median of about 23 months (2022 data) reached us only through a third-party guide (*assumed*). Xero's FY21 deck gives 14.8 months of revenue, about 17 of gross profit [our calc]. |
| AR5a onboarding completion | Not answerable from the web | **AGREE** | Userpilot's 37.5% counts new users, trial sign-ups included, in products that use Userpilot. |
| AR5b correcting machine-read tables | Narrowed | **AGREE**, wording fix | Table figures are exact. The invoice paper's 7% is of checks, not invoices (§1 #6). One currency search found no 2025 benchmark showing whole-table exact match near 100% (§6 #18). |

**One-line reading:** the §0 sentence "about $100-400 a year for reading, hosting and steady-state support" does not match the checked file's own §AR6 sum of **$97-652**. With the corrections here (the build's own hosting floor, survey-median hosting as the high case, steady-state storage), the range is about **$109-784** **[our calc]** (§3). The reading that machine reading and hosting are not what decides C-09 survives.

---

## §1 Discards and narrowings (most important first)

No row is discarded. Seven are narrowed, and eleven body statements need the same treatment (B1-B11 below the table).

| # | Claim ID | What was claimed | What the source actually says (quote ≤40 words) | Verdict | Why, and the restricted reading |
|---|---|---|---|---|---|
| 1 | **C-AR40** (and §AR4.4 #3, §AR6) | Median CAC payback is 8 months at $1-5k ACV and 14 months at $5-10k. The checked file carries 8-14 months as one end of the range | Benchmarkit 2025, p. 17: "New CAC Ratio calculation formula is: Total Sales & Marketing expenses / New Customer ARR". p. 22: payback is "on a Gross Margin adjusted basis". N = 148 across 8 ACV bands | **NARROW** | The chart values are exact (p. 23: $1-5k 6/8/12; $5-10k 13/14/18). But the same report's New CAC ratio ($2.00 at $1-5k, $1.60 at $5-10k) implies **30 and 25 months** at its 77% small-company subscription margin, 31 and 25 at 80% **[our calc]**. For a young company nearly all sales spend goes on new customers, so the ratio is the closer reading. Benchmarkit's own $1-5k ratio quartiles ($0.46-2.46) imply 7-37 months. **Restricted reading:** self-reported medians from small samples, contradicted inside the same report. Ratio-implied payback (25-31 months), Weave (~27-38 months) and a KeyBanc/Sapphire median of ~23 months (*assumed*) agree with each other, not with 8-14 months. |
| 2 | **C-AR48** (and §0 AR4b) | "Xero 1.14% a month of customers (≈12.9% a year)" | Xero FY21 investor deck, glossary: "value of monthly recurring revenue (MRR) from subscribers who leave Xero in a month as a percentage of the total MRR at the start of that month." | **NARROW** | The FY26 release prints "Average monthly churn (1.14%)" and does not define it. Xero's own earlier glossary defines the same series ("MRR churn", FY20 1.13%, FY21 1.01%) by revenue. **Restricted reading:** Xero loses about 1.14% of MRR a month to subscribers who leave, ≈12.9% a year [our calc ✓]. That is revenue churn, before downgrades; it is not a customer count. The 83.9% gross margin is exact. |
| 3 | **C-AR43** (and §0 AR4a, §AR4.4 #1) | Median gross margin 77% (total) and 81% (subscription); read as small-SaaS margins of "about 77-85%" | Benchmarkit 2025, p. 42: "at the lowest levels (< $5M) that Gross Margin is typically a little lower." p. 40 chart: under $1M ARR **70%** (50-81%); $1-5M **74%** (64-85%) | **NARROW** | 77% and 81% are medians across all sizes (N = 196 and 76). The same report's size cut gives total margin 70% under $1M and 74% at $1-5M, and subscription margin **77%** (40-90%) at $1-5M. OpenView's 85% under $1M (subscription; third-party copy) rose 15 points in one year, a sign of a small band. **Restricted reading:** the median subscription margin for software firms under $5M ARR is 77-85%, and total margin 70-74%. Weave's split shows why: subscription and payments 77.9%, onboarding −152.9%, total 72.1%. |
| 4 | **C-AR64** (and §AR1.3, §AR6) | Hosting $2.4-6.0k a year, $24-60 a customer at 100; the share-of-revenue figure is "the higher bound" | SaaS Capital 2023, chart "Less than $1 Million in ARR": Hosting "$18,360"; DevOps "$28,950" (median dollars a year) | **NARROW** | The list prices and sums reproduce. But (a) the text adds $100-300 a month of tooling and then uses $2.4k, the stack without it, as the low end. Its own build is **$3.6-6.0k**, $36-60 a customer at 100. (b) The median sub-$1M firm spends **$18,360** on hosting, $184 a customer at 100 **[our calc]**. (c) DevOps labour is a separate cost-of-revenue line in the same survey. **Restricted reading:** $36-60 a customer at 100 is a list-price floor. Real small SaaS firms spend about 3-5 times that, and DevOps labour comes on top. |
| 5 | **C-AR20** (and §AR2.3) | SOC 2 about $29.5-58k in year 1 and $16.5-68k a year after | Secureframe, same page as C-AR17: "Readiness Assessment: $15k - Risk Assessment: $10-20k - Penetration Test: $15k - Compliance Preparation Costs: $25-85k - Formal Audit: $5-150k+ - Annual Maintenance: $10-60k - TOTAL: $80-$350k" | **NARROW** | The sums reproduce. The build takes the platform, audit and test lines and leaves out the rest. The page also lists "Internal costs" (staff time), consultants, training and cyber insurance, and says "Many companies are refusing a Type 1 report and specifically requesting a Type 2". The checked file's ceiling for a later-year audit, $30k, sits under directory estimates for specialist Type II firms of up to about $45k (*assumed*). **Restricted reading:** $29.5-58k and $16.5-68k are the cash paid at list or vendor-range prices to the platform, the auditor and a tester. Internal hours, security tools and insurance are extra and unmeasured. Year 1 may need a Type II if buyers ask for it. |
| 6 | **C-AR61** (and §AR5.2, §AR5.3 #2) | "7% of invoices failed an add-up check" | Invoice paper, §4.2: "The LlamaExtractor passed 93% of these general consistency checks." | **NARROW** | The 94% and 91% are exact. The 93% is **of checks**, not of invoices, and the number of checks per invoice is not given. **Restricted reading:** 7% of consistency checks failed on 102 invoices. The share of invoices with at least one failed check is unknown and at least as high. |
| 7 | **C-AR50** (and §0 AR4c) | Weave ≈$12.1k of sales and marketing per gross new location, payback 31-33 months, "a lower bound on CAC" | Weave release: "Number of customer locations disclosed above includes the impact of the acquisition of TrueLark in May 2025." | **NARROW** (the wording only) | The arithmetic reproduces exactly (§3). The acquisition does push true CAC up. But the file sets location churn equal to 1 − dollar GRR (11%), and logo churn can sit either side of that. At 8-15% logo churn the payback is **27-38 months** **[our calc]**. **Restricted reading:** roughly 27-38 months, central ~32. That is not a lower bound, but still 2-4 times the survey medians. |

**Body statements (not ledger rows) that need the same treatment**

- **B1. §0 AR4a and §AR4.4 #1, "pure software at small scale runs a median of about 77-85%".** Use 77-85% for subscription margin and 70-74% for total margin under $5M ARR (row 3).
- **B2. §0 AR4b, Xero "1.14% a month of customers".** It should read "of MRR, from subscribers who leave" (row 2).
- **B3. §0 AR4c, §AR4.4 #3 and §AR6, "survey medians imply 8-14 months".** Carry 8-14 months only as the self-reported low end. The same survey's cost ratio implies 25-31 months (row 1).
- **B4. §AR1.3 cross-check and §AR6, hosting.** "Small firms run below scale, so the share-of-revenue figure is the higher bound" is not supported. In dollars, the sub-$1M median ($18,360) is far above the lean stack. §AR6 also has no DevOps line, which SaaS Capital books as cost of revenue (10% of ARR under $1M).
- **B5. §AR5.3 #2, "about 7% failed a sum check".** It should be 7% of checks (row 6).
- **B6. §AR6 storage "~$1".** That is year 1 only. A year's packets cost about $1.2 to keep for a year; with seven years kept, the steady-state cost is about **$6-9 a year** **[our calc]**. Negligible either way.
- **B7. §AR2.1-§AR2.3, platform prices "now firm".** The Vanta listing does not say which framework the Essentials package includes. Vendr's live page puts the median Vanta buyer at **$20,000 a year** (373 purchases), and $15-35k for a single SOC 2 framework at 50-200 staff (*assumed*). Read the platform range as starting list prices.
- **B8. §0 AR3 and §AR3.1, FEMA "in 2019, 2020 and 2021".** This is one buyer's single price, renewed and then extended by an option. The record shows a micro-purchase ("LESS THAN OR EQUAL TO THE MICRO-PURCHASE THRESHOLD"), one offer, firm fixed price. It is one observation, not three. It covers "CzarLite and RateWare web access subscriptions" for one system.
- **B9. §AR3.2, row "USAspending keyword searches … no reseller … found".** That holds only for USAspending. A software marketplace lists CzarLite under SMC3, with "Enquire now" and no price (§6 #13).
- **B10. §0 one-line reading, "about $100-400 a year".** This is inconsistent with the checked file's own §AR6 ($97-652). See the §0 note.
- **B11. Citation details (no effect on numbers).**
  - OpenView's metrics table is on p. 13, not p. 12.
  - MetricNet's price list is on PDF page 41, not slide 22.
  - The 2022 SMC3 release says modules are delivered through "RateWare XL, BatchMark XL, and CzarLite Online".
  - Box's CUAD F1 range without the oracle runs 0.66-0.82, not 0.75-0.82.
  - Vendr's live page now reads 373 purchases and a high of $57,221, not 365 and $56,943.
  - The same CzarLite "license agreement" sentence appears on the shippers' page as well as the LSP page, so it does not mark a separate multi-client licence.

---

## §2 Coincidences found

**Shared origins (merge them into one source)**

| Figures | Rows | Single origin | Effect |
|---|---|---|---|
| $92-103 an hour, used for onboarding help **and** for a success manager's hours | C-AR03, C-AR63, §AR1.5 "high-touch" row | **One MetricNet IT service-desk figure** (cost per email-handling minute, with idle time and overhead inside) | One desk-agent rate stands in for two different jobs. Neither job is measured. |
| FEMA $8,764 "in 2019, 2020 and 2021" | C-AR21, C-AR22 | **One buyer, one negotiated price**, renewed and extended by an option | One observation (B8). |
| Benchmarkit 2025 (HiBob copy), Benchmarkit 2026 page, Aleph write-up | C-AR40-45 | **One survey series**, Benchmarkit with partners. Aleph co-authors the 2026 edition | The checked file already merges C-AR42/45. C-AR44 (2026 page) and C-AR45 (Aleph) are the same 2025 data from two pages. |
| Secureframe's platform price and Secureframe's audit-cost guide | C-AR15, C-AR17 | **The same vendor** | The guide that sizes the "without automation" costs belongs to a firm that sells the automation. The checked file labels C-AR17 *assumed*, correctly. |
| Vendor support-cost pages ($18-35, $25-35 SaaS; $30-60 B2B per ticket) | §6 #11 (not in the ledger) | **One vendor analysis** (LiveChatAI 2025), reposted. One repost derives its figure from an assumed 8% of ARR | Not independent of each other. Not used for any verdict. |
| "Licence per shipper" | C-AR27, 28, 29 | As the checked file says: one SMC3 integration pattern | Confirmed. The IBM page dates from 2018. |
| SaaS Capital hosting 5-6% and $18,360 | C-AR06, C-AR07, C-AR64 cross-check | **One survey** (2023) | The share and the dollars are two readings of one dataset, so they cannot bracket each other. |

**Look-alike numbers (equal values that measure different things)**

| Value | Where it appears | What each measures |
|---|---|---|
| ~80% | Benchmarkit 2026 "80% median software margin" (C-AR44); Aleph "Sub-$5K ACV sits at 80%" (C-AR45); OpenView 80% at $1-5M (C-AR46); Benchmarkit hybrid GRR 80% | Two gross margins and two retention rates |
| 85% | Benchmarkit GRR at $1-5k and $5-10k ACV (C-AR42); OpenView margin under $1M (C-AR46) | Retention, and a subscription gross margin |
| ~14 months | Benchmarkit payback at $5-10k ACV (C-AR40); Xero FY21 "CAC months 14.8" (§6 #3) | One is gross-margin-adjusted and self-reported. Xero's counts months of revenue: 14.8 months of revenue ≈ 17 of gross profit |
| ~12-13% a year | Xero 1.14% a month (C-AR48, MRR); Weave 1 − GRR = 11% (C-AR49, dollars incl. contraction); ChartMogul-type logo churn (C-AR51, customers) | Three different churn bases |
| $7,500 | Already in the checked file's watch | Confirmed: list price points, not a SOC 2 cost |
| 94-98% "accuracy" | Invoice fields 94% (C-AR61); PubTables cell scores ≈0.98 (C-AR56) | Already in the checked file's watch. A third unit, *checks*, joins it (row 6) |
| F1 ≈0.5-0.8 on CUAD | ContractEval 0.50-0.64 (C-AR59); Box 0.66-0.82 (C-AR60) | Same contracts, different tasks: clause identification vs metadata field extraction. Not comparable |

**Circular or indirect citations**
- C-AR19, C-AR39, C-AR62 and the N-AR41 figures are search snippets or secondary summaries. C-AR19 now reads at its source (with live data drift, B11), and C-AR62 appears in two secondary summaries. C-AR39 was not reproduced (§5).
- The "check AA / AJ / A" figures cited in §AR1-§AR6 were not re-read; this review was barred from other project files.

---

## §3 Arithmetic re-done

Every **[our calc]** in check AR reproduces. Rows marked "new" are calculations added here, on the same sources.

| Item | Check AR | Recomputed | Result |
|---|---|---|---|
| C-AR03: $1.54-1.71 × 60 | $92-103 an hour | $92.40-102.60 | ✓ |
| C-AR03, **new**: does cost per minute × handle time = cost per ticket? | — | $24.24 ÷ 13.70 = $1.77 (table $1.71); $19.96 ÷ 13.77 = $1.45 (table $1.54) | Averages of ratios, not ratios of averages. Consistent enough |
| C-AR63 / §AR1.5 steady state | $60-291 | 3 × $19.96 = $59.88; 12 × $24.24 = $290.88 | ✓ |
| §AR1.5 onboarding, first year | $185-616; $245-907 | 2 × $92.40 = $184.80; 6 × $102.60 = $615.60; sums $244.68 / $906.48 | ✓ |
| §AR1.5 top-down; high-touch | $148-390; $647-1,847 | 3.8% / 10% × $3,900 = $148.20 / $390; 7 × $92.4 = $646.80; 18 × $102.6 = $1,846.80 | ✓ |
| C-AR64: stack | $200 a month; $2,400 a year | 2 × $24 + $120 + $5 + $12 + $15 = $200; × 12 = $2,400 | ✓ |
| C-AR64: with tooling | $3.6-6.0k | ($200 + $100) × 12 = $3,600; ($200 + $300) × 12 = $6,000 | ✓, but the stated range starts at $2.4k (§1 #4) |
| C-AR64: per customer | $48-120 / $24-60 / $8-20 at 50 / 100 / 300 | $2,400-6,000 ÷ n ✓. **New:** own build $72-120 / $36-60 / $12-20; SaaS Capital median $18,360 ÷ n = $367 / $184 / $61 | ✓; floor narrowed |
| §AR1.3 share cross-check | $195-234 | 5% / 6% × $3,900 | ✓ |
| Storage | 3,000-4,420 packets; ≈$0.002 each kept 7 years | 2,000 × 1.5 / 2.21 ✓. 1 MB × $0.023 per GB-month × 84 months = $0.00193 ✓. **New:** year 1 = 4,420 × 0.001 GB × $0.023 × 12 = $1.22; with seven years kept, $8.54 a year | ✓; "~$1" is year 1 (B6) |
| C-AR20 year 1 | $29.5-58k | $9,500 + $5,000 + $15,000 = $29,500; $23,000 + $20,000 + $15,000 = $58,000 | ✓ |
| C-AR20 later years | $16.5-53k (to $68k) | $9,500 + $7,000 + $0; $23,000 + $30,000; + $15,000 | ✓ |
| §AR2.3 per customer | $330-1,360 / $165-680 / $55-227 | $16,500-68,000 ÷ 50 / 100 / 300 = $330-1,360 / $165-680 / $55-226.67 | ✓ |
| §AR3.1 FEMA escalated | ≈$9,660 | $8,764 × 1.03 × 1.03 × 1.039 = $9,660.34 | ✓ |
| C-AR65 | 2.2×; $88; $29 | $8,764 ÷ $3,900 = 2.247; ÷ 100 = $87.64; ÷ 300 = $29.21 | ✓ |
| C-AR26 [our call] | FEMA ≈ 11× the $800 module | $8,764 ÷ $800 = 10.96 | ✓ (the "explains" is an inference; the module's unit is unknown) |
| §AR4.4 #4 | 1.6 ÷ 0.8 = 2.0 years | 2.0 | ✓ |
| C-AR40, **new**: ratio-implied payback | — | $2.00 ÷ 0.80 × 12 = 30.0 months; ÷ 0.77 = 31.2; $1.60 ÷ 0.77 × 12 = 24.9; quartiles at $1-5k: $0.46-2.46 ÷ 0.80 × 12 = 6.9-36.9 | Contradicts the 8-14 month medians (§1 #1) |
| C-AR50 Weave | start 34,997; churned 3,850; gross adds 8,478; $12,115; revenue $6,000-6,400; GP $4,349-4,618; 31-33 months | 39,625 − 4,628 = 34,997; 0.11 × 34,997 = 3,850; 8,478; $102,703k ÷ 8,478 = $12,114; $239,024k ÷ 39,625 = $6,032, ÷ 37,311 (average) = $6,406; × 72.1% = $4,349-4,619; $12,114 ÷ GP × 12 = 31.5-33.4 months | ✓ |
| C-AR50, **new**: logo churn 8% / 15% | — | gross adds 7,428 / 9,878; CAC $13,827 / $10,398; payback 35.9-38.2 / 27.0-28.7 months | Range ≈27-38 months (§1 #7) |
| C-AR54 annualising | 12.9%; 23.4%; 53.0% | 1 − (1 − m)¹²: 12.85%; 23.43%; 53.01% | ✓ (Xero is MRR churn) |
| §AR5.3 #1 | about 1 complex table in 3; 1 in 5 overall | 1 − 0.6944 = 30.6% (1 in 3.3); 1 − 0.8138 = 18.6% (1 in 5.4) | ✓ |
| §AR6 running cost | $97-652 | $12 + $1 + $24 + $60 = $97; $300 + $1 + $60 + $291 = $652 | ✓. **New** with B4/B6: $12 + $1 + $36 + $60 = $109 to $300 + $9 + $184 + $291 = $784 |
| C-AR05 TSIA bands | — | 49% + 22% + 13.6% = 84.6%; the 6-10% band (≈15.4%) is not stated on the page | No error |
| **New:** Weave onboarding cost per new location | — | Onboarding cost of revenue $8,757k ÷ 8,478 gross adds ≈ **$1,033**; net of onboarding revenue ($5,294k loss) ≈ $624; per net add $1,892 | A real SMB firm's onboarding cost, set against §AR1.5's $185-616 (§6 #4) |
| **New:** Xero FY21 CAC months on a gross-profit basis | — | 14.8 ÷ 0.86 = 17.2 months | A real SMB firm's payback (§6 #3) |

---

## §4 Concerns, unproven (verdicts unchanged)

1. **MetricNet's peer group.** The deck states neither the size nor the region of its "peer group". Its nominal cost per contact barely moved between 2010 ($22.56) and 2023 ($20.61), and its minimum is $5.92. Both fit a peer group that includes offshore desks, which would make $20-24 low for a US founder-run support line. The deck does not say.
2. **Which tier answers our tickets.** MetricNet's own desktop (second-tier) support costs $88-115 a ticket. A question like "why did the software flag this reweigh?" may need product or freight knowledge, closer to second tier than to a first-tier desk. No source measures this for B2B software.
3. **Lightsail as the stack for a SOC 2 company.** The stack uses a $15 staging database, and Lightsail lists that plan with "No Data encryption". Whether staging would hold customer documents, and whether a SOC 2 auditor would accept the stack without extra network, key-management and logging services, is not shown. Their cost is not in the build.
4. **Onboarding hours.** The 2-6 hours are [our call]. Weave spends about $1,000 of onboarding cost per new location (§3). Its onboarding serves a phone-and-software product (the release does not say what it covers), a different job, so this is a lead, not a measure.
5. **Benchmarkit sample sizes per band.** N = 148 for payback across 8 bands and N = 73 for the New CAC ratio across 6. The $1-5k ratio quartiles span $0.46-2.46. The report itself says the falling GRR "could be due to selection bias of participants".
6. **ChartMogul's 2021-22 data** is more than four years old and covers all of ChartMogul's billing customers, consumer apps included. Its ">$500 a month" band means ACV above $6,000.
7. **PubTables-1M and ICDAR-2013** are scientific and government tables, and the 2021 models were tested on data like their training data. Rate sheets that are scanned, or laid out unlike papers, may score lower. No 2025 benchmark found shows whole-table exact match near 100% for vision-language models (§6 #18).
8. **Userpilot's activation** counts new users, trial sign-ups included. A paying customer loading its own agreements may finish more often, or less often. Which way is unknown.
9. **FEMA's price.** Whether $8,764 is list price or discounted, and how many users it covers, is not in the record. It is firm fixed price, one offer, under simplified acquisition.
10. **Vanta Essentials.** The marketplace listing does not say whether the SOC 2 framework is included or is an add-on.
11. **ChartMogul's NRR-band churn figures (C-AR52).** The page does not say whether they come from the December 2025 analysis of 3,500 companies or from another dataset.

---

## §5 Full verdict table

**Source key** (the URLs behind the short names in the Evidence column):
- [MN] MetricNet 2023 deck, https://www.brighttalk.com/resource/core/447335/benchmarking-roundup---summary-of-2023-service-and-support-benchmarks-v3_954461.pdf
- [MN11] MetricNet/HDI "Metric of the Month: Cost per Ticket" (2011), https://www.thinkhdi.com/~/media/HDICorp/Files/Library-Archive/Insider%20Articles/Cost%20per%20Ticket.pdf
- [TSIA] https://www.tsia.com/blog/top-support-services-questions-answered
- [SC23] https://www.saas-capital.com/wp-content/uploads/2023/10/Spending-Benchmarks-for-Private-B2B-SaaS-Companies-2023-W1.pdf
- [LS] https://aws.amazon.com/lightsail/pricing/
- [DO] https://www.digitalocean.com/pricing/managed-databases
- [MKV] https://aws.amazon.com/marketplace/pp/prodview-5ophamrbfxt44 ; [MKD] https://aws.amazon.com/marketplace/pp/prodview-3ubrmmqkovucy ; [MKS] https://aws.amazon.com/marketplace/pp/prodview-7cpg4l6nufwgq ; [MKP] https://aws.amazon.com/marketplace/pp/prodview-ixyb464cbjkam
- [MKC] https://aws.amazon.com/marketplace/pp/prodview-rd3i3pcsjdjmy ; https://aws.amazon.com/marketplace/pp/prodview-zwdcg5dyj4pay
- [SF] https://secureframe.com/hub/soc-2/audit-cost.md
- [VEN] https://www.vendr.com/marketplace/vanta
- [USA] https://api.usaspending.gov/api/v2/awards/CONT_AWD_70FA3019P00000010_7022_-NONE-_-NONE-/ ; …/CONT_AWD_70FA3020P00000006_7022_-NONE-_-NONE-/ ; …/CONT_AWD_HTC71108M0011_9700_-NONE-_-NONE-/ ; transactions: POST https://api.usaspending.gov/api/v2/transactions/
- [P27] https://www.smc3.com/press-releases-20260903.htm ; [P25] https://www.smc3.com/press-releases-20241001.htm ; [P0828] https://www.smc3.com/press-releases-20260828.htm ; [P22] https://smc3.com/press-releases-20211206.htm
- [CZL] https://www.smc3.com/czarlitexl-lsp.htm ; [CZS] https://www.smc3.com/czarlitexl-shippers.htm ; [RWL] https://www.smc3.com/ratewarexl-lsp.htm ; [TP] https://www.smc3.com/technology-providers.htm ; [TERMS] https://www.smc3.com/terms-and-conditions.htm
- [BRO] https://www.smc3.com/knowledge-hub/brochures/SMC3_Brochure_Family_Of_Expert_Solutions_19100.pdf ; [WR] https://transition.smc3.com/knowledge-hub/data-sheets/SMC3_DataSheet_webRater_21410.pdf ; [AUD] https://www.smc3.com/knowledge-hub/data-sheets/SMC3_Data_Sheet_Freight_Payment_Audit_Toolkit_29236-L.pdf ; [ALL] https://www.smc3.com/knowledge-hub/data-sheets/Alliance_Partner_DataSheet_25034.pdf
- [MOD] https://smc3.com/carrier-data-modules.jsp?Search=A ; [MODS] https://smc3.com/carrier-data-modules.jsp?Search=S
- [IBM] https://www.ibm.com/support/pages/setting-tariffs ; [ORA] https://docs.oracle.com/en/cloud/saas/transportation/25c/otmca/Chunk1909926867.html ; [SCC] https://supplychaincloud.atlassian.net/wiki/spaces/SCCS/pages/1414168623/RateWare+XL+CzarLite+Credentials ; [MHL] https://www.materialhandling247.com/article/3gtms_expands_partnership_with_smc3/3gtms
- [SWO] https://platform.softwareone.com/product/czarlite/PCP-0059-0173
- [BM25] https://www.hibob.com/wp-content/uploads/2025-SaaS-Performance-Metrics-Benchmarks.pdf ; [BM26] https://www.benchmarkit.ai/2026-saas-ai-native-metrics ; [ALEPH] https://www.getaleph.com/answers/gross-revenue-retention-saas-2026
- [OV] https://consultingedge.substack.com/api/v1/file/60377f4c-98be-48ea-9f31-438c64eb2fa1.pdf
- [SC25] https://www.saas-capital.com/wp-content/uploads/2025/09/RB32WS1-2025-B2B-SaaS-Retention-Benchmarks.pdf
- [XERO] https://announcements.asx.com.au/asxpdf/20260514/pdf/06zkqzlkq0xnph.pdf ; [XERO21] Xero FY21 investor presentation (ASX copy on a quote host), https://quoteapi.com/resources/4ec85c869fdae450/announcements/xro.asx/3A567051/XRO_Investor_Presentation_FY21_Annual_Results.pdf?embed=1
- [WEAVE] https://s21.q4cdn.com/507868397/files/doc_news/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-2026.pdf
- [CMB] https://chartmogul.com/blog/good-customer-churn-rate/ ; [CMM] https://chartmogul.com/saas-metrics/customer-churn/ ; [REC] https://recurly.com/research/churn-rate-benchmarks/ (fetch tool)
- [UP] https://userpilot.com/saas-product-metrics/
- [PT] https://arxiv.org/pdf/2110.00061 ; [ALN] https://arxiv.org/pdf/2303.00716 ; [CUAD] https://arxiv.org/pdf/2103.06268 ; [CE] https://arxiv.org/pdf/2508.03080 ; [INV] https://arxiv.org/pdf/2510.15727 ; [BOX] https://arxiv.org/pdf/2510.19334

**Tests:** 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search or counter-fetch, 7 arithmetic.

| Claim ID | Test(s) run | Verdict | Reason | Evidence (source + quote) | New label |
|---|---|---|---|---|---|
| C-AR01 | 1-6 | KEEP-verified | Exact. "Fully loaded" is not stated in the deck but matches MetricNet's published method. Peer group size and region not stated (§4.1). Vendor pages run higher, unsourced | [MN] slide 11: "Average Cost per Web Ticket/Email Contact $24.24 $5.92 $19.96 $58.54"; [MN11]: "Salaries and benefits for indirect personnel … Technology expense … Facilities expenses" | *verified* (IT service desks); *assumed* as a stand-in for SaaS support |
| C-AR02 | 1 | KEEP-verified | Exact | [MN] slide 11: "Average Cost per Contact (incl. Self-Help) $17.07 $5.91 $14.80 $34.17" | *verified* (IT desks) |
| C-AR03 | 1-7 | KEEP-verified | Exact; $92.40-102.60 ✓. A rate per handle minute, with idle time and overhead inside; agent utilisation is 45.3% (PDF page 15, 2023 column). Also used for success-manager hours (§2) | [MN] slide 11: "Average Cost per Web Ticket/Email Minute $1.71 $0.92 $1.54 $2.89" | *verified* (IT desks); hourly use for onboarding *assumed* |
| C-AR04 | 1 | KEEP-verified | Exact; not comparable, as the checked file says | [MN] slide 17: "Tickets per User per Month 0.38 0.17 0.39 0.67" | *verified*; not comparable |
| C-AR05 | 1-6 | KEEP-verified | Exact. The page does not describe its population; "mostly larger technology firms" is the checked file's own description. Share of total revenue | [TSIA]: "49% of companies report that their support cost of goods sold (COGS) falls between 0% and 3.8% of revenue." | *verified* (TSIA data, population unstated) |
| C-AR06 | 1-6 | KEEP-verified | Text exact; chart read here from the page image: hosting 5 / 6 / 5%, DevOps 10% under $1M, customer success 10% to $20M | [SC23] p. 4: "a typical B2B company with $3 Million to $5 Million in ARR spends the following as a median percent of ARR: • 5% on Hosting Costs • 5% on DevOps Costs" | *verified* (survey) |
| C-AR07 | 1-6 | KEEP-verified | Chart values exact. The $18,360 also narrows C-AR64 | [SC23] p. 5 chart "Less than $1 Million in ARR": "$18,360" Hosting; "$28,950" DevOps; "$31,000" Customer Success | *verified* (chart) |
| C-AR08 | 1 | KEEP-verified | Chart values exact | [SC23] p. 6 chart "$1 - $3 Million in ARR": "$115,250" Hosting; "$159,380" Customer Success; "$220,000" Sales | *verified* (chart) |
| C-AR09 | 1 | KEEP-verified | Exact | [SC23] p. 2: "The total median spend across all departments is 91% of Annual Recurring Revenue (ARR) for bootstrapped companies while equity-backed are spending 120% of ARR." | *verified* |
| C-AR10 | 1-6 | KEEP-verified | Exact and current; the price comes before the specs in the page's order. The 1 GB database plan lists "No Data encryption" (§4.3) | [LS]: "$60 Standard plan USD/mo $120 High availability plan USD/mo 4 GB Memory 2 Core Processor 120 GB SSD Disk" | *verified* (list) |
| C-AR11 | 1 | KEEP-verified | Exact | [DO]: "Storage range: 10 GiB - 30 GiB. $0.215/GiB/mo, 10 GiB increments. $0.02254 $15.15" | *verified* (list) |
| C-AR13 | 1-6 | KEEP-verified | Exact. Which framework Essentials includes is not stated (§4.10). Vendr's paid median is $20k | [MKV]: "Essentials Package Starting cost for 1-20 employees $14,000.00 Professional Package Starting cost for 1-20 employees $23,000.00" | *verified* (list; starting price) |
| C-AR14 | 1-5 | KEEP-verified | Exact | [MKD]: "Access to the Drata SaaS platform with capacity for a 100 FTE org $25,000.00 SOC 2 Framework SOC 2 2017 control set $7,500.00" | *verified* (list) |
| C-AR15 | 1-5 | KEEP-verified | Exact | [MKS]: "Platform Access the Secureframe Platform up to 100 Employees $7,500.00 First Framework Choice of any Framework $7,500.00" | *verified* (list) |
| C-AR16 | 1-5 | KEEP-verified | Exact; a "starting at" price | [MKP]: "starting at $2000 each. This is an add-on to the Sprinto Starter Platform $2,000.00" | *verified* (list; starting price) |
| C-AR17 | 1-6 | KEEP-assumed | Exact. The same page also gives Type 2 "$7-100k for the audit alone" and a $80-350k total (C-AR20). Vendor interest (§2) | [SF]: "For the audit alone, you can expect the SOC 2 Type 1 cost to be around $5-20k, while the SOC 2 Type 2 cost is $7k-150k on average." | *assumed* (vendor) |
| C-AR18 | 1 | KEEP-verified | Exact on one listing; the other listing uses marketplace boilerplate ("request a private offer") | [MKC]: "Pricing is based on your specific requirements, including the Trust Services Criteria in scope, system complexity, and the reporting period." | *verified* (absence) |
| C-AR19 | 1-6 | KEEP-assumed | Read at the source. Same median, live data drifted (373 purchases; high $57,221). A broker with an interest | [VEN]: "Median buyer pays $20,000 per yearBased on data from 373 purchases, with buyers saving 30% on average." | *assumed* (broker's own data); drop the "snippet" flag |
| C-AR20 | 1-7 | **NARROW** | Sums ✓. Leaves out cost lines listed on the same source page; Type II may be needed in year 1 (§1 #5) | [SF]: "Readiness Assessment: $15k - Risk Assessment: $10-20k - Penetration Test: $15k - Compliance Preparation Costs: $25-85k - Formal Audit: $5-150k+ - Annual Maintenance: $10-60k - TOTAL: $80-$350k" | **[our calc]** ✓; external cash only |
| C-AR21 | 1-6 | KEEP-verified | Exact. Micro-purchase, 1 offer, firm fixed price, "SIMPLIFIED ACQUISITION" (B8) | [USA] 70FA3019P00000010: "TO PURCHASE CZARLITE AND RATEWARE WEB ACCESS SUBSCRIPTIONS FOR THE LOGISTICS SUPPLY CHAIN MANAGEMENT SYSTEM (LSCMS)"; "LESS THAN OR EQUAL TO THE MICRO-PURCHASE THRESHOLD" | *verified* (one buyer) |
| C-AR22 | 1-6 | KEEP-verified | Exact; base and option 1 each $8,764; total obligation $17,528. The same buyer and price as C-AR21 (§2) | [USA] transactions: "THE PURPOSE OF THIS MODIFICATION IS TO EXERCISE OPTION PERIOD 1, INCREASE PURCHASE ORDER AMOUNT AND EXTEND THE PERIOD OF PERFORMANCE." | *verified*; not independent of C-AR21 |
| C-AR23 | 1 | KEEP-verified | Exact; total obligation $5,500; sole source | [USA] HTC71108M0011: "NMFC DATA LICENSE RENEWAL"; "ONLY ONE SOURCE" | *verified* (old; class data) |
| C-AR24 | 1-5 | KEEP-verified | Exact | [P27]: "SMC³ will implement a 3.9% increase on Czarlite®, RateWare® XL, CarrierConnect® XL and BatchMark® XL license fees in 2027." | *verified* |
| C-AR25 | 1 | KEEP-verified | Exact | [P25]: "SMC³ will implement a 3% increase on Czarlite®, RateWare® XL … license fees in 2025. RateWare XL data modules pricing will remain the same." | *verified* |
| C-AR26 | 1-6 | KEEP-verified | Exact; one wording slip (B11). Unit and period not stated | [P22]: "Data Module Updated Rate CzarLite $800 … Carrier Tariff Stock $300 The modules will continue to offer best-in-class data delivered through RateWare XL, BatchMark XL, and CzarLite Online" | *verified* (unit unknown) |
| C-AR27 | 1-6 | KEEP-verified | Exact; page modified 08 December 2018; the TMS loads the tariff data for the shipper | [IBM]: "Negotiate a license with SMC to use the tariff in Sterling TMS." "No other shippers can use this tariff unless they have also been authorized by SMC." | *verified* (IBM's practice, 2018) |
| C-AR28 | 1-6 | KEEP-verified | Exact | [SCC]: "These values are provided by SMC3. If you need any of these credentials, reach out to your SMC3 contact regarding your RateWare XL license." | *verified* |
| C-AR29 | 1 | KEEP-verified | Exact | [ORA]: "glog.RatingEngine.RatewareXL.License= These properties should be added to the CUSTOM Property Set." | *verified* |
| C-AR30 | 1-6 | KEEP-verified | Exact. The "license agreement" sentence is also on the shippers' page (B11) | [RWL]: "Manage and optimize LTL rating complexity and logic for multiple shippers, in both density and class-based pricing"; [CZL]: "on behalf of multiple customers using the same base rate system" | *verified* (a multi-client offer exists; terms unknown) |
| C-AR31 | 1-5 | KEEP-verified | Exact; a freight-payment firm's testimonial; PI# 29236-L 04/2026 | [AUD]: "When you're auditing thousands of freight bills for multiple shippers and LSPs, speed, accuracy and automations make all the difference." | *verified* (that SMC3 publishes it) |
| C-AR32 | 1 | KEEP-verified | Exact; PDF dated March 2016 | [BRO]: "CzarLite has been licensed to more than 1,500 shippers, as well as over 300 logistics intermediaries." | *verified*; old |
| C-AR33 | 1 | KEEP-verified | Exact | [TP]: "With SMC³, a single integration point delivers access to all rates, points of service and transit times." | *verified* |
| C-AR34 | 1-6 | KEEP-verified | Exact; ABF 504-AX row present. Saia 5700 also sold as modules, four editions in nine months (§6 #12) | [MOD]: "data modules are designed for use in the SMC³ RateWare and SMC³ BatchMark products"; "29300 ABF 504-AX, US/US 06/22/2026" | *verified* |
| C-AR35 | 1 | KEEP-verified | Exact; governs the website | [TERMS]: "This license does not include any resale or commercial use of this site or its contents" | *verified* |
| C-AR36 | 1 | KEEP-verified | Exact | [WR]: "Access codes are required for CzarLite, CanadaLite and MexicoLite pricing data." | *verified* |
| C-AR37 | 1 | KEEP-verified | Both counts exist | [TERMS]: "SMC³ presently serves more than 3,000 customers throughout the United States and Canada"; [ALL]: "More than 5,000 North American shippers, carriers, logistics service providers and technology partners rely on SMC³" | *verified* (that SMC3 says so) |
| C-AR38 | 1 | KEEP-verified | Loaded directly (HTTP 200); the quote is word for word; licence holder still not stated | [MHL]: "announced it has expanded its partnership with SMC³ to offer the SMC³ RateWare® XL, CarrierConnect® XL and CzarLite® solutions to its customers." | *verified* (trade press); drop the "fetch summary" flag |
| C-AR39 | 1, 6 | KEEP-assumed | Not reproduced in one search; Saia's site is script-rendered. SMC3 sells Saia 5700 as a module, which does not rule out a free copy | [MODS]: "SAIA 5700-AM, US/US, US/CN 07/06/2026" | *assumed* (snippet, unreproduced) |
| C-AR40 | 1-7 | **NARROW** | Chart exact. Contradicted by the same report's New CAC ratio; small bands (§1 #1) | [BM25] p. 22: "CAC Payback Period (CPP) measures how many months it takes to “payback” the Sales and Marketing Expenses for new customers - on a Gross Margin adjusted basis." | *verified* as reported; *assumed* as a planning value |
| C-AR41 | 1-7 | KEEP-verified | Chart exact ($2.46 / $2.00 / $0.46; $1.80 / $1.60 / $1.50). The numerator is all sales and marketing spend. Aleph gives the 2025 overall figure as $1.63 | [BM25] p. 17: "New CAC Ratio calculation formula is: Total Sales & Marketing expenses / New Customer ARR" | *verified* (survey) |
| C-AR42 | 1-6 | KEEP-verified | Chart exact (99/90/85; 91/85/75; 89/85/78). The report flags possible selection bias | [BM25] p. 29: "GRR has continued to decrease slightly over the past three years from 90% to 88% - though this could be due to selection bias of participants." | *verified* (survey) |
| C-AR43 | 1-6 | **NARROW** | All-size medians; the same report's size cut is lower (§1 #3) | [BM25] p. 42: "at the lowest levels (< $5M) that Gross Margin is typically a little lower." p. 40 chart: "< $1M" 70%; "$1M - $5M" 74% | *verified*; small-company reading narrowed |
| C-AR44 | 1, 3 | KEEP-verified | Exact; all sizes; same series as C-AR45 | [BM26]: "80% median software margin \| Stable through 4 years Industry-wide AI infrastructure costs have not yet compressed software margin at the median." | *verified* (page) |
| C-AR45 | 1-6 | KEEP-assumed | Exact; page "Last updated: October 2026"; Aleph co-authors the survey | [ALEPH]: "Sub-$5K ACV sits at 80% — SMB retention is structurally more volatile." | *assumed* (partner write-up) |
| C-AR46 | 1-6 | KEEP-assumed | Exact, on p. 13. Subscription margin, Q2 2023. The under-$1M band moved +15 points in a year. Conflicts with Benchmarkit's cut (§1 #3) | [OV] p. 13: "G ro s s Margins 85% (70-95%) 80% (72-88%)"; p. 10: "Subscription revenue less cost of goods sold divided by subscription revenue" | *assumed* (third-party copy) |
| C-AR47 | 1-6 | KEEP-verified | Figure 1 exact (98% / 90% under $12k); excludes firms under $1M ARR | [SC25] p. 1: "Excludes Companies with less than $1M ARR"; "Bootstrapped companies report NRR of 104% and 92% GRR." | *verified* (survey) |
| C-AR48 | 1-7 | **NARROW** | Revenue churn by Xero's own definition, not customers (§1 #2). Margin exact | [XERO21] glossary: "value of monthly recurring revenue (MRR) from subscribers who leave Xero in a month as a percentage of the total MRR at the start of that month." | *verified*; unit corrected to MRR |
| C-AR49 | 1-6 | KEEP-verified | Exact. The segment split adds subscription-and-payments margin of 77.9% and onboarding at −152.9% | [WEAVE]: "Dollar-Based Gross Retention Rate (GRR) was 89% as of December 31, 2025." "Full year GAAP gross margin of 72.1%" | *verified* |
| C-AR50 | 1-7 | **NARROW** | Arithmetic ✓. "Lower bound" not supported; 27-38 months (§1 #7) | [WEAVE]: "Number of customer locations disclosed above includes the impact of the acquisition of TrueLark in May 2025." | **[our calc]** ✓; range widened |
| C-AR51 | 1-6 | KEEP-verified | Exact; data Nov 2021-Jan 2022 (§4.6) | [CMB]: "For companies with ARPA per month in the range of <$25, the median monthly customer churn rate is 6.1%. It decreases to 2.2% as your ARPA per month increases to >$500." | *verified* (ChartMogul's data); old |
| C-AR52 | 1 | KEEP-verified | Exact; dataset date for this cut not stated (§4.11) | [CMM]: "Companies in the low NRR range have a median 7.3% customer churn, more than four times the 1.7% median of those with ≥100% NRR." | *verified* (as reported) |
| C-AR53 | 1-5 | KEEP-assumed | Exists (fetch tool; captcha on download). A further contradiction: the text gives "$250+ … 3.54%", the table "Over $250/month: Total 3.07%" | [REC]: "$100–$250/month: Total 2.87% \| Voluntary 2.40% \| Involuntary 0.46%"; "Within the $250+ ARPC cohort on the Recurly network, median annual churn sits at 3.54%" | *assumed* (unit unclear) |
| C-AR54 | 7 | KEEP-verified | 12.85% / 23.43% / 53.01% ✓ | (calculation) | **[our calc]** ✓; Xero's input is MRR churn |
| C-AR55 | 1-6 | KEEP-verified | Exact; "B2B SaaS"; first-party data from Userpilot's own dashboards; new users (§4.8) | [UP]: "Average Activation Rate 37.5% Average activation rate 62 Companies B2B SaaS 37.04% Median activation rate" | *verified* (that Userpilot reports it); not a stand-in |
| C-AR56 | 1-7 | KEEP-verified | Table 4 exact; 1 in 3.3 and 1 in 5.4 ✓; 2021 model, in-domain test (§4.7) | [PT] Table 4: "DETR Simple 0.9468 … Complex 0.6944 … All 0.8138" | *verified* (scientific tables) |
| C-AR57 | 1-6 | KEEP-verified | Exact. Structure exact-match on ICDAR-2013 (and its corrected version for 75% / 81%) | [ALN]: "Baseline exact match accuracy for TATR evaluated on the ICDAR-2013 benchmark is 65% when trained on PubTables-1M, 42% when trained on FinTabNet, and 69% combined." | *verified* |
| C-AR58 | 1 | KEEP-verified | Exact | [CUAD]: "DeBERTa-xlarge has the best performance (44.0% Precision @ 80% Recall)" | *verified*; superseded |
| C-AR59 | 1 | KEEP-verified | Exact; Table 3 values match | [CE]: "GPT 4.1 and GPT 4.1 mini, achieve the highest F1 scores (0.641 and 0.644, respectively)" | *verified* |
| C-AR60 | 1-5 | KEEP-assumed | Exact for 0.80 vs 0.75; Table 1 non-oracle range 0.66-0.82 (B11); vendor | [BOX]: "With an 8192-token context window: F1 score of 0.80 (vs. 0.75 baseline)" | *assumed* (vendor) |
| C-AR61 | 1-6 | **NARROW** | 94% / 91% exact; the 93% counts checks, not invoices (§1 #6). Staffing-firm authors; LlamaExtract is a third-party product | [INV] §4.2: "The LlamaExtractor passed 93% of these general consistency checks." | *verified*; unit corrected to checks |
| C-AR62 | 1-3 | KEEP-assumed | Found in two secondary summaries (search). A third summary gives "others" at 22%, against the 14% average | Search summary of a vendor blog: "Ardent Partners' best-in-class performance of 49.2% straight-through processing"; another: "exception rate of just 9%, compared to 22% for other organizations" | *assumed* (secondary) |
| C-AR63 | 1-7 | KEEP-assumed | Arithmetic ✓. Inputs are [our call] and an IT-desk rate. Weave's onboarding cost of ≈$1,000 per new location is a lead (§4.4) | (calculation; inputs C-AR01, C-AR03) | **[our calc]** ✓; inputs *assumed* |
| C-AR64 | 1-7 | **NARROW** | The low end leaves out the build's own tooling; the survey median is 3-5× (§1 #4) | [SC23] p. 5 chart: Hosting "$18,360" (median, firms under $1M ARR) | **[our calc]** ✓; floor $36-60 a customer at 100 |
| C-AR65 | 1, 2, 7 | KEEP-verified | 2.247 ✓; $87.64 ✓; $29.21 ✓. A scale marker, as the checked file says | (calculation; C-AR21) | **[our calc]** ✓ |

---

## §6 Counter-evidence and leads

These are logged, not new findings. Each is tied to the claim it bears on.

| # | Source | What it says (quote ≤40 words) | Ties to | Type |
|---|---|---|---|---|
| 1 | [BM25] pp. 40, 42 | Total margin by ARR: "< $1M" 70% (50-81%); "$1M - $5M" 74% (64-85%). Subscription "$1M - $5M" 77% (40-90%). "at the lowest levels (< $5M) that Gross Margin is typically a little lower." | C-AR43, C-AR46, B1 | Counter-evidence (same report) |
| 2 | [BM25] p. 17, with p. 18 | "New CAC Ratio calculation formula is: Total Sales & Marketing expenses / New Customer ARR". At $1-5k, $2.00 implies ~30 months at 80% margin | C-AR40, B3 | Counter-evidence (same report) |
| 3 | [XERO21] | Glossary: MRR churn is MRR "from subscribers who leave Xero in a month as a percentage of the total MRR". FY21: "MRR churn 1.01%", "CAC months … 14.8" (months of ARPU), gross margin 86.0% | C-AR48; C-AR40 (a real SMB firm at ≈17 months of gross profit) | Counter-evidence; lead |
| 4 | [WEAVE], disaggregated revenue | "Onboarding: Revenue … $ 3,463 … Gross margin … (152.9)%" (FY2025; cost of revenue $8,757k) ≈ $1,033 per gross new location **[our calc]** | C-AR63 (onboarding help $185-616); C-AR49 | Lead (onboarding for a phone-and-software product; content not stated) |
| 5 | [SF] | "Internal costs: Will you be using people or software to manage your compliance program?" "Many companies are refusing a Type 1 report and specifically requesting a Type 2." | C-AR20 | Counter-evidence (vendor) |
| 6 | [SC23] p. 5 | DevOps "$28,950", Hosting "$18,360" (median, under $1M ARR) | C-AR64, B4 | Counter-evidence |
| 7 | Search summaries of SOC 2 directories and a vendor bundle | Specialist Type I "$12K – $20K"; growth-stage Type 2 "$20K–$40K"; one firm's directory estimate "$20K to $45K for Type II"; a fixed-price Type 1 bundle with the audit included "from $24K" | C-AR17, C-AR20 | Lead (*assumed*; directories and vendors) |
| 8 | [VEN] | "companies with 50-200 employees purchasing a single framework (SOC 2) typically see annual contract values in the range of $15,000–$35,000." | C-AR13, C-AR19, B7 | Lead (*assumed*; broker) |
| 9 | Search summary of a third-party guide on the KeyBanc/Sapphire 14th survey | "median CAC payback was roughly 23 months on 2022 data" (100+ companies, median $25.5M ARR) | C-AR40 | Lead (*assumed*; secondary; larger companies) |
| 10 | [ALEPH] | "replace churned ARR with new logos at $1.63 per dollar instead of expanding at $0.80" (2025 data) | C-AR41 (currency) | Lead |
| 11 | Search summaries of support-software vendors | B2B support "$30-$60 per ticket"; "a 2.3 contact-per-issue rate means your real cost per issue is 2.3x your cost-per-contact benchmark" (no primary study traced) | C-AR01, C-AR63 | Concern (*assumed*; vendors) |
| 12 | [MODS] | "SAIA 5700-AJ … 10/01/2025", "AK … 02/23/2026", "AL … 05/04/2026", "AM … 07/06/2026" | C-AR34, C-AR39; AR3b (carrier base tariffs are paid modules, updated often) | Lead |
| 13 | [SWO] | "CzarLite provides neutral LTL base rates for pricing agreements in North America." Vendor SMC³; "Enquire now" (no price) | C-AR21 row "no reseller found", B9 | Counter-evidence (scope) |
| 14 | [MN] PDF pages 17 and 15 | Desktop support "Cost per Ticket $114.96 $45.23 $88.07 $376.89"; 2010 vs 2023 "Cost per Contact $22.56 $20.61" | C-AR01, C-AR63 (high case; peer group) | Lead (§4.1-4.2) |
| 15 | [WEAVE] | Subscription and payment processing "Gross margin 78.5% 78.1% 77.9% 77.8%" | C-AR49; AR4.4 #1 | Corroboration |
| 16 | [REC] (fetch tool) | "Within the $250+ ARPC cohort on the Recurly network, median annual churn sits at 3.54%" against the table's "Over $250/month: Total 3.07%" | C-AR53 | Counter-evidence (internal inconsistency) |
| 17 | [BOX] Table 1 "Result on CUAD dataset" | F1 values without the oracle: 0.66, 0.74, 0.76, 0.75, 0.80, 0.77, 0.80, 0.82 | C-AR60 | Detail |
| 18 | Search summary of an IJCAI 2025 benchmark of vision LLMs on tables (arXiv 2412.20662) | "low-quality input images" were "a major limitation for the tested models"; no 2025 source found reporting whole-table exact match near 100% | C-AR56, C-AR57 (currency) | Lead (*assumed*; summary) |
| 19 | Search summary of a tax-and-accounting publisher's blog on Ardent 2025 | "Best-in-class teams maintain an exception rate of just 9%, compared to 22% for other organizations." | C-AR62 | Counter-evidence (secondary) |

---

## §7 Could not access

- **SEC EDGAR** (by rule). Weave and Xero were read on their own investor-relations and ASX copies.
- **Xero's FY26 annual report glossary** was not fetched. The definition comes from Xero's FY21 investor deck, so the label assumes Xero did not change it.
- **Recurly**: a plain download hit a captcha, so the page was read through the fetch tool (as in the checked file).
- **SMC3 RateWare XL FAQ** (`transition.smc3.com/knowledge-hub/faqs/SMC3_FAQ_RateWare_XL_17831.pdf`): 404.
- **Saia's website**: script-rendered, with no tariff text in the download. C-AR39 was not reproduced.
- **Ardent Partners' own 2025 report**: not reached; only secondary summaries (C-AR62). One guessed vendor-blog URL failed to connect.
- **KeyBanc/Sapphire 2025 tables**: not tried directly; the checked file reports 403. One lead reached us only through a search summary (§6 #9).
- **Benchmarkit 2026 full report**: not read beyond the public page (as in the checked file).
- **Not read:** the figures from checks AA, AJ, A, AL and AC that check AR cites by old ID. This review was barred from other project files.
- **Not searched (budget):** tickets per customer for B2B software (the checked file's three searches found none); neutral self-serve onboarding rates; cyber insurance for a small SaaS. One search of the ten was left unused.
