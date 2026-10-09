# S3a check L: durability data for freight and trade units (K11 Test 3)

> **What this is:** evidence for knock-out K11 Test 3 at S3a ("settle the unknowns") of run 01. S2 left several freight and trade cards in the unknown band or with no data. This check looks for better series for the unit a fee would be counted on, then measures its fall in both downturns.
> **Date:** 2026-09-15.
> **Status:** input to S3a; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/3a_unknowns.md`.
> **Builds on:** `research/s2_check_H_downturns_freight.md` (check H) and `research/s2_check_J_downturns_other_and_projections.md` (check J). S2's figure is shown beside each new one.
> **Labels:**
> - *verified*: read at the source. That means a quote from the page, a value from a downloaded file, or an official table. "Archived copy" marks an official file or page read from a web.archive.org capture. "Via page extraction" marks a page read through a fetch tool rather than a raw download.
> - *assumed*: a search snippet, secondary summary, vendor or association claim, memory, or blocked page.
> - **[our calc]**: this document's own arithmetic. **[our call]**: this document's judgement.
> - N-L IDs are new sources (§4). N-H, N-J and N-C IDs are reused from earlier checks.

**The test (frozen, `0_criteria.md` §3):** the unit fell 13% or less from peak to trough in both downturns, or rose = pass band; more than 20% in either = fail band; 13-20%, or no data = unknown band.

**Windows:**
- **2008-09:** the highest value in 2006-2008 to the lowest in 2009-2010.
- **2022-25:** the highest in 2021-2022 to the lowest in 2023-2025.

**Practice rules applied (C15, `submarket_selection.md` §5.1):**
- Name the unit.
- Use a proxy only when no count exists, prefer physical measures, and name the proxy.
- Where monthly (or 12-month rolling) and annual data fall in different bands, the finer data decides, so both are shown.
- One firm's volumes never stand for an industry.
- Where parts of a card fall in different bands, the card-level unit decides.

**Plain-language terms:**
- **TEU:** twenty-foot equivalent unit. One 40-foot container is 2 TEU. **Loaded** means the box carries cargo. **Empty** boxes are being repositioned.
- **PIERS:** a commercial database built from ships' manifests and bills of lading (the shipping documents). The Maritime Administration (MARAD) uses it for its container statistics.
- **12-month rolling sum:** each month's value plus the 11 before it. It removes seasonal swings. A rolling figure "Feb 2008" means the 12 months ending February 2008.
- **Waybill Sample:** the regulator's (STB's) sample of railroad shipping documents, scaled up to national totals. **Expanded carloads** are the scaled-up counts.
- **STCC:** the Standard Transportation Commodity Code railroads use to classify freight.
- **T-100:** the Department of Transportation's (DOT's) monthly airline traffic reports. The international segment data cover US and foreign airlines.
- **Short ton:** 2,000 pounds.
- **Real output:** output adjusted for inflation. Dividing revenue by a producer price index (PPI) gives "deflated" revenue.
- **SA:** seasonally adjusted.
- **CBP trade entry:** a customs filing that declares an import. CBP's current statistics count "entry summaries"; older budget documents say "trade entries". The two are not proven to be the same count.
- **Band:** ≤13, 13-20, >20 (percent fall), "rose", or "not found".

---

## 1. Summary table

S2's figure is in brackets after each new one. Rolling = 12-month rolling sum.

| Unit | Cards | Series used | Direct count or proxy | 2008-09 annual; rolling | 2022-25 annual; rolling | Band 2008-09 / 2022-25 | Label | Sources |
|---|---|---|---|---|---|---|---|---|
| **L1** Loaded import containers, US total (TEU) | C-21, C-22, C-23 | MARAD customs-port series (annual) for 2008-09. MARAD/PIERS all-ports monthly and BTS 9-port monthly for 2022-25 | Direct count (loaded boxes, plus empties that carry a freight charge) | 2006 → 2009: **-21.89%**; rolling: **not found** nationally. [S2: at least -15% *verified*; about -21.5% *assumed*] | All ports: **-13.03%**; rolling **-16.08%**. Nine ports: -14.37%; rolling -17.97%. [S2: NRF annual -13.6%] | **>20 / 13-20** | *verified*; [our calc] | N-L01, N-L02, N-L03; N-H26 |
| L1x Two-port cross-check: Los Angeles + Long Beach loaded imports | (cross-check only) | Port-published monthly | Direct count, 2 ports | 2006 → 2009: -25.45%; rolling -27.29% | 2021 → 2023: -18.32%; rolling -25.48% | Not the industry unit | *verified*; [our calc] | N-L04, N-L05, N-L03 |
| **L2** Air freight, international (tons) | C-23 | 2008-09: DOT international freight, both directions, US + foreign airlines. 2022-25: T-100 inbound only | 2008-09: proxy (both directions). 2022-25: direct (inbound) | Both directions: 2007 → 2009 **-20.97%**; rolling **-23.19%**. Inbound: **not found**. [S2: ton-miles, US airlines, -19.8%; rolling -22.7%] | Inbound: **-4.25%**; rolling **-8.04%**. Both directions: -8.25%; rolling -9.40%. [S2: -10.3%; rolling -11.8%] | **>20 (both-direction proxy) / ≤13** | *verified* data; [our calc]; tons unit [our call] | N-L06, N-L07; N-H28 |
| **L3a** Rail carloads, total excluding intermodal | C-30 | BTS "Freight Rail Carloads" (AAR data), monthly | Direct count, all commodities | 2006 → 2009: **-19.88%**; rolling Dec 2006 → Feb 2010 **-20.00%** (-20.0026%). [S2: -19.9%; rolling -20.0%] | 2021 → 2024: -2.07%; rolling -3.28% [S2 same] | **On the 20% line** (annual 13-20; rolling exceeds 20 by 0.003 points) / ≤13 | *verified*; [our calc] | N-J10 |
| **L3b** Carloads of the card's shipper base | C-30 | Waybill Sample: chemicals and plastics (STCC 28), pulp and paper (26), scrap (40), grain mill products (204) | Direct count (expanded sample) | 2007 → 2009: **-12.15%**; rolling Sep 2008 → Oct 2009 **-14.60%**. With grain received (0113) added: -11.39%; rolling -14.25% | 2021 → 2023: -2.14%; rolling -4.19%. With grain: -2.12%; rolling -3.82% | **13-20 (≤13 annual) / ≤13** | *verified* data; [our calc] | N-J09 |
| L3c Carloads excluding coal (context) | C-30 | Waybill proxy: all expanded carloads minus coal (11), mixed shipments (46), empty containers (42) | Proxy | 2006 → 2009: -21.95%. AAR's own figure not found | 2022 → 2023: -0.02% | >20 / ≤13 | [our calc] | N-J09; N-L09 |
| **L4** Loaded truck containers entering from Mexico | C-25 | BTS Border Crossing data, "Truck Containers Loaded", from archived copies of the dataset | Direct count (loaded only) | Laredo: 2007 → 2009 **-8.40%**; rolling **-14.94%**. Whole border: -10.99%; rolling -14.39%. [S2 trucks, which include empties: Laredo -11.6%; rolling -14.1%] | **Rose** at Laredo and across the border (2024 values show a break) | **13-20 (≤13 annual) / rose** | *verified* (archived official file); [our calc] | N-L08; N-H29 |
| **L5** CBP trade entries | C-20 | DHS *Budget-in-Brief*, one "processed trade entries" figure per edition | Direct count, rounded; fiscal years inferred | FY2007 31.4M → FY2009 25.8M: **-17.8%**; no monthly. [S2: not found] | [S2: formal entry summaries FY2022 → FY2023 -7.1%] | **13-20 / ≤13** | Quotes *verified*; year mapping *assumed* [our call] | N-L15; N-L14; N-H22 |
| **L6** Brokered truckloads, industry-wide | C-07 | None found. TIA survey from 2009; Armstrong dollars | — | **Not found** (Armstrong: domestic transportation management gross revenue 2009 -15%, *assumed*) | **Not found** (TIA: Q1 2024 shipments -8.9% on a year earlier, *assumed*) | **not found / not found** | *assumed* | N-L18, N-L19 |
| **L7a** Truck tonnage, annual view | C-01, C-02, C-05, C-14, C-17 (C-11) | ATA SA index, annual averages of the monthly values | Proxy (tons) | 2006 → 2009: **-8.88%** [S2 monthly: -14.6%] | 2022 → 2025: -2.94% [S2 monthly: -5.5%] | **13-20 (monthly decides) / ≤13** | *verified* data; [our calc] | N-H01 |
| **L7b** Real output, long-distance general freight trucking (truckload and LTL together) | same | BLS real sectoral output, NAICS 48412 | Proxy (deflated dollars) | 2007 → 2009: **-17.66%** (all general freight, 4841: -18.98%) | 2021 → 2023: -7.46% (4841: -6.12%) | **13-20 / ≤13** | *verified* data; [our calc] | N-L10 |
| **L7c** Real revenue, truckload (484121) | C-01, C-02, C-05, C-14, C-17 | Census Service Annual Survey ÷ PPI | Proxy (deflated dollars) | 2006 → 2009: **-13.78%** | **Not available** (revenue ends 2022) | **13-20 / not found** | [our calc] on *verified* data | N-L11 |
| **L7d** Real revenue, LTL (484122) | C-11 | Census Service Annual Survey ÷ PPI | Proxy (deflated dollars) | 2007 → 2009: **-25.71%** | **Not available** | **>20 / not found** | [our calc] on *verified* data | N-L11 |
| L7e Cass shipments (cross-check) | C-01 group | Cass Freight Index, shipments (FRED) | Count, one processor's clients | **Not available**: the series starts Jan 2016 | 2022 → 2025: -14.92%; rolling -15.23% | — / 13-20 (one firm, so it cannot decide) | *verified* data; [our calc] | N-C10 |
| **L8a** Spot loads | C-06 | None for 2008-09 | — | **Not found**. A trade article gives all truckload loads -25.5% (Mar 2008 → Apr 2009), with no source named | [S2: DAT index about -1%, *assumed*] | **not found / ≤13** | *assumed* | N-L12 |
| L8b Cargo claims | C-10 | None | — | **Not found** | **Not found** (a vendor claims index began about 2025) | not found / not found | — | N-L22 |
| L8c Detained stops | C-03 | Repeated ATRI surveys (share of stops detained) | No count series | **Not found** | **Not found**. Detention frequency fell between 2014 and 2023 (*assumed*) | not found / not found (direction: down) | Mixed | N-L21 |
| L8d Truck visits to docks | C-04 | None direct | — | **Not found** | **Not found** | not found / not found | — | — |

---

## 2. Notes by unit

### L1. Loaded import containers, US total [C-21, C-22, C-23]

**2008-09: MARAD, *U.S. Waterborne Foreign Container Trade by U.S. Customs Ports*, found at source (N-L01).** MARAD's data page returns 403, but web.archive.org holds the official workbook `container-ports-2000-2017.xlsx` (captured 4 Apr 2021). Our sum of its 63 customs-port rows on the "Import TEU" sheet **[our calc]**:

| Year | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 |
|---|---|---|---|---|---|---|
| Import TEU | 17,365,221 | 18,610,849 | 18,475,545 | 17,097,096 | 14,536,169 | 16,623,149 |

- **Fall, 2006 → 2009: -21.89%** **[our calc]**. Taking 2007 as the peak instead gives -21.32%.
- **What it counts,** from the NOTES sheet (*verified*):
  - sheet title: "Imports in Twenty-Foot Equivalent Units (TEUs) - Loaded Containers Only";
  - "This report only includes loaded containers and empty containers that involve a freight charge";
  - "These statistics include transshipment cargo";
  - "The statistics exclude shipments between U.S. ports (Jones Act trade)";
  - source: "IHS Maritime - Port Import Export Reporting Service (PIERS). Data collected from vessel manifests and bills of lading".

  So it counts TEU, not boxes, at all US customs ports with foreign container trade.
- **Cross-check against the BTS report S2 read (N-H26):**
  - MARAD's 2008 → 2009 change is -14.98% for imports and -8.42% for exports **[our calc]**;
  - BTS wrote "imports fell 15 percent while exports fell 8 percent";
  - the two match, so this workbook is very likely the series behind the BTS report **[our call]**.
- **Vintage check (N-L02):**
  - The 2015 and 2016 releases give 2006 as 18,610,878 and 2009 as 14,536,169: -21.89%.
  - The March 2007 release gives 2006 as 18,476,687: -21.33% against the later 2009 figure.
  - Every vintage and either peak year puts the fall above 20%.
- **Weight as a second physical measure (N-L02):** import metric tons of loaded containers fell from 133,274,803 (2006) to 103,365,451 (2009): **-22.44%** **[our calc]**.
- S2's *assumed* snippet (18.6M to 14.6M, -21.5%) is confirmed in substance; the exact figure is -21.89%.

**2008-09, monthly national series: not found.** MARAD's series is annual. PIERS monthly data are sold commercially. NRF's 2007-2010 monthly releases were not pulled; one search returned no monthly table.

**Two-port monthly cross-check, 2008-09.** Los Angeles publishes monthly "Loaded Imports" for each year (N-L04). Long Beach's "TEUs Archive Since 1995" gives monthly "Loaded Inbound" (N-L05, archived copies; the live polb.com returns "Access Denied"). This is a two-port cross-check, not the industry unit.

| | Annual | 12-month rolling |
|---|---|---|
| Los Angeles | 4,410,170 (2007) → 3,524,386 (2009): -20.09% | Feb 2007 → Jan 2010: -23.04% |
| Long Beach | 3,719,680 (2006) → 2,534,896 (2009): -31.85% | Feb 2007 → Nov 2009: -33.34% |
| **Both ports** | 8,127,865 (2006) → 6,059,282 (2009): **-25.45%** | Feb 2007 8,313,503 → Nov 2009 6,044,806: **-27.29%** |

All percentages **[our calc]**.
- For the two ports, the rolling fall is 1.8 points deeper than the annual one.
- The two ports fell more than the nation. MARAD's own LA plus Long Beach figures fall 26.52% from 2006 to 2009, against 21.89% nationally, because trade shifted toward East and Gulf Coast ports **[our calc]**.
- A national rolling figure would very likely be at least as deep as the annual -21.89%, so finer data would not lift the result out of the >20 band **[our call]**.

**2022-25: new monthly series (N-L03).** BTS's *Supply Chain and Freight Indicators* carries two relevant series from January 2019:

| Series | Annual | 12-month rolling |
|---|---|---|
| "Containerized Imports at U.S. Ports in TEUs": MARAD's analysis of PIERS data, "all U.S. container ports" | 28,891,319 (2022) → 25,127,862 (2023): **-13.03%** | Aug 2022 29,691,630 → Sep 2023 24,915,819: **-16.08%** |
| "Loaded Import Containers at Select U.S. Ports": 9 ports' own figures (Charleston, Houston, Long Beach, Los Angeles, NY-NJ, Oakland, Virginia, Savannah, Seattle-Tacoma) | 24,595,064 (2021) → 21,060,622 (2023): -14.37% | Jun 2022 25,286,848 → Sep 2023 20,743,217: -17.97% |
| Los Angeles + Long Beach (two-port cross-check) | 10,095,135 (2021) → 8,245,688 (2023): -18.32% | Aug 2021 10,395,649 → Aug 2023 7,747,026: -25.48% |
| NRF, 12 largest ports (S2, N-H23 to N-H25) | 25.8M (2021) → 22.3M (2023): -13.6% | — |

All percentages **[our calc]**.

**Caveats:**
- The PIERS all-ports level (28.9M TEU in 2022) is higher than NRF's (25.5M) because it covers every port.
- That the all-ports series is loaded-only is assumed from MARAD's notes on the same PIERS source **[our call]**.
- BTS's Los Angeles values match the port's own pages exactly for the four months checked.

**Band:** 2008-09 **>20** (*verified*, annual, national). 2022-25 **13-20**: the finer rolling data is deeper than the annual data, but still under 20.

### L2. Air freight imports [C-23]

**2008-09: direct inbound tons not found.** The best proxy is better than S2's: tons rather than ton-miles, and foreign airlines are included.
- **Series:** DOT, *U.S. International Air Passenger and Freight Statistics*, dataset "International_Report_Freight" (N-L06). DOT describes it as "All nonstop commercial air freight traffic traveling between international points and U.S. airports". It is split by US gateway, foreign gateway and airline, with "carriergroup" 1 = US airlines and 0 = foreign airlines.
- **No direction:** it has no inbound/outbound field.
- **Unit:** not stated. Its 2021 total (12,752,337) matches the T-100 inbound-plus-outbound total in short tons (12,764,203) within 0.1%, so the unit is short tons **[our call]**.

| Both directions, US + foreign airlines | Annual | 12-month rolling |
|---|---|---|
| 2008-09 | 10,470,623 (2007) → 8,274,699 (2009): **-20.97%** | Feb 2008 10,504,586 → Sep 2009 8,068,627: **-23.19%** |
| 2022-25 | 12,752,337 (2021) → 11,699,818 (2023): -8.25% | Mar 2022 12,874,373 → Oct 2023 11,664,020: -9.40% |

- By airline group, 2007 to 2009: US airlines -21.62%, foreign airlines -20.40% **[our calc]**.

**2022-25: inbound found (N-L07).** BTS's "AFF - T100 Segment Summary Monthly" gives "Inbound International Freight (lbs)" from January 2014 only. Its annual and by-country versions also start in 2014.
- Inbound: 7,875,288 short tons (2021) → 7,540,680 (2023): **-4.25%**. Rolling, Mar 2022 → May 2023: **-8.04%** **[our calc]**.
- Outbound fell more, -11.98%, from 2021 to 2023. The inbound share of two-way tons went from 61.7% to 63.7%.

**What we cannot say:** how inbound air moved in 2008-09. In ocean trade, 2009 imports fell much more than exports (-15.0% against -8.4%, MARAD). If air followed the same pattern, inbound tons fell at least as much as the two-way total. That is untested **[our call]**.

**Band:** 2008-09 **>20** on the two-way proxy, both annual and rolling (inbound not found). 2022-25 **≤13** (inbound).

### L3. Rail carloads [C-30]

**(a) Total carloads excluding intermodal: BTS "Freight Rail Carloads" (AAR data), monthly (N-J10, re-fetched).**
- **Annual:** 16,809,627 (2006) → 13,467,316 (2009): **-19.88%** (-19.8833%) **[our calc]**.
- **12-month rolling:**
  - peak is the 12 months to Dec 2006 (that is, calendar 2006): 16,809,627;
  - trough is the 12 months to Feb 2010 (Mar 2009 - Feb 2010): 13,447,262;
  - fall: **-20.00%** to two decimals, **-20.0026%** to four;
  - the trough is 440 carloads below the 20% line (16,809,627 × 0.8 = 13,447,702) **[our calc]**;
  - the 12 months to Jan 2010 give -19.91%.
- **Precision:** the gap to the line is smaller than routine revisions to AAR's monthly counts would move. Whether BTS's months are calendar months or AAR's 4- and 5-week periods was not checked **[our call]**.
- **2022-25:** 11,631,391 (2021) → 11,391,183 (2024): -2.07%. Rolling Mar 2022 → Feb 2025: -3.28%.
- **Cross-checks held in check J:**
  - AAR said 2009 carloads were "down 16.1 percent compared with 2008, and down 18.2 percent when compared with 2007" (N-L09, which repeats N-J25);
  - BTS gives -16.4% and -18.1%.

**(b) The card-level unit: carloads of C-30's shipper base, from the STB Waybill Sample (N-J09, re-queried).** The card names "rail-served chemical, plastics, paper, scrap and grain processors".

**STCC codes used, and why:**
- **28**, chemicals or allied products. It includes 2821, plastic materials and synthetic resins, so plastics are not added again.
- **26**, pulp, paper or allied products.
- **40**, waste or scrap materials.
- **204**, grain mill products (flour, feed, wet corn milling and other milled products). This is what grain processors ship.
- **Variant B adds 0113, grain.** Processors receive grain cars, and demurrage (the daily charge for holding a railcar) also falls on receivers that hold cars. S2 used 0113 alone. Grain shipments mostly belong to C-29's world, so it is a variant, not the main unit **[our call]**.

| Expanded carloads, by data year | 2006 | 2007 | 2008 | 2009 | 2010 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|
| A: 28 + 26 + 40 + 204 | 4,595,394 | 4,694,624 | 4,622,692 | 4,124,128 | 4,622,251 | 5,278,040 | 5,261,921 | 5,164,948 | 5,365,004 |
| B: A + 0113 | 6,115,373 | 6,248,694 | 6,154,139 | 5,536,939 | 6,153,621 | 6,564,097 | 6,609,603 | 6,469,658 | 6,733,387 |

- **Annual [our calc]:**
  - A: 2007 → 2009 **-12.15%**; 2021 → 2023 **-2.14%**;
  - B: -11.39%; -2.12% (2022 → 2023).
- **12-month rolling, by waybill date** (the date the originating railroad prepared the waybill) **[our calc]**:
  - A: Sep 2008 4,747,556 → Oct 2009 4,054,549: **-14.60%**. For 2022-25: May 2022 → Sep 2023, -4.19%;
  - B: -14.25%; -3.82%.
- **Rolling caveats:**
  - Data year 2024 is the latest the STB has released.
  - December 2024 is undercounted, because waybills dated then but filed in 2025 are not out yet. The 2022-25 rolling series therefore stops at November 2024.
- **Parts of the base, 2008-09 / 2022-25** (these repeat check J where it covered them) **[our calc]**:
  - chemicals (28): -8.75% / -1.23%;
  - plastics (2821): -16.45% / +0.70%;
  - pulp and paper (26): **-21.69%** / -13.61%;
  - scrap (40): **-22.28%** / rose;
  - grain mill products (204): rose (+0.85%) / -3.56%;
  - grain (0113): -9.09% / -3.19%.
- **Caveats:**
  - The sample's record count roughly tripled from data year 2021, while the expanded totals stay continuous (check J).
  - Chemicals carry 54% of base A in 2007, so the result leans on chemicals.

**(c) AAR's "carloads excluding coal", 2006-2010: not found as an annual figure.**
- The AAR year-end coverage read (N-L09) gives only December 2009 excluding coal ("6.9 percent higher ... than in December 2008").
- Railway Age's copy returned 403.
- **Proxy from the Waybill Sample** **[our calc]**: all expanded carloads minus coal (STCC 11), mixed shipments (46, mostly intermodal) and empty containers and shipping devices (42). It falls from 17,774,556 (2006) to 13,872,683 (2009): **-21.95%**. From 2022 to 2023 it falls -0.02%.
- **Accuracy check:** the same proxy with coal kept falls 18.28%, 1.6 points less than AAR's total (-19.88%). So the proxy is approximate.
- **What it shows:** carloads other than coal fell harder than the total, because coal held up. But this base includes autos (STCC 37), lumber and aggregates, which C-30 does not target.

**Band:**
- total carloads: on the line (annual 13-20; rolling over 20 by 0.003 points);
- card-level shipper base: **13-20** on rolling (≤13 on annual) in 2008-09, **≤13** in 2022-25;
- pulp and paper and scrap stay **>20** as segments, as S2 found.

### L4. Laredo and the US-Mexico border [C-25]

**The live dataset has no loaded measure.** On 2026-09-15 the live BTS dataset (keg4-3bc2, N-H29) listed exactly eight measures: Buses, Bus Passengers, Pedestrians, Personal Vehicle Passengers, Personal Vehicles, Train Passengers, Trains, Trucks (*verified*, API).

**Earlier versions did have one (N-L08).** Archived copies of the same dataset's CSV, captured 29 May 2024 (data to Apr 2024) and 1 Oct 2025 (data to Aug 2025), carry 12 measures. The extra four are "Truck Containers Loaded", "Truck Containers Empty", "Rail Containers Loaded" and "Rail Containers Empty". BTS has since dropped them. The two captures agree on every figure below.

**Loaded truck containers entering the US (monthly, not seasonally adjusted) [our calc]:**

| | Laredo | Whole US-Mexico border |
|---|---|---|
| Annual 2006-2010 | 993,234 / 1,009,706 / 988,853 / 924,941 / 1,177,560 | 3,046,640 / 3,065,675 / 2,981,814 / 2,728,703 / 3,174,135 |
| 2008-09, annual | **-8.40%** (2007 → 2009) | **-10.99%** |
| 2008-09, 12-month rolling | May 2008 1,036,722 → Aug 2009 881,872: **-14.94%** | Aug 2006 3,116,542 → Oct 2009 2,668,054: **-14.39%** |
| Annual 2021-2024 | 1,910,648 / 2,080,941 / 2,354,701 / 4,958,781 | 4,720,966 / 5,076,369 / 6,214,521 / 10,664,994 |
| 2022-25 | **Rose.** The rolling low in 2023 is above the 2022 peak | **Rose** |

**Caveats:**
- **A likely break in 2024.** Loaded containers roughly doubled in 2024 while trucks rose 3%. That points to a change in reporting, which may be why BTS dropped the measure **[our call]**. The 2022-25 "rose" holds on 2023 data alone.
- **Empties cushioned the truck counts.** Empty containers at Laredo fell 30% from 2008 to 2010, so the trucks count (which includes empties) fell more than loaded containers on annual data: -11.6% against -8.4%. On rolling sums the two are close: -14.1% against -14.9%.

**Band:** 2008-09 **13-20** (rolling decides; ≤13 on annual), the same band as S2's trucks. 2022-25 **rose**.

### L5. CBP entries, FY2006-FY2011 [C-20]

**What was found: one rounded figure per edition of DHS's *Budget-in-Brief* (N-L15, PDF text read):**

| Edition (published) | Sentence | Fiscal year it most likely describes [our call] |
|---|---|---|
| FY2008 (Feb 2007) | "more than 31.1 million trade entries processed" | FY2006 |
| FY2009 (Feb 2008) | "more than 31.4 million processed trade entries" | FY2007 |
| FY2010 (May 2009) | "approximately 29 million processed trade entries" | FY2008 |
| FY2011 (Feb 2010) | "approximately 25.8 million processed trade entries" | FY2009 |
| FY2012 (Feb 2011) | "processes 25.8 million trade entries annually" | FY2010, or the FY2009 figure repeated |
| FY2013 (Feb 2012) | "processes 29.5 million trade entries annually" | FY2011 |

- **Fall:** 31.4M to 25.8M, **-17.8%** **[our calc]**. The trough is 25.8M whichever reading of the FY2012 edition is right.
- **Why these years:**
  - each edition's traveler count lines up with CBP's year-end figures one year back;
  - the FY2012 edition's "352 million travelers" matches CBP's "more than 352 million travelers in fiscal year 2010" (N-L16);
  - the FY2013 edition's "339 million" is close to FY2011's "more than 340 million".

  The fiscal years are still an inference, so the year mapping is *assumed*.
- **Earlier anchor:** GAO says "entries summaries" filed with CBP "rose from nearly 24 million in fiscal year 2001 to nearly 30 million in fiscal year 2005" (N-L14, *verified* via page extraction). That fits a peak near 31 million in FY2006-07.
- **Caveats:**
  - "Trade entries" is not defined and may include informal entries.
  - The figures are rounded ("more than", "approximately").
  - Do not splice them onto CBP's FY2021-26 "entry summaries" (N-H22): the names differ, and 25.8M (FY2009) against 36.97M (FY2021) implies a large rise.
- **Formal/informal split:** not found for FY2006-FY2011.
- **What else was tried, with no counts found:**
  - CBP's FY2010 year-end release and FY2011 review (value, travelers and containers only);
  - CBP's "typical day" page for FY2011 (64,483 containers a day);
  - archived ACE fact sheets from 2009-2011 (N-L17). They say entry types 01 and 11 "represent approximately 96 percent of all entries filed", but give no totals;
  - GAO-08-46;
  - five web searches.

**Band:** 2008-09 **13-20** (*verified* quotes, *assumed* years). 2022-25 **≤13** (S2).

### L6. Brokered truckloads, industry-wide [C-07]

**Not found in either window.**
- **TIA** (the brokers' trade association) runs a quarterly *3PL Market Report*. Search results say it "first came out in April 2009" and is based on about 43 member companies (N-L19, *assumed*). So there is no 2008 baseline.
- **TIA for 2022-25:** its Q1 2024 release says total shipments fell 8.9% against Q1 2023 (N-L18, association survey, so *assumed*). That is a year-on-year quarterly change, not a peak-to-trough fall. The Q3 2024 report PDF returned 403.
- **Armstrong & Associates (dollars):** domestic transportation management gross revenue fell 15% in 2009, and net revenue fell 11.4% (N-L19, snippet, *assumed*). These are dollars, including purchased trucking, so they are a weak stand-in for loads.
- **An unsourced claim:** a search summary says "a recession like the one in 2008-09 would produce a drop of more than 25% in load volume". Its source was not identified, so it is *assumed* and not used.
- S2's firm data (C.H. Robinson, Landstar, J.B. Hunt, RXO, ArcBest) remain the only load counts, and they diverge.

### L7. General truckload and LTL [C-01, C-02, C-05, C-14, C-17; C-11]

**(a) Cass Freight Index, shipments.** FRED series FRGSHPUSM649NCIS starts in **January 2016** (*verified*: the CSV's first value is 2016-01, 0.974). So there are no 2006-2010 values.
- 2022-25, as a cross-check: the annual average fell from 1.200 (2022) to 1.021 (2025), **-14.92%**. The rolling sum fell from Oct 2022 to Dec 2025: -15.23% **[our calc]**.
- This counts freight bills paid through one processor's clients. Under C15 it cannot stand for the industry, but it is a shipment count and it falls much further than ATA tonnage (-5.5%).
- A similar one-processor count, the U.S. Bank Freight Payment Index, reported Q4 2023 truck shipments 15.7% below Q4 2022, "the largest in the history of the Index" (N-L20, *assumed*).

**(b) ATA tonnage on an annual basis.** ATA's own full-year 2009 figure was not found after three searches. ATA called 2009 "the most severe drop in volumes ever" (N-L13, *verified* via page extraction).
- Annual averages of the monthly SA index (N-H01, re-fetched) **[our calc]**: 85.02 (2006) → 77.47 (2009), **-8.88%**; 2008 → 2009 alone is -8.61%; 2022 → 2025 is -2.94%.
- The monthly fall is -14.6%, as S2 found. Monthly and annual land in different bands, so the finer monthly data decides: **13-20**.
- A search summary quotes preliminary Freight Analysis Framework estimates of -2.4% (2008) and -11.1% (2009) (*assumed*).

**(c) Industry-wide real output.**
- **BLS real sectoral output (N-L10).** BLS publishes it for NAICS 4841 (general freight trucking), 48411 (local) and 48412 (long-distance). It does **not** publish it separately for truckload (484121) or LTL (484122): FRED has no such series. From the annual percent changes **[our calc]**:
  - 48412, long-distance (truckload and LTL together): 2006 +1.7, 2007 +0.2, 2008 -2.9, 2009 -15.2, 2010 +8.8, so 2007 → 2009 is **-17.66%**. For 2021-2025: +3.8, -3.4, -4.2, +2.1, -0.3, so 2021 → 2023 is **-7.46%**;
  - 4841, all general freight: **-18.98%** (2006 → 2009) and -6.12% (2021 → 2023);
  - 48411, local: -24.98% and -4.60%.
- **Census Service Annual Survey revenue divided by BLS PPI (N-L11)** **[our calc]**:
  - truckload (484121): nominal revenue $82,481M (2006), $83,386M (2007), $86,540M (2008), $70,551M (2009). Real revenue falls from 2006 to 2009: **-13.78%**;
  - LTL (484122): nominal $37,948M (2007), $29,260M (2009). Real revenue falls from 2007 to 2009: **-25.71%**;
  - FRED's revenue series end in 2022, so 2022-25 cannot be computed.
- **Caveats:**
  - These are deflated dollars, so they rank below physical counts.
  - The truckload price index includes fuel surcharges and fell 7% in 2009. Deflating by it props up real truckload revenue.
  - LTL's -25.7% partly reflects YRC's share loss to smaller carriers outside large firms' reporting. It is still an industry total (Census covers all employer firms).

**(d) Industry-wide LTL shipment or tonnage series: not found.** One further search found only ATA's all-trucking index and single carriers' figures.

**A load figure without a named source.** Heavy Duty Trucking, 27 Dec 2009: "Truckload volumes, measured by the number of loads, fell a total of 25.5 percent from a peak in March 2008 to a low in April 2009" (N-L12). The quote was read via page extraction, but the article names no source, so it is *assumed*. If it reflects an industry load count, it would be in the >20 band **[our call]**.

**Band, for the coordinator:**
- truckload in 2008-09: every tons or output proxy is 13-20 (monthly tonnage -14.6%, output -17.7%, real revenue -13.8%); only annual tonnage is lower (-8.9%), and one unsourced load figure is >20;
- LTL in 2008-09: >20 on real revenue;
- 2022-25: ≤13 on tons and output; 13-20 on one processor's shipment counts.

### L8. Lower-priority units (quick checks)

- **C-06, spot loads:** 2008-09 still **not found**.
  - A search summary gives TransCore's December 2009 spot-freight availability as "103 percent" above December 2008 (*assumed*). That is a rebound figure, not a fall.
  - The 25.5% load figure above is for truckload loads in general, not spot loads.
- **C-10, cargo claims:** no repeated count series.
  - The Synchro LTL Freight Claim Index calls itself "the industry's first public LTL claims benchmark", but its page gives no method or start date (N-L22, vendor).
  - A vendor report puts 2023 LTL claims at one in every 51 shipments (*assumed*).
  - Carriers publish claims ratios (claims paid ÷ revenue), which are dollars.
- **C-03, detained stops:** confirmed that no repeated count series exists. Repeated surveys give a direction:
  - ATRI's surveys of more than 1,900 drivers and carriers, 2014-2018, found a "27% increase in delays of six or more hours between 2014 and 2018" (N-L21, *verified* via page extraction at Transport Topics).
  - In 2023, "drivers reported being detained in 39.3 percent of all stops", and "driver detention has decreased slightly in the last few years" (ATRI, *verified* via page extraction).
  - Between 2014 and 2023, stops with any detention fell 6.5 points and stops with 2+ hours fell 11.4 points (*assumed*, snippets; the 6.5 matches N-C29).
  - **So:** detention rose into the tight 2018 market and fell in the 2023 downturn. Detained stops = stops × detention rate, and both fell in 2022-25, so detained stops probably fell more than freight volume **[our call]**.
- **C-04, truck visits to docks:** no direct count found. The only hit was a dock-scheduling vendor's figure for April 2020, which is outside both windows.
  - A dock visit is a pickup or a delivery, so a shipment count tracks it most closely in principle. After that comes tonnage (tons per visit vary). Warehouse real output (revenue including storage) tracks it least **[our call]**.
  - The shipment counts available (Cass and U.S. Bank) start in 2016-18 and cover single processors.
  - For 2008-09, only tonnage (-14.6% monthly) and warehouse output (-2.4%, check H) exist.

---

## 3. What the table suggests, for the coordinator (not a call)

**Where the band changes from S2:**
- **C-21, C-22, C-23 (loaded import containers):**
  - The 2008-09 fall is now at source: **-21.89%** (annual, all US ports, loaded TEU). It is above 20% in every vintage and with either peak year, and weight falls 22.4%. S2 had "13-20 at least, likely >20 (*assumed*)".
  - Rolling data would only deepen it (the two-port cross-check is 1.8 points deeper on rolling).
  - For 2022-25, monthly national data give -16.1% (all ports) and -18.0% (nine ports): 13-20, deeper than S2's annual -13.6%.
- **C-23, air:** the better proxy (tons, US and foreign airlines) is >20 in 2008-09 on both annual (-21.0%) and rolling (-23.2%) data; S2 had -19.8% annual. Inbound air in 2022-25 fell only 4-8%. Inbound 2008-09 remains unmeasured.
- **C-30:**
  - Total carloads sit exactly on the line: -19.88% annual; rolling -20.003%, 440 carloads past the line.
  - The card-level unit, carloads of its own shipper base, falls -12.2% annual and **-14.6% rolling** in 2008-09 and -2.1% / -4.2% in 2022-25. That is the 13-20 band on the finer data.
  - Pulp and paper, and scrap, remain >20 as segments.
  - Carloads other than coal (a proxy) fall 22.0%, but that base includes autos, lumber and aggregates the card does not target.
- **C-20:** the 2008-09 gap is filled at the 13-20 band: -17.8% on DHS's rounded "trade entries". The fiscal years are inferred.

**Where the band does not change:**
- **C-25:** the loaded measure (loaded truck containers) gives the same result as S2's trucks: 13-20 on rolling (Laredo -14.9%, border -14.4%), ≤13 on annual, and rose in 2022-25.
- **C-01, C-02, C-05, C-14, C-17:**
  - Still no industry load count for 2008-09. Every tons or output proxy sits in 13-20 except annual-average tonnage (-8.9%). Under C15 the monthly -14.6% decides.
  - A trade article's unsourced -25.5% for truckload loads, and one processor's -15% shipment fall in 2022-25 (Cass), both point deeper than tonnage. Neither can decide under C15.
- **C-11:** still no industry shipment count. Real LTL revenue (Census ÷ PPI) is >20 in 2008-09 (-25.7%); that is a dollar proxy.
- **C-07, C-06, C-10, C-03, C-04:** no usable industry series for 2008-09. The quick checks found none. For C-03, the detention rate falls in downturns, which would make detained stops fall faster than volume.

**Load-bearing findings:**
- MARAD's -21.89% (C-21, C-22, C-23).
- The C-30 card-level unit at -14.6% rolling, against the total's -20.003%.
- The DHS series for C-20.

---

## 4. Sources (new, N-L)

| ID | Source (author / org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-L01 | MARAD, *U.S. Waterborne Foreign Container Trade by U.S. Customs Ports (2000-2017)*, `container-ports-2000-2017.xlsx` | captured 4 Apr 2021 | https://web.archive.org/web/20210404200059/https://cms.marad.dot.gov/sites/marad.dot.gov/files/docs/outreach/data-statistics/7081/container-ports-2000-2017.xlsx | full (archived official file, downloaded, parsed) | NOTES sheet; Import TEU and Export TEU sheets, 63 port rows summed |
| N-L02 | MARAD, earlier vintages: `DS_ContainerPorts_97to14.xls`, `DS_ContainerPorts_00to15.xlsx`, "Container Custom Ports, 1997-2006.xls" (file saved Mar 2007) | captured 5 Sep 2015, 1 Nov 2016, 16 Sep 2008 | https://web.archive.org/web/20150905095507/http://www.marad.dot.gov/wp-content/uploads/xls/DS_ContainerPorts_97to14.xls ; https://web.archive.org/web/20161101074616/https://www.marad.dot.gov/wp-content/uploads/xlsx/DS_ContainerPorts_00to15.xlsx ; https://web.archive.org/web/20080916012919/http://marad.dot.gov/MARAD_statistics/2005%20STATISTICS/Container%20Custom%20Ports,%201997-2006.xls | full (archived official files, parsed) | import TEU and import metric-ton sums by year |
| N-L03 | BTS, *Supply Chain and Freight Indicators* (data.bts.gov y5ut-ibwt) | Jan 2019 - Jun 2026 | https://data.bts.gov/resource/y5ut-ibwt.json | full (API) | "Containerized Imports at U.S. Ports in TEUs" (MARAD analysis of PIERS, all ports); "Loaded Import Containers at Select U.S. Ports in TEUs" (9 ports); notes and sources; indicator list |
| N-L04 | Port of Los Angeles, "Historical TEU Statistics" pages, 2006-2010 and 2021-2025 | page as of Sep 2026 | https://www.portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-2008 (and -2006 to -2025) | full (HTML downloaded, parsed) | monthly loaded imports; calendar-year totals |
| N-L05 | Port of Long Beach, "TEUs Archive Since 1995" | captured 17 Jan 2010, 4 Jan 2011, 14 Jan 2012 | https://web.archive.org/web/20110104071345/http://www.polb.com/economics/stats/teus_archive.asp | full (archived official page, parsed) | monthly "Loaded Inbound" TEU, 2005-2010 |
| N-L06 | US DOT (Office of the Secretary), *U.S. International Air Passenger and Freight Statistics*: "International_Report_Freight" (datahub.transportation.gov u4sg-r5vg) | 1990 - Dec 2025 | https://datahub.transportation.gov/resource/u4sg-r5vg.json | full (API aggregates) | freight totals by year, month and carrier group; column definitions |
| N-L07 | BTS, "AFF - T100 Segment Summary Monthly" (jqx4-4iha); annual (bu82-4pwz); by country (56rv-9p75) | Jan 2014 - Feb 2026 | https://data.bts.gov/resource/jqx4-4iha.json | full (API) | inbound and outbound international freight (lbs); year coverage of all three |
| N-L08 | BTS, *Border Crossing Entry Data* (keg4-3bc2), archived CSV versions | captured 29 May 2024 (data to Apr 2024) and 1 Oct 2025 (data to Aug 2025) | https://web.archive.org/web/20240529204214/https://data.bts.gov/api/views/keg4-3bc2/rows.csv?accessType=DOWNLOAD | full (archived official file, parsed) | list of 12 measures; "Truck Containers Loaded", "Truck Containers Empty" and "Trucks", monthly, Laredo and US-Mexico border |
| N-L09 | Maritime Executive, "AAR Reports 2009 Carload Traffic at Lowest Level Since 1988"; Calculated Risk, "Rail Traffic in 2009: Lowest since at least 1988" (both reporting AAR) | Jan 2010 | https://www.maritime-executive.com/article/2010-1-14-aar-reports-2009-carload-traffic-lowest-level-1988 ; https://www.calculatedriskblog.com/2010/01/rail-traffic-in-2009-lowest-since-at.html | full, via page extraction; secondary | full-year change against 2008 and 2007; December 2009 excluding coal; no full-year figure excluding coal |
| N-L10 | FRED: BLS real sectoral output, IPUIN48412T011000000, IPUIN4841T011000000, IPUIN48411T011000000 | annual to 2025 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=IPUIN48412T011000000 (and the other IDs) | full (CSV) | annual % changes, 2005-2025; that no 484121 or 484122 series exists |
| N-L11 | FRED: Census Service Annual Survey revenue, employer firms (REVEF484121ALLEST, REVEF484122ALLEST); BLS PPI (PCU484121484121, PCU484122484122) | revenue 1998-2022; PPI Dec 2003 - Aug 2026 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=REVEF484121ALLEST (and the other IDs) | full (CSV) | annual revenue; monthly PPI, averaged by year |
| N-L12 | Heavy Duty Trucking, "Economy, Government Top Trucking Issues for 2009" | 27 Dec 2009 | https://www.truckinginfo.com/news/economy-government-top-trucking-issues-for-2009 | full, via page extraction; the figure's source is not named | the 25.5% load sentence |
| N-L13 | Talk Business & Politics, "2009 likely the toughest ever for the trucking industry" | 19 Jan 2010 | https://talkbusiness.net/2010/01/2009-likely-the-toughest-ever-for-the-trucking-industry/ | full, via page extraction | ATA quotes; no full-year tonnage figure |
| N-L14 | GAO-07-735, *Intellectual Property: Better Data Analysis and Integration Could Help U.S. Customs and Border Protection Improve Border Enforcement Efforts* | Apr 2007 | https://www.gao.gov/assets/a259895.html | full, via page extraction | entry summaries, FY2001 and FY2005 |
| N-L15 | DHS, *Budget-in-Brief*, FY2008-FY2013 editions | Feb 2007 - Feb 2012 | FY2010: https://www.dhs.gov/sites/default/files/publications/budget_bib_fy2010.pdf ; FY2011: https://www.dhs.gov/sites/default/files/publications/budget_bib_fy2011.pdf ; FY2008, FY2009, FY2012, FY2013 via web.archive.org captures of https://www.dhs.gov/xlibrary/assets/budget_bib-fy2008.pdf , …/budget_bib-fy2009.pdf , …/budget-bib-fy2012.pdf , …/mgmt/dhs-budget-in-brief-fy2013.pdf | full PDF text (extracted locally) | CBP overview and "Service to the Public" sentences: trade entries and travelers |
| N-L16 | CBP: "CBP Announces Fiscal Year 2010 Year-End Data"; "CBP's 2011 Fiscal Year in Review"; "On a Typical Day in Fiscal Year 2011" | 2010-2011 | https://www.cbp.gov/newsroom/national-media-release/cbp-announces-fiscal-year-2010-year-end-data ; https://www.cbp.gov/newsroom/national-media-release/cbps-2011-fiscal-year-review ; https://www.cbp.gov/newsroom/stats/on-typical-day-fy2011 | full, via page extraction | travelers, trade value, containers; no entry counts |
| N-L17 | CBP ACE fact sheets, archived (ace_entry_summary.xml, ace_accomp_09.xml, ace_accomp_10.xml) | captured 2009-2011 | https://web.archive.org/web/20090906202553/http://www.cbp.gov/xp/cgov/newsroom/fact_sheets/trade/ace_factsheets/ace_entry_summary.xml | full (archived pages) | entry types 01 and 11 are about 96% of entries; no totals |
| N-L18 | TIA, "Logistics Industry Continues to See Declines as the Supply Chain Market Corrects Itself From Pandemic Highs" (Q1 2024 *3PL Market Report*) | 6 Jun 2024 | https://news.tianet.org/logistics-industry-continues-to-see-declines-as-the-supply-chain-market-corrects-itself-from-pandemic-highs/ | full, via page extraction (association survey) | Q1 2024 shipment, revenue and invoice changes |
| N-L19 | TIA *3PL Market Report* background, and Armstrong & Associates 2009 figures, from search results | various | e.g. https://www.logisticsmgmt.com/article/tia_q3_report_shows_steady_annual_gains_in_brokered_3pl_shipments ; https://www.3plogistics.com/hanging-tough-3pl-market-and-financial-results-released/ | snippet only | TIA start date (Apr 2009) and panel (about 43 members); Armstrong DTM 2009 gross -15%, net -11.4% |
| N-L20 | U.S. Bank Freight Payment Index, Q4 2023 release (Business Wire) | 1 Feb 2024 | https://www.businesswire.com/news/home/20240201773777/en/ | snippet only (page 403) | Q4 2023 shipments -15.7% on a year earlier |
| N-L21 | ATRI detention surveys: Transport Topics, "Driver Detention Has Increased in Recent Years, ATRI Finds"; ATRI release; point changes 2014-2023 from search results | 4 Sep 2019; 10 Sep 2024 | https://www.ttnews.com/articles/driver-detention-has-increased-recent-years-atri-finds ; https://truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/ | full, via page extraction (both); snippets for the point changes | survey years and sample; 2014-18 change; 2023 rate; direction |
| N-L22 | Synchro LTL Freight Claim Index page; CorePiper, "The 2026 State of Freight Claims" | 2025-2026 | https://synchrogistics.com/synchro-ltl-claims-index/ ; https://corepiper.com/blog/state-of-freight-claims-2026/ | page extraction (Synchro); snippet (CorePiper); vendors | index description; 2023 claim rate |
| N-L23 | BTS, "Freight by Mode since the Recession" (BTS 39-17) | 2017 | https://web.archive.org/web/2020/https://www.bts.gov/newsroom/freight-mode-recession | archived page, partly read (live page 403) | release text; modal index table (not used) |
| N-L24 | BTS, *National Transportation Statistics* Table 1-54, "U.S.-Mexican Border Land-Freight Gateways: Number of Incoming Truck or Rail Container Crossings" | captured 22 May 2017 | https://web.archive.org/web/20170522183703/https://www.bts.gov/archive/publications/national_transportation_statistics/table_01_54 | archived page, first rows only | confirms container counts by gateway were published (Laredo 2002: 1,437,580); not used |

**Reused and re-fetched or re-queried:**
- N-H01: FRED TRUCKD11, re-fetched as CSV for annual averages.
- N-H29: the live border dataset; its measure list was re-checked.
- N-J09: Waybill Sample, re-queried with new STCC groups and waybill-date months.
- N-J10: BTS rail carloads, re-fetched.
- N-C10: Cass shipments on FRED, re-fetched to check the start date.

**Reused, not re-fetched:**
- N-H22: CBP FY2021-26.
- N-H23 to N-H25: NRF.
- N-H26: BTS/RITA, *America's Container Ports* 2011.
- N-H27: MARAD snippet, now superseded by N-L01.
- N-H28: air ton-miles.
- N-H34: GAO detention.
- N-H36 to N-H39: DAT and TransCore.
- N-J24, N-J25: AAR.
- N-C24: ATRI 2023.
- N-C29: detention trade press.

## 5. Could not access, or not found

**Blocked or refused:**
- **MARAD data pages** (403). The workbooks were read from web.archive.org copies instead (N-L01, N-L02).
- **BTS archive:** *America's Container Ports* 2009 edition (403 via the fetch tool) and "Freight by Mode since the Recession" (403; archived copy read).
- **DOT international air report pages** on transportation.gov: 403.
- **Census international trade API:** redirects to `missing_key.html`, so a key is needed. Air import shipping weight could not be pulled.
- **BTS TranStats "Data Elements" page:** a plain request returns the passenger view whatever the query value. The freight view needs the page's form. Not pursued further.
- **Port of Long Beach live site:** "Access Denied". Archived pages were used.
- **Railway Age's AAR 2009 article, CCJ, Overdrive, Business Wire (U.S. Bank), TIA's Q3 2024 PDF:** 403.
- **DHS Budget-in-Brief FY2009 and FY2012 at dhs.gov:** 404 and curl-blocked. Archived copies were read.

**Not found after searching (the attempts are listed in §2):**
- **A national monthly series of loaded import TEU for 2006-2010.** MARAD is annual. NRF's monthly releases for 2007-2010 were not pulled. The USACE Waterborne Commerce container tables and AAPA were not tried once MARAD was found at source.
- **Inbound international air tons, 2006-2010.** The T-100 summaries start in 2014; the DOT international report has no direction field; TranStats and the Census API were not usable.
- **AAR's full-year 2009 figure for carloads excluding coal.** A Waybill proxy is given instead.
- **CBP counts by fiscal year for FY2006-FY2011 in CBP's own reports,** and any split into formal and informal entries. Only DHS's rounded "trade entries" were found.
- **Industry-wide counts of brokered loads, truckloads, LTL shipments and spot loads for 2008-09.**
- **ATA's own full-year 2009 tonnage change.**
- **Census Service Annual Survey revenue for 484121 and 484122 after 2022.** FRED's series end in 2022; Census's newer survey releases were not checked.
- **Repeated count series for cargo claims, detained stops and truck visits to docks.**
