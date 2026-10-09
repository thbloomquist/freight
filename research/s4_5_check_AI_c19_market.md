# S4.5 check AI: the recovery market's own economics, cost to serve and portal access (C-19)

- **What this is:** input to **S4.5, the profitability check**, for **C-19: retailer on-time-in-full (OTIF) fines and non-trade deductions, for suppliers with $500M or less of sales selling to big-box retailers**, run 01. It covers one slice: **what the businesses already selling deduction recovery reveal about the recoverable rate and the cost to serve, and whether retailers let a third party in.** If existing recovery firms make money serving suppliers of this size, their public numbers bound the two inputs the model cannot measure from the desk:

  > recovered = big-box sales × non-trade deductions % × invalid share × recovered share; fee = 25%;
  > cost = deductions × 5 min triage + invalid ones × 20 min dispute, at $33.70/h loaded (US collector) or $12/h offshore, + $600 fixed
  > (`research/selection_runs/run-01/4_kill_conditions.md` §4.2-§4.4).

- **Date:** 2026-09-22. Everything new here was accessed on 2026-09-22.
- **Status:** input only. **It decides nothing.** No price, segment, score or kill line is set or moved here. Readings are **[our call]** and sit in §7, "For the coordinator (not a call)".
- **Labels:**
  - *verified*: read at the source (SEC filing or exhibit, a retailer's or platform's own published terms or API model, a public job posting's stated pay, a price list on the publisher's own page). Where read through a page-extraction tool, this is said.
  - *assumed*: every vendor claim (always, even on the vendor's own page or help centre), transcripts not filed with the SEC, secondary summaries, search snippets, and anything blocked.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
  - **Vendor figures are kept apart from neutral ones.** Every firm in §4 is a competitor of this card.
- **New source IDs:** N-AI01 to N-AI71 (§8). Earlier IDs keep their meaning and are cited where re-read: N-AE17 (SPS 8-K on SupplyPike), N-AE18 (Carbon6 release), N-AE21 (Q2 2026 call), N-U31 (Q4 2025 call), N-AE26, N-AE34 to N-AE36, N-AE47 (BLS), N-AA40 (wage share 70.0%).
- **Not redone (check AE, `research/s4_check_AE_c19_money.md`):** the 8-K's $8.0M / $25.0M revenue lines, "more than 500" suppliers, the 3P sale headline ($9.5M, 7,300 customers, $23.5M loss), the Q1 2026 call quotes, Eva 20%, Threecolts 15-25%, Vendormint 30%, OverDeduct 25-35%, ClearChain $5,000/month, iNymbus $0.40-0.70/claim and its timing studies, HighRadius enterprise figures, Owlet $1.4M, STAT's $1B/$500B headline. This check goes beyond them.
- **Hard rules kept:** no contact, forms, sign-ups, trials or logins. SEC filings were read only through the WebFetch tool (EDGAR's per-note "R" pages and exhibits); no contact was declared to EDGAR. SPS's investor-relations site timed out, so its documents were read from Wayback Machine copies. LinkedIn job postings were read from its public, logged-out job pages. **No identity was sent anywhere.**
- **Search budget:** the session's shared web-search allowance ran out early in this check (after about 25 searches). Everything after that came from direct fetches of known pages, sites' own public indexes (an API-docs index, a help-centre index, the Wayback Machine's capture index), and logged-out job listings. No other search engine was used as a substitute. Some named firms could not be reached without a search (§9).

**Words used here:**
- **1P / 3P:** a *first-party* supplier sells wholesale *to* the retailer (Amazon Vendor Central, Walmart Retail Link); a *third-party* seller sells *on* a marketplace. C-19's buyer is 1P.
- **Take rate / contingency:** the vendor keeps a percentage of what it recovers. **Subscription:** a flat monthly or yearly fee, whatever is recovered.
- **ARPU / "wallet share":** SPS's average yearly recurring revenue per customer.
- **Adjusted EBITDA:** earnings before interest, tax, depreciation and amortisation, with one-off items removed; a rough cash-profit measure. **Margin** = that ÷ revenue.
- **Pro forma:** the buyer's accounts restated as if an acquired firm had been owned all year. **Customer-relationship intangible:** the value put on the acquired customer base in the purchase accounts.
- **Recovered / identified / mitigated:** vendors use these loosely. *Recovered* = the retailer paid back. *Identified* = flagged as invalid, not yet paid. *Mitigated* = includes fines avoided in future. Only *recovered* is the C-19 fee base.
- **Look-back:** disputing past deductions still inside a window; a one-off first-period catch-up, not a yearly rate.
- **GMV:** gross merchandise value, a seller's sales through a channel.
- **SP-API:** Amazon's Selling Partner API. **AUP:** its Acceptable Use Policy.
- **Retail Link / APDP:** Walmart's supplier portal and its Accounts Payable Dispute Portal. **HighRadius** hosts Walmart's receivables (OTIF-fine) portal. **POL:** Target's Partners Online. **Supplier Hub:** Home Depot's portal. **Vendor Gateway:** Lowe's.
- **EDI 812 / 820:** electronic credit/debit adjustment and remittance advice messages from retailer to supplier.
- **BPO:** business-process outsourcing. **RPA:** robotic process automation ("bots" that operate web portals).
- **Loaded wage:** hourly pay ÷ 0.70, because wages are 70.0% of employer compensation cost (N-AA40).

---

## 1. Summary table

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Revenue per recovery customer a year** | **~$4,700**: Carbon6 (1P + 3P + other seller tools), $40.0M planned ÷ ~8,500 customers | **~$33,000-38,000**: SupplyPike at acquisition, ~$18.4-19.2M a year ÷ 500-550 customers | **$45,000-50,000**: SupplyPike on SPS's 2025 plan ($25.0M, a forecast); ClearChain $60,000 list | revenue lines *verified* (SEC exhibits, results release); customer counts *assumed* (calls, press); per customer **[our calc]** | N-AE17, N-AE18, N-AI07, N-AI09, N-AI35 |
| **SupplyPike list price, per retailer, as % of that retailer's sales (2023)** | **~0.12%** ($58,200 a year at $40-49M of sales) | **~0.12-0.24%** for $6-49M accounts ($10,800-58,200 a year) | **≥0.3%** (<$2M accounts at $6,000 a year) | prices *assumed* (vendor page, read in the archived page code); % **[our calc]** | N-AI16, N-AI15, N-AI14 |
| **Implied recoverable rate, cases with both an amount and a base** | **0.03%**: STAT's "standard deductions disputed and won", $150M of "$500B transactions analyzed" (0.085% with post-audit claims) | **0.46-2.3% a year**: a publisher with "$32M+ GMV" got a $736,129 Amazon look-back settlement (1-5 years); **1.0%**: Glimpse "identified" $10M at a $1B brand (one-off, not recovered) | **2.0-2.7%**: SupplyPike "$500M mitigated" on "$25B" of sales (2022); Glimpse "$1.2M" at a "$45M" brand (secondary source) | all *assumed* (vendor claims); rates **[our calc]** | N-AI22, N-AI29, N-AI45, N-AI18, N-AI25 |
| **Contingency fee share** | **15%** (WakeCommerce, Amazon) | **20-25%** (Eva 20%; OverDeduct 25%; ChargeGuard 25% per reviews; "15 to 25% is the market range") | **30%** (Vendormint); "industry standard of 25-30%" | *assumed* | N-AI32, N-AI36, N-AI33, N-AI39, N-AI37 |
| **Subscription prices and minimums** | $49-99/month self-serve (OverDeduct); SupplyPike $500/month per retailer (2019) | Glimpse **$3,000-4,000/month** (one small brand); SupplyPike $2,000-3,000/month per retailer at $10-29M (2023) | ClearChain **$5,000/month**, "in-house … beats ClearChain … above ~$30M in retail revenue"; SupplyPike "Let's Talk" at $50M+ | *assumed* | N-AI33, N-AI12, N-AI26, N-AI16, N-AI35 |
| **Incumbent profitability** | SupplyPike plan: 2024 Adjusted EBITDA **−$1.5M on $8.0M**; 2025 **breakeven on $25.0M** | Carbon6 plan: **+$5.5M on $40.0M** (13.75%) | SPS, Q2 2026: 1P recovery "nearing consistency with our overall margin profiles" (SPS 2025: **30.8%**) | plans *verified* (SEC exhibit, release); margin quote *assumed* (transcript); 30.8% **[our calc]** on *verified* results | N-AE17, N-AE18, N-AE21, N-AI05 |
| **Posted pay for deduction and chargeback analysts** | **$20.60-27.63/h** (a nut processor's Amazon deductions associate) | median posted midpoint **$30.67/h**, loaded **$43.82/h** (7 in-house postings); SPS's own Revenue Recovery Specialist **$29.47-34.62/h**, loaded **$42.10-49.46/h** | Glimpse's own Deduction Analyst **$85-130K** a year (loaded $58-89/h) | *verified* (postings); loaded **[our calc]** | N-AI45 to N-AI53 |
| **Analyst volumes (deductions per day/week)** | not stated in any of ~25 relevant postings | — | — | not found | N-AI56 |
| **BPO price per deduction or per FTE** | **not published** by Flatworld, Invensis, ARDEM, WNS, Genpact | Walmart itself routes APDP disputes to **Genpact** for review (avg **45 days** to approve) | automation: iNymbus "$5 per claim" → "$1"; bots **$150/month** (Microsoft Power Automate Process), $215 hosted | Walmart/Genpact *assumed* (vendor help centre); bot prices *verified* (list); iNymbus *assumed* | N-AI57, N-AI64, N-AI40, N-AI58 |
| **Portal-access terms** | **Amazon:** portal usernames and passwords may not be requested (AUP 3.3); access must go through "secondary user permissions" (3.7) | **Amazon:** new vendor-only **Invoices API** (v2026-06-25) returns paid/deducted status, shortage-invoice IDs and line-level quantity and price variances with root-cause codes; **no dispute endpoint** | **Walmart:** no payments or deductions API on its supplier developer portal; Retail Link terms behind login (not read). **Target** (2012 rules): no sharing of IDs and passwords, but contractors and agents may be given access under confidentiality | Amazon and Walmart portal *verified* (terms, API model); Target *verified* (archived 2012 copy; current version not readable) | N-AI61, N-AI60, N-AI62, N-AI68, N-AI69 |
| **EDI 812 / 820 availability** | Kroger: **812 and 820** listed as required | Home Depot: **820** on enrolment; remittance also in its portal 3 business days after payment | Walmart, Target, Lowe's, Costco, Amazon: **not confirmed** from public sources read | *assumed* (SPS articles) | N-AI65, N-AI66 |

**One-line reading [our call]:** the market's own numbers do not reveal a recoverable rate for a $20-200M supplier. The only aggregate that splits deduction types (STAT) puts *standard deductions won* at **0.03% of transactions**, the same as the neutral central. What the market does reveal is **willingness to pay**: SupplyPike listed ~0.12-0.24% of a retailer's sales per year, and ~400-500 suppliers bought, skewed larger than average. The incumbent runs profitably at **~$35-50K per customer**, and sold its small take-rate book (~$2,900 per customer) at a loss.

---

## 2. AI1 · SPS Commerce revenue recovery (SupplyPike, Traverse, Carbon6)

### 2.1 What was read

- **SEC filings (via WebFetch, *verified*):**
  - 10-K FY2025: revenue-stream table, acquisitions note, pro forma table, purchase-price allocation (N-AI01).
  - 10-K FY2024: acquisitions note (N-AI02).
  - 10-Q Q2 2026: divestiture note, goodwill roll-forward, revenue note (N-AI03).
  - 8-K exhibits for SupplyPike (N-AE17) and the Q1 2026 results release (N-AI06).
- **Company documents via the Wayback Machine** (the investor site timed out, N-AI71):
  - Investor Day deck, 23 Sep 2025, 101 slides, full text (N-AI04);
  - Q4 2025 results release (N-AI05).
- **Call transcripts (*assumed*):**
  - Q3 2024, Q4 2024, Q2 2025 (Equibles, N-AI07 to N-AI09);
  - Q1 2025 presentation summary (N-AI10);
  - Q3 2025 (Investing.com, N-AI11);
  - Q4 2025 and Q2 2026 re-read for new quotes (N-U31, N-AE21).

### 2.2 Register of numbers

| # | Date | What | Figure | Label | ID |
|---|---|---|---|---|---|
| S1 | 10-K FY2025 | Revenue streams | Fulfillment $637.6M, Analytics $56.0M, Other $24.3M recurring; one-time $33.5M; total $751.5M. **No revenue-recovery line**: recovery revenue is not reported separately | *verified* | N-AI01 |
| S2 | Aug 2024 (8-K ex. 99.1) | SupplyPike plan | Q3 2024 revenue "approximately $3.0 million", Adjusted EBITDA "negatively impacted by approximately $750,000"; FY2024 **$8.0M, −$1.5M**; FY2025 **$25.0M, "breakeven"** | *verified* (a forecast) | N-AE17 (re-read) |
| S3 | Q3 2024 call | SupplyPike scale | CFO: "we expect the acquisition to add approximately **200 customers** to our network and increase wallet share by approximately **350**"; SupplyPike and Traverse "performed a little bit better than expectations". CEO: "SupplyPike customer base does tend to skew a little bit larger … at the larger end of what the historic fulfillment customer is" | *assumed* (transcript) | N-AI07 |
| S4 | 10-K FY2024 | SupplyPike purchase | "a revenue recovery solution"; **$205.8M** net of cash ($118.6M cash + 404,587 shares, $87.2M); subscriber relationships **$71.8M over 9.0 years** (final allocation in FY2025 10-K: customer relationships **$63.0M**, 9 years; developed technology $21.1M; goodwill $133.8M). No pro forma given. Other 2024 buys: Traverse Systems ($29.4M, May 2024), Vision33 SAP integration ($4.3M) | *verified* | N-AI02, N-AI01 |
| S5 | Jan 2025 release | Carbon6 plan | ~$210M, ~40% in stock; Q1 2025 "approximately $7.0 million in revenue and breakeven"; FY2025 "approximately **$40.0 million** in revenue" and Adjusted EBITDA up "approximately **$5.5 million**"; two lines: ChargeGuard (1P deductions) and Seller Investigators (3P) | *verified* (release, page extraction) | N-AE18 (re-read) |
| S6 | Q4 2024 call (10 Feb 2025) | Carbon6 | "We projected around **6,500 customers** … a corresponding decrease in wallet share by about **$1,000**"; Q1 now "about $5.5 million in revenue … and breakeven"; 1P revenue-recovery addressable market "$750,000,000 in the U.S."; SupplyPike described as "100% subscription", Carbon6 as "more of a take-rate model" (search summary of the call) | *assumed* (transcript; take-rate line a snippet) | N-AI08 |
| S7 | 10-K FY2025 | Carbon6 purchase | $210.2M net; customer relationships **$44.5M over 8.0 years**; developed technology $29.4M; goodwill $136.3M. **Pro forma (Carbon6 only, as if owned from 1 Jan 2024): revenue $755.7M (2025), $680.9M (2024)** | *verified* | N-AI01 |
| S8 | Q1-Q2 2025 | Customers | Carbon6 "added approximately **8,500** customers and had an adverse effect on ARPU … The full quarter Q2 impact to ARPU was approximately **$1,400**"; 54,150 customers and ARPU $13,850 at Q1; 2024 ARPU $13,300 | *assumed* | N-AI09, N-AI10 |
| S9 | Q3 2025 call (Oct 2025) | Shortfall | "revenue recovery business, which came in approximately **$3 million below our expectations** in Q3"; "more seasonality … than we had originally anticipated"; headwinds "exclusive to the 3P side"; "the 3P customer count declined approximately 150"; "we offered both models, kind of a SaaS subscription model and take-rate model" | *assumed* | N-AI11 |
| S10 | Q4 2025 call (12 Feb 2026) | Take rate | "1P customers flat sequentially while the number of 3P customers declined by 350"; "With the take rate model that we have there, we did see more to the lower end of what our expectation would be, along with the Amazon policy changes"; future potential "to drive the mix a little bit more from the take rate model to the subscription model" | *assumed* | N-U31 (re-read) |
| S11 | 10-Q Q2 2026 | 3P sale | "$8.8 million in cash, net of cash transferred" (the release says $9.5M paid at closing); loss **$23.5M**; goodwill disposed **$2.3M**; "an immaterial portion of our consolidated operations"; not a discontinued operation; buyer not named | *verified* | N-AI03 |
| S12 | Q2 2026 call (30 Jul 2026) | 1P margins | CEO: "the 1P business, I would say is **nearing consistency with our overall margin profiles**. … It was not that way right out of the gate with … the acquisition of SupplyPike and Carbon6"; not "receiving oversized investment". CFO: the $10.5M removed from H2 2026, and "you can assume the first half of this year was slightly lower than that" | *assumed* | N-AE21 (re-read) |
| S13 | FY2025 results release | Company margin | Adjusted EBITDA **$231.4M** on revenue $751.5M | *verified* (results release) | N-AI05 |
| S14 | Investor Day, 23 Sep 2025 | Sizing | Global TAM $11.1B, US $6.5B, from "US Census NAICS Codes" (Feb 2025); Q2 2025 ARPU **$13,200**; US opportunity by supplier size: **Small ($0-50M revenue) 127,500** firms at an "opportunity" ARPU of $32,500; **Medium ($50-300M) 12,800** at $94,000; **Large ($300M+) 6,300** at $184,500. Revenue recovery appears as one of six products ("Deductions, Chargebacks, Remittance"). **No revenue-recovery revenue, customer count, or basis for the $750M** | *assumed* (vendor deck) | N-AI04 |

### 2.3 What these numbers imply [our calc]

- **SupplyPike's real revenue at acquisition.** Adding ~200 customers and +$350 ARPU to a base of ~44,800-45,350 customers at ARPU $13,000-13,300:
  - revenue added ≈ 200 × (ARPU + 350) + 350 × base ≈ **$18.4-18.6M a year**;
  - the 8-K's $8.0M for Aug-Dec 2024 annualises to **$19.2M**;
  - **per customer: $33-38K** at 500-550 customers. On the 2025 plan ($25.0M, a forecast) it would be $45-50K.
- **Carbon6's real revenue.** The pro forma gap is $680.9M − $637.8M = **$43.1M for 2024**, and $755.7M − $751.5M = $4.2M for 1 Jan-3 Feb 2025, the 34 days before the 4 February close (≈ $44.9M a year). The ARPU arithmetic in Q2 2025 gives ≈ $48M a year. Spread over ~8,500 customers that is **$4,700-5,600 each**, across 1P recovery, 3P recovery and other seller tools.
- **What the 3P book was worth.** 3P revenue ran ≈ $20-21M a year (H2 2026 $10.5M; H1 "slightly lower"). It was sold for $9.5M (**≈ 0.45× revenue**), after carrying ≈ $33M ($9.5M + $23.5M loss). SupplyPike was bought at **≈ 10.7-11.2× revenue** ($205.8M ÷ $18.4-19.2M).
- **Profitability.** SupplyPike was planned to lose $1.5M on $8.0M, then break even on $25.0M; Carbon6 to earn 13.75%. By mid-2026 SPS says the retained 1P business is "nearing" its company margin, which was **30.8%** in 2025 ($231.4M ÷ $751.5M). SPS gives no recovery-only numbers to check this.
- **Revenue per employee.** SupplyPike had ~100 employees at acquisition (N-AE22, check AE): **≈ $185K per employee** on ~$18.5M.

### 2.4 Not disclosed anywhere read

- Revenue-recovery revenue as a line, actual 2025 results against the $25.0M and $40.0M plans, or 1P recovery revenue after the 3P sale.
- 1P recovery customer counts, churn, recoveries per customer, gross margin, and the basis of the $750M addressable market.
- The split of SPS 1P recovery customers between subscription and take rate.

---

## 3. AI2 · SupplyPike before the acquisition

### 3.1 Timeline and scale

| Date | Fact | Label | ID |
|---|---|---|---|
| 2017-18 | Began as the R&D arm of CaseStack (founded 1999), "spun out in 2018 following Hub Group's acquisition of CaseStack"; SPS's own history says SupplyPike was "officially established as its own company in 2018" | *assumed* (press; vendor page) | N-AI18, N-AI19 |
| Jan 2021 - Aug 2022 | Site counters (unchanged across five captures): "**$10M+** Deductions Recovered", "**$5B+** Retail Sales Analyzed", "**160+** Happy Customers" | *assumed* (vendor page, archived) | N-AI17, N-AI14 |
| 20 Jul 2022 | **$25M Series B** (Noro-Moseley, Frontier Growth; Series A investor Blumberg Capital); valued at "$100 million" within two years; "**nearly 400 clients**", all CPG; "nearly 125 employees"; products "helped orchestrate more than **$25 billion** in retail sales and have helped mitigate more than **$500 million** in retail inefficiencies" | *assumed* (press quoting the company) | N-AI18 |
| 2023 | Co-founder CEO left; Dan Sanker became CEO; move to Rogers with "115 employees" | *assumed* | N-AI19 |
| Sep 2023 - Jun 2024 | Homepage: "Trusted by **400+**", then "**500+** retail industry leaders"; E.T. Browne "recovered over $1M from Walmart" | *assumed* (archived) | N-AI17 |
| 31 Jul 2024 | Bought by SPS (§2) | *verified* | N-AI02 |
| Dec 2024 / Feb 2025 | "over $900 million" / "over $1 billion" recovered (check AE) | *assumed* | N-AE24, N-AE25 |

**Funding and revenue before 2024:** the Series A amount and any revenue figure before the acquisition were **not found**. The ARPU arithmetic in §2.3 is the only revenue estimate.

### 3.2 The published price schedule, 2019-2023

The pricing pages were archived with their price tables in the page code, so the whole schedule can be read, not only the default shown. All prices are **per month, per retailer, for the deductions product**, and all are *assumed* (vendor list prices; discounts unknown).

| Capture | How priced | Deductions product price | Other |
|---|---|---|---|
| Dec 2019 (N-AI12) | Flat, per retailer | "Recovery": **$500** per month (up to 10 SKUs); "Visibility" $200; "Snapshot" free | Shipping-document retrieval +$100 per month per integration |
| Jul 2020 (N-AI13) | "Starts at" | Recovery from $500; Visibility from $200 | "Select your annual net ships per retailer to see your price" |
| Jun 2021 (N-AI14) | By Walmart annual sales | **< $10M: $9,720 a year ($810/month); $10-25M: $14,160 ($1,180); $26-49M: $20,160 ($1,680); $50M+: "Let's Talk"**; 10% off for annual billing | BOL/POD retrieval $180/month per connection; Retail Intelligence $7,200-14,400 a year; OTIF Radar $3,600-6,000 |
| May 2022 (N-AI15) | By annual sales, Walmart or Kroger | **<$2M $500; $3-9M $900; $10-19M $2,000; $20-29M $3,000; $30-39M $3,950; $40-49M $4,850; $50M+ quote**; new Walmart suppliers under $2M: all three products for **$99** | History reach: "a full two years" of disputes on one tier, "a full 180 days" on another |
| Feb and Jun 2023 (N-AI16) | By annual sales, per retailer | **Walmart and Kroger:** $500 / 700 / 900 / 2,000 / 3,000 / 3,950 / 4,850. **Target:** $150 / 300 / 750 / 1,500 / 3,000 / 3,950 / 4,850. **Amazon:** $250 / 400 / 800 / 1,600 / 2,800 / 3,950 / 4,850. Tiers: <$2M, $3-5M, $6-9M, $10-19M, $20-29M, $30-39M, $40-49M; $50M+ quote | Banner: "It's settled: All suppliers must dispute on Walmart's APDP"; OTIF Radar $273-1,588 |
| After Jun 2023 | No further captures of the pricing page | — | By 2026 SPS lists "pricing available upon request" (N-AI20, N-AI21) |

### 3.3 The list price as a share of the retailer's sales [our calc]

| Walmart sales band (2023 list) | Price a year | Price ÷ sales |
|---|---|---|
| $3-5M | $8,400 | 0.17-0.28% |
| $6-9M | $10,800 | 0.12-0.18% |
| $10-19M | $24,000 | 0.13-0.24% |
| $20-29M | $36,000 | 0.12-0.18% |
| $30-39M | $47,400 | 0.12-0.16% |
| $40-49M | $58,200 | 0.12-0.15% |

- In 2021 the same bands cost **0.04-0.14%** of sales. The price per retailer roughly **doubled to 2.5×** from 2021 to 2023 at $20-40M of sales.
- **C-19's central supplier at the 2023 list:** $66.7M of big-box sales, about $33M at Walmart:
  - Walmart alone: **$47,400** a year (0.07% of big-box sales), 9.5× the central 25% fee of $5,003;
  - add ~$15M each at Target and Amazon ($18,000 + $19,200): **≈ $84,600** a year (0.13%), 17× the central fee.
- Reviewers' words on value (*assumed*):
  - "periods when it can be difficult to justify the monthly cost" (an accounts-receivable manager, N-AI20);
  - "we more than make up the subscription fees" (consumer goods, 11-50 employees, N-AI21);
  - "recover over a million dollars in the past year and a half, so it is well worth the price" (sporting goods, 51-200 employees, N-AI21).

### 3.4 SupplyPike's own aggregate claims [our calc]

- **Jan 2021 counters:** $10M recovered ÷ $5B of sales analysed = **0.2%**, cumulative. Both are marketing counters, and they never moved while the customer count rose from 160 to 400, so they are stale.
- **Jul 2022 press:** $500M "mitigated" ÷ $25B "orchestrated" = **2.0%**. "Mitigated" includes fines prevented and all deduction types, not only recoveries.

---

## 4. AI3 · Other recovery firms and tools

### 4.1 Cases that state both an amount and a base

All figures are vendor claims (*assumed*); every rate is **[our calc]**.

| # | Firm, case | Amount | Base | Implied rate | What it really measures [our call] |
|---|---|---|---|---|---|
| C1 | **STAT**, all clients (N-AI22) | "$1B+" lifetime, split on its own homepage: "**$600M** Profit leakage (non-deduction) Recovered", "**$275M** Post-audit Errors caught", "**$150M** Standard deductions Disputed and won", "**$100M** Compliance Loss prevented" | "$500B" transactions analysed; "500+" suppliers (Kraft, Funko, B&G Foods, Harman and others) | Standard deductions won: **0.03%**. With post-audit claims: **0.085%**. All categories: 0.2% | The only aggregate that splits types. **Standard deductions land at the neutral central.** Its clients are large |
| C2 | **ChargeGuard (Carbon6)**, "World-Class Publisher", Amazon 1P (N-AI29) | Historical look-back settlement raised "to **$736,129.27** from $95,848.03" | "$32M+ GMV" (period not stated) | 2.3% of one year's GMV; **0.46-1.15% a year** if the look-back covered 2-5 years (Amazon allowed 5 until mid-2025) | A one-off backlog, negotiated upward; Amazon shortages |
| C3 | **Glimpse**, a "$1B CPG brand" (N-AI45, its own job posting; N-AI23) | "reviewed 17,000 deductions in under 24 hours and **identified over $10M** in recoverable revenue" | $1B | **1.0%** identified | Identified, not recovered; one-off; trade deductions included |
| C4 | **Glimpse**, Miss Jones Baking Co. (N-AI26) | "$120,000 in invalid deductions identified during onboarding"; "six figures" recovered; largest single win $22,943.83 (a Walmart shortage) | "8,343 deductions representing **$3.63 million** in deduction value" | 3.3% of deduction dollars found invalid; **average deduction ≈ $435** | Deduction base, not sales; mostly distributors (UNFI, KeHE) plus Walmart |
| C5 | **Glimpse**, "$45M revenue brand" (N-AI25) | "$1.2M recovered … in Year 1" | $45M revenue | **2.7%** | From a funding-news aggregator; **not found on Glimpse's own pages** (N-AI27); natural-foods brands are distributor- and trade-heavy |
| C6 | **SupplyPike** (N-AI17, N-AI18) | $10M; $500M | $5B; $25B | 0.2%; 2.0% | See §3.4 |
| C7 | **Owlet** (SPS; check AE) | $1.4M in six months | $105.7M revenue | 1.3% of a year's revenue in six months | Check AE: likely a first-period catch-up |

Also read, but **no base** stated:
- ChargeGuard "Kids II" ($1.06M → $2.14M; "74% recovery rate on erroneous shortage claims"), a "world-renowned CPG brand" ("over $1M in new fees" recovered plus "over $1M" mitigated in a year), Farouk Systems ($1M in 8 months) (N-AI29);
- Threecolts: Modway $2.7M; Celsius $500K in 8 weeks (N-AI30);
- SalesDuo: WOW Sports $475K over 2020-22, "66% against 20-25%" (N-AI31);
- WakeCommerce: cases of £1.3M, £8.5M, £10M, and "98.1% win rate" on 768 shortage disputes (N-AI32);
- iNymbus: $2.3M of a $2.8M backlog "in just under 3 weeks" (N-AI41);
- Glimpse: Calyan Wax $166,184, Table 87 $145,519, Belcam $137,000, immi $50,000+ in 9 months, Companion Candles $30,000 in 60 days (N-AI26).

### 4.2 Headline rates vendors publish (all *assumed*)

- Glimpse: "2.5% Topline Revenue Lift", "1,154,023" deductions disputed across clients (≈ 5,800 per brand [our calc]), "3-5% of topline" (N-AI27, N-AI25).
- SPS: "$2B+" recovered, "**$700 million** for Walmart suppliers", "5.8%" of revenue lost at Walmart, "1%-5%" typical deduction fees (N-AI42). "5% to 7% of retail revenue" (N-AI43). "Even well-run operations see **1–2% in preventable deductions**" (N-AI44).
- Threecolts: "Recover 2–5% Revenue"; $360M+ recovered (N-AI30).
- WakeCommerce: "averaging £5k lost for every £100k of revenue generated" on Amazon (N-AI32).
- Vendormint: "$3B+ in supplier revenue audited daily" (N-AI37).
- Smyyth (formerly Carixa: carixa.com now redirects to smyyth.com, which sells "Carixa 360° Automation"): "$10 billion in recovery experience" (N-AI38).
- OverDeduct's own illustration: $120,000 of deductions reviewed → $50,000 disputable → $40,000 recovered, a 25% fee of $10,000 (N-AI34).
- A comparison page summarises Carbon6's marketing as "average recovery around 75% of eligible value" (N-AI39).

### 4.3 Prices and minimums found beyond check AE (all *assumed*)

| Firm | Model | Price | Minimum / size note | ID |
|---|---|---|---|---|
| WakeCommerce ProfitGuard (Amazon) | Contingency | "a flat **15%** fee"; "industry standard of 25-30%" | none; 30 days' notice | N-AI32 |
| ChargeGuard (Carbon6) | Contingency | "Published third-party reviews describe a **25%** commission" | — | N-AI39 |
| Tahiti North (agency, comparison) | — | "contingency percentage (**15 to 25% is the market range**)" | — | N-AI39 |
| OverDeduct | Self-serve / contingency / managed | Starter **$49**/month, Pro **$99**/month; done-for-you "**25%** of recovered dollars"; managed: retainer plus reduced % | "No minimum, retainer, or lock-in"; says 25% is "below the 25–35% most contingency auditors charge" | N-AI33 |
| Vendormint | Contingency | "**30%** contingency fee" | none stated | N-AI37 |
| Eva | Contingency | "20%" (confirms check AE) | — | N-AI36 |
| ClearChain | Flat | $5,000/month (confirms check AE); includes "Read-only portal access setup", a "12-month deduction audit", 3PL root-cause work | "Hiring in-house typically only beats ClearChain economically above **~$30M in retail revenue** with several active retailer relationships" | N-AI35 |
| Glimpse | Subscription (case) | Miss Jones: "Monthly cost unchanged: **$3,000–$4,000**", replacing ~15 hours a week of contractor time | — | N-AI26 |
| STAT | Contingency | "no recovery, no fee"; no % stated | — | N-AI22 |
| Resolut (AR tool, screened) | Subscription | $149/month entry; others by quote | not a deduction-recovery service | N-AI42a |

### 4.4 Funding and scale of the newer firms

| Firm | Fact | Label | ID |
|---|---|---|---|
| **Glimpse** | **$35M Series A** led by Andreessen Horowitz (25 Mar 2026), **$52M** total; a $10M 2025 round "retroactively rebranded as a seed round"; "14x year-over-year growth"; "200+ brands"; grew "from 35 to 110 employees"; launched April 2024 after a "hard pivot" | *assumed* (company post; press) | N-AI23, N-AI24, N-AI28 |
| **Carbon6** | Bought chargeguard in May 2023 (release blocked, 403) | *assumed* | N-AI29 |
| **Woodridge Software** | Domain now redirects to "woodridge-software-joins-rcg" (RCG Global Services); page unreachable | *assumed* | §9 |
| iNymbus, Vendormint, ClearChain, OverDeduct, Smyyth, Threecolts, HRG, Cash Flow Solutions | No funding or revenue found | — | §9 |

**Scale reading [our calc]:** Glimpse at ~110 employees and 150-200 clients has **~1.4-1.8 clients per employee**; SupplyPike at ~100 employees and ~500 customers had ~5.

---

## 5. AI4 · Cost to serve

### 5.1 Job postings that state pay

All were read on LinkedIn's public job pages on 2026-09-22 and are *verified* as posted. Hourly = annual ÷ 2,080; loaded = ÷ 0.70 **[our calc]**.

| ID | Employer, title, place | Posted pay | Hourly | Loaded | Duties that matter |
|---|---|---|---|---|---|
| N-AI45 | **Glimpse** (vendor), Deduction Analyst, New York | **$85,000-130,000** + equity | $40.87-62.50 | $58.38-89.29 | "work across a portfolio of leading CPG brands"; "human in the loop"; "Prepare, submit, and manage deduction disputes through retailer portals" |
| N-AI46 | **SPS Commerce** (vendor), Revenue Recovery Specialist, Minneapolis | **$29.47-34.62/hour** | same | **$42.10-49.46** | "drive the resolution of invalid deductions across a book of retailer accounts (such as Amazon, Walmart, and Target)"; "shipping and OTIF violations"; "manage a high volume of disputes across a large book of accounts" |
| N-AI47 | SBH Fashion, AR Chargeback Analyst, New York | $85,000-95,000 | $40.87-45.67 | $58.38-65.25 | "accessing portals to obtain claim copies"; Carixa a plus |
| N-AI48 | BCI Brands, Wholesale Chargeback Analyst, New York | $75,000-85,000 | $36.06-40.87 | $51.51-58.38 | shortages, "shipping violations, EDI violations"; factor disputes |
| N-AI49 | Vince, AR Chargeback Analyst, New York | $55,000-65,000 | $26.44-31.25 | $37.77-44.64 | "routing compliance, EDI transactions"; EDI 820 a plus |
| N-AI50 | John B. Sanfilippo & Son, Deductions Associate, Elgin IL | $20.60-27.63/hour | same | $29.43-39.47 | "Researches and disputes shortage claims through Amazon's vendor platforms" |
| N-AI51 | Bradshaw Home, Deduction Analyst, Fontana CA | $24.50-25.50/hour | same | $35.00-36.43 | shortage and overage claims; carrier-proof portals |
| N-AI52 | Adams Group, AR Senior Collection & Deduction Specialist, Sacramento | $80,000-90,000 | $38.46-43.27 | $54.95-61.81 | deductions plus trade-rebate audit |
| N-AI53 | PepsiCo, CDA Finance Deduction Analyst, Winston-Salem | $60,600-67,000 | $29.13-32.21 | $41.62-46.02 | shared-services deduction analyst |

- **Median midpoint of the seven in-house postings: $30.67/hour, loaded $43.82**, about **1.3×** the BLS mean for bill and account collectors ($23.59; N-AE47) **[our calc]**. Four of the nine are in New York, which lifts the median [our call].
- **SPS's own specialist, loaded, costs 1.25-1.47× the model's $33.70.**
- Also read, duties only (no pay or volumes; N-AI54, N-AI55):
  - nVent, Retail Compliance & Dispute Specialist: "monitor major retail customer portals for compliance infractions, chargebacks, and deductions related to on-time delivery"; "a centralized tracker of all incoming fines, successful disputes, and net losses";
  - Journe Brands, Chargeback Claims Officer;
  - a confidential consumer brand's Cash Application & Deduction Analyst;
  - Tory Burch, Chargeback Analyst.

### 5.2 Volumes

**No posting stated deductions per day or per week.** About 350 listings from ~20 keyword searches were screened, and ~25 relevant postings were read (N-AI56). The only throughput figures remain the vendor ones in check AE (HighRadius 20 a day; iNymbus 8-15 minutes a claim). One more vendor statement: filing "a single dispute can take five to fifteen minutes", attributed to "a supply chain manager" (iNymbus, N-AI41, *assumed*).

### 5.3 BPO prices

- **Not published.** Flatworld Solutions: "customized pricing quote"; Invensis: "25%-30% Cost Reduction", no prices; ARDEM: pricing page 404; Upwork rate pages 403; Genpact and WNS publish none (N-AI57).
- **Walmart outsources the other side.** In APDP, "A claim dispute is submitted via Walmart's Accounts Payable Dispute Portal (APDP) | **Genpact** reviews and approves the dispute | Walmart issues repayment on a check". The average is "**45 days** to be Approved" (some within 7 days by automation, "usually involving smaller dollar amounts"), then "an average of **6 days**" to repayment (SPS help centre, *assumed*, N-AI64).
- **Automation:**
  - iNymbus: Warner Bros from "$5 per claim" to "$1 per claim"; a "$2 billion" client cut direct costs 94%; D&H Distributing automated "80% of freight claims" (N-AI40, *assumed*).
  - Microsoft Power Automate Process: **$150 per bot per month**, hosted $215, paid yearly; UiPath Basic from $25/month, other tiers by quote (N-AI58, N-AI59, *verified* list prices).

### 5.4 The central chain re-run at posted wages [our calc]

Same chain as `4_kill_conditions.md` §4.3: per $1M of big-box sales, 10 deductions triaged at 5 minutes and 1 disputed at 20 minutes (70 minutes), for a fee of $75.

| Wage (loaded) | Variable cost per $1M | Margin per $1M | Break-even big-box sales ($600 fixed) |
|---|---|---|---|
| Model: US collector $33.70 | $39 | $36 | **$16.8M** |
| In-house posted median $43.82 | $51 | $24 | $25.1M |
| SPS specialist $42.10-49.46 | $49-58 | $17-26 | **$23.2-34.7M** |
| Glimpse analyst midpoint $73.84 | $86 | −$11 | never |
| Offshore $12 | $14 | $61 | $9.8M |

At the frozen **pass line** (0.17% found, 0.10% recovered, so 3.4 disputes per $1M), a $50M supplier yields **$8,586** of gross profit at $33.70, **$7,398** at SPS's specialist rate and **$4,639** at Glimpse's analyst rate.

---

## 6. AI5 · Access: may a third party work the retailer's portal, and is the data available?

### 6.1 Amazon (Vendor Central)

- **Acceptable Use Policy for SP-API solution providers** (N-AI61, *verified* at source; no date shown). Quoted:
  - 2.11: "Comply with all applicable Amazon policies … when acting on behalf of an Authorized User, and ensure all submissions and communications are accurate, policy-compliant, and do not result in frivolous or non-compliant contacts or degradation of Amazon support systems."
  - 3.1: "Never share access keys or passwords."
  - 3.3: "**Do not request or share Amazon Portal usernames or passwords from Authorized Users.**"
  - 3.4: "Only act on behalf of Authorized Users that have granted you permission through third-party authorization."
  - 3.6: "Do not ask Authorized Users to share information retrieved from Amazon Portals manually or programmatically to circumvent Amazon policies."
  - 3.7: "**If Amazon Portal access is required to provide features or services that benefit Authorized Users, ask the Authorized User to grant access through secondary user permissions.**"
  - The policy binds developers registered for the SP-API. The Vendor Central terms themselves sit behind a login and were not read.
- **Data by API (new):** the **Invoices API v2026-06-25** is "Vendors only" and lets a vendor "search for invoices within a specified date range, track invoice payment status, and retrieve detailed line-item information for reconciliation" (N-AI60, *verified*: Amazon's docs and its published model file). The model has:
  - invoice statuses "PARTIALLY_PAID", "PARTIALLY_DEDUCTED", "PAID", "DEDUCTED";
  - related identifiers "SHORTAGE_INVOICE_IDS" and "UNIQUE_PAYMENT_IDS" ("Remittance numbers");
  - per line: matched, paid and variance quantities and amounts, with **root-cause codes**: quantity variances ("SHORTAGES_IN_TRANSIT", "NO_APPOINTMENT", "DELETED_APPOINTMENT", "OVERBILLING", "DUPLICATE_INVOICE_DEFECT", "ASIN_MISMATCH", …) and price variances ("DEALBUY", "PRODUCT_COST_NOT_REGISTERED", "CCOGS_PRICE_PROTECTION_AGREEMENT_PPA", "ROUNDING_ISSUES", …).
  - It has **only two read operations**; there is **no endpoint to file a dispute**, and no chargeback (compliance fine) or co-op endpoint in the vendor API list.
- **Retailer moves** (SPS help centre, *assumed*, N-AI64):
  - "For years now, Amazon has limited the disputing of shortage claims through the Vendor Central Dispute Management portal to one dispute per invoice", then added a re-dispute process;
  - Amazon "discontinued the email case creation form for the 'Shortage Claim / Pay On Receipt' issue type";
  - compliance chargebacks: "Vendors have 30 days" to dispute.

### 6.2 Walmart (Retail Link, APDP, HighRadius)

- **No API for payments, deductions, chargebacks, OTIF or disputes** on Walmart's supplier developer portal. It offers Feeds, Items, Order Management, EPCIS (a supply-chain data standard) and drop-ship APIs (N-AI62, *verified*, page extraction).
- **Retail Link terms:** the terms page redirects to the login screen in every capture (N-AI69). **Not read.**
- **How the incumbent connects** (SPS help centre, *assumed*, N-AI63):
  - APDP "is accessed with your normal Retail Link credentials";
  - suppliers type their Walmart **HighRadius** portal "Username and Password" into SPS ("This is NOT your Retail Link login"), and likewise for the Walmart Transportation Portal.
- **Mass disputes exist:** SPS uses "Walmart's Mass Dispute Creation (MDC) process" for shortages without shipping documents (N-AI64).

### 6.3 Target (Partners Online)

- **Rules of Use and Confidentiality Agreement** (N-AI68, *verified*, but only the **2012 archived copy** is readable; the current page renders only with JavaScript):
  - "User shall not permit unauthorized individuals to use User's IDs and/or passwords … **nor shall User permit any individuals to share User's IDs and/or passwords** with other individuals";
  - "User may disclose Confidential Information to its officers, directors, employees, **contractors, and agents** whose duties justify their need to know";
  - "User will contractually bind its agents and **Target-approved third parties** working for User to adhere to the confidentiality and security requirements".
- The incumbent syncs POL data "each weekend" (N-AI63, *assumed*).
- **Windows and rules** (SPS help centre, *assumed*, N-AI64):
  - "Deductions for compliance fines have a **90-day** dispute window";
  - from May 2025, ASN (advance ship notice) availability fines change "from a set 3% COGS received without ASN to **$0.75 per carton**".

### 6.4 Home Depot, Lowe's, Kroger, CVS, Costco

- **Home Depot (Supplier Hub):**
  - SPS asks suppliers to create a user with "**3rd Party User: click 'Yes, they work for', and input 'Contractor'**", using an email address and phone number that SPS supplies;
  - remittance (EDI 820) is available on request to Home Depot's B2B team, and in its MP-SSP portal "three business days from the remittance date" (N-AI63, N-AI66, *assumed*);
  - "as of May 2024, Home Depot has disabled the ability to dispute" trade-discount chargebacks. That is trade, but it shows a retailer closing a dispute path (N-AI64).
- **Lowe's (Vendor Gateway):** access is granted by the supplier's own admin users (N-AI63).
- **Kroger:** 810, **812**, **820**, 824, 850, 856 and 997 are listed as "required"; "Kroger issues an EDI 812 for chargebacks or adjustments" (N-AI65, *assumed*).
- **CVS:** SPS tells suppliers to register a new vendor-portal account using a colleague's name "or a **pseudonym** and email created by your IT team", with a phone number SPS provides (N-AI63, *assumed*).
- **Costco:** nothing public found.
- **SPS's own statement:** "SPS Commerce integrates with dozens of retailer, carrier, and warehouse portals via official API connections or websites. We are familiar with the terms of service of these third-party connections and are compliant with all relevant sections" (N-AI63, *assumed*).

### 6.5 EDI 812 and 820 by retailer

| Retailer | 812 (credit/debit adjustment) | 820 (remittance) | Label | ID |
|---|---|---|---|---|
| Walmart | not confirmed | not confirmed (a Vince posting lists 820 among EDI skills, without naming the retailer) | not found | N-AI49 |
| Target | not confirmed | not confirmed | not found | — |
| Home Depot | not confirmed | **yes**, on enrolment | *assumed* | N-AI66 |
| Lowe's | not confirmed (debit memos in Vendor Gateway) | not confirmed | *assumed* | N-AI63 |
| Costco | not confirmed | not confirmed | not found | — |
| Kroger | **yes** | **yes** | *assumed* | N-AI65 |
| Amazon 1P | not confirmed | not confirmed; **payment status and remittance numbers are available through the Invoices API** | API *verified* | N-AI60 |

---

## 7. For the coordinator (not a call)

Everything here is **[our calc]** or **[our call]**. Nothing is decided.

### 7.1 The vendor "0.2%" anchor, re-read

- Check AE and `4_kill_conditions.md` §4.2 use STAT's "over $1B on $500B" = 0.2% as the vendor-world recovered rate. STAT's own homepage splits the $1B:
  - **60% is "Profit leakage (non-deduction)"**;
  - 10% is "Compliance Loss prevented" (fines avoided, not paid back);
  - **15% is "Standard deductions Disputed and won" = 0.03% of transactions analysed**;
  - with post-audit claims, 0.085%.
- So the one vendor aggregate that can be split **lands on the neutral central for the product C-19 would sell**. The kill line's reasoning note ("half STAT's aggregate") rests on the 0.2% total. This is a reading for the founders, not a proposal to move a frozen line.

### 7.2 What the market reveals: willingness to pay, not a leak rate

- **SupplyPike's list price** was ~0.12-0.24% of a retailer's sales a year for $6-49M accounts, and ~400-500 suppliers bought at list or at a discount. For a buyer to come out ahead on recoveries alone, recoveries would have to be at least that: roughly the kill condition's pass line (0.17% found, 0.10% recovered) or above.
- **Three things break the inference:**
  - (a) value can be labour saved, not money recovered: posted in-house analysts cost $55-95K a year, and ClearChain says in-house only wins "above ~$30M in retail revenue";
  - (b) SPS said SupplyPike's customers "skew a little bit larger";
  - (c) a reviewer found it "difficult to justify the monthly cost" when disputes are denied.
- **Revealed price gap:** a C-19 central supplier would have faced **~$47K (Walmart only) to ~$85K (three retailers)** at SupplyPike's 2023 list, **9-17× the central 25% fee** of ~$5K. Either the market can charge far more than the central chain implies, or SupplyPike's paying customers were not central-chain suppliers. The public record cannot say which.

### 7.3 The incumbent's economics point to large tickets

- **Profitable end:** SupplyPike planned to break even at ~$25M of revenue. By mid-2026 SPS calls its retained 1P recovery business "nearing" company margins (~31%), at **~$35-50K per customer**.
- **Unprofitable end:** the small-ticket take-rate book (3P, **~$2,900 per customer**) earned "the lower end" of expectations, was moved towards a $19.99 subscription, and was then sold at ~0.45× revenue at a $23.5M loss. Amazon policy changes were a stated cause, so this is not only a verdict on take rates.
- **Where C-19 sits:** the central-chain fee (**~$5K** at $66.7M of big-box sales) is nearer the ticket size the market leader exited than the one it kept.

### 7.4 Cost to serve is probably above the model's wage

- Posted pay for this exact job runs **~1.3×** the BLS collector mean. The incumbent's own specialist costs **1.25-1.47×** the model's loaded $33.70.
- **Break-even rises** from $16.8M to **$23-35M** of big-box sales at the central chain. At the pass line the model still clears a $50M supplier ($7.4K of gross profit at SPS's wage).
- At Glimpse's analyst pay the central chain never breaks even, so the fast-growing AI entrant is staffing above the model's cost. This does not change Test 3's definition; it bears on which wage case is "US".

### 7.5 Access

- **No public retailer term found bars a third party from acting for a supplier.**
- **Amazon and Target bar sharing credentials** and point to sub-users (Amazon's "secondary user permissions"; Target's contractors and agents under confidentiality). Home Depot has a "3rd Party User" setting.
- **Walmart's terms could not be read.** Walmart has no deductions API, and the incumbent there relies on supplier-entered passwords (HighRadius). At CVS it relies on pseudonymous registrations, so parts of the access layer rest on practice rather than on published permission.
- **Amazon now publishes an official read API** (June 2026) that exposes shortage and price variances with root causes. That lowers the cost of *finding* invalid Amazon deductions, for us and for every competitor. It does not file disputes.
- For Test 2's "retailer's terms bar third-party access" leg: **no bar found where terms were readable; Walmart unknown.**

### 7.6 Cases with a base cannot settle the rate

- Every case with a base is a vendor claim, and most are one-off look-backs, "identified" amounts, or distributor and trade-heavy brands.
- They span **0.03% to 2.7%**, the same factor-of-100 spread as check AE.
- The only split aggregate (STAT) sits at the low end for standard deductions. Check AE's conclusion stands: **the S5 look-back is the measurement**.

### 7.7 Suggested questions for S5 (not a kit change)

1. What do you pay, or did you pay, SupplyPike/SPS, Glimpse, iNymbus or a contingency firm, and what came back in the last 12 months?
2. Which portals let you add a named third-party or sub-user, and has any retailer refused or warned about a service provider?
3. Do you receive EDI 812/820 from each big-box retailer, or only portal data?
4. How many deductions a week does your team handle, in how many hours, and at what pay?

---

## 8. Sources

Access: **full** = downloaded and read or searched; **page extraction** = read through WebFetch, which summarises long pages (quotes checked where given); **archived** = Wayback Machine copy; **snippet** = search text only; **blocked** = refused.

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AI01 | SPS Commerce, Form 10-K FY2025 (R10, R11, R48, R49, R52, FilingSummary) | filed 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1092699/000109269926000012/R10.htm | page extraction | Revenue streams (no recovery line); Carbon6 and SupplyPike allocations and lives; Carbon6 pro forma |
| N-AI02 | SPS Commerce, Form 10-K FY2024 (R10) | filed 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1092699/000109269925000011/R10.htm | page extraction | SupplyPike "a revenue recovery solution"; $205.8M; $71.8M subscriber relationships; Traverse; no pro forma |
| N-AI03 | SPS Commerce, Form 10-Q Q2 2026 (R8, R9, R49) | filed 2026-07-30 | https://www.sec.gov/Archives/edgar/data/1092699/000109269926000066/R8.htm | page extraction | 3P sale $8.8M net, $23.5M loss, $2.3M goodwill, "immaterial" |
| N-AI04 | SPS Commerce, Investor Day deck (Wayback copy of an investors.spscommerce.com static file) | 2025-09-23 | https://web.archive.org/web/20260313190552/https://investors.spscommerce.com/static-files/9d1a037e-b94d-4ede-a3fb-22f69307e55f | full (archived PDF) | TAM; ARPU $13,200; US opportunity by supplier size; product map |
| N-AI05 | SPS Commerce, Q4 and FY2025 results release (Wayback copy) | 2026-02-12 | https://web.archive.org/web/20260223200700/https://investors.spscommerce.com/static-files/1be11aae-9591-496b-b816-254c6d130714 | full (archived PDF) | Adjusted EBITDA $231.4M; no recovery figures |
| N-AI06 | SPS Commerce, Q1 2026 results release (8-K exhibit) | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1092699/000109269926000042/er_q126.htm | page extraction | No recovery figures |
| N-AI07 | SPS Q3 2024 earnings call transcript (Equibles) | 2024-10 | https://equibles.com/stocks/spsc/calls/2024-q3 | page extraction | ~200 customers, +$350 wallet share; "skew a little bit larger" |
| N-AI08 | SPS Q4 2024 earnings call transcript (Equibles; Investing.com; search summary) | 2025-02-10 | https://equibles.com/stocks/spsc/calls/2024-q4 | page extraction; snippet | 6,500 customers, −$1,000; Q1 ~$5.5M; $750M; subscription vs take rate (snippet) |
| N-AI09 | SPS Q2 2025 earnings call transcript (Equibles) | 2025-07-30 | https://equibles.com/stocks/spsc/calls/2025-q2 | page extraction | 8,500 customers; −$1,400 ARPU; go-to-market teams merged |
| N-AI10 | Investing.com, summary of SPS Q1 2025 presentation | 2025-04-24 | https://www.investing.com/news/company-news/sps-commerce-q1-2025-presentation-highlights-19-revenue-growth-carbon6-integration-93CH-4003574 | page extraction (secondary) | 54,150 customers; ARPU $13,850; 2024 $13,300 |
| N-AI11 | SPS Q3 2025 earnings call transcript (Investing.com) | 2025-10-30 | https://www.investing.com/news/transcripts/earnings-call-transcript-sps-commerce-q3-2025-earnings-beat-eps-forecast-93CH-4322083 | page extraction | ~$3M shortfall; seasonality; 3P −150; both models |
| N-AI12 | SupplyPike, "Pricing – Deductions Navigator" (Wayback) | 2019-12-10 | https://web.archive.org/web/20191210004905/https://www.supplypike.com/deductions/pricing | full (archived HTML) | $500/month per retailer |
| N-AI13 | SupplyPike, "Pricing and Plans" (Wayback) | 2020-07-14 | https://web.archive.org/web/20200714230908/https://www.supplypike.com/pricing | full (archived HTML) | "Starts at" $200/$500 |
| N-AI14 | SupplyPike, "Pricing and Plans" (Wayback; price arrays in page code) | 2021-06-25 | https://web.archive.org/web/20210625043350/https://www.supplypike.com/pricing | full (archived HTML and script) | $9,720 / $14,160 / $20,160 a year by Walmart sales; counters |
| N-AI15 | SupplyPike, "Pricing and Plans" (Wayback) | 2022-05-19 | https://web.archive.org/web/20220519224339/https://www.supplypike.com/pricing | full (archived HTML and script) | $500-4,850/month tiers; $99 new supplier |
| N-AI16 | SupplyPike, "Pricing and Plans" (Wayback, two captures) | 2023-02-09; 2023-06-05 | https://web.archive.org/web/20230209131843/https://www.supplypike.com/pricing | full (archived HTML and script) | Per-retailer arrays (Walmart/Kroger, Target, Amazon); OTIF Radar |
| N-AI17 | SupplyPike homepage (Wayback, 9 captures) | 2020-07 to 2024-06 | https://web.archive.org/web/20240620214824/https://www.supplypike.com/ | full (archived HTML) | Counters; 400+/500+; E.T. Browne >$1M |
| N-AI18 | Talk Business & Politics, J. Della Rosa, "Fayetteville firm SupplyPike receives $25 million in series B capital" | 2022-07-20 | https://talkbusiness.net/2022/07/fayetteville-firm-supplypike-receives-25-million-in-series-b-capital/ | page extraction | ~400 clients; $25B; $500M; $100M valuation; ~125 staff |
| N-AI19 | SPS Supply Chain Source, "Celebrating Years of Innovation & Excellence" | undated | https://www.spscommerce.com/community/articles/5-years-of-excellence | page extraction | History; 115 staff; CEO change |
| N-AI20 | Capterra, "SPS Commerce Revenue Recovery" (SupplyPike) listing | read 2026-09-22 | https://www.capterra.com/p/181276/SupplyPike/ | page extraction | 45 reviews, 4.9; "difficult to justify the monthly cost"; no price |
| N-AI21 | Software Advice listing | read 2026-09-22 | https://www.softwareadvice.com/product/451076-SupplyPike/ | page extraction | Reviewer recoveries and price remarks; "pricing available upon request" |
| N-AI22 | STAT Recovery Solutions homepage (saved copy) | read 2026-09-22 | https://www.statrecovery.com/ | full (HTML) | $1B split: $600M / $275M / $150M / $100M; $500B; clients |
| N-AI23 | Glimpse, "Glimpse raises $35M Series A led by Andreessen Horowitz" | 2026-03-25 | https://www.tryglimpse.com/post/seriesa | page extraction | 14x; 91%; 200+; $1B brand 17,000 deductions |
| N-AI24 | TechCrunch, "After pivoting, Y Combinator grad Glimpse raises $35M led by a16z" | 2026-03-25 | https://techcrunch.com/2026/03/25/a16z-backed-glimpse-raises-new-funds-accelerates-dispute-tracking-automation-for-cpg-brands/ | page extraction | $52M total; seed rebrand; pivot |
| N-AI25 | TAMradar, "Glimpse Raises $35M Series A for CPG Deduction AI" (aggregator) | 2026-08-14 | https://www.tamradar.com/funding-rounds/glimpse-series-a-35m | page extraction (secondary) | "$1.2M … $45M revenue brand"; "3-5% of topline"; 44 employees; 150+ clients |
| N-AI26 | Glimpse resources page and Miss Jones Baking Co. customer story | read 2026-09-22 | https://www.tryglimpse.com/customer-story/miss-jones-baking-co | page extraction | 8,343 deductions, $3.63M; $120K; $3,000-4,000/month; case list |
| N-AI27 | Glimpse homepage | read 2026-09-22 | https://www.tryglimpse.com/ | page extraction | "2.5% Topline Revenue Lift"; 1,154,023 disputes |
| N-AI28 | New Hope Network, D. Brown, "How AI helps CPG brands recover lost revenue from deductions" | 2026-05-05 | https://www.newhope.com/industry-insights/how-ai-is-helping-cpg-brands-fight-back-against-distributor-deductions | page extraction | Glimpse 35→110 staff; 14x revenue; ~10% invalid |
| N-AI29 | Carbon6 ChargeGuard success-stories page and four case-study images (read as images) | Jun and Nov 2024 | https://www.carbon6.io/chargeguard/success-stories | full (PNG images) | Publisher $736,129 on "$32M+ GMV"; Kids II; CPG; Farouk |
| N-AI30 | Threecolts Margin Pro, Amazon vendor deduction recovery | read 2026-09-22 | https://www.threecolts.com/margin-pro/vendor-deduction-recovery/amazon | page extraction; snippet | Modway $2.7M; Celsius $500K (snippet); 2-5% claim |
| N-AI31 | SalesDuo, WOW Sports shortage-claims case | 2024-05-27 | https://salesduo.com/blog/amazon-vendor-central-shortage-claims-case-study/ | page extraction | $475K 2020-22; 66% |
| N-AI32 | WakeCommerce, ProfitGuard | read 2026-09-22 | https://www.wakecommerce.co.uk/profitguard-amazon-chargeback-recovery | page extraction | 15% fee; "25-30%"; £5k per £100k; 98.1% of 768 |
| N-AI33 | OverDeduct, pricing | read 2026-09-22 | https://www.overdeduct.com/pricing | page extraction | $49/$99; 25%; no minimum |
| N-AI34 | OverDeduct, "How contingency deduction recovery works" | read 2026-09-22 | https://www.overdeduct.com/how-contingency-works | page extraction | $120K → $50K → $40K illustration; 20-30% |
| N-AI35 | ClearChain, pricing | read 2026-09-22 | https://useclearchain.com/pricing | page extraction | $5,000/month; read-only access; "~$30M" in-house crossover |
| N-AI36 | Eva, pricing | read 2026-09-22 | https://eva.guru/pricing/ | page extraction | 20% |
| N-AI37 | Vendormint homepage | read 2026-09-22 | https://vendormint.com/ | page extraction | 30%; "$3B+ … audited daily"; 50+ retailers |
| N-AI38 | Smyyth homepage (carixa.com redirects here) | read 2026-09-22 | https://www.smyyth.com/ | page extraction | "Carixa 360° Automation"; "$10 billion in recovery experience" |
| N-AI39 | Tahiti North, "SupplyPike vs Carbon6 vs ChargeGuard (1P)" | 2026-07-11 | https://tahitinorth.com/insights/supplypike-carbon6-chargeguard-alternatives-1p | page extraction | ChargeGuard 25% (reviews); "15 to 25%" range; ~75% claim |
| N-AI40 | iNymbus, "Real Life Case Studies" | read 2026-09-22 | https://www.inymbus.com/case-studies | page extraction | $5 → $1 per claim; 94%; volumes; 80% of freight claims |
| N-AI41 | iNymbus blog: BPO costs (2026-05-11), RPA (2026-05-15), "When 5 to 15% of Revenue Disappears" (2026-07-15) | 2026 | https://blog.inymbus.com/the-story-of-retail-deductions | page extraction | No BPO baseline; $2.3M of $2.8M; 5-15 minutes |
| N-AI42 | SPS Revenue Recovery product pages (main; Walmart) | read 2026-09-22 | https://www.spscommerce.com/products/revenue-recovery/walmart/ | page extraction | "$700 million for Walmart suppliers"; 5.8%; "1%-5%"; connects "directly to Retail Link" |
| N-AI42a | Resolut, pricing (screened) | read 2026-09-22 | https://www.resolutai.com/pricing | page extraction | AR tool $149/month; not deduction recovery |
| N-AI43 | SPS Supply Chain Source, "What Are Revenue Recovery Metrics?" | read 2026-09-22 | https://www.spscommerce.com/community/articles/revenue-recovery-metrics | page extraction | "5% to 7%"; "no universal target" |
| N-AI44 | SPS Supply Chain Source, "EDI Chargebacks Explained" | updated 2026-02-02 | https://www.spscommerce.com/community/articles/edi-chargebacks-explained | full (HTML) | "1–2% in preventable deductions" |
| N-AI45 | LinkedIn, Glimpse "Deduction Analyst" (job 4448263375) | posted ~2026-09-15 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4448263375 | full (public HTML) | $85-130K; duties; $1B brand $10M identified |
| N-AI46 | LinkedIn, SPS Commerce "Revenue Recovery Specialist" (4467159034) | posted ~2026-09-17 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4467159034 | full | $29.47-34.62/hour; book of retailer accounts |
| N-AI47 | LinkedIn, SBH Fashion "AR Chargeback Analyst" (4467420041) | ~2026-09-15 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4467420041 | full | $85-95K |
| N-AI48 | LinkedIn, BCI Brands "Wholesale Chargeback Analyst" (4462032352) | ~2026-09-01 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4462032352 | full | $75-85K |
| N-AI49 | LinkedIn, Vince "AR Chargeback Analyst" (4469980777) | ~2026-09-21 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4469980777 | full | $55-65K; EDI 820 a plus |
| N-AI50 | LinkedIn, John B. Sanfilippo & Son "Deductions Associate" (4465082550) | ~2026-09-15 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4465082550 | full | $20.60-27.63/hour; Amazon shortages |
| N-AI51 | LinkedIn, Bradshaw Home "Deduction Analyst" (4460566708) | ~2026-09-18 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4460566708 | full | $24.50-25.50/hour |
| N-AI52 | LinkedIn, Adams Group "AR Senior Collection & Deduction Specialist" (4453637245) | ~2026-09-08 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4453637245 | full | $80-90K |
| N-AI53 | LinkedIn, PepsiCo "CDA Finance Deduction Analyst" (4454149712) | ~2026-09-15 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4454149712 | full | $60.6-67K |
| N-AI54 | LinkedIn, nVent "Retail Compliance & Dispute Specialist" (4454592959; 4454808098) | ~2026-09-08 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4454592959 | full | Duties; no pay |
| N-AI55 | LinkedIn: Journe Brands (4464186156), confidential consumer brand (4465697178), Tory Burch (4460383906) | ~2026-09 | https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4464186156 | full | Duties only |
| N-AI56 | LinkedIn public job search (~20 keyword queries, ~350 listings); SimplyHired (4 queries) | 2026-09-22 | https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=deductions&location=United%20States | full (listings) | Screening; no volumes stated |
| N-AI57 | BPO pages: Flatworld Solutions pricing; Invensis AR outsourcing; ARDEM pricing; Upwork | read 2026-09-22 | https://www.flatworldsolutions.com/pricing.php ; https://www.invensis.net/services/outsourcing-accounts-receivable | page extraction; ARDEM 404; Upwork 403 | No public prices |
| N-AI58 | Microsoft, Power Automate pricing | read 2026-09-22 | https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing | page extraction | $150/bot/month; $215 hosted; $15/user |
| N-AI59 | UiPath, pricing | read 2026-09-22 | https://www.uipath.com/pricing | page extraction | Basic from $25/month; others by quote |
| N-AI60 | Amazon SP-API docs: index (llms.txt), "Invoices API" page, model financesInvoices_2026-06-25.json (GitHub amzn/selling-partner-api-models), "SP-API models" page | read 2026-09-22 | https://developer-docs.amazon/sp-api/docs/invoice-api.md ; https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/models/finances-api-model/financesInvoices_2026-06-25.json | full (Markdown, JSON) | Vendors only; statuses; shortage and remittance IDs; variance codes; two read operations |
| N-AI61 | Amazon Services API, Acceptable Use Policy (saved copy) | read 2026-09-22 | https://sellercentral.amazon.com/mws/static/policy?documentType=AUP&locale=en_US | full (HTML) | 2.11, 3.1-3.7 |
| N-AI62 | Walmart Developer Portal, Suppliers pages | read 2026-09-22 | https://developer.walmart.com/suppliers ; https://developer.walmart.com/suppliers/docs/get-started | page extraction | API categories; none for payments or deductions |
| N-AI63 | SPS Revenue Recovery (SupplyPike) Help Center, access articles: HighRadius credentials; Walmart Transportation Portal; Home Depot Supplier Hub; CVS SAP Vendor Portal; updating integrations; Lowe's Vendor Gateway admins; Target account status | read 2026-09-22 | https://help.supplypike.com/en/articles/9155664-home-depot-integrate-supplier-hub-to-sps-commerce | full (HTML) | Credentials; "3rd Party User … Contractor"; pseudonym; compliance statement |
| N-AI64 | SPS Help Center, process articles: APDP; Walmart dispute timing; auto-dispute (Walmart, Amazon); Amazon re-dispute; Amazon compliance chargebacks; Target deductions overview; Target compliance program; Home Depot deductions overview; Amazon RevLoss FAQ | read 2026-09-22 | https://help.supplypike.com/en/articles/5229006-how-long-does-it-take-for-walmart-disputes-to-be-approved | full (HTML) | Genpact; 45 and 6 days; MDC; one dispute per invoice; 30 days; 90 days; $0.75 per carton; May 2024 |
| N-AI65 | SPS Supply Chain Source, "How to Set up EDI with Kroger" | 2025-04-15 | https://www.spscommerce.com/community/articles/how-to-set-up-edi-with-kroger | full (HTML) | 812 and 820 required |
| N-AI66 | SPS Supply Chain Source, "Remittance Advice for The Home Depot" | 2025-06-12 | https://www.spscommerce.com/community/articles/remittance-advice-for-the-home-depot | full (HTML) | 820 enrolment; MP-SSP 3 business days |
| N-AI67 | SPS Supply Chain Source, "EDI 812: Debit/Credit Adjustment transaction explained" | 2018-05-24 | https://www.spscommerce.com/community/articles/edi-812-credit-adjustment-spsa | full (HTML) | Definition only; no retailer list |
| N-AI68 | Target Partners Online, "Rules of Use and Confidentiality Agreement" (Wayback) | captured 2012-01-23 | https://web.archive.org/web/20120123163919/https://www.partnersonline.com/sc/public/legal/Pages/Rules-Of-Use.aspx | full (archived HTML) | ID/password sharing ban; contractors and agents; Target-approved third parties |
| N-AI69 | Walmart Retail Link terms page | 2024 captures | https://retaillink.wal-mart.com/home/docs/terms.aspx | blocked (redirects to login) | — |
| N-AI70 | Wayback Machine capture index (CDX) queries: supplypike.com, investors.spscommerce.com, spscommerce.com/community, partnersonline.com, retaillink.wal-mart.com | 2026-09-22 | https://web.archive.org/cdx/search/cdx?url=supplypike.com/pricing&matchType=prefix | full | Finding archived documents |
| N-AI71 | SPS investor-relations site | 2026-09-22 | https://investors.spscommerce.com/ | blocked (timed out) | Replaced by Wayback copies |

Also re-read, with earlier IDs:
- N-AE17 (SPS 8-K ex. 99.1: EBITDA plan lines);
- N-AE18 (Carbon6 release: $7.0M Q1 plan, $5.5M EBITDA);
- N-AE21 (Q2 2026 call: margin quote);
- N-U31 (Q4 2025 call: take-rate quotes).

Downloads are in the session scratchpad (`…/scratchpad/c19_s45/ai/`), not in the project folder.

---

## 9. Could not access, or not found

**Could not access:**
- **Walmart Retail Link terms** (login); **Amazon Vendor Central terms and help pages** (login); **Amazon's retail Conditions of Use** (HTTP 503); **Target's current Partners Online Rules of Use** (JavaScript-only page; the 2012 copy was used).
- **SPS investor-relations site** (timed out; Wayback copies used); **SEC EDGAR direct download** (not attempted: it demands a declared contact).
- **Carbon6-chargeguard acquisition release** (Business Wire 403); **Upwork**, **Indeed** and **ZipRecruiter** (403); **RCG page on Woodridge** (DNS failure); **ARDEM pricing** (404).
- **Glimpse's source for the "$45M brand, $1.2M" case** (only on an aggregator; not found on Glimpse's own pages).

**Not found (searched, or looked for on the firm's own site):**
- **SPS revenue-recovery revenue as a line**, actual 2025 results against plan, 1P recovery customer counts, churn, recoveries per customer, gross margin, and the **basis of the $750M addressable market** (10-Ks, 10-Q, releases, Investor Day deck and five transcripts read).
- **SupplyPike's revenue before 2024**, its Series A amount, and any pricing capture after June 2023.
- **Any case with a sales base from iNymbus, ClearChain, Vendormint, OverDeduct, STAT (single client), Eva, Smyyth/Carixa, HighRadius or Threecolts.**
- **Funding or revenue for iNymbus, Vendormint, ClearChain, OverDeduct, Smyyth, Threecolts.** HRG and "Cash Flow Solutions" could not be located without a web search (budget exhausted).
- **Deductions handled per day or week** in any job posting (~25 relevant postings read).
- **Any BPO's price per deduction or per FTE** for deduction work.
- **Minutes per deduction from a non-vendor source** (beyond check AE's CRF $97 figure, itself vendor-quoted).
- **EDI 812/820 availability** at Walmart, Target, Lowe's, Costco and Amazon.
- **Any published retailer term that expressly bans, or expressly permits, third-party recovery firms** (as distinct from credential sharing).
