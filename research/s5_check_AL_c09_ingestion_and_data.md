# S5 check AL: how the C-09 audit machine gets its documents and data

- **What this is:** desk research for card C-09, after the founders' decision of 2026-10-03 that version 1 is an audit machine only. They wrote that document ingestion "could be manual at first but we would add more value by automatically ingesting these". This check covers AL1-AL6: email ingestion, documents from carriers, the shipper's own systems, reference data for the math, notifications, and security.
- **Builds on:** check AC §2, §3, §6, §9; check T §1 row 5, §3.2, §7; check Z §6; check AA §6; check Y §2.2, §3.4, §3.6. Those are cited by their IDs (N-AC…, N-T…, N-Z…, N-AA…, N-Y…), not redone.
- **Summary for the founders:** `software-initial-pitch.md`.
- **Date:** 2026-10-03.
- **Status:** input to S5. **It decides nothing.** Design suggestions are marked **[our call]**.
- **Method:** about 40 web searches and about 80 page or PDF reads, all read-only.
  - No sign-ups, form submissions or API-key registrations; nobody was contacted, and no identity was sent in any request.
  - A few PDFs were read from the fetch tool's own cache; no files were created.
- **Labels:**
  - *verified*: read at the primary source (official docs, a pricing page, terms, a licence page). For a vendor, it means verified that the vendor says it.
  - *assumed*: a search snippet, a secondary article, a vendor claim reported by others, or memory.
  - **[our calc]**: our arithmetic. **[our call]**: our judgement.
- **Re-checked at the source by the coordinator (2026-10-03), all matching:**
  - **Microsoft 365:** the forwarding default "changed to Off - Forwarding is disabled for new organizations and for existing organizations that weren't actively using" it, in 2021. Blocked mail bounces with "5.7.520 Access denied, Your organization does not allow external forwarding" (N-AL13).
  - **Google:** "Every app that requests access to Google users' restricted data and has the ability to access data from or through a third-party server must go through a security assessment". This is repeated "at least every 12 months", with exemptions for internal-only and personal use (N-AL14).
  - **UCC § 9-406(a):** after notification, the account debtor "may not discharge the obligation by paying the assignor" (N-AL49).

---

## 1. Summary table

| Q | Headline answer | Best evidence | Labels |
|---|---|---|---|
| **AL1** Email ingestion | **Inboxes:** the standard pattern is one dedicated address per customer, which the customer forwards mail to. Examples: Ramp `<company-name>@ap.ramp.com`, Dext `@dext.cc` / `@multiple.dext.cc`, BILL, Stampli, Hubdoc, Loop.<br>**Cost:** the plumbing is cheap. Amazon SES receiving costs $0.10 per 1,000 emails plus $0.09 per 1,000 incoming 256 KB chunks. Postmark includes inbound mail from its $16.50/month Pro plan.<br>**Customer-side friction:** Microsoft 365 has disabled automatic external forwarding by default since 2021 for new tenants and for those not already forwarding. Blocked mail bounces with "5.7.520", so an admin must open forwarding. Gmail needs a confirmation link clicked.<br>**Edge cases needing code:** TIFF images, multi-invoice PDFs, link-only emails.<br>**Direct mailbox access is heavier:** Gmail read scopes are "Restricted" and need a CASA assessment every 12 months ($675-4,500 per app per year at one assessor). Microsoft's app-only Mail.Read needs admin consent, but can be scoped to one AP mailbox.<br>**[our call]:** forwarding first | N-AL03, N-AL04, N-AL08, N-AL09, N-AL13 to N-AL18 | prices and Google/Microsoft rules *verified*; BILL, Stampli, Hubdoc *assumed*; which carriers send link-only emails is **not established** |
| **AL2** Carrier documents | **Carrier APIs:** all 12 LTL carriers checked offer rate-quote and/or document-image services tied to the customer's own login. Seven name weight-and-research (W&R) or inspection documents: ODFL, XPO, Saia, R+L, TForce, ABF, Estes.<br>**No invoice-data API yet:** Estes has an "Invoice Subscription" for notifications; R+L returns invoice *images*; TForce lists "Invoicing" and "Billing Discrepancy" APIs as "Coming Soon".<br>**Terms:** no page read states a fee, rate limit or third-party terms. ODFL's Rating API has a field for a company acting "on behalf of our mutual customer".<br>**Aggregators:** project44 (image retrieval) and SMC3 (CarrierConnect XL documents) publish no prices, and project44 runs on the shipper's own carrier accounts.<br>**EDI 210:** can go to a third party's EDI ID (R+L's setup form has a field for it). A VAN mailbox costs $250/month for 3,000 KC at one vendor; web EDI costs $189 per trading partner per month (Orderful).<br>**Factored TL bills:** after a notice of assignment, paying the carrier does not discharge the debt (UCC 9-406(a)), so the same load can be billed by two payees | N-AL22 to N-AL50 | mostly *verified*; AAA Cooper, Central Transport and FedEx portal details partly *assumed* |
| **AL3** Shipper systems | **ERP market share:** no neutral survey for this segment. The best evidence is check Y's job postings: NetSuite 7 of 47, SAP 10, about 20 naming none.<br>**Unified accounting APIs:** they cover QuickBooks Online, NetSuite, Business Central and Sage Intacct. QuickBooks Desktop is covered only by Codat and Apideck; Acumatica only by Apideck. None of Merge, Codat or Apideck lists Epicor, Infor, SAP Business One, Sage 100/300, Global Shop, JobBOSS, Plex or DELMIAworks.<br>**Prices:** Merge $650/month for up to 10 linked accounts, then $65 each; Apideck €599/month for 25 consumers; Codat and Rutter quote on request.<br>**QuickBooks Online metering:** reads are metered, and Intuit's free Builder tier allows 500,000 read credits a month; calls above that are "blocked".<br>**For v1:** a CSV/Excel export of AP payments works for every ERP. Signed BOLs are most reliably pulled as the carrier's scan | N-AL51 to N-AL61; N-Y (check Y §3.4) | prices and connector lists *verified*; most per-ERP API details *assumed* |
| **AL4** Reference data | **EIA diesel prices:** free and public domain; the API needs a registered key, the bulk files don't.<br>**SMC3:** prices unpublished; +3% for 2026.<br>**Carrier rate APIs:** can return the customer's own pricing (ODFL, R+L), but ODFL's rejects pickup dates before today.<br>**SCAC codes:** licensed. $520/year online, $1,460 for the quarterly file; no derivative works.<br>**ClassIT+:** multi-customer terms still unpublished.<br>**Historical fuel tables:** the Wayback Machine has sparse 2024-2025 captures of the Estes, XPO, ODFL and ABF fuel pages. ODFL keeps a history tool online, and its 2022 fuel tariff is still downloadable. ABF's 2023 rules tariff is still online.<br>**Mileage:** PC*Miler unpublished. Google Routes costs $5 per 1,000 after 10,000 free, but has no truck SKU.<br>**Residential check:** Smarty costs $552/year for 12,000 lookups, including RDI. The USPS API terms limit use to USPS shipping.<br>**Detention times:** only from the customer's own records or visibility subscriptions; no export prices published | N-AL62 to N-AL73 | mostly *verified*; mileage and detention partly *assumed* |
| **AL5** Notifications | **Email:** SES $0.10 per 1,000; Postmark from $15/month for 10,000.<br>**Slack:** incoming webhooks post to one channel per URL and can't delete messages.<br>**Teams:** Office 365 connector webhooks stopped working 2026-05-18 to 22; use the Workflows app.<br>**SMS:** Twilio $0.0083 per segment plus carrier fees | N-AL01, N-AL03, N-AL74 to N-AL76 | *verified* |
| **AL6** Security and AI data | **Buyers:** expect a security questionnaire, SOC 2 (Type II preferred) and cyber insurance. This is from secondary sources; no evidence from buyers in the segment.<br>**AI providers:** all five platforms checked keep API data out of training under paid or commercial terms. Retention differs:<br>- **Anthropic** deletes within 30 days; zero data retention (ZDR) needs approval; the "Covered Models" (Fable/Mythos) require 30-day retention.<br>- **OpenAI** keeps abuse logs for up to 30 days; ZDR needs approval.<br>- **Bedrock** lets the account owner set zero retention for models that allow it.<br>- **Azure** keeps flagged samples for human review unless modified abuse monitoring is approved.<br>- **Gemini's** unpaid tier may use and human-review data.<br>**Carrier confidentiality:** carrier pricing agreements are marked proprietary and confidential, so the shipper's written authority should name the AI and cloud sub-processors | N-AL77 to N-AL86; N-AC03 | AI terms *verified*; buyer expectations *assumed* |

---

## 2. AL1 · Email ingestion

### 2.1 How AP and audit tools take invoices by email

| Tool | Address given to the customer | What the customer sets up | Files accepted | Several invoices in one email or PDF | Sender filter, duplicates | Label |
|---|---|---|---|---|---|---|
| **Ramp** | "_<company-name>@ap.ramp.com_"; separate per-entity addresses, or one "cross-entity" address | Forward by hand, or auto-forward: "Auto-forwarding works best for teams that receive invoices and vendor documents in a centralized mailbox" | "PDF, PNG, JPG, JPEG, WebP, GIF, HEIC, CSV, Word, and Excel" (no TIFF) | "Ramp creates a separate draft bill for each invoice it detects"; add "[Split]" to the subject line | Default "Only if sent by employees or my vendors"; "filters out exact duplicate files automatically by checking the file hash" | *verified* (N-AL08) |
| **Dext** | "@dext.cc - forwards one document per email"; "@multiple.dext.cc - splits each page of the attachment into separate documents" | A Gmail rule. Gmail "typically sends a **verification link** instead of a code"; Outlook works the same way | "PDF, JPG, PNG" | Per-page split on the @multiple address | Rule conditions such as from: invoices@vendor.com | *verified* (N-AL09, page dated 2026-07-29) |
| **BILL** | "companyname@bill.com", at least 8 characters before the @ | Give the address to vendors, or forward to it | not read | not read | not read | *assumed*, snippet; page returned 403 (N-AL10) |
| **Stampli** | A dedicated address per customer | Vendors email it | PDF only; up to 100 files per email; 50 MB per file | not read | not read | *assumed*, snippet; page returned 401 (N-AL11) |
| **Hubdoc** | "[custom]@app.hubdoc.com" | A Gmail filter, "forward it to" | not read | not read | not read | *assumed*, secondary (N-AL12) |
| **Loop** (freight audit) | "your dedicated Loop inbox" | "forward via email, SFTP, or API … instruct your carriers to send invoices directly" | not read | not read | not read | *assumed*, vendor (check Z, N-Z75) |
| **nVision** (FAP; rules for carriers) | — | — | ".PDF, .JPG, .TIFF" | "1 Invoice Per Email (including the backup documentation)" | — | *verified* in check Z (N-Z54) |

**Reading [our call]:** the market has settled on a forward-to address per customer, with three supports:
- a sender allowlist;
- de-duplication by file hash;
- splitting multi-invoice emails and PDFs.

TIFF support is uneven: Ramp and Dext don't list it, nVision accepts it.

### 2.2 What the customer has to set up

| Route | Steps | Who does it | Friction | Evidence |
|---|---|---|---|---|
| **Forward from Gmail / Google Workspace** | Add our address as a forwarding address; confirm the verification link Gmail sends to us; add a filter | AP clerk; a Workspace admin may have to allow forwarding | Low. We must receive and relay Gmail's verification email | *verified* (Dext, N-AL09); the Workspace admin switch *assumed* (memory) |
| **Forward from Microsoft 365** | An Exchange admin sets automatic forwarding to "On - Forwarding is enabled", ideally in a custom outbound spam policy covering only the AP mailbox. A "remote domain" setting can then limit forwarding to our domain | IT or MSP admin | **Medium to high.** The default "Automatic - System-controlled" "In 2021 … changed to **Off - Forwarding is disabled** for new organizations and for existing organizations that weren't actively using" it. Blocked mail bounces: "5.7.520 Access denied, Your organization does not allow external forwarding" | *verified* (N-AL13, 2026-08-18; re-checked) |
| **Carriers send to (or copy) our address** | One change per carrier, in its billing portal or through its billing rep. ODFL: "receive your invoices via email", "Sign up here for e-statement invoices". FedEx Freight Billing Online: "Opt in to email notifications", "Add users to your account" | Logistics or AP, per carrier | Medium: one request per carrier, but no IT work. The carrier's notification may not carry the PDF (§2.4) | *verified* (N-AL19, N-AL20) |
| **Manual upload** | Export and drag in | AP or logistics | Recurring effort | — |

### 2.3 Inbound email services: published prices and limits

| Service | Price as shown (page undated unless stated; read 2026-10-03) | Inbound included? | Size limit | Authentication results passed to us | Raw message | Label |
|---|---|---|---|---|---|---|
| **Amazon SES email receiving** | "$0.10 / 1,000 emails" received + "$0.09 for every 1,000 incoming email chunks" (256 KB); Mail Manager processing "$0.15 / 1,000 emails"; sending "$0.10 / 1,000 emails"; new AWS customers get "up to $200 in AWS Free Tier credits" for 6 months | Yes | not checked | `spfVerdict`, `dkimVerdict`, `dmarcVerdict` (+ `dmarcPolicy` on DMARC fail), `spamVerdict`, `virusVerdict`, each PASS / FAIL / GRAY / PROCESSING_FAILED | Raw MIME in `content` only for the SNS action; the S3 action stores the message | *verified* (N-AL03, N-AL04) |
| **Postmark** | Free "100 emails/month"; Basic "$15.00/mo" for "10,000 emails/month"; Pro "$16.50/mo"; Platform "$18.00/mo"; overage "$1.80 / 1,000" (Basic), "$1.30" (Pro), "$1.20" (Platform) | "Included on Pro and Platform plans only"; MX record points to inbound.postmarkapp.com | not found on the pages read | not found | not found | *verified* (N-AL01, N-AL02) |
| **SendGrid Inbound Parse** | No price on the page | Yes: MX record to `mx.sendgrid.net`, priority 10 | "Limit the total size of your message, including the message and attachments, to 30 MB" | "SPF" and "dkim" fields in the POST | Optional "POST the raw, full MIME message" | *verified* (N-AL05) |
| **Mailgun** | Free "$0/mo", "100 emails/day", "1 inbound route"; Basic "Starting at $15/mo", 10,000/mo, "5 inbound routes"; Foundation "Free for 1 month, then $35/mo", 50,000/mo, "Full access to inbound routing"; Scale "$90/mo", 100,000/mo | Yes, by plan | not read | not read | not read | *verified* (N-AL06) |
| **Cloudflare Email Routing / Email Workers** | Price not stated on the limits page (free, *assumed*) | Yes | "Inbound message size: 25 MiB. Messages larger than this are rejected"; 200 routing rules per domain; 200 destination addresses per account | not read | Worker handlers run under standard Workers CPU and memory limits; on the free tier "complex handlers may exceed these limits and fail to process a message" | *verified* (N-AL07) |

**Cost at scale [our calc].** Assume about 300 carrier emails per customer a month, averaging 1 MB (4 chunks). This volume is an assumption.
- **SES:** $0.0001 + 4 × $0.00009 = **$0.00046 per email**, about **$0.14 per customer a month**. At 100 customers (30,000 emails): $3.00 + $10.80 = **$13.80 a month**.
- **Postmark Pro at 30,000 emails:** $16.50 + 20 × $1.30 = **$42.50 a month**. This assumes inbound mail counts toward the volume, which was not verified.

Either way, ingestion is a rounding error against check AA's per-customer costs.

### 2.4 Edge cases

| Case | What the record shows | Handling **[our call]** |
|---|---|---|
| **Email with a portal link instead of an attachment** | FedEx Freight bills through FedEx Freight Billing Online with "email notifications" you opt into; the page doesn't say whether the PDF is attached (*verified*, N-AL20). ODFL offers email invoices and e-statements, format not stated (*verified*, N-AL19). Saia sends "regular emails with the latest invoice attached … PDF" (*assumed*, N-AL21). Small TL carriers billing from accounting apps often send "view invoice" links (*assumed*, memory). **Which LTL carriers send link-only emails is not established** | Never follow links automatically (phishing risk). Classify the email as "fetch needed" and pull the document from the carrier API or portal (§3). Ask pilot customers for one month of raw carrier emails |
| **TIFF attachments** | Carrier imaging defaults to TIFF:<br>- XPO: "If the user does not enter a format, all imaged documents will be returned in TIFF format" (N-AL25);<br>- Saia returns "GIF, TIF, JPG" (N-AL29);<br>- R+L sends ".jpg or .tiff or .pdf" (N-AL35).<br>Ramp and Dext don't list TIFF (all *verified*) | Convert multi-page TIFF to PDF at intake; keep the original |
| **ZIP attachments** | No evidence found | Unzip with size and depth limits (zip bombs) |
| **Invoice in the HTML body** | No evidence found in this check | Render the body to PDF; keep the raw HTML |
| **Several invoices per email or PDF** | Acumatica users are "manually separating the file into multiple documents" (check Z, N-Z18, *assumed*). nVision demands one invoice per email (*verified*). Ramp detects and splits; Dext splits by page (*verified*) | Classify each page (invoice, BOL, delivery receipt, W&R certificate, rate confirmation, notice of assignment, statement), split, and keep page provenance |
| **Spoofed invoices** | SES and SendGrid pass SPF, DKIM and DMARC verdicts (*verified*). With auto-forwarding, SPF is checked against the customer's forwarding server, not the carrier, so the carrier's DKIM signature and DMARC alignment carry the signal (mechanism *assumed*, memory) | A hard-to-guess address per customer, plus a sender allowlist of carrier domains and the customer's domain (as in Ramp's default). In v1 (audit only, no payments), spoofing threatens data quality. Payment fraud such as "remit-to" changes matters once payments start |

### 2.5 The alternative: connecting to the customer's mailbox

**Gmail:**
- `https://mail.google.com/`, `gmail.readonly`, `gmail.metadata` and `gmail.modify` are **Restricted** scopes (*verified*, N-AL15).
- An app that reaches restricted data "from or through a third-party server" needs a security assessment under "the App Defense Alliance and the cloud application security assessment framework (CASA)". "Google-empanelled security assessors" carry it out, "every 12 months after your assessor's Letter of Assessment (LOA) approval date" (*verified*, N-AL14, page updated 2026-08-19; re-checked).
- Exemptions: personal use or "only a few users"; apps in testing; service accounts reading only their own data; apps "used only by people in your Google Workspace or Cloud Identity organization"; "domain-wide installation" (*verified*).
- **Cost at one assessor** (TAC Security, undated page; *verified* at the lab's page, N-AL16):
  - Basic "$675 per application" a year: one Tier 2 assessment plus two revalidations;
  - Premium "$855";
  - Enterprise Tier 2 "$1800";
  - Enterprise Tier 3 "$4500";
  - "next year you would have to go through the process again";
  - scans take "1 -2 business days", and Google responds in "5-6 business days".
- Other labs: $900-1,500 (*assumed*, snippet).

**Microsoft 365 (Graph):**
- `Mail.Read` delegated: admin consent required "No". Application: "Yes", with the description "Allows the app to read mail in all mailboxes without a signed-in user" (*verified*, N-AL17).
- **RBAC for Applications** in Exchange Online lets an admin restrict `Application Mail.Read` to chosen mailboxes; it "replaces Application Access Policies" (*verified*, N-AL18, updated 2026-08-21):
  - it needs the Organization Management role group or Exchange Administrator;
  - it is set up in PowerShell (`New-ServicePrincipal`, `New-ManagementScope`, `New-ManagementRoleAssignment`);
  - the unscoped Entra grant must be removed, or there is "no effective resource scoping";
  - changes are cached for "between 30 minutes and 2 hours".
- Tenant policies blocking user consent, and publisher-verification rules, are *assumed* (not checked).

### 2.6 Which route is lighter? **[our call]**

| Route | Effort for us | Effort for the customer | Recurring cost | What we see | Verdict |
|---|---|---|---|---|---|
| Upload portal | Low | High, every month | ≈ $0 | Only what is sent | Day 1, and for look-back batches |
| **Forward to our inbox** | Low to medium (MX record, parser, splitter) | Gmail: a rule plus a confirmation. Microsoft 365: an admin opens external forwarding for the AP mailbox | under $50/month at 100 customers [our calc] | Forwarded mail only | **v1 default** |
| Carriers send to our address | Low | One request per carrier | ≈ $0 | Carrier mail only | Best long-term for the top 3-5 carriers |
| Gmail API | High: restricted scope, annual CASA, a security programme | One consent click (if Workspace allows it) | $675-4,500 per app per year, plus engineering | The whole mailbox unless filtered | Not v1 |
| Graph app-only | Medium to high: multi-tenant app, consent flow | Admin consent plus PowerShell scoping | Engineering | All mailboxes unless scoped | Not v1; maybe for larger customers |
| Graph delegated | Medium | User consent, often blocked by tenant policy (*assumed*) | Engineering | That user's mailbox | Not v1 |

---

## 3. AL2 · Getting documents from carriers

### 3.1 The major LTL carriers

"Bill-to only" means the documents are shown only to the party billed on that PRO. A blank or "not found" means nothing was found on the pages read.

| Carrier | Invoice or billing data | Document images (types) | Rate quote | Authentication | Third-party terms | Cost / limits | Sources |
|---|---|---|---|---|---|---|---|
| **ODFL** | No invoice API among its REST services: eBOL v3.1, Document v1.0, Pickup v3.0, Rate Estimate v1.0, Tracking v2.0 (*verified*). Invoices by email and e-statements; view and pay online (*verified*) | Document API v1.0, updated 2026-06-04: BOLs, delivery receipts and delivery photos (snippet). Also Inspection Certificate, Weight Certificate, Weight Verification, Research Verification and Pickup Photo, each "Linked to the bill to party on the pro" (*verified*, check T, N-T18) | Rating API v1.0 (updated 08/21/26). `billToAccount`: "Include in all requests for the most accurate rates based on your OD pricing". `pickupDate` "Must be greater than or equal to today" (*verified*) | ODFL.com username and password, exchanged for a session token; "Session tokens expire one hour after issue" (*verified*) | Optional fields `integrationCustomer` ("The name of the company submitting the request on behalf of our mutual customer"), `transportationManagementSystem` and `thirdPartyLogistics` (*verified*) | No fee stated; SOAP endpoints retire 2027-03-01 (*assumed*, snippet); contact api@odfl.com | N-AL19, N-AL22, N-AL23 |
| **XPO** | None of its six APIs covers invoices (*verified*) | Imaging API, one PRO per call. Types: BL, DR, DRR, CUST, IR (Inspection Report), LOA, NCIC (NMFC Certificate), WI (Weights and Corrections), WRFO (Weights and Research photos). Formats PDF, TIFF, PNG, JPEG; **default TIFF**; returns `scanDate` (*verified*, guide v1.0 dated 2019-09-04) | Rating API: Rate Quote and Spot Quote, create and retrieve quotes (*verified*); retrieval "by confirmation number or date range" (snippet) | "register on the web and subscribe", using "Your Web User ID" (*verified*) | The signup asks for the name of any "TMS/Software Program" used to connect (*verified*) | Rate limits are in the "API Help Center on LTL.XPO.com" (pointer *verified*; not read). No fee stated | N-AL24, N-AL25 |
| **Estes** | The Subscription API includes an "Invoice Subscription" for "receiving invoice-based notifications" (*verified*) | Images API, "supports 14 different types of document images"; list not on the page (*verified*). W&R certificates in My Estes (check T, *assumed*) | Rate Quote API (*verified*) | Client ID and secret requested by email, then an API key, then a bearer token using "the appropriate MyEstes username and password" (*verified*) | not stated | not stated | N-AL26, N-AL27 |
| **Saia** | not found | Get Images: "BOL", "POD", "WGT"; weight certificates with "&WC=Yes"; formats "GIF, TIF, JPG" (*verified*) | Rate quote via the developer portal: "Saia Secure credentials allow you to have access to your rates" (*assumed*) | Base64 of "Saia Secure user id : password" (*verified*); plus a portal subscription key (*assumed*) | not found | not found | N-AL29, N-AL30 |
| **ABF (ArcBest)** | not found; the full docs are behind sign-in | Document retrieval: "signed bills of lading, delivery receipts, packing lists, customs documents, weight confirmations and more" (*verified*, article 2018-02-08) | "Rate quote, Volume quote" (*verified*) | An arcb.com account; the "API ID" is visible after sign-in (*assumed*) | not found | not stated | N-AL31, N-AL32 |
| **FedEx Freight** | No invoice operation in the Freight LTL API (*verified*). FedEx Freight Billing Online offers opt-in email notifications, PDF downloads, "supporting documents", "Dispute Entire Invoice" within 180 days, and "Add users to your account" (*verified*) | The API generates BOLs and labels for new shipments (*verified*). Signature proof of delivery via the Track API (*assumed*). A copy of the weight verification "upon request" (check T, *verified*) | "Get Freight LTL Rate Quotes", based on origin, destination "and various other inputs"; account-specific pricing not stated (*verified*) | OAuth on developer.fedex.com (*assumed*) | Compatible-provider programme (*assumed*, not checked) | not stated | N-AL20, N-AL33 |
| **R+L** | Document Retrieval returns an "Invoice" image type (check T, *verified*). EDI 210 covers "Prepaid, Collect, 3rd Party, Corrections and Additional Charges" by default (*verified*) | BillOfLading, DeliveryReceipt, Invoice, WeightCertificate, NmfcCertificate, LetterOfAuthorization, DeliveryPhoto, for documents "you have access to" (check T, N-T27). An EDI image feed carries BOL, DR, WIC (weight certificate), LOA and NMFC as jpg, tiff or pdf (*verified*) | "customer specific LTL rate quotes". The response gives `Charge`, `NetCharge` and `CustomerDiscounts`; `PickupDate` "Will default to today's date if not passed in" (*verified*) | An `apiKey` header (*verified*) | The EDI form has a "Third-Party Payor or Logistics Company (Company name acting on behalf of the customer…)" field (*verified*). Third parties need a letter of authorisation (*assumed*, snippet) | not stated | N-AL34, N-AL35, N-AL36 |
| **SEFL** | not found | Web Connect can "receive a Proof of Delivery" (*verified*) | "get a rate quote" (*verified*) | not stated | not stated | "an inexpensive way…" (*verified* wording; no fee given) | N-AL38 |
| **TForce Freight** | **"Invoicing" and "Billing Discrepancy" APIs listed as "Coming Soon"** (*verified*) | Documents API: "Request Bill of Lading, Delivery Receipts, and Weight and Inspection Certificate document images" (*verified*). Types WRC, REWE, CMC (check T, N-T29) | Rating API (*verified*) | not stated on the portal home page | not stated | not stated; contact groundfreightapisupport@tforcefreight.com | N-AL37 |
| **AAA Cooper** | not found | "Imaging Web Service retrieves images and documents" (*assumed*) | Rate Estimate (*assumed*) | not found | not found | not found | N-AL40 |
| **Averitt** | not found | "PRO Document Request Types" and "PRO Document Request", plus order-number versions; types not listed (*verified*) | LTL Rate Quote, Truckload Rate Quote, "Dynamic LTL Rate Quote (ExactRate)" (*verified*) | "An Averitt.com username and password is required" for the dashboard; request an API key (*verified*); the key is passed as a URI parameter (*assumed*) | not stated | not stated | N-AL39 |
| **Central Transport** | not found | Web services include documents (*assumed*) | Rate quote (*assumed*) | An account with Web Services enabled yields a "customer number and access code" (*assumed*) | not found | not found | N-AL40 |

**Reading [our call]:**
1. **Supporting documents can be reached by API at most big LTL carriers, using the customer's own login.** That covers BOLs, delivery receipts, W&R and inspection certificates, and photos. Check T found the same, with ODFL limiting access to the bill-to party.
2. **Invoices themselves still arrive by email, EDI or portal.** No carrier offers an invoice-data API yet; TForce says one is coming.
3. **Third-party use is anticipated but not written down.**
   - The forms expect it: ODFL's `integrationCustomer` and `thirdPartyLogistics` fields, XPO's question about the TMS name, R+L's third-party payor field.
   - Neither published fees nor published bans were found.
   - So: get a letter of authority from each customer, keep the credentials in a vault, and ask the carriers about their terms.

### 3.2 Multi-carrier document aggregators

| Provider | What is offered | What it needs | Price | Label |
|---|---|---|---|---|
| **project44** LTL Image Retrieval (`POST /api/v4/ltl/images/query`) | Document types "BILL_OF_LADING", "DELIVERY_RECEIPT", "WEIGHT_CERTIFICATE", "INVOICE", "INSPECTION_CERTIFICATE", "LETTER_OF_AUTHORIZATION", "LUMPER_CERTIFICATE", "PACKING_SLIP". Formats PDF, TIF, PNG, GIF, JPG (default PNG) | `capacityProviderAccountGroup` (the shipper's own carrier accounts), `proNumber`, destination `postalCode` and `documentType`; `pickupDate` optional ("Some carriers require this") | Not on the page; no carrier list | *verified* (N-AL41) |
| **SMC3 CarrierConnect XL** | Shippers can "view and download digital documents including weight certification, proof of delivery, bills of lading"; invoices too (*assumed*, snippet) | not stated | Not published. For 2026, a "3% increase" on "Czarlite®, RateWare® XL, CarrierConnect® XL and BatchMark® XL license fees" | *verified* (N-AL43, N-AL44) |
| Others (TMS vendors, Banyan and so on) | not checked | — | — | — |

**Reading [our call]:** project44 normalises the carriers' APIs but still needs the shipper's credentials for each carrier. It saves integration work, not authorisation work. For a startup, connecting directly to the 5-6 carriers with the most spend is cheaper at first.

### 3.3 EDI 210 for a small third party

**How it works.** The carrier sends 210s to the EDI ID (ISA sender or receiver) named in the setup. R+L's "EDI Trading Partner Profile" (*verified*, N-AL35) shows what a setup asks for:
- **Parties:**
  - "Trading Partner (Company that is requesting the EDI setup with R+L)";
  - "Are you a third-party logistics company?";
  - "Third-Party Payor or Logistics Company";
  - "Bill To Information (Required on a 210)".
- **Transmission:** "VAN", "FTP Direct (Preferred)" or "SFTP Direct"; "Only PGP Encryption is supported".
- **Process:** test and production dates; ISA sender ID and qualifier; "If you are requesting a 210 Invoice a 997 is required".
- **Default content:** "you will receive all Invoices (Prepaid, Collect, 3rd Party, Corrections and Additional Charges) via EDI".
- **Images:** an optional image feed (BOL, DR, WIC, LOA, NMFC).

Estes supports "204", "211", "210", "214", "212", "990" and "997" via EDI@estes-express.com, with no minimum volume, setup time or fee stated (*verified*, N-AL28). **Watch-out:** TForce stops mailing delivery receipts and BOLs once electronic invoicing is set up (check AC, N-AC14).

| Option | Published price (date shown) | Label |
|---|---|---|
| **Nexus VAN** | Entry "$250/monthly" for up to 3,000 KC; Mid-tier "$2,499/monthly" for up to 35,000 KC; Growth "$4,499/monthly" for up to 75,000 KC; overage from "$0.08 per KC" (Entry) to "$0.05 per KC" (Enterprise). Says customers never pay setup, trading-partner or mailbox fees (undated) | *verified* (N-AL45) |
| **Orderful** | "Web EDI Fulfillment" "$189/month per trading partner"; "Integrated" "Starting at $399/month"; Enterprise "Custom" (more than 20 trading partners). Content "as of 2025" | *verified* (N-AL46) |
| **Stedi** | The pricing page now lists only healthcare transactions (claims, eligibility, ERAs): "No monthly minimums, setup fees". Freight X12 (210) is not addressed | *verified* (N-AL47) |
| Typical VAN fees | "$0.10-$0.30 per KC" and "monthly VAN fees of $50 to $500"; Kleinschmidt (a transport VAN) "start at $200 per month" | *assumed* (N-AL48) |
| SPS Commerce; AS2 software | not checked | — |

**Cost [our call / our calc].**
- If a 210 averages about 1 KC (an assumption), Nexus's $250 entry tier covers about 3,000 invoices a month: **about $0.08 per invoice** at full use.
- Orderful's per-trading-partner model costs **$1,512 a month for 8 carriers** [our calc], which doesn't fit v1.
- Whether carriers set up EDI for small accounts was **not found**. R+L and Estes state no minimum.

### 3.4 TL carriers, brokers and factoring companies

| Source of the bill | How it arrives | Evidence |
|---|---|---|
| Asset-based TL carrier | A PDF invoice by email, with the signed BOL used as the POD, the rate confirmation and any lumper receipt | *assumed* (check Z, N-Z58); public tariffs such as Werner's (check AC, N-AC24) |
| Broker | The shipper gets the broker's invoice, not the carrier's. On the carrier side, C.H. Robinson requires "an invoice with the Carrier Name and C.H. Robinson Load Number" | *verified* (check AC, N-AC09) |
| **Factoring company** | A Notice of Assignment (NOA) on the factor's letterhead tells the payer to pay the factor until the factor revokes it in writing | *assumed* (N-AL50) |
| **The law** | UCC § 9-406:<br>- (a): "After receipt of the notification, the account debtor may discharge its obligation by paying the assignee and **may not discharge the obligation by paying the assignor**."<br>- (c): the assignee "shall seasonably furnish reasonable proof that the assignment has been made".<br>- (d): a term restricting assignment "is ineffective" | *verified* (N-AL49; (a) re-checked) |

**Duplicate-billing risk [our call].** The same load can be billed by both the carrier and its factor. If the shipper pays the carrier after receiving an NOA, the factor can still collect, and the overpayment must be recovered from the carrier. The audit should:
- keep a payee register per carrier (by MC/DOT number), with any NOA on file;
- match loads across payees by BOL, load or PRO number, date and amount;
- flag changes to the remit-to address;
- treat NOA letters as a document type at intake.

This check is worth most **before** payment.

---

## 4. AL3 · Shipper-side systems

### 4.1 Which ERP or accounting systems this segment uses

- **No neutral market-share survey** for US manufacturers and distributors with 20-499 staff was found (two searches).
- **Best local evidence: check Y's 47 job postings** (N-Y; *verified* there):
  - NetSuite 7, all at firms without a "large" marker;
  - the SAP family 10 (Business One once);
  - Epicor, Dynamics GP and Infor SyteLine once each;
  - no Acumatica, Sage, Plex or ECI;
  - about 20 named no ERP.
- **Secondary claims** (*assumed*, N-AL61):
  - "570 verified Manufacturing ERP implementations": SAP 32%, Microsoft Dynamics 18%, Infor 14%, Odoo 13%, NetSuite 9%;
  - "NetSuite accounts for roughly 15% of ERP installations among mid-size distributors";
  - small manufacturers often pair a shop MRP (JobBOSS², E2) with QuickBooks Online as the ledger.

### 4.2 Can each system be read by API (vendor bills, payments, attachments)?

| System | API for bills, payments, attachments | Covered by a unified API? (Merge / Codat / Apideck connector lists, *verified*) | Label |
|---|---|---|---|
| **QuickBooks Online** | Bill, BillPayment and Attachable entities (*assumed*, snippet). **Reads count as "CorePlus" calls and are metered** (*verified*, from Intuit guide v1.2, 03.2026):<br>- **Builder:** no charge; "500,000" CorePlus credits a month; calls above that "will be blocked";<br>- **Silver:** "US$300"/month, "1 million" credits, then "US$3.50" per 1,000 calls between 1M and 10M;<br>- **Gold:** "US$1,700", "10 million";<br>- **Platinum:** "US$4,500", "75 million".<br>Writes ("Core") are "unmetered and uncharged" | Merge, Codat and Apideck all list it | fees *verified* (N-AL57); entities *assumed* (N-AL58) |
| QuickBooks Desktop / Enterprise | No cloud REST API (Web Connector, *assumed*) | Codat ("On-premise") and Apideck; not Merge | lists *verified* |
| **NetSuite** | REST record `vendorBill`. Files "are not supported via REST Web Services", so use a RESTlet or the SOAP attach call. "Bill Capture" by email in the product | All three list it | *assumed* (N-AL59) |
| **Dynamics 365 Business Central** | API v2.0 is "enabled by default" online, under the Microsoft APIs Terms of Use (*verified*). Resources such as purchaseInvoices, vendorPayments and attachments (*assumed*, memory) | All three list it | N-AL60 |
| Dynamics GP | eConnect and web services (*assumed*) | none | — |
| **Sage Intacct** | AP bill, payment and attachment objects (*assumed*) | All three list it; Apideck also lists "Sage Intacct REST" | lists *verified* |
| Sage 100 / 300 | No modern REST API documented (*assumed*) | **None**: Codat and Apideck list Sage 50, and Codat lists Sage 200, but neither lists 100 or 300 | *verified* by absence |
| Epicor Kinetic / Prophet 21 | REST business objects (*assumed*) | none | *verified* by absence |
| Infor (CSI/SyteLine, SX.e) | ION API (*assumed*) | none | *verified* by absence |
| SAP Business One | Service Layer (*assumed*) | none (Apideck lists SAP S/4HANA Cloud only) | *verified* by absence |
| **Acumatica** | Contract-based REST API (*assumed*) | **Apideck only** ("Acumatica", "MYOB Acumatica") | *verified* |
| Global Shop, JobBOSS²/E2, Plex, DELMIAworks | not established | none | *verified* by absence |

### 4.3 Unified accounting APIs: prices

| Vendor | Published price (as shown, undated unless stated) | Fit for this segment **[our call]** | Label |
|---|---|---|---|
| **Merge** | Launch: "First 3 free" production linked accounts; "$650/month for up to 10 total production Linked Accounts"; "$65 per Linked Account after". Professional and Enterprise are "Contract-based pricing" | Cloud ledgers only (no QuickBooks Desktop or Acumatica). 50 customers = $650 + 40 × $65 = **$3,250/month** [our calc] | *verified* (N-AL51, N-AL52) |
| **Apideck** | Launch "€599"/month for 25 consumers (one API category); Scale "€1,299"/month for 100 consumers; €2,199/month at 200 (€10.99 each); a 30-day trial. A consumer counts as "active" if it made at least one call that month | Widest coverage, including Acumatica and QuickBooks Desktop/Enterprise | *verified* (N-AL53, N-AL54) |
| **Codat** | Pricing page returned 404. Snippets: a "Start-up" plan at $30/month; roughly $30-50 per connected company; platform fees of $12-24k a year | Includes QuickBooks Desktop, NetSuite, Business Central and Intacct | connectors *verified* (N-AL55); price *assumed* |
| **Rutter** | Free 30-day sandbox; Full Access: "Get a custom quote" | — | *verified* (N-AL56) |
| Railz | not checked | — | — |

### 4.4 The lowest-effort path: a CSV/Excel export of AP payments **[our call]**

Check AC's request R2 sets the minimum (*verified* there): vendor, invoice number, invoice date, amount, paid date and payment reference. Suggested standard columns:

| Column | Why the audit needs it |
|---|---|
| Vendor ID, vendor name, remit-to name and address | Map to the carrier's SCAC; catch factoring and NOA payees |
| Vendor invoice number (usually the PRO), plus any external document number | The duplicate key; joins to carrier documents |
| Invoice date, posting date, due date | Late fees; 180-day windows |
| Gross amount, discount taken, amount paid, any short-pay or credit lines | Overpayment and duplicate math |
| Payment date, method (check/ACH/card), payment reference, void flag | Proof of payment; reversals |
| GL account or cost centre; PO, BOL or memo; entity or location | Selects the freight vendors; joins to BOLs |
| Currency | Canada lanes |

Remove bank account and routing numbers at source, as check AC's R2 requires.

### 4.5 Where BOLs live

| Location | Format and export | Evidence |
|---|---|---|
| Carrier portal or BOL API, if the shipper creates BOLs there | XPO's BOL API can "list individual and multiple submitted BOLs" and "retrieve and email a BOL PDF"; ODFL eBOL v3.1; Estes BOL built to the "NMFTA Digital LTL Council standard" | *verified* (N-AL24, N-AL22, N-AL26) |
| ERP shipping module (prints VICS BOLs), or shipping software | PDF printouts; report exports | *assumed* |
| TMS (about 10-15% adoption under $25-75M of spend) | Export | check Y §2.2 |
| 3PL portal, when the 3PL is the bill-to party | 3PL access only | check T §3.2 |
| **The signed BOL as scanned by the carrier** | XPO "BL" type; ABF "signed bills of lading"; R+L "BillOfLading" | *verified* |

**Reading [our call]:**
- For reweigh and reclass disputes, the proof is the shipper's own paper (check T §3.2).
- The signed BOL is easiest to get from the carrier's imaging.
- Spec sheets must still come from the shipper.

---

## 5. AL4 · Reference data the audit math needs

| Item | Availability | Licence / terms | Price (as shown) | Label | Source |
|---|---|---|---|---|---|
| **SMC3 CzarLite / RateWare XL** | A licensed product, sold through SMC3 | Re-rating on behalf of clients: terms not public | Not published. For 2026: a "3% increase"; "RateWare XL data modules pricing will remain the same" | *verified* (press release); price not found | N-AL44, N-AC34 |
| **Carrier rate APIs: do they return the contract price?** | **ODFL, yes:** `billToAccount` gives "the most accurate rates based on your OD pricing". **R+L, yes:** "customer specific", with `CustomerDiscounts`. Saia: "access to your rates" (*assumed*). XPO, Estes, ABF, FedEx, TForce, Averitt: not stated | The customer's own credentials | No fee stated | *verified* (ODFL, R+L) | N-AL23, N-AL34 |
| **Can they price a past ship date?** | **ODFL, no:** `pickupDate` "Must be greater than or equal to today". R+L defaults to today; past dates not stated. FedEx: "Past ready time or past date … should not be entered to schedule a pickup" (pickup context). XPO: existing quotes can be retrieved | — | — | *verified* | N-AL23, N-AL33, N-AL24 |
| **NMFTA ClassIT+** | Prices are in checks T and AA ($2,967-9,809 a year for API access) | Multi-customer and third-party terms **not public**: "transaction guidelines will be defined in license agreements" | — | *assumed* (snippet) | N-AL64, N-T41 |
| **NMFTA SCAC codes** | Online lookup; quarterly or daily files; a web service | "Publication or reproduction of the SCAC®, in whole or in part, in any public forum… or the creation of any derivative works… without specific licensing, is strictly prohibited" | SCAC Online "$520.00" for a "12-Month Subscription"; SCAC Quarterly Data "$1,460.00" (renewal "$1,160.00" for 2024 subscribers); Web Services API "$3,050 for 25K Records per month … $18,250 for 1000K" (*assumed*, snippet) | *verified* except the API price | N-AL63 |
| **EIA diesel price** | API, bulk files ("zipped datasets updated twice daily"), an Excel add-in, web tables (check AC, N-AC25) | The API needs a key ("Registration and compliance with the API Terms of Service Agreement"); "EIA data is provided free of charge"; "U.S. government publications are in the public domain"; cite as "Source: U.S. Energy Information Administration (date)" | Free | *verified*; **no key registered** (rules) | N-AL62 |
| **Historical carrier fuel tables** | See the Wayback test below. ODFL's page "Fuel Surcharge Rates - Current & History" has a search and export tool. ODFL tariff 128-AA ("EFFECTIVE June 1, 2022", "Cancels TARIFF ODFL 128-Z") is still downloadable, while the page links 128-CC as current | Public carrier pages | Free | *verified* | N-AL65 to N-AL67 |
| **Carrier rules tariffs** (accessorial prices) | Current versions for 9 carriers (check T §3). **Old versions can stay online:** ABF 111-AQ ("apply on shipments tendered on or after November 7, 2022", "Last revised: January 10, 2023") is still on arcb.com, while 111-AU (2026-06-22) is current | Public | Free | *verified* (one carrier tested) | N-AL68, check T |
| **TL mileage** | PC*Miler is the industry reference (*assumed*). Rand McNally MileMaker: price not found. HERE truck routing ≈$2.75 per 1,000 with 5,000 free a month (*assumed*, partner site). Google Routes Essentials: 10,000 free a month, then "$5.00" per 1,000, falling to "$0.38" at the highest tier; Pro "$10.00" to "$0.75"; **no truck SKU in the pricing table** | "Billing-grade" means the contract's named engine and version **[our call]** | PC*Miler not published by Trimble ("PC*Miler Web … $84.99/month per user", *assumed*) | Google *verified*; rest *assumed* | N-AL69, N-AL70 |
| **Residential delivery check** | **Smarty** US address verification includes "Residential vs. commercial (RDI)"; no overage costs (it returns error 402).<br>**USPS APIs:** the terms (updated 2026-01-22) allow use "only … to facilitate USPS shipping or mailing transactions unless specifically allowed otherwise", and bar a database "for third-party usage" | Smarty is commercial. USPS is **not usable** for freight audit **[our call]** | Smarty Professional "$552 per year" for 12K lookups (→ **$0.046 per lookup** [our calc]); free trial of "42 days" with "1,000 address lookups" | *verified* | N-AL71, N-AL72 |
| **Detention evidence** | Visibility platforms log arrival and departure events (project44 TL events "ARRIVAL_AT_STOP" / "DEPARTURE_FROM_STOP", *assumed*). An export exists only if the customer or its broker subscribes. ELD data belongs to the carrier (*assumed*). The best evidence is still the delivery receipt's "wait time" boxes and dock logs (check AC §3.5, §6) | Platform contracts | **No pricing found** | *assumed* | N-AL42, N-AL73 |

**Wayback Machine test** (read-only availability API, 2026-10-03; seven queries, each returning the single closest capture):

| Carrier fuel page | Date requested | Closest capture returned |
|---|---|---|
| Estes `/resources/fees-and-surcharges/fuel-surcharge` | 2024-06-01 | **2024-04-05** 01:29:45 (HTTP 200) |
| Estes | 2025-07-01 | **2025-09-16** 01:46:55 (200) |
| XPO `/fuel-surcharge-table/` | 2024-07-01 | **2024-07-07** 16:46:48 (200) |
| XPO | 2025-01-15 | **2024-10-13** 06:15:40 (200) |
| XPO | 2025-07-01 | **none returned** |
| ODFL `/us/en/resources/fuel-surcharge.html` | 2024-07-01 | **2024-12-09** 04:55:08 (200) |
| ABF `/abf-freight/resources/fuel-surcharge.html` | 2024-07-01 | **2024-09-07** 17:01:50 (200) |
| ABF | 2025-07-01 | **2025-05-23** 17:19:38 (200) |

(*verified*, N-AL65.) The CDX listing API and the capture pages themselves sit on web.archive.org, which the fetch tool cannot reach. So the captures couldn't be counted, and we couldn't confirm that each one holds the table rather than an empty JavaScript shell. Check AC also found that Estes's history tab did not load.

**Reading [our call]:**
- Captures are months apart. They can recover a carrier's band table (diesel price band → percentage), and with EIA's weekly prices that rebuilds the weekly percentages, provided the bands didn't change in between.
- Start our own weekly archive of fuel pages and tariff PDFs now. It costs almost nothing.

---

## 6. AL5 · Notifications and dispute plumbing (brief)

| Channel | Option | Price / terms (as shown) | Label |
|---|---|---|---|
| Transactional email | Amazon SES | "$0.10 / 1,000 emails"; attachments "$0.12 per GB" | *verified* (N-AL03) |
| | Postmark | Basic "$15.00/mo" for 10,000; Pro "$16.50/mo"; overage $1.80 or $1.30 per 1,000 | *verified* (N-AL01) |
| Slack | Incoming webhook | One URL per user and channel; webhooks "do not allow you to delete a message after it's been posted" and "cannot override the default channel". Price and rate limit not on the page (about 1 message per second, *assumed*) | *verified* (N-AL74) |
| Microsoft Teams | Office 365 connectors (the old incoming webhooks) | "progressively disabled" 2026-05-18 to 2026-05-22; "After these dates, Office 365 Connectors will no longer function". The replacement is the Workflows app on Power Automate (update dated 2026-04-14) | *verified* (N-AL75) |
| SMS | Twilio | "$0.0083" per segment, plus carrier fees (AT&T "$0.0035", T-Mobile "$0.0045", Verizon "$0.005"), giving **$0.0118-0.0133 per outbound segment** [our calc]. A2P 10DLC registration fees apply (amounts not fetched) | *verified* (N-AL76) |
| Disputes to carriers | Carrier email or portal: FedEx Freight Billing Online's "Dispute Entire Invoice" within 180 days (N-AL20); the Estes discrepancy tool; ODFL claims (check T §3.2; check AK §5.2) | Free | *verified* |

---

## 7. AL6 · Security and data handling (brief)

### 7.1 What mid-market finance teams ask a new vendor for

| Ask | What the record says | Label |
|---|---|---|
| Security questionnaire | SIG Lite (about 128 questions) for mid-market buyers; SIG Core (627) for Fortune 1000 programmes | *assumed* (N-AL85) |
| SOC 2 | Type I tests the design of controls at a point in time; Type II tests that they work, over 3-12 months. Buyers often want Type II. It costs about $20-50k a year, recurring (check AA, N-AA51) | *assumed* |
| What peers have | Cass: SOC 1 Type 2 and SOC 2 Type 2. Trax: SOC 2 Type 2 and ISO 27001 | *assumed* (N-AL86) |
| Cyber insurance | Contracts often set minimums of $1-5M; SOC 2 doesn't require it | *assumed* (N-AL85) |
| Evidence from buyers in this segment | **None found** (check Z §4); an interview item | — |

### 7.2 AI providers' data terms for API use

| Provider | Training on API data | Default retention | Zero data retention (ZDR) | Label |
|---|---|---|---|---|
| **Anthropic API** | Commercial Terms: "Anthropic may not train models on Customer Content from Services"; "Customer Content is Customer's Confidential Information" (effective 2025-06-17). Docs: "Retained data is never used for model training without your express permission" | Privacy Center (updated 2026-07-01): "we automatically delete inputs and outputs on our backend within 30 days of receipt or generation". The exceptions:<br>- the Files API;<br>- ZDR agreements;<br>- Usage Policy enforcement (flagged inputs and outputs kept "up to 2 years", classifier scores "up to 7 years");<br>- the law.<br>Docs: conversation content "is not retained by default; the exception is Covered Models" | "contact the Anthropic sales team"; enabled per organisation.<br>**Covered:** the Messages and Token Counting APIs, for eligible features.<br>**Not covered:** the Console, Managed Agents, Batch processing ("No"), the Files API ("No"), code execution ("No").<br>Fable 5.1, Mythos 5.1, Fable 5 and Mythos 5 "require 30-day data retention and are not available under ZDR unless expressly authorized" | *verified* (N-AL77 to N-AL80) |
| **OpenAI API** | "As of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in…)" | Abuse-monitoring logs "up to 30 days" | ZDR and modified abuse monitoring are "subject to prior approval by OpenAI".<br>**Eligible endpoints:** `/v1/chat/completions`, `/v1/responses` (with limits), `/v1/embeddings`.<br>**Not eligible:** Assistants, Threads, Vector Stores | *verified* (N-AL81) |
| **Google Gemini API** | **Unpaid tier:** data is used "to provide, improve, and develop Google products", and "Human reviewers may read, annotate, and process your API input and output".<br>**Paid tier:** "Google doesn't use your prompts … or responses to improve our products" | Paid tier: logged "for a limited period of time" for abuse detection (terms effective 2026-03-23) | Vertex AI: the page didn't render (**not verified**) | *verified* (Gemini API, N-AL82) |
| **AWS Bedrock** | Model providers "don't have access to Amazon Bedrock logs or to customer prompts and completions" | Set by the account:<br>- `none`: "No request or response data is written to durable storage";<br>- `default`: per model;<br>- `aws_review`: kept "for up to 30 days" inside AWS for models that require human review (currently Claude Fable 5 and 5.1) | The account sets `none` itself, for models that allow it (e.g. Claude Opus 4.8); policies can enforce it | *verified* (N-AL83) |
| **Azure** (Foundry Models sold by Azure, incl. Azure OpenAI) | Prompts and completions "are NOT available to OpenAI" and are "NOT used to train any generative AI foundation models without your permission" | Flagged samples may be stored for human review (period not stated on this page, updated 2026-06-05) | "managed customers may apply to modify abuse monitoring", which stops data storage | *verified* (N-AL84) |

**Why this matters for carriers' confidential pricing [our call]:**
- **The agreements are confidential.** A SEFL agreement reads "PROPRIETARY AND CONFIDENTIAL PROPERTY OF SOUTHEASTERN FREIGHT LINES" (check AC, N-AC03).
- **Carriers already accept billing agents.** The YRC-First Brands contract routes freight bills "care of" ITS Traffic Systems, Blue Grace and Williams and Associates (N-AC05). 49 CFR 378 lets a shipper "or its authorized agent" file claims (check T).
- **So the shipper's letter of authority and NDA should:**
  - name us as agent;
  - list our cloud and AI sub-processors;
  - commit to providers whose terms treat content as confidential and bar training.
- **For customers who ask, offer ZDR:**
  - Anthropic or OpenAI ZDR (after approval), or Bedrock with `none`;
  - avoid the Covered Models for ZDR customers;
  - never send customer documents to a free or unpaid tier.

---

## 8. Design implications for ingestion and data

1. **Build intake in this order [our call]:**
   - **(a) weeks 0-2:** manual upload, with a guided export checklist;
   - **(b) weeks 2-6:** a forwarding inbox per customer;
   - **(c) months 2-4:** carrier document APIs on the customer's credentials for its top LTL carriers. EDI 210 copies only for customers already on EDI or with high volume;
   - **(d) last:** the ERP connection. A CSV export first, then a unified API once about 10 customers share a cloud ledger.
2. **Intake stack [our call]:**
   - SES receiving (or Postmark Pro) on a subdomain;
   - a hard-to-guess address per customer;
   - raw MIME stored unchanged;
   - SPF, DKIM and DMARC verdicts recorded;
   - a sender allowlist;
   - duplicates caught by file hash and by (SCAC, PRO, amount).
3. **A normaliser for the edge cases [our call]:**
   - TIFF→PDF;
   - safe unzip;
   - HTML body→PDF;
   - splitting multi-invoice PDFs;
   - classifying each page (invoice, BOL, DR, W&R certificate, rate confirmation, NOA, statement), keeping page provenance.
4. **A customer setup kit [our call]:**
   - **Gmail:** the steps, including confirming Gmail's verification email;
   - **Microsoft 365 admin:** a custom outbound spam policy that allows forwarding for the AP mailbox only, plus a remote domain limited to our domain;
   - **carriers:** a short template asking each one to send invoices to our address.
5. **No mailbox connectors in v1 [our call].** Gmail's route needs CASA every 12 months ($675-1,800 a year at TAC for Tier 2) and a security programme behind it. If built later, Graph app-only with RBAC scoping to one AP mailbox is the narrower route.
6. **Carrier documents [our call]:**
   - credentials kept in a vault, with a letter of authority per customer;
   - fill ODFL's `integrationCustomer` field;
   - start with the carriers that expose W&R and inspection documents (ODFL, XPO, Saia, R+L, TForce, ABF, Estes);
   - for FedEx, become an added user in FedEx Freight Billing Online;
   - pull documents only for flagged bills (reweigh, reclass, detention), to stay light on the carriers.
7. **Rate APIs probe today's pricing; they can't re-rate a look-back [our call].**
   - ODFL rejects past pickup dates, and general rate increases move base rates.
   - For past shipments, use the shipper's agreement and quotes; XPO can retrieve stored quotes.
   - Use SMC3 base rates only after SMC3 confirms a licence for re-rating on behalf of clients.
8. **Archive reference data from day 1 [our call]:**
   - weekly snapshots of 12 carriers' fuel pages and tariff PDFs;
   - ODFL's history export;
   - old tariff PDFs while they are still on carriers' servers;
   - Wayback captures to fill gaps;
   - for the diesel index, EIA's keyless bulk or XLS files, until the founders register an API key under a company identity.
9. **Licensed data [our call]:** don't redistribute SCAC lists; use SCAC Online internally ($520 a year). Ask NMFTA about multi-customer ClassIT+ use before building reclass checks (check T §7).
10. **Residential checks [our call]:** Smarty RDI (≈4.6¢ a lookup), only on bills carrying a residential charge. Not USPS APIs, because of their terms.
11. **Detention [our call]:** ask only customers who already keep dock or appointment logs or visibility exports. Don't buy visibility data for v1.
12. **TL and factoring [our call]:** keep a payee and NOA register by MC number, match loads billed by two payees, and flag remit-to changes. This is worth most before payment.
13. **ERP [our call]:**
    - publish the CSV template from §4.4, with a mapping step;
    - choose Apideck if Acumatica or QuickBooks Desktop customers matter, Merge for cloud-only;
    - for QuickBooks Online, Intuit's free Builder tier (500,000 read credits a month) suffices for a pilot.
14. **Notifications [our call]:** SES or Postmark for email; Slack webhooks; Teams via Workflows (the old connectors are gone); SMS optional.
15. **Security [our call]:**
    - aim for SOC 2 Type I before scaling mid-market sales, then Type II;
    - write the SIG Lite answers in advance;
    - buy cyber insurance;
    - use AI providers under commercial terms with no training, ZDR on request, named as sub-processors;
    - keep consignee names out of model prompts where the check doesn't need them.

---

## 9. Sources

| ID | Title / publisher | Date on page | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AL01 | Postmark, Pricing | none | https://postmarkapp.com/pricing | extraction | Plans, overage, inbound by plan |
| N-AL02 | Postmark, "Inbound domain forwarding" | none | https://postmarkapp.com/developer/user-guide/inbound/inbound-domain-forwarding | extraction | MX setup |
| N-AL03 | Amazon SES pricing | none | https://aws.amazon.com/ses/pricing/ | extraction | Receiving, sending, Mail Manager prices |
| N-AL04 | AWS, "Contents of notifications for Amazon SES email receiving" | none | https://docs.aws.amazon.com/ses/latest/dg/receiving-email-notifications-contents.html | full page | Verdict fields; raw content |
| N-AL05 | Twilio SendGrid, "Setting up the Inbound Parse Webhook" | none | https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/setting-up-the-inbound-parse-webhook | extraction | 30 MB; SPF/dkim fields; raw MIME |
| N-AL06 | Mailgun, Pricing | none | https://www.mailgun.com/pricing/ | extraction | Plans; inbound routes |
| N-AL07 | Cloudflare, Email Routing limits | none | https://developers.cloudflare.com/email-routing/limits/ | extraction | 25 MiB; rule and destination limits |
| N-AL08 | Ramp Help Center, "Bill Pay AP email forwarding" | none | https://support.ramp.com/bill-pay-ap-email-forwarding | extraction | Address format, file types, split, filters |
| N-AL09 | Dext Help, "Set up email forwarding rules to Dext" | 2026-07-29 | https://help.dext.com/en/articles/416678-set-up-email-forwarding-rules-to-dext | extraction | @dext.cc / @multiple.dext.cc; Gmail verification |
| N-AL10 | BILL, "Set up, use, and maintain your Inbox" | — | https://vendorpayhelp.bill.com/hc/en-us/articles/360006991712-Set-up-use-and-maintain-your-Inbox | snippet (403) | Inbox address format |
| N-AL11 | Stampli, "Emailing Invoices to Stampli" | — | https://help.stampli.com/en/articles/5581626-emailing-invoices-to-stampli | snippet (401) | PDF only, 100 files, 50 MB |
| N-AL12 | Expensent / Receiptor guides to Hubdoc | 2026 | https://www.expensent.com/guides/email-receipts-to-hubdoc | snippet | Hubdoc address |
| N-AL13 | Microsoft Learn, "Control external email forwarding and fix 5.7.520 errors" | 2026-08-18 | https://learn.microsoft.com/en-us/defender-office-365/outbound-spam-policies-external-email-forwarding | full page (re-checked) | Default off since 2021; NDR text |
| N-AL14 | Google, "Restricted scope verification" | updated 2026-08-19 | https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification | extraction (re-checked) | CASA, 12-month cycle, exemptions |
| N-AL15 | Google, Gmail API scopes | none | https://developers.google.com/workspace/gmail/api/auth/scopes | extraction | Restricted scopes |
| N-AL16 | TAC Security, "ESOF AppSec ADA CASA FAQs" | none | https://tacsecurity.com/esof-appsec-ada-casa-faqs/ | extraction | CASA prices and timing |
| N-AL17 | Microsoft Graph permissions reference | none | https://learn.microsoft.com/en-us/graph/permissions-reference | extraction | Mail.Read consent |
| N-AL18 | Microsoft Learn, "RBAC for Applications in Exchange Online" | 2025-11-25; updated 2026-08-21 | https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac | full page | Scoping Mail.Read |
| N-AL19 | ODFL, "Invoices & Claims" | none | https://www.odfl.com/us/en/resources/invoices-claims.html | extraction | Email invoices, e-statements |
| N-AL20 | FedEx Freight Billing Online; fedex.com LTL billing page | none | https://www.fedexfreight.com/en-us/manage-account/billing ; https://www.fedex.com/en-us/billing-online/ltl-freight.html | extraction | Notifications, disputes, users |
| N-AL21 | Saia FAQ | — | https://www.saia.com/faq | snippet (empty fetch) | PDF invoice emails |
| N-AL22 | ODFL, "Shipping API Integration Services" | versions to 2026-09-08 | https://www.odfl.com/WebServiceSignup | extraction | API list; no invoice API |
| N-AL23 | ODFL, "Rating API Development Guide" v1.0 | 2026-08-21 | https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Rate%20Estimate%20API%20Development%20Guide.pdf | PDF pages read | Auth, billToAccount, integrator fields, pickupDate |
| N-AL24 | XPO, "XPO API" help centre | none | https://www.xpo.com/help-center/integration-with-customer-systems/api/ | extraction | Six APIs; signup; BOL listing |
| N-AL25 | XPO, "API Implementation Guide — Imaging" v1.0 | 2019-09-04 | https://www.xpo.com/cdn/files/s1/XPO_API_Imaging_Guide.pdf | PDF pages read | Image types, formats, TIFF default |
| N-AL26 | Estes, "Freight Shipping APIs" | none | https://www.estes-express.com/resources/digital-services/api/ | extraction | 14 image types; APIs |
| N-AL27 | Estes, API Developer Portal | none | https://developer.estes-express.com/ | extraction | Auth; Invoice Subscription |
| N-AL28 | Estes, "Electronic Data Interchange (EDI)" | none | https://www.estes-express.com/resources/digital-services/edi | extraction | EDI sets; contact |
| N-AL29 | Saia, "Web Services: Get Images" | none | https://www.saiasecure.com/irsec/n_GetImage.asp | extraction | BOL/POD/WGT; auth; formats |
| N-AL30 | Saia developer portal; 3PL support guide | — | https://saiaprodapi.developer.azure-api.net/ ; https://3plsupport.com/docs/3pl-university-guides/integrations/carrier-integrations/saia/how-to-get-credentials/ | snippet | Subscription key; rates |
| N-AL31 | ArcBest, "Shipping APIs" | none | https://arcb.com/technology/shippers/API | extraction | API list |
| N-AL32 | ArcBest support, "Document Retrieval"; "API Access" | 2018-02-08 | https://support.arcb.com/en/articles/1509576-document-retrieval ; https://support.arcb.com/en/articles/2851223-api-access | extraction; snippet | Document types; API ID |
| N-AL33 | FedEx Developer, "Freight LTL API Documentation" | none | https://developer.fedex.com/api/en-us/catalog/ltl-freight/docs.html | extraction | Operations; past-date note |
| N-AL34 | R+L Carriers Developer, "Rate Quote" | none | https://technology.rlcarriers.com/api-documentation/rate-quote/ | extraction | Customer-specific quotes; PickupDate |
| N-AL35 | R+L, "EDI Trading Partner Profile" | undated | https://rl-cdn.com/docs/rlc/edi/trading_partner_profile.pdf | PDF pages read | Third-party payor, transmission, 210 scope, images |
| N-AL36 | R+L API tools list; letter-of-authority snippet | — | https://www.rlcarriers.com/freight/shipping-software/api | snippet | API list; LOA |
| N-AL37 | TForce Freight Developer Portal | none | https://developer.tforcefreight.com/ | extraction | APIs; Invoicing "Coming Soon" |
| N-AL38 | SEFL, "Web Connect" | none | https://www.sefl.com/seflWebsite/technology/webConnect.jsp | extraction | Services; "inexpensive" |
| N-AL39 | Averitt, "API" | none | https://www.averitt.com/technology/api | extraction | API list; access |
| N-AL40 | AAA Cooper / Central Transport web services (p44 support, nopCommerce, Quote Factory pages) | — | https://support.p-44.com/hc/en-us/articles/4408763925787-AAA-Cooper-Transportation-AACT ; https://www.nopcommerce.com/en/central-transport | snippet | Service lists |
| N-AL41 | project44, "LTL: Image Retrieval" | none | https://developers.project44.com/api-reference/api-docs/ltl:-image-retrieval | extraction | Types, inputs, formats |
| N-AL42 | project44 TL tracking pages | — | https://developers.project44.com/api-reference/api-docs/tl:-tracking | snippet | Arrival/departure events |
| N-AL43 | SMC3, "LTL APIs - Shippers"; CarrierConnect XL snippets | none | https://www.smc3.com/ltl-api-shippers.htm | extraction; snippet | Documents |
| N-AL44 | SMC3, "SMC³ Updates 2026 Pricing" | 2025-09-23 | https://www.smc3.com/press-releases-20250923.htm | extraction | +3% |
| N-AL45 | Nexus VAN, Pricing | none | https://www.nexusvan.com/pricing | extraction | VAN tiers per KC |
| N-AL46 | Orderful, Pricing | "2025" | https://www.orderful.com/pricing | extraction | Per trading partner |
| N-AL47 | Stedi, Pricing | none | https://www.stedi.com/pricing | extraction | Healthcare-only page |
| N-AL48 | Commport; Boldvan; Capterra (Kleinschmidt) | 2026 | https://www.commport.com/per-transaction-vs-kilocharacter-edi-pricing/ ; https://www.capterra.com/p/183675/Kleinschmidt-EDI-Integration/ | snippet | Typical VAN fees |
| N-AL49 | Cornell LII, UCC § 9-406 | — | https://www.law.cornell.edu/ucc/9/9-406 | extraction (re-checked) | (a), (c), (d) |
| N-AL50 | FreightWaves Checkpoint; Harter Secrest & Emery; TCEast | 2026-05-03 (TCEast) | https://www.freightwaves.com/checkpoint/notice-of-assignment-in-factoring/ ; https://hselaw.com/news-and-information/legalcurrents/dont-pay-that-invoice-twice-how-to-handle-ucc-%C2%A79-406-notices-of-assignment/ | snippet | NOA practice; pay-twice risk |
| N-AL51 | Merge, Pricing | none | https://www.merge.dev/pricing | extraction | Launch tier |
| N-AL52 | Merge, Accounting API | none | https://www.merge.dev/categories/accounting-api | extraction | Connector list |
| N-AL53 | Apideck, Pricing | none | https://www.apideck.com/pricing | extraction | Plans |
| N-AL54 | Apideck, Accounting API | none | https://www.apideck.com/accounting-api | extraction | Connector list |
| N-AL55 | Codat docs, accounting integrations; Codat pricing snippets | — | https://docs.codat.io/integrations/accounting/overview | extraction; snippet | Connector list; price claims |
| N-AL56 | Rutter, Pricing | none | https://www.rutter.com/pricing | extraction | Contact sales |
| N-AL57 | Intuit, "Intuit App Partner Program Guide" | v1.2, 03.2026 | https://static.developer.intuit.com/resources/Intuit_App_Partner_Program_Guide.pdf | PDF text | Tiers; CorePlus metering |
| N-AL58 | Intuit Developer, QuickBooks Online entities | — | https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api | snippet | Bill, BillPayment, Attachable |
| N-AL59 | Oracle NetSuite help "attach / detach"; NetSuite Professionals | — | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N3481947.html | snippet | vendorBill; attachments |
| N-AL60 | Microsoft Learn, Business Central API (v2.0) | 2026-08-10 | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/ | full page | Enabled by default; terms |
| N-AL61 | ERP Research "ERP Market Share 2026"; Anchor Group; MSDynamicsWorld | 2026 | https://www.erpresearch.com/erp-market-share ; https://www.anchorgroup.tech/blog/wholesale-distribution-erp-statistics | snippet | Market claims |
| N-AL62 | EIA, Open Data; "Copyrights and Reuse" | none | https://www.eia.gov/opendata/ ; https://www.eia.gov/about/copyrights_reuse.php | extraction | Key, free, bulk, public domain |
| N-AL63 | NMFTA, SCAC product descriptions; NMFTA Store | none | https://nmfta.org/standard-carrier-alpha-code-scac-product-descriptions/ ; https://store.nmfta.org/Products/ProductDetail?SKU=SCACONLINE ; https://store.nmfta.org/category/scaccdroms | extraction; API-price snippet | Prices; licence notice |
| N-AL64 | NMFTA ClassIT+ API pages | — | https://classitplus.nmfta.org/products/api | snippet | Licence agreements |
| N-AL65 | Internet Archive availability API (7 queries) | 2026-10-03 | https://archive.org/wayback/available?url=… | JSON | Closest captures |
| N-AL66 | ODFL, "Fuel Surcharge Rates – Current & History" | period from 2026-10-07 shown | https://www.odfl.com/us/en/resources/fuel-surcharge.html | extraction | History tool; 128-CC link |
| N-AL67 | ODFL, Tariff ODFL 128-AA | effective 2022-06-01 | https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/ODFL%20128%20AA.PDF | PDF text | Old tariff online; Monday index, Wednesday change |
| N-AL68 | ArcBest, ABF 111-AQ; ABF fuel page URL | last revised 2023-01-10 | https://arcb.com/sites/default/files/pdf/ABF111-AQ01-10-2023.pdf ; https://arcb.com/abf-freight/resources/fuel-surcharge.html | PDF text; search | Old rules tariff online |
| N-AL69 | Google Maps Platform pricing | none | https://developers.google.com/maps/billing-and-pricing/pricing | extraction | Routes prices; no truck SKU |
| N-AL70 | TrustRadius / Capterra (PC*Miler); Placematic (HERE); MileMaker search | 2026 | https://www.trustradius.com/products/trimble-maps-pc-miler/pricing ; https://placematic.com/here-location-services/here-pricing/ | snippet | Mileage prices |
| N-AL71 | Smarty, US address verification pricing | none | https://www.smarty.com/pricing/us-address-verification | extraction | $552 for 12K; RDI |
| N-AL72 | USPS APIs, Terms and Conditions | updated 2026-01-22 | https://developers.usps.com/terms-and-conditions | extraction | Use limited to USPS shipping |
| N-AL73 | TT News "Detention Data Drives…"; visibility listings | 2026 | https://www.ttnews.com/articles/detention-data-drives-decisions | snippet | Detention data practice |
| N-AL74 | Slack, "Sending messages using incoming webhooks" | none | https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks | extraction | Limitations |
| N-AL75 | Microsoft 365 Developer Blog, "Retirement of Office 365 connectors within Microsoft Teams" | updated 2026-04-14 | https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/ | extraction | Shut-off dates |
| N-AL76 | Twilio, US SMS pricing | "September 2026" | https://www.twilio.com/en-us/sms/pricing/us | extraction | Per-segment and carrier fees |
| N-AL77 | Anthropic, "API and data retention" | current | https://platform.claude.com/docs/en/manage-claude/api-and-data-retention | full page | ZDR scope, eligibility, Covered Models |
| N-AL78 | Anthropic Privacy Center, "How long do you store my organization's data?" | updated 2026-07-01 | https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data | extraction | 30-day deletion; exceptions |
| N-AL79 | Anthropic, Commercial Terms of Service | effective 2025-06-17 | https://www.anthropic.com/legal/commercial-terms | extraction | No training; confidentiality |
| N-AL80 | Anthropic Claude API skill bundle (local copy of official docs) | cached 2026-09-25 | local: claude-api/shared/models.md, error-codes.md | read | Covered Models need 30-day retention |
| N-AL81 | OpenAI, "Data controls in the OpenAI platform" | none | https://developers.openai.com/api/docs/guides/your-data | extraction | Training, retention, ZDR |
| N-AL82 | Google, Gemini API Additional Terms | effective 2026-03-23 | https://ai.google.dev/gemini-api/terms | extraction | Paid vs unpaid |
| N-AL83 | AWS, Bedrock "Data protection" and "Data retention" | 2026 | https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html | full page | Provider access; retention modes |
| N-AL84 | Microsoft Learn, "Data, privacy, and security for Foundry Models sold by Azure" | 2026-05-18; updated 2026-06-05 | https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy | full page | No training; abuse monitoring |
| N-AL85 | SOC 2 / SIG / cyber-insurance explainers (Secureframe, UpGuard, Boulay and others) | 2025-26 | https://secureframe.com/blog/soc-2-type-ii ; https://www.upguard.com/blog/sig-questionnaire | snippet | Buyer expectations |
| N-AL86 | Navix, "Top Freight Audit Companies Compared (2026)" | 2026 | https://www.navix.io/freight-audit-companies/ | snippet | Peers' SOC claims |
| Local | Checks AC, T, Z, AA, Y (N-AC…, N-T…, N-Z…, N-AA…, N-Y…) | 2026-09 | `research/s5_check_{AC,T,Z,AA,Y}_*.md` | read | Context; not redone |

---

## 10. Could not access, or not found

**Blocked or failed:**
1. BILL's inbox help (HTTP 403) and Stampli's help article (401). Snippets only.
2. Saia's web-integration page and FAQ came back empty. ABF's API docs need sign-in. R+L's API index returned 404.
3. Codat pricing (404), OpenAI's enterprise-privacy page (403) and NMFTA's "SCAC Licensing" help article (403).
4. Vertex AI's data-governance page didn't render its content, so Vertex retention and ZDR are not verified.
5. web.archive.org (the CDX API and capture pages) is unreachable from the fetch tool. Only the archive.org availability API worked, so captures couldn't be counted or inspected.

**Not established or not found:**
6. Which LTL carriers email a link instead of a PDF.
7. Carriers' API fees, rate limits and terms of use, for all 12. XPO points to its help centre, which was not read.
8. Invoice-data APIs at ODFL, XPO, Saia, ABF and FedEx Freight: none found. The AAA Cooper and Central Transport details are snippets only.
9. Minimum volumes for EDI, and whether carriers set up EDI for small accounts.
10. Not checked: SPS Commerce prices and AS2 software. The Kleinschmidt figure is from a Capterra snippet only.
11. A neutral ERP market-share survey for manufacturers and distributors with 20-499 staff (two searches).
12. API docs for Epicor, Infor, SAP Business One, Sage 100/300, Acumatica, Global Shop, JobBOSS, Plex and DELMIAworks were not fetched (budget). Those rows are *assumed*.
13. SMC3 prices, and its licence for re-rating on behalf of clients: not published.
14. ClassIT+ third-party or multi-customer terms: not public.
15. Not checked at source: the SCAC web-service price, PC*Miler, HERE, and other CASA labs.
16. Rand McNally MileMaker's price.
17. Detention export prices at project44, FourKites, MacroPoint and Trucker Tools.
18. Not on the pages read: Postmark's inbound size limit and authentication fields; Slack's webhook rate limit and plan requirement. Twilio's 10DLC registration fees are on a separate page, which was not fetched.
19. Not checked, from memory only: Microsoft publisher verification and user-consent defaults; the Google Workspace admin switch for auto-forwarding.

**Skipped by rule:**
20. The EIA API key was not registered (rules). The keyless bulk and XLS files are noted instead.
21. Wayback gaps: no capture was returned for XPO near 2025-07, and the closest ODFL capture to 2024-07 is 2024-12-09.
