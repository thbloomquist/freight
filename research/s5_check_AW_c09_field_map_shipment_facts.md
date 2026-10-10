# Check AW · Field map, slice 2: the documents that record what physically happened

*Reviewed 2026-10-10: `research/s5_check_AW_adversarial.md` (ledger 28 kept verified, 2 kept assumed, 4 narrowed, 0 discarded). The corrections are applied in `data/doc-explanation.md`; this file is kept as written. Main ones: 43 weight-certificate and 6 inspection-certificate pages in set 04 (page-level count); 27 ABF quote-difference notes, 21 naming a lumper; tariff reweigh thresholds mostly set the fee, not the correction.*

Written 2026-10-10 for the C-09 prototype. One of three field-map slices. This slice covers the documents the bill is checked *against*: bills of lading (BOL), delivery receipts (DR, also called proof of delivery or POD), weight and inspection (W&I) records, EDI 214 status and 204 tender messages, rate quotes, and truckload (TL) rate confirmations. Public files in `data/` only; no web fetches were needed. Individuals' names, signatures and phone numbers appear on many of these pages; none is transcribed here, and no street address of a possible private home is given.

Terms: **PRO** = the carrier's shipment and bill number. **Reweigh / reclass** = the carrier changes the weight or the freight class after pickup. **Density** = pounds per cubic foot (pcf); many NMFC items set the class by density. **Hexahedron** = the smallest box that encloses the freight, which is what a dimensioner measures. **Accessorial** = an extra-service charge. **Detention** = a charge for time a truck waits past its free time. **AT7, AT8, B10, L11...** = segments (lines) of an X12 EDI message.

## 0. Summary for the pipeline

1. **Carrier-issued certificates are public after all.** UPS Freight weight certificates (about 38 pages in set 04 by OCR count) and "Freight Inspection Certificates" (4), a TForce weight certificate plus a cube measurement certificate (21-015 pp. 36-37), and a Holland "Weight & Inspection Certificate – Weight Correction" (21-006 p. 15). `data/doc-explanation.md` §1.2 says "No carrier-issued certificate image"; that is wrong.
2. **The certificate beats the BOL on weight and class.** NMFC Item 250100-A §§3-4 and Uniform BOL terms §7(d) say charges follow the articles actually shipped. The shipper can only rebut with better evidence, e.g. its own legal-for-trade scale ticket or a certified public-scale weighing. The BOL is the *declaration* the change is measured from, not the answer.
3. **Certificates contain checkable arithmetic, and it sometimes fails.** UPS Freight's certificate for PRO 406858966 prints a density of 20.08 pcf, which is the BOL weight (4,117 lb) divided by the cube. Its own weight (4,825 lb) gives 23.54 pcf. A shipper's certificate computed density on *net* weight (3.99 pcf) where carriers use gross weight (5.66). The software should recompute weight ÷ cube on every certificate.
4. **There is a unit trap.** A Pure Fishing BOL declared kilograms (149.59 kg = 329.8 lb). Holland's certificate shows "tendered 151, actual 360, variance 209" lb. The bill's 61-lb and 5-lb lines equal the BOL's kilogram figures read as pounds. Read correctly, the variance is about 30 lb *[our reading]*.
5. **For accessorials, the BOL shows only what was requested.** SEFL's residential (Item 753) and limited-access (Item 754) items both say an unmarked BOL "will not relieve" the shipper. SEFL liftgate (890-100) applies when "required or requested". TForce charges residential "regardless of a shipper's designation". In a real Yellow dispute (23-003), each side used a satellite picture to argue whether the premises was a storage site. The decisive fact is the nature of the premises, and no document in this slice states it.
6. **DRs differ widely.** Only some carry tick-boxes for services performed (XPO, Yellow) or arrive/depart or wait times (UPS Freight 2008, Yellow 2008). XPO's 2021-25 DRs give only a delivered time. The 214s in set 19 carry no arrival-plus-delivery pair for any shipment.
7. **Join keys break in predictable ways.** BOL numbers have leading-zero variants. Several BOL numbers can share one field ("63387,63388"). Freight-forwarder booking numbers stand in for BOL numbers. A rate confirmation's "Bill of Lading Number" can hold the shipper's SID. A second carrier's billing advice can serve as the BOL. Payers differ between two BOLs for the same load.
8. **No shipper-facing TL price and no quote document is public.** All 18 rate confirmations in the catalogue are broker-to-carrier. The "6 files evidencing B5" are ABF bills that print a quote number, plus pleadings in Central Freight v. Amazon. The one shipper-side TL price held is an EDI 204 (Seaboard Foods, L3 $2,377.08).

## 1. Method

Read 2026-10-10. Scans were rendered with `pdftoppm` at 50-300 dpi and viewed. Text layers and the set 04 OCR were searched with `grep` and `python3 -I`. All arithmetic was done in `python3 -I`.

| Type | Files and pages read | Real examples seen |
|---|---|---|
| BOL forms, terms, standards | 15-075 (2 pp), 15-076 (1 p), 15-077 (1 p, NMF 100-AV Item 250150), 15-079 pp. 23-24 (Item 250100-A) | templates |
| Filled BOLs | 03-003 pp. 5, 9, 13, 17, 21 (XPO, VICS short form and shipper-printed); 04-008 p. 7; 04-009 pp. 18, 89; 06-016 p. 11 (UPS Freight 2008, 2018); 21-002 p. 6 (ODFL 2004); 21-006 pp. 13, 19, 20; 21-015 p. 34 (TForce, a billing advice used as BOL); 23-002/003/004 pp. 4-5 (GlobalTranz); 22-003 p. 14; 22-012 p. 5 | 17 |
| Delivery receipts | 03-003 pp. 6, 10, 14, 18, 25; 21-004 p. 8 (XPO 2020-25); 04-008 p. 6; 04-009 pp. 16-17, 86-88 (UPS Freight 2008); 05-015 pp. 1-12 (Yellow 2008-09); 21-006 p. 21 (Yellow 2022); 21-015 p. 35 (TForce 2022) | 14 |
| W&I and reweigh | 04-008 p. 8; 04-009 pp. 19, 91 (UPS Freight certificates); OCR keyword pass over all 417 OCR pages of set 04; 21-015 pp. 33, 36-37; 21-006 pp. 12, 14-15; 23-004 pp. 4-8; 23-011 p. 4; 24-007 pp. 4-5; 03-003 pp. 11-21 (XPO reweigh bills); 21-004 p. 4, 21-005 (text); 07-017 p. 8, 07-018 pp. 11-19; 15-078 (HB44 §5.58 S.1.6, T.3, UR.5), 15-082, 15-083, 15-084 | 9 certificates or tallies, 12 reweighed bills |
| EDI 214 / 204 | 19-016 to 19-023 (all 8 real 214s), 19-036; 19-024, 19-025, 19-026, 19-027 (204s); 19-001 (the 210 matching a 214); 12-049 | 8 + 4 |
| Quotes (B5) | 01-001 (text: quote lines and notes, e.g. pp. 30, 35); 09-046 pp. 38-40 (deposition); 09-048 pp. 3, 6-10 | 0 quote documents |
| TL rate confirmations / packets | 10-035 pp. 2-4; 10-042 pp. 1-2; 10-043; 22-003 pp. 9-18; 22-013 pp. 4-7; 22-012 pp. 4-7, 20 | 7 rate cons, 5 invoices |
| Tariff items used as basis | 13: SEFL 1090 Items 753, 754, 890-100, 996; ODFL 100-Q Items 367, 995; ABF 111-AU Item 992; XPO 199-AK.3 Item 239; Estes 105 Items 751, 992; TForce 102-T residential ¶8 | current versions only |

**Limits.**
- The tariffs read are 2025-26 versions. The bills are from 2004-2026, so tariff thresholds are only *assumed* to have applied then.
- OCR counts for set 04 are approximate, because the OCR garbles headers.
- The set 02 SEFL bills were not re-read; the AT verification transcriptions are relied on.

## 2. Field inventory

Reliability codes: **S** = structured (EDI); **T** = typed or printed (text layer or clean print); **H** = handwritten; **St** = stamp or label; **Sc** = typed but a scan, so OCR is needed.

### 2.1 Bill of lading

| Field | Where it sits | Seen in (file, page) | Example value | Reliability | Checks |
|---|---|---|---|---|---|
| BOL number | VICS top right; UPGF box 2; ODFL box 6 | 04-008 p. 7; 06-016 p. 11; 21-006 p. 13 | 62782; 180926120044; 00286320003321169 (17-digit GS1) | T/H; often blank on shipper-printed XPO forms (03-003 pp. 5, 13, 17) | A2, A6, A7 |
| PRO label | Affixed barcode sticker | all filled BOLs | "UPS Freight 241 325 140 CIN"; 712-591246 | St (barcode plus print) | A2, A6 |
| Ship date | Form header | 03-003 p. 5; 06-016 p. 11 | 12-28-21 (H); 09/26/2018 (T) | T/H | B1, B8, G1 |
| Shipper SID, consignee CID, FOB | VICS ship-from / ship-to | 15-075; 21-006 p. 13 | SID 0002181470 | T | join only |
| Consignee name and address, suite, dock | VICS ship-to; UPGF box 1 has "suite" and "dock" | 04-009 p. 89 | "Delphi CMM3 … Suite B, Dock 2" | T/H | D2 (premises), A6 |
| Freight terms | Prepaid / Collect / 3rd Party boxes; ODFL says "defaults to prepaid" | 21-002 p. 6; 04-008 p. 7; 06-016 p. 11 | Collect ☒; "Third Party Prepaid" ☒ | T/H tick | A5 |
| Third-party bill-to | VICS box | 03-003 pp. 5, 9; 22-012 p. 5 | Vital Pharmaceuticals; "Pepsi Beverages Co. c/o Cass" | T | A5, A3 |
| PO, customer order no., packages, weight, pallet Y/N | Customer order table | 03-003 pp. 13, 17, 21 | "GRAND TOTAL 10 / 8567" | T/H | A6, C1 |
| Handling units, package type, weight per line | Carrier information table | 03-003 p. 5; 21-002 p. 6 | "1 PALLETS 200 lbs" | T/H | C1 |
| NMFC item and sub, class | "LTL only" columns | 21-002 p. 6; 21-006 p. 19 (PipingRock); 04-009 p. 89 | 156600-3 / 250; 157320-05 / 125; class 100, NMFC blank | T/H; often blank (03-003 pp. 9, 13, 17, 21) | B4, C1 |
| Weight unit | Column header | 21-006 p. 13 | **"WEIGHT (kg)" 149.59** | T | C1 (normalise first) |
| Dimensions, total cube | Description text or a cube box | 06-016 p. 11; 21-006 p. 19; 23-004 p. 5; ABF bills echo them | 48×48×24 … "TOTAL CUBE: 44"; "Vitamins (48L 40W 48H)" | T | C1, B3 (cube minimum) |
| Accessorial request boxes | UPGF box 5; ODFL box 7 codes (ARN, CA, EXD, HYD, IDC, OVL, PFF, RDC) | 06-016 p. 11; 04-009 p. 89; 15-076 | "LIFT GATE PICKUP/DELIVERY" ☒; none ticked | T tick | D2 |
| Special instructions (free text) | VICS has only this; no tick-boxes on the Estes VICS form | 15-075; 03-003 p. 17 | "Appointment needed"; "Call 48 hrs. in advance for delivery appt." | H/T | D2 (appointment, notify) |
| Guaranteed service requested | UPGF box "Guaranteed delivery requested" | 06-016 p. 11; 04-009 p. 89 | unticked | T tick | E1 |
| Quote or rate estimate number | ODFL box 18 "Rate Estimate #" | 15-076 | (none filled in samples) | T | B5, A7 |
| Required delivery date | ODFL box 16 | 15-076 | — | T | E1, E2 |
| Declared value | Value box | 06-016 p. 11 | 20,000.00 | T | out of scope (cargo) |
| Loaded by / counted by, driver piece count, date received | Signature block | 03-003 p. 5; 06-016 p. 11 | "By shipper"; received 9/27/18 against BOL date 09/26/2018 | H tick | D2 (shipper load and count) |
| Stack and handling flags | Description or special instructions | 04-008 p. 7; 21-006 p. 19 | "DO NOT DOUBLE STACK"; "Stack: No" | T | D1 |

### 2.2 Delivery receipt

| Field | Where it sits | Seen in | Example value | Reliability | Checks |
|---|---|---|---|---|---|
| PRO, origin and destination terminal, ship date | Header | 03-003 p. 6; 04-009 p. 16; 21-004 p. 8 | 405-677016, NPB→NRM, 2/12/21 | T/Sc | join |
| Shipper and consignee as the carrier keyed them | Header blocks | all | VITAMIN SHOPPE | Sc | D2 |
| Bill-to account | Header or description | 04-009 p. 16 | DR "BILL TO: 24068435" against bill-to 32801414 on the freight bill (p. 15) | Sc | A5 |
| Weight, pieces, reweigh text | Description | 03-003 p. 14; 04-008 p. 6; 21-015 p. 35 | "CBR REWEIGH OF SHIPMENT FEE"; "WEIGHT DECLARED AS 00557 LBS. ACTUAL WEIGHT IS 00655 LBS." | Sc | C1 |
| Handling units counted | Description | 04-009 p. 16 | "PIECE(S) COUNTED AND VERIFIED ON 5 SK HANDLING UNIT(S) SAID TO CONTAIN (18 OT) REELS" | Sc | C1, D2 |
| Services-performed boxes | Bottom row | XPO 03-003 p. 6, 21-004 p. 8 (inside, liftgate, residential, construction/util); Yellow 05-015 p. 7 (plus "# pieces sort & seg"); Yellow 2022 21-006 p. 21 ("Delivery services provided not listed above": liftgate, sort/seg, limited access, inside, residential, other) | all unticked in samples | T tick | D2 |
| Delivered pieces, date, time | Bottom row | 03-003 p. 25; 21-004 p. 8 | "1025", 12/21/20 (H); "5 Of 5 / 09:13 / 12/29/2025" (T) | H (2020-21), T (2025) | E1, E2, D3 |
| Arrive / depart, wait time | UPS Freight ODOM / ARRIVE / DEPART; Yellow "WAIT TIME START / END" | 04-009 p. 16; 05-015 p. 1 | 12:37 / 12:57 (H); blank | H | D3 |
| Appointment | Header or autocode | 05-015 p. 7; 03-003 p. 18 | "APPT# 1237660 APP 01/05"; handwritten appointment | T/H | D2 (APT), E1 |
| Guaranteed-service banner | Description | 05-015 p. 1 | "EXACT EXPRESS … XPRS DATE 12/29/08 DELIVER BY 17:00" | Sc | E1 |
| Dimensions and chargeable weight | Description | 05-015 p. 7 | "DIMENSION INFO … CHARGEABLE (GAD) WEIGHT 237" | Sc | C1 |
| Consignee receiving stamp, exceptions | Over the body | 03-003 pp. 14, 18, 25; 05-015 p. 7 | "Subject To Count The Vitamin Shoppe"; "DROP TRAILER COUNT SUBJECT TO VERIFICATION UPON UNLOAD"; "received 704 cases…" | St/H | D2 (business evidence), cargo |
| Address correction | Handwritten | 04-009 p. 16 | "Moved to old … Building, Antwerp OH" | H | D2 (redelivery), A6 |
| Child (handling-unit) PROs | Description | 21-004 p. 8 | 5 child PROs | T | join at pallet level |

### 2.3 Weight, inspection and reweigh records

| Field | Where it sits | Seen in | Example value | Reliability | Checks |
|---|---|---|---|---|---|
| Freight bill (PRO) number, weighed date, service centre | Header of a carrier "WEIGHT CERTIFICATE" | 04-008 p. 8 (UPS Freight 2008); 21-015 p. 37 (TForce 2022) | 241325140, 04/17/2008, CIN; 546903626, 12/20/2022, DTR | Sc (TForce page is an image without a text layer) | C1, G1 |
| Weight per handling unit and total | Certificate table | same | 210 / 220 / 225 = 655; 735 / 755 / 835 / 820 / 735 / 785 = 4,665 | Sc | C1 |
| Legal basis cited | Certificate text | same | "certified 'legal for trade' … NMFC 100-series items 360 and 995" (TForce adds UPGF 102 items 362, 990) | Sc | C1 |
| Inspection PRO, date, terminals, packing type, dimensions per piece, cube, density, NMFC item, change type, comment | UPS Freight "Freight Inspection Certificate" | 04-009 pp. 19, 91 | 54×41×32 in ×5 = 205.00 ft³, "Shipment Density 20.08", NMFC 041330-02, change "N", "SPMT SHOULD BE RATED 41330-2, CL 85" | Sc | C1, B4 |
| Cube certificate | TForce "CUBE MEASUREMENT CERTIFICATE" | 21-015 p. 36 | 6 units, 537.33 ft³, "NTEP certified dimensioning device installed at our Detroit, MI facility"; columns "No top loading", "Manual measurement" | Sc | C1, B3 |
| Tendered vs actual weight, variance | Holland "Weight & Inspection Certificate – Weight Correction" | 21-006 p. 15 | 151 / 360 / 209; dimensions "-" (not measured) | T (image) | C1 |
| Reweigh note on the bill itself | Bill description | 04-009 p. 15; 21-015 p. 33; 03-003 pp. 12, 16; 21-004 p. 4 | "WEIGHT DECLARED AS 04117 LBS. ACTUAL WEIGHT IS 04825 LBS."; "RE-WEIGHED PER WEIGHT CERTIFICATE"; "WAIVED INSPECTION" | T/Sc | C1, C2 |
| Shipper's own weight certificate | Mover's form | 23-004 p. 8 | 2 crates 84×45×87 in, gross 1,422 + 731 = 2,153 lb, tare 636, net 1,517, "Density 3.99", "WEIGHED ON CERTIFIED SCALE" | T | C1 (rebuttal) |
| Consignee or forwarder pallet tally | Warehouse form | 21-006 p. 14 | pallet 1: gross 355, 80 cartons, 48×40×54; shipment no. 2181470 | H | C1 (rebuttal) |
| Device standard | HB44 §5.58 Table S.1.6; T.3 | 15-078 | tolerance ±1 division; dimensions printed or recorded and "available upon request by customer"; device ID required where more than one device is used | T | C1 |
| Device type approval | NTEP certificate | 15-082, 15-083 | TLD250 max 39×31×39 in; CS900 max L 100 × W 36 × H 36 in | T | C1 (parcel-size devices, not pallets) |
| W&I vendor charge to carrier | Vendor invoice | 24-007 pp. 4-5 | per-PRO charges $15-129 to NEMF | Sc | context only |

### 2.4 EDI 214 (shipment status)

| Field | Segment | Seen in | Example | Reliability | Checks |
|---|---|---|---|---|---|
| PRO, shipment ID (BOL), SCAC | B10-01, -02, -03 | 19-017 | 00902527924 / 00280740007194473 / ODFL | S | join |
| References | L11 with a qualifier (PO, BM = BOL, QN) | 19-016, 19-023 | L11*65585*BM; L11*48117132*PO | S | join |
| Parties | N1 SH/SF, CN/ST, BT | 19-023 | BT = bill-to party | S | A5 |
| Status event, reason, date, time, time zone | AT7-01 (or -03 for appointment), -02, -05, -06, -07 | all | AF (departed pickup), AG (estimate), X1 (arrived at delivery), X6, X4, D1 (delivered); time zones ET/CT/LT | S | E1, E2, D3, A6 |
| Location, equipment | MS1, MS2 | 19-021, 19-023 | WILMINGTON OH; trailer | S | — |
| Weight, lading quantity | AT8 | 19-017 | 606 lb on the first message, 650 lb on pickup and delivery | S | C1 |
| Pickup and estimated delivery dates | G62 86, 17 | 19-023 | 20130211 / 20130214 | S | E1 |

Counts over the 8 real files: 16 shipment keys and 38 AT7 events (AF 9, AG 7, X6 6, D1 5, appointment 4, X1 3, X3 2, X2 1, X4 1). No shipment has both an arrival (X1) and a delivery (D1) event. Code meanings beyond D1 are *assumed* from the X12 code list.

### 2.5 EDI 204 (load tender)

| Field | Segment | Seen in | Example | Checks |
|---|---|---|---|---|
| Carrier, shipment ID, payment | B2-02, -04, -06 | 19-024, 19-025 | SEFL / 65675 / PP | A6, A7, A5 |
| Purpose (original, change) | B2A | 19-027 | 04 = change | — |
| Stop sequence and type | S5 (CL, LD, UL, CU, PU) | 19-026 | 3 stops: 1 pickup, 2 drops | D4 |
| Pickup and delivery windows | G62 37/38 (or 10) and 53/54, time qualifiers I/K/G/L | 19-025, 19-027 | 2013-02-13 14:00-16:30 | D3, E2 |
| NMFC item per line, weight | L5-03, AT8 | 19-025 | 157320-3 at 432 lb; 4620-5 at 106 lb | B4, C1 |
| References | L11 (order, PO, route, max temperature, miles per stop) | 19-027, 19-026 | "-10.0 F*MT"; "233*MI" | D4, B7 |
| Total weight and **tendered charge** | L3-01, -03 | 19-027; 19-026 (marked TEST) | 42,186 lb, $2,377.08; 7,000 lb, $989 | B6 |

### 2.6 Rate quotes (B5)

| Field | Where it sits | Seen in | Example | Checks |
|---|---|---|---|---|
| Quote / PQ schedule number | Bill description | 01-001 (84 "PRICING QUOTE" lines, 82 distinct PQ numbers) | "PQ SCHEDULE NO: LWVPH42154" | B5, A7 |
| Carrier's own quote-difference note | Bill description | 01-001 (22 notes, e.g. p. 30) | "The invoice amount differs from the quoted amount … Special Service of SPECIAL HANDLING SERVICES - LUMPER that was not included in the quote" (lumper 18, sort/seg 2, limited-access military 1, non-business-hours delivery 1) | B5, D2 |
| Measured cube and rated dimensions | Bill description | 01-001 (81 and 101 occurrences) | "ABF MEASURED CUBE: 26.670 CUFT", "RATED DIMENSIONS: 40X48X24" | C1 |
| Dynamic discount line | Bill line | 01-001 (19 lines) | DYNDISC −181.83 | B5 |
| Quote number on the SEFL bill | Bill footer | set 02 per AT verification | QUOTE #CWEN3E465 | B5 |
| The quote document itself | — | **not held**; the CFL v. Amazon files (09-033, -046 to -049) argue about spot quotes but attach none | — | B5 |

### 2.7 TL rate confirmation and packet

| Field | Seen in | Example | Checks |
|---|---|---|---|
| Load or order number, date | 10-035 p. 2; 10-043; 22-003 p. 17 | CHR #218316538; KCH 8615027 dated 01/28/2024 for expected pickup 01/26/2024 | A7, A6 |
| BOL number field | 10-043; 22-013 p. 5; 22-012 p. 7 | MEMT134075; 502464982; **76930091 (the shipper's SID, not its BOL number 4505279147)** | A7 |
| Stops with date, appointment time, reference | all | pickup 12/8/16 13:30, delivery 12/9/16 06:30 | D3, D4, E2 |
| Weight, pieces, dimensions | 10-035; 22-003 p. 17 | 14,062 lb est.; 4 crates with dims, 2,414 + 2,635 + 2,690 + 5,269 = 13,008 lb | (TL flat: weight rarely moves price) |
| Linehaul and fuel | 10-035 p. 3; 22-013 p. 5 | flat $1,373.00 "includes $136.08 fuel"; $2,800.00 | B6, B8 |
| Distance | 22-013 p. 5; 22-003 p. 17 | 1,432.07 mi; 97 mi | B7 |
| Detention, TONU, layover, lumper terms and evidence rule | 10-035 p. 2; 10-043; 22-012 pp. 7, 20; 10-042 p. 2 | Costco "in time and out time" label; "arrival and departure times must be stamped and/or written on the BOL"; "in and out times must be marked on the bills by the receiver"; King of Freight "does not pay detention, TONU fees, or layovers" | D3, D5, D6, D7 |
| Billing deadlines | 22-013 p. 6; 10-042 p. 1 | accessorials within 24 hours, invoices within 45 days; 10% cut if paperwork is over 3 business days late | G1 |
| All-inclusive clause | 10-035 p. 4; 10-043; 22-013 p. 6 | "inclusive of all charges … no different tariff rate" | B6, D1 |

## 3. Overlaps with the bill: what confirms, what contradicts, who wins

| Bill field | Compared with | Who wins when they disagree, and why | Seen |
|---|---|---|---|
| Billed weight | BOL declared weight → carrier certificate → shipper's own scale ticket | **The carrier's scale record**, if it exists and is legal for trade. NMFC 250100-A §4: "Freight charges must be assessed on the actual gross weight". Uniform BOL §7(d): charges follow "the articles actually shipped". Each carrier's tariff sets the fee and trigger: XPO 239, fee $50.70 for an increase of 25 lb or more; ODFL 367, $25 for an increase of 20 lb or more, scales within 1%; ODFL 995, 40 lb per pallet tolerance when pallets are not broken out; Estes 992, $25 for +100 / −500 lb; ABF 992, $55 when charges move $10 or more, reductions processed only above the fee; SEFL 996, $15. The shipper rebuts with "satisfactory proof" (Estes 992 ¶4) or a certified public scale (ABF 992 ¶5, $317.17, only while ABF holds the freight). | XPO 590.48→660, 8,567→8,715, 1,210→1,425 lb (03-003 pp. 11-21); UPS 557.28→655 (04-008 pp. 5-8), 4,117→4,825 (04-009 pp. 15-19); TForce 4,424→4,665 (21-015); Holland "151"→360 (21-006); SEFL 2,430→2,720 with no note (AT §7.2) |
| Billed class / NMFC | BOL class → inspection certificate with density | **The inspection, where it shows dimensions.** NMFC 250100-A §3(a): if the description "is found to be inaccurate, the carrier … shall correct". Density = certificate weight ÷ certificate cube, which the software must recompute. | UPS 450285371: BOL class 100, 650 lb; certificate 515 lb ÷ 53.08 ft³ = 9.70 pcf; billed class 150 plus inspection $18 plus reweigh fee $18 on a *downward* reweigh (04-009 pp. 85-91). PipingRock 1,135 lb ÷ 106.67 ft³ = 10.64 pcf, class 125 on all three documents (21-006 pp. 18-21) |
| Accessorial: residential, limited access | BOL marks; DR stamp; premises | **The nature of the premises**, under the carrier's item. The BOL only shows a request: SEFL 753 and 754, "omission … will not relieve". Definitions differ: Estes 751 excludes the part of a premises selling to the walk-in public; TForce charges if its system *or* the actual address is residential, "regardless of a shipper's designation". | 23-003: limited access declined because the carrier listed the site as self-storage; the shipper replied with a satellite photo and a forklift unload. SEFL $94 "per Google Earth" (AT §7.1) |
| Accessorial: liftgate, inside, sort/segregate, notify, appointment | BOL boxes or special instructions; DR boxes | **Request (BOL) or requirement (tariff), then performance (DR).** SEFL 890-100 applies when liftgate is "required or requested", so an unmarked BOL does not defeat it. A ticked DR box or a printed "verified by receiving dept." line supports performance. | XPO 326-343835: APT $51.90 matches the BOL's "Appointment needed" (03-003 pp. 19-21); UPS Store BOL liftgate ☒ (06-016 p. 11); Yellow DR "sort and seg verified by … receiving dept. yes/no" left blank (05-015 p. 1) |
| Lumper, special handling vs quote | ABF quote note | **The quote, if it excludes the service**: ABF itself prints that lumper "was not included in the quote" | 01-001 p. 30 |
| Consignee name, dock | BOL ship-to; DR stamp; DR address note | DR stamps show a business received it; a DR address correction supports a redelivery or reconsignment charge | "…CITY WHSE" charged residential (AT); "Moved to old … Building" (04-009 p. 16) |
| Delivery date and time vs guarantee | DR delivered date/time; 214 D1; 210 B3-09; BOL guarantee box; DR banner | **DR or 214 for the time**; the carrier's guarantee item for the terms. Uniform BOL §2(a): no schedule unless "arranged or agreed to in writing or electronically prior to shipment" | ODFL 214 D1 2012-09-27 11:07 CT = 210 delivery date 20120927 (19-017, 19-001); Yellow "XPRS DATE 12/29/08" with the consignee's appointment on 12/30 (05-015 p. 1) |
| Detention (TL; LTL wait time) | Rate con terms; receiver's in/out record; BOL or DR times | **The evidence the rate con names**: the receiver's label, the BOL stamp, a detention form. LTL: the carrier tariff; DR wait boxes where they exist | CHR (10-035 p. 2); KCH (10-043); Taylor/BDS (22-012 p. 20); J&L BOL detention boxes blank (22-003 p. 14) |
| Quote number | BOL box 18 / bill PQ number | The quote applies only if referenced (practice *assumed*, AK §3.2 A7); ABF prints its own difference note | 01-001 |
| Freight terms, payer | BOL terms box; third-party box; rate con; carrier letters | **The BOL as corrected by written authority** (the shipper's letter of authority, a corrected BOL). In brokered TL the **rate con** decides who pays the carrier, whatever the shipper's BOL says. Uniform BOL §7(a): consignor and consignee are liable "as billed or corrected" under 49 U.S.C. 13710 | Winn-Dixie: BOL Collect, re-billed prepaid third party "per letter", $15 corrected-BOL fee (21-002 pp. 6, 17); PipingRock BOL "Bill collect to" consignee vs broker Sunteck's BOL "Third party" (21-006 pp. 19-20), Holland billed collect; Pepsi BOL bill-to Pepsi c/o Cass vs Taylor invoice to BDS (22-012 pp. 4-5) |
| Pieces / handling units | BOL totals; DR counts; bill | Bill and DR follow the carrier's count; BOL totals can be internally inconsistent | XPO 405-634110: BOL "10" packages against 9 pallet lines; bill 9 pcs (03-003 pp. 15-17) |
| Cube (cube minimum B3) | BOL dimensions; carrier cube certificate; bill "measured cube" | Carrier measurement, ±1 division (HB44 T.3); recompute from dimensions | ABF 40×48×24 = 26.667 ft³ = "MEASURED CUBE 26.670" (01-001 p. 35); UPS bill 210 ft³ vs its own certificate 205.00 (04-009 pp. 15, 19) |
| TL linehaul, fuel, miles | Rate con; 204 L3 | Rate con ("inclusive of all charges") | Werner $2,800 = $2,800 (22-013 pp. 4-5); Taylor 332 mi × $0.47 = $156.04 (22-012 p. 4) |

## 4. What each document cannot prove

- **BOL.**
  - An unmarked BOL does not defeat a residential, limited-access or liftgate charge (SEFL 753, 754, 890-100).
  - A declared weight is only a declaration: §7(d) and Item 250100 let the carrier correct it.
  - A blank class does not mean any particular class.
  - BOLs printed from a shipper's own system can contradict themselves. 03-003 p. 9 lists a tent, a table and banners under a pre-printed "Nutrition Supplements" commodity line.
  - The payer box is not the payer in brokered TL.
- **Delivery receipt.**
  - A company stamp or signature shows a business received the freight. It does not show there is no dwelling on the premises (Item 753 covers "the entire premises on which a dwelling for living is located").
  - An empty services box does not prove the service was not done; most samples leave every box blank.
  - Weight on a DR is printed after the reweigh (03-003 p. 14 already shows the reweigh fee), so it is not independent evidence.
  - Handwritten dates and times are ambiguous (03-003 p. 14 has two different handwritten dates).
- **W&I certificate.**
  - It proves what the carrier's device read. It does not prove the device was legal for trade on that day: no certificate seen names a device ID or an NTEP certificate number.
  - The two NTEP certificates held are for parcel-size dimensioners (maximum height 36-39 in), so they cannot vouch for pallet measurements.
  - Holland's certificate gives no dimensions at all.
  - The DOJ complaint alleges Yellow and Roadway made 75,324 positive and 42 negative reweigh corrections over the same period (07-018 p. 18; allegations, not findings). Absent a shipper-side weight, the bill will not reveal a reweigh that should have *lowered* the charge.
- **Shipper's certificate or tally.** It is rebuttal evidence only. Its density may use net weight (23-004 p. 8), and its dimensions may differ from its own BOL: 84 vs 87 in.
- **EDI 214.**
  - It shows event times, not who caused a delay. No AT7 reason other than "NS" (normal) or "NA" was seen.
  - It does not show accessorials performed or signatures.
  - Weights can change between messages for the same PRO: 606 → 650 lb on ODFL 00902527924, source unstated.
  - Times can be junk ("00000000", 19-021).
- **EDI 204.** It shows what was tendered and, for TL, the tendered price. It does not show what was agreed if the carrier counter-offered.
- **Rate confirmation.** Every one held is broker-to-carrier. It proves what the broker owes the carrier, not what the shipper owes the broker.
- **Quote evidence.** The bill's quote number proves a quote existed, not its terms. ABF's own note is the carrier's account of the difference.

## 5. Join keys

| Key | Appears on | Failure cases seen |
|---|---|---|
| PRO | bill, DR, certificate, 214 B10-01, 210 B3-02, BOL label | Alpha prefix or check digit ("I579382821", "670-438395-X", "406858966 RO" suffix); child PROs per pallet (21-004 p. 8); an older carrier's PRO on the same paper (21-015 p. 34) |
| BOL number | BOL, bill ("B/L NO", ABF "Bill of Lading No"), 214 B10-02, 210 B3-03, L11 BM, rate con | Leading zeros: ABF "00209216" vs CRN "000209216"; SID 0002181470 vs tally 2181470. Several in one field: "63387,63388" (19-018). Pipes: "502464982\|IDB61769\|954" (22-013 p. 4). Booking number used as BOL: N1883348HKG (21-006). Field holding a different identifier (22-012). Blank on shipper forms (03-003) |
| PO | BOL, bill, 214/210 L11 PO | Placeholder POs ("AUG 2022", "NONE", "#Aug 2022"); several POs per shipment ("MULTIPLE PO#'S", 03-003 p. 14) |
| Shipper number / SID | BOL, bill (ODFL "shipper#"), XPO "SN#/SI" | Carrier writes its own shipper number onto the BOL (21-002 p. 6) |
| HAWB / load / tender ID | rate con, invoice | Packet pages from different loads filed together: rate con ATL 113077 next to invoice ATL 113224 (22-003 pp. 12-13); the shipper required a valid "Tender ID" on invoices (09-048 p. 3) |
| Quote / PQ number | bill, BOL box 18 | Quote not on BOL; shipper cannot show the quote |
| Ship date | all | DR and BOL dates differ by a day (pickup vs paperwork); TForce bill ship date 12/20/2022 vs the billing advice's 12/13/22 (handoff between carriers) |
| Consignee name and city | all | Delivered to a different address than billed (04-009 p. 16); "c/o" names; a person's name care of a business |
| Weight (as a tie-breaker only) | all | Changes between documents by design (reweigh); units differ (kg) |

Rule *[our call]*: key on PRO first, then BOL number with zeros and punctuation stripped and multi-value fields split, then PO plus ship date plus consignee. Never key on amount and date.

## 6. Gaps: facts the checks need that no document in this slice carries

| Fact | Checks | Who holds it |
|---|---|---|
| Whether a dwelling or limited-access use is on the premises | D2 | Nobody authoritative. The carrier's address database is not shared; the shipper knows its customer; public map and zoning data is evidence only |
| The device record behind a certificate (device ID, last inspection), and inspection photos | C1 | Carrier (HB44 S.1.6: "available upon request") |
| Pre-reweigh charges, i.e. the original bill | A4, C1 | Shipper's AP file; often missing (AT §7.2) |
| Arrival and departure times at LTL delivery | D3 | Carrier's driver app, often not printed; consignee's dock log |
| Who caused a delay (consignee appointment vs carrier) | E1, E2, D3 | Carrier and consignee; the 214 reason code is "NS" in all samples |
| Transit standard for a guarantee | E1 | Carrier's published transit tables |
| The quote document and its conditions | B5 | Shipper's portal history; carrier |
| Shipper-facing TL price when a broker is used (the broker's quote or tender) | B6 | Shipper's TMS or email; the only public example is a 204 L3 |
| Pallet tare when the BOL does not split it | C1 (ODFL 995) | Shipper |
| Whether "liftgate required" (no dock) | D2 | Consignee; DR box when ticked |
| Tariff versions in force for older bills | C2, D1 | Carrier archives; Wayback (AT §8) |

## 7. Recommended reading order for this slice *[our call]*

| Fact | Trust first | Fallback | Do not use for this |
|---|---|---|---|
| Declared weight, class, NMFC, pieces | BOL (normalise units, sum the lines, check against grand totals) | 204 L5/AT8; the bill's "WEIGHT DECLARED AS" line | DR (printed after the reweigh) |
| Actual weight | Carrier weight certificate | Bill's "ACTUAL WEIGHT IS" line; 214 AT8 on the pickup message | BOL |
| Dimensions, cube, density | Carrier inspection or cube certificate (recompute weight ÷ cube) | Bill "MEASURED CUBE"/"RATED DIMENSIONS"; BOL dimensions | NTEP certificate (a type approval, not a reading) |
| Services requested | BOL boxes, then special instructions | 204 notes; quote note on bill | DR |
| Services performed | DR boxes and printed verification lines | Driver notes; carrier POD image | BOL |
| Premises type | (none) → reviewer question | Consignee name and stamp as evidence | BOL, DR as proof |
| Delivery date and time | DR typed time; 214 D1 | 210 B3 delivery date | Handwritten DR date when it conflicts |
| Detention times | The record the rate con names | DR or BOL arrive/depart; 214 X1 → D1 | Bill line alone |
| Payer | Corrected BOL or letter of authority; in brokered TL the rate con | BOL terms box | Bill-to account on the DR |
| TL price | Rate con or 204 L3 for the same load (match on load/HAWB) | Shipper's own tender | A rate con for another load |
| Quote | Quote document | Bill PQ number plus carrier note | — |

## 8. Claim ledger

| # | Claim | Tag |
|---|---|---|
| 1 | UPS Freight weight certificate for 241325140, weighed 04/17/2008 at CIN, 3 units totalling 655 lb, citing NMFC items 360 and 995 | *verified* 04-008 p. 8 (first unit read as 210, sum consistent) |
| 2 | Bill 241325140: declared 557 → actual 655 lb, reweigh fee $18.00; BOL 62782 shows 557.28 lb, "Freight Charges: Collect" | *verified* 04-008 pp. 5, 7 |
| 3 | About 38 OCR pages with a UPS Freight weight certificate and 4 with a Freight Inspection Certificate in set 04 | *assumed* (OCR keyword count, garbled headers) |
| 4 | Inspection certificate 406858966: 54×41×32 in ×5 = 205.00 ft³, weight 4,825, density printed 20.08 = 4,117/205; 4,825/205 = 23.54 | *verified* 04-009 p. 19; arithmetic [our calc] |
| 5 | Bill 406858966: declared 4,117 → 4,825 lb, "WAIVED INSPECTION", 210 cubic feet, NMFC 041330-02 class 85, AS WEIGHT 5000 | *verified* 04-009 p. 15 |
| 6 | DR 406858966 has arrive/depart times and an address-change note; DR bill-to 24068435 vs bill 32801414 | *verified* 04-009 pp. 15-16 |
| 7 | 450285371: BOL 650 lb class 100; certificate 515 lb, 45.5×48×42 in = 53.08 ft³, 9.70 pcf; billed class 150 with inspection $18 and reweigh fee $18 | *verified* 04-009 pp. 85, 89, 91; [our calc] |
| 8 | TForce 546903626: billing advice 4,424 lb C70; certificate 4,665 lb (6 units) on 12/20/2022; cube 537.33 ft³ on 12/21/2022; 8.68 pcf | *verified* 21-015 pp. 33-37; [our calc] |
| 9 | Holland 609-194236-2: BOL weights in kg (131.49 / 149.59); certificate 151 / 360 / 209; bill lines C125 61, C200 294, C175 5 lb, REWT $35 | *verified* 21-006 pp. 12-13, 15 |
| 10 | The kg-read-as-lb explanation; correct variance about 30 lb | *assumed* [our reading; 149.59 × 2.20462 = 329.8] |
| 11 | XPO reweighs 590.48→660 ($37.25), 8,567→8,715 ($35.25), 1,210→1,425 ($39.40) lb | *verified* 03-003 pp. 11-21 |
| 12 | XPO 326-343835 APT $51.90 with "Appointment needed" on the BOL | *verified* 03-003 pp. 19-21 |
| 13 | XPO, Yellow 2008, Yellow 2022 DRs carry accessorial tick-boxes; UPS Freight DR has arrive/depart; Yellow DR has wait-time start/end | *verified* 03-003 p. 6; 05-015 pp. 1, 7; 21-006 p. 21; 04-009 p. 16 |
| 14 | XPO 2025 DR: delivered "5 Of 5", 09:13, 12/29/2025, 5 child PROs | *verified* 21-004 p. 8 |
| 15 | NMFC 250100-A §§2(c), 3(a), 4 and Uniform BOL §§2(a), 7(a), 7(c), 7(d) as quoted | *verified* 15-079 pp. 23-24; 15-077 |
| 16 | Tariff thresholds: XPO 239, ODFL 367 and 995, Estes 992, ABF 992, SEFL 996 | *verified* set 13 text (2025-26 versions); applying them to older bills is *assumed* |
| 17 | SEFL 753 and 754 omission language; SEFL 890-100 "required or requested"; Estes 751 walk-in exclusion; TForce "regardless of a shipper's designation" | *verified* 13 sefl_1090 lines 2669-2740, 4572-4584; estes_exla_105 line 3377; tforce_upgf_102-T line 2856 |
| 18 | Limited-access dispute decided on a "Self-Storage Warehouse" listing, rebutted with a satellite image | *verified* 23-003 pp. 4-5 |
| 19 | TONU dispute: the EDI pickup request said 1 unit, the BOL 3 units | *verified* 23-002 p. 4 |
| 20 | Shipper weight certificate: density 3.99 = net 1,517 / 380.63 ft³; gross density 5.66; BOL dims 87×45×87 vs certificate 84×45×87 | *verified* 23-004 pp. 5, 8; [our calc] |
| 21 | HB44 §5.58: tolerance ±1 division; dimensions printed or recorded and available on request; hexahedron note | *verified* 15-078 |
| 22 | NTEP TLD250 maximum 39×31×39 in; CS900 maximum height 36 in | *verified* 15-082 p. 1; 15-083 p. 1 |
| 23 | DOJ complaint: 75,324 positive vs 42 negative reweigh corrections (allegation) | *verified* 07-018 p. 18 |
| 24 | 214 tallies (16 keys, 38 events, no X1+D1 pair); ODFL AT8 606→650; SEFL time "00000000"; WTVA "63387,63388" | *verified* 19-016 to 19-023 |
| 25 | ODFL 214 ↔ 210 chain on PRO 00902527924, BOL 00280740007194473, PO 21838107023, 650 lb, delivered 2012-09-27 | *verified* 19-017, 19-001 |
| 26 | Seaboard 204 L3 42,186 lb, $2,377.08; SEFL 204 L5 157320-3 and 4620-5 | *verified* 19-027, 19-025 |
| 27 | ABF bills: 84 pricing-quote lines, 82 distinct PQ numbers, 22 quote-difference notes (18 lumper), 81 "measured cube" | *verified* 01-001 text (counts include any repeated pages) |
| 28 | Auditor's method: re-rate "derived from the bill of lading … not freight bill to bill of lading"; documents listed | *verified* 09-046 pp. 38-40 (depo pp. 35-37) |
| 29 | All 18 rate confirmations in the catalogue are broker or 3PL to carrier | *verified* catalogue `parties`; 10-035, 10-042, 10-043, 22-003, 22-012, 22-013 read |
| 30 | CHR detention evidence is the Costco label; KCH needs times on the BOL; BDS/Taylor needs receiver-marked in/out times | *verified* 10-035 p. 2; 10-043; 22-012 p. 20 |
| 31 | Rate con 22-012 "Bill of Lading Number: 76930091" equals the BOL's SID; BOL number 4505279147 | *verified* 22-012 pp. 5, 7 |
| 32 | LEI rate con ATL 113224: 13,008 lb by four crate lines, $500; J&L invoice 5207 $500; a different-load rate con (ATL 113077) filed beside it | *verified* 22-003 pp. 12-17; [our calc] |
| 33 | ODFL BOL guide boxes 2, 6, 7, 16, 18 as listed | *verified* 15-076 |
| 34 | Key-on-PRO rule and reading order | *assumed* [our call] |

**Catalogue corrections noticed (not applied).**
- 10-043 lists "CJ Logistics (broker); KCH Transportation (carrier)". The page says KCH issued the confirmation and the carrier is CJ Logistics.
- 15-082 is described as a "static LTL dimensioner". Its maximum size is 39 in.
- `data/doc-explanation.md` §1.2 ("No carrier-issued certificate image") and §1.1 ("quotes … 6 files evidence B5") need correcting per §0.
