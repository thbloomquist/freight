# S2 check J: downturn falls for farm, industrial and consumer units; BLS projections; substitutes (K11 Tests 1 and 3)

- **What this is:** evidence for knock-out K11 ("durable") at S2 of run 01, covering Tests 1 and 3 for the units listed as J1-J17 (cards C-15, C-16, C-24 to C-40), plus BLS 10-year projections and substitutes for all 40 cards (C-01 to C-40).
  - Test 1 is "no projected shrinking". Here that means the BLS projections (Part 2) and substitutes (Part 3). Census firm counts are handled by the coordinator.
  - Test 3 is "no drastic fall in the unit a fee would be counted on" (Part 1).
- **Date:** 2026-09-15.
- **Status:** input to S2; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/2_knockouts.md`.
- **Labels:**
  - *verified* means read at the source: a quote from the page, or a value from a downloaded official file or official table.
  - *assumed* means a search snippet, secondary summary, vendor claim, memory, or a page that was blocked.
  - **[our calc]** marks our own arithmetic. Every percentage change in Part 1 and every output % in Part 2 is **[our calc]** unless the source printed it.
- **Terms used below:**
  - *Peak-to-trough*: the percentage change from the highest value in the peak window to the lowest later value in the trough window.
    - 2008-09 downturn: peak in 2005-2008, trough in 2009-2011.
    - 2022-25 downturn: peak in 2021-2022, trough in 2023-2025.
  - *Bands*, matching K11 Test 3 in `0_criteria.md`:
    - "≤13%" (fell 13% or less);
    - "13-20%";
    - ">20%";
    - "rose" (no later value below the peak);
    - "no data".
  - *NSA / SA*: not seasonally adjusted / seasonally adjusted.
  - *12-month rolling*: the sum or average of the latest 12 months. We use it on monthly NSA series so that seasons do not create false troughs.
  - *Marketing year (MY)*: USDA's crop year. For example, MY2007 is the 2007 crop, sold in 2007/08.
  - *STCC*: the Standard Transportation Commodity Code railroads use.
  - *Expanded carloads*: sampled carloads multiplied by the STB's expansion factor, which estimates all carloads.
  - *Chained dollars*: inflation-adjusted (real) dollars.
  - *PPI*: Producer Price Index.
- **Method:** physical counts or tons were preferred. Where only dollars exist, we deflated them by the closest PPI **[our calc]** and say so. Annual data is used unless a monthly series is named.

---

## 0. Quick read for the coordinator (not a decision)

| Band pattern | Units (series) |
|---|---|
| ≤13% or rose in **both** windows | J1 produce truck shipments (national, Nogales, Pharr); J3 grain production; J4 grain by rail; J5 rail chemicals; J7 milk; J13 gasoline + distillate combined; J17 grocery, beer and wine, drug wholesale (real) |
| 13-20% in at least one window, and never >20% | J2 bulk farm exports (2008-09: -19.7%); J5 total rail carloads (2008-09: -19.9%, just under the line); J5 plastics by rail (2008-09); J6 cattle slaughter (2022-25: -13.8%); J13 distillate alone (2008-09); J10 all chemicals index G325 (2008-09: -18.4%) |
| >20% in at least one window | J4 barge grain (2022-25: -28.4%); J5 pulp and paper, and scrap, by rail (2008-09); J8 cut flowers by weight (2008-09: -25.0%; by value -8.0%); J10 basic chemicals and resins (2008-09); J11 aggregates (2008-09: -36.9%); J12 wood products and logs (2008-09); J13 residential heating oil (2008-09); J14 new light vehicles (2008-09: -38.6%); J15 interstate and cross-county movers, existing-home sales (2008-09); J16 housing starts, building-material dealers, lumber wholesale (2008-09); J17 hardware and plumbing wholesale (2008-09) |
| no data | J9 oversize/overweight permits in 2008-09; J14 used vehicles at auction; J15 van-line shipments |

Where two series for one unit disagree, both are shown. The choice between them is the coordinator's.

---

## 1. Part 1: downturn data, J1-J17

### 1.1 Summary table

| Unit | Cards | Series used | Direct or proxy | 2008-09 peak → trough | 2022-25 peak → trough | Band (08-09 / 22-25) | Label | Sources |
|---|---|---|---|---|---|---|---|---|
| J1a Produce truck shipments, all origins | C-26, C-27 | USDA AMS Market News movement, truck and truck-import modes, annual sum (10,000-lb units) | direct | 2008 5,786,114 → no lower year in 2009-11 (2009: 5,946,343, +2.8%) | 2021 7,818,109 → 2025 6,938,560, **-11.3%** | rose / ≤13% | *verified* | N-J06 |
| J1b Nogales produce crossings | C-27 | same, district "Mexico Crossings Through Nogales Arizona" | direct | 2008 440,829 → 2009 429,806, **-2.5%** | 2021 618,946 → 2025 570,314, **-7.9%** | ≤13% / ≤13% | *verified* | N-J06 |
| J1c Pharr produce crossings | C-27 | same, "…Pharr Texas" (exists from late 2011). For 2008-09, "…Through Texas" (all Texas ports) | direct (22-25); proxy (08-09) | 2008 422,564 → 2009 495,122, rose | 2022 788,982 → 2024 833,407, rose | rose / rose | *verified* | N-J06 |
| J1d All trucks at the border ports | C-27 | BTS incoming trucks, all cargo: Nogales; Hidalgo (which includes the Pharr bridge, *assumed*) | proxy | Nogales 2008 303,757 → 2009 276,877, **-8.8%**; Hidalgo 2005 491,077 → 2009 419,426, **-14.6%** | Nogales 2021 379,106 → 2023 381,969, rose; Hidalgo 2021 687,659 → 2023 708,726, rose | ≤13% (Nogales), 13-20% (Hidalgo) / rose | *verified* | N-J11 |
| J2 Farm and food export tons | C-24 | USDA PSD US exports, MY: corn, wheat, sorghum, barley, milled rice, soybeans, soybean meal, soybean oil (1,000 t) | proxy (bulk only) | MY2007 148,786 → MY2011 119,401, **-19.7%** | MY2021 166,460 → MY2023 146,880, **-11.8%** | 13-20% / ≤13% | *verified* | N-J05 |
| J3 Grain to country elevators | C-28 | USDA PSD production, corn + wheat + soybeans (1,000 t, MY) | proxy | 2007 459,857 → 2011 451,324, **-1.9%** | 2021 547,777 → 2024 551,166, rose (+0.6%) | ≤13% / rose | *verified* | N-J05 |
| J4a Grain by rail (sample) | C-29 | STB Carload Waybill Sample, grain (STCC 0113), expanded carloads | direct | 2007 1,554,070 → 2009 1,412,811, **-9.1%** | 2022 1,347,682 → 2023 1,304,710, **-3.2%** (2024: 1,368,383; 2025 not yet released) | ≤13% / ≤13% | *verified* | N-J09 |
| J4b Grain by rail (weekly) | C-29 | STB weekly service metrics: grain carloads originated by the Class I railroads | direct | not covered (starts 2017) | 2021 1,347,129 → 2023 1,178,500, **-12.5%** | — / ≤13% | *verified* | N-J08 |
| J4c Grain by barge | C-29 | USACE downbound grain, short tons, at Mississippi Locks 27, Ohio Olmsted and Arkansas Lock 1 | direct | 2006 37,332,337 → 2011 30,356,013, **-18.7%** | 2021 36,741,011 → 2023 26,294,289, **-28.4%** | 13-20% / >20% | *verified* | N-J07 |
| J5a Rail carloads, total excl. intermodal | C-30 | AAR carloads via BTS, monthly, summed by year (12-month rolling in brackets) | direct | 2006 16.81M → 2009 13.47M, **-19.9%** [Dec 2006 → Feb 2010: -20.0%] | 2021 11.63M → 2024 11.39M, **-2.1%** [Mar 2022 → Feb 2025: -3.3%] | 13-20% (borderline) / ≤13% | *verified* | N-J10; cross-checks N-J24, N-J25 |
| J5b Chemicals by rail | C-30 | Waybill sample STCC 28; weekly "Chemicals" | direct | 2007 2,500,646 → 2009 2,281,828, **-8.8%** | sample 2021 3,257,403 → 2023 3,217,493, **-1.2%**; weekly 2022 1,850,979 → 2023 1,848,385, -0.1% | ≤13% / ≤13% | *verified* | N-J09, N-J08 |
| J5c Plastics by rail | C-30 | Waybill sample STCC 2821 (plastic materials) | direct | 2007 631,870 → 2009 527,924, **-16.5%** | 2022 852,200 → 2023 858,150, rose | 13-20% / rose | *verified* | N-J09 |
| J5d Grain by rail | C-30 | as J4a and J4b | direct | -9.1% | -3.2% / -12.5% | ≤13% / ≤13% | *verified* | N-J09, N-J08 |
| J5e Pulp and paper by rail | C-30 | Waybill sample STCC 26; weekly "Pulp, Paper and Allied Products" | direct | 2006 921,644 → 2009 721,720, **-21.7%** | sample 2021 795,195 → 2023 686,964, **-13.6%**; weekly 2021 322,050 → 2023 295,451, **-8.3%** | >20% / 13-20% or ≤13% (the sources disagree) | *verified* | N-J09, N-J08 |
| J5f Scrap by rail | C-30 | Waybill sample STCC 40 (waste and scrap); weekly "Waste and Scrap" and "Iron and Steel Scrap" | direct | 2007 811,020 → 2009 630,293, **-22.3%** | sample 2022 711,239 → 2024 728,211, rose; weekly waste 2022 → 2023 -1.3%; iron and steel scrap rose | >20% / ≤13% | *verified* | N-J09, N-J08 |
| J6 Cattle moved | C-31 | USDA PSD total cattle slaughter, calendar year (1,000 head) | proxy (slaughter only) | 2008 35,508 → 2009 34,468, **-2.9%** | 2022 34,812 → 2025 30,022, **-13.8%** | ≤13% / 13-20% | *verified* | N-J05 |
| J7 Milk production | C-32 | USDA PSD "Milk, Fluid" production (1,000 t) | direct (tonnes, not pounds) | 2008 86,173 → 2009 85,821, **-0.4%** | 2022 102,701 → 2024 102,452, **-0.2%** | ≤13% / ≤13% | *verified* | N-J05 |
| J8 Cut-flower imports | C-33 | UN Comtrade, US imports of HS 0603, net weight and value (all ports) | direct | weight 2006 162.6M kg → 2009 121.9M kg, **-25.0%** (no 2007 weight); value 2007 $1,043.6M → 2009 $960.4M, **-8.0%** (nominal) | weight 2022 325.8M kg → 2025 313.5M kg, **-3.8%**; value rose | weight >20%, value ≤13% / ≤13% | *verified* | N-J12 |
| J9 Oversize/overweight permits | C-34 | WSDOT permits issued (one state) | direct, one state | no data | 2022 ≈175,220 **[our calc]** → 2023 183,502, rose (2024-25 not published) | no data / rose (partial) | *verified* (2023); 2022 **[our calc]** | N-J23 |
| J10 Tank-truck chemical loads | C-35 | Federal Reserve industrial production (SA monthly): chemicals G325; basic chemicals G3251; resins and synthetic rubber G3252 | proxy | G325 Sep 2007 126.9 → Mar 2009 103.5, **-18.4%**; G3251 Dec 2007 127.5 → Mar 2009 81.9, **-35.8%**; G3252 Nov 2007 119.6 → Mar 2009 80.6, **-32.6%** | G325 Jun 2021 103.2 → Jan 2023 95.4, **-7.5%**; G3251 Jun 2021 100.6 → Jan 2023 90.9, **-9.6%**; G3252 May 2022 98.6 → May 2023 90.4, **-8.2%** | G325 13-20%, G3251 and G3252 >20% / ≤13% | *verified* | N-J13 |
| J11 Aggregates production | C-36 | USGS crushed stone + construction sand and gravel (million t) | direct | 2006 3,100 → 2010 1,955, **-36.9%** (stone -34.8%, sand and gravel -39.8%) | 2022 2,499 → 2025e 2,370, **-5.2%** (stone -2.6%, sand and gravel -9.3%) | >20% / ≤13% | *verified* | N-J14, N-J15, N-J16 |
| J12 Logs to mills | C-37 | Federal Reserve industrial production, wood products (G321, SA monthly); rail lumber and wood (STCC 24) | proxy | G321 Nov 2005 133.7 → May 2009 73.5, **-45.1%**; rail 2005 969,090 → 2009 436,336, **-55.0%** | G321 Mar 2022 105.8 → Dec 2025 94.6, **-10.6%**; rail 2022 558,594 → 2023 522,042, **-6.5%** | >20% / ≤13% | *verified* | N-J13, N-J09 |
| J13 Refined fuel delivered | C-38 | EIA product supplied (kb/d): finished motor gasoline, distillate, and the two combined; EIA residential distillate (heating oil) sales | direct, national | combined 2007 13,482 → 2009 12,627, **-6.3%**; gasoline Sep 2007 → Dec 2011, **-5.8%** (12-mo); distillate Sep 2007 → Feb 2010, **-14.7%** (12-mo); heating oil 2005 5.57bn gal → 2011 3.71bn gal, **-33.3%** | combined 2022 12,838 → 2024 12,757, **-0.6%**; gasoline Mar 2022 → Jan 2023, **-1.3%** (12-mo); distillate Oct 2022 → Nov 2024, **-6.6%** (12-mo); heating oil no data after 2020 | combined ≤13%, distillate 13-20%, heating oil >20% / ≤13% (heating oil no data) | *verified* | N-J02, N-J03 |
| J14 Vehicles moved | C-39 | BEA light-vehicle retail sales, NSA (thousand units) | proxy (new vehicles only) | 2005 16,948 → 2009 10,402, **-38.6%** | 2021 14,947 → 2023 15,502, rose | >20% / rose | *verified* | N-J17 |
| J15 Household moves | C-40 | Census CPS movers aged 1+, by survey year: all, different-county, different-state. NAR existing-home sales | proxy | all movers 2005 39,888k → 2011 35,038k, **-12.2%**; different county **-31.0%**; different state 2005 7,441k → 2010 4,323k, **-41.9%**; NAR 2005 7.08M → 2010 4.19M, **-40.8%** (*assumed*) | all movers 2022 28,179k → 2023 25,624k, **-9.1%**; different state 2022 4,884k → 2023 4,493k, **-8.0%** (CPS table ends 2023); NAR 2022 5.03M → 2024-25 4.06M, **-19.3%** (*assumed*) | all movers ≤13%, interstate >20% / ≤13% (CPS), 13-20% (NAR) | *verified* (CPS); *assumed* (NAR) | N-J18, N-J26, N-J27 |
| J16 Job-site building-material deliveries | C-16 | Housing starts (NSA, thousands); building-material dealers (NAICS 4441) sales, real; lumber and construction-materials wholesale (4233) sales, real | proxy | starts 2005 2,068.1 → 2009 553.9, **-73.2%**; 4441 real 2005 → 2011, **-31.6%**; 4233 real 2005 → 2011, **-46.5%** | starts 2021 1,601.1 → 2025 1,355.7, **-15.3%**; 4441 real 2021 → 2025, **-10.1%**; 4233 real 2022 → 2025, **-14.8%** | >20% / 13-20% (starts, 4233), ≤13% (4441) | *verified* data; real values **[our calc]** | N-J19, N-J20, N-J21, N-J22 |
| J17 Distributors' own-fleet deliveries | C-15 | Census monthly wholesale sales (NSA, summed by year), deflated by PPI **[our calc]**: grocery 4244, beer and wine 4248, drugs 4242, hardware and plumbing 4237 | proxy (dollars, deflated) | grocery 2007 → 2011, **-6.0%**; beer and wine 2008 → 2009, **-4.0%**; drugs 2008 → 2009, **-1.9%**; hardware 2006 → 2009, **-26.8%** | grocery 2021 → 2023, **-1.8%**; beer and wine 2021 → 2025, **-10.2%**; drugs rose; hardware 2021 → 2023, **-4.7%** | grocery, beer and wine, drugs ≤13% / ≤13%; hardware >20% / ≤13% | *verified* data; real values **[our calc]** | N-J21, N-J22 |

### 1.2 Notes per unit

**J1, fresh produce (C-26, C-27).**
- **The series.** USDA AgTransport describes it as "USDA/AMS/Market News/Specialty Crops Program movement data, including only truck and import modes at domestic origins". The unit is "Volume in 10,000 lbs units" (N-J06, *verified*). This is the Market News movement series the brief asked for, so we did not need the annual AMS shipment PDFs (they returned 404/403).
- **Coverage drifts.** The number of reporting origin districts changes over time: 112 in 2007, 124 in 2009, 119 in 2021, 130 in 2025. Data before 2011 is weekly and daily after.
- **The 2025 fall.** The national 2025 low matches R34's Q1 2026 statement (held): Q1 2026 was "down 10 percent from first quarter 2025".
- **The border.** All Mexico-crossing produce rose through 2008-09: 2008 1,085,085 → 2009 1,174,749. It was flat through 2022-25: 2021 2,414,098 → 2025 2,383,341, **-1.3%**.
- **Pharr before 2012.** Pharr has its own district only from late 2011 (2011 holds 48,474, a part-year). For 2008-09, the "Mexico Crossings Through Texas" district is the proxy.
- **BTS truck counts** (N-J11) cover all cargo, not produce.

**J2, farm and food export tons (C-24).**
- The unit is bulk only, by marketing year. The MY2011 low is the 2011 crop year, just before the 2012 drought (MY2012 was 98,826, outside the window).
- Containerised and consumer-oriented farm export tons: **not checked**. USDA FAS GATS needs an interactive query, and PIERS is paid.
- For scale: the MY2021 → MY2022 drop (-18.9% **[our calc]**) happens inside the peak window, so the window rule does not count it.

**J3, grain to elevators (C-28).**
- Metric tons from PSD; not converted to bushels.
- The 2022 drought low (507,858; -7.3% vs 2021 **[our calc]**) also sits inside the peak window.

**J4, grain by rail and barge (C-29).**
- **Rail.** The two rail series agree on direction. The weekly series (N-J08) is the STB's Class I service metrics, per its description: "Each week, the seven Class I railroads submit originated and received carloads by 23 major commodity groups".
- **Barge: which locks.** We summed only the three locks reported since 2003 (Mississippi Locks 27, Ohio Olmsted, Arkansas Lock 1). USDA added four more locks from 2013, and those would double-count the same grain **[our choice]**.
- **Barge: what drives it.** Barge grain swings with river levels and export demand. 2008, at 28.3M t, sits inside the peak window. Low water on the Mississippi in 2022-23 is the likely cause of the 2023 low (*assumed*, not checked).

**J5, rail carloads excluding intermodal (C-30).**
- **Total carloads.** The BTS series (N-J10) is labelled "Freight Rail Carloads" from AAR data.
  - Cross-check against AAR's own words: 2009 carloads were "down 16.1 percent compared with 2008, and down 18.2 percent when compared with 2007" (N-J25, secondary, *assumed*). BTS gives -16.4% and -18.1% **[our calc]**, which matches.
  - AAR's 2023 total, "11,701,875 carloads, up 0.7 percent" (N-J24, *verified*), matches BTS's 11,709k.
  - The 2008-09 fall of -19.9% (annual) and -20.0% (12-month rolling) sits right on the 20% line.
- **Commodities.** AAR's 2008-10 commodity figures are in its paid Rail Time Indicators reports, so the STB Waybill Sample (N-J09) was used instead.
  - The sample's record count roughly tripled from data year 2021, but the expanded totals stay continuous (2020: 32.7M; 2021: 34.4M).
  - The sample's STCC groups are not identical to AAR's weekly categories.
- **Pulp and paper, 2022-25.** The sample (-13.6%) and the weekly series (-8.3%) fall in different bands.

**J6, cattle (C-31).**
- **What drives it.** The 2022-25 fall follows the cattle herd cycle, not freight demand. PSD's calf crop ("Production") fell from 35,131k (2021) to 32,896k (2025) (N-J05, *verified*).
- **Outlook.** PSD's 2026 slaughter forecast is 29,082k, 16.5% below 2022 **[our calc]** (a forecast, outside the window).
- **Not checked:** fed-cattle marketings and auction receipts (NASS QuickStats needs a key; AMS auction reports not queried).

**J7, milk (C-32).** Steady in both windows.

**J8, cut flowers (C-33).**
- **Weight against value.** Comtrade has no 2007 net weight. Using the highest known year (2006) gives the 2008-09 weight fall of -25.0%. Value fell only 8.0% in nominal dollars.
- **Data quality.** The weights come from US trade records via the UN, and weights in trade data can be estimated (*assumed*).
- **Not found:** stem counts.
- **Miami's share** was not re-checked. The project holds about 88% (N-G68).

**J9, oversize and overweight permits (C-34).**
- **What WSDOT gives** (N-J23, *verified*): 2019, 186,859 permits; 2023, 183,502 (85% self-issued). For 2020 and 2022 it gives only self-issued counts (144,256 at 84%; 147,185 at 84%). The implied totals, ≈171,733 and ≈175,220, are **[our calc]** and approximate.
- **Not found:** any state series covering 2007-2010. We tried two searches (TxDMV, WSDOT and PennDOT annual counts) and found nothing.

**J10, tank-truck chemicals (C-35).**
- The brief's proxy is G325, but it includes pharmaceuticals (G3254), which rarely move in tank trucks (*assumed*).
- Basic chemicals (G3251) and resins (G3252) are closer to tank freight, and both fell more than 20% in 2008-09.
- Chemicals by rail fell only 8.8% (J5b).
- The ACC output series was not fetched.

**J11, aggregates (C-36).**
- **Which edition.** The 2005-2007 peak comes from the MCS 2010 edition, and the 2008-2011 values from the revised MCS 2013 edition. MCS 2013 revised 2009 crushed stone to 1,160 (the 2010 edition's estimate was 1,110).
- **Latest years.** MCS 2026 gives 2024 and 2025 as estimates. USGS says construction sand and gravel "was about 870 million tons in 2025 compared with 880 million tons in 2024" (N-J16, *verified*).

**J12, logs (C-37).**
- **Not found:**
  - a sawmill-only industrial production series (G3211 is not in the Fed's file; FRED IDs IPG3211S and IPG32111S failed);
  - softwood lumber production (WWPA reports are paid; one snippet gives only 2021, 37.3 billion board feet, *assumed*, not used);
  - roundwood harvest.
- Both proxies agree: a very deep 2008-09 fall and a mild 2022-25 one.

**J13, fuel (C-38).**
- Distillate fell 13.5% on annual data (2007 4,198 → 2009 3,632 kb/d).
- The residential heating-oil series in EIA's file ends in 2020. Its fall mixes weather with a long switch away from oil heat (*assumed*).
- The combined gasoline plus distillate series is the broadest measure of gallons a fuel marketer delivers.
- For the projection, see the EIA line in Part 2.

**J14, vehicles (C-39).**
- 2022 (13,754k) sits inside the peak window. 2021 → 2022 was -8.0% **[our calc]**.
- **Not found:** used vehicles sold at wholesale auction. We ran two searches of Cox Automotive/Manheim pages: they publish price indexes, not a public volume series. The fact-sheet snippets are *assumed* and not used.

**J15, household moves (C-40).**
- **The CPS table.** Each CPS "survey year" counts people who moved in the previous 12 months. Table A-1 ends at survey year 2023.
- **Interstate movers.** The 2005 row carries a footnote, and different-state movers fell from 7,441k (2005) to 5,679k (2006) before the recession. Measured from 2006 instead, the fall is still **-23.9%** **[our calc]**.
- **NAR figures are all *assumed*:**
  - 2022 5.03M and 2023 4.09M ("an 18.7% decline", an AP article on NAR's site, N-J26);
  - 2024 and 2025 4.06M; 2005 7.08M; the 2010 benchmark of 4.19M (N-J27, snippets).
  - 2021 at 6.12M is from memory; if it is used, 2022-25 becomes **-33.7%** **[our calc]**.
  - NAR's own pages gave no annual history file.
- **Not found:** van-line or interstate household-goods shipment counts. One search found only GAO-10-38's "approximately 800,000 interstate household goods moves annually" (snippet, *assumed*, no time series).

**J16, building materials (C-16).**
- **Which retail row.** We used NAICS 4441 (building material and supplies dealers). It is the finer and more relevant row than 444, which adds garden stores.
- **Deflation.** Real values are 2017 dollars, deflated by the PPI for construction materials (WPUSI012011) **[our calc]**.
  - 4441 real (2017 $ million): 2005 372,255 → 2011 254,451; 2021 303,310 → 2025 272,769.
  - 4233 real: 2005 181,741 → 2011 97,319; 2022 163,811 → 2025 139,516.
- **Nominal changes:**
  - 4441: 2006 $297,554M → 2010 $224,005M, -24.7%; 2022 $442,749M → 2025 $415,857M, -6.1%;
  - 4233: 2006 → 2009, -39.1%; 2022 → 2024, -15.9%.

**J17, distributors' own fleets (C-15).**
- **Deflators** (annual averages, rebased to 2017 **[our calc]**):
  - grocery: PPI finished consumer foods (WPUFD4111);
  - beer and wine: alcoholic beverages (WPU0261);
  - drugs: drugs and pharmaceuticals (WPU063);
  - hardware and plumbing: the simple average of hardware, plumbing fixtures and heating equipment (WPU104, WPU105, WPU106).
- **Real values** (2017 $ million):
  - grocery 2007 590,316 → 2011 554,795; 2021 691,428 → 2023 679,008;
  - beer and wine 2008 128,768 → 2009 123,677; 2021 181,441 → 2025 162,905;
  - drugs 2008 615,642 → 2009 604,070; 2022 794,949 → 2023 867,686;
  - hardware 2006 140,840 → 2009 103,074; 2021 175,307 → 2023 167,057.
- **Nominal:** hardware fell 19.4% (2007 → 2009); grocery fell 2.6% (2008 → 2009).
- The deflator choices are rough, so treat the bands near a line as soft.

---

## 2. Part 2: BLS 10-year projections (Test 1)

**The table** is BLS Employment Projections Table 2.11, "Employment and output by industry, 2025 and projected 2035" (N-J01), read via page extraction.
- **Units.** Employment is in thousands. "Output units: Billions of chained 2017 dollars", so output is real.
- **What BLS prints.** It prints the employment % change, but for output it prints only the compound annual rate. The output % change below is **[our calc]** from the 2025 and 2035 levels; the annual rate is in brackets.
- **"n/p"** means BLS does not publish output for that row.
- **Cross-check.** The figures for truck (484) at +2.1%, 488 at +4.6% and 493 at +2.0% match check C (N-C11).

| Industry | BLS row used (code) | Employment % 2025-35 | Output % 2025-35 **[our calc]** (annual rate) | Label | Source |
|---|---|---|---|---|---|
| Crop production | Crop production (111000) | +3.0 | +10.4 (1.0) | *verified* | N-J01 |
| Animal production | Animal production and aquaculture (112000) | -1.0 | +14.1 (1.3) | *verified* | N-J01 |
| Forestry and logging | Forestry and logging (113000) | -6.8 | n/p | *verified* | N-J01 |
| — forestry | Forestry (1131-2) | -2.0 | +19.5 (1.8) | *verified* | N-J01 |
| — logging | Logging (113300) | -8.3 | +19.4 (1.8) | *verified* | N-J01 |
| Nonmetallic minerals (sand, gravel, stone not split out) | Nonmetallic mineral mining and quarrying (212300) | +6.1 | +15.8 (1.5) | *verified* | N-J01 |
| Food manufacturing | Food manufacturing (311000) | +4.7 | +21.1 (1.9) | *verified* | N-J01 |
| — meat | Animal slaughtering and processing (311600) | +6.1 | +22.7 (2.1) | *verified* | N-J01 |
| — dairy | Dairy product manufacturing (311500) | +5.6 | +29.2 (2.6) | *verified* | N-J01 |
| — grain milling | Grain and oilseed milling (311200) | +1.6 | +12.1 (1.2) | *verified* | N-J01 |
| — fruit and vegetables | Fruit and vegetable preserving and specialty food (311400) | +1.1 | +12.6 (1.2) | *verified* | N-J01 |
| Beverages | Beverage manufacturing (312100) | +6.1 | +33.0 (2.9) | *verified* | N-J01 |
| Paper | Paper manufacturing (322000) | -4.2 | +7.8 (0.7) | *verified* | N-J01 |
| — mills | Pulp, paper, and paperboard mills (322100) | -14.9 | +0.5 (0.0) | *verified* | N-J01 |
| Petroleum and coal products | Petroleum and coal products manufacturing (324000) | -1.2 | +15.2 (1.4) | *verified* | N-J01 |
| Chemicals | Chemical manufacturing (325000) | +4.2 | +24.6 (2.2) | *verified* | N-J01 |
| — basic, resins, agricultural, other chemicals | Chemical manufacturing (3251,2,3,9) (3250A1) | +2.1 | +18.6 (1.7) | *verified* | N-J01 |
| Plastics and rubber | Plastics and rubber products (326000) | +2.5 | +15.0 (1.4) | *verified* | N-J01 |
| — plastics | Plastics product manufacturing (326100) | +3.1 | +16.4 (1.5) | *verified* | N-J01 |
| Nonmetallic mineral products (cement, concrete) | Nonmetallic mineral product manufacturing (327000) | +2.1 | +18.4 (1.7) | *verified* | N-J01 |
| Wood products | Wood product manufacturing (321000) | -0.5 | +17.7 (1.6) | *verified* | N-J01 |
| — sawmills | Sawmills and wood preservation (321100) | -1.4 | +17.2 (1.6) | *verified* | N-J01 |
| Primary metals | Primary metal manufacturing (331000) | -1.6 | +14.2 (1.3) | *verified* | N-J01 |
| Fabricated metals | Fabricated metal product manufacturing (332000) | -2.4 | +7.4 (0.7) | *verified* | N-J01 |
| Machinery | Machinery manufacturing (333000) | -0.9 | +14.1 (1.3) | *verified* | N-J01 |
| Computer and electronic products | (334000) | +4.0 | +20.4 (1.9) | *verified* | N-J01 |
| Electrical equipment | Electrical equipment, appliance, and component (335000) | +11.5 | +17.0 (1.6) | *verified* | N-J01 |
| Motor vehicles | Motor vehicle manufacturing (336100) | +7.1 | +26.1 (2.3) | *verified* | N-J01 |
| — bodies and trailers | (336200) | +3.5 | +34.2 (3.0) | *verified* | N-J01 |
| — parts | Motor vehicle parts manufacturing (336300) | **-13.9** | **-24.6** (-2.8) | *verified* | N-J01 |
| Furniture | Furniture and related products (337000) | -6.3 | +4.9 (0.5) | *verified* | N-J01 |
| Wholesale, all | Wholesale trade (420000) | +2.1 | +26.9 (2.4) | *verified* | N-J01 |
| Durable merchant wholesalers | (423000) | +3.1 | n/p | *verified* | N-J01 |
| — lumber and construction materials (4233), hardware (4237) | Durable goods (4232,3,5,6,7,9) (4230A1) | +2.0 | n/p | *verified* | N-J01 |
| — motor vehicles and parts | (423100) | +2.5 | n/p | *verified* | N-J01 |
| — farm and garden machinery | (423820) | -1.8 | n/p | *verified* | N-J01 |
| Nondurable merchant wholesalers | (424000) | +1.9 | n/p | *verified* | N-J01 |
| — grocery (4244), beer and wine (4248) | (4240A1) | +3.2 | n/p | *verified* | N-J01 |
| — drugs (4242), chemicals (4246) | (4240A2) | +5.4 | n/p | *verified* | N-J01 |
| — petroleum (4247), paper (4241), misc. (4249) | (4240A3) | -1.4 | n/p | *verified* | N-J01 |
| — farm-product raw materials | (424500) | 0.0 | n/p | *verified* | N-J01 |
| Wholesale agents and brokers | (425000) | -4.9 | n/p | *verified* | N-J01 |
| Retail, all | Retail trade (44-450) | -0.2 | +28.7 (2.6) | *verified* | N-J01 |
| Motor-vehicle dealers | Motor vehicle and parts dealers (441000) | +2.3 | +34.3 (3.0) | *verified* | N-J01 |
| — automobile dealers | (441100) | +2.2 | n/p | *verified* | N-J01 |
| Furniture stores | Furniture and home furnishings retailers (449100) | -9.1 | n/p | *verified* | N-J01 |
| — electronics and appliances | (449200) | -13.0 | n/p | *verified* | N-J01 |
| Building materials | Building material and supplies dealers (444100) | +2.2 | n/p | *verified* | N-J01 |
| General merchandise | General merchandise retailers (455000) | +2.5 | +17.3 (1.6) | *verified* | N-J01 |
| Food and beverage stores | Food and beverage retailers (445000) | +0.9 | +11.8 (1.1) | *verified* | N-J01 |
| Gasoline stations | (457100) | +0.3 | n/p | *verified* | N-J01 |
| Fuel dealers | (457200) | -8.2 | n/p | *verified* | N-J01 |
| Nonstore and e-commerce | no row: the table uses 2022 NAICS, which dropped "nonstore retailers" (454) | — | — | not found | N-J01 |
| Air transportation | (481000) | +6.2 | +28.4 (2.5) | *verified* | N-J01 |
| Rail transportation | (482000) | +0.2 | +10.1 (1.0) | *verified* | N-J01 |
| Water transportation | (483000) | +2.9 | +26.8 (2.4) | *verified* | N-J01 |
| Truck transportation | (484000) | +2.1 | +23.9 (2.2) | *verified* | N-J01 |
| Couriers and messengers | (492000) | +4.1 | +24.7 (2.2) | *verified* | N-J01 |
| Warehousing and storage | (493000) | +2.0 | +28.1 (2.5) | *verified* | N-J01 |
| Support activities for transportation | (488000); output only for 487-88 combined | +4.6 | +26.7 (2.4), 487-88 | *verified* | N-J01 |
| — freight transportation arrangement | (488500) | +5.3 | n/p | *verified* | N-J01 |
| — road / rail / water support | (488400 / 488200 / 488300) | +3.0 / +0.8 / +3.3 | n/p | *verified* | N-J01 |
| Rental and leasing | Rental and leasing services (532000) | +1.4 | +26.4 (2.4) | *verified* | N-J01 |
| — car rental | Automotive equipment rental and leasing (532100) | +2.1 | +30.8 (2.7) | *verified* | N-J01 |

**Reading note.** K11 Test 1 passes the projection part if "the BLS 10-year employment **or** output projection is 0 or higher".
- **Only one requested row is below zero on both:** motor vehicle parts manufacturing (336300).
- **Rows with negative employment but positive output:** animal production; forestry and logging; paper and the mills; petroleum and coal; wood products and sawmills; primary and fabricated metals; machinery; furniture.
- **Rows with negative employment and no output published:** fuel dealers; furniture and electronics stores; petroleum/paper wholesale (4240A3); farm-machinery wholesale; wholesale agents. For these, only the parent row's output exists: retail +28.7%, wholesale +26.9%. Whether a parent row counts is the coordinator's call.

**EIA line (C-38).**
- **The source:** EIA *Annual Energy Outlook 2026*, released 8 April 2026, Table 11 "Petroleum and Other Liquids Supply and Disposition", product supplied in million barrels per day (N-J04, *verified*; downloaded file).
- **Gasoline.** Motor gasoline goes from **8.894** (2025) to 8.260 (2030, **-7.1%**) to **6.949** (2035, **-21.9%**) **[our calc]**.
- **Distillate.** Distillate goes from **4.070** (2025) to 4.106 (2030, +0.9%) to **3.706** (2035, **-8.9%**) **[our calc]**.
- **Sector totals.** Transportation liquids go from 13.815 to 11.434 (-17.2%). Residential and commercial liquids go from 1.137 to 1.110 (-2.4%) **[our calc]**.
- **Which case.** The file's scenario code is "cb2026". The AEO2026 page lists a "Counterfactual Baseline Case" and "Side Cases" rather than a "Reference case", so it is *assumed* that cb2026 is the main (baseline) case. The earlier AEO2021 file found at the old URL is not used.

---

## 3. Part 3: substitutes at scale (Test 1)

**How we read "substitute".** A substitute is something a regulator, government program or company is already running, or has scheduled, that would do the card's job or make it unnecessary. Rules that only set invoice contents change the job; they do not substitute for it. This was a light check, capped at about a quarter of the effort, so "none found" means none turned up, not that none exists.

| Card | Possible substitute | Primary source | At scale by about 2031? | Label |
|---|---|---|---|---|
| C-01, C-06 (and the C-25 lane) | Driverless trucks. Aurora: "We expanded driverless operations to 10 trucks in December [2025]"; the aim is "to exit 2026 with more than 200 driverless trucks"; "Driver as a Service" is expected from 2027. It runs a supervised Dallas–Laredo lane. The loads still have to be bought and matched | N-J32 (8-K, 11 Feb 2026); N-C25 (held) | no: hundreds of trucks, against 531,374 for-hire carriers (N-F02) | *verified* (filing); the scale judgement is *assumed* |
| C-08 | FMCSA's new "Motus" registration system, with identity checks through IDEMIA. It replaced the legacy systems from 14 May 2026. It checks identity when a carrier registers, not fraud on each load | N-J33 (Federal Register and FMCSA pages blocked) | unclear | *assumed* (snippets) |
| C-11 | NMFC freight classes based on density, from 2025-07-19. This changes the job; reweigh and inspection disputes remain | N-G20 (held) | no | held |
| C-12 | Carriers' late-delivery refunds. FedEx reinstated its Money-Back Guarantee from 12 Feb 2026 for listed express services; "all other FedEx® services will remain suspended until further notice". This shrinks the refund pool; it is not a substitute | N-J28 | no | *verified* (page extraction); UPS not checked |
| C-20 | The end of the de minimis exemption, which works the opposite way: CBP began enforcing on 29 Aug 2025, and 1.36 billion de minimis shipments (2024) now need entries ("more than 4 million packages every day"). No substitute was found | N-J29, N-J30 | no | *verified*; the executive-order number (14324) is *assumed* |
| C-21 | The FMC's 2024 demurrage and detention billing rule: it sets who may be billed and what an invoice must say. The charges remain | N-F32 (held) | no | held |
| C-24 | APHIS ePhyto: phytosanitary certificates exchanged electronically with participating countries (page modified 20 Aug 2026; the partner list did not load). Exporters still prepare the filings and the origin and letter-of-credit papers | N-J34 | unclear | *verified* (page); partner count not found |
| C-30 | The STB's 2021 demurrage invoice rule (EP 759): it sets invoice contents and machine-readable data. The charges remain | N-G33 (held) | no | held |
| C-31 | Electronic cattle transaction reporting (Washington's ECTR) and electronic veterinary certificates. These digitise part of the paperwork, state by state | N-J35 | unclear | *assumed* (snippet) |
| C-34 | States' self-issue permit portals: 85% of WSDOT's 183,502 permits were self-issued online in 2023. Multi-state routing still varies | N-J23; N-G55 (held) | yes in some states already; unclear nationally | *verified* |
| C-36 | State transportation departments' e-ticketing. FHWA says DOTs "in ten States … are currently applying e-Ticketing to asphalt, concrete, and/or aggregate delivery" (13 May 2024). E-tickets carry the card's job; a DOT-run system could replace third-party tools on public jobs | N-J31; N-G59 (held) | unclear | *verified* |
| C-38 | Electric vehicles and efficiency shrinking gasoline volume: -7.1% by 2030 and -21.9% by 2035 (EIA). This shrinks the unit counted; it does not replace the job | N-J04 | partly: most of the fall comes after 2030 | *verified*; % **[our calc]** |
| C-02, C-03, C-04, C-05, C-07, C-09, C-10, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-22, C-23, C-25 (filings), C-26, C-27, C-28, C-29, C-32, C-33, C-35, C-37, C-39, C-40 | none found | — | — | — |

---

## 4. Sources (N-J)

All accessed 2026-09-15.

| ID | Source (author/org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-J01 | BLS Employment Projections, Table 2.11 *Employment and output by industry, 2025 and projected 2035* | 2026 release | https://www.bls.gov/emp/tables/industry-employment-and-output.htm | page extraction (BLS blocks curl) | title, column units ("Billions of chained 2017 dollars"), all rows for agriculture, mining, manufacturing, wholesale, retail, transportation, rental |
| N-J02 | EIA, US product supplied of finished motor gasoline (MGFUPUS2) and distillate fuel oil (MDIUPUS2), monthly and annual | data to Jun 2026 | https://www.eia.gov/dnav/pet/hist_xls/MGFUPUS2m.xls ; …/MDIUPUS2m.xls (and …a.xls) | full (xls parsed) | monthly values 2004-2026; annual averages and 12-month rolling **[our calc]** |
| N-J03 | EIA, Adjusted sales of distillate fuel oil by end use (residential column) | annual, through 2020 | https://www.eia.gov/dnav/pet/xls/PET_CONS_821DSTA_DCU_NUS_A.xls | full | residential and total sales, 2004-2020 |
| N-J04 | EIA, *Annual Energy Outlook 2026*, Table 11 (scenario code cb2026) | released 8 Apr 2026 | https://www.eia.gov/outlooks/aeo/excel/aeotab11.xlsx ; https://www.eia.gov/outlooks/aeo/tables_ref.php | full (xlsx parsed); page text for the case names | product supplied rows 2025-2035 |
| N-J05 | USDA FAS, PSD Online bulk downloads (grains and pulses, oilseeds, dairy, livestock) | downloaded 2026-09-15 | https://apps.fas.usda.gov/psdonline/downloads/psd_grains_pulses_csv.zip (and psd_oilseeds, psd_dairy, psd_livestock) | full (CSV parsed) | US production and exports by MY; milk production; cattle slaughter, cow slaughter, calf crop, 2004-2026 |
| N-J06 | USDA AMS AgTransport, "Refrigerated Truck Volumes" (Market News, Specialty Crops) | updated Sep 2026 | https://agtransport.usda.gov/resource/rfpn-7etz.json ; metadata …/api/views/rfpn-7etz.json | full (API aggregates) | annual sums by mode and by district, 2000-2026; dataset and column descriptions |
| N-J07 | USDA AMS AgTransport, "Downbound Barge Grain Movements (Tons)" (attribution: US Army Corps of Engineers) | updated Sep 2026 | https://agtransport.usda.gov/resource/n4pw-9ygw.json | full (API aggregates) | annual tons by lock, 2003-2026 |
| N-J08 | USDA AMS AgTransport, "Rail Carloadings" (attribution: STB weekly Rail Service Metrics) | updated Sep 2026 | https://agtransport.usda.gov/resource/tb7q-kn5i.json | full (API aggregates) | originated carloads by commodity and year, 2017-2026 |
| N-J09 | STB, Public Use Carload Waybill Sample (via USDA AgTransport) | data years 2005-2024 | https://agtransport.usda.gov/resource/xve5-xb56.json | full (API aggregates) | expanded carloads by year for STCC 01, 14, 24, 26, 28, 29, 40, 46, 0113, 2821 |
| N-J10 | BTS, Monthly Transportation Statistics, "Freight Rail Carloads" (AAR data) | Jan 2004 - Jun 2026 | https://data.bts.gov/resource/crem-w557.json | full (API) | monthly carloads and intermodal units; column descriptions |
| N-J11 | BTS, Border Crossing Entry Data (trucks) | Jan 2004 - Jul 2026 | https://data.bts.gov/resource/keg4-3bc2.json | full (API aggregates) | annual trucks at Nogales, Hidalgo, Laredo |
| N-J12 | UN Comtrade, public preview API: US (842) imports of HS 0603 from the world | 2005-2025 | https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=842&cmdCode=0603&flowCode=M&partnerCode=0&period=… | full (JSON) | value and net weight by year (2007 weight missing) |
| N-J13 | Federal Reserve, G.17 Industrial Production, `ip_sa.txt` | data to Jul 2026 | https://www.federalreserve.gov/releases/g17/ipdisk/ip_sa.txt | full | G325, G3251, G3252, G3254, G321, G3212, G326, G3273 monthly |
| N-J14 | USGS, *Mineral Commodity Summaries 2010*: Stone (crushed); Sand and gravel (construction) | Jan 2010 | https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/mineral-pubs/stone-crushed/mcs-2010-stonc.pdf ; …/sand-gravel-construction/mcs-2010-sandc.pdf | full (PDF text) | salient statistics 2005-2009e |
| N-J15 | USGS, *Mineral Commodity Summaries 2013*, same two chapters | Jan 2013 | …/mcs-2013-stonc.pdf ; …/mcs-2013-sandc.pdf | full | salient statistics 2008-2012 |
| N-J16 | USGS, *Mineral Commodity Summaries 2026*, same two chapters | 2026 | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-stone-crushed.pdf ; …/mcs2026-sand-gravel.pdf | full | salient statistics 2021-2025e; events text |
| N-J17 | BEA, motor vehicle supplemental tables (`gap_hist.xlsx`), Table 6 | current file | https://apps.bea.gov/national/xls/gap_hist.xlsx | full | monthly light-vehicle sales, NSA |
| N-J18 | Census, CPS historical geographic mobility, Table A-1 | through survey year 2023 | https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/time-series/historic/hst_mig_a_1.xlsx | full | movers (total, different county, different state) and rates, 2004-2023 |
| N-J19 | Census, New Residential Construction, starts (`starts_cust.xlsx`) | to 2026 | https://www.census.gov/construction/nrc/xls/starts_cust.xlsx | full | monthly NSA starts, summed by year |
| N-J20 | Census, Monthly Retail Trade (`mrtssales92-present.xlsx`) | to 2026 | https://www.census.gov/retail/mrts/www/mrtssales92-present.xlsx | full | NAICS 4441 NSA annual totals |
| N-J21 | Census, Monthly Wholesale Trade (via FRED: S4244SM144NCEN, S4248…, S4242…, S4237…, S4233…) | 1992 - 2026 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=S4244SM144NCEN (etc.) | full (CSV) | monthly NSA sales, summed by year |
| N-J22 | BLS, PPI via Public Data API v1: WPUFD4111, WPU0261, WPU063, WPU104, WPU105, WPU106, WPUSI012011 | Jan 2004 - Aug 2026 | https://api.bls.gov/publicAPI/v1/timeseries/data/ | full (JSON) | monthly index values; annual averages **[our calc]** |
| N-J23 | WSDOT, Gray Notebook, "Oversize or overweight permits" | undated page | https://wsdot.wa.gov/about/data/gray-notebook/gnbhome/economicvitality/CVS/oversizepermits.htm | page extraction | permit counts and self-issue shares, 2019-2023 |
| N-J24 | AAR, "Weekly Rail Traffic for December and the Week Ending December 30, 2023" | 3 Jan 2024 | https://www.aar.org/news/weekly-rail-traffic-for-december-and-the-week-ending-december-30-2023/ | page extraction | full-year 2023 carload and intermodal totals |
| N-J25 | Maritime Executive, "AAR Reports 2009 Carload Traffic at Lowest Level Since 1988" (citing AAR) | Jan 2010 | https://www.maritime-executive.com/article/2010-1-14-aar-reports-2009-carload-traffic-lowest-level-1988 | page extraction; secondary | 2009 vs 2008 and 2007 carload % (*assumed*) |
| N-J26 | NAR newsroom, "In the news": AP, "2023 Was Slowest Year For US Home Sales In Nearly 30 Years" | Jan 2024 | https://www.nar.realtor/newsroom/in-the-news/2023-was-slowest-year-for-us-home-sales-in-nearly-30-years-as-high-mortgage-rates-frustrated-buyers | search snippet | 2023 4.09M, -18.7% (*assumed*) |
| N-J27 | Search snippets on existing-home sales: Wolf Street (14 Jan 2026) and Eye On Housing (Jan 2026) for 2025 at 4.06M; Housing Almanac/Norada for 2005 at 7.08M and 2008 at 4.13M; Calculated Risk quoting NAR's Dec 2011 benchmark (2010 at 4,190,000) | 2011-2026 | https://wolfstreet.com/2026/01/14/sales-of-existing-homes-in-2025-drop-to-lowest-since-1995-sellers-massively-yank-listings-off-the-market-waiting-for-spring/ ; https://www.calculatedriskblog.com/2011/12/existing-home-sales-revisions.html | snippets only | *assumed* values |
| N-J28 | FedEx, Service Guide, "Money-Back Guarantee" | effective 12 Feb 2026 | https://www.fedex.com/en-us/service-guide/money-back-guarantee.html | page extraction | reinstatement scope; other services suspended |
| N-J29 | CBP, "CBP ready to enforce end of de minimis loophole…" | 29 Aug 2025 | https://www.cbp.gov/newsroom/national-media-release/cbp-ready-enforce-end-de-minimis-loophole-securing-borders-and | page extraction | effective date; 1.36 billion shipments; 4 million a day. The EO number is from N-J30 (*assumed*) |
| N-J30 | Federal Register, "Notice of Implementation of the President's Executive Order 14324, Suspending Duty-Free De Minimis Treatment for All Countries" (CBP) | 2 Sep 2025 | https://www.federalregister.gov/documents/2025/09/02/2025-16802/notice-of-implementation-of-the-presidents-executive-order-14324-suspending-duty-free-de-minimis | search snippet only (Federal Register pages redirect to an "unblock" page) | EO number and title (*assumed*) |
| N-J31 | FHWA, EDC-6 "e-Ticketing and Digital As-Builts" | 13 May 2024 | https://www.fhwa.dot.gov/innovation/everydaycounts/edc_6/eticketing.cfm | page extraction | the ten-state quote |
| N-J32 | Aurora Innovation, Q4 2025 shareholder letter, 8-K Exhibit 99.1 | 11 Feb 2026 | https://ir.aurora.tech/sec-filings/all-sec-filings/content/0001828108-26-000014/finalaurora25q4sharehold.htm | page extraction | truck counts, 2026 target, 2027 plans, lanes |
| N-J33 | FMCSA "Motus": Federal Register notice 2026-08334 (29 Apr 2026); FMCSA fact sheet; FMCSA registration page | Dec 2025 - Apr 2026 | https://www.federalregister.gov/documents/2026/04/29/2026-08334/availability-of-motus-fmcsas-new-registration-system ; https://www.fmcsa.dot.gov/registration | **blocked** (redirect / 403); search snippets only | Phase I 8 Dec 2025; legacy systems replaced 14 May 2026; IDEMIA identity checks from Apr 2025 (*assumed*) |
| N-J34 | USDA APHIS, "Trading Partners Participating in Electronic Phytosanitary Certification – ePhyto" | modified 20 Aug 2026 | https://www.aphis.usda.gov/plant-exports/ephyto | page extraction (table did not load) | purpose; the fact that a partner list exists |
| N-J35 | Washington State Dept. of Agriculture, livestock inspection / electronic cattle transaction reporting | current | https://agr.wa.gov/services/inspections-and-investigations/inspections/livestock/livestock-inspection | search snippet | ECTR description (*assumed*) |
| N-J36 | GAO-10-38, *Household Goods Moving Industry* | 2009 | https://www.gao.gov/assets/gao-10-38.pdf | search snippet | "approximately 800,000 interstate household goods moves annually" (*assumed*; not used for a band) |
| N-J37 | USDA AMS AgTransport metadata catalogue | Sep 2026 | https://agtransport.usda.gov/api/views/metadata/v1 | full | dataset discovery only |

**Earlier project sources reused (not re-fetched):**
- R34 (AgRTQ, the Q1 2026 volume statement);
- N-C11 (BLS rows, cross-check) and N-C25 (Aurora 2025);
- N-F02 (carrier count);
- N-F32 (FMC rule);
- N-G20 (NMFC density);
- N-G33 (STB rule);
- N-G55 (WSDOT permits);
- N-G59 (e-ticketing vendors);
- N-G68 (Miami share of flower imports).

## 5. Could not access

- **USDA AMS annual *Fresh Fruit and Vegetable Shipments* PDFs:** 404 by curl, 403 by the fetch tool. The same Market News data came from AgTransport (N-J06).
- **Census economic-indicator API (EITS):** it now needs a key, and so does the port-level trade API (used for Miami's share). We used Census xlsx files and FRED copies instead. Miami's share was not re-checked.
- **FRED** timed out at first but worked later. The Fed's G.17 file was used for industrial production. No sawmill-only series was found (G3211 is absent; FRED IPG3211S and IPG32111S failed).
- **BLS www pages** block curl, so Table 2.11 was read by page extraction.
- **AAR commodity carloads for 2007-2010** are in the paid Rail Time Indicators. The STB Waybill Sample was used.
- **NAR annual history file:** not found on NAR's pages (its December summary PDFs contain only charts). All NAR figures are *assumed*.
- **Not found (searches tried are listed in the unit notes):**
  - state oversize/overweight permit counts for 2007-2010 (TxDMV, PennDOT, Florida, Ohio, older WSDOT editions);
  - wholesale used-vehicle auction volumes;
  - interstate household-goods shipment counts;
  - softwood lumber production;
  - roundwood harvest;
  - cut-flower stem counts.
- **Not checked** (time-box):
  - NASS cattle marketings and auction receipts;
  - containerised farm export tons (FAS GATS, PIERS);
  - the ACC chemical output index;
  - UPS guarantee status.
- **FMCSA Motus pages:** the Federal Register (unblock redirect) and fmcsa.dot.gov (403) were not readable, so the Motus details are *assumed*.
- **Stale AEO table:** EIA's `aeotab_11.xlsx` link still serves AEO2021. The AEO2026 file (`aeotab11.xlsx`) was used.
