# S5 check AJ: reading freight documents by machine for the C-09 audit machine

- **What this is:** desk research for card C-09, after the founders' decision of 2026-10-03 that version 1 is an audit machine only. They asked us to "look into this avenue heavily". It covers AJ1-AJ8:
  - what the files look like;
  - the ways to extract data from them;
  - how to make the extraction trustworthy;
  - splitting pages;
  - barcodes;
  - rate agreements;
  - highlighting on the page;
  - what reading costs per customer.

  It builds on earlier work without redoing it: the practice audit (`s5_practice_audit_public_invoices.md`, PA), check AC (`s5_check_AC_c09_example_invoices.md`) and check AA §2 (`s5_check_AA_c09_cost_to_serve.md`).
- **Summary for the founders:** `software-initial-pitch.md`.
- **Date:** 2026-10-03. All web sources were read that day.
- **Status:** input to S5. **It decides nothing.** Design suggestions are marked **[our call]**.
- **Labels:**
  - *verified* = read at the primary source.
  - *assumed* = a search snippet, a vendor's claim, a blog or memory. Vendor accuracy claims are always *assumed*, including benchmarks run by a vendor.
  - **[our calc]** = our arithmetic. **[our call]** = our judgement.
- **Access:** about 33 web searches and about 95 page fetches. The GitHub and Hugging Face public APIs were used without login. No personal identity was sent anywhere, and nobody was contacted.
  - The fetch tool could not parse three PDFs: Saia's billing sheet, FedEx's EDI overview and the GS1 BOL guideline. The tool's own cached copies were read as page images instead. No files were written to the project or to /tmp.
- **IDs:** new sources are N-AJ01 to N-AJ86 (§13). Earlier IDs keep their meaning (N-PA01/02, N-AC02–N-AC16, N-T17–N-T29, N-AA01–N-AA18, N-AA65).
- **Re-checked at the source by the coordinator (2026-10-03), all matching:**
  - PyMuPDF is "available under both, open-source AGPL and commercial license agreements" (N-AJ19);
  - Anthropic list prices: Opus 5.5 $4/$20 per million tokens, Sonnet 5.5 $2/$10, Haiku 4.5 $1/$5, batch at half price (N-AJ01);
  - the XPO PRO check digit is "the first eight digits divided by seven", with the remainder as the check digit (N-AJ54);
  - Marker's model weights are "free for research, personal use, and startups under $5M funding/revenue" (N-AJ16).
- **One correction by the coordinator:** §9 scales the fee at $1.95 per $1,000 of spend. The model's exact figure is **$1.97** ($1,000 × 1.5% × 70% × 75% × 25% = $1.96875). This lowers the "share of fee" percentages by about 1%. The conclusions don't change.
- **A real example built on this method:** `research/img/abf_150235531_highlights.png`. It takes word positions from the PDF's own text layer (`pdftotext -bbox-layout`) and draws highlights on a public ABF bill.

**Words used here:**
- **Text layer:** the machine-readable text inside a born-digital PDF.
- **OCR:** optical character recognition (turning a page image into text).
- **VLM:** a vision-language model, an AI model that reads page images.
- **Bounding box ("bbox"):** the rectangle a word or value occupies on the page.
- **Grounding or citation:** linking each extracted value back to its place on the page.
- **TEDS:** a table-similarity score.
- **PRO:** the carrier's shipment and invoice number.
- **DR:** delivery receipt (the signed proof of delivery).
- **W&R:** weight-and-research certificate.

---

## 1. Summary table

| Q | Headline answer | Best evidence | Labels |
|---|---|---|---|
| **AJ1 What the files look like** | Carrier-direct invoices are mostly born-digital:<br>- every carrier checked emails PDFs;<br>- XPO also sends CSV/XML digests;<br>- EDI 210 is common.<br>The supporting papers are images:<br>- FedEx Freight's "PDF Image Delivery" puts the invoice, BOL and DR in one PDF per invoice;<br>- BOLs carry a PRO sticker the driver applies;<br>- DRs carry signatures, tick-boxes and wait-time boxes.<br>Copies that pass through a shipper's AP team or a 3PL come back as scans with stamps and handwriting (the SEFL set).<br>§2.4 lists 15 parser traps, most of them seen in the public court sets | N-AJ09, N-AJ05, N-AJ04, N-AJ07, N-AJ08, N-AJ61, N-PA01, N-PA02, N-AC02 | carrier statements *verified*; the overall born-digital vs scan split **[our call]** |
| **AJ2 Extraction approaches** | **Born-digital pages:** read the text layer with word coordinates (pdfplumber MIT; pypdfium2 Apache/BSD; poppler `pdftotext -tsv`). It is exact and nearly free.<br>**Scans:** cloud OCR at $1.50 per 1,000 pages returns word boxes and confidence.<br>**VLMs:** best at turning words into fields. Claude's citations give page numbers only; Gemini, Qwen, DeepSeek-OCR and dots.ocr give element boxes.<br>**Grounding vendors:** Reducto, LandingAI, Extend and LlamaExtract give a box per value for **$5.50–62.50 per 1,000 pages**.<br>**Licence traps:**<br>- AGPL: PyMuPDF, Unstract, MinerU 2.5 weights;<br>- MinerU's code carries an attribution duty;<br>- non-commercial: LayoutLMv3, Qwen2.5-VL-3B;<br>- Marker and Surya weights are free only under $5M of funding or revenue | N-AJ15–N-AJ24, N-AJ29–N-AJ39, N-AA02/03 | prices *verified* (stated) unless marked; licences *verified*; benchmark numbers *assumed* when vendor-run |
| **AJ3 Trustworthy enough for an audit** | Papers document VLMs that over-rely on "linguistic priors", invent content, substitute meaning and make "plausible but visually unsupported corrections". The best models still miss about 7% of fields on scanned invoices and about 15% on handwritten forms.<br>Trust must come from **checks outside the model:**<br>- the bill adds up;<br>- each value is found on the page at a known position;<br>- two independent readings agree;<br>- format checks pass (XPO mod-7 PRO check digit, GS1 mod-10 BOL number, SCAC);<br>- the invoice matches the other documents;<br>- a person reviews what is left.<br>A bad claim has a cost: ODFL charges **$50** on settled claims "through no fault of Carrier" and will not reopen a closed claim | N-AJ40–N-AJ43, N-AA18, N-AJ48, N-AJ54, N-AJ60, N-T17, N-AC10 | papers *verified* (abstracts); check-digit gaps **[our calc]** |
| **AJ4 Splitting and classifying pages** | First split on cheap signals: the PRO or BOL number, page titles, "page x of y", barcodes, FedEx's file names. Then classify what is left:<br>- Azure custom classifier: **$3 per 1,000 pages**; splits automatically; needs 5 samples per type;<br>- Google splitter: about $5 per 1,000 (*assumed*);<br>- LLM page classifiers: cents to a few dollars per 1,000.<br>Evidence:<br>- a fine-tuned 7B LLM: page F1 0.987, document F1 0.967 (TABME++);<br>- frontier VLMs: a 0.91–0.94 "packet" score, but only 0.50–0.80 with every page, split and order right (DocSplit) | N-AJ49, N-AJ58, N-AJ59, N-AA03 | *verified* (docs, papers); LLM costs **[our calc]** |
| **AJ5 Barcodes** | The PRO goes on the BOL as a carrier sticker (Estes: "placed here (by driver)"). The GS1 US BOL guideline reserves space for an **optional** GS1-128 barcode of the BOL number and SCAC/PRO. Barcodes on invoices and DRs were not verified.<br>Decoders: zxing-cpp (Apache-2.0), pyzbar (MIT) on ZBar (LGPL-2.1), and Azure's free barcode add-on.<br>A readable barcode beats OCR for the PRO key, but coverage is partial, so it should confirm the key, not be the only key | N-AJ60, N-AJ61, N-AJ63, N-AJ50, N-AJ15 | *verified*; reliability figures *assumed* |
| **AJ6 Rate agreements and tariffs** | Rate loading is still mostly manual, or "AI" on vendors' say-so (Trax "98%", Pando "100%", both *assumed*). Agreements are versioned tables: lanes, zone discounts, floors, FAK ranges, pallet rates with exclusions.<br>The best table parsers score about 80–95% on table benchmarks, so every loaded figure needs a human check. The bills themselves can back-test a load: the ABF set shows 89.5% and a $180 floor.<br>**No published figure for hours per load.**<br>Tariffs come as dated version files. Some superseded files stay online (ABF 2025, Saia 2024); others cannot be found (ABF's 2024 fuel table) | N-AJ65, N-AJ66, N-AJ28, N-AJ25, N-PA01, N-AJ68, N-T24 | mostly *assumed*; local facts *verified* |
| **AJ7 Highlighting on the document** | Products draw coloured boxes on the page, linked to fields (Rossum: yellow, green, red), and grounding APIs return a box per value.<br>Building blocks for our own viewer:<br>- viewer: PDF.js (Apache-2.0) with react-pdf-highlighter-extended (MIT);<br>- annotated PDF for disputes: pypdf (BSD-3) writes true Highlight annotations; pdf-lib has no annotation API;<br>- avoid PyMuPDF (AGPL) unless licensed.<br>Apryse and Nutrient sell by quote only (median about $24–31k a year, *assumed*) | N-AJ69, N-AJ33–N-AJ37, N-AJ21–N-AJ23, N-AJ72, N-AJ71 | *verified* except where marked |
| **AJ8 Is OCR "pricey"?** | **No.** A $1.5–3M customer produces about 4,500–33,000 pages a year. Yearly reading cost by method:<br>- cloud OCR: **$7–50**, at most 0.6% of the fee;<br>- document-AI invoice models: $45–330;<br>- a Claude Sonnet 5.5 pass: $150–444;<br>- Opus 5.5: $300–890.<br>**One 6-minute US exception review ($3.68) costs as much as cloud OCR of about 2,450 pages.**<br>What drives cost: human exception review (42–63% of the fee at a 15% touch rate; 164–242% at the 58% seen in the practice audit), and platform minimums ($5–18k a year) | §9 | **[our calc]** on *verified* prices |

---

## 2. AJ1: What the files really look like, and the text-format traps

### 2.1 Born-digital or scan, by document type

| Document | Usual form | Evidence | Label |
|---|---|---|---|
| **Carrier invoice fetched from the carrier** (email, portal, EDI) | Born-digital PDF with a text layer, or data (EDI 210, CSV, XML) | The 101 ABF bills had a machine text layer and parsed cleanly (N-PA01). All carriers in §2.2 email PDFs or offer EDI; XPO sends "CSV, PDF or XML" (N-AJ05) | *verified* for these sources; "usually" **[our call]** |
| **Invoice after passing through AP or a 3PL** | Scan with stamps, circles, handwriting | The SEFL court set: "handwritten circles and a 'POSTED' stamp", scanned with OCR errors (N-AC03, N-PA02) | *verified* (that set) |
| **Signed BOL** (at pickup) | Image (scan or photo); PRO sticker applied by the driver | Estes BOL item 25: "Estes PRO label is placed here (by driver)" (N-AJ61). FedEx's BOL comes inside an "image" PDF (N-AJ09). The XPO court set was page images (N-AC02) | *verified* |
| **DR / POD** | Image: signature, "received … except as noted", tick-boxes (liftgate, inside), **"WAIT TIME START / END"** boxes, delivery time | XPO and Yellow DRs (N-AC02, N-AC06). Vendor blogs call PODs the least machine-readable document (N-AJ13, *assumed*) | fields *verified*; handwriting common **[our call]** |
| **W&R / inspection certificate** | A carrier-generated report plus photos, from a portal or API | Document APIs: ODFL, R+L, TForce (N-T18, N-T27, N-T29). XPO's Document Finder lists "Weights and Corrections, Weights and Research Photos … Inspection Report, NMFC Certificate" (N-AJ06). No public example (AC §3.6) | sources *verified*; file layout unknown |
| **Lumper / detention receipts** | Paper, photographed or scanned | Factoring programmes require "lumper or detention receipts" in the invoice packet (N-AJ12) | *assumed* |
| **TL rate confirmation** | Born-digital PDF from the broker's system, sometimes signed and rescanned | Two C.H. Robinson confirmations had text layers (N-AC08/09). Sensible's open library carries **18 separate rate-confirmation layouts**, one per broker (N-AJ81) | *verified* |
| **Carrier statements and digests** | A PDF or email covering many bills | Estes: "daily, weekly, and or monthly invoices and/or monthly statements" (N-AJ04). XPO data is "collected in an email … on a daily or weekly basis" (N-AJ05) | *verified* |

### 2.2 How carriers deliver invoices

| Carrier | Invoice channels found | Supporting documents | Label |
|---|---|---|---|
| **ODFL** | "Old Dominion Freight Line now offers you the ability to receive your invoices via email" (e-statement invoices); online invoice pages | Document API: Inspection Certificate, Weight Certificate, Weight Verification, Research Verification, Pickup Photo, "Linked to the bill to party on the pro" (N-T18) | *verified* (N-AJ03) |
| **Estes** | Emailed invoices and statements, daily, weekly or monthly, with a sign-up box for "Bill of Lading" and "Delivery Receipt". Paper, PDF or EDI; emails come from a Billtrust address (snippet) | Document retrieval for BOL, DR and W&R certificate by email (snippet) | form *verified* (N-AJ04); Billtrust *assumed* |
| **XPO** | Electronic Invoice Presentment (EIP): "CSV, PDF or XML", "daily or weekly"; filters for "original or corrected" and "prepaid or collect" | Document Finder (login needed): BOL, LOA, Weights and Corrections, W&R Photos, Freight Bill Copy, DR, Inspection Report, NMFC Certificate, Appointment Confirmation | *verified* (N-AJ05, N-AJ06) |
| **Saia** | "E-Billing: Receive invoices via Email with backup support using Saia Secure Financials option"; a Billtrust portal (snippet) | "backup support" (not specified) | *verified* (N-AJ07); Billtrust *assumed* |
| **ABF / ArcBest** | EDI 210 specification 2024-12 (N-AC16); no invoice-delivery page found | BOL templates read "AFTER PRINTING, PLACE PRO LABEL HERE" (snippet, N-AJ62) | 210 *verified*; rest *assumed* / not found |
| **FedEx Freight** | Three electronic formats:<br>- EDI 210: "one invoice per transaction set, and multiple transaction sets per electronic invoice file";<br>- CSV: "one record per invoice";<br>- **"PDF Image Delivery, which contains the invoice, bill of lading, and delivery receipt for a shipment. Each PDF contains these documents for one invoice. The file naming … indicates the invoice number, account number, and invoice date."**<br>Past-due invoices are also sent "via EDI or PDF image delivery" | Billing portal: "Invoices and supporting document information are available for one year after the invoice date" | *verified* (N-AJ09 pp. 7–8, Jan 2020; N-AJ10) |
| **R+L** | Invoice viewing online (snippet); EDI 210 (N-AC17) | Document Retrieval API: "BillOfLading, DeliveryReceipt, Invoice, WeightCertificate, NmfcCertificate, LetterOfAuthorization, DeliveryPhoto" (N-T27) | API *verified* |
| **SEFL** | "Internet Invoicing": an "abbreviated invoice" emailed as a PDF "the morning following pickup (before 12 Noon)", daily; "Most third parties have additional document requirements (bills of lading, delivery receipts, etc.) and are not suited for this method" | Separate requests | *verified* (N-AJ08) |
| **TForce** | EDI 210 with original, corrected and balance-due invoices; "Once set up electronic invoices, copies of the delivery receipts or bills of lading are no longer mailed" (N-AC14) | Documents API: WRC (W&R certificate), REWE (reweigh ticket), CMC (cube measurement certificate) (N-T29) | *verified* |
| **AAA Cooper** | An "Email Invoicing Request" application (snippet) | — | *assumed* (N-AJ11) |
| **TL carriers, brokers, factors** | A factored carrier submits "the rate confirmation, signed bill of lading, proof-of-delivery, and your invoice", typically "through a mobile app or online portal"; the factor then bills the broker or shipper with a "Notice of Assignment" | Lumper and detention receipts when billed | *assumed* (N-AJ12) |

**Reading [our call]:** expect three input shapes.
1. **Data (EDI 210, CSV, XML).** The cleanest, but supporting papers may stop arriving: TForce stops mailing them, and Estes marks the POD segment "Not Used".
2. **A born-digital invoice PDF**, alone or in a digest.
3. **Image bundles:** FedEx's invoice + BOL + DR files, factoring packets made of phone photos, and rescans from AP or a 3PL.

### 2.3 Template parsers and freight

- **One carrier layout took real work.** The local ABF parse needed about 6 rounds of fixes for that one layout (PA §5).
- **TL layouts multiply.** Sensible's 18 broker-specific rate-confirmation configurations (N-AJ81) show how many there are.
- **Ready-made templates don't cover US freight.** invoice2data's visible template tree holds about 300 templates, mostly European. The only shipping ones are `nl.fedex`, `fr.chronopost` and `fr.laposte.coliposte`. None for US LTL carriers or BOLs was seen (N-AJ80, *verified*, tree truncated).

### 2.4 Format traps a parser meets

| # | Trap | Real example | Handling **[our call]** |
|---|---|---|---|
| 1 | **Several bills in one PDF; repeated pages** | ABF exhibit: 107 pages = 101 bills + 6 copies; **one page held two bills** (N-PA01) | Split and key on PRO; deduplicate on PRO + amount + bill type |
| 2 | **Invoice + BOL + DR in one file** | FedEx PDF Image Delivery (N-AJ09); XPO claim packets (N-AC02) | Classify each page (§5) |
| 3 | **Statements and digests** | XPO EIP; Estes monthly statements; SEFL "PAST DUE INVOICE" reprints (N-AC03) | Treat a statement as a reconciliation source, not an invoice |
| 4 | **Corrected, balance-due and re-billed invoices reusing the PRO** | XPO "CORRECTED INVOICE" / "BALANCE DUE INVOICE"; 4 corrected ABF bills; EDI B308 codes BD/RC/AR/BE; a SEFL shipment of 2023 with "date billed 2025-08-26" (N-AC02–N-AC04, N-AC11/14) | Key on PRO + version; keep both the ship date and the bill date |
| 5 | **Carrier-specific charge codes** | ABF: MCADJ, CCS, SHDL (lumper), DETND (detention), "DEF163 AS2000", "W02/AUTH:Reweigh". XPO: LP1–LP6 (late fees), CBR (reweigh fee), APT, "M". SEFL: "DISCOUNT PERCENTAGE 9100" (N-AC02–N-AC04) | A code dictionary per carrier; "9100" has implied decimals |
| 6 | **Rates per hundredweight (cwt)** | 16.15 cwt × 304.71 = 4,921.07 (SEFL); "M" printed instead of a rate (XPO) | Normalise units; recompute every line |
| 7 | **Deficit-weight and minimum-charge lines** | "ALLOWS LOWER CHARGE AT HIGHER WEIGHT DEF163 AS2000"; "ABSOLUTE MIN CHARGE ADJUSTMENT" bringing the bill to $180.00 net (N-PA01) | Model them as signed adjustment lines |
| 8 | **Credits shown in parentheses or with a minus** | XPO discount "(293.92)"; ABF −6,232.60 and "Dynamic discount −181.83"; 3M's 210 rules: "unable to accept a negative dollar amount" (N-AC02, N-AC04, N-AC11) | Parse the sign explicitly; rely on the sum check |
| 9 | **Non-money text that looks like money** | "READY 1.00 PM" was read as money (N-PA01) | Take amounts by column position; sum check |
| 10 | **Columns aligned by position; reading order** | Needed `pdftotext -layout`. Labels and values can sit far apart, and plain text loses which value belongs to which row (N-AJ86, *assumed*) | Use word coordinates (pdfplumber; poppler `-tsv`), not plain text |
| 11 | **Handwriting, stamps, signatures** | SEFL set (circles, "POSTED"); DR tick-boxes and wait-time boxes (N-AC03, N-AC06) | Flag for a person; never resolve automatically |
| 12 | **Low-quality scans and faxes** | SEFL OCR errors. Azure's minimum text height is "about 8-point text at 150 dots per inch" (N-AJ49). Xerox scanners swapped digits through lossy JBIG2 compression ("sixes were replaced by eights", N-AJ45) | Keep originals; reject or route very low-resolution pages |
| 13 | **Tables spanning pages** | Yellow DR: total charges on "NEXT PAGE" (N-AC06). Azure gives lower confidence to rows split across pages (N-AJ48) | Stitch pages before the sum check |
| 14 | **Two dates, one shown** | ABF and XPO print only one of ship date and bill date in places (N-AC04) | Keep both fields; fetch the missing one from the BOL |
| 15 | **Look-alike duplicates** | Same amount, same day, different shipments on a minimum-charge account (N-PA01) | Key on PRO + BOL, never on amount + date alone |

Rotated pages were not seen in the public sets. A benchmark paper (CC-OCR) reports models weak on "multi-orientation" text (snippet, *assumed*).

---

## 3. AJ2: The extraction approaches, compared

### 3.1 Comparison by family

| Family | How it works | Accuracy evidence | Cost per 1,000 pages | Boxes for highlighting | Handwriting |
|---|---|---|---|---|---|
| **(a) Text layer** (pdfplumber, pdfminer.six, pypdfium2, poppler, PyMuPDF; Camelot/Tabula for tables) | Reads the characters and their positions straight from the PDF; groups them into words, lines and tables | No recognition step, so the characters are exact. Local run: **99/101 bills reconciled to the cent**; both misses were parser mistakes (N-PA01). pdfplumber "Works best on machine-generated, rather than scanned, PDFs" (N-AJ73) | About $0 (compute). Marker without OCR: "23.7 pg/s" on CPU (N-AJ16, *assumed*) | **Exact, per character and per word.** pdfplumber gives `x0, x1, top, bottom` (N-AJ73); poppler gives `-bbox`, `-bbox-layout` and `-tsv` "for each block, line, and word" (N-AJ24) | None (no text layer for ink) |
| **(b) Templates** (invoice2data YAML, Docparser, Parseur, Sensible SenseML, zonal OCR) | Rules or zones per sender and layout | Exact while the layout holds; breaks when it changes (PA §5, ABF vs SEFL) | Docparser: $39 a month for 100 documents of up to 5 pages, about **$78–390** per 1,000 pages. Sensible: $449 a month for 750 documents, then $0.57 per extra document (N-AJ82, N-AJ81) **[our calc]** | Product-dependent (not checked) | Via their OCR |
| **(c) Classic OCR** (Tesseract, PaddleOCR, docTR, EasyOCR; OCRmyPDF adds a text layer to scans) | Detects text lines, then recognises the characters | PP-OCRv5 claims "+4.6% detection and +5.1% recognition accuracy" over its predecessor (N-AJ75, *assumed*) | Self-hosted: cents per 1,000 pages on CPU or GPU **[our call]**. An L4 GPU rents for $0.49 an hour (N-AJ83) | Tesseract TSV: "left, top, width, height, conf, text" per word (N-AJ74). PaddleOCR: line boxes with confidence (N-AJ75) | Weak (Tesseract's docs don't claim handwriting, N-AJ74) |
| **(d) Cloud document AI** (Textract, Azure, Google, Mistral) | Hosted OCR plus field extraction | Table benchmark RD-TableBench: Azure 82.7, Textract 80.9, Google 64.6 (N-AJ28, vendor-run, *assumed*). Mistral OCR on olmOCR-Bench: 72.0 overall, **60.6 on tables** (N-AJ25) | Textract OCR $1.50; AnalyzeExpense $10; Analyze Lending $70 (N-AJ52). Azure Read $1.50; prebuilt invoice $10 (AA, unchanged). Google Enterprise OCR $1.50 (snippet). **Mistral OCR 4.1 $4; "Document AI" $5** (N-AJ29, new) | **Yes.** Textract: a box and confidence per field (`ValueDetection` with `Geometry` and `Confidence`) (N-AJ53). Azure: polygons per word and per field (N-AJ50). Mistral: **block-level** coordinates and per-word confidence, but no word boxes (N-AJ30) | Azure Read reports "handwritten style" (N-AJ51). Textract handwriting is English only (snippet, *assumed*) |
| **(e) VLM/LLM** (Claude, Gemini, GPT; open models) | Reads the page image and/or text and outputs fields | Best invoice field accuracy **96.5% clean / 92.7% scanned** (AA, N-AA18). IDP Leaderboard v1.5: GPT-5.4 83.5, Gemini-3-Pro 82.8, Claude Sonnet 4.6 80.7 (N-AJ27, run by Nanonets, *assumed*). **Handwritten forms: best about 85% of fields** (N-AJ43) | See §9. Per page: Gemini 2.5 Flash about $1.5, Haiku 4.5 about $7, **Sonnet 5.5 about $17, Opus 5.5 about $34** **[our calc]**, from AA's packet figures | **Claude's citations give page numbers only** (`page_location`). Citations can't be combined with schema-enforced output: "returns a 400" (N-AJ02). Gemini gives boxes as "[ymin, xmin, ymax, xmax] normalized to 0-1000" (N-AJ76). Qwen2.5-VL: "bounding boxes or points … stable JSON outputs" (N-AJ77) | Frontier models lead the handwriting tests, but hallucinate (§4) |
| **(f) Grounding vendors** | Parsing plus extraction, with a citation per value | ExtractBench (vendor co-authored): commercial VLMs "often truncate record lists on long" documents; LlamaExtract scores highest (N-AJ44, *assumed*) | Reducto: Parse $10, Extract $20 (N-AJ32).<br>LandingAI: $0.01 per credit at about 1.5 credits per typical page, so **about $15**; DPT-3 Verity about $5.50 (N-AJ34) **[our calc]**.<br>Extend: 5 credits per page at $0.0125, so **$62.50** (N-AJ36) **[our calc]**.<br>LlamaCloud: 1,000 credits = $1.25; credits per page not found (N-AJ37).<br>Unstract: LLMWhisperer $1–15, plus **$0.01 per line coordinate lookup**; the platform costs $499 a month for 5,000 pages (N-AJ38) | **Yes, per value:**<br>- Reducto: a box normalised 0–1, confidence "high" or "low"; "A field's citations array can be empty" (N-AJ33);<br>- LandingAI: block-level boxes, word-level ("atomic") on DPT-3 Verity only; grounding costs zero credits (N-AJ35);<br>- Extend: polygon, `referenceText`, `ocrConfidence` (N-AJ36);<br>- LlamaExtract: `bounding_boxes {x,y,w,h}`, but "Turbo citations include page and matching_text only" (N-AJ37);<br>- Unstructured: element-level coordinates only (N-AJ39) | Via their OCR |

### 3.2 Licences, for a commercial SaaS

| Tool | Code licence | Weights licence | Commercial SaaS risk **[our call]** | Label |
|---|---|---|---|---|
| **PyMuPDF** | **AGPL-3.0**, or a commercial licence from Artifex ("If you determine you cannot meet the requirements of the AGPL…") | — | **Avoid**, or buy the licence | *verified* (N-AJ15, N-AJ19; re-checked) |
| pdfplumber, pdfminer.six, Camelot, tabula-java, invoice2data | MIT | — | Fine | *verified* (N-AJ15) |
| pypdfium2 | "Apache-2.0 / BSD-3-Clause"; PDFium itself under "a BSD-style license" | — | Fine | *verified* (N-AJ22) |
| poppler (`pdftotext`) | GPL (the poppler repo page was blocked) | — | Calling the binary as a separate process is common; get legal advice | *assumed* |
| Tesseract, PaddleOCR, docTR, EasyOCR | Apache-2.0 | PaddleOCR-VL weights Apache-2.0 | Fine | *verified* (N-AJ15, N-AJ20) |
| OCRmyPDF | MPL-2.0 | — | Fine. It uses Ghostscript, which is AGPL (*assumed*, memory) | *verified* / *assumed* |
| **Marker, Surya** | Apache-2.0 | **"modified AI Pubs Open Rail-M license (free for research, personal use, and startups under $5M funding/revenue)"** | OK at the start; budget a paid licence later | *verified* (N-AJ16, N-AJ17; Marker re-checked) |
| **MinerU** | "MinerU Open Source License": Apache-2.0, plus a commercial licence needed above "100 million" monthly active users or "USD 20 million" monthly revenue. **An online service "must clearly and prominently indicate" that MinerU is used** | MinerU2.5 weights **AGPL-3.0** | **Avoid the weights** | *verified* (N-AJ18, N-AJ20) |
| **LayoutLMv3** | MIT (the unilm repo) | **CC BY-NC-SA 4.0 (non-commercial)** | **Do not use** | *verified* (N-AJ15, N-AJ20) |
| Docling; Granite-Docling | MIT | Apache-2.0 | Fine | *verified* |
| olmOCR | Apache-2.0 | Apache-2.0 (built on Qwen2.5-VL-7B) | Fine | *verified* |
| DeepSeek-OCR; dots.ocr | MIT | MIT | Fine | *verified* |
| **Qwen2.5-VL** | — | 7B: Apache-2.0.<br>**3B: "FOR NON-COMMERCIAL PURPOSES ONLY"**.<br>72B: Qwen licence (a separate licence above 100M monthly users; a "Built with Qwen" notice if you distribute a model trained on it) | Use 7B; avoid 3B | *verified* (N-AJ20) |
| Qwen3-VL | Apache-2.0 (repo) | not checked | — | *verified* (code) |
| Unstructured | Apache-2.0 | — | Fine | *verified* |
| **Unstract** | **AGPL-3.0** | — | Use the hosted service, or avoid | *verified* |

### 3.3 Benchmarks, and what they say about freight papers

| Benchmark | Numbers | Relevance | Label |
|---|---|---|---|
| **olmOCR-Bench** (1,403 PDFs; made by AI2, olmOCR's own team) | Overall / Tables / Old scans:<br>- olmOCR v0.4.0: 82.4 / 84.9 / 47.7<br>- Chandra: 83.1 / 88.0 / 50.4<br>- PaddleOCR-VL: 80.0 / 84.1 / 37.8<br>- Marker: 76.1 / 72.9 / 33.5<br>- DeepSeek-OCR: 75.7 / 80.2 / 33.3<br>- MinerU 2.5.4: 75.2 / 84.9 / 33.7<br>- Mistral OCR: 72.0 / 60.6 / 29.3 | **Every system scores 29–50% on old scans**, the closest analogue to faxed or rescanned DRs | *verified* (README) |
| **OmniDocBench v1.6** (1,651 pages; run by OpenDataLab, which also makes MinerU) | Overall / Table TEDS:<br>- PaddleOCR-VL-1.6: 96.34 / 94.76<br>- MinerU2.5-Pro: 95.75 / 93.42<br>- Gemini 3 Pro: 92.91 / 89.15<br>- dots.ocr: 90.77 / 87.18<br>- Qwen3-VL-235B: 89.78 / 83.07<br>- GPT-5.2: 86.59 / 82.95<br>- Mistral OCR: 85.66 / 76.78<br>- olmOCR: 85.74 / 83.00<br>- Marker: 78.44 / 65.77 | Papers, books and slides, not invoices | extraction; spot-check before relying on it |
| **IDP Leaderboard v1.5** (Nanonets) | OCR / Table / KIE:<br>- GPT-5.4: 81.0 / 85.3 / 84.4<br>- Gemini-3-Pro: 77.7 / 88.8 / 81.8<br>- Claude Sonnet 4.6: 73.9 / 86.9 / 81.2 | Field extraction on business documents | *assumed* (vendor) |
| **RD-TableBench** (1,000 complex tables, by Reducto) | Reducto 90.2; Azure 82.7; Textract 80.9; GPT-4o 76.0; Google 64.6 | A proxy for rate-agreement tables | *assumed* (vendor) |
| **OCRBench v2** | "most LMMs score below 50 (100 in total)"; weak at fine-grained perception, layout and complex elements | A general warning | *verified* (N-AJ47) |
| **Berghaus et al. 2025** | Invoice fields 96.50% clean, 92.71% scanned (Gemini 2.5 Pro) | The closest public match to invoices | *verified* (AA) |

**Published self-hosting costs:**
- **olmOCR:** "less than $200 USD per million pages" (N-AJ25, *assumed*).
- **DeepSeek-OCR:** "200k+ pages per day (a single A100-40G)" (N-AJ46, *assumed*). At RunPod's A100 rate of $1.59 an hour, that is **about $0.19 per 1,000 pages** **[our calc]**.
- **The catch:** a GPU left running all year costs $13,928 (A100) or $4,292 (L4) **[our calc]**. At our volumes, self-hosting only pays if the GPU runs in short batches.

---

## 4. AJ3: Making extraction trustworthy enough for an audit

### 4.1 Evidence that AI readers invent or "fix" text

| Finding | Source | Label |
|---|---|---|
| On degraded ID cards and **invoices**, models show "overreliance on linguistic priors" and "frequently" produce "hallucinatory content". A fine-tuned 7B model gained "22% absolute improvement in hallucination-free accuracy over GPT-4o" | KIE-HVQA, arXiv 2506.20168 (N-AJ40) | *verified* (abstract) |
| VLMs beat classic OCR on character error rate, yet produced "orthographic normalization", "spurious content generation" and "semantic substitutions". These errors are "invisible to standard metrics" and hit names hardest | arXiv 2607.24077 (N-AJ41) | *verified* (abstract) |
| "several generative models hallucinate plausible but visually unsupported corrections" on handwriting | OmniHandwritingOCR, arXiv 2608.18586 (N-AJ42) | *verified* (abstract) |
| 17 models on 49 real handwritten forms: the best got "around 85%" of fields; the best model on dates still showed "6% hallucination" | arXiv 2604.16504 (N-AJ43) | *verified* (abstract) |
| Over-compressing pages: "at a compression ratio of 20x, the OCR accuracy still remains at about 60%" | DeepSeek-OCR, arXiv 2510.18234 (N-AJ46) | *verified* (abstract) |
| Not only AI: Xerox scanners swapped digits through JBIG2 pattern matching | Kriesel 2013 (N-AJ45) | *verified* |
| Silent "fixing" of totals: **no measured study found**. The papers above show the general tendency | — | not found |

### 4.2 Validation techniques

| Technique | Evidence | What it catches, and what it misses **[our call]** |
|---|---|---|
| **The bill adds up** | 99/101 ABF bills to the cent; the 2 misses were our parser (N-PA01) | Catches misread amounts. Misses weight, class, PRO and dates |
| **Each value is found on the page** | Reducto returns an empty citation when a value is "inferred" (N-AJ33). ExtractBench scores "word-level grounding F1" (N-AJ44). Claude cites pages only (N-AJ02) | Make the model cite word IDs from our own text or OCR layer, and reject any value whose characters aren't on the page |
| **Two independent readings agree** | Voting across repeat scans removed "between 20 and 50%" of errors; aligning five engines gave a "24.6% relative improvement" (N-AJ84, *assumed*) | Text layer vs cloud OCR vs LLM. When they disagree, a person decides |
| **Confidence scores** | Azure: "0.95 … likely correct 19 out of 20 times"; read and field confidence are separate; barcode confidence is "hard-coded … as 1" (N-AJ48, N-AJ50). Textract gives confidence per field (N-AJ53) | Use them for routing only, calibrated on our own documents |
| **Format checks** | XPO PRO "XXX-XXXXXC": the check digit is the remainder of the first 8 digits ÷ 7 (N-AJ54; re-checked). GS1 BOL: 17 digits with a mod-10 check; the SCAC is four letters, padded with a dash in the barcode (N-AJ60). Saia "MOD 7", SEFL "MOD 11" (snippet, *assumed*). NMFTA's SCAC lookup costs $607 a year (N-AJ56) | **XPO's mod 7 misses digit swaps that differ by 7 (0↔7, 2↔9): 6 of 90, or 6.7%, of random single-digit errors** **[our calc]**. GS1 mod 10 catches every single-digit error but misses 11% of adjacent swaps (those differing by 5) **[our calc]** |
| **Checks across documents** | Field map in AC §8 | Weight, pieces, BOL number and dates against the BOL and the DR |
| **A person reviews** | AWS A2I costs $0.03 per page reviewed (N-AA65). Pando suggests "5–15% … manual review" to start (N-AJ65, *assumed*). **The practice audit found 58–61% needing a document or judgement** (PA §3.1) | Design the screen for exceptions being common |

### 4.3 What a wrong claim costs

- **ODFL's tariff:**
  - "a charge of $50.00 on settled overcharge claims that were through no fault of Carrier";
  - claims are "deemed closed 30 days after the date of the initial ruling";
  - no new claim may be filed on a closed invoice (N-T17, *verified* in check T).
- **TForce:** "Only the payer of the original freight charges can file an overcharge claim", within 180 days (N-AJ57, *verified*).
- **Central Freight v. Amazon:** the carrier sued after a $2.39M audit demand, which was cut to $1.30M by the 18-month claim window (N-AC10, *assumed*: one side's account).
- **Exist v. SEFL:** the shipper's worksheet ignored the agreement's general-rate-increase clause, and SEFL moved to dismiss (N-AC03).
- **Reading [our call]:** a misread figure in a dispute can forfeit the claim for good, not just waste time. A person must verify every disputed figure against the document image.

---

## 5. AJ4: Splitting and classifying pages

| Approach | Price | Facts | Label |
|---|---|---|---|
| **Azure custom classifier** | $3 per 1,000 pages (AA) | Works "one page at a time"; `splitMode` auto, none or perPage (default now `none`); needs "two distinct classes and a minimum of five document samples per class"; up to 1,000 classes; returns a page range and a confidence per document; recommends an "other" class | *verified* (N-AJ49) |
| Google custom splitter/classifier | $5 per 1,000 (up to 1M), then $3 | — | *assumed* (N-AJ31) |
| Textract Analyze Lending | $0.07 a page | Built for mortgage packets; not a fit **[our call]** | *verified* (N-AJ52) |
| LandingAI Classify | 0.5 credits a page, about $5 per 1,000 | — | **[our calc]** (N-AJ35) |
| LLM classifier on page text | Haiku 4.5 at about 1,500 tokens a page: about $2 per 1,000. Gemini Flash-Lite at 258 tokens: about $0.03 | — | **[our calc]** |
| Heuristics | Free | Keywords ("DELIVERY RECEIPT", "BILL OF LADING", "CORRECTED INVOICE", "BALANCE DUE", "INSPECTION"), the PRO/BOL number on each page, barcodes, FedEx's file names | **[our call]** |

**Accuracy evidence:**
- **TABME++ (2024):** a fine-tuned Mistral-7B scored page F1 **0.987** and document F1 **0.967**, and "perfectly segmented 80% of test streams". LayoutLMv3 scored document F1 **0.572**, with only 4.8% of streams entirely right (N-AJ58, *verified*).
- **DocSplit (2026, AWS authors):** Claude Sonnet 4.5 scored 0.925 on packets with pages in order and 0.911 with pages shuffled. With every page, split and order required to be right, scores fell to **0.50–0.80** (N-AJ59, *verified*).
- **Reading [our call]:** heuristics first, a model second, and a page strip a person can fix when the split is unclear.

---

## 6. AJ5: Barcodes

- **GS1 US BOL Guideline R4.0 (2015)** (N-AJ60, *verified*):
  - "The implementation of a barcode for the above mentioned data is intended for carrier usage and is **optional**."
  - "This space can also be used for the carrier proprietary PRO number sticker."
  - The barcode must be GS1-128: AI 402 for the BOL number, 9012K for the SCAC/PRO.
  - "The SCAC and/or Pro# does not have a check digit routine."
- **Where the PRO label goes:** Estes: "Estes PRO label is placed here (by driver)" (N-AJ61, *verified*). ABF: "PLACE PRO LABEL HERE" (snippet, *assumed*).
- **What the label carries:** PRO labels carry a Code 128 barcode of the PRO (template vendor, N-AJ64, *assumed*). Barcodes on actual invoices and DRs were **not verified**.
- **Decoders** (all *verified*):
  - zxing-cpp (Apache-2.0): reads Code39, Code93, Code128, ITF, Codabar, DataMatrix, PDF417 and QR, with Python bindings (N-AJ63);
  - pyzbar (MIT) on ZBar (LGPL-2.1) (N-AJ15);
  - Azure's barcode add-on is "Free" and reads Code 39, 93 and 128, ITF, PDF417, QR and Data Matrix (N-AJ50).
- **Reliability:** barcode misreads are about 1 per million characters, against 1 in 300 for keying (N-AJ64, *assumed*).
- **Reading [our call]:** a decoded barcode with a valid check digit is the strongest PRO key we can get. But it is missing on some pages, and fax resolution can wipe out a 1D barcode, so cross-check it against the text or OCR.

---

## 7. AJ6: Rate agreements and tariffs

- **What an agreement holds, from the local files:**
  - **SEFL:** 3 dated versions; base rate SEFL-0550; floors of $88.50 then $97; zone discounts of 75–92.5%; FAK 70 for classes 77.5–175; per-pallet rates by state, with exclusions; "Subject to general rate increase: YES" (N-AC03).
  - **YRC:** an accessorial schedule, an FAK table and a weekly fuel table (N-AC05).
- **How the industry loads rates:**
  - Contracts are "loaded into a Transportation Management System (TMS)" (N-AJ67, *assumed*).
  - Trax claims "98% extraction accuracy", including "multi-page carrier agreements", with "Targeted Human Review" (N-AJ66, *assumed*).
  - Pando claims its "Pi" agent "extracts rate cards … with 100% accuracy" (N-AJ67, *assumed*).
  - No contract-extraction claim was found for Loop.
- **Table accuracy:** about 65–95 on TEDS-type and table scores (§3.3).
- **Hours to load and verify one agreement: not found** (also not found by AA).
- **Reading [our call]:**
  - an AI model drafts the loaded schedule;
  - a person checks every number against the page image;
  - the load is then back-tested against the customer's own bills (the ABF bills alone show the 89.5% discount and the $180 floor);
  - estimate about 1–3 hours per carrier version.
- **Carrier tariffs:**
  - Versions sit in dated files: ABF111-AS-02-03-2025, ABF111-AU-06-22-2026, Saia_170D_10012025, CNWY_199-AK.1 (N-T20–N-T25).
  - The 2025 ABF version was still downloadable in September 2026 (N-PA03).
  - A 2024 Saia version is still listed online (N-AJ68, *assumed*).
  - **ABF's 2024 table was not found** (PA §8), and the Wayback Machine was blocked here.

---

## 8. AJ7: Highlighting on the document

| Product | What the screen does | Label |
|---|---|---|
| **Rossum** | "Clicking on an extracted value redirects you to the associated field"; hover a box to see its field. **Yellow** = extracted but unreviewed; **green** = checked by a user; **red** = blocks confirmation. Hold ALT to see suggested boxes | *verified* (N-AJ69) |
| Azure Document Intelligence Studio | A test tool with "interactive visualizations" of fields | *verified* (N-AJ51) |
| LandingAI, Reducto, Extend, LlamaExtract | A box per value through their APIs (§3.1) | *verified* |
| Unstract | Source highlighting at $0.01 per line lookup | *verified* (N-AJ38) |
| Docsumo, Nanonets, Hyperscience | Clicking a field "highlights its source line" (Docsumo); per-field boxes (Nanonets); audit trails (Hyperscience) | *assumed* (N-AJ70) |
| Stampli, HubTran, the Textract console | Not documented, or not checked | — |

**Building blocks for our own viewer:**
- **Viewer:** PDF.js (Apache-2.0); react-pdf (MIT); react-pdf-highlighter-extended (MIT). The last supports "text and rectangular highlights", stores positions "independent of the viewport", and has `scrollToHighlight` (N-AJ21).
- **Writing marks into a PDF for a dispute:** **pypdf (BSD-3) adds real Highlight annotations** (N-AJ23). **pdf-lib (MIT) has no annotation support**; it can only draw rectangles onto the page content (N-AJ72). pikepdf is MPL-2.0.
- **Coordinates from born-digital pages:** poppler `-tsv` (N-AJ24). The project's own example uses `-bbox-layout`: `research/img/abf_150235531_highlights.png`.
- **Commercial SDKs:** Apryse and Nutrient sell by quote only. Vendr reports median contracts of about $24k and $31k a year (N-AJ71, *assumed*).

---

## 9. AJ8: What reading costs per customer [our calc]

**Assumptions [our call]:**
- **Invoices per $1,000 of spend:** k = 1.5 (the model's central figure) and 2.21 (the real ABF account).
- **Pages per packet:** 1–2 invoice pages plus 1–3 supporting pages, so 2 / 3.5 / 5 (low / central / high).
- **Fee:** scaled from $3,900 at $2M, i.e. $1.95 per $1,000 of spend: **$2,925 at $1.5M and $5,850 at $3M**. *(Coordinator's note: the model's exact figure is $1.97 per $1,000, giving $2,953 and $5,906. The shares below fall by about 1%.)*
- **LLM costs:** AA's typical 4-page packet. Opus 5.5 is recomputed at $4/$20, giving $0.134 a packet; Sonnet 5.5 is priced the same as Sonnet 5, giving $0.067.

**Pages a year (low – central – high):**
- A ($1.5M, k=1.5): 4,500 – 7,875 – 11,250
- B ($1.5M, k=2.21): 6,630 – 11,603 – 16,575
- C ($3M, k=1.5): 9,000 – 15,750 – 22,500
- D ($3M, k=2.21): 13,260 – 23,205 – 33,150

**Cost a year, central pages (share of the fee):**

| Route | A | B | C | D |
|---|---|---|---|---|
| Text layer only (invoice pages) | $0 | $0 | $0 | $0 |
| Text layer for invoices + cloud OCR for supporting pages | $6.75 | $9.95 | $13.50 | $19.89 |
| Self-hosted open-source OCR/VLM (about $0.20 per 1,000) | $1.58 | $2.32 | $3.15 | $4.64 |
| **Cloud OCR, $1.50 per 1,000** | **$11.81 (0.4%)** | $17.40 (0.6%) | $23.63 (0.4%) | **$34.81 (0.6%)** |
| Document-AI invoice model, $10 per 1,000 | $78.75 (2.7%) | $116.03 (4.0%) | $157.50 (2.7%) | $232.05 (4.0%) |
| Gemini 2.5 Flash pass | $13.28 | $19.56 | $26.55 | $39.12 |
| Claude Haiku 4.5 pass | $65.25 | $96.14 | $130.50 | $192.27 |
| **Claude Sonnet 5.5 pass** | **$150.75 (5.2%)** | $222.11 (7.6%) | $301.50 (5.2%) | **$444.21 (7.6%)** |
| Claude Opus 5.5 pass | $301.50 (10.3%) | $444.21 (15.2%) | $603.00 (10.3%) | $888.42 (15.2%) |
| Grounding vendor, $30–62.50 per 1,000 | $236–492 | $348–725 | $473–984 | $696–1,450 |
| **Human, 15% of packets, US ($3.68 each)** | **$1,242 (42%)** | $1,829 (63%) | $2,483 (42%) | **$3,659 (63%)** |
| Human, 15%, offshore ($1.20 each) | $405 (14%) | $597 (20%) | $810 (14%) | $1,193 (20%) |
| **Human, 58% of packets, US** | **$4,801 (164%)** | $7,074 (242%) | $9,602 (164%) | **$14,147 (242%)** |
| Human, 58%, offshore | $1,566 (54%) | $2,307 (79%) | $3,132 (54%) | $4,614 (79%) |

**Reading [our call]:**
- **OCR is not "pricey" here.** One 6-minute US exception review ($3.68) costs as much as any of these:
  - cloud OCR of **2,453 pages** (about 700 packets);
  - **55 Sonnet 5.5 packet reads**;
  - **105 document-AI invoice packets**.
- **What drives cost, in order:**
  1. The share of packets a person must touch × minutes × wage.
  2. Invoices per dollar of spend (LTL-heavy accounts cost more).
  3. Engineering per carrier layout, and rate-agreement loading.
  4. **Platform minimums:** Rossum $18k a year, Sensible $5,388, Unstract $5,988. Each is more than the whole $3,900 fee from a $2M customer.
  5. Model choice: Opus costs about 23× Gemini Flash, but is still small next to people.
- **Pages per packet** matter only for services priced per page.

---

## 10. Design implications

1. **A layered pipeline [our call]:**
   - EDI, CSV or XML first;
   - otherwise the text layer with word coordinates (pdfplumber or pypdfium2);
   - for scans, OCR with word boxes (Azure Read or Textract);
   - an LLM only to map words to fields;
   - all math in deterministic code;
   - exceptions to a person on the highlight screen.
2. **No number without a location [our call]:** every figure must point to word IDs in our own text or OCR layer, and its characters must match. Otherwise it becomes an exception.
3. **Never let AI decide money [our call]:** re-rating, fuel, discounts and minimums run in code. The AI drafts the dispute text, and a person approves every dispute.
4. **Two agreeing sources on any disputed figure [our call]:** text layer vs OCR, or OCR vs LLM. Confidence scores are for routing only.
5. **Key on PRO + BOL [our call]:**
   - check the PRO's check digit (XPO mod 7);
   - read barcodes when present;
   - keep a version per PRO;
   - keep both the ship date and the bill date.
6. **Prefer carrier data feeds and document portals [our call]:**
   - enrol customers in XPO's CSV/XML digests or in EDI;
   - fetch DRs and W&R certificates as the customer's agent through ODFL, R+L, TForce and XPO.
7. **Build vs buy [our call]:**
   - build the text-layer parsing, the rule engine and the review screen;
   - buy OCR pay-per-page;
   - avoid monthly-minimum platforms at the start;
   - pilot a grounding vendor only on scans.
8. **Licences [our call]:**
   - stay on MIT, Apache or BSD tools;
   - avoid PyMuPDF and Unstract (AGPL), MinerU2.5 weights, LayoutLMv3 and Qwen2.5-VL-3B;
   - budget for Marker or Surya weights once over $5M.
9. **The review screen [our call]:**
   - show the page image with coloured boxes: green = checked, amber = unsure, red = discrepancy;
   - put the contract clause and the expected value side by side;
   - clicking a field jumps to its box;
   - export the PDF with real highlights for the dispute (pypdf).
10. **Handwriting [our call]:** detect and show it, but never resolve it automatically.
11. **Evidence integrity [our call]:** keep the original files and their fingerprints, and never re-compress scans with lossy methods.
12. **Rate loading [our call]:**
    - an LLM drafts;
    - a person checks;
    - back-test against the customer's own bills;
    - store every version with its effective dates.
13. **Measure from the first customer [our call]:** accuracy by carrier, the share of exceptions, and minutes per exception. These numbers decide the margins.

---

## 11. Notes on method

- The OmniDocBench and olmOCR-Bench numbers came through the fetch tool's extract. Spot-check them before quoting externally.
- Prices are as shown on 2026-10-03. Claude prices that are new since AA: Opus 5.5 $4/$20 (batch $2/$10) and Sonnet 5.5 $2/$10. The other AA prices are unchanged where re-checked (Textract).

---

## 12. Could not access, or not found

**Blocked:**
- the Google Document AI pricing page (truncated again; a snippet was used);
- the Wayback Machine (the fetch tool cannot reach it);
- the poppler repo page (bot challenge);
- the AWS Textract + A2I docs (empty page);
- the XPO tariff library (did not render);
- RD-TableBench scores (shown only as an image; Reducto's guide snippet was used).

**Not found:**
- PRO check-digit rules published by ODFL, Estes, ABF, R+L, FedEx Freight, Saia or SEFL. Only XPO publishes its own; the Saia and SEFL entries come from a snippet.
- Carriers' reactions to bad audit claims, beyond tariff terms and two lawsuits.
- The hours needed to load a rate agreement.
- LlamaParse credits per page; Mistral's batch price; Unstructured's pricing.
- Barcodes on real invoices and DRs. Checking would have meant downloading court PDFs.
- Handwriting accuracy on BOLs and DRs specifically.
- The fine detail of MinerU's output boxes.
- The Stampli, HubTran and Textract review screens.

**Searches tried for the gaps:**
- PRO check-digit modulus, by carrier;
- carrier responses to invalid or "frivolous" audit claims;
- archives of superseded rules tariffs;
- rate loading by freight-audit firms;
- handwritten-form OCR benchmarks;
- HubTran OCR document matching.

---

## 13. Sources

All accessed 2026-10-03.

| ID | Title / publisher | Date on page | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AJ01 | Anthropic, Claude API pricing | none | https://platform.claude.com/docs/en/about-claude/pricing | full (re-checked) | Opus 5.5 $4/$20; batch; cache |
| N-AJ02 | Anthropic API reference bundled with Claude Code (claude-api skill) | cached 2026-09-25 | local skill | full | Citations `page_location`; no citations with structured output; PDF limits |
| N-AJ03 | ODFL, Invoices & Claims | none | https://www.odfl.com/us/en/resources/invoices-claims.html | extraction | Email invoices |
| N-AJ04 | Estes, Paperless Invoicing (+ snippet) | none | https://www.estes-express.com/resources/paperless | extraction / snippet | Frequencies; BOL/DR option |
| N-AJ05 | XPO, Electronic Invoice Presentment | none | http://www.xpo.com/help-center/other-tools/electronic-invoice-presentment-eip/ | extraction | CSV/PDF/XML, daily/weekly |
| N-AJ06 | XPO, Document Finder | none | https://www.xpo.com/help-center/document-finder/ | extraction | Document types |
| N-AJ07 | Saia, Billing and Payment Options PDF | none | https://assets.ctfassets.net/kjv8gs2ccggb/5gWWPZxzAorrUK64ikFbJ6/43fc73def6e4125e607f1abe04afcf8a/SaiaBillingAndPayment_Options.pdf | full (image) | E-Billing with backup |
| N-AJ08 | SEFL, Internet Invoicing | none | https://www.sefl.com/SeflInvoice/invoiceSignup/invoice.jsp | extraction | Abbreviated PDF; third parties |
| N-AJ09 | FedEx, EDI Invoicing and Remittance Overview | Jan 2020 | https://www.fedex.com/content/dam/fedex/us-united-states/services/Elec_Inv_Remit_Overview.pdf | full pp. 1–8 (images) | PDF Image Delivery |
| N-AJ10 | FedEx Freight Billing Online | none | https://www.fedexfreight.com/en-us/manage-account/billing | extraction | One-year availability |
| N-AJ11 | AAA Cooper Document Downloads; R+L resources | none | https://www.aaacooper.com/Document-Downloads | snippet | Email invoicing form |
| N-AJ12 | FreightWaves Checkpoint, AtoB, TruckSmarter (factoring) | 2026 | https://www.freightwaves.com/checkpoint/factoring-companies-freight-brokers/ | snippet | Packet contents |
| N-AJ13 | Extend, Docsumo, imagetotable (BOL/POD OCR) | 2026 | https://www.extend.ai/resources/best-bills-lading-ocr-tools | snippet | POD difficulty |
| N-AJ14 | DAT / HubTran release | none | https://www.dat.com/company/news-events/news-releases/dat-keypoint-integrates-hubtran-to-automate-freight-brokers-back-office-operations | snippet | Matching and exceptions |
| N-AJ15 | GitHub API, repository licences (3 queries) | 2026-10-03 | https://api.github.com/search/repositories | JSON extraction | Licence IDs |
| N-AJ16 | Datalab, Marker README | current | https://raw.githubusercontent.com/datalab-to/marker/master/README.md | extraction (re-checked) | Licence; claims |
| N-AJ17 | Datalab, Surya README | current | https://raw.githubusercontent.com/datalab-to/surya/master/README.md | extraction | Licence; line boxes |
| N-AJ18 | MinerU LICENSE.md | © 2026 | https://raw.githubusercontent.com/opendatalab/MinerU/master/LICENSE.md | extraction | Thresholds; attribution |
| N-AJ19 | PyMuPDF, About / Licence | current | https://pymupdf.readthedocs.io/en/latest/about.html | extraction (re-checked) | AGPL or commercial |
| N-AJ20 | Hugging Face model API and cards: dots.ocr, LayoutLMv3, Qwen2.5-VL 3B/7B/72B and licence files, PaddleOCR-VL, olmOCR-2, DeepSeek-OCR, MinerU2.5, Granite-Docling | 2024–2026 | https://huggingface.co/api/models/… | extraction | Weights licences |
| N-AJ21 | react-pdf-highlighter-extended (API + README) | 2024-11-22 | https://github.com/DanielArnould/react-pdf-highlighter-extended | extraction | MIT; features |
| N-AJ22 | pypdfium2 README | current | https://raw.githubusercontent.com/pypdfium2-team/pypdfium2/main/README.md | extraction | Licence |
| N-AJ23 | pypdf licence; annotation docs | current | https://pypdf.readthedocs.io/en/stable/user/adding-pdf-annotations.html | extraction | BSD-3; Highlight annotation |
| N-AJ24 | poppler home; pdftotext(1) man page | 2026-09-03; v26.01.0 | https://poppler.freedesktop.org/ ; https://manpages.debian.org/testing/poppler-utils/pdftotext.1.en.html | extraction | -bbox, -tsv |
| N-AJ25 | AI2, olmOCR README | current | https://raw.githubusercontent.com/allenai/olmocr/main/README.md | extraction | Benchmark; cost; no boxes |
| N-AJ26 | OmniDocBench README | v1.6 | https://raw.githubusercontent.com/opendatalab/OmniDocBench/main/README.md | extraction | Scores |
| N-AJ27 | IDP Leaderboard (Nanonets) | v1.5 | https://idp-leaderboard.org/ | extraction | Scores |
| N-AJ28 | Reducto, RD-TableBench; guide snippet | 2024-11-04 | https://reducto.ai/blog/rd-tablebench | extraction / snippet | Method; scores |
| N-AJ29 | Mistral API pricing | none | https://mistral.ai/pricing/api | extraction (×2) | OCR 4.1 $4; Document AI $5 |
| N-AJ30 | Mistral OCR documentation | current | https://docs.mistral.ai/capabilities/document_ai/basic_ocr/ | extraction | Block boxes; word confidence |
| N-AJ31 | Google Document AI pricing (search) | 2026 | https://cloud.google.com/document-ai/pricing | snippet | $1.50 / $10 / $5 |
| N-AJ32 | Reducto pricing | none | https://reducto.ai/pricing | extraction | $10 / $20 per 1,000 |
| N-AJ33 | Reducto, Citations docs | current | https://docs.reducto.ai/configs/extract/citations.md | extraction | Box per value |
| N-AJ34 | LandingAI pricing | none | https://landing.ai/pricing | extraction | Credits |
| N-AJ35 | LandingAI, Ground; Credit Consumption | current | https://docs.landing.ai/dpt3/ground.md ; https://docs.landing.ai/ade/ade-credit-consumption.md | extraction | Box levels; credit rates |
| N-AJ36 | Extend pricing; extraction response format | none | https://www.extend.ai/pricing ; https://docs.extend.ai/extraction/response-format.md | extraction | Credits; polygons |
| N-AJ37 | LlamaIndex pricing; Extract response format | current | https://www.llamaindex.ai/pricing ; https://developers.llamaindex.ai/llamaparse/extract/guides/response-format/ | extraction | Credits; boxes |
| N-AJ38 | Unstract pricing | none | https://unstract.com/pricing/ | extraction | Plans; highlight price |
| N-AJ39 | Unstructured, document elements | current | https://docs.unstructured.io/api-reference/partition/document-elements | extraction | Coordinates |
| N-AJ40 | He et al., KIE-HVQA, arXiv 2506.20168 | 2025-06/09 | https://arxiv.org/abs/2506.20168 | abstract | Hallucination |
| N-AJ41 | Gardella et al., arXiv 2607.24077 | 2026-07/09 | https://arxiv.org/abs/2607.24077 | abstract | Failure types |
| N-AJ42 | Guo et al., OmniHandwritingOCR, arXiv 2608.18586 | 2026-08-19 | https://arxiv.org/abs/2608.18586 | abstract | Plausible corrections |
| N-AJ43 | Pather et al., arXiv 2604.16504 | 2026-04-14 | https://arxiv.org/abs/2604.16504 | abstract | 85% of fields; 6% |
| N-AJ44 | Zhang et al., ExtractBench, arXiv 2607.29677 | 2026-07-31 | https://arxiv.org/abs/2607.29677 | abstract | Grounding metric |
| N-AJ45 | Kriesel, Xerox JBIG2 | 2013-08-02 | https://www.dkriesel.com/en/blog/2013/0802_xerox-workcentres_are_switching_written_numbers_when_scanning | extraction | Digit swaps |
| N-AJ46 | DeepSeek-OCR, arXiv 2510.18234; README | 2025-10-21 | https://arxiv.org/abs/2510.18234 | abstract / extraction | Throughput; compression |
| N-AJ47 | OCRBench v2, arXiv 2501.00321 | 2024-12 / 2025-06 | https://arxiv.org/abs/2501.00321 | abstract | Below 50/100 |
| N-AJ48 | Microsoft Learn, accuracy and confidence | 2026-04-08 | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/accuracy-confidence | full | Confidence guidance |
| N-AJ49 | Microsoft Learn, custom classifier | 2026-08-15 | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/train/custom-classifier | full | splitMode; limits |
| N-AJ50 | Microsoft Learn, add-on capabilities | 2026-08-15 | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/add-on-capabilities | full | Barcodes free; searchable PDF |
| N-AJ51 | Microsoft Learn, Document Intelligence Studio | 2026-04-09 | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/studio-overview | full | Visualisation |
| N-AJ52 | AWS Textract pricing | current | https://aws.amazon.com/textract/pricing/ | extraction | Prices |
| N-AJ53 | AWS, AnalyzeExpense response objects | current | https://docs.aws.amazon.com/textract/latest/dg/expensedocuments.html | full | Geometry and confidence |
| N-AJ54 | XPO, PRO Number Check-Digit | none | http://www.xpo.com/help-center/resources/pro-number/ | extraction (re-checked) | Mod 7 |
| N-AJ55 | Check-digit snippets; Shipwell | 2024-05-01 | https://intercom.help/shipwell/en/articles/9268914-ltl-pickup-pro-numbers | snippet / extraction | Mod 7/10/11 |
| N-AJ56 | NMFTA, SCAC Verified pricing | current | https://scac.nmfta.org/pricing | extraction | $607 a year |
| N-AJ57 | TForce, Overcharge Claim Information | current | https://www.tforcefreight.com/ltl/apps/OverchargeClaimInformation | extraction | Payer only; 180 days |
| N-AJ58 | Heidenreich et al., arXiv 2408.11981 | 2024-08-21 | https://arxiv.org/html/2408.11981 | extraction | TABME++ numbers |
| N-AJ59 | Islam et al., DocSplit, arXiv 2602.15958 | 2026-02-17 | https://arxiv.org/html/2602.15958v1 | extraction | Scores |
| N-AJ60 | GS1 US, Bill of Lading Guideline R4.0 | 2015-04-06 | https://documents.gs1us.org/adobe/assets/deliver/urn:aaid:aem:86fea182-579d-49bd-8897-72a5613bc1d8/Guideline-Bill-of-Lading-BOL.pdf | pp. 2–5, 16–17, 29 (images) | Barcode rules |
| N-AJ61 | Estes, BOL instructions | none | https://www.estes-express.com/resources/bol-instructions | extraction | PRO label applied by the driver |
| N-AJ62 | ArcBest BOL template titles | 2023–2025 | https://arcb.com/sites/www/files/2025-11/Bill-of-Lading-ABF-TIME-CRITICAL-080425.pdf | snippet | PRO label text |
| N-AJ63 | zxing-cpp README | current | https://raw.githubusercontent.com/zxing-cpp/zxing-cpp/master/README.md | extraction | Formats |
| N-AJ64 | Morovia knowledge base; Cleverence label template | none | https://www.morovia.com/kb/Advantages-Bar-Codes-10613.html | snippet | Error rates; Code 128 |
| N-AJ65 | Pando, match-rate benchmark | 2026-09-17 | https://pando.ai/blogs/freight-audit-automation-a-realistic-match-rate-benchmark | extraction | 5–15% review |
| N-AJ66 | Trax, AI Extractor | none | https://www.traxtech.com/products/ai-extractor | extraction | 98% claim |
| N-AJ67 | Pando Pi; ShipTLI; Warp (rate loading) | 2026 | https://pando.ai/product/ai-agents/pi/ai-freight-audit-pay-specialist/ | snippet | Claims |
| N-AJ68 | Saia 170-D, 2024-10-21 version | 2024 | https://assets.ctfassets.net/kjv8gs2ccggb/3Y5vAsxznsXornATV1AG5D/6b84a348d1a24f4338f8f954633e28de/Saia_170D_10212024.pdf | snippet | Old version still online |
| N-AJ69 | Rossum, Interactive Bounding Boxes | 2025-03-06 | https://knowledge-base.rossum.ai/docs/interactive-bounding-boxes-in-rossum | extraction | Screen behaviour |
| N-AJ70 | Docsumo, Nanonets, Hyperscience | 2026 | https://www.docsumo.com/blog/the-best-intelligent-document-processing-software | snippet | Review screens |
| N-AJ71 | Vendr and others, Apryse and Nutrient prices | 2026 | https://www.vendr.com/marketplace/apryse | snippet | Median prices |
| N-AJ72 | pdf-lib README | current | https://raw.githubusercontent.com/Hopding/pdf-lib/master/README.md | extraction | No annotations |
| N-AJ73 | pdfplumber README | current | https://raw.githubusercontent.com/jsvine/pdfplumber/stable/README.md | extraction | Coordinates |
| N-AJ74 | Tesseract command-line usage | current | https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html | extraction | TSV / hOCR |
| N-AJ75 | PaddleOCR README | v3.7.0 | https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md | extraction | Claims; licence |
| N-AJ76 | Gemini, image understanding | current | https://ai.google.dev/gemini-api/docs/image-understanding | extraction | Box format |
| N-AJ77 | Qwen2.5-VL-7B model card | 2025 | https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct | extraction | Localisation |
| N-AJ78 | dots.ocr README (now dots.mocr) | current | https://raw.githubusercontent.com/rednote-hilab/dots.ocr/master/README.md | extraction | Element boxes |
| N-AJ79 | MinerU output files | current | https://opendatalab.github.io/MinerU/reference/output_files/ | extraction | Files produced |
| N-AJ80 | invoice2data repo tree | current | https://api.github.com/repos/invoice-x/invoice2data/git/trees/master?recursive=1 | extraction (truncated) | Template names |
| N-AJ81 | Sensible configuration library listings; pricing | current | https://api.github.com/repos/sensible-hq/sensible-configuration-library/contents/templates/Logistics ; https://www.sensible.so/pricing | extraction | 18 rate-confirmation configs; prices |
| N-AJ82 | Docparser pricing; BOL template | current | https://docparser.com/pricing/ | extraction / snippet | Credits |
| N-AJ83 | RunPod pricing | 2026-09-27 | https://www.runpod.io/pricing | extraction | GPU hourly rates |
| N-AJ84 | Lopresti & Zhou; Lund et al. (OCR voting) | 1997; 2011 | https://www.semanticscholar.org/paper/Using-Consensus-Sequence-Voting-to-Correct-OCR-Lopresti-Zhou/e17d8b64d137e904fa611b7be082090f5cbe0625 | snippet | Error reductions |
| N-AJ85 | Businessware Tech; Codesota (handwriting) | 2025–26 | https://www.businesswaretech.com/blog/research-best-ai-services-for-automatic-invoice-processing | snippet | Context only |
| N-AJ86 | Digiparser; Unstract "PDF hell" | 2026 | https://www.digiparser.com/blog/pdf-to-text | snippet | Reading-order traps |

Earlier IDs re-used: N-PA01–N-PA03; N-AC02–N-AC17; N-T17–N-T29; N-AA02, N-AA03, N-AA09, N-AA12–N-AA18, N-AA65.
