# S1 scan F — the How axis: freight-company types, who does each shipping job, and the human end users

Run 01, stage S1 "Enumerate candidates". Evidence only: no scoring, ranking, knock-outs or recommendations. Compiled 2026-09-14.

**Labels.** **[V]** = *verified*: read in the source, or computed by us from an official data download. **[A]** = *assumed*: taken from a search snippet or a secondary source, or inferred by us. **[our calc]** marks arithmetic we did; the inputs are shown. Facts the brief already supplied are cited by their existing IDs (R33, R44, N-B01, N-B04, N-B05, N-D30, N-D31). "Brief" means the detention-tool facts and vendor-deal facts given in the task.

---

## 1. Summary

- **Trucking is huge and mostly tiny firms.** On 2026-09-14 FMCSA listed 531,374 active interstate for-hire carriers **[V]**. Of those that report trucks, 91.9% run 10 or fewer and 56.6% run one **[our calc]**. In Census SUSB 2022, 88–94% of firms in every trucking code have fewer than 20 employees. Their share of receipts runs from 8% in LTL to 52% in local trucking **[V]**.
- **Intermediary licence counts:**
  - FMCSA broker authorities: 25,081 active (May 2026 snapshot).
  - FMCSA freight-forwarder dockets: 1,887 active.
  - FMC-regulated ocean intermediaries: over 9,100, of which about 8,600 are NVOCCs.
  - Licensed customs brokers: about 14,500 individuals (secondary source).
  - CBP-listed customs-filing software vendors: about 70.
- **Private fleets:** 170,221 interstate "private-only" fleets report 2.2M power units. That is about a quarter of the interstate power units reported by for-hire plus private-only fleets (self-reported) **[our calc]**.
- **How the shipping jobs get done:** Small shippers, carriers and brokers mostly do buying, booking, tracking, paperwork and billing through in-house generalists: logistics coordinator, dispatcher, billing clerk, track-and-trace rep. They use email, phone, load boards and portals.
- **How outside service firms charge:**
  - % of gross: dispatch services, 5–10%.
  - % of invoice: factoring, 1–5%.
  - Contingency: parcel audit, 25–50% of what they recover.
  - Per item: oversize/overweight permits, $50–150 each; IFTA filing, about $85 per quarter.
- **Charges that regulators have measured:**
  - Ocean container demurrage and detention: about $15.4B, April 2020 to March 2025.
  - Class I rail demurrage: $1.18B in the first nine months of 2021.
  - Truck detention: $1.1–1.3B a year of lost driver earnings (2018 estimate).
- **BLS May 2025:**
  - 97,670 cargo and freight agents, 55% of them at brokers and forwarders.
  - 202,810 dispatchers.
  - 816,870 shipping, receiving and inventory clerks.
- **Biggest gaps:**
  - Armstrong's sub-segment sizes.
  - Counts of dispatch, factoring, claims, permit and IFTA service firms.
  - The NVOCC vs forwarder split.
  - Credible software-adoption data for small carriers.

---

## 2. How to read the counts (caveats)

- **FMCSA "active" means an active registration, not a truck on the road.** Status code A in the Company Census File (N-F02) covers any registration not deactivated. Fleet data comes from carriers' own biennial MCS-150 update forms and can be stale. One firm can hold several USDOT numbers. **[A]**
- **An operating authority (the "MC" or "FF" docket number) is a licence, not a firm.** One firm can hold several. The L&I dataset (N-F03) was frozen on 2026-05-14 when FMCSA moved to its new Motus registration system. The Motus feed (N-F04) is a daily list of changes only, so it cannot give totals. **[V]**
- **SUSB vs Economic Census.** SUSB (N-F01) and the Economic Census (R44) count firms differently. For long-distance truckload, SUSB has 55,905 firms and the Census has 53,705. For freight arrangement, SUSB has 15,852 and the Census has 17,130. R44 is used wherever it exists; SUSB fills the gaps and gives the size mix. **[V]**
- **SUSB size classes are for the whole company.** A firm is classed by the employee count of its entire enterprise, across all its industries. So a small warehouse belonging to a large company counts as "500+ employees". **[A: SUSB methodology]**
- **FMCSA cargo checkboxes** say what a carrier *hauls*, not what equipment it uses, and a carrier can tick several. In this dataset "meat" always equals "refrigerated food", and "construction" always equals "building materials". We found zero records where one flag of either pair was set without the other, which looks like a data quirk. **[V, our query]**
- **Rail (NAICS 482) is outside Census SUSB and Economic Census coverage.** 482111 is missing from the SUSB file **[V, our check]**.

---

## 3. Table: Freight-company types and methods

"PU" = power unit, i.e. a truck or tractor. "Top-50 share" is from R44.

| Method | Plain definition | Codes | Counts (firms or licences, year, source) | Size mix | How they are paid | Notes |
|---|---|---|---|---|---|---|
| **All for-hire trucking (registry view)** | Companies with interstate authority to haul other people's freight for pay | FMCSA USDOT registration; MC authority | 531,374 active interstate for-hire carriers, 2026-09-14 (N-F02) **[V our query]**. 353,672 active MC property-carrier authorities, 2026-05-14 (N-F03) **[V]**. About 580,000 active carriers (N-B05) **[A]**. 914,821 nonemployer trucking businesses (NES 2022, brief). | By PU: 1 PU = 274,660; 2–10 = 171,745; 11–100 = 35,411; 101–1,000 = 3,433; over 1,000 = 294; 0 or blank = 45,831 **[V]**. So ≤10 PU = 446,405 / 485,543 = 91.9%, and 1 PU = 56.6% **[our calc]**. ATA gives 91.5% (N-B01). | Rate per load or per mile, fuel surcharge and extra-service fees (accessorials), invoiced to a shipper or broker **[A]** | The for-hire carriers report 6.84M PUs in total (N-F02) **[V; self-reported]**. |
| **Truckload (TL)** | One shipper's goods fill a trailer that goes direct from A to B | NAICS 484121 | Econ. Census 2022: 53,705 firms, $172.7B (R44). SUSB 2022: 55,905 firms, $172.9B (N-F01) **[V]** | 94% of firms have <20 employees and earn 24% of receipts. 326 firms in 500+ enterprises earn 46% **[V; our calc]** | As above. Small carriers often sell invoices to factors (see below) | Top-50 share 37.4% |
| **LTL (less-than-truckload)** | Many shippers' small shipments (pallets) share trailers and move through a terminal network | 484122 | EC: 7,675 firms, $65.7B (R44). SUSB: 7,204 firms, $66.4B **[V]** | 93% of firms have <20 employees but earn only 8%. 78 firms in 500+ enterprises earn 82% **[V; our calc]** | Priced per shipment by freight class, weight and lane, minus discounts, plus accessorials such as liftgate, residential and reweigh/reclass **[A]** | Top-50 share 82.9% |
| **Local general freight** | Short-haul trucking within a metro area or region | 484110 | EC: 43,243 firms, $54.7B (R44). SUSB: 43,571 firms, $61.4B **[V]** | 93% <20 employees, earning 52%. 174 firms in 500+ enterprises earn 11% **[V; our calc]** | Per load, hour or day **[A]** | Top-50 share 10.5% |
| **Household-goods movers** | Move household and office contents | 484210 | SUSB: 9,083 firms, $20.1B **[V]**. FRED/Service Annual Survey 2022 revenue $22.0B (N-F66) **[A]**. 8,207 active household-goods carrier authorities, 2026-05-14 (N-F03) **[V]** | 85% <20 employees, earning 26%. 29 firms in 500+ enterprises earn 24% **[V; our calc]** | Consumer or corporate move pricing, by weight/volume and distance **[A]** | 53,816 interstate for-hire carriers tick "household goods" (N-F02) **[V]** |
| **Specialized freight** (local and long-distance) | Trucks built for particular cargo: refrigerated ("reefer"), flatbed, tank, dump, auto, livestock, logs, heavy haul | 484220 local; 484230 long-distance | EC: 31,927 firms, $57.5B; 10,701 firms, $52.6B (R44). SUSB: 31,583 firms, $79.4B; 10,292 firms, $51.2B **[V]** | 484220: 92% <20 employees, earning 34%. 484230: 88% <20, earning 18% **[V; our calc]** | As TL; heavy haul also pays for permits and escorts **[A]** | No official split by trailer type found. See the FMCSA cargo table below. NTTC (tank carriers) says it has "over 200" member companies hauling more than 80% of tank volume (N-F67) **[A]** |
| **Rail: Class I** | The largest line-haul railroads | NAICS 482111; STB Class I (revenue floor $900M in 2019 dollars, inflation-adjusted; N-F76 **[A]**) | 6 Class I railroads (AAR, 2025; N-F13) **[V]** | Class I have about 67% of rail mileage, 87% of employees and 89% of revenue (N-F13) **[V]** | Tariff or contract rate per car or container, plus demurrage (charges for holding cars too long) and other accessorials (N-F33) | Not covered by Census firm counts |
| **Rail: short line and regional (Class II/III)** | Small railroads doing first- and last-mile rail | 482111/482112 | 603 short lines (ASLRRA; N-F12) or about 615 (AAR; N-F13) **[V]** | 47,500 route miles (29% of US freight rail), 17,800 employees, about 10,000 customers, 1 in 5 carloads (N-F12) **[V]** | As above | — |
| **Inland water / barge** | Barge and towboat freight on rivers and inland waterways | 483211 | SUSB 2022: 339 firms, $7.65B **[V]** | 78% <20 employees. 20 firms in 500+ enterprises earn 70% **[V; our calc]** | Per ton or per barge, under contract **[A]** | — |
| **Air freight (scheduled freight airlines)** | All-cargo scheduled airlines | 481112 | SUSB 2022: 211 firms, $6.78B **[V]** | 72% <20 employees. 10 firms in 500+ enterprises earn 48% **[V; our calc]** | Per kg of chargeable weight **[A]** | Express integrators sit in couriers, 4921: 6,553 firms, $132.3B, top-50 share 90.9% (R44) |
| **Freight brokers** | Arrange trucking for shippers without owning trucks. They hire a carrier and keep the difference ("spread") | FMCSA broker authority (MC docket); NAICS 488510, shared with forwarders | 25,081 active broker authorities, 2026-05-14 (N-F03), 24,970 of them with a bond on file **[V our query]**. About 25,000 (N-B04, 2025). Brush Pass: 25,087 active in April 2025 (N-B04) **[A snippet]**. 488510: EC 17,130 firms, $134.9B (R44); SUSB 15,852 firms, $129.2B **[V]** | 488510: 87% of firms <20 employees, earning 24%. 261 firms in 500+ enterprises earn 38% **[V; our calc]** | Spread between the shipper price and the carrier cost. Armstrong DTM 2025 net revenue $19.6B on gross $128.3B = 15.3% **[our calc; A secondary, N-F17]** | 2,239 active brokers also hold active carrier authority (N-F03) **[V]**. New FMCSA broker and forwarder financial-responsibility rule effective 2026-01-16 (N-F65) **[A]** |
| **Freight forwarders (domestic, FMCSA)** | Collect and consolidate shipments and take carrier-style liability, while other carriers do the line-haul | FMCSA FF docket; 488510 | 1,887 FF dockets with an active status, 2026-05-14: 1,674 property, 365 household goods (N-F03) **[V our query]** | Not found | Per shipment **[A]** | In this dataset, forwarder status sits in the "contract" field (our observation) **[A]** |
| **Ocean transportation intermediaries (OTIs)**: NVOCCs and ocean freight forwarders (OFFs) | NVOCC: sells ocean shipping under its own bill of lading but runs no ships. OFF: books ocean space and prepares export papers for the shipper (N-F06) **[V]** | FMC OTI licence or registration; 488510 | "Over 9,100" OTIs regulated. "Approximately 8,600 NVOCCs with tariff locations published" at end FY2024. About 645 revocation or termination actions in FY2024 (N-F05) **[V]** | Not found | NVOCC: buys ocean space and resells it with a markup. OFF: forwarding fees **[A]** | NVOCC vs OFF split not found |
| **Customs brokers** | Licensed by CBP to do "customs business" (import entries, duty) for importers (N-F07) | CBP individual licence plus a national permit for the firm (19 CFR 111) | About 14,454 "active licensed customs brokers" (individuals), and "~15,000" on another slide (training-provider slides, 2024; N-F09) **[A]**. Firm and permit count not found. More than 3 million entry summaries in March 2025 (N-F11) **[V]**, roughly 36M a year if steady **[our calc; A]** | Not found | Per-entry and service fees to importers; amounts not verified **[A]** | District permits were abolished and all brokers moved to one national permit on 2022-12-19 (N-F08) **[V]**. 2026 permit fee is $185.38 (N-F07) **[V]** |
| **Intermodal marketing companies (IMCs)** | Buy rail container space from railroads and truck drayage from local carriers, and sell a door-to-door move under one bill | None of its own (488510) | IMC count not found. IANA: total intermodal volume in 2025 was 18.5M containers and trailers, +2.3% (N-F14) **[V]**. IANA IMC members' loads in Q2 2025: 286,642, −8.2% (N-F15) **[A snippet]** | Not found | Margin **[A]** | Armstrong's "intermodal" DTM sub-segment size is not free (R33) |
| **Managed-transportation 3PLs** | Run a shipper's transportation (buying, tendering, auditing) as an outsourced department | Armstrong DTM sub-segment | Size not free | Not found | "A flat amount per shipment or a percent of the purchased transportation ... may include gainshares" (R33) | — |
| **Final-mile carriers** | The last leg to a home or business (parcel, big-and-bulky) | 492210 local messengers and local delivery; 4921 couriers | 492210 SUSB: 4,827 firms, $20.0B **[V]**. Amazon: DSP program has "4,400 entrepreneurs", "390,000 driving jobs", ">20 million packages every day", 19 countries (N-F45; company claim, undated, global) **[V as claim]** | 492210: 67% <20 employees, earning 12%. 35 firms in 500+ enterprises earn 55% **[V; our calc]** | Per stop or package **[A]** | Armstrong's last-mile sub-segment size is not free |
| **Dedicated contract carriage (DCC)** | A carrier supplies trucks and drivers dedicated to one shipper under a multi-year contract **[A]** | Armstrong segment | Armstrong 2025: $32.0B gross (R33). 2024: $31.5B (N-F18) **[A secondary]** | Not found | Contract pay model not documented in sources read | Armstrong reports net = gross = $32.0B for 2025 (N-F17) **[A]** |
| **Warehousing: general / refrigerated / farm products** | Store and handle goods. Public warehouses serve many customers on pay-as-you-go terms; contract warehouses serve a client under a longer, custom contract (N-F64) **[A]** | 493110 / 493120 / 493130 | SUSB 2022: 6,789 firms, $54.7B; 680 firms, $7.4B; 542 firms, $1.2B **[V]**. EC 493 overall: 9,473 firms, $60.3B, top-50 share 48.2%. 49312 top-50 share 73.9%; 49313: 411 firms, $1.0B (R44) | 493110: 53% <20 employees, earning 9%; 1,098 firms in 500+ enterprises earn 64%. 493120: 55% <20; 62 firms earn 59%. 493130: 73% <20, earning 41% **[V; our calc]** | Public: storage per pallet per month plus handling, e.g. $12–25/pallet/month ambient and $25–50 cold (N-F64) **[A]**. Contract: scale- and time-based fees **[A]** | Armstrong value-added warehousing 2025: $72.7B gross, $56.1B net (R33, N-F17) |
| **Port drayage carriers** | Short truck moves of containers between ports or rail ramps and nearby warehouses | Filed under 4841xx; no code of their own **[A]** | Ports of LA/Long Beach drayage truck registry: "23,000+ trucks" (May 2024; N-F21) **[V]**. 48,991 interstate for-hire carriers tick "intermodal containers" (N-F02) **[V]** | Count of licensed motor carriers at the ports not found | Per move plus chassis, waiting and storage charges **[A]** | LA concession agreements run Oct 2021 to Sep 2026 (N-F77) **[A]** |
| **Truck dispatch services** | Outside firms that find, negotiate and book loads for owner-operators | None | Count not found | Serve 1–10-truck carriers **[A]** | "5% to 10%" of gross, "7% most common"; or $50–150 per load; or $500–1,500 per truck per month (N-F39, vendor claim) **[V as claim]** | — |
| **Freight factoring companies** | Buy a carrier's unpaid invoices at a discount for immediate cash. "Recourse" means the carrier bears the loss if the payer defaults | None (finance) | Count not found. Triumph factoring: $1.149B net funds employed at 2025-12-31 (N-F44) **[V]** | Triumph serves 1–4-truck, 5–50-truck and 50+-truck fleets (N-F44 snippet) **[A]** | "1% to 4% per invoice" (N-F40, vendor, 2022) **[V as claim]**. 1–5%, with recourse cheaper than non-recourse (snippets) **[A]**. A reserve is held back, e.g. 5% (N-F40) | TriumphPay connects brokers, shippers, factors and carriers to present, audit and pay invoices (N-F44) **[A]** |
| **Freight audit and payment (FAP) providers** | Check carrier invoices against contracts and pay carriers on the shipper's behalf | None | Cass: $36.4B across 34.5M invoices in 2025 (N-D30). U.S. Bank: about $46B (N-D31). A Gartner market guide names about 15 providers (N-F50) **[A]**. Total count not found | "A few primary competitors and numerous small ... audit firms" (N-D30) | Per-invoice fee, % of spend, gainshare (30–50% of recoveries), or subscription (N-F51, vendor) **[A]** | — |
| **Freight claims services** | File and chase cargo loss or damage claims for shippers | None | Count not found | Not found | Contingency, e.g. "if we don't win, you don't pay" (N-F56, vendor) **[A]**. Percentage not found | Rules: a carrier may not allow less than 9 months to file or less than 2 years to sue (N-F36); it must acknowledge within 30 days and pay, decline or offer within 120 days (N-F35) **[V]** |
| **Oversize/overweight (OS/OW) permit services** | Obtain state permits for oversized or heavy loads | None | Count not found | Not found | Per permit, on top of state fees: $72.50 oversize, $82.50 overweight, $50.50 trip/fuel, $90.50 "superload" (extra-large load), $150 for superloads over 250,000 lb (N-F42, vendor, effective 2026-01-01) **[V as claim]** | 87,293 carriers tick "machinery, large objects" (N-F02), a heavy-haul proxy **[V]** |
| **IFTA/IRP/UCR filing services** | File the quarterly fuel-tax return split across states (IFTA), apportioned plates (IRP) and the annual federal registration fee (UCR) | None | Count not found | Not found | IFTA "$85 per quarter" for 1 truck plus "$25" per extra truck. UCR "$45 filing fee" plus the UCR fee. Form 2290 "$45–$65" (N-F43, vendor) **[V as claim]**. $30–100 per quarter typical (N-F68) **[A]** | — |
| **Private fleets** (in-house trucking) | Shippers (manufacturers, distributors, retailers) running their own trucks for their own goods | FMCSA "private property" class | Private-only (no for-hire class), active interstate: 170,221 (2026-09-14). 236,048 including those also for-hire. All operations incl. intrastate: 1,002,076, of which 807,829 private-only (N-F02) **[V our query]**. "940,280 private fleets ... 47% of the truck market" (N-F19 search snippet; not on the NPTC pages we read) **[A]** | Interstate private-only by PU: 1 = 53,658; 2–10 = 91,693; 11–100 = 20,713; 101–1,000 = 2,048; over 1,000 = 157. ≤10 PU = 86.4% **[our calc]** | Run as a cost centre by 77% of NPTC survey respondents (N-F20) **[V]** | Private-only fleets report 2.22M PUs vs 6.84M for interstate for-hire, so about 24.5% of the combined total **[our calc; self-reported; the 65,827 fleets with both classes are counted as for-hire]**. NPTC's 104 surveyed companies move 70.4% of their outbound and 43% of their inbound shipments in their own fleets (N-F19) **[V]** |
| **"Spreadsheet and phone"** | Doing a job by email, phone, spreadsheet or paper, without dedicated software | — | Descartes/SAPIO 2025 survey of 616 shippers and logistics providers (US, Canada, Western Europe): "only 17% ... fully automated"; "over one-third heavily or mostly reliant on manual processes" (N-F28) **[V; vendor survey]**. "About seven out of 10 shippers use a TMS" (transportation management system); non-users ship mainly parcel and some LTL (a freight-audit firm's CEO, N-F29) **[A]**. Micro-cap brokers: 13% use a homegrown TMS (N-B04) | — | — | No credible survey found on small carriers' software use |

### FMCSA cargo checkboxes: active interstate for-hire carriers, 2026-09-14 (N-F02, our queries) [V]

These count carriers, not trucks, and each carrier can tick several boxes. They are proxies for the specialized sub-types; no official split by equipment type was found.

| Proxy for | Checkbox(es) | Carriers |
|---|---|---|
| Plain dry freight | General freight | 457,813. Of these, 207,020 ticked general freight and none of 13 specialized boxes |
| Reefer | Refrigerated food, meat, or fresh produce (union) | 105,756 (refrigerated food alone: 88,708; produce: 88,596) |
| Flatbed | Building materials; metal sheets/coils; machinery and large objects | 136,759; 83,816; 87,293 (the last is also the heavy-haul proxy) |
| Tank / bulk | Liquids/gases or chemicals (union); dry bulk | 31,590; 77,488 |
| Dump / aggregates | Building materials / construction (duplicate flags); dry bulk | See above. No distinct dump checkbox |
| Auto carriers | Motor vehicles; driveaway/towaway | 76,367; 33,098 |
| Livestock haulers | Livestock | 25,365 (23,779, or 93.7%, with 0–10 PU **[our calc]**) |
| Logging | Logs, poles, beams, lumber | 81,349 (73,612, or 90.5%, with 0–10 PU **[our calc]**) |
| Farm | Grain, feed, hay; farm supplies | 80,155; 65,680 |
| Drayage | Intermodal containers | 48,991 |
| Other | Oilfield equipment; garbage; coal/coke; hazmat flag | 23,468; 24,953; 15,255; 55,545 |

---

## 4. Table: Job × who does it today

Terms, defined on first use:
- **Spot quote:** a one-off price for one load.
- **RFP:** request for proposal, a bid for a year of lanes.
- **Tender:** offering a load to a carrier.
- **Check call:** phoning for a status update.
- **BOL (bill of lading):** the shipping contract and receipt.
- **POD (proof of delivery):** the signed delivery receipt.
- **Accessorials:** extra-service charges.
- **Detention:** a truck held too long at a dock.
- **Demurrage:** a container or railcar kept past its free time.
- **OTIF:** "on-time, in-full", a retailer delivery standard.
- **OS&D:** over, short and damaged.

| Job | Small/mid shippers: who does it | Small carriers/brokers: who does it | Software categories and example vendors (count if known) | Service firms and how they charge | End-user roles |
|---|---|---|---|---|---|
| **(a) Buy capacity and rates** (spot quotes, contract RFPs) | An in-house logistics coordinator or traffic manager, or an operations or purchasing person doing it part-time. They phone or email brokers and carriers for spot quotes and use broker quote portals. Annual RFPs run on spreadsheets and email, or buying is handed to a broker or managed-transportation 3PL **[A]** | **Carrier:** the owner-operator or an in-house dispatcher, or an outside dispatch service, searches load boards, calls brokers and negotiates a rate per load **[A]**. **Broker:** carrier sales reps post loads and call carriers; customer sales reps quote shippers (N-F59 illustration) **[A]** | **Freight procurement / sourcing:** Transporeon, Keelvar, Emerge, GoodShip, Sleek Technologies, Freehand, GoComet (N-F46) **[A]**. **Load boards:** DAT (carrier plans $59–339/mo, broker plans $159–449/mo; "more than 291 million loads & trucks posted annually", N-F41, vendor) **[V as claim]**; Truckstop. **Instant-quote / digital brokerage:** Uber Freight (N-F46) **[A]**. Vendor count not found | **Brokers:** spread; DTM net/gross 15.3% **[our calc; A]**. **Managed transportation:** per shipment or % of purchased transport, plus gainshare (R33). **Dispatch services:** 5–10% of gross (N-F39) | Shipper logistics coordinator or traffic manager (13-1081, 11-3071); broker carrier sales and customer sales reps (43-5011); carrier dispatcher (43-5032); owner-operator |
| **(b) Tender, book, schedule**, incl. dock appointments | A shipping clerk or logistics coordinator tenders by email, phone, broker portal, or TMS/EDI (electronic data interchange). On the receiving side, a dock scheduler assigns time slots and doors to inbound trucks (N-F62 illustration) **[A]** | **Carrier:** the dispatcher accepts the tender, assigns driver and truck, and books pickup and delivery appointments by phone, email or portal **[A]**. **Broker:** the carrier sales or operations rep "sets appointments, dispatches, tracks" (N-F59 illustration) **[A]** | **TMS** (shipper, broker, carrier). **Dock-appointment scheduling:** Opendock, C3 Reservations, DataDocks, GoRamp, LoadingCalendar, Velostics, Conduit, Transporeon (N-F38, N-F47) **[A list]**. Opendock lets "carriers, brokers, and dispatchers ... book, update and cancel dock appointments with warehouses" (N-F69) **[A]**. Count not found | **Dock software, paid by the warehouse per facility** (vendor claims, N-F38) **[V as claims]**: Opendock "~$6,000–$7,000+/year per facility"; LoadingCalendar "$99/month flat"; GoRamp "from $175/month"; DataDocks "from ~$249/month"; Conduit "$149/facility/month"; Velostics "~$4,500+". "Only four show a number" | Shipping clerk (43-5071); warehouse dock scheduler (within 43-5071 / 43-5061 **[A mapping]**); dispatcher (43-5032); broker operations rep (43-5011) |
| **(c) Track and report status** ("check calls") | A logistics coordinator or customer service rep chases status by email and phone, or reads carrier and broker portals. Larger shippers buy visibility platforms **[A]** | **Broker:** "track and trace" reps make check calls. One posting cites "up to 100 per day" (N-F60 illustration) **[A]**. **Carrier:** the dispatcher updates brokers; drivers share location through apps or ELD links **[A]** | **Real-time transportation visibility platforms (RTTVP):** project44 and Shippeo were Leaders in Gartner's 2025 Magic Quadrant (N-F48); FourKites withdrew from it in Feb 2025 (N-F49); Descartes MacroPoint; Trucker Tools (N-F70) **[A]**. **Ocean container tracking:** Vizion, Terminal49, Portcast (N-F54) **[A]**. Gartner's vendor count is paywalled | Usually bundled into the broker's margin or 3PL fee **[A]** | Track-and-trace rep (43-5011); dispatcher (43-5032); truck driver (53-3032); shipper coordinator (13-1081) |
| **(d1) Bill of lading and proof of delivery** | A shipping clerk prepares the BOL. O*NET task: "prepare documents, such as ... bills of lading" (N-F26) **[V]**. A receiving clerk signs the POD and records "damages, or discrepancies" (N-F26) **[V]** | **Carrier:** the driver gets the POD signed; the billing clerk collects BOL, POD and rate confirmation to invoice (N-F63 illustration) **[A]**. **Broker:** needs the POD before paying the carrier **[A]** | **eBOL (electronic BOL):** NMFTA Digital LTL Council eBOL standard, 2022 (N-F57) **[A]**; SmartBOL, project44 eBOL, C.H. Robinson eBOL (N-F57) **[A]**. **Driver document scanning:** inside ELD/TMS apps **[A]**. Count not found | None found specific to BOL/POD | Shipping and receiving clerks (43-5071); driver; carrier billing clerk (43-3031 proxy) |
| **(d2) Customs entries** | An importer hires a customs broker, whose **entry writer** prepares entries (forms 7501 and 3461), classifies goods under the tariff schedule (HTS) and calculates duty "under the supervision of a licensed Customs Broker" (N-F61 illustration) **[A]**. Larger importers have trade-compliance staff **[A]** | Mostly n/a to truck carriers and brokers. Forwarders and NVOCCs coordinate with customs brokers **[A]** | **Filing software on CBP's list (the ABI interface):** about 70 companies on the July 16, 2025 list (N-F10) **[V; our count of entries]**. Includes Descartes brands (Editrade, IES, NetCHB, Questa Web, Visual Compliance), Magaya (ACELYNK), E2open, CustomsCity, KlearNow. Forwarder software: BoxTop sold for about $13M (brief) | Customs brokers charge importers per entry; amounts not verified **[A]**. Volume: more than 3M entry summaries in March 2025 (N-F11) **[V]** | Entry writer; licensed customs broker (O*NET 13-1041.08, within SOC 13-1041; N-F27) **[V]** |
| **(d3) Hazmat shipping papers** | The shipper (the "offeror") prepares them under 49 CFR 172 Subpart C and keeps copies (N-F58) **[A]** | The carrier's driver carries the papers. 55,545 interstate for-hire carriers flag hazmat (N-F02) **[V]** | Labelmaster DGIS, which validates against DOT 49 CFR, IATA and IMO rules, and ProShip integration (N-F58) **[A]**. Count not found | Not found | Shipping clerk or EHS/compliance staff **[A]**; driver |
| **(d4) Oversize/overweight permits** | Rarely the shipper **[A]** | The carrier's dispatcher or permit clerk orders permits state by state on state portals, or pays a permit service **[A]** | Permit-service portals: Highway Permits, OmniPermits, TruckPermity (N-F42, N-F73) **[A]** | Per permit plus state fee, e.g. $50.50–$150 (N-F42) **[V as claim]** | Carrier dispatcher or permit clerk (43-5032) |
| **(d5) IFTA / IRP / UCR filings** | n/a (private fleets do their own) **[A]** | The carrier's office or bookkeeper compiles miles by state (often from the ELD) and fuel receipts, then files; or a filing service does it **[A]** | Small-carrier TMS with IFTA reports: TruckingOffice (N-F74) **[A]**; ELD-based IFTA mileage **[A]** | IFTA $85 per quarter per truck, $25 per extra truck; UCR $45 filing fee (N-F43) **[V as claim]** | Carrier bookkeeper or safety/compliance manager (43-3031 / 13-1041 proxies) |
| **(e1) Audit, pay and reconcile freight bills: truckload / LTL** | An AP clerk and/or logistics coordinator matches each invoice to the BOL, POD and quoted rate, and disputes accessorials and reweigh/reclass charges **[A]**. Or the work goes to an FAP provider | **Carrier:** the billing clerk invoices with rate confirmation and BOL/POD; many carriers sell invoices to a factor (N-F63 illustration, N-F40) **[A]**. **Broker:** a carrier-payables (AP) team pays carriers **[A]** | **FAP:** Cass, U.S. Bank, Trax, nVision Global, CTSI-Global, Intelligent Audit, CT Logistics, Data2Logistics, RateLinx, TranzAct, enVista, Loop (N-F50, N-F51) **[A]**. **Payments network:** TriumphPay (N-F44). **Carrier accounting:** QuickBooks-type tools (N-F63) **[A]** | FAP: per invoice, % of spend, gainshare of 30–50%, or subscription **[A]**. Factoring: 1–4% per invoice (N-F40) **[V as claim]** | Shipper AP clerk (43-3031); carrier billing clerk (43-3031); broker carrier-payables clerk (43-3031) |
| **(e2) Audit, pay and reconcile: parcel** | Shipping or AP staff, or an outsourced parcel-audit firm that claims late-delivery refunds and billing errors from UPS and FedEx **[A]** | n/a | Refund Retriever, Intelligent Audit, TCR, RefundPros, Parcel Service Refund (N-F52, N-F53) **[A]** | Contingency of 25–50% of recovered credits (brief). One vendor splits refunds "50-50" (N-F53) **[A]**. Recoveries of "2% and 5%" of parcel spend (N-F52, vendor) **[A]** | Shipping clerk (43-5071); AP clerk (43-3031) |
| **(f1) Accessorials and truck detention** | Facility staff control loading time. AP or logistics reviews detention bills **[A]** | The carrier's dispatcher or billing clerk logs arrival and departure and bills detention to the broker or shipper; brokers pass it through **[A]** | Seven tools in one 2026 guide: TMSs (Trimble TMW, McLeod), Samsara, and ChargeGuard at $59–349/mo for 5–150-truck carriers. Vendor claim: manual processes capture "only around 40%" (brief) | DOT OIG (2018) **[V]**: detention is "associated with reductions in annual earnings of $1.1 billion to $1.3 billion" for for-hire drivers and cuts carrier net income by $250.6–302.9M a year; a 15-minute rise in dwell time raises expected crash rates 6.2% (N-F30) | Dispatcher (43-5032); billing clerk (43-3031); shipper dock and receiving staff (43-5071) |
| **(f2) Ocean container demurrage and detention (D&D)** | The importer's logistics coordinator, forwarder/NVOCC or customs broker watches free time and disputes invoices **[A]** | Drayage carriers return containers and may be billed **[A]** | D&D management and container visibility: BuyCo, GoComet, Portcast, Vizion, Terminal49, BlueCargo, Windward, TradeTech (N-F54) **[A]** | Charges measured **[V]**: nine carriers, "roughly $15.4 billion in D&D charges between April 1, 2020, and March 31, 2025" (N-F31). FMC billing rule, mostly effective 2024-05-28: invoice within 30 days; at least 30 days to dispute; carrier tries to resolve within 30 days; only one party may be billed; a missing required field "eliminates any obligation ... to pay" (N-F32) | Importer logistics coordinator (13-1081); forwarder operations (43-5011); entry writer |
| **(f3) Rail demurrage** | A rail or traffic manager at the plant tracks car-days and disputes charges **[A]** | n/a | None identified in the sources read (gap) | "The seven Class I railroads ... collected $1.18 billion ... from demurrage fees during the first three quarters of 2021", +33% from 2020 to 2021 (N-F34, trade press) **[V]**. STB holds quarterly railroad reports for 2018 to Q1 2022 (N-F33) **[V]** | Shipper traffic manager (11-3071 / 13-1081) |
| **(f4) Retailer OTIF chargebacks** | The supplier's logistics or compliance manager and an accounts-receivable deductions analyst dispute them **[A]** | Carriers and brokers supply delivery proof **[A]** | Deduction management: iNymbus, HighRadius, RetailPath, DOSS, Vendormint (N-F55) **[A]** | Walmart (N-F37, secondary) **[V]**: prepaid suppliers 90% on-time and 95% in-full; collect suppliers 98% / 95%; fine of "3% cost of goods" on non-compliant cases; billed quarterly; waived if a month's penalty is under $1,000. Vendor fees not found | Supplier logistics manager (11-3071); deductions/AR analyst (43-3031 **[A mapping]**) |
| **(g) Claims and disputes** (cargo loss or damage, OS&D) | A logistics coordinator or claims clerk files the written claim **[A]**. The receiving clerk records OS&D at delivery (N-F26) **[V]** | **Carrier:** the claims desk or owner must acknowledge within 30 days and pay, decline or offer within 120 days (N-F35) **[V]**. **Broker:** mediates **[A]** | Claims modules in FAP/TMS platforms (Loop, nVision) (N-F51) **[A]**; FreightClaims.com (N-F56) **[A]** | Recoupex: "if we don't win, you don't pay"; claims 77% recovered in 2025 (N-F56, vendor) **[A]**. TLI, GEODIS, Sheer Logistics offer claims services **[A]**. Fee % not found | Receiving clerk (43-5071); shipper claims coordinator (13-1081 / 43-5011); carrier claims clerk |

### Cost, decision and payment facts by job (from the sources; no conclusions drawn)

| Job | Who bears the cost | Who decides | Who pays the service or charge |
|---|---|---|---|
| Truck detention | Driver and carrier (N-F30) **[V]** | The facility's loading and unloading practice **[A]** | Detention billed to the broker or shipper when captured (brief) |
| Ocean D&D | The party billed: either the "person for whose account" transport was provided, or the consignee (N-F32) **[V]** | Terminal and carrier free-time rules; the importer's pickup and return timing **[A]** | Importer, forwarder or trucker, depending on the invoice |
| OTIF chargebacks | Supplier: 3% of COGS on late or short cases (N-F37) **[V]** | Retailer rules | Supplier |
| Cargo claims | Carrier liable (N-F35, N-F36) **[V]** | Carrier's claims decision within 120 days | Carrier or its insurer |
| Freight audit | Shipper's overpayments | Shipper finance or logistics | Shipper pays the FAP fee (N-F51) **[A]** |
| Factoring | Carrier pays the discount (N-F40) | Carrier | Broker or shipper pays the invoice to the factor **[A]** |
| Dispatch service | Carrier pays % of gross (N-F39) | Owner-operator | Carrier |
| Dock scheduling software | — | Warehouse or DC | Priced per facility, so paid by the warehouse (N-F38) **[A]** |
| Permits, IFTA | Carrier pays state fees plus service fees (N-F42, N-F43) | Carrier | Carrier |

---

## 5. Human end users: roles and BLS counts

**Source:** BLS Occupational Employment and Wage Statistics (OEWS), May 2025, pulled through the BLS Public Data API (N-F22) **[V, data download]**. OEWS covers wage and salary jobs and excludes the self-employed, so owner-operators and sole-proprietor brokers are missing **[A]**.

**Industry columns:** 4885 = Freight Transportation Arrangement (brokers, forwarders, customs brokers); 484 = Truck Transportation; 493 = Warehousing and Storage.

| SOC | Occupation | US total | In 4885 | In 484 | In 493 | Elsewhere | Freight job titles it covers |
|---|---|---|---|---|---|---|---|
| 43-5011 | Cargo and Freight Agents | 97,670 | 53,390 (55% of the total **[our calc]**) | 4,990 | — | Couriers (492): 9,770; air transport (481): 8,880; durable wholesale (423): 260 | O*NET sample titles: "Freight Broker", "Load Planner", "Logistics Coordinator", "Intermodal Dispatcher", "Traffic and Documentation Clerk" (N-F23) **[V]**. Covers broker carrier sales, track-and-trace, forwarder operations. O*NET also has 43-5011.01 Freight Forwarders (N-F27) |
| 43-5032 | Dispatchers (except police, fire, ambulance) | 202,810 | 8,350 | 34,890 | 3,810 | Couriers: 9,290; rail (482): 1,530 | "Truck Dispatcher", "City Dispatcher", plus non-freight roles (taxi, school bus) (N-F24) **[V]** |
| 13-1081 | Logisticians | 251,040 | 8,550 | 6,370 | 8,400 | Durable wholesale: 12,860 | "Logistician", "Supply Management Specialist" (N-F25) **[V]**. Covers shipper logistics coordinators and analysts **[A mapping]** |
| 43-5071 | Shipping, Receiving and Inventory Clerks | 816,870 | 5,430 | 4,230 | 89,090 | Durable wholesale: 75,730 | "Receiving Clerk", "Shipping Clerk", "Shipping Coordinator", "Traffic Assistant" (N-F26) **[V]** |
| 43-3031 | Bookkeeping, Accounting and Auditing Clerks | 1,373,680 | 7,530 | 16,270 | n/a | — | Carrier billing clerk, broker carrier payables, shipper AP clerk **[A mapping]** |
| 43-5061 | Production, Planning and Expediting Clerks | 390,160 | 2,170 | n/a | 15,820 | — | Expediters and schedulers, possibly including dock schedulers **[A mapping]** |
| 11-3071 | Transportation, Storage and Distribution Managers | 221,180 | 6,440 | 17,860 | 21,430 | — | Traffic manager, fleet manager, warehouse manager **[A mapping]** |
| 43-4051 | Customer Service Representatives | 2,595,750 | 10,920 | 13,670 | n/a | — | Broker and carrier customer service **[A mapping]** |
| 13-1041 | Compliance Officers | 417,070 | 4,520 | 2,750 | — | — | Includes O*NET 13-1041.08 "Customs Brokers" (N-F27) **[V]**. Also trade compliance and some carrier safety/compliance roles **[A mapping]** |
| 53-3032 | Heavy and Tractor-Trailer Truck Drivers | 2,062,040 | — | 900,880 | — | — | Driver: end user of POD capture, ELD and check-call apps |

"n/a" = the series was not requested or not published. "—" = not requested.

**Roles by side** (from O*NET tasks and job postings; **[A]** unless noted):
- **Shipper:**
  - logistics coordinator or traffic manager (buys, tenders, tracks);
  - shipping clerk (BOL; O*NET task **[V]**);
  - receiving clerk (checks shipments against manifests, records damages; O*NET task **[V]**);
  - AP clerk (freight bills);
  - deductions analyst (OTIF);
  - trade-compliance specialist (customs, hazmat).
- **Carrier:**
  - dispatcher (loads, appointments, check calls);
  - driver manager;
  - billing or settlements clerk;
  - safety/compliance manager (IFTA, permits, hazmat);
  - permit clerk (heavy haul);
  - claims clerk.
- **Broker:**
  - carrier sales rep;
  - customer (shipper) sales or account rep;
  - track-and-trace rep;
  - carrier onboarding/compliance specialist;
  - carrier payables clerk.
- **Customs broker / forwarder:**
  - licensed customs broker;
  - entry writer;
  - ISF (importer security filing) filer;
  - forwarder operations / documentation clerk.
- **Warehouse / DC:** dock scheduler, receiving and shipping clerks, inventory control, warehouse manager.

**Job-posting illustrations** (labelled as illustrations, taken from search snippets) **[A]**:
- **Carrier sales representative, broker** (N-F59): "Tendering accept/reject loads, creating loads, setting appointments, dispatching, tracking and tracing loads, and resolving issues"; "communicating directly with carriers to negotiate rates".
- **Track-and-trace representative** (N-F60): "Making a high volume of outbound calls to carriers (up to 100 per day) to confirm shipment status"; "initiating 'check calls' ... on all pickups and deliveries".
- **Customs entry writer** (N-F61): "Entry writers handle entry documentation including 7501 and 3461 forms", "rate commercial invoices with tariff numbers", "calculating duties, arranging payments".
- **Dock scheduler** (N-F62): coordinates inbound appointments and assigns "a specific dock door and arrival time". A listing page shows "$18–$26/hr" (Sep 2026).
- **Freight billing clerk, trucking** (N-F63): "receiving and processing bills of lading", "request updated rate confirmations ... and compare to invoices". A listing page shows "$17–$22/hr" (Aug 2025).

---

## 6. Could not access

**Blocked or paywalled sources:**
- **FMCSA 2024 Pocket Guide to Large Truck and Bus Statistics** (PDF): HTTP 403 (Akamai) through both WebFetch and curl. We counted from the FMCSA open-data files instead (N-F02, N-F03).
- **Census Economic Census API:** needs an API key (redirected to missing_key). The Census 2022 figures for codes not in R44 (484210, 483211, 481112, 4931xx) come from SUSB, not the Economic Census.
- **Armstrong & Associates DTM sub-segment sizes** (brokerage, intermodal, managed transportation, last-mile): not on A&A's free page (N-F16). The Logistics Management and Supply Chain 24/7 articles returned 403.
- **FleetEquipment article on the Descartes survey:** 403. The press release was used instead (N-F28).
- **Gartner:** the Magic Quadrant for RTTVP and the Market Guide for FAP are paywalled; the Peer Insights FAP page returned 403. Vendor names come from snippets only.
- **Port of Los Angeles Clean Truck Program page:** 403. Number of licensed motor carriers not found.
- **federalregister.gov and eCFR:** redirected to an "unblock" page. We used govinfo (N-F08) and Cornell LII (N-F35, N-F36) instead.
- **SEC Triumph 10-K:** only an excerpt was returned (N-F44). No client counts or fee rates.

**Data that doesn't exist in the form we needed:**
- **FMC:** the licensed-OTI list page is form-driven and gives no count. The NVOCC vs OFF vs dual split was not found.
- **CBP:** no official count of individual licensed brokers or permitted broker firms on the pages we read. The figure used is secondary (N-F09).
- **FMCSA Motus dataset:** a daily list of changes only, not usable for totals. The L&I snapshot is frozen at 2026-05-14.
- **STB rail demurrage:** per-railroad quarterly PDFs not opened. Only the trade-press total was used (N-F34).
- **OEWS:** series for 4-digit trucking (4841/4842) and for manufacturing (31–33) do not exist.

**Counts and data not found:**
- **Firm counts:**
  - intermodal marketing companies;
  - truck dispatch services;
  - factoring companies;
  - freight claims services, and their fee %;
  - OS/OW permit services;
  - IFTA/IRP/UCR filing services;
  - port drayage carriers at the LA/LB ports;
  - FAP providers in total.
- **Specialized trucking:** no association-level counts for livestock, logging, auto-carrier or heavy-haul carriers (FMCSA checkboxes used as proxies). NTTC's industry count is not published beyond the "over 200 members" snippet.
- **Software adoption:** no credible survey of small carriers' or owner-operators' software use found.
- **Amazon:** no current US-only DSP count from Amazon.

---

## 7. Sources

Each entry gives: title; publisher or author; date; URL; access date; what was read; source type.

- **N-F01** — Statistics of U.S. Businesses 2022, "us_state_6digitnaics_2022.txt" (firms, establishments, employment and receipts by enterprise size); U.S. Census Bureau; 2022 data; https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_6digitnaics_2022.txt ; accessed 2026-09-14; data download (national rows parsed); primary.
- **N-F02** — Company Census File (dataset az4n-8mr2); FMCSA via data.transportation.gov; updated 2026-09-14; https://data.transportation.gov/resource/az4n-8mr2.json ; accessed 2026-09-14; data download (our aggregate SoQL queries on status_code, carrier_operation, classdef, power_units and crgo_* flags); primary.
- **N-F03** — Carrier – All With History (L&I operating authority, dataset 6eyk-hxee); FMCSA via data.transportation.gov; "last refreshed on 05/14/2026 and will no longer be updated"; https://data.transportation.gov/resource/6eyk-hxee.json ; accessed 2026-09-14; data download (our queries on broker_stat, common_stat, contract_stat, bond_file and docket prefix); primary.
- **N-F04** — Motus Carrier (dataset nakq-58th, daily difference file); FMCSA via data.transportation.gov; 2026-09-14; https://data.transportation.gov/resource/nakq-58th.json ; accessed 2026-09-14; metadata and a group-by query (a list of changes, not totals); primary.
- **N-F05** — 63rd Annual Report, Fiscal Year 2024; Federal Maritime Commission; Apr 2025; https://fmc.gov/wp-content/uploads/2025/04/FY-2024-Annual-Report.pdf ; accessed 2026-09-14; partial (text extracted; pp. 33–34 read); primary.
- **N-F06** — Ocean Transportation Intermediaries; FMC; undated; https://www.fmc.gov/about/bureaus-offices/bureau-of-enforcement-investigations-and-compliance-beic/office-of-compliance/ocean-transportation-intermediaries/ ; accessed 2026-09-14; full page; primary.
- **N-F07** — Customs Brokers; U.S. Customs and Border Protection; undated (lists the 2026 permit fee); https://www.cbp.gov/trade/programs-administration/customs-brokers ; accessed 2026-09-14; full page; primary.
- **N-F08** — Modernization of the Customs Broker Regulations, final rule, 87 FR 63267 (doc. 2022-22445); CBP / Federal Register (govinfo copy); 2022-10-18; https://www.govinfo.gov/content/pkg/FR-2022-10-18/html/2022-22445.htm ; accessed 2026-09-14; partial; primary.
- **N-F09** — "Becoming a Licensed Customs Broker" slides; STAR USA; 2024; https://s3.starusa.org/wp-content/uploads/2024/05/Star-USA-Becoming-a-Licensed-Customs-Broker-Slides.pdf ; accessed 2026-09-14; partial (text extracted); secondary.
- **N-F10** — ABI Software Vendor List (Pub. #1716-0422); CBP Office of Trade; 2025-07-16; https://www.cbp.gov/sites/default/files/2025-07/ABI%20Software%20Vendors%20(FINAL%20July%2016%202025)_508_0.pdf ; accessed 2026-09-14; full (text extracted; our approximate count of vendor entries); primary.
- **N-F11** — "CBP releases March 2025 monthly update"; CBP; 2025-04-14; https://www.cbp.gov/newsroom/national-media-release/cbp-releases-march-2025-monthly-update ; accessed 2026-09-14; partial; primary.
- **N-F12** — The Short Line and Regional Railroad Industry (Industry Facts); ASLRRA; undated; https://www.aslrra.org/about-us/industry-facts/ ; accessed 2026-09-14; full page; trade association.
- **N-F13** — Freight Rail Facts & Figures; Association of American Railroads; 2025 data; https://www.aar.org/freight-rail-facts-figures/ ; accessed 2026-09-14; partial; trade association.
- **N-F14** — "IANA: Intermodal volume fell 2% in Q4, rose 2.3% in full-year 2025"; Progressive Railroading; 2026-02-17; https://www.progressiverailroading.com/intermodal/news/IANA-Intermodal-volume-fell-2-in-Q4-rose-23-in-full-year-2025--76371 ; accessed 2026-09-14; full article; secondary (reports IANA data).
- **N-F15** — "Intermodal volumes see second quarter gains, reports IANA"; Logistics Management; 2025; https://www.logisticsmgmt.com/article/intermodal_volumes_see_second_quarter_gains_reports_iana ; accessed 2026-09-14; snippet only; secondary.
- **N-F16** — U.S. 3PL Market Size Estimates; Armstrong & Associates; 2026 (2025 data); https://www.3plogistics.com/3pl-market-info-resources/3pl-market-information/us-3pl-market-size-estimates/ ; accessed 2026-09-14; full page; primary (analyst estimate).
- **N-F17** — "US 3PL Market Sees Strong Revenue Growth in 2025 as Freight Recession Nears End"; The Logistics News; 2026-06-17; https://thelogisticsnews.org/en/articles/us-3pl-revenues-strong-annual-gains-2025 ; accessed 2026-09-14; full article; secondary (reports A&A).
- **N-F18** — "A Time of Uncertainty for Logistics Providers"; Transport Topics; 2025-04-10; https://www.ttnews.com/articles/time-uncertainty-3pls-2025 ; accessed 2026-09-14; partial; secondary (reports A&A 2024).
- **N-F19** — "Private Fleets Eye More Growth"; Gary Petty, National Private Truck Council; Sep 2025; https://www.nptc.org/gary-column/private-fleets-eye-more-growth/ ; accessed 2026-09-14; full page (the "940,280 / 47%" figure comes from a search snippet and is not on this page); trade association.
- **N-F20** — "Key insights from the NPTC 2025 benchmarking survey on private fleet operations"; FleetOwner (Gary Petty); 2025-08-12; https://www.fleetowner.com/private-fleets/blog/55308859/key-insights-from-the-nptc-2025-benchmarking-survey-on-private-fleet-operations ; accessed 2026-09-14; full article; trade press.
- **N-F21** — "Ports of Long Beach and Los Angeles Win Sustainability Award"; Clean Air Action Plan (Ports of LA/LB); 2024-05-02; https://cleanairactionplan.org/2024/05/02/ports-of-long-beach-and-los-angeles-win-sustainability-award/ ; accessed 2026-09-14; full article; primary (port authorities).
- **N-F22** — OEWS May 2025 national and industry estimates, series OEUN0000000{industry}{SOC}01; U.S. Bureau of Labor Statistics, Public Data API v2; 2025 reference year; https://api.bls.gov/publicAPI/v2/timeseries/data/ ; accessed 2026-09-14; data download; primary.
- **N-F23** — O*NET 43-5011.00 Cargo and Freight Agents; O*NET OnLine (US DOL); current; https://www.onetonline.org/link/summary/43-5011.00 ; accessed 2026-09-14; partial (titles, tasks); primary.
- **N-F24** — O*NET 43-5032.00 Dispatchers, Except Police, Fire, and Ambulance; O*NET OnLine; current; https://www.onetonline.org/link/summary/43-5032.00 ; accessed 2026-09-14; partial; primary.
- **N-F25** — O*NET 13-1081.00 Logisticians; O*NET OnLine; current; https://www.onetonline.org/link/summary/13-1081.00 ; accessed 2026-09-14; partial; primary.
- **N-F26** — O*NET 43-5071.00 Shipping, Receiving, and Inventory Clerks; O*NET OnLine; current; https://www.onetonline.org/link/summary/43-5071.00 ; accessed 2026-09-14; partial; primary.
- **N-F27** — O*NET quick search "customs broker" (13-1041.08 Customs Brokers; 43-5011.01 Freight Forwarders); O*NET OnLine; current; https://www.onetonline.org/find/quick?s=customs+broker ; accessed 2026-09-14; results list; primary.
- **N-F28** — "Descartes' 9th Annual Study Finds Transportation Management Reaches Record Strategic Importance"; Descartes Systems Group (with SAPIO Research); 2025-09-15; https://www.globenewswire.com/news-release/2025/09/15/3149812/0/en/Descartes-9th-Annual-Study-Finds-Transportation-Management-Reaches-Record-Strategic-Importance.html ; accessed 2026-09-14; full release; vendor (survey).
- **N-F29** — "TMS: Time to Ditch the Spreadsheets"; Inbound Logistics (quoting Allan J. Miner, CEO of CT Logistics); June 2025; https://www.inboundlogistics.com/articles/tms-time-to-ditch-the-spreadsheets/ ; accessed 2026-09-14; partial; trade press (expert claim).
- **N-F30** — "Estimates Show Commercial Driver Detention Increases Crash Risks and Costs, but Current Data Limit Further Analysis", Report No. ST2018019; U.S. DOT Office of Inspector General; 2018-01-31; https://www.oig.dot.gov/sites/default/files/FMCSA%20Driver%20Detention%20Final%20Report.pdf ; accessed 2026-09-14; partial (text extracted, summary and findings); primary.
- **N-F31** — Detention and Demurrage (D&D data page); Federal Maritime Commission; data through 2025-03-31; https://www.fmc.gov/detention-and-demurrage/ ; accessed 2026-09-14; partial; primary.
- **N-F32** — "FMC Publishes Final Rule on Detention and Demurrage Billing Practices"; FMC; 2024; https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/ ; accessed 2026-09-14; full article; primary.
- **N-F33** — Demurrage & Accessorial Charges; Surface Transportation Board; undated; https://www.stb.gov/reports-data/demurrage-accessorial-charges/ ; accessed 2026-09-14; full page (index of railroad reports); primary.
- **N-F34** — "'Insult to injury': Record rail demurrage adds to shipper costs"; Supply Chain Dive (S. Zimmerman, E. Lopez); 2022-01-12; https://www.supplychaindive.com/news/insult-injury-rail-demurrage-record-shipper-costs/611667/ ; accessed 2026-09-14; full article; trade press.
- **N-F35** — 49 CFR 370.5 and 370.9 (claims acknowledgment; disposition); Cornell LII; current; https://www.law.cornell.edu/cfr/text/49/370.5 and https://www.law.cornell.edu/cfr/text/49/370.9 ; accessed 2026-09-14; full sections; primary (regulation text).
- **N-F36** — 49 U.S.C. § 14706 (Carmack; limits on filing claims and suits); Cornell LII; current; https://www.law.cornell.edu/uscode/text/49/14706 ; accessed 2026-09-14; partial (subsection e); primary (statute).
- **N-F37** — "Walmart OTIF: A Supplier's Guide to On-Time In-Full"; 8th & Walton; 2024-05-16; https://www.8thandwalton.com/blog/walmart-otif ; accessed 2026-09-14; partial; secondary (consultancy).
- **N-F38** — "How Much Does Dock Scheduling Software Cost? [2026 Pricing Comparison]"; LoadingCalendar; 2026-07-19; https://www.loadingcalendar.com/en/blog/how-much-does-dock-scheduling-software-cost ; accessed 2026-09-14; full article; vendor.
- **N-F39** — "How Much Does a Truck Dispatcher Cost? Percentage vs Flat-Fee (2026)"; FleetCollect (Herman Armstrong); 2026-05-28; https://fleetcollect.net/blog/truck-dispatcher-cost-percentage-vs-flat-fee ; accessed 2026-09-14; full article; vendor.
- **N-F40** — "Truck Factoring Rates: How Much Do Factoring Companies Charge?"; Truckstop; 2022-02-17; https://truckstop.com/blog/freight-factoring-rates/ ; accessed 2026-09-14; full article; vendor.
- **N-F41** — Load Boards (plans and pricing); DAT Freight & Analytics; undated; https://www.dat.com/load-boards ; accessed 2026-09-14; full page; vendor.
- **N-F42** — Fees – Oversize Overweight Permits; Highway Permits; effective 2026-01-01; https://highway-permits.com/fees/ ; accessed 2026-09-14; full page; vendor.
- **N-F43** — IRP IFTA Tax & Permits; SunCoast Compliance; undated; https://www.suncoastcompliance.com/irp-ifta-tax-permits/ ; accessed 2026-09-14; full page; vendor.
- **N-F44** — Triumph Financial, Inc. Form 10-K FY2025; SEC EDGAR; filed 2026; https://www.sec.gov/Archives/edgar/data/1539638/000153963826000007/tfin-20251231.htm ; accessed 2026-09-14; partial (excerpt; client-segment wording comes from a search snippet); primary (filing).
- **N-F45** — "Everything you need to know about Amazon's Delivery Service Partner (DSP) program"; Amazon; undated; https://www.aboutamazon.com/news/policy-news-views/amazon-dsp-program-update ; accessed 2026-09-14; partial; primary (company claim).
- **N-F46** — "Best Freight Procurement Software in 2026"; Freehand; 2026; https://www.freehand.ai/articles/best-freight-procurement-software ; accessed 2026-09-14; snippet only; vendor.
- **N-F47** — "Best Dock Scheduling Software for Warehouses in 2026"; Arrivy; 2026; https://www.arrivy.com/blog/best-dock-scheduling-software-for-warehouses/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F48** — "project44 named a leader in the 2025 Gartner Magic Quadrant for Real-Time Transportation Visibility Platforms for fifth consecutive year"; project44; Feb 2025; https://www.project44.com/press-releases/project44-named-a-leader-in-the-2025-gartner-magic-quadrant-for-real-time-transportation-visibility-platforms-for-fifth-consecutive-year/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F49** — "FourKites Advances AI-First Supply Chain Strategy, Withdraws From Gartner RTTVP Magic Quadrant"; FourKites via BusinessWire; 2025-02-24; https://www.businesswire.com/news/home/20250224055194/en/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F50** — Market Guide for Freight Audit and Payment Providers (doc 3978673; vendor names); Gartner; date not shown; https://www.gartner.com/en/documents/3978673 ; accessed 2026-09-14; snippet only (paywalled); secondary.
- **N-F51** — "How Much Does Freight Audit Cost? Pricing Models Explained"; Navix; undated; https://www.navix.io/freight-audit-cost/ ; accessed 2026-09-14; snippet only; vendor. (Loop's claims page, https://www.loop.com/industry-insights/freight-claims-management-how-to-recover-overpayments-and-loss-or-damage-costs , is also a snippet, vendor.)
- **N-F52** — "Parcel Audit Services: How They Work & What They Recover in 2026"; D'Arrigo Consulting; 2026; https://www.darrigoconsulting.com/blog/parcel-audit-services-guide ; accessed 2026-09-14; snippet only; vendor/consultancy.
- **N-F53** — Parcel Service Refund (home page) and Refund Retriever services; vendors; undated; https://www.parcelservicerefund.com/ and https://www.refundretriever.com/services ; accessed 2026-09-14; snippet only; vendor.
- **N-F54** — "Best Detention and Demurrage Management Software in 2026"; BuyCo; 2026; https://buyco.co/blog/productivity/best-detention-demurrage-management-software/ ; accessed 2026-09-14; snippet only; vendor. (Terminal49 and Vizion blogs also snippets.)
- **N-F55** — "3 Best Automated Retail Chargeback & Deduction Management Platforms for CPG Brands (2026)"; RetailPath; 2026; https://retailpath.xyz/articles/3-best-automated-retail-chargeback-deduction-management-platforms-for-cpg-brands-2026 ; accessed 2026-09-14; snippet only; vendor.
- **N-F56** — Recoupex (Cargo Claims Recovery) and FreightClaims.com; vendors; undated; https://www.recoupex.com/ and https://freightclaims.com/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F57** — "Electronic Bill of Lading Software for US Carriers (2026 Guide)"; Dashdoc; 2026; https://www.dashdoc.com/en-US/blog/electronic-bill-of-lading-software-us ; plus SmartBOL, https://smartbol.com/electronic-bill-of-lading-ebol-solutions/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F58** — DGIS Hazmat Transport Management Software; Labelmaster; plus the eCFR 49 CFR 172.201 snippet; undated; https://www.labelmaster.com/software ; https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-172/subpart-C/section-172.201 ; accessed 2026-09-14; snippet only; vendor / primary (regulation via snippet).
- **N-F59** — "Carrier Sales Representative (Freight Broker)" job posting; Amerilux International; 2025; https://ameriluxinternational.com/wp-content/uploads/2025/job-postings/Carrier-Sales-Representative-Freight-Broker.pdf ; accessed 2026-09-14; snippet only; illustration.
- **N-F60** — Brokerage Tracking Representative posting (Covenant Logistics via JobTarget) and Track Trace job listings (ZipRecruiter); 2025–2026; https://www.jobtarget.com/jobs/jt-t6q7ltviy3/brokerage-tracking-representative-chattanooga-tennessee and https://www.ziprecruiter.com/Jobs/Track-Trace ; accessed 2026-09-14; snippet only; illustration.
- **N-F61** — "Customs Entry Writer Job Description"; GlobalTradeJobs; undated; https://globaltradejobs.com/blog/customs-entry-writer-job-description ; accessed 2026-09-14; snippet only; illustration.
- **N-F62** — Dock Scheduler Jobs listing; ZipRecruiter; Sep 2026; https://www.ziprecruiter.com/Jobs/Dock-Scheduler ; accessed 2026-09-14; snippet only; illustration.
- **N-F63** — Freight Billing Clerk Jobs listing; ZipRecruiter; Aug 2025; https://www.ziprecruiter.com/Jobs/Freight-Billing-Clerk ; accessed 2026-09-14; snippet only; illustration.
- **N-F64** — "Public Warehousing Versus Contract Warehousing"; Amware; and "Public Warehouse 3PL", InventoryOps; undated; https://amware.com/posts/public-warehousing-versus-contract-warehousing and https://www.inventoryops.com/articles/public-warehouse-3pl.html ; accessed 2026-09-14; snippet only; vendor/secondary.
- **N-F65** — Broker and Freight Forwarder Financial Responsibility Rule Overview; FMCSA; 2025–2026; https://www.fmcsa.dot.gov/registration/broker-and-freight-forwarder-financial-responsibility-rule-overview-and-compliance ; accessed 2026-09-14; snippet only; primary (via snippet).
- **N-F66** — Total Revenue for Used Household and Office Goods Moving, Employer Firms (REVEF48421ALLEST); FRED / Census Service Annual Survey; 2022; https://fred.stlouisfed.org/series/REVEF48421ALLEST ; accessed 2026-09-14; snippet only; primary (via snippet).
- **N-F67** — National Tank Truck Carriers (home page / FAQ); NTTC; undated; https://www.tanktruck.org/ ; accessed 2026-09-14; snippet only; trade association.
- **N-F68** — IFTA Quarterly Filing Service; Start4Truckers; undated; https://start4truckers.com/services/ifta-quarterly-filing-service/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F69** — "Dock Appointment Scheduling Software | The Essentials"; Opendock; undated; https://blog.opendock.com/dock-appointment-scheduling ; accessed 2026-09-14; snippet only; vendor.
- **N-F70** — "Descartes MacroPoint vs Trucker Tools"; Gartner Peer Insights; 2025; https://www.gartner.com/reviews/market/real-time-transportation-visibility-platforms/compare/descartes-macropoint-vs-trucker-tools ; accessed 2026-09-14; snippet only; secondary.
- **N-F71** — (reserved; merged into N-F54.)
- **N-F72** — (reserved; merged into N-F58.)
- **N-F73** — OmniPermits (permit costs blog) and TruckPermity (FAQ); vendors; undated; https://omnipermits.com/blog/costs-of-overweight-permits-in-various-us-states and https://truckpermity.com/faq/ ; accessed 2026-09-14; snippet only; vendor.
- **N-F74** — "Best TMS software for small fleets" (TruckingOffice and others); FreightWaves Ratings; undated; https://ratings.freightwaves.com/best-tms-software-for-small-fleets/ ; accessed 2026-09-14; snippet only; secondary/vendor.
- **N-F75** — (reserved.)
- **N-F76** — "STB Sets 2021-2025 'Deflator Factors'"; Railway Age; 2025; https://www.railwayage.com/regulatory/stb-sets-2021-2025-deflator-factors/ ; accessed 2026-09-14; snippet only; trade press.
- **N-F77** — Port of Los Angeles Clean Truck Program; Port of Los Angeles; undated; https://portoflosangeles.org/environment/air-quality/clean-truck-program ; accessed 2026-09-14; snippet only (the page itself returned 403); primary (via snippet).
