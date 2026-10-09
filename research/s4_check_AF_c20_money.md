# S4 check AF: the money in an import entry, for C-20's per-customer model

- **What this is:** new desk research for **S4 step 7** (process change C22, the per-customer profit model and kill condition) in run 01, for **C-20: import entries, prepared for small importers by small customs brokerages' entry writers**. It gathers the inputs for the chain the coordinator will build:

  > fee per brokerage = formal entries a year × minutes saved per entry × loaded wage per minute × fee share (or entries × a per-entry price, capped by the labour saved)
  > gross profit = fee − cost to serve

  It answers AF1-AF8 from the brief.
- **Date:** 2026-09-22. Everything new here was accessed on 2026-09-22.
- **Status:** input to S4 step 7. **It decides nothing.** It sets no price, picks no segment, re-scores nothing and writes no kill condition. Every reading is **[our call]** and sits in §10.
- **Not redone here** (cite by ID): the 23,133,408 electronic formal entries at 5 minutes (N-N05); formal entries FY2023-FY2025 (N-H22); informal entries after de minimis (N-H22); 15,226 licensed and 2,365 permitted brokers in 2022 (N-F08); NCBFAA's 1,500+ members (N-S26); ~70 ABI vendors and NetCHB's 700+ brokers (N-F10, N-S09); broker fees of $100-250 from vendor guides; BLS headline wages for 43-5011 and 13-1041 in NAICS 4885 (N-S01); the Descartes survey (N-S20); IEEPA and refund dates (N-S05, N-S06); the World Bank $100 cost; the permitted-broker CSV's existence (check V). The loaded-wage method (wages = 70.0% of compensation, ECEC Q2 2026) is N-AA40; machine-reading prices are N-AA02 and N-AA12-N-AA17.
- **Labels:**
  - *verified*: read at the source (statute, Federal Register, government data file, court or DOJ release, SEC filing or earnings release page). **A published price list read on the seller's own page is *verified* as the price offered** (what a given customer actually pays may differ).
  - *assumed*: a vendor's performance or time-saved claim (**always**, even when read in full on the vendor's own page), an association figure, an analyst-report summary, a search snippet, a secondary summary, a blocked page.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
- **New source IDs:** N-AF01 to N-AF63 (§11). Vendor figures are kept in separate rows or tables from neutral ones.

**Words used here:**
- **CBP:** US Customs and Border Protection. **ACE:** its Automated Commercial Environment, the system every entry goes into. **ABI:** Automated Broker Interface, the electronic link brokers' software uses to file in ACE.
- **Entry / entry summary (CBP Form 7501):** the filing that declares imported goods, their tariff classification, value and duty. A **formal entry** is required above $2,500 of value (and for some goods below it). An **informal entry** covers $800-2,500 (type 11) (UPS's summary of CBP's rule, N-AF18). **Type 86** was the low-value (de minimis) entry for goods up to $800, now closed.
- **Cargo release (CBP Form 3461 or "ACE Cargo Release"):** the earlier filing that gets goods released; the entry summary follows within 10 working days.
- **ISF ("10+2"):** Importer Security Filing, data sent before an ocean container is loaded abroad.
- **HTS / HTSUS:** Harmonized Tariff Schedule of the United States. **Classification** = choosing the 10-digit HTS number for each product. **Line:** one HTS number (per product and country of origin) on an entry; one invoice can need many lines.
- **Filer code:** the 3-character code CBP gives each broker or self-filing importer. **Permitted broker:** a licensed broker (person or company) holding the permit that lets it do business; since 2022 one national permit per broker.
- **Self-filer:** an importer that files its own entries through ABI without a broker.
- **Entry writer:** the broker's employee who keys the entry. **Licensed customs broker:** the person who passed CBP's exam and supervises.
- **PRA burden statement:** under the Paperwork Reduction Act, CBP must publish how many people fill a form and how long it takes them ("Estimated Time per Response").
- **RIA / RFA:** a rule's Regulatory Impact Analysis and its Regulatory Flexibility Act (small-business) analysis.
- **MPF:** Merchandise Processing Fee, a CBP fee of 0.3464% of value (FY2026 minimum $33.58, maximum $651.50), not a broker fee.
- **Net revenue (freight forwarders):** revenue minus the freight and third-party costs passed through; the part the firm keeps to pay staff and profit.

---

## 1. Summary inputs table

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Entry filers (formal, electronic)** | — | **2,336 filers, 9,903 entries each on average** (23,133,408 total) | — | *verified* (CBP estimate) | N-AF03, N-AF04 |
| Permitted brokers, March 2025 | — | **2,407 rows, one filer code each**; about 730 rows carry a person's name | — | count *verified*; person-name split **[our calc]** | N-AF01 |
| **Formal entries a year, pure brokerage of 1-4 staff** | 1,300 | 1,500 | 1,800 | **[our calc]** from Census payroll, a 50-60% labour share and a $125-150 fee | N-AF12, N-AF13, N-AF21 |
| Same, 5-9 staff | 5,200 | 6,300 | 7,400 | **[our calc]** | same |
| Same, 10-14 / 15-19 / 20-49 staff | 8,900 / 13,200 / 17,000 | — | 12,900 / 19,000 / 54,000 | **[our calc]** | same |
| **Filers above 1,000 / 5,000 / 20,000 entries a year** | 890 / 320 / 90 | ~1,200 / ~480 / ~120 | 1,610 / 670 (≈900 on a bound that overshoots the national total) / 165 (≈310) | **[our call]** shape; **[our calc]** | §2.5 |
| Concentration at the top | Deringer "over a million entries annually" | FedEx + UPS "almost 35%" of the market; top five ~42% | "top 10 ... roughly 60%" (unsourced) | *assumed* | N-AF53, N-AF54, N-AF55, N-AF56 |
| Concentration, low-value channel (type 86, FY2021-22) | 496 of 530 filers had 0.10% of volume | 27 filers had 19.30% | **7 filers had 80.39%** | *verified* (CBP data in CBP's RIA) | N-AF08 |
| **Minutes per formal entry, government** | 5 (7501 transmission) | **10** ("the time required to complete a formal entry is approximately 10 minutes") | 60 (ISF, including the importer's data gathering) | *verified* (CBP/IEc estimates) | N-AF03, N-AF06, N-AF07, N-AF08 |
| Minutes per formal entry, vendors | 20 | 45-60 | 90+ complex; 6 hours for 400-600 lines | *assumed* | N-AF45, N-AF46, N-AF47 |
| **Classification + keying share of entry time** | ~45% (classification 10-15 + entry prep 10-15 of 43-65 min) | — | 75% keying + 25% classification (all "decision" time) | *assumed* | N-AF45, N-AF46 |
| Classifying a new, simple product (a broker's own figure) | 2 min | 3 min | 4 min ("1 to 2 hours to vet 30 simplified, non-ambiguous products") | *verified* as reported in CBP's RIA; minutes **[our calc]** | N-AF08 |
| **Wages, 43-5011 cargo and freight agents, NAICS 4885, May 2025** | $18.72/h (10th pct) | **$27.68/h mean** ($26.31 median) | $38.17/h (90th pct) | *verified* | N-AF11 |
| Loaded rate, same | $26.74/h | **$39.54/h = $0.659/min** | $54.53/h | **[our calc]** (÷ 0.70, N-AA40) | N-AF11 |
| Loaded rate, 13-1041 compliance officers (licensed brokers sit here), NAICS 4885 | $43.19/h (median) | **$49.74/h** (mean) | $60.71/h (national mean) | **[our calc]** on *verified* wages | N-AF11 |
| Loaded rates government analysts used | $36.57/h (CBP, for filers) | $52-63/h (a broker's own HTS-vetting cost) | $62.24/h (IEc, all NAICS 4885 staff × 2) | *verified* | N-AF04, N-AF08 |
| **What importers pay per formal entry (published lists)** | $89.95 (Clearit, truck) | $125 (U. of Iowa's average); $129.95-149.95 (Clearit air/ocean, 3 lines) | $100-250 (Strix full service); $100-200 (Iowa State) | *verified* (published) | N-AF21, N-AF22, N-AF24, N-AF25 |
| Price per extra line | $3.50 (FedEx, over 3 lines) | $5 (DHL, over 5 lines) | $15 (Clearit, per classification over 3) | *verified* (published) | N-AF20, N-AF19, N-AF21 |
| **What brokers pay for ABI software per entry** | $0.20 (CustomsCity, 10,000/month plan) | $0.50-1.52 (CustomsCity, 65-1,000/month) | **$9.95** (CargoWise, whole platform incl. AI, per import formal procedure) | *verified* (published) | N-AF29, N-AF30, N-AF33 |
| **Competitor AI tool prices** | $0.02-0.03 per AI extraction or HTS search (CustomsCity, top tiers) | $0.10-0.25 (CustomsCity, small tiers); $0.42-0.99 per Gaia credit | **$0 extra** inside CargoWise (AI Classification Assistant and invoice ingestion included) | *verified* (published) | N-AF31, N-AF32, N-AF36, N-AF35 |
| Self-filing software sold to importers | — | **$30 per entry + $500 onboarding** (Strix) | — | *verified* (published) | N-AF22 |
| **Margins / pricing power** | — | Expeditors "customs brokerage and other services": net revenue **44.0%** of revenue (2025) | C.H. Robinson customs gross profit per transaction **+26%** (Q4 2025) | *verified*; ratio **[our calc]** | N-AF13, N-AF15 |
| **Error cost** | Broker penalty cap **$30,000 in total** (19 U.S.C. 1641) | Importer negligence: up to **2× lost duties** (or 20% of dutiable value) | Gross negligence 4×; fraud up to domestic value; $54.4M misclassification settlement | *verified* | N-AF48, N-AF49, N-AF51 |
| **Self-filers** | — | **112** (CBP, 2015) | ≤3% of entries not handled by NCBFAA members | *verified* (2015); *assumed* (association) | N-AF10, N-AF05 |

**One-line reading [our call]:** the neutral numbers put a formal entry at 10 minutes of filer time and the market prices say an extra line is worth $3.50-15 to an importer, so a co-pilot's saving is a few dollars an entry; **the decisive new fact is that the three largest broker platforms and a low-price one now ship invoice extraction and classification suggestions themselves (CargoWise at no extra charge, CustomsCity at 2-25 cents)**, which caps the price well below the labour saved.

---

## 2. AF1 · Entries per brokerage

### 2.1 How many filers there are

| What | Figure | Where | Label |
|---|---|---|---|
| Formal entry summaries, electronic | "Estimated Number of Respondents: **2,336**. Estimated Number of Annual Responses per Respondent: **9,903**. Estimated Number of Total Annual Responses: 23,133,408. Estimated Time per Response: 5 minutes." Paper: 28 respondents, 277,284 responses, 20 minutes | 90 FR 46624-46625 (29 Sep 2025), OMB 1651-0022; same table in the supporting statement §12 (N-AF04) | *verified* (N-AF03) |
| Informal entry summaries, electronic | 1,883 respondents × 2,582 = 4,861,906 responses, 5 minutes | same | *verified* (N-AF03) |
| Permitted brokers, March 2025 | **2,407 rows**, columns "Filer Code, Permitted Broker Name, City, State, Work Phone, Extension, Email". Every row has a distinct filer code and a distinct name, so **rows are firms (or sole proprietors), not permits** | CBP CSV "TA-015 Broker Permit_Contact List Final 03.2025" (downloaded with a plain client, no identity) | *verified* (N-AF01) |
| Of which named for a person | About **730** rows are a person's name with no business word (e.g., "Daniel L. Vesque"); about 1,677 are company names | name heuristic | **[our calc]** |
| By state | CA 540, TX 473, NY 362, FL 278, IL 121, NJ 106, GA 63, WA 43 | same CSV | *verified* |
| Big names present | One filer code each for, among others, UPS Supply Chain Solutions (2 codes), FedEx (3 entities), DHL Express, Expeditors (4 incl. Tradewin), Livingston (3), C.H. Robinson, Kuehne + Nagel, DSV, Flexport Customs, A.N. Deringer, Amazon Logistics, Clearit (8PY), Strix (8ND) | same | *verified* |
| Permitted brokers, January 2022 | "there are 2,365 permitted brokers holding a combined total of 3,345 active district permits. These 2,365 brokers represent about 15.5 percent of all brokers ... Approximately two percent of brokers hold a corporate permit, meaning 13.5 percent of brokers hold individual permits" | 87 FR 63299 (18 Oct 2022) | *verified* (N-AF02) |
| Licensed brokers | "approximately 16,170 active licensed Customs brokers" (CBP FAQ, today) against 15,226 in Jan 2022 | CBP broker FAQ | *verified* as stated (N-AF57) |
| NCBFAA | "more than 1,400 member companies with over 110,000 employees ... serving more than 250,000 importers and exporters. The Association's members handle more than 97% of the entries" | NCBFAA comment letter to CBP, 31 Dec 2025 | *assumed* (association figure, read at source) (N-AF05) |

**A puzzle we could not settle [our call]:** CBP's 2022 split (≈2% of 15,226 brokers ≈ 305 corporate permits, ≈13.5% ≈ 2,055 individual permits **[our calc]**) does not match the 2025 list, where about 1,677 of 2,407 names are companies. The likeliest reading is that many individual permit holders trade under a business name, but the documents do not say. It does not change the count of about 2,300-2,400 filing firms.

### 2.2 Concentration: who files most entries

| Evidence | Figure | Label |
|---|---|---|
| **Type 86 (low-value) entries, CBP's filer data FY2021-22** (IEc for CBP, Table 4-1, p. 4-3) | Low volume (0-100,000 a year): **496 filers, 0.10%** of volume; medium (100,000-10 million): **27 filers, 19.30%**; high (10-150 million): **7 filers, 80.39%**. "Although the most brokers fall into the 'low volume' bin, combined they only account for 0.10 percent" | *verified* (N-AF08). **This is the de minimis channel, not formal entries**, and it has closed; it shows how skewed filer volume can be |
| A.N. Deringer | "the largest privately-held US Customs broker and one of the top five entry filers in the US—filing over a million entries annually" | *assumed* (company page) (N-AF53) |
| Research and Markets (2021) | "FedEx and UPS together account for almost 35% of the total market"; market "more than USD 4 billion" (a search snippet adds "based on the number of entries"; the Yahoo copy does not) | *assumed* (analyst summary) (N-AF54) |
| Mordor Intelligence (2026) | market USD 5.48 billion in 2026; "the top five firms controlling approximately 42% combined share" (share basis not stated) | *assumed* (N-AF55) |
| Unsourced snippet | "The top 10 customs brokers ... handle roughly 60% of all import entries ... over 20 million entries annually out of approximately 34 million" | *assumed*; no source named (N-AF56) |

**No public source gives formal entries by filer.** CBP holds it (the RIA above used "volume by filer data" provided by email) but does not publish it.

### 2.3 The industry's size structure (brokers sit inside it)

Census SUSB 2022 (released 10 Apr 2025), NAICS 488510 Freight Transportation Arrangement, which holds forwarders, ship agents and customs brokers together (N-AF12, *verified*):

| Enterprise size | Firms | Employment | Staff per firm **[our calc]** | Annual payroll ($1,000) | Payroll per firm **[our calc]** | Receipts per firm **[our calc]** |
|---|---|---|---|---|---|---|
| <5 employees | 9,675 | 16,387 | 1.7 | 1,095,834 | $113k | $1.14M |
| 5-9 | 2,504 | 16,697 | 6.7 | 1,161,206 | $464k | $3.55M |
| 10-14 | 1,016 | 11,826 | 11.6 | 817,443 | $805k | $6.39M |
| 15-19 | 559 | 9,327 | 16.7 | 664,558 | $1,189k | $8.45M |
| 20-49 (five bands) | 1,062 | 30,691 | 28.9 | 2,302,158 | $2,168k | — |
| 50-499 | 775 | 82,125 | 106 | — | — | — |
| 500+ | 261 | 158,664 | 608 | — | — | — |
| **Total** | **15,852** | **323,348** | 20.4 | 24,269,442 | $1,531k | $8.15M |

Receipts include freight passed through to carriers, so receipts per firm overstate a brokerage's own revenue. About 2,400 of the 15,852 firms (≈15% **[our calc]**) are permitted brokers.

### 2.4 Entries a year for a small brokerage (derived)

No public source states entries per brokerage by staff size (§12). The bracket below is **[our calc]** from three documents:

- a pure customs brokerage's staff are paid out of entry fees, so **revenue ≈ payroll ÷ labour share**;
- the **labour share is taken as 50-60%** of revenue **[our call]**, anchored on Expeditors, whose salaries were **52.2%** of its net revenue in 2025 ($1,915.9M ÷ ($11,069.0M − $7,402.1M)) **[our calc]** from N-AF13;
- **entries = revenue ÷ fee**, with the fee at **$125-150** (U. of Iowa's reported average $125; Clearit's published $129.95-149.95 air/ocean, N-AF24, N-AF21).

| Brokerage size (if it were a pure brokerage) | Payroll per firm | Implied entries a year | Entries per employee per working day (250 days) |
|---|---|---|---|
| 1-4 staff (avg 1.7) | $113k | **1,300-1,800** | 3.0-4.3 |
| 5-9 staff (avg 6.7) | $464k | **5,200-7,400** | 3.1-4.4 |
| 10-14 staff (avg 11.6) | $805k | **8,900-12,900** | 3.1-4.4 |
| 15-19 staff (avg 16.7) | $1,189k | **13,200-19,000** | 3.2-4.6 |
| 20-49 staff | $1.5-3.4M | **17,000-54,000** | — |

**Cross-checks [our calc]:** (1) CBP's national average, 9,903 entries per filer, sits in the 10-14-staff band. (2) Three to four entries per employee per day is consistent with the vendor figure of "10 to 12 entries per day" per entry writer (N-AF46, *assumed*) if roughly a third of staff write entries.

### 2.5 How many filers exceed 1,000 / 5,000 / 20,000 entries

Two methods, both **[our call]** on shape, shown so they can be challenged:

**A. Keep CBP's total and assume a skewed spread.** Take CBP's 2,336 filers and 23.13M entries; give the top 10 filers 35%, 50% or 60% of entries (the §2.2 range); spread the rest across 2,326 filers on a log-normal curve with a spread (σ) of 1.5 or 2.0 **[our call]**:

| Top-10 share | σ | Mean of the rest | Median of the rest | >1,000 | >5,000 | >20,000 |
|---|---|---|---|---|---|---|
| 35% | 1.5 | 6,465 | 2,099 | 1,614 | 665 | 165 |
| 35% | 2.0 | 6,465 | 875 | 1,111 | 456 | 147 |
| 50% | 1.5 | 4,973 | 1,614 | 1,464 | 535 | 119 |
| 50% | 2.0 | 4,973 | 673 | 990 | 377 | 115 |
| 60% | 1.5 | 3,978 | 1,292 | 1,331 | 437 | 89 |
| 60% | 2.0 | 3,978 | 538 | 890 | 318 | 92 |

**B. Assume brokers are sized like all NAICS 488510 firms** (61% under 5 staff, 16% 5-9, 17% 10-49, 6.5% 50+) and use §2.4's entries per band: about 1,430 filers under 5 staff, **≈910 above 5,000** and **≈310 above 20,000** **[our calc]**. But this adds up to roughly 40M+ entries, almost twice CBP's 23M, so **brokers must be smaller than the average NAICS 488510 firm, and method B is an upper bound only** **[our call]**.

**Result [our calc]:** roughly **900-1,600 filers above 1,000 entries, 320-670 above 5,000 (upper bound ~900), and 90-165 above 20,000 (upper bound ~310)**. Self-filers are inside the 2,336 (§9).

---

## 3. AF2 · Minutes per entry, and where they go

### 3.1 Government burden estimates (neutral, but mostly transmission time)

| Filing | Respondents | Responses | **Time per response** | Where | Label |
|---|---|---|---|---|---|
| Entry summary 7501, electronic | 2,336 | 23,133,408 | **5 minutes** | 90 FR 46624 | *verified* (N-AF03) |
| 7501, paper | 28 | 277,284 | 20 minutes | same | *verified* |
| 7501 with Softwood Lumber Act (paper) | 210 | 400,050 | 40 minutes | same | *verified* |
| ACE Cargo Release / ABI (3461 data) | 9,810 | 29,832,210 | **10 minutes** | 90 FR 55155-55156 (1 Dec 2025), OMB 1651-0024 | *verified* (N-AF06) |
| **Importer Security Filing** | **240,000** | 8,100,000 | **1 hour** | 91 FR 40020 (1 Jul 2026), OMB 1651-0001 | *verified* (N-AF07) |
| CBP's own review of each entry summary | — | 28,727,906 | **0.166 hours (10 min)** at $84.17/h = $401.4M a year, **$13.97 per entry summary** **[our calc]** | 7501 supporting statement §14 | *verified* (N-AF04) |

**CBP's RIA for the low-value rule** (prepared by Industrial Economics, Inc., 13 Jan 2025; N-AF08, *verified* as the document states it):

- p. 4-18, footnote 78: "For reference, **the time required to complete a formal entry is approximately 10 minutes**."
- p. 4-20: "CBP estimates the total amount of time required to submit this paperwork [Form 3461] is 10 minutes per shipment ..., representing the time of both brokers and consignees. In the absence of data disaggregated by entity, we assume half of this time (5 minutes) is incurred by brokers."
- p. 4-17, classification of new products, from a high-volume broker: "it takes **1 to 2 hours to vet 30 simplified, non-ambiguous products** and ... this vetting can cost **$50 to $60 per hour** in 2022 dollars ($52 to $63 per hour in 2023 dollars)" → **2-4 minutes and $1.73-4.20 per simple new product** **[our calc]**. "This process can take longer if the product descriptions are ambiguous."
- p. 4-17, on reuse: "By entering these HTSUS codes into a database, they would not need to be re-checked each future time the same product is shipped." Two medium-volume brokers said clients "typically provide HTSUS codes ... [that] tend to be outdated or inaccurate", so they review and reassign them, "neither broker was able to offer a quantitative estimate".

**World Bank Doing Business 2020, United States, import:** documentary compliance **8 hours** and **$100**; border compliance 2 hours and $175 (N-AF60, *verified*). These are elapsed hours, not staff minutes.

**Reading [our call]:** the government figures price the **act of filing** (5-10 minutes) and treat preparation as small. They are the low end for a co-pilot's saving. None measures an entry writer's full preparation time.

### 3.2 Vendor and trade-press figures (all *assumed*)

| Source | Manual | With automation | Breakdown | Label |
|---|---|---|---|---|
| SocialVik blog, "Manual Customs Documentation" (21 May 2026; US, "operational data from brokerage software providers") | **45-60 min** per clean shipment; **90+ min** complex; **10-12 entries per day** per writer | 20-25 entries per day | document collection 8-12; **HS classification 10-15**; value 5-8; ISF 5-7; **ACE entry prep 10-15**; summary/duty 5-8 | *assumed* (N-AF46) |
| FreightMynd, "AI for Customs Brokers" (28 Mar 2026, CEO) | **20-40 min** per declaration | **5-12 min** of broker time; "70% reduction" | "six hours keying data and two hours on classification decisions" (75/25) | *assumed* (N-AF45) |
| Docxster blog (14 Aug 2026), a broker quoted | "10 people working on 400, 500, 600-line items, and it takes 2 to 3 days sometimes ... get it done in six hours, transmit, get a kickback for errors ... That's another four hours" | — | — | *assumed* (N-AF47) |
| Magaya, Broker AI Assistant (18 Feb 2025) | "What used to take several minutes per line item..." | "...is reduced to seconds" | — | *assumed* (N-AF40) |
| TariffLens | "Classification time reduced from 30 minutes to 30 seconds" | — | — | *assumed* (N-AF43) |
| Descartes GM (18 Aug 2026) | "Entering commercial invoice data is one of the most labor-intensive activities in the import process, especially when shipments include complex commercial invoices with hundreds of line items" | — | — | *assumed* (N-AF41) |
| Expedock | "5-10 minutes for each invoice" saved | — | — | *assumed*, snippet (N-AF63) |

**Classification + keying share [our calc]:** SocialVik's classification (10-15) plus entry prep (10-15) = **20-30 of 43-65 minutes ≈ 45%**; FreightMynd puts all of the manual time in keying (75%) and classification (25%).

### 3.3 What was not found

- **Lines per entry** (average HTS lines on a formal entry): not published by CBP (§12). A proxy: price lists include **3 lines** (Clearit, FedEx) or **5 lines** (DHL) in the base fee, which suggests most small entries are short **[our call]**.
- **Share of a repeat importer's lines already classified** (product-database reuse): no figure. The RIA's qualitative statements above, and CargoWise's "linking Customs data to Products allows easy classification of Commercial Invoice Lines for regular Products" (snippet, N-AF35), say reuse is normal practice.
- Job postings stating entries per day: postings found (Mallory Alexander, FNS, CareerBuilder listings) gave none, or had expired.

---

## 4. AF3 · Wages

### 4.1 BLS OEWS May 2025 (N-AF11, *verified*; read from BLS's own May 2025 Excel files, `oesm25nat.zip` and `oesm25in4.zip`)

| Occupation | Where | Employment | Mean $/h | Median $/h | 10th / 90th pct $/h | Annual mean | **Loaded $/h (÷ 0.70)** **[our calc]** |
|---|---|---|---|---|---|---|---|
| 43-5011 Cargo and freight agents (entry writers are classed here) | **NAICS 4885** | 53,390 | **27.68** | 26.31 | 18.72 / 38.17 | $57,570 | **39.54** (median 37.59; 10th 26.74; 90th 54.53) |
| 43-5011 | all industries | 97,670 | 27.52 | 25.13 | 18.43 / 38.37 | $57,230 | 39.31 |
| 13-1041 Compliance officers (licensed brokers) | **NAICS 4885** | 4,520 | **34.82** | 30.23 | 21.64 / 56.20 | $72,420 | **49.74** (median 43.19) |
| 13-1041 | all industries | 417,070 | 42.50 | 38.81 | 23.18 / 64.29 | $88,400 | 60.71 |
| 43-9021 Data entry keyers | NAICS 4885 | 1,950 | 20.61 | 20.41 | 13.82 / 28.70 | $42,860 | 29.44 |
| 11-3071 Transportation, storage and distribution managers | NAICS 4885 | 6,440 | 55.98 | 49.19 | 32.76 / 84.66 | $116,430 | 79.97 |
| All occupations | NAICS 4885 | 251,630 | 33.95 | 27.96 | 17.78 / 59.61 | $70,610 | 48.50 |

NAICS 488510 (six digits) is not published separately; 4885 is the finest level. **Per minute [our calc]:** entry writer $0.659 (mean), compliance officer $0.829, data-entry keyer $0.491.

### 4.2 Loaded rates other analysts used (*verified*)

- **CBP, for 7501 filers: $36.57/h** — "the BLS 2024 median hourly wage rate for Cargo and Freight Agents ($23.99) ... [×] 1.4886, to account for non-salary employee benefits", grown 2.42% (N-AF04, supporting statement §12).
- **IEc for CBP: $62.24/h** — all occupations in NAICS 4885, $29.79 (2022) → $31.12 (2023), "multiply by two to account for fringe benefits and overhead" (N-AF08, p. 4-14).
- **A high-volume broker's own classification cost:** $52-63/h (2023 dollars) (N-AF08, p. 4-17).

### 4.3 Salary sites (*assumed*, search snippets, N-AF58)

Licensed customs broker: ZipRecruiter **$75,242** (Jul 2026; 25th-75th pct $54,000-97,500); Salary.com **$59,378** ($29/h, Jul 2026); Glassdoor **$145,029** (an outlier, method unknown). Customs entry writer: ZipRecruiter **$51,176** (Sep 2026; most $44,000-58,500). These sit around the BLS figures except Glassdoor.

---

## 5. AF4 · What importers pay brokers per entry

### 5.1 Published price lists (the price as offered, *verified* at the seller's page)

| Seller (filer code where known) | Date | Base formal entry | Lines included | Extra line | Other per-entry items | ID |
|---|---|---|---|---|---|---|
| **Clearit Customs Services** (8PY, Champlain NY) | page as of 2026-09-22 | **Ocean $149.95; Air $129.95; Truck $89.95** | "3 HTS Codes & 1 Invoice" | **$15.00 / additional classification**; $15.00 / additional invoice | handling fee $25.00; ISF $50.00 (late $100); PGA $35.00; FDA prior notice $35.00; single bond $5 per $1,000 + $35 (min $40); continuous bond $500/yr; hold, cancellation or protest $200 | N-AF21 |
| **Strix** (8ND, Bozeman MT) | 2026 | **Full brokerage $100-250/entry** "based on complexity"; **self-filing software $30/entry**; both + one-time $500 onboarding | — | — | "Post Summary Corrections: $150 at Strix, up to 10 lines" (blog) | N-AF22, N-AF23 |
| **DHL Express** (US Service & Rate Guide 2026) | eff. 1 Jan 2026 | express model: clearance bundled; Duty Tax Processing **2.5% of duty, min $17.50**; Duty Tax Paid 2%, min $17.00 | 5 | **$5.00 per line after 5 lines, $10.00 minimum** | Single Clearance $35; Non-Routine Entry $35; Post Clearance Modification $90; Permits and Licenses $28; Continuous Bond $525 min | N-AF19 |
| **FedEx** ("2026 changes to FedEx surcharges & fees") | eff. 5 Jan 2026 | express model | 3 | **$3.50 per line over 3 lines** (5 on Canada-US ground) | Disbursement greater of **$15** or 2% (was $14); Duty and Tax Forwarding $29 or 2% (was $27); Broker Document Transfer **$55** (was $51); **Broker Select Option $55 per shipment** (was greater of $10 or $0.50/lb); Live Entry $28; FDA $29; Canada-to-US ground clearance entry fee above $2,000: **$42.25 + $1.95 per additional $1,000** | N-AF20 |
| **UPS Supply Chain Solutions** | changes eff. 1 Sep 2026 | base rates not public ("Customers ... will see it on their brokerage fee schedule") | 1 ("our base price includes one line of classification") | — | "Air/Ocean import entry fee will increase by **$4.00 per entry**"; Northern/Southern Border +$1.25; "Additional line fee for US imports will increase by $0.10 per line"; post-entry services +$10.00. (A snippet says entry preparation rose **$5.00** on air/ocean on 18 Sep 2025, *assumed*.) | N-AF16, N-AF17 |

### 5.2 Public buyers (real procurement pages, *verified* as the buyer states it)

| Buyer | Broker | Statement | ID |
|---|---|---|---|
| **University of Iowa** Purchasing | Scarbrough | "The average price for per clearance is typically around **$125** but this fee can vary depending on the classification of items and in some cases may be much higher." | N-AF24 |
| **Iowa State University** Procurement | Perimeter Logistics Inc. | "The broker fees typically add **$100-$200 per clearance**" | N-AF25 |
| University of Washington | Expeditors International | contract named, no prices | N-AF26 |
| UW-Madison | several approved brokers | no prices ("charges vary widely") | §12 |

**No federal, state or municipal contract with a per-entry unit price was found** (SAM.gov attachments, GSA schedule price lists and state bid tabulations did not surface; §12).

### 5.3 Market guides (all *assumed*)

Artemus Group (9JW): "$80–$200+ per shipment"; entry preparation "$50–$150+"; "$3–$10 per line"; ISF $35-80 (N-AF27). Williamsburg Customs, a site not on CBP's permit list: ocean formal $125-175, air $95-150, HTS classification review $150-300, 15-25% off at 100-500 entries a month (price list dated 15 Jan 2025) (N-AF28). Strix's volume examples: 5 entries/month ≈ $1,000/month, 40 ≈ $7,500, 200 ≈ $22,000 (N-AF23).

### 5.4 What a line is worth to an importer [our calc]

Published extra-line prices run **$3.50 (FedEx), $5 (DHL), $15 (Clearit)**. A 10-line ocean entry at Clearit costs $149.95 + $25 handling + 7 × $15 = **$279.95**, plus ISF $50. This is the price importers pay for the classification and keying of each extra line; **a co-pilot's saving per line cannot sensibly exceed it** **[our call]**.

---

## 6. AF5 · What brokers pay for software, and what competitors charge

### 6.1 ABI filing software (published, *verified*)

| Product | Unit charged | Price | ID |
|---|---|---|---|
| **CustomsCity ABI** monthly plans | "Entry number (cargo release / entry summary)"; "Pricing is per transaction sent to CBP ... Responses ... and sending updates or deletes ... are not charged" | Grow $49/20 = **$2.45**; Express $99/65 = **$1.52**; Scale $299/300 = **$1.00**; Consolidator $499/1,000 = **$0.50**; Business $999/2,500 = **$0.40**; Enterprise $1,499/5,000 = **$0.30**; eCommerce $1,999/10,000 = **$0.20** | N-AF29 |
| **CustomsCity Type 01 & 11 entry system** | "Type 01- HTS Line Numbers" (per line for formal entries) | Free 10; $49/99 = 49¢; $99/330 = 30¢; $299/1,450 = 20¢; $499/5,000 = 10¢; $999/12,500 = 8¢; $1,499/25,000 = **6¢ per line** | N-AF30 |
| **CargoWise** (WiseTech) Value Pack Community Pricing, version 26.09, USA | per "Import, Inwards Duty Deferral/FTZ, Drawback" formal procedure | **$9.95**; export, land border and miscellaneous core customs **$3.28**; forwarding import FCL/FTL $19.95, LCL/LTL/Air $13.30 per shipment | N-AF33 |
| CargoWise, how it is billed | "these fees will be passed through to your customers as a disbursement, appearing as the 'CargoWise Automation Fee' on your customer's invoice" (default); the model replaced seat and transaction licences on **1 Dec 2025** | — | N-AF34, N-AF35 |
| CargoWise, reaction | forwarders report "cost increases between 20 and 50 percent", some say costs "will more than double" (no named sources) | — | *assumed* (N-AF37) |
| Descartes NetCHB | "more than 700 customs brokers"; bought 10 Feb 2022 for **$40 million** up front plus an earn-out of up to **$60.0 million**; no price list | — | *verified* (N-AF42) |
| Converting software to ACE (2015) | "it can cost from **$25,000 to $90,000** to make the change to ACE formatting" (a Technical Advisory Group member) | — | *verified* as CBP reports it (N-AF10, 80 FR 61282) |

### 6.2 AI features already inside the filing platforms

| Platform | Feature | Date | Price | Label |
|---|---|---|---|---|
| **CargoWise** | "AI workflow engine and AI management engine, **AI Classification Assistant**, ComplianceWise and the AI CargoWise Expert chatbot"; ComplianceWise's "AI-automated document ingestion ... captures and feeds Commercial Invoice data" | live 1 Dec 2025 | **included in the $9.95 per entry**, no seat fees | features *verified* (N-AF35); ingestion wording from a snippet, *assumed* |
| **CustomsCity CustomsAI Docs** | "Upload your shipping documents and let AI extract everything needed to create your entry. Review, confirm, and file"; commercial invoices, packing lists, BOLs, AWBs; each AI-filled field starred | on sale 2026 | Free 10; $49/200 = **25¢**; $99/650 = 15¢; $299/3,000 = 10¢; $499/10,000 = 5¢; $999/25,000 = 4¢; $1,499/50,000 = **3¢ per transaction** ("Entry, ISF, AMS, ACE, ACI") | price *verified*; claims *assumed* (N-AF31) |
| **CustomsCity CustomsAI HTS Classification** | "AI-matched classifications with confidence scores"; "30 HTS Codes per search"; "Classify products 10x faster" | on sale 2026 | same tiers, down to $1,999/100,000 = **2¢ per search** | price *verified*; claims *assumed* (N-AF32) |
| **Magaya** Broker AI Assistant | "extract data from any PDF or spreadsheet commercial invoice and create an Entry in Magaya Customs Compliance"; "recommends HTS classification codes" | 18 Feb 2025 | not disclosed | *assumed* (N-AF40) |
| **Descartes** AI-powered Image Document Management | "extracts, validates and prepares data from trade documents to initiate customs and transportation workflows" | 18 Aug 2026 | not disclosed | *assumed* (N-AF41) |

### 6.3 Stand-alone AI tools and entrants

| Company | What for brokers | Money raised | Published price | Claims | Label |
|---|---|---|---|---|---|
| **Gaia Dynamics** (Palo Alto, 2025) | HTS classification, tariff audits, "Partner Program" for brokers | $1.5M pre-seed (Feb 2025); **$7M seed** (Sep 2026; a Form D reportedly shows $8.6M) | Free 30 credits/yr; Starter **$99/mo** (1.2-2.4K credits/yr); Pro **$379/mo** (5-10K); Advanced **$1,399/mo** (20-40K); unlimited users → **$0.42-0.99 per credit** **[our calc]** (credits per classification not stated) | "85%+" faster; "75%+" ROI | price *verified* (N-AF36); funding and claims *assumed* (N-AF38, N-AF39) |
| **Amari AI** | "automate data entry and paperwork" for brokers; entry summaries, ISF, type 86, HTS | **$4.5M** (First Round, Pear), out of stealth Feb 2026 | not published | "more than 30 customers"; brokers are often "mom-and-pop affairs still deeply reliant on fax machines and paper" | *assumed* (N-AF44) |
| **Raft** | AI agents for forwarders and brokers, "document extraction to smarter classification" | **$30M Series B** (Eight Roads) | not published | "saving its customers up to 2 hours on every shipment" | *assumed* (N-AF61) |
| **Caspian** | licensed broker and ABI vendor; duty refunds | **$5.4M seed** (Jul 2025) | not published | — | *assumed* (N-AF62) |
| TariffLens | HTS classification with cited rulings, for entry writers | not found | not published (pricing URL redirects) | "30 minutes to 30 seconds" | *assumed* (N-AF43) |
| KlearNow | customs platform, "flat fee per transaction ... up to 99 HS Codes" (snippet) | not checked | not published | — | *assumed* (§12) |
| Expedock | document AI into CargoWise | not checked | "no per-document fees" | "5-10 minutes for each invoice" | *assumed* (N-AF63) |

---

## 7. AF6 · Does the broker keep the saving?

| Evidence | Figure | Label |
|---|---|---|
| **Expeditors 2025**, "Customs brokerage and other services" (includes Transcon road freight, warehousing) | Revenue **$4,271.2M** (2024 $3,782.3M); directly related costs $2,392.2M ($2,098.2M) → **net revenue $1,878.9M = 44.0%** of revenue (2024 44.5%), **+11.6%** **[our calc]**. The category was **39%** of total revenue (36% in 2024). Company operating income $1,052.5M | *verified* (N-AF13, N-AF14); ratios **[our calc]** |
| Expeditors, management | "Demand for customs brokerage remained strong ... We are beginning to realize meaningful benefits from investments we have made in advanced technology to **reduce the time required to file customs entries**. In addition, we continue to invest in technology solutions, including AI, to further enhance our productivity." | *verified* (N-AF13) |
| **C.H. Robinson Q4 and FY2025** | "Customs adjusted gross profits increased 30.0%, driven by a **26.0% increase in adjusted gross profit per transaction** and a 3.0% increase in transaction volume." FY2025 customs adjusted gross profit **$132.8M (+23.5%)**, ≈18% of Global Forwarding's $741.9M **[our calc]** | *verified* (page extraction of the SEC exhibit) (N-AF15) |
| **Published fees are rising** | UPS SCS +$4.00 per air/ocean entry (1 Sep 2026); FedEx 2026: disbursement $14 → $15, broker document transfer $51 → $55, Broker Select Option to $55 | *verified* (N-AF16, N-AF20) |
| Software cost passed on | CargoWise's per-entry fee defaults to a disbursement on the importer's invoice | *verified* (N-AF34) |
| Structure | top five ≈42% (share basis unstated); 2,336 filers | *assumed* / *verified* (N-AF55, N-AF03) |

**Reading [our call]:** at the large brokers, per-transaction gross profit rose and automation gains show up as capacity ("taking on business"), not price cuts; published fees are rising and software fees are passed through. **This supports H20-03 (the broker keeps a time saving) for 2025-26, a period of tariff-driven demand.** Nothing public shows what small brokerages do with time saved, or their margins.

---

## 8. AF7 · Cost of an error (why a co-pilot needs human review)

| Rule or case | What it says | Label |
|---|---|---|
| **19 U.S.C. 1592(c)** (importer penalties) | Fraud: up to "the domestic value of the merchandise". Gross negligence: lesser of domestic value or "**four times** the lawful duties ... of which the United States is or may be deprived", or 40% of dutiable value if duties were not affected. **Negligence: lesser of domestic value or "two times" the lost duties, or 20% of dutiable value.** A prior disclosure caps negligence at interest on the unpaid duty | *verified* (N-AF48) |
| **19 U.S.C. 1641(d)(2)(A)** (broker penalties) | "a monetary penalty **not to exceed $30,000 in total** for a violation or violations of this section"; unlicensed customs business: "not to exceed $10,000 for each such transaction" | *verified* (N-AF49) |
| **19 CFR 111.28(a)** | brokers "must exercise **responsible supervision and control**" and "employ a sufficient number of licensed brokers relative to the job complexity"; CBP may weigh training, instructions, "the volume and type of business", "the reject rate for the various customs transactions relative to overall volume", access to the HTS and rulings, and the "availability of a sufficient number of individually licensed brokers" | *verified* (N-AF50) |
| United States v. UPS Customhouse Brokerage (Fed. Cir. 2009) | penalties of **$90,000** for failing to exercise responsible supervision over **tariff classification**; $15,000 paid, suit for $75,000; reversed because CBP had not weighed all ten factors | *assumed* (law-firm blog and search snippet; the court PDF would not load) (N-AF52) |
| **Ceratizit USA, DOJ, 18 Dec 2025** | **$54.4 million** to settle allegations it "knowingly misclassified tungsten carbide products using the incorrect Harmonized Tariff Schedule code" (Jun 2015-Mar 2024) and misstated origin; no admission | *verified* (N-AF51) |
| Perfectus Aluminum (May 2026) | **$549.5 million**, "largest-ever trade-related False Claims Act settlement" | *assumed* (law-firm blog) (N-AF59) |
| **CBP FY2024** | "more than **100,000 entry summary compliance reviews** resulting in recovering nearly **$700 million** in lost revenue" (≈$7,000 per review **[our calc]**); entries processed **38.4 million** (36.7M in FY2023) | *verified* (N-AF09) |
| TariffLens | "CBP conducted 71 focused assessments in March 2025 alone, identifying $310M in lost revenue. **42% of penalties come from misclassification**" | *assumed*, vendor (N-AF43) |

**Reading [our call]:** liability for the classification stays with the importer and the broker's licence, so a co-pilot suggests and the broker decides; the time saved is keying plus research, not the review.

---

## 9. AF8 · Self-filing importers

| Evidence | Figure | Label |
|---|---|---|
| **CBP, 2015 ACE rule** | "CBP does not know how many of the **112 self-filers** have already modified their systems"; 38 software developers. (The same page later swaps the two numbers: "our estimated 112 software vendors and 38 self-filers"; total 150 either way) | *verified* (80 FR 61282) (N-AF10) |
| NCBFAA | members "handle more than **97%** of the entries", so at most ~3% are filed by self-filers and non-member brokers **[our calc]** | *assumed* (N-AF05) |
| ISF filers | **240,000** respondents (importers, or agents for them) | *verified* (N-AF07) |
| Self-filing software market | Strix sells self-filing at **$30 per entry** + $500 onboarding, "Best for: Companies with in-house trade teams filing 10+ entries monthly" | *verified* (published) (N-AF22) |
| Eligibility | vendor pages say CBP looks for a "monthly average of 15 entries" and "$1,000,000 or more" of entered value; the regulation (19 CFR 143.2) asks only for the "entry filer code and average monthly volume" in the letter of intent | criteria *assumed*; regulation *verified* (§12) |

**Reading [our call]:** self-filers are a small second buyer (low hundreds of firms, a few percent of entries), but they already have a $30-per-entry self-filing option.

---

## 10. For the coordinator (not a call)

Everything in this section is **[our call]** or **[our calc]**. It shows what the numbers do to the chain; it sets no price and writes no kill condition.

### 10.1 Labour saved per entry

At the entry-writer loaded rate **$39.54/h = $0.659/min** (§4.1):

| Minutes saved per entry | Basis | Labour saved per entry |
|---|---|---|
| **3-5** | CBP's world: a formal entry takes ~10 minutes of filer time (N-AF08); a co-pilot removes a third to a half | **$1.98-3.30** |
| **8-15** | vendor world: 43-65 manual minutes, of which classification + keying 20-30 (N-AF46); a co-pilot removes 40-60% of that | **$5.27-9.89** |
| **20-40** | long or new-product entries (10+ lines, several new products at 2-4 min each, N-AF08; Magaya's "several minutes per line") | **$13.18-26.36** |

The compliance-officer rate ($0.829/min) raises each row by 26%; the data-entry-keyer rate ($0.491/min) lowers it by 25%.

### 10.2 Per-entry fee: the saving against the market's price ceilings

| Fee rule | Low (4 min) | Central (10 min) | High (30 min) |
|---|---|---|---|
| 20% of labour saved | $0.53 | $1.32 | $3.95 |
| 35% of labour saved | $0.92 | $2.31 | $6.92 |

Against:

- **CustomsCity's AI extraction and HTS search: 2-25¢ per use** (N-AF31, N-AF32);
- **CargoWise: $9.95 per entry for the whole platform, AI included**, passed to the importer (N-AF33-N-AF35);
- Gaia: $0.42-0.99 per credit (N-AF36);
- what importers pay per extra line: $3.50-15 (N-AF19-N-AF21).

**Reading:** the fee from a 20-35% share of labour saved, **$0.50-7 per entry**, sits **above** the price the platforms charge for the same AI features. A broker already on CargoWise, Magaya, Descartes or CustomsCity would be comparing a stand-alone co-pilot to a feature it already has at $0-0.25. That is hypothesis **H20-06** (`5_validation.md`), and the desk evidence now leans against it.

### 10.3 Per-brokerage fee and the $5k line

Entries needed for **$5,000 a year**: at $0.25/entry **20,000**; at $1 **5,000**; at $2 **2,500**; at $3 **1,667**; at $5 **1,000**.

**Worked example: a 5-9-staff brokerage filing 6,000 formal entries a year (§2.4 central):**

| Minutes saved | Hours saved a year | Labour saved a year | Fee at 25% of the saving | Fee at CustomsCity's AI price (~$0.10-0.30 per entry for extraction + classification) |
|---|---|---|---|---|
| 5 | 500 (≈0.28 of a 1,800-hour year) | $19.8k | **$4.9k** | $0.6-1.8k |
| 10 | 1,000 (≈0.56) | $39.5k | **$9.9k** | same |
| 20 | 2,000 (≈1.1) | $79.1k | **$19.8k** | same |

### 10.4 Market test: $2.5M and $1M

| Route | $2.5M | $1M |
|---|---|---|
| Customers at $5k a year | 500 | 200 |
| Customers at $10k a year | 250 | 100 |
| Customers at $22.7k a year (the scorecard's 110) | 110 | 44 |
| Entries at $1 each | 2.5M = **10.8%** of 23.13M formal electronic entries | 1.0M = 4.3% |
| Entries at $2 each | 1.25M = **5.4%** | 0.5M = 2.2% |
| Entries at $3 each | 0.83M = 3.6% | 0.33M = 1.4% |

**Where those customers would come from:** §2.5 puts **~320-670 filers above 5,000 entries** (upper bound ~900). **500 customers at $5k** would need most of them. **250 at ~$10k** (≈6,000 entries at a 10-minute saving and a 25% share) would need **40-80%** of them.

If the top ten filers hold 35-60% of entries, the rest file **9.3-15.0M**; **1.25M entries is 8-13%** of that.

### 10.5 Cost to serve per entry

- **Machine reading:** Textract expense extraction $0.01 a page × 3-5 pages = **$0.03-0.05** (N-AA02).
- **LLM classification:** about **$0.001-0.07 per call** (N-AA12-N-AA17), 1-3 calls an entry.
- **Variable cost ≈ $0.03-0.26 per entry**, so **$180-1,560 a year** at 6,000 entries.
- **Human QA by us: none needed in principle**, because the broker must review by law (§8).
- **Fixed cost per customer** (loading the importer's product history, integration with the broker's ABI software, support): **no source found**. C-09's model used $600, which was our own call.

**Reading:** cost to serve is not the constraint for C-20; **price is**.

### 10.6 On the fee rule

- The saving is **staff time, not cash collected**. It becomes money only if the broker hires fewer people, pays less overtime or takes on more entries with the same staff.
- **For the large brokers**, the public evidence says they take the gain as capacity and keep the price (§7).
- **For small brokerages**, nothing public says either way.
- Whether a per-entry price on time saved satisfies "our fee is a share of a measured saving" is exactly the doubt `handoff.md` names. **This check does not resolve it**; it flags it for `submarket_selection.md` §9 as the handoff asks.

### 10.7 What S5 must measure that the web cannot

1. Minutes per entry by task (keying, classification, review) at 3-5 small brokerages, timed, not estimated.
2. The share of lines already in the importer's product history.
3. Which ABI software each brokerage uses, and whether its built-in AI is switched on and used.
4. Formal entries a year and staff count per brokerage, to test §2.4.
5. Whether time saved has been, or would be, turned into more entries per writer or fewer hours.

---

## 11. Sources

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AF01 | CBP, "TA-015 Broker Permit_Contact List Final 03.2025" (CSV) | Mar 2025 (file dated 22 Apr 2025) | https://www.cbp.gov/sites/default/files/2025-04/TA-015%20Broker%20Permit_Contact%20List%20Final%2003.2025.csv | full (downloaded; no identity headers; saved to scratchpad) | 2,407 rows; unique filer codes and names; states; person-name heuristic; big-name codes |
| N-AF02 | CBP/Treasury, "Modernization of the Customs Broker Regulations", final rule, 87 FR 63267 | 18 Oct 2022 | https://www.govinfo.gov/content/pkg/FR-2022-10-18/pdf/2022-22445.pdf | full (PDF) | 87 FR 63299 permit counts and shares; 63311-63312 RFA ($17.5M size standard; "429 average brokers per year"; SUSB 2017 table) |
| N-AF03 | CBP, "Agency Information Collection Activities; Revision; Entry Summary", 90 FR 46624 | 29 Sep 2025 | https://www.govinfo.gov/content/pkg/FR-2025-09-29/pdf/2025-18849.pdf | full | 7501 burden table: 2,336 respondents, 9,903 each, 5 min; paper, lumber and informal rows |
| N-AF04 | CBP, Supporting Statement, Entry Summary 1651-0022 (ICR 202511-1651-003; received 1 Dec 2025, approved 7 May 2026) | Dec 2025 | https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202511-1651-003 (document objectID 164467101) | full (docx) | burden table; $36.57/h loaded-wage method; CBP review 0.166 h at $84.17; $401.4M |
| N-AF05 | NCBFAA, comments on OMB 1651-0022 (J. D. Gonzalez) | 31 Dec 2025 | reginfo.gov DownloadDocument objectID 165205702 | full (PDF) | 1,400+ members, 110,000 employees, 250,000 importers, "more than 97% of the entries" |
| N-AF06 | CBP, "... Entry/Immediate Delivery, and ACE Cargo Release (CBP Form 3461)", 90 FR 55155 | 1 Dec 2025 | https://www.govinfo.gov/content/pkg/FR-2025-12-01/pdf/2025-21726.pdf | full | ACE Cargo Release 9,810 respondents, 29.8M responses, 10 min |
| N-AF07 | CBP, "... Cargo Manifest/Declaration, Stow Plan, Container Status Messages and Importer Security Filing", 91 FR 40017 | 1 Jul 2026 | https://www.govinfo.gov/content/pkg/FR-2026-07-01/pdf/2026-13270.pdf | full | ISF 240,000 respondents, 8.1M responses, 1 hour (91 FR 40020) |
| N-AF08 | Industrial Economics, Inc. for CBP, "Entry of Low-Value Shipments Rulemaking: Regulatory Analysis and Regulatory Flexibility Act Analysis" (docket USCBP-2025-0002-0003) | 13 Jan 2025 | https://downloads.regulations.gov/USCBP-2025-0002-0003/content.pdf | full (188 pp.) | Table 4-1 filer bins (p. 4-3); $62.24/h (p. 4-14); HTS vetting 1-2 h per 30 products, $50-60/h (p. 4-17); "formal entry is approximately 10 minutes" (p. 4-18 fn 78); 5-min broker split (p. 4-20); Table 11-1 |
| N-AF09 | CBP, FY 2024 Trade Fact Sheet | 25 Jun 2025 | https://www.cbp.gov/sites/default/files/2025-06/20250625_cbp_trade_fact_sheet_2025_final.pdf | full | 38.4M entries; 100,000+ entry summary reviews recovering ~$700M; $422M AD/CVD |
| N-AF10 | CBP/Treasury, "ACE Filings for Electronic Entry/Entry Summary", 80 FR 61278 | 13 Oct 2015 | https://www.govinfo.gov/content/pkg/FR-2015-10-13/pdf/2015-25729.pdf | full | 112 self-filers, 38 software developers; $25,000-90,000 conversion (80 FR 61282) |
| N-AF11 | BLS, OEWS May 2025, national (`oesm25nat.zip`) and national industry-specific (`oesm25in4.zip`, nat4d) | released 2026 | https://www.bls.gov/oes/special-requests/oesm25nat.zip ; .../oesm25in4.zip | full (Excel) | wages for 43-5011, 13-1041, 43-9021, 11-3071, 00-0000, national and NAICS 488500 |
| N-AF12 | Census Bureau, SUSB 2022, "Number of Firms ... Receipts by State, Industry, and Enterprise Employment Size" | released 10 Apr 2025 | https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.xlsx | full (Excel) | NAICS 488510 firms, employment, payroll, receipts by size |
| N-AF13 | Expeditors, "Expeditors Reports Fourth Quarter 2025 EPS of $1.49" (PDF release) | 24 Feb 2026 | https://investor.expeditors.com/~/media/Files/E/Expeditors-IR-V2/press-release/2026/EXPDQ41.PDF | full | revenue and costs by service; salaries; management quote on customs technology |
| N-AF14 | Expeditors, Form 10-K 2025 | 2026 | https://www.sec.gov/Archives/edgar/data/746515/000119312526071569/expd-20251231.htm | page extraction (WebFetch; no identity header) | "39% and 36% of ... total revenues" |
| N-AF15 | C.H. Robinson, Q4 2025 earnings release (Ex. 99.1) | Jan 2026 | https://www.sec.gov/Archives/edgar/data/1043277/000104327726000005/ex991earningsreleaseq41231.htm | page extraction (WebFetch) | customs AGP +30%, per transaction +26%, volume +3%; FY $132.8M; Global Forwarding totals |
| N-AF16 | UPS Supply Chain Solutions, "Customs Brokerage Rates" (US) | update 1 Aug 2026; eff. 1 Sep 2026 | https://www.ups.com/us/en/supplychain/tools/surcharges/brokerage-general-rates | full (page text) | per-entry and per-line increases |
| N-AF17 | UPS SCS, "Customs Brokerage Fee - Glossary of Terms" (PDF) | file Feb 2026 | https://assets.ups.com/adobe/assets/urn:aaid:aem:93eea396-bed6-4cf8-87da-bb46cb9687c8/original/as/customs-brokerage-billing-terms.pdf | full | "base price includes one line of classification"; MPF FY2026 |
| N-AF18 | UPS, "U.S. Trade and Tariff Regulatory Update" (PDF) | 29 Apr 2025 | https://www.ups.com/assets/resources/webcontent/en_GB/us-regulatory-update.pdf | full | entry types by value (informal to $2,500) |
| N-AF19 | DHL Express, "Service & Rate Guide 2026: United States" | eff. 1 Jan 2026 | https://www.dhl.com/content/dam/dhl/global/dhl-express/documents/pdf/service-and-rate-guide-us-en.pdf | full | customs services table (multiline, duty tax processing, bonds) |
| N-AF20 | FedEx, "2026 changes to FedEx surcharges & fees" | eff. 5 Jan 2026 | https://www.fedex.com/content/dam/fedex/us-united-states/services/surcharge_and_fee_changes_2026.pdf | full | clearance fees 2025 vs 2026 |
| N-AF21 | Clearit, "Custom Broker Fees USA" price list (Clearit Customs Services, filer 8PY) | read 22 Sep 2026 | https://clearit.com/usa/pricing/ (redirect from clearitusa.com) | page extraction | base fees by mode, lines included, add-ons, bonds |
| N-AF22 | Strix, pricing page (Strix LLC, filer 8ND) | 2026 | https://strixsmart.com/pricing | full (page text) | $30 self-filing; $100-250 full; $500 onboarding |
| N-AF23 | Strix blog, "How Much Does a Customs Broker Cost in 2026?" | 2026 | https://strixsmart.com/resources/blog/customs-broker-cost | page extraction | volume examples; PSC $150; ranges |
| N-AF24 | University of Iowa Purchasing, "Customs clearance" | read 22 Sep 2026 | https://ap-purchasing.fo.uiowa.edu/purchasing/contracts/customs-clearance | page extraction | Scarbrough; ~$125 per clearance |
| N-AF25 | Iowa State University Procurement, "Customs Broker Information" | read 22 Sep 2026 | https://www.procurement.iastate.edu/customs-broker-information | page extraction | Perimeter Logistics; $100-200 per clearance |
| N-AF26 | University of Washington Finance, "Customs Clearance" | read 22 Sep 2026 | https://finance.uw.edu/ps/how-to-pay/supplier-invoice/customs-clearance | page extraction | Expeditors named; no prices |
| N-AF27 | The Artemus Group (filer 9JW), "What Is the Real Cost Of Customs Broker Fees In 2026?" | 2026 | https://artemusgroupusa.com/custom-broker-fees/ | page extraction | ranges (*assumed*) |
| N-AF28 | "Williamsburg Customs" pricing page (not on CBP's permit list) | 15 Jan 2025 | https://www.wiliamsburgmercantile.com/pricing.html | page extraction | ranges (*assumed*) |
| N-AF29 | CustomsCity, "ABI Pricing" | read 22 Sep 2026 | https://customscity.com/abi-pricing/ | full (HTML) | monthly plans, per-transaction prices |
| N-AF30 | CustomsCity, "Type 01 & Type 11 eCommerce Entry System" pricing | read 22 Sep 2026 | https://customscity.com/type-01-pricing/ | full | per HTS line prices |
| N-AF31 | CustomsCity, "CustomsAI Docs" | read 22 Sep 2026 | https://customscity.com/customsai-docs/ | full | features; per-transaction prices |
| N-AF32 | CustomsCity, "CustomsAI HTS Classification" | read 22 Sep 2026 | https://customscity.com/customsai-hts-classification/ | full | features; per-search prices |
| N-AF33 | CargoWise, "CargoWise Value Pack Community Pricing" (version 26.09) | 2026 | https://www.cargowise.com/cargowise-value-pack/cargowise-value-pack-community-pricing/ | page extraction | USA $9.95 import formal procedure; $3.28; forwarding prices |
| N-AF34 | CargoWise, "CargoWise Value Packs" | 2026 | https://www.cargowise.com/cargowise-value-pack/ | page extraction | four packs; "CargoWise Automation Fee" as a disbursement |
| N-AF35 | WiseTech Global, "WiseTech Global launches CargoWise Value Packs ..." | 1 Dec 2025 | https://www.wisetechglobal.com/news/wisetech-global-launches-cargowise-value-packs-introducing-substantial-new-product-capabilities-and-simplified-billing/ (also cargowise.com) | page extraction | AI features included; dates; pass-through; snippet on ComplianceWise ingestion |
| N-AF36 | Gaia Dynamics, pricing page | read 22 Sep 2026 | https://www.gaiadynamics.ai/pricing | full (HTML) | tiers, credits, users |
| N-AF37 | Breakbulk News, "Forwarders Face a High Stakes Test as WiseTech Shifts CargoWise Costs onto Shippers" | 8 Dec 2025 | https://breakbulk.news/forwarders-face-a-high-stakes-test-as-wisetech-shifts-cargowise-costs-onto-shippers/ | page extraction | 20-50% increases (unnamed sources) |
| N-AF38 | Gaia Dynamics, "AI Tools for Customs Brokers" | read 22 Sep 2026 | https://www.gaiadynamics.ai/solutions/customs-brokers | page extraction | claims (*assumed*) |
| N-AF39 | Gaia Dynamics funding (PR Underground/FinancialContent, 16 Sep 2026; runtimewire Form D note) | Sep 2026 | https://www.financialcontent.com/article/prunderground-2026-9-16-gaia-dynamics-raises-7m-to-expand-ai-platform-keeping-businesses-ahead-of-tariffs-and-trade-risk | snippet | $7M seed; $1.5M pre-seed |
| N-AF40 | Magaya, "Magaya Releases AI-Powered Customs Filing Solution" | 18 Feb 2025 | https://www.magaya.com/magaya-releases-ai-powered-customs-filing-solution/ | page extraction | Broker AI Assistant features and claim |
| N-AF41 | Investing.com, "Descartes launches AI document management for customs brokers" | 18 Aug 2026 | https://www.investing.com/news/company-news/descartes-launches-ai-document-management-for-customs-brokers-93CH-4864796 | page extraction | feature; GM quote |
| N-AF42 | Descartes, "Descartes Acquires NetCHB" | 10 Feb 2022 | https://www.descartes.com/resources/news/descartes-acquires-netchb | page extraction | $40M + up to $60M; 700+ brokers |
| N-AF43 | TariffLens, "AI for Customs Brokers" (pricing URL redirects here) | read 22 Sep 2026 | https://www.tarifflens.ai/pricing | full (HTML) | claims (30 min → 30 s; 42% of penalties; 71 focused assessments) |
| N-AF44 | TechCrunch, "These former Big Tech engineers are using AI to navigate Trump's trade chaos" (Amari AI) | 19 Feb 2026 | https://techcrunch.com/2026/02/19/this-former-big-tech-engineers-are-using-ai-to-navigate-trumps-trade-chaos/ | page extraction | $4.5M; 30+ customers; "mom-and-pop" |
| N-AF45 | FreightMynd, "AI for Customs Brokers: Automation Guide (2026)" | 28 Mar 2026 | https://freightmynd.com/blog/ai-for-customs-brokers-guide/ | page extraction | 20-40 min; 5-12 min; 75/25 split |
| N-AF46 | SocialVik, "Manual Customs Documentation: How Much Time CHAs Actually Lose Per Shipment" | 21 May 2026 | https://www.socialvik.com/blog/customs-documentation-time-per-shipment-cha-benchmark | page extraction | task minutes; entries per day |
| N-AF47 | Docxster, "The Customs Broker Software That Actually Cuts Manual Data Entry (2026)" | 14 Aug 2026 | https://www.docxster.com/blog/the-customs-broker-software-that-actually-cuts-manual-data-entry-(2026) | page extraction | long-entry anecdote |
| N-AF48 | 19 U.S.C. 1592 (LII) | current | https://www.law.cornell.edu/uscode/text/19/1592 | full | penalty levels, prior disclosure |
| N-AF49 | 19 U.S.C. 1641 (LII) | current | https://www.law.cornell.edu/uscode/text/19/1641 | full | $30,000 broker cap; $10,000 unlicensed |
| N-AF50 | 19 CFR 111.28 (LII) | current | https://www.law.cornell.edu/cfr/text/19/111.28 | full | responsible supervision factors |
| N-AF51 | DOJ, "Ceratizit USA LLC Agrees to Pay $54.4M ..." | 18 Dec 2025 | https://www.justice.gov/opa/pr/ceratizit-usa-llc-agrees-pay-544m-settle-false-claims-act-allegations-relating-evaded-0 | page extraction | amount; misclassification allegation |
| N-AF52 | Customs & International Trade Law Blog, "A Victory for All Customs Brokers" (US v. UPS Customhouse Brokerage) | 18 Aug 2009 | https://customsandinternationaltradelaw.com/2009/08/18/a-victory-for-all-customs-brokers/ | page extraction + snippet of CAFC 08-1409 | $90,000 / $75,000; holding |
| N-AF53 | A.N. Deringer, "US Customs Brokerage" | read 22 Sep 2026 | https://www.anderinger.com/services/customs-brokerage-consulting/us-customs-brokerage/ | page extraction | >1M entries; top five filer |
| N-AF54 | Research and Markets via Yahoo Finance, "Assessment of the US $4B+ Customs Brokerage Market 2020-2025" | 3 Feb 2021 | https://finance.yahoo.com/news/assessment-us-4b-customs-brokerage-092300464.html | page extraction | FedEx + UPS ~35%; >$4B |
| N-AF55 | Mordor Intelligence, "USA Customs Brokerage Market" | 2026 | https://www.mordorintelligence.com/industry-reports/united-states-customs-brokerage-market | page extraction | $5.48B; top five ~42% |
| N-AF56 | Web search result (no source named), "top 10 customs brokers ... roughly 60%" | 2026 | — | snippet | flagged unsourced |
| N-AF57 | CBP, "Customs Broker Frequently Asked Questions" | read 22 Sep 2026 | https://www.cbp.gov/trade/programs-administration/customs-brokers/frequently-asked-questions | page extraction | ~16,170 licensed brokers; self-filing unaffected |
| N-AF58 | ZipRecruiter, Glassdoor, Salary.com salary pages (licensed customs broker; customs entry writer) | Jul-Sep 2026 | https://www.ziprecruiter.com/Salaries/Licensed-Customs-Broker-Salary ; https://www.glassdoor.com/Salaries/licensed-customs-broker-salary-SRCH_KO0,23.htm ; https://www.salary.com/research/salary/hiring/licensed-customs-broker-salary ; https://www.ziprecruiter.com/Jobs/Customs-Entry-Writer | snippet | salary figures |
| N-AF59 | Sidley, White Collar Watch, "Importer Agrees to Pay $549.5 million ..." | 18 May 2026 | https://whitecollarwatch.sidley.com/2026/05/18/tariff-enforcement-at-the-forefront-importer-agrees-to-pay-549-5-million-in-largest-ever-trade-related-false-claims-act-settlement/ | snippet | $549.5M |
| N-AF60 | World Bank, Doing Business 2020, Economy Profile United States | 2019 data | https://archive.doingbusiness.org/content/dam/doingBusiness/country/u/united-states/USA.pdf | full (PDF) | import documentary 8 h / $100; border 2 h / $175 |
| N-AF61 | Raft, "Raft Raises $30M Series B ..." | 2024-25 | https://www.raft.ai/resources/press-releases/raft-raises-30m-in-series-b-funding-to-transform-global-supply-chain-execution-with-ai | snippet | $30M; "up to 2 hours on every shipment" |
| N-AF62 | BusinessWire, "Caspian Launches AI-Powered Global Trade Advisory Platform, with $5.4M Seed Funding" | 29 Jul 2025 | https://www.businesswire.com/news/home/20250729878632/en/ | snippet | $5.4M; licensed broker and ABI vendor |
| N-AF63 | Expedock product pages | 2026 | https://www.expedock.com/product/customs-files-ap-automation | snippet | "5-10 minutes for each invoice"; "no per-document fees" |

Earlier IDs used: N-AA02, N-AA12-N-AA17, N-AA40 (check AA); N-N05, N-H22, N-F08, N-F10, N-S01, N-S09, N-S20, N-S26 (earlier checks, not re-read).

---

## 12. Could not access, or not found

**Not found (searched, no public source):**
- **Formal entries by filer or by brokerage size.** CBP holds "volume by filer data" (it gave some to its contractor, N-AF08) but does not publish it. No trade-press ranking of brokers by entries was found. §2.4-2.5 are derived, not measured.
- **A small brokerage stating its own entries a year:** none found.
- **Average HTS lines per formal entry:** not in CBP's trade statistics or fact sheet.
- **Share of a repeat importer's lines already classified:** no figure anywhere.
- **Minutes per entry from a neutral time study:** none. The government figures are burden estimates for transmission; the preparation figures are all from vendors.
- **A public contract with a per-entry customs brokerage unit price** (federal, state, municipal, GSA schedule): none surfaced; two university pages give averages only.
- **Base brokerage prices at UPS SCS, Expeditors, Flexport, Livingston, C.H. Robinson:** negotiated, not published.
- **Prices for NetCHB, Magaya Customs Compliance, KlearNow, Descartes' AI feature, Amari, Raft, TariffLens, Expedock:** not published.
- **Small brokerages' margins,** or any NCBFAA statement on price competition.
- **A current CBP count of self-filers** (latest found: 112 in 2015). CBP's self-filer eligibility thresholds (15 entries a month, $1M) appear only on vendor pages; the CBP help article (help.cbp.gov Article1844) would not render.
- **A historical series of broker entry fees** from GAO, USITC or CBP: none found.

**Could not access:**
- CBP's permitted-broker CSV refused curl (Akamai "Access Denied"); **it downloaded with a plain wget request carrying no identity**, and was counted.
- **SEC EDGAR:** read only through WebFetch page extraction (no declared User-Agent was supplied, per the hard rule). That covers the Expeditors 10-K and the C.H. Robinson exhibit; the full financial tables were not reviewed.
- **Census Economic Census product-line data** (revenue from "customs brokerage services"): the Census API now requires a registered key, which was not obtained.
- **federalregister.gov full text and eCFR** returned a CAPTCHA to scripts. The Federal Register API (metadata) and govinfo PDFs were used instead; regulations were read at Cornell LII.
- **omb.report** returned 403. reginfo.gov was used.
- **bls.gov HTML tables** redirected to the OEWS home page. BLS's downloadable May 2025 Excel files were used instead.
- The Federal Circuit PDF (08-1409) returned an empty file or a certificate error; the case is cited from a law-firm blog and a snippet.
- UPS SCS rates via WebFetch were denied; the same page read fine with a plain download.

**Excluded:**
- L.M. Clark's 2018 fee schedule (Canadian entries, not US).
- Williamsburg and Greenwich "Mercantile" guides: not on CBP's permit list, so kept only as *assumed* market ranges.
