# S5 check AK: how freight bills are checked today, the auditors' rule set, and what the C-09 audit machine must do

- **What this is:** desk research for card C-09. The founders decided on 2026-10-03 that the **first version is an audit machine only**, with no carrier payments, and asked:
  - "How are these being identified currently?"
  - "What else must this software do?"
  - how to alert people and make the system easy to use.

  It covers AK1-AK6. It builds on these earlier checks without redoing them:
  - `s5_check_Z_c09_voice.md` §2, §7, §10.1, §14;
  - `s5_check_Y_c09_reach.md` §1;
  - `s5_check_T_ltl_carrier_position.md` §1, §3, §4, §6;
  - `s5_practice_audit_public_invoices.md`;
  - `s5_check_AC_c09_example_invoices.md` §8.
- **Summary for the founders:** `software-initial-pitch.md`.
- **Date:** 2026-10-03. **Budget used:** 48 web searches, about 60 fetches.
- **Status:** input to S5. **It decides nothing.** Design suggestions are marked **[our call]**.
- **Labels:**
  - *verified* = read at the primary source (including a product's own page, for "the product says X").
  - *assumed* = a search snippet, a vendor claim about results, a blog, a review, or memory. Every review quote is an *assumed* anecdote.
  - **[our calc]** = our arithmetic. **[our call]** = our judgement.
  - "Extraction" = the page was read through a fetch tool that returns a model-made summary, so short quotes are "as extracted".
- **Source IDs:** new sources are N-AK01 to N-AK58 (§9). Earlier IDs (N-Y, N-Z, N-T, N-AC, N-PA, N-AB) keep their meaning.
- **Re-checked at the source by the coordinator (2026-10-03), all matching:**
  - XPO: "The invoice must be paid before an overcharge claim can be filed"; claims decided "within 60 days of submission" (N-AK12);
  - Ardent Partners: an average invoice exception rate of 18.4% (N-AK45);
  - FedEx Freight's nine dispute types and required fields (N-AK25).
- **No identity was sent** in any request. Nobody was contacted.

---

## 1. Summary table

| Q | Headline answer | Best evidence | Labels |
|---|---|---|---|
| **AK1 How bills are checked today** | In job postings the duty sits with **logistics staff (22 of 47) and freight-bill specialists (11) more than AP (6)**. AP clerks mostly code and key the bills. There are three routes:<br>**Route 1 (by eye):** compare the bill total with the quote or rate confirmation, scan the extra lines, approve within an informal "payment tolerance", and email the carrier on a mismatch. Variances are often simply expensed.<br>**Route 2 (SMB booking tools):** Freightview, MyCarrier and FreightPOP automate quote-vs-invoice. They offer queues, thresholds and accept/dispute buttons, but they compare against the **quote, not the contract**, and only for shipments booked in the tool.<br>**Route 3 (audit firms and FAPs):** they re-rate against the contract and send exceptions to analysts, or to a shipper portal that shows the bill image and a choice of standard reasons.<br>No association or community-college checklist was found.<br>**A highlighted document helps routes 1 and 2.** But most money sits in lines that need documents **not on the bill** (59 of 101 real ABF bills), so the screen must show missing evidence, not just highlights | N-Y03; N-AK01-03; N-AK50; N-PA01 | postings, product pages and Cass tutorial *verified*; practice claims *assumed*; reading **[our call]** |
| **AK2 The full rule set** | About **33 checks in 7 families**: valid and single bill; rated right; weight and class changes; extras allowed and proven; service as paid; payment, coding and accruals; deadlines. **22 can run unattended once the documents are loaded, 9 partly, 2 need a person** [our calc]. The money is mostly in the "partly" group.<br>Ready-made reason lists exist:<br>- **Cass's 13 standard adjustment reasons**, the same for all clients;<br>- **FedEx Freight's 9 dispute types**, including "Incorrect debtor" (wrong payer) and "Guaranteed shipment";<br>- federal rules require a "detailed description of the reasons" and notice within 7 days | N-AK04, N-AK06, N-AK25, N-AK50, N-AK49, N-AK13 | rules *verified*; values mostly not found or *assumed* |
| **AK3 What existing products do** | **Every product has converged on one screen pattern:** a queue of exceptions; the bill image with billed vs expected amounts; a standard reason; one-click approve / adjust / reject to carrier / dispute; and an audit trail.<br>Newer entrants (Loop, Trax) add agents that email carriers and chase documents, with **rule-set limits on what they may do alone**. AP tools (Stampli, Ramp) add comments on the invoice, staged duplicate checks, reminders, and Slack or mobile approval.<br>**Parcel:** UPS and FedEx both reserve the right to refuse refund requests made by, or based on information from, anyone other than the payer. The wording was already quoted in 2010; when it started was not found | N-AK01-03, N-AK26, N-AK35, N-AK36, N-AK38-41, N-AK50; N-AK28, N-AK29 | product pages and tariff text *verified*; performance claims *assumed* |
| **AK4 Disputes and claims in practice** | Each carrier has its own channel, in two kinds:<br>- **before payment, a billing dispute:** Estes takes up to 100 discrepancies per spreadsheet; FedEx Freight has a 9-type form; Saia has one email for rates and one for accessorials;<br>- **after payment, a formal overcharge claim** on near-identical "standard" forms (ABF, R+L): PRO list, tariff or contract authority, "charges should be" (weight, rate, extension), and the paid bill or a bond of indemnity.<br>**Short pay is mostly barred:** most tariffs ban offsets, and XPO requires payment before a claim.<br>Stated response times run from "24 to 48 hours" (Estes) to 60 days (XPO) and up to 120 days (TForce).<br>**Many bills on one claim** is accepted on forms and batch tools.<br>**No LTL carrier statement on automated claims was found.** The levers are visible: ODFL's $50 fee on no-fault settled claims, TForce's payer-only filing, and the parcel carriers' third-party clauses | N-AK12, N-AK16, N-AK17, N-AK19, N-AK21, N-AK24, N-AK25; N-T05 | forms and pages *verified*; Estes speed *assumed* (carrier claim); some channels by snippet *assumed* |
| **AK5 Alerts and ease of use** | **Users value:** emailed reminders with a **direct link** to the item; due and overdue reminders; comments and @tags **on the invoice**; approve-and-pass-along; weekly or Friday digests; Slack and mobile approval.<br>**They complain about:** carriers missing from the audit tab, manual filters, unclear exceptions, OCR misses, slow search and support.<br>**No neutral false-positive data for freight was found.** General AP sees exceptions on **18.4%** of invoices (Ardent, 2025 survey). The public ABF set has **58%** of bills carrying a line that needs a document, about 3× that [our calc]. Without grouping, the alerts would overwhelm users | N-AK43-45, N-AK03, N-AK33, N-AK41; N-Z32, N-Z40 | product features and Ardent *verified*; reviews *assumed* |
| **AK6 The ease-of-use bar** | **FAPs ask for:** invoices redirected to them (a custom email address, EDI or FTP), the contracts, and shipment data, then **4-12 weeks** (vendor claims).<br>**The lightest-touch options found:**<br>- a forwarding inbox, PDF agreements and a QuickBooks or ERP export;<br>- parcel auditors need only carrier logins and send weekly summaries;<br>- contingency LTL firms offer a "first audit free" and file through the carriers' portals.<br>**Split of work:** vendor analysts or agents handle clear-cut errors. "**Was this service actually performed?**" questions go to humans; Intelligent Audit routes exactly this case to human review.<br>**No evidence compares customer-approval with auto-file outcomes** | N-AK46-48, N-AK33, N-AK35, N-AK36, N-AK09 | product statements *verified*; timings *assumed* |

---

## 2. AK1 · How bills are checked today, step by step

### 2.1 Who does it, and what they compare (from earlier checks, not redone)

- **Who:** of 47 postings at US manufacturers and distributors, the freight-bill duty sits under:
  - a logistics title in **22**;
  - a freight-bill title in **11**;
  - AP in **6** (N-Y03, *verified*).
- **What they compare, in the postings' words** (*verified*, N-Y03):
  - "Audit freight invoices for accuracy against contracted rates, shipment records, purchase orders, bills of lading, and TMS data" (Do it Best);
  - "Review freight invoices for accuracy and compliance with contracted rates and payment tolerances" and "Investigate charges that fall outside established tolerances and obtain approval when required" (BodyBio);
  - "Print out freight bills and code with purchase order numbers if possible" (Fujitec);
  - "execute monthly freight accrual audits" (Bradshaw Home);
  - "Process, audit and approve freight invoices/logs from 3PLs" (Twin City Fan).

### 2.2 The three routes, step by step

| Step | Route 1: by eye against a quote or rate confirmation | Route 2: SMB LTL booking tool's audit screen | Route 3: full re-rating by an audit firm or FAP |
|---|---|---|---|
| **1. Bill arrives** | PDF by email or carrier portal, or paper. Multi-bill PDFs split by hand (N-Z18, *assumed*); ERPs assume "electronically or on paper" (N-Z20, *verified*) | EDI, carrier portal or manual upload, matched to the booked shipment (FreightPOP, N-AK03, *verified*). Freightview creates a card "48 hours after the scheduled pick-up date" (N-AK01, *verified*) | Carriers redirected to send bills to the provider "by mailing paper invoices, sending in PDF files via FTP …, e-mailing them in to a custom e-mail address" or EDI (CT Logistics, N-AK48, *verified*) |
| **2. Find the expected price** | Find the PO, BOL, quote email or rate confirmation by hand (postings, *verified*) | The quote stored at booking. MyCarrier "compares every carrier invoice to the original quote" (N-AK02, *verified*) | The contract version for the ship date: "Shipment date must fall within contract period" (Intelligent Audit, N-AK09, *verified* page text). nVision states "200+ audit checkpoints" (N-AK10; the count is the vendor's) |
| **3. Compare** | Total vs quote; scan for extra lines (reweigh notes, accessorials; bill layout: N-PA01, *verified*) | Line by line vs quote. Thresholds in % or $, "at the total invoice level or per charge code", plus **"negative variance protection"** against bills far *under* quote (FreightPOP, *verified*). Freightview's "Invoice Matching" add-on auto-accepts within a % or $ limit (N-AK01, *verified*) | Each charge re-rated. Exception card: "Accessorial amount mismatch \| Invoiced: $300 \| Contracted: $250 \| Difference: $50.00" (nVision page, N-AK10, *verified* as shown) |
| **4. Decide** | Approve inside "payment tolerances". Outside them, investigate and "obtain approval when required" (BodyBio, *verified*) | **Freightview:** "Yes" to accept as quoted; "No" to dispute or enter another amount, with a note "explaining acceptance of different amounts (e.g., 'reclass or re-consignment fees')". **FreightPOP:** approve, send back to carrier, or "override with password-protected authorization" (*verified*) | **Cass shipper portal (2009 tutorial):** click the PRO on the **Freight Bill Exception report** and the **freight bill image** opens. A **Reject Resolution** dialog then offers:<br>- **Reprocess** (complete a "reprocess stamp");<br>- **Adjust Pay Amount** (choose a standard reason);<br>- **Reject to Carrier** (up to 99 client-specific reasons);<br>- **Discard**.<br>A confirmation screen follows (N-AK50, *verified*) |
| **5. Dispute and record** | Email or phone the carrier. Home-built duplicate dashboards (Epicor, N-Z17, *assumed*). Variances "manually adjusted to the billed cost" and expensed (Acumatica, N-Z16, *assumed*) | **Freightview:** dispute from the tool "with carrier contact emails" and uploaded documents; Disputed and Archived queues; exports with notes and auto-accept flags (*verified*). **MyCarrier:** "submit and manage the dispute directly in the platform" (*verified*) | **Carriers see standard reasons** in their portal: "Out of Tolerance", "Missing Documentation", "Suspected Duplicate" (CassPort carrier guide, N-Z50, *verified*). **Look-back firms** "draft the dispute citing MRA clause + NMFC item + 49 USC 13710 … file it through the carrier's claims portal" (Eller, N-AK46, *verified* as the firm's description) |
| **6. Post** | Key the bill as a vendor bill; accruals trued up monthly (N-Z22 *assumed*; N-Y03 *verified*) | Export to the ERP with GL codes "assigned via configurable rules" (FreightPOP). MyCarrier's one-way sync to QuickBooks Online: "audited invoices become AP Bills automatically" (*verified*) | GL assignment, approval "by the proper authority", ERP posting, "full audit trail" (nVision's "eight requirements", N-AK11, *verified* page text) |
| **Limits** | No tool; supporting documents often not held (N-PA01 §3.1) | Compares with the **quote**, not the agreement, and only for shipments booked in the tool. The audit tab "only shows some freight companies" (N-Z40, *assumed*). MyCarrier Essentials covers "Up to 50" / "Up to 100" shipments a month; above that, an "EDI-enabled Invoice Hub on a Professional Plus plan" (N-AK02, *verified*) | Implementations of weeks to months, aimed at large shippers (check Z §7, *assumed*) |

### 2.3 Tolerances, approvals, short pay, dispute records, and what is skipped

| Practice | What was found | Label, source |
|---|---|---|
| **Tolerances ("approve if within $X")** | Shippers' postings name "payment tolerances" (BodyBio) | *verified*, N-Y03 |
| | SMB tools set thresholds in % or $ (FreightPOP, Freightview add-on) | *verified*, N-AK01, N-AK03 |
| | An audit vendor: "most enterprises set tolerances between 0.5% and 2%" on base freight; accessorials "warrant tighter tolerances"; "dynamic tolerances that adjust based on shipment value" | *assumed* (vendor's description of practice), N-AK09 |
| | Dynamics AX/365 "Audit master": a minimum and maximum tolerance; within it, "the reconciliation is approved and processed for automatic payment"; reason codes "for the overage amount and the underage amount"; separate masters "for different freight bill types or carrier types" | *verified*, N-AK49, N-Z20 |
| | Federal contractors keep bills under $100 instead of sending them for audit | *verified*, 41 CFR 102-118.140(i), N-AK04 |
| | A broker-carrier template leaves "claims of Five Dollars ($5.00) or less" uncorrected | *verified*, N-AC36 (earlier check) |
| **Approval chain** | Logistics approves (4 postings), accounting (1), branch operations (1), "approval when required" above tolerance (1) | *verified*, N-Y03 |
| | Tools add a password override (FreightPOP) and a "reprocess stamp" (Cass) | *verified*, N-AK03, N-AK50 |
| **Short pay** | FAPs short-pay with standard reasons: Cass's list includes "Amount Cut Per Client", "Discount Taken" and "Declined Balance Due" | *verified*, N-AK50 |
| | Carrier tariffs bar offsets (ODFL, Estes, XPO, Saia, TForce). Saia: "no short payment or credit-taking" | *verified*, check T §6 |
| | XPO: "The invoice must be paid before an overcharge claim can be filed" | *verified*, N-AK12 (re-checked by the coordinator) |
| **How disputes are recorded** | Notes and Disputed/Archived queues in SMB tools (*verified*); ERP dashboards and spreadsheets (*assumed*). No first-hand account of a dispute log at a mid-sized shipper was found | N-AK01, N-Z16, N-Z17 |
| **What is skipped under time pressure** | Vendor claims only: "spot-checking a handful of invoices by hand"; checking "gets skipped under time pressure and just gets paid"; AP "rubber-stamps" | *assumed*, N-Z84, N-Z74, N-Z73 |
| | Counter-signal for truckload: per ATRI, **shippers pay fewer than half of detention invoices**, so detention is already contested | *verified*, N-AB41 (earlier check) |

### 2.4 Training material and checklists

- **NITL, TIA, NASSTRAC, AST&L:** no public freight-bill audit checklist or course was found (search 4).
- **Community colleges:** no course material on freight-bill auditing was found (search 6).
- **Government rules that work as a checklist** (41 CFR 102-118, *verified*, N-AK04, N-AK06):
  - every bill must contain "enough information for the auditor to determine which contract or rate tender is used" (102-118.140(b));
  - "a unique agency numbering system … to prevent duplicate payments" (g);
  - notices to the carrier "that include a detailed description of the reasons for any full or partial rejection" (h);
  - notice of any adjustment "within seven calendar days of the agency receipt of the bill" (102-118.160).
- **GSA's post-payment audit** examines bills "for validity, propriety, and conformity of the charges using tariffs, quotations, agreements, or tenders" (*assumed*, snippet, N-AK08).
- **Vendor checklists:** ICC Logistics' groups are:
  - invoice and document basics;
  - class and weight, including "flag reweighs";
  - accessorials, surcharges and duplicates ("Identify duplicate BOLs and invoices across carriers");
  - contract and rate compliance ("Audit discounts, minimums, and accessorial waivers") (N-AK52, *verified* page content).
- **IOFM:** "Freight Audit and Payment Best Practices — The Basics" returned 403. Its snippet advises logging electronic invoice file IDs and having "a procedure to deal with duplicate invoices" (*assumed*, N-AK57).

### 2.5 Is "the document on screen with discrepancies highlighted" an improvement? **[our call]**

- **Route 1 (by eye): a clear improvement.** It removes the hunt. The expected price, the bill and the BOL appear together, and the clerk only decides.
- **Route 2 (SMB booking tools): a moderate improvement.** These tools already flag "quote ≠ invoice". They don't show *why* a line differs, which document proves it, or whether the quote itself matched the contract. A highlight that names its cause ("reweighed: BOL said 1,837 lb, certificate not attached") adds what is missing. It also covers carriers not booked through the tool.
- **Route 3 (FAP portals): a small step.** Cass already put the bill image beside a resolution dialog with standard reasons in 2009 (N-AK50). The improvement is offering route-3 quality to shippers who can't buy route 3.
- **The main caveat comes from the practice audit:** **$0** was provable from the 101 ABF bills alone, and **59 bills (61% of dollars)** carried a line needing a document not on the bill (N-PA01, *verified*, [our calc]). Highlighting the invoice is the cheap part. The product must also show which supporting document is missing for each flagged line, fetch it or ask for it, and turn the answer into a filed dispute.

---

## 3. AK2 · The full rule set professional auditors run

### 3.1 Rulebooks and ready-made reason lists

| Source | What it lists | Label |
|---|---|---|
| **Cass FBA standard adjustment reasons** ("Reasons are the same for all clients") | Weight Incorrect · Rate Error · Error in Extension · Discount Incorrect · Reversed Balance Due · Incorrect Mileage · Amount Cut Per Client · Declined Balance Due · Other Audit Adjustment · Service Failure · Discount Taken · Invalid Accessorial Charge · Service Failure - POD. Purpose stated: "reduce the amount of data entry required while providing useful information for carriers" | *verified*, N-AK50 (2009) |
| **FedEx Freight dispute form types** | Incorrect rate · Incorrect debtor ("invoices sent to the wrong party") · Reweigh review · Guaranteed shipment · Inspection review · Account/reference edits · Documentation requests · Other invoicing issues · Dispute fee or surcharge | *verified*, N-AK25 (re-checked) |
| **FreightPOP audit dimensions** | Rate and contracted price · accessorials · detention and surcharges · duplicates · weight, dimension and quantity · discount · tax · quote-to-invoice | *verified* (product page), N-AK03 |
| **nVision** | "200+ audit checkpoints" across "rates, accessorials, and billing" | *verified* that the page says so; count unverified, N-AK10 |
| **41 CFR 102-118** | Contract or tender identifiable; duplicate-proof numbering; detailed rejection reasons; 7-day adjustment notice; appeals process | *verified*, N-AK04, N-AK06 |

### 3.2 The check table

"Auto?" means whether a machine can decide once the listed data is loaded:
- **Yes:** the machine decides.
- **Partly:** it can flag, but needs a document or a person to close.
- **No:** a person decides.

| # | Check | Data needed | Auto? | Value or evidence | Label, source |
|---|---|---|---|---|---|
| **A. Is it a valid, single, correctly addressed bill?** | | | | | |
| A1 | Math and extensions | Invoice | Yes | 0 errors in 101 ABF bills; Cass reason "Error in Extension" | *verified*, N-PA01, N-AK50 |
| A2 | Duplicate bill (same PRO; same BOL and amount; same PDF re-sent) | PRO, BOL, carrier, amount, dates; file fingerprint | Yes to flag; a person confirms | Minimum-charge accounts produce false "same amount, same day" pairs, so key on PRO + BOL. Stampli checks file name, size and content at entry, then invoice number, vendor, date and amount | *verified*, N-PA01, N-AK38 |
| A3 | Paid twice through a 3PL or broker | AP payment records; 3PL invoices; carrier statement | Partly | IN Holdings: ABF claimed $45,652.49 on bills the debtor says a 3PL "already paid" | bills *verified*; "already paid" *assumed*, N-AC (E-2) |
| A4 | Corrected or balance-due bill matched to the original; carrier's 180-day rebill window | EDI B308 code or "CORRECTED"; original bill date | Yes | 49 U.S.C. 13710(a)(3) | *verified*, check T §4 |
| A5 | **Wrong payer, debtor or freight terms** (prepaid, collect, third party; inbound freight the supplier should pay; wrong legal entity) | BOL freight-terms box and bill-to; PO or vendor freight terms; entity list | Partly: flag, then a person confirms | FedEx Freight has a standard "Incorrect debtor" dispute type. **Value not found** | *verified*, N-AK25 |
| A6 | Bill with no matching shipment | TMS or ERP shipment list | Yes | Cass practice per a snippet | *assumed*, N-AK51 |
| A7 | Bill carries the reference needed to pick the contract or quote | Quote number, agreement ID, account | Yes | 102-118.140(b). Volume-quote numbers "must be on the original bill of lading, or the rate will not apply" (3PL guides) | rule *verified*; quote practice *assumed*, N-AK54 |
| **B. Is it rated right?** | | | | | |
| B1 | Right agreement version for the ship date | Every version with effective dates | Yes, once loaded | SEFL account with 3 versions | *verified*, N-PA02 |
| B2 | LTL base rate × discount | Base tariff (licensed, e.g. CzarLite) or carrier quote; discount; class; weight; lane | Partly (needs licensed base rates) | Without the agreement, only consistency can be checked | *verified*, N-PA01 |
| B3 | Minimum charge (AMC) | Agreement minimum | Yes | 38% of ABF bills sat on the $180 floor | *verified*, N-PA01 |
| B4 | FAK or class applied | FAK table; BOL class and NMFC item | Yes | SEFL: FAK 70 for 77.5-175 | *verified*, N-PA02 |
| B5 | **Quote, dynamic or spot price honoured** | Quote document or ID; BOL | Yes, if the quote is captured | ABF Dynamic LTL: "rates without negotiating a published price"; "Special services are included in the all-in rate if provided at time of quote". A real ABF bill shows "Dynamic discount −$181.83" | *verified*, N-AK14, N-PA01 |
| B6 | Truckload linehaul vs rate confirmation or contract lane | Rate confirmation or contract | Yes | C.H. Robinson confirmations show the fields | *verified*, N-AC08/09 |
| B7 | **Truckload mileage** (PC*MILER practical vs shortest; version) | Contract mileage basis; stop sequence | Partly (needs a licensed mileage engine) | Cass reason "Incorrect Mileage". **Value not found**; the mileage basis in a public tariff was not read | reason *verified*; routing types *assumed*, N-AK50 |
| B8 | Fuel level | Fuel table in force, EIA index, effective-day rule, pickup date | Yes | ABF billed 1.3-1.5 points under its public table every week | *verified*, N-PA01 |
| B9 | Fuel base (linehaul only) | Invoice | Yes | 99 of 99 correct | *verified*, N-PA01 |
| **C. Were weight and description changed fairly?** | | | | | |
| C1 | Reweigh or reclass | BOL weight, class, dims; W&R certificate; spec sheet | Partly: flag and fetch; a person files | 26% of ABF bills, 27% of dollars; FedEx Freight types "Reweigh review" and "Inspection review" | *verified*, N-PA01, N-AK25 |
| C2 | Correction-fee trigger met | Tariff thresholds | Yes | Fees $15-55; triggers from +20 lb (ODFL) to $10 of charges (ABF, R+L) | *verified*, check T §3.1 |
| **D. Are the extras allowed and proven?** | | | | | |
| D1 | Accessorial priced per schedule or waiver | Accessorial schedule and waivers | Yes | Cass reason "Invalid Accessorial Charge"; ABF accessorials = 13.0% of billed | *verified*, N-AK50, N-PA01 |
| D2 | **Accessorial ordered or performed** (liftgate, residential, inside, limited access) | BOL tick boxes, booking options, delivery receipt notes, approvals | Partly: often a question for the shipper | Intelligent Audit routes "an accessorial charge not in your contract, but the charge may reflect a service actually performed" to human review | *verified* (page text), N-AK09 |
| D3 | Detention | Free time; arrival, appointment and departure times | Partly (needs timestamps) | Werner: 2 hours free, then $110/hour from the later of arrival or appointment. ABF billed detention with no times printed | *verified*, N-AC24, N-PA01 |
| D4 | Stop-offs | Stops on the rate confirmation or BOL | Yes | Werner $150 / $175 / $250 / $400 | *verified*, N-AC24 |
| D5 | Truck ordered not used (TONU) | Cancellation time; rate confirmation terms | No | EDI code VOR; price not found | *verified* (code), N-AC12 |
| D6 | Layover | Appointment and arrival records | No | Werner $350 | *verified*, N-AC24 |
| D7 | Lumper | Lumper receipt | Partly (receipt exists; amount matches) | C.H. Robinson requires "a lumper receipt"; Werner bills "face value of lumper receipt". ABF lumper on 33 bills, $1,882.26 | *verified*, N-AC09, N-AC24, N-PA01 |
| **E. Was the service delivered as paid for?** | | | | | |
| E1 | **LTL guaranteed-service refund** | Guaranteed service ordered; POD date and time; transit standard; exclusions | Yes to detect; must be filed inside the window | XPO: "Customer may file for a refund of the fee within 15 days of delivery", via the portal's Refund Request tool. That refunds the **fee only**, not the freight. **Value not found** | *verified*, N-AK12, N-AK13 |
| E2 | Service-failure credit (truckload or contract) | Contract service terms; POD; appointment | Partly | Cass reasons "Service Failure" and "Service Failure - POD". Broker-side rate confirmation: "Rate may be reduced if load picks up or delivers after originally scheduled time" | *verified*, N-AK50, N-AC09 |
| **F. Payment, coding and accruals** | | | | | |
| F1 | Late-payment fees | Due dates, pay dates, late-fee rule | Yes | XPO bills carry late fees for 30-180 days past due | *verified*, N-AC02 |
| F2 | GL coding and allocation | PO or SO, GL rules, entity | Yes (suggest) | nVision "GL Code Assignment"; FreightPOP GL rules; Fastenal's posting codes "General Ledger" | *verified*, N-AK11, N-AK03, N-Y03 |
| F3 | Accrual vs actual | TMS or ERP estimate | Yes | D365 over/under reason codes; "monthly freight accrual audits" | *verified*, N-AK49, N-Y03 |
| F4 | Freight rebilled to customers (adjacent) | Sales-order freight line | Yes | "allocating appropriate costs to customer billings" | *verified*, N-Y03 |
| **G. Deadlines** | | | | | |
| G1 | Shipper's dispute and claim windows | Carrier tariff, contract, statute | Yes | 180 days with different start dates; corrected BOLs within 30 days; XPO guaranteed refunds within 15 days | *verified*, check T §3.2, N-AK13 |
| G2 | Carrier's response deadlines | Claim dates | Yes | 49 CFR 378: acknowledge in 30 days, decide in 60 | *verified*, N-T05 |

### 3.3 Reading **[our call]**

- **33 checks: 22 unattended, 9 partly, 2 need a person [our calc].** The practice audit puts the money in the "partly" group: reweighs, accessorials needing proof, detention, lumper, and payer and 3PL duplicates.
- **Cass's reasons and FedEx Freight's types give a ready-made taxonomy carriers already recognise.** Using the carriers' own names raises the chance that a dispute is routed correctly.
- **Two less obvious checks are probably worth having, because they cost little:**
  - **A5, wrong payer:** FedEx Freight made it a standard dispute type.
  - **B5, dynamic and volume quotes:** a quote not referenced on the BOL may be billed at contract or tariff.

---

## 4. AK3 · What existing products do and how their screens work

### 4.1 Product table

| Group | Product | What the review screen shows and allows | Alerts | Limits | Source, label |
|---|---|---|---|---|---|
| (i) SMB booking tool | **Freightview** | Outstanding / Accepted / Disputed / Archived queues. Yes/No accept; another amount plus a note; dispute "with carrier contact emails"; document upload; custom filters. "Invoice Matching" add-on auto-accepts within % or $. Exports with notes and auto-accept flags; spot-quote edits tracked | Not stated | Reviewers: "only shows some freight companies"; "a lot of steps to create the custom filter" | N-AK01 *verified* (updated 2026-07-17); N-Z40 *assumed* |
| (i) | **MyCarrier Invoice Hub Essentials** | Compares every invoice with the original quote; "no rules to write"; disputes in the platform; one-way sync to QuickBooks Online | Not stated | Up to 50 or 100 shipments a month; above that, the EDI version on Professional Plus | N-AK02 *verified* (2026-08-07) |
| (i) | **FreightPOP** | Line by line vs quote. Thresholds in % or flat, at invoice or charge-code level; negative-variance protection. Approve, send back to carrier, or password override; change logs | **"Friday email"** of approved and outstanding invoices | Compares with the quote | N-AK03 *verified* |
| (ii) Broker back office | **TriumphPay Audit (formerly HubTran)** | The TMS sends a load when "dispatched and delivered". Documents can be flagged "Use as POD". Rules "throw an exception that must be acknowledged and cleared". The broker can put a bill on a "variance list". The approved amount syncs back once | — | TL and LTL only; "the system only pushes the bill once — at the time of approval" | N-AK26 *verified* |
| (ii) | **Triumph POD Detection** | "handwriting identification, signature validation, and data accuracy" | — | Claims "no-touch invoice processing for 75% or more" | N-AK27 (2024-04-11); claim *assumed* |
| (ii) | Denim; Rose Rocket (TMS.ai); Vooma; Raft | Denim "from 3 minutes per job to less than a minute". TMS.ai's "DataBot" reads rate confirmations. Vooma has agents, including "Collect". Raft handles "more than 130,000 documents per month" | — | Screen details not public | N-AK56 *assumed*; N-AK55 snippets |
| (iii) Audit and payment | **Cass (shipper portal)** | Freight Bill Exception report → bill image → Reprocess / Adjust Pay Amount with standard reasons / Reject to Carrier (up to 99 client reasons) / Discard, then a confirmation. A "**mass modify** resolution for resolving multiple invoices at once". Carriers see billed, rated and pay amounts and the reject reasons | Not read | 2009 tutorial; current screens not read | N-AK50 *verified*; N-Z50 *verified* |
| (iii) | **nVision** | Exception card with type, invoiced, contracted and difference; routed "to experienced freight audit professionals". Its standard for a completed record: audit, validation, GL, documents, approval, payment, ERP posting, audit trail | "Billing discrepancies flagged in real time" | — | N-AK10, N-AK11 *verified* (page says) |
| (iii) | **Trax** | "Grouping similar exceptions for consistent handling"; "Configurable rules for determining when agents can act autonomously versus when human approval is required" | — | "planned over the next several quarters" | N-AK36 *verified* (2025-05-12) |
| (iii) | **Loop** | Exception Agent "detects discrepancies, initiates disputes, tracks resolution" by email; "interprets carrier responses, retrieves supporting documents, and drafts accurate replies". Complex cases: "flags for human review rather than sending automatically". "every dispute is logged, tracked, and auditable" | — | "95% touchless approval within 30 days" at one Fortune 100 food company | N-AK35; features *verified* (page says); claim *assumed* |
| (iii) | **Intelligent Audit** | Three paths:<br>- automatic adjustments ("clear-cut errors");<br>- human review ("exceptions requiring judgment");<br>- escalation when "the same exception recurs across multiple shipments with a single carrier" | A reviewer wants alerts "as and when the invoice is pending approval" | — | N-AK09 *verified*; N-Z32 *assumed* |
| (iii) | CTSI-Global; U.S. Bank; Freehand; Pando | Carrier-side "Mailback" queue (CTSI); carrier agreement (U.S. Bank); email intake (Pando) | — | **Shipper screens not read** | N-Z55, N-Z47, N-Z76 (earlier) |
| (iv) AP automation | **Stampli** | Approvers, coding, comments and history stay on the invoice; vendors can be invited. Duplicates are checked in **3 stages**, with "A warning message … at the top of the 'Invoice Details' screen" and a side-by-side comparison. Exception types (PO match, missing data, no owner, duplicate suspicion, coding, vendor disputes) each get "a named resolver", "visible aging" and an SLA by type | Email reminders with direct links; due and overdue reminders (reviews) | OCR "sometimes struggles with unusually-formatted vendor invoices" (review) | N-AK38, N-AK39 *verified*; N-AK43/44 *assumed* |
| (iv) | **Ramp Bill Pay** | An AP inbox builds draft bills from Gmail with attachments; auto-coding; fraud and duplicate flags. "Approval intelligence … provides recommendations only. It does not approve bills" | **Slack:** "approve, edit, or reject the request directly in Slack"; mobile approvals (snippet) | Inbox in beta; most features need Ramp Plus | N-AK40, N-AK41 *verified* |
| (iv) | BILL | Approval policies by amount and approver; checks for duplicate invoice numbers | Slack described by a competitor as "more of a notification bridge" | Help article unreachable | N-AK42 *assumed* |
| (iv) | Tipalti, AvidXchange, Medius | **Not read** (budget). AvidXchange payee complaints are in check Z | — | — | N-Z65 |
| (v) Parcel audit | **71lbs** | Files claims; "**weekly email summary**"; dashboard "typically available by week 2"; customers check refunds in their own carrier accounts | Weekly email | Contingency | N-AK33; features *verified*, timing *assumed* |
| (v) | LateShipment.com; Refund Retriever; Shipware | LateShipment works from the customer's UPS or FedEx credentials and claims "160-point checks". Refund Retriever quotes UPS's payer clause. Shipware not read | — | LateShipment fee 35% of refunds (check AA) | N-AK34 *assumed*; N-AK32 *verified* |

### 4.2 Did UPS and FedEx restrict third-party auditors?

| Carrier | Text (exact) | Where read, and date | Label |
|---|---|---|---|
| **UPS** | "UPS reserves the right to refuse any request for a credit or refund when such request is either (a) made by, or (b) based on information obtained by, a party other than the payer of the shipping charges." The same document requires service failures to be notified "within fifteen (15) calendar days of the date of scheduled delivery", by phone or the online Billing Center | UPS *Terms and Conditions of International Service* (Brazil edition), date not shown in the extracted text. **The US terms PDF was bot-blocked.** Refund Retriever quotes the same wording for UPS's US guarantee, and a 2010 blog quotes it from the UPS Service Guide (p. 30) | *verified* (international terms); US version *assumed* (N-AK32, N-AK30) |
| **FedEx** | "At the sole discretion of FedEx, the money-back guarantee may not be honored when the request is made by, or the information utilized to determine the status of the package is determined by, a third party other than the payer of the charges." Also: credits "applied to the payer's account only, and refunds will be made payable to the payer only" | FedEx Service Guide, Terms and Conditions, International (U.S. edition), **effective 2021-01-04**. The 2010 blog quotes the same wording from the Service Guide (p. 138). The current money-back guarantee page (2026) did not show the clause | *verified* (2021 terms); 2010 *assumed* |
| **When it started** | Not found. **In force by March 2010 at the latest** | — | *assumed* |
| **How parcel auditors work anyway** | They log in with the customer's own carrier credentials, and refunds go to the payer's account. 71lbs: verify refunds "by logging into" your own carrier account | — | *assumed* (credentials, snippet); *verified* (71lbs FAQ) |
| **The pool shrank by carrier action** | FedEx suspended its guarantee on 2025-12-01 and reinstated it only for listed express services (2026-01-13 domestic, 2026-02-11 international) | — | *verified*, N-AK31 |

**What this implies for LTL [our call]:**
- **LTL carriers already hold similar levers:**
  - TForce: "Only the payer of the original freight charges can file an overcharge claim" (*verified*, N-AK21).
  - ODFL shows certificates only to "the bill to party on the pro" and charges **$50** on settled claims "through no fault of Carrier" (*verified*, check T).
- **The regulation allows agents:** 49 CFR 378.2(f) defines the claimant as the shipper "or its authorized agent" (*verified*, N-T05).
- **The parcel clauses target outsiders claiming at scale from their own tracking data.** The safe design is to file **in the payer's name**, from the payer's account or with a letter of authority, and only with checked evidence. Never spray claims or scrape portals in bulk.
- **Carriers can remove a refund pool** (the guarantee suspensions) rather than fight claims. Don't build the business case on one refund type.

---

## 5. AK4 · Disputes and claims in practice

### 5.1 Three routes, and which to use

1. **Before payment, a billing dispute.** Estes: "In instances where a bill needs to be reviewed and adjusted prior to payment, the Rating and Billing Discrepancies tool should be used" (snippet matching the FAQ; *verified* via N-AK24). Paid bills go to the overcharge claim form.
2. **After payment, a formal overcharge claim** under 49 CFR 378 (rules in check T §4), on the carrier's form.
3. **Short pay.** Barred by most tariffs (no offset), and XPO requires payment before a claim (*verified*). FAPs do adjust pay amounts with standard reasons (Cass), which carriers then see as rejects or "Out of Tolerance".

**[our call]:** an audit-only v1 should use route 1 for unpaid bills and route 2 for paid ones, and **never recommend a short pay**.

### 5.2 Carrier channels

| Carrier | Billing dispute (before payment) | Overcharge claim (after payment) | Window stated | Response time stated | Fields and evidence named | Source, label |
|---|---|---|---|---|---|---|
| **ODFL** | Online "File a claim online by PRO number" (login); customer service 1-800-235-5569; ODInvoicing@odfl.com (snippet) | Same portal; status "by PRO number, claim number or claimant number" | Tariff: 180 days after "Carrier's receipt of the shipment"; closed 30 days after the initial ruling | Not on the page. A snippet's "30 days to acknowledge … 120 days to process" looks like cargo claims | "conclusive documentary proof"; $50 fee on no-fault settled claims | N-AK15 *verified*; N-AK58 *assumed*; check T |
| **XPO** | Not described on the page. Tariff: shipper corrections within 30 days of acceptance | Customer portal; overcharge.LTL@xpo.com | "within 180 days of the receipt of the original invoice"; **guaranteed refunds within 15 days of delivery** | "within 60 days of submission" | "reason for the request, claimant information, invoice information and supporting documentation"; **invoice must be paid first** | N-AK12, N-AK13 *verified* (re-checked) |
| **Estes** | **Rating and Billing Discrepancies tool:** "batches of up to 20" without login; spreadsheets of "up to 100" in My Estes, with "supporting documents, images" | Overcharge claim form for paid bills | Tariff: none stated | "usually within 24 to 48 hours", by email | Documents and images; W&R certificates through My Estes | N-AK24 (FAQ extraction) *verified*; speed *assumed* (carrier claim) |
| **Saia** | "Rate and billing inquiries … fbreview@saia.com"; "Accessorial disputes … csdispute@saia.com"; W&R disputes through the website | Overcharge claim form | Tariff: 180 days from the original bill | Not stated | — | N-AK16 *verified* (PDF image) |
| **ABF** | "Freight Bill Review": most inquiries "answered by email within one hour" (snippet) | **Overcharge Claim Form**, P.O. Box 10048, Fort Smith AR | Tariff: 180 days from the initial shipment date | One hour (snippet) | Multiple "ABF PRO #" lines with date and amount; "Nature of overcharge (weight, rate, classification, discount, etc.)"; "Authority for correction (reference tariff, item number, effective date)"; "CHARGES SHOULD BE: Weight / Rate / Extension"; original paid bill **or** a copy plus a bond of indemnity; for weight or description: original BOL, vendor invoice, catalog pages, packing slip or receiving reports; "CLAIMANT SHOULD ASSIGN A NUMBER TO EACH CLAIM" | N-AK17 *verified*; one-hour *assumed* |
| **FedEx Freight** | Billing Online dispute form with **9 types**. Required: email, phone, account number, subject, type, sub-type (PRO optional). Case number by automated email; resolution by email | Tariff: disputes "with detailed supporting information" to fxfrevsoltn@fedexfreight.com | Tariff: 180 days + 7 | Not stated | — | N-AK25 *verified* (re-checked); check T |
| **R+L** | BillPay contact form: issue type (invoice or other), invoice number, statement number, account code, comments (snippet) | **"Standard Form for Presentation of Overcharge Claim"** to overchargeclaims@rlcarriers.com | Tariff: in writing within 180 days of shipment (refund context) | Not stated | "Freight Bill No(s)"; "Basis for overcharge claim or tariff authority"; "Charges should be"; bond of indemnity; BOL "or copy of electronic bill of lading manifest", vendor invoice, catalog pages, packing slip or receiving reports | N-AK19 *verified*; N-AK20 *assumed* |
| **SEFL** | — | Download the form; email it "with any backup" | Not found | "Every effort will be made to process your claim within 30 days of receipt" | Backup documents | N-AK22 *verified* |
| **TForce** | — | Form by mail or overchargeclaims1@tforcefreight.com | "within 180 days of receipt" (tariff: receipt = 10 days after tender) | Acknowledge "within 30 days"; resolve "within 120 days" | Freight bill copy **or a list of freight bill numbers**; "Tariff authority or reason"; supporting documents; **"Only the payer of the original freight charges can file an overcharge claim"** | N-AK21 *verified* |
| **AAA Cooper** | — | Overcharge claim form; fax 855-263-6298; cargoclaims@aaacooper.com | 180 days from the shipment date, "by the responsible party" | Not found | — | N-AK23 *assumed* |

**Note [our call]:** TForce's "within 120 days" is longer than 49 CFR 378.8's 60 days to "pay, decline to pay, or settle". Whether Part 378 binds contract freight is a question for a lawyer; check T flagged the same issue for 14705.

### 5.3 Response times in one place

| Who | Stated response | Label |
|---|---|---|
| ABF Freight Bill Review | Within one hour, for most inquiries | *assumed* (snippet) |
| Estes discrepancy tool | 24-48 hours | *assumed* (carrier claim) |
| FedEx Freight | Case number by automated email; no time stated | *verified* |
| SEFL | 30 days | *verified* (stated) |
| XPO | 60 days | *verified* (stated) |
| TForce | Acknowledge in 30 days; resolve in 120 | *verified* (stated) |
| 49 CFR 378 | Acknowledge in 30 days; decide in 60 | *verified* |
| Brokers | "a couple days to a couple months" | *assumed* (check T) |
| One small importer | "months" per dispute | *verified* as its letter's text (check T) |

### 5.4 Many shipments in one claim

- **The regulation allows it:** 378.3(b) lets one claim cover many shipments with "the same tariff issue or authority or circumstances" (*verified*, N-T05).
- **Carriers' forms and tools accept it** (*verified*):
  - ABF's form has multiple PRO, date and amount lines.
  - R+L asks for "Freight Bill No(s)".
  - TForce accepts "a list of freight bill numbers".
  - Estes takes 20-100 discrepancies per batch.
- **Not found:** whether grouped claims succeed more or less often than single ones.

### 5.5 What a dispute packet should contain (built from the carriers' own forms)

| # | Element | Why | Source, label |
|---|---|---|---|
| 1 | Claimant name, address and payee; **our own claim number** | ABF asks the claimant to number each claim, for "all correspondence" | N-AK17 *verified* |
| 2 | Carrier account number, PRO(s), bill dates, amounts billed and paid | Required by FedEx Freight (account) and all claim forms | N-AK25, N-AK17, N-AK19 *verified* |
| 3 | Nature of the error, in the carrier's own category | ABF's categories (weight, rate, classification, discount); FedEx's types | *verified* |
| 4 | **Authority:** the agreement clause and **version effective date**, the tariff item, the quote number | ABF: "reference tariff, item number, effective date". Eller cites "MRA clause + NMFC item + 49 USC 13710". A GSA notice "cites applicable contract, tariff, or tender, along with other data relied on" | *verified*; GSA *assumed* (snippet) |
| 5 | **"Charges should be":** weight × rate = extension per line, and the difference | ABF and R+L forms | *verified* |
| 6 | **Evidence:** the original BOL (TForce: a re-typed BOL is "NOT acceptable"); the vendor invoice or packing slip plus a **pre-printed** spec sheet or catalog page; the W&R certificate; the delivery receipt with times; the lumper receipt; the rate confirmation or quote; the accessorial approval, or its absence | Carriers' proof rules | *verified*, check T §3.2; N-AK17, N-AK19 |
| 7 | Proof of payment, or a bond of indemnity | ABF and R+L; XPO needs payment first | *verified* |
| 8 | Authority to act (the claimant's agent) | 378.2(f); TForce's payer-only rule | *verified* |
| 9 | For batches: one spreadsheet row per PRO with the same fields | Estes accepts spreadsheets; its template was not read | **[our call]** |

### 5.6 What makes disputes fail, and how carriers react to volume, automation or wrong claims

- **What fails** (check T §6, not redone): re-typed BOLs, an NMFC code that is in fact correct, late filing, offsetting, small downward corrections.
- **Added here** (*verified*):
  - XPO needs the bill paid first;
  - TForce lets only the payer file;
  - ABF needs the original paid bill or a bond of indemnity;
  - ODFL closes a claim 30 days after its ruling and charges $50 on no-fault settlements.
- **Reaction to automated or high-volume claims: no LTL carrier statement found** (search 42). Indirect signals:
  - **(a)** the parcel carriers' payer clauses (*verified*);
  - **(b)** ODFL's no-fault fee (*verified*);
  - **(c)** Estes built a 100-row batch tool, so structured volume is accepted (*verified*);
  - **(d)** overreaching look-backs end in court: Exist v. SEFL; Amazon's demand on Central Freight was cut by about 46% for falling outside the window (check AC; *assumed*, as one party's account).

---

## 6. AK5 · Alerts and ease of use: what users value and complain about

### 6.1 What users value

| Want | Evidence (reviewer role, industry, date) | Label |
|---|---|---|
| An alert when an invoice is waiting for approval | Intelligent Audit reviewer wants alerts "as and when the invoice is pending approval" | *assumed*, N-Z32 |
| **Emails with a direct link** to the item | "I like that I receive emails that have a direct link to open and approve with ease" (operations manager, security, 2024-12-16); "automated email reminders that I need to take action on certain Invoices" (IT manager, 2025-03) | *assumed*, N-AK43/44 |
| Due and overdue reminders | "love the reminder from stampli that invoice is due or overdue" (hospital supply, 2025-01-29) | *assumed* |
| **Conversation on the invoice** | "Approvers can comment, tag others, and see the full context of an invoice" (controller, software, 2026-03); "The ability to ask questions of vendors and employees within Stampli is highly useful" (construction, 2024-11-18) | *assumed* |
| Approve and pass along | "approve and pass along to the next in the chain of command" (terminal manager, trucking, 2025-01-15) | *assumed* |
| Digests | FreightPOP's "Friday email"; 71lbs's "weekly email summary" | *verified* (product pages) |
| Chat and mobile approval | Ramp: approve, edit or reject bills "directly in Slack"; mobile approval (snippet) | *verified*; mobile *assumed* |
| Seeing discrepancies easily | Freightview: "Invoicing is easy to view, navigate, and notice discrepancies" | *assumed*, N-Z40 |
| Deadline tracking, carrier scorecards, contract-renewal help | **No user quotes found.** Vendors claim dashboards of "cost drivers, trends, and areas of risk" (TransImpact) | *verified* as a vendor statement |

### 6.2 Common complaints

| Complaint | Evidence | Label |
|---|---|---|
| Coverage gaps | Audit tab "only shows some freight companies, not all the carriers we work with" | *assumed*, N-Z40 |
| Manual filters | "a lot of steps to create the custom filter" | *assumed*, N-Z40 |
| Not smart enough | "auditing function could be more intelligent and automated" | *assumed*, N-Z40 |
| Unclear exceptions, weak support | Trax: "low confidence in support and exception clarity" | *assumed*, N-Z37 |
| Reporting | U.S. Bank: reports built in Cognos are "not being easy" | *assumed*, N-Z27 |
| OCR misses and recoding | "the 'bot' that scans bills … sometimes struggles with unusually-formatted vendor invoices"; AvidXchange: "We have someone dedicated to recoding invoices" | *assumed*, N-AK44, N-Z65 |
| Slow search | "Searching can be a little frustrating sometimes slow" | *assumed*, N-AK43 |
| Onboarding lag | Orca: "initial onboarding lag" | *assumed*, N-Z35 |

### 6.3 False positives and alert load

- **Freight-specific false-positive rates: none found** (search 35). Vendor statements only:
  - queues "full of false positives that reviewers stop trusting";
  - "below 5%" for "well-calibrated" duplicate detection;
  - Stampli: high performers push exceptions "into the low single digits", while unmanaged teams "can see a fifth of invoices or more" (*assumed*, N-AK39, N-AK58).
- **General AP benchmark:** an average exception rate of **18.4%**; best-in-class "47% lower", about **9.8%** [our calc] (Ardent Partners, State of ePayables 2025, posted 2026-01-22; *verified* extraction, N-AK45, re-checked).
- **Freight load [our calc]:**
  - On the ABF set, **59 of 101 bills (58%)** carry a line that needs a document, about **3.2×** the AP average.
  - At 2.21 bills per $1,000 of spend (N-PA01), each **$1M of LTL-heavy spend** means about **2,210 bills a year**, of which about **1,290** need a document. That is about **5 a working day**; a $5M account would see about **26 a day** if each were shown separately.
  - Grouped by cause, the ABF quarter has about **13 issue groups**: 10 accessorial types, reweighs, restored weights and corrected bills.
- **[our call]:** grouping, not per-bill alerts, is the difference between a queue people use and one they ignore.

---

## 7. AK6 · The ease-of-use bar for a mid-sized shipper

### 7.1 What vendors require to start

| Vendor type | What they ask for | Time to start | Label, source |
|---|---|---|---|
| FAP (TransImpact) | Invoices "via EDI, API, email, or carrier portals"; "Your negotiated carrier contracts and rate agreements"; shipment data from TMS, ERP or WMS (BOLs, POs, delivery records); APIs, EDI or SFTP | "4-6 weeks" | needs *verified*; timing *assumed*, N-AK47 |
| FAP (CT Logistics) | Carriers' bills redirected by mail, FTP, a custom email address, CSV, Excel, X12 EDI and so on | Not stated | *verified*, N-AK48 |
| Enterprise FAPs | 4-12 weeks; Trax "3 to 6 month" | — | *assumed* (checks AA, Z) |
| Agent-led (Loop) | Policies configured in Loop; carriers may send invoices to a Loop inbox | "measurable recovery within weeks" | *assumed* |
| Contingency LTL (Eller) | Works from the master rate agreement, "BOL + reweigh tickets + inspection records" and delivery receipts; "Your first audit is free" | Not stated | *verified* (page says), N-AK46 |
| Competitive audit bid | "a complete & current 30-90 day sampling of invoices", plus business rules and SOPs | — | *assumed* (snippet) |
| SMB booking tool (MyCarrier) | Shipments booked in the tool; a QuickBooks Online connection; "nothing to configure" | Self-serve | *verified*, N-AK02 |
| Parcel (71lbs, LateShipment) | Carrier website logins; "No changes need to be made to your current shipping accounts" | Dashboard "by week 2" | *assumed* (snippet), *verified* (feature) |
| AP (Ramp, Stampli) | Connect an AP inbox (Gmail). Stampli: "deploy in weeks", about $2,000 implementation | — | *verified*, N-AK40; *assumed* (check AA) |

### 7.2 Lightest-touch options found

- a forwarding inbox (CT Logistics, Loop, Ramp);
- carrier logins only (parcel);
- "first audit free" (Eller);
- contingency only, with weekly summaries (71lbs);
- a one-way accounting sync (MyCarrier to QuickBooks Online).

**[our call]:** an audit-only v1 needs **no** bill-to change, carrier enrolment or ACH. It does need:
- every agreement version;
- the invoices;
- BOLs where they exist;
- **authority to act as agent** for carrier portals and claims, asked for only when a dispute needs it.

### 7.3 Who does what: vendor or customer, approval or auto-file

| Model | Who decides a flagged line | Who files | Who answers "did this happen?" | Examples | Label |
|---|---|---|---|---|---|
| **A. Customer reviews in a portal** | The shipper's user | Provider or shipper | Shipper | Cass FBA; Freightview Yes/No; FreightPOP password override | *verified* |
| **B. Provider's analysts** | Vendor auditors ("routed to experienced freight audit professionals"; providers "manage the entire dispute lifecycle") | Provider | The provider asks the shipper (process not published) | nVision, TransImpact | *verified* (pages say) |
| **C. Agents within rule-set limits** | Rules; complex cases flagged "rather than sending automatically" | Agent, by email | Humans, for complex cases | Loop, Trax | *verified* (pages say) |
| **D. Auto-file, report afterwards** | Provider | Provider | — | 71lbs weekly summary | *verified* |
| **E. Judgement queue** | A human | — | "an accessorial charge not in your contract, but the charge may reflect a service actually performed": the **"did you request a liftgate?"** case | Intelligent Audit | *verified* (page text) |
| **Outcome comparison** | **Not found** | — | — | — | — |

---

## 8. Design implications for the audit machine **[our call]**

1. **Review the shipment packet, not just the invoice.**
   - One screen holds the bill, the agreement *version* used, the quote or rate confirmation, the BOL, the delivery receipt or POD, the W&R certificate and the lumper receipt.
   - A **document strip** marks each as present, missing or not needed.
   - Most of the money depends on documents the bill doesn't carry (59 of 101 ABF bills).
2. **Highlight each charge line on the bill image and explain it in one line,** in the shape users know: "Billed $X | Should be $Y | Difference $Z | Rule: Agreement v3 (effective 2022-06-08), FAK item | Evidence: BOL line 2". Clicking a highlight opens the matching line in the other document, side by side (nVision's card; Cass's image plus dialog).
3. **Sort every finding into four outcomes:**
   - **Clear:** auto-approve inside tolerance.
   - **Ready to dispute:** the amount and the authority are computed.
   - **Needs a document:** fetch it from the carrier portal as the bill-to party's agent, or ask for it.
   - **Needs your answer:** one yes/no question with the BOL shown, e.g. "Did you order a liftgate for this delivery?"

   Only the last two reach the customer (Intelligent Audit's paths; Cass's reprocess / adjust / reject).
4. **Group findings by cause and carrier.**
   - One decision and one packet covers "Fuel % above table: 23 bills, $412 (Saia)", as 378.3(b), the carriers' forms and the batch tools allow (Estes up to 100).
   - Show the **cause to fix** as well, e.g. "add the quote number to the BOL" or "put per-pallet dimensions on the BOL".
5. **Set tolerances per charge type, in % and $.**
   - Strict on accessorials.
   - Keep negative-variance protection.
   - Show why each bill was auto-approved (FreightPOP; Freightview's export flag).
   - Start conservative until the customer has seen a month of results.
6. **Detect duplicates on PRO + BOL + carrier, never on amount and date alone,** since that fails on minimum-charge accounts.
   - Show the suspected original side by side.
   - Check across 3PL and carrier bills.
   - Check against AP payment records (Stampli's staged checks; the IN Holdings case).
7. **Store agreements as versions with effective dates.** Always show which version and fuel table were applied, and let the user correct it. This is the real work on the SEFL account.
8. **Build packets in the carriers' standard-form layout:**
   - our claim number;
   - the PRO list;
   - the nature of the error;
   - the authority (clause, item, effective date);
   - "charges should be" (weight, rate, extension);
   - attachments;
   - a note of proof of payment, or a bond of indemnity.

   Keep a **carrier directory** of channels, required fields and windows (§5.2), so each packet goes the carrier's way: Estes's batch tool, FedEx's dispute types, Saia's two inboxes, XPO's portal after payment.
9. **Recommend the route per bill:** dispute before payment for open bills, claim after payment for paid ones, **never short-pay** in v1. Tariffs bar offsets, and XPO requires payment before a claim.
10. **Run a deadline engine.**
    - For every flagged bill, compute the **shortest clock** that applies:
      - XPO guaranteed refunds in 15 days;
      - corrected BOLs in 30 days;
      - 180-day windows, each starting from its tariff's own date;
      - ODFL closing claims 30 days after its ruling.
    - Alert before each clock runs out.
    - Track the carrier's own deadlines too (378's 30-day acknowledgement and 60-day decision) and nudge when they are late.
11. **The customer approves every packet before filing in v1.**
    - One click per group, showing the dollars and the evidence.
    - File in the customer's name as authorised agent (378.2(f)), from their account or address, with a letter of authority.
    - Rules can come later (e.g. "auto-file fuel-table errors under $X").
    - Why: wrong claims cost something (ODFL's $50; closed claims), TForce takes payer-only filings, and the parcel carriers showed they will refuse third-party filers.
12. **Default to one daily or weekly digest.**
    - Send real-time alerts only for deadline-critical items.
    - Every email deep-links to the exact item, which reviewers single out.
    - Offer Slack or Teams and mobile approval (FreightPOP's Friday email; 71lbs's weekly summary; Ramp's Slack).
13. **Watch precision.** Record every dismissed flag by rule and carrier, and retire or retune noisy rules. The aim is a "needs you" count far below the AP average of 18.4% of invoices; grouping (§6.3) is the lever.
14. **Be honest about coverage.** List which carriers and bills could not be fully checked, and why: no agreement loaded, no base rates, no mileage engine. That answers the "only shows some carriers" complaint up front.
15. **Keep onboarding light:**
    - a forwarding inbox for bills;
    - PDF upload of agreements;
    - an optional AP export from QuickBooks or NetSuite, for duplicates and payment dates;
    - **no bill-to or payment changes**;
    - carrier-portal authority asked for per dispute.
16. **Keep an audit trail and close the loop.**
    - Every decision records a standard reason, the user and the time.
    - Track each recovery to the credit memo or refund on the next carrier statement; a contingency fee depends on proven recovery.
    - Export approved amounts and GL codes to AP. GL and accrual checking can come in a later version.
17. **Truckload specifics:**
    - compare against the rate confirmation;
    - check that accessorials were "authorized and approved prior to or at time of occurrence" (C.H. Robinson wording);
    - ask the dock for in and out times for detention;
    - require a receipt for lumper charges.

    Mileage checks wait until a mileage engine is licensed.
18. **Show undercharges as well as overcharges,** e.g. bills far below the quote (FreightPOP's negative-variance rule). Carriers can rebill within 180 days anyway, and showing both builds the trust that customer approval depends on. It produces no fee under contingency.

---

## 9. Sources

All accessed 2026-10-03. Access: "full" = the document was read directly (PDF text or page image); "extraction" = the page was read through the fetch tool's summary; "snippet" = search-result text only.

| ID | Title / publisher | Date on page | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AK01 | Freightview, "Auditing Invoices" | updated 2026-07-17 | https://blog.freightview.com/introducing-auditing-with-freightview | extraction | Queues, actions, Invoice Matching add-on |
| N-AK02 | MyCarrier, "Tips for Setting Up Invoice Hub Essentials" | 2026-08-07 | https://go.mycarrier.io/blog/tips-for-setting-up-invoice-hub-essentials | extraction | Quote comparison, disputes, QBO sync, tiers |
| N-AK03 | FreightPOP, "Freight Invoice Auditing Software" | n.d. | https://www.freightpop.com/freight-auditing-software | extraction | Thresholds, actions, Friday email, GL rules |
| N-AK04 | 41 CFR 102-118.140 (Cornell LII) | current | https://www.law.cornell.edu/cfr/text/41/102-118.140 | full | Audit programme elements (b), (d), (g), (h), (i) |
| N-AK05 | 41 CFR 102-118.145 | current | https://www.law.cornell.edu/cfr/text/41/102-118.145 | full | Audit methods |
| N-AK06 | 41 CFR 102-118.160 | current | https://www.law.cornell.edu/cfr/text/41/102-118.160 | full | 7-day adjustment notice |
| N-AK07 | 41 CFR Part 102-118 and Subparts D, E (index) | current | https://www.law.cornell.edu/cfr/text/41/part-102-118 | index pages | Structure after the 2024 rule |
| N-AK08 | GSA, Postpayment Audits; Disputes Resolution | n.d. | https://www.gsa.gov/buy-through-us/products-services/transportation-logistics-services/transportation-audits/postpayment-audits | snippet (fetch 404/403) | Audit scope; Notice of Overcharge wording |
| N-AK09 | Intelligent Audit, "Freight Audit Parameter Design" | "7.2.26" | https://www.intelligentaudit.com/blog/freight-audit-parameter-design-building-validation-logic-that-scales | extraction | Tolerances; three exception paths |
| N-AK10 | nVision Global, "AI-Driven Freight Audit and Payment" | n.d. | https://corporate.nvisionglobal.com/campaigns/ai-driven-freight-audit-payment/ | extraction | 200+ checkpoints; exception card |
| N-AK11 | nVision Global, "Eight Requirements of a Completed Transportation Record" | Aug 14 (year not shown) | https://corporate.nvisionglobal.com/the-eight-requirements-of-a-completed-transportation-record/ | extraction | GL, documents, approval, audit trail |
| N-AK12 | XPO, "How to file Claims and Refunds" | n.d. | https://www.xpo.com/help-center/claims-and-refunds/how-file-claims-and-refunds/ | extraction (re-checked 2026-10-03) | Overcharge claims; pay first; 60 days |
| N-AK13 | XPO, "Guaranteed Freight Delivery Services" | n.d. | https://www.xpo.com/help-center/premium-services/guaranteed-freight-delivery-services/ | extraction | Fee refund within 15 days |
| N-AK14 | ArcBest, "Dynamic LTL Pricing" | 2020-05 (URL path) | https://arcb.com/sites/default/files/2020-05/Dynamic%20LTL.pdf | full (page images) | All-in rate incl. special services |
| N-AK15 | ODFL, "Invoices & Claims" | n.d. | https://www.odfl.com/us/en/resources/invoices-claims.html | extraction | Claim by PRO; status; invoices |
| N-AK16 | Saia, "Billing and Payment Options" | n.d. | https://assets.ctfassets.net/kjv8gs2ccggb/5gWWPZxzAorrUK64ikFbJ6/43fc73def6e4125e607f1abe04afcf8a/SaiaBillingAndPayment_Options.pdf | full (page image) | fbreview@ / csdispute@ |
| N-AK17 | ABF, Overcharge Claim Form | 2017 (file name) | https://arcb.com/sites/default/files/forms_and_documents/OverchargeClaimForm%20-%20Fillable2017.pdf | full (page images) | Fields; evidence; bond of indemnity |
| N-AK18 | ABF Freight Bill Review (search summary) | n.d. | not identified | snippet | "within one hour" |
| N-AK19 | R+L, Standard Form for Presentation of Overcharge Claim | n.d. | https://rl-cdn.com/docs/rlc/shipping-forms/overcharge-claim-form.pdf | full (page image) | Fields; evidence; email |
| N-AK20 | R+L BillPay contact form | n.d. | https://billpay.rlcarriers.com/BillPay/Contact | snippet | Billing-dispute fields |
| N-AK21 | TForce Freight, "Overcharge Claim Information" | n.d. | https://www.tforcefreight.com/ltl/apps/OverchargeClaimInformation | extraction | Payer only; 30/120 days |
| N-AK22 | SEFL, Overcharge Claims Form Entry | n.d. | https://www.sefl.com/Claims/overChargeClaimsFormEntry.jsp | extraction | Email with backup; 30 days |
| N-AK23 | AAA Cooper rules tariff and document page (search summary) | n.d. | https://www.aaacooper.com/Document-Downloads | snippet | 180 days; channels |
| N-AK24 | Estes, Freight Shipping FAQs | n.d. | https://www.estes-express.com/resources/frequently-asked-questions | extraction | Batch 20/100; 24-48 hours |
| N-AK25 | FedEx Freight, "Dispute a Charge or Invoice" | n.d. | https://www.fedexfreight.com/en-us/manage-account/dispute-charge | extraction (re-checked 2026-10-03) | 9 dispute types; required fields |
| N-AK26 | Tai Software KB, "TriumphPay Audit" | n.d. | https://learn.tai-software.com/knowledge/triumphpay_audit | extraction | Variance list; exceptions; sync |
| N-AK27 | Triumph, "Product Spotlight: POD Detection" | 2024-04-11 | https://triumph.io/blog/broker/product-spotlight-pod-detection/ | extraction | POD checks; 75% claim |
| N-AK28 | UPS, Terms and Conditions of International Service (Brazil edition) | not shown | https://www.ups.com/assets/resources/webcontent/en_US/terms_service_br.pdf | full (PDF text) | Payer clause; 15-day notice |
| N-AK29 | FedEx Service Guide, Terms and Conditions, International (U.S. edition) | effective 2021-01-04 | https://www.fedex.com/content/dam/fedex/us-united-states/services/SG_TermsCond_Intl_2021.pdf | full (PDF text) | Third-party clause; payer-only credits |
| N-AK30 | Shipping Coach (blog), "What Every Shipper Ought to Know About Shipping Refunds…" | 2010-03-13 | https://shippingcoach.wordpress.com/2010/03/13/what-every-shipper-ought-to-know-about-shipping-refunds-guaranteed-service-refunds-parcel-auditors/ | extraction | Clauses in 2010 Service Guides |
| N-AK31 | FedEx, Money-Back Guarantee page | 2026 | https://www.fedex.com/en-us/service-guide/money-back-guarantee.html | extraction | Suspension and reinstatement dates |
| N-AK32 | Refund Retriever, "UPS Money-Back Guarantee" | n.d. | https://www.refundretriever.com/ups-guarantee/ | extraction | Quotes the UPS clause |
| N-AK33 | 71lbs, FAQ | n.d. | https://www.71lbs.com/faq/ | extraction | Weekly summary; dashboard; contingency |
| N-AK34 | LateShipment / 71lbs (search summaries) | n.d. | https://www.lateshipment.com/solutions/fedex/refunds/ | snippet | Credentials; 160-point checks |
| N-AK35 | Loop, "Exception agent" | n.d. | https://www.loop.com/technology/exception-agent | extraction | Agent behaviour; human review; claim |
| N-AK36 | Trax, "Contextual AI for Complex Freight Audit Exception Management" | 2025-05-12 | https://www.traxtech.com/blog/traxs-contextual-ai-for-complex-freight-audit-exception-management | extraction | Grouping; autonomy rules |
| N-AK37 | Trax and CTSI comparison pages (Worldmetrics, Gitnux) | 2026 | https://worldmetrics.org/best/freight-auditing-software/ | snippet | Context only |
| N-AK38 | Stampli, "How Stampli Helps Prevent Duplicate Payments" | n.d. | https://www.stampli.com/blog/news/prevent-duplicate-invoice-payments/ | extraction | Three-stage duplicate checks; warning UI |
| N-AK39 | Stampli, "Invoice exceptions and holds" | n.d. | https://www.stampli.com/resources/invoice-exceptions-and-holds/ | extraction | Exception types; owners; SLAs |
| N-AK40 | Ramp, "AP Agents available in Ramp Bill Pay" | n.d. | https://support.ramp.com/ap-agents-available-in-ramp-bill-pay | extraction | Agents; recommendations only |
| N-AK41 | Ramp, "Set up Ramp's Slack integration" | n.d. | https://support.ramp.com/hc/en-us/articles/360052081394-Set-up-Ramp-s-Slack-integration-for-Admins | extraction | Approve/edit/reject in Slack |
| N-AK42 | BILL approval policies and duplicate checks (search summaries); help article (certificate error) | n.d. | https://help.bill.com/direct/s/article/360000017963 | snippet | Policies; duplicate check |
| N-AK43 | Capterra, Stampli reviews, page 2 | 2025-2026 | https://www.capterra.com/p/147301/Stampli/reviews/?page=2 | extraction | 4.8 from 463; quotes |
| N-AK44 | Capterra, Stampli reviews, page 4 | 2024-2025 | https://www.capterra.com/p/147301/Stampli/reviews/?page=4 | extraction | Reminder and OCR quotes |
| N-AK45 | Ardent Partners, "State of ePayables (Part Nine)" | 2026-01-22 | https://payablesplace.ardentpartners.com/2026/01/state-of-epayables-part-nine-ap-benchmarks-and-best-in-class-performance/ | extraction (re-checked 2026-10-03) | 18.4% exception rate |
| N-AK46 | Eller Audit, "LTL Freight Audit" | n.d. | https://www.elleraudit.com/ltl-freight-audit | extraction | Dispute drafting; first audit free |
| N-AK47 | TransImpact, "Freight Audit & Pay" | n.d. | https://transimpact.com/solutions/freight-audit-pay | extraction | Requirements; 4-6 weeks |
| N-AK48 | CT Logistics, "Freight Bill Audit Service" | n.d. | https://www.ctlogistics.com/freight-audit-services/freight-bill-audit-service | extraction | Invoice redirection options |
| N-AK49 | Microsoft Learn (AX 2012 R3), "Set up an audit master for freight reconciliation" | 2014-04-18 | https://learn.microsoft.com/en-us/previous-versions/dynamicsax-2012/appuser-itpro/set-up-an-audit-master-for-freight-reconciliation | full | Tolerance; over/under reason codes |
| N-AK50 | Cass, "Enhancements to Freight Bill Authorization (FBA) on CassPort" | 2009-09-01 | https://my.cassport.com/tutorial/FBAEnhancementsTutorial.pdf | full (PDF text) | Shipper exception screens; 13 reasons |
| N-AK51 | Cass freight invoice management (search summary) | n.d. | https://www.cassinfo.com/freight-audit-payment/services/freight-invoice-management/ | snippet | Suspense function; "Client Resolution" |
| N-AK52 | ICC Logistics, Freight Audit Checklist | n.d. | https://icclogistics.com/resources/checklists/freight-audit/ | extraction | Checklist sections |
| N-AK53 | Freightview "Invoice Matching" (search summary) | n.d. | https://blog.freightview.com/introducing-auditing-with-freightview | snippet | AI auto-accept |
| N-AK54 | Volume-quote guides (FreightPros, InTek, Ascent; search summaries) | n.d. | https://www.freightpros.com/whitepaper/ltl-volume-quotes/ | snippet | Quote number on BOL |
| N-AK55 | GetApp TMS.ai; Vooma/Raft comparison pages (search summaries) | 2026 | https://www.getapp.com/transportation-logistics-software/a/rose-rocket/ | snippet | DataBot; agents; document volume |
| N-AK56 | Denim, Peregrine success story | n.d. | https://www.denim.com/success-stories/peregrine | extraction | 3 minutes to under 1 minute |
| N-AK57 | IOFM, "Freight Audit and Payment Best Practices — The Basics" | n.d. | https://www.iofm.com/ap/process-improvement/payment/freight-audit-and-payment-best-practices-the-basics | snippet (403) | Duplicate-handling advice |
| N-AK58 | ODFL contacts; duplicate-detection false-positive pages (search summaries) | n.d. | https://www.odfl.com/us/en/resources/freight-knowledge/old-dominion-faqs.html ; https://www.docsumo.com/blog/duplicate-invoice-detection | snippet | ODInvoicing@; claim times; "below 5%" |

**Earlier sources reused:**
- N-Y03 (job postings);
- N-Z16, N-Z17, N-Z18, N-Z20, N-Z22, N-Z25, N-Z27, N-Z32, N-Z35, N-Z37, N-Z40, N-Z41, N-Z47, N-Z50, N-Z55, N-Z65, N-Z73, N-Z74, N-Z76, N-Z84;
- N-T05 and N-T17 to N-T30 (49 CFR 378 and the rules tariffs);
- N-PA01, N-PA02 (practice audit);
- N-AC02, N-AC08, N-AC09, N-AC12, N-AC24, N-AC36;
- N-AB41 (ATRI detention).

---

## 10. Could not access, or not found

**Blocked or failed:**
- GSA pages: gsa.gov Postpayment Audits and Disputes Resolution returned 404; origin-www.gsa.gov returned 403.
- eCFR redirected to a bot-check, which was not followed; Cornell LII was used instead.
- IOFM article: 403.
- UPS US Terms of Service PDF: bot-protected (a 30-byte token); the international (Brazil) edition was used instead.
- BILL help article: TLS certificate error.
- Saia claims and FAQ pages, and Estes's discrepancy-tool page, rendered empty (JavaScript); the Saia PDF and the Estes FAQ were used.
- Werner tariff: the fetch returned a landing page, so the mileage basis and the TONU price could not be read.
- ABF Freight Bill Review page: not found; arcb.com/node/7741 is a cargo-claims guide.
- Gartner, G2, TrustRadius and Reddit: not retried (blocked in check Z).
- SEC EDGAR: not attempted (it requires a declared identity).

**Not found:**
- checklists from NITL, TIA, NASSTRAC or AST&L, and community-college course material;
- first-hand step-by-step accounts from clerks at small or mid-sized shippers, beyond job postings;
- any LTL carrier statement on automated or high-volume audit claims;
- when UPS and FedEx introduced the payer clauses;
- any comparison of customer-approval and auto-file outcomes;
- neutral false-positive rates for freight audit;
- public truckload mileage-basis clauses and TONU prices;
- guaranteed-refund terms for ODFL, Estes and Saia (only XPO was read);
- the typical dollar value of guaranteed-service refunds, wrong-payer bills and mileage errors.

**Not researched (budget):**
- shipper-side screens at U.S. Bank, CTSI, Freehand and Pando;
- Tipalti, AvidXchange and Medius review screens;
- Shipwell's audit features; Shipware;
- Freightview's carrier-coverage rules in its help centre.

**Searches run (48):**
1. Freightview help invoice audit tab variance quote approve dispute carrier invoices
2. MyCarrier invoice hub audit help center invoice discrepancies quoted vs invoiced
3. FreightPOP freight audit invoice reconciliation help article variance tolerance approve
4. freight bill audit checklist NASSTRAC OR NITL OR "AST&L" training freight payment auditing course
5. "freight bill" audit procedure accounts payable "short pay" carrier invoice tolerance "within" approve policy manufacturer SOP
6. community college logistics course "freight bill auditing" lesson OR syllabus OR chapter
7. GSA Transportation Audits postpayment audit "Notice of Overcharge" … 41 CFR 102-118
8. IOFM OR "AP Now" freight invoices accounts payable tips …
9. nVision Global freight audit "audit checks" OR "audit rules" …
10. Cass freight audit "exception" rules tolerance …
11. Intelligent Audit freight audit checks list "guaranteed service" …
12. LTL guaranteed service "refund" OR "credit" … tariff item
13. volume quote spot quote LTL "quote number" must be on bill of lading …
14. Old Dominion ODFL "billing dispute" …
15. Saia "invoice dispute" …
16. ABF Freight "billing inquiry" …
17. R+L Carriers "billing dispute" …
18. TForce Freight "invoice dispute" …
19. AAA Cooper OR Southeastern Freight Lines "billing dispute" …
20. Estes "Rating and Billing Discrepancies" …
21. FedEx Freight "billing dispute" …
22. HubTran TriumphPay carrier invoice audit …
23. Vooma OR Raft OR Denim carrier invoice processing …
24. UPS tariff terms "third party" auditor refund request …
25. FedEx Service Guide third-party auditors …
26. "based on information obtained by, a party other than the payer" UPS
27. "third party other than the payer of the charges" FedEx money-back guarantee auditor
28. LateShipment.com OR 71lbs how it works …
29. Loop freight audit platform exceptions …
30. Trax OR CTSI-Global freight audit exception management …
31. Stampli help center invoice page …
32. BILL help "duplicate invoice" detection …
33. Ramp bill pay help duplicate bill detection …
34. Capterra Stampli reviews cons notifications …
35. invoice exception "false positives" duplicate detection alert fatigue …
36. Capterra OR G2 reviews freight audit Cass OR Trax OR CTSI OR nVision …
37. freight audit payment implementation "letter of authority" …
38. post-payment freight audit contingency "what we need" …
39. freight audit firm "your approval" before filing claims …
40. truckload freight audit mileage verification PC*Miler …
41. freight audit "freight terms" prepaid collect inbound vendor …
42. carrier overcharge claims from freight audit firms frivolous …
43. "logistics coordinator" OR "freight bill" clerk how I audit freight invoices …
44. Cass freight payment shipper "approval" exceptions "CassPort" …
45. Freightview "invoice matching" auto-accept threshold …
46. invoice approval Slack OR "Microsoft Teams" notification …
47. Vooma OR "TMS.ai" OR "Rose Rocket" OR Raft carrier invoice audit agent …
48. Ardent Partners "invoice exception rate" …
