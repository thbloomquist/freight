# Run 01, S3b: fact sheets

> **Stage S3b of `submarket_selection.md` §4, "Desk evidence". Written 2026-09-15** for the 18 cards on the S3b list set at S3a (`3a_unknowns.md` §5.2).
> **What each sheet holds:** the eleven S3b items (`submarket_selection.md` §4 S3b; template in §13), the S3a results the card carries, and its provisional desk score.
> **The scores and the shortlist of 4-6** are in `3_shortlist.md`.
> **Evidence:**
> - three research checks made for this step:
>   - `research/s3b_check_Q_carrier_broker_jobs.md` (N-Q01 to N-Q45): C-02, C-03, C-05, C-06, C-07, C-08;
>   - `research/s3b_check_R_shipper_spend_jobs.md` (N-R01 to N-R26): C-01, C-09, C-10, C-11, C-14, C-17;
>   - `research/s3b_check_S_facility_fleet_trade_jobs.md` (N-S01 to N-S43): C-04, C-15, C-18, C-19, C-20, C-22;
> - everything held from S0-S3a: the cards (`1_candidates.md`), the knock-outs (`2_knockouts.md`), S3a (`3a_unknowns.md`) and their checks;
> - two re-parses made here: the 2022 Economic Census concentration file (N-D01) and SUSB 2022 (N-D04). They give the top-4 and top-50 shares and the small-firm shares for every side.
>
> **Status of this file:** complete. There are 18 fact sheets (§2.1-§2.3), written 2026-09-15. The founders confirmed the shortlist of five on 2026-09-15 (`3_shortlist.md` §8).

## How to read this

**One sheet per card.** Each has a short header (the card's sentence and its status) and a table with one row per S3b item:
1. **Buyers per side:** counts, with sources.
2. **Savings pool:** the S3a range, with how it is built and which inputs are our judgement.
3. **Fee potential:** the savings pool × the S0 fee shares (10%, 20%, 35%), plus the average saving and fee per paying buyer.
   - These are modelling assumptions, not prices. The fee itself is deferred to segment selection (F-7, F-8).
   - The **central fee pool** (20% of the range's geometric midpoint) becomes the bubble size in S4.
4. **Structure:** the top-4 and top-50 shares of each side's revenue (Economic Census 2022), and the revenue share of firms under 20 and under 500 staff (SUSB 2022). Plus the five-forces points that matter, chiefly who keeps a saving once it is made.
5. **Software penetration and why now:** how much of the job is still paper, phone and spreadsheets; whether the systems of record have APIs (Bushel's "plumbing", R30); and a named trigger for change now.
6. **Addressable work:** the roles doing the costly work (BLS OEWS counts and wages), and whether it is text- and number-heavy office work (R22, R23).
7. **Budget holder and implementation:** who pays, and whether a product could show value on day one and go live in weeks (R28).
8. **Cyclicality and growth:** the K11 results, including the Test 2 customer-survival flag (`3a_unknowns.md` §4.5).
9. **Competitors and substitutes:** the incumbent map, as W4's evidence (check D §D5): named vendors, the leader's share, service firms, bundled features, how the job is done today, and any dominance candidate (§5.5, C10).
10. **Fee unit:** the unit a fee would be counted on, and the K11 series or proxy used.
11. **Segments:** the K2 split variable and likely segments, and the sides and segments already ruled out (C12, C15).

After the table come the S3a items the card carries, then the **provisional desk score** (the S4 method at desk level; §3 below).

**Labels:**
- *verified*: read at the source;
- *assumed*: a snippet, a secondary summary, a vendor claim, memory, or a blocked page;
- **[our calc]**: arithmetic done here;
- **[our call]**: a judgement made here.

Source IDs point to the check files, and to earlier files for R-, N-A to N-P.

**Freight words used below** (first use; more in each check file):
- **TMS:** transportation management system, the main office software of a broker, carrier or shipper.
- **ELD:** electronic logging device, the in-cab device every interstate truck must use. It also knows where the truck is.
- **Check call:** a call or text asking a driver where a load is.
- **Factoring:** selling an unpaid freight invoice for cash now, minus a fee.
- **Detention:** paid waiting time at a dock beyond the free time.
- **LTL:** less-than-truckload, where several shippers' pallets share one trailer.
- **OTIF:** on time, in full, a retailer's delivery rule, with fines.
- **Drayage:** short truck moves of containers to and from a port.
- **ACE:** Automated Commercial Environment, US Customs' filing system.

---

## 1. Shared data used by several sheets

### 1.1 Structure of each side (Economic Census 2022; SUSB 2022)

- **Sources:** Economic Census 2022 concentration file, US, all establishments (N-D01, re-parsed here from EC2200SIZECONCEN), and SUSB 2022 (N-D04, re-parsed from `us_state_6digitnaics_2022.txt`).
- **HHI:** the 2022 file flags it "X" (not published) for every code below, so the top-4 share stands in as the check for a dominant firm.
- **Codes:** SUSB 2022 uses 2017 NAICS codes; they map one-to-one for the codes shown, except where noted.
- **Label:** *verified* data; shares **[our calc]**.

| Side (NAICS) | Firms (EC 2022) | Top-4 share | Top-50 share | Firms under 20 staff: share of receipts | Under 500 staff: share of receipts |
|---|---|---|---|---|---|
| Manufacturing (31-33) | 240,644 | 6.9% | 29.0% | 3.3% | 23.7% |
| Wholesale (42) | 265,472 | 6.7% | 30.5% | 9.2% | 33.5% |
| Truckload, long-distance (484121) | 53,705 | 16.7% | 37.4% | 24.3% | 53.8% |
| LTL (484122) | 7,675 | 40.8% | 82.9% | 7.9% | 17.5% |
| Local general freight, incl. drayage (484110) | 43,243 | 2.3% | 10.5% | 51.7% | 89.2% |
| Local specialized (484220) | 31,927 | 1.8% | 9.9% | 33.5% | 66.4% |
| Long-distance specialized (484230) | 10,701 | 14.3% | 38.1% | 18.4% | 59.0% |
| Freight arrangement: brokers, forwarders, customs brokers (488510) | 17,130 | 9.9% | 34.3% | 24.1% | 61.9% |
| General warehousing (493110) | 7,138 | 24.2% | 49.1% | 8.9% | 35.6% |
| Refrigerated warehousing (493120) | 719 | 51.3% | 73.9% | 10.3% | 41.5% |
| Couriers (492110) | 6,553 | 87.7% | 90.9% | 2.6% | 9.6% |
| Grocery wholesale (4244) | 27,414 | 15.1% | 53.5% | 8.9% | 31.4% |
| Beer, wine and spirits wholesale (4248) | 3,734 | 25.4% | 63.4% | 4.1% | 37.9% |
| Hardware and plumbing wholesale (4237) | 9,368 | 19.8% | 57.5% | 8.5% | 39.1% |
| Drug wholesale (424210) | 6,632 | 50.3% | 88.8% | 1.6% | 7.9% |
| Fabricated metals (332) | 49,631 | 5.0% | 20.9% | 9.7% | 53.5% |
| Machinery (333) | 18,779 | 12.5% | 35.8% | 4.5% | 33.2% |
| Furniture makers (337) | 13,818 | 10.9% | 38.4% | 11.8% | 50.2% |
| Durable wholesale (423) | 144,016 | 9.0% | 30.7% | 9.3% | 35.5% |
| E-commerce and mail order (454110; 2017 file, SUSB firms) | 53,556 | — | 63.2% (2017) | 9.2% | 23.6% |

**The A4 score from this table** (`0_criteria.md` §4):
- The top-50 share sets the band: under 20% = 1; 20-80% = 0.5; over 80% = 0.
- Add 0.5, capped at 1, where firms under 20 staff hold 25% or more of receipts.
- The better side counts (C5).
- Counting owner-operators without payroll would lower trucking's top-50 share further: all trucking (484) goes from 28.3% to 22.3% (check D).

### 1.2 Fee potential [our calc]

- **Method:** fee pool = savings pool × fee share, at the S0 shares of 10%, 20% and 35% (`0_criteria.md` §5).
- **Per buyer:** the average saving per paying buyer = savings pool ÷ the buyer count in item 1. The fee per buyer is 20% of that. It is capped by the saving, as S3b item 3 asks.
- These are averages. Real buyers vary widely around them, and the fee itself is deferred (F-7, F-8).

### 1.3 The customer-survival flag

K11 Test 2 is recorded for every side in `3a_unknowns.md` §4.5. The sheets quote the result for their own sides.

---

## 2. Fact sheets

### 2.1 Carrier and broker jobs (research: check Q)

#### C-02 · Load status, for mid-sized shippers and receivers

> **Sentence:** "Knowing where each load is and when it will arrive, for mid-sized shippers and receivers, handled today by brokers' and carriers' check calls, emails and portals."
> **Status after S3a:** S3b. Open: K5 (the removable share is our judgement) and K11 (no load count; proxies in the 13-20% band).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Shippers: 95,579 mid-sized manufacturers and wholesalers (20-499 staff). Receivers: 19,979 warehouse sites. Freight side: 25,081 active broker authorities (14,019 payroll firms in NAICS 4885, BDS 2023) | *verified*: N-E17, N-F03, N-C05 |
| 2 | Savings pool | **$0.18-0.73B a year.** Staff time on status: 53,390 cargo and freight agents × $57,230 × 20-40% of time on status × 30-60% removable. O*NET supports the 20% low end: tracking is a daily task for 79% of cargo agents | counts and wage *verified* (N-F22, N-K09); time and removable shares **[our call]**; N-N28 |
| 3 | Fee potential | 10%: $18-73M · 20%: $36-146M · 35%: $63-255M · **central fee pool $72M**. Per broker authority: saving $7.2k-29.1k a year; a 20% fee is $1.4k-5.8k. Per mid-sized shipper: saving $1.9k-7.6k | **[our calc]** |
| 4 | Structure | Shippers: fragmented but large (manufacturing top-50 29.0%; wholesale 30.5%). Brokers: top-50 34.3%, top-4 9.9%, 24.1% of receipts in firms under 20 staff. **Who keeps the saving:** brokers bundle status into their margin, so the broker keeps a labour saving unless shippers push for price | §1.1; *verified* data |
| 5 | Software penetration and why now | Check calls persist: 79% of cargo agents track loads daily. About 10% of shippers under $25M of freight spend use a TMS (*assumed*). Tracking coverage of small carriers has run "as low as 30 to 40 percent" (vendor). **Plumbing:** ELD APIs exist, but each carrier must consent; EDI 214 status messages come mainly from larger carriers; the broker TMS holds the load list. **Why now:** AI voice agents for check calls (HappyRobot raised $150M in Aug 2026 and runs at 8 of the 10 largest brokers, *assumed*); DAT bought Trucker Tools (Dec 2024, *verified*); location now doubles as fraud proof | N-N28, N-E20, N-Q38, N-Q36, N-Q18, N-Q06 |
| 6 | Addressable work | Brokers: cargo and freight agents (43-5011), 53,390 at $57,570; customer service reps, 10,920. Carriers: dispatchers, 34,890. Shippers: logisticians, 251,040; receiving clerks, 816,870. Text- and number-heavy office work with no human-connection benefit. It is supporting work for a broker, not its core product | *verified*: N-Q01; R22, R23 |
| 7 | Budget holder and implementation | The broker's operations manager or owner (payroll plus per-load tracking fees); the shipper's logistics manager. **An AI check-call layer:** value on day one, live in weeks (it needs the load list and phone numbers). **ELD-based coverage:** months, because each carrier must consent. **A shipper's view across all its brokers:** months | **[our call]** on check Q's evidence; R28 |
| 8 | Cyclicality and growth | **K11 Test 3 open:** truck tonnage -14.6% monthly in 2008-09 (13-20%), -5.5% in 2022-25. **Test 1** pass: broker firms +13.5% (2017-22); BLS 4885 employment +5.3% to 2035. **Test 2:** brokers and shippers clear; the carrier side (4841) is raised | `3a_unknowns.md` §4.1, §4.5; `2_knockouts.md` §4.3 |
| 9 | Competitors and substitutes | **At least 10 named:** project44, FourKites, Shippeo, Descartes MacroPoint, Trucker Tools (DAT); Tive; AI agents HappyRobot and Vooma; ELD share links; TMS portals. No share published. Trucker Tools serves 750+ brokers, about 3% of authorities. **No dominance found.** Service firms: brokers and 3PLs bundle status into their price. Today: phone, text and email, portals, or doing nothing. Charges: MacroPoint $5 down to $0.40 a load; HappyRobot about a $250k annual minimum (*assumed*) | N-F48, N-F49, N-Q07, N-Q18, N-Q25 |
| 10 | Fee unit and K11 series | Loads tracked. Proxy: ATA truck tonnage (no load count exists) | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry (column X). Likely segments: mid-sized manufacturers against distributors; also small against large brokers on the freight side. Ruled out: the LTL carrier side (K10) | `2_knockouts.md` §4.5, §4.2 |

**Provisional desk score:**
- **Axis A 80:** A1 1, A2 1, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 55:** W1 0.5, W2 0, W3 0.5, W4 0.5, W5 1, W6 0.5.
- **W4 = 0.5 [our call], against check Q's suggested 1.** Mature platforms exist, and funded AI entrants are moving down-market. On Q's reading, W would be 62.5. Reasons for every row are in `3_shortlist.md` §2.

#### C-03 · Detention and extra charges at the dock

> **Sentence:** "Getting detention and other extra-service charges recorded, billed and paid, for shippers and receivers whose docks hold trucks, handled today by small truckload carriers' dispatchers and billing clerks with paper logs, phone and email."
> **Status after S3a:** S3b. Open: K11. No series of detained stops exists, and detention becomes less frequent in downturns, so the lean is toward failing **[our call]**.

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Carriers: 531,374 active interstate for-hire carriers, 56.6% with one truck; so about 230k run 2 or more trucks **[our calc]**. The one standalone tool sells to carriers with 5-150 trucks. Payers: shippers, receivers and distribution centres (column X; 19,979 warehouse sites) | *verified*: N-F02, N-E17; N-D35 (vendor) |
| 2 | Savings pool | **$0.27-0.64B a year.** Detention's yearly cost to drivers and carriers, $1.35-1.60B (2018), × 20-40% recovered through better capture. A vendor says manual processes capture only about 40% of what is owed | base *verified* (N-F30); share **[our call]**; N-D34 (*assumed*) |
| 3 | Fee potential | 10%: $27-64M · 20%: $54-128M · 35%: $94-224M · **central $83M**. Per carrier (all 531k): saving $508-1,204 a year; a 20% fee is $102-241. Small per carrier, so the business needs many customers or bigger fleets | **[our calc]** |
| 4 | Structure | Carriers: truckload top-50 37.4% (24.3% of receipts in firms under 20 staff); long-distance specialized 38.1%. Receivers: general warehousing 49.1%. **Who keeps the saving:** the payer (shipper or receiver) holds the power. It pays only 50-70% of what carriers lose (*assumed*), and the saving is a transfer from payer to carrier (payer ≠ saver) | §1.1; N-Q30 |
| 5 | Software penetration and why now | Drivers were detained at 39.3% of stops (2023). Fees are collected on fewer than half of invoices (*assumed*). The job runs on paper logs, driver texts, phone and email. **Plumbing:** good on the carrier side (ELD geofences in Samsara and Motive; TMS features); none from the facility. **Why now:** no binding trigger. FMCSA's detention study (2024) has no published report; the split-duty pilot (Sep 2025) works around detention; no detention-pay bill is in Congress | N-C24, N-D34, N-Q29, N-Q13, N-Q14, N-Q12 |
| 6 | Addressable work | Carrier dispatchers, 34,890 at $58,690; bookkeeping clerks in trucking, 16,270; billing clerks, 5,840. Owner-operators do it themselves and are not counted. Capture and billing are office work; the waiting itself is physical | *verified*: N-Q01 |
| 7 | Budget holder and implementation | The carrier owner, as revenue recovery, so the first recovered charge can pay for the tool. The standalone tool charges $59-349 a month. The shipper's DC manager has the opposite interest. **Implementation:** ELD geofence timestamps + the rate confirmation's terms + the invoice route. Live in weeks, but collection still depends on the payer | N-D35 (vendor); **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 open:** no series of detained stops. Repeated ATRI surveys show detention rose into 2018 and fell by 2023. **Test 1** pass. **Test 2** raised on both carrier sides (4841 at 2.1× the economy's death rate; 4842 lost 15.2% of its firms) | `3a_unknowns.md` §4.1, §4.5; N-L21 |
| 9 | Competitors and substitutes | **About 10-12:** TMS features (Trimble TMW, McLeod); telematics geofencing (Samsara, Motive, Verizon Connect, Geotab); standalone tools ChargeGuard, DetentionIQ, DockClaim, Glocate. No shares; no dominance. Service firms: factors bill accessorials; dispatch services; brokers pass the charge through or absorb it. Today: paper and phone, and often the charge is never billed | N-D34, N-D35, N-Q29 |
| 10 | Fee unit and K11 series | Detained stops (or detention invoices). No series exists | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by carrier fleet size or equipment. Likely segments: dry-van fleets of 5-150 trucks, reefer fleets, flatbed; or by receiver type (grocery DCs). Nothing ruled out | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 67.5:** A1 1, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 0.5.
- **Axis W 55:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.5.

#### C-05 · Getting small carriers paid

> **Sentence:** "Invoicing, approving and paying small carriers' freight bills, for the shippers and brokers who give them loads, handled today by carriers' billing clerks on paper and by factoring companies."
> **Status after S3a:** S3b. K4 settled pass. Open: K5, and K11 (13-20% on tonnage).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Carriers: 446,405 run 10 or fewer trucks. Payers: 25,081 broker authorities, plus shippers | *verified*: N-F02, N-F03 |
| 2 | Savings pool | **$99-798M a year.** Small carriers' revenue, $222.6B, × 23-28% factored (OOIDA surveys, association-flagged) × a 1.29-3.2% fee (Triumph's filed discount rate; OOIDA members' average) × 15-40% removable | base *verified* (N-D04, N-D05); shares sourced (N-N14 to N-N17); removable **[our call]** |
| 3 | Fee potential | 10%: $10-80M · 20%: $20-160M · 35%: $35-279M · **central $56M**. Per small carrier: saving $222-1,788 a year; a 20% fee is $44-358. Per broker: saving $3.9k-31.8k | **[our calc]** |
| 4 | Structure | Carriers: very fragmented (local general freight top-50 10.5%, with 51.7% of receipts in firms under 20 staff; local specialized 9.9%). Brokers: top-50 34.3%. **Payment networks are concentrated:** Triumph's own estimate is that its network touches about 65% of brokered truckload dollars. **Who keeps the saving:** the carrier; the factoring discount is the price of cash | §1.1; N-Q02 to N-Q04 |
| 5 | Software penetration and why now | Carriers email PDF packets and wait 30-45 days (*assumed*); 23-28% factor. The payer side is already on payment networks. **Plumbing:** it exists, and incumbents own most of it (TriumphPay's integrations to broker TMSs, factoring portals). **Why now:** the broker financial-responsibility rule, in force 16 Jan 2026 ($75k security; suspension below it); the broker-transparency proposal at OMB since 27 Aug 2026; load boards buying payment firms (DAT-Outgo, May 2025; Truckstop-Denim, Aug 2025) | N-Q28, N-N16, N-N17, N-Q10, N-Q11, N-Q06, N-Q27 |
| 6 | Addressable work | Carrier bookkeeping clerks, 16,270, and billing clerks, 5,840; broker bookkeeping clerks, 7,530, and billing clerks, 2,240. Most of the pool is not labour: the factoring discount is a price of capital | *verified*: N-Q01 |
| 7 | Budget holder and implementation | The carrier owner (the factoring fee comes out of revenue: a finance cost, not a software budget); the broker's controller or AP manager. **Months to go live:** it needs money movement, a bank partner, AP and TMS integration, and capital for advances. It fails R28 unless the product is billing-only | **[our call]** on check Q's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 open:** tonnage in the 13-20% band. **Test 1** pass. **Test 2:** the carrier side is raised; brokers are clear | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **At least 12:** payment networks (TriumphPay, DAT-Outgo, Truckstop-Denim, Relay); factors (Triumph, RTS, OTR Solutions, Apex, TAFS, eCapital); carrier billing tools. **Dominance candidate: TriumphPay.** It touches about 65% of brokered truckload dollars and serves 67 of the top 100 brokers, but only an estimated 1-4% of small brokers by count **[our calc]**. It is a candidate for a large-broker payer segment only; satisfaction is untested (S5). Charges: % of invoice, per-transaction fees, card interchange | N-Q02 to N-Q05, N-Q27, N-Q44 |
| 10 | Fee unit and K11 series | Invoices paid (or dollars factored). Proxy: ATA truck tonnage | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by carrier fleet size or equipment. Likely segments: owner-operators (1 truck) against small fleets (2-10); by equipment. **Flag:** a payer segment of large brokers carries the TriumphPay dominance candidate, to be tested at S5 | `2_knockouts.md` §4.5; check Q §3.2 |

**Provisional desk score:**
- **Axis A 82.5:** A1 1, A2 0.5, A3 0.5, A4 1, A5 1, A6 1.
- **Axis W 35:** W1 0.5, W2 0, W3 0.5, W4 0.5, W5 0.5, W6 0.
- **A3 = 0.5 [our call], against check Q's suggested 1.** The bond rule acts on brokers' security, not on the payment job, and the transparency rule is unpublished. On Q's reading, A would be 95.

#### C-06 · Matching spot loads with small carriers

> **Sentence:** "Finding and booking spot truckloads, for brokers and shippers who need a load covered, handled today by owner-operators working load boards and independent dispatch services."
> **Status after S3a:** S3b. Open: K4 (no count of dispatch-service use), K5, and K11 (no spot series for 2008-09).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 274,660 one-truck interstate carriers. Brokers: 25,081 authorities | *verified*: N-F02, N-F03 |
| 2 | Savings pool | **$51M-1.10B a year.** 274,660 × 10-30% using dispatch services × $123-222k gross (Census nonemployer average; OOIDA) × a 5-10% fee (vendor) × 30-60% removable | carriers and gross sourced; use share and removable **[our call]**; fee vendor (*assumed*) |
| 3 | Fee potential | 10%: $5-110M · 20%: $10-220M · 35%: $18-385M · **central $47M**. Per owner-operator: saving $186-4,001 a year; a 20% fee is $37-800 | **[our calc]** |
| 4 | Structure | Carriers are very fragmented: most are nonemployers (914,821 in truck transportation) and local trucking's top-50 share is 10.5%. **The channel is concentrated:** DAT and Truckstop are said to hold over 85% of load-board activity (*assumed*). **Who keeps the saving:** the owner-operator | §1.1; N-D05; N-Q26 |
| 5 | Software penetration and why now | OOIDA members under their own authority get 23% of their business via load boards and 2% via digital matching. Dispatch services charge 5-10% of gross. **Plumbing:** load boards connect to broker TMSs, but no open carrier-side API was found. **Why now:** the DAT roll-up (Trucker Tools, Outgo, Convoy, Loadlink, 2024-25); AI dispatch agents (FleetWorks raised $17M, Oct 2025); capacity leaving the market in 2026. **Caution:** Convoy shut down in 2023 after raising about $1.1B | N-N17, N-F39, N-Q06, N-Q20, N-Q04, N-B29 |
| 6 | Addressable work | Carrier dispatchers, 34,890; broker carrier-sales reps (41-3091), 23,890 at $74,810. The owner-operator, the payer, is self-employed. Search and booking are office work; rate negotiation is relationship work ("freight is a relationship-driven business", R27) | *verified*: N-Q01; R22, R27 |
| 7 | Budget holder and implementation | The owner-operator: the dispatch fee or the board subscription (DAT carrier plans $59-339 a month) comes out of revenue. **Implementation:** days to weeks, but it depends on the load boards tolerating third-party tools. One AI tool runs inside DAT as a browser extension, which is platform risk | N-F41; N-Q20; **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 open:** no spot-load series for 2008-09; DAT's index about -1% in 2022-25 (*assumed*). **Test 1** pass. **Test 2** raised on the carrier side | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **At least 10:** load boards (DAT One, Truckstop, 123Loadboard); digital brokers (Uber Freight); AI dispatch (FleetWorks, Numeo, Bubba AI, DispatchMVP, TruckSmarter). **Weak dominance candidate:** DAT may hold about 57% of posted loads **[our calc on assumed inputs]**. But the card's pool is dispatch fees, whose incumbents (dispatch services) are many and small. Today: self-dispatch on boards plus phone, or driving home empty | N-Q07, N-Q20, N-Q26 |
| 10 | Fee unit and K11 series | Loads booked (per load, or % of gross). No 2008-09 series | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by fleet size or equipment; includes expedited and hot-shot (merge M-4). Nothing ruled out | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 72.5:** A1 0.5, A2 0.5, A3 0.5, A4 1, A5 1, A6 1.
- **Axis W 57.5:** W1 1, W2 0, W3 0.5, W4 0.5, W5 0.5, W6 0.5.
- **W1 = 1** follows S2's C-39 precedent: a marketplace gathers the buyers. Here the channel's owner is also the main incumbent.

#### C-07 · A small brokerage's load back office

> **Sentence:** "Quoting, booking, tracking, documenting and paying each truckload, for shippers who use small freight brokers, handled today by small brokerages on broker TMSs, phone and email."
> **Status after S3a:** S3b. Open: K11 (no industry count of brokered loads).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Brokerages: 15,591 freight-arrangement firms under 500 staff, of which about 50-70% are truck brokers, so about 7,800-10,900 **[our calc]**. 87% of arrangement firms have under 20 staff. 25,081 active broker authorities. Shippers that use small brokers | *verified*: N-K05, N-F01, N-F03 |
| 2 | Savings pool | **$0.28-1.3B a year.** 164,684 staff of arrangement firms under 500 × 50-70% in truck brokerage × $57,230 × 20-40% of time on re-keying, tracking, documents and payables × 30-50% removable | counts and wage *verified*; shares **[our call]** |
| 3 | Fee potential | 10%: $28-130M · 20%: $56-260M · 35%: $98-455M · **central $121M**. Per small brokerage (7,796 firms): saving $36k-167k a year; a 20% fee is $7.2k-33.4k. Per authority (25,081): saving $11k-52k | **[our calc]** |
| 4 | Structure | Brokers: top-50 34.3%, top-4 9.9%; 24.1% of receipts in firms under 20 staff and 61.9% under 500. **Who keeps the saving:** the brokerage (staff time), in a business with falling margins (median broker gross margins "some of the lowest levels observed", Dec 2025) | §1.1; N-Q03 |
| 5 | Software penetration and why now | Micro-cap brokers use 20+ TMSs (McLeod about 16%, homegrown about 13%). Calls, email and re-keying stay manual even with a TMS. ">60% of the freight brokerage market operates without software" (2022, unsourced). **Plumbing:** good but heavy on integration (TMS, load boards, tracking, vetting and payment plug-ins). **Why now:** the transparency proposal (electronic records within 48 hours; at OMB since 27 Aug 2026); the bond rule (Jan 2026); *Montgomery* (May 2026); broker counts falling (FMCSA authorities -17.6% from 2022 to 2024); AI agents priced for large brokers | N-B04, R27, N-Q11, N-Q10, N-Q15, N-Q18 |
| 6 | Addressable work | NAICS 4885: 110,840 staff in seven office roles, a wage bill of $6.71B **[our calc]**. Cargo agents 53,390; sales reps 23,890; customer service 10,920; dispatchers 8,350; bookkeeping 7,530; compliance 4,520; billing 2,240. The back office passes R23's screen; sales stays relationship work | *verified*: N-Q01 |
| 7 | Budget holder and implementation | The brokerage owner or president. Decision-makers sit in sales and operations; under 10% in tech (*assumed*). **A full TMS swap:** months, so it fails R28. **An AI or document add-on:** weeks | N-Q33; **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 open:** no industry count of brokered loads; single firms diverge. **Test 1** pass: firms +13.5%; BLS +5.3%. **Test 2** clear (0.9-1.0× the economy), with exits above entries in both years. FMCSA broker authorities fell 17.6% (2022-24) while payroll firms held | `3a_unknowns.md` §4.1, §4.5; N-C05 |
| 9 | Competitors and substitutes | **20+ TMSs:** McLeod, ITS Dispatch, Ascend, Aljex, Tai, Revenova, BrokerPro, MVMNT, Rose Rocket, Alvys, Transfix TMS. **AI and data tools:** HappyRobot, Vooma, Parade, Greenscreens. The leader, McLeod, has about 16%; **no dominance.** Service firms: the freight-agent model, outsourced back offices, TriumphPay for payables. Charges: Tai $945-4,350 a month; Ascend has a free tier; MVMNT offers a free core and earns from finance | N-B04, N-Q40, N-Q43, N-B26 |
| 10 | Fee unit and K11 series | Brokered loads, or seats. No industry count | `3a_unknowns.md` §4.1 |
| 11 | Segments | K2 ✓ (one market). Likely segments: brokerages by size (micro-cap under $10M, growth); by equipment (dry van, reefer, flatbed); by customer industry. Nothing ruled out | `2_knockouts.md` §2 |

**Provisional desk score:**
- **Axis A 80:** A1 1, A2 1, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 55:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.5.
- **A3 = 0.5 [our call], against check Q's suggested 1.** The rule that most directly forces software, the transparency rule, is unpublished. On Q's reading, A would be 92.5.

#### C-08 · Carrier vetting and freight fraud

> **Sentence:** "Checking that a carrier is real, insured and actually hauling the load, for brokers and shippers hiring carriers they don't know, handled today by manual FMCSA look-ups and carrier-monitoring services."
> **Status after S3a:** S3b. K11 passed at S2 (theft rose in both downturns). Open: K4 (no neutral loss data; the regulator says it has none), K5, and K7 (a saving that is mostly risk avoided; S5).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 25,081 active broker authorities (14,019 payroll firms in NAICS 4885), plus shippers that use spot carriers | *verified*: N-F03, N-C05 |
| 2 | Savings pool | **$91-690M a year.** Theft of $454M (2024 confirmed thefts, corrected at S3a) to $725M (2025) (CargoNet, vendor), plus fraud of $0 to $1.0B (TIA, association-flagged, no method stated), × 20-40% prevented by vetting | theft and fraud *assumed*; share **[our call]**; N-N24 to N-N26 |
| 3 | Fee potential | 10%: $9-69M · 20%: $18-138M · 35%: $32-241M · **central $50M**. Per broker authority: saving $3.6k-27.5k a year; a 20% fee is $0.7k-5.5k | **[our calc]** |
| 4 | Structure | Brokers: top-50 34.3% (24.1% of receipts in firms under 20 staff). Carriers, the side being vetted: very fragmented (top-50 about 10%). **Who keeps the saving:** the broker or its insurer. Insurers deny fraud losses that are not theft (*assumed*), so the broker carries them | §1.1; N-Q41 |
| 5 | Software penetration and why now | Manual FMCSA look-ups plus monitoring services. Fraud is rising: Highway blocked 2.0M fraudulent emails in 2025, up 117% (vendor). **Plumbing:** FMCSA's Company Census is an open daily API. Its authority and insurance dataset was frozen on 14 May 2026, when FMCSA moved to Motus, which publishes changes only. **Why now:** Motus registration with ID checks (Q2 2026, *verified*); *Montgomery v. Caribe* (14 May 2026, 9-0: negligent-selection claims against brokers stand, *verified*); H.R. 8870 (an automated red-flag system; a fraud advisory committee); H.R. 5337 safe harbour (pending) | N-Q24, N-F02, N-Q09, N-Q15, N-Q12, N-Q16 |
| 6 | Addressable work | Broker compliance officers (13-1041), 4,520 at $72,420; cargo agents, who vet as they book, 53,390. Registry, insurance and identity checks are data work. A human verification call is now itself an attack channel: half of classified fraud vectors are communication-based | *verified*: N-Q01; N-Q24 |
| 7 | Budget holder and implementation | The broker's compliance or onboarding lead; at small brokers, the owner. The budget line is risk, insurance and, after *Montgomery*, legal defence. **Implementation:** days; FMCSA data plus the carrier's documents give value on the first carrier checked. Deeper identity signals need data pooled across brokers | **[our call]** on check Q's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 pass** (S2): theft incidents rose in both downturns. **Test 1** pass. **Test 2:** brokers clear | `2_knockouts.md` §4.3; `3a_unknowns.md` §4.5 |
| 9 | Competitors and substitutes | **At least 12:** Highway; Descartes MyCarrierPortal (bought Sep 2024 for about $24M upfront); Truckstop RMIS; Carrier411; SaferWatch; DAT CarrierWatch; Carrier Assure; DOTScreener; VerifyCarrier; CarrierOwl; Carrier Atlas; Cipher & Row. **Highway serves 70 of the top 100 brokers** (investor claim), but about 4% of brokers by count. It is a dominance candidate for a top-100 segment only. Service firms: insurers and agents, compliance consultants, factors. Today: SAFER look-ups, calls to insurance agents, carrier packets; at small brokers, often nothing. Prices are mostly unpublished | N-G43, N-Q21, N-Q22, N-Q23 |
| 10 | Fee unit and K11 series | Carriers vetted or monitored, or loads checked. Series: fraud and theft incidents, which rose | `2_knockouts.md` §4.3 |
| 11 | Segments | K2 ✓. Likely segments: small brokers (under 20 staff); mid-sized brokers; shippers hiring spot carriers; carriers verifying brokers. **Flag:** a top-100-broker segment carries the Highway dominance candidate (S5) | check Q §3.2 |

**Provisional desk score:**
- **Axis A 100:** A1 1, A2 1, A3 1, A4 1, A5 1, A6 1.
- **Axis W 65:** W1 0.5, W2 0, W3 1, W4 0.5, W5 1, W6 0.5.
- **Two caveats:**
  - A1 sits on the line: the savings midpoint is $250.6M against a $250M threshold. At 0.5, A would be 90.
  - A4 = 1 comes from the carrier side, the side being vetted, under the better-side rule (C5). The paying side, brokers, is 0.5.
  - Fee feasibility (S4) will weigh K7: the saving is mostly risk avoided.

### 2.2 Shipper spend, audit and planning jobs (research: check R)

**Shared buyer.** All six cards sell to small and mid-sized manufacturers and distributors: 95,579 firms with 20-499 staff (57,309 manufacturers and 38,270 wholesalers; N-E17). They split into two families (check R §3.1):
- **Money back after shipping: C-09, C-10, C-11.** One set of data (bill of lading, proof of delivery, carrier invoice, rate, class) and one budget story: contingency fees paid from recoveries.
- **Buying and planning before shipping: C-01, C-14, C-17.** This is TMS territory: heavier integration, relationship-driven buying, and savings measured against moving benchmarks or agreed baselines.

**A3 reading used for all 18 cards [our call].** A3 = 1 needs a dated rule, rule change or crisis that acts on the card's own job. Triggers that act on the whole freight market (the 2026 rate rise, capacity) or on a neighbouring job count 0.5. So do rules still pending. Check R suggested 1 on C-01; this file uses 0.5 (`3_shortlist.md` §2).

#### C-01 · Buying truckload capacity, for mid-sized shippers

> **Sentence:** "Buying truckload capacity and rates, for mid-sized manufacturers and distributors, handled today by freight brokers and truckload carriers over phone, email and spreadsheets."
> **Status after S3a:** S3b. Open: K7 (whether shippers credit software for savings against a moving benchmark; S5) and K11 (13-20% on tonnage).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 95,579 mid-sized shippers. Carriers: 53,705 truckload firms. Brokers: 25,081 authorities | *verified*: N-E17, N-D01, N-F03 |
| 2 | Savings pool | **$0.52-4.6B a year.** Mid-sized shippers' truckload spend ($387B × 15-30% = $58-116B) × 3-8% overpaid when capacity is bought by phone and email × 30-50% removable. Census cross-check: truckload carriers' receipts are $172.7B (employer firms, 2022), against CSCMP's $387B, which counts more carrier types | base *assumed* (N-K22); shares **[our call]**; N-N13 |
| 3 | Fee potential | 10%: $52-460M · 20%: $104-920M · 35%: $182M-1.61B · **central $309M**. Per shipper: saving $5.4k-48k a year; a 20% fee is $1.1k-9.6k | **[our calc]** |
| 4 | Structure | Shippers: manufacturing top-50 29.0%, wholesale 30.5%. Truckload carriers: top-50 37.4%, top-4 16.7%. Brokers: 34.3%. **Who keeps the saving:** the shipper. But in a tightening market carriers and brokers gain pricing power, and the saving is measured against a benchmark that swings by about ±40% (R34) | §1.1 |
| 5 | Software penetration and why now | Most mid-sized shippers buy without a procurement tool. About 10% use a TMS below $25M of freight spend (*assumed*; other surveys conflict); 17% of respondents are fully automated (vendor survey). **Plumbing:** larger shippers tender by EDI 204 and 990; the rest by email and portals; rate benchmarks must be bought. **Why now:** a capacity squeeze (freight spend +28.1% year on year in Q2 2026, U.S. Bank index, *assumed*); FMCSA's non-domiciled CDL rule, effective 2026-03-16 (*verified*); English-proficiency out-of-service orders (*assumed*). The squeeze helps brokers more than it helps a newcomer | N-E20, N-F28, N-D31, N-R13, N-R15 |
| 6 | Addressable work | Logisticians (13-1081): 56,330 in manufacturing and 27,360 in wholesale. Transportation managers (11-3071): 29,990 and 34,350. Wage bills $7.29B and $7.73B **[our calc]**. Quotes and bids are office work; relationships with core carriers partly fail R23 ("freight is a relationship-driven business", R27) | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | The logistics or transportation manager's freight budget, or purchasing. A bid tool can show below-benchmark rates in its first bid cycle, but the credit is contested (K7). **Live in weeks** for a lane-bid or spot-quote tool; months for a TMS (R28) | **[our call]**; R28, R34 |
| 8 | Cyclicality and growth | **K11 Test 3 open:** truck tonnage -14.6% (2008-09); BLS long-distance output -17.7%. **Test 1** pass. **Test 2:** shippers clear; the carrier side is raised | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **12 procurement tools named:** Transporeon, Freehand, Keelvar, GoComet, GoodShip, MercuryGate and Sleek, the main seven all tagged "Enterprise"; plus Shipsy, Freightify, Fretron, Trimble, FreightFox. Gartner evaluated 17 TMS vendors in 2025. The field is consolidating (Körber bought MercuryGate in Oct 2024; Trimble bought Transporeon in Dec 2022). No shares; **no dominance.** **The real incumbents are service firms:** 25,081 brokers (spread about 15% of gross), digital brokers, and managed-transportation 3PLs. Charges: broker spread; 3PL per shipment, % of spend or gainshare; software by transaction, performance or subscription | N-F46, N-D32, N-R11, N-R10, R33, N-F17 |
| 10 | Fee unit and K11 series | Truckloads bought. Proxy: ATA truck tonnage | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry (column X). Ruled out: the LTL carrier side (K10) | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 75:** A1 1, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 42.5:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.
- On check R's A3 = 1, Axis A would be 87.5.

#### C-09 · Auditing and paying truckload and LTL bills

> **Sentence:** "Checking and paying truckload and LTL freight bills, for mid-sized manufacturers and distributors, handled today by accounts-payable clerks, contingency audit firms and, for larger shippers, audit-and-payment providers."
> **Status after S3a:** S3b, a clean pass on every knock-out.

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 95,579 mid-sized shippers. Carriers: the billing side | *verified*: N-E17 |
| 2 | Savings pool | **$0.34-3.2B a year.** Truckload plus LTL spend of $451B × 15-30% for mid-sized shippers × 1-3% overpaid (below audit vendors' claimed 2-8%) × 50-80% caught by software. The pool is overcharges, not clerk time: processing an invoice costs a median of $5.83 (APQC, 2018) | base *assumed* (N-K22); shares **[our call]**; N-R14 |
| 3 | Fee potential | 10%: $34-320M · 20%: $68-640M · 35%: $119M-1.12B · **central $209M**. Per shipper: saving $3.6k-33k a year; a 20% fee is $0.7k-6.7k. Contingency audit firms take 25-50% of what they recover | **[our calc]**; N-A25, N-A26 |
| 4 | Structure | Shippers: column X. Carriers: truckload 37.4%; LTL 82.9% (that side is ruled out). **Freight audit and payment providers:** the two leaders each touch about 4-5% of trucking dollars. **Who keeps the saving:** the shipper, as recoveries | §1.1; check D §D5 |
| 5 | Software penetration and why now | Cass serves "large manufacturing, distribution and retail enterprises" (*verified*); 51% of *enterprise* shippers outsource the job (Gartner via a vendor, *assumed*). Mid-sized shippers use an AP clerk, a small audit firm, or nobody. **Plumbing:** carrier invoices as EDI 210 or PDF; BOL and POD images; rate sheets held by the shipper; ERP payables; AI document reading makes PDFs usable. **Why now:** the NMFC class dockets (2025-07-19; 2026-05-23) change LTL bills after pickup (*verified*); payment fraud hit 76% of US firms in 2025 (AFP survey, association-flagged); spend +28.1% (*assumed*); AI audit entrants (Loop raised $95M, Apr 2026). Cass's own 10-K warns AI could make its offerings "obsolete" | N-D30, N-R05, N-R02, N-R03, N-R01, N-D31, N-R06 |
| 6 | Addressable work | Bookkeeping and AP clerks (43-3031): 91,710 in manufacturing, 100,750 in wholesale; wage bill $10.41B, of which freight bills are a small part. Matching bills to rates and proofs is text and number work, and passes R23 | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | Finance and AP (the controller), with logistics co-deciding. A contingency audit needs no budget line: the shipper keeps 50-75% of recoveries. **A look-back audit** shows value within days and goes live in weeks (paid invoices plus rate agreements). **Paying carriers** takes months: ERP integration, a bank partner, carrier onboarding | N-A26; **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 pass:** Cass's invoice count -10.5% (2008-09) and -6.4% (2022-25). **Test 1** pass. **Test 2:** shippers clear | `2_knockouts.md` §4.3; `3a_unknowns.md` §4.5 |
| 9 | Competitors and substitutes | **16 named:** Cass, U.S. Bank, Trax, nVision Global, CTSI-Global, Intelligent Audit, CT Logistics, Data2Logistics, RateLinx, TranzAct, enVista, Loop, Freehand, Freightgate, FreightPOP, MyCarrier. Gartner's 2026 guide lists about 15 (not seen). **No dominance:** the leaders hold about 4-5% each and aim at enterprises. **Service firms:** "numerous small transportation bill audit firms", few national. Features: TMS settlement modules; ERP three-way match. Today: pay as billed, a yearly contingency post-audit, or nothing. Charges: per item plus float (Cass); % of spend or gainshare; contingency of 25-50% | N-D30, N-F50, N-F51, N-R06, N-R21, N-R22 |
| 10 | Fee unit and K11 series | Freight invoices, from Cass's invoice count (one processor, but the direct unit) | `2_knockouts.md` §4.3 |
| 11 | Segments | **K2 = S:** split by shipper industry. Ruled out: the LTL carrier side (K10). Adjacent: parcel audit (C-12, on the reserve list) | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 92.5:** A1 1, A2 1, A3 1, A4 0.5, A5 1, A6 1.
- **Axis W 65:** W1 0.5, W2 0, W3 1, W4 1, W5 0.5, W6 0.5.
- **W6 = 0.5 [our call], against check R's suggested 1.** Funded AI entrants are targeting the same work, and the paying half needs a bank partner. On R's reading, W would be 77.5.
- W3 = 1 assumes an audit-first product; with payment from day one, W3 is 0.5.

#### C-10 · Cargo loss and damage claims

> **Sentence:** "Filing and recovering cargo loss and damage claims, for small and mid-sized shippers, handled today by shippers' own staff, their brokers, and contingency claims services."
> **Status after S3a:** S3b. Open: K4 (filing and denial rates are vendor-only), K5 and K11 (no claim counts).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 95,579 mid-sized shippers (all sizes: 239,265 manufacturers, 277,932 wholesalers). Carriers: 7,204 LTL firms; 531,374 for-hire carriers | *verified*: N-E17, N-F01, N-F02 |
| 2 | Savings pool | **$62-442M a year.** LTL claims paid (Census LTL receipts $65.7B × a 0.3-0.5% claims ratio anchored on five carriers' filings), grossed up to the loss never recovered with a vendor's filing and denial rates. Plus truckload ($360M-1.08B, **[our call]**). Total $1.04-2.21B unrecovered × 30-50% for small and mid-sized shippers × 20-40% removable | N-N07 to N-N13; N-K21 (*assumed*); shares **[our call]** |
| 3 | Fee potential | 10%: $6-44M · 20%: $12-88M · 35%: $22-155M · **central $33M**. Per shipper: saving $649-4,624 a year; a 20% fee is $130-925. Claims services take 20-30% on contingency (vendor) | **[our calc]**; N-R08 |
| 4 | Structure | Shippers: column X. Carriers: LTL top-50 82.9% (concentrated; they deny 50-60% of LTL claims, *assumed*); truckload 37.4%. **Who keeps the saving:** the shipper, from an adversarial payer (the carrier or its insurer) | §1.1; N-K21 |
| 5 | Software penetration and why now | About half of eligible claims are never filed. 28% of mid-market shippers use claims software, and under 8% use AI (vendor report, *assumed*). **Rules:** a written claim with set contents (49 CFR 370.3); carriers acknowledge within 30 days and dispose within 120; shippers have at least 9 months to file (*verified*). **Plumbing:** the evidence sits with the shipper (POD exceptions, photos, invoices, BOL), but filing means each carrier's portal or email; there is no claims API. **Why now:** a cargo-theft record, with losses about $725M in 2025, +60% (CargoNet, vendor); AI claims tools launched (Freehand, CorePiper, Ladingly) | N-K21, N-R09, N-F35, N-F36, N-R04, N-R07, N-R08 |
| 6 | Addressable work | Shipping and receiving clerks (43-5071): 230,110 in manufacturing, 124,950 in wholesale; logisticians as claims coordinators. Assembling proof in a fixed legal format is text work, and passes R23 | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | Logistics or finance. Contingency fees come from recoveries. The claims at stake show within days, but the cash arrives 30-120 days later, by rule. **Live in weeks** where receiving already records exceptions; harder where dock habits must change | N-F35; **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 open:** no claim counts. Theft, one part, rose in both downturns; damage claims probably follow shipments. **Test 1** pass. **Test 2:** shippers clear; carriers raised | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **12 named:** claims software (Freehand, iNymbus, TranSolutions MyEZClaim, FreightClaims.com, CorePiper, Ladingly, Claimable, VTM TRANSWARE); modules in Descartes 3G, CargoWise and Loop; managed services at Cass and nVision. **Service firms:** Recoupex, TLI, Sheer, GEODIS; brokers file for their shippers. **No dominance.** Doing nothing is the biggest substitute. Charges: contingency 20-30% (vendor); per claim (iNymbus, about $0.40-0.70); licence | N-R07, N-F51, N-F56, N-R08 |
| 10 | Fee unit and K11 series | Claims filed or recovered. No series exists | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry. Ruled out: the LTL carrier side (K10) | `2_knockouts.md` §4.2, §4.5 |

**Provisional desk score:**
- **Axis A 75:** A1 0.5, A2 1, A3 1, A4 0.5, A5 0.5, A6 1.
- **Axis W 55:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.5.
- **A5 = 0.5 [our call]:** claims recur, but on a small share of loads, not on every one.

#### C-11 · LTL class, reweigh and reclass disputes

> **Sentence:** "Rating and classing LTL shipments and disputing reweighs, reclasses and extra-service charges, for small manufacturers and distributors, handled today by LTL carriers and LTL-focused brokers and 3PLs."
> **Status after S3a:** S3b. Open: K4 (no neutral correction rate), K5 and K11 (leans fail: LTL real revenue -25.7% in 2008-09, a dollar proxy). The LTL carrier side is ruled out (K10).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Small pallet shippers: 235,684 firms in fabricated metals (49,484), machinery (19,028), durable wholesale (153,128) and furniture (14,044), mostly small and mid-sized. LTL carriers: 7,675 firms (side ruled out) | *verified*: N-D04, N-D01 |
| 2 | Savings pool | **$105-920M a year.** LTL receipts $65.7B (Census 2022) × 20-40% from small shippers × 2-5% avoidable reweigh, reclass and extra-service overcharges (vendors say 10-20%) × 40-70% removable | base *verified* (N-N13); shares **[our call]** |
| 3 | Fee potential | 10%: $10-92M · 20%: $21-184M · 35%: $37-322M · **central $62M**. Per shipper: saving $446-3,904 a year; a 20% fee is $89-781. Audit firms recover 3-8% of LTL spend (vendor) | **[our calc]**; N-A26 |
| 4 | Structure | Shippers: fabricated metals top-50 20.9%, machinery 35.8%, durable wholesale 30.7%, furniture 38.4%. LTL carriers: top-50 82.9%, top-4 40.8%, with 17.5% of receipts in firms under 500 staff, so ruled out (K10). **Five forces:** concentrated carriers hold the tariff and the measurement records (buyer power sits with carriers). The shipper keeps the saving only if a dispute succeeds | §1.1; R43 |
| 5 | Software penetration and why now | No survey of how small shippers book LTL or dispute corrections. Cheap tools exist (Freightview from $149 a month; MyCarrier), and LTL 3PL networks are large (WWEX Group claims 121,000+ customers). **Plumbing:** NMFTA's API standards (eBOL 2.1, pickup, visibility, and since 2025 a Preliminary Freight Charges API for reclass notices); adoption not found. Class data needs a ClassIT+ licence; the carrier holds the measurement proof. **Why now:** NMFC Docket 2025-1 (2025-07-19: a 13-tier density scale; 2,000+ commodities consolidated) and Docket 2026-1 (effective 2026-05-23) (*verified*). NMFTA itself says they cause "billing surprises that hit weeks after pickup". Carriers' yearly rate increases of 4.9-5.9% | N-R22, N-R12, N-R26, N-R02, N-G20, N-R03, N-R16 |
| 6 | Addressable work | Shipping clerks (43-5071): 230,110 in manufacturing and 124,950 in wholesale; logisticians; AP clerks for disputes. Density is arithmetic, the class a lookup, and disputes are letters. Measuring the pallet is the one short physical step. Passes R23 | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | The shipping or logistics lead's outbound freight budget. **Value on day one:** check past LTL invoices against their BOLs, and class correctly before pickup. **Live in weeks**; the ClassIT+ licence and each carrier's rules add setup | **[our call]** on check R's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 open, leaning fail:** no industry count of LTL shipments. LTL real revenue fell 25.7% in 2008-09 (dollars); tonnage -14.6% (all trucking). **Test 1** pass. **Test 2:** shippers clear, except furniture makers (firm count -23.6%) | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **About 7 named:** MyCarrier, Freightview, FreightPOP, FreightCenter, Freightquote (C.H. Robinson), NMFTA ClassIT+, SMC3. **No standalone dispute tool found.** Service firms: LTL 3PLs and brokers (WWEX, Freightquote, FreightCenter); audit firms. **No dominance among tools;** NMFTA controls the class data (a dependency). Today: accept the correction, or ask the 3PL rep to dispute it | N-R22, N-R03, N-R12, N-A26 |
| 10 | Fee unit and K11 series | LTL shipments, or corrections disputed. No industry count | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry (fabricated metals, machinery, durable wholesale, furniture). Ruled out: the LTL carrier side (K10) | `2_knockouts.md` §4.2, §4.5 |

**Provisional desk score:**
- **Axis A 92.5:** A1 1, A2 1, A3 1, A4 0.5, A5 1, A6 1.
- **Axis W 62.5:** W1 0.5, W2 0, W3 0.5, W4 1, W5 1, W6 0.5.

#### C-14 · Planning and consolidating shipments

> **Sentence:** "Planning how to ship (choosing the mode, pooling LTL into multi-stop truckloads, moving long lanes to rail intermodal), for mid-sized shippers, handled today by managed-transportation 3PLs on gainshare, intermodal marketing companies, or in-house spreadsheets."
> **Status after S3a:** S3b. Open: K11 (13-20% on tonnage).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 95,579 mid-sized shippers | *verified*: N-E17 |
| 2 | Savings pool | **$0.61-5.4B a year.** Mid-sized shippers' truckload and LTL spend ($68-135B) × 3-8% from mode choice and consolidation (the managed-transportation gainshare precedent) × 30-50% removable | base *assumed* (N-K22); shares **[our call]**; R33 |
| 3 | Fee potential | 10%: $61-540M · 20%: $122M-1.08B · 35%: $214M-1.89B · **central $363M**. Per shipper: saving $6.4k-56.5k a year; a 20% fee is $1.3k-11.3k | **[our calc]** |
| 4 | Structure | Shippers: column X. Carriers: truckload 37.4%; intermodal marketing companies. **Who keeps the saving:** the shipper, but only after operations change, and measured against a baseline both sides must agree. "Agreeing a baseline is the main reason gain sharing arrangements are not used" (*assumed*) | §1.1; N-A30 |
| 5 | Software penetration and why now | The same weak TMS figures as C-01. 62% of shippers outsource domestic transportation (3PL study, *assumed*). Smaller shippers lack the staff to run a TMS (analyst). **Plumbing:** ERP orders, rates for several modes, EDI 204; the optimisation engines sit inside TMSs. **Why now:** the rate rise (+28.1%), LTL rate increases, and Walmart's Prepaid Consolidation Program (May 2026). None forces the change | N-R10, N-E23, N-D31, N-R16, N-E28 |
| 6 | Addressable work | Transportation managers (11-3071): 29,990 in manufacturing and 34,350 in wholesale; logisticians as analysts. The analysis is number work, but the saving needs operational change (order cut-offs, delivery windows), which is not office work | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | The transportation manager or VP of operations; 3PL fees from the freight budget. A what-if run shows value on paper within days, but the real saving needs operational change. **Months** to go live: an ERP-like integration (R28) | **[our call]**; R28 |
| 8 | Cyclicality and growth | **K11 Test 3 open:** tonnage in the 13-20% band. **Test 1** pass. **Test 2:** shippers clear | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **17 TMS vendors** in Gartner's 2025 assessment: MercuryGate (Körber), Trimble/Transporeon, Descartes 3G, Oracle, Blue Yonder, e2open. **A warning:** Trimble paid $200M for Kuebix, a mid-market shipper TMS, then shut it down (*assumed*). **Service firms:** managed-transportation 3PLs on gainshare; intermodal marketing companies (18.5M intermodal units in 2025); brokers. **No dominance.** Today: spreadsheets, a 3PL, or shipping each order as it comes | N-D32, N-R11, N-R10, R33, N-F14 |
| 10 | Fee unit and K11 series | Shipments planned, or savings against a baseline. Proxy: ATA truck tonnage | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry. The intermodal cell is merged in (M-6) | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 75:** A1 1, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 42.5:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.

#### C-17 · Controlling inbound freight from suppliers

> **Sentence:** "Controlling inbound freight from many suppliers (routing guides, collect or prepaid terms, supplier pick-ups), for mid-sized distributors and manufacturers, handled today by the suppliers' chosen carriers and the buyer's purchasing staff."
> **Status after S3a:** S3b. K5 passes (narrowly on the census base). Open: K4 (the overpayment rate is vendor-only) and K11 (13-20% on tonnage).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 95,579 mid-sized distributors and manufacturers, as receivers. Suppliers: the same pool | *verified*: N-E17 |
| 2 | Savings pool | **$0.51-5.3B a year.** Truckload plus LTL spend of $451B × 40% inbound × 50-65% uncontrolled × 15-30% for mid-sized firms × 15-30% overpaid when suppliers choose (vendor) × 25-50% removable. On census trucking receipts, the low end is $0.27-0.33B, still above the $250M pass line | inbound and overpay shares vendor (*assumed*, N-K28, N-E31); others **[our call]**; N-N13 |
| 3 | Fee potential | 10%: $51-530M · 20%: $102M-1.06B · 35%: $178M-1.86B · **central $329M**. Per buyer: saving $5.3k-55k a year; a 20% fee is $1.1k-11k | **[our calc]** |
| 4 | Structure | Buyers and suppliers: both column X. **Who keeps the saving:** the buyer, but it is split between a lower product price and a new freight bill, so it is hard to attribute. Some suppliers earn a margin on freight (*assumed*) | §1.1 |
| 5 | Software penetration and why now | "Only about 35% of companies use a formal routing guide for inbound freight" (vendor, unsourced, *assumed*). No neutral figure after three attempts. **Plumbing:** POs and freight terms sit in the ERP; on prepaid loads the freight cost is hidden in the supplier's price; suppliers book by portal, email or 3PL. **Why now:** the rate rise lifts the freight built into supplier prices; tariffs put landed cost under scrutiny (Cass: about $600M of tariffs in its 2025 volumes); Walmart's collect and prepaid consolidation programs. None forces a mid-sized buyer | N-E31, N-K28, N-D31, N-C15, N-E27, N-E28 |
| 6 | Addressable work | Buyers and purchasing agents (13-1020): 112,200 in manufacturing and 70,490 in wholesale; purchasing managers: 20,100 and 10,070. Wage bills $14.66B and $4.48B; freight is a small part of their work. Changing terms is a supplier negotiation, which partly fails R23 | *verified*: N-F22 extended |
| 7 | Budget holder and implementation | Purchasing owns supplier terms; inbound freight lands in the cost of goods; logistics co-owns. **No value on day one:** the baseline is hidden in supplier prices. **Months** to go live: suppliers must be onboarded and terms changed | **[our call]** on check R's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 open:** tonnage in the 13-20% band. **Test 1** pass. **Test 2:** shippers clear | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **About 6-7 named:** Freehand, FreightPOP, Freightsuite, FreightSimple, BTX Global, Kuebix/FreightWise; TMS inbound modules. **Service firms:** C.H. Robinson's managed-transportation arm runs routing guides for clients; TLI sells vendor routing-guide compliance; managed-transportation 3PLs. The large-retailer model: Walmart's collect pickups. **No dominance.** Today: suppliers ship as they choose, or a PDF routing guide nobody enforces | N-R25, R33, N-E27 |
| 10 | Fee unit and K11 series | Inbound shipments controlled, or freight savings against a baseline. Proxy: ATA truck tonnage | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by shipper industry. Nothing ruled out | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 75:** A1 1, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 42.5:** W1 0.5, W2 0, W3 0.5, W4 1, W5 0.5, W6 0.

### 2.3 Facility, fleet, retail-compliance and trade jobs (research: check S)

**Two groups** (check S §3):
- **Paperwork and compliance jobs: C-19, C-20.** Office work drives the cost, dated retailer or government rules force action, and outside help is already paid per recovery or per entry.
- **Facility, fleet and port jobs: C-04, C-15, C-22.** The saving lands in physical time (dock waiting, miles, terminal waiting), and no forcing event was found. Two triggers went away in 2025, when CARB repealed its fleet and drayage rules.
- **C-18 sits in between:** pure office work, but no trigger, and only vendor evidence of the pain.

#### C-04 · Dock appointments, for warehouses and distribution centres

> **Sentence:** "Booking dock appointments for inbound and outbound trucks, for warehouses, distribution centres and grocery distributors, handled today by phone, email, spreadsheets and appointment portals."
> **Status after S3a:** S3b. Open: K5 and K11 (no count of dock visits; tonnage is the closest proxy).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 54,831 receiving sites: 19,979 warehouse sites and 34,852 grocery-distributor sites. As firms: 7,469 warehouse firms (6,789 general, 680 refrigerated) and 27,458 grocery wholesalers. Booking side: 531,374 carriers and 25,081 brokers | *verified*: N-E17, N-D04, N-F02, N-F03 |
| 2 | Savings pool | **$84-439M a year.** Carriers' direct detention cost, $3.6B, × 25-47% paid by facilities (ATRI: fees paid on "fewer than 50 percent" of invoices) × 9.3-25.8% less waiting (a university study of port gates, used by analogy) | N-C24 (ATRI, association-flagged); N-N02; the 25% low end **[our call]** |
| 3 | Fee potential | 10%: $8-44M · 20%: $17-88M · 35%: $29-154M · **central $38M**. Per site: saving $1.5k-8.0k a year; a 20% fee is $306-1,601. Vendors charge per facility, $99 a month to about $7,000 a year (vendor) | **[our calc]**; N-F38 |
| 4 | Structure | General warehousing: top-50 49.1%, top-4 24.2%, 8.9% of receipts in firms under 20 staff. Refrigerated: 73.9%. Grocery wholesale: 53.5%. **Who keeps the saving:** the facility keeps only the part of detention it would have paid (at most about 47%); carriers bear most of the waiting but do not buy the tool (payer ≠ saver, in part) | §1.1; N-C24 |
| 5 | Software penetration and why now | No neutral survey. The largest network, Opendock (Loadsmart), claims 4,000+ warehouses, about 7% of sites **[our calc; vendor numerator]**. Drivers were detained at 39.3% of stops. **Plumbing:** passes. A standalone calendar needs no integration, and Opendock is API-first, with a server for AI agents (Jun 2026, vendor). **Why now:** no rule. FMCSA's detention work is a research study, and whether its report appeared was not checked (search budget ran out). AI booking agents have arrived (DHL Supply Chain with HappyRobot, Nov 2025) | N-S07, N-S08, N-C24, N-S17, N-S34 |
| 6 | Addressable work | Shipping and receiving clerks in warehousing: 89,090 at $47,820. Planning clerks (43-5061): 390,160. Dock schedulers post at $18-26 an hour. Booking is office work, but the cost it removes, waiting, is physical, and falls only if the site honours its slots | *verified*: N-S01; N-N02 |
| 7 | Budget holder and implementation | The DC or warehouse operations manager, from the site's operations budget. At a 3PL warehouse the cost can be passed to the client. **Live in days to weeks:** the site's own doors, hours and rules are enough; a WMS link can come later. **Day one:** fewer phone calls; a fall in detention takes weeks to show | **[our call]** on check S's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 open:** no count of dock visits. Tonnage -14.6% (the closest proxy); warehouse real output -2.4% (2008-09). **Test 1** pass. **Test 2:** warehousing and grocery clear; carriers raised | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **At least 11:** Opendock, C3 Reservations, DataDocks, GoRamp, LoadingCalendar, Velostics, Conduit, Transporeon, Descartes MacroPoint, Dashdoc, Arrivy. WMS and yard-system modules. AI agents on the carrier side (HappyRobot, Qued). The leader reaches about 7% of sites; **no dominance.** Today: phone, email, shared calendars, first come first served | N-F38, N-F47, N-S41, N-S34 |
| 10 | Fee unit and K11 series | Truck visits (appointments). Proxy: ATA tonnage; warehouse output as a secondary proxy | `3a_unknowns.md` §4.1 |
| 11 | Segments | K2 ✓. Likely segments: grocery DCs, public 3PL warehouses, cold storage, manufacturers' docks. Nothing ruled out | `2_knockouts.md` §2 |

**Provisional desk score:**
- **Axis A 65:** A1 0.5, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 57.5:** W1 0.5, W2 0, W3 1, W4 0.5, W5 0.5, W6 0.5.

#### C-15 · Routing own delivery fleets

> **Sentence:** "Planning daily routes and loads for their own delivery trucks, for food, beverage, industrial and drug distributors (and processors that run their own fleets), handled today by in-house dispatchers with spreadsheets or routing tools."
> **Status after S3a:** S3b, a clean pass on every knock-out.

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Private fleets: 170,221 private-only interstate fleets, 86.4% with 10 or fewer trucks; 807,829 counting fleets that stay inside one state. Distributors: 27,458 grocery wholesalers; 3,615 beer, wine and spirits wholesalers (1,393 beer). Drug wholesalers and meat processors are ruled out (K10), and hardware and plumbing distributors (K11) | *verified*: N-F02, N-D04; `2_knockouts.md` §4.2-4.3 |
| 2 | Savings pool | **$1.6-8.1B a year.** Private fleet cost, $541.4B, × 15-30% for the card's distributors × 2-5% saved by routing. Cross-check: 170,221 fleets × $10-30k each = $1.7-5.1B | base *assumed* (N-K22); shares **[our call]** |
| 3 | Fee potential | 10%: $160-810M · 20%: $320M-1.62B · 35%: $560M-2.84B · **central $720M**, the largest of the 18. Per private fleet: saving $9.4k-47.6k a year; a 20% fee is $1.9k-9.5k | **[our calc]** |
| 4 | Structure | Grocery wholesale: top-50 53.5%, top-4 15.1%. Beer, wine and spirits: 63.4%, 25.4%. In-house fleets have no census row. **Who keeps the saving:** the distributor, which both pays and saves | §1.1 |
| 5 | Software penetration and why now | No neutral routing-adoption figure. NPTC's 2025 survey (104 mostly large fleets, members only) reports only safety technology. **Beer:** VIP's route-accounting system serves "1,000 distributors" (2019) against 1,393 beer-wholesaler firms (2022), and a snippet claims "more than 50 percent of the beer volume". **Plumbing:** passes with integration (orders and addresses from the ERP or route accounting; telematics APIs). **Why now: nothing forces it.** The driver shortage fell to #12 in ATRI's 2025 list, and CARB voted on 25 Sep 2025 to repeal its fleet rules | N-S03, N-S28, N-S29, N-D04, R38, N-S19 |
| 6 | Addressable work | Dispatchers (43-5032): 4,550 in nondurable wholesale and 7,120 in durable wholesale. The saving lands in driver time: 174,610 heavy truck drivers and 91,800 driver-sales workers in nondurable wholesale. Planning is number-heavy work, but the saving is physical, and in beverage the route driver is the customer relationship (partly fails R23) | *verified*: N-S01; N-S02 |
| 7 | Budget holder and implementation | The VP of operations or fleet manager, from the fleet operating budget. A trial on last month's orders works from a CSV export (a "lightweight cost savings assessment", R28). **Weeks** for a standalone planner; **months** where route accounting and driver handhelds must change | **[our call]**; R28 |
| 8 | Cyclicality and growth | **K11 pass (S2):** real wholesale sales for grocery -6.0% and -1.8%; beer and wine -4.0% and -10.2%; drugs rose. The hardware segment fails (-26.8%). **Test 1** pass. **Test 2:** grocery and beer distributors clear | `2_knockouts.md` §4.3; `3a_unknowns.md` §4.5 |
| 9 | Competitors and substitutes | **20+ named** (from Gartner's routing guides): Descartes, Roadnet (Omnitracs), Trimble TMW, Paragon, WorkWave, ORTEC, Oracle, SAP, Manhattan, Blue Yonder, MercuryGate, FarEye, Onfleet, nuVizz, DispatchTrack, Locus; SMB tools OptimoRoute and Routific; VIP BizStride for beverages. Telematics add-ons. **Service substitute:** dedicated contract carriage, $32.0B. **Dominance:** none for the card. **VIP is a candidate in the beer segment** for route accounting (routing not proven); S5 would check it | N-S31, N-S30, R33 |
| 10 | Fee unit and K11 series | Deliveries by distributors' own fleets. Proxy: the distributor groups' real wholesale sales | `2_knockouts.md` §4.3 |
| 11 | Segments | **K2 = S:** split by distributor type (grocery, foodservice, beverage, industrial). Ruled out: drug wholesalers and meat processors (K10); hardware and plumbing (K11). **Flag:** the beer segment (VIP) | `2_knockouts.md` §4.5; check S §3 |

**Provisional desk score:**
- **Axis A 75:** A1 1, A2 0.5, A3 0.5, A4 0.5, A5 1, A6 1.
- **Axis W 47.5:** W1 0.5, W2 0, W3 0.5, W4 0.5, W5 0.5, W6 0.5.

#### C-18 · Warehouse storage and handling bills

> **Sentence:** "Billing storage, handling and extra warehouse services, for e-commerce sellers and distributors that store goods with others, handled today by small public and contract warehouses on spreadsheets and warehouse-system modules."
> **Status after S3a:** S3b. Scope: warehouses under 500 staff (reading 1 in `3a_unknowns.md`). Open: K4 (billing leakage is vendor-only) and K5.

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 7,469 warehouse firms: 6,789 general and 680 refrigerated. 53% of general-warehouse firms have under 20 staff. Customers: 53,556 e-commerce firms, plus distributors | *verified*: N-D04, N-F01, N-E17 |
| 2 | Savings pool | **$110-900M a year.** Receipts of warehouses under 500 staff, $22.5B, × 1-5% billing leakage (vendors claim 3-15%) × 50-80% removable. Firms under 20 staff only: $28-225M, a firm-size floor question for segment selection (F-6) | base *verified*; shares **[our call]** |
| 3 | Fee potential | 10%: $11-90M · 20%: $22-180M · 35%: $38-315M · **central $63M**. Per warehouse firm: saving $14.7k-120k a year; a 20% fee is $2.9k-24k | **[our calc]** |
| 4 | Structure | General warehousing: top-50 49.1%, top-4 24.2%, with 35.6% of receipts in firms under 500 staff. Refrigerated: top-50 73.9%. **Who keeps the saving:** the warehouse (recovered revenue). Its customer's interest runs the other way | §1.1 |
| 5 | Software penetration and why now | Vendor evidence only (Extensiv): "82% of 3PL warehouses lose revenue to uncaptured" charges, and uncaptured charges are the top billing challenge. 63% of mostly larger firms use a WMS. Small public warehouses may bill from spreadsheets (not measured). **Plumbing:** WMS events plus rate sheets (often PDFs), then QuickBooks. **Why now:** none found; labour-cost pressure (vendor survey) | N-S14 to N-S16, N-S37 |
| 6 | Addressable work | Billing clerks in warehousing: 1,160; bookkeeping clerks: 4,130; receiving clerks, who record the billable events: 89,090. In small warehouses billing is a part-time task for the owner or office manager. Office work, with the lowest relationship rating in check S (2.73 of 5) | *verified*: N-S01; N-S02 |
| 7 | Budget holder and implementation | The owner, general manager or controller. Recovered charges add straight to revenue, so the payer is the saver. A look-back audit of 3-12 months of events against contracts shows value fast. **Weeks** where a WMS export exists; where there is none, event capture must be built first | **[our call]** on check S's evidence |
| 8 | Cyclicality and growth | **K11 pass (S2):** warehousing real output -2.4% (2008-09) and rose in 2022-25. **Test 1** pass. **Test 2:** warehousing clear. E-commerce customers are raised (1.6× in 2023) but replenishing | `2_knockouts.md` §4.3; `3a_unknowns.md` §4.5 |
| 9 | Competitors and substitutes | **At least 9:** 3PL WMSs with billing modules (Extensiv, Deposco, Logiwa, Camelot, Magaya, Datex) and leakage specialists (Sequoia, Xorosoft, Packem). Extensiv claims 1,500+ 3PLs, at most about 20% of US warehouse firms **[our calc]**. **No dominance.** Today: WMS reports or paper logs into spreadsheets, then invoices in QuickBooks | N-S15, N-K27 |
| 10 | Fee unit and K11 series | Billable warehouse events, or invoices. Proxy: warehousing real output | `2_knockouts.md` §4.3 |
| 11 | Segments | K2 ✓. Likely segments: small public warehouses without a WMS; cold storage; e-commerce fulfilment 3PLs. The under-20-staff cut is F-6, for segment selection | `3a_unknowns.md` §3 |

**Provisional desk score:**
- **Axis A 72.5:** A1 1, A2 1, A3 0.5, A4 0.5, A5 1, A6 0.5.
- **Axis W 47.5:** W1 0.5, W2 0, W3 0.5, W4 0.5, W5 0.5, W6 0.5.

#### C-19 · Retailer OTIF fines and deductions

> **Sentence:** "Meeting retailers' on-time-in-full rules and disputing the fines and deductions, for small and mid-sized suppliers to big-box retailers, handled today by their carriers and brokers plus in-house deductions staff."
> **Status after S3a:** S3b. K4 settled pass (CRF survey). Open: K5.

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Small and mid-sized suppliers to big-box retailers. **No firm count is held** (a gap). Manufacturers under 500 staff hold 23.7% of manufacturing receipts. Carriers and brokers supply the delivery proof | *verified*: N-D04 |
| 2 | Savings pool | **$56-480M a year.** Small and mid-sized suppliers' sales to big-box stores ($112-240B) × non-trade deductions of ¼-½% of sales (CRF survey median, association-flagged) × 20-40% removable | N-N29; sales base from Census with **[our call]** shares |
| 3 | Fee potential | 10%: $6-48M · 20%: $11-96M · 35%: $20-168M · **central $33M**. Per buyer: not computable without a count. Recovery firms work for about 30% of recoveries, or a flat $5,000 a month (vendors) | **[our calc]**; N-S35 |
| 4 | Structure | Suppliers: manufacturing top-50 29.0%. The retailers are highly concentrated (warehouse clubs and supercenters: top-4 95.6%), so buyer power sits with them: they set the rules and deduct first. **Who keeps the saving:** the supplier, from a powerful customer | §1.1; N-D01 |
| 5 | Software penetration and why now | CRF 2018: **70% of suppliers with sales of $500M or less used no third-party deduction technology**, and none outsourced any deduction task; 6% "just write off" late items (*verified*, association-flagged; dated). **Plumbing:** retailer portals through credentials and bots (no open APIs); EDI 812, 820 and 856; ERP receivables; carriers' POD portals. **Why now:** retailer rules with dates. Walmart from 1 Feb 2024 (quarterly billing, 90% on time, 95% in full, fines of 3% of the cost of goods); Target Q3 2024; Home Depot's monthly disputes (2024). SPS Commerce bought SupplyPike for about $206M (Aug 2024), with its revenue expected to rise from about $8M to $25M | N-N29, N-S13, N-S12, N-S10 |
| 6 | Addressable work | Bill and account collectors (43-3011): 158,830; credit analysts: 64,390; logisticians, for prevention. Matching deduction codes to orders, ASNs and PODs is office work (credit analysts: computers 4.45, physical 1.25) | *verified*: N-S01; N-S02 |
| 7 | Budget holder and implementation | The CFO, controller or credit manager (receivables). Recoveries return to revenue, so the payer is the saver. **Day one:** open deductions still inside the dispute window can be disputed at once; vendors lead with a free audit. **Weeks** per retailer | **[our call]** on check S's evidence |
| 8 | Cyclicality and growth | **K11 pass (S2):** real sales at big-box formats -4.7% (2008-09) and -7.0% (2022-25). **Test 1** pass. **Test 2:** manufacturing clear | `2_knockouts.md` §4.3; `3a_unknowns.md` §4.5 |
| 9 | Competitors and substitutes | **At least 7:** SPS Commerce Revenue Recovery (SupplyPike), iNymbus, HighRadius, Vendormint, RetailPath, DOSS, ClearChain. SPS's share is unknown; it is **the one to watch**, because it already carries many suppliers' EDI. **Service firms:** contingency recovery firms (Vendormint at 30%, STAT Recovery, Woodridge, Smyyth); consultancies. ERP deduction modules. **No dominance shown** | N-F55, N-S35, N-S36, N-S11 |
| 10 | Fee unit and K11 series | Deductions disputed or recovered (or shipments to retailers). Proxy: big-box real sales | `2_knockouts.md` §4.3 |
| 11 | Segments | **K2 = S:** split by shipper industry. Likely segments: by retailer (Walmart, Target, Home Depot and Amazon suppliers) or by supplier industry. Nothing ruled out | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 82.5:** A1 0.5, A2 1, A3 1, A4 0.5, A5 1, A6 1.
- **Axis W 62.5:** W1 0.5, W2 0, W3 0.5, W4 1, W5 1, W6 0.5.
- **Two caveats:**
  - W4 = 1 rests on CRF's 2018 adoption figure; S5 should test whether SPS and others have since filled the gap.
- *Update 2026-09-22 (not a re-score):* the incumbents now named are **SupplyPike (SPS Commerce Revenue Recovery)**, with ~500-550 paying suppliers at ~$33-38k each, and **Glimpse**, with 200+ brands, $52M raised and a $35M a16z Series A (Mar 2026). Their possible weak spots (price rises, paying for denied disputes, coverage gaps, small suppliers priced out) are in `4_5_profitability.md` §3.7 and are tested at S5 as H19-11.
  - A3 would be 0.5 if a "forcing event" had to be a new tightening, since Walmart eased its on-time target in 2024.

#### C-20 · Import entries, for small importers

> **Sentence:** "Preparing and filing import entries (classifying goods, calculating duty, filing the security filing), for small importers, handled today by small customs brokerages' entry writers."
> **Status after S3a:** S3b. Open: K5, and K11 (DHS trade entries -17.8% in 2008-09; the fiscal years are inferred).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | Importers: 240,535, of which 92,517 have 1-19 staff and 97.3% are small or mid-sized. Customs brokers: 15,226 active licensed brokers; **2,365 permitted brokers** (brokerage firms) in 2022. NCBFAA has 1,500+ member companies | *verified*: N-E18, N-F08; N-S26 (association) |
| 2 | Savings pool | **$104-694M a year.** FY2025's 34.7M formal entries × 25-40% from small and mid-sized importers × $40-100 of preparation cost per entry (the $100 is the World Bank's documentary-compliance cost) × 30-50% removable | N-H22, N-N06; low cost and shares **[our call]** |
| 3 | Fee potential | 10%: $10-69M · 20%: $21-139M · 35%: $36-243M · **central $54M**. Per importer: saving $432-2,885 a year. Per permitted brokerage: saving $44k-293k; a 20% fee is $8.8k-58.7k **[our calc]**. Brokers charge importers $100-250 an entry (vendor guides) | **[our calc]** |
| 4 | Structure | Brokers and forwarders: top-50 34.3%, 24.1% of receipts in firms under 20 staff. Importers are fragmented (no census row). **Who keeps the saving:** the broker, in time per entry, unless competition passes it on to importers | §1.1 |
| 5 | Software penetration and why now | Filing is fully electronic through ACE's ABI link (CBP counts 23.1M electronic formal entries a year at 5 minutes each). The manual work is classification, valuation and keying from invoices. Brokers: 25% name manual workflows as their top inhibitor to growth, and 55% plan to prioritise AI (vendor survey with NCBFAA). **Plumbing:** the strongest of the 18 cards. ABI is standard (certification needed to file); the tariff schedule has an open API (*verified*). **Why now, dated:** de minimis ended 29 Aug 2025 (informal entries rose from 5.2M to 15.4M, and 63.2M so far in FY2026); the Supreme Court ruled the IEEPA tariffs unlawful on 20 Feb 2026; CBP's refund process opened 20 Apr 2026 (about $165B on 53M+ entries, law-firm figures, *assumed*) | N-N05, N-F10, N-S20, N-S33, N-J29, N-H22, N-S05, N-S06 |
| 6 | Addressable work | Brokers sit within compliance officers in NAICS 4885 (4,520); entry writers within cargo and freight agents (53,390). The most office-heavy role in the 18 cards (customs brokers: computers 4.47, "importance of being exact" 4.85, physical 1.44) | *verified*: N-S01; N-S02 |
| 7 | Budget holder and implementation | The brokerage owner (operations or IT), where filing software is already charged by use; importers pay per entry. **A classification and extraction co-pilot** works on invoice PDFs with no integration, and shows value on day one. **Filing itself** needs the broker's ABI software API or CBP certification (months). Only licensed brokers or self-filing importers may file | **[our call]** on check S's evidence |
| 8 | Cyclicality and growth | **K11 Test 3 open:** DHS "processed trade entries" -17.8% (FY2007-FY2009); formal entries -7.1% (FY2022-FY2023). **Test 1** pass. **Test 2:** brokers clear | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **About 70 ABI vendors,** among them CargoWise, Descartes (NetCHB and others), Magaya, E2open, CustomsCity, KlearNow. AI classification tools: TariffLens, Gaia Dynamics, Cervo. NetCHB served 700+ brokers in 2022, about 30% of permitted brokers **[our calc]**. **No dominance;** WiseTech and Descartes are the consolidators to watch. Doing nothing is not an option: an entry is required by law | N-F10, N-S09, N-S38, N-S43 |
| 10 | Fee unit and K11 series | Entries. Series: CBP entry counts (FY2021 on) and DHS trade entries (2008-09) | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by importer size, industry or port. Likely segments: small importers through small brokerages; new e-commerce importers after de minimis; refund claims as a time-limited niche. Nothing ruled out | `2_knockouts.md` §4.5 |

**Provisional desk score:**
- **Axis A 92.5:** A1 1, A2 1, A3 1, A4 0.5, A5 1, A6 1.
- **Axis W 65:** W1 1, W2 0, W3 0.5, W4 0.5, W5 1, W6 0.5.
- **The wedge moves W3 and W6** (a solution choice for S6):
  - a co-pilot for brokers: W3 1 and W6 1, so W = 87.5;
  - a full filer: W3 0.5 and W6 0, so W = 52.5.
- **W1 = 1:** NCBFAA's 1,500+ member companies against 2,365 permitted brokers. NCBFAA's membership also includes forwarders.

#### C-22 · Port drayage dispatch

> **Sentence:** "Dispatching container pick-ups and returns (terminal appointments, chassis, empty returns), for importers' and exporters' containers, handled today by small port drayage carriers by phone, terminal portals and spreadsheets."
> **Status after S3a:** S3b (reading 2: its unit is imports plus exports). Open: K4 (no current turn time at source), K5 (central $27M, closest to the reserve line) and K11 (-14.6%).

| # | Item | Fact sheet | Label / source |
|---|---|---|---|
| 1 | Buyers per side | 48,991 interstate carriers tick "intermodal containers". Local general-freight firms: 43,571, of which 34,331 have under 5 staff. The LA/Long Beach registry holds 23,000+ trucks. Importers and exporters | *verified*: N-F02, N-D04; N-F21 |
| 2 | Savings pool | **$69-274M a year.** 36.6M truck transactions at the terminals (2022 loaded TEU, from Army Corps data via BTS) × 0.5 hour of excess time × $75-100 a truck hour × 5-15% removable. Newer snippets suggest shorter turn times; at a 0.25-hour excess the central fee pool would be $19M | N-N01 (*verified*); time and shares **[our call]**; N-N04 (*assumed*) |
| 3 | Fee potential | 10%: $7-27M · 20%: $14-55M · 35%: $24-96M · **central $27M**. Per carrier: saving $1.4k-5.6k a year; a 20% fee is $282-1,119 | **[our calc]** |
| 4 | Structure | Local general freight: top-50 10.5%, top-4 2.3%, with 51.7% of receipts in firms under 20 staff. **Who keeps the saving:** the drayage carrier, but most of the waiting sits on the terminal's side, so the terminals hold the power | §1.1; N-N02 |
| 5 | Software penetration and why now | Harbor Trucking Association and TradeLanes, 2021: "80%" of members say carriers are still not using technology for demurrage and detention problems (association and vendor). **Plumbing:** passes with heavy integration: eModal and terminal portals, chassis pools, delivery orders by email, container-tracking APIs. **Why now: no positive trigger.** CARB repealed its drayage zero-emission rule (vote 25 Sep 2025), and the FMC's 2024 billing rule moves demurrage and detention bills away from truckers | N-S24, N-S39, N-S19, N-F32 |
| 6 | Addressable work | Dispatchers in trucking: 34,890 (drayage cannot be separated out). The work is phone-heavy coordination, but the cost is truck time at terminals, largely outside the dispatcher's control | *verified*: N-S01; N-N02 |
| 7 | Budget holder and implementation | The drayage owner or operations manager, on a thin budget. **Weeks per port** where integrations exist; longer to build them | **[our call]** |
| 8 | Cyclicality and growth | **K11 Test 3 open:** loaded import plus export TEU -14.6% (2007-09). Import-only drayage fell 21.9%, a failing segment. **Test 1** pass. **Test 2:** carriers raised (4841 at 2.1× the economy's death rate) | `3a_unknowns.md` §4.1, §4.5 |
| 9 | Competitors and substitutes | **At least 7:** CargoWise Landside (WiseTech bought Envase in 2023 for $230M; 1,300+ customers of all types); PortPro ($12M Series A); TMSEZ; general trucking TMSs; Terminal49, Vizion, BlueCargo. **No dominance;** WiseTech is the consolidator to watch. Service firms: drayage brokers, intermodal marketing companies | N-S21, N-S22, N-S23, N-F54 |
| 10 | Fee unit and K11 series | Container moves (imports plus exports). Series: MARAD loaded TEU | `3a_unknowns.md` §4.1 |
| 11 | Segments | **K2 = S:** split by importer size, industry or port. Likely segments: by port complex (LA/LB, NY/NJ, Savannah, Houston). Ruled out: import-only drayage (K11) | `3a_unknowns.md` §4.1 |

**Provisional desk score:**
- **Axis A 65:** A1 0.5, A2 0.5, A3 0.5, A4 1, A5 1, A6 0.5.
- **Axis W 47.5:** W1 0.5, W2 0, W3 0.5, W4 0.5, W5 0.5, W6 0.5 (leans 0).
