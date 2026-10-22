# Check BB · Adversarial review of the money-and-dispute validation

**Date:** 2026-10-18. **Reviewer:** adversary of validator BB. **Validator's report:** `research/s5_check_BB_c09_fact_map_money_dispute.md` (435 lines). **Target doc:** `data/doc-exploration.md` (2026-10-10), the money facts M01-M25, the dispute facts D01-D08, §2.5, the §3 rows and derivations, §4.5-§4.6, the M and D rows of the six §5 chains, and §8 rows 1, 3, 5, 6, 8, 13-17, 19, 20, 22, 24, 46.

**How:** offline, read-only on `data/` and `research/` (this file is the only thing written), no sub-agents. Every KEEP-verified, NARROW, DISCARD and ADD verdict of the validator was re-opened at its citation: text-layer sets by `grep -n` on `data/derived/text/`, set 04 by its OCR, EDI by my own parser over all 36 files of set 19 with the separators read from each ISA's own element count (`SCRATCH/bbadv_scripts/edi2.py`), the ABF set by my own script (`abf.py`), scans as the validator's renders in `SCRATCH/renders/` plus three I rendered myself (22-008 p. 10, 21-007 p. 4, 21-006 p. 5). Arithmetic in `python3 -I`. Companies only: no person's name, phone number or home address appears here; where a rendered page carries one, I say so without copying it. Verdicts: **CONFIRM** (the evidence says what the validator says), **OVERTURN** (it does not), **NARROW** (in part; corrected wording given), **could not test**.

## §0 Summary

**Counts, by the validator's section** (every KEEP-verified, NARROW, DISCARD and ADD row of the validator appears in §2 below; KEEP-assumed cells were tested for whether `data/` can carry them):
- **§2.0 priority items** (the §2.5 DISCARD, the TQYL and Werner reinterpretations, the two carrier misattributions, M02, the EDI counts, the 980 total): 8 rows, **8 CONFIRM**; the validator's one KA in that set (the Estes 980 total) is now verified.
- **§2.3 money cells** (validator: 83 KV, 6 KA, 15 N, 9 ADD): 79 rows re-opened: **71 CONFIRM, 3 NARROW** (the YRC "Bill Date" ADD; "29 bills" → 28 for the ABF reweigh remark; the M19 narrowing itself too strong at Estes), **5 KA confirmed untestable** (M15 Fallback and If none, M17 If none, M24 Fallback and If none), 0 OVERTURN; six rows gain an addition (M08, M09, M11, M12, M15, M17).
- **§2.4 dispute cells**: 24 rows: **23 CONFIRM, 1 KA confirmed not held** (D07 Primary); D07 Fallback gains "Date Invoice Paid".
- **§3 columns** (validator: 95 KV, 4 N): the 4 NARROWs **CONFIRM** against AK ll. 136-177; the KV rows CONFIRM in two grouped lines (6 rows).
- **§4.1 join keys**: 10 rows, **10 CONFIRM**; the validator's KA on "63387,63388" is now verified in 19-018.
- **§4.2 §3 rows and derivations**: 15 rows, **15 CONFIRM**. **§4.3 §4.5-§4.6**: 8 rows, **8 CONFIRM**.
- **§4.4 chain M and D rows**: 62 rows: **60 CONFIRM, 2 could not test** (chain A's complaint ¶9; chain B's Form 410 pp. 1-3; neither re-opened by the validator or by me).
- **§4.5 ledger rows**: 15 rows, **15 CONFIRM**. **§5 ADDs**: 14: **12 CONFIRM, 1 NARROW** (ADD 1's YRC part), 1 left to validator BC (M26) with its documents confirmed.
- **In all: 241 rows; 228 CONFIRM, 4 NARROW, 0 OVERTURN, 8 could-not-test, 1 deferred.** Every dataset-wide count the validator reported (82/82, 0/0/0, the L1-08 code set, B3-10, R3; 101 / 101 / 82 / 27 / 21 / 9 groups and 23 bills / 4 / 6 at ABF; 38 UPS lists never over four; 8 TForce lists with ages 7-512 days) reproduces to the unit from my own scripts. Every clock and money figure recomputes. Privacy: 0 hits (§6). `sha256sum -c data/SHA256SUMS`: 271 OK, 0 failed.

**The five findings that matter most.**
1. **The §2.5 DISCARD is right, and the page proves it.** 21-015 p. 34 is The Custom Companies' billing advice with SHIPPERS NO. "MIA 95055" and PRO. NO. "16422968-00"; TForce's bill p. 33 prints "B/L NO. MIA95055". TForce reused the advice's shipper number, not its PRO; AW §5 never said otherwise. The validator's wording should go into the doc as drafted. The two reinterpretations also hold: the pairs are TQYL (19-034; ISA-06 BPTS, GS-02 and B3-11 TQYL), on adjacent pickup dates **and the same invoice date 20251215**; the Werner pair (22-008 pp. 7, 10) shares pickup 01/30/2023 and issue 02/09/2023 and differs only by tractor, trailer, dispatch and weight.
2. **Nothing the validator confirmed was overturned.** The one place its own narrowing is too strong is M19: AAA Cooper's L5 is description and NMFC only, but Estes's L5 also carries a remark ("LEFT MSG FOR DEL APPT 11/14/13") and a contact-like line (19-015 ST 60003), so "carry only the description and NMFC in L5" must not go into the doc for Estes.
3. **Two of its additions need a caveat before they are applied.** YRC's statement "Bill Date" equals its "Due Date" on all eight rows of 21-006 p. 5, so it is a bound, not a bill date; and the SEFL 2020 "MINIMUM FREIGHT CHARGE $1,019.77" on p. 49 is gross − discount (11,330.77 − 10,311.00), not a floor lift, which matters for the M11/M12 ADD.
4. **Six places the validator left assumed or missed are now settled on the files:** XPO's "M" minimum marker (03-003 p. 4, 712-591246) and TForce's "MIN" (21-015 l. 284) close its §7 item 7; the 980 group total 1,218.85 and the "63387,63388" BOL (19-018) close two KAs; the TForce reprint list prints the amount of each earlier print (546903626: 2,369.67 then 1,118.82) and Mode's statement prints "Original Amount" beside "Open Balance", two unlisted sources for M17; the 3PL form carries "Date Invoice Paid" (23-011 l. 209); Stevens bills print DIM WEIGHT / REWEIGH / CHG WEIGHT columns (21-011); Estes's `L1-03` = `FR` flat qualifier (19-015 ST 60003); and the XPO DR echoes the fee name. Counter-examples found: an uneven XPO late-fee ladder (LP1, LP3, LP4, no LP2; 03-003 p. 4), and text under a redaction box (21-004 p. 8).
5. **§5 against the raw traces: the doc dropped more than the validator saw.** Both verdict-setting slips were caught (chain C "20 days" is 18 after delivery and 20 after pickup; chain D "Col/Ppd P" is on the A/R pages). But the walks had filled D03 in chains A, B, D and F and D01 in B and D, and §5 dropped them all; and the consignee's statement, debit memo and check stub that make D07 "never public" wrong were in walk B's own M24 and D07 rows before §5.4 reduced them to "only in the carrier's A/R history". The validator re-found those pages but did not trace the drop to the walk (§4).

## §1 Method

**Files opened, by file_id.**
- Text layer: 01-001 (all 130 pages by script), 02-002 (whole-file counts; pp. 99, 210, 212, 223 lines), 21-005, 21-006, 21-007, 21-012, 21-013, 21-014, 21-015 (pages 32-34 by form feed; ll. 262-300, 580-595, 813-830), 22-011, 22-013, 22-007, 23-010, 23-011, 04-005, 16-095, 20-001, 20-003; set 04 OCR (`ocr_all.txt` and the per-file OCR) for the six-digit code lines and the 38 reprint lists; sets 09, 21, 22, 23, 24 swept for payer-side records (remittance, check, EFT, voucher, portal).
- EDI: all 36 files of set 19 parsed; the 18 real or assumed-real 210 files (19-001…19-015, 19-033…19-035) recounted segment by segment; 19-017 (ODFL 214) by grep.
- Renders viewed (PDF page numbers): 21-015 pp. 33, 34; 22-008 pp. 4, 7, 10; 02-002 pp. 41, 46, 49, 60, 63, 94; 03-003 pp. 11, 12, 14, 19, 20; 21-002 pp. 6, 8-11, 13, 15, 17; 21-001 pp. 7, 11, 12, 13; 21-010 p. 4; 21-004 p. 8; 21-007 p. 4; 21-006 p. 5; 22-012 p. 4; 22-015 p. 4; 23-006 pp. 4, 5; 23-003 pp. 2, 5; 23-004 pp. 2, 4.
- Raw traces: `SCRATCH/walks_raw/walk_A_sets02_03.md` (chains A, B; the final report and its handback copy), `walk_B_sets19_21.md` (C, D), `walk_C_sets23_22.md` (E, F), read in full.
- Other: AK §3.2 ll. 128-177; AV §2.1-§2.2 and the AV adversarial review ll. 49-51, 102, 245, 269; AW §5 and the AW review row 8; `doc-explanation.md` §4.2 l. 196; `data/catalogue.csv` rows 19-033…19-035; set 19 `source.md`; `data/README.md` l. 45.

**Scripts** (`SCRATCH/bbadv_scripts/`, run with `python3 -I`): `edi2.py` (per-ST B3-02/-06/-07/-08/-10/-11, L3-05, ΣL1-04, L1-08 codes, K1/NTE/L5, R3, ISA-06/GS-02, the 980 BT1 total, the TQYL same-amount pairs); `abf.py` (per-PRO page groups, bill-date labels, `AU=`, `Tariff:`, PQ numbers, quote-difference notes, amount + ship-date collisions, CORRECTED INVOICE, two-page bills); inline scripts for the reprint-list sweep, UPS list lengths, TForce list ages, SEFL per-article gross, the clock arithmetic and the privacy regexes.

**Integrity:** `sha256sum -c data/SHA256SUMS` run at the end: 271 OK, 0 failed. `git status`: only the validators' and reviewers' report files are untracked; nothing under `data/` changed. The three renders I made are in the scratchpad, not in the project.

## §2 Per-claim table

Columns: validator row | validator verdict | my verdict | evidence | corrected wording if any. "KV" = KEEP-verified, "KA" = KEEP-assumed, "N" = NARROW, "D" = DISCARD, "A" = ADD, as in the validator's ledger.

### §2.0 The priority items

| Validator row | Val. | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| §2.5 "an older carrier's PRO on a billing advice reused as the BOL (TForce)" | **D** | **CONFIRM** | 21-015 p. 34 (rendered): "THE CUSTOM COMPANIES BILLING ADVICE", boxes DATE SHIPPED 12/13/22, **SHIPPERS NO. MIA 95055**, TRAILER 1638394, ORIGIN CHI, DEST 107, ACCOUNT NO. SATUR01, BILLING DATE 12/13/22, **PRO. NO. 16422968-00**; "Manifest #: 756717", "6911973620" at right; 4424 lb "C70", "LN 1 BOL CLASS 100", "RATED AS 5000 LBS.", "DISCOUNT -64.6%", "FUEL SURCHARGE: 41.70%", TOTALS 402.74 PPD; TForce's barcode label "546 903 626 DTR" affixed at the foot, a handwritten shipper name and address, a signature and "12-20-22" (the handwritten contact name and phone on the page are not copied). 21-015 p. 33 (rendered; text ll. 813-814): FREIGHT BILL NO. 546903626, SHIP DATE 12/20/2022, **B/L NO. MIA95055**, P.O. NO. 448190. So the B/L number TForce printed is the advice's SHIPPERS NO., not its PRO 16422968-00. AW §5 l. 17 says "a second carrier's billing advice can serve as the BOL" and AW's held-BOL list l. 27 says "21-015 p. 34 (TForce, a billing advice used as BOL)"; nothing in AW says the PRO was reused. The doc merged two true cases into one false one | As the validator: "the shipper number of another carrier's billing advice (MIA 95055) reused as TForce's B/L NO., with that carrier's PRO 16422968-00 on the same paper (21-015 pp. 33-34)" |
| §2.5 "two TQL pairs … adjacent dates" | N (TQYL) | **CONFIRM, one addition** | `edi2.py` on 19-034: ISA-06 `BPTS`, GS-02 `TQYL`, B3-11 `TQYL` on all 20 transactions. Pairs: B3-02 34704009 and 34703959, both B3-07 431960 ($4,319.60), N4 BUFFALO NY → ONTARIO CA, G62*86 20251207 / 20251206; 34688921 and 34688904, both 240195 ($2,401.95), WEYAUWEGA WI → SPRINGFIELD MO, 20251202 / 20251203. **All four carry the same B3-06 invoice date 20251215.** Catalogue row 19-034: "TQYL (truckload carrier SCAC)"; README l. 45 "one batch from TQL, a broker" is the inconsistent label | "two TQYL pairs (19-034) on adjacent pickup dates and the same invoice date, and one Werner pair (22-008 pp. 7, 10) on the same pickup and issue date" |
| §2.5 Werner pair 39060407 / 39100828 | N (same date) | **CONFIRM** | 22-008 p. 7 (rendered): FREIGHT BILL NO. 39060407, PICKUP DATE 01/30/2023, ISSUE DATE 02/09/2023, SHIPPER NUMBER "RETURN", tractor 82318, trailer 378044, miles 154, dispatch DB498427VZ, weight 33000, lines 266.88 / 97.02 / 54.05 / 19.97 / 71.40 / 72.27 / 253.24, TOTAL 834.83, "DELIVERY DATE - 01/30/2023", World Kitchen (Greencastle PA) → Instant Brands LLC (Charleroi PA). p. 10 (my render): 39100828, the same two dates, tractor 79405, trailer 387449, DB539267VZ, weight 4444, the same seven amounts, 834.83. 266.88 + 97.02 + 54.05 + 19.97 + 71.40 + 72.27 + 253.24 = 834.83 | — (also: both bills print "RETURN" as the shipper number, so the doc's "a Werner bill printing RETURN" (p. 4) is three bills, pp. 4, 7, 10) |
| M13 Fallback "UPS '003570' = 35.70%" | N (TForce) | **CONFIRM** | 21-015 l. 285 "003570 LTL FUEL ADJUSTMENT 35.70 215.25" sits under the page header l. 262 "TForce Freight … TFORCE FREIGHT LTL" (bill 610384246, "UPGF 560 11/14/22" reference at l. 289). Set 04 OCR (`ocr_all.txt`): "003690 LTL FUEL ADJUSTMENT 36.96" and "003690 … 36.90}" (OCR variants of one code), "003810 … 38.10", "003420 … 34.20", 20 distinct code lines; 0 hits for "003570" or "002550" anywhere in set 04; the carrier header in set 04 reads "UPS Freight" (351 + 179 hits), not TForce | As the validator |
| M15 Primary "UPS '002550 INSPECTION'" | N (TForce) | **CONFIRM** | 21-015 l. 589 "002550 INSPECTION 25.50" under header l. 564 "TForce Freight"; set 04 OCR prints "001860 INSPECTION 18.00" and "001906 INSPECTION 19.06" (2 lines; 7 INSPECTION mentions in all) | As the validator |
| M02 Primary "ISA-06 / GS-02 (the envelope sender)" | N | **CONFIRM** | `edi2.py` distinct (ISA-06, GS-02, B3-11) triples over the 82 real 210s: (ODFL, ODFL, ODFL), (AACT, AACT, AACT), (EXLA, EXLA, EXLA), (BPTS, WIEL, WIEL), (BPTS, TQYL, TQYL), (BPTS, SPXQ, SPXQ). GS-02 equals the carrier in every file; only ISA-06 differs, on the three BPTS batches | As the validator |
| §1a EDI counts (82/82 reconcile; 0 B3-08, K1, NTE; 48 STs with L5; the code set; B3-10; R3; senders) | KV | **CONFIRM** | My recount, 18 real files, 82 210 transactions (ODFL 34, AACT 11, EXLA 3, WIEL 11, TQYL 20, SPXQ 3): B3-07 = L3-05 = ΣL1-04 in 82 of 82 (0 failures); B3-08 filled 0; K1 0; NTE 0; L5 present in 48 STs (AACT 11, EXLA 3, WIEL 11, TQYL 20, SPXQ 3; ODFL 0); L1-08 codes `405` 34, `FUE` 46, `DSC` 46, `DAA` 11, `400` 34, `LUM` 8, `LAY` 2, `STOP` 1, `STC` 1, `TONU` 1, `MMC` 1, `SUF` 1, uncoded 88 (ODFL 72, AACT 13, EXLA 3); B3-10 `017` 34, `035` 46, blank 2; R3 with a SCAC other than the biller: `R3*NEMF*1*HARRISBURG*M****12698` (19-009 ST 0014, B3-07 32560), 5031/12900, 11188/28687, 44150/113205 (19-010 ST 0016-0018), 34104/87446 (19-013 ST 0006), and `R3*OVLD*D**LT**2200302174` (19-015 ST 60001). Every count matches the validator's to the unit. A trap worth recording: a fixed-offset ISA reader (terminator at character 106) finds 0 of the 34 BPTS transactions, because those files' ISA is 107 characters; taking the terminator as the character after the 16th element finds all 82 | — |
| §4.4 chain C contrasts, "group total ST*980 … 1,218.85" | KA (not parsed) | **now verified** | 19-015 ST 60004 is a 980: `BT1*210*3*1*B307*1218.85` (3 bills, total 1,218.85); 523.69 + 498.16 + 197.00 = 1,218.85 | the validator's one KA in this row can be promoted to KV |

### §2.1 The validator's §2 ledger, §2.3 money cells (every KV / KA / N / A cell)

| Validator row | Val. | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| M01 Primary (210 B3-02; TL N9*IV) | KV | CONFIRM | `edi2.py`: B3-02 filled on 82 of 82; 19-001 ST 0001 `B3**00902527924*…`; 19-035 carries `N9*IV` per the validator (not re-parsed by me beyond B3-02 presence) | — |
| M01 Fallback (PDF headers, scan line, BOL label, DR header, 214 B10-01, statement row) | KV | CONFIRM | 01-001 l. 847 "Freight bill No: 150235531"; 02-002 p. 46 "FREIGHT BILL NO: 807148067" (render; the text layer has 0 hits for the label, it is image-only); 03-003 p. 11 "LTL INVOICE# 405-677016", scan line "405677016 0180993 8"; 22-012 p. 4 "PRO. NO. 1848869A"; 03-003 p. 14 "PRO NUMBER 405-677016"; 21-004 p. 8 "Pro Number 271-432501"; 19-017 `B10*00902527924*00280740007194473*ODFL`; 21-015 l. 238-258 statement rows; 21-007 p. 4; 21-010 p. 4 | — |
| M01 If none (always present) | KV | CONFIRM, within the sets opened | every bill page I opened carries a PRO (sets 01, 02, 03, 04 OCR, 21, 22; 82/82 210s). Not a universal proof; see §3 | — |
| M02 Fallback (letterhead; statement header) | KV | CONFIRM | 02-002 p. 46 letterhead "SOUTHEASTERN FREIGHT LINES, INC. (SEFL)"; 22-008 p. 4 "Werner Enterprises"; 21-015 l. 196-198 "TForce Freight … Invoice/Statement No:" | — |
| M02 Never (ISA-06 as the carrier) | KV | CONFIRM | 19-033 ISA-06 `BPTS`, B3-11 `WIEL` (§2.0) | — |
| M02 If none | KV | CONFIRM | as above | — |
| M03 Primary (title plus a changed amount or bill-to on a known PRO) | KV | CONFIRM | 02-002 p. 46 "BALANCE DUE INVOICE", PAY THIS AMOUNT 94.00 vs p. 33 "PAST DUE INVOICE", PREPAID 591.10, same PRO; 03-003 p. 11 "*** BALANCE DUE INVOICE ***", p. 19 "*** CORRECTED INVOICE ***"; 01-001: 4 CORRECTED INVOICE bills (my script: 4 bills, 7 occurrences); 21-002 p. 17 footer "ORIGINAL INVOICE" on the 02/18/05 re-bill | — |
| M03 Fallback (B3-08; Estes Adj/BD; DUP / PAST DUE marks) | N | CONFIRM | B3-08 0 of 82; 21-007 p. 4 (my render): column "Adj/ BD" present, blank on all four rows; 21-001 p. 11 and p. 13 "DUP 6/30/08 RP"; 02-002 p. 33 "PAST DUE INVOICE" | as the validator |
| M03 Never (the title alone) | KV | CONFIRM | 21-002 p. 17: "ORIGINAL INVOICE" footer, Invoice Date 02/18/05, PRO DATE 12/03/04, "CBL DGB 2/18/05 … CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER FROM THE 3RD PARTY" | — |
| M03 If none (group every print by PRO) | KV | CONFIRM | 02-002 pp. 33/46 are two prints of 807148067; pp. 28/41 of 806625953 (p. 41 opened; p. 28 per the walk) | — |
| M04 Primary (earliest of B3-06, PDF bill date, "PREVIOUSLY INVOICED ON", Estes statement) | KV + A | CONFIRM, one NARROW on the ADD | 19-001 ST 0001 B3-06 `20121015`; 02-002 p. 46 "DATE BILLED 06/19/2023" (text l. 49 "06/1912023"); 21-002 p. 17 "Invoice Date 02/18/05"; TForce lists recomputed: 8 lists, all newest-first, earliest entry 12, 13, 210, 22, 396, 7, 133, 512 days after the ship date (the validator's figures exactly); UPS 38 lists; 21-007 p. 4 "Freight Bill Date 4/04/24" six days before "Statement Date 4/10/24". ADD re-opened: 22-008 p. 4 "ISSUE DATE: 01/17/2023"; 22-012 p. 4 "INVOICE DATE 02/26/2026"; 22-015 p. 4 "INVOICE DATE: 7/17/2023"; 22-013 l. 200-201 "Invoice Date 04-25-2025"; 21-006 p. 5 "Bill Date" column exists. **But on 21-006 p. 5 "Bill Date" equals "Due Date" on all eight rows** (6/3/2022 / 6/3/2022 … 8/9/2023 / 8/9/2023), 21-45 days after each pickup date, so the column may be the due date relabelled | ADD wording: "YRC statement 'Bill Date' (21-006 p. 5), which equals its 'Due Date' on every row held, so treat it as a bound" |
| M04 Fallback (statement date, flag as late) | KV | CONFIRM | 21-015 l. 238-243 "Invoice Date 08-08-2023" for PROs shipped 2022-23 | — |
| M04 Never (reprint date; ABF and XPO print no bill date) | KV | CONFIRM | 02-002 p. 33 "DATE BILLED 08/26/2025"; `abf.py`: 0 of 101 bills carry any bill-date label (labels present: Shipment Date 107, Shipping Date 107, PAYMENT DUE DATE, PAID AT A LATER DATE, PICKUP DATE 2); XPO 03-003 pp. 4, 11, 19 and 21-005 ll. 197-256 print only "PAYMENT IS DUE BY" | — |
| M04 If none | KV | CONFIRM (rule) | — | — |
| M05 Primary | KV + A | CONFIRM | 01-001 "PAYMENT DUE DATE: 07/19/2024" (p. 2 of the text; also "Upon Receipt" on p. 30); 02-002 p. 46 "PAYMENT DUE DATE 07/04/2023"; 03-003 p. 11 "*** PAYMENT IS DUE BY 02/27/2021 ***". ADD: 21-002 p. 17 "Due Date 03/05/05"; 22-015 p. 4 "PAYMENT DUE: 8/16/2023"; 21-015 p. 33 "Payment Due ON RECEIPT" and the statement l. 243; 22-012 p. 4 prints none ("Terms are 15 Days from Receipt of Invoice") | — |
| M05 Fallback (tariff item + bill date) | KV | CONFIRM | 2023-06-19 + 15 = 2023-07-04 (p. 46); 2021-02-27 − 15 = 2021-02-12 = the ship date (p. 11); and p. 63: 2023-04-07 + 15 = 2023-04-22 = its printed due date | — |
| M05 If none | KV | CONFIRM | — | — |
| M06 Primary (B3-04 + N1*BT) | KV | CONFIRM | 19-001 ST 0001 `B3-04` PP, `N1*BT*DALMATION PRESS LLC` | — |
| M06 Fallback (terms box, bill-to, statement P/C) | KV | CONFIRM | 02-002 p. 46 "PREPAID", p. 63 "THIRD PARTY"; 03-003 p. 12 "US $1,809.93 PREPAID"; 21-001 p. 11 "P/C P"; 21-015 l. 238-243 statement "P/C" column (per the validator; the text shows "Due / Paid" columns and the P/C flag in the row data) | — |
| M06 If none (always present) | N | CONFIRM | 22-015 p. 4 (render) "PPD / COL: UNKNOWN"; bill-to present | as the validator |
| M07 Primary (class column) | KV | CONFIRM | 02-002 p. 46 "CLASS 70.0"; 01-001 "EX70" 58 occurrences (my count 58) | — |
| M07 Fallback (210 L7-07) | KV | CONFIRM | 19-001 `L7*******050`; 19-015 ST 60001 per the validator | — |
| M07 If none (always present on LTL) | N | CONFIRM | 03-003 p. 11 "PLT MISC 0-0 CLASS 100", p. 19 "… MISC 0-0 CLASS 60", 21-005 l. 226 "… 0-0 CLASS 70": XPO's class sits in the description text | as the validator |
| M08 Primary | KV | CONFIRM | 02-002 p. 51 l. 21 "AS WEIGHT 1,000", l. 23 "DEFICIT 214"; p. 60 "AS WEIGHT 2,000 / DEFICIT WGHT 162"; 01-001 l. 976-977 "DEF111 … / AS500" (seen as "ALLOWS LOWER CHARGE AT HIGHER WEIGHT DEF111 90211 1,001.34" over "AS500"). Also XPO prints "AS WEIGHT 2,000" against 1,942 (21-004 l. 359-360), an addition | add "XPO 'AS WEIGHT' (21-004 l. 360)" |
| M08 Fallback (210 L0-04, L3-01, DAA, L0-02) | KV | CONFIRM | 19-001 `L0****650*G`, `L3*650*G`; ST 0002 DAA per the validator and my code count (DAA 11) | — |
| M08 If none | KV | CONFIRM | every LTL bill opened prints a weight | — |
| M09 Primary (rate column, unit by arithmetic) | KV | CONFIRM | 509 × 600.80/100 = 3,058.07 (p. 46); 645 × 733.17/100 = 4,728.95 (01-001 l. 1420); 03-003 p. 11: 660 × 284.22/100 = 1,875.85 | — |
| M09 Fallback (L1-02/-03; Estes LB is per cwt) | KV | CONFIRM | 810 × 298.86/100 = 2,420.77 (19-015 ST 60001). Addition: Estes ST 60003 is a flat bill with `L1-03` = `FR` and no discount or fuel line (walk B; my parse shows the 3 EXLA STs sum 523.69 + 498.16 + 197.00) | add "Estes `FR` = flat (19-015 ST 60003)" |
| M09 Never | KV | CONFIRM (rule) | — | — |
| M09 If none (always present) | N | CONFIRM | 02-002 p. 49: RATE column empty, "MINIMUM FREIGHT CHARGE $1,019.77"; 21-001 p. 11: no rate, "SORTING OR SEGREGATING" 45.00 only | as the validator |
| M10 Primary (line extension) | KV + A | CONFIRM | 02-002 p. 41: 405 × 3.1597 = 1,279.68; 2,315 × 3.1597 = 7,314.71; sum 8,594.39; 2,720 × 3.1597 = 8,594.38 (recomputed) | — |
| M10 Fallback (L1-04 cents) | KV | CONFIRM | 19-001 `L1**40.17*PH*26111` | — |
| M10 If none | KV | CONFIRM | — | — |
| M11 Primary (printed % and $) | KV + A | CONFIRM | 02-002 p. 46 "88.15% DISC 2695.69"; 21-015 p. 33 "84.00% DISCOUNT 84.00 -4,186.64"; 21-002 p. 17 "Discount Allowed: 70.00% 2299.53-". ADD re-opened: p. 49 "GROSS CHARGE IS 1133077 / DISCOUNT PERCENTAGE 9100 / DISCOUNT AMOUNT 1031100": 11,330.77 × 0.91 = 10,311.00; 11,330.77 − 10,311.00 = 1,019.77 = the printed "MINIMUM FREIGHT CHARGE" line (so on p. 49 that label is the net, not a floor lift) | add to the ADD: "its 'MINIMUM FREIGHT CHARGE $1,019.77' equals gross − discount" |
| M11 Fallback (L5 text; derived) | KV | CONFIRM | 19-009 `LESS 78.00 PCT DISCOUNT`, 19-015 `DISCOUNT 84.0%` (L5 texts listed by my parse); 188.00 ÷ 261.11 = 0.7200; 03-003 p. 11 "XPO LOGISTICS DISCOUNT SAVES YOU ($468.96)"; 21-005 l. 227 "-$534.01" | — |
| M11 If none | KV | CONFIRM | — | — |
| M12 Primary | KV | CONFIRM, and the two assumed markers now verified | 01-001 l. 1072 "ABSOLUTE MIN CHARGE ADJUSTMENT MCADJ ADJ 76.64" (44 occurrences); 02-002 p. 94 "MIN FRT CHG 3454.14". The validator left XPO "M" and TForce "MIN" *assumed* (its §7 item 7): **TForce "MIN" is at 21-015 l. 284** ("65 640000-07 125 MIN 602.94") and **XPO "M" is on 03-003 p. 4** (712-591246, RATE column "M", $680.11 at 200 lb; my render) | the validator's §7 item 7 is closed |
| M12 Fallback (MMC) | KV | CONFIRM | code count MMC 1 (19-010) | — |
| M12 If none | KV | CONFIRM | 362.38 > 152 | — |
| M13 Primary | KV | CONFIRM | 01-001 "FSC 30.3% 54.54" (p. 30), "FSC 30.3% 221.55" per the validator; 02-002 p. 46 "LTL FUEL SURCHARGE OF 22.00%" in the description, 79.72 unlabeled in the charges column | — |
| M13 Fallback | N | CONFIRM | §2.0 | — |
| M13 If none | KV | CONFIRM | — | — |
| M14 Primary | KV | CONFIRM | 01-001 p. 30 "CALIFORNIA COMPLIANCE SURCHARGE CCS 22.00", "SPECIAL HANDLING SERVICES - LUMPER SHDL/44"; 03-003 p. 11 "CBR", p. 19 "APT APPOINTMENT $51.90", "LP1…"; 21-015 l. 589-591 "005000 NOTIFICATION CHARGES 50.00", "002800 LUMPER CHARGE / DST"; 02-002 p. 46 "LIFTGATE SVC", "PVT RESIDEN"; 21-002 p. 17 "CORRECTED BILL OF LADING CHARGE"; 21-001 p. 13 "CALL 72HRS IN ADV FOR DEL APPT 7.50" | — |
| M14 Fallback (L1-08 codes) | N | CONFIRM | my code set equals the validator's to the unit (§2.0) | as the validator |
| M14 If none (uncoded ODFL lines) | KV | CONFIRM | ODFL L1 lines with no rate and no code: `2400` ×3, `1100` ×3 | — |
| M15 Primary | N | CONFIRM | §2.0; plus 03-003 p. 11 "CBR REWEIGH OF SHIPMENT FEE $37.25", 21-002 p. 17 "CORRECTED BILL OF LADING CHARGE 15.00". Addition: XPO's delivery receipts also print the fee line by name (03-003 p. 14, 21-004 p. 8 "CBR REWEIGH OF SHIPMENT FEE", no amount) | add "the XPO DR echoes the fee name without an amount" |
| M15 Fallback (210 coded line) | KA | really untestable on `data/` | no L1-08 code or L5 text in the 82 real 210s names a reweigh, inspection or corrected-BOL fee (my parse searched L5 for REWEIGH / INSPECT / CORRECT / W&I: 0; L1-08 codes RWF / INS / CBL / REW: 0) | — |
| M15 If none (always printed when charged) | KA | untestable; one observation | ABF's 28 bills with "W02/AUTH:Reweigh" print no reweigh-fee line at all (my scan: 0 fee-like lines; the only hit is a PQ number containing "RWF"), so at ABF a reweigh can be billed with no fee line; whether a fee was charged elsewhere cannot be read | — |
| M16 Primary (B3-07 = L3-05) | KV | CONFIRM | 82 of 82 (§2.0) | — |
| M16 Fallback (PDF total labels) | N | CONFIRM | 02-002 p. 46 TOTAL 591.10 / PAY 94.00; p. 41 1088.74 / 110.23; **p. 63 (corrected print) PAY THIS AMOUNT 483.15 = TOTAL 483.15**, which supports the narrowed wording; 21-002 p. 17 "PAY THIS AMOUNT 1133.55"; 01-001 "TOTAL AMOUNT DUE BY $299.27" | as the validator |
| M16 Never (SEFL 2020 PAY = base + 25%) | KV | CONFIRM | p. 49: 647.55 × 0.25 = 161.89, 647.55 + 161.89 = 809.44, 647.55 not printed; p. 60: 139.69 × 0.25 = 34.92, 139.69 + 34.92 = 174.61 | — |
| M16 If none | KV | CONFIRM | column sums reproduce on pp. 41, 46, 60, 63, 94; 03-003 pp. 4, 11, 19; 21-002 p. 17; 21-001 p. 13; 22-008 pp. 4, 7, 10; 22-012 p. 4; 22-015 p. 4 (all recomputed) | — |
| M17 Primary | KV | CONFIRM | 03-003 p. 12 "AMOUNT PAID: US $162.90 / BALANCE DUE: US $1,809.93"; 02-002 p. 46; 01-001 l. 6185-6187 "corrected on 07/30/2024. The original total charge was $ 326.60. The correct charge is $ 300.52, a reduction of $ 26.08". Addition: the TForce reprint list prints the amount of each earlier print, and on 546903626 the 05/02/23 entry reads 2369.67 against 1118.82 on the 05/09/23 entry (21-015 p. 33), so the list is also a source for the amount previously billed; and Mode's statement prints "Original Amount" beside "Open Balance" (21-014 p. 4: 3,698.75 / 745.09) | add both as M17 fallbacks |
| M17 Fallback | KV | CONFIRM | 21-010 p. 4 "528.19- … 72.00"; 21-001 p. 7 "698.33 … 662.90- … 35.43"; 21-002 pp. 13, 15; 1,088.74 − 110.23 = 978.51 | — |
| M17 If none (customer's AP record) | KA | really untestable | sets 09, 21-24 swept for remittance / voucher / AP export: none is a shipper's AP record (the hits are a consignee's debit memo and check stub, 21-002 pp. 8-9, and a 3PL's claim form, 23-011) | — |
| M18 Primary | KV + A | CONFIRM | 01-001 l. 893 "W02/AUTH:Reweigh - See W&R certificate for details.// FUEL", 28 bills (the validator wrote "29 bills": 29 occurrences on 28 bills); 02-002 p. 46; 21-002 p. 17; 21-015 p. 33 "*** SHIPMENT REWEIGHED ***". ADD re-opened: 21-015 p. 33 "WAIVED INSPECTION", "04424-DTR ORIGINAL WGT/REWEIGH", "SHIPMENT WEIGHED AT DTR.", "537.33 CUBIC FEET", "12 LINEAR FEET", "SEC7 DEFAULT"; 21-001 p. 11 "FBA DHE 8/08/07 FREIGHT BILL AUDIT", "CAB SRS 11/02/07 CORRECT AS BILLED", "ADDED SSC PER DR", "ODFL 6100 ITEM 158508 WITH ODFL 660", "ITEM 887 SORT AND SEGREGATE CHARGE PER"; p. 12 "W & I REWEIGH CORRECTE WEIGHT 1070 LBS"; 02-002 p. 60 "DELIVERED TO A PRIVATE RESIDENCE", "PYLE CORR REPT 428"; 01-001 l. 896 "W01/AUTH:Restore original weight//" (10 bills), l. 883 "RATE DETERMINED BY RATEWARE", l. 881 "ALLOWS LOWER CHARGE AT HIGHER WEIGHT" | "28 bills" |
| M18 Fallback (K1; Estes L5 remarks) | KV | CONFIRM | K1 0 of 82; 19-015 ST 60003 `L5*1*LEFT MSG FOR DEL APPT 11/14/13` | — |
| M18 If none | KV | CONFIRM | 0 K1, 0 NTE; 02-002 p. 63 (CORRECTED, no remark) and p. 41 (weight raised, no remark) | — |
| M19 Primary | KV | CONFIRM | 02-002 p. 46 "*LIFTGATE DELIVERY", "QUOTE #CWEN3E465", p. 41 "CL150 NMFC 49880-"; 01-001 l. 879 "CL 100 ITEM 057300-03V", l. 888 "DO NOT BREAK DOWNPU 3-5PSFB FAX"; 21-001 p. 13; 21-002 p. 17 "NMFC #156600 S7 92.5 / OVER 15 DENS" | — |
| M19 If none (not on 210s or XPO bills) | N | **NARROW the narrowing** | AAA Cooper's L5 texts are only "BOOKS, NOI NMFC 161630" (with piece counts) plus the discount and fuel texts. **Estes's L5 carries more:** `LEFT MSG FOR DEL APPT 11/14/13` and, in the same ST 60003 just before it, a contact-like line of a first name and a number (not transcribed), between `LX*1` and `L7`; so at Estes an instruction or contact echo in L5 cannot be excluded. XPO: 03-003 p. 20 "CALL 48HRS IN ADVANCE FOR DELIVE[RY] …", and the class inside the description | "Not on ODFL 210s; AAA Cooper's L5 carries the description and NMFC only; Estes's L5 also carries remarks and a contact-like line (19-015 ST 60003); XPO bills echo the class and, on 326-343835, the appointment instruction (03-003 p. 20)" |
| M20 Primary | N | CONFIRM | 02-002 p. 46 "QUOTE #CWEN3E465", "CUSTOMER NUMBER 071-003454"; `abf.py`: PQ SCHEDULE NO on 82 bills, 82 distinct, "Tariff: AOD000" on 101, "AU=ABF646-468646" on 101 (205 occurrences), "Account No: 468646-0005"; 21-005 l. 219 "QN# 89.8DZ32430239999999999999"; 21-002 p. 17 "TARIFF 559"; "TARIFF CNWY-199" only on the DR footers (03-003 p. 14, 21-004 l. 319 and p. 8), the bills say "TARIFF 199" (03-003 p. 11, 21-005 l. 241) | as the validator |
| M20 Fallback (L7, N9) | KV | CONFIRM | 19-009 `L7*1*CZAR*910…`; 19-001 `N9*PO*21838107023`; TL N9 qualifiers per the validator | — |
| M20 If none | KV | CONFIRM | — | — |
| M21 Primary | KV | CONFIRM | 02-002 p. 46 "1 of 1"; 21-002 p. 17 "Page 1 of 2" / "Page 2 of 2"; 21-001 p. 11 "Page No 2"; 03-003 p. 11 "( continued on next page )", p. 12 "page 9" | — |
| M21 Fallback (no counter: group by PRO) | KV | CONFIRM | `abf.py`: the only "Page x of y" strings on ABF bill pages are court stamps; 6 two-page bills (165526565, 165551769, 165551775, 165261918, 165261921, 165407196) | — |
| M21 Never (SEFL "1 of 3") | N | CONFIRM | p. 49 "1 of 3", p. 60 "1 of 30", different PROs (renders); AV review ll. 49-51, 102, 245 had already narrowed it | as the validator |
| M21 If none | KV | CONFIRM | — | — |
| M22 Primary (TForce / UPS reprint list) | KV | CONFIRM | sweep of every derived text and OCR: "PREVIOUSLY INVOICED" only in 04-006 (17), 04-007 (21), 21-015 (8). The only other reprint banner in `data/` is "- REPRINTED COPY -" on a shipper's BOL / packing-slip supplement (21-012 ll. 327, 348, 370), a phase-2 paper, not a carrier bill | — |
| M22 Fallback (statement rows) | KV + A | CONFIRM; ADD narrowed as under M04 | 21-007 p. 4; 21-006 p. 5 | see M04 |
| M22 If none (not printed by SEFL, ABF, XPO, ODFL) | KV | CONFIRM | 0 hits in 02-002, 01-001, 03-003, 21-004, 21-005, 21-001, 21-002 (renders of the ODFL pages show "DUP 6/30/08 RP" instead) | — |
| M23 Primary | KV + A | CONFIRM | 22-008 p. 4 "DELIVERY DATE - 01/13/2023"; 22-012 p. 4 "DATE DELIVERED 02/24/2026"; 22-015 p. 4 "DELIVERY DATE: 7/11/2023"; 19-009 B3-10 `035`; ADD: 22-013 l. 212-213 "Pick Up Date Delivery Date 01-21-2025 01-23-2025"; B3-10 `035` on 46, blank on 2 (my parse) | — |
| M23 Never (017 as actual) | KV | CONFIRM | 34 of 34 ODFL `017` | — |
| M23 If none | KV | CONFIRM | — | — |
| M24 Primary | KV + A | CONFIRM | 21-015 l. 238-258; 21-010 p. 4; 21-001 p. 7; 21-007 p. 4; 21-014 p. 4 "Annual Interest Rate: 18%", "Terms: Net 30", "Signed Agreement on File: No". ADD re-opened: 22-011 l. 206-212 (Adjusted_Amount, Applied_Amount, Credited_Amount, Balance, Days_Past_Due, Load Number; row 3341783401 … 0 875 0 450.00 176 33417834); 21-006 l. 205-220 (codes "DEF AS IDIS REWT PRNT FSC", "Age Bill Date Due Date Tariff # (PrePaid) P/C Pickup Date"); 21-013 l. 433-435 (Type A/I, "RDWY349533831X"); 04-005 ("Invoice Number Invoice Date Invoice Amount Invoice Due Payment Amount Balance"; one row 563067842 with Payment Amount $93.91, Balance $28.22); 21-002 p. 10 (consignee's statement 186 of 02/06/2005 with aging) | — |
| M24 Fallback (carrier portal) | KA | untestable as a print; bills name the portal | 23-006 p. 5 is a claim-status page; XPO bills "VISIT OUR WEBSITE at ltl.xpo.com/billing" (21-004 l. 209); Holland / New Penn / YRC statement footers "All supporting documents available at www.hollandregional.com", "online bill pay available at www.yrcfreight.com", "go to www.YRCFREIGHT.com, click 'Manage' tab and click 'Report an Issue'" (21-006 ll. 316, 520, 579, 591) | optional: "bills and statements name the portal (XPO, Holland, New Penn, YRC) but no statement print from one is held" |
| M24 If none | KA | really untestable | as M17 If none | — |
| M25 Primary | N | CONFIRM | R3 rows in §2.0; the five NEMF shares are 12698/32560, 5031/12900, 11188/28687, 44150/113205, 34104/87446 = 0.390 each | as the validator |
| M25 Fallback | N | CONFIRM | 02-002 p. 33 "SEFL 34844332 OAKH" in the ORG C/L, C/L PRO NO and DEST C/L boxes; p. 41 DEST C/L "DAFG"; p. 63 and p. 94 "PYLE"; p. 60 "PYLE CORR REPT 428" is a remark line in the description column of SEFL's own bill, boxes blank; 21-015 l. 275 "ADV SCAC PRO# DATE BEY SCAC" header, blank; 21-002 p. 17 ORIG I/L / DEST I/L blank | as the validator |
| M25 If none (carrier) | KV | CONFIRM | no PDF prints a share; set 24's text layer shows interline balances only as claim totals ("Interline Freight Charges", "Offsetting Interline Freight Charges of $39,343.35", 24-002 ll. 111, 160), nothing per PRO | — |

### §2.2 The validator's §2 ledger, §2.4 dispute cells

| Validator row | Val. | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| D01 Primary | KV (rule) | CONFIRM | the three inputs re-opened and the dates recomputed: 2023-06-19 + 180 = 2023-12-16; 2023-05-05 + 180 = 2023-11-01; 2023-05-15 + 180 = 2023-11-11 | — |
| D01 Never (reprint date) | KV | CONFIRM | p. 33 "DATE BILLED 08/26/2025" | — |
| D01 If none | KV | CONFIRM | — | — |
| D02 Primary | KV | CONFIRM | 23-006 p. 4 (render): claimant, "Our Claim Number: SATCO-2300008OC", ship date, two PROs, Billed / Paid / Correct / Overcharge columns, "Duplicate Bill 03/28/2023 Keying error resulted in duplicate payment", "Date Submitted 03/28/2023", indemnification clause, "Claim Tariff Contract Authority :" blank; 23-003 p. 5 and 23-004 p. 4 letters (PRO, BOL, nature, no amount, no date); set 16 forms: "BOND OF INDEMNITY" at ABF l. 59, Averitt l. 37, FedEx l. 72, R+L l. 8; "Nature of overcharge" ABF l. 27, FedEx l. 34, South Bay l. 34, YRC l. 21; "paid freight bill" on all; SF 1113 (20-001) PAID DATE l. 5, CARRIER'S BILL NUMBER l. 11, SCAC l. 16, DIFFERENCES / AMOUNT l. 28, AMOUNT VERIFIED l. 33, TOTAL CLAIMED l. 38; 20-003 ll. 28-30 "(a) The transportation document. (b) An explanation for the claim. (c) Any additional supporting" | — |
| D02 Fallback (worksheet row) | KV | CONFIRM | 02-002 p. 99 l. 7 header "CUSTOMER INV DATE PLT LIFTGATE SURCHARGE FRT CHARGE Need to Be Charged OVER CHG"; p. 210 l. 18 row 364 "807148067 5/15/2023 1 $ 55.00 $ 79.72 $ 362.38 $ 152.00"; p. 212 l. 6 "OVER CHG"; p. 223 l. 19 "364 $ 210.38" | — |
| D02 If none | KV | CONFIRM | — | — |
| D03 Primary | KV | CONFIRM | 23-004 p. 4 letter names "the attached Shippers Weight Certificate and Packing Slip/Inventory"; 23-003 p. 5 satellite image; 23-006 p. 4 boxes unticked (the certificate page 23-004 p. 8 itself was not re-opened by me; its figures are F-scope) | — |
| D03 Never (brochure / sample BOL) | KV | CONFIRM | 16-095 ll. 36-37 | — |
| D03 If none | KV | CONFIRM | no carrier certificate behind any reweigh in the six chains (walks A-D; my renders of 03-003 p. 12, 02-002 p. 41, 21-001 p. 13) | — |
| D04 Primary | KV | CONFIRM | 23-006 p. 4 "Date Submitted 03/28/2023"; p. 5 "Date Received: 03/28/23"; letters undated | — |
| D04 Fallback (e-mail headers, portal) | KV | CONFIRM | 21-002 p. 11 "Sent: Tuesday, March 01, 2005 9:17 AM" (the page carries personal names and e-mail addresses; none copied); 23-006 p. 5 is a web page print ("Results of Inquiry", "Go Back") | — |
| D04 If none | KV | CONFIRM | — | — |
| D05 Primary | KV | CONFIRM | 23-006 p. 5 "This claim is in APPROVED status … Draft Number 1385879"; 23-003 p. 5 "declined per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse" | — |
| D05 Fallback (ODFL refund-and-re-bill history) | KV | CONFIRM | 21-002 p. 11 "did receive the full refund … This is now billing to you for $1133.55"; pp. 13, 15 | — |
| D05 If none | KV | CONFIRM | 23-006 p. 5 prints Date Received 03/28/23, Draft Date 06/20/23, "sent to the claimant on 06/20/23", no decision date or reason; 21-012's "CREDIT MEMO" (l. 475) is a sales document ("No post audit claims accepted" l. 405, "SALES MAN / SALES OFFICE / SALES ORG / VENDOR" l. 381) | — |
| D06 Primary | KV | CONFIRM | 23-006 p. 5; 21-002 p. 13 "2/15/05 REF OPAY … 1,828.04", p. 15 "2/26/05 REF OPAY … 584.63" | — |
| D06 Fallback | KV | CONFIRM | 21-013 l. 434 "A 15831 11/30/2021 … $ (301.94)"; 22-011 l. 206 "Adjusted_Amount Applied_Amount Credited_Amount" | — |
| D06 If none | KV | CONFIRM | — | — |
| D07 Primary (AP export or remittance) | KA | really not held | see M17 If none | — |
| D07 Fallback | KV | CONFIRM, one addition | 21-002 p. 13 "1/27/05 CP CC … 2,412.67-", p. 15 "4/11/05 CP LBHP 76652 72671 1,133.55- LOCKBOX RECEIPT"; 03-003 p. 12; 21-010 p. 4; 23-011 l. 208-210 "Invoice Amount Paid 864.92", "Check Number EFT000000010881" **and "Date Invoice Paid 01/25/2023"**, so the 3PL form carries the paid date too | add "Date Invoice Paid" |
| D07 If none (never public) | N | CONFIRM | 21-002 p. 8 debit memo ("THIS IS TO CHARGE BACK THE VENDOR FOR FREIGHT PAID BY WINN-DIXIE ON A PREPAID DELIVERY PURCHASE ORDER (550038) THAT WAS SENT FREIGHT COLLECT IN ERROR. REFER TO OLD DOMINION #02902161435", $2412.67, 01/26/2005); p. 9 check stub (Check No. 007451329, 11.Feb.2005, "ACC186834 … -2,412.67 … AR CR VOUCHER", 12,427.40 + 12,427.40 − 2,412.67 = 22,442.13); 23-011 l. 208-210 | as the validator |
| D08 Primary | KV | CONFIRM | 02-002 p. 99 header, p. 210 row, p. 223 value | — |
| D08 Fallback (TQL ledger) | KV | CONFIRM | 23-010 p. 6 "EXHIBIT A", "275,915.66"; pp. 16-17 reasons counted: reweigh 13, reclass 11, Liftgate 9, corrected invoice 4, limited access 2, TONU 2 + "TONU paid twice" 1, "duplicate invoice" 1, "alleged residential delivery" (ll. 602, 654) and "alleged residential pickup" (l. 618), "TQL not paying party" 1, "load not delivering" 1 | — |
| D08 If none | KV | CONFIRM | — | — |

### §2.3 The validator's §3 (the §1 columns for M01-M25, D01-D08)

The validator's test was AK §3.2's "Data needed" column (ll. 136-177). I re-read it.

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| M18 Need "must on a correction" | N | CONFIRM | §1 l. 67 defines must as "no DISPUTE verdict on the lines it feeds without it"; §4.6 l. 388 issues "Flag: unexplained change" when M18 is missing; `doc-explanation.md` l. 196 says "If neither has it, ask the reviewer". Two real corrections carry no reason (02-002 pp. 41, 63, my renders). The validator's "useful, and its absence is itself a flag" fits §4.6; the conflict with doc-explanation is real and unresolved |
| M25 Checks "A3, A5" | N | CONFIRM | AK l. 139 A3 "AP payment records; 3PL invoices; carrier statement"; l. 141 A5 "BOL freight-terms box and bill-to; PO or vendor freight terms; entity list": neither names an interline partner or share |
| D06 Checks "credit matching" | N | CONFIRM | no AK check carries that ID; A3 (l. 139) and F1 (l. 166) are the nearest |
| D08 Checks "context" | N | CONFIRM | not an AK ID |
| M01-M17, M19-M24 Checks / Role / Need (KV) | KV | CONFIRM | A2 l. 138 "PRO, BOL, carrier, amount, dates"; A4 l. 140 "EDI B308 code or 'CORRECTED'; original bill date"; F1 l. 166 "Due dates, pay dates, late-fee rule"; A5 l. 141; B4 l. 147 "FAK table; BOL class and NMFC item"; C1 l. 157 "BOL weight, class, dims; W&R certificate; spec sheet"; B3 l. 146; B2 l. 145 "discount; class; weight; lane"; A1 l. 137 "Invoice"; B8 l. 151, B9 l. 152 "Invoice"; D1 l. 154 "Accessorial schedule and waivers"; C2 l. 158 "Tariff thresholds"; A7 l. 143 "Quote number, agreement ID, account"; E1 l. 163 "POD date and time"; A3 l. 139 "carrier statement"; G1 l. 175, G2 l. 176 "Claim dates … acknowledge in 30 days, decide in 60". Each row's Role and Need read as the validator says |
| D01-D05, D07 columns (KV) | KV | CONFIRM | G1 l. 175 "Carrier tariff, contract, statute"; the set 16 forms' required fields (my grep above); C1 l. 157 and the forms' attachment lists; G2 l. 176; A3 l. 139 "AP payment records", F1 l. 166 "pay dates", A2 l. 138 |

### §2.4 The validator's §4.1 (§2.5 join keys)

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| PRO first (strip dashes, prefixes, check characters, suffixes, zeros) | KV | CONFIRM | 21-002 p. 6 label / p. 17 "02902161435" vs pp. 13, 15 "2902161435"; 03-003 p. 11 "405-677016" / "405677016"; 21-006 l. 205-207 "648-358429-6", "670-438395-X"; 21-013 l. 435 "RDWY349533831X"; 22-012 p. 4 "1848869A"; 22-015 p. 4 "ORDER #: 8065404" / "8065404A"; 22-011 l. 212 "3341783401" with "Load # 33417834" (l. 818); 23-006 p. 4 "689201498" / "6892014980" |
| then BOL (split "63387,63388"; tokenise) | KV (BOL part KA) | CONFIRM, and the KA part verified | 22-013 l. 213 "502464982\|IDB61769\|954", l. 258 "Bill of Lading Number: 502464982"; **19-018: `B10*47936549*63387,63388*WTVA` and `L11*63387,63388*BM`** (the validator had not re-opened it) |
| then PO + ship date + consignee; TL load / tender, trailer + pickup date | KV (rule) | CONFIRM | the Werner pair is separable only by tractor / trailer / dispatch (22-008 pp. 7, 10); 22-012 p. 4 "REF 1071942" = rate con load number per the walk |
| Never amount + date (23 of 101 ABF) | KV | CONFIRM | `abf.py` on AMOUNT DUE + Shipment Date: 9 groups, 23 bills; ($256.54, 08/07/2024) = 165551759, -768, -771, -773, -774; ($299.27, 08/07/2024) = 165551756, -761, -762, -769; ($299.27) also on 07/31, 08/01, 08/02 pairs; ($256.72) on 07/24 and 07/29 pairs; ($151.88, 07/24/2024) pair; ($256.54, 08/02/2024) pair |
| two TQL pairs and one Werner pair | N | CONFIRM, one addition | §2.0: TQYL; the four TQYL bills also share one invoice date (20251215) |
| rate con "Bill of Lading Number" = SID | KV | CONFIRM | 22-012 l. 488 "Bill of Lading Number: 76930091", l. 438 "PO Number: 4505279147" (walk C: BOL p. 5 "Bol Number 4505279147", "SID#76930091"; p. 5 not re-opened by me) |
| Werner "RETURN" vs BOL 104310 | KV | CONFIRM, extended | 22-008 p. 4 "SHIPPER NUMBER RETURN", trailer 64082, pickup 01/13/2023, 33000 lb; pp. 7 and 10 also print "RETURN" (my renders); BOL p. 5 "104310" per the validator (not re-opened) |
| forwarder booking number as BOL | KV | CONFIRM | 21-006 l. 237 "9/12/2022 T N1883348HKG …", l. 444-445 "BL N1883348HKG / PO AUG 2022" |
| child PROs per pallet | KV | CONFIRM, one note | 21-004 l. 306 "CHILD PRO #'s: 2346-563892, 2346-563870, 2346-563881, 2217-432501, 2346-563866" is in the text layer of the DR; on the rendered p. 8 that line sits under a redaction box (the text survives beneath it), a trap for any pipeline that trusts the image |
| TForce billing advice | D | CONFIRM | §2.0 |

### §2.5 The validator's §4.2 (§3.1 rows, §3.2-§3.3 bullets, §3.4 derivations)

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| §3.1 "Original total on a correction" | KV | CONFIRM | 326.60 − 300.52 = 26.08 (01-001 l. 6185-6187); 03-003 p. 12; 02-002 p. 41: 1,088.74 − 110.23 = 978.51 |
| §3.1 "Bill type" | KV (one N) | CONFIRM | 21-002 p. 17; 02-002 pp. 33 / 46; B3-08 0/82; the Estes Adj/BD column is empty (21-007 p. 4) |
| §3.2 M18 | KV | CONFIRM | K1 0, NTE 0; pp. 41, 63 no reason |
| §3.2 M22 | KV | CONFIRM | the sweep (§2.1 M22) |
| §3.2 D05 "nothing on the bill side records it" | N | CONFIRM | 21-002 p. 17 "CBL DGB 2/14/05 … PER LETTER FROM THE SHIPPER", "CBL DGB 2/18/05 … PER LETTER FROM THE 3RD PARTY": a re-bill recording accepted correction requests |
| §3.3 D07 "never public" | N | CONFIRM | 21-002 pp. 8-9, 13; 23-011 l. 208-210 |
| §3.4 Discount % 72.0% | KV | CONFIRM | 188.00 ÷ 261.11 = 0.7200 |
| §3.4 Fuel % 17.5% | KV | CONFIRM | 12.79 ÷ 73.11 = 0.1749 |
| §3.4 Original total 978.51 | KV | CONFIRM | 1,088.74 − 110.23 |
| §3.4 Original weight 2,430 lb | KV | CONFIRM | 744.77 ÷ 0.097 ÷ 315.97 × 100 = 2,430.0; the 744.77 is the worksheet's figure (p. 208 per the walk; p. 41 prints 2,720 only, my render) |
| §3.4 Amount paid $150.00 | KV | CONFIRM | 21-005 l. 233-235: 1,301.48 total, AMOUNT PAID 150.00, BALANCE DUE 1,151.48 |
| §3.4 Rate unit "60080" | KV | CONFIRM | 509 × 600.80 / 100 = 3,058.07 |
| §3.4 Deficit weight 167 lb | KV | CONFIRM | 1,000 − 833 = 167; 167 × 36.2 / 100 = 60.45 (19-001 ST 0002 DAA per the validator; DAA code count 11 in my parse) |
| §3.4 TL fuel per mile $0.61 | KV | CONFIRM | 22-008 p. 4 "FUEL ADJ/MILEAGE 93.94", "MILES 154"; 93.94 ÷ 154 = 0.610 |
| §3.4 First bill date bound 03/15/23 | KV | CONFIRM | 21-015 ll. 297-298 "06/07/23 R1679027 818.19 / 03/15/23 33492586 818.19"; ship 03/03/2023; 12 days |

### §2.6 The validator's §4.3 (§4.5 points 2, 3, 5; §4.6 rows)

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| §4.5 (2) 2023-12-16 and 2023-11-01; 2025 reprints give none | KV | CONFIRM | recomputed; p. 33 is a reprint ("DATE BILLED 08/26/2025", "INVOICE PENDING", PREPAID 591.10) |
| §4.5 (3) 896789802 corrected 452 days after shipment, no reason, no first-bill date | KV | CONFIRM | p. 63 (render): CORRECTED INVOICE, SHIPMENT DATE 01/10/2022, DATE BILLED 04/07/2023, PAYMENT DUE 04/22/2023, no remark (the page prints only an "ATTENTION OF" first name, not copied); 2023-04-07 − 2022-01-10 = 452 |
| §4.5 (5) first bill date NOT REPORTED on SEFL / XPO corrected prints and ABF | KV | CONFIRM | pp. 41, 63 carry only their own DATE BILLED; XPO prints none (03-003 pp. 4, 11, 19; 21-005); ABF 0 of 101 |
| §4.5 worked numbers | KV | CONFIRM | 06/19 + 15 = 07/04/2023; 05/15 + 180 = 11/11/2023 |
| §4.6 M04 | KV (rule) | CONFIRM | the TForce ages (133-512 days on 4 of 8) |
| §4.6 M18 | KV (rule) | CONFIRM, with the §6 conflict standing | p. 41: derived old total 978.51, new 1,088.74, no reason |
| §4.6 D05 | KV | CONFIRM | 23-006: received 03/28/23, draft 06/20/23 = 84 days |
| §4.6 D07 | KV (rule) | CONFIRM | no AP export held |

### §2.7 The validator's §4.4 (the M and D rows of the six chains)

| Validator row | Val. | Mine | Evidence |
|---|---|---|---|
| A M01-M03 | KV | CONFIRM | pp. 33, 46 renders |
| A M04, M05 | KV | CONFIRM | p. 46 render; text ll. 44-49 garbled as the validator quotes |
| A M07-M16 | KV | CONFIRM | 3,058.07 × 0.8815 = 2,695.69; 362.38 × 0.22 = 79.72; 362.38 + 55 + 94 + 79.72 = 591.10 |
| A M17 | KV | CONFIRM | p. 210 l. 18 row 364 "$ 55.00 $ 79.72 $ 362.38"; 362.38 + 55 + 79.72 = 497.10 |
| A M18 | KV | CONFIRM | p. 46 two lines "** PER GOOGLE EARTH THIS IS A PRA / DLVY" |
| A M22 | KV | CONFIRM | p. 33 |
| A M25 | KV | CONFIRM | p. 46 DEST C/L "OAKH", C/L PRO NO blank; p. 33 "SEFL 34844332 OAKH" |
| A D01 | KV | CONFIRM | recomputed |
| A D02, D08 | KV, one N | CONFIRM | p. 210 l. 18; p. 223 l. 19; the "OVER CHG" header is on p. 212 l. 6 and on p. 99 l. 7 (the row-1 header line carries both "Need to Be Charged" and "OVER CHG"); "$271,828.70" ×3 in the text |
| A D04, D05 (complaint ¶9) | KA | could not test beyond the walk | not re-opened by me either; the walk reports "p.7 ¶9 'demanded … SEFL refused', undated" |
| A D07 | KV | CONFIRM | derived 591.10 − 94.00 |
| A sibling 806625953 | KV + A | CONFIRM | p. 41 render: every value as listed; DEST C/L "DAFG"; "CL150 NMFC 49880-" and "CL125 NMFC 49880-" both "CLASS 70.0"; no remark |
| A bill 806266163 (p. 94) | KV | CONFIRM | p. 94 render: three CLASS 150.0 articles 1893 / 4581 / 2446 (= 8,920), "T 1090C 610-100 1548.75 CF 5.76 PCF / AW 8920 CW 9292.5", "MIN FRT CHG 3454.14", "**SEFL W&I INSPECTED TO A CUBIC CAPACITY MOVE", "Gross Charge is $ 27523.00 / Discount Percentage % 87.45 / Discount Amount $ 24068.86", "PVT RESIDEN 575.00", 828.99, TOTAL 4913.13, PAY 2694.85, DEST C/L PYLE; all recomputed |
| B M03 | KV | CONFIRM | p. 11 |
| B M04 | KV | CONFIRM | 02/27 − 15 = 02/12/2021 |
| B M07-M16 | KV | CONFIRM | 1,406.89 + 365.79 + 37.25 = 1,809.93; 1,809.93 × 0.015 = 27.15 |
| B M17 | KV | CONFIRM | p. 12 |
| B M21 | KV | CONFIRM | p. 11 "page 8", p. 12 "page 9" |
| B M25 | KV | CONFIRM | p. 14 ORIGIN NPB, DESTINATION NRM, ADVANCE / BEYOND blank |
| B D02, D04 (Form 410 pp. 1-3) | KA | could not test | not re-opened by me; catalogue and the walk agree on 10/13/2022 and $14,879.18 |
| B sibling 326-343835 | KV | CONFIRM | pp. 19-20 renders: 1,425 × 131.87/100 = 1,879.15; −469.79; FSC 30.75% 433.38; CBR 39.40; APT 51.90; LP1-LP5 29.01 ×5; TOTAL 2,079.09 incl. late fees; no amount-paid line; "PAYMENT IS DUE BY 12/16/2021" = SHIPMENT DATE |
| C P01, M06 | KV | CONFIRM | 19-001 ST 0001 |
| C P04/M11, P12/M13 | KV | CONFIRM | 12.79 ÷ 261.11 = 4.9% |
| C M01, M02 | KV | CONFIRM | ISA-15 `T` (catalogue "ISA15=T test flag" for 19-001); 19-017 B10 |
| C M03 | KV | CONFIRM | B3-08 empty; no N9 of an earlier bill |
| C M04 "20 days after delivery" → 18 | N | CONFIRM | B3-06 20121015; 214 D1 20120927; 18 days; 20 days is the count from the pickup 20120925 |
| C M07, M08, M10, M16 | KV | CONFIRM | 261.11 + 12.79 − 188.00 = 85.90 = B3-07 8590 |
| C M18, M19 | KV | CONFIRM | ODFL 34 STs: 0 L5, 0 NTE, 0 K1 |
| C M21 | KV | CONFIRM | `SE*25*0001`; 5 STs in 19-001 |
| C M23 | KV | CONFIRM | 34 of 34 `017` |
| C M25 | KV | CONFIRM | `R3*ODFL*O****00902527924*20121015`; 19-009 ST 0014 NEMF |
| C contrasts | KV (one KA) | CONFIRM; KA now verified | 980 BT1 total 1,218.85 = 523.69 + 498.16 + 197.00 |
| D M01 | KV | CONFIRM | p. 17 "02902161435"; pp. 13, 15 "2902161435" |
| D M03 | KV | CONFIRM | p. 17; 2005-02-18 − 2004-12-03 = 77 |
| D M04 | KV | CONFIRM | p. 17; p. 8 DATE 01/26/2005 |
| D M06-M16 (Col/Ppd P) | KV, one N | CONFIRM | p. 17 column header "PREPAID", "BILL-TO # 76652", no "Col/Ppd"; pp. 13, 15 header "Col/Ppd: P"; 24.72 × 132.89 = 3,285.04; × 0.7 = 2,299.53; 133.04 ÷ 985.51 = 0.1350; 985.51 + 133.04 + 15 = 1,133.55 |
| D M17, M24, D06, D07 | KV | CONFIRM | pp. 13, 15 renders: 1/27/05 CP CC 2,412.67-; 2/14/05 RATE AR 2,412.67- and 584.63; 2/15/05 REF OPAY 1,828.04; 2/18/05 RATE AR 584.63- and 1,133.55 (balance 548.92); 2/26/05 REF OPAY 584.63; 4/11/05 CP LBHP 1,133.55- "LOCKBOX RECEIPT", .00 |
| D M18, M19 | KV | CONFIRM | p. 17 (the two CBL remarks end in personal names, not copied) |
| D M21 | KV | CONFIRM | p. 17 "Page 1 of 2" / "Page 2 of 2", "Continued on next page…", PAY THIS AMOUNT blank on page 1 |
| D D02-D05 | KV (pp. 7, 11); KA (pp. 1-3) | CONFIRM for p. 11; p. 7 and pp. 1-3 not re-opened by me | p. 11 e-mail text as quoted |
| D D08 | KV | CONFIRM | p. 13 handwritten "1. Initial payment … 2a. Partial refund … 2b. Remaining balance refund" |
| D add-on Paper-Pak 14710702037 | KV | CONFIRM | p. 13 render: "BILLED WT 2601LBS REWEIGHED WT 3215LBS", "WIW", "CAB REG 11/19/07 CORRECT AS BILLED", class 050, 3215, 5847, 1879.81, 126.89, 7.50, "DUP 6/30/08 RP", P/C P, W/B 9/28/07; p. 7 row 698.33 / 662.90- / 35.43; 32.15 × 58.47 = 1,879.81; × 0.7 = 1,315.87; 126.89 ÷ 563.94 = 0.2250; at 2,601 lb 566.39 |
| E M01 | KV | CONFIRM | 23-006 p. 4; 23-004 p. 4 "PRO# 6703485626"; 23-003 p. 5 "PRO# 6647373549" |
| E M02 | KV | CONFIRM | "Mail To : YRC (ROADWAY)" |
| E M14 | KV | CONFIRM | 23-003 p. 2 "$ 75.00"; 23-004 p. 2 "$ 382.08"; letters state no amount |
| E M16, M17 | KV | CONFIRM | p. 4: 612.77 / 612.77 / 1225.54 |
| E M20 | KV | CONFIRM | "SATCO-2300008OC"; "Assigned Claim Number: 23009972"; "Draft Number 1385879"; "YRC Claim # 23023786" |
| E D01 | KV | CONFIRM | recomputed 2023-03-19, 189, 129 |
| E D02 | KV | CONFIRM | p. 4 render |
| E D03 | KV | CONFIRM (23-004 pp. 5-8 not re-opened) | p. 4 boxes unticked; the letters name their attachments |
| E D04 | KV | CONFIRM | p. 4, p. 5 |
| E D05 | KV | CONFIRM | p. 5; 23-003 p. 5; 23-004 p. 4 "Unresolved Dispute" |
| E D06 | KV | CONFIRM | p. 5 |
| E D07 | KV | CONFIRM | p. 4; 16-095 l. 31-33 "photocopies of canceled drafts or checks" |
| E clocks | KV | CONFIRM | 189; 84 |
| E lessons (Epiq $0.00) | KV | CONFIRM | forms p. 2 print $75.00 and $382.08 with basis "ADR Claim-Alternative Dispute Resolution" |
| F M01-M05 | KV | CONFIRM | 22-012 p. 4 render |
| F M09, M13, M16 | KV | CONFIRM | 332 × 0.47 = 156.04; 335.15 × 0.47 = 157.52 |
| F M17 | KV | CONFIRM (p. 2, 10, 15 per the validator's text reads) | 711.42 + 449 × 0.42 = 900.00; 673.05 + 445 × 0.51 = 900.00; 1,150 + 900 + 900 = 2,950 |
| F M19, M20 | KV | CONFIRM | p. 4 "Remarks: LOAD BARS/STRAPS** CHECK IN as Best Dedicated Solutions**", "TRACTOR 1019 TRAILER 61336" (the DRIVER column prints a code, not copied) |
| F D01, D02, D04 | KV | CONFIRM | 2026-02-24 + 45 = 2026-04-10; 16 days |
| F P18 money side | KV | CONFIRM (p. 9 per the validator's text read) | p. 4 "Terms are 15 Days from Receipt of Invoice." |

### §2.8 The validator's §4.5 (§8 ledger rows)

| Row | Val. | Mine | Evidence |
|---|---|---|---|
| 1 | KV | CONFIRM | p. 46 render |
| 3 | KV | CONFIRM | 509 × 7.60/100 = 38.68 → 94; 8,920 × 7.60/100 = 677.92 → 575; p. 60: 1,838 × 7.60/100 = 139.69 |
| 5 | KV | CONFIRM | p. 41; 8,594.39 × 0.903 = 7,760.73 |
| 6 | now KV | CONFIRM | p. 94 render |
| 8 | KV | CONFIRM | pp. 11-12 |
| 13 | KV | CONFIRM | recomputed |
| 14 | now KV (one KA) | CONFIRM; the KA (980 total) now verified | §2.0 |
| 15 | now KV | CONFIRM for p. 17; p. 6 (BOL) not re-opened by me | p. 17 render |
| 16 | now KV in full | CONFIRM | pp. 13, 15 renders (pp. 14, 16 not re-opened by me) |
| 17 | KV | CONFIRM | 1,828.04 + 584.63 = 2,412.67 |
| 19 | now KV | CONFIRM | pp. 7, 11, 12, 13 renders |
| 20 | now KV | CONFIRM | pp. 4, 5 renders |
| 22 | now KV | CONFIRM | 23-003 pp. 2, 5 renders |
| 24 (invoice part) | KV | CONFIRM | p. 4 render; rate-con lines per the validator's text reads (ll. 438, 488, 537-539 consistent with the walk) |
| 46 | now KV | CONFIRM | 23-003 p. 2, 23-004 p. 2 renders; set 23 `source.md` rows as quoted by the validator (not re-read by me) |

### §2.9 The validator's §5 additions (each ADD re-opened)

| ADD | Mine | Evidence / wording |
|---|---|---|
| 1 M04 TL issue / invoice dates; YRC "Bill Date" | CONFIRM, NARROW the YRC part | §2.1 M04 |
| 2 M05 labels | CONFIRM | §2.1 M05 |
| 3 M10 gross per article | CONFIRM | 1,279.68 + 7,314.71 = 8,594.39 ≠ 8,594.38 |
| 4 M11 SEFL 2020 no decimal points | CONFIRM, with the note that the printed "MINIMUM FREIGHT CHARGE" there is gross − discount | p. 49 |
| 5 M13 fuel $ unlabeled at SEFL | CONFIRM | p. 46 |
| 6 M16 Never, p. 60 | CONFIRM | p. 60 |
| 7 M18 remark forms | CONFIRM, all present | §2.1 M18 |
| 8 M23 Werner Logistics | CONFIRM | 22-013 l. 212-213 |
| 9 M24 per-issuer fields | CONFIRM | §2.1 M24; add Mode's "Original Amount / Open Balance / Interest / Total Due" (21-014 p. 4) |
| 10 M25 Estes OVLD; SEFL DAFG; CORR REPT | CONFIRM | §2.0, §2.1 |
| 11 D04 e-mail header, portal page | CONFIRM | 21-002 p. 11; 23-006 p. 5 |
| 12 D07 public payer-side records | CONFIRM; add the 3PL's "Date Invoice Paid 01/25/2023" | 23-011 l. 209 |
| 13 §2.5 corrections | CONFIRM | §2.0 |
| 14 M26 late-fee lines (for BC) | the evidence exists: 03-003 p. 11 LP1-LP6 excluded from the total, p. 19 LP1-LP5 included, p. 4 LP1 / LP3 / LP4 included (an uneven ladder, LP2 absent); 02-002 pp. 49, 60 "PENALTY/TARIFF DUE" 25%; 21-010 p. 4 "Assessed LIQD" column; 22-011 l. 842 "AFTER 9/10/2025: 456.75 USD"; 21-014 p. 4 "Interest" column | whether it is a new fact is BC's call; the documents support the row as drafted |

## §3 Counter-examples hunted for the generalisations the validator confirmed

Tested on all files of each type I could read: set 01 (101 ABF bills by script), set 02 (text counts plus 7 renders), set 03 (6 renders), set 04 (OCR of every file), set 19 (all 36 files parsed), set 21 (text of the 10 text-layer files; renders of 21-001, 21-002, 21-004, 21-006, 21-007, 21-010, 21-014, 21-015), set 22 (text of 13 files; renders of 22-008, 22-012, 22-015), set 23 (text of 12 files; renders of 23-003, 23-004, 23-006), set 24 (the 3 text-layer files).

| Generalisation | Result | Evidence |
|---|---|---|
| 82 of 82 real 210s reconcile B3-07 = L3-05 = ΣL1 | **holds**; one failure exists outside the real set | 82/82 on the 18 real files. The partly-real Roadway sample 19-031 (`pls_CTSI210_cropped.txt`) fails: B3-07 34230, L3-05 34220, ΣL1 34230 |
| 0 real 210s carry K1 / NTE / B3-08 | **holds**; one K1 outside the real set | the only `K1*` in set 19 is in 19-031 (partly real) |
| L5 only at AAA Cooper, Estes and the TL batches; "description and NMFC only" at the two LTL carriers | **counter-example at Estes** | 19-015 ST 60003 `L5*1*LEFT MSG FOR DEL APPT 11/14/13` and a contact-like L5 line (a first name and a number) immediately before it; §2.1 M19 |
| 0 of 101 ABF bills print a bill date | **holds** | `abf.py`: the only date labels are Shipment Date (107), Shipping Date (107), PAYMENT DUE DATE, "PAID AT A LATER DATE" (62, a refund-allowance sentence), PICKUP DATE (2) |
| 101 `AU=`, 101 `Tariff:`, 82 PQ numbers (82 distinct), 27 notes, 21 lumper, 9 groups / 23 bills, 4 corrected, 6 two-page | **all hold** | my script reproduces each count; the six non-lumper reasons are limited access (military sites), non-business hours ×2, sorting / segregating, a different fuel rate, a weight difference (3,195 vs 3,207 lb) |
| "PREVIOUSLY INVOICED ON" only at TForce and UPS Freight | **holds** | sweep of `derived/text` and `derived/ocr`; the only other reprint banner is "- REPRINTED COPY -" on a shipper's BOL / packing-slip supplement (21-012 ll. 327, 348, 370), and ODFL's "DUP 6/30/08 RP" stamp (21-001 pp. 11, 13), which the doc already lists under M03 |
| UPS Freight lists never exceed four entries | **holds on the files; the cap is unproven** | 38 lists; my OCR-date count gives {4: 30, 3: 6, 2: 1, 0: 1}; 30 of 38 have exactly four, which looks like a four-slot box, but no list shows a fifth slot and no guide in set 12 was checked for it |
| TForce lists newest-first; earliest entry 7-512 days after shipment | **holds** | 8 lists: 12, 13, 210, 22, 396, 7, 133, 512 days; entries 2, 1, 4, 1, 3, 2, 2, 1; all newest-first |
| M01 PRO always present | **no counter-example** | every bill opened; and on SEFL's scans the PRO digits survive in the text layer even though the label does not ("807148067" ×2 on the bill pages of 02-002, ll. 1927 and 2741, beside garbled headers) |
| M06 terms always present | counter-example already given by the validator | USA Truck "PPD / COL: UNKNOWN" (22-015 p. 4); no other found |
| M07 class always present on LTL | **holds on LTL**; XPO's is inside the description | 03-003 pp. 4, 11, 19; 21-005 l. 226; TL invoices carry none (Werner, Taylor "Van", USA Truck), which the row's "on LTL" already excludes |
| M08 weight always present on LTL | **holds**; one addition | Stevens Transport bills print four weight columns, "TOTAL WEIGHT / DIM WEIGHT / REWEIGH / CHG WEIGHT" ("5000 lbs / 0 lbs / 0 lbs / 5000 lbs", 21-011 ll. 263-264), a layout the row does not list; XPO prints "AS WEIGHT" (21-004 l. 360) |
| M09 rate always present | counter-examples already given by the validator | 02-002 p. 49 (rate column empty), 21-001 p. 11 (accessorial-only print); also 02-002 p. 94 prints no rate on its three re-rated articles (the rate is replaced by the "MIN FRT CHG" line) |
| M14 uncoded lines exist | **holds, wider than ODFL** | uncoded L1 lines: ODFL 72, AAA Cooper 13, Estes 3 (every base-freight line) |
| M15 fee always printed when charged | **untestable**; one observation | ABF: 28 bills with a reweigh remark, 0 fee lines; whether ABF charged nothing or printed nothing cannot be read from the bills |
| M22 not printed by SEFL, ABF, XPO, ODFL | **holds** | 0 hits in 02-002, 01-001, 03-003, 21-001, 21-002, 21-004, 21-005 |
| M23 B3-10 `017` on all ODFL; `035` elsewhere | **holds** | 017 ×34 (ODFL), 035 ×46, blank ×2 (WIEL) |
| M25 no PDF prints a partner share | **holds** | the SEFL boxes carry codes and a partner PRO (OAKH 34844332, DAFG, PYLE), never dollars; TForce ADV / BEY blank; ODFL I/L blank; set 24's text layer carries interline claim totals only |
| SEFL 2020 counter "1 of N" is not a page count | **holds** | p. 49 "1 of 3", p. 60 "1 of 30", one-page prints of different PROs |
| XPO late fees form an unbroken ladder (implicit in the validator's M26 draft) | **counter-example** | 03-003 p. 4 (712-591246) prints LP1, LP3 and LP4 at $10.00 each, no LP2; total 695.65 includes them |
| "Bill Date" on a YRC statement is a bill date | **doubtful** | equals "Due Date" on all eight rows (21-006 p. 5) |
| A rendered court exhibit shows everything the text layer holds | **counter-example** | 21-004 p. 8: the "CHILD PRO #'s" line is in the text layer (l. 306) but under a redaction box on the image |

## §4 §5 versus the raw traces (the M and D rows)

Side by side: what the walk agent reported (companies only) against what `doc-exploration.md` §5 kept, and whether the validator noticed.

| Chain, fact | Raw walk | Doc §5 | Difference | Validator |
|---|---|---|---|---|
| A D03 | "complaint p.6 ¶5 Exhibits A (contracts) and B (summary); agreement + worksheet attached; no BOL/DR; primary" | no D03 row; D03 not in the NOT REPORTED line | a found fact dropped | not noticed |
| A D07 | "p.46 balance 94.00 implies 497.10 paid; complaint p.6 ¶5 says Exhibit B identifies 'checks paid' but no check appears" | "$497.10 paid, derived from M17; date and reference NOT REPORTED" | the complaint's claim of checks dropped | not noticed (harmless) |
| A M20 | quote, SO#, PL#, B/L, customer number | folded into F01-F05 row | — | — |
| A sibling 806266163 M17 | "PAY 2,694.85 → prior 2,218.28 = worksheet 1,744.58 + 55 + 418.70; worksheet NEED $1,599.00 (13 × $123.00), OVER $145.58" | the p. 94 paragraph stops at the bill's own lines | the derived prior total and the worksheet row dropped | not noticed |
| B D01 | "180 d from ≈02/12/2021 original ≈ 2021-08-11 (X26/X18 ¶9 basis); derived, edition caveat" | no D01 row; not in the NOT REPORTED line | a derived deadline dropped | not noticed |
| B D03 | "invoice + BOL + DR per PRO; no certificate" | folded into "D02, D04 Form 410 pp. 1-3" | D03 dropped | not noticed |
| B M02 | "SCAC CNWY; BOL says XPOL" | no row | a key-normalisation detail dropped | — |
| B sibling M18 | "CALL 48HRS IN ADVANCE FOR DELIVE[RY] … CERTIFICATE (mostly redacted)" | not in the sibling paragraph | the remark dropped | the validator found it independently (M19 NARROW, p. 20) without noting the walk had it |
| C M04 | "20121015; 20 days after delivery" | "2012-10-15, 20 days after delivery" | the walk's slip copied: 18 days after delivery, 20 after pickup | **caught** (§4.4 C M04) |
| C M09 contrast | "Estes ST 60003 is a flat-rate bill: L1-03 FR 197.00, no discount or fuel line — P08-type pricing with no quote number" | dropped | an L1-03 qualifier (`FR`) the M09 row does not list | not noticed |
| C M20 | "PO 21838107023; equipment ODFL 530303; no tariff, agreement or quote reference" | no row; not in the NOT REPORTED line | partial fact dropped | — |
| C P21 contrast | "discount on rounded gross: 2420.77 × 0.84 = 2033.45 (unrounded 2033.44)" | dropped | P-scope | — |
| D M06 | walk M06: "PREPAID column; BILL-TO # 76652"; walk F04: "A/R 'Col/Ppd: P'" | M06-M16 row: 'bill-to … (third party), "Col/Ppd P"' cited to p. 17 | the A/R header moved onto the re-bill | **caught** (§4.4 D M06-M16) |
| D M24 / D07 | walk M24: "p.10 (Winn-Dixie statement 186 of 02/06/2005: debit memo DM-HDQACC186834 2,412.67, aged 0-30); p.9 (check stub, 11 Feb 2005: 12,427.40 + 12,427.40 − 2,412.67 = 22,442.13)"; walk D07: "consignee: 2,412.67 by card 1/27/05, clawed back from the vendor by debit memo ACC186834 (01/26/2005) netted on check 007451329" | M17/M24/D06/D07 row: "only in the carrier's A/R history" | the consignee's statement, debit memo and check stub dropped; this is the root of the doc's "D07 never public" | the validator re-found pp. 8-9 on its own (D07 NARROW) but did not record that the walk had reported them and §5.4 dropped them |
| D D01 | "NR as a rule; dates: ship 12/03/04, consignee paid 1/27/05, re-bill 02/18/05, due 03/05/05" | no D01 row; not in the NOT REPORTED line | dropped | not noticed |
| D D03 | "p.3 list; pp.5-17: proof of claim, BOL, memo, statements, e-mails, refunds, revised bill" | folded into "D02-D05" without the attachment list | D03 dropped | not noticed |
| D D02 | "vendor's letter (p.1) says 'paid $1135.55' and 'total of $3,548.22'; with the bill's 1,133.55 the sum is 3,546.22, so the letter carries a $2 typo" | dropped | a documented inconsistency in the claim amount | not noticed |
| D add-on M03 | "print 1 stamped DUP 6/30/08 RP (reprint for the counterclaim), print 2 CUSTOMER COPY; pages 1 of 2 on p.13, 2 of 2 on p.14" | not in the add-on paragraph | dropped | the validator cites "DUP 6/30/08 RP" from p. 11 (M03 Fallback), so the fact survives elsewhere |
| E M06 | "implied: 3PL billed (prepaid-to-3PL BOL; nVision 'Paid Amount'); derived only" | M06 falls under "every M fact but M01, M02, M14, M16, M17, M20" = NOT REPORTED | derived → NOT REPORTED | not noticed; defensible (implied is not found) |
| E M18 | "G2 p.5 declined per YRC Tariff 100-754 …; fallback, quoted by the claimant; 'the message forwarded below' is not in the 5-page file" | M18 NOT REPORTED; the quoted decline sits under P10 and D05 | reclassified from M18 (carrier's reason) to D05 (decision) | not noticed; the missing forwarded message survives in the lessons line |
| E M14 | "whether $382.08 includes a reweigh fee is unknown" | "limited access $75.00; reweigh $382.08" | the caveat dropped | not noticed |
| E clocks | "No copy of Part 378 is held in data/; the 30/60 figures are the brief's" | §4.4 cites Part 378 "as quoted in AX §7 (fetched from the eCFR)" | the walk's caveat replaced by the AX citation | — (consistent with §8 row 37) |
| E D01 | "G2: 04/03/2023 + 180 = 2023-09-30; proof filed 11/08/2023 = day 219, original claim date NOT REPORTED" | "G2's original claim date NOT REPORTED" | the day-219 count dropped | not noticed (harmless) |
| F D03 | "invoice + BOL + rate confirmation per load; primary" | no D03 row; the NOT REPORTED line says "D05-D08" | D03 dropped | not noticed |
| F M21 | "one page, no page counter" | no row; not in the NOT REPORTED line | dropped | — |
| F D02 | "filed 03/12/2026 13:39:16 (16 days after delivery; before the carrier's own 15-day terms could even lapse on receipt)" | "filed 03/12/2026, 16 days after delivery" | the observation dropped | — |

No case was found where §5 turned a NOT REPORTED into a finding. The reverse happened once (E M06, implied → NOT REPORTED). Two verdict-setting values were altered (C M04 20 days; D M06 Col/Ppd), both caught by the validator. The recurring pattern is the silent dropping of D03 (chains A, B, D, F) and D01 (B, D) rows that the walks had filled.

## §6 Privacy check of the validator's report

Patterns run over `research/s5_check_BB_c09_fact_map_money_dispute.md`: phone numbers `[0-9]{3}[-.) ][0-9]{3}[-.][0-9]{4}`, `Mr|Ms|Mrs|Dr|Miss` + capital, e-mail addresses, mixed-case and upper-case street addresses (`[0-9]{2,5} WORD (ST|AVE|RD|BLVD|DR|LN|WAY|TPKE|PKWY|HWY)`), and a listing of every capitalised two-word token with three or fewer occurrences (reviewed by eye). **Result: 0 hits.** The tokens are companies (The Custom Companies, Clamp-Swing Pricing, Dalmation Press, Werner Enterprises, Taylor Truck, Best Dedicated, Yellow Corporation) and field labels. Pages I rendered that carry individuals' names, signatures, e-mail addresses or phone numbers, none of which the validator copied: 21-015 p. 34 (a handwritten contact and phone), 21-002 pp. 10, 11, 13, 17 (a contact name and phone; e-mail headers with names and addresses; a handwritten phone; two names in the CBL remarks), 02-002 pp. 46, 63, 41 (an "ATTENTION OF" first name; shipper and consignee phones), 23-006 p. 4 (the audited-by and prepared-by names), 23-003 p. 5 and 23-004 p. 4 (a carrier employee's name), 22-012 p. 4 (a driver code), 21-011 (a signer's surname). The validator's quotations stop short of each one. The consignee of SEFL 807148067 is referred to by town only throughout, as in the doc.

## §7 Concerns left unproven

1. **R3-08 direction** (the validator's §7 item 1): the five NEMF bills all carry R3-08 / B3-07 = 0.390 to three decimals (12698/32560, 5031/12900, 11188/28687, 44150/113205, 34104/87446). The constancy says the field is a contractual split, not which party keeps it; nothing in `data/` settles it. Set 24's text layer shows interline balances only as claim totals.
2. **TQYL and BPTS identities** (§7 item 2): untestable offline. The catalogue calls TQYL "truckload carrier SCAC" while `README.md` l. 45 calls the same batch "TQL, a broker"; one of the two labels is wrong and the doc's §2.5 inherited the README's.
3. **M15 "always printed when charged"** (§7 item 3): unfalsifiable on bills alone; the ABF observation (28 reweigh remarks, 0 fee lines) shows the absence of a line does not prove the absence of a charge.
4. **The YRC statement's "Bill Date"**: equals "Due Date" on all eight rows of 21-006 p. 5; whether YRC's statement prints a true bill date or copies the due date cannot be decided from one statement. Treat the ADD as a bound until a second YRC statement is held.
5. **The UPS Freight four-entry cap**: 30 of 38 lists are exactly four long; a five-print PRO in set 04 would settle whether the box truncates. None is held.
6. **The TForce list's amounts**: on 546903626 the 05/02/23 entry reads 2,369.67 and the 05/09/23 entry 1,118.82, while the bill in hand (dated after a reweigh that *raised* the weight) totals 1,118.82. The direction is odd (a reweigh upward and a lower total) and the first print is not held; the list's amount column may be the amount then due rather than the amount then billed. Only the 05/02/23 print would settle it.
7. **The Estes contact-like L5 line** (19-015 ST 60003): whether it is a BOL instruction echo ("call X at extension N") or the carrier's own note cannot be read from the 210; it sits between `LX*1` and the remark `LEFT MSG FOR DEL APPT`, which argues for the carrier's side. Either way it is free text in L5 at an LTL carrier.
8. **Pages the validator and I both left to other scopes**: 02-002 complaint pp. 5-10 (chain A D04/D05), 03-003 pp. 1-3 (chain B D02/D04), 21-002 pp. 1-3 and 7, 21-002 p. 6 (BOL), 23-004 pp. 5-8, 22-012 pp. 2, 5-9, 15, 20. Their values in the doc agree with the walks and the catalogue but were not re-opened here.
9. **Redaction boxes over live text** (21-004 p. 8): a pipeline that reads the text layer will see child PROs (and possibly names) that the published image hides. Not a doc error, but a data-handling rule the prototype will need, and one the privacy rule of these reviews should mention.
10. **Line numbers in the validator's 01-001 citations** (ll. 849-867 for bill 150235531) are 20-30 lines earlier than `grep -n` gives on the derived text today (the CL 100 line is l. 879, the lumper line l. 890, the W02 remark l. 893); the values are all present on the page, so nothing turns on it, but a reader following the citations should expect the offset.
