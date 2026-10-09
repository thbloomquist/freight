# S3a check M: settling the unknowns on the 13 lean-fail cards

- **What this is:** evidence for S3a ("settle the unknowns") of run 01.
  - It covers the 13 cards whose unknowns lean toward failing (`research/selection_runs/run-01/2_knockouts.md` §6): C-24 to C-32, C-34, C-35, C-38 and C-40.
  - For each card it looks for the missing inputs S2 named, replaces judgement inputs with sourced ones where a source exists, and re-runs the arithmetic under the frozen tests (`0_criteria.md` §3).
  - It builds on `research/s2_check_K_savings_pools.md` (check K) and shows old → new.
- **Date:** 2026-09-15.
- **Status:** input to S3a; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/3a_unknowns.md`.
- **Labels:**
  - *verified*: read at the source. That means a quote from the page, a value from a downloaded file or official table, or an official API. "Page extraction" means the page was read through the fetch tool.
  - *assumed*: a search snippet, secondary summary, vendor claim, memory, or blocked page. Vendor figures are always *assumed*.
  - **[our calc]** marks our own arithmetic; **[our call]** marks our own judgement.
- **Source IDs:** new sources are N-M01 to N-M45 (§4). Earlier IDs (N-E…, N-G…, N-J…, N-K…) are cited as they are.
  - Where an earlier dataset was queried again for new rows, it keeps its old ID and the text says "re-queried".

**The tests used here (frozen; `submarket_selection.md` §5.1):**
- **K5 desk rule (C13):**
  - pass if 10% of the savings range's low end reaches $25M, i.e. a low end of $250M or more;
  - fail if 35% of the high end is clearly short of $25M, i.e. a high end well under about $71M;
  - unknown in between;
  - a generous case within a few percent of $25M counts as "about", so it is unknown, leaning fail.
- **The central fee pool** is 20% × √(low × high). It only orders the work.
- **K11 Test 3 (with the C15 practice):**
  - It measures the unit a fee would be counted on, peak to trough.
  - Windows (check J): 2008-09 = a peak in 2005-2008 to a trough in 2009-2011; 2022-25 = a peak in 2021-2022 to a trough in 2023-2025.
  - Bands: a fall of 13% or less (or a rise) is the pass band; 13-20% is unknown; over 20% is the fail band.

**How to read the numbers:**
- Every savings pool is cost base × avoidable share × share software could remove.
- The low end multiplies all the low inputs, and the high end all the high ones.
- "Old" is check K's figure; "new" is this check's. Where nothing sourced was found to replace a judgement, the range is left unchanged, and the card says what was tried.

**Words used here:**
- **ICR (information-collection request):** the filing an agency sends to the Office of Management and Budget for each form it requires. It estimates how many forms are filled in a year and how long each takes. So it is the regulator's own estimate of paperwork time.
- **ICVI (interstate certificate of veterinary inspection):** the health paper a veterinarian signs for livestock crossing a state line.
- **Documentary and border compliance (World Bank *Doing Business*):**
  - documentary compliance is the time and cost of getting, preparing and submitting the documents for one shipment, including broker and forwarder fees for them;
  - border compliance is customs clearance, mandatory inspections, and handling at the border.
- **AES/EEI:** the Automated Export System, where exporters file the Electronic Export Information for each export shipment.
- **Phytosanitary certificate:** a plant-health certificate that many importing countries require.
- **FAST (Free and Secure Trade):** US Customs and Border Protection's program of dedicated lanes for pre-vetted carriers, drivers and shippers.
- **Secondary railcar market:** where grain shippers resell guaranteed rail freight they bought from a railroad. A **shuttle train** is a train of about 110 grain cars that runs between one origin and one destination.
- **Demurrage:** a railroad's charge when a customer holds cars beyond the free time. **Accessorials** are extra charges beyond the line-haul rate.
- **OS/OW permit:** a state permit for an oversize or overweight load. A **non-divisible** load is one that can't be broken down, such as a transformer.
- **Hazard class:** the Department of Transportation's grouping of hazardous materials. For example, Class 3 is flammable liquids, most of it fuels; Class 8 is corrosives.
- **Vehicle-tank meter:** the meter on a fuel truck. Its **maintenance tolerance** is the largest error an inspector allows in service.

---

## 1. Summary table

Cards are in the order of the brief: lowest S2 central fee pool first. "S2 → new" gives the savings pool a year.

| Card | Unknowns | S2 range → new range (central fee pool) | Inputs replaced (old → new, label) | Inputs still [our call] | K3/K4/K6/K7 findings | K11 findings | Sources |
|---|---|---|---|---|---|---|---|
| C-27 Border produce | K5, K6, K7 | $7-82M ($5M) → **$7.1-58.9M ($4.1M)**. With a document-cost part added, as C-25 counts it: $12.8-70.7M ($6.0M) | Gateway loads: 362-513k [our call] → **355-368k**. Nogales + Pharr carry 57.5-61.1% of Mexican produce crossings (USDA Market News, *verified*) | Avoidable cost $100-400 a load; removable 20-40%; in the variant, 10-20% of the $160 document cost | **K6:** documents are ~22% of the cost and ~41% of the time of a Mexico-US road crossing (World Bank case, auto parts). The rest is inspection and handling. **K7:** the desk cannot show that importers would credit software; open for S5. Pharr buyer count not found | — | N-J06 (re-queried), N-G14, N-K12, N-M05, N-M06, N-M20, N-M21, N-M22, N-M43 |
| C-31 Livestock | K5, K11 | $11-70M ($6M) → **unchanged $11-70M ($5.6M)**. Generous case still $24.5M | None. Regulator data on the papers part: 87,500 ICVIs a year at 0.25 hours each (APHIS ICR, *verified*), about $8.60 each and $0.24 per average load [our calc] | Admin cost $15-40 a load; removable 30-50%; loads 2.5-3.5M | — | **Card-level unit built** (cattle + hog loads): **2008-09 -2.8% to -3.6%; 2022-25 -4.6% to -8.6%** under three weightings. That is the pass band. Cattle alone: -2.9% / -13.8% | N-J05, N-M01, N-M02, N-M03, N-M42 |
| C-35 Tank loads | K4, K5, K7, K11 | $9-227M ($9M) → **$4-185M ($5.6M)** | Paperwork: 10-20 minutes ($3-8) → **1.5 minutes, $0.56-1.00** (PHMSA ICR, *verified*). Tonnage low end: 213M → 207M tons (CFS 2022 split by hazard class, *verified*) | Wash mismatch $2-30 a load (drives the high end); high tonnage; removable 20-40% | **K4:** loads and paperwork now come from named data; the mismatch rate is still a judgement. **K7:** open | **Chemicals excluding pharma, output: -26.9% monthly (-21.8% annual) in 2008-09; -9.7% in 2022-25.** Rail chemical carloads: -8.8% / -1.2%. No tank-truck count found | N-M04, N-M17, N-M18, N-M19, N-J09, N-J13, N-K09 |
| C-24 Export docs | K3, K4, K5, K7, K11 | $23-114M ($10M) → **$32-117M ($12.3M)** | Containers: snippet → *verified* (3.22-3.52M TEU a year, 2021-25). Cost per container, low end: $40 [our call] → **$60** (World Bank documentary compliance for a US export, *verified*) | Cost high $120; 1.8 TEU a box; removable 30-50% | **K3:** 7,130 farm and food exporters in NAICS 111, 112, 311 and 312 (6,679 small or mid-sized), plus part of 22,481 nondurable-goods wholesalers (*verified*). **K4:** volume and unit cost now come from named data. **K7:** open | **Containerized farm exports: 2022-25 -8.5% (TEU), the pass band. 2008-09: no count** (series starts 2010) | N-M05 to N-M12, N-M44, N-J05, N-J34 |
| C-26 Produce rejections | K4, K5 | $10-274M ($11M) → **unchanged ($10.6M)**. Sensitivity with 2% as the high rejection rate: $10-137M ($7.5M) | None. Context: ReFED's 2% (an expert-interview assumption; *assumed*); USDA PACA handles about 1,117 claims a year, about $18.8k each (snippet; *assumed*) | Rejection rate 1-4%; loss $3-10k a load; removable 20-40% | **K4:** stays open. No neutral rejection rate; PACA claims give a floor of about 0.07% of loads | — | N-K12, N-M24, N-M25, N-M26 |
| C-29 Rail and barge buying | K5, K6, K7, K11 | $36-109M ($13M) → **unchanged ($12.5M)** | None. Context: secondary railcar bids swing with a within-year standard deviation of $151-1,200 a car (*verified*) | Timing premium $20-60 a car and $0.50-1.50 a ton | **K6:** peer-reviewed work treats how many cars to buy and when as a decision problem, so an information lever exists, though the market price dominates. **K7:** the benchmark moves; open | **Rail + barge tons: 2008-09 -9.8%** (USDA modal-share data). **2022-25: -17.9% to -18.2%** with the weekly rail series, or **-8.4%** with the waybill sample | N-M13 to N-M16, N-J07, N-J08, N-J09 |
| C-32 Milk hauling | K5 | $29-148M ($13M) → **unchanged ($13.1M)** | None | Removable 3-8% | 93 dairy co-ops (USDA RD, 2024). Hauler count not found. Non-US routing cases save 3-16% of distance or time | — | N-M27 to N-M30, N-K08, N-K15 |
| C-38 Fuel reconciliation | K5 | $28-164M ($13M) → **unchanged ($13.6M)** | Marketer count: PMAA's "8,000" (*assumed*) → **7,679 firms** (SUSB 2022, *verified*) | Cost $5-15 a load; removable 30-50% | Context: NIST meter tolerance ±0.3%; Maryland found 12% of fuel-truck and rack meters in violation, and 0.7% of delivery tickets | — | N-K05, N-M31, N-M32, N-K38 |
| C-25 Laredo | K5, K7 | $50-177M ($19M) → **$68-183M ($22.4M)** | Paperwork per crossing: $50-150 [our call] → **$160** (World Bank documentary compliance for a Mexico export plus a US import, *verified*) | Share of trucks loaded, 70% (low end only); removable 10-20% of paperwork and 10-25% of delay | **K7:** FAST lanes cut crossings by 2-19 minutes, but FAST is a Customs program, not software; open | (check L) | N-M05, N-M06, N-M22, N-M23, N-K06, N-K18 |
| C-30 Rail demurrage | K5 | $40-236M ($19M) → sensitivity **$40-167M ($16.4M)** | High cost base: $1.57B (2021 pace) → about **$1.05-1.12B for 2024**, scaled by CSX's and UP's revenue lines [our calc on filings] | Low base $0.8B; removable 5-15%; applying the scaling | Class I demurrage totals for 2022-25 not found; disputed or waived share not found | (check L) | N-M33, N-M34, N-M35, N-M45, N-F34 |
| C-34 OS/OW permits | K4, K5, K11 | $39-260M ($20M) → **$53-244M ($22.7M)** | Permits a year: 3.1-5.2M [our calc from a Texas-share call] → **4.24M in 44 states** (FHWA, 2012, *verified*), plus 0-15% for 6 non-reporting states | Cost $50-100 a permit; removable 25-50%; the six-state add-on | **K4:** the count now comes from FHWA data (dated). 30 states ran automated self-issue systems in 2017 | **44-state permits 2008→2009: -10.2%** (the window before 2008 isn't covered). 2022-25: rose in Washington and Texas (no national series) | N-M36, N-M37, N-M38, N-K07, N-J23 |
| C-28 Harvest grain | K5 | $34-314M ($21M) → **unchanged ($20.7M)** | None | Wait 0.2-0.5 hour at $60-90 an hour; ticket work $2-5; removable 15-30% | Elevator companies: about 1,800-2,400 (SUSB 424510: 1,839; 493130: 542; 312 grain co-ops). No neutral queue cost | — | N-K05, N-M27, N-M41, N-E13 |
| C-40 Household moves | K4, K5, K11 | $46-276M ($23M) → **$44-194M ($18.4M)** | Revenue base: $15.3B → **$10.8B** for the household share (Economic Census 2017: 70.6%, *verified*). Estimating cost, low end → **$163.9M** for interstate moves (FMCSA ICR, *verified*) | Claims 1-2%; estimating cost, high end 3%; removable shares | **K4:** household revenue and interstate estimating cost now come from named data. The split of revenue between local and long-distance moves is not published | **CPS movers weighted by revenue: 2008-09 -12.7% to -27.8%**, depending on the split [our call] (mostly 13-20%). **2022-25: -8.4% to -9.1%** | N-M39, N-M40, N-J18, N-K05 |

---

## 2. Card by card

### C-27 · Cross-border produce at Nogales and Pharr

**Open at S2:** K5 ($7-82M; central $5M), K6, K7.

**K5: volume (replaced).**
- **Old:** 60-85% of 604k Mexican produce loads, i.e. 362-513k loads **[our call]**.
- **New:** USDA Market News movement data give the two gateways directly (N-J06, re-queried; *verified*). The units are 10,000 lb:

  | Year | All Mexico crossings | Nogales | Pharr | Nogales + Pharr share | Loads at 40,000 lb **[our calc]** |
  |---|---|---|---|---|---|
  | 2021 | 2,414,098 | 618,946 | 780,643 | 58.0% | 350k |
  | 2022 | 2,374,439 | 575,440 | 788,982 | 57.5% | 341k |
  | 2023 | 2,498,060 | 632,330 | 839,824 | 58.9% | 368k |
  | 2024 | 2,397,514 | 585,848 | 833,407 | 59.2% | 355k |
  | 2025 | 2,383,341 | 570,314 | 886,260 | 61.1% | 364k |

- **Range used:** 355k (2024) to 368k (2023) loads, the last three years.
- **Cross-checks:**
  - The 2025 all-Mexico total (11.9M short tons) matches AgRTQ's 12.07M tons (N-K12) within 1.3% **[our calc]**.
  - Pharr's 8.86B lb in 2025 matches the bridge's own claim of "more than 8.9 billion pounds" (N-M43, *assumed*).
  - The districts are separate ports (Laredo 12.5%, Otay Mesa 12.1% and others), so nothing is counted twice.

**K5: cost per load (not replaced).**
- $100-400 of avoidable cost a load **[our call]**, for extra cold-storage days, inspection holds, reefer waiting and quality loss. No neutral per-load figure was found.
- **Cross-check from the World Bank** (Doing Business 2020, data year 2019; N-M05, *verified*; method N-M06). For a road shipment between Mexico and the US:
  - documentary compliance: $60 for the Mexican export (8 hours) + $100 for the US import (7.5 hours) = **$160 a shipment**;
  - border compliance: $400 (20.4 hours) + $175 (1.5 hours) = **$575**.
  - The case is 15 tonnes of auto parts worth $50,000, not produce.

**K5: removable share:** 20-40% **[our call]**, unchanged.

**Arithmetic [our calc]:**
- Low: 355,000 × $100 × 20% = **$7.1M**. 10% of it = $0.7M.
- High: 368,000 × $400 × 40% = **$58.9M**. 35% of it = **$20.6M**, about 18% short of $25M.
- Central fee pool: 20% × √(7.1 × 58.9) = **$4.1M** (old $5M).
- **Variant [our call on structure].** S2's C-27 cost counts delays and holds but not the document work itself, while C-25 counts document work as a separate part. Adding the World Bank's $160 of document cost a crossing, with C-25's 10-20% removable share:
  - that part adds 355,000 × $160 × 10% = $5.7M to 368,000 × $160 × 20% = $11.8M;
  - total **$12.8-70.7M**; central $6.0M;
  - 35% of $70.7M = **$24.7M, within 2% of $25M** ("about").

**K6: how much of the border cost is paperwork.**
- In the World Bank's case, documents are **22% of the per-shipment cost** ($160 of $735) and **41% of the time** (15.5 of 37.4 hours) **[our calc]**. Produce adds USDA, APHIS and FDA inspection steps, so the paperwork share for produce may differ.
- Other evidence points to physical and government drivers:
  - About 60M lb of the roughly 6B lb of produce entering through Nogales becomes unsellable each year. The reasons named are cosmetic defects, time stuck at the crossing, and a fall in the market price (The Counter, 2019, quoting a local food bank; N-M20, *assumed*).
  - Nogales lacked a cold inspection facility, "likely a contributing factor" in shippers routing berries and avocados through other ports (University of Arizona extension, 2018, revised 2019; N-M21, page extraction). That is a physical fix.
- **Reading:** a separable paperwork part exists, about a fifth of the cost on the World Bank's measure. Most of the cost is inspection, handling and spoilage.

**K7:**
- FAST lanes and unified processing brought average truck crossings to 31 minutes at Ysleta-Zaragoza, "19 minutes quicker than" non-FAST lanes (Texas A&M CIITR, 2020; N-M22, page extraction).
- But FAST is a Customs program with its own lanes, not software.
- Whether importers would credit software for shorter holds cannot be shown at the desk. **Open for S5.**

**Buyer counts at Pharr:** not found.
- The Texas International Produce Association says it represents "over 400 companies" across the chain (N-M43; trade association, snippet, *assumed*).
- Nogales had "over 85" distributors in a 2013 study (N-G17, *assumed*).

### C-31 · Livestock hauling

**Open at S2:** K5 ($11-70M; generous case $24.5M), K11 (cattle slaughter -13.8% in 2022-25).

**K5: loads.** 2.5-3.5M **[our calc]**, unchanged. The three weightings below give 3.10-3.53M loads for 2025 **[our calc]**.

**K5: admin and compliance cost per load: $15-40 [our call], not replaced.** What the regulator's own data say about the "papers" part:
- **ICVIs.** APHIS's burden sheet for animal disease traceability (OMB 0579-0327, submitted Aug 2026; N-M03, *verified*) counts:
  - 87,500 ICVIs a year completed by private respondents at 0.25 hours each;
  - 52,000 handled by states at 0.2 hours each;
  - an average wage of $34.40 an hour.
  - The Federal Register notice gives the whole collection: 947,082 responses and 536,091 hours a year (N-M02, *verified*).
- **So [our calc]:**
  - one ICVI costs about 0.25 × $34.40 = **$8.60** of time;
  - ICVIs cover about 87,500 ÷ 3.1M = **2.8% of loads**, because most moves are within a state, go direct to slaughter, or are exempt;
  - averaged over all loads, that is **$0.24 a load**.
- **Brand-inspection fees:** $1 a head in Montana; $0.65 a head for cattle consigned to licensed markets in Colorado (state pages via snippet; N-M42, *assumed*). These are government fees, and software cannot remove them.
- **Reading:** on the regulator's numbers, papers are a small slice of the $15-40. The rest (dispatch calls, driving-hours exemption tracking) has no neutral source. The evidence leans toward the low end, but no sourced input replaces the range.
- **Hauler time studies:** not found.

**K5: removable share:** 30-50% **[our call]**.

**Arithmetic [our calc]:** unchanged at $11.2-70.0M. The generous case is 35% × $70.0M = **$24.5M** ("about"). Central fee pool $5.6M.

**K11: card-level unit built.**
- **Unit:** livestock loads = cattle slaughter × moves ÷ head per load, plus hog slaughter × moves ÷ head per load.
- **Data:** USDA PSD calendar-year slaughter (cattle N-J05; hogs N-M01, same file; *verified*).
- **Weightings [our call]:**
  - S2's: cattle 2.5 moves and 50 head a load; hogs 2.5 moves and 200 head. Cattle are 48% of loads.
  - Cattle-heavy: cattle 3 moves and 40 head; hogs 2 moves and 200 head. Cattle 64%.
  - Hog-heavy: cattle 2 moves and 60 head; hogs 3 moves and 170 head. Cattle 31%.

| Series **[our calc]** | 2008-09 | 2022-25 | Band |
|---|---|---|---|
| Cattle slaughter alone (S2) | 2008 35,508k → 2009 34,468k: **-2.9%** | 2022 34,812k → 2025 30,022k: **-13.8%** | ≤13% / 13-20% |
| Hog slaughter alone | 2008 116,452k → 2010 110,260k: **-5.3%** | 2021 128,986k → 2023 127,971k: **-0.8%** | ≤13% / ≤13% |
| Loads, S2 weights | 2008 → 2011: **-2.8%** | 2021 → 2025: **-6.8%** | ≤13% / ≤13% |
| Loads, cattle-heavy | 2008 → 2009: **-2.8%** | 2021 → 2025: **-8.6%** | ≤13% / ≤13% |
| Loads, hog-heavy | 2008 → 2010: **-3.6%** | 2021 → 2025: **-4.6%** | ≤13% / ≤13% |

- **Result:** every weighting of the card-level unit falls in the pass band in both windows. Only cattle alone sits in the unknown band. It follows the herd cycle (check J), and it is a candidate segment note.
- **Notes:**
  - Annual data only; monthly slaughter was not checked.
  - Feeder-pig imports (6.5-7.0M head a year in 2021-25, rising) end up in slaughter counts, so they are not added separately.
  - Sheep and goats are left out as small.
  - PSD forecasts 29.1M cattle for 2026, outside the window.

### C-35 · Tank loads: hazmat papers and tank-wash certificates

**Open at S2:** K4, K5 ($9-227M; central $9M), K7, K11.

**K4/K5: tank-load tonnage (low end replaced).**
- **Old:** 20-35% of 1,067M hazmat truck tons **[our call]** ÷ 25 tons = 8.5-15M loads.
- **New:** the 2022 Commodity Flow Survey's hazmat table by hazard class and mode (CF2200H07; N-M19, *verified*):
  - hazmat by truck: **1,307.9M tons** (for-hire 633.4M; company-owned 432.6M; the rest is truck with type not split);
  - Class 3 flammable liquids by truck: **1,040.0M tons (79.5%)**, mostly fuels, which belong to C-38;
  - everything else by truck: **267.9M tons**. That is gases 156.0M (of which flammable gas, mostly propane, 60.8M, and non-flammable gas 94.3M), corrosives 70.5M, miscellaneous 23.3M, and other classes 18.2M.
- **Low:** non-Class-3 tons minus flammable gas = **207.1M tons** **[our calc]**. Counting flammable gas as fuel is **[our call]**.
- **High:** S2's 373M tons is kept **[our call]**. Non-fuel Class 3 chemicals (solvents, alcohols) and the card's non-hazardous food liquids are not in the class split.
- **Loads at 25 tons:** 8.28-14.92M **[our calc]**.
- **Caveat:** CFS tons also include packaged hazmat, not only tank loads.

**K5: paperwork per load (replaced).**
- **Old:** 10-20 minutes of clerk time, $3-8 **[our call]**.
- **New:** PHMSA's supporting statement for OMB 2137-0034 (the collection expired in 2015; N-M04, *verified*):
  - "Each shipping paper, with emergency response information, will take approximately 1 minute and 30 seconds";
  - it values a paper at "$1.00" and a preparer at "$25.00" an hour;
  - it estimates "as many as 260 million shipments per year".
- **New range:** $0.56 (1.5 minutes at the BLS clerk mean of $22.50 an hour, N-K09) to $1.00 (PHMSA's own cost) **[our calc]**.

**K5: wash mismatch and rejected loads:** $2-30 a load **[our call]**, unchanged. No neutral rate was found; the only prices are forum figures for a wash (N-K40, *assumed*).

**K5: removable share:** 20-40% **[our call]**.

**Arithmetic [our calc]:**
- Low: 8.28M × ($0.56 + $2) × 20% = **$4.2M**.
- High: 14.92M × ($1.00 + $30) × 40% = **$185.0M**. 35% of it = $64.8M.
- Central fee pool: **$5.6M** (old $9.0M).
- The high end now rests almost entirely on the wash-mismatch judgement.

**K4:** loads and paperwork cost now come from named data. The mismatch rate, which drives most of the pool, is still a judgement.

**K7:** no data on how often loads are refused, or fines paid, over papers or wash mismatches. Open for S5.

**K11: which series is closest to tank-truck loads.**
- No public physical series of tank-truck loads was found. Neither ATA nor NTTC publishes one that turned up.

| Series | 2008-09 | 2022-25 | What it measures |
|---|---|---|---|
| **Chemicals excluding pharmaceuticals** (Fed G.17 code G325@4), monthly, seasonally adjusted | Sep 2007 123.2 → Jan 2009 90.1: **-26.9%** | Jul 2021 97.8 → Jan 2024 88.3: **-9.7%** | output volume index |
| the same, annual averages | 2007 120.3 → 2009 94.1: **-21.8%** | 2021 93.5 → 2023 91.5: -2.1% | |
| All chemicals, G325 (S2) | -18.4% | -7.5% | includes pharmaceuticals |
| Basic chemicals, G3251 (S2) | -35.8% | -9.6% | |
| Pharmaceuticals, G3254 | Dec 2006 → Jul 2010: -18.9% | -7.8% | rarely moves in tank trucks |
| Chemicals by rail, STCC 28 (S2, N-J09) | **-8.8%** | **-1.2%** | physical count of loads, by rail |

- **Labels:** values are read from the Fed's file (N-M17, *verified*). The meaning of G325@4 comes from FRED's title for its series "Chemicals Except Pharmaceuticals and Medicines (NAICS = 3251-3,5-9)" (N-M18, snippet, *assumed*). FRED's quoted Q4 2025 value (91.65) is within 0.2 of the file's.
- **Reading:**
  - The closest measure of what fills the tanks, chemicals excluding pharma, is in the **fail band** for 2008-09 on both monthly and annual data. It is closer to the unit than S2's G325, because pharmaceuticals rarely move in tank trucks.
  - The closest physical count of chemical loads, rail carloads, is in the **pass band**. But rail carries longer, contract bulk flows.
  - The two still point in opposite directions, as at S2.

### C-24 · Export documents for farm and food exporters

**Open at S2:** K3, K4, K5 ($23-114M; central $10M), K7, K11.

**K3: who the buyers are.**
- Census, *A Profile of U.S. Importing and Exporting Companies, 2022-2023* (N-M07, *verified*): identified exporters in 2023 by company industry.

  | NAICS | Exporters | Of which small or mid-sized |
  |---|---|---|
  | 111 crop production | 2,407 | 2,390 |
  | 112 animal production | 415 | 410 |
  | 311 food manufacturing | 3,033 | 2,651 |
  | 312 beverage and tobacco | 1,275 | 1,228 |
  | **Total [our calc]** | **7,130** | **6,679** |

- **Plus** an unknown share of the 22,481 exporters among nondurable-goods wholesalers (424), which include grain merchants and grocery wholesalers.
- Census counts the firms but doesn't name them. Channels such as USDA's cooperator groups and the state regional trade groups are *assumed*; they were not researched.

**K4/K5: containers (now verified).**
- **Old:** 285,000 TEU a month, from a snippet (N-K33, *assumed*), giving 1.9M boxes.
- **New:** USDA AMS *Port Profiles by Commodity* (N-M11, *verified*). Containerized farm exports:
  - 3.52M TEU (2021), 3.37M (2022), 3.22M (2023), 3.34M (2024), 3.41M (2025);
  - the 2021-24 average is 280k TEU a month, which confirms N-K33.
  - At 1.8 TEU a box **[our call]**, that is **1.79-1.95M boxes a year** **[our calc]**.

**K4/K5: cost per container (low end replaced).**
- **Old:** $40-120 **[our call]**.
- **New low:** **$60**, the World Bank's documentary compliance for a US export (Doing Business 2020, data year 2019; N-M05, *verified*). It includes forwarder and broker document fees and certificates of origin (N-M06), and takes 1.5 hours.
- **High:** $120 is kept **[our call]**: the $60 plus up to $60 for holds, bank fees for document discrepancies, and re-issues.
- **Other sourced pieces (context):**
  - **Export filing:** "3 minutes per AES transaction", for 17,025,219 transactions a year (Census ICR 0607-0152, Federal Register 19 Sep 2023; N-M08, *verified*). That is about $1.1-1.7 a filing **[our calc]**. The filing is already electronic and cheap.
  - **Phytosanitary certificate:** "$106" per commercial certificate (N-M09, *verified*). This is a government fee, which software can't remove, so it is left out.
    - PPQ issued "more than 643,000" federal certificates in its 2024 fact sheet, and "more than 699,900" in 2018 (N-M10, snippets, *assumed*).
  - **Letter-of-credit share of US farm exports:** not found.

**K5: removable share:** 30-50% **[our call]**.

**Arithmetic [our calc]:**
- Low: 1.79M × $60 × 30% = **$32.2M**.
- High: 1.95M × $120 × 50% = **$117.3M**. 35% of it = $41.0M.
- Central fee pool: **$12.3M** (old $10M).

**K7:** most of the saving is holds and rejections avoided. The desk cannot count it. USDA's electronic phytosanitary certificates (ePhyto) already cover part of the certificate step (N-J34). Open for S5.

**K11:**

| Series | 2008-09 | 2022-25 | Band |
|---|---|---|---|
| All containerized farm exports, TEU (N-M11) | no data (series starts 2010) | 2021 3,517,866 → 2023 3,218,487: **-8.5%** | no data / ≤13% |
| the same, metric tons | no data | 2021 39.2M → 2023 36.2M: -7.6% | |
| Containerized grain only, TEU (N-M12) | no data (starts 2010) | 2021 764k → 2023 815k: **rose** | |
| Bulk farm exports (S2 proxy, N-J05) | -19.7% | -11.8% | 13-20% / ≤13% |

- **2022-25:** the direct unit is in the pass band.
- **2008-09:** no count was found. Snippets say ocean container rates hit historic lows in 2009, and that grain moving in containers grew from 2004 to 2011 (N-M44, *assumed*). That points to a smaller fall than bulk's, but gives no number. "No data" is unknown under Test 3.

### C-26 · Produce reefer booking and rejected loads

**Open at S2:** K4, K5 ($10-274M; central $11M).

**Volume:** 1.71M loads, *verified* at S2 (N-K12).

**Rejection rate, 1-4% [our call]: no neutral rate found.**
- **ReFED** (a nonprofit): "Based on expert interviews, ReFED assumed that 2.00% of all produce and nuts shipments are rejected by the quality assurance teams of produce buyers". ReFED rates this "Very Low" in data quality (N-M24; page read, but the figure is itself an assumption, so *assumed*).
- **USDA PACA disputes:** "approximately 3,350 PACA claims involving more than $63 million" were resolved over three years (USDA blog via snippet; the page returned 403; N-M25, *assumed*).
  - That is about 1,117 claims a year and about $18,800 a claim **[our calc]**, or about **0.07% of loads**.
  - It is a floor: it counts only disputes that reach USDA.
  - Filing costs $100 for an informal complaint and $500 for a formal one (N-M26, *verified*).
- **AMS destination-inspection counts:** not found.

**Loss per rejected load, $3-10k [our call]:** no neutral figure. The average PACA claim of about $19k (the gross amount disputed; *assumed*) fits a net loss in this range.

**Arithmetic [our calc]:**
- Unchanged: **$10.3-273.6M**; central **$10.6M**.
- **Sensitivity:** with ReFED's 2% as the high rejection rate, 1.71M × 2% × $10k × 40% = $136.8M. The range becomes $10-137M, central $7.5M.

**K4:** stays open. The only systematic rejection estimate is ReFED's expert-interview assumption.

### C-29 · Buying rail and barge freight for grain

**Open at S2:** K5 ($36-109M; central $13M), K6, K7, K11.

**K5/K6: is there a timing premium that software could capture?**
- **Secondary railcar bids** (USDA AMS data via AgTransport; N-M14, *verified*). Weekly average bids for guaranteed shuttle-train freight in the near month, by railroad, 2015-2025 **[our calc]**:
  - yearly means run from **-$189 to +$1,354 a car**;
  - within-year standard deviations run from **$151 to $1,200 a car**, typically $250-550;
  - weekly extremes run from -$675 to +$4,354.
- **Reading:** S2's software-capturable premium of $20-60 a car is about 4-24% of a typical within-year standard deviation **[our calc]**. That is context only; the premium stays **[our call]**.
- **Peer-reviewed work:**
  - Wilson (2021, *Agribusiness* 37:472-488; N-M15, abstract via Crossref, *verified*): "the export basis and rail‐car values in the secondary market are determined simultaneously".
  - Bullock et al. (2025, *Agribusiness*; N-M16, abstract, *verified*) build a Monte Carlo optimization whose "primary decision variable was the number of shuttle trains to purchase in the rail market", noting "the significance of primary and secondary railcar markets for risk management".
- **K6 reading:** the cost is a market price. But peer-reviewed work treats how many cars to buy and when as a decision problem, so a separable information lever exists. Its size is not measured.
- **K7 reading:** the benchmark moves by hundreds of dollars a car within weeks, so a saving is hard to attribute. Open for S5.
- **Range:** unchanged at $36-109M; central $12.5M.

**K11: card-level unit built: grain tons moved by rail and barge.**
- **2008-09:** USDA's *Transportation of U.S. Grains: A Modal Share Analysis* data (N-M13, *verified*). Rail + barge: 2006 219.5M tons → 2011 198.0M tons, **-9.8%** **[our calc]**. The years between: 2008 205.5, 2009 205.5, 2010 217.0.
- **2022-25:** the modal-share data end in 2022. So the two S2 series were combined, each mode's index weighted by its 2021 or 2022 tonnage **[our calc]**:

  | Rail series used | Barge series | Peak → trough | Change |
  |---|---|---|---|
  | STB weekly Class I originated grain carloads (N-J08, re-queried: 2021 1,347,129; 2022 1,313,601; 2023 1,178,500) | USACE tons at Mississippi Locks 27, Ohio Olmsted and Arkansas Lock 1 (N-J07, re-queried: 2021 36.74M; 2022 32.73M; 2023 26.29M) | 2021 → 2023 | **-18.2%** (2021 weights) / **-17.9%** (2022 weights) |
  | STB Waybill Sample, all railroads (N-J09: 2022 1,347,682; 2023 1,304,710) | same | 2022 → 2023 | **-8.4%** |

- **Reading:** the rail series decides the band: 13-20% with the weekly series, ≤13% with the waybill sample.
  - The two rail series disagree for 2022 → 2023: -10.3% weekly against -3.2% in the sample.
  - The weekly series counts Class I originations only; the sample counts all railroads.
  - They are two different series, not one series at two frequencies, so the "finer data decides" practice doesn't settle it.

### C-32 · Milk pickup and hauling settlement

**Open at S2:** K5 ($29-148M; central $13M).

**Counts:**
- **Co-ops:** USDA Rural Development's bulletin on 2024 cooperative statistics (N-M27, page extraction):
  - 1,620 farm co-ops in 2024 (1,647 in 2023);
  - "milk and milk products" were the major commodity of **93** co-ops;
  - grain and oilseeds of 312.
- **Milk haulers:** not found. Wisconsin, Minnesota and Pennsylvania publish license lists, but no totals were read.

**Removable share, 3-8% [our call]: not replaced.** No US peer-reviewed routing study with a savings percentage was found.
- **US:** Cornell's Sehulster and Pratt (1983), *Potential Savings in Farm Milk Pickup Costs from Eliminating Route Duplication and Using Improved Scheduling Techniques* (N-M30). The title was found; the PDF was blocked.
- **Non-US cases (context):**
  - A Brazilian co-op with 461 farms: optimized costs differed from current routes by "about 3%", described as "within the range reported in the literature" (MDPI, 2019, snippet; N-M29, *assumed*).
  - An Indian co-op cut route distance from 1,445 to 1,350 km (6.6%) and costs by 6% (snippet; N-M29, *assumed*).
  - A 2024 journal article reports "dropping about 16% of total travel time" (N-M28, abstract via Crossref, *verified*; a lower-tier journal).
- **Reading:** in these cases routing saves 3-16% of distance or time. Hauling charges also cover fixed costs, so S2's 3-8% of the whole charge sits inside that span.

**Arithmetic:** unchanged at **$29-148M**; central **$13.1M**.

### C-38 · Fuel delivery reconciliation

**Open at S2:** K5 ($28-164M; central $13M).

**Marketer count (replaced).**
- SUSB 2022 (N-K05, re-parsed; *verified*):
  - petroleum and petroleum-products merchant wholesalers (4247): **3,596 firms**. That is bulk stations (424710) 1,993 and others (424720) 1,763; some firms are in both 6-digit rows.
  - fuel dealers (454310): **4,083 firms**.
- Together: **7,679 firms** **[our calc]**, close to PMAA's "8,000" (N-K38, *assumed*).

**Cost and error rates (context; none gives a cost per load):**
- **NIST Handbook 44 (2026), §3.31:** meters on fuel trucks delivering petroleum (accuracy class 0.3) have an acceptance tolerance of 0.15% and a maintenance tolerance of 0.3% (N-M31, *verified*). On an 8,500-gallon load, 0.3% is ±25.5 gallons **[our calc]**.
- **Maryland Department of Agriculture, FY2012:** "1,104 vehicle tank and rack meters, with 12 percent in violation"; "1,294 inspections of delivery tickets, with 0.7 percent in violation" (N-M32, page extraction).

**Cost per load, $5-15 [our call]:** not replaced.

**Arithmetic:** unchanged at **$28-164M**; central **$13.6M**.

### C-25 · Cross-border Mexico truckloads through Laredo

**Open at S2:** K5 ($50-177M; central $19M), K7. Check L covers its K11.

**K5: paperwork cost per crossing (replaced).**
- **Old:** $50-150 **[our call]**.
- **New:** **$160** = the Mexican export's documentary compliance of $60 (8 hours) + the US import's documentary compliance of $100 (7.5 hours). Source: World Bank Doing Business 2020, data year 2019 (N-M05, *verified*).
  - Doing Business counts customs-broker and forwarder document fees under documentary compliance (N-M06).
  - Border compliance is separate and not added: $400 for the Mexican export (20.4 hours) and $175 for the US import (1.5 hours).
- **Caveats:**
  - The case is one shipment: 15 tonnes, worth $50,000, by the most-used mode.
  - The World Bank discontinued Doing Business in 2021 after finding data irregularities for some other countries (*assumed*, from memory).

**K5: loaded trucks.**
- BTS's 2024 series gives only "Trucks": 3,026,632 at Laredo (N-K06).
- Its metadata doesn't say whether empty trucks are counted, and the older loaded/empty split is no longer in the dataset.
- The low end assumes 70% loaded **[our call]**; the high end uses every truck.

**K5: removable shares:** 10-20% of paperwork and 10-25% of delay **[our call]**, unchanged. Delay cost $345M (N-K18, unchanged).

**Arithmetic [our calc]:**
- Paperwork: low 3,026,632 × 70% × $160 × 10% = $33.9M; high 3,026,632 × $160 × 20% = $96.9M.
- Delay: $345M × 10-25% = $34.5-86.3M.
- **Total: $68.4-183.2M.** 35% of the high end = $64.1M. Central fee pool **$22.4M** (old $19M).
- Without the loaded-share cut, the low end is $82.9M.

**Do ready documents shorten crossings?**
- FAST plus unified processing: 31 minutes at Ysleta-Zaragoza, "19 minutes quicker than" non-FAST lanes (CIITR, 2020; N-M22, page extraction).
- TTI's crossing-time page for Laredo's World Trade Bridge showed FAST 13 minutes against non-FAST 15 minutes (a snapshot, seen only in a search summary; the page returned an error; N-M23, *assumed*).
- **Reading:** pre-cleared crossings are 2-19 minutes shorter, 13-38% of crossing time **[our calc]**. But FAST is a Customs trusted-trader program, not software. The 10-25% removable delay stays **[our call]**.

**K7:** Customs controls inspection time. Whether shippers would credit software for a shorter crossing is open for S5.

### C-30 · Rail demurrage and accessorial invoices

**Open at S2:** K5 ($40-236M; central $19M). Check L covers its K11.

**Class I demurrage in 2022-25.**
- No STB series after Q1 2022 was found, and railroads do not report demurrage alone. The nearest lines in their filings:
- **CSX "other revenue":** regional subsidiary railroads plus incidental charges, including demurrage, intermodal storage and switching (CSX 10-Ks for 2022 and 2024; N-M34, N-M33, *verified*).

  | Year | Other revenue |
  |---|---|
  | 2021 | $744M |
  | 2022 | $908M |
  | 2023 | $578M |
  | 2024 | $499M |

  - 2022: "$164 million higher ... driven by increases in revenue for intermodal storage and equipment usage, increases in demurrage".
  - 2024: "$79 million lower, primarily resulting from lower carload demurrage and other items".
- **Union Pacific "accessorial revenues":** $779M (2022), $584M (2023), $554M (2024) (10-K figures via snippet; *assumed*). Q2 2024 was $131M against $149M in Q2 2023 (10-Q, page extraction) (N-M35). UP's line also covers intermodal and container charges.

**Reading [our calc; applying these scalings is our call]:**
- S2's high input, $1.57B, is the 2021 peak pace.
- Scaling it by CSX's change from 2021 to 2024 (×0.67), or UP's from 2022 to 2024 (×0.71), gives **$1.05-1.12B for 2024**.

**Arithmetic [our calc]:**
- Low: $0.8B × 5% = **$40M** (S2's 1%-of-revenue call, unchanged).
- High: $1.12B × 15% = **$167.5M**. 35% of it = $58.6M.
- Central fee pool: **$16.4M** (old $19M). S2's $40-236M stays as the peak-year version.

**Disputed or waived share:** not found. The STB's 2019 hearing (EP 754) recorded shipper complaints about thin invoice information and disputes over ordered-in dates, but no share (N-M45, *assumed*).

### C-34 · Oversize and overweight permits

**Open at S2:** K4, K5 ($39-260M; central $20M), K11.

**K4/K5: national permit count (replaced).**
- **Old:** Texas taken as 15-25% of US permits **[our call]**, giving 3.1-5.2M.
- **New:** FHWA's *Comprehensive Truck Size and Weight Limits Study*, Compliance Comparative Analysis Technical Report, Table 18 (N-M36, *verified* from the page's HTML). Permits issued by the 44 states that reported every year:

  | Permit type | 2008 | 2009 | 2010 | 2011 | 2012 |
  |---|---|---|---|---|---|
  | Non-divisible trip | 3,411,636 | 2,987,590 | 3,222,452 | 3,446,444 | 3,490,566 |
  | Non-divisible annual | 263,082 | 244,736 | 242,776 | 260,290 | 272,939 |
  | Divisible trip | 65,401 | 89,703 | 79,236 | 97,389 | 88,918 |
  | Divisible annual | 358,731 | 359,201 | 503,871 | 369,897 | 383,333 |
  | **Total** | **4,098,850** | **3,681,230** | **4,048,335** | **4,174,020** | **4,235,756** |

- **Six states** did not report: +0-15% **[our call]**, giving **4.24-4.87M permits a year** on a 2012 basis.
- **Check:** Texas's FY2025 count of 776,696 (N-K07) is 16-18% of that **[our calc, mixing years]**.

**K5: cost and removable share:** $50-100 a permit and 25-50% **[our call]**, unchanged.
- **Context:** FHWA's 2017 permitting study found "30 States currently using Automated Permit Systems, 6 States in various stages of using Automated Permit Systems, and 13 States that have no imminent plans" (self-issue, single-trip), and 20 states that auto-issue at the industry's harmonized thresholds (N-M37, *verified* from the page's HTML).
- So state portals already self-issue in most states. That argues the high removable share is generous.

**Arithmetic [our calc]:**
- Low: 4.24M × $50 × 25% = **$52.9M**.
- High: 4.87M × $100 × 50% = **$243.6M**. 35% of it = $85.2M.
- Central fee pool: **$22.7M** (old $20M).

**K4:** the count now comes from named federal data, though it dates from 2012. The cost per permit is still anchored on vendor prices.

**K11:**
- **2008-09:** the 44-state total fell **-10.2%** from 2008 to 2009 **[our calc]** (non-divisible trip permits -12.4%), and was back above 2008 by 2011.
  - The table's own printed percentages are slightly different (-11% and -14%).
  - The series starts in 2008, so a peak in 2005-2007 is not covered.
- **2022-25:** no national series.
  - Washington: about 175,220 (2022) → 183,502 (2023), a rise (N-J23).
  - Texas: 742,594 (FY2023; TxDMV budget via snippet, N-M38, *assumed*) → 776,696 (FY2025, N-K07), a rise.
- **Test 1, substitutes:** 30 states already ran automated self-issue systems in 2017. That bears on the permit-service side; it is not evidence that the whole job is substituted at scale.

### C-28 · Harvest grain hauling and scale tickets

**Open at S2:** K5 ($34-314M; central $21M).

**Elevator companies:**
- SUSB 2022 (N-K05, re-parsed; *verified*):
  - grain and field bean merchant wholesalers (424510): 1,839 firms at 4,481 sites;
  - farm product warehousing (493130): 542 firms at 774 sites.
- USDA RD: 312 grain and oilseed co-ops in 2024 (N-M27).
- NASS: 7,922 off-farm storage sites (N-E13).
- So roughly **1,800-2,400 elevator companies** **[our calc; the codes overlap]**.

**Queue cost per load:** no neutral source.
- UGPTI's farm-truck surveys for USDA (Central Plains 2023, DP-321; Northern Plains 2015, DP-284; N-M41) report haul distances (14.9 miles to the first-choice delivery point in the Central Plains), but no waiting times turned up in a text search.
- A vendor's "2-4 hours" (N-K36, *assumed*) is still the only figure.

**Arithmetic:** unchanged at **$34-314M**; central **$20.7M**.

### C-40 · Household moves

**Open at S2:** K4, K5 ($46-276M; central $23M), K11.

**Which moves small movers handle.**
- Economic Census 2017, products by industry, for movers (484210; N-M40, *verified*):

  | Product line | Revenue | Share |
  |---|---|---|
  | All lines | $15.62B (8,454 establishments) | 100% |
  | Household moving | $11.02B | 70.6% |
  | Commercial moving | $1.72B | 11.0% |
  | Warehousing and storage | $0.88B | 5.7% |
  | Packing | $0.52B | 3.3% |
  | Special handling | $0.46B | 2.9% |

- The split between local and long-distance household moves is **not published**.

**Estimating cost (low end replaced).**
- FMCSA's household-goods ICR (OMB 2126-0025, supporting statement of June 2025; N-M39, *verified*):
  - "558,851 for-hire interstate household goods moves occur each year";
  - shippers get "on average, three" estimates, so movers write "1,676,553 cost estimates each year";
  - each takes 2 hours: 3,353,106 hours at a loaded wage of $48.88, or **$163.9M a year**;
  - a bill of lading takes 0.5 hour a shipment;
  - there are 7,861 household-goods carriers.
- This covers **interstate moves only**. Local moves are not regulated by FMCSA.

**Revenue base:** household share 70.6% × $15.3B (receipts of firms under 500 staff, 2022) = **$10.8B** **[our calc; applies a 2017 share to 2022 receipts]**.

**Arithmetic [our calc]:**
- **Claims:** 1-2% × $10.8B = $108-216M **[our call on the rate]**. No neutral claims ratio was found.
- **Estimating:** low $163.9M (FMCSA, interstate only); high 3% × $10.8B = $324M **[our call]**.
- **Removable shares:** claims 10-30%; estimating 20-40% **[our call]**.
- Low: $108M × 10% + $163.9M × 20% = **$43.6M**.
- High: $216M × 30% + $324M × 40% = **$194.4M**. 35% of it = $68.1M.
- Central fee pool: **$18.4M** (old $23M).

**K4:** household revenue and the interstate estimating cost now come from named data. The claims rate and the local share do not.

**K11: card-level unit built.**
- **Unit:** CPS movers (people, not moves; N-J18, re-read), weighted by the revenue share of long-distance moves **[our call]**.
- The 2005 different-state figure carries a footnote in the CPS table, so results are shown from both a 2005 and a 2006 base.

| Series **[our calc]** | 2008-09 | 2022-25 |
|---|---|---|
| Within-state movers (same county + different county) | 2006 32.86M → 2011 29.20M: **-11.1%** | 2021 22.22M → 2023 19.84M: **-10.7%** |
| Different-state movers | 2005 7.44M → 2010 4.32M: **-41.9%** (from 2006: -23.9%) | 2022 4.88M → 2023 4.49M: **-8.0%** |
| Weighted, 30% long-distance | -12.7% (2006 base) to -14.0% (2005 base) | -9.0% to -9.1% |
| Weighted, 50% long-distance | -13.7% to -20.3% | -8.7% to -8.8% |
| Weighted, 70% long-distance | -17.4% to -27.8% | -8.4% to -8.5% |

- **Reading:**
  - 2022-25 is in the pass band under every weighting.
  - 2008-09 is in the **13-20% band for most weightings**. It crosses 20% only with a 70% long-distance share, or a 50% share measured from the footnoted 2005 figure.
  - The missing local/long-distance revenue split keeps it unsettled.

---

## 3. For the coordinator (not a call)

**K5 against the lines.**
- **No card reaches the pass line.** The biggest new low end is C-25's $68M, against the $250M needed.
- **Every central fee pool is still under $25M:**
  - C-27 $4.1M; C-31 $5.6M; C-35 $5.6M; C-26 $10.6M; C-24 $12.3M; C-29 $12.5M; C-32 $13.1M; C-38 $13.6M; C-30 $16.4M; C-40 $18.4M; C-28 $20.7M; C-25 $22.4M; C-34 $22.7M.
  - Under the S3a exit rule, a card that stays open on K5 with a central pool under the floor goes to the reserve list.
- **Closest to the fail line: C-27.**
  - With the gateway volume now sourced, its high end is $58.9M, and 35% of that is $20.6M, about 18% short of $25M.
  - If the card also counts the World Bank's document cost (as C-25 does), the high end becomes $70.7M. 35% of that is $24.7M, which is "about" $25M.
  - Which structure applies is a scoping question for the coordinator.
- **Moved up:** C-24, C-25, C-34.
- **Moved down:** C-27, C-35, C-40, and C-30 as a 2024-scaled sensitivity.
- **Unchanged,** because no sourced replacement was found: C-26, C-28, C-29, C-31, C-32, C-38.
- **The share software could remove is still [our call] on all 13 cards.** It remains the main swing, and only S5 can measure it.

**K11: the units asked for.**
- **C-31:** the card-level unit (cattle + hog loads) is in the pass band in both windows under all three weightings. Cattle alone (-13.8%) was the source of S2's unknown.
- **C-29:** 2008-09 is in the pass band (-9.8%). 2022-25 turns on the rail series: -17.9% to -18.2% with the weekly series, -8.4% with the waybill sample.
- **C-35:** chemicals excluding pharma is in the fail band for 2008-09 (-26.9% monthly, -21.8% annual). Rail chemical carloads are in the pass band (-8.8%). No tank-truck count exists.
- **C-24:** 2022-25 is in the pass band (-8.5%). 2008-09 has no count.
- **C-34:** 2008-09 is -10.2%, but the window before 2008 is not covered. 2022-25 rose in the two states with data.
- **C-40:** 2008-09 is 13-20% for most weightings; 2022-25 is ≤13%. The revenue split is the missing input.

**Other unknowns.**
- **K3 C-24:** a count exists: 7,130 farm and food exporters plus part of 22,481 wholesalers. Reach through commodity groups is not evidenced.
- **K4:**
  - Now built on named data: C-24 (volume and cost), C-34 (count, though dated), C-40 (revenue lines and interstate estimating cost), and C-35 (loads and paperwork).
  - C-35's pool still rests on the wash-mismatch judgement.
  - C-26 has no neutral rejection rate.
- **K6:**
  - C-27: paperwork is about a fifth of the border cost on the World Bank's measure.
  - C-29: an information lever exists (how many cars to buy, and when), but the market price dominates.
- **K7:** C-24, C-25, C-27, C-29 and C-35 remain questions only customers can answer (S5).

**Not done:** the K11 Test 2 flag for customer survival (not in this brief). Check L covers K11 for C-25 and C-30.

---

## 4. Sources (new in this check)

All accessed 2026-09-15.

| ID | Source (author/org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-M01 | USDA FAS, PSD Online livestock file (same download family as N-J05; swine rows new) | downloaded 2026-09-15 | https://apps.fas.usda.gov/psdonline/downloads/psd_livestock_csv.zip | download (CSV parsed) | US cattle and swine total slaughter, imports, production, 2004-2026 |
| N-M02 | Federal Register 2026-00097, APHIS, Animal Disease Traceability ICR notice | 7 Jan 2026 | https://www.govinfo.gov/content/pkg/FR-2026-01-07/pdf/2026-00097.pdf | download | 80,302 respondents; 947,082 responses; 536,091 hours; 0.566 hours per response |
| N-M03 | reginfo.gov ICR 202608-0579-003 (OMB 0579-0327): supporting statement and APHIS Form 71 burden sheet | Aug 2026 | https://www.reginfo.gov/public/do/PRAViewDocument?ref_nbr=202608-0579-003 (objectIDs 171689600, 171688700) | download (docx, xlsx parsed) | ICVI rows: 87,500 private responses at 0.25 hours; 52,000 state responses at 0.2 hours; average wage $34.40 |
| N-M04 | PHMSA, supporting statement, "Hazardous Materials Shipping Papers and Emergency Response Information" (OMB 2137-0034) | expiration 30 Sep 2015 | https://www.reginfo.gov/public/do/DownloadDocument?objectID=58951701 | download (Word file) | 1 minute 30 seconds per paper; $1.00 per paper; $25 an hour; up to 260M shipments a year; 4,625,846 hours |
| N-M05 | World Bank API, Doing Business (source 1), DB16-20 trading-across-borders indicators, USA and MEX | data year 2019 (DB2020) | https://api.worldbank.org/v2/country/USA;MEX/indicator/TRD.ACRS.BRDR.EXPT.COST.DOC.COMP.CD.DB1619?source=1&format=json&date=2019 (and 7 related series) | API query | US: documentary compliance $60/1.5 hours to export and $100/7.5 hours to import; border $175/1.5 hours. Mexico: documentary $60/8 hours (export), $100/17.6 hours (import); border $400/20.4 hours (export), $450/44.2 hours (import) |
| N-M06 | World Bank, Doing Business, "Trading across borders" methodology | archive | https://archive.doingbusiness.org/en/methodology/trading-across-borders | page extraction | What documentary and border compliance include; the case (15 tonnes, $50,000) |
| N-M07 | Census, *A Profile of U.S. Importing and Exporting Companies, 2022-2023* | 2025 release | https://www.census.gov/foreign-trade/Press-Release/edb/edbrel2023.pdf | download | Table 7a and the related tables: exporters by 3-digit NAICS (111, 112, 311, 312, 424), including small and mid-sized |
| N-M08 | Federal Register 2023-20227, Census, Automated Export System ICR (OMB 0607-0152) | 19 Sep 2023 | https://www.govinfo.gov/content/pkg/FR-2023-09-19/pdf/2023-20227.pdf | download | 17,025,219 responses; "3 minutes per AES transaction"; 851,261 hours |
| N-M09 | APHIS, "User Fees for Export Certification of Plants and Plant Products" | modified 25 Jan 2026 | https://www.aphis.usda.gov/user-fees/user-fees-export-certification-plants-plant-products | page extraction | $106 commercial; $61 non-commercial; $6 state administration fee |
| N-M10 | APHIS PPQ "by the numbers" 2024 and the 2018 PPQ report | 2024; 2018 | https://aphis.prod.usda.gov/sites/default/files/ppq-by-the-numbers-2024.pdf ; https://www.aphis.usda.gov/sites/default/files/report-ppq-2018.pdf | snippet (files not readable) | "more than 643,000" and "more than 699,900" phytosanitary certificates (*assumed*) |
| N-M11 | USDA AMS AgTransport, "Port Profiles by Commodity" (hpfj-zhfg) | 2010-2026 | https://agtransport.usda.gov/resource/hpfj-zhfg.json | API aggregates | Farm exports in containers and bulk by year: metric tons and TEU |
| N-M12 | USDA AMS AgTransport, "Containerized Grain data" (c353-2zjn) | 2010-2026 | https://agtransport.usda.gov/resource/c353-2zjn.json | API aggregates | Containerized grain exports: tons and TEU by year |
| N-M13 | USDA AMS AgTransport, "Modal Share Analysis Data" (59m9-gjrx), from *Transportation of U.S. Grains: A Modal Share Analysis* | 1984-2022 | https://agtransport.usda.gov/resource/59m9-gjrx.json | API aggregates | Grain tons by mode (rail, barge, truck) by year |
| N-M14 | USDA AMS AgTransport, "Secondary Railcar Auction Market Bids" (cvu8-kpyk) | 1997-2026 | https://agtransport.usda.gov/resource/cvu8-kpyk.json | API (full pull, 2015 on) | Weekly bids in $ a car by railroad, train type and month; mean, standard deviation, minimum and maximum **[our calc]** |
| N-M15 | W. W. Wilson, "Secondary rail car markets for grain transportation and basis values", *Agribusiness* 37:472-488 | online Dec 2020 | https://api.crossref.org/works/10.1002/agr.21677 (the Wiley page returned 403) | abstract via Crossref | "determined simultaneously" |
| N-M16 | D. W. Bullock et al., "Managing Rail Logistics Risks Faced by Upper Great Plains Grain Shippers: A Case Study Using Value-at-Risk", *Agribusiness* | 5 Sep 2025 | https://api.crossref.org/works/10.1002/agr.70029 | abstract via Crossref | Optimization over how many shuttle trains to buy; primary and secondary markets used for risk management |
| N-M17 | Federal Reserve, G.17 `ip_sa.txt` (same file as N-J13; new series) | data to Jul 2026 | https://www.federalreserve.gov/releases/g17/ipdisk/ip_sa.txt | download | G325@4 and G3254 monthly; annual averages **[our calc]** |
| N-M18 | FRED search results for "Chemicals Except Pharmaceuticals and Medicines (NAICS = 3251-3,5-9)" | 2026 | https://fred.stlouisfed.org/series/IPG3254S84T (as listed in the search results) | snippet | The series title matched to G325@4 (*assumed*); Q4 2025 value 91.65 |
| N-M19 | Census, 2022 CFS Hazardous Materials, table CF2200H07 (hazard class by mode) | 2022 data | https://www2.census.gov/programs-surveys/cfs/data/2022/CF2200H07.zip | download (the API needs a key) | US tons by hazard class for truck, for-hire and company-owned truck |
| N-M20 | The Counter, on produce dumped at the Nogales border | 28 May 2019 | https://thecounter.org/nogales-arizona-food-waste-dumping-america-mexico-border/ | page extraction; secondary | about 6B lb imported; about 60M lb unsellable a year; causes (*assumed*) |
| N-M21 | University of Arizona Cooperative Extension (D. Duval, A. Kerna Bickel, G. Frisvold), *Potential Economic Impact of Cold Inspection Facility Upgrade at Mariposa Port of Entry, Nogales, AZ* | Dec 2018, revised Sep 2019 | https://extension.arizona.edu/publication/potential-economic-impact-cold-inspection-facility-upgrade-mariposa-port-entry-nogales | page extraction | No cold inspection facility at Nogales; perishables routed elsewhere; no per-truck figures |
| N-M22 | Texas A&M TTI (CIITR), D. Salgado Manzano, "When Time Is Money, Fast Is Good; Faster Is Better" | 20 Mar 2020 | https://ciitr.tti.tamu.edu/2020/03/20/when-time-is-money-fast-is-good-faster-is-better/ | page extraction | FAST plus unified processing: 31 minutes; 19 minutes quicker than non-FAST (Ysleta-Zaragoza) |
| N-M23 | TTI Border Crossing Information System, World Trade Bridge page | snapshot | https://bcis.tti.tamu.edu/CrossingDetails/Index/WTB | search summary only (the page returned HTTP 500) | FAST 13 minutes against non-FAST 15 minutes (*assumed*) |
| N-M24 | ReFED, Insights Engine, Food Waste Monitor farm methodology | undated | https://docs.refed.org/methodologies/food_waste_monitor/farm.html | page extraction | 2.00% rejected by buyers' quality teams, "based on expert interviews", data quality "Very Low" |
| N-M25 | USDA blog, "PACA, the First Line of Defense for the Produce Industry" | undated | https://www.usda.gov/about-usda/news/blog/paca-first-line-defense-produce-industry | snippet (the page returned 403) | about 3,350 claims and more than $63M over 3 years; FY2010 nearly 2,000 claims and $30M (*assumed*) |
| N-M26 | USDA AMS, "An Overview of the PACA Complaint Process" (slides) | Aug 2013 | https://www.ams.usda.gov/sites/default/files/media/Presentation_-_Overview_of_PACA_Complaint_Process%5B1%5D.pdf | download | Informal complaint fee $100; formal $500 |
| N-M27 | USDA Rural Development, GovDelivery bulletin on agricultural cooperative statistics (2024 data) | 2025-26 | https://content.govdelivery.com/accounts/USDARD/bulletins/4033d4c | page extraction | 1,620 co-ops (2024), 1,647 (2023); milk 93; grain and oilseeds 312 |
| N-M28 | Remsei et al., dairy supply-chain routing and forecasting, *Journal of Infrastructure, Policy and Development* | 2024 | https://api.crossref.org/works/10.24294/jipd9403 | abstract via Crossref | "dropping about 16% of total travel time" |
| N-M29 | Search snippets on milk-collection routing cases: MDPI *AgriEngineering* 2019 (Castrolanda, Brazil); a GIS case (India) | 2019; undated | https://www.mdpi.com/2624-7402/1/1/6 (403) ; https://www.scribd.com/document/210476031/Milk-route-optimisation-using-GIS | snippet | "about 3%"; 1,445 → 1,350 km, 6% (*assumed*) |
| N-M30 | Sehulster and Pratt, Cornell research bulletin 83-26, *Potential Savings in Farm Milk Pickup Costs from Eliminating Route Duplication and Using Improved Scheduling Techniques* | 1983 | https://ideas.repec.org/p/ags/cudarb/184123.html | title only (the PDF was empty or blocked) | — |
| N-M31 | NIST Handbook 44 (2026), §3.31 Vehicle-Tank Meters | 2026 | https://www.nist.gov/document/2026-nist-handbook-44-section-331 | download | Accuracy class 0.3 (petroleum, large meters): acceptance 0.15%, maintenance 0.3% |
| N-M32 | Maryland Department of Agriculture, press release on weights-and-measures violations | 25 Mar 2013 | https://news.maryland.gov/mda/press-release/2013/03/25/mda-reports-weights-measures-law-violations-reports-cover-january-1-through-march-13-2013/ | page extraction | FY2012: 1,104 fuel-truck and rack meters, 12% in violation; 1,294 delivery-ticket inspections, 0.7% |
| N-M33 | CSX Corporation, Form 10-K for 2024 (CSX investor PDF) | Feb 2025 | https://s2.q4cdn.com/859568992/files/doc_financials/2024/q4/79e798a5-6a06-4312-b41f-07265f9fd851.pdf | download | Other revenue $499M (2024) against $578M (2023); "lower carload demurrage" |
| N-M34 | CSX Corporation, Form 10-K for 2022 (CSX investor PDF) | Feb 2023 | https://s2.q4cdn.com/859568992/files/doc_financials/2022/ar/2022-csx-final-10k.pdf | download | Other revenue $908M (2022) against $744M (2021); "increases in demurrage" |
| N-M35 | Union Pacific: 10-Q for Q2 2024 (sec.gov) and 10-K figures via search snippet | 2024-25 | https://www.sec.gov/Archives/edgar/data/100885/000143774924023463/unp20240630c_10q.htm ; https://www.sec.gov/Archives/edgar/data/100885/000010088525000042/unp-20241231.htm | page extraction (10-Q); snippet (10-K) | Accessorial revenue Q2 2024 $131M against $149M; annual $779M, $584M, $554M (2022-24; *assumed*) |
| N-M36 | FHWA, *Comprehensive Truck Size and Weight Limits Study*, Compliance Comparative Analysis Technical Report, chapter 3, Table 18 | 2015 | https://ops.fhwa.dot.gov/freight/sw/map21tswstudy/technical_rpts/ccanalysis/03enforcement.htm | page HTML parsed | Permits issued by 44 states, 2008-2012, by type |
| N-M37 | FHWA, *Best Practices in Permitting of Oversize and Overweight Vehicles: Final Report* (FHWA-HOP-17-061), §4 | data collected 2017 | https://ops.fhwa.dot.gov/publications/fhwahop17061/sec4.htm | page HTML parsed | 30 states with automated permit systems, 6 in progress, 13 with no plans; 20 at the harmonized thresholds |
| N-M38 | TxDMV, *FY 2024 Operating Budget* | 2023 | https://www.txdmv.gov/sites/default/files/report-files/TxDMV-FY-2024-Operating-Budget.pdf | snippet | FY2023: 742,594 OS/OW permits (*assumed*) |
| N-M39 | FMCSA, supporting statement for OMB 2126-0025, "Transportation of Household Goods; Consumer Protection" | 18 Jun 2025 | https://www.reginfo.gov/public/do/DownloadDocument?objectID=159171501 | download (docx parsed) | 558,851 interstate moves; 1,676,553 estimates at 2 hours each; $48.88 an hour; bill of lading 0.5 hour; 7,861 carriers |
| N-M40 | Census, Economic Census 2017, products by industry (EC1700NAPCSINDPRD) | 2017 data | https://www2.census.gov/programs-surveys/economic-census/data/2017/sector00/EC1700NAPCSINDPRD.zip | download | NAICS 484210 product lines: household $11.02B of $15.62B; commercial $1.72B, and others |
| N-M41 | UGPTI (A. Dybing, K. Vachal, B. Rahman), *Central Plains Grain Farm Truck Fleet & Marketing Patterns* (DP-321) and the AMS summary; UGPTI DP-284 (Northern Plains, 2015) | 2023; 2015 | https://www.ugpti.org/resources/reports/downloads/dp-321.pdf ; https://www.ams.usda.gov/sites/default/files/media/GrainFarmTruckFleetSummary.pdf ; https://www.ugpti.org/resources/reports/downloads/dp-284.pdf | download (text search) | 14.9 miles average to the first-choice delivery point; no wait-time figures found |
| N-M42 | Montana Department of Livestock; Colorado rules on brand inspection (via search) | current | https://liv.mt.gov/Brands-Enforcement/Inspection-Requirements ; https://www.sos.state.co.us/CCR/GenerateRulePdf.do?ruleVersionId=6034&fileName=8+CCR+1205-6 | snippet | $1 a head (Montana); $0.65 a head for market-consigned cattle (Colorado) (*assumed*) |
| N-M43 | Texas International Produce Association (about page, via search); Pharr volume snippet | current | https://texipa.org/about-us/ | snippet | "over 400 companies"; Pharr "more than 8.9 billion pounds" (*assumed*) |
| N-M44 | Search snippets on containerized farm exports around 2009 (S&P Global; AMS/UGPTI containerized grain profile) | 2020; undated | https://www.spglobal.com/commodity-insights/en/news-research/latest-news/shipping/110520-feature-backhaul-container-rates-for-us-exports-poised-for-rebound ; https://www.ams.usda.gov/sites/default/files/media/U.S.%20Containerized%20Grain%20and%20Oilseed%20Export%20Industry%20Profile%20Phase%20I.pdf | snippet; the PDF's text had no year series | Container rates at historic lows in 2009; grain in containers grew from 2004 to 2011 (*assumed*) |
| N-M45 | STB, EP 754 demurrage hearing and policy statement (via search) | 2019 | https://www.federalregister.gov/documents/2019/10/10/2019-22200/policy-statement-on-demurrage-and-accessorial-rules-and-charges | snippet | Invoice-information complaints; disputes over ordered-in dates; no share (*assumed*) |

**Earlier sources re-queried or re-parsed (IDs kept):**
- N-J06 (produce districts, 2021-25);
- N-J07 (barge tons at the three locks, by year);
- N-J08 (weekly Class I grain carloads, by year);
- N-J18 (CPS table A-1, within-state against different-state);
- N-K05 (SUSB 2022: 4247, 424710, 424720, 454310, 424510, 493130, 484210);
- N-K06 (the BTS border measure list).

**Earlier sources cited without re-fetching:** N-E13, N-F34, N-G14, N-G17, N-J05, N-J09, N-J13, N-J23, N-J34, N-K07, N-K08, N-K09, N-K11, N-K12, N-K15, N-K18, N-K33, N-K36, N-K38, N-K40.

---

## 5. Could not access, or not found

**Blocked or broken:**
- USDA blog on PACA: HTTP 403. Its figures come from the search snippet only (N-M25).
- Wiley article pages (*Agribusiness*): 403. Crossref abstracts were used instead.
- MDPI (*AgriEngineering*): 403.
- AgEconSearch, Sehulster and Pratt: the record page returned 403, and the PDF came back empty.
- USDA RD's *Agricultural Cooperative Statistics 2023* (SR87) PDF at rd.usda.gov: "Access Denied". The GovDelivery bulletin was used, and AgEconSearch listed no file.
- APHIS PPQ "by the numbers" (2024 and FY22) and the 2018 PPQ report: returned HTML or unreadable files. Snippets only.
- TxDMV Chairman's reports for FY2022-FY2024 at the FY2025 URL pattern: not found (HTML returned).
- Union Pacific 10-K for 2023 and 2024: sec.gov blocks curl, the fetch tool returned only the front sections, and UP's investor PDF timed out.
- TTI's crossing-time page for the World Trade Bridge: HTTP 500.
- Census API (`cfshazmat`, `ecnlines`): "Missing Key" or 404. The www2.census.gov bulk files were used instead.
- BTS border data: the current dataset carries only "Trucks", with no loaded/empty split.
- Pennsylvania Milk Marketing Board licensed-hauler list: the PDF has no text layer.
- Pennsylvania weights-and-measures 2023 report: meter results are listed by inspector, with no clear totals. Not used.
- The scholarly-search server was not connected. Crossref's public API was used instead.

**Searched, not found (queries run; about three well-aimed attempts each):**
- **A neutral produce rejection rate, and AMS destination-inspection counts** (C-26).
  - Queries: "USDA AMS fresh fruit vegetable destination market inspections per year …"; "fresh produce truckloads rejected at receiving percent study university OR USDA …"; "PACA Division annual report fiscal year informal complaints …".
- **A neutral loss per rejected load** (C-26).
- **Holds, cold-storage days or delay cost per produce load at Nogales and Pharr; Pharr buyer counts** (C-27).
  - Queries: "Nogales produce imports border crossing cost per truck study University of Arizona …"; "Pharr McAllen produce importers distributors number of companies …".
- **A per-load admin cost from hauler time studies; brand-inspection head counts** (C-31).
  - Queries: "brand inspection fee per head annual report head inspected …"; "OMB 0579 interstate certificate of veterinary inspection …".
- **A physical tank-truck volume series; tank-wash mismatch or rejection rates** (C-35).
  - Queries: "Federal Reserve G.17 … chemicals excluding pharmaceuticals"; "reginfo.gov 2137-0034 …". No NTTC or ATA series turned up.
- **The letter-of-credit share of US farm exports; containerized farm exports for 2006-2011** (C-24).
  - Queries: "containerized agricultural exports 2009 increase backhaul …"; three queries on phytosanitary certificate counts.
- **Elevator queue cost per load** (C-28).
  - Queries: "grain elevator harvest truck wait time study extension …"; "Northern Plains grain farm truck fleet survey elevator wait time …"; UGPTI DP-321 and DP-284 text searches.
- **Milk hauler counts; a US peer-reviewed routing study with savings** (C-32).
  - Queries: "number of licensed bulk milk haulers …"; "milk collection route optimization … percent"; "milk hauling route optimization United States …"; four Crossref queries.
- **Class I demurrage totals for 2022-25; the disputed or waived share** (C-30).
  - Queries: "rail demurrage charges disputed waived percent … EP 754"; "Union Pacific 10-K accessorial revenues …" (two); "CSX 10-K other revenue demurrage …" (two).
- **National OS/OW permits after 2012; permits for 2005-2007; the share of permits self-issued nationally** (C-34).
  - Queries: "number of oversize overweight permits issued by state table FHWA …"; "Texas oversize overweight permits issued fiscal year 2008 2009 2010 …"; "TxDMV oversize overweight permits issued FY 2023 OR FY 2024 …".
- **The local against long-distance revenue split for movers (484210); a neutral claims ratio; FMCSA complaint counts** (C-40).
  - Economic Census 2017 product lines read; "FMCSA household goods information collection supporting statement …".
- **The share of northbound Laredo trucks that are loaded** (C-25).
  - Query: "BTS border crossing data 'Truck Containers Loaded' …"; BTS measure list checked.
- **Neutral reconciliation cost or error rate per fuel load** (C-38).
  - Queries: "weights and measures vehicle tank meters inspected percent rejected …"; NIST HB44 read. Only compliance rates were found.
