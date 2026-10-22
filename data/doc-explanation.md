# The documents behind a freight price dispute, form by form

Written 2026-10-10 for the founders, from check AT (`research/s5_check_AT_c09_document_dataset.md`) and its verification (`research/s5_check_AT_adversarial.md`). It explains each document in the chain, whether its format is shared across firms or belongs to one firm, what it decides in the worked SEFL mismatch (AT §7), what `data/` holds, and what is missing with its cost. Nothing here is decided; the open points stay in AT §8.

Revised the same day after a fact-check against the files and the web (the first version is in git, commit 9e65703). The main change: the BOL does not decide a residential charge; whether a dwelling stands on the delivery premises does (§1.1-§1.2). §4 is the pipeline: what the software pulls from each document, in what order, and the math that decides whether a line is worth disputing. Two sentences were corrected on 2026-10-10 while writing `doc-exploration.md` (the fact-by-fact lookup map): §1.2 on what evidence overturns a reweigh or reclass, and §4.5 step 1 on the carrier's default class when the BOL is silent.

Freight terms used: **LTL** (less-than-truckload: pallets sharing a trailer, priced by weight and class); **TL** (truckload: one shipper's load, priced flat); **PRO number** (the carrier's bill number); **cwt** (hundredweight, 100 lb); **NMFC** (the National Motor Freight Classification, which assigns every commodity a class from 50 to 500); **FAK** ("freight all kinds", an agreement rule that rates several classes as one); **accessorial** (an extra service charge: liftgate, residential delivery, redelivery, detention); **EDI** (electronic data interchange, machine-readable business documents in the X12 standard); **BOL** (bill of lading); **W&I** (weight and inspection).

## 1. The chain, in the order the paperwork is created

### 1.1 Before the shipment: the price is set

**Pricing agreement (rate agreement).**
- *Purpose:* the contract between one shipper and one carrier. It names the base tariff the discount applies to, the discount by lane and direction, the FAK, the per-shipment minimum after discount, and exceptions to the accessorial prices.
- *Format:* per firm, with no common layout. SEFL uses "rating item" tables of three pages per version (lanes, then definitions and Item 610 floors); YRC a 40-section contract (First Brands); Home Depot a lane-pricing schedule; Walmart a contract whose "Lanes and Rates" appendix is an empty cover page; GM a terms-and-conditions document. Three of the shippers' contracts held shut the carrier's tariff out except where named (Kroger, Walmart, Home Depot); SEFL's pricing and the YRC–First Brands contract let the tariff fill every gap.
- *In the dispute:* the source of truth for the price, in the version in force on the ship date. SEFL issued three (01/15/2021, 06/08/2022, 04/12/2023), so the 2023-05-15 shipment falls under the third, which says 88.15% off (unchanged from 2022), class 70 under the FAK and an absolute minimum of $152 on the Oregon lane; the separate accessorial-exceptions page (rows effective 4/7/2021) sets liftgate at $55.
- *Held:* SEFL's in three dated versions (set 02); YRC-First Brands, GM, Schneider, Kroger, CJ Logistics (set 11); Home Depot's contract with lane pricing and Walmart's contract without its lanes (set 23).

**Rules tariff.**
- *Purpose:* the carrier's public rulebook, which fills every gap the agreement leaves: accessorial prices, reweigh and reclass fees, cubic-capacity minimums, the overcharge-claim window (SEFL's tariff has none, so the statute governs), late-payment penalties, discount forfeiture on unpaid bills.
- *Format:* per firm in wording, item numbers and prices, but every carrier's covers the same family of items. Some carriers date each item (SEFL, Estes, R+L; FedEx and ODFL mark revised items), others date the whole issue (ABF, XPO, TForce), so the software must use the item or issue in force on the ship date: ABF billed its California surcharge at $22 in 2024, while the issues held say $27 (2025) and $34 (2026), and ABF 111-AS applies only to shipments from 2024-09-09.
- *In the dispute:* SEFL 1090 Item 753 (dated 2022-12-16, so in force for the 2023 bills) applies the residential charge "only when the carrier is requested or required to make … delivery at a private residence", and defines a private residence as "the entire premises on which a dwelling for living is located". The price is $7.60/cwt, with a $94 minimum and a $575 maximum. The shipper "should" mark the BOL, but leaving it off "will not relieve the shipper and/or consignee from the responsibility of paying". So the charge turns on one fact, whether the delivery premises is a private residence (any premises with a dwelling), apartment, boat slip or estate, and not on the BOL. The agreement's accessorial-exceptions page (set 02, p. 22) has no residential line, so the tariff price applies. The $94 line on bill 807148067 is priced exactly by this item (509 lb × $7.60/100 = $38.68, raised to the $94 minimum). So are the other eight residential lines in set 02 (§1.2, BOL).
- *Carriers define "residence" differently* (set 13): Estes and R+L exclude the part of a premises "where commercial or business activity is conducted that involves the sale of merchandise or services to the walk-in public"; ABF, XPO, FedEx Freight and Dayton count home-based businesses and the business part of the premises as residential; TForce charges if either its system or the actual address is residential "regardless of a shipper's designation", and "If an address can be construed as either residential or commercial, then it will be considered a Residence"; ODFL treats a consignment to a residential address as a request; SEFL says nothing about a business on the premises. Estes carries the same "will not relieve" sentence as SEFL.
- *Held:* 28 files: 26 tariffs from 15 carriers, several in dated versions, and 2 GSA publications (set 13).

**Base rate tariff.**
- *Purpose:* the table of undiscounted class rates per cwt, by origin, destination and class, that the agreement's discount is taken from.
- *Format:* proprietary. SEFL-0550 is SEFL's own; CzarLite is SMC3's neutral table that many agreements reference.
- *In the dispute:* without it the software can check that the printed gross equals weight × the printed rate ($600.80/cwt × 509 lb = $3,058.07), but not that $600.80 was the right rate for Miami to Sisters, class 70.
- *Held:* none.

**Fuel surcharge table.**
- *Purpose:* for LTL, the carrier's weekly percentage, keyed to the EIA/DOE diesel index with that carrier's own bands and effective weekday. Truckload fuel is often dollars per mile (Werner, Taylor, FedEx FTL). A contract can carry its own table: First Brands' contract with YRC gives 15.30% at $3.66-3.71, where ABF's tariff (a different carrier; no YRC table is held) gives about 31%.
- *Format:* per firm, including what the percentage applies to: ABF and Estes exclude accessorials, while FedEx applies it to "other services which consume fuel".
- *In the dispute:* 22.00% × net $362.38 = $79.72 is correct arithmetic, but whether 22.00% was SEFL's figure for the week of 2023-05-15 cannot be checked, because no 2023 copy of SEFL's table was found (none in `data/`, none in the Wayback index). The billed level is at least consistent: every 2023-05-15 row in the shipper's worksheet works out to 22.0%.
- *Held:* current tables (DOE, GSA, FedEx Freight LTL and TL), one Estes capture from 2023-03-27, the EIA weekly diesel series (set 14). No 2023-24 captures for ABF, SEFL, ODFL, XPO or Saia.

**Rate quote.**
- *Purpose:* a carrier's priced quote for one shipment. Its number is printed on the bill (CWEN3E465 on the primary example).
- *Format:* per firm.
- *In the dispute:* quote-to-bill matching (check B5) would show whether the residential charge was in the quoted price. The quote is not in the Exist exhibit.
- *Held:* no quote document. The six files tagged B5 are ABF bills that print a quote number (82 distinct) and ABF's own notes on why a bill differs from its quote (27; a note can give several reasons, and 21 name a lumper), plus five court filings in Central Freight v. Amazon. SEFL charges $35 to add and apply a spot quote number that was not on the original BOL (Item 360-5 ¶6, a corrected-BOL request), so a quote missing from the BOL can still be applied, for a fee.

**Rate confirmation (TL only).**
- *Purpose:* the broker's or carrier's one-page agreement for one load: flat linehaul, fuel, and the detention, layover, truck-ordered-not-used and lumper terms.
- *Format:* one layout per broker, each with its own free hours and hourly prices (TQL, rate confirmations filed in 2025: $25-30 an hour after 3-4 hours, layover $250-300, TONU $150 after 2 hours; Coyote's broker–carrier agreement: $25 an hour after 2 free hours, capped at $150 per location, with in/out times on the BOL or another shipping document the broker accepts; a broker/carrier agreement between a small carrier and U.S. Xpress Logistics: $50 an hour from 2 hours after the appointment time).
- *In the dispute:* for TL it plays the role the pricing agreement plays for LTL. The TL invoice is checked line by line against it.
- *Held:* 12 files in set 10 (11 rate confirmations or load tenders, one broker-carrier agreement); packets of rate con + invoice + BOL (set 22). Every rate confirmation held is broker-to-carrier, so none shows what a shipper agreed to pay a broker. The only shipper-side agreed TL price held is an EDI 204 tender (Seaboard Foods, $2,377.08, set 19). What shippers were billed is held: TL carrier invoices to shippers and TQL's invoices to one shipper (set 22).

### 1.2 At pickup and delivery: the facts are recorded

**Bill of lading (BOL).**
- *Purpose:* the shipper's own description of the shipment at pickup: pieces, weight, class, NMFC item, delivery instructions, prepaid or collect, who pays.
- *Format:* the VICS/GS1 form is a shared standard, followed loosely, with carrier variants and handwriting.
- *In the dispute:* it is evidence for the $94, not the deciding document. Item 753 says the shipper should mark residential delivery on the BOL, and that leaving it off does not relieve it of the charge. If "residential" was on the BOL, the shipper admitted it and the charge stands. If it was not, that alone wins nothing: the shipper has a case only if there is no dwelling on the delivery premises. Under SEFL's wording a shop on the same lot as a house is still a residence; under Estes's or R+L's, the walk-in retail part of it is not (§1.1, rules tariff). What the BOL does show is what was ordered. SEFL's bill reprints the BOL's special instructions, and bill 807148067 shows "'LIFTGATE DELIVERY" and the quote number but no residential request. For the second example it holds the declared weight (2,430 lb implied) against the 2,720 lb billed. The 2,430 is implied by the shipper's worksheet row for the original bill: $744.77 freight = 24.30 cwt × $315.97 × (1 − 90.30%), and $1,088.74 − $110.23 = $978.51 original total. That the BOL itself shows 2,430 is *assumed*. The bill also reprints the shipper's declared classes ("CL150", "CL125 NMFC 49880"), rated at 70 under the FAK. It is absent from the Exist exhibit.
- *The residential pattern in set 02:* 9 of the 62 distinct SEFL bills carry a residential line, $1,587.44 in all. Every one is priced exactly by Item 753: the $94 minimum on 320, 509 and 900 lb; $7.60/cwt on 1,315, 1,460, 1,838, 2,408 and 2,590 lb; the $575 cap on 8,920 lb (which would be $677.92 uncapped). All seven 2023 lines came on balance-due bills (pp. 46, 82, 84, 90, 91, 93, 94), three of them printed "per Google Earth". One Ocean City, MD consignee was charged as a residence on all three bills held for it, and SEFL's own 2020 bill (p. 60, which also prints a partner carrier's "CORR REPT") names it "OCEAN WAVES CITY WHSE", a warehouse. Its 2023 bill (p. 94) hit the $575 cap on 13 pallets. The shipper's worksheet has no residential column and checked none of the nine.
- *Held:* the blank VICS form and uniform BOL terms (set 15); filled BOLs for XPO (set 03), UPS Freight (sets 04, 06), the TL packets (set 22), Winn-Dixie's wrong-payer BOL (set 21).

**Delivery receipt (proof of delivery).**
- *Purpose:* the carrier's copy signed at delivery, with date, time, and sometimes in/out times for detention.
- *Format:* per carrier.
- *In the dispute:* it would show who signed for the freight and whether with a company stamp or name, which is evidence the consignee is a business but not proof that no dwelling stands on the premises (Item 753's test), and when the driver arrived. For the redelivery example (bill 807307041) it would show the first attempt on 05/25/2023.
- *Held:* XPO (set 03), Yellow (set 05), ODFL and others (set 21), Delphi's UPS Freight receipts (set 04).

**Weight and inspection certificate.**
- *Purpose:* the carrier's record of a reweigh or re-class: scale or dimensioner reading, dimensions, the inspector's note.
- *Format:* per carrier or per W&I vendor.
- *In the dispute:* in the second example the weight rose from 2,430 to 2,720 lb on a balance-due bill with no inspection note on either print, so the first ask in a claim is this certificate. Where SEFL did inspect, the bill says so ("** CLASS INSPECTION PER W&I **", p. 35). On weight and class the carrier's legal-for-trade reading beats the BOL: NMFC Item 250100 says "Freight charges must be assessed on the actual gross weight of the shipment", and the uniform BOL terms bill "the articles actually shipped". What evidence overturns a carrier's reading is defined for a reclass and only loosely for a reweigh (checked 2026-10-10): for class, "an invoice or packing slip along with a pre-printed specification sheet or catalog page, which lists the commodity description, weight, and shipping dimensions" (SEFL 170 Note 3; Estes 170 Note C; XPO 205 the same), and TForce refuses an edited copy of the BOL; for weight, "satisfactory proof" (Estes 992 ¶4), "documentation that the weight was in error" (FedEx 980 ¶3), and the claim forms ask for a certified weight ticket or the vendor's invoice (YRC F-154, ABF, FedEx, set 16). FedEx 980 ¶2 is the only item that promises the shipper a copy of the weight verification on request. ABF will get a certified public-scale weight on request for $317.17 plus the scale's fee in its 2026 issue ($282.81 in 2025; Item 992 ¶5), and a mover's certified-scale certificate was filed against a Yellow reweigh (set 23), outcome not shown. Certificates carry arithmetic that can be wrong. UPS Freight's inspection certificate for PRO 406858966 prints a density of 20.08 lb/ft³, which is the BOL weight (4,117 lb ÷ 205 ft³); its own weight gives 23.54. A Holland certificate (tendered 151, actual 360 lb) fits a BOL in kilograms read as pounds; read correctly, the gap is about 30 lb against the BOL's 149.59 kg total, or about 70 lb against its lines, which sum to 131.49 kg (*assumed*).
- *Held:* carrier-issued certificates: UPS Freight weight certificates and Freight Inspection Certificates (set 04: 43 weight-certificate pages and 6 inspection-certificate pages, 4 typed and 2 older handwritten, across all nine bill files; page-level count); a TForce weight certificate and cube certificate (21-015 pp. 36-37; its 537.33 ft³ recomputes exactly from the six pallets' dimensions); a Holland W&I weight correction (21-006 p. 15). Also a shipper-side weight certificate attached to a GlobalTranz reweigh dispute against Yellow (set 23); a W&I vendor's invoice to NEMF (set 24); NTEP type approvals for two parcel-size dimensioners, too small for pallets (set 15). No certificate names its device or its NTEP number.

### 1.3 After delivery: the money is asked for

**Freight bill (the invoice).**
- *Purpose:* the carrier's demand for payment: the shipment facts, each charge line, discount, fuel, total, due date.
- *Format:* per firm in layout, charge codes and which dates are printed. No two carriers' bills look alike. SEFL publishes a sample invoice (sefl.com/vspdfdocs/shipping_invoiceExample.pdf, dummy data dated 2003, the same layout as the 2023 Exist bills). It has no explanations, but it is a PDF form whose fields are named (ProNumber, BillType = "ORIGINAL INVOICE", BLNum, ShipDate, BillDate, DueDate, DetPieces, DetDescr, DetTypeCharge, DetWeight, DetRate, DetRevenue, Amount and others), so it is a free field map of SEFL's layout. No other carrier's sample was found. SEFL's 2020 layout writes "DISCOUNT PERCENTAGE 9100" or "9100 DISC" for 91.00%; its 2023 layout prints "88.15% DISC", so one carrier has two layouts. Both print rates without the decimal point ("60080" for $600.80/cwt; "65255." in 2020). ABF prints the tariff code ("Tariff: AOD000") and deficit weight ("DEF163 … ALLOWS LOWER CHARGE AT HIGHER WEIGHT"); XPO prints one discount line, "M" for a minimum and "RE-WEIGHED PER WEIGHT CERTIFICATE"; TForce prints "WAIVED INSPECTION" and both the declared and actual weight; ODFL prints its own audit lines ("W & I REWEIGH CORRECTE WEIGHT 1070 LBS", "CORRECT AS BILLED", "ADDED SSC PER DR"); UPS Freight bills of 2008-10 are mostly scans, read through the OCR in `derived/ocr/` (the faxed bills in the dataset are ODFL's of 2004-08); Werner bills in two layouts: one all-in linehaul line with no fuel (Werner Logistics), or freight plus a "FUEL ADJ/MILEAGE" dollar line, the miles (154) and four or five more lines (Werner Enterprises; $0.61 a mile is derived, not printed); Wintzer bills per ton. Rates print in dollars at XPO and TForce but in cents with no decimal point at ABF, SEFL and ODFL, so the unit is settled by testing weight × rate against the printed charge.
- *In the dispute:* this is what the software reads. On the primary example every line the agreement prices reconciles to it: 88.15% off, class 70 under the FAK, liftgate $55. The gross rate ($600.80/cwt) and the 22.00% fuel cannot be checked, because no base tariff or 2023 SEFL fuel table is held (§1.1). The line the carrier added is priced exactly by Item 753, so the question is whether it applies, not what it costs. SEFL's bills also reprint parts of the BOL: special instructions ("'LIFTGATE DELIVERY" on 807148067; "'ARRIVAL NTC" on 806373725, p. 24), the quote number and, on some bills, the shipper's declared classes ("CL150 NMFC 49880-", pp. 24 and 41).
- *Held:* 101 ABF bills with a text layer (set 01); 62 distinct SEFL bills as scans (set 02); 6 XPO invoices (set 03); 853 pages of UPS Freight bills, BOLs and delivery receipts, mixed (set 04); ODFL, XPO and TForce bills (set 21); TL invoices from Werner, USA Truck, Wintzer, Taylor and broker invoices from TQL and RXO (set 22).

**EDI 210 (and 214 status, 204 tender).**
- *Purpose:* the same invoice as a machine file, sent carrier to shipper.
- *Format:* the X12 segment skeleton (ISA/GS/ST, B3, N1-N4, LX, L5, L0, L1, L7, L3) is shared, so one parser reads every carrier's envelope, provided it takes the separators from the ISA's own characters, not from fixed widths: the three truckload files sent to Target carry a 107-character ISA. The charge mapping is per firm: Estes and AAA Cooper write the discount and fuel percentages as text ("DISCOUNT 84.0%"; "LESS 78.00 PCT DISCOUNT", "Fuel Surcharge 29.00 PCT") beside a negative discount line; ODFL sends the discount as a bare negative line (code DSC) and fuel as a dollar line on code 405, neither with its percentage, so both must be worked out (on ODFL's first bill, $188.00 off $261.11 is 72.0%, and $12.79 on the $73.11 net is 17.5%). Rates are in dollars per cwt and every carrier's charge field is in cents (an X12 rule, not an ODFL one). Estes labels its per-cwt rate "LB" (per pound): 8.10 cwt × $298.86 = $2,420.77, the printed charge; read per pound it would be $242,076.60. AAA Cooper names the base tariff in L7 (`L7*1*CZAR*910`), TL carriers bill a flat linehaul (code 400, 0.00 in the rate field) plus a fuel dollar line (FUE) and coded accessorials (LUM, LAY, STOP, STC, TONU). Versions run 4010 to 4060, and shippers publish their own inbound maps (3M rejects negative amounts, on line charges as well as the total, so the negative discount lines of ODFL, AAA Cooper and Estes must be re-mapped for it; Insight requires a proof-of-delivery segment).
- *In the dispute:* the core fields are the PDF bill's, already structured, but not all of them. Percentages may be missing (ODFL). The carrier's printed reason ("PER GOOGLE EARTH …", "CLASS INSPECTION PER W&I") arrives only as free text: in the optional K1 remarks segment (30 characters a field), which 3M requires on balance-due bills and no real 210 held uses, or in an L5 line, as Estes sends its remarks. No 210 carries the BOL, the delivery receipt or a weight certificate. Those come by a separate channel: Pitt Ohio sends the images by FTP alongside its 210s, and Kuehne+Nagel has a document API. TForce's guide says that once EDI invoicing starts, "copies of the delivery receipts or bills of lading are no longer mailed to the customer". In return a 210 codes most extra charges (405 or FUE fuel, DSC discount, LUM, LAY, TONU; RES residential appears in the TForce and FedEx guides, not in a real file held). Lines with no code: the base-freight lines of all three LTL carriers (ODFL, AAA Cooper, Estes), AAA Cooper's deficit-weight lines, and ODFL's $24 and $11 lines on its three Canadian bills. ODFL marks its 210 delivery date as estimated (code 017) on all 34 of its bills, so the actual date must come from the delivery receipt or a 214. Every real 210 held adds up: in all 82 invoices the lines equal the total. The carriers' guides define a balance-due or corrected 210 flagged in B3-08 ("BD" at TForce and FedEx Freight; 3M asks for "AR" with the reason in K1). None says the PRO is reused (FedEx's parcel guide gives a late-fee invoice its own number and cites the original in L11); reuse of the PRO is seen only on PDF prints (SEFL, ABF, XPO, TForce). None of the 82 real 210s fills B3-08 or K1, so the EDI form of a correction is unseen.
- *Held:* 36 files (set 19). 26 are real: 210 invoices from ODFL (8) and AAA Cooper (6) to one Florence, AL book shipper and from Estes (1); 214 status messages from Holland, ODFL, SEFL, R+L and a carrier with SCAC WTVA (8); a shipper's 204 tenders to ODFL and SEFL (2); a food shipper's TL tender (1). 4 are assumed real: three batches of TL 210s that a freight-payment firm sent to Target, under SCACs WIEL, TQYL (TQL, a broker) and SPXQ, and one broker's tender. 1 is partly real and 5 are templates. No SEFL or Holland 210 is held. Also held: 14 implementation guides (set 12).

**Balance-due or corrected bill.**
- *Purpose:* a later bill under the same PRO number, issued when the carrier re-rates or re-bills after delivery. SEFL's BALANCE DUE prints ask only for the difference; ABF's and SEFL's corrected invoices and XPO's 2021 ones restate the full corrected total.
- *Format:* per firm, in five shapes. SEFL prints "BALANCE DUE INVOICE" and "PAY THIS AMOUNT" with only the difference due; ABF prints the original total, the new total and the reduction; XPO prints the amount paid and the balance, with "RE-WEIGHED PER WEIGHT CERTIFICATE"; TForce prints the declared and the actual weight; ODFL prints "W & I REWEIGH CORRECTE WEIGHT 1070 LBS" or "CORRECT AS BILLED", and re-bills a new payer under the same PRO titled "ORIGINAL INVOICE". So a correction is found by the PRO plus a changed amount or payer, not by the title alone.
- *In the dispute:* this is where both worked disputes are born. The $94 residential line appeared on the balance-due print dated 06/19/2023, 35 days after shipment, with the carrier's reason printed ("** PER GOOGLE EARTH THIS IS A PRA DLVY"). The weight change appeared on the balance-due print of 05/05/2023, 16 days after shipment. Each restarts the shipper's 180-day clock from its own receipt (13710(a)(3)(B): "within 180 days of receipt of the bill"), so the windows ran to 2023-12-16 and 2023-11-01 at the earliest, counted from the print dates; receipt came some days later. The lesson from the verification: match every balance-due bill to its original and to every later reprint before any date arithmetic; the 2025 "PAST DUE INVOICE" prints of the same bills are reprints, not new bills.
- *Held:* 48 SEFL prints of 2022-23 (37 BALANCE DUE, 7 CORRECTED, 4 ORIGINAL INVOICE), 13 of them (12 balance-due, 1 original) paired with their 2025 PAST DUE reprints (set 02); XPO's reweigh correction (set 03); ODFL's wrong-payer refund and re-bill, end to end (set 21).

**Statement of account.**
- *Purpose:* the carrier's list of open bills, used to chase payment; the place short-pays and disputed balances show up.
- *Format:* per carrier, from a one-page list to Kuehne+Nagel's 276-page pro ledger (pp. 10-285 of a 285-page claim).
- *In the dispute:* the unpaid $94 and $110.23 would sit on SEFL's statement until paid or credited; the 2025 reprints are the collection step.
- *Held:* sets 21 and 22 (including RXO's, 22-011 p. 4) and 24; the catalogue also tags statements in sets 01, 03, 04, 09 and 23.

### 1.4 The dispute itself

**The shipper's audit worksheet or dispute log.**
- *Purpose:* whatever the shipper's staff keep to compare bills with the agreement and track claims.
- *Format:* bespoke to each shipper. Exist's is a 3,645-row spreadsheet with columns for invoice, date, pallets, liftgate, surcharge, freight charge, "NEED TO BE CHG" and "OVER CHG".
- *In the dispute:* it is the document our software replaces, and the example of what it must not do. Exist's "NEED TO BE CHG" is pallets × the per-shipment absolute minimum, a misreading of Item 610, so its $271,829 claim is overstated and it never flagged the $94 that was actually added without an order.
- *Held:* the three yearly worksheets (set 02, pp. 99-224).

**Overcharge claim.**
- *Purpose:* the shipper's formal dispute to the carrier, filed inside the window. The statute gives 180 days from receipt of each bill, but carriers' tariffs start the clock from at least five other dates (ship date at ABF, carrier's receipt of the freight at ODFL, bill date at XPO and Saia, receipt of the invoice plus 7 days at FedEx, tender plus 10 days at TForce), and contracts move it again (Walmart: 12 months from payment). The software computes every clock that applies and shows the earliest.
- *Format:* content standardised by 49 CFR Part 378 (identify the bill, state the amount and reason, attach proof); ABF, R+L, Averitt, YRC, South Bay and FedEx Freight use forms that follow the standard overcharge-claim layout; ABF, R+L, Averitt and FedEx print a bond of indemnity, while YRC and South Bay ask for indemnity only when originals are missing; XPO and Central Transport use their own web forms; brokers give 5-30 days under their own terms.
- *In the dispute:* for the $94 a claim would carry the balance-due bill, the BOL showing the delivery instructions, the agreement's exceptions page, Item 753, and a statement, with evidence, that no dwelling stands on the delivery premises. For the weight it would carry the original and the balance-due bill side by side, the BOL weight, and a request for the certificate.
- *Held:* claim forms from 7 carriers (set 16); real claims filed against Yellow by shippers and an audit firm (set 23); SF 1113 and the government's Notice of Overcharge process (set 20). No shipper's complete Part 378 packet is public.

**The carrier's answer.**
- *Purpose:* approved, declined with a reason, or a credit memo or refund against the bill.
- *Format:* per carrier.
- *In the dispute:* the half of the chain the Exist file never reaches, because no claim was filed in time.
- *Held:* Yellow's "APPROVED" status printouts on nVision's claims and a GlobalTranz decline reason (set 23); ODFL's refund of $2,412.67 and re-bill of $1,133.55 to the vendor (set 21). No stand-alone credit memo or denial letter.

**Payment record.**
- *Purpose:* the shipper's accounts-payable export or remittance showing what was paid, when and through whom; needed for duplicate-payment, paid-via-3PL and late-fee checks (A2, A3, F1).
- *Format:* per shipper's ERP.
- *Held:* none; never public. Pleadings and contract clauses only (sets 09, 11, 01).

**The law.**
- 49 U.S.C. 13710(a)(3): the carrier has 180 days from receipt of the original bill to bill additional charges (A); the shipper has 180 days from receipt of each bill, original or subsequent, to contest it (B).
- 49 CFR Part 378: the claim's content; the carrier acknowledges within 30 days and decides within 60.
- *Southern Furniture Leasing v. YRC* (10th Cir. 2021): "compliance with the 180-day time limit is not optional."
- 31 U.S.C. 3726: the government's window is 3 years, not 180 days.
- *Held:* sets 08 and 20. Shared by everyone.

## 2. Shared or per firm, in one table

| Shared across firms | Per firm |
|---|---|
| EDI X12 210/214/204 segment skeleton | PDF bill layout, charge codes, which dates print |
| VICS/GS1 bill-of-lading form (followed loosely) | The 210 charge mapping, per shipper-carrier pair |
| NMFC item and class numbers | Pricing agreement layout and terms |
| Part 378 claim content and the 30/60-day clocks | Rules tariff wording, item numbers and prices |
| Standard overcharge claim form (6 carriers) | Fuel table bands and effective weekday |
| 49 U.S.C. 13710's two 180-day windows | Rate quote, rate confirmation, statement, claim channel, carrier response |
| Government billing (GBL, SF 1113, 41 CFR 102-118), for one shipper only | Base rate tariff (proprietary or licensed) |

Design reading (AT §6): one standard data path, many per-firm readers.

## 3. What we do not have, and what it would cost

| Missing | Why it matters | Where it comes from | Cost |
|---|---|---|---|
| Base rate tariff (CzarLite, or a carrier's own such as SEFL-0550) | Verifies the gross rate itself, not just the arithmetic (check B2, and the published minimum in B3) | An SMC3 licence; carrier base tariffs are sold as SMC3 data modules, and no free carrier download was confirmed | CzarLite data module listed at $800 (2022 price list), carrier tariff modules $300, each on top of RateWare access. FEMA paid $8,764 a year for one organisation's CzarLite and RateWare web access (2019-21). The price for software serving many customers is not published (AR §AR3). *verified* prices; the multi-customer unit *not answerable from the web* |
| 2023-24 fuel tables in force | Check B8 on every real bill in sets 01 and 02 | The carrier on request, or a retry of the Wayback CDX index | $0 in cash. No archived 2023-24 copies exist for ABF, SEFL, ODFL, XPO or Saia (Wayback availability API, 2026-10-09) |
| BOLs and delivery receipts for the SEFL bills | Evidence for the $94 (what was ordered, who received it) and the declared weight for the reweigh | Only Exist or SEFL | Not obtainable; not in the court file |
| Tariff editions in force at the ship date (ABF 111 before 2024-09-09; SEFL 1090 items revised after 2023, such as 996, 830, 890-100, 647, 754) | Any fee, minimum or accessorial whose item changed after the shipment | The carrier on request | $0 |
| A quote document | Check B5: whether a charge was in the quoted price | The shipper's portal history | $0 in cash; interview documents |
| The device record behind a carrier certificate, a stand-alone credit memo or denial letter, a shipper's Part 378 packet, an AP export, a dispute log | The second half of the dispute and the payment checks (A2, A3, C1, F1) | Interviewees' own files, under NDA, kept outside the project in `~/Documents/personal/bio/freight_private/` and deleted after the assessment (D-18) | $0 in cash beyond any interview incentive the founders set; the cost is the NDA and the founders' hours |
| PACER-only exhibits: Estes v. Coverlex Doc 19-1 (a pricing agreement, a 2,498-bill list, discount-forfeiture exemplars); Estes v. Whatman Docs 1-1, 9-5, 19-5 (sample BOL, invoice, past-due warning); Central Freight v. Amazon Doc 1-1 (Amazon's audit demand letter); Transport Systems v. Amazon Doc 1; Exist v. SEFL filings after Doc 1 including the 2026-02-12 order; Hannum Doc 72-3; Surge v. Mondelez; Coyote v. Jusda and Landstar v. Urban Roads (broker-to-shipper invoices) | Would close the pricing-agreement, demand-letter and broker-invoice gaps | A PACER account (a login, which the project's rules have so far excluded) | PACER charges $0.10 a page, capped at $3.00 a document, and waives the quarter's fees entirely if usage is $30 or less. About 12 documents, so roughly $30-40 at most, and possibly $0 if spread over two quarters. Buying them with the RECAP browser extension installed also puts free copies into the public archive. *assumed* on the PACER fee schedule as known; re-check at pacer.uscourts.gov before buying |
| Lewis v. YRC Doc 63-1 (165 pages) | More Yellow bills | RECAP, free | $0; skipped only for the 25 MB per-file cap |
| R+L v. Qualcomm joint appendix (450 pages) | Surfaced on the W&I query, unread | RECAP, free | $0; not fetched for size |
| A public LTL pricing agreement with prices on a .gov or .edu site | A second agreement layout from a neutral source | Not found anywhere | Not purchasable |
| Carrier-published 210 guides for SEFL, ODFL, Saia, Averitt, Dayton, AAA Cooper, Pitt Ohio, Central Transport | Per-carrier charge maps | The carrier's EDI team, on onboarding | $0; given to trading partners |
| NMFC class data in machine form | Class lookups for check C1 | NMFTA licence (ClassIT) | Price not published (AL); DoD paid $5,500-5,803 for an "NMFC data license renewal" in 2008 (AR) |

Two points for the founders, not decided here:
- The PACER list is cheap. The only reason to hold off is the rule against logins and accounts in research sessions, which buying would waive for one purpose.
- The base tariff is the one real expense. It matters only if the prototype is to check gross rates. Discounts, classes, minimums, accessorials, fuel arithmetic and corrected-bill reconciliation, which together cover every discrepancy found in the public sets so far, need no base tariff.

## 4. The pipeline: where the software looks, and the math that decides a dispute

Built 2026-10-10 from three field maps that list every field with its file and page: the bill side (`research/s5_check_AV_c09_field_map_bills.md`), the shipment facts (`research/s5_check_AW_c09_field_map_shipment_facts.md`) and the price terms (`research/s5_check_AX_c09_field_map_price_terms.md`). It is a proposal [our call], not a decision.

The rule behind it: **gather first, compute second.** Every check has a fixed list of inputs. It runs only when all of them are present. When one is missing, the software looks for it in the next document down the list. If no document has it, the line says what is missing and who can supply it, instead of guessing. The money math is plain code, never AI (`software-initial-pitch.md` §5). The customer's own reviewer decides what to file (D-23). The stages below are the inside of the machine's steps 3-7 (read, check the reading, link, re-price, findings) in `software-initial-pitch.md` §2.

### 4.1 The seven stages

```
STAGE                 LOOKS AT, IN THIS ORDER                              PRODUCES
1 Bill facts          EDI 210 -> PDF bill -> corrected and balance-due     one record per PRO, each print
                      prints -> statement of account                       kept as a dated event
2 Shipment facts      BOL -> carrier certificate -> delivery receipt       declared vs actual weight and class,
                      -> EDI 214 / 204 -> rate confirmation (TL)           services ordered and done, times
3 Price terms         payor -> agreement version -> rules-tariff edition   the rules in force on the ship date
                      -> fuel table -> base tariff (only if licensed)
4 Expected charge     stages 1-3                                           what each bill line should be
5 Compare             billed vs expected, line by line                     a difference per line
6 Trigger test        the facts from stage 2                               does the charge apply at all?
7 Clock and verdict   every clock that applies, tolerances                 flag / ask / not checkable / matches
```

### 4.2 Stage 1: build one record per bill

Read the 210 first when the shipper receives one: its numbers need no reading. Then fill what the 210 lacks from the PDF.

| Field | First source | Fill from | Rule |
|---|---|---|---|
| PRO, line charges, total | 210 | PDF text layer, then OCR | Check OCR against the column sum and, on XPO bills, the scan line |
| Discount %, fuel % | PDF printed % | 210 text (AAA Cooper, Estes) | Otherwise derive them: discount ÷ gross, fuel ÷ net. ODFL's first bill: $188.00 ÷ $261.11 = 72.0%; $12.79 ÷ $73.11 = 17.5% |
| Rate unit | none | none | Test weight × rate = charge; never assume. SEFL "60080" × 5.09 cwt = $3,058.07, so $600.80/cwt |
| Bill type, correction | PDF title plus a changed amount or payer on a known PRO | 210 B3-08 | ODFL titles a re-bill to a new payer "ORIGINAL INVOICE", so the title alone misleads |
| Carrier's reason for a change | PDF remarks ("PER GOOGLE EARTH …", "W & I REWEIGH …") | 210 K1 or L5 text (Estes) | If neither has it, flag the line in its own bucket, "unsupported change, carrier's record requested", counted apart in Test 1 (founders, 2026-10-20) |
| What the BOL asked for | The PDF's echo of the BOL: special instructions, declared class, quote number | none | The 210 does not carry it |
| Ship date | 210 B3-12 or G62 | PDF | BOL |
| Receipt date, for the clock | The date the customer received each bill print: for a 210, its interchange date (ISA-09 / GS-04; 1 to 40 days after the bill date on the real 210s held); for a PDF, the e-mail or portal timestamp; on paper, a received stamp ("FEB 23 REC'D" on an ODFL bill dated 02/18/05, set 21); the payment firm's process date | The bill date (next row), as the earliest the bill could have arrived, marked as a fallback | The 180-day clocks run from receipt (49 U.S.C. 13710(a)(3)); a reprint's date or a re-sent file is never the first receipt. Receipt date first, bill date as the fallback (founders, 2026-10-20) |
| Bill date, the clock's fallback | The earliest of: the first 210's B3-06, the PDF bill date, the earliest-dated "PREVIOUSLY INVOICED ON" entry. That list runs newest first and can stop short (UPS Freight's never shows more than four; on 4 of 8 TForce bills its earliest entry falls 133-512 days after shipment), so treat it as a "no later than" date | Statement date, marked late | Otherwise the clock is "unknown", shown as such |
| Delivery date | Not the bill: the delivery receipt or a 214 | 210 only when coded 035 (actual) | ODFL codes its 210 date 017 (estimated) |
| Payer, terms | 210 B3-04 and bill-to | PDF terms box | Statement |
| Paid, open balance | Statement | XPO and SEFL balance lines | The shipper's payment export |

Four rules hold the record together:
- **One PRO is one bill; every print is an event** with a date and an amount. SEFL's 2025 "PAST DUE INVOICE" prints repeat 2023 bills (12 balance-due prints and one original, 806656602); they are not new bills.
- **Match on keys, never on money.** Match the PRO with zeros, dashes, SCAC prefixes and letter suffixes stripped, then the BOL number. Never match on amount and date: 23 of the 101 ABF bills share both with another bill.
- **Do not check an incomplete bill.** Group pages by PRO and read the page counter: ABF's corrected bill 165261918 runs onto a second page (pp. 75-76). A counter is evidence, not proof: SEFL's fourteen 2020 prints (pp. 49-62) each read "1 of 3", "1 of 12" or "1 of 30" on a different PRO. And there PAY THIS AMOUNT is not the bill's total but a base plus a 25% penalty (p. 49: $647.55, not printed, + $161.89 = $809.44).
- **Derive what is missing.** Original amount = new total − balance due (SEFL 806625953: $1,088.74 − $110.23 = $978.51). The original weight follows from the original net (below, §4.8).

### 4.3 Stage 2: gather the shipment facts

| Fact | Trust first | Fall back to | Never use for this |
|---|---|---|---|
| Declared weight, class, NMFC item | BOL (convert kilograms; sum the lines against the grand total) | 204 tender; the bill's "WEIGHT DECLARED AS" | Delivery receipt (it may already show the reweighed weight) |
| Actual weight, dimensions, density | Carrier certificate, with weight ÷ cube recomputed | Bill's "ACTUAL WEIGHT IS", "MEASURED CUBE" | BOL |
| Services ordered | BOL boxes and special instructions; the bill's echo of them | 204 notes | Delivery receipt, except a consignee's signed request written on it (Estes 567) |
| Services done | Delivery-receipt boxes and printed verification lines | Driver notes | BOL |
| Premises type (residential, limited access) | Nothing authoritative: a question for the reviewer | Consignee name, receiving stamp, the customer's knowledge of its own customer, map and zoning data, all as evidence | BOL or delivery receipt as proof |
| Delivery date and time | Typed delivery receipt; 214 "delivered" event | 210 only if coded actual | A handwritten date that conflicts |
| Detention times | The record the rate confirmation names (receiver's label, BOL stamp) | Delivery-receipt or BOL in/out times; 214 arrival then delivery | The bill line alone |
| Payer | Corrected BOL or letter of authority; in brokered TL, the rate confirmation | BOL terms box | Bill-to on the delivery receipt |
| TL agreed price | The shipper's own rate confirmation, tender or 204 for the same load | The carrier's or broker's invoice to the shipper (what was billed, not what was agreed) | A rate confirmation for another load, or a broker-to-carrier one (it prices the broker's leg) |

Link each document to the bill by PRO first, then by BOL number (zeros and punctuation stripped, multi-value fields split), then by PO + ship date + consignee. Check each certificate's own arithmetic. UPS Freight's certificate for PRO 406858966 printed a density of 20.08 lb/ft³ from the BOL weight (4,117 ÷ 205); its own weight gives 23.54.

### 4.4 Stage 3: load the price terms in force on the ship date

1. **Payor first.** Most tariffs read apply "the pricing published specifically for the account of the payor of the freight charges" (SEFL 201, ODFL 764, XPO 4, Estes 760, Saia 105, ABF, AAA Cooper), falling back to the shipper's or consignee's pricing. FedEx Freight and TForce rank by the BOL's terms instead (prepaid: the shipper's; collect: the consignee's inbound, else the shipper's; third party: its own). So the BOL's terms box and payor, or a corrected BOL, pick the agreement before any price is checked.
2. **Agreement version.** Take the latest version effective on or before the ship date. Bill 807148067 (shipped 2023-05-15) falls under the 04/12/2023 version.
3. **Rules.** Take the agreement's terms first. Then take the carrier's tariff item in the edition in force on the ship date. Some contracts shut the tariff out except where named (Kroger, Walmart, Home Depot).
4. **Fuel.** Take the contract's table first, otherwise the carrier's, at the diesel week the carrier's rule names. ABF, for example, uses Wednesday's rate from the prior Monday's EIA price.
5. **Base rate.** Only with a licensed base tariff. Without one, the printed rate is taken as given and only the arithmetic is checked.

Anything missing here (the agreement, a fuel table, a tariff edition) becomes a named request to the customer or the carrier.

### 4.5 Stage 4: compute the expected charge

**LTL**, rounding half up to the cent at each step:
1. **Class:** if the BOL's class sits inside the agreement's FAK range, use the FAK class; otherwise the actual class. If the BOL gives no usable class or density, the carrier's default applies and is punitive: class 150 at SEFL (Item 170) and XPO (26.3), 175 at Estes (170), up to 250 at TForce; a BOL with no weight is weighed and charged a fee (ABF 992 ¶4; Estes 993 $20; ODFL 367 $25; XPO 239 $50.70). The blank is the carrier's licence to fill it, not a dispute in itself (`doc-exploration.md` §4.2).
2. **Gross:** Σ weight/100 × rate, plus any deficit weight at the next weight break.
3. **Discount:** gross × the agreement's %; net = gross − discount.
4. **Minimum:** net = the largest of the net, the discounted published minimum and the agreement's floor, or the tariff's absolute minimum where the agreement sets none (ABF 615, ODFL 180, FedEx 404). Test the cubic minimum when cube ≥ 750 ft³ and density < 6 lb/ft³ (SEFL Item 610-100).
5. **Fuel:** fuel % × the carrier's fuel base (net linehaul at ABF, Estes and SEFL; wider at FedEx).
6. **Each accessorial:** the agreement's exception if there is one. Otherwise the tariff: weight/100 × rate, held between the item's minimum and maximum, or a flat fee. *Whether it applies is stage 6.*
7. **Correction fee:** only if the tariff's threshold is met. ABF charges when the charges move by $10 or more; ODFL when the weight rises by 20 lb or more.
8. **Total:** balance due = new total − what was already billed on the same PRO.

**TL:** linehaul (flat, or per mile × miles) + fuel (%, per mile, or "included") + detention, max(0, hours − free hours) × rate up to any cap + stop-offs + layover + TONU + lumper at the receipt's face value. Each term comes from the rate confirmation first, then the master agreement.

### 4.6 Stages 5 and 6: compare, then test the trigger

Every line ends in one of four states:

| State | Meaning | Example from the public sets |
|---|---|---|
| Matches | Billed = expected, within tolerance | 807148067's discount, liftgate and residential price |
| Price wrong | The charge applies but the amount differs | A fuel % off the carrier's table, once that table is held |
| Trigger in question | The price is right, but whether the charge applies needs a fact | The $94 residential line |
| Not checkable | An input is missing, and is named | 807148067's 22% fuel (no 2023 SEFL table); its $600.80 rate (no base tariff) |

A price is checked against the tariff; a **trigger** is checked against a fact from stage 2. The tariff's own wording says which fact:

| Charge | Applies when (tariff wording) | The fact that settles it | Where the fact is |
|---|---|---|---|
| Residential | A dwelling stands on the delivery premises (SEFL 753); each carrier defines it differently (§1.1) | Premises type | The reviewer; the stamp and consignee name as evidence |
| Limited access | The site is a limited-access location; SEFL 754's list ("mini storage warehouses", "schools" …) "includes but is not limited to" and covers the entire premises | Site type | The same |
| Liftgate | "required or requested" (SEFL 890-100); asked on the BOL or noted on the delivery receipt (Estes 567) | Request or need | BOL box; delivery-receipt note |
| Notification, appointment | Requested by any means; an appointment or call-ahead on the BOL counts (SEFL 647), and a request not on the BOL is charged to whoever made it | Who asked, and how | BOL; the carrier's record of the request |
| Redelivery | The first attempt failed "through no fault of the carrier" (SEFL 830) | The first-attempt record and its reason | Delivery receipt, 214 |
| Detention | Time past the free time, from arrival or from the later of arrival and appointment | Timestamps, and the notice the rate confirmation requires (KCH: within 2 hours of the appointment; LEI: calls at arrival, at two hours and at departure) | The record the rate confirmation names |
| Reweigh, reclass | The carrier's reading differs from the BOL. Tariff thresholds mostly set the correction fee, not the correction (Estes 992; ABF 992, which processes a reduction only above its reweigh fee: $50 in the 2025 issue, $55 in 2026) | The certificate | The carrier: ask early, or pull it through the carrier's document API where one exists (ODFL, TForce); HB44 keeps a dimensioner's readings on request only 30 days after invoicing |
| Two charges for one condition | ABF: no residential charge when limited access is charged; XPO: one charge per address | None needed | The bill itself |

A contract can move the burden: First Brands' requires the carrier to hold the shipper's authorization for any accessorial.

### 4.7 Stage 7: the clock and the verdict

**The clock.** Compute every clock that applies and show the earliest:
- the statute's 180 days from receipt of each bill;
- the carrier's own start date (§1.4);
- the contract's;
- short windows such as XPO's 15 days for a guarantee refund.

Aim inside the earliest. Windows are not always enforced: Yellow approved a claim filed 189 days after pickup against its own form's "180 days of pickup" (`doc-exploration.md` §5.5). So a line up to 10 days past the earliest deadline is still shown, as "late: file now, may be refused". The founders' words (2026-10-20): "Make it noted this isn't ALWAYS enforced. So maybe we have a buffer of 10 days but really try to get it into this 180 day gap." Courts enforce the statute's 180 days (*Southern Furniture*: "not optional"), so the buffer is no reason to plan past it.

Then watch the carrier's clocks after filing: 30 days to acknowledge and 60 to decide (Part 378). Yellow's draft for a real claim is dated 84 days after it received the claim; the approval date is not printed.

**The verdict per line** [our call]:
- **Flag for dispute:** the carrier owes money on the difference, the line is inside the window or no more than 10 days past it, and the proof is in hand or is a document the carrier must produce. When the only thing missing is the carrier's own record (a certificate behind a reweigh, a reason for a change), the flag goes in its own bucket, "unsupported change, carrier's record requested", counted apart in Test 1 (founders, 2026-10-20).
- **Ask the reviewer:** the trigger is in question. Ask once per consignee, not once per bill.
- **Not checkable:** name the missing input and who can supply it.
- **Matches.**

For now there is no tolerance: any difference in the shipper's favour is flagged, whatever its size (founders, 2026-10-20: "For now lets say any difference, so long as there is money that the carrier needs to pay"). Per-charge tolerances in dollars and percent (`software-initial-pitch.md` §6) can come later. Flagged lines are grouped by cause and carrier, because one claim may cover many shipments with the same issue (49 CFR 378.3(b)). Each line shows the reviewer three things: the dollars at stake (billed − expected), the earliest deadline and the proof.

**The claim the pipeline fills.** Part 378.4 requires the claimant's name, its file number if any, the amount sought if known, and (for an overcharge) the freight bill. It allows the rate, class or weight claimed, the tariff authority, the payment details and other documents. The standard form adds the PRO and date, the nature of the error, paid against should-be and, on most carriers' forms, a bond of indemnity.

### 4.8 Four bills through the pipeline

**A. SEFL 807148067, the $94 residential line.**

| Stage | What happens |
|---|---|
| 1 | One bill, two prints: the balance-due print of 06/19/2023 and a 2025 reprint. Original total = $591.10 − $94.00 = $497.10. Reason printed: "PER GOOGLE EARTH THIS IS A PRA DLVY". No 210 |
| 2 | BOL and delivery receipt not held. The bill's echo of the BOL shows "'LIFTGATE DELIVERY" and quote CWEN3E465, but no residential request |
| 3 | Payor Exist (prepaid) → the 04/12/2023 agreement → its exceptions page has no residential line → SEFL 1090 Item 753, in force since 2022-12-16 |
| 4 | 509 lb × $7.60/100 = $38.68, raised to the $94 minimum |
| 5 | Billed $94 = expected. The gross rate and the 22% fuel: not checkable |
| 6 | Trigger: is there a dwelling on the premises? Ask the reviewer |
| 7 | Clock: about 2023-12-16, from receipt of the 06/19/2023 bill. **Verdict: ask the reviewer.** If the answer is "a business, no dwelling", flag it with the balance-due bill, the BOL, the exceptions page and Item 753 |

**B. SEFL 806625953, the weight raised from 2,430 to 2,720 lb.**

| Stage | What happens |
|---|---|
| 1 | Balance-due print of 05/05/2023: $110.23 due on a $1,088.74 total. Original total derived: $978.51. No inspection note |
| 2 | No certificate on the bill. Declared weight from the BOL (not held; 2,430 *assumed*) |
| 3 | Shipped 2023-04-19, seven days after the 04/12/2023 version took effect: 90.30% off, a $127.50 floor on the Midwest lanes. SEFL's 2023 reweigh-fee item is not held |
| 4 | At 2,430 lb: 24.30 × $315.97 × (1 − 90.30%) = $744.77; + $55 liftgate + 24% fuel $178.74 = $978.51 |
| 5 | Billed $1,088.74 − expected $978.51 = $110.23 |
| 6 | Trigger: a certified reading above the declared weight. None is printed, so the fact needed is the carrier's certificate |
| 7 | Clock: about 2023-11-01. **Verdict: flag for dispute**, asking for the certificate. Without one, the carrier has no recorded reading behind the change |

**C. ODFL PRO 00902527924, a machine-file bill (set 19).**

| Stage | What happens |
|---|---|
| 1 | The 210 gives 650 lb × $40.17/cwt = $261.11, discount −$188.00, fuel $12.79, total $85.90 (= B3-07). Derived: 72.0% off, fuel 17.5% of net. Its delivery date is coded estimated |
| 2 | The 214 for the same PRO shows delivery on 2012-09-27 at 11:07. The weight reads 606 lb on the first message and 650 lb at pickup and delivery |
| 3 | ODFL's agreement and its 2012 fuel table are not held |
| 4-5 | The arithmetic passes. The discount and fuel levels cannot be compared |
| 7 | **Verdict: not checkable.** Needs the account's ODFL agreement and ODFL's fuel table for the ship week |

**D. One consignee across several bills (set 02).** SEFL charged the Ocean City, MD consignee as a residence on all three bills held for it: $139.69 in 2020, then $99.94 and $575.00 in 2023, $814.63 in all. SEFL's own 2020 bill names that consignee "OCEAN WAVES CITY WHSE". Stage 6 asks the reviewer one question for the address, not three, and the answer settles every bill to that consignee.

### 4.9 What the pipeline still lacks
- **Base rates,** so the gross rate (B2) is never checked: §3.
- **Fuel tables and tariff editions in force on old ship dates** (B8, and any item revised since): ask the carrier.
- **The account's agreement and any quote:** interview documents.
- **Premises type:** no authoritative public source.
- **The shipper's payment export,** for duplicates and payments through a 3PL (A2, A3).
- **No real balance-due 210 has been seen,** so the first build should detect corrections from the PDF path.
