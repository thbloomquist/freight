# Check AX · Field map, slice 2: what a shipment *should* cost, and what a dispute must contain

*Reviewed 2026-10-10: `research/s5_check_AX_adversarial.md` (ledger 22 kept verified, 8 narrowed, 1 discarded: the "L7 Not Used" line is in Estes' 210 guide, not ArcBest's). The corrections are applied in `data/doc-explanation.md`; this file is kept as written. Main ones: FedEx Freight and TForce rank pricing by the BOL's terms, not the payor; some tariffs date the whole issue, not each item; YRC and South Bay print no bond of indemnity.*

Written 2026-10-10 for the C-09 prototype's field map (one of three slices). Scope: the documents that set the price (pricing agreements, rules tariffs, fuel tables, base-tariff references, TL rate confirmations) and the documents a dispute produces (claim forms, the law, carriers' answers). Everything here comes from files in `data/` (cited by `file_id`) or from one regulation fetched at the source (eCFR). Nothing is decided. Plain-English terms: **cwt** = 100 lb; **AMC** = absolute minimum charge (the floor a bill can't go under after discount); **FMCS** = SEFL's "floor minimum charge per shipment"; **FAK** = "freight all kinds", one class used for a range of classes; **accessorial** = an extra-service charge; **payor** = whoever pays the bill; **PRO** = the carrier's bill number; **W&I** = weight and inspection; **TONU** = truck ordered not used; **GRI** = general rate increase; **210** = the EDI invoice.

## 1. Method

- **Read in full or by item (34 files):** the SEFL–Exist agreement, all three versions and the two exception pages (02-002 pp. 12-22, page images viewed for pp. 18, 21, 22); SEFL bills pp. 33, 46, 49-51 (02-002); two ABF bills (01-001 pp. 23-24); rules tariffs of SEFL (13-065), ABF (13-046, CCS item in 13-047/048), ODFL (13-053), Estes (13-049), XPO (13-063, claim item in 13-064), R+L (13-058), Saia (13-056, 13-054), FedEx Freight (13-051), TForce (13-060), and the claim items of AAA Cooper (13-066), Central (13-073), Dayton (13-072), Werner (13-068), USA Truck (13-071). About 110 items read.
- **Fuel (6 files):** EIA weekly diesel (14-074, converted to CSV, 1,686 weeks 1994-03-21 to 2026-09-14), Estes 2023 capture (14-076, table parsed from the page script), FedEx LTL and FTL, GSA, DOE Atlas (14-071 to 14-075).
- **Contracts (6):** YRC–First Brands (11-037), Kroger–Medallion (11-041), CJ Logistics (11-039), Home Depot (23-005, Schedule A and A-1), Walmart (23-012, pp. 74-96 OCR'd with tesseract because the text layer is only the claim form). GM (11-038) has no usable text layer and was not read.
- **TL (10):** rate confirmations 10-035, 10-036, 10-037, 10-038, 10-039, 10-042, 10-043; packets 22-012 (Taylor), 22-013 (Werner); Werner and USA Truck tariffs.
- **EDI (5):** L7 tariff segments in 19-012, 19-013, 19-015, 19-031; element definitions in 12-046 (XPO 210 guide) and 12-040 (ArcBest).
- **Dispute outputs (17):** claim forms 16-082 to 16-084, 16-092 to 16-095; government 20-001, 20-003, 20-005; real claims and answers 23-003, 23-006, 23-010, 23-011; law 08-024 (statute text as quoted by the court), 08-028; **49 CFR Part 378 fetched from the eCFR versioner API, version 2026-09-01** (`https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-49.xml?part=378`, default client, no identity sent).
- Arithmetic re-done in `python3 -I` with half-up rounding to the cent. Individuals' names on the pages were not transcribed.

## 2. What each price document specifies

### 2.1 Pricing agreement (LTL)

| Term | Where it sits | Firms seen | Example value (file_id, page) | Effective-date logic | Checks |
|---|---|---|---|---|---|
| Base tariff named | Rating-item column "BASE RATES" | SEFL; Home Depot; Walmart | `SEFL-0550 CURRENT` (2021) → `SEFL-0550 01/10/22` (2022, 2023) (02-002 pp. 12, 15, 18); "Home Depot customized Czarlite ... effective 8/29/05" (23-005 Sch. A); "Walmart 20/20 Tariff of Rates based on a class 50" (23-012 p. 89) | "CURRENT" floats with the carrier's increases; a dated base is frozen | B2 |
| Discount by lane | Row: route × direction × terms | SEFL | WCPC outbound 90.90 (2021) → 88.15 (2022, 2023); MWPC outbound 92.50 → 90.30; NEPC outbound 92.10 → 87.45 (pp. 13, 16, 19) | Version by ship date | B1, B2 |
| FAK | Columns CLASS / FAK RANGE + note | SEFL; Home Depot | "Apply FAK exception class 70.0 on commodities described in NMFC class 077.5 thru 175.0. All other commodities apply actual class." (p. 19); Home Depot tiers FAK 55/70/100/250 (23-005 Sch. A) | Version | B4 |
| Floor minimum | FMCS column, or "Item 610" | SEFL | Direct FMCS $88.50 (2021), $97.00 (2022, 2023); Item 610 OR/AZ/CA… $128.00 → $143.50 → $152.00; MWPC $107.25 → $120.25 → $127.50 (pp. 14, 17, 20) | Version | B3 |
| Per-pallet rates | Table under direct rows; p. 21 sheet | SEFL | AL 1 pallet $143.25 (p. 18) vs $151.75 (p. 21); p. 21 flags "SUBJECT TO GENERAL RATE INCREASE: YES", "FUEL INCLUDED IN RATE: NO" | p. 21 is undated; its rates run 5.9-6.1% above p. 18 on six cells **[our calc]**, consistent with a GRI applied | B2, B3 |
| Accessorial exceptions | Separate page | SEFL; First Brands; Walmart | Liftgate $55 direct↔partner, $30 direct↔direct; limited access $50/$25; inside $25; notification $0/$7.50; reconsignment $30; redelivery $80 (p. 22, eff. 4/7/2021, "SUBJECT TO GENERAL RATE INCREASE: NO"); First Brands liftgate $20 flat, re-weighing and corrected BOL waived (11-037 Sch. B) | Own date column | D1 |
| Contract fuel table | Schedule | First Brands; Walmart; Home Depot | 15.30% at $3.660-3.709 (11-037 p. 27); Walmart "Appendix C" (not attached, 23-012 p. 77); Home Depot amendment "Amend Fuel Table" eff. 10/27/2022 (23-005) | Amendment date | B8, B9 |
| Lane price rows | Schedule | Home Depot | Point-to-state rows with minimum and discount columns, eff. 10.27.2022; one row reads $150.00 and 55.00 (23-005 Sch. A-1; column split *assumed*) | Amendment date | B2, B3 |

### 2.2 Rules tariff (LTL): the rules that move money

| Term | Item | Carriers seen | Example value (file_id, item) | Effective-date logic | Checks |
|---|---|---|---|---|---|
| AMC | ABF 615; ODFL 180; TForce 610-A; FedEx 404; Saia 650 | 5 | ABF: greater of discounted linehaul, discounted minimum, or account AMC (13-046); ODFL $169-255 by miles (13-053); TForce $186 (13-060); FedEx $243 Economy (13-051) | Item date | B3 |
| Cubic / density minimum | SEFL 610-100; ODFL 610-1; XPO 233; FedEx 613; TForce 575-A | 5 | SEFL: ≥750 ft³ and <6 pcf → cube × 6 lb at class 150, customer's discount (eff. April 19, 2022); ODFL and XPO: class 125, 350-750 ft³ at <3 pcf or ≥750 ft³ at <6 pcf | SEFL item predates the 2023 bills | B3 |
| Reweigh / reclass fee and threshold | SEFL 996; ABF 992; ODFL 367; XPO 239; R+L 992 and inspection item; FedEx 981; Saia 850; TForce 365; Estes 993, 993-10 | 9 | SEFL $15 any change; ABF $50 if charges move ≥$10; ODFL $25 if weight +20 lb or reclass; XPO $50.70 at +25 lb; R+L corrects only if BOL ≥50 lb light, $40 if +$10; FedEx $40 at +50 lb or −200 lb; Saia $39; TForce $40 if net +$15; Estes $20 | SEFL 996 dated Dec 1st, 2025: 2023 fee unknown | C1, C2 |
| Corrected BOL fee and window | SEFL 360-5; ABF 362; ODFL 365; XPO 205; Estes 360-03 | 5 | $35 / $50 / $45 / $52.70 / $20; ABF payor change "within a period of 30 days from date of the initial bill of lading"; XPO changes "within thirty days (30) days after the shipment has been accepted" | Item date | A5, C1 |
| Fuel base | SEFL 110; ABF 161; Estes 530; TForce 1; FedEx 570 | 5 | ABF: linehaul incl. minimums and AMC, "will not apply to charges for special services"; Estes and TForce: all charges "other than accessorial"; **FedEx: "linehaul transportation, and other services which consume fuel"** | Item date | B9 |
| Fuel week rule | ABF 161; Estes 530; Saia 1005; FedEx 570 | 4 | Wednesday on the prior Monday's EIA (ABF); Tuesday's announcement, effective Wednesday (Estes, Saia) | — | B8 |
| Payment term | SEFL 817; ABF 427; ODFL 434; XPO 207; Estes 720; TForce 721 | 6 | 15 days from presentation (SEFL, ABF, ODFL, XPO, TForce); 30 days (Estes) | — | F1 |
| Late fee / discount forfeiture | SEFL 817 §4; ABF 427; ODFL 564; Estes 720; XPO 207; R+L failure-to-pay item; Saia (Sec. C); TForce 721 | 8 | SEFL 25% and ABF 30% on collection; ODFL 35% if unpaid 42 days after due date; Estes 10% ($21 min), then "full undiscounted, class rates"; XPO 10% ($50 min) per 30 days, discounts revoked on collection; R+L "Forfeiture of all discounts" plus 125%; Saia discounts revoked "automatically" after 15 days net / 30 courtesy; TForce 1.5% a month | — | F1 |
| Payor's pricing applies | SEFL 201; ODFL 764; XPO 4; Estes 760; Saia 105 | 5 | "the applicable pricing published specifically for the account of the payor of the freight charges will apply" (SEFL 201 §1) | — | A3, A5, B1 |
| Rounding | ODFL 565; Estes 530; First Brands fuel clause | 3 | under half a cent dropped, half a cent or more rounds up | — | A1 |
| Guaranteed service | SEFL 752; XPO 200 | 2 | SEFL $50, all charges waived if late; XPO 25% of net linehaul, min $70.25, refund "within 15 days of delivery" | — | E1 |
| Claim window | see §6 | 13 | — | — | G1, G2 |

**Accessorial prices** (rate per cwt / minimum / maximum, or flat; current issues; the item number in brackets):

| Carrier (file) | Residential | Liftgate | Limited access | Notification | Redelivery | Detention with power |
|---|---|---|---|---|---|---|
| SEFL (13-065) | $7.60 / $94 / $575 [753] | $7.25 / $89 / $225 [890-100] | $94 flat [754] | $25 [647] | $9.00 / $105 / $550 [830] | $23 per 15 min after 20-60 min free by shipments per stop [500] |
| ABF (13-046) | $14 / $190 / $685 [751] | $12 / $225 / $625 [758] | $14 / $190 / $685 [440] | $68 incl. appointment [485-1] | $17 / $145 / $700 [830] | $75 per 15 min, $90 min [500] |
| ODFL (13-053) | $7.20 / $125 / $580 [753-1] | $4.40 / $115 / $330 [891] | $7.20 / $125 / $580 [753-4] | $30 [647] | $7.20 / $175 / $580 [830] | $3 a minute, $50 min, 20-60 min free [502] |
| Estes (13-049) | $8.50 / $75 / $550 [751] | $4.95 / $75 / $350 [567] | $85 [751-10] | $30; $25 residential [647] | $10.00 / $85 / $900 [830] | [500], not read |
| XPO (13-063) | $16.90 / $191 / $932 [224] | $14.20 / $274 / $682 [218] | in [224], not read | $27.90 [221] | $19.60 / $186 / $586 [229] | $76.50 per 15 min, $101.25 min, 15-60 min free by weight [211] |
| R+L (13-058) | $15 / $225 / $1,530 [753-2] | $16 / $225 / $820 [520] | $15 / $225 / $1,530 | $100 | $4.60 / $62 plus original charges [830] | not read |
| Saia (13-056) | $11.54 / $166 / $694.50 [753] | $11.54 / $156.50 / $364 [575] | $173.50 [1000] | $64 [647-1] | $14.95 / $153.50 / $752 [830] | not read |
| FedEx (13-051) | $243 flat [750-2] | $13.96 / $207 / $681 [890] | not read | $65 [750-3] | $21.05 / $210 / $2,203 [830] | not read |
| TForce (13-060) | $15 / $207 / $800, first of two columns [753] | $13 / $200 / $615 [892-A] | $195 flat [755-A] | $65 [647] | $18 / $160 / $1,000 [830-A] | not read |

**Version drift is real.** ABF's California Compliance Surcharge was billed at **$22.00** on 2024 bills (01-001 pp. 23-24), reads **$27.00** in 111-AS (13-046) and **$34.00** in both 111-AU issues (13-047, 13-048). A rule engine loaded with today's tariff would wrongly flag every 2024 bill.

### 2.3 Fuel surcharge tables and the index (set 14)

| Term | Where | Seen | Example (file_id) | Effective-date logic | Checks |
|---|---|---|---|---|---|
| Index | EIA weekly U.S. on-highway diesel | all | Mon 2023-05-08 $3.922; 05-15 $3.897; 2024-07-29 $3.768 (14-074) | Monday price | B8 |
| LTL % table | Carrier table | ABF, FedEx, TForce, R+L, Estes 2023, GSA, DOE Atlas | ABF $3.76-3.77 → 31.70% (13-046 Item 161); Estes 2023: 30 rows, $3.490-4.090, e.g. $3.910-3.930 → 32.00% (14-076) | Effective Wednesday (ABF, Estes, Saia, FedEx LTL, GSA: "shipment pickup date is controlling" 14-072) | B8 |
| TL per-mile table | Carrier table | Werner; FedEx FTL; DOE Atlas | Werner $3.40-3.449 → $0.47/mile (13-068 Item 310) | Werner: loads dispatched Mon-Sun on Monday's price; FedEx FTL: set Monday, effective Tuesday (14-075) | B8, B7 |
| Contract table | Agreement | First Brands | 15.30% at $3.660-3.709 against ABF's tariff 30.70-31.10% at $3.66-3.71 (11-037; 13-046) | Contract version | B8 |

The Estes capture holds only the 30 rows embedded in the page script; the "current" level and the history were loaded from an API and are not in the file. No other 2023-24 carrier table is held.

### 2.4 Base-tariff references (no base tariff is held)

| How it is named | Where | Example (file_id) | What it lets us check |
|---|---|---|---|
| Agreement column | SEFL rating item | `SEFL-0550 01/10/22`; Canada `SEFL-0551 CURRENT` (02-002 pp. 15-19) | Which table and which edition, not the rate |
| Rules-tariff governing list | SEFL 1090 Item 100; XPO Item 1; ODFL Items 100, 400 | SEFL550, SEFL551, fuel SEFL195, mileage HGB100 (13-065); XPO base CNWY 599, fuel CNWY 190 (13-063); ODFL class tariffs 505/506/550/559, fuel ODFL 128 (13-053) | Same |
| PDF bill | ABF | "Tariff: AOD000", "RATE DETERMINED BY RATEWARE", "AU=ABF646-468646" (01-001 pp. 23-24) | The authority number points to the account's agreement |
| PDF bill | SEFL | Printed rate "60080" = $600.80/cwt (02-002 p. 33) | Arithmetic only |
| EDI 210 L7 segment | L702 agency, L703 tariff, L707 class, L710 effective date (12-046) | AAA Cooper `L7*1*CZAR*910****060***20120917*0562` (19-013); `L7*1*SMC*ZRH****060***20110919*0361` (19-012); YRC `L7*1*RDWY*4516****50` (19-031); Estes `L7*2*OVL*DCN****70***20131120` (19-015). ArcBest's 210 marks L7 "Not Used" (12-040) | Table, edition date, class |

What cannot be checked without the base tariff: the gross rate itself (is $600.80/cwt right for Miami → Sisters OR, class 70, 509 lb?), the published minimum before discount (ABF's "MIN 702.71"), deficit-weight alternation (which weight break is cheaper), and cubic minimums at class 125/150 rates. Everything downstream of the printed rate can be checked.

### 2.5 TL rate confirmations and TL tariffs

| Term | Where | Seen | Example (file_id, page) | Logic | Checks |
|---|---|---|---|---|---|
| Linehaul | Rate con line | CHR, TQL, BDS, Taylor | "Line Haul - FLAT RATE 1 $4,800.00" (10-036 p. 3); "$1,200.00 Line Haul Flat" (10-037 p. 14); BDS "LINEHAUL 44,000 1.00 FLT 2,800.00" (22-013 p. 4) | Per load | B6 |
| Fuel | Rate con | CHR; BDS; Taylor; Coyote | CHR: "$688.08 fuel surcharge within the listed transportation rate" (10-036); BDS: rate "includes all stop-off charges, fuel surcharges" (22-013); Taylor: "FUEL SURCHARGE $/MILE 332 Miles .47" (22-012 p. 4); Coyote: quoted rate "includes any and all fuel surcharges" unless agreed in writing (10-038) | Per load | B8, B7 |
| Detention | Rate con or agreement | Coyote, TQL, Werner, USA Truck, Transport Systems | Coyote 2 h free, $25/h, cap $150 per location, proof of arrival/departure on BOL (10-038 p. 11); TQL 3 h after appointment, 4 h FCFS, $25 dry / $30 reefer (10-037); Werner 2 h free from the later of arrival or appointment, $110/h (13-068 Item 320); USA Truck $75/h after 90 min, $650/day max (13-071 Item 41); $50/h after 2 h in a carrier-drafted broker agreement (10-039 p. 15) | — | D3 |
| Layover | same | TQL, Werner, USA Truck | TQL max $250 dry / $300 reefer; Werner $350 solo / $500 team; USA Truck $650 per 24 h | — | D6 |
| TONU | same | TQL, Werner, SEFL, Transport Systems | TQL $150, "eligibility begins 2 hours after rate confirmation is accepted"; Werner $250; SEFL 985 TL $143.25/day or $2.75/mile, min $432; "WILL CHARGE FULL LOAD AMOUNT IF LOAD IS CANCELLED" (10-039 p. 15) | — | D5 |
| Lumper | same | CHR, TQL, Werner, BDS | "a lumper receipt is provided" (10-036); "Valid lumper receipts are required" (10-037); Werner "face value of lumper receipt or a minimum load/unload charge of $150" | — | D7 |
| Stop-offs | same | USA Truck; BDS | $75 / $100 / $150 (13-071 Item 52); included in BDS rate (22-013) | — | D4 |

## 3. Precedence: which document wins

1. **Signed agreement over rules tariff, for what it covers.** SEFL exceptions page: "UNLESS OTHERWISE STATED IN CONTRACT OR TARIFF, ACCESSORIAL CHARGES WILL BE ASSESSED ACCORDING TO THE PROVISIONS OF THE SEFL 1090 RULES TARIFF SUBJECT TO THE EXCEPTIONS BELOW" (02-002 p. 22); every version: "all shipments are subject to SEFL 1090 Rules Tariff" (pp. 14, 17, 20). ODFL Item 766 §2: a rule in a schedule governed by the tariff "will apply in lieu of the rule in this Tariff" (13-053). TForce: "Exceptions to any of the Items in this publication will be noted in agreements" (13-060 cover). First Brands: "Items not specifically addressed in this Agreement will be governed by Carrier's Rules Tariff" (11-037).
2. **Some shippers exclude the tariff entirely.** Kroger: "The terms and conditions of any tariff of the Carrier shall not govern unless specifically included herein", and conflicts go "(1) this Agreement; (2) purchase order documents; (3) Shipper's receipts; (4) bill of lading; or (5) any other shipping documents" (11-041 §26). Walmart: tariffs "are not applicable ... except to the extent, they are expressly incorporated" (23-012 p. 77). Where the BOL incorporates the tariff, it binds the shipper (*Mafcote v. Estes*, 08-028: "The tariff controls").
3. **Agreement version by ship date.** SEFL issues dated 01/15/2021, 06/08/2022, 04/12/2023 (02-002). Bill 806625953 shipped 2023-04-19, **seven days** after the 2023 version: its MWPC floor is $127.50, not 2022's $120.25 **[our calc]**. Watch the base edition too: "CURRENT" (2021) floats; "01/10/22" is frozen.
4. **Tariff item by effective date at shipment.** ABF Item 160 §3: "All transportation charges ... will be assessed on the basis of provisions legally in effect at the time of shipment"; Item 382: "When two or more revisions of an item cover the same time period the version with the latest issue date supersedes" (13-046). XPO Item 10 §3 says the same (13-063). ABF 111-AS applies "on shipments tendered on or after September 9, 2024", so **no ABF tariff held governs the May-Aug 2024 bills in set 01**. SEFL prints a date per item: 753 "Effective: December 16, 2022" and 610-100 "April 19, 2022" cover the 2023 bills; 996, 830, 890-100, 647 and 754 are dated 2024-26 and do not.
5. **Payor's pricing.** The agreement that applies is the payor's (SEFL 201, ODFL 764, XPO 4, Estes 760 §3, Saia 105). SEFL 201 Note B: when a logistics company pays, "the pricing published specifically for the logistics company ... will apply". So the payor field selects the agreement before any price check.
6. **Within an agreement.** Home Depot: "Point to point rates will take precedence over all other rates"; zip-to-zip next; then point-to-state, state-to-state; same type, "the lower rate will apply" (23-005 Sch. A). SEFL p. 21: pallet rates "BASED ON THE LOWEST TO HIGHEST LANE PRECEDENT". Estes 760 §4: negotiated commodity or per-unit pricing "will not alternate with" class rates.
7. **Quote vs agreement.** Estimates are "not binding either on ABF Freight or the shipper" (ABF 160 §2; XPO 10 §2). Spot quotes are their own price: ABF's CCS "will not apply to shipments moving under a LTL Volume Spot Quote" (Item 162). SEFL treats "A request to add and apply a spot quote number to a freight bill that was not provided on the original bill of lading" as a corrected BOL at $35 (360-5 §6): the quote number must be on the BOL.
8. **TL: rate confirmation, under the master agreement.** CJ Logistics: "in the event of a conflict ... between the Rate Confirmation Sheet ... and this Agreement ... the terms of this Agreement shall supersede and prevail"; accessorials "shall only be valid when specifically agreed to in a signed writing" (11-039). BDS: "This Rate Confirmation Sheet is a legally binding agreement" and "will only pay Carrier on rate confirmation" (22-013).
9. **Origin vs delivering carrier (interline).** Saia 105 §2-3: accessorials requested on the BOL take the origin carrier's price; those requested after the original invoice take the delivering carrier's (13-056).

## 4. The expected-charge formula

**LTL, line by line** (r() = round half up to the cent; every step names its source):
1. **Pick the price set (B1, A5).** Payor from the BOL terms box → that payor's agreement → the version with the latest effective date on or before the ship date → the row for route (direct / partner zone), direction, terms.
2. **Rated class (B4).** If the BOL's NMFC class is inside the FAK range → FAK class; otherwise actual class. *Needs the BOL.*
3. **Gross (A1; B2 needs base rates).** gross = Σ r(weight_i/100 × rate_i) [+ deficit weight × rate at the next break, e.g. "AS WEIGHT 1000 / DEFICIT 90", 02-002 p. 35]. Without base rates only the arithmetic is checked.
4. **Discount (B2).** disc = r(gross × d%); net = gross − disc.
5. **Minimums (B3).** net′ = max(net, discounted published minimum, AMC or FMCS or Item 610 floor). ABF shows the lift as its own line "MCADJ". If cube ≥ 750 ft³ and density < 6 pcf, also test the cubic minimum (SEFL 610-100: cube × 6 lb at class 150 with the customer's discount). *Needs the cube.*
6. **Pallet rates (SEFL direct lanes).** Per pallet by state and pallet count, no discount; not for mixed pallets and loose pieces, pallets over 48", or 20,000 lb and more (02-002 p. 18).
7. **Fuel (B8, B9).** fuel = r(f% × net′), where f% = the payor's table (contract first, else tariff) at the index for the carrier's week rule, and the base excludes accessorials, except FedEx (§2.2).
8. **Accessorials (D1).** price = agreement exception if present, else r(clamp(weight/100 × rate, min, max)) or the flat fee, from the item in force on the ship date. **Whether it applies at all is §5's trigger (D2).**
9. **Corrections (C1, C2).** New weight or class only with the carrier's certificate; add the fee only if the item's threshold is met.
10. **Total and balance due (A1, A4).** total = net′ + fuel + Σ accessorials + surcharges; balance due = new total − the total already billed for the same PRO.

**TL:** total = linehaul (flat, or rate/mile × miles) + fuel (% of linehaul or $/mile × miles, or "included") + detention max(0, hours − free) × rate, capped + stop-offs + layover + TONU + lumper at receipt face value. Each term comes from the rate confirmation, then the master agreement, then the carrier's tariff only if referenced.

**Worked example 1, SEFL bill 807148067** (02-002 pp. 33, 46; ship Mon 2023-05-15; Miami Gardens FL → Sisters OR, a WCPC lane):

| Line | Rule applied | Expected | Billed | Source |
|---|---|---|---|---|
| Version | latest ≤ 2023-05-15 | 04/12/2023 | — | pp. 18-20 |
| Class | NMFC 49880 apparel; FAK 70 on 77.5-175 (BOL class not in file) | 70 | 70 | p. 19 |
| Gross | r(5.09 × 600.80) | 3,058.07 | 3,058.07 | rate not checkable |
| Discount | r(3,058.07 × 0.8815) | 2,695.69 | 2,695.69 | p. 19 WCPC outbound |
| Net vs floor | 362.38 > $152.00 Item 610 (OR) | 362.38 | 362.38 | p. 20 |
| Liftgate | exception "DIRECT to PARTNERSHIP ... $55 MIN CHARGE" beats 890-100 ($89 today) | 55.00 | 55.00 | p. 22 |
| Residential | no exception → 1090 Item 753: r(5.09 × 7.60) = 38.68 → $94 minimum; item effective 2022-12-16, so in force | 94.00 *if triggered* | 94.00 | 13-065 |
| Fuel | 22.00% × 362.38; base excludes accessorials | 79.72 | 79.72 | level not checkable |
| Total | | 591.10 | 591.10 | |

Every price reconciles. The one open question is the residential **trigger**. Missing from the public set: the BOL, the delivery receipt, quote CWEN3E465, the SEFL-0550 base rate, and SEFL's 2023 fuel table. For scale: Estes' public 2023 table gave 32.00% at the same index ($3.922, 14-076), so one carrier's table cannot stand in for another's.

**Worked example 2, ABF bill 165526559** (01-001 p. 24; ship Fri 2024-08-02; Ontario CA → Ontario CA; 199 lb):

| Line | Rule applied | Expected | Billed |
|---|---|---|---|
| Linehaul | published minimum "MIN" (base rate, not held) | — | 702.71 |
| Discount | r(702.71 × 0.895) | 628.93 | 628.93 |
| Net | 702.71 − 628.93 | 73.78 | — |
| AMC lift | Item 615: the greater of …; account AMC $180 (agreement not held) | +106.22 | MCADJ 106.22 |
| CCS | $22 on the bill; the held tariffs say $27 or $34 and postdate the shipment | ? | 22.00 |
| Fuel | 30.3% × 180.00; Item 161 counts AMC as linehaul and excludes CCS | 54.54 | 54.54 |
| Total | 180.00 + 22.00 + 54.54 | 256.54 | 256.54 |

The arithmetic and fuel base pass. The fuel **level** does not: for the week starting Wed 2024-07-31, the prior Monday index was $3.768, and 111-AS gives 31.70%; the bill says 30.3%, 1.4 points lower. That matches the practice audit's 1.3-1.5. But 111-AS postdates the bill, and accounts can have their own fuel tables (First Brands'), so this is "not checkable", not an error. Missing: the ABF agreement behind "AU=ABF646-468646" (89.5%, $180, class "EX70" on the sister bill p. 23), RateWare / AOD000 base rates, ABF 111 in force before 2024-09-09, and ABF's 2024 fuel table.

**Worked example 3, TL, Taylor** (22-012 p. 4): FLAT RATE $993.96 + fuel 332 miles × $0.47 = $156.04; total $1,150.00 = the rate confirmation's "Total Cost USD 1,150.00". The rate confirmation says 335.15 miles and the invoice 332: fuel used the invoice's miles (B7 is a question, not a finding). Werner (22-013): the invoice's LINEHAUL $2,800.00 equals the all-in rate confirmation.

## 5. Triggers vs prices

The price comes from the tariff or agreement and can be machine-checked. **Whether the service was ordered or performed is a fact from another document.** The tariff wording decides which document.

| Accessorial | Trigger wording (exact) | Fact needed, and from where |
|---|---|---|
| Residential | SEFL 753 §1: "apply only when the carrier is requested or required to make pickup or delivery at a private residence ... The term 'private residence' shall apply to the entire premises on which a dwelling for living is located." §2: shipper "should indicate"; omission "will not relieve the shipper and/or consignee" | Is there a dwelling on the delivery premises? Address type, delivery receipt, consignee. The BOL is evidence, not the trigger |
| | Definitions differ: ABF 751 includes "that portion of the premises where commercial or business activity is conducted"; Estes 751 and R+L 753-2 exclude the part "that involves the sale of merchandise or services to the walk-in public"; XPO 224: "determined by Carrier in its reasonable discretion", including "a business operating within a private residence"; FedEx 750-2: "including locations where a business is operated from a home"; TForce: "If an address can be construed as either residential or commercial, then it will be considered a Residence"; ODFL 753-1: consignment to a residential address "will be considered a request" | The same home-based shop is residential at ABF, XPO, FedEx and TForce, and may not be at Estes or R+L. Rules must be per carrier |
| Liftgate | SEFL 890-100: "required or requested"; Estes 567: request "so stated on the Bill of Lading", or the consignee notes it on the delivery receipt with a signature; FedEx 890 and XPO 218: charged even when the driver uses "alternate means"; Saia 753 §8: "Liftgate service will apply on residential pickup and delivery"; Estes 751: required if any piece is 50 lb or more at a residence | BOL tick box; delivery-receipt notation |
| Limited access | SEFL 754 list (e.g. "mini storage warehouses", "schools"), same omission sentence as 753 | Site type. The YRC decline in 23-003 turned on exactly this |
| Notification | SEFL 647 Note A: applies "whenever the original bill of lading or subsequent versions lists a requirement for a delivery appointment, a call ahead"; ODFL 647 counts even "For carrier convenience, call before arrival"; XPO 221: "requiring, asking, or encouraging" | BOL text. Combination rule: included free with residential at ABF 751, XPO 224, FedEx 750-3 §2 |
| Redelivery | "through no fault of the carrier" (SEFL 830, ODFL 830, XPO 229, FedEx 830); TForce 830-A: at a residence, not charged unless a delivery time was agreed first | First-attempt record (SEFL prints "ORIG DEL ATTEMPT: 05/25/2023", 02-002 p. 35) |
| Detention | SEFL 500: time starts on "actual notification ... of the arrival", times "entered into the carrier's driver hand-held log device"; XPO 211: arrival to departure "per driver or carrier electronic records"; Werner: from "arrival ... or the appointment ..., whichever is later" | Timestamps: delivery receipt, ELD, gate log |
| Reweigh / reclass | thresholds in §2.2; scales "NTEP-certified" (SEFL 996), ±1% (ABF 992, ODFL 367) | Carrier certificate vs BOL weight and class |
| Exclusivity rules | ABF 751: residential "will not apply on shipments when the charge in Item 440 ... is assessed"; XPO 224: "only apply a single charge per address, per shipment" | Machine-checkable: two such charges on one bill |
| Contract can flip the burden | First Brands Sch. B: "Carrier must have authorization from First Brands Group for accessorial charges incurred and is responsible for retaining documentation"; Walmart Sch. I: storage, redelivery and reconsignment need "prior written approval", detention and notification "do not apply" | Approval records, not the BOL |

## 6. Clocks the software must compute

**The shipper's dispute window has at least six start dates.** The engine should compute every one that applies and show the earliest.

| Clock | Rule (exact where it decides) | Source |
|---|---|---|
| Statute, shipper | "must contest the original bill or subsequent bill within 180 days of receipt of the bill" | 49 U.S.C. 13710(a)(3)(B), quoted in 08-024 |
| Statute, carrier rebill | "within 180 days of the receipt of the original bill" | 13710(a)(3)(A), 08-024 |
| From shipment date | ABF 428 "within 180 days of the initial shipment date", suit within 18 months; AAA Cooper 660; Werner 585; YRC form "within 180 days of pickup" | 13-046, 13-066, 13-068, 16-095 |
| From carrier's receipt of the shipment | ODFL 396 "no more than 180 days after Carrier's receipt of the shipment"; Central same | 13-053, 13-073 |
| From date of original bill | XPO 23(5); Saia 1030(6); USA Truck 17 | 13-063, 13-056, 13-071 |
| From receipt of invoice | FedEx 438 "180 days from the receipt of the original invoice plus 7 days"; TForce 813 "receipt shall mean 10 days after the shipment has been tendered"; XPO's claim page "180 days of the receipt of the original invoice and only after the invoice has been paid" | 13-051, 13-060, 16-083 |
| No tariff window | SEFL 1090 has no overcharge-claim item; Item 202 §7 sets 180 days from shipment for *allowance* discrepancies only. The statute governs | 13-065 |
| Contracts | First Brands: 180 days after the original bill date, and carrier charges not submitted within 180 days of service "are null and void"; Walmart: 12 months from "final invoice payment", additional charges barred after 12 months | 11-037 §13-14; 23-012 p. 78 |
| Rebill exemption | Saia 1030(5): "Except for the revocation of discounts ..., Carrier must issue any bill for charges in addition ... within 180 days" | 13-056 |
| Carrier's answer | 378.7 acknowledge "within 30 days"; 378.8 "pay, decline to pay, or settle ... within 60 days"; 378.3(a) a non-collecting carrier forwards within 15 days; 378.9(b) carrier-found overpayments refunded "within 30 days" | eCFR |
| Claim closure | ODFL 396: "closed 30 days after the date of the initial ruling" unless more information arrives within 30 days; $50 if settled "through no fault of Carrier" | 13-053 |
| Set-off triggers | Kroger may set off claims, including a Part 378 overcharge claim, "as to which Carrier has not paid, declined or offered a compromise of settlement within sixty (60) days" (the 60-day words may attach only to the third category); Home Depot offsets loss-and-damage claims 90 days after sending | 11-041 §2.4; 23-005 |
| Corrected BOL | ABF 30 days from the initial BOL; XPO 30 days after acceptance; Estes LOA $20 after 30 days from the bill date | 13-046, 13-063, 13-049 |
| Guarantee refund | XPO 200: "within 15 days of delivery" | 13-063 |
| Late fee / forfeiture | 15 days from presentation (SEFL, ABF, ODFL, XPO, TForce); ODFL 35% at 42 days past due; Saia revocation after 15/30 days, 25% at 61-90 and 50% over 90 days; Estes 30 days, then notice, then 10 or 20 days to pay | §2.2 |
| TL and broker | TQL detention, layover and lumper "within 5 business days"; Taylor (Pepsi): "within 48 hours of delivery", TONU "same day"; KCH: notify "within 2 hours after the appointment time"; BDS: invoices more than 45 days late; Coyote: invoice "within fifteen (15) days after delivery" | 10-037, 22-012, 10-043, 22-013, 10-038 |
| Government | 31 U.S.C. 3726: GSA has 3 years; a Notice of Overcharge is not a "contest" under 13710 | 20-005 |

Worked clock, 807148067: balance-due bill dated 2023-06-19 → statute (taking bill date as receipt) 2023-12-16; an ABF-style shipment-date rule would have given 2023-11-11 **[our calc]**. A real case of a missed carrier clock: YRC's status page shows a claim received 03/28/23 and approved with a draft dated 06/20/23, **84 days** later, past 378.8's 60 (23-006 p. 5); the claim was filed 189 days after the 09/20/2022 ship date, so YRC's own "180 days of pickup" was not enforced on a duplicate payment.

## 7. Dispute outputs

**What Part 378 requires** (eCFR 2026-09-01): a claim "shall not be paid unless filed in writing with the carrier that collected the transportation charges" (378.3(a)); it "shall include the name of the claimant, its file number, if any, and the amount of the refund sought to be recovered, if known" and "shall be accompanied by the freight bill" (378.4(a)-(b)). It may add "The rate, classification, or commodity description or weight claimed to have been applicable", "Complete tariff authority", "Freight bill payment information" and "Other documents or data" (378.4(b)(1)-(4)). Duplicate-payment claims need the paid bills and payment information (378.4(c)). Missing papers are "not ... grounds for disallowance"; the carrier must ask (378.4(d), 378.5(c)). Copies need an indemnity agreement (378.4(e)). One claim may cover many shipments with "The same tariff issue or authority or circumstances" (378.3(b)).

**Fields a claim record must carry** (the union of the forms):

| Field | ABF 16-092 | FedEx 16-082 | YRC 16-095 | R+L 16-093 | Averitt 16-094 | South Bay 16-084 | XPO web 16-083 |
|---|---|---|---|---|---|---|---|
| Claimant name, address, own claim number | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PRO and date; ship date | PRO, date | PRO | bill numbers | bill numbers | bill #, bill date | PRO, origin, destination | up to 100 PROs |
| Nature | "weight, rate, classification, discount" | ✓ | tick: rate, weight, description, classification, overpayment, payment in error, duplicate, discount application error | basis | reason | ✓ | reason |
| Authority | "tariff, item number, effective date" | ✓ | tariff authority, discount item number | ✓ | NMFC item/sub, class, tariff, item | ✓ | agreement or tariff copies |
| Paid vs should be | weight, rate, extension | pkgs, articles, weight, rate, charges | itemised per PRO, summing to the total | weight, rate, extension | weight, rate, charges, O/C | same as FedEx | — |
| Bond of indemnity | ✓ | ✓ | — | ✓ | ✓ | indemnify | — |
| Precondition | — | — | 180 days of pickup | — | — | — | invoice paid first |

**Attachments by dispute type:** weight or description → original BOL, "Vendor invoice ... when claim is based on weight", "Catalog pages", "Original packing slip" (ABF, R+L), "Weight certificate or certified statement" (FedEx, South Bay); for a consignee's claim, a "certified weight ticket" (YRC). YRC: "All Class and Weight disputed claims must be supported with the shipper's bill of lading ... Brochures and 'sample' bills of lading will not be accepted." Reclass proof is defined in the tariffs: "an invoice or packing slip along with a pre-printed specification sheet or catalog page, which lists the commodity description, weight, and shipping dimensions" (SEFL 170 Note 3; XPO 205 the same). Duplicate payment → canceled checks or drafts (YRC). Pricing → the agreement page (XPO). The real 3PL form in 23-011 carries BOL number, invoice amount paid, date paid, EFT number, PRO, overcharged amount ($276.37), reason ("PLEASE CREDIT THE REWEIGH FEE"), and attachments "SPECS SHEET" and "INVOICE".

**What a carrier's answer looks like:** 378.8 requires the reasons "in writing ..., citing tariff authority". Real examples: YRC's status page, "This claim is in APPROVED status ... A detailed report of our audit of this claim was sent to the claimant", with draft number and amount ($612.77 for a "Keying error resulted in duplicate payment", 23-006 pp. 4-5); a decline "per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse", which the 3PL appealed with a satellite image of a commercial warehouse (23-003 p. 5), the mirror of the SEFL residential case; ODFL's refund and re-bill (set 21, AT §7.5). A broker's dispute ledger (23-010) groups 100+ disputes under reasons such as TONU (14), no record of load (14), reweigh overpayment (13), reclass overpayment (11), liftgate overpayment (9), failure to apply the discount (7), charges above quote (3) **[our count]**. **Government side:** a carrier's claim to GSA must include "(a) The transportation document. (b) An explanation for the claim. (c) Any additional supporting documentation" (41 CFR 102-118.545 as amended, 20-003); SF 1113 carries the carrier's bill number, SCAC, amounts claimed and "Differences" (20-001).

## 8. Gaps: inputs no public document gives

| Missing | Blocks | Cost (doc-explanation §3) |
|---|---|---|
| Base rates: SEFL-0550, ABF RateWare / AOD000, XPO CNWY 599, ODFL 505-559, CzarLite / SMC ZRH editions, Walmart 20/20, Home Depot custom CzarLite | B2, published minimums in B3, deficit-weight alternation, cubic minimums | SMC3 CzarLite module $800 (2022 list), carrier modules $300, plus RateWare; FEMA paid $8,764 a year; multi-customer price unpublished |
| Fuel tables in force at the ship date: SEFL195, ABF 2024, ODFL 128, XPO CNWY 190, Saia; only 30 Estes rows from 2023 | B8 on every real bill | $0 via the carrier; no 2023-24 archive captures exist |
| Tariff editions in force at the ship date: SEFL 1090 is current only; ABF before 2024-09-09 (111-AR) not held | Any item dated after the ship date (ABF CCS; SEFL 996, 830, 647, 754) | $0, ask the carrier |
| Account agreements: ABF AU=ABF646-468646; SEFL 2020; Walmart lanes ("As attached hereto", nothing attached) and Appendix C fuel; Kroger rates "contained in Shipper's Trans System" | B1-B4, B8 | Interviewee documents under NDA |
| NMFC class data | Class lookups for B4 and C1 | ClassIT price unpublished; DoD paid $5,500-5,803 (2008) |
| Mileage engine: PC*MILER Version 31 (First Brands), HGB100 (SEFL) | B7, TL per-mile fuel | Licence, price not researched here |
| BOLs, delivery receipts, certificates, timestamps, approvals | Every trigger in §5 | Interviewee documents |

**Where this check differs from `data/doc-explanation.md`** (beyond the Item 753 and 180-day corrections already in hand):
1. §1.1 lists "Home Depot and Walmart contracts with lane pricing". Walmart's Appendix B is a cover page, "(As atached hereto or as otherwise mutually agreed in writing)", with no lanes attached, and Schedules E and H are empty title pages (23-012 pp. 88, 93-94). Only Home Depot has lane rows.
2. §1.4 "filed inside 180 days of the bill" is one of at least six start dates (§6). SEFL's own tariff sets no overcharge window at all.
3. §3 says the base tariff serves "checks B1, B6". It serves B2, plus the published minimum in B3. B1 (agreement version) and B6 (TL linehaul) need no base tariff.
4. §1.1 "U.S. Xpress: $50 an hour after 2 hours" comes from the carrier-drafted broker agreement (10-039 p. 15). The U.S. Xpress rate confirmation instead requires 30 minutes' notice before detention. Coyote's $25 an hour is also capped at $150 per location.
5. §1.1 says fuel is "the carrier's weekly percentage". TL fuel is often dollars per mile (Werner, Taylor, FedEx FTL), contracts carry their own tables (First Brands), and FedEx LTL applies fuel beyond linehaul. B9 "fuel on linehaul only" is therefore a per-carrier rule.
6. §1.4 leaves FedEx Freight out of the standard-form group. Its PAP201 form follows the standard "Presentation of Overcharge Claims" layout with a bond of indemnity (16-082).

## 9. Claim ledger

| # | Claim | Tag | Source |
|---|---|---|---|
| 1 | SEFL agreement versions dated 01/15/2021, 06/08/2022, 04/12/2023; base "SEFL-0550 CURRENT" in 2021, "01/10/22" after | *verified* | 02-002 pp. 12, 15, 18 (p. 18 image viewed) |
| 2 | Discount and Item 610 floor values by version, as in §2.1 | *verified* | 02-002 pp. 12-20 text layer; 2023 WCPC and MWPC rows per AT-adversarial image |
| 3 | Exceptions page header and values; redelivery and dock-pickup rows all read $80 at 400 dpi (AT read one as $60) | *verified*; the $60/$80 glyph is a scan ambiguity | 02-002 p. 22 image |
| 4 | p. 21 pallet rates 5.9-6.1% above p. 18 on six cells; flags "SUBJECT TO GENERAL RATE INCREASE: YES" | *verified* values, [our calc] ratio; GRI reading *assumed* | 02-002 pp. 18, 21 images |
| 5 | SEFL 753 wording, $7.60 / $94 / $575, "Effective: December 16, 2022" | *verified* | 13-065 Item 753 |
| 6 | SEFL has no overcharge-claim window item; 202 §7 covers allowances only | *verified* (text search of the full issue) | 13-065 |
| 7 | 807148067 and 165526559 reconcile line by line as in §4 | [our calc] on *verified* transcriptions | 02-002 pp. 33, 46; 01-001 p. 24 |
| 8 | ABF CCS $22 (2024 bills), $27 (111-AS), $34 (111-AU) | *verified* | 01-001 pp. 23-24; 13-046/047/048 Item 162 |
| 9 | ABF 111-AS applies to shipments on or after September 9, 2024 | *verified* | 13-046 introduction |
| 10 | EIA $3.768 on 2024-07-29; ABF table 31.70% at $3.76-3.77; bill 30.3% | *verified* | 14-074; 13-046 Item 161; 01-001 p. 24 |
| 11 | Estes 2023 capture holds 30 rows, $3.490-4.090; $3.910-3.930 → 32.00% | *verified* | 14-076 page script |
| 12 | Accessorial prices in the §2.2 matrix | *verified* (current issues); Estes limited-access row picked from a multi-line section, *assumed* which line is the general charge | the items cited |
| 13 | Reweigh, inspection and corrected-BOL fees and thresholds | *verified* | items cited in §2.2 |
| 14 | Late-fee and forfeiture terms | *verified*; FedEx forfeiture not found in its partial text layer | items cited |
| 15 | Claim-window wording per carrier, §6 | *verified* | 13-046, -053, -056, -060, -063, -066, -068, -071, -073, -051; 16-083, 16-095 |
| 16 | 13710(a)(3)(A)/(B) wording | *verified* as quoted by the court | 08-024 |
| 17 | Part 378 wording (378.3, 378.4, 378.5, 378.7, 378.8, 378.9) | *verified* | eCFR versioner, 2026-09-01 |
| 18 | Residential definitions differ by carrier | *verified* | 13-046, -049, -051, -053, -058, -060, -063 |
| 19 | L7 element meanings (L702, L703, L707, L710) | *verified* | 12-046 L7 segment; 19-012/013/015/031 |
| 20 | ArcBest 210 marks L7 "Not Used" | *verified* | 12-040 line 90 |
| 21 | First Brands: tariff covers only gaps; Sch. B prices; 180-day terms; 15.30% fuel | *verified* | 11-037 |
| 22 | Kroger tariff exclusion and conflict order; Walmart tariff exclusion, 12-month windows, 20/20 tariff, empty lanes appendix | *verified* | 11-041; 23-012 pp. 75-94 (tesseract OCR) |
| 23 | Home Depot custom CzarLite 8/29/05, FAK tiers, precedence, no forfeiture | *verified*; the A-1 row values *assumed* (narrow-column split) | 23-005 |
| 24 | Taylor $993.96 + 332 × $0.47 = $1,150.00; rate con 335.15 miles | *verified* + [our calc] | 22-012 p. 4 |
| 25 | TQL, Coyote, CHR, KCH, BDS terms in §2.5 | *verified* | 10-037, 10-038, 10-036, 10-043, 22-013 |
| 26 | "$50 an hour after 2 hours" sits in the carrier-drafted broker agreement (Exhibit B), not U.S. Xpress's rate confirmation | *verified* | 10-039 p. 15 |
| 27 | YRC approval 84 days after receipt; filed 189 days after ship date | *verified* dates, [our calc] | 23-006 pp. 4-5 |
| 28 | YRC limited-access decline wording and appeal | *verified* | 23-003 p. 5 |
| 29 | TQL dispute reason counts | [our count] of the text layer | 23-010 |
| 30 | GSA can take 3 years; Notice of Overcharge is not a contest under 13710 | *verified* | 20-005 |
| 31 | 2020 SEFL bills carry "PENALTY/TARIFF DUE" ($161.89 on p. 49, $107.51 on p. 51); basis not derivable without the 2020 agreement | *verified* lines; basis not answerable | 02-002 pp. 49, 51 |
