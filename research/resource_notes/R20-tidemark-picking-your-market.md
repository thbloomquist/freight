# R20 - Picking Your Market (Vertical SaaS Knowledge Project chapter)
- URL: https://www.tidemarkcap.com/vskp-chapter/picking-your-market | Author: Bob Solomon ("Founder, Software Platform Consulting, & FMR President of ServiceChannel") and Dave Yuan ("Founder and Partner, Tidemark") | Year: undated on the page; the analysis uses "The government's business census (released in 2020, from 2017)", so c. 2021-23. The VSKP index now also lists "Picking Your Market (2025)" | Type: primary (VC/operator essay) | Access: I downloaded the page with curl and read the free text in full: intro, three attributes, how to read the chart, "Vertical SMB SaaS Heaven", "Implications". The text then ends with a gate notice: "To continue reading, login or request access below." Tidemark says it has "moved everything into our Founder & Operator portal", so any text after the notice was not seen. I downloaded both charts (AVIF), converted them to PNG and viewed them. | Accessed: 2026-09-14
- Secondary sources consulted (not in study_links.md): (1) Tidemark, "Where Are The Opportunities in Vertical SaaS? Picking Your Market in 2025", https://www.tidemarkcap.com/vskp-chapter/where-are-the-opportunities-in-vertical-saas-picking-your-market-in-2025. (2) Tidemark, "What Census Data Tells Us About Growth, Fragmentation, and the Next Great SaaS Markets (Maybe)", https://www.tidemarkcap.com/vskp-chapter/what-census-data-tells-us-about-growth-fragmentation-and-the-next-great-saas-markets-maybe. Both are gated after a teaser ("request access to the rest of this piece"), so only their index blurbs were read. The freight numbers placed on the screen below come from R44 (a study_links resource) and are my own computation.
- Decision the resource addresses: vertical selection (which SMB industry to build a vertical SaaS for) and market sizing (what "big" means for a vertical SaaS vendor). It also gives a reproducible desk screen for fragmentation (stages S3/S4). It does not cover problem discovery or fee design.

## Strategies or frameworks described

### 1. The three attributes of "the ideal SMB vertical" (author's list: Gigantic; Highly fragmented market; Highly fragmented value chain)
- Origin and intended context: Tidemark's Vertical SaaS Knowledge Project (VSKP), written for founders who "want to build a vertical SaaS company". The scope is US SMB verticals, and the vendor is called a "Vertical SaaS Vendor (VSV)". Examples are restaurants (Toast, Olo, DoorDash, UberEats), healthcare practitioners, building trades and auto dealers. *(verified)*
- Mechanism and steps (verbatim, author's order):
  1. "Gigantic: Big markets have the universal quality of being full of money. For a Vertical SaaS Vendor (VSV), you should define your market not just by total size, but by number of locations, initial ARPU, and expansion ARPU. Ideally you can do this by either expanding and extending." ("expanding" links to the VSKP multi-product chapter; "extending" links to "Patterns of Extension".)
  2. "Highly fragmented market: It is challenging to build a business in a market where SMBs are fighting over the leftovers of large enterprises. A VSV should target a market with lots of small and midsize merchants."
  3. "Highly fragmented value chain: You want to be selling to fragmented buyers and buying from fragmented sellers. Having this up and down the value chain is important for two reasons: One, it makes a marketplace possible, and two, it often means a better profit pool from payments. Many small payments are generally much more profitable than fewer large payments."
- Criteria, inputs and data required:
  - Number of locations.
  - Initial ARPU and expansion ARPU. The source names these three quantities and gives no operator. *Reader inference:* the natural reading is size ≈ locations × (initial ARPU + expansion ARPU). The "locations × initial ARPU × expansion ARPU" wording in study_links.md is a paraphrase, not the source's formula.
  - Share of the market held by SMBs versus large enterprises.
  - Fragmentation of the customer's own buyers and sellers.
- Output produced: a target profile for an SMB vertical. The source says of the value-chain attribute: "We will save fragmentation up and down the value chain for another day." It is therefore not operationalised on this page.
- Rationale and evidence base:
  - The rationale is given inline. Money lives in big markets. SMBs in enterprise-dominated markets fight "over the leftovers". Value-chain fragmentation makes a marketplace and a payments profit pool possible.
  - The evidence is the authors' authority (a VC plus the former president of ServiceChannel) and named success cases. No outcome data link the attributes to company success.
- Assumptions, limitations, critiques:
  - Stated: "they are all views looking towards the past. Startups are building for the future, so make sure you know how you expect your market to grow (and why)."
  - *Reader inference:* the ARPU framing assumes a subscription-plus-payments model. It does not consider a fee taken from savings.
- Key quotes: see the three definitions above, and "After all, we know that there are no small airlines!" (section "Implications").

### 2. The Census fragmentation screen (bubble chart of 4-digit NAICS industries)
- Origin and intended context: same chapter. "To kickstart this analysis for you, we set out to study which industries are both big and dominated by SMBs." The data are the 2017 Economic Census. *(verified)*
- Mechanism and steps (verbatim):
  1. "I mapped industries at the 4-digit NAICS level. (There is a perpetual argument around which level of classification is best, but we used the 4-digit for today's exercise.)"
  2. "Each circle represents one 4-digit NAICS code." / "A circle's size is proportional to the sales of the industry." / "The x-axis represents the number of companies in each 4-digit NAICS industry." / "On the y-axis you see the market share of all but the top 50 companies."
  3. Reading the chart: "So for industries up near 90% on the y-axis, the top 50 companies represent only 10% of the market (highly fragmented). Conversely, in industries near 10% on the y-axis, the top 50 companies represent nearly 90% of the revenue."
  4. Zones: "In the upper right of the diagram, you see fragmented verticals with many SMBs. This is Vertical SMB SaaS Heaven." / "In the upper left are the fragmented industries that have fewer companies—these verticals are SMB or mid-market opportunities. The lower left of the chart is the land of the giants. In these verticals, you are an enterprise solution, or your company will fail."
  5. Zoom-in filter: "only including those industries where the top 50 companies have less than 20% market share". The second chart also widens the x-axis to include restaurants and colour-codes related verticals: restaurants and bars (blue), healthcare practitioners outside hospital networks (red), building-lifecycle trades (green) and auto dealers (purple).
- Criteria, inputs and data required: firm count and top-50 revenue share by NAICS code, from the Economic Census concentration table (R44), plus industry sales.
- What the two charts show (viewed):
  - Chart 1, "Concentration of Industries (At NAICS 4 Digit Level)", has an x-axis to 200,000 companies. Its handwritten zones read:
    - "Mid-market Heaven e.g. Hospitals, Auto Dealers (SMB), B2B Electronics";
    - "Enterprise Heaven / SMB Hell e.g. Auto mfg, Oil pipelines, Airlines";
    - "SMB Heaven", with "Restaurants →" off the chart.
  - Chart 2, "SMB-Dominated Industries (By 4-Digit NAICS Code)", has a y-axis from 76% to 96%. It labels Dentists (about 92%, about 125k firms), Mechanical Trades Contractors (about 88%, about 180k), Restaurants (about 85%, about 425k), Auto Dealers (about 83%, about 45k, large bubble) and Physician Offices (about 82%, about 170k).
  - Neither chart labels any transportation, warehousing or agriculture code. *(verified by viewing)*
- Output produced: a map of industries by SMB count and fragmentation, used "to help know which market to pick". A second use is suggested: compare the size of the vertical SaaS businesses already built in each vertical against the opportunity. "This analysis would help you determine where there is potential growth left in an existing market, or how big the opportunity is for a new player in a new vertical."
- Rationale and evidence base: the screen operationalises attributes 1 and 2. It rests on public census data and is fully reproducible. There is no validation that position on the chart predicts outcomes.
- Assumptions, limitations, critiques:
  - Stated: the choice of classification level is arbitrary ("perpetual argument"), and the screen is backward-looking.
  - *Reader inference:* the Economic Census covers employer firms only (see R44), so one-truck owner-operators with no payroll are invisible. A 4-digit code can hide opposite structures underneath it.
- Freight codes placed on the screen (*reader computation* from R44, same 2017 census; y = 100 − top-50 share):

  | Code | 2017 firms | y (share outside top 50) | Where it lands |
  |---|---|---|---|
  | 4842 Specialized freight trucking | 46,282 | 80.4% | Just passes the "<20% top-50" SMB-heaven filter (2022: 52,012 firms, 81.4%) |
  | 4841 General freight trucking | 66,075 | 60.4% | Mid-chart |
  | 4885 Freight transportation arrangement (brokers and forwarders) | 15,097 | 67.2% | Upper-left / mid-market band |
  | 4931 Warehousing and storage | 8,068 | 55.5% | Mid-chart |
  | 4921 Couriers and express delivery | 4,215 | 5.1% | "land of the giants" |

  At 6-digit level the split is sharp:
  - 484122 LTL trucking: 14.7% (concentrated).
  - 48411 local general freight: 89.8% (fragmented).
  - 48422 local specialized freight: 90.0% (fragmented).
- Key quotes: see the steps above, and "For instance, both florists and personal care services (barbers, nail salons, etc) are fragmented industries—but the latter are 10x the size of the former." (section "Implications").

### 3. Other VSKP guidance visible on the page (index blurbs only; the chapters themselves were not read)
- "Know Your Tam": "understanding your 'Operational TAM' - not just 'handwavy' market size - can be the difference between sustained growth and hitting an unexpected wall."
- "Control Point Patterns (2024)": "The control point is the last tool to be thrown out before an owner ceases operations, and more importantly, you have the unfair right to offer most products a merchant needs. The result will be that one or two Vertical SaaS players may dominate in any market."
- "Picking Your Market in 2025": "With 2022 census data now available, Bob Solomon ... shares an updated look at which verticals are ripe for a SaaS solution."
- The census growth piece: Solomon analyses "how all 820 six-digit NAICS industries changed between the 2017 and 2022 Economic Censuses".
- The case-study list includes "CargoWise: Bootstrapped Legends", a freight-forwarding software case (title only).
- Rationale and evidence base: not assessable (content gated).

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- This is the most reproducible desk screen in the batch. With R44 it can be run today for every freight-company NAICS code, at 4- or 6-digit level and for 2017 and 2022.
- It gives a clear finding: the freight-company side splits into fragmented pockets and "giants". The fragmented pockets are local and specialized trucking, and to a lesser degree truckload and brokerage. The giants are couriers and LTL.
- Its third attribute, fragmented buyers and fragmented sellers, is the only criterion in the vertical-SaaS literature that matches the project's two-sided definition directly. Its "payments profit pool" rationale also fits freight, where payments and factoring already sit between brokers and carriers (R27, R29).
- It has three limits for this project:
  - It scores industries as SaaS customers. The shipper side must be scored separately with shipper-industry codes (R32).
  - It sizes by ARPU, not by customer savings, so it cannot test the fee-from-savings rule.
  - It is silent on customer-acquisition cost, which is where fragmentation hurts (see R21 and R30).

## Read status: full for the publicly visible text and both charts; partial overall, because the page ends with a login/request-access notice and the 2025 update is gated
