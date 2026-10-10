# Check AT · The public document dataset for the C-09 prototype

**What this is.** The founders' request of 2026-10-09, verbatim: "I want you to find a real example of a mismatch, one that would correspond to a discrepancy and a dispute in 180 days. We need this data to begin building out our initial prototype. We want as diverse of a dataset as possible, to ensure we can cover any and all edge cases. So as many discrepancies, document types, and formats of the document itself. Are these documents a standardized format or does each firm and shipping company have their own? … This will require extensive web search to find leads on where we can find the documents, then pulling the actual documents themselves and saving them in data/". Scope set the same day: **TL and LTL only; three lead-finding agents plus one verifier; free sources only** (paywalled items are logged, not bought).

*Revised 2026-10-10 after the field-map checks AV, AW and AX (`data/doc-explanation.md` §4); the first version is in git. Corrected: what decides the residential charge, the set 19 counts, carrier-issued certificates (held), SEFL's sample bill, ODFL's and Werner's formats, Walmart's empty lanes appendix.*

**Builds on:** AC (example invoices), AD (Delphi and DOJ reweigh files), AJ (document formats), AK (the 33 checks), AO (tariffs and claim forms), the practice audit. **Date:** 2026-10-09. **Status:** an input to the prototype. It decides nothing. **Searches used:** 383 queries, register lookups and candidate URLs are logged in `data/leads_tried.csv` (206 hits, 125 misses, 51 blocked, 1 too large). **No identity was sent:** every agent brief forbade the user's name or email in headers, forms or queries; sec.gov was not fetched; nobody was contacted; no logins. **Labels:** *verified* = the file was opened and read; *assumed* = snippet, party statement or OCR only. **Adversarial review:** `s5_check_AT_adversarial.md` (summary in §0.1, written after the review).

## 0. Summary

| | Before (2026-10-08) | After |
|---|---|---|
| Files in the project | 0 (one PNG) | **271** in `data/sources/`, 24 sets, 10,474 pages, 438 MB |
| Real documents (from actual shipments, contracts or disputes) | 0 | **188** (after the adversarial corrections) |
| Real TL invoices to a shipper | none public | **yes** (Werner, USA Truck, Wintzer, Taylor, Autumn, Cornerstone; TQL and RXO broker invoices) |
| Real EDI 210 interchanges | none (guides only) | **36 files** (26 real, 4 assumed real, 1 partly real, 5 templates): 210s from ODFL, AAA Cooper, Estes and three TL batches; 214s from Holland, ODFL, SEFL, R+L and WTVA; 204 tenders |
| Carrier responses to overcharge claims | none | **yes** (YRC "APPROVED" printouts on nVision claims; a GlobalTranz TONU and reweigh dispute with the weight certificate; a Manitoulin interline dispute) |
| Corrected bills with the error shown | one note on an ABF bill | ODFL wrong-payer correction end to end (Winn-Dixie), 39 pages of ODFL bills with the carrier's own audit notes (Paper-Pak), SEFL 2025 re-bills |
| Checks (A1-G2) with real evidence | about 18 | **all 33**, thinnest on E1 (guaranteed-service refund), F2, F4 |
| Carriers in real documents | 6 | about 60 distinct names |

**0.1 Adversarial summary** (`s5_check_AT_adversarial.md`). All 271 rows were checked: **145 verified, 123 narrowed, 3 wrong.** The three wrong rows: two DOJ exhibits catalogued as reweigh evidence are lists of government tenders with no weights or dollars; GSA 1000-D is a five-page rate table, not a rules tariff. The recurring narrowings: checks tagged from a document's boilerplate rather than an instance (detention, TONU and lumper on rate confirmations; late fees on plain statements), filing dates used as shipment dates, "complaint" on answers and exhibits. After corrections 188 files are real, and **F2 (GL coding) and F4 (rebilled freight) have no real evidence; E1 (guaranteed-service refund) has one file and B9 (fuel base) three.** The worked example's transcription, arithmetic and agreement reading all held, but **its first version's timing claim was wrong**: the verifier found the same bill on p. 41 as a balance-due invoice dated 2023-05-05 for exactly the $110.23 difference, so the carrier re-rated the weight 16 days after shipment, not 22 months later. §7 was rewritten on that finding, and the verifier's recommended primary example (one added line, with the carrier's reason printed) is now first. Coverage counts in §5 are the corrected ones. The verifier's sub-agents were cut off by a session limit, so sets 01, 03-06, 10 and 11 had identity checks only; their check tags stand as the collectors claimed.

**The format answer in one sentence:** only the EDI X12 skeleton, the VICS/GS1 bill-of-lading form, NMFC classes, Part 378's claim content and the "Standard Form for Presentation of Overcharge Claims" are shared; every carrier's PDF bill, its mapping of the 210, its rules tariff, its fuel table and its claim channel, every rate agreement, and every broker's rate confirmation are its own (§6).

**The worked mismatch:** SEFL bill 807148067, shipped 2023-05-15: 35 days later the carrier issued a $94.00 balance-due bill adding one line, "PVT RESIDEN 94.00", with its reason printed on the bill, "per Google Earth this is a private delivery". One line, one tariff item (SEFL 1090 Item 753, $94 minimum), and one fact decides it: is there a dwelling on the delivery premises? Item 753 charges whenever there is, and an unmarked BOL does not relieve the shipper. The shipper's 180 days to contest ran to about 2023-12-16. The shipper's own worksheet never flagged the $94; it claimed $210.38 on the base freight by a theory that misreads the agreement (§7). A second example, bill 806625953, shows a weight raised from 2,430 to 2,720 lb on a balance-due bill with no inspection note.

## 1. Method

- **Round 0, rescue (coordinator, no web).** Every PDF the earlier checks had downloaded still sat in old session scratchpads under `/tmp` (lost on reboot). 106 files were copied into `data/`, hashed, page-counted and tested for a text layer, and catalogued from the research files' source tables. Dropped after opening: a Miller v. Costco deposition (135 pp), a Vital Pharmaceuticals sale order (280 pp), bankruptcy payment lists (not freight documents; listed in `data/README.md` as known, not kept).
- **Round 1, three agents by territory.** A, courts (CourtListener's RECAP search API, anonymous, free PDFs only; 45 queries, ~105 candidate PDFs opened, 43 kept). B, bankruptcy claim registers (Epiq, Angeion/Donlin Recano reachable without a browser; Kroll, Stretto, Omni, Verita blocked; 51 claims kept out of ~70 opened). C, standards, carriers, government and archives (45 searches, 5 GitHub code searches, 6 Wayback calls; 70 files kept). Each agent delivered a manifest, a leads log and a findings note with a claim ledger; the coordinator mapped files to sets, deduplicated by SHA-256 and merged the logs.
- **Hygiene.** Every download in its own empty directory; scripts kept apart; Python run with `-I`; generic user agent; 25 MB per file cap; company names only in the catalogue.
- **Round 2, verification.** One agent opened every real-document file (first, middle, last page), confirmed or corrected the catalogue row, cited an evidencing page per check, re-transcribed the worked example from the PDF, described the files no earlier check had read, measured OCR accuracy on scanned bills, resolved the unknown URLs and spot-checked privacy → `s5_check_AT_adversarial.md`. A script checked every hash, page count and URL.

## 2. Where the documents came from, and what did not work

| Channel | Result | Notes |
|---|---|---|
| **CourtListener RECAP** (free copies of PACER filings) | 79 files | The API answers anonymously at 5 queries a minute, 50 an hour; docket HTML pages refuse `curl` (use `docket_id:` filters). Exhibits often listed but not attached; several wanted exhibits are PACER-only (§10). |
| **Bankruptcy claims agents** | 49 claims | **Epiq** has a JSON search endpoint and a document-by-id link (Yellow, STG Logistics, Instant Brands, Tupperware, Tuesday Morning); **Angeion/Donlin Recano** (NEMF) answers HTML form posts until an AWS WAF challenge after ~40 searches. **Kroll, Stretto, Omni, Verita/KCC** block scripts (403, Incapsula, JS-only). Surge Transportation and US Logistics Solutions have no public claims agent. Helper scripts are in the session scratchpad; the method is in `data/README.md`. |
| **GitHub** | 36 EDI files | Test fixtures of an X12 parser (`spiridonov/baldr`, 2012-13) are genuine carrier interchanges; a 2025-26 extraction benchmark (`e3-solutions/scac-ln-bench`) holds 193 broker-side 210s, of which three TL files were kept (its PDFs are air-courier bills, out of scope). |
| **Carrier sites** | 51 files | Tariffs, 210 guides, claim forms, document-API manuals. SEFL publishes a sample bill whose form fields are named, with no explanations; no other carrier's sample was found. |
| **Government** | 33 files | GAO, GSA OIG, DoD IG, USPS OIG, CBCA decisions, SF 1113, the 2024 rule on protesting a Notice of Overcharge. GSA Form 7925 (the notice itself), the DoD FMR chapter and the DTR Part II chapters refused connections. |
| **Wayback Machine** | 1 file | The CDX index returned 429 all day; the availability API shows **no 2023-24 captures** of the ABF, SEFL, ODFL, XPO or Saia fuel pages, so the weekly fuel level on the real bills cannot be re-checked from archives. One Estes capture (2023-03-27) was kept. |
| Web search for W&I certificates, claim letters, annotated bills | nothing | Blocked by the session's search limit for agent A; agent C's searches found no public W&I certificate image and no public LTL pricing agreement with prices beyond one university page (*assumed*, 404 on fetch). |

## 3. The sets

| Set | What | Files | Pages | Real? |
|---|---|---|---|---|
| 01 `in_holdings_abf` | 101 ABF bills, May-Aug 2024, text layer (Bankr. C.D. Cal. 1:24-bk-11323 Doc 920) | 1 | 129 | real |
| 02 `exist_v_sefl` | **62 distinct SEFL bills** 2020-23 as 2025 past-due reprints, 2023 balance-due prints and 2022-23 corrected invoices (scans with the court's OCR layer), the pricing agreement in 3 dated versions, the pallet table, the accessorial exceptions, and the shipper's 3,645-row overcharge worksheet (S.D. Fla. 1:26-cv-20049 Doc 1-2); page map in the adversarial file §2 | 1 | 224 | real |
| 03 `vital_pharma_xpo` | 6 XPO invoices with VICS BOLs and delivery receipts, a corrected invoice "re-weighed per weight certificate" | 1 | 51 | real |
| 04 `delphi_ups_freight` | ~850 pp of UPS Freight bills, BOLs, DRs 2008-10, 48 of 169 reweighed; OCR in `derived/ocr/` | 11 | 859 | real |
| 05-06 | Yellow delivery receipts; a UPS Freight straight BOL | 2 | 164 | real |
| 07 `hannum_v_yrc_doj` | the DOJ reweigh case: complaints, exhibits, YRC's answers | 7 | 192 | real |
| 08 `overcharge_case_law` | Southern Furniture v. YRC ("180 days is not optional"), Lewis, Mafcote, Gaines, Sivak, Ricks v. Menlo (FCA), Grupp v. DHL | 12 | 404 | real |
| 09 `collection_and_cargo_suits` | carrier-v-shipper, 3PL and broker suits: Estes v. Macy's and v. Coverlex (discount forfeiture), Con-way v. Autosports, YRC v. Royal, ODFL v. Robertshaw, Central Freight v. Amazon (the $2.86M set-off and the freight-audit expert's deposition), Cargo Transportation Services (3PL bankruptcy), detention and lumper narratives | 24 | ~1,000 | real |
| 10 `rate_confirmations_tl` | 12 broker and carrier rate confirmations and load tenders: C.H. Robinson, TQL (2006 and 2025), Coyote, U.S. Xpress, Scotlynn, Landstar, King of Freight, CJ Logistics, Skyway, RMW | 12 | ~150 | real |
| 11 `shipper_carrier_contracts` | YRC-First Brands LTL contract, GM logistics T&Cs, Schneider Logistics MTSA (180-day clauses), Kroger carrier contract (freight-bill payment vendor, Part 378 duplicate-payment clause), CJ Logistics, Surge broker-carrier agreement | 6 | ~170 | real |
| 12 `edi_210_guides` | 14 implementation guides: 3M, Cardinal Glass, Insight (shipper side); ArcBest, Estes, FedEx (4010 and 4060), R+L, TForce (210 and 211), XPO/Con-way | 14 | ~300 | template |
| 13 `rules_tariffs` | 28 tariffs: ABF (3 versions), Estes, FedEx Freight (2), ODFL (2), Saia (2019, 2024, 2025), R+L (2), TForce (2), XPO (4), SEFL, AAA Cooper, Dayton, Central Transport, Landstar, Werner, USA Truck, GSA 200-A and 1000-D | 28 | ~2,700 | template |
| 14 `fuel_tables_and_index` | DOE, GSA, FedEx Freight LTL and TL, the Estes 2023 capture, EIA weekly diesel | 6 | 14 | mixed |
| 15 `bol_forms_and_standards` | Estes VICS BOL, ODFL BOL guide, NMFTA uniform BOL terms, NMFC supplements, NIST HB44 §5.58, NTEP dimensioner certificates | 10 | ~110 | template |
| 16 `claim_forms_and_dispute_letters` | overcharge claim forms: ABF, R+L, Averitt, YRC F-154, FedEx Freight PAP201, XPO process sheet, South Bay; NCWM letters (Heatlines, ABF, XPO, Lynden, NMFTA) | 15 | ~50 | mixed |
| 17 `fap_and_carrier_guides` | Cass carrier guide and FBA tutorial (13 adjustment reasons), U.S. Bank carrier agreement, J&J/CT Logistics guide, ODFL and TForce document APIs, a university RFP, carrier billing pages | 12 | ~260 | template |
| 18 `gov_audit_reports` | GAO (4), GSA OIG (2), DoD IG (2), USPS OIG (2) | 10 | ~290 | real |
| 19 `edi_samples_real` | **36 X12 files** (26 real, 4 assumed real, 1 partly real, 5 templates): 210s from ODFL (8), AAA Cooper (6) and Estes; a partly real Roadway→CTSI file and a UPS template; three batches of TL 210s a freight-payment firm sent to Target (one from TQL, a broker; dairy loads with TONU); 214s from ODFL, SEFL, Holland, R+L and WTVA; 204 tenders to ODFL and SEFL, plus two TL tenders. No SEFL or Holland 210 | 36 | — | mixed |
| 20 `gov_claims_forms_and_decisions` | SF 1113/1113A, the 2024 Notice-of-Overcharge rule, three CBCA rate decisions (ABF 2010 contesting a GSA overcharge), GAO B-261127, DTR App V | 8 | ~60 | mixed |
| 21 `ltl_bills_and_corrections` | ODFL bills with the carrier's audit notes (Paper-Pak, 2007); the Winn-Dixie wrong-payer correction (ODFL); XPO bills to STG with late fees and a reweigh fee; TForce Freight bills; Yellow and K+N statements; ODFL, Estes, Mountain Valley statements; New Penn delivery receipts | 15 | ~590 | real |
| 22 `tl_invoices_and_packets` | **real TL invoices to shippers**: Werner to Instant Brands (66 pp) and to STG (packets: invoice + rate con + BOL), USA Truck to Tupperware via a payment provider, Wintzer per-ton invoices with BOLs, Taylor Truck Line packets, Landstar Ranger (TONU line) and Express, TQL and RXO broker invoices, LEI/Hudson packets with detention time boxes, a 287-page dedicated-fleet contract with fuel table and invoices | 19 | ~900 | real |
| 23 `overcharge_claims_vs_yellow` | shippers' and 3PLs' overcharge claims in Yellow's bankruptcy: nVision claim presentations with YRC's "APPROVED" status printouts (3), GlobalTranz disputes (limited access, TONU, reweigh with the weight certificate), Unishippers claim form, TQL's categorised dispute ledger, Cass's carrier agreement and per-record fees, Home Depot's contract with lane pricing and Walmart's contract, whose lanes appendix is an empty cover page (1,498 pp) | 12 | ~1,700 | real |
| 24 `nemf_interline_and_carrier_claims` | claims in NEMF's bankruptcy: AAA Cooper, Saia (interline agreement with claim deadlines), Covenant, Schneider, Oak Harbor write-off report, Manitoulin dispute letters, a W&I vendor's invoice, ~60 Landstar bills with BOL and POD | 9 | ~250 | real |

Per-set `source.md` files list every file with its case, URL, document types, checks and notes; `data/catalogue.csv` is the machine-readable record (fields in `data/catalogue_fields.md`).

## 4. Found and not found, by the gaps set before round 1

| Gap | Result | Where |
|---|---|---|
| Real TL carrier invoice to a shipper; broker invoice to a shipper | **found** | set 22: Werner (direct to a manufacturer), USA Truck, Wintzer (per-ton + 21% fuel, text layer), Taylor, Autumn, Cornerstone; TQL and RXO broker invoices; packets with rate con + invoice + BOL |
| Detention with timestamps; TONU; layover; lumper | **partly**: priced terms on 8 rate confirmations and agreements; a BOL with in/out detention boxes; a Landstar Ranger invoice line "TRUCK ORDERED NOT USED $250"; a GlobalTranz TONU dispute; TONU lines in three TL 210s; lumper and waiting-time refusals only as narratives | sets 10, 22, 23, 19, 09 |
| Carrier dispute responses, credit memos, re-rated bills | **found**: YRC "APPROVED" printouts on nVision claims; GlobalTranz's decline reason quoted; Winn-Dixie's refund and corrected bill; ODFL's "CORRECT AS BILLED" and reweigh notes; SEFL's 2025 re-bills. **Not found:** a stand-alone credit memo or denial letter, a shipper's Part 378 packet | sets 23, 21, 02 |
| W&I / reweigh certificates | **carrier-issued ones are held**: UPS Freight weight certificates and Freight Inspection Certificates (set 04: 43 weight-certificate and 6 inspection-certificate pages, page-level count), a TForce weight and cube certificate (21-015 pp. 36-37), a Holland W&I weight correction (21-006 p. 15), found by check AW. Also the shipper's weight certificate attached to the GlobalTranz reweigh dispute, and what a carrier pays a W&I vendor (NEMF claim 740) | sets 04, 21, 23, 24 |
| Wrong payer | **found**: Winn-Dixie (collect at class 250 instead of prepaid at class 85), Estes v. Macy's, YRC v. Alliance 3PL, ODFL v. Robertshaw | sets 21, 09 |
| Bill with no matching shipment | **not found** as a document; the DOJ reweigh and FCA cases are the nearest | sets 07, 08 |
| Guaranteed-service refunds | **not found**; only the charge line on ODFL bills | set 21 |
| 3PL / paid-twice proof | pleadings and contract clauses only (Cargo Transportation Services, Kroger's Part 378 duplicate-payment clause, the IN Holdings objection) | sets 09, 11, 01 |
| Real EDI 210 files | **found**, 36 | set 19 |
| Public LTL pricing agreement with prices | **not found** on .gov/.edu; one university page *assumed*. Substitutes: the Home Depot contract with lane pricing in Yellow's claims register (Walmart's lanes appendix is empty); SEFL's three versions; the YRC contract (Schedule C still missing) | sets 23, 02, 11 |
| Historical weekly fuel tables | **not found**: no Wayback captures for 2023-24 (ABF, SEFL, ODFL, XPO, Saia); one Estes 2023 capture | set 14 |
| Later filings in the known cases | Hannum Docs 102, 118 (YRC's side); Central Freight v. Amazon Docs 54, 185, 185-1, 309; Exist v. SEFL later filings not free; Vital Pharmaceuticals' other carrier claims not swept (throttled) | sets 07, 09 |

## 5. Coverage of the 33 checks

Counts of real files evidencing each check after the adversarial corrections (the collectors' own counts, before correction, are in `s5_check_AT_adversarial.md` task 7; where a row was not content-checked, its claim stands):

| Family | Checks: real files |
|---|---|
| A, one real correct bill | A1 math 43 · A2 duplicate 12 · A3 paid via 3PL 10 · A4 corrected bill 14 · A5 wrong payer 14 · A6 no shipment 11 · A7 reference 11 |
| B, priced right | B1 version 7 · B2 discount 48 · B3 minimum 7 · B4 FAK 11 · B5 quote 6 · B6 TL linehaul 25 · B7 mileage 10 · B8 fuel level 49 · B9 fuel base **3** |
| C, weight and class | C1 reweigh/reclass 49 · C2 correction fee 20 |
| D, extras | D1 priced 25 · D2 ordered 7 · D3 detention 24 · D4 stop-off 6 · D5 TONU 6 · D6 layover 9 · D7 lumper 15 |
| E, service | E1 guaranteed refund **1** · E2 service credit 2 |
| F, payment | F1 late fees 18 · F2 GL coding **0** · F3 accrual 1 · F4 rebilled **0** |
| G, deadlines | G1 shipper window 15 · G2 carrier deadline 6 |

Still to come from interviews (AC §9's request list stands): a shipper's own AP export and dispute log, the carrier's certificates for the shipper's own reweighs, a credit memo, the fuel tables in force on the real bills' ship dates, the SMC3 or SEFL base rate tables.

## 6. Are the documents standardised? What is shared and what is per firm

**Shared across firms** (*verified* on the files in sets 12, 15, 16, 19, 20):
- **EDI X12 210 (invoice), 214 (status), 204 (tender).** The segment skeleton (ISA/GS/ST, B3, N1-N4, LX, L5, L0, L1, L7, L3) is the same in every real file. But every carrier maps charges differently: Estes and AAA Cooper write the percentages as text (`L5*1*DISCOUNT 84.0%` with a negative `L1 … DSC` line and "Fuel Surcharge added at 29.00"; "LESS 78.00 PCT DISCOUNT"); ODFL rates in dollars per hundredweight (`L1**93.06*PH*…`; the charge field is in cents for every carrier) with a negative DSC line and fuel on code 405, neither carrying its percentage; AAA Cooper names the base tariff in L7 (`L7*1*CZAR*910`) with the NMFC item; TL carriers bill a flat linehaul (code 400) plus fuel and TONU; versions run 4010, 4030, 4060, and shippers publish their own inbound maps (3M rejects negative amounts; Insight requires a POD segment). Each shipper-carrier pair is a bespoke mapping.
- **The VICS/GS1 bill of lading** form (set 15; filled copies in sets 03, 04, 22), followed loosely, with carrier variants and handwriting.
- **NMFC** item and class numbers on every LTL bill; the FAK clause in agreements refers to them.
- **Government billing**: GBL/CBL, SF 1113, 41 CFR 102-118, and the Notice of Overcharge process (set 20), a standard for one shipper only.
- **Overcharge claims**: 49 CFR Part 378 fixes the content and the carrier's 30- and 60-day clocks; ABF, R+L, Averitt, YRC and South Bay all use the "Standard Form for Presentation of Overcharge Claims" with a bond of indemnity; XPO and Central Transport use their own online forms (set 16).
- **One family of rules**: every rules tariff has the same item classes (minimums, reweigh and reclass fees, accessorials, the 180-day window) and every fuel table keys to the EIA/DOE weekly diesel index with its own bands and effective day (sets 13, 14).

**Per firm** (*verified* on sets 01-04, 21-23):
- **The PDF bill.** No two carriers' bills look alike, and only SEFL publishes a sample (a form with named fields, no explanations). ABF prints the tariff code, deficit weight and rating notes; SEFL's 2020 layout prints "DISCOUNT PERCENTAGE 9100" for 91.00% and its 2023 layout "88.15% DISC", and both price per hundredweight as "60080"; XPO prints one discount line and "M" for a minimum; ODFL prints its own audit lines ("CORRECT AS BILLED", "W & I REWEIGH CORRECTE WEIGHT 1070 LBS"); UPS Freight bills of 2008-10 are mostly scans; Werner bills in two layouts (an all-in linehaul line with no fuel, or freight plus fuel per mile with the miles printed); Wintzer bills per ton. Charge codes differ (ABF MCADJ/SHDL/DETND; XPO LP5/LP6 late fees). Which of ship date, bill date and due date is printed differs.
- **Rate agreements.** SEFL's "rating item" tables (base tariff, discount by route and direction, floor minimum, FAK range, per-pallet rates with exclusions, accessorial exceptions, three dated versions) against the YRC-First Brands 33-article contract, Home Depot's and Walmart's lane-pricing exhibits, GM's T&Cs, Schneider's MTSA. Base tables are proprietary (SEFL-0550) or licensed (CzarLite).
- **TL rate confirmations.** One layout per broker (12 in set 10), with detention, TONU, layover and lumper rules in each broker's own words and prices (TQL 2025: $25-30 an hour after 3-4 hours, layover $250-300, TONU $150 after 2 hours; Coyote: $25 an hour after 2 free hours only if in/out times are on the BOL; U.S. Xpress: $50 an hour after 2 hours).
- **Statements of account** (set 21, 24): per carrier, from a one-page list to K+N's 285-page pro ledger.
- **Claims channels.** A form per carrier; broker windows of 5-30 days against the statutory 180 (AM).
- **The paper trail's shape.** Born-digital carrier PDFs (ABF), scanned and stamped copies once they pass through AP or a 3PL (SEFL, Delphi), faxed bills (ODFL, 2004-08), court-filed claim packets with cover forms, and EDI. The 15 parser traps in `software-initial-pitch.md` §4.3 all appear in this set (several bills per PDF, corrected bills reusing the PRO, per-carrier charge codes, cwt rates, deficit-weight lines, credits in brackets, handwriting, low-quality scans).

## 7. The worked mismatch, with its dispute and the 180-day clock

**Honest framing.** No public set shows a dispute filed and credited inside 180 days with the bill, the agreement and the carrier's answer together. The nearest are (a) the Yellow claims register, where the carrier's "APPROVED" printouts sit on an audit firm's claims (set 23), and (b) *Exist v. SEFL*, the one set with bills, the agreement and the shipper's dispute computation, whose dispute was filed late. The examples below are from (b): each shows the mismatch, the arithmetic, the dispute document and the window as it should have run, with the actual dates beside it. The coordinator transcribed the bills from the page images; the verifier transcribed them again independently, recomputed every figure, and corrected the first version's timing claim (`s5_check_AT_adversarial.md` §2).

**7.0 The exhibit's page map** (verifier, *verified*): pp. 1-11 summons (e-filed 11/10/2025) and the complaint (e-filed 10/07/2025, Miami-Dade case 2025-019705-CA-01; removed and docketed in S.D. Fla. 01/06/2026); pp. 12-14, 15-17, 18-20 the pricing agreement effective 01/15/2021, 06/08/2022 and 04/12/2023; p. 21 the pallet-rate table; p. 22 the accessorial exceptions; **pp. 23-35 thirteen 2023 bills as "PAST DUE INVOICE" reprints dated 08/26/2025; pp. 36-48 the same thirteen as their 2023 "BALANCE DUE INVOICE" prints; pp. 49-62 fourteen 2020 bills in an older layout; pp. 63-97 thirty-five 2022-23 corrected and balance-due invoices** (62 distinct bills); pp. 99-198 the 2021 and 2022 worksheets; pp. 199-211 the 2023 worksheet rows 1-398 (columns: customer, invoice, date, pallets, liftgate, surcharge, freight charge, "need to be charged"); pp. 212-224 its spill column "OVER CHG". Sheet totals $131,987.80 + $109,577.87 + $30,263.03 = $271,828.70, the complaint's claim.

**7.1 Primary example: bill 807148067, one added line with the carrier's reason printed (D2).**
- **The bill** (set 02, p. 33, the 2025 reprint; p. 46, the 2023 balance-due print): Southeastern Freight Lines; shipper Exist Inc., Miami Gardens FL (an SEFL direct point); consignee in Sisters OR (a West Coast Partnership Carrier lane, "WCPC"); **shipment date 05/15/2023**; quote #CWEN3E465; 1 pallet of apparel, NMFC 49880, STC 16 boxes, **class 70.0, 509 lb at $600.80/cwt = 3,058.07; 88.15% discount 2,695.69; net 362.38; LIFTGATE SVC 55.00; PVT RESIDEN 94.00; fuel 22.00% 79.72; total 591.10**; note printed on the bill: "** PER GOOGLE EARTH THIS IS A PRA[IVATE] DLVY". The balance-due print (p. 46) is **dated 06/19/2023, due 07/04/2023, "PAY THIS AMOUNT 94.00"**: the same lines, and the only new money is the residential line.
- **The agreement in force** (version effective 04/12/2023, pp. 19-20): "WCPC OUTBOUND PPD/COL — SEFL-0550 01/10/22 — Item 610 — 88.15 — 70 — 77.5 THRU 175 — ALL"; Item 610 absolute minimum after discount, WCPC (OR) $152.00; accessorial exceptions (p. 22): liftgate $55 to or from partner points; residential delivery is not in the exceptions, so SEFL 1090 governs: Item 753 §4, "$7.60/CWT with a minimum charge of $94.00 and a maximum charge of $575.00 per shipment" (set 13, current tariff; the 2023 value *assumed* the same).
- **What the software finds [our calc]:** math 509 × 6.008 = 3,058.07, × 0.8815 = 2,695.69, net 362.38 ✓ (A1); discount 88.15% = the WCPC outbound row ✓ (B2); class 70 under the FAK ✓ (B4); net above the $152.00 floor ✓ (B3); liftgate $55 on a partner lane ✓ (D1); fuel 22.00% × 362.38 = 79.72, on net linehaul only ✓ (B9); residential 509 lb × $7.60/cwt = $38.68 → the $94.00 minimum ✓ (D1). Every line is priced right. **The flag is D2: does the charge apply?** The bill says the carrier decided it from a satellite image, 35 days after delivery. Item 753 §1 applies the charge whenever the delivery premises is "the entire premises on which a dwelling for living is located"; §2 says the shipper should mark it on the BOL, but omission does not relieve it of the charge. So the dispute turns on one fact, whether a dwelling stands on the consignee's premises. The BOL is evidence of what was ordered, not the deciding document. Cass's reason: "Invalid Accessorial Charge"; FedEx-style routing: "Dispute fee or surcharge".
- **The dispute document the shipper has:** worksheet row 364 (p. 210): `807148067 5/15/2023 1 $55.00 $79.72 $362.38 $152.00`, OVER CHG (p. 223) **$210.38**. The shipper never flagged the $94; it claimed the base freight by the theory in 7.3. What a Part 378 claim would need instead: the balance-due bill, the BOL showing the delivery instructions, the agreement's exceptions page, Item 753, and a statement that the consignee is a business (AK §5.5).
- **The clock [our calc, `python3 -I` datetime]:** balance-due bill 2023-06-19 → the shipper's 180 days to contest (49 U.S.C. 13710(a)(3)(B)) ran to **2023-12-16**, counted from the bill's date (the statute counts from receipt, a few days later); the carrier issued its additional charge 35 days after shipment, inside its own 180 days (13710(a)(3)(A)). The complaint of 2025-10-07 came 661 days after the window closed. *Southern Furniture v. YRC* (set 08): "compliance with the 180-day time limit is not optional."

**7.2 Second example: bill 806625953, a weight raised with no inspection note (C1, A4).** Set 02, p. 28 (2025 reprint) and **p. 41 (balance-due print dated 05/05/2023, due 05/20/2023, "PAY THIS AMOUNT 110.23")**; shipment date 04/19/2023; shipper Exist, Miami Gardens FL; consignee in Duluth MN (MWPC lane); quote #CWDV2BGFC.

| Line as printed | Weight | Rate | Charge |
|---|---|---|---|
| 1 PLT 9 boxes of apparel, CL150 NMFC 49880, rated **CLASS 70.0** | 405 | 31597 ($315.97/cwt) | 1,279.68 |
| 3 PLT 45 boxes of apparel, CL125 NMFC 49880, rated **CLASS 70.0** | 2,315 | 31597 | 7,314.71 |
| GROSS FRT CHG | | | 8,594.39 |
| 90.30% DISC | | | 7,760.73 |
| NET FRT CHG | | | 833.66 |
| LIFTGATE SVC | | | 55.00 |
| LTL FUEL SURCHARGE OF 24.00% | | | 200.08 |
| **TOTAL**, 4 pieces, 2,720 lb | | | **1,088.74** |

| Line as printed | Weight | Rate | Charge |
|---|---|---|---|
| 1 PLT 9 boxes of apparel, CL150 NMFC 49880, rated **CLASS 70.0** | 405 | 31597 ($315.97/cwt) | 1,279.68 |
| 3 PLT 45 boxes of apparel, CL125 NMFC 49880, rated **CLASS 70.0** | 2,315 | 31597 | 7,314.71 |
| GROSS FRT CHG | | | 8,594.39 |
| 90.30% DISC | | | 7,760.73 |
| NET FRT CHG | | | 833.66 |
| LIFTGATE SVC | | | 55.00 |
| LTL FUEL SURCHARGE OF 24.00% | | | 200.08 |
| **TOTAL**, 4 pieces, 2,720 lb | | | **1,088.74** |

- **The agreement in force** (version effective 04/12/2023, pp. 19-20): "MWPC OUTBOUND PPD/COL — SEFL-0550 01/10/22 — Item 610 — 90.30 — 70 — 77.5 THRU 175 — ALL. Apply FAK exception class 70.0 on commodities described in NMFC class 077.5 thru 175.0." Item 610 MWPC absolute minimum $127.50; liftgate $55 to partner points (p. 22).
- **The checks [our calc]:** math 405 × 3.1597 = 1,279.68 and 2,315 × 3.1597 = 7,314.71, sum 8,594.39, × 0.9030 = 7,760.73, net 833.66 ✓ (A1); discount 90.30% = the MWPC outbound row ✓ (B2); classes 150 and 125 inside 77.5-175, FAK 70 ✓ (B4); net above $127.50 ✓ (B3); liftgate $55 ✓ (D1); fuel 24.00% × 833.66 = 200.08 on net only ✓ (B9); fuel level 24.00% for the week of 2023-04-17 **not checkable**, SEFL's 2023 table is not public and no archive capture exists (B8, §4). Every line is consistent with the agreement.
- **The mismatch.** The shipper's worksheet row 292 (p. 208; OVER CHG p. 221) records the same invoice from its copy of the **original** bill: liftgate $55.00, surcharge **$178.74**, freight **$744.77**, total $978.51; 178.74 / 744.77 = 24.0%, the same fuel week. The balance-due bill charges net **$833.66** and fuel $200.08, total $1,088.74, and asks for the difference, **$110.23 (+11.3%)**; same discount, same fuel rate, same liftgate, so only the gross changed: 744.77 / 0.097 = $7,678.04 gross, which at $315.97/cwt is **2,430.0 lb** against the **2,720 lb** on the re-rated bill [our calc; the verifier reproduced every figure]. Reading: a weight increase of 290 lb, billed 16 days after shipment, with **no reweigh, W&I or inspection note on either print** (compare p. 35, which prints "** CLASS INSPECTION PER W&I **" when an inspection was done).
- **Discrepancy types:** C1, a weight change without the certificate referenced; A4, a balance-due bill the shipper never reconciled to the original. Cass's reasons: "Weight Incorrect", "Reversed Balance Due"; FedEx-style routing: "Reweigh review".
- **The dispute document the shipper has:** worksheet row 292 (4 pallets, the three charge columns, "NEED TO BE CHG" $510.00, "OVER CHG" $234.77) and the complaint's allegations of "double invoices and … erroneous billings". What a Part 378 claim would need instead: the original and the balance-due bill side by side, the BOL weight, a request for the weight certificate, the agreement row, the dates (AK §5.5).
- **The clock [our calc]:** balance-due bill 2023-05-05 → the shipper's 180 days ran to **2023-11-01**; the carrier's own additional charge came 16 days after shipment, inside its 180 days. The complaint of 2025-10-07 is 706 days after the window closed. The 2025-08-26 document on p. 28 is a "past due" reprint of the unpaid $110.23, printed six weeks before the suit, not a new bill: the first draft of this section read it as a re-bill 22 months late, and the verifier's find of p. 41 corrected that.
- **Caveats.** The original invoice image is not in the exhibit; its amounts come from the shipper's worksheet (a party document, *assumed*). Nothing in the file says whether a reweigh happened; "no inspection note" is an absence on two prints.

**7.3 Why the shipper's $271,829 claim is overstated, and what the software must not do.** On every 2023 row the verifier tested, "NEED TO BE CHG" equals **the pallet count × the Item 610 absolute minimum for the partner zone**: row 292, 4 × $127.50 (MWPC) = $510.00; row 364, 1 × $152.00 (WCPC, Oregon) = $152.00; row 323, 4 × $130.50 (NEPC) = $522.00; rows 396 and 398, 1 × and 2 × $127.50. But Item 610 is "the absolute minimum charge after application of discount" per shipment (p. 20), not a per-pallet rate, and the per-pallet rates (pp. 18, 21) exist only for SEFL-direct states and Florida. On partner lanes the worksheet's "overcharge" is just the gap between the discounted class rate and pallets × minimum, and it misses the one line the carrier added without an order (the $94 in 7.1). Check AC's caution about this worksheet is now explained (the shipper's own rationale is not in the record; this is our reading). A look-back that reproduced it would lose the carrier's trust at the first claim.

**7.4 Other instances in the same exhibit (verifier, *verified*).**
- **A correction with its proof cited (C1, D2, parser trap 7).** p. 35 and p. 48, bill 807307041, shipped 05/22/2023 to Michigan: two pallets declared CL-175 and CL-125, rated class 70 under the FAK; "AS WEIGHT 1000 / DEFICIT 90 lb" (rated up to the 1,000-lb break); "** CLASS INSPECTION PER W&I **"; "REDELIVERY 80.00" with "ORIG DEL ATTEMPT: 05/25/2023" printed; net 291.79, total 489.52. The shipper's original shows net 338.47 and no redelivery (total 466.24); the balance-due bill of 06/22/2023 asks $23.28: the inspection *lowered* the freight and the $80 redelivery (the agreement's exception price, p. 22) was added. The shipper claims $83.47 by the pallets × minimum theory.
- **Cubic-capacity minimums with the rule cited on the bill (B3).** pp. 24-26 and 37-39, bills 806373725, 806445173 and 806446820: "APPLY SEFL 1090-B ITEM 610-100 816.54 CF / 5.41 PCF AW=4420 CW=4899 / MIN FRT CHG 2014.40" and the like; the density rule re-rates a 4,656-lb shipment at 5,188.8 lb. Discounts 88.15 and 90.30 as the agreement says; the only open question is the cube measurement. (The practice audit's OCR had read these bills' discount amounts, $38,705.48 and so on, as discounts of "3870", "1618", "1875".)
- **A late-payment penalty (F1) and a bill before the earliest agreement held (B1).** p. 49, bill 882437984, shipped 03/11/2020 under the older account: "***** PENALTY/TARIFF DUE ***** $161.89", "DISCOUNT PERCENTAGE 9100" for 91.00%; the 2020 agreement is not in the file.
**7.5 Instances in other sets, one paragraph each.**
- **A carrier-initiated reweigh with the certificate referenced (C1, A4).** Set 03: XPO's corrected invoice "RE-WEIGHED PER WEIGHT CERTIFICATE" with a reweigh fee; the shipper's 180 days run from the corrected bill.
- **A wrong-payer error corrected end to end (A5, A4).** Set 21, Winn-Dixie: the BOL marked collect at class 250 instead of prepaid at class 85; ODFL refunded $2,412.67 and re-billed the vendor $1,133.55 with a $15 corrected-BOL charge and the note "change charges to prepaid 3rd party per letter from the shipper" (agent A, *verified*, pages in the adversarial file).
- **A shipper's claim approved by the carrier (the dispute side).** Set 23: nVision's overcharge presentations to YRC with YRC's "APPROVED" status printouts; GlobalTranz's reweigh dispute with the shipper's weight certificate attached and the carrier's decline reason quoted on another.
- **Downward reweighs never credited (government).** Set 07: the relator's two bills (declared 4,310 lb against a scale weight of 3,345 lb, $222.84; 620 against 220 lb, $133.23) in a case of 75,324 upward reweighs against 42 downward; the government's window is 3 years under 31 U.S.C. 3726, not 180 days.

## 8. For the prototype, and open points

**Parse order [our call]:** set 01 (ABF, text layer, 101 bills) for the reader and the checks; set 19 (real 210s) for the data path, with set 12's guides as the per-carrier maps; set 02 (SEFL) for OCR, agreement matching, the three versions and balance-due reconciliation (13 bills appear as both the 2023 balance-due print and the 2025 reprint); set 22 (Werner, Taylor packets) for TL: rate con → invoice → BOL linking; set 21 (ODFL with audit notes, Winn-Dixie) for corrected-bill handling; set 23 for what a claim and a carrier's answer look like; set 10 for broker rate-confirmation layouts.

**OCR quality to expect (verifier, tesseract 5 at 200 dpi):** on the SEFL bills, 17 of 20 total-line amounts read right (17 of 18 on the modern layout; the 2020 layout without a "TOTAL" label failed), but weights were often wrong (1,775 read as 4,775); on the Delphi UPS Freight scans 5 of 5 totals right with 3 line-item errors in about 17. So: totals on clean carrier layouts are reliable; line items, weights and hand-annotated pages need a second read (the text layer, or a higher-resolution re-OCR of the amount column), which is the pitch's "two independent readings agree" rule.

**Open for the founders (not decided here):**
1. Whether to buy from PACER the exhibits that would close the remaining gaps: Estes v. Coverlex Doc 19-1 (a pricing agreement, a 2,498-bill list and discount-forfeiture exemplars), Estes v. Whatman Docs 1-1 and 9-5 (sample BOL, invoice, past-due warning), Central Freight v. Amazon Doc 1-1 (Amazon's audit demand letter), Exist v. SEFL's 2026-02-12 order, Hannum Doc 72-3.
2. Whether copyrighted carrier tariffs and guides stay inside `data/` (kept for research) or are linked only.
3. Whether to split the multi-bill court PDFs into one file per bill now (derived, not catalogued) or leave it to the prototype's page sorter.
4. A re-try of the Wayback CDX index on another day for the fuel pages, and of the throttled CourtListener queries (Vital Pharmaceuticals' other carrier claims, Winn-Dixie's carrier claims).

## 9. Sources

All 271 files are listed with their URLs in `data/catalogue.csv` and per set in `data/sources/<set>/source.md`; the agents' findings notes and claim ledgers are in the session scratchpad (`dl_A/findings_A.md`, `dl_B/findings_B.md`, `dl_C/findings_C.md`) and their load-bearing claims are repeated in §11. Statute: 49 U.S.C. 13710(a)(3) (A: the carrier's 180 days to bill additional charges; B: the shipper's 180 days to contest); 49 CFR Part 378; 31 U.S.C. 3726. Case: *Southern Furniture Leasing v. YRC*, 10th Cir. No. 19-3262 (2021-03-03), set 08.

## 10. Could not access, or not found

- **PACER-only exhibits** (free RECAP copies absent): Estes v. Coverlex Doc 19-1; Estes v. Whatman Docs 1-1, 9-5, 19-5; Central Freight v. Amazon Doc 1-1; Transport Systems v. Amazon Doc 1; Hannum Doc 72-3; Exist v. SEFL filings after Doc 1; Surge v. Mondelez; Coyote v. Jusda and Landstar v. Urban Roads (broker-to-shipper invoices).
- **Too large:** Lewis v. YRC Doc 63-1 (165 pp, over the 25 MB cap); the R+L v. Qualcomm Federal Circuit joint appendix (450 pp, surfaced on the W&I query, not fetched).
- **Blocked registers:** Kroll (403), Stretto (Incapsula), Omni (403), Verita/KCC (TLS chain and JavaScript only); Angeion after ~40 searches (AWS WAF).
- **Blocked government files:** GSA Form 7925 (the Notice of Overcharge), DoD FMR vol. 10 ch. 13, DTR Part II chapters (ustranscom.mil refuses), DFAS 1998 instructions.
- **Wayback:** CDX 429 all day; no 2023-24 captures of the ABF, SEFL, ODFL, XPO or Saia fuel pages per the availability API.
- **Not found anywhere public:** a stand-alone credit memo or denial letter; a shipper's Part 378 packet; a bill for a shipment that never moved; a guaranteed-service refund instance; any public LTL pricing agreement with its prices on a .gov or .edu site; carrier-published 210 guides for SEFL, ODFL, Saia, Averitt, Dayton, AAA Cooper, Pitt Ohio, Central Transport; an explained sample bill from any carrier (SEFL's sample has named fields only); a quote document; a shipper-facing TL rate confirmation (all held are broker-to-carrier); LTL claims from R+L, Averitt, Dayton, Pitt Ohio, Central Transport or FedEx Freight in any reachable register.
- **Throttled, not run:** 11 CourtListener queries (the Vital Pharmaceuticals proof-of-claim sweep, Winn-Dixie's carrier claims, TL-carrier and GBL queries); agent A's 15 web-side searches.

## 11. Claim ledger

| ID | Claim | Source | Label | Where |
|---|---|---|---|---|
| AT-01 | SEFL bill 806625953 (shipped 2023-04-19): 2,720 lb, net 833.66, total 1,088.74; p. 41 is its "BALANCE DUE INVOICE" dated 05/05/2023 for $110.23; p. 28 the "PAST DUE INVOICE" reprint dated 08/26/2025 | set 02 pp. 28, 41 | *verified* (both read from images; verifier) | §7.2 |
| AT-02 | The shipper's worksheet row 292 for the same invoice shows freight 744.77, surcharge 178.74, liftgate 55.00, need 510.00, over 234.77 | set 02 pp. 208, 221 (text layer) | *verified* | §7.2 |
| AT-03 | Agreement v3 (eff. 04/12/2023): MWPC outbound 90.30% discount, FAK 70 for NMFC 77.5-175, Item 610 MWPC minimum $127.50; WCPC outbound 88.15%, Oregon minimum $152.00; NEPC minimum $130.50 | set 02 pp. 19-20 (render and OCR) | *verified* | §7.1-7.3 |
| AT-04 | "NEED TO BE CHG" = pallets × Item 610 minimum on rows 292, 323, 364, 396, 398 | set 02 pp. 199-211, 212-224 | *verified* [our calc, verifier] | §7.3 |
| AT-05 | Bill 807148067: 509 lb at 600.80/cwt, 88.15% discount, net 362.38, liftgate 55, residential 94, fuel 22% 79.72, total 591.10, "per Google Earth this is a private delivery"; p. 46 is its balance-due bill of 06/19/2023 for $94.00; worksheet row 364 claims $210.38 | set 02 pp. 33, 46, 210, 223 | *verified* (verifier) | §7.1 |
| AT-06 | SEFL 1090 Item 753: residential $7.60/cwt, minimum $94.00, maximum $575; §1 applies it to the entire premises on which a dwelling stands; §2: the shipper should mark the BOL, but omission does not relieve it of the charge | set 13, derived text | *verified* (the item is dated 2022-12-16, so in force for the 2023 bill) | §7.1 |
| AT-07 | Bill 807307041 prints "** CLASS INSPECTION PER W&I **", "REDELIVERY 80.00", "ORIG DEL ATTEMPT: 05/25/2023", deficit weight to 1,000 lb; p. 48 balance due $23.28 dated 06/22/2023 | set 02 pp. 35, 48 | *verified* | §7.4 |
| AT-07a | The complaint was e-filed 10/07/2025 (p. 5); p. 1 is the summons of 11/10/2025; pp. 23-35 are 2025 reprints, pp. 36-48 the 2023 balance-due prints of the same 13 bills, pp. 49-62 fourteen 2020 bills, pp. 63-97 thirty-five 2022-23 corrected bills: 62 distinct bills (13 + 14 + 35, recounted from the page headers by check AV's review) | set 02 | *verified* (verifier) | §7.0 |
| AT-08 | Real carrier 210s: Estes `L5*1*DISCOUNT 84.0%` with a negative DSC L1; ODFL `L1**93.06*PH*…` plus a negative DSC line and fuel on 405; AAA Cooper `L7*1*CZAR*910` | set 19 | *verified* | §6 |
| AT-09 | ODFL bills in Paper-Pak carry "FREIGHT BILL AUDIT", "CORRECT AS BILLED", "REWEIGH CORRECTED WEIGHT 1070 LBS", "SPEED SERVICE -- GUARANTEED 78.77" | set 21, pp. 8-13 (OCR) | *verified* by agent A | §4 |
| AT-10 | Winn-Dixie Doc 6929: BOL "Freight Collect at class 250" instead of prepaid class 85; ODFL refunded $2,412.67 and re-billed $1,133.55 with a $15 corrected-BOL charge | set 21, p. 17 | *verified* by agent A | §7.7 |
| AT-11 | TQL 2025 rate con: detention $25-30/h after 3 h by appointment or 4 h first-come; layover max $250/$300; TONU $150 after 2 h; lumper receipts within 5 business days | set 10, pp. 13-14, 20 | *verified* by agent A | §6 |
| AT-12 | Landstar Ranger invoice line "TRUCK ORDERED NOT USED $250"; GlobalTranz TONU and reweigh disputes with a weight certificate; YRC "APPROVED" printouts on nVision claims | set 22, set 23 | *verified* by agent B (pages in the adversarial file) | §4 |
| AT-13 | Werner TL invoices direct to a manufacturer; Werner and Taylor packets of invoice + rate con + BOL; TQL and RXO broker invoices to a shipper | set 22 | *verified* by agent B | §4 |
| AT-14 | Epiq's register answers a JSON search and serves claim PDFs by document id; Kroll, Stretto, Omni and Verita block scripts | agent B leads log | *verified* (this session) | §2 |
| AT-15 | The Wayback availability API shows no captures of the ABF, SEFL, ODFL, XPO or Saia fuel pages for the probed 2022-24 dates; one Estes capture of 2023-03-27 | `data/leads_tried.csv`; set 14 | *verified* (this session) | §2 |
| AT-16 | Schneider Logistics MTSA: overcharge and undercharge claims within 180 days of receipt of the shipment; invoices may be refused if received 180+ days after delivery | set 11, p. 6 | *verified* by agent A | §6 |
| AT-17 | Con-way BOL ¶9: additional charges billed, and disputes raised, within 180 days of the original bill | set 09, Con-way v. Autosports opinion | *verified* by agent A | §6 |
| AT-18 | Amazon's freight-audit expert re-rates each bill from the BOL, delivery receipt, inspection and weight certificates, reconsignment letters and tariffs, then files an overcharge claim | set 09, Doc 185-1 pp. 35-41 | *verified* by agent A | §4 |

## 12. Coincidence watch

- The first draft of §7 read the "DATE BILLED 08/26/2025" on p. 28 as a re-bill 22 months late. It was a reprint; the balance-due bill of 2023-05-05 on p. 41 carried the same figures. The lesson for the software is the same one the pitch already states: a corrected or balance-due bill must be matched to its original and to every later print of itself before any date arithmetic is done (parser trap 4).
- Bill 807148067 was first offered as a "no-flag control". It is not: the $94 residential line was added on a balance-due bill the shipper never noticed. A bill that reconciles to the agreement line by line can still carry one unordered charge.
- Agent C's claim that the "Standard Form for Presentation of Overcharge Claims" is near-universal rests on five carriers' forms; XPO and Central Transport already differ.
- The coverage counts in §5 come from the collectors' own `discrepancy_checks` tags, which are generous for tariffs and guides; the real-file counts are the ones to trust, and the verifier's corrected matrix supersedes them.
