# data/ — the public document dataset for the C-09 prototype

Built 2026-10-09 (check AT: `research/s5_check_AT_c09_document_dataset.md`; verification: `research/s5_check_AT_adversarial.md`) and extended 2026-10-21 (check BE: `research/s5_check_BE_c09_new_document_channels.md`; verification: `research/s5_check_BE_adversarial.md`). **658 files, 27 sets, 12,402 pages, 864 MB.** Five archived tariff editions were added on 2026-10-20; check BE added 382 files (sets 25-27 and closers in sets 09, 13-16, 19, 21, 23). About 548 are real documents from actual shipments, contracts, payments or disputes; the rest are guides, tariffs, forms and specifications.

## What this is, and is not
- **Public records only.** Court filings (free RECAP copies of PACER documents), bankruptcy claims registers and their dockets, carrier and government sites, GitHub test fixtures, Wayback captures, litigation-discovery productions published by the UCSF Industry Documents Library (set 25), tribunal and board decisions (set 26) and open-data payment ledgers (set 27). Nothing here is under NDA. Real customer data from interviews or look-backs never goes in this folder (decision D-18): it stays in `~/Documents/personal/bio/freight_private/` and is deleted after the assessment.
- **Companies, not people.** The catalogue, notes and case cards name companies only; tribunal cases with an individual party are cited by neutral citation. The raw files are public records and may contain individuals' names, signatures and phone numbers; do not transcribe them anywhere in the project.
- **Set 25 (IDL) privacy rules (founders, 2026-10-21).** Originals are kept as published; their stripped CSVs (person and address columns dropped, e-mails blanked; rules in `derived/idl/STRIPPED.md`) are in `derived/idl/`, which is not in git and is regenerated with `_tools/idl_strip.py`. Five JUUL–DCL workbooks hold consumers' names, addresses and phones, so `data/` holds only a zip of their stripped CSVs (`*__stripped.zip`) and the originals are in `~/Documents/personal/bio/freight_private/idl_originals/`. Rights stay with the producing companies; IDL publishes under court agreements or fair use with a takedown policy (*assumed*, BE §8 item 7).
- **Redacted copy.** 19-046 (a Kraft 204) had a staff e-mail and phone in two NTE segments, replaced by `[REDACTED]`; the original's SHA-256 is in its row.
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
doc-exploration.md     the same chain cut per fact (2026-10-10; validated cell by cell by checks AZ-BC, 2026-10-18): the 88 facts a dispute needs, where each lives with its fallbacks, what NOT REPORTED means and does to the 180-day clocks, six real chains from sources/ walked fact by fact, and the founders' decisions of 2026-10-20 (§9)
open-questions.md      the ten customer-interview questions that decide C-09 (from chat, 2026-10-09), with what each one decides
answer_keys/           30 case cards from set 26 (check BE): each decision's facts mapped to the fact IDs, what the method lacks, the true outcome with a quoted reason; expected_verdict TBD (founders). They are answer keys: a blind run gets a whited-out decision, never the card
derived/idl/           stripped CSVs of set 25's spreadsheets (not in git; regenerate: python3 _tools/idl_strip.py sources/25_idl_shipper_freight_files derived/idl <B2C ids>; needs openpyxl, xlrd)
_tools/idl_strip.py    the stripping script (rules in derived/idl/STRIPPED.md)
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
| 09 `collection_and_cargo_suits` | carrier-v-shipper, 3PL and broker suits (BE added the later rulings: Estes v. Coverlex's $1.83M forfeiture judgment, Central Freight v. Amazon's verdict and dismissal, Transport Systems v. Amazon); Central Freight v. Amazon (audit set-off, expert deposition); detention and lumper disputes |
| 10 `rate_confirmations_tl` | 12 broker and carrier rate confirmations and load tenders (CHR, TQL, Coyote, U.S. Xpress, Scotlynn, Landstar, …) |
| 11 `shipper_carrier_contracts` | YRC-First Brands, GM, Schneider Logistics, Kroger, CJ Logistics, Surge broker-carrier agreement |
| 12 `edi_210_guides` | 14 X12 210/211 implementation guides, carrier and shipper side |
| 13 `rules_tariffs` | 34 rules tariff files from 16 carriers and GSA (XPO CNWY 199-AI.2 of 2024 added by BE), several in dated versions, including five archived editions from the Wayback Machine (added 2026-10-20): ABF 111-AR of 2023, SEFL 1090 of March 2021 and as of April 2024, SEFL Item 753 in its 2021 and 2022 wording |
| 14 `fuel_tables_and_index` | DOE, GSA, FedEx Freight LTL and TL fuel tables, one Estes 2023 capture, the EIA weekly diesel series; from BE, ODFL's fuel master tariffs 128-AA/BB/CC (in force 2022-06-01 to date) and Yellow Tariff 100 Items 700/703/705 (2022) with its last fuel page (2023-07-12) |
| 15 `bol_forms_and_standards` | VICS BOL, uniform BOL terms, NMFC supplements, NIST HB44 §5.58, NTEP dimensioner certificates |
| 16 `claim_forms_and_dispute_letters` | overcharge claim forms from 7 carriers; NCWM letters on reweigh rules (incl. a small importer's account) |
| 17 `fap_and_carrier_guides` | Cass and U.S. Bank carrier material (13 adjustment reasons), document APIs, a university RFP, carrier billing pages |
| 18 `gov_audit_reports` | GAO, GSA OIG, DoD IG, USPS OIG transportation audits |
| 19 `edi_samples_real` | **48 X12 files** (12 added by BE from a GitHub parser's test folder: production RASY TL 210s, ACDT 210s, a Kraft 204 → RASY 214 pickup chain, a 204 original/cancel pair, a 990; repo unlicensed, kept for research; 19-046 redacted). The first 36: (26 real, 4 assumed real, 1 partly real, 5 templates): 210 invoices from ODFL, AAA Cooper, Estes, and TL 210s a freight-payment firm sent to Target (one batch from TQL, a broker); 214s from Holland, ODFL, SEFL, R+L and WTVA; 204 tenders. No SEFL or Holland 210 |
| 20 `gov_claims_forms_and_decisions` | SF 1113, the Notice-of-Overcharge rule, CBCA and GAO rate decisions |
| 21 `ltl_bills_and_corrections` | ODFL bills with the carrier's audit notes, a wrong-payer correction end to end, later bankruptcy dispositions of held claims (BE: Mode, TForce Freight, two Winn-Dixie docket entries that are Case 2's outcome; keep them from a blind run), XPO and TForce bills, statements of account, PODs |
| 22 `tl_invoices_and_packets` | **real TL invoices to shippers** (Werner, USA Truck, Wintzer, Taylor, …), broker invoices (TQL, RXO), packets of rate con + invoice + BOL, a TONU line |
| 23 `overcharge_claims_vs_yellow` | shippers' and 3PLs' overcharge claims in Yellow's bankruptcy, with (from BE) their withdrawals, the omnibus objections and orders that re-assigned them, and four preference complaints listing Yellow's payments to audit firms and brokers; with the carrier's "APPROVED" printouts, a reweigh dispute with the weight certificate, Home Depot's contract with lane pricing and Walmart's contract (its lanes appendix is empty) |
| 24 `nemf_interline_and_carrier_claims` | carrier claims in NEMF's bankruptcy: interline statements, Saia's interline agreement, a dispute correspondence, a W&I vendor's invoice |
| 25 `idl_shipper_freight_files` | **shippers' own freight files** from opioid and JUUL discovery (UCSF IDL, 2006-2020): Mallinckrodt's freight-payment log of 4,901 bills with audit reason codes and 22 quarterly weekly-payment files; JUUL/PAX's 3PL contract, price schedules, invoice detail, AP ageing, billing-error credits and credit memo; a YRC quote → BOL → W&I certificate chain; Endo and Actavis UPS SCS rate schedules, invoices and exception logs; Cephalon claim logs |
| 26 `answer_key_decisions` | 171 reasoned decisions with facts and outcomes: BC Civil Resolution Tribunal 13, GSBCA 89, CBCA 15, CPUC undercharge investigations 54 (28 with per-bill tables); 30 are carded in `answer_keys/` |
| 27 `public_ap_ledgers` | 1,627 payment rows to carriers from 9 Socrata open-checkbook datasets (Richmond, Los Angeles, Connecticut, Cook County ×2, Montgomery County, Atlanta, Dallas, Kansas City): reversals, repeated invoices, GL coding, payment lag |

## Are freight bills standardised? (short answer; AT §6 has the evidence)
Shared across firms: the EDI X12 210/214/204 skeleton, the VICS/GS1 bill-of-lading form, NMFC classes, Part 378's claim content and the "Standard Form for Presentation of Overcharge Claims". Per firm: every carrier's PDF bill layout and charge codes, its mapping of the 210 (Estes writes the discount as text and a negative line, ODFL as a negative line only with no percentage on discount or fuel, AAA Cooper names the base tariff), its rules tariff, its fuel table and its claim channel; every rate agreement; every broker's rate confirmation. Build for one standard data path and many per-firm readers.

## The worked mismatch (AT §7)
SEFL bill 807148067 (set 02, pp. 33 and 46): shipped 2023-05-15; 35 days later a $94.00 balance-due bill added one line, "PVT RESIDEN 94.00", with the carrier's reason printed on it ("per Google Earth this is a private delivery"). Every other line that the agreement prices reconciles to it (the gross rate and the fuel % cannot be checked without the base tariff and the 2023 fuel table); the one question is whether a dwelling stands on the delivery premises. SEFL 1090 Item 753 applies the charge to "the entire premises on which a dwelling for living is located", and leaving residential off the BOL "will not relieve" the shipper of it, so the BOL is evidence, not the deciding document (`doc-explanation.md` §1.1-§1.2; 9 of the 62 SEFL bills carry a residential line). The shipper's 180 days ran to 2023-12-16 at the earliest (the clock runs from receipt); its worksheet never flagged the $94 and the suit came in October 2025. Second example, bill 806625953 (pp. 28 and 41): a balance-due bill of 2023-05-05 for $110.23 that raised the weight from 2,430 to 2,720 lb with no inspection note. The shipper's own worksheet multiplies pallets by the per-shipment minimum charge, which is why its $271,829 claim is overstated. Page map and the independent re-transcription: `research/s5_check_AT_adversarial.md` §2.

## How the registers were reached (for the next round)
- **CourtListener:** `https://www.courtlistener.com/api/rest/v4/search/?type=r&available_only=on&q=…` (anonymous, 5 a minute, 50 an hour); PDFs at `storage.courtlistener.com/recap/gov.uscourts.<court>.<id>/…pdf`.
- **Epiq:** POST `https://dm.epiq11.com/api/search/getcards` (type CasesClaims, filter projectCode: YRC = Yellow, INB = Instant Brands, TLP = Tupperware, TUE = Tuesday Morning, SLQ = STG Logistics); claim PDFs by GET at `https://document.epiq11.com/document/getdocumentbycode?docId=<id>&projectCode=<code>&source=DM` (HEAD returns 405).
- **Angeion / Donlin Recano (NEMF):** HTML POST claimant search, then `/Clients/nemf/GetClaim?claimNumber=N` (redirects to signed S3; HEAD returns 403; a WAF challenge appears after about 40 searches).
- **Epiq dockets (check BE):** POST the same `getcards` endpoint with `{"type":"CasesDockets","term":"","groupBy":"docketNumber","filters":[{"name":"projectCode","values":["yrc"]},{"name":"dbSource","values":["dm"]},{"name":"isAdversaryProceeding","values":["false"]},{"name":"docketNumberSorting","values":["3291-3304"]}],"sort":"asc","documentFrom":0,"documentTake":50,"origin":"CasePage"}`. `filters` must be a list; `docketNumber` is silently ignored (use `docketNumberSorting`, ranges allowed); text search is the `docketText` filter; the response is a JSON string to parse twice. Claims: `CasesClaims`, `groupBy:"claimNumber"`, filter `claimNumberSorting` (returns `remarks`, `docketNumbers`). Documents by the same `getdocumentbycode` GET.
- **UCSF IDL (set 25):** Solr `https://metadata.idl.ucsf.edu/solr/ltdl3/select?q=ot:"…"&fq=collectioncode:(juul OR endo OR teva OR insys OR mnk OR mck)&wt=json`; files at `https://ucsf-idl-dataset.s3.us-east-1.amazonaws.com/{c1}/{c2}/{c3}/{c4}/{id}/` (list with `?list-type=2&prefix=…`; spreadsheets as `{id}.zip`, scans as `{id}.pdf`). One file sits under several ids: dedupe by filename and size. Pair "credit memo", "short pay", "rebill" with a carrier name or SCAC.
- **Decisions (set 26):** BC CRT search `https://decisions.civilresolutionbc.ca/crt/en/d/s/index.do?cont=<q>&iframe=true`, PDFs `…/crt/crtd/en/<id>/1/document.do` (curl; a captcha after about 70 requests); GSBCA `https://www.gsbca.gsa.gov/rate/rate1.htm`…`rate6.htm`; CBCA `https://www.cbca.gov/decisions/rate.html`; CPUC folders under `https://files.cpuc.ca.gov/LegacyCPUCDecisionsAndResolutions/Decisions/`.
- **Socrata (set 27):** discovery `https://api.us.socrata.com/api/catalog/v1?q=vendor%20payments`; rows by SoQL `$where`; exact URLs in each row.
- **Blocked to scripts:** Kroll, Stretto, Omni, Verita/KCC; NYSCEF, CanLII, MuckRock, DocumentCloud, non-Socrata checkbooks; Wayback's CDX index (429 all day on 2026-10-09; it answered again on 2026-10-20: `https://web.archive.org/cdx/search/cdx?url=…&fl=timestamp,original,statuscode`, raw files at `https://web.archive.org/web/<timestamp>id_/<url>`). Some captures are cut at 1 MiB in the archive itself: check `x-archive-orig-content-length` and open the PDF before keeping it. Only `matchType=prefix` queries without server-side filters answer reliably.

## Known, not kept
Bankruptcy statement-of-financial-affairs payment lists (about 90 PDFs used for spend figures in checks AD, AN, S3a); the Miami-Dade freight-audit contract (AS); a Miller v. Costco deposition and a Vital Pharmaceuticals sale order (downloaded earlier, not freight documents); GSA freight-audit price lists (AN). Their URLs are in those research files.

## Verify
```
cd data && sha256sum -c SHA256SUMS | grep -v ': OK'
python3 -I -c "import csv;print(sum(1 for _ in csv.DictReader(open('catalogue.csv'))))"; find sources -type f ! -name source.md | wc -l
```
Both counts must match (658). Rows carry `verify_status` from the adversarial pass (145 verified, 123 narrowed, 3 wrong, all corrections applied); 5 rows still carry `UNRESOLVED` in `url` (the file came from an earlier session and its canonical URL was not found). HEAD checks on 2026-10-09: 250 of 261 URLs answer 200; the claims agents, GAO and NMFTA refuse HEAD requests from scripts but serve GET; two links are dead (the Estes 210 guide moved; the Mitsui v. Roadway RECAP path is unconfirmed).
