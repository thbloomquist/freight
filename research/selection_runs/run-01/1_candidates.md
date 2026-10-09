# Run 01, S1: candidate sub-markets (the long list)

> **Stage S1 of `submarket_selection.md` §4, "Enumerate candidates". Written 2026-09-14** under the frozen criteria sheet `0_criteria.md`.
> **Output:** 40 candidate cards (C-01 to C-40), plus 5 reserve niches (R-1 to R-5) that are listed but not carded. **Gate:** passed (§6).
> **Evidence:**
> - the resource notes (R-IDs) and the S0 checks (N-A to N-D);
> - three web scans done for this stage, kept in `research/`:
>   - `s1_scan_E_shipper_side.md` (sources N-E);
>   - `s1_scan_F_freight_company_side.md` (N-F);
>   - `s1_scan_G_outside_grid.md` (N-G).
>
> Card figures come from those files. S3 re-checks any figure it relies on.
> **Nothing here is scored, knocked out or ranked.** Knock-outs start at S2. A card on this list may well fail one later. That is expected: some are fringe on purpose (R15).

## How to read this

**What a card is.** Every candidate is one sentence in the standard form (`submarket_selection.md` §2.2):

> "[shipping job] for [shipper group], handled today by [freight-company type or method]"

Worked example, card C-21:
- The sentence: *"Avoiding and disputing container demurrage and detention charges, for small and mid-sized importers, handled today by their forwarders, customs brokers and port truckers."*
- The **shipper group** (small importers) is Abell's "who".
- The **job** (stop paying daily fees on containers) is the "what".
- The **freight-company type** (forwarders, brokers, truckers) is today's "how" (R05, R06). Software would be a new "how".
- The card then records four roles:
  - whose cost falls: the importer. Nine ocean carriers billed about $8.9B of these fees in 2020-22 (N-G01).
  - who decides;
  - who pays;
  - which side is harder to win.
- It names the person who does the work on each side, and checks the candidate against R02's five signs of a real sub-market.

**How the list was built** (the five S1 steps):
1. Three axes were drawn up from data: 19 shipper groups, 8 jobs and 17 freight-company types (§1).
2. They were crossed in a grid (§2).
3. Candidates were added from outside the grid: five shipment chains walked hand-off by hand-off, investors' pain maps, and 21 fringe niches (§3).
4. Each candidate was written as a card (§4).
5. The cards were checked against R02's signs and near-duplicates merged (§5).

**IDs.**
- G = shipper group (who).
- J = job (what).
- H = freight-company type or method (how).
- C = candidate card.
- R = reserve niche.
- M = merge decision.

**Labels.**
- *verified*: the source says it.
- *assumed*: secondary, vendor, search snippet or inference.
- **[our call]**: a design choice made in this stage.
- **[our calc]**: arithmetic done here.

Vendor figures are always *assumed*. The three scans use (V)/(A) or [V]/[A] for the same two labels.

**Freight words used here**

| Term | Meaning |
|---|---|
| Truckload (TL) | One shipper's goods fill a trailer that goes straight from A to B |
| LTL | Less-than-truckload: many shippers' pallets share trailers through carrier terminals, priced by freight "class" |
| Reefer | A refrigerated trailer |
| Drayage | Short truck moves of containers to and from ports and rail ramps. At trade shows the same word means material handling |
| Broker | A licensed firm that arranges trucks for shippers without owning trucks, and keeps the difference ("spread") |
| 3PL | Third-party logistics provider: an outside firm that runs some of a shipper's logistics |
| Forwarder / NVOCC | Arranges international shipments. An NVOCC issues its own bill of lading but runs no ships |
| Customs broker | Licensed by CBP to file import entries and pay duty for importers |
| Bill of lading (BOL) / proof of delivery (POD) | The shipping contract and receipt / the signed delivery receipt |
| Accessorials | Extra charges beyond the base rate: detention, liftgate, lumper and so on |
| Detention / demurrage | Charges for holding a truck (detention) or a container or railcar (demurrage) past its free time |
| Lumper | A third-party crew that unloads trucks at a warehouse, usually paid per load |
| Factoring / quick pay | Selling an unpaid freight invoice for cash now, minus a fee / a broker paying a carrier early for a discount |
| OTIF | "On time, in full": a retailer's delivery standard, with fines for misses |
| TMS | Transportation management system: software to plan, buy, track and pay for shipments |
| EDI | Electronic data interchange: an old machine-to-machine standard for orders, tenders and invoices |
| Owner-operator | A trucker who owns and drives their own truck, often under their own authority |
| Private fleet | A shipper's own trucks ("in-house fleet") |
| PACA | The Perishable Agricultural Commodities Act: licensing and payment law for produce traders |
| Scale ticket | The weight and grade record for a truckload of grain, logs or aggregates |
| OS/OW | Oversize/overweight loads, which need a permit from each state crossed |
| FMCSA | The federal regulator that registers carriers and brokers. Its counts come from self-reported forms |
| NAICS / SCTG | Industry codes / commodity codes used by Census and the freight surveys |

**Contents**
1. The three axes
2. The grid
3. Candidates from outside the grid
4. The cards
5. Sub-market signs and merges
6. Gate check and coverage
7. Notes for S2, deferred items and proposals
8. Sources

---

## 1. The three axes (S1 step 1)

### 1.1 Who: shipper groups (the columns of the grid)

Built from the Commodity Flow Survey (CFS 2022; R32, N-E01 to N-E07), the Freight Analysis Framework (FAF5, 2024 flows; R31, N-E09), USDA counts (N-E10 to N-E16), Census firm-size data (SUSB 2022, N-E17) and the importer/exporter profile (N-E18). The CFS covers mining, manufacturing, wholesale, e-commerce and company warehouses; it leaves out farms and imports, so FAF and USDA fill those in (R32 note). "For-hire" = a trucking company paid to haul; "own truck" = the shipper's own fleet; "customer pick-up" = the buyer collects the goods. Tons and value are *verified* (downloaded tables, N-E); shares are **[our calc]** from them.

| ID | Shipper group (plain words) | Codes | How its freight moves | Firms and size | Notes used on the cards |
|---|---|---|---|---|---|
| G01 | Food and beverage manufacturers | NAICS 311, 312 | Food: 614.2M tons, $1,033.5B, avg 421 mi. For-hire truck 51.8% of tons, own truck 14.7%, rail 11.8%, customer pick-up 10.9% | 25,675 food + 11,382 beverage firms; 74-80% have under 20 employees; firms under 500 employees earn about 21% of receipts | 21% of all temperature-controlled tons start here (N-E06). Many sell to big-box retailers (G15) |
| G02 | Grocery and food distributors | 4244 | 351.4M t, $988.5B, avg 103 mi. **Own truck 61.5%** of tons, for-hire 31.2% | 27,458 firms; 82.9% under 20 employees | Largest single origin of temperature-controlled freight (23.4% of it) |
| G03 | Fresh-produce grower-shippers, packers and wholesalers | Farms 1112, 1113; wholesalers 424480; SCTG 03 | FAF 2024: SCTG 03 is 741.9M t, 83.7% by truck (includes soybeans). Produce by truck: 7.76M t in Q1 2026, 45% from Mexico (R34) | 41,793 vegetable and 97,343 fruit farms; 4,480 produce wholesalers (73.4% of receipts in firms under 500); over 13,200 PACA licensees (2020) | Farm-origin family (§8.4 of the process doc) |
| G04 | Grain and oilseed farms and country elevators | 1111; 4245, 424510; SCTG 02 | All grain 2022: truck 62%, rail 26%, barge 12%. Domestic grain 80% truck; export grain 45% rail, 44% barge (N-E10) | 330,930 grain farms; 7,922 off-farm storage facilities (Dec 2024); 1,839 grain-wholesaler firms | Farm-origin family; the "messy middle" of R30 |
| G05 | Livestock, dairy and meat producers | 1121-1123; 3116; SCTG 01, 05 | Live animals: 97.6M t, 99.8% truck (FAF 2024). Meat and seafood: 120.0M t; for-hire 48.6%, own truck 32.4% | 534,633 beef ranches, 11,186 feedlots, 23,153 dairies, 21,865 hog and 75,597 poultry farms; 1,221 auction markets (FY2022) | Farm-origin family |
| G06 | Chemical, plastics and fuel makers and distributors | 324, 325, 326; 4246, 4247 | Chemicals: 776.1M t, avg 852 mi; for-hire 28.6%, rail 21.5%, pipeline 18.9%. Chemical wholesalers: own truck 45.1%. Hazmat is 21.3% of all CFS tons | 10,455 chemical and 8,369 plastics firms | Hazmat papers; tank trucks and railcars |
| G07 | Building-materials, aggregates and wood-products shippers (and the job sites they deliver to) | 212, 321, 327; 4233 | Mining: 2,523.9M t at avg **48 mi**, customer pick-up 21.3%. Gravel is the largest commodity by tons (1,910.9M t). Mineral products: own truck 41.7%. Lumber and construction-materials wholesalers: own trucks carry 64.6% of value | 3,523 mining, 11,761 wood and 8,807 mineral-products firms | Short, heavy loads; the receiver is often a contractor |
| G08 | Metal, machinery and equipment makers | 331-335 | Machinery: for-hire 79.0% of tons. Fabricated metal: for-hire 62.6% | 49,484 fabricated-metal firms (firms under 500 earn 53.5% of receipts); 19,028 machinery firms | Flatbed, LTL, oversize loads |
| G09 | Vehicle makers, parts wholesalers, and vehicle dealers | 336; 4231 | Vehicle makers: for-hire 53.8%, truck-rail 16.5%, customer pick-up 12.1% | 9,145 vehicle-maker firms; firms under 500 employees earn only 10% of receipts | Car hauling for dealers and auctions sits here |
| G10 | Industrial and durable-goods distributors | 423 (other than 4231, 4233) | Durable wholesale overall: own truck 43.1% of tons, for-hire 29.6%; parcel 23.0% of value | 153,128 firms; 83.2% under 20 employees | A mix of LTL, parcel and own fleet |
| G11 | E-commerce and mail-order sellers | 4541 | 52.2M t, $1,007.9B. **Parcel 47.7% of tons, 65.3% of value** | 53,556 firms; 93.2% under 20 employees; 440 firms with 500+ employees earn 76% of receipts | Parcel-centred |
| G12 | Furniture and home-goods makers and sellers | 337; 4232 | Furniture makers: for-hire 59.9%, own truck 24.4% | 14,044 furniture makers; 81.3% under 20 employees | Big-and-bulky deliveries to homes |
| G13 | Importers | All industries | FAF 2024 imports: 1,096.9M t; 55.9% of tons arrive by water, 26.8% of value by air; the US leg is 42.0% truck | 240,535 importers (2024); 97.3% small or mid-sized; 38.5% have 1-19 employees | Customs entries, drayage, container charges |
| G14 | Exporters, especially of farm and food products | All; SCTG 01-07 | Farm and food exports 214.8M t (FAF 2024); leg to the port: truck 45.4%, rail 35.8%, water 14.6% | 271,250 exporters; 97.1% small or mid-sized; 60% export to only one country | Export documents |
| G15 | Suppliers to big-box retailers | Cross-industry | The retailer sets the rules: "collect" (the retailer arranges the truck) or "prepaid" (the supplier does) | n/a | Walmart fines 3% of cost of goods on late or short cases; goals of 90% on time (prepaid), 98% ready for pick-up (collect), 95% in full (N-E24 to N-E26) |
| G16 | Warehouses and distribution centres, as receivers and shippers | 4931 | As origins: 305.7M t, $1,347.7B; for-hire 46.0%, own truck 43.2% | 9,195 firms with 19,979 sites; 51% of sites belong to firms with 500+ employees | Dock appointments; storage and handling bills |
| G17 | Drug and medical makers and distributors | 3254; 4242 | Drug wholesalers: 43.3M t but $1,087.1B; for-hire carries 77.5% of value; $201.7B of temperature-controlled value | Not extracted | Cold chain |
| G18 | Households moving their belongings | Not in the CFS | Movers | n/a | Fringe |
| G19 | Scrap and recycling yards | 423930; SCTG 41 | Waste and scrap: 178.1M t, for-hire 54.4% of tons | Not extracted | Fringe |

Two handling types cut across groups: temperature-controlled freight (10.2% of CFS tons; 47.7% of it in shippers' own trucks) and hazmat (21.3% of tons) (N-E06, N-E07). They show up inside cards rather than as columns.

**What the data cannot tell us yet:**
- Shippers' technology habits by size. The only size-specific figure is a Gartner estimate relayed by a logistics-provider blog: "Under $25 Million [freight spend]: Roughly 10%" use a TMS, against 50% above $100M (N-E20, *assumed*). A vendor survey of 616 shippers and providers found "only 17% ... fully automated" (N-F28, vendor). A freight-audit CEO says "about seven out of 10 shippers use a TMS" (N-F29, *assumed*). These conflict, so S3 treats technology habits as unknown per candidate.
- How much freight the receiver arranges. Customer pick-up (11.4% of tons) is the only official measure. No economy-wide figure for "collect" freight was found (N-E31, *assumed*).

### 1.2 What: shipping jobs, in the shipper's words

The seven starter jobs come from `submarket_selection.md` §4 S1 **[our call there]**. One job is added here, J8, because both the managed-transportation definition (R33: "transportation planning, carrier selection, tendering, and routing") and the private-fleet evidence (N-F19, N-F20) show a planning job that none of J1-J7 covers **[our call]**. The "words" columns are desk paraphrases, built from job postings and O*NET task lists (N-F23 to N-F26, N-F59 to N-F63). They are *assumed* until S5 hears the real words (R18).

| ID | Job | In the shipper's words | In the freight company's words | Who does it today at small firms (N-F table) |
|---|---|---|---|---|
| J1 | Buy capacity and rates | "Get a truck at a fair price"; "lock in next year's lanes" | "Find paying loads for my trucks" | Shipper logistics coordinator by phone and email; carrier owner or dispatcher on load boards; broker sales reps |
| J2 | Tender, book and schedule | "Book the pickup"; "get a dock appointment" | "Get the load assigned and the appointment set" | Shipping clerk; warehouse dock scheduler; carrier dispatcher |
| J3 | Track and report status | "Where is my load and when will it arrive?" | "Answer the check calls" | Coordinator chasing email; broker track-and-trace reps, "up to 100 [calls] per day" (N-F60) |
| J4 | Handle documents and compliance | "Get the paperwork right so nothing is held or fined" | "Get the signed bill of lading so I can bill"; "keep permits and filings current" | Shipping clerk (bill of lading); customs entry writer; carrier safety or permit clerk |
| J5 | Audit, pay and reconcile freight bills | "Pay only what we owe" | "Get paid in full, and fast" | Shipper AP clerk; carrier billing clerk; factoring company |
| J6 | Manage detention, demurrage and extra charges | "Stop paying for waiting and surprise fees" | "Get paid for the hours we waited" | Carrier dispatcher and billing clerk; importer's coordinator; supplier's deductions analyst |
| J7 | Claims and disputes | "Get paid back for goods that arrive damaged or short" | "Settle the claim without losing the customer" | Receiving clerk records the damage; shipper claims coordinator; carrier claims desk |
| J8 | Plan and consolidate shipments *(added)* | "Choose the mode, combine small shipments, plan the routes" | "Build loads and routes that fill the truck" | Traffic manager or in-house dispatcher with spreadsheets; managed-transportation 3PL |

### 1.3 How: freight-company types and methods (the rows of the grid)

Built from Armstrong & Associates' 3PL segments (R33), the asset carriers by NAICS code (R44, N-F01), FMCSA's registries (N-F02, N-F03), the FMC and CBP (N-F05 to N-F11), and the in-house methods (N-F19, N-F20, N-F28). One row is added **[our call]**: H17, the service firms that do one job for a fee (audit, factoring, dispatch, claims, permits). Several cards are "handled today" by them.

| ID | Type or method | Codes | Count (year, source) | Size mix | How it is paid |
|---|---|---|---|---|---|
| H01 | Freight brokers (arrange trucks without owning them) | FMCSA broker authority; NAICS 488510 (shared with forwarders) | 25,081 active broker authorities (May 2026, N-F03); 17,130 firms in 488510 (2022, R44) | 87% of 488510 firms have under 20 employees and earn 24% of receipts | The spread between the shipper's price and the carrier's pay; net about 15% of gross (N-F17, **[our calc]**) |
| H02 | Intermodal: containers by rail with trucks at each end (intermodal marketing companies) | 488510 | 18.5M containers and trailers moved in 2025 (IANA, N-F14); IMC count not found | Not found | Margin |
| H03 | Managed-transportation 3PLs (run a shipper's transport as an outsourced department) | Armstrong DTM sub-segment | Size not public (R33) | Not found | "a flat amount per shipment or a percent of the purchased transportation ... gainshares" (R33) |
| H04 | Final-mile carriers (last leg to a home or business) | 492210; 4921 | 4,827 local-delivery firms (N-F01) | 67% under 20 employees, earning 12% | Per stop or package |
| H05 | International forwarders, NVOCCs and customs brokers | FMC OTI licence; CBP licence; 488510 | Over 9,100 ocean intermediaries, about 8,600 of them NVOCCs (FY2024, N-F05); about 14,500 licensed customs brokers (N-F09, *assumed*); 1,887 FMCSA freight-forwarder dockets (N-F03) | Not found | Markup on ocean space; per-entry and service fees |
| H06 | Warehouses: public and contract | 493110, 493120, 493130 | 6,789 general, 680 refrigerated and 542 farm-product warehouse firms (N-F01) | General: 53% under 20 employees, earning 9% | Storage per pallet per month plus handling (N-F64, *assumed*) |
| H07 | Dedicated contract carriage (trucks and drivers dedicated to one shipper) | Armstrong DCC | $32.0B gross (2025, R33) | Not found | Contract |
| H08 | Truckload carriers | 484121 | 53,705 firms (R44); 531,374 active interstate for-hire carriers of all kinds, 56.6% with one truck (N-F02, **[our calc]**) | 94% under 20 employees, earning 24% | Per load or mile, plus fuel and extra-service charges |
| H09 | LTL carriers (shared trailers through terminals) | 484122 | 7,675 firms; top-50 share 82.9% (R44) | 78 firms in 500+ enterprises earn 82% | By freight class, weight and lane, plus extra-service charges |
| H10 | Local trucking, including port drayage | 484110 | 43,243 firms (R44); 48,991 carriers tick "intermodal containers" (N-F02); 23,000+ trucks in the LA/Long Beach drayage registry (N-F21) | 93% under 20 employees, earning 52% | Per load, hour or day, plus chassis and waiting charges |
| H11 | Specialized trucking: reefer, flatbed, tank, dump, livestock, logging, auto, heavy haul | 484220, 484230 | 42,628 firms (R44). Carriers ticking each cargo type (N-F02): reefer 105,756; flatbed cargo 136,759; tank/liquids 31,590; dry bulk 77,488; livestock 25,365; logs 81,349; motor vehicles 76,367; machinery and large objects 87,293 | Local specialized: 92% under 20 employees, earning 34% | As truckload; heavy haul also pays for permits and escorts |
| H12 | Household-goods movers | 484210 | 9,083 firms (N-F01); 8,207 active household-goods authorities (N-F03) | 85% under 20 employees, earning 26% | Weight or volume and distance |
| H13 | Rail, barge and air freight | 482; 483211; 481112 | 6 Class I railroads and about 603 short lines serving about 10,000 customers (N-F12, N-F13); 339 barge firms; 211 air-freight firms (N-F01) | Class I railroads earn 89% of rail revenue | Tariff or contract rate, plus demurrage |
| H14 | Parcel and courier carriers | 4921 | 6,553 firms; top-50 share 90.9% (R44) | Concentrated | Per package plus surcharges |
| H15 | In-house fleet (the shipper's own trucks) | FMCSA "private property" | 170,221 private-only interstate fleets, 86.4% with 10 or fewer trucks, about a quarter of interstate trucks (N-F02, **[our calc]**) | Mostly small | A cost centre for 77% of fleets surveyed (N-F20) |
| H16 | Spreadsheet and phone (the shipper or carrier does it by hand) | — | "over one-third heavily or mostly reliant on manual processes" (N-F28, vendor survey of 616 firms) | — | Staff time |
| H17 | Job-specific service firms *(added)* | None | Freight audit and payment: "a few primary competitors and numerous small ... audit firms" (N-D30); a Gartner guide names about 15 (N-F50, *assumed*). No counts found for factoring, dispatch, claims, permit or filing services (N-F) | — | Audit: per invoice or 25-50% of what is recovered. Factoring: 1-5% per invoice. Dispatch: 5-10% of gross. Permits: $50.50-150 each on top of state fees (N-F39, N-F40, N-F42, vendor claims) |

**Two FMCSA counts that look different.**
- Scan F counted **interstate** carriers: 531,374 active for-hire, 91.9% of those reporting trucks with 10 or fewer (N-F02).
- Scan G counted **all operations**, including carriers that stay inside one state: 1,383,613 active for-hire, 92.6% with 5 or fewer trucks (N-G49).
- Both are queries of the same file on the same day. They differ only in the filter.
- The cargo-type counts on the fringe cards use scan G's wider filter and self-reported cargo boxes, so treat them as upper bounds.
- Two pairs of boxes return identical counts ("meat" and "refrigerated food"; "construction" and "building materials"), which looks like a data-mapping fault in the file (N-F02, N-G49).

---

## 2. The grid (S1 step 2)

The grid follows R02's product/market layout: freight-company types are the rows and shipper groups the columns. Each cell is a possible candidate.

**Cell key:**
- **Numbers** are the cards drawn from that cell, with the "C-" dropped: 21 = C-21.
- **X** means the cell's freight is pooled in column X.
- **●** means a large flow that has no card of its own; see "Gaps" below.
- **R-n** is a reserve niche (§5.3).
- A **blank** cell means little or none of the group's freight moves that way in the CFS/FAF data, or no source links the two.

**Column X is "general freight".** It holds the ordinary truckload and LTL freight of mid-sized manufacturers and distributors (G01, G06, G08, G10, G12), whose jobs are the same whatever they make. Cards in column X apply to all of them. Their industry is a segment variable for Q6, not a separate sub-market (see M-1 in §5.2).

**How the cells were placed.**
- Asset rows (H08-H15) come from each group's CFS/FAF mode shares, mapped to the nearest row **[our call]**.
- Intermediary rows (H01-H07, H16, H17) cannot be read from the CFS, which does not say whether a hired truck was booked through a broker. They are placed from the sources on each card (*assumed*).

| How ↓ / Who → | X | G01 | G02 | G03 | G04 | G05 | G06 | G07 | G08 | G09 | G10 | G11 | G12 | G13 | G14 | G15 | G16 | G17 | G18 | G19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **H01** Brokers | 01 02 06 07 08 | X | | 26 | | | X | | X | 39 | X | | X | 25 | | 19 | | | | |
| **H02** Intermodal | 14 | X | | | | | X | | | | X | | | | | | | | | |
| **H03** Managed transportation | 14 | X | | | | | X | | X | | X | | | | | | | | | |
| **H04** Final mile | | | | | | | | | | | | ● | 13 | | | | | | | |
| **H05** Forwarders, NVOCCs, customs brokers | | | | 27 | | | | | | | | | | 20 21 23 25 33 | 24 | | | | | |
| **H06** Warehouses | | | 04 | 27 | | | | | | | 18 | 18 | | | | | 04 18 | | | |
| **H07** Dedicated contract carriage | | | 15 | | | | | | | | 15 | | | | | | | | | |
| **H08** Truckload | 01 02 03 05 06 | X | | | | | X | | X | | X | | X | | | 19 | 03 | | | |
| **H09** LTL | 11 | X | | | | | X | | X | | X | | X | | | | | | | |
| **H10** Local and drayage | | | | 27 | | | | 36 | | | | | | 21 22 25 | | | | | | R-1 |
| **H11** Specialized (reefer, flatbed, tank, dump, livestock, logs, auto) | | ● | | 26 | 28 | 31 32 | 35 | 36 37 | 34 | 39 | | | | | | | | R-5 | | |
| **H12** Household-goods movers | | | | | | | | | | | | | | | | | | | 40 | |
| **H13** Rail, barge, air | | | | | 29 | | 30 | 30 | | | | | | 33 | 29 | | | | | R-1 |
| **H14** Parcel and courier | | | | | | | | | | | | 12 | | | | | | R-5 | | |
| **H15** In-house fleet | | | 15 | | 28 | 15 | 38 | 16 | | | 15 | | | | | | | 15 | | |
| **H16** Spreadsheet and phone | 09 10 17 | | | | | | | | | | | | | | | 19 | | | | |
| **H17** Job-specific service firms | 05 06 09 10 | | | | | | | | 34 | | | 12 | | | | | | | | |

**Gaps (● cells): large flows with no card of their own, and why.**
- **G01 × H11, reefer freight of food and beverage makers.** 21% of all temperature-controlled tons start here (N-E06). Its jobs (buying capacity, detention, freight audit) are the same as C-01, C-03 and C-09, and only the equipment differs. Reefer is therefore a segment variable inside those cards. Produce reefer (C-26) is separate, because its rejection and PACA system is different (M-2).
- **G11 × H04, final-mile parcel to homes for e-commerce sellers.** The parcel jobs sit in C-12. Final-mile delivery of small parcels is run by concentrated carriers (couriers' top-50 share is 90.9%, R44), and no separate small-seller job was found in the scans. Big-and-bulky final mile is C-13.

**Reading the grid for "unserved markets"** (R02: empty cells "show gaps"). Freight does not move in most empty cells here (barge × e-commerce, for example), so they are not opportunities. The useful reading is different: cells where freight and charges clearly move, but the scans named **no specialized software**. These are possible unserved markets. They are *assumed*, because absence in a desk scan is not proof, and S3 item 9 checks them:
- rail demurrage invoices for carload shippers (C-30): Class I railroads collected $1.18B in demurrage in the first nine months of 2021 (N-F34). Scan F found no software, and scan G found one service firm (N-G34);
- tank-wash certificates and hazmat papers for bulk shippers (C-35): no specialized software firm identified (N-G58);
- cut-flower import clearance in Miami (C-33): no specialized firm identified (N-G68);
- inbound freight control for receivers (C-17) and job-site delivery for building-material dealers (C-16): software not researched in S1.

**Coverage of the axes.**
- Every **How** row has at least one card, except that the dedicated-carriage row (H07) sits inside C-15 (M-3).
- Every **Who** column has at least one card, or pools into X, except G19 (scrap), which is reserve R-1.
- Every **job** J1-J8 appears on at least two cards (table in §6).

---

## 3. Candidates from outside the grid (S1 step 3)

### 3.1 Five shipment chains, walked one hand-off at a time

Each chain lists the hand-offs in order and marks where **paper**, **payments** or **waiting** charges pile up (R26's method). The full step-by-step tables, with the documents, payments and charges at each step, are in `research/s1_scan_G_outside_grid.md` §2.

**A. An import container from Asia to a mid-sized importer's warehouse.**
The hand-offs:
1. Purchase order to the supplier.
2. Booking with a forwarder or NVOCC.
3. Security filing to CBP, due at least 24 hours before loading abroad (ISF).
4. Ocean bill of lading.
5. Arrival notice, then the customs entry (Form 7501) filed by a customs broker.
6. Release. It needs four things at once, each tracked in a different party's system: freight paid, bill of lading surrendered, customs cleared, no terminal holds.
7. Terminal appointment and chassis.
8. Drayage truck to the warehouse.
9. Empty container returned.
10. The demurrage and detention invoice.

Where it piles up:
- **Waiting charges at and after the terminal.**
  - Nine ocean carriers billed about $8.9B in demurrage and detention in 2020-22 and collected $6.9B, so about 22% went uncollected (N-G01, *verified*; **[our calc]**).
  - Average charges after 14 days in 2023 ran from $1,919 (Houston) to $2,478 (New York) per container (N-G05, a vendor's own benchmark).
  - Since 2024-05-28, an FMC rule sets what these invoices must contain and gives 30-day windows to issue and to dispute them. "Failure to include the minimum information ... eliminates the Billed Party's obligation to pay" (N-G02, N-G03).
- **Customs paperwork.** The same invoice and packing-list data is keyed twice, for the security filing and for the entry. Fines are fixed per violation: $5,000 for a security-filing violation (N-G07, *assumed*). CBP processed more than 2.9M entry summaries in September 2024 alone (N-G09, *verified*).
- **Drayage extras.** Chassis-split, pre-pull, storage and dry-run lines. No frequency data was found.

Cards drawn: C-20, C-21, C-22, C-23.

**B. Fresh produce from a packing shed to a grocery warehouse, plus the Mexico border variant.**
The hand-offs:
1. Sale confirmed.
2. Load tendered to a broker, then to a reefer carrier, with a temperature setpoint.
3. Loading, with pulp temperatures recorded.
4. Delivery, with a lumper unload and the receiver's quality check.
5. If the receiver **rejects** the load: USDA inspection, then salvage or a claim.
6. Pallet exchange.
7. Invoices.

Where it piles up:
- **Two dispute systems for one load.** PACA settles trading disputes, but it "does not give the USDA jurisdiction over transportation companies". A temperature claim runs under the trucking liability law instead (N-G12, *verified*).
- **Scale of the dispute system.** USDA handled more than 2,340 PACA cases worth $126.3M over three years (N-G16, *assumed*: snippet of a blocked page).
- **Payment deadlines.** PACA's default is payment within 10 days of acceptance. Longer terms must be in writing and no more than 30 days, or the seller loses its trust rights (N-G13, *assumed*).
- **Inspection fees.** Imported produce is inspected at $0.00635/lb (N-G14, *verified*).

The border variant adds more hand-offs: a Mexican customs broker, a "transfer" truck that pulls the trailer across, a US customs broker, a cold dock and inspection, then a US reefer (N-G18, vendor). In Q1 2026, 45% of produce moved by truck came from Mexico (R34).

Cards drawn: C-26, C-27.

**C. An LTL shipment from a small manufacturer to a distributor.**
The hand-offs:
1. Class lookup.
2. Bill of lading.
3. The origin terminal's measuring machine and scale.
4. Linehaul.
5. Delivery, with any extra services.
6. Invoice, then a **corrected invoice**.
7. Dispute or claim.

Where it piles up:
- **Corrections after delivery.** Reweigh and reclass fees add 10-20% to base rates and arrive 2-6 weeks after delivery (N-G23, vendor).
- **Extra-service charges** are "20 to 30 percent of total LTL spend" (N-G24, vendor).
- **The 2025 class change.** Freight class moved to a 13-tier density scale on 2025-07-19, so any system holding old classes misprices until it is updated (N-G20, N-G21, *verified*).
- **No neutral data on how often LTL invoices are corrected.** Vendor claims run from 3% to 15%.

Cards drawn: C-11 (and C-09 for the audit afterwards).

**D. Grain from the field to an export ship.**
The hand-offs:
1. Combine, grain cart, then a farm truck.
2. Country elevator: scale ticket and grade.
3. Settlement against the farmer's contract.
4. Railcar rights or a barge.
5. Export elevator, with official inspection and weight certificates.
6. Final settlement.

Where it piles up:
- **Scale tickets to contracts.** Every truckload's ticket must be matched to the right contract, with drying and storage charges, before the farmer is paid (N-G30, *assumed*). No farm-software API existed in 2017 (R30).
- **Transport price swings.**
  - St. Louis barge freight was 792% of its benchmark tariff on 2026-09-08, against a 2025 average of 435%, so about $31.61 against $17.37 a ton (N-G25, *verified*; **[our calc]**).
  - Bids for BNSF grain-train rights moved from +$563 to −$100 per car within eight months (N-G27, N-G28, *assumed*).
- **The harvest queue** at the elevator (R30).

Cards drawn: C-28, C-29, C-24.

**E. A brokered truckload from a supplier to a big-box retailer.**
The hand-offs:
1. Purchase order and the retailer's routing guide.
2. Tender to the broker.
3. Rate confirmation to the carrier.
4. Appointment in the retailer's portal.
5. Pickup.
6. Check calls.
7. Unload, with a lumper, possible detention, and proof of delivery.
8. Invoice.
9. Factoring or quick pay.
10. **OTIF fines and deductions**.

Where it piles up:
- **Detention.** Drivers were detained at 39.3% of stops in 2023, costing $3.6B directly (N-C24). The usual terms are 2 free hours, then $50-100 an hour (N-G38, vendor).
- **Lumpers** cost $100-500 a load (N-G37, vendor).
- **Broker phone work.** Small and mid-sized brokers "can make and receive hundreds, if not thousands, of calls per day" (N-G44).
- **Deductions.**
  - Walmart fines 3% of the cost of goods on late or short cases (N-G35, vendor sources).
  - Vendors say deductions take 5-7% of supplier revenue, 10-20% of them are invalid, and only 20-30% are disputed (N-G36, vendor claims).

Cards drawn: C-03, C-04, C-05, C-07, C-08, C-19.

### 3.2 Investors' pain categories

The baseline is Bessemer's 2021 map (R28). The scans found no free 2023-26 map as complete as R28. The newer categories come from theses and analyst summaries (N-G40 to N-G47).

| Pain category | Source and date | New since 2021? | Card(s) |
|---|---|---|---|
| "procurement" | R28, 2021; R22 names "freight procurement for a shipper" | — | C-01 |
| "first mile" | R28 | — | C-28 (field to elevator), C-04 |
| "drayage" | R28 | — | C-22 |
| "customs clearance" | R28 | — | C-20, C-27 |
| "last mile" | R28 | — | C-13 |
| "data entry and invoice processing" | R28 | — | C-05, C-09, C-18 |
| Manual booking | R28 ("Booking freight is still a highly manual process") | — | C-04, C-07 |
| AI agents for brokers' "phone calls, emails, and paperwork" | a16z/HappyRobot, 2024 (N-G44); Gartner, 2025 (N-G42); FreightTech 100, 2025 (N-G40) | **Yes** | C-07, C-02 |
| Fraud, double brokering, carrier identity | FTV Capital on Highway, 2025 (N-G43) | **Yes** | C-08 |
| Cross-border Mexico, tariffs and trade | FreightTech 100 2026 (N-G40); PitchBook Q2 2025 (N-G47) | **Yes** | C-25, C-20 |
| Visibility | Gartner 2025 calls it mature ("Slope of Enlightenment", N-G42) | No | C-02 |

No investor source names dock or appointment scheduling as a category. It appears only on vendor pages (scan G §3). C-04 comes from the grid and the chain walk instead.

### 3.3 Fringe niches, added on purpose

R15: good beachheads often "exist on the fringe". Scan G checked 21 niches (table in its §4). Each one went into a card, was merged into one, or was held in reserve because the 40-card cap **[our call]** was reached:

| Niche | Outcome |
|---|---|
| Livestock hauling | C-31 |
| Farm-to-plant milk pickup | C-32 |
| Harvest grain hauling | C-28 (also a grid cell) |
| Oversize/overweight permits | C-34 |
| Tank and hazmat hauling | C-35 |
| Aggregates and dump trucking | C-36 |
| Log hauling | C-37 |
| Fuel delivery | C-38 |
| Vehicle transport | C-39 |
| Household moves | C-40 |
| Cut flowers into Miami | C-33 |
| Rail carload shippers | C-30 (also a grid cell) |
| Cross-border Mexico via Laredo | C-25 |
| Big-and-bulky final mile | C-13 (also a grid cell) |
| Inland barge shippers | Merged into C-29 (M-5) |
| Expedited and hot-shot | Merged into C-06 (M-4) |
| Scrap and recycling | Reserve R-1 |
| Trade-show freight | Reserve R-2 |
| Fine-art shipping | Reserve R-3 |
| Returns / reverse logistics | Reserve R-4 |
| Pharma cold chain | Reserve R-5 |

---

## 4. The cards (S1 step 4)

Each card follows the template in `submarket_selection.md` §13, with the fields in its order:
- the sentence;
- Who: the shipper group, with codes, size, region and technology habits where known;
- What: the job, in their words;
- How: the method or freight-company type used today;
- the four roles: whose cost falls, who decides, who pays, and which side is harder to win;
- the human end user on each side;
- the five sub-market signs from R02: products, customers, competitors, price, channels;
- the source of the idea.

**Reading the fields:**
- "Harder side" is a desk guess, labelled *assumed*. S5 tests it.
- It is not the entry side, which is chosen at segment selection (Q6; F-5).
- "Pays" means whose budget the job sits in today. It says nothing about our fee, which is deferred (F-7, F-8).
- In the sign line: ✓ = the scans found evidence that this sign sets the card apart; ? = not found yet.

### 4.1 Truckload and brokerage: general freight (C-01 to C-10)

#### C-01 · Buying truckload capacity, for mid-sized shippers
- **Sentence:** "Buying truckload capacity and rates, for mid-sized manufacturers and distributors, handled today by freight brokers and truckload carriers over phone, email and spreadsheets."
- **Who (column X: G01, G06, G08, G10, G12):**
  - Manufacturers and wholesalers with 20-499 employees: 57,309 manufacturing firms and 38,270 wholesale firms (N-E17, **[our calc]**).
  - Hired trucks carry 35.2% of manufacturing tons and 53.7% of its value (N-E02).
  - Nationwide.
  - Technology: about 10% use a TMS below $25M of freight spend (N-E20, *assumed*).
- **What (J1):** "Get a truck at a fair price for this load, and lock in next year's lanes" (*assumed* paraphrase).
- **How:**
  - H01 brokers: 25,081 active authorities (N-F03).
  - H08 truckload carriers: 53,705 firms in 484121 (R44).
  - In a 2018 survey of 533 carriers, 63% of loads came directly from shippers and 23% through brokers (N-E22).
- **Roles:** cost falls on the shipper (freight spend, staff time) | decides: the shipper's logistics or purchasing manager | pays: the shipper | harder side: shipper side (*assumed*: "freight is a relationship-driven business", R27).
- **End users:**
  - Shipper: logistics coordinator or traffic manager (logisticians, SOC 13-1081: 251,040 in all industries, N-F22).
  - Freight-company side: broker carrier-sales rep (43-5011) or carrier dispatcher (43-5032).
- **Sub-market signs:**
  - products ✓ quote and bid tools;
  - customers ✓ mid-sized shippers without a TMS;
  - competitors ✓ freight-procurement vendors such as Transporeon, Keelvar, Emerge and GoodShip (N-F46, *assumed*);
  - price ✓ broker spread, about 15% of gross (N-F17, **[our calc]**);
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H01/H08 × X; R22 ("freight procurement for a shipper").

#### C-02 · Load status, for mid-sized shippers and receivers
- **Sentence:** "Knowing where each load is and when it will arrive, for mid-sized shippers and receivers, handled today by brokers' and carriers' check calls, emails and portals."
- **Who (X, G16):**
  - The shippers in C-01, plus the warehouses that receive their freight (19,979 warehouse sites, N-E17).
  - Shippers "currently lack visibility across the brokers and carriers they work with" (R27).
- **What (J3):** "Where is my load, and when will it get here?"
- **How:**
  - H01 brokers' track-and-trace reps, making "up to 100 [calls] per day" (N-F60, job posting).
  - H08 carrier dispatchers.
  - Drivers' app or electronic-logbook location links (N-F, *assumed*).
- **Roles:** cost falls on brokers and carriers (staff time) and on shippers (surprises, idle docks) | decides: the shipper's logistics or customer-service lead, or the broker's operations manager | pays: the shipper, inside the broker's margin (N-F, *assumed*) | harder side: freight-company side (*assumed*: small carriers must share location).
- **End users:**
  - Shipper: customer-service rep or logistics coordinator.
  - Freight-company side: broker track-and-trace rep (43-5011). 53,390 cargo and freight agents work at brokers and forwarders (N-F22).
- **Sub-market signs:**
  - products ✓ live location and arrival estimates;
  - customers ✓ shippers without visibility software;
  - competitors ✓ visibility platforms: project44, Shippeo, FourKites, MacroPoint, Trucker Tools (N-F48, N-F49, N-F70, *assumed*);
  - price ? bundled into the broker's margin;
  - channels ?
  - **3 of 5**.
- **Source of the idea:** grid H01/H08 × X; investor maps (AI agents for check calls, N-G44).

#### C-03 · Detention and extra charges at the dock
- **Sentence:** "Getting detention and other extra-service charges recorded, billed and paid, for shippers and receivers whose docks hold trucks, handled today by small truckload carriers' dispatchers and billing clerks with paper logs, phone and email."
- **Who (X, G15, G16):** manufacturers, distributors and distribution centres that load and unload trucks. Drivers were detained at 39.3% of stops in 2023 (N-C24).
- **What (J6):**
  - Shipper: "stop paying surprise fees."
  - Carrier: "get paid for the hours we waited."
- **How:**
  - H08/H11 small carriers: 531,374 active interstate for-hire carriers, 56.6% of them with one truck (N-F02, **[our calc]**).
  - Tools today:
    - TMS features (Trimble TMW, McLeod);
    - telematics (Samsara);
    - one standalone tool (ChargeGuard, $59-349 a month) (N-D34, N-D35).
  - Vendor claim: manual processes capture "only around 40%" of the detention owed (N-D34).
- **Roles:** cost falls on drivers and carriers: $1.1-1.3B a year of lost driver earnings, and $250.6-302.9M a year of carrier net income (2018, N-F30) | decides: the carrier owner, on whether to bill; the facility, on how long loading takes | pays: the broker or shipper, when the charge is captured | harder side: shipper/receiver side (*assumed*: it causes the wait and pays the bill).
- **End users:**
  - Carrier: dispatcher and billing clerk (43-5032, 43-3031).
  - Shipper/receiver: dock and receiving staff (43-5071).
- **Sub-market signs:**
  - products ✓ time-stamped arrival and departure proof;
  - customers ✓ small truckload and reefer carriers;
  - competitors ✓ TMS and telematics features, plus one standalone tool;
  - price ✓ hourly after 2 free hours, typically $50-100 an hour (N-G38, vendor);
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H08 × X; chain E (step E6); R38 (drivers' #5 issue).

#### C-04 · Dock appointments, for warehouses and distribution centres
- **Sentence:** "Booking dock appointments for inbound and outbound trucks, for warehouses, distribution centres and grocery distributors, handled today by phone, email, spreadsheets and appointment portals."
- **Who (G16, G02):** 19,979 warehouse sites (15,416 general, 1,222 refrigerated) and 34,852 grocery-distributor sites (N-E17).
- **What (J2):** "Give every truck a time and a door, so the dock doesn't jam."
- **How:**
  - H06 warehouse staff.
  - Dock-scheduling vendors: Opendock, C3 Reservations, DataDocks, GoRamp, LoadingCalendar, Velostics, Conduit, Transporeon (N-F38, N-F47, vendor lists).
- **Roles:** cost falls on carriers (waiting) and the warehouse (congestion, overtime) | decides: warehouse or DC manager | pays: the warehouse, priced per facility from $99 a month to about $7,000 a year (N-F38, vendor claims) | harder side: freight-company side (*assumed*: every carrier and broker must use the booking link).
- **End users:**
  - Warehouse: dock scheduler (within 43-5071/43-5061; job postings at $18-26 an hour, N-F62).
  - Freight-company side: carrier dispatcher or broker operations rep.
- **Sub-market signs:**
  - products ✓ appointment calendars and booking links;
  - customers ✓ receiving sites;
  - competitors ✓ dock-scheduling vendors;
  - price ✓ per facility;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H06 × G16, G02; chain E (step E3). The process doc lists "book dock appointments" as an example job (§2.2).

#### C-05 · Getting small carriers paid
- **Sentence:** "Invoicing, approving and paying small carriers' freight bills, for the shippers and brokers who give them loads, handled today by carriers' billing clerks on paper and by factoring companies."
- **Who (X):**
  - The payers: brokers (25,081 authorities) and shippers.
  - The carriers: 446,405 of the 485,543 carriers that report trucks run 10 or fewer (N-F02, **[our calc]**).
- **What (J5):**
  - Payer: "pay the right carrier the right amount once proof of delivery is in."
  - Carrier: "get paid in full, and fast."
- **How:**
  - H17 factoring companies charge "1% to 4% per invoice", plus a reserve held back (N-F40, vendor).
  - Payment networks such as TriumphPay (N-F44).
  - Carrier billing clerks with bookkeeping tools (N-F63).
  - Cass says small carriers "were larger users of our quick pay solutions" (N-C15).
- **Roles:** cost falls on the carrier (the discount and the days waiting) | decides: carrier owner | pays: the carrier pays the factor; the broker or shipper pays the invoice | harder side: payer side (*assumed*: brokers and shippers set the terms and the portal).
- **End users:**
  - Carrier: billing or settlements clerk, often the owner-operator.
  - Payer: broker's carrier-payables clerk (43-3031).
- **Sub-market signs:**
  - products ✓ document capture plus payment;
  - customers ✓ carriers with 1-10 trucks;
  - competitors ✓ factors and payment networks;
  - price ✓ a % of each invoice;
  - channels ✓ load boards and factoring networks (*assumed*).
  - **5 of 5**.
- **Source of the idea:** grid H17/H08 × X; chain E (step E7); R27 and R29 (a finance layer; factoring).

#### C-06 · Matching spot loads with small carriers
- **Sentence:** "Finding and booking spot truckloads, for brokers and shippers who need a load covered, handled today by owner-operators working load boards and independent dispatch services."
- **Who (X):** brokers and shippers posting spot freight. DAT alone reports "more than 291 million loads & trucks posted annually" (N-F41, vendor).
- **What (J1):**
  - Broker: "cover this load today with a truck I trust."
  - Carrier: "find a load that pays for the trip."
- **How:**
  - H08/H11 owner-operators: 274,660 one-truck interstate carriers (N-F02).
  - Load boards: DAT carrier plans cost $59-339 a month (N-F41).
  - H17 dispatch services charge "5% to 10%" of gross revenue (N-F39, vendor).
  - Includes expedited and hot-shot carriers (M-4).
- **Roles:** cost falls on carriers (empty miles, dispatch fees) | decides: owner-operator | pays: carrier | harder side: broker/shipper side (*assumed*: they control the freight).
- **End users:**
  - Carrier: owner-operator or dispatcher (34,890 dispatchers work in trucking, N-F22).
  - Broker: carrier-sales rep.
- **Sub-market signs:**
  - products ✓ load matching;
  - customers ✓ owner-operators;
  - competitors ✓ load boards and dispatch services;
  - price ✓ a % of gross;
  - channels ✓ load boards (*assumed*).
  - **5 of 5**.
- **Source of the idea:** grid H17/H08 × X; R38 (owner-operators rank "Broker Issues" first); fringe (hot-shot).

#### C-07 · A small brokerage's load back office
- **Sentence:** "Quoting, booking, tracking, documenting and paying each truckload, for shippers who use small freight brokers, handled today by small brokerages on broker TMSs, phone and email."
- **Who (X):** small and mid-sized shippers that buy through small brokers. 87% of freight-arrangement firms have under 20 employees (N-F01).
- **What (J2, J3, J5):**
  - Shipper: "move my load without chasing anyone."
  - Broker: "get from quote to carrier payment without re-keying."
- **How:**
  - H01 small brokerages.
  - Systems used by micro-cap brokers (check D, N-B04):
    - McLeod, about 16%;
    - homegrown systems, about 13%;
    - ITS Dispatch, about 9%;
    - Ascend, about 6%;
    - Aljex, about 4%;
    - 20 named in all.
  - Entrants:
    - venture-funded TMSs: MVMNT, Rose Rocket, Alvys (N-B26 to N-B28);
    - AI agents for calls and email: HappyRobot (N-G44).
- **Roles:** cost falls on the brokerage (staff time per load) | decides: brokerage owner | pays: brokerage | harder side: broker side (*assumed*: switching systems moves every customer and carrier).
- **End users:**
  - Broker: carrier-sales, customer-sales and track-and-trace reps (43-5011).
  - Shipper: logistics coordinator.
- **Sub-market signs:**
  - products ✓ broker TMS and back-office tools;
  - customers ✓ small brokerages;
  - competitors ✓ broker TMSs;
  - price ✓ per seat; MVMNT gives a free core and earns from finance;
  - channels ✓ broker associations (*assumed*).
  - **5 of 5**.
- **Source of the idea:** grid H01 × X; R27; investor maps (N-G44). Aljex sold for $32.4M with about 400 broker customers (N-B24).

#### C-08 · Carrier vetting and freight fraud
- **Sentence:** "Checking that a carrier is real, insured and actually hauling the load, for brokers and shippers hiring carriers they don't know, handled today by manual FMCSA look-ups and carrier-monitoring services."
- **Who (X):** brokers (25,081) and shippers that use spot carriers.
- **What (J4, J7):** "Make sure the truck that shows up is the one we hired, and the load isn't stolen or double-brokered."
- **How:**
  - H01 carrier-onboarding staff.
  - Registry look-ups.
  - Monitoring services such as Highway: 1,000+ brokers, including 70 of the top 100, and about 915,000 fraud attempts blocked in a year (N-G43, investor thesis).
  - Other vendors were not researched in S1.
- **Roles:** cost falls on brokers, shippers and insurers: 3,625 theft incidents in 2024, averaging $202,364 (N-C23) | decides: broker compliance lead | pays: broker | harder side: carrier side (*assumed*: honest carriers must share data).
- **End users:**
  - Broker: carrier-onboarding and compliance specialist.
  - Carrier: owner or dispatcher.
- **Sub-market signs:**
  - products ✓ identity, insurance and location checks;
  - customers ✓ brokers;
  - competitors ✓ monitoring services;
  - price ?
  - channels ?
  - **3 of 5**.
- **Source of the idea:** grid H01 × X; investor maps (fraud, N-G43); R38 ("double-brokering"). The saving here is mostly risk avoided, which §7 of the process doc calls hard to count. That is a question for K7 at S2.

#### C-09 · Auditing and paying truckload and LTL bills
- **Sentence:** "Checking and paying truckload and LTL freight bills, for mid-sized manufacturers and distributors, handled today by accounts-payable clerks, contingency audit firms and, for larger shippers, audit-and-payment providers."
- **Who (X):** as C-01.
- **What (J5):** "Pay only what we owe, on time."
- **How:**
  - H16 accounts-payable (AP) clerks match each invoice to the bill of lading, the proof of delivery and the quote.
  - H17 audit firms are paid 25-50% of what they recover (N-A25, N-A26).
  - Audit-and-payment providers:
    - Cass paid $36.4B across 34.5M invoices in 2025 (N-D30);
    - U.S. Bank pays about $46B a year (N-D31);
    - a Gartner guide names about 15 providers (N-F50, *assumed*).
- **Roles:** cost falls on the shipper (overpayments, clerk time) | decides: shipper finance or logistics | pays: shipper | harder side: shipper side (*assumed*).
- **End users:**
  - Shipper: AP clerk (43-3031) and logistics coordinator.
  - Carrier: billing clerk.
- **Sub-market signs:**
  - products ✓ invoice matching and payment;
  - customers ✓ mid-sized shippers;
  - competitors ✓ "a few primary competitors and numerous small ... audit firms" (N-D30);
  - price ✓ contingency, or per invoice;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H17/H16 × X; R28 ("invoice processing"); chain C (step C5).

#### C-10 · Cargo loss and damage claims
- **Sentence:** "Filing and recovering cargo loss and damage claims, for small and mid-sized shippers, handled today by shippers' own staff, their brokers, and contingency claims services."
- **Who (X):** all general-freight shippers.
- **What (J7):** "Get paid back for goods that arrive damaged, short, or not at all."
- **How:**
  - H16 in-house staff.
  - H17 claims services: "if we don't win, you don't pay" (N-F56, vendor).
  - Claims modules in audit platforms (N-F51).
  - The rules:
    - carriers must acknowledge a claim within 30 days and settle within 120 (49 CFR 370, N-F35);
    - shippers get at least 9 months to file (N-F36).
- **Roles:** cost falls on the shipper until the carrier or its insurer pays | decides: shipper logistics or finance | pays: the carrier or insurer pays the claim; the shipper pays any claims service | harder side: carrier side (*assumed*: it holds the evidence and the money).
- **End users:**
  - Shipper: claims coordinator and receiving clerk (43-5071).
  - Carrier: claims clerk.
- **Sub-market signs:**
  - products ✓ claim filing and evidence tracking;
  - customers ✓ small and mid-sized shippers;
  - competitors ✓ claims firms;
  - price ✓ contingency;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H17/H16 × X; theft data (N-C23, N-G77).

### 4.2 LTL, parcel and final mile (C-11 to C-13)

#### C-11 · LTL class, reweigh and reclass disputes
- **Sentence:** "Rating and classing LTL shipments and disputing reweighs, reclasses and extra-service charges, for small manufacturers and distributors, handled today by LTL carriers and LTL-focused brokers and 3PLs."
- **Who (X: mainly G08, G10, G12):** small shippers of pallets.
- **What (J2, J6):** "Know the real price before it ships, and stop the reclass surprises."
- **How:**
  - H09 LTL carriers: 7,675 firms. The ten largest hold about 82% of LTL revenue (N-G22).
  - Shipping clerks book on carrier portals.
  - Brokers and 3PLs resell LTL.
- **Roles:** cost falls on the shipper. Vendors say reweigh and reclass fees add 10-20% to base rates, and extra-service charges are "20 to 30 percent of total LTL spend" (N-G23, N-G24, vendor claims) | decides: shipping or logistics lead | pays: shipper | harder side: carrier side (*assumed*: concentrated carriers hold the measuring records).
- **End users:**
  - Shipper: shipping clerk (43-5071).
  - Freight-company side: LTL carrier billing and inspection staff; 3PL LTL rep.
- **Sub-market signs:**
  - products ✓ class and density tools, measuring records;
  - customers ✓ small pallet shippers;
  - competitors ✓ LTL-focused 3PLs (not named in the scans);
  - price ✓ class-based tariffs and discounts;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H09 × X; chain C. Forcing event: freight class moved to a density scale on 2025-07-19 (N-G20).

#### C-12 · Parcel invoice audit, for e-commerce sellers
- **Sentence:** "Auditing parcel invoices and claiming refunds for late deliveries and billing errors, for small e-commerce sellers, handled today by UPS, FedEx and USPS and by contingency parcel-audit firms."
- **Who (G11):** 53,556 e-commerce and mail-order firms, 93.2% with under 20 employees. Parcel carries 65.3% of their shipment value (N-E02, N-E17).
- **What (J5):** "Stop overpaying on every package."
- **How:**
  - H14 parcel carriers. Couriers' top-50 share is 90.9% (R44).
  - H17 parcel-audit firms: Refund Retriever, Intelligent Audit, TCR, RefundPros, Parcel Service Refund (N-F52, N-F53). Vendor claims: they take 25-50% of recoveries, which run at "2% and 5%" of parcel spend.
- **Roles:** cost falls on the seller | decides: owner or operations lead | pays: seller | harder side: carrier side (*assumed*: the carriers control the data and the refund rules).
- **End users:**
  - Seller: shipping clerk or operations lead.
  - Carrier: automated claim portals, not a person.
- **Sub-market signs:**
  - products ✓ parcel invoice audit;
  - customers ✓ small e-commerce sellers;
  - competitors ✓ parcel-audit firms;
  - price ✓ contingency;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H14/H17 × G11.

#### C-13 · Big-and-bulky home delivery
- **Sentence:** "Scheduling big-and-bulky home deliveries and handling damage and redelivery, for furniture and appliance sellers, handled today by final-mile carriers and white-glove 3PLs."
- **Who (G12):** 14,044 furniture makers, 81.3% with under 20 employees (N-E17), plus furniture and appliance retailers.
- **What (J2, J7):** "Get the sofa into the living room on the promised day, undamaged."
- **How:**
  - H04 final-mile carriers: 4,827 local-delivery firms (N-F01).
  - Named providers: Ryder, Hub Group, J.B. Hunt Final Mile, Deliveright (N-G75).
  - One vendor reports a 2.4% damage rate against "12-15% of average furniture carriers" (vendor claim).
- **Roles:** cost falls on the seller (redeliveries, damage, refunds) | decides: seller's operations lead | pays: seller | harder side: freight-company side (*assumed*: fragmented local delivery crews).
- **End users:**
  - Seller: customer-service or logistics coordinator.
  - Freight-company side: final-mile dispatcher and delivery crew.
- **Sub-market signs:**
  - products ✓ two-person crews, room-of-choice delivery;
  - customers ✓ furniture and appliance sellers;
  - competitors ✓ big-and-bulky networks;
  - price ✓ per stop, by service level;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H04 × G12; fringe (scan G note); R28 ("last mile").

### 4.3 Planning, own fleets, warehouses and inbound freight (C-14 to C-18)

#### C-14 · Planning and consolidating shipments
- **Sentence:** "Planning how to ship (choosing the mode, pooling LTL into multi-stop truckloads, moving long lanes to rail intermodal), for mid-sized shippers, handled today by managed-transportation 3PLs on gainshare, intermodal marketing companies, or in-house spreadsheets."
- **Who (X):** as C-01.
- **What (J8):** "Ship the same goods for less by combining and choosing better."
- **How:**
  - H03 managed-transportation 3PLs, paid "a percent of the purchased transportation ... gainshares" (R33).
  - H02 intermodal marketing companies: 18.5M intermodal units moved in 2025 (N-F14).
  - H16 spreadsheets.
- **Roles:** cost falls on the shipper | decides: traffic or logistics manager | pays: shipper (a fee or a gainshare) | harder side: shipper side (*assumed*).
- **End users:**
  - Shipper: traffic manager or logistics analyst (13-1081, 11-3071).
  - Freight-company side: 3PL planner or intermodal rep.
- **Sub-market signs:**
  - products ✓ optimisation;
  - customers ✓ mid-sized shippers;
  - competitors ✓ 3PLs, intermodal marketers, TMSs;
  - price ✓ gainshare;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H03/H02 × X; R33 (the gainshare precedent). The intermodal cell is merged here (M-6).

#### C-15 · Routing own delivery fleets
- **Sentence:** "Planning daily routes and loads for their own delivery trucks, for food, beverage, industrial and drug distributors (and processors that run their own fleets), handled today by in-house dispatchers with spreadsheets or routing tools."
- **Who (G02, G10, G17, G05):** share of each group's freight carried in its own trucks (N-E02, N-E05):

  | Group | Own-truck share |
  |---|---|
  | Grocery distributors | 61.5% of tons |
  | Beer and wine distributors | 91.1% |
  | Hardware and plumbing distributors | 51.5% |
  | Drug wholesalers | 51.3% |
  | Meat | 32.4% of tons |

- **What (J8, J2):** "Get today's orders delivered with fewer trucks and miles."
- **How:**
  - H15 private fleets: 170,221 private-only interstate fleets, 86.4% with 10 or fewer trucks; 807,829 counting fleets that stay inside one state (N-F02).
  - NPTC fleets move 70.4% of their outbound shipments in-house (N-F19).
  - H07 dedicated contract carriage is the outsourced alternative: $32.0B in 2025 (R33; M-3).
- **Roles:** cost falls on the distributor (fleet cost) | decides: transportation or fleet manager | pays: distributor | harder side: shipper side, the only paying side (*assumed*). The other side is the customers' receiving docks.
- **End users:**
  - Distributor: in-house dispatcher or route planner (43-5032).
  - The fleet: driver (53-3032).
- **Sub-market signs:**
  - products ✓ multi-stop routing;
  - customers ✓ distributors with their own fleets;
  - competitors ? routing software, not researched in S1;
  - price ?
  - channels ✓ NPTC and distributor associations (*assumed*).
  - **3 of 5**.
- **Source of the idea:** grid H15 × G02, G10, G17. Merges M-3 and M-7.

#### C-16 · Job-site deliveries, for building-material dealers
- **Sentence:** "Scheduling job-site deliveries of lumber, drywall, block and aggregates, for building-material dealers and lumberyards, handled today by their own flatbed and boom-truck fleets and phone calls with contractors."
- **Who (G07):** lumber and construction-materials wholesalers. Their own trucks carry 64.6% of their shipment value, and buyers collect 17.5% of their tons themselves (N-E02).
- **What (J2, J8):** "Get the right load to the site when the crew is ready."
- **How:** H15 own fleets; H16 phone calls with contractors.
- **Roles:** cost falls on the dealer (truck hours, failed deliveries) and the contractor (crews waiting) | decides: dealer's dispatcher or yard manager | pays: dealer | harder side: the receiver, the contractor (*assumed*).
- **End users:**
  - Dealer: dispatcher (43-5032).
  - Receiver: the contractor's site superintendent.
- **Sub-market signs:**
  - products ✓ boom and crane trucks, site limits;
  - customers ✓ building-material dealers;
  - competitors ? not researched;
  - price ?
  - channels ✓ dealer associations (*assumed*).
  - **3 of 5**.
- **Source of the idea:** grid H15 × G07.

#### C-17 · Controlling inbound freight from suppliers
- **Sentence:** "Controlling inbound freight from many suppliers (routing guides, collect or prepaid terms, supplier pick-ups), for mid-sized distributors and manufacturers, handled today by the suppliers' chosen carriers and the buyer's purchasing staff."
- **Who (X, as receivers):**
  - Customer pick-up moves 11.4% of CFS tons (R32).
  - "Only about 35% of companies use a formal routing guide for inbound freight" (N-E31, vendor snippet, *assumed*).
- **What (J1, J2):** "Stop paying for suppliers' freight choices we don't control."
- **How:**
  - H16 purchasing and receiving staff.
  - The suppliers' carriers and brokers.
  - Walmart runs the large-retailer version: "collect" pick-ups priced as a share of cost of goods (N-E27).
- **Roles:** cost falls on the buyer (freight built into prices, or billed separately) | decides: purchasing manager | pays: the buyer (collect), or the supplier (prepaid) who passes it on in price | harder side: supplier side (*assumed*: suppliers must follow the guide).
- **End users:**
  - Buyer: purchasing or receiving manager.
  - Supplier: shipping clerk.
- **Sub-market signs:**
  - products ✓ routing guides, inbound booking;
  - customers ✓ receivers;
  - competitors ? not researched;
  - price ✓ collect vs prepaid;
  - channels ?
  - **3 of 5**.
- **Source of the idea:** the customer pick-up note in S1 (R32); grid H16 × X.

#### C-18 · Warehouse storage and handling bills
- **Sentence:** "Billing storage, handling and extra warehouse services, for e-commerce sellers and distributors that store goods with others, handled today by small public and contract warehouses on spreadsheets and warehouse-system modules."
- **Who (G11 and G10 as customers; G16):** 6,789 general-warehouse firms, 53% with under 20 employees (N-F01).
- **What (J5):**
  - Seller: "pay the right storage and handling bill."
  - Warehouse: "bill every pallet moved and every extra service."
- **How:** H06 public and contract warehouses. They charge storage per pallet per month, $12-25 ambient and $25-50 cold, plus handling (N-F64, *assumed*).
- **Roles:** cost falls on the warehouse (unbilled work) or its customer (billing errors) | decides: warehouse owner | pays: warehouse | harder side: customer side (*assumed*).
- **End users:**
  - Warehouse: billing or inventory clerk (43-5071, 43-3031).
  - Customer: the seller's operations lead.
- **Sub-market signs:**
  - products ✓ storage and handling billing;
  - customers ✓ small public and contract warehouses;
  - competitors ? warehouse-system billing modules, not researched;
  - price ✓ per pallet plus handling;
  - channels ?
  - **3 of 5**.
- **Source of the idea:** grid H06 × G10, G11. It covers the "handling" half of the origin hypothesis ("shipping and handling").

### 4.4 Retail compliance (C-19)

#### C-19 · Retailer OTIF fines and deductions
- **Sentence:** "Meeting retailers' on-time-in-full rules and disputing the fines and deductions, for small and mid-sized suppliers to big-box retailers, handled today by their carriers and brokers plus in-house deductions staff."
- **Who (G15, mostly G01 and consumer-goods makers):**
  - Walmart fines 3% of the cost of goods on late or short cases (N-E24 to N-E26, N-G35). Its goals:
    - 90% on time (prepaid);
    - 98% ready for pick-up (collect);
    - 95% in full.
  - Kroger charged "$500 per day" for late deliveries (2017, N-E25).
- **What (J6, J7):** "Stop losing 3% on late or short cases, and win back the fines we don't owe."
- **How:**
  - H01/H08 carriers and brokers supply the proof.
  - H16 deductions analysts.
  - Deduction-management software: iNymbus, HighRadius, RetailPath, DOSS, Vendormint (N-F55, vendor).
- **Roles:** cost falls on the supplier. Vendors say deductions take 5-7% of revenue, and 10-20% of them are invalid (N-G36, vendor claims) | decides: supplier's logistics or finance lead | pays: supplier | harder side: the retailer, which sets the rules, and the carriers, which hold the proof (*assumed*).
- **End users:**
  - Supplier: deductions or receivables analyst, and logistics manager.
  - Freight-company side: carrier or broker customer-service rep.
- **Sub-market signs:**
  - products ✓ deduction tracking and dispute packets;
  - customers ✓ retail suppliers;
  - competitors ✓ deduction-management vendors;
  - price ?
  - channels ✓ retail-supplier consultancies and communities (*assumed*).
  - **4 of 5**.
- **Source of the idea:** grid H16 × G15; chain E (step E8).

### 4.5 International and border (C-20 to C-25)

#### C-20 · Import entries, for small importers
- **Sentence:** "Preparing and filing import entries (classifying goods, calculating duty, filing the security filing), for small importers, handled today by small customs brokerages' entry writers."
- **Who (G13):** 240,535 importers in 2024. 92,517 have 1-19 employees, and 36.5% are wholesalers (N-E18).
- **What (J4):** "Clear my goods fast, at the right duty, with no penalties."
- **How:**
  - H05 customs brokers: about 14,500 licensed individuals (N-F09, *assumed*). All have worked under one national permit since December 2022 (N-F08).
  - Entry writers work "under the supervision of a licensed Customs Broker" (N-F61).
  - About 70 vendors are on CBP's filing-software list (N-F10).
  - More than 3M entry summaries were filed in March 2025 alone (N-F11).
- **Roles:** cost falls on the importer (duty errors, holds, fees) | decides: the importer's owner or logistics lead | pays: importer | harder side: broker side (*assumed*).
- **End users:**
  - Importer: logistics coordinator.
  - Broker: customs entry writer and licensed broker (O*NET 13-1041.08).
- **Sub-market signs:**
  - products ✓ CBP filing interface;
  - customers ✓ small importers;
  - competitors ✓ filing-software vendors: Descartes brands, Magaya, E2open, CustomsCity, KlearNow;
  - price ✓ per entry;
  - channels ✓ customs-broker associations (*assumed*).
  - **5 of 5**.
- **Source of the idea:** grid H05 × G13; chain A. Tariffs added customs work in 2025: Expeditors' customs brokerage revenue rose 12.9% (N-C13, N-C15).

#### C-21 · Container demurrage and detention
- **Sentence:** "Avoiding and disputing container demurrage and detention charges, for small and mid-sized importers, handled today by their forwarders or NVOCCs, customs brokers and port drayage truckers."
- **Who (G13):** as C-20. In 2024, 55.9% of import tons arrived by water (N-E09).
- **What (J6):** "Stop paying daily fees for containers left at the port or kept too long."
- **How:**
  - H05 forwarders and NVOCCs (about 8,600 NVOCCs, N-F05), plus customs brokers.
  - H10 drayage carriers.
  - Tools: BuyCo, GoComet, Portcast, Vizion, Terminal49, BlueCargo (N-F54, vendor list).
- **Roles:** cost falls on the importer, or on the trucker billed. Nine carriers billed about $8.9B and collected about $6.9B in 2020-22 (N-G01). The FMC counts about $15.4B charged from April 2020 to March 2025 (N-F31) | decides: the importer's logistics coordinator or its forwarder | pays: the party billed, which must be either the party that contracted for the transport or the consignee (N-F32) | harder side: ocean carrier and terminal side (*assumed*: they set free time and issue the bills).
- **End users:**
  - Importer: logistics coordinator (13-1081).
  - Freight-company side: forwarder operations rep (43-5011) and drayage dispatcher.
- **Sub-market signs:**
  - products ✓ free-time tracking, and invoice checks against the FMC rule;
  - customers ✓ small and mid-sized importers;
  - competitors ✓ demurrage-and-detention tools;
  - price ✓ per-day charges, with rule-based disputes;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** chain A; R26 ("About $200 per pallet per day"); the FMC's 2024 rule (N-F32, N-G03).

#### C-22 · Port drayage dispatch
- **Sentence:** "Dispatching container pick-ups and returns (terminal appointments, chassis, empty returns), for importers' and exporters' containers, handled today by small port drayage carriers by phone, terminal portals and spreadsheets."
- **Who (G13, G14):** importers and exporters moving containers through ports.
- **What (J2, J6):**
  - Importer: "get my box out before free time runs out."
  - Drayage carrier: "get the appointment, the chassis and the empty return done without dry runs."
- **How:**
  - H10 drayage carriers: 48,991 interstate carriers tick "intermodal containers" (N-F02). The Los Angeles/Long Beach drayage registry holds 23,000+ trucks (N-F21).
  - Terminal fees are separate, e.g. PierPass at $38.78 per 20-foot container (N-G11, *assumed*).
- **Roles:** cost falls on the drayage carrier (waiting, dry runs) and the importer (per-diem and chassis charges) | decides: the drayage owner or dispatcher | pays: the drayage carrier pays for its own tools; the importer pays the extra charges | harder side: terminal side (*assumed*).
- **End users:**
  - Drayage carrier: dispatcher (43-5032).
  - Importer or forwarder: coordinator.
- **Sub-market signs:**
  - products ✓ terminal appointments, chassis tracking;
  - customers ✓ port drayage firms;
  - competitors ? drayage software, not researched;
  - price ✓ per move, plus chassis and waiting charges;
  - channels ✓ port-based communities (*assumed*).
  - **4 of 5**.
- **Source of the idea:** grid H10 × G13; R28 ("drayage"); chain A (steps A6-A9).

#### C-23 · Quoting and booking international freight
- **Sentence:** "Quoting and booking ocean and air freight, for small importers, handled today by small forwarders and NVOCCs working from rate sheets, email and forwarding software."
- **Who (G13):** 97.3% of importers are small or mid-sized (N-E18).
- **What (J1, J4):** "Get a firm door-to-door price and a booking this week."
- **How:**
  - H05 ocean intermediaries: over 9,100, about 8,600 of them NVOCCs (N-F05).
  - Software for small forwarders: BoxTop, sold for about $13M (N-B25). Others were not researched.
  - Flexport targeted this importer (R26).
- **Roles:** cost falls on the forwarder (staff time per quote) and the importer (slow quotes, rate surprises) | decides: forwarder owner | pays: forwarder | harder side: importer side (*assumed*).
- **End users:**
  - Forwarder: pricing or operations rep (43-5011).
  - Importer: logistics coordinator.
- **Sub-market signs:**
  - products ✓ rate management and booking;
  - customers ✓ small forwarders;
  - competitors ✓ forwarding software;
  - price ✓ a markup on ocean space;
  - channels ?
  - **4 of 5**.
- **Source of the idea:** grid H05 × G13; R26; check B (BoxTop).

#### C-24 · Export documents, for farm and food exporters
- **Sentence:** "Preparing export documents (export filings, certificates of origin, phytosanitary and inspection certificates, letter-of-credit papers), for small farm and food exporters, handled today by forwarders and export-document services."
- **Who (G14):**
  - 271,250 exporters; 97.1% are small or mid-sized, and 60% export to only one country (N-E18).
  - Farm and food exports were 214.8M tons in 2024 (N-E09).
- **What (J4):** "Get the papers right, so the container isn't held or rejected abroad."
- **How:**
  - H05 forwarders.
  - Official inspection and weight certificates are mandatory for export grain (N-G31, *assumed*).
- **Roles:** cost falls on the exporter (holds, rejections, bank fees for document discrepancies; *assumed*) | decides: the exporter's export coordinator | pays: exporter | harder side: exporter side (*assumed*).
- **End users:**
  - Exporter: export coordinator.
  - Forwarder: documentation clerk.
- **Sub-market signs:**
  - products ✓ certificate and filing packets;
  - customers ✓ farm and food exporters;
  - competitors ? not researched;
  - price ?
  - channels ✓ commodity export groups (*assumed*).
  - **3 of 5**.
- **Source of the idea:** grid H05 × G14; chain D (step D5); farm-origin family.

#### C-25 · Cross-border Mexico truckloads through Laredo
- **Sentence:** "Moving truckloads across the US-Mexico border (Mexican export filing, US entry, transfer across the bridge, trailer interchange), for manufacturers and retailers trading with Mexico, handled today by customs brokers on both sides, transfer carriers and cross-border brokers."
- **Who (G13, G14; across industries):** automotive, electronics and industrial shippers. Laredo sees about 6M truck crossings a year (N-G74, *assumed*).
- **What (J4, J2):** "Get the load across without sitting at the bridge."
- **How:**
  - H05 Mexican and US customs brokers.
  - H10 transfer carriers, which pull trailers across the bridge (no count found).
  - H01 cross-border brokers: Cargado, Nuvocargo, Traffix, Uber Freight (N-G18, N-G40, N-G74).
- **Roles:** cost falls on the shipper (delays, broker fees) and on carriers (waiting) | decides: the shipper's logistics lead or its broker | pays: shipper | harder side: Mexican side (*assumed*: the export filing goes through a Mexican customs broker).
- **End users:**
  - Shipper: trade or logistics coordinator.
  - Freight-company side: customs entry writer; transfer-carrier dispatcher.
- **Sub-market signs:**
  - products ✓ bonded through-trailers, Mexican export filing;
  - customers ✓ manufacturers moving production to Mexico;
  - competitors ✓ cross-border brokers;
  - price ✓ transfer fees and Mexico's 16% VAT;
  - channels ✓ the Laredo broker cluster.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #15); investor maps (cross-border, N-G40).

### 4.6 Farm-origin and food (C-26 to C-33)

This family covers the origin hypothesis: freight that starts on a farm, or near one. The process doc treats it as one family among several, not the default (§8.4).

#### C-26 · Produce reefer booking and rejected loads
- **Sentence:** "Booking reefer trucks and settling rejected or temperature-damaged loads, for fresh-produce grower-shippers and packers, handled today by produce brokers and small reefer carriers."
- **Who (G03):**
  - 41,793 vegetable farms, 97,343 fruit farms and 4,480 produce wholesalers; over 13,200 PACA licensees in 2020 (N-E11, N-E14, N-E17).
  - Seasonal and regional: California, Arizona, Florida, the Pacific Northwest, and Mexico (R34).
- **What (J1, J7):** "Get a clean reefer at a fair rate in peak season, and don't eat the loss when a load is rejected."
- **How:**
  - H01 produce brokers.
  - H11 reefer carriers: 105,756 interstate carriers tick refrigerated food or produce (N-F02).
  - Rates run $1.50-2.76 a mile. The 501-1,500-mile rate went from $3.62 in Q1 2022 to $2.23 in Q4 2025 (R34).
- **Roles:** cost falls on the shipper and receiver (rejections, salvage) and on the carrier (temperature claims) | decides: the shipper's sales or transportation desk | pays: depends on the sale terms (*assumed*) | harder side: carrier side (*assumed*).
- **End users:**
  - Shipper: transportation coordinator or sales desk.
  - Carrier: reefer dispatcher.
- **Sub-market signs:**
  - products ✓ temperature records, USDA inspection certificates;
  - customers ✓ the PACA trading world;
  - competitors ✓ produce brokers; Blue Book, a produce credit agency;
  - price ✓ seasonal spot rates and inspection fees;
  - channels ✓ Blue Book and produce associations (*assumed*).
  - **5 of 5**.
- **Source of the idea:** grid H01/H11 × G03; chain B. One load can lead to two separate disputes: PACA for the trading parties, trucking liability law for the carrier (N-G12).

#### C-27 · Cross-border produce at Nogales and Pharr
- **Sentence:** "Getting Mexican produce across the border and onto US trucks (two customs brokers, a transfer carrier, inspections, a cold dock), for produce importers and distributors at Nogales and Pharr, handled today by customs brokers, transfer carriers and border cold storage."
- **Who (G03, G13):**
  - 45% of the produce moved by truck in Q1 2026 came from Mexico (R34).
  - Nogales has over 85 produce distributors and about 120,000 produce trucks a year (a 2013 study; N-G17, *assumed* and dated).
- **What (J4, J2):** "Clear it, inspect it, and get it onto a US reefer before it loses value."
- **How:**
  - H05 Mexican and US customs brokers.
  - H10 transfer carriers.
  - H06 cold docks.
  - USDA import inspection at $0.00635 per pound (N-G14).
- **Roles:** cost falls on the importer (storage days, inspection holds, spoilage) | decides: the importer or distributor | pays: importer | harder side: Mexican side (*assumed*).
- **End users:**
  - Importer: logistics coordinator.
  - Freight-company side: customs entry writer, transfer-carrier dispatcher, cold-dock staff.
- **Sub-market signs:**
  - products ✓ perishable border hand-offs;
  - customers ✓ border produce distributors;
  - competitors ✓ border-specialist brokers such as Traffix and Cargado (N-G18);
  - price ✓ per-pound inspection, storage;
  - channels ✓ the Nogales cluster.
  - **5 of 5**.
- **Source of the idea:** chain B (border variant); R34.

#### C-28 · Harvest grain hauling and scale tickets
- **Sentence:** "Scheduling harvest trucks and matching scale tickets to contracts, for grain farms and country elevators, handled today by farm-owned trucks, custom haulers and elevator staff on paper tickets and phone."
- **Who (G04):**
  - 330,930 grain and oilseed farms and 7,922 off-farm storage facilities (N-E11, N-E13).
  - Domestic grain moves 80% by truck (N-E10).
  - Midwest and Plains, with a harvest peak.
- **What (J2, J4, J5):**
  - Farmer: "keep the combine running, and get paid for every load."
  - Elevator: "match every ticket to the right contract."
- **How:**
  - H15 farm trucks.
  - H11 grain haulers: 145,062 for-hire carriers tick grain, feed or hay, counting all operations (N-G49).
  - Custom harvesters: about 650 members in their association (N-G54, *assumed*).
  - Elevator software (Agvance, GSS; N-G30) and Bushel (R30).
- **Roles:** cost falls on the farmer (waiting, slow payment) and the elevator (clerk time) | decides: the elevator manager, and the farmer | pays: the elevator pays for software; the farmer pays haul costs | harder side: farmer side (*assumed*: R30 found "going direct to the farmer hasn't worked").
- **End users:**
  - Elevator: scale-house clerk and grain accountant.
  - Farm side: farmer or custom hauler.
- **Sub-market signs:**
  - products ✓ scale tickets matched to contracts;
  - customers ✓ elevators and farms;
  - competitors ✓ elevator software, Bushel;
  - price ?
  - channels ✓ co-ops and grain associations (*assumed*).
  - **4 of 5**.
- **Source of the idea:** grid H15/H11 × G04; chain D (steps D1-D3); fringe (harvest hauling); R30.

#### C-29 · Buying rail and barge freight for grain
- **Sentence:** "Buying and timing rail and barge capacity (train-loading rights, car orders, barge freight), for country elevators and grain merchandisers, handled today by Class I railroads' allocation programs and barge brokers, with merchandisers on spreadsheets."
- **Who (G04, G14):** 1,839 grain-wholesaler firms with 4,481 sites (N-E17). Export grain moves 45% by rail and 44% by barge (N-E10).
- **What (J1, J6):** "Lock in cars and barges at the right time and price."
- **How:**
  - H13 rail: 6 Class I railroads, whose train-loading rights are auctioned and resold (e.g. BNSF's certificates).
  - H13 barge: barge freight is quoted as a percentage of a 1976 tariff, with extra demurrage and fleeting charges.
  - A barge marketplace, OpenTug (N-G76).
  - Includes inland barge shippers (M-5).
- **Roles:** cost falls on the elevator. Freight costs swing sharply: barge freight was 792% of tariff on 2026-09-08 against a 2025 average of 435% (N-G25), and train-right bids ran from +$563 to −$100 per car (N-G27, N-G28) | decides: grain merchandiser | pays: the elevator or merchandiser | harder side: railroad side (*assumed*: concentrated).
- **End users:**
  - Elevator: grain merchandiser or logistics manager.
  - Freight-company side: railroad customer service; barge broker.
- **Sub-market signs:**
  - products ✓ tradable train rights, barge quotes;
  - customers ✓ elevators;
  - competitors ✓ barge marketplaces, railroad programs;
  - price ✓ quoted as a % of tariff;
  - channels ✓ the grain trade (USDA's Grain Transportation Report).
  - **5 of 5**.
- **Source of the idea:** grid H13 × G04, G14; chain D (step D4); fringe (barge).

#### C-30 · Rail demurrage and accessorial invoices
- **Sentence:** "Checking and disputing railcar demurrage and accessorial invoices and managing car orders, for rail-served chemical, plastics, paper, scrap and grain processors, handled today by Class I and short-line railroads, with shipper traffic staff on spreadsheets."
- **Who (G06, G07, G04):**
  - Chemical makers ship 21.5% of their tons by rail, and 16.2% of plastics and rubber tons go by rail (N-E02, N-E05).
  - Short lines serve about 10,000 customers (N-F12).
- **What (J6):** "Stop paying for car-days we didn't cause."
- **How:**
  - H13 railroads: 6 Class I railroads with 89% of rail revenue, and about 603 short lines (N-F12, N-F13).
  - Charges: demurrage of $60-150 per car per day, and accessorials of $60-500 per instance (N-G34, *assumed*, 2019).
  - Class I railroads collected $1.18B in demurrage in the first nine months of 2021 (N-F34).
  - A 2021 regulator rule (STB, EP 759) sets the minimum contents of demurrage invoices, and requires machine-readable data (N-G33).
- **Roles:** cost falls on the shipper | decides: the shipper's rail or traffic manager | pays: shipper | harder side: railroad side (*assumed*: concentrated).
- **End users:**
  - Shipper: traffic manager (11-3071, 13-1081).
  - Railroad: customer service.
- **Sub-market signs:**
  - products ✓ car-day tracking, and invoice checks against the STB rule;
  - customers ✓ rail-served plants;
  - competitors ? one service firm named (RSI Logistics) and no software found, so possibly unserved;
  - price ✓ per car per day;
  - channels ✓ shipper associations (NITL, ReMA).
  - **4 of 5**.
- **Source of the idea:** grid H13 × G06, G07; fringe (rail carload shippers; scrap's rail demurrage).

#### C-31 · Livestock hauling
- **Sentence:** "Scheduling livestock loads and keeping their papers straight (health certificates, brand inspections, hours-of-service exemptions), for ranchers, feedlots and auction markets, handled today by small livestock haulers by phone and paper."
- **Who (G05):**
  - 534,633 beef ranches, 11,186 feedlots and 1,221 auction markets (N-E11, N-E16).
  - Live animals move 99.8% by truck (N-E09).
- **What (J2, J4):** "Get the cattle to the sale on time, with the right papers."
- **How:**
  - H11 livestock haulers: 25,365 interstate for-hire carriers tick livestock, 93.7% of them with 10 or fewer trucks (N-F02).
  - Tools: the Livestock Loads load board, M2X, Toro TMS (N-G52).
  - Driving-hours exemption: 150 air-miles around the origin, plus 150 around the destination (N-G51, *assumed*).
- **Roles:** cost falls on the rancher (weight loss in transit, delays) and the hauler (compliance time) | decides: the hauler owner; the sale barn | pays: the shipper pays the haul | harder side: rancher side (*assumed*: dispersed, as R30 found for farmers).
- **End users:**
  - Hauler: owner or dispatcher.
  - Auction market: office staff.
- **Sub-market signs:**
  - products ✓ live cargo, special trailers;
  - customers ✓ the cattle sector;
  - competitors ✓ a livestock load board and livestock TMSs;
  - price ?
  - channels ✓ cattle associations (NCBA, LMA).
  - **4 of 5**.
- **Source of the idea:** fringe (scan G #1).

#### C-32 · Milk pickup and hauling settlement
- **Sentence:** "Recording farm milk pickups (weights, samples) and settling hauling charges, for dairy farms and their co-ops, handled today by co-op fleets and contract milk haulers."
- **Who (G05):** 23,153 dairy farms (N-E11).
- **What (J4, J5):**
  - Farm: "get credited for every pound, and pay the right hauling rate."
  - Hauler: "log each pickup and sample, and get paid."
- **How:**
  - H11 bulk milk haulers (no count found). Drivers act as licensed samplers and weighers.
  - Tools: AMCS Bulk Hauling, Toro TMS (N-G53).
- **Roles:** cost falls on the farm. Hauling is charged per hundredweight, about 12¢ in Wisconsin against 46¢ in North Dakota, and 75¢ for small farms against 16¢ for large ones (N-G53, *assumed*) | decides: the co-op | pays: the farm, through its milk check | harder side: co-op side (*assumed*).
- **End users:**
  - Hauler: driver-sampler.
  - Co-op: field or payroll staff.
- **Sub-market signs:**
  - products ✓ food-grade tankers, licensed sampling;
  - customers ✓ dairy co-ops;
  - competitors ✓ bulk-hauling software;
  - price ✓ charges per hundredweight;
  - channels ✓ co-ops and Federal Milk Marketing Orders.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #2).

#### C-33 · Cut-flower air imports into Miami
- **Sentence:** "Clearing air-freighted cut flowers through inspection and into cold trucks, for flower importers in Miami, handled today by air cargo handlers, customs brokers and reefer truckers."
- **Who (G03, G13):** US importers of Colombian and Ecuadorian flowers. Miami airport handles about 88% of US cut-flower imports, and CBP had inspected more than 1B stems by 2026-02-06 (N-G68, *verified*).
- **What (J4, J2):** "Get the stems inspected and onto trucks before Valentine's Day."
- **How:**
  - H13 air cargo.
  - H05 customs brokers.
  - H11 reefer trucks.
  - CBP agricultural inspection.
- **Roles:** cost falls on the importer (pest holds, delays, spoilage) | decides: importer | pays: importer | harder side: CBP and airport side (*assumed*).
- **End users:**
  - Importer: logistics coordinator.
  - Freight-company side: customs entry writer; airport cargo handler.
- **Sub-market signs:**
  - products ✓ perishable air cargo, pest inspection;
  - customers ✓ the Miami importer cluster;
  - competitors ? no specialized firm identified, so possibly unserved;
  - price ?
  - channels ✓ the Miami cluster.
  - **3 of 5**.
- **Source of the idea:** fringe (scan G #12).

### 4.7 Specialized and industrial (C-34 to C-40)

#### C-34 · Oversize and overweight permits
- **Sentence:** "Getting state permits and routes for oversize and overweight loads, for equipment, energy and construction shippers, handled today by heavy-haul carriers and permit services."
- **Who (G08, G09, plus energy and construction):** machinery makers send 79.0% of their tons by hired truck (N-E02).
- **What (J4):** "Get every state's permit for this route, fast."
- **How:**
  - H11 heavy-haul carriers: 87,293 interstate carriers tick "machinery, large objects" (N-F02).
  - H17 permit services: J.J. Keller, State Permits ("over one million permits since 1986", vendor claim), Highway Permits, OmniPermits, Oversize.io (N-F42, N-G57). They charge $50.50-150 per permit on top of state fees (N-F42, vendor).
  - Washington state alone issued 183,502 permits in 2023, 85% of them self-issued online (N-G55, *verified*).
  - Rules differ from state to state (GAO, N-G56).
- **Roles:** cost falls on the carrier (permit clerk time, fees passed on to the shipper) | decides: the carrier's dispatcher or permit clerk | pays: carrier, then shipper | harder side: the states (*assumed*).
- **End users:**
  - Carrier: permit clerk or dispatcher.
  - Shipper: logistics coordinator.
- **Sub-market signs:**
  - products ✓ multi-state permitting;
  - customers ✓ heavy haulers;
  - competitors ✓ permit services;
  - price ✓ per permit;
  - channels ✓ state permit portals.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #4); grid H11/H17 × G08.

#### C-35 · Tank loads: hazmat papers and tank-wash certificates
- **Sentence:** "Preparing hazmat shipping papers and matching tank-wash certificates to each load, for chemical and food-liquid shippers, handled today by shippers' compliance staff and tank truck carriers."
- **Who (G06, and G01's liquid foods):**
  - Hazmat is 21.3% of CFS tons (N-E07).
  - Chemical wholesalers carry 45.1% of their tons in their own trucks (N-E02).
- **What (J4):** "Ship it legally, in a tank that's clean for this product."
- **How:**
  - H11 tank carriers: 25,521 for-hire carriers tick chemicals, counting all operations, and 73.6% of them run 5 or fewer trucks (N-G49).
  - The tank-truck association says its "over 200" members haul over 80% of tank volume (N-F67, *assumed*).
  - Hazmat-paperwork software exists (Labelmaster DGIS, N-F58). No tank-wash software firm was found (N-G58).
- **Roles:** cost falls on the shipper (fines, rejected loads) and the carrier (wash costs) | decides: the shipper's safety and compliance staff | pays: shipper | harder side: carrier side (*assumed*).
- **End users:**
  - Shipper: safety/compliance staff or shipping clerk.
  - Carrier: tank dispatcher; tank-wash rack staff.
- **Sub-market signs:**
  - products ✓ DOT-spec tanks, wash codes;
  - customers ✓ chemical and food-liquid shippers;
  - competitors ? no specialized software firm found;
  - price ?
  - channels ✓ the tank-truck association (NTTC).
  - **3 of 5**.
- **Source of the idea:** fringe (scan G #5); grid H11 × G06.

#### C-36 · Aggregates load tickets
- **Sentence:** "Tracking load tickets and reconciling haul pay for aggregates and asphalt, for quarries, plants and road contractors, handled today by dump-truck owner-operators and haul brokers on paper tickets."
- **Who (G07):**
  - Gravel is the largest CFS commodity by weight: 1,910.9M tons at an average of 33 miles, with 30.6% collected by the buyer (N-E04, N-E05).
  - About 1,400 companies operate 3,500 quarries (N-G60, *assumed*).
- **What (J4, J5):**
  - Contractor: "know every load delivered, and pay the right trucker."
  - Hauler: "get paid for every load."
- **How:**
  - H11/H10 dump trucks. Specialized local trucking (48422) has 31,927 firms, and the top 50 hold 9.9% of revenue (R44).
  - E-ticketing vendors: HaulHub ("nearly 40" state DOTs, vendor claim), Fast-Weigh, SMSTurbo, AMCS, Toro TMS (N-G59).
  - State transportation departments increasingly require electronic tickets (N-G59, *assumed*).
- **Roles:** cost falls on the contractor (disputes) and the hauler (unpaid loads) | decides: the contractor or the plant | pays: contractor | harder side: owner-operator side (*assumed*).
- **End users:**
  - Plant and contractor: plant scale operator; contractor's project manager.
  - Hauler: dump-truck owner-operator.
- **Sub-market signs:**
  - products ✓ e-tickets;
  - customers ✓ road contractors;
  - competitors ✓ e-ticketing vendors;
  - price ✓ per ton or per hour;
  - channels ✓ state transportation-department mandates.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #6); grid H11 × G07.

#### C-37 · Log trip tickets and haul pay
- **Sentence:** "Matching log trip tickets to mill scale slips and settling haul and landowner pay, for timber dealers, loggers and mills, handled today by log-truck contractors on paper tickets."
- **Who (G07, wood products):** 11,761 wood-products firms (N-E17).
- **What (J4, J5):** "Pay each hauler and landowner for every load that reached the mill."
- **How:**
  - H11 log trucks: 161,723 for-hire carriers tick logs, poles or lumber, counting all operations (lumber included), and 89.3% run 5 or fewer trucks (N-G49).
  - Software: Logger's Edge ("over 275 companies", vendor claim); Waldo, for digital trip tickets (N-G66).
- **Roles:** cost falls on the logger or dealer (clerk time, disputes) | decides: the timber dealer or logger | pays: dealer | harder side: mill side (*assumed*).
- **End users:**
  - Logging company: office manager.
  - Freight and mill side: log-truck driver; mill scale clerk.
- **Sub-market signs:**
  - products ✓ trip tickets, chain of custody;
  - customers ✓ loggers and dealers;
  - competitors ✓ forestry ticketing software;
  - price ✓ haul paid per ton;
  - channels ✓ timber-dealer networks.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #10).

#### C-38 · Fuel delivery reconciliation
- **Sentence:** "Reconciling terminal pick-ups with the gallons delivered to each tank, and turning deliveries into invoices, for petroleum marketers and fuel distributors, handled today by their own tank fleets and contract fuel carriers."
- **Who (G06: 4247, 45431):**
  - Petroleum wholesalers: hired trucks carry 40.2% of their tons, their own trucks 27.9%.
  - Fuel dealers: their own trucks carry 92.6% (N-E02).
- **What (J4, J5):** "Make sure every gallon loaded is billed to a customer."
- **How:**
  - H15 own tank fleets.
  - H11 fuel carriers: 41,445 for-hire carriers tick liquids or gases, counting all operations (N-G49).
  - Software: PDI (">250 petroleum marketers", vendor claim), Axxis, Red River, Toro TMS (N-G67).
- **Roles:** cost falls on the marketer (fuel lost in handling, missed billing) | decides: the marketer's dispatch or operations lead | pays: marketer | harder side: marketer side (*assumed*).
- **End users:**
  - Marketer: fuel dispatcher.
  - Fleet: driver.
- **Sub-market signs:**
  - products ✓ terminal loading receipts, per-tank delivery;
  - customers ✓ petroleum marketers;
  - competitors ✓ fuel-wholesale software;
  - price ✓ per gallon or per load;
  - channels ✓ sold with fuel-wholesale ERP systems.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #11); grid H15 × G06.

#### C-39 · Vehicle transport
- **Sentence:** "Dispatching car-hauler loads and recording vehicle condition at pick-up and delivery, for dealers, auctions and rental fleets, handled today by car-haul brokers and small car haulers through marketplaces."
- **Who (G09):** vehicle makers and dealers, and motor-vehicle wholesalers (4231) (N-E02).
- **What (J2, J7):** "Move the car, and settle damage disputes with photos, not arguments."
- **How:**
  - H11 car haulers: 76,367 interstate carriers tick motor vehicles (N-F02).
  - Marketplaces: Central Dispatch (Cox Automotive, founded 1999) and Super Dispatch, which also offers electronic bills of lading and a load board (N-G63, N-G64).
- **Roles:** cost falls on the dealer (damage) and the hauler (disputed claims) | decides: the dealer's logistics or wholesale manager | pays: dealer | harder side: hauler side (*assumed*).
- **End users:**
  - Dealer: transport coordinator.
  - Hauler: driver or dispatcher.
- **Sub-market signs:**
  - products ✓ condition inspections, electronic bills of lading;
  - customers ✓ dealers and auctions;
  - competitors ✓ marketplaces;
  - price ✓ per vehicle;
  - channels ✓ dedicated marketplaces.
  - **5 of 5**.
- **Source of the idea:** fringe (scan G #8); grid H11 × G09.

#### C-40 · Household moves
- **Sentence:** "Estimating, inventorying and settling claims on household moves, for households and relocating employees, handled today by small moving companies and moving brokers."
- **Who (G18):** households, and employers paying for relocations.
- **What (J2, J7):** "A fair estimate, my things arriving intact, and no surprise charges."
- **How:**
  - H12 movers: 9,083 firms (N-F01) and 8,207 active household-goods authorities (N-F03).
  - The regulator's 2023 crackdown found more than 1,000 violations (FMCSA "Operation Protect Your Move", N-G61, *assumed*).
- **Roles:** cost falls on households (claims, movers holding goods for extra charges) and on movers | decides: the household, or the employer's relocation manager | pays: the household or the employer | harder side: household side (*assumed*: one-time buyers).
- **End users:**
  - Mover: estimator or claims clerk.
  - Customer: the household.
- **Sub-market signs:**
  - products ✓ estimates and inventories;
  - customers ✓ consumers;
  - competitors ? not verified in the scan;
  - price ✓ estimate-based;
  - channels ✓ consumer lead generation.
  - **4 of 5**.
- **Source of the idea:** fringe (scan G #7); grid H12 × G18.

---

## 5. Sub-market signs and merges (S1 step 5)

### 5.1 The merge rule **[our call]**

Two rules decide whether cells or cards describe the same market:
1. **Same group and same job means one market, whatever the method.** R18 defines a market as "a group of people and the job they are trying to get done". So cells with the same shipper group and the same job are one market even if different freight-company types do the work. The different methods are then listed together on one card.
2. **Otherwise, stay separate only if at least two of R02's five signs differ.** If only the customer group differs, the two are segments of one sub-market, not two sub-markets. R01: "Sub-markets revolve around product categories, whereas market segments revolve around customer needs or behaviors". Such a pair merges, and the difference is kept as a segment option for Q6.

R02 itself sets no minimum number of signs. The "at least two" line is ours (proposal P-3).

### 5.2 Merge log

| # | Merged | Into | Why |
|---|---|---|---|
| M-1 | The general truckload and LTL freight of food, chemical, metal, distribution and furniture shippers (G01, G06, G08, G10, G12) | Column X cards: C-01, C-02, C-03, C-05 to C-11, C-14, C-17 | Only the customer group differs. The jobs, competitors, prices and channels are the same, so industry becomes a Q6 segment variable |
| M-2 | Reefer freight of food and beverage makers (G01 × H11) | C-01, C-03, C-09 | Only the product (the equipment) differs. Produce reefer stays separate as C-26, because its customers, competitors, prices and channels differ (PACA, Blue Book, seasonal spot rates) |
| M-3 | Dedicated contract carriage (H07) | C-15 | Same group and same job, planning and running a delivery fleet. Dedicated carriage is the outsourced method for it |
| M-4 | Expedited and hot-shot carriers | C-06 | Same job (finding spot loads), same channel (load boards). Scan G found no separate data |
| M-5 | Inland barge shippers | C-29 | Same group (elevators and grain merchandisers) and same job (buying transport capacity) |
| M-6 | The intermodal cell (H02 × X) | C-14 | Same group and same job (choosing the mode). Intermodal marketers are one method for it |
| M-7 | Meat processors' own fleets (G05 × H15) | C-15 | Same job; only the customer group differs |

### 5.3 Close neighbours checked and kept apart

| Pair | Signs that differ | Count |
|---|---|---|
| C-01 / C-14 | products (quotes and bids vs optimisation); competitors (procurement vendors vs managed-transportation 3PLs); price (broker spread vs gainshare) | 3 |
| C-01 / C-17 | customers (the shipping role vs the purchasing role); products (outbound bids vs routing guides); price (collect vs prepaid terms) | 3 |
| C-02 / C-07 | products (visibility vs broker TMS); customers (shippers vs brokers); competitors (visibility platforms vs broker TMSs) | 3 |
| C-03 / C-04 | customers (carriers vs warehouses); competitors (TMS and telematics features vs dock schedulers); price (per truck vs per facility) | 3 |
| C-05 / C-06 | products (payment vs load matching); competitors (factors vs load boards and dispatch services); price (% of invoice vs % of gross) | 3 |
| C-09 / C-11 | products (invoice audit vs class and density rating); competitors (audit-and-payment firms vs LTL 3PLs); price (contingency vs class tariffs) | 3 |
| C-09 / C-12 | products (freight-bill audit vs parcel refund claims); customers (mid-sized shippers vs e-commerce sellers); competitors (audit-and-payment firms vs parcel-audit firms) | 3 |
| C-15 / C-16 / C-38 | products (multi-stop routes vs boom trucks vs tank meters); customers (distributors vs building-material dealers vs fuel marketers); channels; competitors for C-38 (fuel-wholesale software) | ≥ 2 each |
| C-20 / C-24 | customers (importers vs exporters); products (import entries vs export certificates); competitors (customs-filing software vs forwarders) | 3 |
| C-21 / C-22 | customers (importers vs drayage carriers); products (invoice disputes vs appointments and chassis); price (per-day fees vs per-move rates) | 3 |
| C-25 / C-27 | products (bonded through-trailers vs perishable cold docks); customers (manufacturers vs produce distributors); channels (the Laredo vs Nogales clusters) | 3 |
| C-26 / C-27 | products (domestic reefer vs border hand-offs); competitors (produce brokers vs border brokers); channels | 3 |
| C-28 / C-29 | products (scale tickets vs rail and barge rights); customers (farms and elevators vs merchandisers); price (tariff-percentage quoting) | 3 |
| C-29 / C-30 | customers (elevators vs processors); products (buying capacity vs checking invoices); price (auction bids vs per-car-day charges) | 3 |
| C-31 / C-32 | products (live animals vs milk tankers with sampling); customers (ranchers vs dairy co-ops); competitors; price (per-hundredweight charges) | 4 |
| C-36 / C-37 | customers (road contractors vs mills and landowners); competitors (e-ticketing vendors vs forestry ticketing software); channels (state DOT mandates vs timber networks) | 3 |

### 5.4 How many signs each card shows

- **5 of 5 (14 cards):** C-05, C-06, C-07, C-20, C-25, C-26, C-27, C-29, C-32, C-34, C-36, C-37, C-38, C-39.
- **4 of 5 (17 cards):** C-01, C-03, C-04, C-09, C-10, C-11, C-12, C-13, C-14, C-19, C-21, C-22, C-23, C-28, C-30, C-31, C-40.
- **3 of 5 (9 cards):** C-02, C-08, C-15, C-16, C-17, C-18, C-24, C-33, C-35.

A "?" means the desk scans did not find evidence, not that the sign is absent. Most are "channels", or competitors not researched in S1. Several ✓ marks rest on vendor pages (*assumed*). S3 and S5 fill these in.

### 5.5 Reserve niches: listed, not carded

These are not rejected. They were held back because the 40-card cap **[our call]** was reached. The ones held were those that overlap an existing card or had the thinnest US evidence in scan G. S2 can pull any of them in if too few cards survive (§10's "long-list length" knob), or the founders can raise the cap (proposal P-4).

| # | Niche | Evidence found | Why held |
|---|---|---|---|
| R-1 | Scrap and recycling shipments (G19) | Grades and weights, bin tracking, export bookings. One firm's rail demurrage rose from $1,500-2,700 a month (2015-17) to over $23,000 a month (Q1 2019) (N-G34). Vendors ReSpark and cieTrade (N-G65) | Its best-documented cost, rail demurrage, sits in C-30, and its export leg in C-23/C-24 |
| R-2 | Trade-show freight | Show-site "drayage" billed at $60-200 per hundredweight round trip (N-G70, *assumed*) | No US volume or firm count; trade and vendor sources only |
| R-3 | Fine-art shipping | A market-research estimate of about $3.35B worldwide (N-G71, *assumed*) | No US data |
| R-4 | Returns and reverse logistics | Retail returns of $890B in 2024, 16.9% of sales (N-G72, *verified*) | No freight-specific data; the job is mostly retail operations |
| R-5 | Pharma cold chain (G17 × H11/H14) | About $35B a year lost to cold-chain failures (IQVIA, 2019, via N-G73, *assumed*) | One secondary estimate only; many vendors already named (Tive, Sensitech) |

---

## 6. Gate check and coverage

**The S1 gate: "every card fits the sentence, and no two cards describe the same market" (`submarket_selection.md` §4 S1).**

| Test | Result | How it was checked |
|---|---|---|
| Every card fits the standard sentence | **Pass** | Each card opens with one sentence in the form "[job], for [group], handled today by [method]" |
| No two cards describe the same market | **Pass** | The merge rule (§5.1) was applied, giving 7 merges (§5.2). The 16 closest pairs were checked, and each differs on at least two signs, most on three (§5.3) |
| 20-40 cards | **Pass** | 40 cards, plus 5 reserve niches |
| A human end user named on each side (R16) | **Pass** | Every card has an "End users" line naming a role |
| The four roles recorded | **Pass** | On every card. "Harder side" is *assumed* |

**Which cards cover each job:**

| Job | Cards | Count |
|---|---|---|
| J1 Buy capacity and rates | C-01, C-06, C-17, C-23, C-26, C-29 | 6 |
| J2 Tender, book and schedule | C-04, C-07, C-11, C-13, C-15, C-16, C-17, C-22, C-25, C-27, C-28, C-31, C-33, C-39, C-40 | 15 |
| J3 Track and report status | C-02, C-07 | 2 |
| J4 Documents and compliance | C-08, C-20, C-23, C-24, C-25, C-27, C-28, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38 | 15 |
| J5 Audit, pay and reconcile | C-05, C-07, C-09, C-12, C-18, C-28, C-32, C-36, C-37, C-38 | 10 |
| J6 Detention, demurrage and extra charges | C-03, C-11, C-19, C-21, C-22, C-29, C-30 | 7 |
| J7 Claims and disputes | C-08, C-10, C-13, C-19, C-26, C-39, C-40 | 7 |
| J8 Plan and consolidate | C-14, C-15, C-16 | 3 |

**Balance of the list:**
- **Farm-origin freight** has 8 of 40 cards (C-26 to C-33). The process doc says it is "one family of candidates, not the default" (§8.4).
- **Supply-side cards,** where the job is mainly the freight company's (C-05, C-06, C-07, C-08, C-22), sit next to shipper-side cards. The entry side stays open until Q6 (F-5).

---

## 7. Notes for S2, deferred items and proposals

### 7.1 Facts S2 will run into (recorded here, not judged)

- **Concentrated freight-company sides.** Under C11, a card leaves at S2 only if both sides fail a side-specific knock-out.
  - C-11: LTL, with a top-50 share of 82.9%. K10 is unknown at S2 and is settled at S3 by the small-firm check (C9).
  - C-12: couriers, 90.9%.
  - C-29, C-30: Class I railroads. Rail is not in the Economic Census, so K10 needs another source (N-F13).
  - C-21: ocean carriers.
- **Key figures that come only from vendor pages:**
  - C-11: LTL correction rates;
  - C-12: parcel recovery rates;
  - C-18: warehouse pricing;
  - C-19: deduction rates;
  - C-36: e-ticketing coverage.
  K4 asks for "named data", so these need better sources at S2/S3.
- **Units a fee could be counted on, with downturn data already held** (for K11 Test 3):

  | Unit | Card | Downturn data |
  |---|---|---|
  | Freight invoices | C-09 | Cass invoice counts fell 2.3% in 2023 (N-C15) |
  | Customs entries | C-20 | Customs brokerage revenue fell 20.5% (N-C13) |
  | Detained stops | C-03 | N-C24 |
  | Container demurrage and detention charges | C-21 | The FMC's series (N-F31) |

- **Savings that are mostly risk avoided** rather than money recovered: C-08 (fraud), and parts of C-20 and C-35. §7 of the process doc calls such savings hard to count and credit (K7).
- **Rules that fix invoice contents or claim deadlines** apply to:
  - C-10: the 30- and 120-day claim rules (N-F35);
  - C-21: the FMC's 2024 billing rule (N-F32);
  - C-26: PACA's payment terms (N-G13);
  - C-30: the STB's 2021 invoice rule (N-G33).

### 7.2 Still deferred (unchanged, `0_criteria.md` §6)

The following stay deferred to segment selection (Q6):
- the entry side (F-5);
- the firm-size floor (F-6);
- the fee per customer (F-7);
- the fee share of savings (F-8);
- whether our revenue swings with freight volume (O-3).

The "harder side" on each card is a desk guess made to fill the template. It does not choose the entry side.

### 7.3 Proposed process changes: not applied

These follow the decision-record rule: nothing here changes `submarket_selection.md` until the founders sign it off. After sign-off, each would be logged in §9.

| # | Proposal | Reason |
|---|---|---|
| P-1 | Add J8, "plan and consolidate shipments", to the S1 starter job list (§4 S1 step 1) | R33's managed-transportation definition ("transportation planning, carrier selection, tendering, and routing") and the private-fleet data (N-F19, N-F20) show a job that J1-J7 do not cover. Three cards use it |
| P-2 | Add H17, "job-specific service firms" (audit, factoring, dispatch, claims, permits), to the How axis | Several jobs are done today by fee-charging service firms that are not freight-company types. Neither R33 nor R44 has a row for them. Six cards use it |
| P-3 | Write the merge rule (§5.1) into S1 step 5, and reuse it at Q6 | R02 lists the five signs but not how many must differ. Without a rule, merges are unrepeatable |
| P-4 | Long-list cap: keep 40 and carry the reserve list, or raise it to 45 and card R-1 to R-5 | 45 distinct candidates turned up, and R15 asks for "as long a list as possible". §10 says to change the knob if too few distinct problems turn up in S5 |

### 7.4 Data gaps found in S1 (for S3)

- Shippers' technology habits by size: only a vendor-relayed Gartner estimate exists (N-E20), and it conflicts with two vendor surveys (N-F28, N-F29).
- The share of freight on "collect" terms, where the receiver arranges transport (N-E31).
- How often LTL invoices are corrected: vendor claims only (N-G24).
- Firm counts for factoring, dispatch, claims, permit and filing services; intermodal marketing companies; transfer carriers; milk haulers (N-F, N-G).
- Armstrong & Associates' sub-segment sizes (paywalled, N-F16).
- Produce rejection rates; national oversize/overweight permit totals (N-G).
- Software for rail demurrage, tank-wash certificates, cut-flower clearance, building-material job-site delivery and inbound freight control. Each was not found or not researched (§2).

---

## 8. Sources

**How this stage was run (2026-09-14).**
- Three web-research agents each gathered the evidence for one S1 step: the shipper axis (scan E), the freight-company axis (scan F), and the chain walks, investor maps and fringe (scan G).
- Each scan labels every figure *verified* or *assumed* and lists what it could not access.
- The coordinator built the axes, grid, cards and checks from those scans and from the existing notes.
- Unlike the S0 checks, no load-bearing figure was re-fetched by the coordinator at S1. Card figures are only used to describe candidates, and S3 re-checks any figure it relies on.
- Two of the three scans queried FMCSA's carrier file themselves, with different filters (§1.3).

**Existing sources used:**
- Resource notes: R01, R02, R05, R06, R08, R15, R16, R18, R22, R26-R34, R38, R39, R44.
- S0 checks: N-A25, N-A26, N-B04, N-B24 to N-B28, N-C13, N-C15, N-C23, N-C24, N-D30, N-D31, N-D34, N-D35. Their full entries are in `submarket_selection.md` §14 and the S0 check files.

**New sources, by scan.** The full entries, with URL, date, what was read and the source type, are in each scan's source list:

| Scan | IDs | File |
|---|---|---|
| E: shipper side (Who) | N-E01 to N-E32 | `research/s1_scan_E_shipper_side.md` §5 |
| F: freight-company side (How) | N-F01 to N-F77 | `research/s1_scan_F_freight_company_side.md` §7 |
| G: chain walks, investor maps, fringe | N-G01 to N-G78 | `research/s1_scan_G_outside_grid.md` §6 |

**The most load-bearing new sources:**

| ID | Source | Used for |
|---|---|---|
| N-E01 to N-E07 | Census, 2022 Commodity Flow Survey tables (mode, industry, commodity, temperature control, hazmat), www2.census.gov/programs-surveys/cfs/data/2022/ | Who axis; mode shares on most cards |
| N-E09 | BTS/FHWA/ORNL, FAF5.7.1 2018-2024 data (faf.ornl.gov) | Farm-origin and import flows |
| N-E10 | USDA AMS, *Transportation of U.S. Grains: A Modal Share Analysis, 1984-2022* (Sept 2024) | C-28, C-29 |
| N-E11, N-E13, N-E14, N-E16 | USDA: 2022 Census of Agriculture; Grain Stocks (Jan 2025); PACA; Packers and Stockyards report | Farm-origin groups |
| N-E17 | Census, Statistics of US Businesses 2022 | Firm counts and size mix on both sides |
| N-E18 | Census, *A Profile of U.S. Importing and Exporting Companies, 2023-2024* | C-20 to C-25 |
| N-F02, N-G49 | FMCSA Company Census File (data.transportation.gov az4n-8mr2), queried 2026-09-14 | Carrier counts, fleet sizes, cargo types |
| N-F03 | FMCSA licensing and insurance file (6eyk-hxee), frozen 2026-05-14 | Broker, forwarder and household-goods authorities |
| N-F05 | FMC, FY2024 Annual Report | Ocean intermediary counts |
| N-F10, N-F11 | CBP, ABI software vendor list (July 2025); March 2025 monthly update | C-20 |
| N-F22 | BLS, Occupational Employment and Wage Statistics, May 2025 | End-user roles |
| N-F30 | US DOT Inspector General, driver detention report (2018) | C-03 |
| N-F31, N-F32, N-G01 to N-G03 | FMC demurrage and detention data page, final rule notice, and NPRM | C-21 |
| N-F34, N-G33 | Supply Chain Dive on record rail demurrage (2022); STB final rule on demurrage invoices (EP 759, 2021) | C-30 |
| N-G12 | Blue Book, "Reefer Carriers and PACA" (2025) | C-26 |
| N-G14 | USDA AMS, Section 8e import inspection fee rule (2024) | C-26, C-27 |
| N-G20, N-G21 | NMFTA on NMFC Docket 2025-1 (the 2025 density-based class change) | C-11 |
| N-G22 | Old Dominion Freight Line, 10-K for FY2024 | C-11 |
| N-G25 | USDA AMS, downbound grain barge rates dataset | C-29 |
| N-G43, N-G44 | FTV Capital on Highway (2025); a16z-led HappyRobot release (2024) | Investor categories; C-07, C-08 |
| N-G55 | WSDOT Gray Notebook, oversize/overweight permits | C-34 |
| N-G68 | CBP, cut-flower inspections release (Feb 2026) | C-33 |

**Access problems.** Each scan lists what it could not reach (scan E §4, scan F §6, scan G §5). Among them:
- Federal Register and eCFR pages;
- several USDA AMS, FMCSA and BTS pages;
- Gartner and PitchBook reports;
- Walmart's supplier portal;
- the NTT DATA 3PL Study.

The scholarly-search server was not connected in this session and was not used.
