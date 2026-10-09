# S5 check AS, adversarial review

- **What this is:** an adversarial check of check AS's web evidence, done so that coincidences are pruned and faulty web data is thrown out before the C-09 re-run uses it. Each claim was tested to see whether it breaks. No objection was invented: a claim that survives is reported as a result too.
- **File checked:** `research/s5_check_AS_c09_market_models.md` (80 ledger rows, C-AS01 to C-AS81 with C-AS59 unused; the §0 verdicts; the body sections; the Coincidence watch). It was not edited.
- **Date:** 2026-10-08. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.** It proposes no price and no fee form for C-09.
- **Searches used:** 10 of the 10 allowed (listed in §7). **Fetches made:** 91 page and PDF downloads with curl, each in its own scratchpad directory; 1 header-only request (the Vendr redirect); 2 fetch-tool attempts (Gusto, both HTTP 403); 2 Wayback availability queries (refused, HTTP 429). Two Wayback copies were read (Gusto's R&D pricing page; an Ingham County resolution). Downloads are kept in the session scratchpad, outside the project.
- **No identity was sent. Nobody was contacted.** Pages were fetched with a generic browser user-agent and no identifying headers. No logins, sign-ups, pricing or demo forms, API keys or PACER. SEC EDGAR was not fetched.
- **Rows checked in full (all seven tests that apply):** 48. These are the 40 load-bearing (Y) rows plus 8 N rows that feed a §0 verdict or the §AS3 count (C-AS11, 21, 24, 46, 65, 66, 67, 70).
  - **Sampled (at least existence and the quote):** 29 rows, covering AS1, AS2 and AS3: C-AS08, 13, 18, 19, 20, 23, 25, 28, 30, 31, 33, 36, 48, 53, 55, 56, 57, 61, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 80.
  - **Not checked:** 3. C-AS16 has no URL in the file (cited from check AN). C-AS17 rests on a Capterra snippet with no URL (Capterra returns 403). C-AS74 rests on a snippet of a PDF the file reports as 404.
  - **Also re-read:** all 35 vendor pages behind the §AS3 hours-saved flags, scanned for time and labour wording.
- **How labels are used here:** **KEEP-verified** means the row's own sentence is true as written about its own population: a vendor's own list price or its own wording, or a public contract. Where only "what the vendor says" is verified, the New label says so. **KEEP-assumed** means the number is a vendor's claim about others, an aggregator's figure or a search snippet.

**Words used here:**
- **Share / take rate / contingency:** the vendor is paid a percentage of money recovered or saved.
- **Customer files:** the customer's own staff send the dispute or claim to the counterparty (carrier, retailer, telecom company, tax authority).
- **Identified / realized:** a saving someone says exists, against a saving that has actually come back.
- **Headline / secondary:** check AS's own rule (§AS3): headline means the page title, the navigation tagline or the top statistics; secondary means elsewhere on the page.
- **Look-alike:** two equal-looking numbers or words that measure different things.
- **DocuSign envelope stamp:** the envelope ID line an e-signature service prints on each page of a signed document.
- **Legacy contract:** a renewal with the incumbent vendor, awarded without competition.
- **Tax-credit software:** software that finds tax credits a business can claim (for example the federal R&D credit) and prepares the paperwork. The business claims the credit on its own tax return.

---

## §0 Result in one table

**Row verdicts**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|
| 61 | 9 | 7 | **0** | 3 |

**No row is discarded.** Every quote that was re-fetched is in its source word for word (the Riverside PDF is a scan, so its text has OCR noise), and every [our calc] reproduces. What breaks is how some findings are read:
- **Claim (a), the absence, has two partial exceptions.** One is inside the file's own scope: SSI's parcel customers request the refunds themselves, and SSI still charges a contingency fee. The other is outside the eight markets: tax-credit software (Gusto) charges "15% of identified tax credits" while the business files its own return.
- **Claim (b) holds only where a vendor states its method.** Gusto bills on credits it has itself *identified*. Several contracts bill "when you receive the credit" without saying how receipt is checked.
- **Claim (c) is true as written, but it is not the only public buyer.** Ingham County (Michigan, 2009) paid a monthly fee *plus* 50% of recoveries. Miami-Dade's stated reason is that it "already pays fixed or recurring fees" for the audit.
- **Claim (d):** Vendr's cloud fee ranges contradict themselves on the same page. Tangoe's 20% pays a people-led advisory team, not the software.
- **AS3:** two of the five "headline" flags are not headlines, three N vendors carry time wording, and "sold on money only" mislabels the N group.

**Verdicts on the §0 question rows**

| Question | Proposed verdict | This review | Reason |
|---|---|---|---|
| **AS1** published prices | Answered for list prices (narrowed) | **AGREE**, with three corrections | Every list price re-read matches. **AuditRes's $2,500 a month is the price of one unit,** and "a unit maps to a scoped workspace tied to that category's volume". The listing has 0 ratings, and no other web presence was found (§1 #7). nShift's product page now says "Pricing scales with the size of your freight operation" (a hint at the price's basis, not a price). Lojistic's EDI fees run $15-35 a month, not $15-30. |
| **AS2a** customer files + share | Narrowed (absence in public pricing) | **AGREE**, narrowed further | SSI's parcel arrangement is an in-scope look-alike, and §0 omits it (the file set it aside in its Coincidence watch). Tax-credit software is a category where the customer files and the vendor takes a share. EasyPost is misplaced in the "customer files" column (§1 #1, #9). |
| **AS2b** how a recovery is confirmed | Narrowed | **AGREE**, with a sixth route | Add **"fee on the vendor's own identified amount"** (Gusto). "Every share-billing example reads the counterparty's record itself … or validates receipt" (What the web could not settle #4) overstates. Woodstock 2025, WAI and SSI's parcel fee bill on receipt and do not say how receipt is checked. SPS's matching quote is not tied to its share billing (§1 #3, #4). |
| **AS2c** share on top of a subscription | Narrowed (one public buyer) | **AGREE with the verdict; the reading needs narrowing** | Exhibit 1 is quoted exactly and governs (also under Article 2's order of precedence). But the county's reason is double payment: Core Services are those "for which the County already pays fixed or recurring fees". The deal is a non-competitive legacy renewal. Ingham County paid a $4,000 monthly fee *plus* 50% of cost recovery (2009). The Exhibit pages carry no DocuSign stamp (§1 #2, §4.1). |
| **AS2d** share levels | Narrowed | **AGREE**, two corrections | Vendr's page gives $5M+ cloud spenders both "20–28%" and "23–27%", so cite about 20-35% overall. Tangoe's 20% is not a "software involved" share: it pays Tangoe's Advisory Services team, which takes "the lead on all aspects", while the platform's own audits are suspended (§1 #5, #6). |
| **AS3** hours-saved flags | Answered (wording as published) | **PARTLY AGREE**, counts and reading need correcting | Wording quotes are exact. **But:** Trax's "Eliminate 80%" sits in a role card, and Arcadia's "save time, money, and carbon" is a blog-post teaser; neither is a headline. Under the file's own rule, Trans Audit ("save time, money"), OverDeduct ("No time to DIY? Have us recover it for you") and Ownwell (DIY "5-20+ hours" vs "Minimal") carry time wording. Kuebix and Cass say "operational efficiency" (Spendflo's "efficiency" was marked unclear). Consistent counts: **Y 22 (3 headline, 19 secondary), unclear 3, N 10.** The reading that share-billed vendors "sell mostly on money" does not hold (§1 #10). |

---

## §1 Discards and narrowings (most important first)

No row is discarded. Seven ledger rows are narrowed, and seven body statements need the same treatment. They are ordered by how much they bear on the kill condition and the fee-rule question.

| # | Claim ID or place | What was claimed | What the source actually says (quote ≤40 words) | Verdict | Why, and the restricted reading |
|---|---|---|---|---|---|
| 1 | **§0 AS2a; §AS2.1 "not found"; What the web could not settle #1** (rows C-AS22, C-AS66) | (a) No software where the customer files and the vendor takes a share, in eight markets including "freight and parcel" | SSI: "For parcel billing, our process promptly provides you the information you need to request the refunds directly from your small-parcel carrier." "SSI receives payment via a nominal contingency fee based on the recoverable refunds." | **NARROW** | **SSI's parcel line is in scope** (§0 names "freight and parcel"). Its customer requests the refunds, and SSI's stated fee is a contingency. The file noted this only in its Coincidence watch and set it aside as "parcel … outside the comparison". **Outside the eight markets,** Gusto's R&D service (archive, June 2025) says "Pay 15% of identified tax credits". There, "proprietary software finds and calculates your credits", experts review, and the study is filed "with your income tax return" by the business. A law firm's page calls this "a common version" of success-fee SaaS (§6 #2). **Restricted reading:** no product was found that leaves a dispute against a *commercial counterparty* to the customer and bills a share of *confirmed* recoveries. Two partial exceptions exist. SSI's parcel fee ("recoverable refunds") is undefined. Tax-credit software bills on identified credits, the counterparty is a tax authority, and experts review the work. The absence is narrower than "none in eight markets". |
| 2 | **§0 AS2c; §AS2.4 [our call]; §AS2.7 #3** (rows C-AS37, C-AS41) | (c) A public buyer refused a share on billing-error credits while paying a platform fee, which "bears directly on" a subscription-plus-share form | Exhibit 1 §2(a): "Core Services are services included in the Contractor's base software, platform functionality, and standard audit and management services for which the County already pays fixed or recurring fees." | **NARROW** (rows stay KEEP-verified) | The exclusion is quoted exactly, and Exhibit 1 governs. Appendix A also outranks Appendix B under Article 2. But: (i) the stated reason is **double payment** for work the platform fee already covers; (ii) the deal is a **non-competitive legacy renewal**, and the memo puts replacement at "$2.5 million to $3 million"; (iii) **Ingham County, Michigan (2009)** agreed to "50% of any cost recovery for their initial base audit" *and* "a $4,000 monthly fee" (§6 #4); (iv) Exhibit 1's pages lack the DocuSign stamp found on pp. 1-28 (§4.1). **Restricted reading:** one county, locked in to its vendor, refused a share on billing-error credits *because its platform fee already paid for the audit that finds them*. Another county accepted a monthly fee plus a 50% share (2009). Nothing here is from a private shipper. |
| 3 | **§0 AS2b; §AS2.7 #2; What the web could not settle #4** | (b) Where a share is billed, the recovery is confirmed from a record the vendor reads itself, or after approval and validated receipt; "every share-billing example" does so | Woodstock (NY) 2025 telecom-audit agreement: "The fee for obtaining credits or refunds is fifty (50%) percent of the credit or refund. This portion of the fee is payable when you receive the credit or refund." | **NARROW** | The five routes are real, and **no case of a share billed on customer self-report alone was found** (this part survives). But: Gusto bills a share of credits **it has identified**, with no confirmation of a realized recovery (§6 #1). Woodstock's contract, WAI ("Refund checks from carrier payable to you") and SSI's parcel fee are all due on receipt, and none says how receipt is checked. **Restricted reading:** where a share-billing vendor *states* its method, it reads the counterparty's record or validates receipt. Several share contracts do not state a method, and one software-led share is billed on the vendor's own identification. |
| 4 | **C-AS34** (SPS as a route-1 example in §AS2.3 and §0 AS2b) | SPS confirms recoveries from remittance records it reads itself | SPS: "Automatically match payments to invoices and deductions, with recovery and dispute status data ready for reconciliation. Reduce manual cash application, keep ERP records accurate". Pricing FAQ: "SPS Revenue Recovery offers flexible pricing options to fit your business needs." | **NARROW** | The quote is exact. It describes cash application in the customer's books. Nothing on SPS's pages ties it to confirming a recovery before a take rate is billed, and the take rate itself is only a G2 snippet (C-AS35). **Restricted reading:** SPS's software matches remittances to deductions; its fee basis and confirmation method are not public. Also on the page: "Software handles the disputing", so SPS's software files. |
| 5 | **C-AS51** and §0 AS2d "23-27% at $5M+" | Vendr's deal data: 30-35% of savings at $200K-$500K, 28-30% at $1M-$5M, 23-27% at $5M+ | Same page, two figures for the same band: "Fee percentage: 20–28% of realized savings (negotiated based on volume)" and "those with $5M+ spend commonly achieve 23–27%". | **NARROW** | The quotes in the file exist, but the page contradicts itself. It also gives "25–30%" for buyers above $1M. It calls itself a mix of "ProsperOps's published pricing with Vendr's dataset" and mentions a "pricing analysis agent", although ProsperOps publishes no rate. **Restricted reading:** one data-company page, apparently machine-assembled, puts ProsperOps's share at about 20-35% of realized savings, falling with cloud spend; the bands are not reliable. |
| 6 | **§AS2.2 and §0 AS2d** (Tangoe among "share levels where software is involved") | Tangoe is a hybrid of a platform fee plus a 20% share where the "Software" or vendor acts | Appendix A §3.A.2: Tangoe shall "Take the lead on all aspects of the audit and optimization project, including project management, analysis, and Vendor interaction." | **NARROW** | Additional Terms A: "lifecycle audit services, if any, will be suspended … until such a time as the Tangoe Advisory Services team has completed its Services". **Restricted reading:** the 20% pays a people-led advisory audit attached to a software contract. It is not a share charged by software. |
| 7 | **C-AS12; §AS1.4 #2** (AuditRes "publish[es] an audit price in full") | AuditRes lists its freight line at $2,500 a month as a fixed subscription | "Each product line is sold as units covering the invoice audit, evidence, and recovery work for one spend category. A unit maps to a scoped workspace tied to that category's volume." | **NARROW** | The price and the no-share sentence are exact. But $2,500 is the price **per unit**, and units scale with volume. The listing shows "0 ratings" and says "production readiness … vary by product". A search found no other web presence (§6 #11). **Restricted reading:** one seller's listed unit price for a freight workspace, with no evidence anyone buys it. |
| 8 | **C-AS44** (and §AS2.5 "Buyer's experience") | A 2011 county survey: "The alleged savings is difficult to document"; another county's savings were "under $10,000" | Edgefield's answer: "We have saved $23,500 in monthly bills over the last 18 months." Colleton, the county quoted, answered "no" to realizing savings, and paid "30% of the alleged savings. For us, that was about $15K." | **NARROW** | Quotes exact, but selective. Four of the five counties that hired an auditor answered "yes" to realizing savings: Berkeley under $10K a year; Edgefield $23,500 over 18 months; Hampton $2,268 one-time and $15,340 a year net of fees; Jasper about $21,000 over two years. **Restricted reading:** one county of five paid 30% (about $15K) on savings it says it never saw; the other four report modest realized savings. |
| 9 | **C-AS66; §AS2.1 parcel row** (EasyPost in the "customer files" column) | EasyPost states the split: software by subscription or per claim, services 25-50% | "You connect carrier accounts; the platform flags discrepancies and files claims. You pay a subscription or per-claim fee and keep what's recovered." | **NARROW** | In EasyPost's words, the subscription software **files the claims itself**. So it does not support "a subscription goes with the customer doing it". It is a counter-case to "a share goes with the vendor's software filing". **Restricted reading:** EasyPost (parcel, vendor) contrasts software that files, priced by subscription, with firms that file, priced at 25-50%. The split it states is software against service, not customer against vendor. |
| 10 | **§AS3 count and reading; §0 AS3** (rows C-AS67, C-AS70) | 19 Y (5 headline: MyCarrier, Freightview, Trax, Glimpse, Arcadia), 15 N "sold on money only", 1 unclear. Share-billed vendors "sell mostly on money" | Trax: the line sits under "Procurement Leader" in a role-card section, beside "Eliminate 80% of manual contract verification work"; its top statistics are "$25B in transportation spend managed", "25+ years", "125+". Arcadia: "Blog One energy platform for businesses to save time, money, and carbon" | **NARROW** | **Trax and Arcadia are secondary,** not headline. Arcadia's line is a blog-post teaser; its flag stands on "No manual processing". **N vendors with time wording on the pages read:** Trans Audit, "A freight audit company can help organizations of all sizes save time, money, and improve carrier relations"; OverDeduct, "No time to DIY? Have us recover it for you" and "Brands with no time to fight deductions"; Ownwell, "Time required: 5-20+ hours" for DIY against "Minimal". **Unclear:** Kuebix ("improve operational efficiencies") and Cass ("power operational efficiency"), by the rule applied to Spendflo. **Consistent counts:** Y 22 (3 headline: MyCarrier, Freightview, Glimpse; 19 secondary), unclear 3, N 10. "N" means no time wording was found, not "sold on money only": Kuebix's page sells TMS features. **Reading:** among share-billed vendors, Lojistic, SSI, Trans Audit, OverDeduct, Glimpse (headline), Tangoe, ProsperOps and Ownwell carry time wording, and Eller, Liberata, nOps, Zesty, Archera and MD Clarity do not. Glimpse is share-billed (*assumed*), not subscription-priced, and Trax and Loop publish no price. **No pattern by price form is shown.** |

**Smaller body corrections (verdicts unchanged)**

- **B1. §0 AS2a lists Kuebix among products "where the customer files or acts"**, but §AS1.1 says who files at Kuebix is "Not stated". Drop it from that list, or mark it unknown.
- **B2. §AS1.1 row 7 and §AS1.2:** Lojistic's EDI connections cost $35 a month on the free account and $30/$25/$20/$15 on the paid rungs. The crossovers ignore these fees, and also the $29 history add-on on the contingency rung. They are list-price crossovers only.
- **B3. §AS1.4 #3 and What the web could not settle #1:** nShift's product page today says "Pricing scales with the size of your freight operation". This hints that the price will follow operation size, not a share. It is not a price.
- **B4. C-AS11 can be upgraded.** nShift's own blog says: "Audit starts to show its best value from around EUR 1.5 million a year in freight spend across several carriers." Read at the source, so *verified* as nShift's statement.
- **B5. C-AS32's origin is now traced.** The "$1,000 per month … 10% on won disputes" line comes from an AI-written company profile (Extruct). It names Glimpse's real clients and distributor add-ons, so the name-collision worry eases, but it is still one aggregator. A search summary of another aggregator gives "$100/month". Stays *assumed*.
- **B6. §AS2.3 route 1 (ProsperOps).** ProsperOps's help page says its "Base Savings" include "inherited or customer-procured Standard Reserved Instances, Convertible Reserved Instances which ProsperOps has not optimized". So ProsperOps bills on some savings from the customer's own purchases, read from the provider's bill. This is the trap Archera describes (§AS2.6), applied to ProsperOps by its own words.
- **B7. Coincidence watch "Two 'share where the customer acts' look-alikes".** The reason given for setting SSI aside ("parcel is outside the comparison") conflicts with §0, which counts "freight and parcel" as one of the eight markets. Report SSI in §0 (see #1).

---

## §2 Coincidences found

**Shared origins (merge them into one source)**

| Figures | Rows | Single origin | Effect |
|---|---|---|---|
| 3-7% (or 5-7%) of freight spend recoverable | C-AS09, C-AS70; Eller (N-AS21) | nShift's RFP pack cites "DataIntelo and MarketIntelo market research, 2026; Journal of Commerce benchmark study, 2020"; its product page adds Forrester and Drewry. Eller's page: "Trax Technologies cites 5–7% … AFS Logistics claims up to 8%" | Confirms the file's "partly circular" note. Eller adds nothing independent. |
| Glimpse "$1,000 per month … 10% on won disputes" | C-AS32 | One AI-written company profile (Extruct, undated) | One origin. Another aggregator, seen only as a search summary, gives a $100 entry price. Unconfirmed. |
| ProsperOps fee bands | C-AS51 | One Vendr page that "combines ProsperOps's published pricing with Vendr's dataset" | Internally inconsistent (§1 #5). vendr.com/pricing still answers HTTP 301 to vertice.one/pricing (re-observed). |
| 25% (and 20-50%) on recovery | C-AS26, 47, 60, 61, 62, 63, 66 | Convention among services that file: OverDeduct "below the 25–35% most contingency auditors charge"; ClearChain "Most chargeback firms take 20–30%"; RevRecoup outsourced "20–50%"; EasyPost 25-50%; Ownwell 25-50%; Woodstock 50% | Confirms the file's circular-risk warning. These are service rates, and they do not support a software share. |
| "Keep 100%" | Coincidence watch | Marketing trope | Not limited to subscription software. ClearChain, a service that files, says "You keep 100% of every dollar we recover". RevRecoup's self-collection software says "No percentage fee on Collect". |
| SCAC survey | C-AS44 | One survey, five county answers | Five answers in one document, not five studies. |

**Look-alike numbers and words (equal on the surface, different underneath)**

| Value | Where it appears | What each measures |
|---|---|---|
| "Identified" as a fee base | Gusto: "15% of identified tax credits"; Tangoe: "Identified Savings" are only "presented to Customer … for review and approval" (no fee); SSI: "recoverable refunds"; OverDeduct: "amounts actually recovered"; Miami-Dade: "verified reduction of actual County expenditures" | Five different fee triggers, from the vendor's own calculation to a verified cut in spending. **Compare fee rates only on the same trigger.** |
| "Self-service" / "self-serve" | MyCarrier: "fully self-service. You do not need a sales call"; Jarvio: "Self-service tools … you submit the claims"; EasyPost: "audit software" where "the platform … files claims" | Turned on without sales; the customer files; the software files. Three meanings. |
| "Subscription" / flat fee | MyCarrier Invoice Hub (the customer files); ClearChain $5,000 a month (the vendor files); AuditRes (per unit, scaled by volume) | A flat price says nothing about who files. |
| 50% | Woodstock 2025 (credits and 12 months of reductions); Ingham 2009 (initial-audit recoveries); Red Bank 2010 (credits to $20,000) | The same telecom-audit service convention. These are not three independent price points. |
| "Up to 99%" / 75% recovery | SPS Recovery Estimator: "SPS Commerce's recovery percentage is up to 99%"; a search summary: "as much as 75%" | Vendor ceilings, not rates. |

**Circular or indirect citations**
- C-AS16 (FreightVerify), C-AS19's Cass figure (N-X14) and the other "cited, not re-read" IDs were not re-checked here. Their URLs are not in the checked file.

---

## §3 Arithmetic re-done

All **[our calc]** in check AS reproduce. Rows marked "new" are calculations added here, on the same sources.

| Item | Check AS | Recomputed | Result |
|---|---|---|---|
| §AS1.2 annual list prices | $1,788; $720 / $2,400; $828 / $3,036; $30,000 (+$11,940); $71,508 | 149×12; 60×12, 200×12; 69×12, 253×12; 2,500×12, 995×12; 5,959×12 | ✓ (AuditRes is per unit, §1 #7) |
| C-AS15 Lojistic crossovers | $990; $2,900; $61,889 | 99 ÷ 0.10 = 990; 290 ÷ 0.10 = 2,900; 5,570 ÷ 0.09 = 61,888.9 | ✓ (EDI and history fees excluded, B2) |
| C-AS26 OverDeduct crossover | $3,960 a year | 990 ÷ 0.25 = 3,960; the vendor's page states "about $3,960" | ✓ |
| C-AS29 ClearChain | 3x = $15,000 a month; $60,000 a year | 5,000 × 3; 5,000 × 12; the page says "$60K flat" | ✓ |
| C-AS37 / C-AS43 Miami-Dade fees | $296,400 a year; $1,482,000 over 5 years | 24,700 × 12 = 296,400; × 5 = 1,482,000 | ✓ |
| C-AS43 in-scope spend | $16.3M | 6.3 + 9.6 + 0.2 + 0.2 = 16.3 | ✓ |
| C-AS43 platform share of spend | ≈0.7%; all-in ≈1.8% | (4,300 + 5,000) × 12 = 111,600 ÷ 16.3M = 0.685%; 296,400 ÷ 16.3M = 1.818% | ✓ (the all-in figure includes UCaaS, which is outside the audit scope: §4.3) |
| **new:** Miami-Dade variable telecom fee | — | "1.00% of County's annual Telecom Spend in excess of $14,000,000": at $16.3M, about +$23,000 a year | Illustrative; the fees quoted in AS are minimums |
| Months of saving paid as fee | Tangoe 2.4; Des Moines 8.1; Red Bank 12 and 10.8 | 0.20×12; 0.45×18; 0.50×24; 0.45×24 | ✓ |
| **new:** Woodstock 2025 | — | 50% × 12 months of reduction = **6.0 months** of the saving | Public contingency, 2025 |
| **new:** Ingham County 2009 | — | $4,000 × 12 = $48,000 (matches the resolution); ÷ ($84,000 × 12 = $1.008M telecom a year) = **4.8%** of telecom spend as a fixed fee, plus 50% of initial-audit recovery | Compare Miami-Dade's platform at about 0.7% of in-scope spend |
| C-AS44 SCAC, Colleton | ≈$50K alleged | $15K ÷ 0.30 = $50K | ✓ |
| §AS3 count | 19 + 15 + 1 = 35 | 35 | ✓ as counted; under a consistent rule, 22 + 10 + 3 = 35 (§1 #10) |
| C-AS51 Vendr example | 30-35% | The page's own example: $100,000 of savings → $30,000-35,000 fee | ✓ (bands inconsistent, §1 #5) |

---

## §4 Concerns, unproven (verdicts unchanged)

1. **Miami-Dade Exhibit 1's signature status.** Contract pp. 1-28 each carry a DocuSign envelope stamp, and pp. 29-31 (Exhibit 1) carry none. Their footers also differ ("9/22" against "Rev. 8.14.25"). Whether Tangoe signed the exhibit is not shown. The Board adopted the package on 21 April 2026, and the base agreement covers "all other appendices and attachments hereto", so the county's position is documented either way.
2. **The county's leverage.** The memo calls the deal a "Non-Competitive Legacy Contract" and says competition "is not practicable at this time". A locked-in buyer may negotiate differently from a private shipper choosing a new tool. The direction of the effect is unknown.
3. **C-AS43 "all-in about 1.8%".** It divides fees that include UCaaS ($15,400 a month) by the audit addendum's telecom spend. UCaaS is not among the in-scope audit vendors. The ratio mixes bases.
4. **Arcadia's page has moved.** The URL check AS read (`/solutions/utility-bill-management`) now redirects to `/utility-expense-management`. The version AS read may have shown the tagline differently.
5. **What the time wording sells.** OverDeduct's, ClearChain's and Ownwell's time wording sells handing the work to the vendor's staff. It does not sell hours cut by software. Whether that falls under the founders' paid-hours rule is the founders' call, not this review's.
6. **SSI's currency.** The summary sheet's footer carries a 2019 date, and the web page is undated. Whether SSI still runs the parcel arrangement, and what "based on the recoverable refunds" means in practice, could not be checked.
7. **Gusto's terms.** The current pricing and terms pages returned 403 to both curl and the fetch tool. The 15% rests on an archive copy of 15 June 2025. A search summary says the accountant-facing page words it as "up to 15%".
8. **Ingham County's arithmetic.** "$48,000 minus recovery annually" may mean the monthly fee was offset against recoveries. The underlying contract was not found.
9. **ClearChain's claim about software** ("60% of the dashboard alerts age out unactioned") is a service vendor's statement about its rivals. It bears on follow-through under D-23 but is unmeasured.
10. **Trans Audit's time sentence** describes "a freight audit company" in general, on its own page. It is flagged because the file flagged Freightview's equally generic line.

---

## §5 Full verdict table

**Source key** (the URLs behind the short names in the Evidence column):
- [FVP] https://www.freightview.com/pricing · [FVA] https://blog.freightview.com/introducing-auditing-with-freightview · [FVH] https://www.freightview.com/
- [MCP] https://go.mycarrier.io/plans-and-pricing · [MCB] https://go.mycarrier.io/blog/tips-for-setting-up-invoice-hub-essentials · [MCF] https://go.mycarrier.io/fast-ltl-freight-audit-and-payments · [MCD] https://help-center.mycarriertms.com/en/articles/12460685-creating-disputes · [MCQ] https://help-center.mycarriertms.com/en/articles/12455590-invoice-hub-faq-s
- [FPP] https://www.freightpop.com/pricing · [FPA] https://www.freightpop.com/freight-auditing-software
- [KB] https://www.freightwisellc.com/kuebix · [KBH] https://help.kuebix.com/knowledge-base/freight-pay-audit-process-flow/
- [NSR] https://nshift.com/hubfs/nShift-Audit-RFP-pack.pdf · [NSP] https://nshift.com/products/audit · [NSN] https://nshift.com/newsroom/nshift-announces-nshift-audit-ai-powered-freight-invoice-audit · [NSB] https://nshift.com/blog/freight-audit-checklist-before-the-first-invoice
- [AR] https://aws.amazon.com/marketplace/pp/prodview-5o5ck2jqrtkiw · [LJ] https://lojistic.com/pricing · [IA] https://www.intelligentaudit.com/ · [CASS] https://www.cassinfo.com/freight-audit-payment
- [NOP] no-price pages: https://shipwell.com/pricing/ (now redirects to a demo-request page) ; https://www.ratelinx.com/freight-audit/ (redirects to a resources page) ; https://www.smartfreight.com/pricing (redirects to the homepage) ; https://www.transimpact.com/ ; https://www.echo.com/shippers/echoship (redirects to the homepage) ; https://www.loop.com/ ; https://www.traxtech.com/
- [FS] https://www.freightsimple.com/ · [LOC] https://locus.sh/blogs/freight-audit-settlement-software-buyers-guide-2026.md
- [SSI] https://ssui.com/contingency-parcel-freight-invoice-audits/ (and the summary sheet https://ssui.com/wp-content/uploads/2020/11/SSI-contingency-freight-audit-services.pdf)
- [TA] https://transaudit.com/freight-audit-company/ · [EL] https://www.elleraudit.com/ltl-freight-audit · [WAI] https://waionline.com/freight-post-audit
- [ODP] https://overdeduct.com/pricing · [ODH] https://overdeduct.com/how-contingency-works · [ODT] https://overdeduct.com/terms
- [CCF] https://useclearchain.com/faq · [CCP] https://useclearchain.com/pricing · [GL] https://www.tryglimpse.com/ · [EXT] https://www.extruct.ai/hub/tryglimpse-com/
- [PM] https://promomash.com/pricing?hsLang=en (redirects to /plans) · [SPS] https://www.spscommerce.com/products/revenue-recovery/ · [SPS1] https://www.spscommerce.com/products/revenue-recovery/1p/
- [HR] https://www.highradius.com/product/deductions-management-software/ (redirects to a landing page) · [VHR] https://www.vendr.com/marketplace/highradius · [VPO] https://www.vendr.com/marketplace/prosperops
- [MD] https://www.miamidade.gov/govaction/legistarfiles/Matters/Y2026/260241.pdf · [SCAC] https://sccounties.org/sites/default/files/uploads/services/research/surveys/11/telecom-utility_auditing.pdf · [RB] https://www.redbanknj.org/DocumentCenter/View/10325/10-241 · [DSM] https://councildocs.dsm.city/communications/1998/98-015.pdf · [RIV] https://media.rivcocob.org/proceeds/2026/p2026_01_27_files/03.10001.pdf
- [LIB] https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-15/documents/92302/532464089949551-pricing-document-2026-01-30-0718.pdf · [HCD] https://www.healthcaredive.com/press-release/20260323-strategic-audit-solutions-expands-auditsuite360-platform-with-launch-of-ema/
- [POP] https://www.prosperops.com/pricing · [POH] https://help.prosperops.com/how-does-prosperops-bill · [NOPS] https://www.nops.io/pricing/ · [ZES] https://zesty.co/pricing/ · [ARC] https://archera.ai/pricing
- [VER] https://www.vertice.one/pricing · [VROI] https://www.vendr.com/resources/roi · [SPF] https://www.spendflo.com/pricing · [MDC] https://www.mdclarity.com/comparison/best-healthcare-underpayment-recovery-services
- [RG] https://revenuegeeks.com/amazon/fba-reimbursement-tools · [JAR] https://jarvio.io/best-amazon-reimbursement-tools · [REDO] https://redo.com/resources/articles/comparisons/best-chargeback-management-software
- [OW] https://www.ownwell.com/blog/property-tax-consultants-how-to-choose · [AD] https://www.appealdesk.com/compare/appealdesk-vs-ownwell · [EP] https://www.easypost.com/blog/parcel-audit-software/
- [ARCA] https://arcadia.com/solutions/utility-bill-management (redirects to /utility-expense-management) · [TAN] https://www.tangoe.com/telecom-expense-management/invoice-audit-optimization/

**Tests:** 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search or counter-fetch, 7 arithmetic.

| Claim ID | Verdict | New label | Evidence (source + quote ≤40 words) | Note |
|---|---|---|---|---|
| C-AS01 | KEEP-verified | *verified* (list price) | [FVP]: "0-50 ships per month $149 / mo 51-500 ships per month Call now" | Tests 1-5. Trial and annual-billing lines also present |
| C-AS02 | KEEP-verified | *verified* | [FVA]: "This add-on tool is available by request" ; "You can challenge the cost and submit the dispute back to your carrier, you must provide the contact email." | Tests 1-5. Help page "Last updated on 17 Jul 2026" |
| C-AS03 | KEEP-verified | *verified* (list price) | [MCP]: "$60 / month" ; "$200 / month" ; "Invoice Hub + Precision Payments … Contact for Pricing" | Tests 1-5 |
| C-AS04 | KEEP-verified | *verified* | [MCB]: "Invoice Hub Essentials is fully self-service. You do not need a sales call or a custom quote to turn it on." ; "Up to 50 shipments a month Up to 100 shipments a month" | Tests 1-5. "Self-service" means activation (§2) |
| C-AS05 | KEEP-verified | *verified* (that it says so); $88 *assumed* | [MCF]: "Catching only ONE overcharge can pay for the entire month's Invoice Hub subscription." ; "$88 The average amount of unexpected charges" | Tests 1-4. "20 - 30%" is a "Percentage of invoices that contain surprise charges", no origin |
| C-AS06 | KEEP-verified | *verified* | [MCD]: "Click Email Dispute to kick things off." [MCQ]: "to alert you of new invoices and re-bills" | Tests 1-3. [MCF] adds "track dispute outcomes" |
| C-AS07 | KEEP-verified | *verified* | [FPP] table code: row "Carrier Invoice Audit" has fa-times, fa-times, fa-times, fa-check; "Unlimited freight shipments / month at a metered price. Pay for what you use." | Tests 1-5 |
| C-AS08 | KEEP-verified | *verified* | [KB]: "$69 /month Single User, Single Location Up to 100 rate quotes per month." | Test 1. Not the customer-files list (B1) |
| C-AS09 | KEEP-verified | *verified* | [NSR] p. 7: "Pricing is confirmed at general availability. The demo comes with a tailored quote sized on your operation" | Tests 1-6. [NSP] now: "Pricing scales with the size of your freight operation." (B3) |
| C-AS10 | KEEP-verified | *verified* | [NSP]: "send it to the carrier from the platform or download it as a PDF to send yourself. The whole exchange stays in one thread until you mark it resolved." | Tests 1-5. [NSR] p. 5: "Nothing is filed without your approval." |
| C-AS11 | KEEP-verified | *verified* (nShift's statement; upgraded from *assumed*) | [NSB]: "Audit starts to show its best value from around EUR 1.5 million a year in freight spend across several carriers." | Tests 1, 2 (B4) |
| C-AS12 | **NARROW** | *verified* (list unit price); as a market price *assumed* | [AR]: "A unit maps to a scoped workspace tied to that category's volume." ; "0 ratings" | Tests 1-6 (§1 #7) |
| C-AS13 | KEEP-verified | *verified* | [AR]: "passed 514 automated tests with zero failures" ; "does not represent this documentation as a SOC 2 report" | Test 1 |
| C-AS14 | KEEP-verified | *verified* (list price) | [LJ]: "Contingency 29 % Of Recovered Refunds" ; "Starter $ 99 /month Plus 19 % of Recovered Refunds" ; "Unlimited $ 5,959 /month 0 % of Recovered Refunds" | Tests 1-5. EDI $15-35, not $15-30 (B2). Instant connections use "your carrier account username and password" |
| C-AS15 | KEEP-verified | **[our calc]** ✓ | (calculation from C-AS14) | Test 7 (§3) |
| C-AS16 | not checked | unchanged | — | No URL in the file |
| C-AS17 | not checked | unchanged | — | Snippet; Capterra 403 |
| C-AS18 | KEEP-assumed | *assumed* | [IA]: no price on the homepage; "Spend less time and recover more with our turnkey claims management program." | Test 1 on the homepage; Gartner snippet not re-read |
| C-AS19 | KEEP-verified | *verified* (absence) | [NOP] and [CASS]: no monthly, per-user or per-invoice price on any of these pages | Test 1. Shipwell, SmartFreight and Echo pricing URLs now redirect to demo or home pages |
| C-AS20 | KEEP-verified | *verified* | [FS]: "We audit all bills and challenge incorrect charges automatically." | Test 1 |
| C-AS21 | KEEP-assumed | *assumed* | [LOC]: "Three models are common: contingency share of recoveries, per-invoice processing fees, and platform or module licensing. Blends are frequent." | Tests 1-4. Its table pairs "Contingency share of recoveries" with a "Post-payment recovery service" (§6 #12) |
| C-AS22 | KEEP-verified | *verified* | [SSI]: "submit the claims to recover your refunds, and confirm refunds and credits upon receipt. For parcel billing, our process promptly provides you the information you need to request the refunds directly" | Tests 1-6. The row is right; its parcel half bears on claim (a) (§1 #1) |
| C-AS23 | KEEP-verified | *verified* (that it says so) | [SSI]: "you have zero upfront costs, which may expedite decision making by your team" | Test 1 |
| C-AS24 | KEEP-verified | *verified* | [TA]: "At Trans Audit, we bill based on a percentage of the monies we retrieve." | Tests 1-4. Same page: "save time, money" (§1 #10) |
| C-AS25 | KEEP-verified | *verified* | [EL]: "Your first audit is free. You only pay when we recover money." | Test 1 |
| C-AS26 | KEEP-verified | *verified* (list price) | [ODP]: "Self-serve deduction management software is $49/mo (Starter) or $99/mo (Pro), month-to-month" ; "Done-for-you recovery We file; you pay 25% on recovery." | Tests 1-5, 7 |
| C-AS27 | KEEP-verified | *verified* (that it says so) | [ODH]: "Software subscriptions charge monthly regardless of results and still leave you to do the disputing." ; "Contingency is paid only out of recovered dollars, after the fact." | Tests 1-4 |
| C-AS28 | KEEP-verified | *verified* | [ODT]: "we are paid an agreed percentage of amounts actually recovered, as set out in a separate service agreement" | Test 1. "Effective August 10, 2026" |
| C-AS29 | KEEP-verified | *verified* | [CCF]: "If we don't recover at least 3x your fee, you get your money back." ; "Read-only access to your retailer portals (Retail Link, Partners Online, Vendor Central, etc.) is enough." | Tests 1-5, 7. ClearChain files ("We do the work") with a flat fee |
| C-AS30 | KEEP-verified | *verified* | [CCF]: "A senior in-house deductions analyst runs $120–160K fully loaded" | Test 1 |
| C-AS31 | KEEP-verified | *verified* (that it says so) | [GL]: "80 % Reduction in Labor Hours" ; "More revenue, same headcount" | Test 1. Top statistic, so headline holds |
| C-AS32 | KEEP-assumed | *assumed* (one aggregator; origin traced) | [EXT]: "The pricing structure includes a platform fee of $1,000 per month, along with a commission of 10% on won disputes." | Tests 1-6 (B5) |
| C-AS33 | KEEP-verified | *verified* (that it says so) | [PM]: "we have found that the basic SaaS support model is not one that promotes high adoption and success for our clients." | Test 1 |
| C-AS34 | **NARROW** | *verified* (feature); as a confirmation route *assumed* | [SPS]: "Automatically match payments to invoices and deductions, with recovery and dispute status data ready for reconciliation." | Tests 1-6 (§1 #4) |
| C-AS35 | KEEP-assumed | *assumed* | [SPS1]: "SPS Revenue Recovery offers flexible pricing options to fit your business needs." (no rate or model on SPS's own pages) | Tests 1, 6. G2 not re-tried |
| C-AS36 | KEEP-assumed | *assumed* | [VHR]: "Median contract value $12,973 per year" | Test 1 |
| C-AS37 | KEEP-verified | *verified* | [MD] App. B: "a one-time contingency fee of 20% of Realized Savings resulting from the optimization and audit findings recommended by Tangoe and approved by Customer for implementation with the Vendor" | Tests 1-7. Also: "Actual billed amount will be the greater of: (i) the Minimum Monthly Fee or (ii) total devices under management" |
| C-AS38 | KEEP-verified | *verified* | [MD] App. A §3.F: "Tangoe shall invoice Customer for its fees when requested credits are approved by the Vendor and validated by Tangoe as received by the Customer." | Tests 1-5 |
| C-AS39 | KEEP-verified | *verified* | [MD] App. A §3.A.7: "Verify that the expense reduction and or credit are reflected in Vendor's subsequent billing." | Tests 1-5. §3.B.8's 10 business days exact |
| C-AS40 | KEEP-verified | *verified* | [MD] Additional Terms E: "the greater of $200/hour times the hours expended on the project or the full contingency fee associated with all Audit and Optimization Savings identified" | Tests 1-5. 24-month tail (Terms D) and Audit Exclusions (§4.a) exact |
| C-AS41 | KEEP-verified | *verified* | [MD] Exh. 1 §3(a): "Billing Discrepancies are expressly deemed part of Core Services. No performance-based or contingency fee shall apply to credits, refunds, or corrections resulting from billing discrepancies." | Tests 1-6. Reading narrowed (§1 #2); signature concern (§4.1) |
| C-AS42 | KEEP-verified | *verified* | [MD] Exh. 1 §2(d): "Have been approved in writing by the County; Have been implemented by the County and/or its service providers; and Result in a verified reduction of actual County expenditures." | Tests 1-5. §8: "The County reserves the right to audit all calculations" |
| C-AS43 | KEEP-verified | *verified*; ratios [our calc] ✓ | [MD] App. C: "Savings Target $300,000 Measurement The first 12 months of the Initial Term of this Schedule" | Tests 1, 7. All-in ratio mixes bases (§4.3) |
| C-AS44 | **NARROW** | *verified* (survey answers) | [SCAC] Edgefield: "We have saved $23,500 in monthly bills over the last 18 months." | Tests 1-7 (§1 #8) |
| C-AS45 | KEEP-verified | *verified* | [RB]: "$1.00 to 20,000.00 50%" ; "$0.00 to 500.00 50% multiplied by 24" | Tests 1-5, 7 |
| C-AS46 | KEEP-verified | *verified* | [DSM]: "Telcon' s fee is 45 percent of all one-time savings (refunds), and 45 percent of all recurring savings for the first 18 months" | Tests 1, 2, 7 |
| C-AS47 | KEEP-verified | *verified* | [LIB]: "The fee is calculated as a percentage of the total value of recoveries achieved." ; "Standard Fee 25% Minimum Fee 12.5%" | Tests 1-5. "our service teams will undertake recovery action" |
| C-AS48 | KEEP-verified | *verified* (that it says so) | [HCD]: "keeping 100% of recoveries rather than paying contingency fees to third-party recovery auditors" | Test 1. "Currently deployed within the healthcare sector" |
| C-AS49 | KEEP-verified | *verified* | [POP]: "ProsperOps takes a small percentage of the realized savings, as determined by your provider's billing system — not a percentage of your cloud spend." | Tests 1-5 |
| C-AS50 | KEEP-verified | *verified* | [POH]: "Base Savings are the monthly savings generated from all other compute discount instruments (e.g., Savings Plans, and inherited or customer-procured Standard Reserved Instances …)" | Tests 1-6 (B6) |
| C-AS51 | **NARROW** | *assumed* | [VPO]: "Fee percentage: 20–28% of realized savings (negotiated based on volume)" against "those with $5M+ spend commonly achieve 23–27%" | Tests 1-7 (§1 #5) |
| C-AS52 | KEEP-verified | *verified* | [NOPS]: "nOps Cost Visibility & Allocation is priced as a flat, predictable fixed fee based on your cloud spend. For Autonomous Rate Optimization, you pay only a percentage of savings realized." | Tests 1-5 |
| C-AS53 | KEEP-verified | *verified* | [ZES]: "Pricing based on actual usage and realized savings." | Test 1 |
| C-AS54 | KEEP-verified | *verified* (own terms); rivals *assumed* | [ARC]: "Most tools charge a percentage of your savings across every commitment you hold, including the native ones you purchased sometime before you signed." | Tests 1-6. Premiums "appear as a line item on your existing cloud invoice" |
| C-AS55 | KEEP-verified | *verified* (wording); baseline *assumed* | [VER]: "Cost savings contractually guaranteed" ; "50% Reduction in purchasing time" | Test 1. Baseline snippet not re-read |
| C-AS56 | KEEP-verified | *verified* (that it says so) | [VROI]: "an average of 17.13%" ; "Up to 80% faster negotiations" | Test 1 |
| C-AS57 | KEEP-verified | *verified* | [SPF]: "Platform fee + per completed request" | Test 1 |
| C-AS58 | KEEP-verified | *verified* (that it says so); range *assumed* | [MDC]: "taking a percentage (typically 20 to 35 percent) of recovered revenue. There are no upfront fees, and the vendor is only paid when dollars actually land back in the provider's bank account." | Tests 1-4. The confirmation method is not stated |
| C-AS60 | KEEP-assumed | *assumed* (affiliate) | [RG]: "Sellerboard does not offer an end-to-end claim process. Instead, it identifies potential reimbursement opportunities, allowing you to handle the claims yourself." | Tests 1-6. All prices in the table match. The page also lists Sellerise at "0% Fees", where the seller files "with the software's assistance" |
| C-AS61 | KEEP-assumed | *assumed* | [JAR]: "Self-service tools like Jarvio and Sellerboard show you the opportunities but you submit the claims." | Test 1 |
| C-AS62 | KEEP-assumed | *assumed* (rivals); *verified* (Redo's own $0) | [REDO]: "None of these numbers share a definition of a win, a time period, or a denominator" ; "Disputifier 20% of recovered revenue, capped at $250 per case" | Tests 1-5. Redo itself "files before the bank's deadline" at $0 |
| C-AS63 | KEEP-verified | *verified* (each on itself) | [AD]: "AppealDesk provides a $49 DIY evidence packet; you file and handle any hearing." [OW]: "Some contracts calculate contingency on multi-year "projected savings" rather than your actual first-year reduction." | Tests 1-5. [OW]: "At 25% contingency (Ownwell's rate)" |
| C-AS64 | KEEP-assumed | *assumed* | [AD]: "claimed I would save $600 on my property taxes, the actual savings were $55. Plus, they charged their 25% fee on the $600" | Tests 1-4. A competitor quoting a review |
| C-AS65 | KEEP-verified | *verified* | [RIV] (scanned): "22o/o of all recovered revenue" ; "annual amount not to exceed $250,000" | Tests 1, 2 |
| C-AS66 | **NARROW** | *assumed* | [EP]: "You connect carrier accounts; the platform flags discrepancies and files claims. You pay a subscription or per-claim fee and keep what's recovered." | Tests 1-3 (§1 #9) |
| C-AS67 | **NARROW** | *verified* (wording); headline → secondary | [ARCA]: "Blog One energy platform for businesses to save time, money, and carbon" ; "No manual processing." | Tests 1, 2, 5 (§1 #10, §4.4) |
| C-AS68 | KEEP-verified | *verified* | [TAN]: "Gain Productivity Tangoe acts on savings opportunities, handling invoice corrections, managing vendor disputes, and automating service modifications." | Test 1 |
| C-AS69 | KEEP-verified | *verified* (that it says so) | [NOP] Loop: "Discover how automation can free your staff from tedious manual workflows." | Test 1 |
| C-AS70 | **NARROW** | *verified* (wording); headline → secondary | [NOP] Trax: "Procurement Leader Eliminate 80% of manual contract verification work." | Tests 1, 2 (§1 #10) |
| C-AS71 | KEEP-verified | *verified* | [FPA]: "No clerks required to move data between systems." | Test 1 |
| C-AS72 | KEEP-verified | *verified* (that it says so) | [MCP] navigation: "Audit invoices and resolve disputes 90% faster" | Test 1 |
| C-AS73 | KEEP-verified | *verified* | [IA]: "Spend less time and recover more with our turnkey claims management program." | Test 1 |
| C-AS74 | not checked | unchanged | — | Snippet; PDF 404 per the file |
| C-AS75 | KEEP-verified | *verified* | [FVH]: "Save time and money quoting, booking and analyzing Truckload, LTL and Parcel shipments with Freightview." | Test 1 |
| C-AS76 | KEEP-verified | *verified* | [SSI]: "Reduce administrative overhead – focus on what you do best" | Test 1 |
| C-AS77 | KEEP-verified | *verified* (that it says so) | [HCD]: "Accounting and Finance teams are under more pressure than ever to do more with less" | Test 1 |
| C-AS78 | KEEP-verified | *verified* | [POP]: "Automate cloud savings and minimize FinOps effort" | Test 1 |
| C-AS79 | KEEP-verified | *verified* | [LJ]: "Lojistic handles disputes, fixes recurring billing errors, streamlines payment, and eliminates manual work" | Test 1 |
| C-AS80 | KEEP-verified | *verified* | [HR]: "Automatically write off valid deductions with high confidence, reducing manual effort." [SPS]: "Finance spends hours logging into retailer portals" | Test 1 |
| C-AS81 | KEEP-verified | *verified* | [WAI]: "Claims filed and handled completely by us in your name." ; "Refund checks from carrier payable to you." ; "All you pay is a percentage of the amount recovered." | Tests 1-4. The confirmation method is not stated (§1 #3) |

---

## §6 Counter-evidence and leads

These are logged, not new findings. Each is tied to the claim it bears on. Search-summary items are marked *assumed*.

| # | Source | What it says (quote ≤40 words) | Ties to | Type |
|---|---|---|---|---|
| 1 | Gusto, R&D Tax Credit Services pricing (archive copy of 15 June 2025): https://web.archive.org/web/20250615215701id_/https://gusto.com/product/pricing/r-and-d | "Pay 15% of identified tax credits." "Our proprietary software finds and calculates your credits while our experts review your information for compliance. CPAs then produce your tax credit study to file with your income tax return." | (a), (b), (d) | **Counter-evidence (partial).** A share where the customer files (its own return), billed on identified credits. Expert-reviewed. Current page 403 (§4.7) |
| 2 | Law-firm page on success-fee SaaS: https://terms.law/SaaS-Agreements-Hub/success-fee-saas/ | "A common version analyzes payroll data to surface federal tax credits and then takes a cut of the credits the customer actually claims." Also: the fee "earned on a claimed credit" against "a credit that survives". | (a), (b) | Counter-evidence (category level, *assumed*: a seller of legal services) |
| 3 | ADP SmartCompliance R&D Tax Credits: https://apps.adp.com/en-US/apps/628915/ADP%20SmartCompliance%C2%AE%20R&amp;D%20Tax%20Credits/features | "ADP applies fees based on a percentage of the R&D tax credits successfully captured. Employers pay only if and when ADP secures the identified eligible R&D tax credits." | (a) | Lead. Expert-led ("ADP's tax credit specialists"), so not a clean software case |
| 4 | Ingham County (Michigan) Board resolution 09-117, adopted 28 April 2009 (archive): https://web.archive.org/web/20101216125753id_/http://ingham.org/BC/BC/INDEX/2009/09-117.htm | "Ingham County will agree to pay SpyGlas fees equal to 50% of any cost recovery for their initial base audit" ; "will also pay a $4,000 monthly fee for a period of one-year" | (c) | **Counter-evidence.** A public buyer paying a monthly fee plus a share (telecom expense management) |
| 5 | Town of Woodstock (NY), telecom-audit agreement, 21 August 2025: https://woodstockny.gov/download_file/769e0cc0-4f8a-4ef0-a671-dde427a985a8/991 | "The fee for obtaining credits or refunds is fifty (50%) percent of the credit or refund. This portion of the fee is payable when you receive the credit or refund." | (b), (c), (d) | Corroboration (a public buyer pays a share on billing credits, 2025; a service, no platform fee); the confirmation method is not stated |
| 6 | RevRecoup pricing (B2B collections): https://revrecoup.com/pricing | "Self-collection is creditor-controlled software." ; "No percentage fee on Collect" ; outsourced: "20–50% Pay only on money actually recovered" | (a) | **Corroboration in a ninth market:** customer acts → $0/$299/$999 a month; specialist acts → share |
| 7 | SSI page [SSI] | "SSI receives payment via a nominal contingency fee based on the recoverable refunds. We only get paid when you get paid." | (a), (b) | Counter-evidence (in scope, parcel; §1 #1) |
| 8 | EasyPost blog [EP] | "Audit software usually charges a subscription or per-claim fee, which lets you keep 100% of the recovery." (software that "files claims") | (a) split | Counter-evidence to "the vendor's software files → share" |
| 9 | ClearChain FAQ [CCF] | "a brand pays $2K/month for a deduction dashboard, nobody on the team has time to work the queue, and 60% of the dashboard alerts age out unactioned." | Follow-through under D-23 | Lead (vendor claim about rivals, *assumed*) |
| 10 | San Diego Independent Budget Analyst report 11-32 (June 2011): https://www.sandiego.gov/sites/default/files/11_32.pdf | "Some audit firms will help their clients develop "self-audit" capabilities by evaluating payment data and providing the client with exception reporting. This allows the client to validate possible errors and directly investigate and/or recover overpayments" | (a) | Lead: a customer-recovers model in AP audit; its fee is not stated |
| 11 | Search 10 (AuditRes) | Only the AWS listing was found; no website, founding date or customer list | C-AS12 | Lead (interest, currency) |
| 12 | Locus guide [LOC] | "Typical pricing | Contingency share of recoveries | Per invoice or platform | Platform or module" (columns: post-payment recovery service; pre-payment audit software; settlement integrated with execution) | (a) split | Corroboration (vendor): the split falls between service and software |
| 13 | nShift product page [NSP] | "Pricing scales with the size of your freight operation. A demo includes a tailored quote sized on your operation and a view of your likely recovery range." | AS1, AS2a | Lead (B3) |
| 14 | Miami-Dade memo [MD] p. 2 | "Replacement of the existing TEM System is estimated to cost between $2.5 million to $3 million" ; "Competition for these services is not practicable at this time" | (c) | Context (§4.2) |
| 15 | Tangoe addendum [MD] App. A, Additional Terms A | "lifecycle audit services, if any, will be suspended for in-scope Vendors processed by the TEM system until such a time as the Tangoe Advisory Services team has completed its Services" | (d) | Context (§1 #6) |
| 16 | SPS [SPS] ; Glimpse [GL] | "Software handles the disputing and surfaces trends automatically." ; "Glimpse wins money back, automatically. You don't have to lift a finger." | (a) classification | Corroboration: both vendors' software files, as AS classed them |
| 17 | Search 8 (demurrage and detention dispute tools), summary only | No D&D dispute product with a published share was found; one carrier portal's dispute features were reported as free | (a) in a freight-adjacent market | Corroboration (*assumed*) |
| 18 | FourOneOne "D and Defender" (D&D evidence tool): https://fouroneone.io/ | "Use the proof to dispute D&D charges. Free dispute generation included - no extra cost." | (a) | Lead, unresolved. The customer disputes; the price is not on the page, the pricing URL returned HTTP 500, and a search summary reports inconsistent "Pay only for results" wording |

---

## §7 Could not access, and searches

**Blocked or unusable:**
- **Gusto** (curl 403; fetch tool 403 twice): the current R&D pricing, terms and accountant pages. Read instead on an archive copy of 15 June 2025.
- **Indie Hackers** post on "a tool that takes 25% of the money it recovers" (403): who files there is unknown.
- **Ingham County**'s original URL (404): read on an archive copy of 16 December 2010.
- **FourOneOne / Provar** pricing URL (HTTP 500).
- **Wayback availability API** (429, twice): archive copies were reached by direct URL instead.
- **Not tried, because the checked file reports them blocked:** G2, Capterra and Gartner (C-AS17, the Gartner part of C-AS18, the G2 part of C-AS35), and the PHTI PDF (C-AS74).
- **No URL in the checked file:** C-AS16 (N-AN14) and the "cited, not re-read" IDs (N-Z36, N-Z43, N-Z78, N-Z83, N-AK47, N-AN07, N-AN08, N-AN10, N-AA29, N-X14, N-AE34, N-AI16, N-AI26, N-AI33, N-AI35).
- **SEC EDGAR** (by rule). Cass's per-item fee (N-X14) was not re-checked.
- **Redirects observed (content still served):** Arcadia; Shipwell pricing → demo request; SmartFreight pricing → homepage; Echo EchoShip → homepage; RateLinx → resources page; HighRadius → a landing page; Promomash → /plans. vendr.com/pricing → vertice.one/pricing (HTTP 301).

**Searches run (10):**
1. R&D tax credit software fee percentage of the credit company claims credit on its own return payroll tax offset pricing
2. underpayment detection software "percentage of recovered" OR "percent of recovered" provider staff submit appeals in-house software pricing contingency license
3. self-serve recovery software "success fee" customer submits disputes itself "only pay" when credit received overcharge detection tool percentage of recovered credits
4. Gusto R&D tax credit "15%" identified credits fee Form 6765 who files help center
5. SPS Commerce Revenue Recovery pricing "take rate" OR "percentage of recovered" OR "flat fee per retailer" deductions
6. tryglimpse Glimpse deductions recovery pricing commission monthly fee CPG "Glimpse" "$1,000" OR "10%" won disputes
7. telecom expense management contract county OR state OR city "contingency fee" billing error credits refunds plus monthly platform fee Tangoe OR Calero OR Sakon OR Brightfin agenda pdf 2024 2025
8. demurrage detention dispute software pricing "percentage of" savings OR "success fee" shipper submits disputes itself self-serve D&D invoice audit
9. "nShift Audit" pricing general availability October 2026 price per invoice OR subscription OR "percentage"
10. "AuditRes" invoice audit overpayment recovery platform company

**Counter-search for claim (a), in sum:** five of the ten searches (1-4, 8) looked for software that takes a share while the customer files. They found tax-credit software (Gusto, ADP) where the business files its own return and the vendor takes a share of identified or captured credits. They also found more evidence of the split in collections (RevRecoup), in demurrage and detention, and in healthcare underpayments, where Clear Health publishes no price. Nothing was found for a dispute against a commercial counterparty.

**Not searched (budget):**
- Work Opportunity Tax Credit screening software prices.
- Utility-bill audit software with a share where the customer contacts the utility.
- Healthcare revenue-cycle software priced as a percentage of collections.
- Apex Analytix or PRGX self-service software prices.
- More public telecom-audit contracts from 2020-2026 with both a platform fee and a share.
- Whether nShift Audit has reached general availability with a public price (search 9 found none).
