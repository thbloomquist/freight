# S5 check AR: our cost and software economics (C-09)

- **What this is:** desk research for card C-09 under D-23 (2026-10-08). C-09 is now a software company, not an audit firm. In the founders' words: "We have no analysts, this is a software company. A software as a service, we do no manual reviews here. We offer a tool that can automatically catch things for them and raise the concerns to their human reviewers." The customer's own staff review the flags and file the disputes; the customer uploads its rate agreements, the software reads them and the customer confirms the rules. **Our** cost per customer is now only: machine reading, storage and hosting, support (including help with self-serve onboarding), and any per-customer licence. Company-level costs (SOC 2, development) and the cost of winning a customer are reported separately. This check gathers web evidence for those numbers and for the SaaS benchmarks used to judge payback (`handoff_c09_software_rerun.md` §3, §6). Five questions:
  - **AR1** per-customer running cost: support, hosting, cost-of-revenue shares;
  - **AR2** SOC 2 cost;
  - **AR3** SMC3 CzarLite licence terms for software that serves many customers;
  - **AR4** benchmarks for payback: gross margin, churn, cost of winning a customer (CAC) and CAC payback for small B2B software;
  - **AR5** self-serve onboarding completion, and how often machine-read contracts or rate tables need a human correction.
- **Builds on / not redone:**
  - check AA §2 (cloud OCR $1.50 per 1,000 pages; LLM prices; about $0.10 per bill packet; S3 $0.023/GB-month, a 1 MB packet kept 7 years ≈ $0.002), §6 (SMB customer-success managers handle 100-250 accounts, so 7-18 hours per account a year; SaaS Capital 2026: support plus success median 9% of ARR, hosting 5%, DevOps 4%; SOC 2 recurring $20-50k a year per Scrut.io; NMFTA ClassIT+ $2,967-9,809 a year), §7 (PRGX 35-45% gross margin; AI products 45-53%, ICONIQ 2026; vertical vs horizontal public software ~65% vs 75%);
  - check AJ §3, §7, §9 (reading $12-300 a year for a $1.5-3M customer; table scores about 65-95 on TEDS-type measures; Trax 98% and Pando 100% rate-agreement extraction, *assumed*; hours to load an agreement not found; 1-3 hours per carrier version [our call]);
  - check A §A3 (High Alpha 2025 retention by ACV and CAC payback by ARR; SaaS Capital 2023 retention by ACV; Bessemer 2021 SMB CAC payback under 12 months; Tunguz CAC by motion; Mindbody 2010);
  - check AN (N-AN29: CzarLite listed at $800 from 2022, unit not stated), check AL (N-AL44: SMC3 +3% for 2026; NMFTA licence terms not public), check AC (N-AC34: the CzarLite page).

  Those figures are cited by their old IDs and are not re-argued.
- **Date:** 2026-10-08. Everything new here was accessed on 2026-10-08.
- **Status:** input to S5. **It decides nothing.** It proposes no price for our product and no fee form. An adversarial check of this file follows (`research/s5_check_AR_adversarial.md`).
- **Searches used:** 27 web searches of the 40 allowed. Separately, 14 queries to the public USAspending.gov API (no key, no login), and about 70 page or PDF fetches (most by plain download, some through the fetch tool). Downloaded files are kept outside the project in the session scratchpad.
- **No identity was sent. Nobody was contacted.** No logins, sign-ups, forms, quote requests or API keys. SEC EDGAR was not fetched; company figures come from investor-relations copies (Xero via the ASX, Weave via its IR site).
- **Adversarial review (2026-10-08):**
  - 64 rows: 48 KEEP-verified, 9 KEEP-assumed, 7 NARROW and **0 DISCARD**; every row checked. The reviewer agreed with every §0 verdict, with wording fixes, and every **[our calc]** reproduces exactly.
  - **Where the review and this file differ, the review's restricted readings govern** (`s5_check_AR_adversarial.md` §1). In particular:
    - **CAC payback (C-AR40):** Benchmarkit's medians of 8 and 14 months contradict the same report's New CAC ratio ($2.00 and $1.60 per $1 of new revenue), which implies about **25-31 months**, close to Weave's;
    - **Weave (C-AR50):** payback about 27-38 months; "a lower bound on CAC" is not supported;
    - **Xero (C-AR48):** the 1.14% is monthly **revenue** churn by Xero's own glossary, not a share of customers;
    - **gross margin (C-AR43):** 77-81% are medians across all sizes; the same report gives 70% under $1M of revenue and 74% at $1-5M;
    - **hosting (C-AR64):** $24-60 a customer is a list-price floor. This file's own build with monitoring gives $3.6-6.0k a year ($36-60 a customer at 100), and the median company under $1M of revenue spends $18,360 a year, about $184 a customer at 100. DevOps labour is not counted;
    - **SOC 2 (C-AR20):** the totals count only the platform, the audit and a penetration test, not readiness work or staff time; buyers may ask for Type II in year one;
    - **invoice extraction (C-AR61):** the 7% is a share of consistency checks failed, not of invoices;
    - **FEMA (C-AR21, C-AR22):** one buyer's micro-purchase, renewed: one observation, not three.
  - The §0 one-line reading's "$100-400 a year" understates §AR6's own sum ($97-652); with the review's corrections it is about **$109-784**. Storage's "~$1" is the first year; the steady state is about $6-9 a year.
- **Re-checked at the source by the coordinator (2026-10-08), all matching:**
  - MetricNet's deck, slide text: "Average Cost per Web Ticket/Email Contact $24.24 $5.92 $19.96 $58.54", handle time 13.70 minutes;
  - FEMA's award on USAspending: "TO PURCHASE CZARLITE AND RATEWARE WEB ACCESS SUBSCRIPTIONS FOR THE LOGISTICS SUPPLY CHAIN MANAGEMENT SYSTEM (LSCMS)", 8764.0, 2019-03-22 to 2020-03-21;
  - Lightsail's $24 (4 GB, 2 vCPUs, 80 GB SSD) and $120 (high-availability 4 GB database) plans.
- **Labels:** *verified* = read at the source (a body's own report, a public procurement record, a paper, or a company's own page or price listing for "what this company says"). *assumed* = a vendor or association figure offered as a market measurement, a search snippet, a secondary repost, or text read only through the fetch tool's summary. **[our calc]** = our arithmetic, shown. **[our call]** = our judgement. Vendor figures are kept in their own rows, apart from neutral ones.
- **New sources:** N-AR01 to N-AR41 (Sources section). Re-read with new passages: N-AN29 (SMC3 2022 module prices).

**Words used here:**
- **ACV:** annual contract value, what one customer pays a year. **ARR:** annual recurring revenue, the whole company's.
- **Logo churn:** the share of customers who leave in a period. **GRR (gross revenue retention):** the share of last year's recurring revenue kept from the same customers, before any upsell. **NRR:** the same, after upsells.
- **CAC (cost of winning a customer):** sales and marketing spend divided by new customers won. **CAC payback:** months of a customer's gross profit needed to repay its CAC. **New CAC ratio:** sales and marketing dollars spent per $1 of new customers' ARR.
- **Gross margin:** revenue minus cost of revenue (hosting, support, reading, licences), as a share of revenue. **COGS:** cost of goods sold, the same cost of revenue.
- **SOC 2:** an audit report on a software company's security controls. **Type I** tests the design of controls on one day; **Type II** tests that they worked over a period (usually 3-12 months). **Compliance platform:** software (Vanta, Drata, Secureframe, Sprinto) that collects the evidence an auditor needs; the auditor is paid separately.
- **CzarLite:** SMC3's neutral LTL base-rate table, which many LTL discounts are applied to. **RateWare XL:** SMC3's rating engine that applies base rates and discounts. **Data module:** one base-rate table (CzarLite, or one carrier's own base tariff) loaded into RateWare or BatchMark. **LSP:** logistics service provider (3PL, broker, freight-payment firm).
- **Exact-match table accuracy:** the share of tables a machine reads with every cell right. **F1:** a 0-1 score that balances finding the right items against flagging wrong ones.
- **Activation:** a new user reaching the first useful result. **Time to value:** how long that takes. **Straight-through processing (STP):** a document handled with no human touch.

---

## §0 Summary

| Question | What the web says now | Best evidence | Label | **Proposed verdict** |
|---|---|---|---|---|
| **AR1a** Support cost per customer | **Unit cost of one support contact:** an IT service-desk benchmark puts an email or web ticket at **$24.24 average, $19.96 median** (range $5.92-58.54), 13.7 minutes of handling, $1.54-1.71 per handling minute [C-AR01, C-AR03]. **Support as a share of revenue:** half of TSIA's companies keep support COGS **under 3.8% of revenue**, 13.6% spend 10-18% [C-AR05]; SaaS Capital's small companies spend a median **10% of ARR** on support and success [C-AR06]. **Tickets per customer per month: not found** from any neutral source. **[our calc]** with 3-12 tickets a year: **$60-290 a year** steady state, plus **$185-616 once** for 2-6 hours of onboarding help [C-AR63] | N-AR01, N-AR02, N-AR03 | unit costs and shares *verified*; ticket count **[our call]** | **Narrowed** (unit cost and share of revenue found; the ticket count is ours) |
| **AR1b** Hosting per customer | List prices for a small multi-tenant stack: a 4 GB server $24 a month, a 4 GB managed database with failover $120 a month, 250 GB of object storage $5 a month [C-AR10]. **[our calc]** a lean production stack plus staging and tools costs **$2.4-6.0k a year**, or **$24-60 per customer at 100 customers**, $8-20 at 300 [C-AR64]. Storage of bill packets stays negligible (check AA). Survey cross-check: hosting is a median **5-6% of ARR** at small SaaS firms [C-AR06, C-AR07] | N-AR04, N-AR05, N-AR03 | prices *verified*; stack **[our call]** | **Answered from the web** (list prices) with our stack as the assumption |
| **AR1c** Cost-of-revenue shares for small SaaS | SaaS Capital 2023, median % of ARR: under $1M ARR hosting ~5%, DevOps ~10%, support/success ~10%; at $1-5M hosting 5-6%, DevOps 5%, support/success 10% [C-AR06, C-AR07]. Under $1M ARR the median company spent **$18,360 on hosting and $31,000 on customer success** in a year [C-AR07] | N-AR03 | *verified* (survey) | **Answered** (for "a typical small SaaS"; not specific to document processing) |
| **AR2** SOC 2 cost | **Compliance platforms, 12-month list prices on AWS Marketplace:** Sprinto $7,500 + $2,000 for SOC 2; Secureframe $7,500 + $7,500; Vanta $14,000-23,000 for 1-20 employees; Drata $25,000 + $7,500 [C-AR13-C-AR16]. **Auditor fees are not published** by the firms checked [C-AR18]; a compliance vendor puts Type I at $5-20k and Type II at $7-150k, citing one firm at $20k / $30k [C-AR17]. **[our calc]** first year (Type I) about **$29.5-58k**; recurring (Type II) about **$16.5-53k**, or up to $68k with a yearly penetration test [C-AR20]; check AA's $20-50k (Scrut.io) sits inside this | N-AR06-N-AR10 | platform prices *verified* (list); audit fees *assumed* (vendor) | **Narrowed** (platform list prices settled; audit fees only from vendors and directories) |
| **AR3** SMC3 CzarLite licence for a multi-customer SaaS | **No price or licence unit for our case is published.** New hard facts: **(1)** a federal agency (FEMA) paid SMC3 **$8,764 a year** for "CzarLite and RateWare web access subscriptions" for one internal system, in 2019, 2020 and 2021 [C-AR21, C-AR22]; **(2)** licence fees rose 3% for 2025, 3% for 2026 and **3.9% for 2027** [C-AR24, C-AR25]; **(3)** two TMS vendors make each customer bring its own SMC3 licence: IBM's TMS says "No other shippers can use this tariff unless they have also been authorized by SMC" [C-AR27, C-AR28]; **(4)** SMC3 also sells to LSPs that rate "for multiple shippers" and shows a freight-payment firm "auditing thousands of freight bills for multiple shippers" [C-AR30, C-AR31]. So both routes exist (each customer licenses, or we hold a multi-client licence); **which applies to a SaaS auditor, and at what price, only SMC3 can say.** [our calc] If our cost per customer were FEMA's $8,764, it would be **2.2 times** the old $3,900 fee at a $2M customer [C-AR65] | N-AR23, N-AR15, N-AR20, N-AR22, N-AR13, N-AR18 | *verified* (procurement record, SMC3 pages, vendor docs) | **Narrowed** (a single-organisation price exists; the multi-customer unit and price are **Not answerable from the web**) |
| **AR3b** Carriers' own base tariffs instead | Carrier base tariffs (e.g., ABF 504-AX, dated 2026-06-22) are sold **as SMC3 data modules** "designed for use in the SMC³ RateWare and SMC³ BatchMark products" ($300 a module in 2022) [C-AR34, C-AR26]. Rules tariffs are public (check AJ); **no free download of a carrier's base-rate tables was confirmed** [C-AR39] | N-AR19, N-AN29 | *verified* (SMC3 list); carrier downloads *assumed* (snippet) | **Narrowed** |
| **AR4a** Gross margin | Small SaaS, median: **85%** under $1M ARR, **80%** at $1-5M (OpenView 2023) [C-AR46]; **81%** subscription and **77%** total revenue (Benchmarkit 2025) [C-AR43]; software margin **80%**, stable four years (Benchmarkit 2026) [C-AR44]. Public SMB firms: Xero **83.9%**, Weave **72.1%** [C-AR48, C-AR49]. Check AA's AI products at 45-53% remain the AI-heavy case | N-AR29, N-AR26, N-AR27, N-AR31, N-AR32 | *verified* (reports, filings); OpenView copy *assumed* (third-party host) | **Answered** (for software in general) |
| **AR4b** Churn at ACV of about $1-10k | **GRR by ACV, Benchmarkit 2025 (2024 data):** **85%** at $1-5k and **85%** at $5-10k ACV (quartiles 75-91% and 78-89%) [C-AR42]; its 2026 edition (2025 data, via a partner's page): **80%** under $5k ACV, PLG 79%, sales-led 88% [C-AR45]. SaaS Capital 2025: **90%** GRR under $12k ACV (firms over $1M ARR) [C-AR47]. Public SMB firms: Xero **1.14% a month** of customers (≈12.9% a year) [C-AR48]; Weave GRR **89%** [C-AR49]. ChartMogul: median monthly logo churn **6.1%** for customers paying under $25 a month and **2.2%** above $500 a month (≈23% a year) [C-AR51] | N-AR26, N-AR28, N-AR30, N-AR31, N-AR32, N-AR33 | surveys and filings *verified*; partner page *assumed* | **Answered** as a range: **roughly 10-25% of revenue lost a year** at our likely ACV [our call] |
| **AR4c** CAC and CAC payback | **CAC payback by ACV, Benchmarkit 2025 (2024 data, N=148):** median **8 months at $1-5k** (quartiles 6-12) and **14 months at $5-10k** (13-18) [C-AR40]. **New CAC ratio:** median **$2.00** of sales and marketing per $1 of new ARR at $1-5k ACV (quartiles $0.46-2.46), **$1.60** at $5-10k [C-AR41]. OpenView 2023: 8 months under $1M ARR, 11 at $1-5M [C-AR46]. **A real SMB vertical firm:** Weave spends about **$12k of sales and marketing per gross new location** that pays about $6k a year, a payback of roughly **31-33 months** **[our calc]**, a lower bound on CAC [C-AR50]. No source splits out founder-led sales | N-AR26, N-AR29, N-AR32 | surveys *verified*; Weave **[our calc]** | **Narrowed** (survey medians are self-reported; the one real firm checked is ~3× slower) |
| **AR5a** Self-serve onboarding completion | **Only vendor data.** Userpilot's own customers: activation **37.5%** (62 companies), onboarding-checklist completion **19.2%** (188 companies), time to value 1 day 12 hours [C-AR55]. Nothing measures "upload your contracts and confirm the rules" | N-AR35 | vendor with stated sample (*verified* that it says so; not neutral) | **Not answerable from the web** for our task (only a vendor proxy) |
| **AR5b** How often machine-read rate tables need correcting | **Neutral table benchmarks:** a strong 2021 table reader got **every cell right in 94.7% of simple tables but only 69.4% of complex ones** [C-AR56]; whole-table exact match on another benchmark was **65-81%** [C-AR57]. Invoices: an LLM extractor got **94%** of fields right (91% of line items) and **7%** of invoices failed an add-up check, on 102 invoices [C-AR61]. Contracts: the best LLMs score **F1 0.50-0.64** finding clauses in commercial contracts (2025) [C-AR59]. **No study of freight rate agreements or rate confirmations** was found (N-AR41). Reading [our call]: **expect one or more wrong cells in roughly 1 complex table in 3 to 1 in 5**, so the customer's confirmation step is not optional | N-AR36, N-AR37, N-AR40, N-AR39 | *verified* (papers) | **Narrowed** (neighbouring document types only) |

**One-line reading [our call]:** under D-23 our own running cost per customer is small next to the old review labour: about **$100-400 a year** for reading, hosting and steady-state support, plus a few hundred dollars of first-year onboarding help (§AR6). Two numbers can still swamp it: **an SMC3 licence if it turns out to be per customer** (FEMA paid $8,764 a year for one organisation), and **the cost of winning a customer**, where survey medians (8-14 months payback at $1-10k ACV) and one real SMB firm (about 31-33 months) disagree.

---

## §AR1 · Per-customer running cost

### AR1.1 Support: unit cost of a contact

| # | Source | Population | Number | What it is, and is not | Label | Claim |
|---|---|---|---|---|---|---|
| 1 | MetricNet, *Benchmarking Roundup: 2023 IT Service and Support Benchmarks*, slide 11 | One peer group of IT service desks (size and region not stated) | **Email/web ticket: $24.24 average, $19.96 median** (min $5.92, max $58.54); voice $18.35; chat $23.26; all contacts incl. self-help $17.07 | Internal IT help desks, not a software vendor's customer support. Fully loaded cost per contact (labour, tools, facilities, overhead) | *verified* (MetricNet's own deck) | C-AR01, C-AR02 |
| 2 | Same | Same | Email/web handle time **13.70 min** average (median 13.77); cost per handling minute **$1.71** average (**$1.54** median) | $1.54-1.71 a minute is **$92-103 an hour** fully loaded **[our calc]** | *verified*; hourly **[our calc]** | C-AR03 |
| 3 | Same, slide 17 (desktop support) | Internal desktop support | **0.38 tickets per user per month** | An employee's tickets to their own IT department. Not a B2B customer's tickets to a vendor; shown only as an order of magnitude | *verified*; **not comparable** | C-AR04 |

**Tickets per customer per month for B2B software: not found.** Two web pages give 0.3-0.8 per customer and 15-25 per enterprise customer with no source; a vendor repost attributes 4-8 contacts a customer a year to Zendesk, unverified (search summaries, N-AR41). None is used.

### AR1.2 Support as a share of revenue

| # | Source | Population | Number | Label | Claim |
|---|---|---|---|---|---|
| 4 | TSIA, "Top Support Services Questions Answered" (updated 2025-08-14) | TSIA's benchmark members (mostly larger technology firms) | **49%** of companies have support COGS of **0-3.8% of revenue**; **22%** at 3.8-6%; **13.6%** at 10-18%. TSIA warns that keeping support below 4% "may not be sustainable in XaaS models" | *verified* (TSIA's page) | C-AR05 |
| 5 | SaaS Capital, *Spending Benchmarks for Private B2B SaaS Companies* (2023 survey), "Spend by Company Size" | Private B2B SaaS firms responding to its survey | Median **customer support/success 10% of ARR** in every band under $20M; hosting 5% (under $1M), 6% ($1-3M), 5% ($3-5M); DevOps 10% under $1M, 5% above | *verified* (survey; chart values read from the image) | C-AR06 |
| 6 | Same, dollar chart "Less than $1 Million in ARR" | Same | Median dollars a year: hosting **$18,360**; DevOps $28,950; professional-services COGS $14,500; other COGS $9,900; **customer success $31,000**; sales $46,250; marketing $18,540; R&D $51,475; G&A $31,797 | *verified* (chart) | C-AR07 |
| 7 | Same, $1-3M ARR | Same | Hosting $115,250; customer success $159,380; sales $220,000; marketing $145,000 | *verified* (chart) | C-AR08 |
| 8 | Same, "Funding Source" | Same | Bootstrapped firms spend a median **91% of ARR** in total, equity-backed 120%; equity-backed spend **25% more on customer success** | *verified* | C-AR09 |

Check AA already holds SaaS Capital 2026 (support plus success 9% of ARR) and Gainsight (100-250 accounts per SMB success manager).

### AR1.3 Hosting a small multi-tenant app (list prices)

| Item | Price | Source | Label | Claim |
|---|---|---|---|---|
| AWS Lightsail Linux server, 4 GB / 2 vCPU / 80 GB SSD | **$24 a month** (2 GB: $12; 8 GB: $44) | N-AR04 | *verified* | C-AR10 |
| AWS Lightsail managed database, 4 GB / 2 cores / 120 GB | **$60 standard, $120 high-availability** a month (1 GB: $15 / $30) | N-AR04 | *verified* | C-AR10 |
| AWS Lightsail object storage, 250 GB with 500 GB transfer | **$5 a month** | N-AR04 | *verified* | C-AR10 |
| DigitalOcean managed PostgreSQL, 1 GiB / 1 vCPU | **$15.15 a month**; extra storage $0.215 per GiB-month | N-AR05 | *verified* | C-AR11 |

**[our calc] A lean production stack:** two 4 GB app servers ($48) + a 4 GB high-availability database ($120) + object storage ($5) + a staging server and database ($12 + $15) = **$200 a month, $2,400 a year** at list. Add monitoring, logging, email, backups and error tracking at **$100-300 a month [our call]**: **$3.6-6.0k a year**. Range used: **$2.4-6.0k a year**, which is:

| Customers | 50 | 100 | 300 |
|---|---|---|---|
| Hosting per customer a year | $48-120 | **$24-60** | $8-20 |

Variable storage stays negligible: a $2M customer sends about 3,000-4,420 bill packets a year (1.5-2.21 per $1,000, check AA and the practice audit), at about $0.002 each kept seven years (check AA) **[our calc]**. Cross-check: SaaS Capital's median hosting of 5-6% of ARR would be $195-234 a year on a $3,900 customer; small firms run below scale, so the share-of-revenue figure is the higher bound **[our call]**.

### AR1.4 Document-processing SaaS specifically

Nothing new was found on the cost structure of small document-processing SaaS (not searched beyond AA and AJ; budget). Check AJ's reading cost ($12-300 a year at $1.5-3M of spend) and its platform minimums (Rossum $18k, Sensible $5,388, Unstract $5,988 a year) stand.

### AR1.5 Support cost per customer [our calc]

| Piece | Low | High | Inputs |
|---|---|---|---|
| Steady-state tickets a year | 3 | 12 | **[our call]**: 0.25-1 a month; no source found |
| Cost per ticket | $19.96 | $24.24 | MetricNet median / average email ticket (C-AR01) |
| **Steady-state support a year** | **$60** | **$291** | 3 × $19.96; 12 × $24.24 |
| Hours of onboarding help, first year only | 2 | 6 | **[our call]**: a call to set up, help reading the first agreements, one follow-up |
| Loaded cost per hour | $92 | $103 | MetricNet $1.54-1.71 a minute (C-AR03) |
| **One-off onboarding help** | **$185** | **$616** | 2 × $92.40; 6 × $102.60 |
| **First-year support** | **$245** | **$907** | sum |
| Top-down cross-check, on a $3,900 customer | $148 | $390 | 3.8% (TSIA) to 10% (SaaS Capital) of revenue |
| High-touch case (a success manager, not D-23's model) | $647 | $1,847 | 7-18 hours (check AA, Gainsight) × $92-103 |

**Reading [our call]:**
- The bottom-up and top-down figures meet at roughly **$60-390 a year** in steady state. The first year carries the onboarding hours, and they cost more than the steady-state tickets.
- MetricNet's costs are for internal IT desks, which handle simpler tickets. A question like "why did the software flag this reweigh?" may take longer than 13.7 minutes, so the high end is the safer planning value.
- **Tickets per customer is the missing input.** It is measurable from the first design partners.

---

## §AR2 · SOC 2 cost

### AR2.1 Compliance platforms (list prices, 12-month contracts on AWS Marketplace)

| Vendor | Line items, as listed | First-year platform + SOC 2 [our calc] | Label | Claim |
|---|---|---|---|---|
| **Sprinto** | Starter Platform, up to 100 employees, **$7,500**; First Compliance Framework "starting at $2000" | **$9,500** | *verified* (list) | C-AR16 |
| **Secureframe** | Platform, up to 100 employees, **$7,500**; First Framework **$7,500** | **$15,000** | *verified* (list) | C-AR15 |
| **Vanta** | Essentials **$14,000**, Plus $21,500, Professional **$23,000** ("Starting cost for 1-20 employees"); Trust Center $6,000; AWS FTR module $7,500 | **$14,000-23,000** | *verified* (list) | C-AR13 |
| **Drata** | Platform Fee "with capacity for a 100 FTE org" **$25,000**; SOC 2 Framework **$7,500** | **$32,500** | *verified* (list) | C-AR14 |
| Vendr (a procurement broker), Vanta | "Median buyer pays $20,000 per year, based on data from 365 purchases. Lowest was $7,500 and highest was $56,943." | — | *assumed* (search snippet; Vendr sells negotiation services) | C-AR19 |

Marketplace list prices are starting prices; private offers and discounts are common (a procurement broker reports median discounts of 42% on one platform, *assumed*, snippet). None of these includes the auditor.

### AR2.2 Audit fees

| Source | Figure | Label | Claim |
|---|---|---|---|
| Two licensed CPA firms' AWS Marketplace listings (Type I and II, "fixed-fee") | **No price published**: "Pricing is based on your specific requirements, including the Trust Services Criteria in scope, system complexity, and the reporting period" | *verified* (absence) | C-AR18 |
| Secureframe, "How Much Does a SOC 2 Audit Cost" (a compliance vendor) | Audit alone: **Type I about $5-20k; Type II $7k-150k**; average quote $5,000-60,000; "one firm certified by the AICPA ... charges $20,000 for a SOC 2 Type I audit and $30,000 for a SOC 2 Type II"; readiness assessment ~$15k; penetration test ~$15k; annual maintenance $10-60k | *assumed* (vendor) | C-AR17 |
| A SOC 2 directory (snippet) | Startup-specialist firms' Type II estimates $7-30k; the directory says "our estimates, not live quotes" and takes paid placements | *assumed* (snippet) | (search summary, N-AR41) |
| Check AA, Scrut.io (vendor) | Type II audit $30-80k; recurring $20-50k without automation; platform $10-30k | *assumed* (as AA) | — |

### AR2.3 SOC 2 a year [our calc]

| Year | Platform | Audit | Penetration test | **Total** |
|---|---|---|---|---|
| Year 1 (Type I) | $9,500-23,000 | $5,000-20,000 | ~$15,000 | **$29,500-58,000** |
| Each later year (Type II) | $9,500-23,000 | $7,000-30,000 (the startup-specialist part of the vendor ranges) **[our call]** | $0-15,000 | **$16,500-53,000** (to $68,000 with a yearly test) |

Per customer, recurring: **$330-1,360** at 50 customers, **$165-680** at 100, **$55-227** at 300. Drata's $32,500 platform would sit at the top of the range. Whether mid-sized shippers demand SOC 2 at all is check AQ's question.

**Reading [our call]:** the platform list prices are now firm at about $9.5-23k a year for a small company. The audit fee is the soft number; no firm publishes one.

---

## §AR3 · SMC3 CzarLite licence terms for software serving many customers

### AR3.1 What a licence has cost a real buyer

| Evidence | Figure | What it can and cannot say | Label | Claim |
|---|---|---|---|---|
| USAspending.gov, award 70FA3019P00000010, FEMA (DHS), Information Technology Commodities office | **$8,764** for "CZARLITE AND RATEWARE WEB ACCESS SUBSCRIPTIONS FOR THE LOGISTICS SUPPLY CHAIN MANAGEMENT SYSTEM (LSCMS)", 2019-03-22 to 2020-03-21; not competed, micro-purchase | **One organisation, one internal system, web access.** Users, modules and API use not stated. A government buyer may get list price or a discount | *verified* (federal procurement record) | C-AR21 |
| Same, award 70FA3020P00000006 | **$8,764** base (signed 2020-03-20) + **$8,764** option period 1 (2021-01-29); potential end 2025-03-21 | The same price two years running; later options not shown as exercised | *verified* | C-AR22 |
| Same, award HTC71108M0011, DoD (TRANSCOM) | "NMFC DATA LICENSE RENEWAL" $5,803, de-obligated to $5,500 (2008) | Class data, not CzarLite; old | *verified* | C-AR23 |
| SMC3 press release, 2021-12-06 (re-read of N-AN29) | Data module rates from 2022: **CzarLite $800**; CanadaLite and MexicoLite $800; **Carrier Tariff Stock $300**; "The prices vary by module and service level"; modules are "delivered through RateWare XL, BatchMark XL, and CzarLite" products | **A module fee on top of the software it runs in**, not a whole licence; this explains why FEMA's web-access subscription costs ~11× the $800 module **[our call]** | *verified* | C-AR26 |
| SMC3 press releases 2024-10-01, 2025-09-23 (check AL), 2026-09-03 | Licence fees for CzarLite, RateWare XL, CarrierConnect XL and BatchMark XL: **+3% for 2025, +3% for 2026, +3.9% for 2027**; "RateWare XL data modules pricing will remain the same" (2025) | Escalators, not prices. 2023-2024 changes not read (a news snippet says +4.9% for 2024, *assumed*) | *verified* | C-AR24, C-AR25 |
| SMC3 press release, 2026-08-28 | CzarLite rates updated on 2026-09-28, an average **+5.8%** in the rates themselves | Changes the base the discounts apply to, not the licence fee | *verified* (N-AR15) | — |

**[our calc]** FEMA's 2021 price with only the published 2025-2027 escalators applied is about $9,660 a year (2022-2024 changes unknown). Compared with the old contingency fee at a $2M customer ($3,900, check AJ), $8,764 is **2.2×**. Spread over customers, it is $88 each at 100 and $29 at 300.

### AR3.2 Who must hold the licence

| Evidence | What it says | Label | Claim |
|---|---|---|---|
| **IBM Sterling TMS** support page "Setting Up Tariffs" (modified 2018-12-08) | "you must have a license from SMC to use these tariffs in Sterling TMS"; the user negotiates the licence with SMC, SMC sends the TMS "a letter that authorizes you"; "**No other shippers can use this tariff unless they have also been authorized by SMC.**" | *verified* (vendor doc) | C-AR27 |
| **Supply Chain Cloud** (a TMS for Microsoft Dynamics users), help page "RateWare XL (CzarLite) Credentials" | The customer enters SMC3 credentials: "These values are provided by SMC3. If you need any of these credentials, reach out to your SMC3 contact regarding your RateWare XL license." | *verified* (vendor doc) | C-AR28 |
| **Oracle Transportation Management** admin guide (25C) | RateWare XL rating needs a Username, Password and **License** property set by the customer | *verified* (vendor doc) | C-AR29 |
| **SMC3 for LSPs** (RateWare XL and CzarLite pages) | RateWare XL lets LSPs "Manage and optimize LTL rating complexity and logic **for multiple shippers**"; CzarLite lets LSPs "Negotiate across carriers and **on behalf of multiple customers**"; LSPs hold a "CzarLite license agreement" | *verified* (SMC3's pages) | C-AR30 |
| **SMC3 "Smarter LTL Freight Audits" datasheet** (PI# 29236-L, 04/2026) | Sells RateWare Plus, BatchMark XL, CarrierConnect XL, APIs and EDI as an audit toolkit; a freight-payment firm's testimonial: "When you're auditing thousands of freight bills **for multiple shippers and LSPs** ..." | *verified* (SMC3's page; testimonial is the customer's claim) | C-AR31 |
| SMC3 brochure (2016) | "CzarLite has been licensed to more than 1,500 shippers, as well as over 300 logistics intermediaries" | *verified*; old | C-AR32 |
| SMC3 technology-provider page | Alliance partners (named TMS and ERP vendors) integrate SMC3 "for a complete TMS LTL solution"; "a single integration point delivers access to all rates" | *verified* | C-AR33 |
| SMC3 webRater datasheet | "Access codes are required for CzarLite, CanadaLite and MexicoLite pricing data" | *verified* | C-AR36 |
| SMC3 website terms | The **website** licence excludes "any resale or commercial use of this site or its contents ... any derivative use ... any use of data mining, robots"; this governs the site, not the products | *verified* | C-AR35 |
| 3Gtms partnership (trade press, 2018-04-17) | 3Gtms expanded its partnership "to offer the SMC³ RateWare® XL, CarrierConnect® XL and CzarLite® solutions to its customers"; licence holder not stated | *assumed* (fetch summary) | C-AR38 |
| USAspending keyword searches | No other federal buyer, and no reseller, of CzarLite or RateWare found | *verified* (search result, not proof of absence) | C-AR21 |

### AR3.3 Carriers' own base tariffs as an alternative

- Carrier base tariffs are distributed **as SMC3 data modules**: the list includes "ABF 504-AX, US/US 06/22/2026" and states "data modules are designed for use in the SMC³ RateWare and SMC³ BatchMark products"; "Pricing may vary for custom shipper tariffs" [C-AR34]. In 2022 a "Carrier Tariff Stock" module was $300 [C-AR26].
- A 2023 trade-press snippet says "Updated Saia 5700 rates and the Saia 170D rules tariff are available at saia.com" (*assumed*, snippet; the page returned 403) [C-AR39]. Whether the base tables themselves download freely, or only after a customer login, was not confirmed.
- Check AL holds the other route: ODFL's and R+L's rate APIs return the customer's own contract price with the customer's credentials, but ODFL's will not price a past date.

### AR3.4 Reading [our call]

1. **Neither "per customer" nor "a gate" is settled. Both routes exist.** TMS vendors make each shipper hold its own SMC3 licence (IBM, Supply Chain Cloud, Oracle); SMC3 also licenses LSPs and freight-payment firms that rate and audit for many shippers.
2. **If each customer must hold its own licence, it is a buying hurdle, not our cost.** FEMA's $8,764 a year for one organisation is the only public price, and it is larger than the whole old fee at a $2M customer.
3. **If we hold a multi-client licence, the price is unknown.** At FEMA's scale it would be $29-88 a customer a year; an LSP or audit licence is likely priced higher, and possibly by volume, but no figure was found.
4. **The design can avoid the question at first.** Check AL's reading stands: audit against the customer's own agreement, the quote numbers on the bills and the carriers' own rate APIs, and use SMC3 base rates only after SMC3 confirms the licence. The real question for SMC3 is short: "What licence does a SaaS company need to re-rate its customers' LTL bills against CzarLite and carrier base tariffs, and is it priced per customer, per bill or flat?"

---

## §AR4 · Benchmarks for judging payback

### AR4.1 Gross margin

| Source | Population | Figure | Label | Claim |
|---|---|---|---|---|
| OpenView 2023 SaaS Benchmarks (with Paddle), metrics table | Survey respondents by ARR band | Median **85%** (quartiles 70-95%) under $1M ARR; **80%** (72-88%) at $1-5M; 75% at $5-20M | *assumed* (the full report, read from a copy on a third-party host; OpenView's own site now returns 404) | C-AR46 |
| Benchmarkit 2025 B2B SaaS Performance Metrics Benchmarks (2024 data) | 583 participants (N varies by metric) | Total-revenue gross margin **77%** median; subscription **81%**; professional services **30%** | *verified* (the report; partner-hosted copy) | C-AR43 |
| Benchmarkit 2026 (2025 data), report page | Not stated on the page | "**80% median software margin** \| Stable through 4 years" | *verified* (page) | C-AR44 |
| Xero, FY26 results release (year to 2026-03-31) | SMB accounting software | **83.9%** (89.0% in FY25; the fall follows a payments acquisition) | *verified* (company release via the ASX) | C-AR48 |
| Weave, Q4 and FY2025 results release | SMB vertical software (dental, medical), about $6k a location a year | GAAP **72.1%**; non-GAAP 72.7% | *verified* (company release) | C-AR49 |

### AR4.2 Churn and retention at small ACV

| Source | Population | Figure | Label | Claim |
|---|---|---|---|---|
| **Benchmarkit 2025** (2024 data, N=225), GRR by ACV | Survey | Median GRR **90%** under $1k ACV (85-99%); **85%** at $1-5k (75-91%); **85%** at $5-10k (78-89%); 87% at $10-25k (82-95%); overall 88% | *verified* (chart values read from the image) | C-AR42 |
| **Aleph × Benchmarkit 2026** (2025 data, 342 companies), via Aleph's page | Survey | Median GRR **84%** overall (88% a year earlier); "**Sub-$5K ACV sits at 80%**"; sales-led 88%, hybrid 80%, product-led 79% | *assumed* (a partner's write-up; Aleph sells finance software) | C-AR45 |
| **SaaS Capital 2025** retention brief | 1,000+ private B2B SaaS firms; **excludes firms under $1M ARR** | ACV under $12k: NRR **98%**, GRR **90%**; bootstrapped firms GRR 92%, NRR 104%; month-to-month contracts GRR 89% | *verified* | C-AR47 |
| **Xero** FY26 | 4.92M SMB customers, ARPC NZ$55.44 a month | "Average monthly churn (1.14%)"; ≈ **12.9% a year** [our calc: 1 − 0.9886¹²] | *verified* | C-AR48 |
| **Weave** FY2025 | 39,625 SMB locations | Dollar-based GRR **89%**, NRR 93% | *verified* | C-AR49 |
| **ChartMogul** (data Nov 2021-Jan 2022) | ChartMogul's subscription customers | Median monthly customer churn **6.1%** under $25 ARPA, **2.2%** above $500 ARPA; ≈ 53% and **23%** a year [our calc] | *verified* that ChartMogul reports it (its own customer data) | C-AR51 |
| ChartMogul (December 2025 analysis, 3,500 software companies) | Same | Median monthly customer churn **1.7%** where NRR ≥100%, 7.3% where NRR <60%; 3.1-3.5% at growth of 0-100% a year | *verified* (as above) | C-AR52 |
| Recurly (July 2026 data) | Recurly's billing customers | By monthly price per customer, $100-250: **2.87%**; labelled "median annual" but SaaS at 3.04-3.22% "annual" cannot be annual against every survey above; the page is internally inconsistent | *assumed* (fetch summary; unit unclear) | C-AR53 |

### AR4.3 CAC and CAC payback

| Source | Population | Figure | Label | Claim |
|---|---|---|---|---|
| **Benchmarkit 2025** (2024 data, N=148), CAC payback by ACV | Survey; gross-margin-adjusted | Median **8 months** under $1k (5-10); **8** at $1-5k (6-12); **14** at $5-10k (13-18); 18 at $10-25k (15-22); 22 at $25-50k | *verified* (chart values read from the image) | C-AR40 |
| **Benchmarkit 2025** (N=73), New CAC ratio by ACV | Same | Median **$2.00** per $1 of new ARR at $1-5k (quartiles $0.46-2.46); **$1.60** at $5-10k ($1.50-1.80); $1.81 at $10-25k; overall $2.00, up 14% in 2024 | *verified* (chart values read from the image) | C-AR41 |
| **OpenView 2023** | Survey by ARR | CAC payback **8 months** (5-11) under $1M ARR, **11** (5-16) at $1-5M; sales and marketing **27%** and **35%** of ARR | *assumed* (third-party copy) | C-AR46 |
| **SaaS Capital 2023** | Under $1M ARR | Median sales $46,250 + marketing $18,540 a year (C-AR07) | *verified* | C-AR07 |
| **Weave FY2025 [our calc]** | A public SMB vertical firm | Sales and marketing $102.7M; net new locations 4,628; churned ≈ 11% × 34,997 = 3,850; gross new ≈ 8,478; **≈ $12,100 of S&M per gross new location**; revenue ≈ $6,000-6,400 a location; gross profit ≈ $4,350-4,620; **payback ≈ 31-33 months** | **[our calc]** from *verified* inputs. Rough: S&M also funds upsell; the location count includes an acquisition (May 2025), so true CAC is **higher** | C-AR50 |

**Not found:** any benchmark for founder-led sales specifically, and KeyBanc/Sapphire's 2025 tables (the library page returned 403). High Alpha (check A) already warns that early-stage firms "are not always fully accounting for all expenses to acquire customers".

### AR4.4 Reading [our call]

1. **Gross margin:** pure software at small scale runs a median of about **77-85%**; SMB firms with payments or hardware run 72-84%. Check AA's AI-product figure (45-53%) is the case if machine reading becomes a large cost. Under D-23 it should not (AR1).
2. **Churn at $1-10k ACV:** survey medians put GRR at **80-90%**, so **10-20% of revenue is lost a year**, more for product-led motions. Two public SMB firms sit at 87-89% a year.
3. **CAC payback:** survey medians say **8 months at $1-5k ACV and 14 months at $5-10k**. Weave, a real SMB vertical company with inside sales, needs about **31-33 months**. The surveys are self-reported and small at these bands; Weave's figure is rough and includes brand and upsell spend. Check A's Bessemer target (SMB under 12 months) sits between them. **Both ends should be carried into the re-run as a range, not one number.**
4. A New CAC ratio of $1.60-2.00 means about **$1.60-2.00 of sales and marketing per $1 of first-year revenue**: at a 12-month payback bar and an 80% margin this is already over a year **[our calc]**: 1.6 ÷ 0.8 = 2.0 years at $5-10k ACV. The ratio and the payback medians in the same report do not agree, which is another reason to treat the medians loosely.

---

## §AR5 · Self-serve onboarding and correcting machine-read contracts

### AR5.1 Self-serve onboarding completion

| Source | Figure | What it measures | Label | Claim |
|---|---|---|---|---|
| Userpilot, *SaaS Product Metrics Benchmark Report 2025* page (547 companies in all, first-party data from its own dashboards) | Activation **37.5%** average (62 B2B companies; median 37.04%); onboarding-checklist completion **19.2%** (188 companies); time to value **1 day 12 hours** (62 companies); one-month retention 46.9% | New **users** reaching a first value event in products that use Userpilot; not a customer loading its contracts | *verified* that Userpilot reports it (stated samples; its own customer base) | C-AR55 |
| Data-import vendor (Dromo) and onboarding blogs (search summaries) | "Unassisted import completion" proposed as the metric; "more than half" of self-service CSV uploads said to fail; self-serve completion 25-45% (mixed sources) | Unsourced vendor claims | *assumed* | (N-AR41) |

**Not found:** any neutral figure for the share of B2B customers who finish a data-loading onboarding (contracts, price lists) without help. The closest proxy is Userpilot's 19.2% checklist completion, which is a different task.

### AR5.2 How often machine-read tables, contracts and invoices need correcting

| Source | Task | Figure | Label | Claim |
|---|---|---|---|---|
| **PubTables-1M** (Microsoft research, 2021), Table 4 | Reading table structure and text from scientific papers | Share of tables with **every cell exactly right**: **94.7% simple, 69.4% complex, 81.4% all** (DETR model); cell-level scores (GriTS) ≈ 0.98 | *verified* (paper). Interest: the authors built the model | C-AR56 |
| **"Aligning benchmark datasets for table structure recognition"** (same team, 2023) | Same, on ICDAR-2013 tables | Exact-match accuracy **65%** (trained on PubTables-1M), **42%** (FinTabNet, financial reports), **69%** combined; **75% / 65% / 81%** after cleaning the training labels | *verified* (paper) | C-AR57 |
| **Invoice information extraction** (an industry team's preprint, 2025) | 102 born-digital and scanned invoices | LLM extractor: **94%** of fields right, **91%** of line-item fields; **93%** passed add-up checks (so 7% failed); a layout parser: 63% / 58% / 80% | *verified* (paper; small sample) | C-AR61 |
| **ContractEval** (NLLP 2025) | Finding the clause for 41 risk categories in CUAD commercial contracts | F1: GPT-4.1 **0.641**, GPT-4.1 mini 0.644, Claude Sonnet 4 **0.523**, Gemini 2.5 Pro 0.497; open models mostly lower | *verified* (paper) | C-AR59 |
| **CUAD** (2021) | Same dataset, pre-LLM models | Best: **44.0% precision at 80% recall**; "a lawyer would need to read through about 2 irrelevant clauses for every 1 relevant clause" at ~30% precision | *verified* (paper); superseded by ContractEval | C-AR58 |
| **Box** (a document-software vendor's paper, 2025) | Metadata extraction from CUAD contracts | F1 **0.75-0.82** with LLMs and chunk selection | *assumed* as a market figure (vendor research; read at source) | C-AR60 |
| Ardent Partners 2025 via secondary pages | Accounts-payable invoices | Straight-through processing **49.2%** best-in-class, 23.4% others; exception rate 14% average, 9% best-in-class | *assumed* (secondary); this is check AQ's territory | C-AR62 |
| Rate confirmations and rate cards | Freight documents | **No neutral study found.** A manuscript on rate confirmations reports no per-field percentages in its public listing; vendors claim 90-99.8% | *assumed* (vendor claims) | (N-AR41) |

### AR5.3 Reading [our call]

1. **Cell-level scores hide table-level errors.** A reader that gets 98% of cells right still gets **about 1 complex table in 3** wrong somewhere (PubTables-1M), and one-fifth to one-third of tables in other benchmarks. A carrier agreement holds several dense tables (discounts by lane, minimums, accessorials, fuel), so **most agreements will hold at least one wrong cell** until a person checks it.
2. **Add-up checks catch some, not all.** On invoices, about 7% failed a sum check even with the better extractor; rate tables have fewer internal sums to test, so back-testing against the customer's own paid bills (check AJ) is the stronger check.
3. **For A09-17 (self-serve onboarding)** the web gives no completion rate for our task. The two numbers to measure with design partners are: the share of agreements whose loaded rules the customer confirms without our help, and the minutes that takes.

---

## §AR6 · Our cost per customer, put together [our calc]

For a reference customer with about $2M of truckload and LTL spend (3,000-4,420 bills a year). Revenue is left blank: the fee form and price are Q6 decisions.

| Line | Low | High | Source |
|---|---|---|---|
| Machine reading | $12 | $300 | check AJ §9 (cloud OCR to a Sonnet-class LLM pass) |
| Storage of packets | ~$1 | ~$1 | check AA (≈$0.002 a packet kept 7 years) |
| Hosting share (at 100 customers) | $24 | $60 | §AR1.3 |
| Support, steady state | $60 | $291 | §AR1.5 |
| **Running cost a year, excluding licences** | **≈$97** | **≈$652** | sum |
| Onboarding help, first year only | $185 | $616 | §AR1.5 |
| SMC3 licence | $0 (not used, or held by the customer) | $88 (FEMA-scale, company-level, 100 customers) — or **$8,764 if per customer and paid by us** | §AR3 |
| NMFTA class data, only if needed | $0 | $30-98 (check AA's $2,967-9,809 spread over 100) | check AA |
| **Company level, reported separately:** SOC 2 | $16,500 a year | $68,000 a year | §AR2.3 |
| **Company level:** CAC | survey medians imply 8-14 months of gross profit at $1-10k ACV | a real SMB firm: ~31-33 months | §AR4.3 |

**Reading [our call]:** under D-23, our variable cost per customer is a few hundred dollars a year. Whether C-09 pays now turns on what the customer recovers and pays, on the cost of winning the customer, and on SMC3's answer. It does not turn on reading or hosting.

---

## What the web could not settle

1. **Support tickets per customer per month** for small B2B software, from a neutral source. Only unsourced blog figures exist.
2. **SMC3's licence unit and price for a SaaS that re-rates many customers' bills**: per customer, per bill or flat; and whether such a company counts as a technology provider (each customer licenses), an LSP or an auditor. FEMA's $8,764 is the only public price, for one organisation.
3. **Whether carriers' base-rate tables can be downloaded free** (as opposed to rules tariffs, which can). They are sold as SMC3 data modules; a carrier-by-carrier check was not done.
4. **SOC 2 audit fees from a neutral source.** Every figure comes from compliance vendors or referral directories.
5. **CAC for founder-led or very early sales.** Surveys cut by ACV or ARR, not by who sells.
6. **KeyBanc/Sapphire 2025 survey tables** (access blocked).
7. **A self-serve onboarding completion rate for a data-loading task** like uploading and confirming contracts.
8. **The accuracy of machine-reading freight rate agreements or rate confirmations.** Only neighbouring document types (papers' tables, financial tables, invoices, contract clauses) have neutral evaluations.
9. **The cost structure of a small document-processing SaaS** from a public filing (not searched; budget).

---

## Contact leads (no names)

| Role and organisation | Why | URL | Questions |
|---|---|---|---|
| Sales or alliance-partner team, SMC3 | The licence a SaaS company needs to re-rate its customers' LTL bills; per customer, per bill or flat; whether customers can bring their own licence | https://www.smc3.com/partners.htm ; https://www.smc3.com/technology-providers.htm | AR3, A09-08 |
| Rating team at a freight-payment firm quoted by SMC3 | How a multi-client audit licence from SMC3 is structured and priced | https://www.smc3.com/knowledge-hub/data-sheets/SMC3_Data_Sheet_Freight_Payment_Audit_Toolkit_29236-L.pdf | AR3 |
| Support team of a TMS that uses customer-held SMC3 credentials (Supply Chain Cloud) | How often its customers already hold a RateWare XL licence, and what they pay | https://supplychaincloud.atlassian.net/wiki/spaces/SCCS/pages/1414168623/RateWare+XL+CzarLite+Credentials | AR3 |
| Contracting office, FEMA Information Technology Commodities (awards 70FA3019P00000010, 70FA3020P00000006) | What the $8,764 covered (users, modules, API or web only) | https://www.usaspending.gov/award/CONT_AWD_70FA3020P00000006_7022_-NONE-_-NONE- | AR3 |
| Research team, Benchmarkit | CAC payback and GRR at $1-10k ACV split by sales motion (founder-led, inside sales, self-serve) | https://www.benchmarkit.ai/2026-saas-ai-native-metrics | AR4 |

---

## Sources

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-AR01 | MetricNet, *Benchmarking Roundup: Summary of 2023 IT Service and Support Benchmarks* (webinar deck hosted by BrightTALK) | ©2023 | https://www.brighttalk.com/resource/core/447335/benchmarking-roundup---summary-of-2023-service-and-support-benchmarks-v3_954461.pdf | full PDF (text layer) | slides 11-12 (service desk), 17 (desktop support) |
| N-AR02 | TSIA, "Top Support Services Questions Answered: Insights From TSIA Intelligence" | updated 2025-08-14 | https://www.tsia.com/blog/top-support-services-questions-answered | full page (download) | support cost as % of revenue |
| N-AR03 | SaaS Capital, *Spending Benchmarks for Private B2B SaaS Companies* (2023 survey) | 2023-10 | https://www.saas-capital.com/wp-content/uploads/2023/10/Spending-Benchmarks-for-Private-B2B-SaaS-Companies-2023-W1.pdf | full PDF; charts read from page images | pp. 1-6 |
| N-AR04 | Amazon Lightsail pricing | current | https://aws.amazon.com/lightsail/pricing/ | full page (download) | Linux bundles, managed databases, object storage |
| N-AR05 | DigitalOcean managed databases pricing | current | https://www.digitalocean.com/pricing/managed-databases | full page (download) | PostgreSQL plans |
| N-AR06 | AWS Marketplace, Vanta listing | current | https://aws.amazon.com/marketplace/pp/prodview-5ophamrbfxt44 | full page (download) | 12-month contract dimensions |
| N-AR07 | AWS Marketplace, Drata listing | current | https://aws.amazon.com/marketplace/pp/prodview-3ubrmmqkovucy | full page (download) | 12-month contract dimensions |
| N-AR08 | AWS Marketplace, Secureframe listing | current | https://aws.amazon.com/marketplace/pp/prodview-7cpg4l6nufwgq | full page (download) | 12-month contract dimensions |
| N-AR09 | AWS Marketplace, Sprinto listing | current | https://aws.amazon.com/marketplace/pp/prodview-ixyb464cbjkam | full page (download) | 12-month contract dimensions |
| N-AR10 | Secureframe, "How Much Does a SOC 2 Audit Cost" (markdown copy of the hub page) | page title says 2025 | https://secureframe.com/hub/soc-2/audit-cost.md | full text (download) | cost lines |
| N-AR11 | AWS Marketplace, two CPA firms' SOC 2 audit listings | current | https://aws.amazon.com/marketplace/pp/prodview-rd3i3pcsjdjmy ; https://aws.amazon.com/marketplace/pp/prodview-zwdcg5dyj4pay | full pages (download) | pricing sections (no prices) |
| N-AR12 | SMC3, CzarLite pages (main, shippers, LSPs, technology providers) | current | https://www.smc3.com/czarlite.htm ; https://www.smc3.com/czarlitexl-shippers.htm ; https://www.smc3.com/czarlitexl-lsp.htm ; https://www.smc3.com/czarlitexl-tech.htm | full pages (download) | all text |
| N-AR13 | SMC3, RateWare XL pages (main, LSPs, technology providers), technology providers, partners, integration, product integration, LTL API pages | current | https://www.smc3.com/rateware.htm ; https://www.smc3.com/ratewarexl-lsp.htm ; https://www.smc3.com/ratewarexl-tech.htm ; https://www.smc3.com/technology-providers.htm ; https://www.smc3.com/partners.htm | full pages (download) | all text |
| N-AR14 | SMC3, Terms & Conditions (website) | current | https://www.smc3.com/terms-and-conditions.htm | full page (download) | §§ I, II.D, II.P |
| N-AR15 | SMC3 press releases: "Announces 2027 Pricing" (2026-09-03); "Updates CzarLite Rates" (2026-08-28); "Updates 2025 Pricing" (2024-10-01); "Updating Select Data Module Rates" (2021-12-06, re-read of N-AN29) | as stated | https://www.smc3.com/press-releases-20260903.htm ; https://www.smc3.com/press-releases-20260828.htm ; https://www.smc3.com/press-releases-20241001.htm ; https://smc3.com/press-releases-20211206.htm | full pages (download) | all text |
| N-AR16 | SMC3, *Family of Expert Solutions* brochure | 2016-03 (PDF date) | https://www.smc3.com/knowledge-hub/brochures/SMC3_Brochure_Family_Of_Expert_Solutions_19100.pdf | full PDF | text search for licence |
| N-AR17 | SMC3, webRater datasheet | undated | https://transition.smc3.com/knowledge-hub/data-sheets/SMC3_DataSheet_webRater_21410.pdf | full PDF | all |
| N-AR18 | SMC3, "Smarter LTL Freight Audits Start Here" datasheet (PI# 29236-L) | 2026-04 | https://www.smc3.com/knowledge-hub/data-sheets/SMC3_Data_Sheet_Freight_Payment_Audit_Toolkit_29236-L.pdf | full PDF | all |
| N-AR19 | SMC3, carrier data modules list (search "A") | current | https://smc3.com/carrier-data-modules.jsp?Search=A | full page (download) | note; ABF rows |
| N-AR20 | IBM Support, Sterling TMS "Setting Up Tariffs" | modified 2018-12-08 | https://www.ibm.com/support/pages/setting-tariffs | full page (download) | all |
| N-AR21 | Oracle Transportation Management 25C administration guide, "External Rating" | 25C | https://docs.oracle.com/en/cloud/saas/transportation/25c/otmca/Chunk1909926867.html | full page (download) | all |
| N-AR22 | Supply Chain Cloud help, "RateWare XL (CzarLite) Credentials" | published "Jun 01" (year not shown) | https://supplychaincloud.atlassian.net/wiki/spaces/SCCS/pages/1414168623/RateWare+XL+CzarLite+Credentials | full page (download) | all |
| N-AR23 | USAspending.gov API v2: awards to "SOUTHERN MOTOR CARRIERS"; award detail and transactions for 70FA3019P00000010, 70FA3020P00000006, HTC71108M0011; keyword searches CzarLite, RateWare, SMC3, "SMC 3", "LTL base rate" | data as of 2026-10-08 | https://api.usaspending.gov/api/v2/search/spending_by_award/ ; https://api.usaspending.gov/api/v2/awards/{id}/ ; https://api.usaspending.gov/api/v2/transactions/ | JSON | all returned fields |
| N-AR24 | Material Handling & Logistics 24/7, "3Gtms expands partnership with SMC3" | 2018-04-17 | https://www.materialhandling247.com/article/3gtms_expands_partnership_with_smc3/3gtms | fetch-tool extraction | partnership sentence |
| N-AR25 | SMC3, "Strategic partners deliver complete solutions" alliance datasheet (25034) | undated | https://www.smc3.com/knowledge-hub/data-sheets/Alliance_Partner_DataSheet_25034.pdf | full PDF | all |
| N-AR26 | Benchmarkit, *2025 B2B SaaS Performance Metrics Benchmarks* (2024 data), copy hosted by survey partner HiBob | 2025 | https://www.hibob.com/wp-content/uploads/2025-SaaS-Performance-Metrics-Benchmarks.pdf | full PDF; charts read from page images (pp. 17-18, 22-23, 29-30, 40-44) | key findings; CAC; GRR; gross margin |
| N-AR27 | Benchmarkit, *2026 B2B SaaS & AI-Native Metrics* page | 2026 | https://www.benchmarkit.ai/2026-saas-ai-native-metrics | full page (download) | top findings |
| N-AR28 | Aleph, "Gross revenue retention (GRR): 2026 benchmarks" (on Aleph × Benchmarkit 2026) | updated 2026-10 | https://www.getaleph.com/answers/gross-revenue-retention-saas-2026 | full page (download) | GRR by motion and ACV |
| N-AR29 | OpenView and Paddle, *2023 SaaS Benchmarks Report* (copy on a third-party file host) | ©2023 | https://consultingedge.substack.com/api/v1/file/60377f4c-98be-48ea-9f31-438c64eb2fa1.pdf | full PDF (52 pp.) | pp. 8-12, 34-39 |
| N-AR30 | SaaS Capital, *Research Brief 32: 2025 B2B SaaS Retention Benchmarks* | 2025-09 | https://www.saas-capital.com/wp-content/uploads/2025/09/RB32WS1-2025-B2B-SaaS-Retention-Benchmarks.pdf | full PDF; Figure 1 read from page image | pp. 1-3 |
| N-AR31 | Xero, FY26 results market release (ASX) | 2026-05-14 | https://announcements.asx.com.au/asxpdf/20260514/pdf/06zkqzlkq0xnph.pdf | full PDF | pp. 1-3 |
| N-AR32 | Weave, "Weave Announces Fourth Quarter and Full Year 2025 Financial Results" (IR site) | 2026-02-18 | https://s21.q4cdn.com/507868397/files/doc_news/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-2026.pdf | full PDF | highlights; definitions; income statement |
| N-AR33 | ChartMogul, "Customer churn" metric page; blog "What is a good customer churn rate?" | 2025-12 analysis; blog data Nov 2021-Jan 2022 | https://chartmogul.com/saas-metrics/customer-churn/ ; https://chartmogul.com/blog/good-customer-churn-rate/ | full pages (download); the ARPA chart (SVG) could not be read | text figures |
| N-AR34 | Recurly, churn rate benchmarks | July 2026 data | https://recurly.com/research/churn-rate-benchmarks/ | fetch-tool extraction (download blocked by a captcha) | ARPC bands, SaaS figure |
| N-AR35 | Userpilot, *SaaS Product Metrics Benchmark Report 2025* page | 2025 | https://userpilot.com/saas-product-metrics/ | full page (download) | summary figures, method |
| N-AR36 | *PubTables-1M: Towards comprehensive table extraction from unstructured documents* (arXiv 2110.00061v3) | 2021-11-18 | https://arxiv.org/pdf/2110.00061 | full PDF | §5, Table 4 |
| N-AR37 | *Aligning benchmark datasets for table structure recognition* (arXiv 2303.00716v2) | 2023-05-23 | https://arxiv.org/pdf/2303.00716 | full PDF | abstract; Table 3; Fig. 4 |
| N-AR38 | *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review* (arXiv 2103.06268v2) | 2021-11-08 | https://arxiv.org/pdf/2103.06268 | full PDF | §4, Table 2 |
| N-AR39 | *ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts* (arXiv 2508.03080v1; NLLP 2025) | 2025-08-05 | https://arxiv.org/pdf/2508.03080 | full PDF | §3-4, Table 3 |
| N-AR40 | *Invoice Information Extraction: Methods and Performance Evaluation* (arXiv 2510.15727v2) | 2025-10-22 | https://arxiv.org/pdf/2510.15727 | full PDF | §3.1, §4 |
| N-AR41 | Search summaries only: Vendr (Vanta median $20k, 365 purchases); a SOC 2 directory's audit estimates; unsourced ticket-rate pages; a 2023 trade-press snippet on Saia 5700 rates; Ardent Partners 2025 AP metrics via secondary pages; a news snippet on SMC3's 2024 increase (+4.9%); Dromo and onboarding blogs; vendor claims on rate-confirmation extraction; Box metadata-extraction paper (read at https://arxiv.org/pdf/2510.19334, Table on F1) | 2026-10-08 | as stated in each claim | snippet (Box: full PDF) | as stated |

Cited, not re-read: N-AA02, N-AA47, N-AA50-N-AA55 (check AA), N-AJ66, N-AJ67 (check AJ), N-A10, N-A13, N-A16, N-A20, N-A36 (check A), N-AL23, N-AL44 (check AL), N-AC34 (check AC).

---

## Could not access, or not found

**Blocked or unusable:**
- **KeyBanc/Sapphire 2025 SaaS survey:** the key.com library page returned 403 to the fetch tool and nothing to a plain download. Only the press-release headline was seen (search summary).
- **OpenView's own site:** report pages return 404 (the firm has closed); the report was read from a third-party copy (N-AR29), so it is labelled *assumed*.
- **Recurly:** a plain download hit a captcha; read only through the fetch tool.
- **Supply Chain 24/7 (Saia 5700 article):** 403 to both download and fetch tool.
- **ChartMogul ARPA chart:** an SVG with text drawn as shapes; the middle ARPA bands ($100-500 a month) could not be read. Only the end values in the text were used.
- **HDI/MetricNet 2021 "Understanding Cost per Ticket":** the figures sit in images; no numbers in the text.
- **AWS Marketplace CPA-firm listings:** no prices ("Request private offer").
- **SEC EDGAR:** not fetched by rule; Weave's 10-K was not read (the IR release was used).
- **Benchmarkit 2026 full report:** not read beyond its public page; ACV cuts for 2025 data seen only through Aleph's write-up.

**Searched, not found:**
- Tickets per customer: "SaaS customer support tickets per customer per month benchmark B2B report"; "TSIA support services benchmark 'support cost' percent of revenue software company incidents per customer per year"; "Zendesk Benchmark report software industry average tickets per month per customer OR 'tickets per 1,000 customers' B2B".
- Neutral SOC 2 audit fees: "CPA firm SOC 2 Type II audit fixed fee published pricing page startup 'Type I' 'Type II' price"; USAspending keyword searches "SOC 2 Type II", "SOC 2 Type 2", "SOC 2 audit" (no audit purchases found).
- SMC3 multi-customer licence terms: "'SMC3' RateWare OR CzarLite 'license' required customer must obtain own license TMS documentation"; "'Southern Motor Carriers' OR 'SMC3' CzarLite OR RateWare purchase order OR 'sole source' OR contract award amount agency"; "'SMC3' 'your own' license ... 'pass-through' freight audit software"; "freight audit company 'RateWare' OR 'CzarLite' audit LTL invoices for clients licensed SMC3 'on behalf of' shippers".
- Free carrier base tariffs: "LTL carrier base rate tariff download public ODFL 559 OR 'ABF 504' OR 'EXLA 500' OR 'Saia 599' ..."; "saia.com Saia 5700 base rates tariff download rate tables shippers".
- CAC by sales motion: "'New CAC Ratio' by ACV '$5K' OR '$15K' B2B SaaS benchmark 2025 median sales-led inside sales SMB"; "Benchmarkit 2025 ... CAC payback gross revenue retention by ACV PDF" (found the report; no founder-led cut).
- Onboarding: "Userpilot product metrics benchmark report ..."; "B2B SaaS benchmark share of new accounts that complete data import or connect integration during self-serve onboarding percent study"; "OpenView 2023 SaaS benchmarks report PDF ... activation".
- Freight document extraction: "freight 'rate confirmation' OR 'rate card' OR tariff document extraction accuracy LLM evaluation study percent fields correct logistics".

**Not searched (budget):** cost structure of public document-processing companies; churn disclosures of other SMB SaaS firms (SPS Commerce, Thryv); Pendo and Appcues onboarding reports; NMFTA ClassIT+ multi-customer terms (check AL covers); cyber insurance for a small SaaS; Vendr's pages for Drata, Secureframe and Sprinto; Pavilion's 2024 edition (downloaded, not read).

---

## Claim ledger

| Claim ID | Question | Claim in one sentence | Number (unit, denominator, population, period) | Verbatim quote (≤40 words) + page/section | Source ID + URL | Published / accessed | Source type | Publisher and what they sell | Origin trace | Fits our segment? | Proposed label | Load-bearing? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-AR01 | AR1 | An email or web support ticket costs about $20-24 fully loaded at an IT service desk | $24.24 average, $19.96 median, $5.92-58.54 range; per contact; one peer group of IT service desks; 2023 | "Average Cost per Web Ticket/Email Contact $24.24 $5.92 $19.96 $58.54" (columns Average, Min, Median, Max), slide 11 | N-AR01 https://www.brighttalk.com/resource/core/447335/benchmarking-roundup---summary-of-2023-service-and-support-benchmarks-v3_954461.pdf | ©2023 / 2026-10-08 | benchmark firm's deck | MetricNet; sells benchmarking reports ($399-2,999 a KPI set, slide 22) | MetricNet's own benchmark database; peer group size not stated | Partly: internal IT desks, not a vendor's customers | *verified* | Y |
| C-AR02 | AR1 | Other channels cost similar amounts per contact | voice $18.35, chat $23.26, all contacts incl. self-help $17.07; 2023 | "Average Cost per Contact (incl. Self-Help) $17.07 $5.91 $14.80 $34.17", slide 11 | N-AR01 | ©2023 / 2026-10-08 | as above | as above | as above | Partly | *verified* | N |
| C-AR03 | AR1 | An email ticket takes about 14 minutes at $1.54-1.71 a minute | 13.70 min average; $1.71 average, $1.54 median per minute; 2023 | "Web Ticket/Email Handle Time (minutes) 13.70 3.80 13.77 24.91"; "Average Cost per Web Ticket/Email Minute $1.71 $0.92 $1.54 $2.89", slide 11 | N-AR01 | ©2023 / 2026-10-08 | as above | as above | as above | Partly | *verified*; $92-103 an hour [our calc] | Y |
| C-AR04 | AR1 | Employees file about 0.38 desktop-support tickets a month | 0.38 average; per user per month; internal desktop support; 2023 | "Tickets per User per Month 0.38 0.17 0.39 0.67", slide 17 | N-AR01 | ©2023 / 2026-10-08 | as above | as above | as above | No (employees, not customers) | *verified*; not comparable | N |
| C-AR05 | AR1 | Half of TSIA's companies keep support cost under 3.8% of revenue | 49% at 0-3.8%; 22% at 3.8-6%; 13.6% at 10-18%; share of companies; TSIA members; 2025 | "49% of companies report that their support cost of goods sold (COGS) falls between 0% and 3.8% of revenue . 22% fall into the 3.8% to 6% range . 13.6% report support costs between 10% and 18%" | N-AR02 https://www.tsia.com/blog/top-support-services-questions-answered | 2025-08-14 / 2026-10-08 | association page | TSIA; sells membership and benchmarking | TSIA's benchmark data; sample not stated | Partly (mostly larger tech firms) | *verified* | Y |
| C-AR06 | AR1, AR4 | Small private SaaS firms spend a median 10% of ARR on support/success and about 5% on hosting | % of ARR, medians, by ARR band; 2023 survey | "a typical B2B company with $3 Million to $5 Million in ARR spends the following as a median percent of ARR: • 5% on Hosting Costs • 5% on DevOps Costs", p. 4 | N-AR03 https://www.saas-capital.com/wp-content/uploads/2023/10/Spending-Benchmarks-for-Private-B2B-SaaS-Companies-2023-W1.pdf | 2023-10 / 2026-10-08 | lender's survey | SaaS Capital; lends to SaaS firms | its 2023 annual survey; other bands read from the chart image | Partly (software firms in general) | *verified* | Y |
| C-AR07 | AR1, AR4 | The median sub-$1M-ARR company spent $18,360 on hosting and $31,000 on customer success | median $ a year; private B2B SaaS under $1M ARR; 2023 survey | chart "Less than $1 Million in ARR": "$18,360" Hosting; "$31,000" Customer Success; "$46,250" Sales; "$18,540" Marketing, p. 5 (image) | N-AR03 | 2023-10 / 2026-10-08 | as above | as above | as above | Partly | *verified* (chart) | Y |
| C-AR08 | AR1 | At $1-3M ARR the medians are $115,250 hosting and $159,380 customer success | median $ a year; 2023 | chart "$1 - $3 Million in ARR": "$115,250" Hosting; "$159,380" Customer Success; "$220,000" Sales, p. 6 (image) | N-AR03 | as above | as above | as above | as above | Partly | *verified* (chart) | N |
| C-AR09 | AR1 | Bootstrapped firms spend 91% of ARR in total, equity-backed 120%, and the latter 25% more on success | % of ARR; 2023 | "The total median spend across all departments is 91% of Annual Recurring Revenue (ARR) for bootstrapped companies while equity-backed are spending 120% of ARR.", p. 2 | N-AR03 | as above | as above | as above | as above | Partly | *verified* | N |
| C-AR10 | AR1 | A 4 GB server is $24 and a 4 GB failover database $120 a month on Lightsail | $ a month, list, US regions | "$24 USD/mo 4 GB Memory 2 vCPUs 80 GB SSD Disk 4 TB Transfer"; "$60 Standard plan USD/mo $120 High availability plan USD/mo 4 GB Memory 2 Core Processor 120 GB SSD Disk" | N-AR04 https://aws.amazon.com/lightsail/pricing/ | current / 2026-10-08 | company price page | AWS; sells cloud hosting | primary | Yes | *verified* | Y |
| C-AR11 | AR1 | The smallest DigitalOcean managed PostgreSQL is $15.15 a month | $ a month, list | "1 GiB 1 vCPU Storage range: 10 GiB - 30 GiB. $0.215/GiB/mo, 10 GiB increments. $0.02254 $15.15" | N-AR05 https://www.digitalocean.com/pricing/managed-databases | current / 2026-10-08 | company price page | DigitalOcean; sells cloud hosting | primary | Yes | *verified* | N |
| C-AR12 | AR1 | (merged into C-AR64) | — | — | — | — | — | — | — | — | — | — |
| C-AR13 | AR2 | Vanta lists $14,000-23,000 for 12 months for 1-20 employees | $ per 12 months, list, AWS Marketplace | "Essentials Package Starting cost for 1-20 employees $14,000.00 Professional Package Starting cost for 1-20 employees $23,000.00 Plus Package Starting cost for 1-20 employees $21,500.00" | N-AR06 https://aws.amazon.com/marketplace/pp/prodview-5ophamrbfxt44 | current / 2026-10-08 | company price listing | Vanta; sells compliance automation | primary (list price; private offers differ) | Yes (company-level cost) | *verified* (list) | Y |
| C-AR14 | AR2 | Drata lists $25,000 for the platform plus $7,500 for SOC 2 | $ per 12 months, list | "Drata Platform Fee Access to the Drata SaaS platform with capacity for a 100 FTE org $25,000.00 SOC 2 Framework SOC 2 2017 control set $7,500.00" | N-AR07 https://aws.amazon.com/marketplace/pp/prodview-3ubrmmqkovucy | current / 2026-10-08 | company price listing | Drata; compliance automation | primary | Yes | *verified* (list) | Y |
| C-AR15 | AR2 | Secureframe lists $7,500 platform plus $7,500 first framework | $ per 12 months, list | "Platform Access the Secureframe Platform up to 100 Employees $7,500.00 First Framework Choice of any Framework $7,500.00" | N-AR08 https://aws.amazon.com/marketplace/pp/prodview-7cpg4l6nufwgq | current / 2026-10-08 | company price listing | Secureframe; compliance automation | primary | Yes | *verified* (list) | Y |
| C-AR16 | AR2 | Sprinto lists $7,500 platform plus $2,000 for one framework | $ per 12 months, list | "Sprinto Starter Platform Includes all core platform features up to 100 employees ... $7,500.00 First Compliance Framework ... starting at $2000 each." | N-AR09 https://aws.amazon.com/marketplace/pp/prodview-ixyb464cbjkam | current / 2026-10-08 | company price listing | Sprinto; compliance automation | primary | Yes | *verified* (list) | Y |
| C-AR17 | AR2 | A compliance vendor puts Type I audits at $5-20k and Type II at $7-150k | $ per audit; undefined sample; page says 2025 | "For the audit alone, you can expect the SOC 2 Type 1 cost to be around $5-20k, while the SOC 2 Type 2 cost is $7k-150k on average." | N-AR10 https://secureframe.com/hub/soc-2/audit-cost.md | 2025 (title) / 2026-10-08 | vendor guide | Secureframe; sells compliance automation | not traced; one unnamed firm at "$20,000 for a SOC 2 Type I audit and $30,000 for a SOC 2 Type II" | Yes | *assumed* (vendor) | Y |
| C-AR18 | AR2 | Licensed CPA firms selling SOC 2 audits on AWS Marketplace publish no price | — | "Pricing is based on your specific requirements, including the Trust Services Criteria in scope, system complexity, and the reporting period." | N-AR11 https://aws.amazon.com/marketplace/pp/prodview-rd3i3pcsjdjmy | current / 2026-10-08 | firm's listing | a CPA firm; sells audits | primary | Yes | *verified* | N |
| C-AR19 | AR2 | A procurement broker says buyers pay Vanta a median $20,000 a year | $20,000 median; 365 purchases; range $7,500-56,943 | "Median buyer pays $20,000 per year, based on data from 365 purchases. Lowest was $7,500 and highest was $56,943." (search snippet) | N-AR41 (vendr.com/marketplace/vanta) | not shown / 2026-10-08 | broker page | Vendr; sells SaaS-buying services | Vendr's customer purchases | Yes | *assumed* (snippet) | N |
| C-AR20 | AR2 | SOC 2 costs about $29.5-58k in year 1 and $16.5-68k a year after | $ a year; small SaaS | — | our calculation from C-AR13-C-AR17 | 2026-10-08 | [our calc] | — | platform list prices + vendor audit ranges + vendor pen-test figure | Yes | **[our calc]** (inputs mixed *verified*/*assumed*) | Y |
| C-AR21 | AR3 | FEMA paid SMC3 $8,764 for a year of CzarLite and RateWare web access | $8,764; one agency system; 2019-03-22 to 2020-03-21 | "TO PURCHASE CZARLITE AND RATEWARE WEB ACCESS SUBSCRIPTIONS FOR THE LOGISTICS SUPPLY CHAIN MANAGEMENT SYSTEM (LSCMS)"; obligation 8764.0; "NOT COMPETED UNDER SAP" | N-AR23 https://api.usaspending.gov/api/v2/awards/CONT_AWD_70FA3019P00000010_7022_-NONE-_-NONE-/ | 2019-03-22 / 2026-10-08 | federal procurement record | US Treasury's USAspending; sells nothing | FPDS contract data | Partly (one organisation, not a multi-customer SaaS) | *verified* | Y |
| C-AR22 | AR3 | FEMA renewed at the same $8,764 in 2020 and exercised an option at $8,764 in 2021 | $8,764 a year; 2020-03-18 to 2021-03-21, then option 1 | "TO PURCHASE CZARLITE AND RATEWAREXL WEB ACCESS SUBSCRIPTIONS ..."; P00001: "THE PURPOSE OF THIS MODIFICATION IS TO EXERCISE OPTION PERIOD 1, INCREASE PURCHASE ORDER AMOUNT AND EXTEND THE PERIOD OF PERFORMANCE." | N-AR23 https://api.usaspending.gov/api/v2/transactions/ (award CONT_AWD_70FA3020P00000006_7022_-NONE-_-NONE-) | 2020-03-20, 2021-01-29 / 2026-10-08 | federal procurement record | as above | as above | Partly | *verified* | Y |
| C-AR23 | AR3 | DoD paid SMC3 about $5,500 to renew an NMFC data licence in 2008 | $5,803 obligated, $303 de-obligated; 2008 | "NMFC DATA LICENSE RENEWAL"; "NMFC DATA LICENSE DE-OBLIGATION OF EXCESS FUNDS" | N-AR23 (award CONT_AWD_HTC71108M0011_9700_-NONE-_-NONE-) | 2008-01-07 / 2026-10-08 | federal procurement record | as above | as above | No (class data, old) | *verified* | N |
| C-AR24 | AR3 | SMC3 raises CzarLite and RateWare XL licence fees 3.9% for 2027 | +3.9%; licence fees; 2027 | "SMC³ will implement a 3.9% increase on Czarlite ® , RateWare ® XL, CarrierConnect ® XL and BatchMark ® XL license fees in 2027." | N-AR15 https://www.smc3.com/press-releases-20260903.htm | 2026-09-03 / 2026-10-08 | company press release | SMC3; sells LTL rate data and software | primary | Yes | *verified* | Y |
| C-AR25 | AR3 | SMC3 raised the same licence fees 3% for 2025, data modules unchanged | +3%; 2025 | "SMC³ will implement a 3% increase on Czarlite®, RateWare® XL, CarrierConnect® XL and BatchMark® XL license fees in 2025. RateWare XL data modules pricing will remain the same." | N-AR15 https://www.smc3.com/press-releases-20241001.htm | 2024-10-01 / 2026-10-08 | company press release | SMC3 | primary | Yes | *verified* | N |
| C-AR26 | AR3 | CzarLite was an $800 data module and a carrier tariff module $300 from 2022 | $ per module; unit and period not stated; from 2022-01-01 | "The prices vary by module and service level." ... "Data Module Updated Rate CzarLite $800 CanadaLite $800 MexicoLite $800 ... Carrier Tariff Stock $300" | N-AR15 https://smc3.com/press-releases-20211206.htm (re-read of N-AN29) | 2021-12-06 / 2026-10-08 | company press release | SMC3 | primary | Yes | *verified* (unit unknown) | Y |
| C-AR27 | AR3 | In IBM's TMS each shipper needs its own SMC authorisation to use a tariff | per shipper, per tariff | "you must have a license from SMC to use these tariffs in Sterling TMS" ... "No other shippers can use this tariff unless they have also been authorized by SMC." | N-AR20 https://www.ibm.com/support/pages/setting-tariffs | modified 2018-12-08 / 2026-10-08 | vendor documentation | IBM; sells TMS software | primary for IBM's practice | Partly (a TMS used by shippers) | *verified* | Y |
| C-AR28 | AR3 | In another TMS the customer supplies its own SMC3 credentials under its own licence | per customer | "Note: These values are provided by SMC 3 . If you need any of these credentials, reach out to your SMC 3 contact regarding your RateWare XL license." | N-AR22 https://supplychaincloud.atlassian.net/wiki/spaces/SCCS/pages/1414168623/RateWare+XL+CzarLite+Credentials | "Jun 01" / 2026-10-08 | vendor documentation | Supply Chain Cloud; sells shipping/TMS software | primary | Partly | *verified* | Y |
| C-AR29 | AR3 | Oracle's TMS needs a RateWare XL licence key set by the customer | — | "glog.RatingEngine.RatewareXL.Username= glog.RatingEngine.RatewareXL.Password= glog.RatingEngine.RatewareXL.License=" | N-AR21 https://docs.oracle.com/en/cloud/saas/transportation/25c/otmca/Chunk1909926867.html | 25C / 2026-10-08 | vendor documentation | Oracle; sells TMS | primary | Partly | *verified* | N |
| C-AR30 | AR3 | SMC3 sells RateWare XL and CzarLite to LSPs that rate for many shippers | — | "Manage and optimize LTL rating complexity and logic for multiple shippers, in both density and class-based pricing" (RateWare XL for LSPs); "Negotiate across carriers and on behalf of multiple customers using the same base rate system" (CzarLite for LSPs) | N-AR13 https://www.smc3.com/ratewarexl-lsp.htm ; N-AR12 https://www.smc3.com/czarlitexl-lsp.htm | current / 2026-10-08 | company pages | SMC3 | primary | Yes (a multi-client licence type exists) | *verified* | Y |
| C-AR31 | AR3 | SMC3 markets an audit toolkit used by a firm auditing bills for many shippers | — | "When you're auditing thousands of freight bills for multiple shippers and LSPs, speed, accuracy and automations make all the difference." (customer testimonial) | N-AR18 https://www.smc3.com/knowledge-hub/data-sheets/SMC3_Data_Sheet_Freight_Payment_Audit_Toolkit_29236-L.pdf | 2026-04 / 2026-10-08 | company datasheet | SMC3 | testimonial from a freight-payment firm | Yes | *verified* (that SMC3 publishes it) | Y |
| C-AR32 | AR3 | CzarLite was licensed to 1,500+ shippers and 300+ intermediaries by 2016 | counts; 2016 | "CzarLite has been licensed to more than 1,500 shippers, as well as over 300 logistics intermediaries." | N-AR16 https://www.smc3.com/knowledge-hub/brochures/SMC3_Brochure_Family_Of_Expert_Solutions_19100.pdf | 2016-03 / 2026-10-08 | company brochure | SMC3 | primary | Partly | *verified*; old | N |
| C-AR33 | AR3 | TMS and ERP vendors integrate SMC3 as alliance partners | — | "With SMC³, a single integration point delivers access to all rates, points of service and transit times." | N-AR13 https://www.smc3.com/technology-providers.htm | current / 2026-10-08 | company page | SMC3 | primary | Partly | *verified* | N |
| C-AR34 | AR3 | Carrier base tariffs are sold as SMC3 data modules for RateWare and BatchMark | e.g., ABF 504-AX effective 2026-06-22 | "*Please Note: Pricing may vary for custom shipper tariffs with multiple geographies; data modules are designed for use in the SMC³ RateWare and SMC³ BatchMark products." | N-AR19 https://smc3.com/carrier-data-modules.jsp?Search=A | current / 2026-10-08 | company list | SMC3 | primary | Yes | *verified* | Y |
| C-AR35 | AR3 | SMC3's website licence bars resale, derivative use and data mining of the site | — | "This license does not include any resale or commercial use of this site or its contents; any collection and use of any product listings, descriptions, or prices; any derivative use of this site or its contents" | N-AR14 https://www.smc3.com/terms-and-conditions.htm | current / 2026-10-08 | website terms | SMC3 | primary | No (site, not products) | *verified* | N |
| C-AR36 | AR3 | CzarLite data in webRater sits behind access codes | — | "Access codes are required for CzarLite, CanadaLite and MexicoLite pricing data." | N-AR17 https://transition.smc3.com/knowledge-hub/data-sheets/SMC3_DataSheet_webRater_21410.pdf | undated / 2026-10-08 | company datasheet | SMC3 | primary | Partly | *verified* | N |
| C-AR37 | AR3 | SMC3 claims 3,000+ customers (terms page) and 5,000+ users (partner datasheet) | counts | "SMC³ presently serves more than 3,000 customers throughout the United States and Canada"; "More than 5,000 North American shippers, carriers, logistics service providers and technology partners rely on SMC³" | N-AR14; N-AR25 https://www.smc3.com/knowledge-hub/data-sheets/Alliance_Partner_DataSheet_25034.pdf | current / 2026-10-08 | company pages | SMC3 | primary; the two counts differ | Partly | *verified* (that SMC3 says so) | N |
| C-AR38 | AR3 | A TMS vendor offers SMC3 products to its customers | — | "to offer the SMC³ RateWare® XL, CarrierConnect® XL and CzarLite® solutions to its customers" (fetch summary) | N-AR24 https://www.materialhandling247.com/article/3gtms_expands_partnership_with_smc3/3gtms | 2018-04-17 / 2026-10-08 | trade press | MH&L 24/7; media | press release | Partly | *assumed* (fetch summary) | N |
| C-AR39 | AR3 | Saia's base rates were said to be available on its website | — | "Updated Saia 5700 rates and the Saia 170D rules tariff are available at saia.com" (search snippet) | N-AR41 (supplychain247.com, 403) | 2023 / 2026-10-08 | trade press snippet | Supply Chain 24/7; media | Saia press release, not read | Yes | *assumed* (snippet) | N |
| C-AR40 | AR4 | Median CAC payback is 8 months at $1-5k ACV and 14 months at $5-10k | months; gross-margin-adjusted; N=148; 2024 data | "CAC Payback Period should be evaluated in context of the company attribute most correlated to the metric's performance, which is Annual Contract Value (ACV)"; values from chart, p. 23 | N-AR26 https://www.hibob.com/wp-content/uploads/2025-SaaS-Performance-Metrics-Benchmarks.pdf | 2025 / 2026-10-08 | benchmark survey | Benchmarkit; sells benchmarking (with Maxio and partners) | survey self-reports; partner-hosted copy | Partly (software in general) | *verified* (chart read from image) | Y |
| C-AR41 | AR4 | Median New CAC ratio is $2.00 per $1 of new ARR at $1-5k ACV and $1.60 at $5-10k | $ S&M per $1 new ARR; N=73; 2024 | "the New CAC Ratio increased by 14% in 2024 to a median of $2.00 of Sales and Marketing expense to acquire $1.00 of New Customer ARR.", p. 17; ACV values from chart, p. 18 | N-AR26 | 2025 / 2026-10-08 | as above | as above | as above | Partly | *verified* (chart) | Y |
| C-AR42 | AR4 | Median GRR is 85% at $1-5k and $5-10k ACV | % GRR; N=225; 2024 | "GRR has continued to decrease slightly over the past three years from 90% to 88% - though this could be due to selection bias of participants.", p. 29; ACV values from chart, p. 30 | N-AR26 | 2025 / 2026-10-08 | as above | as above | as above | Partly | *verified* (chart) | Y |
| C-AR43 | AR4 | Median gross margin is 77% on total revenue and 81% on subscriptions | %; N=196 (total), N=76 (subscription); 2024 | "Total Revenue (77% median) ● Subscription Revenue 81% median) ● Pro Services Revenue (30%)", p. 44 | N-AR26 | 2025 / 2026-10-08 | as above | as above | as above | Partly | *verified* | Y |
| C-AR44 | AR4 | Benchmarkit 2026: software margin 80% median; GRR fell from 88% to 84% | %; 2025 data | "80% median software margin \| Stable through 4 years"; "GRR: 88% → 84% \| 75th percentile: 95% → 91%" | N-AR27 https://www.benchmarkit.ai/2026-saas-ai-native-metrics | 2026 / 2026-10-08 | benchmark page | Benchmarkit | survey | Partly | *verified* | Y |
| C-AR45 | AR4 | GRR under $5k ACV was 80% in 2025, and product-led firms 79% | %; 342 companies; 2025 data | "Sub-$5K ACV sits at 80%"; "Sales-led 88% ... Hybrid 80% ... Product-led (PLG) 79%" | N-AR28 https://www.getaleph.com/answers/gross-revenue-retention-saas-2026 | 2026-10 / 2026-10-08 | partner write-up | Aleph; sells FP&A software (report co-author) | Aleph × Benchmarkit 2026 survey | Partly | *assumed* (secondary write-up) | Y |
| C-AR46 | AR4 | OpenView 2023: under $1M ARR, margin 85%, payback 8 months, GDR 84%; at $1-5M, 80%, 11 months, 90% | medians (quartiles) by ARR; Q2 2023 | "Gross Margins 85% (70-95%) 80% (72-88%)"; "CAC Payback (months) 8 (5-11 mo's) 11 (5-16 mo's)"; "Gross Dollar Retention 84% (78-95%) 90% (72-95%)", p. 12 | N-AR29 https://consultingedge.substack.com/api/v1/file/60377f4c-98be-48ea-9f31-438c64eb2fa1.pdf | ©2023 / 2026-10-08 | VC survey report | OpenView (closed VC firm) and Paddle (billing vendor) | survey; copy on a third-party host, provenance unconfirmed | Partly | *assumed* (third-party copy) | Y |
| C-AR47 | AR4 | SaaS Capital 2025: GRR 90% and NRR 98% under $12k ACV | medians; 1,000+ firms over $1M ARR; Q1 2025 | "Bootstrapped companies report NRR of 104% and 92% GRR."; Figure 1 "Less than $12k": 98% / 90%; "Excludes Companies with less than $1M ARR" | N-AR30 https://www.saas-capital.com/wp-content/uploads/2025/09/RB32WS1-2025-B2B-SaaS-Retention-Benchmarks.pdf | 2025-09 / 2026-10-08 | lender's survey | SaaS Capital; lends to SaaS firms | annual survey | Partly | *verified* (Figure read from image) | Y |
| C-AR48 | AR4 | Xero lost 1.14% of customers a month in FY26 at 83.9% gross margin | 1.14% a month (≈12.9% a year [our calc]); 4.92M customers; ARPC NZ$55.44 a month; FY to 2026-03-31 | "Average monthly churn (1.14%)10 remained below pre-pandemic trends"; "Gross margin percentage 83.9% 89.0% -5.1pp" | N-AR31 https://announcements.asx.com.au/asxpdf/20260514/pdf/06zkqzlkq0xnph.pdf | 2026-05-14 / 2026-10-08 | listed company release | Xero; sells SMB accounting software | company-reported, unaudited KPI | Partly (SMB, lower ACV) | *verified* | Y |
| C-AR49 | AR4 | Weave kept 89% of revenue gross and ran a 72.1% gross margin in 2025 | GRR 89%, NRR 93%; GAAP GM 72.1%; revenue $239.0M; 39,625 locations; S&M $102,703k; FY2025 | "Dollar-Based Gross Retention Rate (GRR) was 89% as of December 31, 2025."; "Full year GAAP gross margin of 72.1%" | N-AR32 https://s21.q4cdn.com/507868397/files/doc_news/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-2026.pdf | 2026-02-18 / 2026-10-08 | listed company release | Weave; sells SMB practice software | company-reported | Partly (SMB vertical, ~$6k a location) | *verified* | Y |
| C-AR50 | AR4 | Weave spends roughly $12k of S&M per gross new location, a ~31-33-month payback | $12,115; 8,478 gross adds; GP $4,349-4,618 a location; FY2025 | — | our calculation from C-AR49 | 2026-10-08 | [our calc] | — | assumes location churn ≈ 1 − GRR; acquisition in counts makes CAC an under-estimate | Partly | **[our calc]** | Y |
| C-AR51 | AR4 | Monthly logo churn falls from 6.1% (ARPA under $25) to 2.2% (over $500) | median % a month; ChartMogul customers; Nov 2021-Jan 2022 | "For companies with ARPA per month in the range of <$25, the median monthly customer churn rate is 6.1%. It decreases to 2.2% as your ARPA per month increases to >$500." | N-AR33 https://chartmogul.com/blog/good-customer-churn-rate/ | data 2021-22 / 2026-10-08 | vendor data page | ChartMogul; sells subscription analytics | its customers' billing data | Partly | *verified* (that ChartMogul reports it) | Y |
| C-AR52 | AR4 | Median monthly logo churn is 1.7% where NRR ≥100% and 7.3% where under 60% | median % a month; 3,500 software companies; Dec 2025 analysis | "Companies in the low NRR range have a median 7.3% customer churn, more than four times the 1.7% median of those with ≥100% NRR." | N-AR33 https://chartmogul.com/saas-metrics/customer-churn/ | 2025-12 / 2026-10-08 | vendor page | ChartMogul | as above | Partly | *verified* (as above) | N |
| C-AR53 | AR4 | Recurly reports 2.87% churn at $100-250 a month per customer, unit unclear | % (labelled "median annual"); Recurly network; July 2026 | "The Recurly network shows a median annual churn rate of 3.22% for SaaS businesses (July 2026 data)." (fetch summary) | N-AR34 https://recurly.com/research/churn-rate-benchmarks/ | July 2026 / 2026-10-08 | vendor page | Recurly; sells subscription billing | its network; page internally inconsistent | Partly | *assumed* (fetch summary; unit unclear) | N |
| C-AR54 | AR4 | (annual equivalents of monthly churn, shown in §AR4.2) | 1.14% → 12.9%; 2.2% → 23.4%; 6.1% → 53.0% | — | our calculation: 1 − (1 − m)¹² | 2026-10-08 | [our calc] | — | — | — | **[our calc]** | N |
| C-AR55 | AR5 | Userpilot's customers: 37.5% activation, 19.2% checklist completion, 1.5 days to value | averages; 62 / 188 / 62 companies; 2025 page | "37.5% Activation Rate 62 companies analyzed 19.2% Onboarding Checklist Completion Rate 188 companies analyzed 1 Day 12 Hrs Time-To-Value 62 companies analyzed" | N-AR35 https://userpilot.com/saas-product-metrics/ | 2025 / 2026-10-08 | vendor report page | Userpilot; sells onboarding software | first-party data from its own dashboards | No (users, not a contract-loading task) | *verified* that Userpilot reports it (stated sample; not neutral) | Y |
| C-AR56 | AR5 | A strong table reader gets every cell right in 94.7% of simple tables but 69.4% of complex ones | share of tables exactly right; PubTables-1M test set; 2021 | "AccCont ... the percentage of tables whose text content matches the ground truth exactly for every cell"; Table 4, DETR: "Simple 0.9468 ... Complex 0.6944 ... All 0.8138" | N-AR36 https://arxiv.org/pdf/2110.00061 | 2021-11-18 / 2026-10-08 | research paper | Microsoft research; the model's authors | primary | Partly (scientific tables, not rate sheets) | *verified* | Y |
| C-AR57 | AR5 | Whole-table exact match on another benchmark was 65-81% | share of tables; ICDAR-2013; 2023 | "Baseline exact match accuracy for TATR evaluated on the ICDAR-2013 benchmark is 65% when trained on PubTables-1M, 42% when trained on FinTabNet, and 69% combined." | N-AR37 https://arxiv.org/pdf/2303.00716 | 2023-05-23 / 2026-10-08 | research paper | as above | primary | Partly | *verified* | Y |
| C-AR58 | AR5 | Pre-LLM contract models reached 44% precision at 80% recall | CUAD; 2021 | "DeBERTa-xlarge has the best performance (44.0% Precision @ 80% Recall)"; "a lawyer would need to read through about 2 irrelevant clauses for every 1 relevant clause" | N-AR38 https://arxiv.org/pdf/2103.06268 | 2021-11-08 / 2026-10-08 | research paper | university authors | primary | No (clauses, old models) | *verified* | N |
| C-AR59 | AR5 | 2025 LLMs score F1 0.50-0.64 finding risk clauses in contracts | F1; CUAD test set, 41 categories; 2025 | "GPT 4.1 and GPT 4.1 mini, achieve the highest F1 scores (0.641 and 0.644, respectively)"; Table 3 "Claude Sonnet 4 0.523", "Gemini 2.5 Pro Preview 0.497" | N-AR39 https://arxiv.org/pdf/2508.03080 | 2025-08-05 / 2026-10-08 | research paper | university authors | primary | Partly (clauses, not numbers in rate tables) | *verified* | N |
| C-AR60 | AR5 | A vendor reports F1 0.75-0.82 for LLM metadata extraction on CUAD | F1; CUAD; 2025 | "With an 8192-token context window: F1 score of 0.80 (vs. 0.75 baseline)" | N-AR41 https://arxiv.org/pdf/2510.19334 | 2025-10-22 / 2026-10-08 | vendor research paper | Box; sells content and AI software | primary | Partly | *assumed* (vendor) | N |
| C-AR61 | AR5 | An LLM extractor read 94% of invoice fields right, and 7% of invoices failed an add-up check | 94% fields, 91% line items, 93% checks passed; 102 invoices; 2025 | "The extractor achieved an accuracy of 94%"; "exhibited a slightly lower accuracy of 91%"; "The LlamaExtractor passed 93% of these general consistency checks." | N-AR40 https://arxiv.org/pdf/2510.15727 | 2025-10-22 / 2026-10-08 | industry preprint | authors at a staffing firm's data-science unit; no stake in the tools tested stated | primary; small sample | Partly (invoices, not freight) | *verified* | Y |
| C-AR62 | AR5 | Best-in-class AP teams process 49.2% of invoices with no touch, others 23.4% | share of invoices; 212 AP professionals; 2024 data | "best-in-class performance of 49.2% straight-through processing" (snippet of a vendor's summary) | N-AR41 (tungstenautomation.com; imagetotable.ai) | 2025 / 2026-10-08 | secondary summaries of an analyst report | Ardent Partners (analyst, sponsored by AP vendors) via vendors | not read at source | Partly | *assumed* (secondary) | N |
| C-AR63 | AR1 | Our support cost is about $60-291 a year steady state plus $185-616 of first-year onboarding help | $ per customer a year | — | our calculation from C-AR01, C-AR03 and our ticket and hour assumptions | 2026-10-08 | [our call] / [our calc] | — | tickets per customer and onboarding hours are [our call] | Yes | **[our calc]** | Y |
| C-AR64 | AR1 | Hosting costs about $2.4-6.0k a year, $24-60 per customer at 100 customers | $ per customer a year | — | our calculation from C-AR10 and a [our call] stack | 2026-10-08 | [our calc] | — | list prices; stack and tooling are [our call] | Yes | **[our calc]** | Y |
| C-AR65 | AR3 | FEMA's $8,764 is 2.2× the old $3,900 fee at a $2M customer, or $29-88 a customer if company-level | ratio; $ per customer | — | our calculation from C-AR21 and check AJ's fee | 2026-10-08 | [our calc] | — | the old contingency fee is a scale marker, not a price | Yes | **[our calc]** | Y |

(C-AR12 was merged into C-AR64 while drafting and is not used.)

---

## Coincidence watch

| Figure | Sources that give it | Do they share an origin? | Note |
|---|---|---|---|
| **"8 months" CAC payback** | OpenView 2023, under $1M **ARR** [C-AR46]; Benchmarkit 2025, under $1k and $1-5k **ACV** [C-AR40]; High Alpha 2025, $1-5M ARR (check A) | No shared data, but all are self-reported surveys of VC-adjacent firms | Different cuts (company size vs contract size). High Alpha warns early-stage firms under-count CAC. Agreement is not corroboration of a real firm's payback; Weave's ~31-33 months [C-AR50] is the counter-example |
| **~90% GRR** | SaaS Capital under $12k ACV 90% [C-AR47]; Benchmarkit under $1k ACV 90% [C-AR42]; OpenView $1-5M ARR 90% [C-AR46]; Weave 89% [C-AR49]; check A's SaaS Capital 2023 90% | Partly: SaaS Capital 2023 and 2025 are the same survey series | SaaS Capital excludes firms under $1M ARR, which raises its figure. Benchmarkit's own bands are not monotonic (90% under $1k, 85% at $1-10k), so small samples per band matter |
| **80% under $5k ACV vs 85% at $1-5k** | Aleph × Benchmarkit 2026 (2025 data) [C-AR45]; Benchmarkit 2025 (2024 data) [C-AR42] | Yes, the same survey series a year apart | Not two findings. The 2026 page says GRR fell market-wide by 4 points, which explains most of the gap |
| **80% gross margin** | Benchmarkit 2026 software margin [C-AR44]; OpenView $1-5M ARR [C-AR46]; Benchmarkit 2025 subscription 81% [C-AR43] | Partly (Benchmarkit twice) | All self-reported. Real SMB firms with payments or hardware run 72-84% [C-AR48, C-AR49] |
| **$7,500** | Drata SOC 2 framework, Secureframe platform and framework, Sprinto starter platform, Vanta "AWS FTR Module" [C-AR13-C-AR16]; Vendr's lowest Vanta deal [C-AR19] | No | A common price point on the same marketplace, not evidence that SOC 2 "costs $7,500" |
| **SOC 2 audit ranges** | Secureframe ($5-20k / $7-150k) [C-AR17]; check AA's Scrut.io ($30-80k); a referral directory ($7-30k) | Likely cross-copying among vendor blogs; none names a firm or sample | Treat as one vendor-sourced range, not three |
| **Support 4% vs 10% of revenue** | TSIA (half under 3.8% of revenue) [C-AR05]; SaaS Capital (support plus success 10% of ARR) [C-AR06] | No | Different definitions: TSIA counts support COGS only; SaaS Capital adds customer success. Not a conflict |
| **$800 vs $8,764 for CzarLite** | SMC3 2022 module price [C-AR26]; FEMA's yearly web-access subscription [C-AR21] | Same seller, different items | The $800 is one data module; FEMA bought access to RateWare plus CzarLite. Do not treat $800 as the licence price |
| **"3,000" vs "5,000" SMC3 customers** | SMC3 website terms; SMC3 partner datasheet [C-AR37] | Same company | Different dates and definitions (customers vs "rely on"); neither is used in any number |
| **"Licence per shipper"** | IBM [C-AR27], Supply Chain Cloud [C-AR28], Oracle [C-AR29] | Possibly: all integrate the same SMC3 web service, which takes a customer licence key | Three vendors following one SMC3 integration pattern, not three independent rules. SMC3's LSP and audit offers [C-AR30, C-AR31] show the other pattern exists |
| **Table "accuracy" 94-98%** | Invoice extractor 94% of fields [C-AR61]; PubTables cell scores ≈0.98 vs 69-95% whole-table exact [C-AR56]; check AJ's vendor 98% (Trax) | No | Field-level and cell-level scores look high while whole-document or whole-table correctness is much lower. Always ask which unit a percentage counts |
