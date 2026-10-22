# Check BA · Adversarial review of the shipment-facts validation

Written 2026-10-18 (finished 2026-10-19). Adversarial review of `research/s5_check_BA_c09_fact_map_shipment_facts.md` (validator BA, the phase-2 shipment facts F01-F22 of `data/doc-exploration.md`). Method per the common brief: every citation behind the validator's KEEP-verified, NARROW, DISCARD and ADD verdicts was re-opened on the files in `data/`; every generalisation was re-tested on all files of its type; §5 was compared with the three raw walk reports; the validator's report was scanned for individuals' names and phone numbers. Read-only on `data/` and `research/` except this file; offline; no sub-agents; companies only. Verdicts: **CONFIRM** (the evidence says what the validator says), **OVERTURN** (it does not; counter-evidence given), **NARROW** (in part; corrected wording given), **could not test**.

## §0 Summary

**Counts** (this reviewer's own re-check; they replace the first pass's provisional counts, which had folded most KEEP-assumed cells into CONFIRM).
- **Validator §2, the §2.2 cells** (80 judged: 38 KV, 22 N, 20 KA). KV: **CONFIRM 38**. N: **CONFIRM 14, NARROW 6, OVERTURN 2**. KA: **5 testable and verified** on held files (F01 Never; F13, F14, F15, F16 If none), **1 partly verified** (F09 If none), **1 narrowed** (F22 Primary), **13 could not test** (no customer TMS, dock log, ELD or first-attempt record is held). The two overturns are the validator's own corrections, not the doc's: the FedEx 360 ¶6 DISCARD inside F04 If none, and the F10 Fallback narrowing on "QN#".
- **Validator §3, the §1.2 columns** (66 entries): **CONFIRM 66**, including its two NARROWs (F01 and F05 Checks), each checked against AK §3.2's "Data needed" column.
- **Validator §4.1, dataset-wide tests** (10 rows): **CONFIRM 5, NARROW 5**.
- **Validator §4.2, the §3/§4/§5/§8 claims** (77): **CONFIRM 72, NARROW 4, OVERTURN 1** (the §4.1 shipper-owed row's "FedEx 360 ¶6 not found").
- **Validator §5, additions** (9): **CONFIRM 6, NARROW 3**.
- EDI re-run with my own parser (`SCRATCH/baadv_scripts/edi_tally.py`, `edi_check2.py`): every 210 count reproduces (82 transactions in **18** files, not 17; B3-03, B3-04, B3-10, B3-12, N9, G62, L0-08, L5-03, K1); the 214 counts reproduce except the reason codes, which are **NS 36, BK 1, NA 1**.
- Privacy scan of the validator's report: no phone number, honorific, e-mail address or signer name.

**The five findings that matter most.**
1. **The validator's one discard is wrong.** FedEx Item 360 ¶6 is in both held FedEx files (13-050 and 13-051, l. 1014-1017, PDF p. 14): "6. When Consignor fails to state the freight terms (prepaid or collect) in writing on the Bill of Lading: A. Shipments originating from Canada … will move as collect … B. All other shipments will move as prepaid and all applicable charges will be borne by Consignor." The validator read ¶¶1-5 (l. 989-1012) and stopped at the page break. With TForce 361-A ¶3 (13-060 l. 1423-1425), the doc's F04 If none can be re-tagged *verified*, with the Canada exception added. ODFL's BOL guide pre-prints the same default (15-076 box 2, "FREIGHT CHARGES (defaults to prepaid)").
2. **"QN#" is in a held XPO text layer.** 21-005 prints `QN# 89.8DZ32430239999999999999` (and once `QN# 88.27DZ…`) in the CUSTOMER NUMBERS block on 7 lines (l. 219, 298, 374, 452, 698, 777, 1010; PDF pp. 4, 5, 8, 9, 17, 18, 25), four shipments (SN# 107856, 107857, 108929, 105392). The validator's narrowing of F10 Fallback is overturned; the doc's wording stands.
3. **Four of the validator's corrected wordings need correcting again.** (a) UPS Freight "NONE" in the B/L NO. field: **16 of 42** bills whose field I could read (04-006 OCR 5 of 8; 04-007 OCR 2 of 10; 24 bills in the `ocr_all` files read on renders, 9 of 24), not 7 of 24; P.O. NO. reads NONE more often (15 of the 24 rendered). (b) 214 reasons: **NS 36, BK 1, NA 1**; the NA is a WTVA appointment event (19-018 ST 000010003 `AT7***AB*NA*20121109*1000*LT`). (c) F06 Never: UPS 241325140's DR prints **both** weights ("WEIGHT DECLARED AS 00557 LBS. ACTUAL WEIGHT IS 00655 LBS.", 04-008 p. 6), so only XPO prints the reweighed weight alone. (d) F06 Fallback: the validator's "earliest message … 606 before 650" is unproven: all 18 ODFL 214 messages sit in one interchange dated 2012-10-15 11:44 (19-017 ISA-09/10, GS-04/05), after delivery, and no message carries its own send time; file order is not event order.
4. **Chain A's F07 row reports the rated class as the BOL's echo.** §5.1 lists "'APPAREL IT-49880' rated 'CLASS 70.0'" among the facts "all from the bill's echo of the BOL", but 70.0 is the SEFL FAK rated class (doc §2.2 F07 Never: "the rated class on the bill"). Walk A had it right ("actual declared class NOT REPORTED"); the sibling bill does echo the declared classes ("CL150 NMFC 49880-", "CL125 NMFC 49880-", 02-002 p. 41), p. 46 does not. The validator kept the row as KEEP-verified.
5. **Held documents the validator did not use change the F14-F18 and F22 cells.** ODFL's document API lists "Detention Certificate", "Lumper Certificate", "Delivery Receipt", "Delivery Photo" and "Delivery Appointment Document" as fetchable types (17-095 l. 137-159), an If-none source for F14-F17 and F22 the doc never names; carrier POD images are held (21-012 New Penn DRs, received date "3/16/22", "11 PCS", "3 refused dmg"; 24-004 Landstar "BOL and POD" pages); a UPS Freight **reconsignment BOL with a "DELIVERY ATTEMPTED? YES/NO" box** is held (04-009 p. 67), the nearest thing to F18's first-attempt record; UPS bills print **REDELIVERY CHARGE** lines (OCR, `ocr_all` stamps 145 and 345), so F18's "other carriers do not print the date" rests on more than TForce; a broker's **TONU confirmation** ($150, load 965638, 22-013 pp. 24-25) is held but prints no cancellation time; and TQL's terms give **5 business days** for detention, layover and lumper receipts (10-037 p. 14, l. 749-750, 756-758), the one held support for §4.6's "5-30 days".

Also corrected from the first pass of this review: the Holland certificate's "Tendered 151" does not equal the BOL's 149.59 kg; the stronger evidence that Holland read the BOL's kilograms as pounds is the bill itself, which rates "FISH SUP C125 61" and "C175 5" lb (21-006 p. 12) against the BOL's 60.958 kg and 5.302 kg lines (p. 13). The 2025 reprint p. 35 of SEFL 807307041 does carry "ORIG DEL ATTEMPT" in its text layer, garbled ("ORIG DEL ATTEP:iPT: 05/25/2023", l. 2094). And the validator's ADD #7 cites the wrong Holland bill: p. 12 is PRO 609-194236-2 (Pure Fishing); the PipingRock load of pp. 19-20 is PRO 670-438395-X, billed collect on **p. 18**.

## §1 Method

**Files opened** (file_id; PDF pages as the PDF counts; "text" = `data/derived/text/`, "OCR" = `data/derived/ocr/04_delphi_ups_freight/`):
- Doc and reports: `data/doc-exploration.md` (all 727 lines), the validator's report (all 308 lines), the three raw walk reports in the scratchpad (`walk_A_sets02_03.md`, `walk_B_sets19_21.md`, `walk_C_sets23_22.md`), `SCRATCH/id_to_path.tsv`, AK §3.2 rows A2, A6, A7, C1, D2, D3, E1.
- EDI (parsed with each ISA's own separators by my own script `baadv_scripts/edi_tally.py` and `edi_detail.py`, `python3 -I`): 19-001 to 19-015, 19-033/-034/-035 (82 210 transactions), 19-016 to 19-023 (16 214 keys, 38 AT7 events), 19-024 to 19-027 (four 204s).
- Text layers searched with `grep`/`sed` (line → page by form-feed count): 01-001 (all 129 pages parsed for Freight bill No / Shipment Date / AMOUNT DUE), 02-002, 10-035, 10-037, 10-039, 10-042, 10-043, 10-046, 13-047 (ABF 992, 993), 13-049 (Estes 567), 13-050 and 13-051 (FedEx Item 360 ¶¶1-10, 980 ¶¶2-3), 13-059 and 13-060 (TForce 361-A), 13-065 (SEFL 360-5, 753, 890-100), 13-072 (Dayton weight verification), every set 13 tariff for "copy of", "upon request", "certificate", "weight ticket"; 15-075, 15-076, 15-077 l. 52-55, 15-078 l. 226-231, 15-079 l. 1693-1697, 15-082 l. 35-52; 17-095 l. 136-162, 17-096 l. 840-853; 21-005, 21-006, 21-015; 22-006, 22-007, 22-012, 22-013; 23-003, 23-004; set 04 OCR (all ten files) for "B/L NO", "NONE", "NTEP", "serial", "device", "GUARANTEED DELIVERY REQUESTED", "Inspector ID"; `data/catalogue.csv` for lumper, letter of authority, ELD, dock log, TONU, cancel, quote.
- Pages rendered and read (reusing the validators' renders in `SCRATCH/renders/`, plus my own at 110 dpi: 04-006 p. 53; 10-046 pp. 4, 5, 6, 8; 05-015 pp. 2-6 at 60 dpi and all 48 pages at 40 dpi as a contact sheet): 02-002 pp. 35, 41, 46, 48, 60; 03-003 p. 14; 04-006 p. 53; 04-008 p. 7; 04-009 pp. 15, 16, 18; 05-015 pp. 1, 7 (+ pp. 2-6 montage); 06-016 p. 11; 10-037 p. 12; 10-039 p. 11; 10-044 p. 16; 10-046 pp. 4, 5, 6, 8; 15-076 p. 1; 21-001 pp. 11, 13, 14; 21-004 p. 8; 21-006 pp. 12, 13, 15, 19, 20, 21; 21-015 pp. 33, 34, 35, 36, 37; 22-008 p. 7; 22-015 p. 4; 23-004 p. 8. (A second batch is listed where it was added to §2.)
- Arithmetic re-done in `python3 -I` (chain E cube and densities, chain F weights and fuel, UPS densities, TForce density, SEFL derived weight, Paper-Pak lines, Winn-Dixie density, ODFL deficit).
- Privacy scan of the validator's report with `grep -E` for `[0-9]{3}[-.) ][0-9]{3}[-.][0-9]{4}`, `\(?[0-9]{3}\)?[ -][0-9]{3}-[0-9]{4}`, `\b(Mr|Ms|Mrs|Dr)\.? [A-Z]`, e-mail addresses, "ATTN", "signed by", "weigh-master", and for a list of surnames seen on the rendered pages (hit/no-hit only).

**Not done:** no web; no file under `data/` or `research/` touched except this report (`sha256sum -c data/SHA256SUMS` passes; re-run at the end of the second pass, every file OK); no individual's name, signature, e-mail or phone number transcribed, although the rendered pages carry many (rate-con contacts, drivers, inspectors, a weigh master, consignee contacts, an NTEP chair).

**Second pass (2026-10-19, this reviewer), on top of the above.**
- Every §0 finding of the first pass was re-opened: 13-050/13-051 l. 985-1020; 21-005 `grep -n "QN#"` (7 hits, pages by form-feed count); `edi_tally.py` re-run; 04-006 p. 53 render; 02-002 l. 2091-2094 and the p. 35 and p. 48 renders; 10-037 l. 740-758; 21-006 pp. 12, 13, 15 renders and l. 390-440.
- New scripts in `SCRATCH/baadv_scripts/`: `ln.sh` (prints a derived-text line with its PDF page), `edi_check2.py` (N9*PO and N9*BM per transaction, TL B3-03 against N9*LN, TL L0-08/-09 values, B3-09), `abf_dup.py` (the 101 ABF bills of 01-001 grouped by ship date and AMOUNT DUE).
- New renders in `SCRATCH/renders/baadv2/`: 25 UPS Freight bill pages from 04-008, 04-009, 04-010, 04-011, 04-012, 04-013 cropped to the P.O. NO./B/L NO. fields (montages `m1.png`, `m2.png`); 05-015 p. 7 at 200 dpi with crops of its two date stamps; 21-012 pp. 6-9 (New Penn DRs); 24-004 (`nemf_claim_209`) pp. 4-9; 04-009 p. 67 (UPS reconsignment BOL); 04-012 p. 8; 22-012 p. 5 at 150 dpi (freight-terms crop); 10-040 p. 1 (lower half).
- Renders read from the earlier sets: 02-002 pp. 35, 41, 46, 48; 03-003 pp. 11, 12, 13, 14, 15, 17, 19, 20, 21, 22; 04-008 pp. 6, 7, 8; 04-009 pp. 15, 16, 18, 19, 85, 89, 91; 05-015 pp. 1, 7; 06-016 p. 11; 10-036 p. 2, 10-037 p. 12, 10-039 p. 11, 10-040 p. 1, 10-041 p. 1, 10-044 p. 16, 10-046 pp. 4, 5, 6, 8; 15-076 p. 1; 21-001 pp. 11, 13, 14; 21-002 pp. 6, 17; 21-004 p. 8; 21-006 pp. 12, 13, 15, 19, 20, 21; 21-015 pp. 34, 35, 36, 37; 22-003 pp. 12-13; 22-008 p. 7; 22-012 pp. 5, 20; 22-013 p. 4; 22-015 p. 4; 23-003 p. 5; 23-004 pp. 5, 8; 23-006 p. 4.
- Text re-opened: 13-047/13-048 (ABF 992 ¶¶4-5, 993), 13-049 l. 540-560 and 2453-2460, 13-051 l. 485-495, 3340-3379, 13-060 l. 1412-1427, 4270-4292, 13-065 l. 547-550, 1360-1372, 2681-2687, 4574-4578, 4739-4760; every set 13 tariff for "certificate", "weight ticket", "scale ticket", "weight receipt", "copy of"; 15-075 l. 1-6; 15-077 l. 52-56; 15-078 l. 226-231; 15-079 l. 1693-1697; 15-082 l. 35-52; 17-095 l. 136-162; 17-096 l. 840-853; 01-001 (counts and l. 879, 987, 1504, 6434, 2054); 02-002 (residence, inspection, date-billed lines); 10-035, 10-042, 10-043, 10-044 (lumper and detention terms); 21-015 l. 271-944 (B/L NO. fields), l. 713-716, 836-849; 22-006 l. 197-200; 22-007 l. 249; 22-012 l. 200-240, 425-540; 22-013 l. 210-232, 250-272, 293-296, 790-846; 22-014 l. 196-199; 23-003 l. 236-281; 23-004 l. 196-203; the set 04 OCR (`ocr_all.txt` mapped to document and page by its court headers) for B/L fields, certificates, "REDELIVERY", "DELIVERY ATTEMPTED", "GUARANTEED DELIVERY REQ".
- Catalogue: searched `doc_types`, `format_notes` and `notes` for POD, lumper, TONU, cancel, ELD, detention, letter of authority, quote (sets 09, 10, 21, 22, 23, 24); the hits that bear on a KEEP-assumed cell were opened (21-012, 22-013, 22-019 by its note, 23-002, 24-004).
- Walk reports: walk A read directly; walks B and C decoded from their JSON strings into `SCRATCH/baadv_walk_B_sets19_21_decoded.md` and `SCRATCH/baadv_walk_C_sets23_22_decoded.md`.
- The doc reviewed is the 727-line version at `git show HEAD:data/doc-exploration.md` (saved as `SCRATCH/baadv_head_doc.md`), the text the validator read.
- Nothing under `data/` or `research/` was changed except this report; `sha256sum -c data/SHA256SUMS` re-run at the end: every file OK.

## §2 Per-claim table

Verdicts: **C** = CONFIRM, **N** = NARROW, **O** = OVERTURN, **CNT** = could not test. For the validator's KEEP-assumed (KA) cells: **KA→V** = a held file tests it and it holds (re-tag *verified*), **KA→N** = a held file tests it and it needs narrowing, **KA/CNT** = no file of that type in `data/`. Line numbers are in `data/derived/text/…` unless marked OCR; "p." is the PDF page.

### §2.1 The §2.2 cells (validator §2)

| Validator row | Validator | Mine | Evidence (re-opened) | Corrected wording |
|---|---|---|---|---|
| F01 Primary | KV | C | 15-075 l. 3 "Bill of Lading Number:" (top right; the validator's l. 4 is one off); 06-016 p. 11 box 2 "180926120044"; 04-009 p. 89 "5825.10"; 15-076 p. 1 box 6 "Assign a B/L#, LOAD# and PO# if applicable. These are not required"; 21-006 p. 13 "00286320003321169"; 04-008 p. 7 "62782"; blank on 03-003 pp. 13, 17, 21; 21-002 p. 6 has no such box | — |
| F01 Fallback | N | N | Counts reproduce: B3-03 filled ODFL 34/34, AACT 11/11, TL 34/34, `NS` EXLA 3/3; N9*BM on the 11 AACT transactions only; N9*PO on 82/82 transactions; L11*BM on 8 messages (HMES 2, WTVA 5, RNLO 1); B10-02 on 16/16 keys. But two parts of the corrected wording do not hold: (i) "the TL 210s put the load number there": B3-03 (e.g. 19-033 ST1 `100687708`) matches no N9 in the same bill (N9*LN is `2`; IV, PO, SO differ; 0 of 34 TL B3-03 values equal N9*LN), so its meaning is not stated in the file; (ii) the piped string "502464982\|IDB61769\|954" is on Werner Logistics' **invoice** (22-013 p. 4, "Customer Ref #" column, the "Bill of Lading" column **blank**), not on a rate con; the broker's rate con splits it ("Bill of Lading Number: 502464982", "Pickup/Delivery Number: 502464982/idb61769", p. 5). File count: 18 files (15 LTL, 3 TL), not 17 | "210 B3-03 (ODFL, AAA Cooper; the TL 210s fill it with a shipment ID the file does not label, carry no N9*BM); N9*BM at AAA Cooper only; N9*PO on every real 210; 214 B10-02 on every key, L11*BM only on Holland, WTVA and R+L 214s; the bill's B/L field or remarks; a TL invoice's reference field (tokenise: Werner Logistics 'Customer Ref # 502464982\|IDB61769\|954', its B/L field blank) and the rate con's reference fields" |
| F01 Never | KA | KA→V | Re-run on 01-001 (`abf_dup.py`): 101 bills parsed; **23 bills in 9 groups** share ship date and AMOUNT DUE (e.g. 08/07/2024 $256.54 on pp. 40, 49, 53, 55, 56; 08/07/2024 $299.27 on pp. 37, 42, 43, 50) | re-tag *verified* (AV §5.2's figure reproduces) |
| F01 If none | N | N | Estes 19-015 ST1-3 B3-03 `NS` ✓. TForce 21-015: NONE pp. 5, 10, 24, 39; a number pp. 15 "148262", 20 "26574543", 30 "6100354362", 33 "MIA95055" ✓ 4 of 8. UPS Freight: the validator's 7 of 24 does not reproduce. 04-006 OCR: NONE pp. 15, 23, 39, 49, **53** (rendered: P.O. NONE and B/L NONE), numbers pp. 69, 97, 101 (5 of 8); 04-007 OCR: NONE pp. 66, 108, numbers pp. 22, 34, 44, 60, 74, 84 ("??2716"), 88, 100 (2 of 10); the `ocr_all` files rarely OCR the B/L value, so I rendered all 24 readable bills there (`renders/baadv2/m1.png`, `m2.png`): NONE on 04-008 pp. 27, 91; 04-009 p. 65; 04-010 pp. 75, 87; 04-011 pp. 68, 94; 04-012 pp. 35, 55 (9 of 24); values such as "AL03", "57003228", "SKO 39785", "TO00236115", "46442-1". Total **16 of 42**. P.O. NO. reads NONE on 15 of the 24 rendered | "Estes 210 sends 'NS'; UPS Freight and TForce print 'NONE' in the B/L NO. field when none was given (UPS Freight 16 of 42 bills read; TForce 4 of 8), otherwise the shipper's reference" |
| F02 Primary | KV | C | 03-003 p. 13 "Date: 2/12/2021"; 21-002 p. 6 "12/3/2004"; 22-012 p. 5 "Date:02/23/2026"; 23-004 p. 5 "Shipment Date: 07/03/2023"; 06-016 p. 11 "09/26/2018", "Date received: 9/27/18". One more held gap of the same kind: 04-009 p. 18 shipping order dated "July 30, 2008", bill and DR "7-31-2008" / "07/31/08" (pp. 15, 16) | — |
| F02 Fallback | N | C | B3-12 filled 48/48 LTL, blank 34/34 TL; G62*86 on ODFL 34 + EXLA 3 = 37 of 48; AACT G62 22/35/41 on 11/11; 03-003 p. 12 and p. 11 "SHIPMENT DATE 02/12/2021"; 02-002 p. 46 "05/15/2023"; 21-002 p. 17 "PRO DATE 12/03/04"; 04-009 p. 15 "7-31-2008"; 21-015 p. 33 (text l. 811 block); 21-006 p. 12 "Shipment Date: 07/08/2022"; 9 AF events; DR headers 03-003 p. 14, 04-009 p. 16, 21-015 p. 35; Yellow DR "BILL DATE: 12/22/08" (05-015 pp. 1, 7) | — |
| F02 Never | KV | C | 02-002 p. 35 "PAST DUE INVOICE", date billed 08/26/2025 for a 05/22/2023 shipment; p. 48 the 06/22/2023 print; 03-003 p. 12 "PAYMENT IS DUE BY 02/27/2021" | — |
| F02 If none | KA | KA/CNT | No customer TMS export in `data/` (catalogue search) | — |
| F03 Primary | KV | C | 03-003 p. 13; 21-002 p. 6; 22-012 p. 5; 23-004 p. 5 | — |
| F03 Fallback | KV | C | N1*SH and N1*CN on 82/82 transactions; 214 N1 sets {SH,CN} 6, {BT,SH,CN} 6, {CN,SF} 2, {ST,SF} 2 keys, so a ship-from and a ship-to on 16/16; 03-003 p. 14 "VITAMIN SHOPPE"; ZIP 32254 (21-002 p. 6) vs 32205 (p. 17) | — |
| F03 If none | KA | KA/CNT | as F02 | — |
| F04 Primary | KV | C | 03-003 p. 13 "Prepaid X"; 21-002 p. 6 COLLECT marked, third-party block struck through; 22-012 p. 5 third-party bill-to Pepsi c/o Cass, terms blanks unfilled (see §4, chain F); 06-016 p. 11 "Third Party Prepaid ☒"; 04-009 p. 89 "Collect ☒"; 21-006 p. 13 Collect ☒, p. 20 "Third Party ☑"; 23-004 p. 5 "All charges prepaid to : GlobalTranz" | — |
| F04 Fallback | N | C | B3-04 on 82/82 (PP 48 LTL; TL PP 19, TP 12, CC 3); N1*BT ODFL 34 only; 21-002 p. 17 "CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER FROM THE 3RD PARTY"; 22-013 p. 4 / 22-012 p. 4 invoice "Bill To" = the broker; 22-015 p. 4 "PPD / COL: UNKNOWN" | — |
| F04 Never | KV | C | 04-009 p. 16 "BILL TO: 24068435" vs p. 15 "BILL TO: 32801414" | — |
| F04 If none | N (+ D of FedEx 360 ¶6) | **O** (the discard) | 13-050 and 13-051 l. 1014-1017 (p. 14), Item 360 ¶6, quoted in §0; TForce 361-A ¶3 at 13-060 l. 1423-1425 (the validator's l. 1424-1426 is one off) | "Customer; if blank the carrier bills prepaid to the shipper (TForce 361-A ¶3; FedEx 360 ¶6, except shipments from Canada, which move collect), *verified*" |
| F05 Primary | KV | C | 03-003 p. 17 "GRAND TOTAL 10 / 8567", order block 1+1+1+1+3+1+1 = 9, "1256 / 9", driver "9skd"; 22-012 p. 5 19 + 1 = 20, 1,844 + 42 = 1,886; 21-002 p. 6; 23-004 p. 5 | — |
| F05 Fallback | N | C | L0-08 filled ODFL 18 of 77 lines, AACT 11 of 14, EXLA 2 of 3; DR lines 03-003 p. 14 "DELIVERED 2 PCS", 04-009 p. 16, 21-015 p. 35 "PIECES DLVRD 6", 21-004 p. 8 "5 Of 5" | — |
| F05 Never | KV | C | 19-033 `30000*PLT` on 2 of 11 WIEL bills. Note: of the 34 TL L0-08 values, TQYL carries "1 PLT" twice and "56 PLT" three times, which a parser could take for counts; the rule ("never use") holds | — |
| F05 If none | KA | KA/CNT | — | — |
| F06 Primary | KV | C | 21-006 p. 13 both tables "WEIGHT (kg)", lines 5.302 / 60.958 / 65.23, "GRAND TOTAL 149.59"; 03-003 p. 13 "WEIGHT (LB) 590.48"; 21-002 p. 6. Sharper evidence for "with its header": Holland's bill rates "C125 61" and "C175 5" lb (21-006 p. 12), the BOL's 60.958 and 5.302 kg read as pounds | — |
| F06 Fallback | N | N | 204 AT8 19-025 `AT8*G*L*432*17`, `…*106*4`; 19-027 `AT8*G*L*42186**1335` ✓; bills 21-015 p. 33, 04-009 p. 15 "04117", 04-009 p. 85 "00650" ✓; XPO 03-003 pp. 11-12 print only 660 ✓; derivation 744.77 ÷ 0.097 ÷ 315.97 = 24.30 cwt ✓ (02-002 p. 208 l. 10366 "$ 744.77"), "2430" 0 hits ✓. The validator's "earliest message … 606 before 650" is unproven: 19-017's 18 messages are one interchange (ISA-09/10 `121015*1144`, GS-04 `20121015`), sent after delivery; no message carries a send time; ST order is not event order | "214 AT8: ODFL 00902527924 carries 606 lb on its AG (estimate) message and 650 on the AF, AB and D1 messages; no segment says which is declared or which came first" |
| F06 Never | N | N | XPO prints the reweighed weight alone (03-003 p. 14 "660", 21-004 p. 8 "10315" with CBR). UPS 241325140's DR prints **both**: "WEIGHT DECLARED AS 00557 LBS. ACTUAL WEIGHT IS 00655 LBS." with 655 in the column (04-008 p. 6); TForce both (21-015 p. 35); UPS 406858966 the declared 4117 with "AS WEIGHT 5000" (04-009 p. 16) | "The DR as the declared weight: XPO's DR prints the reweighed weight alone; UPS Freight and TForce DRs print 'WEIGHT DECLARED AS … ACTUAL WEIGHT IS …' once a reweigh precedes delivery, and the declared weight otherwise" |
| F06 If none | KA | KA/CNT | — | — |
| F07 Primary | N | C | 15-075 "LTL ONLY NMFC# CLASS"; 21-002 p. 6 "156600-3 / 250"; 21-006 p. 19 "157320-05 / 125"; 23-004 p. 5 "150 / 100240-1"; NMFC blank beside a class on 04-009 p. 89, 06-016 p. 11, 21-006 p. 13 (125, 200); no class column on 03-003 pp. 13, 17, 21; p. 21 "NMFC 072160 CLASS 60" handwritten below the signatures | — |
| F07 Fallback | N | C | 204 L5-03 only 19-025 (`157320-3`, `4620-5`); 02-002 p. 41 "CL150 NMFC 49880-", "CL125 NMFC 49880-"; 01-001 l. 879 (p. 17) "CL 100 ITEM 057300-03V (EX70)"; 21-015 p. 34 "LN 1 BOL CLASS 100"; 210 L5-03 1 of 82 (19-015 `186900`); AACT inside L5-02 ("BOOKS, NOI NMFC 161630", 19-009). Caveat in §3: the "partly real" 19-031 fills L5-03 on both its bills | — |
| F07 Never | KV | C | 02-002 p. 41 CL150/CL125 rated "CLASS 70.0"; 04-009 p. 89 class 100, billed 150 (p. 85) | — |
| F07 If none | N | C | as F07 Primary | — |
| F08 Primary | KV | C | 06-016 p. 11 "Dimension = 48 X 48 X 24", "TOTAL CUBE: 44"; 21-006 p. 19 "Vitamins (48L 40W 48H)"; 23-004 p. 5 87 / 45 / 87 | — |
| F08 Fallback | KV | C | 01-001: 101 "RATED DIMENSIONS" lines; 21-015 p. 33 handling-unit lines and "TOTAL CUBIC FEET: 537.326" (l. 849); 21-002 p. 17 "SW SKID DIMS: 44"X42"X51" EA"; 22-003 p. 17 crate lines not re-opened by the validator or me | — |
| F08 If none | KA | KA/CNT | — | — |
| F09 Primary | N | C | 15-076 p. 1 box 7 is a free-text line "Accessorial Services Requested: Liftgate Required, Call for Delivery Appointment, Inside Delivery, Protect from Freezing", with the code list ARN, CA, EXD, HYD, IDC, OVL, PFF, RDC beside it; 06-016 p. 11 box 5 liftgate ☒, others blank; 04-009 p. 89 box 5 all blank; 03-003 p. 21 "Appointment needed" (special instructions) and "Call 48 hrs. in advance for delivery appt." (additional shipper info); 23-003 p. 4 (l. 231) remarks | — |
| F09 Fallback | N | C | 204 NTE only on 19-026 (`TEST TEST …`) and 19-027 (placeholders); 02-002 p. 46 "*LIFTGATE DELIVERY"; 01-001 l. 1504 (p. 24) "MUST DELIVER ON 7/15/24"; 21-001 p. 13 "CALL 72HRS IN ADV FOR DEL APPT", p. 11 "SORTING OR SEGREGATING"; 01-001 l. 2054, 2495 quote-difference note (22 hits in all) | — |
| F09 Never | KV | C | 13-049 l. 2455-2459 (p. 51) | — |
| F09 If none | KA | KA→V (in part) | The tariff basis is in held text: SEFL 647 Note A (13-065 l. 1364-1372, "requested by any means whatsoever", "otherwise requested by one of the parties to the shipment at any point during transit"); Estes 567 ¶2 (13-049 l. 2458-2459, "a verbal request may be accepted with a written confirmation to follow"). No carrier record of a phoned request is held | "Customer; the carrier's record of a phoned request (SEFL 647 Note A, Estes 567 ¶2: *verified* as rules; no such record held)" |
| F10 Primary | KV | C | 15-076 p. 1 box 18 "Rate Estimate # 12345678", "Enter the rate reference number provided by OD" | — |
| F10 Fallback | N | **O** | 21-005 l. 219, 298, 374, 452, 698, 777, 1010 (pp. 4, 5, 8, 9, 17, 18, 25) `QN# 89.8DZ32430239999999999999` / `QN# 88.27DZ…` in the CUSTOMER NUMBERS block, four shipments; 02-002 p. 46 "QUOTE #CWEN3E465", p. 41 "#CWDV2BGFC", p. 48 "#CWEY44EC6"; 01-001 82 "PQ SCHEDULE NO" lines | keep the doc's wording ("QN#" verified on 21-005) |
| F10 If none | KA | KA/CNT | — | — |
| F11 Primary | KV | C | 06-016 p. 11 and 04-009 p. 89 "GUARANTEED DELIVERY REQUESTED (if box is checked)", blank; OCR: 4 hits in 04-006, 8 in `ocr_all` (one of them 04-009 p. 89), so 11 more pages ✓ (tick state on those 11 not re-checked); 15-076 box 16 "Required Delivery Date" | — |
| F11 Fallback | KV | C | 19-026 G62 37/38 `I 0830`/`K 1800`, 53/54 `G 0800`/`L 1430`; 19-027 37/38, 53/54; 19-025 37/38; 05-015 p. 1 "XPRS DATE: 12/29/08 DELIVER BY: 17:00 LOCAL TIME"; p. 7 "//DELIVER 01/05 OR 01/06 ONLY //EARLY DELIVERIES NOT ACCEPTABLE" | — |
| F11 If none | KA | KA/CNT | — | — |
| F12 Primary | KV | C | 04-008 p. 8 (241325140, 04/17/2008, CIN, 210/220/225, total 3 / 655); 21-015 p. 37 (735+755+835+820+735+785 = 4,665, 12/20/2022, DTR); 21-006 p. 15 (Tendered 151, Actual 360, Variance 209; dimensions "-") | — |
| F12 Fallback | KV | C (one example misread) | 04-009 p. 15 "ACTUAL WEIGHT IS 04825 LBS."; 21-015 p. 33; 21-001 p. 13 "BILLED WT 2601LBS REWEIGHED WT 3215LBS"; 03-003 p. 12 "…ED PER WEIGHT CERTIFICATE"; 19-017 ST2 `AT8*G*L*650`; DRs 04-008 p. 6, 21-015 p. 35, 03-003 p. 14. But 21-006 p. 12 "BILLED WGHT MINUS ACTUAL WGHT 140 LBS" is the **deficit line** of an AS-weight rating (360 + 140 = 500, "BILLED AS WEIGHT SEE CODE DEF 500 LBS"), not a reweigh statement; that bill's reweigh evidence is "WEIGHT INSPECTION CHARGE REWT 35.00" and the 360 total | drop the 21-006 p. 12 example or relabel it "deficit line" |
| F12 Never | KV | C | 04-009 p. 18 "Total 4,117 lbs" vs certificate 4,825 (p. 19) | — |
| F12 If none | N | N | FedEx 980 ¶2 at 13-051 l. 3346-3349 ✓; ABF 992 ¶5 $317.17 is at **13-048** l. 5634-5636 (in 13-047 it is l. 5608-5610); SEFL 992 $33 "only … while in the custody of the carrier" (13-065 l. 4745-4748); TForce 990 ¶¶3-4 $220 (13-060 l. 4287-4291); FedEx 990 $155 / $419 (13-051 l. 3371-3377; l. 491 is the index); ODFL API l. 143, 158 and TForce API l. 843, 851 ✓. Two items the validator missed, both selling a **certificate document** but not a copy of a reweigh record: ABF 993 "Weight Receipt, Certified", $55 "when ABF Freight is required to provide consignee with a weight certificate as a condition of performing delivery" (13-048 l. 5643-5648); Estes 105 Item 281 ¶3, $15.65 for a scale ticket on inbound convention-center shipments (13-049 l. 555-556). No other set 13 item promises a copy | "Carrier: FedEx 980 ¶2 promises a copy of the verification record; SEFL 992, ABF 992 ¶5, TForce 990, FedEx 990 sell a new weighing while the freight is in custody; ABF 993 and Estes 281 sell a weight certificate at delivery; the ODFL and TForce document APIs list weight, inspection and cube certificates" |
| F13 Primary | KV | C | 04-009 p. 19 54×41×32 ×5 = 205.00, weight 4825, density 20.08 (= 4,117 ÷ 205); p. 91 45.5×48×42 = 53.08, 515, 9.70; 21-015 p. 36 537.33 ft³, 6 units (4,665 ÷ 537.33 = 8.68) | — |
| F13 Fallback | KV | C | 01-001 "ABF MEASURED CUBE" 81 lines; 04-009 p. 85 "PLASTIC AUTO PARTS 9.70 PCF", "53.08 CUBIC FEET"; 21-015 l. 836 "ACTUAL DENSITY: 8.7 LBS/CUFT"; 02-002 p. 48 "** CLASS INSPECTION PER W&I **" | — |
| F13 Never | KV | C | 15-082 l. 37-51 (NTEP device evaluation, committee chair signature, no shipment) | — |
| F13 If none | KA | KA→V | Every inspection or cube certificate held is the carrier's own: UPS 04-009 pp. 19, 91; TForce 21-015 p. 36 | re-tag *verified* |
| F14 Primary | KV | C | 21-004 p. 8 "Delivered 5 Of 5 / Time 09:13 / Date 12/29/2025", typed | — |
| F14 Fallback | N (+ADD) | N | 19-017 ST4 `AT7*D1*NS***20120927*1107*CT`, 5 D1 events, ODFL only; B3-10 035 on 46, 017 on 34, blank on 2 WIEL (whose B3-09 is also blank); TL invoices 22-013 p. 4 "01-23-2025", 22-008 p. 7 "DELIVERY DATE - 01/30/2023", 22-012 p. 4, 22-015 p. 4 "7/11/2023", 22-006 l. 199 "4/27/2023" ✓; also Landstar Global Logistics bills print "DELIVERED 11/26/18", "DELIVERED 1/10/19" (24-004 pp. 4-7). The ADD's "consignee's receiving stamp" is not proven: the "JAN 05 '09 10:46" stamp on 05-015 p. 7 carries no name or label, and the DR's own delivery PCS/DATE/TIME box carries a second, partly legible date stamp ("JAN 0? 200?", `renders/baadv2/y7_crop3.png`) | "…; TL invoices that print it (Werner Enterprises, Werner Logistics, Taylor, USA Truck, Autumn, Landstar Global Logistics); a handwritten DR date; a date-time stamp on the DR (Yellow 05-015 p. 7, whose stamp is unlabelled)" |
| F14 Never | KV | C | 03-003 p. 14 consignee line "2/25/21", driver line "3/2/21"; ODFL B3-10 = 017 on 34/34 | — |
| F14 If none | KA | KA→V | Carrier POD images are held: New Penn DRs 21-012 pp. 6-9 (received date "3/16/22" handwritten, TIME blank); Landstar "BOL and POD" pages in 24-004; ODFL's API lists "Delivery Receipt" and "Delivery Photo" (17-095 l. 139-140) | re-tag *verified*; add "carrier document API (ODFL: Delivery Receipt, Delivery Photo)" |
| F15 Primary | N | C | XPO 03-003 pp. 14, 22, 21-004 p. 8; Yellow 05-015 pp. 1, 7; YRC 2022 21-006 p. 21 ("DELIVERY SERVICES PROVIDED NOT LISTED ABOVE": liftgate, sort/segregation, limited access, inside, residential, other); ODFL 21-001 p. 11 boxes; all unticked. "ADDED SSC PER DR" sits in the "Rate Clerk" remark block of the ODFL bill (21-001 p. 11, with "FBA DHE 8/08/07 FREIGHT BILL AUDIT", "CAB SRS 11/02/07 CORRECT AS BILLED"); 05-015 p. 1 "DRIVER ASSIST, SORT AND SEG NOTIFICATION VERIFIED BY [consignee] RECEIVING DEPT. YES ___ NO ___" | — |
| F15 Fallback | KV | C | 21-004 p. 8 "Driver Notes" box; 21-001 p. 11; 02-002 p. 60 "DELIVERED TO A PRIVATE RESIDENCE" (l. 3613) | — |
| F15 Never | KV | C | 06-016 p. 11 liftgate ☒ on the BOL, a request | — |
| F15 If none | KA | KA→V | Carrier PODs held (21-012 pp. 6-9) carry the service boxes ("LIFTGATE … SORT/SEGREGATION … LIMITED ACCESS … INSIDE … RESIDENTIAL … OTHER", unticked) | re-tag *verified* |
| F16 Primary | KV | C | 03-003 p. 14 stamp, signature, "DELIVERED 2 PCS"; 05-015 p. 7 "DROP TRAILER COUNT SUBJECT TO VERIFICATION UPON UNLOAD"; 21-006 p. 21 "RECEIVED BY - PRINTED NAME / SIGNED / DATE / TIME"; 22-012 p. 5 | — |
| F16 If none | KA | KA→V | 21-012 p. 8: a carrier POD with signature, received date "3/16/22", "11 PCS" and "3 refused dmg" written on it | re-tag *verified* |
| F17 Primary | KV | C | 10-035 l. 36-37; 10-043 l. 57-58; 22-012 p. 20 and l. 475-479; 10-039 p. 11; 10-044 p. 16; 10-046 p. 5; 22-003 p. 12 (small print) | — |
| F17 Fallback | N (+ADD) | C | 04-009 p. 16 ODOM/ARRIVE/DEPART "546 / 1237 / 1257"; 21-015 p. 35 boxes filled by hand; 05-015 pp. 1, 7 WAIT TIME blank, p. 7 "TIME ARRIVED AT CONSIGNEE TO MAKE DELIVERY ___"; labels 04-008 p. 7 "286 / 618 / 634", 04-009 p. 18 "688 / 1636 / 1714", blank on 04-009 p. 89; X1 on WTVA keys only (3), D1 on ODFL keys only (5) | — |
| F17 Never | KV | C | 01-001 l. 987 (p. 18) "DETND/140 42.71", l. 6434 (p. 78) "DETND/100 42.36". A further example: Landstar Global Logistics bill 0893044 "DETENTION 112.50", no times (24-004 p. 4) | — |
| F17 If none | N | C | as F17 Fallback; add that ODFL's API lists a "Detention Certificate" and a "Delivery Appointment Document" (17-095 l. 138, 141), a carrier record the If-none cell does not name | (validator's wording) + "; carrier document API (ODFL: Detention Certificate)" |
| F18 Primary | KA | KA/CNT (with a near miss) | No first-attempt DR and no attempt status in the 8 real 214s (codes X6, AG, AF, AB, D1, X1, X2, X3, X4; 19-036, a template, has LY and RD). Near miss: a UPS Freight **Reconsignment Bill of Lading** with a "DELIVERY ATTEMPTED? YES ☐ NO ☐" box, storage days and a dated reconsignment authorization (04-009 p. 67, PRO 437730963; same form by OCR at `ocr_all` stamps 331 and 387) | add "the carrier's reconsignment BOL (UPS Freight: 'Delivery attempted? yes/no')" as a fallback |
| F18 Fallback | N | C | 02-002 p. 48 (06/22/2023 print) "ORIG DEL ATTEMPT: 05/25/2023", "REDELIVERY 80.00"; p. 35 (08/26/2025 reprint) same, text layer garbled at l. 2094; p. 67 "ORIG DEL ATTEMPT: 11/21/2022" (l. 4003); p. 69 garbled (l. 4091); TForce "016575 REDELIVERY CHARGE 165.75", no date (21-015 l. 715, p. 30) | — |
| F18 If none | KA | KA/CNT | — | — |
| F19 Primary | KV | C | No document states premises type; 23-003 p. 4 l. 231 remarks only | — |
| F19 Fallback | KV | C | 02-002 p. 60 consignee "OCEAN WAVES CITY WHSE" (l. 3591), "DELIVERED TO A PRIVATE RESIDENCE" (l. 3613); p. 46 "PER GOOGLE EARTH"; 03-003 p. 14 stamp; 23-003 p. 5 image and sentence | — |
| F19 Never | KV | C | 13-065 l. 2682-2686 "will not relieve"; DR residential boxes blank in every DR viewed (also 21-012) | — |
| F19 If none | KA | KA/CNT | [our call] | — |
| F20 Primary | N | C | 22-012 l. 431 "Load Number: 1071942", l. 440 "Distance (Miles): 335.15", stops with expected dates and appointment times (l. 492-509); 22-013 l. 250, 256 "954354", "1,432.07"; 204 S5 4/4, G62 4/4; L11*MI only in 19-026 (`233`, `756`), whose NTE reads "TEST TEST …"; 19-024/-025 no L11; 19-027 L11 without MI | — |
| F20 Fallback | N | C | 22-012 l. 221, 235 "REF 1071942", "332/332"; 22-008 p. 7 "DISPATCH NO. DB498427VZ", "MILES 154"; 22-013 p. 4 "Tour # 4001028440", Stops/Miles block empty; 22-015 p. 4 "ORDER #: 8065404", no miles | — |
| F20 Never | KV | C | 22-003 p. 12 LEI confirmation HAWB ATL 113077, Montpelier IN → Elk Grove Village IL, 213 miles, $500; p. 13 invoice 5207, HAWB ATL 113224, Bensenville IL → Waukesha WI, $500, issued by a different carrier name than the confirmation's | — |
| F20 If none | KA | KA/CNT | — | — |
| F21 Primary | KV (204) | C | 19-027 `L3*42186*G*2377.08*FR*237708`, `N1*BT*Seaboard Foods`; 19-026 `L3*7000*G*989*FR*98900` (test-marked) | — |
| F21 Fallback | KV | C | 22-015 p. 4 USA Truck to Tupperware c/o Envista, $5,150.00; 22-008 p. 7 Werner Enterprises to World Kitchen, $834.83 | — |
| F21 Never | KV | C | Read: 10-035 l. 36 (C.H. Robinson); 10-036 p. 2 (C.H. Robinson → Floyd Inc); 10-037 p. 12 (TQL → Pink Cheetah Express); 10-039 p. 11 (U.S. Xpress Logistics → Transport Systems); 10-040 p. 1 (Scotlynn → Dray Hub); 10-041 p. 1 (Landstar Ranger carrier tender); 10-042 l. 37 (King of Freight → Viva Express); 10-043 l. 10 (KCH → CJ Logistics); 10-044 p. 16 (Skyway); 10-046 p. 4 (Yellow Logistics → RMW Expeditors); 22-003 p. 12 (LEI → Silver Arrow Express); 22-012 l. 431, 22-013 l. 250, 22-014 l. 197-198 (BDS) | — |
| F21 If none | KA | KA/CNT | — | — |
| F22 Primary | KA | KA→N | No lumper receipt, layover record or cancellation-time record is held, but a broker's **TONU confirmation** is: BDS load 965638, dated 02/25/2025, "Net Freight Charges USD 0.00 … TONU Fixed Cost 1.00 USD 150.00" (22-013 pp. 24-25, l. 803-843), with no cancellation time. Also TONU lines: 22-019 (Landstar Ranger "TRUCK ORDERED NOT USED 250.00", per its catalogue note; scan not opened) and a TONU dispute letter 23-002 (l. 202-206). ODFL's API lists a "Lumper Certificate" (17-095 l. 153) | "The receipt; the carrier's or broker's notice record (a broker's TONU confirmation is held, 22-013 pp. 24-25, and prints no cancellation time); carrier document API (ODFL: Lumper Certificate)" |
| F22 Fallback | KV | C | 01-001: 54 "LUMPER" hits; 10-037 p. 12 "Layover … Flat … $300.00"; 22-007 l. 249 "UNLOADING 451.00" (and 5 more UNLOADING lines, l. 295-573). Further face-value lines: TForce "LUMPER CHARGE / DST 28.00" (21-015 l. 590); BDS TONU $150 (22-013 l. 843) | — |
| F22 If none | KA | KA/CNT | — | — |

### §2.2 The §1.2 columns (validator §3; 66 entries, one row per fact)

Source for every row: `research/s5_check_AK_c09_audit_workflow_and_products.md` §3.2, l. 138-176 ("Data needed" column). Role and Need are design calls; I confirm them where the AK row's data list is consistent with them.

| Fact | Validator (Checks / Role / Need) | Mine | Evidence | Note |
|---|---|---|---|---|
| F01 | N / KV / KV | C / C / C | A2 "PRO, BOL, carrier, amount, dates; file fingerprint"; A6 "TMS or ERP shipment list"; A7 "Quote number, agreement ID, account" (its note: quote numbers "must be on the original bill of lading", i.e. F10) | the NARROW (A7 → F10/M20) holds |
| F02 | KV ×3 | C ×3 | B1 "Every version with effective dates"; B8 "… pickup date"; G1 window start | — |
| F03 | KV ×3 | C ×3 | A6; D2 "delivery receipt notes" | — |
| F04 | KV ×3 | C ×3 | A5 "BOL freight-terms box and bill-to"; A3's own data list is "AP payment records; 3PL invoices; carrier statement", so the A3 link is inferential (a third-party payer) | — |
| F05 | N / KV / KV | C / C / C | C1 "BOL weight, class, dims; W&R certificate; spec sheet" (no pieces); 03-003 p. 17 vs p. 15 (BOL 10, billed 9 PCS) | the NARROW holds |
| F06 | KV ×3 | C ×3 | C1; B3's list is only "Agreement minimum", but a minimum-charge test needs the weight | — |
| F07 | KV ×3 | C ×3 | B4 "FAK table; BOL class and NMFC item" | — |
| F08 | KV ×3 | C ×3 | C1 "dims"; B3 via a cube minimum (SEFL 610-100, doc §5.1 P07) | B3 link thin, not wrong |
| F09 | KV ×3 | C ×3 | D2 "BOL tick boxes, booking options" | — |
| F10 | KV ×3 | C ×3 | B5 "Quote document or ID; BOL"; A7 | — |
| F11 | KV ×3 | C ×3 | E1 "Guaranteed service ordered"; E2 "appointment" | — |
| F12 | KV ×3 | C ×3 | C1 "W&R certificate" | — |
| F13 | KV ×3 | C ×3 | C1; B4 | — |
| F14 | KV ×3 | C ×3 | E1 "POD date and time"; E2 "POD"; D3 "arrival, appointment and departure times" (D3 leans more on F17) | — |
| F15 | KV ×3 | C ×3 | D2 "delivery receipt notes" | — |
| F16 | KV ×3 | C ×3 | D2 | — |
| F17 | KV ×3 | C ×3 | D3 | — |
| F18 | KV ×3 | C ×3 | AX §5 Redelivery row (the validator's cite); D2's name does not list redelivery, D1 covers accessorials generally | — |
| F19 | KV ×3 | C ×3 | D2 "(liftgate, residential, inside, limited access)" | — |
| F20 | KV ×3 | C ×3 | B6; B7 "stop sequence"; D4 "Stops on the rate confirmation or BOL"; D3 | — |
| F21 | KV ×3 | C ×3 | B6 "Rate confirmation or contract" | — |
| F22 | KV ×3 | C ×3 | D5 "Cancellation time; rate confirmation terms"; D6 "Appointment and arrival records"; D7 "Lumper receipt" | — |

### §2.3 Dataset-wide tests (validator §4.1; 10 rows)

| Test | Validator | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| F01: B3-03, N9*BM/PO on all real 210s | counts | N | Counts reproduce (`edi_tally.py`). "82 transactions in 17 files" is 18 files (14 baldr ODFL/AACT, 1 EXLA, 3 TL); "the load number on all 34 TL bills" is not labelled in the file (see §2.1 F01 Fallback) | "82 transactions in 18 files … the TL bills fill B3-03 with an unlabelled shipment ID" |
| F01: "NONE" on UPS and TForce | 7 of 24; 4 of 8 | N | TForce 4 of 8 reproduces; UPS 16 of 42 (§2.1 F01 If none) | "UPS Freight NONE on 16 of 42 bills read" |
| F14: B3-09 with B3-10 | counts | C | 017 ODFL 34; 035 AACT 11, EXLA 3, TQYL 20, SPXQ 3, WIEL 9; B3-09 and B3-10 blank on 2 WIEL | — |
| F14/F17: AT7 codes on real 214s | 38 events; NS 37, BK 1 | N | Events and status codes reproduce (AF 9, AG 7, X6 6, AB 4, D1 5, X1 3, X3 2, X2 1, X4 1); reasons **NS 36, BK 1, NA 1** (19-018 ST 000010003); X1 only WTVA, D1 only ODFL, no key with both ✓ | "Reason codes: NS on 36, BK on 1 (19-017 ST 0017), NA on 1 (19-018 ST 000010003, an appointment event)" |
| F12: certificates held, device named | counts; no device ID | N | No certificate names a device ID or NTEP number ✓ (04-008 p. 8, 04-009 pp. 19, 91, 21-015 pp. 36-37, 21-006 p. 15 viewed). The coverage premise is wrong: `ocr_all.txt` carries the headers of Doc 20041 (04-011, "Pg 2 of 117" … "Pg 117 of 117", l. 9715-13348) as well as 04-008, -009, -010, -012, -013, -014, so 04-011 **is** OCR'd (7 "WEIGHT CERTIF" lines fall in it); the per-file OCR texts for those seven files hold court headers only. The counts remain OCR keyword counts, not page views | "… `ocr_all.txt` covers 04-008 to 04-014, including 04-011 …" |
| F06: DRs printing reweighed vs declared | lists | N | UPS 241325140 (04-008 p. 6) prints both, not the reweighed alone (§2.1 F06 Never) | as §2.1 F06 Never |
| F09/F15: Never rules BOL vs DR | no DR box ticked anywhere | C | 03-003 pp. 14, 22; 21-004 p. 8; 05-015 pp. 1, 7; 21-006 p. 21; 06-016 p. 11; and the New Penn DRs 21-012 pp. 6-9 (boxes unticked) | — |
| F19: any document states premises type | none | C | 02-002 pp. 46, 60; 23-003 p. 5 (l. 269-274) | — |
| F21: every rate con broker-to-carrier | 15 read | C | 13 re-opened (§2.1 F21 Never); none is shipper-issued | — |
| Sets outside the chains (204 segments) | S5 4/4, G62 4/4, L11 2/4, AT8 4/4, L5 NMFC 1/4, L3 charge 2/4 | C | `edi_tally.py` 204 block: L11 only on 19-026 and 19-027; L3 charge only on 19-026 (989) and 19-027 (2377.08); L5-03 only on 19-025 | — |

### §2.4 The §3, §4, §5 and §8 claims (validator §4.2; 77 rows)

| # | Where / claim | Validator | Mine | Evidence | Corrected wording |
|---|---|---|---|---|---|
| 1 | §3.1 Weight: precedence; XPO 590.48 → 660, UPS 4,117 → 4,825, SEFL 2,430 → 2,720 | KV | C | 03-003 pp. 13-14; 04-009 pp. 15, 18, 19; 02-002 p. 41 (405 + 2,315 = 2,720, no remark); 15-079 l. 1693-1696; 15-077 l. 53-54; 13-051 l. 3350-3352 | — |
| 2 | §3.1 Class: UPS 450285371 BOL 100, 9.70 pcf, billed 150 | KV | C | 04-009 p. 89 (class 100, NMFC blank, 650); p. 91 (53.08, 515, 9.70, "NOI 4 BUT LESS THAN 10 PCF"); p. 85 (018260-02, 150, 515, INSPECTION 18.00, REWEIGH FEE 18.00) | — |
| 3 | §3.1 Payer: Winn-Dixie; UPS DR bill-to; +ADD two Holland BOLs | KV (+ADD) | N | Winn-Dixie and UPS parts ✓ (21-002 pp. 6, 17; 04-009 pp. 15-16). The ADD's two BOLs (21-006 p. 19 PipingRock "Bill Collect to" the consignee; p. 20 Sunteck "Third Party ☑") are one load, PRO 670-438395-X (same date 9/8/2022, 2 units, 1,135 lb, NMFC 157320-05 class 125, booking N1883348HKG). Holland's bill for that load is **p. 18** ("670-438395-X … CHARGES: COLLECT", l. 398-402), not p. 12 (PRO 609-194236-2, Pure Fishing) | "… Holland billed collect (21-006 p. 18)" |
| 4 | §3.1 Ship date: TForce 12/20 vs 12/13 | KV | C | 21-015 p. 34 "DATE SHIPPED 12/13/22 … BILLING DATE 12/13/22"; p. 35 "PICK UP DATE 12/20/22"; p. 37 weighed 12/20/2022. Same kind of gap: 04-009 p. 18 BOL "July 30, 2008" vs pickup 07/31/08 | — |
| 5 | §3.1 Delivery date: ODFL 210 017 vs 214 D1 | KV | C | 19-001 ST1 `B3-09 20120927`, `B3-10 017`; 19-017 ST4 `AT7*D1*NS***20120927*1107*CT` | — |
| 6 | §3.1 Services: XPO 326-343835 APT; SEFL 890-100 | KV | C | 03-003 p. 21, p. 22 "11A … APPT 21st", p. 19 "APT APPOINTMENT $51.90"; 13-065 l. 4576 | — |
| 7 | §3.1 Pieces | N | C | 03-003 p. 17 seven order lines 1+1+1+1+3+1+1 = 9; p. 15 "9" PCS | — |
| 8 | §3.2 F18 bullet | KV | C (scope note) | 02-002 pp. 48, 35, 67; 21-015 l. 715. "Other carriers" rests on more than TForce: UPS Freight bills print "004500 REDELIVERY CHARGE 45.00" and "006900 REDELIVERY CHARGE 69.00" with no date in the OCR (`ocr_all` l. 2907 stamp 145, l. 14483 stamp 345) | — |
| 9 | §3.2 F17 bullet | N | C | as §2.1 F17 | — |
| 10 | §3.3 F19 bullet | KV | C | 02-002 pp. 46, 60; 03-003 p. 14; 13-065 l. 2682-2686 | — |
| 11 | §3.3 device record | N | C | 21-015 p. 36 "an NTEP certified dimensioning device installed at our Detroit, MI facility", no ID; UPS and Holland certificates name no device | — |
| 12 | §3.3 delay fault: NS everywhere | N (37 of 38) | N | 19-017 ST 0017 `AT7*D1*BK`; 19-018 ST 000010003 `AT7***AB*NA` | "NS on 36 of 38 events; one late ODFL delivery carries BK and one WTVA appointment NA" |
| 13 | §3.3 F21 bullet | KV | C | §2.1 F21 Never | — |
| 14 | §3.4 Original weight 2,430 derived | KV | C | `python3`: 744.77 ÷ 0.097 ÷ 315.97 = 24.2999 cwt; 02-002 l. 10366 (p. 208) | — |
| 15 | §3.4 Deficit 1,000 − 833 = 167 | KV | C | 19-001 ST2 `L0****86*G`, `L0****747*G`, `L0****167*G` with `L1**36.2*PH*6045****DAA`, `L3*1000*G` | — |
| 16 | §4.1 shipper-owed row (incl. "FedEx 360 ¶6 not found") | KV | **O** (that clause) | 13-050/-051 l. 1014-1017. The rest holds: TForce 361-A ¶3 (l. 1423-1425); 15-079 l. 1695; 15-077 l. 54; SEFL 753 l. 2682-2686; SEFL 360-5 ¶6 l. 549; "(2sk)" handwritten on 03-003 p. 13; "UPS Freight resp. piece count: 4" on 06-016 p. 11 | strike "FedEx 360 ¶6 not found"; cite both |
| 17 | §4.1 carrier-owed row | KV | C | 13-051 l. 3346-3349; 15-078 l. 229-230; certificate absent in chains B, C, D add-on, E (and the A sibling) | — |
| 18 | §4.1 nobody row | KV | C | §2.3 F19 | — |
| 19 | §4.1 customer row | KV | C | no shipper-issued rate con held; 22-012 is broker-to-carrier | — |
| 20 | §4.6 F06/F07/F09 row | KV | C | rows 1, 16 | — |
| 21 | §4.6 F12/F13 row (+ADD APIs) | KV (+ADD) | C | 17-095 l. 143, 158; 17-096 l. 843, 851 | — |
| 22 | §4.6 F14/F17 row: "TL dispute windows of 5-30 days" | N | N | The validator's held windows reproduce (22-012 l. 475-480, l. 533; 10-042 l. 8, 102; 10-046 p. 5; 22-012 l. 537-540 45 days) but it missed three: TQL **5 business days** for detention/layover and lumper receipts (10-037 p. 14, l. 749-750, 756-758; "Carrier waives the right … after 5 business days"); KCH notice within **2 hours** after the appointment (10-043 l. 55); Coyote receipts within **48 hours** (10-038 l. 881) and lumper receipts within 24 (l. 1105) | "accessorial notice and receipt windows of 2 hours to 5 business days, and invoice windows of 45 days, in the confirmations held; '5-30 days' is supported only at its low end (TQL)" |
| 23 | §4.6 F19 row | KV | C | [our call]; evidence list ✓ | — |
| 24 | §5.1 A: F01-F05, F07, F09, F10 from p. 46 | KV | **N** | p. 46 values all ✓ (B/L 51124115, 05/15/2023, Miami Gardens FL → Sisters OR, PREPAID, "1 PLT APPAREL IT-49880 / STC 16 BX", "*LIFTGATE DELIVERY", "QUOTE #CWEN3E465"). But "CLASS 70.0" is the rated FAK class, not an echo of the BOL (doc §2.2 F07 Never; walk A: "actual declared class NOT REPORTED"); p. 46 echoes no declared class, unlike the sibling p. 41 ("CL150", "CL125") | move F07 to the NOT REPORTED list for chain A: "F07: the declared class is not echoed; 'CLASS 70.0' is the rated FAK class (M19)" |
| 25 | §5.1 A: F06 509 lb | KV | C | p. 46 WEIGHT 509, no remark | — |
| 26 | §5.1 A: F19 | KV | C | p. 46; p. 33 (l. 1945) | — |
| 27 | §5.2 B: F01 | KV | C | 03-003 p. 13 blank B/L field; sticker 405-677016 | — |
| 28 | §5.2 B: F02 | KV | C | p. 13; p. 14; pp. 11-12 | — |
| 29 | §5.2 B: F03-F05 | KV | C | p. 13 | — |
| 30 | §5.2 B: F06 | KV | C | p. 13 | — |
| 31 | §5.2 B: F07 | KV | C (page) | The carrier's "PLT MISC 0-0 CLASS 100" is on p. 11 (invoice page 1) and p. 14 (DR); p. 12 (invoice page 2) shows only LP6 and the total | cite p. 11, not p. 12 |
| 32 | §5.2 B: F09 | KV | C | p. 13 | — |
| 33 | §5.2 B: F12 | KV | C | p. 12 remark; p. 14 "660", "CBR REWEIGH OF SHIPMENT FEE" | — |
| 34 | §5.2 B: F14 | KV | C | p. 14 (consignee "2 25 /21", driver "3/2/21"; TIME blank) | — |
| 35 | §5.2 B: F15/F16 | KV | C | p. 14 | — |
| 36 | §5.2 B sibling 326-343835 | KV | C (one uncertainty dropped) | pp. 19-22; arithmetic re-done: 14.25 × 131.87 = 1,879.15; 469.79 = 25.0%; 433.38 = 30.75% of 1,409.36; total 2,079.09 with LP1-LP5. Walk A read the handwritten weight as "1,210.00 (… could be read 1,200.00)"; the doc and the validator print 1,210.00 without the caveat; my render reading agrees with 1,210.00 but it is handwriting | — |
| 37 | §5.3 C: F01 | KV | C | 19-001 ST1 B3-03, N9*PO; 19-017 ST1-4 B10-02, L11*PO | — |
| 38 | §5.3 C: F02 | KV | C | B3-12, G62*86, ST2 AF 1640 CT | — |
| 39 | §5.3 C: F03/F05 | KV | C | N1 SH/CN; `L0****650*G***1*PCS`; AT8-04 `1` | — |
| 40 | §5.3 C: F06/F12 | KV | C | ST1 `AT8*G*L*606*1`; ST2-4 `650`; L0-04 650 | — |
| 41 | §5.3 C: F07-F09 NOT REPORTED | KV | C | 0 L5 in 34 ODFL 210s; AACT 19-009 `L5*1*BOOKS, NOI NMFC 161630` | — |
| 42 | §5.3 C: F14 | KV | C | as row 5 | — |
| 43 | §5.3 C: F17 | KV | C | ST1-4 | — |
| 44 | §5.4 D: F01 | KV | C (location) | 21-002 p. 6; p. 17 "NS", "LOAD#: NS". The handwritten "2904896" is in the carrier's PRO-label box at top right (the row headed DEST / SHIP # / CUBE %), not "by the shipper block"; p. 17 prints it as "SHIPPER # 2904896" | — |
| 45 | §5.4 D: F02/F03 | KV | C | p. 6 "12/3/2004", "32254"; p. 17 "PRO DATE 12/03/04", "32205" | — |
| 46 | §5.4 D: F04 | KV | C | p. 6 | — |
| 47 | §5.4 D: F05/F06 | KV | C | p. 6; p. 17 2472 | — |
| 48 | §5.4 D: F07 | KV | C | p. 6 "156600-3", 250, "Over 15 Dens."; p. 17 "PLASTIC ARTICLES NMFC #156600 S7 92.5 / OVER 15 DENS", class 085 | — |
| 49 | §5.4 D: F08 | KV | C | p. 17; 4 × 44 × 42 × 51 / 1728 = 218.17; 2,472 ÷ 218.17 = 11.33 | — |
| 50 | §5.4 D: F13 | KV | C | p. 17 remark block | — |
| 51 | §5.4 Paper-Pak | KV | C | 21-001 pp. 13-14; 32.15 × 58.47 = 1,879.81; × 0.7 = 1,315.87; 126.89 ÷ 563.94 = 22.5%; 563.94 + 126.89 + 7.50 = 698.33; at 2,601 lb, rounding each line: 26.01 × 58.47 = 1,520.80; × 0.3 = 456.24; fuel 22.5% = 102.65; + 7.50 = 566.39; 698.33 − 566.39 = 131.94 (the doc's figures reproduce) | — |
| 52 | §5.5 E: F01 | KV | C | 23-004 p. 5 "GTZ BOL NO : 27205339", "PU# KKFA0871883"; p. 8 "GBL NO: KKFA0871883"; 23-003 l. 195 "26665544"; 23-006 p. 4 PROs only | — |
| 53 | §5.5 E: F02 | KV | C | 23-006 p. 4 both rows 09/20/2022; 23-004 p. 5 07/03/2023; 23-003 l. 199 04/03/2023 | — |
| 54 | §5.5 E: F03/F04 | KV | C | 23-004 p. 5, p. 8 "Autryville, NC" | — |
| 55 | §5.5 E: F05 | KV | C | 23-004 p. 5 "0 / 2"; 23-003 l. 238 "0 1" | — |
| 56 | §5.5 E: F06/F08 | KV | C | 23-004 p. 8: crates 84×45×87, 190.31 each, total 380.63, tare 318 + 318 = 636, gross 1,422 + 731 = 2,153, net 1,104 + 413 = 1,517, "Density: 3.99"; 2 × 84 × 45 × 87 / 1728 = 380.625; 1,517 ÷ 380.63 = 3.99; 2,153 ÷ 380.63 = 5.66; 87 / 84 = +3.6% | — |
| 57 | §5.5 E: F07 | KV | C | 23-004 p. 5; 23-003 l. 238 | — |
| 58 | §5.5 E: F12 | KV | C | 23-004 l. 198-202 | — |
| 59 | §5.5 E: F15/F19 "carrier (quoted)" | N | C | 23-003 p. 5 (last page of the packet) holds the claimant's sentence "Per the message forwarded below, it was declined …" and a satellite image; no forwarded message appears. The "(quoted)" came from walk C's own F19 row (its F15 row says "claimant's word") | — |
| 60 | §5.6 F: F01 | KV | C | 22-012 p. 5; l. 438; l. 488; l. 221 | — |
| 61 | §5.6 F: F02/F14 | KV | C | p. 5; l. 219-221 | — |
| 62 | §5.6 F: F03 | KV | C | p. 5; l. 205; l. 493, 503 | — |
| 63 | §5.6 F: F04 | KV | C (unresolved mark) | p. 5 third-party block ✓; l. 212 "Bill To: BEST DEDICATED SOLUTIONS" ✓. Walk C read "'3rd Party' circled by hand"; at 150 dpi (`renders/baadv2/tf5_crop.png`) the terms blanks are unfilled and a hand-drawn oval around the receiver's signature crosses the terms line; whether it marks "3rd Party" cannot be told | — |
| 64 | §5.6 F: F05/F06 | KV | C | p. 5; l. 513-515; l. 229; 42,653 + 1,469 = 44,122; − 43,529 = 593 | — |
| 65 | §5.6 F: F07/M07 | KV | C | p. 5 hatched; l. 219-221 "Van" | — |
| 66 | §5.6 F: F09/F11 | KV | C | l. 498-509; seal and food-grade rules l. 441-483 | — |
| 67 | §5.6 F: F16 | KV | C | p. 5 both boxes "By Shipper" ticked; signatures and dates | — |
| 68 | §5.6 F: F17 | KV | C | p. 5; the handwritten notes also carry the driver's name and truck and seal numbers (not only trailer, PRO and date), but no times | — |
| 69 | §5.6 F: F20 | KV | C | l. 431, 440; p. 7; l. 235 | — |
| 70 | §5.6 F: F21 | KV | C | p. 8 l. 519 "Net Freight Charges USD 1,150.00"; invoice p. 4 | — |
| 71 | §8 row 9 | KV (upgrade) | C | 03-003 pp. 13-14 | — |
| 72 | §8 row 10 | KV (upgrade) | C | 03-003 pp. 19-22 | — |
| 73 | §8 row 12 | KV | C | 19-001 ST1 B3 string; 19-017 ST1-4 | — |
| 74 | §8 row 15 (BOL part) | KV (upgrade) | C | 21-002 p. 6 | — |
| 75 | §8 row 21 | KV (upgrade) | C | 23-004 l. 73 "382.08", l. 86 "ADR Claim-Alternative Dispute Resolution"; pp. 5, 8 | — |
| 76 | §8 row 24 (BOL and rate-con part) | KV (upgrade) | C | 22-012 pp. 4-8, 20; l. 479 "within 48 hours", l. 533 "within 24 hours"; p. 20 load 749936 dated 05/16/2023 | — |
| 77 | §8 row 19 (bonus) | KV (pp. 13-14) | C | 21-001 pp. 13-14; p. 7 statement not re-opened by either of us | — |

### §2.5 The validator's additions (validator §5; 9 rows)

| # | Addition | Mine | Evidence | Corrected wording |
|---|---|---|---|---|
| 1 | F17 fallback: pickup times on UPS Freight's PRO label; TForce DR boxes; Yellow prompts | C | 04-008 p. 7 "286 / 618 / 634"; 04-009 p. 18 "688 / 1636 / 1714"; 21-015 p. 35; 05-015 p. 7 | — |
| 2 | F17 primary: Skyway, Yellow Logistics, U.S. Xpress, LEI, Scotlynn records | C | 10-044 p. 16; 10-046 p. 5 ($35/hour after two free hours, six-hour cap, $250 layover, facility-noted times within 24 hours); 10-039 p. 11; 22-003 p. 12; 10-040 p. 1 "DETENTION WILL START 4 HOURS AFTER APPOINTMENT TIME AT $20/HR OR UNTIL LAYOVER OR $160 IS HIT" | — |
| 3 | F14 fallback: a consignee's dated receiving stamp (05-015 p. 7) | N | The "JAN 05 '09 10:46" stamp is unlabelled; the DR's own delivery PCS/DATE/TIME box carries a second date stamp, partly legible ("JAN 0? 200?"), so neither the owner of the 10:46 stamp nor its meaning (arrival, receipt, review) is printed (`renders/baadv2/y7_crop.png`, `y7_crop3.png`) | "…; a date-time stamp on the DR (Yellow 05-015 p. 7; unlabelled, so whose and of what is for the reviewer)" |
| 4 | F14 fallback: Autumn and Werner Enterprises invoices | C (extend) | 22-006 l. 199; 22-008 p. 7; add Landstar Global Logistics "DELIVERED 11/26/18" etc. (24-004 pp. 4-7) | add Landstar Global Logistics |
| 5 | F12 If none: document APIs by name | C (extend) | 17-095 l. 143, 158; 17-096 l. 843, 851. The same ODFL list also names "Delivery Receipt", "Delivery Photo", "Delivery Appointment Document", "Detention Certificate", "Lumper Certificate", "Weight Verification", "Freight Bill Correction" (l. 137-159), and TForce's "CUSX Customer Exception Sheet" (l. 852) | carry the API names into F14, F15, F17 and F22 If none as well |
| 6 | F22 primary: "every broker confirmation read requires a signed or valid unloading receipt" | N | Holds for TQL (10-037 p. 12 "None w/ valid unloading receipt"; p. 14 "Valid lumper receipts are required"), U.S. Xpress (10-039 p. 11), KCH (10-043 l. 51), C.H. Robinson (10-036 l. 134; 10-035 l. 159), BDS (22-013 l. 294-295), Yellow Logistics (10-046 p. 6). Not for Skyway, whose terms make lumper and other accessorial charges payable only "with its prior written approval" (10-044 l. 389-391), or King of Freight, whose confirmation is silent on lumpers (10-042, 0 hits); Scotlynn and Landstar Ranger not read for it | "The receipt (seven of the broker confirmations read require a signed or valid receipt; Skyway requires prior written approval instead)" |
| 7 | §3.1 Payer, second "Seen": two BOLs for one Holland load; "Holland billed collect (p. 12)" | N | Two BOLs for one load ✓ (21-006 pp. 19, 20, PRO 670-438395-X); the bill is p. 18 (l. 398-402 "CHARGES: COLLECT"), not p. 12 | "(21-006 p. 19 vs p. 20; Holland billed collect, p. 18)" |
| 8 | §2.5 join trap: the BOL's carrier box holds the first broker | C (extend) | 10-046 p. 8 "CARRIER CHRobinson" vs p. 4 Yellow Logistics → RMW Expeditors ✓. A second case: chain F's BOL names "Carrier Name: BEST DEDIC" (the broker) while Taylor hauled (22-012 p. 5; p. 6 l. 431) | add the chain F example |
| 9 | Missing fact F17a, drop-trailer and hook times (for BC) | C (evidence) | 04-008 p. 7; 10-046 p. 4 "Drop trailer 7/27 from 1200-1300, pick up trailer on 7/28 at 1300"; 05-015 p. 1 "DROP TRAILER APP 12/30 0500-13…" | whether it earns an ID is BC's question |

## §3 Counter-examples found for generalisations

Each line: the generalisation, the file and value that breaks or bounds it.

1. **"FedEx 360 ¶6 not found" (validator §2 F04, §4.2 row 16).** Found: 13-050 and 13-051 l. 1014-1017, with a Canada-origin exception the doc does not carry.
2. **"QN# not found in the XPO text layers held" (validator §2 F10).** 21-005, 7 lines, 4 shipments (§2.1).
3. **"NS in every real 214" / "NS on 37 of 38".** 19-018 ST 000010003 `AT7***AB*NA*20121109*1000*LT` (and BK on 19-017 ST 0017).
4. **"UPS Freight prints a number on 17 of 24, NONE on 7".** 16 NONE of 42 read; 04-006 p. 53 and nine rendered `ocr_all` bills (§2.1 F01 If none).
5. **"The DR prints the reweighed weight (XPO, UPS 241325140)".** 04-008 p. 6 prints the declared 557 and the actual 655.
6. **"606 on the earliest message, before 650".** 19-017 is one interchange of 18 messages sent 2012-10-15 11:44; no message is dated.
7. **"The TL 210s put the load number in B3-03".** 0 of 34 TL B3-03 values equal any N9 value in the bill; nothing labels it.
8. **The piped Werner reference as a rate-con field.** It is the invoice's "Customer Ref #" with the B/L column blank (22-013 p. 4); the rate con splits it (p. 5).
9. **"FedEx 980 ¶2 promises a copy; others for a fee in custody".** ABF 993 sells a certified weight receipt to a consignee at delivery for $55 (13-048 l. 5643-5648); Estes 105 Item 281 ¶3 sells a scale ticket for $15.65 on convention-center deliveries (13-049 l. 555-556). Neither is a copy of a reweigh record, so "FedEx 980 ¶2 is the only copy promise" survives across set 13 (searched for "certificate", "scale ticket", "weight receipt", "copy of", "verification record").
10. **"No real 210 carries K1; NMFC in L5-03 on 1 of 82".** True of the 82 real transactions. The catalogue's "partly real" RDWY 210 to CTSI (19-031) carries `K1*1*REMARKS` (placeholder text) and L5-03 on both its bills (`10450000`, `99999812`); a parser test set built from set 19 should exclude or flag it.
11. **"F18: other carriers do not print the attempt date; TForce only".** UPS Freight bills print REDELIVERY CHARGE lines with no date in the OCR (`ocr_all` stamps 145 and 345); UPS's reconsignment BOL has a "DELIVERY ATTEMPTED? YES/NO" box (04-009 p. 67). No ABF, XPO or ODFL redelivery line turns up in the text layers of sets 01, 03 and 21 (scanned pages without text not covered).
12. **"No first-attempt record is held" (F18 Primary).** Bounded: the UPS reconsignment BOL (04-009 p. 67) records whether delivery was attempted and dates the reconsignment authorization; it is not a first-attempt DR.
13. **"No lumper receipt, cancellation record or layover record is held" (F22 Primary).** A broker's TONU confirmation is held (22-013 pp. 24-25, $150, no time); a TONU dispute letter (23-002 l. 202-206); a TONU invoice line (22-019, per catalogue).
14. **"Every broker confirmation read requires a receipt" (ADD #6).** Skyway (10-044 l. 389-391), King of Freight (10-042).
15. **"Not reported in any public file" (F17 If none) and the If-none parties for F14-F17, F22.** ODFL's document API names "Detention Certificate", "Delivery Appointment Document", "Delivery Receipt", "Delivery Photo", "Lumper Certificate" (17-095 l. 137-159). Whether any is filled for a given shipment is not testable offline.
16. **TL accessorial windows "24 hours to 3 business days" (validator §4.2 row 22).** TQL 5 business days (10-037 p. 14); KCH 2 hours (10-043 l. 55); Coyote 48 hours and 24 hours (10-038 l. 881, 1105).
17. **"Every Holland example is the Pure Fishing load".** 21-006 holds two Holland loads: 609-194236-2 (pp. 12-15) and 670-438395-X (pp. 18-21).
18. **"04-011 has no OCR".** It is inside `ocr_all.txt` (Doc 20041 headers, l. 9715-13348).
19. **Generalisations confirmed on the full set** (no counter-example found): N9*PO on 82/82; N1 SH and CN on 82/82; B3-04 on 82/82; B3-12 blank on all 34 TL 210s; X1 never with D1 on one key; no certificate names a device ID; no DR service box ticked in any DR viewed (sets 03, 05, 21, and 21-012); no shipper-issued rate confirmation; 23 of 101 ABF bills share amount and ship date.

## §4 §5 versus the raw traces (F rows only)

Sources: walk A (`SCRATCH/walks_raw/walk_A_sets02_03.md`, chains A and B), walk B and walk C (decoded to `SCRATCH/baadv_walk_B_sets19_21_decoded.md` and `SCRATCH/baadv_walk_C_sets23_22_decoded.md`), against `git show HEAD:data/doc-exploration.md` §5.1-§5.6. Companies only. "Caught" = whether the validator's report notices the difference.

| Chain, fact | Walk (raw) | Doc §5 | Caught? | Assessment |
|---|---|---|---|---|
| A, F07 | "APPAREL IT-49880 … CLASS 70.0 \| NMFC 49880, rated 70 (FAK) \| fallback (bill echo); **actual declared class NOT REPORTED**" | F07 folded into "F01-F05, F07, F09, F10 … 'APPAREL IT-49880' rated 'CLASS 70.0' … **all from the bill's echo of the BOL**" | No (KV) | A NOT REPORTED turned into a value. 70.0 is the FAK rated class (doc §2.2 F07 Never); p. 46 echoes no declared class. §2.4 row 24 |
| A, F01 | "SHIPPER B/L NO. 51124115"; "SO# 143695 / PL# 224629" | "B/L 51124115" | No | SO and PL# (shipper order and packing-list numbers, F01's "shipper number") dropped; minor |
| A, F08, F11, F14-F17 | NOT REPORTED, with the pages looked at (p. 46, p. 33) | "NOT REPORTED in this chain: F08, F11, F14-F17" | — | same |
| A, F09 | "fills liftgate only; no residential/notify instruction echoed" | "*LIFTGATE DELIVERY" | — | same in substance |
| B, F02 | "invoice **p.11** SHIPMENT DATE 02/12/2021" | "invoice 'SHIPMENT DATE 02/12/2021'" | — | the validator cites p. 12, which also prints it; both right |
| B, F07 | "bill echo 'PLT MISC 0-0 CLASS 100' (**p.11**)" | "invoice 'PLT MISC 0-0 CLASS 100'" | No | the validator cites p. 12, which does not print the line (§2.4 row 31) |
| B, F17 | "DR p.14 TIME box blank \| NOT REPORTED" | in the NOT REPORTED list | — | same |
| B sibling, F06 | "handwritten WEIGHT '1,210.00' (read at 200 dpi; **could be read 1,200.00**)" | "weight '1,210.00'" | No | uncertainty dropped; "(digits uncertain)" kept for the NMFC only. My render agrees with 1,210.00 |
| B, F14 | consignee line "2/25/21", driver line "3/2/21", "delivered about 02/25/2021 … ambiguous" | same | — | same; render confirms both dates |
| C, F06/F12 | "606 (AG message) vs 650 (AF/AB/D1) … which is declared is not provable" | "606 lb on the estimate message, 650 at pickup and after; **no document says which is declared**" | — | same; neither claims a time order. The validator's §2 wording ("earliest … before") adds one (§2.1 F06 Fallback) |
| C, F15/F16 | "NR; AT7-02 'NS' = normal status; no signer" | in the NOT REPORTED list | — | same |
| C, F04 | "PP; bill-to Dalmation Press LLC; not in 214" | P01/M06 row | — | same |
| D, F01 | "shipper's account number handwritten on the BOL **and printed as SHIPPER # 2904896**" | "shipper's account number handwritten on the BOL (2904896)" | Partly (the validator places it "by the shipper block", which the render does not show) | the number sits in the carrier's PRO-label box; p. 17 prints it under "SHIPPER #" (§2.4 row 44) |
| D, F09 | "WD p.6 \| **none ticked**" | in the NOT REPORTED list (F09-F12) | No | the doc is the better reading: the 2004 ODFL form has no service boxes, so "nothing requested" cannot be read off it; the walk's "none ticked" overstates |
| D, F19 | "warehouse consignee ('GM Whse.') \| No residential question" | absent from both the table and the NOT REPORTED list | No | a dropped row; harmless (no residential charge) |
| D, F07 | "Re-bill: class 085, description 'NMFC #156600 S7 92.5' (**as I read the fax**)" | "the re-bill rates 085"; M18/M19 row quotes "S7 92.5" without the caveat | No | the render (p. 17) reads "S7 92.5"; caveat not needed |
| E, F09 | "G2 'Pickup Remarks: … Must check in at window. Delivery Remarks: Closed 12:00 - 1:00 for lunch.'; G1 comments blank \| Primary; no limited-access or residential box on either BOL" | **absent** (neither a row nor in the NOT REPORTED list) | No | a dropped row that matters a little: G2's dispute is a limited-access charge, and its BOL's remarks are the only F09 evidence |
| E, F06/F08 (G2) | "G2 '492 lbs'"; "G2 '37 In 90 In 56 In', no cube … derived 107.92 ft³, 4.56 lb/ft³" | G1 only | No | G2 values dropped; minor |
| E, F08 cube | "2 × 84×45×87/1728 = 380.62 ft³; on BOL dims 394.22 ft³ … 5.66 (5.46 on BOL dims)" | "380.63 total" and "1,517 ÷ 380.62 = 3.99" in one cell | No | 380.625 rounds to 380.63 (the certificate's print); the doc uses both; the BOL-dims figures (394.22 ft³, 5.46 pcf) were dropped |
| E, F15/F19 | F15: "G2 p.5 (**claimant's word**)"; F19: "carrier (**quoted**): 'listed as a Self-Storage Warehouse'" | "carrier (quoted)" | Yes (validator NARROW) | the walk contradicted itself; the doc took the F19 wording; the page holds only the claimant's sentence |
| E, F16 | "NOT REPORTED \| BOL signature lines blank as printed" | in the NOT REPORTED list | — | same |
| F, F04 | "BOL 'THIRD PARTY … C/O Cass' … **'3rd Party' circled by hand**" | third-party bill-to only | No (the validator says "terms boxes themselves blank") | unresolved: at 150 dpi an oval around the receiver's signature crosses the terms line; no mark sits in the blanks (§2.4 row 63) |
| F, F09 | "rate con 'Appointment Required: Yes', seal/BOL/food-grade rules, 'Freeze protection required below 32°F'; BOL '**Master Bill of Lading** … ticked'" | F09/F11 row without the Master-BOL tick | No | minor; the render shows a tick in the Master BOL box |
| F, F05/F06 | three counts: 20 HU; 1,886 vs 1,892 packages; HU "0" | same | — | same; arithmetic re-done |
| F, F14 | "invoice DATE DELIVERED 02/24/2026; BOL receiver's handwritten date '02/24/26' and driver's note '2/24/26'; time NOT REPORTED" | same | — | same |
| F, F21, F22 | F21 NOT REPORTED "structurally"; F22 "n/a" | same | — | same |
| F, P15 (bears on F17) | "the brief's own misplacement of the in/out-times rule (p.20, a 2023 load, not pp.6-8)" | §5.6 heading paragraph says so | Yes | consistent |

**The three checks the assignment named.**
- **Chain B's handwritten delivery dates:** 03-003 p. 14 (render): consignee DATE field "2 25 /21", driver line "3/2/21", TIME blank. Doc, walk and validator agree.
- **Chain E's certificate arithmetic:** 84 × 45 × 87 / 1728 = 190.3125 per crate; × 2 = 380.625 (printed 380.63); net 1,104 + 413 = 1,517; gross 1,422 + 731 = 2,153; tare 318 + 318 = 636; 1,517 ÷ 380.63 = 3.985 → 3.99 printed; 2,153 ÷ 380.63 = 5.656 → 5.66; 87 ÷ 84 = 1.0357 (+3.6%). All reproduce (23-004 p. 8 render).
- **Chain F's three weights:** BOL 42,653 + 1,469 = 44,122 lb (22-012 p. 5); rate con 43,529 lb (l. 515); invoice 43,529 (l. 229); 44,122 − 43,529 = 593. All reproduce.

## §5 New-fact tests

Not applicable (BC only). The validator's one proposed new fact (F17a, drop-trailer and hook times) is recorded with its evidence in §2.5 row 9 for validator BC's reviewer.

## §6 Privacy check

Scanned `research/s5_check_BA_c09_fact_map_shipment_facts.md` (308 lines) with `grep -E` for phone patterns (`[0-9]{3}[-.) ][0-9]{3}[-.][0-9]{4}`, `\(?[0-9]{3}\)?[ -][0-9]{3}-[0-9]{4}`), honorifics (`\b(Mr|Ms|Mrs|Dr)\.? [A-Z]`), e-mail addresses, the labels "ATTN", "attention", "signed by", "weigh master", "inspector", "driver info", "contact:", and a list of 50 given names and surnames read on the rendered pages behind its citations (drivers, dispatchers, inspectors, a weigh master, consignee and shipper contacts, broker staff, a carrier employee named in a claim letter, an auditor, signers). **No hit.** Every capitalised two-word sequence in the report was listed and checked: all are companies, places or form labels (e.g. "Floyd Inc", "Pink Cheetah", "Silver Arrow", "Cornelius Leasing" are carrier names). The report says "no individual's name … transcribed" and that holds. The same scan was run on this report before handing it back.

## §7 Concerns left unproven

**The validator's own §7, item by item.**
1. "5-30 days" for broker windows: now partly settled offline. TQL's 5 business days (10-037 p. 14) is the only held window inside 5-30; nothing held reaches 30. The upper end still rests on AM's web reading.
2. SEFL 647 Note A as the carrier's record of a phoned request: the rule is in the held text (13-065 l. 1364-1372); no carrier record of such a request is held.
3. XPO "QN#": settled (21-005, §2.1 F10).
4. "23 of 101" ABF duplicates: settled (re-run, 9 groups).
5. Set 04 certificate count: the OCR covers all nine bill files (04-011 included), but the counts are keyword lines, not pages viewed; the AW review's 43/6 page count was not repeated.
6. Which ODFL 214 weight is declared: still open, and so is which message came first (one interchange, no message times). Would settle it: ODFL's BOL or its "Weight Certificate" for PRO 00902527924.
7. A 214 failed-attempt status: none in the 8 real files; the X12 code list was not consulted (offline). A UPS reconsignment BOL with a "Delivery attempted?" box is held (04-009 p. 67).
8. Werner Enterprises invoices printing miles and a delivery date: I also saw only 22-008 p. 7. Would settle it: render the other invoice pages of 22-008.
9. 10-045's confirmations and 22-005, 22-009, 22-010: not re-read by me either.
10. UPS 406858966 density consequence: the certificate's own comment "SPMT SHOULD BE RATED 41330-2, CL 85" (04-009 p. 19) and the bill's class 85 (p. 15) agree; whether 20.08 vs 23.54 pcf would change a density-rated item was not checked.
11. Yellow's 2008 WAIT TIME boxes: not checked beyond pp. 1 and 7 (both blank); the 40-dpi contact sheet in `SCRATCH/renders/` is too small to read.

**Mine.**
12. The 05-015 p. 7 stamps: who applied "JAN 05 '09 10:46", and what the partly legible stamp in the DR's delivery DATE box reads. Would settle it: a higher-resolution source scan; the PDF itself is the limit.
13. Chain F's freight-terms marks (22-012 p. 5): whether the hand-drawn oval was meant to mark "3rd Party" (walk C) or only to circle the receiver's signature. Not decidable from the image.
14. The meaning of B3-03 on the TL 210s (19-033 to 19-035): the shipper's load number, a BOL number or a TMS shipment ID. Would settle it: the matching invoice PDFs the source repository is said to hold (catalogue note on 19-033), not in `data/`.
15. The 214 reason code "NA" (19-018) and "BK" (19-017): their meanings are from memory of the X12 code list, not checked offline; the counts do not depend on them.
16. ODFL's document API types ("Detention Certificate", "Lumper Certificate", "Delivery Appointment Document"): the guide lists them; whether ODFL fills them for an ordinary shipment, and whether any other carrier offers the same, is untestable offline.
17. UPS Freight REDELIVERY CHARGE lines (`ocr_all` stamps 145, 345) and the "DELIVERY ATTEMPTED" remark (stamp 330): read from OCR only; not rendered, so a date beside them could have been missed.
18. The 21-012 New Penn DRs and the 24-004 Landstar packet were opened only for their first pages (21-012 pp. 6-9; 24-004 pp. 4-9); their other pages may hold the times, receipts or attempt records that F14-F18 and F22 lack.
19. The validator's §6 inconsistencies were not each re-tested; items 2, 5, 7 and 8 are affected by the findings above (7 is withdrawn by finding 1; 8 changes to 16 of 42).
