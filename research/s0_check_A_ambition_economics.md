# S0 check A: ambition, scale and unit economics

- **Date:** 2026-09-14. **Stage:** S0 ("set the rules") check of the founders' first S0 decisions, part A.
- **Scope:** questions A1–A6: ambition, scale, unit economics, founder base rates, fee share of savings, and vertical versus horizontal benchmarks. A second agent covers market structure, fragmentation, incumbents, SMB channels in freight, expansion, and the norms for scorecard weights.
- **Prior notes reused (cited by R-ID, not re-read at source):** R19 (Cohen), R23 (a16z), R24 and R42 (Euclid), R25 (Poyar), R33 (Armstrong).
- **New web sources:** N-A01 to N-A39, listed in §5 with URL, date and access status.
- **Labels:**
  - *verified* means read at the source during this check: page text, a PDF text layer, or a chart image viewed.
  - *assumed* means a search snippet, a secondary summary, or something that could not be checked.
  - **[our call]** marks our own arithmetic or judgement.
- **Founder's target, clarified 2026-09-14** (verbatim, relayed by the coordinator): "$10M Revenue, also just a $10M valuation as well. It could be $250K-$1M Profit I'd be more than happy." Two earlier readings are dropped as instructed: "$10M cumulative net profit" and "$10M founders' proceeds from a sale". The three readings used below are:
  - (a) STRETCH: about $10M ARR by year 5;
  - (b) a $10M company valuation;
  - (c) FLOOR: $250K–$1M profit per year.

---

## 1. Summary

**The target.** The founders' three readings of the 5-year target need very different revenue.
- The two outcomes they would be "more than happy" with come out at the same size, about **$2.5M ARR**:
  - A **$10M valuation** needs about $1.8–4.0M ARR at 2026 private-SaaS multiples of 2.5–5.5× (N-A07, N-A08, N-A09). At 4× that is $2.5M.
  - **$250K a year of profit** needs about $2.5M ARR at a 10% margin. That is the median margin bootstrapped SaaS firms of $3–5M ARR reported in 2025. The range runs from $0.83M ARR at a lean 30% margin to $5M ARR at the 5.5% median for all bootstrapped firms (N-A06).
- Only the **stretch**, $10M ARR, is four times larger.

**How often this happens.** In ChartMogul's 6,525-company dataset (N-A01):
- 25.1% of startups reach $1M ARR within five years of first revenue;
- one in ten reaches $10M ARR within ten years.

What that means for each reading:
- **The stretch** needs roughly upper-quartile growth in every year (N-A10), about the venture-backed "T2D3" track (N-A12). Two documented SMB vertical companies each took about seven years to reach ~$10M ARR: Mindbody and Levelset (N-A36, N-A37). So the floor is realistic but still a top-quartile result, and the stretch is a top-decile result that should not drive the plan.
- **Customer counts** (Janz's arithmetic, N-A14/N-A15):
  - The floor needs about 250 customers at a $10k annual fee per customer (ARPA), or 2,500 at $1k.
  - The stretch needs 1,000 or 10,000.

**Selling directly to small businesses** (SMBs) is how most B2B software starts, and direct sales is the most common go-to-market motion (N-A10). It stays economic past the first customers only when three things hold (N-A10, N-A13, N-A16, N-A20):
- the annual fee per customer is roughly $5k or more;
- the cost of winning a customer is paid back within about 12 months;
- gross revenue retention is about 88–90% or better.

Below about $5k a year per customer, the evidence points to self-serve, inbound or partner channels.

**Founder base rates.**
- First-time founders succeed less often than founders with a prior success: 20.9% versus 30.3% predicted IPO success, among venture-backed ventures from 1986–2000 (N-A22).
- Three or more years of prior work in the specific industry roughly doubles the chance of building a top-growth firm (N-A23).

**Fee shares near freight.**
- Audit services that do the recovery work keep 25–50% of what they recover (N-A25, N-A26, N-A27).
- Managed-transportation gainshares split 50/50 (*assumed*; N-A30).
- Large government recovery audits pay 9–12.5% (N-A28).
- Energy service companies that finance the equipment take 85% (N-A29).
- A fee for software alone should be planned at 10–25%.

**Vertical versus horizontal software.**
- Vertical SaaS is not verifiably faster-growing than horizontal SaaS.
- Its retention edge is small: gross retention 92% versus 90%, net retention 101% versus 102% (N-A16).
- Its market leaders can hold much larger shares: over 40% versus under 20% (N-A34).

**Recommendation [our call].**
- **Set the K5 size floor from the "more than happy" outcome.** The entry segment should hold a fee pool of about **$25M a year or more** (reachable businesses × realistic annual fee), which is about $2.5M ARR at a 10% market share.
- **Treat the $10M ARR stretch as a ceiling test, not a knock-out.** The beachhead plus its adjacent segments should hold a fee pool of about **$50–100M a year**. Score this rather than knock candidates out on it.

---

## 2. Findings by question

### A1. What the 5-year target needs, and how common it is

#### A1.1 Base rates: who reaches $1M and $10M ARR, and how fast

| Source | Sample | Finding (exact quote or figure, and its location) | Label |
|---|---|---|---|
| ChartMogul, *Against the Odds: The 2025 SaaS Growth Report* (N-A01), 15 Oct 2025 | 6,525 software companies, over more than a decade, ChartMogul customers | "Almost half of software startups do eventually make it to $1 million ARR after they've started monetizing – if they're willing to stick around 10 years." "One-in-ten makes it to $10 million ARR. And just one out of every fifty startups make it to $25 million ARR within 10 years." Under "How long it really takes to hit your first million": 3.3% reach $1M in under a year, 13.4% within three years, 25.1% within five years. Caveat: "starting the clock at initial monetization and using a 10 year measurement window" | *verified*, checked on two copies: ChartMogul's page and Kyle Poyar's write-up |
| ChartMogul, *SaaS Growth Report 2023* (N-A02), 30 Aug 2023 | "over 2,200 SaaS businesses", 12 months to June 2023 | PDF p. 2: "Top-tier SaaS startups reach $1M ARR within 9 months. The median startup takes approximately 2 years and 9 months. On average, SaaS startups reach $10M ARR in slightly over 5 years. Even after 10 years in business, only 13 % of SaaS startups are able to hit the $10M ARR mark." p. 17: "Best-in-class SaaS businesses reach the $10M ARR mark in 2 years and 9 months. It takes the median startup a little more than 5 years." The report adds that its milestone data "naturally has survivorship bias" | *verified* (PDF text) |
| High Alpha, *2025 SaaS Benchmarks Report* (N-A10) | "800+ Respondents"; 69% US; 23% under $1M ARR; ICP 37% enterprise, 35% mid-market, 19% SMB, 7% micro-business (p. 8) | Median YoY growth, with the interquartile range, p. 11: under $1M ARR 100% [29–300%]; $1–5M 50% [24–100%]; $5–20M 31% [15–72%]; $20–50M 30% [16–41%]; over $50M 16% [10–29%] | *verified* (PDF) |
| SaaS Capital, *2026 Private B2B SaaS Company Growth Rate Benchmarks* (N-A03) | "more than 1,000 private B2B SaaS companies", 15th annual survey | "The median growth rate for all companies in the survey registered 22%". "Bootstrapped companies report median growth of 20%". "Equity-backed companies reported median growth of 25%" | *verified* |
| SaaS Capital, *Growth, Profitability, and the Rule of 40* (N-A06), 21 Aug 2025 | annual survey, by ARR band and funding | Charts 2 and 3 give median growth by ARR band. **Bootstrapped**: 25% (2025) and 34% (2023) at $1–3M; 12% and 29.5% at $3–5M; 24% and 34% at $5–10M; 18% and 26.5% at $10–20M. **Equity-backed**: 38% (2025) and 60% (2023) at $1–3M; 39% and 38% at $3–5M; 16.5% and 34% at $5–10M; 25% and 39% at $10–20M | *verified* (chart images viewed) |
| SaaS Capital, *2026 Benchmarking Metrics for Bootstrapped SaaS* (N-A05), 24 Apr 2026 | >1,000 companies | Bootstrapped firms at $3–20M ARR: median growth 15%, 90th percentile 42.3%; NRR 103%; GRR 91% | *verified* |
| KeyBanc Capital Markets & Sapphire Ventures, 2025 survey (N-A11), 13 Nov 2025 | 16th annual private-SaaS survey; the sample size is not stated in public text | "ARR growth is projected to accelerate from 15% in 2024 to 20% in 2025, marking the first rebound in three years" | *verified* (press release and landing page); full report gated |
| Neeraj Agrawal (Battery Ventures), *The SaaS Adventure*, TechCrunch (N-A12), 1 Feb 2015 | framework, no sample | T2D3 stages: establish product-market fit; reach $2M ARR, landing 30–60 starter clients in one to two years; then triple to $6M, triple to $18M, and double three times to $144M. The article says "this is not the only growth path to SaaS success" | *verified* |
| Bessemer, *Scaling to $100 Million* (N-A13), 21 Sep 2021 | Bessemer's cloud benchmarks | Average growth of about 200% for companies at $1–10M ARR (middle 50%: 100–230%) | *verified*. This is a VC's own picture of fast-growing, venture-backed companies, so treat it as an upper bound |

**Bias notes (*assumed* unless marked):**
- ChartMogul's customers include low-priced B2C and prosumer apps. B2B firms with a $5k+ annual fee per customer need far fewer customers per $1M, so they may reach milestones faster. ChartMogul's 2025 report does not split by price, so this is not measured.
- High Alpha's band medians describe the companies that are in each band today, which means survivors. Its sample is mostly venture-backed: median monthly burn at $1–5M ARR is $175k (p. 11, *verified*).

**Growth-path arithmetic [our call].** Assumptions:
- The company ends year 1 at $0.5M ARR (or $0.25M).
- Each later year it grows at the High Alpha 2025 median or upper-quartile rate for its current band (N-A10), or at SaaS Capital's 2025 bootstrapped median (N-A06). The bootstrapped path assumes 100% growth while ARR is under $1M.

| Path (ARR at end of year, $M) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| High Alpha median, starting from $0.5M | 0.50 | 1.00 | 1.50 | 2.25 | **3.38** |
| High Alpha upper quartile, starting from $0.5M | 0.50 | 2.00 | 4.00 | 8.00 | **13.76** |
| High Alpha median, starting from $0.25M | 0.25 | 0.50 | 1.00 | 1.50 | **2.25** |
| High Alpha upper quartile, starting from $0.25M | 0.25 | 1.00 | 2.00 | 4.00 | **8.00** |
| SaaS Capital bootstrapped median, starting from $0.5M | 0.50 | 1.00 | 1.25 | 1.56 | **1.95** |

Reading the paths:
- A company that performs like a median survivor every year ends year 5 at about $2–3.4M ARR. That matches readings (b) and (c).
- $10M by year 5 needs upper-quartile growth for four years in a row, starting from a strong first year.

#### A1.2 Reading (a), the stretch: $10M ARR by year 5

**For:**
- Top performers do it. ChartMogul's "best-in-class" reach $10M ARR in 2 years 9 months, and the 2023 median among those that got there was "a little more than 5 years" (N-A02).
- T2D3 reaches $18M ARR two years after the $2M mark, so about 3–4 years after product-market fit, since $2M itself takes "one to two years" (N-A12).

**Against:**
- Only 13% (2023) or one in ten (2025) reach $10M ARR even within ten years (N-A01, N-A02).
- The "5 years" median counts only the survivors that reached $10M.
- Documented vertical SMB companies were slower:
  - Levelset: "$0 to $1M took 18 months. $1M to $10M took 6 years. $10M to 20M took 18 months." (N-A37, *verified*)
  - Mindbody launched as a SaaS product in 2003. It "grown from $4.4m in recurring revenue in 2008 to $6.8m in 2009" and was "on plan to reach $11.4 in 2010" (N-A36, Bessemer memo of 2 Jul 2010, *verified*). That is about 7 years from SaaS launch to about $10M.

**Scale context [our call].** Euclid's venture bar is a path to a "$15B TAM / $100m ARR" (R42). T2D3 is a path to $144M. So even the stretch sits below venture scale. It is an "indie-plus" ambition: above Cohen's indie threshold (R19) and below Euclid's.

#### A1.3 Reading (b): a $10M valuation

**Multiples in 2025–2026:**
- **SaaS Capital Index** (public B2B SaaS; "There are currently 63 publicly-traded companies in the SCI"): the median multiple was **4.6× on 31 Aug 2026**. That is the chart annotation on the index page, viewed as an image (N-A08, *verified*). The multiple is "current Market Cap divided by annualized current run-rate revenue" (FAQ on the same page, *verified*). SaaS Capital's April 2026 post says the index hit "decade-plus lows" in Q1 2026 (N-A08, *verified*).
- **SaaS Capital's private-company model** (24 Jan 2025): "predicted private SaaS company valuation multiple of 4.8x" for bootstrapped firms and 5.3× for equity-backed ones, when the public index stood at 7.0×. The model's inputs are public multiples, ARR growth and NRR, from a survey of more than 1,500 companies (N-A07, *verified*).
  - [our call] If the private-to-public ratio (4.8/7.0) still holds with the index at 4.6×, bootstrapped private SaaS would sit near 3.2×. This assumes the ratio is stable.
- **FE International** (25 Aug 2026; a sell-side advisor on "more than 1,500 completed transactions since 2010"; N-A09, *verified*):
  - "Private SaaS businesses generally transact between 2x and 7x ARR in 2026".
  - Firms under $1M ARR are "usually priced on seller discretionary earnings at 2.5x to 4x SDE" (SDE: profit plus the owner's own pay). *Corrected 2026-09-14 on re-check by the coordinator; this line first said "2x to 3x".*
  - Firms at $5–10M ARR sell for "3.5x to 5.5x ARR".
  - "Businesses valued under roughly $5M are typically priced on a multiple of seller discretionary earnings", and above that EBITDA becomes the basis.
  - Advocacy note: sell-side advisors have an interest in quoting high multiples.

**Conversion [our call]: required ARR = $10M ÷ multiple.**

| Multiple | Why this value | ARR needed |
|---|---|---|
| Low: 2.5× | FE's floor of 2×, the scaled SaaS Capital estimate of about 3.2×, and a small firm's discount | **$4.0M** |
| Mid: 4.0× | Between the scaled bootstrapped estimate (about 3.2×) and FE's $5–10M band (3.5–5.5×) | **$2.5M** |
| High: 5.5× | Top of FE's $5–10M band, for a fast-growing, high-NRR firm | **$1.8M** |

**Caveat.** A valuation is not cash. It becomes real only in a sale or a priced funding round. Below about $5M of value, buyers price on SDE (N-A09), so a $10M valuation effectively means a company in the ARR-multiple range of more than about $1–2M ARR. That is consistent with the table.

#### A1.4 Reading (c), the floor: $250K–$1M profit per year

**Margins of small private SaaS companies:**
- **SaaS Capital, spending, 10 Jun 2026** (N-A04, *verified*):
  - Median total spend is "96% of Annual Recurring Revenue (ARR)" for bootstrapped firms and "101% of ARR" for equity-backed ones.
  - "83% of bootstrapped companies are operating within two percentage points of breakeven or are profitable while only 52% of equity-backed are breakeven or profitable."
- **SaaS Capital, Rule of 40, 21 Aug 2025** (N-A06, charts 1–3, *verified* from the images). The charts label the metric "Profitability"; we read it as an EBITDA-type margin (*assumed*).

  | ARR band | Bootstrapped margin, 2025 (2023) | Equity-backed margin, 2025 (2023) | Bootstrapped median Rule of 40, 2025 |
  |---|---|---|---|
  | $1–3M | 4.5% (0%) | −8% (−53%) | 45.5 |
  | $3–5M | 10% (19.5%) | −20% (−20%) | 25 |
  | $5–10M | 4% (9.5%) | −11.5% (−27%) | 29 |
  | $10–20M | 0% (16%) | −5.5% (−19.5%) | 20 |
  | All companies | 5.5% (9%) | −7% (−20%) | 34.5 |

- **KeyBanc/Sapphire 2025:** "EBITDA margins have steadily improved since 2022 and are expected to turn positive by 2026" (N-A11, *verified*). The typical survey firm is venture-backed and loss-making.
- **Bessemer, 2022:** "The sum of a company's revenue growth and FCF margin should be as high as possible (ideally above 40)." (N-A35, *verified*). [our call] A firm that deliberately grows only about 10% a year while staying at the Rule-of-40 line would run about a 30% margin. That is our "lean" case.
- Blog claims of 64% or 70–90% margins for one-person "micro-SaaS" were found but not used (*assumed*). They describe tiny apps with no sales or support staff, not a freight SaaS that sells to businesses.

**Conversion [our call]: required ARR = annual profit ÷ margin.**

| Margin | Why this value | ARR for $250K profit | ARR for $1M profit |
|---|---|---|---|
| 5% | Bootstrapped median, all companies, 2025 (5.5%) | $5.0M | $20M |
| **10%** | Bootstrapped median at $3–5M, 2025 | **$2.5M** | $10M |
| 20% | Bootstrapped $3–5M in 2023 (19.5%); a disciplined operator | $1.25M | $5.0M |
| 30% | A lean firm at the Rule-of-40 line growing about 10% | $0.83M | $3.3M |

**Notes:**
- **"Profit" needs a definition.** If the founders mean owner earnings that include their own pay (SDE, the basis FE uses below about $5M of value), the ARR needed falls. Two founders paying themselves $150k each would add $300k of SDE on top of EBITDA. That is an illustration only.
- **$1M a year of profit is effectively the stretch.** It needs $10M ARR at the median-like 10% margin, or $5M at 20%.
- **Base rate for the floor.** 25.1% of monetizing startups reach $1M ARR within five years (N-A01). The share reaching $2.5M in five years is not published, but it must be lower (inference).

#### A1 verdict

**Verdict: Partly supported.**
- **(c) the floor and (b) the valuation** both come out at about $2.5M ARR in year 5. That is a realistic but roughly top-quartile outcome for a new SaaS company, and it fits bootstrapped benchmarks.
- **(a) the stretch** is a top-decile, T2D3-like outcome. The documented vertical SMB companies did not hit it within 5 years.

**Implication for S0:**
- Record the ambition level as **"indie-plus"**: plan to about $2.5M ARR by year 5 and keep $10M ARR as an upside the market must allow.
- Decide explicitly how to fund it. SaaS Capital shows bootstrapped firms grow only slightly slower (20% versus 25%) but break even far more often (N-A03, N-A04).

---

### A2. The customer-count arithmetic (Janz)

**Christoph Janz (Point Nine Capital), 5 Oct 2014, "Five ways to build a $100 million business"** (N-A14, *verified*). The five ways:
- "1,000 enterprise customers paying you $100k+ per year each" (elephants);
- "10,000 medium-sized companies paying you $10k+ per year each" (deer);
- "100,000 small businesses paying you $1k+ per year each" (rabbits);
- "1 million consumers or 'prosumers' paying you $100+ per year each" (mice);
- "10 million active consumers who you monetize at $10+ per year each by selling ads" (flies).

On channels:
- For rabbits: "the closest thing to a silver bullet is inbound marketing".
- For deer: "you can use an inside sales force to close leads, potentially also to generate leads".

**Update, 7 Apr 2019, "Five years later: Five ways to build a $100 million SaaS business"** (N-A15, *verified*):
- The fly is dropped and a $1M-per-customer "whale" is added: "there are quite a few SaaS companies with a significant whale customer segment".
- Janz warns that "not all five ways are equally promising" and that "Most customer acquisition channels are either scalable or profitable but not both."
- The post argues that SMB models need either very low churn or a fee high enough to pay for outbound sales. That is our paraphrase of its argument.

**Scaled down [our call]:**

| Animal (annual fee per customer) | Customers for $100M (Janz) | For $10M, stretch (a) | For $2.5M, floor (c) / valuation (b) |
|---|---|---|---|
| Elephant ($100k) | 1,000 | 100 | 25 |
| Deer ($10k) | 10,000 | 1,000 | 250 |
| Rabbit ($1k) | 100,000 | 10,000 | 2,500 |
| Mouse ($100) | 1,000,000 | 100,000 | 25,000 |

**Cross-checks:**
- **Cohen (R19):** "1,000 paying customers is the minimum needed for a sustainable, small company" at $30–100 a month. He adds that for B2B "100k is sufficient" as the count of businesses that have the problem.
- **Euclid (R24):** "With an absolutel [sic] max of 10k buyers, a $7k ACV isn't going to cut it for a venture-scale outcome". [our call] The same 10,000 buyers at $7k a year is a $70M pool. The floor would need about 360 customers (a 3.6% share) and the stretch about 1,430 (a 14% share). A segment too small for VCs can still be large enough for the founders' targets.

**Verdict: Supported.** The arithmetic is definitional and was verified at source.

**Implication for S0:** choose the "animal" first, because the annual fee per customer (ARPA) decides which sales channel can pay for itself. "SMBs reached directly" points to deer, at about $5k–25k a year per customer, not rabbits (see A3). The founders' "many businesses" weight should count businesses that can pay at that level, not all businesses.

---

### A3. SMB economics: churn, payback, and when direct selling stops paying

**Retention by contract size.** Retention rises with ACV (annual contract value), and the ACV band is the right thing to benchmark against.

- **High Alpha 2025, p. 41, "ACVs Under $10k Are Most Challenged"** (N-A10, *verified*):

  | ACV band | Share of respondents | Median growth | Median GRR | Median NRR |
  |---|---|---|---|---|
  | Under $1k | 4% | 30% | 83% | 98% |
  | $1k–5k | 11% | 25% | 88% | 97% |
  | $5k–10k | 8% | 25% | 85% | 94% |
  | $10k–15k | 10% | 40% | 88% | 107% |
  | $15k–25k | 11% | 38% | 88% | 104% |
  | $25k–50k | 16% | 30% | 92% | 105% |
  | $50k–100k | 18% | 44% | 94% | 104% |
  | $100k–250k | 12% | 30% | 91% | 102% |
  | Over $250k | 9% | 32% | 92% | 105% |

  Quote: "At the low end, smaller contracts are prone to churn and limited expansion."

- **SaaS Capital, 2023 B2B SaaS Retention Benchmarks** (N-A16; "more than 1,500 private B2B SaaS companies"; excludes firms under $1M ARR; *verified*):
  - "For retention, benchmarking by ACV is the best starting point."
  - Figure 1, median NRR / GRR by ACV: under $12k 100% / 90%; $12–25k 102% / 90%; $25–50k 103% / 92%; $50–100k 105% / 93%; $100–250k 107% / 93%; over $250k 110% / 93%.
  - "Companies with ACVs above $25,000 show median gross revenue retention of ~93%, while companies below $25,000 show 90% median gross revenue retention."
  - The 2025 update adds that at $25–50k ACV median NRR is "102% with the top quartile reporting NRR of 111% and the lowest quartile reporting 97%" (N-A16, 18 Sep 2025, *verified*).
- **Bessemer 2021:** gross retention of 85–90% across scales, with SMB-focused businesses possibly at 70–80% (N-A13, *verified* that the page says this; the wording is from the page extraction, not an exact quote).
- **ChartMogul retention report, 2023:** "Only 2.7% of SaaS businesses with an ARPA less than $10/month have net retention rates over 100%" (N-A17, *verified*, partial read).
- **Mindbody in 2010, a working SMB vertical example** (N-A36, *verified*):
  - "average price of $75/mth per client"; "11% annualized churn and 2% net churn";
  - "blended customer acquisition cost of ~$1,100"; "13-15 month gross profit customer payback period".

**Payback on the cost of winning a customer (CAC payback) and cost norms:**
- **Bessemer 2021** (N-A13, *verified*): SMB-focused firms should "target CAC payback <12 months"; mid-market "<18 months"; enterprise "<24 months".
- **High Alpha 2025** (N-A10, pp. 11, 38, *verified*): median CAC payback is 5 months under $1M ARR, 8 at $1–5M, 14 at $5–20M, 20 at $20–50M, and 17 over $50M. The report warns that "early-stage companies are not always fully accounting for all expenses to acquire customers, which may artificially lower their CAC payback period."
- **KeyBanc/Sapphire 2025:** "Account executive payback periods expected to shorten to 18 months by 2026" (N-A11, *verified*).
- **Tunguz, 9 Oct 2025** (N-A20, *verified*):
  - self-serve / product-led at "<$5K annually" (CAC $100–500; payback 3–6 months);
  - inside sales at "$5K-$50K" (CAC $5K–15K; payback 6–12 months);
  - field sales at ">$50K" (CAC $25K–100K+; payback 12–24 months).

**Is there an ACV "valley of death"? The evidence points both ways.**

*For a dead zone:*
- Tunguz (21 Jul 2016, N-A19, *verified*): "many startups prefer to field sales teams on accounts that are $3k+ because the velocities are sustainable and the quotas are attainable". At a $500 ACV, one rep would need to close about 1,000 customers a year.
- High Alpha's weakest retention bands are ACVs under $10k (above).
- Airtree's "valley of death" of $5k–100k ACV could not be opened (HTTP 403), so it is *assumed* and not used.

*Against a dead zone:*
- Tunguz (21 Apr 2017, N-A18, *verified*) found public software companies at IPO at every ACV "from $87 to $780,000" and concluded "there's existence proof of successful software companies at every price point" (market-cap differences p = 0.37).
- He notes the survivorship bias himself: a real answer would need "the startup bankruptcy rate by ACV".

**What a salesperson costs.** The Bridge Group's 2024 benchmark of more than 170 B2B SaaS companies (N-A21, *verified*, blog summary):
- median annual quota "$800K", and on-target earnings "$190K" with "a 53:47 base : variable split";
- "the difference in quota for a <$25K ACV seller and a $250K+ seller is nearly 2.5X".

**Rep and payback arithmetic [our call]:**
- **Deals a rep must close each year** (quota ÷ ACV):

  | Quota | $1k ACV | $5k | $10k | $25k |
  |---|---|---|---|---|
  | $800K (Bridge median) | 800 | 160 | 80 | 32 |
  | About $320K (our guess: the <$25K-ACV quota, taking the median as near the top end and dividing by 2.5) | 320 | 64 | 32 | 13 |

- **Minimum annual fee per customer for inside sales to pay back within 12 months** = CAC × 12 ÷ (payback months × gross margin). With Tunguz's inside-sales CAC of $5k–15k, a 12-month payback and High Alpha's roughly 80% software gross margin (p. 11), the minimum comes to **about $6k–19k a year per customer**.
- **Customers lost each year at the stretch.** At $5k per customer and 85–88% gross retention, a $10M ARR base of 2,000 customers loses 240–300 customers a year that must be replaced before any growth.

**What must be true for founder-led outreach to SMBs to stay economic past the first customers [our call, built on the sources above]:**
1. **Expected annual fee per customer of about $5k or more**, or a named scalable channel if lower: inbound or search (Janz's rabbits), a marketplace or TMS integration, or an association or partner. High Alpha finds channel partnerships grow as fast as direct sales: 35% growth and 90% GRR for each (p. 42).
2. **CAC payback of 12 months or less, counted honestly.** Founders' time is not free once other work competes for it. High Alpha warns that early-stage firms undercount CAC.
3. **Gross revenue retention of about 88–90% or better**, which in practice means being a control point or system of record (Tidemark, A6). Otherwise churn replacement eats the sales capacity.
4. **One motion, not two.** Levelset's former CRO describes the $1–10M stall as "flying two planes at once" (SMB and enterprise motions run side by side), with growth stalling around $4–5M ARR (N-A37, *verified*, partly paraphrased).
5. **A list-driven, persistent early motion.** "Go put 100 logos in a list… and do something to get their attention once a week, every week." (N-A37). T2D3 expects 30–60 "starter clients" before scaling (N-A12).

**Evidence on the founder claim ("SMBs are more accessible, since we can reach out directly"):**
- *For:*
  - Direct sales is the most common motion, used by about 40% of respondents, with 35% median growth and 90% GRR (High Alpha p. 42, *verified*).
  - Early vertical winners began with list-driven direct outreach (N-A37).
- *Against:*
  - Small contracts churn more and expand less (N-A10, N-A16, N-A13).
  - SMBs need a sub-12-month payback (N-A13).
  - Direct selling below about $5k a year per customer is uneconomic by most practitioners' thresholds (N-A19, N-A20).
  - Janz: channels are "either scalable or profitable but not both" (N-A15).

**Verdict: Partly supported.** Reaching out directly works for the first customers at any price. It stays economic only at roughly $5k or more a year per customer, with a payback of 12 months or less and gross retention of about 88% or better.

**Implication for S0:**
- Add a rule [our call]: if the entry motion is founder-led direct outreach, a candidate must show an expected annual fee of about $5k or more per customer and a credible path to a payback within 12 months.
- Otherwise it must name a scalable channel: inbound, marketplace, integration or partner.

---

### A4. Base rates: first-time versus serial founders

**Gompers, Kovner, Lerner and Scharfstein, "Performance Persistence in Entrepreneurship"** (N-A22). Read in the January 2009 working-paper draft; published in the *Journal of Financial Economics* 96(1), 2010, pp. 18–32. *verified* from the draft; the published figures may differ slightly (*assumed*).
- **Sample:** "a sample of 8,753 entrepreneurs in 9,790 ventures". These are founders in the VentureSource database, 1986–2000, with outcomes tracked to Dec 2007.
- **Definition of success:** "going public or filing to go public by December 2007."
- **Raw rates:** "The overall success rate on first-time ventures is 25.3%". Serial entrepreneurs' later ventures succeeded 29.1% of the time.
- **Predicted rates** (p. 13): "The predicted success rate of entrepreneurs with a track record of success is 30.3%, compared to only 21.8% for serial entrepreneurs who failed in their prior venture, and 20.9% for first-time entrepreneurs."
- **Investor experience matters too:** "First-time entrepreneurs have a 20.9% chance of succeeding when funded by more experienced venture capital firms and a 14.3% chance of succeeding when funded by a less experienced venture capital firm."
- **Interpretation (intro):** the persistent part is "market timing skill", meaning choosing the right industry and year.

**Azoulay, Jones, Kim and Miranda, "Age and High-Growth Entrepreneurship"**, *AER: Insights* 2(1), 2020, pp. 65–82; NBER w24489 (N-A23, *verified*: abstract, introduction and §V.A). The study covers "the 2.7 million founders in the U.S. between 2007-2014 who started companies that go on to hire at least one employee" (NBER introduction). Section V.A links "all 2.5 million founders" to their earlier jobs using Census employment records (LEHD), which do not cover Massachusetts.
- "Prior experience in the specific industry predicts much greater rates of entrepreneurial success."
- "For achieving a 1 in 1,000 highest-growth firm, having no experience in the 2-digit level industry leads to a success rate of 0.11%, while having at least three years of experience in the start-up's industry shows success rates that rise from 0.22% (2-digit NAICS experience) to 0.24% (4-digit NAICS experience) to 0.26% (6-digit NAICS..."
- "a 50-year-old founder is 1.8 times more likely to achieve upper-tail growth than a 30-year-old founder."

**General survival.** US Bureau of Labor Statistics, Business Employment Dynamics, Table 7 (N-A24, *verified*). The table covers all private establishments, not growth startups.
- The March 2014 cohort: 79.7% alive after 1 year, 69.3% after 2, 50.8% after 5.
- The March 2015 cohort: 55.4% alive after 5 years.

**SaaS-specific base rate.** One in ten monetizing software startups reaches $10M ARR within ten years (N-A01).

**First-time SaaS founders specifically:** no public dataset was found. **The evidence here is thin.**

**Balance:**
- *For "first-timers face worse odds":* Gompers et al. and Azoulay et al. above.
- *Against, or nuance:*
  - Previously failed founders do no better than first-timers (21.8% versus 20.9%), so experience alone is not the edge. Picking the right industry and time is, and that is what S0–S7 is meant to do [our call].
  - The sample is venture-backed companies from 1986–2000, judged by IPO. It is not bootstrapped SMB SaaS.

**Verdict: Supported (first-timers face lower odds). The size is moderate.** The gap is about 9 points on IPO odds. The industry-experience effect is larger: roughly double the rate of reaching the top 0.1% of growth firms.

**Implication for S0:**
- Treat team knowledge (W2) and the "lived the problem" note in S0 step 2 as serious criteria.
- Prefer candidate sub-markets where a founder has three or more years of work in that freight sub-industry. If none, plan to recruit a co-founder or advisor who has.
- Plan on the floor outcome, not the stretch.

---

### A5. Converting a savings pool into a fee pool: what share of savings gets charged

| Arrangement (who carries work, risk, capital) | Fee as share of savings or recoveries | Source (location) | Label |
|---|---|---|---|
| Software vendor raising its price for AI savings (vendor carries no collection risk) | 10% ("could easily capture 10% of this upside") | a16z (R23, footnote 1) | *verified* in R23; the share is asserted, not measured |
| Medicare Recovery Audit Contractors (government post-payment recovery audits, huge volume, lowest bid wins) | "the contingency percentages for each of the four permanent RACs, which range from 9.0% to 12.5%"; contracts went to the firm that "bid the lowest contingency percentage" | CRS report R40592, 21 May 2009 (N-A28, payment section) | *verified* |
| Chargeback recovery; flight-delay compensation (vendor does all the work) | "25% per recovered chargeback"; AirHelp "35% success fee" | Poyar / Tremont survey (R25, p. 21 and newsletter) | *verified* in R25 |
| Parcel audit and refund services (vendor does claims work, paid only on success) | "Typical contingency rates range from 25% to 50% of recovered credits"; RefundPros: "25% commission" | D'Arrigo Consulting, 29 Apr 2026 (N-A25); RefundPros page, undated (N-A27) | *verified*. Both are service sellers talking their book |
| Freight (LTL / truckload) audit on contingency | "the net savings to the shipper after the provider's fee is typically 50–75% of the total recovery", which implies a fee of 25–50% [our inference] | D'Arrigo Consulting, 29 Apr 2026 (N-A26) | *verified*. Consultant source |
| Managed-transportation gainshare (3PL runs transportation, shares savings above a baseline) | "Most gain sharing relationships are based on a 50/50 sharing of cost savings". Also: agreeing a baseline "is the main reason gain sharing arrangements are not used" | Logistics Management / Supply Chain 24/7, "Optimizing 3PL partnerships" (N-A30) | *assumed*: search snippet only (page returned 403). R33 confirms gainshares exist but gives no share; ShipperGuide defines gain-share with no share (N-A31) |
| Energy-savings shared-savings contract (energy service company, or ESCO, finances and installs the capital project) | "A typical division of the value of future savings would be 85% for the ESCO and 15% for the Owner", with the ESCO share falling over time "due to its up-front investment" | Hawaii State Energy Office, Feb 2013 (N-A29, p. 1) | *verified*. The guaranteed-savings model has since become the US standard (LBNL, *assumed*, snippet) |

**The pattern [our call]:** the fee share rises with the share of work, collection risk and capital the vendor carries:
- about 10% for a pure price uplift or a very-high-volume audit;
- 25–50% where the vendor does the recovery work and is paid only on success;
- 50% for an operating gainshare;
- about 85% where the vendor funds the capital.

**Size of the recoverable pool, for converting savings into an annual fee:**
- Parcel audits "recover between 2% and 5% of total shipping spend" (N-A25).
- For LTL 3–8% and truckload 1–3% of spend is recovered (N-A26).
- "recoverable errors often range from 2% to 8% of freight spend" for operations without an audit programme (N-A32).
- Mature programmes recover less per dollar (N-A32). So audit-type savings shrink after year 1, which bears on A5 durability (R19 "Enduring").

**Verdict: Supported, with a gap.**
- Fees taken out of savings are well documented near freight: audit contingencies, parcel refunds and gainshares.
- The documented high shares, 25–50%, belong to service-heavy recovery models.
- No source says what share freight customers will pay for software alone. That part is **not settled**.

**Implication for S0:**
- Model software-only fees at 10–25% of realized savings. Use 25–50% only if the product includes a done-for-you recovery or audit service.
- Rename the knobs [our call]. `submarket_selection.md` §10's "Savings capture share (10/20/35%)" is a fee share, but this brief uses "capture share" for market share. Call them "fee share of savings" and "market share".

---

### A6. Vertical versus horizontal SaaS benchmarks

**Retention: only a small, mixed edge.** SaaS Capital 2023, p. 3, Figure 4 (N-A16, *verified*):
- Whether a company sells a vertical or a horizontal product "reveals only minor, and mixed, differences. During the pandemic, we saw that vertically focused companies reported better retention than horizontally focused companies but that relationship has faded."
- Median NRR: horizontal 102%, vertical 101%.
- Median GRR: horizontal 90%, vertical 92%.

**Where vertical retention comes from: control points.** Tidemark's 2025 report page (N-A33, *verified* from page text; full report gated):
- "One of the big advantages of winning a Control Point is superior customer retention. When you're embedded in the core operations of a customer, churn tends to be low".
- "Using median 2024 ARR growth, Multi-Product companies grew about 21% faster than their Single-Product peers."
- The sample is "200+ Vertical SaaS companies across 20 sectors and five continents".
- The public text gives no numbers comparing vertical with horizontal firms.

**Ceilings: not lower, because vertical leaders take much larger shares.**
- Tidemark, "Truths about Vertical SaaS" (N-A34, *verified*): "Leaders in horizontal software markets struggle to get to 20% market share, whereas leaders in many vertical & SMB markets can exceed 40%+ market share." Also, once a vendor passes "roughly 10%" local share "it becomes easier to grow."
- Bessemer, July 2022 (N-A35, *verified*): vertical companies "trade market size for market share and in some cases achieve 50%+ market penetration"; "In vertical markets, one or two vendors often dominate and capture most of the value."
- Euclid (R42): among about 100 public companies, "vertical software companies appear no more TAM-constrained than horizontal peers".

**Growth speed: no verified comparison.** Several widely repeated claims could not be traced to a primary source; see §5.2.

**Dated examples:**

| Company (segment) | Timeline | Source | Label |
|---|---|---|---|
| Mindbody (fitness and wellness studios; SMB; about $900 a year per client) | SaaS launched 2003; $4.4M recurring revenue in 2008, $6.8M in 2009, planned $11.4M in 2010; "over 8,500 clients". About 7 years from SaaS launch to about $10M | Bessemer memo, 2 Jul 2010 (N-A36) | *verified* |
| Levelset, formerly zlien (construction payment and lien compliance; ran SMB and enterprise sales motions side by side) | "$0 to $1M took 18 months. $1M to $10M took 6 years. $10M to 20M took 18 months." About 7.5 years to $10M | Euclid, *VERTICALS #10*, 23 Dec 2025 (N-A37) | *verified* |
| CargoWise / WiseTech (freight forwarders and customs brokers; **freight**) | Bootstrapped. "In '92, I started writing a system"; "Growing about 3% a month from 2008 to 2011"; at interview time "800 million AUD revenue and still growing 30%", "50% EBITDA margin", "18,000 customers". Pricing is usage-based: "Only charge you when you use the software" | Tidemark, *Bootstrapped Legends: CargoWise* interview, undated (N-A39) | *verified*. No $10M date is given; the interview date is *assumed* to be about 2023, from the A$800M revenue |
| Alvys (trucking and freight TMS; **freight**; founded 2020) | "tripled its revenue in each of the past two years and is on track to double it again in 2025"; "1,000-plus customers"; $77M raised in total. No ARR disclosed | Crunchbase News, 29 Sep 2025 (N-A38) | *verified* |

**Verdict: Partly supported / not settled.**
- *Retain better:* only marginally, about 2 points of gross retention in SaaS Capital's data. The strong retention belongs to control-point products.
- *Grow slower:* not settled. No verified comparison exists. The documented vertical SMB examples each spent about 6–7 years in the $1–10M band.
- *Lower ceilings:* not supported. Vertical leaders win higher shares and are not more constrained by market size.

**Implication for S0:**
- The founders' 15 points for "growth / transfer to other markets" matches the evidence that expansion (more products, adjacent segments) drives vertical growth (N-A33, R24).
- Plan for a high share of a smaller segment. That supports a 20–35% market share in the stretch test, but only 10% in the floor test (§3.6).
- Budget for a slow $1–10M phase.

---

## 3. The $10M arithmetic [our call]

**Assumptions:**
1. Revenue is a recurring annual fee: ARR = customers × ARPA (average annual revenue per customer). Year-5 point estimate. The customer counts are the standing base; replacing churned customers is extra (see A3).
2. **Market share (the brief's "capture share")** = the share of all businesses in the segment that become paying customers. Values used: 10%, 20% and 35%.
3. **Fee share** = fee ÷ realized savings for the customer. Values used, from A5:
   - 10%: software only, the low end (R23; the Medicare RAC range of 9–12.5%);
   - 25%: the mid case (parcel-audit low end; chargeback recovery);
   - 50%: service-heavy (the audit contingency high end; a 50/50 gainshare).
4. **Fee pool** = all businesses in the segment × ARPA = ARR ÷ market share. It is market revenue at 100% share.
5. **Savings pool** = fee pool ÷ fee share. It is the realized savings the whole segment must generate. It is a cap on what customers can pay, never a market size (R42; `submarket_selection.md` T12).
6. Valuation multiples and margins are as set out in A1.3 and A1.4. Planning values: 4.0× and a 10% margin.

### 3.1 Required ARR by reading

| Reading | Founder's words | Conversion | ARR range | Planning ARR |
|---|---|---|---|---|
| (a) STRETCH | "$10M Revenue" | ARR ≈ revenue | $10M | **$10M** |
| (b) VALUATION | "a $10M valuation" | $10M ÷ multiple (2.5× / 4.0× / 5.5×) | $4.0M / $2.5M / $1.8M | **$2.5M** |
| (c) FLOOR | "$250K-$1M Profit" (per year) | profit ÷ margin (5% / 10% / 20% / 30%) | $250K: $5.0M / $2.5M / $1.25M / $0.83M. $1M: $20M / $10M / $5M / $3.3M | **$2.5M** ($250K at 10%) |

### 3.2 Customers needed

| Reading (ARR) | ARPA $1k | $5k | $10k | $25k | $50k |
|---|---|---|---|---|---|
| (a) $10M | 10,000 | 2,000 | 1,000 | 400 | 200 |
| (b) and (c) planning, $2.5M | 2,500 | 500 | 250 | 100 | 50 |
| (b) range, $1.8M–$4.0M | 1,818–4,000 | 364–800 | 182–400 | 73–160 | 36–80 |
| (c) range, $0.83M–$5.0M ($250K profit) | 833–5,000 | 167–1,000 | 83–500 | 33–200 | 17–100 |

### 3.3 Businesses needed in the segment (customers ÷ market share)

| Reading (ARR) | Market share | ARPA $1k | $5k | $10k | $25k | $50k |
|---|---|---|---|---|---|---|
| (a) $10M | 10% | 100,000 | 20,000 | 10,000 | 4,000 | 2,000 |
| (a) $10M | 20% | 50,000 | 10,000 | 5,000 | 2,000 | 1,000 |
| (a) $10M | 35% | 28,571 | 5,714 | 2,857 | 1,143 | 571 |
| (b) and (c), $2.5M | 10% | 25,000 | 5,000 | 2,500 | 1,000 | 500 |
| (b) and (c), $2.5M | 20% | 12,500 | 2,500 | 1,250 | 500 | 250 |
| (b) and (c), $2.5M | 35% | 7,143 | 1,429 | 714 | 286 | 143 |

The business counts scale in proportion to ARR. Multiply the $2.5M row by 0.73 for $1.8M ARR, by 1.6 for $4.0M, and by 2.0 for $5.0M.

### 3.4 Annual fee pool and annual savings pool

| Reading (ARR) | Market share | Fee pool (ARR ÷ share) | Savings pool at 10% fee share | at 25% | at 50% |
|---|---|---|---|---|---|
| (a) $10M | 10% | $100M | $1.0B | $400M | $200M |
| (a) $10M | 20% | $50M | $500M | $200M | $100M |
| (a) $10M | 35% | $28.6M | $286M | $114M | $57M |
| (b) and (c), $2.5M | 10% | $25M | $250M | $100M | $50M |
| (b) and (c), $2.5M | 20% | $12.5M | $125M | $50M | $25M |
| (b) and (c), $2.5M | 35% | $7.1M | $71M | $29M | $14M |

**Sensitivity at a 10% share:** the fee pool for (b) runs from $18M ($1.8M ARR) to $40M ($4.0M). For (c) it runs from $8.3M ($0.83M) to $50M ($5.0M).

### 3.5 Savings each customer must realize per year to support each ARPA (ARPA ÷ fee share)

| ARPA | 10% fee share | 25% | 50% |
|---|---|---|---|
| $1k | $10k | $4k | $2k |
| $5k | $50k | $20k | $10k |
| $10k | $100k | $40k | $20k |
| $25k | $250k | $100k | $50k |
| $50k | $500k | $200k | $100k |

**Illustration [our call]:**
- Audit-type savings run at 2–8% of freight spend (N-A25, N-A26, N-A32).
- A $5k fee at a 25% fee share needs $20k a year of realized savings.
- That in turn needs a customer spending roughly **$250k–$1M a year on freight**.
- A $1k fee at 25% needs $4k of savings, or about $50k–200k of freight spend.

This links the size of the "SMB" targeted to the fee the product can charge.

### 3.6 Which reading should set the S0 size floor (K5) [our call]

**1. K5 knock-out = the floor, using (c) and (b) at their shared ~$2.5M ARR planning value.** The entry segment's fee pool, meaning reachable businesses × realistic ARPA, should be **about $25M a year or more**, i.e. $2.5M ARR at a conservative **10% market share**. Equivalent minimum counts of reachable businesses:
- about 25,000 at $1k ARPA;
- about 5,000 at $5k;
- about 2,500 at $10k;
- about 1,000 at $25k;
- about 500 at $50k.

Why:
- It is the outcome the founders say would make them "more than happy". A segment that cannot deliver it even at a modest share is a true knock-out.
- 10% is conservative next to documented shares for vertical leaders: over 40% (N-A34) and 50%+ (N-A35), both survivor examples. It also matches a16z's 10% (R23) and Tidemark's "roughly 10%" tipping point (N-A34).
- $25M matches the unvalidated indie floor already in `submarket_selection.md` §10 ("tens of millions of fee potential"). This check gives that knob its first grounding.
- Base rates (A1) say to plan on the floor, not the stretch.

**2. The stretch is a ceiling test, not a knock-out.** The beachhead plus the adjacent segments reachable with the same core product should hold a fee pool of **about $50M or more** ($10M ARR at a 20% share); $100M at 10% is better. At about $29M the stretch works only with 35% leadership. Score this under A1 (savings pool and fee potential) and A6 (expansion) rather than knocking candidates out.

Why:
- The founders want "medium scale" and said "the Market Share must accomodate", so the stretch must at least be possible.
- Euclid lets a beachhead be a fraction, about 10%, of the eventual market, and says expansion matters more than the starting size (R42, R24).

**3. Cohen check (R19).** Cohen sets his threshold for a viable indie business where the customer count × the budget per customer comes to about 100M, with his other rows at average scores. His footnote 19 reads: "100k businesses at $1000/mo ... consider the threshold of those numbers combined to be 100M". The footnote says per month, but the rubric's budget row is annual, so read it as a budget pool of about $100M a year. A segment that sits right at our $25M floor therefore needs above-average scores on awareness, liquidity, differentiation and lock-in to pass Cohen's multiplicative check.

**4. Pair K5 with the A3 channel rule.** A segment can pass K5 with many businesses at a low annual fee and still fail to be economic through direct outreach. Pair K5 with "ARPA ≥ ~$5k, or a named scalable channel".

---

## 4. Open questions the founders must answer

1. **Profit definition.** Is "$250K–$1M profit" EBITDA after paying yourselves market salaries, or owner earnings (SDE) that include your pay? At a 10% margin the answer moves the ARR needed by several hundred thousand dollars per founder salary.
2. **When does the 5-year clock start?** Today, product launch, or first revenue? ChartMogul's base rates start at first monetization (N-A01); "usually takes between two and five years" to $1M ARR from there.
3. **Funding.** Bootstrapped, lightly funded, or venture-backed? The stretch path (T2D3) is a venture-backed path, and equity-backed SaaS runs at negative margins (N-A06). Bootstrapped SaaS mostly breaks even (N-A04).
4. **Valuation meaning.** Is "$10M valuation" a sale price, a funding-round price, or a paper figure? Who would buy a $1.8–4.0M ARR freight SaaS, and on what basis? Below about $5M of value, buyers price on SDE (N-A09).
5. **Target ARPA and motion.** What annual fee per customer do you expect? If under about $5k, which scalable channel (inbound, marketplace, TMS integration, association, partner) replaces founder outreach?
6. **Fee share and service.** Will you sell software only (plan on 10–25% of savings) or a done-for-you recovery or audit service (25–50%)? Are you willing to run the service part, with its labour and collection risk?
7. **Team fit.** Does either founder have three or more years of work in the specific freight sub-industry being considered (N-A23)? Has either built a company before (N-A22)? If not, who will you add?
8. **Runway.** How many years of runway, and how much founder time, can you commit before reaching about $1M ARR? The median in the 2023 data was about 2 years 9 months from first revenue (N-A02).
9. **"Medium scale" in numbers.** Is the $10M ARR stretch a must-be-possible condition (the ceiling test in §3.6) or only a hope? The answer decides whether the stretch test is scored or becomes a second knock-out.
10. **Knob naming.** Confirm that "capture share" in `submarket_selection.md` §10 means the fee share of savings, and adopt separate names for fee share and market share (A5).

---

## 5. Sources

### 5.1 New web sources (N-A)

| ID | Author / org | Title | Date | URL | Access | What was read |
|---|---|---|---|---|---|---|
| N-A01 | ChartMogul; also Kyle Poyar, Growth Unhinged (same data) | Against the Odds: The 2025 SaaS Growth Report; "The odds of making it" | 15 Oct 2025 | https://chartmogul.com/reports/saas-growth-the-odds-of-making-it/ ; https://www.growthunhinged.com/p/the-odds-of-making-it | full (web) | milestone shares, time to $1M, method caveats |
| N-A02 | ChartMogul | SaaS Growth Report 2023 (web and PDF) | 30 Aug 2023 | https://chartmogul.com/reports/saas-growth-report/ ; PDF https://chartmogul.com/reports/saas-growth-report/saas-growth-report-2023.pdf | full (PDF text) | pp. 2, 16, 17 (milestones, survivorship note) |
| N-A03 | SaaS Capital | 2026 Private B2B SaaS Company Growth Rate Benchmarks | 2026 (15th survey) | https://www.saas-capital.com/research/private-saas-company-growth-rate-benchmarks/ | partial (page text; band detail only in charts) | median growth: all, bootstrapped, equity-backed |
| N-A04 | SaaS Capital | 2026 Spending Benchmarks for Private B2B SaaS Companies | 10 Jun 2026 | https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/ | full | spend as % of ARR; share at breakeven or profitable |
| N-A05 | SaaS Capital | 2026 Benchmarking Metrics for Bootstrapped SaaS Companies | 24 Apr 2026 | https://www.saas-capital.com/blog-posts/benchmarking-metrics-for-bootstrapped-saas-companies/ | full | $3–20M bootstrapped growth, NRR, GRR |
| N-A06 | SaaS Capital | Growth, Profitability, and the "Rule of 40" for Private SaaS Companies | 21 Aug 2025 | https://www.saas-capital.com/blog-posts/growth-profitability-and-the-rule-of-40-for-private-saas-companies/ | full (text; charts 1–3 viewed as images) | growth and margin by ARR band and funding, 2023 and 2025 |
| N-A07 | SaaS Capital | 2025 Private SaaS Company Valuations | 24 Jan 2025 | https://www.saas-capital.com/blog-posts/private-saas-company-valuations-multiples/ | full | 4.8× and 5.3× predicted private multiples; SCI 7.0× at the time; method |
| N-A08 | SaaS Capital | The SaaS Capital Index (chart dated 8/31/2026); "Four early 2026 SaaS trends" | chart 31 Aug 2026; post 9 Apr 2026 | https://www.saas-capital.com/the-saas-capital-index/ ; https://www.saas-capital.com/blog-posts/four-early-2026-saas-trends/ | full (chart image viewed; FAQ text) | 4.6× median; method; Q1 2026 "decade-plus lows" |
| N-A09 | FE International | SaaS Valuation Multiples 2026: Private Deal Benchmarks | 25 Aug 2026 | https://www.feinternational.com/blog/saas-valuation-multiples | full | private multiples by size; SDE versus EBITDA versus ARR basis |
| N-A10 | High Alpha | 2025 SaaS Benchmarks Report (PDF) | 2025 | https://2994607.fs1.hubspotusercontent-na1.net/hubfs/2994607/2025%20SaaS%20Benchmarks%20Report.pdf (landing: https://www.highalpha.com/saas-benchmarks) | full PDF. The file is publicly hosted and was found via search; the landing-page form was **not** submitted | pp. 8, 11, 38, 41, 42 |
| N-A11 | KeyBanc Capital Markets & Sapphire Ventures | 2025 SaaS Survey (press release and landing page) | 13 Nov 2025 | https://investor.key.com/press-releases/news-details/2025/PRIVATE-SAAS-COMPANY-SURVEY-REVEALS-AI-DRIVEN-TRANSFORMATION-AND-SUSTAINED-OPERATIONAL-EXCELLENCE/default.aspx ; https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey | partial; **full report gated** (form not submitted) | growth, EBITDA trend, GRR, AE payback headline |
| N-A12 | Neeraj Agrawal, Battery Ventures (TechCrunch) | The SaaS Adventure (T2D3) | 1 Feb 2015 | https://techcrunch.com/2015/02/01/the-saas-travel-adventure/ | full | stage definitions and caveat |
| N-A13 | Bessemer Venture Partners | Scaling to $100 Million | 21 Sep 2021 | https://www.bvp.com/atlas/scaling-to-100-million | full | CAC payback targets by segment; GRR; growth by band |
| N-A14 | Christoph Janz (Point Nine) | Five ways to build a $100 million business | 5 Oct 2014 | http://christophjanz.blogspot.com/2014/10/five-ways-to-build-100-million-business.html | full | five ways; channel notes |
| N-A15 | Christoph Janz (Point Nine) | Five years later: Five ways to build a $100 million SaaS business | 7 Apr 2019 | http://christophjanz.blogspot.com/2019/04/five-years-later-five-ways-to-build-100.html | full | changes (whale added, fly removed); channel quote |
| N-A16 | SaaS Capital | 2023 B2B SaaS Retention Benchmarks (Research Brief 28, PDF); "What is a Good Retention Rate ... 2025?" | 2023; 18 Sep 2025 | https://www.saas-capital.com/wp-content/uploads/2023/05/RB28WS1-2023-B2B-SaaS-Retention-Benchmarks.pdf ; https://www.saas-capital.com/blog-posts/what-is-a-good-retention-rate-for-a-private-saas-company/ | full (2023 PDF, figures 1–6 viewed); partial (2025 page, values only in charts) | NRR and GRR by ACV; vertical versus horizontal; bootstrapped versus equity-backed |
| N-A17 | ChartMogul | SaaS Retention Report | 1 Nov 2023 | https://chartmogul.com/reports/saas-retention-report/ | partial | retention by ARPA (headline figures) |
| N-A18 | Tomasz Tunguz | Is There a No Man's Land in SaaS ACVs? | 21 Apr 2017 | https://tomtunguz.com/no-mans-land-saas/ | full | ACV at IPO; survivorship caveat |
| N-A19 | Tomasz Tunguz | The Smallest ACV to Justify an Inside Sales Team at a SaaS Startup | 21 Jul 2016 | https://tomtunguz.com/smallest-acv-to-justify-inside-sales-team/ | full | $3k+ rule; rep velocity arithmetic |
| N-A20 | Tomasz Tunguz | A Founder's Guide to Go-to-Market Strategy | 9 Oct 2025 | https://tomtunguz.com/go-to-market-guide/ | full | ACV thresholds; CAC and payback by motion |
| N-A21 | The Bridge Group | 2024 SaaS AE Metrics & Compensation: Benchmark Report (blog) | 5 Mar 2024 | https://blog.bridgegroupinc.com/2024-ae-metrics-compensation-benchmark | partial (blog summary; full report not opened) | quota, OTE, quota spread by ACV |
| N-A22 | Gompers, Kovner, Lerner, Scharfstein | Performance Persistence in Entrepreneurship (JFE 96(1), 2010, 18–32; draft Jan 2009) | 2009 / 2010 | https://www.newyorkfed.org/medialibrary/media/research/economists/kovner/performance_persistence.pdf (published: https://www.sciencedirect.com/science/article/abs/pii/S0304405X09002311) | full (working-paper PDF text); published version not read | intro; data section; Table 5 discussion (p. 13); VC-experience results |
| N-A23 | Azoulay, Jones, Kim, Miranda | Age and High-Growth Entrepreneurship (AER: Insights 2(1), 2020, 65–82; NBER w24489) | 2020 | https://www.aeaweb.org/articles?id=10.1257%2Faeri.20180582 ; https://www.nber.org/system/files/working_papers/w24489/w24489.pdf | partial (abstract, intro, §V.A) | industry-experience and age effects |
| N-A24 | US Bureau of Labor Statistics, Business Employment Dynamics | Table 7. Survival of private sector establishments by opening year | current table | https://www.bls.gov/bdm/us_age_naics_00_table7.txt | full (table) | 2014, 2015, 2019 and 2020 cohorts |
| N-A25 | Paul D'Arrigo, D'Arrigo Consulting | Parcel Audit Services: How They Work & What They Recover in 2026 | 29 Apr 2026 | https://www.darrigoconsulting.com/blog/parcel-audit-services-guide | full | contingency 25–50%; recovery 2–5% |
| N-A26 | Paul D'Arrigo, D'Arrigo Consulting | Shipping Audit: How to Recover 2–8% of Your Carrier Spend (2026) | 29 Apr 2026 | https://www.darrigoconsulting.com/blog/shipping-audit-freight-audit-guide | full | net to shipper 50–75%; LTL, truckload and parcel recovery rates |
| N-A27 | RefundPros | FedEx Refund Services for Businesses | undated | https://refundpros.com/fedex-refund-services/ | full | 25% commission |
| N-A28 | Congressional Research Service (via EveryCRSReport) | R40592, Medicare's Recovery Audit Contractor (RAC) Program: Background and Issues | 21 May 2009 | https://www.everycrsreport.com/reports/R40592.html | partial (payment section) | 9.0–12.5% contingency; lowest-bid award |
| N-A29 | Hawaii State Energy Office (PDF author field: Elizabeth Raman) | Pros & Cons of Guaranteed Energy Savings vs. Shared Savings Performance Contracts | Feb 2013 | https://energy.hawaii.gov/wp-content/uploads/2012/06/Pros-and-Cons-of-guaranteed-vs.-shared-energy-savings-2013.pdf | full (2 pp.; fetched with curl after WebFetch returned 403) | 85/15 typical split and why |
| N-A30 | Logistics Management / Supply Chain 24/7 | Global Logistics: Optimizing 3PL partnerships | undated | https://www.logisticsmgmt.com/article/global_logistics_optimizing_3pl_partnerships (mirror: https://www.supplychain247.com/article/global_logistics_optimizing_3pl_partnerships) | **not accessible (HTTP 403 on both)**; only search snippets seen | 50/50 gainshare and baseline quotes, *assumed* |
| N-A31 | Hal Koss, ShipperGuide | Managed Transportation Pricing & ROI Made Simple | undated | https://blog.shipperguide.com/managed-transportation-pricing | full | five pricing models; gain-share definition (no share given) |
| N-A32 | William Carlin, Racklify | Inbound Freight Audit Costs & Who Pays | updated 28 Aug 2026 | https://racklify.com/encyclopedia/inbound-freight-audit-costs-savings-and-who-pays-pricing-models-and-roi/ | full | pricing models; 2–8% recoverable; mature-programme decay |
| N-A33 | Tidemark (with Stripe) | 2025 Vertical & SMB SaaS Benchmark Report (page); Stripe landing page; SaaSletter summary | Nov 2025 | https://www.tidemarkcap.com/vskp-chapter/2025-vertical-smb-saas-benchmark-report ; https://stripe.com/lp/vertical-saas-benchmark-2025 ; https://www.saasletter.com/p/vertical-saas-benchmarks-2025 | partial; **full report gated** (form not submitted) | sample, multi-product growth, control-point retention |
| N-A34 | Dave Yuan, Tidemark | Truths about Vertical SaaS | undated | https://www.tidemarkcap.com/vskp-chapter/vertical-saas-truisms | full | market-share ceilings; 10% local tipping point |
| N-A35 | Bessemer Venture Partners | Ten lessons from a decade of vertical software investing | Jul 2022 | https://www.bvp.com/atlas/ten-lessons-from-a-decade-of-vertical-software-investing | full | 50%+ penetration; Rule of 40 |
| N-A36 | Bessemer Venture Partners | Mindbody investment memo | 2 Jul 2010 | https://www.bvp.com/memos/mindbody | full | revenue history, clients, price, churn, CAC, payback |
| N-A37 | Euclid Ventures (with Martin Roth, ex-CRO of Levelset) | VERTICALS #10: Why $1–10M ARR is the Hardest | 23 Dec 2025 | https://insights.euclid.vc/p/vertical-sales-strategy-by-stage-levelset-procore | full | Levelset timeline; the "two planes" stall; "Dream 100" |
| N-A38 | Crunchbase News | Trucker's Son Bucks Logistics Funding Decline With $40M Raise For Startup Alvys | 29 Sep 2025 | https://news.crunchbase.com/transportation/logistics-software-startup-seriesb-alvys/ | full | founding year, growth multiples, customer count, funding |
| N-A39 | Tidemark (interview with Richard White) | Bootstrapped Legends: CargoWise | undated (about 2023, *assumed*) | https://www.tidemarkcap.com/post/bootstrapped-legends-cargowise | full (interview text) | bootstrapped history, growth, pricing model, scale |

### 5.2 Claims found in search but not verified (not used as evidence)

| Claim | Where it appeared | Why not used |
|---|---|---|
| "Vertical SaaS companies hit $10M ARR 40% faster than horizontal peers" (attributed to Bessemer's 2025 State of the Cloud) | kgt.solutions blog, via search summaries | Not found on bvp.com (the 2025 State of the Cloud URL returned 404; a site search found no match). Unverified |
| "Vertical SaaS grows 5 percentage points faster at the median, with 7 points more NRR and 5 points less churn" (attributed to Tidemark) | search-engine summary | Not in Tidemark's public 2025 page text; the full report is gated. Unverified |
| "Vertical 31% versus horizontal 28% growth; vertical 91% versus horizontal 78–85% gross retention" | valueaddvc.com and saasmag.com blogs | Secondary, unsourced. Contradicted by SaaS Capital's measured 92% versus 90% GRR (N-A16) |
| "$5k–$100k ACV valley of death" (Airtree) | medium.com/airtree-venture, via a search snippet | Page returned HTTP 403. *assumed*; Tunguz (N-A18, N-A20) used instead |
| Micro-SaaS profit margins of 64% or 70–90% | several blogs | Not about B2B vertical SaaS with sales and support; not used for reading (c) |
| Carta founder-ownership figures (56% after seed, 36% after Series A) | search summaries of Carta's report | Not needed once the "founders' proceeds" reading was dropped; not verified |
| GSA transportation post-payment audit contingency rates | gsa.gov pages | Pages returned 403; no rate found. Not used |
