# S0 check C: durability, and options for knock-out K11

> **What this is:** the durability investigation that S0.4 row O-3 asks for. On 2026-09-14 the founders decided (F-17, verbatim): "Durability should be its own investigation in itself, unrelated to scoring that is just a hard check of viability." Old row A7 ("growth, low cyclicality, stable structure") therefore left the score and becomes knock-out K11, a pass/fail check at S2. **That it is a hard check is settled; this file does not reopen it.** It covers how documented practice defines and measures durability (C1, C2), how cyclical freight actually is (C3), how software vendors fared in 2022-25 (C4), how to make Constellation's churn test measurable (C5), and options for K11's test and thresholds (C6, §3).
> **Date:** 2026-09-14. **Status:** input to S0. It decides nothing.
> **Labels:** *verified* means read at the source: a quote copied from the page, a downloaded file, or official data downloaded and filtered here. *assumed* means a search snippet, a secondary summary, memory, or a blocked source. **[our calc]** and **[our call]** mark this document's own arithmetic and judgement. R-IDs are reading notes; N-A and N-B IDs are sources from checks A and B (reused, not re-fetched unless noted); N-C IDs are new and listed in §5. Figures read through a page-extraction tool rather than a raw download are marked "via page extraction".

**Plain-language terms used below:**
- **Peak-to-trough:** how far something falls from its high point before a downturn to its low point during it, as a percentage.
- **Truckload (TL):** one shipper's freight fills a whole trailer. **LTL (less-than-truckload):** a carrier combines many small shipments in one trailer and sorts them at terminals. **Drayage:** short truck moves of shipping containers between ports or rail ramps and nearby warehouses. **Intermodal:** containers that travel mostly by rail, with trucks at each end. **Freight forwarder:** arranges international shipments. **Customs broker:** files import paperwork and pays duties for the importer.
- **NAICS:** the US industry code system (e.g. 484121 = long-distance truckload). **PPI:** the Producer Price Index, the prices businesses charge. **BDS / QCEW / BED:** official US counts of firms and establishments (explained in C2).
- **Firm death rate** **[our calc]:** firms that closed completely in a year ÷ firms that year.

---

## 1. Summary

**What "durable" means in documented practice.** The sources use at least six meanings, not one:
- (a) customer firms survive downturns;
- (b) the job or cost the software removes persists when volume falls;
- (c) the market is not shrinking or being displaced over the long term;
- (d) the vendor's revenue does not swing with customer volume;
- plus (e) customers' ability to pay (profits fall much further than revenue);
- and (f) cycle timing (freight has its own cycle, apart from the economy's).

The one fully published formula is **S&P's industry-risk method**. It rates cyclicality 1-6 from the average peak-to-trough fall in industry revenue (bands at 4, 8, 13, 20 and 32%) and in profit margin (bands at 3, 7, 12, 24 and 72%). A separate "competitive risk and growth" factor covers long-term decline and substitution (N-C01, *verified*). S&P rates the transportation industries it calls cyclical **5 of 6 ("high risk")**: revenue fell about 11% and profitability about 59% on average in recessions since 1989 (N-C02, *verified*).

**Freight is cyclical, but unevenly, and 2022-25 was a price downturn more than a volume one.**
- Freight volume (the BTS freight index) fell **16.3%** in 2008-09 and **3.2%** in 2022, then stayed flat.
- Prices collapsed instead: truckload prices fell **24.1%** and broker prices **32.7%** (N-C08, N-C09, *verified* data; **[our calc]**).
- Revenue falls in 2022-25 **[our calc]**:
  - forwarder Expeditors **-45.5%** (2023);
  - broker C.H. Robinson **-28.7%** (2023);
  - LTL carrier Old Dominion **-6.3%** (2023).
- **Firm deaths:** in general freight trucking the rate reached **19.4% in 2023**, twice the economy's 9.4%. Among brokers and forwarders it matched the economy (9.4%) (N-C05, *verified* data; **[our calc]**).
- **Some jobs held up or grew:**
  - freight **invoice counts** fell 2.3% while freight **dollars** fell 14.4% (Cass, 2023);
  - **customs brokerage** fell far less than air and ocean freight;
  - **cargo theft** incidents rose 27% in 2024.

**Software vendors held up better than their customers**, provided revenue was recurring and not tied to a collapsing volume:
- **Held up:** Descartes grew every year with 91-93% recurring revenue. WiseTech grew 15% organically while forwarders' revenue halved. DAT's organic revenue rose in 2023, fell in 2024, and rose again in 2025.
- **Did not hold up:** revenue tied to transactions fell. At Blend, mortgage-software revenue fell 18% and title revenue 58% in 2023. Asset-light freight businesses fell with freight: Uber Freight -24%; Convoy shut down; Transfix sold its brokerage to become a software company (N-C16 to N-C20, N-C26, N-B29).

**K11 options, lenient to strict (§3) [our call]:**
1. No structural decline.
2. Customer firms survive downturns.
3. The job's countable unit holds up in downturns.
4. S&P-style revenue cyclicality.

What each does to the pool:
- Options 1 and 3 keep every freight family alive, and Option 3 drops specific jobs.
- Option 2 drops general-freight carriers (TL, LTL, local, drayage), about two-thirds of trucking employer firms.
- Option 4 drops nearly every freight-company-side candidate and leaves shipper-side candidates in defensive shipper groups.

**Suggested starting point, for discussion only:** Options 1 + 3 as the knock-out, with Option 2 recorded as a flag and Option 4 used as a sensitivity case. **The founders decide.**

---

## 2. Findings

### C1. What do sources mean by a "durable" or "non-cyclical" market for software?

| Meaning | What documented sources say (label) | How it is measured | Freight reading |
|---|---|---|---|
| **(a) Customer firms survive downturns** | Cohen's "Enduring" test: "Will they still be paying (or paying-it-forward) a year from now?" (R19, *verified*). Constellation: "if the underlying attrition of the industry that you are serving is low, this can be a very good business model"; and high churn from clients "going bankrupt and merging" "may be very attractive" (N-B12, letters on 2015 and 2013, *verified*) | Firm death and survival rates (BDS, BED); licence counts (FMCSA) | Freight fails on raw exit rates for general trucking and passes for brokers and warehousing on census data (C3) |
| **(b) The job or cost persists when volume falls** | Index Ventures: "In uncertain economic environments, software spend shifts to the must-haves, away from the nice-to-haves" (N-C22, *verified* via page extraction). Emergence's second reason: moving to new software "often requires some initial IT investment, and this can be hard to make if an industry is in a 'down cycle'" (R21, *verified*). SaaS Capital: "What they sold, and to whom, mattered greatly" (N-C21, *verified* via page extraction) | Volume of the unit the saving is counted in (invoices, loads, entries, claims) | Varies by job: invoice counts and theft held up; broker load counts fell 26% (C3) |
| **(c) The market is not shrinking or displaced** | S&P's second factor covers "Risk of secular change and substitution" and "Risk in growth trends" (N-C01, *verified*). R12 asks for "longer-term variables (e.g. market growth prospects ...)" (*verified*). Porter: "Industry structure changes over time, and is not static" (R43, *verified*) | 10-year projections (BLS); 5-year census change (R44); named substitutes | S&P: trucking growth "tends to track that of gross domestic product"; substitution risk "medium", from rail (N-C02, *verified*). BLS projects truck employment +2.1% for 2025-35 (N-C11) |
| **(d) Vendor revenue does not swing with customer volume** | Emergence's first reason: "seasonal or annual forms of cyclicality make it difficult to build recurring revenue businesses" (R21, *verified*). CAMP's "Predictability" test (R25, *verified*). Rate swings from $3.62 to $2.23 per mile (R34, *verified*) | Volatility of the pricing unit; recurring share of vendor revenue | Mostly a fee-design question, deferred to segment selection (F-7, F-8). K11 can test only the market facts that (d) depends on (C4) |
| **(e) Ability to pay** (sources add) | S&P weights profit cyclicality above revenue cyclicality, "because of the importance of an entity maintaining adequate profitability" (N-C01, *verified*). "For companies with high fixed costs, declines in EBITDA margin are typically much steeper than revenue declines" (N-C02, *verified*). Truckload margin -2.3% (R38) | Margin peak-to-trough (S&P Table 5) | Transportation cyclical margins fell 59% on average (N-C01) |
| **(f) Cycle timing** (sources add) | S&P calibrates on economy-wide recessions (N-C01, *verified*). Berman & Pfleeger measure correlation with GDP (N-C04, *verified*) | Correlation with GDP; industry-specific downturn windows | The 2022-25 freight downturn shows in prices and exits more than in volume (C3). A test keyed only to GDP recessions would miss it **[our call]** |

**Verdict C1:** "Durable" has no single documented meaning. The only codified formula (S&P) combines (a)/(e) through revenue and margin cyclicality with (c) through its growth and substitution factor. (b) and (d) come from software investors and from vendor filings, not from a formula.

**Implications for S0:**
- The founders should say which meanings K11 must test (§4, Q1).
- (d) is mostly about how the fee is built, which is deferred. K11 should test only whether a stable countable unit exists in the market, not choose a fee model.

---

### C2. Existing formulas and published thresholds

| Method (source) | Formula in plain words | Data it needs | Freight data exists? | Thresholds |
|---|---|---|---|---|
| **S&P industry risk** (N-C01, 2013 criteria; the Jan 2024 corporate methodology still points to its Appendix 1 for "the historical cyclical peak-to-trough decline in profitability and revenues for major recessions", N-C03; all *verified*) | For each recession, the fall from "the year before the recession to the year the recession ends", with a lagging year added for late-cycle industries. Average across recessions. Revenue is inflation-adjusted; profit is EBITDA ÷ sales. Look up the revenue band and margin band in Table 2, giving 1-6. Combine with competitive risk and growth (Table 1), which "the criteria weight ... more heavily ... because [it] is a prospective analysis" | Industry revenue and EBITDA margin across recessions | Public carriers and brokers only (10-Ks). No margins for private SMB families | **Revenue bands:** ≤4%, 4-8%, 8-13%, 13-20%, 20-32%, >32%. **Margin bands:** ≤3%, 3-7%, 7-12%, 12-24%, 24-72%, >72%. The bands come from "k-means clustering". **Growth factor:** low risk if sales grow at or above nominal GDP; high risk if "rising by less than 1%, or are declining". A high rating on barriers to entry or on substitution caps the competitive factor at 4 |
| **S&P, transportation cyclical sector** (N-C02, Feb 2014, *verified*) | The same method applied to airlines, shipping and trucking. Company volatility uses the "standard error of regression (SER), subject to having at least seven years of historical annual data" | As above | — | Cyclicality 5 (high). Competitive risk 4 (barriers "High Risk", margins "High Risk", substitution "Low Risk", growth "Medium Risk"). Average revenue PTT -10.7%, 2007-09 -17.3%. Average margin PTT -59.1% (N-C01 Tables 5-6) |
| **Moody's surface transportation** (N-C28) | Scorecard with a business profile factor | — | — | **Not accessed** (login page). A snippet says it considers cyclicality (*assumed*). No thresholds verified |
| **Correlation with GDP** (Berman & Pfleeger, BLS, 1997; N-C04, *verified*) | "the Pearson product moment coefficient of correlation (r)" between industry employment (or final demand) and GDP; "coefficients closer to 1 showing cyclical industries" | Annual industry employment and GDP | Yes (BLS CES) | No cut-off. Ranked: household furniture 0.9591 is the most cyclical; beverages 0.0091 the least. **Trucking and warehousing: employment r = .7621; final demand .3579 (historical), .6586 (projected)** |
| **Firm death and entry rates** (Census BDS; N-C05, *verified*) | Firm death = "Count of firms that have exited in their entirety during the period. All establishments owned by the firm must exit". Exit rate = "100 * (estabs_exit at time t divided by the average of estabs at t and t-1)". The year runs from March 12 to March 12 | Free CSV by 4-digit NAICS, 1978-2023 (payroll firms only) | Yes: 4841, 4842, 4885, 4931, 4921 | None published. Compare with the all-economy rate **[our call]** |
| **Survival of new establishments** (BLS BED Table 7; N-C06, N-A24, *verified* via page extraction) | Share of establishments opened in a given March still alive 1, 2 and 5 years later | Sector level only (all transportation and warehousing) | Yes, but not by family | None. Transportation's 1-year survival: 73.4% (2008 cohort) against 75.2% for all private businesses; 75.6% (2022) against 76.3%; 77.0% (2024) against 77.9% |
| **Licence counts** (FMCSA, via N-B02, N-B03, N-B04) | Active authorities over time; grants against revocations | FMCSA census file; analysts' extracts | Yes, but noisy: "Changes in assumptions, filters, and date of data collection can lead to differences among analyses". December 2025 revocations were "some 6,400 based on FTR's analysis or nearly 8,600, according to Trucking Dive's analysis" (N-B02, *verified*, new passage) | None |
| **Freight cycle depth and timing** (BTS Freight TSI, Cass Freight Index, PPI; N-C08 to N-C10, *verified* data) | Peak-to-trough of monthly volume or price series | FRED or BLS | Yes. Cass on FRED only from 2016 | None published |

**Worked example of S&P's method [our calc].** Transportation cyclical has revenue PTT 10.7%, which falls in the 8-13% band, and margin PTT 59.1%, in the 24-72% band. Table 2 gives **5**, matching S&P's own rating.
- For broker C.H. Robinson, revenue fell 11.7% (2008→09) and 28.7% (2022→23), an average of 20.2%. That is the 20-32% band, which lands between 2 and 6 depending on margins.
- Without margin data (which private SMB families do not publish), a desk test can place a family by revenue but cannot fix its S&P category.

**Verdict C2:** One published threshold set exists (S&P). Its bands are statistical clusters, not viability limits, and it was calibrated on large rated companies in economy-wide recessions. Census BDS gives a free, reproducible exit measure by 4-digit NAICS. FMCSA counts are the only licence-level measure, but analysts' results differ.

**Implications for S0:**
- Anchor any numeric K11 threshold to S&P's revenue bands (13% and 20% are natural lines) and state that the anchoring is **[our call]**.
- Use BDS for exits and note that it lags: the 2023 release is the latest found.
- Name which data source wins when sources disagree (C3, brokers).

---

### C3. Freight evidence by family

**Peak-to-trough changes (*verified* data; percentages **[our calc]**).**
- **Revenue:** from SEC filings (N-C12 to N-C16).
- **Prices:** the PPI (N-C08).
- **Jobs:** BLS employment, CES (N-C08).
- **Establishments:** QCEW (N-C07; its API has no 2006-11 files).
- **Exits:** Census BDS; each cell gives the firm death rate against the all-economy rate (N-C05).
- **Timing:** BDS "2009" means March 2008 to March 2009, and "2023" means March 2022 to March 2023.

| Family | 2008-09 | 2019-20 | 2022-25 | BDS firm deaths, 2009 / 2023 (economy 10.0% / 9.4%) |
|---|---|---|---|---|
| **All freight volume** (BTS TSI, seasonally adjusted) | -16.3% (Jan 2008 → Apr 2009) | -11.9% (Aug 2019 → Apr 2020) | -3.2% (Mar → Nov 2022), then flat between 134.7 and 139.3 into mid-2026 | — |
| **Brokerage** (488510) | C.H. Robinson revenue -11.7%; broker PPI -11.8% | PPI -12.8% | C.H. Robinson -28.7% (2023) and -34.3% by 2025. J.B. Hunt's brokerage (ICS) -55.1% from 2021 to 2025, with "Overall volumes decreased 26%" in 2023. PPI -32.7% (Dec 2021 → Aug 2023). FMCSA broker authorities -17.6% (Jan 2022 → end-2024, from N-B04). **But** QCEW establishments +8.4% (2022 → 2025) | 4885: **9.0% / 9.4%** (0.9× / 1.0×) |
| **Long-haul truckload** (484121) | Truckload PPI -11.5%; long-distance employment -15.9%; J.B. Hunt total revenue -14.2% | PPI -9.1% | PPI -24.1% (Mar 2022 → Nov 2024), then +29.5% by Aug 2026 (preliminary). Employment -11.4%. J.B. Hunt truckload segment -25.1% (2022 → 2024). Establishments -6.9% (2023 → 2025) | 4841 (all general freight): **16.6% / 19.4%** (1.7× / 2.1×) |
| **LTL** (484122) | Old Dominion revenue -19.0%; LTL PPI -9.1% | PPI -4.2% | Old Dominion -6.3% (2023) and -12.2% by 2025. PPI -11.8% (Jun 2022 → Apr 2023), then 18.6% above its 2022 peak by Aug 2026. LTL employment -10.6% (2022 → 2025) | Inside 4841; cannot be separated |
| **Specialized and local trucking** (4842, 48411) | Employment -14.9% (specialized), -15.8% (local general freight) | -9.9% / -7.7% | -5.0% / -7.4%. Establishments -3.4% / -5.2% (2023 → 2025) | 4842: **12.9% / 13.6%** (1.3× / 1.4×). Local general freight is inside 4841 |
| **Drayage and intermodal** | J.B. Hunt total -14.2% (proxy) | — | J.B. Hunt intermodal (JBI) -15.2% (2022 → 2024). Drayage firms are mostly local general freight (48411, *assumed* classification) | Proxy only |
| **Warehousing** (4931) | Employment -8.1% | -6.0% | Employment -6.1% (Mar 2022 → Jul 2023), then recovered. Establishments +9.7% (2022 → 2025) | **6.2% / 6.2%** (0.6× / 0.7×) |
| **Forwarding and customs** (in 488510) | Expeditors revenue -27.4% | Expeditors -2.4% (2018 → 19) | Expeditors -45.5% (2023): airfreight -44.9%, ocean -63.9%, **customs brokerage and other -20.5%** | Inside 4885 |
| **Couriers** (4921; fails K10 anyway) | Employment -16.5% | -6.2% | -9.2% | 12.5% / 11.9% (1.25× / 1.27×) |

**Other facts, all *verified*:**
- **2021-22 entrants were followed by 2023 exits, i.e. churn more than shrinkage.**
  - General freight trucking firms rose from 63,867 (2020) to 85,509 (2022), +33.9%, on establishment entry rates of 25.8% and 26.5%.
  - In 2023 firm deaths hit 19.4% while entries were 19.3%, and the firm count held at 85,244 (N-C05; **[our calc]**).
  - In 2008-09 the count fell 9.9%, from 48,538 (2007) to 43,726 (2010).
- **2008 failures, trade-press count (*assumed*: secondary report of Avondale Partners, via page extraction):** 785 trucking companies with about 39,000 trucks failed in Q3 2008 alone (N-C27).
- **Cass's clients are losing small carriers:** "carrier consolidation with small and medium-sized trucking companies exiting the market or selling to larger carriers continues to put downward pressure on financial fees as the smaller trucking companies were larger users of our quick pay solutions" (N-C15, 2025 10-K).
- **The data sources disagree on brokers.** FMCSA broker authorities fell 17.6%, while QCEW payroll establishments in 488510 rose 8.4% and BDS firms in 4885 rose from 13,619 (2021) to 14,019 (2023) **[our calc]**. The likely reason is that FMCSA counts licences, many of them non-employer or dormant, while QCEW and BDS count payroll businesses and include forwarders and customs brokers (*assumed* explanation).

**Major shipper groups.** S&P Table 6 gives average revenue PTT across recessions, with 2007-09 in brackets (N-C01, *verified*):
- **Defensive groups:**
  - health care services 0.0%;
  - pharmaceuticals -0.2% (-0.4%);
  - retail and restaurants -0.6% (-3.4%);
  - branded nondurables -1.1% (-3.8%);
  - containers and packaging -3.5% (-5.0%);
  - agribusiness and commodity foods -3.7% (-6.7%).
- **Middle:**
  - forest and paper -5.6% (-11.4%);
  - consumer durables -7.4% (-18.5%);
  - capital goods -7.7% (-21.8%);
  - building materials -8.0% (-16.9%).
- **Cyclical:**
  - auto manufacturers -16.5% (-30.7%);
  - downstream metals -17.4% (-34.3%);
  - homebuilders -20.1% (-44.5%).
- **For comparison:** transportation cyclical -10.7% (-17.3%); technology software and services -5.9% (-11.8%).

**Jobs documented as holding up or rising in downturns (*verified* unless marked):**
- **Auditing and paying freight bills.**
  - Cass, 2023: "Transportation invoice volumes decreased 2.3% ... primarily due to the on-going freight recession", while transportation dollar volumes fell 14.4%.
  - Invoice counts fell a cumulative 6.4% from 2022 to 2025 **[our calc]**.
  - Work counted per invoice held up far better than work counted per dollar (N-C15).
- **Customs brokerage.**
  - It "accounted for approximately 40% and 27% of Expeditors' total revenues in 2023 and 2022" (N-C13). It fell 20.5% against 45-64% for freight.
  - It grew 12.9% in 2025 as tariffs rose. Cass estimates tariffs added "approximately $600 million" to 2025 dollar volumes (N-C15).
- **Cargo theft and claims.**
  - 2024 saw "3,625 reported incidents representing a stark 27 percent increase from 2023".
  - The average value per theft rose to $202,364 from $187,895 (N-C23, via page extraction).
- **Detention** (trucks kept waiting at a customer's dock).
  - "In 2023, drivers reported being detained in 39.3 percent of all stops", costing "$3.6 billion in direct expenses and $11.5 billion in lost productivity" (N-C24).
  - Detention persisted through the downturn, but did not rise: a trade-press summary says it fell 6.5 points since 2014 (N-C29, *assumed*).
- **Dedicated contract trucking.** J.B. Hunt's dedicated segment (DCS) moved from $3,524M (2022) to $3,543M (2023), and was $3,376M in 2025 (N-C14).
- **Compliance work** was not measured here.

**Verdict C3:**
- **Revenue:** freight companies' revenue is highly cyclical, with double-digit falls in 2008-09 and 20-45% falls for brokers and forwarders in 2023. LTL and warehousing are the least cyclical families.
- **Exits:** general freight trucking stands out at twice the economy's firm death rate. Brokers, forwarders and warehouses sit at or below the economy.
- **The 2022-25 downturn** hit prices, not volumes, and followed an entry boom.
- **Several shipping jobs were steadier than the freight dollars around them:** invoices, customs, theft and claims, detention, and dedicated contracts.

**Implications for S0:**
- A family-level K11 would judge whole families on revenue that is mostly freight passed through to carriers.
- A job-level K11 tests what a fee would actually be counted on. It fits the card format "[shipping job] for [shipper group], handled today by [...]" (`submarket_selection.md` §2.2).

---

### C4. Software vendors through the 2022-25 freight downturn

| Vendor (what it sells; how it charges) | Customers' downturn | Vendor result (*verified*; % **[our calc]**) | Source |
|---|---|---|---|
| **Descartes** (logistics software; 90-93% "services revenues", i.e. recurring) | Shippers, carriers, forwarders, brokers | Revenue $486.0M (FY Jan 2023) → $572.9M → $651.0M → $729.0M, i.e. +17.9%, +13.6%, +12.0%. Part of the growth is acquisitions: in FY2025, acquisitions added $35.0M and existing and new customers $29.7M. Expects to "lose approximately 5% to 7% of our aggregate annualized recurring services revenues from the previous year in the ordinary course". Lists "a decline in shipment volumes" as a risk | N-C17, N-C12 |
| **WiseTech / CargoWise** (forwarder and customs software; "Only charge you when you use the software", N-A39) | Forwarders: Expeditors -45.5% | FY24 (to Jun 2024): "Total revenue of $1,041.7 million, up 28% (up 15% organically)". Organic CargoWise growth was "primarily driven by LGFF rollouts [large global forwarders], price increases ..." | N-C18 |
| **DAT** (load board, inside Roper; subscriptions) | Brokers and carriers | 2023: organic growth "led by ... freight match". 2024: "a decline in our businesses serving the ... freight match markets primarily related to end market conditions". 2025: growth again "led by ... freight match". Bought Trucker Tools in Dec 2024 | N-C19 |
| **Cass** (freight audit and payment; fees per invoice, plus float income on dollars) | Shippers' freight bills | Invoices -2.3% and dollars -14.4% in 2023. Total revenue rose 8.2% in 2023 on interest income. In 2025, "pressure on transportation related processing fees" | N-C15 |
| **SPS Commerce** (retail supply-chain EDI network; subscriptions) | Retail trading partners | Revenue grew every year from 2009 to 2025: $450.9M → $536.9M → $637.8M → $751.5M (2022-25), i.e. +19.1%, +18.8%, +17.8% | N-C12 |
| **Blend** (mortgage software; mostly per-transaction; a non-freight vertical in a volume collapse) | "From 2021 until 2023, annual mortgage originations declined 68.0%" | Software platform revenue -20.5% (2021 → 2023). In 2023, Mortgage Suite -18% and Title -58%; total -33% | N-C20 |
| **Uber Freight** (digital brokerage) | Brokerage | 2023: "Freight revenue decreased $1.7 billion, or 24%" ... "a consequence of the challenging freight market cycle"; 2025: -1% | N-C16 |
| **Convoy; Transfix** (digital brokers) | Brokerage | Convoy shut down in Oct 2023 (N-B29). Transfix sold its brokerage to NFI and now focuses "on powerful software and data solutions for brokers, shippers, and carriers" (5 Jun 2024) | N-B29, N-C26 |

**Investor writing on cyclical verticals.**
- **For resilience:**
  - SaaS Capital studied 16 public SaaS firms from 2006 to 2011. Growth fell "from 40% on average just prior to the recession, to 10%", and "Over 80% of the companies continued to grow through the recession" (N-C21, via page extraction).
  - Constellation on its own small vertical-software businesses in 2009: "we have grown our maintenance revenues organically, even during the recent recession"; "Attrition due to the loss of customers in 2009 was ~4%" (N-B12, letter covering 2009, *verified*, new passage).
  - Index Ventures: vertical software "often serves as the operating system for customers" (N-C22).
- **Against resilience:**
  - SaaS Capital: "Of the three public SaaS companies that actually shrank in the recession, one sold exclusively to auto dealers, one was a recruiting application, and one was an advertising platform"; the model "will not completely insulate businesses that ... sell into highly cyclical industries" (N-C21).
  - Constellation's homebuilder software: "Total Organic Growth has averaged -10% in each of the last two years", and group organic net revenue saw "a 3% contraction in 2009", its worst on record (N-B12).
  - Index Ventures: vendors "which serve more discretionary categories are likely to feel a crunch", and slow-to-implement products see purchases pushed "to a later date" (N-C22).
- **Gaps:** no investor source specific to restaurants or energy was found that this check could verify.

**Verdict C4: supported, with a clear condition.**
- Recurring software revenue fell much less than customers' revenue: every recurring freight-software vendor checked grew through 2022-25.
- Revenue tied to transactions or freight dollars fell with the cycle: Blend, Uber Freight, Cass's dollar-based fees, and DAT in 2024.
- Growth figures include acquisitions and price rises (Descartes, WiseTech), so they overstate resilience.
- These are survivors and large firms. A new entrant must also win new customers while budgets are frozen (R21, N-C22).

**Implications for S0:**
- Durability of *our* revenue depends partly on fee design, which is deferred.
- At sub-market level, K11 should check that the candidate has a countable unit that does not collapse in downturns. Invoices and filings passed in 2022-25; loads and freight dollars did not. That keeps the fee options open for later.

---

### C5. Making Constellation's churn test measurable at the desk stage

**The test (N-B12, letter on 2013, *verified*):**
- "By high churn, we mean that they acquire a greater proportion of new clients each year, and lose a higher percentage of existing accounts, than our average business."
- The two cases: churn because "switching costs are low" is "likely to be unpleasant". Churn because "lots of new potential clients are being created, and old ones are going bankrupt and merging" "may be very attractive".
- **Against:** the same letter says "the jury is still out on whether our high churn businesses are as attractive as our low churn businesses".

**A desk version in three steps [our call]:**
1. **Is the customer base replenishing?** From BDS for the side's 4-digit NAICS, compare the establishment exit rate with the entry rate in the latest year and in the worst downturn year, and check the firm count.
   - Entry ≥ exit, with a stable count, is Constellation's "being created ... going bankrupt" case.
   - Exit > entry for two years or more, with a falling count, means a shrinking pool.
   - **Freight examples (2023):**
     - general freight trucking: exit 19.3% against entry 19.3%, count flat;
     - brokers and forwarders: exit 10.5% against entry 9.0%, count 14,019 against 14,106 in 2022;
     - warehousing: exit 6.9% against entry 9.9% (N-C05).
2. **How much churn will exits alone cause?** Compare the customer firm death rate with incumbent vendors' ordinary attrition.
   - **Vendor benchmarks:** Descartes expects to lose 5-7% of recurring revenue a year (N-C17); Constellation's customer attrition was ~4% (N-B12).
   - **The rule:** a death rate of 10% or more, roughly twice the benchmark, means most expected logo churn is exits, not switching.
   - **Examples:** general freight trucking (19.4%) and specialized trucking (13.6%) are exit-driven; brokers (9.4%) are borderline; warehousing (6.2%) is not.
3. **What are the switching costs? (settled in S3 and S5).**
   - Desk proxy: Cohen's Enduring scale. "1.0: Strong lock-in from fiat, integrations, or being the system-of-record" against "0.5: Recurring-revenue from a recurring-problem" (R19, *verified*).
   - Interview question for S5: "what happened with your last software vendor: did you switch, or did it close?" This measures the split directly.

**Verdict C5:**
- Steps 1-2 are measurable in under an hour per candidate from one free CSV.
- Step 3 needs S3 and S5.
- Constellation's own caveat means passing the test shows a customer base that can support a business. It does not show the business is attractive.

**Implications for S0:** carry Steps 1-2 as the "customer survival" flag on each card (Option 2 in §3). Put Step 3 into the S3 fact sheet (item 8) and S5 interviews.

---

### C6. K11 options (summary; full table and worked example in §3)

Four candidate definitions, each a pass/fail test answerable in hours from named data **[our call]**:
1. **No structural decline** tests meaning (c).
2. **Customer firms survive downturns** tests (a) and (e) through exits.
3. **The job's countable unit holds up** tests (b), and the market side of (d).
4. **S&P-style revenue cyclicality** tests (a) and (e) through revenue, the way credit analysts do.

Unknowns go forward flagged, as the S2 rule already says (`submarket_selection.md` §4 S2).

**Verdict C6:** the options differ mainly in what they do to the pool:
- Option 1 removes nothing.
- Option 3 removes specific jobs.
- Option 2 removes most carrier-side families.
- Option 4 removes almost all freight-company-side families.

**Implications for S0:** the choice interacts with the founders' earlier direction toward fragmented SMB sides (D2, D3). Those sides are the ones Options 2 and 4 remove.

---

## 3. K11 options **[our call; for the founders to decide]**

| Option | Test (pass/fail) | Threshold | Desk data source (time per candidate) | Meaning tested |
|---|---|---|---|---|
| **1. No structural decline** (lenient) | The side's industry is not in long-term decline, and no named substitute removes the job within 5 years of launch | Pass if: BLS 10-year employment or output projection ≥ 0; census firms 2022 ≥ 2017 (R44); and no primary source shows a substitute operating at scale on the job. Fail if two of the three point to decline | BLS Table 2.11 (N-C11); R44; news and filings (about 1 hour) | (c) |
| **2. Customer firms survive** (moderate) | Customer exits in downturns are not far above the economy, and the population recovers | Pass if firm death rate ≤ 1.5× the economy in both BDS 2009 and 2023, **and** the firm count's peak-to-trough fall is ≤ 15%. Cross-check FMCSA; if it disagrees, mark "unknown" | BDS 4-digit CSV (N-C05); QCEW (N-C07); FMCSA (N-B04) (about 1 hour) | (a), (e) |
| **3. The job's unit holds up** (moderate, per job) | The countable unit the saving is measured in (invoices, loads, entries, claims, detained stops) holds up in downturns | Pass if the unit's peak-to-trough fall is ≤ 13% in each measured downturn, or it rose. Fail if > 20% in any. 13-20% or no data: unknown. Lines taken from S&P's revenue bands (N-C01) | Public volume lines (Cass, J.B. Hunt, Expeditors), BTS TSI, CargoNet, ATRI (1-3 hours) | (b); market side of (d) |
| **4. S&P-style revenue cyclicality** (strict) | The side's revenue is low-cyclical in credit-rating terms | Pass if average revenue peak-to-trough across 2008-09 and 2022-25 is ≤ 8% (S&P revenue bands 1-2). Fail above 13%. Between: unknown | Public comparables' 10-Ks (N-C12); S&P Table 6 for shipper groups (2-4 hours) | (a), (e) as revenue |

**Worked example: seven freight families and jobs (from C3; all figures *verified* data, judgements **[our call]**):**

| Family (and an example job) | Option 1 | Option 2 | Option 3 (example job) | Option 4 |
|---|---|---|---|---|
| Brokerage (cover truckload capacity for small shippers) | **Pass**: 488 support activities +4.6% projected; brokerage and forwarding firms 15,097 → 17,130 (R44); Convoy failed, so no digital displacement | **Unknown**: census passes (0.9× / 1.0×, count -4.8% in 2008-10); FMCSA fails (-17.6%) | **Fail** for load-based jobs: ICS volumes -26% (2023) | **Fail**: C.H. Robinson average -20.2% |
| Long-haul truckload (bill and collect detention) | **Pass**: 484 +2.1% projected; firms 31,908 → 53,705. Driverless trucks run on one Texas lane since 2025 (N-C25), a revisit trigger, not a fail | **Fail**: 1.7× / 2.1× the economy | **Pass** for detention: 39.3% of stops in 2023 while volume moved -3.2%. 2008-09 unknown | **Fail**: J.B. Hunt 2009 -14.2%, truckload segment -25.1% |
| LTL (fails K10 already) | **Pass** | **Fail** by code (4841); LTL alone unknown | Unknown: Old Dominion revenue -6.3% is a proxy, not a unit | **Fail**: Old Dominion average -15.6% |
| Specialized and local trucking | **Pass**: firms 46,282 → 52,012 | **Pass**: 1.3× / 1.4×; count -13.5% (2007 → 2011). Local general freight (4841) fails | Unknown: employment -14.9% (2008-09), -5.0% (2022-25), but no unit series found | Unknown: no public comparables |
| Warehousing (book dock appointments) | **Pass**: 493 +2.0% projected | **Pass**: 0.6× / 0.7× | **Pass** on the proxy: employment -8.1% / -6.1% | Unknown: no revenue comparables found |
| Forwarding and customs (clear import entries) | **Pass**: tariffs raised customs work in 2025 | **Pass** on census (4885); FMCSA does not cover forwarders | **Unknown**: customs revenue -20.5% is a revenue proxy; entry counts not checked | **Fail**: Expeditors average -36.5% |
| Shipper-side example: audit and pay freight bills for food and consumer-goods shippers | **Pass** | Not computed here (shipper NAICS); S&P shows food and branded goods among the least cyclical | **Pass**: invoices -2.3% (2023), -6.4% (2022-25); 2008-09 unknown | **Pass**: branded nondurables -1.1%, agribusiness -3.7% (S&P Table 6) |

**What each option does to the pool that can clear K5 **[our calc]**:**
- **Option 1:** nothing is removed.
- **Option 2:** removes carrier-side cards in general freight trucking (TL, LTL, local, drayage). That is 85,244 of the 127,465 employer firms in 4841 plus 4842 (about 67%, BDS 2023). Brokers (~14,000 firms) remain. Brokers alone clear the $25M K5 fee pool at about $1,800 a year per firm (14,000 × $1,786).
- **Option 3:** keeps every family, but removes jobs whose unit collapses. Per-load brokerage jobs fail; invoice, theft, detention and dock jobs pass. So it moves the choice from "which family" to "which job". The census data does not cover jobs, so K5 is unchanged at family level.
- **Option 4:** removes every freight-company-side family with data, which covers the fragmented SMB sides the founders favoured (D2, D3). What is left is shipper-side cards in defensive shipper groups (food, pharma, retail, branded goods, packaging).

**Suggested starting point, labelled as a suggestion, not a decision [our call]:**
- **K11 = Option 1 AND Option 3.** A fail needs clear evidence; unknowns go forward (S2 rule).
- **Record Option 2** on every card as a "customer survival" flag for S3 item 8 and for the C5 test, rather than a knock-out. Three reasons:
  - the data sources disagree for brokers;
  - Constellation's test says exit churn can be acceptable when entries replace exits;
  - code 4841 mixes TL, LTL and local carriers.
- **Keep Option 4** as the strictest case in the S4 sensitivity check (like the 40/45/15 comparison) and as a lens for S7.
- **Why this pair:** it tests the long-term existence of the market (c) and the durability of what a fee would be counted on (b). It stays neutral on fee design (d), which is deferred.

**What K11 also feeds:**
- **S7 revisit triggers (freight-rate cycle).** Series to watch **[our calc]** from N-C08 to N-C10:
  - the truckload PPI: +29.5% from its Nov 2024 trough by Aug 2026;
  - the LTL PPI: 18.6% above its 2022 peak;
  - the broker PPI: still 14.1% below its Dec 2021 peak;
  - Cass shipments: 2026 average so far 2.6% below 2025 (not seasonally adjusted);
  - the BDS annual release: the 2023 release was announced 25 Sep 2025, so a 2024 release is likely due (*assumed*);
  - FMCSA authority counts.

  Rates are recovering and volumes are flat. A rate rebound would re-test Option 3 for dollar-based units, not count-based ones.
- **O-2, re-splitting A7's 15 points.** Meaning (b) sits close to A5 (frequency and recurrence).
  - If K11 includes Option 3, putting A7's points on A5 would count the same thing twice. The UK manual on scoring against several criteria warns against this: "double counting should not be allowed" (N-B31).
  - If K11 is Option 1 only, most of the durability signal leaves both the knock-out and the score, and A5 is the natural place for it.
  - Either way, the balance check (R12) still needs a long-term row besides A6.

---

## 4. Open questions for the founders

1. **Which meanings of durability did you intend:** (a) customers survive, (b) the job persists, (c) no long-term decline, (d) our revenue doesn't swing? Also (e) ability to pay and (f) cycle timing? (d) is mostly fee design, which you deferred. Should K11 test only the market facts behind it?
2. **Family or job?** Should K11 judge a whole freight family (NAICS) or each card's shipping job? Options 1, 2 and 4 are family tests; Option 3 is a job test.
3. **Which side?** The entry side is deferred and scores use the better side (C5). Should a card pass K11 if either side passes, or must both?
4. **Which downturns count?** 2008-09 and 2022-25 only, or also 2019-20? And should a price-led downturn (2022-25) count the same as a volume-led one (2008-09)?
5. **Which data wins when sources disagree?** For brokers, FMCSA shows -17.6% while census shows growth. Payroll-firm counts (BDS, QCEW) or licences (FMCSA)?
6. **Thresholds:** relative to the economy (Option 2) or absolute (Options 3 and 4)? Are S&P's band edges (8%, 13%, 20%) acceptable anchors, knowing they are statistical clusters, not viability limits?
7. **Unknowns:** confirm they go forward flagged (the S2 rule), not treated as fails.
8. **A7's 15 points (O-2):** after choosing K11, where should they go, given the double-counting risk with A5?
9. **Revisit triggers:** which of the series in §3 should be dated triggers in S7?

---

## 5. Sources

### 5.1 New sources (N-C)

| ID | Source (author / org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-C01 | *General Criteria: Methodology: Industry Risk* (Standard & Poor's) | 19 Nov 2013 (copy hosted by S&P Maalot, with later Appendix IV change notes) | https://www.maalot.co.il/Publications/MT20161215151239.pdf | full PDF text | ¶5-37; Tables 1-6; Appendices I-II. Whether the bands changed after this copy was not checked (*assumed* unchanged; see N-C03) |
| N-C02 | *Key Credit Factors For The Transportation Cyclical Industry* (Baggaley et al., S&P) | 12 Feb 2014 | https://maalot.co.il/publications/MT20150607142115.pdf | full PDF text | ¶11-32, 50, 62-65 |
| N-C03 | *Corporate Methodology* (S&P Global Ratings) | 7 Jan 2024 | https://www.maalot.co.il/Publications/MT20240214173645.PDF | partial | ¶15, 21; guidance on p. 81 pointing to the Industry Risk Appendix 1 |
| N-C04 | *Which industries are sensitive to business cycles?* (Jay Berman, Janet Pfleeger), *Monthly Labor Review* 120(2), pp. 19-25 | Feb 1997 | https://www.bls.gov/mlr/1997/02/art2full.pdf | full PDF text | method, Table 1, Exhibit 2 |
| N-C05 | Census Business Dynamics Statistics, 2023 release: `bds2023_vcn4.csv`, `bds2023.csv`, and the codebook | release announced 25 Sep 2025 | https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/ ; https://www.census.gov/content/dam/Census/programs-surveys/business-dynamics-statistics/codebook-glossary.pdf | full (CSV filtered locally; codebook text) | 4841, 4842, 4885, 4931, 4921 and all-economy rows, 2005-2023; definitions of firm death, exit rate and the March 12 timing. The API now needs a key, so the CSVs were used |
| N-C06 | BLS Business Employment Dynamics, Table 7: survival, transportation and warehousing | current table | https://www.bls.gov/bdm/us_age_naics_48_table7.txt | via page extraction (curl blocked by BLS) | cohorts 2005-2010, 2012, 2014-2024. The all-private table is N-A24, with new cohorts read (2008, 2014, 2021-2024) |
| N-C07 | BLS QCEW open data, annual averages, US private | 2018-2025 | https://data.bls.gov/cew/data/api/{year}/a/industry/{code}.csv | full for 2018-2025; **2006-2011 files not served** | establishments and employment for 484110, 484121, 484122, 4842, 488510, 4931, 4921 |
| N-C08 | BLS Public Data API v1: PPI PCU484121484121, PCU484122484122, PCU488510488510; CES CES4348400001, CES4348411001, CES4348412001, CES4348420001, CES4349200001, CES4349300001 | Jan 2005 - Aug 2026 (latest months preliminary) | https://api.bls.gov/publicAPI/v1/timeseries/data/ | full | peak-to-trough windows computed locally |
| N-C09 | BTS Freight Transportation Services Index (FRED TSIFRGHT, seasonally adjusted) | Jan 2006 - Jun 2026 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=TSIFRGHT&cosd=2006-01-01 | full CSV (curl timed out; saved via the fetch tool, then parsed) | peak-to-trough |
| N-C10 | Cass Freight Index: Shipments (FRED FRGSHPUSM649NCIS; not seasonally adjusted) | Jan 2016 - Aug 2026 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=FRGSHPUSM649NCIS | **partial**: FRED file starts in 2016, so no 2008-09 | annual averages computed locally |
| N-C11 | BLS Employment Projections, Table 2.11 *Employment and output by industry, 2025 and projected 2035* | 2026 | https://www.bls.gov/emp/tables/industry-employment-and-output.htm | via page extraction | rows 484, 488, 492, 493 and total. Output units were not re-checked |
| N-C12 | SEC XBRL company facts: C.H. Robinson, Expeditors, J.B. Hunt, Old Dominion, Cass, SPS Commerce, Descartes, Uber | FY2007-FY2025 | https://data.sec.gov/api/xbrl/companyfacts/ | full | annual revenue |
| N-C13 | Expeditors 10-Ks for FY2023 (filed 23 Feb 2024) and FY2025 (filed 25 Feb 2026) | 2024, 2026 | EDGAR: expd-20231231.htm, expd-20251231.htm | full text, searched | revenue by service; customs share |
| N-C14 | J.B. Hunt 10-Ks for FY2023 (23 Feb 2024) and FY2025 (24 Feb 2026) | 2024, 2026 | EDGAR: jbht20231231_10k.htm, jbht20251231_10k.htm | full text, searched | segment revenue; ICS volumes |
| N-C15 | Cass Information Systems 10-Ks for FY2023 (28 Feb 2024) and FY2025 (6 Mar 2026) | 2024, 2026 | EDGAR: cass-20231231.htm, cass-20251231.htm | full text, searched | invoice and dollar volumes; freight-recession and consolidation text. Revenue levels differ between the two filings (restated), so only text and volumes are used |
| N-C16 | Uber 10-Ks for FY2023 (15 Feb 2024) and FY2025 (13 Feb 2026) | 2024, 2026 | EDGAR: uber-20231231.htm, uber-20251231.htm | full text, searched | Freight segment text |
| N-C17 | Descartes Form 40-F exhibits: FY2024 annual information form (ex99-1, filed 22 Apr 2024) and FY2026 MD&A (ex99d2, filed 11 Mar 2026) | 2024, 2026 | EDGAR: tm242227d1_ex99-1.htm; dsgx-20260131xex99d2.htm | full text, searched | revenue by source; 5-7% attrition; risk text |
| N-C18 | *WiseTech delivers strong financial performance and outlook*, FY24 ASX release (WiseTech Global) | 21 Aug 2024 | https://www.wisetechglobal.com/media/ritbv4l3/wtc-fy24-asx-release.pdf | full (5 pp.) | revenue, organic growth, drivers |
| N-C19 | Roper Technologies 10-Ks for FY2023, FY2024, FY2025 | 2024-2026 | EDGAR: rop-20231231.htm, rop-20241231.htm, rop-20251231.htm | full text, searched | Network Software organic growth and freight-match text; Trucker Tools |
| N-C20 | Blend Labs 10-K for FY2023 | filed 14 Mar 2024 | EDGAR: blnd-20231231.htm | full text, searched | revenue table; mortgage-volume text |
| N-C21 | *How Do SaaS Companies Perform in a Recession?* (Rob Belcher, SaaS Capital) | 10 Sep 2018 | https://www.saas-capital.com/blog-posts/how-do-saas-companies-perform-in-a-recession/ | via page extraction | sample, growth, the three that shrank |
| N-C22 | *Vertical Software Wins in Bull and Bear Markets* (Nina Achadjian, Index Ventures) | 22 Jul 2022 | https://www.indexventures.com/perspectives/vertical-software-wins-in-bull-and-bear-markets/ | via page extraction | downturn passages |
| N-C23 | *2024 Supply Chain Risk Trends Analysis* (Verisk CargoNet) | 21 Jan 2025 | https://www.cargonet.com/news-and-events/cargonet-in-the-media/2024-theft-trends/ | via page extraction (the Verisk release page did not render) | incidents, value per theft. The loss totals and "strategic theft" shares seen in snippets are *assumed* and not used |
| N-C24 | *New Research Documents Substantial Financial and Safety Impacts from Truck Driver Detention* (ATRI) | 10 Sep 2024 | https://truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/ | via page extraction | detention share and costs. A fee-collection figure (fees "collected on fewer than half" of invoices) came only as a page summary: *assumed*, not used |
| N-C25 | *Aurora Begins Commercial Driverless Trucking in Texas* (Aurora Innovation) | 1 May 2025 | https://ir.aurora.tech/news-events/press-releases/detail/119/aurora-begins-commercial-driverless-trucking-in-texas-ushering-in-a-new-era-of-freight | via page extraction | launch sentence; planned routes |
| N-C26 | *NFI Acquires Transfix Brokerage, Transfix Launches SaaS Platform* (Transfix) | 5 Jun 2024 | https://transfix.io/press/nfi-buys-brokerage-business-unit-of-transfix | via page extraction | sale; software focus |
| N-C27 | *Nearly 800 Trucking Companies Out of Business Due to Recession* (Work Truck Online, citing Avondale Partners) | 8 Jan 2009 | https://www.worktruckonline.com/63200/nearly-800-trucking-companies-out-of-business-due-to-recession | via page extraction; secondary | Q3 2008 failures (*assumed*) |
| N-C28 | *Surface Transportation and Logistics* methodology (Moody's) | undated | https://ratings.moodys.com/api/rmc-documents/360641 | **blocked** (login page) | nothing; a snippet says cyclicality is considered (*assumed*) |
| N-C29 | *New study shows detention improving slightly but still pervasive* (FreightWaves) | 2024 | https://www.freightwaves.com/news/new-study-shows-detention-improving-slightly-but-still-pervasive | search snippet only | detention -6.5 points since 2014 (*assumed*) |

### 5.2 Earlier sources reused
R12, R19, R21, R25, R34, R38, R43 and R44 (reading notes, not re-read). N-A24, N-A39 and N-B31, reused. N-B02 and N-B04 reused; N-B02 was re-opened for new passages on data differences and December 2025 revocations. N-B03 and N-B29 reused. N-B12 (Constellation letters): the PDFs covering 2009, 2013 and 2015 were re-downloaded for new passages on recession attrition, homebuilder software and the churn caveat.

### 5.3 Could not access, or used only second-hand
- **Moody's methodology** (login required): no Moody's thresholds.
- **S&P revisions after the 2013 criteria copy:** not checked.
- **Cass Freight Index before 2016:** FRED's file starts in 2016, and the cassinfo.com archive was not tried. So there is no 2008-09 Cass depth; the BTS TSI is used instead.
- **QCEW 2006-2011:** not served by the open-data API.
- **BLS pages:** they block curl, so BLS survival and projection tables were read via page extraction.
- **Verisk's own 2024 cargo-theft release** did not render; CargoNet's page was used instead.
- **Trimble's transportation segment:** not extracted, so it is not used.
- **CBP customs-entry counts:** not checked, so Option 3 for customs stays "unknown".
