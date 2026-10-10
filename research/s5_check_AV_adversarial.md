# S5 check AV, adversarial review

- **What this is:** an evidence-backed adversarial check of check AV (the bill-side field map for C-09's audit machine) and of the parts of `data/doc-explanation.md` that rest on it. Each claim was tested to see whether it breaks. No objection was invented, and a claim that survives is reported as a result too.
- **Files checked:** `research/s5_check_AV_c09_field_map_bills.md` (the §8 ledger, 29 rows, and every number in §0, §3.1 and §4, plus the §2 and §5 cells those rest on); `data/doc-explanation.md` §1.3 (the "Freight bill", "EDI 210", "Balance-due or corrected bill" and "Statement of account" entries), §4.2 and §4.8 example C. Neither file was edited.
- **Date:** 2026-10-10.
- **Status:** input to S5. **It decides nothing.**
- **What was opened:**
  - **Set 19:** all 22 files holding 210s (82 real or assumed-real transactions, plus the template and partly real files), parsed by my own script (`scratchpad/scripts/edi.py`, `survey.py`, `odfl.py`, `tl.py`, `inv.py`, `uncoded.py`, run with `python3 -I`); the ODFL 214 file 19-017.
  - **Set 12 guides** (text layers): 3M, FedEx Freight 4010, the FedEx 4060 guide, TForce, XPO, Estes, R+L, Insight.
  - **01-001 ABF:** all 107 bill pages by script; pp. 17, 18, 23, 40, 49, 50, 53, 55, 56, 75-77 read in full.
  - **02-002 SEFL:** pp. 18, 19, 22, 28, 30, 35, 41, 43, 46, 49-52, 63, 70, 98 viewed at 80 dpi; counters of pp. 47-75 and title/PRO strips of pp. 20-98 viewed as contact sheets; worksheet p. 208 (row 292) by OCR.
  - **03-003 XPO:** pp. 4, 7, 15, 16 viewed; header strip of all 51 pages.
  - **04-006 UPS Freight:** pp. 15-16; the "PREVIOUSLY INVOICED ON" lists in every set 04 text layer.
  - **Set 21:** 21-001 pp. 11-12, 21-002 pp. 13 and 17, 21-005 pp. 4, 5 and 8, 21-006 pp. 4-5, 21-007 p. 4, 21-010 p. 4, 21-013 pp. 8-10 and a page scan of all 285, 21-014 p. 4, 21-015 pp. 4-5, 32-33 and every reprint list.
  - **Set 22:** 22-001 p. 1, 22-007 pp. 5, 7, 8, 22-008 pp. 4, 5, 7, 10, 22-011 pp. 4 and 31, 22-012 p. 4 and its rate con, 22-013 pp. 4-6, 12-13, 24-25, 22-015 p. 4.
  - **Other:** SEFL 1090 Item 753 (set 13); the Southern Furniture opinion (set 08); `catalogue.csv`.
  - **Web:** SEFL's sample invoice, fetched once from sefl.com into a fresh scratchpad folder with a generic browser user-agent. Nothing identifying was sent. Its SHA-256 equals the two copies earlier agents left in the scratchpad. Its fields were read from the raw bytes, and it has no JavaScript.
- **Not checked, and why:**
  - **Cells outside the ledger, §0, §3.1 and §4** were checked only where a claim rests on them. Not checked: ODFL's "CLASS 085"; XPO 03-003 pp. 5-6, 12, 20, 23; UPS 04-006 pp. 2-3; most of AV §5.1's key formats.
  - **The earlier doc wording quoted in AV §3.1.** That version is not in git: HEAD, commit 9e65703, holds an older draft with similar "stamps" wording. Only the file facts behind §3.1 were tested.
  - **Two doc sentences from other checks:** Pitt Ohio's FTP images and Kuehne+Nagel's document API (from check AL).
  - **"No other carrier's sample was found":** not re-searched.
- **Privacy:** no person's name, signature, phone number or home street address is copied below. Companies only.

**Words used here:**
- **KEEP-verified:** the sentence is true as written about its own population, and I re-opened the file and redid the arithmetic.
- **KEEP-assumed:** the sentence is plausible, but it rests on a reading, a label or a search I did not repeat.
- **NARROW:** the smaller or corrected reading that survives.
- **DISCARD:** the file contradicts the sentence. No sentence reached this.
- **Counter:** the "1 of N" box printed at the top right of a SEFL bill.

---

## §0 Result in one table

| Part | KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|---|
| AV ledger, 29 rows | 23 | 1 | 5 | 0 | 0 |
| AV body numbers (§0, §2/§5 cells, §3.1, §4), 27 rows | 16 | 1 | 10 | 0 | 0 |
| Doc sentences (§1.3, §4.2, §4.8 C), 70 rows | 43 | 6 | 20 | 0 | 1 |
| **All** | **82** | **8** | **35** | **0** | **1** |

**What survives.** Every piece of arithmetic AV did reproduces to the cent:
- **The EDI 210s:** 82 of 82 add up (L1 sum = B3-07 = L3-05). All 34 ODFL bills reproduce at a whole-percent discount (65/68/70/72/77) and 16.0/17.0/17.5% fuel on net. 0 of 82 fill B3-08 or K1, and none uses L1-19.
- **The PDF bills:** ABF's 23 of 101 bills in 9 same-total, same-date groups (after removing duplicate pages); SEFL 806625953; XPO's late fees; UPS 028582002 ($412.82 against $825.64, exactly double); Werner's lines; Taylor's $1,150.00.
- **The doc's §4.8 C** (ODFL PRO 00902527924, with its 214) is right in every number.

**What changes the doc** (exact text in §2). Most important first:
1. **§4.2 rule 3, SEFL p. 49.** "1 of 3" is printed, but "pages 2-3 are missing" is not shown.
   - All 14 SEFL prints from 2020 (pp. 49-62) read "1 of N", each on a different PRO (one "1 of 3", three "1 of 12", ten "1 of 30").
   - On those prints, PAY THIS AMOUNT is a base plus a 25% penalty on it: p. 52 is $50.00 + $12.50; p. 49 is $647.55 + $161.89 = $809.44.
   - The pay-amount mismatch is real, but "missing pages" is not its proven cause.
2. **§4.2 bill-date row and AV §0/§4.11/#29: "PREVIOUSLY INVOICED ON".** The list runs newest first, and it is not a complete history.
   - UPS Freight lists never show more than 4 entries (29 of 38 show exactly 4).
   - UPS 028582002 was shipped 03/30/2009. Its earliest listed invoicing is 12/21/2009, and all four entries are at $825.64, while its delivery receipt was priced at $412.82.
   - On 4 of 8 TForce bills the earliest entry falls 133-512 days after shipment.
   - So the earliest entry is a "no later than" date for the first bill.
3. **§1.3 Freight bill, Held: "59 distinct SEFL bills" should be 62.** AT's own page map gives 13 + 14 + 35 = 62, and the headers confirm 62 distinct PROs.
4. **§1.3 Balance-due, Held: "48 corrected and balance-due prints, 13 paired".** The 48 prints of 2022-23 are 37 BALANCE DUE, 7 CORRECTED and 4 ORIGINAL INVOICE. The 13 reprinted in 2025 are 12 balance-due prints and one original: p. 30 reprints p. 43, bill 806656602, an ORIGINAL INVOICE.
5. **§1.3 EDI 210: "the guides say … a second 210 with the same PRO".** No guide says the PRO is reused. The one guide that describes a follow-up invoice (FedEx's 4060 guide for Express and Ground, 12-052) gives it a new number and cites the original in L11. That the same PRO is reused is shown only by the PDF prints.
6. **§1.3 EDI 210: uncoded lines.**
   - Base-freight lines carry no L1-08 code at all three LTL carriers (ODFL 66 lines, AAA Cooper 10, Estes 3), not only at ODFL.
   - AAA Cooper's 3 deficit-weight lines are uncoded too.
   - "RES residential" appears only in guides (TForce, FedEx 4060), never in a real 210.
7. **§1.3 Balance-due: the quoted reason.** The bill prints "** PER GOOGLE EARTH THIS IS A PRA DLVY" (p. 46, also p. 91), not "PRIVATE DLVY".
8. **§1.3 Balance-due, Purpose:** "for the difference" is true of SEFL's BALANCE DUE prints only. ABF's corrected invoice, SEFL's CORRECTED INVOICE and XPO's 2021 corrected invoices restate the full corrected total.
9. **§1.3 Freight bill: "The bill also reprints … 'ARRIVAL NTC' … declared classes".** Bill 807148067 (p. 46) prints neither. They are on 806373725 (p. 24) and 806625953 (p. 41).
10. **§1.3 EDI 210: reasons arrive "only if … K1".** Estes sends its remark in an L5 line ("LEFT MSG FOR DEL APPT 11/14/13", 19-015).

The other changes are wording:
- Estes's per-pound arithmetic should be written per cwt;
- TL accessorial codes;
- AAA Cooper also needs re-mapping for 3M;
- Werner prints four or five extra lines, and its fuel is not printed per mile;
- "never by the title" should read "not by the title alone";
- the Kuehne+Nagel ledger is 276 pages;
- statements are also held in set 22;
- K1 or L5;
- one of SEFL's 2025 reprints repeats an original;
- a fixed-width ISA trap.

---

## §1 Verdict per claim

### §1.1 AV's claim ledger (§8)

| ID | Claim (short) | Verdict | Evidence | Correction |
|---|---|---|---|---|
| 1 | 82 real or assumed-real 210s; lines = B3-07 = L3-05 in all 82 | KEEP-verified | My parser: ODFL 34 (19-001…008), AAA Cooper 11 (19-009…014), Estes 3 (19-015), TL 34 (WIEL 11, TQYL 20, SPXQ 3); 0 mismatches. One trap: the three BPTS files have a 107-character ISA (ISA12 "004010"), so a fixed-width ISA reader finds only 48 of the 82 real transactions, none of the 34 TL ones (it did on my first run) | — |
| 2 | ODFL rate $/cwt (40.17 PH); charges in cents | KEEP-verified | 19-001 ST 0001: 650 × 40.17/100 = 261.11. Note: ODFL's DSC and 405 lines also put their *dollar* amount in L1-02 labelled PH (`L1**-188.00*PH*-18800`), a second mislabel | — |
| 3 | All 34 ODFL bills reproduce at {65,68,70,72,77}% and {16.0,17.0,17.5}% of net | KEEP-verified | `odfl.py`: 34 of 34 reproduce to the cent with a whole-percent discount and fuel on net (gross = base + DAA lines; uncoded $24/$11 excluded) | — |
| 4 | ODFL B3-10 = 017 on all 34 | KEEP-verified | 34/34; code 017 = "Estimated Delivery" in 12-043 (FedEx Freight) and 12-046 (XPO). On the one ODFL bill with a 214 (00902527924) the "estimated" 2012-09-27 equals the 214's D1 date | — |
| 5 | No real 210 fills B3-08 or K1 | KEEP-verified | 0 of 82. K1 appears only in 19-031 (partly real, cropped); POD and B2A only in templates | — |
| 6 | B3-08 codes: 3M AR/BE; TForce BD/RC; FedEx Freight BD/CO/PD; FedEx 4060 AD/BD/PD/RB | NARROW | Codes match (3M p. 4; 12-045; 12-043 lines 510-515; 12-052 lines 930-935). But 12-052 is headed "FedEx Express, FedEx Ground, FedEx Non-Transportation, FedEx Smart Post": a parcel guide, not an LTL guide | Label the last as "FedEx Express/Ground 4060 (parcel)". FedEx Freight's own LTL guide (12-043) already lists PD |
| 7 | AAA Cooper and Estes write the percentages as L5 text; L1-19 unused | KEEP-verified | 19-009 "LESS 78.00 PCT DISCOUNT", "Fuel Surcharge 29.00 PCT"; 19-015 "DISCOUNT 84.0%", "Fuel Surcharge added at 29.00". L1 never has more than 12 elements in a real file | — |
| 8 | Estes labels a per-cwt rate "LB" | KEEP-verified | 810 × 298.86/100 = 2,420.77; also 2,750 × 93.98/100 = 2,584.45; qualifier `LB` on both; the Estes guide lists LB as per pound | — |
| 9 | ODFL Canadian bills carry two uncoded L1 lines ($24, $11) | KEEP-verified | 19-001 ST 0005 (Brampton ON), 19-002 ST 0001 (Brampton ON), 19-003 PRO …152 (Concord ON); `L1****2400`, `L1****1100`; these are also the three 77% bills. No other ODFL bill goes to Canada | — |
| 10 | AAA Cooper: CZAR 910 (78%, NEMF interline) and SMC ZRH (87.2%, direct) for one shipper | KEEP-verified | All 5 CZAR bills carry `R3*NEMF`; all 6 SMC ZRH bills have no R3. One CZAR bill is a minimum charge (no discount); one has 29.50% fuel | — |
| 11 | TL 210s are sent by BPTS; L0-08 piece counts are junk; fuel is flat | KEEP-verified | ISA-06 `BPTS` in 19-033…035; L0-08 such as `30000 PLT` on 30,000 lb and `44001 PLT`; fuel only as a FUE dollar line. That BPTS is "a freight-payment firm" is the catalogue's label ("freight payment/broker"), so *assumed* | — |
| 12 | SEFL sample: 27 named fields incl. PageNum, TtlPageNum | KEEP-verified | My download: 2 pages, AcroForm, JavaScript none, 27 `/T` names incl. PageNum and TtlPageNum; created 2003-11-05; values dated 10/17/03-11/06/03 | — |
| 13 | SEFL p. 49 is page 1 of 3, and its pay amount ≠ printed lines | NARROW | Counter reads "1 of 3" (200-dpi crop); 1,019.77 + 117.27 + 161.89 = 1,298.93 ≠ 809.44. But 14 SEFL prints from 2020, each a different PRO, all read "1 of N" (p. 49 "1 of 3"; pp. 50, 51, 54 "1 of 12"; pp. 52-53, 55-62 "1 of 30"). And PAY THIS AMOUNT = base + 25%: p. 52 50.00 + 12.50 = 62.50; p. 50 192.54 + 48.14 = 240.68; p. 51 430.04 + 107.51 = 537.55; p. 49 647.55 + 161.89 = 809.44 | "p. 49 prints '1 of 3' and its pay amount ≠ its lines; on the 2020 layout the counter is not shown to number a bill's pages, and the pay amount is a base (not always printed) plus a 25% penalty" |
| 14 | ABF corrected notice prints the original total, the new total and the reduction | KEEP-verified | 01-001 p. 75, PRO 165261918: $326.60 → $300.52, "a reduction of $26.08" (326.60 − 300.52 = 26.08) | — |
| 15 | 23 of 101 ABF bills share total and ship date, in 9 groups | KEEP-verified | `abf.py`: 107 bill pages, 101 distinct PROs (6 bills run to two pages); by PRO, 9 groups and 23 bills; five at $256.54 on 08/07/2024. Counted by page it would be 13 groups and 33 pages | — |
| 16 | TForce prints the declared and the actual weight | KEEP-verified | 21-015 p. 33: "WEIGHT DECLARED AS 04424 LBS. ACTUAL WEIGHT IS 04665 LBS." | — |
| 17 | UPS 028582002: DR $412.82 at 86%; copy $825.64 at 65% | KEEP-verified | 04-006 p. 15: 5,582 × 37.80/100 = 2,110.00, −65% = 738.50, +11.80% = 87.14, total 825.64; p. 16: 5,582 × 47.25/100 = 2,637.50, −86% = 369.25, +11.80% = 43.57 (the OCR reads "11.00"), total 412.82. 825.64 = 2 × 412.82 exactly | — |
| 18 | ODFL's re-bill to the vendor is titled "ORIGINAL INVOICE" | KEEP-verified | 21-002 p. 17: footer "ORIGINAL INVOICE"; "CHANGE CHARGES TO PREPAID 3RD PARTY PER LETTER"; 2,472 × 132.89/100 = 3,285.04, −70% = 985.51, +133.04 +15.00 = 1,133.55 | — |
| 19 | XPO late fees: 1.5% (2021) and 10% (2024) of the pre-fee total; $10 floor *assumed* | KEEP-verified | 03-003 p. 7: (881.75 + 275.55) × 1.5% = 17.36 ×4; p. 4: 665.65 × 1.5% = 9.98, billed 10.00; 21-005 p. 8: 1,817.32 × 10% = 181.73 ×4; p. 4: 1,084.56 × 10% = 108.46 ×2, total 1,301.48 | — |
| 20 | Werner direct bills print miles; two $834.83 bills differ only in equipment, dispatch no. and weight | KEEP-verified | 22-008 pp. 7, 10: 39060407 and 39100828, both pickup 01/30/2023, 154 mi, same lines; tractor 82318/79405, trailer 378044/387449, dispatch DB498427VZ/DB539267VZ, weight 33000/4444 | — |
| 21 | Werner shipper no. "RETURN" against BOL 104310 | KEEP-verified | 22-008 p. 4 "RETURN"; p. 5 BOL "104310", trailer 64082, 1-13-23, 33,000 | — |
| 22 | Werner Logistics invoiced 92 days after delivery, against a 45-day rate-con rule | KEEP-verified | 22-013 p. 4: delivery 01-23-2025, invoice 04-25-2025 = 92 days; p. 6: invoices "received by BDS more than FORTY-FIVE (45) days after DELIVERED services … will not be accepted". The invoice date stands in for receipt | — |
| 23 | Taylor flat + per-mile fuel = the rate con's all-in $1,150 | KEEP-verified | 22-012 p. 4: 993.96 + 332 × 0.47 (156.04) = 1,150.00; rate con "Net Freight Charges USD 1,150.00" | — |
| 24 | TQL invoice dates differ from the claim list's | KEEP-verified | 22-007 p. 8: 26737009 dated 01/11/2024; p. 5 list: 1/26/2024 | — |
| 25 | Mode interest ≈ 18%/yr over 75 days, 1-4 cents off | NARROW | 21-014 p. 4: open × 18% × (age − 30)/365 reproduces only within **1-5** cents, always low. 75 days applies to the 105-day rows only (73 and 65 days elsewhere); e.g. 3,698.75 at age 103: calc 133.16, printed 133.11 | "Interest ≈ open balance × 18% × (age − 30)/365, printed 1-5 cents below; the day-count rule is unknown" |
| 26 | ODFL short-pays of $72.00 on two bills | KEEP-verified | 21-010 p. 4: 600.19 − 528.19 = 72.00; 234.32 − 162.32 = 72.00; total open 144.00 | — |
| 27 | The two $72 short-pays are one recurring deduction | KEEP-assumed | Same figures; the reason is not printed | — |
| 28 | A balance-due 210 arrives as a second 210 with the same PRO (guides only) | NARROW | The guides define codes (3M AR/BE; TForce BD/RC; FedEx BD/CO/PD) but none says B3-02 repeats the original PRO. 3M's examples use the placeholder "INVOICENUMBER". FedEx's parcel 4060 guide gives a late-fee invoice its own number and cites the original in `L11 … 'R7'` (12-052 lines 686-723) | "Guides define a correction flag in B3-08; none says the PRO is reused. Reuse is shown only on PDF prints (SEFL, ABF, XPO, TForce)." Tag stays *assumed* |
| 29 | The first "PREVIOUSLY INVOICED" entry is the original bill date | NARROW | Lists run newest first (21-015 p. 5: 06/07/23, then 03/15/23). TForce, ship date to earliest entry: 12, 13, 22, 7 days on four bills; 133, 210, 396, 512 days on the other four. UPS (set 04): 29 of 38 lists have exactly 4 entries and none has more; 028582002, shipped 03/30/2009, has its earliest entry on 12/21/2009, and all four entries are at $825.64 while its DR was priced at $412.82 | "The **earliest-dated** entry is a 'no later than' bound on the first bill date; it equals the first bill only when the list is complete" (still *assumed*) |

### §1.2 AV body numbers (§0, §2/§5 cells, §3.1, §4)

| ID | Claim (short) | Verdict | Evidence | Correction |
|---|---|---|---|---|
| B1 | §0: "The PDFs of ABF, SEFL (2023), XPO (fuel only), TForce/UPS and ODFL print the percentages" | NARROW | ODFL prints the discount % only ("Discount Allowed: 70.00%"; fuel "FUEL INCREASE 133.04", 21-002 p. 17); SEFL 2020 prints the discount only ("9100 DISC"; fuel "FUEL SURCHARG $117.27", 02-002 p. 49) | "…, TForce/UPS print both; XPO the fuel % only; ODFL and SEFL 2020 the discount % only" |
| B2 | §0/§2.4: corrections arrive in five shapes | KEEP-verified | Each shape seen: SEFL p. 41; ABF p. 75; XPO 21-005 p. 4; TForce p. 33; ODFL 21-002 p. 17. More variants exist (§3 #16) | — |
| B3 | §0: TForce/UPS reprints "list every earlier invoicing … the only bill-side record of when the first bill went out" | NARROW | As #29 | "list some earlier invoicings (UPS at most four); the earliest is a 'no later than' bound" |
| B4 | §2.2: ABF "ORIGINAL INVOICE (100), CORRECTED INVOICE (7 prints)" | NARROW | These are pages. By PRO: 97 original bills and 4 corrected (150256193, 165261918, 165261921, 165407196) | "100 original and 7 corrected pages = 97 and 4 bills" |
| B5 | §3.1: the two phrases are XPO's and TForce's; ODFL's notes read …; printed, not stamped | KEEP-verified | 21-005 p. 5 and 03-003 p. 16 (XPO); 21-015 pp. 5, 33 (TForce); 21-001 pp. 11-12 (ODFL, typed lines). The earlier doc wording AV quotes is not in git; HEAD has "ODFL stamps its own audit notes" | — |
| B6 | §3.1: neither Werner layout is "one flat line plus fuel" | KEEP-verified | 22-013 pp. 4, 12, 13 (one LINEHAUL FLT line); 22-008 pp. 4, 7 (freight, fuel, management fee, tolls, trailer, tractor use; + minimum mileage on p. 7) | — |
| B7 | §3.1: ODFL's $24/$11 have no code; "ODFL's base-freight lines also have an empty code field" | NARROW | True, but not only ODFL: base-freight lines are uncoded at AAA Cooper (10) and Estes (3) too, and AAA Cooper's 3 deficit-weight lines (`L1*2*50.85*PH*966`) are uncoded | "Base-freight lines are uncoded at all three LTL carriers; AAA Cooper's deficit lines too" |
| B8 | §3.1: AAA Cooper also writes discount and fuel as text | KEEP-verified | 19-009 | — |
| B9 | §3.1: 0 of 82 carry B3-08; "FedEx's 4060 guide also has 'PD'" | NARROW | 0/82 ✓. The 4060 guide is the Express/Ground parcel guide; FedEx Freight's 4010 guide (12-043) also lists PD. That PD is "the EDI form of SEFL's 2025 reprints" is an analogy (*assumed*) | Name it as the FedEx parcel guide; cite 12-043 for LTL |
| B10 | §4.1: 650 × 40.17 = 261.11; 188/261.11 = 72.0% | KEEP-verified | 19-001 | — |
| B11 | §4.2: 12.79/73.11 = 17.5%; PRO …931: 62.84/369.66 = 17.0%, 15.5% with the $35 | KEEP-verified | 62.84/404.66 = 15.53% | — |
| B12 | §4.3: 1,088.74 − 110.23 = 978.51 = worksheet row 292 | KEEP-verified | p. 41; p. 208 row 292: 744.77 + 55 + 178.74 = 978.51 | — |
| B13 | §4.4: 744.77/0.097 = 7,678.04 → 2,430.0 lb; TForce +241 lb, +5.4% | KEEP-verified | 7,678.04/3.1597 = 2,429.99; 4,665 − 4,424 = 241, 5.45%. The $744.77 is the shipper's worksheet figure, not a carrier print | — |
| B14 | §4.5: 1,301.48 − 1,151.48 = 150.00 | KEEP-verified | 21-005 p. 4 prints "AMOUNT PAID: US $150.00" | — |
| B15 | §4.6: 600.19 − 528.19 = 234.32 − 162.32 = 72.00 | KEEP-verified | 21-010 p. 4 | — |
| B16 | §4.7: 1,000 − (86 + 747) = 167 = DAA; 8,580 + 1,420 = 10,000 | KEEP-verified | 19-001 ST 0002 (L3 1000, DAA 167 × 36.2 = 60.45); 19-012 ST 0004 (`L0*2*10000*LB*1420`) | — |
| B17 | §4.8: 93.94/154 = 0.61; 97.02/154 = 0.63; Taylor 332 × 0.47 = 156.04; TQYL $301.95 on $2,600 and $2,100 | KEEP-verified | 22-008 pp. 4, 7; 22-012 p. 4; 19-034: 34766638 (2,600), 34688921 and 34688904 (2,100), all Weyauwega-Springfield, all 41,140 lb | — |
| B18 | §4.9: late-fee bases; RXO 450 × 1.015 = 456.75 | KEEP-verified | As #19; 22-011 p. 31 "REVISED INVOICE": −875, −875, +875 → 450.00; "AFTER 9/10/2025: 456.75" | — |
| B19 | §4.10: UPS re-rate | KEEP-verified | As #17 | — |
| B20 | §4.11: 610384246 shipped 03/03/23, earliest listing 03/15/23 (12 days); "the date the shipper's 180 days are counted from" | NARROW | Arithmetic ✓ (21-015 p. 5). Read as the first bill only when the list is complete (see #29) | Add "if the list is complete; otherwise a 'no later than' date" |
| B21 | §4.12: R3-08 = $126.98 of $325.60 = 39.0% to NEMF | KEEP-verified | 19-009; the same 39.0% on all five NEMF bills (5031/12900, 11188/28687, 44150/113205, 34104/87446). Whether R3-08 is NEMF's share or AAA Cooper's is *assumed* | — |
| B22 | §4.13: 509 × 600.80/100 = 3,058.07; 645 × 733.17/100 = 4,728.95; 2,472 × 132.89/100 = 3,285.04 | KEEP-verified | 02-002 p. 46; 01-001 p. 23; 21-002 p. 17 | — |
| B23 | §5.2: UPS and TForce copies list the same PRO "2-4 times" | NARROW | TForce lists hold 1-4 entries (four bills have one); UPS 0-4, mostly 4 | "1-4 times" |
| B24 | §5.2: SEFL's 2025 reprints repeat 2023 balance-due bills (pp. 23-35 against pp. 36-48) | NARROW | 13 pairs ✓, but p. 30 (upside down) reprints 806656602, which p. 43 shows as an ORIGINAL INVOICE (pay = total, $609.57) | "repeat 2023 bills: 12 balance-due prints and 1 original" |
| B25 | §2.5: Kuehne+Nagel ledger row on 21-013 p. 8 | NARROW | p. 8 is the "EXHIBIT A" cover; the row `C94886386 … RDWY349533831X` is on p. 10; the ledger runs pp. 10-285 (276 pages) | Cite p. 10 |
| B26 | §2.5: YRC statement shows "bill, pickup and delivery dates" | NARROW | 21-006 p. 5 shows Age, Bill Date, Due Date, Tariff, P/C, Pickup Date; no delivery date seen | "bill, due and pickup dates" |
| B27 | §2.1: BPTS is "a freight-payment firm" | KEEP-assumed | Catalogue label only | — |

---

## §2 The doc's sentences (§1.3, §4.2, §4.8 C)

Abbreviations in this section: KV = KEEP-verified; KA = KEEP-assumed; N = NARROW.

### §1.3 "Freight bill (the invoice)"

| # | Sentence (short) | Verdict | Evidence | Exact replacement if it must change |
|---|---|---|---|---|
| F1 | "per firm in layout … No two carriers' bills look alike." | KA | Consistent with every layout viewed | — |
| F2 | SEFL sample: dummy data dated 2003, same layout as 2023 Exist bills, named fields (ProNumber, BillType = "ORIGINAL INVOICE", …) | KV | My download (see header): all listed names present; BillType value "ORIGINAL INVOICE"; dates 10/17/03-11/06/03; layout matches 02-002 p. 41 | — |
| F3 | "No other carrier's sample was found." | KA | Not re-searched | — |
| F4 | SEFL 2020 "DISCOUNT PERCENTAGE 9100"/"9100 DISC"; 2023 "88.15% DISC"; rates without a point ("60080"; "65255.") | KV | p. 49 "DISCOUNT PERCENTAGE 9100"; p. 50 "9100 DISC", "65255."; p. 46 "88.15% DISC", "60080" | — |
| F5 | ABF "Tariff: AOD000"; "DEF163 … ALLOWS LOWER CHARGE AT HIGHER WEIGHT" | KV | AOD000 on all 107 bill pages; DEF163 on p. 17 | — |
| F6 | XPO one discount line, "M", "RE-WEIGHED PER WEIGHT CERTIFICATE" | KV | 03-003 pp. 4, 15, 16; 21-005 pp. 4-5 | — |
| F7 | TForce "WAIVED INSPECTION" and both weights | KV | 21-015 pp. 5, 33 | — |
| F8 | ODFL audit lines | KV | 21-001 pp. 11-12 | — |
| F9 | UPS Freight 2008-10 mostly scans, via `derived/ocr/`; the faxed bills are ODFL's of 2004-08 | KA | `derived/ocr/04_delphi_ups_freight/` exists; 21-001 is faxed (JUN-30-2008 header) and 21-002 holds a 2005 fax; no exhaustive search for other faxes | — |
| F10 | "Werner bills in two layouts, one all-in linehaul line with no fuel (Werner Logistics) or freight plus fuel per mile with the miles printed and five more lines (Werner Enterprises)" | N | 39015347 has four more lines; 39060407 and 39100828 have five; the fuel line is a dollar amount, "FUEL ADJ/MILEAGE 93.94", with no per-mile rate printed (22-008 pp. 4, 7, 10) | "Werner bills in two layouts: one all-in linehaul line with no fuel (Werner Logistics), or freight plus a "FUEL ADJ/MILEAGE" dollar line, the miles (154) and four or five more lines (Werner Enterprises; $0.61 a mile is derived, not printed);" |
| F11 | Wintzer bills per ton | KV | 22-001 p. 1: 19.74 × $16.50 = $325.71; 21% fuel $68.40 | — |
| F12 | Rates in dollars at XPO and TForce, in cents with no point at ABF, SEFL, ODFL; unit settled by weight × rate | KV | §1.2 B22; XPO "391.89"; TForce "106.84" | — |
| F13 | Primary example reconciles: 88.15% off, class 70 FAK, liftgate $55 | KV | Agreement p. 19, WCPC outbound 88.15%, class 70, FAK 77.5-175; p. 22 liftgate DIRECT to PARTNERSHIP $55; bill p. 46 DEST C/L "OAKH" | — |
| F14 | Gross rate and 22.00% fuel not checkable | KV | No base tariff; set 14 has no SEFL table | — |
| F15 | The added line is priced exactly by Item 753 | KV | SEFL 1090 Item 753 (eff. 12/16/2022): $7.60/cwt, min $94, max $575; 509 × 7.60/100 = 38.68 → $94 | — |
| F16 | "The bill also reprints parts of the BOL: special instructions ("'LIFTGATE DELIVERY", "'ARRIVAL NTC"), the quote number and the shipper's declared classes." | N | 807148067 (p. 46) shows "'LIFTGATE DELIVERY" and the quote, but no "ARRIVAL NTC" and no declared class ("PLT APPAREL IT-49880 / STC 16 BX"). "'ARRIVAL NTC" is on p. 24 (806373725); declared classes on p. 24 and p. 41 | "SEFL's bills also reprint parts of the BOL: special instructions ("'LIFTGATE DELIVERY" on 807148067; "'ARRIVAL NTC" on 806373725, p. 24), the quote number and, on some bills, the shipper's declared classes ("CL150 NMFC 49880-", pp. 24 and 41)." |
| F17 | Held: "101 ABF bills …; 59 distinct SEFL bills as scans (set 02); 6 XPO invoices (set 03); 853 pages of UPS Freight …" | N (SEFL only) | ABF 101 ✓; XPO 6 ✓ (712-591246, 712-591121, 405-677016, 405-634110, 326-343835, 976-973841); set 04 bill files 103+111+108+92+107+117+113+92+10 = 853 ✓. SEFL: pp. 36-48 (13) + pp. 49-62 (14) + pp. 63-97 (35) = 62 distinct PROs, no repeats (title strips); AT §7.0's own map sums to 62 | Replace "59 distinct SEFL bills" with "62 distinct SEFL bills". The same denominator appears in §1.2 ("9 of the 59") and `data/README.md` |

### §1.3 "EDI 210"

| # | Sentence (short) | Verdict | Evidence | Exact replacement if it must change |
|---|---|---|---|---|
| E1 | Purpose: the same invoice as a machine file | KV | — | — |
| E2 | "the X12 segment skeleton … is shared, so one parser reads every carrier's envelope" | N | Skeleton ✓. But the three BPTS files' ISA is 107 characters (ISA12 "004010", standard 5 characters), so a fixed-width ISA reader mis-splits them (mine found 48 of the 82 real transactions, none of the TL ones, until fixed) | Append: "provided it takes the separators from the ISA's own characters, not from fixed widths: the three BPTS truckload files carry a 107-character ISA." |
| E3 | Estes and AAA Cooper text; ODFL bare DSC and 405 lines; 188.00/261.11 = 72.0%, 12.79/73.11 = 17.5% | KV | §1.1 #2, #7; §1.2 B10-B11 | — |
| E4 | "Rates are in dollars per cwt and every carrier's charge field is in cents (an X12 rule)" | KV | L1-04 and B3-07 are N2 in every guide read; weight-line rates PH. Exceptions in the rate field: Estes FR 197.00 flat, AAA Cooper MN, TL 0.00, ODFL DSC/405 dollars labelled PH | — |
| E5 | "810 lb × 298.86 = $2,420.77 only works per hundredweight" | N | 810 × 298.86 = 242,076.60; the printed charge needs 8.10 cwt | "Estes labels its per-cwt rate "LB" (per pound): 8.10 cwt × $298.86 = $2,420.77, the printed charge; read per pound it would be $242,076.60." |
| E6 | AAA Cooper names the base tariff in L7 (`L7*1*CZAR*910`) | KV | 19-009 | — |
| E7 | "TL carriers bill a flat linehaul (code 400) plus fuel and TONU." | N | 19-033…035 codes: 400 ×34, FUE ×34, LUM ×8, LAY ×2, STOP, STC, TONU ×1 | "TL carriers bill a flat linehaul (code 400, 0.00 in the rate field) plus a fuel dollar line (FUE) and coded accessorials (LUM, LAY, STOP, STC, TONU)." |
| E8 | Versions run 4010 to 4060 | KV | Guides 4010 (3M, Estes, TForce, FedEx Freight) and 4060 (FedEx parcel) | — |
| E9 | "3M rejects negative amounts, on line charges as well as the total, so ODFL's and Estes's negative discount lines must be re-mapped" | N | 3M B307, L104, L305: "3M is unable to accept a negative dollar amount" ✓. AAA Cooper sends negative DSC lines too (19-009…014) | "…, so the negative discount lines of ODFL, AAA Cooper and Estes must be re-mapped for it;" |
| E10 | Insight requires a proof-of-delivery segment | KV | 12-047 line 41: POD "M … Must use" | — |
| E11 | Core fields structured; percentages may be missing (ODFL) | KV | §1.1 #3 | — |
| E12 | "The carrier's printed reason … arrives only if the carrier fills the optional K1 remarks segment, 30 characters a field; 3M has to require it for balance-due bills." | N | K101 AN 1/30 ✓; 3M "Reason for balance due invoice should be sent in K1" ✓. But Estes sends a remark in L5 ("LEFT MSG FOR DEL APPT 11/14/13", 19-015), and K1 appears in no real file | "The carrier's printed reason ("PER GOOGLE EARTH …", "CLASS INSPECTION PER W&I") arrives only as free text: in the optional K1 remarks segment (30 characters a field), which 3M requires on balance-due bills and no real 210 held uses, or in an L5 line, as Estes sends its remarks." |
| E13 | No 210 carries the BOL, the delivery receipt or a weight certificate | KV | None of the 82; Insight's POD segment carries a date and a name, not the receipt | — |
| E14 | Pitt Ohio FTP images; Kuehne+Nagel document API | Not checked | From check AL | — |
| E15 | TForce: "copies of the delivery receipts or bills of lading are no longer mailed to the customer" | KV | 12-045 lines 443-444 | — |
| E16 | "In return a 210 gives a code for most extra charges (405 fuel, DSC discount, RES residential, TONU), though ODFL's base-freight lines and two of its Canadian charges ($24 and $11) carry none." | N | Uncoded lines in real files: ODFL base 66 + the $24/$11 ×3 bills; AAA Cooper base 10 + deficit 3; Estes base 3. RES appears only in 12-045 and 12-052 | "In return a 210 codes most extra charges (405 or FUE fuel, DSC discount, LUM, LAY, TONU; RES residential appears in the TForce and FedEx guides, not in a real file held). Lines with no code: the base-freight lines of all three LTL carriers (ODFL, AAA Cooper, Estes), AAA Cooper's deficit-weight lines, and ODFL's $24 and $11 lines on its three Canadian bills." |
| E17 | ODFL 017 on all 34 | KV | §1.1 #4 | — |
| E18 | All 82 add up | KV | §1.1 #1 | — |
| E19 | "The carriers' guides say a balance-due bill comes as a second 210 with the same PRO, flagged in B3-08 ("BD" at TForce and FedEx Freight; 3M asks for "AR" with the reason in K1), but none of the 82 fills B3-08 or K1, so that rests on the guides alone." | N | Codes ✓; "same PRO" not in any guide (§1.1 #28) | "The carriers' guides define a balance-due or corrected 210 flagged in B3-08 ("BD" at TForce and FedEx Freight; 3M asks for "AR" with the reason in K1). None says the PRO is reused (FedEx's parcel guide gives a late-fee invoice its own number and cites the original in L11); reuse of the PRO is seen only on PDF prints (SEFL, ABF, XPO, TForce). None of the 82 real 210s fills B3-08 or K1, so the EDI form of a correction is unseen." |
| E20 | Held: 36 files; 26 real (ODFL 8, AAA Cooper 6 "to one book publisher", Estes 1; 214s 8; 204s 2; TL tender 1); 4 assumed real; 1 partly real; 5 templates; 14 guides | KA | Counts ✓ (catalogue: 26/4/1/5; set 12 = 14). "One book publisher": the ODFL bills go to two bill-to names (Dalmatian Press LLC ×5; Anderson Press Inc., in care of a logistics firm ×29), for shippers named Dalmatian Press and Whitman Publishing at one Florence, AL address; AAA Cooper's bills name no bill-to. Affiliation is *assumed* | Optional: "to one Florence, AL book shipper" |

### §1.3 "Balance-due or corrected bill"

| # | Sentence (short) | Verdict | Evidence | Exact replacement if it must change |
|---|---|---|---|---|
| BD1 | "Purpose: a second bill under the same PRO number for the difference, issued when the carrier re-rates after delivery." | N | Only SEFL's BALANCE DUE prints ask for the difference (p. 41 $110.23; p. 46 $94.00). ABF 165261918 asks the full corrected $300.52; SEFL CORRECTED 896789802 asks the full $483.15; XPO 2021 CORRECTED asks the full total and adds "IF ORIGINAL CHARGES HAVE BEEN PAID, PLEASE REMIT THE DIFFERENCE"; ODFL's re-bill changes the payer, not the rate | "*Purpose:* a later bill under the same PRO number, issued when the carrier re-rates or re-bills after delivery. SEFL's BALANCE DUE prints ask only for the difference; ABF's and SEFL's corrected invoices and XPO's 2021 ones restate the full corrected total." |
| BD2a | "per firm, in five shapes. SEFL …; ABF …; XPO … with "RE-WEIGHED PER WEIGHT CERTIFICATE"; TForce …; ODFL …" | KV | §1.2 B2; XPO's paid/balance (21-005 p. 4) and re-weigh note (p. 5) are on the same PRO | — |
| BD2b | "So a correction is found by the PRO plus a changed amount or payer, never by the title." | N | Titles do flag SEFL, XPO and ABF corrections; the doc's own §4.2 uses "PDF title plus a changed amount or payer". The point is that the title is not sufficient: ODFL p. 17; 26 ABF ORIGINAL INVOICE pages carry W01/W02 reweigh codes | "So a correction is found by the PRO plus a changed amount or payer, not by the title alone." |
| BD3 | The $94 line on the print of 06/19/2023, 35 days after shipment, "with the carrier's reason printed ("** PER GOOGLE EARTH THIS IS A PRIVATE DLVY")" | N | Dates ✓ (p. 46: shipped 05/15/2023, billed 06/19/2023 = 35 days). The bill prints "** PER GOOGLE EARTH THIS IS A PRA / DLVY" (p. 46; also p. 91; p. 93 "…A RESIDENTIAL DLVY; PRA NOT IN…") | Replace the quote with: ("** PER GOOGLE EARTH THIS IS A PRA DLVY") |
| BD4 | Weight change on the balance-due print of 05/05/2023, 16 days after shipment | KV | p. 41: shipped 04/19/2023, billed 05/05/2023 | — |
| BD5 | 13710(a)(3)(B) "within 180 days of receipt of the bill"; windows to 2023-12-16 and 2023-11-01 | KV | Southern Furniture text, line 826; 06/19 + 180 = 12/16; 05/05 + 180 = 11/01 | — |
| BD6 | Match every balance-due bill to its original and to every later reprint; the 2025 PAST DUE prints are reprints | KV | pp. 28, 33, 35 reprint pp. 41, 46, 48 with DATE BILLED 08/26/2025 and "INVOICE PENDING" in PAY THIS AMOUNT. One of the 13 repeats an original (BD7) | — |
| BD7 | "Held: 48 SEFL corrected and balance-due prints, 13 of them paired with their 2025 reprints (set 02)" | N | Title strips of pp. 36-48 and 63-97: BALANCE DUE 37, CORRECTED 7 (pp. 63, 68, 72, 75, 76, 78, 79), ORIGINAL 4 (pp. 43, 70, 73, 96). The 13 pairs (pp. 23-35 against 36-48) include p. 30 ↔ p. 43, an ORIGINAL | "*Held:* 48 SEFL prints of 2022-23 (37 BALANCE DUE, 7 CORRECTED, 4 ORIGINAL INVOICE), 13 of them (12 balance-due, 1 original) paired with their 2025 PAST DUE reprints (set 02);" |

### §1.3 "Statement of account"

| # | Sentence (short) | Verdict | Evidence | Exact replacement if it must change |
|---|---|---|---|---|
| S1 | Purpose: the carrier's list of open bills; where short-pays show | KA | 21-010 shows the $72 short-pays | — |
| S2 | "from a one-page list to Kuehne+Nagel's 285-page pro ledger" | N | 21-013 is a 285-page claim: pp. 1-7 the claim form, p. 8 the exhibit cover, pp. 10-285 the ledger (276 pages, counted by script) | "from a one-page list to Kuehne+Nagel's 276-page pro ledger (pp. 10-285 of a 285-page claim)" |
| S3 | The unpaid $94 and $110.23 would sit on SEFL's statement; the 2025 reprints are the collection step | KA | No SEFL statement held; the 2025 prints are titled PAST DUE INVOICE, due 09/10/2025 | — |
| S4 | "Held: sets 21 and 24." | N | AV's own statements include RXO 22-011 p. 4 (set 22). The catalogue also tags statements in sets 01, 03, 04, 09, 22, 23 | "*Held:* sets 21 and 22 (the layouts in AV §2.5, including RXO, 22-011 p. 4) and 24; the catalogue also tags statements in sets 01, 03, 04, 09 and 23." |

### §4.2 Stage 1

| # | Sentence (short) | Verdict | Evidence | Exact replacement if it must change |
|---|---|---|---|---|
| R0 | Read the 210 first: its numbers need no reading | KV | 82/82 add up | — |
| Ta | PRO, lines, total: 210 → PDF text → OCR, checked against the column sum and XPO's scan line | KV | XPO scan lines "712591246 0069565 6", "266489086 0115148 5" = PRO + cents + check digit | — |
| Tb | Discount %, fuel %: PDF → 210 text (AAA Cooper, Estes) → derive; ODFL example | KV | §1.2 B10-B11 | — |
| Tc | Rate unit: test weight × rate; SEFL "60080" × 5.09 cwt = $3,058.07 | KV | p. 46 | — |
| Td | Bill type: title + changed amount or payer on a known PRO → 210 B3-08; ODFL "ORIGINAL INVOICE" | KV | 21-002 p. 17 | — |
| Te | Carrier's reason: PDF remarks → "210 K1" | N | E12 | Change "210 K1" to "210 K1 or L5 text (Estes)" |
| Tf | What the BOL asked for: the PDF's echo only; "The 210 does not carry it" | KV | No special instructions, declared class or quote number in any real 210 | — |
| Tg | Ship date: 210 B3-12 or G62 → PDF → BOL | KV | §2.1 | — |
| Th | Bill date for the clock: "The earliest of: first 210's B3-06, the PDF bill date, the first "PREVIOUSLY INVOICED ON" entry" | N | §1.1 #29: the list runs newest first (the first *listed* entry is the latest) and can be cut short | "The earliest of: the first 210's B3-06, the PDF bill date, the earliest-dated "PREVIOUSLY INVOICED ON" entry (the list runs newest first and can stop short: UPS Freight's never shows more than four, and on 4 of 8 TForce bills its earliest entry is 133-512 days after shipment, so treat it as a "no later than" date)" |
| Ti | Delivery date: DR or 214; 210 only if 035; ODFL 017 | KV | §1.1 #4 | — |
| Tj | Payer, terms: B3-04 + bill-to → PDF terms → statement | KV | 19-033 PP/CC/TP | — |
| Tk | Paid, open balance: statement → XPO and SEFL balance lines → payment export | KV | 21-005 p. 4; 02-002 p. 41 | — |
| R1 | "SEFL's 2025 "PAST DUE INVOICE" prints repeat 2023 balance-due bills; they are not new bills." | N | BD7: one of the 13 repeats an ORIGINAL INVOICE | "SEFL's 2025 "PAST DUE INVOICE" prints repeat 2023 bills (12 balance-due prints and one original, 806656602); they are not new bills." |
| R2 | Match on keys; "23 of the 101 ABF bills share both with another bill" | KV | §1.1 #15 | — |
| R3 | "Read the page counter and group pages by PRO. SEFL p. 49 says "1 of 3", pages 2-3 are missing, and its pay amount does not equal its printed lines." | N | §1.1 #13 | "**Do not check an incomplete bill.** Group pages by PRO and read the page counter: ABF's corrected bill 165261918 runs onto a second page (pp. 75-76). A counter is evidence, not proof: SEFL's fourteen 2020 prints (pp. 49-62) each read "1 of 3", "1 of 12" or "1 of 30" on a different PRO. And there PAY THIS AMOUNT is not the bill's total but a base plus a 25% penalty (p. 52: the $50.00 limited-access line + $12.50; p. 49: $647.55, not printed, + $161.89 = $809.44, against $1,298.93 of printed lines)." |
| R4 | Original = new total − balance due (806625953) | KV | §1.2 B12 | — |

### §4.8 example C (ODFL PRO 00902527924)

| # | Sentence (short) | Verdict | Evidence |
|---|---|---|---|
| C1 | 650 × $40.17 = $261.11; −$188.00; fuel $12.79; total $85.90 = B3-07; 72.0%, 17.5%; delivery coded estimated | KV | 19-001 ST 0001 |
| C2 | 214: delivery 2012-09-27 at 11:07; 606 lb on the first message, 650 lb at pickup and delivery | KV | 19-017 (baldr_214_2): ST 0001 `AT7*AG` (estimated delivery) 20120927 1600 CT, `AT8*G*L*606`; ST 0002 `AT7*AF` (departed pickup) 20120925, 650; ST 0004 `AT7*D1` (completed unloading) 20120927 1107 CT, 650 |
| C3 | ODFL's agreement and 2012 fuel table not held | KV | Set 14 holds no ODFL table; set 13's ODFL 100-Q is 2025 and points to "Fuel Increase Master Tariff ODFL 128", not held |
| C4-5 | Arithmetic passes; levels cannot be compared | KV | As C1 |
| C7 | Verdict "not checkable" | KV (the inputs; the verdict is *our call*) | — |

---

## §3 Counter-examples searched for, and what was found

1. **A real 210 with B3-08 or K1:** none among the 82. K1 appears only in 19-031 (partly real, cropped); no template fills B3-08.
2. **A real 210 using L1-19:** none (L1 never runs past element 12).
3. **An ODFL bill not on a whole percent:** none. All 34 reproduce exactly.
4. **An ODFL Canadian bill without the $24/$11, or a non-Canadian bill with them:** none. The three Canadian consignees carry both, and all three are the 77% bills.
5. **Uncoded lines beyond ODFL's $24/$11: found.** Base-freight lines at all three LTL carriers (79 lines: ODFL 66, AAA Cooper 10, Estes 3) and AAA Cooper's 3 deficit-weight lines. ODFL also puts DSC and 405 dollar amounts in the L1-02 rate field labelled PH, a trap for any parser that multiplies weight × rate on PH lines. This supports AV's "never assume the unit" rule.
6. **An ABF same-total pair that is the same bill:** none. All 23 have distinct BOL numbers or, where the BOL reads "SEE BELOW", distinct pieces, weights and dimensions (pp. 50, 53, 55, 56). A trap was found instead: six ABF bills run to two pages, so a page-level count gives 13 groups and 33 pages instead of 9 and 23.
7. **The ODFL "estimated" delivery date against the actual:** on the one bill with a 214, they are the same date (2012-09-27).
8. **The SEFL page counter: found.** Counters on 14 different 2020 bills, all reading "1 of N". The penalty pattern explains every 2020 PAY THIS AMOUNT checked (pp. 49-52).
9. **Completeness of "PREVIOUSLY INVOICED ON": found.** UPS lists stop at four entries. UPS 028582002's four entries all post-date and differ from its $412.82 pricing. On 4 of 8 TForce bills the earliest entry is 133-512 days after shipment.
10. **"Same PRO" in the guides:** none. FedEx's parcel guide gives a new invoice number with the original in L11.
11. **SEFL titles: found.** p. 43 is an ORIGINAL INVOICE inside the balance-due run, and p. 30 is its upside-down 2025 reprint.
12. **SEFL distinct bills:** 62, not 59.
13. **Fixed-width ISA: found.** The three BPTS files have a 107-character ISA.
14. **"PRIVATE DLVY" anywhere in set 02:** none. The bills read "PRA DLVY" (pp. 46, 91) and "RESIDENTIAL DLVY; PRA NOT IN…" (p. 93). "PRIVATE" occurs only on pp. 58 and 60.
15. **"'ARRIVAL NTC" on 807148067:** absent. It is on p. 24 (806373725), among other pages.
16. **Correction shapes beyond five: found.**
    - RXO's TL "REVISED INVOICE" (22-011 p. 31) prints payment lines −875, −875, +875 and a remaining subtotal.
    - XPO's 2021 "CORRECTED INVOICE" restates the full total with "IF ORIGINAL CHARGES HAVE BEEN PAID, PLEASE REMIT THE DIFFERENCE".
    - SEFL's CORRECTED INVOICE (p. 63) gives the full total and no reason. AV lists this one itself in §2.4.
17. **Mode interest:** residuals of 1-5 cents, all low; none exact.
18. **Werner extra lines:** four on 39015347, five on 39060407 and 39100828.
19. **ABF ORIGINAL INVOICEs carrying reweigh codes:** 26 pages, not just p. 77 (e.g. pp. 17, 22, 27, 43).

---

## §4 Concerns left unproven

These are stated as concerns, not findings.

- **What SEFL's 2020 counter numbers** (a mailing batch, a statement run, or something else). Also how the unprinted base on p. 49 ($647.55) arises, for example an earlier part-payment. Neither is printed.
- **Whether R3-08 is NEMF's share or AAA Cooper's.** The same 39.0% appears on all five interline bills.
- **BPTS's identity** as a freight-payment firm rests on the catalogue.
- **Stripping letter suffixes** from PROs (§4.2 rule 2) could merge an original with a re-issued invoice, if a suffix marks re-issue. TQL's "26531517A" is the only suffixed number in its list. No case was found.
- **The 2,430 lb reading** for 806625953 assumes the same per-cwt rate at 2,430 and 2,720 lb. Without SEFL-0550, the weight break is not checked.
- **The catalogue dates the set 19 214s 2013-02-11,** but 19-017's ISA date is 2012-10-15, matching the 210 it describes. This is a catalogue issue, outside AV.
- **"9 of the 59" in the doc's §1.2** shares the corrected denominator (62). The nine residential lines were not re-counted here.
- **AV §3.1 quotes a doc version** that is not in git, so whether those exact sentences existed cannot be checked.
