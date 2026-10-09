# Run 01, S2: knock-outs

> **Stage S2 of `submarket_selection.md` §4, "Knock out". Written 2026-09-15** under the frozen criteria sheet `0_criteria.md` (§3, knock-outs K1-K11).
> **Input:** the 40 cards in `1_candidates.md`.
> **Result:** 6 cards fail and are dropped. 34 go forward to S3. Of those, 2 pass every test and 32 carry at least one "unknown" that S3 must settle.
> **Gate:** "roughly 8-15 survivors". **Not met: 34 survive.** The process doc reads that as "Far more means the knock-outs are too loose". §7 explains why it happened and sets out the options.
> **Founders' decision (2026-09-15): option C.** S3 now runs in two steps: S3a settles the unknowns, lean-fail cards first, and S3b builds full fact sheets for the cards still standing. The S3 procedure in `submarket_selection.md` §4 has been updated to match (C14). §7 records the founders' answers.
> **S3a result (2026-09-15):** see `3a_unknowns.md`. C-21 and C-23 were dropped on K11; 18 cards go to S3b and 14 to a reserve list. One figure in this file is corrected there: C-08's theft base (§4.1, marked).
> **Evidence:**
> - the resource notes (R-IDs), the S0 checks (N-A to N-D) and the S1 scans (N-E to N-G);
> - four inputs made for this stage:
>   - `research/s2_check_H_downturns_freight.md` (N-H01 to N-H39): how far freight and trade units fell in 2008-09 and 2022-25 (K11 Test 3);
>   - `research/s2_check_J_downturns_other_and_projections.md` (N-J01 to N-J37): the same for farm, industrial and consumer units, plus BLS 10-year projections and substitutes (K11 Tests 1 and 3);
>   - `research/s2_check_K_savings_pools.md` (N-K01 to N-K45): savings pools for 23 cards (K5);
>   - the Economic Census concentration files for 2022 and 2017 (N-D01) and Census SUSB 2022 (N-D04), re-parsed here for every industry code on every card (§4.2, §4.3).
>
> **What this file does not do:** score or rank the survivors. That is S3-S4. The only scores here are provisional desk scores for the six dropped cards (§5), as the S2 step asks.

## How to read this

**What S2 does.** S0 froze eleven must-have tests (K1-K11) before any card existed, and every card faces them here:
- A card that clearly fails a test is dropped.
- A card that passes goes forward.
- So does a card where the desk evidence can't tell. "Unknown" is not a soft fail. S3 settles it with more evidence. Fringe cards are not to be killed early, because good beachheads often "exist on the fringe" (R15; `submarket_selection.md` §4 S2).

**Symbols in the sheet:**
- ✓ **pass**.
- ✗ **fail:** the card is dropped, with a one-line reason.
- ? **unknown:** the card goes forward, flagged for S3.
- **S** (K2 only): the card is one market but too big for word of mouth, so a split variable is named for segment selection (§3, P-5). S is never a fail.

**Worked example: C-21, container demurrage and detention.**
- **K1-K4 and K6-K10 pass:**
  - it is distinct: S1 found three differing signs against its nearest neighbour, C-22;
  - importers and forwarders can be named from CBP and FMC records;
  - the FMC publishes the charges: about $15.4B over five years (N-F31);
  - the cost comes from billing and coordination;
  - the saving (charges avoided or disputed) can be counted;
  - importers already pay forwarders, and demurrage-and-detention tools exist;
  - on the forwarder side, the 50 largest firms hold 34.3% of revenue.
- **K2 is S.** 240,535 importers across every industry are too many to talk to each other, so the card is to be split by importer size or port at segment selection.
- **K5 is ?** The savings pool is $93-279M a year (check K):
  - a 10% fee share of the low end is $9M, under the $25M floor;
  - a 35% share of the high end is $98M, over it.
  - The desk range cannot settle it.
- **K11 is ?** Loaded import containers fell at least 15% from the 2006 record to 2009 (*verified*), and about 21.5% on a figure seen only in a search snippet. They fell 13.6% from 2021 to 2023. Both windows sit in or next to the 13-20% "unknown" band.
- **Result:** forward, with two unknowns (K5 and K11) for S3.

**Words used here:**
- **Savings pool:** the yearly cost a card's customers bear that software could remove. It caps what they could pay (`submarket_selection.md` §2.1).
- **Fee pool:** the savings pool × the share of it we might charge. K5 needs about $25M a year.
- **Fee share:** our fee as a share of the saving. S0 models it at 10%, 20% and 35% (`0_criteria.md` §5). It is a modelling assumption, not a price; the fee share itself is deferred (F-8).
- **Top-50 share:** the share of an industry's revenue held by its 50 largest firms (Economic Census).
- **Small-firm share:** the share of revenue held by firms under 20 or under 500 employees (Census SUSB).
- **Peak to trough:** the fall from a series' high point before a downturn to its low point during it.
- **Proxy:** a series that stands in for a card's unit when no count of the unit exists, e.g. furniture-store sales for home deliveries. Every proxy used is named.
- **Side:** the shipper side or the freight-company side of a card. Some tests are run for each side (`submarket_selection.md` §5).

---

## 1. Result at a glance

**Dropped (6):**

| Card | Failed | One-line reason |
|---|---|---|
| C-13 Big-and-bulky home delivery | K11 | Its unit fell more than 20%. Inflation-adjusted furniture-store sales fell 27.0% from Jan 2007 to Oct 2009, and 22.7% on annual data (N-H18, N-H19) |
| C-16 Job-site deliveries for building-material dealers | K11 | Building-material dealers' real sales fell 31.6% and lumber wholesalers' 46.5% (2005-2011); housing starts fell 73.2% (N-J19 to N-J22) |
| C-33 Cut-flower air imports into Miami | K5 (and K11) | The savings pool is $3.5-21M a year. Even a 35% fee share gives about $7M, far under $25M (check K). Import weight also fell 25.0% in 2006-09 (N-J12) |
| C-36 Aggregates load tickets | K11 | Crushed stone plus sand and gravel output fell 36.9% from 2006 to 2010 (USGS, N-J14, N-J15) |
| C-37 Log trip tickets and haul pay | K11 | Wood-products output fell 45.1% (Nov 2005 to May 2009), and rail lumber loads fell 55.0% (N-J13, N-J09). Its size is also doubtful: a savings pool of $15-72M (check K) |
| C-39 Vehicle transport | K11 | Light-vehicle sales fell 38.6% from 2005 to 2009 (BEA, N-J17) |

**Forward to S3 (34):**
- **Pass every test (2):**
  - C-09, auditing and paying truckload and LTL bills;
  - C-15, routing own delivery fleets.
- **Carry unknowns (32).** §6 lists each one, with what S3 needs to settle it.

**Four patterns to know before S3:**
- **Durability (K11) did most of the cutting.**
  - Five of the six drops are jobs tied to construction, housing, furniture or new vehicles, which fell 23-73% in 2008-09.
  - Three of them held up in 2022-25: aggregates fell 5.2%, wood products 10.6%, and vehicle sales rose. Furniture-store sales fell 14-21% and the building-material series 10-15%, in or near the unknown band.
- **Size (K5) could only remove the clearly tiny.**
  - On nearly every card, the share of the cost that software could remove is a judgement, so the desk ranges span 3-50× (§4.1). Only C-33 falls clearly short.
  - On a middle reading, a 20% fee share of each range's midpoint, **16 cards lean toward failing** (13 of them still in the list). Every surviving farm-origin card (C-26 to C-32) is among them, and C-33 fails outright. The eight farm-origin cards have central fee pools of $2-21M.
- **The general-freight family is undecided on durability.**
  - Truck tonnage, the best proxy for truckloads, fell 14.6% in 2008-09 (N-H01). That is inside the 13-20% "unknown" band.
  - No industry-wide count exists for brokered loads, LTL shipments, spot loads or detained stops.
- **Structure (K10) and projections (K11 Test 1) removed nothing.** Under rule C11, a card leaves only if both of its sides fail. Every card has a trucking, brokerage or warehousing side that passes both tests:
  - its top 50 firms hold 75% of revenue or less;
  - its firm count grew from 2017 to 2022;
  - its BLS projection is positive.
  - **So at sub-market level both tests are pass-throughs.** They can rule out a side or a segment, but never a card.
  - **The founders may reconsider how these tests work** (2026-09-15). The flag is recorded where the tests are specified: `submarket_selection.md` §5 and §5.1, §9 (tension T15), and `0_criteria.md` §3.

---

## 2. The knock-out sheet

- **Symbols:** ✓ pass · ✗ fail · ? unknown · S split flagged for segment selection (K2 only).
- **K9** passes for every card (F-16).
- **Evidence** for every column is in §4; how each test was applied is in §3.

| Card | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | K11 | Result | Unknowns and notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 Buying truckload capacity | ✓ | S | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ? | forward (2) | K7: rate savings measured against a moving benchmark. K11: tonnage -14.6% |
| C-02 Load status | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K5: $0.18-0.73B. K11 as C-01 |
| C-03 Detention and extra charges | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (1) | K11: no series for detained stops |
| C-04 Dock appointments | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K5: $0.14-0.36B. K11: truck visits 13-20%; warehouse proxies ≤13% |
| C-05 Getting small carriers paid | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K4/K5: factored share not found. K11 as C-01 |
| C-06 Matching spot loads | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K4/K5: use of dispatch services not found. K11: no 2008-09 spot series |
| C-07 A small brokerage's back office | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (1) | K11: no industry count of brokered loads |
| C-08 Carrier vetting and fraud | ✓ | ✓ | ✓ | ? | ? | ✓ | ? | ✓ | ✓ | ✓ | ✓ | forward (3) | K4/K5: fraud losses beyond theft not sourced. K7: mostly risk avoided |
| C-09 Auditing and paying freight bills | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **pass** | Invoices fell 10.5% (2008-09) and 6.4% (2022-25) |
| C-10 Cargo claims | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K4/K5: claim rates vendor-only. K11: no series of claim counts |
| C-11 LTL class and reclass disputes | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | The LTL carrier side fails K10 at S3 (small-firm check). K11: no industry series |
| C-12 Parcel invoice audit | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (2) | Courier side ruled out (K10). K4/K5: recovery rates vendor-only |
| C-13 Big-and-bulky home delivery | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **fail** | K11 (§1) |
| C-14 Planning and consolidating | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (1) | K11 as C-01 |
| C-15 Routing own delivery fleets | ✓ | S | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **pass** | Segments ruled out: drug wholesalers (K10), hardware and plumbing distributors (K11) |
| C-16 Job-site deliveries | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **fail** | K11 (§1) |
| C-17 Controlling inbound freight | ✓ | S | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K4: inputs mostly vendor. K11 as C-01 |
| C-18 Warehouse storage and handling bills | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (2) | K4/K5: leakage rates vendor-only |
| C-19 Retailer OTIF fines and deductions | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (2) | K4/K5: deduction rates vendor-only |
| C-20 Import entries | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K11: no entry counts for 2008-09 |
| C-21 Container demurrage and detention | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K11 leans fail: containers down at least 15%, likely more than 20% |
| C-22 Port drayage dispatch | ✓ | S | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K4: turn-time data dated. K11 leans fail, as C-21 |
| C-23 Quoting and booking international freight | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K11 leans fail: containers as C-21; air -22.7% |
| C-24 Export documents | ✓ | ✓ | ? | ? | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | forward (5) | K5 leans fail |
| C-25 Cross-border Mexico through Laredo | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | forward (3) | K5 leans fail |
| C-26 Produce reefer booking and rejected loads | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (2) | K5 leans fail |
| C-27 Cross-border produce | ✓ | S | ✓ | ✓ | ? | ? | ? | ✓ | ✓ | ✓ | ✓ | forward (3) | K5 leans fail |
| C-28 Harvest grain hauling and scale tickets | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (1) | K5 leans fail |
| C-29 Buying rail and barge freight for grain | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ | ✓ | ✓ | ? | forward (4) | K5 leans fail. Rail and barge sides ruled out (K10) |
| C-30 Rail demurrage and accessorial invoices | ✓ | S | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K5 leans fail. Railroad side ruled out (K10). Paper and scrap shippers fail K11 as segments |
| C-31 Livestock hauling | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (2) | K5 leans fail: the generous case is about $25M |
| C-32 Milk pickup and hauling settlement | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (1) | K5 leans fail |
| C-33 Cut-flower air imports into Miami | ✓ | ✓ | ? | ? | ✗ | ? | ? | ✓ | ✓ | ✓ | ✗ | **fail** | K5, and K11 (§1) |
| C-34 Oversize/overweight permits | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K5 leans fail. State self-issue portals already substitute in some states |
| C-35 Tank loads: hazmat papers and wash certificates | ✓ | ✓ | ✓ | ? | ? | ✓ | ? | ✓ | ✓ | ✓ | ? | forward (4) | K5 leans fail |
| C-36 Aggregates load tickets | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **fail** | K11 (§1) |
| C-37 Log trip tickets and haul pay | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **fail** | K11; K5 also leans fail (§1) |
| C-38 Fuel delivery reconciliation | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | forward (1) | K5 leans fail. The heating-oil segment fails K11. The marketer side fails Test 1 |
| C-39 Vehicle transport | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **fail** | K11 (§1) |
| C-40 Household moves | ✓ | ✓ | ✓ | ? | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | forward (3) | K5 leans fail. Interstate moves fell more than 20%; local moves 13% or less |

---

## 3. How each test was applied

The tests are the frozen ones in `0_criteria.md` §3. The table below says how each was checked at the desk and what counted as a fail. Where the frozen text left room, the reading used is marked **[our call]**, and §8 asks the founders to confirm the readings that change results.

| # | Frozen test (short) | How it was checked here | Counted as a fail when |
|---|---|---|---|
| K1 | Distinct and internally alike | Distinct: S1's sign check (`1_candidates.md` §5). Every card differs from its nearest neighbours on at least two of R02's five signs. Alike: the members share the job and the need | The members plainly have different needs, or the card duplicates a neighbour. **None did** |
| K2 | One market on each side, not too big | On each side: same product, same sales process, and word of mouth.<br>• A card that mixes products or sales processes is split and re-tested (S2 step 3). None needed it.<br>• A card that is one market but spans several industries or regions, too many for its buyers to talk to each other, is marked **S**. The split variable is named, and the split is made at segment selection, as S1's merge M-1 already did for industry **[our call; P-5]** | Never. A K2 failure splits a card; it does not drop it |
| K3 | Identifiable and reachable | At least one paying side can be named from a public list or database and reached through a channel where buyers gather. Lists: FMCSA, CBP, FMC, PACA, the Census, association rolls | No paying side can be named or reached. **None failed.** Hard-to-reach sides are noted (farmers, households) |
| K4 | Measurable | The buyer count and the cost base of the savings pool come from named data. "?" where the cost base rests mostly on vendor claims or search snippets | Neither the count nor the cost can be estimated from any named source. **None failed** |
| K5 | Big enough: a fee pool of about $25M or more | Savings pool range (check K for 23 cards; §4.1 for the other 17) × the S0 fee shares.<br>• **Pass:** a 10% share of the low end reaches $25M, i.e. a pool of $250M or more.<br>• **Fail:** a 35% share of the high end is clearly below $25M, i.e. a pool well under $71M.<br>• **Unknown:** anything between.<br>These lines were set before the estimates came in **[our call]**.<br>One reading was added afterwards: a generous case within a few percent of $25M counts as "about $25M" (the frozen wording), so it is unknown, leaning fail. It affects only C-31, whose generous case is $24.5M. On a strict $25M line C-31 would fail.<br>**Accepted by the founders, 2026-09-15** ("This is good."). It is now the K5 desk rule in `submarket_selection.md` §5.1 (C13) | Even the most generous inputs, taken together, fall clearly short |
| K6 | Software can fix it | The card's target cost, or a separable part of it, comes from information, coordination or paperwork. Where only part does, the K5 pool counts only that part | The cost is physical, or set by a market or a government, with no information lever. **None failed; three are "?"** |
| K7 | Saving measurable and attributable | A countable outcome with a baseline, which a customer would credit to software. "?" where the saving is mostly risk avoided, or is measured against a moving market price. These are the two weak fits named in `submarket_selection.md` §7, which labels them *assumed* until S5 | The outcome cannot be counted at all. **None failed** |
| K8 | Someone can and will pay | A party holds the budget, sees the cost on its own P&L, and pays for the job today (a service firm, software or staff), or could buy from a startup | Nobody pays for the job and nobody's P&L shows it. **None failed** |
| K9 | Team would commit | Passes for every card (F-16) | — |
| K10 | Not in the "land of the giants" | Top-50 share of each side's industry, at 6-digit NAICS where published (N-D01, re-parsed). Pass at 75% or less; fail above 85%; 75-85% is unknown. For the unknowns, S3's small-firm check was run in advance from SUSB 2022 (N-D04) and is shown in §4.2 | Both sides fail (C11). **None did** |
| K11 | Durable | **Test 1, for each side:** the BLS 2025-35 projection (N-J01), census firm counts for 2022 against 2017 (N-D01), and substitutes (N-J Part 3). Fail if two of the three point to decline. Where BLS publishes no output for a row, its employment projection is read alone **[our call]**.<br>**Test 3, for each card:** the unit the saving is counted in, named in §4.3, peak to trough in 2008-09 and 2022-25 (N-H, N-J). Pass at 13% or less, or a rise. Fail above 20% in either downturn. 13-20%, or no data, is unknown.<br>• Only a proxy was found for many units. The closest one was used, and it is named. Physical measures were preferred over dollars.<br>• Where monthly (or 12-month rolling) and annual data fall in different bands, the finer data was used, because the test measures peak to trough **[our call]**.<br>• Where parts of a card fall in different bands, the card-level unit decides, and the failing segments are recorded for segment selection **[our call; P-7]** | Test 1 fails on both sides, or Test 3 fails. The Test 3 unit is the same for both sides, so a Test 3 fail removes the card. **Six cards failed Test 3; none failed Test 1** |

---

## 4. Evidence by test

### 4.1 K5: savings pools

**How the numbers were built:**
- **23 cards** come from check K (`research/s2_check_K_savings_pools.md`), which shows the arithmetic for each card.
- **The other 17** were estimated here from sources the project already held (table below).
- Every range multiplies the low inputs together for the low end and the high inputs together for the high end. So each range is wide by design.

**The K5 lines [our calc]:**
- **Pass:** savings pool of $250M or more at the low end. A 10% fee share of that is $25M.
- **Fail:** high end clearly under about $71M. Even a 35% fee share of that is less than $25M.

**The central fee pool** is 20% of the range's midpoint (the geometric mean of low and high).
- It is shown only to indicate which way each unknown leans. It is not the test.
- Under $25M is marked **leans fail**.

| Card | Savings pool a year (low-high) | K5 | Central fee pool | Label | Where |
|---|---|---|---|---|---|
| C-01 Buying truckload capacity | $0.52-4.6B | ✓ | $311M | mostly assumed | below |
| C-02 Load status | $0.18-0.73B | ? | $73M | mixed | below |
| C-03 Detention and extra charges | $0.27-0.64B | ✓ | $83M | mixed | below |
| C-04 Dock appointments | $0.14-0.36B | ? | $46M | mixed | below |
| C-05 Getting small carriers paid | $0.07-1.4B | ? | $62M | mostly assumed | below |
| C-06 Matching spot loads | $0.06-1.2B | ? | $55M | mostly assumed | below |
| C-07 Small brokerage back office | $0.28-1.3B | ✓ | $122M | mixed | below |
| C-08 Carrier vetting and fraud | $0.15-0.59B | ? | $59M | mostly assumed | below |
| C-09 Auditing and paying freight bills | $0.34-3.2B | ✓ | $210M | mostly assumed | below |
| C-10 Cargo claims | $70-370M | ? | $32M | mostly assumed | check K |
| C-11 LTL disputes | $0.10-0.90B | ? | $60M | mostly assumed | below |
| C-12 Parcel invoice audit | $0.10-0.83B | ? | $59M | mostly assumed | below |
| C-13 Big-and-bulky home delivery | $100-610M | ? | $50M | mixed | check K |
| C-14 Planning and consolidating | $0.61-5.4B | ✓ | $363M | mostly assumed | below |
| C-15 Routing own fleets | $1.6-8.1B | ✓ | $725M | mostly assumed | below |
| C-16 Job-site deliveries | $25-310M | ? | $18M, leans fail | mixed | check K |
| C-17 Inbound freight | $0.51-5.3B | ✓ | $320M | mostly assumed | check K |
| C-18 Warehouse bills | $110-900M ($28-225M if only warehouses under 20 staff) | ? | $64M | mixed | check K |
| C-19 OTIF fines and deductions | $0.11-1.44B | ? | $80M | mixed | below |
| C-20 Import entries | $0.10-0.64B | ? | $49M | mixed | below |
| C-21 Container D&D | $93-279M | ? | $32M | mostly verified | check K |
| C-22 Drayage dispatch | $67-268M | ? | $27M | mostly assumed | check K |
| C-23 International quoting | $127-707M | ? | $60M | mixed | check K |
| C-24 Export documents | $23-114M | ? | $10M, leans fail | mostly assumed | check K |
| C-25 Laredo | $50-177M | ? | $19M, leans fail | mixed | check K |
| C-26 Produce rejections | $10-274M | ? | $11M, leans fail | mixed | check K |
| C-27 Border produce | $7-82M | ? | $5M, leans fail | mixed | check K |
| C-28 Harvest grain | $34-314M | ? | $21M, leans fail | mixed | check K |
| C-29 Rail and barge buying | $36-109M | ? | $13M, leans fail | mixed | check K |
| C-30 Rail demurrage | $40-236M | ? | $19M, leans fail | mixed | check K |
| C-31 Livestock | $11-70M (generous case $24.5M) | ? | $6M, leans fail | mixed | check K |
| C-32 Milk hauling | $29-148M | ? | $13M, leans fail | mostly verified | check K |
| C-33 Cut flowers | $3.5-21M (generous case $7.4M) | ✗ | $2M | mixed | check K |
| C-34 OS/OW permits | $39-260M | ? | $20M, leans fail | mixed | check K |
| C-35 Tank loads | $9-227M | ? | $9M, leans fail | mostly assumed | check K |
| C-36 Aggregates tickets | $92-417M | ? | $39M | mixed | below |
| C-37 Log tickets | $15-72M (generous case $25.2M) | ? | $7M, leans fail | mixed | check K |
| C-38 Fuel reconciliation | $28-164M | ? | $13M, leans fail | mixed | check K |
| C-39 Vehicle transport | $31-282M | ? | $19M, leans fail | mostly assumed | below |
| C-40 Household moves | $46-276M | ? | $23M, leans fail | mixed | check K |

**The 17 estimates made here.** Each is cost base × avoidable share × share that software could remove.
- **Labels:** the counts and bases are *verified* unless marked; every share is **[our call]**; all arithmetic is **[our calc]**.
- **Three bases are *assumed*:** the 2024 spend figures from CSCMP's *State of Logistics*, read through a FreightWaves summary (N-K22): truckload $387B, LTL $64B, private fleets $541.4B.
- **The mid-sized shippers' share** (15-30%) is the same call check K used for C-17.

| Card | Cost base | Avoidable and removable shares | Savings pool |
|---|---|---|---|
| C-01 | Mid-sized shippers' truckload spend: $387B (N-K22) × 15-30% = $58-116B | Overpaying when capacity is bought by phone and email: 3-8%. Removable: 30-50% | $58B × 3% × 30% = **$0.52B**; $116B × 8% × 50% = **$4.6B** |
| C-02 | Status-checking wages: 53,390 cargo and freight agents at brokers and forwarders (N-F22) × $57,230 mean wage (N-K09) = $3.06B | Time spent on status: 20-40%. Removable: 30-60% | **$0.18-0.73B** |
| C-03 | Detention's yearly cost to drivers and carriers: $1.1-1.3B of lost driver earnings plus $250.6-302.9M of carrier net income (N-F30, 2018) = $1.35-1.60B | Recovered through better capture: 20-40%. A vendor says manual processes capture only about 40% of the detention owed (N-D34, *assumed*) | **$0.27-0.64B** |
| C-04 | Detention that facilities pay: carriers' direct detention cost of $3.6B (N-C24) × about 40% billed and collected (N-D34, *assumed*) = $1.44B. Carriers' $11.5B of lost productivity is left out, because carriers do not usually pay for dock scheduling | Wait time cut by appointments: 10-25% | **$0.14-0.36B** |
| C-05 | Small carriers' revenue: $222.6B **[our calc]** = nonemployer trucking receipts of $112.9B (N-D05) + the receipts of firms under 20 staff, $109.7B (SUSB, N-D04: 24.3% of truckload, 51.7% of local, 33.5% of local specialized, 18.4% of long-distance specialized) | 20-40% of it factored × fees of 1-4% (N-F40, vendor). Removable: 15-40% | **$0.07-1.4B** |
| C-06 | Owner-operators' dispatch fees: 274,660 one-truck carriers (N-F02) × 10-30% using dispatch services × $150-250k gross × fees of 5-10% (N-F39, vendor) | Removable: 30-60%. Empty miles are left out, because no deadhead share was sourced | **$0.06-1.2B** |
| C-07 | Small brokerages' wages: 164,684 employees of 488510 firms under 500 staff (N-K05) × 50-70% in truck brokerage × $57,230 = $4.7-6.6B | Time on re-keying, tracking, documents and payables: 20-40%. Removable: 30-50% | **$0.28-1.3B** |
| C-08 | Cargo theft of ~~$733.6M: 3,625 incidents × $202,364 (N-C23)~~ *corrected 2026-09-15 at S3a:* about $454M, because only 2,243 of 2024's 3,607-3,625 crime events were confirmed thefts, at $202,364 each (N-N24; `3a_unknowns.md` §4.4). Plus fraud and double-brokering losses, not sourced; up to the same again **[our call]**. Total ~~$0.73-1.47B~~ (S3a's revised range: $91-690M) | Prevented by vetting: 20-40% | **$0.15-0.59B** (superseded at S3a) |
| C-09 | Mid-sized shippers' truckload plus LTL spend: $451B (N-K22) × 15-30% = $68-135B | Overpayments: 1-3%, below the 2-8% that audit vendors claim (N-A26, N-A32). Caught by software: 50-80% | **$0.34-3.2B** |
| C-11 | Small shippers' LTL spend: $64B (N-K22) × 20-40% = $12.8-25.6B | Avoidable reweigh, reclass and extra-service overcharges: 2-5%. Vendors say reweigh and reclass fees add 10-20% (N-G23). Removable: 40-70% | **$0.10-0.90B** |
| C-12 | Parcel spend of e-commerce sellers under 500 staff: their receipts are $207B (SUSB 454110: $878.7B × 23.6%), × 5-10% spent on parcel | Recoverable errors and refunds: 2-5% (N-F52, N-F53, vendor). Removable: 50-80% | **$0.10-0.83B**. Firms under 20 staff only: $0.04-0.32B |
| C-14 | As C-09: $68-135B | Mode choice and consolidation: 3-8%, following the managed-transportation gainshare precedent (R33). Removable: 30-50% | **$0.61-5.4B** |
| C-15 | Private fleet cost: $541.4B (N-K22) × 15-30% for the card's distributors = $81-162B | Routing savings: 2-5% of fleet cost | **$1.6-8.1B**. Cross-check: 170,221 private-only fleets (N-F02) × $10-30k each = $1.7-5.1B |
| C-19 | Small and mid-sized suppliers' sales to big-box stores:<br>• warehouse clubs, supercenters and home centres sold $1,068B in 2022 (N-D01, re-parsed: $810.4B + $258.0B);<br>• × 70-75% bought from suppliers;<br>• × 15-30% from small and mid-sized suppliers (manufacturers under 500 staff hold 23.7% of manufacturing receipts, N-D04);<br>• = $112-240B | Invalid deductions and avoidable fines: 0.5-1.5% of those sales. Vendors say 5-7% of revenue is deducted and 10-20% of that is invalid (N-G36). Removable: 20-40% | **$0.11-1.44B** |
| C-20 | Formal entry summaries: 31.9M in FY2023 (N-H22) × 25-40% from small and mid-sized importers = 8.0-12.8M. They hold 30.2% of import value (N-E18) | Preparation cost of $40-100 per entry; broker fee levels were not found (check K). Removable: 30-50% | **$0.10-0.64B** |
| C-36 | Gravel and crushed stone: 1,910.9M tons (CFS 2022, N-E04) ÷ 22-25 tons a load = 76-87M loads | Ticket, reconciliation and dispute cost of $3-8 a load. Removable: 40-60% | **$92-417M** |
| C-39 | Vehicles moved by car haulers: 15.5M new light vehicles in 2023 (N-J17), plus 0-8M used vehicles at auction (volume not found, N-J) | Admin and damage-dispute cost of $10-30 a vehicle. Removable: 20-40% | **$31-282M** |

**What the table shows:**
- **Seven cards clear K5 even at a 10% fee share of their low end:** C-01, C-03, C-07, C-09, C-14, C-15, C-17. All seven are general-freight jobs for mid-sized shippers, carriers or brokers.
- **Only C-33 clearly fails.**
- **Twenty-nine are unknown.** On nearly all of them the swing comes from the removable share, which is our judgement on every card. S5's interviews and savings assessments are the only real source for it (`submarket_selection.md` §4 S5).

### 4.2 K10: the structure of each side

- **Source:** 2022 top-50 shares from the Economic Census (N-D01), re-parsed for US rows, all establishments. 6-digit codes where published.
- **"Pre-check":** S3's small-firm test (fail if firms under 500 employees hold less than 20% of revenue) applied now from SUSB 2022 (N-D04) to the sides in the 75-85% band.
- **Sides with no census row** (farms, importers, households) are described in words.

| Card | Shipper-side industries: top-50 share | Freight-company side: top-50 share | K10 |
|---|---|---|---|
| C-01, C-02, C-09, C-14, C-17 | Column X: manufacturing 29.0%, wholesale 30.5%. Their 6-digit codes run from fabricated metals (20.9%) to chemicals (46.5%) | Brokers and forwarders (488510) 34.3%; truckload (484121) 37.4%; LTL (484122) 82.9% | ✓ |
| C-03 | Column X; general warehousing (493110) 49.1% | Truckload 37.4%; long-distance specialized (484230) 38.1% | ✓ |
| C-04 | General warehousing 49.1%; refrigerated (493120) 73.9%; grocery wholesalers (4244) 53.5% | Truckload 37.4%; brokers 34.3% | ✓ |
| C-05, C-06, C-08 | Payers: brokers 34.3%; column X | Carriers: truckload 37.4%; local (484110) 10.5%; local specialized (484220) 9.9% | ✓ |
| C-07 | Column X | Brokers 34.3% | ✓ |
| C-10 | Column X | LTL 82.9% (?); truckload 37.4% | ✓ |
| C-11 | Fabricated metals (332) 20.9%; machinery (333) 35.8%; durable wholesale (423) 30.7%; furniture (337) 38.4% | LTL 82.9% (?). **Pre-check: firms under 500 hold 17.5% → fails at S3**, so the LTL side is ruled out | ✓ |
| C-12 | E-commerce sellers (454110; 2017 file, since 2022 NAICS dropped the code) 63.2% | Couriers (492110) 90.9% ✗ | ✓ (courier side ruled out) |
| C-13 | Furniture makers 38.4%; furniture retailers (449110) 54.0%; electronics and appliance retailers (449210) 74.4% | Local delivery (492210) 66.2%; local freight 10.5% | ✓ |
| C-15 | Grocery wholesale 53.5%; beer, wine and spirits (4248) 63.4%; hardware and plumbing (4237) 57.5%; **drug wholesalers (424210) 88.8% ✗**; meat processors (3116) 77.2% (?; pre-check 12.7% → fails at S3) | In-house fleets (no census row) | ✓ (drug wholesalers and meat processors ruled out as segments) |
| C-16 | Lumber and construction-materials wholesale (4233) 54.0%; other building-material dealers (444180) 28.2% | Own fleets; contractors (construction, 23) 11.4% | ✓ |
| C-18 | Customers: e-commerce 63.2%; durable wholesale 30.7% | General warehousing 49.1%; refrigerated 73.9% | ✓ |
| C-19 | Manufacturing 29.0% | Truckload 37.4%; brokers 34.3% | ✓ |
| C-20, C-21, C-22 | Importers: no industry code. Small and mid-sized importers hold 30.2% of known import value (N-E18) | Brokers and forwarders 34.3%; local freight (drayage) 10.5% | ✓ |
| C-23 | Importers (as above) | Brokers and forwarders 34.3%; scheduled air freight (481112) 98.6% ✗ | ✓ |
| C-24 | Exporters: 97.1% of 271,250 are small or mid-sized (N-E18) | Brokers and forwarders 34.3% | ✓ |
| C-25 | Manufacturing 29.0% | Brokers and forwarders 34.3%; local freight 10.5%; truckload 37.4% | ✓ |
| C-26, C-27 | Produce wholesalers (424480) 39.6%; farms (tens of thousands; not in the Economic Census) | Long-distance specialized 38.1%; local specialized 9.9%; brokers 34.3%; refrigerated warehousing 73.9% | ✓ |
| C-28 | Grain wholesalers (424510) 74.6%; farm-product warehousing (493130) 64.5%; 330,930 grain farms | Local specialized 9.9% | ✓ |
| C-29 | Grain wholesalers 74.6% | Railroads: six Class I roads hold 89% of rail revenue (N-F13) ✗; inland water freight (483211) 95.1% ✗ | ✓ (freight side ruled out) |
| C-30 | Chemicals (325) 46.5%; plastics and rubber (326) 33.2%; paper (322) 68.9%; recyclables wholesale (423930) 46.8%; grain milling (3112) 89.0% ✗ | Railroads ✗ | ✓ (railroad side and grain millers ruled out) |
| C-31 | Ranches and feedlots (farms); livestock wholesalers (424520) 79.6% (?; **pre-check 97.1% → passes**) | Local specialized 9.9%; long-distance specialized 38.1% | ✓ |
| C-32 | Dairy farms; dairy processing and co-ops (3115) 75.3% (?; pre-check 18.7% → fails at S3) | Local specialized 9.9% | ✓ (co-op and processor side ruled out) |
| C-33 | Flower wholesalers (424930) 54.0% | Scheduled air freight 98.6% ✗; customs brokers 34.3% | ✓ |
| C-34 | Machinery 35.8%; construction 11.4% | Long-distance specialized 38.1%; local specialized 9.9% | ✓ |
| C-35 | Chemicals 46.5%; chemical wholesalers (4246) 57.9% | Long-distance and local specialized | ✓ |
| C-36 | Highway construction (237310) 26.8%; sand and gravel (212321) 48.1%; limestone quarrying (212312) 72.0%; ready-mix (327320) 50.2% | Local specialized (dump trucks) 9.9% | ✓ |
| C-37 | Logging (113310): not in the Economic Census; SUSB shows firms under 20 hold 64.8% of receipts. Sawmills (321113) 59.3% | Local specialized 9.9% | ✓ |
| C-38 | Fuel dealers (457210) 45.2%; petroleum wholesale (4247) 83.4% (?; pre-check 30.0% → passes); bulk stations (424710) 88.0% ✗; petroleum wholesalers (424720) 87.4% ✗ | Long-distance and local specialized | ✓ (bulk terminals ruled out as a segment) |
| C-39 | New-car dealers (441110) 20.5%; auto wholesale and auctions (423110) 88.8% ✗; car rental (532111) 95.5% ✗ | Long-distance specialized 38.1% | ✓ |
| C-40 | Households (no code) | Movers (484210) 37.2% | ✓ |

**Result:** as check D predicted, K10 removes no card at S2. What it does is rule out single sides and segments. These are carried to segment selection (P-8).

### 4.3 K11: durability

#### Test 1: no projected shrinking (one result per side)

**Sources:**
- firm counts from the Economic Census, 2017 and 2022 (N-D01, re-parsed);
- projections from BLS Table 2.11, 2025-35 (N-J01). Output is in chained 2017 dollars, so it is real;
- substitutes from check J, Part 3.

| Industry (code) | Firms 2017 → 2022 | BLS 2025-35, employment / output | Indicators pointing down |
|---|---|---|---|
| Truckload (484121) | 31,908 → 53,705 (+68.3%) | Truck: +2.1% / +23.9% | none |
| Local general freight (484110) | 29,977 → 43,243 (+44.3%) | as truck | none |
| LTL (484122) | 4,410 → 7,675 (+74.0%) | as truck | none |
| Local specialized (484220) | 29,544 → 31,927 (+8.1%) | as truck | none |
| Long-distance specialized (484230) | 9,222 → 10,701 (+16.0%) | as truck | none |
| Movers (484210) | 7,668 → 9,519 (+24.1%) | as truck | none |
| Brokers and forwarders (488510) | 15,097 → 17,130 (+13.5%) | +5.3% / not published (transport support 487-88 output +26.7%) | none |
| Couriers (492110); local delivery (492210) | +55.5%; +28.0% | +4.1% / +24.7% | none |
| General and refrigerated warehousing (493110, 493120) | +21.7%; +9.8% | +2.0% / +28.1% | none |
| Scheduled air freight (481112) | 185 → 184 (-0.5%) | Air: +6.2% / +28.4% | firm count |
| Inland water freight (483211) | +12.4% | Water: +2.9% / +26.8% | none |
| Rail (482) | not in the Economic Census | +0.2% / +10.1% | none |
| Manufacturing (31-33); wholesale (42) | -3.4%; -10.7% | Wholesale +2.1% / +26.9%. Every manufacturing row has positive output except motor-vehicle parts | firm count |
| Furniture makers (337) | -0.8% | -6.3% / +4.9% | firm count |
| Furniture stores (442 → 449110) | not comparable (codes regrouped) | -9.1% / not published | projection |
| Livestock wholesalers (424520) | -18.2% | Farm-product raw materials: 0.0% / not published | firm count |
| **Petroleum bulk stations (424710)** | 2,296 → 1,855 (-19.2%) | Petroleum and paper wholesale: -1.4% / not published | **two of three: this side fails** |
| **Fuel dealers (454310 → 457210)** | 4,639 → 3,984 (-14.1%; the code was renumbered, not redefined) | -8.2% / not published | **two of three: this side fails** |
| Motor-vehicle parts (3363) | -5.5% | -13.9% / -24.6% | two of three (not a whole side on any card) |

**Substitutes (N-J Part 3):**
- **Found on four cards:**
  - C-34: states' self-issue permit portals. 85% of Washington's 183,502 permits were self-issued in 2023 (N-J23).
  - C-38: electric vehicles and efficiency. EIA's 2026 outlook has gasoline down 7.1% by 2030 and 21.9% by 2035 (N-J04).
  - C-36: e-ticketing run by state transportation departments in 10 states (N-J31).
  - C-24: USDA's electronic phytosanitary certificates (N-J34).
- **At scale nationally by about 2031:** none of them.
- **Everywhere else:** none found. Driverless trucks are running "10 trucks" (Dec 2025) against a target of more than 200 by the end of 2026 (N-J32). That is not scale.

**Result:**
- **No card fails Test 1.** Every card has a side where at most one indicator points down.
- **One card has a side that fails:** C-38's marketer side (fuel dealers and bulk terminals). Its carrier side passes, so the card stays. The decline is recorded for S3 and for W6.

#### Test 3: no drastic fall in the unit a fee would be counted on

**How to read it:**
- **Bands:** ≤13% passes, 13-20% is unknown, >20% fails.
- **Data:** where only annual data is named, the figure is annual. Otherwise it is monthly or 12-month rolling.
- **Labels:** *verified* unless marked. All percentages are from checks H and J.

| Card | Unit, and the series used | 2008-09 | 2022-25 | Test 3 |
|---|---|---|---|---|
| C-01, C-02, C-05, C-14, C-17 | Truckloads, shipments or invoices. Proxy: ATA truck tonnage (N-H01) | -14.6% | -5.5% | ? |
| C-03 | Detained stops. No series exists, only the GAO 2010 and ATRI 2023 snapshots (N-H34, N-C24) | not found | not found | ? |
| C-04 | Truck visits to docks. Proxy: truck tonnage; warehousing real output and jobs as secondary proxies (N-H21, N-C08) | -14.6% (output -2.4%, jobs -8.1%) | -5.5% (output rose) | ? |
| C-06 | Spot loads. DAT's volume index, which mixes spot and contract loads; December points only (N-H36 to N-H38, *assumed*) | not found | about -1% | ? |
| C-07 | Brokered loads. Firm counts only (N-H04 to N-H06, N-H12, N-H14):<br>• 2008-09: C.H. Robinson -0.8%, Landstar -12.6%;<br>• 2022-25: Landstar -21.6%, J.B. Hunt -48%; RXO and ArcBest rose | no industry series | no industry series | ? |
| C-08 | Fraud and theft incidents: FreightWatch, then CargoNet (N-H30 to N-H33, *assumed*) | rose (+12% in 2009) | rose | ✓ |
| C-09 | Freight invoices: Cass's invoice count (N-H03) | -10.5% | -6.4% | ✓ |
| C-10 | Cargo claims. Theft rose (as C-08). No claim counts were found, and damage claims probably follow shipments (13-20%) | not found | not found | ? |
| C-11 | LTL shipments. Carriers only (N-H08 to N-H13):<br>• 2008-09: Old Dominion -15.0%, Saia -7.1%, YRC -43.2%;<br>• 2022-25: Old Dominion -14.8%; Saia rose | no industry series | no industry series | ? |
| C-12 | Parcels. UPS and FedEx volumes; the Pitney Bowes index (N-H15 to N-H17; the industry index is *assumed*) | UPS -5.8%; FedEx Ground rose | industry about flat | ✓ |
| C-13 | Home deliveries. Proxy: furniture-store sales, inflation-adjusted (N-H18, N-H19) | **-27.0%** (annual -22.7%) | -20.6% (annual -14.1%) | **✗** |
| C-15 | Deliveries by distributors' own fleets. Proxy: real wholesale sales for grocery; beer and wine; drugs; hardware and plumbing (N-J21, N-J22) | -6.0%; -4.0%; -1.9%; **-26.8%** | -1.8%; -10.2%; rose; -4.7% | ✓ (hardware segment ✗) |
| C-16 | Job-site deliveries. Proxies: building-material dealers' real sales; lumber wholesale, real; housing starts (N-J19 to N-J22) | **-31.6%; -46.5%; -73.2%** | -10.1%; -14.8%; -15.3% | **✗** |
| C-18 | Billable warehouse activity. Proxy: warehousing real output (N-H21) | -2.4% | rose | ✓ |
| C-19 | Shipments to big-box stores. Proxy: real sales at general merchandise stores; clubs and supercenters; grocery (N-H18) | -4.7%; -4.2%; -6.4% | -7.0%; -6.4%; -7.8% | ✓ |
| C-20 | CBP entry summaries (N-H22) | not found | -7.1% (formal) | ? |
| C-21, C-22 | Loaded import containers:<br>• 2008-09: BTS/RITA, a lower bound (N-H26); MARAD, the ~21.5%, via snippet (N-H27, *assumed*);<br>• 2022-25: NRF (N-H23) | at least -15%; about -21.5% | -13.6% (annual) | ?, leans fail |
| C-23 | Containers as above; air cargo ton-miles (N-H28) | as above; air -22.7% (annual -19.8%) | -13.6%; air -11.8% | ?, leans fail |
| C-24 | Farm export tons. Proxy: bulk tons only (N-J05) | -19.7% | -11.8% | ? |
| C-25 | Northbound trucks at Laredo and across the whole border (N-H29) | -14.1% / -14.7% (annual -11.6% / -12.1%) | rose | ? |
| C-26 | Produce truck shipments (N-J06) | rose | -11.3% | ✓ |
| C-27 | Produce crossings: Nogales; Texas ports as the proxy for Pharr (N-J06) | -2.5%; rose | -7.9%; rose | ✓ |
| C-28 | Loads to elevators. Proxy: grain production (N-J05) | -1.9% | rose | ✓ |
| C-29 | Grain by rail (waybill sample; weekly series); grain by barge (N-J07 to N-J09) | rail -9.1%; barge -18.7% | rail -3.2% or -12.5%; barge **-28.4%** | ? |
| C-30 | Rail carloads, total (N-J10). Segments (N-J09): chemicals -8.8%, plastics -16.5%, **pulp and paper -21.7%, scrap -22.3%** | -19.9% | -2.1% | ? (paper and scrap segments ✗) |
| C-31 | Cattle loads. Proxy: slaughter (N-J05) | -2.9% | -13.8% | ? |
| C-32 | Milk production (N-J05) | -0.4% | -0.2% | ✓ |
| C-33 | Flower imports: weight; value (N-J12) | **-25.0%**; -8.0% (nominal) | -3.8%; rose | **✗** (weight) |
| C-34 | Oversize/overweight permits, Washington only (N-J23) | not found | rose (2022-23) | ? |
| C-35 | Chemical tank loads. Proxies: production of all chemicals and of basic chemicals (N-J13); chemical rail carloads (N-J09) | -18.4% and -35.8%; rail -8.8% | -7.5% and -9.6%; rail -1.2% | ? |
| C-36 | Aggregates output (USGS; N-J14 to N-J16) | **-36.9%** | -5.2% | **✗** |
| C-37 | Logs to mills. Proxies: wood-products output; rail lumber loads (N-J13, N-J09) | **-45.1%; -55.0%** | -10.6%; -6.5% | **✗** |
| C-38 | Fuel deliveries: gasoline plus distillate (N-J02). Segments: distillate -14.7%; **heating oil -33.3%** (N-J03) | -6.3% | -0.6% | ✓ (heating-oil segment ✗) |
| C-39 | Vehicles moved. Proxy: new light-vehicle sales (N-J17) | **-38.6%** | rose | **✗** |
| C-40 | Household moves. Census CPS movers, all and different-state (N-J18); NAR home sales (*assumed*) | all -12.2%; interstate -41.9% (-23.9% measured from 2006); NAR -40.8% | all -9.1%; interstate -8.0%; NAR -19.3% | ? (interstate segment ✗) |

**Where the proxy choice matters:**
- **C-04.** On truck tonnage it is unknown. On the warehouse proxies it would pass. Dock appointments count truck visits, so tonnage is closer to the unit.
- **C-35.** Chemical production says fail, but rail carloads of chemicals say pass. Rail carloads are a physical count, while production is output, so the result is unknown.
- **C-40.** Local and interstate moves land in different bands, and it is not known which dominates small movers' work. The result is unknown.
- **C-33.** Weight is closer to shipments than value is, so weight was used. The card fails K5 either way.

### 4.4 The other tests: every call that is not a plain pass

| Test | Card | Call | Reason |
|---|---|---|---|
| K3 | C-24 | ? | Farm and food exporters are not counted separately among the 271,250 exporters (check K). No list or channel was found beyond commodity export groups (*assumed*) |
| K3 | C-33 | ? | The number of Miami flower importers was not found |
| K3 | C-28, C-31, C-40 | ✓ (with notes) | Farmers, ranchers and households are costly to reach one by one: selling direct to farmers "hasn't worked" (R30). Each card has a reachable paying side (elevators, haulers and auction markets, movers) |
| K4 | C-05, C-06, C-08, C-10, C-11, C-12, C-17, C-18, C-19, C-22, C-24, C-26, C-33, C-34, C-35, C-37, C-39, C-40 | ? | The cost base rests mostly on vendor claims or snippets, or its volume was not found. Named on each row of §4.1 and in check K |
| K6 | C-27 | ? | Most of the border cost is set by government inspection and physical handling: inspection holds, cold-storage days, spoilage. Only the hand-off coordination is information |
| K6 | C-29 | ? | The cost is a market price for rail and barge capacity. Software's only lever is timing |
| K6 | C-33 | ? | CBP agricultural inspection drives the holds (N-G68) |
| K6 | C-13, C-25, C-26, C-31, C-40 | ✓ (part only) | Part of each card's cost is physical: damage, bridge queues, temperature, shrink, breakage. Check K counted only the information part in each savings pool |
| K7 | C-01, C-29 | ? | Rate savings are measured against a benchmark that swings. Truckload prices fell 24.1% and then rose 29.5% (N-C08). Barge rates went from 435% to 792% of tariff (N-G25). §7 calls this a poor fit for a fee |
| K7 | C-08, C-24, C-35 | ? | Much of the saving is risk avoided: fraud, document holds and rejections, fines. §7 says such a saving "cannot be counted or credited" (*assumed* until S5) |
| K7 | C-25, C-27, C-33 | ? | Border and inspection time depends mostly on CBP, so a customer may not credit software for a shorter crossing |
| K8 | all 40 | ✓ | Every card has a party paying for the job today: a spread, a contingency fee, a factoring discount, a subscription or staff time (the "How" line on each card). Evidence of software spend is thin for C-16, C-29, C-30 and C-33, but in each the cost sits on the buyer's own P&L |

### 4.5 K2: split flags

- **What an S flag means:** the card is one market on product and sales process, but it spans too many industries, regions or carriers for word of mouth.
- **When the split happens:** at segment selection (Q6), using the variable named below. That is how S1 treated industry (merge M-1).
- **Decided 2026-09-15 (C12):** these 17 cards will be split into segments, because the project targets segments, not whole sub-markets.
  - In the founders' words: "These will be split into segments, we are going to be targetting segments."
  - Each flagged card that reaches S3b names its split variable and likely segments on its fact sheet (`submarket_selection.md` §4 S3b, item 11).
  - Segment selection starts from them (`submarket_selection.md` §11).

| Split variable | Cards |
|---|---|
| Shipper industry (column X, M-1) | C-01, C-02, C-09, C-10, C-11, C-14, C-17, C-19, C-30 |
| Carrier fleet size or equipment | C-03, C-05, C-06 |
| Distributor type | C-15 |
| Importer size, industry or port | C-20, C-21, C-22 |
| Border gateway (Nogales, Pharr) | C-27 |

---

## 5. Dropped cards: the final record

**What the record holds.** The S2 step asks for each dropped card's "final 'score' for each of the matrices":
- **The knock-out matrix:** the card's row in §2.
- **The two scoring matrices:** Axis A ("is it worth winning?") and Axis W ("can we win?"). They are scored below at desk level, with the run-01 weights (`0_criteria.md` §4) and 1 / 0.5 / 0 per row.
- **Fee feasibility** (F1-F5) is a separate gate, not a matrix, and is not scored.

These scores are **provisional**. They are recorded only so that a drop can be challenged later. They are not used to rank anything, and survivors are scored in S3.

**How each row was scored [our call]:**

| Row | 1 | 0.5 | 0 |
|---|---|---|---|
| A1 (savings pool, by the range's midpoint) | above $250M | $71-250M | under $71M |
| A2 (fit for automation) | office work drives the cost | mixed | mostly physical |
| A3 (pain and urgency) | a forcing event | a known cost without one | little evidence |
| A4 (fragmentation) | the census band from `0_criteria.md` §4 | | |
| A5 (frequency) | every load | seasonal | one-off |
| A6 (expansion leverage) | several adjacent groups | one or two | none |
| W1 (access) | one channel gathers most buyers | partial | dispersed |
| W2 (team knowledge) | | | every card, until domain immersion (F-15) |
| W3 (whole product and time to value) | data at hand | integration needed | no data access |
| W4 (competition and substitutes) | both hold (C10 rule) | one holds | neither |
| W5 (willingness to change) | a mandate or evidence of the wish to change | neutral or unknown | resistance |
| W6 (time and resources to win) | fast | moderate | slow |

**Axis A (weights: A1 20, A2 10, A3 25, A4 15, A5 15, A6 15):**

| Card | A1 | A2 | A3 | A4 | A5 | A6 | **Axis A** |
|---|---|---|---|---|---|---|---|
| C-13 Big-and-bulky | 0.5 | 0.5 | 0.5 | 1 | 1 | 0.5 | **65** |
| C-16 Job-site deliveries | 0.5 | 0.5 | 0.5 | 1 | 1 | 0.5 | **65** |
| C-33 Cut flowers | 0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | **40** |
| C-36 Aggregates tickets | 0.5 | 1 | 1 | 1 | 1 | 0.5 | **82.5** |
| C-37 Log tickets | 0 | 1 | 0.5 | 1 | 1 | 0.5 | **60** |
| C-39 Vehicle transport | 0.5 | 0.5 | 0.5 | 0.5 | 1 | 0.5 | **57.5** |

**Axis W (weights: W1 20, W2 5, W3 20, W4 15, W5 15, W6 25):**

| Card | W1 | W2 | W3 | W4 | W5 | W6 | **Axis W** |
|---|---|---|---|---|---|---|---|
| C-13 Big-and-bulky | 0.5 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **47.5** |
| C-16 Job-site deliveries | 0.5 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **47.5** |
| C-33 Cut flowers | 1 | 0 | 0.5 | 1 | 0.5 | 0.5 | **65** |
| C-36 Aggregates tickets | 1 | 0 | 0.5 | 0.5 | 1 | 0.5 | **65** |
| C-37 Log tickets | 0.5 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **47.5** |
| C-39 Vehicle transport | 1 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | **57.5** |

**What each score rests on** (the census figures are from §4.2 and N-D04):
- **C-13:**
  - **A:** A1 uses a midpoint of about $250M. On A4, furniture retailers' top-50 share is 54.0%, and firms under 20 staff hold 26.1% of furniture-store receipts, which earns the small-firm bonus. Deliveries recur with every sale.
  - **W:** sellers pay 3PLs $10.15B a year (N-K04), so there is proven spend. Delivery software was not researched.
- **C-16:**
  - **A:** A4 gets the bonus. Other building-material dealers' top-50 share is 28.2%, and firms under 20 hold 25.0% of receipts. Deliveries go out daily.
  - **W:** no dealer software was found, and no forcing event.
- **C-33:**
  - **A:** the pool is tiny: a midpoint of about $9M.
  - **W:** reach is easy, since Miami handles about 88% of US cut-flower imports (N-G68). Importers pay brokers and handlers, and no specialized software was found. So W4 = 1.
- **C-36, the strongest dropped card on these scores:**
  - **A:** the cost is paper tickets. State transportation departments in 10 states are applying e-ticketing (N-J31), which is a forcing event (A3 = 1). The dump-truck side is fragmented (top-50 share 9.9%). Loads recur daily.
  - **W:** the mandates give it both a channel and a reason to change (W1 = 1, W5 = 1).
  - **Why it fails:** only the 2008-09 construction collapse removes it (-36.9%). Its 2022-25 fall was -5.2%.
  - **If the founders ever relax the 2008-09 half of Test 3,** C-36 is the first card to reopen.
- **C-37:**
  - **A:** A1 is 0, with a midpoint of about $33M. The paperwork fits automation, and the log-truck side is fragmented.
  - **W:** Logger's Edge serves more than 275 firms (vendor claim), so software exists.
- **C-39:**
  - **A:** car haulers and dealers are both mid-band on A4.
  - **W:** two marketplaces gather most of the market (Central Dispatch, Super Dispatch), so W1 = 1. They already offer electronic bills of lading and inspections, so W4 = 0.5.

---

## 6. Survivors: what S3 must settle

**How to read this table:**
- **Order:** by how the unknowns lean. Cards with a single unknown come first, and cards whose unknowns lean toward failing come last.
- **Lean** is not a call: it shows which way the desk evidence points.
- **Who settles them:** S3a, a short pass before any fact sheet is written (option C, C14).
  - It starts with the cards whose unknowns lean toward failing, at the bottom of this table.
  - Its exit rules are in `submarket_selection.md` §4 S3a.

| Card | Unknowns | What would settle them | Lean |
|---|---|---|---|
| C-09 Auditing and paying freight bills | none | — | clean pass |
| C-15 Routing own delivery fleets | none | — | clean pass |
| C-03 Detention and extra charges | K11 | No series of detained stops exists. S3 can accept the ATRI and GAO snapshots, or the founders can rule | pass |
| C-07 Small brokerage back office | K11 | An industry count of brokered loads (TIA market reports, not searched yet) | open |
| C-14 Planning and consolidating | K11 | A 2008-09 count of truckloads and LTL shipments; tonnage fell 14.6% | open |
| C-01 Buying truckload capacity | K7, K11 | K7: whether shippers credit software for rate savings against lane benchmarks (S5). K11: as C-14 | open |
| C-17 Inbound freight | K4, K11 | Neutral evidence on inbound overpay; K11 as C-14 | open |
| C-02 Load status | K5, K11 | Share of broker and shipper staff time spent on status; K11 as C-14 | pass on size |
| C-04 Dock appointments | K5, K11 | Savings per site (overtime, detention paid); which proxy fits dock visits | open |
| C-12 Parcel invoice audit | K4, K5 | Small sellers' parcel spend; neutral recovery rates; how the FedEx and UPS guarantee changes affect them (N-J28) | pass on size |
| C-18 Warehouse bills | K4, K5 | Neutral billing-leakage evidence; the firm-size scope the card means | pass on size |
| C-19 OTIF fines and deductions | K4, K5 | Neutral deduction and fine rates | pass on size |
| C-20 Import entries | K5, K11 | Preparation cost per entry; CBP entry counts for FY2007-FY2010 (DHS performance reports, not opened) | pass on size |
| C-05 Getting small carriers paid | K4, K5, K11 | Share of small-carrier revenue that is factored, and fee levels (factoring firms' filings); K11 as C-14 | pass on size |
| C-06 Matching spot loads | K4, K5, K11 | Use of dispatch services; spot-load counts for 2008-09 | pass on size |
| C-08 Carrier vetting and fraud | K4, K5, K7 | Fraud and double-brokering losses beyond theft; whether brokers credit vetting for losses avoided (S5) | pass on size |
| C-10 Cargo claims | K4, K5, K11 | Neutral claim filing and recovery rates; claim counts in 2008-09 | pass on size |
| C-11 LTL disputes | K4, K5, K11 | Neutral LTL correction rates; industry LTL shipments | pass on size |
| C-21 Container D&D | K5, K11 | Disputable share of the charges; 2006-09 loaded import TEU at source (MARAD) | K11 leans fail |
| C-22 Drayage dispatch | K4, K5, K11 | Current turn-time data; containers as C-21 | K11 leans fail |
| C-23 International quoting | K5, K11 | Forwarder time spent quoting; containers as C-21; air imports by direction | K11 leans fail |
| C-28 Harvest grain | K5 | Elevator queue cost per load; the number of elevator companies | K5 leans fail |
| C-32 Milk hauling | K5 | Counts of co-ops and haulers; the savings from routing pickups | K5 leans fail |
| C-38 Fuel reconciliation | K5 | Reconciliation cost per load; the marketer count (4,083 fuel dealers, against PMAA's 8,000) | K5 leans fail; marketer side declining |
| C-26 Produce rejections | K4, K5 | A neutral rejection rate and loss per load | K5 leans fail |
| C-30 Rail demurrage | K5, K11 | Class I demurrage for 2023-25 (STB filings); total carloads fell 19.9%, right on the line | K5 leans fail |
| C-31 Livestock hauling | K5, K11 | Admin cost per load; cattle slaughter fell 13.8% in 2022-25, following the herd cycle | K5 leans fail |
| C-25 Laredo | K5, K7, K11 | Customs-broker fees per crossing; whether ready documents shorten crossings; rolling against annual counts (-14.7% against -12.1%) | K5 leans fail |
| C-27 Border produce | K5, K6, K7 | Share of border cost that is paperwork; buyer counts at Pharr | K5 leans fail |
| C-34 OS/OW permits | K4, K5, K11 | A national permit count; a permit series for 2008-09; how far state self-issue portals substitute | K5 leans fail |
| C-40 Household moves | K4, K5, K11 | Neutral claims and estimating costs; which moves small movers mostly handle | K5 leans fail |
| C-29 Rail and barge buying | K5, K6, K7, K11 | Evidence of a timing premium; which rail series to use; barge weighting | K5 leans fail |
| C-35 Tank loads | K4, K5, K7, K11 | Tank-load counts; which chemical proxy to use | K5 leans fail |
| C-24 Export documents | K3, K4, K5, K7, K11 | A count of farm and food exporters; document-cost evidence; containerized farm export tons | K5 leans fail |

**For the origin hypothesis** (CLAUDE.md asks for evidence either way):
- All eight farm-origin cards (C-26 to C-33) have small savings pools at sub-market level. Their central fee pools run from $2M to $21M against a $25M floor, and C-33 fails outright.
- This does not test whether farmers lose profit to shipping. It says that the farm-origin freight jobs carded in S1 look small as software fee pools.
- The farm-side cost is mostly physical (shrink, spoilage), or a market price (barge and rail rates), or it sits with a few intermediaries.

---

## 7. Gate check, and options for the founders

**The gate.** "Roughly 8-15 survivors. Far more means the knock-outs are too loose. Far fewer means unknowns may have been treated as fails" (`submarket_selection.md` §4 S2). The range is **[our call]**, with no source behind it (§10). **Result: 34.**

**Why so many survive:**
1. **The desk cannot settle K5 for most cards.**
   - The share of a cost that software could remove is our judgement on every card, so the ranges span 3-50×.
   - Only S5's interviews and savings assessments will produce that share.
2. **The frozen durability test puts general freight in its "unknown" band.**
   - Truck tonnage fell 14.6% in 2008-09 (N-H01).
   - Several units have no industry-wide count at all: brokered loads, LTL shipments, spot loads, detained stops, and customs entries before 2021.
3. **K10 and Test 1 cannot remove a card at sub-market level.**
   - Rule C11 needs both sides to fail.
   - Every card has a fragmented trucking, brokerage or warehousing side whose firm count grew and whose projection is positive.
4. **S1 wrote the cards to meet most must-haves.** Every card is a software-addressable job with a named payer. So K1, K3, K6, K8 and K9 pass almost by construction.

**Options** (the counts are **[our calc]** from §4 and §6):

| Option | What it does | Survivors | For | Against |
|---|---|---|---|---|
| **A. Keep all 34** | S3 as written: a fact sheet for every survivor, then keep 4-6 on a provisional desk score | 34 | Follows the rule that unknowns go forward (R15), and nothing is dropped on a judgement call | Heavy: 34 fact sheets, against the 8-15 S3 was sized for |
| **B. Settle K5 now on the central case** | Drop cards whose central fee pool (20% of the midpoint) is under $25M: C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-34, C-35, C-38, C-40 | 21 | Fastest. Uses evidence already gathered | Treats "leans fail" as "fails", which is what the gate warns against. The removable share behind each drop is our judgement. It removes the whole farm-origin family on one assumption |
| **C. Split S3 in two** | **S3a:** a short pass (hours per card) that settles only the K5 and K11 unknowns, lean-fail cards first, using the "what would settle them" column in §6. **S3b:** full fact sheets only for the cards still standing | 34 enter S3a; likely under 20 reach S3b | Keeps "unknown goes forward". Spends S3's effort on the likeliest cards. Each drop comes from evidence, not from a lean | One more step. Some K5 unknowns cannot be settled at the desk, so S3a may still leave a set larger than 15 |
| **D. Re-set the gate** | Treat S2 as a floor filter, and let S3's provisional desk score do the narrowing to 4-6. S3 already has that step | 34 | No process change beyond the gate knob | Same workload as A, and the provisional score would rest on thin evidence for the lean-fail cards |

**Suggested starting point, [our call], not a decision: Option C.**
- It follows the process's own rule that unknowns are settled in S3, not treated as fails.
- It puts the effort where the leans point.
- The founders may prefer B for speed, knowing that it drops the fringe and farm-origin cards on one assumption: the share software could remove.

**Decision, 2026-09-15: option C.** The founders' answers follow.

### Founders' answers, 2026-09-15 (verbatim)

> "Yes, add a note about option C."
>
> On K10 and K11 Test 1: "We may reconsider how this test works since its a pass-through, add this to the document that specifies this test."
>
> On the K2 split flags: "These will be split into segments, we are going to be targetting segments. Ensure this is documented."
>
> On the K5 cut-offs and the "about $25M" reading: "This is good."
>
> "Add these to the documents, then I will move on with another Claude Code agent to S3."
>
> "Ensure the S3 process is updated according to what we have discovered."

**What each answer settles, and where it is written:**

| Item | Outcome | Where |
|---|---|---|
| The gate (P-9) | **Option C.** Read as choosing C, because the reply names option C and asks for the S3 process to be updated before moving on. S3 is now two steps:<br>• S3a settles the unknowns, lean-fail cards first, with a reserve list for size unknowns that still lean fail;<br>• S3b builds fact sheets for the rest | `submarket_selection.md` §4 S3a-S3b (C14) |
| K10 and K11 Test 1 as pass-throughs | **Flagged for review, not changed.** Both tests stay as frozen for run 01 | `submarket_selection.md` §5 and §5.1, §9 (T15); `0_criteria.md` §3; P-10 below |
| The K2 split flags (P-5) | **Decided.** The 17 cards flagged S are split into segments at segment selection, because the project targets segments | `submarket_selection.md` §4 S2 step 3, §5.1 K2, §11 (C12); `0_criteria.md` K2 |
| The K5 desk rule and the "about" reading (P-6) | **Accepted.** The central case sets the order of S3a's work but never fails a card by itself, so option B's use of it is not adopted | `submarket_selection.md` §5.1 K5, §10 (C13); `0_criteria.md` K5 |
| Updating S3 with what S2 found | **Done.** S3 gains the S3a pass. The fact sheet gains two lines: the unit a fee would be counted on, with the K11 series used (P-7 b-e); and the card's segments, including the sides and segments already ruled out (P-8) | `submarket_selection.md` §4 S3, §5.1 K11, §13 (C14, C15) |

---

## 8. Proposed process changes (not applied)

These follow the decision-record rule: nothing here changes `submarket_selection.md` or `0_criteria.md` until the founders sign it off. After sign-off, each change would be logged in §9 of the process doc. S1's proposals P-1 to P-4 are still open and untouched.

| # | Proposal | Reason |
|---|---|---|
| P-5 | **K2 at sub-market level.** When a card is one market on product and sales process but too big for word of mouth, flag it S with a named split variable, and make the split at segment selection. Write this into §5.1 | Aulet's three conditions describe the beachhead (R16), and here the beachhead is the segment. Splitting the 17 flagged cards now would reverse S1's merge M-1 and roughly double the list, and every piece would face the same tests as its parent |
| P-6 | **K5 at the desk.** Write the band rule into §5.1:<br>• pass: 10% of the low end reaches $25M;<br>• fail: 35% of the high end is clearly short of it;<br>• unknown between;<br>• "about" covers a generous case within a few percent of the line.<br>Also decide whether S3 settles K5 on the central case (Option B in §7) | The removable share is a judgement on nearly every card, so the desk ranges are wide. Without a written rule, K5 calls depend on who runs S2 |
| P-7 | **K11 Test 3 in practice:**<br>(a) add "the unit a fee would be counted on" to the S1 card template;<br>(b) use a proxy only when no count exists, prefer physical measures to dollars, and name it;<br>(c) where monthly and annual data differ across a band line, the finer data decides;<br>(d) one firm's volumes never stand for an industry;<br>(e) where parts of a card fall in different bands, the card-level unit decides and failing segments go to segment selection | S2 had to choose units for eight cards (C-04, C-08, C-10, C-15, C-30, C-35, C-38, C-40). Single firms ranged from growth to -48% in the same downturn (check H, H3 and H6) |
| P-8 | **Carry the segments ruled out here into segment selection:**<br>• LTL carriers (C-11);<br>• couriers (C-12);<br>• drug wholesalers and meat processors (C-15, K10), and hardware and plumbing distributors (C-15, K11);<br>• railroads and barge lines (C-29, C-30);<br>• grain millers, and paper and scrap shippers (C-30);<br>• dairy co-ops and processors (C-32);<br>• heating-oil dealers and bulk terminals (C-38);<br>• interstate moves (C-40, leaning) | K10 and K11 cannot drop a card when one side passes (C11), but they do rule out sides and segments. Without a record, segment selection would re-test them |
| P-9 | **The S2 gate.** Choose among Options A-D in §7, and set §10's "Survivors after knock-outs" knob to match | The 8-15 range has no source, and this run shows the frozen desk knock-outs cannot reach it in freight |
| P-10 | **Reconsider K10 and K11 Test 1 at sub-market level** (added 2026-09-15). Options include applying them only to the side we would sell to, once it is chosen, or applying them at segment level | Under C11 they removed no card in run 01, so they worked as pass-throughs. The founders flagged it: "We may reconsider how this test works since its a pass-through" |

**Status, 2026-09-15:**
- **P-5: accepted,** applied as C12.
- **P-6: accepted,** applied as C13. The central case is used only to order S3a's work.
- **P-7:** parts (b)-(e) applied as C15, under the founders' instruction to update S3 with what S2 found. Part (a), a new field on S1's card template, stays proposed for future runs.
- **P-8: applied** as part of C15. Ruled-out sides and segments go on each fact sheet and into segment selection.
- **P-9: option C chosen,** applied to S3 as C14.
- **P-10: open** (tension T15).
- **S1's P-1 to P-4:** still open, untouched.

---

## 9. Sources

**New inputs made for this stage.** Their full entries (URL, date, access and what was read) are in each file:

| File | IDs | What it covers |
|---|---|---|
| `research/s2_check_H_downturns_freight.md` | N-H01 to N-H39 | 2008-09 and 2022-25 falls for 15 freight and trade units, from filings (Cass, C.H. Robinson, Landstar, J.B. Hunt, Werner, Old Dominion, Saia, Con-way, YRC, ArcBest, XPO, RXO, UPS, FedEx), FRED/ATA, Census retail, BLS, CBP, NRF, BTS/RITA, BTS air and border data, CargoNet and DAT |
| `research/s2_check_J_downturns_other_and_projections.md` | N-J01 to N-J37 | 17 farm, industrial and consumer units, from USDA PSD and AgTransport, the STB waybill sample, BTS/AAR, UN Comtrade, Federal Reserve G.17, USGS, EIA, BEA, Census CPS, starts, retail and wholesale; BLS Table 2.11 projections; EIA AEO2026; substitutes |
| `research/s2_check_K_savings_pools.md` | N-K01 to N-K45 (N-K02, N-K17 and N-K44 unused) | Savings pools for 23 cards, from FMC, BTS, USDA, NASS, AAR, EIA, TxDMV, Census SUSB, BLS OEWS and vendor sources (labelled *assumed*) |

**Census files re-parsed here (the IDs are from check D):**
- **N-D01**, Economic Census concentration files: EC2200SIZECONCEN.zip (released 10 Apr 2025) and EC1700SIZECONCEN.zip, from www2.census.gov/programs-surveys/economic-census/data/{2022,2017}/sector00/.
  - Filtered to the US (GEO_ID 0100000US) and all establishments (TYPOP 00).
  - Firm concentration codes 001 (all firms), 604 (4 largest) and 650 (50 largest): firms, receipts, top-4 and top-50 shares, and HHI with its flags. About 130 codes were extracted.
- **N-D04**, SUSB 2022: us_state_naics_detailedsizes_2022.xlsx.
  - US rows only; enterprise sizes "01: Total", "06: <20 employees" and "19: <500 employees".
  - Receipt shares are **[our calc]**. SUSB 2022 still uses 2017 NAICS codes (for example 454110 and 442110), which the 2022 Economic Census renumbered.

**Earlier sources cited in this file:**
- **Resource notes:** R15, R16, R20, R21, R25, R30, R33, R38, R44.
- **S0 checks:** N-A25, N-A26, N-A32; N-B04, N-B16, N-B17; N-C08, N-C11, N-C13, N-C15, N-C23, N-C24; N-D05, N-D30, N-D34.
- **S1 scans:** N-E02, N-E04, N-E17, N-E18; N-F02, N-F13, N-F22, N-F30, N-F31, N-F39, N-F40, N-F52, N-F53; N-G23, N-G25, N-G36, N-G55, N-G68.

**Not re-fetched.** As at S1, card figures reused from earlier stages were not re-fetched here. S3 re-checks any figure a fact sheet relies on.

**Access limits:**
- Paywalled or blocked: AAR's commodity reports for 2007-10, MARAD's container file, the AHAM shipment file, NAR's history file, and the Federal Register and FMCSA pages.
- Not found: CBP entry counts before FY2021, spot-load volumes before 2016, permit counts before 2019, and cut-flower stem counts.
- Details are in the "could not access" section of each check. The scholarly-search server was not connected in this session.
