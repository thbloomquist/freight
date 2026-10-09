# S3b check Q: carrier and broker jobs (C-02, C-03, C-05, C-06, C-07, C-08)

> **What this is:** new desk evidence for six S3b fact sheets in run 01 (`submarket_selection.md` §4 S3b):
> - item 5: software penetration and why now;
> - item 6: the roles doing the costly work;
> - item 7: the budget holder and implementation;
> - item 9: competitors, substitutes and the incumbent map;
> - evidence and a suggested score for eight rows: A2, A3, A6, W1, W3, W4, W5, W6.
>
> **Date:** 2026-09-15. **Status: input to S3b; decides nothing.** Every score here is a suggestion under the row rules in `2_knockouts.md` §5. The coordinator makes the calls, and scores A1, A4, A5 and W2 from data already held.
> **Labels:**
> - *verified*: read at the source;
> - *assumed*: a snippet, a secondary summary, a vendor claim, memory, or a blocked page. Vendor figures are always *assumed*;
> - **[our calc]**: arithmetic done here;
> - **[our call]**: a judgement made here.
>
> **IDs:** new sources are N-Q01 to N-Q45 (§4). Earlier IDs (R, N-B to N-N) are cited as they stand and were not re-fetched, except N-N14, which was re-read.
> **Pricing:** how incumbents charge is recorded as evidence only. The project's own fee is deferred (F-7, F-8), and nothing here recommends a price.

## Words used (freight jargon, first use)

- **Broker:** a firm that finds a truck for a shipper's load and keeps the spread between the two prices. It holds a federal "authority" (an MC number).
- **Owner-operator:** a one-truck carrier, usually the driver who owns the business.
- **TMS (transportation management system):** the main office software of a broker, carrier or shipper: loads, rates, carriers, documents, invoices.
- **ELD (electronic logging device):** the in-cab device every interstate truck must use to log driving hours, required since the 2017 mandate (N-B22). It also knows where the truck is.
- **Check call:** a phone call or text to a driver or dispatcher asking where a load is.
- **EDI (electronic data interchange):** standard machine-to-machine messages. EDI 214 is the "carrier shipment status" message.
- **API:** a published way for one piece of software to fetch data from another. It is Bushel's "plumbing" (R30).
- **Load board:** a website where brokers post loads and carriers search for them (DAT, Truckstop).
- **Spot load:** a load booked one at a time at today's price, not under contract.
- **Dispatch service:** an outside firm that finds and books loads for owner-operators, for a share of their gross revenue.
- **Detention:** time a truck waits at a shipper's or receiver's dock beyond the free time, usually two hours.
- **Accessorial:** any charge on top of the base rate, such as detention, a lumper (unloading) fee, layover, or TONU (truck ordered, not used).
- **Rate confirmation:** the broker-carrier agreement for one load.
- **BOL (bill of lading):** the shipping document.
- **POD (proof of delivery):** the signed delivery receipt.
- **Factoring:** selling an unpaid freight invoice to a finance firm (a "factor") for cash now, minus a fee.
- **Quick pay:** a broker paying a carrier early in exchange for a discount.
- **Double brokering:** a carrier, or a fake one, takes a load and secretly re-brokers it to another truck, often without paying.
- **Negligent selection:** a lawsuit claim that a broker chose an unsafe carrier.
- **Contingent cargo insurance:** a broker's back-up cargo policy.
- **SNPRM:** a supplemental notice of proposed rulemaking. **OMB/OIRA** is the White House office that reviews a rule before it is published.

---

## 1. Summary

| Card | Penetration (one line) | Trigger(s) | Budget holder | Implementation | Vendors (count; leader; dominance) | Service firms | Suggested A2 / A3 / A6 / W1 / W3 / W4 / W5 / W6 | Sources |
|---|---|---|---|---|---|---|---|---|
| **C-02 Load status** | Brokers still make check calls: 79% of cargo agents track loads daily. Tracking platforms exist, but coverage of small carriers is patchy (vendor: "as low as 30 to 40 percent" in past years). About 10% of shippers under $25M freight spend use a TMS | AI check-call agents (HappyRobot: $150M Series C, 4 Aug 2026; 8 of the 10 largest brokers). DAT bought Trucker Tools (Dec 2024). Fraud makes location a proof of identity | Broker operations manager (payroll plus per-load tracking fees); shipper logistics manager | **Weeks** for an AI check-call layer (needs the load list and phone numbers). ELD data needs each carrier's consent | ≥10 (5 visibility platforms, sensors, AI agents, plus TMS and ELD features); no share published; Trucker Tools serves 750+ brokers (~3% of authorities); **no dominance found** | Brokers bundle it into their margin | **1 / 0.5 / 1 / 0.5 / 0.5 / 1 / 1 / 0.5** | N-N28, N-E20, N-Q07, N-Q18, N-Q25, N-Q38 |
| **C-03 Detention and extra charges** | Drivers are detained at 39.3% of stops; fees are collected on fewer than half (*assumed*). Vendor: manual processes capture about 40% | **None binding.** FMCSA's detention study uses ELD and TMS data, but no report was found. FMCSA's split-duty pilot (Sep 2025, 256 drivers) is a workaround | Carrier owner (revenue recovery); shipper DC manager (accessorial spend) | **Weeks:** ELD geofence timestamps, plus the rate confirmation's terms, plus the invoice route | ~10-12 (TMS and telematics features, plus 3-4 standalone tools such as ChargeGuard at $59-349/mo); no shares; no dominance | Factors, dispatch services; brokers pass the charge through | **0.5 / 0.5 / 0.5 / 0.5 / 0.5 / 1 / 0.5 / 0.5** | N-C24, N-D34, N-D35, N-Q13, N-Q14, N-Q29 |
| **C-05 Getting small carriers paid** | Carriers send paper or PDF packets and wait 30-45 days; 23-28% of owner-operators factor. The payer side is already on networks: Triumph says its network touches over 50% of brokered truckload transactions | Broker financial-responsibility rule in force since **16 Jan 2026**. Transparency SNPRM at OMB since **27 Aug 2026**. Load boards bought payment firms: DAT-Outgo (May 2025), Truckstop-Denim (Aug 2025) | Carrier owner (the factoring fee comes out of revenue); broker controller or AP manager (carrier payables) | **Months:** money movement, a bank partner, broker AP and TMS integration, capital for advances | ≥12 networks, factors and tools. **TriumphPay: ~65% of brokered truckload dollars touched [our calc on company figures]; 67 of the top 100 brokers → dominance candidate** (payer side, large brokers) | Factors (1.29-3.2%), broker quick pay (1.5-5%) | **0.5 / 1 / 1 / 0.5 / 0.5 / 0.5 / 0.5 / 0** | N-Q02 to N-Q04, N-N14 to N-N17, N-Q10, N-Q11, N-Q06 |
| **C-06 Matching spot loads** | Owner-operators search boards and phone brokers. OOIDA members under their own authority: 23% of business via load boards, 2% via digital matching. Dispatch services charge 5-10% of gross | DAT roll-up: Trucker Tools, Outgo, Convoy, Loadlink (2024-25). AI dispatch agents (FleetWorks $17M, Oct 2025). Capacity leaving the market in 2026 | Owner-operator (dispatch fee, board subscription) | **Days to weeks**, but depends on load-board access; no open carrier-side API found | ≥10 (3 boards, 5 AI dispatch tools, digital brokers). DAT + Truckstop ">85%" (*assumed*) → DAT ≈ 57% of posted loads [our calc on assumed inputs]: **weak dominance candidate** | Dispatch services; brokers themselves | **0.5 / 0.5 / 1 / 1 / 0.5 / 0.5 / 0.5 / 0.5** | N-N17, N-F39, N-F41, N-Q06, N-Q08, N-Q20, N-Q26 |
| **C-07 A small brokerage's back office** | Micro-cap brokers: 20+ TMSs, McLeod ~16%, homegrown ~13%. Calls, email and re-keying stay manual. ">60% operate without software" (2022, unsourced) | Transparency SNPRM would require electronic records produced within 48 hours. Bond rule (Jan 2026). *Montgomery* (May 2026). Broker count falling. AI agents priced for large brokers | Brokerage owner; sales and operations leaders decide (tech under 10%) | TMS swap = **months** (fails R28); AI add-on = **weeks** | 20+ TMSs plus ≥4 AI tools; leader McLeod ~16%; **no dominance** | Freight-agent model; outsourced back office; TriumphPay (payables) | **1 / 1 / 1 / 0.5 / 0.5 / 1 / 0.5 / 0.5** | N-B04, R27, N-Q01, N-Q11, N-Q18, N-Q33, N-Q40 |
| **C-08 Carrier vetting and fraud** | Manual FMCSA look-ups plus monitoring services. Fraud rising: confirmed theft $454M (2024) → ~$725M (2025) (vendor) | **Motus** registration with ID checks (Q2 2026). ***Montgomery v. Caribe*** (14 May 2026, 9-0). H.R. 8870 (§5007, §7109) ordered reported May 2026. H.R. 5337 safe-harbour bill pending | Broker compliance or onboarding lead (risk and insurance budget); the owner at small brokers | **Days:** public FMCSA data plus carrier documents. Deeper identity signals need network data | ≥12 tools. Highway: 70 of the top 100 brokers, but ~4% of brokers by count. Candidate only for a top-100 segment | Insurers and agents, compliance consultants, factors | **1 / 1 / 1 / 0.5 / 1 / 0.5 / 1 / 0.5** | N-Q09, N-Q15, N-Q12, N-Q16, N-G43, N-Q21, N-Q22, N-N24 |

**Where the two sides differ (rule C5, better side used):**
- C-02: W1 and W5 are better on the freight-company (broker) side.
- C-03: the carrier side is better on W1 and W5.
- C-05: the payer (broker) side is better on A3.
- C-06: the carrier side is better on W1.
- C-07 and C-08: the broker side is better on A3 and W5 (C-07 on A3 only).

---

## 2. Card by card

### C-02 · Load status, for mid-sized shippers and receivers

#### Item 5: software penetration and why now

**How much still runs on phone and email:**
- **Brokers:**
  - "Track delivery progress of shipments" is a core task for cargo and freight agents: 79.0% do it daily or more, 29.1% several times a day, 14.7% hourly (O*NET, N-N28, *verified*).
  - Job posts cite "up to 100" check calls a day (N-F60, *assumed*).
- **Shippers:**
  - About 10% of shippers with under $25M of freight spend use a TMS (a Gartner figure quoted by a vendor blog in 2019, N-E20, *assumed*).
  - Descartes/SAPIO 2025, 616 shippers and logistics firms: "only 17% ... fully automated", and over a third "heavily or mostly reliant on manual processes" (N-F28, vendor survey, *assumed*).
  - R27 (2022): shippers "currently lack visibility across the brokers and carriers they work with".
  - Tive 2024, 244 respondents: 24% see 75-100% of their shipments; 45% see less than half (N-Q39, vendor, *assumed*).
- **Tracking coverage:**
  - Brokers' customers often require 80-95% of loads tracked. Vendors say the "industry average has been as low as 30 to 40 percent in past years" (N-Q38, vendor, *assumed*).
  - Small carriers and owner-operators often resist being tracked (N-Q38). This is why check calls survive at brokers that already pay for a tracking platform.
- **Category maturity:** Gartner's 2025 Hype Cycle places "Real Transportation Visibility Platforms" on the "Slope of Enlightenment", i.e. mature (N-G42, via a vendor summary, *assumed*).

**Systems of record, and whether they have plumbing (R30):**
- **ELD and telematics:**
  - Samsara documents a public REST API. A third party gets a token only after the carrier accepts a data-sharing addendum (N-Q36, *assumed*).
  - Both Samsara and Motive generate shareable tracking links that work with Trucker Tools and FourKites (N-Q36, *assumed*).
  - So the location data exists, but each carrier must consent.
- **Driver apps:**
  - Trucker Tools' app connects "350,000 owner-operators, carriers, and drivers" (N-Q07, vendor).
  - MacroPoint says it connects "over 200k carriers" (N-Q25, vendor).
- **EDI 214:** the standard status message, used mostly by larger truckload and LTL carriers (N-Q37, *assumed*).
- **Broker TMS:** holds the load list and carrier contacts. The rate confirmation carries the driver's phone number (*assumed*).
- **Plumbing verdict [our call]:** present, but split across many systems and gated by consent on the carrier side.

**Named triggers:**
- **AI voice agents for check calls:**
  - HappyRobot closed a $150M Series C on 4 Aug 2026 at a $1.22B post-money valuation. It has "150-plus customers" and "eight of the 10 largest US freight brokers running its agents in production" (Forkast, N-Q18; secondary, vendor claims, *assumed*).
  - Vooma raised $16.6M (Dec 2024; N-Q19, *assumed*).
  - RXO says its AI "automated more than 500,000 calls" in Q1 2026 (N-Q19, snippet, *assumed*).
  - a16z: small and mid-size brokers "can make and receive hundreds, if not thousands, of calls per day" (N-G44).
- **Consolidation into the load board:** DAT bought Trucker Tools on 17 Dec 2024 and Convoy on 30 Jul 2025 (Roper 10-K, N-Q06, *verified*).
- **Fraud and liability:**
  - Location now proves that the hired truck has the load (Highway's load-level verification, N-G43).
  - Triumph's Q2 2026 letter names "a new era of vicarious liability for brokers and shippers" (N-Q04, *verified*).
- **Minor:** FMCSA's detention study collects ELD and TMS data (N-Q13), so status data is becoming regulatory evidence.

#### Item 6: addressable work

| Side | Role (SOC; industry) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|---|
| Broker | Cargo and freight agents (43-5011; NAICS 4885, freight transportation arrangement) | 53,390 | $57,570 | N-Q01, *verified* |
| Broker | Customer service representatives (43-4051; 4885) | 10,920 | $51,980 | N-Q01 |
| Broker | Dispatchers (43-5032; 4885) | 8,350 | $54,280 | N-Q01 |
| Carrier | Dispatchers (43-5032; 484, truck transportation) | 34,890 | $58,690 | N-Q01 |
| Shipper | Logisticians (13-1081; all industries) | 251,040 | $89,730 | N-Q01 |
| Shipper and receiver | Shipping, receiving and inventory clerks (43-5071; all industries) | 816,870 | $46,810 | N-Q01 |

- **Coverage of the counts:**
  - NAICS 4885 includes forwarders and customs brokers. S2 assumed 50-70% of its staff work in truck brokerage.
  - Owner-operators are self-employed, so OEWS leaves them out.
- **A small check for K5:** the in-industry mean wage for cargo agents ($57,570) is 0.6% above the $57,230 S2 used. C-02's pool is unchanged **[our calc]**.
- **R22:** status work is phone, text, email and portal updates. That is text- and number-heavy office work.
- **R23:** "human connection" is not the benefit of a status update. Exceptions (a late load, a rebooking) need judgement.
- **R22, core or supporting:** tracking is supporting work for a broker, not its core product (selling and covering loads), so it should meet less resistance.

#### Item 7: budget holder and implementation

**Budget:**
- **Broker side:** the operations manager or owner. The cost sits in operating payroll (track-and-trace reps) and in per-load tracking fees.
  - Brush Pass: about a third of brokerage software decision-makers sit in sales, 51% in customer- or carrier-facing roles, and under 10% in tech (N-Q33; no method given, *assumed*).
- **Shipper side:** the logistics or transportation manager, from the logistics operations budget. Status is usually bundled into the broker's price (N-F row (c), *assumed*).

**Day one, and live in weeks (R28):**
- **An AI check-call or text agent** needs only the load list (a TMS export, or rate confirmations) and driver phone numbers. It could show value on day one and go live in weeks **[our call]**. HappyRobot integrates with broker TMSs (N-Q18).
- **Automatic location from ELDs** needs each carrier's consent, so coverage builds over months.
- **A shipper-side view across all its brokers** needs a feed from each broker (EDI 214, a portal, or parsed emails). That takes months.

#### Item 9: competitors, substitutes and the incumbent map

**Named software, ≥10:**
- **Visibility platforms:** project44, FourKites, Shippeo, Descartes MacroPoint, Trucker Tools (now DAT) (N-F48, N-F49, N-F70, N-Q07).
- **Sensor tracking:** Tive (N-Q39).
- **AI check-call agents:** HappyRobot, Vooma (N-Q18, N-Q19). RXO built its own.
- **Features inside larger products:** ELD share links (Samsara, Motive; N-Q36); customer portals in broker TMSs (*assumed*).

**The leader's share:**
- None published.
- Gartner's 2025 Leaders were project44 and Shippeo (N-F48). FourKites withdrew from the assessment (N-F49).
- Trucker Tools says it gives "real-time visibility for more than 750 leading freight brokers" (N-Q07, vendor). That is about 3% of 25,081 broker authorities **[our calc]**.
- MacroPoint gives no broker count.

**Dominance (C10):** no vendor is shown serving more than half of brokers or of mid-sized shippers. No show-stopper found.

**Service firms:** brokers and 3PLs bundle status into their margin or fee (N-F row (c)). Outsourced call centres were not researched.

**How the job is done today:**
- phone, text and email check calls;
- carrier and broker portals;
- ELD tracking links;
- doing nothing: the receiver simply waits;
- general-purpose AI tools: no evidence found.

**How incumbents charge (evidence only):**
- MacroPoint: "starts at $5 per load and can be discounted as low as 40 cents a load", plus a flat implementation fee (N-Q25, vendor).
- A third-party MacroPoint connector for a broker TMS costs $149.95 to set up plus $39.95-49.95 a month (N-Q25, snippet).
- The Trucker Tools driver app is free to carriers; brokers pay (N-Q07).
- HappyRobot: a "minimum annual spend of approximately $250,000" (N-Q18, *assumed*).

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **1** | Office labour drives the cost: check calls and emails by 53,390 cargo agents averaging $57,570 |
| A3 | shipper 0.5; freight-co 0.5 | **0.5** | A known cost, but no regulation or crisis forces a change. AI agents are a technology shift, not a forcing event |
| A6 | — | **1** | The same status data proves detention (C-03), feeds dock appointments (C-04), verifies the truck (C-08), triggers payment at POD (C-05) and supports claims (C-10) |
| W1 | shipper 0; freight-co 0.5 | **0.5** (freight-co side) | Shippers are spread across every industry. Brokers are partly gathered: TIA has about 1,600-1,700 members (N-Q35) out of ~25,000 brokers; plus load-board marketplaces and TMS integrations |
| W3 | — | **0.5** | Integration needed: the TMS load list, ELD APIs gated by carrier consent, and EDI 214 for larger carriers |
| W4 | — | **1** | Proven spend: staff time and per-load fees. Software is weak on coverage (check calls persist; historic compliance 30-40%, vendor) and missing at most mid-sized shippers (~10% use a TMS). *Caveat:* the platforms are mature, and the "weak" evidence is vendor-sourced. Read as "mature software exists", this row would be 0.5 |
| W5 | shipper 0.5; freight-co 1 | **1** (freight-co side) | Brokers are buying check-call automation: 8 of the 10 largest run HappyRobot, which has 150+ customers. The evidence comes from large brokers only |
| W6 | — | **0.5** | Moderate. An AI agent layer can be built fast. Location coverage needs a carrier network, against DAT, Descartes, project44 and funded AI entrants |

---

### C-03 · Detention and extra charges at the dock

#### Item 5: software penetration and why now

**How much still runs on paper and phone:**
- Drivers were detained at 39.3% of stops in 2023 (ATRI, N-C24, *verified*).
- Detention fees were "collected on fewer than half" of invoices (N-C24; page summary, *assumed*).
- Vendor claims (N-D34, *assumed*):
  - carriers using manual processes "capture only around 40%" of the detention owed;
  - "most tools only show _that a driver waited_".
- The job runs on paper logs, driver texts, phone and email disputes (card C-03).
- Shippers and receivers "are only willing to pay 50% to 70% of the revenue carriers lose" while trucks wait (TheTrucker, 2024, N-Q30; secondary, *assumed*).

**Systems of record and plumbing:**
- **ELD and telematics geofences** (a geofence is a virtual fence around a site) timestamp arrival and departure (N-Q29, vendor, *assumed*):
  - Samsara's "Time on Site Report" is meant, in part, "to investigate customer detention time";
  - Motive offers detention reports filtered by location.
- **Carrier TMSs** with detention features: Trimble TMW, McLeod (N-D34).
- **Rate confirmations** carry the detention terms. Typically $50-100 an hour after 2 free hours (N-G38, vendor).
- **Factoring portals** bill accessorial lines with the invoice (N-F40).
- **Plumbing verdict [our call]:** good on the carrier side (ELD APIs, N-Q36). The payer's facility has no data feed.

**Triggers:** none binding.
- **FMCSA's detention study**, "Impact of Driver Detention Time on Safety and Operations" (Federal Register, 16 Feb 2024, N-Q13, *verified*):
  - "Approximately 80 carriers and 2,500 CMV drivers";
  - 12 months of ELD, TMS and telematics data.
  - A final report was planned for July 2025 (secondary snippet, *assumed*). No published report was found (§5).
- **FMCSA's Split Duty Period Pilot Program** (Federal Register, 17 Sep 2025, N-Q14, *verified*):
  - about 256 drivers may pause the 14-hour driving window for 30 minutes to 3 hours at a pickup or delivery;
  - its stated aim is to "mitigate the impacts of unreasonable 'detention times'".
  - It is an hours-of-service workaround, not a pay rule.
- **Congress:**
  - CRS's review of trucking issues for reauthorization (updated 11 Sep 2026) lists no detention-pay bill (N-Q12).
  - Earlier attempts failed. DOT's 2014 Grow America Act proposed paying drivers for on-duty waiting; ATA called it "extraordinarily misguided" and OOIDA supported it (N-Q31, *assumed*). A later House bill to set maximum unpaid detention did not advance past introduction (N-Q31, snippet).
- **Indirect:** the broker-transparency SNPRM would require records of "charges and payments tied to a shipment" (N-Q11). That could show whether detention paid by shippers reaches carriers (inference).
- **Market:** the truckload sector's average profit margin was -2.3% (R38), so recovered revenue matters more.

#### Item 6: addressable work

| Side | Role (SOC; industry) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|---|
| Carrier | Dispatchers (43-5032; 484) | 34,890 | $58,690 | N-Q01, *verified* |
| Carrier | Bookkeeping, accounting and auditing clerks (43-3031; 484) | 16,270 | $53,480 | N-Q01 |
| Carrier | Billing and posting clerks (43-3021; 484) | 5,840 | $47,070 | N-Q01 |
| Shipper and receiver | Shipping, receiving and inventory clerks (43-5071; all industries) | 816,870 | $46,810 | N-Q01 |

- **Owner-operators:** 56.6% of active interstate for-hire carriers run one truck (card C-03, from N-F02). The owner does this work and is not counted in OEWS.
- **R22:** logging, billing and disputing are text and number work. The waiting itself is physical.
- **R23 [our call]:** billing needs no human touch. Disputing with a shipper customer is relationship-sensitive; brokers may waive a charge to keep a customer.

#### Item 7: budget holder and implementation

**Budget:**
- **Carrier side:** the owner or office manager. This is revenue recovery, so the first recovered charge can pay for the tool. ChargeGuard sells to carriers with 5-150 trucks at $59-349 a month (N-D35, vendor).
- **Shipper side:** the DC or transportation manager. Detention sits in freight and accessorial spend, paid by accounts payable. Their interest is the opposite: avoid the charge.

**Implementation:**
- Data needed:
  - arrival and departure timestamps (an ELD geofence API, or a driver app);
  - the detention terms on the rate confirmation;
  - the invoice route (TMS, factor or broker portal).
- Value on day one for new loads, live in weeks **[our call]**. Collection still depends on the payer.

#### Item 9: competitors, substitutes and the incumbent map

**Named software, ~10-12:**
- **A 2026 guide lists 7 tools:** five TMSs (including Trimble TMW and McLeod), Samsara, and one driver-management platform (N-D34).
- **Standalone:** ChargeGuard (N-D35); DetentionIQ, DockClaim, Glocate (N-Q29, snippets).
- **Features inside telematics:** geofencing is standard in Samsara, Motive, Verizon Connect and Geotab (N-Q29, *assumed*).
- **Shipper side:** dock-appointment tools (the C-04 vendors) shorten the wait rather than bill it.

**The leader's share:** none published (check D, worked example 3).

**Dominance:** none.

**Service firms:**
- factors, which bill and collect accessorials with the invoice;
- dispatch services;
- brokers, who pass the charge through or absorb it.

**How the job is done today:** paper and driver-reported times; phone and email; often nothing (the charge is never billed); shippers pay part.

**How incumbents charge (evidence only):**
- monthly subscriptions (ChargeGuard, $59-349);
- bundled into per-truck telematics and TMS fees;
- the factor's percentage on the accessorial line.

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **0.5** | Mixed. The cost is physical waiting at the dock. Software can document and bill it, but not shorten it; the office part is capture, billing and disputes |
| A3 | carrier 0.5; shipper 0.5 | **0.5** | A known cost: 135.9M driver-hours a year (R38), $1.1-1.3B of lost driver earnings (N-F30). No forcing event: there is no pay mandate, and the FMCSA pilot works around detention |
| A6 | — | **0.5** | One or two adjacent groups: other accessorials (lumper, layover, TONU) and shipper dwell and dock appointments (C-04) |
| W1 | carrier 0.5; shipper 0 | **0.5** (carrier side) | Carriers are partly reachable through factors, load boards, telematics app marketplaces, and OOIDA (150,000+ members, N-Q34). Shippers are dispersed |
| W3 | — | **0.5** | Integration needed: an ELD geofence API with carrier consent, the rate confirmation's terms, and the invoice route |
| W4 | — | **1** | Proven spend: billing staff, telematics and TMS modules, ChargeGuard subscriptions. Software is weak: tools mostly "show that a driver waited", and the standalone category is nearly empty |
| W5 | carrier 0.5; shipper 0 | **0.5** (carrier side) | Carriers feel the pain (drivers' #5 issue, R38), but there is no evidence they would switch tools. Payers resist (they pay 50-70%, *assumed*) |
| W6 | — | **0.5** | The tool is quick to build. But each recovered dollar depends on the payer agreeing, and ChargeGuard's prices suggest thin budgets |

---

### C-05 · Getting small carriers paid

#### Item 5: software penetration and why now

**How much still runs on paper:**
- **The carrier's side:**
  - The billing clerk, often the owner, gathers the rate confirmation, BOL and POD, then emails an invoice packet or uploads it to a portal (N-F63, illustration, *assumed*).
  - Brokers typically pay in 30-45 days (N-Q28, *assumed*).
- **How carriers get cash sooner:**
  - 23-28% of owner-operators factor (OOIDA 2019 and 2022, N-N16 and N-N17, *verified*; OOIDA flag).
  - Fees: OOIDA members averaged 3.2% (2019). Triumph's average discount was 1.29-1.37% in 2025 (N-N15, *verified*).
  - Quick pay costs 1.5-5% for payment in about 2-5 days (N-Q28, *assumed*).
- **The payer side is already digital, and concentrated:**
  - Triumph, Q4 2024 letter: "we believe that more than 50% of all brokered freight transactions touch our network", "using $110 billion as the addressable truckload market" (N-Q02, *verified* filing; a company estimate).
  - The network's "breadth" was $71B annualized in Q4 2025 (N-Q03). "Network engagement" was $88.5B in Q2 2026, against a market re-sized to $135B (N-Q04). That is about **65% and 66%** **[our calc]**.
  - Triumph's Payments segment processed 33.6M invoices, paying carriers $40.5B, in 2025 (N-N14, *verified*, re-read).

**Systems of record and plumbing:**
- Broker TMS and accounting. Triumph "integrates directly into the payor's TMS and accounting systems" (N-Q02).
- Payment networks. Triumph's LoadPay carrier account has an "integration to 400+ brokers" (N-Q03).
- Factoring portals.
- Load boards with payments built in: DAT-Outgo, Truckstop-Denim.
- Bank rails (ACH).
- **Plumbing verdict [our call]:** it exists, and incumbents own most of it.

**Named triggers:**
- **The FMCSA broker financial-responsibility rule**, compliance date **16 January 2026** (89 FR 107021, N-Q10, *verified*):
  - brokers must hold $75,000 of security (a surety bond, BMC-84, or a trust, BMC-85);
  - trust assets must be liquid "within 7 calendar days";
  - FMCSA suspends a broker's authority when its available security falls below $75,000.
  - Carriers' claims for unpaid freight draw on that security, so late or missed payment now meets a faster penalty (inference).
- **The broker-transparency SNPRM**, sent to OMB on **27 August 2026** (FreightWaves, N-Q11, *assumed* secondary):
  - brokers would keep electronic transaction records, including charges, payments, amounts and dates;
  - they would give a copy to a carrier or shipper within 48 hours of a request.
  - It follows OOIDA's petition, and about 7,000 comments on the November 2024 proposal (N-Q11, N-Q12). Not yet published.
- **H.R. 8870 §4019** would exclude from the "broker" definition any person providing only financial assistance, analysis or accounting services (CRS, N-Q12). That clarifies the legal footing of payment and factoring firms (inference).
- **Load boards are absorbing payments:**
  - DAT bought Outgo, a factoring and fintech firm, closing 15 May 2025 (Roper 10-K, N-Q06, *verified*);
  - Truckstop bought Denim in Aug 2025 (N-Q27, *assumed*).
- **Market:**
  - By Dec 2025, median broker gross margins had fallen to "some of the lowest levels observed" (N-Q03, *verified*).
  - Spot and contract rates rose sharply in 2Q 2026 (N-Q04). Bigger invoices mean bigger factoring fees.

#### Item 6: addressable work

| Side | Role (SOC; industry) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|---|
| Carrier | Bookkeeping, accounting and auditing clerks (43-3031; 484) | 16,270 | $53,480 | N-Q01, *verified* |
| Carrier | Billing and posting clerks (43-3021; 484) | 5,840 | $47,070 | N-Q01 |
| Broker | Bookkeeping, accounting and auditing clerks (43-3031; 4885) | 7,530 | $52,600 | N-Q01 |
| Broker | Billing and posting clerks (43-3021; 4885) | 2,240 | $46,330 | N-Q01 |

- **Coverage:** most of the 446,405 carriers with 10 or fewer trucks (N-F02) bill for themselves. The self-employed are not in OEWS.
- **R22:** matching documents and approving payments is text and number work.
- **But most of the pool is not labour:** the factoring discount is a price of money (working capital).
- **R23:** invoicing needs no human connection. Factoring relationships (credit checks, collections) are partly human.

#### Item 7: budget holder and implementation

**Budget:**
- **Carrier side:** the owner-operator. Factoring fees come out of revenue: a finance cost, not a software budget.
- **Payer side:** the broker's controller or AP manager. Carrier payables is a cost centre. Triumph pitches it as a way to earn revenue from quick pay (N-Q02).

**Implementation:**
- Data needed:
  - the rate confirmation, BOL and POD;
  - carrier bank details, which carry payee-fraud risk;
  - broker AP and TMS integration.
- It also needs a bank or money-transmitter partner, and capital for any advance.
- Months, not weeks. It fails R28's "live in weeks" unless the product is a billing-only tool for carriers **[our call]**.

#### Item 9: competitors, substitutes and the incumbent map

**Named firms, ≥12:**
- **Payment networks:** TriumphPay (payments, audit, LoadPay); DAT/Outgo; Truckstop/Denim; Relay Payments (its broker customers "represent more than $1.5 billion" of annual freight payments, N-Q27).
- **Factors:** Triumph (#2 in North America, N-N15), RTS Financial, OTR Solutions, Apex Capital, TAFS, eCapital, England Logistics (N-Q44, N-G39).
- **Carrier billing tools:** TruckingOffice (N-F74), QuickBooks-type bookkeeping (N-F63).
- **Shipper-side freight audit and payment** (Cass, U.S. Bank) is card C-09.

**Dominance (C10): a show-stopper candidate. The rule needs one vendor serving more than half the target customers for the job, and those customers satisfied.**
- **The payer side, counted by transactions:**
  - Triumph's own estimate has been above 50% of unique brokered truckload transactions since Q4 2024, and about 65% by Q4 2025 and Q2 2026 **[our calc]**.
  - It "will serve 67 of the top 100 freight brokers and 8 of the top 10" (Q4 2025 letter, N-Q03, *verified*). It recently added BlueGrace and J.B. Hunt (N-Q03).
  - Management said on the Q4 2024 call that the goal was "60% to 65% of market share" by end-2025 (N-Q05, *assumed*, transcript).
- **The payer side, counted by customers:** "hundreds of smaller brokers" (N-Q03), against an estimated 25,000 active truck brokers (CRS, N-Q12). Reading "hundreds" as 200-900, that is roughly 1-4% of small brokers **[our calc]**.
- **The carrier side:**
  - TriumphPay pays "more than 150,000 carriers" by same-day ACH (vendor roundup, N-Q27, *assumed*). That is about a third of the 446,405 small carriers **[our calc]**, though the 150,000 includes larger carriers.
  - Triumph factoring bought $11.7B in 2025, 19-23% of the factored pool (S3a check N).
- **Reading [our call]:** a show-stopper candidate for any payer-side segment made up of large brokers (the top 100). Not shown for small brokers, shippers or carriers.
  - "Touch" counts a transaction if any Triumph product reaches it, including when only the carrier's factor is on the network. So it overstates how many brokers chose Triumph.
  - Satisfaction is an S5 question.

**Service firms:** factors (1.29-3.2% per invoice); brokers' quick-pay programmes (1.5-5%); dispatch services that invoice on the carrier's behalf.

**How the job is done today:** email or PDF packets, broker portals, waiting 30-45 days, or factoring. Doing nothing means waiting.

**How incumbents charge (evidence only):**
- a percentage of each invoice (factoring, quick pay);
- per-transaction fees to brokers and factors (Triumph's "transaction fees");
- 1.68% average interchange on LoadPay debit-card spend (N-Q03);
- subscriptions for carrier billing tools.

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **0.5** | Mixed. The paperwork is office work, but most of the pool (the factoring discount) is a price of capital |
| A3 | payer 1; carrier 0.5 | **1** (payer side) | A dated regulation on brokers tied to non-payment: since 16 Jan 2026 a broker whose security falls below $75k is suspended; the transparency SNPRM is pending. *Caveat:* the rule acts on the bond, not directly on the payment workflow |
| A6 | — | **1** | A payments core reaches factoring, fuel cards, insurance, broker AP and shipper freight pay (C-09). This is the fintech layer (`submarket_selection.md` §6, implication 4) |
| W1 | carrier 0.5; payer 0.5 | **0.5** | The gathering points exist (factors, load boards, payment networks), but they are the competitors |
| W3 | — | **0.5** | Integration needed: TMS and AP, bank rails. The whole product includes money movement |
| W4 | — | **0.5** | Proven spend: factoring fees, quick-pay discounts. Software is not weak: modern networks already hold the payer side |
| W5 | carrier 0.5; payer 0.5 | **0.5** | Brokers are changing, but toward networks already chosen (BlueGrace, J.B. Hunt joined Triumph, N-Q03). OOIDA members were largely "not supportive" of factoring (N-N16), but there is no evidence of them switching |
| W6 | — | **0** | Slow. It needs capital and a bank partner, against entrenched networks (Triumph, DAT, Truckstop), for a self-funded team |

---

### C-06 · Matching spot loads with small carriers

#### Item 5: software penetration and why now

**How much still runs on phone:**
- Owner-operators, or their dispatcher, search load boards and then phone the broker to negotiate each load (N-F job row (a), *assumed*).
- OOIDA 2022, members under their own authority: 32% of business came from brokers directly, 23% from load boards, 22% from shippers, 2% from digital matching and 21% from "other" (N-N17, *verified*; OOIDA flag).
- Dispatch services charge "5% to 10%" of gross (N-F39, vendor).
- The share of owner-operators using a dispatch service is still not found (S3a check N; §5).

**Systems of record and plumbing:**
- **Load boards:**
  - DAT One: "more than 668,000 loads posted daily" (N-Q07, vendor);
  - Truckstop;
  - 123Loadboard, at $35-50 a month (N-Q26, *assumed*).
- **ELD:** hours available and location.
- **Broker TMSs.**
- **Factoring,** now inside the boards.
- **Plumbing verdict [our call]:** load boards integrate with brokers' TMSs, but no open carrier-side API was found. One AI dispatch tool "work[s] inside the DAT load board as a Chrome extension" (Numeo, N-Q20, *assumed*). That means platform risk.

**Named triggers:**
- **The DAT roll-up** (Roper 10-K, N-Q06, *verified*):
  - Trucker Tools (17 Dec 2024), Outgo (15 May 2025), Convoy (30 Jul 2025);
  - Canada's Loadlink combined with DAT in 2025;
  - DAT now runs "electronic marketplaces that automate broker and carrier freight capacity matching ... freight tracking and financing".
  - DAT's CEO: "load matching, compliance, visibility and now payments live under one roof" (N-Q08, *assumed*).
- **Truckstop** bought Denim (Aug 2025, N-Q27, *assumed*).
- **AI dispatch agents** (N-Q20, all *assumed*):
  - FleetWorks raised $17M in Oct 2025 for an "always-on AI dispatcher";
  - Bubba AI launched a "Voice AI Dispatcher" for owner-operators (Mar 2025);
  - Numeo;
  - DispatchMVP, from $49 a month.
- **Capacity:** Triumph, Q2 2026: "The reduction in supply is real and unlikely to reverse in the near term". It names "regulatory enforcement, industry efforts to combat fraud, and ... vicarious liability" (N-Q04, *verified*). That means a tighter spot market; it is not a rule on this job.
- **A caution:** Convoy shut down in Oct 2023 after raising about $1.1B (N-B29). Its assets now sit inside DAT (N-Q06).

#### Item 6: addressable work

| Side | Role (SOC; industry) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|---|
| Carrier | Dispatchers (43-5032; 484) | 34,890 | $58,690 | N-Q01, *verified* |
| Broker | Sales representatives of services (41-3091; 4885): carrier- and customer-sales reps | 23,890 | $74,810 | N-Q01 |
| Broker | Cargo and freight agents (43-5011; 4885) | 53,390 | $57,570 | N-Q01 |

- **The pool's payer** is the owner-operator: 274,660 one-truck carriers (N-F02). They are self-employed, so OEWS leaves them out.
- **Dispatch services' staff** cannot be separated out in OEWS **[our call]**.
- **R22:** searching, calling and negotiating rates is text, voice and number work. But R22 warns that relationship-heavy work resists automation, and "freight is a relationship-driven business" (R27).
- **R23:** negotiation is partly relationship work. Searching and paperwork are not.

#### Item 7: budget holder and implementation

**Budget:**
- The owner-operator. The dispatch fee (5-10% of gross) or the load-board subscription (DAT carrier plans $59-339 a month, N-F41) is an operating cost out of revenue.
- On the broker side: the carrier-sales manager, whose budget is the cost of covering loads.

**Implementation:**
- Data needed:
  - load-board credentials;
  - the carrier's lanes, equipment and target rates;
  - hours-of-service status from the ELD;
  - a phone or email channel to brokers.
- Value on day one is possible (book a load), live in days. It depends on the load boards tolerating third-party tools **[our call]**.

#### Item 9: competitors, substitutes and the incumbent map

**Named software, ≥10:**
- **Load boards:** DAT One, Truckstop, 123Loadboard (N-Q26).
- **Digital brokers and apps:** Uber Freight (N-F46); Convoy's technology, now DAT's.
- **AI dispatch:** FleetWorks, Numeo, Bubba AI, DispatchMVP, TruckSmarter (N-Q20).
- **Features inside larger products:** Trucker Tools' "automated booking" (N-Q06).

**The leader's share:**
- DAT calls DAT One "the industry's largest marketplace for spot truckload freight" (N-Q07, vendor).
- Blogs claim DAT and Truckstop "together control over 85%" of carrier digital freight matching, and that DAT posts "nearly double" Truckstop's loads (N-Q26, *assumed*).
- On those inputs, DAT ≈ 57% of posted loads **[our calc on assumed inputs]**.

**Dominance (C10): a weak candidate.**
- DAT may exceed half of load-board activity. But the inputs are vendor blogs, and the unit is posted loads, not carriers served.
- The card's savings pool is dispatch fees. Its incumbent is dispatch services, which are many and small.
- Settling this needs a survey or S5.

**Service firms:** dispatch services (5-10% of gross); brokers themselves; freight agents.

**How the job is done today:** self-dispatch on boards plus phone calls; direct shipper freight; doing nothing (driving home empty). No evidence of general-purpose AI tools in use.

**How incumbents charge (evidence only):**
- board subscriptions per month;
- dispatch fees as a % of gross;
- AI dispatch tools at $0-49+ a month;
- factoring fees charged inside the boards (Outgo, Denim).

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **0.5** | Mixed. Search and booking are office work; negotiation is relationship work (R22, R27); part of the cost (empty miles) is physical |
| A3 | carrier 0.5; broker 0.5 | **0.5** | A known cost (owner-operators rank "Broker Issues" first, R38), with no forcing event |
| A6 | — | **1** | A carrier-side booking core reaches payments (C-05), tracking (C-02), vetting (C-08), and other carrier types (hot-shot, flatbed, reefer) |
| W1 | carrier 1; broker 0.5 | **1** (carrier side) | Load boards gather most small carriers, as the two marketplaces did for C-39 at S2. But the main incumbent (DAT) owns the channel, so reach comes with platform risk |
| W3 | — | **0.5** | Integration needed; board access is not open to carrier-side tools |
| W4 | — | **0.5** | Proven spend: dispatch fees, subscriptions. Software is not weak: DAT One is being built out, and five AI dispatch tools already exist |
| W5 | carrier 0.5; broker 0.5 | **0.5** | Only 2% of OOIDA own-authority members' business comes via digital matching; Convoy is gone; buying is relationship-driven |
| W6 | — | **0.5** | Moderate. An AI dispatcher can be built fast, but it lives on DAT's and Truckstop's terms, against funded entrants |

---

### C-07 · A small brokerage's load back office

#### Item 5: software penetration and why now

**How much still runs on phone, email and spreadsheets:**
- **Brush Pass, 2025 survey of 895 "micro-cap" brokerages** (under $10M gross revenue) (N-B04; chart read to ±0.5 points):
  - 20 named systems hold about 74%;
  - McLeod ~16%, homegrown ~13%, ITS Dispatch (Truckstop) ~9%, Ascend ~6%, Aljex (Descartes) ~4%.
- **a16z (2022):**
  - "more than 60% of the freight brokerage market operates without software";
  - the process runs on "Excel, paper and pencil, and a telephone".
  - (R27; the figures are unsourced, *assumed*.)
- Even with a TMS, the costly work stays manual (card C-07; N-G44): calls, emails, re-keying rate confirmations, chasing documents, carrier payables.

**Systems of record and plumbing:**
- **The TMS:** APIs vary by vendor (*assumed*).
- **Load boards:** DAT and Truckstop integrations.
- **Tracking connectors:** MacroPoint, Trucker Tools (N-Q25, N-Q07).
- **Vetting:** Highway, MyCarrierPortal and RMIS plug into TMSs. Transfix built Highway into its TMS in June 2026 (N-Q24).
- **Payments:** TriumphPay plugs into the TMS and accounting system (N-Q02).
- **Accounting:** QuickBooks-type tools.
- **EDI** with larger shippers.
- **Plumbing verdict [our call]:** good, but heavy on integration.

**Named triggers:**
- **The broker-transparency SNPRM** has been at OMB since 27 Aug 2026 (N-Q11, N-Q12):
  - brokers would keep transaction records electronically and produce them within 48 hours of a request;
  - a broker on paper or spreadsheets would need software to comply (inference).
  - Not yet published.
- **The financial-responsibility rule** has been in force since 16 Jan 2026 (N-Q10, *verified*).
- **Montgomery v. Caribe Transport II** (14 May 2026): negligent-selection claims against brokers survive (N-Q15). Documented carrier vetting becomes part of the back office.
- **Broker counts are falling:**
  - FMCSA broker authorities fell 17.6% from Jan 2022 to end-2024 (N-B04, via check C);
  - they were down 8.6% year on year in March 2025 (Brush Pass, N-Q32, *assumed*).
  - Triumph, Q2 2026: "smaller brokers may face greater pressure as shippers reassess risk and liability" (N-Q04, *verified*).
- **AI agents are sold to large brokers first:**
  - HappyRobot: $150M Series C, Aug 2026, with a minimum annual spend of about $250k (N-Q18, *assumed*);
  - Vooma's customers include Echo, MODE, Arrive and NFI (N-Q19, *assumed*).
  - Triumph bought Greenscreens.ai, a broker pricing tool, in Q2 2025 (N-N14, *verified*).

#### Item 6: addressable work (all NAICS 4885)

| Role (SOC) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|
| Cargo and freight agents (43-5011) | 53,390 | $57,570 | N-Q01, *verified* |
| Sales representatives of services (41-3091) | 23,890 | $74,810 | N-Q01 |
| Customer service representatives (43-4051) | 10,920 | $51,980 | N-Q01 |
| Dispatchers (43-5032) | 8,350 | $54,280 | N-Q01 |
| Bookkeeping, accounting and auditing clerks (43-3031) | 7,530 | $52,600 | N-Q01 |
| Compliance officers (13-1041) | 4,520 | $72,420 | N-Q01 |
| Billing and posting clerks (43-3021) | 2,240 | $46,330 | N-Q01 |
| **Total** | **110,840** | **wage bill $6.71B** **[our calc]** | |

- **Coverage:** 4885 includes forwarders and customs brokers.
- **R22:** quoting, booking, documenting and paying are text and number office work. Sales calls are relationship work.
- **R23:** the back office passes the screen. Customer and carrier sales are close to the broker's "core product" and to relationships, so AI would augment them rather than replace them.

#### Item 7: budget holder and implementation

**Budget:**
- At small firms, the brokerage owner or president.
- Brush Pass: about a third of decision-makers sit in sales, 51% in customer- or carrier-facing roles, and under 10% in tech (N-Q33, *assumed*).
- The trade-off is software spend per seat against headcount.

**Implementation:**
- **A full TMS swap** moves every customer, carrier, rate and accounting link. That takes months and fails R28's "weeks, not months" (card C-07, *assumed*).
- **An add-on** (AI for email and calls, or document capture feeding the existing TMS) needs inbox and phone access plus one TMS integration. That takes weeks **[our call]**.

#### Item 9: competitors, substitutes and the incumbent map

**Named software:**
- **The micro-cap survey** names 20 systems (N-B04). G2 lists 76+ free TMSs (N-D37, *assumed*).
- **Named TMSs:** McLeod, ITS Dispatch, Ascend, Aljex, Tai, Revenova, BrokerPro, MVMNT, Rose Rocket (TMS.ai), Alvys, Transfix TMS (N-Q40, N-Q24; N-B26 to N-B28).
- **AI and data tools:** HappyRobot, Vooma, Parade, Greenscreens (Triumph).

**The leader's share:** McLeod, about 16% of micro-cap brokers (N-B04). The four largest vendors hold about 36% (check D).

**Dominance:** none.

**Service firms:**
- the freight-agent model (independent agents selling under a brokerage's authority);
- outsourced back-office firms (not researched);
- TriumphPay, which takes over carrier payables;
- factoring for brokers.

**How the job is done today:** a TMS plus email, phone and spreadsheets; 13% homegrown. No evidence of general-purpose AI tools in use.

**How incumbents charge (evidence only):**
- per seat or per company per month: Tai TMS from $945 a month (2 logins), Premium+ at $4,350 (N-Q40, vendor); Ascend has a free tier (N-Q40);
- a free core with money made from finance (MVMNT, N-B26). MVMNT has raised $24.5M; its last round was Feb 2023, with about 28 staff (N-Q43, *assumed*). Its outcome is unknown;
- annual minimums for AI agents (~$250k, N-Q18).

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **1** | Office work drives the cost: a $6.7B wage bill in 4885 **[our calc]** for quoting, booking, documents and payables |
| A3 | broker 1; shipper 0.5 | **1** (broker side) | A cluster of 2026 broker rules: the bond rule in force, the transparency SNPRM (electronic records), *Montgomery*. *Caveat:* the rule that most directly forces software is not yet published. Read as "pending", this row is 0.5 |
| A6 | — | **1** | The back office is the system of record. It reaches payments (C-05), vetting (C-08), tracking (C-02) and shipper tools (C-01, C-14); this is MVMNT's fintech thesis (R27) |
| W1 | broker 0.5; shipper 0 | **0.5** (broker side) | Brokers can be named from FMCSA records (N-B04) and are partly gathered: TIA (~1,600-1,700 members), load boards, TMS marketplaces |
| W3 | — | **0.5** | Integration needed: TMS, email, phone, load boards, accounting |
| W4 | — | **1** | Proven spend: seats and staff. The costly calls, email and re-keying remain unautomated in legacy TMSs, and AI agents are priced for large brokers |
| W5 | broker 0.5; shipper 0.5 | **0.5** | The wish to automate exists, but brokers resist TMS migration (R21, migration costs). Unknown for add-ons |
| W6 | — | **0.5** | Moderate. The field is crowded: 20+ incumbents plus funded AI. An add-on path is faster. Aljex's ~$32.4M sale with ~400 customers shows an exit path (N-B24) |

---

### C-08 · Carrier vetting and freight fraud

#### Item 5: software penetration and why now

**How much still runs manually:**
- Vetting today means manual FMCSA look-ups plus monitoring services (card C-08). No survey of small brokers' tool use was found (§5).
- **Fraud and theft are rising:**
  - CargoNet: confirmed thefts cost $454M in 2024 and about $725M in 2025 (N-N24, vendor);
  - TIA puts fraud at $0.5-1B a year (N-N25, N-N26, association, *assumed*);
  - FMCSA told Congress it lacks the data to quantify unlawful brokerage (N-N27, *assumed*).
- **Highway's own counts** (N-Q24, vendor):
  - 1,986,995 fraudulent emails blocked in 2025, up 117%;
  - 8,525,962 fraudulent phone numbers flagged;
  - in Q2 2026, fraudulent emails were up 48.5% on Q1, and communication-based attacks made up 50% of classified fraud vectors.

**Systems of record and plumbing:**
- **The FMCSA Company Census** is an open API on data.transportation.gov, updated daily (N-F02).
- **The L&I dataset** of operating authority and insurance history was frozen on 14 May 2026, when FMCSA moved to Motus. The Motus feed lists changes only (N-F03, N-F04).
- **Insurance certificates** come from insurance agents; no data feed was found (*assumed*).
- **Identity signals** come from phone, email, device and ELD location (Highway, N-G43).
- **Plumbing verdict [our call]:** the public registry is open, but insurance and authority history now require processing the Motus change feed.

**Named triggers:**
- **Motus**, FMCSA's new registration system (Federal Register, 29 Apr 2026, 91 FR 23144, N-Q09, *verified*):
  - Phase II was "planned for the second quarter of 2026", when "Motus will become available to all regulated entities";
  - identity is checked by IDEMIA against a government-issued ID;
  - MC/FF numbers are kept "in response to stakeholder feedback";
  - FMCSA cites "identity theft, hijacking FMCSA motor carrier accounts, selling of motor carrier numbers".
  - CRS adds "facial recognition and photos of driver licenses" and a Login.gov process (N-Q12).
- **The Supreme Court, *Montgomery v. Caribe Transport II*** (decided 14 May 2026, 9-0, opinion by Justice Barrett; N-Q15, *verified*):
  - negligent-hiring claims against brokers fall within the FAAAA's safety exception, so federal law does not pre-empt them;
  - requiring brokers "to exercise ordinary care in selecting a carrier" is permissible state safety regulation.
  - Brokers can no longer dismiss negligent-selection suits early, so documented vetting matters.
- **H.R. 8870, the BUILD America 250 Act** (ordered reported 22 May 2026 by 62-2; N-Q17, *assumed*). Sections listed by CRS (N-Q12):
  - §5007, "an automated red-flag system to spot suspicious information inputted by registrants";
  - §7109, "a 20-member advisory committee on cargo theft and freight fraud".
- **H.R. 5337, the Motor Carrier Safety Selection Standard Act** (introduced 11 Sep 2025; referred to subcommittee 12 Sep 2025; N-Q16, *verified*):
  - brokers that verify a carrier's registration, insurance and safety compliance "shall be considered reasonable and prudent" in selecting it;
  - a safe harbour that would define the vetting checklist. Pending.
- **CORCA (H.R. 2853)** passed the House on 12 May 2026 by 348-60 (N-Q42, *assumed*).
- **Insurers:** contingent cargo policies exclude losses from "Dishonest Acts" of unauthorised third parties, and insurers deny fraud losses that are not theft (N-Q41, *assumed*).

#### Item 6: addressable work

| Side | Role (SOC; industry) | Employed, May 2025 | Mean wage | Source |
|---|---|---|---|---|
| Broker | Compliance officers (13-1041; 4885): a proxy for carrier-onboarding and compliance specialists | 4,520 | $72,420 | N-Q01, *verified* |
| Broker | Cargo and freight agents (43-5011; 4885): carrier-sales reps vet carriers as they book | 53,390 | $57,570 | N-Q01 |
| Carrier | Dispatchers (43-5032; 484): the carrier's end user | 34,890 | $58,690 | N-Q01 |

- **R22:** registry, insurance and identity checks are text and data work.
- **R23:** human connection is no benefit here. A verification phone call is itself now a channel for attacks (communication-based fraud is 50% of vectors, N-Q24).

#### Item 7: budget holder and implementation

**Budget:**
- The broker's compliance or carrier-onboarding manager; at small brokers, the owner.
- The line is risk, compliance and insurance (claims, premiums). *Montgomery* shifts part of it to legal defence.

**Implementation:**
- Public FMCSA data plus the carrier's documents give value on the first carrier checked. Live in days **[our call]**.
- Self-serve tools already sell to small brokers: VerifyCarrier, DOTScreener, CarrierOwl (N-Q22, N-Q23).
- Deeper identity signals need data pooled across many brokers. That pooled data is Highway's advantage.

#### Item 9: competitors, substitutes and the incumbent map

**Named software, ≥12:**
- Highway;
- Descartes MyCarrierPortal, formerly MyCarrierPackets, acquired 18 Sep 2024 for about $24M upfront plus up to $6M in earn-outs (N-Q21);
- Truckstop RMIS (acquired 2021);
- Carrier411 ("over 1 million companies");
- SaferWatch;
- DAT CarrierWatch ("500,000+" companies);
- Carrier Assure (founded 2022; A-F carrier scores);
- DOTScreener, VerifyCarrier, CarrierOwl, Carrier Atlas, Cipher & Row (N-Q22, N-Q23).
- **Features inside TMSs:** Transfix TMS with Highway built in (N-Q24).

**The leader's share:**
- Highway: "1,000+ brokers, including 70 of the top 100" (FTV Capital, 2025, N-G43; investor claim, *assumed*).
- That is about 4% of 25,081 broker authorities **[our calc]**.

**Dominance (C10):** a candidate only for a segment of top-100 brokers (70%). Not shown for small brokers: there is no survey, and the count share is about 4%.

**Service firms:**
- insurance agents and insurers (underwriting, claims);
- compliance consultants;
- factors, which check who they pay;
- FMCSA's own Motus identity checks, a partial substitute.

**How the job is done today:** SAFER look-ups, calls to insurance agents, carrier packets, watch-lists; at small brokers, often nothing (*assumed*).

**How incumbents charge (evidence only):**
- "most of these vendors don't publish standard pricing and quote by volume" (N-Q22);
- per broker seat plus per monitored carrier, e.g. $50-500 a month per seat and $2-10 per carrier per month (N-Q23, *assumed*);
- carriers usually pay nothing (N-Q23).

#### The eight rows

| Row | By side | Suggested | Reason **[our call]** |
|---|---|---|---|
| A2 | — | **1** | Office work (registry, insurance and identity checks) is what fails when a loss happens |
| A3 | broker 1; carrier 0.5 | **1** (broker side) | Forcing events: *Montgomery* (May 2026), Motus (Q2 2026), and a fraud crisis (theft +60% in 2025, vendor) |
| A6 | — | **1** | An identity core reaches payee checks in payments (C-05), onboarding, insurance, shipper-side vetting, and carriers verifying brokers ("Highway for Carriers", N-Q24) |
| W1 | broker 0.5; carrier 0.5 | **0.5** | Partial channels: TIA, load boards (Truckstop owns RMIS; DAT runs CarrierWatch), TMS integrations |
| W3 | — | **1** | Data at hand: FMCSA public data and the carrier's documents. *Caveat:* L&I was frozen on 14 May 2026, and the Motus feed lists changes only. Identity signals need scale |
| W4 | — | **0.5** | Proven spend, yes. Software is not weak: the tools are funded and modern (Highway, Descartes, Truckstop, DAT) |
| W5 | broker 1; carrier 0.5 | **1** (broker side) | Evidence of the wish to change: 1,000+ brokers on Highway; liability after *Montgomery*; insurers denying fraud losses |
| W6 | — | **0.5** | Moderate. Crowded with funded leaders who pool data across brokers. There is an opening for cheap documented-diligence tools for small brokers |

---

## 3. For the coordinator (not a call)

### 3.1 Patterns across the six cards

**1. Four platforms now each cover several of these jobs.**

| Platform | Matching (C-06) | Tracking (C-02) | Payments and factoring (C-05) | Vetting (C-08) | Broker TMS (C-07) | Other | Sources |
|---|---|---|---|---|---|---|---|
| DAT (Roper) | DAT One; Loadlink; Convoy's technology | Trucker Tools | Outgo | CarrierWatch | — | rate data | N-Q06, N-Q07, N-Q22 |
| Truckstop | Truckstop board | not checked | Denim | RMIS | ITS Dispatch | app marketplace | N-Q22, N-Q27, N-B04 |
| Triumph | "rumored" (N-Q08) | — | TriumphPay, factoring, LoadPay | carrier performance scoring (Isometric) | — | Greenscreens pricing | N-N14, N-Q02 to N-Q04 |
| Descartes | — | MacroPoint | — | MyCarrierPortal | Aljex | — | N-Q21, N-B24 |

- **What it means [our call]:**
  - The expansion paths (A6) are contested.
  - W4's "weak or missing software" holds best where the platforms have not yet reached: detention (C-03) and AI for small brokers' back office (C-07).

**2. The 2026 broker-rule cluster lifts C-05, C-07 and C-08 together.** It comprises:
- the bond rule (16 Jan 2026);
- Motus (Q2 2026);
- *Montgomery* (14 May 2026);
- the transparency SNPRM (at OMB since 27 Aug 2026);
- H.R. 8870 (ordered reported May 2026).

These are not independent pieces of evidence. If the transparency rule stalls, the A3 of C-05 and C-07 weakens with it.

**3. AI agents are sold to big brokers first.** HappyRobot runs at 8 of the 10 largest, with a ~$250k minimum.
- Small brokers and owner-operators are the underserved end. This supports W4 on C-02 and C-07.
- But funded entrants are moving down-market: FleetWorks, Numeo, DispatchMVP.

**4. OEWS misses owner-operators.** On C-03, C-05 and C-06 the self-employed owner does the costly work, so role counts understate it.

**5. Forcing events and strong incumbents go together.**
- The job with no forcing event and the weakest payer (C-03, detention) has the emptiest software field.
- The jobs with forcing events (C-05, C-08) have the strongest incumbents.

**6. A small K5 input check:** C-02's OEWS wage is 0.6% above S2's figure, so no change.

### 3.2 Dominance show-stopper candidates (C10), for the coordinator to rule on

| Card | Vendor | Evidence | Scope where it could apply | Label |
|---|---|---|---|---|
| **C-05** | TriumphPay | Over 50% of unique brokered truckload transactions touched since Q4 2024; about 65% in Q4 2025 and Q2 2026 **[our calc]**. Serves 67 of the top 100 brokers and 8 of the top 10 | A payer-side segment of large brokers. **Not** shown for small brokers (roughly 1-4% by count **[our calc]**), shippers or carriers. Satisfaction is untested (S5) | Company filings, *verified*; the share is the company's own estimate |
| C-08 | Highway | 70 of the top 100 brokers | A top-100 segment only; about 4% of all brokers by count **[our calc]** | investor claim, *assumed* |
| C-06 | DAT | May hold over half of load-board activity (DAT ≈ 57% **[our calc]** on blog inputs) | The unit is posted loads, not carriers served; the card's pool is dispatch fees | *assumed* |
| C-02, C-03, C-07 | — | No vendor near half | — | — |

### 3.3 Partial subtotals: rows from this check only **[our calc]**

The coordinator adds A1 (20), A4 (15), A5 (15) and W2 (5).

| Card | A2 + A3 + A6 (of 50) | W1 + W3 + W4 + W5 + W6 (of 95) |
|---|---|---|
| C-02 | 37.5 | 62.5 |
| C-03 | 25 | 55 |
| C-05 | 45 | 35 |
| C-06 | 32.5 | 57.5 |
| C-07 | 50 | 55 |
| C-08 | 50 | 65 |

### 3.4 Readings made here [our call], to confirm or overturn

1. **C-02 W4 = 1** rests on "weak on coverage, missing at mid-sized shippers". The alternative reading is 0.5, because the platforms are mature.
2. **A3 = 1 on C-05 and C-07** rests on the 2026 broker rules. The alternative is 0.5, because the rule that most directly acts on each job is either indirect (C-05) or unpublished (C-07).
3. **C-06 W1 = 1** follows C-39's precedent at S2: the marketplace gathers the buyers. The channel owner is also the main incumbent.
4. **C-08 W3 = 1** despite the Motus data transition.

### 3.5 The biggest gaps

- **No survey of small brokers' tools** for tracking, vetting or payments. Brush Pass surveyed only TMSs (N-B04, N-Q32). This is the gap that decides the dominance tests.
- **Load-board shares:** vendor blogs only.
- **FMCSA's detention study:** no published results found.
- **The share of owner-operators using dispatch services:** still not found, so C-06's K4 stays open.
- **Factoring market shares** beyond Triumph's own rank, and the number of factoring firms.
- **Prices of vetting tools:** not published.
- **The shipper and receiver view of detention:** who pays, and how much. Only a secondary 50-70% figure.
- **Tracking compliance rates:** vendor figures only.

---

## 4. Sources

### 4.1 New sources (N-Q)

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-Q01 | U.S. BLS, Occupational Employment and Wage Statistics, May 2025, via Public Data API v2 (24 series: OEUN0000000{488500, 484000, 000000}{SOC}{01, 04}) | 2025 reference year | https://api.bls.gov/publicAPI/v2/timeseries/data/ | API download, *verified* | Employment and mean annual wage for 43-5011, 43-5032, 43-3031, 43-3021, 13-1041, 43-4051, 41-3091 in 4885; 43-5032, 43-3031, 43-3021 in 484; 43-5071 and 13-1081 in all industries |
| N-Q02 | Triumph Financial, Q4 2024 shareholder letter (Form 8-K exhibit) | filed 2025-01-22 | https://www.sec.gov/Archives/edgar/data/1539638/000162828025002174/tfin-shareholderletterx4q24.htm | full text (EDGAR), *verified* | "more than 50% of all brokered freight transactions touch our network"; $110B denominator; integration into payors' TMS and accounting; Intelligence segment; LoadPay counts |
| N-Q03 | Triumph Financial, Q4 2025 shareholder letter (8-K exhibit) | filed 2026-01-26 | https://www.sec.gov/Archives/edgar/data/1539638/000153963826000004/tfin-shareholderletterx4q25.htm | full text (EDGAR), *verified* | Breadth $71B and depth $117B annualized; payment volume $44.0B ($39.3B from brokers); "67 of the top 100 freight brokers and 8 of the top 10"; "hundreds of smaller brokers"; 9,053,274 invoices in Q4; LoadPay 6,000+ accounts, "integration to 400+ brokers"; interchange 1.68%; broker-margin erosion |
| N-Q04 | Triumph Financial, Q2 2026 shareholder letter (8-K exhibit) | filed 2026-07-21 | https://www.sec.gov/Archives/edgar/data/1539638/000153963826000028/tfin-shareholderletterx2q26.htm | full text (EDGAR), *verified* | Market re-sized from $110B to $135B; broker payment volume $49.4B; Network engagement $88.5B; "reduction in supply is real"; "vicarious liability"; smaller brokers under pressure; Capacity Intelligence launch |
| N-Q05 | Triumph (TFIN) Q4 2024 earnings call transcript (The Motley Fool) | call 2025-01-23 | https://www.fool.com/earnings/call-transcripts/2026/04/22/triumph-tfin-q4-2024-earnings-transcript/ | page summary via WebFetch; secondary transcript, *assumed* | "eclipsed the 50% market share goalpost"; goal of "60% to 65%" by year-end |
| N-Q06 | Roper Technologies, Form 10-K FY2025 | filed 2026-02-24 | https://www.sec.gov/Archives/edgar/data/882835/000088283526000009/rop-20251231.htm | full text (EDGAR), *verified* | DAT's description; acquisitions of Trucker Tools (2024-12-17), Outgo (2025-05-15) and Convoy (2025-07-30); Loadlink combined with DAT in 2025 |
| N-Q07 | DAT news release, "DAT acquires Trucker Tools, an innovator in real-time load tracking and visibility" | 2024-12-17 | https://www.dat.com/company/news-events/news-releases/dat-acquires-trucker-tools-an-innovator-in-real-time-load-tracking-and-visibility | page via WebFetch; vendor, *assumed* | "more than 750 leading freight brokers"; "350,000 owner-operators, carriers, and drivers"; "more than 668,000 loads posted daily" |
| N-Q08 | FreightWaves, "DAT acquires Outgo, enters race to become dominant freight exchange platform" | 2025-05-16 | https://www.freightwaves.com/news/dat-acquires-outgo-enters-race-to-become-dominant-freight-exchange-platform | page summary via WebFetch; trade press, *assumed* | Outgo's fractional factoring; DAT CEO quote; Triumph "rumored" to enter load matching |
| N-Q09 | Federal Register, FMCSA, "Availability of Motus, FMCSA's New Registration System", 91 FR 23144-23148, FR Doc 2026-08334 | 2026-04-29 | https://www.govinfo.gov/content/pkg/FR-2026-04-29/html/2026-08334.htm | full text (govinfo), *verified* | Phase II in Q2 2026 for all users; replaces URS and the FMCSA Portal; IDEMIA identity checks; MC/FF numbers kept; fraud language |
| N-Q10 | Federal Register, FMCSA, "Broker and Freight Forwarder Financial Responsibility; Extension of Compliance Date", 89 FR 107021-107026, FR Doc 2024-30509 | 2024-12-31 | https://www.govinfo.gov/content/pkg/FR-2024-12-31/html/2024-30509.htm | full text (govinfo), *verified* | Compliance date 16 Jan 2026; 49 CFR 387.307; $75,000; 7-day liquidity; suspension when security falls below $75,000 |
| N-Q11 | FreightWaves, "Broker Transparency Proposal Clears FMCSA and Heads to the White House" | 2026-08-29 | https://www.freightwaves.com/news/broker-transparency-proposal-clears-fmcsa-and-heads-to-the-white-house | page summary via WebFetch; trade press, *assumed* (headlines in CCJ, Overdrive and TT agree, but those pages returned 403) | SNPRM to OMB on 27 Aug 2026; electronic records; 48 hours; NPRM of 20 Nov 2024; ~7,000 comments |
| N-Q12 | Congressional Research Service, *Surface Transportation Reauthorization: Commercial Trucking Issues*, R48759 (mirror copy) | updated 2026-09-11 | https://www.everycrsreport.com/reports/R48759.html (congress.gov and crsreports.congress.gov returned 403) | page via WebFetch; *verified* at a mirror | Detention (Feb 2024 information gathering; Sep 2025 pilot); Motus; H.R. 8870 §§5007, 7109, 4019; H.R. 2853; S. 3950; ~25,000 active truck brokers, ~5,000 handle most brokered freight; broker transparency |
| N-Q13 | Federal Register, FMCSA ICR, "Impact of Driver Detention Time on Safety and Operations", 89 FR 12413-12416, FR Doc 2024-03256 | 2024-02-16 | https://www.govinfo.gov/content/pkg/FR-2024-02-16/html/2024-03256.htm | full text (govinfo), *verified* | Objectives; ~80 carriers and 2,500 drivers; ELD, TMS and telematics data; 12 months; no report date given |
| N-Q14 | Federal Register, FMCSA, "Hours of Service of Drivers; Pilot Program To Allow Commercial Drivers To Pause Their 14-Hour Driving Window", 90 FR 44872-44879, FR Doc 2025-17938 | 2025-09-17 | https://www.govinfo.gov/content/pkg/FR-2025-09-17/html/2025-17938.htm | full text (govinfo), *verified* | Split Duty Period Pilot; ~256 drivers; 30 minutes to 3 hours; detention language; comments due 17 Nov 2025 |
| N-Q15 | Supreme Court, *Montgomery v. Caribe Transport II, LLC*, No. 24-1238 (LII copy; the slip opinion is at supremecourt.gov/opinions/25pdf/24-1238_1b7d.pdf) | decided 2026-05-14 | https://www.law.cornell.edu/supremecourt/text/24-1238 | page via WebFetch, *verified* | 9-0, Barrett J.; negligent-hiring claim saved by the FAAAA safety exception; "ordinary care in selecting a carrier" |
| N-Q16 | govinfo BILLSTATUS, H.R. 5337 (119th Congress), Motor Carrier Safety Selection Standard Act | introduced 2025-09-11 | https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr5337.xml | XML download, *verified* | Sponsor Rep. Stauber; referred to the Highways and Transit Subcommittee on 2025-09-12; CRS summary of the safe harbour |
| N-Q17 | H.R. 8870, BUILD America 250 Act: T&I Committee release; Holland & Knight; Conference Board; congress.gov bill page (snippets) | May 2026 | https://transportation.house.gov/news/documentsingle.aspx?DocumentID=410054 ; https://www.congress.gov/bill/119th-congress/house-bill/8870 | search snippets, *assumed* | Markup on 21-22 May 2026, 62-2; $580B over FY2027-31; FMCSA $5B; trucking sections |
| N-Q18 | Forkast, "HappyRobot Wants $1.2 Billion to Run Your Freight by Voice" | 2026-08-20 | https://forkast.news/happyrobot-wants-1-2-billion-to-run-your-freight-by-voice/ | page summary via WebFetch; secondary with vendor claims, *assumed* | Series C on 4 Aug 2026, $150M, $1.22B; 150+ customers; 8 of 10 largest brokers; ~$250k minimum annual spend |
| N-Q19 | Vooma funding (Business Wire, 2024-12-02; FreightWaves); RXO AI call automation (search result) | 2024-12; 2026 | https://www.businesswire.com/news/home/20241202150186/en/ ; https://www.freightwaves.com/news/vooma-grabs-16-6m-in-funding-as-brokers-prepare-for-market-swing | snippets, *assumed* | $16.6M; customers Echo, MODE, Arrive, NFI; RXO "more than 500,000 calls" in Q1 2026 |
| N-Q20 | AI dispatch tools for carriers: FleetWorks; Bubba AI (GlobeNewswire, 2025-03-25); Numeo; DispatchMVP; TruckSmarter | 2025-26 | https://numeo.ai/best-ai-dispatch-tools ; https://www.globenewswire.com/fr/news-release/2025/03/25/3048891/0/en/ ; https://dispatchmvp.ai/dispatch-software-owner-operators | snippets; vendor, *assumed* | FleetWorks $17M (Oct 2025); Numeo runs inside DAT as a Chrome extension; DispatchMVP from $49/month |
| N-Q21 | Descartes, "Descartes Acquires MyCarrierPortal" | 2024-09-18 | https://www.descartes.com/resources/news/descartes-acquires-mycarrierportal | page via WebFetch; vendor, *assumed* | ~$24M upfront plus up to $6M earn-out; product description; no customer count |
| N-Q22 | DOTScreener, "Carrier Vetting Software Compared" | 2026-05-23 | https://dotscreener.com/blog/carrier-vetting-software-compared | page via WebFetch; vendor, *assumed* | Seven tools and their owners; "most of these vendors don't publish standard pricing"; Carrier411 "over 1 million companies"; CarrierWatch "500,000+" |
| N-Q23 | Carrier onboarding overviews: Carrier Atlas; CarrierOwl; Truckstop "Top 5 Compliance Tools for Freight Brokers" | 2025-26 | https://carrieratlas.com/carrier-packets.php ; https://carrierowl.com/blog/carrier411-alternatives ; https://truckstop.com/blog/compliance-tools-for-brokers/ | snippets; vendor, *assumed* | Seat and per-carrier price ranges; Carrier Assure (2022, A-F); Truckstop owns RMIS; carriers pay nothing |
| N-Q24 | Highway press releases: Q4 2025 Freight Fraud Index (2026-01-26); Q2 2026 Freight Fraud Index (2026-07-28); Transfix-Highway partnership (2026-06-23) | 2026 | https://www.globenewswire.com/news-release/2026/01/26/3225705/0/en/ ; https://www.globenewswire.com/news-release/2026/07/28/3334396/0/en/ ; https://www.businesswire.com/news/home/20260623233493/en/ | Q2 2026 page via WebFetch; others snippets; vendor, *assumed* | 1,986,995 emails and 8,525,962 phone numbers (2025); Q2 2026 +48.5% emails; 50% communication-based vectors; Highway built into Transfix TMS |
| N-Q25 | Descartes MacroPoint pricing page; MacroPoint Capacity Network release (DC Velocity); LoadManager MacroPoint integration listing | undated; 2025 | https://macropoint.com/news/rvp-pricing/ ; https://www.dcvelocity.com/articles/52783 ; https://www.loadmanager.com/product/macropoint-integration-for-freight-brokers/ | pricing page via WebFetch; others snippets; vendor, *assumed* | "$5 per load ... as low as 40 cents"; "over 200k carriers"; connector $149.95 setup plus $39.95-49.95/month |
| N-Q26 | Load-board comparisons: ExpertMarket; American Truckers LLC; Truck Dispatch Experts | 2025-26 | https://www.expertmarket.com/fleet-management/best-load-boards-for-truckers ; https://www.americantruckersllc.com/blog/best-load-boards-owner-operators-2026.html | snippets, *assumed* | "DAT and Truckstop together control over 85%"; DAT "nearly double" Truckstop; 123Loadboard $35-50/month |
| N-Q27 | Payment competitors: Truckstop acquires Denim (TheTrucker; PYMNTS, 2025); Relay Payments (TT; DC Velocity); Freehand freight-payment roundup | 2025-26 | https://www.thetrucker.com/trucking-news/business/truckstop-com-acquires-denim-for-instant-freight-payments ; https://www.ttnews.com/articles/relay-freight-payment ; https://www.freehand.ai/articles/best-freight-payment-software | snippets, *assumed* | Denim deal (Aug 2025); RelayDirect ">$1.5 billion"; TriumphPay same-day ACH to "more than 150,000 carriers" |
| N-Q28 | Quick-pay fee pages: FreightWaves ("The Broker Offers You Quick Pay..."); OTR Solutions; eCapital; Truckstop | 2025-26 | https://www.freightwaves.com/news/the-broker-offers-you-quick-pay-and-it-sounds-like-free-money-read-this-before-you-take-it ; https://otrsolutions.com/blog/quick-pay-for-truckers | snippets, *assumed* | Quick pay 1.5-5%, 2-5 days; standard terms 30-45 days |
| N-Q29 | Detention features and tools: Samsara "Time on Site Report" (help centre); Motive detention blog; DetentionIQ; DockClaim (403); Glocate | undated | https://kb.samsara.com/hc/en-us/articles/360043256251-Time-on-Site-Report ; https://gomotive.com/blog/detention-time-cost-safety-data/ ; https://www.detentioniq.com/ | snippets; vendor, *assumed* | Geofence detention reports; standalone tool names |
| N-Q30 | TheTrucker, "Will FMCSA's latest study of driver detention generate results?" | 2024-05-01 | https://www.thetrucker.com/trucking-news/truckload-authority/trends-in-trucking/will-fmcsas-latest-study-of-driver-detention-generate-results | page summary via WebFetch; secondary, *assumed* | Comment counts; payers pay "50% to 70%"; two-hour standard |
| N-Q31 | FleetOwner, "DOT seeks mandatory detention pay via reauthorization proposal" (Grow America Act); CCJ, "Bill seeks compensation for excessive detention" (snippet) | 2014-04-30; undated | https://www.fleetowner.com/news/regulations/article/21687796/ ; https://www.ccjdigital.com/business/article/14919730/bill-seeks-compensation-for-excessive-detention | FleetOwner page via WebFetch; CCJ snippet; *assumed* | Proposal and reactions (ATA against, OOIDA for); a later bill that did not advance |
| N-Q32 | Brush Pass Research, blog index pages 1-2 | 2023-2025 | https://brushpassresearch.blog/ ; https://brushpassresearch.blog/page/2/ | page summaries via WebFetch; secondary blog, *assumed* | Post list; broker authorities -8.6% year on year (Mar 2025) and -9.9% (Jan 2025); TMS surveys cover micro-, growth- and mid-cap brokers only |
| N-Q33 | Brush Pass Research, "Who makes buying decisions at freight brokerages?" | 2023-08-31 | https://brushpassresearch.blog/2023/08/31/who-makes-buying-decisions-at-freight-brokerages/ | page via WebFetch; no method stated, *assumed* | About a third in sales; 51% in customer- or carrier-facing roles; tech under 10% |
| N-Q34 | OOIDA, "About Us" | current | https://www.ooida.com/about-us/ | snippet; association claim, *assumed* | 150,000+ members; 240,000+ trucks |
| N-Q35 | TIA membership (Supply Chain 24/7 profile; Truckstop marketplace listing) | current | https://www.supplychain247.com/company/transportation_intermediaries_association | snippets, *assumed* (tianet.org was blocked earlier, check B) | 1,600-1,700+ member companies |
| N-Q36 | Samsara REST API overview; ELD integration pages (Alvys help centre; Load Market; Industrial Monitor Direct) | current | https://developers.samsara.com/docs/rest-api-overview ; https://help.alvys.com/en/articles/11697799-samsara-eld-telematics | snippets, *assumed* | Public API; token needs the carrier's data-sharing addendum; tracking links usable by Trucker Tools and FourKites |
| N-Q37 | EDI 214 definitions (1 EDI Source; TrueCommerce; TraceLink) | current | https://www.1edisource.com/resources/edi-transactions-sets/edi-214/ | snippets, *assumed* | X12 214 carrier shipment status message; used by truckload and LTL carriers |
| N-Q38 | Tracking-compliance claims (Trucker Tools blog; CCJ, "Load boards start new chapter on freight visibility"; Truckstop broker tracking guide) | 2021-26 | https://www.truckertools.com/digital-load-tracking-basics-what-brokers-need-to-know-about-real-time-visibility/ ; https://www.ccjdigital.com/technology/article/15065904/ | snippets; vendor, *assumed* | Required 80-95%; "as low as 30 to 40 percent in past years"; small carriers resist tracking |
| N-Q39 | Visibility surveys as quoted by Locus (Tive 2024 survey; Gartner 2025 CSCO survey) | 2024-25 | https://locus.sh/blogs/real-time-shipment-visibility-platforms-2026/ | snippet; vendor, *assumed* | Tive: 24% see 75-100% of shipments, 45% under half (244 respondents) |
| N-Q40 | Broker TMS pricing roundups (SoftwareConnect; BrokerPro; ARK TMS) | 2026 | https://softwareconnect.com/roundups/best-freight-broker-software/ ; https://www.brokerpro.com/pricing/ | snippets; vendor, *assumed* | Tai from $945/month (2 logins), Premium+ $4,350; Ascend free tier; McLeod price not published |
| N-Q41 | Insurance and fraud: Avalon Risk, "Claims Corner: Dishonest Acts of Third-Parties"; WTW (2023); DOTScreener on contingent cargo | 2023-26 | https://www.avalonrisk.com/quest-news/claims-corner-dishonest-acts-of-third-parties ; https://www.wtwco.com/en-us/insights/2023/09/ | snippets, *assumed* | Contingent cargo excludes dishonest acts of third parties; fraud losses denied |
| N-Q42 | Cargo-theft legislation: C.H. Robinson May 2026 market update; NMFTA; Land Line (S. 2938) | 2026 | https://www.chrobinson.com/en-us/resources/insights-and-advisories/north-america-freight-insights/may-2026-freight-market-update/government-regulations/ ; https://nmfta.org/news/cargo-thieves-have-gone-corporate-congress-is-finally-catching-up/ | snippets, *assumed* | CORCA (H.R. 2853) passed the House 12 May 2026, 348-60; S. 2938 (Sen. Young) |
| N-Q43 | MVMNT profiles (Crunchbase; PitchBook; CB Insights) | 2026 | https://www.crunchbase.com/organization/the-mvmnt-group ; https://pitchbook.com/profiles/company/465487-48 | snippets, *assumed* | $24.5M raised; last deal Feb 2023; 28 employees |
| N-Q44 | Factoring-company roundups (FreightFactoringUSA; ATS; Solution Scout) | 2026 | https://freightfactoringusa.com/best-freight-factoring-companies-compared/ ; https://www.atsinc.com/blog/carriers/top-factoring-companies-for-trucking | snippets, *assumed* | Names only (RTS, OTR Solutions, Apex, TAFS); no volume ranking |
| N-Q45 | Visibility vendor roundups (Gartner Peer Insights RTTVP market page; Chain; GetAFreightQuote) | 2025-26 | https://www.gartner.com/reviews/market/real-time-transportation-visibility-platforms | snippets, *assumed* | Vendor names only |

### 4.2 Earlier sources reused (not re-fetched unless stated)

- **Resource notes:** R21, R22, R23, R27, R28, R30, R38.
- **S0 checks:** N-B03, N-B04, N-B22, N-B24, N-B26, N-B27, N-B28, N-B29 (check B); N-C23, N-C24 (check C); N-D34, N-D35, N-D37 (check D).
- **S1 scans:** N-E20 (scan E); N-F02, N-F03, N-F04, N-F28, N-F30, N-F39, N-F40, N-F41, N-F46, N-F48, N-F49, N-F60, N-F63, N-F70, N-F74, and the job table in §2 of scan F; N-G38, N-G39, N-G42, N-G43, N-G44 (scan G).
- **S3a check N:** N-N14 (**re-read 2026-09-15**: text search for the Payments network, LoadPay, Greenscreens and competition), N-N15, N-N16, N-N17, N-N24, N-N25, N-N26, N-N27, N-N28.
- **EDGAR full-text search** (efts.sec.gov) was used only to locate Triumph's letters. It is not cited as a source.

---

## 5. Could not access, or not found

**Blocked:**
- **CRS R48759:** congress.gov and crsreports.congress.gov returned 403. The everycrsreport.com mirror was used (N-Q12).
- **Federal Register pages** redirected to an "unblock" page. The govinfo copies were used (N-Q09, N-Q10, N-Q13, N-Q14).
- **The transparency SNPRM:** CCJ and Overdrive articles returned 403. FreightWaves was used (N-Q11).
- **DockClaim's detention-tool comparison** returned 403.

**Searched, not found (the attempts):**
- **FMCSA detention study results (C-03).**
  - (1) "FMCSA driver detention study results released report 2026";
  - (2) "FMCSA truck driver detention time data collection 2025 2026 rulemaking Congress bill detention";
  - (3) the February 2024 notice itself (N-Q13), which gives no report date.
  - CRS's September 2026 review mentions only the 2024 information gathering and the 2025 pilot. Treated as not published.
- **A detention-pay bill in the 119th Congress (C-03).**
  - (1) "bill introduced 2025 truck driver detention time compensation Congress";
  - (2) CRS R48759's trucking provisions;
  - (3) the FleetOwner and CCJ history (2014 and earlier). None found.
- **Visibility adoption among small brokers and mid-sized shippers (C-02).**
  - (1) "survey percent of shippers using real-time transportation visibility platform 2025";
  - (2) "Descartes MacroPoint Trucker Tools brokers load tracking market share";
  - (3) "freight brokers tracking compliance rate percent of loads tracked".
  - Only vendor figures were found (N-Q38, N-Q39).
- **A survey of small brokers' vetting, tracking or payment tools (C-02, C-05, C-08).**
  - (1) Brush Pass index pages 1 and 2 (TMS and pricing-tool surveys only);
  - (2) the Highway and Descartes releases (no small-broker counts);
  - (3) Triumph's letters (large-broker counts plus "hundreds of smaller brokers"). Not found.
- **Load-board market shares (C-06).**
  - (1) "DAT load board market share Truckstop 123Loadboard";
  - (2) "DAT Freight & Analytics number of subscribers ... Roper 10-K";
  - (3) Roper's FY2025 10-K text (no subscriber or share figures).
  - Vendor blogs only (N-Q26).
- **Factoring shares and the number of factoring firms (C-05).**
  - (1) "largest transportation factoring companies North America ... ranking volume" (review rankings only);
  - (2) Triumph's 10-K and letters (only its own "#2" rank, N-N15).
  - Dropped after two attempts, because the review rankings carried no volume data at all.
- **Vetting-tool prices (C-08).**
  - (1) "Highway carrier identity platform pricing" (not published);
  - (2) the DOTScreener comparison ("most ... don't publish");
  - (3) the Carrier Atlas overview (ranges only, N-Q23).
- **Share of owner-operators using dispatch services (C-06):** not retried. S3a check N made three attempts (OOIDA surveys, ATRI and FMCSA, Overdrive).
- **Broker TMS adoption beyond Brush Pass (C-07):** one search found only paid market-research summaries, which were not used.
- **Tooling:** the scholarly-search MCP server was not connected, and was not used.
