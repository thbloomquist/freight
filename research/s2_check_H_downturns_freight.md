# S2 check H: downturn data for knock-out K11 Test 3 (freight and trade units)

> **What this is:** evidence for knock-out K11 Test 3 at S2 of run 01. Test 3 asks whether the unit a fee would be counted on fell drastically in the last two downturns. The rule, from `research/selection_runs/run-01/0_criteria.md`: "pass if it fell 13% or less from peak to trough in both 2008-09 and 2022-25, or rose; fail if it fell more than 20% in either; 13-20%, or no data, is unknown."
> **Date:** 2026-09-15.
> **Status:** input to S2; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/2_knockouts.md`.
> **Labels:**
> - *verified*: read at the source. That means a quote from the page, a value from a downloaded file, or an official table. "Via page extraction" marks a page read through a fetch tool rather than a raw download.
> - *assumed*: a search snippet, secondary summary, vendor claim, memory, or blocked page. Vendor figures are always *assumed*, even when read on the vendor's own page.
> - **[our calc]**: this document's own arithmetic.
> - N-H IDs are new sources (§4). N-C IDs are reused from `research/s0_check_C_durability.md` and were not re-fetched.

**Windows used:**
- **2008-09:** the highest value in 2006-2008 to the lowest in 2009-2010.
- **2022-25:** the highest in 2021-2022 to the lowest in 2023-2025.

Each note says whether the data are monthly or annual.

**Plain-language terms:**
- **Peak-to-trough:** the fall from the high point to the low point, as a percentage.
- **SA:** seasonally adjusted, meaning regular calendar swings are removed.
- **Real:** adjusted for inflation. Here that means divided by a matching consumer price index (CPI).
- **12-month rolling sum:** each month's value plus the 11 before it. It removes seasonal swings from unadjusted monthly data.
- **Truckload (TL):** one shipper fills the trailer. **LTL (less-than-truckload):** many small shipments share a trailer.
- **ADV:** average daily volume (packages per operating day).
- **TEU:** twenty-foot equivalent unit. One 40-foot container is 2 TEU.
- **Entry summary:** the customs filing (CBP Form 7501 or its electronic form) that declares an import and pays duty. An **informal entry** is the simplified version for low-value shipments.
- **Revenue ton-mile:** one ton of paid cargo carried one mile.
- **Band:** ≤13, 13-20, >20 (percent fall), "rose", or "not found".

---

## 1. Summary table

| Unit | Cards | Series used | Direct count or proxy | 2008-09 peak → trough | 2022-25 peak → trough | Band 2008-09 / 2022-25 | Label | Sources |
|---|---|---|---|---|---|---|---|---|
| **H1** General truckload loads | C-01, C-02, C-05, C-14, C-17 | ATA For-Hire Truck Tonnage Index, monthly SA | Proxy (tons, not loads) | Jan 2008 87.6 → Apr 2009 74.8: **-14.6%** | Sep 2022 118.7 → Oct 2025 112.2: **-5.5%** | **13-20 / ≤13** | *verified* | N-H01; N-C09 |
| **H2** Spot truckload loads | C-06 | DAT Truckload Volume Index (spot and contract loads); December readings only | Count, vendor | **not found** | Van index Dec 2021 ≈223 → Dec 2023 221: about **-1%** **[our calc]** | **not found / ≤13** | *assumed* | N-H36 to N-H39 |
| **H3** Brokered truckload loads, industry-wide | C-07, C-08 | Firm load counts, annual: C.H. Robinson, Landstar, J.B. Hunt ICS, RXO, ArcBest Asset-Light | Count, firms only; **no industry series found** | C.H. Robinson 2008 → 2009 **-0.8%**; Landstar 2007 → 2009 **-12.6%** (brokerage carriers alone **-14.7%**) | Landstar 2022 → 2025 **-21.6%**; J.B. Hunt ICS 2021 → 2025 **-48.0%**; RXO and ArcBest rose | Firms ≤13 to 13-20; industry **not found** / firms from rose to >20; industry **not found** | *verified* (firm data) | N-H04, N-H05, N-H06, N-H12, N-H14 |
| **H4** Freight invoices processed | C-09 | Cass transportation invoice count, annual | Direct count, one firm | 2008 25.85M → 2009 23.14M: **-10.5%** | 2022 36.81M → 2025 34.45M: **-6.4%** | **≤13 / ≤13** | *verified* | N-H03; N-C15 |
| **H5** Detained stops | C-03 | Driver surveys (GAO 2010; ATRI 2023) | No series | **not found** (2010 snapshot only) | **not found** (2023 snapshot only) | **not found / not found** | — | N-H34, N-H35; N-C24, N-C29 |
| **H6** LTL shipments | C-11 | Carrier shipment counts, annual | Count, carriers only; **no industry series found** | Old Dominion **-15.0%**, Saia **-7.1%**, Con-way **-2.8%**, YRC **-43.2%**; Old Dominion + Saia **-10.8%** | Old Dominion **-14.8%**, Saia rose, XPO **+0.3%** (2022 → 2025); Old Dominion + Saia **-3.3%**; Yellow closed in 2023 | Carriers diverge; industry **not found** in both windows | *verified* (carrier data) | N-H08 to N-H13 |
| **H7** US domestic parcels | C-12 | UPS US domestic ADV; FedEx Ground ADV; Pitney Bowes index (industry) | Count | UPS 2007 → 2009 **-5.8%**; FedEx Ground rose | UPS 2021 → 2025 **-18.4%** (planned cut of its largest customer); industry about flat, 2021 → 2023 | **≤13 / ≤13** for the industry (*assumed*); UPS alone 13-20 | UPS and FedEx *verified*; industry *assumed* | N-H15, N-H16, N-H17 |
| **H8** Big-and-bulky deliveries | C-13 | Furniture store sales, real (Census retail survey ÷ CPI) | Proxy (dollars) | NAICS 442, monthly SA, Jan 2007 → Oct 2009: **-27.0%** real; NAICS 4421, annual: **-22.7%** real | NAICS 442 Jan 2021 → Mar 2024: **-20.6%** real (-13.0% nominal); NAICS 4421 annual 2021 → 2023: **-14.1%** real | **>20 / 13-20 to >20** | *verified* data, **[our calc]** | N-H18, N-H19, N-H20 |
| **H9** Warehouse arrivals, appointments, billable activity | C-04, C-18 | BLS real output, warehousing (NAICS 4931), annual | Proxy; no direct unit found | 2008 → 2009 **-2.4%** | **Rose** (a -1.4% dip in 2022 falls inside the peak window) | **≤13 / rose** | *verified* | N-H21; N-C08 |
| **H10** Shipments to big-box retailers | C-19 | Real sales at general merchandise (452), warehouse clubs and supercenters (452311), and grocery (4451), monthly SA | Proxy (dollars) | **-4.7%** / **-4.2%** / **-6.4%** | **-7.0%** / **-6.4%** / **-7.8%** | **≤13 / ≤13** | *verified* data, **[our calc]** | N-H18, N-H19 |
| **H11** CBP entry summaries | C-20 | CBP entry summaries by fiscal year | Direct count | **not found** | Formal entries FY2022 34.35M → FY2023 31.93M: **-7.1%**; all entries **-6.2%** | **not found / ≤13** | *verified* (page extraction); the formal-entry split is **[our calc]** on an *assumed* reading | N-H22 |
| **H12** Loaded import containers (TEU) | C-21, C-22, C-23 | BTS/MARAD for 2008-09; NRF Global Port Tracker for 2022-25; annual | Direct count | 2008 → 2009 **-15%** (*verified*, a lower bound); 2006 → 2009 about **-21.5%** (*assumed*) | 2021 25.8M → 2023 22.3M: **-13.6%** | **13-20 at least; likely >20 (assumed) / 13-20** | Mixed | N-H23 to N-H27 |
| **H13** Air cargo imports (tons) | C-23 | International air cargo revenue ton-miles, both directions (BTS TranStats), 12-month rolling | Proxy; import tons not found | Feb 2008 → Sep 2009 **-22.7%** (annual -19.8%) | Mar 2022 → Oct 2023 **-11.8%** (annual -10.3%) | **>20 (13-20 on annual) / ≤13** | *verified* data, **[our calc]** | N-H28 |
| **H14** US-Mexico northbound trucks | C-25 | BTS incoming truck crossings, 12-month rolling: whole border and Laredo | Direct count (includes empty trucks) | Border: Jul 2008 → Oct 2009 **-14.7%** (annual -12.1%). Laredo: **-14.1%** (annual -11.6%) | **Rose** | **13-20 (≤13 on annual) / rose** | *verified* | N-H29 |
| **H15** Cargo theft incidents or claims | C-10 | FreightWatch for 2009; CargoNet for 2022-25 | Direct count (thefts); claims not searched | **Rose** (2009 +12%) | **Rose** (about 1,794 → 2,852 → 3,607 → 3,594) | **rose / rose** | *assumed* (a secondary report, and vendor data) | N-H30 to N-H33; N-C23 |

---

## 2. Notes by unit

### H1. General truckload shipments or loads [C-01, C-02, C-05, C-14, C-17]

**Main series: the ATA For-Hire Truck Tonnage Index, via FRED (series TRUCKD11).** It is monthly, seasonally adjusted, indexed to 2015 = 100. FRED's note reads "BTS calculation from American Trucking Association Monthly Truck Tonnage Report" (N-H01, *verified* via page extraction).
- **2008-09:** the 2006-08 high was 87.6 (Jan 2008) and the 2009-10 low was 74.8 (Apr 2009): **-14.6%** **[our calc]**.
- **2022-25:** 118.7 (Sep 2022) to 112.2 (Oct 2025): **-5.5%** **[our calc]**.
- The index then recovered to 117.6 in Mar 2026 and read 113.3 in Jun 2026.
- This matches the BTS freight index the project already holds: -16.3% and -3.2% (N-C09).

**One firm's miles and loads, as a cross-check (annual, from 10-Ks; *verified*):**
- **Werner, total miles in thousands:** 1,025,129 (2006), 1,012,964 (2007), 979,211 (2008), 872,856 (2009), 871,290 (2010).
  - The 2008-09 fall is **-15.0%** **[our calc]** (N-H07).
  - Werner also cut its fleet on purpose: average tractors went from 8,757 to 7,252, **-17.2%** **[our calc]**.
  - Werner's 10-Ks for 2021-2025 give no total miles, so its 2022-25 change was not found.
- **J.B. Hunt truckload segment (JBT), loads:**
  - 2008-09: 864,622 (2006) to 465,493 (2010), **-46.2%** **[our calc]**. Over the same years J.B. Hunt's intermodal loads rose from 629,533 to 1,075,027. The company was moving truckload freight onto rail on purpose, so this is a strategy shift, not the market (N-H06).
  - 2022-25: loads on the restated basis in the 2023-2025 10-Ks were 398,070 (2022), 410,091 (2023), 389,832 (2024) and 432,794 (2025), so **-2.1%** **[our calc]**. By then JBT was mostly "power only", with independent contractors pulling customers' trailers.

**Not found:**
- the Cass Freight Index shipments series before 2016. Cass's archive starts in January 2018 (N-H02) and FRED's starts in 2016 (N-C10).
- Knight's and Heartland's operating statistics. Searching the 10-K text found no mile or load totals.

**Caveats:**
- Tonnage counts weight, not loads.
- ATA's panel leans toward large contract fleets.
- The two single firms each changed strategy during the window.

**Band:** 2008-09 **13-20**; 2022-25 **≤13**.

### H2. Spot-market truckload loads [C-06]

**2008-09: not found.** What was tried:
- search: "DAT spot market load posts 2009 decline percent compared 2008 truckload";
- search: "TransCore freight index 2009 spot market load volume declined percent year 2008 annual" (DAT belonged to TransCore then);
- a FleetOwner article of 3 Nov 2010 (N-H39). It gives "65% increase in spot market freight availability in September 2010, compared with the previous year", but no 2009-against-2008 figure.

A search summary said spot freight in Q2 2010 was "up 331 percent" on Q2 2009. That is *assumed*, since the page was not seen, and it is not a peak-to-trough figure. It suggests a very deep 2009 low.

**2022-25: DAT Truckload Volume Index (TVI), December readings only.** All figures are vendor claims, so *assumed*. The TVI counts "loads with a pickup date during that month", with January 2015 = 100. The releases for 2022 and 2023 say it covers spot **and** contract loads (N-H36, N-H37), so it is not spot-only.

| December | Van TVI | Change on a year earlier, as stated | Source |
|---|---|---|---|
| 2022 | 215 | -3.6% | N-H36 |
| 2023 | 221 | "nearly 2% lower" | N-H37 |
| 2024 | 260 | +12% | N-H38 |

- December 2021 works out to about 223 **[our calc]**.
- The stated changes do not reconcile: 215 to 221 is a rise, yet DAT calls it lower. So DAT revises the index.
- These points suggest volume swings within a few percent, but December readings are not a peak-to-trough measure.
- An annual count of DAT load posts for 2023 against 2022 was not found (two searches).

**Band:** 2008-09 **not found**; 2022-25 **≤13** (*assumed*, weak). Overall: no data for one window.

### H3. Brokered truckload loads, industry-wide [C-07, C-08]

**Industry-wide: not found.**
- TIA market figures were **not searched** in this pass.
- No public industry count of brokered loads turned up in the searches that were run.
- The FMCSA broker-authority count the project holds (-17.6%, N-B04 via check C) counts firms, not loads.

**Firm data, annual, from 10-Ks (*verified*):**
- **C.H. Robinson (N-H04), 2008-09:** "Truckload volumes increased approximately seven percent in 2008", then "decreased 0.8 percent in 2009", then "increased 15.6 percent in 2010". So the 2008 high to the 2009 low is **-0.8%**. That against an industry that fell 14-16% (H1) means C.H. Robinson gained share.
- **C.H. Robinson, 2022-25:** "Our combined NAST truckload and LTL volume increased 5.5 percent in both 2021 and 2020" and "decreased 1.0 percent in 2022". (NAST is its North American truck division.) The 2023-2025 10-K texts give no NAST volume percentage; a text search of those filings found none. The 2025 10-K mentions only "increased LTL and truckload volumes". Its revenue fell 28.7% in 2023 (held, N-C12).
- **Landstar (N-H05), 2008-09:** truck loads from its owner-operators and brokerage carriers went 1,445,860 (2007), 1,392,280 (2008), 1,263,920 (2009), 1,413,140 (2010). That is **-12.6%** **[our calc]**. Brokerage-carrier loads alone went 588,660 to 501,980, **-14.7%** **[our calc]**.
- **Landstar, 2022-25:** truckload loads (van plus flatbed-type equipment) went 1,944,625 (2021), 2,054,777 (2022), 1,764,343 (2023), 1,647,587 (2024), 1,611,599 (2025). That is **-21.6%** **[our calc]**.
- **J.B. Hunt brokerage (ICS) (N-H06):** loads on the restated basis in the 2023-2025 10-Ks were 1,063,473 (2021), 1,027,529 (2022), 764,839 (2023), 609,854 (2024), 553,126 (2025). That is **-48.0%** from 2021 to 2025, and -25.6% in 2023 alone **[our calc]**, which matches the -26% the project holds. ICS lost share.
- **RXO (N-H14):** "a 12% increase in load volume" in 2023, and "a 1% increase in legacy RXO load volume" in 2024. It then bought Coyote in 2024, so its later totals mix in acquired volume. It rose.
- **ArcBest Asset-Light (N-H12), shipments per day:**
  - +58.3% in 2022 (including the MoLo acquisition);
  - +5.3% in 2023;
  - +5.5% in 2024;
  - -1.8% in 2025.

  It rose.

**Caveat:** the firms point in opposite directions, so share shifts dominate. One firm cannot stand for the industry.

**Band:** industry **not found** in both windows. The firms range from ≤13 to 13-20 in 2008-09, and from rose to >20 in 2022-25.

### H4. Freight invoices processed [C-09]

**Cass transportation invoice count, in thousands, annual (N-H03, *verified*):**

| Year | 2007 | 2008 | 2009 | 2010 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Invoices | 23,480 | 25,854 | 23,137 | 26,287 | 36,783 | 36,807 | 35,949 | 35,729 | 34,451 |

- **2008-09:** -10.5% (the 10-K's own figure, "(10.5)%").
- **2022-25:** -6.4% **[our calc]**, the same as the project holds (N-C15).
- In the same years the invoice **dollar** volume fell 19.6% (2009) and 14.4% (2023).
- **Restatement:** the FY2007 10-K gave 2007 as 25,206. The FY2008 10-K restates it as 23,480, and the passage read gives no reason. Either way 2008 is the peak.

**Caveats:**
- This is one processor. Cass's counts move with its own client wins and losses, as well as with freight.
- Cass notes small carriers consolidating (N-C15).

**Band:** **≤13 / ≤13**.

### H5. Detention frequency, i.e. detained stops [C-03]

**Not found for either window, as expected.** There is no repeated series with a consistent definition.
- **GAO-11-198 (N-H34, *verified* via page extraction), 2010 survey:**
  - "302 structured interviews with truck drivers ... in July and August 2010";
  - "about 68 percent--had reported experiencing detention time within the last month";
  - one company tracked "detention time on 12 percent of deliveries over a 3-month time period".
- **FMCSA follow-up study:** detention on "approximately 10 percent of their stops" (N-H35, *assumed*, search summary only).
- **ATRI, 2023:** 39.3% of stops (held, N-C24).
- **Trade press:** detention fell 6.5 points between 2014 and 2023 (held, N-C29, *assumed*).

These use different definitions, and GAO's figure counts drivers, not stops. So no peak-to-trough can be computed.

**Band:** **not found / not found**.

### H6. LTL shipments or tons [C-11]

**Carrier data, annual unless stated (*verified*; percentages **[our calc]** except where a filing states them):**

| Carrier | 2008-09 | 2022-25 |
|---|---|---|
| Old Dominion (N-H08), total shipments in thousands | 6,765 (2007) → 5,750 (2009): **-15.0%**. Tons 5,545 → 4,902: -11.6% | 12,989 (2022) → 11,072 (2025): **-14.8%**. LTL tons 10,211 → 8,177: **-19.9%** |
| Saia (N-H09), LTL shipments in thousands | 6,888 (2007) → 6,398 (2010): **-7.1%** | 7,730 (2021), 7,697 (2022) → 7,997, 8,988, 8,929 (2023-25): **rose** |
| Con-way Freight (N-H10), shipments per day | -2.9% (2008), +0.1% (2009): **-2.8%** from 2007 to 2009 | — (bought by XPO in 2015; *assumed*, from memory) |
| YRC/Yellow (N-H11), shipments per day | -11.2% (2008), -36.0% (2009), -18.8% (2010): **-43.2%** by 2009, **-53.9%** by 2010. The filings blame "diversion of freight by customers to other carriers resulting in market share loss" | LTL shipments 16,707 (2021) → 13,853 (2022), -17.1%. Shut down in 2023 (as the task brief states; not re-sourced here) |
| ArcBest ABF (N-H12), tonnage per day | -5.3% (2007), -4.2% (2008), -11.4% (2009): **-15.1%** from 2007 to 2009 | -2.4% (2023), -14.3% (2024), then +1.2% (2025): **-16.4%** from 2022 to 2024 |
| XPO (N-H13), shipments per day | — | 49,257 (2022), 51,322 (2023), 51,508 (2024), 49,420 (2025): +0.3% from 2022 to 2025. 2021 was higher ("lower shipments per day" in 2022), but the 2021 figure was not extracted. Pounds per day 71,739 (2021) → 65,268 (2025): **-9.0%** |

**Adding up the survivors with complete annual counts (Old Dominion plus Saia) [our calc]:**
- 2008-09: 13,653 → 12,178 thousand, **-10.8%**.
- 2022-25: 20,686 → 20,001 thousand, **-3.3%**.
- Both figures lean high, because survivors took freight from the carriers that shrank or closed (YRC in 2009, Yellow in 2023).

**Industry index: not found.** There is no public count of LTL shipments across the industry. What the project holds points the same way: BLS LTL employment fell 10.6% from 2022 to 2025 (N-C08), and ATA tonnage for all trucking fell 14.6% (H1). FedEx Freight is the largest LTL carrier, but its volumes appear only in graphs in FedEx's 10-Ks, and the large private carriers (Estes, R+L, TForce and others) publish none.

**Caveat:** the spread between carriers, from -3% to -43% in 2008-09 and from a rise to -20% in 2022-25, is mostly share shifting.

**Band:** carriers diverge; the industry figure was **not found** in either window. The best single guide is ATA tonnage (13-20 in 2008-09).

### H7. US domestic parcel volume [C-12]

**UPS, US domestic ADV in thousands (N-H15, *verified*):**
- **2008-09:** 13,857 (2007), 13,576 (2008), 13,050 (2009), 13,286 (2010): **-5.8%** **[our calc]**.
- **2022-25:** 21,462 (2021), 20,787 (2022), 19,030 (2023), 19,161 (2024), 17,510 (2025).
  - From 2021 to 2025 that is **-18.4%**; from 2021 to 2023 it is -11.3% **[our calc]**.
  - The 2025 fall is deliberate: "planned volume declines from our largest customer and revenue quality actions" (UPS 2025 10-K). So UPS lost share on purpose.

**FedEx (N-H16, *verified*; fiscal years end in May):**
- **2008-09:**
  - Ground ADV rose each year: 3,126, 3,365, 3,404, 3,523 (FY2007-FY2010).
  - SmartPost ADV rose from 599 to 1,222.
  - Express US domestic ADV fell 2,778 to 2,603, -6.3% **[our calc]**.
- **2022-25:** Ground ADV is only shown in graphs, so it was not extracted. The text says FY2023 Ground revenue grew "partially offset by lower volumes" and FY2024 had "higher volumes".

**Industry: the Pitney Bowes Parcel Shipping Index (N-H17, *assumed*: vendor figures, search snippets only):**
- 21.7 billion parcels (2021) and 21.2 billion (2022, "declined two percent");
- a later release restates 2022 as 21.5 billion;
- 21.7 billion (2023) and 22.4 billion (2024).

That is about flat from 2021 to 2023. USPS package volumes were **not searched**.

**Band:** 2008-09 **≤13**; 2022-25 **≤13** for the industry (*assumed*), 13-20 for UPS alone.

### H8. Big-and-bulky home deliveries [C-13]

**Proxy: furniture store sales, Census Monthly Retail Trade (N-H18, *verified* download).** Deflated by BLS CPI series: furniture and bedding (CUSR0000SEHJ) and household furnishings and supplies (CUSR0000SAH3) (N-H19, *verified*). All percentages **[our calc]**.

| Series | 2008-09 | 2022-25 |
|---|---|---|
| NAICS 442 furniture and home furnishings stores, monthly SA, nominal | Jan 2007 $9,355M → Oct 2009 $6,717M: **-28.2%** | Apr 2022 $12,199M → Mar 2024 $10,610M: **-13.0%** |
| Same, real (furniture and bedding CPI) | Jan 2007 → Oct 2009: **-27.0%** | Jan 2021 → Mar 2024: **-20.6%** |
| Same, real (household furnishings CPI) | **-28.8%** | Mar 2021 → Dec 2025: **-22.5%** |
| NAICS 4421 furniture stores, annual, not seasonally adjusted (NSA), nominal | $59,057M (2006) → $44,888M (2009): **-24.0%** | $78,640M (2022) → $71,782M (2024): **-8.7%** |
| Same, real (annual average furniture CPI) | **-22.7%** | 2021 → 2023: **-14.1%** |

**AHAM major-appliance unit shipments: not found at source.** AHAM sells its annual shipment file (item 50011_21), so it could not be opened. Snippets (all *assumed*, N-H20):
- Q1 2023 shipments were 18.3M units, down 18% on Q1 2022;
- refrigerator shipments fell "to less than 8.4 million in 2009, down from a high of 11.1 million in 2005". EIA quotes this from AHAM, but 2005 falls outside the window.

**Caveats:**
- These are store dollars, not deliveries, and furniture stores are only part of big-and-bulky retail.
- The real 2021 peak was lifted by pandemic stimulus, so the 2022-25 result depends on which price index is used: -14% to -23%.

**Band:** 2008-09 **>20**; 2022-25 **13-20 to >20**.

### H9. Warehouse truck arrivals, dock appointments, billable activity [C-04, C-18]

**Direct unit: not found.** No public series counts truck arrivals or dock appointments. Dock-scheduling vendors' data were not checked.

**Closest proxy: BLS "real sectoral output", warehousing and storage (NAICS 4931).** It is annual, given as percent change, via FRED series IPUIN4931T011000000 (N-H21, *verified* via page extraction):
- **2008-09:** +3.0% (2007), +2.3% (2008), **-2.4% (2009)**, +10.3% (2010). So 2008 to 2009 is **-2.4%**.
- **2022-25:** +8.7% (2021), -1.4% (2022), +3.9% (2023), -0.2% (2024), +1.8% (2025). With 2021 = 100, every year from 2023 to 2025 sits above 100 **[our calc]**, so it **rose**.
- Warehousing employment, which the project holds: -8.1% and -6.1% (N-C08).

**Caveat:** output here is inflation-adjusted revenue. It includes storage and value-added services, and e-commerce lifts it. It is not dock traffic.

**Band:** **≤13 / rose**.

### H10. Shipments to big-box retailers [C-19]

**Proxy: retail sales, monthly SA (N-H18), deflated by CPI (N-H19). All percentages [our calc]:**

| Series | 2008-09 real | 2022-25 real | Nominal (08-09 / 22-25) |
|---|---|---|---|
| NAICS 452 general merchandise (includes clubs and supercenters), deflated by CPI commodities | Dec 2008 → Nov 2009: **-4.7%** | Mar 2021 → Mar 2023: **-7.0%** | -4.0% / -2.6% |
| Same, deflated by CPI all items | **-3.8%** | **-5.4%** | — |
| NAICS 452311 warehouse clubs and supercenters | **-4.2%** | **-6.4%** | -2.1% / -2.9% |
| NAICS 4451 grocery stores, deflated by CPI food at home | Dec 2006 → Feb 2009: **-6.4%** | Aug 2021 → Feb 2024: **-7.8%** | -2.4% / -1.0% |

**Caveats:**
- This is sales dollars, not shipment counts.
- The Census file still reports these codes after the NAICS 2022 revision, which renumbered general merchandise to 455.

**Band:** **≤13 / ≤13**.

### H11. CBP import entry summaries filed [C-20]

**2022-25: CBP's "Trade Statistics" page (N-H22, *verified* via page extraction; direct download was refused).** Fiscal years run October to September.

| FY | Total entry summaries | Informal entry summaries | Total minus informal **[our calc]** |
|---|---|---|---|
| 2021 | 36,970,050 | 4,687,348 | 32,282,702 |
| 2022 | 39,126,589 | 4,771,976 | 34,354,613 |
| 2023 | 36,692,525 | 4,763,303 | 31,929,222 |
| 2024 | 38,362,713 | 5,164,046 | 33,198,667 |
| 2025 | 50,084,153 | 15,404,788 | 34,679,365 |
| 2026 (to 27 Jul 2026) | 92,827,312 | 63,239,269 | 29,588,043 |

- Total entries: FY2022 to FY2023, **-6.2%** **[our calc]**.
- Formal entries (total minus informal): **-7.1%** **[our calc]**. This assumes the total includes the informal ones (*assumed*). The page does not say, but the FY2026 figures only make sense that way.
- The FY2025-26 surge in informal entries fits the end of the low-value ("de minimis") duty exemption. That explanation is *assumed*, not read at source.
- For comparison, Expeditors' customs revenue fell 20.5% in 2023 (N-C13).

**2008-09: not found.** CBP's page covers FY2021 onward. What was tried:
- "CBP trade statistics 'entry summaries' fiscal year 2009 number processed";
- "CBP 'entry summaries' fiscal year 2008 OR 2009 OR 2010 'million entry summaries' performance accountability report";
- "GAO CBP 'entry summaries' annually 2008 OR 2009 OR 2010";
- "'entry summaries' CBP 2010 OR 2009 OR 2008 statistics 'formal entries' annual count".

The DHS/CBP Performance and Accountability Reports for FY2008-FY2010 were listed in results but not opened.

**Band:** 2008-09 **not found**; 2022-25 **≤13**.

### H12. Loaded import containers (TEU) at US ports [C-21, C-22, C-23]

**2008-09:**
- **BTS/RITA, *America's Container Ports* (Jan 2011) (N-H26, *verified*, full PDF text):**
  - "maritime container imports fell 15 percent while exports fell 8 percent" in 2009;
  - "following record high imports in 2006";
  - "Between 2007 and 2009 ... imports declined steeply".

  So from the 2006 peak to 2009 the fall exceeds 15%. The figure 8 data behind the chart are not printed in the PDF.
- **Snippets (*assumed*):**
  - MARAD, 18.6M TEU (2006) to 14.6M (2009): **-21.5%** **[our calc]** (N-H27);
  - NRF retail imports, 15.8M (2008) to 13.2M (2009): -16.5% **[our calc]** (N-H25).

**2022-25: NRF Global Port Tracker, annual.** It covers the 12 largest container ports.
- "Imports during 2023 totaled 22.3 million TEU, down 12.8% from 2022" (N-H23, *verified*).
- 2024 was 25.5M, and 2025 was forecast at 25.2M, "down 1.4%" (N-H24, *verified*; 2025 is a December 2025 forecast).
- The 2021 record of 25.8M and 2022's 25.5M are *assumed* (snippets, N-H25).
- 2021 to 2023: **-13.6%** **[our calc]**.
- A monthly series would show a deeper fall: NRF forecast the first half of 2023 22.3% below the first half of 2022 (*assumed*, snippet).
- Whether NRF counts only loaded containers is not stated in the releases read.

**Band:** 2008-09 at least **13-20** (*verified* lower bound), likely **>20** (*assumed*); 2022-25 **13-20**.

### H13. Air cargo imports (tons) [C-23]

**Direct unit: not found.**
- The BTS T-100 international segment data by direction needs a form-based download, which was not attempted.
- Census data on import weight by air needs a key or login.

**Proxy: BTS TranStats "Air Cargo Summary Data" (N-H28, *verified*, raw HTML download parsed).**
- It gives monthly cargo revenue ton-miles (freight and mail) by region, from October 2002 to June 2026.
- The page says it covers "U.S. airlines". The default selection is "All", and whether foreign carriers are included is unclear.
- International here means the total minus domestic **[our calc]**, both directions.

| | Annual (millions of ton-miles) | 12-month rolling |
|---|---|---|
| 2008-09 | 53,326 (2007) → 42,754 (2009): **-19.8%** | Feb 2008 → Sep 2009: **-22.7%** |
| 2022-25 | 69,836 (2021) → 62,657 (2023): **-10.3%** | Mar 2022 → Oct 2023: **-11.8%** |

**Caveats:**
- These are ton-miles, not tons.
- Inbound and outbound are mixed.
- It is possibly US carriers only.

**Band:** 2008-09 **>20** (13-20 on annual); 2022-25 **≤13**.

### H14. US-Mexico northbound truck crossings, total and Laredo [C-25]

**Source: BTS Border Crossing Entry Data, dataset keg4-3bc2 (N-H29, *verified*, API download).** The measure is "Trucks" entering the US; it counts empty trucks too. The dataset has no loaded-container measure; its measures are buses, passengers, pedestrians, personal vehicles, trains and trucks. Monthly data are not seasonally adjusted, so 12-month rolling sums are used.

| | Whole US-Mexico border | Laredo |
|---|---|---|
| Annual 2006-2010 | 4,760,516 / 4,882,500 / 4,866,252 / 4,291,465 / 4,742,925 | 1,518,989 / 1,563,836 / 1,555,197 / 1,382,319 / 1,585,682 |
| 2008-09, annual | **-12.1%** | **-11.6%** |
| 2008-09, 12-month rolling | Jul 2008 → Oct 2009: **-14.7%** | **-14.1%** |
| Annual 2021-2025 | 6,949,300 / 7,258,400 / 7,356,659 / 7,617,207 / 7,589,315 | 2,568,471 / 2,799,601 / 2,936,130 / 3,026,632 / 2,945,388 |
| 2022-25 | **Rose.** The rolling low in 2023-25 is +0.2% above the 2022 peak | **Rose** (+0.7%) |

All percentages **[our calc]**.

**Band:** 2008-09 **13-20** (≤13 on annual); 2022-25 **rose**.

### H15. Cargo theft incidents or claim counts [C-10]

**2008-09:**
- Heavy Duty Trucking, 29 Jan 2010, reporting FreightWatch International: "an average of 72 cargo theft incidents occurred per month in 2009, a gain of 12 percent, the most ever recorded" (N-H32). This is *assumed*: a secondary report.
- Search snippets give 48-50 thefts a month in 2008 and 899 incidents in 2010 (N-H33, *assumed*). They do not square with the "+12%".
- CargoNet's first annual report seems to date from about 2011: search-result title only, *assumed*.

It **rose**.

**2022-25: CargoNet (Verisk), US and Canada.** These are vendor data, so *assumed* here. Check C labelled the 2024 page *verified*.
- 2023: "CargoNet recorded 2,852 events ... a 59% increase year-over-year" (N-H30). That puts 2022 at about 1,794 **[our calc]**; a snippet says 1,778.
- 2024: 3,625 (N-C23), restated as 3,607 in the 2025 release.
- 2025: 3,594. Within that, confirmed cargo thefts went from 2,243 to 2,646 (N-H31).

It **rose**.

**Cargo claim counts: not searched** in this pass.

**Band:** **rose / rose**.

---

## 3. What the table suggests, for the coordinator (not a call)

- **Rose, or ≤13, in both windows:**
  - H4 invoices;
  - H9 warehouse proxy;
  - H10 big-box proxy;
  - H15 theft.
- **13-20 in one window:**
  - H1 truckload tonnage (2008-09);
  - H14 border trucks (2008-09, on rolling sums);
  - H12 containers (2022-25; 2008-09 likely worse).
- **Above 20 in at least one window:**
  - H8 furniture proxy (2008-09);
  - H13 air proxy (2008-09, on rolling sums);
  - H12 containers (2008-09, *assumed*).
- **No usable series for at least one window:**
  - H2 spot loads;
  - H5 detention;
  - H11 customs entries (2008-09);
  - industry-wide H3 brokerage and H6 LTL. For these two only single firms were found, and they diverge widely.

---

## 4. Sources (new, N-H)

| ID | Source (author / org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-H01 | FRED series TRUCKD11, "Truck Tonnage Index" (BTS calculation from the ATA Monthly Truck Tonnage Report) | through Jun 2026 | https://fred.stlouisfed.org/data/TRUCKD11.txt | full, via page extraction (curl to FRED timed out) | header; monthly values Jan 2006 - Dec 2010 and Jan 2021 - Jun 2026 |
| N-H02 | Cass Freight Index Report archives (Cass Information Systems) | page as of Sep 2026 | https://www.cassinfo.com/freight-audit-payment/cass-transportation-indexes/freight-index-archives | full, via page extraction | available months (Jan 2018 - Jul 2026 only) |
| N-H03 | Cass Information Systems 10-Ks, FY2007-FY2010 and FY2021, FY2022, FY2024 | 2008-2011, 2022-2025 | EDGAR CIK 708781: d22884.txt, d24451.txt, b176897_10k.htm, v214144_10k.htm, cass-20211231.htm, cass-20221231.htm, cass-20241231.htm | full text, searched | processing-volume tables (transportation invoice and dollar volumes) |
| N-H04 | C.H. Robinson 10-Ks, FY2008-FY2010 and FY2021-FY2025 | 2009-2011, 2022-2026 | EDGAR CIK 1043277: d10k.htm (2009-2011 filings), chrw-20211231.htm to chrw-20251231.htm | full text, searched | truckload volume sentences; the NAST combined-volume sentence |
| N-H05 | Landstar System 10-Ks, FY2007-FY2010 and FY2021-FY2025 | 2008-2011, 2022-2026 | EDGAR CIK 853816: g11727e10vk.htm, g17645e10vk.htm, g22126e10vk.htm, g25406e10vk.htm, d238952d10k.htm, d428854d10k.htm, d16653d10k.htm, d874247d10k.htm, d66072d10k.htm | full text, searched | "Number of loads" tables by mode |
| N-H06 | J.B. Hunt Transport Services 10-Ks, FY2007-FY2010 and FY2021-FY2025 | 2008-2011, 2022-2026 | EDGAR CIK 728535: a08-2564_110k.htm, a09-1357_110k.htm, jbhunt_10k-123109.htm, jbh_10k-123110.htm, jbht20211231_10k.htm to jbht20251231_10k.htm | full text, searched | "Operating Data by Segment": JBT, JBI, DCS and ICS loads (new passages; N-C14 covered revenue and the ICS text) |
| N-H07 | Werner Enterprises 10-Ks, FY2007-FY2010 and FY2021-FY2025 | 2008-2011, 2022-2026 | EDGAR CIK 793074: wern10k2007.txt to wern10k2009.txt, d10k.htm (2011), wern-20211231.htm to wern-20251231.htm | full text, searched | total miles, average tractors, segment operating statistics |
| N-H08 | Old Dominion Freight Line 10-Ks, FY2007-FY2010 and FY2021-FY2025 | 2008-2011, 2022-2026 | EDGAR CIK 878927: d10k.htm (2008-2011 filings), odfl-10k_20211231.htm, odfl-20221231.htm to odfl-20251231.htm | full text, searched | total shipments and tons (selected data); LTL shipments, tons, per-day figures |
| N-H09 | Saia 10-Ks, FY2007, FY2009, FY2010, FY2022-FY2025 | 2008-2011, 2023-2026 | EDGAR CIK 1177702: c23563e10vk.htm, c56460e10vk.htm, c62449e10vk.htm, saia-20221231.htm to saia-20251231.htm | full text, searched | operating statistics: LTL tonnage and shipments |
| N-H10 | Con-way 10-Ks, FY2007-FY2010 | 2008-2011 | EDGAR CIK 23675: d10k.htm, f51426e10vk.htm, f54807e10vk.htm, f58158e10vk.htm | full text, searched | Con-way Freight operating-statistic % changes |
| N-H11 | YRC Worldwide / Yellow 10-Ks, FY2007-FY2010, FY2021, FY2022 | 2008-2011, 2022-2023 | EDGAR CIK 716006: d10k.htm (2008-2011 filings), yell-20211231.htm, yell-20221231.htm | full text, searched | tonnage and shipments per day (% changes); LTL shipments table; share-loss text |
| N-H12 | Arkansas Best / ArcBest 10-Ks, FY2008-FY2010 and FY2021-FY2025 | 2009-2011, 2022-2026 | EDGAR CIK 894405: d66448e10vk.htm, c96681e10vk.htm, a10-22405_110k.htm, arcb-20211231x10k.htm to arcb-20251231x10k.htm | full text, searched | ABF / Asset-Based tonnage-per-day and shipment changes; Asset-Light shipments per day |
| N-H13 | XPO 10-Ks, FY2022-FY2025 | 2023-2026 | EDGAR CIK 1166003: xpo-20221231.htm to xpo-20251231.htm | full text, searched | LTL pounds per day and shipments per day tables |
| N-H14 | RXO 10-Ks, FY2022-FY2024 | 2023-2025 | EDGAR CIK 1929561: rxo-20221231.htm, rxo-20231231.htm, rxo-20241231.htm | full text, searched | load-volume sentences |
| N-H15 | United Parcel Service 10-Ks, FY2007-FY2010 and FY2021-FY2025 | 2008-2011, 2022-2026 | EDGAR CIK 1090727: d10k.htm (2008-2011 filings), ups-20211231.htm to ups-20251231.htm | full text, searched | US Domestic Package average daily package volume tables; 2025 volume-decline text |
| N-H16 | FedEx 10-Ks, FY2007-FY2010 and FY2021-FY2024 | 2007-2010, 2021-2024 | EDGAR CIK 1048911: g08210e10vk.htm, c73820e10vk.htm, c87681e10vk.htm, c03116e10vk.htm, fdx-10k_20210531.htm to fdx-20240531.htm | full text, searched (FY2022+ volumes are graphs) | package statistics tables (FY2007-FY2010); Ground segment revenue text (FY2021-FY2024) |
| N-H17 | Pitney Bowes Parcel Shipping Index releases (Pitney Bowes, via Business Wire and others) | 28 Mar 2023 and later | https://www.businesswire.com/news/home/20230328005199/en/ | snippet only (vendor) | US parcel totals 2021-2024 as quoted in search results |
| N-H18 | Census Bureau, *Estimates of Monthly Retail and Food Services Sales by Kind of Business*, mrtssales92-present.xlsx | file as of Sep 2026 | https://www.census.gov/retail/mrts/www/mrtssales92-present.xlsx | full (downloaded, parsed) | sheets 2006-2026; NAICS 442, 4421, 445, 4451, 452, 452311, 452319; seasonally adjusted and not adjusted blocks |
| N-H19 | BLS Public Data API v1: CPI series CUSR0000SA0, SAC, SAF11, SAH3, SEHJ, SACL1E | Jan 2006 - Aug 2026 | https://api.bls.gov/publicAPI/v1/timeseries/data/ | full | monthly SA index values used as deflators |
| N-H20 | AHAM shipment snippets: Kitchen & Bath Design News, "Appliance Shipments Off Sharply in First Quarter of 2023"; EIA *Today in Energy* id=3030; AHAM store item 50011_21 | 2011; 2023 | https://www.kitchenbathdesign.com/appliance-shipments-off-sharply-in-first-quarter-of-2023/ ; https://www.eia.gov/todayinenergy/detail.php?id=3030 ; https://www.aham.org/ItemDetail?iProductCode=50011_21&Category=DATAPROG | snippet only; AHAM file paywalled | Q1 2023 units; the 2005 → 2009 refrigerator figure |
| N-H21 | FRED series IPUIN4931T011000000, BLS "Real Sectoral Output ... Warehousing and Storage (NAICS 4931)" | annual to 2025 | https://fred.stlouisfed.org/data/IPUIN4931T011000000.txt | full, via page extraction | annual % changes 2000-2025; definition note |
| N-H22 | CBP, *Trade Statistics* ("Imports and Revenue Collection") | updated 27 Jul 2026 | https://www.cbp.gov/newsroom/stats/trade | full, via page extraction (curl got 403) | total and informal entry summaries FY2021-FY2026; column headers; update note |
| N-H23 | NRF, "Import Cargo Returning to Normal After Red Sea Disruptions" | early 2024 (the page shows no date) | https://nrf.com/media-center/press-releases/import-cargo-returning-normal-after-red-sea-disruptions | full, via page extraction | the 2023 total sentence |
| N-H24 | NRF, "Declining Import Cargo Volume Expected to Continue in 2026" | 8 Dec 2025 | https://nrf.com/media-center/press-releases/declining-import-cargo-volume-expected-to-continue-in-2026 | full, via page extraction | 2024 total; 2025 forecast; list of ports covered |
| N-H25 | NRF Global Port Tracker figures seen only in search results (2021 25.8M, 2022 25.5M; 2008 15.8M, 2009 13.2M; H1 2023 forecast) | various | e.g. https://nrf.com/media-center/press-releases/imports-drop-below-2-million-teu-pandemic-driven-shipping-surge-comes | snippet only | figures as quoted |
| N-H26 | BTS/RITA, *America's Container Ports: Linking Markets at Home and Abroad* | Jan 2011 | https://www.govinfo.gov/content/pkg/GOVPUB-TD12-PURL-gpo8844/pdf/GOVPUB-TD12-PURL-gpo8844.pdf | full PDF text | pp. 3-15: import falls, the 2006 record, total loaded TEU 2008-09, figure 8 notes (the chart's data are not printed) |
| N-H27 | MARAD, *U.S. Waterborne Foreign Container Trade by U.S. Customs Ports* | 2000-2017 data page | https://www.maritime.dot.gov/data-reports/data-statistics/us-waterborne-foreign-container-trade-us-customs-ports-2000-%E2%80%93-2017 | **blocked** (403); snippet only | 18.6M (2006) and 14.6M (2009) container imports, as quoted in a search summary |
| N-H28 | BTS TranStats, *Air Cargo Summary Data* (freight.asp) | Oct 2002 - Jun 2026 | https://www.transtats.bts.gov/freight.asp | full (raw HTML parsed) | monthly cargo revenue ton-miles by region; page notes |
| N-H29 | BTS, *Border Crossing Entry Data* (data.bts.gov dataset keg4-3bc2) | Jan 1996 - Jul 2026 | https://data.bts.gov/resource/keg4-3bc2.json | full (Socrata API) | monthly "Trucks", whole US-Mexico border and Laredo; list of measures |
| N-H30 | CargoNet (Verisk), *2023 Supply Chain Risk Trends Analysis* | 16 Jan 2024 | https://www.cargonet.com/news-and-events/cargonet-in-the-media/2023-theft-trends/ | full, via page extraction (vendor) | 2023 events; % change |
| N-H31 | CargoNet (Verisk), "Cargo Theft Losses Surge to Estimated $725 Million in 2025" | 21 Jan 2026 | https://www.cargonet.com/news-and-events/cargonet-in-the-media/2025-theft-trends/ | full, via page extraction (vendor) | 2025 and 2024 events; confirmed thefts |
| N-H32 | Heavy Duty Trucking, "FreightWatch: Cargo Theft Reaches Highest Level Ever Recorded" (reporting FreightWatch International) | 29 Jan 2010 | https://www.truckinginfo.com/news/freightwatch-cargo-theft-reaches-highest-level-ever-recorded | full, via page extraction; secondary | 2009 monthly average and % change |
| N-H33 | FreightWatch figures for 2008 and 2010, and the CargoNet first-report title, from search results | 2009-2012 | e.g. https://www.asisonline.org/security-management-magazine/articles/2012/02/the-new-highwaymen/ ; https://www.nbcnews.com/news/amp/wbna41949096 | snippet only; ASIS page **blocked** (403) | figures as quoted |
| N-H34 | GAO-11-198, *Commercial Motor Carriers: More Could Be Done to Determine Impact of Excessive Loading and Unloading Wait Times on Hours of Service Violations* | Jan 2011 | https://www.gao.gov/assets/a315300.html | full, via page extraction | survey method and dates; detention frequency |
| N-H35 | FMCSA-sponsored detention study, as summarised in search results about GAO-11-198 | c. 2014 | https://www.gao.gov/products/gao-11-198 | snippet only | "approximately 10 percent of their stops" |
| N-H36 | DAT Freight & Analytics, "DAT Truckload Volume Index: Spot rates ended 2022 on an upswing" | 19 Jan 2023 | https://www.dat.com/company/news-events/news-releases/dat-truckload-volume-index-spot-rates-ended-2022-on-an-upswing | full, via page extraction (vendor) | TVI definition; December 2022 values |
| N-H37 | DAT, "DAT Truckload Volume Index: Gap between spot and contract rates narrowed in December" | 17 Jan 2024 | https://www.dat.com/company/news-events/news-releases/dat-truckload-volume-index-gap-between-spot-and-contract-rates-narrowed-in-december | full, via page extraction (vendor) | December 2023 values; definition |
| N-H38 | DAT, "DAT: Spot truckload volumes end December on a positive trend" | 22 Jan 2025 | https://www.dat.com/company/news-events/news-releases/dat-spot-truckload-volumes-end-december-on-a-positive-trend | full, via page extraction (vendor) | December 2024 values; definition |
| N-H39 | FleetOwner, "TransCore Freight Index shows increase" | 3 Nov 2010 | https://www.fleetowner.com/refrigerated-transporter/article/21224746/transcore-freight-index-shows-increase | full, via page extraction | September 2010 spot-freight changes; no 2009-against-2008 figure |

**Reused, not re-fetched:**
- N-C08: BLS employment (warehousing and LTL).
- N-C09: BTS freight index (TSI).
- N-C10: Cass shipments on FRED, 2016 onward.
- N-C12: SEC revenue data.
- N-C13: Expeditors.
- N-C14: J.B. Hunt (revenue and ICS text).
- N-C15: Cass 10-Ks, FY2023 and FY2025.
- N-C23: CargoNet 2024.
- N-C24: ATRI.
- N-C29: FreightWaves detention snippet.
- N-B04: FMCSA broker authorities.

## 5. Could not access, or not done

**Blocked or refused:**
- **FRED** by curl: timeouts. Its series were read by page extraction instead.
- **Census economic-indicators API**: needs a key. The retail Excel file (N-H18) was used instead.
- **CBP trade page** by curl: 403. Read by page extraction.
- **MARAD** container data page and **BTS archive** figure 8 table: 403. So 2006-2008 loaded import TEU are known only from snippets.
- **ASIS "New Highwaymen"** article: 403.
- **AHAM** annual shipment file: sold, not free.

**Not found after searching (what was tried is listed under each unit):**
- **Cass Freight Index shipments before 2016.** The archive starts in 2018 and FRED in 2016, so there is no 2008-09 Cass shipments figure.
- **DAT/TransCore spot volumes for 2008-09.** Also no annual DAT load-post counts for 2022-25.
- **CBP entry summaries, FY2007-FY2010.** The DHS/CBP Performance and Accountability Reports were not opened.
- **C.H. Robinson NAST volume percentages for 2023-2025.** Not in the 10-K text.
- **FedEx Ground ADV for FY2022-FY2025.** Shown only as graphs.
- **XPO's 2021 shipments per day.**
- **Knight's and Heartland's** mile or load totals.
- **Industry-wide LTL shipment and brokered-load series.**

**Not attempted in this pass:**
- T-100 air freight by direction (a form-based download);
- Census import weight by air (needs a key or login);
- the Ports of Los Angeles and Long Beach loaded-import pages;
- TIA brokerage market data;
- USPS package volumes;
- cargo claim counts;
- Pitney Bowes' own index pages.
