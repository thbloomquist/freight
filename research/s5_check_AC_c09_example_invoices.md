# S5 check AC: what real freight invoices and their supporting documents look like, and where public ones exist (C-09)

- **What this is:** desk research for S5 in run 01, on card **C-09**: "Checking and paying truckload and LTL freight bills, for mid-sized manufacturers and distributors (US, 20-499 staff), handled today by accounts-payable clerks, contingency audit firms and, for larger shippers, audit-and-payment providers."
  - **The founders asked:** "Can you find example invoices as well? If this information exists publicly, if not note it as something to explore through customer interviews."
  - **Why it matters:** the planned savings assessment (`selection_runs/run-01/5_interview_kit.md` §6.1) re-checks 1-3 months of paid TL and LTL invoices against rate agreements, BOLs and PODs. Real documents show which fields exist, what the look-back can and cannot check, and what to ask interviewees for.
- **Not covered here:** LTL carriers' rules tariffs, inspection rules and dispute windows (check T, `s5_check_T_ltl_carrier_position.md`, is linked, not redone); FAP providers' carrier terms (check Z §10.1); overcharge rates (check X); recruiting (check Y).
- **Date:** 2026-09-17. All sources accessed 2026-09-17.
- **Status:** input to S5. **It decides nothing.** Suggestions are marked **[our call]**.
- **Labels:**
  - *verified*: read at the source. For court exhibits this means the page image or text layer was read directly.
  - *assumed*: a search snippet, a vendor claim, a secondary summary, or memory. **A party's allegation in a lawsuit is *assumed*** even when read in full: it is one side's account.
  - **real / mock / template** for documents: *real* = a document from an actual transaction; *mock* = a made-up filled example; *template* = a blank form or a specification with placeholder data.
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
  - **Segment fit:** each real document says whether the shipper looks inside C-09's segment. Staff counts were **not** checked, so "size unknown" is common.
- **Privacy:** court exhibits here contain names, signatures and phone numbers of private people. None are copied. Only company names, document numbers already public on the court docket, field names and amounts are recorded.
- **Access, in one line:** CourtListener's free RECAP archive was the richest source (queried through its public search API with no identity). DoD's transportation site failed a certificate check, USAID's data portal is offline, Kaggle pages did not render, and no carrier "how to read your invoice" page was found. About 40 web searches were used.
- **New sources:** N-AC01 to N-AC40 (§11). Existing IDs cited: N-T17 to N-T30 (check T), N-Z47, N-Z49, N-Z50, N-Z54 (check Z).

**Words used here:**
- **LTL / TL:** less-than-truckload (several shippers' pallets on one trailer, priced by class and weight) / truckload (one shipper's load, priced per load or per mile).
- **PRO / freight bill number:** the carrier's shipment ID, usually also the invoice number on LTL bills.
- **BOL:** bill of lading, the shipping document signed at pickup. **VICS BOL:** the standard short-form BOL layout most shippers print.
- **POD / delivery receipt (DR):** the signed record of delivery. LTL carriers print a "delivery receipt" that doubles as the POD.
- **cwt:** hundredweight, 100 lb. LTL rates are quoted "per cwt".
- **Base rate / tariff:** the carrier's (or SMC3's CzarLite) price table by lane, class and weight break, before discount.
- **Discount:** the negotiated percentage off the base rate. **Absolute minimum charge (AMC) / floor minimum:** the lowest net charge a shipment can bill after discount.
- **FAK:** "freight all kinds", a contract term that rates a range of NMFC classes at one class (for example "class 70 for anything from 77.5 to 125").
- **Deficit weight:** rating a shipment as if it weighed the next weight break (for example 1,837 lb billed as 2,000 lb) when that is cheaper; carriers must apply it under the "alternation" rule.
- **Fuel surcharge (FSC):** a percentage (LTL) or cents per mile (TL) tied to the U.S. Energy Information Administration's weekly diesel price.
- **Accessorial:** an extra-service charge (liftgate, residential, detention, lumper, appointment, reweigh fee).
- **Reweigh / W&R or W&I certificate:** the carrier re-weighs or re-measures after pickup and issues a "weight and research" or "weight and inspection" certificate as its proof.
- **Detention:** a charge for time a truck waits beyond "free time" at pickup or delivery. **Lumper:** a third-party unloader.
- **Rate confirmation (rate con):** a broker's or carrier's one-load price agreement.
- **EDI 210:** the electronic motor-carrier freight invoice (ANSI X12 transaction set 210). Segments named here: **B3** header (invoice number, BOL, dates, amount due), **N9** references, **N1-N4** parties, **L5** description, **L0** quantity and weight, **L1** rate and charge, **L7** tariff and class, **L4** dimensions, **POD** proof of delivery, **K1** remarks, **L3** totals.
- **FAP:** freight audit and payment provider (Cass, U.S. Bank and others).
- **3PL / bill-to agent:** a logistics company that receives, and sometimes pays, the carrier's bills for the shipper.
- **Proof of claim:** a creditor's filing in a bankruptcy case listing what it says it is owed, usually with invoices attached.

---

## 0. Summary table

| Question | What was found | Best public example | Label |
|---|---|---|---|
| **AC1 Real carrier invoices** | **LTL: yes, three real sets in court filings, 2020-2024.** (1) 6 XPO LTL invoices with their BOLs and delivery receipts; (2) about 75 pages of Southeastern Freight Lines (SEFL) freight bills from a Miami apparel maker's overbilling suit; (3) **107 ABF Freight invoice pages (101 distinct bills, May-Aug 2024)** for a supplement maker, a ready-made 3-month look-back sample. **TL: no real carrier-to-shipper invoice found**, only blank templates. **No carrier publishes a "how to read your invoice" page** among the 16 named | ABF set (N-AC04); XPO set (N-AC02) | documents *verified*, **real** |
| **AC2 EDI 210** | Seven public 210 specifications: two from shippers (3M 2017, Cardinal Glass 2024), five from carriers (TForce, Estes 2008, ArcBest 2024, R+L, Pitt Ohio), each with segment lists; four carry sample transactions. A 210 carries everything on the PDF face except the **signed POD image, inspection certificates, photos and the rate agreement**; class (L7) and POD segments are optional and **Estes marks both "Not Used"** | 3M guide with TL sample and "billing error" corrections (N-AC11) | *verified*, **template** |
| **AC3 Documents checked against** | **A real LTL shipper-carrier contract** (YRC-First Brands, 2021: accessorial schedule, FAK table, weekly DOE fuel table, 180-day billing and claim windows) and **a real SEFL customer pricing agreement in three dated versions** (discounts, FAK, per-pallet rates, accessorial exceptions). Two real C.H. Robinson rate confirmations (broker to carrier). Public fuel tables (DOE ATLAS weekly 2025, GSA, Werner TL, XPO, Estes) and the EIA diesel series. A filled VICS BOL, a UPS Freight BOL, XPO and Yellow delivery receipts. **No weight or inspection certificate is public.** SEC exhibits were thin | N-AC05, N-AC03, N-AC21, N-AC24 | *verified*, **real** and **template** |
| **AC4 Datasets** | **No public dataset of US domestic freight invoices exists that was found.** The court sets above are the practical substitute. USAID's health-commodity shipment file (10,324 rows, international, freight cost per shipment) is real but out of scope. Government payment files (Chicago, Vermont) lack invoice numbers. USDA publishes weekly reefer TL lane rates (benchmarks, not invoices). Kaggle "freight invoice" data: none found | ABF claim set (101 bills) | *verified* |
| **AC5 Annotated errors** | **One real, large, shipper-made look-back is public:** Exist Inc.'s spreadsheets of **3,645 SEFL invoices (2021-2023)**, each marked "need to be charged" and "over charge", **totalling exactly the $271,828.70 sued for [our calc]**. It is an allegation, not a proven error. Other real cases: the ABF bills that a 3PL says it had already paid; Amazon's 2016 audit claim against Central Freight (8-pallet discount, cut back by an 18-month claim window). Vendor blogs describe errors in text but **show no annotated real invoice** | N-AC03 | documents *verified*; claims *assumed* |
| **AC6 Not public** | **Only obtainable from the shipper:** its own paid invoices, its rate agreements and every version in force, the carrier's base rate table, historical fuel tables, W&R certificates, detention in/out times, lumper receipts, AP payment records, dispute and credit history, and 3PL or broker bills | §6, §9 | [our call] |

---

## 1. AC1 · Carrier freight invoices (TL and LTL)

### 1.1 Real LTL invoices found

| # | Carrier / document | Where (all free on CourtListener) | Shipments | Segment fit | Fields visible | Error or correction shown? | Label |
|---|---|---|---|---|---|---|---|
| I-1 | **XPO Logistics (CNWY) LTL invoices**, 6, each with its **VICS BOL** and **XPO delivery receipt** | *In re Vital Pharmaceuticals*, Bankr. S.D. Fla. 22-17842, Doc 533-7 (XPO proof of claim 1-1, filed 2022-10-13) (N-AC02) | 2020-12-11 to 2021-12-28 | Out: shipper is a large energy-drink maker (size *assumed*) | "LTL INVOICE#" (= PRO); bill-to; shipper; consignee; customer numbers (PO, redacted); shipment date; pieces; description with class ("PLT MISC CLASS 100"); weight; **rate per cwt or "M" (minimum)**; charges; **"XPO LOGISTICS DISCOUNT SAVES YOU"** line; **"FSC FUEL SURCHARGE 30.50%"**; accessorial lines (**"CBR REWEIGH OF SHIPMENT FEE"**, "APT APPOINTMENT"); **late-fee lines LP1-LP6 ("30 DAYS PAST DUE" … "180 DAYS PAST DUE")**; total; payment due date; "CORRECTED INVOICE" or "BALANCE DUE INVOICE"; "AMOUNT PAID"; remarks such as "RE-WEIGHED PER WEIGHT CERTIFICATE" and "VOLUME SHIPMENT PRICING SAVES YOU $ 5805.94 … BASED ON 932 MILES" | **Corrections, yes:** reweigh fees on 3 of 6 invoices ($35.25-$39.40) with "re-weighed per weight certificate" notes; late fees on 4 of 6. No error is alleged by anyone | **real**, *verified* (page images) |
| I-2 | **Southeastern Freight Lines freight bills**, about 75 pages, labelled "PAST DUE INVOICE", "BALANCE DUE INVOICE" or unlabelled; some with handwritten circles and a "POSTED" stamp | *Exist, Inc. v. Southeastern Freight Lines*, S.D. Fla. 1:26-cv-20049, Doc 1-2, Exhibit A pp. 23-97 (N-AC03) | 2020-2023 | **Possibly in segment**: "a manufacturer and distributor of various clothing and apparel" (complaint ¶7); staff not checked | Freight bill no.; consignee; shipper; pieces; description with **NMFC item and actual class** ("CL110 NMFC 49880"); **billed class** ("CLASS 70.0", the FAK); weight; rate; **"GROSS FRT CHG", "90.30% DISC", "NET FRT CHG"**; "LIFTGATE SVC"; **"LTL FUEL SURCHARGE OF 24.00%"**; total; prepaid; quote number; shipper order and pick-list numbers; shipment date; payment due date; shipper B/L no.; date billed; customer number; origin and destination terminal codes. A 2020 bill also shows "MINIMUM FREIGHT CHARGE", "GROSS CHARGE IS", "DISCOUNT PERCENTAGE 9100" and "PENALTY/TARIFF DUE" | **Alleged**, yes: the shipper says the bills exceeded agreed prices and included double invoices (§5.1) | **real**, *verified* (images and OCR text); allegation *assumed* |
| I-3 | **ABF Freight (ArcBest) LTL invoices**, 107 pages = **101 distinct freight bills** plus 6 repeated copies | *In re IN Holdings*, Bankr. C.D. Cal. 1:24-bk-11323, Doc 920 (debtors' objection to ArcBest Claim No. 2, filed 2025-12-16), Exhibit 2 (N-AC04) | **2024-05-09 to 2024-08-09** | **Possibly in segment**: IN Holdings (Irwin Naturals) "formulated, marketed, and distributed vitamins and supplements"; sold for $42.5M in 2025; staff not checked. Bills went to a 3PL, TLS Transportation | "ORIGINAL INVOICE" / "CORRECTED INVOICE"; freight bill no.; shipment date; account no.; amount due; payment due date; bill-to; shipper and consignee accounts; P.O. number; **bill of lading no.**; **tariff code ("AOD000")**; pieces; description with **NMFC item, density band and exception class** ("DENS 8 12 CL 100 ITEM 057300-03V (EX70)"); weight; class; rate; charge; **"ALLOWS LOWER CHARGE AT HIGHER WEIGHT DEF163 AS2000"** (deficit weight); **"RATE DETERMINED BY RATEWARE"**; **"DISC,89.5%"**; **"ABSOLUTE MIN CHARGE ADJUSTMENT MCADJ"**; "CALIFORNIA COMPLIANCE SURCHARGE CCS"; "SPECIAL HANDLING SERVICES - LUMPER SHDL"; "NEW YORK ISLAND DELIVERY"; **"DRIVER DETENTION AT DEST DETND"**; "FUEL SURCHARGE FSC 30.3%"; **"DYNAMIC DISCOUNT"**; **"W02/AUTH:Reweigh - See W&R certificate for details."**; "W01/AUTH:Restore original weight"; **"ABF MEASURED CUBE"** and **"RATED DIMENSIONS: 48X40X44"**; pricing-quote schedule no.; lumper refund allowance; consignee signature on some | **Yes, three kinds** (§1.3, §5): reweighs; a detention charge with no times on the bill; and the debtor's position that a 3PL had already paid every bill | **real**, *verified* (machine text layer) |
| I-4 | **Yellow Transportation delivery receipts** (the freight-bill form used as POD) and a delivery manifest | *In re Circuit City Stores*, Bankr. E.D. Va. 08-35653, Doc 6033-2 (N-AC06) | 2008-12 | Out (large retailer) | Freight bill number with check digit; bill date; destination/origin; shipper; consignee; P.O.; shipper number; pieces; description; class, weight, rate and extension columns (**blank** on this copy); total freight charges "NEXT PAGE"; **"WAIT TIME START / END"** boxes; "INSIDE DELIVERY / LIFT GATE / # PIECES SORT & SEG / RESIDENTIAL / CONSTRUCTION SITE" tick boxes; appointment confirmation; "RECEIVED IN GOOD CONDITION" signature | No | **real**, *verified* (pp. 1, 3 viewed) |

**One date worth noting [our calc]:** the SEFL bill 806282380 is for a shipment of **2023-04-03** but shows "date billed **2025-08-26**" and a payment due date of 2025-09-10, marked "PAST DUE INVOICE / INVOICE PENDING". Whether that is a reprint of an older bill or a late re-bill is not shown on the face; the 180-day rebill limit in 49 U.S.C. 13710(a)(3) (check T §4) turns on which it is. **A look-back should capture both the shipment date and the bill date** (the ABF and XPO bills print only one of the two in places).

**Reading [our call]:** the bills from three national LTL carriers share the same core: PRO, dates, parties, BOL or PO references, pieces, weight, class, rate, gross charge, discount, net charge, fuel percentage, accessorial lines, total. They differ in how much rating logic they print. **ABF prints the most** (tariff, deficit weight, rating engine, measured cube, dimensions, reweigh authorisation codes). **XPO prints the least** (a single discount line; "M" for minimum).

### 1.2 Worked re-rating of four real bills [our calc]

The arithmetic on each bill face was re-done to show which checks a look-back can run **from the invoice alone**, and which need another document.

| Bill | Face values | Re-computed | Checks passed on the face | What the face cannot tell |
|---|---|---|---|---|
| **XPO 712-591121** (ship 2021-12-02, 300 lb, class 100) | rate $391.89/cwt; charges $1,175.67; discount ($293.92); FSC 31.25% $275.55; LP1, LP2, LP4, LP5 late fees $17.36 each; total $1,226.74 | 3.00 cwt × 391.89 = 1,175.67; 25.0% discount = 293.92; FSC 31.25% × 881.75 = 275.55; late fee = 1.5% × 1,157.30 = 17.36; total 881.75 + 275.55 + 69.44 = 1,226.74 | Math, discount %, FSC applied to net linehaul only, late fee = 1.5% per period | Whether 25% is the agreed discount; whether $391.89 is the right base rate; whether 31.25% was XPO's table value that week (EIA diesel was $3.720 on 2021-11-29, N-AC25); whether late fees were owed |
| **SEFL 806282380** (ship 2023-04-03, 1,615 lb, NMFC class 110 rated FAK 70, to Michigan) | rate 304.71; gross $4,921.07; 90.30% discount $4,443.73; net $477.34; liftgate $55.00; LTL FSC 24.00% $114.56; total $646.90 | 16.15 × 304.71 = 4,921.07; × 90.30% = 4,443.73; FSC 24% × 477.34 = 114.56 (not on liftgate); 477.34 + 55 + 114.56 = 646.90 | Math, FSC base. **Against the public pricing agreement (§3.1):** the 06/08/2022 and 04/12/2023 versions both give Midwest-partner outbound **90.30%** and **FAK 70 for 77.5-175**; the accessorial table gives **liftgate $55 "direct to partnership"**. All three match | The base rate SEFL-0550 ($304.71/cwt) is SEFL's own table, not public; the fuel table in force that week |
| **ABF 150235531** (ship 2024-07-01, 2 pallets, 1,837 lb, EX70) | rate 348.19; charge 6,396.25; deficit weight to 2,000 lb 567.55; disc 89.5% −6,232.60; CCS 22.00; lumper 149.10; FSC 30.3% 221.55; dynamic discount −181.83; total $942.02 | 18.37 × 348.19 = 6,396.25; 1.63 × 348.19 = 567.55; 89.5% × 6,963.80 = 6,232.60; FSC 30.3% × 731.20 = 221.55; 731.20 + 22 + 149.10 + 221.55 − 181.83 = 942.02 | Math, deficit-weight rule applied, discount %, FSC base | Agreed discount and AMC; base rate; **what the BOL weight was before the reweigh note** (the bill shows only the final weight); whether the lumper was authorised |
| **ABF 150256193** (corrected invoice, ship 2024-05-09, 389 lb) | charge 3,509.21; deficit to 500 lb 1,001.34; disc 89.5% −4,036.94; CCS 22.00; NY island delivery 100.00; **driver detention at destination 42.71**; FSC 31.5% 149.19; dynamic discount −269.11; total $518.40 | 3.89 × 902.11 = 3,509.21; 1.11 × 902.11 = 1,001.34; 89.5% × 4,510.55 = 4,036.94; FSC 31.5% × 473.61 = 149.19; total 518.40 | Math, FSC base | **Detention was added on a corrected invoice ("Z20DET/AUTH:Add detention") with no arrival or departure times on the bill** |

**Two more rules read off the ABF bills [our calc]:**
- **Absolute minimum charge:** on two 1-pallet bills the net after 89.5% discount plus "ABSOLUTE MIN CHARGE ADJUSTMENT" comes to exactly **$180.00** (702.71 − 628.93 + 106.22; 1,534.24 − 1,373.14 + 18.90), and FSC 30.3% is charged on the $180. An agreement's AMC can therefore be tested from bills alone once the agreed figure is known.
- **Fuel base:** on all **57 of 57** ABF bills where the parser found charge, discount and FSC lines, FSC equals the printed percentage × net linehaul (including any AMC adjustment), never × accessorials. The XPO and SEFL bills follow the same rule. A contract can say otherwise; the YRC contract says fuel "shall not be assessed to over-dimensional penalties, permits or other charges not directly related to the consumption of fuel" (N-AC05).

### 1.3 The ABF set as a ready-made 3-month look-back sample [our calc]

Counts are from a script over the court PDF's machine text layer, not a line-by-line hand check. Each count is of **distinct freight bills (101)**.

| Item | Count | What it tests |
|---|---|---|
| Distinct freight bills; date range | 101; 2024-05-09 to 2024-08-09 | The kit's "1-3 months" (§6.1) |
| Pages in the claim; repeated copies | 107; **6 bills attached twice** (identical amounts). The claim total of **$45,652.49 equals the 101 distinct bills**; all 107 pages sum to $48,131.72 | A duplicate test on a paper pile must key on PRO + amount, not page count |
| Corrected invoices | 4 | B308-type corrections (§2) |
| **Reweigh note "See W&R certificate"** | **28 (28%)**; on **10** of them a second note "Restore original weight" | Needs BOL weight + W&R certificate |
| Absolute minimum charge adjustments | 39 | AMC figure in the agreement |
| Lumper lines ("SHDL") | 28 | Authorisation and lumper receipt |
| Deficit-weight rating applied | 17 | Rate table with weight breaks |
| "Dynamic discount" lines | 17 | Carrier pricing programme; not in any agreement seen |
| California compliance surcharge | 95 | Agreed? (it is a per-bill fee of $22) |
| Detention lines | at least 1 | Timestamps |
| Discount | 89.5% on every rated bill | One agreement |
| FSC % | 30.3% (60), 30.4% (39), 30.9% (2), 31.5% (1); 5 without FSC | Weekly table in force (EIA diesel $3.52-$3.89 over the period, N-AC25) |
| Rated dimensions printed; measured cube printed | 99; 86 | Density-based rating evidence |
| Bill-to | All 101 to a 3PL (TLS Transportation) | Who paid (§5.2) |

### 1.4 TL invoices

| Searched for | Found | Label |
|---|---|---|
| Real invoices from asset TL carriers (Schneider, J.B. Hunt, Werner, Knight-Swift) to shippers | **None.** CourtListener queries on each carrier with "invoice", "fuel surcharge", "linehaul" and "detention" returned driver-pay cases, insurance cases and bankruptcy cure schedules, not invoices | — |
| Broker invoices to shippers (C.H. Robinson, TQL, Echo, Coyote, Arrive) | **None** readable. Broker lawsuits found were against carriers or drivers | — |
| Templates | Many free "trucking invoice templates" (Enerpize, InvoiceQuick, Invoice Fly, CarrierInvoice) with linehaul, fuel, detention "by hours and hourly rate", layover, lumper and TONU lines (N-AC39) | **mock/template**, *assumed* (snippets) |
| 3M's EDI 210 sample | A TL invoice in data form: linehaul $1,020.00 flat + fuel $0.36/mile × 349 miles = $125.64, total $1,145.64; plus a "balance due" ferry charge and a "billing error" re-bill with remark "USED OLD PRICE GUIDE" (N-AC11) | **template**, *verified* |

**What a TL bill must carry, from public TL documents [our call]:** load or rate-confirmation number, BOL, pickup and delivery dates, origin and every stop, miles, linehaul (flat or per mile), fuel (per mile, from a DOE table), and each accessorial with its unit (hours of detention, stops, lumper receipt amount). The Werner tariff and the C.H. Robinson confirmations in §3 define those units.

### 1.5 Carrier "how to read your invoice" pages

**None found** for ODFL, Estes, Saia, XPO, R+L, ABF, TForce, FedEx Freight, SEFL, AAA Cooper, Averitt, Central Transport, Schneider, J.B. Hunt, Werner or Knight-Swift (searches in §12). What exists instead:
- **Carrier document-retrieval portals and APIs** (inspection and weight certificates, delivery receipts, photos), already listed in check T §1 row 5 and §3.2 (N-T18, N-T21, N-T27, N-T29).
- **ODFL, Estes and FedEx Freight BOL forms and BOL guides** (templates).
- **Broker and vendor explainers**, text only. FreightSimple (2024-10-07) walks through header, shipment details, linehaul, fuel, accessorials, "Reweigh and reclassification charges", "Deficit weight billing" and "Minimum charge", and names six errors ("Fuel surcharge calculation," "Discount not applied," "Unauthorized accessorials," "Duplicate invoices," "Rate not as quoted," "Weight discrepancy"). **It shows no invoice image** (N-AC38, *assumed*).
- **FedEx parcel and air freight invoice guides** (Europe and Malaysia): parcel, out of scope (snippets).

### 1.6 Government transportation payment guides (government shippers, out of segment)

| Source | What it says a bill or audit needs | Label |
|---|---|---|
| **41 CFR 102-118.285** (federal agencies' prepayment audit) | "Assurance that each TSP bill … contains appropriate information for the prepayment audit to determine which contract or rate tender is used"; "Verification of all transportation bills against filed rates and charges before payment"; notice to the carrier "of any adjustment within 7 calendar days of receipt of the bill"; "Detailed written notices" for rejections; an offset right (N-AC27) | *verified* (page extraction) |
| **GSA Uniform Rules Tariff 200-A** (2021-10-01), Item 325 detention | Free time, then $10.25 per vehicle per 15 minutes; **"The consignor or consignee will stamp or mark the delivery receipt with time of arrival and departure, or provide a certified statement verifying this time for computation of charges and presentation by the TSP for payment."** Item 1250: a requested reweigh costs $18.46 if the error is under 5% (N-AC20) | *verified*, **template** |
| **California State Administrative Manual 3851** (rev. 03/2007) | For freight over $50, attach "all supporting prepaid freight bills" and the purchase order; charges not above "the lowest lawful charges on file with the PUC"; ensure payments "are not duplicated" (N-AC28) | *verified* (page extraction) |
| **DoD Defense Transportation Regulation Part II ch. 212 and Part IV App. A (Third Party Payment System)** | Snippet only: the carrier must hold proof of delivery (a signed bill of lading) before e-billing. The PDFs failed to load (§12) | *assumed* |

---

## 2. AC2 · EDI 210 samples and specifications

### 2.1 Public 210 guides found

| Publisher | Side | Version / date | Sample transaction? | Notable rules | Label |
|---|---|---|---|---|---|
| **3M** (N-AC11) | Shipper (carrier guideline) | 4010, 2017-08-11 | **Yes, three:** a TL invoice; B308 = **"AR" (Adding Revenue/Balance Due)**; B308 = **"BE" (Billing Error)** with K1 "USED OLD PRICE GUIDE" | BOL number "Mandatory for 3M"; weight and weight qualifier mandatory; "**3M is unable to accept a negative dollar amount**"; reason for a balance-due invoice "should be sent in K1" | *verified*, **template** |
| **Cardinal Glass Industries** (N-AC12) | Shipper | 4010, v1.5 2015, notes 2024-05-28 | No | L108 special-charge codes accepted include **DET** (detention of trailers), **DSC** (discount), **FUE** (fuel), **LAY** (layover), **LOA/UNL** (loading/unloading labour), **SOC** (stop-off), **RCL** (redelivery), **VOR** (vehicle ordered but not used), **MIN** (minimum guarantee); L707 "Freight Class Code … class 70, 77.5, etc." | *verified*, **template** |
| **TForce Freight** (N-AC14) | LTL carrier | 4010 | **Yes** (dated 2000): 1 skid 1,013 lb, class 50, $22.92/cwt = $232.18; discount −$150.92 (65.0% [our calc]); fuel $1.22; total $82.48 | B308 **"BD" Balance Due, "RC" Revenue Correction**; "Can provide electronically the original, corrected or balance due invoices"; "**Once set up electronic invoices, copies of the delivery receipts or bills of lading are no longer mailed to the customer.**" | *verified*, **template** |
| **ArcBest (ABF)** (N-AC16) | LTL carrier | 2024-12 | **Yes**: per-mile linehaul, discount line (DSC), fuel line (FUE), "MIN CHARGE ADJ" line | Bill-to (N1*BT) loop shown | *verified*, **template** |
| **Estes Express Lines** (N-AC15) | LTL carrier | 4010, 2008-08-12 | No | **L7 (tariff and class), L4 (dimensions), POD and K1 detail marked "Not Used"** | *verified*, **template** |
| **R+L Carriers** (N-AC17) | LTL carrier | 4010 ("Proprietary and Confidential" header, publicly hosted) | Not checked | Uses C2 bank ID, ITD terms, H3 handling, **L4 measurements, POD segment (date, time, name)** | *verified* (partial) |
| **Pitt Ohio** (N-AC13) | LTL carrier (regional) | 4010, web page | No | B302 = "Pitt Ohio Pro Number"; B303 = BOL; N9 BM/BN/CN/CR/PO; L103 "MN – Minimum, PH – Per Hundred"; **L707 freight class and L713 tariff distance used** | *verified*, **template** |
| FedEx (N-AC18) | Parcel and air carrier | revisions to 2022-12 | Remittance CSV example | FedEx Express and Ground only; **FedEx Freight LTL 210 guide not found** | *verified* (partial) |
| FCA (Chrysler) freight payment 210; Empower Data Logistics 210 guide | Shipper; FAP-type | — | — | Snippet only; downloads failed (§12) | *assumed* |
| **FAP carrier guides** (Cass, U.S. Bank, nVision, CTSI) | FAP | — | — | Already covered in check Z §10.1 (N-Z47, N-Z49, N-Z50, N-Z54): EDI or invoice images; nVision "1 Invoice Per Email (including the backup documentation)"; **no public FAP 210 specification found** | see check Z |

### 2.2 What a 210 carries compared with a PDF bill

| Data item | EDI 210 segment | On the real PDF bills (§1.1) | Look-back note [our call] |
|---|---|---|---|
| PRO / invoice number | B302 | All three carriers | Duplicate key |
| BOL number; PO | B303, N9*BM; N9*PO | ABF (BOL no., P.O.); SEFL (shipper B/L no.); XPO (PO, redacted) | Join to BOL and to AP |
| Invoice date; amount due; payment terms | B306, B307; ITD (R+L) | All | Duplicate and late-fee checks |
| **Correction type** | **B308** (BD, RC, AR, BE) | "CORRECTED INVOICE", "BALANCE DUE INVOICE", "PAST DUE INVOICE" | Corrections and rebills are where reweighs and added accessorials show up |
| Delivery / pickup date | B309, B312, G62 | XPO delivery receipt; SEFL and ABF show shipment date | Fuel week is keyed on pickup date |
| Parties | N1 SH, CN, BT + N3/N4 | All | Lane for rating |
| Description and NMFC item | L5 (free text) | ABF, SEFL print NMFC item | Reclass check |
| Pieces, weight, packaging | L0 | All | Reweigh check (needs BOL) |
| Rate, rate basis, charge | L1 (L102, L103 PH/MN/FR/PM, L104) | All | Re-rating |
| Discount, fuel, accessorial lines | L1 with L108 codes (DSC, FUE, DET …) | All | 3M-style guides may net discounts away (no negatives) |
| **Class** | **L707** (optional; Estes "Not Used") | ABF and SEFL columns; XPO in description | Reclass check |
| **Dimensions** | **L4** (optional; Estes "Not Used") | ABF "RATED DIMENSIONS" | Density rating |
| **Proof of delivery** | **POD** (date, time, name; optional; Estes "Not Used") | Separate delivery receipt image | Detention and delivery disputes |
| Remarks (reweigh, reason) | K1 | ABF "W02/AUTH:Reweigh", XPO "RE-WEIGHED PER WEIGHT CERTIFICATE" | Flags where to pull certificates |
| **Not in any 210 guide seen** | — | — | **W&R or inspection certificate, photos, signed BOL/POD image, lumper receipt, detention in/out times as a structured field, the rate agreement, the quote** |

**Reading [our call]:** a shipper receiving EDI 210s has cleaner data for duplicate, math and fuel checks, but **may have fewer supporting papers**: TForce stops mailing delivery receipts and BOLs once EDI starts. Supporting documents then come only from carrier portals, which check T shows are open to the bill-to party.

---

## 3. AC3 · The documents the audit checks against

### 3.1 LTL pricing agreements and contracts

| Document | Where | What it contains | Missing | Segment fit | Label |
|---|---|---|---|---|---|
| **"LTL Motor Carrier Transportation Contract"**, YRC Enterprise Services (for YRC Freight, Holland, Reddaway, New Penn) and First Brands Group, dated 2021-03-15 | Yellow Corp. adversary case 25-51852, Doc 1-1, Exhibit A (also main case 23-11069 Doc 7410-1) (N-AC05) | 33 articles. **Art. 13:** invoices by paper, EDI "or participation in First Brands Group's self-invoicing freight payment program"; charges "not submitted and received within … one hundred and eighty (180) day period are null and void"; overcharge, "duplicate payment or over-collection claims" governed by 49 CFR 378. **Art. 14:** undercharge and overcharge actions "commenced not more than 180 days after the original bill date". **Art. 1(j):** shipper audit right over carrier records, kept 3 years. **Schedule A:** facilities and **freight-bill-to addresses (care of ITS Traffic Systems, Blue Grace Logistics, Williams and Associates)**. **Schedule B:** accessorial table (e.g., liftgate $20; driver detention with power $20 per quarter hour after 30 min, 2 hours free; inside delivery $2/cwt min $30; **re-weighing, corrected BOL, first redelivery "Waived"**) and **"Carrier must have authorization from First Brands Group for accessorial charges incurred and is responsible for retaining documentation"**; **FAK table** (NMFC 50-77.5 → 50; 85-110 → 77.5; 125-200 → 125; 250-500 → 250, with plant exceptions); **weekly fuel table** keyed to EIA's Monday diesel price ($1.210-1.259 → 0.60% … $4.010-4.059 → 17.40%, +0.3% per 5¢ beyond), "shown as a separate entry on the Carrier's freight bill", not on "over-dimensional penalties, permits". Schedule D cargo liability | **Schedule C "Pricing" (discounts, base rates) is listed in the contents but not in the filed copy** | Out: large auto-parts group (size *assumed*) | **real**, *verified* |
| **SEFL customer pricing agreement** ("TARIFF SEFL 6009, RATING ITEM 000-068386") for Exist Inc., three versions effective **2021-01-15, 2022-06-08, 2023-04-12**; plus an undated "Pallet Rates Pricing" table and an "Accessorial Charge Exceptions" table | *Exist v. SEFL*, Doc 1-2, Exhibit A pp. 12-22 (N-AC03) | Per route and direction: **base rate SEFL-0550** with its effective date; **floor minimum charge** ($88.50 in 2021, $97.00 later); **discount** (81.00% SEFL-direct outbound; Midwest partner outbound 92.50% in 2021, **90.30%** in 2022-23; other partner zones 75-92.10%); **FAK class 70 for NMFC 77.5-125 (or -175)**; **per-pallet rates by destination state** for 1, 2-4 and 5-7 pallets up to 1,000 lb each, with exclusions (more than one shipment on a pallet; mixed pallets and loose pieces; pallets over 48 in; 20,000 lb or more); Item 610 absolute minimums for partner zones ($102.75-$324.75); liability limits by reference to SEFL 1090. The undated pallet table adds columns **"Fuel included in rate: NO", "Includes loose pieces: NO", "Subject to general rate increase: YES"**. The accessorial exceptions (effective 2021-04-07): liftgate $30 direct-to-direct, $55 to or from partners; limited access $25/$50; inside delivery $25; notification $0/$7.50; reconsignment $30; redelivery $80. Marked "PROPRIETARY AND CONFIDENTIAL PROPERTY OF SOUTHEASTERN FREIGHT LINES" | The **SEFL-0550 base rate table** itself | Possibly in segment (size unknown) | **real**, *verified* |
| SMC3 **CzarLite** base rates | smc3.com (N-AC34) | "the most widely used neutral LTL base rate … for thousands of successful shipper, carrier and logistics service provider (LSP) pricing agreements"; sold through RateWare XL and APIs; **price and re-rating licence terms not published** ("contact SMC³") | The tables | — | *verified* (page extraction); licence *assumed* paid |
| State or university LTL contracts with published discounts | — | **Not found** (one search) | — | — | — |

### 3.2 TL rate confirmations

| Document | Where | Fields | Label |
|---|---|---|---|
| **C.H. Robinson "Contract Addendum and Carrier Load Confirmation"** #218316538 (Sacramento CA to Salt Lake City UT, 2016-12-08) | *Miller v. Costco*, D. Nev. 3:17-cv-00408, Doc 130-8, Exhibit H (N-AC08) | Load number; carrier; equipment ("Van - Min L=53"); customer requirements; shipper, pickup date and **appointment time**; commodity, est. weight 14,062 lb, 30 pallets, reference; receiver and delivery date; **"Line Haul - FLAT RATE" $1,373.00**; "C.H. Robinson has included a **$136.08 fuel surcharge within the listed transportation rate**" (9.9% [our calc]); billing address; **"Detention at Costco is based on the computer printed 'in time' and 'out time' listed on the Costco Depot signature label"**; "$250 fine per occurance" for appointment failures | **real**, *verified*; broker to carrier |
| C.H. Robinson load confirmation #390013200 (Charleston SC to Sioux Falls SD, 2022-02-28, 42,984 lb brake drums, 18 pallets) | *Atkinson v. Super Ego Holding*, N.D. Ill. 1:22-cv-04127, Doc 21-5, Exhibit E (N-AC09) | Same layout; **linehaul flat $4,800.00, of which $688.08 fuel** (14.3% [our calc]); "all billing must be accompanied by an invoice with the Carrier Name and C.H. Robinson Load Number"; **"Accessorial charges (including but not limited to labor, detention, and/or layover charges) must be authorized and approved prior to or at time of occurrence"**; "Carrier shall ensure the bill of lading is notated … when detention occurs, that a lumper receipt is provided when a lumper is hired"; "Rate may be reduced if load picks up or delivers after originally scheduled time" | **real**, *verified*; broker to carrier |
| Broker-to-shipper quotes or shipper-to-carrier TL rate sheets or bid awards | — | **Not found** | — |

**Reading [our call]:** these confirmations are the broker's cost side. A C-09 shipper that books TL through a broker sees the broker's own invoice and quote, not this page. For shipper-to-carrier TL, the public rulebook is the carrier tariff (Werner, §3.4).

### 3.3 Fuel-surcharge tables and the index

| Table | Where | Structure | Label |
|---|---|---|---|
| **YRC-First Brands contract table** | N-AC05 | EIA Monday price bands of 5¢ → +0.30% each; effective Monday-Sunday of the next week | **real**, *verified* |
| **DOE ATLAS (Department of Energy's own freight programme), CY2025 weekly quick reference** | N-AC21 | For each Monday review date: national diesel price, **LTL FSC %**, **TL FSC $/mile**, effective Wednesday. Example: 2025-12-29 $3.500 → 13.5% and $0.26/mile, effective 2025-12-31 | **real** (government shipper), *verified* |
| **GSA fuel surcharge** (effective 2021-10-01) | N-AC19 | Neutral at $2.50 and below; +1% per 13¢ band ($2.501-2.630 = 1.0% … $5.361-5.490 = 23.0%); applies to shipments "picked up the ensuing Wednesday through the following Tuesday"; "shipment pickup date is controlling" | **template** (government), *verified* |
| **Werner TL tariff**, effective 2025-10-14, Item 310 | N-AC24 | **$ per mile** by DOE band (e.g., $2.55-2.599 → $0.30; $4.00-4.049 → $0.59); "effective for loads dispatched Monday through Sunday based on the DOE National Average price released on Monday of that Week" | **template** (public tariff), *verified* |
| **XPO LTL** | N-AC22 | Rates "published each Tuesday" by EIA and "become effective on the following Monday"; shown 2026-09-21: **LTL CNWY 190 56.75%**, volume shipments 113.50%; band examples $3.500 → 30.00%, $6.285 → 56.75%; volume table applies at 15,000 lb or more | *verified* (page extraction) |
| **Estes LTL** | N-AC23 | EIA price "updated every Tuesday", effective "the following Wednesday"; 0.1% per 2¢ below $3.61, 0.2% per 2¢ above; table PDF and a "History" tab (history content did not load) | *verified* (page extraction) |
| **EIA weekly U.S. No. 2 diesel retail price** (the index) | N-AC25 | Weekly since 1994, e.g., 2021-11-29 $3.720; 2024-07-01 $3.813 | *verified* |

**Reading [our call]:** the index is public; **the table in force on the ship date is not**. Carriers publish today's table. The XPO bills' percentages (24.60% at about $2.53-2.56 in December 2020; 30.50-31.25% at $3.61-3.72 in late 2021) cannot be checked against XPO's current page, whose bands have moved. Carriers also differ on **which week applies** (XPO: the Monday after publication; Estes and GSA: the Wednesday; Werner: the same week). A look-back needs the shipper's contract table, or the carrier's historical table, plus the pickup date.

### 3.4 Accessorial price schedules

| Schedule | Where | Examples | Label |
|---|---|---|---|
| YRC-First Brands Schedule B | N-AC05 | See §3.1; rule "Carrier must have authorization … and is responsible for retaining documentation" | **real**, *verified* |
| SEFL accessorial exceptions for Exist | N-AC03 | Liftgate $30/$55 by lane type; redelivery $80; all "Subject to general rate increase: NO" | **real**, *verified* |
| **Werner TL tariff** (2025-10-14) | N-AC24 | Stops in transit $150 first, $175 second, $250 third, $400 each after; **tractor detention: 2 hours free, then $110.00 per hour, free time from "the truck's arrival date/time, or the appointment date/time, whichever is later"**; load/unload "face value of lumper receipt or a minimum … of $150"; layover $350; multiple invoices $75 per extra consignee; **overcharge claims "within 180 days of shipment date"** | **template** (public tariff), *verified* |
| GSA Uniform Rules Tariff 200-A | N-AC20 | Detention per 15 minutes; reweigh fee; timestamp rule (§1.6) | **template**, *verified* |
| LTL carrier rules tariffs (ODFL, FedEx Freight, XPO, Estes, Saia, ABF, R+L, TForce, SEFL) | check T §3 (N-T17 to N-T30) | Reweigh and inspection fees $15-55; proof rules | *verified* in check T |
| Schneider tariff page | schneider.com/tariff (N-AC39) | Snippet only: liability terms | *assumed* |

### 3.5 BOLs and PODs

| Document | Where | Fields | Label |
|---|---|---|---|
| **Estes VICS bill of lading** (blank) | N-AC26 | Ship from, ship to, third-party bill-to, BOL number, carrier and SCAC, trailer and seal numbers, PRO number, freight terms (prepaid, collect, third party), customer order lines (packages, weight, pallet/slip), handling unit and package quantities and types, weight, hazmat, commodity, **NMFC # and class (LTL only)**, declared value, "Trailer Loaded: By Shipper / By Driver", **"Freight Counted: By Shipper / By Driver/pallets said to contain / By Driver/Pieces"**, shipper and carrier signatures | **template**, *verified* |
| **Filled VICS short-form BOLs** for XPO shipments, 2020-2021 | N-AC02 | As above, filled: 1 pallet, 200 lb, class 60, NMFC blank, prepaid, "Freight Counted: By driver/pieces", pickup date; signatures redacted by us (not copied) | **real**, *verified* |
| **UPS Freight straight bill of lading** (2018) | N-AC07 | Per-line weight and class; dimensions written per piece; **"TOTAL CUBE"**; NMFC column; additional-services tick boxes (inside delivery, liftgate, residential, notification, sort and segregate); COD; excess-liability declaration; PRO sticker; shipper and driver signatures | **real**, *verified* (page image); contains a private person's name and phone, not copied |
| **XPO delivery receipt** ("XPO CONTRACTUAL COPY") | N-AC02 | PRO; equipment number; date; origin and destination terminals; consignee; shipper; shipper numbers; pieces, hazmat, description, weight, "PPD"; **"RECEIVED … PIECES ABOVE DESCRIBED FREIGHT IN GOOD ORDER EXCEPT AS NOTED"**; **"SHRINK WRAP INTACT?"**; delivered pieces and **time** box; inside delivery, liftgate, residential, construction tick boxes; consignee signature and date; "SUBJECT TO … TARIFF CNWY-199" | **real**, *verified* |
| **Yellow delivery receipt** (2008) | N-AC06 | **"WAIT TIME START / END"** boxes; service tick boxes; signature | **real**, *verified* |

### 3.6 Weight and inspection certificates

**No public example was found**, in court filings, carrier pages or vendor blogs. What is public:
- **Pointers on real bills:** ABF "W02/AUTH:Reweigh - See W&R certificate for details." and "ABF MEASURED CUBE: 48.890 CUFT"; XPO "RE-WEIGHED PER WEIGHT CERTIFICATE" (N-AC04, N-AC02).
- **Document types in carrier portals and APIs** (Inspection Certificate, Weight Certificate, W&R photos, NMFC Certificate), linked to the bill-to party: check T §1 row 5 and §3.2.

### 3.7 Shipper-carrier agreements filed with the SEC

| Search (EDGAR full-text, via the fetch tool, no identity) | Hits | Useful? | Label |
|---|---|---|---|
| "transportation services agreement" + "fuel surcharge" + "accessorial" | 6 (Heartland Express 10-Qs; Martin Midstream affiliate master transportation agreement 2019; A&P-C&S supply agreement 2011) | No shipper-carrier pricing | *verified* (search results) |
| "motor carrier transportation agreement" | 25 (mostly Power2Ship and Furia Organization, 2004-2008 micro-caps) | Power2Ship Ex. 10.32 (2006) is a **broker-carrier template**: carrier paid "within fifteen days" of receiving "CARRIER's freight bill, bill of lading, clear delivery receipt"; carrier disputes within "ninety (90) days"; "claims of Five Dollars ($5.00) or less" not corrected; **no rate schedule** | *verified* (page extraction), **template** |
| "fuel surcharge" + "detention" + "bill of lading" + "carrier" + "shipper" + "accessorial" | 20; three EX-10 (Furia matrix 2005; Sears Hometown services amendment 2016; NEDAK Ethanol 2007) | Sears Hometown: an affiliate services agreement, invoicing and 120-day stale-claim terms, no freight rates | *verified* (page extraction) |

**Reading [our call]:** public companies rarely file carrier contracts as exhibits, and mid-sized private shippers file nothing. **Bankruptcy dockets and commercial lawsuits are the public route to real agreements.**

---

## 4. AC4 · Public datasets of real shipments with freight charges

| Dataset | Real or synthetic | Fields | Size | Licence | Use for practising a look-back | Label |
|---|---|---|---|---|---|---|
| **ABF claim set** (IN Holdings Doc 920, Exhibit 2) | **Real** | Every field in §1.1 I-3 | 101 distinct LTL bills, 3 months | Public court record | **Best available practice file:** duplicates, math, FSC base, AMC, deficit weight, reweigh flags, detention without times, 3PL payment. No agreement, BOLs or W&R certificates | *verified* |
| **Exist v. SEFL exhibits** | **Real** (bills, agreement) plus the shipper's spreadsheets | About 75 pages of bills; 3 pricing-agreement versions; 3,645 spreadsheet rows (customer, invoice no., date, pallets, liftgate, surcharge, freight charge, "need to be charged", "over charge") | 224 pages | Public court record | **Only public set that pairs bills, the agreement and a shipper's own audit.** Spreadsheet needs OCR clean-up | *verified* |
| **XPO claim set** (Vital Pharmaceuticals Doc 533-7) | **Real** | 6 invoices + BOLs + delivery receipts | 6 shipments | Public court record | Matching invoice ↔ BOL ↔ POD; reweigh fees; late fees | *verified* |
| **USAID "Supply Chain Shipment Pricing Data" (SCMS Delivery History)** | **Real** (US government health-commodity shipments) | 33 columns incl. PO/SO, ASN/DN, country, vendor, INCO term, **shipment mode** (Air 6,113; Truck 2,830; Air Charter 650; Ocean 371; N/A 360), scheduled and delivered dates, product, line value, **weight (kg)**, **freight cost (USD)**, insurance | **10,324 rows**, deliveries 2006-2015 [our calc from dates]; freight cost numeric in 6,198 rows, others say "See ASN…", "Freight Included in Commodity Cost" or "Invoiced Separately" | Original portal offline; mirrors say the source "did not include an explicit license" (snippet) | Cost-per-kg outliers and cross-reference checks only. **International, no carrier, rate agreement or accessorial lines. Out of scope** | CSV *verified* via a GitHub mirror (N-AC29); provenance *assumed* |
| **City of Chicago "Payments"** (Socrata s4vu-giwb) | Real (municipal) | Voucher number, amount, check date, contract number, vendor name | FedEx Freight 15 payments ($2,853.51), ABF 1 ($1,650) | Open data | Duplicate test on amount + date only; **no PRO or invoice number**. Government shipper, **out of segment** | *verified* (API) (N-AC30) |
| **Vermont SFY2017 Vendor Payments** | Real (state) | Quarter ending, department, vendor, amount, account, fund | Quarterly totals | Open Database License | **Aggregated; unusable** for invoice-level tests. Out of segment | *verified* (metadata) (N-AC31) |
| **USDA AMS Specialty Crops National Truck Rate Report** (weekly) | Real (market survey) | Origin district, destination city, truck availability, **rate range per load** for 48-53 ft reefers, % change | ~6 pages weekly; e.g., Imperial/Coachella lettuce to Chicago $6,400-6,700 (2026-09-15) | US government | **TL spot-rate benchmark** (farm-origin reefer), not invoices. Ties to the origin hypothesis | *verified* (N-AC32) |
| Kaggle "freight invoice" or LTL audit datasets | — | **None found**; general "Invoice Dataset", "Cargo 2000", "DataCo Smart Supply Chain" (retail e-commerce shipping, provenance not checked) | — | — | — | *assumed* (snippets) |
| ATRI, FMCSA | — | ATRI publishes operating cost per mile, not shipment rates; FMCSA registration and safety files carry no rates | — | — | None | *assumed* (memory) |

---

## 5. AC5 · Annotated error examples

### 5.1 Real

| # | Case | What is marked | Numbers | Who says so | Document | Label |
|---|---|---|---|---|---|---|
| E-1 | **Exist, Inc. v. Southeastern Freight Lines** (filed Miami-Dade 2025-10-07; removed to S.D. Fla. 2026-01-06; SEFL moved to dismiss 2026-01-16; the court's 2026-02-12 order was not available) | Per invoice: "FRT CHARGE" vs "Need to Be Charged", difference in "OVER CHG". The complaint alleges bills that "substantially exceeded the SEFL shipping quotes" and "double invoices and … erroneous billings filled with multiple billing mistakes" | Three sheets: **2021 (rows to 1,866) $131,987.80; 2022 (rows to 1,383) $109,577.87; 2023 (Jan-May, 398 rows) $30,263.03. Sum $271,828.70, exactly the amount claimed** [our calc]; about $74.58 per invoice [our calc]. From OCR of about 94% of rows: **the claimed overcharge is about 22-25% of billed base freight and about 16-20% of base + fuel + liftgate** [our calc, approximate]. The 2023 sheet lists 2 invoice numbers twice (rows 95/99, 96/100) | The shipper (plaintiff) | Spreadsheet print-outs, the bills and the agreement | Documents **real**, *verified*; **overcharges *assumed*** (unproven) |
| E-2 | **In re IN Holdings, objection to ArcBest's Claim No. 2** | The debtor says the 107 invoices "were already paid by one of the Debtors' logistics providers, TLS Transportation", and that ArcBest "was never directly in privity of contract with the Debtors" | Claim $45,652.49 for bills dated 2024-05-09 to 08-09 | The debtor (objector) | 101 real ABF bills | Bills **real**, *verified*; "already paid" *assumed* |
| E-3 | **Central Freight Lines v. Amazon Fulfillment Services** (W.D. Wash. 2017, complaint) | Amazon's 2016 audit demanded **$2,389,538** because "a 30 percent discount was not applied to the 8 Pallet Shipments" (2012-June 2016), later reduced to **$1,302,440** because "the Agreement provides that all claims by Amazon must be filed within 18 months of the original invoice"; also a dispute over billing same-day, same-destination BOLs as one shipment | ≈46% of the demand fell outside the contract's claim window [our calc] | The carrier (plaintiff), describing the shipper's audit | Complaint text; the demand letter exhibit was not read | *assumed* (one party's account); out of segment |
| E-4 | XPO bills in Vital Pharmaceuticals | Reweigh fees plus "RE-WEIGHED PER WEIGHT CERTIFICATE"; corrected and balance-due invoices; late fees for 30-180 days past due | Reweigh fees $35.25-$39.40 | Carrier's own bill | **real** | *verified*; not alleged to be wrong |
| E-5 | ABF bill 150256193 | Detention added on a corrected invoice with no times printed | $42.71 | Carrier's own bill | **real** | *verified*; not alleged to be wrong |

### 5.2 Templates and vendor material

| Source | What | Label |
|---|---|---|
| 3M EDI 210 guide | A re-bill with B308 = "BE" (Billing Error) and K1 "USED OLD PRICE GUIDE": fuel line changed from $125.64 to $150.00 | **template**, *verified* |
| Vendor and broker blogs (FreightSimple, Nuvocargo, GingerControl, TransImpact, FreightPOP, Packizon and others) | Lists of error types (fuel on the wrong index, duplicates, reweigh upcharges, unauthorised accessorials) and ranges ("5–8% in manual programs") in text. **No annotated real invoice image found** | *assumed* (vendor claims, snippets) |

**Reading of E-1 [our call]:** the shipper's worksheet compares each bill with a per-pallet rate. The agreement's own pallet table says those rates are **"Subject to general rate increase: YES"** and **exclude** mixed pallets and loose pieces, pallets over 48 in and heavy pallets. Whether the "need to be charged" column allowed for those rules is not shown. Many 2021 rows show small gaps ($6.25-$7.50 on a $104.50-$110.75 base). **A look-back that ignores such clauses can overstate recoveries; a carrier will cite them.** This is a question for the savings assessment's method, not a finding about this case.

---

## 6. AC6 · What is not publicly available

| Document the look-back needs | Public example? | If not public: the exact ask | Likely format | Who holds it at the shipper | Privacy / NDA |
|---|---|---|---|---|---|
| **Paid LTL invoices** | Yes, but only other shippers' (§1.1) | "Your LTL carrier invoices for [3 recent months], every page, including corrected and balance-due bills" | PDF by email or portal download; EDI 210 files; FAP or TMS export | AP clerk or controller; logistics coordinator if a TMS audit tab is used | Consignee names are customers: accept redacted or coded consignees; carrier bank remit details not needed |
| **Paid TL invoices** (asset carriers) | **No** | "Your truckload invoices for the same months, with the rate confirmation or quote for each load" | PDF with rate con attached; broker portal | AP; transportation or purchasing lead | Same |
| **Broker and 3PL bills** | **No** (bill-to agents appear on real bills: ITS Traffic Systems, Blue Grace, TLS) | "If a broker or 3PL pays carriers for you, their invoices to you and the carrier bills behind them if you receive them" | PDF statement; 3PL portal | AP; logistics | 3PL margin is sensitive: ask only for what you are billed |
| **Rate agreements, every version in force** | Yes (two real, §3.1) | "Each carrier pricing agreement or rating item with its effective date, including any superseded version that covers the months we check" | PDF from carrier sales rep; email attachment | Logistics or purchasing; sometimes only the carrier rep | Carriers mark them "proprietary and confidential": check the agreement's confidentiality clause; offer an NDA |
| **Base rate table** (CzarLite or carrier base such as SEFL-0550) | **No** (licensed or proprietary) | "Do you have RateWare, CzarLite or the carrier's rating tool? If not, can you get per-shipment rate quotes or the carrier's re-rate for a sample?" | Software; quote PDFs | Rarely held by a mid-sized shipper [our call] | SMC3 licence terms unknown (§3.1) |
| **Quotes and spot or volume quotes** | Quote numbers appear on bills (SEFL "QUOTE #", ABF "PQ SCHEDULE NO") | "The quote emails or PDFs referenced on these bills" | Email; carrier website quote history | Shipping clerk; customer-service rep | — |
| **Fuel table in force** | Index yes; carrier's historical table mostly no | "The fuel schedule in your agreement, or the carrier's table for those weeks" | Contract schedule; carrier PDF | Logistics | — |
| **Accessorial schedule and exceptions** | Yes (tariffs; two contracts) | "Any accessorial exceptions or waivers you negotiated (liftgate, detention, reweigh fees)" | Contract schedule | Logistics | — |
| **BOLs** | Yes (filled real examples) | "Your BOL copies for the sampled shipments, as printed or from your shipping software" | Shipping software export; scans | Shipping or warehouse | Customer names on BOLs |
| **PODs / delivery receipts** | Yes (real examples) | "Delivery receipts for the sample, or permission to download them from carrier portals as your agent" | Carrier portal PDF | Nobody at the shipper, often [our call]; carrier portal as bill-to party (check T) | Consignee signatures: do not retain names |
| **W&R / inspection certificates and photos** | **No** | "For every reweighed or reclassed bill, the carrier's certificate, or portal access to pull it" | Carrier portal PDF and images | Carrier; sometimes the logistics lead | — |
| **Detention evidence** (arrival and departure times) | **No** (only rules: GSA stamp rule; Costco "in time/out time" label) | "Your dock or gate log, appointment system records or yard check-in times for bills with detention" | Dock-scheduling export; paper gate log | Warehouse or receiving supervisor | Driver names on logs |
| **Lumper receipts** | **No** | "Lumper receipts for bills with lumper or unloading charges" | Paper or PDF from consignee | Rarely held; consignee or carrier | — |
| **Spec sheets and packing lists** (proof for reclass or reweigh disputes) | Rules only (check T) | "Pre-printed spec sheet or catalog page with shipping weight and dimensions for the items in the sample" | Product master data; catalog PDF | Product or operations | Product data is commercial: NDA |
| **AP payment records** | Format only (Chicago file) | "AP export for the freight vendors: vendor, invoice number, invoice date, amount, date paid, check or ACH reference, any short-pay" | CSV or Excel from ERP | AP clerk; controller | **Remove bank account and routing numbers**; keep payment reference only |
| **Carrier statements of account** | Yes (SEFL "past due" and "balance due" bills) | "Each carrier's current statement or open-items list" | Carrier portal; email | AP | — |
| **Carrier contracts and terms** (claim windows, audit rights) | Yes (YRC contract) | "Your signed transportation agreements with carriers or brokers" | PDF | Owner, controller or logistics | Confidentiality clauses |
| **Dispute and credit history** | **No** | "Any disputes, short-pays or credit memos with carriers in the last 12 months, and their outcomes" | Email threads; credit memos; claims portal | Logistics or AP | — |
| **Existing audit reports** (FAP, TMS audit tab, contingency firm) | **No** | "Any audit report or exception list from a current provider or tool" | PDF or portal export | Controller or logistics | May be under the provider's terms |

---

## 7. Document register

| Document type | Example found? (link) | Real / mock / template | Fields visible | Usable for practising the audit? | Label |
|---|---|---|---|---|---|
| LTL invoice, XPO | [Doc 533-7](https://storage.courtlistener.com/recap/gov.uscourts.flsb.797115/gov.uscourts.flsb.797115.533.7.pdf) (N-AC02) | real | §1.1 I-1 | Yes: math, discount, FSC base, reweigh fee, late fees; matched BOL and POD | *verified* |
| LTL freight bill, SEFL (2020-2023 shipments; some rebilled or reprinted in 2025) | [Doc 1-2 Ex. A](https://storage.courtlistener.com/recap/gov.uscourts.flsd.704429/gov.uscourts.flsd.704429.1.2_3.pdf) (N-AC03) | real | §1.1 I-2 | Yes: against the real agreement | *verified* |
| LTL invoice, ABF | [Doc 920 Ex. 2](https://storage.courtlistener.com/recap/gov.uscourts.cacb.1993985/gov.uscourts.cacb.1993985.920.0_1.pdf) (N-AC04) | real | §1.1 I-3 | **Yes, 101 bills**: duplicates, math, FSC, AMC, deficit weight, reweigh flags, detention | *verified* |
| LTL delivery receipt as freight-bill form, Yellow | [Doc 6033-2](https://storage.courtlistener.com/recap/gov.uscourts.vaeb.476891/gov.uscourts.vaeb.476891.6033.2.pdf) (N-AC06) | real | §1.1 I-4 (rates blank) | POD only | *verified* |
| TL invoice, asset carrier | Not found | — | — | — | — |
| TL invoice template | InvoiceQuick, Enerpize, CarrierInvoice (N-AC39) | mock / template | Linehaul, fuel, detention hours × rate, layover, lumper, TONU | Only to design fields | *assumed* |
| EDI 210 specifications | 3M, Cardinal, TForce, ABF, Estes, R+L, Pitt Ohio (N-AC11 to N-AC17) | template | §2 | Yes, to design a parser | *verified* |
| LTL contract (shipper-carrier) | [YRC-First Brands](https://storage.courtlistener.com/recap/gov.uscourts.deb.198600/gov.uscourts.deb.198600.1.1.pdf) (N-AC05) | real | Terms, accessorials, FAK, fuel table, windows; **no pricing schedule** | Yes: rules and fuel | *verified* |
| LTL pricing agreement (rating item) | SEFL for Exist, pp. 12-22 of N-AC03 | real | Discounts, FAK, minimums, pallet rates, accessorial exceptions, effective dates | Yes | *verified* |
| Base rate table | Not public (CzarLite, N-AC34) | — | — | No | *assumed* |
| TL rate confirmation (broker-carrier) | [CHR 2016](https://storage.courtlistener.com/recap/gov.uscourts.nvd.123884/gov.uscourts.nvd.123884.130.8.pdf), [CHR 2022](https://storage.courtlistener.com/recap/gov.uscourts.ilnd.418007/gov.uscourts.ilnd.418007.21.5.pdf) (N-AC08, N-AC09) | real | §3.2 | Structure only | *verified* |
| Fuel tables | YRC contract; [DOE ATLAS 2025](https://atlas.doe.gov/RateRoute/FuelSurcharge/2025CurrentFSCMatrix.pdf); [GSA](https://www.gsa.gov/system/files/Fuel%20Surcharge%20(effective%2010-1-21).pdf); [Werner](https://www.werner.com/wp-content/uploads/2025/10/Tariff-Effective-10-14-2025.pdf); XPO; Estes | real (contract, DOE); template (GSA, Werner); public (XPO, Estes) | §3.3 | Yes, with EIA series | *verified* |
| Diesel index | [EIA weekly](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMD_EPD2D_PTE_NUS_DPG&f=W) (N-AC25) | real | Weekly price | Yes | *verified* |
| Accessorial schedules | YRC; SEFL; Werner; [GSA 200-A](https://www.gsa.gov/system/files/GSA%20No_200-A%20Uniform%20Rules%20Tariff.pdf); LTL rules tariffs (check T) | real and template | §3.4 | Yes | *verified* |
| BOL | [Estes VICS blank](https://www.estes-express.com/dA/020c7fc70d/EstesVICSbol.pdf); filled VICS (N-AC02); UPS Freight (N-AC07) | template; real | §3.5 | Yes | *verified* |
| POD / delivery receipt | XPO (N-AC02); Yellow (N-AC06) | real | §3.5 | Yes | *verified* |
| Weight or inspection certificate | Not found | — | — | — | — |
| Detention time record | Not found (rules only: GSA 200-A; CHR/Costco label rule) | — | — | — | *verified* (rules) |
| Shipper's own audit worksheet | Exist sheets, pp. 99-224 of N-AC03 | real (allegation) | Invoice no., date, pallets, liftgate, fuel, charge, should-be, over | Yes: compare method | *verified* |
| AP / payment records | [Chicago payments](https://data.cityofchicago.org/resource/s4vu-giwb.json) (N-AC30) | real (government) | Voucher, amount, date, vendor | Weak | *verified* |
| SEC carrier agreements | Power2Ship Ex. 10.32 (N-AC36) | template | Payment and dispute terms, no rates | No | *verified* |
| Shipment cost dataset | [USAID SCMS mirror](https://raw.githubusercontent.com/jrcinco/supply-chain-shipment-price-data/HEAD/SCMS_Delivery_History_Dataset.csv) (N-AC29) | real (out of scope) | §4 | Weak | *verified* |
| Government payment and audit rules | 41 CFR 102-118.285; GSA 200-A; CA SAM 3851 | template (rules) | §1.6 | Checklist only | *verified* |

---

## 8. Field map: what each error check needs, and where the field lives

"Invoice" = the carrier bill (PDF or EDI 210). **Bold "shipper only"** = only obtainable from the shipper (or with its authority from the carrier), never public.

| Error type | Fields needed | Carried by | Public example of the field? | Obtainable from |
|---|---|---|---|---|
| **Duplicate** | PRO / invoice no.; invoice date; amount; BOL no.; PO; ship date; payee; **date paid, payment reference** | Invoice (B302, B303, B306, B307, N9); **AP payment record** | Invoice fields yes (all three sets); ABF set contains 6 repeated copies; payment fields only in government files | Invoice: shipper or carrier portal. **AP record: shipper only** |
| **Rate ≠ agreement** (LTL) | Lane (origin and destination ZIP); weight; billed class; **agreement version effective on ship date** (discount, FAK, AMC, pallet rates, exclusions, GRI clause); **base rate table**; quote number | Invoice (L0, L1, L7, N4); **agreement**; **base tariff** | Agreement examples yes (SEFL, YRC); base tables no | **Agreement: shipper only.** **Base rates: licensed (SMC3) or the carrier's quote** |
| **Rate ≠ agreement** (TL) | Load no.; stops; miles; linehaul; **rate confirmation or contract lane rate** | Invoice; **rate con or contract** | Rate con examples (broker to carrier) yes | **Shipper only** (rate cons, bid awards) |
| **Fuel surcharge misapplied** | Pickup date; FSC % or $/mile; charge base (net linehaul vs accessorials); miles (TL); **fuel table in the contract** or the carrier's table for that week; EIA price and the effective-day rule | Invoice (L1 FUE); **contract fuel schedule**; EIA | Yes: EIA series; DOE, GSA, Werner, contract tables; bills show FSC on net linehaul | EIA public. **Contract table: shipper only.** Carrier's historical table: carrier |
| **Unapproved accessorial** | Accessorial code and amount; **agreed accessorial schedule and waivers**; **authorisation record**; BOL service tick boxes; delivery receipt notes | Invoice (L1 L108); **contract**; BOL; DR; **approval email or TMS booking** | Schedules yes; BOL and DR tick boxes yes; authorisation records no | **Shipper only** (approvals, contract exceptions) |
| **Detention without timestamps** | Detention line (hours, rate); **free-time rule**; **arrival, appointment and departure times**; who caused the delay | Invoice (often no times: ABF example); tariff or contract; **DR "wait time" boxes; dock or gate logs** | Rules yes (Werner, GSA, YRC); DR boxes yes; real time records no | **Shipper only** (gate log, appointment system); DR from carrier portal |
| **Reweigh / reclass without proof** | Billed weight and class; **BOL weight, class, NMFC item, dimensions**; **W&R or inspection certificate** (device, date, measurements, photos); reweigh fee; corrected-invoice flag; **spec sheet or packing list** | Invoice (K1 remarks, B308, L0, L4, L7); **BOL**; **carrier certificate**; **shipper product data** | Invoice pointers yes (ABF, XPO); BOL examples yes; certificates no | BOL: **shipper**. **Certificate: carrier portal (bill-to party).** **Spec sheets: shipper only** |
| **Math / extension** | Rate × rated weight; deficit weight; discount; minimum charge; line totals | Invoice alone | Yes: all four worked bills in §1.2 | Invoice |
| **Late fees** (seen on XPO bills; not in the kit's list) | Payment due date; **date paid**; late-fee rule in tariff or agreement | Invoice; **AP record**; tariff | Late-fee lines yes | **AP record: shipper only** |
| **Paid twice through a 3PL or broker** (E-2) | Carrier bill; **3PL invoice to shipper**; **3PL's payment to carrier** | Carrier bill; **3PL documents** | Bill-to agents visible on bills | **Shipper and its 3PL only** |
| **Recoverable or time-barred** | Ship date; bill date; **contract claim window** (YRC 180 days; Amazon-Central Freight 18 months); statute (check T §4) | Invoice; **contract** | Contract examples yes | **Contract: shipper only** |

---

## 9. Interview and assessment request list (for the founders to use)

**In the interview (block E, "Data"), past behaviour only [our call]:**
1. "When a carrier bill arrives, where does it land: email, carrier portal, EDI, a 3PL? Can you show me last month's?"
2. "Which of your carriers bill you directly, and which go through a broker or 3PL?"
3. "Where are your carrier pricing agreements kept? When did you last open one, and why?"
4. "Last time a bill had a reweigh, reclass or detention charge, what did you do? Did you get the carrier's certificate or the times?"
5. "Does anyone record truck arrival and departure times at your dock? Where?"
6. "Has a carrier ever billed you twice, or billed you after a 3PL paid? How did you find out?"
7. "Do you ever pay late fees on freight bills?" (XPO bills show them.)

**For the savings assessment (kit §6.1), the data request [our call]:**

| # | Ask | Minimum | Nice to have | Format | Holder | Privacy note |
|---|---|---|---|---|---|---|
| R1 | Carrier invoices, all pages, for 3 months | LTL + TL, incl. corrected and balance-due bills | 6 months, to see rebills | PDF or EDI 210 files or TMS export | AP / logistics | Consignee names may be coded |
| R2 | AP payment export for freight vendors, same months | Vendor, invoice no., invoice date, amount, paid date, payment reference | Short-pays, credits | CSV / Excel | AP / controller | **Strip bank account and routing numbers** |
| R3 | Every pricing agreement and rating item in force in those months, with effective dates | Top 3 carriers by spend | All carriers, prior versions | PDF | Logistics / purchasing | NDA; carrier confidentiality clauses |
| R4 | Accessorial exceptions, fuel schedule, claim window from each contract | As in the agreement | Carrier rules tariff version | PDF | Logistics | — |
| R5 | TL rate confirmations or broker quotes per load | For every TL bill in the sample | Bid award sheet | PDF / email | Transportation lead | — |
| R6 | BOLs for a sample of ≥50 shipments | Shipper's printed BOLs | Shipping-software export with dims and class | PDF / CSV | Shipping | Customer names |
| R7 | Authority to download PODs and W&R / inspection certificates from carrier portals as agent | For reweigh, reclass and detention bills | All sampled shipments | Letter of authority | Owner / controller | Keep signatures out of work files |
| R8 | Dock or gate logs, or appointment-system records | For bills with detention | All sampled days | Export / scans | Receiving supervisor | Driver names |
| R9 | Spec sheets or catalog pages with shipping weight and dimensions | Items on reweigh/reclass bills | Product master | PDF / CSV | Operations | NDA |
| R10 | Carrier statements and any dispute or credit history | Last 12 months | Emails | PDF / email | AP | — |
| R11 | If a 3PL or broker pays carriers: its invoices to the shipper | Same months | Its carrier-payment proof | PDF | AP | 3PL margin |

**Practice before the first assessment [our call]:** run the §6.1 method end to end on the public ABF set (101 bills) and on a slice of the Exist set (bills + agreement + worksheet), and record the hours. Both are public court records.

---

## 10. For the coordinator (not a call)

1. **Real LTL invoices are public, through court records, not carriers.** Three sets (XPO 2020-21, SEFL 2020-25, ABF 2024) show the same core fields and let math, discount, fuel-base, minimum-charge and deficit-weight checks be run from the bill face alone (§1.2). **No carrier publishes a "how to read your invoice" page** (§1.5).
2. **A free, realistic 3-month practice sample exists:** 101 ABF bills for a supplement maker, May-Aug 2024. On it: **28% carry a reweigh note** pointing to a W&R certificate the bill does not include; 39 carry absolute-minimum adjustments; detention appears with no times; and all bills went to a 3PL that, per the debtor, had already paid them (§1.3, §5.1 E-2) [our calc; debtor's claim *assumed*].
3. **A mid-sized-looking manufacturer's own look-back is public:** Exist Inc.'s 3,645-row sheets against SEFL total **exactly the $271,828.70 it sued for**, about **22-25% of base freight** on the rows parsed [our calc]. It is an unproven allegation, and the agreement's "subject to general rate increase" and pallet exclusions show how a method can overstate recoveries (§5.1). The dismissal motion's outcome was not available.
4. **Pricing agreements do exist in public, with version dates.** One SEFL customer agreement has three versions (2021, 2022, 2023), and a real YRC contract includes accessorial, FAK and fuel schedules and **180-day** billing and claim windows. **The base rate tables they discount from are not public** (SEFL-0550; SMC3 CzarLite is licensed). So **LTL "rate ≠ agreement" cannot be re-rated without the shipper's quotes, a rating licence or the carrier's help** (§3.1, §8).
5. **Fuel is checkable only with the table in force on the pickup date.** The EIA index is public; carriers publish only today's table and differ on the effective day (XPO the following Monday, Estes and GSA the Wednesday, Werner the same week) (§3.3).
6. **No public TL carrier invoice, W&R or inspection certificate, detention time record or lumper receipt was found.** Those, plus AP payment records and dispute history, are interview or assessment items (§6, §9).
7. **EDI 210 guides are plentiful and consistent, but class, dimensions and POD are optional** (Estes marks them "Not Used"), and **TForce stops mailing BOLs and delivery receipts once a customer takes EDI**. An EDI shipper may hold cleaner bills and fewer proofs (§2).
8. **Two error types outside the kit's list appear on real bills:** late fees for 30-180 days past due (XPO) and payment through a 3PL that the carrier still bills (ABF). [our call] Whether to add them to kit §6.1 is for the founders.

---

## 11. Sources

All accessed 2026-09-17. "Full" means the document or its text layer was read (or searched in full); "extraction" means a fetch tool's model-made extract.

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-AC01 | CourtListener RECAP search API (type=rd), about 40 queries on carrier names, "freight bill", "fuel surcharge", "rate confirmation", "reweigh", docket listings for 6110866, 72108192 | run 2026-09-17 | https://www.courtlistener.com/api/rest/v4/search/ | full (JSON) | Hit lists, docket entries (Exist v. SEFL: MTD 2026-01-16, order 2026-02-12 not available) |
| N-AC02 | *In re Vital Pharmaceuticals, Inc.*, Bankr. S.D. Fla. 22-17842, Doc 533-7 (Exhibit 23: XPO Logistics Freight proof of claim 1-1, $14,879.18, with 6 LTL invoices, VICS BOLs, delivery receipts) | filed 2022-12-15 (claim 2022-10-13) | https://storage.courtlistener.com/recap/gov.uscourts.flsb.797115/gov.uscourts.flsb.797115.533.7.pdf | full (page images) | Invoices 712-591246, 712-591121, 405-677016, 405-634110, 326-343835, 976-973841; BOL; DR |
| N-AC03 | *Exist, Inc. v. Southeastern Freight Lines, Inc.*, S.D. Fla. 1:26-cv-20049, Doc 1-2 (state complaint, Exhibit A: SEFL rating items, pallet and accessorial tables, freight bills; Exhibit B: shipper worksheets) | complaint 2025-10-07; removed 2026-01-06 | https://storage.courtlistener.com/recap/gov.uscourts.flsd.704429/gov.uscourts.flsd.704429.1.2_3.pdf | full (OCR text + page images) | Complaint ¶¶5-27; pp. 12-23, 49, 99-224 |
| N-AC04 | *In re IN Holdings, Inc.*, Bankr. C.D. Cal. 1:24-bk-11323, Doc 920 (objection to ArcBest Claim No. 2 with 107 ABF invoices) | 2025-12-16 | https://storage.courtlistener.com/recap/gov.uscourts.cacb.1993985/gov.uscourts.cacb.1993985.920.0_1.pdf | full (text layer, script-parsed) | Objection pp. 1-7; all invoices |
| N-AC05 | Yellow Corporation adversary 25-51852, Doc 1-1, Exhibit A: YRC Enterprise Services "LTL Motor Carrier Transportation Contract" with First Brands Group (also 23-11069 Doc 7410-1) | contract 2021-03-15; filed 2025-08-05 | https://storage.courtlistener.com/recap/gov.uscourts.deb.198600/gov.uscourts.deb.198600.1.1.pdf | full (text) | Arts. 1-17, Schedules A-E |
| N-AC06 | *In re Circuit City Stores*, Bankr. E.D. Va. 08-35653, Doc 6033-2 (proof of claim #14349 exhibits: Yellow Transportation delivery receipts, manifest) | 2009-12-08 | https://storage.courtlistener.com/recap/gov.uscourts.vaeb.476891/gov.uscourts.vaeb.476891.6033.2.pdf | pages 1, 3 (images) | DR fields |
| N-AC07 | *UPS Freight, Inc. v. Complete Family Dental, LLC*, D.N.J. 1:19-cv-20524, Doc 1 (complaint with UPS Freight BOL) | 2019-11-20 | https://storage.courtlistener.com/recap/gov.uscourts.njd.421582/gov.uscourts.njd.421582.1.0.pdf | pages 8-12 (images) | BOL fields |
| N-AC08 | *Miller v. Costco Wholesale Corp.*, D. Nev. 3:17-cv-00408, Doc 130-8, Exhibit H (C.H. Robinson load confirmation #218316538) | 2021-07-29 (load 2016-12) | https://storage.courtlistener.com/recap/gov.uscourts.nvd.123884/gov.uscourts.nvd.123884.130.8.pdf | full (text) | Rate details, detention rule |
| N-AC09 | *Atkinson v. Super Ego Holding, LLC*, N.D. Ill. 1:22-cv-04127, Doc 21-5, Exhibit E (C.H. Robinson load confirmation #390013200) | 2022-11-07 (load 2022-02) | https://storage.courtlistener.com/recap/gov.uscourts.ilnd.418007/gov.uscourts.ilnd.418007.21.5.pdf | full (text) | Rate details, terms 1-7 |
| N-AC10 | *Central Freight Lines, Inc. v. Amazon Fulfillment Services*, W.D. Wash. 2:17-cv-00814, Doc 1 (complaint) | 2017-04-26 | https://storage.courtlistener.com/recap/gov.uscourts.wawd.245873/gov.uscourts.wawd.245873.1.0.pdf | pp. 1-9 (text) | ¶¶1-44 |
| N-AC11 | 3M, "210 Motor Carrier Freight Details and Invoice" 4010 carrier guidelines (3M-IB210-4010) | 2017-08-11 | https://multimedia.3m.com/mws/media/1056503O/210-freight-invoice-version-4010-edi-carrier-guidelines.pdf | full | Segments, B308, examples |
| N-AC12 | Cardinal Glass Industries, "210 Freight Invoice - 4010" v1.5 | 2015-05-29; notes 2024-05-28 | https://www.cardinalcorp.com/wp-content/uploads/2024/05/Technical-Guide-210-Freight-Invoice-Version2-4010.pdf | full (searched) | L1/L108 codes, L7 |
| N-AC13 | Pitt Ohio, EDI implementation guide, 210 | undated web page | https://pittohio.com/mypittohio/forms/example/210_Motor_Carrier_Freight_Details_and_Invoice | full | Segment usage |
| N-AC14 | TForce Freight, "210 Motor Carrier Freight Details and Invoice v4010 Specifications" | example dated 2000 | https://www.tforcefreight.com/downloads/TFF-210-4010.pdf | full | B308, example, business policies |
| N-AC15 | Estes Express Lines, 210 v4010 | 2008-08-12 | https://www.estes-express.com/dA/2f7a66fe-a154-4b42-8c5c-73c716165ce0/Estes210v4010.pdf | full (searched) | Segment usage ("Not Used") |
| N-AC16 | ArcBest, "EDI Specs 210" | 2024-12 | https://arcb.com/sites/www/files/2024-12/ArcBest-EDI-Specs-210.pdf | full | Example 210 |
| N-AC17 | R+L Carriers, "EDI File Format - EDI 210 Invoice" | undated | https://rl-cdn.com/docs/rlc/edi/210-rlc-format-invoice.pdf | partial (searched) | Heading, B308, POD, L4 |
| N-AC18 | FedEx, "EDI Invoicing and Remittance: 210 … 820 … 997" (Express and Ground) | revisions to 2022-12 | https://www.fedex.com/content/dam/fedex/us-united-states/services/Freight_210-4010_motor_carrier_freight_details_and_invoice_and_820_payment_order-remittance_advice.pdf | partial | Scope; L1 |
| N-AC19 | GSA, "Fuel Surcharge – Effective 10/1/21" | 2021-10-01 | https://www.gsa.gov/system/files/Fuel%20Surcharge%20(effective%2010-1-21).pdf | full | Table, timing |
| N-AC20 | GSA, Uniform Rules Tariff No. 200-A | 2021-10-01 | https://www.gsa.gov/system/files/GSA%20No_200-A%20Uniform%20Rules%20Tariff.pdf | full (searched) | Items 325, 1250 |
| N-AC21 | DOE ATLAS, "CY 2025 DOE Weekly Fuel Surcharge Quick Reference Guide" | 2025-12-30 | https://atlas.doe.gov/RateRoute/FuelSurcharge/2025CurrentFSCMatrix.pdf | full | Weekly LTL %, TL $/mile |
| N-AC22 | XPO, "Fuel Surcharge Table" | page shows 2026-09-21 | https://www.xpo.com/fuel-surcharge-table/ | extraction | Timing, bands, current % |
| N-AC23 | Estes, "Fuel Surcharge" | current | https://www.estes-express.com/resources/fees-and-surcharges/fuel-surcharge | extraction | Timing, increments |
| N-AC24 | Werner Enterprises, "Tariff Governing Rules, Regulations and Accessorial Charges" | effective 2025-10-14 | https://www.werner.com/wp-content/uploads/2025/10/Tariff-Effective-10-14-2025.pdf | full (searched) | Items 300-320, 585, accessorial table |
| N-AC25 | U.S. EIA, "Weekly U.S. No 2 Diesel Retail Prices" | through 2026-09 | https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMD_EPD2D_PTE_NUS_DPG&f=W | full | 2020-12, 2021-11/12, 2024-05 to 08 |
| N-AC26 | Estes, VICS bill of lading (blank PDF) | current | https://www.estes-express.com/dA/020c7fc70d/EstesVICSbol.pdf | full (text) | Fields |
| N-AC27 | 41 CFR 102-118.285 (LII) | current | https://www.law.cornell.edu/cfr/text/41/102-118.285 | extraction | (a)-(l) |
| N-AC28 | California State Administrative Manual 3851, "Audit of Freight Bills" | rev. 03/2007 | https://www.dgs.ca.gov/Resources/SAM/TOC/3800/3851 | extraction | Requirements |
| N-AC29 | USAID SCMS Delivery History Dataset, GitHub mirror (jrcinco); original data.usaid.gov unreachable | data 2006-2015 | https://raw.githubusercontent.com/jrcinco/supply-chain-shipment-price-data/HEAD/SCMS_Delivery_History_Dataset.csv | full (CSV) | Columns, counts |
| N-AC30 | City of Chicago, Payments (Socrata s4vu-giwb) | through 2025 | https://data.cityofchicago.org/resource/s4vu-giwb.json | full (API queries) | Carrier vendor rows |
| N-AC31 | State of Vermont, SFY2017 Vendor Payments (metadata) | 2017 | https://data.vermont.gov/api/views/8sss-k2wn.json | full (metadata) | Columns, licence |
| N-AC32 | USDA AMS, Specialty Crops National Truck Rate Report (FVWTRK) | 2026-09-16 | https://www.ams.usda.gov/mnreports/fvwtrk.pdf | full | Structure, sample rates |
| N-AC33 | Horizon Logistics, "LTL Training Manual – Module 1", hosted on Georgia Tech ISyE 6203 course page | 2010 | https://www2.isye.gatech.edu/~jvandeva/Classes/6203/LTL-Training-Manual---Module-1-(2).pdf | full (partly garbled text) | Weight breaks, deficit weight example, payment terms |
| N-AC34 | SMC3, "CzarLite LTL Base Rate" | current | https://www.smc3.com/czarlite.htm | extraction | Use, access; no price |
| N-AC35 | SEC EDGAR full-text search (efts.sec.gov), 6 queries, via the fetch tool with no identity | run 2026-09-17 | https://efts.sec.gov/LATEST/search-index?q=%22motor%20carrier%20transportation%20agreement%22 | JSON extraction | Hit lists (§3.7) |
| N-AC36 | Power2Ship, SB-2/A Ex. 10.32 "Motor Carrier Transportation Agreement" | 2006-05-05 | https://www.sec.gov/Archives/edgar/data/1082733/000109991006000081/ex10-32.txt | extraction | Payment, dispute, audit terms |
| N-AC37 | Sears Hometown & Outlet Stores, 8-K Ex. 10.3 (services agreement amendment) | 2016-05-17 | https://www.sec.gov/Archives/edgar/data/1548309/000119312516593208/d195136dex103.htm | extraction | Not a freight contract |
| N-AC38 | FreightSimple, "How to Read and Understand Your Freight Invoice" (broker) | 2024-10-07 | https://www.freightsimple.com/blog/how-to-read-freight-invoice | extraction | Sections, error list, no image |
| N-AC39 | Search snippets: carrier invoice explainer searches; trucking invoice templates (Enerpize, InvoiceQuick, Invoice Fly, CarrierInvoice); FCA 210 freight payment guide; Empower Data Logistics 210 guide; Schneider tariff page; DoD DTR Part II ch. 212 and Part IV App. A (TPPS); vendor error blogs (Nuvocargo, GingerControl, TransImpact, FreightPOP, Packizon); Kaggle dataset listings | 2024-26 | e.g. https://schneider.com/tariff ; https://www.business.ustranscom.mil/dtr/part-ii/dtr_part_ii_212.pdf ; https://ps.nafta.extra.fcagroup.com/sites/itb-ebus/Shared%20Documents/210FreightPaymentInvoice.pdf | snippet | Titles and summaries only |
| N-AC40 | GitHub, austinlasseter/datasets-shipping-logistics (README) | current | https://github.com/austinlasseter/datasets-shipping-logistics | extraction | Dataset list; no US invoice data |

---

## 12. Could not access, or not found

**Blocked or unusable:**
- **DoD transportation regulation PDFs** (ustranscom.mil DTR Part II ch. 212; Part IV App. A on the Third Party Payment System): certificate verification failed in the fetch tool; the command-line download returned nothing. Snippet only.
- **GSA U.S. Government Freight Transportation Handbook** (May 2021): the download returned an HTML page instead of the PDF.
- **USAID data portal** (data.usaid.gov, dataset a3rc-nmf6) and the data.gov catalogue query: no response or 404. A GitHub mirror of the CSV was used.
- **Kaggle dataset pages:** rendered empty in the fetch tool.
- **Empower Data Logistics 210 guide** and **FCA freight payment 210 guide:** downloads failed; snippets only.
- **Saia "freight bill review" page:** the fetch returned no content.
- **Estes fuel-surcharge history tab:** the history did not load in the extract.
- **Scanned exhibits without a text layer** (UPS Freight complaint, Circuit City claim): OCR is not available in this environment (no language data for tesseract), so selected pages were read as images; the rest were not read.
- **Exist v. SEFL court order of 2026-02-12** on the motion to dismiss: not in the free RECAP archive. PACER was not used (rule).
- **Central Freight v. Amazon demand-letter exhibit** and the sealed exhibits: not read.

**Searched, not found (web searches unless noted):**
- **Carrier "how to read your invoice" pages or sample invoices:** "how to read" LTL freight bill invoice sample PRO; Old Dominion "sample invoice" OR "understanding your invoice" OR "freight bill explained"; Estes invoice explained guide PDF; "sample freight bill" OR "sample freight invoice" LTL PDF; FedEx Freight invoice sample explanation; ABF OR ArcBest "understanding your invoice"; Saia OR R+L OR Averitt OR TForce OR AAA Cooper OR Central Transport "sample invoice" OR "invoice explanation"; Schneider OR J.B. Hunt OR Werner OR Knight-Swift customer invoice guide.
- **Real TL carrier or broker invoices to shippers** (CourtListener): Werner, Schneider National Carriers, Landstar, J.B. Hunt Transport, Knight or Swift with "invoice" and "fuel surcharge"; Echo Global Logistics, Total Quality Logistics, Arrive or Coyote invoices; "truckload" invoice "line haul" "stop off"; "freight invoice" "detention" "hours" (web): "truckload" carrier invoice sample PDF with detention and stop-off.
- **Weight and inspection certificates** (web): "weight and inspection certificate" OR "W&I certificate" sample image; (CourtListener): "weight and research" certificate; "inspection certificate" reweigh; "weight certificate" "freight bill"; "weight verification" "freight bill" PRO.
- **Detention time records** (CourtListener): "detention" "in time" "out time" invoice carrier exhibit.
- **Annotated error examples with images** (web): freight invoice error example screenshot annotated fuel surcharge duplicate reweigh; Freightview OR MyCarrier OR FreightPOP help centre audit discrepancy screenshot.
- **State or university LTL contracts with published discounts** (web): state contract LTL "CzarLite" discount "absolute minimum charge" pricing agreement.
- **Public-agency meeting packets with freight bills** (web): city council agenda packet "freight bill" invoice "fuel surcharge" carrier names.
- **University course samples of freight bills** (web): university logistics course "freight bill" exercise; only a 2010 training manual on a course page was found (N-AC33).
- **FAP providers' EDI 210 specifications** (web): U.S. Bank Freight Payment OR Syncada carrier EDI 210 guide; Cass carrier 210 EDI specifications. Check Z's carrier documents cover their non-EDI terms.
- **FedEx Freight (LTL) EDI 210 guide:** not found; the FedEx guide found covers Express and Ground.
- **Other LTL carrier proofs of claim with invoices** (CourtListener): ODFL "proof of claim" invoices; Saia Motor Freight invoice; Estes "proof of claim" invoices (service lists only); R+L "proof of claim" (service lists only); TForce Freight invoice.
- **SEC shipper-carrier agreements with rates:** four EDGAR full-text queries (§3.7) found none.
- **Kaggle or academic freight-invoice datasets:** Kaggle freight invoice dataset LTL audit; USAID supply chain shipment pricing licence.
- **Vendor payment files with invoice numbers:** open data vendor payments "invoice number" carrier names (only aggregated or voucher-level files found).
