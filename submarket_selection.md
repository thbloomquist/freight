# Sub-market selection: the process

> **Answers Q1:** how do we choose a freight sub-market, and later a segment inside it, for a vertical SaaS whose fee comes out of the money it saves customers?
> **Version 1.5, 2026-09-16.** The process is defined, and run 01 has started. **S0 is frozen (2026-09-14).** §4 S0.1-S0.4 hold the founders' initial decisions, the research on them, and the final decisions; the frozen sheet is `research/selection_runs/run-01/0_criteria.md`. Process changes C1-C21 are logged at the end of §9. **S1 is done (2026-09-14):** 40 candidate cards in `research/selection_runs/run-01/1_candidates.md`. Its proposed process changes (P-1 to P-4) are not applied yet. **S2 is done (2026-09-15):** 6 cards dropped and 34 carried forward in `research/selection_runs/run-01/2_knockouts.md`. The 8-15 gate was missed. The founders chose option C (2026-09-15), so S3 runs as S3a, which settles the unknowns, then S3b, full fact sheets for the cards still standing. S2's lessons are applied as C12-C15, and T15 flags K10 and K11 Test 1 for review. **S3a and S3b are done (2026-09-15):** 2 more cards dropped, 18 fact sheets written, and a shortlist of five confirmed by the founders (`research/selection_runs/run-01/3a_unknowns.md`, `3_factsheets.md`, `3_shortlist.md`); P-15 to P-17 were adopted as C16-C18. **S4 is done (2026-09-16):** the five are scored with fee feasibility and the checks, and the file's reading is that the desk cannot rank them (`research/selection_runs/run-01/4_scorecard.md`); proposals P-18 to P-22 are recorded, not applied. The founders demoted C-08 and sent C-09, C-11, C-19 and C-20 to S5 unranked (2026-09-16), and adopted P-18 and P-21 plus the S5 coverage rule as C19-C21. **S5 opened (2026-09-16): the desk half is done, and the interviews are next.** Written so far: the two counterparty-only sides' documented positions, C-19's buyer count, a recruiting map (checks T, U, V), the hypotheses, interview kit, evidence log and proposed 1-10 re-score rules (`research/selection_runs/run-01/5_validation.md`, `5_interview_kit.md`, `5_log.md`). Proposals P-23 to P-26 and decisions D-14 to D-20 await the founders. Running the rest of the process is Q5.

**Built from:**
- The 45 resources in `study_links.md`, cited here as R01-R45.
- One reading note per resource in `research/resource_notes/`, with exact quotes, page numbers and how much of the source was actually read.
- Two syntheses across resources:
  - `research/synthesis_A_methods.md`: general selection methods and problem discovery (R01-R19, R35, R36, R40, R43).
  - `research/synthesis_B_vsaas_freight.md`: vertical SaaS, fee pricing, sizing, and freight data and examples (R20-R34, R37-R39, R41, R42, R44, R45).

**Labels** (as CLAUDE.md requires):
- *verified*: the source says it. The R-ID names the source, and its note holds the quote.
- *assumed*: the source states it without evidence, or it comes from memory, a summary, or a source not checked here.
- **[our call]**: a design choice made by combining sources. Each one is a knob to tune (§10) or a decision to challenge (§9).

**How to use this doc:**
1. Run stages S0-S7 in order. §1 is the one-page view and §4 is the full procedure. Each stage produces a named file and has a gate.
2. Use the scorecard in §5 as written for the first run. Change it only through §10, and log every change in §9.
3. Use the same process one level down to pick a segment inside the chosen sub-market (Q6), and in any future market (§11).

**Contents:**
1. The process on one page
2. Vocabulary and the unit we are choosing
3. Why the process has this shape
4. The procedure, stage by stage
5. The scorecard
6. What the vertical-SaaS sources add
7. The fee-from-savings lens
8. Applying it to freight (data map, market structure, worked examples, the farmer lead)
9. Tensions between sources and how we resolved them
10. Tuning guide
11. Reusing the process
12. Limits of the evidence
13. Templates
14. Source index

---

## 1. The process on one page

```
S0 set rules ─► S1 long list (20-40) ─► S2 knock-outs (~8-15 left) ─► S3 desk facts ─► shortlist (4-6)
      ─► S4 score ─► S4.5 profit check ─► S5 talk to both sides (top 3-4) ─► re-score ─► S6 choose (1 + backups) ─► S7 record
                          ▲                                                                       │
                          └─────────────── a revisit trigger fires: return to S4 with new evidence ◄┘
```

| Stage | Question it answers | Core methods (sources) | Output | Gate to move on |
|---|---|---|---|---|
| **S0 Set the rules** | What do we want, what can we do, and how will we judge? | Fix knock-outs and weights before seeing candidates (R14, R12); personal filter (R15); core abilities (R40); prior knowledge (R36) | Criteria sheet: ambition level, team inventory, knock-outs, weights, scales. Dated. | The sheet is frozen before any candidate is scored |
| **S1 Enumerate** | Which sub-markets could we enter? | Customer group × function × method (R05/R06); jobs-to-be-done definition (R18); wide brainstorm (R15, R40); walk the shipment chain (R26); freight datasets (R31-R34, R44) | 20-40 candidate cards | Each card uses the standard sentence and is distinct from the others (R02) |
| **S2 Knock out** | Which candidates fail a must-have? | ADAMS tests (R10); Dolnicar's six knock-outs (R14); Aulet's three conditions (R16); the project's three rules plus a short CAMP check (R25) | Pass/fail sheet | About 8-15 survive. Unknowns go forward flagged; they are not dropped |
| **S3 Desk evidence** | How big, how structured, and how addressable is each one? | Bottom-up sizing (R42, R19); fragmentation screen (R20 + R44); five forces (R43); digital intensity (R45); budget and implementation (R28); labour versus software spend (R22, R23) | One fact sheet per survivor, then a shortlist | 4-6 on the shortlist (R15) |
| **S4 Score** | Which are worth winning, and which can we win? | Weighted two-axis matrix (R12, R14, R40); CAMP (R25); multiplicative check (R19); show-stopper veto (R16) | Scorecard, plot, sensitivity check | The top ranks hold under weight changes. If not, the top 3 go to S5 unranked |
| **S4.5 Profitability check** *(added 2026-09-22, C25)* | Can the card be proven profitable, or unprofitable, before any customer interview? | Audit every public source on the per-customer model's deciding inputs: real transaction documents first, then neutral studies, then the market's own economics, with vendor claims kept apart; a desk look-back on any real data found | A profitability verdict per card: proven profitable, proven unprofitable, or not provable from the web (with the residual unknowns named) | A card proven unprofitable does not go to S5 unless the founders decide otherwise |
| **S5 Validate** | Do real shippers and freight companies confirm the problem, its cost, and who pays? | Primary research (R15); Mom Test rules (R35); jobs-to-be-done interviews (R18); issue vote split by actor type (R38) | Interview log; re-scored scorecard | The evidence thresholds in §4 S5 are met |
| **S6 Choose** | Which one first, which are backups, and what is the first product? | Beachhead (R16, R17); Agile Focus (R40); wedge triangulation (R24); immediate-ROI wedge (R28); hub node (R29, R30) | One primary, 1-2 backups, growth options, a wedge hypothesis, and a parked list | Team sign-off with written deciding factors (R16) |
| **S7 Record and revisit** | Why did we choose it, and what would make us change? | Deciding factors (R16); review habit (R04, R40); three-year projection (R12) | Decision record in CLAUDE.md, with triggers | Triggers are measurable and dated |

---

## 2. Vocabulary and the unit we are choosing

### 2.1 Terms

| Term | Meaning (source) |
|---|---|
| Market | "a group of people and the job they are trying to get done" (R18, *verified*) |
| Sub-market | "a smaller slice of the overall market where the products, competitive environment, or customer usage differ significantly from the rest of the market" (R01, *verified*). R02 gives five signs that one exists: unique product features, distinct customer groups or uses, specialised competitors, different prices or costs, and tailored distribution (*verified*) |
| Segment | A group of customers inside a sub-market who share needs or behaviour. "Sub-markets revolve around product categories, whereas market segments revolve around customer needs or behaviors" (R01, *verified*). Order of work: identify sub-markets, decide where to compete, then segment inside the chosen one (R01) |
| Beachhead | The first market you set out to dominate. Its end users use the same product, buy through the same sales process, and talk to each other (R16, *verified*) |
| Wedge | The first product sold into the beachhead. Chosen by "what the customer will immediately adopt, what you can build quickly, and the attractiveness of that wedge to support a large business down the road" (R24, *verified*) |
| SOM / SAM / TAM | What you can serve and win from day one; what a broader product and sales reach could win; "all revenue in the startup's zone of value" (R42, *verified*) |
| Savings pool **[our call]** | The avoidable cost a candidate's customers incur each year that software could remove, measured the way a fee would be measured. It is the project's working currency, because "the fee has to come out of savings" (CLAUDE.md) |

### 2.2 The unit: one candidate freight sub-market

Each candidate is written as one cell of Abell's three-axis grid (R05, summarised in R06):

> **"[shipping job] for [shipper group], handled today by [freight-company type or method]"**

- **Who** (Abell's customer groups): the shipper group. It can be cut by commodity, shipper industry, size, region, or technology habits.
- **What** (customer functions): the shipping job, in the shipper's own words. Examples: buy capacity, tender and track loads, audit and pay freight bills, handle claims, book dock appointments, clear customs.
- **How** (technologies): the freight-company type or method doing the job today. That can be an asset carrier (truckload, LTL, reefer, flatbed, drayage), a broker, a managed-transportation 3PL, a forwarder or customs broker, an in-house fleet, or spreadsheet and phone.

**Why this unit:**
- Abell: "The choice is one of technologies, functions and customers to serve" (R06, *verified*).
- It matches the project's two-sided definition: shippers plus the freight companies that handle their freight (`prompt.txt`).
- It meets Ulwick's tests of a good market definition. It "does not assume a product or a solution", it stays stable as technology changes, and it "reveals all sources of competition" (R18, *verified*).
- Day says different purposes need different definitions (R07, *verified*: abstract). Defining by customer usage (bottom-up) serves problem discovery. Defining by shared capabilities (top-down) serves judging leverage and ability to win.

**Every card also records four roles**, because in freight they are often different parties **[our call]**:
1. Whose cost falls.
2. Who decides.
3. Who pays.
4. Which side is harder to win. Aulet: "start by focusing your efforts on the more difficult side first. It is usually on the demand side, but not always" (R15, *verified*).

**Two-sided rules from the sources:**
- Do each step once for each side of the market (R15).
- Ulwick's definition canvas "can be used twice to define both sides of a double-sided market", and once for each party in a distribution chain (R18).
- Dolnicar's two axes compare "us versus the segment", not shipper versus carrier. Both sides therefore need their own rows in the scorecard (R14 note).

---

## 3. Why the process has this shape

Ten design principles. Each one gives its reason, what it guards against, and the alternative we did not take.

**P1. Fix the rules before looking at candidates.**
- Dolnicar agrees the knock-outs and the weighted attractiveness criteria in Step 2 of her method and applies them only at the final choice in Step 8. Her reason: "there is no single best measure of segment attractiveness ... necessary for users to return to their specifications of what an ideal target segment looks like for them" (R14, *verified*).
- In the directional policy matrix (DPM), each manager "vote[s] with 100 points" before scoring, to beat "the 'who shouts the loudest' approach to management meetings" (R12, *verified*).
- Guards against: tuning the criteria to fit a favourite, such as the farmer lead.
- Not taken: Aulet's unweighted, discussion-only ranking (R16). We keep his discussion step and fix the weights first.

**P2. Go wide before going narrow.**
- Aulet: build "as long a list as possible ... Let a thousand flowers bloom!", because good beachheads often "exist on the fringe" (R15, *verified*).
- Where to Play: "A varied set of market opportunities is an asset in and of itself" (R40, *verified*).
- Steve Blank reports a *Management Science* study of 85 VC-backed startups: experienced founders "generate a portfolio of market opportunities before deciding where to play" (R40, via Blank; the paper itself was not read).
- Guards against: anchoring on the first idea. Shane found that founders discover "opportunities related to the information that they already possess" (R36, *verified*: abstract), so a deliberately wide list is how we see past our own starting assumptions.

**P3. Run cheap pass/fail gates before expensive scoring and research.**
- Aulet: primary research is "time-consuming and expensive in terms of opportunity costs, so you want to focus your research on compelling candidates" (R16, *verified*).
- R04 separates "evaluate segment viability" from "evaluate attractiveness". R14 re-checks the knock-outs before any scoring.

**P4. Ask two separate questions: is it worth winning, and can we win it?**
- Three independent sources use the same two axes:
  - the DPM: market attractiveness against business strength (R12);
  - Dolnicar: "How attractive is the segment to us?" against "How attractive are we to the segment?", or "Would you like to marry this person? ... Would this person marry you?" (R14);
  - Where to Play: "value creation potential" against "the overall challenge in capturing this value" (R40).
- Kotler's rule adds fit with "company objectives and resources" (R09; not verified at the source).
- Guards against: chasing a large market we cannot win, or an easy one not worth having.

**P5. Measure in savings, not in freight spend.**
- This follows from the project's fee rule.
- a16z's worked example: save a customer one $60k worker and "capture 10% of this upside" (R23, *verified*).
- The CAMP test asks whether an outcome can carry a fee (R25).
- Freight already has a precedent. Managed-transportation 3PLs charge "a percent of the purchased transportation" and "may include gainshares where transportation savings are shared" (R33, *verified*).
- Euclid warns against sizing a market from customer ROI (R42). So the savings pool caps what each customer can pay; it is not the market size (see §9, T12).
- Guards against: Simkin & Dibb's finding that practitioners fall back on "short-term profitability measures" (R13, *verified*: abstract), and against mistaking large freight spend for a large software opportunity.

**P6. Scores structure the discussion; they don't make the decision.**
- The DPM gives "objectivity ... an input" (R12). Dolnicar's plot "serves as a useful basis for discussions" (R14). Where to Play makes teams "less susceptible to biases and intuition" (R40).
- Cohen calls his own score "dangerously close to a silly quiz ... having to think through the answers and trade-offs is most of the value of the exercise" (R19).
- No source in the study list shows that weighted scoring predicts venture success (synthesis A, §S4).
- Hence: coarse scales, a sensitivity check, and written deciding factors.

**P7. Desk evidence narrows the list; talking to customers decides.**
- Aulet: "Somewhere around 90% of the data in the chart came from direct interaction", and "If there is already a market research report out there with all the information you need, it is probably too late for your new venture" (R15, *verified*).
- Cohen's failure pattern: the founder talks to three customers, they agree the problem exists, the founder builds the product, "Founder fails to make enough sales" (R19).
- Bushel's founder on the first decade of agtech: "solutions looking for problems" (R30).
- The Mom Test: "You shouldn't ask anyone if your business is a good idea" (R35, *verified*: official blurb).
- Desk data are still the right tool for cutting a long list: Cohen's Fermi estimates "avoid the analysis-paralysis of deep research" (R19).

**P8. Start narrow and keep related options open.**
- For focus:
  - Aulet: "burn the boats!" (R16).
  - Moore: target "a single, highly challenging use case in a single industry" (R17).
  - Cohen: re-target a niche when the numbers fail (R19).
  - Flexport's self-imposed constraint (R26).
  - Euclid: "make a small number of users really love you" (R24).
- For flexibility: 72% of 25 technology ventures had to change their initial market within three years, and those that entered broadly, with closely related options, did better (R40, working paper, *verified*).
- Hence: one primary, one or two related backups, and everything else parked. Where to Play: "Say 'no' to all other options" (R40).

**P9. Write down the decision, its reasons, and what would change it.**
- Aulet's worksheet has a "Key deciding factors" row (R16). Dolnicar sends the choice to an advisory committee (R14). Where to Play: "Make it a habit whenever you need to revisit your strategy" (R40).
- CLAUDE.md: "Always record how we decided, not just what."

**P10. Size the beachhead precisely; judge the expansion path rather than the TAM.**
- Euclid: "It's not the TAM you start with; it's the TAM you exit with" (R42). Euclid also aims "for high resolution on beachhead" and gives three expansion axes (R24).
- Tidemark sizes a vertical by "number of locations, initial ARPU, and expansion ARPU" (R20).
- Aulet asks: "Can you leverage this market segment to enter others?" (R16).

---

## 4. The procedure, stage by stage

Each run keeps its files in `research/selection_runs/run-NN/` **[our call]**. The templates are in §13.

### S0: Set the rules

**Purpose:** fix what "best" means before any candidate is on the table.

**Steps:**
1. **Ambition level.** ~~Write down whether we are building an indie-scale business or a venture-scale one, because it sets the size floor.~~ *Changed 2026-09-14 (C1):* state the ambition as numbers: the floor outcome, the stretch outcome, the time horizon and when it starts, and the funding. Then derive the K5 size floor from the floor: minimum fee pool = floor yearly revenue ÷ the market share we expect to win (§10). Run 01 showed why: "net $10M" had three readings whose revenue needs differed four-fold (S0.2, D1). **[our call]**, because the sources' floors differ by orders of magnitude:
   - Cohen's viability threshold is about 100k businesses with real budgets, where a score of 1 or more means a viable indie business (R19).
   - Euclid's venture-scale floor is a beachhead SOM "in the vicinity of a few hundred million" and a path to a "$15B TAM / $100m ARR" (R42). Part II uses "$100M for a beachhead" (R24).
2. **Team inventory.** List our skills, freight contacts, insider knowledge, and places where we can watch the work being done (R36; R15's matrix row "existing knowledge and contacts in market"; R40's "core abilities"). Note anywhere a founder has "lived the problem" (R26, R27, R29).
3. **Personal filter.** Name the kinds of candidates we would not spend years on. Aulet: "Is this market segment one I could get really, really excited about and dedicate the next six years of my life to serving? ... If not, don't do it" (R15).
4. **Freeze the knock-out list** (§5.1).
5. **Freeze the weights.** Each team member privately splits 100 points across the Axis A criteria and another 100 across Axis W (§5.2, §5.3). Average the splits (R12). Then check the DPM balance rule: a mix of short-term and long-term criteria, and of criteria about us and criteria about the market (R12).
6. **Freeze scales and rules** (defaults in §10):
   - 1 / 0.5 / 0 at the desk stage, and 1-10 after interviews;
   - scores add up within each axis;
   - a show-stopper vetoes a candidate;
   - Cohen's multiplicative score is run as a check.
7. **Date the sheet.** Any later change goes in §9 with a reason.

**Output:** `0_criteria.md`. **Gate:** no candidate is scored until this file exists.

**Pitfalls:**
- Letting the farmer lead shape the weights.
- Leaving the ambition level unset, so size floors get argued case by case.

#### S0 record, run 01 (opened 2026-09-14)

This run's S0 has four parts:
1. **Initial decision:** the founders' instincts, as stated.
2. **Research:** the evidence for and against each part of it.
3. **Finalized decision:** made together by the founders and Claude once the research is done. When signed, part 3 becomes the frozen criteria sheet for run 01 (`research/selection_runs/run-01/0_criteria.md`).
4. **Outstanding items:** what is left to investigate or decide before S0 can be frozen, and which decisions each could change (S0.4).

##### S0.1 Initial decision (founders, 2026-09-14)

In the founders' words:
> "I believe a highly to medium fragmented market with few incumbents is our best bet. This should be small to medium scale, where we can practice freight savings to eventually scale or transfer to other subsequent markets. We want medium scale really, too small makes this not worth the costs. We want to be able to net $10 Million from this excursion, within 5 years. Meaning the Market Share must accomodate for this. Small to Medium Businesses are more accessible as well, since we can reach out directly. But we would want enough businesses to be in the market/segment so if one avenue fails we can continue to reach out to others."
>
> "100 Point Weight Split: 40 Market Size; 45 Many Businesses, Fragmentation; 15 Opportunity for Growth, how learnings in this market can apply to other markets so we can go Vertical after this Horizontal SAAS has been built."

Clarification of the $10M target, same day:
> "$10M Revenue, also just a $10M valuation as well. It could be $250K-$1M Profit I'd be more than happy."

The same instincts, split into six decisions. The last column is where each one lands in this doc; that mapping is **[our call]**.

| # | Decision | Founders' words | Where it lands |
|---|---|---|---|
| D1 | Ambition: medium scale within 5 years. Any of three outcomes would count: $10M in revenue, a $10M valuation, or $250K-$1M in profit (a year, presumably; to confirm in S0.3) | "We want medium scale really, too small makes this not worth the costs." "Meaning the Market Share must accomodate for this." Clarified: "$10M Revenue, also just a $10M valuation as well. It could be $250K-$1M Profit I'd be more than happy." | S0 step 1; K5 size floor; §10 rows "Ambition level" and "Size floor" |
| D2 | Sell to small and mid-sized businesses (SMBs), reached directly | "Small to Medium Businesses are more accessible as well, since we can reach out directly." | K10 becomes active; W1 |
| D3 | Market structure: fragmented, with few incumbents | "a highly to medium fragmented market with few incumbents is our best bet" | A4 and K10 (many small customers); W4 (few competitors) |
| D4 | Depth: enough businesses that one failed avenue is not fatal | "enough businesses to be in the market/segment so if one avenue fails we can continue to reach out to others" | K5; A4; W1 |
| D5 | The first market is a practice ground whose lessons transfer | "practice freight savings to eventually scale or transfer to other subsequent markets" | A6; S6 backups and growth options |
| D6 | Weights: 40 market size / 45 many businesses and fragmentation / 15 growth | the 100-point split above | Axis A: A1 = 40, A4 = 45, A6 = 15, so A2, A3, A5 and A7 get 0. Axis W: no split given |

Not yet answered: the team inventory (step 2), the personal filter (step 3) and the Axis W weights (step 5).

##### S0.2 Research: does the evidence support each decision?

**How this was checked (2026-09-14).** Two evidence checks. Each one looked for evidence that supports the founders' instinct and for evidence against it:
- **Check A**, `research/s0_check_A_ambition_economics.md`: the $10M target, growth and valuation benchmarks, SMB churn and acquisition cost, and fee shares (sources N-A01 onward).
- **Check B**, `research/s0_check_B_structure_access.md`: fragmentation, incumbents, reaching SMBs, depth, expansion, weights, and six freight-software cases (sources N-B01 to N-B31).

The full quotes, dates and access status are in those files. This section keeps each finding, its source ID and its label. N-A and N-B sources are listed in §14.

**Verdicts at a glance:**

| # | Decision | Verdict | In one line |
|---|---|---|---|
| D1 | Ambition | Partly supported | Both outcomes the founders would be "more than happy" with need about $2.5M of yearly recurring revenue by year 5. That is realistic but roughly a top-quartile result. $10M is a top-decile result |
| D2 | SMBs, reached directly | Partly supported | Direct selling wins the first customers. Every company that scaled then added a channel partner, a free product or payments |
| D3a | Fragmented customers | Partly supported | One of two well-documented vertical-SaaS patterns, not the only norm. Freight's carrier and broker sides are fragmented |
| D3b | Few incumbents | Not supported as a way to pick | The sources split. The better-documented signal is customers already spending on the problem, with weak or legacy software for that job |
| D4 | Enough businesses | Partly supported | The sources measure "enough" in revenue and also cap size so word of mouth works. At the founders' scale the number of freight firms is rarely the limit |
| D5 | Lessons transfer | Partly supported; the terms are swapped | The plan is vertical SaaS followed by horizontal expansion. It works where segments share a customer type or workflow, and often slowly |
| D6 | 40/45/15 weights | Not supported as a split | 85 points on size and count is far above published scorecards, counts the number of businesses twice, and gives pain and ability to pay nothing |

**Is this the norm for a first vertical SaaS?** In parts.
- **The target customer is normal.** Fragmented small-business verticals are the pattern most vertical-SaaS investors write about (R20, N-B08, N-B09), and freight's carrier and broker sides fit it. It is not the only pattern: concentrated industries with large contracts are just as well documented (R24, N-B08).
- **The ambition is modest by the documented standards, which suits a first company.** At about $2.5M of yearly recurring revenue, the right comparables are small vertical-software businesses of the kind Constellation Software buys (N-B12), and the freight-software sales of Aljex and BoxTop (N-B24, N-B25). Venture-backed companies are the wrong comparison.
- **Three parts are not the norm** and should change before S0 is frozen:
  - using "few incumbents" as a reason to pick a market (D3b);
  - relying on direct outreach alone to grow (D2);
  - the 40/45/15 weights (D6).
- **First-time founders start with lower odds.**
  - Among venture-backed companies from 1986-2000, judged by whether they went public, predicted success was 20.9% for first-time founders against 30.3% for founders with a prior success (N-A22, *verified*).
  - Three or more years of work in the specific industry roughly doubles the chance of building a top-growth firm (N-A23, *verified*). This is the effect the founders can act on, through the team inventory (S0 step 2) and W2.

**D1. Ambition: medium scale within 5 years: partly supported.**

What each outcome needs (check A; the arithmetic is **[our call]**):

| Outcome | How it converts | Yearly recurring revenue (ARR) needed by year 5 |
|---|---|---|
| $250K-$1M profit a year: the "more than happy" floor | Profit ÷ margin. In 2025, bootstrapped SaaS firms with $3-5M ARR had a median margin of 10%; across all bootstrapped firms the median was 5.5% (N-A06, *verified* from the charts) | $250K at 10%: **$2.5M**. The range runs from $0.83M at a lean 30% margin to $5M at 5%. $1M of profit at 10% needs $10M |
| A $10M valuation | $10M ÷ revenue multiple. Private SaaS "generally transact between 2x and 7x ARR in 2026", and firms at $5-10M ARR at "3.5x to 5.5x ARR". Below about $5M of value, buyers price on owner earnings instead (N-A09, FE International, a sell-side advisor; *verified*). The public SaaS median was 4.6× on 31 Aug 2026 (N-A08) | **$2.5M** at 4×. The range runs from $1.8M at 5.5× to $4.0M at 2.5× |
| $10M revenue: the stretch | — | **$10M** |

So the two outcomes the founders would be happy with need a business of the same size, about $2.5M ARR. Only $1M a year of profit, or $10M of revenue, needs four times more.

Supports:
- **$2.5M ARR in 5 years is on a documented path.** A company that grows at the median rate for its size every year ends year 5 at about $2-3.4M ARR, if it reaches $0.25-0.5M in year 1. This is check A's arithmetic from High Alpha's 2025 benchmarks of 800+ firms (N-A10) and SaaS Capital's bootstrapped medians (N-A06).
- **Businesses this size sell in freight software.** Aljex, with about 400 broker customers, sold for $32.4M in 2018; BoxTop sold for about $13M in 2024 (N-B24, N-B25, *verified*).
- **Profit is realistic at this scale.** "83% of bootstrapped companies are operating within two percentage points of breakeven or are profitable" (N-A04, *verified*).

Does not support, or qualifies:
- **Even the floor is a better-than-average result.** In ChartMogul's data on 6,525 software companies, "25.1% reach that figure [$1M ARR] within 5 years" of first revenue (N-A01, *verified*). The share reaching $2.5M is not published, but it must be lower.
- **$10M by year 5 is a top-decile result.**
  - "One-in-ten makes it to $10 million ARR" within ten years (N-A01).
  - Getting there takes upper-quartile growth four years in a row (N-A10), about Battery's venture-backed "T2D3" path (N-A12).
- **Documented small-business vertical companies took about 7 years to reach $10M.**
  - Mindbody launched its SaaS product in 2003 and had $4.4M of recurring revenue in 2008, $6.8M in 2009 and a plan for $11.4M in 2010 (N-A36).
  - Levelset: "$1M to $10M took 6 years" (N-A37). Euclid's piece on it is titled "Why $1–10M ARR is the Hardest".
- **"Profit" and "valuation" need definitions.**
  - Owner earnings that include the founders' pay need less revenue than profit left after paying market salaries.
  - A valuation is only real in a sale or a priced funding round (N-A09).

What it means for the decision:
- **Record the ambition as "indie-plus"** (check A): plan on about $2.5M ARR by year 5, and keep $10M as the upside the market must still allow.
- **Set the K5 floor from the "more than happy" outcome.**
  - The entry segment's yearly fee pool (reachable businesses × realistic fee) should be about **$25M or more**, which is $2.5M ARR at a 10% market share.
  - That equals about 5,000 reachable businesses at $5k a year each, or 2,500 at $10k (check A, **[our call]**).
  - This gives the unvalidated "tens of millions" floor in §10 its first grounding. 10% is conservative: vertical leaders often take more than 40% (N-B09).
- **Test the stretch as a scored ceiling, not a knock-out.** The beachhead plus its adjacent segments should hold a fee pool of about $50-100M a year (A1, A6).
- **Decide how to fund it.** Median growth is 20% for bootstrapped firms and 25% for equity-backed ones (N-A03), but equity-backed firms at $1-20M ARR run at negative margins (N-A06).
- **Convert savings into fees at realistic shares.**
  - Documented fees taken from savings run 9-12.5% for large recovery audits (N-A28), 25-50% for parcel and freight audits where the vendor does the recovery work (N-A25, N-A26), and about 50/50 for managed-transportation gainshares (N-A30, *assumed*: page blocked).
  - No source gives a software-only share in freight, so plan at 10-25% (check A).
  - At 25%, a $5k yearly fee needs $20k of realised savings per customer. Audits recover about 2-8% of freight spend (N-A26, N-A32), so that customer spends roughly $250k-$1M a year on freight **[our call]**.
  - So the fee rule sets how small an "SMB" customer can be.

**D2. Sell to SMBs, reached directly: partly supported.**

Supports:
- Aulet: deal directly with customers at the start, because "direct customer feedback is an essential part of that process" (R15, *verified*).
- Toast sold "direct to SMBs today via an inside sales force", led by a co-founder who had "never sold anything in his life", with a "6-8 month payback on sales efforts" (N-B19, Bessemer's 2015 memo, *verified*).
- In SMB verticals, the buyer "is often the owner, or sits next to the owner", and "local merchants _talk_" (N-B09, Tidemark, *verified*).
- In freight the prospect list is public. Every carrier and broker authority is in the FMCSA census file (N-B04, *verified*).

Does not support, or qualifies:
- No source shows direct outreach alone scaling to thousands of SMB customers. Each company that scaled added something:
  - a distributor partner: Gordon Food Service brought in about 25% of Toast's bookings by 2015 (N-B19, *verified*);
  - a free product timed to a regulation: Motive's free driver app had a million downloads in four years before its paid products, timed to the ELD mandate (N-B22, *verified*);
  - payments, which can "increase revenue per customer by 2-5x" (N-B11, a16z, *verified*).
- Selling one-to-one to dispersed customers failed on acquisition cost in agriculture (R30).
- The smallest freight firms have the least to pay with and close most often:
  - truckload profit margin of -2.3% (R38);
  - 91.5% of carriers run 10 or fewer trucks (N-B01, ATA, 2024 data, *verified*);
  - active broker authorities fell by 3,104 in 2024 (N-B04, *verified*).
- ServiceTitan, a leader in a fragmented SMB vertical, chose not to target firms with five or fewer employees (N-B20, S-1 filing, *verified*).
- **Direct selling pays only at higher fees.**
  - Practitioner thresholds put inside sales at "$5K-$50K" a year per customer, and self-serve below "$5K" (N-A20, Tunguz, *verified*).
  - Inside sales costs $5-15k to win a customer. For that to pay back within 12 months at an 80% gross margin, the fee has to be about $6-19k a year per customer (check A, **[our call]**).
  - Bessemer asks SMB-focused firms to "target CAC payback <12 months" (N-A13).
- **Small contracts churn most.**
  - In High Alpha's 2025 survey, contracts under $10k a year kept only 83-88% of their revenue each year, or 94-98% counting expansion (N-A10, p. 41, *verified*).
  - At $5k per customer and 85-88% retention, a $10M base of 2,000 customers loses 240-300 customers a year that must be replaced before any growth (check A, **[our call]**).
- Janz: "Most customer acquisition channels are either scalable or profitable but not both" (N-A15, *verified*).

What it means for the decision:
- Keep direct outreach for the first customers, and run it as an S5 test: replies per 100 contacts and time to a first meeting become W1 evidence.
- Name the channel that would carry growth after the first customers (a partner, a free tool, or payments), and score W1 on that channel.
- Set a firm-size floor. Are one-truck owner-operators in scope?
- Pair direct outreach with a price floor. A candidate sold through founder-led outreach should support about $5k or more a year per customer, with payback within 12 months. Otherwise it must name a channel that scales (check A, **[our call]**).

**D3. A fragmented market with few incumbents.** These are two separate claims, so they were checked separately.

*D3a. Fragmented customers (many small buyers): partly supported.*

Supports:
- Tidemark: target "a market with lots of small and midsize merchants" (R20). "Most verticals are highly fragmented, and the end customers are typically small business merchants." Leaders in vertical and SMB markets "can exceed 40%+ market share", against under 20% in horizontal markets (N-B09, *verified*; partly gated).
- Bessemer: Mindbody, Clio and Weave reached leadership "by starting in the SMB segments overlooked by incumbents" (N-B08, 2022, *verified*).
- a16z backed MVMNT specifically for small and mid-sized freight brokers (R27).
- Freight fits the pattern on the carrier and broker side. The top 50 firms hold about 10-19% of revenue in local and specialized trucking, and 34-37% among brokers and truckload carriers (R44; §8.2).

Does not support, or qualifies:
- The opposite pattern, concentrated industries with large contracts, is just as well documented:
  - Veeva, Guidewire and nCino. Bessemer: "There are only about five thousand banks in the US. Without six-figure deals, our portfolio company would have never achieved IPO scale" (R24; N-B08, *verified*).
  - Emergence prefers concentration because it lowers acquisition cost and helps word of mouth (R21).
  - Bessemer: "Many verticals require a move up-market to sustain growth" (N-B08).
- At the founders' scale, the closest record is Constellation Software, which buys and runs small vertical-software businesses. Its markets are "tiny", and "usually characterised by a gradually consolidating customer base" (N-B12, letter on 2016, *verified*).
- Fragmented freight turns over fast:
  - 5,409 fewer brokers since January 2022 (N-B04, *verified*);
  - 88,000 trucking authorities revoked in 2023 (N-B03, *assumed*: secondary compilation).
  Constellation's test for this: churn because old customers go bankrupt while new ones form can still be attractive, but churn because switching costs are low makes the business "unpleasant" (N-B12, *verified*).
- Convoy shut down in 2023 after raising about $1.1B. A trade-press obituary blames, among other things, the "thousands of other freight brokers" shippers could switch to (N-B29, opinion).

*D3b. Few incumbents (few competitors): not supported as a way to pick a market.*

Supports:
- Thiel: the perfect target market is "served by few or no competitors" (N-B13, *assumed*: quote pages only, book not read).
- Cohen: in a small market "you might not have many viable competitors" (R19).
- Tidemark, on small verticals: "fewer competitors are being funded to compete" (N-B09).
- Bushel's grain-handling middle was open because "There's just so few software investments" (R30).

Does not support:
- Paul Graham: "A crowded market is actually a good sign, because it means both that there's demand and that none of the existing solutions are good enough" (N-B14, *verified*).
- Constellation: "most vertical markets have several viable competitors" (N-B12, *verified*). The attractive case it describes is "a few rational competitors intent on making a decent living", not none.
- Toast entered against Micros and NCR, "each accounting for roughly 25% market share" (N-B19, *verified*).
- Cohen asks for proof of budget, not an empty field: "You want to target companies who outsource this particular problem to outside vendors" (R19).

The freight check:
- Small brokers already use McLeod, homegrown systems, Truckstop's ITS Dispatch and Ascend TMS (N-B04, *verified*).
- Aljex had about 400 broker customers when it was sold (N-B24).
- MVMNT, Rose Rocket and Alvys are venture-funded entrants (N-B26 to N-B28).
- So "few incumbents" is false for small-broker software as a category. It may still hold for particular savings jobs (freight audit, detention billing, claims), which were not checked. That belongs in S3, fact-sheet item 9.

What it means for the decision:
- Keep fragmentation, but score it as structure (top-50 share, buyer power) for each side. Choosing SMBs in D2 makes knock-out K10 active.
- Replace "few incumbents" with a test scored in W4. Customers already spend on the problem: they pay a 3PL, auditor or broker, or spend staff time on it. And today's software for that job is weak, legacy or missing.

**D4. Enough businesses that one failed avenue is not fatal: partly supported.**

Supports:
- Every source wants a beachhead big enough for the goal. Aulet's worksheet asks "Is the market big enough to be interesting?" (N-B17, *verified*).
- Resilience from options is backed by data. In Where to Play's sample, 72% of ventures changed their initial market within three years, and those with closely related options did better (R40).

Does not support, or qualifies:
- The sources measure "enough" in revenue, not in number of firms. Aulet's TAM is "how much annual revenue you would accumulate if you achieved 100% market share" (N-B17, *verified*).
- They also cap the size:
  - Aulet: "Is it reasonable in size for us to achieve meaningful word of mouth, meaning it is not too big?" (N-B17, worksheet 04.4, *verified*);
  - Moore: "big enough to matter but small enough to lead" (N-B16, *verified* on Moore's own blog).
- The "$20-100M a year" beachhead range often credited to Aulet appears only in book reviews (N-B18, *assumed*). His own SensAble example was about $10-15M a year (N-B17).
- Businesses of the founders' size have sold in freight software:
  - Aljex, broker software with about 400 customers, sold for $32.4M in 2018 (N-B24, *verified*);
  - BoxTop, software for small and mid-sized forwarders, sold for about $13M in 2024 (N-B25, *verified*).

The arithmetic **[our calc]**. Customers needed = target yearly revenue ÷ revenue per customer; firms needed = customers ÷ market share.
- At $6k a year per customer, $3M of yearly revenue needs 500 customers and $10M needs about 1,667. At a 20% share, that is 2,500 to 8,333 firms (check B).
- Freight has about 25,000 active broker authorities (N-B04), 17,130 broker and forwarder employer firms, and more than 50,000 employer firms in each of truckload and specialized trucking (R44).
- $10M a year at a 10% share of the firms outside the top 50 needs about $1,900-3,100 per customer in the trucking codes, and about $5,900 among brokers and forwarders (R44 data).
- Count only becomes the limit at around $1,200 a year per customer, and those are the customers least able to pay.

What it means for the decision:
- State "enough" as the K5 floor, in yearly fee potential, derived from D1's floor outcome: about $25M a year or more (D1).
- Add a word-of-mouth ceiling to K2 (R16).
- Get resilience from one or two related backup segments (S6), which the process already requires, rather than from a raw count.

**D5. The first market as a practice ground whose lessons transfer: partly supported, but the terms are swapped.**

The terms:
- "Vertical" and "horizontal" come from a matrix with products as rows and industries as columns. "By launching net new products, you are moving vertically on that chart. By venturing into new industries, you are moving horizontally" (R24, footnote 2, *verified*).
- A product for a freight sub-market is already vertical SaaS. The founders' plan, one freight sub-market and then others, is therefore vertical SaaS followed by horizontal expansion.
- A second reading is possible: build a horizontal capability, such as a savings-measurement engine, then specialise it for each sub-market. The founders should say which they mean (S0.3).

Supports:
- Expansion leverage is a standard criterion (R16, R17, R24, R40). The founders' 15 points matches the default A6 weight.
- ServiceTitan began in residential plumbing and turns its "learnings from trades we have penetrated so far into a proven strategy to enter new trades verticals" (N-B20, *verified*). Mindbody went from yoga studios to salons (R24).
- Moore: the next target is "an _adjacent_ process owner, someone for whom your chasm-crossing sponsor would make a good reference" (N-B16, *verified*).

Does not support, or qualifies:
- Transfer is slower and harder when workflows differ:
  - ServiceTitan entered trades with different workflows (pest control, lawn care, landscaping) by acquisition (N-B20);
  - Veeva still calls its products outside life sciences "initial applications" years after entering those markets (N-B21).
- The more common growth path is new products for the same customers:
  - Bessemer's "layer cake" of new products (N-B08);
  - multi-product companies grew about 21% faster in Tidemark's benchmark of 200+ companies (N-B10);
  - payments is "almost certainly the most popular vertical expansion modality" (R24).
- Motive's move from trucking into other fleet industries was venture-funded ($567M raised by 2023) and rode a one-off regulatory deadline (N-B22).
- At the founders' scale, Constellation shows that one niche plus add-on products can be enough (N-B12).

What it means for the decision: define A6 as "adjacent freight sub-markets that share the customer type or the workflow, plus add-on products (payments, factoring, audit) for the same customers", and decide which of Euclid's three axes comes first (R24).

**D6. The 40 / 45 / 15 weight split: not supported as a split.**

- **Far above published norms.**
  - Scorecards that assign weights give market size about 10-25%. Payne's angel scorecard gives "Size of the Opportunity" 25% and the team 30% (N-B30, *verified*).
  - Aulet's eight beachhead criteria are unweighted, about 12.5% each (R16), and Gurley counts fragmentation as one factor in ten (R41).
  - Only Tidemark's unweighted three attributes (gigantic, fragmented market, fragmented value chain) put similar emphasis on size and fragmentation (R20), and they were written for venture-scale SMB SaaS.
  - No GE-McKinsey example with published weights could be verified.
- **Counts the number of businesses twice.** Market size is built as buyers × revenue per buyer (R42, R20, R19), so scoring "market size" and "many businesses" separately counts buyers twice. The UK government's multi-criteria analysis manual: "double counting should not be allowed in MCA, since double-counted effects are likely to be given more weight in the final overall decision than they deserve" (N-B31, *verified*). Its cure is a minimum threshold, which is our K5.
- **Leaves out what the sources call essential.**
  - Pain and urgency (A3), ability to pay (K8), fit for automation (A2), and recurrence and durability (A5, A7) all get zero. Cohen's reason for multiplying his rows applies here: they are "a series of 'ands'" (R19).
  - No Axis W weights are set, although two of the founders' own beliefs (direct reach, few incumbents) are Axis W rows (W1, W4).
  - The split fails the DPM balance rule, which asks for a mix of short- and long-term, and internal- and market-facing, criteria (R12).
- **What is sound.** The emphasis on market structure matches Tidemark (R20), and 15 points on expansion matches the default.

What it means for the decision:
- Keep the emphasis, but put it where it does not double count:
  - raise A1 (fee potential) and A4 (fragmentation, defined as structure plus reachable count);
  - put "enough businesses" into K5 as a floor.
- Split 100 points across all of A1-A7 and 100 across W1-W6 (S0 step 5). Check B offers one split for discussion **[our call]**: A1 30, A4 20, A6 15, A3 15, A2 10, A5 5, A7 5.
- Keep 40/45/15 as a sensitivity case in S4 step 5, to see whether it changes the ranking.

**Second round of research (2026-09-14): durability, fragmentation and incumbents.**

S0.4 left three items that needed evidence before the founders could decide: O-3 (durability), O-4 (how to measure fragmentation) and O-5 (how to measure "few incumbents"). Two more checks ran:
- **Check C**, `research/s0_check_C_durability.md` (sources N-C01 to N-C29): what "durable" means, the published formulas, how cyclical each freight family is, how software vendors fared in 2022-25, and options for knock-out K11.
- **Check D**, `research/s0_check_D_fragmentation_incumbents.md` (sources N-D01 to N-D37): the standard concentration formulas and thresholds, how investors judge fragmentation, the freight data under each measure, and how to count incumbents for a freight job.

On 2026-09-14 the coordinator re-fetched six load-bearing sources, and all matched: S&P's cyclicality bands (N-C01), the Census firm-death rates (N-C05), the Census note on HHI (N-D02), the 2023 merger guidelines (N-D07), CB Insights' failure shares (N-D29) and Cass's description of its competitors (N-D30).

*O-3, durability (check C):*
- **No single meaning.** Sources use at least six: customer firms survive downturns; the job persists when volume falls; the market is not shrinking or being displaced; the vendor's revenue does not swing; customers keep the ability to pay; and cycle timing.
- **One published formula.** S&P rates an industry's cyclicality 1-6 from its average peak-to-trough fall in revenue (bands at 4, 8, 13, 20 and 32%) and in profit margin (3, 7, 12, 24 and 72%). The bands come from "k-means clustering", so they are statistical groupings, not viability limits. S&P rates the transportation industries it calls cyclical 5 of 6 (N-C01, N-C02, *verified*).
- **Freight is cyclical, unevenly.** The 2022-25 downturn was mostly in prices: freight volume fell 3.2% while truckload prices fell 24.1% and broker prices 32.7% (N-C08, N-C09, *verified* data; **[our calc]**). In 2023, 19.4% of general freight trucking firms closed, twice the economy's 9.4%, yet the number of firms held flat (85,509 → 85,244). Brokers and forwarders (9.4%) and warehousing (6.2%) were at or below the economy (N-C05, *verified*).
- **Some jobs were steadier than the freight dollars around them.** Cass's invoice count fell 2.3% in 2023 while the dollars on those invoices fell 14.4% (N-C15). Expeditors' customs brokerage fell 20.5% while its air and ocean freight fell 45-64% (N-C13). J.B. Hunt's brokerage load volumes fell 26% (N-C14). All *verified*.
- **Software vendors.** Those with recurring revenue grew through 2022-25: Descartes +12-18% a year, including acquisitions (N-C17). Revenue tied to transactions or freight volume fell: Uber Freight -24% (N-C16); mortgage software at Blend -18% as originations collapsed (N-C20). Whether *our* revenue swings is therefore mostly a matter of fee design, which is deferred (F-7, F-8).

*O-4, fragmentation (check D):*
- **The standard formulas are published for every freight code.** The Economic Census gives the revenue shares of the 4, 8, 20 and 50 largest firms, and the Herfindahl-Hirschman Index (HHI: the sum of each firm's squared percentage share): "2017 is the first time HHI is available for sectors other than Manufacturing" (N-D02, *verified*). Withheld values are flagged "D", not zero (N-D03).
- **The published thresholds were built for other purposes.** Antitrust bands flag mergers: "Markets with an HHI greater than 1,800 are highly concentrated" (N-D07, *verified*). On them every freight industry except couriers is unconcentrated, so they cannot rank our candidates. The two startup lines contradict each other: Tidemark wants the top 50 firms below 20% (R20), Emergence prefers them above 80% (R21). No source ties any band to acquisition cost, share won or word of mouth.
- **The most direct measure of an SMB market is small firms' share of revenue** (Census SUSB, N-D04). In 2022, firms under 20 employees held 52% of receipts in local general freight, 24% in truckload and in brokerage, 8% in LTL and 3% in couriers (**[our calc]** from *verified* data).
- **K10 is fragile for LTL.** The census leaves out owner-operators with no payroll. If 10% of long-distance owner-operator receipts belonged to LTL, its top-50 share would fall from 82.9% to about 74% (N-D05, **[our calc]**).

*O-5, few incumbents (check D):*
- **The founders' "ballpark number" has an official precedent.** "The Agencies may instead measure market concentration using the number of significant competitors in the market", when shares are hard to measure (N-D07, footnote 12, *verified*).
- **A count is cheap; shares exist only for some jobs.** Small-broker TMS: 20 named systems, and the leader, McLeod, has about 16% (N-B04 chart, read by check D). Freight audit and payment: "Competition consists of a few primary competitors and numerous small transportation bill audit firms" (N-D30, *verified*). Detention billing: no shares found.
- **The evidence does not support a cap on the number of competitors.** Of 101 startup post-mortems, 42% cited not targeting a "market need" and 19% being outcompeted (N-D29, *verified*). It does support caution about one dominant vendor: vertical markets "tend to have winner-take-most dynamics" (N-B11); three incumbents "chased away dozens of new entrants" (N-B08).

##### S0.3 Finalized decision

_Pending. To be made together. Nothing below is decided yet._

When every row is settled:
1. Date the sheet and freeze it (S0 step 7).
2. Copy it to `research/selection_runs/run-01/0_criteria.md`.
3. Start S1.

**Decisions to make.** The "Starting point" column is Claude's suggestion from S0.2, **[our call]**, offered for discussion. The "Final" column is filled in together.

| # | Question | Options, with the evidence | Starting point | Final |
|---|---|---|---|---|
| F-1 | Which outcome sets the floor? What do "profit" and "valuation" mean? | Floor from the "more than happy" outcomes, about $2.5M ARR, or from $10M revenue, which is four times larger and a top-decile result (D1). Profit after market salaries, or owner earnings including the founders' pay? Valuation as a sale price, a funding-round price, or a paper figure? | Floor about $2.5M ARR by year 5; $10M is the stretch | **Decided 2026-09-14:** floor of $2.5M yearly revenue. Profit = the company's profit. Valuation = what another company would pay to buy it (answers below) |
| F-2 | When does the 5-year clock start? | Today, at product launch, or at first revenue. ChartMogul's base rates start at first revenue (N-A01) | | **Decided 2026-09-14:** at product launch (fourth-round answers below) |
| F-3 | How will it be funded? | Bootstrapped firms break even more often and grow a little slower (N-A03, N-A04). Venture-backed firms grow faster but lose money at this size (N-A06), and suit the $10M stretch rather than the floor | | **Decided 2026-09-14:** self-funded, with early revenue from paying design partners |
| F-4 | K5 size floor | Entry segment's yearly fee pool of at least about $25M (D1), or check B's $15-50M (D4) | At least $25M, at a 10% market share | Follows from F-1: a candidate's yearly fee pool of about $25M or more, at a 10% market share **[our call]** |
| F-5 | Which side do we sell to first? | Freight companies: counted, on a public list, fragmented. Shippers: more freight spend per firm (D2, D3; T10) | State a preference now; confirm per candidate in S4 (T10) | **Deferred 2026-09-14:** to segment selection (Q6) and later market analysis |
| F-6 | Firm-size floor | Are one-truck owner-operators in? About 70% of for-hire carriers run one truck (N-B05, *assumed*). Truckload margins are thin (R38). ServiceTitan skips firms of five employees or fewer (N-B20) | Leave out firms too small to support the fee in F-7 | **Deferred 2026-09-14:** with F-5 |
| F-7 | Expected yearly fee per customer, and the channel | $5k or more, sold directly or by inside sales; or under $5k, with a named channel that scales (D2) | $5k or more, or name the channel | **Deferred 2026-09-14:** not a sub-market-selection decision |
| F-8 | Fee share of savings | Software only: 10-25%. With a done-for-you audit or recovery service: 25-50% (D1) | 10-25%, software only | **Deferred 2026-09-14:** with F-7 |
| F-9 | How is fragmentation measured? | Raw count, reachable count, or structure: top-50 share and buyer power (D3a, D6) | Structure per side on the census screen, plus reachable count; K10 active | ~~**For further investigation (2026-09-14):** use an existing formula, or documented business practice (answers below)~~ **Decided 2026-09-14 (O-4):** top-50 share for the zones, plus a small-firm check. K10 fails above 85%; 75-85% goes forward as unknown and is settled at S3 by small firms' share of revenue. A4 scores structure plus a small-firm bonus; the number of buyers stays in A1 and K5 (C9; fifth-round answers below) |
| F-10 | Replace "few incumbents"? | Keep it, or replace it with "customers already spend on the problem, and today's software for that job is weak, legacy or missing", scored in W4 (D3b) | Replace | ~~**For further investigation (2026-09-14):** likely a ballpark count of the companies in the space and each one's share of the market (answers below)~~ **Decided 2026-09-14 (O-5):** replaced. W4 scores proven spend plus weak, legacy or missing software. The ballpark count and market shares are recorded on every S3 fact sheet as W4's evidence. The only veto is one dominant vendor whose customers are satisfied; there is no cap on the number of competitors (C10; fifth-round answers below) |
| F-11 | Depth and breadth | K5 floor, plus a word-of-mouth ceiling in K2, plus 1-2 related backups (D4) | Accept | **Decided 2026-09-14:** yes, including the "not too big" check (C3) |
| F-12 | Which expansion axis comes first? What did "Vertical after Horizontal" mean? | New products for the same customers (Euclid's vertical axis); the same product for adjacent sub-markets (horizontal axis); or the customers' partners (value chain) (D5; R24) | | **Decided 2026-09-14:** vertical first, then horizontal. Start with a highly specific focus on one segment's use cases (vertical); only after that, expand across segments and sub-markets (horizontal) |
| F-13 | Axis A weights: 100 points over A1-A7 | The founders' 40/45/15 (D6); the doc's defaults 25/15/15/10/10/15/10 (§5.2); check B's illustration A1 30, A2 10, A3 15, A4 20, A5 5, A6 15, A7 5 | Each founder splits 100 privately, then average (S0 step 5). Keep 40/45/15 as a sensitivity case | ~~**Decided 2026-09-14:** A1 20, A2 10, A3 25, A4 15, A5 10, A6 5, A7 15. 40/45/15 kept as the S4 sensitivity comparison (answer below)~~ **Revisited 2026-09-14 (O-2):** A7 left the score (F-17), so its 15 points went to the long-term rows. Final: A1 20, A2 10, A3 25, A4 15, A5 15, A6 15. 40/45/15 is still the S4 sensitivity comparison (C7; fifth-round answers below) |
| F-14 | Axis W weights: 100 points over W1-W6 | Defaults 20/15/20/15/15/15 (§5.3). The founders' beliefs about direct reach and incumbents belong here (W1, W4) | Each founder splits 100, then average | ~~In progress; see "How the weights work" below~~ **Decided 2026-09-14 (O-1):** W1 20, W2 5, W3 20, W4 15, W5 15, W6 25 (fifth-round answers below) |
| F-15 | Team inventory (S0 step 2) | Skills, freight contacts, and years in any freight sub-industry. Three or more years in the specific industry roughly doubles the odds of a top-growth firm (N-A23) | | **Answered 2026-09-14:** limited freight knowledge and contacts today. Domain immersion comes after sub-market and segment selection, before building (answers below) |
| F-16 | Personal filter (S0 step 3) | Kinds of sub-market we would not spend years on (R15) | | **Answered 2026-09-14:** nothing is off the table for now |
| F-17 | Tolerance for downturns | The number of active brokers fell by 3,104 in 2024 (N-B04). 88,000 trucking authorities were revoked in 2023 (N-B03, *assumed*). Accept a cyclical customer base, or weight A7 higher? | | **Decided 2026-09-14:** durability is its own investigation and a hard viability check, not a scored criterion. A7 leaves the score (C6; S0.4). **K11 defined 2026-09-14 (O-3):** Test 1, no projected shrinking, and Test 3, no drastic fall in the unit a fee would be counted on. Test 2, customer survival, is recorded as a flag. The strict S&P revenue test is an S4 comparison (C8; fifth-round answers below) |

**Founders' answers, 2026-09-14** (verbatim):
> "$2.5M in yearly revenue. Profit is companys profit, I'd like to take home $250K at least in 5-7 years. Valuation is how much the company could be bought for by another company."
>
> "Self-Funded, this is SAAS so we'd like to do it ourselves and make money off of design partners for initial deployments."
>
> "Which side we sell to first will come from segment selection and further market analysis, it is way too early to tell."
>
> "Expected fee per customer, once again you're getting ahead of yourselves. We are just doing Sub-Market Selection here."
>
> "Horizontal After Vertical. Vertical means a highly specific focus for use cases of a single segment, Horizontal goes across segments and sub-markets."

**What is now settled, and what follows for sub-market selection:**

- **F-1, floor and meanings: decided.**
  - The floor is **$2.5M in yearly revenue**. $10M stays the stretch (D1).
  - "Profit" means the company's profit. The founders' personal goal is to "take home $250K at least in 5-7 years".
  - "Valuation" means the price another company would pay to buy the business. For scale: private SaaS businesses "generally transact between 2x and 7x ARR in 2026", and those valued under roughly $5M are priced on owner earnings instead (N-A09).
  - *What follows:* the K5 floor (F-4) is a candidate yearly fee pool of about $25M or more, which is $2.5M at a 10% market share **[our call]**.
- **F-3, funding: decided.** Self-funded, with early revenue from design partners who pay for the first deployments.
  - *What follows:*
    - Plan on self-funded benchmarks. Median growth is about 20% a year for bootstrapped private SaaS (N-A03), and most bootstrapped firms run at or near breakeven (N-A04).
    - The $10M stretch is a venture-backed path (N-A12), so it stays an upside only.
    - In scoring, W6 (time and resources to win) should count how much money and time a candidate needs before customers pay.
    - The paid savings assessment in S5, step 4, can double as the first design-partner revenue.
- **F-5 and F-6, entry side and firm-size floor: deferred** to segment selection (Q6) and later market analysis.
  - *What follows:* S1-S4 score both sides of each candidate and do not pick an entry side (proposed process change 8).
- **F-7 and F-8, fee per customer and share of savings: deferred.** They are not sub-market-selection decisions.
  - *What follows:* S3 still estimates each candidate's fee potential with the §10 modelling ranges. That is only to compare the candidates' size, not to set a price. Process change 5 is parked.
- **F-12, expansion: decided. Vertical first, then horizontal.**
  - In the founders' terms, vertical is "a highly specific focus for use cases of a single segment", and horizontal "goes across segments and sub-markets". The plan is to start vertical and expand horizontally.
  - This replaces the wording in S0.1 ("go Vertical after this Horizontal"), which stays as the original record.
  - *What follows:* A6 (expansion leverage) scores how far the core built for the first segment could reach across other segments and sub-markets. That matches Euclid's horizontal axis, "selling existing product lines into net-new customer verticals" (R24), and Moore's adjacent segments (N-B16). Process change 7 is answered.
- **Still open:**
  - F-2: when the clock starts;
  - F-11: depth and breadth;
  - F-14: the Axis W weights;
  - F-17: tolerance for downturns.
- **Marked for further investigation:** F-9 and F-10 (third-round answers below).

**Founders' answer on the Axis A weights, 2026-09-14** (verbatim):
> "A1 20 A2 10 A3 25 A4 15 A5 10 A6 5 A7 15"
>
> "Then, yes keep 40/45/15 as a comparison."

| Row | Criterion (§5.2) | Run 01, final (O-2) | Run 01, before A7 left | First split, 40/45/15 (D6) | Doc default (§5.2) |
|---|---|---|---|---|---|
| A1 | Savings pool and fee potential | **20** | 20 | 40 | 25 |
| A2 | Fit for automation | **10** | 10 | 0 | 15 |
| A3 | Pain and urgency (per side) | **25** | 25 | 0 | 15 |
| A4 | Fragmentation (per side; redefined, C9) | **15** | 15 | 45 | 10 |
| A5 | Frequency and recurrence | **15** | 10 | 0 | ~~10~~ 15 |
| A6 | Expansion leverage | **15** | 5 | 15 | ~~15~~ 20 |
| A7 | Durability (now knock-out K11) | — | 15 | 0 | ~~10~~ — |
| | **Total** | **100** | 100 | 100 | 100 |

- **What changed from the first split.**
  - Size and count (A1 + A4) went from 85 to 35. That removes most of the double counting flagged in D6.
  - Pain and urgency (A3) is now the heaviest row.
  - Expansion (A6) moved from 15 to 5. The 40/45/15 comparison gives A6 15, so it will show whether that change affects the ranking.
- **Balance check** (S0 step 5; R12). Short-term rows (A1, A3) and long-term rows (A6, A7) both carry weight, so the check passes. The criteria about us come from Axis W, whose weights (F-14) are still open. *Update, later on 2026-09-14: A7 has since left the score (F-17, C6). Its 15 points are unassigned, and A6 (5) is now the only long-term row. Both need re-checking when the weights are re-split (S0.4, O-2).* *Re-checked 2026-09-14 (O-2, C7):* A7's 15 points went to A5 (+5) and A6 (+10). A5 counts as a long-term row, because its sources are Cohen's "Enduring" (R19) and Bessemer's "sticky long-term value" (R28) **[our call]**. The long-term rows now carry 30 points against 45 for the short-term rows, and Axis W (O-1) holds the criteria about us, so the check passes.
- **Comparisons in S4, step 5.** The ranking is computed with this split, then again with 40/45/15 (A1 40, A4 45, A6 15, all other rows 0). If another founder submits a split, it is averaged in (S0 step 5).

**Founders' answers, 2026-09-14, third round** (verbatim):
> "Fragementation is to be measured with any existing formulas for this, or we will look into business insights as to how this is measured. The same can be said for few incumbents, we will likely look into a ballpark number of how many companies exist in the space and their slice of the market pie for this. But we will find out more, mark this for further investigation."
>
> "Nothing is off the table currently, limited knowledge about freight and limited contact this will come after Sub-Market and Segment selection I will do Domain Immersion. I am going to absorb as much as possible once I have a target, before building the Software."

- **F-9, how fragmentation is measured: marked for further investigation.** Use an existing formula, or documented business practice for how it is measured.
  - Starting points already in the evidence:
    - For each industry, the Economic Census publishes the revenue share of the 4, 8, 20 and 50 largest firms, and the Herfindahl-Hirschman Index (HHI), a standard concentration measure (R44, *verified*).
    - Tidemark's screen uses the top-50 share (R20). Emergence's test is "fewer than 50 companies represent over 80% of revenue" (R21).
  - To investigate: which measure to use, and any published thresholds for "fragmented" and "concentrated". Neither has been checked yet.
- **F-10, "few incumbents": marked for further investigation.** Likely measured as a ballpark count of the companies already serving the space, and each one's share of the market.
  - To investigate: where company counts and shares can be found for a freight job. The F-9 measures could be applied to these companies instead of to the customers **[our call]**.
- **F-16, personal filter: answered.** Nothing is off the table for now.
  - *What follows:* knock-out K9 (team would commit) passes for every candidate in run 01.
- **F-15, team inventory: answered.** Freight knowledge and contacts are limited today. The founder plans domain immersion after sub-market and segment selection, absorbing as much as possible about the target before building the software.
  - *What follows:*
    - W2 (team knowledge and access) will likely score low for every candidate, so it will do little to separate them until the immersion.
    - S5's interviews are recruited through open channels rather than personal contacts: associations, public carrier and broker lists, and trade events (§4 S5, step 1). S5 is a light round. The deep immersion comes after the choice, as the S5 scope note already says.
    - Three or more years of industry experience roughly doubles the odds of a top-growth firm (N-A23). The immersion plan is the main way to close that gap.

**How the weights work (for F-13 and F-14)**

*What they are for.* In S4, each shortlisted sub-market is scored on a list of criteria. The weights say how much each criterion counts toward the total. They are set now, before any candidate is on the table, so they can't be bent later to favour a candidate we already like (P1).

*Two scores, not one.* Each candidate gets two totals, each out of 100:
- **Axis A, "is it worth winning?"** This is about the market: 7 criteria, A1-A7.
- **Axis W, "can we win it?"** This is about us against that market: 6 criteria, W1-W6.

They stay separate so that a big market we can't win and an easy market not worth having both show up as weak. One combined number would hide which problem a candidate has. The two totals are plotted on a chart, with A going up and W going across. The top-right corner is where we want to be (P4; R12, R14).

*The arithmetic.*
- The weights on each axis add up to 100.
- At the desk stage, each candidate scores 1 (strong), 0.5 (middling) or 0 (weak) on each criterion.
- The candidate's total on an axis is the sum of weight × score.

So a criterion weighted 40 adds 40 points when the candidate is strong on it, 20 when it is middling and 0 when it is weak. A criterion weighted 0 cannot change the result at all.

*The criteria in plain words:*

| Row | The question it asks | Doc default (§5) | Where 40/45/15 lands |
|---|---|---|---|
| A1 | How much money is on the table: the yearly costs our software could remove, and so the fees we could earn across all buyers? This is "market size" in this process | 25 | 40 ("market size") |
| A2 | Is the costly work office work (data, documents, messages) that software can do, rather than physical work? | 15 | 0 |
| A3 | Do customers feel the cost, care about it, and have a reason to act now? | 15 | 0 |
| A4 | Are there many small buyers, with none big enough to dominate? | 10 | 45 ("many businesses, fragmentation") |
| A5 | Does the saving recur with every shipment or week, so the fee recurs too? | ~~10~~ 15 | 0 |
| A6 | After a deep focus on one segment (vertical), could the same core reach other segments and sub-markets (horizontal)? Vertical first, then horizontal | ~~15~~ 20 | 15 ("growth") |
| A7 | ~~Is the market growing and stable, not too cyclical?~~ Left the score on 2026-09-14 (F-17). Durability becomes a hard check, K11 | ~~10~~ | 0 |
| W1 | Can we reach the buyers cheaply? The belief that "we can reach out directly" is scored here | 20 | not set |
| W2 | Do we know this world, and do we have contacts in it? | 15 | not set |
| W3 | Can we get the data we need and show a measured saving within weeks? | 20 | not set |
| W4 | ~~What do customers use today, and how weak is it? The "few incumbents" belief is scored here~~ Do customers already pay for this job, and is today's software for it weak? The "few incumbents" count is recorded as evidence, not scored (C10) | 15 | not set |
| W5 | Are customers willing to change how they work? | 15 | not set |
| W6 | How much time and money would it take us to win? This matters more now that we are self-funded | 15 | not set |

*Run 01's final weights (O-1, O-2):* A1 20, A2 10, A3 25, A4 15, A5 15, A6 15; W1 20, W2 5, W3 20, W4 15, W5 15, W6 25 (the F-13 and F-14 rows above).

*Three things to know before splitting the points:*
1. **Knock-outs already remove markets that are too small.** K5 rejects every candidate below the floor (about $25M a year of fee potential, F-4) before any scoring. So the weight on A1 only chooses between candidates that are all big enough.
2. **A1 already contains the number of businesses.** A1 is worked out as the number of buyers × what each would pay, so a heavy weight on A4 rewards the count a second time.
   - Example: market P has 10,000 firms paying $2k a year; market Q has 1,000 firms paying $20k. Both are $20M.
   - Under 40/45/15, P scores 85 before A6. Q scores between 40 and 62.5, depending on how fragmented 1,000 firms counts as. The money is the same.
   - If you do prefer P, name why (more places to turn if one avenue fails, stronger word of mouth, weaker buyers) and weight A4 for that reason (D6; N-B31).
3. **A zero weight switches a criterion off.** Under 40/45/15, a big, fragmented market where nobody feels the cost (A3) scores the same as one where everybody does. Cohen's warning is that these conditions are "a series of 'ands'" (R19).

*How to fill it in.* Each founder privately splits 100 points across A1-A7, and another 100 across W1-W6. Then we average the splits (R12). Any criterion can get a low weight. A zero means "this does not matter to us at all".

*What the "sensitivity case" is.* After scoring in S4, the ranking is recomputed with each founder's own split, and again with 40/45/15. If the same candidate comes out on top every time, the choice doesn't depend on the weights. If the top candidate changes, we look at why before choosing (S4, step 5).

**Process changes the research suggests.** Accept or reject each one here. After sign-off, apply them to §4, §5 and §10 with the old text struck through, and log them in §9. The founders' answers of 2026-09-14 are marked on each item:
1. **S0 step 1:** state the ambition as numbers (floor outcome, stretch outcome, horizon, funding), and derive K5 from the floor: fee-pool floor = floor ARR ÷ market share (D1). **Accepted 2026-09-14; applied as C1.**
2. **§10 naming:** rename the knob "Savings capture share" to "fee share of savings", and add a separate "market share" knob at 10/20/35% (check A). **Accepted; applied as C2.**
3. **K2:** add a word-of-mouth ceiling, "not too big" (R16, N-B17; D4). **Accepted; applied as C3.**
4. **W4:** score customers' proven spend on the problem, and weak, legacy or missing software for the job, rather than the number of competitors (D3b). **Parked until F-10 is investigated (S0.4, O-5).**
5. **W1:** add the channel rule. Direct selling needs a fee of about $5k or more a year per customer; below that, name a channel that scales (D2). *Parked 2026-09-14 with F-7: it depends on the fee per customer, which is not a sub-market decision.* **Confirmed parked.**
6. **A4:** define it as market structure per side plus reachable count, not raw count (D6). **Parked until F-9 is investigated (S0.4, O-4).**
7. **A6:** name the expansion axis (D5). **Accepted 2026-09-14 in the founders' words, vertical first, then horizontal; applied as C4.**
8. **§5 two-sided rule:** at sub-market level, score the per-side rows for both sides and carry both totals. The entry side is chosen in segment selection (Q6), following F-5. **Accepted: rank on the better side; applied as C5.**

**Founders' answers, 2026-09-14, fourth round** (verbatim):
> "1. Yes. 2. Yes. 3. Yes. 4. Park until F-10 is investigated. 5. Parked 6. Parked again 7. Vertical then horizontal. Veritcal then horizontal. Veritcal then horizontal. Again and again and again, ITS VERTICAL FIRST THEN HORIZONTAL. 8. Better side."
>
> "5 Year clock -> Product Launch"
>
> "Yes add a not too big check."
>
> "Durability should be its own investigation in itself, unrelated to scoring that is just a hard check of viability."

- **Process changes:** 1, 2, 3, 7 and 8 are accepted and applied as C1-C5 (change log at the end of §9). 4 and 6 are parked until F-10 and F-9 are investigated. 5 stays parked with F-7.
- **Expansion (F-12, change 7): vertical first, then horizontal.** This doc states the plan in that order everywhere.
- **F-2, decided:** the 5-year clock starts at product launch. ChartMogul's base rates start at first revenue (N-A01). With design partners paying from launch (F-3), the two starting points should be close **[our call]**.
- **F-11, decided:** keep the K5 floor, add the "not too big" check to K2 (C3), and keep 1-2 related backups (S6).
- **F-17, decided:** durability is its own investigation and a hard viability check, not a scored criterion. A7 leaves Axis A and becomes knock-out K11 once the investigation defines it (C6; S0.4, O-3).

**Founders' answers, 2026-09-14, fifth round** (a second session, working through S0.4). The answers were picks among options, plus one note in the founders' own words (verbatim):
> O-1: "Self-funded tilt (Suggested)". O-2: "Long-term rows (Suggested)". The doc's default weights: "Same rule as O-2 (Suggested)".
>
> O-3, what "durable" meant: "Customers survive downturns", "The cost persists in downturns", "Not shrinking long-term", "Our revenue won't swing", and "Swinging revenue happens, but we dont want drastic downturns. Markets happen to shrink but we dont want projections of shrinking."
>
> O-3, the K11 test: "Tests 1 + 3, flag 2 (Suggested)". O-4: "Top-50 + small-firm check (Suggested)". O-5: "Spend + weak software, veto (Suggested)". O-6: "Freeze after writing (Suggested)".

- **F-14 (O-1), decided:** W1 20, W2 5, W3 20, W4 15, W5 15, W6 25.
  - W2 drops from the default 15 to 5 because every candidate will score low on it until domain immersion (F-15). Its 10 points go to W6, which self-funding made more important (F-3).
- **F-13 (O-2), revisited:** A7's 15 points go to the two long-term rows, A5 (10 → 15) and A6 (5 → 15). Final split: A1 20, A2 10, A3 25, A4 15, A5 15, A6 15. The doc's default weights are fixed the same way: A7's 10 points go to A5 (+5) and A6 (+5) (C7).
  - Worked example shown to the founders (made-up candidates, desk scores 1 / 0.5 / 0). X is a big, painful saving that is mostly a one-time fix and stays in one sub-market (A1 1, A2 1, A3 1, A4 0.5, A5 0, A6 0). Y is half the size and pain, but recurs every shipment and carries to other sub-markets (A1 0.5, A2 1, A3 0.5, A4 0.5, A5 1, A6 1). With the final split, Y ranks first, 70 to 62.5. Spreading A7's points evenly (23/12/29/18/12/6) would have ranked X first, 73 to 65 **[our calc]**.
  - Check C notes that K11's Test 3 and A5 look related. They measure different things: A5 scores how often the saving recurs, Test 3 whether it holds up in a downturn. The UK scoring manual treats a pass/fail hurdle as compatible with scoring: the hurdle "usually guarantees preference independence" (N-B31). The founders kept the split.
- **F-17 (O-3), K11 defined** (C8; §5.1). The founders' note maps onto two tests **[our call]**:
  - "we dont want projections of shrinking" → **Test 1, no projected shrinking** (check C Option 1).
  - "we dont want drastic downturns" → **Test 3, no drastic fall in the unit a fee would be counted on** (check C Option 3). Its lines, 13% and 20%, are S&P's revenue bands (N-C01).
  - "Customers survive downturns" → **Test 2, recorded as a flag** on every card (S3 item 8), not a knock-out. As a knock-out it would remove about two-thirds of trucking employer firms (85,244 of 127,465 in NAICS 4841 plus 4842, 2023; N-C05), and the data disagree for brokers (FMCSA licences -17.6%, census firms up).
  - "Our revenue won't swing" → mostly fee design, deferred with F-7 and F-8. K11 tests only the market fact behind it, through Test 3.
  - The strict S&P revenue test (check C Option 4) becomes a comparison in S4 step 5, next to 40/45/15.
- **F-9 (O-4), decided:** top-50 zones plus a small-firm check (check D option C). K10 fails above 85%; 75-85% is unknown and settled at S3; A4 gets a small-firm bonus (C9; parked change 6 applied).
- **F-10 (O-5), decided:** W4 scores proven spend plus weak, legacy or missing software; the incumbent map is recorded on every fact sheet; the only veto is a dominant vendor (check D option D; C10; parked change 4 applied).
- **New rule, confirmed with the freeze (C11):** until the entry side is chosen (F-5), K10 and K11 remove a card only if both sides fail. If one side fails, the card goes forward with that side marked. This follows C5's "better side" rule.
- **O-6, S0 frozen 2026-09-14.** The default scales and rules are confirmed (S0 step 6). The frozen sheet is `research/selection_runs/run-01/0_criteria.md` (S0 step 7).

##### S0.4 Outstanding items (handoff, 2026-09-14)

~~The founders will settle these with another Claude Code session.~~ **All six were settled on 2026-09-14 in a second session (fifth round, S0.3), and S0 is frozen.** Each row says what to do, what it depends on, and which decisions already made it could change. The outcomes follow the table.

**Where S0 stands:**
- **Decided:** ~~F-1, F-2, F-3, F-11, F-12, F-15, F-16, F-17, and F-13 (which needs re-splitting, O-2).~~ All of F-1 to F-4 and F-9 to F-17, with F-13 revisited and K11 defined under F-17. F-4 follows from F-1.
- **Deferred to segment selection (Q6):** F-5, F-6, F-7, F-8.
- **Applied to the process:** ~~C1-C6~~ C1-C11 (change log at the end of §9).
- **Order:** ~~S1 (listing candidates) can start at any time. S2 (knock-outs) needs O-3 and O-4. S4 (scoring) needs O-1 and O-2.~~ Nothing blocks S1-S4 any more. Next is S1.

| # | To do | Kind | Depends on | Could change decisions already made |
|---|---|---|---|---|
| O-1 | Split 100 points across W1-W6 (F-14) | Founders' decision | — | Nothing decided so far. It completes the S0 balance check, since Axis W holds the criteria about us. Keep in mind: W2 will score low for every candidate for now (F-15); how W4 is scored is parked (O-5); W6 is where self-funding counts (F-3) |
| O-2 | Re-split Axis A now that A7 has left the score | Founders' decision | O-3 helps | F-13: the run-01 split now totals 85, with A7's 15 points unassigned. Options: re-split, or scale the six remaining rows up to 100. It also re-opens the balance check: without A7, A6 (5) is the only long-term row on Axis A. The 40/45/15 comparison is unaffected, since A7 was 0 there. The doc's default weights (§5.2) now total 90 and need the same fix |
| O-3 | Durability investigation (F-17), then define knock-out K11 | Research, then founders' decision | — | Which candidates survive S2. Freight is cyclical: Emergence rates transportation lower for "fragmentation and cyclicality" (R21); active brokers fell by 3,104 in 2024 (N-B04); the census growth from 2017 to 2022 includes the 2021-22 boom (R44). A strict threshold could remove whole families of candidates (brokerage or truckload, for example), leaving fewer that clear K5. It also feeds O-2 and the S7 revisit triggers (freight-rate cycle) |
| O-4 | Fragmentation measure (F-9): choose the formula and thresholds | Research, then founders' decision | — | K10's "land of the giants" test (top-50 share above 80%), the §10 fragmentation bands, and the zones in §8.2 all use today's defaults. A different measure or threshold could move industries between zones (refrigerated warehousing sits at 73.9%, near the line) and change which candidates pass K10. Parked change 6 (A4) is decided after this |
| O-5 | "Few incumbents" measure (F-10): a ballpark count of companies serving the space, and their market shares | Research, then founders' decision | O-4 (the same formulas may apply) | How W4 is scored (parked change 4) and S3 fact-sheet item 9. If the founders make it a hard cap, it becomes a knock-out and would remove candidates at S2. The evidence is split on whether few competitors is a good sign (D3b) |
| O-6 | Freeze S0 | Founders | O-1 to O-3, plus O-4 and O-5 where they feed knock-outs | Confirm the default scales and rules (S0 step 6). Date the sheet and copy the decided values to `research/selection_runs/run-01/0_criteria.md` (S0 step 7). Then S2 can run |
| — | Deferred to segment selection (Q6), not S0: entry side (F-5), firm-size floor (F-6), fee per customer (F-7), fee share of savings (F-8), and parked change 5 (W1 channel rule) | Later stage | Q5 | When decided, they could change the K5 floor's equivalent business counts (which assume a realistic fee), which side's score counts (C5 uses the better side until then), K10 (which applies to the side we sell to) and W1 |

**Outcomes (2026-09-14; details in S0.3, fifth round):**

| # | Outcome |
|---|---|
| O-1 | **Done.** W1 20, W2 5, W3 20, W4 15, W5 15, W6 25 (F-14) |
| O-2 | **Done.** A1 20, A2 10, A3 25, A4 15, A5 15, A6 15. The balance check passes (long-term rows 30, short-term 45). The doc's defaults are fixed the same way (C7) |
| O-3 | **Done** (check C). K11 = Test 1 (no projected shrinking) + Test 3 (no drastic fall in the unit a fee would be counted on). Test 2 (customer survival) is a flag; the strict S&P revenue test is an S4 comparison (C8). It removes specific jobs, such as per-load brokerage, not whole families |
| O-4 | **Done** (check D). Top-50 zones; K10 fails above 85%, and 75-85% is settled at S3 by small firms' share of revenue; A4 gets a small-firm bonus (C9). On 2022 data only couriers fail at S2; LTL goes to S3 as unknown |
| O-5 | **Done** (check D). Not a knock-out. W4 = proven spend + weak software; the incumbent map goes on every fact sheet; a dominant vendor with satisfied customers is a show-stopper at S4 (C10) |
| O-6 | **Done.** Scales and rules confirmed; the both-sides rule for K10 and K11 added (C11); sheet frozen at `research/selection_runs/run-01/0_criteria.md` |
| — | **Still deferred.** Added to the list: whether *our* revenue swings with freight volume, which depends on fee design (O-3) |

### S1: Enumerate candidates

**Purpose:** a long list of comparable candidates, so that the final pick is a real choice.

**Steps:**
1. **Build the three axes** (R05/R06):
   - *Who:* shipper groups. Draw them from the Commodity Flow Survey (CFS), which crosses shipper industry with commodity and transport mode (R32). Add the Freight Analysis Framework (FAF5), which unlike the CFS covers agricultural freight (R31). Add shipper size and technology habits; Flexport targeted "mid-market companies ... They use Google Analytics to track their website, and then they have to use a fax machine to do logistics" (R26).
   - *What:* shipping jobs, in the shipper's words rather than ours (R18). Starter list **[our call]**, drawn from R28's named pain points and R38's process-type issues:
     - buy capacity and rates;
     - tender, book and schedule;
     - track and report status;
     - handle documents and compliance;
     - audit, pay and reconcile freight bills;
     - manage detention, demurrage and extra charges;
     - claims and disputes.
   - *How:* freight-company type or method:
     - Armstrong & Associates' 3PL segments (R33): brokerage, intermodal, managed transportation, last mile, international forwarding and customs, value-added warehousing, dedicated contract carriage;
     - asset carriers by NAICS code (R44);
     - "in-house fleet" and "spreadsheet and phone".
2. **Cross the axes in a grid** (R02's product/market grid). Freight-company types are the rows and shipper groups the columns. Each cell is a candidate; empty cells show "unserved markets".
3. **Add candidates from outside the grid:**
   - Walk one shipment's chain, one hand-off at a time, and note where paper, payments or waiting charges pile up. R26's example: demurrage of "about $200 per pallet per day" while a paper bill of lading crossed the ocean.
   - Borrow investors' pain categories (R28): "procurement, first mile, drayage, customs clearance, and last mile"; data entry; invoice processing; manual booking.
   - Add some fringe candidates on purpose (R15).
4. **Write each candidate as a card** (§13): the standard sentence, the demand-side job, the supply-side method, and the four roles. Name the human end user on each side, as a role such as logistics coordinator or dispatcher. R16 asks for "actual human end users and not just general companies or departments in companies".
5. **Check each card against R02's five sub-market signs**, and merge near-duplicates.

**Output:** `1_candidates.md` with 20-40 cards. The count is **[our call]**; R15 asks only for "as long a list as possible". **Gate:** every card fits the sentence, and no two cards describe the same market.

**Why this way:**
- Abell's axes list candidates but do not choose between them: the framework "does not provide assistance to determine the appropriate scale or size of a business" (R06).
- Ulwick's quality tests keep the definition about the job rather than our product (R18).

**Freight notes:**
- The CFS does not cover farms (R32 note). Use FAF5 (R31) and USDA data (R34, R39) for freight that starts on a farm.
- "Customer Pickup" moves 11.4% of CFS tonnage (R32, *verified*). There the receiver, not the shipper, arranges transport and may be the buyer.

**Pitfalls:**
- Defining candidates by mode alone (R08: "several different products can be used in the same application").
- Defining them by the product we would build (R18).

### S2: Knock out

**Purpose:** remove candidates that fail a must-have, cheaply.

**Steps:**
1. Apply §5.1 to each card with a quick desk check: hours per card, not days **[our call]**.
2. Record one of three results:
   - **Pass.**
   - **Fail:** drop the card, with a one-line reason. Include their final 'score' for each of the matrices.
   - **Unknown:** carry the card forward with a flag, to be settled in S3. **[our call]**, so that fringe candidates are not killed early (R15).
3. A failed "one market" test (K2) means split the card and re-test it; do not drop it. Aulet: "continue to iterate on the market segmentation matrix until they are" (R16).
   - *Clarified 2026-09-15 (C12):* split at S2 only a card that mixes products or sales processes. A card that is one market but too big for word of mouth is flagged **S**, and its split variable is named. It is split into segments at segment selection (Q6), because the project targets segments.

**Output:** `2_knockouts.md`. **Gate:** roughly 8-15 survivors **[our call]**. Far more means the knock-outs are too loose. Far fewer means unknowns may have been treated as fails. *Run 01 (2026-09-15):* 34 survived. The founders kept the knock-outs as frozen, added a written desk rule for K5 (C13), and split S3 in two instead (C14).

**Why this way:** size, reachability and internal sameness each appear as must-haves in three or more sources (R10, R14, R16, R02). This is the strongest agreement in the method literature (synthesis A, §S2).

### S3: Desk evidence

**Purpose:** facts that separate the survivors, and a shortlist of 4-6.

*Changed 2026-09-15 (C14; the founders chose option C in `research/selection_runs/run-01/2_knockouts.md` §7).* In run 01, S2 passed 34 cards against a gate of 8-15, and 32 of them carry unknowns. S3 therefore runs in two steps:
- **S3a** settles the unknowns in a short pass.
- **S3b** builds full fact sheets only for the cards still standing.

#### S3a: settle the unknowns

**Input:** the S2 sheet, and its table of what would settle each unknown (`2_knockouts.md` §2 and §6).

**Steps:**
1. **Send cards with no unknowns straight to S3b.** In run 01 these are C-09 and C-15.
2. **Work in lean order.**
   - First take the cards whose unknowns lean toward failing: a central fee pool (20% of the savings range's midpoint) under the K5 floor, or a K11 unit already near or over 20%.
   - Then take the rest.
   - Spend hours per card, not days **[our call]**, as in S2.
3. **Find the missing input** named for each unknown, then re-apply the frozen test with it:
   - **K5:** use the desk rule in §5.1 (C13). Keep low-high ranges, but replace judgement shares with sourced ones wherever a source exists: a neutral rate, a filing, or a regulator's data.
   - **K11:** use the practice in §5.1 (C15). Name the unit, prefer physical counts, use the finest data, and never let one firm stand for an industry. Record the Test 2 customer-survival flag at the same time (S3b item 8).
   - **K4, K6, K7:** settle them with named data where it exists. Questions only customers can answer, such as whether they would credit software for a saving, stay open for S5.
4. **Record each unknown as one of three:**
   - settled pass;
   - settled fail, with the evidence;
   - still open, with the reason the desk cannot settle it.
5. **Apply the exit rules [our call]:**
   - **A card that fails a test is dropped.** Keep the same record as S2's dropped cards: the knock-out row and provisional Axis A and W scores (`2_knockouts.md` §5).
   - **A card still open on K11,** because no better series exists, goes on to S3b with its flag. S4's strict durability comparison (S4 step 5) shows whether the flag matters.
   - **A card still open on K5** whose central fee pool stays under the floor goes to a **reserve list**, not to S3b. It is not dropped: the founders can pull it into S3b at any time, and S5 is where its removable share could be measured.
   - **Every other card** goes to S3b.

**Output:** `3a_unknowns.md`. **Gate:** every unknown is either settled or has its reason for staying open written down, and both the S3b list and the reserve list are set. *Run 01 (2026-09-15):* gate met. Of 75 unknowns, 9 were settled pass, 2 settled fail and 64 stay open with reasons. C-21 and C-23 were dropped on K11 (import containers -21.9% in 2008-09). 18 cards go to S3b and 14 to the reserve list. Proposals P-11 to P-14 are recorded, not applied (`research/selection_runs/run-01/3a_unknowns.md`).

**Why this way:** it keeps S2's rule that unknowns go forward and are settled in S3, so fringe cards are not killed early (R15). It also spends the fact-sheet effort on the cards most likely to survive. Run 01's S2 showed that the desk cannot settle most size unknowns, because the share of a cost that software could remove is a judgement on nearly every card (`2_knockouts.md` §4.1).

#### S3b: fact sheets and the shortlist

**For each card on the S3b list, fill a one-page fact sheet** (§13):

1. **Buyer counts on each side.**
   - Firm counts for freight-company NAICS codes (R44).
   - Establishments by shipper industry (R32).
   - Freight flows (R31, R34).
2. **Savings pool, built bottom-up.** Avoidable cost per unit (per shipment, load, invoice or claim) × annual volume × the share software could remove **[our call]**.
   - Use order-of-magnitude estimates: Cohen uses power-of-ten figures from quick searches (R19), and Aulet's matrix sizes in "10s, 100s, 1Ks" (R15).
   - Cost anchors already in the notes:

     | Cost | Figure | Source |
     |---|---|---|
     | Truck detention | 135.9 million driver-hours a year | R38, *verified* |
     | Non-fuel trucking cost | $1.779 per mile | R38 |
     | Truckload profit margin | -2.3% | R38 |
     | Produce reefer rates, Q1 2026 | $1.50-$2.76 per mile, by distance band | R34, *verified* |
     | Demurrage | about $200 per pallet per day | R26, *assumed*: a founder's recollection from 2015 |
3. **Fee potential.** Buyers × a realistic yearly fee per buyer, where each buyer's fee is capped by that buyer's savings. This follows R42's "number of customers in ICP * ARPA" and R23's capture share. Model the ~~capture share~~ fee share of savings at 10%, 20% and 35% (§10; renamed 2026-09-14, C2). The result becomes the bubble size in S4.
4. **Structure of each side.**
   - Top-50 revenue share and HHI (R44), placed on Tidemark's fragmentation screen (R20).
   - Porter's five forces, especially buyer power and who keeps a saving once it is made (R43).
   - *Added 2026-09-14 (C9):* small firms' share of revenue from Census SUSB, for firms under 20 and under 500 employees (N-D04), and the top-4 share and HHI as a check for one dominant firm. Where a side includes owner-operators, add Nonemployer Statistics (N-D05). Use 6-digit codes where they exist. For a card that is unknown on K10 (top-50 share between 75% and 85%), settle it here: it fails if firms under 500 employees hold less than 20% of the side's revenue. *Run 01:* S2 ran this check in advance for every such side (`2_knockouts.md` §4.2), so S3b only records the result.
5. **Software penetration and why now.**
   - How much work still runs on paper, phone and spreadsheets. R27: "more than 60% of the freight brokerage market operates without software". R28: "50% of the largest enterprise shippers in the U.S. still rely on some combination of email and spreadsheets".
   - Sector digital intensity: OECD rates "Transportation and storage" and agriculture "Low" in both periods (R45).
   - Whether the existing systems of record have APIs, Bushel's "plumbing" (R30).
   - A named trigger for change now (R28's drivers).
6. **Addressable work.**
   - Which roles do the costly work, and is it text- or number-heavy office work (R22)?
   - Is it work where "human connection isn't a key benefit", and not "delivering on a core product" (R23)?
7. **Budget holder and implementation.** Who holds the budget? Can the product "demonstrate value on day one" and go live "in weeks, not months" (R28)?
8. **Cyclicality and growth.** Emergence's cyclicality factor (R21); changes in the census data from 2017 to 2022 (R44); rate swings (R34).
   - *Added 2026-09-14 (C8):* settle any K11 unknowns (Test 3's 13-20% band, or missing data). *From 2026-09-15 (C14):* S3a does this before the fact sheets are written; S3b records the result. Record the Test 2 customer-survival flag for each side: the firm death rate against the economy's in Census BDS 2009 and 2023, the entry rate against the exit rate, and the firm count. Entries that replace exits are Constellation's acceptable kind of churn (check C, C5).
9. **Competitors and substitutes,** including "the 'do nothing' option" (R15) and Porter's substitutes (R43).
   - *Added 2026-09-14 (C10):* the incumbent map, as W4's evidence. Record the number of named software vendors for the job, the largest vendor's share if known, the service firms that do the job (3PLs, auditors, factoring firms), TMS or telematics features that cover it, and how the job is done today. Tag each figure *verified* or *assumed* (check D, D5).
   - *Added 2026-09-16 (C20, from P-21):* **single-point dependencies.** Name any party that is not a competitor but can withdraw the data, licence or access the product needs, and say what happens if it does. W4 scores competitors, not dependencies. Run 01 found one on three of five shortlisted cards: NMFTA's class licence (C-11), FMCSA's frozen authority dataset and the move to Motus (C-08), and retailer portals with no open API (C-19).
10. *Added 2026-09-15 (C15):* **The unit a fee would be counted on,** and the series or proxy used for K11 Test 3, with its fall in both downturns. Where a proxy stands in for the unit, say why it is the closest one.
11. *Added 2026-09-15 (C12, C15):* **Segments.**
   - For a card flagged S at S2, name its split variable and its likely segments. The project targets segments, so this is the first cut for segment selection (§11).
   - Also list the sides and segments that K10 and K11 have already ruled out (`2_knockouts.md` §8, P-8).

**Then:** give each ~~survivor~~ card on the S3b list a provisional desk score (S4 method, 1/0.5/0 scale) and keep the top 4-6. *Added 2026-09-15:* use the row rules in `2_knockouts.md` §5, so that these scores compare with the ones recorded for dropped cards. Aulet: "Four to 10 ... usually 4 to 6 is a good range" (R15).
- *Added 2026-09-15 (C16):* **how the cut is made.**
  - Rank the cards by the sum of the two axes (A + W, out of 200).
  - Keep the cards above the first clear break inside 4-6.
  - Break ties on the central fee pool.
  - Record how the order moves under other readings, and under the founders' first 40/45/15 split.
  - S4 still keeps the two axes separate and plots them.
- *Added 2026-09-15 (C18):* **score the job, flag the wedge.** Score each card's job as its sentence defines it. Where the first product would change W3 or W6 (for example, audit-first against audit-and-pay), record the effect as a sensitivity. The wedge is chosen at S6.

**Output (S3b):** `3_factsheets.md`, `3_shortlist.md`. **Gate:** 4-6 candidates on the shortlist, each with a savings-pool estimate and its assumptions written down. *Run 01 (2026-09-15):* gate met. There are 18 fact sheets, and the founders confirmed a shortlist of five: C-08, C-09, C-20, C-11, C-19 (`research/selection_runs/run-01/3_factsheets.md`, `3_shortlist.md`).

**Pitfalls:**
- Sizing by freight spend or shipment value. CFS "value" is the value of the goods, not the shipping cost (R32 note).
- Reading Armstrong & Associates' gross revenue as a software budget. It includes the freight charges passed through to carriers (R33 note).
- Forgetting that owner-operators without payroll are missing from the census tables (R44).
- *Added 2026-09-15 (run 01 S2):* resting a size figure on a share that is only our judgement. In S2 the removable share was a judgement on nearly every card, which is why K5 settled so little. Label such a share, and replace it with a sourced one wherever one exists.
- Letting one firm's volumes stand for an industry. In 2022-25, single brokers' load counts ranged from growth to -48% (`research/s2_check_H_downturns_freight.md`, H3).

### S4: Score

**Purpose:** a ranked, auditable comparison of the shortlist.

**Steps:**
1. **Score Axis A (worth winning) and Axis W (can we win)** with §5.2 and §5.3, using the S0 weights.
   - Score 1 / 0.5 / 0 per criterion at the desk stage (R12).
   - Give every score an evidence link and a *verified* or *assumed* tag.
   - Score Axis W against whatever the customer uses today: a broker, a spreadsheet, or an incumbent TMS. R12 scores strength "relative to the dominant player(s)", but a pre-revenue team has no position to compare (R12 note).
   - *Added 2026-09-15 (C18):* score each card's job as its sentence defines it. Record the effect of the first product (the wedge) on W3 and W6 as a sensitivity. The wedge is chosen at S6.
   - *Added 2026-09-15 (C17):* at desk level, A3 = 1 needs a dated rule, rule change or crisis that acts on the card's own job (§5.2).
2. **Score fee feasibility** with §5.4: the four CAMP questions (R25), payer-saver alignment, and position in the payment flow (R41).
3. **Run the checks** in §5.5:
   - the show-stopper veto (R16);
   - Cohen's multiplicative score for each paying side (R19);
   - for candidates that match buyers with sellers, Gurley's 10-factor count (R41).
4. **Plot the result.** Axis A on the y-axis and Axis W on the x-axis, both 0-100. Bubble size is fee potential, and the marker shows whether the candidate passes fee feasibility (R12, R14).
5. **Check sensitivity.** Recompute the ranking with each team member's own S0 weights. If the top candidate changes, the evidence is too thin to rank: send the top 3 to S5 unranked **[our call]** (synthesis A, T7). Run 01 also recomputes with the founders' first split (40/45/15: A1 40, A4 45, A6 15) and applies the strict durability test (S&P-style revenue cyclicality: an average revenue fall of 8% or less passes, over 13% fails; check C Option 4) to show which candidates it would have removed (C8).
6. **Write the key deciding factors** under the table (R16).
7. **Per-customer profit and kill condition** (*added 2026-09-22, C22*). For every card going to S5, build the per-customer chain from the fact sheet's fee unit and savings pool (fee = unit volume × leak rate × share removed × share realised × fee share; gross profit = fee − cost to serve), source and label every input, and compute the break-even customer size, the leak rate needed to cover variable cost, both with the cheapest allowed review labour, and the customer size at which the fee reaches check A's $5k-a-year direct-selling benchmark. Then write a **kill condition**: a measurement S5's savings assessment or data-access test will make, with three bands (kill / conditional, condition named / pass), fixed before the assessment runs and moved afterwards only through §9. Enter it in the S5 gate tracker. A card with no kill condition does not go to S5. Template and worked example: `research/selection_runs/run-01/4_kill_conditions.md` §1-§2. *Changed 2026-09-22 (C23):* **a card is eliminated at this step only if it fails the per-customer test even with every unmeasured input at its most favourable value** (the ceiling test). Otherwise it goes on, and its kill condition names the input and the line.
   *Note, 2026-10-08 (D-23, not a process change):* the founders decided the company employs no analysts and does no manual review ("We have no analysts, this is a software company … we do no manual reviews here"; `software-initial-pitch.md` §1A), and that this applies to every card. So no card's model may include **our own** review labour, and "the cheapest allowed review labour" above no longer has a meaning for us. The C-09 re-run (`handoff_c09_software_rerun.md` §4) will propose an adapted template as **P-31**; until the founders adopt it, this step stands as written and no §9 entry is made.

**Output:** `4_scorecard.md`, with the plot, and `4_kill_conditions.md` (step 7). **Gate:** the ranking holds, or the top 3 go forward together. *Run 01 (2026-09-16):* gate met in part. The five were scored, and the ranking holds against the weights under six of seven splits. It does not hold against the checks: the top card, C-08, fails fee feasibility (F1-F4 = 1.0 against a floor of 2, because its saving is risk avoided), scores 0.04 on Cohen's scale and fails the strict durability test, so it cannot be the S6 primary while the fee rule stands. Four of the five score an identical raw 3.5 of 6 on Axis W, so that axis does not separate them. The file's reading is the gate's second branch: the desk cannot rank them, so they go to S5 together. One row was changed (C-09's W3, applying C18) and proposals P-18 to P-22 are recorded, not applied. The founders decided on 2026-09-16 to demote C-08 while keeping the fee rule, to accept the C-09 correction, and to send **four cards to S5 unranked: C-09, C-11, C-19 and C-20** (`research/selection_runs/run-01/4_scorecard.md` §9.1). They also adopted P-18 and P-21 and set S5's coverage by side type, applied as C19-C21. **C19 forces a re-score of this run:** C-08's A4 goes 1 → 0.5 and its Axis A 100 → 92.5, because its 1 came from the side being vetted rather than the side that pays; no other card moves (§9.4 of that file). *2026-09-22:* step 7 was added after this run's S4 had closed (C22) and applied to the four finalists before the first interview: C-09's kill condition is in `research/selection_runs/run-01/4_kill_conditions.md` §2; C-11, C-19 and C-20 are assigned to a separate chat (`handoff.md`). That chat filled them the same day (§3-§5 of the same file). The founders decided the same day (D-22, §7.4 of that file): **C-11 and C-20 are eliminated**, C-19's lines are adopted, and the focus is C-09 and C-19. C-11 fails even with every unmeasured input at its best; C-20 was viable on paper, but its saving is paid staff time.

**Reading the plot** (R14's worked example, *verified*):
- Drop candidates that are low on both axes, even large ones.
- A candidate that is very attractive to us but not keen on us is "unlikely" to be won now.
- The best match may be small. If so, keep a second, compatible candidate too.

### S4.5: Profitability check

*Added 2026-09-22 (C25), in the founders' words:*

> "I want to add an S4.5 Profitability check, which is a test if any of our sub-markets can be proven profitable before we do customer reviews. This relies on auditing web information relevant to what we've checked out.
>
> This will be a similar process to what we've just done for C-09. Though we want to find any and all web information we can to see if we can iron this out without customer interviews."

**Purpose:** before any customer interview, find out whether a card can be **proven profitable, or proven unprofitable, from public evidence alone**. S4 step 7 builds the per-customer model on the desk evidence already held and fixes the kill lines. S4.5 then audits everything else the web holds on the inputs that decide that model.

**Input:** the card's per-customer model and kill condition (S4 step 7), its fact sheet, and its checks.

**Steps:**
1. **Name the deciding inputs.** From the step-7 model, list the inputs whose plausible range crosses break-even, the $5k-a-year line or check A's 12-month payback. Only these need the audit.
2. **Audit the web for each deciding input**, in this order:
   - (a) **real transaction documents:** court and bankruptcy exhibits, lender and receivables-finance records, filings with line items;
   - (b) **neutral studies:** regulators, government data, university research with company data, associations read at the source;
   - (c) **the market's own economics:** what incumbents earn and spend per customer, and what that implies;
   - (d) **vendor claims**, kept apart.

   Label every figure and re-check the load-bearing ones at the source.
3. **Run a desk look-back on any real transaction-level data found**, as the C-09 practice audit did on 101 court-filed invoices (`research/s5_practice_audit_public_invoices.md`).
4. **Re-run the step-7 model and the market test** on the audited ranges at three points: central, the least favourable end, and the most favourable end that neutral or *verified* evidence supports.
5. **Give the verdict** against this bar, fixed before the audit (**[our call]**, default until the founders change it; §10):
   - **Proven profitable (from the web):** using only *verified* or neutral inputs, three things hold:
     - a customer in the card's segment gives positive gross profit;
     - that customer repays a $5-15k acquisition cost within 12 months (check A, §A3);
     - enough such customers exist for $1M of revenue at a 10% share and $2.5M at no more than 35%.
   - **Proven unprofitable:** the card fails even at the most favourable end that neutral or *verified* evidence supports (the C23 ceiling test on the audited ranges). Propose elimination.
   - **Not provable from the web:** anything else. Name each input still open and the document that would settle it, and confirm that the S5 kill condition measures it.

**Frozen lines do not move here.** S4.5 changes no kill condition. If the audit argues for a different line, that goes through §9.

**Output:** `research/selection_runs/<run>/4_5_profitability.md`, one section per card, plus its check files. **Gate:** a card proven unprofitable does not go to S5 unless the founders decide otherwise. From run 02 on, every card going to S5 carries an S4.5 verdict.

*Run 01 (2026-09-22):* applied first to C-19, in the chat that ran S4 step 7 for C-11, C-19 and C-20. C-09 is not run for now, in the founders' words: "Conduct this on C-19, since it seems like the estimates necessary for C-09 are unlikely."

### S5: Validate with primary evidence

**Purpose:** confirm or kill the top candidates' problems, costs and payers with real people before committing.

*Added 2026-09-22 (C26):* **where S4.5 found the recoverable rate concentrated in a minority of customers, screen every recruit for that minority's marker, run the savings assessment on one that has it, and record the screen yield and the new-money share.**

**Scope:** the top 3-4 from S4 **[our call]**. Cover both sides of each, starting with the harder side (R15).
- *Changed 2026-09-16 (C21, from D-12):* **how deeply each side is covered depends on what that side is.**
  - **A side that could buy from us** gets the full treatment in step 1.
  - **A counterparty-only side** — one that sets the rules or holds the evidence and that we would never sell to, such as a concentrated retailer, an LTL carrier or a regulator — is covered instead by its **documented position** (published rules, tariffs, dockets, supplier manuals, dispute windows) plus 1-2 interviews with people who work against it daily: a broker or 3PL representative, a contingency recovery firm, a former analyst.
  - Say on each card which of the two every side is, and why. Asking a pre-revenue team to run five discovery calls with a top-4 retailer sets a gate that cannot be met and that tells us nothing about the card when it is missed.
  - *Run 01:* C-09's carriers and C-20's importers could buy from us; C-11's LTL carriers and C-19's big-box retailers are counterparty-only.

**Steps:**
1. **Recruit** 5 interviewees per side per candidate ~~on both sides~~ *on every side that could buy from us (C21); a counterparty-only side takes 1-2*. The default is **[our call]**; Aulet says "at least a few weeks", and his company SensAble spent "over three months" (R15).
   - Channels: associations, co-ops, load-board communities, trade events.
   - How easily people are recruited is itself evidence for reachability (W1).
2. **Interview rules:**
   - Ask about their work and about specific past events, never about our idea (R35). The three Mom Test rules (talk about their life, ask about specifics in the past, talk less) come from summaries of the book (*assumed*).
   - Map the job: its steps, and the "other products they use immediately before, while, and immediately after" (R18).
   - Stay in "inquiry mode", not "advocacy mode" (R15).
   - Get numbers: the last incident of the target cost, what it cost, how often it happens, and who paid.
   - Count commitments as evidence: sharing real invoices or data exports, an introduction to a colleague, a pilot (R35; *assumed*, from summaries).
3. **Run a lightweight savings assessment** on real data with at least one willing customer per finalist **[our call]**.
   - Bessemer's advice: lead with "risk-free POCs or lightweight cost savings assessments that prove their value upfront" (R28).
   - Examples: re-audit one month of a shipper's freight invoices, or one month of a carrier's detention records.
   - It tests the problem, the size of the saving, and CAMP's measurability and attribution, all on real data (synthesis B, S5).
4. **Test willingness to pay early.** Euclid: "Even monetization at this stage is discovery—a dynamic test of willingness to pay" (R24). Put a price on the assessment or the pilot.
5. **Use a light survey where a side is too large to interview.** ATRI's method (R38):
   - a bounded list of issues;
   - each respondent picks a top three, scored 3/2/1;
   - results are split by actor type.

   The split is what reveals where a problem lives: owner-operators rank "Broker Issues" first, while carrier executives rank it tenth (R38, *verified*).
6. **Log every hypothesis** as Hypothesis / Validated / Finding / Next step, the format Aulet uses in his Bloom example (R15).
7. **Re-score S4 on a 1-10 scale** (R14), this time with evidence links.

**Gate, per finalist** (defaults **[our call]**):
- ~~at least 5 interviews on each side~~ *changed 2026-09-16 (C21):* at least 5 interviews on each side that could buy from us, and for a counterparty-only side its documented position plus at least 1 interview with someone who works against it daily;
- at least 3 people on the paying side describe a specific, recent incident with a cost attached;
- at least 2 commitments on the paying side;
- a named data source that would measure the saving, and at least one interviewee willing to share it;
- a savings assessment on real data for at least one customer (step 3), or a written reason why it could not be done.

**Why:**
- P7 (talking to customers decides).
- Moore: pragmatist buyers want proof "in use cases that they themselves have and with customers they know and can reference" (R17, *verified*).

**Reading before interviewing:**
- ATRI 2025 for the carrier side (R38).
- The 2026 3PL Study for shippers and 3PLs (R37). It sits behind a registration form, so whether to register is the user's decision.

**Scope note:** this is a light round. Deep discovery inside the chosen sub-market belongs to the segment stage (Q6):
- Where to Play calls itself "the front-end of Customer Development" (R40, via Blank).
- Euclid's funnel narrows from "talk to everyone" to a defined ideal customer only after the beachhead is chosen (R24).

**Output:** `5_validation.md` (the stage record: side types, hypotheses, plan, re-score rules, gate tracker), `5_interview_kit.md` (guides, messages, assessment protocols, prices, survey) and `5_log.md` (the evidence). **Gate:** the per-finalist thresholds above.

*Run 01 (opened 2026-09-16):* the desk half is done; the primary half has not started.
- **Checks:**
  - **T:** the LTL carriers' documented position for C-11 (`research/s5_check_T_ltl_carrier_position.md`);
  - **U:** the big-box retailers' documented position for C-19, plus C-19's buyer count and a current reading of the 2018 tool gap (`research/s5_check_U_retailer_position.md`);
  - **V:** a recruiting map for every side (`research/s5_check_V_recruiting_channels.md`).
- **Desk findings that change what the interviews test:**
  - C-11's carriers accept the shipper's own pre-pickup paperwork as proof, not later measurements, and no neutral correction rate exists. FedEx Freight's filing bounds dimensioner re-rating at about 0.8% of revenue.
  - C-19's buyer count is about 15,000-55,000 (central about 29,000), anchored on Walmart's 31,196 published suppliers. The share of small suppliers using no deduction tool fell from 70% (2018) to 55% (2023, *assumed*).
- **Nothing is re-scored at the desk.** The gate is not met.
- **Proposals and decisions:** P-23 to P-26 (one interview for two shipper cards; early stop; 1-10 anchors fixed before interviews; counterparty sides off the per-side rows) are proposed, not applied. D-14 to D-20 await the founders (`5_validation.md` §10).

### S6: Choose

**Steps:**
1. **Pick the primary:** the best-placed candidate on both axes after S5 that also passes the fee gate. Check it against:
   - Moore's rule, "big enough to matter, small enough to lead" (R17; the phrase is confirmed only in podcast show notes);
   - Aulet's three conditions, which must still hold (R16).
2. **Pick 1-2 backups and 1-2 growth options.** Each should share the software core, the data sources, or one side of the market with the primary.
   - Where to Play: a "smart portfolio of backup and growth options". Its data show that the successful broad entrants' options "tend to be closely related" (R40).
   - Euclid's three axes help find them: new products for the same customers; the same product for adjacent sub-verticals; extension to customers' partners along the value chain (R24).
3. **Write the wedge hypothesis:**
   - what customers will adopt immediately, what we can build quickly, and why it can grow into a large business (R24);
   - prefer automation or optimisation "as a wedge to provide immediate ROI" (R28);
   - a supporting workflow meets less resistance but more competition from horizontal tools. R22 names "freight procurement for a shipper" as one.
4. **Decide the entry point.** Where a hub exists, equip it rather than cut it out:
   - Silo chose produce distributors, who are "responsible for connecting growers, grocers, restaurants, and even other distributors" (R29).
   - Bushel: "the middle of the supply chain ... is the most underserved" (R30).
5. **Park everything else explicitly.** "Say 'no' to all other options" (R40).
6. **Team sign-off,** with the key deciding factors written down (R16).

**Output:** `6_decision.md`.

### S7: Record and revisit

**Steps:**
1. **Record the decision** under "Answers / Decisions" in CLAUDE.md, with how it was made and links to the evidence.
2. **Write revisit triggers** that are measurable and dated **[our call]**, following Aulet's "Pursue it until it proves not to work or is much less attractive than originally anticipated" (R16). Defaults:
   - The saving cannot be measured for the first N customers.
   - Fewer than X of Y target customers will share baseline data.
   - A backup's re-score beats the primary's by 10 or more points on either axis.
   - An outside change moves a scored input: a regulation, the freight-rate cycle, or a well-funded entrant. Re-score the affected rows. Porter: "Industry structure is dynamic" (R43). R12 projects each candidate three years ahead. *Added 2026-09-14:* check C §3 lists candidate series for the freight-rate cycle (the truckload, LTL and broker producer price indexes, Cass shipments, the annual Census BDS release, FMCSA authority counts). Driverless trucking at scale on a card's lanes re-opens K11 Test 1 (N-C25). Which of these become dated triggers is decided in S7.
   - A new edition of a data source used in scoring (synthesis B, S7):

     | Source | Refresh cycle |
     |---|---|
     | Economic Census, CFS | every five years (2022 is the latest) |
     | FAF | new versions |
     | Food Dollar | every March |
     | AgRTQ | quarterly |
     | ATRI | every October |

   - A shift in pricing norms. In customer service, outcome pricing went "from unusual to the market standard" between 2023 and 2024 (R25).
   - A scheduled review at 6 and 12 months, whatever happens (R40: "Make it a habit").
3. **When a trigger fires, go back to S4** with the new evidence, not to S1. Restart at S1 only if the whole shortlist fails.
4. **Strike through superseded answers** instead of deleting them (CLAUDE.md).

---

## 5. The scorecard

**Two-sided scoring rule [our call]:**
- Rows marked "(per side)" are scored twice: once for the shipper side and once for the freight-company side.
- ~~The axis total uses the **entry side**, the side we would sell to first. Record the other side's score next to it.~~ *Changed 2026-09-14 (C5):* the axis total uses the **better side**, whichever side scores higher. Record the other side's total next to it. The entry side itself is chosen in segment selection (Q6; S0.3 F-5).
- *Added 2026-09-16 (C19, from P-18):* **A4 is an exception to the better-side rule.** It is scored on the side that would pay, because A4 measures fragmented buyers with weak buying power, and a fragmented side that never pays us says nothing about the prize. Every other per-side row keeps the better-side rule.
- A candidate whose other side refuses to take part fails in practice, however strong its total.
- *Added 2026-09-14 (C11):* until the entry side is chosen, the side-specific knock-outs K10 and K11 remove a card only if both sides fail. If one side fails, the card goes forward with that side marked as ruled out.
  - *Flagged for review 2026-09-15 (T15):* in run 01 this made K10 and K11 Test 1 pass-throughs. No card failed either test, because every card has a trucking, brokerage or warehousing side that passes.
  - The founders may reconsider how these tests work.
- Sources: R15 ("complete each step ... once for each side of the market"); synthesis A §3; synthesis B §5, which calls the link between the sides "coupling": who pays whom, where the money flows, and who feels the pain.

### 5.1 Knock-outs (each is pass, fail or unknown)

| # | Test | Passes when | Sources |
|---|---|---|---|
| K1 | Distinct and internally alike | Members share needs, and the candidate clearly differs from its neighbours | R10 "differentiable"; R14 "homogeneity", "distinctness"; R02 five signs |
| K2 | One market on each side, and not too big | Same product, same sales process, and word of mouth, tested separately on the shipper side and the freight-company side. *Added 2026-09-14 (C3):* not so big that its buyers stop talking to each other. Aulet asks whether it is "reasonable in size for us to achieve meaningful word of mouth, meaning it is not too big". A fail means split the card. *Clarified 2026-09-15 (C12):* at sub-market level, split at S2 only a card that mixes products or sales processes. A card that is one market on each side but too big for word of mouth is flagged **S**: its split variable is named, and it is split into segments at segment selection (Q6), because the project targets segments | R16; N-B17; N-B16 |
| K3 | Identifiable and reachable | We can name the buyers and reach them "at an affordable cost" | R10 "accessible"; R14 "identifiability", "reachability" |
| K4 | Measurable | Buyer counts and the savings pool can be estimated from named data | R10 "measurable" |
| K5 | Big enough | Fee potential clears the S0 floor. Measure fee potential, not headcount: freight populations are small, with "more than 17,000 freight brokers in the U.S." (R27).<br>*Desk rule added 2026-09-15 (C13):* take the savings pool as a low-high range.<br>• Pass if a 10% fee share of the low end reaches the floor.<br>• Fail if a 35% share of the high end is clearly short of it.<br>• Unknown in between.<br>A generous case within a few percent of the floor counts as "about" the floor, so it is unknown, leaning fail. A central case (20% of the range's midpoint) sets the order of S3a's work but never fails a card by itself | R10 "substantial"; R16 size band; R19; R42; `2_knockouts.md` §3 |
| K6 | Software can fix it | The target cost comes from information, coordination or paperwork, not from trucks, fuel or roads | CLAUDE.md; R22 (text- and number-heavy work automates, manual labour does not); R23 role screen |
| K7 | Saving measurable and attributable | There is a countable outcome and a baseline, and customers would credit software for it (the M and A of CAMP) | CLAUDE.md; R25 |
| K8 | Someone can and will pay | A party in the pair holds a budget, sees the saving on its own P&L, and could buy from a startup. Cohen's "0: They cannot buy from you" is a fail | R15/R16 "well-funded"; R19; R28 budget and "turning opex budget into IT budget" |
| K9 | Team would commit | The candidate passes the S0 personal filter | R15 |
| K10 | Not in the "land of the giants" (applies only if S0 chose selling to small and mid-sized firms) | ~~The side we sell to is not concentrated: the top 50 firms hold 80% of revenue or less (R21's threshold).~~ *Changed 2026-09-14 (C9):* the side is not concentrated. Pass if the top 50 firms hold 75% of revenue or less; fail above 85%. Between 75% and 85% is unknown, settled at S3: fail if firms under 500 employees hold less than 20% of the side's revenue (Census SUSB, N-D04). Use 6-digit codes where they exist. Until the entry side is chosen, a card fails only if both sides fail (C11). In the concentrated corner "you are an enterprise solution, or your company will fail" (R20). ~~On 2022 census data this fails LTL (82.9%) and couriers (90.9%) (R44)~~ On 2022 data couriers (90.9%) fail at S2; LTL (82.9%) is unknown at S2 and fails at S3, since firms under 500 employees hold 17.5% of its receipts (R44; check D).<br>*Flagged for review 2026-09-15 (T15):* in run 01, K10 removed no card, because every card has a side that passes and C11 needs both sides to fail. At sub-market level it only rules out sides and segments. The founders may reconsider how it works | R20; R21; R41; R44; N-D01; N-D04 |
| K11 | Durable (*added 2026-09-14, C6; ~~the test is still to be defined~~ defined 2026-09-14, C8*) | ~~Pending the durability investigation (S0.4, O-3). A pass/fail check of viability, expected to cover what A7 used to score (growth, cyclicality, stable structure). The investigation sets the measures and thresholds~~ Both tests must pass. Unknowns go forward, and until the entry side is chosen a card fails only if both sides fail (C11). **Test 1, no projected shrinking:** pass if the side's BLS 10-year employment or output projection is 0 or higher, its census firm count in 2022 is at least its 2017 count (R44), and no primary source shows a substitute doing the job at scale within 5 years of launch; fail if two of the three point to decline. **Test 3, no drastic fall in the unit a fee would be counted on** (invoices, loads, customs entries, claims, detained stops): pass if the unit fell 13% or less from peak to trough in each measured downturn (2008-09 and 2022-25), or rose; fail if it fell more than 20% in either; 13-20%, or no data, is unknown. The 13% and 20% lines are S&P's revenue bands (N-C01). **Not a knock-out:** Test 2, customer survival, is recorded as a flag in S3 item 8.<br>*Flagged for review 2026-09-15 (T15):* in run 01, Test 1 removed no card, for the same reason as K10.<br>*Practice added 2026-09-15 (C15):*<br>• Name the unit a fee would be counted on.<br>• Use a proxy only when no count exists, prefer physical measures to dollars, and name the proxy.<br>• Where monthly and annual data fall on different sides of a band line, the finer data decides.<br>• One firm's volumes never stand for an industry.<br>• Where parts of a card fall in different bands, the card-level unit decides, and the failing segments go to segment selection | R21 cyclicality; R44; N-B03; N-B04; N-C01; N-C05; N-C11; check C; `2_knockouts.md` §3 |

### 5.2 Axis A: worth winning

Default weights total 100. The team re-sets them in S0. Run 01 uses the founders' split recorded in §4 S0.3 (F-13): A1 20, A2 10, A3 25, A4 15, A5 15, A6 15. ~~Since A7 left the score (C6), the remaining defaults total 90 and the run-01 split totals 85. Both are to be fixed (S0.4, O-2).~~ *Fixed 2026-09-14 (C7):* A7's points went to the long-term rows A5 and A6, in the defaults and in the run-01 split.

| # | Criterion | What to look at | Weight | Sources |
|---|---|---|---|---|
| A1 | Savings pool and fee potential | Avoidable cost × volume × the share software can remove; fee per buyer × number of buyers | 25 | CLAUDE.md; R23; R25; R33; R42 |
| A2 | Fit for automation | The costly work is text- or number-heavy office work that is "not being done or being done poorly"; labour spend far exceeds software spend | 15 | R22; R23; R28 |
| A3 | Pain and urgency (per side) | A top-three priority; customers know about it and care; a forcing event such as a regulation or a crisis. *Clarified 2026-09-15 (C17):* at the desk, 1 needs a dated rule, rule change or crisis that acts on the card's own job. Triggers that act on the whole freight market or on a neighbouring job, or that are still pending, score 0.5 | 15 | R15 "Urgency of Need"; R17 compelling reason to buy; R19 Self-Aware; R21 regulatory change, dissatisfaction with incumbents |
| A4 | Fragmentation ~~and number of buyers~~ (per side) | ~~Many buyers with weak buying power; fragmented buyers and fragmented sellers~~ *Changed 2026-09-14 (C9, parked change 6):* market structure per side. Top-50 share under 20% = 1, 20-80% = 0.5, over 80% = 0. Add 0.5, capped at 1, if firms under 20 employees hold 25% or more of the side's revenue (Census SUSB). The number of buyers is not scored here, because A1 and K5 already contain it (check B, B5). *Changed 2026-09-16 (C19, from P-18):* A4 is scored on **the side that would pay**, not the better side (C5). Until the entry side is chosen (Q6), use the side the card's own fact sheet names as the budget holder (S3b item 7), and record the other side's score beside it | 10 | R20; R41; R44; R43; N-D01; N-D04 |
| A5 | Frequency and recurrence | The saving recurs with every shipment or week, so the fee recurs too | ~~10~~ 15 | R41 frequency; R19 Enduring; R28 "sticky long-term value" |
| A6 | Expansion leverage | ~~Adjacent sub-markets reachable with the same core; extension along the value chain; data that builds up over time~~ *Changed 2026-09-14 (C4):* **vertical first, then horizontal.** After a highly specific focus on one segment's use cases (vertical), how far the same core could reach across other segments and sub-markets (horizontal). Extension along the value chain, and data that builds up over time, count as supporting evidence | ~~15~~ 20 | R16 leverage; R17 "bowling alley" (via R15); R24 expansion axes; R42; R21 "Value in Data"; N-B16; N-B20 |
| ~~A7~~ | ~~Durability~~ | ~~Growth, low cyclicality, stable structure~~ *Moved out of scoring 2026-09-14 (C6; S0.3 F-17):* durability becomes hard check K11, defined by its own investigation (S0.4, O-3) | ~~10~~ | R12 long-term criteria; R21 cyclicality; R44 growth 2017→2022 |

**Why these weights [our call]:**
- A1 is the heaviest because the fee rule makes the savings pool the business model.
- A2 and A3 decide whether software can reach the pool and whether anyone is motivated to act.
- A6 carries "the TAM you exit with" (R42).
- The set follows R12's balance rule: short-term criteria (A1, A3) are matched by long-term ones (A6, A7). *A7 left the score on 2026-09-14 (C6). Re-check the balance when the weights are re-split (S0.4, O-2).* *Re-checked 2026-09-14 (C7):* A5 now counts as a long-term row, because its sources are Cohen's "Enduring" (R19) and Bessemer's "sticky long-term value" (R28) **[our call]**. With A5 at 15 and A6 at 20 against A1 at 25 and A3 at 15, the defaults pass.

### 5.3 Axis W: can we win

Default weights total 100. Run 01 uses the founders' split recorded in §4 S0.3 (F-14): W1 20, W2 5, W3 20, W4 15, W5 15, W6 25.

| # | Criterion | What to look at | Weight | Sources |
|---|---|---|---|---|
| W1 | Access and cost to reach (per side) | Sales channels; points where buyers gather (hubs, associations, co-ops, load boards, TMS marketplaces); word of mouth | 20 | R16; R10; R21 (concentration lowers acquisition cost and aids word of mouth); R29 hub; R30 acquisition cost |
| W2 | Team knowledge and access | Insider knowledge, contacts, ability to watch the work | 15 | R36; R15; R26; R29 |
| W3 | Whole product and time to value | Integrations and data access needed; value in days and live in weeks; existing APIs. No API, EDI or other data access at all is a show-stopper (R30) | 20 | R16 "whole product"; R28 implementation; R30 "plumbing"; R15 rows "Other Components Needed" and "Important Partners" |
| W4 | Competition and substitutes | ~~Incumbent software; brokers or 3PLs doing the job as a service; spreadsheets; doing nothing; general-purpose AI tools~~ *Changed 2026-09-14 (C10, parked change 4):* two questions. Do customers already pay for the job, through a service firm, software or staff time? Is today's software for it weak, legacy or missing? Both = 1, one = 0.5, neither = 0. The evidence is the incumbent map on the S3 fact sheet (item 9): named vendors and the leader's share, brokers or 3PLs doing the job as a service, TMS features, spreadsheets, doing nothing, general-purpose AI tools. The number of competitors is recorded, not scored. One dominant vendor is a show-stopper (§5.5) | 15 | R16; R43; R22; R27; R19; N-D07; N-D29; N-B11 |
| W5 | Willingness to change (per side) | Contract cycles, lock-in, relationship-driven buying, desire to automate, migration cost | 15 | R19 Liquid; R15 "Willingness to Change"; R22 desire to automate; R21 migration costs; R27 "relationship-driven" |
| W6 | Time and resources to win | How fast we could lead; capital and partners needed; how many things must go right | 15 | R16; R15 external and execution filters |

**Why [our call]:** W1 and W3 carry the most weight because the two freight-specific failure stories in the sources are the cost of reaching customers (R30) and the burden of implementation (R28, R21).

### 5.4 Fee feasibility (F)

Score each question 0, 0.5 or 1.

| # | Question | Source |
|---|---|---|
| F1 | Consistency: do all customers value the same outcome, so no bespoke contracts are needed? | R25 |
| F2 | Attribution: would customers credit us for the outcome? | R25 |
| F3 | Measurability: can the outcome be measured in real time from data we can get? | R25 |
| F4 | Predictability: can we predict each customer's saving? Savings measured against freight rates suffer from rate swings: the 501-1,500-mile reefer produce rate went from $3.62/mile in Q1 2022 to $2.23 in Q4 2025 (R34, *verified*) | R25; R34 |
| F5 | Payer equals saver: does the party whose cost falls also pay, or can the fee be taken where the money already moves? | **[our call]**, see T10; R41: "if you bring the cash, you are king", while a fee billed later is seen as "a 'tax'" |

**How to read it [our call]:**
- F1-F4 total 3 or more: a savings-share fee is plausible.
- 2 to 2.5: plan a hybrid, such as a platform fee plus a success bonus, or outcome pricing with a cap (R25).
- Below 2: the candidate cannot meet the fee rule as written. Flag it rather than dropping it automatically, and log it in §9, because the rule itself may need revisiting.
- *Added 2026-09-22 (C24):* **a labour saving counts as a saving under the fee rule only where the customer shows it converts into cash** (hours not paid, work not turned away). Such a card is priced per unit as a stated share of the measured minutes. Separately, the founders will not build software whose saving is cutting paid hours (D-22: "I dont care for creating software that cuts paid hours").
- *Added 2026-10-08 (C28):* **a subscription meets the fee rule.** It is presented as a share off the top of the money the customer recovers, but it is not contingent on recoveries. Founders: "A Subscription. We market it as a scoop off the top of the money they will make, but it will not be contingent on them actually making money." The price is set at Q6.

**Base rate:** outcome pricing is the exception, so expect to need the hybrid fallbacks. In R25's survey of 240 software firms:
- 5% price mainly on outcomes today, and 25% expect to by 2028;
- 41% use hybrid pricing.

### 5.5 Checks run after scoring

- **Show-stopper veto.** Aulet's worksheet scale runs "Very High (best - 1) ... Show Stopper (worst - 4)" (R16). A show-stopper on any row drops the candidate.
  - *Added 2026-09-14 (C10):* a dominant incumbent is a show-stopper on W4. That means one vendor already serves more than half of the target customers for the job, and those customers report being satisfied. The share comes from a survey or filings (S3 item 9); satisfaction is checked in S5. No source gives a number: "more than half" is **[our call]**, set beside Veeva's "over 50% market share" (N-B11).
- **Cohen's multiplicative score, per paying side** (R19).
  - Mechanics: seven rows are multiplied together and divided by 625,000. A score of 1 or more means a viable indie business; 2 or more means a scale-up.
  - Use it to catch a weak link. Cohen: "Why multiply? Because this is a series of 'ands'".
  - His "Plausible" row assumes about 100k businesses, which freight populations may not reach. He allows "a high-price-tag product in a small niche", so adjust that row rather than failing the candidate.
- **Gurley's 10-factor count**, for candidates with a matching or network element (R41): "a 7 or 8 out of 10 would imply that your opportunity of success is much, much higher than if you only match 3 or 4 out of 10".
- **Weight and durability sensitivity** (S4 step 5): the founders' first split (40/45/15) and the strict S&P-style durability test (check C Option 4) (C8).

### 5.6 Crosswalk: where each source's criteria went

This table shows that the scorecard is the union of the sources' criteria with duplicates removed. If a row is questioned, it also shows which sources to go back to.

| Source | Its criteria | Our rows |
|---|---|---|
| Aulet's 8 (R15/R16) | well-funded; accessible to sales; compelling reason to buy; whole product; entrenched competition; leverage to other segments; team values; time to win | K8/A1; W1; A3; W3; W4; A6; K9; W6 |
| Kotler (R09, *assumed*: not seen at source) | size and growth; structural attractiveness; objectives and resources | A1/~~A7~~ K11; A4/W4; K9/W2/W6 |
| ADAMS (R10) | accessible, differentiable, actionable, measurable, substantial | K3, K1, K6, K4, K5 |
| Dolnicar's knock-outs (R14) | homogeneity, distinctness, size, match, identifiability, reachability | K1, K1, K5, K6/K8, K3, K3 |
| Cohen (R19) | plausible, self-aware, lucrative, liquid, eager (twice), enduring | K5/A4, A3, A1/K8, W5, K8/W4, A5 |
| Tidemark (R20) | gigantic; fragmented market; fragmented value chain; "land of the giants" | A1/K5; A4; A4/A6; K10 |
| Emergence (R21) | regulatory change; dissatisfaction with incumbents; concentration; value in data; low cyclicality; migration costs; *dropped as dated or irrelevant:* mobile workforce, SaaS platform alignment, visual dependence, privacy | A3; A3/W4; W1; A6; ~~A7~~ K11; W5 |
| Bessemer, vertical AI (R22) | labour versus software spend; automation propensity; desire to automate; core versus supporting workflow | A2; A2; W5; W4 and the S6 wedge |
| a16z (R23) | role screen; share of the saving captured | K6/A2; A1 |
| Bessemer, supply chain (R28) | budget holder; speed of implementation; immediate-ROI wedge; sticky value | K8/F5; W3; S6; A5 |
| Porter (R43) | the five forces | A4, W4, and F5 (who keeps the saving) |
| Gurley (R41) | new experience; economic advantage; room for technology; fragmentation; supplier sign-up friction; size; market expansion; frequency; payment flow; network effects | A3; A1; A2; A4; W1; A1/K5; A6; A5; F5; A6 |
| CAMP (R25) | consistency, attribution, measurability, predictability | F1-F4, K7 |
| Where to Play (R40) | potential versus challenge (sub-criteria not verified) | Axis A versus Axis W |
| DPM (R12) | balance of short- and long-term, and of internal and market-facing, criteria | the weighting rule in S0 |

---

## 6. What the vertical-SaaS sources add

| Source | What it says (*verified* unless marked) | What we take from it |
|---|---|---|
| Tidemark, *Picking Your Market* (R20) | The ideal vertical is "Gigantic", has a "Highly fragmented market" and a "Highly fragmented value chain" ("selling to fragmented buyers and buying from fragmented sellers"). Size it by "number of locations, initial ARPU, and expansion ARPU". Census screen: x = number of companies, y = revenue share outside the top 50, bubble = sales; upper right = "Vertical SMB SaaS Heaven"; zoom filter = top 50 hold less than 20%. "There are no small airlines!" | A reproducible desk screen for criterion A4, which §8.2 runs on freight. Tidemark's third attribute is the only VSaaS criterion that matches our two-sided unit directly |
| Emergence, *Cloud-Friendly Industry* (R21) | A 2013 scorecard of eight factors that speed adoption and two that slow it. Transportation sits in the second tier, with "more hurdles relating to fragmentation and cyclicality". It prefers concentrated industries ("fewer than 50 companies represent over 80% of revenue") for lower acquisition cost and word of mouth | Useful factors mapped in §5.6. Its view of concentration is the opposite of Tidemark's; see T1 |
| Bessemer, *Vertical AI* (R22) | AI opens verticals once "perceived as too small". Target "text-and quantitative-heavy" work and work "not being done or being done poorly". Supporting workflows ("freight procurement for a shipper") meet less resistance. "just because something can be automated, doesn't mean it should" | Criteria A2 and W5, and the S6 wedge choice |
| a16z, *Vertical SaaS: Now with AI Inside* (R23) | Three waves: cloud, then cloud plus fintech, then cloud plus fintech plus AI, "turning Labor into Software". US software spend of $313bn was "just 3%" of $10.5 trillion in labour spend in 2022 (*assumed*: no source given). Fee example: 10% of a $60k saving | Screen roles, then take a share of the saving (K6, A1, §7) |
| a16z, *Investing in MVMNT* (R27) | Why small and midmarket freight brokers: "$800 billion" of shipper spend; ">60% of the freight brokerage market operates without software"; enterprise tools are "overengineered and cost prohibitive" for the long tail; a fintech layer on top; the founder "lived the problem" (all figures *assumed*: unsourced, 2022) | A compact template of the reasons an investor gives for choosing one freight segment |
| Bessemer, *Supply Chain Roadmap* (R28) | A budget test: carriers and brokers need a product that can "demonstrate value on day one" and turn "opex budget into IT budget". An implementation test: value in days, live in weeks. Wedge: "automation or optimization ... immediate ROI". Convoy, cited approvingly in 2021, shut down in 2023 (reader note) | Criteria W3 and K8, and the S6 wedge rule. A reminder that high scores do not guarantee success |
| Euclid, *Market Sizing* Parts I and II (R42, R24) | Size bottom-up (customers × ARPA). "no significant correlation exists between either ACV or number of customers and Enterprise Value" among about 100 public software companies. Three expansion axes. Choose the wedge by triangulation | S3 sizing, A6, S6 |

**Implications for us [our call]:**
1. Score each side's market structure separately. The best case is fragmented customers who can be reached through a concentrated channel (T1).
2. Look for workflows where the incumbent is labour, not software (R22, R23, R27, R28). Such savings are software-addressable almost by definition.
3. Prefer first products that pay for themselves within days (R28). That also suits a fee taken from savings.
4. In freight, expect the fintech layer (payments, factoring, quick-pay) to be part of any expansion path, and check who already holds it (R23 wave 2; R27; R29).
5. Treat VC criteria as hypotheses, not facts. They are advocacy by investors with portfolios in the category, drawn from companies that survived, and several are dated (R21 is from 2013, R41 from 2012, R28 from 2021).

---

## 7. The fee-from-savings lens

- **The arithmetic.** Fee = ~~capture share~~ fee share of savings × realised saving (renamed 2026-09-14, C2).
  - a16z's 10% is simply asserted, for an incumbent raising its prices (R23).
  - Our share has to be derived from attribution and measurability, and it has to cover the cost of winning and serving each customer (R23 note).
- **Feasibility test: CAMP** (R25), scored in §5.4:
  - Consistency: "Do all customers value the same outcomes?"
  - Attribution: "Can you convince customers to give your product credit?"
  - Measurability: "Can you measure and report on the outcomes in real-time?"
  - Predictability: "Can you predict the outcomes your product will achieve?"
- **How common savings pricing is:** 5% of 240 surveyed software firms price mainly on outcomes, 25% expect to by 2028, and hybrid pricing grew from 27% to 41% in a year (R25). Fallback structures include "Platform fee plus success bonus" and "PAYG with a cap" (R25).
- **Which savings suit a fee.** This is *assumed* until S5 confirms it.
  - Good fit: savings that come as discrete, per-shipment recoveries that can be audited. Examples are freight-bill overcharges, duplicate bills, disputed extra charges, detention billing captured, and demurrage avoided. These resemble R25's recovery businesses with explicit success fees: AirHelp's "35% success fee", "25% per recovered chargeback", and "Only pay for revenue recovered above a baseline".
  - Poor fit: "rate savings" measured against a market benchmark. They score badly on predictability and attribution, because rates swing by about ±40% within a few years (R34).
  - Also weak: risk avoided, such as screening shipments against the denied-parties list (R26). The saving is an event that never happens, so it cannot be counted or credited.
- **Success rate sets the margin** under outcome pricing. In R25's illustration, charging $1 per success, an 80% success rate gives a 75% gross margin and a 60% rate gives 50%. So the first product should target outcomes we can deliver reliably from the start (R25).
- **Freight precedent.** Managed-transportation 3PLs are paid "a flat amount per shipment or a percent of the purchased transportation", and "may include gainshares where transportation savings are shared" (R33, *verified*). Shippers already pay freight intermediaries out of measured savings. Those intermediaries are also the incumbents who collect that fee.
- **Payment position.** "being part of the payment flow is superior", whereas billing after the fact is seen as "a 'tax'" (R41). Where an existing money flow exists (freight payment, audit recovery, factoring), taking the fee there is easier to sustain.
- **Budget.** Selling to carriers or brokers requires value "on day one" that is paid for out of operating costs (R28).
- **Sizing caution.** Euclid rejects market sizes built from "ROI users receive from the product" (R42). Use savings only as the cap on what each customer pays, so market size = buyers × realistic fee (T12).
- **Durability.** Bessemer backs "sticky long-term value, extending beyond short term cost savings" (R28). A one-off clean-up of savings can churn once it is done. Prefer savings that recur, or a path to becoming the customer's system of record, which Cohen's Enduring row scores highest (R19). This is criterion A5.
- **Payer is not always the saver.** Detention hours are lost by carriers and drivers but caused "at Customer Facilities" (R38). Record whose cost falls and who pays for every candidate (F5, T10).

---

## 8. Applying it to freight

### 8.1 Data map: which source answers which question

| Question (stage) | Source | What it gives | Access | Limits |
|---|---|---|---|---|
| Which shipper industries ship what, by which mode? (S1, S3) | CFS 2022 (R32) | Shipper NAICS × commodity (SCTG) × mode × origin-destination. 2022 totals: 12.2 billion tons worth $18.0 trillion; trucks carried 68.1% of tons and 73.5% of value | census.gov/programs-surveys/cfs, data.census.gov, experimental shipment-level public use file | Excludes farms and imports. "Value" is the value of goods, not freight cost |
| How much freight moves where, including farm freight? (S1, S3) | FAF5.7.1 (R31) | Tons, value and ton-miles by region pair × commodity × mode, for 2017, 2018-2024 and forecasts to 2050 | faf.ornl.gov/faf5: Data Tabulation Tool, or 300-700 MB zip files | Modelled estimates. Flows, not spend. No firm counts |
| How big is each type of freight intermediary? (S1, S3) | Armstrong & Associates (R33) | 2025 US 3PL market $323.4B: domestic transportation management $128.3B, international $85.9B, warehousing $72.7B, dedicated carriage $32.0B, software $4.5B | Free summary page | Gross revenue, including freight passed through. No firm counts |
| How fragmented is each freight-company type? (S3, A4, W1) | Economic Census concentration tables (R44) | Firms, revenue, top-4/8/20/50 shares and HHI by NAICS code, 2017 and 2022 | EC1700SIZECONCEN / EC2200SIZECONCEN zip files on www2.census.gov | Firms with payroll only, so owner-operators without payroll are missing |
| How much do transport firms spend on purchased transportation, by mode? (S3) | Economic Census table EC1748PURMODE (R44) | Cost of purchased transportation by mode of shipping, 2017 | data.census.gov, or the Census FTP (sector 48) | Not extracted yet |
| What do produce truck moves cost, and how volatile is that? (S3, F4) | USDA AgRTQ (R34) | Q1 2026: 7.76 million tons of produce by truck, 45% from Mexico; rates $1.50-$2.76/mile by distance band; history back to 2017 | ams.usda.gov/services/transportation-analysis/agrtq, plus datasets and dashboards | Corridor quotes, not contract rates. Fresh produce only |
| Where does the food dollar go? (L-FARM) | USDA ERS Food Dollar (R39) | Farm share 11.8¢; transportation and storage 4.1¢ of each food dollar (2024) | ers.usda.gov food-dollar pages; Ag-FEDS underlying data | National averages on a value-added basis |
| How digital is each sector? (S3, A2, W5) | OECD taxonomy (R45) | Transportation and storage "Low" and agriculture "Low" in both 2001-03 and 2013-15 | Free PDF | Sector aggregates, cross-country averages, 2013-15 |
| What do carriers say hurts? (S5) | ATRI Critical Issues 2025 (R38) | More than 4,200 respondents; top-ten issues with separate rankings for drivers and carriers; detention costs 135.9M hours a year | NCDOT-hosted PDF | Trucking only. Measures votes, not dollars. Industry-affiliated publisher |
| What do shippers and 3PLs say? (S5) | 2026 3PL Study (R37) | Themes: relationships, technology, tariffs, talent | Registration required (not done) | Unread; sponsor-authored |
| Add once shortlisted | ATRI Operational Costs of Trucking; FMCSA registration statistics; USDA Grain Transportation Report (rejected list in `study_links.md`) | Carrier cost benchmarks, carrier counts, grain modal data | See `study_links.md` | Cut for count, not for quality |

### 8.2 The freight-company side on Tidemark's fragmentation screen

Revenue share held by the 50 largest firms in 2022, from R44 (*verified* data). The zone assignments are the reader's computation against R20's filter (top 50 below 20% = "SMB heaven") and R21's concentration test (top 50 above 80%).

| NAICS | Industry | Firms (2022) | Top-50 share | Zone |
|---|---|---|---|---|
| 48422 | Specialized freight trucking, local | 31,927 | 9.9% | Fragmented |
| 48411 | General freight trucking, local | 43,243 | 10.5% | Fragmented |
| 4842 | Specialized freight trucking (all) | 52,012 | 18.6% | Fragmented (passes R20's filter) |
| 488510 | Freight transportation arrangement (brokers, forwarders) | 17,130 | 34.3% | Middle |
| 484121 | Long-distance truckload | 53,705 | 37.4% | Middle |
| 493 | Warehousing and storage | 9,473 | 48.2% | Middle |
| 49312 | Refrigerated warehousing | 719 | 73.9% | Near-concentrated |
| 484122 | Long-distance LTL | 7,675 | 82.9% | Concentrated (passes R21's test) |
| 4921 | Couriers and express delivery | 6,553 | 90.9% | Concentrated |

- Brokerage revenue roughly doubled between 2017 and 2022, from $64.9B to $134.9B, while the top-4 share fell from 12.2% to 9.9% (R44). That period includes the 2021-22 freight boom, so treat it as partly cyclical.
- The same census table exists for shipper industries, so both sides of a candidate can be scored on one scale (R44 note).
- *Added 2026-09-14 (C9):* K10 now fails above 85%, with 75-85% settled at S3 by small firms' share of revenue. On these figures only couriers fail at S2. LTL goes forward as unknown and fails at S3, because firms under 500 employees hold 17.5% of its receipts. Refrigerated warehousing (73.9%) passes. Check D §D4 shows the same industries under the top-4 share, HHI and small-firm share, and adds owner-operators: counting nonemployers lowers all trucking's top-50 share from 28.3% to 22.3% (N-D05).

### 8.3 Freight examples of sub-market choice, and the lesson each teaches

| Example | How they chose | Lesson for our process |
|---|---|---|
| Flexport (R26) | The founder lived as an importer, priced the pains (demurrage "about $200 per pallet per day", paper bills of lading, cashier's checks), sized the market top-down, then chose a segment by technology habits and turned other customers away | Walk the chain as the customer does (S1). Technology habits are a usable segmentation variable. Warning: Flexport concluded "you had to be full-stack. You have to actually do the work", which bears on our software-only rule (T11) |
| MVMNT (R27) | a16z gives three reasons for small and midmarket brokers: market size, the software gap, and a fintech layer, plus a founder who worked as a broker | Criteria A1, A2 and W2. Brokers survive because freight is "relationship-driven" (W5) |
| Silo (R29) | Chose wholesale produce distributors, the hub "connecting growers, grocers, restaurants, and even other distributors", still on "pencil and paper". It partnered with them "instead of competing with or otherwise 'disrupting' them" and earned money through finance (factoring, faster payments, PACA) | Pick the hub node and equip the incumbent (S6). The loss pools named are waste and cash flow, not shipping cost |
| Bushel (R30) | Selling direct to farmers failed: "The cost of acquisition ... it's maybe too high". Bushel moved to "the messy middle": elevators, co-ops, retailers, grain companies. It warns against "solutions looking for problems", and it had to build "plumbing" because ag software lacked APIs | Weight reachability (W1) and integration readiness (W3). Even if the farmer lead proves true, the farmer may be the wrong customer |
| Bessemer's supply-chain map (R28) | An investor category map; a budget test and an implementation test; the immediate-ROI wedge | A checklist of problems that software can fix (S1 "what" axis, S6 wedge) |

### 8.4 The farmer lead: what the evidence so far says

This section is evidence to record in the CLAUDE.md Work Log. It does not decide anything.

**Against the lead, at national level:**
- Of each consumer food dollar in 2024, the farm share was 11.8¢. Transportation and storage for the whole chain took 4.1¢ (R39, *verified*).
- Farms bought 5.1¢ of inputs per food dollar. Agribusiness supplied 3.0¢ of that, and "all other industry groups collectively sold 2.1 cents of inputs to farms" (R39, *verified*).
- So the freight that farms buy directly is at most about 2.1¢ out of 11.8¢ of gross farm receipts, or under about 18%. The real figure is smaller, because energy, finance and others share the 2.1¢. This bound is the reader's computation from R39's figures.
- The farmer's low share of the food dollar comes mainly from processing, food service and retail, not freight (R39 note).

**Against farmers as the customer:** a decade of selling direct to farmers failed on the cost of reaching them. The reachable buyer is the handler in the middle (R30).

**Consistent with the lead, but not proof of it:**
- Farmers get only 7.1¢ of each food-away-from-home dollar, because that food receives "additional processing and transportation" (R39, *verified*).
- Produce reefer rates are volatile. For 501-1,500 miles they were $3.62/mile in Q1 2022 and $2.23 in Q4 2025 (R34, *verified*).
- Harvest logistics lose time when the grain cart, tractor, semi and elevator queue fall out of step: "If any of those things are out of sync, then you're waiting" (R30).
- Two loss pools exist, but neither is a shipping cost:
  - "40 percent of perishable food is wasted in the supply chain" (R29, *assumed*: no source given);
  - growers and distributors face "cashflow challenges" (R29).

**What could still make it true:**
- *Assumed; needs testing:*
  - Specific commodities or channels, such as long-haul perishables, export grain, or produce sold into food service, where "additional processing and transportation" lowers the farm share (R39).
  - Freight that farmers pay indirectly, through lower prices for their crop rather than a freight bill. For grain, the local price (the "basis") often has freight built into it (R39 note, reader knowledge, unverified).
  - Hauling done with the farm's own trucks and labour, which the statistics count as farm value added or labour, not "transportation" (R39 note).
- For produce, 45% of reported US truck volume comes from Mexico (R34). The shipper in question is therefore often an importer at the border, not a US grower.
- The farm-side cost Bushel describes is labour and waiting time in the harvest-to-elevator sequence, not a freight rate (R30).

**How the process treats it [our call]:**
- In S1, farm-origin freight is one family of candidates, not the default.
- It gets tested at S3 with commodity-level Ag-FEDS data (R39), AgRTQ (R34) and the USDA Grain Transportation Report (from the rejected list).

---

## 9. Tensions between sources and how we resolved them

Each tension gives our default resolution and the condition that would flip it. Log changes here with the date. Strike old entries through; never delete them.

| # | Tension | Sources | Our default | Flip it when |
|---|---|---|---|---|
| T1 | Is fragmentation good or bad? | Good: "Highly fragmented market", "fragmented buyers and ... fragmented sellers" (R20); "High buyer and supplier fragmentation is a huge positive" (R41). Bad: concentration lowers acquisition cost and helps word of mouth (R21); dispersed farmers cost too much to reach (R30) | Score fragmentation (A4: many buyers, weak buying power, room for a payments or marketplace layer) separately from reachability (W1: a concentrated channel or hub through which to reach them). The best case is a fragmented side reached through a concentrated channel. The two sides may deserve opposite properties (R21 note) | S5 shows that acquisition cost through the channel is too high. Then raise W1's weight |
| T2 | Start small, or go gigantic? | Small: "not too big and not too small" (R15); "small enough to lead" (R17); niche re-targeting (R19); the funnel (R24). Big: "Gigantic" (R20); venture floors (R42) | The beachhead is small enough to lead and sized bottom-up in detail. The expansion path is scored (A6) instead of TAM precision. The floor comes from the S0 ambition level | The ambition level changes |
| T3 | Focus or flexibility? | "burn the boats!" (R16); single use case (R17) versus keeping related options open, backed by the 25-venture data (R40) | Focus execution on one primary. Keep 1-2 related backups on paper, with triggers (§4 S7). Aulet also allows "you can always come back", and Where to Play also says "Say 'no' to all other options" | Switching to a backup proves expensive; then narrow the backups to the closest ones |
| T4 | Select from a list, or discover through what we know? | The enumerate-score-select methods (R12, R14, R15, R40) versus "entrepreneurs do not always select between alternative market opportunities" (R36) | Run the selection, but score team access (W2) and budget time for immersion or insider advisors | S5 interviews in unfamiliar candidates turn up far fewer costed problems than in familiar ones |
| T5 | Team fit: a gate or a score? | First filter (R15) versus one scored factor among others (R14, R12, R09) | Both: a knock-out (K9) and a score (W2) | Never; this is a values choice |
| T6 | Formal tools or what practitioners do? | Weighted matrices (R12, R14) versus practice collapsing to short-term profit (R13) and "dangerously close to a silly quiz" (R19) | Coarse scales; the plot is for discussion; deciding factors are written down; no single number decides | A study linking scoring discipline to outcomes appears |
| T7 | Add, multiply, or rank? | Weighted sums (R12, R14); multiplication "because this is a series of 'ands'" (R19); unweighted ratings plus discussion (R16) | Add within each axis, run the multiplicative score as a check, and let a show-stopper veto. Fee feasibility stays a separate gate and plot marker rather than a third weighted axis (synthesis B suggested 35/35/30), so a high attractiveness score cannot hide a failing fee | Sensitivity checks keep flipping the ranking; then fall back to R16's discussion ranking |
| T8 | Desk research or primary research? | "If there is already a market research report out there with all the information you need, it is probably too late" (R15) versus Fermi estimates (R19) and top-down sizing (R03) | Desk evidence cuts the list (S2-S3); primary evidence decides (S5) | S5 rarely changes the desk ranking; then shrink S5 |
| T9 | Is a sub-market a product category or a job? | Product categories (R01, R02) versus people plus job (R18); customer × function × technology (R06); depends on purpose (R07) | Each card carries both: a demand-side label (shipper group + job) and a supply-side label (freight-company type). Validate with R02's five signs and R16's three conditions | Job-defined cards fail to produce more distinct problem lists in interviews than mode-defined ones |
| T10 | Which side first, and what if payer and saver differ? | "start ... on the more difficult side first" (R15). Shippers "hold most of the purse strings", but "Either model can work" (R28). "Aggregating demand is much harder and more critical" (R41). Silo and Bushel entered through the intermediary (R29, R30) | Record the four roles for every candidate. Start discovery on the harder side (R15). Enter on the side with the best fee feasibility (CAMP plus budget) and the lowest acquisition cost; that side must pass F (synthesis B, T7) | A candidate's saver and payer can be linked through a shared money flow; then give F5 full marks |
| T11 | Software only, or full-stack service? | The project's software-only rule versus Flexport's "you had to be full-stack" (R26) and Emergence's migration costs (R21) | Keep the rule. Where the winners in a candidate are service firms, score W3 and W4 lower and note it. Also consider selling software to those firms instead of competing with them: R29 partnered with distributors "instead of competing with or otherwise 'disrupting' them", and managed-transportation 3PLs already earn gainshares (R33) | Several finalists can only be won as a service; then revisit the rule in CLAUDE.md |
| T12 | Size the market by savings? | The fee rule versus Euclid's rejection of "ROI users receive from the product" as a sizing method (R42) | The savings pool caps each customer's fee (ARPA). Market size = buyers × realistic fee | Never; this keeps the two ideas consistent |
| T13 | Is low digital intensity headroom or friction? | Headroom (R27, R28); sectors at the bottom in 2001-03 "tend to remain" there (R45); "technophobic decision-makers" (R22); migration costs (R21) | Count it both ways: as headroom in A2 and as adoption risk in W5. Require a named reason why now | A why-now trigger is confirmed in S5; then relax W5 |
| T14 | Cost savings as the entry point, or as lasting value? | Wedge with "immediate ROI" (R28) versus "sticky long-term value, extending beyond short term cost savings" (R28) | Enter on a saving, and score recurrence and system-of-record potential (A5) | Churn data from pilots show savings do not recur |
| T15 | Do the side-specific knock-outs bite at sub-market level? (added 2026-09-15) | The both-sides rule (C11, which follows C5's "better side") against the purpose of K10, keeping out of the "land of the giants" (R20), and of K11 Test 1, no projected shrinking | Keep C11 for run 01. In run 01, K10 and K11 Test 1 removed no card, because every card has a fragmented, growing trucking, brokerage or warehousing side. The tests rule out sides and segments only (`2_knockouts.md` §4.2-4.3). The founders flagged it: "We may reconsider how this test works since its a pass-through" | The entry side is chosen (Q6), or the founders re-define the tests, for example by applying them to the side we would sell to, or at segment level (P-10) |

**Change log** (process changes, newest at the bottom; see "How to change the process" in §10)

| # | Date | Change | Where | Why and evidence |
|---|---|---|---|---|
| C1 | 2026-09-14 | The ambition is stated as numbers, and the K5 floor is derived from the floor outcome | §4 S0 step 1; §10 | In run 01, "net $10M" had three readings whose revenue needs differed four-fold (S0.2, D1). Accepted by the founders (S0.3, change 1) |
| C2 | 2026-09-14 | "Savings capture share" renamed "fee share of savings"; a separate "market share" knob added | §10; §4 S3 step 3; §7 | Two different numbers shared one name (check A). Accepted (change 2) |
| C3 | 2026-09-14 | K2 gains a "not too big" check | §5.1 | Aulet's worksheet 04.4 (N-B17); Moore's "small enough to lead" (N-B16). Accepted (change 3; F-11) |
| C4 | 2026-09-14 | A6 reworded: vertical first, then horizontal | §5.2 | The founders' definition (S0.3, F-12). Accepted (change 7) |
| C5 | 2026-09-14 | Two-sided rule: the axis total uses the better side; the entry side is chosen in segment selection | §5 | The entry side was deferred (F-5). Accepted (change 8) |
| C6 | 2026-09-14 | Durability leaves the score (A7) and becomes a hard viability check (K11), to be defined by its own investigation | §5.1; §5.2 | The founders' decision (S0.3, F-17). Follow-ups in S0.4 (O-2, O-3) |
| — | 2026-09-14 | ~~Parked: change 4 (W4) until F-10 is investigated; change 5 (W1 channel rule) with F-7; change 6 (A4) until F-9 is investigated~~ Change 5 (W1 channel rule) stays parked with F-7. Changes 4 and 6 were applied later the same day as C10 and C9 | S0.3; S0.4 | The founders' decision |
| C7 | 2026-09-14 | A7's weight moves to the long-term rows. Run 01: A5 10 → 15, A6 5 → 15. Defaults: A5 10 → 15, A6 15 → 20. A5 counts as a long-term row | §4 S0.3; §5.2 | A7 left the score (C6), leaving 85 and 90 points, and R12's balance rule needs a long-term row besides A6. The founders' choice (O-2) |
| C8 | 2026-09-14 | K11 defined: Test 1 (no projected shrinking) and Test 3 (the unit a fee would be counted on falls 13% or less = pass, over 20% = fail). Test 2 (customer survival) is recorded as a flag. The strict S&P revenue test joins S4's sensitivity check | §5.1; §5.5; §4 S3 item 8, S4 step 5, S7 | Check C. The founders' choice (O-3), from their note: "we dont want drastic downturns ... we dont want projections of shrinking" |
| C9 | 2026-09-14 | K10 fails above a top-50 share of 85%; 75-85% is unknown, settled at S3 by small firms' revenue share (under 20% in firms below 500 employees fails). A4 becomes structure per side plus a small-firm bonus; the number of buyers stays in A1 and K5 (parked change 6) | §5.1; §5.2; §4 S3 item 4; §8.2; §10 | Check D: no band has outcome evidence; the two startup lines contradict each other; LTL's result is fragile once owner-operators count; small-firm share measures the SMB market directly. The founders' choice (O-4) |
| C10 | 2026-09-14 | W4 scores proven spend plus weak, legacy or missing software (parked change 4). The incumbent map is recorded as evidence. A dominant vendor with satisfied customers is a show-stopper. No cap on the number of competitors | §5.3; §5.5; §4 S3 item 9 | Check D: failures cite missing demand more than competition (N-D29); dominance is the documented risk (N-B11, N-B08). The founders' choice (O-5) |
| C11 | 2026-09-14 | Until the entry side is chosen, K10 and K11 remove a card only if both sides fail | §5 two-sided rule; §5.1 | Follows C5's "better side" rule (check D, D4). Confirmed with the S0 freeze (O-6) |
| C12 | 2026-09-15 | K2 at sub-market level: a card that is one market but too big for word of mouth is flagged S, with a named split variable, and is split into segments at segment selection. S2 splits only a card that mixes products or sales processes | §4 S2 step 3; §5.1; §11; §13 | Run 01 S2 (P-5): splitting 17 cards at S2 would have reversed S1's merge M-1 and roughly doubled the list. The founders: "These will be split into segments, we are going to be targetting segments." |
| C13 | 2026-09-15 | K5 desk rule: pass if 10% of the savings range's low end reaches the floor; fail if 35% of its high end is clearly short; unknown in between. Within a few percent of the floor counts as "about". The central case orders S3a's work but never fails a card | §5.1; §10 | Run 01 S2 (P-6): the removable share is a judgement on nearly every card, so desk ranges are wide. The founders: "This is good." |
| C14 | 2026-09-15 | S3 is split into S3a and S3b. S3a settles the unknowns, lean-fail cards first, with a reserve list for size unknowns that still lean fail. S3b builds fact sheets and the shortlist for the rest | §4 S3; §10; §13 | Run 01 S2 passed 34 cards against a gate of 8-15. The founders chose option C (`2_knockouts.md` §7): "Yes, add a note about option C." and "Ensure the S3 process is updated according to what we have discovered." The reserve rule and the time box are **[our call]** |
| C15 | 2026-09-15 | K11 Test 3 practice (P-7 b-e), and ruled-out sides and segments carried to segment selection (P-8). The fact sheet gains the fee unit and a segments line | §4 S3; §5.1; §11; §13 | Run 01 S2 had to choose units for eight cards, and single firms ranged from growth to -48%. Applied under the founders' instruction to update S3 with what S2 found. P-7 (a), a new field on S1's card template, stays proposed |
| C16 | 2026-09-15 | S3b's cut to 4-6: rank by the sum of the two axes, keep the cards above the first clear break, break ties on the central fee pool, and record the order under other readings and the 40/45/15 split (P-15) | §4 S3b; §10 | Run 01's S3b step said "keep the top 4-6" without saying how two axes combine. Adopted by the founders on 2026-09-15 (`research/selection_runs/run-01/3_shortlist.md` §8) |
| C17 | 2026-09-15 | A3 at desk level: 1 needs a dated rule, rule change or crisis that acts on the card's own job. Market-wide triggers, a neighbouring job's triggers and pending rules score 0.5 (P-16) | §5.2; §4 S4; `0_criteria.md` §5 | The three S3b research checks read A3 differently on five cards, and A3 is Axis A's heaviest row. Adopted by the founders |
| C18 | 2026-09-15 | Score each card's job as its sentence defines it. Record the effect of the first product (the wedge) on W3 and W6 as a sensitivity; the wedge is chosen at S6 (P-17) | §4 S3b, S4; `0_criteria.md` §5 | Keeps the scores to the problem (problem first, solution second, CLAUDE.md). In run 01, C-20's Axis W moved from 52.5 to 87.5 depending on the wedge. Adopted by the founders |
| C19 | 2026-09-16 | **A4 is scored on the side that would pay, not the better side** (P-18). Until the entry side is chosen, use the side the fact sheet names as the budget holder, and record the other side beside it | §5 two-sided rule; §5.2; `0_criteria.md` §4 | Run 01's S4: C-08 scored A4 = 1 from the carriers being vetted, who never pay us; its paying side, brokers, scores 0.5. That one row was half of C-08's lead. A4 measures fragmented buyers with weak buying power (R20, R41), so a fragmented non-paying side says nothing. Adopted by the founders 2026-09-16 (`research/selection_runs/run-01/4_scorecard.md` §9.1). **Run 01 re-scored:** C-08's Axis A goes 100 → 92.5; no other shortlisted card moves |
| C20 | 2026-09-16 | **Single-point dependencies are recorded on the fact sheet** (P-21): any party that is not a competitor but can withdraw the data, licence or access the product needs | §4 S3b item 9; §13 | Three of five shortlisted cards have one (NMFTA's class licence, FMCSA's frozen authority dataset and move to Motus, retailer portals with no open API), and W4 scores competitors, not dependencies. Adopted by the founders 2026-09-16 |
| C21 | 2026-09-16 | **S5 coverage depends on what each side is** (D-12): full interviews on a side that could buy from us; for a counterparty-only side, its documented position plus 1-2 interviews with people who work against it daily | §4 S5 scope, step 1, gate; §10 | Run 01's four finalists include two whose second side is a top-4 retailer or a concentrated LTL carrier base. Five discovery calls with those parties is a gate a pre-revenue team cannot meet, and missing it would say nothing about the card. Chosen by the founders 2026-09-16 |
| C22 | 2026-09-22 | **S4 gains step 7: per-customer profit and a kill condition for every card going to S5.** The chain is fee = unit volume × leak rate × share removed × share realised × fee share, gross profit = fee − cost to serve; the four numbers are break-even size, the rate that covers variable cost, both with the cheapest labour, and the size that reaches $5k a year. The kill condition is three-banded, measurable by S5's assessment or data-access test, fixed before the measurement, and owned by the founders | §4 S4 step 7; §10; §13; `0_criteria.md` §5; `research/selection_runs/run-01/4_kill_conditions.md` | Through S4 the score measured the pool (A1, K5) and whether a fee was chargeable in principle (F1-F5), never profit per customer. For C-09 that row entered only at S6 and, with the practice audit's inputs, showed a customer that never pays back its acquisition cost at the desk's central rates. Every "money back" card has come in under its desk estimate as evidence improved, so the test belongs before S5, not after. The founders' decision, 2026-09-22 (`4_scorecard.md` §9.1, D-21): "Adopt the Kill Condition, this is going to be part of S4, for subsequent runs, but we are going to run it against all of our remaining candidates now." Applied to run 01 late: C-09 done, C-11, C-19, C-20 handed to a separate chat |
| C23 | 2026-09-22 | **The ceiling test in S4 step 7** (P-27): a card is eliminated at step 7 only if it fails the per-customer test even with every unmeasured input at its most favourable value; otherwise it goes on with its kill condition | §4 S4 step 7; §4 S4.5 step 5 | The founders' rule of 2026-09-22 was to eliminate any card that shows no viability and to keep cards alive on unknowns (D-22, `research/selection_runs/run-01/4_kill_conditions.md` §7.1). C-11 was the first card eliminated this way, on measured customer size. Adopted by the founders 2026-09-22 ("4. Yes") |
| C24 | 2026-09-22 | **Labour savings under the fee rule** (P-28): a labour saving counts as a saving only where the customer shows it converts into cash (hours not paid, work not turned away), and such a card is priced per unit as a stated share of the measured minutes | §5.4 | C-20's saving was an entry writer's time, which is money only if the broker turns it into cash (`research/selection_runs/run-01/4_kill_conditions.md` §5.5). Adopted by the founders 2026-09-22 ("4. Yes"). The founders also said they will not build software that cuts paid hours (D-22) |
| C25 | 2026-09-22 | **New stage S4.5, Profitability check**, between S4 and S5: audit every public source on the per-customer model's deciding inputs (real transaction documents first), run a desk look-back on any real data, re-run the model, and give a verdict: proven profitable, proven unprofitable, or not provable from the web | §1; §4 S4.5; §10 | The founders' words, 2026-09-22: "I want to add an S4.5 Profitability check, which is a test if any of our sub-markets can be proven profitable before we do customer reviews. This relies on auditing web information relevant to what we've checked out." Run 01 applies it to C-19 first (`research/selection_runs/run-01/4_5_profitability.md`) |
| C26 | 2026-09-22 | **Screen before the savings assessment when the leak is concentrated** (P-29): where S4.5 shows the recoverable rate is skewed across customers, S5 screens every recruit for the marker of the high-leak group and runs the savings assessment on one that has it. It also records the screen yield and the new-money share (the recovered dollars the customer would not have got on its own). Run 01, C-19: non-trade deductions of 1% of sales or more | §4 S5 step 3; `research/selection_runs/run-01/4_kill_conditions.md` §4.7; `5_interview_kit.md` §5.5, §6.3 | S4.5 found that on the neutral distribution a random small supplier would fall under C-19's kill line about 64% of the time even if the business were real, because the test would measure the median customer, not the business. Founders, 2026-09-22: "Yes screen recruits first." |
| C27 | 2026-09-22 | **C-19's Test 1 pass line re-derived** (P-30): ~~0.17%~~ → **0.22% of sales, provable-invalid, at a $50M supplier**, with a table by the supplier's size (0.47% at $20M, 0.14% at $100M, 0.094% at $200M). The kill line stays 0.05% | `research/selection_runs/run-01/4_kill_conditions.md` §4.7; §10 | The 0.17% line's comparison rested on STAT's all-in 0.2%, and STAT's own split puts deductions won at 0.03%. The line is re-derived on S4.5's bar (12-month payback on a $10k acquisition cost at US wages) for a screened supplier (non-trade deductions 1.2% of sales, from the one in-segment ledger). It rises because the test is now payback, not a $5k fee, and screened suppliers cost more to serve. Founders, 2026-09-22: "Update according to P30 as well." |
| C28 | 2026-10-08 | **A subscription meets the fee rule** (C-09 re-run, `research/selection_runs/run-01/4_kill_conditions.md` §2.5.10 question 1): the fee may be a fixed subscription, presented as a share off the top of the money the customer recovers but not contingent on recoveries. The price stays a Q6 decision | §5.4; `CLAUDE.md` constraints | Under D-23 the customer files the disputes, so a share needs proof of every credit, and check AS found the market prices customer-files software by subscription. Founders, 2026-10-08: "A Subscription. We market it as a scoop off the top of the money they will make, but it will not be contingent on them actually making money." |
| C29 | 2026-10-09 | **C-09's kill condition re-set on the software basis** (D-23). Test 1 measures the flagged rate on in-window spend (what the software flags and the shipper's reviewer accepts as wrong and provable), against three lines read at the shipper's size, **Kill / Cover / Pass**: at $1.5M, under 0.044% kills; 0.51% covers our first-year cost for a customer won for $0; 6.44% or more passes, repaying even a $10,000 acquisition cost within 12 months. Between Kill and Pass, a pilot of at least one billing cycle settles follow-through, and S6 cannot confirm C-09 until the acquisition cost is measured. Test 2 is unchanged, with a "no" that names only SOC 2 treated as a cost question. Test 3 sets the customer's timed hours against its stated capacity, with our reading cost at or under $0.50 a bill. Replaces the 2026-09-22 lines (kill under 0.75%, pass at 1.3%) | `research/selection_runs/run-01/4_kill_conditions.md` §2.4 (struck through), §2.5.8, §2.5.11, §2.5.12; §10; `0_criteria.md` §5 | The 2026-09-22 lines costed our own analysts' review, which D-23 rules out. The new lines rest on the founders' answers of 2026-10-08 (a subscription, hours as capacity, the look-back design, Test 1 on flagged dollars, the acquisition cost bounded at $0-$10,000) and are fixed before any look-back. Founders, 2026-10-09: "Adopt the Kill/Cover/Pass lines" |

---

## 10. Tuning guide

| Knob | Default | Range the sources give | When to change it |
|---|---|---|---|
| Ambition level (S0) | ~~Must be stated~~ Stated as numbers (C1). Run 01: floor $2.5M yearly revenue, stretch $10M, 5 years from product launch, self-funded (S0.3) | Indie: score of 1 or more on Cohen's scale, about 100k businesses (R19). Venture: beachhead SOM of a few hundred million and a path to a $15B TAM (R42) | Funding plans change |
| Long-list length (S1) | 20-40 cards | "as long a list as possible" (R15); five domains (R40); Documentum's 80 markets (via R15) | Too few distinct problems turn up in S5 |
| Survivors after knock-outs (S2) | About 8-15. *Run 01 (2026-09-15):* 34 survived; the founders split S3 (C14) rather than tighten the knock-outs | none given | Knock-outs are too loose or too tight |
| K5 desk lines (S2, S3a; added 2026-09-15, C13) | Pass if 10% of the savings range's low end reaches the floor; fail if 35% of its high end is clearly short. Within a few percent counts as "about", so unknown, leaning fail. The central case, 20% of the midpoint, only orders S3a's work | The S0 fee shares of 10%, 20% and 35% (this table) | Sourced removable shares arrive, from S5's savings assessments or neutral data |
| S3a reserve rule (added 2026-09-15, C14) | A card still unknown on K5 after S3a, with a central fee pool under the floor, goes to a reserve list, not S3b. It is not dropped, and the founders can pull it into S3b | none; **[our call]** | S3b has room for more cards, or S5 evidence arrives |
| Shortlist (S3) | 4-6 | "Four to 10 ... usually 4 to 6" (R15) | Team capacity for S5 |
| S3b cut rule (added 2026-09-15, C16) | Sum of the two axes; keep the cards above the first clear break inside 4-6; break ties on the central fee pool; record the sensitivity. *Run 01:* five cards, with a 10-point break at 145/135 | none; **[our call]** | S4's sensitivity keeps changing the shortlist |
| Weights (S0) | §5.2 and §5.3 defaults; each person splits 100 points per axis, then average. Run 01: A1 20, A2 10, A3 25, A4 15, A5 15, A6 15; W1 20, W2 5, W3 20, W4 15, W5 15, W6 25 (S0.3) | 100-point votes (R12); percentages (R14: 25/35/20/10/10); no weights (R16) | Sensitivity checks keep flipping ranks, or a new team member joins |
| Scoring scale | 1 / 0.5 / 0 at desk stage; 1-10 after S5 | 1 / 0.5 / 0 (R12); 1-10 (R14); Very High to Show Stopper (R16); powers of ten (R19) | The evidence gets richer |
| How scores combine | Add per axis; multiplicative check; show-stopper veto | R12, R14 (add); R19 (multiply); R16 (discuss) | See T7 |
| Bubble variable | Fee potential | Income (R12); profit potential (R14) | Fee model changes |
| Fee-feasibility cut | F1-F4 of 3 or more = plausible; 2-2.5 = hybrid; below 2 = flag | CAMP (R25) | Pilots show which outcomes customers accept |
| ~~Savings capture share~~ **Fee share of savings** (S3 fee potential; renamed 2026-09-14, C2) | Model 10%, 20% and 35%; validate in S5 | 10%, asserted (R23); a "35% success fee" and "25% per recovered chargeback" (R25); gainshares with no stated share (R33); 9-12.5% for large recovery audits and 25-50% for parcel and freight audits (N-A28, N-A25, N-A26) | Pilots show what customers accept |
| **Market share** (K5 floor and S3; added 2026-09-14, C2) | 10% for the floor test; 20% and 35% for the stretch | Vertical leaders "can exceed 40%+ market share", and growth gets easier past "roughly 10%" (N-B09); "50%+ market penetration" in some cases (N-B08). Both describe survivors | Evidence on the share achievable in the chosen sub-market |
| Size floor (K5) | Venture: a beachhead SOM of a few hundred million (R42). Indie: tens of millions of fee potential (**[our call]**, from synthesis B, not validated). Run 01: about $25M a year of fee potential, the $2.5M floor ÷ a 10% market share (C1; S0.3 F-4) | "$100M for a beachhead" (R24); "a few hundred million" (R42); about 100k businesses (R19) | The ambition level changes |
| NAICS level for the census screen | ~~6-digit for freight companies; 4-digit for shipper industries~~ 6-digit on both sides where they exist (C9) | 4-digit (R20); 3- to 6-digit available (R44). Finer levels expose opposite structures: all trucking (484) has a top-50 share of 28.3%, but LTL has 82.9%. On the shipper side, 3114 looks mixed (64.2%) while its sub-code 311411 fails K10 (97.4%) (check D) | A code has too few firms to be meaningful |
| Fragmentation bands | Top-50 share below 20% = fragmented; 20-80% = mixed; above 80% = concentrated. K10 fails ~~above 80%~~ above 85%, with 75-85% settled by the small-firm check (C9) | R20's filter; R21's threshold. Antitrust HHI bands (N-D07, N-D08, N-D09) and CR4 bands (N-D13) exist but were built for other purposes (check D) | Evidence on acquisition cost by band ~~; the F-9 investigation (S0.4, O-4)~~ |
| Small-firm check (K10's 75-85% zone; A4 bonus; added 2026-09-14, C9) | K10 zone: fail if firms under 500 employees hold less than 20% of revenue. A4 bonus: +0.5 if firms under 20 employees hold 25% or more | None published; **[our call]** from check D (Census SUSB, N-D04) | Evidence on which firm sizes actually buy |
| Durability lines (K11 Test 3; added 2026-09-14, C8) | The unit a fee would be counted on falls 13% or less = pass; more than 20% = fail; between = unknown. Downturns: 2008-09 and 2022-25 | S&P's revenue bands at 4, 8, 13, 20 and 32% (N-C01): statistical clusters, not viability limits | A new downturn, or pilots show which units hold up |
| Dominance veto (W4 show-stopper; added 2026-09-14, C10) | One vendor serves more than half the target customers for the job, and they are satisfied | Veeva's "over 50% market share" (N-B11). The 2023 guidelines' 30% line (N-D07) is a reference, not a test | S5 evidence on switching |
| Implementation target (W3) | 4 weeks or less to the first measured saving | "demonstrate value in a matter of days and be live in weeks" (R28) | Every integration-heavy finalist fails it |
| Expansion horizon (A6) | 5 years | "usually 5-10 years down the road" (R42) | The stage changes |
| Interviews in S5 | ~~5 per side per finalist~~ *changed 2026-09-16 (C21):* 5 per finalist on every side that could buy from us; 1-2 plus the documented position on a counterparty-only side. Over 2-4 weeks | "at least a few weeks"; "over three months" (R15) | Answers keep diverging; then add more |
| S5 evidence gate | §4 S5 | none given | First run shows it is too strict or too loose |
| Kill-condition lines (S4 step 7; added 2026-09-22, C22) | Per card, three bands on the measured leak rate, on document access and on measured cost to serve. ~~Run 01, C-09: kill under 0.75% of in-window spend, pass at 1.3% or more; kill if 2 of the first 3 shippers refuse the rate agreement; kill if measured cost is negative at a $1.5M customer under US and offshore wages.~~ **Run 01, C-09 (adopted 2026-10-09, C29):** Test 1 on the flagged rate, Kill / Cover / Pass by the shipper's size (at $1.5M: under 0.044% / 0.51% / 6.44% or more), the middle band settled by a pilot's follow-through; kill if 2 of the first 3 shippers decline to upload; kill if the customer's timed hours exceed twice its capacity. *Note, 2026-10-08 (D-23): C-09's lines rest on our own review cost (US and offshore wages), which D-23 rules out; a re-run is pending (`handoff_c09_software_rerun.md`). The lines stay frozen and in force until the founders adopt new ones, which will then be logged in §9 (~~C28~~ C29; C28 is the fee-rule entry of 2026-10-08). C-19's lines are flagged for the same re-run.* *2026-10-09: adopted as C29 (`research/selection_runs/run-01/4_kill_conditions.md` §2.5.12).* Run 01, C-19 (adopted 2026-09-22; C26, C27): kill under 0.05% of sales in provable-invalid non-trade deductions, pass at 0.22% at a $50M supplier (table by size), measured on a supplier screened at 1% or more | none published; **[our call]** from the per-customer model (`research/selection_runs/run-01/4_kill_conditions.md` §2.4) | Only through §9, and never after the measurement it applies to has been seen |
| Profitability bar (S4.5; added 2026-09-22, C25) | **Proven profitable:** on *verified* or neutral inputs only, positive gross profit, a $5-15k acquisition cost repaid within 12 months, and enough such customers for $1M at a 10% share and $2.5M at no more than 35%. **Proven unprofitable:** fails even at the most favourable neutral-supported values | check A §A3 (12-month payback, $5k per customer); check A §3.3 (10-35% shares); **[our call]** on combining them | Only before an audit starts, through §9 |
| Backups | 1 primary, 1-2 backups, 1-2 growth options | "a small portfolio of backup and growth options" (R40) | Cost of switching turns out high or low |
| Planning horizon | 3-year projection on each score sheet | 3 years (R12, R40); six-year commitment question (R15) | Stage changes |
| Revisit triggers | §4 S7 list | "until it proves not to work" (R16); a regular habit (R40) | After each trigger review |
| Who decides | Whole team, signed, with deciding factors; an optional outside reviewer (the adversarial review stage in `prompt.txt`) | Team signature (R16); advisory committee (R14) | Team changes |

**How to change the process:**
1. Change the knob in the table above, keeping the old value struck through, with a date.
2. Log the reason and the evidence in §9.
3. If a run is in progress, re-score the affected rows and note the change in that run's decision record.

---

## 11. Reusing the process

- **Segment stage (Q6).** Run S0-S7 again inside the chosen sub-market. What changes:
  - The unit becomes a customer segment: an end user doing a job, per Aulet (R15) and Ulwick (R18).
  - Desk evidence thins out and primary research grows (R15; R24's funnel).
  - Dolnicar's plot was built for segments (R14).
  - Cohen's rubric fits best here, because it scores "a specific type of buyer solving a specific problem" (R19).
  - *Added 2026-09-15 (C12, C15):* the project targets segments. The chosen sub-market arrives with a first cut already made:
    - the split variable its K2 S flag named at S2, such as shipper industry, fleet size, importer size or port;
    - the sides and segments that K10 and K11 already ruled out (`2_knockouts.md` §4.5, §8).
- **Another industry.** The generic parts carry over unchanged: the S0-S7 structure, the knock-out, score and check mechanics, and the crosswalk. The freight-specific parts must be replaced:
  - the two-sided unit (§2.2);
  - the data map and census screen (§8);
  - the fee examples (§7).

---

## 12. Limits of the evidence

**Where the process rests on data, and where on authority:**

| Part of the process | Strongest support | Strength |
|---|---|---|
| Keep related backups (P8) | R40 working paper: 25 ventures, qualitative, one country. Association, not causation | Weak to moderate empirical |
| Practice falls back to short-term profit (P5, P6) | R13: cases plus two studies of UK firms (full text not read) | Moderate empirical |
| TAM precision matters less than expansion (P10) | R42: about 100 public software companies, survivors only | Weak empirical |
| Outcome pricing is rare (§7) | R25: 240 self-selected software vendors | Moderate survey; says nothing about freight buyers |
| Opportunities come from prior knowledge (T4) | R36: 8 case studies of one invention | Weak empirical |
| Weighted two-axis scoring (S4) | R12, R14, R40, R09: textbook authority, one real case (R12) | Authority only; no outcome evidence |
| Talk to customers before choosing (S5) | R15, R35, R17, R19: practitioner authority | Authority, strong agreement across sources |
| VC vertical criteria (§6) | R20-R24, R27, R28, R41: investor essays | Authority plus survivorship and advocacy bias |
| Durability lines (K11) | S&P's k-means bands (N-C01), calibrated on large rated companies in economy-wide recessions | Statistics, but not viability limits |
| Fragmentation bands and the small-firm check (K10, A4) | Tidemark's and Emergence's lines (R20, R21), which contradict each other; no outcome data (check D) | Authority only |
| No cap on competitors (W4) | CB Insights' 101 failure post-mortems (N-D29, self-selected); Golder and Tellis on pioneers (N-D28, abstract only) | Weak empirical |

**Not read in full (details in each note):**
- Only a record or abstract was available for: Abell (R05), Day (R07), Kotler (R09; its three-part evaluation rule is *assumed*), McDonald & Dunbar (R11), Simkin & Dibb (R13), Shane (R36).
- Partial reads:
  - Shapiro & Bonoma (R08; the inner three nests are *assumed*).
  - Moore (R17; the book was not read).
  - The Mom Test (R35; its rules come from summaries).
  - Where to Play (R40; its worksheets are behind an email sign-up, so the potential and challenge sub-criteria are *assumed*).
  - Porter (R43).
  - Tidemark (R20; the text after a login notice, and the 2025 update, are gated).
  - FAF5 (R31; its tables were not pulled).
  - AgRTQ (R34; the regional sections were not read).
- Unread: the 3PL Study (R37; registration required).

**Check before hard-coding** (each takes minutes):
- the Where to Play worksheet sub-criteria (email sign-up);
- Kotler's three-part rule (a library copy of R09).

**Corrections found while reading.** `study_links.md` has not been edited; these are listed for the adversarial review. Sources: synthesis A §8 and synthesis B §8.
- R13: "practice collapses to short-term profitability" overstates the abstract. Better: "suggests practice often reduces to short-term profitability".
- R17: "big enough to matter, small enough to lead" is not on Moore's page. It is confirmed only in Lenny's Podcast show notes, which are on the rejected list.
- R09: the catalog page confirms only the chapter title. The requirements list and the evaluation rule are not visible there.
- R08: the HBR page shows only the opening paragraph.
- R35: "customer slicing" is not on the storefront page.
- R16: the free Google Doc worksheet exists and uses an ordinal scale with no weights.
- R40: "backed by the authors' academic research" is the site's own claim.
- R20: "locations × initial ARPU × expansion ARPU" is a paraphrase. Tidemark names the three quantities and gives no formula.
- R45: the "bottom quartile on every indicator" gloss is correct for agriculture, too strong for transportation (whose online-sales score is high).
- R32: the Census press release's South-region tonnage is internally inconsistent; do not quote it.
- R41: the downloaded page contains an injected sentence that is not Gurley's; do not quote it.
- R33: the four segments listed sum to $318.9B. The $323.4B total also includes "Contract Software/Systems" at $4.5B.
- R34: the Q1 2026 issue says "During first quarter 2025" in its diesel sentence, a typo in the source.
- R37: the landing page shows Langley and NTT DATA but not Penske (unverified).
- R24/R42: Euclid's beachhead floor differs between Part I ("a few hundred million") and Part II ("$100M").
- R44: the note reads the HHI "n/a" cells as zero. The 2022 file flags them "D", meaning withheld to protect individual firms (check D; N-D03).

---

## 13. Templates

**Candidate card (S1)**
```
ID: C-07
Sentence: "[job] for [shipper group], handled today by [freight-company type / method]"
Who (shipper group, with codes): e.g. NAICS / SCTG, size band, region, technology habits
What (the job, in their words):
How (today's method or freight-company type, with NAICS):
Roles: cost falls on __ | decides: __ | pays: __ | harder side: __
Human end user on each side (a role, e.g. shipper logistics coordinator, carrier dispatcher):
Sub-market signs (R02): products / customers / competitors / price / channels
Source of the idea: grid cell / chain walk / investor map / fringe
```

**Knock-out sheet row (S2)**
```
C-07 | K1 ✓ | K2 split? | K3 ✓ | K4 ? | K5 ? | K6 ✓ | K7 ? | K8 ✓ | K9 ✓ | K10 ✓ | K11 ? | result: forward (4 unknowns) | reason: —
```
*Added 2026-09-15 (C12):* K2 can also read **S**: one market, but too big for word of mouth, so it is split into segments at segment selection (name the split variable).

**Fact sheet (S3)**
```
Buyers per side (count, source) | Savings pool (unit cost × volume × addressable share; assumptions)
Fee potential (buyers × fee cap) | Structure (top-50 share, small-firm share, HHI, five-forces notes)
Software penetration + why now | Addressable roles | Budget holder | Time to go live
Cyclicality / growth (K11 unknowns; Test 2 survival flag) | Incumbent map for W4: vendors, leader's share, service firms, how it's done today (including doing nothing)
Unit a fee would be counted on | K11 series or proxy, and its fall in both downturns (C15)
Single-point dependencies: parties that are not competitors but can withdraw data, a licence or access (C20)
Segments: K2 split variable and likely segments | sides and segments ruled out (C12, C15)
From S3a: unknowns settled (evidence) / still open (why) (C14)
Each line tagged verified / assumed, with a link
```

**Score sheet (S4)**
```
| Row | Weight | C-03 score | evidence | C-07 score | evidence | ... |
A1 … A6, W1 … W6 → axis totals (0-100); A7 is now knock-out K11
F1-F5 → fee total | Cohen score per paying side | Show-stopper? | Gurley count (if matching)
Sensitivity: top candidate under each person's weights
Key deciding factors:
```

**Interview log (S5), from R15**
```
Hypothesis | Validated? (yes / with hesitancy / no) | Finding (quote, number, date, role) | Next step
```

**Decision record (S6-S7)**
```
Date | Primary | Backups | Growth options | Parked (reasons)
Wedge hypothesis (adopt now / build fast / grows how)
Key deciding factors | Evidence links | Weights used (and whether sensitivity held)
Revisit triggers (measurable, dated) | Team sign-off
```

**Kill condition (S4 step 7; added 2026-09-22, C22):** the template is in `research/selection_runs/run-01/4_kill_conditions.md` §1, with C-09 as the worked example in §2.

---

## 14. Source index

| R-ID | Contribution | Used in |
|---|---|---|
| R01, R02, R03, R04 | Sub-market definitions, the five signs, the product/market grid, market-definition methods, the STP sequence | §2, S1, S2, T9 |
| R05, R06 | Customer group × function × technology: the unit of analysis | §2.2, S1 |
| R07 | Definitions depend on purpose (top-down versus bottom-up) | §2.2, S1 |
| R08 | Nested variables for segmenting business markets | S1 |
| R09, R10 | ADAMS knock-outs; the three-part evaluation rule (not verified at source) | K1-K5, §5.6 |
| R11, R12 | Directional policy matrix: 100-point weights, 1/0.5/0 scores, the balance rule | P1, S0, S4, §10 |
| R13 | Practice falls back on short-term profit | P5, P6, T6 |
| R14 | Knock-outs fixed in advance; the "to us / to the segment" plot | P1, P4, S4, K1 |
| R15, R16 | Brainstorm, narrow to 4-6, primary research, the eight criteria, three conditions, beachhead worksheet | throughout |
| R17 | Beachhead, whole product, "small enough to lead" | S6, P8 |
| R18 | Jobs-to-be-done market definition and its quality tests | §2, S1, S5 |
| R19 | Six tests and the multiplicative score | S3, §5.5, T7 |
| R20, R44 | Vertical attributes and the census fragmentation screen, with the freight data | §6, §8.2, A4 |
| R21 | Adoption accelerators and brakes; concentration preferred | §6, T1, W5 |
| R22, R23 | Automation fit, labour versus software spend, fee arithmetic | K6, A2, §7 |
| R24, R42 | Sizing, expansion axes, wedge triangulation | S3, S6, P10, T2, T12 |
| R25 | CAMP, pricing base rates, hybrid fallbacks | K7, §5.4, §7 |
| R26-R30 | Freight and agriculture selection examples | §8.3, S6 |
| R31-R34, R39, R45 | Datasets | §8.1, S3 |
| R35, R36, R37, R38 | Interview discipline, prior knowledge, outside problem surveys | S5, T4 |
| R40 | Identify, evaluate, prioritise; related backups | P2, P8, S6, T3 |
| R41 | Ten factors for two-sided markets; payment flow | §5.5, §7, T1 |
| R43 | Five forces; who keeps the saving | S3, W4, F5 |

### 14.2 Sources added by the S0 check (run 01)

The full entries, with URL, date, access status and what was read, are in `research/s0_check_A_ambition_economics.md` (N-A), `research/s0_check_B_structure_access.md` (N-B), `research/s0_check_C_durability.md` (N-C) and `research/s0_check_D_fragmentation_incumbents.md` (N-D).

On 2026-09-14 the coordinator re-fetched five load-bearing sources: N-A01, N-A09, N-B01, N-B04 and N-B24. The figures used here all matched. One figure in check A that this doc does not use was wrong: FE International gives "2.5x to 4x SDE" for firms under $1M ARR. It has been corrected in check A. In the second round, also on 2026-09-14, the coordinator re-fetched N-C01, N-C05, N-D02, N-D07, N-D29 and N-D30, and all matched.

| ID | Source | Used in |
|---|---|---|
| N-A01 | ChartMogul, *Against the Odds: The 2025 SaaS Growth Report* (15 Oct 2025) | S0.2 norm, D1 |
| N-A03, N-A04, N-A06 | SaaS Capital: 2026 growth benchmarks; 2026 spending benchmarks; *Growth, Profitability, and the Rule of 40* (2025) | D1, F-3 |
| N-A08 | SaaS Capital Index (chart of 31 Aug 2026) | D1 |
| N-A09 | FE International, *SaaS Valuation Multiples 2026* (25 Aug 2026) | D1 |
| N-A10 | High Alpha, *2025 SaaS Benchmarks Report* | D1, D2 |
| N-A12 | Neeraj Agrawal (Battery), *The SaaS Adventure* (T2D3), 2015 | D1 |
| N-A13 | Bessemer, *Scaling to $100 Million*, 2021 | D2 |
| N-A15 | Christoph Janz, *Five years later: Five ways to build a $100 million SaaS business*, 2019 | D2 |
| N-A20 | Tomasz Tunguz, *A Founder's Guide to Go-to-Market Strategy*, 2025 | D2 |
| N-A22 | Gompers, Kovner, Lerner and Scharfstein, *Performance Persistence in Entrepreneurship*, JFE 2010 | S0.2 norm |
| N-A23 | Azoulay, Jones, Kim and Miranda, *Age and High-Growth Entrepreneurship*, AER: Insights 2020 | S0.2 norm, F-15 |
| N-A25, N-A26, N-A28, N-A30, N-A32 | Fee shares: D'Arrigo's parcel and freight audit guides (2026); CRS report on Medicare recovery audits (2009); Logistics Management on 3PL gainshares (*assumed*: page blocked); Racklify on freight audit costs (2026) | D1, F-8 |
| N-A36, N-A37 | Bessemer's Mindbody memo (2010); Euclid, *VERTICALS #10*, on Levelset (2025) | D1 |
| N-B01 | ATA, *American Trucking Trends 2025* (28 Aug 2025) | D2 |
| N-B03 | IFA Commercial Factor, carrier and broker failures 2024-25 (secondary) | D3a, F-17 |
| N-B04 | Brush Pass Research: broker counts and exits; the software micro-cap brokers use (2025) | D2, D3, D4, F-17 |
| N-B05 | FreightWaves, carrier and shipper counts (2026, citing ATA and FMCSA) | F-6 |
| N-B08 | Bessemer, *Ten lessons from a decade of vertical software investing* (2022) | S0.2 norm, D3a, D5 |
| N-B09 | Tidemark, *Truths about Vertical SaaS* | D1, D2, D3 |
| N-B10 | Tidemark, *2025 Vertical & SMB SaaS Benchmark Report* (public page only) | D5 |
| N-B11 | a16z, *Fintech Scales Vertical SaaS* (2020) | D2; W4; §5.5 |
| N-B12 | Constellation Software president's letters (2010-2021) | S0.2 norm, D3, D5 |
| N-B13, N-B14 | Thiel, *Zero to One* (quote pages only, *assumed*); Paul Graham, *How to Get Startup Ideas* (2012) | D3b |
| N-B16, N-B17, N-B18 | Moore, *After the Chasm*; Aulet's Step 4 page and worksheets; Brikman's review of Aulet (source of the *assumed* $20-100M range) | D4 |
| N-B19 | Bessemer, Toast Series B memo (2015) | D2, D3b |
| N-B20, N-B21 | ServiceTitan S-1 (2024); Veeva 10-K (FY2024) | D2, D3a, D5, F-6 |
| N-B22 | Contrary Research, Motive (2023) | D2, D5 |
| N-B24, N-B25 | Aljex (2018) and BoxTop (2024) sales to Descartes | S0.2 norm, D1, D3b, D4 |
| N-B26, N-B27, N-B28 | MVMNT, Rose Rocket and Alvys funding coverage | D3b |
| N-B29 | FreightWaves, Convoy obituary (2023; opinion) | D3a |
| N-B30, N-B31 | Payne's scorecard method (2011); UK DCLG multi-criteria analysis manual (2009) | D6; F-13 (O-2) |
| N-C01, N-C02 | S&P, *General Criteria: Methodology: Industry Risk* (2013); *Key Credit Factors for the Transportation Cyclical Industry* (2014) | S0.2 second round; K11; §10; §12 |
| N-C05 | Census Business Dynamics Statistics, 2023 release | S0.2 second round; K11 Test 2 flag |
| N-C08, N-C09 | BLS producer price and employment series; BTS Freight Transportation Services Index | S0.2 second round |
| N-C11 | BLS Employment Projections, Table 2.11 | K11 Test 1 |
| N-C13, N-C14, N-C15 | Expeditors, J.B. Hunt and Cass 10-Ks | S0.2 second round; K11 Test 3 |
| N-C16, N-C17, N-C20 | Uber, Descartes and Blend filings | S0.2 second round |
| N-C25 | Aurora, commercial driverless trucking in Texas (2025) | S7 |
| N-D01, N-D02, N-D03 | Economic Census concentration tables (2017, 2022); the 2017 note on HHI; the data dictionary | S0.2 second round; K10; A4; §12 |
| N-D04, N-D05 | Census Statistics of US Businesses 2022; Nonemployer Statistics 2022 | S0.2 second round; K10; A4; §8.2 |
| N-D07, N-D08, N-D09 | DOJ/FTC *Merger Guidelines* (2023) and *Horizontal Merger Guidelines* (2010); EU horizontal merger guidelines (2004) | S0.2 second round; W4; §10 |
| N-D13 | Abdel-Raouf, CR4 market-structure bands (reporting Shepherd) | §10 |
| N-D28, N-D29 | Golder and Tellis, *Pioneer Advantage* (1993); CB Insights, *The Top 20 Reasons Startups Fail* (2016) | S0.2 second round; W4; §12 |
| N-D30 | Cass Information Systems 10-K, FY2025 | S0.2 second round; W4 |
