# S3b check S: facility, fleet, retail-compliance and trade jobs (C-04, C-15, C-18, C-19, C-20, C-22)

- **What this is:** new desk research for S3b ("fact sheets and the shortlist") in run 01. It covers the six cards below:

  | Card | Job |
  |---|---|
  | C-04 | Dock appointments, for warehouses and distribution centres |
  | C-15 | Routing own delivery fleets, for food, beverage and industrial distributors |
  | C-18 | Warehouse storage and handling bills, for small public and contract warehouses |
  | C-19 | Retailer OTIF fines and deductions, for small and mid-sized suppliers to big-box retailers |
  | C-20 | Import entries, for small importers, via customs brokers' entry writers |
  | C-22 | Port drayage dispatch, for small drayage carriers |

  For each card it gathers:
  - the fact-sheet items that need new research: item 5 (software penetration and why now), item 6 (addressable work), item 7 (budget holder and implementation) and item 9 (competitors, substitutes and the incumbent map) (`submarket_selection.md` §4 S3b, §13);
  - evidence and a suggested score for eight rows: A2, A3, A6, W1, W3, W4, W5 and W6.
- **Not covered here:** items 1-4, 8, 10 and 11, and rows A1, A4, A5 and W2. The coordinator scores those from data already held.
- **Date:** 2026-09-15.
- **Status:** input to S3b; **it decides nothing**. Every score is a suggestion, labelled **[our call]**, made under the row rules in `research/selection_runs/run-01/2_knockouts.md` §5 (restated below). The coordinator makes the calls.
- **Labels:**
  - *verified*: read at the source (a quote from the page, a value from a downloaded file or an official table).
  - *assumed*: a search snippet, a secondary summary, a vendor claim, memory, or a blocked page. **Vendor figures are always *assumed*,** even when read on the vendor's own page.
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
  - **Affiliation flags.** An association survey counts as a source, but it is always shown with who runs it:
    - CRF (credit managers);
    - NCBFAA (customs brokers and forwarders);
    - HTA (West Coast drayage carriers);
    - NPTC (private fleets);
    - ATRI (the research arm of the American Trucking Associations).
- **New sources** are N-S01 to N-S43 (§4). Earlier sources keep their IDs. All were accessed on 2026-09-15.

**The row rules used here** (`2_knockouts.md` §5, verbatim scale):

| Row | Weight | 1 | 0.5 | 0 |
|---|---|---|---|---|
| A2 Fit for automation | 10 | office work drives the cost | mixed | mostly physical |
| A3 Pain and urgency (per side) | 25 | a forcing event | a known cost without one | little evidence |
| A6 Expansion leverage | 15 | several adjacent groups | one or two | none |
| W1 Access and cost to reach (per side) | 20 | one channel gathers most buyers | partial | dispersed |
| W3 Whole product and time to value | 20 | data at hand | integration needed | no data access |
| W4 Competition and substitutes | 15 | both hold: proven spend, and weak, legacy or missing software (C10) | one holds | neither |
| W5 Willingness to change (per side) | 15 | a mandate or evidence of the wish to change | neutral or unknown | resistance |
| W6 Time and resources to win | 25 | fast | moderate | slow |

- **Per-side rows** (A3, W1, W5) are judged for both sides, and the better side is named (rule C5).
- **The dominance show-stopper** (§5.5, C10): one vendor already serves more than half of the target customers for the job, and they are satisfied. Satisfaction can only be checked in S5.

**Freight words used here** (others are in `1_candidates.md` and check N):
- **Dock appointment:** a booked time slot and door for a truck at a warehouse.
- **Detention:** time a truck waits at a shipper's or receiver's dock beyond the free time (often 2 hours), which carriers bill as a fee.
- **WMS (warehouse management system):** software that records what is received, stored, picked and shipped in a warehouse. **YMS:** yard management system, which tracks trailers in the yard.
- **TMS (transportation management system):** software that plans, dispatches and bills truck moves.
- **3PL:** a third-party logistics firm. A **public warehouse** stores goods for many customers and bills per pallet; a **contract warehouse** serves one customer under a contract.
- **OTIF (on time, in full):** a retailer's delivery rule, with fines for late or short cases. **MABD:** the "must arrive by date" the rule is measured against.
- **Deduction / chargeback:** money a retailer keeps back from a supplier's invoice, for a fine, a shortage or a dispute.
- **EDI:** electronic data interchange, the standard business messages between firms. Examples: 856 = advance ship notice (ASN); 812 = credit/debit adjustment; 204/214 = load tender/status.
- **POD:** proof of delivery.
- **Customs broker:** a firm or person licensed by CBP (US Customs and Border Protection) to file entries for importers. An **entry writer** prepares the entries under a licensed broker.
- **ACE:** Automated Commercial Environment, CBP's trade system. **ABI:** Automated Broker Interface, the EDI link that filing software uses to talk to ACE.
- **HTS:** Harmonized Tariff Schedule, the US list of tariff codes and duty rates.
- **De minimis:** the $800 duty-free threshold for low-value shipments, ended on 29 Aug 2025 (N-J29).
- **IEEPA:** International Emergency Economic Powers Act, the law used for the 2025 tariffs. **CAPE:** CBP's claim system for IEEPA refunds.
- **Drayage:** short truck moves of containers between a port or rail terminal and a nearby warehouse. A **chassis** is the wheeled frame a container rides on. A **dry run** is a wasted trip, e.g. when the container is not available.
- **Terminal appointment system (TAS):** the terminal's booking system for truck visits (eModal is the main one in the US, N-S39).
- **Per diem:** a daily charge for keeping a container or chassis too long.
- **Route accounting:** the distributor's order, invoice and settlement system for delivery routes, often with driver handhelds.

---

## 1. Summary table

| Card | Penetration (one line) | Trigger(s) | Budget holder | Implementation | Vendors (count; leader; dominance) | Service firms | Suggested A2 / A3 / A6 / W1 / W3 / W4 / W5 / W6 **[our call]** | Sources |
|---|---|---|---|---|---|---|---|---|
| **C-04 Dock appointments** | No neutral survey found. The largest network, Opendock, claims 4,000+ warehouses, about 7% of 54,831 warehouse and grocery-distributor sites [our calc; vendor numerator]. Drivers are still detained at 39.3% of stops (ATRI) | No rule or retailer mandate with a date. FMCSA's detention study is research, not a rule (notice of Feb 2024). Technology shift: AI booking agents (DHL Supply Chain with HappyRobot, Nov 2025; Opendock's server for AI agents, Jun 2026) | DC or warehouse operations manager; the warehouse operations budget. Carriers bear most of the waiting but do not buy the tool | A standalone calendar plus a booking link. No integration is needed to start, and APIs exist | 11+ named; leader by claim Opendock (about 7% of sites); **no dominance** | 3PL warehouse operators; broker operations reps; AI voice agents on the carrier side | 0.5 / 0.5 / 1 / 0.5 / 1 / 0.5 / 0.5 / 0.5 | N-S07, N-S08, N-S17, N-S34, N-S41, N-F38, N-C24, N-S01, N-S02 |
| **C-15 Routing own fleets** | No neutral share found (the NPTC 2025 summaries list only safety technology). Beer: VIP's route accounting serves "more than 1,000 distributors" (2019) against 1,393 beer-wholesaler firms (2022), and claims over half of US beer volume (snippet) | No forcing event. The driver shortage fell to #12 in ATRI's 2025 list. CARB voted on 25 Sep 2025 to repeal the Advanced Clean Fleets rules for private and drayage fleets | Distributor's VP of operations or fleet manager; the fleet operating budget. Payer = saver | An order export from the ERP, customer addresses and truck data. Simple tools go live in weeks; route-accounting and handheld integration takes longer | 20+ named; no share data; **VIP is a dominance candidate in the beer segment only** | Dedicated contract carriage, $32.0B (R33) | 0.5 / 0.5 / 1 / 0.5 / 0.5 / 0.5 (beer: show-stopper candidate) / 0.5 / 0.5 | N-S03, N-S04, N-S28 to N-S32, R38, N-S19, R33, N-S01, N-S02 |
| **C-18 Warehouse bills** | Vendor-only. Extensiv's benchmark (200-240 3PL warehouses): "82% of 3PL warehouses lose revenue to uncaptured" charges. 63% of mostly larger firms use a WMS (snippet) | None found. Labour-cost pressure (70% cite it; vendor survey) | Warehouse owner or controller; the finance and administration budget | Needs WMS event data and rate cards: integration with the WMS, or spreadsheets where no WMS exists | 9+ named; Extensiv "1,500+ 3PLs", at most about 20% of 7,469 US warehousing firms [our calc]; **no dominance** | Few; outsourced bookkeeping (*assumed*) | 1 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 | N-S14 to N-S16, N-S37, N-K27, N-D04, N-S01, N-S02 |
| **C-19 OTIF and deductions** | CRF 2018: **70% of suppliers with sales of $500M or less used no third-party deduction technology**, and none of them outsourced any deduction task | Retailer rules with dates: Walmart's OTIF changes from 1 Feb 2024 (quarterly billing; 90% on-time and 95% in-full goals; 3% of cost of goods); Target's fine change in Q3 2024; Home Depot's monthly dispute cadence (2024) | Supplier's CFO, controller or credit manager (accounts receivable); logistics for prevention | Retailer-portal credentials (bots), ERP receivables, EDI 856/812 and carrier PODs. Back-claims can show value within days | 7+ software vendors; SPS Commerce (SupplyPike; $206M deal; about $25M of 2025 revenue) with share unknown; **no dominance shown** | Contingency recovery firms (e.g. 30% of recoveries); consultancies; carriers supply the proof | 1 / 1 / 1 / 0.5 / 0.5 / 1 / 1 / 0.5 | N-N29, N-S10 to N-S13, N-S35, N-S36, N-S40, N-F55, N-S01, N-S02 |
| **C-20 Import entries** | Filing is fully electronic (ABI); the manual work is classification and keying from invoices. Brokers and forwarders: 25% cite manual workflows as the top inhibitor to growth, and 55% plan to prioritise AI (vendor survey with NCBFAA) | De minimis ended 29 Aug 2025. Supreme Court IEEPA ruling on 20 Feb 2026. CAPE refunds from 20 Apr 2026: about $165B of duties on 53M+ entries | Broker owner (operations or IT; software per entry); the importer pays the broker per entry | A classification and extraction co-pilot works on invoice PDFs with no integration. Filing needs ABI certification or a partner's API. HTS has an open API | About 70 ABI vendors; NetCHB "more than 700 customs brokers", about 30% of 2,365 permit holders [our calc]; **no dominance** | Customs brokerages (NCBFAA: 1,500+ member companies); forwarders; parcel carriers | 1 / 1 / 1 / 1 (broker side) / 0.5 / 0.5 / 1 (broker side) / 0.5 | N-F08, N-F10, N-H22, N-J29, N-S05, N-S06, N-S09, N-S20, N-S26, N-S33, N-S38 |
| **C-22 Drayage dispatch** | HTA/TradeLanes 2021: "80%" of members say carriers still don't use technology for demurrage and detention problems. 34,331 of 43,571 local-trucking firms have under 5 staff | No positive forcing event. CARB repealed its drayage zero-emission rule (vote 25 Sep 2025). The FMC billing rule (2024) moves demurrage and detention bills away from truckers | Drayage owner or operations manager; a small operations budget | Integration needed: terminal appointment systems (eModal and others), terminals' availability data, chassis pools, customers' delivery orders | 7+ named; WiseTech (Envase: "more than 1,300 customers" of all types, about $35M revenue; plus Trinium); PortPro; no share data; **no dominance shown** | Drayage brokers and intermodal marketing companies; dispatch services | 0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 0.5 (W6 leans 0) | N-S19, N-S21 to N-S25, N-S39, N-F32, N-D04, N-S01, N-S02 |

**What these rows add to each axis [our calc]** (weight × suggested score; the coordinator adds A1, A4, A5 and W2):

| Card | A2 + A3 + A6 (out of 50) | W1 + W3 + W4 + W5 + W6 (out of 95) |
|---|---|---|
| C-04 | 32.5 | 57.5 |
| C-15 | 32.5 | 47.5 |
| C-18 | 30 | 47.5 |
| C-19 | **50** | 62.5 |
| C-20 | **50** | **65** |
| C-22 | 25 | 47.5 (35 if W6 = 0) |

---

## 2. Card by card

Each card gives items 5, 6, 7 and 9, then the eight rows with a one-line reason.

**Two neutral measures used on every card:**
- **Role counts and wages:** BLS OEWS May 2025, by the public API (N-S01, *verified*).
- **Is it office work, and does human connection matter?** O*NET 30.0 ratings (N-S02, *verified* download):
  - importance on a 1-5 scale for "Working with Computers", "Performing General Physical Activities" and "Establishing and Maintaining Interpersonal Relationships";
  - how often each contact method is used, on a 1-5 scale, for telephone and face-to-face.
  - These test R22 (text- and number-heavy work) and R23 ("human connection isn't a key benefit").

| SOC | Role | Computers | Physical | Interpersonal | Telephone | Face-to-face | Rated |
|---|---|---|---|---|---|---|---|
| 43-5032 | Dispatchers | 4.12 | 1.84 | 3.80 | 5.00 | 4.97 | 2021 |
| 43-5071 | Shipping, receiving and inventory clerks | 3.25 | 3.83 | 3.28 | 4.45 | 4.86 | 2019 |
| 43-5061 | Production, planning and expediting clerks | 4.35 | 1.99 | 3.15 | 4.76 | 4.92 | 2022 |
| 43-3021 | Billing and posting clerks | 4.67 | 1.60 | 2.73 | 4.72 | 4.00 | 2022 |
| 13-1041.08 | Customs brokers | 4.47 | 1.44 | 3.78 | 5.00 | 4.72 | 2017 |
| 43-5011 | Cargo and freight agents | 3.14 | 3.21 | 3.41 | 4.55 | 4.57 | 2021 |
| 43-3011 | Bill and account collectors | 4.16 | 2.14 | 3.58 | 4.62 | 3.80 | 2018 |
| 13-2041 | Credit analysts | 4.45 | 1.25 | 3.75 | 4.68 | 4.68 | 2020 |
| 13-1081 | Logisticians | 4.29 | 1.79 | 4.21 | 5.00 | 4.61 | 2016 |
| 53-3032 | Heavy and tractor-trailer truck drivers | 2.82 | 3.46 | 2.76 | 3.97 | 4.06 | 2022 |
| 53-3031 | Driver/sales workers | 2.41 | 4.36 | 2.80 | 3.77 | 4.60 | 2020 |

### 2.1 C-04 · Dock appointments, for warehouses and distribution centres

**Item 5: software penetration and why now**
- **How much still runs on phone, email and spreadsheets: no neutral figure found** (§5).
  - Proxy 1: in a 2025 Peerless Research Group study for *Logistics Management*, 63% of companies use a WMS. Among firms shopping for a yard system, 44% want "automated dock scheduling" (N-S37, snippet, *assumed*). The sample leans to larger firms, and dock scheduling is narrower than a WMS.
  - Proxy 2, the largest network: Opendock (owned by Loadsmart) says it connects carriers to "4,000+ warehouses" (June 2026, N-S08, vendor, *assumed*). An earlier snippet said 3,000+ warehouses, 600,000+ appointments a month and 75,000+ carriers (N-S07, *assumed*).
    - There are 19,979 warehouse sites and 34,852 grocery-distributor sites (N-E17): 54,831 in all.
    - So Opendock reaches about **7% of those sites** **[our calc; vendor numerator]**, before counting manufacturers' and retailers' own docks.
  - Evidence that the job is done poorly: drivers reported being detained at **39.3% of stops** in 2023 (ATRI, N-C24; ATRI flag). Detention/delay at customer facilities is truck drivers' #5 issue in ATRI's 2025 survey (R38, *verified*).
- **Systems of record and plumbing (R30):**
  - the receiving site's WMS (purchase orders and ASNs);
  - carriers' and brokers' TMSs, and EDI 204/214 (load tender and status);
  - booking links sent by email;
  - the dock-scheduling tool itself.
  - **Open APIs exist.** Opendock calls itself "API-first", with an API discovery endpoint and "the first MCP server built for dock appointment scheduling", which lets AI agents "schedule, modify, cancel, and query dock appointments across any warehouse on the platform" (9 Jun 2026, N-S08, vendor, *assumed*). It lists HappyRobot, Qued and others as agent partners.
  - Plumbing test: **passes**. The job can run on a standalone calendar with no integration, and a leading vendor already exposes an API.
- **Triggers for change now:**
  - **No regulation or retailer rule with a date was found.**
    - FMCSA's *Impact of Driver Detention Time on Safety and Operations* is a "research study" with about "80 carriers and 2,500 CMV drivers". It is an information collection filed 16 Feb 2024, not a rulemaking (N-S17, *verified*).
    - A final report was planned for July 2025 (N-S18, snippet, *assumed*). Whether it was published, and whether any detention bill is moving in 2025-26, was not checked: the web-search budget ran out (§5).
  - **Technology shift: AI agents now book appointments on the carrier side.**
    - HappyRobot's voice agents handle "appointment scheduling" among other calls.
    - HappyRobot raised a $150M Series C at a $1.22B valuation (Aug 2025), and DHL Supply Chain partnered with it on 11 Nov 2025 for "appointment scheduling, driver follow-up calls and warehouse coordination" (N-S34, snippets, *assumed*).
    - Qued sells AI appointment scheduling to brokers (N-S34).
    - This cuts both ways: agents lower the carrier side's friction with booking portals, but they also compete for the job.

**Item 6: addressable work**
- **Warehouse side: dock schedulers.** They sit inside two SOC codes (N-S01, *verified*):
  - 43-5071 shipping, receiving and inventory clerks: 816,870 nationally at a $46,810 mean, of whom 89,090 are in warehousing (NAICS 493) at $47,820;
  - 43-5061 production, planning and expediting clerks: 390,160 at $62,150.
  - Job postings show dock schedulers at $18-26 an hour (N-F62, illustration).
  - The share of these clerks' time spent on appointments is not measurable from these sources.
- **Freight-company side:** dispatchers (43-5032: 34,890 in truck transportation at $58,690) and broker operations reps (43-5011).
- **R22, text- and number-heavy office work?** Mixed.
  - Booking is calendar and message work, and planning clerks score 4.35 on computers and 1.99 on physical activity (N-S02).
  - But the costly part is physical: waiting trucks and a congested dock. Shipping and receiving clerks score 3.83 on physical activity.
  - Appointments save time only if the facility honours them. At LA/Long Beach, METRANS found "no evidence that the appointment system affected queuing" when terminals gave appointment trucks no priority (N-N02, *verified*).
- **R23, human connection:** not a key benefit **[our call]**. Booking a slot is a transaction; the telephone use (4.45-4.76 of 5) is the cost to remove.

**Item 7: budget holder and implementation**
- **Budget holder:** the DC or warehouse operations manager (within 11-3071, transportation, storage and distribution managers: 221,180 at $121,600, N-S01), paying from the site's operations budget (overtime, labour, detention charged back by carriers).
  - At a 3PL warehouse the cost can be passed on to the client **[our call]**.
  - Carriers bear most of the waiting, but they do not buy the facility's tool (card; N-C24).
- **Can it show value on day one and go live in weeks (R28)?**
  - **Data needed:** doors, hours, load types and booking rules, all held by the site. Carriers enter their own load details.
  - **Integration:** none is needed to start. A WMS link for purchase orders or ASNs is optional later.
  - **Go-live:** days to weeks **[our call]**. Carriers must be told to use the link.
  - **Day-one value:** fewer phone calls at once. A fall in detention takes weeks of data to show.

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors: at least 11** **[our count]**:
  - Opendock (Loadsmart); C3 Reservations (C3 Solutions, privately held, N-S41); DataDocks; GoRamp; LoadingCalendar; Velostics; Conduit; Transporeon (Trimble, *assumed*); Descartes (dock appointment scheduling in MacroPoint, N-S41); Dashdoc; Arrivy (N-F38, N-F47; mostly vendor lists, *assumed*).
- **Largest vendor's share:** no survey. On its own claim, Opendock reaches about 7% of sites [our calc]. **No vendor is near half of the target customers, so there is no dominance candidate.**
- **Service firms:**
  - 3PLs run appointments inside the warehouses they operate;
  - brokers' operations reps book appointments for carriers;
  - AI voice and email agents (HappyRobot, Qued) do it on the carrier side (N-S34).
- **Features inside larger products:**
  - WMS dock modules (Manhattan, Blue Yonder, Körber: *assumed*, not checked);
  - yard systems (C3 Yard; Kaleris: *assumed*);
  - TMS and visibility suites (Descartes MacroPoint, Transporeon).
- **How it is done today:** phone, email, shared spreadsheets or calendars, and first-come-first-served live unloading. "Doing nothing" means queues and detention. General-purpose AI agents are arriving on the carrier side.
- **How incumbents charge (evidence only):**
  - per facility, from $99 a month to about $7,000 a year (N-F38, vendor, *assumed*);
  - carriers usually book free (*assumed*);
  - AI agents' pricing was not found.

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **0.5** | The booking is office work, but the cost it removes (waiting at the dock) is physical, and it falls only if the site honours slots (N-N02) |
| A3 | **0.5** both sides | A known cost (detention at 39.3% of stops; drivers' #5 issue) with no rule or retailer mandate. The carrier side feels more pain but does not buy; tie |
| A6 | **1** | Several adjacent groups: yard management; detention billing (C-03); load status (C-02); lumper payments; a carrier-side booking network across sites; manufacturers' and cold-storage docks |
| W1 | **0.5** both sides | Warehouse side: dispersed sites reached through associations (IWLA, WERC, grocery groups) and through carriers, who see the tool whenever they book. Carrier side: dispersed. Tie; the warehouse side pays |
| W3 | **1** | Data at hand: the site's own doors and hours are enough to go live, and APIs exist for later links |
| W4 | **0.5** | Proven spend: yes (per-facility subscriptions, clerk time, detention paid). Weak or missing software: no; 11+ vendors, API-first and AI-ready |
| W5 | **0.5** both sides | Neutral: no mandate. Carriers' dislike of booking portals is plausible but was not sourced |
| W6 | **0.5** | A simple product, but a two-sided network race against funded players (Opendock/Loadsmart; AI-agent firms valued at $1B+) |

### 2.2 C-15 · Routing own delivery fleets (food, beverage and industrial distributors)

**Item 5: software penetration and why now**
- **Share of distributors or private fleets that plan routes by hand: no neutral figure found** after three attempts (§5).
  - NPTC's 2025 Benchmarking Survey (104 companies, mostly large private fleets; NPTC flag) is members-only. Two public summaries were read:
    - FleetOwner lists only safety technology: "in-cab cameras (88%)", "speed monitoring (86%)", "collision warning (83%)" (N-S03, page extraction, secondary).
    - Penske: "Nearly three-quarters reported adoption of a broad range of technologies" (N-S04, vendor summary, *assumed*).
    - Neither gives a routing-software line.
  - Vendor compilations say 70% of fleets use "some form of fleet management technology", and a Geotab survey says 63% of fleet managers who use telematics rank route optimisation as their top priority (search snippets, vendor, *assumed*, not used).
- **Beer distributors: one system of record may hold most of them.**
  - VIP (Vermont Information Processing) serves "1,000 distributors and 800 suppliers", as of 16 Oct 2019 (Seven Days, N-S28, page extraction, secondary).
  - A search snippet quotes VIP: its "route accounting system supports more than 50 percent of the beer volume in the U.S." (N-S29, *assumed*; the source pages did not show it or returned 403).
  - Census SUSB 2022 counts **1,393 beer and ale wholesaler firms** (424810) and 2,238 wine and spirits wholesalers (424820) (N-D04 re-parsed, *verified*).
  - **If most of VIP's 1,000+ distributors are beer wholesalers, VIP serves well over half of them** **[our calc; the upper bound is about 72%; VIP also serves wine, spirits and soft-drink distributors]**.
  - VIP's site lists a "BizStride Logistics" product with "Routing" (N-S30, vendor, *assumed*). Whether VIP's routing module (not only its route accounting) is what beer distributors use to route was not found.
- **Systems of record and plumbing (R30):**
  - the distributor's ERP or route accounting (VIP for beverages; others *assumed*), which holds orders, customers and invoices;
  - driver handhelds;
  - telematics and ELDs (electronic logging devices);
  - the routing engine.
  - Orders and addresses exist as ERP exports (CSV). Telematics vendors commonly offer APIs (*assumed*). Plumbing test: **passes, with integration**.
- **Triggers for change now: none that forces action.**
  - The driver shortage dropped out of ATRI's top-10 industry issues in 2025 "for the first time in the survey's history" (#12; R38, *verified*). Private-fleet driver turnover is 18.4%, against a 15-year average of 14.5% (N-S03).
  - **CARB voted on 25 Sep 2025 to repeal** the Advanced Clean Fleets rules for high-priority and drayage fleets, with repeal expected to take effect 1 Jan 2027. Enforcement has been paused since November 2023 (N-S19, snippets, *assumed*). The California electric-truck mandate on private fleets is therefore no longer a trigger.
  - Cost pressure is steady, not new: NPTC fleets report "$3.81 per mile" (N-S03). Route optimisation marketed as AI is a vendor claim.

**Item 6: addressable work**
- **Planners** (N-S01, *verified*):
  - dispatchers (43-5032): 202,810 nationally at $54,740; 4,550 in nondurable-goods wholesale at $59,350; 7,120 in durable-goods wholesale at $57,160; 480 in food manufacturing;
  - some route planners sit in 43-5061 (planning clerks).
- **Where the saving lands: driver hours, miles and trucks.**
  - Heavy truck drivers (53-3032): 174,610 in nondurable wholesale at $61,250.
  - Driver/sales workers (53-3031): 91,800 in nondurable wholesale at $52,030.
  - S2's pool used 2-5% of fleet cost (`2_knockouts.md` §4.1).
- **R22, text- and number-heavy office work?** The planning is number-heavy optimisation (dispatchers: computers 4.12, physical 1.84; N-S02), but the cost removed is physical: miles, hours and trucks.
- **R23, human connection:** partly a key benefit.
  - Driver/sales workers score 4.60 on face-to-face contact and 4.36 on physical activity (N-S02).
  - In beverage distribution the route and its driver often *are* the customer relationship: shelf service and ordering **[our call]**.
  - Re-planning routes touches that relationship, which R23 warns against ("delivering on a core product").

**Item 7: budget holder and implementation**
- **Budget holder:** the distributor's VP of operations, transportation manager or fleet manager (11-3071), paying from the fleet operating budget (drivers, fuel, trucks). The distributor both pays and saves (card).
- **Data needed:** daily orders, geocoded addresses, delivery windows, truck capacities and driver hours. These are held in the ERP or route-accounting system.
- **Integration:**
  - CSV import is enough for a trial on past orders (a "lightweight cost savings assessment", R28) **[our call]**;
  - live daily use needs a two-way link to the ERP or route accounting (load sheets, invoices, handhelds).
- **Go-live:** weeks for a standalone planner; months where route accounting and handhelds must change **[our call]**.
- **Day-one value:** plausible as a re-plan of last month's orders showing miles saved. Realised savings need drivers to follow the plan.

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors: 20+** **[our count]**:
  - Gartner's routing market guides list Descartes, Roadnet (Omnitracs), Trimble TMW, Paragon, WorkWave, ORTEC, Oracle, SAP, Manhattan, Blue Yonder, MercuryGate, Geoconcept, Cheetah, Carrier Logistics and others. The 2023-25 guides add FarEye, Onfleet, nuVizz, Kardinal and EPG, and also evaluate Aptean, Bringg, DispatchTrack and Locus (N-S31, via vendors' announcements, *assumed*).
  - Plus SMB tools on the card: OptimoRoute and Routific. Plus VIP (BizStride) for beverages (N-S30).
- **Largest vendor's share:**
  - no survey;
  - a tech-tracking site puts Roadnet at "0.4% market share" of a broad fleet category (N-S32, *assumed*, not meaningful);
  - a competitor calls Roadnet "notoriously complicated" (N-S32, competitor claim, *assumed*).
- **Dominance:**
  - **for the card as a whole: none shown;**
  - **for the beer-distributor segment: VIP is a show-stopper candidate** for the route-accounting job, and possibly for routing. It needs a check of which routing tool beer distributors actually use, and whether they are satisfied (S5).
- **Service firms:**
  - dedicated contract carriage, which takes over the fleet: $32.0B in 2025 (R33);
  - for-hire truckload and LTL.
- **Features inside larger products:** routing add-ons in telematics platforms (Samsara, Motive, Geotab: *assumed*); ERP and route-accounting modules (VIP); TMS routing (MercuryGate, Blue Yonder).
- **How it is done today:** fixed routes kept by experienced dispatchers, spreadsheets, maps, and older desktop routing installs (card; N-S32). "Doing nothing" means keeping static routes.
- **How incumbents charge (evidence only):** per vehicle or per driver per month for SaaS routing, and enterprise licences for suites (*assumed*; no price page was read in this check).

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **0.5** | Number-heavy planning, but the cost removed is physical (miles, hours, trucks) and the removable share is small (2-5%) |
| A3 | **0.5** shipper side (distributor); **0** other side (receiving docks feel little) | A known cost with no forcing event: the driver shortage is off ATRI's top 10, and CARB's fleet rule is being repealed. Better side: distributors |
| A6 | **1** | Several adjacent groups: proof of delivery, driver apps, customer arrival notices, route accounting; other private fleets (building materials, propane and milk hauling; the last two are reserve cards C-38 and C-32); field service |
| W1 | **0.5** | Partial channels: NPTC; NBWA ("over 5,000 engaged distributor leaders", N-S27); food-distributor associations (*assumed*). Beer is reachable through VIP's ecosystem only as a partner |
| W3 | **0.5** | Integration needed: ERP orders, addresses, handhelds and route accounting |
| W4 | **0.5** (beer segment: show-stopper candidate) | Proven spend: yes (dispatch staff, routing licences, $32.0B of dedicated carriage). Weak or missing software: no; 20+ vendors, many of them modern SaaS. Legacy only in parts (a competitor's claim) |
| W5 | **0.5** | Neutral: no mandate. Possible resistance from driver-sales reps who "own" routes (*assumed*, not sourced) |
| W6 | **0.5** | Moderate: routing algorithms are a mature, crowded category, and incumbents sit inside ERPs and telematics |

### 2.3 C-18 · Warehouse storage and handling bills (small public and contract warehouses)

**Item 5: software penetration and why now**
- **Neutral adoption or leakage survey: none found.** Check N's three tries (IWLA; WERC and academic; public 3PL filings) are not repeated here.
- **Vendor surveys only (all *assumed*):**
  - Extensiv's *4th Annual 3PL Warehouse Benchmark Report* (19 Oct 2023; "more than 240 3PL warehouses"; N-S14):
    - "Seventy percent (70%) of respondents cited increased labor costs";
    - "over half (53%) indicate that labor makes up more than 40% of overall business costs".
  - Extensiv billing pages (N-S16, snippets):
    - "82% of 3PL warehouses lose revenue to uncaptured monthly shipping, receiving & storage charges";
    - the 2025 benchmark (200+ warehouses) shows 7 points more respondents citing uncaptured charges, and 10 points more citing a lack of billing automation, than the year before.
  - Check N also records Extensiv's 2025 survey naming uncaptured charges as the top billing challenge, cited by 56%.
  - Every one of these surveys is run by a WMS vendor that sells the fix.
- **WMS use as a proxy:** 63% of companies use a WMS (Peerless Research Group 2025, N-S37, snippet, *assumed*). The sample leans to larger firms, while 53% of general-warehouse firms have under 20 staff (N-F01).
  - **So a large share of small public warehouses may bill from spreadsheets with no WMS at all** **[our call; not measured]**.
- **Systems of record and plumbing (R30):**
  - the WMS: receipts, picks, storage snapshots and extra-service events;
  - customers' EDI orders and advices (*assumed*);
  - the accounting package (Extensiv integrates with QuickBooks, N-S15);
  - the rate sheets in each customer's contract, often PDFs or spreadsheets.
  - Plumbing test: **passes where a WMS exists** (exports or the vendor's integrations); it fails for paper-based sites.
- **Triggers for change now: none found.**
  - No regulation or customer mandate.
  - Labour-cost pressure is the only named driver (N-S14, vendor).

**Item 6: addressable work**
- **Roles** (N-S01, *verified*):
  - billing and posting clerks (43-3021): 404,060 nationally at $51,070, but only 1,160 in warehousing (NAICS 493) at $46,290;
  - bookkeeping clerks (43-3031): 4,130 in warehousing at $52,560;
  - shipping, receiving and inventory clerks (43-5071), who record the billable events: 89,090 in warehousing at $47,820.
  - Reading: in small warehouses billing is a part-time task of the owner, office manager or bookkeeper **[our call]**.
- **R22, text- and number-heavy office work? Yes.**
  - Billing clerks score 4.67 on computers and 1.60 on physical activity (N-S02).
  - The leakage is an information problem: events not recorded or not matched to the rate sheet.
- **R23, human connection:** not a key benefit. Billing clerks have the lowest "interpersonal relationships" rating in this check (2.73, N-S02).

**Item 7: budget holder and implementation**
- **Budget holder:** the warehouse owner or general manager, or the controller, paying from the finance and administration budget.
  - Recovered charges add straight to revenue, so the payer is the saver.
  - On the customer side, the seller's operations lead only audits.
- **Data needed:** WMS event history and storage snapshots, plus each customer's rate sheet.
- **Integration:** a WMS export or API; where there is no WMS, event capture has to be built (which amounts to a WMS).
- **Go-live:** weeks where a WMS export exists **[our call]**.
- **Day-one value:** plausible. A look-back audit of 3-12 months of events against contracts can show unbilled charges quickly. Vendors market exactly this (N-K27, vendor).

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors: at least 9** **[our count]**:
  - 3PL WMSs with billing modules: Extensiv (formerly 3PL Central), Deposco, Logiwa, Camelot, Magaya, Datex (card);
  - billing-leakage specialists: Sequoia, Xorosoft, Packem (N-K27, vendor, *assumed*).
- **Largest vendor's share:**
  - Extensiv 3PL Warehouse Manager says "1,500+ 3PLs and counting" (N-S15, vendor, *assumed*).
  - Census counts 6,789 general-warehousing firms and 680 refrigerated-warehousing firms: 7,469 in all (N-D04 re-parsed, *verified*).
  - So Extensiv reaches **at most about 20%** of them **[our calc]**, and less if its count includes non-US and fulfilment-only customers.
  - **No dominance.**
- **Service firms:** outsourced bookkeeping (*assumed*); customer-side audits of 3PL invoices (vendor guides only).
- **Features inside larger products:** billing modules in every 3PL WMS ("Automate Billing", "Send invoices in minutes", N-S15), and ERP billing (*assumed*).
- **How it is done today:** WMS reports or paper logs copied into spreadsheets, then invoices in QuickBooks. "Doing nothing" means leakage.
- **How incumbents charge (evidence only):** WMS subscription tiers (Extensiv shows "Enterprise" and "Professional" tiers but no prices, N-S15); per warehouse or per user (*assumed*).

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **1** | Text- and number-heavy office work drives the cost: matching recorded events to rate sheets |
| A3 | **0.5** warehouse side; **0.5** customer side | A known cost, on vendor evidence only, with no forcing event. Tie |
| A6 | **0.5** | One or two adjacent steps: inventory visibility for the warehouse's customers; auditing 3PL invoices from the customer side. Going deeper means competing with the WMS itself |
| W1 | **0.5** warehouse side; **0** customer side | Partial: IWLA (membership size not found), WMS partner marketplaces, dispersed small firms. Better side: warehouses |
| W3 | **0.5** | Integration needed: WMS event data plus rate sheets |
| W4 | **0.5** | Proven spend: yes (clerk and owner time, WMS subscriptions). Weak or missing software: not shown. Modern 3PL WMSs bill automatically; the gap is sites without a WMS, which is not measured |
| W5 | **0.5** | Neutral on neutral evidence. Vendor surveys show rising concern about uncaptured charges (+7 points), which would lean to 1 if confirmed in S5 |
| W6 | **0.5** | Moderate: a billing layer needs links to many WMSs, or else it competes with WMS vendors directly |

### 2.4 C-19 · Retailer OTIF fines and deductions (small and mid-sized suppliers to big-box retailers)

**Item 5: software penetration and why now**
- **A neutral adoption figure exists, though dated:** the CRF *2018 Customer Deduction Survey* (N-N29, re-read pp. 26-37, *verified* PDF text; CRF flag, run by Attain Consulting Group; 203 companies, 52% with sales of $500M or less).
  - "Use of 3rd Party Technologies": **44% use, 56% do not**. By size: **30% of firms with sales of $500M or less** use it, against 58% of larger firms. So **70% of the smaller suppliers used no third-party deduction technology** [our calc].
  - "Do you Outsource any Deduction Management Tasks?": **9% yes**. That is **0% of firms at $500M or less** and 18% of larger ones.
    - The text extraction labels the other slice 94%, probably 91%.
    - Those who outsource hand out mainly "Collection / recovery of invalid claims (42%)".
  - **Dispute windows:**
    - 74% usually finish on time;
    - 14% are often late but the customer still accepts;
    - 6% are often late and the customer "WILL NOT accept";
    - 6% "just write off".
  - **Biggest internal challenge:** 41% name cross-departmental cooperation (our reading of the chart); the other slices are 21%, 21%, 11%, 3% and 3%.
  - 27% felt that "new compliance rules or deduction types were being created".
  - ERP: "61% of responding companies with revenue > $500 million use SAP ... as compared with 18% reported by smaller companies".
  - Caveat: the survey is from 2018. Vendors have multiplied since, e.g. SupplyPike's growth (below).
- **Systems of record and plumbing (R30):**
  - retailer portals: Walmart Retail Link, Target, Amazon Vendor Central, Home Depot;
  - EDI 812 (adjustments), 820 (remittance) and 856 (ASN);
  - the supplier's ERP receivables;
  - carriers' and 3PLs' portals holding PODs and bills of lading.
  - **Retailer portals are reached by credentials and bots, not open APIs:**
    - iNymbus uses robotic process automation to "read retailer portals, gather and prepare complete claims packages, and upload them" (N-S36, vendor, *assumed*);
    - SPS "connects directly to Retail Link, your carrier and 3PL portals, and file storage systems" (N-S11, vendor, *assumed*).
  - Plumbing test: **passes with integration effort**, one retailer at a time.
- **Triggers for change now: retailer rules with dates.**
  - **Walmart, from 1 Feb 2024:**
    - "the new OTIF targets became 90% for on-time and 95% for in-full", replacing a 98% OTIF goal in force since Sep 2020 (Logistics Viewpoints, 5 Feb 2024, N-S13, page extraction, secondary);
    - fines are charged quarterly instead of monthly (N-S12, vendor, *assumed*);
    - the fine stays 3% of the cost of goods on each case in violation (N-E24, N-E26, N-S13).
    - An Uber Freight executive says "Walmart suppliers are currently paying 0.16% of the cost of goods sold in fines to Walmart" (N-S13, *assumed*: an interested party).
  - **Target, Q3 2024:** "on time and fill rate fines from 5 percent to 3 percent of cost of goods sold"; fill rate measured by item instead of by order; the prepaid on-time window set to one day either side (SPS webinar page, 10 Dec 2024, N-S12, vendor, *assumed*).
    - **Conflict:** another vendor snippet says Target's revision in Aug 2024 reintroduced a 95% fill-rate standard with a 5% penalty and a $150 minimum (N-S40, *assumed*). The current terms are unsettled here.
  - **Home Depot, 2024:** disputes moved from quarterly to monthly, and the 12-month dispute window now runs from the invoice date. **Amazon** now lets suppliers re-dispute shortage claims (N-S12, vendor, *assumed*).
  - **Reading [our call]:** the fines recur every quarter under rules each retailer can change at will, which works like a standing mandate. Walmart's 2024 change *eased* its on-time goal, which lowers urgency at the largest retailer.
  - **Market event:** SPS Commerce bought SupplyPike on 1 Aug 2024 for about $206M ($119M cash and $87M in stock) and expected about $25M of 2025 revenue from it (N-S10, company release, *verified* at source for the company's statements). A public company is paying up for the job.

**Item 6: addressable work**
- **Roles** (N-S01, *verified*):
  - deductions analysts, within bill and account collectors (43-3011: 158,830 at $49,060) and credit analysts (13-2041: 64,390 at $100,850);
  - logistics managers and logisticians (13-1081: 251,040 at $89,730) for prevention.
- **R22, text- and number-heavy office work? Yes.** The work is matching deduction codes to purchase orders, ASNs, PODs and contracts, then filing a packet in a portal. Credit analysts score 4.45 on computers and 1.25 on physical activity; collectors 4.16 (N-S02).
- **R23, human connection:** mostly not a key benefit for the dispute packet **[our call]**. Collections carry some relationship work (interpersonal 3.58-3.75), but retailers' portals are designed to be impersonal.

**Item 7: budget holder and implementation**
- **Budget holder:** the supplier's CFO or controller, or its credit manager.
  - Recoveries return to revenue from the receivables budget. Prevention sits with the logistics manager.
  - The payer is the saver.
  - Recovery firms are paid out of what they recover (below), a model close to the project's fee rule (evidence only; F-7 and F-8 are deferred).
- **Data needed:**
  - deduction lines (portal and EDI 812/820);
  - purchase orders and ASNs (ERP and EDI 856);
  - PODs and bills of lading (carrier and 3PL portals).
- **Integration:** portal credentials and bots per retailer, plus an ERP export.
- **Day-one value: yes, plausibly.**
  - Open deductions still inside the dispute window (12 months at Home Depot, N-S12) can be disputed at once.
  - Vendors lead with a "complimentary audit" (N-S11), which is R28's "lightweight cost savings assessment".
- **Go-live:** weeks per retailer **[our call]**.

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors: at least 7** **[our count]**:
  - SPS Commerce Revenue Recovery (formerly SupplyPike), iNymbus, HighRadius, Vendormint, RetailPath, DOSS (N-F55, N-S35, N-S36; vendor, *assumed*);
  - ClearChain, which sells a flat-fee service (N-S35).
- **Largest vendor's share:**
  - SPS says it has "recovered more than $700 million for Walmart suppliers" (N-S11, vendor, *assumed*) and expected about $25M of 2025 revenue from SupplyPike (N-S10).
  - No customer count was found: SPS's FY2025 10-K could not be downloaded (§5).
  - **Share unknown; no dominance shown.** SPS is the one to watch, because it already carries many suppliers' EDI (*assumed*).
- **Service firms:**
  - contingency recovery firms: Vendormint charges "a 30% contingency fee on recovered revenue"; STAT Recovery; Woodridge Retail Group; Smyyth (N-S35, vendor, *assumed*);
  - retail consultancies such as 8th & Walton (N-F37);
  - carriers and brokers, who supply the delivery proof.
- **Features inside larger products:** ERP deduction modules (SAP, used by 61% of CRF's larger respondents); accounts-receivable automation suites (HighRadius).
- **How it is done today:**
  - in-house analysts with spreadsheets, and 70% of smaller suppliers with no third-party tool (2018);
  - write-offs: 6% "just write off" late items;
  - CRF: 6-10% of deduction dollars are invalid, and 60% of the invalid dollars are recovered (N-N29, via check N).
- **How incumbents charge (evidence only):**
  - a contingency share of recoveries, e.g. 30% (Vendormint);
  - a flat monthly fee, e.g. $5,000 a month (ClearChain, N-S35);
  - subscriptions (*assumed*).

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **1** | Office work drives the cost: document matching and portal filing |
| A3 | **1** supplier side; **0.5** carrier side | Supplier side: retailer rules with dates (Walmart 1 Feb 2024; Target Q3 2024; Home Depot 2024) and fines every quarter. It leans to 0.5 if "forcing event" must mean a new tightening, since Walmart's 2024 change eased its target. Better side: suppliers |
| A6 | **1** | Several adjacent groups: more retailers (iNymbus covers "51+"); trade-promotion deductions; freight claims (C-10); freight bill audit (C-09); ASN and EDI accuracy; foodservice distributors as suppliers |
| W1 | **0.5** both sides | Partial: suppliers gather around retailer ecosystems (Walmart's supplier community, consultancies, SPS's network) and CRF, with no single channel |
| W3 | **0.5** | Integration needed: bots per retailer portal, ERP and EDI data, carrier PODs. Back-claims make time to value short |
| W4 | **1** | Both hold for the card's small and mid-sized suppliers: proven spend (analysts; 30% contingency firms; SPS's $25M line), and software missing for most (70% used none; CRF 2018). **Leans 0.5** if S5 finds SPS or others now widely used; the adoption figure is from 2018 |
| W5 | **1** supplier side; **0.5** carrier side | Evidence of the wish to change: suppliers already hand recovery to contingency firms, and SupplyPike's revenue was expected to triple from 2024 to 2025 ($8M to $25M, N-S10) |
| W6 | **0.5** | Moderate: portal bots must be built retailer by retailer, and a funded incumbent (SPS) owns the EDI relationship |

### 2.5 C-20 · Import entries, for small importers (customs brokers' entry writers)

**Item 5: software penetration and why now**
- **Filing is already electronic; the manual work sits before it.**
  - CBP's burden estimate counts **23,133,408 electronic formal entries a year at 5 minutes each**; paper filing takes 20 minutes (N-N05, *verified*).
  - Every broker files through ABI software, from a list of about 70 vendors (N-F10).
  - The remaining manual work is classifying goods under the HTS, valuing them, and keying data from the importer's invoices and packing lists (PDFs and email) into the filing software (N-F61, illustration).
- **Brokers' own view** (Descartes 2025 benchmark study; 434 forwarders and customs brokers across four regions, run with seven associations including NCBFAA; 4 Nov 2025; N-S20, vendor survey, *assumed*; NCBFAA flag):
  - "25% cited manual workflows as the top inhibitor to growth";
  - "55% of respondents plan to prioritize AI investment over next two years";
  - 67% see technology as "fundamental or highly important to growth".
- **Systems of record and plumbing (R30):**
  - **ACE via ABI**, a standard EDI interface open to certified software (N-F08 describes ABI as "a voluntary program available to brokers, importers, carriers, port authorities and independent service centers", *verified*);
  - the **ACE Portal**, where importers and brokers file IEEPA refund claims (N-S05);
  - **HTS data through a public REST endpoint**: a direct query of `hts.usitc.gov/reststop/search` returned JSON duty rates (N-S33, *verified*);
  - CBP rulings (CROSS);
  - the importer's invoices as documents.
  - Plumbing test: **passes**, with the strongest open data of the six cards. The catch is that filing needs a certified ABI connection, or a partner that has one.
- **Triggers for change now (dated):**
  1. **The end of de minimis on 29 Aug 2025** (N-J29). Informal entries went from 5.16M (FY2024) to 15.40M (FY2025) and 63.24M in FY2026 to date. Formal entries rose 31.9M → 33.2M → 34.7M from FY2023 to FY2025 (N-H22, via check N).
  2. **The IEEPA tariffs ruled unlawful.**
     - The Supreme Court ruled on 20 Feb 2026 that "IEEPA does not confer authority to impose tariffs".
     - On 4 Mar 2026 the Court of International Trade ordered CBP to liquidate and reliquidate entries without IEEPA duties.
     - Importers or their brokers claim refunds through **CAPE** in the ACE Portal, which opened for its first phase on 20 Apr 2026.
     - The scale: about **$165-166B of duties on "over 53 million" entries from "more than 330,000" importers** (Skadden, Mar 2026, N-S05, law-firm summary, *assumed* until seen in CBP's filings).
     - By 11 May 2026, 126,237 refund claims had been submitted (N-S06, snippet, *assumed*).
  3. **Technology:** AI classification tools aimed at brokers (TariffLens; Gaia Dynamics, whose engine was tested against the broker licence exam in April 2025), and CBP's own Cargo Classification Tool (N-S38, vendor snippets, *assumed*).

**Item 6: addressable work**
- **Roles** (N-S01, *verified*):
  - customs brokers sit within compliance officers (13-1041): 4,520 in freight transportation arrangement at $72,420;
  - entry writers are mostly counted as cargo and freight agents (43-5011): 53,390 in freight arrangement at $57,570.
- **Licensed population** (N-F08, CBP's 2022 broker rule, *verified*):
  - "15,226 active, licensed customs brokers";
  - "As of January 2022, there are **2,365 permitted brokers**", about 15.5% of all brokers, since "the majority of brokers ... work under the auspices of a corporate permit";
  - "Approximately two percent of brokers hold a corporate permit".
  - A directory snippet puts active licences at about 11,400 (N-S42, *assumed*), which conflicts with CBP's 2022 figure.
- **R22, text- and number-heavy office work? Yes, the most of the six cards.** Customs brokers score 4.47 on computers, 4.32 on processing information, 4.85 on "importance of being exact" and 1.44 on physical activity (N-S02).
- **R23, human connection:** partly. Importers value a broker's advice and the licence's liability cover (*assumed*), but the classification and keying are not relationship work **[our call]**.

**Item 7: budget holder and implementation**
- **Two budget holders:**
  - **Broker side:** the brokerage owner or licensed broker, paying from the operations or IT budget. Filing software is usage-based ("Only charge you when you use the software", CargoWise, N-A39), so a per-entry saving fits how brokers already buy.
  - **Importer side:** the owner or logistics lead, who pays broker fees per entry as part of landed cost.
- **Data needed:**
  - commercial invoices and packing lists (PDFs held by the importer or broker);
  - HTS and rulings (open);
  - the broker's past entries (in the ABI software).
- **Integration:**
  - an extraction and classification co-pilot can run on documents with **no integration**, and its value (minutes per entry) shows on day one **[our call]**;
  - pushing data into filing needs the broker's ABI software API, or CBP certification as an ABI vendor (months: *assumed*).
- **Whole-product catch:** only a licensed broker or a self-filing importer can file. A product sold to importers directly must bring a broker.

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors:**
  - about **70 on CBP's ABI list** (N-F10);
  - notable ones: CargoWise (WiseTech), Descartes (NetCHB and other brands), Magaya, E2open, CustomsCity, KlearNow (card);
  - AI classification add-ons: TariffLens, Gaia Dynamics, Cervo (N-S38).
- **Largest vendor's share:**
  - NetCHB: "More than 700 customs brokers" use it (Descartes acquisition release, 10 Feb 2022, N-S09, vendor, *assumed*; price "$40 million" plus up to "$60.0 million" earn-out).
  - Against **2,365 permitted brokers** in Jan 2022 (N-F08), that is **about 30%** **[our calc; the two counts may define "broker" differently]**.
  - Snippets add "45% of all Type 86 filings", the de minimis entry type now ended, and name CargoWise, Descartes OneView and NetCHB as the three most-used ABI systems (N-S43, *assumed*).
  - **No vendor shown above half: no dominance.**
- **Service firms:**
  - customs brokerages themselves: NCBFAA "represents more than 1500 member companies with 110,000 employees in international trade" (N-S26; NCBFAA flag);
  - forwarders (Expeditors' customs brokerage revenue rose 12.9% with the 2025 tariffs, N-C13);
  - parcel carriers' in-house brokerage (*assumed*).
- **Features inside larger products:** forwarding suites (CargoWise), trade-compliance modules in ERPs (*assumed*), e-commerce duty tools (*assumed*).
- **How it is done today:** entry writers key invoice data into ABI software and look classifications up in the HTS and rulings. **"Doing nothing" is not an option:** an entry is required by law.
- **How incumbents charge (evidence only):**
  - broker fees per entry, $100-250 in vendor price guides (check N, *assumed*);
  - usage-based filing software (N-A39);
  - AI tools: subscriptions (*assumed*).

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **1** | The most text- and number-heavy role in this check (classification, valuation, data entry) |
| A3 | **1** broker side; **1** importer side | Dated forcing events: de minimis ended 29 Aug 2025; IEEPA ruling 20 Feb 2026; CAPE refunds from 20 Apr 2026 on 53M+ entries. Tie; brokers carry the workload |
| A6 | **1** | Several adjacent groups: importer security filings; other agencies' filings; duty drawback; post-entry corrections and refunds; export documents (reserve C-24); Mexico cross-border (reserve C-25) |
| W1 | **1** broker side; **0** importer side | A small, organised buyer set: 2,365 permit holders (2022), NCBFAA with 1,500+ member companies and nine regional areas, and CBP's ABI vendor list as a shop window. The 240,535 importers are dispersed (N-E18). Better side: brokers |
| W3 | **0.5** | Integration needed to file (ABI software API or certification). A document co-pilot has its data at hand, so the wedge could score higher |
| W4 | **0.5** | Proven spend: yes (per-entry broker fees; filing software). Weak or missing software: not shown. About 70 vendors, two consolidators (WiseTech, Descartes) and AI entrants; "legacy" is not sourced |
| W5 | **1** broker side; **0.5** importer side | Evidence of the wish to change: 55% plan to prioritise AI and 25% name manual workflows as the top inhibitor (vendor survey with NCBFAA), under volume shocks |
| W6 | **0.5** | Moderate: licensing, liability and ABI certification, plus fast-moving AI entrants and consolidators. **Leans 0** if the product must file entries itself; **leans 1** for a co-pilot wedge |

### 2.6 C-22 · Port drayage dispatch (small drayage carriers)

**Item 5: software penetration and why now**
- **How much still runs by phone and spreadsheet:**
  - A Harbor Trucking Association and TradeLanes survey (1 Feb 2021; sample size not stated; N-S24, association and vendor; HTA flag): "Eighty percent (80%) of members report that carriers still aren't leveraging technology to resolve these issues", meaning demurrage and detention.
    - Auditing and disputing took about 45 minutes per invoice.
    - "No Appointment Available" was the most-cited dispute reason.
  - WiseTech calls the sector "an intensely complex and highly fragmented ecosystem" (N-S21).
  - **Firm structure:** 43,571 local general-freight trucking firms (484110), of which **34,331 have under 5 employees** (N-D04 re-parsed, *verified*). 48,991 interstate carriers tick "intermodal containers" (N-F02). The LA/Long Beach registry holds 23,000+ trucks (N-F21).
  - Many buyers are one-truck or few-truck operators.
- **Systems of record and plumbing (R30):**
  - terminal appointment systems, mainly eModal (Advent Intermodal). Gloucester Terminal made it the required system from 11 Mar 2026. Terminals also collect fees through it; Oakland's export gate fee must be "claimed via eModal" (N-S39, snippets, *assumed*);
  - terminal websites and the LA port's data portal (Port Optimizer);
  - chassis-pool portals (*assumed*);
  - delivery orders from importers and forwarders (email and PDF);
  - container-tracking APIs (Terminal49, Vizion; N-F54).
  - Plumbing test: **passes with heavy integration**. The data exists, but it is split terminal by terminal and pool by pool. Vendors such as PortPro and Envase built these links (N-S23, N-S21).
- **Triggers for change now: no positive forcing event found.**
  - **CARB's drayage zero-emission rule is being repealed.** Since 1 Jan 2024, new trucks added to the registry had to be zero-emission. CARB voted on 25 Sep 2025 to repeal the requirement, effective 1 Jan 2027, with no enforcement since Nov 2023 (N-S19, snippets, *assumed*). A compliance trigger has gone.
  - **The FMC's billing rule** (mostly effective 28 May 2024) says a demurrage or detention bill must go to the party that contracted for the transport, or to the consignee (N-F32). That moves some of these bills away from truckers.
  - Tariff-driven import swings in 2025 were not measured here.

**Item 6: addressable work**
- **Roles** (N-S01, *verified*):
  - dispatchers (43-5032): 34,890 in truck transportation at $58,690 (drayage cannot be separated out);
  - heavy truck drivers (53-3032): 900,880 in trucking at $61,540.
- **R22, text- and number-heavy office work?** Mixed.
  - Dispatch is phone-heavy office coordination (dispatchers: telephone 5.00, face-to-face 4.97, repeat-same-tasks 4.50; N-S02).
  - But the cost to remove is truck time at terminals: waiting and dry runs.
  - A dispatcher controls only part of that. METRANS found appointment savings depend on terminals giving priority and having cargo ready (N-N02, *verified*).
- **R23, human connection:** partly. The dispatcher-driver relationship matters in owner-operator fleets (*assumed*), but booking and checking availability do not need it.

**Item 7: budget holder and implementation**
- **Budget holder:** the drayage company's owner or operations manager, from a thin operations budget. Importers pay the per diem and extra charges.
- **Data needed:**
  - orders (delivery orders);
  - container availability and holds at each terminal;
  - appointments;
  - chassis;
  - driver positions.
- **Integration:** needed with each terminal's appointment system or eModal, chassis pools and customers.
  - PortPro advertises "AI-based order entry" and "integrations for other supply chain participants" (N-S23, *assumed*).
- **Go-live:** weeks per port if the integrations already exist; longer to build them **[our call]**.
- **Day-one value:** fewer phone calls and portal checks. A fall in dry runs shows within weeks.

**Item 9: competitors, substitutes and the incumbent map**
- **Named software vendors: at least 7** **[our count]**:
  - **CargoWise Landside (WiseTech Global)**, which combines Envase and Trinium (N-S22, *assumed*). Envase itself bundles the Profit Tools, Compcare, GTG and DrayMaster products (search snippets, *assumed*);
  - PortPro;
  - TMSEZ (snippet);
  - general trucking TMSs (McLeod, Trimble TMW: *assumed*);
  - appointment and visibility helpers: Terminal49, Vizion, BlueCargo (N-F54).
- **Largest vendor's share:**
  - WiseTech bought Envase on 24 Jan 2023 for **US$230M**. Envase's "more than 1,300 customers across North America include trucking companies, ports, depots, and warehouses", with about "US$35 million of revenue" expected for 2023 (N-S21, company release, *verified* at source for the company's statements).
  - Against 43,571 local-trucking firms, 1,300 customers of all types is **at most about 3%** **[our calc]**. The denominator is mostly owner-operators, so the share among port fleets that use a TMS is unknown and could be much higher.
  - PortPro raised a $12M Series A in Jan 2023 and gives no customer count (N-S23).
  - **No dominance shown.** WiseTech is the consolidator to watch.
- **Service firms:** drayage brokers and intermodal marketing companies; dispatch services for owner-operators (*assumed*).
- **Features inside larger products:** eModal's own tools on the terminal side; general trucking TMSs.
- **How it is done today:** phone, terminal portals, spreadsheets and whiteboards (card; vendor snippet). "Doing nothing" means dry runs and waiting.
- **How incumbents charge (evidence only):**
  - TMS subscriptions (*assumed*);
  - eModal charges vary by terminal and service, and are not published (N-S39, *assumed*).

**The eight rows [our call]**

| Row | Suggested | Reason |
|---|---|---|
| A2 | **0.5** | Mixed: coordination is office work, but the cost is truck time at terminals, largely outside the dispatcher's control (N-N02) |
| A3 | **0.5** carrier side; **0.5** importer side | A known cost with no forcing event. CARB's repeal removes one trigger, and the FMC rule shifts demurrage and detention bills away from truckers. Tie |
| A6 | **0.5** | One or two adjacent steps: billing extras and per-diem disputes (overlapping the dropped C-21); rail-ramp drayage and other ports |
| W1 | **0.5** carrier side; **0** importer side | Partial: buyers cluster at about ten port complexes. HTA represents drayage carriers at LA, Long Beach, Oakland and Seattle/Tacoma only (N-S25), and every LA/LB truck is on one registry (N-F21) |
| W3 | **0.5** | Integration needed: terminals, eModal, chassis pools, customers |
| W4 | **0.5** | Proven spend: yes (dispatch staff; TMS spend, with Envase at about $35M of revenue). Weak or missing software: not shown. There are two funded modern vendors, although HTA's 2021 "80%" figure points to a gap in use |
| W5 | **0.5** carrier side; **0.5** importer side | Neutral: very small firms on thin margins; slow uptake suggested by HTA (2021) |
| W6 | **0.5**, leans **0** | Moderate to slow: integrations port by port, a consolidator (WiseTech) and a funded specialist (PortPro), and a central fee pool closest to the reserve line of the six (K5 central $27M, `3a_unknowns.md` §5.2) |

---

## 3. For the coordinator (not a call)

**1. The six cards fall into two groups on these eight rows [our calc; our call]:**

| Group | Cards | A2 + A3 + A6 | W1 + W3 + W4 + W5 + W6 | What they share |
|---|---|---|---|---|
| Paperwork and compliance jobs | C-19, C-20 | 50 of 50 each | 62.5 and 65 of 95 | Office work drives the cost. Retailer or government rules with dates force action. There is proven spend on outside help (contingency recovery firms; per-entry broker fees). The fee is already counted per recovery or per entry |
| Facility, fleet and port jobs | C-04, C-15, C-22 | 25-32.5 | 47.5-57.5 | The saving lands in physical time (dock waiting, miles, terminal waiting). No forcing event was found; two triggers went *away* in 2025 (CARB's fleet and drayage rules). The software market is crowded or consolidating (Opendock with AI agents; 20+ routing vendors; WiseTech in drayage) |
| In between | C-18 | 30 | 47.5 | Pure office work, but no trigger, and only vendor evidence of the pain |

**2. Show-stopper candidates (W4, dominance rule C10):**
- **C-15, beer-distributor segment only.**
  - VIP's route accounting serves "1,000 distributors" (2019) against 1,393 beer-wholesaler firms (2022), and a snippet claims "more than 50 percent of the beer volume".
  - It is the route-accounting job, not proven for routing.
  - If C-15 is shortlisted, S5 must check which routing tool beer distributors use and whether they are satisfied. Segment selection (Q6) could route around beer (grocery, foodservice, industrial).
- **No other dominance candidate.** The leaders' reach [our calc; vendor numerators]:

  | Card | Leader | Reach |
  |---|---|---|
  | C-04 | Opendock | about 7% of sites |
  | C-18 | Extensiv | at most about 20% of warehousing firms |
  | C-20 | NetCHB | about 30% of permitted brokers |
  | C-22 | Envase | at most about 3% of local-trucking firms |
  | C-19 | SPS (SupplyPike) | unknown |

- **Watch-list, not show-stoppers:**
  - WiseTech (CargoWise) in both C-20 and C-22;
  - SPS Commerce in C-19, which owns suppliers' EDI links and bought SupplyPike for $206M.

**3. Readings that could move a score:**
- **C-19 A3:** 1 if a standing retailer fine programme with dated rule changes counts as a forcing event; 0.5 if only a new tightening counts (Walmart *eased* its on-time goal in Feb 2024).
- **C-19 W4:** 1 rests on CRF's 2018 figure (70% of smaller suppliers used no third-party tool). It could be 0.5 by 2026, and S5 should test it.
- **C-20 W3 and W6:** the wedge decides them. A document and classification co-pilot for brokers has its data at hand (W3 1, W6 fast). A filer that replaces ABI software needs certification and a licence (W3 0.5, W6 slow).
- **C-04 W3 = 1** is the only "data at hand" among the facility cards, because a booking calendar needs no integration. The same simplicity lowers W6: it is easy to copy, and the AI-agent firms are well funded.
- **C-22 W6:** it leans 0 on integration count and competition.

**4. The fee-from-savings lens (evidence only; F-7 and F-8 are deferred):**
- Contingency pricing on recoveries is already normal in C-19: "a 30% contingency fee on recovered revenue" (Vendormint). That is the closest match to the project's fee rule among these cards.
- C-20 has per-entry pricing and usage-based software, which ties a fee to the unit.
- C-04, C-15, C-18 and C-22 are sold per facility, vehicle, user or subscription (*assumed* for C-15 and C-22).

**5. Biggest gaps (details in §5):**
- **No neutral adoption survey** for C-04 (dock scheduling), C-15 (routing), C-18 (3PL billing) or C-22 (drayage TMS). Each penetration line rests on a vendor's network claim, a trade survey snippet, or association data from 2021.
- **Vendor customer counts:** SupplyPike/SPS (the 10-K could not be downloaded), PortPro, and CargoWise's US customs share.
- **Channel sizes:** IWLA, NPTC and HTA membership counts were not found. NCBFAA's was (1,500+ member companies).
- **C-04 trigger check incomplete:** whether a detention bill or rule moved in 2025-26, and whether FMCSA published its detention study. The web-search budget ran out first.
- **Target's current OTFR terms conflict** between two vendor sources (3% vs 5% of cost of goods).
- **C-15's VIP claim** ("50% of beer volume") is a snippet only.

**6. Possible corrections or notes for other files (evidence only, not edits):**
- CBP counted **15,226 active licensed brokers** and **2,365 permitted brokers** in 2022 (N-F08, *verified* here). The card's "about 14,500 licensed individuals" (N-F09, secondary) is close; the permitted count is the better measure of brokerage *firms*.
- **Opendock's own figure has grown** from "3,000+" (older landing page) to "4,000+" warehouses (June 2026).
- **C-15's segment notes:** CARB's repeal removes the California electric-truck trigger that the card's "EV and emissions rules" lead assumed.

---

## 4. Sources

**Existing IDs re-read or re-parsed in this check** (listed in their own files):
- **N-N29**, the CRF 2018 Customer Deduction Survey: pp. 26-37 re-read (third-party technology, outsourcing, dispute windows, internal challenges, ERP).
- **N-F08**, CBP's 2022 broker-regulation final rule: full text re-downloaded from govinfo and searched (15,226 licensed brokers; 2,365 permitted brokers; 13,772 electronic filers; the description of ABI).
- **N-D04 / N-E17**, Census SUSB 2022, `us_state_6digitnaics_2022.txt`: re-parsed for firm counts in 424810, 424820, 424410, 424490, 424470, 424210, 484110, 488510, 493110 and 493120.
- **R38**, ATRI *Critical Issues 2025*: resource note re-read (driver shortage #12; detention is drivers' #5 issue).

**Cited without re-fetching:** N-C24, N-N02, N-N05, N-H22, N-J29, N-F02, N-F10, N-F21, N-F32, N-F37, N-F38, N-F47, N-F54, N-F55, N-F61, N-F62, N-E18, N-E24, N-E26, N-K27, N-C13, N-A39, R22, R23, R28, R30, R33.

**New sources.** All were accessed on 2026-09-15. Downloads are in the session scratchpad (`…/scratchpad/checkS/`).

| ID | Source (author/org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-S01 | BLS, OEWS May 2025 national and industry estimates, series OEUN0000000{industry}{SOC}{01 employment, 04 mean wage} | 2025 reference year | https://api.bls.gov/publicAPI/v1/timeseries/data/ | API query (*verified*) | 14 SOCs nationally; 12 industry × SOC pairs (484000, 493000, 488500, 424000, 423000, 311000) |
| N-S02 | O*NET 30.0 database, *Work Activities* and *Work Context* (US DOL / National Center for O*NET Development) | 2025 release; ratings dated 2016-2023 | https://www.onetcenter.org/dl_files/database/db_30_0_text/Work%20Activities.txt ; …/Work%20Context.txt | download, parsed (*verified*) | Importance (IM) and context (CX) ratings for 12 occupations (table in §2) |
| N-S03 | FleetOwner, "Key insights from the NPTC 2025 benchmarking survey on private fleet operations" (NPTC flag) | 2025 | https://www.fleetowner.com/private-fleets/blog/55308859/key-insights-from-the-nptc-2025-benchmarking-survey-on-private-fleet-operations | page extraction; secondary | 104 companies; $3.81 a mile; turnover 18.4%; 70.4% of outbound shipments; safety-technology shares; no routing line |
| N-S04 | Penske Truck Leasing blog, "NPTC Benchmarking Survey: Private Fleets Strengthen Control Over Outbound and Inbound Freight" | 2025-09-23 | https://www.pensketruckleasing.com/resources/blog/nptc-benchmarking-survey-private-fleets-strengthen-control-over-outbound-and-inbound-freight/ | page extraction; vendor summary (*assumed*) | "Nearly three-quarters reported adoption of a broad range of technologies"; fleet metrics; no routing line |
| N-S05 | Skadden, "Tariff Refund Mechanism Takes Shape After Supreme Court's IEEPA Ruling" | 2026-03 | https://www.skadden.com/insights/publications/2026/03/tariff-refund-mechanism-takes-shape | page extraction; secondary (law firm); figures *assumed* | Ruling 20 Feb 2026; CIT order 4 Mar 2026; CAPE; about $165-166B, 53M+ entries, 330,000+ importers |
| N-S06 | Search snippets on the IEEPA ruling and CAPE (NRF; Holland & Knight; Penn Wharton Budget Model; Avalara) | 2026-02 to 2026-05 | https://nrf.com/blog/ieepa-tariff-refunds-are-moving-forward ; https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs ; https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/ | snippet (*assumed*) | 6-3 ruling; CAPE phase one from 20 Apr 2026; 126,237 claims by 11 May 2026 |
| N-S07 | Loadsmart / Opendock landing pages | undated | https://lp.loadsmart.com/opendock-international ; https://loadsmart.com/warehouse/ | snippet only; both pages fetched without the figures; vendor (*assumed*) | "over 3,000 warehouses", "600,000+ appointments", "75,000 carriers" |
| N-S08 | Opendock blog (L. Platero), "Dock Scheduling API & MCP for AI Agents" | 2026-06-09 | https://blog.opendock.com/dock-scheduling-api-mcp-server | page extraction; vendor (*assumed*) | "API-first"; MCP server; "4,000+ warehouses"; agent partners |
| N-S09 | Descartes, "Descartes Acquires NetCHB", Form 6-K Exhibit 99.1 (SEC) | 2022-02-10 | https://www.sec.gov/Archives/edgar/data/1050140/000092963822000375/exhibit99-1.htm | page extraction; vendor claims (*assumed*) | "More than 700 customs brokers"; $40M plus up to $60.0M earn-out |
| N-S10 | SPS Commerce, "SPS Commerce Acquires SupplyPike" (GlobeNewswire) | 2024-08-01 | https://www.globenewswire.com/news-release/2024/08/01/2922667/12398/en/SPS-Commerce-Acquires-SupplyPike.html | page extraction; company release | Price ($119M cash, $87M stock); revenue expected about $8M (2024) and $25M (2025); no customer count |
| N-S11 | SPS Commerce, "Walmart Deduction Management / SPS Revenue Recovery" | undated | https://www.spscommerce.com/products/revenue-recovery/walmart/ | page extraction; vendor (*assumed*) | "$700 million" recovered; connects to Retail Link and carrier and 3PL portals; complimentary audit; no pricing |
| N-S12 | SPS Commerce community (SupplierWiki), "Retail Updates Every Supplier Should Know Before 2025" | 2024-12-10 | https://www.spscommerce.com/community/learn/retail-supplier-updates | page extraction; vendor (*assumed*) | Walmart (Feb 2024), Target (Q3 2024), Home Depot and Amazon dispute changes |
| N-S13 | Logistics Viewpoints, "Walmart Lowers their Shipping Requirements, but their Suppliers Still Struggle" | 2024-02-05 | https://logisticsviewpoints.com/2024/02/05/walmart-lowers-their-shipping-requirements-but-their-suppliers-still-struggle/ | page extraction; secondary | 90% / 95% targets from 1 Feb 2024; 98% since Sep 2020; "0.16% of the cost of goods sold in fines" (Uber Freight) |
| N-S14 | Extensiv newsroom, "4th Annual 3PL Warehouse Benchmark Report …" | 2023-10-19 | https://www.extensiv.com/newsroom/4th-annual-3pl-warehouse-benchmark-report-reveals-most-3pls-fighting-higher-labor-costs-and-many-experiencing-stagnant-or-declining-order-volumes | page extraction; vendor survey (*assumed*) | 240+ 3PL warehouses; labour 70% / 53%; volumes; capacity |
| N-S15 | Extensiv, "Extensiv 3PL Warehouse Manager" product page | undated | https://www.extensiv.com/extensiv-3pl-warehouse-manager | page extraction; vendor (*assumed*) | "1,500+ 3PLs and counting"; billing automation; QuickBooks; tiers without prices |
| N-S16 | Extensiv billing blog pages (snippets) | 2025-26 | https://www.extensiv.com/blog/billing-best-practices-for-3pl-warehouses ; https://www.extensiv.com/blog/warehouse-billing-complete-guide-to-3pl-invoicing-and-cost-management | snippet; vendor (*assumed*) | "82% of 3PL warehouses lose revenue …"; 2025 benchmark +7 and +10 points |
| N-S17 | FMCSA, "Agency Information Collection Activities; Approval of a New Information Collection Request: Impact of Driver Detention Time on Safety and Operations", Federal Register 2024-03256 (govinfo copy) | 2024-02-16 | https://www.govinfo.gov/content/pkg/FR-2024-02-16/html/2024-03256.htm | full text download (*verified*) | "research study"; 80 carriers and 2,500 drivers; 2014 study's limits; aims |
| N-S18 | Snippets on the FMCSA detention study timeline (FreightWaves; Trucking Info; Overdrive) | 2023-24 | https://www.freightwaves.com/news/fmcsa-details-new-truck-driver-detention-time-survey ; https://www.truckinginfo.com/10204733/fmcsa-outlines-plans-for-driver-detention-study | snippet (*assumed*) | Final report planned for July 2025 |
| N-S19 | Snippets on CARB's repeal of Advanced Clean Fleets (CCJ; Sidley; Heavy Duty Trucking; California Renewable Transportation Alliance) | 2025-08 to 2026 | https://www.ccjdigital.com/alternative-power/article/15745098/carb-to-formally-repeal-advanced-clean-fleets-rule ; https://environmentalhealthsafetybrief.sidley.com/2025/08/07/carb-proposes-to-repeal-advanced-clean-fleets-regulation/ ; https://ca-rta.org/carb-to-repeal-high-priority-and-drayage-fleet-provisions-in-acf/ | snippet (*assumed*) | Vote 25 Sep 2025; effective 1 Jan 2027; enforcement paused from Nov 2023; the drayage rule's 2024 requirement |
| N-S20 | Descartes, "Descartes' Study Finds 67% of Freight Forwarders and Customs Brokers View Technology as Fundamental to Growth" (GlobeNewswire; NCBFAA flag) | 2025-11-04 | https://www.globenewswire.com/news-release/2025/11/04/3180097/0/en/Descartes-Study-Finds-67-of-Freight-Forwarders-and-Customs-Brokers-View-Technology-as-Fundamental-to-Growth.html | page extraction; vendor survey (*assumed*) | 434 respondents; 7 associations; 67%, 55%, 25% figures |
| N-S21 | WiseTech Global, "WiseTech Global acquires Envase Technologies …" | 2023-01-24 | https://www.wisetechglobal.com/news/wisetech-global-acquires-envase-technologies-leading-north-american-landside-logistics-software-platform/ | page extraction; company release | US$230M; "more than 1,300 customers"; about US$35M revenue for 2023; "highly fragmented ecosystem" |
| N-S22 | CargoWise Landside pages (snippet) | 2026 | https://www.cargowise.com/landside/solutions/containers-by-road/drayage-tms/ | snippet; vendor (*assumed*) | "Trinium Technologies and Envase Technologies are now part of CargoWise Landside" |
| N-S23 | FreightWaves, "Container drayage TMS provider PortPro raises $12M" | 2023-01-27 | https://www.freightwaves.com/news/container-drayage-tms-provider-portpro-raises-12m | page extraction; trade press | Series A; platform features; no customer count. The BusinessWire release returned 403 |
| N-S24 | TradeLanes / Harbor Trucking Association, "New Research by Harbor Trucking Association and TradeLanes.co …" (HTA flag) | 2021-02-01 | https://www.tradelanes.co/blog/new-research-by-harbor-trucking-association-and-tradelanes.co-shows-health-of-nations-truckers-rail-lines-import-and-export-industries-at-stake | page extraction; association/vendor survey (*assumed*) | 80% not using technology; 89% negative effect; 45 minutes per invoice; top dispute reasons |
| N-S25 | Harbor Trucking Association, home page | undated | https://www.harbortruckers.com/ | page extraction | Ports covered; no member count |
| N-S26 | NCBFAA, home page | undated | https://www.ncbfaa.org/ | page extraction | "more than 1500 member companies with 110,000 employees"; nine areas |
| N-S27 | NBWA, home page | undated | https://www.nbwa.org/ | page extraction | "over 5,000 engaged distributor leaders" (not a firm count) |
| N-S28 | Seven Days (Vermont), "Colchester-Based VIP Taps Into the Beverage Industry With Software Solutions" | 2019-10-16 | https://www.sevendaysvt.com/news/colchester-based-vip-taps-into-the-beverage-industry-with-software-solutions-28696969/ | page extraction; secondary | "now exceeding 1,000 distributors and 800 suppliers"; 429 employees |
| N-S29 | Search snippet quoting VIP on beer volume (attributed to VIP and Vermont Business Magazine, 2022) | 2022 | https://vermontbiz.com/news/2022/july/17/tracking-beverage-industry-vermont-information-processing | snippet only; page returned 403 (*assumed*) | "route accounting system supports more than 50 percent of the beer volume in the U.S." |
| N-S30 | VIP (Vermont Information Processing), home page (redirected from public.vtinfo.com) | 2026 | https://vipinsights.com/ | page extraction; vendor (*assumed*) | "BizStride Logistics" with "Routing"; no share claims |
| N-S31 | Gartner *Market Guide for Vehicle Routing and Scheduling*, vendor lists via vendors' announcements and a summary | 2016-2025 | https://www.gartner.com/en/documents/4009301 ; https://fareye.com/news/fareye-recognized-in-the-2025-gartner-market-guide-for-vehicle-routing-and-scheduling-report ; https://www.citylogistics.info/business/gartners-market-guide-to-vehicle-routing-and-scheduling-systems/ | snippet; report paywalled (*assumed*) | Representative vendors named in §2.2 |
| N-S32 | Snippets on Roadnet (enlyft; DispatchTrack; Descartes "Roadnet alternative" page) | 2025-26 | https://enlyft.com/tech/products/omnitracs-roadnet ; https://www.dispatchtrack.com/blog/roadnet-training/ | snippet; vendor or competitor (*assumed*) | "0.4% market share"; "notoriously complicated" |
| N-S33 | USITC, HTS REST search endpoint | queried 2026-09-15 | https://hts.usitc.gov/reststop/search?keyword=copper%20wire | direct query returned JSON (*verified*) | HTS numbers, descriptions, general and special duty rates |
| N-S34 | Snippets on HappyRobot and Qued (FreightWaves AI Excellence awards 2025; Sacra; Qued) | 2025 | https://www.freightwaves.com/news/freightwaves-announces-winners-of-ai-excellence-in-supply-chain-awards ; https://sacra.com/c/happyrobot/ ; https://www.qued.com/how-ai-could-help-streamline-logistics-operations-transport-topics/ | snippet (*assumed*) | $150M Series C at $1.22B; 150+ customers; DHL partnership of 11 Nov 2025; appointment automation |
| N-S35 | Deduction-recovery service pages (Vendormint; ClearChain; STAT Recovery; Woodridge Retail Group) | 2026 | https://vendormint.com/ ; https://useclearchain.com/services/walmart-deduction-recovery ; https://www.statrecovery.com/deduction-management-services ; https://www.woodridgeretailgroup.com/deduction-recovery | snippet; vendor (*assumed*) | 30% contingency; $5,000 a month flat; recovery claims |
| N-S36 | iNymbus pages (DeductionsXchange) | 2026 | https://www.inymbus.com/deductionsxchange-ar-automation-software ; https://www.inymbus.com/ | snippet; vendor (*assumed*) | Robotic process automation on retailer portals; "51+" retailers; "up to 80%" process-cost cut |
| N-S37 | *Logistics Management* / Peerless Research Group, 2025 automation study and YMS article | 2025 | https://www.logisticsmgmt.com/article/2025_automation_survey_diving_deep_into_the_warehouse_automation_trends ; https://www.logisticsmgmt.com/article/2025_yms_update_how_yard_management_systems_are_transforming_the_modern_supply_chain | snippet; page returned 403 (*assumed*) | 63% use a WMS; 62% a TMS; 44% want automated dock scheduling |
| N-S38 | AI classification tool pages (TariffLens; Gaia Dynamics; Cervo) | 2025-26 | https://www.tarifflens.ai/ ; https://www.gaiadynamics.ai/blog/how-to-find-the-right-import-tariff-codes-for-your-products-in-the-usa-using-ai ; https://usecervo.com/resources/how-ai-handles-hts-classification | snippet; vendor (*assumed*) | Product claims; broker-exam test (Apr 2025); CBP's Cargo Classification Tool |
| N-S39 | eModal snippets (CargoSprint; Crowley; Maersk on OICT) | 2024-26 | https://cargosprint.com/emodal-ocean/ ; https://www.crowley.com/shipping-logistics-announcements/gloucester-terminal-moves-to-emodal-appointment-system-3-11-2026/ ; https://www.maersk.com/news/articles/2024/08/09/oakland-international-container-terminal-oict-export-gate-fee | snippet (*assumed*) | Required appointment system at Gloucester from 11 Mar 2026; fees collected through eModal; prices unpublished |
| N-S40 | Snippet on Target's On-Time Fill Rate (Productiv) | 2025-26 | https://getproductiv.com/otif-compliance-guide | snippet; vendor (*assumed*) | Aug 2024: 95% fill rate, 5% of cost of goods, $150 minimum (conflicts with N-S12) |
| N-S41 | C3 Solutions and Descartes MacroPoint dock-scheduling pages (snippets) | 2026 | https://www.c3solutions.com/dock-scheduling/faq/ ; https://macropoint.com/features/dock-appointment-scheduling/ | snippet; vendor (*assumed*) | C3 is privately held; MacroPoint offers dock appointment scheduling |
| N-S42 | Customs broker directory (snippet) | 2026 | https://customsbrokerindex.com/blog/us-customs-broker-list-find-licensed/ | snippet (*assumed*) | "approximately 11,400 active individual and corporate customs broker licenses" |
| N-S43 | Snippets on NetCHB and the ABI market (FreightWaves; Cervo ABI guide) | 2022; 2026 | https://www.freightwaves.com/news/descartes-acquires-e-commerce-us-customs-filing-provider-netchb ; https://usecervo.com/resources/abi-integration-guide | snippet (*assumed*) | "45% of all Type 86 filings"; the "three most widely used ABI systems" |

---

## 5. Could not access, or not found

**Blocked or unusable:**
- **SPS Commerce 10-K for FY2025** (the SupplyPike and Revenue Recovery customer count). EDGAR full-text search found the filing (`spsc-20251231.htm`, accession 0001092699-26-000012), but the direct path returned "NoSuchKey", and the folder index request returned no JSON. It was not read.
- ***Supply Chain Management Review*, "2025 Warehouse/DC Operations Survey":** HTTP 403. The *Logistics Management* article on the 2025 automation study also returned 403, so its figures are snippets only (N-S37).
- **Vermont Business Magazine on VIP (2022):** HTTP 403. VIP's own site (N-S30) and the NBWA guide listing showed no share figure, so the "50% of beer volume" claim is a snippet only (N-S29).
- **Port of Los Angeles, Clean Truck Program page** (the number of registered trucks and motor carriers): HTTP 403.
- **PortPro's funding release on BusinessWire:** HTTP 403. FreightWaves' article (N-S23) had no customer count.
- **federalregister.gov:** redirected to an "unblock" page. The govinfo copy was used instead (N-S17).
- **IWLA's 2026 membership application PDF:** read in full, but it has no member count.

**Searched, not found** (what was tried; each line was dropped after about three well-aimed attempts):
- **The share of warehouses using dock-scheduling software (C-04):**
  - a general search for adoption surveys;
  - SCMR's 2025 Warehouse/DC survey (403);
  - *Logistics Management* / Peerless Research Group (snippet only).
  - Only vendor network claims were found.
- **The share of distributors or private fleets using routing software (C-15):**
  - NPTC's 2025 survey (members-only; two public summaries read, with no routing line);
  - a search of fleet-technology surveys (vendor compilations only);
  - a search of distributor surveys.
- **Neutral 3PL billing or automation data (C-18):** check N's three tries (IWLA, WERC and academic, public 3PL filings) stand. Only Extensiv's vendor surveys were found. IWLA's membership size was also not found.
- **Current Target OTFR terms (C-19):** two vendor sources conflict (N-S12, N-S40). Target's own vendor manual was not reachable by search.
- **SupplyPike or SPS customer counts (C-19):** the acquisition release (none) and the 10-K (not downloadable).
- **CargoWise's share of US customs filings (C-20):** none found. Only NetCHB's broker count (2022) was found.
- **Drayage TMS customer counts beyond Envase (C-22):** PortPro's funding coverage (none).
- **Membership counts for NPTC and HTA:** home pages only; no figures.
- **FSMA 204** (FDA food-traceability rule) as a possible C-19 or C-15 trigger for food suppliers: not checked. A vendor snippet mentioned it, but its compliance date was not verified.

**Not attempted: the web-search budget for this session ran out** (200 of 200 searches) before these checks:
- whether any federal or state detention-pay bill or rule moved in 2025-26 (C-04 trigger);
- whether FMCSA published its detention study's final report (planned July 2025);
- a list of drayage TMS vendors with shares;
- NCBFAA's regional member counts.
- Direct page fetches were used after that point.

**Tooling:**
- The scholarly-search MCP server was not connected, so peer-reviewed sources were reached only through general web search.
- cbp.gov was not needed directly: CBP figures came from the Federal Register via govinfo (N-F08, N-N05) and from earlier checks (N-H22, N-J29).
