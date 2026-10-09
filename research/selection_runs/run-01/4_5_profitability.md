# Run 01, S4.5: profitability check

> **Stage S4.5 of `submarket_selection.md` §4 (added 2026-09-22 as C25).** Before any customer interview, audit every public source on the inputs that decide a card's per-customer model. Give one of three verdicts: **proven profitable**, **proven unprofitable**, or **not provable from the web**.
> **Run 01 applies it to C-19 first.** C-09 is not run for now (founders' words in §1).
> **Labels:** *verified* = read at the source; *assumed* = vendor, association second-hand, snippet or secondary; **[our calc]** = arithmetic; **[our call]** = judgement.
> **Nothing here moves a frozen line.** C-19's kill condition (`4_kill_conditions.md` §4.7, frozen 2026-09-22) stands whatever this file finds; a case for moving it goes through `submarket_selection.md` §9.
> **Status:** C-19 done 2026-09-22: **not provable from the web** (§3.6). It is narrowed to a business built on the upper tail of suppliers, with four open inputs for S5. Both proposals were adopted the same day as C26 (screen recruits first) and C27 (the pass line is re-derived to 0.22% at a $50M supplier) (§4), and the incumbents are mapped in §3.7.

## 1. The decision that created this stage

**The founders' words, 2026-09-22 (verbatim):**

> "4. Yes
>
> I want to add an S4.5 Profitability check, which is a test if any of our sub-markets can be proven profitable before we do customer reviews. This relies on auditing web information relevant to what we've checked out.
>
> This will be a similar process to what we've just done for C-09. Though we want to find any and all web information we can to see if we can iron this out without customer interviews.
>
> Conduct this on C-19, since it seems like the estimates necessary for C-09 are unlikely."

**Recorded as:**
- "4. Yes" adopts P-27 as **C23** (the ceiling test) and P-28 as **C24** (labour savings under the fee rule).
- The new stage is **C25**, written into `submarket_selection.md` §1, §4 S4.5, §9 and §10, and into `0_criteria.md` §5.
- The verdict bar below is the process default, **[our call]**. The founders can change it before an audit starts.

## 2. The bar (fixed before the audit)

| Verdict | Test |
|---|---|
| **Proven profitable (from the web)** | Using only *verified* or neutral inputs: a customer in the card's segment gives positive gross profit, **and** repays a $5-15k acquisition cost within 12 months (check A §A3), **and** enough such customers exist for $1M at a 10% share and $2.5M at no more than 35% |
| **Proven unprofitable** | Fails even at the most favourable end that neutral or *verified* evidence supports (C23, the ceiling test, on the audited ranges) |
| **Not provable from the web** | Anything else. Each open input is named, with the document that would settle it |

> **Note, 2026-10-08 (D-23):** C-09's kill-test re-run (`handoff_c09_software_rerun.md`) uses this bar's **12-month payback** test, but it **is not C-09's S4.5**. The founders chose "Targeted checks + adversarial", not the full profitability check. C-09 still has no S4.5 verdict.

## 3. C-19 · Retailer on-time-in-full fines and deductions

> **Flag, 2026-10-08 (D-23):** the founders decided the company employs no analysts and does no manual review, and that this applies to C-19 too ("Yes, flag C-19 for later"; `software-initial-pitch.md` §1A). The model re-run below costs **our staff's** triage and dispute minutes at a US collector's wage (and an offshore case). It needs the same software-basis re-run as C-09 before the two cards are compared at S6. Until then this section stands as the record of the service-basis audit; its "not provable from the web" verdict is unchanged.

### 3.1 The deciding inputs (step 1)

From the step-7 model (`4_kill_conditions.md` §4.2-§4.3), two inputs cross the bar within their plausible ranges:

1. **The recoverable rate:** invalid non-trade deductions actually paid back, as a share of the supplier's big-box sales. Neutral central 0.03% (CRF medians); vendors imply 0.2-0.4%.
2. **The cost per deduction:** the average deduction's size, which sets how many items must be looked at per dollar of fee, and the minutes each takes.

Two more matter only at the edges: **the number of suppliers at each size** (for the market test) and **access to the retailer portals** (without it there is no product).

### 3.2 What the web would have to show [our calc]

The recoverable rate needed at each supplier size, at the model's central cost inputs (non-trade deductions 0.5% of sales, $500 each, 5 minutes triage, 20 minutes per dispute, $600 fixed, 25% fee):

| Big-box sales of the supplier | Break-even, US collector | 12-month payback on a $5k acquisition cost | on $10k | on $15k | Same three, offshore review |
|---|---|---|---|---|---|
| $10M | 0.041% | 0.28% | 0.51% | 0.75% | 0.24% / 0.45% / 0.66% |
| $20M | 0.027% | 0.14% | 0.26% | 0.38% | 0.12% / 0.23% / 0.33% |
| $50M | 0.019% | 0.066% | **0.11%** | 0.16% | 0.05% / 0.09% / 0.14% |
| $100M | 0.016% | 0.040% | 0.063% | 0.087% | 0.03% / 0.05% / 0.07% |
| $200M | 0.015% | 0.026% | 0.038% | 0.050% | 0.02% / 0.03% / 0.04% |

**Reading:** "proven profitable" needs neutral or *verified* evidence that suppliers of a given size recover at least the rate in their row, **and** that enough suppliers of that size exist. The neutral central (0.03%) clears the bar only for suppliers near the $500M cap. The vendors' 0.2% clears it from about $20M up.

### 3.3 The audit (step 2)

Three checks ran on 2026-09-22, one per evidence tier, adding 185 new sources (N-AG01 to N-AG62, N-AH01 to N-AH52, N-AI01 to N-AI71). Load-bearing figures were re-read at the source in this chat (§5).

**(a) Real transaction documents: check AG** (`research/s4_5_check_AG_c19_ledgers.md`)

| Finding | Figure | Label |
|---|---|---|
| **The one in-segment ledger that splits chargebacks from trade lines** | M Design Village, a ~$19-24M nursery-furniture importer selling to Walmart, Target, Amazon and Wayfair: "7516 - Chargebacks" $13,688.77 and "7534 - Amazon - Chargebacks" $14,382.18 on "5100 - Sales - Merchandise" of $2,337,843.99, 18 Nov-31 Dec 2024. **Non-trade chargebacks = 1.20% of sales**. It is one company, in its holiday peak, in Chapter 11 | *verified* (Bankr. D.N.J. 24-21406, Doc 101; re-read at source); rate **[our calc]** |
| The older ledger | *ANConnect*: 0.20% (2011-15; known, N-AE14) | *verified* |
| **The retailer side of the same money** (found after the verdict; it does not change it) | ShopKo, a $2.0-2.3B discount chain, listed in its 2019 bankruptcy the fines it collected from all its vendors: early/late, fill rate, ASN and other vendor chargebacks of $5.73M, $6.55M and $6.56M in FY2016-18. That is **0.24-0.32% of its sales**, about **0.33-0.46% of what it paid vendors** (assuming cost is 70-75% of sales). Early/late fines were 55-62% of the total; fill-rate fines rose from 9% to 24% | *verified* (Bankr. D. Neb. 19-80075, Doc 10, SOFA; re-read at source); rates **[our calc]** |
| Everything else public | **All-type "dilution"** of 3.7-20% of sales (E. Gluck 20% in a January; Instant Brands; M Design 5.2%), dominated by returns, promotions and damages. **Unusable for C-19**, because it mixes trade with non-trade | *verified* |
| A real dispute record | E. Gluck's turnaround advisers spent **23 hours on one Amazon dispute round** (14 h building the list, 6 h filing, 3 h follow-up). The count and value disputed are not stated | *verified* (fee statements) |
| Not found anywhere public | Deduction counts, average size, invalid share, disputed or recovered share, and dilution by retailer | — |

**(b) Neutral studies: check AH** (`research/s4_5_check_AH_c19_neutral.md`)

| Finding | Figure | Label |
|---|---|---|
| **The primary CRF/Attain 2021 survey, split by size** (earlier checks had it only through a vendor's slides) | Suppliers with $500M of revenue or less (40 respondents): non-trade deductions median **¼-½% of sales** (46% under 0.25%; 14% at 3-10%). Invalid share of **all** deduction dollars median **1.1-5%**, split in two (54% at 5% or less, 43% at 15% or more). Recovered share median **70%**. 48% track no deduction metrics; auto write-off $10-25 | *verified* (full PDF; the ≤$500M columns of Q33, Q34 and Q37 re-read at source); self-reported; Attain sells consulting |
| The survey chain for a small supplier | **Median ~0.008-0.011% of sales recovered; mean ~0.10%.** On a simulation of the answer distributions (answers treated as independent **[our call]**), **~64% of small suppliers fall under the kill line (0.05% found), ~18% in the conditional band, ~18% at or above the pass line (0.17%)** | **[our calc]** |
| CRF 2023 (all sizes, no size split) | Non-trade median **1.1-2% of sales**, up from ¼-½% (2018) and ½-1% (2021) | *verified* (slides) |
| CRF benchmark sample (c. 2012, n = 287) | **$18.80** median cost per deduction (not the vendor-quoted $97); ~2,167 deductions a year per staff member = **~52 minutes each** by hand; ~11 deductions per $1M of sales (all types) | *verified*; minutes **[our calc]** |
| A 3PL's dispute cases (2026 preprint, not peer reviewed) | 16.5% of one account's compliance chargeback dollars reversed on dispute | *verified* as the preprint's text |
| Supplier OTIF performance | Point observations only (Walmart's top 75 suppliers "as low as 10 percent" in 2017; "only 60%" of suppliers meeting OTIF, per a Walmart-sponsored MIT capstone, 2020). **No distribution exists** | *verified* |

**(c) The market's own economics: check AI** (`research/s4_5_check_AI_c19_market.md`)

| Finding | Figure | Label |
|---|---|---|
| **The vendor aggregate, split by its own author** | STAT's "$1B+" lifetime recoveries: **$600M "Profit leakage (non-deduction)"**, $275M "Post-audit Errors caught", **$150M "Standard deductions Disputed and won"**, $100M "Compliance Loss prevented", on "$500B" of "Transactions analyzed". **Deductions won = 0.03% of transactions**; 0.085% with post-audit claims | *assumed* (vendor claim; homepage re-read at source 2026-09-22); rates **[our calc]** |
| What suppliers pay the leader | SupplyPike at acquisition: ~$18.4-19.2M a year from ~500-550 suppliers = **~$33-38k per customer**. Its 2023 list price was **$150-4,850 a month per retailer**, about **0.12-0.24% of that retailer's sales** for $6-49M accounts | revenue *verified* (SPS 8-K); counts and list prices *assumed* (call, archived pages); rates **[our calc]** |
| Whether the leader makes money | SupplyPike's plan: −$1.5M Adjusted EBITDA on $8.0M (Aug-Dec 2024), breakeven on $25.0M (2025). SPS (Q2 2026): 1P recovery "nearing" its overall margin (~30.8%). SPS sold its small Amazon-seller book (~$2,900 per customer) at about 0.45× revenue, booking a $23.5M loss | plans *verified*; margin quote *assumed* (transcript) |
| Pay for the work | Median posted in-house deductions analyst: **$30.67/h** ($43.82 loaded), 1.3× the BLS collector mean. SPS's own Revenue Recovery Specialist: $29.47-34.62/h ($42-49 loaded) | *verified* (postings) |
| Portal access | Amazon: portal passwords may not be requested, but "secondary user permissions" may be granted. A new vendor-only Invoices API (v2026-06-25) returns shortage and price variances with root causes, but **has no dispute endpoint**. Walmart: **no deductions API**. Target (2012 rules): contractors and agents may be given access | *verified* |
| EDI remittance files | 812 and 820 confirmed only at Kroger; 820 at Home Depot | *assumed* |

### 3.4 Desk look-back on real data (step 3)

**No transaction-level deduction data is public.** Across roughly 180 new sources, not one real remittance advice, EDI 812/820 file, portal export or deduction ledger with reason codes turned up for a supplier to a big-box retailer. The nearest things found:
- M Design Village's monthly P&L lines (extracted to a CSV in the session scratchpad; §3.3a);
- E. Gluck's adviser time entries on Amazon chargebacks (28 rows; 23 hours for one dispute round).

Neither gives an invalid share. **The look-back S4.5 asks for cannot be run on C-19 from public data.** That is itself a finding: unlike C-09, whose invoices surface in court records, deduction detail stays inside retailer portals.

### 3.5 The model re-run (step 4) [our calc]

**Method.** The S4 step 7 cost model (`4_kill_conditions.md` §4.2) is kept, with two inputs replaced by audited ones:
- **The recoverable rate is drawn per supplier** from the CRF 2021 answer distributions for suppliers at $500M or less (non-trade share × invalid share × recovered share). The three answers are treated as independent **[our call]**.
- **Supplier size** follows check AE's spread of Walmart's 31,196 supplier records (big-box sales = 2 × Walmart sales).

Wages are run at the BLS collector rate ($33.70 loaded) and at the posted-pay rate ($45). The fee base is either every recovered dollar (the vendors' practice) or half of them, the half the supplier would not have recovered alone. "Qualifying" means the customer's yearly gross profit repays a $10k acquisition cost within 12 months.

| Case | Suppliers qualifying | Their median fee a year | Their median gross profit | Share of suppliers with $20M+ of big-box sales that qualify | $1M needs (share of qualifying) | $2.5M needs |
|---|---|---|---|---|---|---|
| **All recoveries count, BLS wage** | **810-1,290** | $35,000 | $24,900 | **15%** | 2-4% | 6-9% |
| All recoveries count, posted wage | 740-1,160 | $38,600 | $25,000 | 14% | 2-4% | 6-9% |
| **Half are incremental, BLS wage** | **360-530** | $40,900 | $21,800 | **8%** | 5-7% | 12-18% |
| Half are incremental, posted wage | 260-410 | $52,000 | $22,200 | 6% | 5-7% | 12-18% |

(Ranges are the two spreads, σ 2.0 and 2.5, of the supplier-size curve.)

**Payback on winning one qualifying customer:**

| How the profitable supplier is found | Payback, all recoveries count | Payback, half incremental |
|---|---|---|
| Signed directly, $10k acquisition cost | **~5 months** | ~5-6 months |
| Every prospect screened costs the full $10k (only 6-15% qualify) | **31-34 months** | 69-90 months |
| A $2k screen per prospect, then $10k to close | **11-12 months** | 19-23 months |

**What the re-run says:**
1. **The typical small supplier is not a profitable customer.** At the neutral median it recovers about 0.01% of big-box sales, and the fee does not cover US labour. **C-19 can only be a business built on the upper tail.**
2. **The tail exists on neutral inputs.** It is about 800-1,300 suppliers if every recovery counts, and about 260-530 if only half are new money. Each pays a median $35-52k a year, which matches SupplyPike's real revenue per customer ($33-38k). Once found, a tail customer repays its acquisition cost in about five months, and $2.5M needs only 6-18% of the tail.
3. **Finding the tail is the problem.** Only 6-15% of suppliers with $20M+ of big-box sales are in it. Unless a cheap screen identifies them, the effective cost of winning one runs to 31-90 months of payback, which fails check A's 12-month norm.
4. **The tail may already be taken.** SupplyPike alone had ~500-550 paying suppliers at acquisition (skewed large), and Glimpse reports 200+ brands. That is roughly the size of the whole qualifying tail in the model. **This is the show-stopper question (H19-04): are those customers satisfied?**
5. **The "vendor world" was a misreading.** The 0.2% vendor rate used in step 7 (`4_kill_conditions.md` §4.2, and the reasoning for the 0.17% pass line) was STAT's all-in figure. STAT's own split puts deductions won at **0.03%**, the neutral central. The frozen line is not moved; this is recorded for the founders (§4).

### 3.6 Verdict (step 5)

**C-19: not provable from the web.** It is neither proven profitable nor proven unprofitable, but it is now much narrower than it was.

- **Why not "proven profitable":**
  - On neutral inputs the typical supplier in the segment is unprofitable.
  - The profitable tail rests on three things no neutral source measures:
    - that the survey answers are independent;
    - that the fee can be charged on recoveries the supplier would have made anyway;
    - that the tail can be found for about $2k a prospect or less.
- **Why not "proven unprofitable":** at the favourable end that neutral and *verified* evidence supports, the tail pays well. The CRF upper quartiles recover about 0.23% of sales, and a real in-segment ledger shows non-trade chargebacks of 1.2% of sales.
- **What is open, and what would settle each point:**

| Open input | What settles it | Already in S5's kill condition? |
|---|---|---|
| **The non-trade invalid share** in a tail supplier's own deductions | the deduction look-back (`5_interview_kit.md` §6.3) | **Yes**, Test 1 |
| **How many prospects are in the tail** (screen yield) | a screening question to every recruit: non-trade deductions as a share of sales, and big-box sales | **No**, proposed as P-29 (§4) |
| **The incremental share**: what the supplier already recovers on its own | the supplier's own dispute and recovery records for the look-back period | **No**, proposed as P-29 |
| **Whether the tail is already served**, and satisfied | the interview question on SPS and Glimpse use (H19-04) | Yes, as the show-stopper test |
| Portal access per retailer | the access test | **Yes**, Test 2 |

**Reading for the founders [our call]:** the audit makes C-19 less attractive than step 7 did. The average supplier doesn't pay, the "vendor world" rate turned out to be the neutral one, and the leading incumbent already serves a customer base about the size of the profitable tail. What survives is a specific, testable business: **find the suppliers whose non-trade deductions run at 1% of sales or more, with a high invalid share, that SPS and Glimpse don't already serve or serve badly.**

### 3.7 The incumbents: SupplyPike (SPS Commerce) and Glimpse, and where they may be vulnerable

*Added 2026-09-22 at the founders' request:* "Mention SupplyPike & Glimpse in C-19, perhaps we could find discomfort with those applications and shake up the market."

**Who they are:**

| | SupplyPike (SPS Commerce Revenue Recovery) | Glimpse |
|---|---|---|
| What it is | Deduction software, Walmart-first, founded Dec 2017 in Fayetteville, AR. Bought by SPS Commerce, the largest retail EDI network, in Aug 2024 for ~$206M | AI deduction recovery with human analysts, aimed at consumer brands. Y Combinator graduate |
| Scale | ~500-550 paying suppliers at acquisition, skewed larger; ~$18.4-19.2M a year; SPS expected $25.0M for 2025 (a forecast) | "200+ brands"; ~110 staff; $52M raised, including a $35M Series A led by Andreessen Horowitz (Mar 2026) |
| Price | Per retailer, per month, by that retailer's sales: $150-4,850 in 2023 (about 0.12-0.24% of that retailer's sales for $6-49M accounts), about **2-2.5× the 2021 list**. By 2026, "pricing available upon request" | Subscription; one small brand pays $3,000-4,000 a month |
| Economics | Planned −$1.5M EBITDA on $8.0M (Aug-Dec 2024), breakeven in 2025. SPS says 1P recovery is "nearing" company margins | ~1.4-1.8 clients per employee; analysts paid $85-130k: a service-heavy model |
| Public ratings | Capterra 4.9 of 5 from 45 reviews | Not read (G2 blocked the fetch; the search budget was used up) |

Sources: check AI (N-AI05, N-AI12 to N-AI16, N-AI20, N-AI21, N-AI23 to N-AI27, N-AI45); check U (N-U01, N-U34); Capterra re-read 2026-09-22. Prices and ratings are *assumed* (vendor pages and review sites); SPS's revenue lines are *verified*.

**Where discomfort may be (evidence, then hypothesis):**

| Possible weak spot | What the record shows | Label |
|---|---|---|
| **Price, and price rises** | SupplyPike's per-retailer list price roughly doubled to 2.5× from 2021 to 2023, then went "upon request". A C-19 central supplier would have faced **~$47k (Walmart only) to ~$85k (three retailers) a year** at the 2023 list, **9-17× a 25% contingency fee** on the central chain. One reviewer: "periods when it can be difficult to justify the monthly cost" | prices *assumed* (archived vendor pages); multiple **[our calc]**; review *assumed* |
| **Paying when disputes are denied** | A subscription is paid whether or not disputes win. The complaints on Capterra: "Lacks escalation options for denied disputes"; "no guidance on pursuing claims outside platform"; "unclear denial explanations"; "not all deductions are recoverable" | *assumed* (reviews, Jul-Aug 2026) |
| **Coverage and evidence gaps** | "does not incorporate all retail partners"; "sometimes it might not capture backup documents"; "Lacks real-time visibility into claim status"; "onboarding took longer than expected" | *assumed* (reviews) |
| **Small suppliers priced out** | SupplyPike's customers "skew a little bit larger" (SPS). SPS sold its small-ticket Amazon book (~$2,900 per customer) at a $23.5M loss. Glimpse's human-analyst model is costly per client | revenue *verified*; quotes *assumed* (transcripts) |
| **Ownership change** | SupplyPike is now a module of SPS's EDI platform, which SPS says it wants to "cross-sell" | *assumed* (transcripts) |
| **Against all of this** | Capterra's 4.9 from 45 reviews is strong. Most reviews shown are dated Jul-Aug 2026, a cluster that may reflect a review drive **[our call]**, but the praise is concrete ("recover over a million dollars in the past year and a half, so it is well worth the price") | *assumed* |

**What "shaking up the market" could mean here [our call, hypotheses for S5, not decisions]:**
1. **Pay only when money comes back.** A contingency fee (C-19's 25%) against a per-retailer subscription that is due even when disputes are denied. For a supplier in the upper tail, 25% of recoveries may be comparable to SupplyPike's list price. For everyone else it costs nothing unless something is recovered.
2. **Serve the tail the leader skews away from.** High-leak suppliers under ~$50M of big-box sales, where SupplyPike's list price is a large share of sales and Glimpse's analyst model is costly.
3. **Win on the evidence chain, not just the portal.** Pull proof of delivery and carrier timestamps into each dispute. That is the gap reviewers name ("backup documents", denials, escalation), and it links to C-09's freight documents.

**How S5 tests it** (added to the kit, §5.5, and the hypotheses, `5_validation.md` H19-11): ask users of SupplyPike, SPS, Glimpse or others:
- what they pay;
- what came back in the last 12 months;
- the last time a dispute was denied, and what they did next;
- whether they have considered cancelling or switching, and why.

These are past-behaviour questions, not opinions (the kit's rules, §1.2). The W4 show-stopper question stands: satisfied users of one vendor serving more than half the target customers would stop the card.

## 4. Proposals from this audit (both adopted 2026-09-22)

| # | Proposal | Why |
|---|---|---|
| **P-29 → adopted as C26** (founders: "Yes screen recruits first.") | **C-19's S5 look-back is run on a tail supplier, and two more numbers are recorded.** Screen every C-19 recruit for non-trade deductions as a share of sales and for big-box sales, and run the look-back on one reporting 1% or more. Also record: (a) the screen yield, the share of recruits reporting 1% or more; (b) the incremental share, the invalid dollars the supplier would not have recovered on its own. The frozen lines in `4_kill_conditions.md` §4.7 stay as they are | On the neutral distribution, a look-back on a random small supplier would kill C-19 about 64% of the time even if the tail business is real, because the test would be measuring the median supplier, not the business. The two added numbers are the ones the re-run shows decide profitability. This changes who is measured, not the line, but it touches a frozen condition, so it goes through `submarket_selection.md` §9 if adopted |
| **P-30 → adopted as C27** (founders: "Update according to P30 as well.") | **Re-derive the pass line.** Adopted as a change, not a note: the pass line becomes **0.22% at a $50M supplier**, with a table by size (`4_kill_conditions.md` §4.7). Original note: the 0.17% pass line in `4_kill_conditions.md` §4.7 was reasoned partly on STAT's 0.2%, which proves to be mostly non-deduction money | A frozen line moves only through §9. The founders may want to know that the pass line sits about 5.7 times above the only vendor figure for deductions actually won |

## 5. Sources

- **Checks written for this stage (2026-09-22):**
  - `research/s4_5_check_AG_c19_ledgers.md` (N-AG01 to N-AG62): bankruptcy and court records, lender terms, the M Design Village and E. Gluck extracts;
  - `research/s4_5_check_AH_c19_neutral.md` (N-AH01 to N-AH52): CRF 2021 and 2023 surveys, the CRF benchmark sample, university and regulator sources;
  - `research/s4_5_check_AI_c19_market.md` (N-AI01 to N-AI71): SPS filings and calls, SupplyPike's archived prices, STAT, vendor cases, job postings, portal terms and APIs.
- **Re-read at the source in this chat:**
  - CRF/Attain 2021 survey (the ≤$500M columns of Q33, Q34 and Q37, and the size-split medians): https://www.crfonline.org/wp-content/uploads/2021/07/2021-Deduction-Benchmarks_final.pdf
  - M Design Village, Bankr. D.N.J. 24-21406, Doc 101 (lines 5100, 7516, 7517, 7524, 7534): https://storage.courtlistener.com/recap/gov.uscourts.njb.1119534/gov.uscourts.njb.1119534.101.0.pdf
  - STAT's homepage split: https://www.statrecovery.com/
- **Arithmetic:** the step-7 cost model (`4_kill_conditions.md` §4.2) plus a simulation over the CRF 2021 answer distributions and check AE's supplier-size curve. The scripts are in the session scratchpad, not in the project.
