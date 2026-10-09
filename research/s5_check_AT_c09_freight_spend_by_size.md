# S5 check AT: how much freight a C-09 customer buys, by size (C-09)

- **What this is:** desk research for card C-09 (software that reads a shipper's freight bills and rate agreements and flags bills that look wrong; the shipper's own staff review the flags and file disputes; a flat monthly subscription). The kill-test lines are read at the customer's **truckload (TL) plus less-than-truckload (LTL) spend** (`research/selection_runs/run-01/4_kill_conditions.md` §2.5.11: at $1.5M, Kill under 0.044% flagged and Pass at 6.44%; at $5M, Pass at 2.03%). The founders asked, verbatim: "Can we get an estimate on the business size of these customers and any info about how much they spend on shipping? The more they spend on shipping the more room for money to be made by us." This check answers five questions:
  - **AT1** freight cost as a share of revenue, from small and mid-sized public firms' own filings;
  - **AT2** other real documents (bankruptcy payment lists) and neutral benchmarks;
  - **AT3** the mode split: what share of a shipper's freight dollars is TL+LTL;
  - **AT4** four named shippers from the contacts file: **kept outside the project** in `~/Documents/personal/bio/freight_private/c09_shipper_sizes.md`, as instructed. Nothing about them is repeated here;
  - **AT5** a conversion table from revenue to TL+LTL spend per segment, the revenue needed for $1M-$10M of TL+LTL spend, and how many US firms sit above each line.
- **Builds on / not redone:** check Y §2.3 (freight 1.6-3.2% of receipts **[our calc]**; the CPA firm's "3 percent of gross sales on inbound" and "7 percent of net sales on outbound", N-Y20) and §3.1 (segments SG1-SG6 and their NAICS codes); check X §7.2-§7.4 (Establish Davis: transportation 3.68% of sales, N-X21; CSCMP 2024 TL $387B, LTL $64B, private fleets $541.4B, N-K22; CFS 2022 shares by value; check X's TL+LTL share inputs 45/60/75% for manufacturers and 25/40/55% for wholesalers); check AN §AN8 and §AN10 (three bankrupt mid-sized firms, trucking 0.9-4.8% of revenue, N-AN22-N-AN24; broker shares); check AD §4.1 (nine small firms' LTL, median ~0.7% of revenue, N-AD14-N-AD22). Those are cited by their old IDs and not re-argued.
- **Date:** 2026-10-09. Everything new here was accessed on 2026-10-09.
- **Status:** input to S5 and to the kit's spend screen. **It decides nothing.** The conversion percentages in AT5 are our estimates, not findings.
- **Searches used:** 8 web searches of the 40-60 allowed. About 100 reads with the fetch tool, almost all of them SEC pages (filings, the XBRL data API and EDGAR full-text search). Four curl downloads with a generic browser user-agent: BEA's input-output tables, two Census SUSB tables, and the CourtListener search API with five court PDFs (each in its own scratchpad folder, parsed by scripts kept elsewhere).
- **No identity was sent. Nobody was contacted.** The fetch tool reached SEC EDGAR, the XBRL API and EDGAR full-text search **without a contact User-Agent**; no identity went into any header, URL or query. No logins, forms, sign-ups or gated downloads. Data-broker sites that came up in one search (Owler, ContactOut, CB Insights, PitchBook) were **not** used for any figure.
- **Quotes:** the fetch tool returns quotes of at most 125 characters, so long sentences appear here as consecutive fragments in quotation marks. Amounts in thousands are given as the filing gives them.
- **Labels:**
  - *verified* = read at the source: the company's own filing, the SEC's XBRL API (the company's own tagged value), a court filing, or a government table;
  - *assumed* = a vendor or association figure, a secondary summary, or a search-result summary;
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
- **New sources and claims:** N-AT01 to N-AT43 (claim ledger). Cited, not re-read: N-K22, N-X21, N-Y20, N-Y21, N-AN22-N-AN24, N-AD14-N-AD22.

**Words used here:**
- **TL (truckload):** one shipper fills or books a whole trailer. **LTL (less-than-truckload):** a carrier combines several shippers' pallets in one trailer and bills each by weight, class and distance. **Parcel:** boxes sent by UPS, FedEx and similar. **Private or own fleet:** the shipper's own trucks and drivers. **Drayage:** short truck moves of ocean containers between a port or rail ramp and a warehouse.
- **Outbound / inbound freight:** freight on what a firm ships to customers / on what it buys. **Prepaid / collect:** the seller pays the carrier / the buyer pays. **Delivered pricing:** the freight is inside the product price.
- **Freight-out:** a firm's outbound freight cost. **Shipping and handling (S&H):** outbound freight, often with packing and some warehouse labour. **DSD (direct store delivery):** a maker's own trucks deliver to stores.
- **COGS / SG&A:** cost of goods sold / selling, general and administrative expenses (where a firm books its freight).
- **10-K:** a US public company's annual report to the SEC. **XBRL:** the machine-readable tags in that report; the SEC publishes each tagged number through its data API. **SOFA:** a bankrupt business's sworn Statement of Financial Affairs; Part 2 item 3 lists payments to each creditor in the 90 days before filing (creditors paid less than a threshold, $6,425-8,575 depending on the year, may be left out).
- **SUSB:** Census Statistics of US Businesses (firm counts by size). **BEA Use table:** the Bureau of Economic Analysis table of what each industry buys from every other industry.
- **FAP:** freight audit and payment provider. **TMS:** transportation management system (software to quote, book and track shipments). **3PL:** third-party logistics provider.
- **SG1-SG6:** the six candidate segments from check Y §3.1: SG1 LTL-heavy distributors (HVAC, plumbing, electrical, MRO, fasteners); SG2 capital goods and consumer durables makers; SG3 food, beverage and household nondurables makers; SG4 containers, packaging and paper; SG5 building materials and forest products; SG6 agribusiness. **Contrast:** auto parts, metals and homebuilders, which fail the durability test.

---

## §0 Summary

| Question | What the record says | Best evidence | Label | **Proposed verdict** |
|---|---|---|---|---|
| **AT1** Freight as a share of revenue, from filings | **30 public firms with $38M-$1.46B of revenue** (4 more above the range as context) disclose a freight amount. These are mostly outbound figures and often include parcel. **Ratio range by segment [our calc]:** SG1 distributors **0.6-4.7%** (median 1.8%; 1.6% with the four larger distributors); SG2 **2.2-5.1%** (median 3.1%; Virco 10.2% with classroom delivery); SG3 **2.1-8.5%** (median 4.3%; up to 10.6% where warehousing or own fleets are included); SG4 **3.0-5.2%** (median 3.9%); SG5 **4.0-4.5%**, 10.1% with an own fleet; SG6 **2.6-19.6%** (bulk potash, salt and clay at the top; ag chemicals 7.8%). Recent re-reads move little: EACO 1.76% (2017) → 1.49% (2025); WD-40 4.3% → 2.9%; Tootsie 8.5% → 7.8% (2025 figure includes warehousing). **No firm read discloses an inbound freight amount** | N-AT01-N-AT35 | filings and XBRL *verified*; ratios **[our calc]** | **Answered from the web** for public firms (the 2016-17 tagged data dominate; public firms are larger than the target) |
| **AT2** Other real documents and benchmarks | **Two new bankruptcy payment lists:** an oilfield-supply distributor ($47-99M) paid for-hire trucking **~$0.23M a year** (0.24-0.50% of revenue) while spending ~4× that on its own fleet; a consumer-durables brand (Instant Brands LLC, $524M) paid ~$20M a year to transport payees (3.8%), of which **TL+LTL was only 4.7%** (12.6% with port drayage): parcel 45%, ocean 31%. **BEA's 2023 Use table (neutral):** the freight on what manufacturers buy, by for-hire truck, is **0.8-3.3% of output** by industry (food 3.28%, nonmetallic minerals 3.02%, paper 1.78%, machinery 1.00%). CSCMP 2026 (secondary): logistics $2.40T, 7.8% of GDP; parcel $241.3B, rail $97.3B (2025) | N-AT36-N-AT41 | filings and BEA data *verified*; CSCMP *assumed* | **Narrowed** (two more bankrupt firms; a neutral inbound benchmark) |
| **AT3** Mode split | **Nationally [our calc] on CSCMP 2024:** TL+LTL = **58%** of for-hire TL, LTL, parcel and rail dollars, **34%** once private fleets are counted. **BEA:** truck carries **49-81%** of the for-hire freight on manufacturers' inputs (rail most of the rest). **Firm level:** TL+LTL (with brokers) was 68%, 97% and 99.7% of trucking-plus-parcel at three bankrupt makers and distributors, but **5-13%** at an importer selling through parcel and retailers, and a distributor's own fleet cost ~4× its for-hire trucking. **Proposed TL+LTL share of a firm's outbound freight [our call]:** SG1 25/**40**/55%; SG2 45/**65**/80%; SG3 and SG4 45/**60**/75%; SG5 35/**55**/70%; SG6 35/**50**/65% | N-AT36, N-AT37, N-AT39-N-AT41; N-K22, N-AN22-N-AN24 | mixed | **Narrowed** (no filing splits freight by mode; the split is a property of each firm) |
| **AT4** Four named shippers | Written to the private folder only | — | — | See the private file |
| **AT5** Revenue → TL+LTL spend, thresholds, firm counts | **Central TL+LTL as % of revenue [our calc]:** SG1 **1.1%**, SG2 **2.6%**, SG3 **3.8%**, SG4 **3.2%**, SG5 **3.5%**, SG6 **5.2%** (ranges 0.3-12.8%). **Revenue needed for $1.5M of TL+LTL (central):** SG1 **~$130M**, SG2 **~$58M**, SG3 **~$39M**, SG4 **~$46M**, SG5 **~$43M**, SG6 **~$29M**. **US firm-industry entries above the $1.5M line (SUSB 2022) [our calc]:** about **11,300** across the six segments (1,100-2,400 each); about **5,700** above $5M; about **3,400** above $10M, where FAP providers start | N-AT42, N-AT43 and AT1-AT3 | counts *verified*; everything else **[our calc]** / **[our call]** | **Proposed table** (estimates, with wide ranges) |

**One-line reading [our call]:** a mid-sized maker in SG2-SG6 typically buys **2.5-5% of revenue** in TL+LTL freight, so **$1.5M of TL+LTL needs roughly $30-60M of revenue**, and $5M needs roughly $100-200M. Distributors (SG1) need about twice to four times the revenue, because much of their freight is parcel, their own trucks, or paid by their suppliers. Importers that sell through parcel and big retailers can sit far below these ratios.

---

## §AT1 · Freight as a share of revenue, from real filings

### AT1.1 Method

- **Finding the firms.** US GAAP had an XBRL tag for this cost until 2018: **"Shipping, Handling and Transportation Costs (Deprecated 2018-01-31)"**, defined as "Cost incurred during the reporting period in transporting goods and services to customers. Includes freight-out costs." [N-AT01]. The SEC's data API lists every filer that used it in a year: **345 filers for calendar 2016 and 284 for 2017** [N-AT02]. Firms in SG1-SG6 with revenue of about $20M-$1.5B were picked from these lists, and a few more were found through EDGAR full-text search.
- **Checking them.** Each value was read either in the filing itself (quote, classification, revenue) or, where the note could not be reached with the fetch tool, from the SEC's API for that company (the company's own tagged figure, *verified*, with "quote not read" noted). Revenue is from the same filing or the same API.
- **Recent years.** The tag was retired in 2018, so the most recent 10-Ks of twelve firms were re-read. Four still give an amount (EACO, Tootsie Roll, WD-40, J&J Snack Foods); the other eight (AAON, Acme United, John B. Sanfilippo, Oil-Dri, Compass Minerals, Watts, Johnson Outdoors, American Vanguard) state none in the parts read.
- **Bias to keep in mind [our call]:** firms choose whether to disclose. Those with large freight bills are more likely to do so, which pushes the ratios up. Public firms are also larger than C-09's target, and most of these figures are **outbound only**, often **with parcel**, and sometimes with **warehousing or own-fleet** costs.

### AT1.2 The firms

Ratios are freight ÷ revenue **[our calc]**. "XBRL" = the company's tagged figure read through the SEC API; "10-K" = read in the filing.

| # | Firm (what it does) | Seg | FY | Revenue | Freight amount | **Ratio** | What it covers, and where it is booked | Quote (fragments as returned) | Claim | Label |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **EACO Corp** (Bisco Industries: electronic components and fasteners to manufacturers; 644 staff, 7 DCs in 2025) | SG1 | Aug 2017 | $156.954M | $2.760M | **1.76%** | S&H; in cost of revenues; freight billed to customers is in revenue | "Shipping and handling expenses are included in cost of revenues" … "were approximately $2,760,000 and $2,653,000 for the years ended August 31, 2017 and 2016" | N-AT03 | *verified* (10-K) |
| 1b | EACO Corp | SG1 | Aug 2025 | $427.931M | $6.360M | **1.49%** | same; FY2024 $5.53M on $356.231M = 1.55% | "Shipping and handling expenses are included in cost of revenues and were approximately $6,360,000 and $5,530,000" | N-AT04 | *verified* (10-K) |
| 2 | **The Hillman Companies** (fasteners and hardware to retailers) | SG1 | 2017 | $838.368M | $39.205M | **4.68%** | "freight and handling"; in SG&A | "The costs incurred to ship product to customers, including freight and handling expenses," … "$39,205 in 2017, $36,283 in 2016" (thousands) | N-AT05 | *verified* (10-K, XBRL page R26) |
| 3 | **Transcat** (test and measurement instrument distributor plus calibration services) | SG1 | Mar 2017 | $143.898M (distribution sales $72.795M) | $0.9M | **0.63%** of total; 1.24% of distribution sales | XBRL tag; the note was not reached | quote not read | N-AT06 | *verified* (XBRL) |
| — | *Context, above the range:* MSC Industrial (MRO) | SG1 | Sep 2017 | $2,887.7M | $120.0M | **4.15%** | XBRL tag | — | N-AT07 | *verified* (XBRL) |
| — | *Context:* Applied Industrial Technologies (MRO, power transmission) | SG1 | Jun 2017 | $2,593.7M | $20.1M | **0.77%** | XBRL tag; looks partial **[our call]** | — | N-AT07 | *verified* (XBRL) |
| — | *Context:* Watsco (HVAC distributor) | SG1 | 2017 | $4,342.0M | $47.7M | **1.10%** | XBRL tag | — | N-AT07 | *verified* (XBRL) |
| — | *Context:* Pool Corp (pool supplies distributor) | SG1 | 2017 | $2,788.2M | $45.2M | **1.62%** | XBRL tag | — | N-AT07 | *verified* (XBRL) |
| 4 | **Acme United** (scissors, cutting tools, first aid) | SG2 | 2017 | $130.550M | $6.596M | **5.05%** | shipping to customers; SG&A | "The costs of shipping product to our customers ($6,595,544 in 2017 and $5,388,481 in 2016)" "are included in selling, general and administrative expenses." | N-AT08 | *verified* (10-K) |
| 5 | **Omega Flex** (flexible gas piping) | SG2 | 2017 | $101.799M | $2.562M | **2.52%** | shipping; selling expense | "Shipping costs are included in selling expense" … "The expense relating to shipping was $2,562,000, $2,339,000 and $2,429,000" | N-AT09 | *verified* (10-K) |
| 6 | **P&F Industries** (pneumatic and hand tools) | SG2 | 2017 | $58.974M | $2.017M | **3.42%** | S&H; SG&A | "Expenses for shipping and handling costs are included in selling, general and administrative expenses," "and totaled approximately $2,017,000 and $2,013,000" | N-AT10 | *verified* (10-K) |
| 7 | **Virco Mfg.** (school furniture) | SG2 | Jan 2018 | $189.287M | $19.299M | **10.20%** | "shipping and classroom delivery"; SG&A; "third party carriers for more than 90% of customer deliveries" | "shipping and classroom delivery costs of approximately $19,299,000, $16,116,000 and $15,799,000," "were included in selling, general and administrative expenses." | N-AT11 | *verified* (10-K) |
| 8 | **Watts Water Technologies** (plumbing and flow-control products) | SG2 | 2017 | $1,456.7M | $52.1M | **3.58%** | XBRL tag | quote not read | N-AT12 | *verified* (XBRL) |
| 9 | **Johnson Outdoors** (fishing, diving, camping equipment) | SG2 | Sep 2017 | $490.565M | $10.844M | **2.21%** | XBRL tag | quote not read | N-AT13 | *verified* (XBRL) |
| 10 | **AAON** (rooftop HVAC units) | SG2 | 2017 | $405.232M | $11.4M | **2.81%** | in cost of sales; the sentence says "fees", which may mean amounts billed **[our call]: ambiguous** | "We incur shipping and handling costs in the distribution of products sold that are recorded in cost of sales." … "shipping and handling fees amounted to approximately $11.4 million," | N-AT14 | *verified* (10-K) |
| 11 | **Tootsie Roll Industries** (confectionery) | SG3 | 2017 | $515.674M | $43.973M | **8.53%** | XBRL tag | — | N-AT15 | *verified* (XBRL) |
| 11b | Tootsie Roll | SG3 | 2025 | $724.675M (net product sales) | $56.780M | **7.84%** | "freight, delivery and warehousing"; in SG&A (selling, marketing and administrative) | "Selling, marketing and administrative expenses include freight, delivery and warehousing expenses." "These expenses decreased from $57,581 in 2024 to $56,780 in 2025" | N-AT16 | *verified* (10-K) |
| 12 | **WD-40 Company** (lubricants, household maintenance products) | SG3 | Aug 2017 | $380.506M | $16.4M | **4.31%** | XBRL tag | — | N-AT17 | *verified* (XBRL) |
| 12b | WD-40 Company | SG3 | Aug 2025 | $619.985M | $18.2M | **2.94%** | paid to third parties for shipment from its DCs and contract makers; in SG&A | "we exclude the portion associated with amounts paid to third parties for shipment to our customers" … "These costs totaled $18.2 million and $17.3 million" | N-AT17 | *verified* (10-K) |
| 13 | **J&J Snack Foods** (frozen snacks, beverages) | SG3 | Sep 2017 | $1,084.224M | $81.824M | **7.55%** | XBRL tag | — | N-AT18 | *verified* (XBRL) |
| 13b | J&J Snack Foods | SG3 | Sep 2025 | $1,583.233M (above the range) | $168.305M | **10.63%** | the income-statement line "Distribution" (broader than freight) | table values | N-AT18 | *verified* (10-K table) |
| 14 | **John B. Sanfilippo & Son** (nuts) | SG3 | Jun 2018 | $888.595M | $20.418M | **2.30%** | freight plus preparing goods for shipment; selling expense; FY2017 $17.682M on $846.635M = 2.09% | "Shipping and handling costs, which include freight and other expenses to prepare finished goods for shipment, are included in selling expenses." | N-AT19 | *verified* (10-K) |
| 15 | **Coffee Holding Co.** (coffee roaster) | SG3 | Oct 2017 | $77.128M | $2.412M | **3.13%** | shipping to customers; selling and administrative | "Costs associated with shipping product to customers aggregating approximately $2,412,000 and $1,506,000" "is included in selling and administrative expenses." | N-AT20 | *verified* (10-K) |
| 16 | **Scott's Liquid Gold** (household and personal care) | SG3 | 2017 | $42.186M | $2.614M | **6.20%** (2016: 5.11%) | "primarily of freight-out"; selling expense | "Shipping and handling costs totaled $2,614,300 and $1,799,900" … "comprised primarily of freight-out as selling expenses." | N-AT21 | *verified* (10-K) |
| 17 | **Ocean Bio-Chem** (cleaning and maintenance products) | SG3 | 2017 | $38.933M | $1.226M | **3.15%** | all S&H; in COGS | "All shipping and handling costs incurred by the Company are included in cost of goods sold" … "totaled approximately $1,226,000 and $1,120,000" | N-AT22 | *verified* (10-K) |
| 18 | **Reed's** (ginger beverages) | SG3 | 2017 | $37.714M | $3.942M | **10.45%** | "Delivery and handling expense" line; includes warehouse labour and rent **[our call]** | "an increase in freight charges of $173,000 and additional labor related charges of $48,000" | N-AT23 | *verified* (XBRL; MD&A) |
| 19 | **AEP Industries** (plastic films) | SG4 | Oct 2016 | $1,095.830M | $47.690M | **4.35%** | "Delivery" line; S&H "including transportation costs by third party providers" | "All costs related to shipping and handling of products to customers, including transportation costs by third party providers" | N-AT24 | *verified* (10-K) |
| 20 | **Appvion** (Paperweight Development Corp.; coated and specialty papers sold mainly through merchant distributors) | SG4 | 2016 | $690.4M | $36.0M | **5.21%** | XBRL tag | quote not read | N-AT25 | *verified* (XBRL) |
| 21 | **Myers Industries** (plastic containers; tire-repair distribution) | SG4 | 2016 | $558.062M | $16.8M | **3.01%** | XBRL tag; both from the same filing | quote not read | N-AT26 | *verified* (XBRL) |
| 22 | **Tredegar** (plastic films; aluminium extrusions) | SG4 (partly metals) | 2017 | $961.330M | $33.683M | **3.50%** | XBRL tag | quote not read | N-AT27 | *verified* (XBRL) |
| 23 | **Huttig Building Products** (building-materials distributor) | SG5 | 2017 | $753.2M | $34.0M | **4.51%** | S&H to customers; operating expense | "Costs associated with shipping and handling products to the Company's customers are charged to operating expense." "Shipping and handling costs were $34.0 million" | N-AT28 | *verified* (10-K, R24) |
| 24 | **PGT Innovations** (impact-resistant windows and doors) | SG5 | 2017 | $511.081M | $20.6M | **4.03%** | finished-goods S&H in SG&A; **inbound shipping in cost of sales, no amount** | "Costs relating to shipping and handling of our finished products are included in selling, general and administrative expenses" "totaled $20.6 million" | N-AT29 | *verified* (10-K) |
| 25 | **Advanced Drainage Systems** (plastic pipe) | SG5 | Mar 2018 | $1,330.354M | $133.8M | **10.06%** | XBRL tag; **own fleet**: "approximately 700 tractors and approximately 1,200 trailers" | "We deliver products to many of our customers through our own fleet of vehicles." | N-AT30 | *verified* (XBRL; 10-K) |
| 26 | **Intrepid Potash** (potash and Trio fertilizer) | SG6 | 2017 | $157.607M | $29.039M | **18.42%** (2016: 17.19%) | freight on delivered sales, billed on to customers and inside gross sales | "When a sale occurs on a delivered basis, we incur and, in turn, bill the customer and record as gross revenue the product sales value, freight" | N-AT31 | *verified* (10-K) |
| 27 | **Compass Minerals** (road salt; plant nutrition, $585M of its sales) | SG6 (salt is outside) | 2017 | $1,364.4M | $267.5M | **19.61%** | S&H cost, company-wide; no segment split read | "Shipping and handling cost / 267.5 / 244.9" ; "Sales / $ 1,364.4 / $ 1,138.0" | N-AT32 | *verified* (10-K) |
| 28 | **Oil-Dri Corp. of America** (clay cat litter, ag and animal-health carriers) | SG6 / SG3 | Jul 2017 | $262.307M | $39.226M | **14.95%** | XBRL tag | quote not read | N-AT33 | *verified* (XBRL) |
| 29 | **American Vanguard** (crop-protection chemicals) | SG6 | 2017 | $355.047M | $27.75M | **7.82%** | XBRL tag | quote not read | N-AT34 | *verified* (XBRL) |
| 30 | **Omega Protein** (fish meal and oil for feed and nutrition) | SG6 | 2016 | $390.831M | $10.2M | **2.61%** | XBRL tag | quote not read | N-AT35 | *verified* (XBRL) |

### AT1.3 Ratio range by segment [our calc]

| Segment | Firms in the range | Low | **Median** | High | Notes |
|---|---|---|---|---|---|
| **SG1** distributors | 3 (+4 above the range) | 0.63% | **1.76%** (1.62% with the four larger ones) | 4.68% | Two of the three in-range firms are fastener distributors. Parcel and own trucks are inside or beside these figures |
| **SG2** capital goods, consumer durables | 7 | 2.21% | **3.42%** (3.1% without Virco) | 5.05% (Virco 10.20% with classroom delivery) | Mostly prepaid outbound; parcel included |
| **SG3** food, beverage, household | 8 | 2.09% | **4.31%** (freight-out measures) | 8.53% | Up to 10.5-10.6% where warehousing or a "Distribution" line is reported |
| **SG4** packaging and paper | 4 | 3.01% | **3.93%** | 5.21% | Large paper firms run higher **[our call]**; KapStone, above the range, tagged $299.9M in 2017 (revenue not read) |
| **SG5** building materials | 3 | 4.03% | **4.51%** | 10.06% (own fleet) | Only three firms |
| **SG6** agribusiness | 5 | 2.61% | **14.95%** | 19.61% | The top three are bulk minerals with freight passed on to customers. **For SG6's target firms (feed, ag chemicals, farm supplies) the closer cases are 2.6% and 7.8%** **[our call]** |

**Recent versus 2016-17:** EACO 1.76% → 1.49%; WD-40 4.31% → 2.94%; Tootsie 8.53% → 7.84% (now including warehousing); J&J Snack Foods 7.55% (S&H) → 10.63% ("Distribution", a wider line). Where the measure is the same, the 2025 ratios are no higher than in 2017 **[our calc]**.

### AT1.4 Inbound freight

- **No firm read discloses an inbound freight amount.** PGT says inbound shipping for materials is in cost of sales, with no figure [N-AT29]. Inbound freight sits inside inventory cost, as the brief expected.
- The neutral measure of inbound freight is BEA's Use table (§AT2.3).

### AT1.5 Reading [our call]

1. **Outbound freight at small and mid-sized public makers runs about 2-5% of revenue in SG2-SG5, a little higher in food (SG3), and 1-2% at distributors (SG1)** once parcel-heavy and own-fleet cases are set aside. Bulk minerals (potash, salt, clay) run 15-20% and are not typical of SG6's target firms.
2. **These are not TL+LTL figures.** They include parcel, sometimes the firm's own trucks, sometimes packing and warehousing, and they leave out inbound freight. §AT3 and §AT5 convert them.
3. **The 2016-17 data are old but not stale**, because the four firms re-read in 2025 show similar or lower ratios.

---

## §AT2 · Other real documents and neutral benchmarks

### AT2.1 Two new bankruptcy payment lists

Found through the CourtListener RECAP search API (free public court PDFs). Of nine filings opened, two had a readable SOFA with payees for a distributor or maker. **Annualised = 90-day total × 365/90 [our calc].** Distressed firms pay irregularly, and payees under the SOFA threshold are left out ($7,575 on Instant Brands' form; $6,825 for a 2021 filing such as WB Supply's, per check AD).

| Firm (court, petition) | What it does | Revenue (SOFA Part 1) | Freight payees in 90 days | **Annualised** | % of revenue | What else the list shows | Claim |
|---|---|---|---|---|---|---|---|
| **WB Supply LLC** (Bankr. D. Del. 21-10729, 2021-04-20) | Oilfield pipe, valve and fittings distributor (SG1-like; energy end market) | 2019: $218,633,590; 2020: **$98,552,915**; 2021 to filing: $14,109,542 (110 days; **~$46.8M** a year **[our calc]**) | **$57,375.48** to four payees: Ally Global Logistics $20,761.95; Saia $15,963.03; Pradon Construction & Trucking $12,400.50; USA Logistics $8,250.00 | **~$0.23M** | **0.24%** of 2020; **0.50%** of the 2021 run-rate | **Own fleet:** WEX Fleet (fuel cards) $86,181.46 and Enterprise Fleet Management $149,715.92 in the same 90 days, **~$0.96M a year**, about **4×** its for-hire trucking **[our calc]** | N-AT36 |
| **Instant Brands LLC** (Bankr. S.D. Tex. 23-90716, 2023-06-12; this entity's SOFA only) | Small kitchen appliances and housewares, imported (SG2 consumer durables) | 2021: $558,910,180.94; **2022: $524,423,763.92** | 32 payees whose stated reason is "FREIGHT": **$7,401,282**. Without 3PL warehouses (Körber $2,333,831 and two others) and TMS software (BluJay $46,493): **$4,966,623** of transport | **~$20.1M** of transport | **3.84%** | **By mode [our calc, classes our call]:** parcel (UPS, UPS Mail Innovations, FedEx) **45.0%**; ocean carriers **31.5%**; port drayage 8.0%; customs and forwarding 5.1%; unclear 4.8%; **LTL (TForce, Old Dominion, Estes) 2.4%**; **TL and brokers (Werner, Autumn Logistics, BNSF Logistics) 2.3%**; rail 1.1%. **TL+LTL $0.94M a year (0.18% of revenue), $2.54M with drayage (0.48%)** | N-AT37 |

**With the twelve on file:** checks AD and AN hold nine small makers and distributors ($31-389k of LTL a year, median ~0.7% of revenue, LTL carriers only) and three mid-sized ones (trucking payees $1.53-1.91M a year, 0.9-4.8% of revenue). **The public record now holds 14 bankrupt firms.** Their all-trucking ratios cluster at **2.9-4.1%** for the three domestic mid-sized makers and distributors, and fall to **0.2-0.5%** for a distributor running its own fleet and an importer whose freight is parcel and ocean **[our calc]**.

### AT2.2 What the two new lists add [our call]

- **Own fleets hide freight from C-09.** WB Supply's for-hire trucking was about a fifth of its trucking cost. A distributor's local deliveries on its own trucks produce no carrier bills to audit.
- **Importers that sell through parcel and big retailers buy little TL or LTL.** Instant Brands spent 3.8% of revenue on transport, but under 0.5% on TL+LTL even with drayage. One likely reason is that big-box retailers often route and pay inbound freight themselves (collect). This is **[our call]**; the SOFA does not say who paid for outbound loads.
- **A TMS appears in the payee list** (BluJay Solutions, $46,493 in 90 days) at a $524M firm. That is consistent with check Y's view that TMS use starts at larger shippers.

### AT2.3 Neutral benchmark: what industries pay for freight on their inputs (BEA Use table)

- **What it measures.** In BEA's input-output accounts, goods are valued at producers' prices and "Transportation costs and wholesale and retail trade margins are treated separately" "as commodities that are produced by industries and purchased by intermediate and final users." [N-AT38] **Our reading [our call]:** an industry's "truck transportation" purchase is therefore the for-hire trucking of the goods it buys (its **inbound** freight, whoever arranged it), plus trucking it buys directly. Own trucks are not in it. Parcel ("couriers and messengers") shows near zero for manufacturers and looks unreliable here. For wholesalers it misses the freight on goods bought for resale.
- **2023, summary industries** (BEA's annual Use table, before redefinitions, producers' value; ratios to each industry's output **[our calc]**) [N-AT39]:

| Industry (BEA summary) | Output 2023 | **For-hire truck** | Rail | Water | Air | All purchased transport | Truck's share of it |
|---|---|---|---|---|---|---|---|
| Farms | $555.3B | **2.24%** | 0.51% | 0.21% | 0.04% | 3.04% | 74% |
| Food, beverage and tobacco (SG3) | $1,179.8B | **3.28%** | 0.60% | 0.16% | 0.07% | 4.16% | 79% |
| Wood products (SG5) | $168.7B | **2.02%** | 0.61% | 0.01% | 0.12% | 3.36% | 60% |
| Paper products (SG4) | $203.4B | **1.78%** | 1.17% | 0.05% | 0.10% | 3.43% | 52% |
| Chemical products (incl. fertilizer, cleaning) | $1,029.4B | **0.81%** | 0.48% | 0.08% | 0.05% | 1.48% | 54% |
| Plastics and rubber (SG4 in part) | $298.6B | **1.14%** | 0.71% | 0.04% | 0.16% | 2.31% | 49% |
| Nonmetallic mineral products (SG5) | $161.8B | **3.02%** | 1.35% | 0.24% | 0.37% | 5.64% | 54% |
| Machinery (SG2) | $452.0B | **1.00%** | 0.14% | 0.02% | 0.07% | 1.23% | 81% |
| Electrical equipment and appliances (SG2) | $168.1B | **1.10%** | 0.19% | 0.04% | 0.05% | 1.38% | 79% |
| Furniture (SG2) | $80.9B | **1.78%** | 0.33% | 0.02% | 0.11% | 2.57% | 69% |
| *Contrast:* primary metals / fabricated metals / motor vehicles and parts | $318.9B / $431.6B / $777.1B | **3.14% / 1.08% / 1.22%** | 1.17 / 0.26 / 0.19% | | | 4.66 / 1.48 / 1.51% | 67 / 73 / 81% |
| *Wholesale trade (freight on resale goods not captured)* | $2,840.6B | 0.37% | 0.01% | 0.00% | 0.25% | 3.49% (mostly "other transportation and support", which holds couriers) | 10% |

- **2017, detailed industries close to the segments** (BEA benchmark Use table) [N-AT40]: for-hire truck as % of output **[our calc]**:
  - SG2: HVAC equipment 1.08%; major household appliances 0.90%; upholstered furniture 2.44%; institutional furniture 1.55%; mechanical power transmission 1.00%.
  - SG3: frozen food 2.29%; fruit and vegetable canning 1.73%; snack food 2.17%; coffee and tea 3.17%; soft drinks 1.08%; breweries 1.52%; soap and cleaning compounds 0.75%.
  - SG4: paperboard mills 1.71% (rail 1.50%); paperboard containers 2.01%; plastics bottles 1.02%; plastics packaging film 1.07%.
  - SG5: sawmills 2.47%; millwork 1.85%; cement 1.42% (rail 2.40%); ready-mix concrete 4.31%; lime and gypsum 1.92% (rail 2.81%).
  - SG6: other animal food 2.88% (rail 2.42%); flour milling 4.06% (rail 4.87%); soybean processing 5.23%; fertilizer 1.20% (rail 1.03%); pesticides 0.87%.
- **Other benchmarks on file:** Establish Davis, transportation 3.68% of sales on average, inbound and outbound, participating firms (N-X21, *verified* as published, a voluntary sample); the CPA firm's "3 percent of gross sales on inbound" and "7 percent of net sales on outbound" for distributors (N-Y20, *assumed*, 2011).
- **CSCMP's 2026 State of Logistics** (via Supply Chain Digest, *assumed*): US business logistics costs **$2.40 trillion, 7.8% of GDP** in 2025; parcel **$241.3B** (2025) and $229.5B (2024); rail **$97.3B**; trucking 59.5% of transportation costs; transportation 61.8% of logistics costs [N-AT41].

### AT2.4 Reading [our call]

1. **Inbound freight is real money for makers.** By BEA's measure the freight on manufacturers' inputs by for-hire truck runs **1-3% of output** (more in food, minerals and feed). Added to the 2-5% outbound figures in AT1, total freight lands near **3-6% of revenue**, which fits Establish Davis's 3.68% and the 2.9-4.1% of the three domestic mid-sized bankrupt firms.
2. **Only part of the inbound reaches the firm as a carrier bill.** When a supplier ships prepaid or prices delivered, the buyer gets no freight bill. AT5 therefore counts **25/50/75%** of BEA's inbound truck figure as bills the firm pays itself **[our call]**.
3. **Two firm shapes break the average:** distributors with their own fleets and importers selling through parcel and retailers. A screener question on "own trucks" and "who pays outbound freight" would catch both (kit §12 Q3 asks spend only).

---

## §AT3 · Mode split: what share of freight dollars is TL+LTL

| Level | Source | TL+LTL share | Parcel | Own fleet | Rail / ocean / other | Label |
|---|---|---|---|---|---|---|
| **US, all shippers, 2024** | CSCMP via FreightWaves (N-K22) and Supply Chain Digest (N-AT41): TL $387B, LTL $64B, private fleets $541.4B, parcel $229.5B, rail $97.3B | **58%** of TL+LTL+parcel+rail; **34%** if private fleets are counted **[our calc]** | 30% / 17% | — / 41% | rail 13% / 7% | inputs *assumed*; shares **[our calc]** |
| US, by value moved, 2022 | CFS (scan E): for-hire truck 44.8%, own trucks 23.0%, parcel 13.4%, customer pick-up 5.7% of shipment value | value moved, not spend | — | — | — | *verified* (known) |
| **Manufacturers' inbound, by industry, 2023** | BEA Use table (§AT2.3) | truck = **49-81%** of purchased transport (machinery 81%, food 79%, furniture 69%, paper 52%, plastics 49%); fertilizer 37% and flour milling 39% in 2017 | unreliable | not covered | rail most of the rest | *verified* data; **[our calc]** |
| Latex Foam International, 2014 (N-AN22) | trucking payees $376,933 vs UPS $175,665 in 90 days | **68%** of trucking + parcel (brokers 51% of trucking) | 32% | — | — | *verified* (known); **[our calc]** |
| United Gilsonite, 2011 (N-AN23) | $454,620 vs UPS $13,601 | **97%** | 3% | — | — | *verified* (known); **[our calc]** |
| Agway Farm & Home Supply, 2022 (N-AN24) | $464,933 vs FedEx $1,492 | **99.7%** | 0.3% | — | — | *verified* (known); **[our calc]** |
| **Instant Brands LLC, 2023** (N-AT37) | transport payees $4.97M in 90 days | **4.7%** (12.6% with drayage) | 45% | — | ocean 31.5% | *verified*; **[our calc]** |
| **WB Supply, 2021** (N-AT36) | for-hire $57k vs fleet costs $236k in 90 days | **20%** of for-hire + fleet | — | ~80% | — | *verified*; **[our calc]** |
| Filings (AT1) | Virco: "third party carriers for more than 90% of customer deliveries"; ADS: "our own fleet of vehicles", ~700 tractors; Intrepid relies "heavily upon truck and rail" | — | — | — | — | *verified* |

**Proposed TL+LTL share of a firm's outbound freight, by segment [our call]** (used in AT5):

| Segment | Low / **central** / high | Why |
|---|---|---|
| SG1 distributors | 25 / **40** / 55% | Parcel is about half of wholesalers' shipments (CFS, check Y §3.2); own trucks for local delivery (WB Supply; durable-goods wholesalers move 43% of tons on own trucks, check X §7.3). Same as check X's wholesaler input |
| SG2 capital goods, durables | 45 / **65** / 80% | BEA truck share 69-81%; CFS shows LTL and parcel, almost no full loads (check Y §3.3). Importers and direct-to-consumer brands fall far below (Instant Brands 5-13%) |
| SG3 food, household | 45 / **60** / 75% | Mixed TL and LTL; some DSD fleets; parcel 23% of shipments for prepared food (check Y §3.1) |
| SG4 packaging, paper | 45 / **60** / 75% | Paper mills use rail (BEA rail ≈ truck); box plants deliver locally, often on own trucks |
| SG5 building materials | 35 / **55** / 70% | Own fleets common (ADS); cement and gypsum use rail |
| SG6 agribusiness | 35 / **50** / 65% | Rail and barge for bulk (BEA: rail ≥ truck in flour milling); feed mills deliver on their own trucks |

**Reading [our call]:** no filing splits freight by mode, and the payment lists show the split is **a property of each firm** (TL+LTL from 5% to 99.7% of trucking-plus-parcel). The segment shares above are judgement calls anchored on the national and BEA splits. The interview's spend question already asks for TL, LTL and parcel separately (`C09-open-questions-evidence.md` §0, A1); that answer replaces these for any real prospect.

---

## §AT4 · Four named shippers

Held outside the project in `~/Documents/personal/bio/freight_private/c09_shipper_sizes.md` (kit §1.3), as instructed.

---

## §AT5 · Conversion table: revenue → TL+LTL spend [our calc]

> **Two warnings before using these numbers.** (1) **Public firms are larger than the target**: the AT1 firms have $38M-$1.46B of revenue and most are above $100M. (2) **Disclosed freight usually leaves out inbound freight**, and often includes parcel, own trucks or warehousing. The table corrects for both with judgement calls; it is an estimate, not a measurement.

### AT5.1 The formula and inputs

**TL+LTL as % of revenue = O × s + I × p**, where:
- **O** = outbound freight as % of revenue (AT1 quartiles, rounded) *verified* filings, **[our calc]**;
- **s** = TL+LTL share of outbound (§AT3) **[our call]**;
- **I** = for-hire truck freight on purchased inputs as % of output (BEA, §AT2.3) *verified* data, **[our calc]**; for SG1 distributors BEA cannot measure it, so it is **[our call]** (0.5 / 1.0 / 2.0%; below the CPA firm's 3% for all inbound modes, because many suppliers prepay);
- **p** = share of that inbound arriving on bills the firm pays itself, 25 / 50 / 75% **[our call]**.

"Low" multiplies all the low inputs together and "high" all the high ones, as check X did, so the ranges are wide on purpose.

| Segment | O low / central / high | s | I | **TL+LTL % of revenue: low / central / high** | TL+LTL per $100M of revenue |
|---|---|---|---|---|---|
| **SG1** distributors | 0.8 / 1.6 / 4.2% | 25 / 40 / 55% | 0.5 / 1.0 / 2.0% | 0.8×0.25+0.5×0.25 = **0.33%** / 1.6×0.40+1.0×0.50 = **1.14%** / 4.2×0.55+2.0×0.75 = **3.81%** | $0.33M / **$1.14M** / $3.81M |
| **SG2** capital goods, durables | 2.5 / 3.1 / 5.1% | 45 / 65 / 80% | 1.0 / 1.1 / 1.8% | 1.125+0.25 = **1.38%** / 2.015+0.55 = **2.57%** / 4.08+1.35 = **5.43%** | $1.38M / **$2.57M** / $5.43M |
| **SG3** food, household | 3.1 / 4.3 / 7.5% | 45 / 60 / 75% | 1.0 / 2.5 / 3.3% | 1.395+0.25 = **1.65%** / 2.58+1.25 = **3.83%** / 5.625+2.475 = **8.10%** | $1.65M / **$3.83M** / $8.10M |
| **SG4** packaging, paper | 3.0 / 3.9 / 5.2% | 45 / 60 / 75% | 1.1 / 1.8 / 2.0% | 1.35+0.275 = **1.63%** / 2.34+0.90 = **3.24%** / 3.90+1.50 = **5.40%** | $1.63M / **$3.24M** / $5.40M |
| **SG5** building materials | 4.0 / 4.5 / 10.1% | 35 / 55 / 70% | 1.5 / 2.0 / 3.0% | 1.40+0.375 = **1.78%** / 2.475+1.00 = **3.48%** / 7.07+2.25 = **9.32%** | $1.78M / **$3.48M** / $9.32M |
| **SG6** agribusiness | 2.6 / 7.8 / 15.0% | 35 / 50 / 65% | 1.0 / 2.5 / 4.0% | 0.91+0.25 = **1.16%** / 3.90+1.25 = **5.15%** / 9.75+3.00 = **12.75%** | $1.16M / **$5.15M** / $12.75M |

**Where the inputs come from:** O for SG6 uses American Vanguard's 7.8% as the central, not the 15% median, because the top three SG6 firms are bulk minerals (§AT1.3) **[our call]**. I comes from BEA 2023: machinery 1.00%, electrical 1.10%, furniture 1.78% (SG2); food 3.28%, soap 0.75% (SG3); paper 1.78%, plastics 1.14%, paperboard containers 2.01% (SG4); wood 2.02%, nonmetallic minerals 3.02% (SG5); animal food 2.88%, flour milling 4.06%, fertilizer 1.20% (SG6).

**Cross-check against real firms [our calc]:**

| Real firm | Revenue | Actual trucking (TL+LTL+brokers) | Table's central for its segment | Fit |
|---|---|---|---|---|
| Latex Foam (foam maker; SG2/SG4-like) | $53M | ~$1.53M (2.86%) | SG2 2.57% → $1.37M | **close** |
| United Gilsonite (coatings; SG3-like household) | $45M | ≥$1.84M (≥4.10%) | SG3 3.83% → $1.72M | **close** |
| Agway Farm & Home Supply (SG6 distributor) | $48-221M | ~$1.89M (0.85-3.96%) | SG6 5.15% → $2.5-11.4M | **too high** for a distributor |
| WB Supply (SG1-like distributor) | $47-99M | ~$0.23M (0.24-0.50%), plus ~$0.96M own fleet | SG1 1.14% → $0.53-1.12M | **too high** (own fleet) |
| Instant Brands LLC (SG2 importer) | $524M | ~$0.94M TL+LTL; $2.54M with drayage | SG2 2.57% → $13.5M | **far too high** (parcel, ocean, retailer-routed) |

The table fits domestic makers that ship prepaid, and it overstates distributors with own fleets and importers selling through parcel and big retailers.

### AT5.2 Revenue needed for each TL+LTL spend level

Revenue = spend ÷ TL+LTL % **[our calc]**. Central first; the range in brackets uses the high and low percentages.

| TL+LTL spend a year | **SG1** distributors | **SG2** capital goods, durables | **SG3** food, household | **SG4** packaging, paper | **SG5** building materials | **SG6** agribusiness |
|---|---|---|---|---|---|---|
| **$1M** | **$88M** ($26-308M) | **$39M** ($18-73M) | **$26M** ($12-61M) | **$31M** ($19-62M) | **$29M** ($11-56M) | **$19M** ($8-86M) |
| **$1.5M** | **$132M** ($39-462M) | **$58M** ($28-109M) | **$39M** ($19-91M) | **$46M** ($28-92M) | **$43M** ($16-85M) | **$29M** ($12-129M) |
| **$2M** | **$175M** ($52-615M) | **$78M** ($37-145M) | **$52M** ($25-122M) | **$62M** ($37-123M) | **$58M** ($21-113M) | **$39M** ($16-172M) |
| **$3M** | **$263M** ($79-923M) | **$117M** ($55-218M) | **$78M** ($37-182M) | **$93M** ($56-185M) | **$86M** ($32-169M) | **$58M** ($24-259M) |
| **$5M** | **$439M** ($131M-1.5B) | **$195M** ($92-364M) | **$131M** ($62-304M) | **$154M** ($93-308M) | **$144M** ($54-282M) | **$97M** ($39-431M) |
| **$10M** | **$877M** ($262M-3.1B) | **$390M** ($184-727M) | **$261M** ($123-608M) | **$309M** ($185-615M) | **$288M** ($107-563M) | **$194M** ($78-862M) |

### AT5.3 How many US firms sit above each line

- **Source:** Census SUSB 2022, firms by **enterprise receipts size** for each NAICS code (N-AT42), and the sector-level split of the $100M+ class into $100-250M, $250-500M, $500M-1B, $1-2.5B and $2.5B+ for manufacturing and wholesale (N-AT43). *verified* tables.
- **Firms by receipts band, 2022** (segment NAICS as in check Y §3.1; SG3 = 311 less 3111 and 3112, plus 3121 and 3256) **[our calc]**:

| Segment | All firms | Under $10M | $10-20M | $20-50M | $50-100M | **$100M+** |
|---|---|---|---|---|---|---|
| SG1 (4237, 42361, 42384) | 22,449 | 17,115 | 1,911 | 1,537 | 676 | **1,210** |
| SG2 (333, 335, 337) | 37,665 | 30,686 | 2,459 | 1,994 | 813 | **1,713** |
| SG3 (311 excl. 3111-3112, 3121, 3256) | 37,448 | 33,030 | 1,357 | 1,181 | 612 | **1,268** |
| SG4 (322, 32611, 32616, 4241) | 9,201 | 6,553 | 781 | 773 | 380 | **714** |
| SG5 (321, 327, 4233) | 30,892 | 24,426 | 2,423 | 1,918 | 812 | **1,313** |
| SG6 (3111, 3112, 3253, 42491, 4245) | 10,855 | 7,277 | 950 | 941 | 512 | **1,175** |
| *All manufacturing (31-33)* | 239,265 | 203,179 | 13,250 | 10,755 | 4,617 | **7,464** |
| *All wholesale (42)* | 277,932 | 223,250 | 20,169 | 16,483 | 7,454 | **10,576** |

- Sector split of the $100M+ class: manufacturing 3,527 / 1,464 / 980 / 715 / 778 and wholesale 5,424 / 2,159 / 1,215 / 847 / 931 firms at $100-250M / $250-500M / $500M-1B / $1-2.5B / $2.5B+ (N-AT43).
- **Firms at or above each spend line, central case [our calc]** (range in brackets from the high and low percentages). Within a receipts class, firms are spread evenly; above $100M each segment gets its sector's split.

| TL+LTL spend line | SG1 | SG2 | SG3 | SG4 | SG5 | SG6 | **Six segments** |
|---|---|---|---|---|---|---|---|
| **≥ $1M** | 1,330 (532-2,891) | 2,935 (2,033-4,818) | 2,674 (1,712-4,022) | 1,455 (980-1,953) | 3,146 (1,993-6,238) | 2,673 (1,286-3,914) | **~14,200** |
| **≥ $1.5M** | 1,079 (380-2,224) | 2,342 (1,664-3,666) | 2,156 (1,346-3,213) | 1,148 (755-1,560) | 2,367 (1,493-4,717) | 2,218 (1,067-3,379) | **~11,300** |
| ≥ $2M | 898 | 1,952 | 1,845 | 979 | 1,968 | 1,931 | ~9,600 |
| ≥ $3M | 576 | 1,621 | 1,460 | 754 | 1,472 | 1,584 | ~7,500 |
| **≥ $5M** | 403 (169-1,081) | 1,201 (751-1,799) | 1,146 (615-1,697) | 592 (344-754) | 1,131 (660-2,049) | 1,198 (453-1,921) | **~5,700** |
| **≥ $10M** | 238 (107-577) | 716 (465-1,259) | 658 (384-1,174) | 344 (215-522) | 654 (413-1,283) | 826 (278-1,348) | **~3,400** |
| **$1.5-10M band** | 841 | 1,626 | 1,498 | 804 | 1,713 | 1,392 | **~7,900** |

**Caveats on the counts [our call]:**
- **These are firm-industry entries, not distinct firms.** SUSB counts a firm in every industry where it has an establishment, and the size class is the whole enterprise's receipts. A $5B group with one plant in SG2 counts as an SG2 firm above every line. The large-firm counts are therefore too high, and the six-segment sums double-count.
- **Wholesale receipts include the resale value of goods,** and SG4, SG5 and SG6 mix wholesalers into percentages built mostly on makers. Their counts are too high at the lower lines.
- **Firms above about $10M of TL+LTL are where FAP providers' stated floors begin** (check Y §2.1: "$10 million and $1 billion"; "at least $10 million"). The **$1.5-10M band, about 7,900 entries**, sits below the floors that audit-and-pay firms state, and across it C-09's pass line falls from 6.44% (at $1.5M) to 2.03% (at $5M).

### AT5.4 Reading [our call]

1. **The founders' intuition holds: spend drives the room.** C-09's pass line falls as spend rises (6.44% at $1.5M, 2.03% at $5M). The revenue that buys that spend differs by segment by a factor of four.
2. **For a screen on revenue alone:** an SG2-SG6 maker with **$40-60M or more of revenue** has a central TL+LTL spend near $1.5M; **$100-200M** puts it near $5M. A distributor (SG1) needs **$130M+** for $1.5M.
3. **Revenue is a weak screen on its own.** Real firms of the same size range from $0.2M to $1.9M of trucking (AT5.1 cross-check). Three screener questions would separate them: own trucks or not, who pays outbound freight (prepaid or collect), and how much is parcel. The interview's A1 spend band (TL, LTL and parcel separately) remains the measurement.
4. **The pool is in the thousands, not the hundreds.** Roughly 11,000 firm-industry entries clear $1.5M and about 7,900 sit between $1.5M and $10M. That is the pool the S5 interviews sample from. The counts double-count, and they include firms that already use an FAP or a 3PL.

---

## What the web could not settle

- **TL+LTL as a share of any firm's freight.** No 10-K splits freight by mode; only payment lists do, and only for bankrupt firms.
- **Inbound freight amounts.** None of the 30 firms discloses one.
- **The spread of freight ratios among private firms of $20-200M revenue.** Public firms are larger, and the 14 bankrupt firms are not a sample.
- **Who pays outbound freight (prepaid versus collect or retailer-routed)** in each segment. Not found in any public source read.
- **A current XBRL tag for freight.** The FASB tag was retired in 2018, so later years must be read firm by firm.

## Could not access, or not found

- **Filing notes not reached with the fetch tool** (values taken from the SEC's XBRL API instead, quotes not read): Transcat, Watts Water, Johnson Outdoors, Appvion, Myers Industries, Tredegar, Advanced Drainage Systems (value), Oil-Dri, American Vanguard, Omega Protein. Some filings keep the notes in a separate document.
- **Recent 10-Ks without a stated amount in the parts read:** AAON 2025, Acme United 2025, Oil-Dri FY2026, American Vanguard 2025, John B. Sanfilippo FY2026, Compass Minerals FY2025 (only in parts read), Watts 2025, Johnson Outdoors FY2025, Lawson Products 2018, Houston Wire & Cable 2017 (freight in cost of sales, no amount), DXP 2017, UFP Technologies 2017.
- **Revenue element not found in the XBRL API:** AAON and Encore Wire (AAON read in its 10-K instead; Encore Wire dropped); KapStone (revenue not read; its tagged freight is noted only).
- **EDGAR full-text search** returned HTTP 500 twice for multi-company queries; smaller queries worked.
- **CourtListener's website search** returned 403 to the fetch tool; its public search API worked without a login. Of nine filings opened, Hamilton Scientific (revenue near zero), BWGS and A-1 Plank & Scaffold (scanned images), Partition Systems, Mr. Tortilla and Figueroa Mountain Brewing (petitions without a SOFA), and Champion Laboratories (auto filters, a contrast firm; no revenue line found in the text) were not used.
- **CSCMP's 2026 report** is sold by CSCMP; only a press summary was read. TL, LTL and private-fleet dollars for 2025 were not found in it.
- **BEA's interactive application** was not used; the static zip of all input-output tables (2024 release) was downloaded instead.

---

## Claim ledger

| ID | Question | Claim | Verbatim quote or table value (≤40 words) | URL | Date seen | Label |
|---|---|---|---|---|---|---|
| N-AT01 | AT1 | The US GAAP XBRL tag for freight-out was "Shipping, Handling and Transportation Costs", retired in 2018 | Label "Shipping, Handling and Transportation Costs (Deprecated 2018-01-31)"; description "Cost incurred during the reporting period in transporting goods and services to customers. Includes freight-out costs." | https://data.sec.gov/api/xbrl/companyconcept/CIK0000784539/us-gaap/ShippingHandlingAndTransportationCosts.json | 2026-10-09 | *verified* |
| N-AT02 | AT1 | 345 filers used the tag for calendar 2016 and 284 for 2017 | frame entry counts: 345 (CY2016), 284 (CY2017) | https://data.sec.gov/api/xbrl/frames/us-gaap/ShippingHandlingAndTransportationCosts/USD/CY2016.json ; …/CY2017.json | 2026-10-09 | *verified* |
| N-AT03 | AT1 | EACO's S&H was $2.76M on revenues of $156.954M in FY2017 | "Shipping and handling expenses are included in cost of revenues" … "were approximately $2,760,000 and $2,653,000 for the years ended August 31, 2017 and 2016"; revenues $156,954 (thousands) | https://www.sec.gov/Archives/edgar/data/784539/000114420417060658/tv480016_10k.htm | 2026-10-09 | *verified*; ratio **[our calc]** |
| N-AT04 | AT1 | EACO's S&H was $6.36M on $427.931M in FY2025 (644 staff, seven DCs) | "Shipping and handling expenses are included in cost of revenues and were approximately $6,360,000 and $5,530,000"; revenues $427,931 / $356,231; "644 full-time employees" | https://www.sec.gov/Archives/edgar/data/784539/000110465925114547/eaco-20250831x10k.htm | 2026-10-09 | *verified* |
| N-AT05 | AT1 | Hillman's freight and handling was $39.205M on net sales of $838.368M in 2017 | "The costs incurred to ship product to customers, including freight and handling expenses," … "$39,205 in 2017"; net sales $838,368 | https://www.sec.gov/Archives/edgar/data/1029831/000102983118000006/R26.htm ; …/R4.htm | 2026-10-09 | *verified* |
| N-AT06 | AT1 | Transcat tagged $0.9M for FY2017 on revenue of $143.898M (distribution sales $72.795M) | XBRL value 900000 (end 2017-03-25); Revenues 143,898,000; "Distribution sales … $72,795 (FY2017)" | https://data.sec.gov/api/xbrl/frames/us-gaap/ShippingHandlingAndTransportationCosts/USD/CY2016.json ; https://data.sec.gov/api/xbrl/companyconcept/CIK0000099302/us-gaap/Revenues.json ; https://www.sec.gov/Archives/edgar/data/99302/000120677418001839/trns3429041-10k.htm | 2026-10-09 | *verified* (XBRL) |
| N-AT07 | AT1 | Four larger distributors tagged freight of 0.8-4.2% of sales in FY2017 | MSC 119,979,000 / 2,887,744,000; Applied 20,060,000 / 2,593,746,000; Watsco 47,670,000 / 4,341,955,000; Pool 45,247,000 / 2,788,188,000 | CY2017 frame (above); companyconcept SalesRevenueNet (CIK 1003078, 109563, 945841) and Revenues (CIK 105016) | 2026-10-09 | *verified* (XBRL) |
| N-AT08 | AT1 | Acme United's shipping cost was $6.596M on $130.550M in 2017 | "The costs of shipping product to our customers ($6,595,544 in 2017 and $5,388,481 in 2016)" "are included in selling, general and administrative expenses." | https://www.sec.gov/Archives/edgar/data/2098/000102660818000010/acu_10k123117.htm | 2026-10-09 | *verified* |
| N-AT09 | AT1 | Omega Flex's shipping was $2.562M on $101.799M in 2017 | "The expense relating to shipping was $2,562,000, $2,339,000 and $2,429,000"; "sales for the full year of 2017 were $101,799,000" | https://www.sec.gov/Archives/edgar/data/1317945/000149315218002916/form10-k.htm | 2026-10-09 | *verified* |
| N-AT10 | AT1 | P&F's S&H was $2.017M on $58.974M in 2017 | "and totaled approximately $2,017,000 and $2,013,000, respectively, for the years ended December 31, 2017 and 2016." | https://www.sec.gov/Archives/edgar/data/75340/000114420418017894/tv488997_10k.htm | 2026-10-09 | *verified* |
| N-AT11 | AT1, AT3 | Virco's shipping and classroom delivery was $19.299M on $189.287M; third-party carriers make over 90% of deliveries | "shipping and classroom delivery costs of approximately $19,299,000" ; "Virco depends upon third party carriers for more than 90% of customer deliveries." ; sales $189,287,000 | https://www.sec.gov/Archives/edgar/data/751365/000162828018005275/virc2018131-10k.htm | 2026-10-09 | *verified* |
| N-AT12 | AT1 | Watts tagged $52.1M on net sales of $1,456.7M in 2017 | XBRL 52,100,000; SalesRevenueNet 1,456,700,000 | CY2017 frame; https://data.sec.gov/api/xbrl/companyconcept/CIK0000795403/us-gaap/SalesRevenueNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT13 | AT1 | Johnson Outdoors tagged $10.844M on $490.565M in FY2017 | XBRL 10,844,000; SalesRevenueNet 490,565,000 | CY2017 frame; https://data.sec.gov/api/xbrl/companyconcept/CIK0000788329/us-gaap/SalesRevenueNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT14 | AT1 | AAON's S&H "fees" were $11.4M on net sales of $405.232M in 2017, booked in cost of sales | "shipping and handling fees amounted to approximately $11.4 million," ; "recorded in cost of sales" ; net sales $405,232 | https://www.sec.gov/Archives/edgar/data/824142/000082414218000021/aaon2017annualreport.htm | 2026-10-09 | *verified*; meaning ambiguous **[our call]** |
| N-AT15 | AT1 | Tootsie Roll tagged $43.973M on net product sales of $515.674M in 2017 | XBRL 43,973,000; SalesRevenueGoodsNet 515,674,000 | https://data.sec.gov/api/xbrl/companyconcept/CIK0000098677/us-gaap/ShippingHandlingAndTransportationCosts.json ; …/SalesRevenueGoodsNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT16 | AT1 | Tootsie Roll's freight, delivery and warehousing was $56.780M, 7.8% of net product sales, in 2025 | "Selling, marketing and administrative expenses include freight, delivery and warehousing expenses." "These expenses decreased from $57,581 in 2024 to $56,780 in 2025" ; "from 8.0% in 2024 to 7.8% in 2025" | https://www.sec.gov/Archives/edgar/data/98677/000110465926021621/tr-20251231x10k.htm | 2026-10-09 | *verified* |
| N-AT17 | AT1 | WD-40 paid third parties $18.2M for shipment on net sales of $619.985M in FY2025 ($16.4M on $380.506M in FY2017) | "we exclude the portion associated with amounts paid to third parties for shipment to our customers" … "These costs totaled $18.2 million and $17.3 million" | https://www.sec.gov/Archives/edgar/data/105132/000010513225000067/wdfc-20250831.htm ; companyconcept CIK 105132 | 2026-10-09 | *verified* |
| N-AT18 | AT1 | J&J Snack Foods tagged $81.824M on $1,084.224M in FY2017; its "Distribution" line was $168.305M on $1,583.233M in FY2025 | XBRL 81,824,000; SalesRevenueNet 1,084,224,000; FY2025 table: Distribution 168,305; net sales 1,583,233 | https://www.sec.gov/Archives/edgar/data/785956/000143774925036456/jjsf20250927_10k.htm ; companyconcept CIK 785956 | 2026-10-09 | *verified* |
| N-AT19 | AT1 | John B. Sanfilippo's S&H was $20.418M on $888.595M in FY2018 | "Shipping and handling costs, which include freight and other expenses to prepare finished goods for shipment, are included in selling expenses." Table: $20,418 / $17,682 | https://www.sec.gov/Archives/edgar/data/880117/000119312518255065/d582081d10k.htm | 2026-10-09 | *verified* |
| N-AT20 | AT1 | Coffee Holding's shipping was $2.412M on $77.128M in FY2017 | "Costs associated with shipping product to customers aggregating approximately $2,412,000 and $1,506,000" ; net sales $77,127,595 | https://www.sec.gov/Archives/edgar/data/1007019/000149315218001192/form10-k.htm | 2026-10-09 | *verified* |
| N-AT21 | AT1 | Scott's Liquid Gold's S&H, mainly freight-out, was $2.614M on $42.186M in 2017 | "Shipping and handling costs totaled $2,614,300 and $1,799,900" ; "comprised primarily of freight-out as selling expenses." | https://www.sec.gov/Archives/edgar/data/88000/000156459018007324/slgd-10k_20171231.htm | 2026-10-09 | *verified* |
| N-AT22 | AT1 | Ocean Bio-Chem's S&H was $1.226M on $38.933M in 2017, in COGS | "Shipping and handling costs totaled approximately $1,226,000 and $1,120,000" | https://www.sec.gov/Archives/edgar/data/350737/000121390018003739/f10k2017_oceanbiochem.htm | 2026-10-09 | *verified* |
| N-AT23 | AT1 | Reed's delivery and handling was $3.942M on $37.714M in 2017, including labour and warehouse costs | "an increase in freight charges of $173,000 and additional labor related charges of $48,000" ; XBRL 3,942,000 | https://www.sec.gov/Archives/edgar/data/1140215/000149315218004464/form10k.htm | 2026-10-09 | *verified* |
| N-AT24 | AT1 | AEP's delivery expense was $47.690M on $1,095.830M in FY2016 | "All costs related to shipping and handling of products to customers, including transportation costs by third party providers" ; Delivery 47,690; net sales 1,095,830 | https://www.sec.gov/Archives/edgar/data/785787/000119312517010915/d249630d10k.htm | 2026-10-09 | *verified* |
| N-AT25 | AT1 | Appvion tagged $36M on net sales of $690.4M in 2016 | XBRL 36,000,000; "2016: $690.4 million" | CY2016 frame; https://www.sec.gov/Archives/edgar/data/1166365/000116636517000006/c365-20161231x10k.htm | 2026-10-09 | *verified* (XBRL) |
| N-AT26 | AT1 | Myers tagged $16.8M on $558.062M in 2016 (same filing) | XBRL 16,800,000 and SalesRevenueNet 558,062,000, accession 0001564590-17-003837 | https://data.sec.gov/api/xbrl/companyconcept/CIK0000069488/us-gaap/ShippingHandlingAndTransportationCosts.json ; …/SalesRevenueNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT27 | AT1 | Tredegar tagged $33.683M on $961.330M in 2017 | XBRL 33,683,000; SalesRevenueGoodsNet 961,330,000 | CY2017 frame; https://data.sec.gov/api/xbrl/companyconcept/CIK0000850429/us-gaap/SalesRevenueGoodsNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT28 | AT1 | Huttig's S&H was $34.0M on $753.2M in 2017, in operating expense | "Shipping and handling costs were $34.0 million, $30.2 million and $28.8 million in 2017, 2016 and 2015, respectively." | https://www.sec.gov/Archives/edgar/data/1093082/000156459018004735/R24.htm | 2026-10-09 | *verified* |
| N-AT29 | AT1 | PGT's finished-goods S&H was $20.6M on $511.081M in 2017; inbound is in cost of sales | "Costs relating to shipping and handling of our finished products are included in selling, general and administrative expenses" "totaled $20.6 million" | https://www.sec.gov/Archives/edgar/data/1354327/000119312518082384/d451998d10k.htm | 2026-10-09 | *verified* |
| N-AT30 | AT1, AT3 | ADS tagged $133.8M on $1,330.354M in FY2018 and runs ~700 tractors | "We deliver products to many of our customers through our own fleet of vehicles." ; "approximately 700 tractors and approximately 1,200 trailers" | https://www.sec.gov/Archives/edgar/data/1604028/000156459018014670/wms-10k_20180331.htm ; CY2017 frame | 2026-10-09 | *verified* |
| N-AT31 | AT1 | Intrepid's freight was $29.039M on sales of $157.607M in 2017, billed on to customers on delivered sales | potash "Less: Freight costs 11,818"; Trio "17,221"; total "29,039"; "When a sale occurs on a delivered basis, we incur and, in turn, bill the customer" | https://www.sec.gov/Archives/edgar/data/1421461/000142146118000007/ipi-12312017x10k.htm | 2026-10-09 | *verified* |
| N-AT32 | AT1 | Compass Minerals' S&H was $267.5M on $1,364.4M in 2017 | "Shipping and handling cost / 267.5 / 244.9" ; "Sales / $ 1,364.4 / $ 1,138.0" ; Plant Nutrition sales $210.0M (N. America) and $375.0M (S. America) | https://www.sec.gov/Archives/edgar/data/1227654/000122765418000031/cmp-20171231x10k.htm | 2026-10-09 | *verified* |
| N-AT33 | AT1 | Oil-Dri tagged $39.226M on $262.307M in FY2017 | XBRL 39,226,000; total net sales $262,307,000 | CY2017 frame; https://www.sec.gov/Archives/edgar/data/74046/000007404617000041/odc10k7312017.htm | 2026-10-09 | *verified* (XBRL) |
| N-AT34 | AT1 | American Vanguard tagged $27.75M on $355.047M in 2017 | XBRL 27,750,000; SalesRevenueNet 355,047,000 | CY2017 frame; https://data.sec.gov/api/xbrl/companyconcept/CIK0000005981/us-gaap/SalesRevenueNet.json | 2026-10-09 | *verified* (XBRL) |
| N-AT35 | AT1 | Omega Protein tagged $10.2M on revenues of $390.831M in 2016 | XBRL 10,200,000 (accession 0001437749-17-003546); revenues $390,831 | https://data.sec.gov/api/xbrl/companyconcept/CIK0001053650/us-gaap/ShippingHandlingAndTransportationCosts.json ; https://www.sec.gov/Archives/edgar/data/1053650/000143774917003546/ome20161231_10k.htm | 2026-10-09 | *verified* (XBRL) |
| N-AT36 | AT2, AT3 | WB Supply paid four trucking payees $57,375.48 in 90 days, against 2020 revenue of $98.6M, and spent $235,897 on its own fleet | "Saia Motor Freight Line Total 15,963.03" ; "Ally Global Logistics, LLC Total 20,761.95" ; "Operating a business $98,552,915.00" ; "Enterprise Fleet Management Total 149,715.92" | https://storage.courtlistener.com/recap/gov.uscourts.deb.184860/gov.uscourts.deb.184860.18.0.pdf | 2026-10-09 | *verified*; classes **[our call]**; annualised **[our calc]** |
| N-AT37 | AT2, AT3 | Instant Brands LLC paid 32 "FREIGHT" payees $7,401,282 in 90 days against 2022 revenue of $524.4M; LTL and TL carriers were under 5% of transport | "TOTAL UNITED PARCEL SERVICE" $2,195,379 ; "TOTAL OLD DOMINION FREIGHT LINES $37,460" ; "TOTAL TFORCE FREIGHT, INC $68,492" ; "Operating a business $524,423,763.92" | https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.432.0.pdf | 2026-10-09 | *verified*; classes **[our call]**; shares **[our calc]** |
| N-AT38 | AT2 | BEA values goods at producers' prices and records transportation as a separate purchase by the users | "These prices exclude wholesale and retail trade margins and transportation costs," … "Transportation costs and wholesale and retail trade margins are treated separately" "as commodities that are produced by industries and purchased by intermediate and final users." | https://www.bea.gov/help/glossary/producers-prices | 2026-10-09 | *verified*; inbound reading **[our call]** |
| N-AT39 | AT2, AT3, AT5 | BEA's 2023 Use table: for-hire truck purchases are 0.8-3.3% of output in the segments' industries | sheet "2023", $ millions: Food 311FT, row 484 Truck transportation 38,685, Total Industry Output 1,179,810 (3.28%); Machinery 333: 4,500 of 451,962 (1.00%); Paper 322: 3,623 of 203,354 (1.78%) | https://apps.bea.gov/industry/iTables%20Static%20Files/AllTablesIO.zip (IOUse_Before_Redefinitions_PRO_1997-2023_Summary.xlsx) | 2026-10-09 | *verified* data; ratios **[our calc]** |
| N-AT40 | AT2, AT5 | BEA's 2017 detailed Use table gives truck and rail purchases for industries close to each segment | e.g., 311119 other animal food truck 2.88%, rail 2.42%; 322210 paperboard containers 2.01%; 333415 HVAC equipment 1.08%; 325310 fertilizer 1.20% | same zip (IOUse_Before_Redefinitions_PRO_2017_Detail.xlsx, sheet "2017", row T008) | 2026-10-09 | *verified* data; ratios **[our calc]** |
| N-AT41 | AT2, AT3 | CSCMP 2026: US logistics $2.40T (7.8% of GDP) in 2025; parcel $241.3B, rail $97.3B | "$2.40 trillion"; parcel "$241.3 billion" (2025), "$229.5 billion" (2024); rail "$97.3 billion"; trucking 59.5% of transport costs | https://www.scdigest.com/firstthoughts/26-06-26.php?cid=23144 | 2026-10-09 | *assumed* (secondary summary) |
| N-AT42 | AT5 | SUSB 2022 firm counts by enterprise receipts size per NAICS code | e.g., "31-33 Manufacturing 18: 100,000+ 7464"; "42 … 18: 100,000+ 10576" (firms, $1,000 classes) | https://www2.census.gov/programs-surveys/susb/tables/2022/us_6digitnaics_rcptsize_2022.xlsx | 2026-10-09 | *verified*; segment sums **[our calc]** |
| N-AT43 | AT5 | SUSB 2022 splits $100M+ firms into five larger classes for manufacturing and wholesale | Manufacturing: 3,527 / 1,464 / 980 / 715 / 778; Wholesale: 5,424 / 2,159 / 1,215 / 847 / 931 ($100-250M … $2.5B+) | https://www2.census.gov/programs-surveys/susb/tables/2022/us_naicssector_large_rcptsize_2022.xlsx | 2026-10-09 | *verified* |

---

## Coincidence watch

| Figure | Sources that give it | Do they share an origin? | Note |
|---|---|---|---|
| **About 3-4% of revenue for total freight** | Establish Davis 3.68% (N-X21); three domestic mid-sized bankrupt firms 2.9-4.1% (N-AN22-N-AN24); Instant Brands 3.84% (N-AT37); AT1 medians plus BEA inbound | No: a voluntary benchmark sample, sworn payment lists and filings | **Look-alikes measuring different things.** Establish Davis counts inbound and outbound including own fleets; the payment lists count for-hire payees only; Instant Brands' 3.84% is mostly parcel and ocean. Agreement on the total says nothing about the TL+LTL share |
| **All 30 firms' main figures come from one era and one tag** | SEC XBRL frames and filings for fiscal 2016-2018 (N-AT02); 10 firms rest on the API value alone, without a quote | Yes: one tag, one era, and the filers chose to disclose | Firms that report freight are self-selected and the years are 2016-18. Four 2025 re-reads (EACO, WD-40, Tootsie, J&J) show similar or lower ratios, which eases but does not remove the concern |
| **SG6's high ratios** | Intrepid 18.4%, Compass 19.6%, Oil-Dri 15.0% | Same product type (bulk minerals) | The SG6 median is driven by minerals, not by feed mills or farm-supply firms. AT5 uses 7.8% (ag chemicals) as SG6's central **[our call]** |
| **SG1's in-range firms** | EACO and Hillman | Both are fastener distributors | SG1's HVAC, plumbing and electrical distributors are represented only by larger firms (Watsco 1.1%, Pool 1.6%) |
| **SG5 rests on three firms** | Huttig, PGT, ADS | No | Too few for a range; ADS's figure includes an own fleet |
| **BEA 2017 and 2023 agree closely** | N-AT39, N-AT40 | Yes: annual tables are extrapolated from the 2017 benchmark | Not two independent measurements |
| **National mode shares** | CSCMP 2024 via FreightWaves (N-K22) and CSCMP 2026 via Supply Chain Digest (N-AT41) | Yes: the same report series, both read second-hand | The 58% / 34% TL+LTL shares inherit any error in CSCMP's estimates |
| **The model's central matches two real firms** | Latex Foam and United Gilsonite (AT5.1 cross-check) | Partly circular: those two firms were already on file and inform the "close" reading | The cross-check is a sanity check, not a test; it fails for three other real firms |
