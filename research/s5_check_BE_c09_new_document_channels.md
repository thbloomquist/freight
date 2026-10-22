# Check BE · New public channels for C-09 dispute documents, and a collection round

**What this is.** The founders' request of 2026-10-20, verbatim: "How are we currently getting docs? The examples we use for our disputes, are there any other avenues to get a more complete set of documents that are publicly available? We are currently using Court Records right which do not include everything we might need, can we check for any other avenues of exploration for pulling more docs to run more complete testing of potential disputes that may occur? Use Explore Agents, ones that ask the questions and ones that look for opportunities in the answers found."

**Builds on:** check AT (the dataset, `s5_check_AT_c09_document_dataset.md`), its verification, the fact map (`data/doc-exploration.md`), check BD (the dispute walk-through). **Dates:** 2026-10-20 to 2026-10-21. **Status:** an input to the prototype. It decides nothing. **Labels:** *verified* = the file was opened and read; *assumed* = snippet, metadata or a party's statement only. **Adversarial review:** `s5_check_BE_adversarial.md` (summary in §0.1). **No identity was sent:** every brief forbade the user's name or email in headers, forms or queries; sec.gov was not fetched; nobody was contacted; no logins, nothing bought.

## 0. Summary

| | Before (check AT, 2026-10-20) | After (check BE) |
|---|---|---|
| Files in `data/sources/` | 276 in 24 sets | **658 in 27 sets** (+382: 53 in existing sets, 149 in set 25, 171 in set 26, 9 in set 27) |
| Channels that delivered files | 5: RECAP, two claims registers, GitHub, carrier and government sites (+ Wayback) | **+5: Epiq's docket search, the UCSF Industry Documents Library, tribunal and board decision archives, Socrata open-checkbook APIs, further Wayback tariff captures** |
| Shipper-side business records (AP, audit, payment logs) | none | **yes**: a freight-payment log of 4,901 bills with audit reason codes, weekly payment files, a 3PL's invoices with a billing-error credit memo, rate schedules with discounts, a W&I certificate tied to a quote and a BOL |
| Disputes with a known outcome, ready to score | the six chains of `doc-exploration.md` §5 | **+30 answer-key case cards** (`data/answer_keys/`) from 171 decisions |
| Public AP payment rows to carriers | none | **1,627 rows** from 9 Socrata datasets |
| Checks with no real evidence | F2 (GL coding), F4 (rebilled) | F2 and F4 now evidenced (set 25 and 27); E1 still only terms |

**The answer to the founders' question in one paragraph.** Court records are one of five channels today, and every one of them sees a dispute from outside: what a carrier or a shipper chose to file. The documents that court records rarely hold are the shipper's own working files: its AP export, its audit exceptions, its rate schedule, its credit memos. These exist in public in one place found: **litigation discovery archives**, above all the UCSF Industry Documents Library, where the opioid and JUUL productions include shippers' freight departments. The outcomes that court records leave open are often in **the claims register's docket** (Epiq), not the claim itself. And a dispute with a known verdict, the thing needed to *score* the method, is published in bulk by **tribunals and contract boards** (BC Civil Resolution Tribunal, GSBCA, CBCA, the old California PUC). Public **AP ledgers** (Socrata) give payment-side patterns but no documents. Still not public anywhere searched: a stand-alone carrier denial letter, a shipper's Part 378 packet, an LTL guaranteed-service refund, and the carrier's certificate behind a disputed reweigh on the shipper's own bills.

**0.1 Adversarial summary** (`s5_check_BE_adversarial.md`). All 382 rows and all 30 cards were checked: **268 rows verified, 114 narrowed, 0 wrong; 11 cards verified, 19 narrowed, 0 wrong.** Every file matches its hash, size and page count. Most narrowings are vocabulary: withdrawal forms and orders carry no check instance of their own (the instance is on the held claim), and CPUC start dates were placeholders. The ones that change a claim:
- 21-019 closes only the **objection** in 21-002, not the claim;
- 21-018 shows only a debtor split, and "allowed" is a register remark;
- 23-020's earlier "unconditional" withdrawal is not in the file;
- 23-024's amount range was wrong ($7.99-$3,824.80, not $42.78-$2,680.78);
- 25-046 is a delivery receipt with a W&I stamp, not a separate certificate;
- GSBCA-14208's card had "$1,845" corrupted to ",845";
- the cards used "refund" for opposite outcomes (now "payable", "notices invalid" or "undercharge (collect)").

The privacy sweep found what the collectors missed, all fixed the same day under the founders' rules:
- a sixth JUUL–DCL workbook (25-115) with about 47,000 consumer names, now replaced by a stripped zip;
- one consumer address left in a zip;
- staff phones and names in four derived CSVs, now regenerated with a corrected tool;
- four private individuals' names in the Atlanta ledger, redacted.

**No check has a complete chain yet**, as held files. The closest are Estes v. Coverlex (all five parts described for one bill inside the judgment, but the price exhibits are PACER-only) and JUUL–DCL invoice 166482 (price terms, bill detail and a $6,450 billing-error credit, but no record of which line was wrong).

## 1. Method

- **Round 1, three Explore agents (read-only, no saving).** E1, the *questioner*, worked from the repo only: per-check coverage, the missing document types ranked by the facts they unlock, the chains one document short of complete, and 32 questions for the scouts, each marked if `data/leads_tried.csv` had already answered it. E2 scouted government, public-sector and non-RECAP legal channels; E3 scouted datasets, code, vendors, training material, document-sharing sites and archives (about 50 searches and fetches each).
- **Round 2, three *opportunity* Explore agents** working from round 1's answers: E4 mined the Industry Documents Library for chains and the rarest gaps; E5 tried to close the near-complete chains through the channels that work; E6 scored the decision archives as answer keys and the Socrata ledgers as test data.
- **Founders' choices after the exploration (2026-10-21):** collect from all four channel groups (close the near-chains, IDL, answer-key decisions, AP ledgers); keep IDL files in `data/` with personal columns stripped in derived files; 3 collectors and 1 verifier.
- **Collection, three agents.** K1 near-chain closers, K2 IDL, K3 decisions and ledgers. Each staged files in its own scratch folder with a manifest in catalogue format and a leads log; the coordinator merged them (`data/catalogue.csv`, `SHA256SUMS`, per-set `source.md`, `derived/text/`), deduplicated by SHA-256 (no file was already held).
- **Founders' choices on three issues the collectors raised (2026-10-21):**
  - five JUUL–DCL workbooks hold consumers' names, addresses and phones in their B2C sheets: **"Stripped copy only"** — `data/` holds a zip of stripped CSVs per workbook; the originals are in `~/Documents/personal/bio/freight_private/idl_originals/` with their SHA-256 in the catalogue note;
  - size: **"Trim + derived not in git"** — the 51 weekly Mallinckrodt payment files were cut to one per quarter (22 kept, 29 left out, 135 MB; their URLs are in the leads log), and `data/derived/idl/` (280 stripped CSVs) is in `.gitignore` except its `STRIPPED.md`, regenerable with `data/_tools/idl_strip.py`;
  - the GitHub EDI repo has no licence, and one Kraft tender held a staff e-mail and phone: **"Keep for research, redact"** — kept like the copyrighted tariffs; 19-046 is a redacted copy (two NTE segments), marked in its row.
- **Verification, one agent** (no fan-out): content checks on every K1 row, the ledgers and the 30 cards with their decisions read in full; identity checks on the rest; a privacy sweep; coverage → `s5_check_BE_adversarial.md`.

## 2. Where documents come from today (the founders' first question)

| Channel | Files before BE | What it gives | What it cannot give |
|---|---|---|---|
| CourtListener RECAP (free copies of PACER filings) | 79-81 | bills, BOLs, agreements and pleadings attached to collection suits, fraud cases and bankruptcy objections | anything not attached as an exhibit; exhibits never bought by a RECAP user; most outcomes (they sit in later entries, often PACER-only) |
| Bankruptcy claims registers (Epiq, Angeion) | 49 | the claimant's own dispute packet: claim forms, letters, the carrier's "APPROVED" printouts | the disposition (in the docket, not the claim); Kroll, Stretto, Omni and Verita block scripts |
| GitHub | 36 | real EDI 210/214/204 interchanges in parser test folders | anything not EDI |
| Carrier sites | 51 | tariffs, guides, claim forms, fuel tables (current only) | past editions; any customer's prices |
| Government sites | 33 | audit reports, rate decisions, claim forms | private shippers' records |

## 3. Channels tested (E2-E6), and their verdicts

| Channel | Verdict | What it holds for us | Access |
|---|---|---|---|
| **UCSF Industry Documents Library** (opioid, JUUL productions) | **promising** | shippers' freight files 2006-2020: payment and audit logs, rate schedules, 3PL invoices and reconciliations, credit memos, W&I certificates, claim logs | Solr search + open S3 bucket, anonymous (§4) |
| **Epiq docket search** (Yellow) | **promising** | claim withdrawals, omnibus objections and orders, preference complaints with payment exhibits | JSON POST (§4) |
| **RECAP, entries added since round 1** | **promising** | judgments and later rulings in held cases | as before |
| **BC Civil Resolution Tribunal** | **promising, rate-limited** | small freight-billing disputes with facts and a reasoned outcome (remeasure, accessorial not performed, quote vs invoice) | `&iframe=true` search; PDFs; a captcha after about 70 requests |
| **GSBCA rate decisions 1996-2006** | **promising** | federal freight-bill disputes with tender, bill and outcome; 255 plain-text files | index pages rate1-6 |
| **CBCA rate decisions 2007-2024** | marginal-promising | detention, deadlines, reweigh evidence; mostly household goods | one index page |
| **CPUC legacy decisions 1958-77** | promising for math tests | per-bill tables of charge collected vs correct charge (undercharges) | folders list directly |
| **Socrata open-checkbook APIs** | **promising for AP checks** | invoice-level payments to carriers: reversals, repeats, GL coding, payment lag | anonymous SoQL |
| Wayback CDX for tariffs and fuel tables | marginal (flaky) | ODFL 128 fuel tariffs 2022-25, Yellow Item 700/703/705 | prefix queries only |
| GAO B-decisions | marginal | old rate decisions; PDFs are scans and refuse scripts | HTML summaries only |
| NASPO / WA DES pricing exhibits | marginal | parcel/air pricing with minimums and a guarantee waiver; no LTL | free |
| regulations.gov (FMCSA dockets) | marginal | carrier narratives on detention and rate confirmations; attachments rare | DEMO_KEY API |
| BBB complaint pages | marginal | carriers' written replies (wording, e.g. ODFL refunds a late shipment only when Guaranteed was requested on the BOL, *assumed* from one page) | WebFetch only |
| State procurement, cooperative contracts | dead for LTL prices | Utah's UPS LTL page is gone with no capture | — |
| Hugging Face, Kaggle, Zenodo | dead | no freight bill, BOL or 210; synthetic invoices | — |
| Vendor and claims-training material | dead | field lists only; no sample denial letter or Part 378 packet | — |
| Blocked to scripts | — | NYSCEF, CanLII, MuckRock, DocumentCloud, Reddit, non-Socrata checkbooks (checkbooknyc, OpenTheBooks, Ohio, Colorado), ToxicDocs | — |

## 4. Access recipes (new; also in `data/README.md`)

- **Epiq docket search** (K1, *verified*): POST `https://dm.epiq11.com/api/search/getcards` with `{"type":"CasesDockets","term":"","groupBy":"docketNumber","filters":[{"name":"projectCode","values":["yrc"]},{"name":"dbSource","values":["dm"]},{"name":"isAdversaryProceeding","values":["false"]},{"name":"docketNumberSorting","values":["3291-3304"]}],"sort":"asc","documentFrom":0,"documentTake":50,"origin":"CasePage"}`. `filters` must be a list; a filter named `docketNumber` is silently ignored (use `docketNumberSorting`, which takes ranges); text search is the `docketText` filter; the response is a JSON string to parse twice. Documents by the existing `getdocumentbycode?docId=<documentId>&projectCode=YRC&source=DM`. Claims: `type:"CasesClaims"`, `groupBy:"claimNumber"`, filter `claimNumberSorting`; returns `remarks`, `docketNumbers`, `imageDocumentId`.
- **IDL** (E4, K2, *verified*): search `https://metadata.idl.ucsf.edu/solr/ltdl3/select?q=ot:"…"&fq=collectioncode:(juul OR endo OR teva OR insys OR mnk OR mck)&fl=id,filename,dd,…&wt=json` (`ot` = OCR text; year filter `fq=dd:2017*`; facets work on `/select`, not `/query`). Files at `https://ucsf-idl-dataset.s3.us-east-1.amazonaws.com/{c1}/{c2}/{c3}/{c4}/{id}/` (the first four characters of the id), listable with `?list-type=2&prefix=…`; native spreadsheets come as `{id}.zip`, scans as `{id}.pdf`. The same file sits under 3-8 ids (one per custodian): dedupe by filename and size. Many Endo files are placeholders, "Document Withheld - Non-Opioid Product Document" (43 logged). Always combine "credit memo", "short pay", "rebill", "overcharge" with a carrier name or SCAC: alone they return pharma trade deductions.
- **BC CRT** (E6, K3, *verified*): search `https://decisions.civilresolutionbc.ca/crt/en/d/s/index.do?cont=<query>&iframe=true`; documents `…/crt/crtd/en/<id>/1/document.do` (curl, not WebFetch). After about 70 requests at 1.1 s the site serves a captcha for the rest of the day.
- **GSBCA** `https://www.gsbca.gsa.gov/rate/rate1.htm` … `rate6.htm` → `mNNNNNN.txt`. **CBCA** `https://www.cbca.gov/decisions/rate.html`. **CPUC** folders under `https://files.cpuc.ca.gov/LegacyCPUCDecisionsAndResolutions/Decisions/` list their PDFs.
- **Socrata**: discovery `https://api.us.socrata.com/api/catalog/v1?q=vendor%20payments` (213 datasets; 49 with an invoice column across 24 portals) and `q=checkbook`; rows by SoQL `$where=<vendor> in(...)` after a grouped scan of loose name patterns; exact URLs in each set-27 row.
- **Wayback**: only `matchType=prefix` CDX queries without server-side filters answer reliably; domain-wide filtered queries hang.

## 5. What was collected

| Set | Files | Contents |
|---|---|---|
| 23 (+13) | 23-013 … 23-025 | GlobalTranz withdrawals of claims 16200, 16215, 16595 (Docs 3304, 3303, 3295); the 21st omnibus objection and order with its schedule (Cass 19254 re-assigned between debtors); withdrawals by TForce Worldwide (17932), TQL (18553, conditional on a setoff agreement), Home Depot (17878); preference complaints against nVision, Cass, ACCO/Cass and GlobalTranz with payment exhibits |
| 21 (+5) | 21-016 … 21-020 | Mode's withdrawal (17019); the 32nd omnibus order (TForce Freight 10129 split between debtors); two later Winn-Dixie docket entries (Docs 7355, 7354; quarantined for the Case 2 blind run, §7) |
| 09 (+13) | 09-055 … 09-067 | Estes v. Coverlex Docs 12, 33 (judgment $1,829,154.14 on 2,498 bills, with one bill's forfeiture arithmetic), 63; Transport Systems v. Amazon Docs 19, 43; Central Freight v. Amazon Docs 51, 57, 184, 197, 254, 263, 310 (verdict $2,472,227.10), 331 (dismissal) |
| 14 (+7) | 14-077 … 14-083 | ODFL 128-AA, 128-BB, 128-CC (fuel master tariffs effective 2022-06-01, 2023-12-04, 2025-04-09; none truncated); Yellow Tariff 100 Items 700, 703, 705 (2022-03); Yellow's fuel page frozen "as of 07-12-2023" |
| 19 (+12) | 19-037 … 19-048 | production TL 210s from RASY (per-mile linehaul, two fuel lines, loading credit, unloading charge); ACDT 210s; a Kraft 204 → 214 pickup chain (shared SI 20447663200101); 204 original/cancel pair; a 990 |
| 13, 15, 16 (+1 each) | 13-079, 15-085, 16-097 | XPO CNWY 199-AI.2 (2024-04-15); Yellow's Uniform BOL terms; Yellow's blank inspection report |
| **25 `idl_shipper_freight_files`** (new, 149) | 25-001 … | Mallinckrodt (paylog pycp0254, 4,901 bills with audit reason codes, and FedEx siblings; 22 quarterly TRN payment files 2007-13 with Audit $ and discount %), JUUL/PAX (DCL contract and 2016-17 price schedules, invoice detail, AP ageing, "Billing Errors" credits and a credit memo; a YRC quote → BOL → W&I certificate chain), Endo and Actavis with UPS SCS (CzarLite/FAK schedules, invoice CSVs, exception logs, audit-savings decks), Cephalon/Teva claim logs, single bills and delivery receipts |
| **26 `answer_key_decisions`** (new, 171) | 26-001 … | BC CRT 13 (2018-20), GSBCA 89 (about 70 are Tri-State munitions TL), CBCA 15, CPUC 54 (28 with per-bill tables) |
| **27 `public_ap_ledgers`** (new, 9) | 27-001 … | Richmond, Los Angeles, Connecticut, Cook County (2), Montgomery County, Atlanta, Dallas, Kansas City: 1,627 carrier rows |

**Answer-key cards** (`data/answer_keys/`, 30 + `INDEX.md`): 12 BC CRT, 7 GSBCA, 6 CBCA, 5 CPUC. Each card maps the decision's facts to the fact IDs of `doc-exploration.md` §1, lists what the method lacks and which pipeline stages can run, and records the true outcome with a quoted reason and reference. `expected_verdict` is TBD on every card: the founders set it. The cards cover A1, A3-A7, B1-B8, C1, D1-D5, E1, E2, F1, G1, G2 and 57 fact IDs; not A2, C2, D6, D7, F2-F4.

## 6. Chains closed, and what still is not public

| Held chain | New file(s) | What it settles | Still missing |
|---|---|---|---|
| 23-002 GlobalTranz 16200 ($60 TONU) | 23-013 | claim withdrawn 2024-05-07, no reason | Yellow's bill; the pickup request; Yellow Tariff 100 |
| 23-003 GlobalTranz 16215 ($75 limited access) | 23-014 | withdrawn, no reason | Yellow 100 Item 754 (2023); the bill |
| 23-004 GlobalTranz 16595 ($382.08 reweigh) | 23-015 | withdrawn, no reason | the carrier's certificate; the bill |
| 23-006 nVision 11113 ("APPROVED") | 23-022 | partly: the approved draft is not among the 11 refunds Yellow paid nVision before filing (unpaid *assumed*) | the claim's disposition |
| 23-001 Cass 19254 | 23-016 … 23-018 | split between two debtors; validity not ruled on | the allowance |
| 23-010 TQL 18553 | 23-020 | withdrawn on condition of a setoff agreement | the agreement's terms |
| 23-009, 23-005, 21-014 | 23-019, 23-021, 21-016 | withdrawn (TForce Worldwide; Home Depot 2025-11-03; Mode 2024-03-26) | — |
| 21-015 TForce Freight 10129 | 21-017, 21-018 | debtor split; "allowed" only on the register | — |
| 21-002 Winn-Dixie (Case 2) | 21-019, 21-020 | part of the outcome (§7) | the claim's final treatment; ODFL's 2004-05 price terms |
| 09-041 Estes v. Coverlex | 09-055 … 09-057 | **closed**: judgment $1,829,154.14 stands; one bill's forfeiture arithmetic worked | the agreement and tariff exhibits (PACER only) |
| 09-033 / 09-048 Central Freight v. Amazon | 09-060 … 09-067 | **closed**: verdict $2,472,227.10, then dismissal with prejudice (settlement inferred) | the audit itself (sealed) |
| 10-039 Transport Systems v. Amazon | 09-058, 09-059 | closed, but not on billing (forum clause; standing) | — |
| 21-003 (ODFL statement, June-July 2023) | 14-077 | the fuel tariff in force (128-AA, 2022-06-01 to 2023-12-03) | the weekly diesel reading, in the held EIA series |

**In set 25, the near-chains are new rather than closed.** They are Mallinckrodt's paylog (4,901 bills, each with an audit reason code), JUUL–DCL (price schedule → invoice → billing-error credit → credit memo) and PAX–YRC (quote → BOL → W&I certificate, +106 lb, but the final invoice is missing). None has the carrier's price terms behind the shipper's audit. About 25 IDL queries found no agreement for the paylog's carriers.

**Still not public after BE** (searched in every channel above): a stand-alone carrier denial letter or carrier credit memo on an LTL bill (the IDL credit memo is a 3PL's); a shipper's Part 378 overcharge packet; an LTL guaranteed-service refund (terms only); the carrier's W&I certificate behind a reweigh on the shipper's own disputed bill (IDL's PAX–YRC chain has one, but its final invoice is missing); a shipper-facing TL rate confirmation from a TMS; Yellow Tariff 100's rules items (754, TONU, reweigh); any rules-tariff edition before 2021; weekly carrier fuel tables before 2022 (ODFL) or outside 2021-22 (Yellow). PACER-only, not bought: Estes v. Coverlex 19-1; Estes v. Whatman 1-1, 9-5, 19-5; Central Freight v. Amazon 1-1; Hannum 72-3; Exist v. SEFL Docs 4-6 (Doc 6 is the order on the motion to dismiss).

## 7. Outcomes that touch the walk-throughs (blind-run note)

- **Case 1 (Yellow claim 16200, check BD), already run.** New outcome: GlobalTranz withdrew the claim (Doc 3304, filed 2024-05-07; the form states $60.00 filed, the register $0.00), with no reason stated. It fits BD's §6 reading (an approved dispute lost to payment and the bankruptcy) and is offered to the founders as an extra outcome to compare. BD is not edited here.
- **Case 2 (ODFL / Winn-Dixie, 21-002), running blind from a kit outside the project.** 21-019 and 21-020 belong to its outcome, which is not described here. **The Case 2 runner must not read rows 21-019/21-020, this section or `s5_check_BE_adversarial.md` before writing its verdict.** The kit itself (`~/Documents/personal/bio/freight_case2_blind/`) was not touched.
- **The answer-key cards are outcomes.** A blind run on any of them needs a whited-out copy of the decision, never the card.

## 8. Open points (for the founders; nothing decided)

1. Whether to buy the PACER-only exhibits (§6), above all Exist v. SEFL Doc 6.
2. Whether to OCR the GAO B-decisions (scanned; hundreds of old rate decisions).
3. Whether to widen IDL beyond the first pass (a Mallinckrodt search for the paylog carriers' agreements found none in about 25 queries; the 43 withheld Endo files cannot be had).
4. Whether answer-key cards from other regimes (BC contract law; the federal 3-year audit rule; 1960s California minimum rates, where the sign is reversed) count toward the clock tests (G1, G2) or only toward the compare-stage math.
5. Who sets each card's `expected_verdict`, and when (before or after a blind run).
6. Whether to retry the BC CRT for the 26 identified but unfetched decisions (2021-26; citations in K3's list, held in the leads log) on another day.
7. IDL's reuse wording: its copyright and policy pages are a JavaScript app and returned no text to scripts; the metadata marks all 178 records "public, no restrictions" (*verified*), and earlier search snippets describe "court-approved agreements … or the fair use doctrine" with a takedown policy (*assumed*). Someone should read the page in a browser.
8. Seven sources contradict themselves: CBCA 1637, CBCA 3467, 2019 BCCRT 63 and 2018 BCCRT 886 (the cards use each order's figure), plus CBCA 4071, CPUC D63338 and GSBCA 15194 (`s5_check_BE_adversarial.md` §4). Whether such cases stay as answer keys is for the founders.
9. 19-027, held since check AT (a Seaboard 204), carries a person's name and phone in a G61 segment: the issue fixed in 19-046. Redact it the same way?
10. The founders' privacy rule was applied to a sixth workbook (25-115) after verification; the same rule may still be needed for parcel rows to individuals in the pharmaceutical consignee columns (verifier's concern, unproven).

## 9. Claim ledger

| ID | Claim | Source | Label |
|---|---|---|---|
| BE-01 | No check of the 33 had a complete chain in `data/` before BE | E1, from `doc-exploration.md` §5.7, AT §5, catalogue | verified |
| BE-02 | Epiq's docket search answers anonymous JSON POSTs with the filter shape in §4 | K1 runs | verified |
| BE-03 | Docs 3304, 3303, 3295 withdraw claims 16200, 16215, 16595 | 23-013 … 23-015 | verified (K1; re-checked by V1) |
| BE-04 | Cass 19254 was re-assigned between debtors, not disallowed | 23-016 … 23-018 | verified (K1; re-checked by V1) |
| BE-05 | Estes v. Coverlex: judgment $1,829,154.14 | 09-056 | verified |
| BE-06 | ODFL 128-AA/BB/CC effective 2022-06-01, 2023-12-04, 2025-04-09; byte lengths match the archive's originals | 14-077 … 14-079 | verified |
| BE-07 | IDL Solr and S3 answer anonymously; native files arrive as zip | E4, K2 | verified |
| BE-08 | pycp0254 holds 4,901 bills with audit reason codes | 25-row for pycp0254 | verified (K2) |
| BE-09 | 43 Endo freight files are withheld as "Non-Opioid Product Document" | K2 leads log | verified |
| BE-10 | BC CRT serves a captcha after about 70 requests | K3 HTTP log | verified |
| BE-11 | GSBCA lists 255 rate decisions as plain text | rate1-6.htm | verified |
| BE-12 | 49 Socrata datasets carry an invoice column, across 24 portals | E6 catalogue query | verified |
| BE-13 | No ML dataset holds a freight bill, BOL or 210 | E3 searches | verified (searched sets), assumed beyond them |
| BE-14 | No LTL price sheet on any procurement portal searched | E2 | verified for those searched |
| BE-15 | IDL reuse is fair use with a takedown policy | search snippets | assumed |
| BE-16 | 268 of 382 rows verified as written, 114 narrowed, 0 wrong | `s5_check_BE_adversarial.md` §1 | verified |
| BE-17 | No check has a complete chain as held files after BE | `s5_check_BE_adversarial.md` §6 | verified |

## 10. Coincidence watch

- Three of the strongest new chains (GlobalTranz, nVision, Cass) all come from one bankruptcy, Yellow's. A method tuned on them learns one carrier's habits.
- The IDL shippers are large pharmaceutical and vaping companies, far above C-09's $0.5-10M segment (27 rows are "possibly" in segment). Their freight departments are more mature than a mid-sized shipper's.
- The answer keys over-represent disputes someone chose to litigate, and GSBCA is about 80% one claimant (Tri-State).
- The AP ledgers are municipal buyers, outside the segment, and vendor-master names are not proof of the service bought (Cook's and Atlanta's "UPS Freight" rows look like parcel).
