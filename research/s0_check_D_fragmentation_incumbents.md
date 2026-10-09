# S0 check D: how to measure fragmentation and "few incumbents" (O-4, O-5)

> **What this is:** research on the two S0 items the founders marked for further investigation: how fragmentation is measured (F-9, handoff item O-4) and how "few incumbents" is measured (F-10, handoff item O-5) (`submarket_selection.md` §4 S0.3-S0.4). It builds on check B (B1a, B1b, B5) and check A. It does not re-argue check B's verdict on "few incumbents" (D3b).
> **Date:** 2026-09-14. **Status:** input to S0. It decides nothing. The options in §3 are for the founders to decide together with Claude.
> **Labels:** *verified* means read at the source: a quote copied from the page, or a value taken from a downloaded file or data table. *assumed* means a search snippet, a secondary source, memory, or a source that could not be opened. **[our calc]** and **[our call]** mark this document's own arithmetic and judgement. R-IDs are reading notes; N-A and N-B IDs are sources from checks A and B; N-D IDs are new sources, listed in §5.

**The founders' words (third round, 2026-09-14, verbatim):**
> "Fragementation is to be measured with any existing formulas for this, or we will look into business insights as to how this is measured. The same can be said for few incumbents, we will likely look into a ballpark number of how many companies exist in the space and their slice of the market pie for this. But we will find out more, mark this for further investigation."

**What these measures drive today** (every default is **[our call]** in `submarket_selection.md`):
- **K10**, the "land of the giants" knock-out, is active because the founders target SMBs. It fails when the top 50 firms hold more than 80% of revenue (R21's number). On 2022 data it fails LTL (82.9%) and couriers (90.9%). Refrigerated warehousing is at 73.9% (§8.2).
- **§10 bands:** a top-50 share under 20% is fragmented (R20), 20-80% is mixed, and over 80% is concentrated.
- **A4** (weight 15) scores fragmentation and number of buyers, per side. Parked change 6 waits on O-4.
- **W4** scores competition and substitutes. Parked change 4 waits on O-5. A hard cap would make "few incumbents" an S2 knock-out.

**Words used below:**
- *NAICS*: the North American Industry Classification System, the government's industry codes. For example, 484121 is long-distance truckload trucking. More digits means a narrower industry.
- *Concentration*: how much of an industry's revenue sits with its largest firms. *Fragmentation* is the opposite: revenue spread over many small firms. An *oligopoly* is a market dominated by a few sellers.
- *Antitrust*: competition law. The merger guidelines below were written to decide when a merger harms competition, not to pick markets.
- *TMS*: transportation management system, software to plan, tender, track and bill loads (R33). *FAP*: freight audit and payment, meaning checking carrier invoices against agreed rates and then paying them.
- *Accessorial*: a charge on top of the base line-haul rate. Examples: detention (the carrier waits past the free time at a dock), lumper fees, liftgate (common usage, *assumed*).
- *Incumbent*: whoever does the job for the customer today. That can be a software vendor, a service firm (3PL, auditor, factoring firm), in-house staff, or nobody.
- *SMB*: small and mid-sized business. *PE*: private equity. A *roll-up* or *buy-and-build* is a PE strategy of buying many small firms and merging them.

---

## 1. Summary

**Fragmentation (O-4).**
- **Standard formulas exist and are published for every freight code.**
  - The Economic Census gives the revenue share of the 4, 8, 20 and 50 largest firms (concentration ratios, CR4-CR50) (N-D01, *verified*).
  - It also gives the Herfindahl-Hirschman Index (HHI), outside manufacturing since 2017 (N-D02, *verified*).
  - Some HHI values are withheld to protect individual firms, including couriers and, in 2022, refrigerated warehousing. R44's "n/a" is a withheld value (flag "D"), not a zero (N-D03, *verified*).
- **Published thresholds were built for two different jobs.**
  - Antitrust bands exist to flag concentrated markets for merger review. The 2023 US guidelines call an HHI above 1,800 "highly concentrated". The 2010 guidelines drew that line at 2,500. The EU sees no concerns below 1,000 (N-D07, N-D08, N-D09).
  - Startup lines exist to sort industries for a vendor: Tidemark's top-50 share under 20% (R20) and Emergence's top-50 share over 80% (R21).
  - No source links any measure or band to software outcomes such as customer acquisition cost (CAC), market share won, or word of mouth.
- **On 2022 freight data, the antitrust measures call every freight industry except couriers "unconcentrated".** So they cannot separate candidates for A4; the top-50 share can.
  - **LTL** is the case where the measure decides the answer. It is concentrated on the top-50 share (82.9%, fails K10), medium on CR4 (40.8%), and unconcentrated on HHI (572, the same as about 17 equal-sized firms).
  - **Refrigerated warehousing** is mixed on the top-50 share and medium on CR4.
  - **Couriers** are concentrated on every measure.
- **K10 is fragile for LTL.**
  - The census tables miss owner-operators with no payroll (R44). Adding Nonemployer Statistics (N-D05) lowers trucking's top-50 share from 28.3% to 22.3% [our calc].
  - If even 10% of long-distance owner-operator receipts belonged to LTL, LTL would fall to about 74% and pass K10 [our calc].
- **The most direct measure of an SMB market is the share of revenue held by small firms,** not a concentration index. Census Statistics of US Businesses (SUSB) gives it (N-D04). In 2022, firms with fewer than 20 employees held 52% of local general-freight receipts, 24% in truckload and in brokerage, 8% in LTL and 3% in couriers ([our calc] from *verified* data).

**Few incumbents (O-5).**
- **A ballpark count is cheap for most jobs, but each firm's slice of the pie is known only for some** [our calc, from D5].
  - *Small-broker TMS:* a 2025 survey chart gives shares. McLeod leads at about 16%; 20 systems are named; the four largest vendors hold about 36%; the HHI is about 450-610, like 16-22 equal-sized vendors (N-B04 chart).
  - *Freight audit and payment:* the two largest named providers pay about $36B and $46B of freight bills a year (N-D30, N-D31). That is roughly 9% of US trucking revenue. Cass describes its competition as "a few primary competitors and numerous small transportation bill audit firms".
  - *Detention billing:* the job sits inside TMS and telematics products, plus a few standalone tools. No shares exist.
- **The evidence on what incumbents mean for a new entrant does not support a cap on the number of competitors.**
  - "No market need" was cited in 42% of 101 startup failure write-ups, against 19% for being outcompeted (N-D29).
  - Almost half of market pioneers fail. The "early market leaders" that succeed enter about 13 years after the pioneers (N-D28).
- **It does support caution where one vertical vendor dominates** ("winner-take-most", N-B11; incumbents that "chased away dozens of new entrants", N-B08).
- **The 2023 US merger guidelines allow "the number of significant competitors" as a substitute measure** when shares are "difficult to measure" (N-D07, *verified*). That is the founders' "ballpark number" idea, and it has an official precedent.

**Suggested starting points, [our call], not decisions:**
- **O-4, option C:** keep the top-50 bands for the zones and for A4, and add a small-firm-share tie-breaker for candidates within 5 points of the K10 line.
- **O-5, option D:** score W4 on proven spend plus weak incumbents. Record the vendor count and the leader's share as W4's evidence. Veto a candidate only when one vendor dominates the job.

---

## 2. Findings

### D1. The standard formulas

| Measure | In plain words | Worked example | Data needed | Published by the Economic Census? |
|---|---|---|---|---|
| **CRn** (concentration ratio: CR4, CR8, CR20, CR50) | Add up the revenue shares of the n largest firms | Shares of 30, 20, 10 and 5%, then many small firms: CR4 = 65% | Revenue of the top n firms, and the industry total | Yes. CR4/8/20/50 for every freight code in §8.2 and for shipper industries (manufacturing, wholesale), in 2017 and 2022 (N-D01, *verified*) |
| **HHI** (Herfindahl-Hirschman Index) | Square each firm's percentage share, then add them up. 10,000 means one firm has everything; the number falls toward 0 as the market splits into many tiny firms | DOJ's example: shares of 30, 30, 20 and 20% give 2,600 (N-D06, *verified*) | Each firm's share; in practice, the largest firms' shares | Yes since 2017, computed on the top 50 firms (N-D02). Withheld (flag "D") for some codes. In 2022 that was 31 of the 131 transport and warehousing industry rows, 110 of 630 in manufacturing and 30 of 161 in wholesale (N-D01; the count is [our calc]) |
| **Numbers-equivalent** (10,000 ÷ HHI) | "As concentrated as N equal-sized firms" (Adelman 1969, N-D12, *assumed*) | An HHI of 2,600 is like 3.8 equal firms. Five equal firms give 2,000 and six give 1,667 (N-D07 footnote 13, *verified*) | HHI | Not published; divide 10,000 by the HHI [our calc] |
| **Gini coefficient / Lorenz curve** | How unequal the firms' sizes are. 0 means all equal | Four firms at 70/10/10/10% give a Gini of 0.45. Two firms at 50/50 give 0, although their HHI is 5,000 [our calc] | Every firm's size, or counts by size class | Not published as such |
| **Small-firm share** (Census SUSB) | The share of firms, or of revenue, in firms below a size, e.g. under 20 or under 500 employees | Local general freight, 2022: firms under 20 employees are 93% of firms and hold 52% of receipts (N-D04; shares are [our calc]) | SUSB tables. Receipts are published only for years ending in 2 and 7 | Separate Census program; 6-digit codes; the 2022 tables came out in April 2025 (N-D04, *verified*) |
| **Nonemployer count and receipts** (Census NES) | Businesses with no payroll, such as one-truck owner-operators, which every table above leaves out | Truck transportation, 2022: 914,821 nonemployer businesses with $112.9B of receipts, against 156,156 employer firms (N-D05, R44, *verified*) | NES file | Published, but it does not split truckload from LTL |

Notes (*verified* unless marked):
- **OECD on the trade-offs.**
  - CR4 "inevitably do[es] not distinguish between markets in which there are only five firms and those where there is a long tail of firms with smaller market shares".
  - The CR50 "fails to distinguish between those markets in which the four largest firms hold shares of 80 percent and those where they hold shares of 20 percent".
  - The HHI "solves this problem" (N-D10).
- **Same CR4, different HHI (toy example, [our calc]).**
  - Market P: four firms at 10% each and 60 firms at 1%. CR4 is 40%, the HHI is 460, like 22 equal firms.
  - Market Q: one firm at 37% and 63 firms at 1%. CR4 is also 40%, but the HHI is 1,432, like 7 equal firms.
  - Both have a CR50 of 86%, because with only 64 firms the top 50 hold nearly everything by construction.
- **The census HHI covers only the top 50 firms.** The true HHI is therefore slightly higher, and the numbers-equivalent slightly lower. For fragmented industries the gap is negligible: the 2010 guidelines note that small firms "do not affect the HHI significantly" (N-D08).
- **Which measures researchers actually use.** Krivka calls CR and HHI "the most popular concentration indicators in empirical research". Entropy, Rosenbluth and Gini "are applied on an irregular basis only", and such measures "ignore or pay little attention to the number of" firms (N-D11).
- **An industry code is not a market.**
  - The OECD warns of "arbitrariness in the definition since it is not based on substitutability" (N-D10).
  - National figures also understate concentration in local markets such as local trucking. Abdel-Raouf adjusts CR4s "to reflect the market locality problem" (N-D13).

Strengths and weaknesses for our purpose, spotting many small buyers we can sell to [our call]:
- **CR4:** the simplest, and IBISWorld's measure. Says nothing about whether a tail of small firms exists.
- **CR50 (top-50 share):** sees the tail, is Tidemark's axis, and is published everywhere. It lumps the top 4 in with the rest, and it is inflated in industries with few firms (refrigerated warehousing has 719).
- **HHI and numbers-equivalent:** best at spotting one dominant firm, and the regulators' standard. They squeeze every fragmented freight industry into a range of about 2 to 150, so they cannot rank those industries against each other. Withheld for some codes.
- **Gini:** measures inequality, not concentration, and is not published. Not recommended.
- **SUSB small-firm share:** the most direct measure of revenue held by small buyers, which is the SMB market itself. Limits:
  - it sizes firms by all their employees, across all their industries;
  - noise is deliberately added to the values (N-D04 flag sheet: "Low noise applied to cell value (less than 2%)");
  - it still leaves out nonemployers.
- **NES:** the only fix for owner-operators. The counts are large, but receipts per business are small: about $123k on average in trucking [our calc].

**Verdict D1:** standard formulas exist and cost nothing to apply. CRn and HHI are published for freight and shipper codes, SUSB gives small-firm shares, and NES covers owner-operators. No single measure answers "are there many small buyers?". Concentration measures describe the top of an industry; the small-firm share describes the bottom.
**Implications for S0:** describe each side's structure with two numbers: the top-50 share, which sets the zone, and the small-firm receipts share, which shows whether an SMB market exists. Keep the HHI as a check for one dominant firm. Drop Gini.

### D2. Published thresholds, and what each was built for

| Source | Measure | Threshold (quoted) | Built for | Status |
|---|---|---|---|---|
| DOJ/FTC *Merger Guidelines*, 18 Dec 2023 (N-D07) | HHI; share of the merged firm | "Markets with an HHI greater than 1,800 are highly concentrated, and a change of more than 100 points is a significant increase". A merger creating "a firm with a share over thirty percent" is also presumed harmful if the HHI rises by more than 100. DOJ's page describes 1,000-1,800 as moderately concentrated (N-D06) | Merger enforcement | *verified*. Still stated on DOJ's page (updated 17 Jan 2024). Whether anything replaced it in 2025-26 was not checked, so treat it as in force (*assumed*) |
| Same document, footnote 12 | Count | "The Agencies may instead measure market concentration using the number of significant competitors in the market. This measure is most useful when there is a gap in market share between significant competitors and smaller rivals or when it is difficult to measure shares" | Merger enforcement | *verified* |
| DOJ/FTC *Horizontal Merger Guidelines*, 19 Aug 2010 (N-D08) | HHI | "Unconcentrated Markets: HHI below 1500"; "Moderately Concentrated Markets: HHI between 1500 and 2500"; "Highly Concentrated Markets: HHI above 2500". "The purpose of these thresholds is not to provide a rigid screen" | Merger enforcement. Replaced in 2023, whose footnote 15 says the 1982-2010 guidelines used 1,000 and 1,800 | *verified* |
| EU horizontal merger guidelines, 2004/C 31/03 (N-D09) | HHI; share | Concerns are "unlikely" in "a market with a post-merger HHI below 1000". Also unlikely between 1,000 and 2,000 "and a delta below 250", and above 2,000 "and a delta below 150". A combined share not exceeding "25 %" suggests no concern. The levels "do not give rise to a presumption" | Merger enforcement | *verified* |
| Shepherd, as reproduced by Abdel-Raouf (N-D13, N-D14) | CR4 | "Competitive: If CR4C < 40%"; "Loose Oligopoly: If 40% ≤ CR4C ≤ 60%"; "Tight Oligopoly: If CR4C > 60%". These are "the traditional market structure demarcations, but they are arbitrary". Effective competition needs "at least five strong competitors in the market, no dominant firm, and easy entry" (Shepherd and Shepherd 2004) | Economics: classifying market structure | *verified* at the secondary paper. Shepherd's own texts not read (*assumed*) |
| St. Louis Fed (N-D16) | CR5 | "A rule of thumb is that an oligopoly exists when the top five firms in the market account for more than 60% of total market sales" | Public education | *verified* |
| IBISWorld (N-D15) | CR4 | Measures "the market share of the top four operators". A major player "generates over 5% of the industry's revenue" (*verified*). The bands (low under 40%, medium 40-70%, high over 70%) were seen only in search snippets | Market-research reports | bands *assumed* |
| Bain 1951, via APEC 2008 (N-D17) | CR8 | "in industries with eight-firm concentration ratio (CR8) of more than 70 percent, profits were significantly higher" | Economics: does concentration raise profits? | *verified* at the secondary report. Bain's 1959 CR4/CR8 classes could not be found at source (N-D18, *assumed*; not used) |
| Tidemark (R20) | Top-50 share | "only including those industries where the top 50 companies have less than 20% market share" | VC targeting of SMB vertical SaaS | *verified* |
| Emergence (R21) | Top-50 share | "highly concentrated industries in which fewer than 50 companies represent over 80% of revenue", treated as a **plus** (lower CAC, better word of mouth) | VC targeting of "industry cloud" | *verified* |
| Hammer et al. 2017 (N-D20) | HHI | PE add-on acquisitions are "most likely in moderately fragmented industries with HHI between 1000 and 1500", compared with "highly fragmented industries with HHI of up to 500". Also, "virtually all buyouts (99%) are in competitive marketplaces with HHI below 1500" | Academic study of 9,548 PE buyouts in 86 countries | *verified* (accepted manuscript) |

What the table shows [our call]:
- **The antitrust bands start where our interest ends.** An HHI of 1,000, which is both the EU's safe zone and the start of the US "moderate" band, equals 10 equal-sized firms. Every freight code except couriers sits far below it (D4).
- **The two startup lines point in opposite directions.** Tidemark wants the top 50 to hold under 20%; Emergence prefers them to hold over 80%. K10 uses Emergence's number as a *fail* line, the reverse of how Emergence meant it.
- **On PE's scale, freight is highly fragmented.** In Hammer et al., an HHI up to 500 counts as highly fragmented, and 72% of their buyouts sat in industries in that band (N-D20). Every freight code except couriers falls in it.

**Verdict D2:** thresholds exist for CR4, CR5, CR8, CR50 and HHI, but none was built to choose markets for SMB software. The two that were built for picking markets, Tidemark's and Emergence's, contradict each other, and neither has outcome data behind it (R20, R21).
**Implications for S0:** keep the 20% and 80% top-50 lines as conventions labelled [our call], not as "the standard". Use the antitrust lines (HHI 1,800, CR4 60%) only to spot a dominant firm.

### D3. How investors and analysts judge "fragmented" in practice

- **Vertical-SaaS VCs.**
  - Tidemark plots the top-50 share against the number of firms and industry sales, at 4-digit NAICS (R20). Emergence uses the same statistic, read the other way (R21).
  - Bessemer uses no number. It looks for "SMB segments overlooked by incumbents" and warns that some verticals have "too few logos" (N-B08).
  - a16z's freight thesis cites a count and a concentration claim: "more than 17,000 freight brokers", and "one-third of the market is served by the 10 largest national brokers" (R27; figures unsourced). The census shows the top 8 brokers with 15.5% and the top 20 with 23.4% (R44). Their definitions of "market" may differ, but the two pictures do not match.
- **Gurley** judges fragmentation qualitatively, as one of ten factors: "High buyer and supplier fragmentation is a huge positive for an online marketplace" (R41).
- **Constellation** describes its markets in words, not numbers: "tiny markets ... usually characterised by a gradually consolidating customer base" (N-B12).
- **Private equity** uses "fragmented" as the case for roll-ups.
  - INSEAD: buy-and-build works "especially in fragmented markets where consolidation can create outsized returns" (N-D21; no threshold).
  - A deal-software blog lists "No clear industry leader. Little industry consolidation" (N-D22; no threshold).
  - The numeric PE thresholds seen in search results ("less than 30%" held by the top companies, "CR4 below 20%") come from unsourced blogs (N-D22, *assumed*).
  - The one study with data measures fragmentation by HHI (N-D20; D2).
- **Porter.**
  - A fragmented industry is one where no firm "has a significant market share and can strongly influence the industry outcome" (*Competitive Strategy*, 1980; N-D19, *assumed*: seen only on secondary pages).
  - On buyer power: "Buyer power is highest when buyers are large relative to the competitors serving them" (R43, *verified*). For a vendor, fragmented customers means each customer has little power over price.
- **Freight-tech incumbents describe their customers as fragmented.** Descartes sees "an opportunity for logistics technology providers to unite this highly fragmented community", noting that "a large number of organizations still have manual … business processes" (N-D36, *verified*).
- **Evidence linking any measure or band to software outcomes: none found.** The claims that concentration lowers acquisition cost (R21) and that vertical leaders can pass 40% share (N-A34) are practitioner statements drawn from survivors. The nearest data:
  - In the Census Annual Business Survey of 850,000+ firms, advanced-technology adoption "is rare and generally skewed towards larger and older firms" (N-D23, *verified*). Industries made up of small firms adopt less, which is both headroom and friction (T13).
  - PE add-on deals cluster at an HHI of 1,000-1,500 (N-D20). That concerns acquisitions, not software sales.

**Verdict D3:** practice splits three ways: VCs use the top-50 share, PE research and antitrust use HHI bands, and Bessemer, Gurley, Constellation and Porter judge qualitatively. Nobody publishes evidence tying a band to acquisition cost, share won, or word of mouth.
**Implications for S0:** whatever measure is chosen, keep its bands as a tuning knob (§10). Revisit them when S5 produces evidence on acquisition cost, as T1 already provides.

### D4. Applying it to freight

**The freight-company side, 2022.** The census data are *verified* (N-D01, R44) and the SUSB shares come from N-D04. The zones and equal-firm figures are **[our calc]**.

| NAICS | Industry | Employer firms | CR4 | Top-50 | HHI | ≈ equal firms | Receipts in firms <20 employees | Top-50 zone | CR4 zone (IBISWorld / Shepherd) | HHI zone (2023) |
|---|---|---|---|---|---|---|---|---|---|---|
| 48411 | General freight, local | 43,243 | 2.3% | 10.5% | 3 | ~3,200 | 51.7% | fragmented | low / competitive | unconcentrated |
| 48422 | Specialized, local | 31,927 | 1.8% | 9.9% | 2 | ~4,200 | 33.5% | fragmented | low / competitive | unconcentrated |
| 4842 | Specialized, all | 52,012 | 6.0% | 18.6% | 15 | ~670 | 27.4% | fragmented | low / competitive | unconcentrated |
| 488510 | Brokers and forwarders | 17,130 | 9.9% | 34.3% | 43 | ~230 | 24.1% | mixed | low / competitive | unconcentrated |
| 484121 | Truckload, long-distance | 53,705 | 16.7% | 37.4% | 98 | ~100 | 24.3% | mixed | low / competitive | unconcentrated |
| 484230 | Specialized, long-distance | 10,701 | 14.3% | 38.1% | 74 | ~135 | 18.4% | mixed | low / competitive | unconcentrated |
| 493 | Warehousing, all | 9,473 | 18.5% | 48.2% | 148 | ~68 | — | mixed | low / competitive | unconcentrated |
| 49312 | Refrigerated warehousing | 719 | 51.3% | 73.9% | D (2017: 584) | ~15-17 | 10.3% | mixed, near the line | medium / loose oligopoly | unconcentrated (2017 value) |
| 484122 | LTL, long-distance | 7,675 | 40.8% | 82.9% | 572 | ~17 | 7.9% | concentrated (fails K10) | medium / loose oligopoly | unconcentrated |
| 4921 | Couriers and express | 6,553 | 87.7% | 90.9% | D (at least 1,923) | ≤5 | 2.6% | concentrated (fails K10) | high / tight oligopoly | highly concentrated |

How to read it:
- "≈ equal firms" is 10,000 ÷ HHI.
- Where the HHI is withheld ("D"), its floor comes from spreading each CR band evenly among its firms. For couriers: 87.7² ÷ 4 ≈ 1,923 [our calc].
- SUSB uses 6-digit codes (484110, 484220, 492110, 493120), and its receipt totals differ from the Economic Census's. Use it for shares only.

**Which industries change zone under which measure [our calc]:**
- **LTL changes the most.** It is concentrated on the top-50 share (fails K10), "medium" or "loose oligopoly" on CR4, and "unconcentrated" on HHI (like 17 equal firms). Its SMB market is thin either way: firms under 500 employees hold 17.5% of receipts, about $11.6B (N-D04).
- **Refrigerated warehousing** moves from "mixed" on the top-50 share to "medium" or "loose oligopoly" on CR4 (51.3%). It stays unconcentrated on its last published HHI (584, in 2017).
- **Couriers are concentrated on every measure.** Adding all 1.34 million courier-and-messenger nonemployers ($17.7B, N-D05) still leaves the top-50 share at about 80%.
- **Every other freight code is "low" or "unconcentrated" on the antitrust-style measures.** Only the top-50 share and the small-firm share separate the fragmented local and specialized codes from the mixed truckload, broker and warehousing codes.
- **At the K10 line:** with top-50 above 80%, LTL and couriers fail. With CR4 above 60%, HHI above 1,800, or IBISWorld's "high", only couriers fail.

**Adding owner-operators, the limit R44 flagged.** The NES 2022 data are *verified* (N-D05); the adjusted shares are [our calc]. Adding nonemployer receipts to the total keeps the census convention of summing each firm's gross receipts.

| Code | Nonemployer businesses | Their receipts | Top-50 share, employer firms only | Top-50 share incl. nonemployers |
|---|---|---|---|---|
| 484 Truck transportation | 914,821 | $112.9B | 28.3% | 22.3% |
| 4841 General freight | 843,179 | $107.2B | 37.6% | 27.5% |
| 48411 Local general freight | 277,895 | $31.4B | 10.5% | 6.7% |
| 48412 Long-distance (truckload and LTL together) | 565,284 | $75.9B | Truckload 37.4% | Truckload 26.0% if all of it were truckload (the lowest it could go) |
| 4842 Specialized | 71,642 | $5.7B | 18.6% | 17.8% |

- **NES does not split long-distance trucking into truckload and LTL,** so LTL cannot be adjusted directly. If 5% of the $75.9B belonged to LTL, LTL's top-50 share would be 78.4%; at 10%, 74.3%. Both would pass K10 [our calc]. Owner-operators probably haul mostly truckload (*assumed*), so the 82.9% stands, but K10's verdict on LTL is fragile.
- **Different counts measure different things.** FMCSA-based counts give about 580,000 active carriers (N-B05, *assumed*); NES counts 914,821 trucking businesses with no payroll. The gap is unexplained here (*assumed* to reflect different definitions).

**A shipper-side example** (the same files, 2022; *verified*):

| NAICS | Shipper industry | Firms | CR4 | Top-50 | HHI | Receipts in firms <500 employees |
|---|---|---|---|---|---|---|
| 424480 | Fresh fruit and vegetable wholesalers | 4,253 | 15.2% | 39.6% | D (2017: 45) | 73.4% |
| 3114 | Fruit and vegetable preserving | 1,674 | 20.6% | 64.2% | 171 | — |
| 424510 | Grain and field bean wholesalers | 2,068 | 30.2% | 74.6% | 361 | — |
| 3116 | Animal slaughtering and processing | 3,149 | 42.7% | 77.2% | 559 | — |
| 311411 | Frozen fruit, juice and vegetable manufacturing | 140 | 58.4% | 97.4% | 1,035 | — |

- **The NAICS level changes the answer.** At 4 digits, 3114 looks mixed (64.2%). One level down, 311411 fails K10 (97.4%) and is "moderately concentrated" even on the 2023 HHI bands. That is the §10 NAICS-level caveat, seen on the shipper side.
- **The produce distributors Silo chose (R29) sit in 424480.** It is mixed, with 73% of receipts in firms under 500 employees.

**Verdict D4:** the measures agree at both ends: local and specialized trucking are fragmented, and couriers are concentrated. They disagree only on LTL and refrigerated warehousing. The antitrust measures cannot rank the fragmented middle. Owner-operators make trucking more fragmented than the census shows, and put LTL's K10 result within a few points of flipping.
**Implications for S0:**
- Keep the top-50 share for zones. Add a tie-breaker near the 80% line, and record the small-firm share for each side.
- Use 6-digit codes on both sides where they exist; the 3114 versus 311411 example argues for this [our call].
- Until the entry side is chosen (F-5, deferred), K10 can only fail a candidate when **both** sides fail it. Otherwise it simply records which side is ruled out. This follows C5's "better side" rule [our call].

### D5. Incumbents: a count and "a slice of the pie" for a freight job

**Sources, what they give, and what they cost:**

| Source type | What it gives | Access in this check | Gives shares? |
|---|---|---|---|
| Software directories (G2, Capterra) | Vendor lists by category | G2 blocked (403); a G2 page is titled "Best 76 Free Transportation Management Systems (TMS)" (N-D37, *assumed*). Capterra's category URLs returned 404 | No; a count only |
| Analyst reports | Gartner's TMS Magic Quadrant: "Gartner evaluated 17 vendors", 24 Mar 2025 (N-D32, via a vendor page). Gartner's *Market Guide for Freight Audit and Payment*, 10 Feb 2026 (N-D33; vendor list not seen). Armstrong: $4.5B of US 3PL contract software (R33) | Reports paywalled | Gartner share data not found in open sources |
| User surveys | Brush Pass: which TMS 895 micro-cap brokers use (N-B04; chart viewed here) | Chart is public | **Yes**, the share of brokerages on each system |
| Funding databases and trade lists (Crunchbase, FreightWaves FreightTech 100) | Who is funded, and who is new | Not checked | No |
| Public filings | Cass: volume paid, and its own view of competitors (N-D30). U.S. Bank: volume (N-D31). Descartes: acquisitions (N-B24, N-B25) | Free | Volumes, which become shares once a total is chosen |
| Service firms that do the job | 3PL gainshares (R33), audit firms on contingency (N-A25, N-A26), factoring (N-B03) | — | Firm counts from census codes; no shares for the specific job |

**Can CRn or HHI be applied to vendors at desk-stage cost?**
- **Yes, where a survey or published volumes exist.**
- **Otherwise the only desk measure is a count of significant competitors.** That is exactly what the 2023 guidelines fall back on when shares are hard to measure (N-D07, footnote 12).
- **For many jobs the honest desk answer is "unknown until S5"** [our call].

**Worked example 1: TMS for small brokers** (micro-cap brokers with $1-9.9M of gross revenue, March 2025). The shares below were read off the N-B04 chart, to about ±0.5 points [our reading]. The chart does not say whether shares are of brokerages or of revenue; brokerages is *assumed*.
- **Count:** 20 named systems, holding about 74% between them; about 26% is other systems. G2 lists at least 76 free TMS products (*assumed*).
- **Slices:**
  - McLeod: about 16%.
  - Proprietary or homegrown systems: about 13%.
  - ITS Dispatch (Truckstop): about 9%.
  - Ascend: about 6%.
  - Aljex (Descartes): about 4%.
  - Every other system: under 4%.
- **Measures [our calc]:**
  - Vendor CR4 is about 36%, or 44% if homegrown systems count as one competitor.
  - The HHI is about 450 for vendors only, and about 610 with homegrown included. That is like 16-22 equal-sized vendors, "unconcentrated" on the 2023 bands and "low" on CR4.
  - The leader's 16% is well under the 30% line in the 2023 guidelines, and under Tidemark's "40%+" for vertical leaders (N-A34).
- **Reading:** many incumbents, none of them dominant, and about 13% of brokers on homegrown systems. "Few incumbents" is false here, as check B found. By Porter's rivalry test, "Competitors are numerous or are roughly equal in size" (R43), which signals price competition.

**Worked example 2: freight audit and payment (FAP) for small and mid-sized shippers.**
- **Count:** Cass says "Competition consists of a few primary competitors and numerous small transportation bill audit firms ... few of these audit firms compete on a national basis" (N-D30, *verified*). Gartner publishes a market guide (N-D33); its list of vendors was not seen.
- **Slices [our calc]:**
  - Cass paid $36.4B of transportation bills in 2025, across 34.5 million invoices (N-D30).
  - U.S. Bank Freight Payment processes "$46 billion in freight payments ... annually" (N-D31).
  - Against 2024 US trucking revenue of $906B (N-B01, *verified*), that is about 4% and 5%, or about 9% together.
  - The comparison is rough: the payment volumes include modes other than trucking, and ATA's revenue figure includes private fleets.
- **Reading:** the two leaders are the "primary competitors", yet each touches only about 5% of the freight pie.
  - Most freight bills, probably including most SMB shippers' bills, pass through no FAP provider at all (*assumed*, an inference).
  - For those shippers the real incumbent is their own accounts-payable clerk, or nobody.
  - Proven spend on the job exists: audit firms work for 25-50% of what they recover (N-A25, N-A26).

**Worked example 3: detention and accessorial billing for carriers.**
- **Count:**
  - A carrier-software vendor's August 2026 guide lists seven tools: five TMSs (including Trimble TMW and McLeod), one telematics/ELD platform (Samsara) and one driver-management platform (N-D34, *verified*). (ELD: electronic logging device.)
  - One standalone tool, ChargeGuard, sells "detention and accessorial charge recovery" to carriers with 5-150 trucks, at $59-$349 a month (N-D35, *verified*).
- **Slices:** no shares are published anywhere that was found, so CRn and HHI cannot be computed.
- **Reading:**
  - The job is mostly a feature inside TMS and telematics products, plus spreadsheets.
  - The guide claims "most tools only show _that a driver waited_", and that "carriers using manual processes often capture only around 40% of the detention they're owed" (N-D34; vendor claims, *assumed* as facts).
  - ATRI puts detention at 135.9 million driver-hours a year (R38).
  - As a standalone category, "few incumbents" may hold here. This is also the job where the ability to pay a fee is least proven: the truckload profit margin is -2.3% (R38).

**Verdict D5:** a ballpark count is cheap for most jobs. A slice of the pie is cheap only where a survey or public volumes exist: TMS yes, FAP roughly, detention no. The count must include service firms, features bundled into larger products, and in-house work. Otherwise a job will look "empty" when the real incumbent is a clerk or a TMS module.
**Implications for S0:** for each job, S3 fact-sheet item 9 should record:
- the number of named software vendors;
- the largest vendor's share, if known;
- the service firms that do the job;
- how the job is done today.

Mark each figure *verified* or *assumed*.

### D6. What incumbent count and share mean for a new entrant

**Evidence that incumbents hurt** (*verified* unless marked):
- **a16z:** vertical markets "tend to have winner-take-most dynamics". "Once one software solution demonstrates its value, the customer base will consolidate around that company". Veeva "has over 50% market share" (N-B11).
- **Bessemer:** "CDK, R&R, and Cox—have chased away dozens of new entrants" (N-B08).
- **Across the whole economy:**
  - The Hamilton Project reports that concentration is rising and "Start-up rates are declining across all sectors" (N-D25). That is a correlation, not a cause.
  - Audretsch and Mahmood's study of 12,000+ new establishments relates their survival to "technological and market structure environments" (N-D26, abstract). The claim that concentration lowered survival comes only from secondary summaries (*assumed*).

**Evidence that incumbents are normal, or a sign of demand:**
- **CB Insights, 101 startup failure write-ups (report dated 2016):** "not targeting a 'market need'" was cited in "42% of cases"; being outcompeted in "19%" (N-D29). The sample is failures that chose to publish, not a random one.
- **Golder and Tellis, about 500 brands in 50 product categories:** "almost half of market pioneers fail", while "early market leaders have much greater long-term success and enter an average of 13 years after pioneers" (N-D28). Being first into an empty field is not the documented advantage.
- **Toast** entered against Micros and NCR, each with about 25% share (N-B19).
- **Paul Graham:** "A crowded market is actually a good sign" (N-B14).
- **Constellation:** "most vertical markets have several viable competitors" (N-B12).
- **Concentration itself is ambiguous.** In the 1990s, "at low levels of initial concentration, we find evidence of efficient concentration driven by tougher price competition". After 2000, concentration went with lower investment and higher prices (Covarrubias, Gutiérrez, Philippon, N-D24; the second point from the abstract summary).

**What this means for each approach** [our call, from the evidence above]:
- **(a) A hard cap, as a knock-out.**
  - No source supports a cap on the *number* of competitors.
  - A cap on the leaders' share below 25% would have removed Toast's market. A count cap would remove every TMS job (20+ systems, D5). Either kind of cap favours empty fields, which is what the failure data warn about.
  - What is supported is a cap on *dominance*: one vertical vendor already serving most customers for the job (N-B11, N-B08). No source gives a number. The 30% line in the 2023 guidelines and Veeva's 50%+ are reference points, not tests.
- **(b) Count plus shares, scored in W4.**
  - It can be measured for some jobs but not others (D5), so candidates are scored unevenly.
  - Its direction is unclear: many vendors can mean demand (Graham) or fierce rivalry (Porter).
  - No study shows that fewer vendors leads to better outcomes for an entrant.
- **(c) Proven spend plus weak, legacy or missing software (parked change 4).**
  - This fits the cases best: Toast; Cohen's advice to target companies that "outsource this particular problem" (R19); Bessemer's white space (N-B08); Emergence's "Dissatisfaction with Incumbents" (R21).
  - Its weakness is that it needs S5 evidence. At the desk it will often score 0.5.
- **(d) A combination.** Score W4 as in (c). Record the count and leader share from (b) on the fact sheet as W4's evidence. Veto only for a dominant vendor. This keeps the founders' "ballpark count and slice" as data without letting an empty field score well.

**Verdict D6:** the evidence treats missing demand as a bigger danger than the presence of competitors. It supports worrying about one dominant vendor, not about many small ones. No empirical study tests any of approaches (a)-(d) for SaaS.
**Implications for S0:** O-5 should not be a cap on the number of competitors. If the founders want a knock-out, tie it to dominance.

---

## 3. Options (D7). All **[our call]**, for the founders to decide

### 3.1 O-4: the fragmentation measure, its bands, K10 and A4

| Option | Measure and bands | K10 (applies only when selling to SMBs) | A4 (parked change 6) | Pros | Cons |
|---|---|---|---|---|---|
| **A. Keep today's default** | Top-50 share: under 20% fragmented, 20-80% mixed, over 80% concentrated | Fail if top-50 > 80% | Band score: fragmented 1, mixed 0.5, concentrated 0 | Published for all codes; matches R20 and R21; already in §8.2 | Uses Emergence's 80% the reverse way; blind to one dominant firm; LTL sits on the line; ignores owner-operators |
| **B. Antitrust HHI** | HHI on the 2023 bands; numbers-equivalent for A4 | Fail if HHI > 1,800. Where the HHI is withheld, use its floor from the CR bands | By numbers-equivalent: 100+ equal firms = 1, 20-100 = 0.5, under 20 = 0 | The regulators' standard; spots a dominant firm | Built for mergers. Every freight code except couriers is "unconcentrated", so it cannot rank them. LTL passes. Withheld for some codes |
| **C. Top-50 plus a small-firm tie-breaker** | Top-50 bands as in A. SUSB share of receipts in firms under 500 employees, recorded per side. HHI and CR4 as a dominant-firm check | Fail if top-50 > 85%. If 75-85%, mark "unknown" and settle it in S3: fail if firms under 500 employees hold less than 20% of receipts | The A band score, plus 0.5 if firms under 20 employees hold 25% or more of receipts, capped at 1 | Keeps today's scale; adds a direct measure of the SMB market; uses S2's "unknown" rule for cases near the line | Two numbers per side. SUSB has noise added and comes out every 5 years. The 20% and 25% cut-offs are ours |
| **D. An SMB revenue pool replaces K10** | SUSB small-firm share only | No separate K10. K5 is tested on the revenue held by firms under 500 employees (fee assumptions stay deferred) | 50% or more of receipts in firms under 500 employees = 1, 20-50% = 0.5, under 20% = 0 | Measures exactly what the founders want: SMBs. No double knock-out | Drops a published concentration statistic; employee count is not revenue; untested |

**Worked example [our calc]:**

| Candidate side | A | B | C | D |
|---|---|---|---|---|
| LTL (top-50 82.9%; HHI 572; 17.5% of receipts in firms under 500 employees) | Fails K10 | Passes K10; A4 0 (17 equal firms) | Unknown at S2, fails at S3 (17.5% < 20%) | A4 0; the SMB pool is about $11.6B of receipts |
| Refrigerated warehousing (73.9%; 2017 HHI 584; 41.5%) | Passes; A4 0.5 | Passes; A4 0 | Passes; A4 0.5 | A4 0.5 |
| Brokers (34.3%; HHI 43; 61.9%, and 24.1% in firms under 20 employees) | Passes; A4 0.5 | Passes; A4 1 | Passes; A4 0.5 | A4 1 |
| Local general freight (10.5%; HHI 3; 89.2% and 51.7%) | Passes; A4 1 | Passes; A4 1 | Passes; A4 1 | A4 1 |
| Couriers (90.9%; HHI at least 1,923; 9.6%) | Fails | Fails | Fails | A4 0; small SMB pool |

**The "reachable count" part of parked change 6.** A1 already multiplies the number of buyers by the fee, so counting buyers again in A4 counts them twice (check B, B5).
- If the founders still want count inside A4, score it only as a floor for word of mouth and resilience. For example: at least 1,000 firms in the size band we would sell to, pass or fail [our call].
- Otherwise, leave count in A1 and K5.

**Suggested starting point [our call]: option C.** It keeps the published top-50 scale the process already uses. It adds the one measure that directly answers "is there an SMB market?". And it treats LTL-type cases near the line as an S3 question rather than a desk verdict.

### 3.2 O-5: the incumbents measure

| Option | Measure | Knock-out or score | W4 (parked change 4) | Pros | Cons |
|---|---|---|---|---|---|
| **A. Count cap** | Number of established vendors for the job; for example, fail above 5 [our call] | Knock-out at S2 | Unchanged | The founders' first instinct; simple | No evidence supports it. It removes every TMS job and favours empty fields (42% "no market need", N-D29). Counts are hard to compare across jobs |
| **B. Count plus shares, scored** | Number of significant vendors, and the leader's share (CR4 or HHI where data exist) | W4 row | 1 if few vendors and none above about 20%; 0.5 if many vendors and no leader; 0 if one vendor holds more than about 40% [our call] | Uses the founders' "ballpark number ... and their slice of the market pie"; HHI where a survey exists | Shares missing for most jobs; what "many vendors" means is ambiguous; misses service firms and in-house work unless they are added |
| **C. Proven spend plus weak incumbents** (parked change 4) | Evidence that customers pay for the job today (a service firm, software or staff time), and that today's software for it is weak, legacy or missing | W4 row | 1 if both hold, 0.5 if one does, 0 if neither | Best supported by the cases (D6); rewards demand, not emptiness | Needs S5 evidence; count and share are not scored |
| **D. C, plus an incumbent map and a dominance veto** | Score as in C. Record the count, leader share and service firms on the S3 fact sheet as W4's evidence. Show-stopper only if one vendor already serves most target customers for the job *and* they report being satisfied [our call] | Scored. The dominance veto is applied at S4 through the §5.5 show-stopper, not at S2 | As in C | Keeps the founders' count and slice as data; guards against winner-take-most (N-B11) without a count cap | The most work per candidate; "most" and "satisfied" need S5 checks |

**Worked example [our call; figures from D5]:**

| Job | A (cap at 5 vendors) | B | C | D |
|---|---|---|---|---|
| Small-broker TMS (20+ systems; leader about 16%; about 13% homegrown) | Fails | 0.5 (many vendors, no leader) | Spend yes. Software weak for part of the market (homegrown systems and small vendors, *assumed*). Score 0.5-1 | As C; no veto (the leader has 16%) |
| FAP for SMB shippers ("a few primary" plus "numerous small" firms; the two leaders touch about 9% of trucking spend) | Unknown: how many count as "established"? | 0.5, low confidence | Spend yes (audit contingencies, N-A25/N-A26). Software for SMB shippers unknown. 0.5 at the desk | As C; no veto |
| Detention billing for carriers (features inside TMS and ELD; a few standalone tools; no shares) | Passes | 1 (few standalone tools), low confidence | Spend: staff time and uncollected detention (R38; vendor claims), 0.5. Software weak ("only show that a driver waited", *assumed*), 1. Score 0.5-1 | As C; no veto |

The count-based options, A and B, match the founders' instinct: they rank detention first and TMS last. C and D score on evidence of demand and weak software instead, which leaves the three jobs close until S5 [our call].

**Suggested starting point [our call]: option D.** It keeps the founders' ballpark count and slice as recorded evidence. It scores W4 the way the cases support (parked change 4). And it replaces a count cap with the one veto the sources back: a dominant vendor.

---

## 4. Open questions for the founders

1. **What should K10 protect against?** "Too little of the revenue sits with small firms", or "a few buyers are big enough to dictate terms"? The first points to the small-firm share (O-4 option C or D), the second to the top-50 share or HHI (A or B).
2. **Is 80% a hard line,** or is a 75-85% "unknown" band, settled in S3, acceptable? LTL at 82.9% is the test case.
3. **Should owner-operators count?** Adding Nonemployer Statistics lowers trucking's top-50 share from 28.3% to 22.3% (D4). The firm-size floor (F-6) is still deferred.
4. **Until the entry side is chosen, should K10 fail a candidate only when both sides fail?** That would follow C5's "better side" rule.
5. **Which NAICS level on the shipper side?** 3114 looks mixed at 4 digits; 311411 is concentrated at 6 (D4).
6. **A4: structure only, or structure plus a floor on the reachable count?** The count is already inside A1 (check B, B5).
7. **"Few incumbents" of what?** Software vendors only, or also service firms (3PLs, auditors, factoring companies), TMS features and in-house staff? D5 shows the answer changes the count for every job.
8. **A cap or a score?** If a knock-out is still wanted, should it be on the *number* of competitors or on one competitor's *dominance*? And what counts as dominant: more than half of the target customers (Veeva-like, N-B11), or another line?
9. **Unknowns at the desk:** accept that shares will be unknown for most jobs and scored 0.5 until S5?

---

## 5. Sources

### 5.1 New sources (N-D)

| ID | Source (author / org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-D01 | Economic Census, *Concentration of Largest Firms*: EC2200SIZECONCEN and EC1700SIZECONCEN (US Census Bureau). The same files as R44, re-parsed here for all sectors and for shipper codes | 2022 file released 10 Apr 2025; 2017 file Nov 2020 | https://www2.census.gov/programs-surveys/economic-census/data/2022/sector00/EC2200SIZECONCEN.zip ; …/2017/sector00/EC1700SIZECONCEN.zip | full (downloaded and parsed) | CR4-CR50, HHI and flags for sectors 21-81; freight and shipper rows |
| N-D02 | *What's New for the 2017 Economic Census* (US Census Bureau) | 2017 cycle | https://www.census.gov/programs-surveys/economic-census/year/2017/economic-census-2017/news-updates/whats-new.html | full | "HHI is calculated using the top 50 firms. 2017 is the first time HHI is available for sectors other than Manufacturing." |
| N-D03 | Economic Census Data Dictionary, 2022 (US Census Bureau) | 2022 cycle | https://www.census.gov/programs-surveys/economic-census/year/2022/technical-documentation/data-dictionary.html | full (via WebFetch) | Flag "D": "Withheld to avoid disclosing data for individual companies; data are included in higher level totals" |
| N-D04 | Statistics of U.S. Businesses: *... by State, Industry, and Enterprise Employment Size: 2022* (US Census Bureau) | released 10 Apr 2025 | https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.xlsx | full (downloaded and parsed) | Firms and receipts by employment size for freight and shipper codes; the noise-flag sheet |
| N-D05 | Nonemployer Statistics 2022, US file (US Census Bureau) | file dated Oct 2024 | https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/2022/historical-datasets/nonemp22us.zip | full (downloaded and parsed) | Counts and receipts for 484, 4841, 48411, 48412, 4842, 488, 492 and 493 |
| N-D06 | *Herfindahl-Hirschman Index* (US DOJ Antitrust Division) | updated 17 Jan 2024 | https://www.justice.gov/atr/herfindahl-hirschman-index | full (via WebFetch) | Formula, the 30/30/20/20 example, the 2023 bands |
| N-D07 | *Merger Guidelines* (US DOJ and FTC) | 18 Dec 2023 | https://www.justice.gov/d9/2023-12/2023%20Merger%20Guidelines.pdf | full (PDF text) | §2.1 (Guideline 1); footnotes 12-16 |
| N-D08 | *Horizontal Merger Guidelines* (US DOJ and FTC) | 19 Aug 2010 | https://www.justice.gov/sites/default/files/atr/legacy/2010/08/19/hmg-2010.pdf | full (PDF text) | §5.3: HHI bands and their purpose |
| N-D09 | *Guidelines on the assessment of horizontal mergers*, 2004/C 31/03 (European Commission) | OJ C 31, 5 Feb 2004 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52004XC0205(02) | full (HTML) | ¶¶17-21 |
| N-D10 | *Market Concentration*, issues paper DAF/COMP/WD(2018)46 (OECD Secretariat) | 20 Apr 2018 | https://www.oecd.org/content/dam/oecd/en/publications/reports/2018/04/market-concentration_30ddfcc7/7231c298-en.pdf | full (PDF text) | ¶¶19-21 and 33-34 |
| N-D11 | *On the Concept of Market Concentration, the Minimum Herfindahl-Hirschman Index, and Its Practical Application* (Algirdas Krivka, Panoeconomicus 63(5): 525-540) | 2016 | http://panoeconomicus.org/index.php/jorunal/article/download/2/2 | full (PDF text) | Survey of concentration measures |
| N-D12 | *Comment on the "H" Concentration Measure as a Numbers-Equivalent* (M. A. Adelman, Review of Economics and Statistics 51(1): 99-101) | Feb 1969 | https://www.jstor.org/stable/1926955 | **not read**; citation via search | The numbers-equivalent idea (*assumed*) |
| N-D13 | *The Market Structure of the U.S. Economy in 1997* (Fatma Abdel-Raouf, Southwestern Economic Review) | date not captured | https://swer.wtamu.edu/sites/default/files/Data/171-186-26-85-1-PB.pdf | full (PDF text) | CR4 structure bands; Shepherd's categories as reported |
| N-D14 | Shepherd, *Causes of Increased Competition in the U.S. Economy, 1939-1980* (Review of Economics and Statistics 64(4)); Shepherd and Shepherd (2004) | 1982; 2004 | https://ideas.repec.org/a/tpr/restat/v64y1982i4p613-26.html | **not read**; seen only through N-D13 and search | The CR4 bands at source (*assumed*) |
| N-D15 | *Industry Reports* help article (IBISWorld Help Center) | undated | https://help.ibisworld.com/en/articles/8149882-industry-reports | full (via WebFetch) | The top-four share measure and the "major player" definition. The concentration bands come only from search snippets (*assumed*) |
| N-D16 | *What Makes a Market an Oligopoly?* (Heather Hennerich, Federal Reserve Bank of St. Louis) | 17 May 2023 | https://www.stlouisfed.org/open-vault/2023/may/what-makes-a-market-an-oligopoly | full (via WebFetch) | Concentration-ratio definition; the top-five 60% rule of thumb |
| N-D17 | *Market Liberalization and its Relationship with Market Structure, Conduct and Performance of the Food Processing Industry in ASEAN Economies* (eds. Tengku Mohd Ariff Tengku Ahmad and Mad Nasir Shamsudin; APEC ATCWG) | Apr 2008 | https://www.apec.org/docs/default-source/Publications/2008/4/Market-Liberalization-and-its-Relationship-with-Market-Structure-Conduct-and-Performance-of-the-Food/08_atc_mktlib_rpt.pdf | partial (literature review) | Bain's (1951) 70% CR8 split |
| N-D18 | *Classification of the market concentration by the Bain criterion (1959)* (ResearchGate table) | — | https://www.researchgate.net/figure/Classification-of-the-market-concentration-by-the-Bain-criterion-1959-Kinds-of_tbl3_328624801 | **blocked** (403); search summary only | Bain's classes (*assumed*; not used) |
| N-D19 | Porter, *Competitive Strategy* (1980), ch. 9, via secondary pages (slm.mba; Brainscape) | 1980 | https://slm.mba/mmpc-012/competitive-strategy-in-fragmented-industries/ | secondary only; book not read (zoboko.com blocked) | Definition of a fragmented industry (*assumed*) |
| N-D20 | *Inorganic growth strategies and the evolution of the private equity business model* (Hammer, Knauer, Pflücke, Schwetzler; Journal of Corporate Finance 45: 31-63) | 2017 | https://ideas.repec.org/a/eee/corfin/v45y2017icp31-63.html ; manuscript: https://isidl.com/wp-content/uploads/2017/11/E5054-ISIDL.pdf | abstract (IDEAS), plus the accepted manuscript's text searched | Fragmentation hypothesis, HHI bands, summary statistics |
| N-D21 | *How Private Equity Firms Can Ace Buy-and-Build* (Douglas, Mohammed, Zeisberger; INSEAD Knowledge) | 28 May 2025 | https://knowledge.insead.edu/economics-finance/how-private-equity-firms-can-ace-buy-and-build | full (via WebFetch) | "especially in fragmented markets"; no threshold |
| N-D22 | Practitioner roll-up blogs: dealroom.net (read); growthshuttle.com and capitalpad.com (search snippets only) | 2025-26 | https://dealroom.net/blog/what-is-a-private-equity-roll-up-strategy | dealroom read; the others *assumed* | Qualitative criteria; unsourced numeric thresholds |
| N-D23 | *Advanced Technologies Adoption and Use by U.S. Firms: Evidence from the Annual Business Survey* (Zolas, Kroff, Brynjolfsson et al.; CES Working Paper 20-40) | Dec 2020 | https://www2.census.gov/ces/wp/2020/CES-WP-20-40.pdf | abstract (PDF text) | Adoption skewed to larger and older firms |
| N-D24 | *From Good to Bad Concentration? U.S. Industries over the Past 30 Years* (Covarrubias, Gutiérrez, Philippon; NBER w25983) | Jun 2019 | https://www.nber.org/papers/w25983 | abstract (via WebFetch; partly a summary) | Efficient versus harmful concentration |
| N-D25 | *The state of competition and dynamism: Facts about concentration, start-ups, and related policies* (Shambaugh, Nunn, Breitwieser, Liu; Hamilton Project) | 13 Jun 2018 | https://www.hamiltonproject.org/publication/economic-fact/the-state-of-competition-and-dynamism-facts-about-concentration-start-ups-and-related-policies/ | full (via WebFetch) | Facts 1-4 and 9-12 |
| N-D26 | *New Firm Survival: New Results Using a Hazard Function* (Audretsch and Mahmood; Review of Economics and Statistics 77(1): 97-103) | 1995 | https://econpapers.repec.org/article/tprrestat/v_3a77_3ay_3a1995_3ai_3a1_3ap_3a97-103.htm | abstract only | Sample and purpose. The concentration result comes from secondary summaries (*assumed*) |
| N-D27 | *What do we know about entry?* (P. Geroski; International Journal of Industrial Organization 13(4): 421-440) | 1995 | https://econpapers.repec.org/RePEc:eee:indorg:v:13:y:1995:i:4:p:421-440 | **not read** (paywalled; no abstract shown) | Not used |
| N-D28 | *Pioneer Advantage: Marketing Logic or Marketing Legend?* (Golder and Tellis; Journal of Marketing Research 30(2): 158-170) | May 1993 | https://gtellis.net/wp-content/uploads/2020/09/pioneering-advantage-marketing-logic-or-marketing-legend.pdf | abstract (PDF text) | Pioneer failure; early leaders enter 13 years later |
| N-D29 | *The Top 20 Reasons Startups Fail* (CB Insights) | PDF dated 27 Jul 2016 | https://s3-us-west-2.amazonaws.com/cbi-content/research-reports/The-20-Reasons-Startups-Fail.pdf | full (PDF text) | 101 failure write-ups; 42% no market need; 19% outcompeted |
| N-D30 | Cass Information Systems, Form 10-K for FY2025 (SEC) | filed 2026 | https://www.sec.gov/Archives/edgar/data/708781/000070878126000010/cass-20251231.htm | full text downloaded and searched | Competition section; 2025 transportation volumes |
| N-D31 | *U.S. Bank Freight Payment Index: Shippers pay more as trucking capacity tightens* (U.S. Bancorp) | 4 Aug 2026 | https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Freight-Payment-Index-Shippers-pay-more-as-trucking-capacity-tightens/default.aspx | full (via WebFetch) | "$46 billion in freight payments processed annually" |
| N-D32 | Gartner, *Magic Quadrant for Transportation Management Systems* 2025, as described on Alpega's page | 24 Mar 2025 | https://www.alpegagroup.com/en-en/community/library/2025-gartner-magic-quadrant-for-transportation-management-systems-tms/ | vendor page read; the report is paywalled | "Gartner evaluated 17 vendors" |
| N-D33 | Freehand press release citing "Gartner Market Guide for Freight Audit and Payment, Brian Day, Brian Whitlock, Matthew Beckett, 10 February 2026" (GlobeNewswire) | 19 Feb 2026 | https://www.globenewswire.com/news-release/2026/02/19/3240923/0/en/freehand-recognized-in-the-2026-gartner-market-guide-for-freight-audit-and-payment-providers.html | full; the guide itself not seen | The guide exists; no vendor count given |
| N-D34 | *Driver Detention Management Software: 7 Top Tools for Carriers* (Connor McCormick, Toro TMS blog) | 17 Aug 2026 | https://www.torotms.com/blog/driver-detention-management-software | full (via WebFetch); vendor content | Tools listed; claims about current practice |
| N-D35 | ChargeGuard home page | undated | https://chargeguard.net/ | full (via WebFetch) | Product, target fleet sizes, pricing; it cites ATRI (*assumed*) |
| N-D36 | Descartes Systems Group, Form 6-K Exhibit 99.1 (MD&A for Q2 of fiscal 2026, period to 31 Jul 2025) (SEC) | 2025 | https://www.sec.gov/Archives/edgar/data/1050140/000141057825001927/dsgx-20250731xex99d1.htm | full text downloaded and searched | "highly fragmented community"; manual processes |
| N-D37 | G2, TMS category pages | 2026 | https://www.g2.com/categories/transportation-management-systems-tms/free | **blocked** (403); title from search | "Best 76 Free Transportation Management Systems (TMS)" (*assumed*) |

### 5.2 Existing sources reused (not re-fetched unless stated)
- **Reading notes:** R19, R20, R21, R27, R29, R33, R38, R41, R43, R44.
- **Check A:** N-A25, N-A26, N-A34.
- **Check B:**
  - N-B01: the ATA release again; its revenue sentence was newly read here: "In 2024, the industry saw revenues at $906 billion".
  - N-B04: its chart image was newly viewed here: "TMS Market Share for Micro-Cap Freight Brokerages ($1-$9.9m in Annual Gross Revenue) March 2025".
  - N-B11: the page was re-read to copy the "winner-take-most" passage.
  - Also: N-B03, N-B05, N-B08, N-B12, N-B14, N-B19, N-B24, N-B25.

### 5.3 Could not access, or used only second-hand
- **Blocked or paywalled:**
  - Bain's 1959 classification table (ResearchGate, 403).
  - Shepherd's own texts, Adelman (1969) and Geroski (1995).
  - IBISWorld's concentration bands (search snippets only; a library glossary page returned 404).
  - Porter's *Competitive Strategy* text (zoboko.com behind a bot check).
  - G2 (403), Capterra (404 on category URLs), Software Advice (404), DockClaim's comparison page (403), Gartner Peer Insights (403), ScienceDirect (403).
  - Gartner's TMS and FAP reports themselves, and any Gartner vendor market-share data (paywalled).
- **Worked around:** the Census API for nonemployer data redirected to a "missing key" page, so the flat file was used instead.
- **Not checked in this pass:** Crunchbase, FreightWaves FreightTech lists, and Trimble and WiseTech filings.
- **A correction for the R44 note (not edited here):** R44 reads the HHI "n/a" cells as "that row reports 0". The 2022 file flags those cells "D", meaning withheld (N-D03). They are not zeros.
