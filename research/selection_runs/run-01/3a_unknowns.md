# Run 01, S3a: settling the unknowns

> **Stage S3a of `submarket_selection.md` §4, "Desk evidence". Written 2026-09-15** under the frozen criteria sheet `0_criteria.md` (§3, knock-outs K1-K11) and the S3a procedure added by change C14.
> **Input:** the S2 knock-out sheet (`2_knockouts.md` §2) and its table of what would settle each unknown (§6). That is 34 cards, 32 of which carry 75 unknowns between them.
> **Result:**
> - **2 cards fail and are dropped:** C-21 and C-23, both on durability (K11). The unit they count a fee on, loaded import containers, fell 21.9% from 2006 to 2009.
> - **18 cards go to S3b** for full fact sheets.
> - **14 cards go to the reserve list.** Each is still unknown on size (K5), with a central fee pool under $25M. None is dropped, and the founders can pull any of them into S3b.
> - **Of the 75 unknowns:** 9 are settled pass, 2 settled fail, and 64 still open, each with the reason the desk cannot settle it.
> **Gate:** "every unknown is either settled or has its reason for staying open written down, and both the S3b list and the reserve list are set." **Met** (§6).
> **Founders' decisions (2026-09-15, §7.2):** C-12 goes to the reserve list; readings 2 and 3 stand (C-22 goes to S3b, C-27 to the reserve list); no reserve card is pulled into S3b for now; S3b continues in this chat with three research agents.
> **Evidence:**
> - three checks made for this step:
>   - `research/s3a_check_L_durability_freight_trade.md` (N-L01 to N-L24): durability series for the freight and trade units;
>   - `research/s3a_check_M_lean_fail_cards.md` (N-M01 to N-M45): every unknown on the 13 cards that leaned toward failing;
>   - `research/s3a_check_N_other_size_cards.md` (N-N01 to N-N30): size and measurability inputs for the other 15 cards;
> - re-parsed here: Census BDS 2023 for the customer-survival flag (N-C05), and MARAD's container workbook, recomputed from the archived official file (N-L01);
> - one new source: Amazon's FY2017 10-K (N-P01), used on C-12.
>
> **What this file does not do:** write fact sheets, score the survivors or pick the shortlist. That is S3b. The only scores here are provisional desk scores for the two dropped cards (§5.1), as the exit rules ask.

## How to read this

**What S3a does.**
- S2 left 75 "unknowns": tests the desk evidence could not call.
- S3a goes back to each one, looks for the missing input S2 named for it (`2_knockouts.md` §6), and re-applies the same frozen test with it.
- It spends hours per card, not days.

**Three results for each unknown:**
- ✓ **settled pass:** the missing input was found, and the test passes with it.
- ✗ **settled fail:** the missing input was found, and the test fails. The evidence is given.
- ? **still open:** the desk cannot settle it. The reason is written down.

**What then happens to each card** (the exit rules, `submarket_selection.md` §4 S3a step 5, **[our call]** set 2026-09-15):
- **A card that fails any test is dropped.** It keeps the same record as S2's drops: its knock-out row and provisional Axis A and W scores.
- **A card still open on K11,** because no better series exists, goes to S3b with its flag.
- **A card still open on K5 whose central fee pool is under $25M** goes to the reserve list, not to S3b. It is not dropped: the founders can pull it in, and S5 is where its removable share could be measured.
- **Every other card goes to S3b.**

**What counts as "found" [our call; it follows the S3a steps as written].** An unknown is settled when the missing input S2 named for it turns up at a named source that is not a vendor. That means:
- government data or a regulator's own estimate;
- a company filing;
- a peer-reviewed or university study;
- a trade association's survey, always flagged with who runs it.

Vendor claims are recorded as context but never settle a test. Questions that only customers can answer stay open for S5.

**Worked example: one data source, two different results (C-21 and C-22).**
- **The starting point.** Both cards live at the ports, where containers are counted in TEU (a twenty-foot-equivalent unit; a 40-foot box is 2 TEU). S2 held both as "unknown, leaning fail" on durability, because it had only a search snippet for the 2008-09 fall in import containers.
- **What S3a found.** Check L found the official MARAD workbook in an archived copy; MARAD's own site blocks downloads. We re-summed it here, and it matches the BTS report S2 had read (imports -15% in 2009).
  - Loaded import containers fell from 18.61M TEU (2006) to 14.54M (2009): **-21.9%**, past the 20% fail line.
- **C-21 (container demurrage and detention, for importers)** counts its fee on import containers. Its unit fell more than 20%, so it **fails K11 and is dropped.**
- **C-22 (port drayage dispatch).** Drayage means short truck moves between a port and nearby warehouses or rail yards. The card serves "importers' and exporters' containers", so its unit is imports plus exports.
  - That total fell from 29.94M TEU (2007) to 25.58M (2009): **-14.6%**. Exports fell only 8.4% in 2009.
  - That is the unknown band, so C-22 **goes on to S3b** with its flag. Import-only drayage is recorded as a failing segment for segment selection.
- **The rule that decides it** is the C15 practice: "the card-level unit decides".

**Words used here** (the rest are in `2_knockouts.md`, "How to read this"):
- **Savings pool, fee pool, fee share:** as in S2. The **central fee pool** is 20% of the geometric midpoint of the savings range. It orders the work and sets the reserve list, but never fails a card by itself (C13).
- **Reserve list:** cards still unknown on size whose central fee pool is under $25M. They are parked, not dropped.
- **Card-level unit:** the unit a fee would be counted on for the card as a whole, as its sentence defines it.
- **Floor:** a sourced figure known to understate the true value. It can set the low end of a range, but not the high end.
- **Rolling:** a 12-month rolling sum (each month plus the 11 before it), which removes seasonal swings. Under C15, when rolling and annual figures fall in different bands, the rolling figure decides.

---

## 1. Result at a glance

**Dropped (2):**

| Card | Failed | One-line reason |
|---|---|---|
| C-21 Container demurrage and detention | K11 | Its unit, loaded import containers, fell 21.9% from 2006 to 2009 (MARAD, all US ports, *verified*; N-L01) |
| C-23 Quoting and booking international freight | K11 | Import containers fell 21.9% (as C-21). International air freight fell 21.0% on annual data and 23.2% rolling from 2007 to 2009 (DOT, both directions, *verified*; N-L06) |

**To S3b (18):** C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-14, C-15, C-17, C-18, C-19, C-20, C-22.
- **Clean passes:** C-09 and C-15.
- **Every other card carries open items** into its fact sheet (§5.2).

**Reserve list (14):** C-12, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-34, C-35, C-38, C-40 (§5.3).
- **C-12 sits exactly on the line.** On the only neutral cost base, used at both ends, its central fee pool is $12M. If that base is read as a floor, the pool is $25M. It is placed on the reserve list by default **[our call]**, and the founders decide (§7.2).

**Five patterns to know before S3b:**
1. **Size (K5) is still settled by nothing.**
   - Sourced inputs replaced many judgements: Census receipts, company filings, regulators' paperwork estimates and World Bank border costs.
   - No card crossed a K5 line. The share software could remove is still our judgement on every card, and only S5's savings assessments can measure it, as S2 found.
2. **The general-freight family stays unknown on durability.**
   - No industry count of truckloads, LTL shipments, brokered loads or spot loads exists for 2008-09.
   - Every proxy found sits in the 13-20% band: truck tonnage -14.6%, long-distance trucking output -17.7%, truckload real revenue -13.8%.
3. **The international family shrank.**
   - Two of the four international cards are dropped on 2008-09 import volumes.
   - C-22 survives because exports held up.
   - C-20 (customs entries) sits in the unknown band at -17.8%.
4. **Every farm-origin card stays small.**
   - After sourced inputs, the central fee pools of C-26 to C-32 run from $4M to $21M, and all seven go to the reserve list.
   - C-31's durability now passes on the card-level unit. This is recorded as evidence for the origin hypothesis (§5.3).
5. **The carrier sides carry the customer-survival flag; the payer sides are clear** (K11 Test 2, §4.5).
   - General freight trucking loses firms at twice the economy's rate.
   - Brokers, warehouses, manufacturers and wholesalers are at or below it.

---

## 2. The sheet after S3a

- **Symbols:** ✓ pass · ✗ fail · ? unknown · S split flagged for segment selection (K2 only).
- **Bold** marks a result S3a changed.
- K1, K8, K9 and K10 had no unknowns at S2 and are unchanged. K10's ruled-out sides still stand (`2_knockouts.md` §4.2).

| Card | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | K11 | S3a result | Still open |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 Buying truckload capacity | ✓ | S | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ? | S3b | K7 (S5); K11 |
| C-02 Load status | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K5; K11 |
| C-03 Detention and extra charges | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K11 |
| C-04 Dock appointments | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K5; K11 |
| C-05 Getting small carriers paid | ✓ | S | ✓ | **✓** | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K5; K11 |
| C-06 Matching spot loads | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K4; K5; K11 |
| C-07 Small brokerage back office | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K11 |
| C-08 Carrier vetting and fraud | ✓ | ✓ | ✓ | ? | ? | ✓ | ? | ✓ | ✓ | ✓ | ✓ | S3b | K4; K5; K7 (S5) |
| C-09 Auditing and paying freight bills | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S3b | — |
| C-10 Cargo claims | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K4; K5; K11 |
| C-11 LTL class and reclass disputes | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K4; K5; K11 |
| C-12 Parcel invoice audit | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | reserve (default; §7.2) | K4; K5 |
| C-14 Planning and consolidating | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K11 |
| C-15 Routing own delivery fleets | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S3b | — |
| C-17 Controlling inbound freight | ✓ | S | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K4; K11 |
| C-18 Warehouse storage and handling bills | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S3b | K4; K5 |
| C-19 OTIF fines and deductions | ✓ | S | ✓ | **✓** | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | S3b | K5 |
| C-20 Import entries | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K5; K11 |
| C-21 Container demurrage and detention | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | **✗** | **dropped** | — |
| C-22 Port drayage dispatch | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | S3b | K4; K5; K11 |
| C-23 Quoting and booking international freight | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | **✗** | **dropped** | — |
| C-24 Export documents | ✓ | ✓ | **✓** | **✓** | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | reserve | K5; K7 (S5); K11 |
| C-25 Laredo cross-border | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | reserve | K5; K7 (S5); K11 |
| C-26 Produce rejections | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | reserve | K4; K5 |
| C-27 Border produce | ✓ | S | ✓ | ✓ | ? | **✓** | ? | ✓ | ✓ | ✓ | ✓ | reserve | K5; K7 (S5) |
| C-28 Harvest grain | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | reserve | K5 |
| C-29 Rail and barge buying | ✓ | ✓ | ✓ | ✓ | ? | **✓** | ? | ✓ | ✓ | ✓ | ? | reserve | K5; K7 (S5); K11 |
| C-30 Rail demurrage | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | reserve | K5; K11 |
| C-31 Livestock hauling | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | **✓** | reserve | K5 |
| C-32 Milk hauling | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | reserve | K5 |
| C-34 OS/OW permits | ✓ | ✓ | ✓ | **✓** | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | reserve | K5; K11 |
| C-35 Tank loads | ✓ | ✓ | ✓ | **✓** | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | reserve | K5; K7 (S5); K11 |
| C-38 Fuel reconciliation | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | reserve | K5 |
| C-40 Household moves | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | reserve | K4; K5; K11 |

**Tally of the 75 unknowns [our calc]:**

| Test | Unknowns at S2 | Settled pass | Settled fail | Still open |
|---|---|---|---|---|
| K3 | 1 | 1 (C-24) | 0 | 0 |
| K4 | 15 | 5 (C-05, C-19, C-24, C-34, C-35) | 0 | 10 |
| K5 | 27 | 0 | 0 | 27 |
| K6 | 2 | 2 (C-27, C-29) | 0 | 0 |
| K7 | 7 | 0 | 0 | 7 (all for S5) |
| K11 | 23 | 1 (C-31) | 2 (C-21, C-23) | 20 |
| **Total** | **75** | **9** | **2** | **64** |

---

## 3. How each unknown was re-tested

| Test | Missing input sought (from `2_knockouts.md` §6) | Settled when | What happened |
|---|---|---|---|
| K3 Identifiable and reachable | A count of farm and food exporters (C-24) | A named list or count exists for at least one paying side | Found (Census, N-M07) |
| K4 Measurable | For each card, the neutral input §6 named: a factored share, a rejection rate, a correction rate, a national permit count, and so on | That input is found at a non-vendor source | Found for 5 of 15. Where only part was found, the card stays open and the part is recorded |
| K5 Big enough | Sourced replacements for judgement inputs, under the desk rule in §5.1 (C13): pass if 10% of the low end reaches $25M; fail if 35% of the high end is clearly short; "about" means within a few percent | A range crosses a line | Ranges moved, but none crossed a line (§4.2) |
| K6 Software can fix it | The share of the cost that comes from information, not physical handling, a market price or a government step (C-27, C-29) | A separable information part is shown | Found for both. Each passes "part only", as S2 did for five cards |
| K7 Saving measurable and attributable | Whether customers would credit software for the saving | Only customers can answer | All 7 stay open for S5, as the S3a procedure says |
| K11 Durable | A better series for the unit a fee would be counted on, under the C15 practice (§5.1): name the unit, prefer physical counts, the finer data decides, never one firm, and the card-level unit decides | The unit's fall lands clearly in a band | 3 settled; 20 still open, 17 of them in the 13-20% band or without any series (§4.1) |

**Readings made in this file [our call; the founders can overturn any of them, §7.1]:**
1. **C-18's firm-size scope.** The card means small and mid-sized warehouses (under 500 staff), the project's SMB focus (S0, D2). The under-20-staff cut is a firm-size floor, which is deferred to segment selection (F-6).
2. **C-22's unit is imports plus exports,** because its sentence names both.
3. **C-27's cost includes the document work.** Its sentence names "two customs brokers", and C-25 already counts that work.
4. **C-30's unit is its shipper base's carloads** (chemicals, plastics, paper, scrap and grain mill products), not all rail carloads.
5. **Two different series that disagree across a band line leave the unit unknown** (C-11, C-29, C-35). The C15 "finer data decides" practice covers one series at two frequencies, not two different series.
6. **C-12's Census cost base is a floor,** because it leaves out shipping booked as cost of goods sold (N-P01).
7. **C-03's durability lean moves from pass to fail.** Repeated surveys show detention becomes less frequent in a downturn, so detained stops fall faster than freight.
8. **Where a check's suggestion is not adopted,** the reason is given in §4. For example, check N suggested C-11's K4 "could now pass", but the neutral correction rate S2 asked for was not found.

---

## 4. Evidence by test

### 4.1 K11 Test 3: the unit a fee would be counted on

- **Bands:** a fall of 13% or less (or a rise) passes; 13-20% is unknown; over 20% fails.
- **Windows:** peak in 2006-2008 to trough in 2009-2010 (check L), or 2005-2008 to 2009-2011 (check M, following check J); and peak in 2021-2022 to trough in 2023-2025.
- **Labels:** *verified* unless marked; percentages are **[our calc]** in the checks.

| Card | Unit, and the series used | 2008-09 | 2022-25 | S2 → S3a | Source |
|---|---|---|---|---|---|
| **C-21** | Import containers, loaded (MARAD, all US ports, TEU) | **-21.89%** (2006 → 2009). Rolling: no national monthly series; LA + Long Beach fall 1.8 points deeper rolling than annual | -13.0% annual; **-16.1% rolling** | ? → **✗** | N-L01 (re-summed here), N-L03 |
| **C-23** | Import bookings: ocean containers plus air freight | Containers -21.89%. Air, both directions, US and foreign airlines: -21.0% annual, **-23.2% rolling** (inbound alone not found) | Containers -16.1% rolling; air inbound -8.0% rolling | ? → **✗** | N-L01, N-L06, N-L07 |
| C-22 | Import plus export containers, loaded (MARAD) | **-14.56%** (2007 29.94M → 2009 25.58M TEU, re-summed here). Import-only drayage -21.89%: a failing segment | Imports -16.1% rolling; exports not measured | ? → ? (13-20) | N-L01 |
| C-30 | Carloads of the card's shipper base (Waybill Sample, STCC 28 + 26 + 40 + 204) | -12.15% annual; **-14.60% rolling**. For context, total carloads fell -19.88% annual and -20.003% rolling | -2.1% annual; -4.2% rolling | ? → ? (13-20) | N-J09 (via check L) |
| C-20 | CBP "processed trade entries" (DHS *Budget-in-Brief*, one rounded figure a year) | **-17.8%** (31.4M → 25.8M; which fiscal year each figure covers is *assumed*) | formal entries -7.1% (S2) | ? → ? (13-20) | N-L15, N-H22 |
| C-25 | Loaded truck containers entering at Laredo (BTS, from archived copies of the dataset) | -8.4% annual; **-14.9% rolling** (whole border -14.4%) | rose | ? → ? (13-20) | N-L08 |
| C-01, C-02, C-05, C-14, C-17 | Truckloads. No industry load count. Proxies: ATA tonnage (monthly -14.6%, annual -8.9%); BLS long-distance trucking output -17.7%; truckload real revenue -13.8% | 13-20 on every finer or industry proxy | tonnage -5.5% | ? → ? | N-H01, N-L10, N-L11 |
| C-11 | LTL shipments. No industry count. LTL real revenue (Census ÷ PPI) **-25.7%** (dollars); all-trucking tonnage -14.6% (physical, not LTL-specific); two surviving carriers -10.8% | the proxies disagree | not available | ? → ? (leans fail) | N-L11, N-H08 to N-H09 |
| C-07 | Brokered loads. No industry count: TIA's survey starts April 2009; Armstrong's figures are dollars (*assumed*) | not found | not found | ? → ? | N-L18, N-L19 |
| C-06 | Spot loads | not found (only a 2009-10 rebound figure) | about -1% (DAT, *assumed*) | ? → ? | N-L12, N-H36 to N-H38 |
| C-10 | Cargo claims | not found | not found | ? → ? | N-L22 |
| C-03 | Detained stops. No count series. Repeated ATRI surveys: detention rose into the tight 2018 market and fell by 2023 | not found | not found; direction down | ? → ? (lean now fail **[our call]**) | N-L21 |
| C-04 | Truck visits to docks. No direct count. Shipment counts would be closest but start in 2016-18; tonnage (-14.6%) is the next closest | 13-20 on tonnage | tonnage -5.5% | ? → ? | N-H01, check L §L8 |
| **C-31** | Livestock loads: cattle plus hogs, under three head-per-load weightings | **-2.8% to -3.6%** | **-4.6% to -8.6%** | ? → **✓** | N-M01, N-J05 |
| C-29 | Grain tons by rail plus barge (USDA modal-share data; STB rail series; USACE barge tons) | -9.8% | -17.9% to -18.2% (weekly Class I rail series) or -8.4% (Waybill Sample) | ? → ? (two series disagree) | N-M13, N-J07 to N-J09 |
| C-35 | Chemical tank-truck loads. No tank-truck series. Chemicals excluding pharmaceuticals (output) against chemical rail carloads (physical count) | output **-26.9%** monthly (-21.8% annual); rail -8.8% | -9.7%; -1.2% | ? → ? (two series disagree) | N-M17, N-J09 |
| C-24 | Containerized farm exports (USDA AMS, TEU) | no data (the series starts in 2010) | -8.5% | ? → ? | N-M11 |
| C-34 | Oversize/overweight permits, 44 states (FHWA) | -10.2% (2008 → 2009; 2006-07 not covered) | rose in Washington and Texas; no national series | ? → ? | N-M36, N-J23, N-K07 |
| C-40 | Household moves: CPS movers, weighted by the long-distance share of revenue **[our call]** | -12.7% to -27.8% (13-20 at most weightings) | -8.4% to -9.1% | ? → ? | N-J18, N-M40 |

**Why the two drops are firm:**
- The fall is above 20% in every MARAD vintage, and from either possible peak year (2006 or 2007: -21.89% or -21.32%).
- Import container weight fell 22.4% over the same years (N-L02).
- A rolling series would only deepen the fall. The only monthly data, for Los Angeles and Long Beach, falls 1.8 points further on rolling sums.
- C-23's other part, air freight, is also above 20% on the best series found.
- **If the founders ever relax the 2008-09 half of Test 3,** C-21 and C-23 reopen together with C-36 (`2_knockouts.md` §5). On 2022-25 alone, both would be in the unknown band.

**Segments that K11 now rules out** (for segment selection; P-8, C15):
- import-only drayage (C-22);
- pulp and paper, and scrap, shippers (C-30, as at S2);
- cattle-only hauling as a durability watch-point (C-31: -13.8% in 2022-25, following the herd cycle);
- interstate moves (C-40, as at S2).

### 4.2 K5: savings pools after sourced inputs

- The central fee pool is 20% × √(low × high). All figures are **[our calc]** in the checks.
- "Inputs replaced" lists the sourced swaps. Every card still has a removable share that is **[our call]**.

| Card | S2 range (central) | S3a range (central) | Inputs replaced (source) | K5 | Route |
|---|---|---|---|---|---|
| C-02 Load status | $0.18-0.73B ($73M) | unchanged | none. O*NET task frequencies support S2's 20% low end of time on status (N-N28) | ? | S3b |
| C-04 Dock appointments | $0.14-0.36B ($46M) | **$84-439M ($38M)** | Detention paid by facilities: at most 47% (ATRI, association-flagged). Wait cut 9.3-25.8% (a university study of port gates) (N-C24, N-N02) | ? | S3b |
| C-05 Carrier payment | $0.07-1.4B ($62M) | **$99-798M ($56M)** | Factored share 23-28% (OOIDA surveys, association-flagged); fee 1.29-3.2% (Triumph's filings; OOIDA) (N-N14 to N-N17) | ? | S3b |
| C-06 Spot loads | $0.06-1.2B ($55M) | **$51M-1.10B ($47M)** | Gross per carrier $123-222k (Census nonemployer statistics; OOIDA) (N-D05, N-N17) | ? | S3b |
| C-08 Vetting and fraud | $0.15-0.59B ($59M) | **$91-690M ($50M)** | Theft base corrected to $454M (2024) to $725M (2025) (CargoNet, vendor). Fraud 0 to $1.0B (TIA, association-flagged, no method stated) (N-N24 to N-N26) | ? | S3b |
| C-10 Cargo claims | $70-370M ($32M) | **$62-442M ($33M)** | LTL base $65.7B (Census 2022); claims ratio 0.3-0.5% anchored on five carriers' filings (N-N07 to N-N13) | ? | S3b |
| C-11 LTL disputes | $0.10-0.90B ($60M) | **$105-920M ($62M)** | LTL base $65.7B (Census 2022) (N-N13) | ? | S3b |
| C-12 Parcel audit | $0.10-0.83B ($59M) | **$19-202M ($12M)** on check N's reading; $19M-0.83B (**$25M**) if the Census figure is a floor | Parcel spend from the Census retail survey's shipping line, about 1.8% of receipts (a floor, N-P01) (N-N20, N-N21) | ? | reserve (default; §7.2) |
| C-18 Warehouse bills | $110-900M ($63M) | unchanged at the SMB scope. Under-20-staff scope: $28-225M ($16M) | none. Leakage rates are vendor-only | ? | S3b |
| C-19 OTIF and deductions | $0.11-1.44B ($80M) | **$56-480M ($33M)** | Non-trade deductions at a median of ¼-½% of sales (CRF survey, association-flagged) (N-N29) | ? | S3b |
| C-20 Import entries | $0.10-0.64B ($50M) | **$104-694M ($54M)** | FY2025's 34.7M formal entries (CBP); $100 document cost as the high end (World Bank) (N-H22, N-N06). CBP's 5-minute filing estimate is a floor for the filing alone, not for preparation, so the $40 low end stays | ? | S3b |
| C-21 Container D&D | $93-279M ($32M) | unchanged. FMC charge complaints refunded about 0.06% of charges (N-N18) | none | ? (moot) | dropped |
| C-22 Drayage dispatch | $67-268M ($27M) | **$69-274M ($27M)**. If the excess wait is 0.25 hour instead of 0.5: $34-274M ($19M) | Volume: 30.2M loaded import TEU and 11.0M export TEU in 2022 (USACE via BTS) (N-N01). Current turn times exist only in snippets, so S2's 0.5-hour excess stays | ? | S3b |
| C-23 Intl quoting | $127-707M ($60M) | unchanged | none. O*NET frequencies are consistent with the 15-30% time share (N-N28) | ? (moot) | dropped |
| C-24 Export documents | $23-114M ($10M) | **$32-117M ($12.3M)** | Containers 3.22-3.52M TEU a year (USDA AMS); $60 document cost as the low end (World Bank) (N-M11, N-M05) | ? | reserve |
| C-25 Laredo | $50-177M ($19M) | **$68-183M ($22.4M)** | $160 of document cost per crossing (World Bank: a Mexican export plus a US import) (N-M05) | ? | reserve |
| C-26 Produce rejections | $10-274M ($11M) | unchanged ($10.6M). With ReFED's 2% as the high rejection rate: $10-137M | none neutral. ReFED's figure is an expert-interview assumption, and PACA claims give only a floor of about 0.07% of loads (N-M24, N-M25) | ? | reserve |
| C-27 Border produce | $7-82M ($5M) | **$12.8-70.7M ($6.0M)**, counting the document work (reading 3). On S2's cost structure alone: $7.1-58.9M ($4.1M) | Gateway loads 355-368k a year (USDA Market News); document cost $160 per crossing (World Bank) (N-J06, N-M05) | ? (the generous case, $24.7M, is "about" $25M, so it leans fail) | reserve |
| C-28 Harvest grain | $34-314M ($21M) | unchanged ($20.7M) | none. About 1,800-2,400 elevator companies (SUSB; USDA RD); no neutral queue cost | ? | reserve |
| C-29 Rail and barge buying | $36-109M ($13M) | unchanged ($12.5M) | none. Secondary railcar bids swing by $151-1,200 a car within a year, as context (N-M14) | ? | reserve |
| C-30 Rail demurrage | $40-236M ($19M) | unchanged ($19.4M). Scaled to 2024: $40-167M ($16.4M) | Railroads' filings put 2024 demurrage at about $1.05-1.12B, against the 2021 peak pace (CSX filings; UP, *assumed*) (N-M33 to N-M35) | ? | reserve |
| C-31 Livestock | $11-70M ($6M) | unchanged ($5.6M). The generous case is still $24.5M ("about") | none. APHIS's own estimate puts health papers at about $0.24 a load on average (N-M03) | ? | reserve |
| C-32 Milk hauling | $29-148M ($13M) | unchanged ($13.1M) | none. 93 dairy co-ops (USDA RD) | ? | reserve |
| C-34 OS/OW permits | $39-260M ($20M) | **$53-244M ($22.7M)** | 4.24M permits a year in 44 states (FHWA, 2012), plus 0-15% for the other six (N-M36) | ? | reserve |
| C-35 Tank loads | $9-227M ($9M) | **$4-185M ($5.6M)** | 1.5 minutes per shipping paper (PHMSA's own estimate); 207M tons at the low end (CFS 2022) (N-M04, N-M19) | ? | reserve |
| C-38 Fuel reconciliation | $28-164M ($13M) | unchanged ($13.6M) | Marketer count 7,679 (SUSB), against PMAA's "8,000" (N-K05) | ? | reserve |
| C-40 Household moves | $46-276M ($23M) | **$44-194M ($18.4M)** | Household share of mover revenue 70.6% (Economic Census 2017); interstate estimating cost $163.9M a year (FMCSA's own estimate) (N-M40, N-M39) | ? | reserve |

**Also checked:**
- **C-17's K5 pass holds.** Swapping CSCMP's spend figure for the census trucking receipts lowers its low end to $0.27-0.33B, still over $250M (N-N13).
- **No card reaches the pass line** (a low end of $250M or more). The largest new low end is C-11's $105M.
- **No card clearly misses the fail line:**
  - C-27's generous case is $24.7M and C-31's is $24.5M. Both count as "about" $25M, so both are unknown, leaning fail.
  - C-27 would fail on S2's cost structure alone ($20.6M). It stays unknown only because its sentence includes the customs brokers' paperwork (reading 3).

### 4.3 K3, K4, K6 and K7

| Test | Card | S3a result | Evidence, or why still open |
|---|---|---|---|
| K3 | C-24 | ✓ | 7,130 farm and food exporters in NAICS 111, 112, 311 and 312, of which 6,679 are small or mid-sized, plus part of 22,481 nondurable-goods wholesalers (Census *Profile of U.S. Importing and Exporting Companies*, N-M07). The forwarder side is licensed and counted by the FMC (N-F05). How to reach exporters through commodity groups is *assumed* |
| K4 | C-05 | ✓ | Factored share (OOIDA surveys: 23% and 28%, association-flagged) and fee (Triumph's 10-K: 1.35% on $11.7B purchased) (N-N14 to N-N17) |
| K4 | C-19 | ✓ | Non-trade deduction rate from the CRF survey of 203 companies (association-flagged, N-N29) |
| K4 | C-24 | ✓ | Containers (USDA AMS) and document cost (World Bank) (N-M11, N-M05) |
| K4 | C-34 | ✓ | National permit count (FHWA, 44 states, 2012; dated) (N-M36) |
| K4 | C-35 | ✓ | Tank-load tonnage (CFS 2022 hazmat by class) and paperwork time (PHMSA) (N-M19, N-M04) |
| K4 | C-06 | ? | No source counts the owner-operators who use dispatch services (three tries: OOIDA 2019, 2022 and 2023; ATRI; trade press). That share swings the pool threefold. Fees are vendor-quoted |
| K4 | C-08 | ? | Theft rests on a vendor (CargoNet) and fraud on an association estimate with no method. The regulator (FMCSA) says it lacks the data (N-N27) |
| K4 | C-10 | ? | The claims paid are now neutral (Census and filings). The step from paid to "owed but never recovered", which makes most of the pool, rests on one vendor survey of filing and denial rates |
| K4 | C-11 | ? | The LTL base is now neutral, but S2 asked for a neutral correction rate (reweigh, reclass) and none exists. No carrier filing, NMFTA figure or study was found |
| K4 | C-12 | ? | Parcel spend now comes from Census (a floor). The recovery rate is still vendor-only |
| K4 | C-17 | ? | The overpayment rate and the inbound shares are vendor-only. The one MIT study found addresses a different question |
| K4 | C-18 | ? | Billing leakage is vendor-only (no IWLA survey, study or 3PL filing found) |
| K4 | C-22 | ? | Volume is now neutral (USACE), but current turn times exist only in snippets. The BTS 2026 port report was blocked |
| K4 | C-26 | ? | No neutral produce rejection rate exists (ReFED's own quality rating: "Very Low") |
| K4 | C-40 | ? | Household revenue and the interstate estimating cost are now neutral. The claims rate and the local/long-distance split are not published |
| K6 | C-27 | ✓ (part only) | In the World Bank's Mexico-US road case, documents are about 22% of the cost and 41% of the time of a crossing. The rest is inspection and handling (N-M05) |
| K6 | C-29 | ✓ (part only) | Peer-reviewed work treats how many rail cars to buy, and when, as a decision problem, so an information lever exists. The market price dominates (N-M15, N-M16) |
| K7 | C-01, C-08, C-24, C-25, C-27, C-29, C-35 | ? | Only customers can say whether they would credit software for a rate saving, a risk avoided, or a shorter hold. FAST lanes cut crossings by 2-19 minutes, but FAST is a Customs program, not software (N-M22). Open for S5 |

### 4.4 Corrections found in earlier stages

| Where | What was wrong | Correction | Effect |
|---|---|---|---|
| S2, C-08 savings pool (`2_knockouts.md` §4.1; N-C23) | 3,625 crime events × the average value of a theft = $733.6M | Only 2,243 of 2024's events were confirmed thefts, so the figure is **about $454M** (CargoNet's own 2025 report, N-N24; vendor, *assumed*). 2025 was about $725M | Range now $91-690M; still unknown. Marked in `2_knockouts.md` §4.1 |
| S1, C-08 card (`1_candidates.md` §4.1) | "3,625 theft incidents" | They are crime events, of which 2,243 were confirmed thefts | Wording only; recorded here, file not edited |
| S2, C-22 K11 lean ("leans fail, as C-21") | It used import containers alone | The card-level unit is imports plus exports: -14.6% | Unknown, not leaning fail |
| S2, C-27 cost base (check K) | It counted delays and holds but not the document work the card names | The document work is added at $160 a crossing (World Bank) | The generous case moves from $20.6M, a fail, to $24.7M, "about" |
| S2, C-12 parcel spend (5-10% of receipts, **[our call]**) | Unsourced | The Census line gives about 1.8% of receipts, but it is a floor (N-P01) | Central $59M → $12M-25M, depending on the reading |
| S2, MARAD snippet (N-H27, *assumed*) | -21.5% | **-21.89%** at source (N-L01) | Confirms the lean, and settles the fail |

### 4.5 K11 Test 2: the customer-survival flag (recorded, not a knock-out)

**What it records.** The frozen sheet names three facts for each side (`0_criteria.md` §3):
- the firm death rate against the economy's, in Census BDS for 2009 and 2023;
- the establishment entry rate against the exit rate;
- the firm count.

**How the flag is read [our call].** The frozen sheet names the facts but sets no line, so this record reuses check C's Option 2 lines (`research/s0_check_C_durability.md` §3):
- the flag is **raised** if the death rate is more than 1.5× the economy's in either year, or if the firm count fell more than 15% from peak to trough in either window;
- otherwise it is **clear**;
- exits above entries in both years is noted beside the flag as Constellation's "shrinking pool" sign (check C, C5). It does not raise the flag by itself.

**Source: Census BDS, 2023 release** (N-C05, re-parsed here for every side code on the 34 surviving cards).
- BDS "2009" runs from March 2008 to March 2009, and "2023" from March 2022 to March 2023.
- It covers payroll firms only, so owner-operators without payroll are missing.
- **The economy:** death rate 10.0% (2009) and 9.4% (2023). Establishment entry and exit: 9.3% and 11.6% (2009), 10.6% and 9.4% (2023).
- **Cross-check:** this re-parse reproduces check C's figures for 4841, 4842, 4885, 4931 and 4921.
- **Firm-count windows** follow S2's Test 3 windows: the highest count in 2006-2008 to the lowest in 2009-2011, and the highest in 2021-2022 to 2023, the last year published.
  - For 4842, check C measured from 2007 and got -13.5%. From the 2006 peak the fall is -15.2%, which raises the flag.
- **Death rate** = firms that closed entirely ÷ firms that year **[our calc]**.

| Side (BDS code) | Cards | Death rate 2009 (× economy) | Death rate 2023 (× economy) | Entry / exit 2009 | Entry / exit 2023 | Firm count, 2008-09 window | Firm count, 2022-23 | Flag |
|---|---|---|---|---|---|---|---|---|
| General freight trucking: TL, LTL, local and drayage (4841) | C-01, C-02, C-03, C-05, C-06, C-08, C-10, C-11 (LTL, ruled out), C-14, C-17, C-19, C-22, C-25 | 16.6% (1.7×) | 19.4% (2.1×) | 14.8% / 18.6% | 19.3% / 19.3% | 48,538 (2007) → 43,726 (2010), -9.9% | 85,509 → 85,244, -0.3% | **Raised:** death rate. Entries matched exits in 2023, after the 2021-22 entry boom |
| Specialized trucking: reefer, bulk, heavy, livestock, movers (4842) | C-03, C-05, C-06, C-26, C-27, C-28, C-31, C-32, C-34, C-35, C-38, C-40 | 12.9% (1.3×) | 13.6% (1.45×) | 9.8% / 16.2% | 13.1% / 14.2% | 42,657 (2006) → 36,185 (2011), -15.2% | 43,064 → 42,221, -2.0% | **Raised:** count, borderline (-13.5% measured from 2007). Exits above entries in both years |
| Brokers, forwarders, customs brokers (4885) | C-01, C-05, C-06, C-07, C-08, C-20, C-22, C-24, C-25, C-26 | 9.0% (0.9×) | 9.4% (1.0×) | 7.9% / 11.3% | 9.0% / 10.5% | 13,809 (2008) → 13,146 (2010), -4.8% | 14,106 → 14,019, -0.6% | Clear. Exits above entries in both years |
| Warehousing, incl. refrigerated and farm-product (4931) | C-02, C-03, C-04, C-18, C-26, C-28 | 6.2% (0.6×) | 6.2% (0.7×) | 9.4% / 9.1% | 9.9% / 6.9% | 6,836 (2008) → 6,821 (2011), -0.2% | 8,381 → 8,576, +2.3% | Clear |
| Couriers (4921; side ruled out by K10) | C-12 | 12.5% (1.2×) | 11.9% (1.3×) | 9.2% / 10.9% | 12.4% / 20.0% | -0.5% | +4.8% | Clear |
| Inland water (4832; side ruled out by K10) | C-29 | 9.1% (0.9×) | 9.6% (1.0×) | 12.6% / 12.4% | 13.9% / 10.1% | -11.1% | +7.6% | Clear |
| Rail (482; sides ruled out by K10) | C-29, C-30 | not in BDS | — | — | — | — | — | not available |
| Manufacturing (31-33), column X | C-01, C-02, C-03, C-09, C-10, C-14, C-17, C-19, C-25 | 8.0% (0.8×) | 6.9% (0.7×) | 5.6% / 9.5% | 6.9% / 7.0% | 269,573 (2007) → 238,436 (2011), -11.6% | 222,723 → 220,696, -0.9% | Clear. Exits above entries in both years: a slowly shrinking pool |
| Wholesale (42), column X, and the proxy for importers (36.5% of importers are wholesalers, N-E18) | as manufacturing, plus C-20 and C-22 | 8.8% (0.9×) | 7.8% (0.8×) | 7.5% / 9.9% | 6.7% / 8.2% | 304,959 (2006) → 281,021 (2011), -7.8% | 250,937 → 246,895, -1.6% | Clear. Exits above entries in both years |
| C-11's shippers: fabricated metals (332), machinery (333), furniture makers (337), durable wholesale (423) | C-11 | 5.8%, 5.8%, 11.6%, 8.1% (0.6-1.2×) | 5.5%, 5.2%, 7.5%, 7.2% (0.6-0.8×) | — | — | -9.0%, -9.5%, **-23.6%**, -9.1% | -0.9%, -2.5%, -1.6%, -2.3% | Clear, except furniture makers (**raised:** count) |
| Grocery wholesale (4244) | C-04, C-15 | 8.0% (0.8×) | 7.8% (0.8×) | 8.8% / 9.0% | 7.4% / 7.7% | -5.0% | -0.5% | Clear |
| Beer, wine and spirits wholesale (4248) | C-15 | 8.4% (0.8×) | 7.2% (0.8×) | 8.1% / 8.7% | 8.0% / 6.4% | -2.9% | +0.5% | Clear |
| Hardware and plumbing wholesale (4237; segment ruled out by K11) | C-15 | 5.5% (0.6×) | 6.2% (0.7×) | 6.0% / 6.7% | 5.6% / 4.6% | -11.6% | -3.8% | Clear |
| Drug wholesale (4242) and meat processing (3116); segments ruled out by K10 | C-15 | 8.8%; 5.6% | 9.8%; 5.6% | — | — | -2.9%; -5.0% | -3.6%; +1.6% | Clear |
| E-commerce and mail-order sellers (4541, 2017 code) | C-12, C-18 | 11.4% (1.1×) | 14.9% (1.6×) | 14.1% / 13.7% | 17.2% / 15.9% | 18,519 (2008) → 18,633 (2009), +0.6% | 44,245 → 44,237, 0.0% | **Raised:** death rate in 2023. Entries above exits in both years, so the pool is replenishing |
| Farm-product raw materials wholesale: grain and livestock dealers (4245) | C-28, C-29, C-31 | 5.6% (0.6×) | 6.7% (0.7×) | 4.4% / 6.0% | 6.9% / 5.6% | 3,949 (2006) → 3,270 (2011), -17.2% | 3,070 → 3,058, -0.4% | **Raised:** count. This is a long consolidation, not a downturn collapse: the count fell every year from 2005 |
| Chemical makers (325) | C-30, C-35 | 6.5% (0.6×) | 7.4% (0.8×) | 6.2% / 7.7% | 7.7% / 7.9% | -5.0% | -1.5% | Clear |
| Plastics and rubber (326); paper (322; segment ruled out by K11) | C-30 | 6.2%; 5.9% | 4.8%; 5.2% | — | — | -12.0%; -11.7% | -3.4%; -4.4% | Clear |
| Misc. durable wholesale, incl. recyclables (4239; scrap segment ruled out by K11) | C-30 | 10.1% (1.0×) | 7.8% (0.8×) | 9.1% / 12.2% | 8.5% / 8.4% | -5.3% | 0.0% | Clear |
| Chemical wholesale (4246) | C-35 | 6.4% (0.6×) | 6.5% (0.7×) | 6.4% / 9.4% | 5.1% / 6.9% | -9.7% | -5.1% | Clear. Exits above entries in both years |
| Petroleum wholesale (4247) | C-38 | 5.2% (0.5×) | 4.7% (0.5×) | 4.3% / 5.1% | 7.3% / 4.8% | -9.6% | -4.3% | Clear |
| Direct selling, incl. fuel dealers (4543, 2017 code) | C-38 | 10.5% (1.0×) | 11.9% (1.3×) | 7.2% / 11.1% | 10.5% / 10.7% | -12.0% | -3.8% | Clear. Exits above entries in both years |
| Construction (23); machinery (333) | C-34 | 14.7% (1.5×); 5.8% | 9.4% (1.0×); 5.2% | 9.9% / 19.9% | 13.0% / 11.1% | **-21.0%**; -9.5% | +1.9%; -2.5% | Construction **raised:** count. Machinery clear |
| Food manufacturing (311) | C-24 | 7.7% (0.8×) | 8.4% (0.9×) | 7.3% / 8.5% | 9.9% / 8.1% | -4.8% | +1.0% | Clear |
| Farms (NAICS 111-112); households | C-26, C-27, C-28, C-31, C-32; C-40 | not in BDS | — | — | — | — | — | not available |

**What the flags say (a record, not a call):**
- **The carrier sides carry the flag.**
  - General freight trucking (4841) loses firms at twice the economy's rate in 2023.
  - Specialized trucking (4842) lost 15% of its firms after 2006.
  - Their churn is mostly exits, not switching (check C, C5 step 2: a death rate of 10% or more).
- **The payer sides are clear.** Brokers and forwarders (4885), warehousing (4931), manufacturing and wholesale all sit at or below the economy's death rate. Manufacturing and wholesale do show exits above entries in both years, a slow consolidation.
- **E-commerce sellers** exit fast (1.6× in 2023), but more enter than leave. That is the replenishing kind of churn (check C, C5).

---

## 5. The exit rules applied

### 5.1 Dropped cards: the final record

**Knock-out rows after S3a:**

| Card | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | K11 | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-21 Container demurrage and detention | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | fail (K11) |
| C-23 Quoting and booking international freight | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | fail (K11) |

**Provisional desk scores,** under the row rules in `2_knockouts.md` §5 and the run-01 weights.
- They are recorded only so that a drop can be challenged later. They rank nothing.
- Fee feasibility (F1-F5) is a separate gate and is not scored.

**Axis A (weights: A1 20, A2 10, A3 25, A4 15, A5 15, A6 15):**

| Card | A1 | A2 | A3 | A4 | A5 | A6 | **Axis A** |
|---|---|---|---|---|---|---|---|
| C-21 Container D&D | 0.5 | 0.5 | 1 | 0.5 | 1 | 1 | **77.5** |
| C-23 Intl quoting | 1 | 1 | 0.5 | 0.5 | 1 | 1 | **80** |

**Axis W (weights: W1 20, W2 5, W3 20, W4 15, W5 15, W6 25):**

| Card | W1 | W2 | W3 | W4 | W5 | W6 | **Axis W** |
|---|---|---|---|---|---|---|---|
| C-21 Container D&D | 0.5 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **47.5** |
| C-23 Intl quoting | 0.5 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **47.5** |

**What each score rests on** (the census figures are from `2_knockouts.md` §4.2 and N-D04):
- **C-21:**
  - **A1 = 0.5:** the savings pool's midpoint is about $161M.
  - **A2 = 0.5:** the charges come partly from port delays (physical) and partly from missed free time and invoice errors (information).
  - **A3 = 1:** there is a forcing event. OSRA 2022 and the FMC's 2024 billing rule gave importers new grounds to dispute (N-F32, N-G03).
  - **A4 = 0.5:** the forwarders' top-50 share is 34.3%. Firms under 20 staff hold 24.1%, just under the 25% bonus line. Importers have no census row.
  - **A5 = 1:** every import container. **A6 = 1:** the same importers are the customers of C-20, C-22 and C-23.
  - **W4 = 0.5:** proven spend (the charges, forwarders' fees), but software is not missing: six named tools (N-F54).
  - **W5 = 0.5:** the formal dispute channel is barely used, with about $1.9M a year refunded, 0.06% of charges (N-N18).
- **C-23:**
  - **A1 = 1:** midpoint about $300M.
  - **A2 = 1:** staff time on rate sheets and email drives the cost.
  - **A3 = 0.5:** a known cost, with no forcing event found.
  - **A4 = 0.5:** as C-21.
  - **A5 = 1; A6 = 1.**
  - **W4 = 0.5:** forwarders pay for staff and software today, and forwarding software exists (BoxTop was sold for about $13M, N-B25).
- **Both cards score high on Axis A.** Like C-36 at S2, they are removed only by the 2008-09 half of Test 3. On 2022-25 alone they would be in the unknown band (containers -16.1% rolling; air imports -8.0%).

### 5.2 The S3b list (18 cards) and what each carries

Each fact sheet records these items under "From S3a" (`submarket_selection.md` §13). The Test 2 flags are in §4.5.

| Card | Open items carried into S3b | Notes for the fact sheet |
|---|---|---|
| C-01 Buying truckload capacity | K7: whether shippers credit software for rate savings against a moving benchmark (S5). K11: no load count; the proxies are 13-20% | Carrier side (4841) flag raised; shipper side clear |
| C-02 Load status | K5 $0.18-0.73B (central $73M). K11 as C-01 | O*NET supports the low end of the time on status |
| C-03 Detention and extra charges | K11: no series of detained stops. Detention becomes less frequent in downturns, so the lean is now toward failing **[our call]**. S2 also left the founders the option to rule (`2_knockouts.md` §6) | Carrier sides (4841, 4842) flags raised |
| C-04 Dock appointments | K5 $84-439M ($38M). K11: no dock-visit count; tonnage -14.6% | The wait-cut potential comes from a port-gate study (N-N02), used by analogy |
| C-05 Getting small carriers paid | K5 $99-798M ($56M). K11 as C-01 | Factored share and fee now sourced (K4 ✓). Carrier side flag raised |
| C-06 Matching spot loads | K4: no count of dispatch-service use. K5 $51M-1.10B ($47M). K11: no spot-load series for 2008-09 | — |
| C-07 Small brokerage back office | K11: no industry count of brokered loads | Broker side clear on Test 2 |
| C-08 Carrier vetting and fraud | K4: vendor theft data, association fraud estimate, no regulator data. K5 $91-690M ($50M). K7: risk avoided (S5) | The theft base is corrected (§4.4) |
| C-09 Auditing and paying freight bills | none | Clean pass |
| C-10 Cargo claims | K4: vendor filing and denial rates. K5 $62-442M ($33M). K11: no claim counts | The claims ratio now comes from carriers' filings |
| C-11 LTL class and reclass disputes | K4: no neutral correction rate. K5 $105-920M ($62M). K11: leans fail (LTL real revenue -25.7%, a dollar proxy) | LTL carrier side ruled out (K10) |
| C-14 Planning and consolidating | K11 as C-01 | — |
| C-15 Routing own delivery fleets | none | Clean pass. Segments ruled out: drug wholesalers and meat processors (K10); hardware and plumbing distributors (K11) |
| C-17 Controlling inbound freight | K4: the overpay rate is vendor-only. K11 as C-01 | K5 still passes on the census base, narrowly ($0.27-0.33B low end) |
| C-18 Warehouse storage and handling bills | K4: leakage is vendor-only. K5 $110-900M ($63M) | Scope is SMB warehouses (reading 1). The under-20-staff cut ($16M central) belongs to segment selection (F-6) |
| C-19 OTIF fines and deductions | K5 $56-480M ($33M) | The deduction rate is now sourced (K4 ✓) |
| C-20 Import entries | K5 $104-694M ($54M). K11: -17.8% on DHS's rounded counts (fiscal years inferred) | The end of the low-value (de minimis) exemption tripled informal entries from FY2025: a named trigger for S3b item 5 |
| C-22 Port drayage dispatch | K4: no current turn time at source. K5 $69-274M ($27M), or $19M if the excess wait is 0.25 hour. K11: -14.6% (imports + exports) | Import-only drayage is a failing segment. Closest S3b card to the reserve line |

### 5.3 The reserve list (14 cards)

- **What reserve means:** each card is still unknown on K5, with a central fee pool under $25M. It is parked, not dropped.
- **What would pull a card into S3b:**
  - the founders' call, at any time;
  - or S5-grade evidence of the share software could remove (a savings assessment or interviews) that lifts its central fee pool over $25M.

| Card | K5 range (central) | Other open items | What keeps it small |
|---|---|---|---|
| C-34 OS/OW permits | $53-244M ($22.7M) | K11: no data before 2008 | 30 states already ran self-issue permit portals in 2017 (N-M37) |
| C-25 Laredo cross-border | $68-183M ($22.4M) | K7 (S5); K11: -14.9% rolling | Most crossing time is Customs inspection |
| C-28 Harvest grain | $34-314M ($20.7M) | — | No neutral queue cost; the removable share is our judgement |
| C-30 Rail demurrage | $40-236M ($19.4M; $16.4M scaled to 2024) | K11: -14.6% rolling on the shipper base | Demurrage fell from its 2021-22 peak (CSX, UP filings) |
| C-40 Household moves | $44-194M ($18.4M) | K4: claims rate and local share not published. K11: 13-20% at most weightings | Interstate moves fail K11 as a segment |
| C-38 Fuel reconciliation | $28-164M ($13.6M) | — | The marketer side fails Test 1 (S2) |
| C-32 Milk hauling | $29-148M ($13.1M) | — | Routing saves only a few percent of a hauling bill |
| C-29 Rail and barge buying | $36-109M ($12.5M) | K7 (S5); K11: two rail series disagree for 2022-25 | The cost is mostly a market price |
| C-24 Export documents | $32-117M ($12.3M) | K7 (S5); K11: no 2008-09 data | Export filing is already electronic and cheap: 3 minutes per filing (Census) |
| C-12 Parcel invoice audit | $19-202M ($12M); $19M-0.83B ($25M) on the floor reading | K4: recovery rate vendor-only | **On the line; the founders decide (§7.2).** The main late-delivery refund is suspended for ground services (FedEx: express only from Feb 2026; UPS: air only since 2021) (N-J28, N-N30) |
| C-26 Produce rejections | $10-274M ($10.6M) | K4: no neutral rejection rate | Much of the loss is physical (temperature, shrink) |
| C-27 Border produce | $12.8-70.7M ($6.0M) | K7 (S5) | Closest card to a K5 fail: its generous case is "about" $25M only when the document work is counted (reading 3) |
| C-31 Livestock hauling | $11-70M ($5.6M) | — (K11 now passes) | Health papers cost about $0.24 a load on the regulator's own estimate |
| C-35 Tank loads | $4-185M ($5.6M) | K7 (S5); K11: the two series disagree | A shipping paper takes 1.5 minutes (PHMSA); the high end rests on a wash-mismatch judgement |

**For the origin hypothesis** (CLAUDE.md asks for evidence either way):
- All seven surviving farm-origin cards (C-26 to C-32) go to the reserve list. After sourced inputs, their central fee pools run from $4.1M to $20.7M.
- C-31's durability passes once hogs are counted with cattle.
- As at S2, this tests the fee pool for software. It does not test whether farmers lose profit to shipping.

---

## 6. Gate check

**The gate:** "every unknown is either settled or has its reason for staying open written down, and both the S3b list and the reserve list are set" (`submarket_selection.md` §4 S3a).

| Condition | Status |
|---|---|
| Every unknown settled, or open with a reason | Met: 9 pass and 2 fail, each with evidence (§4). All 64 open unknowns carry a reason (§4.1-4.3) |
| S3b list set | Met: 18 cards (§5.2) |
| Reserve list set | Met: 14 cards (§5.3), with C-12's placement pending the founders (§7.2) |

**Against option C's expectation.** The founders chose option C knowing that "likely under 20 reach S3b" (`2_knockouts.md` §7). The S3b list is 18. S3b's own gate is 4-6 cards on the shortlist, each with a savings-pool estimate and its assumptions written down.

---

## 7. For the founders

### 7.1 Readings made here [our call]: confirm or overturn

The eight readings are listed in §3. Three of them change where a card goes:
- **Reading 2** keeps C-22 in S3b. Without it, C-22 would be dropped with C-21.
- **Reading 3** keeps C-27 on the reserve list. Without it, C-27 would fail K5 and be dropped.
- **Reading 6** sets C-12's range (§7.2).

### 7.2 Decisions (made 2026-09-15)

Each follows the decision-record format: the default suggested here, the research behind it, then the decision the founders made. The founders chose from options put to them; their choices are quoted verbatim.

| # | Decision | Default suggested here [our call] | Why | Founders' decision |
|---|---|---|---|---|
| D-1 | C-12, reserve or S3b? | **Reserve** | Check N's reading (the only neutral cost base, used at both ends) gives a central of $12M. Reading the base as a floor gives $25M: "about" the line, which the K5 rule reads as leaning fail. The main refund that parcel audit recovers, for late ground deliveries, is suspended at both big carriers. The courier side is already ruled out (K10) | **Reserve.** "Reserve list (Recommended)" |
| D-2 | Pull any reserve card into S3b? | **None** | Each is still unknown on size, with a central under $25M. The closest are C-34 ($22.7M), C-25 ($22.4M) and C-28 ($20.7M) | **None.** "None for now (Recommended)". Cards can still be pulled in later |
| D-3 | How S3b runs | Continue in this chat | 18 fact sheets. The new research is mainly items 5, 7 and 9 (software penetration and why now, implementation, the incumbent map). Items 1-4, 8, 10 and 11 can be filled largely from S1-S3a | **Continue in this chat, with three research agents.** "Continue here, 3 agents (Recommended)" |
| D-4 | Readings 2 and 3 (C-22's unit is imports plus exports; C-27's cost includes the customs brokers' paperwork) | Keep both | Each reads the card's unit or cost from its own sentence, under C15's "the card-level unit decides". Without them, C-22 would fail K11 and C-27 would fail K5 | **Keep both.** "Keep both (Recommended)" |

### 7.3 Corrections to earlier stages

Listed in §4.4. Only the C-08 figure is marked in the earlier file (`2_knockouts.md` §4.1), with a pointer here. The other corrections are superseded by this file's calls.

### 7.4 Proposed process changes (not applied)

These follow the decision-record rule: nothing changes `submarket_selection.md` or `0_criteria.md` until the founders sign it off. After sign-off, each would be logged in §9 of the process doc. P-7 (a) and P-10 from S2, and P-1 to P-4 from S1, are still open.

| # | Proposal | Reason |
|---|---|---|
| P-11 | **One-sided sources.** Write into the K5 desk rule (§5.1): "a sourced figure that bounds only one end of a range replaces that end only" | Check N used ATRI's "fewer than 50 percent" as C-04's high end only, but the Census retail line as both ends of C-12, although it is a floor (N-P01). Without a rule, the same kind of evidence is used two ways |
| P-12 | **Scope check on savings pools.** At S2 (and in S3b item 2), confirm that each card's savings pool covers every cost part its sentence names | S2's C-27 pool left out the customs brokers' paperwork the card names. Adding it moved the card from a K5 fail to "about" |
| P-13 | **When two series disagree.** Extend the K11 practice (C15): "where two different series for the unit fall in different bands, the result is unknown, and both go to S4's strict durability comparison" | The current practice ("the finer data decides") covers one series at two frequencies, not two different series. Three cards needed the reading: C-11, C-29 and C-35 |
| P-14 | **The reserve line.** Extend the K5 "about" reading to the reserve rule: "a central fee pool within a few percent of $25M counts as under it" | C-12's central is $25.1M on one reading and $12M on the other. With no rule, its placement turns on $0.1M |
| P-7 (a), still open | The S1 card template should name the unit a fee would be counted on | C-22's result changed once its unit was read from its sentence (imports and exports), not from its neighbour's |

---

## 8. Sources

**New inputs made for this step** (full entries in each file):

| File | IDs | What it covers |
|---|---|---|
| `research/s3a_check_L_durability_freight_trade.md` | N-L01 to N-L24 | K11 Test 3 for the freight and trade units: MARAD container workbooks (archived), BTS supply-chain indicators, DOT international air freight, BTS border data (archived), the STB Waybill Sample, DHS *Budget-in-Brief*, BLS real output, Census service revenue ÷ PPI, ATRI detention surveys |
| `research/s3a_check_M_lean_fail_cards.md` | N-M01 to N-M45 | Every unknown on the 13 lean-fail cards: USDA PSD and AgTransport, OMB paperwork estimates (APHIS, PHMSA, Census AES, FMCSA), World Bank *Doing Business*, the Census exporter profile, FHWA permit studies, the Economic Census product lines, railroad filings, peer-reviewed railcar-market work |
| `research/s3a_check_N_other_size_cards.md` | N-N01 to N-N30 | Size and measurability inputs for the other 15 cards: BTS port statistics, carriers' 10-Ks and 8-Ks, Triumph's filings, OOIDA surveys, the FMC budget justification and 2024 rule, Census retail and wholesale expense surveys, the 2022 Economic Census, CBP's paperwork estimate, O*NET, the CRF deduction survey, CargoNet |

**Re-parsed here:**
- **N-C05, Census Business Dynamics Statistics, 2023 release:** `bds2023.csv`, `bds2023_sec.csv`, `bds2023_vcn3.csv`, `bds2023_vcn4.csv` from https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/ (downloaded 2026-09-15). The Census API returned nothing without a key, so the CSVs were used, as in check C. Firm deaths, firms, and establishment entry and exit rates for 2005-2011 and 2019-2023, for the economy, 7 sectors, 12 three-digit and 57 four-digit codes.
- **N-L01, MARAD *U.S. Waterborne Foreign Container Trade by U.S. Customs Ports (2000-2017)*:** the archived official workbook (web.archive.org capture of 4 Apr 2021). The "Import TEU", "Export TEU" and "Total TEU" sheets were re-summed over their 63 port rows [our calc]. Imports: 18,610,849 (2006), 14,536,169 (2009). Exports: 11,310,114 (2008), 10,357,721 (2009). Total: 29,941,572 (2007), 25,582,144 (2009).

**New source cited here:**

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-P01 | Amazon.com, Inc., Form 10-K for 2017 | filed Feb 2018 | https://www.sec.gov/Archives/edgar/data/1018724/000101872418000005/amzn-20171231x10k.htm | full text (EDGAR), *verified* | "Cost of sales primarily consists of ... inbound and outbound shipping costs"; "Shipping costs, which include sortation and delivery center and transportation costs, were $11.5 billion, $16.2 billion, and $21.7 billion in 2015, 2016, and 2017". Worldwide, against the Census retail survey's $8.1B for all e-commerce firms' purchased transportation, shipping and warehousing in 2017 (N-N21). So the Census line very likely leaves out shipping booked as cost of goods sold **[our call]** |

**Searched, not found:** the Census retail survey's definition of its "purchased transportation, shipping, and warehousing services" line, and whether it asks firms to include shipping booked as cost of goods sold. One web search found only the survey overview pages.

**Earlier sources cited in this file:**
- **S0 and S1:** N-B25; N-C24; N-D04, N-D05; N-E18; N-F05, N-F32, N-F54; N-G03.
- **S2:** N-H01, N-H08, N-H09, N-H22, N-H27, N-H36 to N-H38; N-J05, N-J07 to N-J09, N-J18, N-J23, N-J28; N-K05, N-K07.
- **Process documents:** `0_criteria.md`; `submarket_selection.md` §4, §5.1, §9, §10, §13; `2_knockouts.md` §2-§8; `research/s0_check_C_durability.md` §3 and C5.

**Access limits,** in addition to those in each check:
- the Census BDS API needs a key;
- MARAD's site returns 403;
- the BTS 2026 port report, CBP's rule analysis for low-value shipments, and FMCSA's 2024 broker report all returned 403 (check N).
