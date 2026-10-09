# S5 check U: the retailers' documented position, the buyer count and the 2018 gap (C-19)

- **What this is:** desk research for S5 ("Validate with primary evidence") in run 01, on card **C-19**, "Meeting retailers' on-time-in-full rules and disputing the fines and deductions, for small and mid-sized suppliers to big-box retailers, handled today by their carriers and brokers plus in-house deductions staff."
  - **The big-box retailers are a counterparty-only side** (rule C21, `submarket_selection.md` S5). They set the rules and deduct first, and we would never sell to them. C21 covers such a side with its **documented position** (published rules, supplier manuals, dispute windows) plus 1-2 interviews with people who work against it daily. **This file is that documented position.**
  - It also covers the two gaps S4 flagged (`4_scorecard.md` §7.1): "Is the 2018 gap still open, or has SPS's SupplyPike closed it? And how many small and mid-sized suppliers are there?"
  - It builds on check S §2.4 (`s3b_check_S_facility_fleet_trade_jobs.md`) and does not repeat it. Load-bearing items from check S were re-read where they could be.
- **Not covered here:**
  - the interviews themselves (§6 lists who and what to ask);
  - the supplier side, which could buy from us and gets the full S5 treatment (5 interviews, commitments, a savings assessment);
  - any re-score. §7 says which rows the evidence bears on; the coordinator makes the calls.
- **Date:** 2026-09-16.
- **Status:** input to S5; **it decides nothing**.
- **Labels:**
  - *verified*: read at the source (a quote from the page, a value from a downloaded file or an official filing).
  - *assumed*: a search snippet, a secondary summary, a vendor claim, memory, or a blocked page. **Vendor figures are always *assumed*,** even when read on the vendor's own page. Almost every retailer rule below is *assumed*, because the retailers publish their rules only behind supplier logins; **Kroger is the exception** (a public policy PDF).
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
  - **Affiliation flags.** An association survey counts as a source, but it is always shown with who runs it:
    - CRF, the Credit Research Foundation (credit managers). Its deduction surveys are run with Attain Consulting Group; its 2023 survey also names Carixa, IAB LLC and RVCF as partners. **Carixa sells deduction software.**
    - NACM, the National Association of Credit Management (credit managers).
    - GS1 US (the barcode standards body; members are firms that license barcodes).
- **New sources** are N-U01 to N-U40 (§8). All were accessed on 2026-09-16. Downloads are in the session scratchpad (`…/scratchpad/checkU/`).

**Words used here** (others are in check S):
- **OTIF (on time, in full):** a retailer's delivery rule, with fines for late or short deliveries. Target calls its version **OTFR** (on-time fill rate) and, since 2025, the **Perfect Order** programme.
- **MABD:** Walmart's "must arrive by date". **ORAD:** Kroger's "original requested arrival date".
- **COGS:** cost of goods sold, i.e. the retailer's purchase cost of the goods. "3% of COGS" means 3% of what the retailer pays the supplier for the late or short goods.
- **Prepaid vs collect:** on a **prepaid** order the supplier books and pays the carrier, and is measured on arrival at the retailer's distribution centre (DC). On a **collect** order the retailer books the carrier, and the supplier is measured on being ready for pickup.
- **Deduction / chargeback / offset:** money a retailer keeps back from what it pays the supplier. **AP** (accounts payable) deductions come off the retailer's payments; an **AR** (accounts receivable) chargeback is billed to the supplier as an invoice first.
- **Shortage claim:** a deduction for units the retailer says it did not receive.
- **Post-audit claim:** a deduction raised months or years later by the retailer's own or a hired audit firm.
- **EDI messages:** 856 = advance ship notice (**ASN**); 753 = request for routing instructions; 812 = credit/debit adjustment; 820 = remittance advice.
- **POD / BOL:** proof of delivery / bill of lading.
- **1P / 3P:** first-party vendors sell wholesale *to* Amazon (Vendor Central); third-party sellers sell *on* Amazon's marketplace.
- **DSD:** direct store delivery (the supplier delivers to stores, not to a DC; mostly outside OTIF).
- **Portals named below:** HighRadius (Walmart's AR portal), APDP (Walmart's Accounts Payable Disputes Portal in Retail Link), EIPP (Walmart's invoice portal used for SQEP), Synergy in Partners Online (Target), SPM in Supplier Hub (Home Depot's Supplier Performance Management), VCS in Vendor Gateway (Lowe's Vendor Compliance System), Lavante (Kroger's invoice-research site), Vendor Central (Amazon).
- **SQEP:** Walmart's Supplier Quality Excellence Program, which charges for inbound quality defects (ASN, labels, loads).

---

## 1. Summary table

| Question | Desk answer | Label | Sources |
|---|---|---|---|
| **What do the retailers fine for, and how much?** | Late and short deliveries, plus ASN, label and routing defects. **3% of the cost of the affected goods is the common OTIF rate** (Walmart, Target, Kroger). Home Depot and Lowe's use **10% offsets** plus flat fees ($250-1,000 per ASN or routing breach). Amazon charges 2-6% of cost for ASN accuracy bands and 3-10% for late or cancelled POs. Costco assesses case by case | Kroger *verified*; the rest *assumed* (vendor and 3PL guides) | N-U20, N-E26, N-U12, N-U16, N-U17, N-U18, N-U23 |
| **How is the fine collected?** | **Every retailer takes it out of what it pays the supplier.** Walmart bills OTIF fines as an invoice first and deducts them if unpaid. Kroger: "Kroger will deduct the amount(s) due from any outstanding invoice" | Kroger *verified*; others *assumed* | N-U20, N-U07, N-U16, N-U19, N-U23 |
| **How long does a supplier have to dispute?** | **From 48 business hours to 24 months, and the compliance fines have the short windows:** Home Depot about 4 weeks; Lowe's the 2nd-16th of each month; Walmart AP chargebacks 15-30 days; Amazon chargebacks 30 days. Longer: Kroger 180 days; Walmart SQEP 13 months, shortages 12 months, general 24 months; Target 18 months (collect orders 9 months); Amazon shortages 2 years. **Walmart's OTIF window is unsettled** (vendors say 30 days, or no fixed window) | Kroger *verified*; others *assumed* | §2 |
| **What evidence wins?** | Signed BOL and POD, carrier and DC check-in or gate times, dock-appointment confirmations, ASNs, TMS screenshots. **Two shifts:** Amazon "no longer requires suppliers to provide a POD" and prefers unit-level receipt data; Walmart's APDP does not accept carrier-generated delivery reports | *assumed* | N-U10, N-U17, N-U24, N-U08 |
| **Changes since 2024** | **Mostly tightening.** Kroger raised its on-time bar 90% → 93% and added fee schedules (2025); Target added three Perfect Order metrics (May 2025) and fines for repeat disputes (by Nov 2025); Amazon capped shortage disputes at 2 years and ended bulk disputes (2025). **Easing:** Walmart's targets (Feb 2024), Target's fine rate 5% → 3% (Aug 2024), Walmart's prepaid consolidation option (May 2026) | mixed | §3 |
| **How many buyers?** | **About 15,000 to 55,000 small and mid-sized suppliers sell direct to big-box retailers; central about 29,000** [our calc on [our call] factors]. Anchor: Walmart publishes 31,196 US supplier records (Dun & Bradstreet, FYE 2025), and says more than 60% are small businesses | anchor *verified*; factors **[our call]** | N-U03, N-U04, N-U01, N-D04 |
| **What that does to Cohen** | The central count rounds to **10,000**, so C-19's Cohen score **stays 1.00**. It reaches 10.00 only above 31,623, which is the upper ~42% of the range [our calc] | **[our calc]** | §4.4 |
| **Is the 2018 gap still open?** | **Open, but narrowing.** Among firms with sales of $500M or less, the share using **no** third-party deduction technology fell from **70% (2018) to 65% (2021) to 55% (2023)** (CRF surveys, as shown on a vendor's slide). SPS bought about 550 1P revenue-recovery customers in 2024-25, about **1.2% of its own 46,900 1P customers** [our calc]. No dominance | survey *assumed* (CRF flag; vendor slide); SPS counts *verified* (10-K) | N-U28, N-U01 |
| **Who works against retailers daily?** | Contingency recovery firms (e.g. HRG in Bentonville, Vendormint, Smyyth, Woodridge, STAT, ClearChain); retail-compliance teams at 3PLs; retail consultancies (8th & Walton); vendors' managed-service analysts; former retailer-side auditors (Kroger routes billing correspondence to PRGX). They gather at CRF forums and NACM's Credit Congress | *assumed* (vendor pages, snippets); PRGX *verified* | §6 |

---

## 2. The retailers' rules, compared

**Access.** Walmart (Retail Link / Supplier One), Target (Partners Online), Home Depot (Supplier Hub), Lowe's (Vendor Gateway), Costco and Amazon (Vendor Central) publish their compliance manuals only behind supplier logins, which this check did not use. Their rules below come from vendor, 3PL and consultancy guides (*assumed*), cross-checked where two sources agree. **Kroger's policy is public and was read in full** (*verified*).

### 2.1 What is measured, the fine, and prepaid vs collect

| Retailer | What is measured (target) | Fine or chargeback | Prepaid vs collect | Label |
|---|---|---|---|---|
| **Walmart** | OTIF per case against the MABD window: on time, and in full at 95% of ordered cases. SQEP separately measures inbound quality (PO accuracy, ASN, labels, loads) | OTIF: **3% of COGS on non-compliant cases**, billed **quarterly** since Feb 2024; a month's total under $1,000 was waived (2024). SQEP: **$200 per PO plus $1 per non-compliant case** | **Prepaid: 90%** of cases delivered on time at the DC. **Collect: 98%** ready for pickup by the appointment time. In full 95% for both | *assumed* (N-E26 re-read, N-F37, N-S12, N-U09) |
| **Target** | On time 100% within the window; **Fill Rate Original**: at least 95% of the items on the original order, measured by item (since 4 Aug 2024). **Perfect Order** (since 4 May 2025): ASN availability, ASN accuracy, scannable barcodes | On time and fill rate: **3% of COGS** (down from 5% in Q3 2024). ASN and barcode: **$0.75 per carton**, $100 minimum | **Collect:** ready for pickup within the window booked in Target's routing system (entry by 11:00 CT two business days before). **Prepaid:** received within the in-yard delivery window, one day either side (2024) | *assumed* (N-U12, N-U14, N-S12, N-U15) |
| **Home Depot** | Monthly scorecard per merchandise vendor (SPM): **fill rate 98%, on time 90%, ASN timeliness 100%**, routing compliance, data quality (DQC), and "V codes" for vendor-caused carrier delays | Fill rate: **10% offset** on items not received. On time: **10% of items** on the late shipment. Missing ASN **$1,000**, late ASN $250, wrong TMS ship ID $100. Routing violation **$250**. Offsets apply only when the month's average falls below the threshold | **Prepaid:** received on or before the expected delivery date. **Collect:** marked "ready to ship" in Home Depot's TMS by 11:00 local time two days before pickup | *assumed* (N-U17, N-U16) |
| **Lowe's** | Vendor Performance in VCS: **fill rate 98%, on time 95%**, ASN, labels, invoices | Fill rate: **10% offset** on the value not received. On time: **10% of the PO value**. ASN $250 per ASN; invoice errors about $50; label defects about $10 | Mostly **collect**. Collect: measured against the ready-to-ship date sent on EDI 753, with a one-day grace. Prepaid: the date the load is received at the DC | *assumed* (N-U18, N-U19; one undated 3PL page) |
| **Costco** | Depot appointments (no walk-ins), ASN before the truck arrives, pallet and SSCC label rules | Charges are "more often assessed individually rather than as a standardized percentage" (vendor guide). One snippet: $500 administrative fine plus redelivery for a late or turned-away truck. **Fee schedule is behind the supplier login** | Collect by default (Costco routes) | *assumed* (N-U22) |
| **Kroger** | **ORAD on-time** ("a PO is gated-in at the applicable Kroger DC on the ORAD"): **93%** per 4-week period from 1 Jan 2025 (was 90%). **Case fill 95%.** Arrival within 30 minutes of the appointment. From 2025, live location and temperature data on inbound loads | **3% of the invoiced amount** on each vendor-caused late PO, waived for a period at 93% or better. **3% of the missing items' value** below 95% fill. $200 per shipment late by more than 30 minutes or with no appointment. **$100 per PO (cap $10,000)** unless 90% of POs send location data (from 1 May 2025) and temperature data (from 1 Nov 2025) every 15 minutes. $100-1,000 for label, pack, pallet and paperwork faults. Carrier detention and truck-order-not-used fees are passed back | **Vendor-managed (prepaid):** the vendor books DC appointments in time to meet ORAD. **Kroger-managed (collect):** the vendor must offer pickup appointments in time and be ready; "many of these fees will not apply if Kroger manages your inbound lanes" | ***verified*** (N-U20) |
| **Amazon 1P** | PO on-time accuracy (ship or delivery window), ASN accuracy, carton, prep and label rules; **shortage claims** (units invoiced but not matched to receipts) | ASN accuracy: **2% / 4% / 6% of cost** at compliance above 95% / 70-95% / below 70%. PO on-time: **3% of cost** for units outside the window; **10%** for shipments auto-cancelled. Shortage: the invoiced value not received | The window measured differs: ship window for Amazon-collected freight, delivery window for prepaid (as the guides describe it) | *assumed* (N-U23, N-U24) |

### 2.2 How the fine is collected, the dispute window, the portal and the evidence

| Retailer | How collected | Dispute window | Portal / process | Evidence accepted | Label |
|---|---|---|---|---|---|
| **Walmart** | OTIF: "Walmart issues a chargeback in the form of an invoice"; if unpaid, "Walmart will automatically deduct the amount from future payments". Fines issued about 5 weeks after quarter end. AP deductions come straight off invoice payments | **OTIF: unsettled.** "30-day window … before forfeiture" (ClearChain; iNymbus says 30 days) against SPS's advice to "wait to dispute between 60-150 days after a fine has been invoiced" (2023). **AP chargebacks: 15-30 days from posting. Shortages: 12 months from invoice date. General invoice disputes: up to 2 years. SQEP: 13 months** from the fine | OTIF: HighRadius (AR). AP deductions: APDP in Retail Link. SQEP: EIPP. Disputes take about 30-45 days to resolve | "Signed BOL with carrier timestamp, DC receiving stamp, dock-appointment confirmation, and the original PO" (ClearChain). **APDP does not accept carrier-generated delivery reports** (Glimpse). HighRadius takes up to 10 attachments | *assumed* (N-U06, N-U07, N-U08, N-U09, N-U10) |
| **Target** | Deducted as a chargeback, after a violation "lifecycle" of about two weeks in which an exemption can be requested (snippet) | "Target will not research claims dated more than **18 months** from the document date." Collect shipments "MUST be submitted within **9 months** of the shipping date." **5 business days** to add missing documents | Synergy, reached through Partners Online (POL). **Target "will begin charging fines for any deduction disputed for a fifth time or more"** | Prepaid: a valid POD (signed BOL plus Target's delivery receipt). Collect: proof of shipment (carrier-signed BOL) | *assumed* (N-U13, N-U15) |
| **Home Depot** | "Financial offsets are calculated per metric and deducted at the Payables Vendor level." Issued in the first week of the month for the previous month | **SPM offsets: about 4 weeks** (opens the second Wednesday of the fiscal month, closes the second Tuesday of the next). **V codes: 48 business hours.** DQC: by the end of the following fiscal month. "Disputes submitted after the deadline are automatically denied." Separately, **12 months from invoice date** for invoice disputes (type not stated) | SPM app in Supplier Hub; Vendor PlanEx (V codes); a DQC dispute form | BOL copies, TMS screenshots, ASN copies, label or manifest documents | *assumed* (N-U16, N-U17, N-S12) |
| **Lowe's** | "That month's fines will be deducted from the invoice" once the window passes | **2nd-16th of each month**, for the previous month's fines (about 15 days) | "Rebuttals" inside the VCS app, with a reason code | Reason code plus supporting documents | *assumed* (N-U19) |
| **Costco** | Deducted from the invoice (snippet) | **Not published.** One generic snippet: "30 to 60 days" | Not found | Not found | *assumed* (N-U22) |
| **Kroger** | "Kroger will deduct the amount(s) due from any outstanding invoice. If there are monies due to Kroger that have not been deducted within sixty (60) days, Vendor must pay by check" | **No window is named for compliance fees.** Billing inquiries: "Kroger will only research invoices from 60 – 180 days past the original invoice date. Any billing inquiries must be resolved within **180 days** of the original invoice date." Advice messages on payments: 180 days | Lavante, Kroger's invoice-research site; correspondence is handled by PRGX, a recovery-audit firm | "a copy of the original invoice accompanied by verified proof of delivery" (policy); a POD for late-shipment disputes (SPS wiki) | ***verified*** (N-U20); wiki *assumed* (N-U21) |
| **Amazon 1P** | Deducted from remittances | **Chargebacks: 30 days**, and a denied dispute can be reopened once. **Shortages:** first dispute "within **30 days** of the invoice due date"; lookback capped at **2 years** of invoices (North America, mid-2025; previously 5 years); line by line only (bulk disputes ended by Aug 2025); a re-dispute is allowed for partly approved or denied claims | Vendor Central (Payments → Invoices → shortages; chargeback disputes) | "Amazon no longer requires suppliers to provide a POD. Amazon prefers data directly related to the unit-level receipt": ASNs, EAN codes, carton images; signed BOLs still help | *assumed* (N-U23, N-U24, N-U25, N-U26) |

### 2.3 Notes, retailer by retailer

**Walmart**
- **Targets.** The 90% / 98% / 95% goals took effect on 1 Feb 2024, replacing a single 98% OTIF goal (N-E26 re-read: "Last Updated February 5, 2024"; N-S13). *Assumed* (vendor, trade press).
  - Two vendor pages still describe a single "98 percent OTIF" target (N-U11). They are treated as out of date.
  - No Walmart OTIF target change after Feb 2024 was found.
- **Collection.** OTIF fines are an AR invoice in HighRadius, not an AP deduction, and are taken off future payments if unpaid (N-U07, SPS, updated 6 May 2024, *assumed*). **For measurement this matters (F3):** a recovered OTIF fine shows up as an approved dispute in HighRadius, not as a line on the remittance.
- **Dispute window.** The one conflict this check could not settle.
  - Short-window reading: 30 days (N-U10 ClearChain; N-U09 iNymbus, 25 Aug 2026).
  - Long-window reading: SPS (28 Aug 2023) advises waiting 60-150 days after invoicing before disputing in-full fines, "to allow more time for POs to be received properly" (N-U06).
  - Glimpse (2026) separates the two systems: OTIF chargebacks go through HighRadius, not APDP; the "15 to 30 days from posting date" window is for **AP chargebacks** in APDP; "Miss the AP chargeback window and the money is gone for good" (N-U08).
  - **[our call]:** the window has to be asked in the C21 interview (§6.2).
- **SQEP.** Launched 15 Sep 2020; "$200 per PO plus $1 per non-compliant case"; disputes through EIPP within 13 months (N-U09, *assumed*).
- **Other windows.** Walmart's returns deductions (code 98) "are no longer visible or disputable in APDP" since July 2023 (N-U08, *assumed*).
- **New in 2026.** Walmart's Prepaid Consolidation Program (26 May 2026): a Walmart-managed consolidation option; "Since it's managed by Walmart, there's no need for suppliers to change their prepaid freight terms" (N-U05, *verified*, company page). It is a prevention route for prepaid suppliers, not a rule.

**Target**
- **Fine rate: conflict resolved toward 3%.** Check S held two vendor claims (3% per N-S12; 5% with a $150 minimum per N-S40).
  - SPS's help centre (13 Mar 2025) lists "3% COGs" for fill rate and on time (N-U12).
  - WarehouseQuote's 2026 guide lists "3% COGS" for all four OTFR metrics (N-U14).
  - N-S12 (Dec 2024) dates the cut from 5% to 3% to Q3 2024.
  - **Reading [our call]:** 3% is current; the 5% figure predates Aug 2024. Still *assumed*.
- **Perfect Order (4 May 2025).** ASN availability moved from "3% COGs of all goods received without an ASN" to "$0.75 per carton"; ASN accuracy and barcode accuracy were added at $0.75 per carton (N-U12). The $100 minimum is from search summaries only (N-U15).
- **Disputes.** Dispute codes include A030 carton shortage, A034 unit shortage, A036 cost difference and A176 auto-chargeback (N-U13, updated 21 Nov 2025). Target asks suppliers to limit re-disputes to three and will fine a fifth dispute (N-U13).

**Home Depot**
- **Two sources agree** on a monthly offset cycle with a short window (N-U17, 12 Mar 2024: "have a month from then to dispute"; N-U16, 7 May 2026: second Wednesday to second Tuesday).
- **Correction to check S.** Check S item 7 used Home Depot's "12-month dispute window" as the example of back-claims a vendor could file on day one. N-S12 (re-read) says only "12 months based on the invoice date" and "trade discounts are no longer disputable". **The compliance offsets this card targets have a window of about 4 weeks**, so the 12 months applies to invoice disputes, not to OTIF-type offsets **[our call]**.
- The threshold figures (98% / 90%, 10% offsets, $1,000 missing ASN) come from one vendor page (N-U17). A 3PL marketplace page mentions a supplier scorecard ("SER") with a 95% line but no rates (N-U17 row note).

**Lowe's**
- Weakest sourcing of the seven. The SPS SupplierWiki page returned 404 on fetch; the 2nd-16th window and "deducted from the invoice" come from its search snippet (N-U19).
- The 98% / 95% and 10% figures come from one undated 3PL page (N-U18). **They match Home Depot's structure closely enough that a copying error cannot be ruled out [our call].**

**Costco**
- No public rate or window. A vendor guide says the charges are individual rather than a percentage, and a 3PL-side snippet says Costco's fee schedule is published "through a portal that requires a login" (N-U22). Nothing here is load-bearing.

**Kroger** (the one retailer read at source)
- The letter of 2 Dec 2024, signed by two Kroger logistics VPs, with "Kroger Policies" as Appendix A (N-U20, *verified*). Load-bearing quotes:
  - "Effective January 1st, 2025, our ORAD compliance threshold will increase from 90% to 93%. This policy will be reviewed annually and is subject to change."
  - Late POs "will be subject to a fee of 3% of the invoiced amount (the "ORAD Compliance Fee"). Fees will be assessed via invoice deductions."
  - "Loads that arrive after midnight of the ORAD, but that are still within the Kroger distribution centers' receiving hours for the previous day will be considered on time."
  - "Vendor agrees that all amounts set forth in this fee table are reasonable liquidated damages and do not constitute a penalty."
  - "Kroger reserves the right to deduct, set-off or withhold payments determined by Kroger to be due and owing by Vendor, whether determined by Kroger during any audit conducted on behalf of Kroger or otherwise."
- **The fee applies only to vendor-caused lateness** ("found to be a result of Vendor-caused issues"). **That is the dispute lever:** proving the carrier, the appointment or the DC caused the delay. It needs carrier and gate records.
- Kroger reviews books "for a period of up to five (5) years" through a third party of its choosing. That is the source of post-audit claims.
- History: in 2017 Kroger charged "$500 per day for deliveries made past a two-day window" (Grocery Dive, N-U40, *assumed*). The per-PO 3% model is newer.

**Amazon 1P**
- Chargeback rates are from an agency guide of Jul 2024 (N-U23). No later rate change was found.
- **Shortage rules tightened through 2025** (N-U24, N-U25, N-U26, all vendor).
  - The 2-year cap is dated "As of mid-2025".
  - The end of bulk disputes is dated only by an article of 26 Aug 2025.
  - The new re-dispute process is described in an article of 7 Apr 2026, which says Amazon announced it "earlier in September" without a year; N-S12 (Dec 2024) already describes re-disputes of up to 10 claims.
- **The population shrank.** From Sep 2024, Amazon told many smaller vendors it would stop buying from them on 9 Nov 2024 and would "no longer enter into any new agreements, or extend current ones"; agencies report the cut fell mainly on vendors under about $10M of US revenue (N-U27, *assumed*).

**Dollar General and Best Buy:** not covered. One Dollar General search found no fine rate. Best Buy was skipped: its 10-K says its 20 largest suppliers are about 80% of purchases (N-U37), so few small suppliers are exposed.

---

## 3. Changes since 2024

| Date | Who | Change | Tightens or eases the supplier's position | Label; source |
|---|---|---|---|---|
| 1 Feb 2024 | Walmart | On time 98% → **90%** (prepaid); in full **95%**; collect 98%; OTIF billing monthly → **quarterly** | **Eases** | *assumed*; N-E26, N-S13, N-S12 |
| 8 May 2024; 31 Jul 2024; 4 Feb 2025 | SPS Commerce | Buys Traverse Systems (~50 1P customers), SupplyPike (~200) and Carbon6 (~300 1P plus ~8,200 3P) | Market: the EDI incumbent enters recovery | *verified*; N-U01 |
| 4 Aug 2024 (Q3 2024) | Target | Fill Rate Original replaces the revised metric, measured by item; on-time and fill fines **5% → 3%** of COGS; prepaid window one day either side | **Eases** the rate; **tightens** the measure (item level) | *assumed*; N-U12, N-S12 |
| 2024 (reported Dec 2024) | Home Depot | Disputes quarterly → **monthly**; trade discounts "no longer disputable" | **Tightens** | *assumed*; N-S12 |
| 2024 (reported Dec 2024) | Amazon | Suppliers may **re-dispute** shortage claims (up to 10 per re-dispute) | **Eases** | *assumed*; N-S12 |
| Sep → 9 Nov 2024 | Amazon | Ends Vendor Central agreements with many smaller vendors | Shrinks the small 1P population | *assumed*; N-U27 |
| 1 Jan 2025 | Kroger | ORAD on-time bar **90% → 93%**; new enterprise-wide fee schedule for all DCs | **Tightens** | ***verified***; N-U20 |
| 1 May 2025; 1 Nov 2025 | Kroger | Near-real-time **location**, then **temperature**, data on inbound loads; $100 per PO, cap $10,000 | **Tightens** (a new data duty, which falls on the supplier's carrier) | ***verified***; N-U20 |
| 4 May 2025 | Target | **Perfect Order**: ASN availability, ASN accuracy, barcodes, at $0.75 per carton | **Tightens** (two new metrics) | *assumed*; N-U12 |
| Mid-2025 | Amazon | Shortage disputes capped at **2 years** of invoices (was 5); bulk disputes ended (by Aug 2025); POD no longer required, unit-level data preferred | **Tightens** (more line-level work, shorter lookback) | *assumed*; N-U24, N-U25 |
| By 21 Nov 2025 | Target | **Fines for disputing** a deduction a fifth time or more | **Tightens** (a direct counter to high-volume disputing) | *assumed*; N-U13 |
| Q4 2025 (said 12 Feb 2026) | SPS Commerce | Revenue recovery came in at "the lower end" of expectations, with "effects from the take rate model" and "Amazon policy changes"; plans to shift from a take rate to subscriptions | Market: a retailer's rule change hit a contingency-style model | *assumed*; N-U31 |
| 25 Mar 2026 | Glimpse | $35M Series A led by Andreessen Horowitz ($52M in total); "more than 200 retail brands" | Market: a funded entrant | *assumed*; N-U34 |
| 26 May 2026 | Walmart | **Prepaid Consolidation Program**, managed by Walmart, with no change to prepaid terms | **Eases** (a prevention route) | *verified*; N-U05 |
| 30 Jun 2026 | SPS Commerce | Sells its 3P revenue-recovery business (~7,300 customers) for $9.5M to focus on "1P suppliers who operate multi-retailer trading relationships" | Market: the incumbent narrows onto **this card's buyer** | *verified* (release) N-U33; count *assumed* N-U32 |

**Reading [our call]:**
- **Rules:** 7 tightenings against 4 easings since Jan 2024 (Target's Aug 2024 change counts on both sides; Amazon's vendor cuts on neither). The easings are concentrated at Walmart in early 2024. Since Jan 2025 every dated rule change found tightens, except Walmart's consolidation option.
- **Retailers are pushing back on dispute volume itself:** Target's repeat-dispute fine and Amazon's end of bulk disputes both act on high-volume, automated disputing. That is the method a software entrant would use.
- **Not found:** any 2024-2026 change at Lowe's or Costco, or any Walmart target change after Feb 2024.

---

## 4. The buyer count

**The population:** small and mid-sized suppliers (**sales of $500M or less**, matching CRF's cut) that sell direct to at least one big-box retailer (Walmart, Target, Home Depot, Lowe's, Costco, Kroger, Amazon 1P).

### 4.1 Inputs

| # | Input | Value | Label | Source |
|---|---|---|---|---|
| I1 | **Walmart's US supplier records**, summed over its 50 state pages plus DC and Puerto Rico. Footnote: "Supplier figures provided by Dun & Bradstreet for FYE 2025" | **31,196** (30,599 without Puerto Rico); spend with them **$412.4B**. Largest: California 3,868, Texas 2,509, Illinois 2,385, New York 1,922 | *verified* (read from Walmart's data file); sum **[our calc]** | N-U03 |
| I2 | Walmart: "more than 60 percent of Walmart U.S. suppliers that are small businesses" (9 Oct 2025). "Small business" is not defined | >60% → **>18,700** small suppliers [our calc] | *verified* (company statement) | N-U04 |
| I3 | **SPS Commerce 1P recurring revenue customers**, 31 Dec 2025 ("1P" = customers with retailer or wholesale trading connections, not only a marketplace connection). Total 54,600; ARPU (annual revenue per customer) about $14,350 | **46,900** | *verified* (10-K) | N-U01 |
| I4 | SPS's acquired revenue-recovery bases: Traverse "approximately 50 1P" (May 2024); SupplyPike "approximately 200 1P" (Jul 2024); Carbon6 "approximately 300 … 1P" (Feb 2025) | **~550** | *verified* (10-K) | N-U01 |
| I5 | Home Depot supplier base "between 10,000 and 12,000" (2008); Lowe's "approximately 7,000 merchandise vendors worldwide" (10-K, around FY2001) | 10-12k; ~7k | *assumed* (snippets; 18-25 years old) | N-U36 |
| I6 | Latest 10-Ks of Walmart, Target, Home Depot, Lowe's, Costco, Kroger, Dollar General, Best Buy and Amazon | **No supplier counts.** Dollar General: two largest suppliers 11% and 8% of purchases; Best Buy: 20 largest about 80% | *verified* (absence) | N-U37 |
| I7 | **Census SUSB 2022** (firm counts by employment size). Consumer-goods manufacturers (NAICS 311, 312, 315, 316, 3222, 3256, 3351, 3352, 337, 3399) and consumer-goods merchant wholesalers (4232, 4236, 4237, 4239, 4242, 4243, 4244, 4249); the code choice is **[our call]** | Under 500 staff: 75,272 + 131,723 = **206,995**. 5-499 staff: 41,634 + 54,659 = **96,293**. 20-499 staff: 15,315 + 18,600 = **33,915**. 500+ staff: 1,555 + 1,946 = 3,501 [our calc] | *verified* (file re-parsed) | N-D04 / N-E17 (re-parsed) |
| I8 | GS1 US: "More than 300,000 members across 25 industries" | >300,000 barcode licensees | *assumed* (the body's own claim; GS1 US flag) | N-U35 |
| I9 | Amazon ended many small 1P vendor agreements from 9 Nov 2024 | Unquantified reduction | *assumed* | N-U27 |
| I10 | Amazon 1P vendor count | **Not found.** An agency claim of about 1 million 1P vendors was dismissed as unsupported | — | §9 |

### 4.2 Method

**Step 1: start from Walmart**, the retailer with the widest supplier base and the only one publishing a current count (I1). Three adjustments, all **[our call]**:
- **a. Double counting across states: × 0.75-1.0.** It is not stated whether Dun & Bradstreet counts a supplier once (at its headquarters) or once per state where it has a location.
- **b. Suppliers in scope of OTIF-type fines: × 0.6-0.9.**
  - Excluded: direct-store-delivery suppliers and any service or non-resale suppliers in the D&B list.
  - The $412.4B spend is close to Walmart's US merchandise cost, which suggests the list is mostly merchandise suppliers.
- **c. Size cut to $500M of sales or less: × 0.85-0.95.** Walmart says more than 60% are "small businesses" (I2), and the firms above $500M number in the low thousands at most. Census shows only 3,501 firms with 500+ staff across the 18 consumer-goods codes in I7.
- **Walmart-only result:**
  - low 31,196 × 0.75 × 0.6 × 0.85 = **11,932**;
  - high 31,196 × 1.0 × 0.9 × 0.95 = **26,673** [our calc].

**Step 2: add suppliers that sell to other big-box retailers but not to Walmart. Uplift × 1.3-2.0 [our call].**
- Home Depot's (10-12k, 2008) and Lowe's (~7k, around 2001) bases are each a third to a half of Walmart's today, overlap heavily with each other, and overlap partly with Walmart (I5).
- Target, Kroger and Costco add mostly food and consumer suppliers who also sell to Walmart.
- Amazon added small 1P vendors until 2024 and then cut many of them (I9).
- **Result:**
  - low 11,932 × 1.3 = **15,512**;
  - high 26,673 × 2.0 = **53,345**;
  - geometric midpoint **28,766** [our calc].

**Step 3: cross-checks.**
- **Against SPS (I3).**
  - SPS's 46,900 1P customers include retailers, distributors, 3PLs and suppliers to regional or non-big-box buyers.
  - SPS is also only one of several retail EDI providers.
  - A population of 15-55k direct big-box suppliers is consistent with that. **A 100,000+ count would need SPS to reach well under half of it, while also carrying many customers outside it [our call].**
- **Against Census (I7).**
  - The range sits between the consumer-goods firms with 20-499 staff (33,915) and those with 5-499 staff (96,293).
  - **A 100,000+ count would need almost every consumer-goods manufacturer and wholesaler with 5 or more staff to sell direct to a big-box retailer, which is implausible [our call].**
  - Caveat: SUSB counts a firm once in each industry it operates in, so summing across codes slightly overcounts.
- **Against GS1 US (I8):** 300,000+ is a ceiling on firms with barcoded products, most of which never ship to a big-box DC.

### 4.3 Result, the overlap problem and the size cut

- **Buyer count: about 15,000 to 55,000; central about 29,000** [our calc on [our call] factors].
- **The overlap problem.**
  - One supplier often sells to several retailers, so retailer counts cannot be added.
  - This check handles it with the step-2 uplift, which is the least supported factor.
  - The two published counts that would narrow it (current Home Depot and Lowe's supplier numbers) were not found.
  - SPS says its 1P focus is suppliers "who operate multi-retailer trading relationships" (N-U33), which suggests multi-retailer suppliers are common among the paying buyers.
  - The C21 interviews should ask how many retailers a typical client sells to (§6.2).
- **The size cut.**
  - CRF cuts at $500M of sales; Census cuts at 500 staff; Walmart does not define "small business".
  - Most consumer-goods firms under 500 staff are under $500M of sales, but some larger-staff firms are too. The employee cut therefore slightly undercounts mid-sized suppliers **[our call]**.
  - The factors above use sales, not staff.
- **Who is too small to pay.**
  - The count includes micro-suppliers whose deductions are too small to be worth disputing.
  - CRF's 2018 median of non-trade deductions at ¼-½% of sales (N-N29) means a supplier selling $5M a year to big-box stores carries about $12,500-25,000 of such deductions [our calc]. Only a share of that is disputable.
  - This belongs in Lucrative, not in Plausible, but it is a reason the paying count is below the problem count.

### 4.4 What it does to Cohen's Plausible row

Cohen's score for C-19 is Plausible × 0.5 × $1,000 × 1.0 × 0.5 × 0.5 × 0.5 ÷ 625,000, which equals **Plausible ÷ 10,000** [our calc on `4_scorecard.md` §4.2].

| Count used | Rounded to a power of ten | Cohen score | Unrounded score (for scale only) |
|---|---|---|---|
| Low, 15,512 | 10,000 | **1.00** | 1.55 |
| **Central, 28,766** | **10,000** | **1.00** | 2.88 |
| High, 53,345 | 100,000 | **10.00** | 5.33 |
| Rounding boundary | 31,623 (10^4.5) | — | — |

- **The central reading keeps S4's 10,000**, so C-19 stays at 1.00, the indie threshold. The count is no longer a pure judgement: it rests on Walmart's published 31,196.
- **It is a knife-edge.** The boundary sits at 42% of the way down from the top of the range on a log scale [our calc]. A 10% higher central factor would flip it.
- **The "if the count is 100,000" line in S4 is not the central reading**, but it is inside the range.
- **Per-buyer check:** the central fee pool of $33M ÷ 28,766 = **about $1,150 a year per buyer** [our calc], consistent with S4's Lucrative row of $1,000. SPS's own view is higher: it calls revenue recovery "a $750 million addressable market across 1P U.S. sellers" (N-U31, *assumed*: a vendor's addressable-market claim). That is about $26,000 per buyer on this count [our calc], or 4.5× this card's high-end fee potential of $168M.

---

## 5. The 2018 gap today

**The 2018 baseline** (N-N29, *verified* PDF, CRF flag): 30% of firms with sales of $500M or less used third-party deduction technology, so **70% used none**; none outsourced any deduction task.

**Newer readings of the same survey series.** Read on a slide presented by **Carixa, a deduction-software vendor and CRF survey partner**, at NACM's Credit Congress (dated 9 May 2024, presented 11 Jun 2024), headed "Use of 3rd Party Technologies" and sourced "*2023 Deduction Metrics Survey" (N-U28). The slide image was read directly; the survey report was not (participation-only, N-U30). *Assumed*, CRF flag.

| Survey year | Use 3rd-party technology, sales ≤ $500M | **Use none, ≤ $500M** [our calc] | Use it, sales > $500M | Use it, all respondents |
|---|---|---|---|---|
| 2018 | 30% | **70%** | 58% | 44% (N-N29) |
| 2021 | 35% | **65%** | 75% | 57% |
| 2023 | **45%** | **55%** | 73% | 68% |

- **The 2018 row on the slide matches the 2018 PDF** (30% / 58%). That supports the slide's fidelity for the later rows.
- Same slides: **47% of 2023 respondents said deductions as a share of sales had increased** in the past 12 months, against 34% in 2021.
- An earlier Carixa deck (CRF August Forum, 8 Aug 2023, N-U29) cites the 2021 CRF survey: deductions "up to 1% of sales", "5-10%" invalid, "60%" recovered, "90-day median" resolution.
- **Caveats [our call]:**
  - Sample sizes are not shown. The 2021 Attain survey drew "more than 100 companies" (IOFM snippet, N-U30 row note).
  - Respondents are credit professionals who chose to answer a benchmarking survey, and are likely more automated than the average small supplier.
  - "Third-party technology" is broad: it can mean any tool (an AR suite, OCR, a portal bot), not specifically retailer-deduction recovery.
  - The figure covers all customers' deductions, not only big-box retailers.

**What SPS's filings and calls say.**
- **Scale of SPS's recovery base.** SPS acquired about **550 1P revenue-recovery customers** in 2024-25 (N-U01, *verified*). That is **1.2% of SPS's own 46,900 1P customers**, and **1.0-3.5% of this file's buyer count** [our calc]. SPS has not disclosed a later revenue-recovery customer count (N-U31, N-U32).
- **Q4 2025:** revenue recovery landed at "the lower end of what our expectation would be", citing "effects from the take rate model" and "Amazon policy changes" (CFO, N-U31, *assumed*).
- **Q2 2026:** "We are seeing the cross-selling to our fulfillment customers be good" (CEO); the 3P sale divested "approximately 7,300 customers" (CFO) (N-U32, *assumed*).
- **The Q4 2025 $750M addressable-market claim** (N-U31) implies SPS sees most of the 1P market as unserved. It is a vendor claim and not evidence of penetration.

**Other entrants since 2024.**
- **Glimpse:** "more than 200 retail brands" and $52M raised (N-U34, *assumed*).
- Check S's named vendors still stand (N-F55, N-S35, N-S36).
- No customer counts were found for iNymbus, HighRadius, Vendormint or Carixa (§9).

**Best current reading [our call], dated 2023 data read on 2026-09-16:**
- **The gap is still open but narrowing.** In 2023, **55%** of firms with sales of $500M or less used no third-party deduction technology, down from 70% in 2018.
- **Pace:** +5 points of adoption from 2018 to 2021 and +10 points from 2021 to 2023. If adoption rose by 5-15 points after 2023, it would be about 50-60% by 2026, **leaving roughly 40-50% of small and mid-sized suppliers with no third-party tool** [our calc; extrapolation, weak].
- **SPS has not closed the gap.** Its disclosed recovery base is a few percent of the buyers at most. **But since June 2026 it is aimed squarely at this card's buyer** (1P multi-retailer suppliers), and it sells into an EDI base of 46,900 1P customers.

---

## 6. Who works against retailers daily, and what the C21 interviews must settle

### 6.1 Firm types and where they gather

| Firm type | What they do daily against retailers | Named public examples | Label; source |
|---|---|---|---|
| **Contingency deduction-recovery and post-audit claim firms** | File disputes and fight post-audit claims for suppliers, paid a share of recoveries (Vendormint: 30%) or a flat fee (ClearChain: $5,000 a month) | HRG (Bentonville, AR; "Retail Deduction Recovery Experts"), Vendormint, Smyyth, Woodridge Retail Group, STAT Recovery, ClearChain, OverDeduct | *assumed* (vendor pages, snippets); N-U38, N-S35 |
| **Deduction-software vendors' managed-service analysts** | Run portal bots and dispute queues across retailers | SPS Revenue Recovery (SupplyPike), iNymbus, Glimpse, Carixa, HighRadius, RetailPath | *assumed*; N-S36, N-U34, N-U28. **These are competitors: good for facts on retailer behaviour, poor for facts on the gap** [our call] |
| **Retail-compliance teams at 3PLs** | Build loads, labels, ASNs and appointments to each retailer's routing guide; field chargebacks on behalf of brand clients | Distribution Alternatives, ShipCalm, WarehouseQuote (a 3PL marketplace), Productiv (compliance software) all publish retailer compliance guides | *assumed*; N-U14, N-U18, N-U22 |
| **Carriers and brokers on retail lanes** | Hold the check-in, appointment and POD records that decide on-time disputes; Walmart and Kroger now run their own consolidation or managed-lane options | Uber Freight (quoted on Walmart fines, N-S13); Walmart's Prepaid Consolidation Program (N-U05); Kroger-managed lanes (N-U20) | *assumed* / *verified* |
| **Retail consultancies** | Advise suppliers on one retailer's scorecards and portals | 8th & Walton (Walmart) | *assumed*; N-F37 |
| **Retailer-side audit firms and their former staff** | Raise post-audit claims *for* retailers; former staff know the retailer's position from inside | **PRGX**: Kroger routes billing-inquiry correspondence to a PRGX mailbox (N-U20, *verified*) | *verified* for Kroger's use of PRGX; the move of ex-staff into supplier-side firms is **[our call]** |
| **Where these people gather** | Credit and deductions sessions | **CRF** March Forum (23-25 Mar 2026, Charleston) and August Forum & Expo (2026, Denver); **NACM** Credit Congress (deductions sessions, e.g. Jun 2024); IOFM accounts-receivable webinars; the Northwest Arkansas supplier community around Bentonville (HRG, 8th & Walton) | *assumed* (snippets, N-U39); NACM session *verified* (N-U28) |

No individuals are named. Recruiting 1-2 interviewees is S5's job; the easiest first contacts are a contingency recovery firm and a 3PL compliance lead **[our call]**.

### 6.2 What the 1-2 C21 interviews must settle

1. **Walmart's OTIF dispute window in practice.** Is it 30 days, or no fixed window? It is the one rule conflict this file could not settle (§2.3).
2. **The deduction mix** for a typical small or mid-sized client: what share is OTIF and compliance fines, what share shortages, what share pricing and promotions? Only the first two rest on freight evidence, and this decides how much of the pool the card's sentence covers.
3. **What evidence actually wins, per retailer.** Retailer gate or yard records, carrier POD, appointment confirmations, or ASN data? Who holds each? Does the carrier or broker hand it over quickly?
4. **How short windows are missed.** How often do clients miss Home Depot's monthly window, Lowe's 2nd-16th, Walmart's 15-30 days for AP chargebacks, or Amazon's 30 days? That is the day-one value question for W3.
5. **The 2026 gap.** Among the small and mid-sized suppliers they see, what share uses SPS/SupplyPike, iNymbus, Glimpse or similar, what share uses a recovery firm, and what share does it in-house with spreadsheets or not at all? This is the test of the 2023 figure of 55% with no tool.
6. **Minimum client size.** Below what sales or deduction volume will a recovery firm not take a client? That floor cuts the buyer count to the paying count.
7. **Retailer counter-moves.** Target's repeat-dispute fine, Amazon's end of bulk disputes, portal limits on bots or shared credentials: how much do they cut win rates for automated disputing?
8. **Carriers and brokers.** Do they ever pay back fines they caused? Are they the first line today, as the card's sentence says?
9. **Overlap.** How many big-box retailers does a typical client sell to? This tests the ×1.3-2.0 uplift in §4.2.

---

## 7. For the coordinator (not a call)

**Desk reading of S4's question [our call]:**
- **"Is the 2018 gap still open, or has SPS's SupplyPike closed it?"** Open, but narrower. About 55% of suppliers at $500M or less used no third-party deduction technology in 2023, against 70% in 2018 (CRF, via a vendor's slide). SPS's disclosed recovery base is a few percent of the buyers. SPS has not closed the gap; it has aimed at it.
- **"How many small and mid-sized suppliers are there?"** About 15,000-55,000, central about 29,000, anchored on Walmart's published 31,196 supplier records.

**Rows the evidence bears on:**

| Row | S4 score | What this check adds | Direction **[our call]** |
|---|---|---|---|
| **A1** savings pool | 0.5 | Per-buyer fee about $1,150 at the central count (range about $110-10,800 [our calc]). CRF 2023: 47% of companies saw deductions rise as a share of sales. SPS claims a $750M 1P addressable market (vendor) | **Holds 0.5.** Upside only from a vendor claim |
| **A3** pain and urgency | 1 | S4's caveat was that a forcing event might have to be a new tightening, since Walmart eased in 2024. Since then: **Kroger 1 Jan 2025** (93% plus a new fee schedule), **Target 4 May 2025** (Perfect Order), **Amazon mid-2025** (2-year cap, end of bulk disputes), **Target by Nov 2025** (repeat-dispute fines), **Kroger May and Nov 2025** (data fees). Kroger's is *verified* | **Firms up the 1**, even under the strict reading |
| **W1** access | 0.5 | The buyers are spread across at least 8 retailer portals with no neutral gathering point. The most concentrated channel, SPS's 46,900 1P customers, belongs to a competitor. Partial channels: recovery firms, 3PLs, CRF and NACM forums | **Holds 0.5**; leans lower if SPS's network is the only efficient route |
| **W3** whole product and time to value | 0.5 | Eight or more portals and a dozen windows from 48 business hours to 24 months. **The OTIF-type fines have short windows** (Home Depot about 4 weeks; Lowe's 15 days; Walmart AP chargebacks 15-30 days; Amazon 30 days). **Check S's Home Depot "12 months" applies to invoice disputes, not to compliance offsets.** Long windows remain for shortages and invoice disputes (Walmart 12-24 months, Target 18, Amazon 24, SQEP 13). Evidence rules are shifting (Amazon prefers unit-level data; Walmart's APDP rejects carrier-generated delivery reports) | **Holds 0.5.** Day-one back-claims are weaker for OTIF fines than S3b assumed, and hold for shortages |
| **W4** competition and substitutes | 1 | Gap 70% → 55% with no tool (2018 → 2023); SPS's recovery base is 1.0-3.5% of buyers; no dominance. But a funded entrant (Glimpse, $52M) and SPS's refocus on 1P | **Holds 1 on the letter** (software still missing for most in 2023). **The S4 sensitivity W4 = 0.5 is now closer**, and "most" may not hold by 2026-27 if the trend continued |
| **W6** time and resources to win | 0.5 | SPS sold 3P in Jun 2026 to focus on multi-retailer 1P suppliers and is cross-selling recovery into its EDI base. Retailers now counter high-volume disputing (Target, Amazon). SPS's take-rate revenue was hit by Amazon's policy changes | **Holds 0.5, leans 0** |
| **F3** measurability | 1 | Every retailer collects by deduction, with reason codes. **Walmart OTIF recoveries show up as approved HighRadius disputes on an AR invoice, not as remittance lines**, so measurement is retailer by retailer | **Holds 1** |
| **F4** predictability | 0.5 | Published rates (3% of cost; 10% offsets; per-carton fees) make a supplier's fines predictable from its own history. But rules change often (11 dated rule changes in about 30 months, §3), and SPS's take-rate revenue moved with Amazon's policy | **Holds 0.5**; retailer rule changes are the source of unpredictability |
| **Cohen Plausible** | 10,000 (a judgement) | Central 28,766 → rounds to 10,000 → score 1.00. High end 53,345 → 100,000 → 10.00. Boundary 31,623 | **Confirms 10,000 as the central reading, now anchored on a published count.** A knife-edge: the upper ~42% of the range gives 10.00 |

**Not covered, and worth knowing:** W5 is untouched. The Amazon 1P population fell in late 2024 (I9), which lowers the Amazon-only share of the count but does not change the range.

---

## 8. Sources

**Existing IDs re-read or re-parsed in this check** (listed in their own files):
- **N-E26**, SPS SupplierWiki, "Walmart's OTIF Performance Metrics": re-read (updated 5 Feb 2024; prepaid 90%, collect 98%, in full 95%).
- **N-S12**, SPS SupplierWiki, "Retail Updates Every Supplier Should Know Before 2025" (10 Dec 2024): re-read for Home Depot's wording ("12 months based on the invoice date"; trade discounts "no longer disputable"), Target, Walmart and Amazon.
- **N-D04 / N-E17**, Census SUSB 2022, `us_state_6digitnaics_2022.txt`: re-downloaded and re-parsed for firm counts by employment size in the 18 consumer-goods codes in §4.1 (I7).

**Cited without re-fetching:** N-N29, N-F37, N-F55, N-S10, N-S11, N-S13, N-S35, N-S36, N-S40.

**New sources.** All were accessed on 2026-09-16. Downloads are in the session scratchpad (`…/scratchpad/checkU/`).

| ID | Source (author/org) | Date | URL | Access | What it gives |
|---|---|---|---|---|---|
| N-U01 | SPS Commerce, Form 10-K for FY2025 (SEC EDGAR, `spsc-20251231.htm`) | filed 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1092699/000109269926000012/spsc-20251231.htm | full download, text searched (*verified*) | 54,600 customers, 46,900 1P; ARPU ~$14,350; ~50 / ~200 / ~300 1P customers added with Traverse, SupplyPike, Carbon6; SupplyPike "an automated invoice deduction management and prevention solution", $205.8M; Carbon6 $210.2M |
| N-U02 | SPS Commerce, Form 10-K for FY2024 (`spsc-20241231.htm`) | filed 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1092699/000109269925000011/spsc-20241231.htm | full download, text searched (*verified*) | 45,350 customers at end-2024; SupplyPike described as "a revenue recovery solution" |
| N-U03 | Walmart, "Location Facts" state pages and their data file (`locations.js`); footnote on the Texas page | figures FYE 2025; page updated 2026 | https://corporate.walmart.com/content/dam/corporate/documents/about/location-facts/locations.js ; https://corporate.walmart.com/about/location-facts/united-states/texas | full download, parsed (*verified*) | `numberOfSuppliers` and `spentWithSuppliers` for 52 states and territories; sum 31,196 and $412.4B [our calc]; "Supplier figures provided by Dun & Bradstreet for FYE 2025" |
| N-U04 | Walmart, "Walmart Highlights U.S. Manufacturing and Small Business Growth at 2025 Open Call" | 2025-10-09 | https://corporate.walmart.com/news/2025/10/09/walmart-highlights-us-manufacturing-and-small-business-growth-at-2025-open-call | page extraction; company statement | "more than 60 percent of Walmart U.S. suppliers that are small businesses"; $350B US commitment |
| N-U05 | Walmart, "Walmart Enhances Supply Chain to Bring Customers What They Need, When They Need It" | 2026-05-26 | https://corporate.walmart.com/news/2026/05/26/walmart-enhances-supply-chain-to-bring-customers-what-they-need-when-they-need-it | page extraction; company statement | Prepaid Consolidation Program; no change to prepaid terms; no OTIF change |
| N-U06 | SPS Commerce / SupplierWiki, "The Unofficial Guide to Disputing Walmart OTIF Fines" | updated 2023-08-28 | https://www.spscommerce.com/community/articles/walmart-otif-dispute-process | page extraction; vendor (*assumed*) | Fines invoiced in HighRadius, 3% of COGS, about 5 weeks after quarter end; advice to dispute in-full fines 60-150 days after invoicing |
| N-U07 | SPS Commerce / SupplierWiki, "How To Dispute Walmart OTIF Chargebacks" | updated 2024-05-06 | https://www.spscommerce.com/community/articles/how-to-dispute-walmart-otif-chargebacks | page extraction; vendor (*assumed*) | Chargeback "in the form of an invoice"; deducted from future payments if unpaid; HighRadius, not APDP; 10 attachments |
| N-U08 | Glimpse, "How to Dispute Walmart Deductions: A Step-by-Step Guide" | 2026 (titled June 2026) | https://www.tryglimpse.com/post/disputing-walmart-deductions-step-by-step | page extraction; vendor (*assumed*) | APDP vs HighRadius; AP chargebacks 15-30 days; shortages 12 months; general 2 years; APDP rejects carrier-generated delivery reports; code 98 change (Jul 2023) |
| N-U09 | iNymbus blog, "Walmart OTIF vs SQEP" | 2026-08-25 | https://blog.inymbus.com/walmart-otif-vs-sqep | page extraction; vendor (*assumed*) | OTIF targets and 3% fine, quarterly billing; SQEP launched 15 Sep 2020, $200 per PO + $1 per case, 13-month window via EIPP; OTIF 30 days via APDP (conflicts with N-U07) |
| N-U10 | ClearChain, "Walmart OTIF Chargebacks Explained" | undated (2026) | https://useclearchain.com/walmart-otif-chargebacks | page extraction; vendor (*assumed*) | "30-day window"; evidence list (BOL with carrier timestamp, DC receiving stamp, appointment confirmation, PO) |
| N-U11 | RetailPath, "Walmart OTIF Fines Explained"; Orderful, "Walmart OTIF Requirements" | 2026-02-07; 2025-10-01 (updated 2026-03-19) | https://www.retailpath.ai/blog/walmart-otif-fines/ ; https://www.orderful.com/blog/walmart-otif | page extraction; vendors (*assumed*) | Both describe a single 98% target (out of date against N-E26); fines "quietly reduce what you are paid" |
| N-U12 | SPS Commerce Help Center, "Understanding Target's Compliance Program" | 2025-03-13 | https://help.supplypike.com/en/articles/8300994-understanding-target-s-compliance-program | page extraction; vendor (*assumed*) | Fill Rate Original 95% (from 4 Aug 2024); on time 100%; 3% COGS; Perfect Order from 4 May 2025 at $0.75 per carton; prepaid vs collect definitions |
| N-U13 | SPS Commerce, "Target Disputing Best Practices for 2025" | updated 2025-11-21 | https://www.spscommerce.com/community/articles/target-disputing-best-practices-for-2025 | page extraction; vendor (*assumed*) | 18-month research limit; collect 9 months; 5 business days; Synergy and POL; POD vs proof of shipment; fines for fifth dispute; dispute codes |
| N-U14 | WarehouseQuote, "2026 Target Vendor Compliance Guide" | 2026 (undated) | https://www.warehousequote.com/resources/target-supplier-compliance-guide | page extraction; 3PL marketplace (*assumed*) | Four OTFR metrics at 3% COGS; collect routing entry by 11:00 CT two business days before; Synergy |
| N-U15 | Search summaries on Target Perfect Order and the dispute lifecycle (Distribution Alternatives; Productiv; Cahoot) | 2025-26 | https://www.daserv.com/target-vendor-compliance-guide/ ; https://getproductiv.com/target-compliance-asn-accuracy ; https://www.cahoot.ai/target-vendor-portal/ | snippet (*assumed*) | $100 minimum; two-week violation lifecycle for exemption requests; 18 months / 9 months |
| N-U16 | iNymbus blog, "Home Depot Supplier Compliance & Dispute Process Explained" | 2026-05-07 | https://blog.inymbus.com/home-depot-supplier-compliance-and-dispute-process-explained | page extraction; vendor (*assumed*) | SPM metrics; offsets "deducted at the Payables Vendor level"; windows (second Wednesday to second Tuesday; V codes 48 business hours; DQC); prepaid vs collect |
| N-U17 | SPS Commerce / SupplierWiki, "Compliance at Home Depot"; WarehouseQuote, "Home Depot Supplier Compliance Guide" | updated 2024-03-12; undated | https://www.spscommerce.com/community/articles/compliance-at-home-depot ; https://www.warehousequote.com/resources/home-depot-supplier-compliance-guide | page extraction; vendor / 3PL marketplace (*assumed*) | 98% fill, 90% on time, 10% offsets; ASN $1,000 / $250 / $100; routing $250; a month to dispute; evidence types; SER 95% (no rates) |
| N-U18 | Distribution Alternatives, "3PL for Lowe's" | undated | https://www.daserv.com/3pl-for-lowes/ | page extraction; 3PL (*assumed*) | 98% fill, 95% on time, 10% offsets; ASN $250; invoice ~$50; label ~$10; EDI 753 ready date with one-day grace |
| N-U19 | SPS SupplierWiki, "Vendor Performance (Compliance/OTIF) at Lowe's" (search snippet; page 404 on fetch); Productiv, "Lowe's Vendor Compliance" | undated; 2026-03 | https://supplierwiki.supplypike.com/articles/vendor-performance-compliance-otif-at-lowes ; https://getproductiv.com/lowes-vendor-compliance | snippet; page extraction; vendors (*assumed*) | VCS rebuttals 2nd-16th of the month; "deducted from the invoice"; Lowe's mainly collect; no rates on Productiv |
| N-U20 | Kroger (VP Logistics & Transportation; VP Supply Chain Planning & Logistics), "VNC Program Updates" letter with Appendix A "Kroger Policies" | 2024-12-02 (posted Mar 2025) | https://kroger.onenetwork.com/wp-content/uploads/2025/03/1-VNC-Program-Updates_final_signed.pdf | full PDF download, text read (*verified*) | ORAD 90% → 93% (1 Jan 2025); 3% late-PO fee; 95% case fill; fee schedule; location and temperature data (1 May / 1 Nov 2025); deduction from invoices; 60-180-day inquiry window; PRGX and Lavante; prepaid vs Kroger-managed |
| N-U21 | SPS SupplierWiki, "What Are the Different Types of Kroger Deductions?" | updated 2025-04-21 | https://www.spscommerce.com/community/articles/what-are-the-different-types-of-kroger-deductions | page extraction; vendor (*assumed*) | 13 deduction types; ORAD late shipment needs POD; 180 days; Lavante |
| N-U22 | Productiv, "Costco Vendor Compliance"; search summaries on Costco fines (Productiv, WarehouseQuote, Stone Management) | 2026-02-15; 2026 | https://getproductiv.com/costco-vendor-compliance ; https://www.warehousequote.com/resources/2026-costco-supplier-compliance-checklist | page extraction; snippet; vendors (*assumed*) | Appointments, ASN, pallets, SSCC labels; charges "assessed individually"; $500 late-truck fine (snippet); fee schedule behind login; "30 to 60 days" (snippet) |
| N-U23 | Hinge Commerce, "Vendor Central Operational Performance: Chargebacks, Invoices and Disputes" | 2024-07-10 | https://hingecommerce.com/vendor-central-invoices-chargebacks/ | page extraction; agency (*assumed*) | ASN accuracy 2/4/6%; PO on-time 3% and 10%; deducted from remittances; reopen once; ~3 weeks to resolve |
| N-U24 | SPS Commerce Help Center, "Shortage Claim" | 2025-09-17 | https://help.supplypike.com/en/articles/6839939-shortage-claim | page extraction; vendor (*assumed*) | 30 days from invoice due date; 2-year limit "As of mid-2025"; "Amazon no longer requires suppliers to provide a POD" |
| N-U25 | Threecolts, "Amazon Ends Bulk Shortage Claims"; Wake Commerce, "Amazon Vendor Central Shortage Claims" | 2025-08-26; 2024-07-11 | https://www.threecolts.com/blog/amazon-ends-bulk-shortage-claims/ ; https://www.wakecommerce.co.uk/blog/amazon-vendor-central-shortage-claims | page extraction; vendor / agency (*assumed*) | Bulk disputes discontinued; lookback 5 years → 24 months; claims can take up to 35 days |
| N-U26 | SPS Commerce Help Center, "Amazon's New Shortage Re-Disputing Process" | 2026-04-07 | https://help.supplypike.com/en/articles/10113369-amazon-s-new-shortage-re-disputing-process | page extraction; vendor (*assumed*) | Re-disputes only for partly approved or denied claims; initial review up to 40 days |
| N-U27 | Search summaries on Amazon's Vendor Central terminations (eComCatalyst; eComCrew; Digital Position) | 2024-09 to 2024-11 | https://ecomcatalyst.com/2024/09/09/amazon-abruptly-cancels-vendor-central-accounts-november-9-deadline/ ; https://www.ecomcrew.com/amazon-mass-terminates-vendor-central-agreements/ | snippet (*assumed*) | Agreements ended from 9 Nov 2024; mainly vendors under ~$10M US revenue |
| N-U28 | Carixa (deduction-software vendor), "Autonomous Trade Deductions: Unlocking Revenue Excellence…", NACM Credit Congress handout, citing the CRF "2023 Deduction Metrics Survey" (CRF flag) | slides dated 2024-05-09; presented 2024-06-11 | https://creditcongress.nacm.org/images/Handouts/33053_Unlocking%20Revenue%20Excellence.pdf | full PDF download; chart slides read as images (the survey itself not read, so *assumed*) | Third-party technology use by size, 2018 / 2021 / 2023 (30% / 35% / 45% at ≤$500M; 58% / 75% / 73% above); all respondents 68% (2023), 57% (2021); deductions rising: 47% (2023) vs 34% (2021) |
| N-U29 | Carixa, "How Technology is Changing the Way We Manage Deductions", CRF August Forum, citing the 2021 CRF deductions survey (CRF flag) | 2023-08-08 | https://www.crfonline.org/wp-content/uploads/2023/08/3-Carixa-Managing-Deductions.pdf | full PDF download (*assumed*) | "Up to 1% of sales"; 5-10% invalid; 60% recovered; 90-day median resolution |
| N-U30 | CRF, "Deductions Survey" page; IOFM webinar page on Attain's 2021 survey (snippet; page 403) | 2023; 2021 | https://www.crfonline.org/deductions-survey/ ; https://www.iofm.com/ar/webinars/2021-deduction-benchmarks-results-of-attain-consulting-group-s-annual-survey | page extraction; snippet (*assumed*) | 2023 survey partners Attain, Carixa, IAB LLC, RVCF; report only for participants; 2021 survey "more than 100 companies" |
| N-U31 | SPS Commerce Q4 2025 earnings call transcript (The Motley Fool) | 2026-02-12 | https://www.fool.com/earnings/call-transcripts/2026/02/12/sps-commerce-spsc-q4-2025-earnings-transcript/ | page extraction; company statements via a third-party transcript (*assumed*) | "$750 million addressable market across 1P U.S. sellers"; revenue recovery at the lower end of expectations; take rate; Amazon policy changes; shift to subscription |
| N-U32 | SPS Commerce Q2 2026 earnings call transcript (The Motley Fool) | 2026-07-30 | https://www.fool.com/earnings/call-transcripts/2026/07/30/sps-commerce-spsc-q2-2026-earnings-call-transcript/ | page extraction; third-party transcript (*assumed*) | Cross-selling recovery to fulfillment customers; ~7,300 customers divested; $9.5M; $23.5M loss; customer recovery anecdotes |
| N-U33 | SPS Commerce, "SPS Commerce Announces Agreement to Sell 3P Revenue Recovery Business" | 2026-06-30 | https://www.spscommerce.com/press/sps-commerce-announces-agreement-to-sell-3p-revenue-recovery-business/ | page extraction; company release | Focus on "1P suppliers who operate multi-retailer trading relationships"; 1P retailers supported: Amazon, Walmart, Kroger, Target, Home Depot, Lowe's |
| N-U34 | TechCrunch, "After pivoting, Y Combinator grad Glimpse raises $35M led by a16z" | 2026-03-25 | https://techcrunch.com/2026/03/25/a16z-backed-glimpse-raises-new-funds-accelerates-dispute-tracking-automation-for-cpg-brands/ | page extraction; trade press; company claims (*assumed*) | $35M Series A, $52M in total; "more than 200 retail brands"; portal agents |
| N-U35 | GS1 US, "About Us" (GS1 US flag) | undated | https://www.gs1us.org/who-we-are/about-us | page extraction (*assumed*: the body's own claim) | "More than 300,000 members across 25 industries" |
| N-U36 | Search snippets: SupplyChainBrain, "Home Depot Turns Its Attention to Supplier Performance Management"; Lowe's Form 10-K for FY2001 | 2008; 2002 | https://www.supplychainbrain.com/articles/605-home-depot-turns-its-attention-to-supplier-performance-management ; https://www.sec.gov/Archives/edgar/data/0000060667/000006066702000003/form10k2001e.txt | snippet (*assumed*; the 10-K download returned an empty file) | Home Depot 10,000-12,000 suppliers; Lowe's ~7,000 merchandise vendors |
| N-U37 | Latest Form 10-Ks of Walmart (FY Jan 2026), Target (Jan 2026), Home Depot (Feb 2026), Lowe's (Jan 2026), Costco (Aug 2025), Kroger (Jan 2026), Dollar General (Jan 2026), Best Buy (Jan 2026), Amazon (Dec 2025) | filed 2025-10 to 2026-03 | e.g. https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm ; https://www.sec.gov/Archives/edgar/data/56873/000110465926037723/kr-20260131x10k.htm (URLs via EDGAR submissions API) | full downloads, text searched (*verified*) | No supplier counts; Dollar General's two largest suppliers 11% and 8%; Best Buy's 20 largest ~80% |
| N-U38 | Deduction-recovery firm pages (HRG; Smyyth; Woodridge Retail Group; Vendormint; OverDeduct) | 2026 | https://www.hrg-audit.com/ ; https://www.smyyth.com/ar-deduction-services-outsourcing/post-audit-claims-management/ ; https://www.overdeduct.com/compare/best-cpg-retail-deduction-recovery-services | snippet; vendors (*assumed*) | Firm types; HRG in Bentonville; 30% contingency (Vendormint); post-audit claims "generated by retail audit teams or outsourced audit firms" |
| N-U39 | Search snippets on CRF events | 2026 | https://www.crfonline.org/events/march/ ; https://www.crfonline.org/events/august/ | snippet (*assumed*) | March Forum 23-25 Mar 2026, Charleston; August Forum & Expo 2026, Denver |
| N-U40 | Grocery Dive, "Walmart and Kroger fine suppliers for late or incomplete deliveries" | 2017-11-28 | https://www.grocerydive.com/news/grocery--walmart-and-kroger-fine-suppliers-for-late-or-incomplete-deliveries/534461/ | page extraction; trade press (*assumed*) | Kroger's 2017 fine of $500 a day beyond a two-day window (history only) |

---

## 9. Could not access, or not found

**Behind supplier logins (not attempted, by rule: no registration or log-in):**
- **Walmart's own OTIF policy and dispute terms** (Retail Link / Supplier One). **This leaves the Walmart OTIF dispute window unsettled** (§2.3).
- **Target's vendor manual** (Partners Online).
- **Home Depot's Supplier Hub and SPM documents.**
- **Lowe's Vendor Gateway documents.**
- **Costco's fee schedule**, the most thinly sourced retailer here.
- **Amazon Vendor Central help pages.**

**Blocked or unusable:**
- **SPS SupplierWiki's Lowe's Vendor Performance article:** the redirect returned 404, so its figures are a search snippet (N-U19).
- **CRF's 2021 and 2023 deduction survey reports:** available only to participants (N-U30). The 2021 and 2023 figures come from a vendor's slides (N-U28).
- **IOFM's page on Attain's 2021 survey:** HTTP 403.
- **SPS's investor-relations release on the 3P sale:** timed out. SPS's own press page (N-U33) was used instead.
- **Lowe's FY2001 10-K text:** the EDGAR download returned an empty file, so the ~7,000 vendor figure is a snippet (N-U36).
- **EDGAR full-text search**, used to look for supplier counts in older retailer 10-Ks: returned no usable JSON.

**Searched, not found** (each line was dropped after about three well-aimed attempts):
- **Current supplier counts for Target, Home Depot, Lowe's, Costco and Kroger:**
  - FY2025 10-Ks (N-U37);
  - corporate and sustainability pages;
  - general searches.
  - Only Walmart publishes one (N-U03).
- **Amazon 1P vendor count:** only an unsupported agency claim (~1 million), dismissed.
- **Customer counts for SupplyPike after 2024, iNymbus, HighRadius (deductions), Vendormint and Carixa:**
  - SPS's 10-K and two call transcripts;
  - vendor pages;
  - searches.
- **A neutral 2024-2026 survey of deduction-technology adoption** (IOFM, NACM, Hackett, APQC): none with a size split. The Hackett Group's Mar 2026 vendor matrix release has no adoption rate.
- **Walmart OTIF target changes after 1 Feb 2024:** none found. Vendor pages still quoting 98% are out of date (N-U11).
- **Any 2024-2026 rule change at Lowe's or Costco.**
- **The definition behind Walmart's supplier count:** whether multi-state suppliers are counted once or per state, and whether Sam's Club and non-resale suppliers are included. Not stated on the pages.
- **Dollar General's OTIF fine rate:** one search, none found. **Best Buy:** not attempted (§2.3).

**Tooling:**
- The scholarly-search MCP server was not connected.
- SEC EDGAR files were downloaded directly with a declared user agent; `data.sec.gov` submissions were used to locate the latest 10-Ks.
- Most retailer rules were read through WebFetch page extraction, which returns a model's summary of the page with quotes. That is one more reason vendor-page rules stay *assumed*.
