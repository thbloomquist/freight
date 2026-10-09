# catalogue.csv — field definitions

One row per original file under `sources/`. Derived files (`derived/`) and tools (`_tools/`) are not catalogued.

| Field | Meaning | Values |
|---|---|---|
| `file_id` | `<set_id>-<running number>` | e.g. `02-004` |
| `set_id`, `set_name` | the folder under `sources/` | `01` … |
| `path` | path relative to `data/` | |
| `source_kind` | where it came from | `court-recap` (CourtListener RECAP, free copies of PACER filings), `claims-agent` (Kroll, Stretto, Epiq, Omni, Verita, Donlin Recano registers), `carrier-site`, `gov`, `github`, `archive-org`, `press`, `other` |
| `case_or_docket` | case name and number, if a court or claims record | |
| `doc_number` | docket entry or claim number | |
| `url` | the exact download URL. `UNRESOLVED` = the file was rescued from an earlier session's scratchpad and its URL is still to be confirmed | |
| `retrieved_on` | date the copy in `data/` was made | ISO date |
| `retrieved_by` | `round0-rescue` (copied from an earlier session's download), `agent-A`, `agent-B`, `agent-C`, `coordinator` | |
| `sha256`, `bytes`, `pages` | from `sha256sum` and `pdfinfo` | |
| `text_layer` | does `pdftotext` return real body text? `yes` = all three sampled places (pp. 1-3, middle, last) give more than 40 words after the court stamp is removed; `partial` = some do; `no` = none; `na` = not a PDF | |
| `ocr_available` | is there a `derived/ocr/` text for it | yes / no |
| `carriers` | carriers whose documents appear | pipe-separated |
| `parties` | companies only, never individuals | |
| `doc_types` | what is inside, pipe-separated | `invoice_ltl, invoice_tl, invoice_broker, corrected_invoice, statement, bol, delivery_receipt, rate_confirmation, pricing_agreement, contract, rules_tariff, fuel_table, accessorial_schedule, wi_certificate, claim_form, dispute_letter, carrier_response, credit_memo, audit_worksheet, edi_guide, edi_sample, complaint, opinion, gov_audit_report, payment_list, form_template, other` |
| `discrepancy_checks` | the audit checks the file gives evidence for, by the IDs in `research/s5_check_AK_c09_audit_workflow_and_products.md` §3.2 | A1 math · A2 duplicate · A3 paid twice via 3PL · A4 corrected/balance-due bill · A5 wrong payer · A6 no matching shipment · A7 reference for contract/quote · B1 agreement version · B2 base rate × discount · B3 minimum charge · B4 FAK/class · B5 quote honoured · B6 TL linehaul vs rate con · B7 TL mileage · B8 fuel level · B9 fuel base · C1 reweigh/reclass · C2 correction fee · D1 accessorial priced per schedule · D2 accessorial ordered/performed · D3 detention · D4 stop-offs · D5 TONU · D6 layover · D7 lumper · E1 guaranteed-service refund · E2 service-failure credit · F1 late fees · F2 GL coding · F3 accrual · F4 rebilled · G1 shipper dispute window · G2 carrier response deadline |
| `real_or_template` | `real` = a document from an actual shipment, contract or dispute; `template` = a blank form, a guide, a tariff or a specification; `mixed` | |
| `mode` | `LTL`, `TL`, `both`, `na` | |
| `date_start`, `date_end` | shipment or document dates covered | |
| `in_segment` | does the shipper look like C-09's target (a mid-sized shipper buying roughly $0.5-10M of trucking a year)? | yes / possibly / no / unknown / na |
| `format_notes` | layout, scan quality, handwriting; the word counts behind `text_layer` | |
| `cited_in` | the research file and source ID that first used it | |
| `notes` | free text | |
| `verify_status`, `verify_note` | set by the verification pass (`research/s5_check_AT_adversarial.md`) | unverified / verified / narrowed / wrong |
