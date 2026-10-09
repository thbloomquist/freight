# S5 check AO, adversarial review

- **What this is:** an adversarial check of check AO, run because the founders asked for "adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data". Each claim was tested against its source. Objections are raised only where the evidence supports them. A claim that survives is a result too.
- **File checked:** `research/s5_check_AO_c09_carriers_and_access.md` (87 ledger rows, C-AO01 to C-AO87; its §0, body sections and Coincidence watch). Context read: `C09-business-proposal.md` §7-§8 (Test 2: "2 of the first 3 shippers decline" to share the agreement and invoices under an NDA).
- **Date:** 2026-10-07.
- **Status:** input to S5. **It decides nothing.**
- **Searches used:** 10 of 10 (listed in §6). **Fetches made:** about 89: 83 page or PDF downloads, plus 2 Wayback index queries, 3 read-only CourtListener API queries and 1 GitHub API query. Every cited URL in the checked file was fetched again, except the CourtListener API queries (N-AO44), which back no claim.
- **No identity was sent. Nobody was contacted.** A generic browser user-agent was used. There were no logins, sign-ups or form submissions. SEC EDGAR was not fetched. Downloads are in the session scratchpad under `AO-adv/downloads/`, outside the project folder.
- **Rows checked:**
  - **In full, all seven tests: 63 rows.** These are the 36 rows marked load-bearing (Y) and the 27 rows marked N that feed a number or verdict in §0.
  - **Existence and meaning (tests 1-2), plus currency where the file was a tariff: the other 24 rows.** That is every remaining row, not a sample. Arithmetic (test 7) was also redone on the three calculation rows among them (C-AO50, C-AO86, C-AO87).
  - **Not checked: 0.**
  - Test 6 (counter-search) was run per question, not per row: 10 searches plus targeted fetches of current tariff reissues and origin pages.

### Words used here

| Word | Meaning |
|---|---|
| **Reissue** | A carrier republishes its rules tariff with a new effective date. Items can change between reissues, so a quote must be checked against the current file |
| **Intra-Canada section** | The part of FedEx Freight's tariff that applies only to shipments moving inside Canada (its items carry the suffix "-2B") |
| **Discount revocation** | A penalty for paying late: the payer loses its negotiated discount and owes the full list ("class") rate |
| **Liquidated damages** | A penalty fixed in advance in the tariff, here for the carrier's cost of collecting an overdue bill |
| **Origin** | The first place a number was measured. A figure repeated by three websites from one origin is one source, not three |
| **Look-alike number** | Two figures that match but measure different things |
| **Wayback copy** | An archived snapshot of a web page or file at web.archive.org, used when the live link is dead |
| **STB** | Surface Transportation Board, the federal body that took over the remaining trucking-rate duties of the ICC (Interstate Commerce Commission) in 1996 |

---

## §0 Result in one table

**Verdicts on the 87 ledger rows**

| Verdict | Count | Rows |
|---|---|---|
| **KEEP-verified** | 71 | All rows not listed below |
| **KEEP-assumed** | 9 | C-AO10, C-AO41, C-AO57, C-AO58, C-AO59, C-AO70, C-AO71, C-AO72, C-AO73 (the researcher already labelled every one of these *assumed*) |
| **NARROW** | 6 | C-AO32, C-AO37, C-AO40, C-AO51, C-AO74, C-AO86 |
| **DISCARD** | 1 | C-AO47 |
| Not checked | 0 | — |

**Verdicts on the researcher's proposed question verdicts (§0 of the checked file)**

| Question | Proposed verdict | Mine | Reason |
|---|---|---|---|
| **H09-C1a** (published rules on short pays and offsets) | Answered from the web | **AGREE**, with two corrections | The rules exist as quoted, and the cited tariffs are still current (TForce, XPO and ABF were reissued in 2026 with the same words). **Correction 1:** the list of carriers that revoke discounts misses **FedEx Freight** (Item 435 ¶5A), so it is five carriers, not four. **Correction 2:** the reading "the rules are settled and one-sided" needs a counterweight. The STB said in 1997 that liquidated damages "must bear a reasonable relationship" to collection costs and were "never intended … as a penalty upon a shipper" (§6, CE-1). The rules on paper are answered. Whether they hold against a good-faith short pay is not |
| **H09-C1b** (short pays in practice) | Not answerable from the web | **AGREE** | No count or cost was found by the researcher or by me. The §0 phrase "trucking dilution under 3% is the norm" overstates the SFNet deck, which gives it as an example (C-AO40) |
| **H09-C2** (would carriers pay for faster payment) | Narrowed | **AGREE**, with one correction | The broker quick-pay prices are confirmed, and Uber Freight's 2% is now confirmed from an archived copy. **Correction:** "Big LTL carriers instead charge payers 2-3% for card payments" fails for FedEx Freight. Its 3% card charge sits in the **Intra-Canada** section only (C-AO47, DISCARD), so only ABF's 2% is a verified US card surcharge |
| **H09-C4** (auditor claims) | Narrowed | **AGREE**, with one correction | TForce's guarantee-refund bar and FedEx Freight's "debtor only" rules for its Close of Business and A.M. delivery services are firm. FedEx's Money-Back Guarantee exclusion is **discretionary** ("At the sole discretion of FedEx Freight … may not be honored"), not "outright" (C-AO51) |
| **A09-11** (will shippers share under an NDA) | Narrowed | **AGREE** | All four confidentiality clauses read as quoted. A search found the FedEx third-party NDA clause in five Middle East and Africa templates and in a signed 2023 agreement that incorporates US terms, but still no US-published copy. The count "8 of 10 LTL rules tariffs have no rate-confidentiality item" holds |
| **D-16 (a)** (1099 threshold) | Answered from the web | **AGREE** | Confirmed in the IRS instructions (the same file is the current revision) and in the statute: 26 U.S.C. 6041(a) says "$2,000", amended by Pub. L. 119-21 §70433(a), for payments made after 2025-12-31 |
| **D-16 (b)** (gift caps, incentive norms) | Narrowed | **AGREE** | Flex, DRiV, the SIS screener and the panel figures read as quoted |
| **D-18** (NDA templates, retention) | Answered for templates; Narrowed for retention | **AGREE** | The Common Paper MNDA and DPA clauses read as quoted. The repository's last commit is 2022-06-07, as stated |
| **D-19** (recruiting time, reply rates) | Narrowed | **AGREE**, with corrections to the inputs | The much-quoted **3.43% comes from one origin, Instantly's 2026 report**. Woodpecker's blog repeats it and credits Instantly in its own FAQ (§2). Smartlead's 0.74% is counted **per person contacted**, not per email. So the worked example counts people, not emails (C-AO74) |

---

## §1 Discards and narrowings (most consequential first)

### 1.1 Ledger rows

| Claim ID | What was claimed | What the source actually says (quote) | Verdict | Why |
|---|---|---|---|---|
| **C-AO47** | "FedEx Freight adds 3% to card payments" (used in §0 and §AO2.1: "Big LTL carriers instead charge payers 2-3%") | FedEx Freight 100-Y, PDF p. 57, under the header "Rules Tariff – Intra-Canada Section 2B": "435-2B CREDIT CARD PAYMENTS CCHF 1. Payment … can be made by credit card subject to an additional 3% handling charge." No card surcharge appears in the US section (full-text search for "credit card") | **DISCARD** for US use | Wrong population. The "-2B" suffix marks the Intra-Canada section. The true, restricted reading (3% on intra-Canada shipments) has no use for our US segment. The US section's Item 435 ¶2.C.1 (discounts may be adjusted by payment type, C-AO82) stands. **§0 H09-C2 should read:** "ABF charges payers 2% on certain business card payments; FedEx Freight may adjust discounts by payment type" |
| **C-AO37** + §AO1.2 | Under a full-rate rule, real ABF bill 150235531 would rise from $942.02 to $9,063.10, about 9.6× | Arithmetic confirmed against the court record ("AMOUNT DUE: $942.02"; "DISC 89.5% -6,232.60"; "FUEL SURCHARGE FSC 30.3% 221.55"; "DYNAMIC DISCOUNT DYNDISC -181.83"). The STB said in 1997 that liquidated damages "must bear a reasonable relationship to the costs of the carrier's collection effort" | **NARROW** | **Reading to keep:** "On paper, a whole-bill full-rate rule applied to a bill of this shape would multiply it about 9.6-9.8 times. The federal regulator's stated view is that such charges must track collection costs, so this is a ceiling written in tariffs, not an exposure shown to be enforceable." Three reasons. (1) The bill's "dynamic discount" (−$181.83) is also a discount; under "all discounts are revoked" it would go too, giving $9,244.93 (9.81×). (2) The STB statement (§6, CE-1) cuts against reading the multiple as a likely cost. (3) Estes's rule rates "based on the applicable NMFC rating(s)", and this bill moved at exception class 70 against NMFC class 100, so the rate base itself is uncertain |
| **C-AO32** (and the §AO1.3 design reading) | FedEx Freight Item 438 "makes a dispute through its channels the thing that stops the clock" | Item 438 ¶3: "Invoices not disputed via one of the channels above are due and payable by Customer within the agreed-upon payment terms." Item 435 ¶5 (same page): "If Carrier is forced to utilize an outside collection source … Revocation of all applicable discounts and allowances, resulting in collection of gross charges." | **NARROW** | **Reading to keep:** "Item 438 names FedEx Freight's dispute channels and says undisputed invoices are due on terms; it does not say that a channel dispute suspends payment terms or the Item 435 collection penalty." The quote is exact. "Stops the clock" is an inference the text does not make. The design advice "dispute before payment through each carrier's channel" is still sensible, but it is not shown to protect the payer |
| **C-AO74** (§AO7 worked example) | Emails needed for 5 interviews: 1,352 at 0.74%; 667 at 1.5%; 292 at 3.43% | Smartlead: "The typical sender earns one reply per 135 contacts, a 0.74% reply rate." Woodpecker: "the median reply rate is 1.5% (56,614 campaigns)." Instantly: "The overall average reply rate is 3.43%" | **NARROW** | **Reading to keep:** "At published cold-sales benchmarks, 5 held interviews need roughly 290-1,350 *people contacted* (each typically sent a multi-email sequence), assuming half of replies book." The arithmetic is right. The unit is people contacted, not emails. The three rates are cross-industry sales benchmarks from vendors that sell email tools. The 3.43% has one origin (Instantly), not two (§2) |
| **C-AO51** (and §AO3 "bar agents … outright") | FedEx Freight's Money-Back Guarantee "may not be honored" for third-party requests, listed with TForce as a "hard exclusion" | Item 760 ¶6: "Limitation: At the sole discretion of FedEx Freight, the Money-Back Guarantee may not be honored when the request is made by … a third party other than the payer of the charges." | **NARROW** | **Reading to keep:** "FedEx Freight may, at its discretion, refuse Money-Back Guarantee requests made by a third party, and pays any refund to the debtor only; its Close of Business and A.M. Delivery refunds are available 'upon request of the debtor only'." The ledger quote leaves out "At the sole discretion of FedEx Freight". The same discretionary wording is in FedEx's 2021 parcel terms. TForce's bar ("No agent … may request") is firm. FedEx's is firm only for Items 756 and 757 |
| **C-AO40** (as used in §0 H09-C1b) | "trucking dilution under 3% is the norm in one association deck" | SFNet deck p. 7: "A trucking company with dilution <3%, the advance rate may be 90% or more. A construction company may have dilution of 15%" | **NARROW** | **Reading to keep:** "SFNet's training deck defines dilution to include short pays and offsets, and uses '<3% dilution → 90%+ advance' as an example for a trucking client." It is an example, not a measured norm. The ledger row says so already; the §0 wording does not |
| **C-AO86** | Quick pay on a $2,000 load costs $25-$80; low end is U.S. Bank at 1.25% on 45-day terms | U.S. Bank agreement (R 9.2020), Schedule 1: "Base Rate 1%" … "For every 0.25% band that the Wall Street Journal Prime Rate exceeds the applicable Floor Rate, the Discount Fee will increase by two and one-half basis points" (floor 6%, "no maximum") | **NARROW** | **Reading to keep:** "$25 is a floor; U.S. Bank's fee also rises by 0.025 points for each quarter point that the prime rate sits above 6%." Example: at a prime rate of 6.75-6.99%, the 45-day fee is 1.10% + 0.25% = 1.35%, or $27. The researcher's "1% base, +0.25% to +1.00% by terms" leaves out this add-on. The prime rate for 2026 was not checked (no search spent) |

### 1.2 Body findings that do not trace to a ledger row

| Where | What the file says | What the sources show | Effect |
|---|---|---|---|
| §AO1.1 FedEx row; §AO1.3 reading; §0 H09-C1a | FedEx Freight penalty: "Not read in full (budget)". Full-rate pricing listed for "four carriers (Saia, Estes, XPO, R+L)" | FedEx Freight Item 435 ¶5, US section, PDF p. 19 (the same item the file cites for the credit period): "Revocation of all applicable discounts and allowances, resulting in collection of gross charges." | **Five** carriers revoke discounts: Saia (automatically), Estes (after notice), and XPO, R+L and FedEx Freight (on referral to collection). This adds to the file's reading and does not contradict it |
| §AO1.3, GSBCA row | "the carrier protested; the board held most claims time-barred". Government deduction "not read here, *assumed*" | Decision: "Agency determinations of carrier overcharges for shipments became final because **the carrier** waited beyond the three-year period to submit most claims". The statute it cites allows a claim within three years after "a deduction pursuant to statute. 31 U.S.C. 3726(a)" | The time-barred claims were the **carrier's** challenges, so the government's overcharge demands stood. The government's deduction right is named in the decision, so that point can move from *assumed* to *verified* (out of segment either way) |
| §AO1.2 caveat | "No tariff read says whether discount revocation applies to the whole bill or only the unpaid part" | R+L Item 775 ¶1: "Forfeiture of all discounts … on all unpaid freight bills". 49 CFR 377.203(g)(2)(iii): damages "Shall be applied only to the nonpayment of original, separate and independent freight bills" | Both texts work at the level of the whole bill, which points toward whole-bill revocation. Neither settles a *partial* short pay. The caveat stands, but now has text behind it (logged in §4) |
| Sources N-AO01, N-AO03, N-AO07 (currency) | TForce 102-T eff. 2026-03-16; XPO CNWY 199-AK.1 eff. 2026-02-16; ABF 111-AU dated 2026-06-22 | Newer reissues exist: TForce 102-T eff. **2026-08-03** and **2026-08-17**; XPO **AK.2** (2026-05-18) and **AK.3** (2026-08-17, the one XPO's tariff library now lists); ABF 111-AU "Last revised: August 21, 2026" | **Every quoted sentence is unchanged** in the newest reissue (checked phrase by phrase). Page numbers shift by +1 for TForce and XPO. The file should cite the current reissues. No verdict changes |
| §AO2.1 RXO row | All three RXO options are "via TriumphPay" | RXO: "Advance Pay has a 4.0% fee, but cannot be requested or managed through TriumphPay". RXO's options page: "For a 4% fee per transaction, RXO will pay you via Comchek within one hour from the time you submit your completed paperwork" | Minor. The 4% is for payment within an hour after proof of delivery, outside TriumphPay. Werner's "Advance Pay" is a different product: a fuel advance of 40% at pickup for a $10 fee |
| §AO1.3 FreightWaves row (N-AO18) | "the page carries a 'Sponsored' label" | The page code shows `"isSponsored":""` (empty) and no visible "Sponsored" text. The piece sits in a contributed category ("the-playbook"), and its author is listed with a logistics company's email domain | The *assumed* label stays, for a different reason: it is a contributed column by someone with a commercial interest, not a labelled advertisement |
| Coincidence watch, 180 days | Start points listed for XPO, Saia, FedEx, TForce, AAA Cooper | ODFL Item 396: "180 days after Carrier's receipt of the shipment"; ABF Item 428: "within 180 days of the initial shipment date" | Two more carriers start the clock at the shipment, not the invoice. That shortens the real claim window. Add them to the list |

---

## §2 Coincidences found

| Figure | Where it appears | True origin and relationship | What to do |
|---|---|---|---|
| **3.43% cold-email reply rate** | Web Tonic manufacturing page ("Instantly"); Web Tonic trucking page ("Woodpecker's own platform data (20M+ emails)"); check V N-V26 (Instantly); Woodpecker blog ("Average cold email reply rate: 3.43% platform-wide") | **One origin: Instantly's "Cold Email Benchmark Report 2026"** (page "Updated January 12, 2026"): "The overall average reply rate is 3.43%". Woodpecker's blog (published 2026-02-24) calls it platform-wide, but its own FAQ says "3.43%, based on Instantly's benchmark analysis". It also repeats Instantly's "42% of replies from follow-ups". The "20M+ emails" is Woodpecker's total send volume, not the base of the 3.43%. Woodpecker's own measured figure is a **1.5% median** | Merge into one source: Instantly, a vendor, *assumed*. Web Tonic's trucking-page attribution is wrong. This settles the researcher's open item |
| **Woodpecker 1.5% vs 3.43%** | Web Tonic pages; Woodpecker's benchmark tool and blog | Different metrics. The 1.5% is a median of campaign reply rates ("last 90 days, 2025 · updated 2026-08-05"). The 3.43% is Instantly's average | Look-alike sources. Do not treat them as two readings of one rate |
| **0.74% and "top 10% clear 2.6%"** | Web Tonic trucking page | **Origin: Smartlead's benchmark page.** "one reply per 135 contacts, a 0.74% reply rate"; top 10% "a reply every 38 contacts" (= 2.63%). The unit is **people contacted**, for senders with at least 500 emails. "H1 2026" was not found on Smartlead's page | One source. Change the unit in any worked example |
| **"Full undiscounted rate" penalties** | Saia, Estes, XPO, R+L, FedEx Freight | All five implement 49 CFR 377.203(g)(1)(ii) ("require payment of the full, nondiscounted rate"); Saia cites it by number | Five carriers sharing one regulatory template is not independent evidence that the penalty is enforced or common in practice |
| **FedEx "consent plus NDA" clause** | Middle East template (N-AO12); five more Middle East and Africa templates (Kenya, Egypt, Saudi Arabia, Bahrain, Kuwait); a signed 2023 agreement in a UK public contract notice | One corporate template. The UK copy names US documents (FedEx Ground Economy terms, the FedEx Freight 100 Series Rules Tariff) | Counts as one FedEx drafting choice, not an industry norm. It does make US use somewhat more likely (§6, CE-7) |
| **"Third party other than the payer" (FedEx)** | FedEx Freight Item 760 ¶6; FedEx 2021 parcel terms | Same company and same wording, **including "At the sole discretion of FedEx"** in both | Confirms the researcher's entry. Both are discretionary |
| **3%** | FedEx Freight card charge; Con-way immediate pay (2008); TriumphPay flyer (snippet) | The FedEx 3% is Intra-Canada only (C-AO47) | The look-alike is weaker than the file says: the FedEx figure does not even apply to US shipments |
| **2%** | Uber Freight quick pay; TriumphPay Select Carrier "starts at 2%" (FreightWaves, 2020-12-11); ABF card surcharge | Uber Freight's 2% is now confirmed from an archived copy of its agreement. TriumphPay's 2% is a platform rate across brokers | Broker quick-pay figures cluster at 2%, partly through one platform (TriumphPay). The ABF 2% is a different product paid by shippers |
| **"TriumphPay shares the fee with the broker"** (coincidence watch, "search only") | FreightWaves, per a search result | The FreightWaves Select Carrier article (2020-12-11) was fetched. It contains no statement about sharing or splitting the fee | Not supported by the page read. Logged as unproven (§4). The shared-platform point stands without it |
| **Advance Pay** | RXO 4%; Werner "Advance Pay $10 service fee" | Same name, different products: RXO pays the full invoice within one hour after proof of delivery; Werner advances 40% at pickup for fuel | Look-alike names. Do not compare the prices |

---

## §3 Arithmetic re-done

| Row | Researcher's calculation | Redone | Result |
|---|---|---|---|
| C-AO37 | $942.02 + $6,232.60 + $1,888.48 = $9,063.10; 9.62× | Inputs confirmed on the court record. Net linehaul $6,963.80 − $6,232.60 = $731.20. Fuel 30.3% × $731.20 = $221.55. Bill total $6,396.25 + $567.55 − $6,232.60 + $22.00 + $149.10 + $221.55 − $181.83 = **$942.02**. Fuel on gross 30.3% × $6,963.80 = $2,110.03, so the change is +$1,888.48. New total **$9,063.10, 9.621×** | **Correct** as stated. If the dynamic discount is also revoked: $9,244.93 (9.814×). Narrowed in §1 |
| §AO1.2, ABF 30% | 30% × $149.10 = $44.73 | $44.73 | Correct |
| C-AO50 | 2.5% × 365 ÷ 29 = 31% a year | 31.47%. On the net amount received (fee taken off the invoice): 2.5 ÷ 97.5 × 365 ÷ 29 = 32.27% | Correct ("about 31%") |
| C-AO74 | 5 ÷ (0.0074 × 0.5) = 1,352; 5 ÷ 0.0075 = 667; 5 ÷ 0.01715 = 292 | 1,351.4 → 1,352; 666.7 → 667; 291.5 → 292 | Arithmetic correct. The unit is wrong for Smartlead (people contacted, not emails). Narrowed |
| C-AO86 | $2,000 × 1.25% / 2.5% / 4% / 1.5% = $25 / $50 / $80 / $30 | Same | Correct as arithmetic. U.S. Bank's prime add-on makes $25 a floor. Narrowed |
| C-AO87 | $2,000 ÷ $200 = 10 calls | 10. The threshold is "$2,000 or more", so the tenth call reaches it | Correct |
| C-AO08 | 2 of 10 LTL tariffs have a rate-confidentiality item | Full-text search of the 8 other files for "confiden", "disclos", "proprietary" and "strict confidence". The word "confidential" appears only in blind-shipment items (XPO, Saia, SEFL, AAA Cooper), and not at all in ODFL, Estes, ABF or R+L | Correct |
| §AO2.1 worked example | $2,000: RXO $50, $80; Werner $30; U.S. Bank $25 | Same | Correct |

---

## §4 Concerns, unproven (verdicts unchanged)

1. **Saia's "automatic" revocation vs the federal rule.** Saia Item 435 Sec. C applies revocation "automatically … without the need for Carrier to reinvoice Payor". 49 CFR 377.203(g)(2)(vi) says such damages "shall be applied only … when the carrier has issued a revised freight bill or notice … within 90 days". The two may conflict. No ruling on Saia's wording was found. C-AO14 is unchanged: the tariff says what the file says.
2. **Whole bill or unpaid part.** R+L's and the regulation's wording works at the level of the bill (§1.2). Whether a partial short pay puts the whole bill's discount at risk remains a question for a carrier's credit team or a lawyer.
3. **Whether disclosure to one's own agent under an NDA counts as "disclosure"** under FedEx Freight Item 250. Item 250 binds "Consignor and Consignee" and has no agent carve-out. TForce's Item 130 expressly contemplates agents and auditors. Whether a court would treat a shipper's sharing with its auditor as a breach of Item 250 is a legal question. Nothing found answers it.
4. **US use of the FedEx consent-plus-NDA clause** (C-AO05). Still no US-published copy, though the 2023 UK-notice agreement that incorporates US terms makes it more likely (§6, CE-7).
5. **TriumphPay fee-sharing** (coincidence watch). Not found in the FreightWaves article fetched.
6. **Smartlead's period.** Web Tonic says "H1 2026". Smartlead's page, as fetched, does not state a period in the text read.
7. **Saia currency.** Saia 170-D (eff. 2025-10-01) is the newest found. One search found no 170-E, and Saia's tariff page is a script-only app. A newer reissue cannot be ruled out.
8. **The prime rate in 2026**, which sets the size of U.S. Bank's add-on, was not checked.
9. **J&J's carrier guide is dated January 2014.** The FAP practices it shows (weekly short-pay reports, 30-day rejection) may have changed.
10. **The FreightWaves 2026 column's author** is listed with a logistics company's email domain. A commercial interest is possible but not shown.

---

## §5 Full verdict table

**URL key** (each cell cites a key; quotes are verbatim and 40 words or fewer):

| Key | URL |
|---|---|
| TF | https://tforcefreight.com/downloads/UPGF-102-T-20260817.pdf (current reissue; the cited 2026-03-16 file https://www.tforcefreight.com/downloads/UPGF-102-T-20260316.pdf has the same words) |
| FXF | https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf |
| TSA | https://www.fedex.com/content/dam/fedex/meisa-middle-east/campaign/FedEx_Transportation_Services_Agreement.pdf |
| YRC | https://storage.courtlistener.com/recap/gov.uscourts.deb.198600/gov.uscourts.deb.198600.1.1.pdf |
| XPO | https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.3_Eff._08.17.2026.pdf (current; the cited AK.1 file has the same words) |
| SAIA | https://assets.ctfassets.net/kjv8gs2ccggb/3Y5vAsxznsXornATV1AG5D/ffe12c504b75b780d9462fa25f9f0329/Saia_170D_10012025.pdf |
| EST | https://www.estes-express.com/dA/ea677fdb-3bfa-45fb-9ef8-511174177f84/EstesRulesTariff.pdf |
| ODFL | https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/Complete%20ODFL%20100-Q%20Tariff.pdf |
| ABF | https://arcb.com/sites/www/files/2026-08/ABF-111-AU-08-21-2026.pdf (current revision; the cited 2026-06-22 file has the same words) |
| RL | https://rl-cdn.com/docs/rlc/rules/rl-rules.pdf |
| SEFL | https://www.sefl.com/vsmisc/RT1090%20Full.pdf |
| AAA | https://www.aaacooper.com/docs/default-source/default-document-library/tariff/RulesTariff190.pdf |
| LAND | https://www.landstar.com/media/vduhe3j1/land-100-a-march-17-2020.pdf |
| FW20 | https://www.freightwaves.com/news/what-about-shippers-confidentiality-issues-among-concerns-in-broker-transparency-hearing |
| FW26 | https://www.freightwaves.com/news/you-delivered-that-load-three-weeks-ago-here-is-why-you-still-do-not-have-the-money-and-what-to-do-about-it |
| U13708 | https://www.law.cornell.edu/uscode/text/49/13708 |
| CFR377 | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-49?part=377 |
| JNJ | https://jnj.ctlogistics.com/sites/default/files/docs/jnj_freight_payment_carrier_guide.pdf |
| SFN | https://www.sfnet.com/docs/default-source/uploadedfiles/factoring-module-1-deck.pdf |
| GSB | https://www.gsbca.gsa.gov/rate/m140550.txt |
| RXO | https://rxo.com/carriers/carrier-payment-options/rxo-triumphpay/ |
| WER | https://www.werner.com/carrier-payment-options/ |
| CON | https://www.con-way.com/resources/quick_pay_registration.pdf |
| USB | https://s203.q4cdn.com/711684571/files/doc_news/2020/06/News-Release-06-10-2020-1703080680821272.pdf |
| USBA | https://www.usbank.com/dam/documents/pdf/splash/corporate-payments/transportation/US-Bank-Carrier-Application-and-Agreement.pdf |
| LOOP | https://help.loop.com/articles/9657000706-quickpay |
| UBER | https://web.archive.org/web/20250114042015id_/https://www.uberfreight.com/wp-content/uploads/2023/10/Uber_Freight-Quick_Pay_Agreement.pdf (live URL returns 404) |
| XPOC | https://www.xpo.com/cdn/files/s1/Overcharge_Claim_Process_02-24-26.pdf |
| PAP | https://www.fedexfreight.com/content/dam/web/ca/documents/overcharge-claims-form.pdf |
| LOA | https://www.logisticsplus.com/wp-content/uploads/2015/10/LP-LOA-Letter-of-Authorization-Template.docx |
| BEN | https://www.beneschlaw.com/insight/trucking-rate-payment-and-collection-rules-of-the-road/pdf/ |
| NSR | https://nshift.com/hubfs/nShift-Audit-RFP-pack.pdf |
| NSB | https://nshift.com/blog/freight-audit-checklist-before-the-first-invoice |
| IRS | https://www.irs.gov/pub/irs-prior/i1099mec--2026.pdf (identical to the current https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| U6041 | https://www.law.cornell.edu/uscode/text/26/6041 |
| FLEX | https://flex.com/downloads/supplier-practice-guidelines |
| DRIV | https://www.drivparts.com/en-in/suppliers/purchasing/ethics-statement.html |
| SIS | https://www.surveymonkey.com/r/usa-tires |
| CPN / CPC / CPD | https://raw.githubusercontent.com/CommonPaper/Mutual-NDA/main/Mutual-NDA.md ; …/Mutual-NDA-coverpage.md ; https://raw.githubusercontent.com/CommonPaper/DPA/main/DPA.md |
| NACHA | https://www.nacha.org/rules/supplementing-data-security-requirements |
| RALLY | https://help.rallyuxr.com/articles/9829874426-recruiting-with-user-interviews |
| RESP | https://www.respondent.io/marketplace |
| WT1 / WT2 | https://www.webtonic.io/blog/trucking-and-logistics-email-marketing-statistics ; https://www.webtonic.io/blog/manufacturing-and-industrial-cold-email-outbound-statistics |
| INST | https://instantly.ai/cold-email-benchmark-report-2026 |
| WPM | https://woodpecker.co/cold-email-benchmarks/ |
| SML | https://www.smartlead.ai/benchmarks/state-of-cold-email |
| ATA | https://trucking.org/national-accounting-finance-council |
| PA | https://storage.courtlistener.com/recap/gov.uscourts.cacb.1993985/gov.uscourts.cacb.1993985.920.0_1.pdf |
| STB | https://www.stb.gov/wp-content/uploads/archived-press-release/htmls/43BD2DD0715452748525652A0045FB3A.html.pdf |

| Claim ID | Test(s) run | Verdict | Reason | Evidence (key + quote) | New label |
|---|---|---|---|---|---|
| C-AO01 | 1-7 (6: search 1, current reissue) | KEEP-verified | Exact. Unchanged in the 2026-08-17 reissue (p. 13) | TF Item 130: "held in strict confidence by all parties, including the agents of the customer, and may not be disclosed unless required by law or as expressly permitted by a written agreement" | *verified* |
| C-AO02 | 1-7 | KEEP-verified | Exact. The researcher's "ambiguous" reading is fair: the item contemplates auditors seeing rates | TF Item 130: "to notify any Third Party or auditor of the confidential nature of the rates and charges, except to the extent expressly permitted by a written agreement" | *verified* |
| C-AO03 | 1, 2, 5 | KEEP-verified | Exact; the carrier's own right | TF Item 100 ¶13: "may disclose information as specifically required by law or for payment and audit purposes" | *verified* |
| C-AO04 | 1-7 (6: search 3, search 6) | KEEP-verified | Exact. It binds "Consignor and Consignee"; there is no agent or auditor carve-out. Whether sharing with one's own agent breaches it is a legal question (§4) | FXF Item 250: "are confidential and shall be held in strict confidence by all parties and may not be disclosed unless required by law" | *verified* |
| C-AO05 | 1-7 (6: search 3) | KEEP-verified (template) | Exact. It is a Middle East FedEx Express/TNT template. The same clause sits in a 2023 signed agreement that incorporates US terms; there is still no US-published copy | TSA §6: "disclosure by Customer of this Agreement or any terms to any third party without consent by FedEx and execution of a mutually agreeable non-disclosure agreement between FedEx and such third party shall be considered a breach" | *verified* (template); US use *assumed* (unchanged) |
| C-AO06 | 1-7 | KEEP-verified | Exact, Art. 23(e), p. 13. One negotiated contract with a large shipper | YRC: "e) to auditors, accountants, major lending institutions or legal counsel retained by a party for the purpose of assessing the accuracy of freight charges." | *verified*; large shipper |
| C-AO07 | 1, 2 | KEEP-verified | Exact, p. 10 | YRC Art. 13: "Payments shall be made exclusively by First Brands Group or its freight payment agent." | *verified* |
| C-AO08 | 1-7 | KEEP-verified | Count reproduced by full-text search (§3) | SAIA: "Carrier will not ensure the confidentiality of the transaction." (blind shipments only) | *verified* **[our calc]** |
| C-AO09 | 1-4 | KEEP-verified | Quote exact; FreightWaves reporting a speaker; about brokers | FW20: "shippers don't want their competitors to know what they're paying for freight" | *verified* as reported |
| C-AO10 | 1, 2 | KEEP-assumed | Quote exact; a commenter | FW20: "shippers "consistently" require nondisclosure agreements with brokers" | *assumed* |
| C-AO11 | 1, 2 | KEEP-verified | Exact. The invoice itself must show the actual rates, which supports asking for invoices first | U13708 (a): "presented or electronically transmitted for payment to the person responsible … or agent of such responsible person, the actual rates, charges, or allowances" | *verified* |
| C-AO12 | 1, 2 | KEEP-verified | Exact, p. 38 | FXF Item 765: "Freight Payment Processor (commonly referred to as "Bill-To"): A bank or freight payment agency designated to pay the freight charges" | *verified* |
| C-AO13 | 1-7 (6: search 10) | KEEP-verified | Exact, Item 1030 ¶7, p. 146. No Saia dispute carve-out found | SAIA: "Short payment or taking credit for any freight bills by any party is not permitted." | *verified* |
| C-AO14 | 1-7 (6: search 4) | KEEP-verified | Exact. Counter-evidence logged: STB 1997 (CE-1) and a possible tension with 377.203(g)(2)(vi) (§4) | SAIA Item 435 Sec. C: "all discounts are revoked … This provision applies automatically at the expiration of the authorized credit period, without the need for Carrier to reinvoice Payor" | *verified* (rule); enforceability not shown |
| C-AO15 | 1-7 | KEEP-verified | Exact; 25% (min $132.50) and 50% (min $265.00) | SAIA Item 435 Sec. B: "within sixty (60) calendar days of presentation of the Freight Bill will result in the following late payment service charges" | *verified* |
| C-AO16 | 1-7 | KEEP-verified | Exact, p. 47 | SAIA Item 435 Sec. H: "without offset for any cause, including but not limited to, cargo claims and overcharge claims" | *verified* |
| C-AO17 | 1-7 (6: search 8, AK.3) | KEEP-verified | Exact. Unchanged in AK.3 (p. 32) | XPO Item 207: "When shipments are assigned or placed with a collection agency, attorney or authorized agent for collection, all discounts are revoked" | *verified* |
| C-AO18 | 1, 2, 5 | KEEP-verified | Exact; unchanged in AK.3 | XPO Item 207: "An invoice dispute is insufficient grounds for debtor to withhold payment of any other valid invoices." | *verified* |
| C-AO19 | 1-7 (6: search 4) | KEEP-verified | Exact, Item 720 ¶3c, p. 63. The 10-20 day window after notice is confirmed | EST: "Non-payment after this time period, will result in the shipper paying the carrier's full undiscounted, class rates applicable at the time of the shipment, based on the applicable NMFC rating(s)." | *verified* |
| C-AO20 | 1-7 | KEEP-verified | Exact, Item 825, p. 76 | EST: "not permitted to offset any part of the freight charges by the value of any outstanding loss and damage, overcharge or over-collected claims" | *verified* |
| C-AO21 | 1-7 (6: search 7, Aug 2026 revision) | KEEP-verified | Exact; unchanged in the 2026-08-21 revision | ABF Item 427 ¶2B: "will be subject to a late payment fee of thirty percent (30%) of the unpaid amount." | *verified* |
| C-AO22 | 1-7 | KEEP-verified | Exact, p. 64. File "Updated: October 5, 2026" | ODFL Item 564 ¶1: "within forty-two (42) days from the original invoice due date to avoid payor being charged an assessment of liquidated damages in an amount equal to 35% of the unpaid receivable" | *verified* |
| C-AO23 | 1, 2 | KEEP-verified | Exact | ODFL Item 564 ¶6: "shall not be deemed as payment received by the Carrier" | *verified* |
| C-AO24 | 1-7 | KEEP-verified | Exact, p. 39 | ODFL Item 396: "Carrier will not open new overcharge claims on any invoice for which a closed overcharge claim exists." | *verified* |
| C-AO25 | 1-7 | KEEP-verified | Exact, p. 117, "Updated 10/05/2026" | RL Item 775 ¶2: "A penalty of 125% of the remaining freight bill amount due subject carriers after having added back any forfeitures" | *verified* |
| C-AO26 | 1-7 | KEEP-verified | Exact, p. 128; 25% in ¶4 | SEFL Item 817 ¶6: "unless a formal claim is filed and has been finally processed" | *verified* |
| C-AO27 | 1-7 | KEEP-verified | Exact; unchanged in the reissue | TF Item 721 ¶3: "a service charge of 1.5% per month (or fraction thereof) will be assessed and due on the unpaid balance" | *verified* |
| C-AO28 | 1-7 | KEEP-verified | Exact. Note the scope: the claim closes where the claimant accepts a payment on a declined or partly settled claim | TF Item 813: "the Claimant accepts the payment, the matter will be considered closed and no further claims for the same shipment will be honored" | *verified* |
| C-AO29 | 1-7 | KEEP-verified | Exact, p. 12 | AAA Item 210 ¶2: "Any freight bill not paid within 60 calendar days of the ship date will be assessed liquidated damages of 35% of the unpaid receivable." | *verified* |
| C-AO30 | 1-7 (6: search 5) | KEEP-verified | Exact, p. 34. "Responsible party" may mean the payer of record, not "no agent". No carrier rule on LOAs for claims was found | AAA Item 660: "must be submitted within 180 days of shipment date and must be submitted by the responsible party of the freight charges" | *verified* |
| C-AO31 | 1, 2 | KEEP-verified | Exact | AAA Item 210 ¶5: "will pay freight charges twice in the event the third party or broker fails to pay freight charges to CARRIER" | *verified* |
| C-AO32 | 1-7 | **NARROW** | Quote exact; the body's "stops the clock" is not in the text (§1) | FXF Item 438 ¶3: "Invoices not disputed via one of the channels above are due and payable by Customer within the agreed-upon payment terms." | *verified* (quote); inference *[our call]* |
| C-AO33 | 1-7 | KEEP-verified | Exact, US section p. 46 (repeated in the Intra-Canada section, p. 61) | FXF Item 960 ¶9: "Customer shall not deduct or offset any cargo claim or other alleged claim or debt of Carrier … unless authorized in writing by Carrier." | *verified* |
| C-AO34 | 1-7 | KEEP-verified | Exact, Rule 850, p. 50; 15-day credit in Rule 435 confirmed | LAND: "Payor's obligation to pay freight and ancillary charges in full is absolute and shall not be affected or reduced by any event or occurrence including, but not limited to, any setoff or counterclaim" | *verified*; 2020 file |
| C-AO35 | 1-7 (6: search 4) | KEEP-verified | Exact. The STB's 1997 reading of (g)(1) is logged (CE-1) | CFR377 (g)(1)(ii): "The second method is to require payment of the full, nondiscounted rate instead of the discounted rate otherwise applicable." | *verified* |
| C-AO36 | 1-7 | KEEP-verified | Exact. Also note (g)(2)(iii): applies only to "original, separate and independent freight bills" | CFR377 (g)(2)(iv): "Shall not apply to instances of clear clerical or ministerial error such as non-receipt of a carrier's freight bill" | *verified* |
| C-AO37 | 1-7 | **NARROW** | Arithmetic correct; reading narrowed (§1, §3) | PA: "DISC 89.5% -6,232.60 … FUEL SURCHARGE FSC 30.3% 221.55 DYNAMIC DISCOUNT DYNDISC -181.83"; STB: "must bear a reasonable relationship to the costs of the carrier's collection effort" | **[our calc]**; ceiling on paper |
| C-AO38 | 1-7 | KEEP-verified | Exact. 2014 document, large shipper | JNJ: "Short pay Reports - available weekly reports on all invoices that are short paid and the reasonings" | *verified*; out of segment, dated |
| C-AO39 | 1, 2 | KEEP-verified | Exact | JNJ: "After 30 days, the FBs will be rejected." | *verified* |
| C-AO40 | 1-7 | **NARROW** | The figure is an example, not a norm (§1) | SFN p. 7: "A trucking company with dilution <3%, the advance rate may be 90% or more." | definition *verified*; figure *assumed* (example) |
| C-AO41 | 1-4 | KEEP-assumed | Exact. No "Sponsored" flag; a contributed column (§1.2) | FW26: "many non-recourse agreements only cover broker bankruptcy or business closure - not a broker who disputes the invoice, claims a short delivery, or simply refuses to pay" | *assumed* |
| C-AO42 | 1, 2 | KEEP-verified | Quote exact; the body paraphrase needs fixing (§1.2) | GSB: "Agency determinations of carrier overcharges for shipments became final because the carrier waited beyond the three-year period to submit most claims" | *verified*; out of segment |
| C-AO43 | 1-7 | KEEP-verified | Exact; page modified 2026-03-26. Advance Pay is outside TriumphPay (§1.2) | RXO: "QuickPay has a 2.5% fee per transaction … Advance Pay has a 4.0% fee, but cannot be requested or managed through TriumphPay" | *verified* (own terms) |
| C-AO44 | 1-7 | KEEP-verified | Exact; also on TriumphPay | WER: "2.5% next day and 1.5% 5-day payment options (service fee deducted from total invoice)" | *verified* (own terms) |
| C-AO45 | 1-7 | KEEP-verified | Exact; PDF from 2008 | CON: "Immediate Pay: a 3% fee will be deducted from the total agreed upon payment for the shipment." | *verified*; dated |
| C-AO46 | 1-7 | KEEP-verified | Exact. The fee is in the carrier agreement, with a prime add-on (C-AO86) | USB: "typically anywhere from 45 and up to 90 days - new flexibility to accelerate cash flow when needed … for a fee" | *verified* |
| C-AO47 | 1-7 | **DISCARD** (US use) | Intra-Canada section only (§1) | FXF p. 57, "Rules Tariff – Intra-Canada Section 2B … 435-2B CREDIT CARD PAYMENTS … subject to an additional 3% handling charge" | intra-Canada only |
| C-AO48 | 1-7 | KEEP-verified | Exact; unchanged in the 2026-08-21 revision | ABF Item 721: "a two percent (2%) handling surcharge will be applicable on all service fees and charges. This rate is the same or lower than our cost of acceptance" | *verified* |
| C-AO49 | 1, 2, 5 | KEEP-verified (upgraded) | Live PDF 404; the Wayback copy (2025-01-14) confirms it. Current status unknown | UBER: "less a discount of two percent (2%) of such amount … within two (2) business days following Uber Freight's receipt, review and approval of the required shipment documents" | *verified* (archived, Jan 2025) |
| C-AO50 | 1, 7 | KEEP-verified (arithmetic) | 31.5% (32.3% on net) | inputs C-AO43, C-AO44 | **[our calc]** |
| C-AO51 | 1-7 | **NARROW** | Discretionary, not a bar (§1) | FXF Item 760 ¶6: "At the sole discretion of FedEx Freight, the Money-Back Guarantee may not be honored when the request is made by … a third party other than the payer" | *verified*; discretionary |
| C-AO52 | 1-7 | KEEP-verified | Exact, pp. 32, 33, 36. Items 756 and 757 also say "upon request of the debtor only" | FXF: "Carrier will not issue refunds or credits to third parties and/or agencies." | *verified* |
| C-AO53 | 1-7 (6: search 1) | KEEP-verified | Exact; unchanged in the reissue (p. 63). Items 823 and 826 refund only the guarantee surcharge; Items 822 and 825 refund freight charges | TF Item 823 ¶6: "No agent, representative, or third party may request cancellation or refund on behalf of the payer and no refunds will be made to any party other than the payer." | *verified* |
| C-AO54 | 1-7 | KEEP-verified | Exact. The agreement goes to the carrier that is party to it, so there is no confidentiality issue | XPOC: "If the claim is related to a pricing agreement or tariff, copies of those documents must also be provided" | *verified* |
| C-AO55 | 1, 2 | KEEP-verified | Exact; form PAP201/315, Canadian copy | PAP: "BOND OF INDEMNITY: The undersigned guarantees to protect any carrier having an interest against any and all loss, costs, and expenses" | *verified* |
| C-AO56 | 1-4 | KEEP-verified | Exact; does not mention claims | LOA: "authorization to send invoices that are third-party billed to (Client Name) c/o Logistics Plus Inc. … for auditing and payment purposes" | *verified* |
| C-AO57 | 1, 2 | KEEP-assumed | Exact; a law firm summary dated 2025-01-13 | BEN: "Today publishing rate tariffs is only strictly required for household goods or traffic in the noncontiguous domestic trade under 49 USC § 13702." | *assumed* |
| C-AO58 | 1, 2 | KEEP-assumed | Exact; vendor | NSB: "Procurement may hold the contract while logistics owns the shipment data and finance receives the bill." | *assumed* |
| C-AO59 | 1, 2 | KEEP-assumed | Exact. The retention schedule "completes at GA", so it does not exist yet | NSR: "The Audit-specific security documentation set (data residency statement, retention schedule, sub-processor list, AI data-handling note) completes at GA" | *assumed* |
| C-AO60 | 1-7 (6: statute fetched) | KEEP-verified | Exact. The statute confirms it, and the cited file is the current revision | IRS p. 1: "For tax years beginning after 2025, the minimum threshold amount … increased to $2,000"; U6041: "Pub. L. 119-21, § 70433(a), substituted "$2,000" for "$600"" | *verified* |
| C-AO61 | 1-7 | KEEP-verified | Exact, p. 5 | IRS: "A payment or series of payments made to individuals for participating in a medical research study or studies." | *verified* |
| C-AO62 | 1-7 | KEEP-verified | Exact, Rev C, PDF dated 2024-04-29 | FLEX §5.2: "Gifts in cash or cash equivalents from existing or prospective suppliers are always prohibited." | *verified*; large firm |
| C-AO63 | 1-7 | KEEP-verified | Exact. India-locale page of a large group | DRIV: "accepting only noncash gifts of insignificant value (under $50 USD) … no employee or family members may receive a cash equivalent from any supplier or customer" | *verified* |
| C-AO64 | 1-7 | KEEP-verified | Exact. Business respondents (roles include owner, finance, purchasing) | SIS: "We are providing compensation of $150 for those who qualify, are selected, and successfully complete an approximately 60-minute Zoom video interview." | *verified* (offer) |
| C-AO65 | 1-7 | KEEP-verified | Exact §2 (an HTML tag sits inside the sentence) | CPN: "may disclose Confidential Information to its employees, agents, advisors, contractors and other representatives having a reasonable need to know for the Purpose" | *verified* |
| C-AO66 | 1-7 | KEEP-verified | Exact §6 | CPN: "the Receiving Party may retain Confidential Information in accordance with its standard backup or record retention policies or as required by law" | *verified* |
| C-AO67 | 1-7 | KEEP-verified | Exact. Both defaults are bracketed fill-ins, with an "In perpetuity" box | CPC: "[1 year(s)] from Effective Date, but in the case of trade secrets until Confidential Information is no longer considered a trade secret" | *verified* |
| C-AO68 | 1-7 | KEEP-verified | Exact §7.2(a). It covers personal data only, not rate agreements | CPD: "After the DPA expires, Provider will return or delete Customer Personal Data at Customer's instruction unless further storage … is required or authorized by Applicable Law." | *verified* |
| C-AO69 | 1-7 | KEEP-verified | Exact. It applies to ACH originators above 2 million entries, so it is an analogy for us | NACHA: "protect DFI Account Numbers used in the initiation of Entries by rendering them unreadable when stored electronically" | *verified* |
| C-AO70 | 1-7 | KEEP-assumed | Exact; a vendor figure relayed by a partner, "Last updated 22 hours ago" | RALLY: "Median minutes to first qualified applicant: 77 minutes Median hours to first confirmed session: 24 hours" | *assumed* |
| C-AO71 | 1-7 | KEEP-assumed | Exact; marketing claim | RESP: "Your first qualified participant in 15 minutes." | *assumed* |
| C-AO72 | 1-7 (6: origin fetched) | KEEP-assumed | Origin confirmed at Smartlead. The unit is people contacted; "H1 2026" is not on the origin page | SML: "The typical sender earns one reply per 135 contacts, a 0.74% reply rate." | *assumed* (vendor, per contact) |
| C-AO73 | 1-7 (6: origin fetched) | KEEP-assumed | Origin confirmed at Woodpecker: a campaign median, last 90 days of 2025 | WPM: "the median reply rate is 1.5% (56,614 campaigns)" | *assumed* (vendor) |
| C-AO74 | 1-7 | **NARROW** | Unit and origin corrected (§1, §2) | INST: "The overall average reply rate is 3.43%"; SML: "one reply per 135 contacts" | **[our calc]**; people contacted |
| C-AO75 | 1, 2 | KEEP-verified | Exact | ATA: "NAFC's Study Groups are: Taxation, Accounting Principles, Credit & Collection, Financial Relations, Risk Management and Information Technology." | *verified* |
| C-AO76 | 1-7 | KEEP-verified | Exact, p. 38 | ODFL Item 395: "may not offset any part of freight charges on any outstanding loss and damage, overcharge, or over collected claim" | *verified* |
| C-AO77 | 1-7 | KEEP-verified | Absence reproduced ("offset", "set-off", "setoff", "set off", "deduct", "withh", "short pay": none). An R+L credit-period item does exist | RL: no match for the offset terms in the 133-page file "Updated 10/05/2026" | *verified* (search) |
| C-AO78 | 1-7 | KEEP-verified | Exact; unchanged in the Aug 2026 revision | ABF Item 427 ¶3: "as result of any overcharge claim, charge back, duplicate payment or loss and/or damage cargo claim" | *verified* |
| C-AO79 | 1-7 | KEEP-verified | Exact; unchanged in AK.3 (p. 19) | XPO Item 23(5): "Debtor shall not have the right to withhold or offset the payment of charges for any reason, including but not limited to, claims for lost or damaged goods." | *verified* |
| C-AO80 | 1-7 | KEEP-verified | Exact; unchanged in the reissue (p. 21) | TF Item 166 Part 13: "may not be offset by customer, shipper, consignee or payer against freight charges otherwise owed to Carrier" | *verified* |
| C-AO81 | 1-7 | KEEP-verified | Exact, p. 33 | AAA Item 649: "is not permitted to offset any part of the freight charges by the value of any outstanding loss and damage, overcharge or over-collected claims" | *verified* |
| C-AO82 | 1, 2 | KEEP-verified | Exact, US section, p. 19 | FXF Item 435 ¶2.C.1: "FedEx Freight may consider payment type in determining pricing and discounts, and reserves the right to adjust discounts based on payment type." | *verified* |
| C-AO83 | 1, 2 | KEEP-verified | Exact | WER: "Balance of invoice is paid within 30 days of receipt of invoice, POD, lumper receipts, etc., or by Quick Pay" | *verified* |
| C-AO84 | 1, 2 | KEEP-verified | Exact; 2014 | JNJ: "enables discount payment terms for our carriers that opt to participate in the program" | *verified*; dated |
| C-AO85 | 1, 2 | KEEP-verified | Exact; "Last updated 1 year ago" | LOOP: "QuickPay is a payment option offered to carriers to get paid for delivered loads faster for a discounted rate." | *verified* |
| C-AO86 | 1, 2, 7 | **NARROW** | Prime add-on omitted (§1) | USBA Schedule 1: "Base Rate 1% … For every 0.25% band that the Wall Street Journal Prime Rate exceeds the applicable Floor Rate, the Discount Fee will increase by two and one-half basis points" | **[our calc]**; $25 is a floor |
| C-AO87 | 1, 7 | KEEP-verified (arithmetic) | 10 calls | IRS p. 2: "At least $2,000 in: … Other income payments (box 3)" | **[our calc]** |

---

## §6 Counter-evidence and leads

**Searches used (10):** (1) TForce rules tariff 2026 → reissues of 2026-08-03 and 2026-08-17; (2) Saia 170-E → nothing usable; (3) the FedEx consent-plus-NDA phrase → Middle East and Africa templates and a UK 2023 agreement; (4) court or regulator rulings on discount revocation → STB 1997, *Humboldt Express v. Wise* (4th Cir. 1999), *Delta Traffic Service v. Mennen* (D.N.J. 1990); (5) LOAs for third-party overcharge claims → no carrier rule; one newsletter; (6) FAP onboarding and carrier consent → a vendor FAQ; (7) ABF 111-AV → 111-AU revised 2026-08-21; (8) XPO CNWY 199 2026 → AK.2, then AK.3 from XPO's library page; (9) early-payment discounts and carriers → leads only; (10) Saia dispute process and late-fee waivers → Union Pacific's (rail) policy, PITT OHIO Item 725.

**Counter-evidence** (each tied to a claim; logged, not a new finding):

| ID | Source | What it says (quote) | Bears on |
|---|---|---|---|
| CE-1 | STB press release No. 97-60, 1997-07-28, comments filed in *In re Humboldt Express* (Bankr. W.D.N.C.). STB | "where no collection attempt has been made, the appropriate remedy for a late payment is to assess reasonable interest charges … the liquidated damages provision … was never intended … as a penalty upon a shipper or to provide a windfall for a trucking company." | C-AO14, C-AO17, C-AO19, C-AO25, C-AO35, C-AO37; §AO1.3's "settled and one-sided". It is persuasive commentary, not a ruling, and dates from 1997. It tempers any reading of full-rate revocation as a likely cost of a good-faith short pay |
| CE-2 | 49 CFR 377.203(g)(2)(vi), CFR377 | "shall be applied only after the authorized credit period, and when the carrier has issued a revised freight bill or notice of imposition of collection expense charges for late payment within 90 days" | C-AO14 (Saia's "without the need for Carrier to reinvoice") |
| CE-3 | FedEx Freight Item 435 ¶5, FXF p. 19 | "If Carrier is forced to utilize an outside collection source … Revocation of all applicable discounts and allowances, resulting in collection of gross charges." | §AO1.1, §AO1.3 count (adds FedEx Freight) |
| CE-4 | Instantly, *Cold Email Benchmark Report 2026* (INST), updated 2026-01-12 | "The overall average reply rate is 3.43% with top-performers of users exceeding 10% reply rates" | C-AO74; coincidence watch (single origin) |
| CE-5 | Woodpecker benchmark tool (WPM), updated 2026-08-05 | "Across the whole platform … the median reply rate is 1.5% (56,614 campaigns)." | Woodpecker's own measure is not 3.43% |
| CE-6 | Uber Freight Quick Pay Agreement, Wayback copy 2025-01-14 (UBER) | "less a discount of two percent (2%) of such amount" | C-AO49 (upgraded) |
| CE-7 | FedEx Transportation Services Agreement, signed 2023, UK Contracts Finder attachment https://www.contractsfinder.service.gov.uk/Notice/Attachment/657f57b8-dcd7-4e89-b24d-f2bd963c1d66 | Same §6 clause; incorporates "the FedEx Freight 100 Series Rules Tariff, the FedEx Ground Economy terms at https://www.fedex.com/content/dam/fedex/us-united-states/…" | C-AO05: makes US use more plausible; still not a US-published copy |
| CE-8 | Court record of the ABF bill (PA), p. 17 | "W02/AUTH:Reweigh - See W&R certificate for details.// … W01/AUTH:Restore original weight// … PQ SCHEDULE NO" | C-AO37. The bill moved under a pricing quote, and its "dynamic discount" is tied to that quote, which would also fall under "all discounts revoked" |

**Leads** (not findings; for the founders or a later check):

| ID | Lead | Where | Why it may matter |
|---|---|---|---|
| L-1 | *Humboldt Express v. Wise Co.*, 190 F.3d 624 (4th Cir. 1999): a tariff that revoked discounts and added a 30% late charge, challenged as unreasonable | CourtListener search result (full text not readable, §7) | The only appellate case found on loss-of-discount penalties. The outcome on reasonableness was not read |
| L-2 | *Delta Traffic Service v. Mennen* (D.N.J. 1990): per a third-party summary, a loss-of-discount provision was held unenforceable | Search 4 summary only | Possible precedent against revocation; unread |
| L-3 | Union Pacific (rail) late-payment Q&A: "If the dispute results in a correction to the freight bill it will not be subject to the late payment finance charge … the time that the freight bill was in dispute will be excluded" | https://www.up.com/shipping/resources/latepayqa | A large carrier that carves out disputes. Rail, so out of segment. A model question for trucking carriers |
| L-4 | PITT OHIO Item 725: 10% of net revenue from day 61, then a collection expense charge; no dispute carve-out seen | https://pittohio.com/myPittOhio/RulesTariff/725 | An eleventh LTL tariff for the H09-C1 table |
| L-5 | Newsletter "LOAs in LTL – It's a Broken Process" (2024-05-31): LOA misuse "has led to a growing sense of skepticism among LTL carriers" | https://lets-talk-logistics.beehiiv.com/p/loas-ltl-broken-process | About pricing LOAs, not claims. A probe for carrier interviews (H09-C4) |
| L-6 | Lojistic FAQ: "All UPS and FedEx customers have a confidentiality clause in their carrier agreement(s)" | https://www.lojistic.com/shipping-faqs/parcel-freight-contract-negotiation-questions | A vendor treats confidentiality as a routine shipper objection (parcel). Relevant to A09-11 |
| L-7 | TForce Item 170 ¶2: delinquent participants forfeit "any allowance, discount, or incentive payment" | TF | A sixth, narrower forfeiture rule (incentive programs only) |
| L-8 | Rally's panel pricing for User Interviews recruits: "Moderated B2B $65" per participant | RALLY | A budget input for D-16 and D-19 |
| L-9 | Search summaries: broker quick pay "1-3%… with 2% being the most common", and dynamic discounting has had little traction in trucking | Search 9 (otrucking.com; FreightWaves "New twists in freight invoice factoring"); not read | Context for H09-C2; vendor or aggregator claims |

---

## §7 Could not access

- **4th Circuit opinion, *Humboldt Express v. Wise* (1999):** FindLaw returned 403; Public.Resource.Org returned status 451; the CourtListener opinion page returned an empty 202 (a bot check); CourtListener's opinion API needs a login (not attempted). Only the caption and the start of the opinion were read, from the CourtListener search API.
- **STB press release HTML pages:** 404. Read the PDF copies on stb.gov instead (same text in both releases).
- **XPO "Overcharge Claims Overview External LINKED" PDF:** 404 (storage error).
- **7bridges audit help page:** 404.
- **Uber Freight Quick Pay Agreement:** live URL 404. Read the Wayback copy of 2025-01-14 instead. The Wayback availability API returned 429; the index query worked.
- **Saia's tariff page:** script-only app; no file list was readable. The newest revision could not be confirmed (§4).
- **Not checked for newer reissues:** AAA Cooper 190-AF (eff. 2025-12-22), Estes EXLA 105 (FF Revision 3, PDF dated 2026-08-02), SEFL 1090 (PDF dated 2026-08-11), Landstar LAND 100-A (2020). FedEx Freight (items revised to 2026-10-01), ODFL (updated 2026-10-05) and R+L (updated 2026-10-05) are recent on their face.
- **The 2026 prime rate** (sets U.S. Bank's add-on): not checked.
- **Respondent's "30 Mins" median** (coincidence watch, snippet only): not checked.
