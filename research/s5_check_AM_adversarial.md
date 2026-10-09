# S5 check AM, adversarial review

- **What this is:** an adversarial check of check AM's web evidence. The founders asked for "adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data". Each claim was tested to see whether it breaks. No objection was invented: a claim that survives is reported as a result too.
- **File checked:** `research/s5_check_AM_c09_leak_and_recovery.md` (74 ledger rows, §0 verdicts, body sections, Coincidence watch). It was not edited.
- **Date:** 2026-10-07. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.**
- **Searches used:** 9 of the 10 allowed. **Fetches made:** about 70: page and PDF downloads, Wayback copies, 2 CourtListener search-API queries, and eCFR version lists. Downloads are kept in the session scratchpad.
- **No identity was sent. Nobody was contacted.** No logins, forms, API keys or PACER. SEC EDGAR was not fetched; FedEx Freight's 10-K was read on the company's own investor-relations site.
- **Rows checked in full (all seven tests):** 50. These are the 33 load-bearing (Y) rows plus 17 N rows that feed a number or verdict in §0 (C-AM02, 13, 22, 23, 24, 26, 27, 28, 29, 49, 51, 56, 59, 61, 62, 63, 65).
  - **Sampled:** 22 rows, at least the existence test, covering every question: C-AM06, 12, 14, 17, 36, 37, 39, 43, 44, 45, 53, 57, 60, 64, 66, 67, 68, 70, 72, 73, 74, 75.
  - **Not checked:** 2. C-AM69 is reachable only on EDGAR. C-AM71 is a TRID search that was not re-run.
- **How labels are used here:** **KEEP-verified** means the row's own sentence is true as written about its own population (government, a co-op survey, one carrier). Where that population is not our segment, the "New label" column adds "*assumed* as a stand-in for our segment". **KEEP-assumed** means the number itself is a vendor figure, a self-report or a secondary source.

**Words used here:**
- **Flagged / identified:** an auditor says a charge is wrong.
- **Collected / credited:** the money came back.
- **Self-report:** a figure supplied by the party whose work it measures. An example is an auditor reporting its own finds.
- **Denominator:** the base a percentage is taken of.
- **Look-alike:** two equal-looking numbers that measure different things.
- **Pre-payment audit:** a bill is checked before it is paid.
- **Post-payment audit:** a bill is checked after it is paid, and the money is claimed back.
- **Chevron:** a court rule, overruled by the Supreme Court in 2024, that told judges to defer to an agency's reading of an unclear statute.
- **OIRA:** the White House office that reviews draft regulations before they are published.

---

## §0 Result in one table

**Row verdicts**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|
| 46 | 15 | 11 | **0** | 2 |

**No row is discarded.** Every quote that was re-fetched is in its source, word for word, and every [our calc] reproduces. What breaks is how some numbers are read:
- the biggest federal billing-stage figure is mostly one auditor's self-report;
- the DoD "≈1.5%" is the higher of two years;
- the 0.068% is a yield on estimated total spend;
- the Texas 69% is not a false-flag rate;
- the "unsettled law" on contract freight rests on a case that did not decide the point.

**Verdicts on the §0 question rows**

| Question | Proposed verdict | This review | Reason |
|---|---|---|---|
| A09-01 the leak | Narrowed | **AGREE**, with two wording corrections | Nothing measures our segment. But the federal pre-payment figures are **auditor self-reports**, and **one firm supplies 79% of the FY2011 flags**: 4.67% on its own billings, while the other four auditors pooled 1.66%. "Neutral government regimes" that "bracket" 1.5% overstates it. They are reference points, not bounds, and the DoD ≈1.5% is the high year of two (§1, rows 1-2). The §0 statement that "passenger bills" are mixed in is unsupported. |
| A09-02 share one audit catches | Narrowed | **AGREE** | GAO 1992's 72-78% stays the only recall measure. The Texas 69% "rejected" cannot stand in for precision, because some rejected flags were errors the agencies had already fixed (§1, row 7). |
| A09-03 share credited | Narrowed | **AGREE** | No in-segment number. Note that the Texas 24% was cut short by the contract ending early. |
| A09-10a law, direct LTL tariff freight | Answered | **AGREE** | Statute, STB release, 10th Circuit and tariffs all re-read. Detail: some tariffs and contracts require an "action or proceeding … commenced" within 180 days. That is stricter wording than the statute's "contest" (FedEx Freight 100-Y Item 438; YRC-First Brands Art. 14). |
| A09-10b contract freight | Narrowed | **AGREE with the verdict; the stated reason needs correcting** | The 4th Circuit's *Gaines* decided only whether a federal court could hear a carrier's suit, and never addressed 13710(a)(3)(B). The 10th Circuit (*Southern Furniture*) said 14101 "says nothing that contradicts, or even calls into question" the 180-day limit. Better wording: "untested for contract truckload freight. The only appellate statements lean towards the 180-day rule applying unless a contract expressly waives it." How often contracts waive it still cannot be answered from the web. |
| A09-10c broker-billed freight | Narrowed | **AGREE**, wording fix | Part 378's text does settle that it covers carriers only. 13710(a)(3)(B), the shipper's rule, does not name who billed, so "texts settle the scope" is too strong for 13710. Two more public broker terms found (15 days and 10 days), so no counter-example. |
| A09-10d in-window share | Narrowed | **AGREE** | All 15 cells reproduce. The 46% Amazon figure comes from a roughly 4-year look-back and does not belong next to the 12-month shares (§1, row 9). A monthly-cycle calculation is added in §3. |
| A09-13 decay | Narrowed | **AGREE** | Three corrections. The Texas row is not a decay measure. The "fall after the 1998 pre-payment mandate" link is weakened, because agencies largely did not comply. Newer GSA collections (FY2021-23) are now found (§6). |

---

## §1 Discards and narrowings (most important first)

No row is discarded. Eleven are narrowed, and seven body statements need the same treatment (B1-B7 below the table).

| # | Claim ID | What was claimed | What the source actually says (quote ≤40 words) | Verdict | Why, and the restricted reading |
|---|---|---|---|---|---|
| 1 | **C-AM01** | Federal pre-payment auditors flagged 3.37% of initial billings in FY2011; §0 treats this as the top of a "neutral" bracket | GSA OIG 2013, App. A: "Obtained relevant transportation data from five prepayment contract auditors to determine the amount of transportation overcharges". Table II: "National Traffic Service 16 $64,919,906 $3,029,262" | **NARROW** | The OIG compiled the auditors' own reports and does not say it verified them. One freight-audit firm reports $3.03M of the $3.85M; the other four pool to **1.66%** **[our calc]**. **Restricted reading:** in FY2011, five contract auditors reported flagging 3.37% of $114M of federal billings. One firm reported 4.67% on 57% of the billings and the rest 1.66%. Self-reported, flagged not credited, government tender freight mixed with household goods. |
| 2 | **C-AM08** | GSA's post-payment audits identified $33.9M of DoD PowerTrack overpayments, "≈1.49%" of FY2007 payments | DoD IG D-2009-072, fn. 6: "These are summary results as provided by the Director GSA Transportation Audit Division. We did not verify their accuracy". p. 12 fn. 13: "We did not determine whether these are mutually exclusive." | **NARROW** | The ratio is right, but four things limit it. (a) FY2007 is the high year: FY2006's $9.4M is 0.41-0.94% on any FY2006 base of $1.0-2.3B, and the two years together give **0.95-1.32%** **[our calc]**. (b) PowerTrack carried ocean freight too, and the IG did not check overlap with $14.1M of ocean duplicate payments. (c) The vendors told the IG that GSA "will identify between three and five percent", while GSA's own figure was a third to a half of that. (d) GSA's own programme later repaid $29.6M of overcharge notices to one DoD vendor as erroneous (§6). **Restricted reading:** an unverified GSA summary of "improper or duplicate" payments across all PowerTrack modes, about 1-1.5% of payments. |
| 3 | **C-AM18** (and C-AM61) | Federal post-payment audits issue overcharges of about 0.068% of annual bills | GSA OIG 2014, p. 1: "the estimated $16.3 billion in annual transportation bills". fn. 2: modes include "air cargo, air passenger, domestic household goods". p. 8: "over 6,000 rail freight bills not audited by the second tier contractor." | **NARROW** | The arithmetic is right. But the base is an estimate of all FY2012 federal transportation spending, air passenger travel included, not the bills actually audited. The OIG documents bills never submitted and second-tier audits skipped. **Restricted reading:** about $11M a year of overcharge notices on bills paid 2007-09, set against estimated total federal transportation spending. That is a programme yield, not an error rate on audited freight bills. |
| 4 | **C-AM42** and the A09-10b reason | The 4th Circuit said Chapter 137's collection rules are "not implicated" without a tariff, making the law on contract freight "unsettled in the courts" | *Gaines*, p. 3: "whether, absent a federal tariff, federal courts have subject matter jurisdiction over a motor carrier's breach of contract claim against a shipper for unpaid freight charges." | **NARROW** | The quote is exact, but the case is about whether a federal court can hear the suit at all. It discusses 13710(a)(1), 13706 and 14705, never (a)(3)(B). Counter-evidence: *Southern Furniture* (10th Cir. 2021, pp. 13-14): "§ 14101 says nothing that contradicts, or even calls into question, § 13710(a)(3)(B)'s time limit". **Restricted reading:** one court tied Chapter 137's rate and collection provisions to tariffs when deciding jurisdiction; it did not rule on the shipper's 180-day notice. |
| 5 | **C-AM35** and §AM4.5 #4 | "The broker's record is a federal right" that the look-back can ask for | FMCSA NPRM 2024: "By phrasing the requirement as a private ''right to review,'' the original regulation did not prohibit a broker from requiring a waiver of the private ''right to review''" | **NARROW** | The text is exact, and §371.3 is unchanged in the eCFR: a single version on record, from 2016. But FMCSA itself says the right can be contracted away. Its 48-hour duty is still a proposal (trade press: a supplemental proposal went to OIRA in August 2026, *assumed*). **Restricted reading:** a right to see the record that a contract may waive. None of the seven public shipper-facing broker terms read here waives it expressly. |
| 6 | **C-AM32** | 13710's billing-dispute paragraph is framed around motor carriers, so "by their text" it does not reach a broker's bill | 13710(a)(3)(B): "If a shipper seeks to contest the charges originally billed or additional charges subsequently billed, the shipper may request that the Board determine whether the charges billed must be paid." | **NARROW** | (a)(2) and (a)(3)(A) name motor carriers; (a)(3)(B), the shipper's rule, does not say who billed. **Restricted reading:** the surrounding text points to carriers' bills. Whether the shipper's 180-day rule reaches a broker's invoice is not settled by the words and is untested in court (two searches found no case). |
| 7 | **C-AM23** and the §AM2 reading | In a state AP audit, agencies "rejected" 69% of flagged duplicate dollars, so audit precision can be far below recall | Texas 2021, p. 5: "Reasons an agency disagreed with Auditec findings include: • Agency has collected a refund for overpayment. • … • Payment was reversed, stopped or voided." | **NARROW** | The figures are exact (68.9% disagreed, 23.2% agreed, 7.8% still under review). But disagreement includes real errors the agencies had already caught. **Restricted reading:** 69% of flagged duplicate dollars were not left for the outside auditor to collect, partly as false flags and partly as errors already fixed. It is not a false-flag rate. |
| 8 | **C-AM24** | A state programme found 0.05% against an expected 0.1% (A09-13), and collected 24% of valid claims (A09-03) | Texas 2023 letter: "the vendor declined to exercise the renewal option and the contract ended on August 31, 2021. According to the vendor, the engagement was not profitable" | **NARROW** | The figures are exact. "0.05% vs 0.1%" is the contingency auditor's own conclusion against an industry norm, not against an earlier year, so it is not a decay series. Valid claims were 0.0016% of eligible spend **[our calc]**. The 24% stops at an early contract end. **Restricted reading:** one state AP programme, government, not freight. Use for neither decay nor the credited share. |
| 9 | **C-AM56** and §0 A09-10d | "One real contract window cut a shipper's demand by about 46%", placed beside the 12-month shares | Central Freight complaint ¶35-36: Amazon "claims it overpaid from 2012 to June 2016"; "the Agreement provides that all claims by Amazon must be filed within 18 months of the original invoice" | **NARROW** | The 45.5% cut is right. But the demand covered about 4 years, the carrier says nothing was overcharged (it claims an oral price change was agreed), and the shipper is Amazon. **Restricted reading:** in one large-shipper dispute, an 18-month window removed 45.5% of a 4-year claim, on the carrier's account. It says nothing about a 12-month look-back. |
| 10 | **C-AM05** and §0 A09-01 | The pre-payment bills have "household goods and passenger bills mixed in" | GSA OIG 2013, p. 1: "TSP services include shipping goods (household and commodities) and transporting individuals (via airlines, trains, and ships)." | **NARROW** | The sentence describes the GSA division's whole remit, not Tables II-III. The five contractors are freight-bill and relocation auditors. Household goods are supported (a relocation firm and a move manager); passenger bills are not. |
| 11 | **C-AM22** | DFAS staff say a rapidly conducted audit identifies more errors | DoD IG, p. 6: "DFAS post-payment audit personnel, familiar with DFAS audits of DoD-wide payments, told us that the amount of overpayments identified … is directly related to the time elapsed" | **NARROW** | **Restricted reading:** an opinion about DoD-wide payment audits, not freight, and not measured. |

**Body statements (not ledger rows) that need the same treatment**

- **B1. §0 A09-01, "Two neutral government regimes now bracket it".** These are not neutral measurements.
  - **Pre-payment side:** contractor self-reports (row 1).
  - **Post-payment side:** run by contractors paid "Based on a negotiated percentage … for the overcharges that are successfully collected" (GSA OIG 2014, fn. 7).
  - **The same programme later repaid $29.6M of its own notices as erroneous** (§6).
  - **Better wording:** "government-compiled auditor figures from neighbouring populations". The §0 one-line reading ("billing-stage checks … find several percent") should say "auditors report several percent, mostly one firm".
- **B2. §AM1.3 #3 merges two opposite things.** In the GAO rail case, the Army's own paperwork errors made the shipper **overpay**. Those are overcharges caused by the shipper's documents, and possibly recoverable. The SJ repost says bill-of-lading errors make carriers correct bills **upward, legitimately**. GAO's $1.3M is not a "legitimate correction". Whether such overcharges count under the kill test ("billed wrong in the carrier's favour, provable") is a definition question for the founders. The sources do not answer it.
- **B3. §AM4.5 #2, "Monthly or pre-payment checking is the only version that reaches broker-billed freight".** By the arithmetic in §3, a monthly batch filed within 5 days of month end keeps 83% of bills inside a 30-day window. It keeps **0% inside a 5-day window and 17% inside a 10-day window**. **Restricted reading:** monthly checking reaches 30-day and 30-business-day broker windows if disputes are filed within days of month end. Windows of 5-10 days need checking on receipt of each invoice.
- **B4. §AM5, "The fall from ~$47M to ~$11-12M a year follows the pre-payment mandate"** (C-AM62 link, [our call]). The same GSA OIG 2013 report shows the mandate was largely not applied:
  - FY2011 compliance by department ran 0-77%, Defense 20% (Table I);
  - "only 54 percent of GSA's transportation expenses were subjected to prepayment audits".
  - Also, the comparison sets FY1987 **collections, before carrier refunds** (GAO 1989: $34M "disbursed … for carrier refunds and contract audit services", and a reserve "for settlement of carrier protests") against 2007-09 **overcharges issued**. The fall cannot be credited to the mandate.
- **B5. "What the web could not settle" #10 (the FMCSA broker-records rule) is now partly settled.** §371.3 was unchanged in the 2026-09-01 eCFR (one version on record), so the 2024 proposal was not final. Trade press says a supplemental proposal reached OIRA on 2026-08-27 (*assumed*).
- **B6. "Could not access", GSA budget justifications FY2022-2025.** Wayback copies exist and add facts (§6): GSA receipts of $12.7M (FY2021), $28.8M (FY2022, a one-off surge) and $12.4M (FY2023), and the $29.6M refund of erroneous notices.
- **B7. C-AM13 and C-AM15-16 carry a "fetch-tool extraction (curl 403)" flag.** All three pages loaded directly here (HTTP 200) and the quotes are verbatim, the SJ "97%" sentence included (row text in §5). The flag can be removed. The labels stay *assumed*, because the sources are vendors.

---

## §2 Coincidences found

**Shared origins (merge them into one source)**

| Figures | Rows | Single origin | Effect |
|---|---|---|---|
| $33.9M (DoD PowerTrack, FY2007); $33.1M (all agencies, bills paid 2007-09); $11M a year; OMB's "$12 million" target; GAO 1989's $47.2M; GSA receipts $12.7M / $28.8M / $12.4M (FY2021-23, new) | C-AM08, 18, 30, 59, 60, 61; §6 | **GSA's Transportation Audits Division**, reported through different auditors (DoD IG, GSA OIG, GAO, OMB, GSA's own budget) | One programme's own books. Matching scale (~$11-13M a year) is not corroboration. The $33.9M vs $33.1M clash is inside one source, so it weakens **both** C-AM08 and C-AM18/61, not only C-AM08 as check AM says. |
| 3.37%, 4.98%, 1.9%, 0.66-4.67% | C-AM01, 02, 03, 06 | **The contract auditors' own reports**, compiled by GSA OIG | One self-reported origin. One firm is 79% of the FY2011 dollars. |
| SJ "97%" accuracy and "about 50%" of BOLs wrong | C-AM15; Work Log 2026-09-22 | **One broker repost of one consultancy column** (2016-12-12, per a search summary) | One source, used twice in the project. The consultancy's own site says it argued for carriers to stop trusting shippers' BOL data and re-weigh instead (interest). The "50%" is stated as background ("Given that about 50%…"), not as a survey result. |
| 18 months | C-AM52 (Avient), C-AM56 (Amazon-Central Freight), Benesch | **The statute**, 49 U.S.C. 14705: Benesch says "Many transportation agreements will include this principle." | Like 180 days (already in check AM's watch), 18 months in contracts copies the statute; it is not independent drafting. |
| Broker dispute windows | C-AM47-51 plus two found here (EFL 15 days, Traffic Tech 10 days) | **Three template families**: "conclusively presumed to be valid" (GlobalTranz, AM LTL, EASE); "Customer is permitted … within the allowable … days" (Freightquote, TLI, Traffic Tech); "deemed valid" (EFL) | Seven public terms are about three independent drafts. The pattern of short windows still holds; no longer window was found. |
| Avient carriage terms | C-AM52, and C-AM25 "voluntary refund" | An old template: it cites "49 C.F.R. 1008", the pre-1996 number of Part 378, and repeats the STB's 1997 wording | Check AM already linked the refund clause to the STB. The template's age is new. |
| Fort Irwin (Army training centre) | C-AM12 (GAO 1988, rail overcharges) and GAO 1991 (§6 lead: 16% of pre-audited bills) | **The same installation** | Not two independent populations. |

**Look-alike numbers (equal values that measure different things)**

| Value | Where it appears | What each measures |
|---|---|---|
| ~1.5% | Model's overcharge rate; DoD ≈1.49%; GSA FY2011 ex-NTS 1.66% | The model's guess of provable overcharges as a share of spend; an unverified, multi-mode, FY2007-only "identified" figure; four auditors' self-reported flags on government bills |
| 3-5% | DoD IG vendor claim (C-AM09); GSA pre-payment pooled 3.37-4.98% (C-AM01/03); Tioga 3.5% (C-AM16) | A vendor prediction; auditor self-reports of flags; one broker's "recovered" share with no base. In the DoD report the vendors' 3-5% for the same payments was 2.0-3.4 times what GSA actually identified. |
| ~4.5-5% | AFS 4.5% (error count per audited invoice); NTS 4.67% and Table III 4.98% (dollars flagged) | Counts against dollars |
| 15-16% | Model "15% of invoices need a person"; GAO 1991 "overcharges on about 16 percent" of pre-audited bills | Review workload against bills found wrong. **Do not pair them.** |
| 180 days | 13710; GSA's 180-day / six-month **delay** of DoD audits (GSA OIG 2014 p. 4; DoD IG p. 5-6) | A shipper's statutory dispute window against an administrative audit delay |
| 60 days | Part 378 carrier decision (C-AM26); GSA's 60 days for a carrier to protest a notice (GSA OIG 2014 p. 2); GSA's 60-day goal for PowerTrack audits (DoD IG p. 6) | Three different clocks |
| 0.1% | PRG mature rate (C-AM64); Texas "expected 0.1 percent" (C-AM24) | Check AM already flags these as one industry rule of thumb. Confirmed: both are recovery-auditors' own statements. |

**Circular or indirect citations**
- C-AM18, 19, 20, 21, 30, 40, 64, 65, 73, 74 and 75 quote "see check X/AB/AC/T" instead of a verbatim passage. This review re-read every original except the Inbound Logistics vendor pages (403). All match the earlier checks.
- C-AM15 equals the project's earlier "SJ 97%" (same repost): one source, not two.

---

## §3 Arithmetic re-done

All **[our calc]** in check AM reproduce. Rows marked "new" are calculations added here, on the same sources.

| Item | Check AM | Recomputed | Result |
|---|---|---|---|
| C-AM01: $3,846,770 ÷ $114,216,991 | 3.37% | 3.368% | ✓ |
| C-AM01, **new**: the four contractors other than NTS | — | ($3,846,770 − $3,029,262) ÷ ($114,216,991 − $64,919,906) = **1.66%**; NTS alone 4.67% on 56.8% of billings | NTS is 78.7% of the flags |
| C-AM02: range and ratio | 0.66-4.67%; ≈7× | 0.661% (Lexicon) to 4.666% (NTS); ratio 7.06 | ✓ |
| C-AM03: $40,615,368 ÷ $815,189,005; median | 4.98%; 4.07% | 4.982%; median of ten 4.065%; Table III totals add up exactly | ✓ |
| C-AM03, **new**: without the Navy | — | ($40.62M − $24.08M) ÷ ($815.19M − $401.13M) = **3.99%**; Navy is 49.2% of billings and 59.3% of flags | Pooled figure is not driven by the Navy alone |
| C-AM06: $785,000 ÷ $41M | 1.9% | 1.91% | ✓ |
| C-AM08: $33.9M ÷ $2,276M | ≈1.49% | 1.489% | ✓ |
| C-AM08, **new**: FY2006 and the two years together (assumes FY2006 PowerTrack payments of $1.0-2.3B: DoD paid ~$1B a year before PowerTrack (C-AM68) and $2.276B in FY2007) | — | FY2006: $9.4M ÷ $1.0-2.3B = **0.41-0.94%**; FY2006-07: $43.3M ÷ $3.28-4.55B = **0.95-1.32%** | The 1.49% is the high year |
| C-AM09: 3% × $2.276B | $68.28M | $68.28M | ✓ |
| C-AM09, **new**: vendors' prediction against GSA's figure | — | 3% ÷ 1.489% = 2.0×; 5% ÷ 1.489% = 3.4× | Vendors overstated by 2.0-3.4× |
| C-AM12: $1.3M ÷ $3.0M | 43% | 43.3% (of "over $3 million", so at most 43%) | ✓ |
| C-AM13: 11,881 ÷ 250,000 | ≥4.75% | 4.752%; 4.5% would need ≈264,000 invoices | ✓ (check AM's flag stands) |
| C-AM14: type shares | 42.8 / 14.4 / 12.3 / 10.3; ~20% unclassified | 42.83 / 14.38 / 12.34 / 10.34; 20.1% | ✓ |
| C-AM18: ($33.1M ÷ 3) ÷ $16.3B | 0.068% | 0.0677% | ✓ (meaning narrowed in §1) |
| C-AM19: $2,193,447 ÷ $486.4M | 0.45% | 0.451% | ✓ |
| C-AM20: FedEx Freight give-backs ÷ revenue | 1.34-2.61% | FY2026 (101 + 83) ÷ 8,795 = 2.09%; FY2025 (8 + 111) ÷ 8,892 = 1.34%; FY2024 (11 + 235) ÷ 9,424 = 2.61% (IR copy of the 10-K) | ✓ |
| C-AM23: Texas duplicates | 68.9% / 23.2% | 68.94% / 23.23%; plus $281,107.66 (7.83%) still under review; the three parts sum exactly to $3,590,685.86 | ✓ |
| C-AM24: Texas | 24.4%; 0.0016% | $205,475 ÷ $840,613 = 24.44%; $840,613 ÷ $54B = 0.00156% | ✓ |
| C-AM30: ($33.1M − $6.3M) ÷ $33.1M | 81% | 80.97% (by value; GSA's own Figure 3 is by count) | ✓ |
| C-AM56: ($2,389,538 − $1,302,440) ÷ $2,389,538 | ~46% | 45.49% | ✓ (meaning narrowed in §1) |
| C-AM61: $33.1M ÷ 3 | ~$11M | $11.03M | ✓ |
| C-AM63: $9.4M → $33.9M | 260% | +260.6% | ✓ |
| C-AM59 vs C-AM61 | "fall from ~$47M to ~$11M" | Not like for like: FY1987 cash **collected, before carrier refunds**, against 2007-09 notices **issued**, counted by the year the bill was paid | The direction stands; the size of the fall is uncertain |

**§AM4.4 in-window table (C-AM55).** All 15 cells reproduce with share = max(0, window − delay) ÷ look-back, capped at 100%:

| Window | 12 months, file day 0 | 12 months, file day 30 | 24 months, file day 0 |
|---|---|---|---|
| 180 days | 49.3% | 41.1% | 24.7% |
| 30 days | 8.2% | 0% | 4.1% |
| 30 business days (≈42 days) | 11.5% | 3.3% | 5.8% |
| 5 days | 1.4% | 0% | 0.7% |
| 18 months (548 days) | 100% | 100% | 75.1% |

**New: share of bills still inside a broker's window under a monthly or weekly cycle [our calc].** Assumptions: bills spread evenly over a 30-day month, disputes filed d days after month end, window W counted from the invoice date. Share = min(1, max(0, W − d) ÷ 30). For weekly, a 7-day batch filed 2 days after the week ends.

| Broker window (W) | Monthly, file d = 0 | d = 5 | d = 10 | d = 15 | Weekly, d = 2 |
|---|---|---|---|---|---|
| 5 days (EASE) | 17% | 0% | 0% | 0% | 43% |
| 10 days (Traffic Tech) | 33% | 17% | 0% | 0% | 100% |
| 15 days (EFL, from receipt) | 50% | 33% | 17% | 0% | 100% |
| 30 days (GlobalTranz, AM LTL, Freightquote) | 100% | 83% | 67% | 50% | 100% |
| 30 business days (TLI) | 100% | 100% | 100% | 90% | 100% |

This is design arithmetic, not a decision. It narrows §AM4.5 #2 (see B3).

---

## §4 Concerns, unproven (verdicts unchanged)

1. **C-AM30, GSA's 81% "collected".** It is 1 − written-off ÷ issued. Whether "issued" still counts overcharges cancelled when a carrier's protest was allowed, or amounts still open, is not stated. The OIG itself calls the $6.3M "unable to collect", so the reading is consistent with the source.
2. **C-AM76, EASE's 14101(b) waiver.** 14101(b)(1) lets "a carrier" contract with a shipper, and FMCSA writes that "in most brokered transactions, the broker is not the shipper, and 49 U.S.C. 14101(b) does not apply" (NPRM 2024; said of broker-carrier contracts). A broker invoking 14101(b) may therefore have no legal effect. No court ruling was found, and the 5-day window binds as an ordinary contract term either way.
3. **Broker standing in the carrier's shoes.** EASE's terms say "EASE receives and reserves the Carrier's legal rights to collect payment from Customer". In a broker's collection suit, carrier-law rules (13710 included) might be argued. Untested.
4. **C-AM27, SFNet's "trucking company".** Factored trucking firms are typically small carriers whose customers are often brokers, which would make the example even further from shipper overcharge credits. The deck does not say.
5. **C-AM16, Tioga Pipe's size.** Whether the shipper has 20-499 staff (our segment) could not be found: its site is script-rendered and has no size information.
6. **C-AM01/02, NTS's 4.67%.** It may reflect its client and mode mix (16 agencies) as much as its skill. Not separable from the table.
7. **GSA receipts (§6).** Budget "receipts" are overcharges collected across all modes, air passenger included. The mix by mode is not stated.
8. **C-AM70.** The OIG says a February 2008 study measured FY2008 costs, a fiscal year then only five months old. A further reason to treat every federal denominator as soft.
9. **C-AM41, *NMFTA v. GSA*.** The holding on GSA's authority went through Chevron step two (Chevron was overruled in 2024). The quoted 13710 statement is the parties' shared position and is unaffected. GSA reports a later D.D.C. ruling upholding its audit authority again (§6).

---

## §5 Full verdict table

**Source key** (the URLs behind the short names in the Evidence column):
- [G13] GSA OIG A120060 (2013), https://gsaig.gov/sites/default/files/audit-reports/A120060_1.pdf
- [G14] GSA OIG A120169 (2014), https://www.gsaig.gov/sites/default/files/audit-reports/A120169_1.pdf
- [CJ25] GSA FY2025 budget narrative (Wayback), https://web.archive.org/web/20240313205044id_/https://origin-www.gsa.gov/system/files/16.%20FY2025%20CJ%20Permanent%20Authorities%20Narrative_Final.pdf
- [D09] DoD IG D-2009-072 (Wayback), https://web.archive.org/web/20120916052919id_/http://www.dodig.mil/Audit/reports/fy09/09-072.pdf
- [D01] DoD IG D-2001-148 (Wayback), https://web.archive.org/web/20120916222040id_/http://www.dodig.mil/Audit/reports/fy01/01-148.pdf
- [GAO88] https://gao.justia.com/general-services-administration/1988/5/army-transportation-nsiad-88-174
- [GAO89] https://gao.justia.com/general-services-administration/1989/8/transportation-audits-afmd-89-47
- [GAO92] https://www.gao.gov/assets/nsiad-92-157.pdf
- [GAO99] https://www.gao.gov/assets/t-nsiad-99-213.pdf
- [USDA] https://archive.org/download/cooperativefreig87mill/cooperativefreig87mill_djvu.txt
- [FDX] FedEx Freight 10-K FY2026 (investor-relations copy), https://ir.fedexfreight.com/financial-information/sec-filings/content/0001628280-26-053359/fdxf-20260531.htm
- [FXT] FedEx Freight 100-Y rules tariff, https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf
- [AFS] https://afs.net/blog/stats-incredible-common-ltl-invoice-errors/
- [SUN] https://www.suntecktts.com/?p=6005
- [SJS] the consultancy's own site, page ?p=13265 "End of Honor System". The domain is its principal's surname, so it is withheld under the no-names rule; it is reachable from a search for the survey.
- [TLIC] https://shiptli.com/case-studies/ltl-audit-recovery-program/
- [TLIT] https://translogisticsinc.com/terms-and-conditions (the same firm as TLI; the site links to shiptli.com)
- [TX21] https://fmx.cpa.texas.gov/fm/audit/recovery/rpt2021/Recovery_Audit_2021.pdf
- [TX23] https://fmx.cpa.texas.gov/fm/audit/recovery/rpt2023/RecoveryAuditReportLetterto88thLegislature.pdf
- [STB] https://stb.gov/wp-content/uploads/archived-press-release/htmls/05ACA69D02C0C7468525652900647A0C.html.pdf
- [SFN] https://www.sfnet.com/docs/default-source/uploadedfiles/factoring-module-1-deck.pdf
- [EASE] https://easelogistics.com/terms-and-conditions/
- [GTZ] https://www.globaltranz.com/terms-conditions/
- [AML] https://www.amtrucking.com/pickup-request.php
- [FQ] https://www.freightquote.com/terms-and-conditions/
- [AV] https://www.avient.com/content/terms-conditions-carriage
- [BEN] https://www.beneschlaw.com/insight/trucking-rate-payment-and-collection-rules-of-the-road/pdf/
- [USC10] https://www.law.cornell.edu/uscode/text/49/13710
- [USC14] https://www.law.cornell.edu/uscode/text/49/14101
- [C378] https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-49.xml?part=378
- [C371] https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-49.xml?part=371 (version list: https://www.ecfr.gov/api/versioner/v1/versions/title-49.json?part=371)
- [NPRM] https://www.govinfo.gov/content/pkg/FR-2024-11-20/pdf/2024-27115.pdf
- [GAI] https://www.ca4.uscourts.gov/Opinions/122269.P.pdf
- [NMF] https://ecf.dcd.uscourts.gov/cgi-bin/show_public_doc?2013cv0429-33
- [SF] https://storage.courtlistener.com/pdf/2021/03/03/southern_furniture_leasing_v._yrc.pdf
- [UPS] https://www.govinfo.gov/content/pkg/USCOURTS-mied-2_13-cv-15263/pdf/USCOURTS-mied-2_13-cv-15263-1.pdf
- [CL] CourtListener search API: https://www.courtlistener.com/api/rest/v4/search/?type=o&highlight=on&q= with `caseName:(Mastercraft) AND "13710"` and `caseName:(Barber) AND "13710(a)(3)(B)"`
- [LS] https://www.landstar.com/media/vduhe3j1/land-100-a-march-17-2020.pdf
- [CFA] https://storage.courtlistener.com/recap/gov.uscourts.wawd.245873/gov.uscourts.wawd.245873.1.0.pdf
- [YFB] https://storage.courtlistener.com/recap/gov.uscourts.deb.198600/gov.uscourts.deb.198600.1.1.pdf
- [WER] https://web.archive.org/web/20251107021304id_/https://www.werner.com/wp-content/uploads/2025/10/Tariff-Effective-10-14-2025.pdf
- [GSAD] https://www.gsa.gov/directives-library/gsa-delegation-of-authority-tts
- [OMB] https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/OMB/expectmore/detail/10004382.2006.html
- [NV] https://www.govinfo.gov/content/pkg/USCOURTS-gand-1_11-cv-00389/pdf/USCOURTS-gand-1_11-cv-00389-0.pdf
- [LOOP] https://www.loop.com/customer-story/great-dane

**Tests:** 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search or counter-fetch, 7 arithmetic.

| Claim ID | Test(s) run | Verdict | Reason | Evidence (source + quote) | New label |
|---|---|---|---|---|---|
| C-AM01 | 1-7 | **NARROW** | Exact. Contractor self-reports; one firm 79% of dollars; others 1.66% (§1 #1) | [G13] App. A-1: "Obtained relevant transportation data from five prepayment contract auditors to determine the amount of transportation overcharges" | *assumed* (self-report; government) |
| C-AM02 | 1-4, 7 | KEEP-assumed | Table exact; 0.661-4.666%; ratio 7.06. Each figure is the auditor's own | [G13] p. 6 Table II: "Lexicon Relocation 1 7,288,059 48,174 45,594 0" | table *verified*; as auditor performance *assumed* |
| C-AM03 | 1-7 | KEEP-assumed | Exact; 4.98%, median 4.07%. Auditor-reported; agencies chosen because they had data; without the Navy 3.99% | [G13] p. 6: "prepayment contract auditors identified nearly $41 million in overcharges during the 6-year period ended fiscal year 2011 (Table III)" | *assumed* (self-report; government) |
| C-AM04 | 1-6 | KEEP-verified | Definition exact | [G13] p. 6: "*Total Savings are the amounts saved due to identified overcharges." | *verified* |
| C-AM05 | 1-6 | **NARROW** | Describes the division's remit, not Tables II-III; passenger bills not shown (§1 #10) | [G13] p. 1: "TSP services include shipping goods (household and commodities) and transporting individuals (via airlines, trains, and ships)." | *verified* for scope only |
| C-AM06 | 1, 7 | KEEP-verified | Exact; 1.91% | [G13] p. 7: "one move manager identified $785,000 in transportation overcharges for 12 agencies with billings totaling $41 million." | *verified* (household goods); *assumed* as a stand-in |
| C-AM07 | 1-6 | KEEP-assumed | Exact, but the base is TRANSCOM's unaudited prototype data | [D09] App. A p. 13: "TRANSCOM stated that the data is not from official records and should not be audited. We did not verify the accuracy of the data." | IG report *verified*; $2.276B *assumed* |
| C-AM08 | 1-7 | **NARROW** | High year of two; multi-mode; overlap with ocean duplicates unchecked; unverified (§1 #2) | [D09] p. 4: "controls over PowerTrack ocean freight transportation payments were inadequate to prevent duplicate payments"; fn. 6: "We did not verify their accuracy" | *assumed* |
| C-AM09 | 1-7 | KEEP-assumed | Exact; $68.28M ✓. The vendors' 3-5% was 2.0-3.4× GSA's own figure | [D09] p. 6: "Recovery audit companies indicate that GSA will identify between three and five percent in transportation overpayments." | *assumed* (unchanged) |
| C-AM11 | 1-6 | KEEP-verified | Exact; the government's contracting officer withheld the rates; $3M is a contractor's estimate | [G14] p. 11: "the contracting officer does not want to make the subcontractor rates available. A contractor estimated annual overcharges of $3 million" | observation *verified*; $3M *assumed* (unchanged) |
| C-AM12 | 1, 2 | KEEP-verified | Exact; ≤43%. The body misreads it (B2) | [GAO88]: "military transportation offices' improper preparation of government bills of lading (GBL) accounted for about $1.3 million of the overcharges" | *verified* (Army rail) |
| C-AM13 | 1-7 | KEEP-assumed | Page loaded directly; quotes verbatim. It counts errors, not dollars, and the direction of the errors is not stated | [AFS]: "Total errors discovered (approximately 4.5% of total audited)" | *assumed*; drop the "fetch-tool" flag |
| C-AM14 | 1, 7 | KEEP-assumed | Shares exact | [AFS]: "Of total errors (5,088) were attributable to inaccurate accessorial charges" | *assumed* |
| C-AM15 | 1-6 | KEEP-assumed | 97% now verbatim. "50%" of BOLs is background, not a survey result. Author's interest stated. One source with the project's earlier SJ use | [SUN]: "range of billing accuracy was 94 to 99 percent depending on the carrier, with the average being 97 percent." [SJS]: "[the principal] made the case for LTL carriers to stop honoring shippers data on the shipments attributes listed on the BOLs." | *assumed*; interest noted |
| C-AM16 | 1-6 | KEEP-assumed | Exact. A broker that also took over the disputes; no base or period; size unknown | [TLIC]: "TLI's program recovered 3.5% of total LTL spend for Tioga Pipe." "the entire carrier dispute process offloaded to TLI" | *assumed* |
| C-AM17 | 1 | KEEP-assumed | Exact | [TLIC]: "most shippers with high LTL activity are losing between 2% and 3% of spend to billing errors" | *assumed* |
| C-AM18 | 1-7 | **NARROW** | Base is estimated total spend incl. air passenger, not audited bills (§1 #3) | [G14] p. 1: "the estimated $16.3 billion in annual transportation bills paid by federal agencies"; p. 8: "over 6,000 rail freight bills not audited by the second tier contractor" | programme ratio *verified*; as an error rate *assumed* |
| C-AM19 | 1-6 | KEEP-verified | Exact; collections only, 1977, regulated rail and truck | [USDA]: "just 0.45 percent, yet this represents over $2 million." | *verified* (1977 co-ops); *assumed* as a stand-in |
| C-AM20 | 1-7 | KEEP-verified | Table and text match the investor-relations copy; ratios ✓; all causes | [FDX]: "These revenue adjustments were $ 83 million in 2026, $ 111 million in 2025, and $ 235 million in 2024." | *verified* (carrier aggregate) |
| C-AM21 | 1-6 | KEEP-verified | Exact. First auditor paid fees plus 3.9% commission; >80% of bills were DoD's | [GAO92] p. 3: "GSA collected $10.2 million in overcharges related to motor carrier payments. About 22 percent of this amount was not identified until the second audit." | *verified* (government 1989-91) |
| C-AM22 | 1-6 | **NARROW** | DoD-wide payments; an opinion (§1 #11) | [D09] p. 6: "DFAS post-payment audit personnel, familiar with DFAS audits of DoD-wide payments, told us" | reported *verified*; for freight *assumed* |
| C-AM23 | 1-7 | **NARROW** | Disagreements include errors already fixed (§1 #7) | [TX21] p. 5: "Agency has collected a refund for overpayment." "Payment was reversed, stopped or voided." | *verified* (Texas AP); not precision |
| C-AM24 | 1-7 | **NARROW** | Auditor's own conclusion; early contract end; not decay (§1 #8) | [TX23]: "the vendor declined to exercise the renewal option and the contract ended on August 31, 2021. According to the vendor, the engagement was not profitable" | *verified* (Texas AP); out of use for decay |
| C-AM25 | 1-6 | KEEP-verified | Exact; no contrary authority found | [STB]: "the law does not preclude carriers from voluntarily paying shipper claims … even if the shipper has not complied with the 180-day requirement." | *verified* (release; full decision not read) |
| C-AM26 | 1, 2, 5 | KEEP-verified | Exact; last amended 2018 | [C378] §378.8: "shall pay, decline to pay, or settle each written claim within 60 days after its receipt by that carrier" | *verified* |
| C-AM27 | 1-4 | KEEP-assumed | Exact; an illustration | [SFN]: "A trucking company with dilution <3%, the advance rate may be 90% or more." | *assumed* |
| C-AM28 | 1-6 | KEEP-verified | Exact. GlobalTranz and TLI also bar offset: 3 of 5 sampled terms | [EASE] §III: "Customer shall not withhold payment as a setoff because of a dispute or claim with EASE or Carriers, including claims for overcharge" | *verified* |
| C-AM29 | 1, 2 | KEEP-verified | Exact; a large shipper's own terms | [AV] §7: "Shipper may offset unpaid freight charges against unpaid freight claims when said claims are outstanding for more than 90 days." | *verified* |
| C-AM30 | 1-7 | KEEP-verified | 80.97% ✓; the OIG frames the $6.3M as uncollectable. Concern §4.1 | [G14] p. 12: "the Division was unable to collect $6.3 million in overcharges during calendar years 2007 – 2009." | *verified* (government); *assumed* as a stand-in |
| C-AM31 | 1, 5, 6 | KEEP-verified | Exact; unchanged since 1996 | [USC10]: "A shipper must contest the original bill or subsequent bill within 180 days of receipt of the bill in order to have the right to contest such charges." | *verified* |
| C-AM32 | 1-6 | **NARROW** | (a)(3)(B) does not name who billed (§1 #6) | [USC10]: "If a shipper seeks to contest the charges originally billed or additional charges subsequently billed, the shipper may request that the Board determine" | text *verified*; broker reach *assumed* |
| C-AM33 | 1, 2, 5, 6 | KEEP-verified | Exact; "broker" absent from Part 378 | [C378] §378.1: "by motor carriers and household goods freight forwarders subject to 49 U.S.C. subtitle IV, part B" | *verified* |
| C-AM34 | 1, 2, 5 | KEEP-verified | Exact | [C378] §378.3(a): "shall not be paid unless filed in writing with the carrier that collected the transportation charges." | *verified* |
| C-AM35 | 1-6 | **NARROW** | Waivable by contract per FMCSA; reform not final (§1 #5) | [NPRM]: "the original regulation did not prohibit a broker from requiring a waiver of the private ''right to review''" | *verified*; "a waivable right" |
| C-AM36 | 1 | KEEP-verified | Exact | [C371] §371.10: "the broker must also abide by the law or regulations which apply to that person." | *verified* |
| C-AM37 | 1, 5 | KEEP-verified | Exact; still a proposal (§371.3 unchanged on 2026-09-01) | [NPRM]: "would require brokers to provide the records required to be maintained under § 371.3(a) within 48 hours when a party to the transaction requests those records." | *verified* (proposal) |
| C-AM38 | 1-6 | KEEP-verified | Exact | [STB]: "the 180-day notification period is a generally applicable notification requirement that is a prerequisite to any sort of relief, at either the Board or in court." | *verified* |
| C-AM39 | 1 | KEEP-verified | Exact | [STB]: "some shippers, under their current auditing practices, are sometimes unable to detect problems until after the 180-day period" | *verified* |
| C-AM40 | 1-6 | KEEP-verified | Exact (p. 10); no later citing decision found; pp. 13-14 support the rule applying alongside 14101 | [SF] p. 10: "compliance with the 180-day time limit is not optional." | *verified* |
| C-AM41 | 1-6 | KEEP-verified | Exact (p. 15). The parties' shared position, not a holding; Chevron note (§4.9) | [NMF] p. 15: "As both parties seem to agree, that section provides the Surface Transportation Board with jurisdiction over a billing dispute regardless of whether the bill involved a regulated rate or a negotiated commercial rate." | *verified* |
| C-AM42 | 1-6 | **NARROW** | A jurisdiction case; never addresses (a)(3)(B) (§1 #4) | [GAI] p. 3: "whether, absent a federal tariff, federal courts have subject matter jurisdiction over a motor carrier's breach of contract claim" | *verified*; restricted use |
| C-AM43 | 1 | KEEP-verified | Exact (parcel) | [UPS] p. 7: "must notify UPS of the request within 180 days of receiving the contested invoice, or any billing dispute is waived." | *verified* |
| C-AM44 | 1 | KEEP-assumed | Snippet exists (cluster 2562022) | [CL]: "180-day dispute period, outlined in 49 U.S.C. § 13710(a)(3)(B), governs this case." | *assumed* (snippet) |
| C-AM45 | 1 | KEEP-assumed | Snippet exists (cluster 2149874) | [CL]: "statutory notice provision set out in 49 U.S.C. § 13710(a)(3)(B) applies to Barber's claims against UPS." | *assumed* (snippet) |
| C-AM46 | 1, 2, 5 | KEEP-verified | Exact. It speaks of "a carrier", relevant to §4.2 | [USC14]: "A carrier providing transportation or service subject to jurisdiction under chapter 135 may enter into a contract with a shipper" | *verified* |
| C-AM47 | 1-6 | KEEP-verified | Exact §V; no longer broker window found in a counter-search | [EASE] §V: "Such notice must be provided within five (5) days from the date of the invoice." | *verified* |
| C-AM48 | 1-6 | KEEP-verified | Exact; also "net/15 … without offset or deduction" | [GTZ]: "made within 30 days from the date of the invoice. In the event GlobalTranz does not receive timely written notice of the dispute, the charges will be conclusively presumed to be valid." | *verified* |
| C-AM49 | 1-3 | KEEP-verified | Word for word the same as GlobalTranz | [AML]: "Any dispute by Customer of any invoice issued by AMLTL shall be made in writing … within 30 days from the date of the invoice." | *verified* |
| C-AM50 | 1-6 | KEEP-verified | Exact; payment by card at booking; the window runs from an adjustment | [FQ]: "The Customer is permitted thirty (30) days from the date of the adjustment to dispute the charge(s)." | *verified* |
| C-AM51 | 1-3 | KEEP-verified | Exact; the same firm as C-AM16 | [TLIT]: "Customer is permitted thirty (30) business days from the date of the invoice to dispute any invoiced charges." | *verified* |
| C-AM52 | 1-6 | KEEP-verified | Exact §9; an old template (cites 49 C.F.R. 1008) | [AV] §9: "may be filed at any time within 18 months of delivery, and pursuant to 49 U.S.C. 14101(b), the parties hereby expressly waive" | *verified* |
| C-AM53 | 1 | KEEP-verified | 0 hits for "overcharge" or "dispute" | [LS]: (absence; text search) | *verified* (absence) |
| C-AM54 | 1-6 | KEEP-assumed | Exact; says the same of the 18-month rule | [BEN] p. 1: "This rule is found at 49 USC § 13710. The principle also appears in many transportation agreements." | *assumed* |
| C-AM55 | 1, 2, 7 | KEEP-verified | All 15 cells reproduce (§3) | (calculation; inputs C-AM31, 47-52) | **[our calc]** ✓ |
| C-AM56 | 1-7 | **NARROW** | A 4-year claim, the carrier's account (§1 #9) | [CFA] ¶36: "the Agreement provides that all claims by Amazon must be filed within 18 months of the original invoice." | *assumed*; restricted use |
| C-AM57 | 1, 5 | KEEP-verified | Exact; GSA adds it "has no plans to exercise its powers under Section 3726" | [GSAD]: "a delegation of authority from the Administrator of General Services to all Federal agencies to exercise all authorities conferred by Section 3726" | *verified* |
| C-AM59 | 1-3, 7 | KEEP-verified | Exact; collected before carrier refunds (B4) | [GAO89]: "collected $100.8 million in transportation overcharges and disbursed $34 million for carrier refunds and contract audit services" | *verified* |
| C-AM60 | 1 | KEEP-verified | Exact; GSA's own target | [OMB]: "GSA expects to recover $12 million in transportation overcharges in both of these years." | *verified* |
| C-AM61 | 1, 7 | KEEP-verified | $11.03M ✓; caveats as C-AM18 | [G14] p. 4: "For bills paid during 2007 to 2009 the Division issued overcharges of $33.1 million" | *verified* |
| C-AM62 | 1-6 | KEEP-verified | The law is exact; the body's link to the fall is narrowed (B4) | [G13] p. 1: "Public Law 105-264 (passed on October 19, 1998) requires that federal agencies conduct prepayment audits of all transportation billings." | *verified*; link *assumed* |
| C-AM63 | 1, 7 | KEEP-verified | Exact; +260.6% | [D09] p. 5: "In FY 2007, GSA identified another $33.9 million—a 260 percent increase" | *verified* (reported) |
| C-AM64 | 1 | KEEP-assumed | Exact; PRG's own statement | [GAO99] p. 6: "According to PRGI, its overpayment identification rate under the demonstration program is 0.48 percent of purchases reviewed" | *assumed* (unchanged) |
| C-AM65 | 1 (one source) | KEEP-assumed | Loop: a fall in the share of invoices with errors under a pre-payment tool, not first-year against later recoveries. Inbound Logistics pages 403 | [LOOP]: "Great Dane could see that 7.8% of invoices had errors … Now, only 3.6% of invoices have errors" | *assumed* |
| C-AM66 | 1 | KEEP-verified | The IG's paraphrase; DoD only "partially agreed" | [D09] p. 9: "he agreed to develop a comprehensive plan to target the upfront validation services and charges before payment to the carrier." | *verified* |
| C-AM67 | 1 | KEEP-verified | Exact | [NV] p. 3: "Cardinal estimated that it cost approximately $1.2 million to perform FPA services "in-house"" | *verified* |
| C-AM68 | 1 | KEEP-verified | Exact | [D01]: "DoD annually processed approximately 1.25 million transportation freight payments totaling approximately $1 billion." | *verified* |
| C-AM69 | — | not checked | EDGAR barred | — | unchanged |
| C-AM70 | 1 | KEEP-verified | Exact (p. 4); see §4.8 | [G13] p. 4: "transportation costs incurred in fiscal year 2008 totaled between $40 billion and $50 billion, compared to the $25 billion reported by OMB." | *verified* (cited) |
| C-AM71 | — | not checked | TRID not re-run | — | unchanged |
| C-AM72 | 6 | KEEP-verified | Two web searches here also found no decision citing *Southern Furniture* and none applying 13710 to a broker | (search results) | *verified* (search); absence is not proof |
| C-AM73 | 1 | KEEP-verified | Art. 14 and Part 378 confirmed | [YFB] Art. 14: "shall be commenced not more than 180 days after the original bill date" | *verified* |
| C-AM74 | 1, 5 | KEEP-verified | The original URL now serves Werner's home page; read on Wayback (2025-11-07) | [WER] Item 585: "Any claim for overcharges of freight bills must be submitted within 180 days of shipment date" | *verified* (archive) |
| C-AM75 | 1 (1 of 9) | KEEP-verified | FedEx Freight tariff confirms 180 days | [FXT] Item 438: "shall be commenced not more than 180 days from the receipt of the original invoice plus 7 days" | *verified* |
| C-AM76 | 1-6 | KEEP-verified | Exact §VIII; legal effect doubtful (§4.2) | [EASE] §VIII: "To the extent that the provisions herein are inconsistent with Part (b) … the Parties expressly waive all rights and remedies they may have under the Act." | *verified* (text) |

---

## §6 Counter-evidence and leads

These are logged, not new findings. Each is tied to the claim it bears on.

| # | Source | What it says (quote ≤40 words) | Ties to | Type |
|---|---|---|---|---|
| 1 | GSA FY2025 budget narrative, P-2 to P-3 [CJ25] | The programme "made a voluntary payment of $29.6 million to a U.S. Department of Defense (DoD) vendor. The payment reflected … acknowledgement of a contracting officer's prior decisions that Notices of Overcharge (NOCs) issued to the vendor were erroneous." Up to "$11.8 million" more may be owed. FY2023 receipts were $12,354k. | C-AM08, 18, 30, 61 (GSA "identified" and "issued" figures include erroneous notices); A09-02 precision | Counter-evidence |
| 2 | GSA FY2024 and FY2023 budget narratives (Wayback: https://web.archive.org/web/20240715041817id_/https://origin-www.gsa.gov/system/files/16_FY2024_CJ_Permanent_Authorities_Narrative_Final.pdf ; https://web.archive.org/web/20240624002652id_/https://origin-www.gsa.gov/system/files/15_FY_2023_CJ_Permanent_Authorities_Narrative_Final_508cO.pdf) | Receipts FY2021 "$ 12,743" and FY2022 "$ 28,846" (thousands); "In FY 2022, there is a planned surge in collections tied to outstanding receivables set to expire" | A09-13 programme series (newer than 2007-09) | Lead (currency) |
| 3 | GAO NSIAD-92-61 (Dec. 1991), pp. 2-3, https://www.gao.gov/assets/nsiad-92-61.pdf (scanned; read as page images) | "GAO found subsequent GSA-identified overcharges on about 16 percent of the bills, involving more than $75,000" (135 DoD-pre-audited bills, FY1989, Fort Irwin). Pre-audit "helped indirectly, in DOD's opinion, to deter another $34 million in overcharges" | A09-02 (pre-audit misses); A09-13 (deterrence, DoD's opinion) | Lead. Same site as C-AM12 |
| 4 | FMCSA NPRM 2024 [NPRM] | "the Agency believes that in most brokered transactions, the broker is not the shipper, and 49 U.S.C. 14101(b) does not apply." | C-AM35, C-AM76 | Counter-evidence (partial) |
| 5 | *Southern Furniture*, pp. 13-14 [SF] | "§ 14101 says nothing that contradicts, or even calls into question, § 13710(a)(3)(B)'s time limit for a shipper to provide notice that it intends to contest a bill." | C-AM42, A09-10b | Counter-evidence |
| 6 | EFL broker terms, https://efl.global/transportation-broker-terms-conditions ; Traffic Tech client terms, https://traffictech.com/client-terms-conditions-partner-with-traffic-tech/ | "within fifteen (15) days of receipt of the invoice"; "Customer is permitted ten (10) calendar days from the date of the invoice to dispute any invoiced charges." | C-AM47-51 (no longer windows found) | Corroboration (template families, §2) |
| 7 | GlobalTranz [GTZ]; TLI terms [TLIT] | "without offset or deduction"; "without deduction, offset or setoff" | C-AM28 | Corroboration |
| 8 | *NMFTA v. GSA*, pp. 5-6 [NMF] | e.g., "ABF Freight received 1,483 notices, totaling more than $401,000 in overcharges"; "YRC received 2,310 notices, totaling about $600,000" | A09-01: typical size of a federal post-payment overcharge notice to LTL carriers (≈$260-270 each, no spend base) | Lead |
| 9 | GAO T-NSIAD-99-213, p. 6 [GAO99] | "Collections by DOD as of June 1999 amounted to $2.6 million" against $29.3M identified, after vendors disputed and recovery "virtually stop[ped] for 8 months" | A09-03 (AP, not freight: 8.9% collected at that date) | Lead |
| 10 | FedEx Freight 100-Y Item 438 [FXT]; YRC-First Brands Art. 14 [YFB] | "Any action or proceeding by Customer to recover overcharges … shall be commenced not more than 180 days" | A09-10a: some tariffs and contracts require an action to be *started*, stricter than a notice | Lead (detail) |
| 11 | DoD IG D-2009-072, pp. 5-6 [D09] | GSA "performed this function after a delay of six months from date of payment"; GSA's "goal [is] to complete PowerTrack payment audits within 60 days" | C-AM08 (period mismatch is about 6 months) | Context |
| 12 | Trade press via search (FreightWaves, Carrier Atlas) | Supplemental broker-transparency proposal sent to OIRA on 2026-08-27; not final | C-AM37, B5 | Lead (*assumed*) |
| 13 | The consultancy's own site [SJS] | "rapid deployment of dimensional machines have increased revenue and profits for carriers and reduced auditing of bills." | C-AM15 (interest) | Counter-evidence (interest) |

---

## §7 Could not access

- **SEC EDGAR** (by rule). FedEx Freight's 10-K was read on its investor-relations site instead. C-AM69 (Elizabeth Arden) was not checked.
- **gao.gov PDFs** return 403 to curl. They were read through the fetch tool's saved copy: GAO 1992 and 1999 have a text layer; NSIAD-92-61 is scanned and was read as page images, because OCR language data was not installed.
- **Inbound Logistics** articles (403): the vendor sources behind C-AM65 other than Loop.
- **A trade-press legal column on the 180-day rule** (ccjdigital.com, 403). **A case summary** on cabadvantage.com redirected to a landing page.
- **The uShip help page** on paid LTL invoice disputes (403).
- **Tioga Pipe's own site**: script-rendered, with no size information.
- **Werner tariff**: the original URL now serves the company home page; the Wayback copy of 2025-11-07 was used.
- **media.defense.gov** (403): DoD IG reports were read on Wayback copies.
- **Not re-run:** TRID searches (C-AM71). **Not read:** the full STB decisions behind the 1997 release (C-AM25, 38, 39).
