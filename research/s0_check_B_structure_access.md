# S0 check B: market structure, SMB access, expansion and weights

> **What this is:** an evidence check of the founders' first S0 decisions (`submarket_selection.md` §4 S0) on five questions: fragmentation and incumbents (B1), reaching SMBs directly (B2), having enough businesses (B3), carrying learnings to other markets (B4), and the 40/45/15 weight split (B5). A second check (check A) covers the $10M target, growth and valuation benchmarks, SMB churn and CAC figures, and fee-share percentages. Those are not repeated here.
> **Date:** 2026-09-14. **Status:** input to S0. It decides nothing.
> **Labels:** *verified* means read at the source; the quote is copied from the page or from a file downloaded and converted to text. *assumed* means a secondary summary, memory, or a source that could not be opened. **[our calc]** and **[our call]** mark this document's own arithmetic or judgement. R-IDs are the reading notes in `research/resource_notes/`. N-B IDs are new sources, listed in §5.

**The founders' S0 text (verbatim):**
> "I believe a highly to medium fragmented market with few incumbents is our best bet. This should be small to medium scale, where we can practice freight savings to eventually scale or transfer to other subsequent markets. We want medium scale really, too small makes this not worth the costs. We want to be able to net $10 Million from this excursion, within 5 years. Meaning the Market Share must accomodate for this. Small to Medium Businesses are more accessible as well, since we can reach out directly. But we would want enough businesses to be in the market/segment so if one avenue fails we can continue to reach out to others. 100 Point Weight Split: 40 Market Size; 45 Many Businesses, Fragmentation; 15 Opportunity for Growth, how learnings in this market can apply to other markets so we can go Vertical after this Horizontal SAAS has been built."

**Ambition clarified by the founders (relayed 2026-09-14, verbatim):** "$10M Revenue, also just a $10M valuation as well. It could be $250K-$1M Profit I'd be more than happy." Any of these, within five years, counts:
- **Floor:** $250K-$1M profit a year.
- **Middle:** a $10M valuation, meaning a few $M of ARR.
- **Stretch:** $10M of revenue.

This is a small-to-medium business, between Cohen's indie threshold (R19) and Euclid's venture floors (R42: a beachhead SOM "in the vicinity of a few hundred million"; R24: "$100M for a beachhead"). This document judges "big enough" and "enough businesses" against this band, not against the venture floors.

---

## 1. Summary

The founders' instincts are partly in line with documented vertical-SaaS practice, but three of the five need rewording before S0 is frozen.

**Fragmented customers (B1): partly supported.** This is one of two well-documented vertical-SaaS archetypes: fragmented SMB verticals (Tidemark R20, N-B09; Bessemer N-B08; a16z's freight pick R27). The other archetype, concentrated high-contract-value verticals such as Veeva, nCino and Guidewire, is just as well documented (R21, R24, N-B08). Neither is "the norm". At the founders' scale, Constellation Software's letters show that small, even "tiny", niche markets produce good businesses (N-B12).

**Few incumbents (B1): not supported as a selection criterion.** Some sources favour it (Thiel N-B13; Cohen R19). Others read a crowded market as a sign of demand (Paul Graham N-B14) or treat several viable competitors as normal (Constellation N-B12). What the cases actually show is proven spend plus weak, legacy or absent software in one workflow. Toast entered against two incumbents with about 25% share each (N-B19). In freight, small brokers already choose among several TMS products (N-B04).

**Reaching SMBs directly (B2): partly supported.** Founder-led direct selling is the documented start. Every scaled case then added a channel partner (Toast), a free product (Motive) or payments. The smallest freight firms are both the least able to pay and the most likely to exit: active broker authorities fell by 3,104 in 2024 (N-B04).

**Enough businesses (B3): partly supported.** Every source wants a beachhead big enough for the goal, plus backups. But the sources measure "enough" in revenue, not in headcount, and warn that a segment that is too big loses word of mouth (Aulet N-B17; Moore N-B16). At the founders' scale, most freight-company segments clear the count bar if revenue per customer is about $6k or more a year [our calc].

**Transfer to other markets (B4): partly supported, but mislabelled.** A freight product is already vertical SaaS. Moving it into adjacent sub-markets is horizontal expansion in Euclid's terms (R24). ServiceTitan shows this works when the segments share a customer type or workflow, and that it often takes acquisitions (N-B20).

**The 40/45/15 weights (B5): not supported.** Putting 85 of 100 points on size plus count is far above every weighted scorecard found; those give size about 10-25%. Only Tidemark's unweighted list of attributes has a similar emphasis. It counts the number of businesses twice, because market size ≈ customers × revenue per customer (R42; N-B31). It also leaves out pain, ability to pay, reachability, competition, team fit and fee feasibility.

---

## 2. Findings by question

### B1. "A highly-to-medium fragmented market with few incumbents": is this the norm for vertical SaaS?

These are two separate claims and are checked separately:
- **B1a. Fragmented customers:** many small buyers, and no dominant firms among them.
- **B1b. Few incumbents:** few software competitors, or few firms already doing the job.

#### B1a. Fragmented customers

**Evidence for (vertical SaaS favours fragmented SMB markets):**
- Tidemark, *Picking Your Market* (R20, *verified*): the ideal vertical is "Gigantic", has a "Highly fragmented market" and a "Highly fragmented value chain". "It is challenging to build a business in a market where SMBs are fighting over the leftovers of large enterprises. A VSV should target a market with lots of small and midsize merchants."
- Tidemark, *Truths about Vertical SaaS* (N-B09, Dave Yuan, undated, partly gated, *verified*):
  - "Most verticals are highly fragmented, and the end customers are typically small business merchants."
  - "Leaders in horizontal software markets struggle to get to 20% market share, whereas leaders in many vertical & SMB markets can exceed 40%+ market share."
- Bessemer, *Ten lessons from a decade of vertical software investing* (N-B08, Feinstein and Rea, 18 Jul 2022, *verified*):
  - "Mindbody, Clio, and Weave found their path to market leadership by starting in the SMB segments overlooked by incumbents."
  - "By focusing on a vertical market, these companies are able to trade market size for market share and in some cases achieve 50%+ market penetration."
- a16z on MVMNT (R27, 2022, *verified* quote; the figures themselves are unsourced): picked "midmarket and small freight brokers" because "more than 60% of the freight brokerage market operates without software", and enterprise tools "are overengineered and cost prohibitive for the small to midsize long tail of brokers".
- Gurley (R41, 2012, *verified*, written for marketplaces): "High buyer and supplier fragmentation is a huge positive for an online marketplace."
- Constellation Software, letter covering 2009 (N-B12, Mark Leonard, dated 25 Mar 2010, *verified*): "We have been a serial acquirer of inherently attractive small vertical market software businesses in a large number of different verticals", run by managers "who have built industry leading (albeit small) vertical market software businesses with great economics".

**Evidence against, or qualifying (concentrated and high-contract-value verticals are just as documented):**
- Emergence (R21, 2013, *verified*) prefers concentrated industries, "in which fewer than 50 companies represent over 80% of revenue", because "customer acquisition costs (CAC) can be especially attractive" and "industry concentration helps with word of mouth". It puts transportation in its second tier, with "more hurdles relating to fragmentation and cyclicality".
- Euclid (R24, 2025, *verified*): the high-contract-value zone ("$500k-1m ACV / 1-2k customers (e.g. Palantir, Veeva, Guidewire, Trade Desk, Manhattan Associates)") "is dominated by vertical businesses".
- Bessemer (N-B08, *verified*):
  - "There are only about five thousand banks in the US. Without six-figure deals, our portfolio company would have never achieved IPO scale."
  - "In some verticals, there are too few logos to build a big SMB/mid-market vertical software business."
  - Lesson 7: "Many verticals require a move up-market to sustain growth."
- a16z, *Fintech Scales Vertical SaaS* (N-B11, 4 Aug 2020, *verified*): fintech "unlocks new verticals where previously the total addressable market (TAM) for software was too small and/or the cost of acquiring customers was too high". Many fragmented SMB verticals only work once a payments layer is added.
- Bushel (R30, *verified*): selling direct to dispersed farmers failed: "The cost of acquisition ... it's maybe too high."
- Constellation, letter on 2016 (N-B12, *verified*): "We seek out vertical market software businesses where motivated small teams composed of good people, can produce superior results in tiny markets. These markets are usually characterised by a gradually consolidating customer base". Small VMS niches are often *consolidating*, not fragmented.
- ServiceTitan S-1 (N-B20, Nov 2024, *verified*): even a leader in a fragmented SMB vertical excludes the smallest firms: "we do not focus on down-market trades businesses, which we define as having five employees or fewer."

**Freight check (both sides are fragmented, with exceptions):**
- **Trucking.** "91.5% of carriers operating 10 or fewer trucks and 99.3% operating fewer than 100 power units" (ATA, 2024 data, N-B01, *verified*; ATA is an industry association).
- **Brokers.** 25,334 active broker authorities at the end of 2024 (Brush Pass Research, N-B04, *verified*). The census counts 17,130 employer firms in freight arrangement in 2022, with a top-50 revenue share of 34.3% (R44).
- **Concentrated corners.** LTL (82.9%) and couriers (90.9%) fail knock-out K10 (R44; `submarket_selection.md` §8.2).
- **Customer turnover is high.**
  - Brokers: "2024 closes with 3,104 fewer freight brokerages", and 5,409 fewer since January 2022 (N-B04, *verified*).
  - Carriers: 88,000 trucking authorities were revoked in 2023 (N-B03, *assumed*: a secondary compilation citing FMCSA data via TruckInfo.net). The for-hire carrier population was "largely unchanged in 2025" (N-B02, *verified*).
- Constellation's letter covering 2013 gives the test for this kind of turnover (N-B12, *verified*): "Sometimes the higher churn is because the clients' switching costs are low. Sometimes the higher churn is because lots of new potential clients are being created, and old ones are going bankrupt and merging. If it is the latter, these software businesses may be very attractive. If it is the former, then the software businesses are likely to be unpleasant".

#### B1b. Few incumbents (few software competitors)

**Positions that favour few or no competitors:**
- Thiel, *Zero to One* (2014) (N-B13, *assumed*: verbatim text from quote sites; the book was not read):
  - "The perfect target market for a startup is a small group of particular people concentrated together and served by few or no competitors."
  - "Every startup should start with a very small market. Always err on the side of starting too small."
- Cohen (R19, *verified*): "In a small market, you might not have many viable competitors, lessening the importance of differentiation."
- Tidemark (N-B09, *verified*), on small vertical markets: "This is a bug, but also a feature—fewer competitors are being funded to compete."
- Bushel (R30, *verified*): the grain-handling middle was open because "it's not sexy ... There's just so few software investments".

**Positions that read competitors as proof of demand, or absence as a warning:**
- Paul Graham, *How to Get Startup Ideas* (N-B14, Nov 2012, *verified*):
  - "A crowded market is actually a good sign, because it means both that there's demand and that none of the existing solutions are good enough."
  - "It's exceptionally rare for startups to be killed by competitors — so rare that you can almost discount the possibility."
- Cohen (R19, *verified*) asks for proof of budget rather than an empty field: "You want to target companies who outsource this particular problem to outside vendors."
- Andreessen (N-B15, 25 Jun 2007, *verified*): "When a great team meets a lousy market, market wins." What matters is demand, not the absence of rivals.
  - A widely quoted line attributed to Andreessen says that claiming "no competition" signals "a terrible market". It is **not** in the essay it is usually tied to, so it is not used here (*unverified*).
- Constellation, letter covering 2014 (N-B12, *verified*): "most vertical markets have several viable competitors who exhibit little correlation between their profitability and relative scale."
- Constellation, letter covering 2015 (N-B12, *verified*): "Some markets have rabid venture-backed competitors with a grow-at-any-cost ethos, while others have a few rational competitors intent on making a decent living." The attractive case is *rational* competitors, not *no* competitors.
- Incumbents can block entry (Bessemer N-B08, *verified*): "Three 40+ year old software companies—CDK, R&R, and Cox—have chased away dozens of new entrants."
- White space can exist inside a crowded vertical (N-B08, *verified*): "Banks had plenty of software vendors (including massive incumbents like FIS and Ellie Mae) but no one was paying attention to the commercial loan origination process."
- Displacing legacy incumbents is the documented pattern:
  - Toast's founders "could use cloud delivery to constantly make their software better than the legacy on-premise incumbents" (N-B08).
  - Bessemer's 2015 memo: Toast faced "two large incumbents, Micros and NCR, each accounting for roughly 25% market share" (N-B19, *verified*).
  - Emergence lists "Dissatisfaction with Incumbents" as an accelerator (R21).

**Freight check on incumbents (*verified* unless marked):**
- Small brokers already have several software options:
  - Brush Pass contacted 895 "micro-cap" brokerages ("under $10m in annual gross revenue"). It reports that "McLeod leads the pack" alongside "in-house or homegrown proprietary systems", followed by "Truckstop's ITS Dispatch" and Ascend TMS (N-B04, 2 Apr 2025; the chart's shares were not given in text).
  - Aljex had about 400 broker customers when Descartes bought it (N-B24).
  - Venture-funded entrants: MVMNT (N-B26), Rose Rocket (N-B27), Alvys (N-B28).
- In many jobs the real incumbent is labour, spreadsheets and the broker's service itself: "the majority of this process happens with Excel, paper and pencil, and a telephone" (R27; *assumed* as a market fact, since it is unsourced).
- **So "few incumbents" is false for small-broker TMS as a category. It may be true for specific savings jobs** (freight audit, detention billing, claims), which were not checked here. That belongs in the S3 fact sheet, item 9 ("Competitors and substitutes").

**Verdict B1:**
- **Fragmented customers: partly supported.** It is one of two documented vertical-SaaS archetypes and is the one most VC essays on SMB vertical SaaS favour. It is not the only norm. At the founders' scale, Constellation shows that small, concentrated or consolidating niches also make good businesses.
- **Few incumbents: not supported as stated.** The sources split, and the absence of competitors is ambiguous: it can mean no demand or no budget. The better-documented signal is proven spend on the problem, with incumbents that are weak, legacy or absent in one specific workflow.

**Implications for S0:**
1. Keep fragmentation (A4). Score it for each side separately with the census screen (R44, §8.2). Note that customer-base turnover in freight is high, and record it under durability (A7).
2. Replace "few incumbents" with W4 (competition and substitutes), scored on how weak the incumbents are and on evidence that customers already spend on the problem: they pay a 3PL, auditor or broker to handle it (R19, R33).
3. Scored this way, "few incumbents" stops being a reason to pick a market and becomes a hypothesis to test for each job.

---

### B2. "SMBs are more accessible since we can reach out directly"

**Evidence that founder-led direct outreach works early:**
- Aulet (R15, *verified*): "You want to deal directly with customers when starting out, rather than rely on third parties to market and sell your product, because your product will go through iterations of improvement rapidly, and direct customer feedback is an essential part of that process."
- Toast, Bessemer Series B memo (N-B19, Bennett and Ahlgren, 14 Dec 2015, *verified*):
  - "Toast is primarily selling direct to SMBs today via an inside sales force".
  - Co-founder Aman Narang led sales although he had "never sold anything in his life".
  - "6-8 month payback on sales efforts".
- ServiceTitan (N-B20, *verified*): "Our founders, Ara Mahdessian and Vahe Kuzoyan, are the sons of trades business owners." Their first access came through a network they had lived in.
- MVMNT (R27, *verified*): the founder "lived the problem himself ... working as a broker".
- Tidemark (N-B09, *verified*):
  - "The software buyer for these merchants is often the owner, or sits next to the owner, and is a significant user of the software."
  - "Most vertical markets are local, and local merchants _talk_."
- In freight, the prospect list is public. Brush Pass built its sample of 895 micro-cap brokers from "the FMCSA census file of active freight brokerages" (N-B04, *verified*).

**Evidence on what changes at scale, and against relying on direct outreach alone:**
- Tidemark (N-B09, *verified*): "Having strong product-led growth, performance marketing, or an efficient salesforce (inside and local) is critical."
- Toast (N-B19, *verified*): a supplier partner, Gordon Food Service, was "accounting for about 25% of Toast bookings" by 2015.
- Bushel (R30, *verified*): one-to-one selling to dispersed customers had an acquisition cost "maybe too high".
- Emergence (R21, *verified*): concentration, not fragmentation, lowers CAC and helps word of mouth.
- a16z (N-B11, *verified*): adding fintech can "increase revenue per customer by 2-5x". That is what makes high-CAC SMB verticals pay back.
- Cohen (R19, *verified*): an internet funnel needs "10,000 Impressions -> 1 paying customer" for $30-100/month products.
- Motive (N-B22, Contrary Research, 27 Jul 2023, *verified*): it grew through a free product rather than outreach. The driver app, released December 2013, "was downloaded one million times in its first four years". Paid products followed, timed to the ELD mandate, which Contrary says took full effect in 2017.
- Bessemer (R28, *verified*): selling to carriers or brokers "requires a special product that can demonstrate value on day one, and justify its cost by offsetting operating expenses".
- Ability to pay at the small end of freight:
  - Truckload profit margin of -2.3% (R38, via `submarket_selection.md` §4 S3).
  - ServiceTitan's exclusion of firms with five employees or fewer (N-B20).

**Channels vertical SaaS uses to reach SMBs, with freight analogues:**

| Channel | Documented example | Freight analogue (to check in S3/S5) |
|---|---|---|
| Founder network, direct selling | ServiceTitan founders from trades families (N-B20); MVMNT's founder, an ex-broker (R27); Toast co-founder on inside sales (N-B19) | Team inventory (W2). The FMCSA census gives contact records for every carrier and broker authority (N-B04) |
| Inside sales | Toast, 2015: "6-8 month payback" (N-B19) | Phone and email to brokers and carriers; check-A holds the CAC figures |
| Supplier or distributor partner | Gordon Food Service, about 25% of Toast bookings (N-B19) | Factoring firms, fuel-card issuers, insurers, load boards. Truckstop, a load-board company, sells ITS Dispatch, a leading small-broker TMS (N-B04) |
| Trade associations | none found in the general vertical-SaaS sources | OOIDA: "More than 150,000 members", owning or operating "more than 240,000" trucks (N-B06, *verified*). TIA: "more than 1,700" members (N-B07, *assumed*: third-party profile; tianet.org blocked the fetch) |
| Free tool / product-led growth | Motive's free logbook app (N-B22); MVMNT's free TMS, monetised through financial services (N-B26) | Ascend TMS appears among the leading small-broker TMS (N-B04) |
| Embedded payments | a16z: 2-5x revenue per customer (N-B11); "As many as 30% of vertical SaaS companies that don't start with payments will add it over time" (R24) | Factoring, quick-pay and freight payment (R27, R29). A fee taken inside a payment is not seen as "a 'tax'" (R41) |

**Freight population facts (for B2 and B3):**

| Fact | Figure | Source | Status |
|---|---|---|---|
| Carriers with 10 or fewer trucks | 91.5% (99.3% have fewer than 100 power units), 2024 data | N-B01 ATA, 28 Aug 2025 | *verified*; industry association |
| For-hire carriers with 10 or fewer trucks; single-truck share | 97%; 70% | N-B05 FreightWaves, 17 Mar 2026, citing ATA | *verified* at FreightWaves; underlying source not read |
| Active US motor carriers | about 580,000, mid-2025 | N-B05, citing FMCSA | *assumed* (secondary) |
| Trucking companies with more than six trucks | "only about 10%" | R27, 2022 | *assumed* (unsourced) |
| Active broker authorities | 26,216 (31 Aug 2024); 25,334 (end of 2024); 25,087 (Apr 2025) | N-B04 Brush Pass for 2024 (the end-2024 count uses Carrier Details data); the Apr 2025 figure comes via N-B03, citing Brush Pass | 2024 figures *verified*; Apr 2025 *assumed*; "active" is not defined |
| Broker net exits | -3,104 in 2024; -5,409 since Jan 2022; an average of 257 closures a month in 2024 | N-B04 | 2024 and since-2022 figures *verified*, and re-checked by the coordinator on 2026-09-14. The 257-a-month figure was not found on re-check, so treat it as *assumed* |
| Employer firms: freight arrangement; truck transportation | 17,130; 156,156 (2022) | R44 | *verified*; payroll firms only |
| Carrier exits | 88,000 authorities revoked in 2023; net loss of about 10,000 carriers in H1 2024 | N-B03 | *assumed* (secondary compilation) |
| 2025 carrier population | "largely unchanged ... compared to the previous year" | N-B02 Trucking Dive, 12 Jan 2026 | *verified* |

**Verdict B2: partly supported.**
- *Supported:* founder-led direct outreach is the documented way to win the first customers. In freight it is cheap to start, because every carrier and broker authority is on a public list.
- *Not supported:* no source shows direct outreach alone scaling to thousands of SMB customers. The cases that scaled added a channel partner (Toast), a free product tied to a regulatory deadline (Motive), or payments.
- *Freight-specific cautions:* the smallest firms have the thinnest margins and the highest exit rates. Scaled SMB leaders often skip the very smallest firms (ServiceTitan).
- At the founders' scale (hundreds to low thousands of customers; see the B3 table), inside sales plus one channel partner is plausible **[our call]**, not proven.

**Implications for S0:**
- Score reachability (W1) for each side, naming the channel.
- Decide a firm-size floor. For example, are owner-operators with one truck in scope or not?
- Treat "we can reach out directly" as an S5 test: time taken, and replies received per 100 contacts, recorded as W1 evidence (§4 S5 step 1 already says recruiting ease is evidence).

---

### B3. "Enough businesses so if one avenue fails we can reach others"

**What the sources say about beachhead size and depth:**
- **Aulet, Step 4** (N-B17; R16, *verified* unless marked):
  - TAM definition: "The TAM is how much annual revenue you would accumulate if you achieved 100% market share" (d-eship.com Step 4 page).
  - Purpose of the step: "To make sure your Beachhead Market is not too big or too small" (2024 edition, front-matter preview).
  - Worksheet 04.4 asks all three of:
    - "Is the market big enough to be interesting?"
    - "Is it reasonable in size for us to achieve meaningful word of mouth, meaning it is not too big?"
    - "Is it possible to get to positive cash flow in this market in a reasonable period of time (typically three years ...)?"
  - Worksheet 04.3 row 7: "Estimated time to achieve 20 percent market share".
  - Step 2 checklist (R16): "less than a billion and more than a few hundred thousand".
  - SensAble's own beachhead TAM was about "$10M-$15M per year" (Step 4 page).
  - **The often-quoted range "$20-100M/year" was not found in any primary Aulet text available here.** It appears in book reviews (N-B18, Brikman 2022: "typically, $20-100M/year"). *Assumed.* The book's Step 4 chapter was not accessible: O'Reilly returned 403, and the archive.org copy is lending-only.
- **Moore** (N-B16, *verified* on Moore's own blog; before this only a podcast summary was available, R17): the next target should be "big enough to matter but small enough to lead, and as always, a good fit with your crown jewels". Pragmatists buy on references "with customers they know and can reference" (R17).
- **Aulet's word-of-mouth condition** (R16, *verified*): "If your end users don't talk to each other—if they are separated by large distances, for example—you're going to have a hard time building up sales across the full group of end users."
- **Cohen** (R19, *verified*):
  - B2B: "100k is sufficient".
  - "1,000 paying customers is the minimum needed for a sustainable, small company" at $30-100/month.
  - Exception: "a high-price-tag product in a small niche can be a fine company".
- **Thiel** (N-B13, *assumed*: book not read): PayPal targeted eBay's "few thousand high-volume 'PowerSellers'" and was "serving 25% of them" after three months.
- **Paul Graham** (N-B14, *verified*): "You can either build something a large number of people want a small amount, or something a small number of people want a large amount. Choose the latter."
- **Euclid** (R24, *verified*):
  - Customer count and contract value trade off along an "inverse power-law" ("half the customer count would have a 72% higher ACV").
  - "With an absolutel [sic] max of 10k buyers, a $7k ACV isn't going to cut it for a venture-scale outcome." That is a venture yardstick, far above the founders' band.
- **Where to Play** (R40, *verified*): "72% of firms in our sample" changed their initial market within three years. Broad entrants whose options "tend to be closely related" did better.
- **Constellation** (N-B12, *verified*):
  - "the average business that we buy costs something less than $3MM" (letter covering 2011).
  - "The biggest is 307 employees, and the average business unit currently has 44 employees" (letter covering 2012).
  - As of Dec 2016, 158 of 193 business units had fewer than 100 employees (letter on 2016).
  - "your niche has to be the clients that you already have ... if the underlying attrition of the industry that you are serving is low, this can be a very good business model" (letter covering 2015).
- **Freight exit comparables** (*verified*):
  - Aljex, a broker TMS with "400 customers in North America", was sold to Descartes for "$32.4 million in cash" (N-B24, 1 Feb 2018).
  - BoxTop, serving "small- to mid-sized logistics services providers", was sold for about "$US 13 million" (N-B25, 11 Jun 2024).
  - Both sit near the founders' "$10M valuation" goal, which suggests exits exist at that scale.

**The tension, and how the sources resolve it:**
- *Many prospects give resilience.* This is what the founders want, and R40's data on keeping related backups supports it.
- *A small, connected segment is easier to dominate.* Word of mouth and references pass between peers (R16, R17, N-B16, Aulet's worksheet 04.4 "not too big").
- The sources reconcile the two by separating:
  - **depth inside one segment:** enough reachable prospects to hit the revenue goal;
  - **breadth across segments:** one or two *related* backup segments (R40), or Moore's next "adjacent" pin (N-B16).
- Raw business count measures neither. The process already covers breadth in S6 (backups and growth options).

**Ambition-adjusted arithmetic [our calc].** Customers needed = target ARR ÷ ARPA (average annual revenue per account). Firms needed in the segment = customers ÷ market share. Three things are assumptions here:
- the ARPA levels;
- the 20% share, from Aulet's worksheet row;
- the 40% share, from Tidemark's "40%+" for leaders.

Check A covers what revenue the profit floor implies.

| ARPA per customer per year | Customers for $3M ARR | Customers for $10M ARR | Firms needed at 20% share ($3M / $10M) | Firms needed at 40% share ($3M / $10M) |
|---|---|---|---|---|
| $1,200 ($100/month, e.g. an owner-operator tool) | 2,500 | 8,333 | 12,500 / 41,667 | 6,250 / 20,833 |
| $6,000 ($500/month, e.g. a small-carrier or small-broker tool) | 500 | 1,667 | 2,500 / 8,333 | 1,250 / 4,167 |
| $24,000 ($2,000/month, e.g. a mid-size broker, or a savings-share fee) | 125 | 417 | 625 / 2,083 | 313 / 1,042 |

Compare these with the freight populations: about 25,000 active broker authorities (N-B04); 17,130 freight-arrangement employer firms, 53,705 long-distance truckload firms and 52,012 specialized trucking firms (R44, 2022); and about 580,000 active carriers (N-B05, *assumed*).

What the arithmetic shows **[our calc]**:
- At an ARPA of $6k or more, nearly any freight-company segment with a few thousand firms clears the count bar for the founders' band.
- Only at very low ARPA does count become binding. That is exactly where customers are least able to pay and most likely to exit.
- The implied beachhead TAM for $3-10M ARR at 20% share is about $15-50M a year. That sits at the low end of the secondary $20-100M range and above SensAble's $10-15M.

**Verdict B3: partly supported.**
- *Supported:* every source wants a beachhead big enough for the goal, plus related fallbacks.
- *Not supported:* using a raw count of businesses as the measure of resilience. The sources measure "enough" in revenue (TAM or fee potential). They add a ceiling ("not too big") so that word of mouth still works, and they get resilience from related backup segments.
- At the founders' scale, the count of firms is rarely the binding constraint in freight. ARPA, reachability and customer survival are.

**Implications for S0:**
- Turn "enough businesses" into the K5 floor, stated in beachhead fee potential. The default is about $15-50M a year **[our calc]**, to be revised once check A's revenue path is known.
- Add a word-of-mouth ceiling to K2 (R16).
- Keep the S6 rule of one or two related backups.

---

### B4. "Learnings apply to other markets so we can go Vertical after this Horizontal SaaS"

**Definitions:**
- **Vertical vs horizontal (Euclid R24, footnote 2, *verified*):** "'vertical' and 'horizontal' come from a business matrix that visualized products sold as rows and industries served as columns. So by launching net new products, you are moving vertically on that chart. By venturing into new industries, you are moving horizontally across that chart."
- **Vertical SaaS (a16z N-B11, *verified*):** software for "a specific industry, such as construction or fitness", where customers prefer "purpose-built software for their specific industry and use cases". Constellation uses the same sense: "vertical market software ('VMS')" (N-B12).
- **Horizontal SaaS:** software for one business function used across many industries (accounting, CRM, email). The sources read here define it only by contrast, as above. The examples are common usage (*assumed*).

**What the founders' sentence most likely means.** Software built for a freight sub-market is already **vertical SaaS**. The plan the founders describe elsewhere is: start in one freight sub-market, "practice freight savings", then "scale or transfer to other subsequent markets". In the sources' terms that is **vertical SaaS followed by horizontal expansion**, meaning the same product taken into adjacent sub-markets:
- Euclid's horizontal axis (R24);
- Moore's bowling alley (R15, citing Moore);
- Aulet's leverage criterion (R16).

The sentence therefore appears to swap the two words. A second reading is possible: build a *horizontal capability*, such as a savings-measurement engine, and then specialise it for each freight sub-market. The founders should say which they mean (§4).

**The three expansion axes (R24, *verified*):**
- **Vertical:** "selling net-new products into your existing industry/customer base".
- **Horizontal:** "selling existing product lines into net-new customer verticals".
- **Value-chain:** "selling into ecosystem partners of current customers".

**Evidence on expansion:**
- **Moore** (N-B16, *verified*): the next target is "an _adjacent_ process owner, someone for whom your chasm-crossing sponsor would make a good reference. This lowers the bar for how problematic the use case may be because there is already some proof that the solution will work." Moore's own "bowling alley" text was not read; secondary summaries describe adjacent niches as sharing buyers or use cases (*assumed*).
- **Euclid** (R24, *verified*, and flagged by Euclid as expectation, not data): "we expect there is an inverse correlation between ACV and horizontal expansion activity. Mindbody and ServiceTitan ... have aggressively added new verticals over time; Veeva and OpenGov have not added so much."
- **ServiceTitan** (N-B20, *verified*):
  - "ServiceTitan began by serving a single trade—plumbing—and focusing on residential homes, and we now serve many trades that serve all sites: homes, businesses and even new construction."
  - "we formulate our learnings from trades we have penetrated so far into a proven strategy to enter new trades verticals."
  - "our most successful ventures are not the ones where we tell our customers where they should go next, but rather the ones in which our customers are already heading for a destination and they insist that they need ServiceTitan to journey with them."
  - Trades with different workflows came by acquisition: "we ... cover the pest, cleaning, lawncare and commercial landscaping verticals with our FieldRoutes and Aspire solutions."
- **Veeva** (N-B21, FY2024 10-K, *verified*): about eight years after Veeva entered consumer products (2016) and chemicals (2017) (dates from a secondary source, *assumed*), its 10-K still calls these "Our initial applications for customers outside of life sciences", serving "a set of customers". Reading this as a small, slow-growing expansion is an inference; the text read does not give the revenue share.
- **Motive:**
  - Its IPO release (N-B23, 23 Dec 2025, *verified*) says it "serves nearly 100,000 customers from small businesses to Fortune 500 enterprises" across transportation, construction, energy, field service, agriculture and more.
  - Contrary (N-B22, *verified*) records the move upmarket and the products added: dashcams, maintenance, spend management and dispatch.
  - Contrary also records "Raised $567 million" by 2023. This expansion was venture-funded.
- **Mindbody** (R24, *verified*): "selling its business management suite into salons beyond its initial beachhead in yoga and pilates studios".
- **Product expansion to the same customers is the more common path:**
  - Bessemer lesson 2: "The best vertical software companies build a layer cake of new products that drive continuous growth" (N-B08, *verified*).
  - Tidemark: "Multi-Product companies grew about 21% faster than their Single-Product peers" (N-B10, *verified*; 200+ companies; vendor benchmark).
  - Euclid: payments is "almost certainly the most popular vertical expansion modality" (R24).
- **Constellation** (N-B12, 2015, *verified*): some business units "built high market share in core systems ... after which they've purchased and built add-on products to serve their clients better and drive up switching costs". Leonard adds, "we may have been overly cautious regarding cross selling synergies."
- **Where to Play** (R40, *verified*): most ventures had to change markets. Those with closely related options did better.

**What transferred and what did not:**

| Case | What transferred | What did not, or needed more | Source |
|---|---|---|---|
| ServiceTitan | A "shared services layer" and a repeatable playbook for entering new trades; expansion followed customers into adjacent trades and commercial work | Trades whose workflows differ (pest, lawn care, landscaping) came through acquisitions, not the core product; the smallest firms stayed out of scope | N-B20 |
| Veeva | The content and data platform (quality, regulatory, claims) reached consumer products and chemicals | Still described as "initial applications" for "a set of customers" years later | N-B21 |
| Motive | Vehicle telematics, safety and spend products carried from trucking to any fleet-heavy industry, and up-market | The entry mechanism, a free driver app monetised when the ELD mandate took effect, depended on a one-off regulatory deadline | N-B22, N-B23 |
| Mindbody | The business-management suite, from yoga to salons | Not examined in detail here | R24 |
| Toast | By 2015 it was moving from independents to "mid-market" chains of 10-200 locations | — | N-B19 |

**Verdict B4: partly supported, and mislabelled.**
- *Supported:* expansion leverage is a standard criterion (R16, R17, R24, R40), and 15 of 100 points matches the project's default A6 weight of 15.
- *Mislabelled:* the plan is vertical SaaS with horizontal (adjacent-segment) expansion, not "horizontal, then vertical".
- *Qualified:* adjacent-segment expansion is documented where segments share a customer type or workflow. It often needs acquisitions or years (ServiceTitan, Veeva). The most common growth route is new products, especially payments, for the same customers. At the founders' scale, Constellation shows a single niche plus add-on products can be enough.

**Implications for S0:**
- Define A6 as: "adjacent freight sub-markets that share the customer type or the workflow, plus add-on products (payments, factoring, audit) for the same customers."
- Ask the founders which of Euclid's three axes they mean. Backups picked in S6 should share the software core and one side of the market (already in §4 S6).

---

### B5. Weight norms: is 40 / 45 / 15 typical?

**Published example weight splits found:**

| Source | Kind | Criteria and weights | Weight on size | Weight on count or fragmentation | Status |
|---|---|---|---|---|---|
| Payne Scorecard Method (N-B30; written 2001, revised Jan 2011) | Angel valuation of pre-revenue startups | Team 0-30%; "Size of the Opportunity" 0-25%; Product/Technology 0-15%; Competitive Environment 0-10%; Marketing/Sales Channels/Partnerships 0-10%; Need for Additional Investment 0-5%; Other 0-5% | 25% | 0 | *verified* |
| Dolnicar worked example (R14, 2018) | Textbook, hypothetical | Five unnamed attractiveness criteria at 25/35/20/10/10% | not named | not named | *verified* |
| DPM real B2B case (R12) | Textbook note | 11 attractiveness criteria. The weights shown include 14 for "long-term prospects with the client" and 8 for "current presence in the client". Rule: a mix of short- and long-term, internal- and market-facing criteria | not given | not given | *verified* (partial) |
| Aulet beachhead worksheet (R16) | Startup method | 8 criteria, unweighted; "Economically attractive" is one (about 12.5% if equal) | about 12.5% | 0 | *verified* |
| Gurley (R41, 2012) | VC, marketplaces | 10 factors, each counted equally | 10% | 10% (fragmentation) | *verified* |
| Emergence (R21, 2013) | VC, industry cloud | 10 factors, no weights | 0 | 1 factor, and it favours *concentration* | *verified* |
| Tidemark (R20) | VC, SMB vertical SaaS | 3 attributes, no weights: gigantic; fragmented market; fragmented value chain | about 33% | about 67% | *verified*; **closest to the founders' emphasis** |
| Cohen (R19, 2023) | Practitioner, multiplicative | 7 rows multiplied; count ("Plausible") and budget ("Lucrative") are the two power-of-ten rows | budget row | count row | *verified* |
| Project default (`submarket_selection.md` §5.2) | This project | A1 25, A2 15, A3 15, A4 10, A5 10, A6 15, A7 10, plus a separate 100 points across Axis W | 25 | 10 | — |
| **Founders' S0** | — | 40 size / 45 many businesses and fragmentation / 15 growth | **40** | **45** | — |

No GE-McKinsey example with published weights could be verified. McKinsey's own page timed out, and secondary sites say the weights are set by each firm. That item is **not settled**.

**Finding 1: 85 of 100 on size plus count is atypical.**
- Published scorecards that assign weights give size about 10-25%.
- Where fragmentation appears, it is one factor among ten, and one source (R21) scores concentration in the opposite direction.
- Only Tidemark's unweighted three-attribute list puts comparable emphasis on size and fragmentation. It was written for venture-scale SMB SaaS, whereas the founders' ambition is smaller (see the update above).
- Andreessen's "market matters most" (N-B15) supports a heavy weight on *demand*. His "great market" is "a market with lots of real potential customers" where "the market _pulls_ product out of the startup". That is pull, not size or headcount alone.

**Finding 2: scoring market size and number of businesses separately double counts, unless the terms are redefined.**
- Market size is built as buyers × revenue per buyer:
  - Euclid: "number of customers in ICP * ARPA" (R42);
  - Tidemark: "number of locations, initial ARPU, and expansion ARPU" (R20);
  - Cohen: Plausible (count) × Lucrative (budget) (R19).
- The UK government's multi-criteria analysis manual (N-B31, DCLG, Jan 2009, §5.4.4.5, *verified*): "double counting should not be allowed in MCA, since double-counted effects are likely to be given more weight in the final overall decision than they deserve."
- The same manual warns that apparent double counting is sometimes real value: "Sometimes, what appears to be double counting isn't." Its test, from §5.4.4.4-5: "if criteria X and Y really reflect the same value, then when scoring options on Y, one will wish to look at scores given to X."
- **Applied here [our calc]:** take two candidates with equal fee potential, one with 2,000 buyers at $5k and one with 500 buyers at $20k. If the team prefers the first, the count carries a *separate* value: resilience, word of mouth, weak buyer power, or room for payments or a marketplace (R20, R41). Name that value and score *it*, for example fragmentation as structure (top-50 share) or reachable prospects. Do not score raw count on top of size.
- Euclid's inverse power law (R24) shows count and revenue per customer tend to trade off. A heavy weight on count therefore tilts the ranking toward low-ARPA segments, which need more customers and more acquisition spend.
- The manual's cure fits the S0 structure (§5.4.4.4, *verified*): "options falling below any minimum level are rejected outright because better performance on other criteria can't compensate. This hurdle usually guarantees preference independence." That is knock-out K5.

**Finding 3: what the three criteria leave out, which the sources treat as essential:**

| Missing criterion | Sources that require it | Project row |
|---|---|---|
| Pain, urgency, compelling reason to buy | R15 "Urgency of Need"; R16 "compelling reason to buy"; R17; R19 "Self-Aware" | A3 |
| Ability and willingness to pay, and budget | R15/R16 "well-funded"; R19 "Lucrative"; R28 "turning opex budget into IT budget" | K8, A1 |
| Reachability and cost to reach | R10, R14 (knock-outs); R16 "accessible to your sales force"; R30 | K3, W1 |
| Competition and substitutes, including doing nothing | R16; R43; Payne 10% (N-B30) | W4 |
| Team knowledge and fit | R15 personal filter; R16; Payne 30% for the team (N-B30) | K9, W2 |
| Whole product and time to value | R16; R28 "live in weeks" | W3 |
| Time to win | R16 "How quickly can you win this market?" | W6 |
| Frequency and durability | R19 "Enduring"; R41 "Frequency"; R21 cyclicality | A5, A7 |
| Fee feasibility (the project's own rule) | R25 CAMP; CLAUDE.md | F1-F5 |

- Two of the founders' **own** stated beliefs, that SMBs are reachable directly and that incumbents are few, have no weight. Both belong on Axis W (W1 and W4).
- The split has no internal-facing criteria. It therefore fails the DPM balance rule (R12).

**Verdict B5: not supported as a weight split.**
- 85 of 100 on size plus count is far from every weighted scorecard found (Tidemark's unweighted attribute list is the one close match).
- It double counts the number of businesses unless "market size" and "many businesses" are redefined.
- It leaves out criteria most sources treat as essential.
- Its emphasis on market *structure* is defensible and matches Tidemark's attribute list.

**Implications for S0:**
- Complete S0 step 5 as written (§4): split 100 points across A1-A7 and 100 across W1-W6, then average across team members (R12).
- To keep the founders' emphasis:
  - raise A1 (fee potential) and A4 (fragmentation, defined as structure plus reachable count) above their defaults;
  - move "enough businesses" into K5 as a floor;
  - put SMB access on W1 and incumbents on W4.
- One illustration, **[our call]** and for discussion only: A1 30, A4 20, A6 15, A3 15, A2 10, A5 5, A7 5.
- The S4 sensitivity check (step 5) will then show whether an 85/100 split would change the ranking.

---

## 3. Case studies: small-carrier and small-broker software

| # | Case | Segment and go-to-market | Outcome (dated) | Lesson for S0 | Sources |
|---|---|---|---|---|---|
| 1 | **KeepTruckin / Motive** | Founded June 2013. A free driver logbook app released December 2013, "downloaded one million times in its first four years". Paid ELD and fleet products timed to the ELD mandate, in full effect in 2017. First customers were "small-to-medium, often family-owned businesses" | ARR of $150M (2021); Series F at a $2.9B valuation (May 2022); $567M raised. IPO filing 23 Dec 2025 (NYSE: MTVE), "nearly 100,000 customers from small businesses to Fortune 500 enterprises" across many industries | Reaching fragmented small fleets worked through a free product plus a regulatory forcing event, with venture capital, then moving up-market and into other industries. Not repeatable without an equivalent trigger | N-B22, N-B23 |
| 2 | **Aljex → Descartes** | Back-office TMS for freight brokers in North America; "400 customers", "about three million freight moves per year" | Acquired for "$32.4 million in cash" (DC Velocity, 1 Feb 2018); now sold as Descartes Aljex | An exit comparable at the founders' scale: a few hundred broker customers supported a roughly $30M sale to a consolidator. Revenue was not disclosed | N-B24 |
| 3 | **BoxTop → Descartes** | Shipment-management software for "small- to mid-sized logistics services providers" (forwarders) | Acquired for "approximately £10.25 million ($US 13 million)", paid from cash on hand (11 Jun 2024). Founded 1995 (*assumed*, search snippet) | A long-lived niche freight-software business with a small exit, in the Constellation pattern. Descartes acts as a serial buyer in this niche | N-B25 |
| 4 | **MVMNT** | TMS for small and mid-size brokers; "TMS 2.0 ... all for free", with money made from "financial services and other products". Founder was an ex-broker | $20M Series A (Oct 2022). No outcome after 2022 was found in this search | A free core plus a fintech layer is the documented bet for the small-broker long tail (R27). Its result is **unknown**, so it neither supports nor refutes the approach | N-B26, R27 |
| 5 | **Rose Rocket** | TMS for carriers, brokers and 3PLs "ranging from 2 to 2,000 trucks" | $38M Series B (7 Jul 2023) to "accelerate expansion into larger enterprise fleets"; $69M raised in total. Rebranded as TMS.ai in 2025 (*assumed*, secondary) | A venture-funded carrier TMS moved up-market from the smallest fleets, echoing Bessemer's "Many verticals require a move up-market" (N-B08) | N-B27 |
| 6 | **Convoy (failure)** | Digital freight broker matching shippers with carriers, most of them small | Shut down Oct 2023 after raising about $1.1B (peak valuation $3.8B, Apr 2022). FreightWaves blames overfunding, the freight recession and falling unit economics: "freight is a commodity — and thus capacity is fungible ... shippers could easily find alternatives to Convoy's services with thousands of other freight brokers in the market" | Fragmentation cuts both ways. Thousands of substitutes make loyalty hard, and the 2023-25 downturn hit freight startups and their customers together | N-B29 |

Also seen, not developed:
- **Alvys** (founded 2020): a carrier TMS that raised $40M in its Series B (Oct 2025) and $77M in total. It is described as serving "mid-market fleets" (N-B28). Its "1,000+ customers" figure is *assumed* (secondary).
- Tai Software and Revenova (broker TMS) were not researched.

---

## 4. Open questions the founders must answer before S0 is frozen

1. **Which side pays first?** Shippers, or freight companies (carriers or brokers)? "SMBs we can reach out directly" reads like the freight-company side. The census and FMCSA counts differ sharply by side (R44, N-B01, N-B04).
2. **What does "market size" mean?** Is it the revenue pool (buyers × our fee) or the savings pool? If it is the revenue pool, it already contains the number of businesses (B5, Finding 2).
3. **What does "many businesses / fragmentation" measure?** Raw count, reachable count, or structure (top-50 share, buyer power)? Only structure and reachability avoid double counting.
4. **What revenue per customer (ARPA) do you expect?** The B3 table shows it decides whether count matters at all. Check A holds the fee-share and churn inputs.
5. **Is there a firm-size floor?** Are owner-operators and single-truck carriers (70% of for-hire firms, N-B05) in scope, given thin margins (R38), high exit rates (N-B03, N-B04) and ServiceTitan's choice to skip the smallest firms (N-B20)?
6. **"Go Vertical after Horizontal":** do you mean new products for the same customers (Euclid's vertical axis), the same product for adjacent sub-markets (horizontal axis), or the customers' partners (value-chain axis) (R24)?
7. **"Few incumbents":** few *software* competitors, or few firms doing the *job* (brokers, 3PLs, auditors)? What evidence would show that customers already spend on the problem (R19)?
8. **Channels:** which channels does the team already have: association memberships, factoring or load-board contacts, carrier or broker relationships (W1, W2)?
9. **Weights for Axis W and the missing Axis A rows:** each founder splits 100 across A1-A7 and 100 across W1-W6 (§4 S0 step 5).
10. **Cyclicality:** are you prepared to launch into a customer base that shrank about 10% a year in 2024 (N-B04)? How will the plan survive the next freight downturn (R21, A7)?

---

## 5. Sources

### 5.1 New sources (N-B)

| ID | Source (author / org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-B01 | *ATA American Trucking Trends 2025* announcement (American Trucking Associations) | 28 Aug 2025 (2024 data) | https://www.trucking.org/news-insights/ata-american-trucking-trends-2025 | full (page); report itself not read | fleet-size sentence |
| N-B02 | *Carrier attrition eases in 2025* (David Taube, Trucking Dive) | 12 Jan 2026 | https://www.truckingdive.com/news/fmcsa-grants-reinstatements-revocations-operating-authority-2025-data/808968/ | full | 2025 carrier population and revocations; the analysis excludes brokers |
| N-B03 | *Carrier & Broker Failures in 2024-2025 ...* (David Jencks, IFA Commercial Factor) | 21 Jan 2026 | https://magazine.factoring.org/magazine-articles/carrier-amp-broker-failures-in-20242025-and-why-2026-may-bring-one-last-wave | full; a secondary compilation | exit figures, each with its underlying source named (not checked) |
| N-B04 | Brush Pass Research blog (Kevin Hill): home page; "2024 closes with 3,104 fewer freight brokerages"; "What TMS software are Micro-Cap freight brokerages using?" | Aug 2024 – Apr 2025 | https://brushpassresearch.blog/ ; …/2025/01/07/2024-closes-with-3104-fewer-freight-brokerages/ ; …/2025/04/02/what-tms-software-are-micro-cap-freight-brokerages-using/ | full (text); the TMS chart's numbers were not in the text | active broker counts, net exits, micro-cap TMS ranking |
| N-B05 | *There Are 292,000 Shippers in America and 9 out of 10 Carriers Have 10 Trucks or Less* (Adam Wingfield, FreightWaves) | 17 Mar 2026 | https://www.freightwaves.com/news/there-are-292000-shippers-in-america-and-97-of-carriers-have-10-trucks-or-less-the-match-has-been-right-in-front-of-you-the-whole-time | full | carrier counts; its figures come second-hand from ATA and FMCSA |
| N-B06 | OOIDA *About Us* | undated | https://www.ooida.com/about-us/ | full | membership figures |
| N-B07 | TIA membership (third-party profile of the Transportation Intermediaries Association, via search) | undated | https://www.supplychain247.com/company/transportation_intermediaries_association (tianet.org returned 403) | **blocked** at tianet.org; search snippet only | "more than 1,700" members (*assumed*) |
| N-B08 | *Ten lessons from a decade of vertical software investing* (Brian Feinstein, Caty Rea, Bessemer) | 18 Jul 2022 | https://www.bvp.com/atlas/ten-lessons-from-a-decade-of-vertical-software-investing | full | all ten lessons |
| N-B09 | *Truths about Vertical SaaS* (Dave Yuan, Tidemark) | undated | https://www.tidemarkcap.com/vskp-chapter/vertical-saas-truisms | **partial**: gated after a login notice | public section |
| N-B10 | *2025 Vertical & SMB SaaS Benchmark Report* page (Tidemark) | 2025 | https://www.tidemarkcap.com/vskp-chapter/2025-vertical-smb-saas-benchmark-report | **partial**: full report behind a form (not submitted) | public headline figures |
| N-B11 | *Fintech Scales Vertical SaaS* (Kristina Shen, Kimberly Tan, Seema Amble, Angela Strange, a16z) | 4 Aug 2020 | https://a16z.com/fintech-scales-vertical-saas/ | full | definitions, 2-5x, winner-take-most, small-TAM passage |
| N-B12 | Constellation Software president's letters (Mark Leonard): letters covering 2009 (dated 25 Mar 2010), 2011, 2012, 2013, 2014, 2015, 2016 (the "2017" file), and 15 Feb 2021 | 2010-2021 | index: https://www.csisoftware.com/category/pres-letters ; files: https://www.csisoftware.com/wp-content/uploads/2026/04/{shareholder-letter-2009, 2011_presidents_letter, presidents-letter-final, presidentletter_2013, presidents_letter_2014, pl_2015, 2017-presidents-letter-1, letter-to-shareholders-february-15-2021}.pdf | full (PDFs downloaded, text extracted, relevant sections read) | passages on VMS niches, market share, business-unit size, churn and competitors. Years are taken from each letter's content; exact publication dates beyond those stated are *assumed* |
| N-B13 | *Zero to One* (Peter Thiel with Blake Masters), quotations as reproduced on Goodreads | 2014 | https://www.goodreads.com/quotes/8638438-every-startup-is-small-at-the-start-every-monopoly-dominates | book **not read**; quote pages only | "start with a very small market"; "few or no competitors"; PowerSellers (*assumed*) |
| N-B14 | *How to Get Startup Ideas* (Paul Graham) | Nov 2012 | https://paulgraham.com/startupideas.html | full | Competition and "Well" sections |
| N-B15 | *The only thing that matters* (Marc Andreessen, pmarchive) | 25 Jun 2007 | https://pmarchive.com/guide_to_startups_part4.html | full | market vs team vs product; confirmed the "no competition" line is **absent** |
| N-B16 | *After the Chasm—Scaling Beyond the Beachhead* (Geoffrey Moore, author's blog) | undated | https://geoffreyamoore.com/business_blogs/after-the-chasm-scaling-beyond-the-beachhead/ | full | adjacent target, "big enough to matter but small enough to lead" |
| N-B17 | Aulet, Step 4 *Beachhead TAM*: companion page, Worksheets 04.1-04.4 (public Google Doc text export), and the 2024 edition's front-matter preview | page undated; book 2024 | https://www.d-eship.com/step4/ ; https://docs.google.com/document/d/1yUliikdg5pnjRGGQio7USmtLmb2NQ0EHqtyOgQkd9JI/export?format=txt ; https://api.pageplace.de/preview/DT0400.9781394222537_A48810143/preview-9781394222537_A48810143.pdf | **partial**: page, worksheets and preview read; the book's Step 4 chapter was **not accessible** (O'Reilly 403; archive.org lending-only) | TAM definition, the SensAble example, worksheet questions, the "not too big or too small" line |
| N-B18 | *Review: Disciplined Entrepreneurship* (Yevgeniy Brikman) | 29 Aug 2022 | https://www.ybrikman.com/blog/2022/08/29/disciplined-entrepreneurship/ | full; secondary | the "$20-100M/year" beachhead range (reviewer's summary) |
| N-B19 | *Toast* Series B investment memo (Kent Bennett, Eric Ahlgren, Bessemer) | 14 Dec 2015 | https://www.bvp.com/memos/toast | full | go-to-market, payback, the Gordon Food Service channel, incumbents, segments |
| N-B20 | ServiceTitan, Inc. Form S-1 (SEC) | filed Nov 2024 | https://www.sec.gov/Archives/edgar/data/1638826/000119312524260611/d577298ds1.htm | full text downloaded; searched for the passages quoted | founders, expansion history, shared services, acquisitions, down-market exclusion |
| N-B21 | Veeva Systems Form 10-K, fiscal year ended 31 Jan 2024 (SEC) | filed 25 Mar 2024 | https://www.sec.gov/Archives/edgar/data/1393052/000139305224000013/veev-20240131.htm | full text downloaded; searched | passages on customers outside life sciences |
| N-B22 | *Report: Motive Business Breakdown & Founding Story* (Contrary Research) | 27 Jul 2023 | https://research.contrary.com/company/motive | full; secondary research firm | founding, free app, ELD mandate, ARR, funding |
| N-B23 | *Motive Files Registration Statement for Proposed Initial Public Offering* (Motive press release) | 23 Dec 2025 | https://gomotive.com/motive-files-registration-statement-for-proposed-initial-public-offering/ | full | customer description, ticker. The revenue figure seen in search snippets was not verified |
| N-B24 | *Descartes acquires TMS provider Aljex for $32.4 million* (DC Velocity), plus the Descartes acquisition page | 1 Feb 2018 | https://www.dcvelocity.com/articles/29464-descartes-acquires-tms-provider-aljex-for-32-4-million ; https://www.descartes.com/about/investor-relations/acquisitions/descartes-acquires-aljex | full | price, customers, freight moves |
| N-B25 | *Descartes Acquires BoxTop Technologies* (Descartes) | 11 Jun 2024 | https://www.descartes.com/resources/news/descartes-acquires-boxtop-technologies | full | price, customer segment |
| N-B26 | *MVMNT leveling playing field for smaller brokers* (Jack Glenn, FreightWaves) | 19 Jul 2022 | https://www.freightwaves.com/news/mvmnt-leveling-playing-field-for-smaller-brokers | full | free TMS, revenue model |
| N-B27 | *Rose Rocket Raises $38M USD Series B ...* (Fleet News Daily, press-release based) | 7 Jul 2023 | https://fleetnewsdaily.com/rose-rocket-raises-38m-usd-series-b-to-scale-its-network-centric-tms-solutions-while-expanding-into-the-enterprise/ | full | customer range, move into enterprise |
| N-B28 | *Alvys Closes $40M Series B ...* (The AI Insider) | 9 Oct 2025 | https://theaiinsider.tech/2025/10/09/alvys-closes-40m-series-b-to-enhance-ai-driven-freight-operations-for-carriers-and-brokers/ | full (the Business Wire original returned 403) | amount, founding year, segments |
| N-B29 | *Death from overfunding: An obituary for Convoy* (Craig Fuller, FreightWaves) | 23 Oct 2023 | https://www.freightwaves.com/news/death-from-overfunding-an-obituary-for-convoy | full; opinion by a trade-press CEO | funding, causes of failure |
| N-B30 | *Scorecard Valuation Methodology* (Bill Payne) | May 2001, revised Jan 2011 | https://seedspot.org/wp-content/uploads/2021/02/Scorecard-Valuation-Methodology.pdf | full (PDF downloaded, text extracted) | factor weights, worked example, rationale |
| N-B31 | *Multi-criteria analysis: a manual* (Dodgson, Spackman, Pearman, Phillips; UK Department for Communities and Local Government) | Jan 2009 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/7612/1132618.pdf | full PDF downloaded; §5.4.4 read | redundancy, preference independence, double counting |

### 5.2 Existing reading notes used
R12, R14, R15, R16, R17, R19, R20, R21, R24, R27, R28, R30, R38 (via `submarket_selection.md`), R40, R41, R42, R43, R44. No note was re-read at its original source except R17, which is now backed by N-B16.

### 5.3 Could not access, or used only second-hand
- Aulet's book, Step 4 chapter: O'Reilly returned 403 and archive.org is lending-only. The "$20-100M/year" range therefore stays *assumed*.
- McKinsey, *Enduring Ideas: the GE-McKinsey nine-box matrix*: timed out, so no GE-McKinsey weight example was verified.
- tianet.org (403), CNBC (403), S&P Global's Transfix analysis (403), Business Wire's Alvys release (403).
- The FMCSA 2024 Pocket Guide PDF returned an HTML block page, so ATA and FreightWaves figures were used instead.
- Tidemark's gated sections, including the full 2025 benchmark (form not submitted).
- *Zero to One* itself (only quote pages).
- Moore's *Inside the Tornado* (bowling-alley detail only from secondary summaries, *assumed*).
