# R29 - Investing in Silo
- URL: https://a16z.com/announcement/investing-in-silo/ | Author: Anish Acharya, Andreessen Horowitz (a16z), filed under "Fintech" | Year: 2020 (posted 24 Sep 2020; page metadata shows a last modification on 2 May 2023) | Type: primary (VC investment announcement; five short paragraphs) | Access: free, read in full from the live page (raw HTML downloaded 2026-09-13 to scratchpad `r29_a16z.html`, text in `r29_a16z.txt`) | Accessed: 2026-09-13
- Decision the resource addresses: vertical selection (why fresh-food / wholesale food distribution) and beachhead or niche choice (why the distributor node of the produce chain, and why an operating-system-plus-fintech product for it). It is an investor's rationale, not a method; nothing in it is presented as a general framework.

## Strategies or frameworks described
The source names no strategy or framework. What follows is the article's implicit selection rationale, broken into the steps it actually argues, with the author's wording kept. Strategy titles below are the reader's labels (marked as such), except where a phrase is the author's.

### Reader label: "Why this industry" - three signals plus technological neglect (paragraph 1)
- Origin and intended context: B2B vertical software for US fresh-food wholesale distribution, seed/early-stage startup, 2020 (post-COVID framing).
- Mechanism and steps (verbatim): "Yet the agriculture industry (the stuff we actually eat!) has largely remained unchanged by technology, despite being the largest category of consumer spend, the presence of massive waste (40 percent of perishable food is wasted in the supply chain), and a renewed focus on having a resilient food supply chain in a post-COVID era."
- Criteria, inputs and data required: size of end spend; a large measurable loss (waste); a topical resilience motive; low prior digitisation. No sources are cited for the 40 percent figure or the "largest category of consumer spend" claim (source's claim, unverified here).
- Output produced: an industry-level "worth entering" judgement.
- Assumptions, limitations, critiques: reader inference: waste is treated as the pool of value software can recover; the author does not quantify what share of that waste is addressable by a distributor's operating system.
- Key quotes: as above.

### Reader label: "The hub node" - pick the party that connects everyone (paragraph 1; the curator's phrase "pick the hub node of the chain" is a paraphrase, not the author's words)
- Origin and intended context: same.
- Mechanism and steps (verbatim): "Food distributors are at the heart of this supply chain - they are responsible for connecting growers, grocers, restaurants, and even other distributors. And this dense network of relationships requires a high degree of operational and logistical excellence, as fresh food begins losing value the moment it enters the supply chain."
- Criteria, inputs and data required: which actor has the densest set of relationships; where operational/logistical execution matters most; perishability (value decays with time).
- Output produced: the customer node (wholesale food distributors).
- Assumptions, limitations, critiques: the article does NOT say growers or retailers were considered and rejected; the curator's "not growers or retailers" is an inference from the choice made, not a stated comparison (reader note for the adversarial reviewer). Reader inference: the hub logic assumes that a system of record at the hub can pull the other parties onto it ("there is a strong network emerging").
- Key quotes: as above.

### Reader label: "System of record for a pencil-and-paper operation" - product-market-fit rationale (paragraph 2)
- Origin and intended context: same.
- Mechanism and steps (verbatim): "Silo: an operating system and system of record for wholesale food distributors that is reducing waste, improving margins, and catalyzing an historic shift from pencil and paper (really) to software. The product has exceptionally strong market fit because it solves so many of the operational problems that distributors have. Price sheets, inventory, purchase orders, logistics, and even accounting is all handled on the Silo platform; this is for food distributors what Toast is for restaurants."
- Criteria, inputs and data required: current tooling of the customer (pencil and paper); breadth of operational problems solvable by one system; an analogue in another vertical (Toast).
- Output produced: product scope (price sheets, inventory, purchase orders, logistics, accounting).
- Assumptions, limitations, critiques: reader inference: "logistics" is one module among five; the article gives no detail on carriers, freight rates or shipping cost, so it does not describe the carrier side of a freight sub-market.
- Key quotes: as above.

### Author's phrase: "partnering with and supporting existing distributors, instead of competing with or otherwise 'disrupting' them" (paragraph 3)
- Mechanism and steps (verbatim): "Silo is a 'system of record' for wholesale food predicated on partnering with and supporting existing distributors, instead of competing with or otherwise 'disrupting' them. As a result, there is a strong network emerging, which Silo's technology aims to assist in driving further reductions in spoilage and increasing profits for all participants within the supply chain."
- Criteria: whether the incumbent intermediary is to be armed rather than replaced.
- Output: a go-to-market posture (arm the incumbent hub).
- Assumptions, limitations, critiques: none stated. Reader inference: this is the same choice R30 (Bushel) makes for grain, and the opposite of the disintermediation model (marketplaces that bypass distributors/brokers).

### Author's phrase: "fintech adjacent" monetisation via factoring, faster payments and PACA (paragraph 3)
- Mechanism and steps (verbatim): "We believe that financial services will be a key enabler of this ecosystem, where factoring and faster payments, coupled with laws like PACA, can solve many of the cashflow challenges that growers and distributors face. Indeed, Silo is an excellent example of the kind of 'fintech adjacent' businesses that we're excited to invest in."
- Criteria, inputs and data required: presence of a cashflow problem across the chain; a legal structure (PACA, the US Perishable Agricultural Commodities Act - reader gloss, the article only says "laws like PACA") that makes receivables financeable.
- Output produced: a revenue layer on top of the operating system.
- Assumptions, limitations, critiques: reader inference: the money is made on payments/credit, not on a share of freight savings; the article never claims a shipping-cost saving.

### Author's criterion: team with on-the-ground experience (paragraph 4)
- Verbatim: "As with all investments, the team is the central lynchpin. In this case, Ashton and Antonio's passion, knowledge, and deep expertise for the ag space make them an incredibly compelling team to solve this problem." "... Ashton and Antontio also have the on-the-ground experience that is necessary in this interconnected, largely family-driven space: in fact, they started this business hand-delivering pallets of farm-grown food in a cargo van!" Also: "applying technology thinking to a domain that's largely been ignored by builders and technologists."
- Reader inference: this echoes the insider-knowledge point of R36 (Shane 2000) and R30's "cultural gap": the sub-market chosen was one the founders had physically worked in.

### Examples, case studies and data sources used by the author
- Silo (portfolio company; founders Ashton Braun and Antonio Bustamante); analogy to Toast (restaurants); Marc Andreessen's "software is eating the world" (2011) as framing; PACA as an enabling law. Data: "40 percent of perishable food is wasted in the supply chain" and "the largest category of consumer spend" - both uncited in the article. No numbers on distributor margins, freight or shipping cost.

## Reader's judgement on relevance to a two-sided freight sub-market choice
Judgement: The article is short and promotional, but it is a clean worked example of a node-selection rationale inside an agricultural chain: enter an industry with a large measurable loss (waste) and low digitisation, then pick the actor that "connect[s]" everyone else and still runs on paper, arm it rather than disintermediate it, and monetise partly through finance rather than only through software fees. For the project's two-sided definition it covers the shipper side only in passing (growers ship to distributors) and does not describe carriers, brokers or freight rates at all, so it is evidence about WHERE the reachable, paper-based hub sits, not about freight-company issues. On the origin hypothesis it is silent on farmers losing profit to shipping; the losses it names are spoilage and cashflow ("cashflow challenges that growers and distributors face"), which is a different cost pool than shipping and handling. Method contributions that can be clustered with R28 and R30: waste/loss pool as the entry signal; hub-node choice; paper-based operations as a readiness signal; partner-not-disrupt; founders' insider experience. Weight it as an A-authority but thin (five paragraphs, no data, investor-authored, author's bio says he focuses on consumer investing).

## Read status: full
