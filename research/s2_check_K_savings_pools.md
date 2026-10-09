# S2 check K: rough yearly savings pools for 23 cards (evidence for knock-out K5)

- **What this is:** evidence for knock-out K5 ("big enough": a yearly fee pool of about $25M or more) at stage S2 of run 01. It covers 23 of the 40 cards in `research/selection_runs/run-01/1_candidates.md` §4.
- **Date:** 2026-09-15.
- **Status:** input to S2; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/2_knockouts.md`.
- **Labels:**
  - *verified*: read at the source (a quote from the page, or a value from a downloaded file or official table).
  - *assumed*: a search snippet, secondary summary, vendor claim, memory, or blocked page. Vendor claims are always *assumed*.
  - **[our calc]** marks our own arithmetic; **[our call]** marks our own judgement.

**How to read the numbers.**
- The **savings pool** is the avoidable cost a card's customers incur each year that software could remove, counted the way a fee would be counted (`submarket_selection.md` §2.1, §4 S3 step 2):
  - It is worked out as cost per unit × yearly volume × the share software could remove.
  - It is not freight spend or goods value.
  - It caps what customers could pay. It is not a market size (T12).
- **The K5 lines.** A $25M fee pool needs a savings pool of **$250M at a 10% fee share, $125M at 20%, and $71M at 35%** **[our calc]**. Hence the three bands the coordinator asked for: under ~$70M, $70-250M, and over ~$250M.
- **What fee shares look like elsewhere** (check A, A5): about 10% for software-only; 25-50% where the vendor does the recovery work.
- **The ranges are Fermi ranges.** The low end multiplies all the low inputs; the high end multiplies all the high ones. So each range is wide by design.
  - The "mid" is the geometric mean of low and high **[our calc]**. It is given only to help the reader; it is not a best estimate.
- **Unit costs we used across cards [our call]:**
  - **Truck hour, $75-100.** R38 gives non-fuel cost of $1.779 per mile; at about 45 mph that is roughly $80 an hour.
  - **Wages:** BLS national mean wages from May 2025 (N-K09):
    - cargo and freight agents, $57,230;
    - shipping, receiving and inventory clerks, $46,810;
    - heavy truck drivers, $59,710.
- **Overlaps.** Several pairs count parts of the same cost and should not be added together:
  - C-21 and C-22 (container per-diem);
  - C-26 and C-27 (produce);
  - C-35 and C-38 (fuel is kept in C-38);
  - C-10 and C-13 (damage).

**Freight words used here** (other terms are in `1_candidates.md`):
- **TEU:** a twenty-foot equivalent unit, a standard container size. A typical box is about 1.8 TEU **[our call]**.
- **cwt:** hundredweight, 100 lb.
- **Carlot:** USDA's standard produce truckload of 40,000 lb (N-G14).
- **L/C:** letter of credit, a bank payment guarantee that pays only against documents that match exactly.
- **Turn time:** the minutes from joining the queue outside a port terminal to leaving through the exit gate.
- **Claims ratio:** claims paid ÷ carrier revenue.

---

## 1. Summary table

| Card | Cost pool (yearly, range) | Removable share | Savings pool, low-high | Buyers per side | What they spend on the job today | Label strength | Source IDs |
|---|---|---|---|---|---|---|---|
| C-10 cargo claims | $1.1-1.9B of eligible loss and damage that goes unrecovered (all shippers). Small and mid-sized shippers: 30-50% of it | 20-40% [our call] | **$70-370M** (mid ~$160M) | Shippers: 239,265 manufacturers and 277,932 wholesalers (all sizes). Carriers: 7,204 LTL firms; 531,374 for-hire carriers | Contingency claims services (fee % not found); parcel analogue 25-50% | mostly assumed | N-K21, N-K22, N-K03, N-F56, N-A25 |
| C-13 big-and-bulky | $0.5-1.5B (5-15% of $10.15B in 3PL delivery spend) | 20-40% [our call] | **$100-610M** (mid ~$250M) | Sellers: 14,044 furniture makers, 12,708 furniture stores, 3,931 appliance stores. Carriers: 4,827 local-delivery firms | $10.15B a year in 3PL delivery fees; $100-300 per white-glove stop | mixed | N-K04, N-K05, N-K30, N-K31, N-G75 |
| C-16 job-site delivery | $0.08-0.62B (5-15% of a $1.65-4.1B dealer fleet cost) | 30-50% [our call] | **$25-310M** (mid ~$90M) | Dealers: 20,291 building-material dealers, 1,536 home centres, 4,552 lumber wholesalers. Contractors: not counted | $1.65B in dealer driver wages; software not found | mixed | N-K09, N-K05, N-E02 |
| C-17 inbound control | $2.0-10.6B of overpay on mid-sized firms' uncontrolled inbound freight | 25-50% [our call] | **$0.5-5.3B** (mid ~$1.6B) | Buyers: mid-sized share of 239,265 manufacturers and 277,932 wholesalers. Suppliers: same pool | Managed-transportation fees and gainshares (50/50, assumed) | mostly assumed | N-K22, N-K28, N-E31, R33, N-A30 |
| C-18 warehouse bills | $0.23-1.1B (1-5% leakage on $22.5B receipts of warehouses under 500 staff) | 50-80% [our call] | **$110-900M** (mid ~$320M). Firms under 20 staff only: $28-225M | Warehouses: 6,789 general and 680 refrigerated firms. Customers: 53,556 e-commerce firms, plus distributors | Warehouse-system billing modules (not researched) | mixed | N-K05, N-K27, N-F64 |
| C-21 container D&D | $0.93B a year (small and mid-sized importers' 30.2% share of $3.08B a year) | 10-30% [our call] | **$90-280M** (mid ~$160M) | Importers: 240,535 (97.3% small or mid-sized). About 8,600 NVOCCs; about 14,454 customs brokers | The D&D charges themselves; tool prices not found | mostly verified | N-F31, N-K01, N-G01, N-E18 |
| C-22 drayage dispatch | $1.3-1.8B of excess truck time at terminals | 5-15% [our call] | **$65-270M** (mid ~$130M) | Carriers: 48,991 with the intermodal flag (23,000+ trucks at LA/LB). Importers: 240,535 | PierPass $38.78 per TEU (a terminal fee); software not researched | mostly assumed | N-K32, N-K19, R38, N-F02, N-F21 |
| C-23 intl quoting | $0.42-1.41B of forwarder staff time spent quoting | 30-50% [our call] | **$130-710M** (mid ~$300M) | Forwarders: about 8,600 NVOCCs; 15,591 arrangement firms under 500 staff. Importers: 240,535 | Forwarding software (BoxTop sold for ~$13M); no prices found | mixed | N-K05, N-K09, N-K35, N-F05, N-B25 |
| C-24 export docs | $76-228M of document cost on ~1.9M ag export containers | 30-50% [our call] | **$23-115M** (mid ~$50M) | Exporters: 271,250 (97.1% small or mid-sized; the farm-and-food subset is not counted). About 9,100 ocean intermediaries | Forwarder document fees (not found) | mostly assumed | N-K33, N-K34, N-E18, N-F05 |
| C-25 Laredo | $0.5-0.8B (Laredo's share of $1.5B in border delay, plus paperwork) | 10-25% of delay; 10-20% of paperwork [our call] | **$50-180M** (mid ~$95M) | Crossings: 3,026,632 northbound trucks a year. Shippers, brokers and transfer carriers: not counted | Customs-broker fees on both sides (not found) | mixed | N-K06, N-K18 |
| C-26 produce rejections | $51-685M (1.71M loads × 1-4% rejected × $3-10k loss) | 20-40% [our call] | **$10-275M** (mid ~$55M) | Shippers: 41,793 vegetable farms, 97,343 fruit farms, 4,480 wholesalers, 13,200+ PACA licensees. Carriers: 105,756 with the reefer flag | USDA 8e inspection at $0.00635 per lb (≈$254 a load); broker margins | mixed | N-K12, N-G14, N-K25, N-K26 |
| C-27 border produce | $36-205M (362-513k loads × $100-400) | 20-40% [our call] | **$7-80M** (mid ~$25M) | Importers: 85+ Nogales distributors (2013); Pharr count not found. Crossings: Nogales 404,588 trucks; Hidalgo/Pharr 721,489 | 8e inspection fee; cold storage (not found) | mixed | N-K12, N-K06, N-K23, N-K24, N-G17 |
| C-28 harvest grain | $0.23-1.05B (16-21M loads × $14-50 of queueing and ticket work) | 15-30% [our call] | **$35-315M** (mid ~$105M) | Elevators: 7,922 storage sites; 1,839 grain wholesalers. Farms: 330,930. Carriers: 145,062 with the grain flag | Elevator software (Agvance, GSS, Bushel); no prices | mixed | N-K10, N-K36, N-E11, N-E13, N-G49 |
| C-29 rail and barge buying | $36-109M of avoidable timing premium (already net of what software can't remove) | embedded [our call] | **$36-110M** (mid ~$65M) | Merchandisers: 1,839 grain wholesalers (4,481 sites). Carriers: 6 Class I railroads; 339 barge firms | Not found | mixed | N-K13, N-K14, N-G25, N-G27 |
| C-30 rail demurrage | $0.8-1.6B of Class I demurrage billed | 5-15% [our call] | **$40-240M** (mid ~$95M) | Shippers: about 10,000 short-line customers (Class I count not found). Railroads: 6 Class I, ~603 short lines | One service firm (RSI); no software found | mixed | N-F34, N-G34, N-F12 |
| C-31 livestock | $38-140M (2.5-3.5M loads × $15-40 of admin) | 30-50% [our call] | **$11-70M** (mid ~$28M) | Shippers: 534,633 ranches, 11,186 feedlots, 21,865 hog farms, 1,221 auctions. Carriers: 25,365 livestock haulers | Livestock load boards and TMSs (no prices) | mixed | N-K11, N-E11, N-E16, N-F02 |
| C-32 milk hauling | $0.97-1.86B in hauling charges (2.32B cwt × $0.42-0.80) | 3-8% [our call] | **$29-150M** (mid ~$65M) | Farms: 23,153 dairies. Co-ops and haulers: counts not found | Hauling at $0.42 per cwt (weighted, Upper Midwest); no software prices | mostly verified | N-K08, N-K15, N-K43, N-E11 |
| C-33 cut flowers | $17-52M (1-3% of $1.74B in imports via Miami) | 20-40% [our call] | **$3.5-21M** (mid ~$9M) | Miami importers: count not found | Not found | mixed | N-K20, N-G68, N-K42 |
| C-34 OS/OW permits | $155-520M (3.1-5.2M permits × $50-100) | 25-50% [our call] | **$39-260M** (mid ~$100M) | Carriers: 87,293 with the machinery flag (an upper bound). Permit services: count not found | Permit services charge $50.50-150 per permit (vendor) | mixed | N-K07, N-G55, N-F42, N-F02 |
| C-35 tank loads | $43-567M (8.5-15M chemical tank loads × $5-38) | 20-40% [our call] | **$9-230M** (mid ~$45M) | Shippers: 10,455 chemical makers. Carriers: 25,521 with the chemicals flag; NTTC has 200+ members | Tank washes at $200-1,000+; Labelmaster DGIS (no price) | mostly assumed | N-E07, N-K40, N-K41, N-G49 |
| C-37 log tickets | $38-120M (12.7-15M loads × $3-8) | 40-60% [our call] | **$15-72M** (mid ~$33M) | Loggers: 7,369 firms. Wood-products firms: 11,761. Carriers: 161,723 with the logs flag (includes lumber) | Logger's Edge (275+ firms, vendor); Waldo; no prices | mixed | N-K37, N-K05, N-E17, N-G49, N-G66 |
| C-38 fuel reconciliation | $92-328M (18-22M loads × $5-15) | 30-50% [our call] | **$28-165M** (mid ~$67M) | Marketers: 4,083 fuel dealers, 1,763 petroleum wholesalers, 1,993 bulk-terminal firms (PMAA says 8,000). Carriers: 41,445 with the liquids flag | PDI (250+ marketers, vendor); no prices | mixed | N-K16, N-K05, N-K38, N-K39, N-G67 |
| C-40 household moves | $306-766M (claims 1-2% plus estimating 1-3% of $15.3B revenue at firms under 500 staff) | 10-30% of claims; 20-40% of estimating [our call] | **$46-276M** (mid ~$113M) | Movers: 9,083 firms; 8,207 household-goods authorities. Households: ~0.8M interstate moves (assumed, dated) | Not found | mixed | N-K05, N-K29, N-F03 |

**What "label strength" means here:**
- **Mostly verified:** the volume and the unit cost were both read at the source; only the removable share is our call.
- **Mixed:** the volume was read at the source, but the unit cost or share is assumed or our call.
- **Mostly assumed:** the volume or the cost base itself comes from snippets, secondary summaries or vendors.

---

## 2. Card by card

### C-10 · Cargo loss and damage claims
- **Cost pool.** The loss and damage that shippers are owed but never recover: claims that are unfiled, abandoned or wrongly denied.
  - **LTL claims paid.** 2024 LTL spend was $64B (CSCMP via FreightWaves, N-K22, *assumed*: a secondary summary). The industry claims ratio is 0.35% (Synchrogistics index, N-K03, *assumed*). So paid claims ≈ $224M **[our calc]**.
  - **Filing and denial rates** (vendor survey, N-K21, *assumed*):
    - about 50% of eligible claims are filed;
    - 50-60% of LTL claims and 20-35% of truckload claims are denied.
  - **LTL eligible loss** ≈ $224M ÷ (0.5 filed × 0.45 paid) ≈ $1.0B, of which about $0.78B goes unrecovered **[our calc]**.
  - **Truckload.** 2024 TL spend was $387B (N-K22, *assumed*). No claims ratio was found, so we use 0.05-0.15% paid **[our call]**. That gives $194-581M paid and $0.36-1.08B unrecovered **[our calc]**.
  - **Total unrecovered:** $1.14-1.85B **[our calc]**.
  - The vendor figure of "$50 billion or more" in yearly claims (N-K21) is *assumed* and not used.
- **Small and mid-sized shippers' share:** 30-50% **[our call]**. No data on freight spend by shipper size was found.
- **Removable share:** 20-40% **[our call]**, from raising the filing rate and the recovery rate. A vendor says recovery runs 35-45% on manual processes and 70-85% on automated ones (N-K21, *assumed*).
- **Buyers:**
  - shippers: 239,265 manufacturing and 277,932 wholesale firms (scan E, *verified*; this is all sizes, an upper bound);
  - carriers: 7,204 LTL firms (N-F01) and 531,374 interstate for-hire carriers (N-F02).
- **Spend today:** claims services work on contingency ("if we don't win, you don't pay", N-F56). Their fee % was not found; parcel-audit contingencies run 25-50% (N-A25).
- **Savings pool [our calc]:** low $1,135M × 0.30 × 0.20 = **$68M**; high $1,854M × 0.50 × 0.40 = **$371M**; mid about $160M. **Straddles $70M and $250M.**

### C-13 · Big-and-bulky home delivery
- **Cost pool.** Failed, damaged and re-delivered stops.
  - The 3PL big-and-bulky last-mile market was "approximately $10.15 billion" in 2024 (Armstrong & Associates, N-K04, *verified*).
  - One vendor quotes a damage rate of "12-15%" for average furniture carriers (N-G75, *assumed*).
  - First-attempt delivery failures run 5-20% (parcel-wide vendor figures, N-K31, *assumed*).
  - We use 5-15% of delivery spend as the cost of failure and damage handling **[our call]**. That gives **$0.51-1.52B** **[our calc]**.
  - At $100-300 per white-glove stop (N-K30, *assumed*), the market implies about 34-100M stops a year **[our calc]**.
  - Retailers' own delivery fleets and the value of damaged goods are left out, so this may be low.
- **Removable share:** 20-40% **[our call]**, from scheduling, customer confirmation and photo proof. Software cannot remove physical handling damage.
- **Buyers** (N-K05, SUSB 2022, *verified*):
  - furniture makers: 14,044 (N-E17);
  - furniture stores: 12,708;
  - appliance stores: 3,931;
  - furniture wholesalers: 4,535;
  - local delivery firms: 4,827 (N-F01).
- **Savings pool [our calc]:** $10.15B × 5% × 20% = **$102M**; × 15% × 40% = **$609M**; mid about $250M. **Straddles $250M.**

### C-16 · Job-site deliveries for building-material dealers
- **Cost base.** BLS May 2025 figures for building-material and supplies dealers (NAICS 4441; N-K09, *verified*):
  - 20,040 heavy truck drivers at a mean of $51,870;
  - 13,470 light truck drivers at a mean of $45,450.
  - Driver wages total **$1.65B** **[our calc]**.
  - As a high case, we take full fleet cost at 2.5× wages, **$4.1B** **[our call]**. Driver pay is roughly 40% of truck operating cost, from ATRI's cost study, which we did not re-read.
  - Lumber wholesalers' own fleets are left out (no BLS series exists for NAICS 4233), even though own trucks carry 64.6% of their shipment value (N-E02). So this may be low.
- **Avoidable share:** 5-15% of fleet cost goes to failed deliveries, sites that aren't ready, waiting and re-trips **[our call]**. Nothing was published. Cost pool: $0.08-0.62B **[our calc]**.
- **Removable share:** 30-50% **[our call]**.
- **Buyers** (N-K05, *verified*): 20,291 other building-material dealers; 1,536 home-centre firms; 4,552 lumber wholesalers.
- **Savings pool [our calc]:** $1.65B × 5% × 30% = **$25M**; $4.1B × 15% × 50% = **$310M**; mid about $88M. **Straddles $70M and $250M.**

### C-17 · Controlling inbound freight from suppliers
- **Cost pool.** Overpayment on inbound freight whose carrier the supplier chooses.
  - 2024 for-hire truckload plus LTL spend: $387B + $64B = $451B (N-K22, *assumed*).
  - Inbound is "40-60% of total freight spend" (vendor snippets, N-K28, *assumed*). We use 40% **[our call]**.
  - Only "about 35%" of companies use an inbound routing guide (N-E31, *assumed*). We take 50-65% of inbound as uncontrolled **[our call]**.
  - Mid-sized firms' share of that spend: 15-30% **[our call]**.
  - Vendors say firms overpay 15-30% when suppliers control inbound freight (N-K28, *assumed*).
  - Cost pool: $451B × 0.40 × 0.50 × 0.15 × 15% = **$2.0B**, up to × 0.65 × 0.30 × 30% = **$10.6B** **[our calc]**.
- **Removable share:** 25-50% of the overpay **[our call]**.
- **Spend today:** managed-transportation 3PLs charge per shipment or a % of spend, plus gainshares (R33). A 50/50 gainshare is typical (N-A30, *assumed*).
- **Savings pool [our calc]:** **$0.51-5.3B**; mid about $1.6B. **Over $250M even at the low end**, but every input except the CSCMP figure is assumed or our call.

### C-18 · Warehouse storage and handling bills
- **Cost base.** Receipts of warehouse firms with fewer than 500 employees (SUSB 2022, N-K05, *verified*):
  - general warehousing: $19.43B (35.6% of $54.65B);
  - refrigerated warehousing: $3.08B (41.5% of $7.41B);
  - total: **$22.5B** **[our calc]**.
- **Leakage (unbilled work plus billing errors).** Vendors say 3PLs lose "between 3 and 15%" of revenue, or "around 3%" of billing revenue. Datex uses a 2% illustration (N-K27; all vendor, *assumed*). We use 1-5% **[our call]**, giving a cost pool of $0.23-1.1B.
- **Removable share:** 50-80% **[our call]**. Vendors say automated event capture takes leakage below 0.1% (*assumed*).
- **Buyers:** 6,789 general and 680 refrigerated warehouse firms (N-F01); 53,556 e-commerce firms (N-E17).
- **Savings pool [our calc]:** $22.5B × 1% × 50% = **$113M**; × 5% × 80% = **$900M**; mid about $320M. **Straddles $250M.** If only warehouses with fewer than 20 staff are counted, as the card's sentence suggests ($5.6B of receipts), the pool is $28-225M.

### C-21 · Container demurrage and detention
- **Cost pool.**
  - Nine ocean carriers collected "roughly $15.4 billion" in D&D from April 2020 to March 2025 (N-F31, *verified*). That is **$3.08B a year** **[our calc]**.
  - The collected and billed amounts peaked in Q4 2024, 85% above Q2 2020 (N-K01, *verified*).
  - In 2020-22, 22% of what was billed went uncollected (N-G01, *verified*; **[our calc]**).
  - Small and mid-sized importers hold 30.2% of known import value (N-E18, *verified*). We use that as their share: **$0.93B** **[our calc]**.
  - Terminal demurrage and carriers outside the nine are not counted, so this may be low.
- **Removable share:** 10-30% **[our call]**, from free-time alerts and disputes under the 2024 FMC billing rule. The 22% uncollected shows how much is disputable.
- **Buyers:** 240,535 importers (N-E18); about 8,600 NVOCCs (N-F05); about 14,454 licensed customs brokers (N-G10, *assumed*).
- **Savings pool [our calc]:** **$93-279M**; mid about $160M. **Straddles $250M.**

### C-22 · Port drayage dispatch
- **Volume.**
  - US container imports were 28.2M TEU in 2024 (N-K32, *assumed*: snippets).
  - Loaded exports were not found; we use 12M TEU **[our call]**.
  - About 22M boxes each make about 2 terminal moves; we remove 20% for on-dock rail. That gives about **35.7M truck transactions** **[our calc]**.
- **Excess time.** The Harbor Trucking Association measured an average LA/LB turn time of 69 minutes against 35 minutes at the best terminal (November 2019, via Transport Topics, N-K19, *assumed*: secondary and dated). We use 0.5 hour of excess per transaction **[our call]**.
- **Cost pool:** 35.7M × 0.5 h × $75-100 = **$1.3-1.8B** **[our calc]**.
- **Removable share:** 5-15% **[our call]**. Most of the wait is on the terminal's side, beyond the dispatcher's reach.
- **Buyers:** 48,991 carriers tick "intermodal containers" (N-F02); 23,000+ trucks on the LA/LB registry (N-F21).
- **Savings pool [our calc]:** **$67-268M**; mid about $134M. **Straddles $70M and $250M.**

### C-23 · Quoting and booking international freight
- **Cost pool (staff time spent quoting).**
  - Freight-arrangement firms (NAICS 488510) with fewer than 500 staff employ 164,684 people (N-K05, *verified*).
  - Share of them in ocean and air forwarding: 30-50% **[our call]**. The code also covers truck brokers and customs brokers.
  - Mean wage for cargo and freight agents: $57,230 (N-K09, *verified*).
  - Share of their time spent quoting and booking: 15-30% **[our call]**. A vendor survey says manual quotes take "57 hours" from request to quote (Freightos 2018, N-K35, *assumed*); that is elapsed time, not hours of work.
  - Cost pool: **$0.42-1.41B** **[our calc]**.
- **Removable share:** 30-50% **[our call]**. Importers' own time and lost sales are left out.
- **Buyers:** about 8,600 NVOCCs out of 9,100+ ocean intermediaries (N-F05); 15,591 arrangement firms with fewer than 500 staff (N-K05).
- **Savings pool [our calc]:** 164,684 × 0.30 × 0.15 × $57,230 × 0.30 = **$127M**; 164,684 × 0.50 × 0.30 × $57,230 × 0.50 = **$707M**; mid about $300M. **Straddles $250M.**

### C-24 · Export documents for farm and food exporters
- **Volume.** Waterborne containerized ag exports averaged 285,000 TEU a month in 2021-24 (USDA GTR, via snippet, N-K33, *assumed*). That is 3.4M TEU, or about **1.9M containers a year** **[our calc]**.
- **Cost per container:** $40-120 **[our call]** for preparation time, certificate and courier fees, bank fees for document discrepancies, and holds.
  - 65-75% of L/C document sets are refused on first presentation (N-K34, *assumed*). That applies only to the unknown share of exports paid by L/C.
  - Cost pool: **$76-228M** **[our calc]**.
  - Bulk grain is left out, because its official certificates are already system-issued (N-G31).
- **Removable share:** 30-50% **[our call]**.
- **Buyers:** 271,250 exporters (N-E18); the farm-and-food subset was not counted.
- **Savings pool [our calc]:** **$23-114M**; mid about $51M. **Straddles $70M.**

### C-25 · Cross-border Mexico truckloads through Laredo
- **Volume.** In 2024, Laredo had 3,026,632 incoming trucks. All ports on the Mexico border had 7,617,207, and on the Canada border 5,550,550 (BTS API, N-K06, *verified*).
- **Delay cost.**
  - Texas A&M's CIITR says border delays cost "more than $1.5 billion in direct economic costs annually" across 49 land ports (N-K18, *verified*).
  - Laredo has 23.0% of incoming trucks **[our calc]**. Assuming cost scales with trucks, that is **$345M a year** **[our calc]**.
- **Paperwork cost.** Two customs brokers handle each load; no fee was found. We use $50-150 per crossing **[our call]**, giving $150-450M.
- **Removable share:**
  - 10-25% of delay, from document readiness and pre-filing; inspection queues remain **[our call]**;
  - 10-20% of paperwork **[our call]**.
- **Savings pool [our calc]:** low $34.5M + $15.1M = **$50M**; high $86M + $91M = **$177M**; mid about $94M. **Straddles $70M.**

### C-26 · Produce reefer booking and rejected loads
- **Volume.** USDA reported truck shipments of fresh produce in 2025 of 8.62 + 9.33 + 8.59 + 7.71 = **34.25M tons** (AgRTQ Q1-Q4 2025, N-K12, *verified*; **[our calc]**). At USDA's 40,000-lb carlot (N-G14), that is **1.71M loads** **[our calc]**.
- **Rejection rate.** One vendor cites "approximately 12%" rejected or delayed (N-K25, *assumed*: snippet, page empty). No neutral rate exists (scan G gap). We use 1-4% actually rejected **[our call]**.
- **Loss per rejected load:** $3-10k **[our call]**, covering salvage discount, re-consignment, inspection and storage. Load values were not sourced.
- **Cost pool:** **$51-685M** **[our calc]**.
- **Removable share:** 20-40% **[our call]**, from temperature records, timely inspection and dispute packets. A vendor claims 40-60% (N-K26, *assumed*).
- **Buyers:** 41,793 vegetable farms, 97,343 fruit farms, 4,480 produce wholesalers and 13,200+ PACA licensees (N-E11, N-E14, N-E17); 105,756 carriers tick reefer cargo (N-F02).
- **Savings pool [our calc]:** 1.71M × 1% × $3k × 20% = **$10M**; 1.71M × 4% × $10k × 40% = **$274M**; mid about $53M. **Straddles $70M and $250M.**

### C-27 · Cross-border produce at Nogales and Pharr
- **Volume.** Mexican produce by truck in 2025 was 3.51 + 3.55 + 2.33 + 2.68 = **12.07M tons**, or 604k loads (N-K12, *verified*; **[our calc]**).
  - Pharr claims "over 65%" of US fresh produce imports from Mexico (N-K23, *assumed*: the bridge owner's own claim), or 109,000 produce truckloads (N-K24, *assumed*: snippet).
  - Nogales had about 120,000 produce trucks in a 2013 study (N-G17, *assumed*).
  - All-truck crossings in 2024: Nogales 404,588 and Hidalgo/Pharr 721,489 (N-K06, *verified*).
  - We use 60-85% of the 604k loads for the two gateways, or **362-513k loads** **[our call]**.
- **Avoidable cost per load:** $100-400 **[our call]**, for extra cold-storage days, inspection holds, reefer waiting and quality loss. The cost pool is $36-205M.
- **Removable share:** 20-40% **[our call]**.
- **Savings pool [our calc]:** **$7-82M**; mid about $24M. **Mostly under $70M; the top end crosses it.**

### C-28 · Harvest grain hauling and scale tickets
- **Volume.** 2025 production was corn 17.0B bushels, soybeans 4.26B and wheat 1.98B, a total of 23.24B (NASS, N-K10, *verified*).
  - At about 1,000 bushels per semi, that is about 23M loads. We assume 70-90% move farm to elevator by truck **[our call]**, so **16-21M loads**.
- **Cost per load.**
  - Waiting: a vendor cites elevator waits of "2-4 hours" at busy times (N-K36, *assumed*). We use 0.2-0.5 hour of avoidable wait on an average load × $60-90 per hour **[our call]**.
  - Ticket-to-contract matching: $2-5 of clerk time **[our call]**.
  - Total: $14-50 per load. Cost pool: **$0.23-1.05B** **[our calc]**.
- **Removable share:** 15-30% **[our call]**, from queue scheduling and electronic ticket matching.
- **Buyers:** 7,922 off-farm storage sites (N-E13); 1,839 grain wholesalers with 4,481 sites (N-E17); 330,930 grain farms (N-E11); 145,062 carriers tick grain (N-G49).
- **Savings pool [our calc]:** **$34-314M**; mid about $103M. **Straddles $70M and $250M.**

### C-29 · Buying rail and barge freight for grain
- **Volume.**
  - Grain carloads "totaled 1.07 million" in 2024 (AAR, N-K13, *verified*).
  - Grain barged through the Mississippi system's locks totalled 29,626 thousand tons in 2024 (USDA GTR Table 10, N-K14, *verified*).
- **Premium software could avoid through better timing.**
  - Secondary-market bids for railcars swung from +$563 to −$100 per car (N-G27, N-G28, *assumed*).
  - Barge freight ran at 435% of tariff on average in 2025 and 792% on 2026-09-08 (N-G25, *verified*).
  - We use $20-60 per car and $0.50-1.50 per ton **[our call]**, already net of what software can't remove.
- **Savings pool [our calc]:** rail $21-64M + barge $15-44M = **$36-109M**; mid about $63M. **Straddles $70M.**
- **Buyers:** 1,839 grain wholesalers (N-E17); 339 barge firms (N-F01); 6 Class I railroads.

### C-30 · Rail demurrage and accessorial invoices
- **Cost pool.**
  - Class I railroads collected $1.18B in demurrage in the first nine months of 2021 (N-F34, *verified*, trade press). That pace is **$1.57B a year** at the peak **[our calc]**.
  - Union Pacific averaged $212M a year, about 1% of its revenue, in 2019 (N-G34, *assumed*). If all Class Is charged about 1% of revenue, the pre-peak level was about **$0.8B** **[our call]**.
  - Accessorials are left out. No figures for 2023-25 were found; they sit only in per-railroad STB PDFs.
- **Removable share:** 5-15% **[our call]**, from checking invoices against the STB's 2021 invoice rule and managing car orders.
- **Buyers:** short lines serve about 10,000 customers (N-F12); the Class I shipper count was not found.
- **Savings pool [our calc]:** $0.8B × 5% = **$40M**; $1.57B × 15% = **$236M**; mid about $97M. **Straddles $70M.**

### C-31 · Livestock hauling
- **Volume.** Commercial slaughter in 2025 was 29.8M cattle and 128M hogs (NASS, N-K11, *verified*).
  - Each animal moves 2-3 times **[our call]**. Loads hold about 50 cattle or about 200 hogs on average **[our call]**.
  - That gives about 3.1M loads; we use **2.5-3.5M** **[our calc]**.
- **Admin and compliance cost per load:** $15-40 **[our call]**, for dispatch calls, health and brand papers, and driving-hours exemption tracking. The cost pool is $38-140M.
  - Weight loss in transit ("shrink") is a physical cost and is left out.
- **Removable share:** 30-50% **[our call]**.
- **Savings pool [our calc]:** 2.5M × $15 × 30% = **$11M**; 3.5M × $40 × 50% = **$70M**; mid about $28M. **Under $70M; the top end touches it.**

### C-32 · Milk pickup and hauling settlement
- **Volume.** US milk production in 2025 was "232 billion pounds", or 2.32B cwt (NASS, N-K08, *verified*).
- **Hauling rate.**
  - The Upper Midwest order's weighted average charge was "$0.4202" per cwt in May 2023; the pre-2011 method gives "$0.6137" (Market Administrator staff paper, N-K15, *verified*).
  - The per-farm average was $0.7969 in May 2024 (N-K43, *assumed*).
  - We use $0.42-0.80 **[our call]**. The national hauling bill is **$0.97-1.86B** **[our calc]**.
- **Removable share:** 3-8% **[our call]**. Better pickup routing cuts truck miles, so software changes how trucks are used; settlement admin is a smaller part.
- **Buyers:** 23,153 dairy farms (N-E11). Counts of co-ops and haulers were not found.
- **Savings pool [our calc]:** **$29-148M**; mid about $66M. **Straddles $70M.**

### C-33 · Cut-flower air imports into Miami
- **Cost base.** US cut-flower imports were "$1.98 billion" in 2024 (farmdoc daily, N-K20, *verified*). Miami handles 88% (N-G68, *verified*), so **$1.74B** passes through it **[our calc]**.
- **Avoidable cost.** "2 percent of shipments" are found non-compliant (N-K42, *assumed*: snippet). We use 1-3% of value lost to holds, fumigation, delay and paperwork **[our call]**. The cost pool is $17-52M.
- **Removable share:** 20-40% **[our call]**.
- **Savings pool [our calc]:** **$3.5-21M**. **Under $70M.**

### C-34 · Oversize and overweight permits
- **Volume.**
  - Texas issued "776,696 oversize/overweight permits" in FY2025, 82% of them single-trip routed (TxDMV, N-K07, *verified*).
  - Washington issued 183,502 in 2023 (N-G55, *verified*).
  - No national total is published (N-K45).
  - If Texas is 15-25% of US permits **[our call]**, the US total is **3.1-5.2M** **[our calc]**.
- **Cost per permit:** $50-100 **[our call]**, anchored on permit-service fees of $50.50-150 on top of state fees (N-F42, vendor, *assumed*). The cost pool is **$155-520M**.
- **Removable share:** 25-50% **[our call]**. State portals already self-issue much of this: 85% in Washington.
- **Buyers:** 87,293 carriers tick "machinery, large objects" (N-F02), an upper bound.
- **Savings pool [our calc]:** **$39-260M**; mid about $100M. **Straddles $70M, and the top end just reaches $250M.**

### C-35 · Tank loads: hazmat papers and tank-wash certificates
- **Volume.**
  - CFS 2022 hazmat was 2,590.1M tons, 41.2% of it by truck (for-hire plus own fleet), or 1,067M tons (N-E07, *verified*; **[our calc]**).
  - Leaving out fuels (counted in C-38), we take 20-35% as chemical and other tank loads **[our call]**. At 25 tons a load, that is **8.5-15M loads**.
  - PHMSA's figure of about 1.2M hazmat shipments a day, 94% by truck, is mostly small packages (N-K41, *assumed*).
- **Cost per load:**
  - paperwork, $3-8: 10-20 minutes at a clerk's $46,810 mean wage (N-K09) **[our call]**;
  - wash mismatches and rejected loads, $2-30: 0.2-1% of loads × $1,000-3,000 **[our call]**. A tank wash costs $200-1,000 or more (N-K40, *assumed*).
  - The cost pool is **$43-567M** **[our calc]**.
- **Removable share:** 20-40% **[our call]**.
- **Savings pool [our calc]:** **$9-227M**; mid about $44M. **Straddles $70M.**

### C-37 · Log trip tickets and haul pay
- **Volume.**
  - US roundwood harvest is about 440-460M m³ a year (439M m³ in 2018 and 462M m³ in 2023, including fuelwood; N-K37, *assumed*: snippets; FAOSTAT was down).
  - We take 75-85% as industrial logs trucked to mills, at about 1 green ton per m³ **[our call]**. That gives 330-390M tons, or **12.7-15M loads** at 26 tons.
- **Settlement and ticket cost per load:** $3-8 **[our call]**. The cost pool is $38-120M.
  - Cross-check: 0.5-1% of logging receipts of $13.8B (N-K05, *verified*) is $69-138M.
- **Removable share:** 40-60% **[our call]**.
- **Savings pool [our calc]:** **$15-72M**; mid about $33M. **Under $70M; the top end touches it.**

### C-38 · Fuel delivery reconciliation
- **Volume.**
  - 2024 product supplied was 8,967 thousand barrels a day of finished gasoline and 3,792 of distillate (EIA, N-K16, *verified*). That is 137.5B + 58.1B = **195.6B gallons** **[our calc]**.
  - We take 80-95% as delivered by truck, at 8,500 gallons a load **[our call]**. That gives **18-22M loads**.
- **Cost per load:** $5-15 for reconciliation, billing admin and errors **[our call]**. Vendors say "2-3% of fuel invoices contain errors" (N-K39, *assumed*). The cost pool is **$92-328M** **[our calc]**.
- **Removable share:** 30-50% **[our call]**.
- **Buyers:** 4,083 fuel dealers, 1,763 petroleum wholesalers and 1,993 bulk-station and terminal firms (N-K05, *verified*); PMAA claims "8,000 independent marketing companies" (N-K38, *assumed*).
- **Savings pool [our calc]:** **$28-164M**; mid about $67M. **Straddles $70M.**

### C-40 · Household moves
- **Cost base.** Mover receipts were $20.08B, with firms under 500 staff holding 76.3%, or **$15.3B** (N-K05, *verified*; **[our calc]**).
- **Cost pool.**
  - Claims: "top movers keep claims under 1% of revenue" (N-K29, vendor, *assumed*). We use 1-2% industry-wide **[our call]**, or $153-306M.
  - In-home surveys and re-estimates: 1-3% of revenue **[our call]**, or $153-460M.
- **Removable share:** 10-30% of claims (inventory and photo records) and 20-40% of estimating (virtual surveys) **[our call]**.
- **Buyers:** 9,083 movers (N-F01); 8,207 household-goods authorities (N-F03); about 0.8M interstate household-goods moves a year (AMSA, via snippet, N-K29, *assumed*, dated).
- **Savings pool [our calc]:** $15M + $31M = **$46M**; $92M + $184M = **$276M**; mid about $113M. **Straddles $70M and $250M.**

---

## 3. Sources (new in this check)

Existing IDs (R-, N-A to N-G) are cited in the text and listed in their own files. All new sources were accessed on 2026-09-15. Three IDs are skipped because those sources were read but not used:
- N-K02: the STB demurrage page, which carries no figures;
- N-K17: EIA's gasoline FAQ, superseded by N-K16;
- N-K44: an undated turn-time snippet.

| ID | Source (author/org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-K01 | Federal Maritime Commission, Detention and Demurrage data page (re-read; same page as N-F31) | data to 2025-03-31 | https://www.fmc.gov/detention-and-demurrage/ | full | $15.4B collected; peak in Q4 2024 85% above Q2 2020; Q1 2025 billings −24%. No yearly $ split |
| N-K03 | Synchrogistics, LTL Claims Ratio Index update 3Q25 | 2025-12-09 | https://synchrogistics.com/ltl-claims-ratio-index-update-3q25/ | full; consultancy (*assumed*) | Industry ratio 0.35%; 0.59% in 1Q20 |
| N-K04 | Armstrong & Associates, big-and-bulky last-mile 2025 release | 2025-06-02 | https://www.3plogistics.com/big-and-bulky-last-mile-delivery-in-the-united-states-2025/ | full | "approximately $10.15 billion" (2024) |
| N-K05 | Census, SUSB 2022 national file (same file as N-E17 and N-F01; new rows and columns) | 2022 data | https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_6digitnaics_2022.txt | download | Firms, employment and receipts by size for 488510, 4931xx, 484210, 423310, 444110/190, 4247xx, 454310, 113310, 4422/4431, 423210 |
| N-K06 | BTS, Border Crossing Entry Data (keg4-3bc2) | 2024 | https://data.bts.gov/resource/keg4-3bc2.json | API query | 2024 trucks: Laredo 3,026,632; Nogales 404,588; Hidalgo 721,489; border totals |
| N-K07 | Texas DMV, FY2025 Chairman's Annual Report | FY2025 | https://www.txdmv.gov/sites/default/files/report-files/FY-2025_Chairmans_Annual_Report.pdf | download | 776,696 OS/OW permits; 82% single-trip; 25-minute processing |
| N-K08 | USDA NASS, Milk Production (mkpr0226) | 2026-02-20 | https://esmis.nal.usda.gov/sites/default/release-files/795784/mkpr0226.txt | download | 2025 production of 232B lb |
| N-K09 | BLS OEWS May 2025, via the public API | 2025 | https://api.bls.gov/publicAPI/v1/timeseries/data/ | API query | NAICS 4441 heavy drivers 20,040 at $51,870, light 13,470 at $45,450; national means: 43-5011 $57,230, 43-5071 $46,810, 53-3032 $59,710 |
| N-K10 | USDA NASS, Crop Production 2025 Summary (cropan26) | 2026-01 | https://esmis.nal.usda.gov/sites/default/release-files/795725/cropan26.txt | download | Corn 17.0B, soybeans 4.26B, wheat 1.98B bushels |
| N-K11 | USDA NASS, Livestock Slaughter 2025 Summary | 2026-04 | https://www.nass.usda.gov/Publications/Todays_Reports/reports/lsan0426.pdf | download | Cattle 29.8M head; hogs 128M head |
| N-K12 | USDA AMS, AgRTQ Q1-Q4 2025 | 2025-26 | https://www.ams.usda.gov/sites/default/files/media/RTQ1stQuarter2025.pdf (and 2nd, 3rd, 4th) | download (national summaries) | Quarterly tons in total and from Mexico |
| N-K13 | AAR, Rail Industry Overview | 2025-01-10 | https://www.aar.org/wp-content/uploads/2025/01/AAR-RIO-January-10-FINAL.pdf | download | "Grain carloads totaled 1.07 million" (2024) |
| N-K14 | USDA AMS, Grain Transportation Report 01-23-25, Table 10 | 2025-01-23 | https://www.ams.usda.gov/sites/default/files/media/GTR01232025.pdf | download | Total grain barged in 2024: 29,626 thousand tons |
| N-K15 | Federal Milk Market Administrator (Upper Midwest), Staff Paper 25-01 on hauling charges | Aug 2025 | https://www.fmma30.com/StaffPapers/StaffPaper--25-01.pdf | download (Table 1 and notes) | Weighted $0.4202 per cwt (May 2023); $0.6137 by the old method |
| N-K16 | EIA, product supplied, annual | 2020-2025 | https://www.eia.gov/dnav/pet/pet_cons_psup_dc_nus_mbblpd_a.htm | download | 2024: gasoline 8,967 and distillate 3,792 thousand barrels a day |
| N-K18 | Texas A&M TTI (CIITR), O. Gurbuz, "Simplifying the Financial Impact of Border Crossing Delays" | 2026-04-02 | https://ciitr.tti.tamu.edu/2026/04/02/simplifying-the-financial-impact-of-border-crossing-delays/ | full | ">$1.5 billion" a year across 49 ports |
| N-K19 | Transport Topics (Harbor Trucking Association data), "Truck Turn Times Improve…" | 2019-12-04 | https://www.ttnews.com/articles/truck-turn-times-improve-ports-los-angeles-long-beach | full; secondary (*assumed*) | 69-minute average; best terminal 35 minutes |
| N-K20 | farmdoc daily, G. Niño and J. Janzen | 2025-02-10 | https://farmdocdaily.illinois.edu/2025/02/valentines-day-and-the-gains-from-agricultural-trade-cut-flowers-in-the-us.html | full | 2024 imports $1.98B; Colombia $1.24B |
| N-K21 | CorePiper, "2026 State of Freight Claims Report" | 2026-04-27 | https://corepiper.com/blog/state-of-freight-claims-2026/ | full; vendor (*assumed*) | ~50% filed; denial rates by mode; recovery 35-45% manual vs 70-85% automated; ~$1,200 average claim |
| N-K22 | FreightWaves (J. Kingston), on CSCMP's State of Logistics 2025 | 2025-06-11 | https://www.freightwaves.com/news/logistics-gdp-share-rose-in-24-not-likely-to-drop-cscmp-report | full; secondary (*assumed*) | 2024: truckload $387B, LTL $64B, private $541.4B |
| N-K23 | City of Pharr, produce-season release | 2024-10-15 | https://pharr-tx.gov/pharr-bridge-celebrates-30-years-of-connecting-two-nations-with-11th-annual-produce-season-kickoff/ | full; own claim (*assumed*) | "over 65%" of produce imports from Mexico |
| N-K24 | Search snippets (Rio Grande Guardian and others) on Pharr volumes | 2024 | https://riograndeguardian.com/fresh-produce-season-2024-2025-is-officially-underway/ | snippet | 109,000 produce truckloads |
| N-K25 | Trinity Logistics, produce rejections | undated | https://trinitylogistics.com/blog/preventing-shipment-rejections-during-produce-season | snippet (page empty) | "approximately 12%" rejected or delayed |
| N-K26 | Clarifresh, "The Cost of Fresh Produce Rejections" | 2025-04-22 | https://clarifresh.com/blog/the-cost-of-fresh-produce-rejections/ | full; vendor | Traceability cuts rejections 40-60% (claim) |
| N-K27 | Datex (full), plus Sequoia, Xorosoft and Packem snippets on 3PL billing leakage | 2026-05-26 | https://datexcorp.com/blog/why-3pl-billing-errors-cost-more-than-you-think/ | full and snippets; vendor | 2% illustration; "3 and 15%"; "around 3%" |
| N-K28 | FreightSimple, Freehand, FCBCO on inbound freight | undated | https://www.freightsimple.com/blog/inbound-freight-management-manufacturers | snippet; vendor | Inbound 40-60% of spend; 15-30% overpay |
| N-K29 | SmartMoving (claims); moveBuddha (AMSA move counts) | 2025-26 | https://www.smartmoving.com/blog/whats-the-ideal-cost-of-goods-sold ; https://www.movebuddha.com/blog/moving-industry-statistics/ | snippet | Claims under 1% of revenue; ~800,000 interstate moves |
| N-K30 | White-glove delivery price guides (several) | 2026 | https://amzprep.com/what-is-white-glove-delivery/ | snippet | $100-300 per stop |
| N-K31 | Locus and others on failed first attempts | 2025-26 | https://locus.sh/blogs/failed-first-attempt-delivery-cost-framework-us/ | snippet; vendor | 5-20% fail on the first attempt |
| N-K32 | Global Trade Magazine / TT on 2024 US container imports | 2025 | https://www.ttnews.com/articles/us-ports-high-note-2024 | snippet | 28.2M TEU of imports |
| N-K33 | USDA AMS GTR (via snippet), containerized ag exports | 2024 | https://www.ams.usda.gov/sites/default/files/media/GTR08222024.pdf | snippet (not found in the PDF text) | 285,000 TEU a month on average, 2021-24 |
| N-K34 | tradefinance.training, on L/C discrepancies | undated | https://www.tradefinance.training/blog/articles/discrepancies-in-documentary-credit-presentations/ | snippet | 65-75% refused on first presentation |
| N-K35 | Freightos 2018 survey (via GoFreight and others) | 2018 | https://gofreight.com/blog/education/quote-faster-win-more-speed-to-lead | snippet; vendor | "57 hours" per manual quote |
| N-K36 | GrainFlow / Farm Progress on elevator lines | 2025-26 | https://agfundernews.com/grainflow-targets-grain-elevator-gridlock-with-ai-scheduling-system | snippet; vendor | 2-4 hour waits at busy times |
| N-K37 | FAO-based snippets on US roundwood | 2018, 2023 | https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en | snippet | 439M m³ (2018); 462M m³ (2023) |
| N-K38 | PMAA (via Yahoo/PEI snippets) | undated | https://pei.org/wiki_pei/petroleum-marketers-association-america/ | snippet | "8,000 independent marketing companies" |
| N-K39 | Square 9 and others on fuel invoices | undated | https://www.square-9.com/blog/fuel-delivery-automation-reconciliation/ | snippet; vendor | "2-3% of fuel invoices contain errors" |
| N-K40 | Trucker forums on tank washouts | undated | https://www.bulkloads.com/forum/tank-washouts/ | snippet | $200 up to $1,000+ per wash |
| N-K41 | PHMSA / DOT (via snippets) | various | https://www.phmsa.dot.gov/training/hazmat/phmsas-quarterly-newsletter-hazardous-materials-safety-april-june-2022 | snippet | ~1.2M shipments a day; 94% by truck |
| N-K42 | CBP / USDA Valentine's flower releases (via snippet) | various | https://www.cbp.gov/newsroom/local-media-release/cbp-agriculture-specialists-miami-ensure-flowers-are-pest-free | snippet | "2 percent of shipments" non-compliant |
| N-K43 | Bullvine / Farm Bureau snippets on milk hauling | 2024-25 | https://www.fb.org/market-intel/milk-price-differentials-long-overdue-for-an-update | snippet | $0.7969 per cwt per farm (May 2024); NMPF $0.92-1.00 per cwt per 100 miles |
| N-K45 | FHWA, OS/OW permit pages | undated | https://ops.fhwa.dot.gov/freight/sw/permit_report/index.htm | full (no counts) | FHWA publishes no national permit count |

---

## 4. Could not access, or not found

**Blocked or broken:**
- World Grain article on 2024 grain carloads: HTTP 403. The AAR PDF was used instead.
- BTS hazmat-shipments-by-mode table: HTTP 403.
- FAOSTAT API: error 521.
- Trinity Logistics page: returned empty.
- The AMSA Senate testimony PDF: unreadable.
- WCMTOA turn-time page: shows no data.

**Not opened:** STB demurrage and accessorial data exist only in per-railroad quarterly PDFs (2018-Q1 2022). Nothing for 2023-25 was found.

**Searched, not found:**
- a national count of OS/OW permits, and permit counts for PA, FL, CA, OH, OK, MN, IA, KS and ND;
- a neutral produce rejection rate;
- tank-wash volumes;
- NLBMDA figures on delivery cost;
- a truckload cargo claims ratio;
- a neutral claims ratio for movers;
- customs-broker fee levels;
- counts of big-and-bulky deliveries and furniture-specific failure rates;
- forwarder quote volumes;
- US loaded container exports;
- official USFS roundwood tonnage;
- rates of flower fumigation and holds;
- counts of milk haulers, co-ops, Miami flower importers and transfer carriers;
- prices of the software used for most jobs.

**Tooling:** the scholarly-search server was not connected and was not used.
