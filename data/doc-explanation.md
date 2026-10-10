# The documents behind a freight price dispute, form by form

Written 2026-10-10 for the founders, from check AT (`research/s5_check_AT_c09_document_dataset.md`) and its verification (`research/s5_check_AT_adversarial.md`). It explains each document in the chain, whether its format is shared across firms or belongs to one firm, what it decides in the worked SEFL mismatch (AT §7), what `data/` holds, and what is missing with its cost. Nothing here is decided; the open points stay in AT §8.

Freight terms used: **LTL** (less-than-truckload: pallets sharing a trailer, priced by weight and class); **TL** (truckload: one shipper's load, priced flat); **PRO number** (the carrier's bill number); **cwt** (hundredweight, 100 lb); **NMFC** (the National Motor Freight Classification, which assigns every commodity a class from 50 to 500); **FAK** ("freight all kinds", an agreement rule that rates several classes as one); **accessorial** (an extra service charge: liftgate, residential delivery, redelivery, detention); **EDI** (electronic data interchange, machine-readable business documents in the X12 standard); **BOL** (bill of lading); **W&I** (weight and inspection).

## 1. The chain, in the order the paperwork is created

### 1.1 Before the shipment: the price is set

**Pricing agreement (rate agreement).**
- *Purpose:* the contract between one shipper and one carrier. It names the base tariff the discount applies to, the discount by lane and direction, the FAK, the per-shipment minimum after discount, and exceptions to the accessorial prices.
- *Format:* per firm, with no common layout. SEFL uses one-page "rating item" tables; YRC a 33-article contract; Home Depot and Walmart lane-pricing exhibits; GM a terms-and-conditions document.
- *In the dispute:* the source of truth for the price. In the worked example it says 88.15% off, class 70 under the FAK, liftgate $55, absolute minimum $152 on the Oregon lane.
- *Held:* SEFL's in three dated versions (set 02); YRC-First Brands, GM, Schneider, Kroger, CJ Logistics (set 11); Home Depot and Walmart contracts with lane pricing (set 23).

**Rules tariff.**
- *Purpose:* the carrier's public rulebook, which fills every gap the agreement leaves: accessorial prices, reweigh and reclass fees, cubic-capacity minimums, the 180-day window, late-payment penalties, discount forfeiture on unpaid bills.
- *Format:* per firm in wording, item numbers and prices, but every carrier's covers the same family of items.
- *In the dispute:* SEFL 1090 Item 753 sets residential delivery at $7.60/cwt with a $94 minimum, and puts the duty to mark a residence on the shipper's BOL. The $94 line on bill 807148067 is priced exactly by this item.
- *Held:* 28 tariffs from 16 carriers and GSA, several in dated versions (set 13).

**Base rate tariff.**
- *Purpose:* the table of undiscounted class rates per cwt, by origin, destination and class, that the agreement's discount is taken from.
- *Format:* proprietary. SEFL-0550 is SEFL's own; CzarLite is SMC3's neutral table that many agreements reference.
- *In the dispute:* without it the software can check that the printed gross equals weight × the printed rate ($600.80/cwt × 509 lb = $3,058.07), but not that $600.80 was the right rate for Miami to Sisters, class 70.
- *Held:* none.

**Fuel surcharge table.**
- *Purpose:* the carrier's weekly percentage, keyed to the EIA/DOE diesel index with that carrier's own bands and effective weekday.
- *Format:* per firm.
- *In the dispute:* 22.00% × net $362.38 = $79.72 is correct arithmetic, but whether 22.00% was SEFL's figure for the week of 2023-05-15 cannot be checked, because no 2023 copy of SEFL's table exists anywhere public.
- *Held:* current tables (DOE, GSA, FedEx Freight LTL and TL), one Estes capture from 2023-03-27, the EIA weekly diesel series (set 14). No 2023-24 captures for ABF, SEFL, ODFL, XPO or Saia.

**Rate quote.**
- *Purpose:* a carrier's priced quote for one shipment. Its number is printed on the bill (CWEN3E465 on the primary example).
- *Format:* per firm.
- *In the dispute:* quote-to-bill matching (check B5) would show whether the residential charge was in the quoted price. The quote is not in the Exist exhibit.
- *Held:* quotes only in other sets (6 files evidence B5).

**Rate confirmation (TL only).**
- *Purpose:* the broker's or carrier's one-page agreement for one load: flat linehaul, fuel, and the detention, layover, truck-ordered-not-used and lumper terms.
- *Format:* one layout per broker, each with its own free hours and hourly prices (TQL 2025: $25-30 an hour after 3-4 hours, layover $250-300, TONU $150 after 2 hours; Coyote: $25 an hour after 2 free hours only if in/out times are on the BOL; U.S. Xpress: $50 an hour after 2 hours).
- *In the dispute:* for TL it plays the role the pricing agreement plays for LTL. The TL invoice is checked line by line against it.
- *Held:* 12 rate confirmations and load tenders (set 10); packets of rate con + invoice + BOL (set 22).

### 1.2 At pickup and delivery: the facts are recorded

**Bill of lading (BOL).**
- *Purpose:* the shipper's own description of the shipment at pickup: pieces, weight, class, NMFC item, delivery instructions, prepaid or collect, who pays.
- *Format:* the VICS/GS1 form is a shared standard, followed loosely, with carrier variants and handwriting.
- *In the dispute:* this is the document that decides the $94. Item 753 says the shipper must mark residential delivery on the BOL and that omission does not relieve it of the charge. If "residential" was on the BOL the charge stands; if not, and the address is a shop, the shipper has a case. For the second example it holds the declared weight (2,430 lb implied) against the 2,720 lb billed. It is absent from the Exist exhibit.
- *Held:* the blank VICS form and uniform BOL terms (set 15); filled BOLs for XPO (set 03), UPS Freight (sets 04, 06), the TL packets (set 22), Winn-Dixie's wrong-payer BOL (set 21).

**Delivery receipt (proof of delivery).**
- *Purpose:* the carrier's copy signed at delivery, with date, time, and sometimes in/out times for detention.
- *Format:* per carrier.
- *In the dispute:* it would show whether the Oregon address was a business and when the driver arrived. For the redelivery example (bill 807307041) it would show the first attempt on 05/25/2023.
- *Held:* XPO (set 03), Yellow (set 05), ODFL and others (set 21), Delphi's UPS Freight receipts (set 04).

**Weight and inspection certificate.**
- *Purpose:* the carrier's record of a reweigh or re-class: scale or dimensioner reading, dimensions, the inspector's note.
- *Format:* per carrier or per W&I vendor.
- *In the dispute:* in the second example the weight rose from 2,430 to 2,720 lb on a balance-due bill with no inspection note on either print, so the first ask in a claim is this certificate. Where SEFL did inspect, the bill says so ("** CLASS INSPECTION PER W&I **", p. 35).
- *Held:* one shipper-side weight certificate attached to a GlobalTranz reweigh dispute against Yellow (set 23); a W&I vendor's invoice to NEMF (set 24); NTEP dimensioner certificates (set 15). No carrier-issued certificate image.

### 1.3 After delivery: the money is asked for

**Freight bill (the invoice).**
- *Purpose:* the carrier's demand for payment: the shipment facts, each charge line, discount, fuel, total, due date.
- *Format:* per firm in layout, charge codes and which dates are printed. No two carriers' bills look alike and none publishes an annotated sample. SEFL writes "DISCOUNT PERCENTAGE 9100" for 91.00% and "60080" for $600.80/cwt; ABF prints the tariff code and deficit weight; XPO prints one discount line and "M" for a minimum; ODFL stamps its own audit notes; UPS Freight bills of 2008-10 are faxed scans; Werner's TL invoice is one flat line plus fuel; Wintzer bills per ton.
- *In the dispute:* this is what the software reads. On the primary example every line reconciles to the agreement except the one the carrier added.
- *Held:* 101 ABF bills with a text layer (set 01); 59 distinct SEFL bills as scans (set 02); 6 XPO invoices (set 03); about 850 pages of UPS Freight bills (set 04); ODFL, XPO and TForce bills (set 21); TL invoices from Werner, USA Truck, Wintzer, Taylor and broker invoices from TQL and RXO (set 22).

**EDI 210 (and 214 status, 204 tender).**
- *Purpose:* the same invoice as a machine file, sent carrier to shipper.
- *Format:* the X12 segment skeleton (ISA/GS/ST, B3, N1-N4, LX, L5, L0, L1, L7, L3) is shared, so one parser reads every carrier's envelope. The charge mapping is per firm: Estes writes the discount as text with a negative line, ODFL rates in cents per cwt with fuel on code 405, AAA Cooper names the base tariff in L7, TL carriers bill a flat linehaul (code 400) plus fuel and TONU. Versions run 4010 to 4060, and shippers publish their own inbound maps (3M rejects negative amounts; Insight requires a proof-of-delivery segment).
- *In the dispute:* the fields are the same as the PDF bill, already structured. A shipper on EDI gets the balance-due bill as a second 210 with the same PRO.
- *Held:* 36 real interchanges from ODFL, AAA Cooper, Estes, SEFL, Holland and three TL carriers (set 19); 14 implementation guides (set 12).

**Balance-due or corrected bill.**
- *Purpose:* a second bill under the same PRO number for the difference, issued when the carrier re-rates after delivery.
- *Format:* per firm. SEFL prints "BALANCE DUE INVOICE" and "PAY THIS AMOUNT" with only the difference due; XPO prints "RE-WEIGHED PER WEIGHT CERTIFICATE"; ODFL stamps "REWEIGH CORRECTED WEIGHT 1070 LBS" or "CORRECT AS BILLED".
- *In the dispute:* this is where both worked disputes are born. The $94 residential line appeared on the balance-due print dated 06/19/2023, 35 days after shipment, with the carrier's reason printed ("** PER GOOGLE EARTH THIS IS A PRIVATE DLVY"). The weight change appeared on the balance-due print of 05/05/2023, 16 days after shipment. Each restarts the shipper's 180-day clock from its own date, so the windows ran to 2023-12-16 and 2023-11-01. The lesson from the verification: match every balance-due bill to its original and to every later reprint before any date arithmetic; the 2025 "PAST DUE INVOICE" prints of the same bills are reprints, not new bills.
- *Held:* 48 SEFL corrected and balance-due prints, 13 of them paired with their 2025 reprints (set 02); XPO's reweigh correction (set 03); ODFL's wrong-payer refund and re-bill, end to end (set 21).

**Statement of account.**
- *Purpose:* the carrier's list of open bills, used to chase payment; the place short-pays and disputed balances show up.
- *Format:* per carrier, from a one-page list to Kuehne+Nagel's 285-page pro ledger.
- *In the dispute:* the unpaid $94 and $110.23 would sit on SEFL's statement until paid or credited; the 2025 reprints are the collection step.
- *Held:* sets 21 and 24.

### 1.4 The dispute itself

**The shipper's audit worksheet or dispute log.**
- *Purpose:* whatever the shipper's staff keep to compare bills with the agreement and track claims.
- *Format:* bespoke to each shipper. Exist's is a 3,645-row spreadsheet with columns for invoice, date, pallets, liftgate, surcharge, freight charge, "NEED TO BE CHG" and "OVER CHG".
- *In the dispute:* it is the document our software replaces, and the example of what it must not do. Exist's "NEED TO BE CHG" is pallets × the per-shipment absolute minimum, a misreading of Item 610, so its $271,829 claim is overstated and it never flagged the $94 that was actually added without an order.
- *Held:* the three yearly worksheets (set 02, pp. 99-224).

**Overcharge claim.**
- *Purpose:* the shipper's formal dispute to the carrier, filed inside 180 days of the bill.
- *Format:* content standardised by 49 CFR Part 378 (identify the bill, state the amount and reason, attach proof); ABF, R+L, Averitt, YRC and South Bay accept the "Standard Form for Presentation of Overcharge Claims" with a bond of indemnity; XPO and Central Transport use their own web forms; brokers give 5-30 days under their own terms.
- *In the dispute:* for the $94 a claim would carry the balance-due bill, the BOL showing the delivery instructions, the agreement's exceptions page, Item 753, and a statement that the consignee is a business. For the weight it would carry the original and the balance-due bill side by side, the BOL weight, and a request for the certificate.
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
- 49 U.S.C. 13710(a)(3): the carrier has 180 days from receipt of the bill to bill additional charges (A); the shipper has 180 days to contest (B).
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
| Standard overcharge claim form (5 carriers) | Fuel table bands and effective weekday |
| 49 U.S.C. 13710's two 180-day windows | Rate quote, rate confirmation, statement, claim channel, carrier response |
| Government billing (GBL, SF 1113, 41 CFR 102-118), for one shipper only | Base rate tariff (proprietary or licensed) |

Design reading (AT §6): one standard data path, many per-firm readers.

## 3. What we do not have, and what it would cost

| Missing | Why it matters | Where it comes from | Cost |
|---|---|---|---|
| Base rate tariff (CzarLite, or a carrier's own such as SEFL-0550) | Verifies the gross rate itself, not just the arithmetic (checks B1, B6) | An SMC3 licence; carrier base tariffs are sold only as SMC3 data modules | CzarLite data module listed at $800 (2022 price list), carrier tariff modules $300, each on top of RateWare access. FEMA paid $8,764 a year for one organisation's CzarLite and RateWare web access (2019-21). The price for software serving many customers is not published (AR §AR3). *verified* prices; the multi-customer unit *not answerable from the web* |
| 2023-24 fuel tables in force | Check B8 on every real bill in sets 01 and 02 | The carrier on request, or a retry of the Wayback CDX index | $0 in cash. No archived 2023-24 copies exist for ABF, SEFL, ODFL, XPO or Saia (Wayback availability API, 2026-10-09) |
| BOLs and delivery receipts for the SEFL bills | They decide the $94 and the weight dispute | Only Exist or SEFL | Not obtainable; not in the court file |
| Carrier-issued W&I certificate, stand-alone credit memo or denial letter, a shipper's Part 378 packet, an AP export, a dispute log | The second half of the dispute and the payment checks (A2, A3, C1, F1) | Interviewees' own files, under NDA, kept outside the project in `~/Documents/personal/bio/freight_private/` and deleted after the assessment (D-18) | $0 in cash beyond any interview incentive the founders set; the cost is the NDA and the founders' hours |
| PACER-only exhibits: Estes v. Coverlex Doc 19-1 (a pricing agreement, a 2,498-bill list, discount-forfeiture exemplars); Estes v. Whatman Docs 1-1, 9-5, 19-5 (sample BOL, invoice, past-due warning); Central Freight v. Amazon Doc 1-1 (Amazon's audit demand letter); Transport Systems v. Amazon Doc 1; Exist v. SEFL filings after Doc 1 including the 2026-02-12 order; Hannum Doc 72-3; Surge v. Mondelez; Coyote v. Jusda and Landstar v. Urban Roads (broker-to-shipper invoices) | Would close the pricing-agreement, demand-letter and broker-invoice gaps | A PACER account (a login, which the project's rules have so far excluded) | PACER charges $0.10 a page, capped at $3.00 a document, and waives the quarter's fees entirely if usage is $30 or less. About 12 documents, so roughly $30-40 at most, and possibly $0 if spread over two quarters. Buying them with the RECAP browser extension installed also puts free copies into the public archive. *assumed* on the PACER fee schedule as known; re-check at pacer.uscourts.gov before buying |
| Lewis v. YRC Doc 63-1 (165 pages) | More Yellow bills | RECAP, free | $0; skipped only for the 25 MB per-file cap |
| R+L v. Qualcomm joint appendix (450 pages) | Surfaced on the W&I query, unread | RECAP, free | $0; not fetched for size |
| A public LTL pricing agreement with prices on a .gov or .edu site | A second agreement layout from a neutral source | Not found anywhere | Not purchasable |
| Carrier-published 210 guides for SEFL, ODFL, Saia, Averitt, Dayton, AAA Cooper, Pitt Ohio, Central Transport | Per-carrier charge maps | The carrier's EDI team, on onboarding | $0; given to trading partners |
| NMFC class data in machine form | Class lookups for check C1 | NMFTA licence (ClassIT) | Price not published (AL); DoD paid $5,500-5,803 for an "NMFC data license renewal" in 2008 (AR) |

Two points for the founders, not decided here:
- The PACER list is cheap. The only reason to hold off is the rule against logins and accounts in research sessions, which buying would waive for one purpose.
- The base tariff is the one real expense. It matters only if the prototype is to check gross rates. Discounts, classes, minimums, accessorials, fuel arithmetic and corrected-bill reconciliation, which together cover every discrepancy found in the public sets so far, need no base tariff.
