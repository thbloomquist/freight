# Check BE: adversarial verification (V1)

Verifier V1, 2026-10-21, on the 382 rows check BE added to `data/catalogue.csv` and the 30 case cards in `data/answer_keys/`. The repo was not edited by the verifier. Its per-row verdicts and corrections were applied by the coordinator the same day (§9). Scanned pages were read by OCR (repo tessdata) or as page images, spreadsheets from the derived CSVs and the originals, EDI segment by segment. No web access was used. No person's name appears in this file.

## 1. Summary counts

| Set | Rows | Verified | Narrowed | Wrong | Checked |
|---|---|---|---|---|---|
| K1 (09, 13-16, 19, 21, 23) | 53 | 15 | 38 | 0 | content |
| 25 (IDL) | 149 | 141 | 8 | 0 | identity (chain members: content) |
| 26 (decisions) | 171 | 105 | 66 | 0 | 30 card rows content; rest identity |
| 27 (AP ledgers) | 9 | 7 | 2 | 0 | content (patterns re-run) |
| Case cards | 30 | 11 | 19 | 0 | each decision read in full |

All 382 files:
- exist;
- match their sha256 and byte count;
- match their pdfinfo page count;
- appear in `SHA256SUMS`.

There are no duplicate file_ids.

Most K1 narrowings are vocabulary, not substance:
- Withdrawal forms, orders and preference complaints carry no instance of a check. The instance is on the held claim, so their `discrepancy_checks` should be blank.
- The EDI rows used `real (ISA15=P)`-style values; the field allows only real / template / mixed, so the ISA15 flag moves to `format_notes`.
- 30 of the 66 set-26 narrowings are CPUC `date_start` placeholders (`YYYY-01-01`), not dates of shipments or of the review period.

## 2. Corrections that change a number or a chain claim

| file_id | Claim as written | Correct reading (evidence) |
|---|---|---|
| 23-024 | ACCO: 41 transfers 5/18-7/27/2023, $42.78-$2,680.78 | 41 transfers 5/18-8/2/2023, **$7.99-$3,824.80**; the total $22,731.82 is right (Exh. A) |
| 23-014 / 23-015 / 23-021 | amounts not given | 16215 = $75.00; 16595 = $382.08; Home Depot 17958 vs YRC Inc. = $5,017,363.46, the other four = $16,496,493.54 each |
| 23-020 | an earlier *unconditional* withdrawal of *other* claims (Doc 1890) | not in the file. It is an *amended* notice, so an earlier notice exists, but its terms are unverified. The condition is confirmed: the Setoff Agreement under Docket 522 must stay in force |
| 21-018 | 21-015 closed as "allowed" | the file shows only the debtor split: $7,575.03 → $1,284.57 USF Holland + $6,290.46 YRC. "Allowed" is a register remark; the order's para. 5 says nothing in it admits validity |
| 21-019 | "Closes outcome of 21-002" | it closes only the **objection**, withdrawn without prejudice for claim 7664. The claim's final treatment is not shown. ODFL is not named in the order (carriers=) |
| 09-056 | checks include B8 | fuel appears only as $20.66, with no level or index: drop B8; date_start = 2018 (no day given) |
| 09-058 | B6 | B1: the clause makes the signed broker/carrier agreement prevail over the rate sheet; no linehaul comparison is made |
| 09-067 | settled after the verdict | settlement is inferred, not stated. The stamp reads Document 328 (stipulated motion, 2021-09-14), with the order signed 2021-09-15 |
| 14-077 | date_end blank | 2023-12-03: 128-BB takes effect 2023-12-04, so 128-AA governs 21-003 (June-July 2023) |
| 14-083 | "weekly-applied value for 21-006 to 2023-07-05" | the rates are as of **2023-07-12**, one week after the last 21-006 bill |
| 15-085 / 16-097 | dated 2023-08 / 2022-03 | those are capture dates; the PDFs were last modified 2021-08-25 (form OP-097EX3 01/09) and 2013-10-10. Drop G1 from 15-085: its nine-month limit is for cargo claims |
| 19-037 / 19-038 / 19-039 | D4/D7 only on 19-039; "adds UNL" | STO (stop-off) and UNL (unloading) lines already appear in 19-037 (STO on 3 of 7 invoices, UNL on 5 of 7) and in 19-038. 19-038 also has two invoices to one consignee with identical $2,490.75 totals but different shipment IDs: a near-duplicate (A2) test case. Accessorials carry the rate qualifier "PM" on flat amounts, a parser trap. All 26 RASY, ACDT and Conoco B3 totals equal the sum of their L1 lines |
| 19-043 / 19-046 / 19-048 | D4; D3 | the two S5 stops are origin and destination, not stop-offs; AT7 AA is a pickup appointment with no arrival or departure time. Drop D4 and D3 |
| 25-046 | DR + W&I certificate, C1/C2/B8 | a delivery receipt carrying an inspection stamp; no separate certificate and no correction fee. Weight 3,813 + scale differential 55 + **tare 272** = 4,140 lb. DR dated 2017-05-22, delivered 05-30 |
| 25-118 | QBR 2012-2013 | slide 1 is dated 2014-03-19 |
| 26-107 | 466096 BC Ltd. | **466095** BC Ltd. (para. 1) |
| 26-028 / 034 / 037 / 039 | "closing words" | each auto-extracted quote was footnote text; the true closing sentences are now in the rows |
| 26-080 | mode TL | a forwarder shipment from Indonesia, so mode = na |
| 26-132 | | the decision contradicts itself: the opinion says "15 instances", but the table has 24 rows with undercharges, dated from 6-21-60 against a stated review period of July-September 1960. The undercharges sum to $727.73, recomputed |
| 27-007 | 435 rows; 6 negatives all on payment 717965 | 433 data rows; the negatives are 3 on 717965 and 3 on 3299365 |
| 27-002 | 12 rows | 11 data rows |

## 3. Re-verifications

All confirmed except where noted.

- **Docs 3304 / 3303 / 3295** withdraw claims 16200 / 16215 / 16595, each dated 5/06/24 and filed 05/07/24.
- **Docs 4914 and 5185** only move Cass 19254 between debtors: Schedule 1, row 73, p. 15 (the page image is upside down; rotated and OCR'd): $283,387.35 → $12,924.56 Yellow Corporation + $270,462.79 YRC Inc. No ruling on validity. Order 5185 recites "Re: Docket No. 5164", not 4914; the relationship between the two dockets is unresolved.
- **TQL 18553**: the withdrawal is conditional, as stated.
- **Winn-Dixie Doc 7355** withdraws the objection to claim 7664 (OCR, p. 2).
- **Estes v. Coverlex Doc 33:** $1,829,154.14 = $335,575.69 + $1,493,578.45. The worked bill checks: $84 + $15.00 + $20.66 = $119.66 and $537.03 + $15 + $20.66 = $572.69.
- **ODFL 128-AA / BB / CC:** effective 2022-06-01, 2023-12-04 and 2025-04-09; each ends in `%%EOF` with a complete page count; none is truncated.
- **Kraft 204/214:** the 204 and the 214 share SI 20447663200101 (shipment 2044766320).
- **kraft4 redaction:** no e-mail or phone pattern is left; two `[REDACTED]` NTEs; SE count 38 = 38 segments; the hash matches the row.
- **Set 27 patterns:**

| Ledger | Pattern | Result |
|---|---|---|
| Richmond | invoice 428-113379 | holds. Plus: the utility lines net to zero; the $273.38 freight line was posted twice; the check's lines sum to its $2,845.74 total, so the doubles were paid |
| Los Angeles | 172392721 reversal | ±$127.06 on 2021-05-13, holds |
| Cook County | repeated invoices on the same check | 13 found, holds |
| Connecticut | duplicate line | SOSM100015312 ×2, holds |
| Dallas | reversal | ±$65.10 on 2015-10-22 / 2015-12-02, holds |

- **Set 25 chain numbers:** pycp0254: 4,901 bills, mode counts and audit-code counts. DCL 166836: $363,723.74 open invoice; $10,580 billing-error credit; $207 credit memo. DCL 166482: $6,450 credit. PAX–YRC: $2,950 vs $4,217.57 quotes; BOL weights 413 + 6,050 = 6,463; W&I 6,463 → 6,569 (+106), PRO 979-408870-0. Endo: Czar Lite 2000, FAK 50/70. Actavis: 54% off Czar Lite 95, $70 minimum. mkxw0443: 106 → 103 columns in the derived CSV (POD name and addresses dropped). All checked.

## 4. Case cards

Every decision was read in full, including the order. The four contradictions K3 reported, and the figure each order uses (the cards use the order figure in all four):

| Card | Figures in the decision | The order uses |
|---|---|---|
| CBCA 1637 | table and intro $12,216.83 (recomputed from 31 rows) vs Decision $12,093.71 | **$12,093.71** |
| CBCA 3467 | p. 5 $339,895.73 vs p. 6 $339,895.75 | **$339,895.75** |
| 2019 BCCRT 63 | invoices sum to $4,470 vs claimed $4,450 | **$4,450** |
| 2018 BCCRT 886 | computed $797.29 vs claimed $721.99 | **$721.99** |

Three more contradictions inside the decisions:
- CBCA 4071: invoice dated 2013-05-30 on p. 4 but "May 20, 2013" on p. 5; $10,185,586.04 invoiced vs $10,185,568.04 sought.
- CPUC D63338: "15 instances" vs 24 table rows.
- GSBCA 15194: the footnote's disputed amounts sum to $6,167.85, exactly the overcharge total, although the Board describes them as a smaller gap.

Card corrections:
- **Number corruption, GSBCA-14208:** F25 and M14 read ",845"; it should be **$1,845** (a shell `$1` expansion had dropped the digits).
- **The `result` field was used inconsistently**: "refund" sometimes meant the payer gets money back and sometimes that the carrier gets paid. Now **payable** for CRT-2019-1327, CRT-2019-44 and GSBCA-13948; **notices invalid** for CBCA-3467, where no refund was ordered; **undercharge (collect)** for CPUC D59496, D63749 and D66029 ("split" was unsupported there, because no allegation failed; it stays for D63338, where the rebate allegation failed).
- **Check tags the decision does not evidence:** A4 on CBCA-1637; E2 on CBCA-5663; C1 on CBCA-8051; F1 on D59496; A3 on D72074, CRT-2018-886, CRT-2019-1327 and CRT-2019-261; A4 on CRT-2018-886; F1 on CRT-2019-261.
- **Facts:** CBCA-5663 F18: no delivery attempt is recorded; the base was closed and could not be reached by phone. CBCA-6729: the ref is p. 2 (the PDF has 2 pages); the signature was requested on 2018-09-27 and obtained later. CBCA-3467: the repayment demand covered 70 of the 79 payments.
- **Mode:** GSBCA-14330's mode is assumed; the decision does not state it.
- **Privacy:** CRT-2018-886 quoted the decision's defined term for the customer, which para. 1 defines to include an individual; replaced with "[the customer]".

Verified with no change: CRT 2018-465, 2018-600, 2018-659; CRT 2019-101, 2019-572, 2019-63, 2019-659; CRT 2020-297; GSBCA 13733, 14110, 14376.

## 5. Privacy sweep

**(a) E-mail regex.** 0 hits in `derived/idl` (281 CSVs), `answer_keys`, the set-27 CSVs and the five unzipped `*__stripped.zip`.

**(b) Phones and street addresses.**
- Zips: one consumer street address with its ZIP was left in hlkx0332 (`DCL_-_B2C.csv`, City column). No phones.
- `derived/idl`: the same kind of address in `skbp0318__Freight_20200.csv`; a residential-looking mis-delivery address in a comment in `fgcm0347__Oct._2015-_RAW_DATA.csv`; named wholesaler staff with 8 direct phone numbers in `lmdg0349__Sheet1.csv` free text (the tool's PHONE pattern was defined but not applied to cells); First Name / Last Name / Position columns for about 35 client staff in `jlwc0253__Project_Team.csv`. Other hits are business addresses or toll-free numbers.
- Set 27: no phones or addresses; Richmond and Los Angeles redacted; Atlanta (27-007) `invoice_description` named 4 private individuals in 5 rows, not redacted.

**(c) Our own text** (case_or_docket, parties, notes, format_notes, the cards): no individual's name, cross-checked against the representatives, members, judges, signers and witnesses named in the decisions and K1 files. The BC CRT cards cite by neutral citation, apart from the defined term in §4.

**Beyond the scope set, but material.** The original of 25-115 (`skbp0318`, PAX freight and adjustments, March 2017) holds about 47,000 consumer recipient names with city, state, ZIP and tracking numbers (Company column of sheet "Freight 20200", about 880 more on "Freight 20201"): the same class of data for which the founders replaced five workbooks with stripped zips, but this one was not replaced. Separately, the held 19-027 (a Seaboard 204, outside BE) carries a person's name and phone in a G61 segment, the issue fixed in kraft4.

## 6. Coverage and chain closure

Real files added by BE per check, after corrections (K1 / 25 / 26 / 27). Set 25 and 26 tags were checked by sampling and keyword checks, not one by one.

| Check | Count | Check | Count | Check | Count |
|---|---|---|---|---|---|
| A1 | 6/30/12/0 | B4 | 0/6/14/0 | D4 | 3/0/12/0 |
| A2 | 2/22/0/4 | B5 | 7/10/3/0 | D5 | 0/2/1/0 |
| A3 | 0/0/3/1 | B6 | 4/0/2/0 | D6 | 0/0/2/0 |
| A4 | 2/5/16/3 | B7 | 0/1/12/0 | D7 | 3/0/0/0 |
| A5 | 0/0/5/0 | B8 | 6/37/1/0 | E1 | 0/8/3/0 |
| A6 | 8/5/2/0 | B9 | 1/1/0/0 | E2 | 0/7/3/0 |
| A7 | 7/17/4/0 | C1 | 0/4/9/0 | F1 | 4/7/4/2 |
| B1 | 1/13/29/0 | C2 | 0/1/0/0 | F2 | 0/12/0/8 |
| B2 | 1/38/61/0 | D1 | 4/42/37/0 | F3 | 0/31/0/0 |
| B3 | 1/10/12/0 | D2 | 0/11/44/0 | F4 | 0/4/0/0 |
| | | D3 | 0/2/10/0 | G1 | 5/5/20/0 |
| | | | | G2 | 0/2/6/0 |

| Held chain | Closed by | Status |
|---|---|---|
| 23-002 (16200) | 23-013 | outcome: withdrawn, no reason |
| 23-003 (16215) | 23-014 | outcome: withdrawn, no reason |
| 23-004 (16595) | 23-015 | outcome: withdrawn, no reason |
| 23-006 (nVision 11113) | 23-022 | partly: the approved draft is absent from the 11 cleared transfers; unpaid is assumed |
| 23-001 (Cass 19254) | 23-016/017/018 | debtor split only; allowance open |
| 21-002 (Winn-Dixie) | 21-019 (+ 21-020) | partly: objection withdrawn; the claim's final treatment unknown |
| 09-041 (Estes v. Coverlex) | 09-056, 09-057 (09-055 first step) | closed: judgment $1,829,154.14 stands |
| 09-033 / 09-048 (Central Freight v. Amazon) | 09-066, 09-067 | closed: verdict $2,472,227.10, then dismissal with prejudice (settlement inferred) |
| Transport Systems v. Amazon (10-039) | 09-058, 09-059 | closed, but not on billing (forum clause; standing) |
| 23-010 (TQL) | 23-020 | closed by a setoff agreement; terms not public |
| 23-009 (TForce Worldwide) | 23-019 | withdrawn |
| 23-005 (Home Depot) | 23-021 | withdrawn 2025-11-03 |
| 21-014 (Mode) | 21-016 | withdrawn 2024-03-26 |
| 21-015 (TForce Freight 10129) | 21-017/018 | debtor split; allowance only on the register |

**Is any chain complete (price terms + shipment facts + bill + dispute + outcome) for one instance? None, as held files.** The closest:
1. **F1/B3, Estes v. Coverlex.** All five parts are described for one worked bill inside 09-056 and 09-041, and the outcome is final; but the price documents (tariff 550-01, the pricing agreement, EXLA 105) are exhibits not on RECAP.
2. **JUUL–DCL invoice 166482:** price terms grxw0289 / rjdb0321 / ggbp0406; shipment and bill detail xqgg0299; outcome zghn0318, the $6,450 "Billing Errors" credit. Missing: the dispute record and which line was wrong, so the check is unknown.
3. **A5, Winn-Dixie (21-002 + 21-019):** lacks the carrier's price terms and the claim's final outcome.

## 7. Concerns left unproven

- **Register facts** ($0.00 balances, "THIS CLAIM IS WITHDRAWN", "ALLOWED", the other ten GlobalTranz withdrawals, Doc 1890) were not re-opened (no web access).
- **Set 26 non-card rows:** checked by script that the case number, date, closing quote and amounts appear in each file and that the outcome matches the last paragraph (89 GSBCA + 9 CBCA); 6 hand-read. Check tags were not checked one by one.
- **Set 25:** amounts and IDs in the notes were found by token match in text or derived CSVs; slide decks checked by file signature and first slide only.
- **Doc 5164 vs 4914:** which objection Order 5185 rests on is unresolved.
- **Person-name scans are heuristic.** The pharmaceutical consignee columns (TRN files, Hobart paylogs) are mostly businesses, but some rows may be individuals.

## 8. Claim ledger (selection)

| ID | Claim | Where | Verdict |
|---|---|---|---|
| 23-013/014/015 | withdraw 16200/16215/16595 | p. 1 each | verified |
| 23-018 | Cass row 73 split | p. 15, OCR rotated | verified |
| 23-020 | conditional withdrawal | p. 2 | verified |
| 23-022 | 11 transfers $61,944.55; draft absent | Exh. A; 23-006 pp. 4-5 | verified |
| 23-024 | date and amount range | Exh. A | wrong figures → corrected |
| 21-016 | 18% interest statement | pp. 6-10 OCR | verified (+statement) |
| 21-018 | "allowed" | order para. 5 | narrowed |
| 21-019 | objection to 7664 withdrawn | p. 2 OCR | verified (scope narrowed) |
| 09-056 | $1,829,154.14; worked bill | pp. 2-5 | verified |
| 09-066 | verdict $2,472,227.10 | p. 3 | verified |
| 14-077/078/079 | effective dates; not truncated | p. 1; EOF | verified |
| 14-083 | rates as of 07-12-2023 | HTML | narrowed |
| 19-037..039 | B3 = ΣL1; STO/UNL | parsed | verified; checks added |
| 19-043/048 | shared SI | L11 | verified |
| 19-046 | redaction clean | regex, SE count | verified |
| 27-001 | 428-113379 pattern; doubles paid | CSV | verified |
| 27-005 | 13 repeated invoices | CSV | verified |
| 27-007 | negatives, row count, names | CSV | narrowed |
| 25-095 | 4,901 bills, mode and audit codes | derived CSV | verified |
| 25-124/144/130 | 166836 $363,723.74; $10,580; 166482 $6,450 | derived CSVs | verified |
| 25-044/050/052 | quotes; 6,463 → 6,569 | OCR text | verified |
| 25-046 | 4,140 lb incl. tare 272 | page image | narrowed |
| 25-115 | consumer names in original | xlsx scan | privacy flag |
| CBCA-1637 | order $12,093.71 | p. 6 | verified |
| CBCA-3467 | order $339,895.75 | p. 6 | verified |
| D63749 | 35 rows = $278.88 | page image | verified |
| D63338 | 24 rows = $727.73 | p. 3 | verified |
| GSBCA-15194 | fn. 1 sum $6,167.85 | fn. 1 | verified (ambiguity noted) |
| GSBCA-14208 | $1,845 | text | card corrupted → corrected |
| CRT-2019-63 / 2018-886 | $4,450 / $721.99 ordered | orders | verified |

## 9. Applied by the coordinator (2026-10-21)

- **All 382 row verdicts and corrections** written to `data/catalogue.csv` (`verify_status`, `verify_note`, and the corrected fields, blank values included), and every BE row's line in its set's `source.md` regenerated. Notes corrections that paraphrased the old text were applied by hand with the same meaning.
- **All 19 card corrections** applied to `data/answer_keys/`; every card carries a verification line; `INDEX.md` checks and modes refreshed. All 30 front blocks parse as YAML.
- **Privacy (§5), under the founders' rules of 2026-10-21:**
  - 25-115 replaced in `sources/` by a stripped zip; its original moved to `freight_private/idl_originals/` (six originals there now);
  - the hlkx0332 zip's residual consumer address blanked (25-032, new hash);
  - `_tools/idl_strip.py` now blanks phones inside cells and drops first/last-name columns; all of `derived/idl/` regenerated with it, then the fgcm0347 comment address, skbp0318's City-column addresses and jlwc0253's Project Team name columns blanked by hand (logged in `derived/idl/STRIPPED.md`);
  - Atlanta 27-007: 5 cells' names replaced by "[name removed]" (new hash).
- **Not changed:** 19-027 (held since check AT; a person's name and phone in a G61 segment) is left for the founders (BE §8), since it is outside BE's rows.
- **Verify:** `sha256sum -c SHA256SUMS` clean; 658 catalogue rows = 658 files under `sources/`.
