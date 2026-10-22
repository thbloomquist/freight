# Check BB · Validation of doc-exploration.md, money asked (M01-M25) and dispute (D01-D08)

**Date:** 2026-10-18. **Validator:** BB (one of four: AZ, BA, BB, BC). **Target:** `data/doc-exploration.md` (2026-10-10), the fact-by-fact lookup map for C-09's dispute software. **Scope:** the 25 phase-3 money facts (M01-M25) and the 8 phase-4 dispute facts (D01-D08): their §1.3/§1.4 columns, every §2.3/§2.4 cell (Primary, Fallback, Never, If none), §2.5 (the join keys), the §3 rows and §3.4 derivations that touch them, the §4.5 clock arithmetic and §4.6 rows for M04/M18/D05/D07, the M and D rows of the six §5 chains, and 15 assigned §8 ledger rows.

**How:** offline, read-only on `data/` and `research/`, no sub-agents. Every claim was re-opened on the real files: text-layer sets by `grep -n` on `data/derived/text/`, EDI by parsing `data/sources/19_edi_samples_real/` with each ISA's own separators in `python3 -I`, scans by `pdftoppm -r 150` to `SCRATCH/renders/` and reading the PNG. Dataset-wide rules ("82 of 82", "never", "not printed by …") were tested on **all** files of the type, not on the six chains. Arithmetic was recomputed in `python3 -I`. Companies only: no person's name or phone number appears here. Verdicts follow the common brief: KEEP-verified / KEEP-assumed / NARROW / DISCARD / ADD, each with a file_id and page, line or X12 path and the value seen.

## §0 Summary

**Counts.**
- **§2 cells (33 IDs × 4):** 132 cells, 28 empty ("—"); of the 104 with a claim: **83 KEEP-verified, 6 KEEP-assumed, 15 NARROW, 0 DISCARD**, plus 9 cells carrying an ADD.
- **§1 column entries (33 × 3):** **95 KEEP-verified, 4 NARROW** (M18 Need; M25, D06, D08 Checks).
- **Other claims (§2.5, §3.1-§3.4, §4.5-§4.6, the six chains' M/D rows, 15 §8 ledger rows):** 85 rows: **74 KEEP-verified, 5 KEEP-assumed, 6 NARROW, 1 DISCARD**. Eight of the nine §8 rows tagged *assumed* (6, 14, 15, 16, 19, 20, 22, 46, and the invoice part of 24) are now re-opened on the files and hold.
- **Dataset-wide rules tested on every file of the type:** 82 of 82 real 210s reconcile B3-07 = L3-05 = ΣL1; 0 carry B3-08, K1 or NTE; 0 of 101 ABF bills print a bill date; 101 carry `AU=` and `Tariff:`; 82 carry a PQ number; 27 quote-difference notes (21 naming a lumper); 23 bills in 9 amount + date collision groups; "PREVIOUSLY INVOICED ON" exists only on TForce (8 lists) and UPS Freight (38 lists, never more than four entries); the SEFL clock dates 2023-12-16 / 2023-11-01 / 2023-11-11, the 452 days, 189 / 84 / 129 days, and all nine §3.4 derivations recompute.

**The five findings that matter most.**
1. **The §2 claim "everything is observed on files" holds for the money and dispute facts.** Every Primary cell of M01-M25 and D01-D08 except D07's (the customer's AP export, not held) was re-opened on a real file and carries the fact. The 15 narrowings are wording (a wrong carrier, a list that is incomplete, an example read as a rule); none moves a Primary to a Fallback.
2. **One §2.5 failure case is wrong in substance (DISCARD).** TForce did not reuse "an older carrier's PRO" as the BOL: its bill 546903626 prints "B/L NO. MIA95055", the *shipper number* on The Custom Companies' billing advice (21-015 pp. 33-34); the older carrier's PRO 16422968-00 sits on the same paper as TForce's label, which is AW §5's separate PRO case. Two other §2.5 details are off: the "two TQL pairs" are TQYL (a truckload SCAC in the BPTS batch, 19-034), and the Werner pair shares the **same** pickup and issue date, not adjacent ones (22-008 pp. 7, 10).
3. **Three examples are attributed to the wrong carrier.** "UPS '003570' = 35.70%" (M13) and "UPS '002550 INSPECTION'" (M15) are on TForce's 2023 bill (21-015 l. 285, 589); UPS Freight's 2009-10 bills carry the same six-digit encoding with other values ("003690 LTL FUEL ADJUSTMENT 36.96", "001860 INSPECTION 18.00", set 04 OCR). "ISA-06 / GS-02" as the envelope sender (M02) is half right: GS-02 was the carrier in every real file; only ISA-06 (`BPTS`) differs.
4. **Two "never" rules are too strong.** M19 "Not on 210s or XPO bills": AAA Cooper and Estes 210s echo the description and NMFC item in L5, and XPO's corrected invoice 326-343835 prints the BOL's appointment instruction (03-003 p. 20). D07 "never public": a consignee's debit memo and check stub deducting the freight (21-002 pp. 8-9) and a 3PL's paid amount with its EFT number (23-011 p. 4) are in public files; what is never held is a shipper's AP export as such. M21's Never ("pp. 2-3 absent") repeats a claim the AV review had already narrowed: SEFL's 2020 counter reads "1 of 3" on p. 49 and "1 of 30" on p. 60 for different PROs.
5. **The reprint-list and statement claims that drive the first-bill clock are exactly right, and the money arithmetic is right to the cent everywhere.** TForce's eight lists all run newest-first with the earliest entry 7-512 days after shipment (4 of 8 beyond 100 days); UPS Freight's 38 lists never exceed four entries; Estes's "Freight Bill Date" column exists (21-007 p. 4), and YRC's statement adds a "Bill Date" per PRO (21-006 p. 5), an ADD. The SEFL, XPO, ODFL, Taylor and Werner chains reconcile line by line; the only arithmetic slip found is chain C's "20 days after delivery" (18).

## §1 Method

**Files opened (by file_id), and how.**
- Text layer, by `grep -n` and `python3 -I` over `data/derived/text/`: 01-001 (all 130 pages, 107 bill pages, 101 PROs), 02-002 (225 pages: pp. 33, 41, 46, 49, 51, 60, 63, 94, 99, 158, 199, 210, 212, 223 and whole-file counts), 21-005, 21-006, 21-007, 21-013, 21-014, 21-015, 22-007, 22-011, 22-012, 22-013, 23-003, 23-004, 23-006, 23-010, 23-011, 16-082/-083/-084/-092/-093/-094/-095, 20-001/-002/-003, 04-005 (text) and 04-006/-007 (OCR, `data/derived/ocr/04_delphi_ups_freight/`, 38 "PREVIOUSLY INVOICED ON" lists).
- EDI, parsed with each ISA's own separators (`*`, `~`, `>`), every real or assumed-real 210 in set 19: 19-001…19-008 (ODFL, 34 transactions), 19-009…19-014 (AAA Cooper, 11), 19-015 (Estes, 3), 19-033/-034/-035 (BPTS→Target TL batches: WIEL 11, TQYL 20, SPXQ 3) = **82 transactions**; 214s in 19-017 (ODFL) by grep.
- Scans rendered with `pdftoppm -r 150` to `SCRATCH/renders/` and read as images (page numbers as the PDF counts): 02-002 pp. 33, 41, 46, 49, 60, 63, 94; 03-003 pp. 7, 11, 12, 14, 19, 20; 21-002 pp. 7-17; 21-001 pp. 7, 11, 12, 13, 14; 21-004 p. 8; 21-010 p. 4; 21-015 pp. 4, 34; 22-008 pp. 4, 5, 7, 10; 22-012 pp. 2, 4, 9, 10, 15; 23-006 pp. 4, 5; 23-004 p. 2; 23-003 pp. 2, 5.
- Sources read for the (b) order and (d) consistency tests: AK §3.2 (ll. 128-177), AV §2-§5, §7 and its adversarial review §0-§1, AW §5, AX §6-§7, `doc-explanation.md` §4.2-§4.4, the walk reports in `SCRATCH/walks_raw/` and set 23's `source.md`.

**Scripts run** (all `python3 -I`, kept in `SCRATCH/bb_scripts/`):
- `edi210.py`: per-ST B3-02/-03/-04/-06/-07/-08/-09/-10/-11, L3-05, ΣL1-04, K1/NTE/L5 counts, L1-08 codes, R3 partners, ISA-06/GS-02 senders. Output in `SCRATCH/bb_scripts/edi210_out.txt`.
- `abf.py` plus a second pass: per-PRO page groups, bill-date labels, `AU=`, `Tariff:`, `PQ SCHEDULE NO`, the quote-difference notes and the words after "following reasons:", amount + ship-date collision groups.
- Inline scripts: TForce reprint-list ages (4-digit years), UPS Freight reprint-list lengths, TQYL same-amount pairs, SEFL footer lines by page, set 23 form fields, the clock and §3.4 arithmetic.

`sha256sum -c data/SHA256SUMS` was run at the end (result in §1a below). Nothing under `data/` was created, changed or deleted.

### §1a Integrity
`sha256sum -c data/SHA256SUMS`: 271 OK, 0 failed (run after all work). `git status`: only the four validators' new report files are untracked; nothing under `data/` changed.

**Dataset-wide tests the brief asked for, with counts** (details in the ledgers below):
- **Set 19, every real 210 (82 transactions):** B3-07 = L3-05 = ΣL1-04 in **82 of 82**; **0** carry B3-08; **0** carry K1; **0** carry NTE; **48** carry at least one L5 (AAA Cooper 11, Estes 3, all 34 TL; **0** of ODFL's 34). L1-08 codes seen: `405` 34, `FUE` 46, `DSC` 46, `DAA` 11, `400` 34, `LUM` 8, `LAY` 2, `STOP` 1, `STC` 1, `TONU` 1, `MMC` 1, `SUF` 1, **uncoded 88** (every base-freight line at all three LTL carriers, AAA Cooper's deficit lines, ODFL's $24/$11 Canadian lines). R3 with a partner SCAC other than the biller: AAA Cooper `R3*NEMF…*12698` on 5 bills (19-009 ST 0014 $126.98 of $325.60; 19-010 ST 0016-0018; 19-013 ST 0006), and Estes `R3*OVLD*D**LT**2200302174` (19-015 ST 60001, R3-08 blank). B3-10: `017` 34 (all ODFL), `035` 46, blank 2 (WIEL). Senders: ISA-06 = GS-02 = B3-11 at ODFL, AAA Cooper, Estes; on the 34 TL transactions ISA-06 = `BPTS` while GS-02 = B3-11 = `WIEL`/`TQYL`/`SPXQ`.
- **Set 01 (101 ABF bills, 107 bill pages):** **0** bills print any bill-date label (only "Shipment Date" and "PAYMENT DUE DATE"); `AU=ABF646-468646` on **101** bills (205 occurrences); `Tariff: AOD000` on **101**; `PQ SCHEDULE NO` on **82** bills, 82 distinct values; "The invoice amount differs from the quoted amount" notes: **27** (27 bills), **21** naming LUMPER within the note (the other six: limited access, non-business hours ×2, sorting/segregating, a different fuel rate, a weight difference); amount + ship-date collisions: **9 groups, 23 bills** (five at $256.54 on 08/07/2024); 4 CORRECTED INVOICE bills; no page counter on any bill page.
- **"PREVIOUSLY INVOICED ON" across every derived text:** only 04-006 (17), 04-007 (21) and 21-015 (8); 0 in sets 01, 02, 03, 21-ODFL/XPO and everywhere else. UPS Freight's 38 lists hold 4, 4, …: distribution {4: 30, 3: 1, 2: 1, 1: 5, 0: 1}, **never more than four**. TForce's 8 lists hold 2, 1, 4, 1, 3, 2, 2, 1 entries, every list newest-first; earliest entry minus ship date = 12, 13, 210, 22, 396, 7, 133, 512 days (so on 4 of 8 the earliest entry is not the first bill).
- **Statements held, fields per type:** TForce 21-015 p. 4: statement no., invoice date, aging 0-30/31-60/61-90/91-365/over 365, per row PRO, ship date, customer reference, P/C, amount, remarks, and a remittance "Reason" column. Estes 21-007 p. 4 "Account Listing": Adj/BD, Pro, Statement Date, Billed Amount, Freight Bill Date, Statement Number, BOL, PO, Terms, Balance Due (Adj/BD blank on all 4 rows). ODFL 21-010 p. 4 and 21-001 p. 7 "Statement of Account by Pro Detail": Pro, Pro Date, Freight Charges, Assessed LIQD, Net Cash Posted, Misc Adj, Remaining Frt Charges, Remaining LIQD, Total Open AR. Kuehne+Nagel 21-013 p. 10: Item Type A (credit, negative) / I (invoice), item number, item date, due date, amount, "SCAC / Pro Number" (`RDWY349533831X`). RXO 22-011 p. 4: invoice date/number, transaction type, pay terms, due date, Invoice_Amount, Adjusted_Amount, Applied_Amount, Credited_Amount, Balance, Days_Past_Due, Load Number. Mode 21-014 p. 4: Net 30, 18% annual interest, per row invoice date, age, amount, open balance, interest. YRC 21-006 pp. 4-5: Pro, amount, accessorial codes (`DEF AS IDIS REWT PRNT FSC`), age, Bill Date, Due Date, Tariff #, P/C, Pickup Date. UPS 04-005: invoice number/date/amount/due, payment amount, balance. TQL 22-007 p. 5: invoice no., invoice date, amount, balance due (dates differ from the invoices' own, p. 8).
- **Sets 16 and 20, what the forms require:** every carrier form (ABF 16-092, FedEx 16-082, YRC 16-095, R+L 16-093, Averitt 16-094, South Bay 16-084, XPO page 16-083) asks for claimant name and address, the claimant's own claim number, the amount, the PRO(s) (with date at ABF, Averitt, South Bay), the nature of the overcharge, the tariff/item authority (NMFC item, sub, class, tariff item at Averitt), and a paid-versus-should-be line (weight, rate, charges); ABF, FedEx, R+L, Averitt and South Bay print a bond of indemnity; attachments named are the paid freight bill, the original BOL, the vendor invoice "when claim is based on weight", catalog pages, packing slips (ABF, R+L), a weight certificate (FedEx, South Bay, YRC "certified weight ticket"), canceled checks for duplicate payment (YRC), the agreement or tariff copies (XPO); YRC: "Brochures and 'sample' bills of lading will not be accepted" (l. 36-37), 180 days of pickup, acknowledge in 30 days; XPO: invoice must be paid first, 180 days of receipt of the original invoice. SF 1113 (20-001): paid date, carrier's bill number, SCAC, subvoucher amounts, "DIFFERENCES … AMOUNT", "AMOUNT VERIFIED", "TOTAL CLAIMED"; 41 CFR 102-118.545 as amended (20-003 l. 29-30): "(a) The transportation document. (b) An explanation for the claim. (c) Any additional supporting documentation."
- **Set 23, Epiq figure:** `source.md` rows 23-003 and 23-004 read "Claim 16215 (filed 11/8/2023, $0.00)" and "Claim 16595 (filed 11/9/2023, $0.00)"; the forms' item 7 print "$75.00" (23-003 p. 2) and "$382.08" (23-004 p. 2). Confirmed.

## §2 Verdict ledger for §2.3, §2.4 (every cell of M01-M25 and D01-D08)

Verdicts: **KV** = KEEP-verified, **KA** = KEEP-assumed, **N** = NARROW, **D** = DISCARD, **A** = ADD. A cell printed "—" in the doc is recorded as "empty" (nothing to test). Pages are PDF pages; "l." is a line in the derived text; EDI paths are file, ST, segment-element.

### §2.3 Money asked

| ID | Cell | Claim as written (short) | Verdict | Evidence (file_id p./l./segment = value) | Corrected wording (N/D/A only) |
|---|---|---|---|---|---|
| M01 | Primary | 210 B3-02 (TL also N9*IV) | KV | 19-001 ST 0001 B3-02 = `00902527924`; 19-035 ST 226126002 B3-02 = `1103693` and `N9*IV*1103693`; B3-02 filled on 82 of 82 | — |
| M01 | Fallback | PDF header labels; XPO scan line; BOL's PRO label; DR header; 214 B10-01; statement row | KV | 01-001 l. 847 "Freight bill No: 150235531"; 02-002 p. 46 "FREIGHT BILL NO: 807148067"; 03-003 p. 11 "LTL INVOICE# 405-677016" and scan line "405677016 0180993 8"; 22-012 p. 4 "PRO. NO. 1848869A"; BOL label: 03-003 p. 13 sticker "405-677016" in the carrier box, 21-002 p. 6 label "02902161435 SFC"; DR: 03-003 p. 14 "PRO NUMBER 405-677016", 21-004 p. 8 "Pro Number 271-432501"; 19-017 `B10*00902527924`; statement rows 21-015 p. 4, 21-007 p. 4, 21-010 p. 4 | — |
| M01 | Never | — | empty | — | — |
| M01 | If none | Always present | KV | no bill opened lacks one; 82/82 210s | — |
| M02 | Primary | 210 B3-11 (SCAC) and ISA-06 / GS-02 (the envelope sender, e.g. a freight-payment firm) | **N** | B3-11 filled 82/82. On the 34 BPTS transactions ISA-06 = `BPTS` but GS-02 = `WIEL` / `TQYL` / `SPXQ` = B3-11 (19-033/-034/-035); at ODFL, AAA Cooper, Estes all three are the carrier. "Freight-payment firm" is the catalogue's label for BPTS, not shown in the file (AV review B27) | "210 B3-11 (SCAC); ISA-06 is the envelope sender and can differ (`BPTS` on the Target TL batches, *assumed* a freight-payment firm); GS-02 was the carrier in every real file" |
| M02 | Fallback | PDF letterhead; statement header | KV | 02-002 p. 46 letterhead SEFL; 22-008 p. 4 Werner Enterprises; 21-015 p. 4 "TForce Freight … Invoice/Statement No: R1754408" | — |
| M02 | Never | ISA-06 as the carrier | KV | 19-033 ISA-06 `BPTS` ≠ B3-11 `WIEL` | — |
| M02 | If none | Always present | KV | as above | — |
| M03 | Primary | PDF title or banner plus a changed amount or bill-to on a known PRO | KV | 02-002 p. 46 "BALANCE DUE INVOICE" (PAY 94.00) vs p. 33 "PAST DUE INVOICE" (PREPAID 591.10), same PRO 807148067; 03-003 p. 11 "*** BALANCE DUE INVOICE ***", p. 19 "*** CORRECTED INVOICE ***"; 01-001 4 "CORRECTED INVOICE" bills (150256193, 165261918, 165261921, 165407196); 21-002 p. 17 "ORIGINAL INVOICE" on a re-bill to a new payer | — |
| M03 | Fallback | 210 B3-08 (unused in every real 210 held); statement Adj/BD flag (Estes); "DUP" / "PAST DUE" marks | **N** | B3-08 empty in 82/82. Estes 21-007 p. 4 carries the column header "Adj/ BD" but it is blank on all four rows held, so no flag value was ever seen. "DUP 6/30/08 RP" 21-001 p. 11; "PAST DUE INVOICE" 02-002 p. 33 | "… statement Adj/BD column (Estes 21-007; present as a header, never populated in the file held); …" |
| M03 | Never | The title alone (ODFL re-bills a new payer under "ORIGINAL INVOICE") | KV | 21-002 p. 17 footer "ORIGINAL INVOICE", "Invoice Date 02/18/05", "CBL DGB 2/18/05 … CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER" | — |
| M03 | If none | Derived: group every print by PRO | KV (rule) | supported by pp. 33/46 and 28/41 of 02-002 (two prints per PRO) | — |
| M04 | Primary | earliest of: first 210's B3-06; PDF bill date (SEFL "DATE BILLED", ODFL "Invoice Date"); earliest "PREVIOUSLY INVOICED ON" entry (TForce, UPS; newest first, can stop short); Estes statement "Freight Bill Date" | KV (+A) | 19-001 ST 0001 B3-06 `20121015`; 02-002 p. 46 "DATE BILLED 06/19/2023" (text l. 49 garbled "06/1912023"); 21-002 p. 17 "Invoice Date 02/18/05"; TForce 21-015: 8 lists, all newest-first, earliest entry 7-512 days after shipment; UPS set 04: 38 lists, max 4 entries; 21-007 p. 4 "Freight Bill Date 4/04/24" | ADD to the list: YRC statement "Bill Date" (21-006 p. 5); TL invoices print an issue/invoice date (22-008 p. 4 "ISSUE DATE 01/17/2023"; 22-012 p. 4 "INVOICE DATE 02/26/2026"; 22-015 p. 4 "INVOICE DATE: 7/17/2023"; 22-013 l. 200 "Invoice Date") |
| M04 | Fallback | Statement date (flag as late) | KV | 21-015 p. 4 "Invoice Date: 8-08-23" for bills shipped 2022-23 | — |
| M04 | Never | A reprint's date; ABF and XPO print no bill date | KV | 02-002 p. 33 reprint "DATE BILLED 08/26/2025" of a 06/19/2023 bill; ABF 0 of 101 bills carry any bill-date label; XPO 03-003 pp. 7, 11, 19 and 21-005 (text) print none | — |
| M04 | If none | Mark the clock "unknown, no later than …" | KV (rule) | consistent with the TForce ages above | — |
| M05 | Primary | PDF ("PAYMENT DUE DATE", "PAYMENT IS DUE BY") | KV (+A) | 01-001 l. 853 "PAYMENT DUE DATE: 07/19/2024"; 02-002 p. 46 "PAYMENT DUE DATE 07/04/2023"; 03-003 p. 11 "*** PAYMENT IS DUE BY 02/27/2021 ***" | ADD labels: ODFL "Due Date 03/05/05" (21-002 p. 17); USA Truck "PAYMENT DUE: 8/16/2023" (22-015 p. 4); TForce "Payment Due ON RECEIPT" (21-015 p. 4); Taylor prints none (22-012 p. 4) |
| M05 | Fallback | Tariff payment item + bill date | KV | 06/19/2023 + 15 = 07/04/2023 (p. 46); XPO 02/27/2021 − 15 = 02/12/2021 = ship date (p. 11) | — |
| M05 | Never | — | empty | — | — |
| M05 | If none | Derived | KV (rule) | as above | — |
| M06 | Primary | 210 B3-04 + N1*BT | KV | 19-001 ST 0001 B3-04 `PP`, `N1*BT*DALMATION PRESS LLC`; 19-035 ST 226126002 `TP`, ST 226126003 `CC` | — |
| M06 | Fallback | PDF terms box ("PREPAID"/"COLLECT"/"THIRD PARTY", ODFL "P/C" box) and bill-to block; statement P/C | KV | 02-002 p. 46 "PREPAID", p. 63 "THIRD PARTY"; 03-003 p. 12 "US $1,809.93 PREPAID"; 21-001 p. 11 "P/C P" box; 21-015 p. 4 "P/C C" | — |
| M06 | Never | — | empty | — | — |
| M06 | If none | Always present | **N** | 22-015 p. 4 (USA Truck) prints "PPD / COL: UNKNOWN"; the bill-to is present | "Bill-to always present; the terms field can read UNKNOWN on a TL invoice (USA Truck 22-015 p. 4)" |
| M07 | Primary | PDF class column ("CLASS 70.0", ABF "EX70") | KV | 02-002 p. 46 "CLASS 70.0"; 01-001 l. 1420 "EX70" (58 occurrences) | — |
| M07 | Fallback | 210 L7-07 | KV | 19-001 ST 0001 `L7-07` = `050`; 19-009 ST 0014 `060`; 19-015 ST 60001 `70` | — |
| M07 | Never | — | empty | — | — |
| M07 | If none | Always present on LTL | **N** | XPO prints the class inside the description text, not in a column: 03-003 p. 11 "PLT MISC 0-0 CLASS 100", p. 7 "PLT NUTRITION SUPPLEMENTS CLASS 100" | "Always present on LTL, in a column at SEFL, ABF, ODFL, TForce and inside the description line at XPO" |
| M08 | Primary | PDF weight column; "AS WEIGHT 1,000 / DEFICIT 214"; "DEF111 AS500" | KV | 02-002 p. 51 l. 21 "AS WEIGHT 1,000", l. 23 "DEFICIT 214"; p. 60 "AS WEIGHT 2,000 / DEFICIT WGHT 162"; 01-001 l. 976-977 "DEF111" over "AS500" in the type column | — |
| M08 | Fallback | 210 L0-04; L3-01 rated weight; ODFL L1 DAA line; AAA Cooper L0-02 | KV | 19-001 ST 0001 `L0-04` 650; ST 0002 `L3*1000` with `L1**36.2*PH*6045****DAA`; 19-012 ST 0004 `L0*2*10000*LB*1420` | — |
| M08 | Never | — | empty | — | — |
| M08 | If none | Always present on LTL | KV | every LTL bill opened prints a weight | — |
| M09 | Primary | PDF rate column, unit by weight × rate = charge (SEFL "60080"; ABF "73317"; XPO "391.89") | KV | 02-002 p. 46: 509 × 600.80/100 = 3,058.07; 01-001 l. 1420: 645 × 733.17/100 = 4,728.95; 03-003 p. 7: 300 × 391.89/100 = 1,175.67 | — |
| M09 | Fallback | 210 L1-02/-03 (Estes "LB" is per cwt) | KV | 19-015 ST 60001 `L1*2*298.86*LB*242077`: 810 × 298.86/100 = 2,420.77 | — |
| M09 | Never | A fixed unit assumption | KV (rule) | the three carriers above use two notations | — |
| M09 | If none | Always present | **N** | blank on minimum-charge and accessorial-only prints: 02-002 p. 49 rate column empty ("MINIMUM FREIGHT CHARGE $1,019.77"); 21-001 p. 11 no rate (sorting charge only) | "Present on rated lines; blank on minimum-charge and accessorial-only prints" |
| M10 | Primary | PDF line extension | KV | 02-002 p. 46 3058.07; p. 41 two articles 1279.68 + 7314.71 = 8594.39 | ADD: the gross is the sum of per-article extensions (4.05 × 315.97 = 1,279.68; 23.15 × 315.97 = 7,314.71), not the total weight × rate (27.20 × 315.97 = 8,594.38) |
| M10 | Fallback | 210 L1-04 (cents) | KV | 19-001 ST 0001 `L1**40.17*PH*26111` | — |
| M10 | Never | — | empty | — | — |
| M10 | If none | Derived: Σ weight × rate | KV | as above, per article | — |
| M11 | Primary | PDF printed % and $ | KV | 02-002 p. 46 "88.15% DISC 2695.69"; 01-001 l. 859 "DISC … 89.5% -6,232.60"; 21-015 l. 826 "84.00% DISCOUNT 84.00 -4,186.64"; 21-002 p. 17 "Discount Allowed: 70.00% 2299.53-" | ADD: SEFL 2020 prints both without points, "DISCOUNT PERCENTAGE 9100 / DISCOUNT AMOUNT 1031100" (02-002 p. 49) |
| M11 | Fallback | 210 L5 text (AAA Cooper, Estes); derived $ ÷ gross (ODFL 210; XPO "DISCOUNT SAVES YOU" prints $ only) | KV | 19-009 ST 0014 `L5*2*LESS 78.00 PCT DISCOUNT`; 19-015 `L5*1*DISCOUNT 84.0%`; 19-001 `L1**-188.00*PH*-18800****DSC`, 188.00 ÷ 261.11 = 72.0%; 03-003 p. 11 "XPO LOGISTICS DISCOUNT SAVES YOU ($468.96)", 21-005 l. 227 "-$534.01", no % | — |
| M11 | Never | — | empty | — | — |
| M11 | If none | Derived | KV | as above | — |
| M12 | Primary | PDF "MCADJ", "MIN", "M", "MIN FRT CHG" | KV | 01-001 l. 1072 "ABSOLUTE MIN CHARGE ADJUSTMENT MCADJ ADJ 76.64" (44 occurrences); 02-002 p. 94 "MIN FRT CHG 3454.14", p. 49 "MINIMUM FREIGHT CHARGE". XPO "M" and TForce "MIN" not seen on the pages I opened (AV §2.2, *assumed* here) | — |
| M12 | Fallback | 210 code MMC (AAA Cooper) | KV | 19-010 `L1*1**MN*10000****MMC****MINIMUM CHRGE` | — |
| M12 | Never | — | empty | — | — |
| M12 | If none | Derived: compare net with the floor | KV (rule) | 02-002 p. 46: 362.38 > $152 floor (p. 20) | — |
| M13 | Primary | PDF ("FSC 30.3%", "LTL FUEL SURCHARGE OF 22.00%") | KV | 01-001 l. 867 "FSC 30.3% 221.55"; 02-002 p. 46 "LTL FUEL SURCHARGE OF 22.00%" with the $79.72 printed unlabeled in the charges column | — |
| M13 | Fallback | 210 L5 text; derived $ ÷ net (ODFL; XPO volume bills; UPS "003570" = 35.70%) | **N** | 19-009 `L5*3*Fuel Surcharge 29.00 PCT`; 19-001 12.79 ÷ 73.11 = 17.5%. But "003570 LTL FUEL ADJUSTMENT 35.70 215.25" is **TForce's** 2023 bill (21-015 l. 285; p. 33 prints "004030 LTL FUEL ADJUSTMENT 40.30"); UPS Freight's 2009-10 bills use the same encoding ("003690 LTL FUEL ADJUSTMENT 36.96", set 04 OCR); in both the % is printed, not derived | "… TForce / UPS Freight print the fuel % as a six-digit code and a percent ('003570 LTL FUEL ADJUSTMENT 35.70', 21-015 l. 285; '003690 … 36.96', set 04 OCR)" |
| M13 | Never | — | empty | — | — |
| M13 | If none | Derived | KV | as above | — |
| M14 | Primary | PDF name (+ code at ABF, XPO, TForce; name only at SEFL, ODFL) | KV | ABF l. 862 "CCS 22.00", l. 865 "SHDL/210"; XPO p. 11 "CBR", p. 19 "APT APPOINTMENT $51.90", "LP1"; TForce l. 527 "005000 NOTIFICATION CHARGES 50.00"; SEFL p. 46 "LIFTGATE SVC", "PVT RESIDEN"; ODFL 21-002 p. 17 "CORRECTED BILL OF LADING CHARGE", 21-001 p. 13 "CALL 72HRS IN ADV FOR DEL APPT 7.50" | — |
| M14 | Fallback | 210 L1-08 codes (405/FUE, DSC, LUM, LAY, TONU, STOP, SUF) with L5 text | **N** | real-file code set: `405` 34, `FUE` 46, `DSC` 46, `DAA` 11, `400` 34, `LUM` 8, `LAY` 2, `STOP` 1, `STC` 1, `TONU` 1, `MMC` 1, `SUF` 1; 88 L1 lines uncoded; TL L5 text e.g. `L5*2*FUEL SURCHARGE`, `L5*1*TRUCK ORDER NOT USED` (19-035) | "210 L1-08 codes seen in real files: 405/FUE, DSC, DAA, MMC, SUF, 400, LUM, LAY, STOP, STC, TONU; base-freight lines carry no code at any LTL carrier" |
| M14 | Never | — | empty | — | — |
| M14 | If none | Always present; uncoded lines exist (ODFL $24, $11) | KV | 19-001 ST 0005, 19-002 ST 0001, 19-003: `L1****2400`, `L1****1100` | — |
| M15 | Primary | PDF ("CBR REWEIGH OF SHIPMENT FEE", "CORRECTED BILL OF LADING CHARGE", UPS "002550 INSPECTION") | **N** | 03-003 p. 11 "CBR REWEIGH OF SHIPMENT FEE $37.25"; 21-002 p. 17 "CORRECTED BILL OF LADING CHARGE 15.00"; "002550 INSPECTION 25.50" is TForce (21-015 l. 589); UPS Freight prints "001860 INSPECTION 18.00", "001906 INSPECTION 19.06" (set 04 OCR) | "… TForce '002550 INSPECTION 25.50'; UPS Freight '001860 INSPECTION 18.00'" |
| M15 | Fallback | 210 coded line | KA | no real 210 held carries a reweigh, inspection or corrected-BOL fee line (code set above); a real corrected 210 would test it | — |
| M15 | Never | — | empty | — | — |
| M15 | If none | Always printed when charged | KA | no counter-example in `data/`; not provable from it | — |
| M16 | Primary | 210 B3-07 = L3-05 (82 of 82 real 210s reconcile) | KV | `edi210.py`: 82 of 82, B3-07 = L3-05 = ΣL1-04 | — |
| M16 | Fallback | PDF "TOTAL" / "TOTAL AMOUNT DUE" / "PAY THIS AMOUNT", cross-checked against the column sum and the scan line (XPO) | **N** | 02-002 p. 46 "TOTAL 591.10"; 01-001 "TOTAL AMOUNT DUE BY $942.02"; 21-002 p. 17 "PAY THIS AMOUNT 1133.55"; XPO scan line cents 0180993 = 1,809.93 (03-003 p. 11). But on SEFL balance-due prints "PAY THIS AMOUNT" is the balance (p. 46: 94.00 against TOTAL 591.10; p. 41: 110.23 against 1088.74) | "… 'PAY THIS AMOUNT' only on original and corrected prints (ODFL 21-002 p. 17; SEFL p. 63); on SEFL balance-due prints it is the balance (M17)" |
| M16 | Never | SEFL 2020 "PAY THIS AMOUNT" (a base plus a 25% penalty, p. 49) | KV | p. 49 $809.44 = 647.55 + 161.89 (647.55 not printed); p. 60 $174.61 = PVT RESIDEN 139.69 + "PENALTY/TARIFF DUE" 34.92 (139.69 × 0.25 = 34.92, base printed) | — |
| M16 | If none | Derived | KV | column sums reproduce on every bill opened | — |
| M17 | Primary | XPO "AMOUNT PAID / BALANCE DUE"; SEFL balance-due "PAY THIS AMOUNT"; ABF "original total … correct charge … reduction" | KV | 03-003 p. 12 "AMOUNT PAID: US $162.90 / BALANCE DUE: US $1,809.93"; 02-002 p. 46 "PAY THIS AMOUNT 94.00"; 01-001 l. 6185-6187 "The original total charge was $ 326.60. The correct charge is $ 300.52, a reduction of $ 26.08" | — |
| M17 | Fallback | Statement (cash posted, remaining); A/R history (set 21 pp. 13-16); derived original = new total − balance due | KV | 21-010 p. 4 "Net Cash Posted 528.19- … Remaining 72.00"; 21-001 p. 7 "698.33 … 662.90- … 35.43"; 21-002 pp. 13-16; 1,088.74 − 110.23 = 978.51 | — |
| M17 | Never | — | empty | — | — |
| M17 | If none | Customer's AP record | KA | not held | — |
| M18 | Primary | PDF remarks and reason codes (ABF "W02/AUTH:Reweigh - See W&R certificate"; SEFL "** PER GOOGLE EARTH …"; ODFL "CBL DGB 2/14/05 …"; TForce "*** SHIPMENT REWEIGHED ***") | KV (+A) | 01-001 l. 866 "W02/AUTH:Reweigh - See W&R certificate for details." (29 bills); 02-002 p. 46 "** PER GOOGLE EARTH THIS IS A PRA DLVY"; 21-002 p. 17 "CBL DGB 2/14/05 CORRECTED BILL OF LAD CHANGE TO ADD COMMODITY DESCRIPTION PER LETTER FROM THE SHIPPER"; 21-015 l. 824 "*** SHIPMENT REWEIGHED ***" | ADD forms seen: TForce "WAIVED INSPECTION", "04424-DTR ORIGINAL WGT/REWEIGH", "SHIPMENT WEIGHED AT DTR." (21-015 p. 33); ODFL "FBA DHE 8/08/07 FREIGHT BILL AUDIT", "CAB SRS 11/02/07 CORRECT AS BILLED", "ADDED SSC PER DR" (21-001 p. 11), "W & I REWEIGH CORRECTE WEIGHT 1070 LBS" (p. 12); XPO "…ED PER WEIGHT CERTIFICATE" (03-003 p. 12) |
| M18 | Fallback | 210 K1 (never used in a real file) or L5 remarks (Estes) | KV | K1 0 of 82; 19-015 `L5*1*LEFT MSG FOR DEL APPT 11/14/13` | — |
| M18 | Never | — | empty | — | — |
| M18 | If none | Carrier: no real 210 carries it; SEFL's corrected prints sometimes print nothing (896789802, p. 63) | KV | 0 of 82 (no K1, no NTE, no remark-type L5 outside Estes); 02-002 p. 63 (CORRECTED, no remark) and p. 41 (BALANCE DUE raising the weight, no remark) | — |
| M19 | Primary | PDF description block (SEFL, ABF, ODFL) | KV | 02-002 p. 46 "*LIFTGATE DELIVERY", "QUOTE #CWEN3E465", p. 41 "CL150 NMFC 49880-"; 01-001 l. 863-864 "DO NOT BREAK DOWNPU 3-5PSFB FAX", l. 849 "CL 100 ITEM 057300-03V"; 21-001 p. 13 "CALL 72HRS IN ADV FOR DEL APPT", 21-002 p. 17 "NMFC #156600 S7 92.5 / OVER 15 DENS" | — |
| M19 | Fallback | — | empty | — | — |
| M19 | Never | — | empty | — | — |
| M19 | If none | Not on 210s or XPO bills | **N** | AAA Cooper and Estes 210s echo the description and NMFC item in L5 (19-009 `L5*1*BOOKS, NOI NMFC 161630`; 19-015 `L5*2*HAND TOOLS, OTHER THAN POWER*186900*N`), never instructions or a quote; ODFL's 34 have no L5. XPO's corrected invoice 326-343835 prints "CALL 48HRS IN ADVANCE FOR DELIVE[RY] …" (03-003 p. 20) and the BOL's class in the description ("PLT MISC 0-0 CLASS 100", p. 11) | "Not on ODFL 210s; AAA Cooper and Estes 210s carry only the description and NMFC in L5; XPO bills echo the class and, on 326-343835, the appointment instruction (03-003 p. 20)" |
| M20 | Primary | PDF: quote ("QUOTE #", "PQ SCHEDULE NO", "QN#"), tariff ("Tariff: AOD000", "TARIFF 559", "TARIFF CNWY-199"), authority ("AU=ABF646-468646"), account | **N** | 02-002 p. 46 "QUOTE #CWEN3E465"; 01-001 "PQ SCHEDULE NO" on 82 bills; 21-005 l. 219 "QN# 89.8DZ32430239999999999999"; 01-001 "Tariff: AOD000" ×101; 21-002 p. 17 "TARIFF 559"; "AU=ABF646-468646" on 101 bills; accounts 02-002 p. 46 "CUSTOMER NUMBER 071-003454", 01-001 "Account No: 468646-0005". "TARIFF CNWY-199" is printed on XPO's delivery receipts (03-003 p. 14, 21-004 p. 8 footer); the invoices say "TARIFF 199" (03-003 p. 11) | "… tariff ('Tariff: AOD000', 'TARIFF 559', XPO 'TARIFF 199' on the bill and 'TARIFF CNWY-199' on the DR footer) …" |
| M20 | Fallback | 210 L7 (tariff), N9 (references) | KV | 19-009 ST 0014 `L7*1*CZAR*910****060***20120917*0562`; `N9*BM`, `N9*PO`, `N9*CR`; TL `N9*IV/LN/IT/CR/HU/PO/SO` (19-035) | — |
| M20 | Never | — | empty | — | — |
| M20 | If none | Per carrier | KV | the six layouts above differ | — |
| M21 | Primary | PDF ("1 of 1", "Page 2 of 3", "( continued on next page )") | KV | 02-002 p. 46 "1 of 1"; 21-002 p. 17 "Page 1 of 2" / "Page 2 of 2"; 21-001 p. 11 "Page No 2"; 03-003 p. 11 "( continued on next page )" | — |
| M21 | Fallback | None: group pages by PRO and test the column sum | KV | ABF prints no counter on any of 107 bill pages (the only "Page x of" strings are court stamps); 6 bills run to two pages | — |
| M21 | Never | A counter as proof of completeness (SEFL p. 49 "1 of 3" with pp. 2-3 absent) | **N** | p. 49 prints "1 of 3"; p. 60, a different PRO on the same 2020 layout, prints "1 of 30"; AV review #13: all 14 2020 prints read "1 of N" on different PROs, and the pay-amount gap on p. 49 is the 25% penalty (647.55 + 161.89 = 809.44), not missing pages | "A counter as proof of completeness: on SEFL's 2020 layout '1 of 3' (p. 49) and '1 of 30' (p. 60) do not number a bill's pages, and 'pp. 2-3 absent' is not shown" |
| M21 | If none | Derived | KV | column sums reproduce on complete bills | — |
| M22 | Primary | TForce / UPS Freight reprint list | KV | 21-015 (8 lists), 04-006/-007 (38 lists); no other file in `data/derived/` contains "PREVIOUSLY INVOICED" | — |
| M22 | Fallback | Statement rows per PRO (Estes freight bill date) | KV (+A) | 21-007 p. 4 | ADD: YRC statement "Bill Date" per PRO (21-006 p. 5) |
| M22 | Never | — | empty | — | — |
| M22 | If none | Not printed by SEFL, ABF, XPO, ODFL | KV | 0 hits in 02-002, 01-001, 03-003, 21-005, 21-001, 21-002; SEFL reprints carry a new DATE BILLED instead (p. 33), ODFL marks "DUP" (21-001 p. 11) | — |
| M23 | Primary | TL invoices (Werner, Taylor, USA Truck); 210 B3-09 with qualifier | KV (+A) | 22-008 p. 4 "DELIVERY DATE - 01/13/2023"; 22-012 p. 4 "DATE DELIVERED 02/24/2026"; 22-015 p. 4 "DELIVERY DATE: 7/11/2023"; 19-009 ST 0014 B3-09 `20121221` B3-10 `035` | ADD: Werner Logistics "Delivery Date 01-23-2025" (22-013 l. 212-213); the TL 210s: 46 of 48 non-ODFL transactions coded 035, 2 WIEL blank |
| M23 | Fallback | — | empty | — | — |
| M23 | Never | 210 coded 017 as an actual date | KV | 34 of 34 ODFL B3-10 = `017` | — |
| M23 | If none | Use F14 | KV (rule) | — | — |
| M24 | Primary | Statement (aging, cash posted, Adj/BD, remaining, interest) | KV (+A) | aging 21-015 p. 4; cash posted and remaining 21-010 p. 4, 21-001 p. 7; Adj/BD 21-007 p. 4 (column only); interest 21-014 p. 4 "Annual Interest Rate: 18%" | ADD: RXO Adjusted/Applied/Credited/Days_Past_Due/Load (22-011 p. 4); YRC accessorial codes, tariff, bill/due/pickup dates (21-006 pp. 4-5); K+N item type A/I (21-013 p. 10); UPS invoice/payment/balance (04-005); a consignee's own aging statement (21-002 p. 10) |
| M24 | Fallback | Carrier portal | KA | none held; YRC's claim-status page (23-006 p. 5) is the only portal print | — |
| M24 | Never | — | empty | — | — |
| M24 | If none | Customer AP for the shipper's side | KA | not held | — |
| M25 | Primary | 210 R3 (AAA Cooper: NEMF, $126.98 of $325.60) | **N** | 19-009 ST 0014 `R3*NEMF*1*HARRISBURG*M****12698`, B3-07 `32560`; also 19-015 ST 60001 `R3*OVLD*D**LT**2200302174` (a second SCAC, R3-08 blank); 19-001 `R3*ODFL*O` (self) | "210 R3 (AAA Cooper: `R3*NEMF…*12698` = $126.98 of $325.60; Estes names a second SCAC, OVLD, with no share; ODFL names itself)" |
| M25 | Fallback | PDF boxes (SEFL C/L PRO, TForce ADV/BEY, ODFL ORIG/DEST I/L); partner's "CORR REPT" | **N** | 02-002 p. 33 "C/L PRO NO 34844332", DEST C/L "OAKH"; p. 41 DEST C/L "DAFG"; pp. 63, 94 "PYLE"; 21-015 l. 275 "ADV SCAC PRO# DATE BEY SCAC" (blank); 21-002 p. 17 ORIG I/L / DEST I/L boxes (blank). "PYLE CORR REPT 428" is a remark line on SEFL's own bill 628583681 (02-002 p. 60), naming the partner's correction report; the report itself is not held and the line carries no share | "… ; a partner's correction-report number printed as a remark on the SEFL bill ('PYLE CORR REPT 428', 02-002 p. 60); no partner share is printed on any PDF held" |
| M25 | Never | — | empty | — | — |
| M25 | If none | Carrier | KV | no PDF prints a share | — |

### §2.4 The dispute

| ID | Cell | Claim as written (short) | Verdict | Evidence | Corrected wording |
|---|---|---|---|---|---|
| D01 | Primary | Computed from P16/P17 + M04 (receipt of each bill) + F02 (ship date) + D07 (payment date for Walmart-style contracts) | KV (rule) | inputs re-opened: 02-002 p. 46 DATE BILLED 06/19/2023 → +180 = 2023-12-16; p. 41 05/05/2023 → 2023-11-01; ship 05/15/2023 → 2023-11-11 | — |
| D01 | Fallback | — | empty | — | — |
| D01 | Never | The reprint date | KV | 02-002 p. 33: "DATE BILLED 08/26/2025" on the reprint of the 06/19/2023 bill would give a 2026 deadline | — |
| D01 | If none | Derived; "unknown" if M04 is unknown | KV (rule) | — | — |
| D02 | Primary | The claim form or letter (set 23: 3PL letters; set 16: carrier forms; SF 1113) | KV | 23-006 p. 4 "PRESENTATION OF OVERCHARGE CLAIM" (claimant, own number SATCO-2300008OC, ship date, two PROs, billed/paid/correct/overcharge, "Duplicate Bill", "Date Submitted 03/28/2023", indemnification clause, "Claim Tariff Contract Authority:" blank); 23-003 p. 5 and 23-004 p. 4 (PRO, BOL, nature, no amount, no date); the seven set 16 forms and SF 1113 as listed in §1a | — |
| D02 | Fallback | The shipper's worksheet row (set 02 "OVER CHG") as a draft | KV | 02-002 p. 99 l. 7 header "CUSTOMER INV DATE PLT LIFTGATE SURCHARGE FRT CHARGE Need to Be Charged OVER CHG"; p. 210 l. 18 row 364 "807148067 5/15/2023 1 $55.00 $79.72 $362.38 $152.00"; p. 212 l. 6 "OVER CHG" column, p. 223 l. 19 "364 $ 210.38" | — |
| D02 | Never | — | empty | — | — |
| D02 | If none | The software fills it from M01, M04, M16, M18, P10 | KV (rule) | the forms' fields map onto those IDs (§1a) | — |
| D03 | Primary | The claim's attachments (set 23: BOL, shipper's weight certificate, spec sheet, inventory) | KV | 23-004 p. 5 BOL "GTZ BOL NO : 27205339"; p. 8 certificate: 2 crates 84×45×87, 190.31 ft³ each, 380.63 total, tare 636, gross 2153, net 1517, "Density: 3.99", "*WEIGHED ON CERTIFIED SCALE*"; 23-003 p. 4 BOL, p. 5 satellite image; 23-006 p. 4 "Attached Documentation" boxes all unticked | — |
| D03 | Fallback | — | empty | — | — |
| D03 | Never | A brochure or sample BOL (YRC refuses them) | KV | 16-095 l. 36-37 "Brochures and 'sample' bills of lading will not be accepted" | — |
| D03 | If none | Customer, carrier (certificate) | KV | the certificate in 23-004 is the shipper's; no carrier certificate behind a reweigh in any chain | — |
| D04 | Primary | The claim letter's date; the carrier's acknowledgement (no stand-alone one held; YRC's status page prints a received date, 23-006) | KV | 23-006 p. 4 "Date Submitted 03/28/2023"; p. 5 "Date Received: 03/28/23"; the 3PL letters (23-003 p. 5, 23-004 p. 4) are undated | — |
| D04 | Fallback | Email headers, portal records | KV | 21-002 p. 11: a carrier e-mail with a header date "Sent: Tuesday, March 01, 2005" recording the refund and re-bill; 23-006 p. 5 is a portal print | — |
| D04 | Never | — | empty | — | — |
| D04 | If none | Customer | KV | — | — |
| D05 | Primary | The carrier's answer (YRC "APPROVED" status with draft number; GlobalTranz's quoted decline "per YRC Tariff 100-754 … Self-Storage Warehouse") | KV | 23-006 p. 5 "This claim is in APPROVED status … Draft Number 1385879"; 23-003 p. 5 "declined per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse" | — |
| D05 | Fallback | ODFL's refund-and-re-bill history (set 21) as an implicit decision | KV | 21-002 p. 11 e-mail ("did receive the full refund … now billing to you for $1133.55"), pp. 13-15 A/R rows | — |
| D05 | Never | — | empty | — | — |
| D05 | If none | Carrier; no stand-alone denial letter or credit memo is public; YRC's page prints the draft date, not the decision date | KV | 23-006 p. 5 prints "Date Received", "Draft Date 06/20/23" and "sent to the claimant on 06/20/23", no decision date or reason. The two "CREDIT MEMO" pages in 21-012 (pp. 16-17) are a manufacturer's sales credit memos to a dealer, not a carrier's (§8) | — |
| D06 | Primary | The answer (YRC draft 1385879, $612.77, 06/20/23); A/R history (ODFL refunds $1,828.04 and $584.63) | KV | 23-006 p. 5; 21-002 p. 13 "2/15/05 REF OPAY … 1,828.04", p. 15 "2/26/05 REF OPAY … 584.63", details pp. 14, 16 | — |
| D06 | Fallback | Statement credit rows (Kuehne+Nagel item type A; RXO adjusted/credited columns) | KV | 21-013 p. 10 "A 15831 11/30/2021 … $ (301.94)"; 22-011 p. 4 "Adjusted_Amount Applied_Amount Credited_Amount" | — |
| D06 | Never | — | empty | — | — |
| D06 | If none | Customer AP | KV | — | — |
| D07 | Primary | The shipper's AP export or remittance | KA | none held | — |
| D07 | Fallback | A/R history in a carrier's claim (set 21); XPO "AMOUNT PAID"; statement cash posted; the 3PL's invoice and its payment to the carrier | KV | 21-002 p. 13 "1/27/05 CP CC … 2,412.67-", p. 15 "4/11/05 CP LBHP … 1,133.55- LOCKBOX RECEIPT"; 03-003 p. 12 "AMOUNT PAID: US $162.90"; 21-010 p. 4 "Net Cash Posted 528.19-"; 23-011 p. 4 "Invoice Amount Paid 864.92", "Check Number EFT000000010881" | — |
| D07 | Never | — | empty | — | — |
| D07 | If none | Customer only; never public | **N** | payer-side records do appear in public files: the consignee's check stub deducting the freight (21-002 p. 9, 11 Feb 2005, "ACC186834 … -2,412.67 AR CR VOUCHER") and its debit memo (p. 8); the 3PL's claim form with the amount paid and EFT number (23-011 p. 4); what is never held is a shipper's AP export as such | "Customer; a shipper's AP export is never public, though one consignee's check stub and debit memo (21-002 pp. 8-9) and a 3PL's paid-amount and EFT number (23-011 p. 4) are" |
| D08 | Primary | The shipper's spreadsheet (set 02 pp. 99-224) | KV | 02-002 p. 99 starts at row 1 (l. 7 header), p. 224 is the last worksheet page, p. 225 blank; row 364 at p. 210 l. 18 and p. 223 l. 19 | — |
| D08 | Fallback | A broker's dispute ledger (TQL, 23-010) | KV | 23-010 pp. 16-17: per PRO, amount, TQL PO, and a reason ("Overpayment due to reweigh", "… reclass", "… Liftgate", "… TONU paid twice", "… duplicate invoice", "… alleged residential delivery", …); pp. 7-15 claim lists by PRO; p. 6 "EXHIBIT A" summary ($275,915.66) | — |
| D08 | Never | — | empty | — | — |
| D08 | If none | Customer | KV | — | — |

**§2 cell counts:** 132 cells; 28 empty ("—"); of the 104 cells with a claim: **83 KEEP-verified, 6 KEEP-assumed, 15 NARROW, 0 DISCARD**; 9 cells also carry an ADD.

## §3 The §1 columns for M01-M25 and D01-D08 (Checks, Role, Need)

Test: does AK §3.2's "Data needed" for the named check(s) call for this fact (Checks)? Is the Role the one the fact plays in the pipeline (Role)? Does the Need match §1's own definition ("must = no DISPUTE verdict on the lines it feeds without it")?

| ID | Checks (as written) | Verdict | Role | Verdict | Need | Verdict | Evidence / note |
|---|---|---|---|---|---|---|---|
| M01 | all | KV | key | KV | must | KV | AK A2 "PRO, BOL, carrier, amount, dates"; every check joins on it |
| M02 | all | KV | key | KV | must | KV | AK A2 "carrier"; A3/A5 sender (AV §2.1) |
| M03 | A4 | KV | state | KV | must | KV | AK A4 "EDI B308 code or 'CORRECTED'" |
| M04 | G1, A4 | KV | clock | KV | must | KV | AK A4 "original bill date"; G1 windows run from receipt (AX §6) |
| M05 | F1 | KV | clock | KV | useful | KV | AK F1 "Due dates, pay dates, late-fee rule" |
| M06 | A5 | KV | price | KV | must | KV | AK A5 "BOL freight-terms box and bill-to"; picks P01 |
| M07 | B4 | KV | price | KV | must | KV | AK B4 "FAK table; BOL class and NMFC item" (the rated class is what is compared) |
| M08 | C1, B3 | KV | price | KV | must | KV | AK C1 "BOL weight …", B3 minimum |
| M09 | B2 | KV | price | KV | must | KV | AK B2 "discount; class; weight; lane" with the rate |
| M10 | A1 | KV | price | KV | must | KV | AK A1 "Invoice" (extensions) |
| M11 | B2 | KV | price | KV | must | KV | AK B2 "discount" |
| M12 | B3 | KV | price | KV | must | KV | AK B3 "Agreement minimum" |
| M13 | B8, B9 | KV | price | KV | must | KV | AK B8 fuel level, B9 "Invoice" (fuel base) |
| M14 | D1-D7 | KV | price | KV | must | KV | AK D1 "Accessorial schedule and waivers" against the billed line |
| M15 | C2 | KV | price | KV | must | KV | AK C2 "Tariff thresholds"; the fee line is the thing tested |
| M16 | A1 | KV | price | KV | must | KV | AK A1 |
| M17 | A4, A3 | KV | state | KV | must on a correction | KV | AK A4 (original matched), A3 "AP payment records; carrier statement" |
| M18 | C1, D2 | KV | trigger evidence | KV | must on a correction | **N** | By §1's own definition, "must" means no verdict without it; but §4.6 gives a verdict when M18 is missing ("Flag: unexplained change"), and two real SEFL corrections carry none (02-002 pp. 41, 63). "useful, and its absence is itself a flag" matches §4.6 |
| M19 | D2, B4 | KV | trigger evidence | KV | useful (fallback for F07, F09) | KV | chains A and B filled F07/F09 only from it |
| M20 | A7, B1, B5 | KV | key | KV | must when present | KV | AK A7 "Quote number, agreement ID, account" |
| M21 | A1 | KV | state | KV | must | KV | A1 cannot run on an incomplete bill (ABF pp. 75-76 two-page correction) |
| M22 | G1, A4 | KV | clock | KV | useful | KV | only TForce/UPS carry it |
| M23 | E1 | KV | trigger | KV | useful | KV | AK E1 "POD date and time"; F14 is the primary |
| M24 | F1, A3 | KV | state | KV | useful | KV | AK A3 "carrier statement", F1 pay dates |
| M25 | A3, A5 | **N** | price | KV | useful | KV | neither A3's nor A5's "Data needed" names the interline partner or share (AK ll. 139, 141); the row is kept by AV §2.1's own mapping, not by AK §3.2. Wording: "A3, A5 (AV §2.1; not in AK's data-needed lists)" |
| D01 | G1 | KV | clock | KV | must | KV | AK G1 "Carrier tariff, contract, statute" |
| D02 | G1 | KV | state | KV | must to file | KV | the forms' required fields (§1a) |
| D03 | C1, D2 | KV | state | KV | must to file | KV | AK C1 "W&R certificate; spec sheet"; the forms' attachment lists |
| D04 | G2 | KV | clock | KV | must | KV | AK G2 "Claim dates" |
| D05 | G2 | KV | state | KV | must | KV | AK G2 "decide in 60" |
| D06 | credit matching | **N** | state | KV | must | KV | "credit matching" is not an AK §3.2 check ID; the nearest are A3 (statement) and F1; or it is the pipeline's own close-out step. Wording: "A3 (credit matching; no AK ID)" |
| D07 | A2, A3, F1 | KV | state | KV | must for A3, F1 | KV | AK A3 "AP payment records", F1 "pay dates", A2 via 3PL |
| D08 | context | **N** | state | KV | useful | KV | not an AK check; harmless, but the column should say "none (context for G1/A2)" |

**§3 counts:** 99 entries (33 × 3): **95 KEEP-verified, 4 NARROW** (M18 Need, M25 Checks, D06 Checks, D08 Checks), 0 DISCARD.

## §4 The other claims assigned (§2.5, §3, §4.5-§4.6, the §5 chains, the §8 ledger)

### §4.1 §2.5, the join keys

| Where | Claim | Verdict | Evidence |
|---|---|---|---|
| §2.5 | Match on PRO first (strip dashes, SCAC prefixes, check characters, suffixes; with and without leading zeros) | KV | forms seen: `02902161435` on the BOL label and re-bill, `2902161435` in the A/R (21-002 pp. 6, 13, 17); `405-677016` on the face, `405677016` in the scan line (03-003 p. 11); `648-358429-6`, `670-438395-X` (21-006 p. 4); `RDWY349533831X` (21-013 p. 10); `1848869A` (22-012 p. 4); `8065404` / `8065404A` (22-015 p. 4); `3341783401` = load 33417834 + "01" (22-011 p. 4); N's `689201498` / `6892014980` (23-006 p. 4) |
| §2.5 | then BOL (zeros and punctuation stripped; split "63387,63388"; tokenise "502464982\|IDB61769\|954") | KV | 22-013 l. 213 "502464982\|IDB61769\|954", l. 258 "Bill of Lading Number: 502464982"; "63387,63388" is in 19-018 per AW §5 (not re-opened by me, F-scope) |
| §2.5 | then PO + ship date + consignee; TL: load or tender number, then trailer + pickup date | KV (rule) | Werner pair below is separable only by trailer/tractor/dispatch; Taylor "REF 1071942" = rate con "Load Number: 1071942" (22-012 pp. 4, 6) |
| §2.5 | **Never match on amount + date**: 23 of the 101 ABF bills share both with another bill | KV | `abf.py`: 9 groups, 23 bills, keyed by PRO (five at $256.54 on 08/07/2024: 165551759/-768/-771/-773/-774; four at $299.27 on 08/07/2024) |
| §2.5 | two TQL pairs and one Werner pair match on lane, amount and adjacent dates | **N** | the "TQL" pairs are in the **TQYL** 210 batch (19-034, a truckload SCAC per the catalogue, sent by BPTS): 34704009 / 34703959 both $4,319.60, Buffalo → Ontario, G62*86 20251207 / 20251206; 34688921 / 34688904 both $2,401.95, Weyauwega → Springfield, 20251202 / 20251203 (adjacent). The Werner pair 39060407 / 39100828 (22-008 pp. 7, 10) is $834.83 on the **same** pickup date 01/30/2023 and the same issue date 02/09/2023, same lane, 154 mi; they differ only by tractor (82318 / 79405), trailer (378044 / 387449), dispatch (DB498427VZ / DB539267VZ) and weight (33000 / 4444). Wording: "two TQYL (19-034) pairs on adjacent pickup dates and one Werner pair on the same date" |
| §2.5 | a rate confirmation's "Bill of Lading Number" holding the shipper's SID (set 22) | KV | 22-012 l. 488 "Bill of Lading Number: 76930091", l. 438 "PO Number: 4505279147"; the BOL p. 5 (per §5.6) carries "Bol Number 4505279147", "SID#76930091" |
| §2.5 | a Werner bill printing "RETURN" for the shipper number while its BOL says 104310 | KV | 22-008 p. 4 "SHIPPER NUMBER RETURN", trailer 64082, pickup 01/13/2023, 33000 lb; p. 5 BOL "SHIPPER'S NO. MUST SHOW ON BILL 104310" (handwritten and stamped), "Carrier 64082 Werner", 1-13-23, 33,000 |
| §2.5 | a freight-forwarder booking number standing in for a BOL number | KV | 21-006 l. 237 statement row "9/12/2022 T N1883348HKG PO# R AUG 2022 …", l. 444 "BL N1883348HKG" |
| §2.5 | child PROs per pallet (XPO 2025 DR) | KV | 21-004 p. 8 (an XPO Delivery Receipt, PRO 271-432501, 5 pallets, "CBR REWEIGH OF SHIPMENT FEE"); text l. 20 "CHILD PRO #'s: 2346-563892, 2346-563870, 2346-563881, 2217-432501, 2346-563866" |
| §2.5 | an older carrier's PRO on a billing advice reused as the BOL (TForce) | **D** | 21-015 p. 33 (TForce bill 546903626) prints "B/L NO. MIA95055"; p. 34 is "THE CUSTOM COMPANIES BILLING ADVICE" with "SHIPPERS NO. MIA 95055" and "PRO. NO. 16422968-00" (plus "6911973620"). TForce reused the advice's **shipper number**, not its PRO, as the B/L number; the older carrier's PRO sits on the same paper as TForce's affixed label "546 903 626 DTR", which is AW §5's separate PRO failure case. Wording: "the shipper number of another carrier's billing advice (MIA 95055) reused as TForce's B/L NO., with that carrier's PRO 16422968-00 on the same paper (21-015 pp. 33-34)" |

### §4.2 §3.1 rows, §3.2-§3.3 bullets, §3.4 derivations

| Where | Claim | Verdict | Evidence |
|---|---|---|---|
| §3.1 "Original total on a correction" | ABF prints old and new → XPO prints paid and balance → SEFL prints only the difference → derive; SEFL 806625953: $1,088.74 − $110.23 = $978.51 = the worksheet row | KV | 01-001 l. 6185-6187 ($326.60 → $300.52, −$26.08; 326.60 − 300.52 = 26.08); 03-003 p. 12 AMOUNT PAID 162.90 / BALANCE DUE 1,809.93; 02-002 p. 41 TOTAL 1088.74, PAY THIS AMOUNT 110.23; 1,088.74 − 110.23 = 978.51 (AV review B12 ties it to worksheet row 292) |
| §3.1 "Bill type" | Title → changed amount or payer on a known PRO → statement flag → B3-08; winner PRO + change; ODFL re-bill titled ORIGINAL INVOICE; SEFL 2025 "PAST DUE" reprints | KV (one N) | 21-002 p. 17; 02-002 p. 33 vs p. 46; B3-08 0/82. The "statement flag" step rests on Estes's empty Adj/BD column (§2 M03) |
| §3.2 M18 | the PDF bill only; no real 210 fills K1; SEFL's corrected prints sometimes carry nothing | KV | K1 0/82, NTE 0/82; 02-002 pp. 41 and 63 carry no reason |
| §3.2 M22 | "Previously invoiced on": TForce and UPS Freight reprints only | KV | §1a sweep: 21-015, 04-006, 04-007 only |
| §3.2 D05 | the carrier's decision and its date: the carrier's answer only; nothing on the bill side records it | **N** | 23-006 p. 5 is the only answer. But ODFL's re-bill records the carrier's acceptance of two correction requests on the bill side ("CBL DGB 2/14/05 … PER LETTER FROM THE SHIPPER", "CBL DGB 2/18/05 … PER LETTER FROM THE 3RD PARTY", 21-002 p. 17), which §2.4 D05 itself lists as an implicit decision. Wording: "… only a carrier's answer records a decision and its reason; a re-bill's remark can record that a correction request was accepted (ODFL 21-002 p. 17), never a decline" |
| §3.3 D07 | the shipper's payment: never public | **N** | as §2 D07 If none: 21-002 pp. 8-9 (consignee's debit memo and check stub), 23-011 p. 4 (3PL's paid amount and EFT number), 21-002 p. 13 (the carrier's record of a card payment) |
| §3.4 Discount % | DSC ÷ gross: ODFL 210 72.0% | KV | 188.00 ÷ 261.11 = 0.7200 (19-001 ST 0001) |
| §3.4 Fuel % | fuel $ ÷ net: ODFL 210 17.5% | KV | 12.79 ÷ 73.11 = 0.1749 → 17.5% |
| §3.4 Original total | new total − balance due: SEFL 806625953 $978.51 | KV | 1,088.74 − 110.23 = 978.51 (02-002 p. 41) |
| §3.4 Original weight | original net ÷ (1 − discount) ÷ rate: 2,430 lb | KV | 744.77 ÷ 0.097 ÷ 315.97 × 100 = 2,430.0 (the $744.77 is the worksheet's figure, p. 208 per AV B13; the bill p. 41 prints 2,720 only) |
| §3.4 Amount paid | total − balance due: XPO 266-489086 $150.00 | KV | 1,301.48 − 1,151.48 = 150.00; 21-005 l. 234 prints "AMOUNT PAID: US $150.00" |
| §3.4 Rate unit | weight × rate = charge: SEFL "60080" = $600.80/cwt | KV | 509 × 600.80 ÷ 100 = 3,058.07 (p. 46) |
| §3.4 Deficit weight | rated − actual: ODFL 1,000 − 833 = 167 lb | KV | 19-001 ST 0002 `L3*1000`, L0 weights 86 + 747 = 833, `L1**36.2*PH*6045****DAA` (167 × 36.2 = 60.45) |
| §3.4 TL fuel per mile | fuel $ ÷ miles: Werner $93.94 ÷ 154 = $0.61 | KV | 22-008 p. 4 "FUEL ADJ/MILEAGE 93.94", "MILES 154"; 0.610 |
| §3.4 First bill date (bound) | earliest "previously invoiced" entry, else "no later than" the earliest print: TForce 610384246 03/15/23 | KV | 21-015 l. 297-298: 06/07/23 then 03/15/23; ship 03-03-2023 (12 days) |

### §4.3 §4.5 points 2, 3, 5 and the §4.6 rows

| Where | Claim | Verdict | Evidence |
|---|---|---|---|
| §4.5 (2) | the 2023 balance-due prints in set 02 gave 180 days from their own receipt (about 2023-12-16 and 2023-11-01); the 2025 "PAST DUE" reprints gave none | KV | 02-002 p. 46 DATE BILLED 06/19/2023 + 180 = 2023-12-16; p. 41 DATE BILLED 05/05/2023 + 180 = 2023-11-01; p. 33 is a reprint (DATE BILLED 08/26/2025, PREPAID 591.10, "INVOICE PENDING") of the same PRO 807148067 |
| §4.5 (3) | SEFL 896789802 was corrected 452 days after shipment with no reason printed, p. 63; SEFL prints no first-bill date on a corrected print; no real post-180-day balance-due bill with its original was found | KV | p. 63 "CORRECTED INVOICE", SHIPMENT DATE 01/10/2022, DATE BILLED 04/07/2023 (text l. 43 "04/0712023"), no remark; (2023-04-07 − 2022-01-10) = 452 days; the print carries no earlier bill date; the exhibit holds no original for it |
| §4.5 (5) | when the first bill date is NOT REPORTED (SEFL and XPO corrected prints, ABF: no bill date printed), show "unknown, no later than" the earliest print or statement date | KV | SEFL corrected prints carry only their own DATE BILLED (pp. 41, 63); XPO prints no bill date (03-003 pp. 7, 11, 19; 21-005); ABF 0 of 101 |
| §4.5 worked numbers elsewhere | 807148067: 06/19 + 15 = 07/04/2023 due; ship-date rule 2023-11-11 | KV | computed; p. 46 PAYMENT DUE DATE 07/04/2023 |
| §4.6 M04 | first bill date missing: owed by carrier; clock unknown; "no later than [earliest print]"; computed from the bound | KV (rule) | consistent with the TForce ages (earliest entry 133-512 days after shipment on 4 of 8) and SEFL's reprints |
| §4.6 M18 | reason missing: owed by carrier; **Flag** unexplained change; show old and new totals, "no reason printed" | KV (rule) | 02-002 p. 41: old total derived 978.51, new 1,088.74, no reason. See §6 for the conflict with `doc-explanation.md` §4.2 ("ask the reviewer") and with §1's "must" |
| §4.6 D05 | carrier's answer missing: open claim; days since filing against 30/60; carrier's 30/60 days | KV | 23-006: received 03/28/23, draft 06/20/23 = 84 days; no acknowledgement date printed |
| §4.6 D07 | payment record missing: customer; not checkable (A2 via 3PL, A3, F1); "connect the AP export" | KV (rule) | no AP export held; §2 D07 |

### §4.4 The M and D rows of the six §5 chains

| Chain, row | Claim | Verdict | Evidence |
|---|---|---|---|
| A M01-M03 | p. 46 "FREIGHT BILL NO: 807148067", "BALANCE DUE INVOICE", "1 of 1"; p. 33 "PAST DUE INVOICE"; one bill, two prints | KV | rendered pp. 33, 46 |
| A M04, M05 | p. 46 footer "DATE BILLED 06/19/2023", "PAYMENT DUE DATE 07/04/2023"; labels garbled in the text layer, read by position | KV | render shows the labels legibly; text l. 44-49 prints `?AY TfiIS A.P3OUNT`, `R=?:IT T0:`, "06/1912023" |
| A M07-M16 | 509 × $600.80/cwt = 3,058.07; 88.15% = 2,695.69; net 362.38; LIFTGATE SVC 55.00; PVT RESIDEN 94.00; fuel 79.72; TOTAL 591.10 | KV | p. 46; 3,058.07 × 0.8815 = 2,695.69; 0.22 × 362.38 = 79.72; sum 591.10 |
| A M17 | PAY THIS AMOUNT 94.00 against TOTAL 591.10 → previously billed 497.10; worksheet 362.38 + 55 + 79.72 = 497.10 | KV | p. 46; p. 210 l. 18 row 364 "$55.00 $79.72 $362.38" |
| A M18 | "** PER GOOGLE EARTH THIS IS A PRA DLVY" | KV | p. 46 (two lines: "** PER GOOGLE EARTH THIS IS A PRA" / "DLVY") |
| A M22 | the 2025 reprint prints "PREPAID 591.10" and "INVOICE PENDING", the full total | KV | p. 33 |
| A M25 | p. 46 "DEST C/L OAKH"; p. 33 "SEFL 34844332 OAKH"; share NOT REPORTED | KV | p. 46 DEST C/L box "OAKH", C/L PRO NO blank; p. 33 "C/L PRO NO 34844332", "OAKH" |
| A D01 | from the balance-due print 2023-12-16; ship-date rule 2023-11-11; SEFL's own start date NOT REPORTED | KV | computed; SEFL 1090 has no claim item (AX §6; P-scope) |
| A D02, D08 | worksheet p. 210 row 364: 1 PLT, $55.00, $79.72, $362.38, "NEED TO BE CHG" $152.00, "OVER CHG" $210.38 (p. 223); suit claims "no less than $271,828.70", filed 10/07/2025 | KV, one N | p. 210 l. 18; p. 223 l. 19 "364 $ 210.38"; the "OVER CHG" header for that column block is on p. 212 l. 6 (and p. 99 l. 7); complaint text l. 412, 478, 521 "$271,828.70". Wording: '"OVER CHG" column (header p. 212, value p. 223)' |
| A D04, D05 | complaint p. 7 ¶9 "demanded … SEFL refused", undated; no written decision | KA | the complaint paragraph not re-opened by me (P/F validators' pages); no carrier answer is in the exhibit (consistent with the pages I opened) |
| A D07 | $497.10 paid, derived from M17; date and reference NOT REPORTED | KV | p. 46 (594.10 − 94.00 is not printed as paid; derived) |
| A sibling 806625953 | balance-due print 05/05/2023: 405 + 2,315 = 2,720 lb at $315.97/cwt; gross 8,594.39; discount 7,760.73; net 833.66; liftgate 55.00; fuel 24.00% = 200.08; total 1,088.74; PAY 110.23; no remark; echoes "CL150 NMFC 49880-" and "CL125 NMFC 49880-" both rated 70 | KV (+A) | p. 41. ADD: the gross is per article (1,279.68 + 7,314.71), see §2 M10; DEST C/L "DAFG" is a second interline example |
| A bill 806266163 (p. 94) | "T 1090C 610-100 1548.75 CF 5.76 PCF / AW 8920 CW 9292.5", "**SEFL W&I INSPECTED TO A CUBIC CAPACITY MOVE", three articles class 150, "MIN FRT CHG 3454.14", "Gross Charge is $27523.00 / Discount Percentage % 87.45 / Discount Amount $24068.86" in the description column, "PVT RESIDEN 575.00" | KV | p. 94 rendered; 1,548.75 × 6 = 9,292.5; 8,920 ÷ 1,548.75 = 5.76; 27,523 × 0.8745 = 24,068.86; 0.24 × 3,454.14 = 828.99 fuel; TOTAL 4913.13, PAY 2694.85 |
| B M03 | "*** BALANCE DUE INVOICE ***" | KV | 03-003 p. 11 |
| B M04 | not printed; "PAYMENT IS DUE BY 02/27/2021" → original billed about 02/12/2021 on 15-day terms | KV | p. 11; 02/27 − 15 = 02/12/2021 = SHIPMENT DATE |
| B M07-M16 | 660 × $284.22/cwt = 1,875.85; −468.96; net 1,406.89; FSC 26.00% 365.79; CBR 37.25; LP1-LP6 6 × 27.15 = 162.90; "TOTAL US $1,809.93 PREPAID"; the total excludes the late-fee lines above it | KV | pp. 11-12; 1,406.89 + 365.79 + 37.25 = 1,809.93; lines including late fees sum to 1,972.83; 0.015 × 1,809.93 = 27.15 |
| B M17 | "AMOUNT PAID: US $162.90 / BALANCE DUE: US $1,809.93"; the amount paid equals the six late fees | KV | p. 12; 6 × 27.15 = 162.90 |
| B M21 | p. 11 "(continued on next page)", p. 12 "page 9"; 2 pages, complete | KV | p. 11 footer "page 8", p. 12 "page 9" |
| B M25 | DR "ORIGIN NPB, DESTINATION NRM", advance/beyond blank; direct | KV | p. 14 |
| B D02, D04 | Form 410 pp. 1-3: the carrier's claim against the shipper, filed 10/13/2022, $14,879.18 | KA | pp. 1-3 not re-opened (the derived text covers pp. 2-3; the amount and date are in the catalogue row) |
| B sibling 326-343835 | CORRECTED INVOICE: 1,425 × $131.87 = 1,879.15, −469.79 (25%), net 1,409.36, FSC 30.75% = 433.38, CBR 39.40, APT 51.90, LP1-LP5 5 × 29.01 = 145.05, TOTAL 2,079.09 including the late fees, no amount-paid line; "PAYMENT IS DUE BY 12/16/2021" = the ship date | KV | pp. 19-20; 1,409.36 + 433.38 + 39.40 + 51.90 + 145.05 = 2,079.09; SHIPMENT DATE 12/16/2021 |
| C P01, M06 | 210 B3-04 `PP`; N1*BT Dalmation Press LLC, Florence AL | KV | 19-001 ST 0001 |
| C P04/M11, P12/M13 | DSC −188.00 → 72.0%; code 405 12.79 → 17.5% of net; on gross 4.9% | KV | 12.79 ÷ 261.11 = 4.9% |
| C M01, M02 | B3-02 `00902527924`; 214 B10-01 same; B3-11 / ISA-06 / GS-02 = ODFL; ISA-15 = `T` | KV | 19-001 ISA-15 `T`; 19-017 `B10*00902527924*00280740007194473*ODFL` |
| C M03 | original, by absence (no B3-08, no prior-bill reference) | KV | B3-08 empty; no N9 of an earlier bill |
| C M04 | B3-06 2012-10-15, 20 days after delivery | KV | `20121015`; 214 D1 `20120927`; 18 days after 09-27 by calendar, 20 counting from the 214's AF pickup? No: 2012-09-27 → 2012-10-15 = **18 days**. Wording: "18 days after delivery" |
| C M07, M08, M10, M16 | L7-07 `050`; L0 `650*G`; L1 26111; B3-07 `8590` = L3-05; 261.11 + 12.79 − 188.00 = 85.90 | KV | 19-001 ST 0001 |
| C M18, M19 | no free text at all (no L5, NTE, K1) | KV | ODFL's 34 transactions: 0 L5, 0 NTE, 0 K1 |
| C M21 | `SE*25*0001`; GS/GE 5 transactions | KV | 19-001 has 5 ST segments (ST 0001-0005; the file's count) |
| C M23 | B3-09 `20120927`, qualifier `017`; must not be read as actual | KV | 34/34 ODFL `017`; the 214 D1 equals it on this PRO |
| C M25 | `R3*ODFL*O`; no partner; contrast AAA Cooper `R3*NEMF*1*HARRISBURG…12698` | KV | 19-001; 19-009 ST 0014 |
| C contrasts | AAA Cooper 37685697: B3-03 and N9*BM; `L5*…LESS 78.00 PCT DISCOUNT`, `Fuel Surcharge 29.00 PCT`; `L7*1*CZAR*910…20120917*0562`; delivery 035; `R3*NEMF`, $126.98 of $325.60; 1,147.26 × 0.78 = 894.86; 252.40 × 0.29 = 73.20; ISA-15 `P`. Estes 2200302174: B3-03 `NS`; N9*PO 16720942; `DISCOUNT 84.0%`; `L1 298.86 LB`, 810 × 298.86/100 = 2,420.77; `SUF 24.05`; group total 1,218.85 | KV (one N) | 19-009 ST 0014 as listed (B3-07 32560; L1 114726 × 0.78 = 89,486 ✓; FUE 7320: net 114726 − 89486 = 25240 × 0.29 = 7319.6 ✓). 19-015 ST 60001: `B3**2200302174*NS*PP**20131120*52369`, `N9*PO*16720942`, `L5*1*DISCOUNT 84.0%`, `L1*2*298.86*LB*242077`, `L1*3***2405****SUF`. The "group total ST*980 … 1,218.85" I did not parse (a 980 is not a 210; my script skipped non-210 STs) → KA for that number |
| D M01 | BOL label; re-bill; A/R prints 2902161435 (leading zero dropped) | KV | 21-002 p. 6 label "02902161435 SFC"; p. 17 "Pro # 02902161435"; pp. 13-16 "Pro#: 2902161435" |
| D M03 | re-bill footer "ORIGINAL INVOICE"; a re-bill 77 days after the PRO date with two CBL remarks and a prior $2,412.67 bill to another payor in the A/R | KV | p. 17 PRO DATE 12/03/04, Invoice Date 02/18/05 (77 days); p. 13 "1/27/05 CP CC … 2,412.67-" |
| D M04 | "Invoice Date 02/18/05"; the first bill's date not in the file (before the 01/26/2005 debit memo) | KV | p. 17; p. 8 debit memo DATE 01/26/2005 referring to the ODFL PRO |
| D M06-M16 | bill-to Clamp-Swing Pricing (third party), "Col/Ppd P"; class 085; 2,472 lb; "13289" = $132.89/cwt; gross 3,285.04; 70% = 2,299.53; net 985.51; FUEL INCREASE 133.04; CORRECTED BILL OF LADING CHARGE 15.00; total 1,133.55 | KV (one N) | p. 17: BILL-TO# 76652 Clamp-Swing; class 085; 2472; 13289; 3285.04; "Discount Allowed: 70.00% 2299.53-"; 133.04; 15.00; Total 1133.55; 2,472 × 132.89/100 = 3,285.04; × 0.7 = 2,299.53; 133.04 ÷ 985.51 = 13.5%. "Col/Ppd: P" is printed on the A/R pages (pp. 13-16), not on the re-bill, whose column header reads "PREPAID". Wording: "… (third party; the A/R prints 'Col/Ppd: P', the re-bill's column header 'PREPAID')" |
| D M17, M24, D06, D07 | A/R pp. 13-16: consignee paid $2,412.67 by card 1/27/05; 2/14 reverses it and posts $584.63; refund $1,828.04 on 2/15/05; 2/18 re-posts $1,133.55 on the third party; refund $584.63 on 2/26/05; lockbox receipt $1,133.55 on 4/11/05; balance .00; 1,828.04 + 584.63 = 2,412.67 | KV | p. 13 (1/27/05 CP CC 2,412.67-; 2/14/05 RATE AR 2,412.67- and 584.63; 2/15/05 REF OPAY 1,828.04), p. 14 (refund detail 1,828.04), p. 15 (2/18/05 RATE AR 584.63- and 1,133.55; 2/26/05 REF OPAY 584.63; 4/11/05 CP LBHP 1,133.55- "LOCKBOX RECEIPT", balance .00), p. 16 (refund detail 584.63); 1,828.04 + 584.63 = 2,412.67 |
| D M18, M19 | the three remark lines plus "C/ADDITIONAL REDUCTION, ALLOWANCE OR ADJUSTMENT MAY APPLY"; description echo "NMFC #156600 S7 92.5 / OVER 15 DENS" against class 085 | KV | p. 17 ("DRP 12/09/04 CORRECT AS BILLED"; "CBL DGB 2/14/05 …"; "CBL DGB 2/18/05 …"; "C/ADDITIONAL REDUCTION, ALLOWANCE OR ADJUSTMENT MAY APPLY" printed twice) |
| D M21 | "Page 1 of 2" and "Page 2 of 2" on one PDF page; the total only on page 2 | KV | p. 17 |
| D D02-D05 | vendor's memo p. 7; ODFL e-mail p. 11 "did receive the full refund … now billing to you for $1133.55"; claim amendment p. 3; objection pp. 1-2; both corrections accepted | KV (pp. 7, 11); KA (pp. 1-3 not re-opened) | p. 7 fax memo ("issue a corrected bill of lading showing Prepaid, bill 3rd party"); p. 11 e-mail as quoted |
| D D08 | A/R p. 13, the vendor's handwritten "1. Initial payment … 2a. Partial refund … 2b. Remaining balance refund" | KV | p. 13 |
| D add-on Paper-Pak 14710702037 | "BILLED WT 2601LBS REWEIGHED WT 3215LBS", "WIW", "CAB REG 11/19/07 CORRECT AS BILLED"; class 050, 32.15 cwt × $58.47 = 1,879.81, 70% = 1,315.87, fuel 126.89 = 22.5% of 563.94, "CALL 72HRS IN ADV FOR DEL APPT" 7.50, total 698.33; at 2,601 lb the bill would be 566.39, so the reweigh added $131.94; statement 5/25/08: 698.33, net cash posted 662.90, remaining 35.43 | KV | 21-001 pp. 13-14 (PRO date 9/28/07; "DUP 6/30/08 RP"; "DISCOUNT ALLOWED 70.00% 1315.87"; 3215; 5847; 1879.81; 126.89; 7.50; 698.33); p. 7 row "14710702037 9/28/07 698.33 .00 662.90- .00 35.43"; 26.01 × 58.47 = 1,520.80, × 0.30 = 456.24, × 1.225 = 558.89, + 7.50 = 566.39; 698.33 − 566.39 = 131.94 |
| E M01 | N p. 4 "689201498" and "6892014980" (one bill keyed twice); G1 "6703485626"; G2 "6647373549" | KV | 23-006 p. 4; 23-004 p. 4; 23-003 p. 5 |
| E M02 | "Mail To : YRC (ROADWAY)"; BOL "Carrier: YRC"; debtor "YRC Inc." / "Yellow Corporation" | KV | 23-006 p. 4; 23-010 p. 4 "YRC Inc. (the 'Debtor')"; "Carrier: YRC" on the BOLs per the walk (F-scope) |
| E M14 | limited access $75.00; reweigh $382.08; only from the proof-of-claim's item 7 | KV | 23-003 p. 2 item 7 "$ 75.00"; 23-004 p. 2 "$ 382.08"; neither letter states an amount |
| E M16, M17 | N p. 4 "Billed Amount 612.77" twice; "Total Paid : 1225.54", "Correct Amount : 612.77", "Overcharge Amount : 612.77" | KV | p. 4 rendered |
| E M20 | claimant number "SATCO-2300008OC" (court form "SATCO2300008OC"); carrier claim 23009972; draft 1385879; G2 "YRC Claim # 23023786" | KV | 23-006 p. 4, p. 5, p. 2 text l. 13 "SATCO2300008OC"; 23-003 p. 5 |
| E D01 | N: 180 days from 09/20/2022 = 2023-03-19; claim dated 03/28/2023, day 189; G1 filed day 129 | KV | computed: 2022-09-20 + 180 = 2023-03-19; (2023-03-28 − 2022-09-20) = 189; (2023-11-09 − 2023-07-03) = 129 |
| E D02 | N carries claimant, own number, ship date, PROs, billed/paid/correct/overcharge, "Duplicate Bill … Keying error resulted in duplicate payment", "Date Submitted 03/28/2023", "Claim Tariff Contract Authority:" blank; the 3PL letters carry PRO, BOL, nature, no amount, no date | KV | 23-006 p. 4; 23-003 p. 5; 23-004 p. 4 |
| E D03 | N "Attached Documentation" boxes unticked, indemnity clause; G1 BOL, inventory, certificate "WEIGHED ON CERTIFIED SCALE"; G2 BOL, satellite image | KV | 23-006 p. 4; 23-004 pp. 5, 8 (inventory pp. 6-7 not re-opened); 23-003 pp. 4-5 |
| E D04 | "Date Submitted 03/28/2023"; "Date Received: 03/28/23"; acknowledgement date NOT REPORTED in all three | KV | 23-006 pp. 4-5 |
| E D05 | N "APPROVED status … approved for disbursement"; G2 declined, reason quoted; G1 unresolved; the decision date is not printed, only "Date Received", "Draft Date" and "sent … 06/20/23" | KV | 23-006 p. 5; 23-003 p. 5; 23-004 p. 4 "Unresolved Dispute" |
| E D06 | "Draft Number 1385879", "Draft Amount 612.77", "Draft Date 06/20/23"; whether cashed NOT REPORTED; the proof of claim for the same $612.77 says it was not | KV | 23-006 p. 5; catalogue/source.md "Claim 11113 (filed 9/20/2023, $612.77)" |
| E D07 | "Paid Amount 612.77" twice; no dates, check numbers or payee; the form asks for "photocopies of canceled drafts or checks" | KV (form wording per 16-095 l. 32) | 23-006 p. 4 |
| E clocks | 189 days; 84 days from receipt to draft, past 378.8's 60 | KV | (2023-06-20 − 2023-03-28) = 84 |
| E lessons | the Epiq register lists both GlobalTranz claims at $0.00 while the forms print $382.08 and $75.00 | KV | set 23 `source.md` rows 23-003, 23-004; forms p. 2 |
| F M01-M05 | "PRO. NO. 1848869A"; Taylor Truck Line, Northfield MN; "CUSTOMER COPY"; "INVOICE DATE 02/26/2026"; no due date (15 days from an unknown receipt) | KV | 22-012 p. 4 |
| F M09, M13, M16 | "FLAT RATE … $993.96"; "FUEL SURCHARGE $/MILE 332 Miles .47 $/Mile $156.04"; "Total: $1,150.00"; at 335.15 miles fuel would be 157.52 | KV | p. 4; 332 × 0.47 = 156.04; 335.15 × 0.47 = 157.52 |
| F M17 | proof of claim p. 2 $2,950.00 = 1,150.00 + 900.00 (p. 10) + 900.00 (p. 15: 673.05 + 445 × .51) | KV | p. 2 item 7 "2,950.00", item 13 "1,150.00"; p. 10 PRO 1773131A 711.42 + 449 × 0.42 (188.58) = 900.00; p. 15 PRO 1580296A 673.05 + 445 × 0.51 (226.95) = 900.00 |
| F M19, M20 | "Remarks: LOAD BARS/STRAPS** CHECK IN as Best Dedicated Solutions**"; "TRACTOR 1019 TRAILER 61336" | KV | p. 4 |
| F D01, D02, D04 | invoice by delivered + 45 = 2026-04-10; filed 03/12/2026, 16 days after delivery; a non-payment claim | KV | 2026-02-24 + 45 = 2026-04-10; (2026-03-12 − 2026-02-24) = 16; rate con l. 537-539 "more than FORTY-FIVE (45) days after DELIVERED services … will not be accepted" |
| F P18 (money side) | invoice "Terms are 15 Days from Receipt of Invoice"; broker p. 9 "30-DAY TERM" with quick-pay discounts | KV | p. 4; p. 9 "EMAIL 30-DAY TERM INVOICES …", quick-pay fees 5% / 3% / 2% |

### §4.5 The §8 ledger rows assigned

| Row | Claim (short) | Tag in doc | Verdict | Evidence |
|---|---|---|---|---|
| 1 | SEFL 807148067 figures, remark, B/L 51124115, dates, quote, "1 of 1" | verified (C) | KV | 02-002 p. 46 rendered: every value present (SHIPPER B/L NO 51124115; QUOTE #CWEN3E465; 05/15/2023; 06/19/2023; 07/04/2023) |
| 3 | 509 × 7.60/100 = 38.68 → 94; 8,920 × 7.60/100 = 677.92 → 575 | verified (C) | KV | recomputed: 38.684, 677.92; p. 46 $94.00, p. 94 $575.00. Also p. 60: 1,838 × 7.60/100 = 139.69 = "PVT RESIDEN $139.69" (an un-capped middle case) |
| 5 | 806625953: 2,720 lb billed, 2,430 derived, no remark; PAY 110.23 on 1,088.74 | verified (C) | KV | p. 41 rendered; 744.77 ÷ 0.097 ÷ 315.97 = 2,430.0; 8,594.39 × 0.903 = 7,760.73 |
| 6 | 806266163 cube line and figures | *assumed* | **now KV** | p. 94 rendered: "T 1090C 610-100 1548.75 CF 5.76 PCF", "AW 8920 CW 9292.5", "MIN FRT CHG 3454.14", "**SEFL W&I INSPECTED TO A CUBIC CAPACITY MOVE", "Gross Charge is $ 27523.00 / Discount Percentage % 87.45 / Discount Amount $ 24068.86", "PVT RESIDEN 575.00", three CLASS 150.0 articles 1893 / 4581 / 2446 lb (= 8,920) |
| 8 | XPO 405-677016 figures, "…ED PER WEIGHT CERTIFICATE", due 02/27/2021 | verified (C) | KV | pp. 11-12 rendered; arithmetic in §4.4 B |
| 13 | 72.0% and 17.5% derived; 261.11 + 12.79 − 188.00 = 85.90 | verified (C) | KV | 19-001 ST 0001; recomputed |
| 14 | AAA Cooper and Estes contrast values | *assumed* | **now KV** (one KA) | parsed from 19-009 ST 0014 and 19-015 ST 60001 (§4.4 C contrasts); only the "ST*980 group total 1,218.85" stays *assumed* (not parsed) |
| 15 | Winn-Dixie: BOL collect, 2,472 lb gross, class 250, NMFC 156600-3, 12/3/2004; re-bill 02/18/05 titled ORIGINAL INVOICE, class 085, 132.89, 70%, fuel 133.04, CBL 15.00, total 1,133.55, three remark lines | *assumed* (render) | **now KV** | 21-002 p. 6 (COLLECT ticked; DATE 12/3/2004; P.C. NO. 550038; NMFC 156600-3; class 250; 2304 net / 168 tare / 2472 gross); p. 17 as listed in §4.4 D |
| 16 | A/R history: 1,133.55 lockbox 4/11/05; 584.63 refund 2/26/05; 584.63 and 1,133.55 postings 2/18/05; 1,828.04 refund 2/15/05; 2,412.67 paid 1/27/05 | verified p. 15; p. 13 per agent | **now KV in full** | pp. 13, 14, 15, 16 rendered (§4.4 D) |
| 17 | 1,828.04 + 584.63 = 2,412.67 | verified (C) | KV | recomputed |
| 19 | Paper-Pak bill and statement figures | *assumed* | **now KV** | 21-001 pp. 7, 13, 14 rendered (§4.4 D add-on) |
| 20 | Yellow N: claim 03/28/2023, ship 09/20/2022, draft 06/20/23, $612.77 ×2; APPROVED; no decision date | dates verified; page content *assumed* | **now KV** | 23-006 pp. 4-5 rendered |
| 22 | GlobalTranz 16215 decline wording; claim $75.00 | *assumed* | **now KV** | 23-003 p. 5 ("declined per YRC Tariff 100-754 because this location is listed as a Self-Storage Warehouse"), p. 2 item 7 "$ 75.00" |
| 24 (invoice part) | Taylor: flat 993.96 + 332 × .47 = 156.04 = 1,150.00; rate con all-in 1,150.00; 335.15 miles → 157.52; "FREIGHT CLASS Van"; rate con "Bill of Lading Number: 76930091", "PO Number: 4505279147"; 48-h (p. 7) and 24-h (p. 8); in/out-times rule on p. 20; BOL 44,122 vs 43,529 | arithmetic verified; page content *assumed* | **KV** for the invoice, rate con and claim (22-012 p. 4 rendered; text l. 438, 440, 479, 488, 519, 533, 537-539, 1297); the BOL weights (p. 5) are F-scope and not re-opened by me |
| 46 | Epiq register $0.00 vs forms $382.08 and $75.00 | *assumed* | **now KV** | set 23 `source.md` rows; 23-004 p. 2, 23-003 p. 2 rendered |

**§4 counts:** 85 rows: **74 KEEP-verified, 5 KEEP-assumed** (chain A D04/D05 complaint paragraph; chain B Form 410 pp. 1-3; chain C's ST*980 total; chain D pp. 1-3; the "63387,63388" BOL in 19-018), **6 NARROW** (TQL→TQYL and the Werner pair's dates; §3.2 D05; §3.3 D07; chain A "OVER CHG" page; chain C "20 days" → 18; chain D "Col/Ppd P"), **1 DISCARD** (the TForce billing-advice case in §2.5). Of the 15 §8 rows, the 8 tagged *assumed* or part-assumed (6, 14, 15, 16, 19, 20, 22, 24, 46) are now re-opened and verified, except chain C's group total and the BOL weights of row 24.

## §5 Additions (new places, moved fallbacks, new facts), each with a drafted row

Drafted in the doc's own §2 table format (`ID | Fact | Primary | Fallback | Never | If none`), changes in **bold**.

1. **M04 first bill date, more places.** `| M04 | Bill date; first bill date | The earliest of: the first 210's B3-06 for that PRO; the PDF bill date (SEFL "DATE BILLED", ODFL "Invoice Date", **TL invoices' "ISSUE DATE" / "INVOICE DATE": Werner 22-008 p. 4, Taylor 22-012 p. 4, USA Truck 22-015 p. 4, Werner Logistics 22-013**); the earliest "PREVIOUSLY INVOICED ON" entry (TForce, UPS; newest first, can stop short); Estes statement "Freight Bill Date" **(21-007 p. 4) or YRC statement "Bill Date" (21-006 p. 5)** | Statement date (flag as late) | A reprint's date; ABF and XPO print no bill date | Mark the clock "unknown, no later than …" |`
2. **M05 due date, more labels.** Fallback unchanged; Primary adds **ODFL "Due Date" (21-002 p. 17), USA Truck "PAYMENT DUE" (22-015 p. 4), TForce "Payment Due ON RECEIPT" (21-015 p. 4); Taylor prints none (22-012 p. 4)**.
3. **M10 gross is per article.** Add to If none: **"Σ over articles of weight × rate, each rounded (SEFL 806625953: 1,279.68 + 7,314.71 = 8,594.39, not 27.20 cwt × 315.97 = 8,594.38; 02-002 p. 41)"**.
4. **M11 discount without decimal points.** Add to Primary: **SEFL 2020 "DISCOUNT PERCENTAGE 9100 / DISCOUNT AMOUNT 1031100 / GROSS CHARGE IS 1133077" (02-002 p. 49): 91.00%, $10,311.00, $11,330.77**.
5. **M13 fuel $ unlabeled in the charges column at SEFL.** Add to Primary: **"at SEFL the % is in the description ('LTL FUEL SURCHARGE OF 22.00%') and the $ sits unlabeled in the charges column (02-002 p. 46: 79.72), so it is read by position"**; and the TForce / UPS code form from §2 M13.
6. **M16 Never, a second penalty example with the base printed.** **"02-002 p. 60: PAY THIS AMOUNT $174.61 = PVT RESIDEN 139.69 + PENALTY/TARIFF DUE 34.92 (25%)"**.
7. **M18 more remark forms** (so a profile per carrier can list them): TForce "WAIVED INSPECTION", "04424-DTR ORIGINAL WGT/REWEIGH", "SHIPMENT WEIGHED AT DTR.", "537.33 CUBIC FEET", "12 LINEAR FEET", "SEC7 DEFAULT" (21-015 p. 33); ODFL "FBA DHE 8/08/07 FREIGHT BILL AUDIT", "CAB SRS 11/02/07 CORRECT AS BILLED", "ADDED SSC PER DR", "ODFL 6100 ITEM 158508 WITH ODFL 660", "ITEM 887 SORT AND SEGREGATE CHARGE PER" (21-001 p. 11), "W & I REWEIGH CORRECTE WEIGHT 1070 LBS" (p. 12), "DRP 12/09/04 CORRECT AS BILLED" (21-002 p. 17); SEFL "DELIVERED TO A PRIVATE RESIDENCE", "PYLE CORR REPT 428" (02-002 p. 60); ABF "W01/AUTH:Restore original weight//", "RATE DETERMINED BY RATEWARE", "ALLOWS LOWER CHARGE AT HIGHER WEIGHT" (01-001 l. 851-879).
8. **M23 Werner Logistics.** Primary adds **"Werner Logistics 'Pick Up Date / Delivery Date' columns (22-013 l. 212-213)"**.
9. **M24 statement fields by issuer** (the Primary cell lists five fields from five files; a per-issuer list is what a parser needs): TForce (aging, PRO/ship date/reference/P-C/amount/remarks, remittance "Reason"); Estes (Adj/BD, statement date, billed amount, freight bill date, statement no., BOL, PO, terms, balance); ODFL (freight charges, assessed LIQD, net cash posted, misc adj, remaining); Mode (18% interest, age, open balance); YRC (accessorial codes, tariff, bill/due/pickup dates, P/C); RXO (adjusted/applied/credited, days past due, load); Kuehne+Nagel (item type A/I, SCAC+PRO); UPS (invoice/payment/balance); a consignee's own statement with aging (21-002 p. 10).
10. **M25 partner examples.** Primary adds **Estes `R3*OVLD*D**LT**…` (19-015, no share)**; Fallback adds **SEFL "DEST C/L DAFG" (02-002 p. 41)** and corrects "CORR REPT" to a remark line on SEFL's bill (p. 60).
11. **D04 fallback has a real example.** Fallback: **"Email headers (ODFL's dated e-mail recording the refund and re-bill, 21-002 p. 11), portal records (YRC status page, 23-006 p. 5)"**.
12. **D07 payer-side records that are public.** Fallback adds **"a consignee's debit memo and check stub deducting the freight from the vendor (21-002 pp. 8-9); a 3PL's claim form stating the amount paid and the EFT number (23-011 p. 4)"**; If none reworded as in §2.
13. **§2.5 corrections** (text): "two TQYL pairs (19-034) on adjacent pickup dates and one Werner pair (22-008 pp. 7, 10) on the same pickup and issue date"; "the shipper number of another carrier's billing advice ('MIA 95055') reused as TForce's B/L NO., with that carrier's PRO on the same paper (21-015 pp. 33-34)".
14. **A money fact §1 lacks (for validator BC's completeness pass; drafted here because it is M-side):** `| M26 | Late-fee or penalty lines billed, their base and their rule reference (XPO "LP1 LATE FEE 30 DAYS PAST DUE" … "LP6", "TARIFF 199", 03-003 p. 11; SEFL "PENALTY/TARIFF DUE" = 25% of the base, 02-002 pp. 49, 60; ODFL "Assessed LIQD" on statements, 21-010 p. 4; RXO "AFTER 9/10/2025: 456.75", 22-011 p. 31; Mode interest, 21-014 p. 4) | F1 | price + state | useful |`. Today these lines fall under M14 "accessorial lines", but they are priced by P18, not by an accessorial schedule, and on XPO's balance-due print they are excluded from the total (03-003 p. 11) while on the corrected print they are included (p. 19), which M14 cannot express.

## §6 Inconsistencies with `doc-explanation.md` §4 and the field maps (listed, not resolved)

1. **M18 missing** (given in the brief): `doc-explanation.md` §4.2 "If neither has it, ask the reviewer" vs `doc-exploration.md` §4.6 "Flag: unexplained change".
2. **M18 Need "must on a correction"** (§1.3) vs §4.6, which issues a verdict (flag) when it is missing, and §1's own definition of "must".
3. **§3.2 D05 "nothing on the bill side records it"** vs §2.4 D05's fallback (ODFL's refund-and-re-bill history as an implicit decision) and the re-bill's own remarks recording accepted corrections (21-002 p. 17).
4. **§2.5 "two TQL pairs"** vs AV §5.2 "TQYL" (19-034); and the README's "one batch from TQL, a broker" vs the catalogue's "TQYL (truckload carrier SCAC)" for the same file. TQL the broker appears separately in 22-007 and 23-010.
5. **§2.5 TForce billing advice** vs AW §5 ("an older carrier's PRO on the same paper, 21-015 p. 34") and the bill itself (B/L NO. = the advice's shipper number MIA95055): the doc merged two failure cases into one wrong one.
6. **M13 and M15 "UPS '003570'" and "UPS '002550 INSPECTION'"** vs AV §2.2 whose column is headed "TForce / UPS Freight (21-015, 04-006)": both examples are on TForce's 2023 bill (21-015 l. 285, 589); UPS Freight's 2009-10 bills carry the same encoding with other values.
7. **M02 "ISA-06 / GS-02 (the envelope sender)"** vs AV §2.1 ("ISA-06 `BPTS` (a freight-payment firm), GS-02 `WIEL`"): GS-02 was the carrier in every real file.
8. **M14's code list** vs AV §2.1's (`DAA`, `MMC`, `400`, `STC` also occur; base-freight lines uncoded at all three LTL carriers per the AV review B7).
9. **M21 Never "SEFL p. 49 '1 of 3' with pp. 2-3 absent"** vs the AV adversarial review #13 / R3, which had already narrowed it (the 2020 layout's counter does not number pages; the pay gap is the penalty); `doc-explanation.md` §4.2 carries the narrowed wording, `doc-exploration.md` the old one.
10. **D07 "never public"** (§2.4, §3.3) vs §5.4's own M17/D07 rows (the carrier's A/R history and the consignee's card payment are in a public file) and 21-002 pp. 8-9, 23-011 p. 4.
11. **§5.4 M06 "Col/Ppd P"** attributed to the re-bill p. 17; it is on the A/R pages pp. 13-16; the re-bill's column header is "PREPAID".
12. **§5.3 C M04 "20 days after delivery"**: 2012-09-27 → 2012-10-15 is 18 days.
13. **Chain A D02 "OVER CHG" column p. 223**: the column header is on p. 212 (and p. 99); p. 223 carries the value.
14. **M25 Checks "A3, A5"** vs AK §3.2, whose data-needed lists for A3 and A5 do not mention an interline partner or share.

## §7 Concerns left unproven, or not testable offline

1. **Whether R3-08 is the partner's share or the biller's** (AV review concern): the same 39.0% on all five NEMF bills; only AAA Cooper's 210 guide or NEMF's statement would settle it. Not in `data/`.
2. **Whether TQYL is TQL's SCAC** and **what BPTS is**: web lookups (SCAC directory); not testable offline. The doc's "freight-payment firm" and "TQL" both rest on labels.
3. **M15 "Always printed when charged"** and **M15 fallback "210 coded line"**: no real corrected or fee-bearing 210 is held; a real balance-due 210 would test both.
4. **"No stand-alone denial letter or credit memo is public"**: a negative over the public record; I can only say none is in `data/` (the "CREDIT MEMO" pages in 21-012 are a manufacturer's sales credits).
5. **Chain C's "group total ST*980 … 1,218.85"** (19-015): my parser took 210 transactions only; the 980 was not parsed.
6. **Pages I did not re-open that the chains' D rows cite:** 02-002 complaint pp. 5-10 (¶9 "demanded … refused"); 03-003 pp. 1-3 (Form 410 date and amount); 21-002 pp. 1-3 (objection and claim amendment); 23-004 pp. 6-7 (inventory); 22-012 p. 5 (BOL weights 44,122 / 42,653 + 1,469). These are P/F-scope or claim-form pages; their values in the doc are consistent with the catalogue and `source.md` but stay *assumed* here.
7. **The "M" (XPO) and "MIN" (TForce) minimum markers** (M12 Primary): AV §2.2 cites them; I did not see one on the pages I rendered (03-003 pp. 7, 11, 19 are not minimum-charge bills; 21-015 p. 33 is rated).
8. **Chain F's "BOL p. 5" fields** and **chain B's BOL/DR pages beyond pp. 13-14** are F-scope.

## §8 Coincidence watch

1. **"CREDIT MEMO" in 21-012 (pp. 16-17)** looks like the carrier credit memo the doc says is not public; it is a manufacturer's sales credit memo to a dealer ("No post audit claims accepted"), a different document type under the same title.
2. **"TQL" in §2.5** is not the broker TQL (22-007, 23-010) but the SCAC TQYL in a BPTS→Target 210 batch (19-034).
3. **UPS vs TForce**: the doc's "UPS" code examples (M13, M15) are on TForce's 2023 bill; the two carriers share the layout lineage, so the examples are right in form but wrong in attribution.
4. **The SEFL 2020 counters** "1 of 3" (p. 49) and "1 of 30" (p. 60) on different PROs: a template field read as a page counter.
5. **The Werner pair** (22-008 pp. 7, 10): two bills identical in every printed money field, date and lane; only equipment, dispatch number and weight differ. A "duplicate" test on amount + date + lane would wrongly merge them; the doc's rule (never amount + date) is right, but its "adjacent dates" misdescribes this pair.
6. **The TForce reprint list and the statement** (21-015 pp. 4-5): the statement's "Invoice Date 8-08-23" and the bill's list entry "06/07/23 R1679027" are two prints of the same open balance; neither is the first bill (03/15/23).
7. **The five NEMF interline bills** all at 39.0% (AV review): consistent to the cent, which is why the share's direction cannot be inferred from the arithmetic.
8. **XPO "no bill date"** holds on two layouts (2021 image bills in 03-003; 2024 text bills in 21-005), so it is not an artefact of one scan.
9. **The two SEFL residential bills p. 46 and p. 60** both carry a quote, a liftgate line and a residential line with a Google-Earth/private-residence remark; p. 60 is a 2020 layout and p. 46 a 2023 one, so the remark pattern is the carrier's practice, not one clerk's.

