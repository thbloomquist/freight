# data/ — the public document dataset for the C-09 prototype

Built 2026-10-09 (check AT: `research/s5_check_AT_c09_document_dataset.md`; verification: `research/s5_check_AT_adversarial.md`). **271 files, 24 sets, 10,474 pages, 438 MB.** 188 are real documents (after the adversarial corrections) from actual shipments, contracts or disputes; the rest are guides, tariffs, forms and specifications.

## What this is, and is not
- **Public records only.** Court filings (free RECAP copies of PACER documents), bankruptcy claims registers, carrier and government sites, GitHub test fixtures, one Wayback capture. Nothing here is under NDA. Real customer data from interviews or look-backs never goes in this folder (decision D-18): it stays in `~/Documents/personal/bio/freight_private/` and is deleted after the assessment.
- **Companies, not people.** The catalogue and notes name companies only. The raw files are public records and may contain individuals' names, signatures and phone numbers; do not transcribe them anywhere in the project.
- **Copyright.** Carrier tariffs, EDI guides and claim forms are kept for research. Whether they stay here or are linked only is an open point for the founders (AT §8).

## Layout
```
catalogue.csv          one row per file under sources/  (fields: catalogue_fields.md)
SHA256SUMS             sha256sum -c SHA256SUMS
leads_tried.csv        every query, register lookup and candidate URL tried by the three collectors (383 rows: 206 hits, 125 misses, 51 blocked)
sources/<NN>_<set>/    the files + source.md (one line per file: case, document types, checks evidenced, URL, notes)
derived/text/<set>/    pdftotext -layout output for every file with a text layer (regenerable, not hashed)
derived/ocr/04_…/      tesseract output for the Delphi set (copied from the 2026-09-22 session)
_tools/tessdata/       eng.traineddata, so `tesseract <png> - --tessdata-dir data/_tools/tessdata --psm 6` works
verify_rows.csv        the verifier's per-row verdicts and corrections (applied to catalogue.csv; report in research/s5_check_AT_adversarial.md)
doc-explanation.md     the document chain behind a price dispute, form by form: purpose, shared or per-firm format, role in the worked SEFL mismatch, what is held, what is missing and its cost; §4 is the dispute pipeline (what to pull from each document, in what order, and the math that decides a dispute)
```

## The sets, in one line each
| Set | Contents |
|---|---|
| 01 `in_holdings_abf` | 101 ABF bills, May-Aug 2024, text layer (the practice-audit set) |
| 02 `exist_v_sefl` | 62 distinct SEFL bills 2020-23 as reprints, balance-due and corrected prints (scans), the pricing agreement in 3 dated versions, the shipper's 3,645-row overcharge worksheet: **the dispute set** |
| 03 `vital_pharma_xpo` | 6 XPO invoices with BOLs and delivery receipts, a reweigh correction |
| 04 `delphi_ups_freight` | ~850 pp of UPS Freight bills, BOLs, DRs (2008-10), 48 of 169 reweighed; OCR in derived/ |
| 05, 06 | Yellow delivery receipts; a UPS Freight straight BOL |
| 07 `hannum_v_yrc_doj` | the DOJ reweigh fraud case, both sides |
| 08 `overcharge_case_law` | the 180-day cases (Southern Furniture v. YRC), discount-forfeiture and FCA opinions |
| 09 `collection_and_cargo_suits` | carrier-v-shipper, 3PL and broker suits; Central Freight v. Amazon (audit set-off, expert deposition); detention and lumper disputes |
| 10 `rate_confirmations_tl` | 12 broker and carrier rate confirmations and load tenders (CHR, TQL, Coyote, U.S. Xpress, Scotlynn, Landstar, …) |
| 11 `shipper_carrier_contracts` | YRC-First Brands, GM, Schneider Logistics, Kroger, CJ Logistics, Surge broker-carrier agreement |
| 12 `edi_210_guides` | 14 X12 210/211 implementation guides, carrier and shipper side |
| 13 `rules_tariffs` | 28 rules tariffs from 16 carriers and GSA, several in dated versions |
| 14 `fuel_tables_and_index` | DOE, GSA, FedEx Freight LTL and TL fuel tables, one Estes 2023 capture, the EIA weekly diesel series |
| 15 `bol_forms_and_standards` | VICS BOL, uniform BOL terms, NMFC supplements, NIST HB44 §5.58, NTEP dimensioner certificates |
| 16 `claim_forms_and_dispute_letters` | overcharge claim forms from 7 carriers; NCWM letters on reweigh rules (incl. a small importer's account) |
| 17 `fap_and_carrier_guides` | Cass and U.S. Bank carrier material (13 adjustment reasons), document APIs, a university RFP, carrier billing pages |
| 18 `gov_audit_reports` | GAO, GSA OIG, DoD IG, USPS OIG transportation audits |
| 19 `edi_samples_real` | **36 X12 files** (26 real, 4 assumed real, 1 partly real, 5 templates): 210 invoices from ODFL, AAA Cooper, Estes, and TL 210s a freight-payment firm sent to Target (one batch from TQL, a broker); 214s from Holland, ODFL, SEFL, R+L and WTVA; 204 tenders. No SEFL or Holland 210 |
| 20 `gov_claims_forms_and_decisions` | SF 1113, the Notice-of-Overcharge rule, CBCA and GAO rate decisions |
| 21 `ltl_bills_and_corrections` | ODFL bills with the carrier's audit notes, a wrong-payer correction end to end, XPO and TForce bills, statements of account, PODs |
| 22 `tl_invoices_and_packets` | **real TL invoices to shippers** (Werner, USA Truck, Wintzer, Taylor, …), broker invoices (TQL, RXO), packets of rate con + invoice + BOL, a TONU line |
| 23 `overcharge_claims_vs_yellow` | shippers' and 3PLs' overcharge claims in Yellow's bankruptcy with the carrier's "APPROVED" printouts, a reweigh dispute with the weight certificate, Home Depot's contract with lane pricing and Walmart's contract (its lanes appendix is empty) |
| 24 `nemf_interline_and_carrier_claims` | carrier claims in NEMF's bankruptcy: interline statements, Saia's interline agreement, a dispute correspondence, a W&I vendor's invoice |

## Are freight bills standardised? (short answer; AT §6 has the evidence)
Shared across firms: the EDI X12 210/214/204 skeleton, the VICS/GS1 bill-of-lading form, NMFC classes, Part 378's claim content and the "Standard Form for Presentation of Overcharge Claims". Per firm: every carrier's PDF bill layout and charge codes, its mapping of the 210 (Estes writes the discount as text and a negative line, ODFL as a negative line only with no percentage on discount or fuel, AAA Cooper names the base tariff), its rules tariff, its fuel table and its claim channel; every rate agreement; every broker's rate confirmation. Build for one standard data path and many per-firm readers.

## The worked mismatch (AT §7)
SEFL bill 807148067 (set 02, pp. 33 and 46): shipped 2023-05-15; 35 days later a $94.00 balance-due bill added one line, "PVT RESIDEN 94.00", with the carrier's reason printed on it ("per Google Earth this is a private delivery"). Every other line that the agreement prices reconciles to it (the gross rate and the fuel % cannot be checked without the base tariff and the 2023 fuel table); the one question is whether a dwelling stands on the delivery premises. SEFL 1090 Item 753 applies the charge to "the entire premises on which a dwelling for living is located", and leaving residential off the BOL "will not relieve" the shipper of it, so the BOL is evidence, not the deciding document (`doc-explanation.md` §1.1-§1.2; 9 of the 62 SEFL bills carry a residential line). The shipper's 180 days ran to 2023-12-16 at the earliest (the clock runs from receipt); its worksheet never flagged the $94 and the suit came in October 2025. Second example, bill 806625953 (pp. 28 and 41): a balance-due bill of 2023-05-05 for $110.23 that raised the weight from 2,430 to 2,720 lb with no inspection note. The shipper's own worksheet multiplies pallets by the per-shipment minimum charge, which is why its $271,829 claim is overstated. Page map and the independent re-transcription: `research/s5_check_AT_adversarial.md` §2.

## How the registers were reached (for the next round)
- **CourtListener:** `https://www.courtlistener.com/api/rest/v4/search/?type=r&available_only=on&q=…` (anonymous, 5 a minute, 50 an hour); PDFs at `storage.courtlistener.com/recap/gov.uscourts.<court>.<id>/…pdf`.
- **Epiq:** POST `https://dm.epiq11.com/api/search/getcards` (type CasesClaims, filter projectCode: YRC = Yellow, INB = Instant Brands, TLP = Tupperware, TUE = Tuesday Morning, SLQ = STG Logistics); claim PDFs by GET at `https://document.epiq11.com/document/getdocumentbycode?docId=<id>&projectCode=<code>&source=DM` (HEAD returns 405).
- **Angeion / Donlin Recano (NEMF):** HTML POST claimant search, then `/Clients/nemf/GetClaim?claimNumber=N` (redirects to signed S3; HEAD returns 403; a WAF challenge appears after about 40 searches).
- **Blocked to scripts:** Kroll, Stretto, Omni, Verita/KCC; Wayback's CDX index (429 all day on 2026-10-09).

## Known, not kept
Bankruptcy statement-of-financial-affairs payment lists (about 90 PDFs used for spend figures in checks AD, AN, S3a); the Miami-Dade freight-audit contract (AS); a Miller v. Costco deposition and a Vital Pharmaceuticals sale order (downloaded earlier, not freight documents); GSA freight-audit price lists (AN). Their URLs are in those research files.

## Verify
```
cd data && sha256sum -c SHA256SUMS | grep -v ': OK'
python3 -I -c "import csv;print(sum(1 for _ in csv.DictReader(open('catalogue.csv'))))"; find sources -type f ! -name source.md | wc -l
```
Both counts must match (271). Rows carry `verify_status` from the adversarial pass (145 verified, 123 narrowed, 3 wrong, all corrections applied); 5 rows still carry `UNRESOLVED` in `url` (the file came from an earlier session and its canonical URL was not found). HEAD checks on 2026-10-09: 250 of 261 URLs answer 200; the claims agents, GAO and NMFTA refuse HEAD requests from scripts but serve GET; two links are dead (the Estes 210 guide moved; the Mitsui v. Roadway RECAP path is unconfirmed).
