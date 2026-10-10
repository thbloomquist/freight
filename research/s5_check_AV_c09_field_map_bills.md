# Check AV · Field map, bill side: what the carrier sends to ask for money (C-09 prototype)

*Reviewed 2026-10-10: `research/s5_check_AV_adversarial.md` (ledger 23 kept verified, 1 kept assumed, 5 narrowed, 0 discarded; 126 claims in all, 35 narrowed). The corrections are applied in `data/doc-explanation.md`; this file is kept as written. Main ones: 62 distinct SEFL bills, not 59; the PRO reuse is seen only on PDF prints, never in a guide; the "PREVIOUSLY INVOICED ON" list runs newest first.*

Written 2026-10-10. One of three field-map slices for the audit machine (this one: carrier invoices as EDI 210 files and PDFs, corrected and balance-due bills, statements of account). Nothing here is decided. It feeds steps 3-5 of the machine (read, check the reading, link) in `software-initial-pitch.md` §2, and the 33 checks (A1 … G2) defined in `research/s5_check_AK_c09_audit_workflow_and_products.md` §3.2.

**Terms used.** *PRO*: the carrier's bill number. *BOL*: bill of lading, the shipper's pickup paper. *cwt*: hundredweight (100 lb); LTL rates are dollars per cwt. *SCAC*: the 2-4 letter carrier code. *NMFC*: the commodity classification that gives each item a class. *Accessorial*: an extra service charge. *Deficit weight*: phantom pounds added so a shipment rates at the next, cheaper weight break. *Interline*: a shipment handed between two carriers. *TONU*: truck ordered, not used. *Lumper*: paid unloading help. *Text layer*: words a PDF already holds; *OCR*: words read from a scanned image. *X12 notation*: "B3-02" means segment B3, element 2 of an EDI file.

## 0. Summary
- **Every real 210 adds up.** 82 real or assumed-real 210 invoices (ODFL 34, AAA Cooper 11, Estes 3, TL 34): in all 82 the line charges equal the bill total (B3-07) and the L3 total.
- **The 210 never says "corrected" in the files we hold.** No real 210 fills B3-08 (correction indicator) or K1 (remarks). The codes exist only in guides, and they differ by firm: 3M AR/BE, TForce BD/RC, FedEx Freight BD/CO/PD, FedEx 4060 AD/BD/PD/RB.
- **Percentages are where the formats split.** ODFL's 210 gives the discount and fuel only as dollar lines. All 34 ODFL bills reproduce to the cent with discounts of 65/68/70/72/77% and fuel of 16.0/17.0/17.5% of net freight. AAA Cooper and Estes write the percentages as L5 free text. The X12 slot for a percent (L1-19) is unused in every real file. The PDFs of ABF, SEFL (2023), XPO (fuel only), TForce/UPS and ODFL print the percentages.
- **Bill dates are not one date.** The 210 gives the invoice date (B3-06), the ship date (B3-12 or G62) and a delivery date that ODFL marks as *estimated* (B3-10 = 017) on all 34 bills. TForce and UPS Freight reprints list every earlier invoicing ("PREVIOUSLY INVOICED ON"), which is the only bill-side record of when the first bill went out.
- **Corrections arrive in five shapes:**
  - SEFL prints the difference due;
  - ABF prints the original total, the new total and the reduction;
  - XPO prints the amount paid and the balance;
  - TForce prints the declared and the actual weight;
  - ODFL re-bills a new payer under the same PRO and labels it "ORIGINAL INVOICE".
- **Same amount is not same bill.**
  - ABF: 23 of 101 bills fall into 9 groups that share both total and ship date.
  - TL: two TQL pairs and one Werner pair match on lane, amount and adjacent dates but differ in PRO and load number.
- **TL bills rarely carry what the rate check needs.**
  - Miles appear on only two of the seven TL and broker invoice layouts read (Werner Enterprises, Taylor).
  - Fuel is a flat amount on the 210s and on USA Truck's PDF.
  - Werner's direct bill carries a shipper number of "RETURN" while the attached BOL says 104310.

## 1. Method
Everything below was read from files under `data/sources/`, their text layers in `data/derived/`, or page renders (`pdftoppm -r 80`). A few scans were OCR'd at 150 dpi (tesseract, `data/_tools/tessdata`). The 210s were split into segments by a parser in the scratchpad, which also re-summed every transaction. SEFL's sample form was downloaded to its own scratchpad folder. Its 27 form fields were read from the raw bytes with `python3 -I`; the file has no JavaScript, and nothing in it was run.

| Source | file_id | Read |
|---|---|---|
| ODFL 210s (2012-13) | 19-001…19-008 | 8 files, 34 transactions, all segments |
| AAA Cooper 210s (2012-13) | 19-009…19-014 | 6 files, 11 transactions |
| Estes 210s (2013) | 19-015 | 3 transactions plus a group-total (ST*980) |
| TL 210s sent by BPTS to Target (2025-26) | 19-033…19-035 | 3 files, 34 transactions (WIEL 11, TQYL 20, SPXQ 3) |
| Template / partly real 210s | 19-029…19-032 | segment inventory only (K1, POD, B2A appear only here) |
| 210 guides | 12-039…12-046, 12-051, 12-052 | B3, L0, L1, L7 definitions and code lists |
| ABF bills (2024, text layer) | 01-001 | 101 bills by script (title, PRO, total, dates); pp. 18, 23, 24, 75-77 read in full |
| SEFL bills (scans, OCR layer) | 02-002 | pp. 46, 49, 50, 51, 63, 70 viewed; pp. 28, 33, 35, 41, 48 per the verifier's transcription (`s5_check_AT_adversarial.md` §2) |
| SEFL sample invoice | sefl.com/vspdfdocs/shipping_invoiceExample.pdf | 2 pp., 27 named fields |
| XPO bills (2020-21, image only) | 03-003 | pp. 4-7, 15, 16 viewed; pp. 12, 20, 23 OCR'd |
| UPS Freight (2009-10, scans) | 04-006 | pp. 2-3 (OCR), 15-16 viewed |
| ODFL bills (2004-08, faxes) | 21-001, 21-002 | 21-001 pp. 11-12; 21-002 pp. 13, 17 |
| XPO bills (2024, text) | 21-005 | pp. 4-5, 8 |
| TForce bills and statements (2022-23, text) | 21-015 | pp. 4-5, 32-33 |
| Statements | 21-006, 21-007, 21-010, 21-013, 21-014, 22-011 | one page each (21-006 pp. 4-5) |
| TL and broker invoices | 22-001, 22-007, 22-008, 22-011, 22-012, 22-013, 22-015 | Wintzer p. 1; TQL pp. 5, 7, 8; Werner Enterprises pp. 4-5, 7, 10; RXO p. 31; Taylor p. 4; Werner Logistics pp. 4-6, 12-13, 23-25; USA Truck p. 4 |

Counts: 82 real or assumed-real 210 transactions. About 38 PDF bills from 12 carriers or brokers were read field by field, plus the 101 ABF bills by script. Nine statement layouts. Privacy: no person's name, signature, phone number or street address is copied below. The SEFL consignee in the worked example is named by town only.

## 2. Field inventory

### 2.1 EDI 210 (structured; every field below is machine-read, so "reliability" is about meaning, not reading)
| Field | Where | Carriers seen | Example (file_id) | Reliability / caveat | Checks |
|---|---|---|---|---|---|
| Sender | ISA-06, GS-02 | all | TL files: ISA-06 `BPTS` (a freight-payment firm), GS-02 `WIEL` (19-033) | the envelope sender may not be the carrier | A5, A3 |
| Carrier SCAC | B3-11 | all | `ODFL`, `AACT`, `EXLA`, `TQYL` | structured | all (key) |
| PRO / invoice no. | B3-02; TL also N9*IV | all | `00902527924` (19-001); `2924422` (19-033) | ODFL keeps leading zeros | A2, A4 |
| BOL / shipment id | B3-03; AAA Cooper also N9*BM | ODFL, AAA Cooper, TL | `00280740007194473` (19-001); Estes `NS` = not supplied (19-015); TL = load no. `100687708` | Estes sends none | A2, A6, C1, D2 |
| Payment terms | B3-04 | all | `PP`, `CC`, `TP` (19-033 has all three) | structured | A5 |
| Invoice date | B3-06 | all | `20121015` (19-001) | TQYL batch: 19 of 20 dated 20251215, for pickups from 2025-10-16 on (60 days earlier) | G1, F1 |
| Net amount due | B3-07, cents | all | `8590` = $85.90 (19-001) | equals the L1 sum in 82/82 | A1 |
| Correction indicator | B3-08 | none in real files | guides only (see §5.2) | absent | A4 |
| Delivery date | B3-09 + B3-10 qualifier | all | ODFL `017` = estimated (34/34); others `035` = delivered | ODFL's is not an actual date; blank on 2 WIEL bills | E1, D3 |
| Ship / pickup date | B3-12 (ODFL, AAA Cooper, Estes); G62*86 (ODFL, Estes, TL); AAA Cooper G62 22/35/41 | all | `20120925` (19-001) | structured | B1, B8, G1 |
| PO numbers | N9*PO, repeating | all | 7 POs on one bill, PRO 00902527927 (19-001) | many-to-one | A6, F2 |
| Other references | N9 CR, BM, IV, LN, IT, HU, SO | AAA Cooper, TL | TL `SO*TONU100698 819` (19-035) | meanings not defined in the files | A6 |
| Parties | N1 SH / CN / BT + N3, N4 | all | ODFL bill-to "c/o" a logistics firm (19-002) | names vary in spelling | A5 |
| Interline / route | R3 | AAA Cooper, ODFL, Estes | AAA Cooper `R3*NEMF*1*HARRISBURG*M****12698` (19-009) | R3-08 = partner's share, $126.98 of $325.60 | A3, A5 |
| Trailer | N7 | ODFL, AAA Cooper | `530303` (19-001) | structured | A6, D3 |
| Description, NMFC | L5-02; L5-03 + L5-04 `N` | AAA Cooper, Estes, TL | Estes `HAND TOOLS…`, `186900`, `N` (19-015); AAA Cooper NMFC inside the text (`BOOKS, NOI NMFC 161630`) | NMFC sometimes only in text | B4, C1 |
| Weight, pieces | L0-04, L0-05, L0-08, L0-09 | all | ODFL `650*G…1*PCS` (19-001); Estes qualifier `A3` = shipper's weight | TL L0-08 is junk (`30000 PLT`, 19-033) | C1, B3 |
| Deficit weight | ODFL: L0 + L1 code `DAA`; AAA Cooper: L0-02 `10000 LB` with L0-04 `1420` | ODFL, AAA Cooper | ODFL 167 lb (19-001, PRO …925) | two encodings | B3, A1 |
| Rate + qualifier | L1-02, L1-03 | all | ODFL `40.17 PH` ($/cwt); Estes `298.86 LB` (works only per cwt); Estes `197.00 FR` flat; AAA Cooper `MN` with code `MMC`; TL `0.00` | qualifier can mislabel the unit | B2, B3 |
| Charge | L1-04, cents | all | `26111` = $261.11 | structured | A1 |
| Charge code | L1-08 | all | `405`/`FUE` fuel, `DSC`, `DAA`, `MMC`, `SUF` (Canadian border fee), `400` linehaul, `TONU`, `LUM`, `LAY`, `STOP`, `STC` | ODFL Canadian bills carry two uncoded lines ($24.00, $11.00; 19-001 ST 0005) | D1, D4-D7 |
| Percent | L1-19 in the standard; in practice L5 text | AAA Cooper, Estes | `LESS 78.00 PCT DISCOUNT`, `Fuel Surcharge 29.00 PCT` (19-009); `DISCOUNT 84.0%`, `Fuel Surcharge added at 29.00` (19-015) | text to parse; absent at ODFL and TL | B2, B8 |
| Class | L7-07 | ODFL, AAA Cooper, Estes, TL | `050`, `060`, `70`; TL `77.5` | meaningless on TL | B4 |
| Tariff | L7-02, -03, -10, -11 | AAA Cooper, Estes | `CZAR`, `910`, `20120917`, rate base `0562` (19-009); `SMC ZRH 20110919` on direct lanes (19-011) | two tariffs for one shipper | B1, B2 |
| Remarks | L5 free text; K1 | Estes | `LEFT MSG FOR DEL APPT 11/14/13` (19-015) | K1 never used | D2, D3 |
| Totals | L3-01, L3-05, L3-11 | all | ODFL `L3*1000*G***11910` (rated-as weight, not actual) | structured | A1 |
| Batch control | ST*980 BT1 | Estes | 3 bills, $1,218.85 (19-015) | structured | A2 (completeness) |
| Test flag | ISA-15 | ODFL, Estes | `T` on real bills (19-001, 19-015) | must not reject on it | none |

### 2.2 PDF LTL bill (layout per carrier)
| Field | ABF (01-001) | SEFL (02-002) | XPO (03-003, 21-005) | TForce / UPS Freight (21-015, 04-006) | ODFL (21-001, 21-002) | Checks |
|---|---|---|---|---|---|---|
| Bill type | top right: "ORIGINAL INVOICE" (100), "CORRECTED INVOICE" (7 prints) | header centre: ORIGINAL, CORRECTED, BALANCE DUE, PAST DUE INVOICE | mid-page banner: "*** CORRECTED INVOICE ***", "*** BALANCE DUE INVOICE ***" | "COPY OF FREIGHT BILL" | footer "ORIGINAL INVOICE", also on the re-bill; "DUP" on reprints | A4 |
| PRO | "Freight bill No: 165526558" | "FREIGHT BILL NO:" `807148067` | "LTL INVOICE# 712-591246" | "FREIGHT BILL NO." `610384246` | `02902161435` | A2 |
| Ship date | "Shipment Date" | footer, first `>` value | "SHIPMENT DATE" | "SHIP DATE" | "PRO DATE" | B1, B8 |
| Bill date | not printed | footer "DATE BILLED" | not printed | "PREVIOUSLY INVOICED ON" list | "Invoice Date" | G1 |
| Due date | "PAYMENT DUE DATE" (or "Upon Receipt") | footer "PAYMENT DUE DATE" | "PAYMENT IS DUE BY" | "Payment Due ON RECEIPT" | "Due Date" | F1 |
| Account | "Account No", shipper and consignee account | footer "CUSTOMER NUMBER" | redacted | consignee, shipper and bill-to numbers | "BILL-TO #" | A5 |
| BOL | "Bill of Lading No: 209242" | footer "SHIPPER B/L NO." | in "CUSTOMER NUMBERS" | "B/L NO." (often NONE) | "SHIPPER B/L NUMBER" | A6 |
| PO | value printed above its label; also "PO:" in remarks (p. 18) | bottom box "PO. NUMBER" and "PO#" in remarks (p. 70) | "PO#" | "P.O. NO." | "PURCHASE ORDER NUMBER" | A6 |
| Quote | "PQ SCHEDULE NO: LMH2W51304A" (p. 18) | "QUOTE #CWEN3E465" | "QN#" (21-005 p. 4) | none seen | none seen | B5, A7 |
| Tariff | "Tariff: AOD000" | not printed; rules cited in notes ("SEFL 1090-B ITEM 610-100") | "TARIFF 199" (late fees) | "UPGF 560 11/14/22 C N 04090" (meaning *assumed*: pricing reference) | "TARIFF 559" | B1 |
| Terms | "Payment Terms: Prepaid" | last row: "PREPAID" / "THIRD PARTY" | "PREPAID" / "COLLECT" after total | "PPD" / "COL" after total | "P/C" box | A5 |
| Terminals, interline | none | DEST TERM, ORIG TERM; bottom boxes ORG C/L, C/L PRO NO, DEST C/L (`PYLE`, p. 63) | none | ORIGIN, DESTINATION, ADV / BEY SCAC | ORIG I/L, DEST I/L | A3, A5 |
| Item, declared class | "CL 100 ITEM 057300-03V" | "CL125 NMFC49880" (BOL echo) | "CLASS 70" in text | NMFC column `640000-09` | "NMFC #156600" | B4, C1 |
| Rated class | "EX70" column | "CLASS 70.0" | none | "CLASS" column | "CLASS 085" | B4 |
| Weight | column | column | column | column | column | C1 |
| Rate | cents per cwt, no point: `73317` | no point: `60080` | dollars: `391.89`; "M" = minimum | dollars: `106.84`; "MIN" | no point: `13289` | B2 |
| Discount | "DISC 89.5% -4,232.41" | "88.15% DISC" (2023); "DISCOUNT PERCENTAGE 9100" (2020) | "XPO LOGISTICS DISCOUNT SAVES YOU ($170.03)", no % | "84.00% DISCOUNT -4,186.64" | "Discount Allowed: 70.00% 2299.53-" | B2 |
| Minimum | "MIN", "ABSOLUTE MIN CHARGE ADJUSTMENT MCADJ" | "MIN FRT CHG", "MINIMUM FREIGHT CHARGE" | "M" | "MIN" | none seen | B3 |
| Deficit | "DEF111 AS500" | "AS WEIGHT 1,000 / DEFICIT 214" (p. 51) | none seen | none seen | none seen | B3 |
| Fuel | "FSC 30.3% 150.45" | "LTL FUEL SURCHARGE OF 22.00%" | "FSC FUEL SURCHARGE 30.50%"; volume bills "TLF …" with no % | "003570 LTL FUEL ADJUSTMENT 35.70" | "FUEL INCREASE 133.04", no % | B8, B9 |
| Accessorials | name + code: CCS, NYILD, DETND/140, SHDL/21, HCDS | name only: LIFTGATE SVC, PVT RESIDEN, NY DEL CHG, REDELIVERY | name + code: CBR reweigh fee, CBL BOL correction | 6-digit code + name: 005000 NOTIFICATION, 002550 INSPECTION | name: SORTING OR SEGREGATING, CORRECTED BILL OF LADING CHARGE | D1, C2 |
| Late fee | none | "PENALTY/TARIFF DUE" (2020) | LP1…LP6 lines | none | liquidated damages in printed terms | F1 |
| Carrier remarks | "W02/AUTH:Reweigh - See W&R certificate", "Z20DET/AUTH:Add detention" | "** PER GOOGLE EARTH THIS IS A PRA DLVY", "** CLASS INSPECTION PER W&I **" | "RE-WEIGHED PER WEIGHT CERTIFICATE" | "*** SHIPMENT REWEIGHED ***", "WAIVED INSPECTION" | "W & I REWEIGH CORRECTE WEIGHT 1070 LBS", "CORRECT AS BILLED", "ADDED SSC PER DR" | C1, D2 |
| BOL echo | "DONT BREAK DOWN PLT", "MUST DELIVER ON 7/15/24" | "'LIFTGATE DELIVERY", "*LIFTGATE DELIVERY *NY DEL CHG" | none seen | "UPS WORLDSHIP" | "PER LETTER FROM THE SHIPPER" | D2 |
| Dimensions | "RATED DIMENSIONS: 48X40X35", "ABF MEASURED CUBE" | cube rule on the bill (pp. 24-26) | none | each handling unit's dimensions, cube, density | handling units, dimensions | C1, B3 |
| Page count | none; bill can run onto the next page (pp. 75-76) | "1 of 1"; "1 of 3" with pp. 2-3 missing (p. 49) | "( continued on next page )" | "Page 2 of 15" (packet) | "Page 2 of 3" | A1 |
| Scan line | none | none | "712591246 0069565 6" = PRO, cents, check digit | none | none | A1 (2nd reading) |
| Total, amount due | "TOTAL AMOUNT DUE" | "TOTAL" row; "PAY THIS AMOUNT" can differ (§4) | "TOTAL" and "TOTAL DUE" | "AMOUNT DUE … COL" | "PAY THIS AMOUNT" | A1 |
| Reading | text layer | OCR; labels garbled, values in fixed order | 2021 image only; 2024 text layer | text (2023); OCR (2009-10) | fax scans, viewed | |

### 2.3 PDF TL and broker invoice
| Field | Werner Enterprises, direct (22-008) | Werner Logistics, to a broker (22-013) | Taylor (22-012) | USA Truck (22-015) | Wintzer, bulk (22-001) | TQL, broker (22-007) | RXO / Coyote, broker (22-011) | Checks |
|---|---|---|---|---|---|---|---|---|
| Invoice no. | "FREIGHT BILL NO." `39015347` | `WLM89131092` | "PRO. NO." `1848869A` | "ORDER #" `8065404`; barcode `8065404A` | `31769` | `26531517A` | `3341783401` (load + "01") | A2 |
| Dates | pickup, issue, delivery | invoice, due, pickup, delivery | delivered, shipped, invoice | invoice, due, ship, delivery | invoice, ship, due | invoice; pickup and drop dates | invoice; dates per stop | G1, D3 |
| Load / dispatch | "DISPATCH NO." | "Tour #" | "REFERENCE #" | none | "LD386284" | "[Load ID:168799693]" in the PO column | "Load #" | B6 |
| BOL / shipper no. | "SHIPPER NUMBER": `RETURN` | inside "Customer Ref #" | none | none | ticket `TKT370072` | none | "PU #s" | A6 |
| Equipment | tractor, trailer | none | tractor, trailer | trailer | none | trailer type, size | trailer | A6 |
| Miles | "MILES 154" | none (rate con: 1,432.07) | "332 Miles", "O-D/Routed 332/332" | none | none | none | none | B7 |
| Weight | 33000 | 44,000 | 43,529 | none | 19.74 tons | 25064 | none | B6 |
| Linehaul | "MISC. FREIGHT SHIPMENTS 266.88" | "LINEHAUL … FLT 2,800.00" | "FLAT RATE 993.96" | "LINE HAUL FLAT 2,089.00" | 19.74 × $16.50 | "FREIGHT 1,402.77" | "FR Flat Rate 1,325.00" | B6 |
| Fuel | "FUEL ADJ/MILEAGE 93.94" | none (all-in) | "$/MILE … .47" | "FUEL SURCHARGE FLAT 1,211.00" | "21% FUEL SURCHARGE 68.40" | none (all-in) | none | B8 |
| Accessorials | management fee, tolls, trailer, tractor use, minimum mileage | TONU $150 (p. 25, on the rate con) | none | "BORDER CROSSING FEE", "MEXICO CHARGE" | none | "UNLOADING 451.00" | none | D3-D7 |
| Payments, terms | "PREPAID" column; "PAY WITHIN 15 DAYS" | "Original Invoice"; due in 30 days | 15 days | "PPD / COL: UNKNOWN" | Net 10; 1.5% a month | 1.5% a month after 30 days | Payment lines −875 / +875; "AFTER 9/10/2025: 456.75" | A5, F1 |
| Reading | image; clean OCR | text | text | image | text with handwriting | text | text | |

### 2.4 Corrected and balance-due bills: what each carrier tells you about the change
| What | Where | Example | Checks |
|---|---|---|---|
| Difference only | SEFL "PAY THIS AMOUNT" on a BALANCE DUE print | 806625953: $110.23 on a $1,088.74 bill (02-002 p. 41) | A4 |
| Original and new totals | ABF "IMPORTANT NOTICE … original total charge was $326.60 … correct charge is $300.52, a reduction of $26.08" | 165261918 (01-001 p. 75) | A4 |
| Reason code | ABF `W02/AUTH:Reweigh - See W&R certificate`, `W01/AUTH:Restore original weight`, `Z20DET/AUTH:Add detention` | 01-001 pp. 18, 76 | C1, D3 |
| Amount paid and balance | XPO "AMOUNT PAID: US $150.00 / BALANCE DUE: US $1,151.48" | 266-489086 (21-005 p. 4) | A4, A3 |
| Weight before and after | TForce "WEIGHT DECLARED AS 04424 LBS. ACTUAL WEIGHT IS 04665 LBS." | 546903626 (21-015 p. 33) | C1 |
| Weight after only | XPO "RE-WEIGHED PER WEIGHT CERTIFICATE"; ODFL "REWEIGH CORRECTE WEIGHT 1070 LBS"; SEFL nothing (806625953) | 03-003 p. 16; 21-001 p. 12 | C1 |
| Original charges line | SEFL 2020 "ORIGINAL CHGS 150.15", "CONTINUED ON NEXT BILL" | 882685261 (02-002 p. 51) | A4 |
| Correction fee | XPO "CBR REWEIGH OF SHIPMENT FEE" $35.25 / $43.25, "CBL BILL OF LADING CORRECTION" $45.00; ODFL "CORRECTED BILL OF LADING CHARGE" $15.00 | 03-003 p. 15; 21-005 p. 8; 21-002 p. 17 | C2 |
| Audit trail with dates | ODFL "FBA … 8/08/07 FREIGHT BILL AUDIT", "… 11/02/07 CORRECT AS BILLED", "CBL … 2/18/05 … CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER" | 21-001 p. 11; 21-002 p. 17 | A5, D2 |
| Earlier invoicings | TForce / UPS "PREVIOUSLY INVOICED ON: 05/09/23 33631700 1118.82; 05/02/23 33614073 2369.67" | 21-015 p. 33 | A4, G1 |
| No reason at all | SEFL CORRECTED INVOICE: shipped 01/10/2022, billed 04/07/2023 (452 days), full total due | 896789802 (02-002 p. 63) | A4, G1 |

### 2.5 Statements of account
| Field | Seen in | Example | Checks |
|---|---|---|---|
| Statement no. and date, account | TForce, UPS, Estes, Mode, RXO | TForce "R1754408", 8-08-23 (21-015 p. 4) | none |
| Aging buckets | TForce, UPS | 0-30 / 31-60 / 61-90 / 91-365 / over 365 | F1 |
| Per row: PRO, ship date, reference, P/C, amount | TForce, UPS | `546903626 12-20-2022 MIA95055 P 1,118.82 REWEIGHED CHECK INVC` (21-015 p. 32) | A2, C1 |
| Bill date, BOL, PO, Adj/BD flag | Estes "Account Listing" | Adj/BD, Pro, Statement Date, Billed Amount, Freight Bill Date, Statement No., BOL (12 digits), PO, Terms, Balance (21-007 p. 4) | A4, G1 |
| Charges, cash posted, liquidated damages, remaining | ODFL | 600.19 / 528.19 posted / 72.00 open (21-010 p. 4) | A3, F1 |
| Accessorial codes, tariff, child account | YRC | `REWT`, `LFTD`, `APPT`, `DEF AS`; tariff `RDWY.499..300100`; bill, pickup and delivery dates (21-006 pp. 4-5) | C1, D1, B1 |
| Original, open, interest | Mode | 18% a year; age in days (21-014 p. 4) | F1 |
| Adjusted, applied, credited, balance, days past due, load no. | RXO | overpaid rows shown as (50.00) (22-011 p. 4) | A3 |
| SCAC fused to PRO, credit items | Kuehne+Nagel ledger | `RDWY349533831X`; item type A (credit) / I (invoice) (21-013 p. 8) | A2 |

## 3. 210 against PDF, field by field
| Field | In 210? | In PDF? | Notes |
|---|---|---|---|
| PRO, totals, line charges | yes | yes | 210 exact; PDF needs OCR on scans |
| Discount % | AAA Cooper, Estes as L5 text; not ODFL | ABF, SEFL, TForce, UPS, ODFL; not XPO | derive from DSC ÷ gross where missing (§4) |
| Fuel % | AAA Cooper, Estes text; not ODFL, not TL | all LTL PDFs except ODFL 2005 and XPO volume bills | TL fuel is per mile or flat |
| Rate unit | dollars per cwt; qualifier may lie (Estes `LB`) | cents per cwt, no point, at ABF, SEFL, ODFL; dollars at XPO, TForce | normalise by checking weight × rate = charge |
| Bill type, correction | B3-08 (unused in real files) | title or banner on every carrier's PDF | PDF is the only real evidence held |
| Carrier remarks, reasons | only if K1/L5 sent (K1 never in real files) | printed (ABF, SEFL, XPO, TForce, ODFL) | reasons decide C1/D2 disputes |
| BOL echo (special instructions, declared class) | no | ABF, SEFL ("'LIFTGATE DELIVERY", "CL150 NMFC 49880") | D2 evidence on the bill itself |
| Quote number | no | ABF, SEFL, XPO | B5 link |
| Dimensions, cube, density | no | ABF, TForce, ODFL, SEFL cube rule | C1, B3 |
| Delivery date | yes, but ODFL's is "estimated" | rarely (Werner, Taylor, USA Truck) | use the delivery receipt or 214 |
| Earlier invoicings | no | TForce, UPS reprints | only bill-side source of the first bill date |
| Interline partner and share | R3 (AAA Cooper) | SEFL C/L boxes, TForce ADV/BEY | A3 |
| Amount paid / open balance | no | XPO 2024, SEFL (difference), statements | read the statement |
| Uncoded charges | ODFL $24 + $11 | name printed on PDF | 210 alone cannot price-check them |

### 3.1 Where this differs from `data/doc-explanation.md` (as of 2026-10-10)
- **§1.3 "Freight bill", Format.** It says "ODFL stamps its own audit notes ('REWEIGHED PER WEIGHT CERTIFICATE', 'WAIVED INSPECTION')". Those two phrases are XPO's ("RE-WEIGHED PER WEIGHT CERTIFICATE", 21-005 p. 5; 03-003 p. 16) and TForce's ("WAIVED INSPECTION", 21-015 pp. 5, 33).
  - ODFL's notes on the pages viewed read "W & I REWEIGH CORRECTE WEIGHT 1070 LBS", "CORRECT AS BILLED" and "ADDED SSC PER DR" (21-001 pp. 11-12).
  - They are printed lines, not stamps (the catalogue's verify_note says the same).
  - The same "stamps" wording recurs in the balance-due paragraph.
- **Same paragraph: "Werner's TL invoice is one flat line plus fuel."** Neither Werner layout held matches.
  - Werner Logistics: one flat linehaul line with no fuel line (22-013 pp. 4, 12, 13).
  - Werner Enterprises: freight, fuel per mile with miles, management fee, tolls, trailer, tractor-use and minimum-mileage lines (22-008 pp. 4, 7).
- **§1.3 "EDI 210": "In return a 210 gives a code for every charge."** ODFL's Canadian bills carry two charge lines ($24.00 and $11.00) with no code and no description (19-001 ST 0005; 19-002 ST 0001; 19-003 PRO 00902528152). ODFL's base-freight lines also have an empty code field.
- **Same paragraph: only Estes is said to write the discount as text.** AAA Cooper does too, and it writes fuel as text: "LESS 78.00 PCT DISCOUNT", "Fuel Surcharge 29.00 PCT" (19-009).
- **"A shipper on EDI gets the balance-due bill as a second 210 … flagged in B3-08."** This is true of the guides, but no real 210 held shows it (0 of 82 transactions carry B3-08). FedEx's 4060 guide also has "PD", past-due billing, which is the EDI form of SEFL's 2025 reprints. Treat it as *assumed* for real traffic until a real balance-due 210 is seen.

## 4. Derived values (computed, never read)
1. **Discount % from a DSC dollar line.** ODFL PRO 00902527924 (19-001): 650 lb × $40.17/cwt = $261.11 gross. The DSC line is −$188.00, and 188.00 ÷ 261.11 = 72.0%. All 34 ODFL bills land on a whole percent and reproduce to the cent.
2. **Fuel % from a 405 line.** Same bill: net 261.11 − 188.00 = 73.11, and 12.79 ÷ 73.11 = 17.5%. Fuel is charged on net linehaul only. On PRO 00902527931 the $35 of uncoded lines is left out: 62.84 ÷ 369.66 = 17.0%, against 15.5% if they were included.
3. **Original amount = corrected total − balance due.** SEFL 806625953: 1,088.74 − 110.23 = 978.51, which equals the shipper's worksheet row 292 (`s5_check_AT_adversarial.md` §2.2).
4. **Implied original weight.** Same bill: the original net was $744.77 at a 90.30% discount, so gross = 744.77 ÷ 0.097 = $7,678.04. At $315.97/cwt that is 2,430.0 lb, against 2,720 lb re-billed. TForce prints both weights (4,424 → 4,665, +241 lb, +5.4%), so there it is read, not derived.
5. **Amount already paid = total − balance due.** XPO 266-489086: 1,301.48 − 1,151.48 = 150.00. XPO prints it too ("AMOUNT PAID", 21-005 p. 4), so the check confirms the reading.
6. **Short-pay from a statement.** ODFL (21-010 p. 4): 600.19 − 528.19 = 72.00 and 234.32 − 162.32 = 72.00. Two bills were each short-paid by exactly $72, which looks like one recurring deduction.
7. **Deficit weight.** ODFL PRO 00902527925: L3 rated weight 1,000 − (86 + 747) actual = 167 lb, which is the DAA line. AAA Cooper PRO 37685699: 8,580 + 1,420 = 10,000.
8. **TL fuel per mile.** Werner 39015347: 93.94 ÷ 154 mi = $0.61/mi (pickup 01/13/2023). Werner 39060407: 97.02 ÷ 154 = $0.63 (01/30/2023). Taylor prints it: 332 mi × $0.47 = $156.04.
   - Taylor's flat $993.96 plus that fuel equals the broker's all-in $1,150.00, so B6 compares totals.
   - TQYL shows why a percentage is meaningless: two bills on one lane carry the same $301.95 fuel on linehauls of $2,600 and $2,100 (19-034).
9. **Late fee base.** XPO 2024: (1,327.50 + 401.57 + 43.25 + 45.00) × 10% = $181.73 per LP line (21-005 p. 8). XPO 2021: (881.75 + 275.55) × 1.5% = $17.36 (03-003 p. 7); on p. 4, 665.65 × 1.5% = $9.98 is billed as $10.00 (a floor, *assumed*). The rate changes, so it must come from the tariff in force (XPO Tariff 199). RXO: 450.00 × 1.015 = $456.75 after the due date.
10. **Re-rate on a reprint.** UPS Freight PRO 028582002 (04-006 pp. 15-16):
    - priced delivery receipt: $47.25/cwt, less 86%, plus 11.80% fuel = $412.82;
    - 2010 "COPY OF FREIGHT BILL": $37.80/cwt, less 65%, plus 11.80% fuel = $825.64.
    - Same weight, double the money, no reason printed. The software can show the change, but not why it happened.
11. **First-bill date from the reprint list.** TForce 610384246: shipped 03/03/23, earliest listed invoicing 03/15/23 (12 days later), then 06/07/23 (21-015 p. 5). This is the date the shipper's 180 days are counted from, approximately (the statute says receipt).
12. **Interline share.** AAA Cooper R3-08: $126.98 of $325.60 = 39.0% to NEMF (19-009).
13. **Rate unit.** SEFL "60080": 509 lb × 600.80 ÷ 100 = $3,058.07, so it is $600.80/cwt. ABF "73317": 645 × 733.17 ÷ 100 = $4,728.95. ODFL PDF "13289": 2,472 × 132.89 ÷ 100 = $3,285.04. The unit is decided by checking weight × rate against the printed charge, never assumed.

## 5. Join keys
### 5.1 Keys and how they are written
- **PRO.**
  - ODFL: 11 digits with leading zeros (`00902527924`).
  - XPO: dashed on the face (`712-591246`), undashed in the scan line.
  - YRC statements: dashes plus a check character (`648-358429-6`, `670-438395-X`).
  - Kuehne+Nagel: SCAC glued on (`RDWY349533831X`).
  - Taylor and TQL: a letter suffix (`1848869A`, `26531517A`).
  - RXO: the load number plus "01" (`33417834` → `3341783401`).
  - **Rule:** strip non-alphanumerics and any SCAC prefix, then match with and without leading zeros, check character and suffix.
- **BOL.**
  - In the 210: B3-03, and N9*BM at AAA Cooper.
  - The same shipper numbering (`0028074000…`) appears at both ODFL and AAA Cooper, so the BOL is the cross-carrier key.
  - Missing: Estes 210 sends `NS`; UPS and TForce print "B/L NO. NONE".
- **PO.** N9*PO can repeat (7 on one ODFL bill). ABF prints the PO in remarks while the field is blank (p. 18). TQL puts its load ID in the PO column.
- **Quote.** ABF "PQ SCHEDULE NO", SEFL "QUOTE #", XPO "QN#". ABF even prints a mismatch notice: "The invoice amount differs from the quoted amount on Quotation LDG91V2074 … SPECIAL HANDLING SERVICES - LUMPER that was not included in the quote" (01-001 p. 75).
- **Dates.** Ship date (210 B3-12 or G62*86; PDF), invoice date (B3-06; SEFL DATE BILLED; ODFL Invoice Date) and statement date are three different things. A link uses the ship date and keeps the others for the clock.
- **Bill type.**
  - 210: B3-08 (unused in real files).
  - PDF: the title, but it is not reliable on its own. ODFL's re-bill to a new payer is titled "ORIGINAL INVOICE" (21-002 p. 17), and ABF's p. 77 is an ORIGINAL INVOICE carrying reweigh codes.
  - Corrections are found by **PRO + a changed amount or bill-to**, not by the title.
- **TL.** Load or dispatch number, rate-confirmation BOL, trailer number, pickup date.
  - Werner Logistics' "Customer Ref #" mixes them in a different order on each bill and cuts them at a fixed width: `502464982|IDB61769|954`, `952909`, `963813|504846313|IDB62` (22-013 pp. 4, 12, 13).
  - Parse it into tokens and match any one.
- **Statement line.** PRO plus open amount. Estes also gives the freight bill date and an Adj/BD flag.

### 5.2 Failure cases seen
- **Reprints are not new bills.**
  - SEFL's 2025 "PAST DUE INVOICE" prints repeat 2023 balance-due bills with a new DATE BILLED (pp. 23-35 against pp. 36-48).
  - UPS and TForce copies list the same PRO 2-4 times under "PREVIOUSLY INVOICED ON".
  - ODFL faxes say "DUP" with a print date 11 months after shipment (21-001 p. 11).
  - FedEx's guide codes this "PD", past-due billing (12-052).
  - **Rule:** one PRO is one bill; each print is an event with a date and an amount.
- **Same amount, different bill.**
  - ABF: 23 of 101 bills share both total and ship date with another (9 groups; five at $256.54 on 08/07/2024).
  - TQYL: 34704009 and 34703959 are both $4,319.60 on one lane, picked up 12-07 and 12-06. 34688921 and 34688904 are both $2,401.95 (19-034).
  - Werner: 39060407 and 39100828 are both $834.83, same date and lane; only the tractor, trailer, dispatch number and weight differ (22-008 pp. 7, 10).
  - Mode: two $3,698.75 invoices on 7/18/2023 (21-014).
  - **Rule:** key on PRO + BOL (or load), never amount + date (AK §3.2, A2).
- **Pages split or missing.**
  - ABF's correction notice runs onto the next page (pp. 75-76).
  - SEFL p. 49 says "1 of 3", but its pages 2-3 are not in the exhibit. Its PAY THIS AMOUNT ($809.44) does not equal its printed lines ($1,019.77 + $117.27 + $161.89). Pages 50 and 51 also fail to reconcile on one page.
  - **Rule:** read the page counter, group pages by PRO, and do not run A1 on an incomplete bill.
- **Missing shared key.** Werner 39015347 prints shipper number "RETURN", while its BOL says 104310 (22-008 pp. 4-5). The only common keys are trailer 64082, 01/13/2023 and the 33,000 lb weight.
- **Summary dates differ from invoice dates.** TQL 26737009 is dated 01/11/2024 on the invoice and 1/26/2024 on the claim's list (22-007 pp. 5, 8).
- **Payer changes under one PRO.** ODFL 02902161435 was billed to the consignee ($2,412.67), refunded, and re-billed to the vendor ($1,133.55) (21-002 pp. 13, 17). A bill-to change on a known PRO is an A5 event, not a duplicate.

## 6. Gaps: facts the checks need that no bill-side document carries
- **The base rate** (CzarLite or SEFL-0550): the bill shows the rate used, not the right one (B2). AAA Cooper's L7 names the tariff and date, which says *which* table to buy.
- **The fuel table in force:** derived fuel % has nothing to be compared with (B8).
- **The agreement:** discount, minimum, FAK, accessorial exceptions (B1-B4, D1).
- **TL miles and the mileage basis:** absent on five of the seven TL and broker layouts, and on every TL 210 (B7). Rate-con miles exist (22-013: 1,432.07) but are not on the invoice.
- **Whether an accessorial was ordered** (BOL ticks, delivery receipt) and detention times (D2, D3). ABF bills "DETND/140" with no arrival or departure time.
- **The weight certificate** behind a reweigh. ABF, XPO and SEFL point to it without attaching it; only TForce prints both weights (C1).
- **The pre-correction weight and amount** when only the correction survives: XPO and SEFL corrected prints.
- **The first bill date** for carriers without a reprint list: SEFL corrected prints, XPO, ABF (G1).
- **What was actually paid:** the shipper's AP record (A3, F1). Statements show the carrier's view only.
- **Reasons for uncoded or unexplained changes:** ODFL's $24/$11 lines, the UPS 86% → 65% re-rate, TForce's 2,369.67 → 1,118.82 re-invoice.
- **Delivery date and time** on LTL bills (ODFL's 210 date is estimated): needed for E1 and D3. It comes from the delivery receipt or a 214.

## 7. Recommended reading order, bill side [our call]
| Field | Trust first | Fallback | Last resort |
|---|---|---|---|
| PRO, line charges, total | 210 | PDF text layer | OCR, cross-checked against the scan line (XPO) and the column sum |
| Discount %, fuel % | PDF printed % | 210 L5 text | derived from dollar lines (§4.1-4.2) |
| Rate unit | weight × rate = charge test | carrier profile | never assume |
| Bill type, correction | PDF title plus a changed amount on a known PRO | 210 B3-08 | statement Adj/BD or remarks (Estes, TForce) |
| Reason for a change | PDF carrier remarks or codes | 210 K1/L5 | ask the shipper (C1/D2 question) |
| Ship date | 210 B3-12 or G62*86 | PDF | BOL |
| Bill date for the clock | earliest of: 210 B3-06 of the first 210 for the PRO, PDF bill date, first "PREVIOUSLY INVOICED" entry, Estes "Freight Bill Date" | statement date (flag as late) | none: mark the clock unknown |
| Delivery date | delivery receipt or 214 | 210 B3-09 only if qualifier 035 | none |
| BOL, PO, quote | 210 N9/B3-03 | PDF fields and remarks | tokenised reference strings (Werner) |
| Payer, terms | 210 B3-04 + N1*BT | PDF terms box | statement P/C |
| Open balance, paid | statement | XPO / SEFL balance lines | none |
| TL miles | invoice (Werner, Taylor) | rate confirmation | mileage engine (licensed) |

## 8. Claim ledger
| # | Claim | Tag | Evidence |
|---|---|---|---|
| 1 | 82 real or assumed-real 210 transactions; line charges = B3-07 = L3-05 in all 82 | verified | 19-001…19-015, 19-033…19-035; parser re-sum |
| 2 | ODFL 210 rate is $/cwt (40.17 PH); charges in cents | verified | 19-001 ST 0001 |
| 3 | All 34 ODFL bills reproduce with discounts {65,68,70,72,77}% and fuel {16.0,17.0,17.5}% of net | verified | 19-001…19-008; our calc |
| 4 | ODFL B3-10 = 017 (estimated delivery) on all 34 | verified | 19-001…19-008; code meaning 12-043 |
| 5 | No real 210 fills B3-08 or K1 | verified | segment survey of 19-001…19-015, 19-033…19-035 |
| 6 | B3-08 codes: 3M AR/BE; TForce BD/RC; FedEx Freight BD/CO/PD; FedEx 4060 AD/BD/PD/RB | verified | 12-039 p. 4; 12-045; 12-043; 12-052 |
| 7 | AAA Cooper and Estes write discount and fuel % as L5 text; L1-19 unused | verified | 19-009, 19-015 |
| 8 | Estes labels a per-cwt rate "LB" | verified | 19-015: 810 × 298.86/100 = 2,420.77 |
| 9 | ODFL Canadian bills carry two uncoded L1 lines ($24, $11) | verified | 19-001 ST 0005; 19-002; 19-003 |
| 10 | AAA Cooper uses CZAR 910 (78%, NEMF interline) and SMC ZRH (87.2%, direct) for one shipper | verified | 19-009…19-014 |
| 11 | TL 210s are sent by BPTS; L0-08 piece counts are junk; fuel is flat | verified | 19-033…19-035 |
| 12 | SEFL sample form has 27 named fields including PageNum and TtlPageNum | verified | sefl.com/vspdfdocs/shipping_invoiceExample.pdf |
| 13 | SEFL p. 49 is page 1 of 3 and its pay amount ≠ printed lines | verified | 02-002 p. 49 (viewed) |
| 14 | ABF corrected notice prints original, new total and reduction | verified | 01-001 p. 75 |
| 15 | 23 of 101 ABF bills share total and ship date in 9 groups | verified | 01-001 by script |
| 16 | TForce prints declared and actual weight on a reweigh | verified | 21-015 p. 33 |
| 17 | UPS 028582002: DR $412.82 at 86%; copy $825.64 at 65% | verified | 04-006 pp. 15-16 (viewed) |
| 18 | ODFL re-bill to vendor titled "ORIGINAL INVOICE" | verified | 21-002 p. 17 |
| 19 | XPO late fees: 1.5% (2021) and 10% (2024) of the pre-fee total | verified (arithmetic); $10 floor *assumed* | 03-003 pp. 4, 7; 21-005 pp. 4, 8 |
| 20 | Werner direct bills: miles printed; two $834.83 bills differ only in equipment, dispatch no. and weight | verified | 22-008 pp. 4, 7, 10 |
| 21 | Werner direct bill shipper no. "RETURN" vs BOL 104310 | verified | 22-008 pp. 4-5 |
| 22 | Werner Logistics invoiced 92 days after delivery against a 45-day rate-con rule | verified | 22-013 p. 4 |
| 23 | Taylor flat + per-mile fuel = rate-con all-in $1,150 | verified | 22-012 p. 4; catalogue note |
| 24 | TQL invoice dates differ from the claim list's dates | verified | 22-007 pp. 5, 8 |
| 25 | Mode interest ≈ 18%/yr over 75 days, 1-4 cents off | verified (arithmetic); day-count rule *assumed* unknown | 21-014 p. 4 |
| 26 | ODFL short-pays of $72.00 on two bills | verified | 21-010 p. 4 |
| 27 | Interpretation that the two $72 short-pays are one recurring deduction | assumed | 21-010 p. 4 |
| 28 | A balance-due 210 arrives as a second 210 with the same PRO | assumed (guides only) | 12-043, 12-045, 12-039 |
| 29 | The first "PREVIOUSLY INVOICED" entry is the original bill date | assumed | 21-015 p. 5 (numbering pattern only) |
