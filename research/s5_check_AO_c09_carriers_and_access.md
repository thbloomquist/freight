# S5 check AO: carriers, data access and interview logistics (C-09)

- **What this is:** desk research for card C-09 on the open questions in `C09-business-proposal.md` §8. The founders asked: "find any web resources you can as to answers to these questions", with "adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data". This file covers H09-C1, H09-C2 and H09-C4 (the carrier side), A09-11 (will shippers share rate agreements and invoices), and facts for three founders' decisions: D-16 (incentives), D-18 (data handling) and D-19 (the time box).
- **Builds on, not redone:** check Z §10 and §13 (U.S. Bank carrier agreement R 9.2020, FAP portals, quick-pay and factoring snippets, carrier anecdotes); check AK §2.3, §4.2 and §5 (carrier dispute channels and claim forms, the UPS and FedEx parcel third-party clauses, TForce's payer-only web page, ODFL's $50 fee); check T §3.2, §4 and §6 (tariff proof rules, 49 U.S.C. 13710 and 14705, 49 CFR 378); check AL §7 (security asks, AI data terms); check AC §3.1, §6 and §9 (the YRC–First Brands and SEFL agreements, the data request list); check V §8.2 and §9 (panel prices, incentive norms, cold-email rates). Those are cited by their IDs (N-Z…, N-AK…, N-T…, N-AL…, N-AC…, N-V…).
- **Date:** 2026-10-07.
- **Status:** input to S5. **It decides nothing.** An adversarial check of this file follows (`research/s5_check_AO_adversarial.md`).
- **Adversarial review (2026-10-07):**
  - All 87 rows checked: 71 KEEP-verified, 9 KEEP-assumed, 6 NARROW (C-AO32, C-AO37, C-AO40, C-AO51, C-AO74, C-AO86) and 1 DISCARD (C-AO47, struck through in the ledger).
  - The reviewer agreed with every §0 verdict and suggested wording fixes.
  - **Where the review and this file differ, the review's restricted readings govern** (`s5_check_AO_adversarial.md` §1).
- **Re-checked at the source by the coordinator (2026-10-07), all matching the review:**
  - TForce 102-T Item 130 is quoted word for word;
  - the IRS 1099 instructions (Rev. Dec 2026) give a $2,000 threshold, "adjusted for inflation beginning in calendar year 2027";
  - FedEx Freight Item 435-2B (the 3% card charge) is listed in the Intra-Canada Section 2B column of the tariff's contents, so C-AO47 is discarded for US use.
- **Searches used:** 28 web searches of the 40 allowed. About 45 page or PDF reads, plus 7 read-only queries to CourtListener's free search API and 4 to GitHub's public API (not counted as web searches).
- **No identity was sent. Nobody was contacted.** No logins, sign-ups or form submissions. SEC EDGAR was not fetched. Downloads sit in the session scratchpad under `AO/downloads/`, outside the project folder.
- **Labels:**
  - *verified*: read at the source. For a company's own published terms (a tariff, a fee page, a form), it means the company says it; for a vendor's claim about the market, the claim is *assumed* even when read at the source.
  - *assumed*: a vendor's market claim, an association figure, a search snippet or a secondary summary.
  - **[our calc]**: arithmetic, shown.
  - **[our call]**: judgement.
- **New sources:** N-AO01 to N-AO44 (§Sources). Re-read existing sources keep their IDs.

---

## Words used here

| Word | Meaning |
|---|---|
| **Short pay** | Paying less than the invoice total, leaving a balance the carrier must chase |
| **Offset (set-off)** | Deducting a claim the payer has against the carrier (an overcharge, a damage claim) from a *different* bill the payer owes |
| **Overcharge claim** | A written request for a refund of charges already paid, filed with the carrier under 49 CFR 378 |
| **Rules tariff** | A carrier's published rulebook (credit terms, fees, claim rules). It applies unless a written contract says otherwise. Its sections are called **items** |
| **Pricing agreement** | The shipper's negotiated discount, minimums, accessorial prices and fuel table with one carrier |
| **Credit period** | The days a carrier lets a payer take to pay. Federal default 15 days, maximum 30 (49 CFR 377.203) |
| **Liquidated damages** | A pre-set penalty for late payment, stated in the tariff as a percentage or as loss of the discount |
| **Discount revocation** | The penalty where a late payer must pay the full, undiscounted ("class") rate instead of its negotiated discount |
| **Quick pay** | A payer (usually a broker) pays the carrier early in exchange for a fee taken off the invoice |
| **Factoring** | A carrier sells its invoices to a finance company for cash now. **Recourse:** the carrier repays if the customer does not pay. **Non-recourse:** the factor bears some non-payment risk |
| **Dilution** | A factoring term: any reduction of a receivable other than cash, such as short pays, disputes or offsets |
| **FAP** | Freight audit and payment provider (Cass, U.S. Bank, CT Logistics…) that checks and pays carrier bills for shippers |
| **Freight payment processor / "Bill-To"** | FedEx Freight's term for a bank or FAP designated to pay freight charges for a shipper |
| **LOA / POA** | Letter of authority (or authorization) / power of attorney: a signed letter letting an agent act for the shipper |
| **Bond of indemnity** | A promise on a claim form to repay the carrier if a duplicate claim is later presented with the original bill |
| **Guarantee refund** | A refund of charges when a guaranteed or time-definite delivery is late |
| **NDA / MNDA** | Non-disclosure agreement / mutual NDA (both sides protect each other's information) |
| **DPA** | Data processing agreement: the contract for handling personal data |
| **1099-MISC** | The IRS information return a business files for certain payments to individuals |
| **Nacha** | The body that writes the rules for ACH (US bank transfer) payments |
| **Panel** | A paid research-recruiting service (User Interviews, Respondent) |

---

## §0 Summary

| Question | What the web says now | Best evidence | Label | **Proposed verdict** |
|---|---|---|---|---|
| **H09-C1a** · Carriers' published rules on short pays, offsets and disputes | Nine of the ten LTL rules tariffs read bar offsets or withholding in so many words; R+L's has no offset item (full-text search) but penalises non-payment. Saia: "Short payment or taking credit for any freight bills by any party is not permitted." Penalties for unpaid bills: discount revocation (Saia automatically at credit-period expiry; Estes after notice; XPO and R+L on referral to collection), or 25-35% liquidated damages (SEFL, ABF, ODFL, AAA Cooper). FedEx Freight: invoices *not* disputed through its channels are due on terms | N-AO01 to N-AO10; 49 CFR 377.203 (N-AO15) | *verified* | **Answered from the web** (published rules of ten LTL carriers and one TL/brokerage group) |
| **H09-C1b** · How carriers handle short pays in practice, how often, at what cost | FAPs short-pay routinely with stated reasons and weekly short-pay reports (a large shipper's 2014 guide). Factoring underwriters treat short pays as "dilution"; trucking dilution under 3% is the norm in one association deck. No carrier-side count or cost of chasing was found | N-AO16, N-AO17 | *verified* (documents); norm *assumed* | **Not answerable from the web** (narrowed) |
| **H09-C2** · Would carriers pay for faster payment; what they pay today | Broker-published quick pay: RXO 2.5% (QuickPay), 4.0% (Advance Pay); Werner 2.5% next day or 1.5% in 5 days; Con-way Multimodal 2008: 3% immediate, 2% in 7 days. U.S. Bank: Quick Pay "for a fee" on 45-90-day shipper terms (fee on file: 1% base). Big LTL carriers instead *charge* payers 2-3% for card payments. **Parked in part:** v1 is audit-only (founders, 2026-10-03) | N-AO20 to N-AO23, N-AO02, N-AO07; N-Z47 | *verified* (published terms) | **Narrowed** (TL carriers hauling for brokers pay 1.5-4%; whether carriers billing a shipper directly would pay a new rail is not answerable from the web) |
| **H09-C4** · How carriers treat an outside audit firm's claims | **New:** two LTL carriers' tariffs exclude third parties from *guarantee refunds* (FedEx Freight Items 756, 757, 760; TForce Items 822, 823, 825, 826). AAA Cooper: overcharge claims "must be submitted by the responsible party". ODFL and TForce close a claim once ruled or settled, so a second auditor cannot reopen it. XPO wants the pricing agreement attached. The law still lets an agent file (49 CFR 378.2(f), on file). **No carrier statement about audit firms as such was found** | N-AO02, N-AO01, N-AO10, N-AO04, N-AO26 | *verified* | **Narrowed** |
| **A09-11** · Will shippers share rate agreements and paid invoices under an NDA | **Confidentiality is contractual, not just a mood.** TForce Item 130 binds customers and "the agents of the customer" and requires notice to "any Third Party or auditor"; disclosure needs a written permission. FedEx Freight Item 250 allows disclosure only when "required by law". A FedEx parcel agreement template requires FedEx's consent **and** an NDA between FedEx and the third party. The one negotiated shipper contract read (YRC–First Brands) carves out "auditors … assessing the accuracy of freight charges". 8 of 10 LTL rules tariffs carry no rate-confidentiality item. Shipper reluctance: one public statement (2020) | N-AO01, N-AO02, N-AO12, N-AC05, N-AO13 | *verified* | **Narrowed** (the clause can be read; whether a shipper says yes is only answerable in the interview — Test 2) |
| **D-16 (a)** · Tax reporting of incentives | IRS: for payments after 2025 the 1099-MISC threshold for "other income", prizes and awards is **$2,000** a year per payee. Medical-research study payments are named under box 3; market-research interviews are not named | N-AO32 | *verified* | **Answered from the web** |
| **D-16 (b)** · Gift caps and incentive norms | Published supplier codes ban cash and cash equivalents from current **or prospective** suppliers (Flex, $25 cap) or allow non-cash under $50 (DRiV). No mid-sized manufacturer's code found. A commercial researcher offers $150 for a 60-minute industry interview. Incentive norms on file (check V) | N-AO33 to N-AO35; N-V23, N-V24 | *verified* (codes); norms *assumed* | **Narrowed** |
| **D-18** · NDA templates, authority forms, retention norms | An open mutual NDA (Common Paper v1.0, CC BY 4.0) lets the recipient share with advisers and contractors on a need-to-know basis, but **lets it keep copies under backup or retention policies** unless the cover page changes that. Its DPA returns or deletes personal data at the customer's instruction. A published audit firm LOA template exists (Logistics Plus). Nacha requires large ACH users to make account numbers unreadable in storage. No freight-audit NDA form or published retention period was found | N-AO36, N-AO37, N-AO28, N-AO38, N-AO30 | *verified* | **Answered from the web** for templates; **Narrowed** for retention norms |
| **D-19** · Time to recruit and response rates | Panels: User Interviews medians 77 minutes to first qualified applicant and 24 hours to first confirmed session (via a partner's help page); Respondent claims a first qualified participant in 15 minutes. Cold email: medians 0.74% (Smartlead, 850M+ emails) and 1.5% (Woodpecker, 56,614 campaigns), via an agency page; the much-quoted 3.43% is attributed to two different vendors. Nothing specific to finance, logistics or carrier owners with a disclosed method | N-AO39 to N-AO42 | *assumed* | **Narrowed** |

---

## §AO1 · H09-C1: how carriers handle short pays and disputes

### AO1.1 What the rules tariffs say (ten LTL carriers, one TL/brokerage group)

Every rule below is the carrier's default. A written contract overrides it (e.g. ODFL 360.4, TForce Item 100 ¶4; on file, check T).

| Carrier, tariff, version | Offset or short pay | Credit period | Penalty for not paying | Source |
|---|---|---|---|---|
| **Saia** 170-D, eff. 2025-10-01 | Item 435 Sec. H: pay "without offset for any cause, including … overcharge claims". Item 1030 ¶7: "Short payment or taking credit for any freight bills by any party is not permitted." | 15 days net, 30 days courtesy | Item 435 Sec. C: **all discounts revoked** at expiry of the credit period, "automatically … without the need for Carrier to reinvoice". Sec. B: 25% (61-90 days, min $132.50); 50% (over 90 days, min $265.00) | N-AO05 pp. 45, 47, 146 |
| **XPO** CNWY 199-AK.1, eff. 2026-02-16 | Item 23(5) and BOL terms ¶9: no right "to withhold or offset … for any reason". Item 207: "An invoice dispute is insufficient grounds for debtor to withhold payment of any other valid invoices." | 15 days from invoice | Item 207: 10.00% late fee, min $50.00 per shipment every 30 days beyond terms; **all discounts revoked** when placed with a collection agency, attorney or authorised agent | N-AO03 pp. 18, 31 |
| **Estes** EXLA 105, eff. 2026-01-02 | Item 825: "not permitted to offset any part of the freight charges by the value of any outstanding loss and damage, overcharge or over-collected claims" | 30 days from invoice | Item 720: 10% service charge (min $21.00) after written notice; then **full undiscounted class rates**; 30% collection fee "calculated on the gross, undiscounted charges" | N-AO06 pp. 63, 76 |
| **R+L** rules tariff, updated 2026-10-05 | No offset item found (full-text search for "offset", "set-off", "deduct", "withhold") | Not read (budget) | Item 775, on legal action such as collections: **forfeiture of all discounts**, plus "A penalty of 125% of the remaining freight bill amount", plus attorney fees | N-AO08 p. 117 |
| **ODFL** 100-Q, eff. 2025-04-14 (pages revised to 2026-10-05) | Item 395: may not offset "on any outstanding loss and damage, overcharge, or over collected claim" | 15 days (Item 434) | Item 564: **35%** liquidated damages if not paid within 42 days of the original invoice due date; credit revocable "at its sole discretion" (Item 434 ¶4) | N-AO04 pp. 38, 42, 64 |
| **ABF** 111-AU, 2026-06-22 | Item 427 ¶3: no offset or delay for "any overcharge claim, charge back, duplicate payment or loss and/or damage cargo claim" | 15 days | Item 427 ¶2B: **30%** late fee when sent to an outside collection agency or attorney | N-AO07 p. 33 |
| **SEFL** 1090, Item 817 eff. 2021-03-01 | ¶6: no offset or delay "unless a formal claim is filed and has been finally processed" | 15 days | ¶4: **25%** liquidated damages when sent to collection or attorney; ¶7 prevailing-party attorney fees | N-AO09 p. 128 |
| **TForce** UPGF 102-T, eff. 2026-03-16 | Item 166 Part 13 and Item 812 Part 1 ¶3: claims "may not be offset"; the shipper "waives … any statutory or common law rights" to set off | 15 days (Item 140) | Item 721: collection costs and attorney fees, plus 1.5% a month from referral to collection | N-AO01 pp. 12, 20, 44, 58 |
| **FedEx Freight** 100-Y, eff. 2026-01-05 (Items 435, 438 revised 2026-06-01) | Item 960 ¶9: no deduction or offset of "any cargo claim or other alleged claim or debt of Carrier … unless authorized in writing by Carrier". Item 438 ¶3: "Invoices not disputed via one of the channels above are due and payable … within the agreed-upon payment terms" | 15 days (Item 435) | Not read in full (budget) | N-AO02 pp. 19, 46 |
| **AAA Cooper** 190-AF, eff. 2025-12-22 | Item 649: no offset of overcharge or damage claims; Item 210 ¶4 | 15 days (Items 210, 650) | Item 210 ¶2: **35%** liquidated damages if not paid within 60 days of the ship date | N-AO10 pp. 12, 33 |
| **Landstar** LAND 100-A (TL and brokerage), eff. 2020-03-15 | Rule 850: payment "is absolute and shall not be affected or reduced by … any setoff or counterclaim" | 15 days (Rule 435) | Not read (budget) | N-AO11 |

**The federal frame** (49 CFR 377.203, N-AO15, *verified*):
- The default credit period is 15 days, and tariffs may not set one "longer than 30 calendar days" ((c), (d)).
- Tariffs may charge late fees, and may impose "liquidated damages" either as a stated percentage or as "the full, nondiscounted rate instead of the discounted rate otherwise applicable" ((g)(1)).
- These may not apply to "clear clerical or ministerial error" such as a bill never received ((g)(2)(iv)). **A dispute about the amount is not listed as an exception** (*verified* by absence in the text).
- Carriers may also offer "discounts for early freight bill payments" ((f)).
- Benesch Law (a transport law firm) notes that publishing rate tariffs is now "only strictly required" for household goods and the noncontiguous trade (N-AO29, *assumed*), so these rulebooks bind through the bill of lading and pricing agreements, not through a filing.

### AO1.2 Worked example: what a short pay can put at risk **[our calc]**

The real ABF bill 150235531 from the practice audit (`s5_practice_audit_public_invoices.md` §3.2, *verified* there):
- linehaul plus deficit weight $6,963.80; discount 89.5% = −$6,232.60; net linehaul $731.20;
- fuel 30.3% of net = $221.55; total billed $942.02.

**If a full-rate rule like Saia's, Estes's or XPO's were applied to a bill of this shape:**
- linehaul rises by the whole discount: **+$6,232.60**;
- fuel, if charged at the same 30.3% on the gross linehaul, rises from $221.55 to 30.3% × $6,963.80 = $2,110.03, so **+$1,888.48**;
- the bill rises from $942.02 to $942.02 + $6,232.60 + $1,888.48 = **$9,063.10, about 9.6 times** ($9,063.10 ÷ $942.02 = 9.62).

**Under ABF's own rule** (a 30% fee on the unpaid amount), short-paying the $149.10 lumper line and letting it go to collection would add 30% × $149.10 = **$44.73**.

**Caveats [our call]:**
- No tariff read says whether discount revocation applies to the whole bill or only the unpaid part. That is a question for a carrier's credit team or a lawyer.
- 49 CFR 377.203(g)(2)(vi) requires the carrier to issue a revised bill or notice within 90 days after the credit period. Penalties are therefore not instant everywhere: Estes gives 10-20 days after its notice.
- This is a ceiling for a bill that goes unpaid, not an expected cost.

### AO1.3 How short pays happen in practice (what the documents show)

| Item | What was found | Label, source |
|---|---|---|
| **A shipper's FAP short-pays routinely** | J&J's carrier guide (its FAP is CT Logistics; "Last Updated: January 2014"): "Short pay Reports – available weekly reports on all invoices that are short paid and the reasonings". Unknown rates mean the invoice "will be short paid or delayed indefinitely". Bills needing carrier input sit in "Carrier Web Resolution" for 30 days, then "will be rejected". "Balance dues must be approved before submitting". The shipper "cannot accept credits" and wants refund cheques | *verified*, N-AO16. Large shipper: out of segment |
| **Factoring treats short pays as normal "dilution"** | SFNet (the asset-based lending and factoring association): "Dilution is non-cash deductions to A/R (i.e., offsets, short pays, billing errors, discounts, disputes …)". "A trucking company with dilution <3%, the advance rate may be 90% or more." | *verified* as SFNet's training text (© 2020); the <3% figure is an example, not a survey, *assumed*, N-AO17 |
| **The carrier usually bears a disputed short pay even when factored** | FreightWaves (2026-04-21; the page carries a "Sponsored" label, origin unclear): many non-recourse agreements cover "broker bankruptcy or business closure — not a broker who disputes the invoice, claims a short delivery, or simply refuses to pay" | *assumed*, N-AO18 |
| **Government auditors and carriers** | Federal post-payment audit: GSA "issued a notice of overcharge demanding a refund"; the carrier protested; the board held most claims time-barred (GSBCA 14055-RATE, 1998). The government deducts overcharges from later payments under its own statute (not read here, *assumed*); private shippers have no such right under these tariffs | *verified*, N-AO19. Government shipper: out of segment |
| **Carrier anecdotes** | On file: a broker short-paid $300 of $3,000 (check Z, N-Z57); ATRI: fleets are paid on fewer than 50% of detention invoices (N-AB41) | *assumed* / *verified* (on file) |
| **Share of carrier invoices short-paid, and hours to chase** | **Not found** (search 24) | — |

**Reading [our call]:**
- **The rules are settled and one-sided.** No carrier read allows offsets (nine bar them in terms; R+L is silent), Saia bars short payment outright, four carriers impose full-rate pricing on unpaid or collected balances (Saia, Estes, XPO, R+L) and four impose 25-35% liquidated damages (SEFL, ABF, ODFL, AAA Cooper). A disputed short pay is therefore a risk the shipper carries, not a neutral act.
- **Yet FAPs short-pay against the rate file every week** (J&J). The two probably co-exist because the shipper's contract and its FAP's rate file govern, and because carriers may not enforce penalties against a large customer (no evidence either way was found). Whether they enforce against a mid-sized one is an interview question for carriers.
- **For the audit-only v1:**
  - dispute before payment through each carrier's own channel (FedEx Freight Item 438 makes a dispute through its channels the thing that stops the clock);
  - file overcharge claims after payment;
  - **never recommend a short pay or an offset** — this repeats check AK §5.1 with tariff text behind it.
- **Interview asks this suggests (carrier side, kit §5.2):** "The last time a shipper short-paid you, did you apply a late fee, the full rate or a collection fee? Why or why not?"

---

## §AO2 · H09-C2: do carriers pay for faster payment, and how much

**Context:** the founders decided on 2026-10-03 that version 1 is an audit machine only ("we can do payments later"). These facts matter only for a later payments product.

### AO2.1 What carriers pay today

| Who pays the carrier | Offer | Price to the carrier | Label, source |
|---|---|---|---|
| **RXO** (broker), via TriumphPay | Standard Pay (default) / QuickPay / Advance Pay | Free / **2.5% per transaction** / **4.0%** | *verified* (RXO page, modified 2026-03-26), N-AO20 |
| **Werner** (broker arm), via TriumphPay | Standard: within 30 days of invoice, POD and lumper receipts. Quick Pay | **2.5% next day; 1.5% within 5 days**, "deducted from total invoice" | *verified* (Werner page, undated), N-AO21 |
| **Con-way Multimodal** (broker), 2008 form | Immediate Pay / Seven Day Pay | **3% / 2%** | *verified* (PDF dated 2008), N-AO22 |
| **Uber Freight** (broker), quick pay agreement | Pay within two business days | 2% (snippet only; the PDF returned 404) | *assumed*, N-AO25 |
| **U.S. Bank Freight Payment** (shipper's FAP) | Quick Pay for "contracted terms – typically anywhere from 45 and up to 90 days"; carriers "choose the payments they want to accelerate for a fee" | Fee not in the release; the carrier agreement on file sets 1% base, +0.25% to +1.00% by terms (N-Z47) | *verified*, N-AO23 (2020 release) |
| **Loop** (FAP), carrier QuickPay | "offered to carriers to get paid for delivered loads faster for a discounted rate" | Not published | *verified* that Loop says it, N-AO24 |
| **J&J** (large shipper), 2014 | "discount payment terms for our carriers that opt to participate" | Not published | *verified*, N-AO16 |
| **Factoring** (on file) | Advance of 90-95% | 1-5%, "most carriers pay 2% to 3.5%" | *assumed*, N-Z62 |

**The other direction (big LTL carriers):**
- **FedEx Freight** Item 435-2B: card payments carry "an additional 3% handling charge". Item 435 ¶2.C.1: FedEx Freight "reserves the right to adjust discounts based on payment type" (*verified*, N-AO02).
- **ABF** Item 721: a 2% card surcharge, "the same or lower than our cost of acceptance" (*verified*, N-AO07).
- So the big LTL carriers pass payment-acceptance costs to the payer rather than absorb them.

**Worked example [our calc]:**
- On a $2,000 truckload invoice: RXO QuickPay 2.5% = $50; Advance Pay 4% = $80; Werner 5-day 1.5% = $30; U.S. Bank 1.25% on 45-day terms = $25 (check Z's example).
- Paying 2.5% to be paid about 29 days early (next day instead of 30) costs about 2.5% × 365 ÷ 29 = **31% a year** in implied interest.

### AO2.2 Would carriers enrol in a shipper-side payment rail?

| Signal | What it says | Label, source |
|---|---|---|
| Carriers' tariffs make the **shipper** bear the risk of a failed intermediary | ODFL Item 564 ¶6: payment to "a freight forwarder, broker or any other party shall not be deemed as payment received by the Carrier". AAA Cooper Item 210 ¶5: the customer "will pay freight charges twice in the event the third party or broker fails to pay" | *verified*, N-AO04, N-AO10 |
| Carriers already recognise FAPs | FedEx Freight Item 765: "Freight Payment Processor (commonly referred to as “Bill-To”)" | *verified*, N-AO02 |
| Lock-in on an existing rail | U.S. Bank: carriers must route all platform shippers through it or face up to +1% (on file) | *verified*, N-Z47 |
| Carriers' complaints about TriumphPay or FAP rails | **Not found** (search 15) | — |

**Reading [our call]:**
- Carriers hauling for brokers already pay **1.5-4%** for speed. These are verified published prices, but they come from brokers, not shippers: the C-09 carriers who bill a mid-sized shipper directly may face different terms.
- The large LTL carriers *charge* payers 2-3% for card payments, so a rail that asks them to pay looks unlikely. Small TL carriers look like the only plausible payers. That is a hypothesis for interviews, not a finding.
- **Shipper-side risk:** if a payments product came later, the tariffs above make the shipper liable to pay twice should the intermediary fail. That is a trust and insurance question for any payment design.

---

## §AO3 · H09-C4: how carriers treat an outside audit firm's claims

| Rule | Text | Scope | Label, source |
|---|---|---|---|
| **FedEx Freight**, Money-Back Guarantee (Item 760 ¶6, eff. 2026-06-01) | "the Money-Back Guarantee may not be honored when the request is made by, or the information utilized to determine the status of the shipment is determined by, a third party other than the payer" | Guarantee refunds only. The **same wording** as FedEx's parcel terms (check AK §4.2), now in an LTL tariff | *verified*, N-AO02 p. 36 |
| **FedEx Freight** Items 756 ¶5, 757 and 760 ¶7 | Refunds "upon request of the debtor only"; "Carrier will not issue refunds or credits to third parties and/or agencies." | Guarantee and delivery-window refunds | *verified*, N-AO02 pp. 32, 33, 36 |
| **TForce** Items 822, 823, 825, 826 | Item 823 ¶6: "No agent, representative, or third party may request cancellation or refund on behalf of the payer and no refunds will be made to any party other than the payer." Item 826 has the same sentence; Item 825 the same without the second comma; Item 822 (LTL Expedited) says "No agent, representative or third party may request cancellation on behalf of the payor" | Guaranteed and expedited service refunds, 15 days from delivery | *verified*, N-AO01 pp. 62-64 |
| **TForce**, overcharge claims | Web page: "Only the payer of the original freight charges can file an overcharge claim" (on file). Tariff Item 813 sets 180 days and closes a claim once a settlement is accepted, but does not repeat the payer-only rule | Overcharge claims | *verified*, N-AK21; N-AO01 p. 58 |
| **AAA Cooper** Item 660 | Overcharge claims "must be submitted by the responsible party of the freight charges", within 180 days of the shipment date | Overcharge claims | *verified*, N-AO10 p. 34 (check AK had this as *assumed*) |
| **ODFL** Item 396 | Closed 30 days after the initial ruling; "Carrier will not open new overcharge claims on any invoice for which a closed overcharge claim exists"; $50 on settled no-fault claims (on file) | Overcharge claims | *verified*, N-AO04 p. 39 |
| **XPO** claim sheet (2026-02-24) | Invoice must be paid first; "If the claim is related to a pricing agreement or tariff, copies of those documents must also be provided"; "up to 100 PROs at a time"; a "Rebuttal of claim" route | Overcharge claims | *verified*, N-AO26 |
| **FedEx Freight** claim form (Canadian site copy, form PAP201) | One "Name of Claimant" field, no agent field; a **bond of indemnity** signed by "The undersigned" | Overcharge claims | *verified*, N-AO27 |
| **Federal law** (on file) | "Claimant means any shipper or receiver, or its authorized agent" (49 CFR 378.2(f)); a carrier must disclose actual rates on bills presented to the payer "or agent of such responsible person" (49 U.S.C. 13708(a)) | All motor carriers under part B | *verified*, N-T05; N-AO14 |
| **An audit firm's own LOA** (Logistics Plus template, dated 2018-01-01) | Authorises the firm to negotiate LTL rates and "to send invoices that are third-party billed to (Client Name) c/o Logistics Plus Inc. … for auditing and payment purposes on behalf of (Client Name)" | Bill routing; does not mention claims | *verified*, N-AO28 |
| **Carrier statements about audit firms, contingency auditors or automated claims** | **Not found** (searches 11, 12) | — | — |

**Reading [our call]:**
- **Two levels of resistance are now visible in published rules.**
  - **(1) Hard exclusion:** FedEx Freight and TForce bar agents from *guarantee refunds* outright, the LTL analogue of the parcel clauses.
  - **(2) Soft gates on overcharge claims:** AAA Cooper wants the "responsible party" to submit, TForce's web page wants the payer, XPO wants the pricing agreement, and ODFL and TForce allow one shot per invoice.
  - None of these bars an agent who files *in the payer's name* with the payer's documents, which the law allows.
- **Design consequence (repeats check AK, now with tariff text):** prepare claims for the shipper to file, or file in its name under an LOA. Do not build revenue on guarantee refunds. Get it right the first time, because a settled claim closes the invoice.
- **What the web cannot tell:** whether carriers slow, deny or penalise claims that arrive from an auditor's address. That is the carrier-interview probe already in kit §5.2 and check Z probe 13.

---

## §AO4 · A09-11: will shippers share rate agreements and invoices under an NDA?

### AO4.1 Confidentiality clauses that bind the shipper

| Document | Clause | Does it allow disclosure to the shipper's auditor? **[our call]** | Label, source |
|---|---|---|---|
| **TForce** rules tariff, Item 130 | Pricing and transportation agreements are confidential, "held in strict confidence by all parties, including the agents of the customer", and "may not be disclosed unless required by law or as expressly permitted by a written agreement". The customer must "notify any Third Party or auditor of the confidential nature of the rates and charges, except to the extent expressly permitted by a written agreement" | **It expects auditors to see rates** and makes the shipper tell them they are confidential. Read strictly, disclosure still needs a written agreement allowing it. Ambiguous: a lawyer's question | *verified*, N-AO01 p. 12 |
| **TForce** Item 100 ¶13 | The carrier "may disclose information … for payment and audit purposes" | The carrier's own right, not the shipper's | *verified*, N-AO01 p. 8 |
| **FedEx Freight** rules tariff, Item 250 | Consignor and consignee agree the agreement and pricing "are confidential … and may not be disclosed unless required by law"; negotiations are confidential too; FedEx may share with its affiliates | **No carve-out** for auditors or agents | *verified*, N-AO02 p. 14 |
| **FedEx Transportation Services Agreement** (parcel template, Middle East site, eff. date field 2019-11-03) | Disclosure "to any third party without consent by FedEx and execution of a mutually agreeable non-disclosure agreement between FedEx and such third party shall be considered a breach by Customer" | **The auditor would need FedEx's consent and its own NDA with FedEx.** Parcel, non-US template. A US copy was found by search but returned 403 | *verified* (template), N-AO12; US version *assumed* |
| **YRC–First Brands contract** (2021-03-15), Art. 23 | Confidentiality does not preclude disclosure "to auditors, accountants, major lending institutions or legal counsel retained by a party for the purpose of assessing the accuracy of freight charges." Art. 13: payment "exclusively by First Brands Group or its freight payment agent" | **Yes, explicitly.** A large shipper negotiated it, so it is not typical of a mid-sized shipper | *verified*, N-AC05 pp. 10, 13 (re-read for Art. 13 and 23) |
| **SEFL** pricing agreement (Exist) | Marked "PROPRIETARY AND CONFIDENTIAL PROPERTY OF SOUTHEASTERN FREIGHT LINES" (on file) | Clause text not seen | *verified*, N-AC03 |
| **ODFL, XPO, Estes, Saia, ABF, R+L, SEFL, AAA Cooper** rules tariffs | No rate-confidentiality item. The word "confidential" appears only for blind shipments ("will not ensure the confidentiality of the transaction") | Silent in the tariff; the pricing agreement may still contain a clause | *verified* by full-text search, N-AO03 to N-AO10 |

**Count [our calc]:** 2 of 10 LTL rules tariffs read (FedEx Freight, TForce) make rates confidential by tariff.

### AO4.2 Evidence of shippers' reluctance, and where agreements live

| Item | What was found | Label, source |
|---|---|---|
| Shippers' wish to keep freight costs secret | At FMCSA's 2020 broker-transparency session, a 3PL CEO said shippers do not want charges to "get down to the carrier level, because shippers don’t want their competitors to know what they’re paying for freight"; a commenter said shippers "“consistently” require nondisclosure agreements with brokers" | *verified* as reported (FreightWaves, 2020-10-29), N-AO13. About brokers passing rates to carriers, not about auditors |
| Where rate agreements sit | An audit vendor: "Procurement may hold the contract while logistics owns the shipment data and finance receives the bill." It also quotes its own interviewees: "It is easier to absorb the cost than fight it." | *assumed* (vendor, European parcel-heavy context), N-AO31 |
| What buyers ask a new audit vendor | A new entrant's evaluation pack: the decision "crosses four desks: logistics, finance and procurement, IT, and security"; it promises a "retention schedule, sub-processor list, AI data-handling note" | *assumed* (vendor), N-AO30 |
| Surveys of shippers' willingness to share rates with auditors | **Not found** (searches 17, 18, 28) | — |

**Reading [our call]:**
- **A "no" at Test 2 may be contractual, not just reluctance.** A shipper bound by a FedEx Freight or FedEx-style clause may be unable to share without the carrier's consent. A shipper with a TForce agreement has to notify the auditor and may need written permission.
- **Possible interview probe (not applied; for the founders):** "Does your agreement with your biggest LTL carrier say anything about sharing it with an auditor or consultant? Has a carrier ever asked you to sign something before an outside party saw your rates?"
- **A mitigation to weigh, not decided:**
  - ask for the invoices first (they carry discount percentages and charges, not the full agreement);
  - offer to sign the carrier's own NDA where a clause requires it;
  - ask whether the shipper's agreement names auditors, as First Brands' did.
- **A09-11 stays an interview measurement** (files received from the first 3). The web can only tell us which clause the shipper may cite.

---

## §AO5 · D-16 input: incentives, gift rules and tax reporting (facts only)

### AO5.1 Tax reporting

| Rule | Text | Label, source |
|---|---|---|
| Threshold from 2026 | "For tax years beginning after 2025, the minimum threshold amount for reporting certain payments … increased to $2,000 and may be adjusted for inflation beginning in calendar year 2027." | *verified*, IRS Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026) p. 1, N-AO32 |
| What counts | "At least $2,000 in: … Prizes and awards … Other income payments (box 3)" | *verified*, p. 2 |
| Research payments named | Box 3 includes "A payment or series of payments made to individuals for participating in a medical research study or studies." Market-research interviews are not named | *verified*, p. 5 |

**Worked example [our calc]:** at $200 a call, one interviewee would need 10 paid calls in 2026 to reach $2,000. At the planned 1-2 calls per person, no 1099 would be triggered.
- Payments to a corporation, or a donation to a charity instead of cash, fall outside this personal-income reporting. That is our reading, not an IRS statement; an accountant should confirm.
- Panels pay incentives themselves (User Interviews adds 3%, on file N-V17).

### AO5.2 Gift rules in published codes

| Company (type) | Rule | Segment fit | Label, source |
|---|---|---|---|
| **Flex** (contract manufacturer, very large), Supplier Practices Guidelines Rev C (2024-04-29) | "Gifts in cash or cash equivalents from existing or prospective suppliers are always prohibited"; gift certificates are listed; "anything with a value of more than $25 USD" is barred | Partly: large firm; the rule covers *prospective* suppliers | *verified*, N-AO33 |
| **DRiV** (auto parts) ethics statement | Employees may accept "only noncash gifts of insignificant value (under $50 USD)", with disclosure; no "cash equivalent from any supplier or customer" | Partly: large firm | *verified*, N-AO34 |
| Mid-sized US manufacturer or distributor codes with dollar caps | **Not found** (search 9 surfaced only large firms) | — | — |

### AO5.3 Incentive amounts (adds to check V §9.1)

| Source | Figure | Label |
|---|---|---|
| SIS International screener (commercial research, tire-industry businesses, undated) | "$150 for those who qualify, are selected, and successfully complete an approximately 60-minute Zoom video interview" | *verified* as offered, N-AO35 |
| Respondent: "C-Level: CXS, President, Owners" $600; manager $200 (on file) | per session | *assumed*, N-V24 |
| User Interviews: B2B 1:1 remote $85/hour recommended; most common $112 (on file) | per hour | *assumed*, N-V23 |
| Incentives for trucking-company owners or billing staff specifically | **Not found** (search 19 found only driver studies, $20-$200) | — |

**Reading [our call], options only, not decided:**
- A cash or gift-card incentive may be refused, or be against policy, at firms whose codes cover "prospective suppliers", as Flex's does, because a researcher who might later sell to them fits that term. A charity donation, a benchmark summary, or nothing are the alternatives already on file.
- The $2,000 IRS threshold makes tax reporting a non-issue at the planned amounts. Recordkeeping per payee is still needed.

---

## §AO6 · D-18 input: NDAs, authority forms, retention and redaction (facts only)

### AO6.1 Open templates

| Template | What it says that matters here | Label, source |
|---|---|---|
| **Common Paper Mutual NDA v1.0** (CC BY 4.0; repository last changed 2022-06-07) | §2: the recipient may share with "its employees, agents, advisors, contractors and other representatives having a reasonable need to know for the Purpose", if they are bound no less strictly. §6: on request, destroy or return, **but** "the Receiving Party may retain Confidential Information in accordance with its standard backup or record retention policies or as required by law". Cover page defaults: the MNDA expires "[1 year(s)]" after signing; confidentiality lasts "[1 year(s)]" (trade secrets longer). §1: confidential information includes "pricing" | *verified*, N-AO36 |
| **Common Paper DPA** (same publisher) | §7.2(a): after expiry the provider "will return or delete Customer Personal Data at Customer’s instruction unless further storage … is required or authorized by Applicable Law"; subprocessors only if approved | *verified*, N-AO37 |
| Bonterms Mutual NDA | The guessed URL returned "Page Not Found"; not read | — |
| **Logistics Plus LOA** (audit firm's published template) | Authority to negotiate LTL rates and to route third-party-billed invoices "c/o Logistics Plus Inc. … for auditing and payment purposes"; signature, date and contact block | *verified*, N-AO28 |
| Carrier claim forms (on file and new) | Standard forms ask for claimant, PROs, authority, "charges should be" and a bond of indemnity (FedEx Freight PAP201, N-AO27; ABF and R+L on file, N-AK17, N-AK19) | *verified* |
| A freight-audit firm's NDA form, or a POA template for claims | **Not found** (searches 3, 4, 20) | — |

### AO6.2 Retention, deletion and redaction norms

| Norm | Text | Fit | Label, source |
|---|---|---|---|
| **Nacha data-security rule** | Large non-bank originators and third-party processors (over 2 million ACH entries a year) must protect account numbers "by rendering them unreadable when stored electronically"; "Encryption, truncation, tokenization, destruction" are options | Partly: we would be far below the volume, but it is the industry norm for bank details | *verified*, N-AO38 |
| What a buyer receives from an audit vendor | A "retention schedule" and "sub-processor list" in the security pack | Partly (European entrant) | *assumed* (vendor), N-AO30 |
| Published retention periods of freight-audit providers | **Not found** (search 10) | — | — |

**Reading [our call], options only:**
- **The open MNDA's default does not match the plan on file.** The plan is to delete raw files after the assessment and keep totals only. Common Paper §6 lets the recipient keep copies under backup policies. Its 1-year confidentiality term is also shorter than carriers' open-ended confidentiality (FedEx Freight, TForce). If the template is used, the cover page's "MNDA Modifications" box is where to:
  - drop the backup exception;
  - lengthen the term;
  - name the auditors' sub-processors (cloud and AI providers, check AL §7.2).
- **An LOA is a separate document from the NDA.** The NDA covers what we may do with the data. The LOA covers what carriers will accept from us: document access as agent (R+L's document API even lists a "LetterOfAuthorization" type, check T) and claims filed in the shipper's name.
- "Bank details removed at source" matches the Nacha norm of truncation or destruction. Asking for an AP export without account and routing numbers (check AC §9, R2) achieves it.

---

## §AO7 · D-19 input: time to recruit and response rates (facts only)

| Channel | Figure | Method disclosed? | Label, source |
|---|---|---|---|
| **User Interviews** (via the Rally help centre, updated about 2026-10-06) | "Median minutes to first qualified applicant: 77 minutes"; "Median hours to first confirmed session: 24 hours"; "Typical within 2 days: All requested participants matched, approved, and scheduled" | No (all study types) | *assumed* (vendor figure relayed by a partner), N-AO39 |
| **Respondent** | "Your first qualified participant in 15 minutes." | No | *assumed* (vendor claim), N-AO40 |
| Cold email, Smartlead platform | "850M+ emails, H1 2026", median reply 0.74%, top 10% at 2.6% | Partly | *assumed* (via an agency page, Webtonic, 2026-09-26), N-AO41 |
| Cold email, Woodpecker | Median reply 1.5% "across 56,614 campaigns" | Partly | *assumed* (via Webtonic, 2026-09-28), N-AO42 |
| Cold email, "3.43%" average | Attributed to **Instantly** on one page and to **Woodpecker** ("20M+ emails") on the other — see Coincidence watch | Conflicting | *assumed*, N-AO41, N-AO42; N-V26 |
| Belkins 0.45%; LinkedIn InMail 18-25% (on file) | — | Partly | *assumed*, N-V25, N-V27 |
| Reply rates for research requests to finance, logistics or carrier staff | **Not found** (search 14) | — | — |

**Worked example [our calc]** (emails needed for 5 held interviews, assuming half of replies book, **[our call]** as in check V):
- at 0.74%: 5 ÷ (0.0074 × 0.5) = **1,352 emails**;
- at 1.5%: 5 ÷ 0.0075 = **667**;
- at 3.43%: 5 ÷ 0.01715 = **292**.

**Reading [our call]:** a panel can schedule generic B2B sessions within 1-2 days by its own figures. A screener for "checks and pays freight bills at a 20-499-staff manufacturer" may run slower; no panel publishes feasibility for such a niche. Cold outreach to one side needs hundreds to about 1,350 emails at published medians. That is consistent with check V's 300-2,200, and suggests a re-dated window measured in weeks for the finance side.

---

## What the web could not settle

1. **How often carriers are short-paid or disputed, and what chasing costs them** (H09-C1b). No survey or filing found.
2. **Whether carriers enforce discount revocation or liquidated damages against a mid-sized shipper that short-pays in good faith**, and whether revocation applies to the whole bill (H09-C1).
3. **Whether carriers billing a shipper directly would pay for early payment through a new rail** (H09-C2). All verified prices are broker or FAP programmes.
4. **Whether carriers treat auditor-filed overcharge claims differently in practice** (H09-C4). The rules gate guarantee refunds; nothing public covers practice.
5. **What a mid-sized shipper's own pricing agreements say about disclosure to auditors**, and whether shippers will share (A09-11). Only their documents and answers can tell.
6. **Gift policies of mid-sized manufacturers and distributors**, and incentive norms for carrier owners and billing staff (D-16).
7. **Retention periods published by freight-audit providers** (D-18).
8. **Response rates for research (not sales) requests** to finance, logistics and carrier roles (D-19).
9. **Whether an LTL carrier would accept an auditor's LOA for claims and document access**; carriers' own LOA requirements were not found.

---

## Contact leads (no names; the founders decide whether to contact anyone)

| Role and organisation | Where found | Question IDs |
|---|---|---|
| Credit & Collection study group, ATA National Accounting & Finance Council | https://trucking.org/national-accounting-finance-council | H09-C1 (enforcement of penalties on short pays), H09-C2, H09-C4 |
| Overcharge claims team, TForce Freight | Item 813; claims page (on file, N-AK21) | H09-C4: may an agent file with a payer's LOA? A09-11: what written permission satisfies Item 130? |
| Revenue solutions (disputes) team, FedEx Freight | Item 438 ¶2 | A09-11: does Item 250 allow disclosure to a shipper's audit agent under an NDA? H09-C1: does a channel dispute stop late fees? |
| Overcharge claims team, XPO | N-AO26 | H09-C4: agent filing; what counts as the "pricing agreement" copy |
| Transportation & logistics practice group, a US transport law firm (e.g. the Benesch article's practice) | N-AO29 | H09-C1 (revocation on partly paid bills), A09-11 (enforceability of tariff confidentiality items against agents), D-18 (NDA modifications) |
| Factoring education, Secured Finance Network (SFNet) | N-AO17 | H09-C1: typical dilution in carrier receivables, and how much is shipper short pays |
| Carrier support team at a shipper's FAP (e.g. CT Logistics) | N-AO16 | H09-C1: how carriers respond to short-pay reports; share of balance-dues approved |

---

## Sources

All accessed on 2026-10-07. "Download" means the file was saved in the scratchpad and its text extracted.

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-AO01 | TForce Freight, Tariff UPGF 102-T "Rules and Charges" (newer copy of N-T28's file) | eff. 2026-03-16; PDF modified 2026-04-27 | https://www.tforcefreight.com/downloads/UPGF-102-T-20260316.pdf | download, full text | Items 100 ¶13, 130, 140, 166 Part 13, 721, 812, 813, 822, 823, 825, 826 |
| N-AO02 | FedEx Freight, 100-Y Rules Tariff (newer copy of N-T19's file) | eff. 2026-01-05; items revised 2026-06-01; PDF modified 2026-09-29 | https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf | download, full text | Items 250, 435, 435-2B, 438, 756, 757, 760, 765, 960 |
| N-AO03 | XPO, Tariff CNWY 199-AK.1 (same file as N-T20) | eff. 2026-02-16 | https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.1_Eff_02.16.2026.pdf | download, full text | Items 23, 207; BOL terms ¶8-9 |
| N-AO04 | Old Dominion, Tariff ODFL 100-Q (newer copy of N-T17's file) | eff. 2025-04-14; pages revised to 2026-10-05 | https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/Complete%20ODFL%20100-Q%20Tariff.pdf | download, full text | Items 395, 396, 434, 564 |
| N-AO05 | Saia, SAIA 170-D Rules Tariff (same file as N-T24) | eff. 2025-10-01 | https://assets.ctfassets.net/kjv8gs2ccggb/3Y5vAsxznsXornATV1AG5D/ffe12c504b75b780d9462fa25f9f0329/Saia_170D_10012025.pdf | download, full text | Item 435 Secs. B, C, H; Item 1030 ¶5-7 |
| N-AO06 | Estes, EXLA 105 Rules Tariff (same file as N-T22) | eff. 2026-01-02; PDF modified 2026-08-02 | https://www.estes-express.com/dA/ea677fdb-3bfa-45fb-9ef8-511174177f84/EstesRulesTariff.pdf | download, full text | Items 720, 825 |
| N-AO07 | ABF Freight, ABF 111-AU (same file as N-T25) | 2026-06-22 | https://arcb.com/sites/www/files/2026-06/ABF111-AU-06-22-2026-3.pdf | download, full text | Items 427, 721 |
| N-AO08 | R+L Carriers Rules Tariff (newer copy of N-T26's file) | "Updated 10/05/2026" | https://rl-cdn.com/docs/rlc/rules/rl-rules.pdf | download, full text | Item 775 |
| N-AO09 | Southeastern Freight Lines, SEFL 1090 (same file as N-T30) | Item 817 eff. 2021-03-01; PDF modified 2026-08-11 | https://www.sefl.com/vsmisc/RT1090%20Full.pdf | download, full text | Item 817 ¶1-7 |
| N-AO10 | AAA Cooper Transportation, AACT Rules Tariff 190-AF | eff. 2025-12-22 | https://www.aaacooper.com/docs/default-source/default-document-library/tariff/RulesTariff190.pdf | download, full text | Items 210, 649, 650, 660 |
| N-AO11 | Landstar, LAND 100-A Rules (TL and brokerage group) | eff. 2020-03-15 | https://www.landstar.com/media/vduhe3j1/land-100-a-march-17-2020.pdf | download, text search | Rules 435, 850 |
| N-AO12 | FedEx, "FedEx Transportation Services Agreement" (template, Middle East site) | effective-date field 2019-11-03; PDF created 2019-09-16 | https://www.fedex.com/content/dam/fedex/meisa-middle-east/campaign/FedEx_Transportation_Services_Agreement.pdf | download, full text | §6 Confidentiality |
| N-AO13 | FreightWaves, "What about shippers? Confidentiality issues among concerns in broker transparency hearing" | 2020-10-29 | https://www.freightwaves.com/news/what-about-shippers-confidentiality-issues-among-concerns-in-broker-transparency-hearing | raw page, quotes checked | Shipper confidentiality statements |
| N-AO14 | 49 U.S.C. 13708, LII (Cornell) | current | https://www.law.cornell.edu/uscode/text/49/13708 | download | (a)-(c) |
| N-AO15 | 49 CFR Part 377, eCFR renderer | current | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-49?part=377 | download | 377.201, 377.203 |
| N-AO16 | CT Logistics, "Johnson & Johnson Regional Transportation Freight Payment Carrier Guide" | "Last Updated: January 2014" | https://jnj.ctlogistics.com/sites/default/files/docs/jnj_freight_payment_carrier_guide.pdf | download, full text | Short-pay reports, web resolution, balance dues, refunds, discount terms |
| N-AO17 | Secured Finance Network, "SFNet Factoring On Demand Series, Module 1: Introduction to Factoring" | © 2020; PDF created 2021-06-30 | https://www.sfnet.com/docs/default-source/uploadedfiles/factoring-module-1-deck.pdf | download, full text | PDF p. 7 "Advance Rate and Dilution" |
| N-AO18 | FreightWaves, "You delivered that load three weeks ago…" (page shows a "Sponsored" label) | 2026-04-21 | https://www.freightwaves.com/news/you-delivered-that-load-three-weeks-ago-here-is-why-you-still-do-not-have-the-money-and-what-to-do-about-it | raw page | Non-recourse exclusions |
| N-AO19 | GSA Board of Contract Appeals, GSBCA 14055-RATE, *Admiral-Merchants Motor Freight* | 1998-02-20 | https://www.gsbca.gsa.gov/rate/m140550.txt | download, full text | Federal notices of overcharge and carrier protests |
| N-AO20 | RXO, "RXO & TriumphPay" carrier payment page | published 2025-12-02; modified 2026-03-26 | https://rxo.com/carriers/carrier-payment-options/rxo-triumphpay/ | raw page | Payment options and fees |
| N-AO21 | Werner, "Carrier Payment Options" | undated | https://www.werner.com/carrier-payment-options/ | raw page | Quick Pay fees, standard terms |
| N-AO22 | Con-way Multimodal, "Carrier Quick Pay Authorization Form" | PDF created 2008-08-25 | https://www.con-way.com/resources/quick_pay_registration.pdf | download, full text | Fees and required paperwork |
| N-AO23 | U.S. Bank, "U.S. Bank Introduces Ways to Enhance Carrier Cash Flow…" (IR copy) | 2020-06-10 | https://s203.q4cdn.com/711684571/files/doc_news/2020/06/News-Release-06-10-2020-1703080680821272.pdf | download, full text | Quick Pay, terms of 45-90 days |
| N-AO24 | Loop Help Center, "QuickPay" | "Last updated 1 year ago" | https://help.loop.com/articles/9657000706-quickpay | raw page | Carrier QuickPay description |
| N-AO25 | Uber Freight, "Quick Pay Agreement" (search snippet) | uploaded 2023-10 | https://www.uberfreight.com/wp-content/uploads/2023/10/Uber_Freight-Quick_Pay_Agreement.pdf | **404**; snippet only | 2% (*assumed*) |
| N-AO26 | XPO, "Overcharge Claim Process" sheet | 2026-02-24 | https://www.xpo.com/cdn/files/s1/Overcharge_Claim_Process_02-24-26.pdf | download, full text | Documents required, 100 PROs, rebuttal |
| N-AO27 | FedEx Freight, "Presentation of Overcharge Claims" form PAP201 (Canadian site copy) | undated | https://www.fedexfreight.com/content/dam/web/ca/documents/overcharge-claims-form.pdf | download, full text | Fields, bond of indemnity |
| N-AO28 | Logistics Plus, "LP LOA Letter of Authorization Template" (.docx) | letter dated 2018-01-01 | https://www.logisticsplus.com/wp-content/uploads/2015/10/LP-LOA-Letter-of-Authorization-Template.docx | download, full text | Whole letter |
| N-AO29 | Benesch Law, "Trucking Rate, Payment, and Collection Rules of the Road" | 2025-01-13 | https://www.beneschlaw.com/insight/trucking-rate-payment-and-collection-rules-of-the-road/pdf/ | download, full text | Statutory summary |
| N-AO30 | nShift, "nShift Audit RFP and security answers" (buyer's evaluation pack) | PDF created 2026-08-15 | https://nshift.com/hubfs/nShift-Audit-RFP-pack.pdf | download, text search | Intro; §7 Security |
| N-AO31 | nShift blog, "What a freight invoice audit needs from you before the first invoice gets analyzed" | 2026-09-03 | https://nshift.com/blog/freight-audit-checklist-before-the-first-invoice | raw page | Who holds the contract; interview quote |
| N-AO32 | IRS, Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026) | PDF modified 2026-06-30 | https://www.irs.gov/pub/irs-prior/i1099mec--2026.pdf | download, full text | pp. 1, 2, 5 |
| N-AO33 | Flex, "Supplier Practices Guidelines", FMS-QMS-4-104-00 Rev C | 2024-04-29 | https://flex.com/downloads/supplier-practice-guidelines | download, full text | §5 gifts |
| N-AO34 | DRiV, "Ethics Statement" (supplier purchasing page) | undated | https://www.drivparts.com/en-in/suppliers/purchasing/ethics-statement.html | raw page | Gift rule |
| N-AO35 | SIS Research, "Compensated Interview \| $150 Honorarium" (SurveyMonkey screener) | undated | https://www.surveymonkey.com/r/usa-tires | raw page | Offer and screener |
| N-AO36 | Common Paper, Mutual NDA v1.0, standard terms and cover page (GitHub) | last commit 2022-06-07 | https://raw.githubusercontent.com/CommonPaper/Mutual-NDA/main/Mutual-NDA.md ; https://raw.githubusercontent.com/CommonPaper/Mutual-NDA/main/Mutual-NDA-coverpage.md | download, full text | §1-11; cover page |
| N-AO37 | Common Paper, DPA (GitHub) | current | https://raw.githubusercontent.com/CommonPaper/DPA/main/DPA.md | download, text search | §1.6, §7 |
| N-AO38 | Nacha, "Supplementing Data Security Requirements" | current (phase 2 eff. 2022-06-30) | https://www.nacha.org/rules/supplementing-data-security-requirements | raw page | Rule summary and FAQ |
| N-AO39 | Rally Help Center, "Recruiting with User Interviews" | "Last updated 21 hours ago" (about 2026-10-06) | https://help.rallyuxr.com/articles/9829874426-recruiting-with-user-interviews | raw page | Time-to-recruit medians |
| N-AO40 | Respondent, marketplace page | current | https://www.respondent.io/marketplace | raw page | Speed claim |
| N-AO41 | Web Tonic (marketing agency), "Dispatch: Trucking Logistics Email Reply Data" | 2026-09-26 | https://www.webtonic.io/blog/trucking-and-logistics-email-marketing-statistics | raw page | Smartlead and Woodpecker figures |
| N-AO42 | Web Tonic, "Manufacturing and Industrial Cold Email Data, 2026" | 2026-09-28 | https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics | raw page | Instantly, Woodpecker, Belkins figures |
| N-AO43 | American Trucking Associations, "National Accounting & Finance Council" | current | https://trucking.org/national-accounting-finance-council | raw page | Study groups |
| N-AO44 | CourtListener RECAP search API (read-only queries) | run 2026-10-07 | https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=… | API JSON | 7 queries for shipper-carrier agreements with confidentiality or audit terms; 3 hits, none usable |

**Existing IDs re-used:** N-AC03, N-AC05 (re-read for Art. 13 and 23), N-AK17, N-AK19, N-AK21, N-AB41, N-T05, N-V17, N-V23 to N-V27, N-Z47 (the same file is still served at the URL: revision "R 9.2020", PDF modified 2021-03-02), N-Z57, N-Z62.

---

## Could not access, or not found

**Blocked or unusable:**
- **Triumph Financial investor site** (tfin.gcs-web.com): the host did not resolve (DNS failure), so dilution and short-pay data for TriumphPay's factored receivables went unread. **SEC EDGAR was not fetched** (house rule).
- **Uber Freight Quick Pay Agreement PDF:** HTTP 404 (snippet only, N-AO25).
- **Common Paper website:** HTTP 403. The same standard was read from the publisher's public GitHub repository.
- **Bonterms Mutual NDA:** the URL tried returned "Page Not Found".
- **Corning supplier code:** "Access Denied" (Akamai).
- **Justia copy of a US FedEx Transportation Services Agreement** (Armlogi Holding, 2020): HTTP 403. Search summaries say it carries the same clause as N-AO12 (*assumed*).
- **CourtListener exhibits** in an Illinois case (Annett Holdings, ilnd 217424, Docs 26-5 and 32-1): the storage returned an XML error, so the files are not stored.
- **User Interviews truck-driver study page:** closed; not used.
- **ATRI's "55% of detention invoices paid" figure** (a search summary): not found on the ATRI page fetched; not used.

**Searched, not found** (search numbers in brackets):
- carrier statements about audit firms or contingency auditors' claims [11, 12];
- a freight-audit firm's NDA or POA template for claims [3, 4, 20];
- published FAP retention periods [10];
- surveys of shippers' willingness to share rates [17];
- shipper-carrier contract templates with auditor carve-outs [7, 18, 28] (search 28 returned only spam mirrors);
- a newer U.S. Bank carrier agreement [16];
- TriumphPay complaints [15];
- surveys of the share of carrier invoices short-paid [24];
- carrier-owner or billing-staff incentive norms [19];
- mid-sized manufacturers' gift codes [9];
- logistics- or finance-specific cold-outreach benchmarks with method [14];
- data-destruction clauses in recovery-audit contracts [25].

**Not attempted:** PACER; NAFC member resources (behind a login); the current NMFC items 300500-300530 (licensed); Teleflex's supplier code; Gardewine's and CFI's TL tariffs (budget); Law360's report on Reckitt Benckiser's suit against invoice auditors (paywall); a Qargo POD-retention page (adjacent vendor; budget).

---

## Claim ledger

| Claim ID | Question | Claim | Number or rule (unit, denominator, population, version) | Verbatim quote + location | Source ID + URL | Published / accessed | Source type | Publisher, what they sell | Origin trace | Fits our segment? | Proposed label | Load-bearing? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-AO01 | A09-11 | TForce makes pricing agreements confidential, binding the customer's agents too | Rule; all TForce LTL customers without a contrary written agreement; UPGF 102-T | "shall be held in strict confidence by all parties, including the agents of the customer, and may not be disclosed unless required by law or as expressly permitted by a written agreement between Carrier and customer" (Item 130, p. 12) | N-AO01 https://www.tforcefreight.com/downloads/UPGF-102-T-20260316.pdf | eff. 2026-03-16 / 2026-10-07 | tariff | TForce Freight, LTL carrier | primary | yes (big LTL carrier) | *verified* | Y |
| C-AO02 | A09-11 | TForce expects shippers to tell auditors the rates are confidential | Rule; same | "to notify any Third Party or auditor of the confidential nature of the rates and charges, except to the extent expressly permitted by a written agreement" (Item 130, p. 12) | N-AO01 (as above) | same | tariff | TForce Freight | primary | yes | *verified* | Y |
| C-AO03 | A09-11 | TForce reserves its own right to disclose for audit purposes | Rule; same | "may disclose information as specifically required by law or for payment and audit purposes" (Item 100 ¶13, p. 8) | N-AO01 | same | tariff | TForce Freight | primary | yes | *verified* | N |
| C-AO04 | A09-11 | FedEx Freight's tariff makes agreements confidential with no auditor carve-out | Rule; consignors and consignees; 100-Y | "Consignor and Consignee agree that the terms of any Pricing or Transportation Agreement, including the attached pricing, are confidential and shall be held in strict confidence by all parties and may not be disclosed unless required by law." (Item 250, p. 14) | N-AO02 https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf | eff. 2026-01-05 / 2026-10-07 | tariff | FedEx Freight, LTL carrier | primary | yes | *verified* | Y |
| C-AO05 | A09-11 | A FedEx agreement template requires FedEx's consent and an NDA with FedEx before any third-party disclosure | Rule; FedEx TSA template (parcel/express, Middle East site) | "disclosure by Customer of this Agreement or any terms to any third party without consent by FedEx and execution of a mutually agreeable non-disclosure agreement between FedEx and such third party shall be considered a breach by Customer" (§6) | N-AO12 https://www.fedex.com/content/dam/fedex/meisa-middle-east/campaign/FedEx_Transportation_Services_Agreement.pdf | 2019 / 2026-10-07 | primary document (template) | FedEx, parcel and express carrier | primary; US copy not read (403) | partly (parcel, non-US template) | *verified* (template); US use *assumed* | Y |
| C-AO06 | A09-11 | A negotiated shipper-carrier contract carves out auditors from confidentiality | Rule; one contract, YRC entities and First Brands, 2021 | "to auditors, accountants, major lending institutions or legal counsel retained by a party for the purpose of assessing the accuracy of freight charges." (Art. 23(e), p. 13) | N-AC05 https://storage.courtlistener.com/recap/gov.uscourts.deb.198600/gov.uscourts.deb.198600.1.1.pdf | contract 2021-03-15; filed 2025-08-05 / 2026-10-07 | court record | Bankruptcy court filing (Yellow Corp.) | primary | partly (large shipper) | *verified* | Y |
| C-AO07 | A09-11, H09-C2 | That contract routes payment through a freight payment agent | Rule; same contract | "Payments shall be made exclusively by First Brands Group or its freight payment agent." (Art. 13, p. 10) | N-AC05 (as above) | same | court record | same | primary | partly | *verified* | N |
| C-AO08 | A09-11 | 8 of 10 LTL rules tariffs read have no rate-confidentiality item | Count; 10 tariffs (ODFL, FedEx Freight, XPO, Estes, Saia, ABF, R+L, TForce, SEFL, AAA Cooper), versions in Sources | No quote (absence). Full-text search for "confiden" finds only blind-shipment text, e.g. Saia "Carrier will not ensure the confidentiality of the transaction." | N-AO03 to N-AO10 (URLs in Sources) | 2025-26 / 2026-10-07 | tariff | the carriers | primary | yes | *verified* (search) **[our calc]** count | Y |
| C-AO09 | A09-11 | A 3PL CEO said shippers do not want competitors to know their freight costs | Statement; one speaker, FMCSA listening session, 2020 | "shippers don’t want their competitors to know what they’re paying for freight" | N-AO13 https://www.freightwaves.com/news/what-about-shippers-confidentiality-issues-among-concerns-in-broker-transparency-hearing | 2020-10-29 / 2026-10-07 | trade press | FreightWaves, freight media and data | speaker at a public FMCSA session (transcript not read) | partly (about brokers, not auditors) | *verified* as reported | N |
| C-AO10 | A09-11 | Shippers routinely require NDAs from brokers (commenter) | Statement; one commenter | "shippers “consistently” require nondisclosure agreements with brokers" | N-AO13 (as above) | same | trade press | same | commenter at the session | partly | *assumed* | N |
| C-AO11 | A09-11, H09-C4 | Federal law requires actual rates on bills presented to the payer or its agent | Statute; motor carriers under ch. 135 | "when a document is presented or electronically transmitted for payment to the person responsible directly to the motor carrier for payment or agent of such responsible person, the actual rates, charges, or allowances" (13708(a)) | N-AO14 https://www.law.cornell.edu/uscode/text/49/13708 | current / 2026-10-07 | regulator (statute) | Cornell LII, free law | primary text | yes | *verified* | N |
| C-AO12 | H09-C2, H09-C4 | FedEx Freight's tariff defines a freight payment processor ("Bill-To") | Definition; 100-Y | "Freight Payment Processor (commonly referred to as “Bill-To”): A bank or freight payment agency designated to pay the freight charges on behalf of Shipper, Consignee, or Third-Party Payor." (Item 765, p. 38) | N-AO02 (as above) | same | tariff | FedEx Freight | primary | yes | *verified* | N |
| C-AO13 | H09-C1 | Saia bars short payment by anyone | Rule; Saia customers; 170-D | "Short payment or taking credit for any freight bills by any party is not permitted." (Item 1030 ¶7, p. 146) | N-AO05 https://assets.ctfassets.net/kjv8gs2ccggb/3Y5vAsxznsXornATV1AG5D/ffe12c504b75b780d9462fa25f9f0329/Saia_170D_10012025.pdf | eff. 2025-10-01 / 2026-10-07 | tariff | Saia, LTL carrier | primary | yes | *verified* | Y |
| C-AO14 | H09-C1 | Saia revokes all discounts automatically when the credit period expires unpaid | Rule; 15 days net, 30 courtesy; 170-D | "Where Payor of Freight Charges fails to make payment during the authorized credit period of fifteen (15) days net, thirty (30) days courtesy, all discounts are revoked" (Item 435 Sec. C, p. 45) | N-AO05 (as above) | same | tariff | Saia | primary; authority cited: 49 CFR 377.203(g)(1)(ii) | yes | *verified* | Y |
| C-AO15 | H09-C1 | Saia's late service charges | 25% of principal (min $132.50) at 61-90 days; 50% (min $265.00) over 90 days; per unpaid invoice | "Failure to make payment of freight charges to the carrier for service performed within sixty (60) calendar days of presentation of the Freight Bill will result in the following late payment service charges" (Item 435 Sec. B ¶2, p. 45) | N-AO05 | same | tariff | Saia | primary | yes | *verified* | Y |
| C-AO16 | H09-C1 | Saia bars offsets, including for overcharge claims | Rule; 170-D | "shall pay all freight charges when due without offset for any cause, including but not limited to, cargo claims and overcharge claims." (Item 435 Sec. H, p. 47) | N-AO05 | same | tariff | Saia | primary | yes | *verified* | N |
| C-AO17 | H09-C1 | XPO charges a 10% late fee and revokes discounts on referral to collection | 10.00% of invoice balance, min $50.00 per shipment, every 30 days beyond terms; CNWY 199-AK.1 | "When shipments are assigned or placed with a collection agency, attorney or authorized agent for collection, all discounts are revoked" (Item 207, p. 31) | N-AO03 https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.1_Eff_02.16.2026.pdf | eff. 2026-02-16 / 2026-10-07 | tariff | XPO, LTL carrier | primary | yes | *verified* | Y |
| C-AO18 | H09-C1 | XPO: a dispute on one invoice does not justify withholding others | Rule; same | "An invoice dispute is insufficient grounds for debtor to withhold payment of any other valid invoices." (Item 207, p. 31) | N-AO03 | same | tariff | XPO | primary | yes | *verified* | N |
| C-AO19 | H09-C1 | Estes: 10% late charge after notice, then full undiscounted class rates, 30% collection fee | 10% (min $21.00); 30% of gross undiscounted charges; 30-day credit; EXLA 105 | "Non-payment after this time period, will result in the shipper paying the carrier’s full undiscounted, class rates applicable at the time of the shipment" (Item 720 ¶3c, p. 63) | N-AO06 https://www.estes-express.com/dA/ea677fdb-3bfa-45fb-9ef8-511174177f84/EstesRulesTariff.pdf | eff. 2026-01-02 / 2026-10-07 | tariff | Estes, LTL carrier | primary | yes | *verified* | Y |
| C-AO20 | H09-C1 | Estes bars offsets for overcharge claims | Rule; same | "is not permitted to offset any part of the freight charges by the value of any outstanding loss and damage, overcharge or over-collected claims." (Item 825, p. 76) | N-AO06 | same | tariff | Estes | primary | yes | *verified* | N |
| C-AO21 | H09-C1 | ABF: 30% fee on collection referral; no offsets | 30% of unpaid amount; ABF 111-AU | "will be subject to a late payment fee of thirty percent (30%) of the unpaid amount." (Item 427 ¶2B, p. 33) | N-AO07 https://arcb.com/sites/www/files/2026-06/ABF111-AU-06-22-2026-3.pdf | 2026-06-22 / 2026-10-07 | tariff | ABF Freight (ArcBest) | primary | yes | *verified* | Y |
| C-AO22 | H09-C1 | ODFL: 35% liquidated damages after 42 days | 35% of unpaid receivable; 42 days from the original invoice due date; ODFL 100-Q | "Carrier must receive full payment of freight charges within forty-two (42) days from the original invoice due date to avoid payor being charged an assessment of liquidated damages in an amount equal to 35% of the unpaid receivable." (Item 564 ¶1, p. 64) | N-AO04 https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/Complete%20ODFL%20100-Q%20Tariff.pdf | eff. 2025-04-14 / 2026-10-07 | tariff | Old Dominion, LTL carrier | primary | yes | *verified* | Y |
| C-AO23 | H09-C2 | ODFL: payment to an intermediary is not payment to ODFL | Rule; same | "all payment for freight charges made by the shipper or consignee to a freight forwarder, broker or any other party shall not be deemed as payment received by the Carrier." (Item 564 ¶6, p. 64) | N-AO04 | same | tariff | ODFL | primary | yes | *verified* | N |
| C-AO24 | H09-C4 | ODFL: one overcharge claim per invoice once closed | Rule; closed 30 days after ruling | "Carrier will not open new overcharge claims on any invoice for which a closed overcharge claim exists." (Item 396 ¶3, p. 39) | N-AO04 | same | tariff | ODFL | primary | yes | *verified* | Y |
| C-AO25 | H09-C1 | R+L: forfeiture of discounts plus a 125% penalty on collection action | 125% of remaining bill, after forfeitures; R+L tariff updated 2026-10-05 | "A penalty of 125% of the remaining freight bill amount due subject carriers after having added back any forfeitures" (Item 775 ¶2, p. 117) | N-AO08 https://rl-cdn.com/docs/rlc/rules/rl-rules.pdf | 2026-10-05 / 2026-10-07 | tariff | R+L Carriers, LTL carrier | primary | yes | *verified* | Y |
| C-AO26 | H09-C1 | SEFL: 25% on collection referral; no offset until a claim is finally processed | 25% of unpaid amount; Item 817 eff. 2021-03-01 | "Customer shall not offset from or delay the payment of lawfully established transportation charges due to Southeastern Freight Lines unless a formal claim is filed and has been finally processed" (Item 817 ¶6, p. 128) | N-AO09 https://www.sefl.com/vsmisc/RT1090%20Full.pdf | 2021 item / 2026-10-07 | tariff | Southeastern Freight Lines | primary | yes | *verified* | N |
| C-AO27 | H09-C1 | TForce: 1.5% a month plus collection costs after referral; no set-off | 1.5% per month; UPGF 102-T | "a service charge of 1.5% per month (or fraction thereof) will be assessed and due on the unpaid balance, beginning at the time the receivable is placed with the collections agency and/or legal counsel" (Item 721 ¶3, p. 44) | N-AO01 | eff. 2026-03-16 | tariff | TForce Freight | primary | yes | *verified* | N |
| C-AO28 | H09-C4 | TForce: an accepted settlement closes the claim for good | Rule; 180 days from deemed receipt | "Where a claim is declined or settled in an amount different from the original claim amount and the Claimant accepts the payment, the matter will be considered closed and no further claims for the same shipment will be honored." (Item 813, p. 58) | N-AO01 | same | tariff | TForce Freight | primary | yes | *verified* | Y |
| C-AO29 | H09-C1 | AAA Cooper: 35% liquidated damages after 60 days from ship date | 35% of unpaid receivable; 190-AF | "Any freight bill not paid within 60 calendar days of the ship date will be assessed liquidated damages of 35% of the unpaid receivable." (Item 210 ¶2, p. 12) | N-AO10 https://www.aaacooper.com/docs/default-source/default-document-library/tariff/RulesTariff190.pdf | eff. 2025-12-22 / 2026-10-07 | tariff | AAA Cooper, LTL carrier | primary | yes | *verified* | N |
| C-AO30 | H09-C4 | AAA Cooper: only the responsible party may submit overcharge claims | Rule; 180 days from shipment date; 190-AF | "must be submitted by the responsible party of the freight charges." (Item 660, p. 34) | N-AO10 | same | tariff | AAA Cooper | primary | yes | *verified* | Y |
| C-AO31 | H09-C2 | AAA Cooper makes the customer pay twice if a third party fails | Rule; same | "will pay freight charges twice in the event the third party or broker fails to pay freight charges to CARRIER." (Item 210 ¶5, p. 12) | N-AO10 | same | tariff | AAA Cooper | primary | yes | *verified* | N |
| C-AO32 | H09-C1 | FedEx Freight: undisputed invoices are due on terms; disputes go through set channels | Rule; 100-Y, Item 438 revised 2026-06-01 | "Invoices not disputed via one of the channels above are due and payable by Customer within the agreed-upon payment terms." (Item 438 ¶3, p. 19) | N-AO02 | same | tariff | FedEx Freight | primary | yes | *verified* | Y |
| C-AO33 | H09-C1 | FedEx Freight bars deducting any claim unless authorised in writing | Rule; same | "Customer shall not deduct or offset any cargo claim or other alleged claim or debt of Carrier from the charges owed to Carrier unless authorized in writing by Carrier." (Item 960 ¶9, p. 46) | N-AO02 | same | tariff | FedEx Freight | primary | yes | *verified* | N |
| C-AO34 | H09-C1 | Landstar: payment obligation absolute, no setoff (TL and brokerage) | Rule; LAND 100-A, 2020 | "Payor’s obligation to pay freight and ancillary charges in full is absolute and shall not be affected or reduced by any event or occurrence including, but not limited to, any setoff or counterclaim" (Rule 850) | N-AO11 https://www.landstar.com/media/vduhe3j1/land-100-a-march-17-2020.pdf | eff. 2020-03-15 / 2026-10-07 | tariff | Landstar, TL carrier and broker group | primary | partly (large, 2020) | *verified* | N |
| C-AO35 | H09-C1 | Federal credit rules: 15-day default, 30-day maximum; liquidated damages may be loss of discount | 15 and 30 days; 49 CFR 377.203 | "The second method is to require payment of the full, nondiscounted rate instead of the discounted rate otherwise applicable." (377.203(g)(1)(ii)); "shall not be longer than 30 calendar days" ((d)) | N-AO15 https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-49?part=377 | current / 2026-10-07 | regulator | eCFR (US government) | primary | yes | *verified* | Y |
| C-AO36 | H09-C1 | Collection penalties exclude clerical errors, not disputes | Rule; same | "Shall not apply to instances of clear clerical or ministerial error such as non-receipt of a carrier's freight bill" (377.203(g)(2)(iv)) | N-AO15 | same | regulator | same | primary | yes | *verified* | N |
| C-AO37 | H09-C1 | On one real bill, full-rate revocation would raise $942.02 to about $9,063.10 | $; one ABF bill (150235531, July 2024); assumes fuel at 30.3% of gross | No quote. Inputs: $6,963.80 gross, $6,232.60 discount (89.5%), $731.20 net, 30.3% fuel, $942.02 total (practice audit §3.2) | `s5_practice_audit_public_invoices.md`; N-PA01 | 2024 bill / — | **[our calc]** on a court record | — | inputs from the court record via the practice audit | partly (ABF itself uses a 30% fee, not revocation) | **[our calc]** | Y |
| C-AO38 | H09-C1b | A large shipper's FAP issues weekly short-pay reports to carriers | Practice; J&J and CT Logistics, 2014 | "Short pay Reports – available weekly reports on all invoices that are short paid and the reasonings" (Q10) | N-AO16 https://jnj.ctlogistics.com/sites/default/files/docs/jnj_freight_payment_carrier_guide.pdf | Jan 2014 / 2026-10-07 | primary document | CT Logistics (FAP) for J&J | primary | no (large shipper), but shows FAP practice | *verified* | Y |
| C-AO39 | H09-C1b | Unresolved carrier items are rejected after 30 days on that FAP's portal | 30 days; same | "FBs that need Carrier input are sent to Carrier Web Resolution and will be displayed online for 30 days for your review. After 30 days, the FBs will be rejected." | N-AO16 | same | primary document | same | primary | no | *verified* | N |
| C-AO40 | H09-C1b | Factoring treats short pays as dilution; trucking under 3% earns 90%+ advances | <3% dilution → ≥90% advance (example); SFNet training deck | "Dilution is non-cash deductions to A/R (i.e., offsets, short pays, billing errors, discounts, disputes, or any reason an invoice is not paid in full)." (PDF p. 7) | N-AO17 https://www.sfnet.com/docs/default-source/uploadedfiles/factoring-module-1-deck.pdf | © 2020 / 2026-10-07 | association training | Secured Finance Network, lenders' association | the 3% is an example, origin not stated | partly | *verified* (text); figure *assumed* | N |
| C-AO41 | H09-C1b | Many non-recourse factoring contracts exclude disputes and short deliveries | Statement; carriers using brokers | "many non-recourse agreements only cover broker bankruptcy or business closure — not a broker who disputes the invoice, claims a short delivery, or simply refuses to pay." | N-AO18 https://www.freightwaves.com/news/you-delivered-that-load-three-weeks-ago-here-is-why-you-still-do-not-have-the-money-and-what-to-do-about-it | 2026-04-21 / 2026-10-07 | trade press (page shows a "Sponsored" label) | FreightWaves | origin not found | partly | *assumed* | N |
| C-AO42 | H09-C1, H09-C4 | Federal auditors issue notices of overcharge that carriers protest | One decision; GSBCA 14055-RATE | "subsequent to payment by the Government, the General Services Administration (GSA) issued a notice of overcharge demanding a refund of a specified dollar amount." (whitespace normalised) | N-AO19 https://www.gsbca.gsa.gov/rate/m140550.txt | 1998-02-20 / 2026-10-07 | court record (board decision) | GSA Board of Contract Appeals | primary | no (government shipper) | *verified* | N |
| C-AO43 | H09-C2 | RXO charges carriers 2.5% for QuickPay and 4.0% for Advance Pay | 2.5% per transaction; 4.0%; Standard Pay free; carriers hauling for RXO | "QuickPay has a 2.5% fee per transaction" | N-AO20 https://rxo.com/carriers/carrier-payment-options/rxo-triumphpay/ | modified 2026-03-26 / 2026-10-07 | broker terms page | RXO, freight broker | primary (own terms) | partly (broker-paid carriers) | *verified* | Y |
| C-AO44 | H09-C2 | Werner charges 2.5% next-day or 1.5% 5-day quick pay | 2.5% / 1.5% of invoice total; carriers hauling for Werner's brokerage | "2.5% next day and 1.5% 5-day payment options (service fee deducted from total invoice)" | N-AO21 https://www.werner.com/carrier-payment-options/ | undated / 2026-10-07 | broker terms page | Werner, carrier and broker | primary (own terms) | partly | *verified* | Y |
| C-AO45 | H09-C2 | Con-way Multimodal charged 3% for immediate and 2% for 7-day pay (2008) | 3% / 2% of agreed payment | "Immediate Pay: a 3% fee will be deducted from the total agreed upon payment for the shipment." | N-AO22 https://www.con-way.com/resources/quick_pay_registration.pdf | 2008 / 2026-10-07 | primary document (form) | Con-way Multimodal, broker | primary | partly (old, broker) | *verified* | N |
| C-AO46 | H09-C2 | U.S. Bank Quick Pay accelerates shipper terms of 45-90 days for a fee | Terms 45-90 days; carriers on U.S. Bank Freight Payment | "Quick Pay gives carriers who are paid according to contracted terms – typically anywhere from 45 and up to 90 days – new flexibility to accelerate cash flow when needed." | N-AO23 https://s203.q4cdn.com/711684571/files/doc_news/2020/06/News-Release-06-10-2020-1703080680821272.pdf | 2020-06-10 / 2026-10-07 | company press release | U.S. Bank, FAP and bank | primary | yes (shipper-side FAP) | *verified* | Y |
| ~~C-AO47~~ | H09-C2 | ~~FedEx Freight adds 3% to card payments and may adjust discounts by payment type~~ **DISCARDED by the adversarial review (2026-10-07):** Item 435-2B sits in the Intra-Canada section; there is no US card surcharge. The discount-by-payment-type part stands as C-AO82 | ~~3% handling charge; 100-Y~~ | "can be made by credit card subject to an additional 3% handling charge." (Item 435-2B) | N-AO02 | same | tariff | FedEx Freight | primary | no (Intra-Canada only) | ~~*verified*~~ discarded | N |
| C-AO48 | H09-C2 | ABF adds 2% to B2B card payments, "same or lower than our cost of acceptance" | 2% of service fees and charges; ABF 111-AU | "a two percent (2%) handling surcharge will be applicable on all service fees and charges. This rate is the same or lower than our cost of acceptance" (Item 721, p. 52) | N-AO07 | same | tariff | ABF Freight | primary | yes | *verified* | N |
| C-AO49 | H09-C2 | Uber Freight's quick pay is 2% | 2%; carriers hauling for Uber Freight | No verbatim (PDF 404; search snippet) | N-AO25 https://www.uberfreight.com/wp-content/uploads/2023/10/Uber_Freight-Quick_Pay_Agreement.pdf | 2023 / 2026-10-07 | broker terms (snippet) | Uber Freight, broker | snippet; page gone | partly | *assumed* | N |
| C-AO50 | H09-C2 | Paying 2.5% to be paid ~29 days early is ~31% a year | 2.5% × 365 ÷ 29 | No quote | — | — | **[our calc]** | — | inputs C-AO43, C-AO44 | partly | **[our calc]** | N |
| C-AO51 | H09-C4 | FedEx Freight may refuse guarantee refunds requested by a third party | Rule; Money-Back Guarantee; Item 760 ¶6 eff. 2026-06-01 | "the Money-Back Guarantee may not be honored when the request is made by, or the information utilized to determine the status of the shipment is determined by, a third party other than the payer" (p. 36) | N-AO02 | eff. 2026-06-01 / 2026-10-07 | tariff | FedEx Freight | primary; same wording as FedEx parcel terms (N-AK29) | yes | *verified* | Y |
| C-AO52 | H09-C4 | FedEx Freight issues guarantee refunds to the debtor only | Rule; Items 756, 757, 760 | "Carrier will not issue refunds or credits to third parties and/or agencies." (pp. 32, 33, 36) | N-AO02 | same | tariff | FedEx Freight | primary | yes | *verified* | Y |
| C-AO53 | H09-C4 | TForce bars agents from requesting guarantee refunds | Rule; Items 822, 823, 825, 826; 15 days from delivery | "No agent, representative, or third party may request cancellation or refund on behalf of the payer and no refunds will be made to any party other than the payer." (Item 823 ¶6, p. 62) | N-AO01 | eff. 2026-03-16 | tariff | TForce Freight | primary | yes | *verified* | Y |
| C-AO54 | H09-C4 | XPO wants the pricing agreement attached to rate-based claims; up to 100 PROs per claim | Rule; XPO sheet 2026-02-24 | "If the claim is related to a pricing agreement or tariff, copies of those documents must also be provided" | N-AO26 https://www.xpo.com/cdn/files/s1/Overcharge_Claim_Process_02-24-26.pdf | 2026-02-24 / 2026-10-07 | carrier form | XPO | primary | yes | *verified* | Y |
| C-AO55 | H09-C4, D-18 | FedEx Freight's claim form carries a bond of indemnity and no agent field | Form PAP201 (Canadian site copy) | "BOND OF INDEMNITY: The undersigned guarantees to protect any carrier having an interest against any and all loss, costs, and expenses, including attorney fees, which may result to carrier from payment of this claim" | N-AO27 https://www.fedexfreight.com/content/dam/web/ca/documents/overcharge-claims-form.pdf | undated / 2026-10-07 | carrier form | FedEx Freight | primary | partly (Canadian copy) | *verified* | N |
| C-AO56 | D-18, H09-C4 | An audit firm publishes an LOA template routing third-party-billed invoices to itself | Template; dated 2018-01-01 | "This letter also serves as authorization to send invoices that are third-party billed to (Client Name) c/o Logistics Plus Inc. at PO Box 183850, Shelby Township, MI 48318 for auditing and payment purposes" | N-AO28 https://www.logisticsplus.com/wp-content/uploads/2015/10/LP-LOA-Letter-of-Authorization-Template.docx | 2018 / 2026-10-07 | vendor document | Logistics Plus, 3PL and audit services | primary | yes | *verified* | N |
| C-AO57 | H09-C1 | Rate tariffs are now strictly required only for household goods and noncontiguous trade | Legal summary | "Today publishing rate tariffs is only strictly required for household goods or traffic in the noncontiguous domestic trade under 49 USC § 13702." | N-AO29 https://www.beneschlaw.com/insight/trucking-rate-payment-and-collection-rules-of-the-road/pdf/ | 2025-01-13 / 2026-10-07 | secondary (law firm) | Benesch Law, legal services | origin: 49 U.S.C. 13702 (not re-read) | yes | *assumed* | N |
| C-AO58 | A09-11 | An audit vendor says the contract, shipment data and bill sit with different teams | Statement; vendor's customers (European, parcel-heavy) | "Procurement may hold the contract while logistics owns the shipment data and finance receives the bill." | N-AO31 https://nshift.com/blog/freight-audit-checklist-before-the-first-invoice | 2026-09-03 / 2026-10-07 | vendor | nShift, shipping and audit software | vendor's own interviews | partly | *assumed* | N |
| C-AO59 | A09-11, D-18 | A new audit entrant says evaluation spans four desks and promises a retention schedule | Statement; nShift Audit, GA October 2026 | "The Audit-specific security documentation set (data residency statement, retention schedule, sub-processor list, AI data-handling note) completes at GA" (§7) | N-AO30 https://nshift.com/hubfs/nShift-Audit-RFP-pack.pdf | 2026-08-15 / 2026-10-07 | vendor | nShift | vendor | partly | *assumed* | N |
| C-AO60 | D-16 | The IRS 1099 threshold rose to $2,000 for payments after 2025 | $2,000 per payee per calendar year; inflation-adjusted from 2027 | "For tax years beginning after 2025, the minimum threshold amount for reporting certain payments required to be reported on certain information returns and/or perform backup withholding on those payments increased to $2,000" (p. 1) | N-AO32 https://www.irs.gov/pub/irs-prior/i1099mec--2026.pdf | Rev. Dec 2026 / 2026-10-07 | regulator | IRS | primary | yes | *verified* | Y |
| C-AO61 | D-16 | Box 3 names medical-research study payments, not market research | Rule; Form 1099-MISC box 3 | "A payment or series of payments made to individuals for participating in a medical research study or studies." (p. 5) | N-AO32 | same | regulator | IRS | primary | yes | *verified* | N |
| C-AO62 | D-16 | Flex bans cash and gift certificates from prospective suppliers, $25 cap | $25 per gift; Rev C | "Gifts in cash or cash equivalents from existing or prospective suppliers are always prohibited." (§5.2) | N-AO33 https://flex.com/downloads/supplier-practice-guidelines | 2024-04-29 / 2026-10-07 | primary document (company code) | Flex, contract manufacturer | primary | partly (very large firm) | *verified* | Y |
| C-AO63 | D-16 | DRiV allows only non-cash gifts under $50 and bans cash equivalents | $50 | "no employee or family members may receive a cash equivalent from any supplier or customer." | N-AO34 https://www.drivparts.com/en-in/suppliers/purchasing/ethics-statement.html | undated / 2026-10-07 | primary document | DRiV, auto parts | primary | partly | *verified* | N |
| C-AO64 | D-16 | A commercial researcher pays $150 for a 60-minute industry interview | $150 per completed ~60-min interview; tire-industry businesses | "We are providing compensation of $150 for those who qualify, are selected, and successfully complete an approximately 60-minute Zoom video interview." | N-AO35 https://www.surveymonkey.com/r/usa-tires | undated / 2026-10-07 | vendor (research firm) | SIS International Research | primary (the offer) | partly | *verified* (offer) | N |
| C-AO65 | D-18 | The Common Paper MNDA lets the recipient share with advisers and contractors on need to know | Rule; v1.0, CC BY 4.0 | "may disclose Confidential Information to its employees, agents, advisors, contractors and other representatives having a reasonable need to know for the Purpose" (§2) | N-AO36 https://raw.githubusercontent.com/CommonPaper/Mutual-NDA/main/Mutual-NDA.md | 2022 / 2026-10-07 | primary document (open standard) | Common Paper, contract standards | primary | yes | *verified* | Y |
| C-AO66 | D-18 | The same MNDA lets the recipient retain copies under backup policies | Rule; §6 | "the Receiving Party may retain Confidential Information in accordance with its standard backup or record retention policies or as required by law" | N-AO36 | same | primary document | Common Paper | primary | yes | *verified* | Y |
| C-AO67 | D-18 | The MNDA's default term and confidentiality period are 1 year | 1 year from the effective date (both defaults); cover page v1.0 | "[1 year(s)] from Effective Date, but in the case of trade secrets until Confidential Information is no longer considered a trade secret under applicable laws." | N-AO36 https://raw.githubusercontent.com/CommonPaper/Mutual-NDA/main/Mutual-NDA-coverpage.md | same | primary document | Common Paper | primary | yes | *verified* | N |
| C-AO68 | D-18 | The Common Paper DPA returns or deletes personal data at the customer's instruction | Rule; §7.2(a) | "After the DPA expires, Provider will return or delete Customer Personal Data at Customer’s instruction unless further storage of Customer Personal Data is required or authorized by Applicable Law." | N-AO37 https://raw.githubusercontent.com/CommonPaper/DPA/main/DPA.md | current / 2026-10-07 | primary document | Common Paper | primary | yes | *verified* | N |
| C-AO69 | D-18 | Nacha requires large ACH users to make account numbers unreadable in storage | Over 2 million ACH entries a year; phase 2 eff. 2022-06-30 | "protect DFI Account Numbers used in the initiation of Entries by rendering them unreadable when stored electronically" | N-AO38 https://www.nacha.org/rules/supplementing-data-security-requirements | current / 2026-10-07 | rule-setter | Nacha, ACH rules body | primary | partly (threshold far above us) | *verified* | N |
| C-AO70 | D-19 | User Interviews: 77 minutes to first qualified applicant, 24 hours to first confirmed session (medians) | Medians; all study types; via Rally's integration page | "Median minutes to first qualified applicant: 77 minutes Median hours to first confirmed session: 24 hours" | N-AO39 https://help.rallyuxr.com/articles/9829874426-recruiting-with-user-interviews | updated ~2026-10-06 / 2026-10-07 | vendor (partner's help page) | Rally, research ops software | origin: User Interviews (not read on UI's site) | partly | *assumed* | Y |
| C-AO71 | D-19 | Respondent claims a first qualified participant in 15 minutes | Claim; no method | "Your first qualified participant in 15 minutes." | N-AO40 https://www.respondent.io/marketplace | current / 2026-10-07 | vendor | Respondent, research panel | vendor | partly | *assumed* | N |
| C-AO72 | D-19 | Smartlead's median cold-email reply rate is 0.74% | 850M+ emails, H1 2026; replies ÷ (denominator not stated) | "Smartlead's own platform data (850M+ emails, H1 2026) puts median cold email reply rate at 0.74%" | N-AO41 https://www.webtonic.io/blog/trucking-and-logistics-email-marketing-statistics | 2026-09-26 / 2026-10-07 | secondary (agency) | Web Tonic, marketing agency | origin: Smartlead (not read) | partly (cross-industry) | *assumed* | Y |
| C-AO73 | D-19 | Woodpecker's median cold-email reply rate is 1.5% | 56,614 campaigns; replies ÷ sends | "Woodpecker's median reply rate is 1.5% across 56,614 campaigns." | N-AO42 https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics | 2026-09-28 / 2026-10-07 | secondary (agency) | Web Tonic | origin: Woodpecker (not read) | partly | *assumed* | Y |
| C-AO74 | D-19 | Emails needed for 5 interviews: 292-1,352 at published rates | 5 ÷ (reply rate × 50% booking) | No quote | — | — | **[our calc]** | — | inputs C-AO72, C-AO73, N-V26 | partly | **[our calc]** | Y |
| C-AO75 | D-16, H09-C1 | ATA's finance council has a Credit & Collection study group | Fact | "NAFC’s Study Groups are: Taxation, Accounting Principles, Credit & Collection, Financial Relations, Risk Management and Information Technology." | N-AO43 https://trucking.org/national-accounting-finance-council | current / 2026-10-07 | association | American Trucking Associations | primary | yes (contact lead) | *verified* | N |
| C-AO76 | H09-C1 | ODFL bars offsets of overcharge claims | Rule; ODFL 100-Q | "The customer responsible for paying freight charges may not offset any part of freight charges on any outstanding loss and damage, overcharge, or over collected claim." (Item 395, p. 38) | N-AO04 https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/Complete%20ODFL%20100-Q%20Tariff.pdf | eff. 2025-04-14 / 2026-10-07 | tariff | ODFL | primary | yes | *verified* | N |
| C-AO77 | H09-C1 | R+L's rules tariff has no offset item | Absence; R+L tariff updated 2026-10-05; searched "offset", "set-off", "setoff", "deduct", "withh" | No quote (absence) | N-AO08 https://rl-cdn.com/docs/rlc/rules/rl-rules.pdf | 2026-10-05 / 2026-10-07 | tariff | R+L Carriers | primary | yes | *verified* (search) | N |
| C-AO78 | H09-C1 | ABF bars offsets for overcharge claims and charge-backs | Rule; ABF 111-AU | "Customer shall not offset from or delay the payment of lawfully established transportation charges due ABF Freight as result of any overcharge claim, charge back, duplicate payment or loss and/or damage cargo claim." (Item 427 ¶3, p. 33) | N-AO07 https://arcb.com/sites/www/files/2026-06/ABF111-AU-06-22-2026-3.pdf | 2026-06-22 / 2026-10-07 | tariff | ABF Freight | primary | yes | *verified* | N |
| C-AO79 | H09-C1 | XPO bars withholding or offset for any reason | Rule; CNWY 199-AK.1 | "Debtor shall not have the right to withhold or offset the payment of charges for any reason, including but not limited to, claims for lost or damaged goods." (Item 23(5), p. 18) | N-AO03 https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.1_Eff_02.16.2026.pdf | eff. 2026-02-16 / 2026-10-07 | tariff | XPO | primary | yes | *verified* | N |
| C-AO80 | H09-C1 | TForce bars offsets of filed or unfiled claims | Rule; UPGF 102-T | "Claims and claim amounts made against Carrier (whether filed or unfiled) may not be offset by customer, shipper, consignee or payer against freight charges otherwise owed to Carrier." (Item 166 Part 13, p. 20) | N-AO01 https://www.tforcefreight.com/downloads/UPGF-102-T-20260316.pdf | eff. 2026-03-16 / 2026-10-07 | tariff | TForce Freight | primary | yes | *verified* | N |
| C-AO81 | H09-C1 | AAA Cooper bars offsets of overcharge claims | Rule; 190-AF | "The customer responsible for the payment of freight charges is not permitted to offset any part of the freight charges by the value of any outstanding loss and damage, overcharge or over-collected claims." (Item 649, p. 33) | N-AO10 https://www.aaacooper.com/docs/default-source/default-document-library/tariff/RulesTariff190.pdf | eff. 2025-12-22 / 2026-10-07 | tariff | AAA Cooper | primary | yes | *verified* | N |
| C-AO82 | H09-C2 | FedEx Freight may adjust discounts by payment type | Rule; Item 435 ¶2.C.1, revised 2026-06-01 | "FedEx Freight may consider payment type in determining pricing and discounts, and reserves the right to adjust discounts based on payment type." (p. 19) | N-AO02 https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf | 2026-06-01 / 2026-10-07 | tariff | FedEx Freight | primary | yes | *verified* | N |
| C-AO83 | H09-C2 | Werner's standard pay is within 30 days of invoice and paperwork | 30 days; carriers hauling for Werner's brokerage | "Balance of invoice is paid within 30 days of receipt of invoice, POD, lumper receipts, etc., or by Quick Pay" | N-AO21 https://www.werner.com/carrier-payment-options/ | undated / 2026-10-07 | broker terms page | Werner | primary (own terms) | partly | *verified* | N |
| C-AO84 | H09-C2 | J&J offered carriers early-payment discount terms through its AP | Practice; J&J, 2014 | "enables discount payment terms for our carriers that opt to participate in the program." (Q8) | N-AO16 https://jnj.ctlogistics.com/sites/default/files/docs/jnj_freight_payment_carrier_guide.pdf | Jan 2014 / 2026-10-07 | primary document | CT Logistics for J&J | primary | no (large shipper) | *verified* | N |
| C-AO85 | H09-C2 | Loop (FAP) offers carriers QuickPay at a discount; rate not published | Practice | "QuickPay is a payment option offered to carriers to get paid for delivered loads faster for a discounted rate." | N-AO24 https://help.loop.com/articles/9657000706-quickpay | ~2025 / 2026-10-07 | vendor help page | Loop, freight audit and payment | primary (own product) | partly | *verified* | N |
| C-AO86 | H09-C2 | Quick-pay cost on a $2,000 load ranges $25-$80 | $; 1.25% (U.S. Bank, on file N-Z47) to 4.0% (RXO Advance Pay) | No quote | — | — | **[our calc]** | — | inputs C-AO43, C-AO44, C-AO45, N-Z47 | partly | **[our calc]** | N |
| C-AO87 | D-16 | One interviewee needs 10 paid calls at $200 to reach the $2,000 threshold | $2,000 ÷ $200 | No quote | — | — | **[our calc]** | — | input C-AO60 | yes | **[our calc]** | N |

---

## Coincidence watch

| Figure or rule | Sources that give it | Shared origin? | Note |
|---|---|---|---|
| **3.43% average cold-email reply rate** | Web Tonic manufacturing page: "Instantly's 2026 cross-industry average"; Web Tonic trucking page: "Woodpecker's own platform data (20M+ emails)"; check V (N-V26): Instantly | **Same agency gives two origins** | One attribution is wrong, or two vendors coincide to two decimals. Treat 3.43% as unattributed until read at Instantly's or Woodpecker's own report |
| **2.5% quick pay** | RXO; Werner | **Yes, partly:** both run on TriumphPay, and FreightWaves (search only) reports TriumphPay shares the fee with the broker | Not two independent market readings. Con-way's 2008 3%/2% is independent but old |
| **3%** | FedEx Freight card handling charge; Con-way immediate pay (2008); a TriumphPay/HubTran flyer's "3% or less" quick pay (search snippet, not read) | No | Look-alikes measuring different things: a card surcharge paid **by shippers**, against quick-pay fees paid **by carriers** |
| **2%** | ABF card surcharge; Con-way 7-day pay; Uber Freight quick pay (snippet); TriumphPay "Select Carrier" rate "starts at 2%" (snippet, not read) | No | Different payers and products |
| **35% liquidated damages** | ODFL Item 564 (42 days after the invoice due date); AAA Cooper Item 210 (60 days after the ship date) | Not traced; both rely on 49 CFR 377.203(g)(1)(i) | Same rate, different triggers. Do not average |
| **30%** | ABF late fee on collection referral (of the unpaid amount); Estes collection fee (of **gross undiscounted** charges) | Shared regulation only | Different bases: Estes's 30% of gross can far exceed ABF's 30% of unpaid |
| **15-day credit period** | Every tariff read (ODFL, ABF, SEFL, TForce, FedEx, AAA Cooper, Landstar); Saia adds 30 days "courtesy"; Estes and XPO count 30 and 15 days from the invoice | **Yes:** the 49 CFR 377.203(c) default | Not independent confirmations |
| **180 days** | 49 U.S.C. 13710; tariffs (XPO, Saia, FedEx, TForce, AAA Cooper) | Yes (the statute) | Start points differ: invoice receipt, invoice date, shipment date (AAA Cooper), deemed receipt 10 days after tender (TForce) |
| **"third party other than the payer" wording** | FedEx Freight Item 760 ¶6 (LTL, 2026); FedEx parcel terms (check AK, 2021 and 2010) | **Yes:** the same company's drafting | One corporate policy, not two carriers agreeing |
| **TForce "payer only"** | TForce web page (overcharge claims, N-AK21); TForce Items 822-826 (guarantee refunds) | Same carrier | The tariff's claim item (813) does not repeat the payer-only rule. Web and tariff differ in scope; check which governs before relying on either |
| **Detention invoices paid** | ATRI 2024 release: fleets "are paid for fewer than 50 percent" (N-AB41, *verified* on file); a search summary: "only 55% of those invoices were paid" (from a driver survey) | Same study family, different respondents | The 55% was not found at the source fetched; do not use. Look-alikes measuring fleets against drivers |
| **Search-engine summary errors** (faulty web data) | (a) A search summary said 49 CFR 378 "applies only to household goods"; the regulation covers motor carriers generally (378.1, on file N-T05). (b) A summary described AAA Cooper's tariff as 190-AD of 2024-11-04; the file served today is 190-AF, effective 2025-12-22. (c) A summary said Part 377's credit rules "do not apply to contract carriage"; the current 377.201 lists only government and passenger-incidental exceptions | n/a | Discarded. Only text read at the source is used above |
| **User Interviews' speed** | Rally's help page (77 minutes, 24 hours); User Interviews' own site not read | Origin: User Interviews (relayed) | One vendor's figure through a partner, not two sources |
| **Respondent's speed** | "first qualified participant in 15 minutes" (marketplace page); a search snippet quoted a "30 Mins" median time to first match from another Respondent page | Same vendor | Different metrics (qualified against matched); neither has a method |
| **1% early-payment fee** | U.S. Bank base discount fee (N-Z47); a card's "reduced fees of just 1%" (N-Z63, on file) | No | Different products |
| **Confidentiality of rates** | TForce Item 130 and FedEx Freight Item 250 share phrases ("held in strict confidence by all parties", "not to post or publicly display the terms or the pricing"); the FedEx TSA template has the same phrasing | Possibly a common drafting ancestor (TForce Freight was UPS Freight until 2021, background knowledge, *assumed*; the FedEx wording appears in both FedEx documents) | Two carriers' clauses are not independent evidence of an industry norm. Eight other tariffs carry no such item |
