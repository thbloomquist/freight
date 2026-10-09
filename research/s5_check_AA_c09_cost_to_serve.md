# S5 check AA: what it really costs to serve one C-09 customer

- **What this is:** new desk research for S5 in run 01. It replaces the unsourced cost-to-serve guesses in check X's per-customer model (`s5_check_X_c09_money.md` §6.4 and §10) with sourced ranges where the web allows, for two ways of running the service:
  - **(a) AI/software-heavy:** machines read and rate every invoice; people look only at exceptions and file disputes;
  - **(b) human-heavy:** people audit every invoice by hand against the rate agreement, as a classic contingency audit firm does.

  It answers AA1-AA7 from the brief, gives a replacement input table (§9), and re-runs the model (§10).
- **Scope:** C-09 as named on 2026-09-17: truckload (TL) and less-than-truckload (LTL) bills of US manufacturers and distributors with 20-499 staff; the likely first product is an audit-only look-back paid as a share of recoveries (contingency). Overcharge rates, claim windows, pricing shares and spend bands are **not** redone; they are in checks X and T.
- **Date:** 2026-09-17. All new sources were accessed on 2026-09-17.
- **Status:** input to S5. **It decides nothing.** Model inputs chosen by us are labelled **[our call]**. The coordinator and the founders decide.
- **Labels:**
  - *verified*: read at the source (an official data release or API, a filing, a statute, a paper, or a vendor's own pricing page for "the stated price").
  - *assumed*: a search snippet, a vendor performance claim (even when read in full), a secondary summary, an aggregator's figure, a blog, or memory.
  - **[our calc]**: our arithmetic. **[our call]**: our judgement.
- **New sources** are N-AA01 to N-AA70 (§13). Earlier IDs keep their meaning (N-X02, N-X12, N-X13, N-X14, N-X16, N-X17, N-X24, N-X26, N-X27, N-X29, N-X30, N-X45, N-K22, N-R14).
- **Search use:** about 65 web searches of the 120 allowed, plus direct fetches and three public data APIs (BLS, Azure retail prices, AWS price list). No request carried any personal identity.

**Words used here:**
- **Document AI / OCR:** cloud services that turn a scanned or PDF page into text (OCR, optical character recognition) or into named fields such as invoice number, total and line items.
- **LLM (large language model):** a model such as Claude, Gemini or GPT that reads text or page images and can extract fields, compare them with a rate agreement and draft a dispute. It is billed per **token**, a chunk of text of roughly 4 characters; a page image also costs tokens.
- **Batch API:** a slower, asynchronous way to call an LLM at half price. **Prompt caching:** re-using a long, repeated prompt (for example a rate agreement) at a tenth of the input price.
- **Invoice packet:** the carrier's freight bill (1-3 pages) plus the BOL (bill of lading, the shipping document signed at pickup) and the POD (proof of delivery, the signed delivery receipt).
- **Exception:** an invoice a person must look at because the machine could not read it confidently, or because it does not match the rate agreement or shipment facts. **Straight-through / touchless:** processed with no human touch. **Dispute:** an exception that becomes a claim or short-payment sent to the carrier.
- **Loaded wage:** the wage plus the employer's other costs (benefits, payroll taxes, leave). **BPO:** business-process outsourcing, often offshore (India, the Philippines).
- **SOC 2:** an outside audit of a software company's security controls that buyers often ask for. It is a **company-level** cost, not a per-customer one.
- **CSM:** customer success manager, the person who looks after existing accounts. **ARR:** annual recurring revenue.
- **Cost of revenue (COR)** and **gross margin** = (revenue − COR) ÷ revenue, as in check X. **Gross profit per customer** = fee minus the direct cost to serve that customer; it excludes sales, marketing and company overhead.

---

## 1. Summary

| Q | Headline | Best evidence | Label |
|---|---|---|---|
| **AA1** Reading one invoice | **Machine reading costs cents, not the $0.50 guessed.** List prices: AWS Textract expense extraction **$0.01 a page**, plain OCR **$0.0015**; Azure prebuilt invoice model **$10 per 1,000 pages**, OCR **$1.50**; Veryfi **$0.16 per invoice**. An LLM reading a 3-5 page packet costs about **$0.001** (Gemini 2.5 Flash-Lite) to **$0.07** (Claude Sonnet 5) to **$0.24** (Claude Opus 5). The best multimodal LLMs extract **92.7-96.5% of invoice fields** correctly (academic benchmark), so checks and human review still matter. General AP teams touch **51-77%** of invoices by hand and see exceptions on **9-22%** | N-AA02, N-AA03, N-AA11, N-AA12-N-AA17, N-AA18, N-X16 | prices *verified* (stated); token costs **[our calc]**; accuracy *verified* |
| **AA2** Adjacent prices | **No public contract or award states a per-invoice freight-audit fee** (five searches). Proxies: the Defense Finance and Accounting Service (DFAS) spent **$18-24 per transportation bill paid** (FY2001-02); offshore AP outsourcing is quoted at **$0.50-2.00 per invoice** against **$3-8** onshore; AP software runs **$0-89 per user a month** plus **$0.59 per ACH payment** (BILL); Stampli about **$0.67-2.50 per invoice** at 500-1,000 invoices a month; parcel audit **35% of refunds** (LateShipment) | N-AA26, N-AA27, N-AA22, N-AA25, N-AA29 | DFAS inputs *verified*, ratio **[our calc]**; BPO and Stampli *assumed*; BILL and LateShipment *verified* (stated) |
| **AA3** Human time and wages | **Every figure for minutes per freight invoice comes from a vendor, and all fall at 8-13 minutes** for a manual audit. **No figure for minutes per overcharge dispute was found**; loss-and-damage claims run 40-60 per processor a month. BLS May 2025: bookkeeping, accounting and auditing clerks average **$25.75 an hour**, logisticians **$43.14**; wages are **70.0%** of private employers' compensation cost, so loaded rates are about **$37** and **$62** an hour. Offshore back-office is quoted at **$6-16 an hour** | N-AA31, N-AA32, N-AA35, N-AA36, N-AA39, N-AA40, N-AA27, N-AA28 | minutes *assumed*; wages *verified*; loaded **[our calc]**; offshore *assumed* |
| **AA4** Share needing a human or disputed | **No neutral freight dispute rate exists.** The best non-vendor figure: an SJ Consulting survey of shippers, 3PLs and audit firms (over $8B of LTL charges) found carriers' LTL **billing accuracy of 94-99%, 97% on average**, so about **3%** of LTL bills are wrong. Vendor figures run from **3.8%** (Laneproof) to "more than 15%" (MyCarrier, no source) | N-AA43, N-X27, N-AA33 | *assumed* (survey read through a broker's blog) |
| **AA5** Fixed and onboarding | **Hours to load a shipper's rate agreements: not found.** Vendors state implementations of **4-6** and **4-12 weeks** (elapsed, not effort). AP software implementation is charged at about **$2,000** (Stampli) to **$5,000-50,000** (AvidXchange). SMB customer-success managers look after a median **100-250 accounts** (2016). Company-level: SOC 2 about **$20-50k a year** after year one; LTL freight-class data by API **$2,967-9,809 a year** (NMFTA) | N-AA47, N-AA48, N-AA49, N-AA24, N-AA50, N-AA51 | ClassIT+ *verified* (stated); rest *assumed* |
| **AA6** Gross margins | Human-heavy recovery audit: **PRGX 35% (2009), 39% (2018), 41% (2019), 45.5% (first nine months of 2020)**. Outsourcers Genpact **35-36%**, EXL **37-38%**. AP software AvidXchange **60-72%**, BILL **84-86%**. AI-native products **45% (2025) → 53% (2026, projected)** (ICONIQ, ~300 executives); Bessemer's fast-growing AI startups **~25% and ~60%**. Vertical SaaS **~65%** against horizontal **~75%** | N-X13, N-X12, N-AA56, N-AA57, N-AA58-N-AA61, N-AA55, N-AA54, N-AA53 | PRGX, ICONIQ, BVP, Euclid *verified*; aggregator margins *assumed* |
| **AA7** Scale | List prices fall **20-60%** above 1M pages a month (Textract, Azure); LLM batch calls cost **50%** less. Ardent's best-in-class AP teams process an invoice for **$2.78 against $12.88** (−78%). PRGX's cost of revenue fell from **62.6% to 54.5%** of revenue (nine months 2019 → 2020) with "improved productivity" | N-AA02, N-AA03, N-AA12, N-X16, N-AA57 | *verified* |

**The model in one line (§10, [our calc] on sourced and [our call] inputs):** with a 25% fee and check X's central rates (1.5% overcharged × 70% caught × 80% credited):
- **AI-heavy, central costs** ($0.65 per invoice, $9.30 per dispute, 5% disputed, $400 fixed a year, 1.5 invoices per $1,000 of spend): break-even at **$0.94M** of TL+LTL spend (check X had $0.68M). The overcharge rate needed to cover variable cost rises from 0.87% to **1.19%**.
- **The same with offshore exception reviewers:** break-even at **$0.28M**; variable cost is covered above **0.46%**.
- **Human-heavy, every invoice audited by a US clerk** (10 minutes): **no spend level breaks even at any of check X's rate sets.** Covering variable cost needs an overcharge rate of about **8%**. With offshore auditors it needs **2.6%**.
- **What drives it:** the share of invoices a person touches × minutes × wage, and **how many invoices a dollar of spend creates** (an LTL-heavy shipper has about twice as many). The unsourced $600 fixed cost is no longer the deciding input.

---

## 2. AA1 · Reading and extracting one freight invoice

### 2.1 Document-AI list prices

| Service | Stated price | Tiers / notes | Source | Label |
|---|---|---|---|---|
| **AWS Textract, US East** | DetectDocumentText (OCR) **$0.0015/page**; AnalyzeExpense (invoices and receipts) **$0.01/page**; Layout $0.004; Tables $0.015; Forms $0.05; Forms+Queries+Tables $0.07 | Above 1M pages a month: OCR $0.0006 (−60%), Expense $0.008 (−20%), Forms+Queries+Tables $0.055 | AWS public price-list file for us-east-1 (N-AA02); the pricing page shows the same numbers for US West (N-AA01) | *verified* (stated) |
| **Azure Document Intelligence, East US** | Read (OCR) **$1.50 per 1,000 pages**; prebuilt models (invoice, receipt) **$10**; layout $10; custom extraction and custom generative **$30**; add-on fields $6; classifier $3 | Read $0.60 above 1M pages. Prebuilt commitment tiers: 20K pages $190/month ($9.50/1K), 100K $900, 500K $4,000, 1M $7,500 ($7.50/1K); "connected" (self-hosted container) meters 10-20% lower | Azure Retail Prices API (N-AA03). The pricing web page renders no numbers (N-AA04) | *verified* (stated) |
| **Google Document AI** | Invoice Parser "**$0.10 per 10 pages**", billed in 10-page blocks per document; Form Parser and Custom Extractor **$30 per 1,000 pages** (up to 1M) | Custom processors add hosting at $0.05/hour (snippet) | Secondary guide dated June 2026 (N-AA06) and search summary (N-AA07). Google's page returned truncated (N-AA05) | *assumed* |
| **Veryfi** | Free up to 100 documents/month; Starter "$500+/mo" minimum for 5,000 docs; "**$0.16 per invoice**", $0.08 per receipt | "Commit to 12 months and get 1 cent discount for every document"; better rates above 10,000/month | N-AA11 | *verified* (stated) |
| **Mindee** | Starter $44/month ($529/year), Pro $116/month; "1 processed page = 1 credit"; overage at the plan unit rate +20% | The extraction gave 6,000 credits for both plans and "≈ 0.044 each", which do not reconcile: **$0.007-0.044 per page** | N-AA08 | *verified* (stated), **figures inconsistent** |
| **Nanonets** | "$0.02 / run" simple, "$0.10 / run" standard AI, "$0.30 / run" complex AI; "A typical invoice processing workflow runs 4–6 blocks per document" | → **$0.08-1.80 per invoice** **[our calc]**; "Up to 40% volume discount" | N-AA10 | *verified* (stated) |
| **Rossum** | Starter "Starting at $18,000 per year"; higher plans by quote | Minimum one-year contract | N-AA09 | *verified* (stated) |
| **Human review add-on (AWS Augmented AI)** | Platform fee **$0.03 per page reviewed** (first 100,000), then $0.02; Mechanical Turk example "$0.012 per page" per reviewer | The platform fee is on top of the reviewer's pay | N-AA65 | *verified* (stated) |
| **Storage (AWS S3 Standard)** | **$0.023 per GB-month** (first 50 TB) | A 1 MB packet kept 7 years costs about **$0.002** **[our calc]** | N-AA66 | *verified* (stated) |

### 2.2 LLM list prices (per million tokens, input / output)

| Model | Standard | Batch | Source | Label |
|---|---|---|---|---|
| Claude Haiku 4.5 | $1 / $5 | $0.50 / $2.50 | N-AA12 | *verified* (stated) |
| Claude Sonnet 5 | $2 / $10 ("now the standard price") | $1 / $5 | N-AA12 | *verified* |
| Claude Opus 5 | $5 / $25 | $2.50 / $12.50 | N-AA12 | *verified* |
| Claude cache hits | 0.1× the input price | — | N-AA12 | *verified* |
| Gemini 2.5 Flash-Lite | $0.10 / $0.40 | $0.05 / $0.20 | N-AA15 | *verified* |
| Gemini 2.5 Flash | $0.30 / $2.50 | $0.15 / $1.25 | N-AA15 | *verified* |
| Gemini 3.8 Flash | $0.75 / $3.75 to 2026-12-31, then $1.50 / $7.50 | half | N-AA15 | *verified* |
| Gemini 3.1 Pro Preview | $2 / $12 (prompts ≤200k) | $1 / $6 | N-AA15 | *verified* |
| OpenAI gpt-5-nano / gpt-5-mini | $0.05 / $0.40; $0.25 / $2.00 | half | N-AA17 | *verified* |
| OpenAI gpt-5.4-mini / gpt-5.5 | $0.75 / $4.50; $5 / $30 | half | N-AA17 | *verified* |

**How pages turn into tokens:**
- **Claude:** "Each page typically uses 1,500–3,000 tokens per page depending on content density", plus image tokens, "Because each page is converted into an image" (N-AA13). An image costs ⌈width/28⌉ × ⌈height/28⌉ tokens, capped at 1,568 on standard-tier models and 4,784 on Claude 4.7 and later (N-AA14). A letter page at 150 dpi (1275 × 1650 px) is about **2,700 image tokens** on the newer models and is capped at **1,568** on Haiku 4.5 **[our calc]**.
- **Gemini:** "Each document page is equivalent to 258 tokens" (N-AA16).
- **OpenAI:** image token rules were not read, so the OpenAI rows below assume OCR text first (Azure Read) at about 1,500 tokens a page **[our call]**.

### 2.3 Cost of reading one invoice packet with an LLM [our calc]

**Assumptions [our call]:**
- **Lean:** 3 pages, a 3,000-token prompt, 800 output tokens.
- **Typical:** 4 pages, a 6,000-token prompt (instructions plus the relevant rate-agreement lines), 1,500 output tokens (fields plus an audit note).
- **Heavy:** 5 pages, 10,000-token prompt, 2,000 output tokens.
- Claude tokens per page: Haiku 4.5 3,000 / 3,750 / 4,500; Sonnet 5 and Opus 5 4,200 / 5,000 / 5,700. No caching is assumed, which overstates repeat prompts.

| Route | Lean | Typical | Heavy |
|---|---|---|---|
| Gemini 2.5 Flash-Lite, batch | $0.0003 | $0.0007 | $0.0010 |
| Gemini 2.5 Flash-Lite | $0.0007 | $0.0013 | $0.0019 |
| Gemini 2.5 Flash | $0.0031 | $0.0059 | $0.0084 |
| Gemini 3.1 Pro Preview | $0.017 | $0.032 | $0.047 |
| Claude Haiku 4.5, batch | $0.008 | $0.014 | $0.021 |
| Claude Haiku 4.5 | $0.016 | $0.029 | $0.043 |
| **Claude Sonnet 5** | $0.039 | **$0.067** | $0.097 |
| Claude Opus 5 | $0.098 | $0.168 | $0.243 |
| Azure Read OCR + gpt-5-mini | $0.008 | $0.012 | $0.016 |
| Azure Read OCR + gpt-5.4-mini | $0.014 | $0.022 | $0.030 |
| *Document AI for comparison:* Textract AnalyzeExpense, 3-5 pages | $0.03 | $0.04 | $0.05 |
| *Azure prebuilt invoice, 3-5 pages* | $0.03 | $0.04 | $0.05 |
| *Veryfi, invoice only* | $0.16 | $0.16 | $0.16 |

**Reading [our call]:** at list prices, the machine part of reading, rating and matching one packet costs **$0.001-0.25**, and about **$0.05-0.10** on a mid-priced model with a second checking pass. Check X's $0.50 was high for the machine part and silent on the human part, which §4-§5 show is the larger cost.

### 2.4 Accuracy, straight-through and exception rates

| Source | Figure | Label |
|---|---|---|
| **Berghaus et al., "Multi-Modal Vision vs. Text-Based Parsing: Benchmarking LLM Strategies for Invoice Processing"** (Fraunhofer IAIS / Lamarr Institute, arXiv 2509.04469, 2025-08-29; N-AA18). Eight models, three public datasets, zero-shot, field-level accuracy | Best (Gemini 2.5 Pro, page image): **clean invoices 96.50%, scanned invoices 92.71%**, scanned receipts 87.46%. Gemini 2.5 Flash-Lite: 95.70% / 91.64% / 85.34%. GPT-5 nano: 86.45% / 80.61% / 58.08%. Reading the image beat converting to text first | *verified* (results table via the HTML version) |
| Same, applied [our calc] | If field errors were independent, an invoice with 20 fields at 92.7-96.5% field accuracy would have at least one wrong field **51-78%** of the time. Errors cluster and cross-checks (totals, PRO match, EDI data) catch many, so this is an upper bound on raw extraction exceptions, not an exception rate | **[our calc]**; independence is **[our call]** |
| **Ardent Partners, AP Metrics that Matter in 2025** (N-X16, re-read pp. 25-28) | Invoice exception rate: **best-in-class 9.0%, all others 22.0%** (14% overall). Touchless: **49.2% vs 23.4%** (32.6% overall). Cost per invoice: **$2.78 vs $12.88**. Only **5%** of AP teams have fully automated exception management; 60% "somewhat" | *verified* (survey; general AP, not freight) |
| IOFM benchmark (search summary; page not identified) | "Industry invoice exception rates average 5%", up to 20%; top AP departments 6,900 invoices per FTE a year against 4,200 on average | *assumed* (snippet) |
| **Vendor claims** | Loop: "Approve 99% of invoices with no touch" (N-AA63). Hypatos: production straight-through of 85-92% against 60-70% for traditional document capture (N-AA68). Payouts.com: 85-95% touchless for PO-backed goods, 20-40% for one-off vendors (N-AA64) | *assumed* (vendor) |

**Reading [our call]:** a person will look at somewhere between **under 5%** (vendor best case) and **over 30%** (general AP average touches) of invoice packets. Nothing public measures this for SMB freight packets with scanned BOLs and handwritten PODs. §9 uses **5 / 15 / 30%**.

---

## 3. AA2 · Per-invoice prices in adjacent markets

### 3.1 AP automation software

| Product | Stated or reported price | Implied per invoice | Source | Label |
|---|---|---|---|---|
| **BILL** | Essentials $49, Team $65, Corporate $89 per user per month; ACH $0.59, check $1.99, card 2.9% | Per payment, not per invoice read | N-AA22 | *verified* (stated) |
| **Ramp** | Free $0; Plus $15/user/month plus a platform fee; "Automated invoice extraction (OCR)" on both; no per-bill fee listed | $0 on the free plan | N-AA23 | *verified* (stated) |
| **Tipalti** | AP "Plans starting at $99/month" plus "Transaction pricing per invoice and payments" (no number); "Standard implementations are included" | Not stated | N-AA20 | *verified* (stated) |
| **Stampli** | No public price; "deploy in weeks". Reported: "mid-market deals at 500–1,000 invoices a month land between $8,000 and $15,000 a year" (attributed to Vendr); "~$2,000 typical" implementation | **$0.67-2.50** **[our calc]** | N-AA21 (verified text); N-AA25, N-AA24 | price *assumed* |
| **AvidXchange** | Reported "~$440/mo"; implementation "$5,000–$50,000" (another summary: $4,000-40,000) | Not derivable | N-AA24, N-AA25 | *assumed* |
| Ken (small AP tool) | $29/month for 50 invoices, $100 for 500, $250 unlimited | $0.20-0.58 **[our calc]** | N-AA24 (the vendor's own blog) | *verified* (stated) |
| Goldman Sachs estimate, via AvidXchange search summary | Manual processing $16.00 (medium) and $22.26 (small business) per invoice; automated $5.89 and $6.89 | — | N-AA25 | *assumed* |

### 3.2 Freight-audit fees per invoice in public contracts

| What | Figure | Source | Label |
|---|---|---|---|
| Public contract, RFP award, bid tabulation, GSA schedule price list or university award with a per-invoice freight-audit fee | **Not found** (five searches; §14). Cass received a GSA schedule contract in October 2024, but its release gives no contract number or prices | N-AA70 | — |
| GSA post-payment data-capture fee, 1989 (known) | $0.28 per motor-freight bill plus a commission | N-X02 | *verified* |
| Cass processing fees per item, 2024 (known) | $1.56 (includes payment) | N-X14 | **[our calc]** |
| **DFAS, the Defense Department's payment agency** (FY2003 budget justification) | "Transportation Bills Paid": cost **$19.5M** (FY2001) and **$14.4M** (FY2002) on **0.8M** bills a year = **$24.40 and $18.00 per bill**. Commercial payments: $15.73 and $17.51 per payment. Nominal dollars; the work shifted into commercial payments in FY2003 | N-AA26 | inputs *verified*; per bill **[our calc]** |
| Vendors on per-invoice pricing | "Vendors rarely publish numbers, because the real answer depends on invoice volume, mode mix, and how much of the work the software does versus offshore labor" (Navix, 2026) | Navix pricing guide (N-X35, known) | *assumed* |

### 3.3 Offshore and BPO rates

| Source | Per invoice | Per hour | Label |
|---|---|---|---|
| **Global BPO Index**, AP outsourcing buyer's guide (2026-07-07; N-AA27) | Offshore (India, Philippines) "**$0.50 to $2.00**"; nearshore "$1.25 to $3.50"; onshore US "**$3.00 to $8.00+**" | Offshore "**$6 to $16**"; nearshore "$12 to $22"; onshore "$28 to $50+" | *assumed* (guide; no method) |
| **HiveDesk**, BPO pricing guide (2026-03-23; N-AA28) | — | Back office: Philippines "**$9-15/hr**", India "**$8-14/hr**", USA "$35-60/hr" | *assumed* |
| nVision Global (known) | — | "400+ full time employees outside of the United States" | N-X45, *assumed* |

These are prices billed by outsourcers, so they already include the vendor's margin **[our call]**.

### 3.4 Parcel audit

| Product | Stated price | Source | Label |
|---|---|---|---|
| **LateShipment.com OneAudit** | "**35% of refunds recovered**" | N-AA29 | *verified* (stated) |
| 71lbs | "No upfront costs", "We only get paid when you save"; no % shown | N-AA30 | *verified* (no number) |
| Parcel Refund Services; RefundPros (known) | 50/50; % not stated | check X §5.1 | *verified* |
| Freightview (TL/LTL booking, some audit) (known) | $149/month for 0-50 shipments | N-X29 | *verified* |
| **Per-shipment parcel-audit subscription prices** | **Not found** | — | — |

---

## 4. AA3 · Human time per step, and wages

### 4.1 Minutes to audit one TL or LTL invoice by hand

| Source | Statement | Minutes per invoice | Label |
|---|---|---|---|
| **Intelligent Audit** (2022-04-18; N-AA31) | Example: "10 minutes" an invoice, "48" a day, "$20" an hour | **10** | *assumed* (vendor example) |
| **Navix** LTL page (2025-12-31, updated 2026-09-15; N-AA32) | "A broker processing 500 LTL shipments per week at ~4 charge lines each is validating 2,000 individual charges — 67-100 hours of labor weekly"; "A single LTL bill can carry 8–12 charge lines" | **8-12** **[our calc]** (2-3 minutes per charge line) | *assumed* (vendor) |
| **US Tech Automations** (2026-06-14; N-AA35) | "average of 12 minutes per invoice"; staff hours per 100 invoices "18–22" manual, "3–5" automated; credited to an "American Shipper 2024 Freight Audit & Payment Benchmark Study" that we could not trace | **11-13** manual, **2-3** automated **[our calc]** | *assumed*; **orphan attribution** |
| Intelligent Audit (2026-07-14; N-AA34) | "Your logistics team spends an average of 15 to 20 hours each week manually reconciling freight invoices" (no volume given) | — | *assumed* (vendor) |
| **MyCarrier** (2024-10-10; N-AA33) | "freight accountants spend an average of 3.4 hours per week auditing freight bills, costing about $77 per 50 shipments" (no volume, no source) | $1.54 per shipment **[our calc]** | *assumed* |
| Parseur (2026-09-08; N-AA19) | General AP: "10 to 30 minutes of manual data entry" per invoice | 10-30 | *assumed* |
| IOFM snippet (general AP, all steps) | 6,900 invoices per FTE a year (top) and 4,200 (average) | **16-26** all-in, at 1,800 working hours **[our calc]** | *assumed* |
| **Time studies, APQC freight figures, job postings stating volumes, audit-firm staffing ratios** | **Not found** (APQC pages 403; §14) | — | — |

### 4.2 Minutes per dispute or claim

| Source | Statement | Label |
|---|---|---|
| **Overcharge disputes (short-pay, re-rate claim)** | **No time or cost figure found** (§14) | — |
| CorePiper, State of Freight Claims 2026 (2026-04-27; N-AA36) | **Loss and damage** claims only: "A single claims processor can handle 40–60 manual claims per month"; shippers often skip claims "under $200–$500 because the documentation and follow-up time cost more than the expected recovery" | *assumed* (vendor synthesis) |
| Same [our calc] | At about 150 working hours a month **[our call]**: **2.5-3.75 hours per damage claim**. Damage claims need 15-20 documents; an overcharge dispute needs the bill, the rate agreement and the BOL, so this is an upper bound **[our call]** | **[our calc]** |
| Warp (2026-03-01; N-AA37) | Damage claims: "Industry estimates put the internal processing cost at $200 to 400 per claim, regardless of outcome" | *assumed* |
| Laneproof (2026-04-18; N-AA38) | Suggests a "48 business hours" resolution window (elapsed, not effort); overcharges "between $85 and $300 per affected load" | *assumed* (vendor) |
| US Tech Automations (N-AA35) | Dispute resolution "22–35 days" manual, "8–14 days" automated (elapsed) | *assumed*; orphan attribution |

### 4.3 Wages

| Occupation / source | Figure | Label |
|---|---|---|
| **BLS OEWS May 2025, 43-3031 Bookkeeping, accounting and auditing clerks** (1,373,680 employed; N-AA39) | Mean **$25.75/hour**; 10th $17.31, 25th $20.92, median $24.36, 75th $29.55, 90th $35.84 | *verified* (BLS API) |
| **BLS OEWS May 2025, 43-3021 Billing and posting clerks** (404,060) | Mean **$24.55**; 10th $17.93, 25th $20.60, median $23.32, 75th $28.02, 90th $32.55 | *verified* |
| **BLS OEWS May 2025, 13-1081 Logisticians** (251,040) | Mean **$43.14**; median $39.58 | *verified* |
| **BLS Employer Costs for Employee Compensation, Q2 2026, private industry** (N-AA40) | Total compensation **$46.89/hour**; wages and salaries **$32.82**; wages = **70.0%** of compensation | *verified* (BLS API) |
| Glassdoor, via search summary (N-AA41) | "Freight Audit Specialist" average $55,879 a year (25th-75th $44,976-69,954); "Freight Audit Analyst" $72,388 ($35/hour; $56,853-93,087) | *assumed* (snippet) |
| ZipRecruiter, via search summary (N-AA41) | Freight audit jobs "$17-$28/hr" (September 2026) | *assumed* |
| Amazon freight audit payment analyst posting, Bellevue WA (N-AA42) | $82,700-139,100 a year; the role includes building "auditing automation strategies" | *verified* (one posting; a high anchor) |
| Offshore back office (§3.3) | $6-16 (Global BPO Index); $8-15 (HiveDesk) billed per hour | *assumed* |

### 4.4 Loaded hourly rates used in §9 [our calc]

| Rate | Build | $/hour |
|---|---|---|
| **Offshore reviewer** | Middle of the billed offshore ranges (§3.3) **[our call]** | **$12.00** |
| **US clerk, loaded** | $25.75 ÷ 0.700 | **$36.79** |
| Blend for account work | average of the US clerk and the logistician | $49.21 |
| **US freight analyst, loaded** | 13-1081 mean $43.14 ÷ 0.700 | **$61.63** |

The Glassdoor averages ($26.9 and $34.8 an hour **[our calc]**) sit inside this range. One caution: the 70.0% wage share is for all private workers; the office-occupation figure was not confirmed (§14).

---

## 5. AA4 · The share of freight invoices that need a human, or get disputed

| Source | Figure | What it measures | Label |
|---|---|---|---|
| **SJ Consulting survey**, reported by a broker's "LTL 101" page (about 2016; N-AA43) | "range of billing accuracy was 94 to 99 percent depending on the carrier, with the average being 97 percent". Respondents: "several large LTL shippers, 3PLs, and freight audit and pay firms" with LTL charges over $8B, 22% of industry revenue. About 50% of bills of lading had weight or description errors | Share of **LTL bills** that are wrong: **1-6%, 3% average** | *assumed* (read through a secondary page; the original was not found) |
| Laneproof (known, N-X27; and N-AA38) | 3.8% of carrier invoices with a billing variance; "Between 3% and 5% of those accessorial line items are overbilled" (12,000+ invoices) | Broker-side invoices | *assumed* (vendor) |
| Tompkins (known, N-X24) | "5 to 10 percent of freight and parcel invoices carry some kind of error" | Invoices | *assumed* |
| MyCarrier (N-AA33) | "the average freight bill error rate in the industry is more than 15%"; "1 in 4 freight bills carry unplanned accessorial charges" | No source given | *assumed* |
| iTech Data (undated; N-AA44) | "Only 17% of freight invoices are accurate" | No source given | *assumed*, unusable |
| LogiSYM (2021; N-AA44) | "as much as 20% freight invoices may be inaccurate", from an unnamed 2021 survey | No source | *assumed*, unusable |
| General AP (§2.4) | Exceptions 9.0-22.0% (Ardent); 5% (IOFM snippet) | All invoice types | *verified* / *assumed* |

**Reading [our call]:**
- **Exceptions and disputes are different numbers.** An exception is any packet a person looks at (unreadable page, missing POD, a variance under tolerance). A dispute is the subset worth claiming. The model keeps them apart: 5 / 15 / 30% of packets looked at, and **3 / 5 / 10%** disputed, tied to check X's low / central / high rate sets.
- **Consistency check [our calc]:** at 1.5 invoices per $1,000, these shares imply an average caught overcharge per dispute of **$56 (low), $140 (central) and $170 (high)**. Laneproof's variances ($85-300, average $127) and Eller's class errors (average $145, N-X26) sit in that band, so the central pair is internally consistent.
- The one non-vendor figure (about 3% of LTL bills wrong) fits the low-to-central dispute share.

---

## 6. AA5 · Fixed and onboarding cost per customer

### 6.1 Implementation times and fees stated or reported

| Vendor / type | Statement | Label |
|---|---|---|
| FreightOptics, freight audit and payment (N-AA48) | "Implementation typically takes 4 to 6 weeks, depending on carrier and system access" | *verified* that the vendor says it |
| Supply Chain Desk, freight-audit software guide (2026-08-22; N-AA49) | "4-12 weeks"; "$1M annually" of freight spend as the target minimum for ROI; Cass "Pricing is not published" | *assumed* |
| Stampli (N-AA21) | "deploy in weeks"; ~$2,000 typical implementation (N-AA24) | *verified* / *assumed* |
| Tipalti (N-AA20; N-AA24) | "Standard implementations are included"; buyers report $5,000-15,000 in year one | *verified* / *assumed* |
| AvidXchange (N-AA24, N-AA25) | $5,000-50,000 (or $4,000-40,000) one-off | *assumed* |
| Vic.ai (N-AA24) | $5,000-10,000 | *assumed* |
| **Hours to load one shipper's rate agreements, fuel tables and accessorial schedules** | **Not found** (implementation guides describe the artefacts, not the hours; rate-loading outsourcers do not publish prices) | — |

Implementation fees are what vendors **charge**, usually to larger customers, so they bound cost only loosely **[our call]**.

### 6.2 Account management

| Source | Figure | Label |
|---|---|---|
| **Gainsight**, from its Chief Customer Officer Summit (2016-03-17; N-AA50) | "The median amount of customers an SMB CSM manages is between 100-250", with $1-2M of ARR; mid-market also 100-250 ($2-5M); enterprise 10-50. Customer success under 20% of ARR is "within industry benchmarks" below $10M ARR | *verified* that Gainsight says it; old |
| **SaaS Capital**, 2026 spending benchmarks (1,000+ private B2B SaaS firms, March 2026; N-AA52) | Customer support plus customer success: median **9% of ARR**. Cost-of-revenue pieces: hosting 5%, DevOps 4%, professional-services COGS 5%, other 3% of ARR | *verified* (survey) |
| [our calc] | 100-250 accounts at about 1,800 working hours a year = **7-18 hours per account** | **[our calc]** |

### 6.3 Company-level costs (not in gross profit, shown per customer for scale)

| Item | Figure | Source | Label |
|---|---|---|---|
| SOC 2 Type 2 audit | $30,000-80,000; recurring "$20,000 to $50,000 per year without automation"; compliance platform "$10,000 to $30,000 annually"; first year with automation $50,000-110,000 (50-100-person SaaS) | Scrut.io (2026-08-05; N-AA51), a compliance vendor | *assumed* |
| **NMFTA ClassIT+ (LTL freight classes) by API** | Shippers $2,967-7,418 (members) / $3,412-8,530 (non-members) a year; 3PLs and 4PLs $3,412-9,809; web app $156-371 per seat a year | N-AA47 | *verified* (stated) |
| SMC3 CzarLite (LTL base rates) | Price not public | — | not found |
| [our calc] | SOC 2 recurring + platform + class data ≈ **$34k-84k a year** → **$340-840 per customer** at 100 customers, $113-280 at 300, $34-84 at 1,000 | **[our calc]** | — |

---

## 7. AA6 · Gross-margin benchmarks

| Company / cohort | Gross margin | Years | Source | Label |
|---|---|---|---|---|
| **PRGX** (recovery audit, mostly large retailers) | **35%** | 2009 | N-X13 | *verified* |
| PRGX | **39.0%** (cost of revenue 61.0%) | 2018 | N-X12 | *verified* |
| PRGX | **41.0%** (cost of revenue $100.2M on $169.8M) | 2019 | N-AA56 | *verified* |
| PRGX | **45.5%** vs 37.4% (cost of revenue 54.5% vs 62.6%, nine months); "improved productivity and expanded operating leverage" | 9M 2020 vs 9M 2019 | N-AA57 | *verified* |
| Genpact (outsourcer, including finance and accounting) | 35.1% → 36.0% | 2022-2025 | stockanalysis.com (N-AA58) | *assumed* (aggregator) |
| ExlService | 36.5% → 38.4% | 2022-2025 | N-AA59 | *assumed* |
| Performant (healthcare recovery audit) | 29.7% → 18.3%, on the aggregator's gross-profit definition | 2021-2024 | N-AA62 | *assumed*; definition unclear |
| AvidXchange (AP software and payments) | 59.7% → 72.3% | 2021-2024 | N-AA61 | *assumed* |
| BILL (AP software and payments, revenue includes float interest) | 85.7% → 83.9% | FY2023-FY2026 | N-AA60 | *assumed* |
| **AI products at software companies** (ICONIQ State of AI 2026, ~300 executives, Q2 2026) | "Gross margins are improving, jumping from **45% in 2025 to a projected 53% in 2026**, and 59% in 2027"; "as products scale, talent's share of cost falls while inference rises" | 2025-2027 | N-AA55 | *verified* (survey) |
| Bessemer State of AI 2025 (2025-08-13) | "Supernovas" (fastest-growing AI startups) "~25% (often negative)"; "Shooting Stars" "60%" | 2025 | N-AA54 | *verified* |
| Vertical vs horizontal public software (Euclid, 36 vertical and 60 horizontal firms) | "roughly **65% vs. 75%** on average" | 2024-05 | N-AA53 | *verified* |
| Cass processing segment | Not separable into a gross margin (known; N-X14, N-D30) | — | — | — |
| Freight audit firms' margins | **Not found** (all private) | — | — | — |

**Reading [our call]:**
- **Human-heavy recovery audit sits at 35-45%, like other outsourcers (35-38%).** Software with payments sits at 60-86%.
- **AI inference is a new cost line** that pure SaaS did not carry. ICONIQ's AI products run 45-53%, and inference's share of their cost rises with scale.
- **An AI-heavy contingency audit lands anywhere from negative to over 80% in §10.** The overcharge rate and the human touch decide it, not the software.

---

## 8. AA7 · Scale effects

| Lever | Evidence | Size | Label |
|---|---|---|---|
| Document-AI volume tiers | Textract OCR $1.50 → $0.60 per 1,000 pages above 1M/month; AnalyzeExpense $10 → $8; Azure Read $1.50 → $0.60; Azure prebuilt commitment $9.50 (20K pages) → $7.50 (1M) per 1,000 | **−20% to −60%** at 1M pages a month | *verified* (N-AA02, N-AA03) |
| Vendor discounts | Nanonets "Up to 40% volume discount"; Veryfi one cent off per document for a 12-month commitment | −6% to −40% | *verified* (stated) |
| LLM batch and caching | Batch −50%; cache hits 0.1× input | up to −50% on reading | *verified* (N-AA12, N-AA15) |
| Automation in AP | Best-in-class $2.78 vs all others $12.88 per invoice; 3.1 vs 17.4 days | −78% | *verified* (N-X16) |
| Productivity in AP | 6,900 vs 4,200 invoices per FTE a year | +64% | *assumed* (IOFM snippet) |
| Offshore vs onshore | $0.50-2.00 vs $3.00-8.00 per invoice | 3-6× cheaper | *assumed* (N-AA27) |
| A recovery-audit firm | Cost of revenue 62.6% → 54.5% of revenue in a year | −8 points | *verified* (N-AA57) |
| Automated vs manual freight audit | 18-22 → 3-5 staff hours per 100 invoices | −75-85% | *assumed*; orphan (N-AA35) |
| **Our model** | Fixed cost per invoice: $400 ÷ 408 invoices = **$0.98** at $272k of spend, $0.09 at $2.9M | ~11× | **[our calc]** |

---

## 9. Replacement input table

Low / central / high are **cost** cases: "low" is the cheapest plausible service. Rows marked **[our call]** have no direct source and are anchored as stated.

### 9.1 (a) AI/software-heavy, with human review of exceptions

| Input | Low | **Central** | High | Build and anchors | Label |
|---|---|---|---|---|---|
| Machine reading, rating, matching per packet | $0.005 | **$0.10** | $0.50 | Gemini 2.5 Flash typical ($0.006); Claude Sonnet 5 typical ($0.067) plus a second check on about half; Opus 5 heavy × 2 ($0.49). Storage $0.002 | prices *verified*; **[our calc]** |
| Share of packets a person reviews | 5% | **15%** | 30% | Vendor best cases under 5%; Ardent exceptions 9% (best) to 22% (others); touchless only 23-49% in AP (§2.4) | **[our call]** |
| Minutes per review | 3 | **6** | 12 | Below the 8-13 minutes vendors give for a full manual audit (§4.1) | **[our call]** |
| Reviewer rate ($/hour, loaded) | $12 | **$36.79** | $61.63 | §4.4 | *verified* / **[our calc]** |
| **Per invoice, total** | **$0.035** | **$0.65** | **$4.20** | reading + share × minutes × rate | **[our calc]** |
| Minutes per dispute (prepare, file, follow up) | 5 | **15** | 45 | LLM drafts the claim; damage claims take 2.5-3.75 hours (upper bound) (§4.2) | **[our call]** |
| **Per dispute, total** | **$1.00** | **$9.30** | **$46.50** | minutes × rate + one LLM call | **[our calc]** |
| **Share of invoices disputed** | 3% | **5%** | 10% | SJ Consulting ~3% of LTL bills wrong; Laneproof 3.8%; Tompkins 5-10%. **Tied to the rate set** (low / central / high) | *assumed* inputs; **[our call]** |
| Account hours a year | 4 | **8** | 18 | SMB CSM 100-250 accounts → 7-18 hours; 4 for pooled tech-touch | *verified* ratio; **[our call]** |
| **Fixed per customer a year** | **$150** | **$400** | **$1,100** | hours × $36.79 / $49.21 / $61.63 | **[our calc]** |
| Onboarding hours | 3 | **8** | 24 | No hours found. Elapsed 4-12 weeks; implementation charged $0-2,000 at SMB AP tools | **[our call]** |
| **Onboarding, one-off** | **$110** | **$400** | **$1,500** | hours × rate | **[our calc]** |

### 9.2 (b) Human-heavy: every invoice audited by hand

| Input | Low | **Central** | High | Build and anchors | Label |
|---|---|---|---|---|---|
| Minutes per invoice | 5 | **10** | 15 | Vendors: 8-12 (Navix), 10 (Intelligent Audit), 11-13 (US Tech Automations) | *assumed* inputs; **[our call]** |
| Auditor rate ($/hour) | $12 (offshore) | **$36.79** | $61.63 | §4.4 | *verified* / *assumed* |
| **Per invoice** | **$1.00** | **$6.13** | **$15.40** | Cross-checks: offshore BPO $0.50-2.00; Ardent $9.40-12.88 (general AP); DFAS $18-24 per transportation bill (2001-02) | **[our calc]** |
| Minutes per dispute | 15 | **45** | 150 | Damage claims 150-225 minutes (upper bound) | **[our call]** |
| **Per dispute** | **$3.00** | **$27.60** | **$154** | minutes × rate | **[our calc]** |
| Share of invoices disputed | 3% | **5%** | 10% | as in (a) | **[our call]** |
| Account hours a year | 8 | **16** | 36 | twice (a): manual rate-agreement upkeep and reporting | **[our call]** |
| **Fixed per customer a year** | **$100** | **$800** | **$2,200** | low at the offshore rate; others as in (a) | **[our calc]** |
| Onboarding hours | 10 | **24** | 60 | manual loading of agreements | **[our call]** |
| **Onboarding, one-off** | **$120** | **$1,200** | **$3,700** | hours × rate | **[our calc]** |
| Cross-check: cost as a share of the fee | 54.5% | **59.0%** | 63.0% | PRGX cost of revenue, 2019-2020 (sourced) | *verified* |

### 9.3 Both models: invoices per $1,000 of TL+LTL spend

| Evidence | Figure | Label |
|---|---|---|
| Cass average transportation invoice, all modes (known) | $1,011 (2024) → **1.0 invoice per $1,000** | **[our calc]** on N-X14 |
| **Saia, full-year 2024**: LTL revenue per shipment "$347.81" ($294.23 excluding fuel) | **2.88 invoices per $1,000** if all LTL | *verified* (N-AA45); **[our calc]** |
| **Knight-Swift truckload, 2024**: revenue per tractor $193,436; miles per tractor 81,563; average haul 383 miles | $2.37 per total mile × 383 = **$908 a load** before empty miles and fuel, so about **$0.9-1.2k** → **0.8-1.1 per $1,000** if all TL | *verified* (N-AA46); **[our calc]** |
| National for-hire split (known): TL $387B, LTL $64B | LTL = 14% of TL+LTL dollars | *assumed* (N-K22) |

| LTL share of the shipper's TL+LTL dollars [our call] | Invoices per $1,000 [our calc] | Used as |
|---|---|---|
| 14% (national mix) | 1.18 | ≈ low (1.0 with Cass's figure) |
| **30%** | **1.49** | **central 1.5** |
| 60% | 2.09 | high 2.1 |
| 100% (LTL only) | 2.88 | sensitivity |

---

## 10. Re-run of the per-customer model [our calc]

### 10.1 Formula

For a shipper with TL+LTL spend **S** a year:
- invoices **N** = S ÷ 1,000 × **k** (invoices per $1,000);
- recoveries **R** = S × overcharge rate **r** × share caught **c** × share credited **p**;
- fee **F** = 25% × R;
- variable cost **V** = N × (cost per invoice + disputed share **d** × cost per dispute);
- **gross profit (run-rate)** = F − V − fixed cost a year; **year 1** also subtracts onboarding.
- **Break-even spend** S\* = fixed ÷ [0.25 × r × c × p − k/1,000 × (cost per invoice + d × cost per dispute)]; "never" when the bracket is zero or negative.
- **Overcharge rate that covers variable cost** r\* = k/1,000 × (cost per invoice + d × cost per dispute) ÷ (0.25 × c × p).

Check X's rate sets are kept: **low** 0.5% × 50% × 60% (d = 3%); **central** 1.5% × 70% × 80% (d = 5%); **high** 3% × 85% × 90% (d = 10%). Spends are the four bands' central TL+LTL spend: **$272k** (manufacturers, 20-99 staff), **$633k** (wholesalers, 20-99), **$1.59M** (manufacturers, 100-499), **$2.9M** (wholesalers, 100-499). No backlog is included (check X §10 has it).

### 10.2 (a) AI-heavy, central costs, k = 1.5

| Row | $272k Low | $272k Central | $272k High | $633k Low | $633k Central | $633k High | $1.59M Low | $1.59M Central | $1.59M High | $2.9M Low | $2.9M Central | $2.9M High |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recoveries | $408 | $2,285 | $6,242 | $950 | $5,317 | $14,527 | $2,385 | $13,356 | $36,490 | $4,350 | $24,360 | $66,555 |
| Fee at 25% | $102 | $571 | $1,561 | $237 | $1,329 | $3,632 | $596 | $3,339 | $9,123 | $1,088 | $6,090 | $16,639 |
| Invoices a year | 408 | 408 | 408 | 950 | 950 | 950 | 2,385 | 2,385 | 2,385 | 4,350 | 4,350 | 4,350 |
| Disputes | 12 | 20 | 41 | 28 | 47 | 95 | 72 | 119 | 238 | 130 | 218 | 435 |
| Variable cost | $379 | $455 | $645 | $882 | $1,059 | $1,500 | $2,216 | $2,659 | $3,768 | $4,041 | $4,850 | $6,873 |
| Fixed a year | $400 | $400 | $400 | $400 | $400 | $400 | $400 | $400 | $400 | $400 | $400 | $400 |
| **Gross profit, run-rate** | −$677 | **−$284** | $516 | −$1,045 | **−$129** | $1,732 | −$2,019 | **$280** | $4,954 | −$3,354 | **$840** | $9,366 |
| Gross margin | — | −50% | 33% | — | −10% | 48% | — | 8% | 54% | — | 14% | 56% |
| Year 1, after $400 onboarding | −$1,077 | −$684 | $116 | −$1,445 | −$529 | $1,332 | −$2,419 | −$120 | $4,554 | −$3,754 | $440 | $8,966 |

### 10.3 (b) Human-heavy, central costs, k = 1.5

| Row | $272k Low | $272k Central | $272k High | $633k Low | $633k Central | $633k High | $1.59M Low | $1.59M Central | $1.59M High | $2.9M Low | $2.9M Central | $2.9M High |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fee at 25% | $102 | $571 | $1,561 | $237 | $1,329 | $3,632 | $596 | $3,339 | $9,123 | $1,088 | $6,090 | $16,639 |
| Variable cost | $2,839 | $3,064 | $3,627 | $6,607 | $7,131 | $8,441 | $16,595 | $17,911 | $21,203 | $30,267 | $32,668 | $38,672 |
| Fixed a year | $800 | $800 | $800 | $800 | $800 | $800 | $800 | $800 | $800 | $800 | $800 | $800 |
| **Gross profit, run-rate** | −$3,537 | **−$3,293** | −$2,867 | −$7,169 | **−$6,601** | −$5,609 | −$16,799 | **−$15,372** | −$12,880 | −$29,980 | **−$27,378** | −$22,833 |
| Year 1, after $1,200 onboarding | −$4,737 | −$4,493 | −$4,067 | −$8,369 | −$7,801 | −$6,809 | −$17,999 | −$16,572 | −$14,080 | −$31,180 | −$28,578 | −$24,033 |
| *PRGX-style: fee × (1 − 59%)* | $42 | $234 | $640 | $97 | $545 | $1,489 | $244 | $1,369 | $3,740 | $446 | $2,497 | $6,822 |

Why (b) fails [our calc]: auditing every invoice by hand at central inputs costs **1.13% of spend**, while the central fee is **0.21% of spend**. Even a 100% fee share would not cover it at central rates. The PRGX-style row cannot go negative by construction, and it describes firms that choose large clients and high-yield work.

### 10.4 Break-even spend and the overcharge rate that covers variable cost

Cost cases use their own k (low 1.0, central 1.5, high 2.1). Caught and credited in r\* are central (70%, 80%), with d = 5%.

| Model | Cost case | Break-even, low rates | **Break-even, central rates** | Break-even, high rates | **r\* (covers variable cost)** |
|---|---|---|---|---|---|
| (a) AI-heavy | Low | $0.48M | $0.07M | $0.03M | 0.06% |
| (a) AI-heavy | **Central** | never | **$0.94M** | $0.12M | **1.19%** |
| (a) AI-heavy | High | never | never | never | 9.79% |
| (a) AI-heavy, **offshore reviewers** (central otherwise: $0.28 per invoice, $3.07 per dispute) | Central | never | **$0.28M** | $0.08M | **0.46%** |
| (b) Human-heavy | Low (all offshore, k = 1.0) | never | $0.11M | $0.02M | 0.82% |
| (b) Human-heavy | **Central** | never | **never** | never | **8.05%** |
| (b) Human-heavy | High | never | never | never | 34.65% |
| (b) Human-heavy, **offshore auditors** (central otherwise: $2.00 per invoice, $9.00 per dispute) | Central | never | never | $0.58M | **2.63%** |
| *Check X, for comparison* ($0.50, $12, 6%, $600, k = 1.0) | — | never | $0.68M | $0.15M | 0.87% |

**Overcharge rate needed for gross profit ≥ 0**, including fixed cost (central caught, credited and d):

| Model / cost case | $272k | $633k | $1.59M | $2.9M |
|---|---|---|---|---|
| (a) AI-heavy, low | 0.45% | 0.23% | 0.13% | 0.10% |
| **(a) AI-heavy, central** | **2.25%** | **1.65%** | **1.37%** | **1.29%** |
| (a) AI-heavy, high | 12.7% | 11.0% | 10.3% | 10.1% |
| (a) AI-heavy, central, offshore reviewers | 1.51% | 0.92% | 0.64% | 0.56% |
| (b) Human-heavy, low | 1.08% | 0.93% | 0.87% | 0.85% |
| **(b) Human-heavy, central** | **10.2%** | **9.0%** | **8.4%** | **8.2%** |
| (b) Human-heavy, central, offshore auditors | 4.73% | 3.53% | 2.98% | 2.82% |

### 10.5 Sensitivities (central rates)

**Invoices per $1,000 (AI-heavy, central costs):**

| k | $272k | $633k | $1.59M | $2.9M | Break-even | r\* |
|---|---|---|---|---|---|---|
| 1.0 (TL-heavy) | −$132 | $224 | $1,166 | $2,456 | $0.41M | 0.80% |
| **1.5** | −$284 | −$129 | $280 | $840 | **$0.94M** | 1.19% |
| 2.1 (60% LTL) | −$466 | −$553 | −$784 | −$1,100 | never | 1.67% |
| 2.9 (all LTL) | −$708 | −$1,118 | −$2,202 | −$3,687 | never | 2.31% |

**Gross profit by cost case, central rates:**

| Model / cost case | $272k | $633k | $1.59M | $2.9M |
|---|---|---|---|---|
| (a) AI-heavy, low | $398 (70%) | $1,125 (85%) | $3,054 (91%) | $5,694 (93%) |
| (a) AI-heavy, central | −$284 | −$129 | $280 (8%) | $840 (14%) |
| (a) AI-heavy, central, offshore reviewers | −$6 | $518 (39%) | $1,905 (57%) | $3,804 (62%) |
| (a) AI-heavy, high | −$4,256 | −$8,444 | −$19,548 | −$34,747 |
| (b) Human-heavy, low (all offshore) | $158 (28%) | $501 (38%) | $1,410 (42%) | $2,655 (44%) |
| (b) Human-heavy, central | −$3,293 | −$6,601 | −$15,372 | −$27,378 |
| (b) Human-heavy, high | −$14,824 | −$31,578 | −$75,992 | −$136,789 |

Percentages are gross margins. The all-offshore human-heavy case (28-44%) lands on PRGX's 35-45%, which is a rough cross-check of the inputs.

### 10.6 What changed from check X

| Check X input | Replacement (central) | Effect |
|---|---|---|
| $0.50 per invoice, one number | **$0.10 machine + $0.55 human review = $0.65** | Machine reading is cheaper than guessed; the human share is new and larger |
| $12 per dispute (18 minutes at $40) | **$9.30** (15 minutes at a sourced $36.79) | Similar |
| 6% disputed (central) | **5%** | Similar; now consistent with a $140 average dispute |
| $600 fixed a year | **$400** ($150-1,100) | Lower; no longer the deciding input |
| $1,000 onboarding | **$400** ($110-1,500) | Lower; hours still unsourced |
| 1 invoice per $1,000 | **1.5** (1.0-2.9) | **Raises variable cost by 50%**; the biggest single change |
| Human-heavy = 60% of the fee | Bottom-up: auditing every invoice costs 1.1% of spend | A human-heavy firm must sample, specialise or price above 25% |

---

## 11. What the web could not settle

The savings assessment on real invoices (`5_validation.md` §6.1; kit blocks C and E) should **time and count** these, per shipper:

1. **Minutes per exception review** after machine reading, split by document type (EDI 210, carrier PDF, scanned BOL, handwritten POD). No freight source exists; the central model assumes 6.
2. **Minutes per dispute from start to close**: preparing the claim, sending it, the number of carrier follow-ups, and elapsed days, split by LTL national, LTL regional, TL asset carrier and broker. No overcharge-dispute figure exists; the model assumes 15.
3. **The share of packets a person must touch** after machine reading (target: 5-30%), and the share actually disputed (3-10%). Also record **the smallest overcharge worth disputing** (damage-claim practice skips claims under $200-500).
4. **Field accuracy of LLM reading on these shippers' own documents.** The academic 92.7-96.5% is for public invoice sets, not freight packets.
5. **Invoices per $1,000 of spend**, the LTL share of dollars, and **pages per packet**, including whether BOLs and PODs exist at all for the look-back period.
6. **Hours to load one shipper's rate agreements**, per carrier (discount, FAK, accessorial schedule, fuel table), and how many change in a year.
7. **Account hours a year per customer**: questions, reports, carrier contacts and rate updates.
8. **Whether LTL base-rate or class data is needed** to rate bills (CzarLite price not public; ClassIT+ by API is $3.0-9.8k a year).
9. **Offshore feasibility:** whether shippers accept invoice data handled offshore (it moves break-even from $0.94M to $0.28M in the model).

---

## 12. For the coordinator (not a call)

1. **Reading a freight invoice by machine costs cents.** At list prices the machine part runs **$0.001-0.25 per 3-5 page packet** [our calc]. **The cost per invoice is set by human touch:** the share of packets a person looks at × minutes × wage. On central inputs that is $0.55 of a $0.65 total.
2. **With sourced wages, the lean model gets worse, not better.** Central AI-heavy break-even moves from check X's $0.68M to **$0.94M** of TL+LTL spend. The overcharge rate needed to cover variable cost moves from 0.87% to **1.19%**. That is above every neutral rate found in check X (0.07-0.48%). **With offshore reviewers the same model breaks even at $0.28M** and needs 0.46%. Where the review work is done is a large lever [our calc].
3. **Invoices per dollar of spend is a hidden second lever.** An LTL bill averages about $348 (Saia 2024), against Cass's all-mode $1,011. A shipper with 60% of its TL+LTL dollars in LTL has about twice the invoices, and on central AI-heavy costs **never breaks even at central rates**. Small LTL-heavy shippers are the costliest to serve per dollar of fee [our calc].
4. **A human-heavy audit of every invoice does not fit a 25% contingency fee.** Vendors put a manual audit at 8-13 minutes an invoice, all vendor figures. At a US clerk's loaded wage that costs about **1.1% of spend**, against a central fee of **0.21%**. Offshore labour and fewer invoices (the all-offshore low case) bring margins to 28-44%, which matches PRGX's 35-45%. This fits the market as check X found it: human firms take 25-50% shares (50/50 for small shippers), serve larger clients, or sample.
5. **The unsourced $600 fixed cost is no longer the deciding input.** The sourced replacement is $150-1,100 a year ($400 central), anchored on 100-250 accounts per SMB customer-success manager and BLS wages. The hours per account and the onboarding hours are still our calls.
6. **Company-level costs sit outside gross profit but are not small for small accounts.** SOC 2 upkeep, a compliance platform and LTL class data come to about $34-84k a year, or **$340-840 per customer at 100 customers** [our calc]. That is about the whole central fee from a $272k shipper.
7. **Margin benchmarks bracket the answer rather than set it.** Human-heavy recovery audit runs 35-45% (PRGX), outsourcers 35-38%, AI-native products 45-53% (ICONIQ), and AP software 60-86%. In the model an AI-heavy contingency audit runs from negative to over 80%, driven by the overcharge rate and the human touch.
8. **The biggest gaps are measurable in the savings assessment:** minutes per exception and per dispute, the touched share, and invoices per $1,000 on real packets (§11). No public freight source measures any of them.

---

## 13. Sources

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-AA01 | Amazon Textract pricing page | current | https://aws.amazon.com/textract/pricing/ | extraction | Per-page prices shown for US West (Oregon); tiers |
| N-AA02 | AWS Price List API, Amazon Textract, us-east-1 (JSON) | current | https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonTextract/current/us-east-1/index.json | full (data file) | Every Textract price dimension and tier in US East |
| N-AA03 | Azure Retail Prices API, "Azure Document Intelligence", eastus | current | https://prices.azure.com/api/retail/prices?$filter=productName eq 'Azure Document Intelligence' and armRegionName eq 'eastus' | full (API) | 68 meters: Read, prebuilt, layout, custom, generative, commitment tiers |
| N-AA04 | Azure Document Intelligence pricing page | current | https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/ | extraction | Structure only; prices not rendered |
| N-AA05 | Google Cloud Document AI pricing | current | https://cloud.google.com/document-ai/pricing | blocked (truncated) | Nothing usable |
| N-AA06 | Invoice Data Extraction blog, "Google Document AI Invoice Parser Pricing Explained" | 2026-06 | https://invoicedataextraction.com/blog/google-document-ai-invoice-parser-pricing | extraction (secondary) | $0.10 per 10 pages, block billing |
| N-AA07 | Search summary citing Flowwright and others on Google Document AI | 2026 | https://flowwright.com/blog/document-ai-pricing-guide | snippet | Form Parser and Custom Extractor $30 per 1,000 pages; hosting $0.05/hour |
| N-AA08 | Mindee pricing | current | https://www.mindee.com/pricing | extraction (two passes, inconsistent) | Plan prices, credits, overage rule |
| N-AA09 | Rossum pricing | current | https://rossum.ai/pricing/ | extraction | Starter from $18,000/year |
| N-AA10 | Nanonets pricing | current | https://nanonets.com/pricing | extraction | Per-block prices; 4-6 blocks per invoice; volume discount |
| N-AA11 | Veryfi pricing | current | https://www.veryfi.com/pricing/ | extraction | $0.16 per invoice; minimums; commitment discount |
| N-AA12 | Anthropic, Claude API pricing | current | https://platform.claude.com/docs/en/about-claude/pricing | full | Model prices, batch, caching |
| N-AA13 | Anthropic, PDF support | current | https://platform.claude.com/docs/en/build-with-claude/pdf-support | full | 1,500-3,000 tokens per page plus image tokens |
| N-AA14 | Anthropic, Vision | current | https://platform.claude.com/docs/en/build-with-claude/vision | full | Image token formula and caps |
| N-AA15 | Google, Gemini API pricing | current | https://ai.google.dev/gemini-api/docs/pricing | extraction | Flash-Lite, Flash, 3.8 Flash, Pro prices, batch |
| N-AA16 | Google, Gemini document processing | current | https://ai.google.dev/gemini-api/docs/document-processing | extraction | 258 tokens per page |
| N-AA17 | OpenAI API pricing | current | https://developers.openai.com/api/docs/pricing | extraction | GPT-5 family standard and batch prices |
| N-AA18 | Berghaus, Berger, Hillebrand, Cvejoski, Sifa, "Multi-Modal Vision vs. Text-Based Parsing: Benchmarking LLM Strategies for Invoice Processing", arXiv 2509.04469 | 2025-08-29 | https://arxiv.org/abs/2509.04469 (results: https://arxiv.org/html/2509.04469) | abstract full; results table by extraction | Field accuracy by model and dataset |
| N-AA19 | Parseur, "AI Invoice Processing Benchmarks 2026" | 2026-09-08 | https://parseur.com/blog/ai-invoice-processing-benchmarks | extraction (secondary) | 10-30 minutes manual entry; pointed to N-AA18 |
| N-AA20 | Tipalti pricing | current | https://tipalti.com/pricing/ | extraction | $99/month AP; per-invoice fees unstated; implementation included |
| N-AA21 | Stampli pricing | current | https://www.stampli.com/pricing/ | extraction | No prices; "deploy in weeks" |
| N-AA22 | BILL pricing | current | https://www.bill.com/pricing | extraction | Per-user plans; ACH, check, card fees |
| N-AA23 | Ramp pricing | current | https://ramp.com/pricing | extraction | Free and Plus plans; OCR included |
| N-AA24 | Ken from Finance, "AP Automation Pricing Compared (2026)" | 2026-05-12 | https://www.kenfromfinance.com/blog/ap-automation-pricing-comparison | extraction (secondary; own prices stated) | Ten vendors' prices and implementation fees |
| N-AA25 | Search summaries on Stampli and AvidXchange pricing (Vendr figures; Goldman Sachs estimate) | 2026 | https://dokka.com/stampli-pricing/ ; https://dokka.com/avidxchange-pricing/ | snippet | $8-15k/year at 500-1,000 invoices/month; $440/month; $4-40k implementation; $16.00-22.26 manual per invoice |
| N-AA26 | DoD Comptroller, FY2003 budget justification, Defense Working Capital Fund, DFAS | 2002 | https://comptroller.war.gov/Portals/45/Documents/defbudget/fy2003/budget_justification/pdfs/06_Defense_Working_Capital_Fund/DFAS.pdf | full (PDF text) | Costs and workload by output, FY2001-2003 |
| N-AA27 | Global BPO Index, "Accounts Payable Outsourcing: A Buyer's Guide" (Anurag Singh) | 2026-07-07 | https://globalbpoindex.com/guides/accounts-payable-services/ | extraction | Per-invoice and hourly rates by delivery model |
| N-AA28 | HiveDesk, "How Much Does BPO Cost?" | 2026-03-23 | https://www.hivedesk.com/blog/outsourcing/bpo-pricing-guide-2026 | extraction | Back-office hourly rates by country |
| N-AA29 | LateShipment.com pricing | current | https://www.lateshipment.com/pricing/ | extraction | OneAudit 35% of refunds |
| N-AA30 | 71lbs pricing | current | https://71lbs.com/pricing | extraction | No numbers |
| N-AA31 | Intelligent Audit, "Should I outsource freight auditing and why" | 2022-04-18 | https://www.intelligentaudit.com/blog/should-i-outsource-freight-auditing-and-why | extraction | 10 minutes, 48 a day, $20/hour example |
| N-AA32 | Navix, "LTL Freight Audit Software for Brokers & 3PLs" | 2025-12-31 (updated 2026-09-15) | https://www.navix.io/ltl-freight-audit-software/ | extraction | Charge lines, 67-100 hours per 2,000 charges |
| N-AA33 | MyCarrier, "Transform Your Freight Audit Process and Reduce Costs with a Powerful TMS" | 2024-10-10 | https://go.mycarrier.io/blog/transform-freight-audit-with-tms | extraction | 3.4 hours/week; $77 per 50 shipments; "more than 15%" |
| N-AA34 | Intelligent Audit, "How automated freight bill auditing eliminated 20 hours of manual work weekly" | 2026-07-14 | https://www.intelligentaudit.com/blog/how-automated-freight-bill-auditing-eliminated-20-hours-of-manual-work-weekly | extraction | 15-20 hours a week; no per-invoice figure |
| N-AA35 | US Tech Automations, "Replace Manual Freight-Invoice Audits With Automation 2026" | 2026-06-14 | https://ustechautomations.com/resources/blog/reduce-reconcile-freightinvoice-audit-discrepancies-with-automation-2026 | extraction | 12 minutes; hours per 100 invoices; orphan attribution |
| N-AA36 | CorePiper, "The 2026 State of Freight Claims Report" | 2026-04-27 | https://corepiper.com/blog/state-of-freight-claims-2026/ | extraction | Damage claims per processor; filing threshold |
| N-AA37 | Warp, "LTL Claims Cost Shippers $2.4 Billion Per Year" | 2026-03-01 | https://www.wearewarp.com/research/ltl-claims-calculator | extraction | $200-400 per claim processing |
| N-AA38 | Laneproof, "Freight Accessorial Charge Disputes: Broker Playbook" | 2026-04-18 | https://www.laneproof.com/blog/freight-accessorial-charge-disputes-broker-playbook | extraction | 3-5% of accessorial lines; $85-300; 48 hours |
| N-AA39 | BLS OEWS May 2025 via public API v1 (series OEUN000000000000043303101-10, OEUN000000000000043302101-10, OEUN000000000000013108101-08) | 2026 release | https://api.bls.gov/publicAPI/v1/timeseries/data/OEUN000000000000043303103 (and sibling series) | full (API) | Employment, mean and percentile hourly wages |
| N-AA40 | BLS ECEC via public API v1 (CMU2010000000000D, CMU2020000000000D, CMU2020000000000P) | Q2 2026 | https://api.bls.gov/publicAPI/v1/timeseries/data/CMU2020000000000P | full (API) | Private industry compensation, wages, wage share |
| N-AA41 | Search summaries of Glassdoor and ZipRecruiter salary pages | 2026 | https://www.glassdoor.com/Salaries/freight-audit-specialist-salary-SRCH_KO0,24.htm ; https://www.glassdoor.com/Salaries/freight-audit-analyst-salary-SRCH_KO0,21.htm ; https://www.ziprecruiter.com/Jobs/Freight-Audit | snippet (ZipRecruiter 403) | Average pay and ranges |
| N-AA42 | Amazon.jobs, "Freight Audit Payment Analyst, ISCAP - Var", Job ID 10513030 | undated | https://amazon.jobs/en/jobs/10513030/freight-audit-payment-analyst-iscap-var | extraction | Pay range; no volumes |
| N-AA43 | SUNTECKtts, "LTL 101: Billing Accuracy" (reports an SJ Consulting survey) | about 2016 | https://www.suntecktts.com/ltl-101-billing-accuracy/ | extraction (secondary) | 94-99% accuracy, 97% average; respondents; BOL errors |
| N-AA44 | LogiSYM, "Is your freight invoice accurate?"; iTech Data, "Auditing freight invoices internally vs FBAP" | 2021-11; undated | https://logisym.org/is-your-freight-invoice-accurate-a-new-study-claims-it-might-not-be/ ; https://itechdata.ai/auditing-freight-invoices-internally-vs-fbap-service-providers/ | extraction | Unsourced error rates (unusable) |
| N-AA45 | Saia, "Saia Reports Fourth Quarter Results" (GlobeNewswire) | 2025-02-03 | https://www.globenewswire.com/news-release/2025/02/03/3019418/0/en/Saia-Reports-Fourth-Quarter-Results.html | extraction | LTL revenue, weight and shipments, Q4 and FY2024 |
| N-AA46 | Knight-Swift, Exhibit 99.1, Q4 2024 results (read through the fetch tool) | 2025-01 | https://www.sec.gov/Archives/edgar/data/1492691/000149269125000004/exhibit99112312024.htm | extraction (two passes) | Truckload revenue per tractor, miles per tractor, length of haul |
| N-AA47 | NMFTA, ClassIT+ pricing | current | https://classitplus.nmfta.org/pricing | extraction | Web-app and API prices by company type and size |
| N-AA48 | FreightOptics, freight audit and payment service page | current | https://www.freightoptics.com/services/freight-audit-and-payment/ | extraction | "4 to 6 weeks" |
| N-AA49 | Supply Chain Desk, "Best Freight Audit Software 2026" | 2026-08-22 | https://www.supplychaindesk.com/blog/best-freight-audit-software/ | extraction | 4-12 weeks; $1M minimum; Cass pricing not published |
| N-AA50 | Gainsight, "Customer Success Team Planning & Cost Benchmarks" | 2016-03-17 | https://www.gainsight.com/blog/customer-success-team-planning-cost-benchmarks/ | extraction | Accounts and ARR per CSM by segment; CS cost % of ARR |
| N-AA51 | Scrut.io, "How much does SOC 2 compliance cost in 2026?" | 2026-08-05 | https://www.scrut.io/hub/soc-2/cost-of-soc-2-audit | extraction | Audit, platform, pen-test, first-year and recurring cost |
| N-AA52 | SaaS Capital, "2026 Spending Benchmarks for Private B2B SaaS Companies" | 2026 | https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/ | extraction | CS+support 9% of ARR; COGS components |
| N-AA53 | Euclid Ventures, "The Vertical SaaS Profit Premium" | 2024-05-10 | https://insights.euclid.vc/p/the-vertical-saas-profit-premium | extraction | 65% vs 75% gross margin; index composition |
| N-AA54 | Bessemer Venture Partners, "The State of AI 2025" | 2025-08-13 | https://www.bvp.com/atlas/the-state-of-ai-2025 | extraction | Supernova and Shooting Star gross margins |
| N-AA55 | ICONIQ, "2026 State of AI Report: The Builder's Economy" | 2026 (Q2 survey) | https://www.iconiq.com/growth/reports/state-of-ai-2026 | extraction | AI product gross margins 2025-2027; inference share rising |
| N-AA56 | PRGX, fourth quarter and full year 2019 results (GlobeNewswire) | 2020-02-25 | https://www.globenewswire.com/news-release/2020/02/25/1990440/12194/en/PRGX-Global-Inc-Announces-Fourth-Quarter-and-Full-Year-2019-Financial-Results.html | extraction | Revenue and cost of revenue 2018-2019 |
| N-AA57 | PRGX, third quarter 2020 results (GlobeNewswire) | 2020-10-27 | https://www.globenewswire.com/en/news-release/2020/10/27/2115480/12194/en/PRGX-Global-Inc-Announces-Third-Quarter-2020-Financial-Results-Increasing-2020-Adjusted-EBITDA-Guidance.html | extraction | Nine-month cost of revenue 2019 vs 2020 |
| N-AA58 | stockanalysis.com, Genpact financials | current | https://stockanalysis.com/stocks/g/financials/ | extraction (aggregator) | Revenue, cost of revenue, gross margin FY2022-25 |
| N-AA59 | stockanalysis.com, ExlService financials | current | https://stockanalysis.com/stocks/exls/financials/ | extraction (aggregator) | Gross margin FY2022-25 |
| N-AA60 | stockanalysis.com, BILL Holdings financials | current | https://stockanalysis.com/stocks/bill/financials/ | extraction (aggregator) | Gross margin FY2023-26 |
| N-AA61 | stockanalysis.com, AvidXchange financials | current | https://stockanalysis.com/stocks/avdx/financials/ | extraction (aggregator) | Gross margin FY2021-24; delisted 2025 |
| N-AA62 | stockanalysis.com, Performant financials | current | https://stockanalysis.com/stocks/pfmt/financials/ | extraction (aggregator) | Gross margin FY2021-24 (definition unclear) |
| N-AA63 | Loop, "Freight and parcel audit" | current | https://www.loop.com/capabilities/freight-and-parcel-audit | extraction | "Approve 99% of invoices with no touch" |
| N-AA64 | Payouts.com, "Touchless Invoice Processing" | 2026-08-19 | https://payouts.com/resources/touchless-invoice-processing | extraction | Touchless ranges by spend category (no sources) |
| N-AA65 | Amazon Augmented AI pricing | current | https://aws.amazon.com/augmented-ai/pricing/ | extraction | $0.03/$0.02 per page reviewed; MTurk example |
| N-AA66 | AWS Price List API, Amazon S3, us-east-1 (JSON) | current | https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/us-east-1/index.json | full (data file) | S3 Standard $0.023/GB-month |
| N-AA67 | Corpay, "AP Team Productivity: Benchmarks and How Automation Moves Them" | 2026-07-31 | https://www.corpay.com/resources/blog/ap-team-productivity-benchmarks | extraction (secondary) | Ardent and APQC figures restated; used to locate N-X16 pages |
| N-AA68 | Search summary of Hypatos and Rossum pages | 2026 | https://www.hypatos.ai/knowledge-base/idp-high-volume-invoice-processing-platforms | snippet | 85-92% straight-through claims |
| N-AA69 | Search summary on IOFM AP benchmarks | 2026 | https://www.iofm.com/ap/benchmarking | snippet (source page not identified) | 5% exception average; 6,900 vs 4,200 invoices per FTE |
| N-AA70 | Cass, "Cass Information Systems Receives GSA Multiple Award Schedule Contract for Freight Audit and Payment" | 2024-10-02 | https://www.cassinfo.com/news/cass-receives-gsa-multiple-award-schedule-contract | extraction | No contract number or prices |

**Earlier sources re-used:** N-X02 (GSA 1989 fee), N-X12 and N-X13 (PRGX 2018 and 2009), N-X14 (Cass fees and average invoice), **N-X16 (Ardent 2025, re-read in full for pp. 15 and 25-28: best-in-class cost, exception, touchless and automation levels)**, N-X17, N-X24 (Tompkins), N-X26 (Eller), N-X27 (Laneproof), N-X29 (Freightview), N-X30 (MyCarrier), N-X35 (Navix pricing guide), N-X45 (nVision), N-K22 (TL and LTL split), N-R14 (APQC 2018), N-D30 (Cass 10-K).

---

## 14. Could not access, or not found

**Blocked or unusable:**
- **Google Document AI pricing page** returned truncated; its prices are from a secondary guide and a snippet (*assumed*).
- **Azure's pricing page** renders no prices without scripts; the Azure Retail Prices API was used instead.
- **bls.gov web pages and download.bls.gov** refuse automated requests ("Access Denied"). The BLS public API was used for OEWS and ECEC. **The ECEC occupational-group series codes could not be confirmed** (the code list is on download.bls.gov), so the all-private-industry wage share (70.0%) is used for clerks and analysts.
- **APQC benchmark pages** (403): invoices per FTE, cycle time to resolve an invoice error.
- **ZipRecruiter** (403); Glassdoor figures are from snippets only.
- **Supply Chain 24/7's article on Loop** (403). **Amazon job 10401342** (404).
- **GSA Advantage contractor text GS07F0150Y** (empty) and **Auditech's government audit page** (404). GSA eLibrary price lists for SIN 541211 were not reached.
- **Vendr's Stampli page** shows no prices without an account (not signed up).
- **Mindee's pricing extraction** gave figures that do not reconcile.
- **Performant's gross margin** is an aggregator's calculation; Performant reports expenses by type, so the definition is unclear.

**Searched, not found:**
- **Per-invoice freight-audit fees in any public contract**: .gov RFP awards, bid tabulations for cities, counties, school districts and utilities, "cents per bill" wording, Cass contract exhibits, GSA schedule price lists (five searches).
- **Hours to load a shipper's rate agreements**, and prices of rate-loading outsourcers (two searches).
- **Minutes or cost per overcharge dispute**: Transportation & Logistics Council, NASSTRAC, IOFM, Hackett, Credit Research Foundation (three searches). Only damage-claim figures were found.
- **A neutral share of freight invoices disputed or held as exceptions**, including GSA counts of notices of overcharge and carrier 10-K billing-accuracy disclosures (four searches).
- **Job postings stating invoice volumes** for freight audit clerks (two searches).
- **Time studies** of manual freight auditing (academic or government).
- **SMC3 CzarLite licence price.**
- **Per-shipment parcel-audit subscription prices** beyond Freightview's tier.
- **The original SJ Consulting survey** (only the broker's summary).
- **The "American Shipper 2024 Freight Audit & Payment Benchmark Study"** cited by US Tech Automations: no trace found (treated as an orphan attribution).
- **Gross margins of freight audit firms** (all private).
- **Recent DFAS unit costs** per transportation bill (only FY2001-2002 found).

**Not attempted:**
- OpenAI's image-token rules (the OpenAI rows use an OCR-text route instead).
- Hackett Group and Levvel/PayStream benchmark reports (gated).
- Cass's fees per item over time, as a scale curve.
- Official Philippine and Indian wage statistics for AP clerks (the offshore rates are billed BPO prices).
- Gartner Peer Insights and Market Guide (login).
