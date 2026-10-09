# Synthesis B: vertical-SaaS selection, fee-from-savings, sizing, freight data and examples

- **Date:** 2026-09-14.
- **Author:** reader-synthesizer B of 2.
- **Covers:** 22 resources from `study_links.md`.
  - 13 have new notes written for this synthesis: R20, R22, R25, R31, R32, R33, R34, R37, R39, R41, R42, R44, R45.
  - 9 had existing notes, which were re-read: R21, R23, R24, R26, R27, R28, R29, R30, R38.
  - All notes are in `research/resource_notes/`.
- **Labels used throughout:**
  - *verified* = read in the source.
  - *inference* = my reasoning.
  - *judgement* = a recommendation for our process.
  - *unverified* = from memory, not checked.
- **Stage tags:** S0-S7 as in the brief.

| R-ID | Short title | Read status | Evidence type |
|---|---|---|---|
| R20 | Tidemark, Picking Your Market | full (public text + 2 charts); rest gated | authority + census data + cases |
| R21 | Emergence, Cloud-Friendly Industry | full | authority/opinion (portfolio review) |
| R22 | Bessemer, Vertical AI Part I | full | authority + unaudited portfolio stats |
| R23 | a16z, VSaaS with AI Inside | full | authority, illustrative arithmetic |
| R24 | Euclid, Market Sizing Part II | full | empirical (about 100 public cos) + opinion |
| R25 | Poyar, 2025 State of B2B Monetization | full (post + PDF pp. 3-7, 13, 19-29) | survey n=240 (self-selected) + framework |
| R26 | Flexport/Petersen interview | full | case (founder) |
| R27 | a16z, Investing in MVMNT | full | case (investor thesis, unsourced numbers) |
| R28 | BVP, Roadmap: Supply Chain Software | full | authority + cited surveys |
| R29 | a16z, Investing in Silo | full | case (thin) |
| R30 | Bushel/Joraanstad interview | full | case (founder) |
| R31 | FAF5 | partial (landing + file inventory) | data |
| R32 | Commodity Flow Survey | full (about) + press release | data |
| R33 | Armstrong 3PL market size | full | data (proprietary estimates) |
| R34 | USDA AgRTQ | partial (landing + PDF pp. 1-3) | data |
| R37 | 2026 3PL Study | abstract-only (gated) | survey (unread) |
| R38 | ATRI Critical Issues 2025 | full | survey n>4,200 (self-selected) |
| R39 | USDA ERS Food Dollar | full (+ chart) | data |
| R41 | Gurley, 10 factors | full | authority/opinion (portfolio) |
| R42 | Euclid, Market Sizing Part I | full | empirical (about 100) + cases |
| R44 | Census concentration tables (2017 + 2022) | full for freight rows | data |
| R45 | OECD digital-intensity taxonomy | partial (abstract, s.4.1, Tables 1/3) | data + method |

---

## 1. Stage map

### S0: Objectives, constraints, team fit; fix knock-outs and weights before looking

**Method: ambition sets the size floors (R42, R24).**
- Steps: declare whether the goal is venture scale or a smaller business, because the floors follow from it.
- Criteria: Euclid wants "a potential path to a $15B TAM / $100m ARR—our beachhead SAM, however, could be as low as 10% of those figures". It concludes the beachhead SOM floor "likely lands in the vicinity of a few hundred million" (R42). Part II says "$100M for a beachhead or $5B at IPO scale" (R24).
- Rationale: "below a certain reasonable revenue potential, the return and dilution profile of venture dollars just won't pencil out" (R42).
- Evidence: about 100 public software companies, with post-IPO survivorship.
- Limitations: the floors are for venture economics only, and Euclid's own two figures disagree ($100M versus "a few hundred million").
- Adaptation (*judgement*): the project has not stated an ambition. Make the SOM floor an S0 parameter and record it before any candidate is scored.

**Method: team and insider access as a declared asset (R27, R29, R30, R28, R22, R41).**
- The sources' wording:
  - R27: "he has lived the problem himself".
  - R29: "on-the-ground experience ... hand-delivering pallets of farm-grown food in a cargo van".
  - R30: "You have to be really nuanced and understand the details of how our culture works".
  - R28: "Teams with substantial industry experience and empathy".
  - R22: "good judgment, a deep understanding of customer needs, effective feedback channels, and a clear grasp of the regulatory landscape".
  - R41: "you also need a world-class entrepreneur".
- Rationale: insiders see the problems and can reach the customers. R30's anti-pattern is capital from outside the culture producing "solutions looking for problems".
- Evidence: cases and authority only.
- Adaptation (*judgement*): in S0, write down our actual access. Which freight roles can we observe, and who can we call? Carry "access" as a scored criterion into S4.

**Method: fix the business-model constraints in advance (R25, R26, R33).**
- The fee-from-savings rule becomes an explicit gate, the CAMP test (R25).
- The pricing fallback is declared: pure outcome pricing, or "Platform fee plus success bonus" (R25).
- The software-only constraint is stated in the knowledge that R26 argues the opposite: "you had to be full-stack. You have to actually do the work".
- R33 shows savings-share fees are already sold by services firms (managed-transportation 3PLs).

**Convergence:** every VC source treats team-market fit as a selection input, not an afterthought (R22, R27, R28, R29, R30, R41).

**Divergence:** the size floors exist only under a venture objective (R24, R42). R20's "Gigantic" presumes one too.

### S1: Define the market and enumerate candidate sub-markets

**Method: industry-code and flow enumeration for both sides (R44, R32, R31, R33, R39, R34, R20).**
- Freight-company side:
  - NAICS 484x trucking, 488510 brokerage and forwarding, 493x warehousing, 492 couriers (R44).
  - A&A intermediary segments (R33): DTM with its sub-segments Freight Brokerage, Intermodal, Managed Transportation and Last-Mile; ITM (forwarding and customs); VAWD; DCC.
- Shipper side:
  - CFS shipper NAICS × SCTG commodity × mode × geography (R32). It covers mining, manufacturing, wholesale, select retail and services, and excludes farms and imports.
  - FAF commodity × mode × origin-destination, which adds agriculture and imports (R31).
  - ERS's 28 food-at-home product accounts (R39).
  - AgRTQ produce commodities and origin regions (R34).
- Classification level: R20 used 4-digit NAICS and notes the "perpetual argument around which level of classification is best".
- Output: a matrix. Rows are shipper groups, columns are freight-company types, and each cell is a candidate sub-market.
- Rationale: official taxonomies make enumeration reproducible and let every later score use the same codes (*inference*).
- Limitations:
  - No single dataset links a shipper group to the specific freight companies it uses. The CFS gives mode only (*inference*).
  - The Economic Census excludes nonemployers (R44).

**Method: walk the value chain to list hand-offs and roles (R26, R27, R23, R24).**
- R26's walk-through: factory → inspection → trucker → consolidator → port → customs broker → ocean carrier → customs broker → trucker → warehouse → retail. "this is a whole system that requires lots of complex coordination."
- R27's chain: "shippers typically turn to brokers, who search for availability, capacity, and pricing information from their network of carriers". Tools are "Excel, paper and pencil, and a telephone".
- R23 lists the office roles still staffed by people (sales, marketing, customer service, finance back office).
- R24's three-axis cube enumerates "the players in your addressable ecosystem, their needs" around a beachhead: vertical expansion, horizontal expansion, and value-chain extension to "suppliers/distributors upstream, customers or their end-users downstream".
- Adaptation (*judgement*): for each matrix cell, draw the hand-off chain and list the roles on both sides. Pains sit on the arrows: documents, payments, waiting charges (R26).

**Method: enumerate by software function (R28, R22).**
- BVP's map (R28): digital infrastructure ("increased digital interoperability" and "transactional pipes for digital bookings"), workflow automation and optimisation, supplier intelligence, developer platforms.
- Named pain points (R28): "procurement, first mile, drayage, customs clearance, and last mile"; "data entry and invoice processing".
- R22 splits workflows into core and supporting, naming "freight procurement for a shipper (i.e. GoodShip)" as supporting.
- Use: a second axis (function) crossed with the industry matrix.

**Method: node choice inside a chain (R29, R30).**
- The hub node: distributors "are at the heart of this supply chain - they are responsible for connecting growers, grocers, restaurants, and even other distributors" (R29).
- "the middle of the supply chain - the agribusiness, the co-op, the retailer, the big grain company, etc. - is the most underserved" (R30).

**Convergence:** R20, R44, R32 and R31 all enumerate on official codes. R26, R27 and R24 all enumerate the actors around a transaction.

**Divergence:** R28 organises by software function, not by freight flow or industry, so a function-first list and an industry-first list must be crossed rather than merged (*inference*).

### S2: Knock-out screen (pass/fail)

**Method: the CAMP fee gate (R25).** "To pull off outcome-based pricing, businesses need outcome consistency, attribution, measurability and predictability (CAMP)". The four questions are quoted in the R25 note.
- Rationale: each question blocks a known failure: bespoke contracts, credit disputes, reliance on customer reporting or proofs of concept, and revenue volatility.
- Evidence: author framework; 5% of 240 vendors price mainly on outcomes.
- Adaptation (*judgement*):
  - Fail outright if the saving cannot be attributed to us (A) or cannot be measured without a customer study (M).
  - Consistency (C) and predictability (P) are scored, not knock-outs.

**Method: budget and day-one value (R28).** "selling to carriers or brokers requires a special product that can demonstrate value on day one, and justify its cost by offsetting operating expenses within these organizations, thus turning opex budget into IT budget."
- Also: "shippers still hold most of the purse strings".
- Adaptation: knock out a candidate if no party in the pair both holds budget and would see the saving on its own P&L (*judgement*).

**Method: the "land of the giants" and concentration knock-outs (R20, R41).**
- R20: "The lower left of the chart is the land of the giants. In these verticals, you are an enterprise solution, or your company will fail."
- R41: "A highly concentrated supplier base will be reluctant to allow a new intermediary in their market".
- Freight-company codes that fail an SMB approach (R44, 2022 top-50 share): couriers (90.9%) and LTL (82.9%).

**Method: software-improvable test (project rule, with R22, R23 and R38 as operationalisation).**
- R23's role screen: "roles where human connection isn't a key benefit, delivering on a core product, or particularly differentiating to the business, are all candidates".
- R22: "just because something can be automated, doesn't mean it should".
- R38's example of what fails: carriers' top issues are macro or regulatory (economy, lawsuit abuse, insurance, parking, English-language proficiency, emissions).

**Method: plumbing readiness (R30, R28).**
- "When we started in 2017, none of the Ag ERPs that are a big part of this space had an API." A tool that needs manual data entry fails when "A spreadsheet could do the same thing" (R30).
- R28 treats "digital infrastructure" and middleware as preconditions.

**Method: minimum size floor (R42, R24).** Apply only if S0 chose venture scale.

**Convergence:** R25, R28 and R23 all require that the value be demonstrable early and credited to the vendor. That is the shared backbone of a fee-from-savings gate.

**Divergence:** a size knock-out is appropriate under venture ambition (R42, R24). Under a bootstrapped ambition it would wrongly kill niches. R20's index lists a "Bootstrapped" category and a "CargoWise: Bootstrapped Legends" case (titles only).

### S3: Desk evidence (size, growth, structure, penetration, labour, cost pools)

**Method: size from locations and ARPU, bottom-up (R20, R42, R24).**
- R20: define the market "by number of locations, initial ARPU, and expansion ARPU".
- R42: "where numbers are available, bottoms-up is best (e.g., number of customers in ICP * ARPA)".
- R24's sanity zones: "$500k-1m ACV / 1-2k customers ... $50-100k ACV / 10-50k customers ... around $5-15k ACV / 200-500k customers"; and "With an absolutel [sic] max of 10k buyers, a $7k ACV isn't going to cut it for a venture-scale outcome".
- R42 warns against sizing from "ROI users receive from the product", which it defines as "dollars saved or generated by customers".
- Adaptation (*judgement*): customer count comes from R44 or the CFS. ARPA comes from the S5 savings estimate × capture share. Total savings is never used as market size.

**Method: fragmentation and concentration (R44 data; R20, R41, R21 criteria).**
- R20's screen: x = number of companies; y = "market share of all but the top 50 companies"; bubble = sales. Zoom filter: "top 50 companies have less than 20% market share".
- R21's threshold: "fewer than 50 companies represent over 80% of revenue" counts as highly concentrated.
- Freight values (2022, R44; top-50 share / firms):

  | Code | Industry | Top-50 share | Firms |
  |---|---|---|---|
  | 48422 | Local specialized trucking | 9.9% | 31,927 |
  | 48411 | Local general freight | 10.5% | 43,243 |
  | 4842 | Specialized trucking | 18.6% | 52,012 |
  | 488510 | Brokerage and forwarding | 34.3% | 17,130 |
  | 484121 | Truckload | 37.4% | 53,705 |
  | 493 | Warehousing | 48.2% | 9,473 |
  | 49312 | Refrigerated warehousing | 73.9% | 719 |
  | 484122 | LTL | 82.9% | 7,675 |
  | 4921 | Couriers | 90.9% | 6,553 |

- R27 adds broker and carrier fragmentation: "more than 17,000 freight brokers ... one-third of the market is served by the 10 largest"; "only about 10% of trucking companies have over six trucks" (unsourced).

**Method: software penetration and digital intensity (R45, R27, R28, R29, R30).**
- R45: transportation and storage and agriculture are "Low" in the OECD global taxonomy in both periods. Transport's software-investment intensity is −0.7; agriculture's is −1.2.
- R27: "more than 60% of the freight brokerage market operates without software, and adoption is even lower for midmarket and SMBs".
- R28: "50% of the largest enterprise shippers in the U.S. still rely on some combination of email and spreadsheets".
- R29: "pencil and paper (really)".
- R30: McKinsey called agriculture the "least digitized".

**Method: labour spend against software spend (R23, R22).**
- R23: "total US software spend ($313bn) was just 3% the size of total labor spend ($10.5 trillion) in 2022". Worked arithmetic: "By saving one worker at $60k per year ... Mindbody could easily capture 10% of this upside, and thus double ACV by an additional $6k."
- R22: software spend is 1% of GDP against 13% for business and professional services.
- Adaptation: size the labour in the roles found in S1 (dispatch, carrier sales, track-and-trace, billing, claims) using occupational wage data. This needs a new data source (*inference*).

**Method: cost and profit pools (R39, R38, R34, R26, R29).**
- R39's industry-group bill shows where value sits in a chain. Transportation and storage is 4.1¢ of the food dollar; the farm share is 11.8¢.
- Carrier economics (R38): "average profit margins were below 2 percent for most sectors ... truckload sector ... -2.3 percent"; non-fuel operating cost "$1.779 per mile"; detention "135.9 million hours annually".
- Priced pains:
  - Reefer produce rates, e.g. $2.56/mile for 501-1,500 miles in Q1 2026 (R34).
  - Demurrage of "About $200 per pallet per day" (R26).
  - "40 percent of perishable food is wasted" (R29, uncited).

**Method: growth and why-now (R20, R28, R30, R44).**
- R20: "they are all views looking towards the past ... make sure you know how you expect your market to grow (and why)".
- R28's drivers: "Massive shocks to the system", and "Increased digitization" with middleware such as Project44 and FourKites.
- R30's pivotal changes: connectivity "largely solved", machinery data, UX expectations.
- R44's growth from 2017 to 2022: brokerage revenue went from $64.9B to $134.9B, and trucking firms from 112,134 to 156,156. Both span the 2021-22 boom, so they are cyclical.

**Method: cyclicality and switching (R21, R34, R38).**
- R21's decelerators: cyclicality ("difficult to build recurring revenue") and migration costs ("In industries such as transportation or manufacturing, software changes can lead to errors, lost revenue and customer dissatisfaction").
- R34's rate series: $3.62/mile in 2022 Q1, $2.23 in 2025 Q4.
- R38: the economy is carriers' number-one issue for the third year running.

**Convergence:**
- Every VC source reads low digitisation plus large manual labour or process cost as headroom (R22, R23, R27, R28, R29, R30).
- R45 confirms the low digitisation with official data.
- R20, R41 and R44 give a common, measurable fragmentation scale.

**Divergence:**
- R45's persistence finding ("sectors which are at the top (resp., bottom) ... tend to remain at the top (resp., bottom)") and R21's migration-cost decelerator say low digitisation also means slow adoption. See §4, T6.

### S4: Score and rank

**Method: Gurley's ten-factor count (R41).** Factors:
1. new experience versus status quo;
2. economic advantages;
3. opportunity for technology;
4. high fragmentation;
5. supplier sign-up friction;
6. market size × penetration;
7. market expansion;
8. frequency;
9. payment flow;
10. network effects.
- Rule: "a 7 or 8 out of 10 would imply that your opportunity of success is much, much higher than if you only match 3 or 4 out of 10."
- Equal weights. The evidence is portfolio experience. Designed for two-sided markets.

**Method: Emergence accelerators and decelerators, producing tiers (R21).** Eight accelerators, including dissatisfaction with incumbents, industry concentration, mobile workforce, value in data and low cyclicality. Two decelerators: privacy and migration costs. No weights. Transportation lands in the second tier "with more hurdles relating to fragmentation and cyclicality".

**Method: the Tidemark bubble plot (R20).** A two-dimensional visual of firm count against fragmentation, with bubble = industry sales. Good for a first sort. Not a full score.

**Method: Bessemer workflow screen (R22).** Automation propensity ("text-and quantitative-heavy"), customer "desire to automate", core versus supporting, work "not being done or being done poorly", horizontal competition.

**Method: BVP supply-chain screens (R28).** Budget, implementation time ("demonstrate value in a matter of days and be live in weeks"), and five qualities, including "Products that offer sticky long-term value, extending beyond short term cost savings".

**Method: a16z MVMNT template (R27).** Four checks: spend size; share of the market without software, by firm size; incumbents "overengineered and cost prohibitive" for the long tail; an attachable fintech layer. Plus team.

**Method: Euclid expansion scoring (R24, R42).** "The ability to grow TAM is more important than TAM itself". Score the vertical, horizontal and value-chain expansion paths.

**Method: CAMP as a scored axis (R25)**, in addition to its role as an S2 gate.

**Method: problem-intensity index (R38).** ATRI's 3/2/1 weighting, normalised with the top issue at 100 (the ICI). It measures votes, not dollars.

**Convergence** (*inference*): taken together, my half's criteria fall into three axes.
1. **Attractiveness to us:** cost pool, customer count and fragmentation, low digitisation, growth and why-now, expansion path, frequency.
2. **Ability to win:** access and insider knowledge, reachability and CAC, implementation speed, plumbing, incumbent weakness, desire to automate.
3. **Fee feasibility:** CAMP, budget holder, day-one value, payment-flow position.

These map onto the "attractiveness × competitiveness" matrices in Agent A's half.

**Divergence:** none of my sources give weights. The only explicit rule is Gurley's equal-weight count.

### S5: Problem discovery and validation before commitment

**Method: insider or lived-experience discovery (R26, R27, R29).**
- Operate as a customer: "Doing this was what made us realize what it took to move freight" (R26).
- Price each pain (demurrage "$200 per pallet per day").
- Look for public data the industry cannot use: "shipping manifests are all public records ... digitize all 300 million bills of lading" (R26).

**Method: talk to everyone, then narrow; sell early (R24).** The funnel runs "IDEA ... talk to everyone, find alignment with #1 problems" → "DISCO ... narrow your beachhead & wedge" → PMF. "Even monetization at this stage is discovery—a dynamic test of willingness to pay."

**Method: a savings assessment as the validation instrument (R28).** Lead "with strong hooks like risk-free POCs or lightweight cost savings assessments that prove their value upfront".
- *Judgement:* this is the S5 test of both the problem and the fee. It measures the saving on real data before any contract.

**Method: structured industry surveys, split by actor (R38, R37).**
- ATRI (R38): a 27-issue list, pick the top three, weight 3/2/1, then an ICI. The split by actor exposes where a problem is felt: owner-operators rank "Broker Issues" first, carrier executives rank it tenth.
- R37 (unread) covers shipper-3PL relationships.

**Method: the role screen (R23)** and the anti-pattern check (R30: "solutions looking for problems").

**Convergence:** R24, R26, R27, R29 and R30 all say problems are found through first-hand contact. The cases credit desk research and third-party reports with little of the discovery.

**Divergence:** R38-style surveys rank by share of votes, not dollars. They screen problems but cannot satisfy the measurable-savings rule on their own.

### S6: Choose a beachhead plus backups; wedge; expansion path

**Method: Euclid's triangulation (R24).** "triangulating what the customer will immediately adopt, what you can build quickly, and the attractiveness of that wedge to support a large business down the road." "make them zealots before widening the funnel."

**Method: BVP's wedge rule (R28).** "leverage automation or optimization as a wedge to provide immediate ROI to customers and thus get in the door quickly. Longer-term ... expand".

**Method: hub node, partner not disrupt (R29, R30).**
- R29: "partnering with and supporting existing distributors, instead of competing with or otherwise 'disrupting' them".
- R30: reach dispersed parties (farmers) through the intermediary's tools.

**Method: a self-imposed focus constraint (R26).** "Let's keep ourselves from getting distracted by every shiny opportunity and just stay focused on certain kinds."

**Method: expansion layers (R23, R20, R24).**
- R23's waves: cloud → cloud + fintech → cloud + fintech + AI, with "Vertical software markets tend to have winner-take-most dynamics".
- R20's expand and extend; its index blurb on control points: "the last tool to be thrown out before an owner ceases operations".
- R24: "As many as 30% of vertical SaaS companies that don't start with payments will add it over time".

**Method: which side goes first in a two-sided pair (R28, R41).**
- R28: shippers "hold most of the purse strings", but brokers or carriers work "as their beachhead market" if value shows on day one. "Either model can work".
- R41: "supplier aggregation is the easy part. Aggregating demand is much harder and more critical."

**Convergence:** start narrow with an immediate-ROI wedge, then expand along a mapped path (R24, R28, R26, R42).

**Divergence:** on the side choice, R41 favours the demand side, R28 is neutral, and R29 and R30 pick the intermediary.

### S7: Record the decision; revisit triggers; iteration

**Data refresh cadences** become revisit triggers:

| Source | Cadence |
|---|---|
| R44 Economic Census | 5-yearly (2017, 2022 available) |
| R32 CFS | 5-yearly (2022 latest) |
| R31 FAF | versioned updates (5.7.1, Aug 2025) |
| R39 Food Dollar | annual (March) |
| R34 AgRTQ | quarterly |
| R38 ATRI | annual (October) |
| R37 3PL Study | annual |

**Assumption triggers:**
- The TAM is a moving target: "It's not the TAM you start with; it's the TAM you exit with" (R42). The growth answer "changes along the way (it should and will)" (R24).
- Pricing norms change fast: "three-in-four software companies made a change to their pricing last year", and customer service went "from unusual to the market standard" for outcome pricing within about 21 months (R25).
- The freight cycle turns (R34 rates; R38 economy).
- New plumbing appears (R30 APIs).
- Regulation shifts (R21 "Dynamic Regulatory Environment"; R38 broker fraud and double-brokering).

**Convergence:** every dated source (R20, R42, R25) warns that its view is backward-looking or will change.

---

## 2. Criteria inventory

| Criterion (normalized) | KO / scored | Axis | Definition & how to measure | Data source / method | Stated by (source wording) | Freight VSaaS note |
|---|---|---|---|---|---|---|
| Addressable cost pool | scored | attractiveness | $ of labour or process cost software can remove per customer × customers | roles × wages; op-cost benchmarks; rates | R23 "saving one worker at $60k"; R22 labour vs software; R29 "massive waste"; R27 "dollars overspent" | ceiling on ARPA under fee-from-savings |
| Customer count (locations) | scored | attractiveness | firms or locations in the candidate | R44 FIRM; R32 establishments | R20 "number of locations"; R24 "ACV * potential customers" | trucking and brokerage: tens of thousands |
| Initial + expansion ARPU | scored | attractiveness / fee | plausible annual fee now and after expansion | S5 savings × capture | R20 "initial ARPU, and expansion ARPU"; R24 zones | derive from savings, not list price |
| Beachhead SOM floor | KO (tunable) | attractiveness | bottom-up SOM ≥ floor | count × ARPA | R42 "few hundred million"; R24 "$100M for a beachhead" | only under venture ambition |
| Expansion path | scored | attractiveness | credible vertical / horizontal / value-chain moves | R24 cube | R42 "ability to grow TAM"; R20 "expanding and extending"; R23 waves | the other side of the pair = value-chain extension |
| Customer-side fragmentation | scored | attractiveness (+ CAC risk) | top-50 share, firm count | R44 VAL_PCT | R20 "Highly fragmented market"; R41 "High Fragmentation"; R21 prefers concentration | see §4, T1 |
| Value-chain fragmentation | scored | attractiveness | fragmentation of the customer's buyers and sellers | R44 on both sides | R20 "fragmented buyers and ... fragmented sellers" | the two-sided definition |
| Concentration ("giants") | KO for SMB go-to-market | ability to win | top-50 > ~80% | R44 | R20 "land of the giants"; R41 "will likely fight"; R21 ">80%" | fails: couriers, LTL |
| Digital intensity / penetration | scored twice | attractiveness (headroom) and ability to win (adoption risk) | software-investment intensity; % without software | R45; R27; R28 | R45 "Low"; R27 ">60% ... without software" | needs a why-now trigger |
| Incumbent mismatch / dissatisfaction | scored | ability to win | incumbents overbuilt or too costly for the segment | interviews, reviews | R21 "Dissatisfaction with Incumbents"; R27 "overengineered and cost prohibitive" | long-tail brokers and carriers |
| Budget holder + day-one value | KO + scored | fee feasibility | payer sees the saving; opex offset | S5 | R28 "turning opex budget into IT budget" | shippers hold budget; carriers need day-one ROI |
| Implementation time | scored | ability to win | days to value, weeks to live | pilots | R28 | EDI/TMS integration burden |
| Plumbing / API readiness | scored (KO if absent) | ability to win | APIs or EDI on systems of record | S5 checks | R30 "none of the Ag ERPs ... had an API"; R28 | ag ERPs, carrier TMS |
| CAMP | KO (A, M) + scored (C, P) | fee feasibility | four questions | R25 | R25 | audits and recoveries score high; rate savings low |
| Payment-flow position | scored | fee feasibility | vendor sits in the money flow | S5 | R41 "Payment Flow"; R20 payments profit pool; R29 factoring/PACA; R27 fintech | freight payment, factoring, audit |
| Automation propensity | scored | attractiveness | text- or quant-heavy office work vs manual | R22; R23 role screen | R22 "highest propensity for automation" | back office, not driving |
| Desire to automate / relationship intensity | scored | ability to win | relationship-bound work resists | S5 | R22 "desire to automate"; R23 "human connection"; R27 "relationship-driven" | brokerage sales resists; back office does not |
| Core vs supporting workflow | scored | ability to win / attractiveness | supporting = less resistance, more horizontal competition | R22 | R22 "freight procurement for a shipper" | shipper procurement named |
| Transaction frequency | scored | attractiveness | shipments or tenders per period | R32; S5 | R41 "Frequency" | regular shippers: high |
| Cyclicality | scored (negative) | attractiveness | volume and rate volatility | R34 series; R38 | R21 decelerator | 2022-25 freight recession |
| Migration / switching cost | scored (negative) | ability to win | cost and risk of changing systems | S5 | R21 names transportation | |
| Regulatory dynamism | scored | attractiveness | frequent rule changes needing software | R38 | R21 accelerator | CSA, broker-fraud rules |
| Value in data / data exhaust | scored | attractiveness | valuable unused data | S5 | R21 "Value in Data"; R26 bills of lading; R38 telematics | |
| Network effects | scored | attractiveness | the n+1000 test | S5 | R41; R42 (Uber) | marketplaces only |
| Supplier sign-up friction | scored | ability to win | cost of onboarding the other side | S5 | R41 | carrier onboarding / vetting |
| Team access / insider knowledge | scored | team fit | named contacts, lived experience | S0 | R26, R27, R29, R30, R28, R22 | |
| Reachability / CAC | scored (KO if extreme) | ability to win | cost to acquire a customer; dispersion | S5 sales tests | R30 "cost of acquisition ... maybe too high"; R24 low-ACV CAC; R21 concentration lowers CAC | farmers: high CAC |
| Hub-node position | scored | ability to win | node connecting most parties | S1 chain map | R29 "at the heart"; R30 "messy middle" | brokers, distributors, elevators |
| Problem intensity (stakeholder votes) | scored | attractiveness | ICI or vote share by actor | our own survey | R38 | votes ≠ dollars |
| Why-now drivers | scored | attractiveness | shocks, new plumbing, AI | desk | R28; R30; R20 "(and why)" | |
| Customer tech posture | scored (segment level) | ability to win | uses modern tools elsewhere | S5 | R26 "Google Analytics ... fax machine" | |
| Durable value beyond savings | scored | fee feasibility (retention) | value persists after the first savings | S5 | R28 "extending beyond short term cost savings"; R25 predictability | see §4, T4 |
| Service requirement (full-stack) | KO (project rule) | other | winners in the candidate do the work | cases | R26 "you had to be full-stack" | see §4, T5 |

---

## 3. Tunable parameters

| Parameter | Values given by sources | Effect of changing it | Suggested default (judgement) |
|---|---|---|---|
| NAICS level for screening | 4-digit (R20); 3- to 6-digit available (R44) | finer levels expose opposite structures, e.g. 484 top-50 28.3% vs LTL 82.9% | 6-digit for the freight-company side; 4-digit for shipper industries |
| Fragmentation bands | "top 50 ... less than 20%" = SMB heaven (R20); ">80%" by <50 firms = concentrated (R21) | moves candidates between go-to-market models | <20% fragmented; 20-80% mixed; >80% concentrated |
| Preferred direction of fragmentation | fragmented good (R20, R41); concentrated good for CAC (R21) | flips rankings | neutral, unless a low-CAC channel or hub exists (§4, T1) |
| ACV × customer-count zones | $500k-1m / 1-2k; $50-100k / 10-50k; $5-15k / 200-500k (R24) | sanity-checks the pairing of customer count and fee | use as a plausibility check only |
| Beachhead SOM floor | "a few hundred million" (R42); "$100M" (R24); "$15B TAM / $100m ARR" (R42) | kills niches if set high | set in S0 from our ambition; if bootstrapped, a much lower floor (*judgement*: tens of millions) |
| Savings capture share | 10% base, 100% extreme (R23); 35% success fee (AirHelp); "25% per recovered chargeback" (R25); gainshares, no % (R33) | revenue vs adoption trade-off | model at 10%, 20% and 35%; validate in S5 |
| Fee structure | 5% of vendors outcome-based now, 25% expected by 2028 (R25); "Platform fee plus success bonus"; "PAYG with a cap" (R25) | risk borne by vendor vs customer | platform fee + success share, capped |
| Pass bar on the marketplace scorecard | 7-8/10 good; 3-4/10 weak (R41) | strictness | ≥7/10 when a marketplace model is in play |
| Survey weighting | top 3, weighted 3/2/1; top issue = 100 (R38) | problem ranking | same instrument, split by actor on both sides |
| Implementation target | value in days, live in weeks (R28) | excludes integration-heavy wedges | ≤4 weeks to first measured saving |
| TAM horizon | 5-10 years (R42) | expansion credit | 5 years |
| Axis weights | none given (Gurley equal weights only) | ranking | attractiveness 35 / ability to win 35 / fee feasibility 30 (*judgement*; revisit after the first run) |
| Data vintage | 2017 vs 2022 census; quarterly AgRTQ; annual ATRI, Food Dollar | staleness | latest edition; note the cycle phase |

---

## 4. Tensions and open questions

**T1. Fragmentation: attractive or costly?**
- For fragmentation:
  - R20: "A VSV should target a market with lots of small and midsize merchants"; "fragmented buyers and ... fragmented sellers".
  - R41: "High buyer and supplier fragmentation is a huge positive".
- Against:
  - R21 prizes concentration because "customer acquisition costs (CAC) can be especially attractive" and word of mouth improves. It placed transportation in tier two with "more hurdles relating to fragmentation and cyclicality".
  - R30 found selling direct to dispersed farmers too costly: "The cost of acquisition in a traditional sales model ... it's maybe too high."
- Candidate resolution (*judgement*):
  - Split the criterion. "Number of buyers and their weak bargaining power" goes on the attractiveness axis. "Reachability and CAC" goes on the ability-to-win axis.
  - Enter a fragmented side through a node that already aggregates it: a hub (R29, R30), brokers aggregating carriers (R27), or payment and factoring flows (R41, R29).
  - Two-sided pairs may ideally be concentrated on the paying side and fragmented on the served side (the R21 note's inference).
- Evidence to settle it: measured CAC and conversion from S5 outreach per candidate, plus R44 counts.

**T2. Start small or go gigantic?**
- R20 says "Gigantic: Big markets have the universal quality of being full of money".
- R42 says "it's okay (perhaps even better ...) to start small… as long as there is a robust path to expansion", and "we like to see a potential path to a $15B TAM ... beachhead SAM ... as low as 10%".
- R41: "if all the other factors are negative, it will not matter that the market is large".
- R26's interviewer: "it's generally easier for a company to start in a smaller market and try to grow that market."
- Resolution (*judgement*): R20's "gigantic" describes the end state (locations × expansion ARPU). Score two separate things: beachhead SOM at high resolution, and expansion-path credibility. Do not score one blended TAM.
- Evidence: a bottom-up SOM and a drawn expansion cube per shortlisted candidate.

**T3. Size by savings or by ARPA?**
- R42 rejects "ROI users receive from the product" as a sizing basis. The project's fee is defined as a share of savings. R23 sizes revenue as a share of savings (10%).
- Resolution: savings is the value ceiling. Revenue = capture share × realised savings = ARPA. Size is customer count × ARPA.
- Evidence: savings assessments in S5 (R28).

**T4. Savings as the hook or as durable value?**
- R28 backs "sticky long-term value, extending beyond short term cost savings". R25's "Predictability" test. *Inference:* once rates or processes are optimised, savings against the baseline shrink and the fee base erodes.
- Resolution: prefer recurring, per-transaction savings (errors, overcharges, detention, wasted labour hours) over one-time savings, and use a platform fee plus a success share.
- Evidence: whether the saving recurs month over month in pilot data.

**T5. Software-only or full-stack service?**
- R26: "Now Flexport is much more than software: We're a managed service, one that's improved by software." R33 shows gainshares are sold by managed-transportation 3PLs, which are services.
- The project's rule is software-only.
- Resolution: keep software-only as the default, but record per candidate whether the incumbent winners are services. If they are, consider "software sold to the service firm" (R29's partner-not-disrupt) rather than competing with it.
- Evidence: S1 competitor map.

**T6. Low digitisation: headroom or adoption drag?**
- Headroom: R27, R28, R29 and R45's "Low" classification.
- Drag:
  - R45: "displaying a higher digital intensity at the beginning of the period positively correlates with increasing intensity over the considered years".
  - R21's migration costs for transportation.
  - R22's "technophobic decision-makers".
  - R30's missing plumbing.
- Resolution: score the criterion twice (headroom and risk) and require a named why-now trigger (R28, R30) plus a day-one-value wedge (R28).

**T7. Which side of the pair to start on?**
- R28: "Either model can work". R41: "Aggregating demand is much harder and more critical". R29 and R30: the intermediary. R27: brokers. R26: shippers (and it became the forwarder itself).
- Resolution: score each side of every pair separately. The beachhead side is the one with the best fee feasibility (CAMP + budget) and the lowest CAC.

**T8. Farmers as customers?**
- Covered in §5 (L-FARM).
- R30 says direct-to-farmer failed on CAC. R39's national numbers make "most of their profit" to shipping implausible.
- Resolution: treat farmers as the end beneficiary. The paying customer may be the handler, distributor or carrier node.

**T9. Appetite for outcome pricing versus reality.**
- R25: "It's still out of reach for 95% of the market". R23: capture 10% "easily".
- Resolution: the CAMP gate plus a hybrid fallback. Treat R23's 10% as an assumption, not evidence.

**T10. VC lens versus project goals.**
- Most sources in this half (R20-R24, R27-R29, R41, R42) optimise for venture outcomes: large TAMs and hyper-growth ("hyper-growth software startup", R28).
- Resolution: keep their structural criteria. Re-derive the size floors from S0.

---

## 5. Lens notes

### L-VSaaS: what the vertical-SaaS literature says makes a good vertical
- Tidemark (R20): gigantic (locations × ARPU), a fragmented market, and a fragmented value chain ("marketplace possible" and "profit pool from payments"). Control points matter.
- Emergence (R21): eight accelerators and two decelerators. Transportation sits in tier two.
- Bessemer (R22): labour spend versus software spend; automation propensity; desire to automate; core versus supporting workflows; stacked products to reach TAM.
- a16z (R23): the three waves (cloud → fintech → AI) raise ARPU; "winner-take-most" dynamics.
- Euclid (R24, R42): bottom-up SOM; ACV × customer zones; the expansion cube.
- BVP supply chain (R28): budget holder, implementation time, "systems of record, not systems of engagement", wedge then expand.
- Shared core (*inference*): many similar, under-digitised customers with a large manual cost; a reachable entry point; a product that proves value fast; room to layer more products (payments, AI labour) later.

### L-FEE: can the fee come out of measured savings?
- The gate: CAMP (R25).
- Base rates: outcome pricing is 5% today and expected to reach 25% by 2028 (R25).
- The fee arithmetic: savings × capture share (R23, 10%).
- A freight precedent: managed transportation earns "a percent of the purchased transportation" and "gainshares where transportation savings are shared" (R33).
- Where the fee is collected matters. It is easier "when you are in the flow of payment" and otherwise risks being seen as a "tax" (R41).
- The sales motion: "lightweight cost savings assessments that prove their value upfront" (R28).
- The moat: the leader's success rate lets it charge more (R25, p. 26).
- The sizing caution: never size from ROI (R42).
- Freight-specific CAMP reading (*inference*, to verify in S5):
  - High attribution and measurability: discrete recoveries such as overcharges, duplicate invoices and accessorial or detention disputes (R38's 135.9M detention hours), and demurrage avoided (R26). These are analogous to R25's "25% per recovered chargeback" and "revenue recovered above a baseline".
  - Low predictability and attribution: rate savings against the market (R34 volatility).
  - Weak for a fee: compliance risk avoided, such as denied-party screening (R26), because the saving is a risk that never materialises.

### L-2SIDED: pairing shippers with freight companies
- Sources that already frame freight two-sidedly:
  - R27's chain (shipper → broker → carrier) and its note on why opacity persists: "carriers benefit from added fragmentation, as shippers' inability to compare prices helps protect carriers' margins".
  - R20's fragmentation on both sides of the value chain.
  - R41's "natural pull on both the consumer and supplier side".
  - R28's budget split between the sides.
  - R38's issue ranking split by actor type. R37 covers the shipper-3PL relationship.
- Data per side: R32 and R31 for shippers; R44 and R33 for freight companies.
- R24's value-chain extension treats the other side as a later expansion.
- *Judgement:* score every candidate as a pair with a sub-score for each side plus a "coupling" score. Coupling = who pays whom, where the payment flows, and who feels the pain (R38 split).

### L-FARM: evidence for and against "farmers lose big chunks of profit to shipping and handling"
**For, or consistent with, the hypothesis:**
- The farm share is only 11.8¢ of the consumer food dollar, and 7.1¢ away from home, where "additional processing and transportation" apply (R39).
- Produce reefer rates run $2.49-2.76/mile at 0-2,500 miles in Q1 2026, and volatility is high ($3.62 → $2.23/mile, 501-1,500 miles, 2022 Q1 → 2025 Q4) (R34).
- "40 percent of perishable food is wasted in the supply chain" (R29, uncited). "cashflow challenges that growers and distributors face" (R29).
- Harvest logistics lose time to synchronisation: "If any of those things are out of sync, then you're waiting" (R30). A labour shortage: "We're only going to have fewer people in agriculture" (R30).

**Against:**
- Transportation and storage are only 4.1¢ of the food dollar across the whole chain (R39).
- Farms buy only 5.1¢ of inputs per food dollar. 3.0¢ is agribusiness, leaving 2.1¢ for all other industry groups, transport included, against a farm gross share of 11.8¢ (R39). *Inference:* farm-paid transport is at most about 18% of farm gross receipts, and realistically much less.
- The farm-side "handling" cost R30 describes is own labour and waiting time, not carrier freight bills.
- Direct-to-farmer software failed on CAC (R30).
- Agriculture is in the lowest digital-intensity group on every available indicator (R45).
- Farm product warehousing is tiny: $1.0B revenue across 411 firms in 2022 (R44).

**Unknowns:**
- Commodity-level transport shares (Ag-FEDS, R39).
- Grain basis and freight embedded in buyer prices (*unverified*).
- Farm-origin freight flows by commodity (R31). The CFS excludes farms (R32).

**Verdict (*judgement*):** national data do not support "most of their profit". The lead may survive for specific perishables, cross-border produce (45% of reported produce truck volume comes from Mexico, R34) or export grain. Test it at commodity level before using it to steer the choice of sub-market.

---

## 6. Freight-specific facts, datasets and worked examples

**Facts:**

| R-ID | Fact (exact) | Source cites its own data? |
|---|---|---|
| R32 | 2022: "12.2 billion tons", "$18.0 trillion"; trucks "8.3 billion tons (68.1%)", "$13.2 trillion (73.5%)"; Customer Pickup "1.4 billion tons ... (about 11.4%)" | yes (survey) |
| R44 | 2022 truck transportation: 156,156 firms, $423.3B, top-4 8.3%, top-50 28.3%; brokerage: 17,130 firms, $134.9B, top-4 9.9%; LTL top-4 40.8%; couriers top-4 87.7% | yes (census) |
| R33 | 3PL market "$323.4 billion in 2025"; DTM $128.3B; ITM $85.9B; VAWD $72.7B; DCC $32.0B; software $4.5B | proprietary, method undisclosed |
| R34 | Q1 2026 produce truck shipments "7.76 million tons"; Mexico 45%; rates $2.76 / $2.56 / $2.49 / $1.50 per mile by distance band | yes (Market News) |
| R39 | farm share 11.8¢; transportation and storage 4.1¢; food services 38.6¢; labour 54.1¢ of the food dollar | yes (ERS model) |
| R38 | detention "135.9 million hours annually"; non-fuel cost "$1.779 per mile"; truckload margin "-2.3 percent"; >4,200 respondents | yes (ATRI research, footnoted) |
| R27 | "$800 billion" of shipper spend; ">60% of the freight brokerage market operates without software"; ">17,000 freight brokers"; "10% of trucking companies have over six trucks" | no (unsourced) |
| R28 | about $25B core supply-chain software; "north of $100 billion" potential; 50% of the largest shippers on email and spreadsheets | BVP's own estimates |
| R26 | demurrage "About $200 per pallet per day"; about 30,000 bills of lading per day; forwarding "about a $1 trillion industry" | no (recollection) |
| R45 | transportation and storage "Low" digital intensity; software-investment intensity −0.7 | yes (OECD) |
| R22 | "freight procurement for a shipper (i.e. GoodShip)" is a supporting workflow | example |
| R21 | transportation in tier two ("fragmentation and cyclicality") | no |
| R25 | AirHelp "35% success fee"; "25% per recovered chargeback" | vendor examples |
| R29 | "40 percent of perishable food is wasted" | no |
| R30 | no ag ERP had an API in 2017 | founder claim |

**Worked examples usable in the process doc:**
- R27 (MVMNT): the four-criterion segment pick. Small and midmarket brokers.
- R29 (Silo): the hub-node pick in produce distribution.
- R30 (Bushel): the "messy middle" pick in grain; the direct-to-farmer failure.
- R26 (Flexport): lived-problem discovery, a technology-posture segment, and full-stack delivery.
- R28 (BVP): the budget and implementation screen.

**Dataset → stage map:**

| Question | Stage | Dataset | Access path |
|---|---|---|---|
| Which shipper industries ship which commodities, by which mode, and how much? | S1, S3 | R32 CFS | census.gov/programs-surveys/cfs (tables by SCTG/NAICS/mode/geography; Public Use File); data.census.gov |
| Which commodity × mode × origin-destination flows are largest, including farm and imports, and how will they grow? | S1, S3 | R31 FAF5 | faf.ornl.gov/faf5/dtt_total.aspx; faf.ornl.gov/faf5/Data/Download_Files/FAF5.7.1_2018-2024.zip |
| How many freight companies of each type, how big, how fragmented? | S3, S4 (R20 screen) | R44 | www2.census.gov/programs-surveys/economic-census/data/{2017,2022}/sector00/EC{17,22}00SIZECONCEN.zip; data.census.gov table ECNSIZE2017.EC1700SIZECONCEN |
| What do transportation firms spend on purchased transport, by mode? | S3 | R44 EC1748PURMODE | data.census.gov / FTP sector48 |
| How big is each intermediary segment, and how is it paid? | S1, S3, L-FEE | R33 | 3plogistics.com U.S. 3PL Market Size Estimates |
| How digital is the sector? | S3 | R45 | OECD PDF, Tables 1 and 3 |
| Where does the food dollar go; what share is transport; farm share by product? | S3, L-FARM | R39 | ers.usda.gov food-dollar summary + Ag-FEDS |
| What does reefer produce trucking cost, and how volatile is it? | S3, S5, CAMP-P | R34 | AgRTQ PDF + datasets page + agtransport.usda.gov |
| What do carriers and drivers say their problems are? | S5 | R38 | NCDOT-hosted PDF (mirror) |
| What do shippers and 3PLs say about each other? | S5 | R37 | 3plstudy.com (registration) |

---

## 7. Gaps and access failures
- **R20:** the page ends in a login or request-access notice. The 2025 update and the census-growth piece are gated. The charts label no freight codes. The "fragmentation up and down the value chain" criterion is never operationalised ("for another day").
- **R31:** the FAF Summary Statistics page is rendered by the app and could not be retrieved, so no FAF headline totals were obtained. The data zips were not downloaded.
- **bts.gov:** returned "Access Denied" to curl. The Census press release was used for the CFS headlines.
- **R37:** not read (registration).
- **R22:** Part IV, "Bessemer's investment framework", is not in study_links.md and was not read.
- **R25:** chart values were read from the text layer. Label-to-bar mapping is inferred for p. 13 and for the 2028 flat and seat shares.
- **R34:** regional and truck-availability sections were not read.
- **R39:** commodity-level transport shares (Ag-FEDS) were not retrieved.
- **R44:** excludes nonemployer owner-operators. Agriculture is outside the Economic Census (*unverified*). EC1748PURMODE was not extracted.
- **Missing across my half:**
  - No source gives weights for combining criteria.
  - No source quantifies CAC per freight segment.
  - No source gives shipper-side software penetration by shipper industry.
  - No source measures freight customers' acceptance of savings-share fees beyond R33's statement that gainshares exist.

## 8. Corrections to study_links.md or existing notes
1. **R20 (study_links.md):**
   - "gigantic, measured as locations x initial ARPU x expansion ARPU" is a paraphrase. The source lists the three quantities with no operator.
   - The page is now partly gated ("To continue reading, login or request access below."), and a "Picking Your Market (2025)" update exists.
2. **R33 (study_links.md):** the four listed segments sum to $318.9B. The page's $323.4B total also includes a fifth row, "Contract Software/Systems" $4.5B. The page was "updated April 20, 2026".
3. **R45 (study_links.md):** "Table 1 placing 'Transportation and storage' ... in the low group" is loose.
   - Table 1 is per indicator. The "Low" global class is in Table 3.
   - Transportation is not bottom on every indicator (online sales = 1.3).
   - "bottom quartile on every indicator" is correct for agriculture.
4. **R41 (page copy):** contains an injected, non-Gurley sentence ("my car tax check ..."). Do not quote it.
5. **R32 (press release used for headlines):** "The South region shipped 1.9 billion tons (40.4%)" is internally inconsistent with the 12.2B-ton total. Check the tables before citing regional figures.
6. **R34 (PDF):** the diesel sentence reads "During first quarter 2025" in the Q1 2026 issue. It is a source typo.
7. **R37 (study_links.md):** names Penske Logistics as co-author. The landing page shows "Langley" and "NTT DATA" but not "Penske". Unverified here.
8. **R24/R42 (source-level, not a note error):** Euclid's beachhead floor differs between Part I ("a few hundred million") and Part II ("$100M").
9. **R44 (study_links.md):** the claim that "the 2022 edition is on data.census.gov" is confirmed. EC2200SIZECONCEN.zip is on the Census FTP and was used here.
10. **Existing notes R21, R23, R24, R26, R27, R28, R29, R30, R38:** no factual errors found on re-reading.
