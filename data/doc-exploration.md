# Document exploration: every fact a dispute needs, where it lives, and what NOT REPORTED means

Written 2026-10-10 for the founders, on their outstanding questions about how the C-09 audit software will work. It is a proposal [our call], not a decision. It builds on `data/doc-explanation.md` (the documents one by one, and the seven-stage pipeline in its §4) and on the three field maps behind it (`research/s5_check_AV_c09_field_map_bills.md`, `..._AW_c09_field_map_shipment_facts.md`, `..._AX_c09_field_map_price_terms.md`). Where that file is organised by document, this one is organised by **fact**: for each thing the software must know, which document carries it, where to look next when it is not there, and what it means when nothing carries it. §5 tests the map on six real chains from `data/sources/`.

Freight terms used: **LTL** (less-than-truckload), **TL** (truckload), **PRO** (the carrier's bill number), **BOL** (bill of lading, the shipper's pickup paper), **DR** (delivery receipt), **cwt** (100 lb), **NMFC** (the commodity classification), **FAK** (one class applied to a range of classes), **accessorial** (an extra-service charge), **W&I** (weight and inspection), **210 / 214 / 204** (the EDI invoice, status and tender messages), **AMC** (absolute minimum charge), **TONU** (truck ordered, not used). Check codes such as A1, B2, D2 are the 33 checks in `research/s5_check_AK_c09_audit_workflow_and_products.md` §3.2.

Privacy: the raw files are public court and bankruptcy records and carry individuals' names and phone numbers. None is copied here; companies and towns only.

## 0. The founders' framing, and what this file answers

The founders' words (2026-10-10):

> There are a series of phases, documents at each phase. We will define them as:
> 
> Before Shipment - Set Price Agreement
> 
> At Pickup & Deliver - Set Facts for Shipment
> 
> After Deliver - Ask for Money for shipment
> 
> Dispute Time - What we are looking into, based off of previous documents. Audit / Question / Answer, documents specifying these types of information for any dispute that occurs.
>
> From these four stages we are going to establish a pipeline of parsing the relevant information across each document in each stage to check for inequality between the Set Price Agreement, with its facts for shipment, with the Money asked for Shipment.
> If expected price =/= actual price
> Then we have caught a DISPUTE.

Their questions, and where each is answered:

| # | Question | Section |
|---|---|---|
| 1 | What is all the information we need to know to identify DISPUTEs? | §1 |
| 2 | In which document does each piece live? | §2 |
| 3 | Do documents overlap, so a fact missing from its usual place can be found elsewhere? | §3 |
| 4 | What happens on NOT REPORTED: is a missing fact itself grounds for a dispute? | §4.1–§4.3 |
| 5 | Is anyone time-bound to re-report, and how does that touch the 180-day limit? | §4.4–§4.5 |
| — | Test it on real subsets of `data/sources/` | §5 |

The phases map onto the documents as follows (the documents themselves are described in `doc-explanation.md` §1):

| Phase | Documents | What the phase fixes |
|---|---|---|
| 1 Before shipment: set the price | pricing agreement, rules tariff, base tariff, fuel table, quote; for TL the rate confirmation or tender | the **rules**: what each line should cost, and when a charge applies |
| 2 At pickup and delivery: set the facts | BOL, delivery receipt, W&I certificate, 214 status, 204 tender, TL packet | the **facts**: what shipped, what was asked for, what was done, when |
| 3 After delivery: ask for money | freight bill (PDF or 210), corrected and balance-due bills, statement | the **claim on the money**: what the carrier says it is owed |
| 4 Dispute time | the shipper's worksheet, the overcharge claim, the carrier's answer, the credit or refund, the payment record | the **question and the answer**, with their clocks |

A DISPUTE in this file means: a bill line whose billed amount differs from the amount the phase-1 rules give for the phase-2 facts (a **price** difference), or a line whose charge applies only if a phase-2 fact is true and that fact is absent or contradicted (a **trigger** difference). The pipeline's four verdicts per line (flag / ask the reviewer / not checkable / matches) are in `doc-explanation.md` §4.7.

## 1. What we need to know: the fact inventory

Derived from the "Data needed" column of all 33 checks (AK §3.2), the expected-charge formula (AX §4) and the trigger table (AX §5). One row per fact, with a stable ID by phase. 

**Role:** 

* *price* = an input to the expected amount 

* *trigger* = decides whether a charge applies at all

* *key* = links documents to each other

* *clock* = sets a deadline

* *state* = what has been billed or paid so far.

**Need:** 

* *must* = no DISPUTE verdict on the lines it feeds without it

* *useful* = sharpens a verdict or a claim but its absence does not block one

### 1.1 Phase 1, price terms (P)

| ID | Fact | Checks | Role | Need |
|---|---|---|---|---|
| P01 | Whose pricing applies: the payor rule (payor's agreement at SEFL, ODFL, XPO, Estes, Saia, ABF, AAA Cooper; the BOL's terms at FedEx Freight and TForce) | A5, B1 | price | must |
| P02 | The agreement's identity and every version with its effective date | B1 | price | must |
| P03 | The base tariff named and its edition ("SEFL-0550 01/10/22", "CZAR 910") | B2 | price | must for B2 only |
| P04 | Discount by lane, direction and terms | B2 | price | must |
| P05 | FAK rule: the class applied and the range it covers | B4 | price | must |
| P06 | Floor minimum (AMC, FMCS, Item 610 floor) per lane, and the published minimum | B3 | price | must |
| P07 | Cubic or density minimum rule (threshold and class) | B3 | price | useful |
| P08 | Pallet, spot-quote or dynamic price, with the quote's conditions | B5 | price | must when a quote number is on the bill |
| P09 | Accessorial exception prices in the agreement, and any waiver | D1 | price | must |
| P10 | Tariff accessorial items: rate, minimum, maximum or flat, **and the trigger wording** (what "residential", "limited access", "required or requested" mean at this carrier) | D1, D2 | price + trigger | must |
| P11 | Reweigh, reclass and corrected-BOL fees with their thresholds and windows | C2, A5 | price + trigger | must |
| P12 | Fuel table in force, the index week rule, and the fuel base (which lines fuel applies to) | B8, B9 | price | must |
| P13 | The base rate itself for the lane, class and weight | B2 | price | must for B2; needs a licence |
| P14 | TL linehaul and fuel terms for the load (flat, per mile, included), and the mileage basis | B6, B7, B8 | price | must (TL) |
| P15 | TL accessorial terms: detention free time, rate, cap and the evidence rule; layover; TONU; lumper; stop-off | D3–D7 | price + trigger | must (TL) |
| P16 | The shipper's claim-window rule: the start date the carrier or contract uses | G1 | clock | must |
| P17 | The carrier's re-bill window (statute, tariff or contract) | A4 | clock | must |
| P18 | Payment terms, late-fee and discount-forfeiture rule | F1 | price + clock | useful |
| P19 | Guaranteed-service terms and the refund window | E1 | price + clock | useful |
| P20 | Combination rules (one charge per address; residential excludes limited access; notification free with residential) | D1 | price | useful |
| P21 | Rounding rule and rate unit convention | A1 | price | useful |

### 1.2 Phase 2, shipment facts (F)

| ID | Fact | Checks | Role | Need |
|---|---|---|---|---|
| F01 | BOL number (and PO, SID, shipper number) | A2, A6, A7 | key | must |
| F02 | Ship or pickup date | B1, B8, G1 | price + clock | must |
| F03 | Shipper and consignee, name and address | A6, D2 | key + trigger evidence | must |
| F04 | Freight terms box (prepaid, collect, third party) and the third-party bill-to | A5, A3 | price (picks P01) | must |
| F05 | Pieces and handling units | C1 | price | useful |
| F06 | Declared weight, with its unit (lb or kg; net or gross) | C1, B3 | price | must |
| F07 | Declared class and NMFC item | B4, C1 | price | must |
| F08 | Declared dimensions, cube, density | C1, B3 | price | useful |
| F09 | Services requested: tick boxes and special instructions (liftgate, appointment, notify, inside, residential) | D2 | trigger | must |
| F10 | Quote or rate-estimate number written on the BOL | B5, A7 | key | must when a quote is claimed |
| F11 | Guaranteed or required delivery date requested | E1, E2 | trigger | useful |
| F12 | Actual weight as the carrier measured it (the certificate) | C1 | price + trigger | must on any reweigh |
| F13 | Actual dimensions, cube and density, and the inspector's note or reclass reason | C1, B4 | price + trigger | must on any reclass |
| F14 | Delivery date and time | E1, E2, D3 | trigger + clock | must for E1, D3 |
| F15 | Services performed at delivery (DR boxes, driver notes, printed verification lines) | D2 | trigger | must |
| F16 | Who received it: signature, stamp, exceptions written on the DR | D2 (evidence) | trigger evidence | useful |
| F17 | Arrival, departure and wait times at pickup and delivery | D3 | trigger | must for D3 |
| F18 | First delivery attempt: date and reason it failed | D2 (redelivery) | trigger | must on a redelivery charge |
| F19 | Premises type: is there a dwelling on the delivery premises; is the site limited access | D2 | trigger | must on a residential or limited-access charge |
| F20 | TL load or tender number, stops, appointment windows, miles | B6, B7, D4, D3 | key + price | must (TL) |
| F21 | The shipper-side agreed TL price for this load (its own rate confirmation, tender or 204) | B6 | price | must (TL) |
| F22 | Lumper receipt; cancellation time; layover record | D5–D7 | trigger | must on those charges |

### 1.3 Phase 3, the money asked (M)

| ID | Fact | Checks | Role | Need |
|---|---|---|---|---|
| M01 | PRO number (normalised: zeros, dashes, SCAC prefix, suffix) | all | key | must |
| M02 | Carrier (SCAC or name) and the envelope sender if different | all | key | must |
| M03 | Bill type: original, corrected, balance-due, reprint | A4 | state | must |
| M04 | Bill date, and the date of the *first* bill on this PRO | G1, A4 | clock | must |
| M05 | Due date | F1 | clock | useful |
| M06 | Terms as billed and the bill-to party | A5 | price | must |
| M07 | Rated class | B4 | price | must |
| M08 | Billed weight, "as" weight and deficit weight | C1, B3 | price | must |
| M09 | Rate and its unit (cents or dollars per cwt; flat; per mile) | B2 | price | must |
| M10 | Gross (linehaul before discount) | A1 | price | must |
| M11 | Discount, % and $ | B2 | price | must |
| M12 | Minimum lift (MCADJ, "M", "MIN") | B3 | price | must |
| M13 | Fuel, % and $ | B8, B9 | price | must |
| M14 | Each accessorial line: name, code, amount | D1–D7 | price | must |
| M15 | Correction fee line (reweigh, inspection, corrected BOL) | C2 | price | must |
| M16 | Total | A1 | price | must |
| M17 | Amount previously billed, amount paid, balance due | A4, A3 | state | must on a correction |
| M18 | The carrier's printed reason or remark for a change ("PER GOOGLE EARTH …", "W & I REWEIGH …", reason codes) | C1, D2 | trigger evidence | must on a correction |
| M19 | The bill's echo of the BOL: special instructions, declared class, declared weight | D2, B4 | trigger evidence | useful (fallback for F07, F09) |
| M20 | References printed: quote number, tariff, agreement or authority number, account | A7, B1, B5 | key | must when present |
| M21 | Page counter and completeness | A1 | state | must |
| M22 | "Previously invoiced on" list or reprint flag | G1, A4 | clock | useful |
| M23 | Delivery date printed on the bill, with its qualifier (actual or estimated) | E1 | trigger | useful |
| M24 | Statement of account: open balance, aging, adjustment flag, cash posted | F1, A3 | state | useful |
| M25 | Interline partner and its share | A3, A5 | price | useful |

### 1.4 Phase 4, the dispute (D)

| ID | Fact | Checks | Role | Need |
|---|---|---|---|---|
| D01 | Every dispute-window start date that applies, and the earliest deadline | G1 | clock | must |
| D02 | The claim's content: claimant, its file number, amount, PRO and date, the nature of the error, the authority (item, agreement page), paid against should-be | G1 | state | must to file |
| D03 | Proof attached: BOL, certificate, spec sheet, agreement page, paid bill, indemnity | C1, D2 | state | must to file |
| D04 | Filing date and the carrier's acknowledgement date | G2 | clock | must |
| D05 | The carrier's decision, its reason and its date | G2 | state | must |
| D06 | Credit, refund or draft: amount and date | credit matching | state | must |
| D07 | The shipper's payment record: date paid, reference, payee (direct or via a 3PL) | A2, A3, F1 | state | must for A3, F1 |
| D08 | The shipper's own dispute log or worksheet | context | state | useful |

Count: 21 + 22 + 25 + 8 = 76 facts. Every "Data needed" entry of the 33 checks maps to at least one row (ticked against AK §3.2 while writing; F2 "GL rules" and F4 "sales-order freight line" are out of the dispute scope and sit under D07's accounting export).

## 2. Where each fact lives: the lookup map

One row per fact. **Primary** is where the software looks first; **fallback** is where it looks next, in order; **never** is a document that carries something that looks like the fact but must not be used for it; **if none** says who could supply it, which is what the NOT REPORTED line will name. Positions are given as a page region or an X12 segment-element ("210 B3-06" = segment B3, element 6). Sources: AV §2 and §7 (bill side), AW §2 and §7 (shipment facts), AX §2–§3 (price terms), `doc-explanation.md` §4.2–§4.4. Everything here is observed on files in `data/` unless marked *assumed*.

### 2.1 Phase 1, price terms

| ID | Fact | Primary | Fallback | Never | If none |
|---|---|---|---|---|---|
| P01 | Whose pricing applies | The carrier's rules tariff item (SEFL 201, ODFL 764, XPO 4, Estes 760, Saia 105: the payor's; FedEx Freight and TForce: the BOL's terms) | The agreement's own scope clause | The bill-to printed on the bill (it is the result, not the rule) | Carrier; a per-carrier profile in the software |
| P02 | Agreement identity and versions | The agreement's header: issue date, account number, "rating item" number (SEFL: pp. 12, 15, 18 of set 02) | The bill's authority reference (ABF "AU=ABF646-468646"; SEFL "TARIFF SEFL 6009") names which agreement to ask for | A reprint's date | **Customer** (its own agreement) |
| P03 | Base tariff name and edition | Agreement "BASE RATES" column ("SEFL-0550 01/10/22") | 210 L7 (`L7*1*CZAR*910…20120917`, AAA Cooper); the bill's tariff line (ABF "Tariff: AOD000"); the rules tariff's governing list (SEFL Item 100) | — | Customer or carrier; for the rates themselves, a licence (§2.1 P13) |
| P04 | Discount by lane | Agreement rating rows (route × direction × terms) | The bill's printed % (SEFL "88.15% DISC", ABF "DISC 89.5%", TForce "84.00% DISCOUNT"); 210 L5 text (AAA Cooper, Estes); derived DSC ÷ gross (ODFL 210, XPO PDF) | — | Customer. Without the agreement the printed % is "as billed", not "as agreed" |
| P05 | FAK rule | Agreement FAK columns and note | The bill's rated class beside its declared class ("CL125 NMFC 49880" rated "CLASS 70.0") shows a FAK was applied, not what it should be | — | Customer |
| P06 | Floor minimum | Agreement FMCS / Item 610 column | Tariff AMC item (ABF 615, ODFL 180, FedEx 404, TForce 610-A, Saia 650); the bill's "MIN", "MCADJ", "M" shows a minimum was applied | — | Customer, then carrier tariff |
| P07 | Cubic minimum rule | Rules tariff item (SEFL 610-100, ODFL 610-1, XPO 233, FedEx 613, TForce 575-A) | The bill when applied (SEFL p. 94 "T 1090C 610-100 … CF 5.76 PCF") | — | Carrier tariff (public) |
| P08 | Quote / spot / pallet price | The quote document | Agreement pallet page (SEFL p. 21); the bill's quote number plus the carrier's own difference note (ABF "The invoice amount differs from the quoted amount …") | A quote for another shipment | **Customer** (portal history); no public quote exists |
| P09 | Accessorial exception prices | Agreement exceptions page (SEFL p. 22, dated 4/7/2021; First Brands Sch. B) | Contract schedule | The tariff price when an exception exists | Customer |
| P10 | Tariff accessorial items, price and trigger wording | Rules tariff, the item and edition in force on the ship date (SEFL 753 "Effective: December 16, 2022") | A later edition, marked *assumed* for that date | A different carrier's item | Carrier (public; old editions on request or Wayback) |
| P11 | Reweigh, reclass, corrected-BOL fees and thresholds | Rules tariff (SEFL 996, 360-5; ABF 992, 362; ODFL 367, 365; XPO 239, 205; Estes 992/993, 360-03; FedEx 980/981; TForce 365; R+L 992, 364; Saia 850) | Agreement waiver (First Brands waives reweigh and corrected-BOL fees) | — | Carrier (public) |
| P12 | Fuel table, week rule, base | Contract table if any (First Brands p. 27; Walmart App. C) | Carrier's table in force that week (set 14: current tables; Estes 2023 capture only) + EIA index; the fuel-base item (ABF 161, Estes 530, SEFL 110, FedEx 570) | Another carrier's table; today's table for an old bill | Carrier (no 2023-24 archive captures exist) |
| P13 | Base rate | SMC3 CzarLite / carrier module (licensed) | None: the bill's printed rate is taken as given and only the arithmetic is checked | — | Licence (`doc-explanation.md` §3) |
| P14 | TL linehaul, fuel, miles basis | The shipper's own rate confirmation or tender (204 L3) for the load | Master agreement; the carrier's tariff (Werner 310) only if referenced | A broker-to-carrier rate con (prices the broker's leg) | Customer |
| P15 | TL accessorial terms and evidence rule | Rate confirmation (TQL, Coyote, KCH, BDS, Taylor pages) | Master agreement (CJ Logistics); carrier tariff (Werner 320, USA Truck 41) | — | Customer |
| P16 | Shipper's claim-window rule | Statute 13710(a)(3)(B) plus the carrier's item (ABF 428, ODFL 396, XPO 23, Saia 1030, FedEx 438, TForce 813, AAA Cooper 660, Central 460, YRC form) and the contract (Walmart, First Brands, Home Depot) | Broker terms | — | Public |
| P17 | Carrier's re-bill window | 13710(a)(3)(A); XPO 23(5); Saia 1030(5); USA Truck 17; contracts (Home Depot §8, First Brands §13-14, Walmart) | — | — | Public |
| P18 | Payment terms, late fee, forfeiture | Rules tariff (SEFL 817, ABF 427, ODFL 434/564, XPO 207, Estes 720, TForce 721) | The bill's printed terms ("PAYMENT DUE DATE", XPO "TARIFF 199" late lines) | — | Public |
| P19 | Guaranteed-service terms | Rules tariff (SEFL 752, XPO 200) | BOL box "Guaranteed delivery requested"; DR banner | — | Public |
| P20 | Combination rules | Rules tariff (ABF 751 vs 440; XPO 224 one charge per address) | — | — | Public |
| P21 | Rounding, rate unit | Tariff (ODFL 565, Estes 530); the unit by testing weight × rate = charge | — | A fixed assumption per carrier | Derived |

### 2.2 Phase 2, shipment facts

| ID | Fact | Primary | Fallback | Never | If none |
|---|---|---|---|---|---|
| F01 | BOL number, PO, SID | BOL header (VICS top right; UPGF box 2; ODFL box 6) | 210 B3-03 / N9*BM / N9*PO; 214 B10-02 / L11 BM; the bill's "B/L NO." field or remarks; the rate con's reference fields (tokenise: Werner "502464982\|IDB61769\|954") | Amount + date as a key | Customer's TMS; Estes 210 sends "NS", UPS and TForce print "NONE" |
| F02 | Ship date | BOL header | 210 B3-12 or G62*86; the bill ("Shipment Date", SEFL footer first value, ODFL "PRO DATE"); 214 AF event; DR header | The bill date; a reprint's date | Customer |
| F03 | Shipper, consignee | BOL ship-from / ship-to | 210 N1 SH/CN + N3/N4; the bill's header; DR header (as the carrier keyed them) | — | Customer |
| F04 | Freight terms and third-party bill-to | BOL terms boxes and third-party box | Corrected BOL or letter of authority; rate con (brokered TL: it decides who pays the carrier); 210 B3-04 + N1*BT; the bill's terms box | The DR's bill-to account (it can differ from the bill's) | Customer; if blank the carrier defaults to prepaid (*assumed*: FedEx 360 ¶6, TForce 361-A per the exploration read) |
| F05 | Pieces | BOL carrier-information table (sum the lines; check against the grand total) | 210 L0-08/-09; the bill; DR count line | TL 210 L0-08 (junk: "30000 PLT") | Customer |
| F06 | Declared weight and unit | BOL weight column **with its header** ("WEIGHT (kg)" on a Pure Fishing BOL) | 204 AT8; the bill's "WEIGHT DECLARED AS" (TForce, UPS); 214 AT8 on the first message; derived from the original net on a corrected bill (SEFL 806625953: $744.77 ÷ (1−0.903) ÷ $315.97 = 2,430 lb) | The DR (printed after the reweigh) | Customer |
| F07 | Declared class and NMFC | BOL "LTL only" columns | 204 L5; the bill's echo ("CL125 NMFC 49880", ABF "CL 100 ITEM 057300-03V"); 210 L5-03/-04 | The rated class on the bill | Customer; blank on many shipper-printed BOLs (set 03) |
| F08 | Declared dimensions, cube | BOL description or cube box | The bill's "RATED DIMENSIONS" (ABF), handling-unit lines (TForce, ODFL); rate con crate lines (TL) | — | Customer |
| F09 | Services requested | BOL tick boxes (UPGF box 5; ODFL box 7 codes) and special instructions | The bill's echo of the BOL ("'LIFTGATE DELIVERY", "MUST DELIVER ON 7/15/24", "CALL 72HRS IN ADV FOR DEL APPT"); 204 notes; the carrier's quote-difference note | The DR (shows what was done, not what was asked), except a consignee's signed request written on it (Estes 567) | Customer; the carrier's record of a phoned request |
| F10 | Quote number on the BOL | BOL box (ODFL box 18 "Rate Estimate #") | The bill's printed quote ("QUOTE #CWEN3E465", "PQ SCHEDULE NO", "QN#") proves a quote was applied, not that it was on the BOL | — | Customer |
| F11 | Guaranteed / required delivery date | BOL box (UPGF "Guaranteed delivery requested"; ODFL box 16) | 204 G62 windows; DR banner ("XPRS DATE … DELIVER BY 17:00") | — | Customer |
| F12 | Actual weight | The carrier's weight certificate (UPS Freight set 04; TForce 21-015 p. 37; Holland 21-006 p. 15) | The bill's "ACTUAL WEIGHT IS" / "REWEIGHED WT" line; 214 AT8 at pickup; the DR's reweigh text | The BOL | **Carrier**, on request (FedEx 980 ¶2 promises a copy; others for a fee while the freight is in custody); carrier document APIs (ODFL, TForce) |
| F13 | Actual dims, density, inspector's note | The carrier's inspection or cube certificate (recompute weight ÷ cube) | The bill's "MEASURED CUBE", density lines, "CLASS INSPECTION PER W&I" | An NTEP type approval (a device approval, not a reading) | Carrier |
| F14 | Delivery date and time | Typed DR date/time (XPO 2025 "09:13 12/29/2025") | 214 AT7 D1 event (ODFL 2012-09-27 1107 CT); 210 B3-09 **only if** B3-10 = 035; TL invoices that print it (Werner, Taylor, USA Truck) | A handwritten DR date that conflicts; ODFL's 210 date (coded 017, estimated) | Carrier POD image or 214 |
| F15 | Services performed | DR tick boxes (XPO, Yellow) and printed verification lines ("ADDED SSC PER DR") | Driver notes; the carrier's remark on the bill | The BOL | Carrier POD; the consignee |
| F16 | Who received it | DR signature block, stamp ("Subject To Count"), exceptions | — | — | Carrier POD |
| F17 | Arrival, departure, wait times | The record the rate confirmation names (receiver's label, times "stamped and/or written on the BOL", a detention form) | DR arrive/depart boxes (UPS Freight 2008), wait-time boxes (Yellow); 214 X1 then D1 (no real 214 held has both) | The bill's detention line alone ("DETND/140" with no times) | Consignee's dock log; carrier ELD. **Not reported in any public file** |
| F18 | First delivery attempt | DR of the first attempt; 214 event with a reason | The bill's printed line ("ORIG DEL ATTEMPT: 05/25/2023", SEFL p. 35) | — | Carrier |
| F19 | Premises type | **No document.** | Evidence only: consignee name ("… CITY WHSE"), receiving stamp, the customer's knowledge of its customer, map or zoning data, the carrier's stated basis ("PER GOOGLE EARTH") | BOL or DR as proof either way | The customer's reviewer (ask once per address) |
| F20 | TL load number, stops, appointments, miles | Rate confirmation or 204 (S5 stops, G62 windows, L11 MI) | The invoice's load/dispatch number and miles (Werner, Taylor only) | A rate con filed beside the packet for another load | Customer |
| F21 | Shipper-side agreed TL price | The shipper's own rate confirmation, tender or 204 L3 | The invoice to the shipper (what was billed, not agreed) | A broker-to-carrier rate con | Customer |
| F22 | Lumper receipt, cancellation, layover record | The receipt; the carrier's or broker's notice record | The invoice line's face value | — | Customer, broker |

### 2.3 Phase 3, the money asked

| ID | Fact | Primary | Fallback | Never | If none |
|---|---|---|---|---|---|
| M01 | PRO | 210 B3-02 (TL also N9*IV) | PDF bill header ("Freight bill No", "FREIGHT BILL NO:", "LTL INVOICE#", "PRO. NO."); XPO scan line; the BOL's affixed PRO label; DR header; 214 B10-01; statement row | — | Always present |
| M02 | Carrier, sender | 210 B3-11 (SCAC) and ISA-06 / GS-02 (the envelope sender, e.g. a freight-payment firm) | PDF letterhead; statement header | ISA-06 as the carrier | Always present |
| M03 | Bill type | PDF title or banner **plus** a changed amount or bill-to on a known PRO | 210 B3-08 (unused in every real 210 held); statement Adj/BD flag (Estes); "DUP" / "PAST DUE" marks | The title alone (ODFL re-bills a new payer under "ORIGINAL INVOICE") | Derived: group every print by PRO |
| M04 | Bill date; first bill date | The earliest of: the first 210's B3-06 for that PRO; the PDF bill date (SEFL "DATE BILLED", ODFL "Invoice Date"); the earliest "PREVIOUSLY INVOICED ON" entry (TForce, UPS; the list runs newest first and can stop short); Estes statement "Freight Bill Date" | Statement date (flag as late) | A reprint's date; ABF and XPO print no bill date | Mark the clock "unknown, no later than …" |
| M05 | Due date | PDF ("PAYMENT DUE DATE", "PAYMENT IS DUE BY") | Tariff payment item + bill date | — | Derived |
| M06 | Terms as billed, bill-to | 210 B3-04 + N1*BT | PDF terms box ("PREPAID" / "COLLECT" / "THIRD PARTY", ODFL "P/C" box) and bill-to block; statement P/C | — | Always present |
| M07 | Rated class | PDF class column ("CLASS 70.0", ABF "EX70") | 210 L7-07 | — | Always present on LTL |
| M08 | Billed, "as" and deficit weight | PDF weight column; "AS WEIGHT 1,000 / DEFICIT 214"; "DEF111 AS500" | 210 L0-04; L3-01 rated weight; ODFL L1 DAA line; AAA Cooper L0-02 | — | Always present on LTL |
| M09 | Rate and unit | PDF rate column, unit settled by weight × rate = charge (SEFL "60080" = $600.80/cwt; ABF "73317"; XPO "391.89") | 210 L1-02/-03 (qualifier can mislabel: Estes "LB" is per cwt) | A fixed unit assumption | Always present |
| M10 | Gross | PDF line extension | 210 L1-04 (cents) | — | Derived: Σ weight × rate |
| M11 | Discount % and $ | PDF printed % and $ | 210 L5 text (AAA Cooper, Estes); derived $ ÷ gross (ODFL 210; XPO "DISCOUNT SAVES YOU" prints $ only) | — | Derived |
| M12 | Minimum lift | PDF "MCADJ", "MIN", "M", "MIN FRT CHG" | 210 code MMC (AAA Cooper) | — | Derived: compare net with the floor |
| M13 | Fuel % and $ | PDF ("FSC 30.3%", "LTL FUEL SURCHARGE OF 22.00%") | 210 L5 text; derived $ ÷ net (ODFL; XPO volume bills; UPS "003570" = 35.70%) | — | Derived |
| M14 | Accessorial lines | PDF name (+ code at ABF, XPO, TForce; name only at SEFL, ODFL) | 210 L1-08 codes (405/FUE, DSC, LUM, LAY, TONU, STOP, SUF) with L5 text | — | Always present; uncoded lines exist (ODFL $24, $11) |
| M15 | Correction fee | PDF ("CBR REWEIGH OF SHIPMENT FEE", "CORRECTED BILL OF LADING CHARGE", UPS "002550 INSPECTION") | 210 coded line | — | Always printed when charged |
| M16 | Total | 210 B3-07 = L3-05 (82 of 82 real 210s reconcile) | PDF "TOTAL" / "TOTAL AMOUNT DUE" / "PAY THIS AMOUNT", cross-checked against the column sum and the scan line (XPO) | SEFL 2020 "PAY THIS AMOUNT" (a base plus a 25% penalty, p. 49) | Derived |
| M17 | Previously billed, paid, balance | XPO "AMOUNT PAID / BALANCE DUE"; SEFL balance-due "PAY THIS AMOUNT"; ABF "original total … correct charge … reduction" | Statement (cash posted, remaining); A/R history (set 21 pp. 13-16); derived original = new total − balance due | — | Customer's AP record |
| M18 | Carrier's reason | PDF remarks and reason codes (ABF "W02/AUTH:Reweigh - See W&R certificate"; SEFL "** PER GOOGLE EARTH …"; ODFL "CBL DGB 2/14/05 …"; TForce "*** SHIPMENT REWEIGHED ***") | 210 K1 (never used in a real file) or L5 remarks (Estes) | — | **Carrier**: no real 210 carries it; SEFL's corrected prints sometimes print nothing (896789802, p. 63) |
| M19 | BOL echo on the bill | PDF description block (SEFL, ABF, ODFL) | — | — | Not on 210s or XPO bills |
| M20 | Printed references | PDF: quote ("QUOTE #", "PQ SCHEDULE NO", "QN#"), tariff ("Tariff: AOD000", "TARIFF 559", "TARIFF CNWY-199"), authority ("AU=ABF646-468646"), account | 210 L7 (tariff), N9 (references) | — | Per carrier |
| M21 | Page counter | PDF ("1 of 1", "Page 2 of 3", "( continued on next page )") | None: group pages by PRO and test the column sum | A counter as proof of completeness (SEFL p. 49 "1 of 3" with pp. 2-3 absent) | Derived |
| M22 | Previously invoiced on | TForce / UPS Freight reprint list | Statement rows per PRO (Estes freight bill date) | — | Not printed by SEFL, ABF, XPO, ODFL |
| M23 | Delivery date on the bill | TL invoices (Werner, Taylor, USA Truck); 210 B3-09 with qualifier | — | 210 coded 017 as an actual date | Use F14 |
| M24 | Statement fields | Statement (aging, cash posted, Adj/BD, remaining, interest) | Carrier portal | — | Customer AP for the shipper's side |
| M25 | Interline partner, share | 210 R3 (AAA Cooper: NEMF, $126.98 of $325.60) | PDF boxes (SEFL C/L PRO, TForce ADV/BEY, ODFL ORIG/DEST I/L); partner's "CORR REPT" | — | Carrier |

### 2.4 Phase 4, the dispute

| ID | Fact | Primary | Fallback | Never | If none |
|---|---|---|---|---|---|
| D01 | Window start dates, earliest deadline | Computed from P16/P17 + M04 (receipt of each bill) + F02 (ship date) + D07 (payment date for Walmart-style contracts) | — | The reprint date | Derived; "unknown" if M04 is unknown |
| D02 | Claim content | The claim form or letter (set 23: 3PL letters; set 16: carrier forms; SF 1113) | The shipper's worksheet row (set 02 "OVER CHG") as a draft | — | The software fills it from M01, M04, M16, M18, P10 |
| D03 | Proof attached | The claim's attachments (set 23: BOL, shipper's weight certificate, spec sheet, inventory) | — | A brochure or sample BOL (YRC refuses them) | Customer, carrier (certificate) |
| D04 | Filing and acknowledgement dates | The claim letter's date; the carrier's acknowledgement (no stand-alone one held; YRC's status page prints a received date, 23-006) | Email headers, portal records | — | Customer |
| D05 | Decision, reason, date | The carrier's answer (YRC "APPROVED" status with draft number; GlobalTranz's quoted decline "per YRC Tariff 100-754 … Self-Storage Warehouse") | ODFL's refund-and-re-bill history (set 21) as an implicit decision | — | Carrier; **no stand-alone denial letter or credit memo is public**; YRC's page prints the draft date, not the decision date |
| D06 | Credit, refund, draft | The answer (YRC draft 1385879, $612.77, 06/20/23); A/R history (ODFL refunds $1,828.04 and $584.63) | Statement credit rows (Kuehne+Nagel item type A; RXO adjusted/credited columns) | — | Customer AP |
| D07 | Payment record | The shipper's AP export or remittance | A/R history in a carrier's claim (set 21); XPO "AMOUNT PAID"; statement cash posted; the 3PL's invoice and its payment to the carrier | — | **Customer only; never public** |
| D08 | Dispute log / worksheet | The shipper's spreadsheet (set 02 pp. 99-224) | A broker's dispute ledger (TQL, 23-010) | — | Customer |

### 2.5 The keys that open the next document

"Where to look next" needs the document and the key that finds the right page of it. Rule [our call, AV §5, AW §5]: match on **PRO** first (strip dashes, SCAC prefixes, check characters and letter suffixes; try with and without leading zeros), then on **BOL number** (zeros and punctuation stripped; split multi-value fields such as "63387,63388"; tokenise pipe-separated reference strings), then on **PO + ship date + consignee**; for TL on **load or tender number**, then trailer + pickup date. **Never match on amount + date**: 23 of the 101 ABF bills share both with another bill; two TQL pairs and one Werner pair match on lane, amount and adjacent dates. Known failures: a rate confirmation's "Bill of Lading Number" holding the shipper's SID (set 22); a Werner bill printing "RETURN" for the shipper number while its BOL says 104310; a freight-forwarder booking number standing in for a BOL number; child PROs per pallet (XPO 2025 DR); an older carrier's PRO on a billing advice reused as the BOL (TForce).

## 3. Overlap: where a fact can be found twice, and which copy wins

### 3.1 Facts carried by two or more documents, and the precedence when they disagree

| Fact | Copies | Winner, and why | Seen |
|---|---|---|---|
| Weight | BOL (declared) → bill (billed; "declared as" and "actual is" at TForce/UPS) → certificate → 214 AT8 → shipper's own scale ticket | **The carrier's legal-for-trade reading** (NMFC 250100-A §4 "actual gross weight"; Uniform BOL §7(d) "the articles actually shipped"), rebuttable only with better evidence (Estes 992 ¶4 "satisfactory proof"; FedEx 980 ¶3) | XPO 590.48 → 660 lb; UPS 4,117 → 4,825; SEFL 2,430 → 2,720 with no certificate |
| Class / NMFC | BOL → bill's echo → rated class → inspection certificate | **The inspection, where it shows dimensions** (250100-A §3(a)); FAK from the agreement decides the rated class | UPS 450285371: BOL class 100, certificate 9.70 pcf, billed 150 |
| Payer and terms | BOL box → corrected BOL / letter of authority → rate con (brokered TL) → 210 B3-04 → bill-to → DR bill-to | **The BOL as corrected by written authority**; in brokered TL the rate con | Winn-Dixie: BOL collect, re-billed prepaid third party "per letter" (set 21); DR bill-to 24068435 vs bill 32801414 (set 04) |
| Ship date | BOL → 210 B3-12 / G62 → bill → DR → 214 AF | BOL or 210; a one-day gap between BOL and pickup is normal | TForce bill 12/20/2022 vs billing advice 12/13/22 (handoff between carriers) |
| Delivery date and time | DR → 214 D1 → 210 B3-09 (035 only) → TL invoice | **Typed DR or 214**; a 210 date coded 017 is an estimate | ODFL 00902527924: 210 "20120927" coded 017; 214 D1 2012-09-27 11:07 CT |
| Services requested vs performed | BOL boxes / instructions → bill echo → DR boxes → carrier remark | Request from the BOL; performance from the DR; the tariff decides whether the request matters (SEFL 890-100 "required or requested") | XPO 326-343835: BOL "Appointment needed" → APT $51.90 |
| Discount % | Agreement → bill printed % → 210 L5 text → DSC ÷ gross | **Agreement** (the others are what was billed) | ODFL 210: 188.00 ÷ 261.11 = 72.0% |
| Fuel % | Contract table → carrier table at the index week → bill printed % → $ ÷ net | **Contract table, else carrier table**; the bill's % is the claim | ABF 30.3% billed vs 31.70% in a later issue: not checkable |
| Original total on a correction | ABF prints old and new → XPO prints paid and balance → SEFL prints only the difference → derive new total − balance due | Printed if present; derived otherwise, and shown as derived | SEFL 806625953: $1,088.74 − $110.23 = $978.51 = the worksheet row |
| Bill type | Title → changed amount or payer on a known PRO → statement flag → B3-08 | **PRO + change**, title second | ODFL re-bill titled ORIGINAL INVOICE; SEFL 2025 "PAST DUE" reprints |
| Quote applied | BOL box 18 → bill quote number → carrier difference note → the quote document | The quote document; the bill proves only that one was applied | ABF: 82 PQ numbers, 27 difference notes |
| TL price | Shipper's rate con / 204 L3 → invoice → broker-to-carrier rate con | Shipper's own rate con; the invoice is the claim | Taylor: $993.96 + 332 × $0.47 = $1,150.00 = rate con |
| Miles | Rate con → invoice (Werner, Taylor) → mileage engine | The contract's mileage basis (PC*MILER version) | Taylor rate con 335.15 vs invoice 332 |
| Pieces | BOL lines → BOL total → bill → DR count | The carrier's count on the bill and DR; BOL totals can be internally inconsistent | XPO 405-634110: BOL "10" against 9 pallet lines, billed 9 |

### 3.2 Facts carried by exactly one document (single points of failure)

- **The carrier's reason for a change** (M18): the PDF bill only. No real 210 fills K1; SEFL's corrected prints sometimes carry nothing. If the PDF is lost, the reason is NOT REPORTED.
- **Lane discounts, FAK, floors, exception prices** (P04–P06, P09): the agreement only. The bill repeats the discount applied, never the one agreed.
- **The first-attempt record** (F18): the DR of the first attempt or a 214 event; SEFL prints the date on the redelivery bill, other carriers do not.
- **"Previously invoiced on"** (M22): TForce and UPS Freight reprints only.
- **The quote's conditions** (P08): the quote document only; no public example exists.
- **Arrival and departure times** (F17): the one record the rate confirmation names; nothing else.
- **The carrier's decision and its date** (D05): the carrier's answer only; nothing on the bill side records it.

### 3.3 Facts carried by no document in the chain

- **Premises type** (F19): nothing authoritative. The carrier's own basis is a map lookup ("PER GOOGLE EARTH"); the shipper's is its knowledge of its customer; a stamp shows a business received the freight, not that no dwelling stands on the premises.
- **The device behind a certificate** (device ID, NTEP number, last inspection): no certificate held names one.
- **Whether a delay was the carrier's or the consignee's fault** (E1, E2, D3): the 214 reason code is "NS" in every real file.
- **The shipper's payment** (D07): never public.
- **The shipper-side TL price when a broker is used** (F21): every rate confirmation held is broker-to-carrier.
- **The transit standard for a guarantee** (E1): the carrier's published tables, not in the chain.

### 3.4 Facts that can be derived when their copy is missing

| Missing | Derive from | Example |
|---|---|---|
| Discount % | DSC ÷ gross | ODFL 210: 72.0% |
| Fuel % | fuel $ ÷ net linehaul | ODFL 210: 17.5% |
| Original total | new total − balance due | SEFL 806625953: $978.51 |
| Original weight | original net ÷ (1 − discount) ÷ rate | SEFL 806625953: 2,430 lb |
| Amount paid | total − balance due | XPO 266-489086: $150.00 |
| Rate unit | weight × rate = charge | SEFL "60080" = $600.80/cwt |
| Deficit weight | rated weight − actual | ODFL 1,000 − 833 = 167 lb |
| TL fuel per mile | fuel $ ÷ miles | Werner $93.94 ÷ 154 = $0.61 |
| First bill date (bound) | earliest "previously invoiced" entry, else "no later than" the earliest print held | TForce 610384246: 03/15/23 |

A derived value is shown as derived, never as read (`software-initial-pitch.md` §5.4: "No number without a place on the page").

## 4. NOT REPORTED: what it means, and what it does to the clocks

A fact is NOT REPORTED when the software has looked in its primary location and every fallback in §2 and found nothing. The verdict then depends on **who owed the fact**. Citations are to items in `data/sources/13_rules_tariffs/`, the NMFC and uniform BOL texts in set 15, the claim forms in set 16, the case texts in sets 08 and 20, and 49 CFR Part 378 as quoted in AX §7 (fetched from the eCFR 2026-09-01 and re-fetched by the AX review). Tariff items are the current issues; applying them to older bills is *assumed* unless the item prints an effective date that covers the ship date.

### 4.1 Who owed it

| Owed by | Facts | What the rules do when it is missing |
|---|---|---|
| **The shipper** (its BOL) | F04 terms, F05 pieces, F06 weight, F07 class/NMFC, F08 dimensions, F09 service marks (residential, limited access, liftgate, appointment), F10 quote number | The carrier fills the gap, normally against the shipper, and charges a fee (§4.2) |
| **The carrier** (its bill and its records) | F12 certificate behind a reweigh, F13 inspection note, F14 delivery time, F18 first attempt, M04 first bill date, M18 reason for a change, M13 fuel % | The charge is unsupported until the carrier produces the record; the shipper can ask, and in a claim the carrier must ask for what *it* needs (§4.3) |
| **Nobody** (a fact about the world) | F19 premises type; who caused a delay | A question for the reviewer, asked once per address |
| **The customer's own files** | D07 payment record, F21 its TL rate con, P02 its agreement, P08 its quote | Not checkable until the customer supplies it; named as a request |

### 4.2 Shipper-owed and missing: not a dispute, but the carrier's licence to re-bill

The documents say, consistently, that an incomplete BOL does not protect the shipper:
- **Weight.** NMFC Item 250100-A §4 (set 15, `nmfc_100-AS_supplement1_2019` l. 1695): "If the stated weight is found to be inaccurate, the carrier or agent shall correct the weight accordingly. Freight charges must be assessed on the actual gross weight of the shipment". Uniform BOL §7(d): if the description "including weight or density … is found to be incorrect or incomplete, the freight charges must be paid based upon the articles actually shipped". No weight at all on the BOL: the carrier weighs and charges (ABF 992 ¶4, "when no weight whatsoever is provided", l. 5630; Estes 993, "without stating the shipment weight", l. 4333, $20; ODFL 367 ¶7 $25; XPO 239 $50.70; Central 400(b) $35). *verified*
- **Class and description.** If the class or density cannot be determined, the default is punitive: SEFL 170 "the shipment will be rated at Class 150" (l. 331-342); XPO 26.3 "initially be billed/rated using class 150" (l. 1010); Estes 170 "assigned a class 175 rating" (l. 484); TForce "not to exceed a class 250 rating" (l. 1404) and, per the exploration read, an omitted dimension defaults to 120×96×96 in (*assumed*, not re-opened). ODFL 100-Q (l. 727-736) adds a verification fee when the shipper "fails to indicate the correct description, density, or weight". *verified* except where marked
- **Service marks.** SEFL 753 §2 (effective December 16, 2022): the shipper's omission "will not relieve the shipper and/or consignee from the responsibility of paying the residential delivery service charges" (l. 2683-2686); SEFL 754 says the same for limited access (l. 2727); Estes 751 and 751-10 carry the same sentence (l. 3383, 3498); TForce charges residential if "Carrier's systems or the actual delivery address is considered a Residence (regardless of a shipper's designation …)" (l. 2856). *verified*
- **Freight terms.** Blank terms default to prepaid, billed to the shipper (FedEx 360 ¶6; TForce 361-A ¶3: *assumed*, from the exploration read).

So on a line the carrier added because the BOL was silent, **the shipper's NOT REPORTED is not grounds for a dispute**. It is the opposite: the rule gives the carrier the right to fill the blank. The dispute, if any, is about the **fact** the carrier filled in (was it really 660 lb; is there really a dwelling), and that is a trigger question for stage 6, decided on the carrier-owed record (§4.3) or the reviewer's knowledge.

One exception, outside our market: on government bills the burden runs the other way. In *PJAX Freight* (CBCA 552-RATE, set 20, l. 342) the board held that "The absence of a notation on a delivery receipt does not establish that the Government ordered" the service, and the carrier's claim failed.

### 4.3 Carrier-owed and missing: a flag, with the ask "produce the record"

When the carrier changed a bill and the record behind the change is NOT REPORTED, the line is a **flag** whose proof is a document the carrier holds:
- **The certificate.** Only FedEx Freight promises it: Item 980 ¶2, "Carrier will make a copy of the written or electronic weight verification available to Shipper or Consignee upon request" (series b, l. 3348). NIST Handbook 44 §5.58 requires dimensioner data that is "available upon request by customer" to be kept "for at least 30 calendar days after the date of invoicing" (set 15, l. 229-230), so the ask must go out fast. Elsewhere a certified weight is a paid service only while the freight is in the carrier's custody (SEFL 992 $33; ABF 992 ¶5 $317.17 plus the scale fee; TForce 990 $220; FedEx 990 $155 or $419). Carrier document APIs (ODFL, TForce; set 17) are the fast channel where they exist. *verified*
- **The reason.** No rule requires a reason, an inspection note or the fuel percentage to be printed (searched for and not found; the nearest is 49 U.S.C. 13708(a)'s duty to disclose "the actual rates, charges, or allowances", quoted in *Sivak v. UPS*, set 08). So a corrected bill with no reason is lawful but unsupported: the line is flagged "unexplained change" and the claim asks for the basis.
- **In the claim itself.** Part 378.4(d) and 378.5(c): missing papers are "not … grounds for disallowance", and the carrier must ask for what it needs; NMFC 300330(d)/300340(c) repeat it, and for ordinary carriers NMFC 300520(g) says the carrier "shall notify the claimant in 5 business days and request the information required" (set 15, `nmfc_100-AO_supplement1_2015` l. 1257). *verified*. In practice carriers push back: XPO's claim page says a claim without the required documentation will be "rejected and sent back for additional information" (set 16, l. 22); ODFL 396 ¶2 and Central 460(2) deem a claim "closed 30 days after the date of the initial ruling" unless more information arrives; ODFL may charge $50 when a claim is settled "through no fault of Carrier". *verified*
- **What proof the shipper needs to overturn a reclass is defined;** for a reweigh it is thinner. Reclass: "an invoice or packing slip along with a pre-printed specification sheet or catalog page, which lists the commodity description, weight, and shipping dimensions" (SEFL 170 Note 3, l. 349; Estes 170 Note C; XPO 205 the same); TForce refuses an edited copy of the BOL. Reweigh: "satisfactory proof" (Estes 992 ¶4), "documentation that the weight was in error" (FedEx 980 ¶3), a "certified weight ticket" or "vendor invoice … when claim is based on weight" (YRC F-154, ABF and FedEx forms, set 16). On an interline move the destination carrier's weight governs (NMFC 401400-A). *verified*

### 4.4 Is anyone time-bound to re-report?

| Who | What | Window | Source |
|---|---|---|---|
| Shipper | Correct the BOL (payer, description, weight) | 30 days from the initial BOL (ABF 362, payor change), from acceptance (XPO 205, l. 1470), or from the bill date (R+L 364; Estes 360-03, $20 letter-of-authority fee after 30 days); with "conclusive documentary proof" (ODFL 365, XPO 205) or "documentary proof" (SEFL 360-5 §5, l. 545) | *verified* |
| Shipper | Add a spot-quote number not on the original BOL | Treated as a corrected BOL, $35 (SEFL 360-5 §6, l. 549) | *verified* |
| Shipper | Correct dimensions | Refused "after the shipment has been tendered for delivery" (TForce, exploration read) | *assumed* |
| Carrier | Bill additional charges | 180 days from receipt of the original bill, or lose "the right to collect such charges" (49 U.S.C. 13710(a)(3)(A), quoted in *Southern Furniture v. YRC*, set 08, l. 299-301, 366); restated from the bill date (XPO 23(5), l. 840; Saia 1030(5), l. 7796, which carves out discount revocation for non-payment; USA Truck 17) or the ship date (ABF 428, l. 1917, "overcharge and undercharge claims … within 180 days of the initial shipment date"; AAA Cooper 660; Werner 585); shortened by contract (Home Depot §8: invoices "not presented within ninety (90) days" are waived, set 23 l. 1218; First Brands §13-14: 180 days or "null and void"; Walmart: 12 months) | *verified* (Walmart from AX's OCR) |
| Shipper | Contest a bill | 180 days from receipt of *each* bill, original or subsequent (13710(a)(3)(B), l. 307, 370); carriers' start dates differ: ship date (ABF 428, YRC form "180 days of pickup"), carrier's receipt of the freight (ODFL 396, Central 460), bill date (XPO 23(5), Saia 1030(6)), receipt of invoice plus 7 days (FedEx 438, l. 1378), tender plus 10 days (TForce 813), "5 business days from the invoice date" (NMFC 300320/300520); SEFL has no item, so the statute governs; brokers 5-30 days (AM §AM4.3); XPO's page: only after the invoice is paid (set 16, l. 28) | *verified* |
| Carrier | Answer a claim | Acknowledge within 30 days (378.7); pay, decline or settle within 60 (378.8), extendable only by written agreement; refund an overpayment it finds itself within 30 days (378.9(b)); a non-collecting carrier forwards within 15 days (378.3(a)) | *verified* (AX §7) |
| Carrier | Keep the dimensioner record | 30 calendar days after invoicing (HB44 §5.58) | *verified* |

### 4.5 What NOT REPORTED does to the 180 days

1. **Nothing stops the shipper's clock.** The statute is a notice requirement: the court in *Southern Furniture* quotes the STB, "So long as the necessary notification is given … within the 180-day period, the moving party preserves its right of action", and holds that "compliance with the 180-day time limit is not optional" (l. 441). The shipper in that case learned of the carrier's silent practice years later from a DOJ unsealing and was still barred. No source pauses either the shipper's 180 days or the carrier's 60 days while a document is missing (searched; not found). **Rule for the software [our call]: a line whose proof is NOT REPORTED is still flagged, with the deadline shown, and the claim is filed inside the window with the missing record requested in it.** Part 378.4(d) means the missing paper cannot be the reason the claim fails; the carrier must ask for it.
2. **Each balance-due print restarts the shipper's clock for that print only.** 13710(a)(3)(B) runs from receipt of "the original bill or subsequent bill"; the 2023 balance-due prints in set 02 gave 180 days from their own receipt (about 2023-12-16 and 2023-11-01), and the 2025 "PAST DUE" reprints gave none, because they are reprints, not new bills.
3. **The carrier's own 180 days is itself a check.** A balance-due bill issued more than 180 days after the shipper received the original (or after the shorter contract window) is a dispute on A4 whatever its merits (SEFL 896789802 was corrected 452 days after shipment with no reason printed, p. 63; whether the original bill was received more than 180 days before is NOT REPORTED, because SEFL prints no first-bill date on a corrected print). No real post-180-day balance-due bill with its original was found in `data/`.
4. **The bar is one-directional.** The 180-day rule "applies only to actions initiated by shippers, not to defenses raised by shippers in actions initiated by carriers" (*PJAX*, set 20, l. 128), so a shipper sued on a late balance-due bill can still defend; and the STB lets a carrier pay a late claim voluntarily (AM, C-AM25). Neither is something the software should count on.
5. **When the first bill date is itself NOT REPORTED** (SEFL and XPO corrected prints, ABF: no bill date printed), the clock is shown as "unknown, no later than" the earliest print or statement date held, and the deadline is computed from that bound. The reviewer sees the uncertainty, not a false date.

### 4.6 The decision table

| Fact missing | Owed by | The line's state | What is shown | The clock |
|---|---|---|---|---|
| F06/F07/F09 declared weight, class, service mark, and the carrier billed on its own reading | Shipper | Trigger in question, decided on the carrier's record (F12/F13) or the reviewer (F19); the omission itself is not the dispute | "The BOL did not state X; the carrier billed Y; its basis is [certificate / none]" | Shipper's 180 days from the balance-due bill |
| F12/F13 certificate behind a reweigh or reclass | Carrier | **Flag**: unsupported change | Dollars at stake, "ask the carrier for the certificate (FedEx 980 ¶2; HB44 30 days)" | Shipper's 180 days; HB44's 30 days for the device record |
| M18 reason for a change | Carrier | **Flag**: unexplained change | The old and new totals, "no reason printed" | Shipper's 180 days |
| M04 first bill date | Carrier | Clock unknown | "no later than [earliest print]" | Computed from the bound |
| F14/F17 delivery or detention times | Carrier (LTL) / the record the rate con names (TL) | Not checkable (LTL guarantee, detention) or **flag** (TL: "no times, no detention" per the rate con's own rule) | Which record is missing and who holds it | Shipper's 180 days; TL dispute windows of 5-30 days |
| F19 premises type | Nobody | **Ask the reviewer**, once per address | The consignee, the carrier's stated basis, the stamp, the carrier's definition of "residence" | Shipper's 180 days |
| P02/P04/P09 the agreement | Customer | Not checkable (price lines); trigger lines still run | "upload the agreement version in force on [ship date]" | — |
| P12 fuel table for that week | Carrier | Not checkable | "fuel 22.00% as billed; no table for the week of [date]" | — |
| P13 base rate | Licence | Not checkable (gross); arithmetic still checked | "rate $600.80/cwt as billed" | — |
| D07 payment record | Customer | Not checkable (A2 via 3PL, A3, F1) | "connect the AP export" | — |
| D05 carrier's answer | Carrier | Open claim | Days since filing against 30/60 | Carrier's 30/60 days |

## 5. Six real chains walked through the map

Method: three agents (2026-10-10), one per pair of chains, each given the §1 fact list as a template and told to report, for every fact ID, the file and page or X12 segment where it was found, the value, and whether it came from the primary location, a fallback, a derivation, or nowhere (NOT REPORTED, with the places looked). Scanned pages with no text layer (sets 03, 21, 23, parts of 02 and 22) were rendered with `pdftoppm` and read as images. The coordinator then re-opened every verdict-setting number at the source: the 210 and 214 segments by grep, the date and money arithmetic in `python3 -I`, and SEFL p. 46, XPO p. 12 and ODFL's receivable history p. 15 as rendered pages; all matched. The tables below keep the rows that carry information; facts marked n/a (TL-only facts on an LTL chain and the reverse) are omitted, and NOT REPORTED facts are listed in one line per chain. Full 76-row walks are in the agents' reports, summarised here. Page numbers are PDF pages.

### 5.1 Chain A: SEFL 807148067 (set 02, Exist v. SEFL). Phases 1, 3 and 4 held; phase 2 absent

What the exhibit holds: the agreement in three dated versions (pp. 12-20), the pallet page (p. 21) and the accessorial-exceptions page (p. 22); the balance-due print of 06/19/2023 (p. 46) and its 2025 reprint (p. 33); the shipper's worksheet row (p. 210, headers p. 199, "OVER CHG" column p. 223); the complaint (pp. 5-10). No BOL, no delivery receipt, no certificate, no original bill, no carrier answer.

| ID | Found at | Value | How |
|---|---|---|---|
| P01 | SEFL 1090 Item 753 §5; bill p. 46 "PREPAID", bill-to Exist | payor = the shipper; its agreement (account 071-003454 on both the 2023 version p. 18 and the bill footer) | primary |
| P02 | pp. 12, 15, 18: 01/15/2021, 06/08/2022, 04/12/2023, "TARIFF SEFL 6009, RATING ITEM 000-068386" | version in force on 05/15/2023 = 04/12/2023 | primary, picked by F02 |
| P03 | p. 18 "SEFL-0550 01/10/22" | base tariff and edition named; the table itself not held | primary |
| P04 | p. 19 WCPC outbound | 88.15% (90.90% in the 2021 version) | primary; lane code resolved through the definitions page p. 20 (OR = WCPC) |
| P05 | p. 19 | FAK class 70 on NMFC classes 77.5-175 | primary |
| P06 | p. 20 Item 610 | $152.00 floor for OR | primary |
| P07 | SEFL 1090 Item 610-100 (eff. April 19, 2022) | ≥750 ft³ and <6 pcf → cube × 6 lb at class 150 | fallback to the tariff; agreement silent |
| P09 | p. 22 (image only; rendered) | liftgate DIRECT→PARTNERSHIP $55 minimum, eff. 4/7/2021; **no residential exception** | primary |
| P10 | SEFL 1090 Item 753 (eff. December 16, 2022) | $7.60/cwt, min $94, max $575; "entire premises on which a dwelling for living is located"; BOL omission "will not relieve" | primary, edition in force |
| P11 | Items 996 (eff. Dec 1st, 2025), 992 (eff. March 1, 2021) | $15 correction fee; $33 weight verification on request | fallback; 996 post-dates the bill |
| P12 | bill p. 46 "LTL FUEL SURCHARGE OF 22.00%"; Item 110 | 22.00% on net linehaul; **the table for the week: NOT REPORTED** | % from the bill; base derived (79.72 = 22% × 362.38) |
| P13 | bill p. 46 "60080" | $600.80/cwt, class 70; not checkable | derived (5.09 × 600.80 = 3,058.07) |
| P16, P17 | SEFL 1090: no overcharge-claim item (text search: 0 hits); Item 202 ¶7 covers allowances only | the statute governs | NOT REPORTED in the tariff |
| P18 | Item 817 (eff. March 1, 2021) | 15 days; 25% on collection; 06/19 + 15 = 07/04/2023 = the printed due date | primary, reconciles |
| F01-F05, F07, F09, F10 | bill p. 46 footer and description block | B/L 51124115; shipped 05/15/2023; Exist, Miami Gardens FL → a consignee in Sisters, OR; prepaid; 1 pallet "STC 16 BX"; "APPAREL IT-49880" rated "CLASS 70.0"; "*LIFTGATE DELIVERY"; "QUOTE #CWEN3E465" | **all from the bill's echo of the BOL** (fallback); the BOL itself is absent |
| F06 | bill p. 46 | 509 lb; declared = billed, no reweigh note | fallback; the declared weight is unproven |
| F19 | bill p. 46 "** PER GOOGLE EARTH THIS IS A PRA DLVY" | the carrier's assertion only | the remark is the only evidence; the BOL could not fill it anyway (Item 753 §2) |
| M01-M03 | p. 46 "FREIGHT BILL NO: 807148067", "BALANCE DUE INVOICE", "1 of 1"; p. 33 "PAST DUE INVOICE" | one bill, two prints; the original print is not in the exhibit | primary |
| M04, M05 | p. 46 footer "DATE BILLED 06/19/2023", "PAYMENT DUE DATE 07/04/2023" | the balance-due print's dates; the first-bill date NOT REPORTED | read **by position** after rendering: the text layer prints the labels as `?AY TfiIS A.P3OUNT`, `R=?:IT T0:` |
| M07-M16 | p. 46 | 509 lb × $600.80/cwt = 3,058.07; 88.15% = 2,695.69; net 362.38; LIFTGATE SVC 55.00; PVT RESIDEN 94.00; fuel 79.72; TOTAL 591.10 | primary; every line recomputed and reconciles |
| M17 | p. 46 "PAY THIS AMOUNT 94.00" against TOTAL 591.10 | previously billed 497.10 | derived (591.10 − 94.00); the worksheet row confirms 362.38 + 55 + 79.72 = 497.10 |
| M18 | p. 46 | "** PER GOOGLE EARTH THIS IS A PRA DLVY" | primary |
| M22 | p. 33 | the 2025 reprint prints "PREPAID 591.10" and "INVOICE PENDING", the full total, not the balance | primary |
| M25 | p. 46 "DEST C/L OAKH"; p. 33 "SEFL 34844332 OAKH" | interline partner; share NOT REPORTED | footer |
| D01 | derived | from the balance-due print: 2023-12-16; from the ship date (ABF-style rule): 2023-11-11; SEFL's own start date NOT REPORTED | derived |
| D02, D08 | worksheet p. 210 row 364; complaint pp. 5-10 | row: 1 PLT, $55.00, $79.72, $362.38, "NEED TO BE CHG" $152.00, "OVER CHG" $210.38 (p. 223); the suit claims "no less than $271,828.70", filed 10/07/2025 | primary |
| D04, D05 | complaint p. 7 ¶9 | "demanded … SEFL refused", undated; no written decision | NOT REPORTED beyond the allegation |
| D07 | derived from M17 | $497.10 paid; date and reference NOT REPORTED | derived |

NOT REPORTED in this chain: F08, F11, F14-F17 (no DR), the certificate (none needed here), M23, M24, D06; P12's table; P16/P17 in the tariff.

**Sibling 806625953 (pp. 41, 28; worksheet p. 208 row 292).** Shipped 04/19/2023 to Duluth, MN (MWPC: 90.30%, floor $127.50 in the 04/12/2023 version, seven days old at shipment). The balance-due print of 05/05/2023 bills 405 + 2,315 = 2,720 lb at $315.97/cwt: gross 8,594.39, discount 7,760.73, net 833.66, liftgate 55.00, fuel 24.00% = 200.08, total 1,088.74, PAY THIS AMOUNT 110.23; **no remark of any kind**. The prior total 978.51 and the original 2,430 lb are derived (worksheet FRT CHARGE 744.77 ÷ 0.097 ÷ 315.97 = 24.30 cwt); no document prints 2,430. The bill echoes "CL150 NMFC 49880-" and "CL125 NMFC 49880-", both rated 70 under the FAK. The worksheet's "NEED TO BE CHG" is $510.00 = 4 pallets × $127.50, the misreading of Item 610.

**Bill 806266163 (p. 94)** prints what the others do not: the cube rule "T 1090C 610-100 1548.75 CF 5.76 PCF / AW 8920 CW 9292.5" (1,548.75 × 6 = 9,292.5; 8,920 ÷ 1,548.75 = 5.76), "**SEFL W&I INSPECTED TO A CUBIC CAPACITY MOVE", three articles re-rated class 150, "MIN FRT CHG 3454.14", and, in the *description* column, "Gross Charge is $27523.00 / Discount Percentage % 87.45 / Discount Amount $24068.86" (NEPC outbound in the 06/08/2022 version, right for a 03/31/2023 shipment to MD), plus "PVT RESIDEN 575.00" (8,920 × 7.60/100 = 677.92, capped at $575).

**Verdicts.** PVT RESIDEN $94.00: price **matches** Item 753 (38.68 → $94 minimum); trigger → **ask the reviewer**, one question for the Sisters, OR address. LIFTGATE $55.00: price **matches** p. 22; performance NOT REPORTED (no DR), so strictly "ask the reviewer" on the trigger, though the request is on the bill's echo. Linehaul: **matches** (3,058.07 → 362.38 > $152 floor); the fuel percent and the gross rate: **not checkable**. Sibling's weight raise 2,430 → 2,720: **flag** (+290 lb, no W&I note, no certificate, no correction fee; the worksheet never saw it). Clock: 2023-12-16 from the balance-due print.

**Lessons.** Eight of the 22 F-facts were filled only from the bill's echo of the BOL, and five (F14-F17, F19) cannot be filled by anything in the exhibit. The footer dates live in a garbled text layer and are read by position. Naive-parse traps: the 2025 reprint reads as a $591.10 open balance; the previous weight is printed nowhere; bill 806266163 puts its gross and discount in the description column; the lane is a partner code resolved only through p. 20; the pallet page p. 21 is undated with prices 5.9-6.1% above p. 18.

### 5.2 Chain B: XPO 405-677016 (set 03, Vital Pharmaceuticals). Phases 2 and 3 held; phase 1 absent

What the packet holds: XPO's proof of claim (Form 410, filed 10/13/2022, $14,879.18) with, per PRO, the invoice, the VICS BOL and the delivery receipt. For this PRO: invoice pp. 11-12, BOL p. 13, DR p. 14, all images (the derived text covers only pp. 2-3). No agreement; XPO's rules tariff is held in 2018 and 2026 issues only, so no edition covers 2021.

| ID | Found at | Value | How |
|---|---|---|---|
| P01 | DR p. 14 "PPD" and footer "SUBJECT TO … TARIFF CNWY-199 IN EFFECT ON DATE OF SHIPMENT"; invoice bill-to VPX Sports | payor = shipper | derived |
| P04 | invoice p. 11 "XPO LOGISTICS DISCOUNT SAVES YOU ($468.96)" | 25.0% (468.96 ÷ 1,875.85); **no % printed** | derived |
| P10, P11 | XPO 199-AK.3 (2026) Item 239 $50.70 at +25 lb; 199-AB-4 (2018) Item 239 $27.25 at +50 lb and +$1 | the billed fee $37.25 matches neither edition | fallback, wrong editions |
| P12 | invoice p. 11 "FSC FUEL SURCHARGE 26.00%" | 26.00% of net (365.79 = 0.26 × 1,406.89) | derived from the bill; no table |
| P16, P17 | XPO 199 ¶9 (2018 and 2026) | 180 days from the date of the original bill, both ways | fallback |
| P18 | invoice "PAYMENT IS DUE BY 02/27/2021 … TARIFF 199"; Item 207: 10% min $50 (2026), no % (2018) | billed 1.5% per 30 days (27.15 = 0.015 × 1,809.93), matching neither edition | fallback |
| F01 | BOL p. 13 "Bill of Lading Number:" **blank**; PRO sticker in the carrier box | no BOL number; the key is the PRO | primary location empty |
| F02 | BOL "Date: 2/12/2021"; DR "2/12/21"; invoice "SHIPMENT DATE 02/12/2021" | 02/12/2021 | primary, confirmed twice |
| F03, F04, F05 | BOL p. 13 | VPX Sports, Weston FL → Vitamin Shoppe, Ashland VA; "Prepaid X"; 2 pallets, 88 cases | primary |
| F06 | BOL p. 13 "WEIGHT (LB) 590.48, GRAND TOTAL 590.48" | 590.48 lb | primary |
| F07 | BOL: **no class or NMFC anywhere**; invoice "PLT MISC 0-0 CLASS 100" | the carrier's rating only | fallback (M19) |
| F09 | BOL special instructions blank ("NO BACK ORDER **DO NOT SHIP WITH LESS THAN 9 MONTHS SHELF LIFE" is a shipper note) | nothing requested | primary |
| F12 | invoice p. 12 "2 PLT .SHP … ED PER WEIGHT CERTIFICATE" (partly redacted); DR p. 14 prints 660 | 660 lb asserted; **the certificate is not attached** | fallback; the DR already carries 660, so the reweigh preceded delivery |
| F14 | DR p. 14 handwritten "2/25/21" on the consignee line and "3/2/21" on the driver line | delivered about 02/25/2021, ambiguous | primary, handwriting |
| F15, F16 | DR p. 14 boxes INSIDE / LIFT GATE / RESIDENTIAL / CONSTRUCTION unticked; "Subject To Count" stamp; "DELIVERED 2 PCS" | nothing performed; received, count unverified | primary |
| M03 | invoice "*** BALANCE DUE INVOICE ***" | balance-due | primary |
| M04 | not printed; "PAYMENT IS DUE BY 02/27/2021" → original billed about 02/12/2021 on 15-day terms | the print's own date NOT REPORTED | derived from P18 |
| M07-M16 | invoice pp. 11-12 | 660 lb × $284.22/cwt = 1,875.85; −468.96; net 1,406.89; FSC 26.00% 365.79; CBR REWEIGH OF SHIPMENT FEE 37.25; LP1-LP6 late fees 6 × 27.15 = 162.90; "TOTAL US $1,809.93 PREPAID" | primary; 1,406.89 + 365.79 + 37.25 = 1,809.93: **the total excludes the late-fee lines printed above it** |
| M17 | p. 12 "AMOUNT PAID: US $162.90 / BALANCE DUE: US $1,809.93" | the amount paid equals the six late fees exactly | primary |
| M21 | p. 11 "(continued on next page)", p. 12 "page 9" | 2 pages, complete | primary |
| M25 | DR "ORIGIN NPB, DESTINATION NRM", advance/beyond blank | direct | primary |
| D02, D04 | Form 410 pp. 1-3 | the carrier's claim against the shipper, the reverse direction | primary |

NOT REPORTED: P02, P03, P05-P09, P13's rate table, P19; F08, F10, F11, F17; M23, M24; D05, D06, D08; D07 beyond "AMOUNT PAID".

**Sibling 326-343835 (pp. 19-22).** BOL p. 21 handwritten: weight "1,210.00", "NMFC 072160 CLASS 60" (digits uncertain), special instructions "Appointment needed" and "Call 48 hrs. in advance for delivery appt."; DR p. 22 "APPT 11A 21st", delivered 12/21/2021, boxes unticked. The CORRECTED INVOICE bills 1,425 lb × $131.87 = 1,879.15, −469.79 (25%), net 1,409.36, FSC 30.75% = 433.38, CBR 39.40, APT APPOINTMENT 51.90, LP1-LP5 5 × 29.01 = 145.05, TOTAL 2,079.09, **which here includes the late fees**, and it prints no amount-paid or balance line. "PAYMENT IS DUE BY 12/16/2021" is the original's due date (equal to the ship date).

**Verdicts.** Reweigh 590.48 → 660 lb (+69.52): trigger threshold met under both held editions, the DR already prints 660, but the certificate named in the remark is absent → **ask the reviewer** (and ask XPO for the certificate). Fee $37.25: **not checkable** (2021 edition not held). Linehaul: **matches** arithmetically; rate, discount and fuel level **not checkable**. Late fees: **not checkable** on the rule and moot on this bill. Sibling: APT $51.90 trigger **matches** (requested on the BOL in the carrier's own words; DR records the appointment); its price **not checkable**.

**Lessons.** The class exists only as the carrier's echo; the BOL number box is blank and the PRO sticker is the key; the delivery date is handwriting with two dates. Naive-parse traps: the balance-due print's TOTAL is not the sum of the lines above it (1,972.83 printed, 1,809.93 total) while the corrected invoice sums everything; "PAYMENT IS DUE BY" on a later print is the original's date; "PLT MISC 0-0" looks like an NMFC item but "0-0" is a placeholder; every tariff-priced line on a 2021 bill is unverifiable from a 2018 or a 2026 issue.

### 5.3 Chain C: ODFL 00902527924 (set 19, EDI). Phase 3 as a 210, phase 2 as a 214; phases 1 and 4 absent

What is held: the 210 (`baldr_210_1.edi`, first ST, 25 segments) and four 214 messages for the same PRO (`baldr_214_2.edi`, ST 0001-0004). Parsed with the ISA's own separators (`*`, `~`).

| ID | Found at | Value | How |
|---|---|---|---|
| P01, M06 | 210 B3-04 `PP`; N1*BT | prepaid; bill-to Dalmation Press LLC, Florence AL; **whose pricing applies NOT REPORTED** | who pays is on the bill |
| P03 | 210 L7 | **no tariff named** (L7-02/-03 blank; only L7-07 = 050) | NOT REPORTED; contrast AAA Cooper `L7*1*CZAR*910…20120917`, Estes `L7*2*OVL*DCN` |
| P04, M11 | 210 L1 `DSC` −188.00 | **72.0%, derived**: 188.00 ÷ (650 × 40.17/100 = 261.11) | no % anywhere in the file |
| P12, M13 | 210 L1 code 405, 12.79 | **17.5% of net, derived**: 12.79 ÷ 73.11; on gross it would be 4.9%, implausible | table NOT REPORTED |
| P13, M09 | 210 L1-02/-03 `40.17 PH` | $40.17/cwt as billed | not checkable |
| P21 | 210 L1-04 `26111` | 261.105 → 261.11: half-up rounding; charges in cents | derived |
| F01 | 210 B3-03; 214 B10-02; N9*PO | BOL 00280740007194473; PO 21838107023 | primary; the 214 agrees |
| F02 | 210 B3-12 `20120925`; G62*86; 214 ST 0002 `AT7*AF…20120925*1640*CT` | 2012-09-25, pickup 16:40 CT | three sources agree; the 214 adds the time |
| F03, F05 | 210 N1*SH / N1*CN; L0 `1 PCS`; 214 AT8 | Dalmation Press, Florence AL → C and E Packaging, Roanoke VA; 1 piece | agree |
| F06, F12 | 214 ST 0001 `AT8*G*L*606`; ST 0002-0004 `650`; 210 L0-04 `650` | 606 lb on the estimate message, 650 at pickup and after; **no document says which is declared**; no certificate | fallback; an unremarked change |
| F07, F08, F09 | — | NOT REPORTED | ODFL's 210 has no L5 at all; contrast AAA Cooper `L5*BOOKS, NOI NMFC 161630` |
| F14 | 214 ST 0004 `AT7*D1*NS***20120927*1107*CT` | delivered 2012-09-27 11:07 CT (actual) | primary; the 210's `B3-09 20120927` is coded `B3-10 017` = **estimated** |
| F17 | 214 AT7 events | pickup 16:40, delivery 11:07; no arrival/departure pairs | partial |
| M01, M02 | 210 B3-02; 214 B10-01; B3-11, ISA-06, GS-02 | 00902527924 (11 digits, leading zeros); ODFL; ISA-15 = `T` | normalise; ignore the test flag |
| M03 | — | original, by absence (no B3-08, no prior-bill reference) | derived |
| M04 | 210 B3-06 | 2012-10-15, 20 days after delivery | primary |
| M07, M08, M10, M16 | L7-07 `050`; L0 `650*G`; L1 26111; B3-07 `8590` = L3-05 | 261.11 + 12.79 − 188.00 = 85.90 | primary; reconciles in cents |
| M18, M19 | — | **no free text at all** (no L5, NTE, K1) | NOT REPORTED |
| M21 | SE `25*0001`; GS/GE 5 transactions | complete | counted |
| M23 | 210 B3-09/-10 | 20120927, qualifier 017 | must not be read as actual |
| M25 | 210 R3 `ODFL*O` | origin carrier, no partner | contrast AAA Cooper `R3*NEMF*1*HARRISBURG…12698` |

NOT REPORTED: every P fact but P01/P13/P21; F07-F11, F13, F15, F16, F18, F19; M05 (B3-08 blank, no ITD), M12, M14, M15, M17, M22, M24; all D facts.

**Contrasts (one 210 each).** AAA Cooper 37685697 (`baldr_210_2.edi` ST 0014): BOL in B3-03 and N9*BM; `L5*…LESS 78.00 PCT DISCOUNT` and `Fuel Surcharge 29.00 PCT` as text beside the dollar lines; `L7*1*CZAR*910…060…20120917*0562`; delivery coded 035 (actual); interline `R3*NEMF`, $126.98 of $325.60; 1,147.26 × 0.78 = 894.86 and 252.40 × 0.29 = 73.20 reconcile; ISA-15 = `P`. Estes 2200302174 (`baldr_valid_1_EXLA.edi` ST 60001): **B3-03 = `NS`** (no BOL number; only N9*PO 16720942); `DISCOUNT 84.0%` as text; `L1 298.86 LB`, yet 810 × 298.86/100 = 2,420.77, so it is per cwt; `SUF 24.05` Canadian border fee outside the fuel base (387.32 × 0.29 = 112.32); a group total `ST*980` of 3 bills = 1,218.85.

**Verdicts.** Arithmetic: **matches** on every line. Discount, fuel level, base rate: **not checkable**. The 606 → 650 lb change: **ask the reviewer** (a 7.3% change with no remark and no certificate; the 210 never mentions it). Delivery date for any E1 check: from the 214, never from the 210's estimated date.

**Lessons.** The 214 supplies what the 210 cannot: the actual delivery time, the pickup time, and a second weight that exposes a change. The 210 supplies every money fact, terms and bill-to, invoice date, equipment. Naive-parse traps: B3-09 read as actual; Estes `NS` read as a BOL number; Estes `LB` read as a per-pound rate; searching ODFL's 210 for a percentage or a tariff name; AAA Cooper's PO `21861117002%` carrying a stray character.

### 5.4 Chain D: ODFL 02902161435 (set 21, Winn-Dixie). The one end-to-end chain through phase 4

What the file holds (`winndixie_flmb715964__6929.0.pdf`, no derived text, every page rendered): the BOL (p. 6), the consignee's debit memo (p. 8), its statement and check stub (pp. 9-10), the carrier's e-mails and fax covers (pp. 11-12), ODFL's accounts-receivable history and detail (pp. 13-16), the re-bill (p. 17, two bill pages on one PDF page), and the bankruptcy objection (pp. 1-3). No delivery receipt, no original bill, no pricing agreement.

| ID | Found at | Value | How |
|---|---|---|---|
| P01 | A/R pp. 13, 15 | the same shipment at class 85 was posted at $584.63 on the consignee's account and $1,133.55 on the third party's | inferred: the payor's pricing changed the price; the $584.63 is itemised nowhere |
| P03, P04, P12 | re-bill p. 17 | "TARIFF 559"; "Discount Allowed: 70.00%" $2,299.53; "FUEL INCREASE" 133.04 = 13.5% of net 985.51 | printed %; fuel % derived; editions NOT REPORTED |
| P07 | BOL p. 6 "Over 15 Dens."; re-bill "SW SKID DIMS: 44"X42"X51" EA" | derived density ≈ 11.3 pcf (4 × 44×42×51/1728 = 218.2 ft³; 2,472 ÷ 218.2), **not over 15** | derived |
| P11 | ODFL 100-Q Item 365 (current: $45 in the 10/2026 revision, $40 in 11/2025) | corrected-BOL fee; §3 collect→prepaid needs the shipper's corrected BOL or letter; §5 description changes need "conclusive documentary proof"; §7 third-party billing after pickup | fallback; the 2005 amount ($15) cannot be checked |
| P18 | re-bill p. 17 terms box | 42 days from the due date, then liquidated damages at 135%; due 03/05/05 | primary |
| F01 | BOL p. 6: **no BOL number**; "SHIPPER B/L NUMBER: NS" on the bill; shipper's account number handwritten on the BOL (2904896); PO 550038; packing slip 37658-KSI | the keys are PRO and PO | primary location empty |
| F02, F03 | BOL p. 6; re-bill | 12/3/2004; Kennerley-Spratling, San Leandro CA → Winn-Dixie GM Whse, Jacksonville FL; **ZIP 32254 on the BOL and A/R, 32205 on the re-bill** | agree, except the ZIP |
| F04 | BOL p. 6 | COLLECT box crossed; "BILL THIRD PARTY" struck through; pre-print "PREPAID … UNLESS MARKED COLLECT" | primary; corrected to prepaid third party on 2/18/05 (M18) |
| F05, F06 | BOL p. 6 | 4 pallets, 48 cartons; 2304 lb net / 168 tare / 2472 gross; the bill uses 2,472 | primary |
| F07 | BOL p. 6 "NMFC 156600-3", class 250, "Plastic Articles Over 15 Dens." | declared class 250 | primary; the re-bill rates 085 |
| F08 | re-bill p. 17 | 44×42×51 in × 4, carrier-recorded | fallback (not on the BOL) |
| F13 | re-bill remark | "CBL DGB 2/14/05 CORRECTED BILL OF LADING CHANGE TO ADD COMMODITY DESCRIPTION PER LETTER FROM THE SHIPPER" | a shipper-requested correction, **not an inspection**; "DRP 12/09/04 CORRECT AS BILLED" is the audit of the original rating |
| M01 | BOL label; re-bill; A/R | 02902161435; the A/R prints **2902161435** (leading zero dropped) | normalise |
| M03 | re-bill p. 17 footer "ORIGINAL INVOICE" | **a re-bill**, 77 days after the PRO date, with two CBL remarks and a prior $2,412.67 bill to another payor in the A/R | derived; the title misleads |
| M04 | re-bill "Invoice Date 02/18/05"; the first bill's date not in the file (before the 01/26/2005 debit memo) | first-bill date bounded only | fallback |
| M06-M16 | re-bill p. 17 | bill-to Clamp-Swing Pricing (third party), "Col/Ppd P"; class 085; 2,472 lb; "13289" = $132.89/cwt; gross 3,285.04; 70% = 2,299.53; net 985.51; FUEL INCREASE 133.04; CORRECTED BILL OF LADING CHARGE 15.00; total 1,133.55 | primary; every line recomputed and reconciles |
| M17, M24, D06, D07 | A/R pp. 13-16 | consignee paid $2,412.67 by card 1/27/05; re-rate 2/14 reverses it and posts $584.63; refund $1,828.04 on 2/15/05; 2/18 re-posts $1,133.55 on the third party; refund $584.63 on 2/26/05; lockbox receipt $1,133.55 on 4/11/05; balance .00 | **only in the carrier's A/R history, which the vendor obtained by fax**; the re-bill is silent on all of it. 1,828.04 + 584.63 = 2,412.67 |
| M18, M19 | re-bill p. 17 | the three remark lines above, plus "C/ADDITIONAL REDUCTION, ALLOWANCE OR ADJUSTMENT MAY APPLY"; description echo "NMFC #156600 S7 92.5 / OVER 15 DENS" **against a class column of 085** | primary |
| M21 | re-bill | "Page 1 of 2" and "Page 2 of 2" on one PDF page; the total only on page 2 | primary |
| D02-D05 | vendor's memo to the shipper p. 7; ODFL e-mail p. 11 ("did receive the full refund … now billing to you for $1133.55"); claim amendment p. 3 (+2,412.67); objection pp. 1-2 | a payor correction and a bankruptcy claim, not a Part 378 claim; both corrections accepted by the carrier | primary |
| D08 | A/R p. 13, the vendor's handwritten "1. Initial payment … 2a. Partial refund … 2b. Remaining balance refund" | the vendor's own log | primary |

NOT REPORTED: P02, P05, P06, P08-P10, P13's table, P16, P17, P19, P20; F09-F12, F14-F18; M05 beyond the due date, M12, M22, M23.

**Add-on, Paper-Pak 14710702037 (`paperpak_odfl_ilnd220449__10.0.pdf` pp. 13-14, statement p. 7).** The bill prints "BILLED WT 2601LBS REWEIGHED WT 3215LBS", "WIW", and "CAB REG 11/19/07 CORRECT AS BILLED" (an audit stamp 52 days after shipment, not a reweigh reason); class 050, 32.15 cwt × $58.47 = 1,879.81, 70% = 1,315.87, fuel 126.89 = 22.5% of 563.94, "CALL 72HRS IN ADV FOR DEL APPT" 7.50, total 698.33. At the billed 2,601 lb the bill would be 566.39, so the reweigh added $131.94; no certificate. The rotated statement of 5/25/08 shows freight 698.33, net cash posted 662.90, remaining 35.43: a short-pay that no document in the file explains.

**Verdicts.** The wrong-payer sequence (A5): every A/R balance reconciles; the carrier was paid once ($1,133.55), and the vendor's loss is the consignee's un-reversed debit memo, a receivable against its own customer, not a carrier overcharge. The re-bill's lines: gross, discount $, fuel $, total **match**; 70%, 13.5% and $132.89 **not checkable**. Class 250 → 085: **ask the reviewer**: a corrected BOL at the shipper's request, whose proof letter is not in the file, with the bill's own description still reading "S7 92.5" and the printed dimensions giving about 11.3 pcf against the BOL's "Over 15 Dens.". The $15 CBL fee: **ask the reviewer** (Item 365 supports the charge in principle; one fee for two corrections is favourable; the 2005 amount is unverifiable). Paper-Pak's $35.43 short-pay: an open balance to show, not to guess.

**Lessons.** M03 cannot be read from the title; it is derived from the invoice date against the PRO date, the remark block and the A/R. M17 and M22 do not exist on the re-bill at all; they live only in the carrier's own receivable history. The PRO loses its leading zero in the carrier's system; the BOL has no number, so PRO + PO are the keys; the consignee ZIP differs between documents.

### 5.5 Chain E: three claims against Yellow (set 23). Phase 4 in isolation

What the packets hold: (N) a freight-audit firm's overcharge claim statement (p. 4) and Yellow's status printout (p. 5); (G1) a 3PL's reweigh dispute letter (p. 4), the BOL (p. 5), an inventory (pp. 6-7) and the shipper's weight certificate (p. 8); (G2) a 3PL's appeal quoting the carrier's decline (p. 5) and the BOL (p. 4). Each sits behind a bankruptcy proof-of-claim form (pp. 1-3). No carrier bill in any packet; no Yellow pricing document; no Yellow rules tariff in `data/`.

| ID | Found at | Value | How |
|---|---|---|---|
| P10 | G2 p. 5, as quoted by the claimant | "declined per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse" | the item number and the carrier's reading come only through the claimant; the item's wording NOT REPORTED |
| P16 | YRC form F-154 p. 1 (set 16) | "Overcharge claims must be filed within 180 days of pickup … We will acknowledge claims within 30 days of receipt" | fallback to the carrier's public form; no packet states a window |
| F01 | G1 p. 5 "GTZ BOL NO : 27205339", "PU# KKFA0871883" (= the certificate's "GBL NO"); G2 "26665544" | the military GBL number is the join between BOL and certificate | primary; N has no BOL at all |
| F02 | N p. 4 "Ship Date 09/20/2022"; G1 "07/03/2023"; G2 "04/03/2023" | N's date is the claim's echo, not a BOL | primary / fallback |
| F03, F04 | G1 p. 5; G2 p. 4 | mover to mover (Mountain Home ID → Fayetteville NC; Wrightstown NJ → El Paso TX); "All charges prepaid to: GlobalTranz" | primary; the certificate gives the customer's destination as a different town (Autryville NC) |
| F05 | G1 p. 5 "Units 0 Pieces 2" | a naive parse reads zero handling units | primary |
| F06, F08 | G1 p. 5 "2153 lbs", "87 In 45 In 87 In"; certificate p. 8: 84×45×87 per crate, 190.31 ft³ each, 380.63 total, tare 636 / gross 2,153 / net 1,517, "Density: 3.99" | BOL weight = the certificate's **gross**; the printed density is net ÷ cube (1,517 ÷ 380.62 = 3.99); on gross it is **5.66**; BOL length 87 vs certificate 84 | primary; recomputed |
| F07 | G1, G2 BOLs | class 150, NMFC 100240-1, household goods | primary |
| F12 | — | **the carrier's reweighed weight appears nowhere**; the letter says only that a re-weigh "was added" | NOT REPORTED; the shipper's certificate is counter-evidence, not the carrier's reading |
| F15, F19 | G2 p. 5 | claimant: "commercial warehouse … unloaded … via forklift", with a satellite image; carrier (quoted): "listed as a Self-Storage Warehouse"; the site is the **shipper's** address (a pickup charge) | contested; both sides second-hand |
| M01 | N p. 4 "689201498" and "6892014980"; G1 "6703485626"; G2 "6647373549" | N's two PROs are one bill keyed twice (the 9-digit is the 10-digit minus its last digit) | normalise |
| M02 | "Mail To : YRC (ROADWAY)"; BOL "Carrier: YRC"; debtor "YRC Inc." / "Yellow Corporation" | one carrier, three spellings | — |
| M14 | G2 p. 2 + p. 5; G1 p. 2 + p. 4 | limited access $75.00; reweigh $382.08 | derived: the accessorial amount is only the proof-of-claim's item 7 |
| M16, M17 | N p. 4 | "Billed Amount 612.77" twice; "Total Paid : 1225.54", "Correct Amount : 612.77", "Overcharge Amount : 612.77" | from the claim statement, not a bill |
| M20 | N pp. 2, 4, 5; G2 p. 5 | claimant number "SATCO-2300008OC" (printed "SATCO2300008OC" on the court form); carrier claim 23009972; draft 1385879; G2 "YRC Claim # 23023786" | the claimant's number is the join across claim, status page and court form, and loses its hyphen |
| D01 | derived from F-154 + F02 | N: 180 days from 09/20/2022 = 2023-03-19; the claim is dated 03/28/2023, **day 189**; G1 filed day 129; G2's original claim date NOT REPORTED | derived |
| D02 | N p. 4; G1 p. 4; G2 p. 5 | N carries claimant, own claim number, ship date, PROs, billed / paid / correct / overcharge, "Duplicate Bill … Keying error resulted in duplicate payment", "Date Submitted 03/28/2023"; "Claim Tariff Contract Authority:" **blank**. The 3PL letters carry PRO, BOL, nature, **no amount and no date**; the court form supplies the amount | only N is a full D02 |
| D03 | N p. 4; G1 pp. 5-8; G2 pp. 4-5 | N: "Attached Documentation" boxes all unticked, indemnity clause printed; G1: BOL, inventory, certificate "WEIGHED ON CERTIFIED SCALE"; G2: BOL, satellite image | primary |
| D04 | N "Date Submitted 03/28/2023", status page "Date Received: 03/28/23"; court filings 11/09/2023 (G1), 11/08/2023 (G2) | acknowledgement date NOT REPORTED in all three | primary |
| D05 | N p. 5 "This claim is in APPROVED status … approved for disbursement"; G2 declined, reason quoted; G1 unresolved | **the decision date is not printed** on Yellow's page: it prints "Date Received", "Draft Date" and the date the audit report "was sent" (06/20/23) | primary |
| D06 | N p. 5 | "Draft Number 1385879", "Draft Amount 612.77", "Draft Date 06/20/23"; whether the draft was issued or cashed NOT REPORTED, and the proof of claim for the same $612.77 says it was not | primary |
| D07 | N p. 4 | "Paid Amount 612.77" twice; dates, check numbers, payee NOT REPORTED (the form asks for "photocopies of canceled drafts or checks"; none attached) | amounts only |

NOT REPORTED: all P facts but P10/P16; F11, F13, F14, F16, F17; every M fact but M01, M02, M14, M16, M17, M20; D05's date and reason (N), D06 (G1, G2), D08 (G1, G2).

**Clocks.** Ship 09/20/2022 → claim 03/28/2023 = 189 days, nine past the form's "180 days of pickup", yet approved. Received 03/28/23 → draft 06/20/23 = **84 days**, past 378.8's 60; the 30-day acknowledgement cannot be checked because no acknowledgement date is printed.

**Verdicts.** N, duplicate payment (A2): two PRO strings normalise to one; paid twice; 1,225.54 − 612.77 = 612.77 → **flag** (the bills themselves are absent, so strictly "flag, bill not held"). G1, reweigh (C1): the carrier's weight NOT REPORTED, so the dollars are **not checkable**; what the reviewer can be shown is that the certificate's gross equals the BOL, the 84-vs-87-in mismatch (3.5% more cube on the BOL), and 5.66 pcf on gross against 3.99 printed on net. G2, limited access (D2): price $75.00 (derived); trigger contested; the item's wording NOT REPORTED → **ask the reviewer**.

**Lessons.** What a real claim carries: N carries D02, D03 (as unticked boxes), D04 (submitted), D07 (amounts only) and D08; the 3PL letters carry D02 without amount or date, and D03. What a real answer carries: D05 as a status word, D06 (draft number, amount, date), D04 (received), and both parties' claim numbers. **What a stand-alone answer never carries:** the decision date, the decision reason, the acknowledgement date, the PRO, the bill, proof that the draft cleared, the paid-against-should-be arithmetic. The G2 decline exists only as the claimant's quotation; the carrier's own words never reached the record. The Epiq register lists both GlobalTranz claims at $0.00 while the forms print $382.08 and $75.00 (`source.md` carries the register's figure).

### 5.6 Chain F: Taylor truckload, load 1071942 (set 22). The TL packet; no dispute stage

What the file holds (`stg_taylor_10401__claim.pdf`): the carrier's proof of claim for three unpaid loads ($2,950.00, p. 2); for this load the invoice (p. 4), the BOL (p. 5, image), the rate confirmation (pp. 6-8). The "in and out times must be marked on the bills by the receiver" rule sits on **p. 20**, the 2023 rate confirmation for the third load, not on this load's.

| ID | Found at | Value | How |
|---|---|---|---|
| P01, P02 | rate con pp. 6, 8 | a broker-to-carrier confirmation, "an addendum" to a Carrier Contract not held; "Load Number: 1071942", dated 02/23/2026 | primary; the master contract NOT REPORTED |
| P08, P09, P14 | rate con p. 8; p. 6 | "Net Freight Charges USD 1,150.00", "includes all stop-off charges, fuel surcharges, out of route, tolls, storage, and/or all arbitrary charges"; "Distance (Miles): 335.15" | primary: an all-in price; the invoice's split into flat + fuel is the carrier's own; the mileage basis NOT REPORTED |
| P15 | rate con pp. 7-8 (p. 20 for the 2023 load) | detention: "submit a Pepsi Detention Form with bills & driver logs within 2 business days"; "detention, layover or lumper reimbursement … within 48 hours of delivery"; TONU "same day"; p. 8: "Reimbursement pertaining to any accessorial charges must be reported within 24 hours of delivery"; lumper reimbursed with receipt, $15 comcheck fee; "$200 fee for early or late arrivals" (club stores); p. 20: "IN AND OUT TIMES MUST BE MARKED ON THE BILLS BY THE RECEIVER: FAILURE TO DO SO WILL RESULT IN NO DETENTION" | evidence rules present; free time, hourly rate and cap NOT REPORTED; **48 hours on p. 7 and 24 hours on p. 8 for the same request** |
| P16, P17 | rate con p. 8 | invoices "more than FORTY-FIVE (45) days after DELIVERED services" not accepted; non-payment inquiries after 45 days from due not investigated | carrier-side clocks; the shipper's window NOT REPORTED |
| P18 | invoice p. 4 "Terms are 15 Days from Receipt of Invoice"; broker p. 9 "30-DAY TERM" with quick-pay discounts | carrier 15 days vs broker 30 | conflict |
| F01 | BOL p. 5 "Bol Number 4505279147", "SID#76930091"; rate con "PO Number: 4505279147", "**Bill of Lading Number: 76930091**"; invoice "REF 1071942" | **the rate con's BOL field holds the SID and its PO field holds the BOL number** | primary; join-key trap |
| F02, F14 | BOL, invoice, rate con | shipped 02/23/2026; delivered 02/24/2026 (invoice; BOL receiver date handwritten); time NOT REPORTED | agree |
| F03 | BOL site codes "US-PL-URBANDALE-IA-OUT" → "US-DC-ELK GROVE VILLAGE-IL-SC DC"; invoice customer codes PEPURB01 / PEPELK | the same two sites under three naming schemes | — |
| F04 | BOL "THIRD PARTY FREIGHT CHARGES BILL TO: Pepsi Beverages Company C/O Cass Information Systems"; invoice "Bill To: BEST DEDICATED SOLUTIONS" | **the BOL's bill-to is the shipper's payment agent for the shipper-broker bill; the carrier bills the broker** | primary |
| F05, F06 | BOL "#PKGS 20", 19 + 1 handling units, 1,886 cases, 44,122 lb (42,653 + 1,469); rate con "Handling Unit Qty 0 … Package Qty 1892", 43,529 lb; invoice 43,529 | three counts; the carrier echoed the tender, not the BOL; 593 lb apart | — |
| F07, M07 | BOL NMFC/class blank ("LTL ONLY"); invoice column "FREIGHT CLASS" prints "**Van**" | the class column holds the equipment type | trap |
| F09, F11 | rate con p. 7 | "Appointment Required: Yes", pickup 12:00, delivery 09:00, seal and food-grade rules; an appointment, not a guarantee | primary |
| F16 | BOL p. 5 | receiver and shipper signatures with dates; "Trailer Loaded: By Shipper", "Freight Counted: By Shipper" | names not transcribed |
| F17 | — | no in/out times on the BOL; none claimed | NOT REPORTED |
| F20 | rate con pp. 6-7; invoice | load 1071942; 2 stops; 335.15 miles; "Equipment Type: 53 V"; invoice "332/332" | two mileages |
| F21 | — | the shipper-broker price is in no document | NOT REPORTED, structurally |
| M01-M05 | invoice p. 4 | "PRO. NO. 1848869A" (letter suffix); Taylor Truck Line, Northfield MN; "CUSTOMER COPY"; "INVOICE DATE 02/26/2026"; no due date printed (15 days from an unknown receipt) | primary |
| M09, M13, M16 | invoice p. 4 | "FLAT RATE … $993.96"; "FUEL SURCHARGE $/MILE 332 Miles .47 $/Mile $156.04"; "Total: $1,150.00" | 993.96 + 156.04 = 1,150.00; at 335.15 miles fuel would be 157.52 |
| M17 | proof of claim p. 2 | $2,950.00 = 1,150.00 + 900.00 (p. 10) + 900.00 (p. 15: 673.05 + 445 × .51) | derived; the invoice prints no balance |
| M19, M20 | invoice | "Remarks: LOAD BARS/STRAPS** CHECK IN as Best Dedicated Solutions**"; "TRACTOR 1019 TRAILER 61336" (the trailer joins invoice and BOL) | echo of the rate con |
| D01, D02, D04 | rate con p. 8; proof of claim pp. 1-2 | invoice by delivered + 45 = 2026-04-10; filed 03/12/2026, 16 days after delivery; a non-payment claim, so no should-be figure | derived / primary |

NOT REPORTED: P20, P21 beyond the exact $/mile; F08, F10, F15 beyond handwritten trailer and seal numbers, F22; M14, M15, M18, M22, M24; D05-D08.

**Verdicts.** B6: expected = the rate con's all-in $1,150.00; billed $1,150.00 → **matches**. The invoice's split is cosmetic and back-solved (1,150.00 − 156.04 = 993.96 exactly); a line-by-line fuel check at the rate con's 335.15 miles would wrongly **flag** $1.48. The mileage basis NOT REPORTED, so per-mile fuel is **not checkable**, and the all-in clause makes it moot. Detention: nothing billed; had a line appeared, F17 absent plus the rate con's own evidence rule = **ask the reviewer**.

**Lessons.** Found only by derivation: the due date, the three-load sum, the mileage discrepancy, the flat rate as a residual. Naive-parse traps: the rate con's BOL and PO fields swapped; the invoice's class column holding "Van"; the BOL's third-party bill-to being the shipper's agent, not the carrier's customer; "Handling Unit Qty 0"; two filing windows (48 h and 24 h) inside one rate con; the carrier's 15-day terms against the broker's 30-day term. A carrier's packet can verify what the **broker** owes the carrier, never what the **shipper** was charged.

### 5.7 Coverage: what each chain could and could not supply

Phase coverage (a phase counts as held when its deciding document is in the chain, not merely echoed):

| Chain | 1 Price | 2 Facts | 3 Money | 4 Dispute |
|---|---|---|---|---|
| A SEFL (set 02) | **held** (agreement, 3 versions; tariff) | absent (echo on the bill only) | held (balance-due + reprint) | held (worksheet, complaint); no carrier answer |
| B XPO (set 03) | absent (tariff named; no edition for 2021) | **held** (BOL, DR); no certificate | held (balance-due; corrected) | carrier's claim only |
| C ODFL EDI (set 19) | absent | partial (214: times, weights) | **held** (210) | absent |
| D ODFL Winn-Dixie (set 21) | absent (tariff number only) | partial (BOL; no DR) | held (re-bill; A/R history) | **held** (letters, refunds, re-bill, claim) |
| E Yellow claims (set 23) | absent | partial (BOL, shipper's certificate) | absent (no bill) | **held** (claim, answer, decline) |
| F Taylor TL (set 22) | **held** (rate con) | held (BOL) | held (invoice) | carrier's claim only |

Facts by outcome across the six chains (must-have facts only):

| Outcome | Facts |
|---|---|
| Found at the primary location in every chain that had the document | M01, M02, M07-M10, M16 (the bill always carries its own money); F02; F03 |
| Found only by fallback or derivation somewhere | M04 (first bill date: derived from due date on XPO; bounded on SEFL and ODFL), M11 and M13 (% derived on ODFL's 210 and XPO's PDF), M17 (derived on SEFL; from the A/R on ODFL), F06 original weight (derived on SEFL 806625953), F07 (echo only on XPO and SEFL), F12 (bill line only; certificate absent in every chain that had a reweigh), F14 (214, handwriting, or TL invoice), P04/P12 (from the bill when the agreement is absent) |
| NOT REPORTED in every chain | **F17 arrival/departure times; F19 premises type as a fact; M18 in machine form (no 210 carries it); the carrier's certificate behind any reweigh (A sibling, B, C, D add-on, E); D05's decision date; the fuel table for the ship week; the base rate; the agreement outside set 02 and the rate con outside set 22** |
| Present in one chain only | the agreement's lane rows (A); a typed delivery time (C, from the 214); the carrier's A/R history (D); a carrier's written decision (E, as a status word and a quoted decline) |

Three things the walks settled that the field maps had only argued: (1) the bill's echo of the BOL is a real fallback for F01-F05, F07, F09 and F10, and the only one when the BOL is lost; (2) the carrier's certificate was absent in **every** reweigh seen (five bills across four sets), so F12's primary location is in practice always a request to the carrier; (3) the first bill date is printed on none of the LTL correction prints walked, so D01 is normally computed from a bound.

## 6. What the walks say about the standardised flow

The founders' goal is a flow that knows where to look next instead of parsing naively. The walks turn that into five rules [our call]:

1. **One fact, one ordered list of places, and the list stops at a named party.** §2 is that list. When the primary and every fallback are empty, the output is not "unknown" but "NOT REPORTED: [fact]; held by [customer / carrier / nobody]", which is the request the reviewer sends. The same fact can stop at different parties on different carriers (the certificate: a free copy at FedEx, a paid service elsewhere).
2. **Read by position and by key, not by label.** SEFL's footer labels are garbage in the text layer but the values sit in a fixed order; XPO's balance-due total sits below lines it excludes; ODFL's re-bill carries "ORIGINAL INVOICE" in its footer. The parser's unit of work is the bill grouped by PRO, with each print a dated event, and the fields read from their known positions on that carrier's layout.
3. **Every derived number is labelled derived and shown with its formula.** Discount and fuel percentages (ODFL, XPO), the original total and weight on a correction (SEFL), the amount paid (XPO), the first bill date (a bound), the TL flat rate as a residual (Taylor). The reviewer sees "2,430 lb, derived from the worksheet's $744.77", never "2,430 lb".
4. **Test the unit before trusting the field.** "60080" is $600.80/cwt because 5.09 × 600.80 = 3,058.07; Estes "LB" is per cwt because 8.10 × 298.86 = 2,420.77; Taylor's "FREIGHT CLASS Van" is an equipment type; XPO's "0-0" is a placeholder, not an NMFC sub; "Units 0" on a 3PL BOL is not zero handling units.
5. **Per-carrier layouts, one shared pipeline.** What is shared: the 210 skeleton, the VICS form, the NMFC, Part 378, the 180-day windows. What is per carrier and must be profiled once: the PDF layout and which dates it prints, the 210 charge mapping (text % at AAA Cooper and Estes, dollars only at ODFL), the correction shape (difference only at SEFL; old and new at ABF; paid and balance at XPO; both weights at TForce; a new payer under the old PRO at ODFL), the claim window's start date, the definition of a residence, and the claim channel.

Where naive parsing would have failed in the six chains, in one list: SEFL's garbled footer; the 2025 reprint read as an open $591.10; the previous weight printed nowhere; gross and discount in SEFL's description column; the partner-code lane (WCPC) resolved only through a definitions page; XPO's total excluding the late fees printed above it while the corrected invoice includes them; "PAYMENT IS DUE BY" on a later print being the original's date; ODFL's 210 delivery date coded estimated; Estes `NS` as a BOL number and `LB` as a per-pound rate; ODFL's re-bill titled ORIGINAL INVOICE; the PRO losing its leading zero in the carrier's A/R; the consignee ZIP differing between BOL and bill; the 3PL's two PRO strings for one bill; the Epiq register's $0.00; the rate con's BOL and PO fields swapped; the BOL's third-party bill-to being the shipper's agent; "Handling Unit Qty 0"; two filing windows inside one rate con.

## 7. Open points for the founders

Nothing here is decided. The points the walks raise:

1. **Carrier-owed NOT REPORTED on a carrier-added charge: auto-flag or ask the reviewer?** §4.6 proposes a flag with the certificate requested. The alternative is to show it as "unsupported, awaiting the carrier" and let the reviewer decide whether to file. The clock does not wait either way.
2. **Protective claims.** Because nothing pauses the 180 days (§4.5), a line with proof outstanding has to be filed before the deadline or lost. Whether the software should recommend filing on a bound (the earliest print date) when the first bill date is NOT REPORTED is a policy choice.
3. **Tolerances** are still unset (`software-initial-pitch.md` §6). The walks give two data points: a $1.48 fuel difference that is a mileage-basis artefact on an all-in TL rate (should not flag), and a $35.43 short-pay that nothing explains (should show as open, not as an error).
4. **Editions in force.** Every tariff-priced line on a 2021 XPO bill and a 2005 ODFL bill was unverifiable from the editions held, as the AX review found for ABF's 2024 bills. The prototype needs the item in force on the ship date, which means asking carriers for old issues or accepting "not checkable" on old bills during a look-back.
5. **PACER purchases** that would close the phase-2 gap in set 02 (the Exist filings after Doc 1, listed in `doc-explanation.md` §3) are cheap; the only reason to hold off is the rule against logins in research sessions.
6. **Catalogue notes, not applied:** `data/sources/23_overcharge_claims_vs_yellow/source.md` lists the GlobalTranz claims 16595 and 16215 at $0.00 (the Epiq register's figure); the forms' item 7 prints $382.08 and $75.00. Changing it needs a catalogue pass.
7. **Corrections applied today to `doc-explanation.md`** (founders' choice, 2026-10-10): §1.2 on what evidence overturns a reweigh or reclass; §4.5 step 1 on the carrier's punitive default class and no-weight fees. And in `research/s5_check_AX_adversarial.md`: the NMFC claim items (300300-300530) are held in `nmfc_100-AO_supplement1_2015`, not missing.

## 8. Claim ledger

Every number or quotation above that sets a verdict or a rule, with its source and tag. *verified* = re-opened at the source during this session (by the walk agent, or by the coordinator where marked C); *assumed* = read by an agent from a file not re-opened, or an inference.

| # | Claim | Tag | Source |
|---|---|---|---|
| 1 | SEFL 807148067: 509 lb × $600.80/cwt = 3,058.07; 88.15% = 2,695.69; net 362.38; liftgate 55; residential 94; fuel 22.00% = 79.72; total 591.10; PAY THIS AMOUNT 94.00; "PER GOOGLE EARTH THIS IS A PRA DLVY"; B/L 51124115; shipped 05/15/2023; billed 06/19/2023; due 07/04/2023; quote CWEN3E465; "1 of 1" | *verified* (C: p. 46 rendered) | 02-002 p. 46 |
| 2 | Item 753: $7.60/cwt, $94 min, $575 max, eff. December 16, 2022; "will not relieve" | *verified* (C: text l. 2669-2686) | 13-065 |
| 3 | 509 × 7.60/100 = 38.68 → 94; 8,920 × 7.60/100 = 677.92 → 575 | *verified* (C: calc) | — |
| 4 | Agreement versions 01/15/2021, 06/08/2022, 04/12/2023; WCPC 88.15%; OR floor $152; liftgate exception $55 eff. 4/7/2021; no residential exception | *verified* | 02-002 pp. 12-22 (AX §2.1 and the walk) |
| 5 | 806625953: 2,720 lb billed, 2,430 derived, no remark; PAY 110.23 on 1,088.74 | *verified* (C: calc 744.77 ÷ 0.097 ÷ 315.97 = 2,430; 8,594.39 × 0.903 = 7,760.73) | 02-002 p. 41 |
| 6 | 806266163 cube line and figures | *assumed* (agent read; not re-opened) | 02-002 p. 94 |
| 7 | SEFL 1090 has no overcharge-claim item | *verified* | 13-065 (AX §6; walk text search) |
| 8 | XPO 405-677016: 660 lb × 284.22 = 1,875.85; −468.96 (25%); FSC 26% = 365.79; CBR 37.25; TOTAL 1,809.93; AMOUNT PAID 162.90; BALANCE DUE 1,809.93; "…ED PER WEIGHT CERTIFICATE"; due 02/27/2021 | *verified* (C: p. 12 rendered; calc) | 03-003 pp. 11-12 |
| 9 | XPO BOL 590.48 lb, BOL number blank, prepaid, no class; DR handwritten 2/25/21 and 3/2/21, boxes unticked | *assumed* (agent render) | 03-003 pp. 13-14 |
| 10 | XPO 326-343835 figures and "Appointment needed" | *assumed* (agent render) | 03-003 pp. 19-22 |
| 11 | XPO Item 239: $27.25 at +50 lb (2018), $50.70 at +25 lb (2026); Item 207 10% min $50 (2026) | *assumed* (agent read) | 13 xpo_cnwy_199-AB-4, -AK.3 |
| 12 | ODFL 210 ST 1: B3 `00902527924`, `PP`, `20121015`, `8590`, `20120927*017`, `20120925`; 214 D1 `20120927*1107*CT`; AT8 606 then 650 | *verified* (C: grep) | 19-001, 19-017 |
| 13 | 72.0% and 17.5% derived; 261.11 + 12.79 − 188.00 = 85.90 | *verified* (C: calc) | — |
| 14 | AAA Cooper and Estes contrast values | *assumed* (agent parse; consistent with AV §2.1) | 19-009, 19-015 |
| 15 | Winn-Dixie: BOL collect, 2,472 lb gross, class 250, NMFC 156600-3, 12/3/2004; re-bill 02/18/05 titled ORIGINAL INVOICE, class 085, 132.89, 70%, fuel 133.04, CBL 15.00, total 1,133.55, three remark lines | *assumed* (agent render; arithmetic C-verified: 24.72 × 132.89 = 3,285.04; × 0.7 = 2,299.53; 133.04 ÷ 985.51 = 13.5%) | 21-002 pp. 6, 17 |
| 16 | A/R history: 1,133.55 lockbox 4/11/05; 584.63 refund 2/26/05; 584.63 and 1,133.55 postings 2/18/05; 1,828.04 refund 2/15/05; 2,412.67 paid 1/27/05 | *verified* (C: p. 15 rendered shows the first four; p. 13 per agent) | 21-002 pp. 13-16 |
| 17 | 1,828.04 + 584.63 = 2,412.67 | *verified* (C: calc) | — |
| 18 | ODFL Item 365: $45 (10/2026), $40 (11/2025); §§3, 5, 7 | *assumed* (agent read) | 13-053 |
| 19 | Paper-Pak bill and statement figures | *assumed* (agent render) | 21-001 pp. 7, 13-14 |
| 20 | Yellow N: claim 03/28/2023, ship 09/20/2022, draft 06/20/23, $612.77 ×2; APPROVED; no decision date | *verified* dates and arithmetic (C: 84 and 189 days) ; page content *assumed* (agent render; matches AX §6) | 23-006 pp. 4-5 |
| 21 | GlobalTranz 16595: BOL 2,153 lb, 87×45×87; certificate 84×45×87, 380.63 ft³, net 1,517, density 3.99; gross density 5.66; claim $382.08 | *assumed* (agent render; arithmetic consistent with AW claim 20) | 23-004 pp. 2, 5, 8 |
| 22 | GlobalTranz 16215 decline wording; claim $75.00 | *assumed* (agent render; wording matches AX §7) | 23-003 pp. 2, 5 |
| 23 | YRC form: 180 days of pickup; acknowledge within 30 days | *verified* | 16-095 (AX §6) |
| 24 | Taylor: flat 993.96 + 332 × .47 = 156.04 = 1,150.00; rate con all-in 1,150.00; 335.15 miles → 157.52; BOL 44,122 lb vs 43,529; rate con "Bill of Lading Number: 76930091" = SID, "PO Number: 4505279147" = BOL; "FREIGHT CLASS Van"; 48-h (p. 7) and 24-h (p. 8) rules; in/out-times rule on p. 20 | *verified* arithmetic (C); page content *assumed* (agent read of the text layer and p. 5 render; consistent with AV, AW claims 23, 31) | 22-012 pp. 2, 4-8, 20 |
| 25 | NMFC 250100-A §4 "actual gross weight"; Uniform BOL §7(d) "articles actually shipped" | *verified* (C: grep) | 15-079 l. 1695; 15-077 l. 54 |
| 26 | ABF 992 ¶4 "no weight whatsoever"; ABF 428 "within 180 days of the initial shipment date" | *verified* (C: grep) | 13-047 l. 5630, 1917 |
| 27 | Estes 993 "without stating the shipment weight"; Estes 170 class 175; Estes 751/751-10 "will not relieve" | *verified* (C: grep) | 13-049 l. 4333, 484, 3383, 3498 |
| 28 | SEFL 170 class 150 default; Note 3 proof definition; 360-5 §5 and §6 | *verified* (C: grep) | 13-065 l. 331-342, 349, 545-549 |
| 29 | XPO 26.3 class 150; 205 thirty days; 23(5) 180 days from the date of the original bill | *verified* (C: grep) | 13 xpo_cnwy_199-AK.1 l. 1010, 1470, 840 |
| 30 | TForce "not to exceed a class 250"; "regardless of a shipper's designation" | *verified* (C: grep) | 13-060 l. 1404, 2856 |
| 31 | TForce dimension default 120×96×96 and refusal after tender; FedEx 360 ¶6 and TForce 361-A prepaid default | *assumed* (agent read; not re-opened) | 13-060, 13-051 |
| 32 | FedEx 980 ¶2 copy of the weight verification on request; FedEx 438 "receipt of the original invoice plus 7 days" | *verified* (C: grep) | 13-051 series b l. 3348, 1378 |
| 33 | Saia 1030(5) "Except for the revocation of discounts" | *verified* (C: grep) | 13-056 l. 7796 |
| 34 | ODFL 396 ¶2 closed 30 days after ruling; ODFL verification fee wording | *verified* (C: grep) | 13-053 l. 1297/1306, 727/736 |
| 35 | ODFL 367, 365; Central 400(b), 460; AAA Cooper 660, 970; Werner 585; USA Truck 17; Saia 850; Dayton 1015; R+L 364; Estes 360-03, 992 ¶4; HB44 paid-certificate prices (SEFL 992, ABF 992 ¶5, TForce 990, FedEx 990) | *verified* by the exploration agent; *assumed* at coordinator level (not re-opened) | set 13 |
| 36 | NMFC 300520(g) "5 business days"; 300330(d)/300340(c); 300300-300530 held in the 2015 edition | *verified* (C: grep l. 1126, 1148, 1257) | 15-079 (`nmfc_100-AO_supplement1_2015`) |
| 37 | Part 378.3, .4(a)-(e), .5(c), .7, .8, .9(b) | *verified* (AX §7, eCFR 2026-09-01; re-fetched by the AX review) | eCFR |
| 38 | *Southern Furniture*: 13710(a)(3)(A)/(B) wording; "not optional"; notice requirement (STB quotation) | *verified* (C: grep l. 299-307, 366-370, 441) | 08-024 |
| 39 | *PJAX*: "applies only to actions initiated by shippers"; "absence of a notation on a delivery receipt" | *verified* (C: grep l. 128, 342) | 20-003 (CBCA 552-RATE) |
| 40 | XPO claim page: "rejected and sent back"; "only after the invoice has been paid" | *verified* (C: grep l. 22, 28) | 16-083 |
| 41 | Home Depot §8: "not presented within ninety (90) days" | *verified* (C: grep l. 1218) | 23-005 |
| 42 | First Brands §13-14; Walmart 12 months | *verified* (AX §6; Walmart via AX's OCR) | 11-037; 23-012 |
| 43 | HB44: "available upon request" retained "at least 30 calendar days after the date of invoicing" | *verified* (C: grep l. 209-230) | 15-078 |
| 44 | Broker windows 5-30 days | *verified* | AM §AM4.3 |
| 45 | NMFC 401400-A destination carrier's weight governs on interline | *assumed* (agent read) | 15-079 p. 23 |
| 46 | Epiq register $0.00 vs forms $382.08 and $75.00 | *assumed* (agent render) | 23-003, 23-004 p. 2; `source.md` |
| 47 | The §2 lookup order and the §4.6 decision table | [our call] | — |
