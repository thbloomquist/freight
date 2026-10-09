# S1 scan E: the shipper side (Who axis)

Run 01, stage S1 "Enumerate candidates". Evidence gathered on 2026-09-14. This file lists **shipper groups** (the demand side) and the facts a candidate card needs. It does not score, rank, knock out or recommend anything, and it says nothing about pricing or which side to sell to.

**Labels.** **(V)** = verified: I read the figure in the source or computed it from a downloaded official table. **(A)** = assumed: from a search snippet, a vendor or secondary page, or my own inference. **[our calc]** = arithmetic I did. "M t" = million short tons. "$B" = billion dollars of *goods value* (what the goods are worth), not what the freight cost.

**Mode abbreviations** (they follow the Census Commodity Flow Survey codes, N-E08):
- **FH**: for-hire truck, meaning a trucking company is paid to haul.
- **PVT**: "company-owned truck", the shipper's own fleet.
- **CPU**: "customer pick-up", where the buyer collects the goods. Only the Census label was read; the full definition was not re-read (A).
- **Parcel**: parcel, USPS or courier.
- **T-R**: truck and rail.
- "t%" = share of tons; "v%" = share of value.

---

## 1. Summary

- **CFS 2022** (Commodity Flow Survey; excludes farms and imports) counts 12.17B tons. Hired trucks carry 32.1% of tons and 44.8% of value; shippers' own trucks 24.6% / 23.0%; customer pick-up 11.4% / 5.7%; parcel 0.5% / 13.4%; rail 12.0% / 3.2% (V, [our calc]).
- **Groups ship very differently** (V): beer and wine distributors move 91% of tons in own trucks, grocery wholesalers 62%; e-commerce sends 48% of tons (65% of value) by parcel; non-fuel mining has 21% customer pick-up; chemicals use 22% rail and 19% pipeline; machinery 79% hired trucks.
- **Special handling:** temperature-controlled freight is 10.2% of tons and 16.6% of value, 48% of it in shippers' own trucks; hazmat is 21.3% of tons (V, [our calc]).
- **Outside the CFS** (FAF5, 2024): food and farm commodities (SCTG 01–07) total 3.57B tons, 84% by truck; imports total 1.10B tons, 56% arriving by water. Grain 2022: 62% truck, 26% rail, 12% barge (V).
- **Counts:** 1.90M farms; 7,922 off-farm grain facilities; over 13,200 PACA produce licensees (2020); 1,221 livestock commission markets (FY2022); 239,265 manufacturing and 277,932 wholesale firms (74% and 85% with fewer than 20 employees); about 97% of 240,535 importers and 271,250 exporters are small or mid-sized (V).
- **Retailer fines:** Walmart fines suppliers 3% of cost of goods on late or incomplete deliveries (trade press, vendor).
- **Gaps:** size-specific technology data (only a vendor-relayed Gartner estimate: about 10% TMS use under $25M freight spend, A); the collect/prepaid split; CFS 2022 ton-miles; small-supplier EDI adoption.

---

## 2. Candidate shipper groups

**How to read this table:**
- Unless marked otherwise, figures are CFS 2022 for the US, all distances (N-E02 to N-E07, V).
- Firm counts come from Census SUSB 2022 (N-E17, V). "<20" means the share of firms with fewer than 20 employees. "Small-firm receipts" means the share of receipts earned by firms with fewer than 500 employees.
- "—" in the tech column means no evidence specific to that group was found. General evidence is in §3.5.
- **The "who arranges" column is limited.** The CFS only shows whether the goods moved in the shipper's own truck (PVT), a hired carrier (FH) or the customer's pick-up (CPU). It does not show who booked or paid a hired carrier: the shipper, a broker or 3PL, or the receiver on "collect" terms.
- The table has 34 rows: 17 manufacturing, mining and fuel groups (rows 1–17, one of them a commodity view), 12 wholesale, farm, retail and warehouse groups (rows 18–29), importers, exporters, big-box suppliers, and 2 cross-cutting handling types (rows 33–34).

| # | Group (plain words) | Codes | Tons · value · avg miles (year, source) | Main modes | Firms / size mix | Tech habits | Who arranges | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Food manufacturers | NAICS 311 | 614.2M t · $1,033.5B · 421 mi (2022, CFS) | FH 51.8% t (62.9% v), PVT 14.7%, rail 11.8%, CPU 10.9%, T-R 8.2% | 25,675 firms, 30,503 establishments; 74.3% <20; 666 firms 500+; small-firm receipts 21.7% | — | Mostly hired carriers; about 11% buyer pick-up | 259.9M t temperature-controlled = 21.0% of all such tons (N-E06) |
| 2 | Meat, poultry & seafood (commodity) | SCTG 05; processors in NAICS 3116/3117 | 120.0M t · $507.2B · 590 mi (2022, CFS) | FH 48.6%, PVT 32.4%, CPU 7.7%, rail 4.1% | NAICS 3116: 3,149 firms, top-50 share 77.2% (held) | — | Hired and own trucks | 119.2M t temperature-controlled, avg 592 mi; FAF 2024 SCTG 05: 95.2% truck |
| 3 | Beverage makers | 312 | 255.0M t · $176.7B · 330 mi | FH 47.2% t (69.4% v); PVT tons suppressed (19.4% v); CPU 6.3% | 11,382 firms; 79.5% <20; 114 firms 500+; small-firm receipts 20.8% | — | Hired trucks by value | Temperature-controlled 217.6M t, but CV (coefficient of variation) is 42%, so imprecise |
| 4 | Sawmills & wood products | 321 | 204.8M t · $173.9B · 310 mi | FH 43.6%, PVT 28.4%, CPU 10.3%, rail 9.5%, T-R 7.5% | 11,761 firms; 72.6% <20; small-firm receipts 42.5% | — | Mix; high own-fleet | — |
| 5 | Paper mills & converters | 322 | 177.1M t · $219.1B · 439 mi | FH 59.4%, rail 15.1%, T-R 14.8%, PVT 5.6% | 2,236 firms; 43.3% <20; 186 firms 500+; small-firm receipts 19.6% | — | Hired carriers & rail | — |
| 6 | Chemical makers | 325 | 776.1M t · $894.1B · 852 mi | FH 28.6%, rail 21.5%, pipeline 18.9%, T-R 14.4%, PVT 7.6% | 10,455 firms; 62.1% <20; 709 firms 500+; small-firm receipts 21.5% | — | Hired carriers & rail | Many hazmat movements (§3.2) |
| 7 | Plastics & rubber product makers | 326 | 72.1M t · $303.6B · 641 mi | FH 69.7%, CPU 12.0%, PVT 10.0%, T-R 5.3% | 8,369 firms; 52.3% <20; small-firm receipts 32.2% | — | Mostly hired trucks | — |
| 8 | Cement, concrete, glass & stone products | 327 | 748.8M t · $162.3B · 250 mi | PVT 41.7%, FH 30.7%, CPU 13.3%, T-R 7.8% | 8,807 firms; 68.4% <20; small-firm receipts 37.5% | — | Own fleet + buyer pick-up = 55% [our calc] | Short, heavy loads |
| 9 | Steel & metal mills | 331 | 164.3M t · $331.7B · 493 mi | FH 56.5%, rail 15.5%, T-R 11.2%, CPU 5.9% | 2,649 firms; 45.0% <20; small-firm receipts 20.5% | — | Hired carriers & rail | — |
| 10 | Fabricated metal shops | 332 | 118.1M t · $474.3B · 659 mi | FH 62.6%, PVT 14.5%, CPU 8.4%, rail 7.6%; parcel 8.5% v | 49,484 firms; 73.6% <20; small-firm receipts **53.5%** | — | Mostly hired trucks | Most fragmented large manufacturing subsector by receipts |
| 11 | Machinery makers | 333 | 41.6M t · $450.1B · 746 mi | FH 79.0% t; parcel 12.7% v | 19,028 firms; 64.6% <20; small-firm receipts 33.2% | — | Hired trucks | — |
| 12 | Electronics makers | 334 | 13.2M t · $366.2B · 1,008 mi | FH 55.7% t; by value FH 48.5%, parcel 36.4%, air 7.8% | 9,698 firms; 64.1% <20; small-firm receipts 22.9% | — | Parcel & hired trucks | High value per ton |
| 13 | Vehicle & parts makers | 336 | 113.2M t · $1,008.2B · 666 mi | FH 53.8%, T-R 16.5%, CPU 12.1%, PVT 7.5%, rail 5.9% | 9,145 firms; 59.7% <20; small-firm receipts **10.0%** | — | Hired trucks; buyer pick-up 12% | Large firms dominate |
| 14 | Furniture makers | 337 | 16.9M t · $90.4B · 574 mi | FH 59.9%, PVT 24.4%, CPU 7.3% | 14,044 firms; 81.3% <20; small-firm receipts 50.2% | — | Hired trucks + own fleet | — |
| 15 | Misc. manufacturing (medical supplies, toys, jewelry, etc.) | 339 | 10.0M t · $168.2B · 862 mi | FH 74.7% t; by value parcel 38.8% | 22,418 firms; 84.1% <20; small-firm receipts 37.7% | — | Parcel & hired trucks | — |
| 16 | Quarries & non-fuel mines (stone, sand, gravel, coal, ores) | 212 | 2,523.9M t (20.7% of CFS tons) · $100.5B · **48 mi** | FH 25.0%, **CPU 21.3%**, rail 19.0%, PVT 11.8%, T-R 10.9%, water 6.3% | 3,523 firms; 71.0% <20; small-firm receipts 28.1% | — | Highest buyer pick-up share of any industry | Gravel (SCTG 12): 30.6% CPU |
| 17 | Refiners & fuel wholesalers | 324; 4247 | 324: 1,571.9M t · $880.3B · 145 mi. 4247: 1,179.1M t · $967.6B · 107 mi | 324: pipeline 39.4%, FH 18.0%, rail 9.4%, water 7.7%. 4247: FH 40.2%, PVT 27.9%, CPU 18.9% | Firm counts not extracted (they are in N-E17) | — | 4247: 19% buyer pick-up | Hazmat |
| 18 | Grocery & food distributors | 4244 | 351.4M t · $988.5B · **103 mi** | **PVT 61.5% t (67.7% v)**, FH 31.2%, CPU 5.5% | 27,458 firms, 34,852 establishments; 82.9% <20; 385 firms 500+; small-firm receipts 31.4% | — | Own fleet dominant | Largest temperature-controlled origin: 290.0M t = 23.4% of such tons, avg 81 mi |
| 19 | Fresh produce wholesalers & shippers | 424480; SCTG 031–033 | CFS has no 6-digit detail. Temperature-controlled fresh vegetables 32.2M t at 66 mi, fruit & nuts 18.2M t at 200 mi. Q1 2026 produce truck volume 7.76M t (R34) | SCTG 03 (includes soybeans): FH 38.6%, PVT 22.5%, water 16.5%, rail 10.7%, CPU 5.2%. The water and rail shares probably reflect soybeans (A) | SUSB: 4,480 firms; 78.8% <20; 51 firms 500+; small-firm receipts **73.4%**. Over 13,200 PACA licensees (2020, all produce trades) | — | No data | 45% of Q1-2026 produce truck tons came from Mexico (R34) |
| 20 | Grain elevators & farm-product wholesalers | 4245, 424510; SCTG 02 | 4245: 661.8M t · $263.4B · 220 mi | FH 31.7%, rail 22.3%, water 15.5%, PVT 15.0%, T-R 11.3% | 4245: 3,399 firms / 6,212 establishments; 424510: 1,839 firms / 4,481 establishments. 7,922 off-farm storage facilities (Dec 2024) | — | No data | All grain, 2022: truck 62%, rail 26%, barge 12%. Exports: rail 45%, barge 44% (N-E10) |
| 21 | Grain & oilseed farms | 1111; SCTG 02 | FAF 2024 SCTG 02, all flows including farm origins: 1,326.1M t · $183.1B (2017$) · 415.1B ton-miles | Truck 78.0% t, rail 14.2%, water 5.2%. By ton-miles: truck 48.2%, rail 31.7%, water 13.4% | 330,930 farms (17.4% of farms); $163.8B sales | — | No data on who books farm-to-elevator hauls | The CFS excludes farms. Domestic grain moves 80% by truck (N-E10) |
| 22 | Fruit, vegetable, nut & greenhouse farms | 1112, 1113, 1114; SCTG 03 | FAF 2024 SCTG 03: 741.9M t · $405.6B (2017$) | Truck 83.7%, rail 7.4%, water 7.0% (SCTG 03 includes soybeans, A) | 41,793 vegetable/melon, 97,343 fruit/tree-nut and 50,785 greenhouse/nursery farms; sales $28.8B / $33.6B / $21.8B | — | No data | Growers selling only their own crop need no PACA license (N-E15) |
| 23 | Livestock & poultry producers | 1121–1123; SCTG 01 | FAF 2024 SCTG 01: 97.6M t | Truck 99.8% | 534,633 beef-cattle ranches, 11,186 feedlots, 23,153 dairies, 21,865 hog farms, 75,597 poultry & egg farms. 1,221 commission markets (auctions), 4,281 dealers/buying agencies, 90 live-poultry dealers (FY2022) | — | No data | CFS SCTG 01 from non-farm origins (2.4M t): FH 77.7% |
| 24 | Beer, wine & spirits distributors | 4248 | 64.7M t · $175.4B · 52 mi | **PVT 91.1% t**, FH 5.8% | Not extracted | — | Own fleet | Extreme own-fleet case |
| 25 | Drug & medical wholesalers | 4242 | 43.3M t · $1,087.1B · 557 mi | PVT 51.3% t, but FH 77.5% of value; parcel 10.5% v | Not extracted | — | Hired carriers by value | Temperature-controlled value $201.7B (tons suppressed) |
| 26 | Durable-goods wholesalers (building materials, hardware, electrical, machinery, auto parts) | 423 (4231–4239) | 1,309.1M t · $3,741.3B · 499 mi | PVT 43.1%, FH 29.6%, CPU 12.0% t; parcel 23.0% v | 153,128 firms / 228,785 establishments; 83.2% <20; small-firm receipts 35.5% | — | Own fleet & buyer pick-up (4233 CPU 17.5%; 4237 PVT 51.5%) | 98.7% of importers in NAICS 423 are small or mid-sized (N-E18) |
| 27 | Nondurable wholesalers in general | 424 | 2,806.2M t · $4,353.0B · 333 mi | PVT 34.4%, FH 34.2%, CPU 10.4%, rail 10.2% | 91,911 firms; 83.5% <20; small-firm receipts 28.2% | — | Mixed | 98.9% of importers in NAICS 424 are small or mid-sized |
| 28 | E-commerce & mail-order sellers | 4541 | 52.2M t · $1,007.9B · 645 mi | **Parcel 47.7% t / 65.3% v**, PVT 25.0%, FH 24.1% | 53,556 firms; 93.2% <20; 440 firms with 500+ employees hold 76.4% of receipts [our calc] | — | Parcel carriers | — |
| 29 | Warehouses & distribution centres as shippers | 4931 | 305.7M t · $1,347.7B (7.5% of CFS value, the largest single industry row) · 368 mi | FH 46.0%, PVT 43.2%, CPU 4.5%; parcel 7.5% v | 9,195 firms / 19,979 establishments; 51.3% of establishments belong to 500+ firms [our calc] | — | Hired carriers + own fleet | 109.5M t temperature-controlled |
| 30 | Importers | All; FAF import flows | FAF 2024: 1,096.9M t · $2,444.9B (2017$) | **Leg into the US:** water 55.9% t, pipeline 22.3%, truck 11.3%, rail 9.3%; air is 26.8% of value. **Leg inside the US:** truck 42.0% t / 67.5% v | 240,535 importers (2024); 97.3% small or mid-sized, holding 30.2% of known import value; 38.5% have 1–19 employees; 36.5% are wholesalers | Flexport quote on fax machines (held) | No data | — |
| 31 | Exporters | All; FAF export flows | FAF 2024 farm & food (SCTG 01–07) exports: 214.8M t | Domestic leg of those farm & food exports: truck 45.4%, rail 35.8%, water 14.6% | 271,250 exporters (2024); 97.1% small or mid-sized, holding 32.1% of value; 60.0% export to only one country | — | No data | — |
| 32 | Suppliers to big-box retailers (the receiver sets the rules) | Cross-industry | n/a | n/a | n/a | Retailers require advance ship notices (ASNs) and EDI (vendor claims, A) | Walmart "collect" = Walmart arranges the truck; "prepaid" = the supplier does | Walmart fines 3% of cost of goods on non-compliant cases. Goals: 90% on time (prepaid), 98% ready for pick-up (collect), 95% in full |
| 33 | Temperature-controlled shippers (cross-cutting) | CFS temperature-controlled flag | 1,238.0M t (10.2% of tons) · $2,992.2B (16.6%) · 290 mi | **PVT 47.7%**, FH 36.5%, CPU 5.8%, rail 3.8% | n/a | — | Own fleet is the largest mode | FH average 308 mi vs PVT 65 mi |
| 34 | Hazmat shippers (cross-cutting) | CFS hazmat | 2,590.1M t (21.3%) · $2,147.4B (11.9%) · 207 mi | Pipeline 30.0%, FH 24.5%, PVT 16.7%, rail 9.5%, CPU 9.3%, water 5.3% | n/a | — | — | — |

---

## 3. Task sections

### 3.1 Task 1: CFS 2022 by shipper industry

**Source and method.** The **Commodity Flow Survey (CFS)** is a Census survey of shipments from mining, manufacturing, wholesale, selected retail and company warehouses. It excludes farms, imports and most services (R32).
- The 2022 Census API endpoints exist (`cfsarea`, `cfstemp`, `cfshazmat`, `cfsexport`), but my queries returned empty responses. I therefore downloaded the published tables from the Census FTP site: CF2200A01, A04, A05, A09, A18, TC01/04/05 and H01 (N-E01 to N-E07).
- **"NAICS"** is the North American Industry Classification System. The CFS tables use NAICS 2017 codes.
- **"Avg mi"** is the CFS field "Average distance (GCD) per shipment", a great-circle (straight-line) distance averaged over shipments. Parcel-heavy groups therefore look long-haul.
- "S" means suppressed by Census; "–" means not published.
- Coefficients of variation (CVs, a measure of sampling error) are in the files. At national level, the water mode has CVs of 12–13% and Great Lakes 42–48% (V). I did not review industry-level CVs cell by cell.
- **Ton-miles are not published** in the 2022 tables. The API has no ton-mile variable.

**National totals by mode, 2022** (N-E01, V; percentages are [our calc]):

| Mode | Tons (M) | % tons | Value ($B) | % value | Avg mi/shipment |
|---|---|---|---|---|---|
| All modes | 12,169.8 | 100 | 17,996.8 | 100 | 552 (2017: 679) |
| For-hire truck | 3,909.5 | 32.1 | 8,062.5 | 44.8 | 381 |
| Company-owned truck | 2,994.4 | 24.6 | 4,141.6 | 23.0 | 174 |
| Customer pick-up | 1,389.7 | 11.4 | 1,018.9 | 5.7 | 139 |
| Parcel, USPS or courier | 61.7 | 0.5 | 2,403.0 | 13.4 | 776 |
| Rail | 1,456.5 | 12.0 | 568.5 | 3.2 | 614 |
| Water (inland 232.6; Great Lakes 47.1; deep sea 155.7) | 435.4 | 3.6 | 171.1 | 1.0 | 409 |
| Air (includes truck-air) | 5.2 | 0.04 | 155.9 | 0.9 | 1,254 |
| Pipeline | 799.8 | 6.6 | 589.6 | 3.3 | (0 reported) |
| Truck and rail | 841.6 | 6.9 | 587.7 | 3.3 | 747 |
| Truck and water | 96.0 | 0.8 | 80.4 | 0.4 | 865 |
| Rail and water | 36.2 | 0.3 | 5.8 | 0.03 | 593 |
| Other multiple modes | S | S | 2.2 | 0.01 | 1,578 |
| Other single modes | 40.8 | 0.3 | 1.4 | 0.01 | 4 |
| Unknown | 101.7 | 0.8 | 208.2 | 1.2 | 471 |

For 2017 the table gives all modes at 12,468.9M t and $14,517.8B (V). Tonnage fell 2.4% from 2017 to 2022 and value rose 24.0% (the published percent changes; V).

**Industry by mode, 2022** (N-E02 tons and value by mode; N-E03 average miles; V). The t% and v% columns are [our calc] from the published cells.

| NAICS | Industry | Tons (M) | Value ($B) | Avg mi | FH t% / v% | PVT t% / v% | CPU t% / v% | Parcel t% / v% | Rail t% | Truck-rail t% | Water t% | Pipeline t% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 00 | Total for all sectors | 12,169.8 | 17,996.8 | 552 | 32.1 / 44.8 | 24.6 / 23.0 | 11.4 / 5.7 | 0.5 / 13.4 | 12.0 | 6.9 | 3.6 | 6.6 |
| 212 | Mining (except oil and gas) | 2,523.9 | 100.5 | 48 | 25.0 / 38.5 | 11.8 / 8.6 | 21.3 / 8.4 | S / S | 19.0 | 10.9 | 6.3 | S |
| 31-33 | Manufacturing | 4,950.0 | 7,073.5 | 666 | 35.2 / 53.7 | 19.1 / 8.5 | 7.7 / 6.1 | 0.2 / 7.2 | 10.3 | 7.3 | 3.0 | 15.5 |
| 311 | Food mfg | 614.2 | 1,033.5 | 421 | 51.8 / 62.9 | 14.7 / 12.5 | 10.9 / 11.2 | 0.1 / 0.5 | 11.8 | 8.2 | S | 0.3 |
| 312 | Beverage and tobacco product mfg | 255.0 | 176.7 | 330 | 47.2 / 69.4 | S / 19.4 | 6.3 / 5.4 | 0.1 / 2.2 | 0.8 | 1.0 | 0.0 | 0.2 |
| 313 | Textile mills | 5.4 | 28.1 | 690 | 63.4 / 66.7 | 20.4 / 16.3 | 8.1 / 6.8 | 1.0 / 5.3 | 0.4 | 4.7 | S | – |
| 314 | Textile product mills | 4.0 | 26.0 | 725 | 48.8 / 48.5 | 31.4 / 21.4 | 10.4 / 8.7 | 5.1 / 19.6 | S | 2.4 | S | – |
| 315 | Apparel mfg | 1.0 | 11.0 | 1019 | 78.2 / 41.3 | 5.1 / 8.0 | S / 3.8 | 8.5 / 46.1 | – | – | – | – |
| 316 | Leather and allied product mfg | 0.5 | 5.2 | 1037 | 59.3 / 34.5 | 8.0 / 10.5 | S / S | 7.4 / 43.0 | S | S | – | – |
| 321 | Wood product mfg | 204.8 | 173.9 | 310 | 43.6 / 50.0 | 28.4 / 30.2 | 10.3 / 6.9 | 0.0 / 0.2 | 9.5 | 7.5 | S | – |
| 322 | Paper mfg | 177.1 | 219.1 | 439 | 59.4 / 70.1 | 5.6 / 9.8 | 3.5 / 4.4 | 0.0 / S | 15.1 | 14.8 | S | S |
| 323 | Printing and related support activities | 21.1 | 95.4 | 636 | 72.8 / 52.8 | 8.0 / 12.2 | 3.2 / 4.3 | 6.5 / 27.8 | S | S | 0.4 | – |
| 324 | Petroleum and coal products mfg | 1,571.9 | 880.3 | 145 | 18.0 / 15.5 | S / 1.8 | 5.3 / 1.7 | 0.0 / 0.0 | 9.4 | 2.8 | 7.7 | 39.4 |
| 325 | Chemical mfg | 776.1 | 894.1 | 852 | 28.6 / 51.4 | 7.6 / 4.1 | 5.3 / 4.1 | S / 4.8 | 21.5 | 14.4 | 2.2 | 18.9 |
| 326 | Plastics and rubber products mfg | 72.1 | 303.6 | 641 | 69.7 / 73.3 | 10.0 / 10.5 | 12.0 / 9.0 | 0.4 / 3.5 | 1.6 | 5.3 | S | S |
| 327 | Nonmetallic mineral product mfg | 748.8 | 162.3 | 250 | 30.7 / 58.9 | 41.7 / 21.4 | 13.3 / 8.6 | 0.0 / 2.4 | 4.1 | 7.8 | S | 0.0 |
| 331 | Primary metal mfg | 164.3 | 331.7 | 493 | 56.5 / 68.9 | 5.0 / 4.7 | 5.9 / 4.9 | 0.0 / 0.8 | 15.5 | 11.2 | 3.5 | – |
| 332 | Fabricated metal product mfg | 118.1 | 474.3 | 659 | 62.6 / 63.1 | 14.5 / 14.6 | 8.4 / 7.6 | 0.5 / 8.5 | 7.6 | 5.1 | S | – |
| 333 | Machinery mfg | 41.6 | 450.1 | 746 | 79.0 / 71.2 | 6.1 / 5.0 | 6.0 / 4.7 | 1.5 / 12.7 | 1.0 | 4.1 | S | – |
| 334 | Computer and electronic product mfg | 13.2 | 366.2 | 1008 | 55.7 / 48.5 | S / 2.9 | 1.5 / 1.5 | 3.6 / 36.4 | S | 9.2 | S | S |
| 335 | Electrical equipment, appliance, and component mfg | 20.5 | 175.0 | 948 | 78.3 / 68.2 | 1.9 / 2.7 | S / 3.4 | 1.6 / 19.1 | 4.9 | 7.7 | – | S |
| 336 | Transportation equipment mfg | 113.2 | 1,008.2 | 666 | 53.8 / 49.7 | 7.5 / 6.9 | 12.1 / 8.5 | 0.4 / 6.4 | 5.9 | 16.5 | – | S |
| 337 | Furniture and related product mfg | 16.9 | 90.4 | 574 | 59.9 / 63.4 | 24.4 / 23.7 | 7.3 / 6.8 | 2.0 / 4.3 | 1.5 | 4.6 | S | S |
| 339 | Miscellaneous mfg | 10.0 | 168.2 | 862 | 74.7 / 48.2 | 3.7 / 5.2 | 4.4 / 3.2 | 9.5 / 38.8 | S | 3.9 | S | – |
| 42 | Wholesale trade | 4,115.3 | 8,094.4 | 438 | 32.8 / 41.3 | 37.2 / 32.4 | 10.9 / 6.7 | 0.6 / 13.6 | 9.2 | 4.6 | 2.9 | 0.5 |
| 423 | Wholesalers, durable goods | 1,309.1 | 3,741.3 | 499 | 29.6 / 39.2 | 43.1 / 27.0 | 12.0 / 6.1 | 1.4 / 23.0 | S | 5.5 | S | S |
| 4231 | Motor vehicle and parts wholesalers | 87.7 | 605.9 | 402 | 47.7 / 39.9 | 38.7 / 37.3 | 5.6 / 4.8 | 2.9 / 14.6 | S | 1.4 | – | – |
| 4232 | Furniture and home furnishing wholesalers | 31.4 | 117.6 | 850 | 54.9 / 51.6 | 19.4 / 22.0 | 5.5 / 6.8 | 4.9 / 15.6 | 7.5 | 6.5 | S | – |
| 4233 | Lumber and other construction materials wholesalers | 658.5 | 287.8 | 206 | 10.9 / 26.6 | S / 64.6 | 17.5 / 4.2 | 0.0 / 1.3 | S | S | S | S |
| 4234 | Professional and commercial equipment wholesalers | 27.5 | 610.8 | 595 | 52.1 / 36.8 | 24.2 / 14.6 | 1.9 / 3.0 | 18.3 / 40.9 | S | S | S | S |
| 4235 | Metal and mineral (except petroleum) wholesalers | 111.4 | 238.7 | 200 | 45.4 / 51.9 | 29.0 / 34.9 | 5.5 / 6.5 | 0.1 / 1.2 | S | 4.0 | 0.1 | – |
| 4236 | Household appliance and electrical/electronic goods wholesalers | 50.5 | 679.7 | 527 | 46.0 / 39.0 | 27.1 / 17.7 | 11.2 / 7.1 | 5.9 / 30.8 | S | 7.3 | – | – |
| 4237 | Hardware, plumbing and heating wholesalers | 31.9 | 261.9 | 316 | 30.5 / 32.2 | 51.5 / 44.8 | 11.1 / 10.8 | 2.9 / 10.7 | 0.9 | 2.3 | S | S |
| 4238 | Machinery, equipment, and supplies wholesalers | 95.7 | 618.8 | 395 | 50.1 / 38.8 | 31.6 / 19.4 | 9.5 / 9.3 | 3.8 / 27.6 | 1.0 | 2.7 | S | – |
| 4239 | Miscellaneous durable goods wholesalers | 214.4 | 320.1 | 880 | 52.0 / 46.9 | 19.1 / 12.7 | 4.6 / 3.8 | 0.7 / 27.3 | 7.4 | 13.6 | S | S |
| 424 | Wholesalers, nondurable goods | 2,806.2 | 4,353.0 | 333 | 34.2 / 43.1 | 34.4 / 37.0 | 10.4 / 7.2 | 0.2 / 5.6 | 10.2 | 4.1 | 4.3 | 0.7 |
| 4241 | Paper and paper product wholesalers | 43.1 | 136.6 | 274 | 29.8 / 28.0 | 60.8 / 53.0 | 3.7 / 4.2 | 2.8 / 12.6 | S | 0.8 | 0.0 | – |
| 4242 | Drugs and druggists' sundries wholesalers | 43.3 | 1,087.1 | 557 | 40.6 / 77.5 | 51.3 / 8.6 | 0.9 / 0.4 | 3.5 / 10.5 | S | 2.3 | S | – |
| 4243 | Apparel, piece goods, and notions wholesalers | 8.1 | 145.0 | 925 | 55.2 / 34.0 | 7.3 / 3.5 | 10.8 / 8.3 | 21.8 / 52.6 | S | 1.6 | S | – |
| 4244 | Grocery and related product wholesalers | 351.4 | 988.5 | 103 | 31.2 / 26.1 | 61.5 / 67.7 | 5.5 / 4.2 | 0.1 / 0.5 | S | 0.6 | 0.0 | – |
| 4245 | Farm product raw material wholesalers | 661.8 | 263.4 | 220 | 31.7 / 36.9 | 15.0 / 16.5 | 3.1 / 2.8 | 0.0 / 0.3 | 22.3 | 11.3 | 15.5 | 0.0 |
| 4246 | Chemical and allied products wholesalers | 228.1 | 203.6 | 237 | 27.9 / 50.4 | 45.1 / 32.8 | 4.0 / 6.6 | 0.2 / 4.2 | S | 5.1 | 0.0 | 0.1 |
| 4247 | Petroleum and petroleum products wholesalers | 1,179.1 | 967.6 | 107 | 40.2 / 38.4 | 27.9 / 28.2 | 18.9 / 21.3 | S / S | 6.8 | 1.0 | S | 1.7 |
| 4248 | Beer, wine, and distilled alcoholic beverage wholesalers | 64.7 | 175.4 | 52 | 5.8 / 9.6 | 91.1 / 86.2 | 1.8 / 2.9 | 0.0 / 0.3 | 0.2 | 0.5 | S | – |
| 4249 | Miscellaneous nondurable goods wholesalers | 226.5 | 385.9 | 453 | 29.0 / 25.3 | 48.3 / 61.4 | 7.6 / 5.0 | 0.4 / 4.9 | 8.1 | 6.1 | 0.0 | S |
| 4541 | Electronic shopping and mail-order houses | 52.2 | 1,007.9 | 645 | 24.1 / 11.4 | 25.0 / 22.1 | 0.9 / 0.4 | 47.7 / 65.3 | S | S | S | S |
| 45431 | Fuel dealers | 46.0 | 43.3 | 19 | S / 3.1 | 92.6 / 95.3 | 0.8 / 0.8 | 0.0 / S | 0.5 | 0.3 | – | S |
| 4931 | Warehousing and storage | 305.7 | 1,347.7 | 368 | 46.0 / 47.1 | 43.2 / 39.6 | 4.5 / 1.4 | 0.9 / 7.5 | S | 1.3 | 0.9 | 0.0 |
| 5111 | Newspaper, periodical, book, and directory publishers | 1.9 | 16.4 | 0 | 57.2 / 58.6 | 26.4 / 12.5 | 2.1 / 1.3 | 8.3 / 23.4 | S | S | S | – |
| 551114 | Corporate, subsidiary, and regional managing offices | 174.8 | 313.2 | 581 | 17.6 / 38.7 | 19.0 / 35.3 | 3.0 / 4.3 | 0.3 / 9.4 | 45.5 | 6.1 | 0.4 | 5.4 |

**Largest industries** (codes at 3–4 digits, sector totals excluded; V, shares [our calc]):
- **By tons:** mining 212 (20.7%); petroleum refining 324 (12.9%); petroleum wholesalers 4247 (9.7%); chemicals 325 (6.4%); nonmetallic minerals 327 (6.2%); farm-product wholesalers 4245 (5.4%); lumber and construction-materials wholesalers 4233 (5.4%); food 311 (5.0%); grocery wholesalers 4244 (2.9%); warehousing 4931 (2.5%); beverages 312 (2.1%); chemical wholesalers 4246 (1.9%); miscellaneous nondurable wholesalers 4249 (1.9%); miscellaneous durable wholesalers 4239 (1.8%); wood 321 (1.7%); paper 322 (1.5%); managing offices 551114 (1.4%); primary metals 331 (1.4%); fabricated metals 332 (1.0%); transportation equipment 336 (0.9%).
- **By value:** warehousing 4931 (7.5%); drug wholesalers 4242 (6.0%); food 311 (5.7%); transportation equipment 336 (5.6%); e-commerce 4541 (5.6%); grocery wholesalers 4244 (5.5%); petroleum wholesalers 4247 (5.4%); chemicals 325 (5.0%); refining 324 (4.9%); appliance and electronics wholesalers 4236 (3.8%); machinery wholesalers 4238 (3.4%); professional equipment wholesalers 4234 (3.4%); auto-parts wholesalers 4231 (3.4%); fabricated metals 332 (2.6%); machinery 333 (2.5%); miscellaneous nondurable wholesalers 4249 (2.1%); electronics 334 (2.0%); primary metals 331 (1.8%); miscellaneous durable wholesalers 4239 (1.8%); managing offices 551114 (1.7%).

**Facts that separate groups** (V unless marked):
- **Share of all CFS freight** [our calc]: manufacturing is 40.7% of tons and 39.3% of value; wholesale is 33.8% and 45.0%.
- **Own-fleet share of tons:** wholesale 37.2%, manufacturing 19.1%. The own-fleet extremes are fuel dealers (92.6%), beer and wine distributors (91.1%), grocery wholesalers (61.5%), paper wholesalers (60.8%), hardware and plumbing wholesalers (51.5%) and drug wholesalers (51.3%).
- **Customer pick-up above 12% of tons:** mining 21.3%, petroleum wholesalers 18.9%, lumber and construction-materials wholesalers 17.5%, nonmetallic mineral products 13.3%, transportation equipment 12.1%, plastics 12.0% and durable wholesalers overall 12.0%.
- **Customer pick-up at 1.5% or less:** e-commerce 0.9%, drug wholesalers 0.9%, fuel dealers 0.8% and electronics 1.5%.
- **Parcel above 35% of value:** e-commerce 65.3%, apparel wholesalers 52.6%, apparel manufacturing 46.1%, leather 43.0%, professional equipment wholesalers 40.9%, miscellaneous manufacturing 38.8% and electronics 36.4%.
- **Rail-heavy:** managing offices 551114 (45.5%), farm-product wholesalers (22.3%), chemicals (21.5%) and mining (19.0%). The 551114 row covers auxiliary establishments of multi-unit companies, such as head-office-controlled shipping points (A, definition not re-read).
- **Average shipment distance:** under 110 miles for mining (48), fuel dealers (19), beer wholesalers (52), grocery wholesalers (103) and petroleum wholesalers (107); about 1,000 miles or more for electronics (1,008), apparel manufacturing (1,019) and leather (1,037).

### 3.2 Task 2: CFS 2022 by commodity (SCTG 2-digit)

**SCTG** is the Standard Classification of Transported Goods, the commodity code used by the CFS and FAF. The table below lists every commodity in the top 22 by tons or by value (N-E04 totals and average miles; N-E05 modes; V; shares [our calc]).

| SCTG | Commodity | Rank tons / value | Tons (M) | Value ($B) | Avg mi | FH t% / v% | PVT t% / v% | CPU t% / v% | Parcel v% | Rail t% | Truck-rail t% | Water t% | Pipeline t% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | Gravel and crushed stone | 1 / 36 | 1,910.9 | 29.9 | 33 | 24.7 / 27.2 | 19.9 / 27.9 | 30.6 / 27.4 | S | 8.3 | 10.7 | 3.7 | 0.0 |
| 31 | Non-metallic mineral products | 2 / 23 | 1,192.0 | 257.5 | 648 | 23.2 / 50.6 | 53.9 / 34.3 | 7.4 / 6.8 | 2.9 | S | 7.1 | S | S |
| 17 | Gasoline and aviation turbine fuel | 3 / 6 | 1,036.6 | 893.8 | 40 | 33.0 / 31.5 | 9.3 / 10.0 | 13.9 / 14.7 | S | 5.3 | 2.2 | 2.7 | 33.4 |
| 19 | Other coal and petroleum products n.e.c. | 4 / 17 | 869.8 | 435.9 | 161 | 30.3 / 30.9 | 18.9 / 17.0 | 7.7 / S | S | 17.5 | 2.3 | 5.9 | 13.9 |
| 18 | Fuel oils | 5 / 12 | 672.9 | 608.2 | 29 | 16.5 / 15.6 | 24.2 / 25.8 | 9.9 / 11.0 | 0.0 | 6.1 | 1.8 | 8.0 | 31.6 |
| 07 | Other prepared foodstuffs, fats and oils | 6 / 7 | 629.4 | 796.9 | 367 | 45.4 / 53.3 | 31.5 / 26.6 | 9.5 / 8.8 | 1.7 | 6.2 | 5.0 | S | 0.3 |
| 15 | Coal | 7 / 35 | 560.5 | 31.9 | 64 | 11.5 / 13.3 | S / S | 0.2 / 0.4 | – | 57.0 | 7.6 | 6.7 | – |
| 02 | Cereal grains | 8 / 29 | 491.1 | 132.7 | 221 | 29.4 / 30.4 | 14.7 / 14.8 | 3.5 / 3.1 | S | 25.7 | 13.3 | 12.4 | – |
| 20 | Basic chemicals | 9 / 19 | 489.8 | 336.1 | 308 | 16.3 / 37.2 | 27.3 / 16.2 | 2.8 / 3.8 | 2.3 | 14.5 | 11.4 | 3.1 | 22.3 |
| 11 | Natural sands | 10 / 39 | 455.1 | 7.5 | 66 | 29.5 / 40.3 | 14.2 / 13.2 | 24.8 / 23.5 | S | 12.3 | 7.1 | S | – |
| 43 | Mixed freight | 11 / 1 | 433.9 | 1,728.4 | 327 | 32.5 / 27.3 | 62.7 / 65.2 | 1.8 / 1.9 | 4.4 | 0.7 | 0.8 | 0.0 | S |
| 04 | Animal feed, eggs, honey, other animal products | 12 / 26 | 335.6 | 179.8 | 646 | 43.0 / 48.3 | 20.2 / 22.4 | 11.1 / 11.8 | 2.1 | 17.3 | 7.0 | 0.8 | S |
| 26 | Wood products | 13 / 18 | 315.0 | 372.5 | 339 | 40.7 / 40.0 | 37.0 / 45.8 | 8.5 / 5.3 | S | 7.7 | 5.1 | S | – |
| 32 | Base metal in primary/semi-finished forms | 14 / 11 | 291.7 | 615.0 | 366 | 55.4 / 61.2 | 16.8 / 18.4 | 6.2 / 6.1 | 1.0 | 10.8 | 7.0 | S | – |
| 03 | Agricultural products (incl. fresh produce, soybeans) | 15 / 22 | 260.3 | 269.3 | 316 | 38.6 / 41.3 | 22.5 / 31.4 | 5.2 / 7.2 | 1.4 | 10.7 | 5.4 | 16.5 | S |
| 24 | Plastics and rubber | 16 / 8 | 239.6 | 769.9 | 514 | 43.2 / 54.2 | 14.3 / 19.8 | 5.9 / 6.1 | 5.6 | 16.2 | 16.1 | S | S |
| 36 | Motorized and other vehicles (incl. parts) | 17 / 3 | 199.3 | 1,466.3 | 472 | 56.0 / 47.4 | 16.2 / 15.5 | 10.0 / 8.0 | 9.1 | 2.9 | 10.6 | S | S |
| 41 | Waste and scrap | 18 / 31 | 178.1 | 97.2 | 171 | 54.4 / 61.3 | 18.5 / 15.2 | 3.9 / 3.1 | S | 8.6 | 12.2 | S | S |
| 23 | Other chemical products n.e.c. | 19 / 14 | 154.4 | 488.0 | 545 | 40.5 / 53.7 | 34.2 / 19.7 | 5.3 / 5.1 | 13.7 | 7.1 | 6.8 | 0.0 | 0.1 |
| 22 | Fertilizers | 20 / 33 | 131.1 | 79.9 | 193 | 24.4 / 25.6 | 37.3 / 44.5 | 6.3 / 7.3 | S | 16.7 | 8.6 | 5.0 | S |
| 08 | Alcoholic beverages | 21 / 21 | 129.3 | 279.1 | 193 | 33.1 / 27.7 | 54.7 / 61.1 | 2.7 / 4.0 | 2.4 | 4.4 | 3.9 | S | 0.3 |
| 05 | Meat, poultry, fish, seafood | 22 / 13 | 120.0 | 507.2 | 590 | 48.6 / 50.5 | 32.4 / 34.2 | 7.7 / 7.0 | S | 4.1 | 2.1 | 0.1 | – |
| 40 | Miscellaneous manufactured products | 23 / 9 | 114.7 | 702.5 | 643 | 42.3 / 39.2 | 21.1 / 17.1 | 3.8 / 3.3 | 37.2 | S | 5.2 | 0.0 | S |
| 33 | Articles of base metal | 28 / 15 | 100.5 | 461.3 | 602 | 55.4 / 53.9 | 19.3 / 20.1 | 8.7 / 7.0 | 13.1 | 3.2 | 10.1 | S | S |
| 35 | Electronic and electrical equipment | 29 / 2 | 98.9 | 1,614.5 | 608 | 59.6 / 46.0 | 17.6 / 12.5 | 6.8 / 4.7 | 30.9 | 1.3 | 6.5 | S | S |
| 34 | Machinery | 30 / 5 | 90.1 | 954.8 | 445 | 58.2 / 57.5 | 20.4 / 12.9 | 10.6 / 8.7 | 15.7 | 1.6 | 4.7 | S | S |
| 30 | Textiles, leather and articles | 32 / 10 | 46.8 | 685.2 | 762 | 50.0 / 37.7 | 17.9 / 14.4 | 5.1 / 3.1 | 43.1 | 0.3 | 1.5 | S | S |
| 21 | Pharmaceutical products | 33 / 4 | 33.4 | 1,459.9 | 468 | 48.8 / 66.0 | 14.8 / 5.7 | 1.4 / 0.5 | 24.1 | 12.3 | 7.7 | S | – |
| 38 | Precision instruments | 36 / 16 | 13.2 | 452.5 | 637 | 40.6 / 31.3 | 18.5 / 9.5 | 4.3 / 2.0 | 50.4 | S | 4.0 | 0.0 | – |
| 37 | Transportation equipment n.e.c. | 38 / 20 | 10.0 | 297.1 | 784 | 37.9 / 36.1 | 6.3 / 11.0 | 2.4 / 1.8 | 29.6 | 17.8 | 5.6 | – | – |

Note: 37 also has air at 26.3% of tons (V).

**Temperature-controlled shipments** (the CFS 2022 temperature-control series, N-E06, V; shares [our calc]). These are shipments that need refrigeration or other temperature control, usually in "reefer" (refrigerated) trailers.
- **Size:** 1,238.0M t (10.2% of CFS tons) and $2,992.2B (16.6% of CFS value), with an average of 290 miles per shipment.
- **By mode (share of temperature-controlled tons):** own truck 47.7% (average 65 mi); for-hire truck 36.5% (308 mi); customer pick-up 5.8% (124 mi); rail 3.8% (945 mi); truck-rail 2.3%; water 1.4%; parcel 0.2%. Parcel is still $155.7B of value.
- **By originating industry (share of temperature-controlled tons):** grocery wholesalers 4244 23.4% (avg 81 mi); food manufacturing 311 21.0% (316 mi); beverage manufacturing 312 17.6% (CV 42%); warehousing 4931 8.8%; beer and wine wholesalers 4248 5.1%; chemicals 325 5.1%. Drug wholesalers 4242 ship $201.7B of temperature-controlled value (tons suppressed).
- **By commodity:** other prepared foods SCTG 07 is 32.3% of these tons, including nonalcoholic beverages 221.8M t and dairy 98.2M t. Mixed freight is 17.7%, alcoholic beverages 9.7% and meat/seafood 9.6% (meat and poultry 114.2M t at 657 mi). Agricultural products are 5.6% (fresh vegetables 32.2M t at 66 mi, fruit and nuts 18.2M t at 200 mi, potatoes 13.5M t at 99 mi). Pharmaceuticals are $416.8B of value but only 3.8M t.

**Hazmat** (hazardous materials; the CFS 2022 hazmat series, N-E07, V; shares [our calc]):
- **Size:** 2,590.1M t (21.3% of CFS tons) and $2,147.4B (11.9% of value), with an average of 207 miles.
- **By mode (share of hazmat tons):** pipeline 30.0%, for-hire truck 24.5% (171 mi), own truck 16.7% (32 mi), rail 9.5% (493 mi), customer pick-up 9.3% (29 mi), water 5.3%, truck-rail 3.7%.

### 3.3 Task 3: Farm-origin and import freight (outside the CFS)

**FAF5.7.1** (Freight Analysis Framework; BTS/FHWA/ORNL) combines the CFS with farm, import, export and other flows. I downloaded the 2018–2024 file (N-E09; the zip unpacks to a 695 MB CSV) and summed national totals. The FAF data dictionary gives the units: tons in thousand tons, "value" in million 2017 constant dollars, ton-miles in million (V). "Domestic mode" is the mode for the US portion of the trip. Imports also have a "foreign inbound mode", the mode used to reach the US entry point. All shares are [our calc].

**All flows by domestic mode, 2024:**

| Domestic mode | Tons (M) | % | Value ($B, 2017$) | % | Ton-miles (B) | % |
|---|---|---|---|---|---|---|
| Total | 20,011.5 | 100 | 18,991.2 | 100 | 5,381.7 | 100 |
| Truck | 12,843.9 | 64.2 | 13,698.7 | 72.1 | 2,408.1 | 44.7 |
| Rail | 1,532.8 | 7.7 | 583.8 | 3.1 | 970.4 | 18.0 |
| Water | 771.5 | 3.9 | 259.2 | 1.4 | 349.5 | 6.5 |
| Air (incl. truck-air) | 6.7 | 0.03 | 646.9 | 3.4 | 7.8 | 0.1 |
| Multiple modes & mail | 634.5 | 3.2 | 2,618.5 | 13.8 | 544.9 | 10.1 |
| Pipeline | 4,025.3 | 20.1 | 1,109.3 | 5.8 | 1,093.2 | 20.3 |
| Other/unknown | 80.3 | 0.4 | 34.2 | 0.2 | 7.8 | 0.1 |
| No domestic mode | 116.4 | 0.6 | 40.6 | 0.2 | 0 | 0 |

The 2022 total was 19,827.2M t, of which truck was 63.9% (V).

**Food and farm commodities (SCTG 01–07), 2024, by domestic mode:**
- All flows: 3,569.3M t (17.8% of FAF tons), $2,334.6B, 1,179.0B ton-miles. Truck 83.8% of tons, 90.7% of value and 60.0% of ton-miles; rail 8.9% / 3.8% / 20.4%; water 3.7% / 1.6% / 8.8%; multiple modes & mail 3.5% / 3.7% / 10.8%.
- Domestic flows only: 3,274.4M t, of which truck 86.6%, rail 6.8%, water 3.1% and multiple modes 3.5%.

| SCTG (FAF 2024, all trade types) | Tons (M) | Truck | Rail | Water | Multiple modes & mail |
|---|---|---|---|---|---|
| 01 Live animals/fish | 97.6 | 99.8% | 0.0% | 0.0% | 0.1% |
| 02 Cereal grains | 1,326.1 | 78.0% | 14.2% | 5.2% | 2.6% |
| 03 Other agricultural products | 741.9 | 83.7% | 7.4% | 7.0% | 1.9% |
| 04 Animal feed | 457.7 | 87.2% | 6.2% | 1.6% | 5.0% |
| 05 Meat/seafood | 111.2 | 95.2% | 1.6% | 0.9% | 2.3% |
| 06 Milled grain products | 146.8 | 84.7% | 5.5% | 0.0% | 9.7% |
| 07 Other foodstuffs | 687.9 | 88.7% | 5.0% | 0.7% | 5.5% |

- SCTG 05–07 are processed foods from manufacturers, not raw farm output.
- FAF's cereal grain tonnage (1,326.1M t, 2024) is much larger than the CFS figure (491.1M t, 2022). Most of the gap is probably shipments that start on farms, which the CFS excludes (A).

**Imports, 2024:** 1,096.9M t (5.5% of FAF tons) and $2,444.9B (2017$).

| Mode | Foreign inbound: % tons | Foreign inbound: % value | Domestic leg: % tons | Domestic leg: % value |
|---|---|---|---|---|
| Water | 55.9 | 45.5 | 3.7 | 1.5 |
| Pipeline | 22.3 | 2.6 | 23.4 | 2.7 |
| Truck | 11.3 | 18.2 | 42.0 | 67.5 |
| Rail | 9.3 | 4.3 | 15.1 | 9.0 |
| Air | 0.5 | 26.8 | 0.2 | 10.3 |
| Multiple modes & mail | 0.5 | 2.3 | 4.8 | 7.0 |
| No domestic mode | – | – | 10.6 | 1.7 |

- **Farm and food imports (SCTG 01–07), 2024:** 80.1M t and $154.0B. Foreign inbound mode: truck 44.2%, water 39.0%, rail 14.2%, air 1.7%. Domestic leg: truck 73.8%, rail 18.6%.
- **Farm and food exports:** 214.8M t. Domestic leg to the port or border: truck 45.4%, rail 35.8%, water 14.6%.

**Grain modal shares** (USDA AMS, "Transportation of U.S. Grains: A Modal Share Analysis, 1984–2022 Update", September 2024; N-E10, V). On method, the report says: "Truck tonnages are estimated by subtracting barge and rail tonnages from total tonnages transported."

| 2022 | Rail | Barge | Truck | Total moved |
|---|---|---|---|---|
| All grains | 151.3M t (26%) | 69.8M t (12%) | 353.7M t (62%) | 574.8M t |
| Exports | 69.1M t (45%) | 66.7M t (44%) | 17.6M t (11%) | 153.4M t |
| Domestic | 82.2M t (20%) | 3.1M t (1%) | 336.1M t (80%) | 421.4M t |
| Corn, all | 22% | 8% | 70% | 380.6M t |
| Wheat, all | 56% | 15% | 29% | 52.6M t |

- The rail share for all grains averaged 24% over the last five years (Table 3); soybeans were 25% by rail in 2022.
- Trend: truck's share of all grain rose from 52% in 2005 to 62–66% in 2019–2022 (Table 2).

**Farms by type** (2022 Census of Agriculture, Table 48; N-E11, V; percentages [our calc]):

| NAICS | Farm type | Farms | % of farms | Sales ($B) |
|---|---|---|---|---|
| 1111 | Oilseed & grain | 330,930 | 17.4 | 163.8 |
| 11115 | of which corn | 167,911 | 8.8 | 93.1 |
| 11111 | of which soybean | 85,688 | 4.5 | 21.1 |
| 11114 | of which wheat | 23,550 | 1.2 | 7.4 |
| 1112 | Vegetable & melon | 41,793 | 2.2 | 28.8 |
| 1113 | Fruit & tree nut | 97,343 | 5.1 | 33.6 |
| 1114 | Greenhouse, nursery, floriculture | 50,785 | 2.7 | 21.8 |
| 1119 | Other crops (235,498 are hay farms) | 443,926 | 23.4 | 28.1 |
| 112111 | Beef cattle ranching | 534,633 | 28.1 | 36.0 |
| 112112 | Cattle feedlots | 11,186 | 0.6 | 45.9 |
| 11212 | Dairy | 23,153 | 1.2 | 60.4 |
| 1122 | Hog & pig | 21,865 | 1.2 | 37.7 |
| 1123 | Poultry & egg (broilers 14,971; eggs 50,090) | 75,597 | 4.0 | 77.9 |
| 1124 / 1125 | Sheep & goat / aquaculture | 79,398 / 4,637 | 4.2 / 0.2 | 1.0 / 2.2 |
| Total | All farms | 1,900,487 | 100 | 543.1 |

**Farms by sales size** (Table 72; N-E12, V):
- 105,384 farms (5.5%) had $1M or more in agricultural sales. Together they sold $425.4B of the $543.1B total, or 78.3% [our calc].
- 993,704 farms (52.3%) are in the economic classes below $10,000 [our calc, summing four rows].

**Grain elevators and off-farm storage** (NASS Grain Stocks, January 10, 2025; N-E13, V):
- "Off-farm storage facilities totaled 7,922 on December 1, 2024, down 1 percent from the December 1, 2023 estimate."
- Off-farm capacity was 11.8 billion bushels. It "includes all elevators, warehouses, terminals, merchant mills, other storage, and oilseed…" facilities.
- On-farm capacity was 13.6 billion bushels.

**Produce dealers (PACA)** (N-E14, N-E15, V). PACA is the Perishable Agricultural Commodities Act, the federal licensing and fair-trade law for fruit and vegetable dealers.
- "PACA Highlights – 2020: PACA maintained over 13,200 active licensees; PACA renewed 8940 licenses and licensed 875 new entities."
- Who needs a licence: "firms that buy or sell over 2,000 pounds of fresh or frozen fruits and vegetables in any given day are required to be licensed."
- "Growers can apply for a PACA license but are not required to have a license, if they only sell products that they have grown."
- I found no count newer than 2020.

**Livestock auction markets** (USDA AMS Packers & Stockyards Division, 2021 & 2022 report; N-E16, V):
- "In FY 2022, there were 271 bonded packers, 90 live poultry dealers, 4,281 registered livestock dealers and market agencies buying on commission, and 1,221 market agencies selling on commission."
- "Livestock auctions, which are market agencies that sell on commission…". So 1,221 is an upper bound on the number of auction businesses (A).
- The count was 1,202–1,236 in every year from 2013 to 2022.

### 3.4 Task 4: Shipper counts and size

**SUSB 2022** (Statistics of US Businesses, Census; N-E17, V; percentages [our calc]):
- SUSB groups firms by enterprise employment. Firm size here is the whole company's employment, not just the establishment's (A: SUSB convention, not re-read).
- SUSB 2022 still uses NAICS 2017 codes, so 454 and 4541 are present (V).
- "Small-firm receipts" is the share of industry receipts earned by firms with fewer than 500 employees.

| NAICS | Industry | Firms | Establishments | <20 | 20–99 | 100–499 | 500+ | % firms <20 | Small-firm receipts |
|---|---|---|---|---|---|---|---|---|---|
| 31-33 | Manufacturing | 239,265 | 285,500 | 177,779 | 44,917 | 12,392 | 4,177 | 74.3 | 23.7% |
| 311 | Food | 25,675 | 30,503 | 19,070 | 4,521 | 1,418 | 666 | 74.3 | 21.7% |
| 312 | Beverage & tobacco | 11,382 | 12,373 | 9,052 | 1,960 | 256 | 114 | 79.5 | 20.8% |
| 321 | Wood products | 11,761 | 13,993 | 8,537 | 2,441 | 571 | 212 | 72.6 | 42.5% |
| 322 | Paper | 2,236 | 3,822 | 969 | 729 | 352 | 186 | 43.3 | 19.6% |
| 325 | Chemicals | 10,455 | 14,601 | 6,496 | 2,200 | 1,050 | 709 | 62.1 | 21.5% |
| 326 | Plastics & rubber | 8,369 | 11,487 | 4,373 | 2,289 | 1,113 | 594 | 52.3 | 32.2% |
| 327 | Nonmetallic mineral products | 8,807 | 14,951 | 6,026 | 1,982 | 536 | 263 | 68.4 | 37.5% |
| 331 | Primary metals | 2,649 | 3,579 | 1,193 | 749 | 419 | 288 | 45.0 | 20.5% |
| 332 | Fabricated metal | 49,484 | 54,040 | 36,413 | 9,978 | 2,282 | 811 | 73.6 | 53.5% |
| 333 | Machinery | 19,028 | 21,759 | 12,301 | 4,556 | 1,427 | 744 | 64.6 | 33.2% |
| 334 | Computer & electronic | 9,698 | 11,285 | 6,215 | 2,198 | 777 | 508 | 64.1 | 22.9% |
| 335 | Electrical equipment | 4,593 | 5,369 | 2,882 | 1,051 | 371 | 289 | 62.7 | 26.8% |
| 336 | Transportation equipment | 9,145 | 11,565 | 5,455 | 2,097 | 994 | 599 | 59.7 | 10.0% |
| 337 | Furniture | 14,044 | 14,606 | 11,421 | 1,966 | 472 | 185 | 81.3 | 50.2% |
| 339 | Miscellaneous mfg | 22,418 | 24,004 | 18,853 | 2,525 | 662 | 378 | 84.1 | 37.7% |
| 212 | Mining (except oil & gas) | 3,523 | 6,057 | 2,501 | 627 | 237 | 158 | 71.0 | 28.1% |
| 42 | Wholesale trade (includes 425 agents/brokers) | 277,932 | 388,706 | 236,359 | 30,583 | 7,687 | 3,303 | 85.0 | 33.5% |
| 423 | Durable-goods wholesalers | 153,128 | 228,785 | 127,376 | 18,861 | 4,728 | 2,163 | 83.2 | 35.5% |
| 424 | Nondurable-goods wholesalers | 91,911 | 123,715 | 76,729 | 10,763 | 3,025 | 1,394 | 83.5 | 28.2% |
| 4244 | Grocery wholesalers | 27,458 | 34,852 | 22,772 | 3,438 | 863 | 385 | 82.9 | 31.4% |
| 424410 | General-line grocery | 2,637 | 3,290 | 2,202 | 274 | 94 | 67 | 83.5 | 12.6% |
| 424420 | Packaged frozen food | 2,495 | 3,116 | 1,956 | 376 | 101 | 62 | 78.4 | 32.1% |
| 424430 | Dairy | 1,352 | 1,800 | 1,037 | 222 | 50 | 43 | 76.7 | 24.7% |
| 424460 | Fish & seafood | 1,868 | 1,964 | 1,575 | 250 | 30 | 13 | 84.3 | 87.8% |
| 424470 | Meat | 1,981 | 2,198 | 1,522 | 350 | 60 | 49 | 76.8 | 41.2% |
| 424480 | Fresh fruit & vegetable | 4,480 | 4,923 | 3,531 | 702 | 196 | 51 | 78.8 | 73.4% |
| 424490 | Other grocery | 10,673 | 14,813 | 9,105 | 1,051 | 308 | 209 | 85.3 | 27.6% |
| 4245 | Farm-product raw materials | 3,399 | 6,212 | 2,639 | 534 | 150 | 76 | 77.6 | 40.4% |
| 424510 | Grain & field bean | 1,839 | 4,481 | 1,300 | 352 | 124 | 63 | 70.7 | 36.2% |
| 424520 | Livestock | 558 | 633 | 475 | 75 | 7 | 0 | 85.1 | 97.1% |
| 454 | Nonstore retailers | 81,750 | 90,991 | 76,229 | 4,069 | 888 | 564 | 93.2 | 27.5% |
| 4541 | Electronic shopping & mail-order | 53,556 | 55,633 | 49,913 | 2,584 | 619 | 440 | 93.2 | 23.6% |
| 4931 | Warehousing & storage | 9,195 | 19,979 | 5,146 | 1,670 | 1,081 | 1,298 | 56.0 | 37.4% |
| 493110 | General warehousing | 6,789 | 15,416 | 3,592 | 1,250 | 849 | 1,098 | 52.9 | 35.6% |
| 493120 | Refrigerated warehousing | 680 | 1,222 | 376 | 176 | 66 | 62 | 55.3 | 41.5% |
| 493130 | Farm-product warehousing | 542 | 774 | 398 | 55 | 46 | 43 | 73.4 | 89.6% |
| 493190 | Other warehousing | 1,399 | 2,567 | 787 | 207 | 159 | 246 | 56.3 | 38.5% |

- SUSB counts 4,480 firms in 424480 and 1,839 in 424510. The Economic Census figures already held are 4,253 and 2,068. The two programs differ in scope.
- A trade-press article counts "approximately 292,825 manufacturing establishments" (citing Vertical IQ; N-E32). That matches SUSB's 285,500 manufacturing establishments.

**Importers and exporters** ("A Profile of U.S. Importing and Exporting Companies, 2023–2024", Tables 1a and 1d; N-E18, V). Census's "SME" (small and medium-sized enterprise) group includes firms with unknown employment.

| Employment size | Exporters | % | Known export value ($B) | % | Importers | % | Known import value ($B) | % |
|---|---|---|---|---|---|---|---|---|
| All identified | 271,250 | 100 | 1,813.0 | 100 | 240,535 | 100 | 2,925.8 | 100 |
| Unknown | 116,428 | 42.9 | 182.9 | 10.1 | 94,200 | 39.2 | 252.3 | 8.6 |
| 1–19 | 91,253 | 33.6 | 92.0 | 5.1 | 92,517 | 38.5 | 160.1 | 5.5 |
| 20–49 | 26,117 | 9.6 | 49.9 | 2.8 | 22,013 | 9.2 | 100.0 | 3.4 |
| 50–99 | 13,582 | 5.0 | 56.2 | 3.1 | 11,526 | 4.8 | 91.9 | 3.1 |
| 100–249 | 11,269 | 4.2 | 121.9 | 6.7 | 9,607 | 4.0 | 141.8 | 4.8 |
| 250–499 | 4,806 | 1.8 | 78.5 | 4.3 | 4,160 | 1.7 | 137.5 | 4.7 |
| 500+ | 7,795 | 2.9 | 1,231.7 | 67.9 | 6,512 | 2.7 | 2,042.2 | 69.8 |

- "Of the 240,535 identified importers in 2024 (a decline of 0.8 percent from 2023), 17.4 percent were manufacturers, 36.5 percent were wholesalers, and 46.1 percent were classified as other."
- "SME importers accounted for 98.7 percent of identified importers within NAICS 423 … and 98.9 percent of 424."
- "In 2024, 60.0 percent of exporters reported exporting to only one country, and accounted for 5.4 percent of the known export value."
- 87,016 companies both imported and exported.
- Among wholesaler importers, 41,241 have 1–19 employees.

### 3.5 Task 5: Technology habits of small and mid-sized shippers

Credible, size-specific US evidence is thin. What was found:
- **TMS adoption by freight spend.** A TMS (transportation management system) is software for planning, buying and tracking shipments.
  - A logistics-provider blog (Intek Logistics, 22 July 2019; N-E20, vendor) cites an unnamed "recent study conducted by Gartner": "there is only a 35% to 40% TMS adoption rate". By freight spend: "Companies Over $100 Million: 50% Adoption of TMS"; "Between $25-$100 Million: 25%"; "Under $25 Million: Roughly 10%".
  - (A) I could not see the Gartner original; its year and method are unknown. Search snippets attribute the same tiers to Gartner through Logistics Management (2015), which returned HTTP 403.
- **Email and spreadsheets.**
  - Bessemer 2021 (held): "50% of the largest enterprise shippers in the U.S. still rely on some combination of email and spreadsheets."
  - A 2025 vendor survey (SHIPSTA by Freightos; N-E21, vendor claim) of "over 70 shippers throughout Europe" found "73% of respondents are not fully digitized, meaning they rely on spreadsheets or fragmented systems to manage freight" (27% highly digitized, 45% somewhat, 28% minimally). The respondents are European, not US.
  - The Flexport quote on fax machines is already held.
- **Electronic ordering (a proxy for EDI).** EDI (electronic data interchange) is the older machine-to-machine standard for documents such as orders and ship notices.
  - Census E-Stats 2022 (N-E19, V): manufacturers' e-shipments were $4,825.9B in 2022 ($4,230.8B in 2021).
  - Merchant wholesale e-commerce sales, including manufacturers' sales branches, were $3,760.2B, with the caveat: "The total quantity response rate (TQRR) for Merchant Wholesale Trade e-commerce sales was 40.4 percent."
  - Census counts orders placed over EDI, internet, extranet or email as e-commerce (A, from the data.gov description).
  - Dividing by SUSB manufacturing receipts of $7,072B gives about 68% e-shipped [our calc, A]. The scopes of the two figures differ, so treat this as rough.
  - **I found no credible survey of EDI adoption among small suppliers.** Vendor pages say large retailers make EDI "the price of entry" for suppliers (A).
- **How shippers buy freight.** See §3.6 (carrier survey, 3PL study).

### 3.6 Task 6: Who arranges transport

**Customer pick-up in the CFS** (V) is the only official measure of freight arranged by the buyer. It is 11.4% of tons and 5.7% of value nationally.
- **By industry:** see §3.1. Highest are mining 21.3% and petroleum wholesalers 18.9%. Lowest are e-commerce and drug wholesalers at 0.9%.
- **By commodity, highest:** gravel 30.6%, natural sands 24.8%, gasoline 13.9%, animal feed 11.1%, machinery 10.6%, other nonmetallic minerals 10.6%, vehicles and parts 10.0%.
- **By commodity, lowest:** coal and metallic ores 0.2%, pharmaceuticals 1.4%, mixed freight 1.8%, logs 2.1%, alcoholic beverages 2.7%, basic chemicals 2.8%, cereal grains 3.5% (N-E05).
- Customer pick-up is 5.8% of temperature-controlled tons and 9.3% of hazmat tons.

**Collect versus prepaid.** "Collect" (or "customer-routed") means the receiver books and pays the carrier. "Prepaid" means the shipper does.
- **I found no economy-wide statistic** on how much inbound freight receivers arrange.
- Vendor snippets (N-E31, A):
  - "Nearly every large retailer mandates FOB Origin, Freight Collect in its vendor routing guide."
  - "Only about 35% of companies use a formal routing guide for inbound freight."
  - Neither is sourced or dated.
- Walmart runs both models (§3.7).

**Buying channels:**
- **Carrier-side survey.** The Freight Source Survey, 2018, of 533 carriers with 12,121 trucks (N-E22, trade press): "approximately 63% of load offerings come via direct interaction between the carrier and shipper, while 23% of the loads came from direct contact with brokers and 14% from the use of an online load board". Small carriers (5–15 trucks) got about 80% directly from shippers.
- **3PL study.** The NTT DATA / Penske / Penn State Third-Party Logistics Study (a 3PL is a third-party logistics provider) is quoted in a snippet: "Sixty-two percent of shippers are outsourcing domestic transportation" (N-E23, A). The edition, 2025 or 2026, and the respondent sizes are unconfirmed, because the PDF is behind a registration form.
- **Intermediaries, for context only.** SUSB 2022 counts 15,852 "freight transportation arrangement" firms (NAICS 488510, brokers and forwarders), 86.8% with fewer than 20 employees (N-E17, V). Other S1 agents cover this side.

### 3.7 Task 7: Receivers as a group

**Warehouses and distribution centres** (SUSB 2022, V):
- Warehousing & storage (4931) has 9,195 firms and 19,979 establishments: general 15,416, refrigerated 1,222, farm-product 774, other 2,567.
- 51.3% of these establishments belong to firms with 500 or more employees [our calc].
- (A) I did not check whether retailer- or manufacturer-owned DCs are counted in 493 or in their parent industry, and I found no credible non-Census DC count.
- As shipping origins in the CFS, 4931 establishments sent 305.7M t worth $1,347.7B in 2022 (V).

**Retailer supplier-compliance programmes.** OTIF means "on time, in full".
- **Walmart, 2017.** "monthly fines against companies that are worth 3% of the value of each late or incomplete shipment" (Grocery Dive, 28 Nov 2017; N-E25).
- **Walmart, 2019.** "require suppliers to deliver full truckloads within a two-day window 87% of the time … Suppliers will be fined 3% of the cost of goods sold if they fail to meet the requirements" (Supply Chain Dive, 8 Mar 2019; N-E24).
- **Walmart, 2024 goals** (SPS Commerce Supplier Wiki, updated 5 Feb 2024, effective 1 Feb 2024; N-E26, vendor):
  - Prepaid: "90% of all cases delivered arrive on time at the distribution center".
  - Collect: "98% of all cases are ready for pick up by the appointment time".
  - "A 95% In-Full goal is applied individually to each Merchandise Alignment."
  - Vendor snippets add that the fine is "3% cost of goods on all cases that did not meet the goal", billed quarterly (N-E29, A).
- **Walmart collect-freight charges.** "The dollar amount of the Pickup charge is a percentage of the COGS determined by the item's department every month" (SPS Commerce, 7 Jun 2022; N-E27, vendor). A snippet puts the charge at 0.49–0.76% of cost of goods and says it was replaced by a fuel-only charge on 1 Feb 2024 (N-E29, A).
- **Walmart consolidation (May 2026).** Walmart launched a "Prepaid Consolidation Program": suppliers ship one national purchase order to one location, and Walmart then spreads the inventory across "42 regional distribution centers". Suppliers pay a per-case rate (Supply Chain Dive, 26 May 2026; N-E28).
- **Kroger, 2017.** "charges suppliers $500 per day for deliveries made past a two-day window" (N-E25).
- **Target and later Kroger figures** (vendor snippets only, N-E30, A): Target's on-time fill-rate programme charges 5% of cost of goods on unfilled items with a $150 minimum (August 2024). Kroger targets 98% on-time and a 95% case fill rate.

---

## 4. Could not access

- **CFS 2022 ton-miles** by industry or commodity are not in the 2022 area-series tables or the API variable list. The 2022 microdata file (PUMS, 677 MB) exists but was not downloaded.
- **Census API queries** for the 2022 CFS returned empty responses, so I used the FTP table files instead.
- **The Gartner TMS-by-size original.** The Gartner blog redirects to a generic page. Logistics Management (2015 State of TMS) and Supply Chain 24/7 returned HTTP 403, and web.archive.org cannot be fetched.
- **The NTT DATA 3PL Study 2025 PDF** is gated behind registration and was not accessed. The Penske blog carried no figures.
- **Other pages that returned HTTP 403:** SDCExec's Loghub spreadsheet study and Fleet Equipment's Descartes 2025 survey. The USDA PACA Fact Finder was also 403 through WebFetch but was read by direct download.
- **The PACA licensee count after 2020** was not found.
- **Livestock auction counts** from the Census of Agriculture or other sources were not found. The Packers & Stockyards register count is used instead.
- **The economy-wide collect versus prepaid share** was not found.
- **EDI adoption among small suppliers:** no credible survey was found.
- **E-Stats 2022 percent-of-total shares:** the visualization shows dollar values only.
- **Walmart's official supplier OTIF documents** sit behind a supplier login. I relied on trade press and vendor pages instead.
- **The formal CFS definition of "customer pick-up"** was not read; only the mode label was.
- **SUSB counts for 324, 4247, 4248 and 4242** are in the downloaded file but were not extracted.
- **Non-Census counts of distribution centres** were not searched in depth.

---

## 5. Sources

Every entry was accessed 2026-09-14.

- **N-E01**: US Census Bureau, 2022 Commodity Flow Survey, table CF2200A01 (mode, with 2017 comparison). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200A01.zip. Table download (national rows). Primary.
- **N-E02**: Census, 2022 CFS table CF2200A18 (industry × mode × distance). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200A18.zip. Table download. Primary.
- **N-E03**: Census, 2022 CFS table CF2200A04 (industry totals, average miles). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200A04.zip. Table download. Primary.
- **N-E04**: Census, 2022 CFS table CF2200A05 (commodity totals, average miles). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200A05.zip. Table download. Primary.
- **N-E05**: Census, 2022 CFS table CF2200A09 (commodity × mode × distance). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200A09.zip. Table download. Primary.
- **N-E06**: Census, 2022 CFS Temperature Control Series tables CF2200TC01, TC04 and TC05 (mode, industry, commodity). https://www2.census.gov/programs-surveys/cfs/data/2022/ (the TC zips). Table download. Primary.
- **N-E07**: Census, 2022 CFS Hazardous Materials Series table CF2200H01 (mode). https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200H01.zip. Table download. Primary.
- **N-E08**: Census, API dataset catalog and 2022 CFS variable lists (https://api.census.gov/data/2022.json; https://api.census.gov/data/2022/cfsarea/variables.json), plus the 2022 CFS PUMS directory and data dictionary (https://www2.census.gov/programs-surveys/cfs/datasets/2022/; the zip is dated 29 Jan 2026). Partial: variable lists and mode codes. Primary.
- **N-E09**: BTS/FHWA/ORNL, Freight Analysis Framework FAF5.7.1, 2018–2024 data and FAF5_metadata.xlsx (files dated 2025-08-07). https://faf.ornl.gov/faf5/Data/Download_Files/FAF5.7.1_2018-2024.zip. Full data download, aggregated. Primary.
- **N-E10**: USDA AMS, "Transportation of U.S. Grains: A Modal Share Analysis, 1984–2022 Update", September 2024. https://www.ams.usda.gov/sites/default/files/media/TransportationofUSGrainsModalShare1984_2022.pdf. Partial: method and Tables 1–5. Primary.
- **N-E11**: USDA NASS, 2022 Census of Agriculture, Vol. 1 Ch. 1 US, Table 48 (farms by NAICS); published 2024 (A). https://www.nass.usda.gov/Publications/AgCensus/2022/Full_Report/Volume_1,_Chapter_1_US/st99_1_048_048.pdf. Full table. Primary.
- **N-E12**: USDA NASS, 2022 Census of Agriculture, Table 72 (summary by market value sold). https://www.nass.usda.gov/Publications/AgCensus/2022/Full_Report/Volume_1,_Chapter_1_US/st99_1_072_072.pdf. Partial: first page. Primary.
- **N-E13**: USDA NASS, "Grain Stocks", released 10 January 2025. https://esmis.nal.usda.gov/sites/default/release-files/xg94hp534/5d86qt759/xp68nc84m/grst0125.pdf. Partial: storage capacity and facilities section. Primary.
- **N-E14**: USDA AMS, "Perishable Agricultural Commodities Act (PACA)" presentation to FVIAC ("PACA Highlights – 2020"; presentation date not captured). https://www.ams.usda.gov/sites/default/files/media/FVIAC_PACA_Presentation.pdf. Full. Primary.
- **N-E15**: USDA AMS, "PACA Fact Finder" brochure (date not captured). https://www.ams.usda.gov/sites/default/files/media/PACAFactFinderBrochure.pdf. Partial: licensing questions and answers. Primary.
- **N-E16**: USDA AMS, "Packers and Stockyards Division: Annual Report 2021 & 2022" (report to Congress; published 2024, A). https://www.ams.usda.gov/sites/default/files/media/PackersandStockyards2021_2022ReporttoCongress.pdf. Partial: Table 1 and overview. Primary.
- **N-E17**: Census, Statistics of US Businesses 2022, us_state_6digitnaics_2022.txt. https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_6digitnaics_2022.txt. Table download (US rows). Primary.
- **N-E18**: Census, "A Profile of U.S. Importing and Exporting Companies, 2023–2024" (release date not captured). https://www.census.gov/foreign-trade/Press-Release/edb/edbrel2024.pdf. Partial: text pages 1–8 and Tables 1, 1a, 1d, 1g. Primary.
- **N-E19**: Census, "E-Commerce Activity Across Sectors: 2021 and 2022" (E-Stats 2022 visualization, 2025) and the E-Stats 2022 landing page (26 March 2025). https://www2.census.gov/library/visualizations/2025/econ/e-commerce-activity-across-sectors-2021-2022.pdf and https://www.census.gov/library/publications/2025/econ/2022-e-stats.html. Full graphic; the landing page had no figures. Primary.
- **N-E20**: Intek Logistics, "TMS Market Size & Growth Expectations", 22 July 2019 (cites a Gartner study). https://www.inteklogistics.com/blog/tms-market-size-and-growth-expectations. Page read through a fetch summary. Vendor (secondary for the Gartner figures).
- **N-E21**: Freightos, "73% of Freight Procurement Teams Still Rely on Manual Processes…", 4 February 2025. https://www.freightos.com/freight-resources/cost-of-freight-procurement-teams-relying-on-manual-processes/. Partial. Vendor.
- **N-E22**: FreightWaves (Zach Strickland), "Carriers still getting majority of loads directly from shippers, while digital apps are a non-factor", 3 April 2018. https://www.freightwaves.com/news/carriers-still-getting-majority-of-loads-directly-from-shippers-while-digital-apps-are-a-non-factor. Partial. Trade press, reporting a survey.
- **N-E23**: NTT DATA / Penske / Penn State, Annual Third-Party Logistics Study, 2025 and 2026 editions. https://us.nttdata.com/en/engage/2025-third-party-logistics-study; Penske blog of 1 October 2024 at https://www.gopenske.com/blog/the-2025-3pl-study-shippers-3pls-navigate-change-within-an-evolving-supply-chain/. Search snippet only (the blog was read but had no figures). Vendor-sponsored.
- **N-E24**: Supply Chain Dive (Matt Leonard), "Walmart tightens on-time, in-full rate for suppliers to 87%", 8 March 2019. https://www.supplychaindive.com/news/walmart-on-time-in-full-87-suppliers/550083/. Partial. Trade press.
- **N-E25**: Grocery Dive (Jeff Wells), "Walmart and Kroger fine suppliers for late or incomplete deliveries", 28 November 2017. https://www.grocerydive.com/news/grocery--walmart-and-kroger-fine-suppliers-for-late-or-incomplete-deliveries/534461/. Partial. Trade press.
- **N-E26**: SPS Commerce / SupplyPike Supplier Wiki (Ryan Petty), "Walmart's OTIF Performance Metrics", updated 5 February 2024. https://www.spscommerce.com/community/articles/walmart-otif-metrics. Partial. Vendor.
- **N-E27**: SPS Commerce / SupplyPike, "New Fees with Walmart's Collect Pickup Program", 7 June 2022. https://www.spscommerce.com/community/articles/walmart-collect-pickup-program. Partial. Vendor.
- **N-E28**: Supply Chain Dive (Max Garland), "Walmart rolling out simplified inbound logistics for suppliers", 26 May 2026. https://www.supplychaindive.com/news/walmart-rolling-out-simplified-inbound-logistics-for-suppliers/821111/. Partial. Trade press.
- **N-E29**: Search-result snippets on Walmart OTIF fine mechanics and collect or fuel charges, from 8th & Walton (https://www.8thandwalton.com/blog/walmart-otif), getproductiv.com (https://getproductiv.com/walmart-otif-routing-guide-compliance) and SPS Commerce ("Walmart's New Fuel Management Program", https://www.spscommerce.com/community/articles/walmarts-new-fuel-management-program). Dates vary. Search snippet. Vendor.
- **N-E30**: Search-result snippets on Target's on-time fill-rate and Perfect Order programmes and on Kroger thresholds (getproductiv.com, https://getproductiv.com/otif-compliance-guide, and similar). Search snippet. Vendor.
- **N-E31**: Search-result snippets on inbound routing guides and collect terms (freehand.ai, https://www.freehand.ai/articles/inbound-freight-management; and others). Search snippet. Vendor.
- **N-E32**: FreightWaves (Adam Wingfield), "There Are 292,000 Shippers in America and 9 out of 10 Carriers Have 10 Trucks or Less…", 17 March 2026. https://www.freightwaves.com/news/there-are-292000-shippers-in-america-and-97-of-carriers-have-10-trucks-or-less-the-match-has-been-right-in-front-of-you-the-whole-time. Partial. Trade press (secondary, citing Vertical IQ).

Also cited and already held: R31 (FAF5.7.1), R32 (CFS 2022 press release), R34 (USDA AgRTQ Q1 2026), R39 (ERS Food Dollar), Bessemer 2021, the Flexport quote, and the Economic Census 2022 concentration figures for 424480, 424510, 3116 and 3114.
