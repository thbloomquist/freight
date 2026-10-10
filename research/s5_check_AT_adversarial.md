# Check AT · Adversarial review of the document dataset (2026-10-09)

**What this is.** The verification pass on `data/` for `s5_check_AT_c09_document_dataset.md`: every catalogue row checked against the file (content checks on the real-document sets; identity checks on guides, tariffs and forms where the sub-agents were cut off), the worked dispute example transcribed and recomputed independently, the files no earlier check had read described, OCR accuracy measured, unknown URLs resolved, privacy spot-checked. Written by the verification agent; the coordinator merged its sub-agents' notes (appended below) and applied the verdicts to `data/catalogue.csv` (`verify_status`, `verify_note`, and the structured corrections to `doc_types`, `discrepancy_checks`, `carriers`, `mode` and dates). Nothing under `data/sources/` was changed.

**Result:** 271 rows: **verified 145, narrowed 123, wrong 3** (two DOJ exhibits are tender lists, not reweigh data; GSA 1000-D is a rate table, not a rules tariff). The worked example's arithmetic and agreement reading held; **its timing claim did not** (§2.3) and the AT file's §7 was rewritten on this review. After corrections, 188 real files; checks F2 and F4 have no real evidence, E1 one file, B9 three.

---

# Verification report, dataset check AT (2026-10-09)

Scope and method. Deliverables: `verify_rows.csv` (271 rows, one per catalogue row) and this report. Rows for sets 07, 08 (tag A2), 09 (A3) and 12-18, 20 (A7) come from three sub-agents whose runs completed before the rate limit; their notes are in `parts/notes_A2.md` and `parts/notes_A7.md` (A3 left only its CSV). Every other row is mine (tag COORD in `parts/verify_rows_COORD.csv`). Labels: *verified* = I (or the named sub-agent) opened the page; *assumed* otherwise. The data folder was not modified; everything written sits under `scratchpad/verify/`.

**Row verdicts (271): verified 145, narrowed 123, wrong 3** (07-020, 07-021 are SDDC tender lists with no reweigh data; 13-070 "gsa_1000-D" is a 5-page baseline-rate table, not a rules tariff). Depth: full check (first, middle, last page plus the pages needed for each discrepancy check) on sets 02, 07, 08, 09, 19, 21, 22, 23, 24; first-page identity only on sets 01, 03-06, 10, 11, 12-18, 20 (the coordinator's reduced scope after the rate limit; set 04 pages 9, 21, 42, 53, 93 of the Delphi exhibits were also opened for the OCR test).

Systematic faults found across the catalogue:
1. Discrepancy checks were often listed as "checkable" rather than evidenced: statements of account carry `A2|F1` (21-003, 21-007..010, 24-001, 24-005, 24-008) with no duplicate or late fee visible; rate-con terms that merely *mention* detention, lumper or TONU were counted as D3/D7/D5 evidence (22-009..014); `E2` was put on cargo-claim packets (21-012, 23-010). After corrections `F2` and `F4` have no real evidence, `E1` has one file (21-001), `B9` three.
2. Dates were sometimes the filing date, not the shipment dates (07-017, 07-023, 22-014, 23-012, 24-004), and set 19 uses long labels instead of bare IDs in `discrepancy_checks`.
3. `doc_types`: "complaint" on answers, motions, exhibits and docket sheets (07-018..021, 08-025..027, 21-001); "invoice_ltl" on statements without line items; "audit_worksheet" on nVision claim presentations (23-006..008); "carrier_response" where only a quoted message exists (23-002).
4. Three attribution problems: 12-046 never names XPO/Con-way; 14-075 never names FedEx; 15-083 certifies CS900, not "CSN210". 12-043 and 12-051 are the same document.
5. Mode is asserted where the document never says it (08-028, 08-029, 24-009).

## Task 2. The worked example, re-done independently

Source: `sources/02_exist_v_sefl/gov.uscourts.flsd.704429.1.2_3.pdf` (224 pp). All pages carry an OCR text layer; I read the three bills from 200-dpi renders and the agreement from the text layer plus a 200-dpi render of p. 19.

### 2.1 Transcriptions (*verified*, pages viewed)

**Bill 806625953 (p. 28, "PAST DUE INVOICE")** — shipper EXIST INC, 1722 NW 215th St, Miami Gardens FL 33056; consignee I LOVE DULUTH, 345 Canal Park Drive, Duluth MN 55802 (CSD/FTL terminal codes). Lines: `1 PLT 9 BOXES OF APPAREL CL150 NMFC 49880- | CLASS 70.0 | 405 lb | rate 31597 | 1279.68` ; `3 PLT 45 BOXES OF APPAREL & CL125 NMFC 49880- | CLASS 70.0 | 2315 | 31597 | 7314.71` ; GROSS FRT CHG 8594.39 ; 90.30% DISC 7760.73 ; NET FRT CHG 833.66 ; LIFTGATE SVC 55.00 ; LTL FUEL SURCHARGE OF 24.00% 200.08 ; TOTAL 4 pcs 2720 lb 1088.74 ; QUOTE #CWDV2BGFC ; packing slip 223530, shipper order 143340 ; PREPAID 2720 1088.74. Footer: SHIPMENT DATE 04/19/2023 ; PAYMENT DUE DATE 09/10/2025 ; SHIPPER B/L 43142300 ; DATE BILLED 08/26/2025 ; CUSTOMER 071-003454 ; PAY THIS AMOUNT: INVOICE PENDING ; SEFL 62317109 DAFG. No reweigh, W&I or inspection note.

**Same bill at p. 41 ("BALANCE DUE INVOICE")** — identical lines and total 1088.74, but PAY THIS AMOUNT **110.23**, DATE BILLED **05/05/2023**, due 05/20/2023.

**Bill 807148067 (p. 33)** — consignee ESTELE, 67905 Cloverdale, Sisters OR 97759 (ATB). `1 PLT APPAREL IT-49880 STC 16 BX | CLASS 70.0 | 509 | 60080 | 3058.07` ; GROSS 3058.07 ; 88.15% DISC 2695.69 ; NET 362.38 ; LIFTGATE SVC 55.00 ; PVT RESIDEN 94.00 ; LTL FUEL SURCHARGE OF 22.00% 79.72 ; note `** PER GOOGLE EARTH THIS IS A PRA[IVATE] DLVY` ; TOTAL 509 lb 591.10 ; SO# 143695 | PL# 224629 ; *LIFTGATE DELIVERY ; QUOTE #CWEN3E465 ; shipment 05/15/2023 ; due 09/10/2025 ; B/L 51124115 ; billed 08/26/2025 ; customer 071-003454 ; SEFL 34844332 OAKH. **p. 46 (balance-due version):** same lines, PAY THIS AMOUNT **94.00**, billed **06/19/2023**, due 07/04/2023.

**Bill 807307041 (p. 35)** — consignee THE SAND BOX, 8437 West Silver Lake Rd, Silver Lake MI 49436 (CSD). `1 PLT 15 BOXES OF APPAREL IT-49880-4 CL-175 | CLASS 70.0 | 525 | 30081 | 1579.25` ; `1 PLT 9 BOXES OF APPAREL & IT-49880-5 CL-125 | CLASS 70.0 | 385 | 30081 | 1158.12` ; AS WEIGHT 1000 ; DEFICIT 90 | 30081 | 270.73 ; GROSS 3008.10 ; 90.30% DISC 2716.31 ; NET 291.79 ; LIFTGATE SVC 55.00 ; REDELIVERY 80.00 ; LTL FUEL SURCHARGE OF 21.50% 62.73 ; LOA IMAGED ; ORIG DEL ATTEMPT: 05/25/2023 ; `** CLASS INSPECTION PER W&I **` ; TOTAL 2 pcs 910 lb 489.52 ; 24 BXS TOTAL ; SO# 141409 | PL# 225024 ; QUOTE #CWEY44EC6 ; shipment 05/22/2023 ; due 09/10/2025 ; B/L 51170641 ; billed 08/26/2025 ; SEFL 62337078 DAFG. **p. 48 (balance-due version):** PAY THIS AMOUNT **23.28**, billed **06/22/2023**, due 07/07/2023.

**Agreement, version effective 04/12/2023 (pp. 18-20, rating item 000-068386, account 071-003454):** p. 19 (render viewed): `MWPC OUTBOUND PPD/COL  SEFL-0550  01/10/22  Item 610  90.30  70  77.5 THRU 175  ALL` ; `MWPC INBOUND COL ... 81.10 70 77.5 THRU 125` ; `NEPC OUTBOUND ... 87.45` (the text layer's "87.5" is an OCR error) ; `SWPC OUTBOUND ... 86.35` ; `WCPC OUTBOUND PPD/COL  SEFL-0550  01/10/22  Item 610  88.15  70  77.5 THRU 175  ALL` ; `WCPC INBOUND COL ... 81.10`. Each: "Apply FAK exception class 70.0 on commodities described in NMFC class 077.5 thru 175.0. All other commodities apply actual class." p. 20, ITEM 610 MINIMUM CHARGE APPLICATION: "the applicable minimum charge from or to the following locations shall be THE ABSOLUTE MINIMUM CHARGE AFTER APPLICATION OF DISCOUNT": CNPC $197.00-$364.50 by province; **MWPC (IA, IL, IN, KS, MI, MN, MO, ND, NE, OH, SD, WI) $127.50**; NEPC $130.50; SWPC (NM) $122.50; **WCPC: CO $161.00; AZ, CA, ID, MT, NV, OR, UT, WA, WY $152.00**; "all shipments are subject to SEFL 1090 Rules Tariff". p. 18 also shows the direct-state per-pallet rates (AL..VA, FL intrastate) and the SEFL direct discount 81.00. **p. 22 accessorial exceptions (eff. 4/7/2021):** LIFTGATE SERVICE direct-to-partnership $55 min charge, partnership-to-direct $55, direct-to-direct $30; LIMITED ACCESS $50/$50/$25; INSIDE DELIVERY $25; NOTIFICATION $0 direct, $7.50 partner; RECONSIGNMENT $30; **REDELIVERY $80 min charge (all points, both directions)**; redelivery dock pickup $60/$80. Residential is not in the exceptions (so SEFL 1090 Item 753 applies: $7.60/cwt, $94.00 minimum, per the 1090 text dump, line 2695).

**Worksheet (2023 sheet pp. 199-211; spill column OVER CHG pp. 212-224):** columns CUSTOMER, INV, DATE, PLT, LIFTGATE, SURCHARGE, FRT CHARGE, NEED TO BE CHG. Row 292 (p. 208): `I Love Duluth 806625953 4/19/2023 4 $55.00 $178.74 $744.77 $510.00`, OVER CHG (p. 221) **$234.77**. Row 398 (p. 211): `The Sand Box 807307041 5/22/2023 2 $55.00 $72.77 $338.47 $255.00`, OVER CHG (p. 224) **$83.47**. Bill 807148067 is **row 364** (p. 210): `Estele 807148067 5/15/2023 1 $55.00 $79.72 $362.38 $152.00`, OVER CHG (p. 223) **$210.38**. Row 66 (p. 201) is a different bill: `Island Republic - Bluffton 804996172 1/30/2023 2 $30.00 $53.22 $183.50 $173.00`, OVER CHG (p. 214) $10.50. Sheet totals: 2021 $131,987.80 (p. 157), 2022 $109,577.87 (p. 198), 2023 $30,263.03 (p. 224); sum $271,828.70 = the complaint's claim (p. 7 para 10).

### 2.2 Arithmetic (python3 -I; `[our calc]`)
- 806625953: 405×3.1597 = 1279.68; 2315×3.1597 = 7314.71; sum 8594.39; ×0.9030 = 7760.73; net 833.66; fuel 24% of net = 200.08; total 833.66+55+200.08 = 1088.74. All printed figures reproduce.
- Shipper's record (row 292): 744.77 + 55 + 178.74 = **978.51**; 178.74 = 24.0% of 744.77, so the fuel rate did not change. Implied gross 744.77/0.097 = 7678.04; at $315.97/cwt that is **2,430.0 lb**. Re-rated weight 2,720 lb. Net difference 88.89 + fuel difference 21.34 = **110.23 = the PAY THIS AMOUNT on p. 41** (1088.74 − 978.51 = 110.23). Increase 11.3%.
- Shipper's "NEED TO BE CHG" 510.00 = 4 pallets × $127.50 (MWPC Item 610 minimum); OVER CHG 744.77 − 510.00 = 234.77 (reproduces). Row 364: 1 × 152.00 (WCPC, OR), 362.38 − 152.00 = 210.38. Row 398: 2 × 127.50 = 255.00, 338.47 − 255.00 = 83.47. Row 323 (806954124, MD = NEPC): 4 × 130.50 = 522.00 (matches p. 209). The reading that NEED TO BE CHG = pallets × the partner-zone Item 610 minimum (and, on direct lanes, the per-pallet rates) holds on every row tested; Item 610 is a per-shipment floor, so the worksheet's partner-lane "overcharges" rest on a misreading (*our reading*, the shipper's reasoning is not stated anywhere in the file).
- 807148067: 509×6.008 = 3058.07; ×0.8815 = 2695.69; net 362.38; fuel 22% = 79.72; total with liftgate 55 and residential 94 = 591.10. Without the residential line 497.10; **balance due on p. 46 = 94.00**, i.e. the June 2023 balance-due bill added exactly the residential charge (SEFL 1090 Item 753 minimum $94.00) on the strength of a Google Earth look.
- 807307041: 525×3.0081 = 1579.25; 385×3.0081 = 1158.12; deficit 90×3.0081 = 270.73; gross 3008.10; ×0.903 = 2716.31; net 291.79; fuel 21.5% = 62.73; total 291.79+55+80+62.73 = 489.52. Shipper's record 338.47+55+72.77 = 466.24 (fuel 21.5% of 338.47 = 72.77); **balance due p. 48 = 23.28 = 489.52 − 466.24.** The W&I inspection *lowered* net freight (338.47 → 291.79) and the $80 redelivery was added.
- 180-day clocks (49 U.S.C. 13710(a)(3)): shipment 2023-04-19 + 180 = 2023-10-16; balance-due bill 2023-05-05 + 180 = **2023-11-01**; past-due reprint 2025-08-26 + 180 = 2026-02-22. Complaint e-filed 2025-10-07 is 902 days after shipment, 886 days (29.1 months) after the balance-due bill, 706 days (23.2 months) after that bill's 180-day window closed, and 42 days after the reprint. For 807148067: bill 2023-06-19 → window 2023-12-16; for 807307041: 2023-06-22 → 2023-12-19.

### 2.3 Differences from the draft (`_worked_example_notes_DRAFT.md`)
1. **The timing claim is wrong.** The draft reads p. 28 as "a 2025 re-bill at a higher weight ... ~22 months after the carrier's own 180-day window". p. 41 shows the same bill, same 2,720 lb and $1,088.74, as a BALANCE DUE INVOICE dated **05/05/2023** for $110.23, sixteen days after shipment and inside any window. The 08/26/2025 document is a PAST DUE reprint ("INVOICE PENDING", payment due 09/10/2025) of a 2023 bill whose $110.23 balance was never paid, printed six weeks before the suit. The G2 "carrier billed late" reading collapses; what survives is A4 (balance-due bill the shipper never matched to the original) and C1 (weight raised 2,430 → 2,720 lb with no W&I note on either print).
2. The draft says "the original invoice image is NOT in the exhibit". The original is still absent, but the 2023 balance-due print (p. 41) *is* in the exhibit and gives the carrier's own date and amount for the re-rating; the draft never mentions pp. 36-48.
3. The draft says pp. 23-97 are "all printed as PAST DUE INVOICE with DATE BILLED 08/26/2025". **Only pp. 23-35 (13 bills) are.** pp. 36-48 are the same 13 bills as 2023 BALANCE DUE INVOICE prints; pp. 49-62 are 14 bills from March-May 2020 in an older layout (account 071-000559, Ft Lauderdale); pp. 63-97 are 35 CORRECTED INVOICE / BALANCE DUE INVOICE prints dated 2022-2023. 59 distinct bill numbers, not "~75 bills".
4. The "true negative" 807148067 is not a no-flag control: the shipper flags it for $210.38 (row 364), and the carrier added the $94 residential charge on a balance-due bill (p. 46). The draft's row number "66" is wrong (row 66 is bill 804996172); "row 82" for 806954124 is also wrong (it is row 323, p. 209, OVER CHG $117.86 on p. 222).
5. Minor: original gross 744.77/0.097 = 7,678.04 (draft 7,677.0) → 2,430.0 lb (draft 2,429.7). Complaint date: the draft hedges "11/10/2025 per e-file stamp; AC says 10/07/2025". Settled: p. 1 is the **summons**, e-filed 11/10/2025; the complaint (p. 5) is e-filed **10/07/2025 07:44:05 PM** (Filing # 233156835) and its cover sheet (p. 4) is signed 10/07/2025; case 2025-019705-CA-01, Miami-Dade circuit court; removed to S.D. Fla. and docketed 01/06/2026.
6. The draft's agreement reading (90.30 MWPC, 88.15 WCPC, FAK 70 for 77.5-175, Item 610 floors $127.50/$152.00, liftgate $55 partner, redelivery $80, residential $94 via 1090 Item 753) is confirmed page by page. Its arithmetic on the three bills is confirmed. Its reading of "NEED TO BE CHG" = pallets × Item 610 minimum holds (five rows tested).

### 2.4 Verdict on "best example", and better candidates
The 806625953 story still works as a C1 + A4 example (weight re-rated upward without an inspection note, on a balance-due bill the shipper did not reconcile), but **not** as a 180-day/G2 example, and the text in the draft and the README must change. Candidates that are clearer, each a single clause with the carrier's own reason printed on the bill:
- **807148067 (pp. 33/46, row 364):** one added line, PVT RESIDEN $94.00, reason printed ("PER GOOGLE EARTH THIS IS A PRA DLVY"), issued 35 days after shipment as a $94.00 balance-due bill. The check is D2 (was residential delivery ordered on the BOL?) against SEFL 1090 Item 753's $94 minimum. The shipper's worksheet does not even flag this $94; it flags the base freight instead. Recommended as the primary example: one line, one tariff item, one document (the BOL) decides it.
- **806445173 (pp. 25/38, row 269) and 806373725 (pp. 24/37) and 806446820 (pp. 26/39):** cubic-capacity re-rates. The bills print the clause: `T 1090C 610-100 864.81 CF 5.36 PCF AW 4635 CW 5188.8 / MIN FRT CHG 1738.16` (p. 38; density 5.36 lb/ft³ → charged weight 5,188.8 lb against 4,656 actual) and `APPLY SEFL 1090-B ITEM 610-100 816.54CF/5.41PCF AW=4420 CW=4899 / MIN FRT CHG 2014.40` (p. 26). SEFL 1090 Item 610-100 is "Minimum Charge – Cubic Capacity and Density-Eligible Shipments" (set 13, 13-065, line 1229 of the text dump). The balance due on p. 38 is $1,050.60 against the shipper's record of $1,159.72 (row 269: 890.90 + 213.82 + 55). This is a B3 example with the rule cited on the bill; the open question is only the cube measurement.
- **The 2020 bill at p. 49 (882437984):** `***** PENALTY/TARIFF DUE ***** $161.89`, hand-posted "POSTED", shipment 3/11/2020, PAY THIS AMOUNT $809.44, discount percentage 91.00 printed as "9100" — the only F1 (late-payment penalty) specimen in the set, and a bill that predates the earliest agreement version attached (01/15/2021), a B1 gap.

**Discounts on pp. 24-26 and 37-39 (settled by viewing):** these are the same three bills printed twice (2025 past-due reprint, then the 2023 balance-due print): 806373725 to S. Lake Tahoe CA (WCPC) `Discount Percentage % 88.15`, Gross Charge $43,908.66, Discount Amount $38,705.48, MIN FRT CHG $5,203.18 + liftgate 55 + arrival notice 7.50 + CA surcharge 8.00 + fuel 24% 1,248.76 = total 6,522.44; 806445173 to Traverse City MI (MWPC) `90.30`, gross 17,919.17, discount 16,181.01, MIN FRT CHG 1,738.16, total 2,210.32, balance due 1,050.60 (p. 38); 806446820 to Arnolds Park IA (MWPC) `90.30`, gross 20,767.00, discount 18,752.60, MIN FRT CHG 2,014.40, total 2,552.86. The OCR strings "3870", "1618", "1875" are the Discount Amounts (38,705.48, 16,181.01, 18,752.60) truncated; "3370" matches nothing printed (probably 806373725's bill number fragment). All three carry customer number **071-003454, the same account** as the other 2023 bills; they are class-150 shipments re-rated under the cubic-capacity minimum.

**Does every bill on pp. 23-97 carry DATE BILLED 08/26/2025?** No. Only pp. 23-35. See item 3 above.

### 2.5 Reading of the catalogue row 02-002
Narrowed: doc_types add `accessorial_schedule` (p. 22) and `corrected_invoice` (pp. 36-48, 63-97); checks become A1|A4|B1|B2|B3|B4|C1|D1|F1|G1 (A2 is only an allegation, p. 6; G1 rests on the dates, no window text); notes replaced as in `verify_rows.csv`.

## Task 3. Unread files described
- **07-020 (Doc 72-2, 62 pp)** and **07-021 (Doc 72-4, 14 pp)**: Exhibits B and D to the U.S. complaint in intervention: four-column SDDC tender lists (Tender Number, Supplement, Effective Date, Expiration Date), Roadway 9/23/2005-12/31/2013 (about 2,650 rows) and YRC 3/1/2005-11/30/2012 (about 500 rows). No reweigh data, worksheets, invoices, dollars or counts. Both rows were marked `wrong`. The only reweigh figures in set 07 are in Doc 72 itself (p. 18: 42 negative vs 75,324 positive corrections out of more than 1.5M invoices, 13 Nov 2006-20 Jan 2007; p. 21: over 13,000 negative-reweigh false claims June 2010-Oct 2012, about 725 a month, about 70,000 extrapolated) and in Exhibit A (72-1, 200 example shipments with actual vs billed weight). (A2, *verified*.)
- **09-031 (ilnd.227745 Doc 1, 12 pp, scan)**: Estes collection complaint filed 2009-01-23; Ex. A (pp. 6-7) a pricing agreement (account 6085222, eff. 2008-02-27, 75% discount, class exceptions CL85 for CL100, CL150 for CL250); Ex. B (pp. 9-12) a **statement of account**, per invoice: date, number, original amount, "discount added back", late fee, collection fee, balance; totals 101,848.57 / 173,595.95 / 10,591.91 / 82,633.36 = $368,669.79 claimed; bill dates 2007-10-26 to 2008-03-06. **No line-item freight bills attached.** (A3, *verified*.)
- **09-034 (deb.190462 Doc 5072, 8 pp)**: Omni Logistics' motion for allowance and payment of an administrative expense of $74,550 (p. 3 twice says $74,500) for about 200 shipments it arranged for Yellow in Oct-Dec 2023; the debtor argued the invoices were time-barred under 13710(a)(3) (pp. 6-7). **No invoices attached** (they are Exhibit A to a separate declaration). The A3 label does not fit; G1/G2 do. (A3, *verified*.)
- **08-028 Mafcote v. Estes (W.D. Ky. 3:07-CV-419-S, Memorandum Opinion, March 5, 2010, 8 pp)**: Estes's rules tariff (EXLA 105-L, Item 490) binds the shipper through its own bills of lading and bars consequential damages for late delivery, and the Carmack Amendment does not reach the customers' late fees, so Estes wins summary judgment on the shipper's claims. On Estes's $226,450.29 counterclaim it recovers only the discounted freight charges: the discount removals, 30% collection fee and interest are barred because the parties' Agreement for Transportation says no penalties, loss of discount or interest will be assessed, and tariff Item 163 yields to a written agreement. (A2, *verified*.)
- **23-006/007/008 yrc_nvision_***: each is a Form 410 claim plus (p. 4) nVision Global's "PRESENTATION OF OVERCHARGE CLAIM" filed on behalf of a shipper (CPI Satcom & Antenna Technologies $612.77; Yazaki $293.30; ZF North America $495.54) and (p. 5) a printout of YRC's web page "Overcharge Claims Status — Results of Inquiry": Assigned Claim Number, Date Received, Claimant Number, Claim Amount, Draft Number, Draft Amount, Draft Date, and the sentence "This claim is in APPROVED status. This claim has been approved for disbursement on one or more shipments associated with the claim. A detailed report of our audit of this claim was sent to the claimant on [date]". Who approved: YRC's overcharge-claims unit (no person named); the claim was audited and submitted by a named nVision auditor (not transcribed). 11113: pro 689201498 paid 09/20/2022 and paid again under 6892014980 ("keying error resulted in duplicate payment"), received 03/28/23, draft 1385879 for $612.77 dated 06/20/23 — approved and drafted, yet still claimed in bankruptcy. 11117 and 11202: draft number 0, no draft date — approved but unpaid. These are **duplicate-payment refunds (A2)**, not rate disputes (B2); the "audit_worksheet" label should go. (*verified* for 11113 p. 4-5; 11117/11202 reason from the OCR keyword "duplicate", *assumed*.)
- **23-004 yrc_globaltranz_16595 (8 pp)**: $382.08 dispute of a YRC reweigh on pro 6703485626 (shipment 07/03/2023, household goods of a service member, no spec sheets). p. 8 is a **shipper-side** certificate: "WHITNEY TRANSFER & STORAGE", location of scale 505 N. 14th E., Mountain Home ID, date 30-Jun-23, two wood crates 84×45×87 in, cubic feet 380.63, tare 636, gross 2,153, **net 1,517 lb**, density 3.99, "WEIGHED ON CERTIFIED SCALE", signed by a weigh master. It supports the shipper (not the carrier): the carrier's reweigh figure is not in the file. (*verified*, p. 8 viewed; the page names the goods' owner, an individual.)
- **23-011 yrc_unishippers_17062**: p. 4 Unishippers overcharge claim form of 02/20/2023, "PLEASE CREDIT THE REWEIGH FEE", $276.37 of $864.92 paid 01/25/2023 on pro 6898764131; the "SPECS SHEET" said to be attached is not in the 4-page file, so there is no weight certificate (row narrowed). (*verified*.)
- **21-002 winndixie (18 pp, scan)**: a Winn-Dixie vendor's (Clamp Swing Pricing Co.) amended claim. Original BOL p. 6 (ODFL pro 02902161435, 12/3/2004, prepaid); the error: the BOL was made out prepaid then changed, so Winn-Dixie paid the freight ($2,412.67) and charged it back to the vendor by debit memo (p. 8, 01/26/2005); ODFL then refunded Winn-Dixie in two "OVERPAYMENT REFUND" postings, $1,828.04 (2/15/05, p. 14) and $584.63 (2/26/05, p. 16), and re-billed the vendor $1,133.55 (e-mail p. 11); **the corrected (re-issued) bill is p. 17** (invoice date 02/18/05, PREPAID, 985 lb class 92.5). The erroneous original bill's image is not in the file. Remittance p. 9, Winn-Dixie statement p. 10, ODFL A/R history pp. 13-16, e-mails pp. 11, 18, letters pp. 1, 3-4, 7. Checks: A5 and A4; not B4 or C2. (*verified* from OCR of all 18 pages.)
- **21-001 paperpak_odfl 10.0 (45 pp)**: Doc 10 is ODFL's **answer and counterclaim** (pp. 1-6, 06/30/2008), not the complaint (which is 09-035). p. 7 ODFL statement of account (19 pros 3/30/07-1/25/08, $8,648.09 billed, $7,497.51 open). pp. 8-45: the 19 bills, each printed twice (original and "CUSTOMER COPY"). Annotations are printed rate-clerk notes, not handwriting: p. 11 (bill 81470114653) "Rate Clerk: RKE / WIW / SORTING OR SEGREGATING / FBA DHE 8/08/07 FREIGHT BILL AUDIT / ADDED SSC PER DR / CAB SRS 11/02/07 CORRECT AS BILLED / ODFL 6100 ITEM 158508 WITH ODFL 660 / SPEED SERVICE GUARANTEED ODFL 100 / ITEM 887 SORT AND SEGREGATE CHARGE PER" with $45.00; p. 22 (13300695197) "NMFC #149020 / FUEL INCREASE / C/ADDITIONAL REDUCTION, ALLOWANCE OR ADJUSTMENT MAY APPLY / WIW / DISCOUNT ALLOWED 70.00% 434.39", total 240.91; p. 33 (13300695254) "HANDLING UNITS: 6 UNITS OF TYPE SKID / ULTRA ZAP 4X7 / FUEL INCREASE / Rate Clerk: RKE / RATED AS- DEFICIT WEIGHT 130 lb at 5,000 / DISCOUNT ALLOWED 70.00% 1611.76". Other pages were read only through OCR keyword hits (discount on pp. 22, 33; guarantee on p. 11). (*verified* for pp. 1-7, 11, 22, 33.)
- **22-013 stg_werner_10053 (28 pp)**: Werner Enterprises' claim ($14,300) against Best Dedicated Solutions (an STG Logistics broker). One packet, load **963813**: rate confirmation p. 14 (02/12/2025, 53' van, Distance 971.84 miles, BOL 504846313, PO IDB62135, Laredo TX → St Joseph MO, appointment 16:00) with fees p. 15 `Net Freight Charges USD 2,100.00 / Total Cost USD 2,100.00`; Werner invoice WLM98113988 p. 13 (invoice 04-25-2025, pickup 02-14-2025, delivery 02-17-2025, BOL 504846313 | PO IDB62135, `LINEHAUL 40,000 lb 1.00 FLT 2,100.000 = 2,100.00`, Total 2,100.00 USD, Miles column blank). **Rate con = invoice.** The BOL p. 19 (ship 2/19/2025, 1,768 pcs, 17 pallets, 43,826 lb) belongs to the next load, 965527 (p. 20); p. 28 BOL (3/6/2025, 1,008 pcs, 14 pallets, 42,388 lb) goes with invoice WLM106881310 (p. 27). Accessorials: **TONU** on invoices p. 17 (WLM61249654, 10-24-2024, `TRUCK ORDERED NOT USED 150.00`) and p. 23 (WLM101611198, 02-27-2025, 150.00) with the matching rate con p. 25 `TONU Fixed Cost 1.00 × USD 150.00`. No detention, lumper, layover or stop-off line anywhere in 10053 or 10102; those words appear only in the rate-con boilerplate (pp. 6, 10, 15, 21, 25) and the quick-pay fee sheets (pp. 7, 11, 16, 22, 26: 2-10% early-pay fees). (*verified* from the text layer and OCR.)

## Task 4. OCR quality (tesseract 5, --psm 6, 200 dpi grey)
SEFL bills (set 02, 10 pages chosen with a seeded random sample: 33, 35, 40, 47, 48, 52, 65, 82, 91, 96). Ground truth read from the renders. TOTAL / PAY-THIS-AMOUNT amounts: p33 591.10/591.10 ✓✓; p35 489.52/489.52 ✓✓; p40 656.90 ✓, 26.98 read as **25.98** ✗; p47 503.02/37.86 ✓✓; p48 489.52/23.28 ✓✓; p52 (2020 layout, hand annotations, no "TOTAL" label): both amounts missed ✗✗; p65 218.63/30.00 ✓✓; p82 646.46/76.16 ✓✓; p91 1669.78/196.84 ✓✓; p96 483.25/483.25 ✓✓. **17 of 20 amounts right (85%)**; on the modern layout 17/18 (94%). Weights were worse (1775 → "4775", 710 → "71"). The embedded Intelligent Capture text layer read all 18 modern-layout amounts right but also mangled weights.
Delphi/UPS Freight bills (set 04, 5 pages: 20040.2 pp. 9, 42, 93; 20040.3 pp. 21, 53). Net Amount Due: 181.32 ✓, 3,460 (certificate total) read "3.460" ≈, 340.87 ✓, 106.81 ✓, 108.39 ✓ → **5/5 totals**; but line amounts had 3 errors in about 17 (391.57 → 391.87; reweigh fee 18.00 → 16.00; 1,730 → 4,730). Lesson for the prototype: totals on clean 1990s-2020s carrier layouts are reliable; line items, weights and anything hand-annotated need a second read (text layer, or re-OCR of the amount column at higher resolution), and the old SEFL 2020 layout without a TOTAL label needs a template.

## Task 5. The 7 UNRESOLVED URLs
WebSearch was unavailable (session limit) and DuckDuckGo/Bing via WebFetch returned challenge pages or junk, so resolution relied on the PDFs' own metadata and curl HEAD with the generic UA (HEAD calibrated against four known-good catalogue URLs, all 200).
- 08-028 mafcote: **https://www.govinfo.gov/content/pkg/USCOURTS-kywd-3_07-cv-00419/pdf/USCOURTS-kywd-3_07-cv-00419-0.pdf** (HEAD 200, application/pdf; the file's metadata is a chambers WordPerfect export of 2010-03-05, consistent with GovInfo). Not downloaded, so identity with the local file is *assumed*.
- 13-062 XPO CNWY 199-AK.2: **https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.2_Eff._05.18.2026.pdf** (HEAD 200, application/pdf; same pattern as 13-061/13-063).
- 13-054 Saia 170-D (2019-02-18): not found (saia.com guesses return HTML).
- 13-064 XPO CNWY 199-AB-4 (2018): not found (404 on the current CDN pattern).
- 15-076 ODFL BOL guide: not found (metadata title "ODFL Bill of Lading BOL Guide", InDesign 2023-12-14; odfl.com DAM guesses 404).
- 15-080 NMFC 100-AR Supplement 4: not found (hubspot pattern of 15-079 returns 404).
- 16-090 NCWM letter 2024-01-03: not found (cdn.ncwm.com guesses 403; the NCWM 2024 Interim/Annual "LR Supporting Files" folder is the likely home).

## Task 6. Privacy spot-check
grep of `catalogue.csv`, `README.md`, `leads_tried.csv` and all 24 `sources/*/source.md`: no e-mail addresses, no phone numbers, no bank or account numbers (the long digit runs in rows 19-024/025/026/027 and `19_edi_samples_real/source.md` are EDI interchange control and load numbers). One class of hit: the relator's surname in the public case caption "U.S. ex rel. Hannum v. Roadway Express" (rows 07-017..07-023 `case_or_docket`; README line 30 and the set folder name `07_hannum_v_yrc_doj`; row 16-090's filename `ncwm_letter_hannum_2024-01-03.pdf` and its `case_or_docket` "(relator in Hannum v. Roadway)"). A case caption is public, but the field rule says companies only; suggest "U.S. ex rel. [relator] v. Roadway" and renaming the 16-090 file. Inside the files themselves individuals' names, e-mails and phone numbers are unavoidable (16-090 p. 1 author block with e-mail and phone; 23-004 pp. 6-8 goods owner; 10-038 p. 1; 22-002 pp. 15, 30; 22-004 pp. 71, 143; 22-006 pp. 14-15; 23-006..008 p. 4 auditor; 24-006 e-mails); none were transcribed into the catalogue or into these outputs.

## Task 7. Coverage matrix (real files evidencing each check; "after" applies the `discrepancy_checks=` corrections in `verify_rows.csv`, and keeps a row's claim where the correction says "unverified")
| check | meaning | real files before | real files after corrections | files after (first 8) |
|---|---|---|---|---|
| A1 | math | 45 | 43 | 01-001 02-002 04-006 04-007 04-008 04-009 04-010 04-011 |
| A2 | duplicate | 22 | 12 | 01-001 04-004 04-005 04-008 04-009 09-043 24-001 23-006 |
| A3 | paid twice via 3PL | 13 | 10 | 01-001 04-008 08-029 22-002 09-037 09-038 09-039 11-041 |
| A4 | corrected/balance-due bill | 8 | 14 | 01-001 02-002 03-003 04-008 04-009 09-031 21-001 21-002 |
| A5 | wrong payer | 15 | 14 | 06-016 08-029 21-002 22-002 09-036 09-037 09-038 09-039 |
| A6 | no matching shipment | 17 | 11 | 19-016 19-017 19-018 19-019 19-020 19-021 19-022 19-023 |
| A7 | reference for contract/quote | 10 | 11 | 01-001 09-033 19-024 19-025 20-004 09-048 09-050 22-013 |
| B1 | agreement version | 7 | 7 | 02-002 08-028 11-037 09-042 24-002 23-005 23-012 |
| B2 | base rate x discount | 51 | 48 | 01-001 02-002 04-006 04-007 04-008 04-009 04-010 04-011 |
| B3 | minimum charge | 5 | 7 | 01-001 02-002 04-009 09-032 21-001 09-043 21-005 |
| B4 | FAK/class | 13 | 11 | 02-002 09-032 19-009 19-010 19-011 19-012 19-013 19-014 |
| B5 | quote honoured | 5 | 6 | 01-001 09-033 09-046 09-047 09-048 09-049 |
| B6 | TL linehaul vs rate con | 35 | 25 | 10-035 10-036 19-026 19-027 19-033 19-034 19-035 20-007 |
| B7 | TL mileage | 12 | 10 | 10-035 10-036 11-038 18-108 08-031 10-038 11-040 22-008 |
| B8 | fuel level | 48 | 49 | 01-001 04-008 04-009 11-037 14-071 14-074 18-099 18-100 |
| B9 | fuel base | 5 | 3 | 01-001 11-037 14-071 |
| C1 | reweigh/reclass | 50 | 49 | 01-001 02-002 03-003 04-004 04-005 04-006 04-007 04-008 |
| C2 | correction fee | 27 | 20 | 03-003 04-006 04-007 04-008 04-009 04-010 04-011 04-012 |
| D1 | accessorial priced per schedule | 29 | 25 | 01-001 02-002 09-032 19-001 19-002 19-003 19-004 19-005 |
| D2 | accessorial ordered/performed | 9 | 7 | 05-015 06-016 22-013 23-002 23-003 21-015 23-010 |
| D3 | detention | 31 | 24 | 01-001 10-035 10-036 11-038 19-027 18-107 10-037 10-038 |
| D4 | stop-offs | 8 | 6 | 19-026 19-027 19-034 20-007 22-007 22-018 |
| D5 | TONU | 10 | 6 | 19-035 10-037 10-039 10-042 22-013 23-002 |
| D6 | layover | 9 | 9 | 19-034 10-037 10-039 10-040 09-050 10-042 10-044 09-051 |
| D7 | lumper | 17 | 15 | 01-001 19-034 10-037 10-038 10-039 10-040 09-050 10-041 |
| E1 | guaranteed-service refund | 1 | 1 | 21-001 |
| E2 | service-failure credit | 12 | 2 | 23-005 23-012 |
| F1 | late fees | 26 | 18 | 02-002 03-003 08-028 09-031 11-037 09-036 09-039 09-040 |
| F2 | GL coding | 1 | 0 |  |
| F3 | accrual | 2 | 1 | 18-107 |
| F4 | rebilled | 1 | 0 |  |
| G1 | shipper dispute window | 21 | 15 | 02-002 08-023 08-024 08-030 09-032 09-033 09-034 11-037 |
| G2 | carrier response deadline | 14 | 6 | 09-032 09-034 20-006 09-043 11-039 11-040 |

Real files counted: 196 before, 188 after. Checks with zero real evidence after corrections: F2, F4.


## Concerns left unproven
1. Sets 01, 03-06, 10, 11 had identity checks only; their discrepancy checks (notably C1|C2|A1|B2 on every Delphi row and D3|D5|D6|D7 on the rate-con rows) stand as claimed except where the five Delphi pages opened gave evidence.
2. Set 19 "assumed real" (brandx, scac_10559, omniparser): ISA15=P proves nothing about provenance; omniparser is ISA15=T.
3. 19-031's $0.10 L1/L3 gap may be a cropping artefact.
4. 23-007 and 23-008's claim reason was taken from an OCR keyword, not read from a render.
5. 24-001's statement pages are rotated and unread; 23-012's DocuSign tables (pp. 24-48) are unreadable by OCR.
6. For 21-004, 22-018 the invoices the row promises were not in the sampled pages; absence is not proven.
7. The 806625953 weight increase: nothing in the file says whether a reweigh happened; the "no inspection note" is an absence on two prints.
8. URL identity for 08-028 and 13-062 rests on HEAD responses, not a byte comparison.
9. The worksheet "pallets × Item 610 minimum" reading is inferred from five rows; the shipper's own rationale is not in the record.
10. Discount "9100" (91.00%) on the 2020 bills (p. 49) is read from a render once; the 2020 agreement is not in the file.

## Claim ledger
| ID | claim | file + page | label |
|---|---|---|---|
| V-01 | Bill 806625953's re-rating to 2,720 lb and $1,088.74 was billed as a $110.23 balance due on 05/05/2023, not in 2025 | 02-002 p41 (vs p28) | verified |
| V-02 | Shipper's record of that bill is 744.77+55+178.74 = $978.51, implying 2,430 lb at the same rate, discount and fuel % | 02-002 p208 row 292 (+ arithmetic) | verified |
| V-03 | pp23-35 are 2025 past-due reprints of the same 13 bills printed as 2023 balance-due bills at pp36-48; pp49-62 are 2020 bills; pp63-97 are 2022-23 corrected/balance-due bills; 59 distinct bills | 02-002 pp23-97 (text layer scan of every page; pp24-26,28,33,35,37-41,46,48,49 viewed) | verified |
| V-04 | Agreement v3: MWPC 90.30, WCPC 88.15, NEPC 87.45; Item 610 floors MWPC $127.50, WCPC (OR) $152.00; liftgate $55 partner, redelivery $80 | 02-002 pp19 (render), 20, 22 | verified |
| V-05 | NEED TO BE CHG = pallets × Item 610 minimum on partner lanes (rows 292, 364, 398, 396, 323) | 02-002 pp208-211, p20 | verified (reading: our calc) |
| V-06 | 807148067: balance-due bill of 06/19/2023 adds exactly the $94.00 residential charge justified "per Google Earth" | 02-002 pp33, 46 | verified |
| V-07 | 807307041: W&I inspection lowered net freight 338.47→291.79 and added $80 redelivery; balance due $23.28 | 02-002 pp35, 48, p211 row 398 | verified |
| V-08 | Complaint e-filed 10/07/2025; p1 is the summons of 11/10/2025; claim $271,828.70 = sum of the three worksheet totals | 02-002 pp1, 4, 5, 7, 157, 198, 224 | verified |
| V-09 | 2020 bill shows "PENALTY/TARIFF DUE $161.89", a late-payment penalty specimen | 02-002 p49 | verified |
| V-10 | Cubic-capacity re-rates cite SEFL 1090 Item 610-100 on the bill (5.36 and 5.41 PCF; charged weights 5,188.8 / 4,899) | 02-002 pp24, 26, 38; 13-065 text line 1229 | verified |
| V-11 | UPS Freight bill 407286132 prints "SHIPMENT REWEIGHED", declared 152 lb vs actual 485 lb, and a REWEIGH FEE of $18.00 | 04-009 p21 | verified |
| V-12 | A UPS Freight WEIGHT CERTIFICATE (3,460 lb, HAR service centre, 4/22/2010) is in the Delphi exhibits | 04-008 p42 | verified |
| V-13 | nVision claims are duplicate-payment refunds; YRC's status page shows APPROVED, draft 1385879 of $612.77 on 06/20/23 | 23-006 pp4-5 | verified |
| V-14 | GlobalTranz 16595's certificate is the shipper's agent's certified-scale weight: net 1,517 lb, density 3.99 | 23-004 p8 | verified |
| V-15 | Werner load 963813: rate con $2,100.00 = invoice $2,100.00; TONU $150 invoiced twice with a matching rate con | 22-013 pp13-15, 17, 23, 25 | verified |
| V-16 | Winn-Dixie: ODFL refunded $1,828.04 + $584.63 to the retailer and re-billed the vendor; corrected bill at p17 | 21-002 pp11, 14, 16, 17 | verified |
| V-17 | Mode Transportation's statement charges 18% annual interest per open invoice (explicit late-fee specimen) | 21-014 pp4-6 | verified (text layer) |
| V-18 | TQYL EDI 210 carries LAY, LUM and STOP charge lines; SPXQ carries TONU; WIEL only 400/FUE | 19-034, 19-035, 19-033 (L1 segments) | verified |
| V-19 | tesseract read 17/20 SEFL total-line amounts and 5/5 Delphi net-amount-due totals correctly | renders in verify/png | verified |
| V-20 | GovInfo and XPO URLs for 08-028 and 13-062 answer HEAD 200 application/pdf | curl, 2026-10-09 | verified (identity assumed) |


---

# Appendix A · Sub-agent notes, sets 07-08 (tag A2)

# Verification notes, tag A2 (sets 07 and 08; 19 rows), 2026-10-09

Method: every file read from `data/derived/text/<set>/<name>.txt` (page breaks = form feeds), with `pdfinfo` and `pdfimages -list` on the scanned 07 attachments and on the two files whose provenance was questioned. Scanned pages 72-2 p2 and p62, and 72-4 p2, were rendered at 100 dpi and viewed (`verify/png/07-020-02.png`, `07-020-62.png`, `07-021-02.png`). Every page number below was opened by me unless marked *assumed*. No individual's name is transcribed; where a file carries them it says so.

Verdicts: verified 5, narrowed 12, wrong 2.

## Per-row evidence

### 07-017  Doc 1, relator's complaint (13 pp, filed 2008-11-03) — narrowed
- p1 caption and "COMPLAINT"; p13 dated 2008-11-03. *verified*
- Not an audit worksheet: the two "real government bills" of the catalogue note are two text paragraphs (p8 paras 31-32: 4,310 lb billed vs 3,345 lb scaled, overcharge about $222.84; 620 vs 220 lb, about $133.23). No bill is attached. *verified*
- C1: p6-8, paras 22-32 (upward corrections processed, downward ignored). C2 (correction fee): nothing in the document; the case is about corrections not made.
- Dates: Roadway "from about 2004" (p6 para 23); Yellow "about 2006" (p6-7); filed 2008-11. The row's 2005-2009 matches neither the pleading nor the filing.
- Corrections: doc_types=complaint; discrepancy_checks=C1; date_start=2004; date_end=2008-11.

### 07-018  Doc 72, US complaint in intervention (32 pp, filed 2018-12-12) — narrowed
- p1: "THE UNITED STATES' COMPLAINT IN INTERVENTION"; conduct "Starting in September 2005 and continuing until at least October 2013" (p1 para 1, p3 para 3). *verified*
- C1: p2-3 (positive vs negative reweigh corrections), p16-18 (Yellow's January 2006 work request to "eliminate the negative adjustments", about $500,000 a month; p18 para 73: 42 negative vs 75,324 positive corrections out of more than 1.5 million invoices, 13 Nov 2006 to 20 Jan 2007), p21 paras 88-89 (records June 2010-Oct 2012: 200 examples of more than 13,000 false claims; about 725 a month; about 70,000 extrapolated over Sept 2005-Oct 2013). *verified*
- p7: table of the four SDDC contracts with dates (2006-02-28 to 2009). p21: Exhibit A described; p23: Exhibits B (Roadway), C (Yellow), D (YRC) are the SDDC tender lists. *verified*
- C2: none found. The row's "audit_worksheet" belongs, if anywhere, to Exhibit A (separate file).
- Corrections: doc_types=complaint; discrepancy_checks=C1; date_start=2005-09; date_end=2013-10.

### 07-019  Doc 72-1, Exhibit A (6 pp) — narrowed
- p1 "EXHIBIT A"; p2 title "Exhibit A: Examples of the Defendants' False Claims"; columns Delivery Date (yyyymmdd), Actual Weight (lbs), Billed Weight (lbs), Weight Variance (lbs), Weight Variance (%), DOD Customer / Shipper or Recipient. Rows run from 20100122 (p2) to 201208xx (p6). *verified*
- `pdfimages -list`: every page is a 200-dpi grey JPEG; the text layer is the court's OCR, with numerals garbled ("7 -216", "-98o/o"). Word counts clear 40 on every page, so "yes" is formally right, but the numbers are unusable from the text layer. *verified*
- C1: p2-6 (the whole table is actual-vs-billed weight). C2: none.
- Corrections: doc_types=audit_worksheet; discrepancy_checks=C1; date_start=2010-01; date_end=2012-08.

### 07-020  Doc 72-2, Exhibit B (62 pp) — wrong (extra task a)
- Section by section: p1 cover sheet "EXHIBIT B" (12 words). p2-62 one continuous four-column table titled "Exhibit B: Roadway's SDDC Tenders": Tender Number, Supplement Number, Effective Date, Expiration Date (viewed p2 and p62 as images). Rows sorted by effective date: 9/23/2005 (p2, first row 002878 / 00 / 9/23/2005 / 9/30/2006) through 9/29/2013 (p62, last three rows 003387-003389 / 01 / 9/29/2013 / 12/31/2013). Internal page numbers 1-61. *verified*
- A regex count of rows in the OCR text gives about 2,649 tender lines (*assumed*; OCR may merge or split a few).
- Does it contain reweigh data, audit worksheets, invoice extracts or statistics? **No.** No weights, no dollar amounts, no counts, no invoices. The only figures are tender and supplement numbers and dates. *verified* (text of every page scanned; p2, p62 viewed)
- Corrections: doc_types=other; discrepancy_checks empty; date_start=2005-09; date_end=2013-12; notes replaced.

### 07-021  Doc 72-4, Exhibit D (14 pp) — wrong (extra task b)
- p1 cover "EXHIBIT D"; p2 title "Exhibit D: YRC's SDDC Tenders", same four columns (viewed p2 as image). First row 004003 / 00 / 3/1/2005 / 2/28/2006; p14 last rows are supplements 01 effective 12/16/2011. Latest expiration seen 11/30/2012 (p12-13). About 498 rows by regex count (*assumed*). *verified for pp 1, 2, 14; the rest from OCR text*
- No reweigh data, worksheets, invoices, dollars or counts. Only tender and supplement numbers and dates.
- Observation: tenders headed "YRC" start in 2005, four years before the 2009 merger named in Doc 72 p3; the complaint's p23 does not explain which entity's SCAC these are. Flagged, not resolved.
- Exhibit C (Yellow's tenders, Doc 72-3) is not in the set.
- Corrections: doc_types=other; discrepancy_checks empty; date_start=2005-03; date_end=2012-11; notes replaced.

### 07-022  Doc 118, Defendants' Answer and Affirmative Defenses (40 pp, filed 2021-10-11) — verified
- p1 title and caption; p40 dated 11 October 2021. *verified*
- C1: p1-2 (paras 1-3 denied), p20 (paras 65-68 denied, "documents speak for themselves"), p39 ninth and tenth defences: the government "accepted Defendants' performance for years, with knowledge that Defendants were not processing most negative reweigh corrections, without objection"; eleventh defence: MFTURP-1 silent on negative reweighs until amended 2013-07-31 (p39-40). *verified*
- Contains individual names (executives, counsel) throughout.

### 07-023  Doc 102, Defendants' Objections to the Magistrate Judge's R&R (25 pp, filed 2020-07-31) — narrowed
- p1 title; p2 background (relator's complaint 2008-11-03; intervention 2018-12-12); p25 dated July 31, 2020 and conclusion (dismiss Counts I, II, IV, V or transfer to D. Kan.). *verified*
- C1 context: p6 (government never reweighed shipments itself), p13 (pre-payment agency verification and post-payment GSA audits, 31 USC 3527, 41 CFR 102-118, 49 USC 13710), p15 (MFTURP-1 "silent with respect to negative reweighs"). It is legal argument on materiality and venue; no reweigh counts of its own. *verified*
- Correction: date_end=2020-07 (the row says 2021).

### 08-022  Southern Furniture Doc 1, class action complaint (18 pp, filed 2019-03-08) — narrowed
- p1 caption; p1-2 "one of the largest less-than-truckload ('LTL') freight carriers". *verified*
- Subject is the suppression of negative reweighs since 2005 (p2 paras 3-4; p9 paras 25-26), class defined from 2005-09-01 (p8). *verified*
- "Fuel surcharge" appears once, in the prayer for relief (p18: "all fuel surcharges paid to YRC"). There is no fuel-level allegation and no 180-day text anywhere in the complaint. So B8 and G1 have no evidence here; C1 does.
- Doc 16 (08-023) p1 records that the pleading dismissed was the First Amended Complaint, Doc 10 of 2019-06-21, not this Doc 1.
- Corrections: discrepancy_checks=C1; date_start=2005-09; date_end=2019-03; notes replaced ("(fuel surcharge)" is wrong).

### 08-023  Southern Furniture Doc 16, Memorandum and Order (14 pp, 2019-10-31) — verified
- p1 title "MEMORANDUM AND ORDER", No. 19-2129-KHV, "the Court sustains defendants' motion"; p14 dated 31 October 2019 and signed by the district judge. It is the court's own opinion, not a party paper. *verified*
- G1 holding: p7 quotes 49 USC 13710(a)(3)(B); p13-14: the 180-day period "is a repose period", runs from receipt of the bill, cannot be equitably tolled, so plaintiff "does not have a cause of action because it did not contest the bills within 180 days of receipt". *verified*
- Pages carry no CM/ECF header stamp (chambers copy as filed on RECAP).

### 08-024  Southern Furniture, 10th Cir. No. 19-3262 (24 pp, filed 2021-03-03) — verified (extra task d)
- p1: PUBLISH, Tenth Circuit, filed March 3, 2021, appeal from D. Kan. "D.C. No. 2:19-CV-02129-KHV-KGG", which is 08-022's docket number; p2 recites the district court's dismissal on the 180-day ground, which is 08-023's holding. The three files are one case chain: district complaint (Doc 1) → district order (Doc 16, on the amended complaint Doc 10) → 10th Cir. opinion. *verified*
- Quote, p10 (last line of section II.A.a): "The statute's mandatory language makes the right to contest or collect charges conditional on compliance with the time limit. ... Quite simply, compliance with the 180-day time limit is not optional." *verified*
- p18: "we AFFIRM the district court's dismissal"; pp 19-24: a dissent that would read the 180-day limit as confined to STB proceedings. *verified*
- `pdfinfo`: created 2021-03-03 with Acrobat Distiller, consistent with the court's own PDF; the row's CourtListener URL was not fetched (no web).

### 08-025  Lewis Doc 1 (21 pp, filed 2019-01-02) — narrowed
- p1: N.D.N.Y. 1:19-cv-00001, "CLASS ACTION COMPLAINT FOR VIOLATION OF THE FEDERAL SECURITIES LAWS" against YRC Worldwide and three officers; p2: class period 2014-03-10 to 2018-12-14, Exchange Act 10(b) and 20(a); p21 dated January 2, 2019. *verified*
- It is a securities case. The reweigh practice appears as the undisclosed adverse fact (p11 para 26: "from 2005 to at least 2013, YRC Worldwide's units systematically overcharged the federal government") and as quoted 10-K language on rerate reserves ($8.8M and $10.4M at end-2017 and end-2016, p11). Not an opinion, not "other".
- Corrections: doc_types=complaint; mode=na; date_start=2014-03; date_end=2019-01; case_or_docket and notes replaced. Contains individual names.

### 08-026  Lewis Doc 75, [Corrected] Amended Class Action Complaint (141 pp, filed 2019-06-19) — narrowed
- p1 title; p2-3 table of contents; p141 certificate of service dated June 19, 2019. *verified*
- Sections B-E (pp 19-37) restate the DOJ complaint almost verbatim (p25-27 paras 76-83 include the 42 vs 75,324 figure). Section F (pp 38-47), "Former YRC Employees Confirm the Overcharge Scheme Continued Before and During the Class Period": six confidential former W&I employees (terminals in California, Illinois, Texas; tenures 2008-2018) describe negative reweighs being blocked, classification manipulation, and target customer lists. *verified pp 38-40, 47*
- This is the only first-hand, post-2013, commercial-customer evidence on the practice in the two sets; worth keeping for C1 even though the pleading is a securities complaint.
- Corrections: doc_types=complaint; mode=na; date_start=2005-09; date_end=2019-06; notes replaced. Contains individual names.

### 08-027  Lewis Doc 81-11, Exhibit J (8 pp, filed 2019-07-15) — narrowed
- p1 "Exhibit J"; p2-8: a PacerPro printout dated 7/11/2019 of the W.D.N.Y. civil docket for 1:08-cv-00811 (United States v. Roadway Express et al.), party and counsel blocks (pp 2-4) and docket text entries 1 to about 89, 2008-11-03 to 2019-03-22 (pp 5-8). *verified*
- It is a docket sheet, not a complaint or opinion; no reweigh evidence. Useful as a map (sealed 2008-2018, notice of election to intervene 2018-11-26 at entry 70, motions to dismiss and transfer 2019).
- Corrections: doc_types=other; discrepancy_checks empty; mode=na; date_start=2008-11; date_end=2019-03; notes replaced. Contains individual names (counsel).

### 08-028  Mafcote v. Estes, W.D. Ky. (8 pp) — narrowed (extra task c)
- Court: United States District Court, Western District of Kentucky, at Louisville. Case: Civil Action No. 3:07-CV-419-S. Title: "MEMORANDUM OPINION". Date: March 5, 2010 (p8, after the signature image). Parties: Mafcote Industries d/b/a Miami Wabash Paper and Royal Consumer Products v. Estes Express Lines. *verified*
- Holding in two sentences: Estes's EXLA 105-L rules tariff (Item 490, no liability for consequential damages from delay) binds the shipper because the shipper's own bills of lading incorporate the applicable tariff, and the Carmack Amendment does not reach third-party late fees, so Estes wins summary judgment on the shipper's claims (pp 2-5). On Estes's $226,450.29 counterclaim, Estes recovers only the original discounted freight charges: the "discount removals" (billing the full undiscounted rate once an invoice is 30+ days unpaid), the 30% collection fee and prejudgment interest are all barred because the parties' Agreement for Transportation says "no penalties; loss of discount or interest will be assessed to SHIPPER for past due amounts" and tariff Item 163 yields to written agreements (pp 5-8). *verified*
- URL / docket source: none in the file. No CM/ECF header, no docket entry number, no footer URL. `pdfinfo`: Title is a chambers WordPerfect path ("N:\documents\Working Docs\Mafcote v Estes\Mafcote v Estes.wpd"), Author is a short staff username, Creator PScript5.dll, Producer Acrobat Distiller 8.0, created 2010-03-05 16:33 EST, modified 17:31 EST, 8 pages, one image on p8 (signature). That profile matches a chambers-produced opinion as distributed through GovInfo/PACER, but the file itself cannot resolve the URL; it stays UNRESOLVED. Candidate to check online later: GovInfo package USCOURTS-kywd-3_07-cv-00419 (*assumed*, not fetched).
- Checks: G1 none (no dispute-window text). B2 only loosely (p6: discounted rate vs full rate as a penalty, not a rate-times-discount error). Better fits: F1 late fees (10% service charge after 30 days, $21 minimum; discount removal; 30% collection fee, pp 6-8) and B1 agreement-over-tariff precedence (p7). Dates: agreement 2000-09-01 (p3 n.3), suit 2007, opinion 2010-03, so date_end=2010-03. Mode LTL is assumed (Estes is an LTL carrier; the opinion does not say).

### 08-029  Gaines Motor Lines v. Klaussner, 4th Cir. No. 12-2269 (25 pp) — narrowed
- p1 PUBLISHED, argued 2013-09-18, decided 2013-10-30; eight motor carriers as appellants; p2 "Vacated and remanded with instructions"; p3 question of first impression: no federal jurisdiction over a carrier's contract claim for unpaid freight charges absent a federal tariff; p25 VACATED AND REMANDED. *verified*
- Facts pp 4-6: shipper hired broker Salem Logistics in August 2007; carriers told to bill "Klaussner Furniture c/o Salem Logistics"; BOLs marked Prepaid with an executed non-recourse clause; Salem paid for a while, then defaulted and closed; carriers sued the shipper under 49 USC 13706(b). That evidences A5 (who owes the freight charges) and A3 (shipper paid the 3PL, carrier unpaid). *verified*
- G1: nothing on a dispute window; 13710(a)(1) and (a)(4) appear only in the jurisdiction analysis (p12, p18). Dropped.
- Mode: the opinion never says TL or LTL (grep for both: none). "TL" is an assumption from multi-stop furniture loads (p4). Left as is, flagged.
- `pdfinfo`: Acrobat PDFMaker 10.1, created 2013-10-29, consistent with the ca4.uscourts.gov URL (not fetched). Text layer: p25 has 30 words, so "partial" is right.

### 08-030  Sivak v. UPS, E.D. Mich. Doc 36 (40 pp, 2014-07-01) — narrowed
- p1: "OPINION AND ORDER GRANTING DEFENDANT'S MOTION TO DISMISS ... IN ITS ENTIRETY"; p39-40 ordered and dated July 1, 2014. A real opinion. *verified*
- G1: p7, section "UPS's 180-Day Notice Requirement", quotes UPS Terms s.47.1 (request within 180 days of receiving the contested invoice or the claim is waived); p12 plaintiffs allege substantial compliance. But p15 n.4: the court "declines to decide whether Plaintiffs were obligated to contest the overcharges within 180 days under both the Shipping Contract and 49 U.S.C. s.13710(a)(3)(B)". So the window text is evidenced; a holding on it is not. *verified*
- Correction: notes only ("window law" claim softened).

### 08-031  Ricks v. Menlo, E.D. Cal. Doc 29, First Amended Complaint (35 pp, filed 2016-02-09) — narrowed
- p1 caption, SEALED stamp, filed Feb 09, 2016; p35 jury demand and signature. *verified*
- p2 paras 2-3 list the six theories; p9 paras 30-31 (air rates billed for LTL ground moves); p12 para 36-37 (TL mileage from the DTOD, LTL by weight; air vs ground fuel and oversize surcharges, ground oversize minimum $125, air oversize 30% of line haul); p18 paras 58-60 (June 2012 email on the fuel surcharge, oversize dimension table); p20 (EXP accessorial applied to the wrong base); p21 (DTOD mileage rounded up, 615.1 to 616; diversion-date FSC). *verified*
- B4 (FAK/class): no freight-class or NMFC allegation found (grep "class", "classification", "NMFC": only "world class" on p6). Dropped.
- Correction: discrepancy_checks=B6|B7|B8|D1. Contains individual names.

### 08-032  Grupp v. DHL, W.D.N.Y. Doc 1 (14 pp, filed 2008-04-18) — verified
- p1 caption, Case 1:08-cv-00301-JTC; the filed copy carries a "PRIVILEGED AND CONFIDENTIAL / ATTORNEY WORK PRODUCT / DRAFT OF 4/18/2008" legend; p14 dated April 18, 2008. *verified*
- B8: p2 para 2 (jet fuel surcharge on ground-only moves; diesel surcharge not passed to contractors); p7-8 paras 24-37 (jet fuel surcharge 22%, capped at 7% for some government packages; diesel 6.3%; conduct "beginning in or about 2003 or 2004"). *verified*
- date_start 2004 is the later of the two years pleaded; acceptable. Contains individual names.

### 08-033  Grupp v. DHL, 2d Cir. 14-3595 Doc 33 (56 pp, filed 2014-11-03) — verified
- p1: "BRIEF AND SPECIAL APPENDIX FOR PLAINTIFFS-APPELLANTS"; p2 table of contents; p7 jurisdictional statement (dismissal 2014-09-11, judgment 2014-09-12, appeal 2014-09-17); p56 SPA-17 is the judgment form. *verified*
- B8: p7-8 (jet vs diesel surcharge). G1: p8 ("this Court's vacatur ... rejecting DHL's 180-day notice argument. See 742 F.3d 51"); p41 and p45 in the special appendix (the district decision quoting the Second Circuit: "the 180-day rule cannot apply to a qui tam action under the FCA"). *verified*
- It is a party's brief, so the G1 statements are an account of the earlier holding, not the holding itself; the row's doc_types "other" is right.

## Extra tasks, summary
- (a) 72-2: Exhibit B, Roadway's SDDC tender list, 62 pp, four columns, about 2,650 rows, 2005-09 to 2013-12; no reweigh data, worksheets, invoices, dollars or counts.
- (b) 72-4: Exhibit D, YRC's SDDC tender list, 14 pp, same layout, about 500 rows, 2005-03 to 2012-11; no reweigh data. Neither file holds any figure about reweighs; the only reweigh figures in set 07 are in Doc 72 (p18: 42 vs 75,324; p21: 200 of 13,000+, about 725 a month, about 70,000 extrapolated) and Exhibit A (72-1).
- (c) Mafcote: see 08-028 above. URL cannot be resolved from the file.
- (d) Same case chain confirmed (08-024 p1 cites D.C. No. 2:19-CV-02129-KHV-KGG; p2 recites the 180-day dismissal). Quote at p10: "Quite simply, compliance with the 180-day time limit is not optional."

## Concerns left unproven
1. Row counts for Exhibits B and D (about 2,649 and 498) come from a regex over garbled OCR; not hand-counted.
2. Exhibit D's "YRC" tenders predating the 2009 merger: unexplained by the complaint.
3. Mode "TL" for 08-029 and "LTL" for 08-028: neither opinion states the mode.
4. The mafcote URL: no offline evidence; the GovInfo package name is a guess.
5. Exhibit A (72-1) row count of 200 is taken from Doc 72 p21, not counted on the scan.
6. For 08-025 and 08-026 I set mode=na because the pleadings are securities complaints; the coordinator may prefer LTL for 08-026, whose section F is substantive LTL evidence.

## Claim ledger
| ID | claim | file + page | label |
|---|---|---|---|
| A2-01 | Yellow made 42 negative and 75,324 positive reweigh corrections out of >1.5M invoices, 2006-11-13 to 2007-01-20 | Doc 72 p18 para 73 | verified |
| A2-02 | DOD records June 2010-Oct 2012 show >13,000 negative-reweigh false claims, about 725 a month; about 70,000 extrapolated over Sept 2005-Oct 2013 | Doc 72 p21 paras 88-89 | verified |
| A2-03 | Exhibit A lists 200 example shipments with actual vs billed weight, deliveries 2010-01 to 2012-08 | 72-1 p2-6 (count from Doc 72 p21) | verified (count assumed) |
| A2-04 | Exhibits B and D are SDDC tender lists with no weights or dollars | 72-2 p2, p62; 72-4 p2, p14 | verified |
| A2-05 | YRC's answer admits the government accepted performance "with knowledge that Defendants were not processing most negative reweigh corrections" | Doc 118 p39 | verified |
| A2-06 | D. Kan. held the 180-day limit of 49 USC 13710(a)(3)(B) is a repose period, not tollable | Doc 16 p13-14 | verified |
| A2-07 | 10th Cir.: "compliance with the 180-day time limit is not optional"; affirmed, with a dissent | 10th Cir. opinion p10, p18, p19-24 | verified |
| A2-08 | Mafcote: tariff incorporated by the shipper's own BOL bars consequential damages; written agreement bars discount removal, 30% collection fee and interest | mafcote p2-5, p6-8 | verified |
| A2-09 | Sivak court declined to decide the 180-day question | sivak p15 n.4 | verified |
| A2-10 | Six former YRC W&I employees (2008-2018) say negative reweighs stayed blocked for commercial customers after 2013 | Lewis Doc 75 p38-47 | verified (allegations, not findings) |

# Appendix B · Sub-agent notes, sets 12-18 and 20 (tag A7)

# notes_A7 — identity-only check of sets 12, 13, 14, 15, 16, 17, 18, 20 (103 rows)

Method: for every PDF, `pdfinfo` metadata + `pdftotext -f 1 -l 1 -layout`; page 2 where page 1 was a bare cover (17-095, 17-096, 16-082, 14-072, 15-083, 13-065, 20-003); page 1 rendered at 100 dpi and viewed for the four scans (16-085, 16-086, 18-099, 18-106). Paired files compared by sha256 and full-text `diff`. Non-PDFs: HTML `<title>` and meta tags; xls OLE streams and BIFF BOUNDSHEET names (no xlrd on the machine, cell values not read); docx `document.xml` and `core.xml`. Discrepancy-check IDs were not chased beyond page 1 (per brief); the evidence column says "not checked" where that applies. Word counts on pp. 1-3 / middle / last were taken for the rows marked `partial` and all agree with the rule. All statements below are *verified* (page opened by me) unless marked *assumed*.

Verdicts: **verified 76 · narrowed 26 · wrong 1** (13-070).

## Extra tasks from the brief

1. **Tariffs whose p.1 date differs from filename/date_start.** Only 13-067 Landstar: p.1 "Effective: March 15, 2020"; the row's 2020-03-17 is the PDF creation date. ABF 111-AS/AU rows use the "Last revised" date (Feb 3 2025 / Aug 21 2026) while the provisions' effective dates are Sep 9 2024 / Jun 22 2026 — consistent with the filename convention, noted, not corrected. 13-049 Estes, 13-065 SEFL, 13-069 GSA 200-A have blank dates that p.1 supplies (Jan 2 2026; Eff. 6/1/2026; Oct 1 2021) — suggested fills in the note column.
2. **real vs template.** 13-071, 13-072, 13-073 (collector wrote `real`) → `template`: tariffs by the field definition. 13-071 is moreover a 25-page *summary of extended services* "as defined in Rules Tariff USA 100", not the tariff. Also narrowed to `template`: 14-072 (GSA FSC schedule), 14-075 (contract exhibit FSC schedule), 14-076 (Estes FSC web page), 20-003 (regulation text).
3. **FedEx series_a / series_b (13-050 / 13-051).** Distinct versions, not duplicates. Both covers read "FedEx Freight 100-Y Rules Tariff, EFFECTIVE: JANUARY 5, 2026". Different sha256. series_a PDF created 2026-09-10, latest item stamps "Revised 9-11-26". series_b created 2026-09-29 and adds Item 570 Fuel Surcharge "(Revised 10-1-26)" and Item 759 Volume Services "(Effective 10-1-26)". Note the actual tariff designation is **FXF 100-Y**, not "100 series".
4. **ODFL 100-Q_a / _b (13-052 / 13-053).** Distinct. Same cover (Effective April 14, 2025, cancels 100-P). _a: 240 pp, no "Updated" line, latest item stamp "Revised 06/15/2026". _b: 244 pp, cover adds "Updated: October 5, 2026", 26 items stamped "Revised 10/05/2026" (Item 151-10 retitled "Allowances or Incentives"; new Remote Access items for DE and MD). 1,282 diff lines.
5. **GSA 200-A (13-069).** Holds: "Uniform Rules Tariff No. 200-A (GSA No. 200-A) ... October 1, 2021, this edition cancels the previous edition", 121 pp. **GSA 1000-D (13-070): wrong.** 5-page Word-2007 PDF (May 2014) titled "SECTION B – TABLE OF BASELINE RATES AND MINIMUM CHARGES, ITEM 100" with an FY15 $65 LTL flat minimum note. It is a rate/minimum-charge table extract, not a rules tariff, and "1000-D" appears nowhere in its text.
6. **Government audit reports (set 18), report number and date on p.1:** AFMD-89-47 Aug 1989 (scan, read from the rendered page); NSIAD-92-157 (June 1992 per PDF date; p.1 shows the number, month not legible in OCR); NSIAD-92-61 Dec 1991; T-NSIAD-99-213 June 29 1999; A120060/Q/9/P13001 Mar 14 2013; A120169/Q/9/P14002 Mar 31 2014; D-2001-148 June 22 2001; D-2009-072 Apr 9 2009 (scan, rendered); USPS 22-202-R23 Apr 25 2023; USPS 20-295-R21 May 5 2021. All match the rows. The `B2|B8|C1` checks copied across 18-099..106 are not evidenced on p.1; B8 (fuel) in a 1989 GAO report is doubtful — left for a full check.
7. **EDI guides (set 12).** Versions: all 4010 except 12-052, which is **4060** and is FedEx **Express/Ground/SmartPost** (not Freight; parcel → mode `na`), dated December 2022 on p.1 (row says 2022-01; metadata title says April 2021). **Shipper guides:** 12-039 (3M, "3M-IB210-4010", Aug 11 2017), 12-041 (Cardinal Glass Industries, v1.5, publ. 5/29/2015, notes 5/28/2024) and 12-047 (Insight Direct USA, v3.1, 3/21/2023) are guides a SHIPPER issues to its carriers; 3M and Cardinal Glass are wrongly in `carriers` (Insight's row is correctly blank). **12-043 and 12-051 are the same document** (FedEx Freight 210/820/997 v4010, December 2022): full-text diff is empty; only the PDF title "(Dec '22)" and ModDate differ; 12-051's "apr2021" name and 2021-04 date are unsupported. **12-046 "XPO_210_spec"** never mentions XPO, Con-way or CNWY — it is a generic "V4010_210_basic.ecs, For internal use only" print dated 09/25/2015; its identity rests on the source URL alone. 12-050 is a **211** (BOL) business-policies guide, not a 210 invoice guide (doc_type edi_guide still fits).
8. **Fuel rows claiming B9.** 14-073 FedEx table shows index→% only (no base price line); 14-071 and 14-075 show price bands starting at zero surcharge, so the base is implied. Noted, not corrected. 14-076 Estes HTML: the surcharge table body is script-loaded and absent from the saved file; only the headers and the "Note A" stepping rule survive.

## Per-row evidence detail (page numbers)
See the `note` column of `verify_rows_A7.csv`; every row cites p.1 (and p.2 where used). Rows needing more than the note:
- 20-003: p.1 col. 3 ends "[FR Doc. 2024–27552 Filed 11–25–24]" after §§102-118.545–.645; the next heading is "41 CFR Part 102–117, FMR Case 2024–03"; p.2 col. 3 ends "[FR Doc. 2024–27565 Filed 11–25–24]" followed by "49 CFR Parts 571" (NHTSA). So 2024-27565 is the 102-117 pronoun rule; the 102-118 amendment is doc 2024-27552 and only its tail is in the file.
- 15-083: p.1 and p.2 name "Model: CS900 and CS900LX", Certificate 05-030P, issue date April 15, 2005, provisional CC. "CSN210" (filename) does not appear.
- 14-075: no occurrence of "FedEx" in any of the 4 pages; headings "Freight Solutions FSC", "Appendix B – Fuel Surcharge, Revised 10/2024", metadata title "Exhibit 6C".
- 16-085..091 (NCWM): dates on p.1 are 2025-01-10, 2025-10-24, 2025-07-02, 2024-07-17, 2024-06-28, 2024-01-03, and July 2025 (PDF date) for the task-group report. All are public-comment letters/reports on NCWM proposal OTH 24.1 (Uniform Shipping/Shipment Law), not letters disputing a bill; `doc_types=other` proposed. 16-088 Lynden describes itself as both LTL and TL → `mode=both`.

## Personal names
Individual names appear on p.1 of 16-085 (letter author), 16-086 and 16-087 (signatories), 16-090 (author, also in the filename and the row's path), 17-094 (contact list), 17-098 (byline), 15-082 and 15-083 (NTEP contacts and chairs), 20-004..006 (counsel and judges, public record), and in the docx author fields of 16-096. None are transcribed here.

## Concerns left unproven
- 12-046 attribution to XPO/Con-way (no internal evidence); 14-075 attribution to FedEx Freight (no internal evidence) — both need the source URL or the collector's download note.
- 14-074 xls cell range 1994–2026 not read (no xlrd; only the sheet names "Contents" and "Data 1" were confirmed).
- 18-100 month "June 1992" taken from the PDF timestamp; the OCR of p.1 does not show the month.
- The discrepancy-check IDs on sets 13, 15, 17 and 18 (e.g. the identical B3..G2 list on every tariff row and B2|B8|C1 on every audit report) were not evidenced beyond p.1.
- 14-071 `real` kept (it records actual weekly 2025 values) but "DOE carriers" is not an issuer; Atlas is.

## Claim ledger
| ID | claim | file + page | label |
|---|---|---|---|
| A7-1 | 13-050 and 13-051 are two revisions of FXF 100-Y (eff. Jan 5 2026); _b adds Item 570 "Revised 10-1-26" and Item 759 "Effective 10-1-26" | fedex_freight_fxf_100_series_a/b.pdf p.1; full-text diff | verified |
| A7-2 | 13-053 is ODFL 100-Q "Updated: October 5, 2026" (244 pp) vs 13-052 without that line (240 pp) | odfl_100-Q_a/b.pdf p.1; diff | verified |
| A7-3 | 12-043 and 12-051 have identical text (FedEx Freight 210/820 v4010, Dec 2022) | both PDFs, full-text diff empty | verified |
| A7-4 | 12-052 is FedEx Express/Ground/SmartPost version 4060, December 2022 | FedEx_210-820_X12-4060_guide_jan2022.pdf p.1 | verified |
| A7-5 | 13-070 is a 5-page "Section B table of baseline rates and minimum charges" with no "1000-D" in the text | gsa_1000-D.pdf p.1 + grep of derived text | verified |
| A7-6 | 13-067 p.1 says Effective March 15, 2020 (row: 2020-03-17) | landstar_land_100-A_2020-03-17.pdf p.1 | verified |
| A7-7 | 20-003 holds the tail of FR Doc 2024-27552 (102-118) and the whole of FR Doc 2024-27565 (102-117) | FR_2024-27565_102-118_amendment.pdf pp.1-2 | verified |
| A7-8 | 14-075 contains no "FedEx" anywhere; headed "Freight Solutions FSC", "Exhibit 6C", "Appendix B revised 10/2024" | FedExFreight_FTL_fuel_surcharge.pdf pp.1-4 | verified |
| A7-9 | 15-083 certifies Mettler-Toledo CS900/CS900LX (cert. 05-030P, Apr 15 2005), not "CSN210" | Mettler_CSN210_NTEP_cert.pdf pp.1-2 | verified |
| A7-10 | 12-046 contains no XPO/Con-way/CNWY identification | XPO_210_spec.pdf, grep of all 22 pp | verified |
