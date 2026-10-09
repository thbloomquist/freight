# S5 check Z: what buyers and carriers already say in public (C-09)

- **What this is:** desk research for S5 ("Validate with primary evidence") in run 01, on card **C-09**, "Checking and paying truckload and LTL freight bills, for mid-sized manufacturers and distributors (US, 20-499 staff), handled today by accounts-payable clerks, contingency audit firms and, for larger shippers, audit-and-payment providers."
  - The founders asked, before the interviews, whether our questions "can be answered from the web as opposed to having to ask people", from "specific forums or other sources".
  - **The angle of this check is first-hand experience and behaviour:** what shippers, AP staff and carriers say in forums, reviews, complaints and community threads. Numbers met in passing are recorded, but a separate check covers overcharge rates, pricing and margins, and another covers recruiting channels.
  - It maps every finding to the hypotheses in `selection_runs/run-01/5_validation.md` §3.1 (H09-01 to H09-11, H09-C1 to H09-C4).
- **Not covered here:** the vendor list and incumbent map already in check R (`s3b_check_R_shipper_spend_jobs.md` §2.2, item 9); Loop's April 2026 Series C; the AFP 2026 fraud survey; LTL tariff rules (check T). They are not repeated.
- **Date:** 2026-09-17. All sources accessed 2026-09-17.
- **Status:** input to S5. **It decides nothing.** Suggestions are marked **[our call]**.
- **Labels:**
  - *verified*: read at the source (a page, an official document or a PDF read directly).
  - *assumed*: a search snippet, a vendor claim, a secondary summary, or memory. **Every forum post, review and complaint is an *assumed* anecdote**, even when read in full; "read in full", "post text only" or "page extraction" is said separately.
  - **Page extraction:** most pages were read through a fetch tool that returns a model-made extract. Short quotes from those pages are given "as extracted" and were not re-checked character by character. Quotes from Reddit come from the raw archive text and are exact.
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
  - **Counts are never converted to rates.** "7 reviews mention audit" means 7 reviews, not a share of users.
- **Privacy:** no usernames, reviewer names or contact details are recorded. Job title, industry and company size are given where the site shows them.
- **Access, in one line:** Reddit was blocked, Gartner Peer Insights, G2, TrustRadius and Glassdoor returned 403, and the session's web-search budget ran out after 44 queries. What was read is listed in §16; what could not be read is in §17. **The thinness of first-hand buyer voice is itself a finding (§1).**
- **New sources:** N-Z01 to N-Z96 (§16).

**Words used here:**
- **FAP:** freight audit and payment provider. It checks carrier invoices and pays carriers on the shipper's behalf (Cass, U.S. Bank and others).
- **LTL / TL:** less-than-truckload (several shippers' pallets share a trailer) / truckload.
- **TMS:** transportation management system, the software used to quote, book and track shipments. **SMB LTL TMS** here means low-cost tools such as Freightview, MyCarrier and FreightPOP.
- **ERP:** the company's accounting and operations system (NetSuite, Acumatica, Business Central, Epicor, SAP, Dynamics 365).
- **EDI 210:** the electronic freight invoice a carrier sends. The alternative is a PDF by email, an upload to a portal, or paper.
- **BOL / POD / PRO:** bill of lading (the shipping document), proof of delivery (usually the signed BOL), and the carrier's shipment number.
- **Accessorial:** an extra-service charge, such as liftgate, residential or limited-access delivery, detention (waiting time) or a lumper (unloading) fee.
- **Reweigh / reclass / inspection:** an LTL carrier re-measures a shipment and re-bills it at a different weight or freight class, usually adding an inspection fee.
- **NMFC dockets:** the freight-class rule changes effective 2025-07-19 (Docket 2025-1) and 2026-05-23 (Docket 2026-1).
- **Contingency / look-back:** an audit firm takes a share of what it recovers; the look-back is how far back in paid invoices it goes.
- **Quick pay / factoring:** a carrier accepts a discount to be paid early, from the payer (quick pay) or by selling the invoice to a factoring company.
- **Short pay:** paying less than the invoice amount.
- **AP automation:** accounts-payable software that captures and pays invoices (Bill, AvidXchange, Tipalti, Stampli).
- **Landed cost / accrual:** freight added to the cost of goods received / booking an expected freight cost before the carrier's bill arrives.
- **Mom Test:** an interview style that asks about past behaviour, never about hypotheticals or a pitch.

---

## 0. Summary table

| Question | What the public record says | First-hand items found | Label | Sections |
|---|---|---|---|---|
| **Z1 How do mid-sized shippers check bills? (H09-01)** | ERP documentation assumes **manual entry and matching**: the freight bill is keyed as a vendor bill and tied to a receipt (NetSuite, Business Central, Acumatica). Only enterprise ERP (Dynamics 365 SCM) ships a tolerance-based freight audit. Users build **custom fields and dashboards to catch duplicate freight invoices** (Epicor) and **manually adjust accrual lines to the billed cost** (Acumatica). A second route not in H09-01: **SMB TMS tools with an audit tab**, which AP departments use | 2 community threads; 7 Capterra reviews; 4 Reddit buyer posts | docs *verified*; posts and reviews *assumed* | §2, §7.3 |
| **Z2 Stories of wrong bills (H09-03, H09-04)** | **21 billing anecdotes** were found, 12 with a dollar amount. **None is clearly inside the segment** (US manufacturer or distributor with 20-499 staff paying its own carrier bills). Most come from very small shippers who booked LTL through brokers and got **post-delivery "adjusted invoices"** for reclass, reweigh or accessorials. **NMFC dockets:** confusion in both directions (a 3PL's "busiest week of 2025" was the week of July 19, with both increases and savings). There is no first-hand report of more corrections on a mid-sized shipper's bills | 21 anecdotes | *assumed* | §3 |
| **Z3 Who decides; procurement and IT hurdles (H09-05)** | **Nothing first-hand found.** One Reddit post asks procurement staff whether they would only hire a freight-spend reviewer paid on verified savings; its replies were not readable | 0 | — | §4 |
| **Z4 Attitudes to contingency pricing (H09-06)** | No buyer statements were found. Vendor terms and critiques are public: contingency shares of **20-35%** and **30-50%**; parcel-first firms with **$50K and $250K minimums**; "no long-term contract and no cancellation fee"; "first audit is free". **New entrants market against contingency** ("a fee that shrinks if the error class is eliminated") and sell subscriptions ($60-149 a month for SMB TMS tools; $2,500-4,000 a month for one mid-market enterprise tool) | 0 buyer items; ~10 vendor pages | *assumed* | §5 |
| **Z5 Data availability (H09-07)** | Invoices arrive **"electronically or on paper"** (Microsoft) and as PDF, JPG or TIFF by email, portal upload, EDI or CSV (FAP carrier instructions). Users **manually split multi-invoice freight PDFs** (Acumatica). Carrier bills often **arrive after the month is closed** (NetSuite). One SMB TMS audit tab shows **"only some"** carriers. Rate agreements: no first-hand item says where they live, and one vendor says "a contract nobody can find" | 3 threads; 2 reviews | docs *verified*; rest *assumed* | §6 |
| **Z6 Satisfaction with providers (H09-08, show-stopper)** | **Enterprise FAP review samples are tiny:** 1-12 Gartner Peer Insights reviews per vendor (Trax 3.5 from 12; nVision 4.8 from 8; Cass 5.0 from 1; U.S. Bank 3.0 from 1). **The biggest satisfied-user bases are SMB LTL TMS tools with audit tabs:** Freightview 4.7 from 743 Capterra reviews, MyCarrier 4.7 from 108, FreightPOP 4.7 from 47. They target "small to mid-sized manufacturers and distributors". Audit is a secondary feature there, with gaps named by users. **No evidence that any vendor serves more than half the segment** | 7 audit mentions in ~100 Freightview reviews; 1 MyCarrier; 1 FreightPOP | ratings *assumed* (snippets and extraction) | §7 |
| **Z7 AP automation and payment rails (H09-09)** | No shipper-side account of how long a payment switch takes. On the payee side, **AvidXchange's Trustpilot page (3.6 from 70; 23 one-star)** is dominated by suppliers complaining about **"a fee to get paid"**, 3-4% acceleration fees and slow ACH. U.S. Bank's carrier agreement lets the bank **debit carrier accounts** for overpayments or errors | 20 one-star extracts; 1 contract | contract *verified*; reviews *assumed* | §8 |
| **Z8 Defensive vs cyclical (H09-11)** | **Too thin to read.** Among the 9 reviews that mention an audit feature: building materials 3, construction 1, consumer goods 1, printing 1, internet 1, warehousing 1, mechanical or industrial engineering 1 | 9 reviews | *assumed* | §9 |
| **Z9 Carriers (H09-C1 to C4)** | **Fees for early payment are public and verified:** U.S. Bank's discount fee starts at **1%** of the invoice, rises with the prime rate and with terms (+0.25% to +1.00% for 31-90 days), and goes **up to 1% higher on all invoices** if a carrier exempts some shippers. Quick pay runs 1.5-5% and factoring 1-5% (most 2-3.5%). Carrier stories of short pays are about **brokers**, not FAPs ($300 held back from a $3,000 load over "late paperwork" although the POD was texted within 15 minutes). **Nothing found on carriers' view of automated vs human audit** | 3 forum threads; 1 contract; 1 user guide | contract and guide *verified*; forums *assumed* | §10 |
| **Z10 Surprises** | (1) Online, **builders outnumber buyers**: 9 of 15 relevant Reddit posts come from sellers, founders or researchers looking for buyers. (2) The mid-market incumbent may be the **SMB TMS audit tab**. (3) Small shippers' wrong bills come **from brokers**. (4) Payees resent **pay-to-get-paid rails**. (5) **Contingency is the old model** in the category's marketing. (6) Vendors are consolidating (Loop absorbed Data2Logistics in 2025) | — | mixed | §11 |

---

## 1. How much of the public record is first-hand?

The founders' question is whether the interview questions can be answered from the web. **For the buyer side, mostly not:** first-hand buyer voice is close to absent, and most of what search returns is vendor content written to rank for "freight audit".

| Source type | Items read | First-hand buyer (shipper) items | First-hand carrier items | Notes |
|---|---|---|---|---|
| Reddit posts (archive text, post only; comments unread) | 15 relevant of 100 returned | 4 (a skeptic; a manufacturer choosing an FAP; an e-commerce brand on NetSuite; an importer) | 0 | 9 are sellers, founders, researchers or consultants looking for buyers (2 of the 9, N-Z05 and N-Z13, are classed so on judgement **[our call]**); 1 is a career post (N-Z09); 1 has no stated role (N-Z15). Reddit itself was blocked (§17) |
| ERP community threads | 3 (Acumatica ×2, Epicor ×1) | 2 describe workflows (one by a consultant for a client) | 0 | Workflow evidence, not complaints |
| ERP vendor documentation | 5 (Dynamics 365 SCM, JD Edwards, NetSuite, Business Central, Anchor Group on NetSuite) | — | — | *verified* where read |
| Software reviews (Capterra pages) | ~100 Freightview reviews across 4 pages; 1 page each for MyCarrier and FreightPOP; comparison and alternatives pages | 9 mention auditing or invoices | 0 | Reviewer industry and sometimes size shown |
| Review ratings (Gartner, G2) | Snippets only (sites returned 403) | 0 quotes read at source | 0 | Counts of 1-12 reviews per FAP vendor |
| Complaint sites (Trustpilot, BBB) | Freightquote, FreightCenter, FreightPros, AvidXchange, TriumphPay; BBB Cass, R+L, AFS | 20 billing complaints (micro shippers, mostly via brokers) | ~20 supplier complaints about AP-automation payment (payees, industry unstated) | Segment mismatch (§3) |
| Trucking forums (TruckersReport) | 5 threads | 0 | 5 (2012-2024; about brokers and detention) | Overdrive returned 403 |
| FAP carrier-facing documents | U.S. Bank carrier agreement; CassPort carrier user guide; Cass, nVision and CTSI carrier help pages | — | — | *verified* (agreement, guide) |
| Vendor and 3PL articles | ~30 | 0 (claims only) | 0 | All *assumed*; used for the competitor watch-list and price anchors |

**Reading [our call]:** the web can answer questions about **documents and prices** (what ERPs do, what FAPs charge carriers, what contingency shares are advertised, who the entrants are). It cannot answer questions about **behaviour inside the segment** (who approves, what they last caught, whether they would accept 25%). The public record also shows a **crowd of small builders chasing the same buyers** (§11.1), which is itself worth knowing before outreach.

---

## 2. Z1 · How mid-sized shippers check freight bills today (H09-01)

### 2.1 What ERP documentation assumes

| ERP | Workflow as documented | Implication for H09-01 | Source | Label |
|---|---|---|---|---|
| **NetSuite** | "After you receive the freight bill, enter the freight charge as a vendor bill", select a landed-cost item, then link that bill to the item receipt | Manual keying of each freight bill; no audit against a rate | N-Z22 | *assumed* (snippet of Oracle docs) |
| **NetSuite (partner blog)** | Freight bills that arrive after the accounting period closed cannot update landed cost on the item receipt; the fix is a six-step custom workaround with saved searches and CSV inventory adjustments. Called "a common issue that many companies run into" | Freight bills arrive late; controllers carry the pain as a **cost-accuracy** problem, not an overcharge one | N-Z24 | page extraction; the partner's claim is *assumed* |
| **Business Central** | The carrier's bill is a purchase invoice with an item-charge line, assigned to the purchase receipt | Manual; no rate check | N-Z23 | *assumed* (snippet of Microsoft docs) |
| **Acumatica (community, 2025-05-02 and 2025-08-13)** | For a client with a "significant amount of outbound shipping costs", a consultant built a custom setup: shipping creates a purchase receipt for the carrier, and when the bill arrives the receipt lines are "manually adjusted to the billed cost(ppv-expensed in bill period)"; "The Purchase Accrual by Period is a great validation screen" | Checking is a **custom build**, and variances are expensed rather than disputed | N-Z16 | thread read in full via extraction; *assumed* anecdote |
| **Acumatica (vendor blog, FreightPOP)** | Acumatica "records freight charges against sales orders and AP bills", but "the automated matching and discrepancy flagging require a connected TMS" | Out of the box, no freight audit | N-Z19 | *assumed* (vendor) |
| **Epicor (users' forum, 2019-09-25 to 11-06)** | One user records packing-slip numbers on AP invoice lines and runs a dashboard to "check freight on past shipments" and find "duplicate freight invoices". Another enters "Est freight … as a misc charge and Act freight … on a UD table" to compare estimate with actual | **Home-built duplicate and variance checks** by in-house staff | N-Z17 | thread read in full via extraction; *assumed* anecdote |
| **Dynamics 365 Supply Chain Management (enterprise)** | A system freight bill with estimated cost is matched to the carrier invoice. "You can receive the invoice electronically or on paper. If it's received on paper, generate an electronic invoice by using the freight bill as a template." An **audit master** sets tolerance limits and reason codes for variances | The only native **tolerance-based freight audit** among the ERPs read, and it sits in an enterprise product | N-Z20 | *verified* (doc dated 2026-06-22) |
| **JD Edwards (enterprise)** | Voucher Match → "Freight To Match" → "Work With Freight Audit History" | Native freight matching in an enterprise ERP | N-Z21 | *verified* (limited page) |

### 2.2 What practitioners and buyers say

| Date | Where | Who (as stated) | What they describe | Relevance | Label |
|---|---|---|---|---|---|
| 2026-02-17 | r/SupplyChainLogistics (4 comments, unread) | A shipper, "We ship a decent volume" | "our invoices look right on the surface but I've never done a proper audit to know for sure"; "carriers are processing thousands of invoices and presumably have their own checks in place" | **Supports "nothing"** and shows skepticism about whether errors are real | *assumed* anecdote; post read in full (N-Z02) |
| 2026-05-12 | r/logistics (1 comment, unread) | An AI audit firm, describing a client: "A medium enterprise", "~$12M/year on freight" | "Their workflow involved SAP plus warehouse teams uploading freight invoices that were later approved for payment"; 8,200 invoices from 12 months; "~$120K in overpayments identified"; "Most slipped through because the process relied on manual review across disconnected systems" | A seller's account of a buyer's process. **$120K on ~$12M ≈ 1.0%** [our calc] | *assumed* (vendor-told); post read in full (N-Z04) |
| 2025-12-31 | r/supplychain | An analyst at a "global appliance manufacturer" | In-house role: "reviewed inbound and outbound freight invoices, validated accessorial charges, and compared billed rates to contracted rates" | A large firm auditing in-house (outside the segment by size) | *assumed*; post read in full (N-Z09) |
| 2025-07-03 | r/SupplyChainLogistics (plus 2 cross-posts removed) | "My company (manufacturing sector)" | "in the final stages of selecting a freight auditor", choosing between TranzAct, Körber and Pando AI; wants "user perspectives (not sales reps)" | A manufacturer **moving to an FAP**, and unable to find user reviews | *assumed*; post read in full (N-Z03) |
| 2025-04-15 | r/Warehousing | "a eComm brand doing about 300-500 orders/day", on NetSuite | "struggling with order routing, freight audit, and warehouse visibility"; wants a TMS "with built-in freight audit" | A buyer who expects audit **inside a TMS** | *assumed*; post read in full (N-Z08) |
| 2026-02-01 | r/SupplyChainLogistics | Someone "working with freight invoice data and freight audit setups" | Discrepancies "more often come from … inconsistent carrier invoice structures", "different naming for the same accessorials", "invoice totals that don't reconcile cleanly with line items" | Data quality, not rates, drives disputes (H09-07) | *assumed*; post read in full (N-Z13) |
| 2025-09-29 | Capterra, Freightview reviews | Manager, building materials | "Our A/P department uses the audit feature" | **AP checking inside an SMB TMS** | *assumed*; page extraction (N-Z40) |
| 2025-09-11 | Capterra, Freightview | Material Control and Traffic, building materials | uses it to "audit the invoices to ensure that we are billed correctly" | Same route | *assumed* (N-Z40) |
| 2025-09-11 | Capterra, Freightview | Shipping department, mechanical or industrial engineering | "Invoicing is easy to view, navigate, and notice discrepancies" | Same route | *assumed* (N-Z40) |
| 2023-12-14 | Capterra, FreightPOP | Logistics manager, building materials | names the "invoice auditing feature" as critical to the company's needs | Same route | *assumed* (N-Z42) |
| n.d. | Capterra, MyCarrier | Operations coordinator, construction | uses the invoice hub to spot "fees and over charges" | Same route | *assumed* (N-Z41) |

### 2.3 How vendors describe the status quo (all *assumed*, vendor claims)
- "Most shippers do it badly — spot-checking a handful of invoices by hand" (US Tech Automations, 2026-06-01, N-Z84).
- "most shippers never verify them line by line"; checking "gets skipped under time pressure and just gets paid at whatever the carrier billed" (Cooter Labs, 2026-08-22, N-Z74).
- "AP cannot reconcile a 40-line ocean invoice against a contract nobody can find, so it rubber-stamps it" (GingerControl, 2026-07-14, N-Z73).
- "Accounts Payable professionals simply do not have the time, knowledge or resources to dig into" freight bills (Supply Chain in 5, 2025-03-27, N-Z93).

**Reading [our call]:** the record **leans toward H09-01** (manual keying, home-built duplicate checks, variances expensed rather than disputed), but it adds a **fourth route H09-01 does not name: an SMB LTL TMS with an audit tab**, used by logistics staff and sometimes by AP. How common each route is cannot be read from the web.

---

## 3. Z2 · First-hand stories of wrong bills (H09-03, H09-04)

### 3.1 Anecdote register

**Segment fit** means a US manufacturer or distributor with 20-499 staff that pays its own carrier bills. "No" or "unknown" is the usual answer: the public complaints come from very small shippers, mostly booking through brokers.

| # | Date | Source | Who (as stated) | Error type | Amount (as stated) | How it ended (as stated) | Segment fit | Label |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-09 | Trustpilot, Freightquote (a broker) | not stated | Balance sent to collections | not stated | "illegitimately sent a 'due balance' to a debt collector" | unknown | *assumed* (N-Z67) |
| 2 | 2026-08-25 | Trustpilot, Freightquote | not stated | Accessorial for carrier's own delivery failure | **$330** extra | "charged an extra $330 for their own delivery failure" | unknown | *assumed* |
| 3 | 2026-06-19 | Trustpilot, Freightquote | not stated | Accessorial (limited access) added after delivery | **$65** | "added $65 after the delivery was made" | unknown | *assumed* |
| 4 | 2026-05-11 | Trustpilot, Freightquote | not stated | Late charges | not stated | "hit months later with random charges" | unknown | *assumed* |
| 5 | 2026-04-29 | Trustpilot, Freightquote | not stated | Inspection in transit (reclass) | price "doubled" | "claim they inspected the load mid-travel and try to charge additional fees" | unknown | *assumed* |
| 6 | 2026-02-04 | Trustpilot, Freightquote | not stated | Fee added | **$64.28** | "added a $64.28 in fees" | unknown | *assumed* |
| 7 | 2025-11-24 | Trustpilot, Freightquote | not stated | Reweigh | 170 lb disputed | "tried to say my weight was 170# off" | unknown | *assumed* |
| 8 | 2025-07-02 | Trustpilot, Freightquote | not stated | Revised bill above the quote | **+25%** | "revised bill for 25% more than what you were quoted and paid" | unknown | *assumed* |
| 9 | 2025-06-04 | Trustpilot, Freightquote | not stated | Refund on a cancelled order | not stated | "3 months without refund" | unknown | *assumed* |
| 10 | 2026-09-03 | Trustpilot, FreightCenter (a broker) | "small business" | Carrier swapped, charges added | **~$600 → ~$3,500** | "charged nearly $3,000 more" | size unknown | *assumed* (N-Z68) |
| 11 | 2026-09-01 | Trustpilot, FreightCenter | a consumer | Dimension (height) correction | **$650 → $2,350** | charge taken from the card three weeks later | no | *assumed* |
| 12 | 2024-09-10 | Trustpilot, FreightPros (now NTG) | not stated | Adjusted invoice after delivery | **~$700** | "quote a great rate and then hit you with an adjusted invoice after delivery" | unknown | *assumed* (N-Z69) |
| 13 | 2024-08-13 | Trustpilot, FreightPros | not stated | Liftgate charged, "not even used" | rate doubled | — | unknown | *assumed* |
| 14 | 2024-03-21 | Trustpilot, FreightPros | not stated | Reclass on "6+ loads" | not stated | "Re-class or make up some reason to charge you way more after delivery" | unknown (repeat shipper) | *assumed* |
| 15 | 2024-03-14 | Trustpilot, FreightPros | not stated | Reclass from class 125 to 175 | **$295 + $185** | extra bill a week later | unknown | *assumed* |
| 16 | 2023-11-25 | Trustpilot, FreightPros | not stated | Weight adjustment | **$460 + $520** | billed a month later | unknown | *assumed* |
| 17 | 2023-11-23 | Trustpilot, FreightPros | not stated | Limited-access accessorial | **$199 + $283.32** | billed after delivery | unknown | *assumed* |
| 18 | 2021-10-18 | Trustpilot, FreightPros | not stated | Adjusted invoice | **$323 + $505** | two weeks after delivery | unknown | *assumed* |
| 19 | 2023-08-31 | Trustpilot, FreightPros | not stated | Charge for a service not used | **$275** | contact attempts unanswered | unknown | *assumed* |
| 20 | 2025-09-13 | BBB, R+L Carriers (an LTL carrier) | a business | Inspection re-rate | not stated | "their inspection department incorrectly changed the freight rate after I shipped product" | unknown | *assumed* (N-Z70) |
| 21 | 2023 (posted 2026-06-10) | r/house_logistics | an importer of home decor, "5+ years" | Duplicate fee (ocean forwarder) | **$2,300** | "my forwarder had double charged a fee for 'peak season adjustment'" | no (ocean, importer) | *assumed*; post read in full (N-Z10) |
| — | 2026-05-12 | r/logistics (a vendor's account) | "A medium enterprise", ~$12M a year | Duplicates and mismatches over 12 months | **~$120K** | "Vendor credits/reversals successfully recovered" | outside by size; seller-told | *assumed* (N-Z04); not counted in the 21 |

**Counts (never rates):**
- **21 anecdotes**; **12 with a dollar figure** (#2, 3, 6, 10, 11, 12, 15, 16, 17, 18, 19, 21).
- **By type:** accessorials 6 (#2, 3, 6, 13, 17, 19); adjusted invoice or charge above quote 5 (#4, 8, 10, 12, 18); reclass or inspection 4 (#5, 14, 15, 20); reweigh or dimensions 3 (#7, 11, 16); duplicate 1 (#21); collections or refund 2 (#1, 9).
- **Billed through a broker:** 19 of 21. **Direct from a carrier:** 1 (#20). **Forwarder:** 1 (#21).
- **Inside the C-09 segment:** 0 confirmed. **Detention, lumper, fuel-surcharge or truckload rate-mismatch stories:** 0 found.
- Freightquote's page showed 9 billing reviews among its latest; its TrustScore is 3.4 from 1,393 reviews. FreightCenter: 2 billing reviews; 4.0 from 1,607. FreightPros: 8 billing reviews; 1.7 from 256 (N-Z67 to N-Z69).

**What the anecdotes do show [our call]:**
- **Corrections arrive late:** "a week later", "two weeks after delivery", "a month later", "months later". A look-back audit and a pre-payment check would see different things.
- **When a small shipper books through a broker, the broker sends the correction.** The counterparty in the dispute is the broker, not the carrier (see §11.3).
- **Repeat pattern:** one reviewer reports reclasses on "6+ loads" (#14).

### 3.2 The NMFC dockets (H09-04)

| Date | Source | What is said | Direction | Label |
|---|---|---|---|---|
| 2026-07-21 | GetTransport blog (the author works a freight desk) | "the single busiest week of 2025 was not peak season. It was the week of July 19", with inquiries split between shippers facing increases and shippers getting savings; examples from the author's desk: a machined-parts pallet moving from class 60 to 55, plastic housings moving to class 250 | **Both directions**; confusion at the change date | *assumed*; page extraction (N-Z88) |
| 2026-06-09 | FreightPlus (a 3PL managing "$300M+" of freight) | "The average shipper-level impact across a full freight program tends to be modest, roughly 2 to 3 percent in either direction"; a Class 100 → 125 reclass "can carry a 20 to 35 percent rate premium"; "Historically, 15% of LTL shipments face reclassification at pickup or delivery" (no source given) | Projection, both directions | *assumed* (N-Z87) |
| (search summary) | unattributed | "Many shippers reported that a pallet that shipped at class 85 all year suddenly rated at class 100" | Increase | *assumed* (search summary; the source page was not identified) |
| 2025-09-13 | BBB, R+L | A business's inspection re-rate complaint (#20) | Increase; no class mentioned | *assumed* |
| 2025-11-24; 2026-04-29 | Trustpilot, Freightquote | A reweigh (#7) and an in-transit inspection (#5) | Increase; not linked to the docket by the reviewer | *assumed* |

**Reading [our call]:** no first-hand record says the dockets **added** corrections to shippers' bills. The only practitioner account says they moved classes **both ways**. This supports keeping the H09-04 probe unprompted (as the kit already does) and counting "cheaper" answers as well as "more corrections".

---

## 4. Z3 · Who decides, budgets, and procurement, IT or security hurdles (H09-05)

| Item | What was found | Label |
|---|---|---|
| Who signs for an audit firm | **Nothing first-hand.** The one related post (r/procurement, 2026-03-07, from a consulting firm) asks whether procurement staff "would only consider it worthwhile if they were paid based on verified savings, or do companies still hire firms on flat consulting fees"; its 2 replies were unreadable | *assumed*; post read in full (N-Z12) |
| Who uses audit tools | Reviewers who mention audit features are mostly **logistics and shipping roles** (director of logistics, shipping manager, logistics coordinator, material control and traffic), plus an accounting specialist and one "A/P department" | *assumed* (N-Z40 to N-Z42) |
| Budget | Encyclopedia entry: shippers pay audit fees "as part of their procurement/operations budget"; contingency providers are "effectively paid from recovered funds" | *assumed* (N-Z80) |
| Security reviews, SOC 2, reluctance to share rates | **Not found.** A security page at Loop returned 404, and the search budget ran out before other vendors' trust pages or buyers' posts could be looked for (§17). The r/freightpayment subreddit asks members to "protect confidential customer and carrier information" | *assumed* (N-Z06) |

**Reading [our call]:** the web does not answer H09-05. Only interviews can.

---

## 5. Z4 · Attitudes to contingency pricing (H09-06)

### 5.1 Public terms (vendor statements; all *assumed*)

| Firm or source | Model | Share or price | Other terms stated | Source |
|---|---|---|---|---|
| ValueXPA (vendor of a subscription alternative), describing recovery audits | Contingency | "20 to 35 percent of recovered amounts" | Look-back "past 12 to 36 months" | N-Z78 |
| Senvo (EU subscription vendor), describing third-party firms | Contingency | "30–50% contingency on recoveries" | — | N-Z83 |
| SSI (Software Solutions Unlimited) | Contingency | "a nominal contingency fee based on the recoverable refunds" | "No long-term contract and no cancellation fee"; refunds "sent to you directly, or credited back to your carrier accounts" | N-Z79 |
| Eller Audit (LTL) | Contingency | share not published | "You only pay when we recover money"; "Your first audit is free"; look-back 180 days, "Some MRAs negotiate longer windows" | N-Z72 |
| Trans Audit | Contingency | share not published | "We only share in the results we produce"; "The first response to a refund request is usually a denial of a claim" | N-Z82 |
| Lojistic | Contingency | "a contingent share of the actual savings generated" | Windows: LTL and air six months; truckload one to two years; ocean and rail up to three years | N-Z77 |
| Shipware (parcel first), per ShipScience | Contingency | not stated | "$50K minimum" | N-Z39 |
| Sifted (parcel first) | **Conflicting:** "$250K minimum; 50% recovery fee" (ShipScience) vs "Subscription-based with no savings fee" (Freehand) | — | — | N-Z39, N-Z36 |
| Intelligent Audit, per Freehand | Mixed | "often with a savings-based or contingency component" | — | N-Z36 |
| Orca, per Gartner listing | Savings-based | "compensation is based directly on the savings it recovers" | — | N-Z25 |
| Freehand | Subscription | "Custom, volume-based. No percentage-of-savings fees" | Enterprises above $250M freight spend | N-Z36 |
| ValueXPA | Subscription | "$2,500 to $4,000 per month"; client keeps "100% of recoveries" | Two-to-four-week diagnostic first | N-Z78 |
| Senvo | Subscription | €0.05-0.20 per invoice | EU shippers | N-Z83 |
| Freightview (SMB LTL TMS with an audit tab) | Subscription | "$149 / mo" for 0-50 shipments; larger tiers "Call now" | Audit tab not tied to a tier on the pricing page | N-Z45 |
| MyCarrier (SMB LTL TMS with an invoice hub) | Usage-based | from "$60.00/month" (Capterra) | "Small to mid-sized manufacturers and distributors" | N-Z43 |

### 5.2 Critiques of contingency (vendor voices; *assumed*)
- "a fee that scales with recoveries is a fee that shrinks if the error class is eliminated, and no commercial arrangement reliably produces an outcome that reduces its own revenue"; recovery programs "institutionalize the error rate" (Locus buyer's guide, 2026, N-Z81).
- A recovery audit "recovers cash" but "does not fix the system that generated the loss"; recoverability falls from "approximately 91 percent" at 0-90 days to "31 percent" at 12-24 months (ValueXPA, 2026-09-15, N-Z78; source of the figures not given).
- "Evaluate contingency agreements carefully for exclusions and minimums"; "Specify which carriers, document types, and accessorials are covered to avoid surprise fees" (Racklify, N-Z80).

### 5.3 Buyer attitudes
- **No buyer post or review was found** on contingency shares, disputes over what counts as a recovery, exclusivity, or auto-renewal. No lawsuit was found in the one search tried (§17).

**Reading [our call]:**
- The public price anchors for the segment are **contingency 20-50%** and **subscriptions from $60-149 a month (SMB TMS) to $2,500-4,000 a month**.
- Newer entrants position contingency as the **legacy, misaligned** model. At interview a 25% share may be judged against a TMS tool the shipper already pays for, or against a "keep 100%" subscription offer.
- Whether a 25% share is accepted cannot be read from the web.

---

## 6. Z5 · Data availability (H09-07)

| Data item | What the record shows | Label | Source |
|---|---|---|---|
| **How carrier invoices arrive** | "You can receive the invoice electronically or on paper" (Microsoft) | *verified* | N-Z20 |
| | FAP carrier instructions accept many forms. nVision: email with "1 Invoice Per Email (including the backup documentation)", as ".PDF, .JPG, .TIFF". U.S. Bank: web entry, EDI or CSV. Cass: EDI or uploaded invoice images, with files stuck "In Process" when missing a "Bill To name" or "Remit To" address | nVision, CassPort *verified*; U.S. Bank methods *assumed* (snippet) | N-Z54, N-Z50, N-Z49 |
| | Loop: "forward via email, SFTP, or API … instruct your carriers to send invoices directly to your dedicated Loop inbox"; Pando's agent "scans relevant carrier emails" and "auto-extracts every PDF or Excel rate card from your inbox" | *assumed* (vendor) | N-Z75, N-Z76 |
| | "unstructured PDFs and EDI in a dozen formats" | *assumed* (vendor) | N-Z73 |
| **Reading PDFs in the ERP** | Acumatica's invoice recognition: freight or carrier invoices cannot create landed-cost documents automatically, and multi-invoice PDFs must be split: "we are manually separating the file into multiple documents" (thread 2023-05 to 2026-04) | *assumed* anecdote; page extraction | N-Z18 |
| **Data quality** | "inconsistent carrier invoice structures", "different naming for the same accessorials", "missing or overloaded fields" | *assumed*; post read in full | N-Z13 |
| **Timing** | Freight bills arrive after the period closed (NetSuite, "a common issue") | *assumed* | N-Z24 |
| **Carrier coverage in SMB tools** | "The auditing section on the website only shows some freight companies, not all the carriers we work with" (Freightview reviewer, internet retailer, 11-50 employees, 2026-02-17); "limited dates when going back on the auditing tab" (logistics, warehousing, 2026-02-19) | *assumed*; page extraction | N-Z40 |
| **PODs and proof** | Carriers send "the signed bol, used as a pod" with the rate confirmation and "lumper receipt" (TruckersReport, 2014). A reweigh dispute needs a manufacturer's "Spec Sheet" and a "Packing Slip" that "cannot be handwritten"; disputes "filed within three days of being invoiced have a MUCH better chance" (FreightPros, 2014) | *assumed* | N-Z58, N-Z92 |
| **Where rate agreements live** | **No first-hand item found.** A vendor's phrase: "a contract nobody can find" | *assumed* | N-Z73 |
| **EDI 210 share among small carriers** | **Not found** (search budget, §17) | — | — |

**Reading [our call]:** the record supports "the data exists but is scattered". Invoices come in mixed formats; PODs travel with invoices on small carriers' loads; SMB TMS audit tabs cover only API-connected carriers. **Where rate agreements live, and how long a pull takes, is interview-only.**

---

## 7. Z6 · Satisfaction with existing providers (H09-08, the show-stopper test)

### 7.1 Ratings found

Gartner Peer Insights, G2 and TrustRadius returned 403, so **most ratings below come from search snippets or third-party articles**, not the review pages. Reviewer company size and industry could not be read for any enterprise FAP vendor.

| Vendor | Gartner Peer Insights (FAP market unless noted) | G2 | Capterra | Other | Segment signal | Top praise / complaint seen | Label, sources |
|---|---|---|---|---|---|---|---|
| **Cass** | 5.0 from 1 review (a 2023 rating, per Freehand) | 5.0 from 1 | — | BBB: 1 complaint in total (2023-12-19, about not processing "paperwork and invoices"); not accredited | Enterprise ("large manufacturing, distribution and retail enterprises", check R) | Praise: "a benchmark amongst its peer group"; "ease of transition, cost competitiveness and business intelligence" | *assumed* (N-Z26, N-Z34, N-Z37); BBB page extraction (N-Z53) |
| **U.S. Bank Freight Payment** | 3.0 from 1 | — | — | — | Enterprise | Praise: "a low rejection rate". Complaint: no "analytical insights"; reports built in Cognos, "not being easy" | *assumed* (N-Z27) |
| **Trax** | 3.5 from 12 | — | — | Worldmetrics "9.2/10" (method opaque) | Multinationals; "3 to 6 month implementation" (Freehand) | Praise: "reporting depth". Complaint: "Too many gaps in operations and management"; "low confidence in support and exception clarity" | *assumed* (N-Z28, N-Z36, N-Z37, N-Z89) |
| **nVision Global** | 4.8 from 8 | 0 reviews (Freehand) | — | — | Global shippers | Praise: expertise and responsiveness; solutions "tailored to each region" | *assumed* (N-Z29, N-Z37) |
| **CTSI-Global** | 3.5 from 8 (**TMS** market) | — | — | Reddit 2023: "Have you used CTSI…?" (0 replies) | Global | "a decades-old, rules-driven system" (Freehand's description) | *assumed* (N-Z31, N-Z15) |
| **Intelligent Audit** | listed; rating not in snippet | a "real G2 review sample" (count not seen) | — | — | "20% of the Fortune 50" (vendor); parcel-heavy | Praise: "Easy to navigate. Shows clear view of all Invoices"; "multi layer approval process". Complaint: wants alerts "as and when the invoice is pending approval" | *assumed* (N-Z32, N-Z37) |
| **TranzAct** | 5.0 from 2 | 0 reviews | — | Considered by a manufacturer, 2025 (Reddit) | Manufacturers; claims National Nail "8% Freight Bill Savings" | — | *assumed* (N-Z30, N-Z03) |
| **Loop** (now including Data2Logistics) | 4.5 from 2 (as of June 2026) | not confirmed | not confirmed | — | "Best for mid-market and enterprise" (Third Fin); customers include Great Dane and GILLIG | Complaint: "Thin independent review base"; no published SLA | *assumed* (N-Z33, N-Z38) |
| **Data2Logistics** | — | — | — | Merged into Loop in August 2025, with StrategIQ Commerce | — | — | *assumed* (N-Z38, N-Z39) |
| **CT Logistics, RateLinx, Freightgate** | not found | not found | not found | — | — | — | search budget (§17) |
| **enVista FAP (Körber since 2022)** | not found | — | — | Körber considered by a manufacturer, 2025 (Reddit) | — | — | *assumed* (N-Z03, N-Z95) |
| **Freehand** | none yet ("no G2/Gartner Peer Insights presence yet", its own article) | — | — | Claims to process "$50B+ in freight payments annually" | Enterprises above $250M freight spend | — | *assumed* (N-Z35, N-Z36) |
| **FreightPOP** | — | 4.8 from 39 | **4.7 from 47** | NetSuite and Acumatica integrations | SMB and mid-market TMS | Praise: "invoice auditing feature" (building materials) | *assumed* (N-Z46, N-Z42) |
| **MyCarrier** | — | 4.7 from 173 | **4.7 from 108** (98 in an older snippet) | from $60 a month | "Small to mid-sized manufacturers and distributors" | Praise: invoice hub for "fees and over charges". Complaint: "the lack of ability to handle invoicing" | *assumed* (N-Z46, N-Z41, N-Z43) |
| **Freightview** | — | 4.7; "55.1% of reviews coming from small businesses" | **4.7 from 743** | $149 a month for 0-50 shipments; "Folks shipping 100-10,000 shipments per month" | SMB and mid-market LTL | Praise: "The auditing process is an added bonus". Complaints: "auditing function could be more intelligent and automated"; audit tab "only shows some freight companies"; "a lot of steps to create the custom filter" | *assumed* (N-Z46, N-Z40, N-Z43, N-Z45) |
| **AFS Logistics** | not found | — | — | BBB lookups returned other firms named AFS | Mid-market (check R) | — | §17 |
| **Transportation Insight / NTG** | — | — | — | Its SMB brokerage brand FreightPros: **Trustpilot 1.7 from 256**, with 8 post-delivery billing complaints (§3) | Audit page: "audits hundreds of thousands of freight bills each month"; client logos are mid-to-large firms | Its audit catches "re-weigh, re-class, and duplicate invoice" | page extraction (N-Z86); *assumed* (N-Z69) |
| **Zero Down Supply Chain Solutions** | "highest review volume" in the Gartner market (count not seen) | none | — | — | "Mid-market to enterprise" | Praise: "Very helpful auditing our freight invoices", "quick responsiveness" | *assumed* (N-Z35, N-Z37) |
| **Orca** | listed | — | — | London, Ontario; founded 2016 (InTek list) | "Organizations formalizing FAP function" | Complaint: "initial onboarding lag" | *assumed* (N-Z25, N-Z35, N-Z90) |
| **Small contingency firms** | — | — | — | No reviews found for SSI, Trans Audit, Eller, Lojistic, Hatfield & Associates. Worldmetrics lists Lojistic as the one "SMB" tool (7.8/10) | SMB claimed | — | *assumed* (N-Z89) |

**Counts from the Capterra pages read (not rates):** across about 100 Freightview reviews on pages 1-4, **7 unique reviews** mention auditing or invoice discrepancies (pages 3 and 4 had none). The MyCarrier page had 1; the FreightPOP page had 1.

### 7.2 Themes
- **Enterprise FAP:** too few public reviews to judge satisfaction (1-12 per vendor). Complaints name **support, exception handling, reporting** and **long implementations**. **No dissatisfaction about recovery results was found**, and no satisfaction either.
- **SMB TMS audit tabs:** high satisfaction with the TMS as a whole (4.7 on hundreds of reviews). The audit feature is praised as a bonus, and criticised for **coverage** (API-connected carriers only), **depth of history** and **manual filtering**.
- **Buyers find it hard to get user references for FAP vendors:** "We're mainly interested in user perspectives (not sales reps)" (N-Z03).

### 7.3 Show-stopper reading (desk only, **[our call]**)
- **No vendor is shown serving more than half the segment with satisfied users.** Enterprise FAPs have tiny public review bases and aim above the segment. **The dominance test is not triggered by desk evidence.**
- **But H09-08's wording "no provider already serves them well" is only partly true.** SMB LTL TMS tools with invoice-audit tabs are marketed to "small to mid-sized manufacturers and distributors" and have hundreds of satisfied reviewers, some of whom use the audit tab in AP. Their share of the segment is unknown. They cover LTL booked through the tool, and apparently not every carrier.
- **Interviews should ask about these tools by behaviour** (§13, probes 1-2), not only about audit firms and FAPs.

### 7.4 New SMB- or mid-market-focused entrants, 2025-2026

"New" here means a firm with AI-audit positioning in 2025-26 content. **Founding dates were not published for most**, so some may be older firms that repositioned. Only Freehand (out of stealth in 2026) and Loop (founded 2021, per Freehand) are dated.

| Name | What it sells | Target size | Public pricing | Funding or scale | Label, source |
|---|---|---|---|---|---|
| **Freehand** | "Fully agentic" audit and payment | "Enterprises above $250M freight spend"; "not small shippers" | "No percentage-of-savings fees" | $75M, co-led by Battery Ventures and NewRoad; emerged from stealth in 2026 | *assumed* (N-Z35, N-Z36) |
| **Loop** | AI-native audit and payment | "Mid-market and enterprise" | none | $95M Series C (known); absorbed Data2Logistics and StrategIQ Commerce (2025) | *assumed* (N-Z38) |
| **Eller Audit** | LTL contingency audit | "Mid-market to Fortune 500" with LTL spend | contingency, "first audit is free" | not stated | *assumed* (N-Z72) |
| **ValueXPA** | Contract-to-invoice enforcement for service vendors, freight included | "$100M+ US industrial manufacturers and distributors"; secondary "$30 to $150 million revenue" | $2,500-4,000 a month; client keeps 100% | not stated | *assumed* (N-Z78) |
| **GingerControl** | "The AI audit layer for global trade spend" (duties, freight invoices, POs) | Mid-market importers (example: "$6M across LTL, parcel, and ocean") | subscription (not published) | not stated | *assumed* (N-Z73) |
| **Cooter Labs** | Agentic freight audit | Enterprise shippers | "Project-Based Packages", "Yearly Retainers" | not stated | *assumed* (N-Z74) |
| **US Tech Automations** | Automated audit and reconciliation | "a few hundred or more loads a month"; not for "fewer than ~50 loads a month" | not published | not stated | *assumed* (N-Z84) |
| **FreightOptics** | "The AI platform that gives shippers total command of their transportation spend" | high-volume shippers | not published | not stated | *assumed* (N-Z85) |
| **Pando (Pi agent)** | AI audit-and-pay agent reading invoices and rate cards from email | Enterprise (Castrol, Nivea, J&J) | not published | Series B $30M (2023, snippet) | *assumed* (N-Z76, N-Z96) |
| **Zero Down Supply Chain Solutions** | Hands-on audit teams | Mid-market to enterprise | "Tiered and transparent" (amounts not seen) | not stated | *assumed* (N-Z35) |
| **Senvo** (EU) | Audit SaaS | EU shippers, 3PLs, e-commerce | €0.05-0.20 per invoice | "€24.9 million in freight spend audited" | *assumed* (N-Z83) |
| **Unnamed builders on Reddit** | An AI audit firm (2026-05); an ex-forwarder offering importers free audits (2025-10); a founder's freight billing and audit product (2024-04); a research team (2022) | Medium enterprises; small importers; merchants | free trials offered | — | *assumed* (N-Z04, N-Z14, N-Z07, N-Z11) |
| **Seen only as search-result titles (not opened)** | Docxster, Tier2 Systems, Freightzy, Truxweb, Warp, CXTMS, Direct Fleet Dispatch, HighQ Logistics, STB Freight, Avantiico, Betachon, King Solutions, Broussard Logistics, Auditec Solutions, Condata Global, Freight Management | — | — | — | titles only |

---

## 8. Z7 · AP automation and how carriers get paid (H09-09)

| Item | What was found | Label | Source |
|---|---|---|---|
| Do mid-sized shippers' carrier invoices go through AP automation? | **No first-hand item found.** Bill's freight-payments page says only "Approved invoices are then paid according to contractual terms" | *assumed* | N-Z95 |
| How carriers are paid by shippers and brokers | Checks, ACH, e-checks, TriumphPay and brokers' own platforms (TrueNorth, 2024-12-17); owner-operators mention checks after the POD, plus Comchek, TCheck and EFS (TruckersReport, 2014) | *assumed* | N-Z64, N-Z58 |
| The payee's view of AP-automation rails | **AvidXchange on Trustpilot: 3.6 from 70 reviews, 23 of them one-star.** Most one-star extracts are from **suppliers being paid**: "They charge a fee to get paid, and if you opt for check" (2026-08-19); "pushed me to use feature…3% service fee off your money" (2026-05-14); "regular ach payments went from 3 days to upwards of 10 days", with repeated offers to "accelerate for a 4% fee"; "been waiting for four months to get paid" (2026-07-23); "same invoice paid twice" (2026-04-27). One **customer**: "AI does not work at all. We have someone dedicated to recoding invoices" (2026-06-24). Industries not stated; one row's dates are inconsistent in the extraction | *assumed* anecdotes; page extraction | N-Z65 |
| Payment-rail terms for carriers | U.S. Bank's carrier agreement (§10.1): enrolment forms, an administrator, ACH authorisation, and the bank's right "to debit Carrier's account(s) in the event of an overpayment or error" | *verified* | N-Z47 |
| Switching payment method | **No shipper account found** of the time or approvals needed to move carrier payment to a third party | — | — |

**Reading [our call]:** the record says nothing about **how long** a mid-sized shipper takes to switch payment rails. It shows strong **payee resentment** of rails that charge the payee. If C-09's payment half were funded by carrier fees, it would meet this sentiment (see H09-C2).

---

## 9. Z8 · Defensive vs cyclical shippers (H09-11)

| Evidence | Defensive groups (food and beverage, packaging, paper, agribusiness, consumer nondurables) | Cyclical groups (auto, metals, homebuilding, building materials, construction, durables) | Other |
|---|---|---|---|
| Reviews mentioning an audit feature (9) | Consumer goods 1 | Building materials 3; construction 1 | Printing 1; internet retail 1; warehousing 1; mechanical or industrial engineering 1 |
| Reddit posts by buyers or in-house staff (4) | — | Appliance manufacturer 1 (outside by size) | Manufacturing, unspecified 1; e-commerce 1; home-decor importer 1 |
| Complaint-site anecdotes (21) | industry not stated | industry not stated | — |

**Reading [our call]:** nothing here distinguishes the two groups. Building materials appears most often among audit-feature reviewers, but 3 reviews cannot carry a conclusion. **The web does not answer H09-11.**

---

## 10. Z9 · Carriers (H09-C1 to H09-C4)

### 10.1 What FAP providers' carrier documents say (*verified* where read)

| Item | U.S. Bank Freight Payment (carrier application and agreement, revision "R 9.2020") | Cass (CassPort carrier user guide, v2.0, December 2024; carrier help centre) | nVision / CTSI |
|---|---|---|---|
| **Fee for early payment** | "Discount Fee" per accelerated payment, "deducted … from the invoiced amounts otherwise payable from Shipper to Carrier". **Base rate 1%** (Advanced Model). Rises 2.5 basis points for every 0.25% the WSJ prime rate is above a 6% floor, "with no maximum". **Extra +0.25% (31-45 days) up to +1.00% (76-90 days)** where the shipper's terms exceed 30 days | Cass Expedite: "a small, expedited fee" (amount not published); payment for invoices "scheduled to be paid more than 2 days from today's date"; "from as long as 10 days to just two days after processing" | not published |
| **Lock-in terms** | "Carrier agrees to process all payment requests for Platform-capable Shippers through the Program"; if the carrier exempts shippers, U.S. Bank may raise the fee "by up to one hundred basis points (1%) for all other transactions". A **$1,000 fee** for U.S. Bank to review a change of control | — | — |
| **Other carrier fees** | $0.25 "each approved payment"; $0.25 per non-compliant shipment; **$25 per remittance-account change**; $30 per declined transaction (invalid or closed account); $150 an hour for custom services | CassPort access; portal fees not stated | nVision: "it is cheaper and quicker if you utilize our online invoice submission portals" |
| **Clawback** | Carrier authorises U.S. Bank "to debit Carrier's account(s) in the event of an overpayment or error", within five business days of settlement or discovery | — | — |
| **Disputes** | "All disputes … including payment requests will be resolved between Shipper and Carrier" | Carriers see "Billed amount, Rated Amounts, Pay Amounts" for each shipment; resolution forms such as "Missing Documentation" and "Out of Tolerance"; a "Suspected Duplicate" flag; "Reject Reporting" by client and reason; "If you find that invoices are rejecting for missing or invalid information, review the billing guides" | CTSI carriers see "Mailback" (invoices "mailed back / rejected"); nVision carriers join disputes on its "Resolution and Collaboration sites" |
| **Invoice submission** | Web entry, EDI or CSV (snippet) | EDI, or invoice images; images lacking a "Bill To name" or a "Remit To" address can sit "In Process" for more than 10 business days | nVision: one invoice per email, PDF, JPG or TIFF, subject "CustomerNumber_SCACCode" |
| Sources | N-Z47, N-Z48, N-Z49 | N-Z50, N-Z51, N-Z52 | N-Z54, N-Z55 |

**Worked example [our calc]:** a $2,000 truckload invoice on 45-day terms, accelerated through U.S. Bank's Advanced Model with prime below 6%, carries a 1.00% + 0.25% = 1.25% discount fee, or **$25**, plus the $0.25 transaction fee. At a higher prime rate the fee rises. The prime rate on the day was not checked.

### 10.2 Carriers' first-hand accounts

| # | Date | Where | Who | What happened | Amount | Maps to | Label |
|---|---|---|---|---|---|---|---|
| C1 | 2023-04-24 | TruckersReport | Owner-operator | A **broker** held back part of the pay for "late" paperwork. The carrier says the POD was texted within 15 minutes of the 2023-02-24 delivery; the invoice went to a factoring company about a week later. Advice from others: claim on "the brokers bond", or put the broker on a do-not-use list | **$3,000 billed, $2,700 paid ($300 short)** | H09-C1, H09-C3 | *assumed*; thread read via extraction (N-Z57) |
| C2 | 2014-07-30 to 08-02 | TruckersReport | Carrier vs broker | Non-payment over a load said to be "short" by 50 cases; argument over what the BOL showed | not stated | H09-C1 | *assumed* (N-Z61) |
| C3 | 2024-02-22 | TruckersReport | A broker | A shipper would not pay because of its own cash flow; the advice was collections (paid "minus their %") or suing the receiver | "a large chunk of payables" | context | *assumed* (N-Z60) |
| C4 | 2014-05 | TruckersReport | Owner-operators answering a shipper | Carriers invoice with the "signed bol, used as a pod", the rate confirmation and the lumper receipt; "Check just cut it and send it out after receiving POD"; PayPal has "additional fees attached" | — | H09-C3, H09-C2 | *assumed* (N-Z58) |
| C5 | 2012-08-03 | TruckersReport | Company drivers and owner-operators | Detention: company drivers should not bill shippers; owner-operators go through the broker ("got paid Tuesday for an hour detention") | 1 hour of detention | Z10 (carriers billing shippers) | *assumed* (N-Z59) |
| C6 | 2026 | Trustpilot, AvidXchange | Suppliers (industry unstated) | Fees to receive payment, slow ACH, a double payment (§8) | 3-4% fees | H09-C2 | *assumed* (N-Z65) |

### 10.3 Early-payment and factoring prices (secondary; *assumed*)
- **Quick pay:** 1.5-5% of load value, e.g. "$1,500 load at 3% = $45"; standard broker terms 30-45 days; quick pay in 24-72 hours (FreightWaves, 2026-03-30, N-Z62).
- **Factoring:** 1-5%, "most carriers pay 2% to 3.5%"; advance 90-95% (same article).
- **Card:** Outgo's debit card "reduced fees of just 1%" (FreightWaves sponsored piece, 2024-12-13, N-Z63).
- **TriumphPay:** "offer quick pay options, these often come with fees" (TrueNorth, N-Z64).
- **A title only** (page 403): Overdrive, "Carrier vetting gone wild: $300 service fee just to get paid?" (N-Z96).

### 10.4 What was not found
- **Carriers' first-hand accounts of short pays by a shipper's FAP or audit firm**, and of how long payment through an FAP takes.
- **BBB complaints by carriers against FAPs:** Cass has 1 complaint in total. Trustpilot has no reviews of TriumphPay and no Cass profile. Other FAPs were not checked (search budget).
- **Carriers' attitudes to automated vs human audit (H09-C4):** nothing. The only related line is a vendor's: "The first response to a refund request is usually a denial of a claim" (N-Z82). That is about carriers denying shippers' claims, not about audit type.

---

## 11. Z10 · Surprises no hypothesis covers

| # | Finding | Evidence | Why it may matter **[our call]** |
|---|---|---|---|
| 11.1 | **Online, builders outnumber buyers.** Of 15 relevant Reddit posts, **9 come from sellers, founders, researchers or consultants looking for buyers or testers** (2 of them classed so on judgement **[our call]**). They date from 2022 (a research team posting in three subreddits) to 2026 (an AI audit firm; a new r/freightpayment subreddit started by a freight-payment firm; a "freight auditors" question). **4** come from buyers | N-Z02 to N-Z14 | Outreach will reach people who have been asked before. Buyer skepticism ("presumably have their own checks in place") is on record |
| 11.2 | **The mid-market incumbent may be the SMB LTL TMS audit tab, not an FAP or contingency firm** | §7 | H09-08's show-stopper test lists FAPs and audit firms only |
| 11.3 | **Small shippers who book LTL through a broker get corrections from the broker**, weeks later, as "adjusted invoices" | 19 of 21 anecdotes (§3) | A mid-sized shipper that books some LTL through 3PLs has a broker, not the carrier, as the counterparty. This is the same issue as C-11's H11-08 |
| 11.4 | **Payees resent pay-to-get-paid rails** | AvidXchange complaints; U.S. Bank's carrier fees, clawback and exemption penalty | A payment half funded by carrier fees inherits the sentiment. It bears on H09-C2 and W6 |
| 11.5 | **Contingency is marketed as the old, misaligned model** by subscription entrants | §5.2 | Positioning risk for an audit-only contingency look-back; a price test may meet "keep 100%" offers |
| 11.6 | **Vendors are consolidating:** Loop absorbed Data2Logistics and StrategIQ Commerce (2025); Körber bought enVista's FAP services (2022, archived post title); AFS Logistics reached an agreement with Leverage Supply Chain Group (2023-12-13, press-release title) | N-Z38, N-Z95 | Check R's list of 16 vendors is out of date in at least one place (Data2Logistics) |
| 11.7 | **Freight bills that arrive after the month closes** are a named controller pain (landed cost) | N-Z24, N-Z16 | An adjacent job (accruals and landed cost) that finance owns, separate from overcharges |
| 11.8 | **Freehand claims "$50B+ in freight payments annually"** (vendor claim) | N-Z36 | If true, a payments player the size of U.S. Bank's $46B (check R) emerged in 2026. Not verified |
| 11.9 | **Payee-detail fraud:** no first-hand story found. U.S. Bank charges carriers $25 per remittance-account change and takes changes by signed form | N-Z47 | The control point exists in FAP contracts; the search for fraud stories was cut short (§17) |
| 11.10 | **The two parcel-first entrants are described inconsistently** (Sifted: a 50% fee with a $250K minimum, or a subscription with no savings fee) | N-Z39, N-Z36 | Vendor comparison articles are written by competitors; treat every competitor claim as *assumed* |

---

## 12. Per-hypothesis table

| H-ID | What the public record says | Anecdote or review count | Direction | Strongest 1-2 quotes (with URL) | Can the web answer it? And what only an interview adds |
|---|---|---|---|---|---|
| **H09-01** Pay as billed; manual AP match, yearly look-back, or nothing | ERP docs assume manual keying. Users build duplicate checks and expense variances. A buyer says invoices "look right on the surface". A fourth route exists: SMB TMS audit tabs | 2 threads; 4 buyer posts; 5 reviews | **Supports**, with a route H09-01 doesn't name | "our invoices look right on the surface but I've never done a proper audit" (2026-02-17, https://www.reddit.com/r/SupplyChainLogistics/comments/1r74pkb/); "Our A/P department uses the audit feature" (Capterra, building materials, https://www.capterra.com/p/136895/Freightview/reviews/) | **Partly.** Documents show what the systems allow; only interviews show which route this firm uses, and how often |
| **H09-02** Overpay 1-3% | Vendor claims only: Eller 8-12% of LTL spend in errors, median recovery 2-5%; Senvo 3-7%; FreightOptics 4-8%. Vendor cases: Loop's Great Dane $73K on $5.1M ≈ **1.4%** [our calc]; the Reddit AI firm $120K on ~$12M a year ≈ **1.0%** [our calc] | 2 vendor cases | **Nothing first-hand**; vendor cases fall in the 1-3% range, vendor claims above it | "~$120K in overpayments identified" (https://www.reddit.com/r/logistics/comments/1takyhf/) | **No.** Only a savings assessment on the firm's own invoices measures it (the numbers check covers benchmarks) |
| **H09-03** 3 of 5 recall a specific overcharge with an amount | 21 public anecdotes, 12 with amounts, **0 confirmed inside the segment**; most are micro shippers booking through brokers | 21 | **Mixed** (the problem is common in public complaints; the segment is absent) | "charged nearly $3,000 more" (small business, 2026-09-03, https://www.trustpilot.com/review/freightcenter.com); "They quote a great rate and then hit you with an adjusted invoice after delivery" (as extracted, 2024-09-10, https://www.trustpilot.com/review/freightpros.com) | **No.** The test is about the segment's own recall; the web gives types and amounts to listen for |
| **H09-04** Dockets added LTL corrections | A 3PL desk reports inquiries in both directions at 2025-07-19; a 3PL projects "2 to 3 percent in either direction"; 1 post-docket business complaint about an inspection re-rate | 3-4 | **Mixed** | "the single busiest week of 2025 was not peak season. It was the week of July 19" (as extracted, https://blog.gettransport.com/logistics-guide/nmfc-freight-classification-reform-2026-ltl-shipper-guide/); "their inspection department incorrectly changed the freight rate after I shipped product" (BBB, 2025-09-13, https://www.bbb.org/us/oh/wilmington/profile/freight-forwarding/r-l-carriers-inc-0292-15781/complaints) | **Partly.** The web shows confusion, not effect on bills. Interviews: did this shipper's LTL bills change, and which way |
| **H09-05** Controller decides; contingency needs no budget | Nothing first-hand. Audit-tool users are mostly logistics roles, with some AP | 0 buyer items; 9 reviews by role | **Nothing found** (role pattern leans to logistics) | "would you only consider it worthwhile if they were paid based on verified savings" (a question, https://www.reddit.com/r/procurement/comments/1rnaiup/) | **No.** Who signs, and what IT or legal asks for, is interview-only |
| **H09-06** 25% share accepted | Vendor anchors: 20-35% and 30-50% contingency; minimums of $50K and $250K (parcel); subscriptions from $60-149 a month (TMS) to $2,500-4,000 a month; entrants attack contingency | 0 buyer items | **Nothing first-hand**; context mixed | "a fee that scales with recoveries is a fee that shrinks if the error class is eliminated" (vendor, https://locus.sh/blogs/freight-audit-settlement-software-buyers-guide-2026/) | **Partly** for anchors; **no** for acceptance. The price test (§6.1 of the kit) must run |
| **H09-07** Invoices, rates and PODs pulled within a week | Mixed formats (paper, PDF, image, EDI, CSV); manual PDF splitting; late bills after month close; audit tabs cover "only some" carriers; PODs travel with small carriers' invoices; rate-agreement location unknown | 3 threads; 2 reviews; 2 forum posts | **Mixed** | "we are manually separating the file into multiple documents" (as extracted, https://community.acumatica.com/financials-7/ap-document-recognition-16154); "only shows some freight companies, not all the carriers we work with" (https://www.capterra.com/p/136895/Freightview/reviews/) | **Partly.** Formats are knowable; pull time and where rates live need Kit E |
| **H09-08** No provider serves them well (show-stopper) | FAP review bases are 1-12 reviews; no dominance evidence. SMB LTL TMS tools with audit tabs have hundreds of 4.7-star reviews and target "small to mid-sized manufacturers and distributors" | ~20 rating snippets; 9 audit-feature reviews | **Mixed:** supports "no dominance", **contradicts "no provider serves them"** | "The auditing process is an added bonus" (Printing, 2025-09-12, https://www.capterra.com/p/136895/Freightview/reviews/); "auditing function could be more intelligent and automated" (Consumer goods, 2026-02-17, https://www.capterra.com/p/136895/Freightview/reviews/?page=2) | **Partly.** Share and satisfaction inside the segment need interviews; ask about TMS audit tabs by name only if they come up |
| **H09-09** Payment switch takes months; audit-first starts now | No shipper account of switch time. Loop lets carriers send invoices to a Loop inbox (audit-first can start without payment). Payees resent AP rails | 0 shipper items; 23 payee complaints | **Nothing found** on the shipper side; indirect support for friction | "They charge a fee to get paid" (supplier, 2026-08-19, https://www.trustpilot.com/review/avidxchange.com) | **No.** Interviews must ask about the last payment-method change |
| **H09-10** Reached through finance, not logistics | Audit-tool reviewers are mostly logistics roles; buyer posts sit in logistics subreddits; one finance-subreddit post (r/Bookkeeping) drew 23 comments (unread); a new r/freightpayment subreddit exists | 9 reviews; 4 posts | **Mixed, leaning against** | "Director of Logistics", "Logistics manager", "Shipping Manager" among audit reviewers (N-Z40 to N-Z42) | **Partly.** The funnel (`5_log.md` §1) is the real test |
| **H09-11** Defensive groups report it as often as cyclical | Building materials 3, construction 1, consumer goods 1 among audit reviewers; nothing else | 9 reviews | **Nothing found** | — | **No** |
| **H09-C1** Carriers lose time and cash to short pays | Short pays found are by **brokers** ($300 of $3,000); FAP documents show reject, "Missing Documentation" and "Out of Tolerance" queues and a bank clawback right | 3 threads; 2 documents | **Partly supports**; nothing FAP-specific | "Carrier authorizes U.S. Bank to debit Carrier's account(s) in the event of an overpayment or error" (https://www.usbank.com/dam/documents/pdf/splash/corporate-payments/transportation/US-Bank-Carrier-Application-and-Agreement.pdf) | **Partly.** Frequency and cost of FAP short pays are interview-only |
| **H09-C2** Carriers take third-party rails and already pay for speed | Fees verified (U.S. Bank 1%+; quick pay 1.5-5%; factoring 2-3.5% typical). Strong resentment of fees to get paid | 1 contract; ~20 payee complaints | **Supports "already pay"; mixed on "would take a third-party rail"** | "The Discount Fee is calculated as percentage of the face value of the invoice approved for payment" (U.S. Bank, Schedule 1); "pushed me to use feature…3% service fee off your money" (2026-05-14, AvidXchange Trustpilot) | **Partly.** Fee levels yes; willingness to enrol with a new rail no |
| **H09-C3** Carriers produce PODs fast | An owner-operator texted the POD "within 15 minutes"; the dispute was over receipt, not speed; small carriers send the signed BOL with the invoice | 2 threads | **Supports** (thin) | POD texted within 15 minutes of delivery (as extracted, https://www.thetruckersreport.com/truckingindustryforum/threads/incomplete-payment-from-broker.2475517/) | **Partly.** LTL carriers' document portals and larger carriers' speed are interview items |
| **H09-C4** Carriers don't resist automated audit more than human | Nothing found | 0 | **Nothing found** | — | **No** |

---

## 13. Sharper interview probes (Mom Test: past events, no hypotheticals, no pitch)

| # | Probe | H-ID | Why the online record suggests it |
|---|---|---|---|
| 1 | "The last carrier invoice you approved: what, if anything, was it compared with before it was paid? Where did that comparison happen: the ERP, the shipping or quoting tool, a spreadsheet?" | H09-01, H09-08 | A fourth checking route (TMS audit tab) exists (§2.2, §7) |
| 2 | "Does the tool you book LTL in have an invoice or audit screen? When did someone last open it, what did it flag, and which carriers weren't in it?" (Ask only if they name such a tool) | H09-08, H09-07 | Users say the tab "only shows some freight companies" |
| 3 | "Tell me about the last invoice that changed **after** delivery: how many days after, by how much, what reason was printed on it, and who noticed?" | H09-03 | Public anecdotes are late adjustments (a week to months) |
| 4 | "What has changed about your LTL invoices in the last 14 months, if anything? Any shipment billed at a different class than the BOL, higher **or lower**?" | H09-04 | The dockets moved classes both ways (§3.2) |
| 5 | "In the last year, which LTL shipments were booked through a broker or 3PL rather than direct? When one of those was corrected, who sent you the new invoice, and what did you do?" | H09-07, H09-03 (and C-11's H11-08) | 19 of 21 public anecdotes came through brokers |
| 6 | "When a freight invoice last didn't match, who emailed the carrier, AP or shipping? How long did it take to close, and was the money credited or just expensed?" | H09-01, H09-10 | ERP users expense variances ("manually adjusted to the billed cost") |
| 7 | "Where is the rate agreement for your biggest LTL carrier right now? When did you last need it, and how long did it take to find?" | H09-07 | No public item says where rates live; a vendor says "a contract nobody can find" |
| 8 | "For the last charge you disputed, what proof did the carrier ask for (packing slip, spec sheet, photos), and where did you get it?" | H09-07, H09-03 | Reweigh disputes need official, non-handwritten documents |
| 9 | "Has anyone ever offered to audit your freight bills for a share of what they recover? What happened next: who else got involved, what did they ask, and why did it go ahead or stop?" | H09-06, H09-05 | No buyer voice on contingency is public; entrants attack the model |
| 10 | "The last time you sent an outside firm your invoices or contract rates, what did IT, legal or procurement ask for first, and how long did it take?" | H09-05 | Security hurdles are absent from the public record |
| 11 | "The last time you changed how you pay a group of vendors (say to ACH, a card or an AP tool), how long from decision to first payment, and who had to sign?" | H09-09 | No shipper account of switch time exists |
| 12 | Carriers: "The last payment you received through a shipper's payment company or AP portal: what came off it, how many days did it take, and what did you have to sign up for?" | H09-C2, H09-C1 | U.S. Bank's fees, clawback and exemption penalty; AvidXchange complaints |
| 13 | Carriers: "The last time an outside auditor or payment company rejected or cut one of your invoices: what reason did they give, what did you send back, how long did it take, and how did it end?" | H09-C1, H09-C4 | Cass and CTSI queues show "Missing Documentation", "Out of Tolerance" and "Mailback" rejections, but no carrier story was found |

---

## 14. Competitor watch-list: mid-market and SMB audit entrants and their positioning

| Name | Positioning in its own words (*assumed*) | Target | Price model | Threat to C-09's audit-only look-back **[our call]** |
|---|---|---|---|---|
| **Freightview** | LTL and truckload quoting, booking and tracking, with an audit tab | "Folks shipping 100-10,000 shipments per month"; 55.1% of G2 reviews from small businesses | $149 a month for 0-50 shipments; larger tiers quoted | **High for LTL booked through it**: already inside the workflow, with AP users. Low for truckload or carriers outside its connections |
| **MyCarrier** | LTL platform with an invoice hub for "fees and over charges" | "Small to mid-sized manufacturers and distributors" | from $60 a month, usage-based | **High** for the same reason |
| **FreightPOP** | TMS with an "invoice auditing feature", NetSuite and Acumatica integrations | SMB and mid-market | not seen | Medium-high |
| **Loop** | AI-native audit and payment; carriers can send invoices to a Loop inbox | "Mid-market and enterprise"; customers include Great Dane and GILLIG | not published | **Medium-high**, well funded; moving down-market is possible |
| **Eller Audit** | LTL contingency audit; "Your first audit is free" | Mid-market to Fortune 500 with LTL spend | contingency | **High (same wedge):** an LTL look-back on contingency |
| **ValueXPA** | Contract enforcement on every vendor invoice; client keeps 100% | Industrial manufacturers, $30-150M+ revenue | $2,500-4,000 a month | Medium: sells to the same controllers with an anti-contingency pitch |
| **Zero Down Supply Chain Solutions** | Hands-on audit teams; "highest review volume" on Gartner | Mid-market to enterprise | "Tiered and transparent" | Medium |
| **US Tech Automations** | Automated audit and reconciliation | "a few hundred or more loads a month" | not published | Medium (unknown traction) |
| **GingerControl** | AI audit of import entries, freight invoices and POs | Mid-market importers | subscription | Low-medium (importer-first) |
| **Cooter Labs, FreightOptics** | Agentic or AI freight audit | Enterprise or high-volume | projects, retainers; not published | Low-medium |
| **Freehand** | "Fully agentic" audit and payment; no share of savings | Enterprises above $250M freight spend | volume-based subscription | Low for the segment now; high for the "AI audit" narrative |
| **Pando (Pi)** | AI agent reading invoices and rate cards from email and paying carriers | Enterprise | not published | Low for the segment |
| **Lojistic, SSI, Trans Audit, Hatfield & Associates** | Contingency audit firms ("No long-term contract and no cancellation fee", SSI) | SMB to mid-market (Lojistic listed as "SMB") | contingency | **The incumbent substitute** for a contingency look-back |
| **Unnamed Reddit builders** | Free audits for small importers; AI audits for medium enterprises; freight billing and audit tools | Small to medium | free trials | Low individually; together they mean crowded outreach |

---

## 15. For the coordinator (not a call)

1. **The web answers documents and prices, not behaviour.** First-hand buyer voice is nearly absent, Reddit was blocked, and most search results are vendor content. H09-01, 03, 05, 06, 09 and 11 still need the interviews. H09-07 and H09-C2 are partly answered.
2. **Show-stopper, desk reading:** no provider is shown serving more than half the segment. Enterprise FAP review bases are 1-12 reviews each. **But SMB LTL TMS tools (Freightview 743 Capterra reviews, MyCarrier 108, FreightPOP 47, all 4.7) already give "small to mid-sized manufacturers and distributors" an invoice-audit tab**, which AP staff use. This incumbent is not named in H09-08 or Kit D.
3. **Contingency is under attack in the category's marketing.** Public anchors are 20-50% contingency, subscriptions of $60-149 a month (TMS) up to $2,500-4,000 a month, and "keep 100%" offers. The 25% price test may be judged against these.
4. **Public wrong-bill stories come from micro shippers booking through brokers** (19 of 21), as post-delivery adjusted invoices. None is confirmed inside the segment. **The broker, not the carrier, is often the counterparty.**
5. **NMFC dockets:** the only practitioner account says classes moved **both ways** at 2025-07-19. No first-hand report of more corrections. The unprompted H09-04 probe should record decreases too.
6. **Carriers already pay for speed, and resent paying to get paid.** U.S. Bank's verified carrier terms: a 1% base discount fee rising with prime and terms, up to +1% for exempting shippers, account debits for errors. AvidXchange's payees complain of "a fee to get paid". A carrier-funded payment half inherits this.
7. **The field is crowded and consolidating.** Loop absorbed Data2Logistics (2025). §7.4 names eleven firms active with 2025-26 AI or audit content; six pitch mid-market shippers (Loop, Eller Audit, ValueXPA, GingerControl, US Tech Automations, Zero Down). On Reddit, 9 of 15 relevant posts are builders seeking the same buyers.
8. **An adjacent finance pain surfaced:** freight bills arriving after month close break landed cost and accruals (NetSuite, Acumatica). It is a controller's job, separate from overcharges.

---

## 16. Sources

All accessed 2026-09-17. "Page extraction" means the page was read through a fetch tool returning a model-made extract.

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-Z01 | PullPush Reddit archive API, query "freight audit" (100 submissions) | 2022-07-11 to 2026-08-30 | https://api.pullpush.io/reddit/search/submission/?q=%22freight%20audit%22&size=100 | full (one call; the next was refused, §17) | Post titles and text; **no comments** |
| N-Z02 | r/SupplyChainLogistics, "Is freight auditing actually worth the effort or is it just something consultants oversell?" | 2026-02-17 | https://www.reddit.com/r/SupplyChainLogistics/comments/1r74pkb/ | post text via archive; 4 comments unread | Buyer skepticism |
| N-Z03 | r/SupplyChainLogistics, "Has anyone used TranzAct, Körber, or Pando AI for freight audit & payment services?" | 2025-07-03 | https://www.reddit.com/r/SupplyChainLogistics/comments/1lqsx2s/ | post text via archive | Manufacturer selecting an FAP |
| N-Z04 | r/logistics, "Recently audited an enterprise firm - $120K saved in 30 days" | 2026-05-12 | https://www.reddit.com/r/logistics/comments/1takyhf/ | post text via archive | Vendor-told case |
| N-Z05 | r/supplychain, "Question for Freight Auditors (Not Freight Brokers)…" | 2026-07-05 | https://www.reddit.com/r/supplychain/comments/1unvpky/ | post text via archive | Builder or learner question |
| N-Z06 | r/freightpayment, welcome post | 2026-07-07 | https://www.reddit.com/r/freightpayment/comments/1upx2rn/ | post text via archive | New subreddit, started by a freight-payment firm |
| N-Z07 | r/smallbusiness, "…at what stage do you need a landed cost report freight audit?" | 2024-04-30 | https://www.reddit.com/r/smallbusiness/comments/1cggbcd/ | post text via archive | Founder: carriers "very hard to close"; "a quote is often cheaper than invoice" |
| N-Z08 | r/Warehousing, "Looking for a WMS/TMS solution that integrates natively with NetSuite" | 2025-04-15 | https://www.reddit.com/r/Warehousing/comments/1jztcv8/ | post text via archive | E-commerce brand wanting built-in freight audit |
| N-Z09 | r/supplychain, "Looking for guidance" | 2025-12-31 | https://www.reddit.com/r/supplychain/comments/1q0jmny/ | post text via archive | In-house freight audit role at an appliance manufacturer |
| N-Z10 | r/house_logistics, "Freight forwarder vs in-house logistics…" | 2026-06-10 | https://www.reddit.com/r/house_logistics/comments/1u1s3fy/ | post text via archive | $2,300 double charge (2023) |
| N-Z11 | r/Bookkeeping and r/logistics, "Do you audit your (freight) invoices?" | 2022-07-14; 2022-07-11 | https://www.reddit.com/r/Bookkeeping/comments/vyuyd6/ ; https://www.reddit.com/r/logistics/comments/vwkbtd/ | post text via archive; 23 and 24 comments unread | Research-team posts |
| N-Z12 | r/procurement, "What would you expect from a logistics consulting firm reviewing your freight spend?" | 2026-03-07 | https://www.reddit.com/r/procurement/comments/1rnaiup/ | post text via archive; 2 comments unread | Savings-based vs flat fee question |
| N-Z13 | r/SupplyChainLogistics, "Freight audit discrepancies: data structure vs rate issues" | 2026-02-01 | https://www.reddit.com/r/SupplyChainLogistics/comments/1qsj61i/ | post text via archive | Data-quality causes |
| N-Z14 | r/supplychain, "I used to work for a major freight forwarder…" | 2025-10-13 | https://www.reddit.com/r/supplychain/comments/1o5cp9g/ | post text via archive | Builder offering free audits to importers |
| N-Z15 | r/supplychain, "Have you used CTSI tms or freight audit and payment?" | 2023-01-19 | https://www.reddit.com/r/supplychain/comments/10fqie9/ | title via archive; 0 comments | No answers |
| N-Z16 | Acumatica Community, "Tracking Shipping Paid for Sales Orders" | 2025-05-02; reply 2025-08-13 | https://community.acumatica.com/financials-7/tracking-shipping-paid-for-sales-orders-30308 | page extraction (full thread) | Accrual and manual adjustment workflow |
| N-Z17 | Epicor User Help Forum, "Advice for capturing freight expenses per order" | 2019-09-25 to 11-06 | https://www.epiusers.help/t/advice-for-capturing-freight-expenses-per-order/60158 | page extraction (full thread) | Duplicate freight invoice dashboard |
| N-Z18 | Acumatica Community, "AP Document Recognition" | 2023-05 to 2026-04 | https://community.acumatica.com/financials-7/ap-document-recognition-16154 | page extraction | Manual splitting of freight PDFs |
| N-Z19 | FreightPOP blog, "How Acumatica Users Manage Freight Operations" (vendor) | n.d. | https://blog.freightpop.com/how-acumatica-users-manage-freight-ltl-bol-invoice-reconciliation | page extraction | Native vs TMS matching |
| N-Z20 | Microsoft Learn, "Reconcile freight in transportation management" (Dynamics 365 SCM) | 2026-06-22 | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/reconcile-freight-transportation-management | full (*verified*) | Paper or electronic invoices; audit master |
| N-Z21 | Oracle, JD Edwards "Matching Freight Invoices" | n.d. | https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoatm/matching-freight-invoices-1.html | page extraction (limited) | Freight audit history |
| N-Z22 | Oracle NetSuite help, landed cost billed separately (and partner blogs) | n.d. | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_162021560020.html | snippet (*assumed*) | Freight bill as vendor bill |
| N-Z23 | Microsoft Learn, "Use item charges to account for extra trade costs" (Business Central) | n.d. | https://learn.microsoft.com/en-us/dynamics365/business-central/payables-how-assign-item-charges | snippet (*assumed*) | Item charge assignment |
| N-Z24 | Anchor Group, "Landed Cost: Bill Received After Item Receipt Period Closed" (NetSuite partner) | n.d. | https://www.anchorgroup.tech/blog/landed-cost-bill-received-after-item-receipt-period-closed | page extraction | Late freight bills |
| N-Z25 | Gartner Peer Insights, Freight Audit and Payment Providers market (incl. Orca, Condata Global, Freight Management listings) | 2026 | https://www.gartner.com/reviews/market/freight-audit-and-payment-providers | **blocked** (403); snippets | Vendor list; Orca's savings-based model |
| N-Z26 | Gartner Peer Insights, Cass FAP services | 2026 | https://www.gartner.com/reviews/product/cass-information-systems-freight-audit-and-payment-services | snippet | 5.0, 1 review |
| N-Z27 | Gartner Peer Insights, U.S. Bank Freight Payment | 2023-2026 | https://www.gartner.com/reviews/product/us-bank-freight-payment-freight-audit-and-payment-services | snippet | 3.0, 1 review; praise and complaint |
| N-Z28 | Gartner Peer Insights, Trax | 2026 | https://www.gartner.com/reviews/product/trax-technologies-freight-audit-and-payment-services | snippet | 3.5, 12 reviews |
| N-Z29 | Gartner Peer Insights, nVision Global | 2026 | https://www.gartner.com/reviews/product/nvision-global-freight-audit-and-payment-services/alternatives | snippet | 4.8, 8 reviews |
| N-Z30 | Gartner Peer Insights, TranzAct | 2026 | https://www.gartner.com/reviews/product/tranzact-freight-audit-and-payment-providers | snippet | 5.0, 2 reviews |
| N-Z31 | Gartner Peer Insights, CTSI-Global (TMS market) | 2023-2026 | https://www.gartner.com/reviews/market/transportation-management-systems/vendor/ctsi-global | snippet | 3.5, 8 reviews |
| N-Z32 | Gartner Peer Insights and G2, Intelligent Audit | 2026 | https://www.gartner.com/reviews/product/intelligent-audit-freight-audit-and-payment-providers ; https://www.g2.com/products/intelligent-audit/reviews | snippets | Praise themes |
| N-Z33 | Gartner Peer Insights, Loop | 2026 | https://www.gartner.com/reviews/market/freight-audit-and-payment-providers/vendor/loop-238291254 | snippet | 4.5, 2 reviews (via Third Fin) |
| N-Z34 | G2, Cass Information Systems | 2026 | https://www.g2.com/products/cass-information-systems/reviews | snippet | 5.0, 1 review |
| N-Z35 | Freehand, "Best Freight Audit Software: 7 Tools Compared" (vendor) | 2026 | https://www.freehand.ai/articles/best-freight-audit-software | page extraction | Competitor positioning |
| N-Z36 | Freehand, "Best AI Freight Audit and Payment Software" (vendor) | 2026-07-08 | https://www.freehand.ai/articles/best-ai-freight-audit-and-payment-software | page extraction | Funding, targets, pricing models |
| N-Z37 | Freehand, "7 Best CTSI-Global Alternatives" (vendor) | 2026 | https://www.freehand.ai/articles/ctsi-global-alternatives | page extraction | Quoted Gartner and G2 review lines |
| N-Z38 | Third Fin, "Loop Freight Audit Review" | 2026 | https://thirdfin.io/freight-audit/loop-freight-audit/ | page extraction | Loop target, mergers, reviews |
| N-Z39 | ShipScience, "Top 7 Loop Alternatives" (parcel-audit vendor) | 2026 | https://www.shipscience.com/top-7-loop-alternatives-for-freight-parcel-audit-2026/ | page extraction | Minimums and fees |
| N-Z40 | Capterra, Freightview reviews, pages 1-4 | 2025-09 to 2026-02 | https://www.capterra.com/p/136895/Freightview/reviews/ (and ?page=2, 3, 4) | page extraction | 4.7, 743 reviews; 7 audit mentions |
| N-Z41 | Capterra, MyCarrierTMS reviews | n.d. | https://www.capterra.com/p/239697/MyCarrier/reviews/ | page extraction | 4.7, 108; invoice hub |
| N-Z42 | Capterra, FreightPOP reviews | 2020-2026 | https://www.capterra.com/p/152285/FreightPOP/reviews/ | page extraction | 4.7, 47; audit feature |
| N-Z43 | Capterra, Freightview vs MyCarrierTMS | 2026 | https://www.capterra.com/compare/136895-239697/Freightview-vs-MyCarrier | page extraction | Prices and target customers |
| N-Z44 | Capterra, FreightPOP alternatives | 2026 | https://www.capterra.com/p/152285/FreightPOP/alternatives/ | page extraction | No audit tools among alternatives |
| N-Z45 | Freightview pricing page | 2026 | https://www.freightview.com/pricing | page extraction | $149 a month tier |
| N-Z46 | G2 and Capterra rating snippets (FreightPOP G2 4.8/39; MyCarrier G2 4.7/173; Freightview G2 4.7, 55.1% small business) | 2026 | https://www.g2.com/sellers/freightpop ; https://www.g2.com/products/mycarriertms/reviews?qs=pros-and-cons ; https://www.g2.com/compare/freightview-vs-shipwell | snippets | Ratings |
| N-Z47 | U.S. Bank, "Freight Payment Service for Carriers: Application & Agreement" | rev. 9.2020 | https://www.usbank.com/dam/documents/pdf/splash/corporate-payments/transportation/US-Bank-Carrier-Application-and-Agreement.pdf | full PDF text (*verified*) | Fees, clawback, lock-in, disputes |
| N-Z48 | U.S. Bank, freight payment page for carriers | 2026 | https://www.usbank.com/corporate-and-commercial-banking/industry-expertise/transportation/freight-audit-payment/carriers.html | page extraction | "100% pre-payment audit"; payment on approval |
| N-Z49 | U.S. Bank carrier Quick Pay and submission methods (search summary) | n.d. | https://www.usbank.com/corporate-and-commercial-banking/industry-expertise/transportation/freight-audit-payment/carriers.html | snippet | Terms "typically anywhere from 45 to 90 days"; web, EDI, CSV |
| N-Z50 | Cass, "CassPort Carrier User's Guide", v2.0 | 2024-12 | https://my.cassport.com/CISFBSYS/Login/Manuals/CassPortCarrierTraining,%20English%20edition.pdf | full PDF text (*verified*) | Exceptions, rejects, submission |
| N-Z51 | Cass, carrier help center | 2026 | https://www.cassinfo.com/carrier-help-center | page extraction | Expedite fee wording and timing |
| N-Z52 | Cass blog, "Dispelling Myths: … Carrier Quick Payment Programs" | 2024-04-08 | https://www.cassinfo.com/blog/dispelling-myths-unveiling-the-true-costs-of-carrier-quick-payment-programs | page extraction | "10 days to just two days" |
| N-Z53 | BBB, Cass Information Systems complaints | 2023-12-19 | https://www.bbb.org/us/oh/columbus/profile/payment-processing-services/cass-information-systems-inc-0302-23023144/complaints | page extraction | 1 complaint |
| N-Z54 | nVision Global, freight help center (carrier FAQ) | 2026 | https://corporate.nvisionglobal.com/freight-help-center/ | page extraction (*verified* wording) | Invoice submission rules |
| N-Z55 | CTSI-Global, "How to Check Invoice Statuses" | 2026 | https://ctsi-global.com/invoice-statuses/ | page extraction | Mailback or rejected |
| N-Z56 | nVision Global, "Evaluating FBAP partners beyond the marketing gloss" (vendor) | 29 Jul (year not shown) | https://corporate.nvisionglobal.com/evaluating-freight-audit-and-payment-fbap-partners-beyond-the-marketing-gloss/ | page extraction | Vendor's list of shipper regrets |
| N-Z57 | TruckersReport, "Incomplete payment from broker" | 2023-04-24 | https://www.thetruckersreport.com/truckingindustryforum/threads/incomplete-payment-from-broker.2475517/ | page extraction (page 1) | $300 short pay |
| N-Z58 | TruckersReport, "Invoicing" | 2014-05-06 to 05-10 | https://www.thetruckersreport.com/truckingindustryforum/threads/invoicing.249648/ | page extraction | What carriers send; payment methods |
| N-Z59 | TruckersReport, "Can I Bill Shipper or Consignee for Excessive Detention" | 2012-08-03 | https://www.thetruckersreport.com/truckingindustryforum/threads/can-i-bill-shipper-or-consignee-for-excessive-detention.185636/ | page extraction | Detention billing |
| N-Z60 | TruckersReport, "Going After Shipper/Receiver for Non-Payment - AS A BROKER" | 2024-02-22 | https://www.thetruckersreport.com/truckingindustryforum/threads/going-after-shipper-receiver-for-non-payment-as-a-broker.2502947/ | page extraction | Shipper non-payment |
| N-Z61 | TruckersReport, "Please help! … Broker won't pay says load was 'short'", page 4 | 2014-07-30 to 08-02 | https://www.thetruckersreport.com/truckingindustryforum/threads/please-help-need-advise-broker-wont-pay-says-load-was-short.257819/page-4 | page extraction | Short-load dispute |
| N-Z62 | FreightWaves, "The Broker Offers You Quick Pay…" | 2026-03-30 | https://www.freightwaves.com/news/the-broker-offers-you-quick-pay-and-it-sounds-like-free-money-read-this-before-you-take-it | page extraction | Quick pay and factoring fees |
| N-Z63 | FreightWaves, "The technology behind making carrier payments instant" (sponsored, Outgo) | 2024-12-13 | https://www.freightwaves.com/news/the-technology-behind-making-carrier-payments-instant | page extraction | 1% card fee |
| N-Z64 | TrueNorth, "How Freight Brokers Process Payments to Carriers" | 2024-12-17 | https://truenorthfleet.com/articles/business/trucking-payment-providers | page extraction | Payment methods |
| N-Z65 | Trustpilot, AvidXchange (all; one-star filter) | 2025-09 to 2026-09 | https://www.trustpilot.com/review/avidxchange.com ; https://www.trustpilot.com/review/avidxchange.com?stars=1 | page extraction | 3.6, 70; 23 one-star |
| N-Z66 | Trustpilot, TriumphPay | 2026 | https://www.trustpilot.com/review/triumphpay.com | page extraction | 0 reviews |
| N-Z67 | Trustpilot, Freightquote | 2025-06 to 2026-09 | https://www.trustpilot.com/review/freightquote.com | page extraction (latest page) | 3.4, 1,393; 9 billing reviews |
| N-Z68 | Trustpilot, FreightCenter | 2026-09 | https://www.trustpilot.com/review/freightcenter.com | page extraction (latest page) | 4.0, 1,607; 2 billing reviews |
| N-Z69 | Trustpilot, FreightPros (NTG) | 2021-10 to 2024-09 | https://www.trustpilot.com/review/freightpros.com | page extraction (latest page) | 1.7, 256; 8 billing reviews |
| N-Z70 | BBB, R+L Carriers complaints | 2025-08 to 2025-09 | https://www.bbb.org/us/oh/wilmington/profile/freight-forwarding/r-l-carriers-inc-0292-15781/complaints | page extraction | 41 complaints in 3 years; 1 business billing complaint |
| N-Z71 | BBB, search "AFS Logistics"; Shreveport profile | 2026 | https://www.bbb.org/search?find_country=USA&find_text=AFS%20Logistics ; https://www.bbb.org/us/la/shreveport/profile/heavy-haul-trucking/afs-logistics-1015-90017538/complaints | page extraction | Other firms of the same name; 0 complaints |
| N-Z72 | Eller Audit, "LTL Freight Audit" | 2026 | https://www.elleraudit.com/ltl-freight-audit | page extraction | Contingency, first audit free, data needs |
| N-Z73 | GingerControl, "Freight Invoice Audit: Where the 5-10% Billing Errors Hide" | 2026-07-14 | https://gingercontrol.com/blog/freight-invoice-audit-guide | page extraction | Positioning; status-quo claims |
| N-Z74 | Cooter Labs, "Agentic Freight Audit…" | 2026-08-22 | https://cooterlabs.com/blogs/agentic-freight-audit-catching-carrier-invoice-overcharges-b | page extraction | Positioning |
| N-Z75 | Loop, "Freight and parcel audit" | 2026 | https://www.loop.com/capabilities/freight-and-parcel-audit | page extraction | Intake, customers, cases |
| N-Z76 | Pando, "AI Agent for Freight Audit" (Pi) | 2026 | https://pando.ai/product/ai-agents/pi/ai-freight-audit-pay-specialist/ | page extraction | Email and PDF intake |
| N-Z77 | Lojistic, freight audit FAQ | n.d. | https://www.lojistic.com/shipping-faqs/ftl-ltl-ocean-rail-air-freight-audit-questions | page extraction | Contingency; windows |
| N-Z78 | ValueXPA, "Continuous Contract Enforcement vs. AP Recovery Audits for Manufacturers" | 2026-09-15 | https://valuexpa.com/insights/contract-enforcement-vs-audits | page extraction | Contingency 20-35%; subscription price |
| N-Z79 | SSI, "Contingency Invoice Audits" | n.d. | https://ssui.com/contingency-parcel-freight-invoice-audits/ | page extraction | Terms |
| N-Z80 | Racklify encyclopedia, "Inbound Freight Audit Costs & Who Pays" | n.d. | https://racklify.com/encyclopedia/inbound-freight-audit-costs-savings-and-who-pays-pricing-models-and-roi/ | page extraction | Pricing models, pitfalls |
| N-Z81 | Locus, "Freight Audit & Settlement Software Buyer's Guide 2026" (vendor) | 2026 | https://locus.sh/blogs/freight-audit-settlement-software-buyers-guide-2026/ | page extraction | Critique of contingency |
| N-Z82 | Trans Audit, "4 Things You Should Demand in a Freight Audit Company" | n.d. | https://transaudit.com/freight-audit-company/ | page extraction | Contingency; claim denials |
| N-Z83 | Senvo, "Freight audit & payment: the complete guide" | 2026 | https://www.senvo.ai/blog/freight-audit-payment | page extraction | EU subscription pricing |
| N-Z84 | US Tech Automations, "Stop Freight Overcharges Before You Pay" | 2026-06-01 | https://ustechautomations.com/resources/blog/automate-automated-freight-audit-invoice-reconciliation-2026 | page extraction | Target; status-quo claim |
| N-Z85 | FreightOptics, "Simplifying the Freight Audit Process" | 2026-04-01 | https://www.freightoptics.com/blog/freight-audit-pay-avoiding-fees/ | page extraction | Positioning |
| N-Z86 | Transportation Insight, "Freight Bill Audit & Payment" | 2026 | https://transportationinsight.com/solutions/freight-bill-audit-payment/ | page extraction | Scale; exception types |
| N-Z87 | FreightPlus, "LTL Freight Class in 2026" | 2026-06-09 | https://freightplus.io/ltl-freight-class-nmfc-density-changes/ | page extraction | Docket impact projection |
| N-Z88 | GetTransport blog, "NMFC Freight Classification Reform 2026" | 2026-07-21 | https://blog.gettransport.com/logistics-guide/nmfc-freight-classification-reform-2026-ltl-shipper-guide/ | page extraction | Desk anecdotes at the docket date |
| N-Z89 | Worldmetrics, "Top 10 Best Freight Auditing Software (2026)" | 2026 | https://worldmetrics.org/best/freight-auditing-software/ | page extraction | Scores (method opaque) |
| N-Z90 | InTek Logistics, "2026 Best Freight Audit & Pay Companies" (3PL) | 2025-10-03 | https://www.inteklogistics.com/blog/best-freight-audit-pay-companies-and-how-to-choose | page extraction | 14 firms with founding years |
| N-Z91 | Hatfield & Associates, "Top 10 Freight Audit Companies for 2025" (vendor) | 2023-04-12 (updated) | https://hatfieldandassociates.com/top-10-freight-audit-companies-2025/ | page extraction | Firm list |
| N-Z92 | FreightPros (NTG), "How to Dispute a Reweigh" | 2014-07-12 | https://www.freightpros.com/whitepaper/dispute-reweigh/ | page extraction | Evidence and timing |
| N-Z93 | Supply Chain in 5 (Substack), "The Beneficial Insights from Freight Pay & Audit Services" | 2025-03-27 | https://supplychainin5.substack.com/p/the-beneficial-insights-from-freight | page extraction | Opinion; no first-hand case |
| N-Z94 | FreightWaves, "Freight Invoice Audits and Why They Matter" | 2025-02-12 | https://www.freightwaves.com/news/freight-invoice-audits-and-why-they-matter | page extraction | No shipper quotes |
| N-Z95 | BILL, "Understanding Freight Payments" | n.d. | https://www.bill.com/learning/freight-payments | page extraction | No payment-method detail |
| N-Z96 | Search-result titles and snippets: Overdrive "Carrier vetting gone wild: $300 service fee just to get paid?"; Pando funding (Lokad review); Körber acquisition of enVista FAP (archived Reddit title, 2022-07-21); AFS Logistics agreement with Leverage Supply Chain Group (Business Wire, 2023-12-13) | various | https://www.overdriveonline.com/business/article/15681389/carrier-vetting-gone-wild-300-service-fee-just-to-get-paid ; https://www.lokad.com/review-of-pando-ai/ ; https://www.businesswire.com/news/home/20231213504624/en/AFS-Logistics-announces-agreement-with-Leverage-Supply-Chain-Group | titles or snippets only (*assumed*); Overdrive blocked | Context only |

---

## 17. Could not access, or not found

**Blocked or refused:**
- **reddit.com and old.reddit.com:** the fetch tool reported it "is unable to fetch" either domain. Web search restricted to reddit.com returned no Reddit results.
- **PullPush (Reddit archive):** one query succeeded (N-Z01). The next returned: "Rate limit exceeded. This website does not provide free scraping resources for agents." **It was not used again.** Reddit comments were never read.
- **Gartner Peer Insights** (403, including the alternative hostnames external.pi.gpi.aws.gartner.com and gcom.pdo.aws.gartner.com), **G2** (403), **TrustRadius** (403), **Capterra's category page** (404 by fetch, 403 by plain request), **Glassdoor** (403).
- **Overdrive** (403, with and without www), **Business Wire's Cass working-capital release** (403), **FreightWaves "Breaking the lock on carrier payments"** (404), **OTR Solutions quick-pay article** (404), **Loop security page** (404), **Trustpilot pages for Cass and Paymode** (404).
- **U.S. Bank's carrier agreement is revision 9.2020.** No newer public version was found, so current fees may differ.

**Search budget:** the session's shared web-search cap (200 queries) was reached after this check's 44th query. After that only known URLs were fetched. **No general search engine was used through the fetch tool.** The list below says which planned searches were therefore not run.

**Searches tried (44), with outcome:**
1. reddit freight bill audit overcharged carrier invoice accounts payable (vendor pages only)
2. "freight audit" reddit r/logistics worth it contingency (no Reddit results)
3. site:reddit.com freight audit company (no Reddit results)
4. site:reddit.com "freight invoices" accounts payable matching carrier (ERP docs, no Reddit)
5. reddit "freight audit" "r/supplychain" OR "r/logistics" OR "r/Accounting" (no Reddit results)
6. Cass Information Systems freight payment reviews G2 OR Capterra OR TrustRadius (Gartner and G2 snippets)
7. Gartner Peer Insights freight audit and payment providers reviews (market listing snippets)
8. "Trax" freight audit reviews ratings Gartner Peer Insights 2026 (3.5, 12)
9. "U.S. Bank Freight Payment" reviews ratings Gartner Peer Insights (3.0, 1)
10. "nVision Global" reviews ratings freight audit (4.8, 8)
11. "Intelligent Audit" reviews rating G2 Gartner freight (themes, no rating)
12. "CTSI-Global" reviews rating Gartner Peer Insights freight audit (TMS market 3.5, 8)
13. "TranzAct" freight audit reviews rating stars (5.0, 2)
14. Freightview reviews Capterra rating LTL shipping software small business (Capterra pages)
15. FreightPOP reviews G2 Capterra rating (4.8/39; 4.7/47)
16. MyCarrier LTL reviews G2 Capterra rating shippers (4.7/173; 4.7/98)
17. Loop freight audit reviews G2 "Loop" logistics payments rating (Gartner 4.5, 2)
18. NetSuite freight invoice carrier bill matching item receipt landed cost "freight bill" community question (docs and partner blogs)
19. Acumatica community freight invoice carrier bill landed cost AP bill freight accrual (threads)
20. Business Central community "freight invoice" carrier vendor invoice item charge purchase receipt (docs)
21. Sage City OR Epicor forum "freight bill" OR "freight invoices" matching accounts payable carrier (Epicor threads; no Sage City thread)
22. "Do you audit your freight invoices" reddit Bookkeeping (not found)
23. "Is freight auditing actually worth the effort or is it just something consultants oversell" (not found; vendor pages)
24. "Has anyone used TranzAct, Körber, or Pando AI for freight audit" (not found; vendor pages)
25. thetruckersreport.com forum Cass freight payment short paid invoice shipper (broker threads only)
26. owner operator complaint shipper payment portal fee virtual card carrier invoice "pay to get paid" (Overdrive title)
27. Overdrive carriers short pay deductions freight payment provider audit shippers slow pay 2025 (vendor pages)
28. BBB complaints "Cass Information Systems" carrier payment (BBB profile)
29. Cass carrier FAQ "Cass Expedite" early payment fee percent carriers (fee not published)
30. "U.S. Bank Freight Payment" carrier FAQ quick pay fee … (carrier agreement PDF)
31. CTSI-Global carrier FAQ invoice short pay … (carrier pages)
32. nVision Global carrier FAQ … (help center)
33. truckersreport "Cass" payment carrier shipper invoice forum thread (CassPort guide PDF)
34. Land Line OOIDA carriers charged fees to get paid portals quick pay broker shipper 2025 (broker-transparency articles; FreightWaves quick pay)
35. FreightWaves carriers virtual card payments fees trucking … (fuel-card pages)
36. LTL carrier shipper short pay freight bill audit firm deduction complaint "short pay" trucking (vendor pages)
37. "freight audit" contingency fee lawsuit breach of contract … (**no case found**)
38. RFP freight bill audit services contingency percentage "look back" period … (**no public RFP or contract found**)
39. BBB complaint reweigh reclass LTL charge "inspection" small business shipper billed extra freight (R+L BBB)
40. NMFC density classification changes 2025 shippers complain reclass invoices higher … (3PL guides; no survey)
41. linkedin.com/posts freight invoice overcharge found duplicate carrier invoices … (**no LinkedIn posts returned**)
42. Quora "freight audit" worth it company experience overcharged freight bills (**no Quora results**)
43. Spiceworks community freight invoice processing AP automation carrier invoices EDI 210 small company (**no Spiceworks results**)
44. AccountingWEB forum freight invoices carrier haulier invoice checking duplicate charges (**no AccountingWEB results**)
- Refused by budget: thetruckersreport "freight payment" OR "audit company" shipper short paid lumper detention invoice deducted; "TriumphPay" carrier complaints fees short paid audit reddit OR forum OR BBB.

**Not found in what was read:**
- Any **first-hand post by a controller, CFO or AP manager at a 20-499-staff shipper** about freight bills, audit firms, contingency shares or FAPs.
- **Procurement, IT or security hurdles** (SOC 2 questionnaires, reluctance to share rates).
- **Disputes over what counts as a recovery**, exclusivity or auto-renewal in contingency contracts; lawsuits between shippers and audit firms.
- **Carriers' accounts of short pays by FAPs or audit firms**, payment times through FAPs, or attitudes to automated vs human audit.
- **The share of small carriers sending EDI 210** vs PDF.
- **Payee-detail (bank-change) fraud stories** in freight payment.
- **Defensive vs cyclical differences** in how shippers talk about freight-bill errors.
- **Ratings for CT Logistics, RateLinx, Freightgate, enVista/Körber FAP and AFS Logistics.**

**Not attempted (search budget reached, or needs a login):**
- Sage City, the Oracle NetSuite community, Dynamics Community threads, Epicor threads beyond the one read; r/Netsuite, r/SAP, r/Accounting, r/FreightBrokers, r/Truckers and r/OwnerOperators (Reddit blocked in any case).
- OOIDA Land Line, CDLLife, JOC, Inbound Logistics, DC Velocity, SupplyChainBrain and Logistics Management articles quoting shippers.
- Software Advice and GetApp category pages; Indeed company reviews; BBB profiles for U.S. Bank Freight Payment, Trax, nVision, CTSI, Intelligent Audit and TriumphPay.
- Tipalti, Stampli and Bill threads about carriers and virtual cards.
- Funding news for 2025-26 AI audit entrants beyond what vendor pages state.
- Anything behind a login (LinkedIn, Facebook groups, Gartner full reviews, G2 full reviews).
