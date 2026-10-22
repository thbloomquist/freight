# Check AZ · Adversarial review of the price-terms validation

Written 2026-10-18. Adversarial reviewer of validator AZ (`research/s5_check_AZ_c09_fact_map_price_terms.md`, 416 lines), which tested the phase-1 price terms P01-P21 of `data/doc-exploration.md` on the files in `data/`. Method: offline, read-only on `data/` and `research/` except this file, no sub-agents; every citation behind a KEEP-verified, NARROW, DISCARD or ADD verdict was re-opened (`grep -n` / `sed -n` on `data/derived/text/`, EDI parsed on the ISA separators, scans rendered with `pdftoppm` and read as images, arithmetic in `python3 -I`). Verdicts on the validator: **CONFIRM** (the evidence says what the validator says), **OVERTURN** (it does not; counter-evidence given), **NARROW** (in part; corrected wording given), **could not test** (nothing in `data/` decides it). Companies only; no individual's name or phone number is transcribed. Written section by section; sections marked *(pending)* were not yet reached when this file was last saved.

## 0. Summary

**Counts (this reviewer's verdicts on the validator's rows).**

| Validator section | Rows | CONFIRM | NARROW | OVERTURN | Could not test |
|---|---|---|---|---|---|
| §2 cells of §2.1 (P01-P21) | 68 | 57 | 9 | 2 | 0 |
| §3 §1.1 columns (Checks, Role, Need) | 63 | 63 | 0 | 0 | 0 |
| §4.1 rows of doc §3 | 12 | 12 | 0 | 0 | 0 |
| §4.2 citations in doc §4 | 69 | 61 | 6 | 0 | 2 (Part 378) |
| §4.3 P rows of doc §5 | 41 | 39 | 1 | 1 | 0 |
| §4.4 ledger rows (incl. 35a-r) | 42 | 37 | 4 | 1 | 0 |
| §5 additions A1-A11 | 11 | 7 | 4 | 0 | 0 |
| **Total** | **306** | **276** | **24** | **4** | **2** |

Also overturned: the validator's §6 item 6 and §8 item 4 (the two ODFL captures "are not two revisions"); narrowed: its §6 item 3 and the NMFC caveat on ledger 7. One §5 P row the validator did not test (chain D P01) was re-opened and confirmed. The validator's report passes the privacy check.

**The five findings that matter most.**
1. **The ODFL Item 365 dates are on the files; the validator's NARROW is wrong** (ledger 18, §5.4 P11, its §6 item 6). The Item 365 page prints "Revised 11/03/2025" in 13-052 (l. 1020; fee $40.00) and "Revised 10/05/2026" in 13-053 (l. 1029; fee $45.00), whose cover reads "Updated: October 5, 2026" (l. 38); the catalogue calls 13-053 a "Distinct version" and walk B recorded both stamps. "Effective: April 14, 2025" is the issue date. Keep the doc's wording, retag ledger 18 *verified*.
2. **Two document types the validator called absent are held.** (a) 19-027, a real shipper-to-carrier truckload tender (bill-to a food producer, mode TL) carrying its price `L3*42186*G*2377.08*FR*237708`: P14 Primary is testable for the 204 L3 form, so the KEEP-assumed is overturned. (b) 23-005 holds a second LTL pricing agreement (Home Depot–Yellow, Schedule A: named base tariff "customized Czarlite International Tariff, effective 8/29/05", tiered FAK, a rate-precedence rule; Schedule A-1: 2,177 lane rows with minimum and discount), so "the only LTL pricing agreement in `data/` is 02-002" is wrong; the catalogue tags four `pricing_agreement` files. 23-005 §8 ¶I also sets an 18-month overcharge window the validator's P16 evidence missed.
3. **TForce's 120×96×96 default and its post-tender refusal are not general rules.** Both sit in Item 645-A, which applies only where "density based rates" are set "upon a written agreement executed by each of customer and Carrier" (13-060 l. 2416-2418). The validator's retags to *verified* (§4.2, §4.4, ledger 31) need that scope; the exploration agent had already dropped it.
4. **P01's "FedEx Freight and TForce: the BOL's terms" is not a contrast with "the payor's".** FedEx 765 ¶1D and TForce 765 ¶1c give the third-party payor's program precedence, and ¶1A-B/¶1a-b put the shipper first on prepaid and the consignee first on collect; TForce overrides the BOL by bill-to affiliation. Saia 105 excepts volume shipments; ABF's item is 765, not 760. And §5.1's P01 row cites SEFL 753 §5 (who pays the residential fee) where SEFL 201 is the pricing rule; the validator kept both.
5. **Edition and scope slips the validator made or kept.** XPO 205's proof wording is in AK.2 (May 2026) as well as AK.3; XPO 239 is $47.85 in AK.1 and AK.2, so the validator "verified" the doc's $50.70 against the AK.1 text. NMFC 300320/300330/300340 apply only to household-goods, noncontiguous and forwarder carriers (300300-A, 15-081 l. 1077-1084), so for SEFL-type carriers only 300520 can apply, which also raises an unproven concern that Part 378 itself (whose 378.1 no file quotes) binds ordinary LTL carriers only where a tariff or contract incorporates it (ODFL 396, Saia 1030(7), Walmart §7e) (§7 item 1).

Also worth the founders' eye: the doc's ABF "DISC 89.5%" is right (code column "DISC", rate column "89.5%" on every bill; the validator's NARROW is overturned); SEFL's fuel rules sit in a separate SEFL 195 Fuel Master Tariff named in Item 100, not held; First Brands' fuel schedule spans pp. 25-27; R+L 364 also demands "conclusive documentary proof"; TForce's reweigh fee is Item 990 ¶2, not 365; the walk agents' found-or-n/a P facts were often swept into §5's NOT REPORTED lines (§4.1 rows 3, 7, 8, 10, 12, 16, 17).

## 1. Method

This section replaces the previous reviewer's reading list. Every entry below was opened by this reviewer on 2026-10-19.

- **Read in full:** the common adversary brief; the validator's report (416 lines); `data/doc-exploration.md` as it stood when the validator read it (`git show HEAD:data/doc-exploration.md`, 727 lines; the working copy edited by the coordinator was not used); `SCRATCH/coordinator_recheck.md`; `SCRATCH/id_to_path.tsv`. **Raw traces:** `walk_A_sets02_03.md` (P rows of chains A and B), `walk_B_sets19_21.md` and `walk_C_sets23_22.md` (the JSON-escaped report after "FINAL REPORT" decoded into the scratchpad), `explore_rules_2.md` l. 1-242 (the source of the doc's "exploration read" claims), `explore_rules_1.md` and `_3.md` searched. **Research files:** AK §3.2 (l. 128-177); AX §6-§7 (l. 177-221, the Part 378 quotations); AX review l. 17, 25, 108, 169; AM l. 113, 155, 191.
- **Text layers re-opened (`sed -n` / `grep -n` on `data/derived/text/`):** set 13: 13-046, 13-047, 13-048 (ABF 161, 362, 427, 428, 615, 751, 765, 992 in all three issues), 13-049 (Estes 360-03, 530, 615, 720, 751, 751-10, 760, 992, 993, 825), 13-050 and 13-051 (FedEx 360 ¶6 in both; 404, 438, 570, 613, 765, 980, 981, 990), 13-052 and 13-053 (ODFL 162, 180, 365, 367, 396, 434, 564, 565, 610-1, 764, with every "Revised" stamp), 13-056 (Saia 105, 650, 850, 1030), 13-058 (R+L 364, 992, l. 325-342), 13-060 (TForce 361-A, 365, 575-A, 610-A, 645-A, 721, 753, 765, 813, 990), 13-061, 13-062, 13-063, 13-064 (XPO 4, 7 ¶7-9, 23, 26.3, 200, 205, 207, 224, 233, 239 in each issue held), 13-065 (SEFL 100, 110, 170, 201, 360-5, 435-10, 610-100, 752, 753, 754, 817, 890-100, 992, 996), 13-066 (AAA Cooper 660, 760, 970), 13-067 (Landstar 765), 13-068 (Werner 310 ×2, 320, 570, 585), 13-071 (USA Truck 14, 17, 41), 13-072 (Dayton 407, 1015), 13-073 (Central 400, 460); a set-13 census for precedence items, cubic items, "walk-in", "overcharge", "undercharge", "disallowance" and "378". Set 15: 15-077, 15-078, 15-079, 15-081 (300300-A to 300530-A and 401400-A, with PDF pages counted on form feeds). Sets 16, 08, 20: 16-082, 16-083, 16-092, 16-093, 16-095; 08-024, 08-030; 20-003, 20-005. Contracts: 11-037 (with a page count of the fuel table), 11-039, 23-005 (§8 ¶A-J, l. 85362-85369, Schedule A l. 85575-85640, Schedule A-1 l. 87850-87872, a "Point to" row count), 10-037, 10-038, 10-043, 22-013. Bills: 01-001 (string census per unique bill number, Python), 02-002 split into 225 form-feed pages (pp. 12-22, 33, 41, 46, 94 and a "6009" / account-number search over all pages), 21-005, 21-015, 22-012 split into pages (pp. 4-9, 20). Catalogue: `doc_types` census, rows 09-031, 09-032, 13-046 to 13-073, 23-005, sets 10 and 22; `data/leads_tried.csv` lines 354-364; `data/sources/14_fuel_tables_and_index/source.md` rows 14-073 to 14-076.
- **EDI parsed with each file's ISA separators** (Python, `SCRATCH/azadv_scripts/edi.py`): all 36 files of set 19 for L7, L5, L3, B2, N1; full dumps of 19-001 ST 0001, 19-009 ST 0014, 19-015 ST 60001-60004, 19-031 (both STs), 19-027 and 19-028.
- **Pages read as images:** existing renders 02-002 pp. 22, 33; 03-003 pp. 11, 14; 05-015 p. 1; 21-002 pp. 6, 13, 15, 16, 17; 22-008 pp. 4, 7; 22-012 p. 4; 23-012 pp. 77, 78, 86. New renders (scratchpad only, prefix `azadv_`): 01-001 p. 17; 02-002 p. 19; 22-012 p. 20 (two crops of the detention block); 23-012 pp. 79-96 as one contact sheet.
- **Other:** `pdfinfo` on 13-052 and 13-053; 14-074 (EIA .xls) converted to CSV from a scratchpad copy with LibreOffice to read the 2024 weekly prices; arithmetic in `python3 -I` (every date and money figure in the validator's §2 and §4, plus the Roadway and Estes 210 lines).
- **Not done:** the web (offline); 49 CFR Part 378 (no copy in `data/`); a full reading of the Central v. Amazon depositions (09-046 to 09-049, searched for quote documents only).
- **Integrity:** nothing under `data/` or `research/` was written except this file; `sha256sum -c SHA256SUMS` run from `data/`: 271 OK, 0 failed (2026-10-19).

## 2. Per-claim table

Verdicts: **C** = CONFIRM, **O** = OVERTURN, **N** = NARROW, **CNT** = could not test. Validator verdicts: KV = KEEP-verified, KA = KEEP-assumed, N = NARROW, A = ADD. "l." is the line in `data/derived/text/<set>/<file>.txt`; "p." the PDF page. Quotations are the file's words.

### 2.1 The §2.1 cells (68 tested by the validator)

| Validator row | Val. | Mine | Evidence (re-opened) | Corrected wording |
|---|---|---|---|---|
| P01 Primary | KV | **N** | Every item quoted exists with the quoted words: SEFL 201 ¶1 (13-065 l. 372-374), ODFL 764 ¶1 (13-053 l. 8187-8190), XPO 4 (13-061 l. 234-236), Estes 760 Part I ¶3 (13-049 l. 3610-3611), Saia 105 ¶1 (13-056 l. 307-310). But the contrast "FedEx Freight and TForce: the BOL's terms" does not hold as a contrast. FedEx 765 ranks, within each set of terms, the paying party's program first: A outbound prepaid → Shipper; B outbound collect → Consignee's inbound program; C inbound collect → Consignee; **D third party → "A pricing program published for the account of Third-Party Payor will take precedence"**; E services requested off the BOL → "the requestor's pricing program" (13-051 l. 2664-2697; the validator cited only A/B/C). TForce 765 1.a-c is the same, and ¶1.a.2 overrides the BOL by affiliation: "If the consignee and the bill-to party are affiliated, the shipment will be considered collect regardless of how the shipment is identified on the bill of lading" (13-060 l. 3112-3116). ODFL 764 ¶3 and SEFL 201 ¶2-3 have the same terms-based fallback. Saia 105 ¶1 excepts "volume rated shipments. On volume shipments the lowest published rate will be applicable" (13-056 l. 308-310). | "The carrier's rules tariff item. All seven name the payor's program first: SEFL 201, ODFL 764, XPO 4, Estes 760, Saia 105 (except volume shipments: lowest rate), ABF 765 ¶3, AAA Cooper 760. FedEx 765 and TForce 765 rank by the BOL's terms (prepaid → shipper, collect → consignee, third party → third-party payor); a freight-payment processor is not a third party, and TForce re-classifies by bill-to affiliation 'regardless of how the shipment is identified on the bill of lading'." |
| P01 Fallback | KV | C | 02-002 p. 18 l. 10 "071-003454 EXIST INC, MIAMI GARDENS, FL" with ROUTE/APPLICATION rows "SEFL OUTBOUND PPD/COL", "SEFL INBOUND COL"; p. 19 "MWPC INBOUND COL". A second agreement carries a debtor clause: 23-005 Schedule A "Actual class will apply on outbound shipments when Home Depot is not the debtor" (l. 85600). | — |
| P01 Never | KV | **N** (citation) | The substance holds: 21-002 p. 17 (render) bill-to "CLAMP-SWING PRICING" after "CBL DGB 2/18/05 CORRECTED BILL OF LADING CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER FROM THE 3RD PARTY". But **"Col/Ppd P" is not on the bill**: the bill's column header reads "PREPAID"; "Col/Ppd: P" is printed on ODFL's A/R screens, 21-002 pp. 13, 15, 16 (renders). | Evidence: "21-002 p. 17 bill-to after the 2/18/05 payor correction; 'Col/Ppd: P' is on the A/R screens pp. 13, 15, 16." |
| P01 If none | KV | C | Payor rules in 13-065, 13-053, 13-061, 13-049, 13-056, 13-047 (Item **765** ¶3 "Paying party", l. 3897), 13-066 (760, l. 3168-3173), 13-051, 13-060, and two TL tariffs the validator did not cite: USA Truck 14 (13-071 l. 350-366) and Werner 570 (13-068 l. 1204-1212). Landstar Rule 765 is a specificity rule, not a payor rule (13-067 l. 1735-1747). | — |
| P02 Primary | KV | C | 02-002 p. 12 l. 6-8 "TARIFF SEFL 6009 / RATING ITEM 000-068386 / EFFECTIVE DATE: 01/15/2021 / 071-000559 EXIST INC, FT LAUDERDALE, FL"; p. 15 l. 7-8 "06/08/2022", "071-000S59"; p. 18 l. 8-10 "04/12/2023", "071-003454 … MIAMI GARDENS". Note the account number changes between versions (071-000559 on the 2021 and 2022 versions; 071-003454 on 2023): the version is picked by rating item + account + date. walk A recorded both accounts; the doc kept one. | — |
| P02 Fallback | N | C | ABF "AU=ABF646-468646" on 205 lines of 01-001. "6009" occurs only on 02-002 pp. 12-16, 18-20, 144 (form-feed split, all 225 pages); the bill p. 46 footer l. 52 prints "071-003454". The validator's wording is right. | (validator's) |
| P02 Never | KV | C | 02-002 p. 33 (render): "PAST DUE INVOICE", footer 08/26/2025 and 09/10/2025, "PREPAID 591.10", "INVOICE PENDING", shipment date 05/15/2023. | — |
| P02 If none | KV | **N** (evidence) | The cell ("Customer") stands, but the validator's evidence "The only LTL pricing agreement in `data/` is the court exhibit 02-002" is wrong. The catalogue tags four files `pricing_agreement` (02-002, 09-031, 09-032, 23-005). 23-005 holds Home Depot's LTL pricing with Yellow: Schedule A "PRICING TERMS" names the base tariff ("The Home Depot customized Czarlite International Tariff, effective 8/29/05"), tiered FAK, a rate-precedence rule (l. 85575-85636), and Schedule A-1 "Effective October 27th, 2022" lane rows with "Primary Minimum" and "Primary Discount" (l. 87850-87870; 2,177 "Point to" lines). | Evidence: "The only *walked* agreement is 02-002; 23-005 (Home Depot–Yellow Schedules A/A-1) is a second LTL pricing agreement held, not walked." |
| P03 Primary | KV | C | 02-002 p. 18 l. 15 "SEFL-0550 01/.10/22"; p. 12 l. 11 "SEFL-0550 CURRENT". Second example: 23-005 Schedule A names its base tariff and edition (above). | — |
| P03 Fallback | KV | **N** (generalisation) | 19-009 ST 0014 `L7*1*CZAR*910****060***20120917*0562` ✓; 01-001 "Tariff: AOD000" on all 101 bills (per unique bill number); 13-065 Item 100 l. 150-166 ✓. The validator's census is incomplete: AAA Cooper also fills L7 with `L7*1*SMC*ZRH****060***20110919*…` in 19-009 ST 0015, 19-011, 19-012 (×3) and 19-014; Roadway fills it in 19-031 (`L7*1*RDWY*4516****50`, `L7*1*RDWY*475****70`; catalogue "partly real"); ODFL's L7 is not "always `L7*******050`": L7-07 carries the rated class: `L7*******077` occurs in seven of the eight ODFL 210s (19-001 to 19-004, 19-006 to 19-008; only 19-005 has 050 alone). ABF bills also print "RATE DETERMINED BY RATEWARE / RATW" (01-001 p. 17, render). | Evidence: "L7-02/-03 filled by AAA Cooper (CZAR 910 or SMC ZRH) and Roadway (RDWY 4516/475, 19-031); blank in every ODFL 210, whose L7-07 is the class (050, 077)." |
| P03 If none | KV | C | No base-rate table anywhere (catalogue `doc_types` census has none). | — |
| P04 Primary | KV | C | 02-002 p. 19 render (new): MWPC 90.30, NEPC 87.45, SWPC 86.35, WCPC 88.15 outbound; 81.10 on every partner inbound-collect row; p. 18 direct 81.00. The text layer's "87.5" and "B8.15" are OCR errors; the image confirms AX review row 2. | — |
| P04 Fallback | N | **O** | The doc's "ABF 'DISC 89.5%'" is a correct reading of the bill's columns. 01-001 p. 17 (render): Description "DISC,89.5%,-CC,-DB,-LC,-DC,-EQ,-TL,-T", **Weight/code column "DISC", Rate column "89.5%"**, Charge "-6,232.60"; the text layer l. 884 shows the same three columns. The code string and the rate column both print the % on all 101 bills. Other quotes re-opened: SEFL p. 46 l. 18 "88.15% DISC 2695.69"; TForce 21-015 l. 826, 957; AAA Cooper 19-009 ST 0014 `L5*2*LESS 78.00 PCT DISCOUNT` (also 19-010 ×2, 19-013; 87.20 in 19-009 ST 0015, 19-011, 19-012, 19-014); Estes 19-015 ST 60001 `L5*1*DISCOUNT 84.0%`; XPO 03-003 p. 11 (render) "($468.96)" on $1,875.85. Add a fourth 210 form: Roadway 19-031 `L5*2*PERCENT DISCOUNT` with `L1*2*76.2*AV*-94884` (the % in L1-02, qualifier AV; 1,245.20 × 0.762 = 948.84). | Keep the doc's "ABF 'DISC 89.5%'" (code and rate columns); optionally add "(also inside the description string 'DISC,89.5%,…')". |
| P04 If none | KV | C | Chains B, C, D carry the % only as billed (03-003 p. 11; 19-001; 21-002 p. 17 render "Discount Allowed: 70.00%"). | — |
| P05 Primary | KV | C | 02-002 p. 19 every partner row "70 / 77.5 THRU 175" (outbound) or "77.5 THRU 125" (inbound) with the note. See A3 for the lane split. | — |
| P05 Fallback | KV | C | 02-002 p. 41 l. 15-18 "CL150 NMFC 49880-", "CL125 NMFC 49880-", "CLASS 70.0". | — |
| P05 If none | KV | C | as P02. | — |
| P06 Primary | KV | C | 02-002 p. 18 "$ 97.00" FMCS (direct); p. 19 "Item 610" on every partner row; p. 20 Item 610: MWPC $127.50, NEPC $130.50, SWPC $122.50, WCPC CO $161.00 and "AZ, CA, ID, MT, NV, OR, UT, WA and WY" $152.00; FMCS defined on p. 20 as "Floor Minimum charge per shipment … after application of discount". | — |
| P06 Fallback | N | C | Saia 650 is a rule (13-056 l. 3510-3514 "the amount referenced will only apply if the total charge after applying the discount … falls below said amount"). ABF 615 $290/$315 (13-047 l. 2894-2895; 13-046 has $245/$275 by weight, $275/$300 Canada). ODFL 180 runs $151 (intrastate) to $270 (interline) in the U.S. and up to $428 on Canada rows, by territory and distance (13-053 l. 822-852). FedEx 404 $254/$243 (13-051 l. 1137-1139). TForce 610-A $186/$195 (13-060 l. 2335-2337). | (validator's) |
| P06 If none | KV | C | ABF 615 ¶3 "Unless otherwise specified by a designated account or lane-specific agreement" (13-047 l. 2888-2889). | — |
| P07 Primary | N | **N** (extend) | FedEx 613 ¶2 "greater than 750 cubic feet and has an average density of less than 4 pounds per cubic foot" (13-051 l. 1917-1918) ✓. The **class** differs too, not only the threshold: XPO 233 rates at "class 125" (13-061 l. 2228-2229); ODFL 610-1 at "Class 125" in both bands (13-053 l. 2710-2719); SEFL 610-100 and TForce 575-A at class 150 with the customer's discount (SEFL: 60% if none, 13-065 l. 1242-1245; TForce 60% only under ¶4b, l. 2200-2206); FedEx 613 at class 150 with "a 50% discount percentage or Customer's otherwise applicable discount percentage, whichever is greater" (l. 1882-1887). Uncited carriers differ again: ABF 611-1 (<4 pcf at 350-750 ft³ → class 77.5; <6 pcf at ≥750 → class 150; 13-047 l. 2827-2845), Estes 615 (>350 ft³ → class 125 or 211% of base, 13-049 l. 2693-2696), Central 611 (51-inch height rule, 13-073 l. 1257-1274). | "Rules tariff item (SEFL 610-100, ODFL 610-1, XPO 233, FedEx 613, TForce 575-A; also ABF 611-1, Estes 615, Central 611): thresholds (3, 4 or 6 pcf; 350 or 750 ft³), the class (77.5, 125 or 150) and the discount applied are per carrier." |
| P07 Fallback | KV | C | 02-002 p. 94 l. 19-21 "T 1090C 610-100 1548.75 CF 5.76 PCF", "AW 8920 CW 9292.5", "MIN FRT CHG 3454.14"; l. 25-26 "SEFL W&I INSPECTED TO A CUBIC CAPACITY MOVE". Note: 27,523.00 × (1 − 0.8745) = 3,454.14, so the "Gross Charge … Discount" lines printed in the description column (l. 33-35) are the arithmetic behind "MIN FRT CHG". | — |
| P07 If none | KV | C | All five items in set 13. | — |
| P08 Primary | KA | C (KA stands) | No quote document in `data/`: catalogue `doc_types` has no quote type; a search of all derived text for "spot quote / quote number / quote #" hits only bills (02-002), tariffs (set 13) and the Central v. Amazon depositions (09-046 to 09-049), which discuss spot quotes but attach none in the lines read. | — |
| P08 Fallback | KV | C | 02-002 p. 21 text "ORDER OF APPLICATION: PALLET RATES TO BE APPLIED BASED ON THE LOWEST TO HIGHEST LANE PRECEDENT" (garbled); 01-001 per unique bill number (Python over the 101 bills): "PQ SCHEDULE" on 82, "quoted amount" note on 27; 02-002 p. 46 l. 28 "QUOTE #CWEN3E465". | — |
| P08 Never | KV | C | logic; ABF notes name the quotation they differ from. | — |
| P08 If none | KV | C | as Primary. | — |
| P09 Primary | KV | C | 02-002 p. 22 (render): every row "4/7/2021"; liftgate DIRECT→PARTNERSHIP and PARTNERSHIP→DIRECT "$55 MIN CHARGE", DIRECT→DIRECT "$30"; limited access $50/$50/$25; inside $25/$25; notification $0.00/$7.5/$7.5; reconsignment $30 (×4); redelivery and dock-pickup redelivery $80 (×4); no residential row; "SUBJECT TO GENERAL RATE INCREASE" NO on every row; handwritten "30" and initials beside the three liftgate rows. 11-037 l. 1058 "Corrected bill of lading $0.00 Waived", l. 1060 "Re-weighing $0.00 Waived". | — |
| P09 Fallback | KV | C | 23-012 p. 89 Sch. I ¶3-¶4 (contact sheet; AZ's render); 23-005 l. 2351 "Add Accessorial Fee from past SOW" is an amendment note, weak but present. | — |
| P09 Never | KV | C | 02-002 p. 22 header "UNLESS OTHERWISE STATED IN CONTRACT OR TARIFF, ACCESSORIAL CHARGES WILL BE ASSESSED ACCORDING TO THE PROVISIONS OF THE SEFL 1090 RULES TARIFFF SUBJECT TO THE EXCEPTIONS BELOW"; p. 46 l. 20 "LIFTGATE SVC 55.00". Caveat on the validator's comparison: SEFL 890-100 ($7.25/cwt, $89 min) is "Effective: January 12th, 2026" (13-065 l. 4570), so it is not the 2023 tariff price. | — |
| P09 If none | KV | C | as P02. | — |
| P10 Primary | KV | C | 13-065 l. 2669 "ITEM 753 Effective: December 16, 2022"; §1 l. 2675-2677; §2 l. 2679-2685 "will not relieve"; §4 l. 2694-2696 "$7.60/CWT … minimum charge of $94.00 and a maximum charge of $575.00". | — |
| P10 Fallback | KV | C | Post-2023 SEFL items: 754 "April 2, 2024" (l. 2708), 170 "Dec 1st, 2025" (l. 313), 996 "Dec 1st, 2025" (l. 4768), 890-100 "January 12th, 2026" (l. 4570). | — |
| P10 Never | KV | C | Residence definitions differ: SEFL 753 §1 "entire premises on which a dwelling for living is located"; ABF 751 "including that portion of the premises where commercial or business activity is conducted" (13-047 l. 3281-3282); Estes 751 §1 ¶2 excludes premises selling "to the walk-in public" (13-049 l. 3376-3378); TForce 753 ¶8 "regardless of a shipper's designation" (13-060 l. 2855-2857). | — |
| P10 If none | N | C | `leads_tried.csv` lines 354, 361, 362 ("blocked", HTTP 429); `14_…/source.md` row 14-075 adds "Wayback captures for the historical LTL tables could not be fetched (archive.org offline/429 all session)". Small correction to the validator's evidence: the catalogue gives `UNRESOLVED` as the URL of both older issues it names (13-054 Saia 2019 and 13-064 XPO 2018), so "came from the carriers' own sites" is the catalogue's `source_kind`, not a resolved URL. | (validator's) |
| P11 Primary | KV | **N** | Every amount quoted re-opened (SEFL 996 $15 l. 4781-4782; SEFL 360-5 NOTE A $35 l. 552; ABF 992 ¶2 $55 at $10 l. 5583-5585; ABF 362 A "$54.00 per change", C "30 days from date of the initial bill of lading" l. 1569-1575; ODFL 367, 365 ✓; Estes 992 ¶2 +100/−500 lb $25, 993 $20, 360-03 $20; FedEx 981 ¶1-2 under 50 lb no fee, $40 at +50 lb; R+L 992 ¶3 $40 at $10, 364 $45.90; Saia 850 $39, no-weight $33). Two corrections. (1) **TForce 365 is "Inspection / Reclassification"** ($40 when inspection raises net charges $15 or more, 13-060 l. 1514-1526); TForce's **reweigh** fee is Item 990 ¶2 ($40 at $15, l. 4281-4283) and its correction fees are 361-A ($50, l. ~1446-1462), both missing from the cell. (2) **XPO 239 is edition-specific**: $47.85 in AK.1 (13-061 l. 2376) and AK.2 (13-062), $50.70 only in AK.3 (13-063 l. 2455-2459), $27.25 in AB-4 (13-064 l. 2180). | "… TForce 365 (reclass), 990 ¶2 (reweigh), 361-A (corrections); … XPO 239 ($27.25 in 2018, $47.85 Feb-May 2026, $50.70 from Aug 2026), 205 …" |
| P11 Fallback | KV | C | 11-037 l. 1058, 1060. | — |
| P11 If none | KV | C | all in set 13. | — |
| P12 Primary | N | **N** | First Brands' fuel schedule is Schedule C §II, heading and week rule on **p. 25** (11-037 l. 1225-1240, "fuel prices announced on Monday … effective Monday through Sunday of the next week"), table rows on pp. 25-27 (11 + 40 + 6 rows, counted on form feeds); l. 1300 is on p. 26 as the validator says, but "p. 26" alone is as partial as the doc's "p. 27". Walmart: confirmed absent. 23-012 p. 77 (render) b(2) "Any fuel surcharge shall be controlled by the schedule attached as Appendix C"; p. 86 lists "APPENDIX C – FUEL SURCHARGE"; the contact sheet of pp. 79-96 shows Appendix A (p. 87, "[Carrier to Provide]"), Appendix B "Lanes and Rates" with no rates (p. 88), Schedule I (pp. 89-91), Appendix D (p. 92), Schedules E and H (pp. 93-94), Attachments 1-2 (pp. 95-96): no Appendix C page. | "First Brands Sch. C §II, pp. 25-27; Walmart names an 'Appendix C' fuel schedule (p. 77) that is not in the file (pp. 79-96)." |
| P12 Fallback | N | **N** (extend) | Validator right that SEFL 110 is a definition (13-065 l. 175-187). What it missed: SEFL's fuel rules live in a separate publication, the "Fuel Master Tariff SEFL195", listed among the governing publications of Item 100 (l. 164) and cited "per 195 Fuel Surcharge Tariff" (l. 636); it is not in `data/`. walk A had reported the 195 pointer. ABF 161 (l. 801-806, 1046-1050, 1070-1071), Estes 530 (l. 2073-2095; Tuesday's DOE price, effective Wednesday), FedEx 570 (l. 1557-1561, Monday's price; base "linehaul transportation, and other services which consume fuel", so not net linehaul only) all re-opened. | "… the fuel-base item (ABF 161, Estes 530, FedEx 570); SEFL's fuel rules are in its separate SEFL 195 Fuel Master Tariff (named in 1090 Item 100; not held), Item 110 only defines the surcharge; the net-only base is observed on the bills." |
| P12 Never | KV | C | 14-076 `["$3.910", "$3.930", "32.00%", "35.30%"]`; 13-046 l. 876 "3.76 3.77 31.70% 63.40%"; 13-046 l. 18 "tendered on or after September 9, 2024"; 14-074 (read from a scratch copy): 2024-07-29 = 3.768. | — |
| P12 If none | N | C | as P10 If none. | (validator's) |
| P13 Primary | KA | C (KA stands) | No base table; 23-005 names a "customized Czarlite International Tariff" (l. 85580) but does not hold it. | — |
| P13 Fallback | KV | C | 02-002 p. 46 l. 15 "509 60080 3058.07" (5.09 × 600.80 = 3,058.07); 19-001 ST 0001 `L1**40.17*PH*26111`. | — |
| P13 If none | KV | C | — | — |
| P14 Primary | KA | **O** | Not untestable: a real shipper-to-carrier TL tender with its price is held. 19-027 (`brycejech_204-MGSEABOARD-RASY…`, catalogue "real"): ISA sender MGSEABOARD → RASY, `N1*BT*Seaboard Foods`, `N1*SH*Americold`, `L11*TL*MD*Mode`, **`L3*42186*G*2377.08*FR*237708`** (flat $2,377.08 for 42,186 lb). The validator's census looked only at rate confirmations. No invoice for that load is held, so the match is untestable, the format is not. | Primary *verified* for the 204 L3 form (19-027: `L3-03` rate, `L3-04` FR, `L3-05` charge in cents); a shipper-issued rate confirmation is still not held. |
| P14 Fallback | N | C | 13-068 l. 747 "ITEM 310 DETENTION WITHOUT POWER", l. 797 "ITEM 310 FUEL SURCHARGE" (Monday DOE price for loads dispatched Monday-Sunday, l. 799-801); 11-039 l. 167-171; 22-012 p. 8 l. 35 "constitutes an addendum". | (validator's) |
| P14 Never | KV | C | 22-012 p. 5 l. 33-36 "THIRD PARTY FREIGHT CHARGES BILL TO: … C/O Cass Information Systems"; p. 4 (render) bill-to "BEST DEDICATED SOLUTIONS". | — |
| P14 If none | KV | C | — | — |
| P15 Primary | N | C | 10-038 l. 151-153 "CARRIER AGREEMENT … This Carrier Agreement" (Coyote, broker-carrier); TQL 10-037 l. 747-749 "Detention starts 3 hours after APPT …", "must be requested within 5 business days"; KCH 10-043 l. 2 "Carrier Rate and Load Confirmation", l. 55 "within 2 hours after the appointment time"; 22-012 pp. 7-8, 20 as quoted. | (validator's) |
| P15 Fallback | KV | C | 11-039 l. 185-187; 13-068 l. 770-780 (2 hours, $110); 13-071 l. 809-812 ($75/h after 1.5 h, $650/day single, $1,300 team). | — |
| P15 If none | KV | C | — | — |
| P16 Primary | KV | **N** | All quotes re-opened (08-024 l. 305-307; ABF 428 13-047 l. 1910-1915; ODFL 396 ¶1; XPO 23(5); Saia 1030(6); FedEx 438; TForce 813; AAA Cooper 660; Central 460(1),(4); 16-095 l. 4; 23-012 p. 78 e; 11-037 l. 504-507). Two misses. (1) For Home Depot the validator cites §8 ¶C (duplicate payments, a 15-day response), but the claim window is **¶I: "eighteen (18) months from the date of receipt of a shipment by the consignee"** (23-005 l. 1260-1262), longer than the statute. (2) Saia 1030 has a second start date in the same item: ¶7 "no later than 180 days from the date of original freight bill presentation" (13-056 l. 7806-7811) beside ¶6 "date of the original bill". | Add "Home Depot §8 ¶I (18 months from consignee's receipt); Saia 1030(6) bill date and 1030(7) presentation". |
| P16 Fallback | KV | C | AM l. 155 (§AM4.3 heading), l. 191 "public SMB broker terms allow 5-30 days"; 22-012 p. 8 l. 22-24 "FORTY-FIVE (45)". | — |
| P16 If none | KV | C | — | — |
| P17 Primary | KV | C | 08-024 l. 298-300; 13-061 l. 840-841; 13-056 l. 7794-7797; 13-071 l. 402-405; 23-005 l. 1216-1222 and l. 85366-85367; 11-037 l. 463-467 (runs from "the date such Transportation Service is provided"); 23-012 p. 78 (render) c(2). | — |
| P17 If none | KV | C | — | — |
| P18 Primary | KV | C | SEFL 817 ¶1 l. 4099-4101, ¶4 l. 4115-4117 25%; ABF 427 ¶2A l. 1887-1889; ODFL 434 ¶2-3 l. 1359-1363, 564 ¶1 35%; XPO 207 13-063 l. 1555-1560; Estes 720 l. 3077-3088; TForce 721 ¶1 l. 2671-2672. Nuance: TForce's "1.5% per month" runs only once the receivable "is placed with the collections agency and/or legal counsel" (l. 2682-2684). | — |
| P18 Fallback | KV | C | 02-002 p. 46 footer; 03-003 p. 11 (render); 21-005 has 23 "REFERENCED IN TARIFF" lines (the "199" wraps), 21-004/-005 have 3 + 15 "PAYMENT IS DUE BY"; 21-002 p. 17 (render); 22-012 p. 4; 22-008 p. 4 (render) "ICC REGULATIONS REQUIRE PAYMENT WITHIN 15 DAYS". | — |
| P18 If none | KV | C | — | — |
| P19 Primary | KV | C | 13-065 l. 2579-2588 Item 752; 13-061 l. 1291-1321 Item 200. Note SEFL 752 waives "all freight charges", not just the fee, and states no refund window. | — |
| P19 Fallback | N | C | 04 OCR `…20040.0.txt` l. 1429, 1723, 2824, 3023 "GUARANTEED DELIVERY REQUESTED (If box is checked)"; 05-015 p. 1 (render) "EXACT EXPRESS SERVICE / XPRS DATE: 12/29/08 / DELIVER BY: 17:00 LOCAL TIME", Yellow. | (validator's) |
| P19 If none | KV | C | — | — |
| P20 Primary | KV | C | 13-047 l. 3305-3307 "Charges will not apply on shipments when the charge in Item 440 … is assessed"; 13-061 l. 1923-1924 (one charge across Items 201, 202, 219, 224, 226). | — |
| P20 If none | KV | C | — | — |
| P21 Primary | KV | C | ODFL 565 13-053 l. 2078-2082; Estes 530 l. 2078-2079; 19-001 6.5 × 40.17 = 261.105 → `26111`; 19-015 ST 60001 8.10 × 298.86 = 2,420.77. Another unit in the same Estes file: ST 60003 `L1*2*197.00*FR*19700` (flat). | — |
| P21 Never | KV | C | as above. | — |
| P21 If none | KV | C | — | — |

**§2.1 tally (68 cells):** C 57, N 9, O 2, CNT 0.

### 2.2 The §1.1 columns (validator §3: 63 entries, all KV)

| Validator rows | Val. | Mine | Evidence | Note |
|---|---|---|---|---|
| P01-P21 Checks (21 entries) | KV | C ×21 | AK §3.2 l. 136-177: each named check's "Data needed" calls for the fact (A5 "BOL freight-terms box and bill-to"; B1 "Every version with effective dates"; B2 "Base tariff … discount; class"; B3 "Agreement minimum"; B4 "FAK table"; B5 "Quote document or ID"; B6 "Rate confirmation or contract"; B7 "Contract mileage basis"; B8 "Fuel table in force, EIA index, effective-day rule"; B9 "Invoice"; C2 "Tariff thresholds"; D1 "Accessorial schedule and waivers"; D2-D7; E1 "transit standard"; F1 "late-fee rule"; G1 "Carrier tariff, contract, statute"; A4 "original bill date" and 13710(a)(3); A1 "Invoice"). | One gap the validator did not test (reverse direction): G2 "Carrier's response deadlines … 49 CFR 378: acknowledge in 30 days, decide in 60" is a rule of the same kind as P16/P17, but no P row carries it (only D04/D05 carry the dates). See §7. |
| P01-P21 Role (21) | KV | C ×21 | Consistent with AX §4-§5 and the §5 traces. | — |
| P01-P21 Need (21) | KV | C ×21 | Every "must" price term is NOT REPORTED in at least one chain with its lines then "not checkable" (§5.7 of the doc). | — |

### 2.3 The §3 rows (validator §4.1: 12 rows, all KV)

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| §3.1 Discount % | KV | C | 19-001 ST 0001 `L1**-188.00*PH*-18800****DSC`, `L1**40.17*PH*26111`; 188.00 ÷ 261.11 = 0.7200. |
| §3.1 Fuel % | KV | C | 01-001 "30.3%" on 60 lines; 13-046 l. 876 "3.76 3.77 31.70%"; 13-046 l. 18 "on or after September 9, 2024"; 14-074 2024-07-29 = 3.768 (re-read, closing the validator's §7 item 12). |
| §3.1 Quote applied | KV | C | per unique bill: 82 PQ, 27 difference notes (Python over 01-001). |
| §3.1 TL price | KV | C | 22-012 p. 4 (render) "FLAT RATE 1 Flat 993.96", "332 Miles .47 $/Mile $156.04", "Total: $1,150.00"; p. 8 l. 4-6 "Net Freight Charges USD 1,150.00". |
| §3.1 Miles | KV | C | 22-012 p. 6 l. 37 "Distance (Miles): 335.15"; p. 4 "O-D/Routed 332/332"; 11-037 l. 1085-1086 "PC Miler, Version 31"; 335.15 × 0.47 = 157.52. |
| §3.2 lane terms bullet | KV | C | Only 02-002 is walked; but see P02 If none: 23-005 is a second agreement held, so "the agreement only" is a statement about the chain, not about `data/`. |
| §3.2 quote bullet | KV | C | no quote document (P08). |
| §3.3 transit standard | KV | C | SEFL 752 "by its published standards" (13-065 l. 2585); XPO 200 "listed on the Carrier's website (Transit Time Calculator)" (13-061 l. 1302-1303). |
| §3.4 Discount % | KV | C | as §3.1. |
| §3.4 Fuel % | KV | C | 12.79 ÷ 73.11 = 0.1749. |
| §3.4 Rate unit | KV | C | 5.09 × 600.80 = 3,058.07. |
| §3.4 TL fuel per mile | KV (file added) | C | 22-008 p. 4 (render): freight bill 39015347, pickup 01/13/2023, MILES 154, "FUEL ADJ/MILEAGE 93.94", total 753.98; p. 7 (render): 39060407, 97.02, 154 miles; 0.610 and 0.630. |

### 2.4 The §4 citations (validator §4.2: 69 rows)

| # | Validator row | Val. | Mine | Evidence | Corrected wording |
|---|---|---|---|---|---|
| 1 | §4.2 NMFC 250100-A §4 | KV | C | 15-079 l. 1693-1696. | — |
| 2 | Uniform BOL §7(d) | KV | C | 15-077 l. 51-53 (right column of Sec. 7, which opens at l. 34). | — |
| 3 | ABF 992 ¶4, l. 5630 | N | C | "no weight whatsoever": 13-046 l. 5579, 13-047 l. 5604, 13-048 l. 5630; fee $91.48 (13-047 l. 5605-5606). | (validator's) |
| 4 | Estes 993 | KV | C | 13-049 l. 4331-4335 "REVISED: AUGUST 3, 2026", $20.00. | — |
| 5 | ODFL 367 ¶7 | KV | C | 13-053 l. 1117-1119. | — |
| 6 | XPO 239 $50.70 | KV | **N** | The wording is in AK.1 (13-061 l. 2374-2376) but **AK.1's fee is $47.85**; $50.70 is AK.3 only (13-063 l. 2455). The validator combined the AK.1 wording with the AK.3 amount, the edition mix it criticised in row 33. | "XPO 239 ($50.70 from 17 Aug 2026; $47.85 Feb-May 2026; $27.25 in 2018)" |
| 7 | Central 400(b) $35 | KV | C | 13-073 l. 801-802 "$35.00 will apply per change"; (b) is at l. 810. | — |
| 8 | SEFL 170 class 150 | KV (edition *assumed*) | C | 13-065 l. 313 "Effective: Dec 1st, 2025"; l. 330-331. | — |
| 9 | XPO 26.3 | KV | C | 13-061 l. 1008-1010. | — |
| 10 | Estes 170 class 175 | KV | C | 13-049 l. 482-485. | — |
| 11 | TForce class 250 | KV | C | 13-060 l. 1401-1404. | — |
| 12 | TForce 120×96×96, retag *verified* | KV | **N** | The words are at 13-060 l. 2433-2436, but they sit in **Item 645-A "Application of Density Based Rates"**, which opens: "Density based rates will only be available upon a written agreement executed by each of customer and Carrier. Where the customer and Carrier have established density based rates in such an agreement, the following terms and conditions shall apply" (l. 2416-2418). The default is not a general rule for every TForce shipment. explore_rules_2 l. 57 omitted the scope; neither the doc nor the validator restored it. | "… for customers with a written density-based-rate agreement, an omitted dimension defaults to 120×96×96 in (TForce 645-A Part 2 ¶4)" |
| 13 | ODFL 100-Q (l. 727-736), verification fee | KV (A: Item 162) | C | Item 162: 13-052 l. 725-727, 13-053 l. 734-736. The doc's "727-736" is one line from each capture, not a range (same pattern as ledger 34). | — |
| 14 | SEFL 753 §2 | KV | C | 13-065 l. 2679-2685. | — |
| 15 | SEFL 754 | KV (edition) | C | l. 2708 "April 2, 2024"; l. 2724-2728. | — |
| 16 | Estes 751 / 751-10 | KV | C | 13-049 l. 3380-3384; l. 3497-3499. | — |
| 17 | TForce 753 ¶8 | KV | C | 13-060 l. 2855-2857. | — |
| 18 | Freight terms default, retag *verified*, Canada | N | C | FedEx 360 ¶6 A-B in both series: 13-050 and 13-051 l. 1014-1017; TForce 361-A ¶3 13-060 l. 1423-1425. | (validator's) |
| 19 | *PJAX* l. 342 | KV (file 20-005) | C | 20-005 l. 342-343; 20-003 has no PJAX text (171 lines). | — |
| 20 | FedEx 980 ¶2 | KV | C | 13-051 l. 3345-3348. | — |
| 21 | HB44 §5.58 | KV | C | 15-078 l. 209, 229-230. | — |
| 22 | SEFL 992 $33 | KV | C | 13-065 l. 4741-4747 (custody limit). | — |
| 23 | ABF 992 ¶5 $317.17 | KV | C | 13-047 l. 5608-5611 (13-048 l. 5635; absent from 13-046). | — |
| 24 | TForce 990 $220 | KV | C | 13-060 l. 4287-4290 (¶3). | — |
| 25 | FedEx 990 | KV | C | 13-051 l. 3374-3377. | — |
| 26 | 13708(a) in *Sivak* | KV | C | 08-030 l. 1050-1055. | — |
| 27 | Part 378.4(d), 378.5(c), .7, .8, .9(b), .3(a) | not testable | CNT (agree) | No copy in `data/`; see §7 for what AX quotes and how the doc uses it. | — |
| 28 | NMFC 300330(d)/300340(c)/300520(g) | KV (15-081) | C | 15-081 l. 1125-1127, 1152-1154, 1256-1257. Scope caveat the doc partly carries: 300300-A limits the 300300-series to "motor carriers of household goods, motor carriers participating in the noncontiguous trade, and freight forwarders" (l. 1077-1084); ordinary carriers fall under 300500-530 (l. 1214-1221). | — |
| 29 | XPO claim page | KV | C | 16-083 l. 20-23. | — |
| 30 | ODFL 396 ¶2, Central 460(2), $50 | KV | C | 13-053 l. 1306-1309, NOTE A l. 1315-1316; 13-073 l. 907-909. ODFL 396 also says "All other provisions of U.S. Code 49 CFR 378 relating to overcharge claims shall apply" (l. 1313). | — |
| 31 | SEFL 170 Note 3 | KV | C | 13-065 l. 347-350. | — |
| 32 | Estes 170 Note C | KV | C | 13-049 l. 507-508. | — |
| 33 | XPO 205 proof only in AK.3 | N | **N** | Present in **AK.2** too: 13-062 l. 1500 "conclusive documentary", l. 1506 "Acceptable documentary proof" (effective May 18, 2026); AK.3 l. 1521, 1527; absent from AK.1 and AB-4 (0 hits). The coordinator's check (13-061/13-063/13-064 only) also missed 13-062. | "XPO 205's proof wording from 199-AK.2 (18 May 2026) on; not in AK.1 (Feb 2026) or AB-4 (2018)" |
| 34 | TForce edited BOL refused | KV | C | 13-060 l. 1410-1411, 1469-1471. | — |
| 35 | Estes 992 ¶4 "satisfactory proof" | N | C | 13-049 l. 4323-4329 (apportioning a corrected weight across articles). The exploration agent read it correctly ("weight can be reapportioned between items", explore_rules_2 l. 89); the rebuttal reading entered at the doc stage. | (validator's) |
| 36 | FedEx 980 ¶3 | KV | C | 13-051 l. 3350-3352. | — |
| 37 | YRC, ABF, FedEx, R+L forms | KV | C | 16-095 l. 31; 16-092 l. 75; 16-082 l. 61-62 (also "Weight certificate or certified statement when claim is based on weight"); 16-093 l. 27. | — |
| 38 | NMFC 401400-A, retag *verified* | KV | C | 15-081 l. 1532-1537, PDF p. 25; the rule covers "a shipment reweighed at destination" and also requires claims to "include evidence of actual weight". | — |
| 39 | ABF 362 30 days | KV | C | 13-047 l. 1574-1575. ABF 362 ¶2 also has a proof rule the doc omits: "Changes in description or weight will be permitted only upon presentation of satisfactory documentation (e.g., …" (l. 1588). | — |
| 40 | XPO 205 from acceptance | KV | C | 13-061 l. 1468-1470. | — |
| 41 | R+L 364 from the bill date | N | C | 13-058 l. 1182-1184. The exploration agent gave no start ("R+L 364: 30 days; $45.90", explore_rules_2 l. 83); "from the bill date" was added in the doc. | (validator's) |
| 42 | "conclusive documentary proof" (ODFL 365, XPO 205) | N (XPO edition) | **N** | ODFL 365 ¶5 13-053 l. 1053-1055 ✓; XPO from AK.2 (row 33); **R+L 364 uses the same words** (13-058 l. 1180), uncited by doc and validator. | "conclusive documentary proof (ODFL 365, R+L 364, XPO 205 from AK.2)" |
| 43 | SEFL 360-5 §5 | KV | C | 13-065 l. 544-547. | — |
| 44 | SEFL 360-5 §6, $35 | KV | C | l. 549, NOTE A l. 552. | — |
| 45 | TForce refusal after tender, retag *verified* | KV | **N** | 13-060 l. 2443-2444, same Item 645-A as row 12: applies only where density-based rates are agreed in writing. | "Refused after tender for customers on density-based rates (TForce 645-A Part 2 ¶8)" |
| 46 | 13710(a)(3)(A) | KV | C | 08-024 l. 298-300, 364-366. | — |
| 47 | XPO 23(5) | KV | C | 13-061 l. 823, 840-841. | — |
| 48 | Saia 1030(5) | KV | C | 13-056 l. 7794-7797. | — |
| 49 | USA Truck 17 | KV | C | 13-071 l. 400-405. | — |
| 50 | ABF 428 l. 1917 | N | C | 13-048 l. 1917; 13-047 l. 1912; 13-046 l. 1911. | (validator's) |
| 51 | AAA Cooper 660; Werner 585 | KV | C | 13-066 l. 2063-2067; 13-068 l. 1238-1242. | — |
| 52 | Home Depot §8 90 days | KV | C | 23-005 l. 1216-1222. | — |
| 53 | First Brands §13-14 | KV | C | 11-037 l. 453-467, 502-507. | — |
| 54 | Walmart 12 months | KV | C | 23-012 p. 78 (render) c(2) and e. | — |
| 55 | 13710(a)(3)(B) | KV | C | 08-024 l. 305-307, 368-370. | — |
| 56 | ABF 428; YRC 180 days of pickup | KV | C | 13-047 l. 1911-1913; 16-095 l. 4. | — |
| 57 | ODFL 396, Central 460 | KV | C | 13-053 l. 1303-1304; 13-073 l. 906. | — |
| 58 | XPO 23(5), Saia 1030(6) | KV | C | 13-061 l. 841-842; 13-056 l. 7800-7801. Saia 1030(7) adds "date of original freight bill presentation" (l. 7810-7811). | — |
| 59 | FedEx 438 | KV | C | 13-051 l. 1376-1378. | — |
| 60 | TForce 813 | KV | C | 13-060 l. 3586-3593 (it also cites "NMFC series items 300500 and 49 CFR Part 370"). | — |
| 61 | NMFC 300320/300520 "5 business days" | KV (15-081) | **N** | The words are at 15-081 l. 1101-1102 and 1232-1233, but 300300-A limits 300320 to household-goods, noncontiguous-trade carriers and freight forwarders (l. 1077-1084). For the LTL carriers the doc is about, only 300520-A(a) applies, and only to NMFC participants ("Only participants in the NMFC at the time the transportation occurs may use the provisions herein", the footer of every page, e.g. l. 1274). | "'5 business days from the invoice date' (NMFC 300520(a), for NMFC participants; 300320 is the household-goods twin)" |
| 62 | SEFL has no item | KV | C | 13-065: 0 hits for "overcharge". R+L 13-058 also has 0 hits for "overcharge": a second carrier where the statute governs. | — |
| 63 | brokers 5-30 days; XPO page | KV | C | AM l. 191; 16-083 l. 27-28. | — |
| 64 | 378.7, 378.8, 378.9(b), 378.3(a) | not testable | CNT (agree) | §7. | — |
| 65 | HB44 30 days | KV | C | 15-078 l. 229-230. | — |
| 66 | *Southern Furniture* ¶1 | KV | C | 08-024 l. 398-402, 440-441. | — |
| 67 | §4.5 ¶2 dates | KV | C | 2023-06-19 + 180 d = 2023-12-16; 2023-05-05 + 180 d = 2023-11-01 [calc]; p. 41 footer "05/0512023" billed, "05120/2023" due (text l. 52-55). | — |
| 68 | *PJAX* l. 128 | KV | C | 20-005 l. 128-129. | — |
| 69 | STB voluntary payment (C-AM25) | KV | C | AM l. 113. | — |

**§2.4 tally (69 rows):** C 61, N 6, O 0, CNT 2.

### 2.5 The P rows of the six §5 chains (validator §4.3: 41 rows)

| Validator row | Val. | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| A, P01 | KV | **N** | The row's source is SEFL 1090 Item 753 §5, which reads "The charges provided in this item will be assessed against the payor of the freight charges …" (13-065 l. 2698-2700): it says who pays the *residential charge*, not whose *pricing* applies. The payor-pricing rule the doc's own §2.1 names is SEFL 201 ¶1 (l. 372-374). Bill p. 46 l. 39 "PREPAID", footer l. 52 "071-003454", agreement p. 18 l. 10 ✓. walk A made the same citation; the doc and the validator kept it. | "SEFL 1090 Item 201 ¶1 (payor's pricing); bill p. 46 'PREPAID', bill-to Exist; account 071-003454 on the 2023 version p. 18 and the bill footer" |
| A, P02 | KV | C | pp. 12, 15, 18 as in §2.1 P02; 04/12/2023 version in force on 05/15/2023 (p. 46 l. 44). | — |
| A, P03 | KV | C | p. 18 l. 15. | — |
| A, P04 | KV | C | p. 19 render WCPC outbound 88.15; p. 13 l. ~22-23 "WCPC OUTBOUNO PPD/COL … 90.90"; p. 20 WCPC definition includes OR. | — |
| A, P05 | KV | C | p. 19. | — |
| A, P06 | KV | C | p. 20 "S152.00" for "AZ, CA, 10, MT, NV, OR …". | — |
| A, P07 | KV | C | 13-065 l. 1229-1245; agreement silent. | — |
| A, P09 | KV | C | p. 22 render. | — |
| A, P10 | KV | C | 13-065 l. 2669-2696. | — |
| A, P11 | KV | C | l. 4768, 4781-4782; l. 4741-4747. | — |
| A, P12 | N (Item 110) | C | p. 46 l. 22 "LTL FUEL SURCHARGE OF 22.00% … 79.72"; 0.22 × 362.38 = 79.72. Add the SEFL 195 pointer (§2.1 P12 Fallback). | (validator's, + SEFL 195) |
| A, P13 | KV | C | p. 46 l. 15. | — |
| A, P16/P17 | KV | C | 13-065: 0 "overcharge"; Item 202 ¶7 l. 444 (allowances). | — |
| A, P18 | KV | C | 13-065 l. 4099-4101; footer 06/19 → 07/04/2023. | — |
| A, bill 806266163 | KV | C | p. 94 l. 13-35 (all strings); 1,893 + 4,581 + 2,446 = 8,920; 27,523.00 − 24,068.86 = 3,454.14 = "MIN FRT CHG". | — |
| A, sibling 806625953 | KV | C | p. 41 l. 15-36; p. 19 MWPC 90.30; 744.77 ÷ 0.097 ÷ 315.97 = 24.30 cwt. | — |
| B, P01 | KV | C | 03-003 p. 14 render "PPD", footer "SUBJECT TO THE TERMS AND CONDITIONS HEREIN, AND TARIFF CNWY-199 IN EFFECT ON DATE OF SHIPMENT"; the DR's BILL TO box is empty; p. 11 render bill-to VPX SPORTS. | — |
| B, P04 | KV | C | p. 11 render; 0.25000. | — |
| B, P10/P11 | KV | C | 13-063 l. 2457-2459; 13-064 l. 2184-2186; p. 11 "$37.25". Note: the 2026 issues disagree among themselves too ($47.85 in AK.1/AK.2), so "matches neither" holds for all four XPO issues held. | — |
| B, P12 | KV | C | 1,406.89 × 0.26 = 365.79. | — |
| B, P16/P17 | N (Item 7 ¶9) | C | 13-063 l. 352 "Bill of Lading - Terms and Conditions Item 7", ¶9 l. 486-488; 13-064 l. 348, 455-457. | (validator's) |
| B, P18 | KV | C | 13-063 l. 1555-1560; 13-064 Item 207 (no %); 0.015 × 1,809.93 = 27.15. | — |
| C, P01/M06 | KV | C | 19-001 ST 0001 B3 and `N1*BT*DALMATION PRESS LLC`. | — |
| C, P03 | KV | C | `L7*******050` in ST 0001. | — |
| C, P04/M11 | KV | C | no L5 in any ODFL 210 (L5 census: 0 in all eight). | — |
| C, P12/M13 | KV | C | 0.1749 and 0.0490. | — |
| C, P13/M09 | KV | C | `L1**40.17*PH*26111`. | — |
| C, P21 | KV | C | 261.105 → 26111. | — |
| C, contrast AAA Cooper | KV | C | 19-009 ST 0014 full dump matches every segment quoted; 1,147.26 − 894.86 + 73.20 = 325.60 = B3-07. | — |
| C, contrast Estes | KV | C | 19-015 ST 60001 dump; 2,420.77 − 2,033.45 + 24.05 + 112.32 = 523.69 = B3-07; ST 980 BT1 1,218.85 = 523.69 + 498.16 + 197.00. | — |
| D, P03/P04/P12 | KV | C | 21-002 p. 17 render: TARIFF "559", "Discount Allowed: 70.00%" 2299.53, FUEL INCREASE 133.04; 133.04 ÷ 985.51 = 0.1350. | — |
| D, P07 | KV | C | p. 6 render "Over 15 Dens.", "156600-3", "250", "2304# Net / 168# Tare / 2472# Gross"; 218.17 ft³, 11.33 pcf. | — |
| D, P11 dates (ledger 18) | N | **O** | The labels are on the files. The Item 365 page prints **"Revised 11/03/2025"** in 13-052 (l. 1020, two lines above "ITEM 365", fee "$40.00" l. 1055) and **"Revised 10/05/2026"** in 13-053 (l. 1029, fee "$45.00" l. 1064); 13-053's cover adds "Updated: October 5, 2026" (l. 38). The catalogue's verify_note for 13-053 says "26 items stamped Revised 10/05/2026 … Distinct version". walk B wrote "copy _b, revised 10/05/2026; copy _a, revised 11/03/2025". "Effective: April 14, 2025" is the issue date of 100-Q, not the item's revision. | Keep the doc's "$45 in the 10/2026 revision, $40 in 11/2025"; better: "$45 (Item 365 revised 10/05/2026, 13-053); $40 (revised 11/03/2025, 13-052); both in issue 100-Q of April 14, 2025". |
| D, P18 | KV | C | p. 17 render terms box "within 42 days from the original invoice due date … 135%", "ITEM 434"; "Due Date 03/05/05". | — |
| E, P10 | KV | C | 23-003 p. 5 text layer l. 1-15: "declined per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse". | — |
| E, P16 | KV | C | 16-095 l. 4-5. | — |
| F, P01/P02 | KV | C | 22-012 p. 6 l. 28, 31; p. 8 l. 35. | — |
| F, P08/P09/P14 | KV | C | p. 8 l. 4-6, 20; p. 6 l. 37. | — |
| F, P15 | KV (semicolon) | C | p. 20 crop render: "DETENTION; FAILURE …" and "RECEIVER; FAILURE …" (semicolons on the image; the text layer and walk C have colons). Also on p. 20: "$150 LATE FINE FOR DELIVERY WITHOUT ADVANCE COMMUNICATION". | — |
| F, P16/P17 | KV | C | p. 8 l. 22-25. | — |
| F, P18 | KV | C | p. 4 render; p. 9 l. 1. | — |
| D, P01 (not in the validator's 41) | — | C | 21-002 p. 13 render "2/14/05 RATE AR 33878 … 584.63 … WINN DIXIE"; p. 15 render "2/18/05 RATE AR 76652 1,133.55 CLAMP-SWING PRICING" and the 584.63 reversal; the A/R prints no class, so "at class 85" is the doc's inference, which its How column says. | — |

**§2.5 tally (41 rows):** C 39, N 1, O 1; plus one untested row (D P01) confirmed.

### 2.6 The §8 ledger rows (validator §4.4: 42 rows incl. 35a-35r)

| Row | Val. | Mine | Evidence / correction |
|---|---|---|---|
| 2 | KV | C | 13-065 l. 2669, 2679-2685, 2694-2696. |
| 7 | KV (+ NMFC caveat) | C, caveat **N** | 0 "overcharge" in 13-065 ✓. The caveat that NMFC "300320/300520" may be SEFL's "rules governing the handling of such claims" (817 ¶6, l. 4131-4133) is half wrong: 300320 is limited to household-goods, noncontiguous and forwarder carriers (15-081 l. 1077-1084); only 300520 could apply, and only if SEFL participates in the NMFC (Item 100 lists NMF100, l. 150-156). |
| 11 | KV, retag | **N** | Item 207 10%, min $50 ✓ (13-063 l. 1559-1560; also AK.1 l. 480-481). "$50.70 at +25 lb (2026)" holds for AK.3 only; AK.1 and AK.2 print $47.85. Retag *verified* with "AK.3 (Aug 2026)" named. |
| 18 | N (dates unsourced) | **O** | See §2.5 D P11: "Revised 10/05/2026" (13-053 l. 1029) and "Revised 11/03/2025" (13-052 l. 1020) are on the item's page. Retag *verified* as written in the doc. |
| 23 | KV | C | 16-095 l. 4-5. |
| 25 | KV | C | 15-079 l. 1694-1696; 15-077 l. 51-53. |
| 26 | N (13-048 lines) | C | 13-048 l. 5630, 1917; 13-047 l. 5604, 1912. |
| 27 | KV | C | 13-049 l. 4333, 484, 3383, 3498. |
| 28 | KV | C | 13-065 l. 331, 349, 545-549. |
| 29 | KV | C | 13-061 l. 1010, 1470, 840. |
| 30 | KV | C | 13-060 l. 1404, 2856. |
| 31 | KV, retag + Canada | **N** | FedEx 360 ¶6 (both series) and TForce 361-A ¶3 ✓. The TForce dimension default and post-tender refusal are in Item 645-A, which applies only under a written density-based-rate agreement (13-060 l. 2416-2418). Retag *verified* with that scope. |
| 32 | KV | C | 13-051 l. 3348, 1378. |
| 33 | KV | C | 13-056 l. 7796. |
| 34 | KV (+ Item 162) | **N** | The cited pairs "1297/1306" and "727/736" are one line per capture: 1297 and 727 are 13-052's, 1306 and 736 are 13-053's (Item 162 at 13-052 l. 725-727, 13-053 l. 734-736; 396 ¶2 at 13-052 l. 1297, 13-053 l. 1306). The doc cites both to 13-053. |
| 35 | KV, retag | C | sub-rows below. |
| 35a ODFL 367 | KV | C | 13-053 l. 1088-1119. |
| 35b ODFL 365 | KV | C | l. 1031-1064 ($45; revised 10/05/2026). |
| 35c Central 400(b) | KV | C | 13-073 l. 801-802, (b) at l. 810. |
| 35d Central 460 | KV | C | l. 905-913. |
| 35e AAA Cooper 660 | KV | C | 13-066 l. 2063-2067. |
| 35f AAA Cooper 970 | KV | C | l. 3814-3832. |
| 35g Werner 585 | KV | C | 13-068 l. 1238-1242. |
| 35h USA Truck 17 | KV | C | 13-071 l. 400-411. |
| 35i Saia 850 | KV | C | 13-056 l. 6115-6118, 6124-6125. |
| 35j Dayton 1015 | KV | C | 13-072 l. 4975-4990. |
| 35k R+L 364 | KV | C | 13-058 l. 1176-1186. |
| 35l Estes 360-03 | KV | C | 13-049 l. 1362-1374. |
| 35m Estes 992 ¶4 | N | C | l. 4323-4329. |
| 35n SEFL 992 | KV | C | 13-065 l. 4741-4747. |
| 35o ABF 992 ¶5 | KV | C | 13-047 l. 5608-5611. |
| 35p TForce 990 | KV | C | 13-060 l. 4287-4290. |
| 35q FedEx 990 | KV | C | 13-051 l. 3374-3377. |
| 35r "HB44" label | N | C | 15-078 prices nothing (l. 205-231). |
| 36 | N (15-081) | **N** | File 15-081 ✓ (0 hits for 300330/300520/401400 in 15-079). But the validator's "l. 1148 is 300340-A(b)" is wrong: l. 1148 is (a) ("Upon receipt of a claim … within 5 business days initiate an investigation"); (b) is l. 1150, (c) l. 1152-1154. |
| 38 | KV | C | 08-024 l. 298-307, 364-370, 400-402, 440-441. |
| 39 | N (20-005) | C | 20-005 l. 128-129, 342-343. |
| 40 | KV | C | 16-083 l. 20-23, 27-28. |
| 41 | KV | C | 23-005 l. 1211-1222. |
| 42 | KV | C | 11-037 l. 453-467, 502-507; 23-012 p. 78 render. |
| 43 | KV | C | 15-078 l. 209, 229-230. |
| 45 | KV, retag, file | C | 15-081 l. 1532-1537, PDF p. 25. |

**§2.6 tally (42 rows):** C 37, N 4 (11, 31, 34, 36), O 1 (18); row 7's KV confirmed with its caveat narrowed.

### 2.7 The validator's additions (§5: A1-A11)

| Add | Mine | Evidence | Corrected wording |
|---|---|---|---|
| A1 payor rule, more tariffs, 3PL nuance | **N** | AAA Cooper 760 ¶1 and Note B (13-066 l. 3168-3189) ✓; SEFL 201 Note B (13-065 l. 384-386) ✓. ABF's item is **765** "PRIORITY OF PRICING--ORDER OF PRECEDENCE" ¶3 "Paying party" (13-047 l. 3872, 3897; 13-046 l. 3891), not 760; the drafted "ABF, AAA Cooper 760" reads as if ABF were 760. Add USA Truck 14 and Werner 570 (TL), Saia 105's volume exception, and the FedEx/TForce correction of §2.1 P01. | see §2.1 P01 wording |
| A2 second 210 naming its tariff | **N** | `L7*2*OVL*DCN****70***20131120` is ST 60001, but `L7*2*EXL*MAN****70***20131120` is **ST 60002** (19-015 dump). More examples: AAA Cooper `SMC*ZRH` (19-009 ST 0015, 19-011, 19-012, 19-014); Roadway 19-031 `L7*1*RDWY*4516` ("partly real"). | "Estes 19-015 ST 60001 `OVL DCN`, ST 60002 `EXL MAN`; AAA Cooper `CZAR 910` / `SMC ZRH`; Roadway 19-031 `RDWY 4516`" |
| A3 FAK per route × direction | **N** | Partner rows ✓ (p. 19: outbound 77.5-175, inbound collect 77.5-125). But "direct SEFL and every INBOUND COL row read 77.5 THRU 125" is wrong for p. 18: the **SEFL INBOUND COL** and **INTRASTATE-FL INBOUND COL** rows read "ACTUAL" with no FAK range (p. 18 l. 43, 65), and the CNPC rows are "ACTUAL" too; 77.5-125 is on SEFL and INTRASTATE-FL *outbound* rows (l. 15, 46). | "FAK per route × direction: SEFL and intrastate outbound 77.5-125; partner outbound 77.5-175; partner inbound collect 77.5-125; SEFL and intrastate inbound collect and Canada: actual class, no FAK" |
| A4 more shipper-window sources | **N** | Central 460(4) l. 910-911 ✓; Werner 585 ✓; USA Truck 17 ✓; NMFC: 300320 is the household-goods/forwarder item (300300-A), so only 300520(a) belongs here. Add Home Depot §8 ¶I (18 months, 23-005 l. 1260-1262) and Saia 1030(7) ("original freight bill presentation", l. 7810-7811). | "Central 460(1),(4); Werner 585; USA Truck 17; Saia 1030(6),(7); Home Depot §8 ¶I; NMFC 300520(a) where the carrier participates in the NMFC" |
| A5 carrier-side windows | C | 13-047 l. 1911-1913; 13-066 l. 2065-2067; 13-068 l. 1240-1242; 13-063 l. 486-487, 13-064 l. 455-456. | — |
| A6 Werner file | C | 22-008 pp. 4, 7 renders. | — |
| A7 15-minute notice | C | 22-012 p. 20 crop render. | — |
| A8 P19 file ids | C | 04 OCR l. 1429; 05-015 p. 1 render. | — |
| A9 ODFL Item 162 | C | 13-053 l. 734-736 (13-052 l. 725-727). | — |
| A10 XPO from invoice date | C | 13-063 l. 1555-1556; Estes 720 l. 3077-3078; ODFL 434 ¶3 "the day following presentation" (13-053 l. 1362). | — |
| A11 interline accessorial precedence | C | Saia 105 ¶2-3 (13-056 l. 312-317) ✓; 02-002 p. 22 "DIRECT to PARTNERSHIP" rows ✓. A second carrier rule: FedEx 765 ¶1E, services requested off the BOL priced on "the requestor's pricing program" (13-051 l. 2692-2693). | — |

**§2.7 tally (11):** C 7, N 4.

### 2.8 Other statements of the validator that this review changes

- **§6 item 6 and §8 item 4** ("ODFL 365's dates … no file carries"; "two captures of one issue … not two revisions"): **OVERTURN**. 13-053 is a later update ("Updated: October 5, 2026", l. 38; 26 items "Revised 10/05/2026"); 13-052's latest stamps run to "Revised 07/22/2026" (one page) while Item 365 there is "Revised 11/03/2025". The catalogue row for 13-053 records "Distinct version".
- **§6 item 3** (XPO 205 wording "only in AK.3"): NARROW, from AK.2 (13-062 l. 1500-1506).
- **§7 items 7, 9, 12** (TQL/KCH not re-opened; AK.2 not opened; EIA not re-opened): closed here, all confirm the doc's or the validator's reading except item 9, which moves the XPO 205 date to May 2026.
- **§0 finding 5 / §4.5 test 1 caveat** (NMFC 300320/300520 at SEFL): NARROW as in row 7 above.

## 3. Counter-examples for the validator's generalisations

Each generalisation the validator confirmed was re-run on every file of its type in `data/` (28 tariffs of set 13; all 36 EDI files of set 19; all 101 ABF bills; the four `pricing_agreement` files; sets 10 and 22). Only the counter-examples found are listed; a generalisation not listed held.

| # | Generalisation confirmed by the validator | Counter-example (file, place, value) | Consequence |
|---|---|---|---|
| 1 | P01: "FedEx Freight and TForce rank by the BOL's terms, not the payor" | FedEx 765 ¶1D: "A pricing program published for the account of Third-Party Payor will take precedence over all other pricing programs" (13-051 l. 2684-2687); ¶1A-C put the shipper first on prepaid and the consignee first on collect, i.e. the payor under those terms. TForce 765 ¶1a-c the same (13-060 l. 3109-3133), with an affiliation override "regardless of how the shipment is identified on the bill of lading" (l. 3113-3116). | The two groups differ in mechanics, not in principle: both pick the payor's program first. NARROW P01. |
| 2 | P01: the payor rule at the seven named carriers | Saia 105 ¶1 "with the exception of volume rated shipments. On volume shipments the lowest published rate will be applicable" (13-056 l. 307-310). Estes 760 ¶1-2: an inbound-collect discount beats an outbound-collect one, and a named-party discount beats a general one, before ¶3's payor rule (13-049 l. 3600-3611). Landstar Rule 765 is a specificity ranking (customer-named rate first, then ZIP-to-ZIP …), with no payor test (13-067 l. 1735-1747). ABF 765 ¶3 adds affiliation tests for third parties (13-046 l. 3891-3915). Home Depot's Schedule A applies FAK 70 "when The Home Depot is the debtor" and actual class otherwise (23-005 l. 85596-85600). | The rule is per carrier and sometimes per agreement; the software profile needs the exceptions. |
| 3 | P03: L7 names a tariff only at AAA Cooper (CZAR); ODFL always `L7*******050` | AAA Cooper `L7*1*SMC*ZRH****060***20110919*…` in 19-009 ST 0015, 19-011, 19-012 (×3), 19-014; Roadway `L7*1*RDWY*4516****50` and `L7*1*RDWY*475****70` (19-031, "partly real"); Estes `L7*2*EXL*MAN` (19-015 ST 60002); ODFL `L7*******077` in 19-001 to 19-004 and 19-006 to 19-008. | Three carriers fill L7-02/-03; ODFL's L7-07 is the rated class, not a constant. |
| 4 | P04 Fallback: "ABF prints … never 'DISC 89.5%'" | 01-001 p. 17 (render) code column "DISC", rate column "89.5%", every bill (101/101 carry "DISC,89.5%" per unique bill number). | OVERTURN of the validator's NARROW. |
| 5 | P04 Fallback: % as L5 text at AAA Cooper and Estes; derived elsewhere | Roadway 19-031 ST 000069122: `L5*2*PERCENT DISCOUNT`, `L1*2*76.2*AV*-94884****DSC****IDIS`; fuel `L1*3*15.5*AV*4594****ENS****FSC` (the % in L1-02 with qualifier AV). 1,245.20 × 0.762 = 948.84; (1,245.20 − 948.84) × 0.155 = 45.94. | A third 210 form: the % as a rate in L1. |
| 6 | P02 If none: "the only LTL pricing agreement in `data/` is 02-002" | Catalogue `pricing_agreement`: 02-002, 09-031, 09-032, 23-005. 23-005 Schedule A (l. 85575-85636) and A-1 (l. 87850-87870, 2,177 "Point to" lines). | A second public agreement to test P02-P06 on, outside the walked chains. |
| 7 | P07: "the threshold and class are per carrier" (validator named only FedEx's 4 pcf) | Class 125 at XPO 233 (13-061 l. 2228-2229), ODFL 610-1 (13-053 l. 2710-2719), Estes 615 (13-049 l. 2693-2696); class 77.5 at ABF 611-1 ¶1 (13-047 l. 2832-2838); FedEx's floor discount of 50% (13-051 l. 1882-1887); TForce's 60% only for mileage-rated or no-class-150 pricing (13-060 l. 2203-2206). | Confirms and widens the NARROW. |
| 8 | P08 Primary: no quote document held | none found (search of all derived text; Central v. Amazon depositions mention spot quotes only). | KA stands. |
| 9 | P11: the fee items named | TForce reweigh fee is 990 ¶2 (13-060 l. 4281-4283), correction fees 361-A $50; SEFL 435-10 ¶5 "$30.00" to add a third-party payer after pickup (13-065 l. 666-667); Estes 993-10 $20 for an "inaccurate, vague or missing commodity description" (13-049 l. 4338-4342); ABF 993 $55 (explore_rules_2 l. 104, not re-opened). XPO 239 $47.85 in AK.1/AK.2. | P11's list is a sample; the fee amounts drift by issue even within 2026. |
| 10 | P12 Fallback: "at SEFL no item fixes the base" | SEFL 1090 Item 100 lists "Fuel Master Tariff SEFL195" as a governing publication (13-065 l. 164); l. 636 "per 195 Fuel Surcharge Tariff". FedEx 570's base is "linehaul transportation, and other services which consume fuel" (13-051 l. 1558-1559), wider than net linehaul. First Brands excludes "over-dimensional penalties, permits or other charges not directly related to the consumption of fuel" (11-037 l. 1229-1230). | The base rule exists at SEFL but in a publication not held; the base is not "net linehaul" at every carrier. |
| 11 | P14 Primary: no shipper-side TL price document | 19-027 `L3*42186*G*2377.08*FR*237708`, bill-to Seaboard Foods, mode TL. | OVERTURN of the KA. |
| 12 | P16: start dates by carrier | Home Depot §8 ¶I: 18 months "from the date of receipt of a shipment by the consignee" (23-005 l. 1260-1262); Saia 1030(7) "no later than 180 days from the date of original freight bill presentation" beside 1030(6) "date of the original bill" (13-056 l. 7800-7811); Dayton 407 d: "Overcharge claims in amounts of $3.00 or less per freight bill will not be accepted" (13-072 l. 529); R+L has no overcharge item (0 hits in 13-058), like SEFL; its l. 339 180-days-from-shipment rule is for refund-program discrepancies only (l. 325-340). | Contracts can lengthen the window; one tariff can carry two starts; a de-minimis floor exists. |
| 13 | P16/P17 and §4.4: NMFC 300320 as a clock for LTL carriers | 15-081 300300-A: "limited in their application to … motor carriers of household goods, motor carriers participating in the noncontiguous trade, and freight forwarders" (l. 1077-1084); 300500-A covers other carriers (l. 1214-1221). | Cite 300520 for ordinary LTL carriers. |
| 14 | P18: credit periods | Central "MAXIMUM CREDIT PERIOD = 30 DAYS" (13-073 l. 206); Dayton "fifteen (15) calendar days plus a grace period" (13-072 l. 372); TForce's 1.5% per month starts only on placement with collections (13-060 l. 2682-2684). | Not every carrier is 15 days from presentation. |
| 15 | P19: refund windows at SEFL 752 and XPO 200 | FedEx: full transportation charges refunded on a missed commitment if the debtor requests "within fifteen (15) calendar days of the date of the scheduled delivery commitment" (13-051 l. 2265-2269, 2340); SEFL 752 waives "all freight charges" and states no window (13-065 l. 2584-2586). | P19's refund amount and window are per carrier. |
| 16 | §4.2-§4.4: TForce defaults and refusals as general rules | Item 645-A scope: written density-based-rate agreement only (13-060 l. 2416-2418). | NARROW rows 12, 45, ledger 31. |
| 17 | §4.3: "conclusive documentary proof (ODFL 365, XPO 205)" | R+L 364 (13-058 l. 1180). | Add R+L. |
| 18 | §4.3: "no rule requires … a reason" / Part 378.4(d) repeated in tariffs | No tariff in set 13 contains the word "disallowance" (grep over all 28 files: 0), confirming explore_rules_2 l. 192 that XPO 23 and Saia 1030 copy 378.4(a)-(c),(e) without (d). Tariffs that incorporate Part 378 by reference: ODFL 396 (13-053 l. 1313), Saia 1030(7) "as the minimum requirements" (13-056 l. 7806-7808); contract: Walmart §7e (23-012 p. 78 render). | The "not grounds for disallowance" protection reaches a claimant through Part 378 itself or an incorporating tariff; no tariff states it. |

## 4. §5 versus the raw traces

P rows of `doc-exploration.md` (HEAD) §5.1-§5.6 against the walk agents' raw reports, and the §4 "exploration read" claims against `explore_rules_2.md`. "Caught?" says whether the validator's report noticed. Companies only.

### 4.1 §5 P rows against walk A (chains A, B), walk B (C, D), walk C (E, F)

| # | Chain, fact | Raw trace says | §5 says | Kind of difference | Caught? |
|---|---|---|---|---|---|
| 1 | A P01 | "T1090 Item 753 §5 p.89; bill p.46 'PREPAID' … primary: tariff + bill terms" | the same, "primary" | Both cite the item on who pays the residential charge; the payor-pricing item is SEFL 201 | No (KV); see §2.5 |
| 2 | A P02 | "p.12 (eff. 01/15/2021, acct 071-000559 Ft Lauderdale) … p.18 (04/12/2023, acct 071-003454 Miami Gardens)" | the three dates; only 071-003454 kept (in P01) | Dropped: the account number changes between versions | No |
| 3 | A P08 | "bill p.46 'QUOTE #CWEN3E465' — quote number only; quote document NOT REPORTED" | no P08 row; P08 absent from the chain's NOT REPORTED line | NOT REPORTED dropped | No |
| 4 | A P09 | "Liftgate DIRECT→PARTNERSHIP $55 … (DIRECT→DIRECT $30); … handwritten '30' annotations beside the liftgate rows" | "$55 minimum … no residential exception" | Detail dropped | Partly (validator noted the handwriting) |
| 5 | A P12 | "Item 110 p.5 … defines FSC on National Fuel Index; p.18 refers TL to '195 Fuel Surcharge Tariff' … NOT REPORTED as a table" | "Item 110" (and §2.1 lists SEFL 110 as "the fuel-base item") | A definition promoted to a base rule; the 195 pointer dropped | Partly (definition caught; 195 not) |
| 6 | A P16 / P17 | P16 "NOT REPORTED in held docs; statute 49 USC 14705 would apply"; P17 separate "NOT REPORTED" | one row "the statute governs" | Statute changed (14705 → the 13710 framing of §4.4); two rows merged | No (the doc's choice is the more apt statute) |
| 7 | A P19 / P20 / P21 | P19 "Items 752/752-1 exist; not read … n/a"; P20 "Item 890-100 … (eff. January 12th, 2026) residential liftgate limit 1,000 lb/piece; fallback, post-dated"; P21 "derived from the bill's own format" | no rows, and not in the NOT REPORTED line | Three facts dropped silently | Partly (validator's P20 ADD note mentions 890-100) |
| 8 | B P08 | "none claimed (no quote on BOL or bill)" | P08 in the NOT REPORTED list | n/a turned into NOT REPORTED | No |
| 9 | B P10 | "X26 Item 221 ($27.90 notification), Item 253 ($71.50 appointment …), Item 224 …; X18 Item 221 ($10.50)" | P10/P11 row shows Item 239 only | Accessorial prices dropped (the sibling's APT $51.90 is then "not checkable" without the 2018/2026 figures shown) | No |
| 10 | B P13 / P20 / P21 | P13 "RATE 284.22 … derived"; P20 "X26 Item 224 p.40, Item 202 p.29 … fallback"; P21 "derived" | no rows; NOT REPORTED line lists "P13's rate table" only | Two found facts dropped | No |
| 11 | B P16 / P17 | "X26 p.11 ¶9 / X18 p.10 ¶9" | "XPO 199 ¶9 (2018 and 2026)" | Item number missing (Item 7 ¶9) | Yes |
| 12 | C P04, P12 | P04 "derived 72.0%"; P12 "derived 17.5% on net" | rows say derived, but the NOT REPORTED line reads "every P fact but P01/P13/P21" | The doc's NOT REPORTED line contradicts its own table | No |
| 13 | C contrast, P21 | "discount on *rounded* gross: 2420.77×0.84 = 2033.45 ✓ (unrounded gives 2033.44)" | not kept | A rounding-order fact for P21 dropped | No |
| 14 | D P11 | "copy _b, revised 10/05/2026; copy _a, revised 11/03/2025, says $40.00" | "$45 in the 10/2026 revision, $40 in 11/2025" | Faithful compression | Validator wrongly called the dates unsourced (§2.5) |
| 15 | D P13, P21 | P13 "13289 = $132.89/cwt, class 85, tariff 559 … Not checkable"; P21 "rate printed without decimal (13289)" | kept in M rows; no P13/P21 row; "P13's table" NOT REPORTED | Moved to M rows | n/a |
| 16 | E P01 | "Derived: the 3PL is payor; whose pricing applies is never stated" | NOT REPORTED ("all P facts but P10/P16") | A derived payor turned into NOT REPORTED | No |
| 17 | E P08 | "n/a — No quote number on either BOL" | in "all P facts but P10/P16" | n/a turned into NOT REPORTED | No |
| 18 | E P19 | "NOT REPORTED — 'Est. Transit Days: 6 day(s)' / '5 day(s)' … is an estimate, not a guarantee" | in the NOT REPORTED sweep | Note dropped | No |
| 19 | F P15 | p. 20 quoted with colons (from the text layer) | the same colons | The image has semicolons | Yes |
| 20 | F P19 | "'$200 fee for early or late arrivals' … 'route delays without communication … will incur a service fee penalty' … Penalties on the carrier, not a refund to the shipper" | "$200 fee" placed under P15; no P19 row; P19 not in the NOT REPORTED line | Reclassified, and the "penalty on the carrier" reading dropped | No |
| 21 | F P16 / P17 | P16 "Carrier-side clock … Shipper-side window: NOT REPORTED"; P17 "Primary; delivered 02/24/2026 → 2026-04-10" | merged "carrier-side clocks; the shipper's window NOT REPORTED"; the date moved to D01 | Faithful | n/a |

No verdict in a P row was softened into a match, and no NOT REPORTED was turned into a finding. The pattern runs the other way: found or n/a facts (A P19-P21, B P13/P20/P21, C P04/P12, E P01/P08) were dropped or swept into NOT REPORTED lines, which makes §5.7's "NOT REPORTED in every chain" and "found only by fallback" lists slightly pessimistic for P facts.

### 4.2 §4 "exploration read" claims against `explore_rules_2.md`

| # | Claim | explore_rules_2 says | doc-exploration (HEAD) says | Caught? |
|---|---|---|---|---|
| 22 | Estes 992 ¶4 | l. 89 "weight can be reapportioned between items 'Upon submission of satisfactory proof'" (correct) | §3.1 and §4.3 use it as the rebuttal standard | Validator caught the misreading; the error entered at the doc stage, not with the agent |
| 23 | R+L 364 | l. 83 "30 days; $45.90" (no start date) | "from the bill date" | Caught; error entered at the doc stage |
| 24 | NMFC 401400-A | l. 95 "T15 `nmfc_100-AO_supplement1_2015.txt`, p. 23" (the right file) | ledger 45 "15-079 p. 23" | Caught; error entered at the doc stage |
| 25 | XPO 205 | l. 82 "XPO 205 (pp. 30-31) … 'conclusive documentary proof'; $52.70" (read in AK.3) | ledger 29 cites AK.1 for 205; §4.3/§4.4 apply the AK.3 wording | Partly (validator says AK.3 only; it is AK.2 and AK.3) |
| 26 | XPO 239 | l. 48 "XPO 239 §1 (AK.3 …, p. 49): $50.70" | §4.2 "$50.70"; validator verified it against AK.1's wording | No (AK.1 is $47.85) |
| 27 | TForce dimension default and refusal | l. 56-58 listed without the Item 645-A scope | the same, tagged *assumed* | No (validator retagged *verified* without the scope) |
| 28 | FedEx 360 ¶6 | l. 66 "no freight terms on the BOL means the shipment moves prepaid" | the same | Caught (Canada exception) |
| 29 | Part 378 and the tariffs | l. 192-194 "XPO 23 and Saia 1030 copy 378.4(a)-(c) and (e) but leave out (d) … no 'disallowance' wording in any tariff"; "Saia 1030(7) incorporates Part 378 'as the minimum'. ODFL 396 …"; "TForce 813 cites … Part 370 … looks like a mis-cite" | §4.3 states 378.4(d) without saying no tariff repeats it | No |
| 30 | Facts the agent found and the doc dropped | ABF 361 ¶1 (BOL rate or class notations "for information purposes" only); FedEx 360 ¶10 (pallet weight added when not listed); Estes 360 ¶6 $4.10 and ABF 360 ¶5; Estes 572 $15; Estes 993-10 $20; SEFL 645-11 ¶4; SEFL 435-10 ¶5 $30; ABF 362 ¶2 "satisfactory documentation"; ABF 993 $55; YRC F-154 "Brochures and 'sample' bills of lading will not be accepted"; Saia 840; Home Depot §8 ¶I (18 months) and ¶J (90 days after a short-pay) | none of these | No. This review re-opened five of them (Estes 993-10, SEFL 435-10, ABF 362 ¶2, Home Depot ¶I and ¶J): all as the agent wrote |

## 6. Privacy check

- **Patterns searched in the validator's report** (416 lines): phone numbers `[0-9]{3}[-.) ][0-9]{3}[-.][0-9]{4}` and `\(?[0-9]{3}\)? ?[0-9]{3}-[0-9]{4}`: 0 hits. Honorifics `Mr|Ms|Mrs|Dr` followed by a capital: 0. Bare 10-digit numbers: two, both carrier bill numbers (l. 282 an Estes PRO, l. 287 a Yellow PRO), not telephone numbers; the other digit runs are NMFC item ranges (l. 333, 411). E-mail addresses (`@`): 0.
- **Names seen on the pages rendered for this review** (signers on 23-012 p. 86, the shipper's signer on 21-002 p. 6, the payee named in the 21-002 p. 17 remark, the user IDs on 21-002 pp. 13-16, the contact named on 05-015 p. 1, the carrier employee named in 23-003 p. 5, the attention line on 02-002 p. 46): none occurs in the validator's report (case-insensitive search on each).
- **Result:** the validator's report is clean. Companies only appear (carriers, shippers, brokers, 3PLs, a payment agent). This review transcribes no individual's name, telephone number or e-mail address either; the same searches were run on this file before it was saved.

## 7. Concerns left unproven

1. **49 CFR Part 378: what the doc uses and what AX quotes.** AX §7 (l. 205) quotes 378.3(a) (a claim "shall not be paid unless filed in writing with the carrier that collected the transportation charges"), 378.3(b) (one claim for many shipments with "The same tariff issue or authority or circumstances"), 378.4(a)-(c), (e), and "Missing papers are 'not ... grounds for disallowance'; the carrier must ask (378.4(d), 378.5(c))". AX §6 (l. 192) gives 378.7 acknowledge "within 30 days", 378.8 "pay, decline to pay, or settle ... within 60 days", 378.3(a) forwarding within 15 days, 378.9(b) carrier-found overpayments refunded "within 30 days". The AX review (row 17, l. 108) re-fetched the eCFR version 2026-09-01 and confirmed every quote, adding 378.7's exception "except when the carrier shall have paid or declined in writing within that period" and 378.8's "except where the claimant and the carrier agree in writing to a specific extension" and "citing tariff authority". **The doc's uses match these quotations:** §4.3's 378.4(d)/378.5(c) sentence; §4.4's 30 days (378.7), 60 days extendable only in writing (378.8), 30-day self-found refund (378.9(b)), 15-day forwarding (378.3(a)); §4.5 ¶1's "the missing paper cannot be the reason the claim fails". Only 378.7's paid-or-declined exception is left out, which changes no clock. **Concern, unproven:** none of the quotations is 378.1 (applicability). The NMFC items that "conform to the regulations of the Federal Motor Carrier Safety Administration" are "limited in their application to … motor carriers of household goods, motor carriers participating in the noncontiguous trade, and freight forwarders" (15-081 300300-A, l. 1077-1084), and ordinary carriers are sent to the 300500-series (l. 1083-1084, 1214-1221). If Part 378 has the same scope, it does not bind SEFL, ABF or ODFL by itself; it reaches them where a tariff or contract incorporates it (ODFL 396, 13-053 l. 1313; Saia 1030(7), 13-056 l. 7806-7808; Walmart §7e, 23-012 p. 78; TForce 813 points to NMFC 300500, 13-060 l. 3587-3588), and otherwise NMFC 300520 applies to NMFC participants: 30-day acknowledgement, a 5-business-day request, 60 days to decide (l. 1252-1260), binding arbitration (300530), and **no "not grounds for disallowance" sentence**. No tariff in set 13 contains "disallowance". What would settle it: the eCFR text of 49 CFR 378.1 at the 2026-09-01 version. Until then, §4.3's and §4.5's reliance on 378.4(d) for ordinary LTL carriers is *assumed*.
2. **Whether a contract can lengthen or shorten the statutory 180 days** (Home Depot §8 ¶I 18 months; Walmart 12 months; Home Depot ¶A and SOW c 90 days; First Brands 180 days from service): a legal question no file answers.
3. **Whether SEFL participates in the NMFC** (so that 300520 is "the carrier's rules governing the handling of such claims" in 817 ¶6): Item 100 names NMF 100 as governing (13-065 l. 150-156), but no participant list is held.
4. **The ODFL revision stamps are dated after the PDFs were made.** 13-053 (CreationDate 2026-09-09) prints "Revised 10/05/2026" on 26 items; 13-052 (CreationDate 2025-10-16, ModDate 2026-09-10) prints stamps up to "Revised 07/22/2026". Advance publication would explain it; no file says so. It does not change the fee readings ($40 / $45).
5. **19-027's role.** The 204's bill-to is a food producer and the sender ID is its TMS ("MGSEABOARD"); that makes it a shipper's tender, but no invoice for load 4085753 is held, so the price on the tender cannot be matched to a bill.
6. **19-031 is "partly real"** in the catalogue without saying which segments; the Roadway counter-examples (L7 tariff, L1 percent with AV) carry that caveat.
7. **Quote documents.** The Central v. Amazon depositions (09-046 to 09-049) talk about a spot-quote rider and spot-quote applications; only searched, not read in full. A rider exhibit elsewhere in that docket would test P08.
8. **TForce defaults outside density agreements.** No other TForce item seen sets a default dimension; a full read of Item 630 (cube determination) was not done.
9. **The carrier's response deadlines (G2) have no P row** (§2.2): whether that is a gap in §1 is for the completeness review (BC).
10. **The validator's own list, still open:** Wayback availability for 2023-24 fuel pages (items 2); broker terms only in AM (3); whether a tariff may start the shipper's clock before receipt of the bill (4); FedEx 438's "Any action or proceeding" wording (5); P14's shipper-issued rate confirmation (8, narrowed by 19-027); ABF 111-AR not held (10); the handwritten "30" on 02-002 p. 22 (11). Closed here: items 7 (TQL, KCH, Coyote re-opened), 9 (AK.2 opened: the proof wording is there), 12 (EIA re-read: 3.768 on 2024-07-29).

