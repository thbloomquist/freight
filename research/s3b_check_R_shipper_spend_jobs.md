# S3b check R: shipper spend, audit and planning jobs (run 01)

> **What this is:** desk evidence for the S3b fact sheets (`submarket_selection.md` §4 S3b):
> - items 5, 6, 7 and 9;
> - evidence for eight scoring rows: A2, A3, A6, W1, W3, W4, W5 and W6.
>
> It covers six shipper-side cards: C-01, C-09, C-10, C-11, C-14 and C-17. Written 2026-09-15.
> **Status:** input to S3b; decides nothing. Every score here is a suggestion, labelled **[our call]**. The coordinator scores the cards and picks the shortlist.
> **Not repeated here:** items 1-4, 8, 10 and 11 (buyer counts, savings pools, structure, durability, fee unit, segments). The coordinator already holds them from S1-S3a.
> **Labels:**
> - *verified*: read at the source.
> - *assumed*: a snippet, secondary summary, vendor claim, memory or blocked page. Vendor figures are always *assumed*, even when read at the source.
> - **[our calc]**: our arithmetic. **[our call]**: our judgement.
>
> **IDs:** new sources are N-R01 to N-R26 (§4). Earlier sources keep their IDs; those re-read here are marked "re-read".
> **Row rules:** `2_knockouts.md` §5 (1 / 0.5 / 0), used exactly. The per-side rows (A3, W1, W5) are judged for both sides, and the better side is named (rule C5).

## How to read this

**Freight words used here** (each defined once):
- **TMS** (transportation management system): software to plan, buy, book and track shipments. **ERP:** the company's main business system (orders, purchasing, accounts payable).
- **EDI** (electronic data interchange): the older machine-to-machine message standard. In trucking:
  - the **EDI 204** is a load tender;
  - the **214** is a shipment status message;
  - the **210** is the carrier's invoice ("Motor Carrier Freight Details and Invoice", N-R24).
- **API:** a modern way for two systems to swap data directly.
- **BOL** (bill of lading): the shipping paper that travels with the freight. **POD** (proof of delivery): the signed delivery receipt, where damage or shortage is written down.
- **FAP** (freight audit and payment): a provider that checks carrier bills against the agreed rate and pays the carriers on the shipper's behalf.
- **Contingency fee:** the service keeps a share of what it recovers, and gets nothing if it recovers nothing.
- **Gainshare:** a 3PL (third-party logistics provider) and a shipper split the savings, measured against a baseline they agree.
- **LTL** (less-than-truckload): several shippers' pallets share one trailer.
- **NMFC** (National Motor Freight Classification): the "freight class" system that sets LTL prices, run by the industry body NMFTA. **Density:** pounds per cubic foot.
- **Reweigh / reclass:** the LTL carrier re-measures a shipment, finds a different weight or class, and re-bills it. The carrier's proof is a **W&R** (weight and research) certificate.
- **Accessorials:** extra-service charges, such as liftgate, residential delivery or waiting time.
- **GRI** (general rate increase): a carrier's yearly across-the-board price rise.
- **Routing guide:** a buyer's written rules telling its suppliers which carrier to use and how to book it.
  - **Collect:** the buyer arranges and pays the carrier.
  - **Prepaid:** the supplier arranges and pays, and usually passes the cost on in its price.
- **Carmack:** the federal law (49 U.S.C. § 14706) that makes carriers liable for cargo loss and damage.
- **Non-domiciled CDL:** a commercial driver's licence issued to a driver who lives in another country.

**Worked example: how a row score is suggested (C-11, A3 pain and urgency).**
- **The row rule:** 1 = a forcing event; 0.5 = a known cost without one; 0 = little evidence.
- **The evidence:**
  - NMFTA changed the LTL class system on 2025-07-19 (N-G20) and again on 2026-05-23 (N-R03).
  - NMFTA itself says the changes "can sometimes lead to differences between the original bill of lading estimate and the final invoice" (N-R02, *verified*).
- **The score:**
  - That is an industry rule change with a date, and it forces every LTL shipper to re-check its classes. So the shipper side gets **1 [our call]**.
  - LTL carriers wrote the change and suffer less from it, so their side gets 0.5.
  - The better side is the shipper side.

---

## 1. Summary table

Suggested scores are in the order A2 / A3 / A6 / W1 / W3 / W4 / W5 / W6. For the per-side rows, the better side is shown in brackets. All scores are **[our call]**.

| Card | Penetration (one line) | Trigger(s) | Budget holder | Implementation | Vendors (count; leader; dominance) | Service firms | Suggested scores | Sources |
|---|---|---|---|---|---|---|---|---|
| **C-01** Buying truckload capacity | Low. About 10% use a TMS below $25M of freight spend (Gartner via a vendor blog, study undated, *assumed*). Buying runs on phone, email and broker portals | 2026 capacity squeeze: freight spend +28.1% year on year in Q2 2026 (N-D31). Non-domiciled CDL final rule effective 2026-03-16 (N-R13). English-proficiency out-of-service orders (N-R15) | Logistics or transportation manager's freight budget | Integration needed: lanes and rates come from the ERP, spreadsheets and broker invoices; tenders go by email, EDI 204 or API; a rate benchmark must be bought | 12 procurement tools named, all 7 main ones tagged "Enterprise" by a vendor's list; 17 TMS vendors in Gartner's 2025 quadrant. No shares. No dominance | 25,081 brokers (spread about 15% of gross); managed-transportation 3PLs (per shipment, % of spend, gainshare) | 0.5 / 1 (shipper) / 1 / 0.5 / 0.5 / 1 / 0.5 / 0 | N-D31, N-R13, N-R15, N-F46, N-E20, N-F28, R27, R33 |
| **C-09** Auditing and paying truckload and LTL bills | The two leaders handle about 9% of trucking dollars. Cass serves "large ... enterprises" (N-D30, *verified*). 51% of enterprise shippers outsource FAP (Gartner via a vendor, *assumed*). Mid-sized shippers: AP clerks or nobody (inference) | AI invoice reading ("shifting from manual review ... to AI-enabled automation", Gartner via a vendor). Payment fraud: 76% of US organisations hit, 74% by business email compromise (N-R01). LTL class changes (N-R02, N-R03). Rising spend (N-D31) | Finance / accounts payable (the controller). Contingency fees come out of recoveries, so no budget line is needed | Data at hand for a look-back audit: invoices (PDF or EDI 210), BOLs, PODs and rate sheets. Paying carriers needs ERP and bank links | About 15 providers in Gartner's guide (list not seen); 16 named here. Leaders: Cass about 4%, U.S. Bank about 5% of trucking revenue. No dominance. Loop raised $95M (Apr 2026) | "Numerous small ... audit firms" (Cass), paid 25-50% contingency | 1 / 1 (shipper) / 1 / 0.5 / 1 / 1 / 0.5 / 1 (0.5 if payment is in the product from launch) | N-D30, N-D31, N-R01, N-R02, N-R05, N-R06, N-R14, N-A26 |
| **C-10** Cargo loss and damage claims | About half of eligible claims are never filed. 28% of mid-market shippers use claims software, and under 8% use AI (vendor report, *assumed*) | Cargo-theft record: losses about $725M in 2025 (+60%), confirmed thefts +18%, average theft $273,990 (N-R04) | Logistics or finance. Contingency fees come out of recoveries | Integration needed: POD exceptions, photos, invoices and BOLs sit with the shipper, but filing goes through each carrier's portal or email. Carriers must pay or decline within 120 days | 12 named (software, TMS and FAP modules, managed services). No shares. No dominance | Claims services (Recoupex, TLI, Sheer, GEODIS, Cass, nVision) on contingency: "typical ... 25–30%" (vendor claim) | 1 / 1 (shipper) / 1 / 0.5 / 0.5 / 1 / 0.5 (shipper) / 0.5 | N-R04, N-K21, N-R07, N-R08, N-R09, N-F35, N-F36 |
| **C-11** LTL class, reweigh and reclass disputes | No survey found. Small shippers book on carrier portals, broker quote sites and cheap LTL tools (Freightview from $149 a month, *assumed*) | NMFC density changes effective 2025-07-19 and 2026-05-23 (N-G20, N-R03). NMFTA's billing-change API (Aug 2025, N-R02). GRIs of 4.9-5.9% (N-R16) | Shipping or logistics lead (outbound freight budget). Disputes are handled by logistics or AP | Integration needed: BOLs and item dimensions (the product master), NMFC class data (a ClassIT+ licence), invoices and W&R certificates. Industry APIs exist (eBOL, pickup, visibility, freight charges); adoption not found | About 7 named LTL tools, plus NMFTA's ClassIT+. No shares. No dominance; NMFTA controls the class data | LTL-focused 3PLs, e.g. WWEX Group (121,000+ customers, 200 franchises; company claim). Audit firms recover 3-8% of LTL spend | 1 / 1 (shipper) / 1 / 0.5 (shipper; carrier side ruled out on K10) / 0.5 / 1 / 1 (shipper) / 0.5 | N-R02, N-R03, N-R12, N-R16, N-R22, N-R26, N-G20, N-G21, N-A26 |
| **C-14** Planning and consolidating shipments | The same TMS gap as C-01. 35% of one trade survey's respondents use a TMS (*assumed*); 17% are fully automated (vendor survey) | No direct forcing event. The 2026 rate rise (N-D31) and LTL GRIs raise the value of pooling. Walmart's prepaid consolidation program for its suppliers (N-E28) | Logistics or transportation manager, or the VP of operations. 3PL fees come from the freight budget | Integration needed: order lines (ERP), shipments, rates for several modes and customer delivery windows. An ERP-like project (R28) | 17 TMS vendors in Gartner's quadrant. MercuryGate bought by Körber (Oct 2024). Kuebix bought for $200M, then shut down (*assumed*). No dominance | Managed-transportation 3PLs (per shipment, % of spend, gainshare; 50/50 *assumed*); intermodal marketing companies | 0.5 / 0.5 / 1 / 0.5 / 0.5 / 1 / 0.5 / 0 | R33, N-D32, N-R10, N-R11, N-R23, N-F28, N-E28, N-A30 |
| **C-17** Controlling inbound freight from suppliers | "Only about 35% of companies use a formal routing guide for inbound freight" (vendor, unsourced, *assumed*). No neutral figure found | No direct forcing event for mid-sized buyers. The 2026 rate rise raises the freight built into supplier prices (N-D31); tariffs put landed cost under scrutiny (N-C15) | Purchasing, which owns supplier terms; inbound freight lands in the cost of goods. Logistics co-owns | Integration needed, with some data missing: POs with freight terms are in the ERP, but prepaid freight is hidden in supplier prices, and suppliers must be onboarded | About 7 named inbound tools or programs. No shares. No dominance | 3PL inbound and routing-guide programs (C.H. Robinson's TMC, TLI) on fees or gainshare | 0.5 / 0.5 / 1 / 0.5 (buyer) / 0.5 / 1 / 0.5 (buyer) / 0 | N-E31, N-K28, N-R25, N-R20, N-R21, R33, N-E27, N-E28 |

---

## 2. Card by card

**Two notes that apply to all six cards:**
- **Role counts** come from BLS OEWS for May 2025, pulled through the BLS API (N-F22, extended here with new series, *verified*). They cover all firm sizes and all of each job's tasks. Freight is only part of what these people do, so the wage bills are orders of magnitude, not savings.
- **Shared buyer.** All six cards sell to the same buyer: small and mid-sized manufacturers and distributors. §3 shows where one product could serve several cards.

### 2.1 C-01 · Buying truckload capacity

**Item 5: software penetration and why now**
- **How the job is done today:**
  - A logistics coordinator or traffic manager, often part-time, phones or emails brokers and carriers for spot quotes.
  - Yearly lane bids run on spreadsheets and email, or the whole job is handed to a broker or a managed-transportation 3PL (scan F, job (a), *assumed*).
  - In a 2018 survey of 533 carriers, "approximately 63% of load offerings come via direct interaction between the carrier and shipper", 23% came through brokers and 14% from load boards (N-E22, trade press).
- **Penetration figures (all weak):**
  - TMS use by yearly freight spend: over $100M, 50%; $25-100M, 25%; under $25M, "Roughly 10%" (a Gartner study quoted by a logistics provider's 2019 blog; year and method unknown; N-E20, *assumed*).
  - Two sources conflict with this:
    - "About seven out of 10 shippers use a TMS", the non-users shipping mainly parcel and some LTL (a freight-audit CEO; N-F29, *assumed*);
    - "35% of respondents currently are using TMS, up from 25% last year" (Peerless Research / Modern Materials Handling, 2025; a warehouse and DC readership; page blocked; N-R23, *assumed*).
  - Descartes/SAPIO 2025 survey (N-F28, re-read; vendor survey, *assumed*):
    - 616 respondents, "evenly split between logistics services providers ... and shippers", in the US, Canada and Western Europe;
    - "Only 17% of respondents report being fully automated", and "over one-third heavily or mostly reliant on manual processes";
    - "80% of respondents plan to increase TMS IT spending".
  - Largest shippers: "50% of the largest enterprise shippers in the U.S. still rely on some combination of email and spreadsheets" (R28, 2021).
  - **Reading [our call]:**
    - The figures disagree because their samples differ: spend tiers, warehouse readers, and a mix of shippers and logistics firms.
    - None measures mid-sized manufacturers and distributors directly.
    - The safe statement is that most mid-sized shippers buy truckloads without a procurement tool.
- **Plumbing (Bushel's test, R30):**
  - Larger shippers tender by EDI 204 (tender) and 990 (reply); others use email, phone, or broker and carrier portals and APIs (N-R24; the general practice is *assumed*).
  - Lane history sits in the ERP (orders, ship-to addresses), in spreadsheets, and in carrier and broker invoices (EDI 210 or PDF).
  - Market-rate benchmarks are bought from data firms such as load boards: DAT claims "more than 291 million loads & trucks posted annually" (N-F41, vendor).
  - **Reading [our call]:** the pipes for tendering exist, but the benchmark is a paid input.
- **Why now (named triggers):**
  - **Capacity squeeze, 2026.** U.S. Bank's Freight Payment Index for Q2 2026 (N-D31, re-read; U.S. Bank is an FAP provider, so this is *assumed* as vendor data):
    - shipments -2.8% year on year, but spending **+28.1%**;
    - "The more important trend is that trucking capacity continues to tighten after several years of excess supply".
  - **Driver-supply rules with dates.**
    - FMCSA's final rule limits non-domiciled CDLs to holders of H-2A, H-2B and E-2 visas. It was published 2026-02-13 and took effect 2026-03-16 (N-R13, *verified*). An interim rule had taken effect on 2025-09-29 (search summary, *assumed*).
    - The rule says "more than 30 States have issued tens of thousands non-domiciled CDLs" (N-R13).
    - Trade sources report more than 14,000 drivers put out of service for English-proficiency violations since June 2025. They forecast 2026 contract rates up 7.6% for dry vans and spot rates up about 8.1% (N-R15, snippets, *assumed*).
  - **Technology.** AI agents for broker calls and quotes are being funded (HappyRobot, N-G44). The same shift could lower the cost of automating a shipper's quote requests (*assumed* inference).
  - **Reading [our call]:** a rate spike after a three-year slump is when shippers re-bid their lanes. It is also when brokers gain power, so it helps the problem more than it helps a newcomer.

**Item 6: addressable work**

| SOC | Role | All industries (mean wage) | Manufacturing | Wholesale |
|---|---|---|---|---|
| 13-1081 | Logisticians (logistics coordinators and analysts) | 251,040 ($89,730) | 56,330 ($90,670) | 27,360 ($79,830) |
| 11-3071 | Transportation, storage and distribution managers (traffic managers) | 221,180 ($121,600) | 29,990 ($127,290) | 34,350 ($113,970) |
| 13-1020 | Buyers and purchasing agents (buy freight in some firms) | 491,430 ($83,770) | 112,200 ($82,180) | 70,490 ($77,210) |

- **Wage bill for manufacturing plus wholesale [our calc]:** logisticians $7.29B; transportation managers $7.73B.
- **Text- and number-heavy office work (R22)?** Yes: quotes, lane bids and rate comparisons. Bessemer names "freight procurement for a shipper" as a supporting workflow (R22).
- **"Human connection isn't a key benefit" (R23)?** Partly fails.
  - "Freight is a relationship-driven business" (R27, *assumed*). Carriers are chosen partly on trust and on service when capacity is tight.
  - **[our call]:** finding rates and running bids pass the R23 screen; the relationship with a shipper's core carriers does not.

**Item 7: budget holder and implementation**
- **Budget:** the logistics or transportation manager's freight budget, or purchasing in some firms (card C-01). The saving shows as a lower freight line: outbound freight in selling costs, inbound freight in the cost of goods (*assumed* accounting practice).
- **Value on day one (R28)?** Only partly.
  - A bid tool can show "rates below benchmark" in its first bid cycle.
  - But whether shippers would credit software for savings against a moving benchmark is open (K7, for S5).
  - Rates swing by about ±40% within a few years (R34), so the saving is hard to attribute (`submarket_selection.md` §7).
- **Live in weeks?**
  - A lane-bid or spot-quote tool: weeks. It needs an export of shipment history and a list of carriers.
  - A full TMS: months. "Supply chain software implementations have traditionally looked a lot like ERP implementations" (R28).
- **Data needed, and where it sits:**
  - past loads and lanes: ERP, spreadsheets, broker invoices;
  - carrier contacts;
  - rate benchmarks: bought;
  - a way to tender: email, EDI 204 or API.

**Item 9: competitors, substitutes and the incumbent map**
- **Software vendors: 12 named** in one vendor's 2026 list of freight-procurement tools (N-F46, now read in full; vendor, *assumed*):
  - main list: Transporeon, Freehand, Keelvar, GoComet, GoodShip, MercuryGate and Sleek Technologies;
  - also mentioned: Shipsy, Freightify, Fretron, Trimble and FreightFox;
  - the list tags all seven main vendors "Enterprise", and gives Sleek's entry point as "~$50K";
  - S1 also named Emerge.
- **TMS products with procurement modules:**
  - Gartner evaluated 17 TMS vendors in 2025 (N-D32).
  - The field is consolidating. Körber completed its purchase of MercuryGate on 2024-10-01 (N-R11, *verified*). Trimble bought Transporeon in December 2022 (N-R10, *assumed*).
- **Leader's share:** none published. **Dominance: none.** No vendor comes near half of mid-sized shippers.
- **Service firms (the real incumbents):**
  - 25,081 active broker authorities (N-F03), keeping a spread of about 15% of gross (N-F17 **[our calc]**);
  - digital brokers such as Uber Freight;
  - managed-transportation 3PLs, paid "a flat amount per shipment or a percent of the purchased transportation", with gainshares (R33, *verified*).
- **Features inside larger products:** TMS procurement and rating modules; load-board rate tools such as DAT and Truckstop (*assumed*).
- **How it is done today, including doing nothing:**
  - phone, email and spreadsheets;
  - handing the whole job to one broker;
  - no evidence either way on general-purpose AI tools (for example, drafting bid emails).
- **How incumbents charge (evidence only):**
  - brokers keep the spread;
  - 3PLs charge per shipment, a % of spend, or a gainshare (R33; 50/50 *assumed*, N-A30);
  - software charges "transaction-cost" (Transporeon), "performance-based" (Freehand) or subscription (GoodShip) fees (N-F46, vendor).

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 0.5 | The work is office work, but the cost is the market rate itself, which software can only shade. Mixed |
| A3 | Shipper 1; carrier 0.5. **Better: shipper** | The 2026 capacity squeeze (spend +28.1%, N-D31) and the dated driver rules (N-R13) force shippers to re-bid. Carriers gain from the squeeze |
| A6 | 1 | Lane, rate and carrier data feed C-14 (planning), C-17 (inbound), C-09 (audit checks bills against rates) and C-02 (status). Horizontally, every shipper group in the grid buys truckloads |
| W1 | Shipper 0.5; carrier 0.5 | Shipper associations (NITL, NASSTRAC, CSCMP) gather mostly large shippers (N-R18, *assumed*). Carriers gather on load boards, but the boards are incumbents (N-F41) |
| W3 | 0.5 | Shipment history must be exported from the ERP or spreadsheets, and a rate benchmark bought. The pipes for tendering exist (email, EDI 204, APIs) |
| W4 | 1 | Proven spend: broker spreads and 3PL fees (R33, N-F17). Weak software for the mid-market: the procurement tools are listed as enterprise (N-F46); about 10% use a TMS below $25M of spend (N-E20, *assumed*) |
| W5 | Shipper 0.5; carrier 0.5 | Relationship-driven buying (R27) against a vendor survey where 80% plan more TMS spending (N-F28). No mandate |
| W6 | 0 | Winning needs a rate benchmark, carrier access, and displacing brokers in a tightening market. Whether customers would credit software for the saving is still open (K7) |

### 2.2 C-09 · Auditing and paying truckload and LTL bills

**Item 5: software penetration and why now**
- **How the job is done today:**
  - An accounts-payable (AP) clerk or logistics coordinator matches each invoice to the BOL, the POD and the quote, and disputes errors by email (scan F, job (e1), *assumed*).
  - Or a contingency audit firm reviews paid bills after the fact (N-A26).
  - Larger shippers use an FAP provider.
- **Penetration:**
  - Cass "provides payment and information processing services to large manufacturing, distribution and retail enterprises" (N-D30, re-read, *verified*).
  - Cass paid $36.4B across 34.5M invoices in 2025 (N-D30). U.S. Bank pays "$46 billion in freight payments annually" (N-D31). Together that is about 9% of 2024 US trucking revenue of $906B (check D **[our calc]**).
  - Gartner's 2026 guide, as quoted by a vendor: "51% of enterprise shippers are already outsourcing with 28% more looking to outsource in the next two years" (N-R05, *assumed*). This covers enterprises only.
  - **Reading [our call]:** among mid-sized shippers, the incumbent is the AP clerk, a small audit firm, or nobody (check D, worked example 2). No survey measures this.
- **Is the cost clerk time or overcharges?** Mostly overcharges.
  - APQC's database of 1,485 organisations (N-R14, *verified*; from 2018, so dated) gives the cost of processing one invoice:
    - median $5.83;
    - top quartile $2.07 or less;
    - bottom quartile $10 or more;
    - distribution and transportation median $1.14.
  - Against that, "recoverable errors often range from 2% to 8% of freight spend" where there is no audit (N-A32, *assumed*).
  - **[our call]:** the pool is overcharges, not clerk time.
- **Plumbing:**
  - Carrier invoices arrive as EDI 210 from larger carriers, or as PDFs by email or portal (scan G chain C; *assumed*).
  - BOL and POD images come from carrier portals.
  - Rate agreements and LTL tariffs are held by the shipper.
  - Payments sit in the ERP's AP module. NetSuite's app marketplace lists freight apps that include invoice audit, such as Freightgate and FreightPOP (N-R21, *assumed*).
  - AI document reading makes PDF invoices usable without EDI. Cass gathers data by several methods, "including those supported by artificial intelligence ("AI")" (N-D30, *verified*).
- **Why now (named triggers):**
  - **AI in audit.**
    - Gartner, as quoted by a vendor: "FAP solutions are shifting from manual review processes to AI-enabled automation" (N-R05, *assumed*).
    - Loop, an AI audit firm, announced a $95M Series C on 2026-04-17 (N-R06). Its total of $210M comes from a search summary (*assumed*).
    - Cass's own 10-K warns that if competitors bring in AI "more quickly or more successfully", its "existing product and service offerings ... may become obsolete" (N-D30, *verified*).
  - **Payment fraud.** AFP's 2026 survey of 465 US treasury practitioners (January 2026; N-R01, *verified*, a trade association's survey):
    - "More than three-quarters of organizations (76%) in the United States experienced attempted or actual payments fraud in 2025";
    - checks were the most targeted method (58%), then ACH debits (30%) and wires (25%);
    - "About three in four organizations (74%) were affected by business email compromise (BEC)";
    - "Just 17% of organizations leverage AI to combat payments fraud".
  - **Rising spend, and LTL bills that change after pickup.**
    - Spend +28.1% year on year in Q2 2026 (N-D31) makes each overcharge bigger in dollars.
    - The NMFC changes cause "differences between the original bill of lading estimate and the final invoice" (N-R02, *verified*).
  - **The incumbent is under strain.** Cass: "volumes continue to decline on a year-over-year basis, which continues to put pressure on transportation related processing fees" (N-D30, *verified*).

**Item 6: addressable work**
- **Roles:**
  - 43-3031, bookkeeping, accounting and auditing clerks (which includes AP clerks): 1,373,680 nationally ($53,560); manufacturing 91,710 ($54,660); wholesale 100,750 ($53,610).
  - Their wage bill across manufacturing and wholesale is $10.41B **[our calc]**, of which freight bills are a small part.
  - 43-3021, billing and posting clerks (the carrier side): 404,060 ($51,070).
  - 13-1081, logisticians: see C-01.
- **Text- and number-heavy?** Yes. The work is matching invoice lines to rates, weights and extra charges. R28 names "invoice processing" as a target.
- **Human connection?** Not a key benefit; disputes are routine letters. It passes R23.

**Item 7: budget holder and implementation**
- **Budget:**
  - Finance holds it (the controller, CFO and AP team), and logistics co-decides (card C-09).
  - FAP fees are "service fees which are typically calculated on a per-item basis" (Cass, N-D30, *verified*).
  - A contingency audit needs no budget line at all: the shipper keeps "50–75% of the total recovery" (N-A26).
- **Value on day one?** Yes, for a look-back audit. Past invoices, BOLs and rate sheets show overcharges within days, which is how the contingency firms work.
- **Live in weeks?**
  - Audit only: weeks. It needs an export of paid invoices plus the rate agreements.
  - Paying carriers as well: months. That needs ERP payment integration, a bank or payments partner, and onboarding each carrier. Cass and U.S. Bank are both banks (N-D30).

**Item 9: competitors, substitutes and the incumbent map**
- **Software and FAP vendors:**
  - Gartner's guide covers about 15 providers (N-F50, *assumed*); its list was not seen (§5).
  - **16 are named across sources:**
    - FAP providers: Cass, U.S. Bank, Trax, nVision Global, CTSI-Global, Intelligent Audit, CT Logistics, Data2Logistics, RateLinx, TranzAct, enVista and Loop (N-F50, N-F51);
    - Freehand, which is in the 2026 guide (N-D33);
    - NetSuite apps with invoice audit: Freightgate and FreightPOP (N-R21);
    - MyCarrier, an LTL platform with audit and payment (N-R22).
- **Leader's share:** Cass about 4% and U.S. Bank about 5% of trucking revenue (check D **[our calc]**).
- **Dominance: none.** Neither leader serves half the target customers, and Cass aims at large enterprises (N-D30).
- **Service firms:**
  - "Competition consists of a few primary competitors and numerous small transportation bill audit firms located throughout the United States. While offering transportation payment services, few of these audit firms compete on a national basis" (N-D30, *verified*).
  - They work on 25-50% contingency (N-A25, N-A26).
- **Features inside larger products:**
  - TMS freight-settlement modules;
  - ERP three-way matching in AP, which checks the invoice against the purchase order and the receipt (*assumed*);
  - bank payables services such as U.S. Bank's.
- **How it is done today:**
  - pay as billed, sometimes with a yearly contingency post-audit (*assumed*);
  - doing nothing;
  - general-purpose AI to read PDFs: no evidence found.
- **How incumbents charge (evidence only):**
  - per item, plus "discounts received for services provided to carriers" and float on "the accounts and drafts payable balances" (Cass, N-D30, *verified*);
  - % of spend, a gainshare of 30-50%, or a subscription (N-F51, *assumed*);
  - contingency of 25-50% (N-A26).

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 1 | Matching bills to rates and proofs is text- and number-heavy office work. The cost (overcharges and clerk time) comes from information errors |
| A3 | Shipper 1; carrier 0.5. **Better: shipper** | Three named, dated drivers: payment fraud (76%, N-R01), LTL class changes that alter bills after pickup (N-R02, N-R03), and spend +28% (N-D31). Alternative reading: none of them targets freight bills as such, which would give 0.5 |
| A6 | 1 | The same invoice, rate and proof data serve C-10 (claims), C-11 (LTL disputes), C-03 (extra charges), C-12 (parcel audit) and C-18 (warehouse bills), and lead to a payments layer (`submarket_selection.md` §6, implication 4) |
| W1 | Shipper 0.5; carrier 0.5 | Finance buyers are dispersed. Partial channels exist: ERP app marketplaces (N-R21), banks, and AFP for treasury staff. Carriers gather in factoring and payment networks (TriumphPay, N-F44) |
| W3 | 1 | A look-back audit needs only files the shipper already holds (invoices, BOLs, rate sheets), which is how contingency firms work. 0.5 if paying carriers is in the first product |
| W4 | 1 | Proven spend: contingency fees of 25-50% and per-invoice FAP fees. Software for the mid-market is weak or missing: the leaders serve large enterprises (N-D30). Caveat: funded AI entrants (Loop, Freehand) may close this gap within the 5-year clock |
| W5 | Shipper 0.5; carrier 0.5 | No mandate. Enterprise outsourcing is rising (N-R05, *assumed*), but 72% of organisations that write checks plan to keep doing so, 68% because vendors require them (N-R01) |
| W6 | 1 (0.5 if payment is in from launch) | An audit-first wedge shows value in days, needs no network, and has a fee precedent. Paying carriers adds a bank partner, money movement and carrier onboarding |

### 2.3 C-10 · Cargo loss and damage claims

**Item 5: software penetration and why now**
- **How the job is done today:**
  - A logistics coordinator or claims clerk files a written claim with the carrier.
  - The receiving clerk notes damage or shortage on the POD (scan F, job (g)).
  - Operations teams rely on "spreadsheets, carrier portals, and institutional memory" (N-K21, re-read; vendor, *assumed*).
- **Penetration** (all *assumed*: vendor figures, sample not disclosed):
  - "only 28% of mid-market shippers" use dedicated claims software, and "under 8%" use AI automation (N-K21).
  - "Only 42-50% of eligible claims are actually filed" (N-K21).
  - A broker-focused vendor says "30–50% of those claims never get filed within the 9-month Carmack window" (N-R08).
- **Rules and plumbing:**
  - **What a valid claim needs** (49 CFR 370.3, N-R09, *verified*):
    - "A written communication from a claimant, filed with a proper carrier within the time limits specified";
    - facts that identify the shipment, a statement "Asserting liability", and "a specified or determinable amount of money";
    - damage notes are not enough on their own: "Bad order reports ... notations of shortage or damage ... shall, standing alone, not be considered ... sufficient".
  - **Deadlines:** carriers must acknowledge a claim within 30 days and pay, decline or offer within 120 days (49 CFR 370.5 and 370.9; N-F35, *verified*). Shippers get at least 9 months to file (N-F36, *verified*).
  - **Where the evidence sits:** with the shipper. That means POD exceptions (receiving), photos, the commercial invoice (the goods' value), the BOL and the freight bill.
  - **Where claims go:** each carrier's own portal or claims email. One robotic-process vendor files "across 50-plus portals" (iNymbus, N-R07, *assumed*). No industry claims API was found.
- **Why now (named triggers):**
  - **Cargo theft at a record** (Verisk CargoNet, US and Canada, via Claims Journal, 2026-01-28; N-R04; CargoNet is a vendor dataset, so *assumed*):
    - estimated losses "surged to nearly $725 million, a 60% increase from a year ago";
    - 3,594 supply-chain crime events in 2025, against 3,607 in 2024;
    - confirmed thefts 2,646, up 18%;
    - an average of $273,990 per theft, up 36%.
  - **AI claims tools have launched:** Freehand, CorePiper and Ladingly (N-R07, N-K21, N-R08; vendor).
  - **Rising freight rates** raise the freight-charge part of each claim (*assumed*).

**Item 6: addressable work**
- **Roles:**
  - 43-5071, shipping, receiving and inventory clerks, who record damage at receipt: 816,870 nationally ($46,810); manufacturing 230,110 ($48,650); wholesale 124,950 ($46,710).
  - 13-1081, logisticians: the claims coordinator (see C-01).
  - The carrier's claims clerk has no SOC code of its own. SOC 13-1031, claims adjusters (324,230, $80,470), works mostly in insurance, so it is not a clean proxy.
- **Text-heavy?** Yes: assembling proof and writing claims in a fixed legal format. The physical damage itself is out of scope; the part software addresses is the loss left unrecovered.
- **Human connection?** Not a key benefit. It passes R23.

**Item 7: budget holder and implementation**
- **Budget:** logistics or finance. Recoveries are credited to the cost of goods or to other income (*assumed*); insured losses go through risk management. Contingency services are paid from recoveries, so no budget line is needed.
- **Value on day one?** Partly.
  - The first batch of open or recent claims can be filed at once, so the amounts at stake show within days.
  - The cash arrives 30-120 days later, by rule (N-F35).
- **Live in weeks?** Yes, if the product starts from the shipper's own exception records and documents. It is harder where receiving staff do not record exceptions, because then the dock's habits must change.

**Item 9: competitors, substitutes and the incumbent map**
- **Software and modules: 12 named** (N-R07, N-F51, N-F56, N-K21, N-R08; all vendor, *assumed*):
  - claims software: Freehand, iNymbus (about $0.40-0.70 a claim), TranSolutions MyEZClaim (licence), FreightClaims.com, CorePiper, Ladingly, Claimable and VTM TRANSWARE;
  - modules inside larger products: Descartes 3G TMS, CargoWise and Loop;
  - managed claims services: Cass and nVision.
- **Leader's share:** none published. **Dominance: none.** Only 28% of mid-market shippers use any claims software (N-K21, *assumed*).
- **Service firms:**
  - Recoupex ("if we don't win, you don't pay"), TLI, Sheer Logistics and GEODIS (N-F56, scan F);
  - Cass's and nVision's managed claims services;
  - brokers, which file claims for their shippers.
- **How it is done today, and the substitutes:**
  - Doing nothing is the biggest substitute: about half of eligible claims are never filed (N-K21).
  - Cargo insurance on high-value loads (*assumed*).
  - Carriers' limits on liability shrink what can be recovered (*assumed*).
  - General-purpose AI tools: none found.
- **How incumbents charge (evidence only):**
  - contingency: Ladingly takes a "20% contingency on recovered funds" and says "Typical claims BPOs charge 25–30%" (N-R08, *assumed*);
  - per claim (iNymbus), licence (TranSolutions), or "performance-based" (Freehand) (N-R07).

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 1 | Claims are document assembly and letters in a fixed legal format (N-R09) |
| A3 | Shipper 1; carrier 0.5. **Better: shipper** | The theft record (losses +60%, N-R04) is a named crisis. The 9-month Carmack clock is a standing deadline, not a new one. Alternative reading: theft losses are often insured, which would give 0.5 |
| A6 | 1 | The same proof-and-dispute core reaches C-09, C-11, C-03, parcel claims (C-12) and retailer deductions (C-19). iNymbus already files across parcel, retailer and ocean portals (N-R07) |
| W1 | Shipper 0.5; carrier 0.5 | TLC runs claims seminars for shippers (N-R19), and brokers are a partner channel (Ladingly sells to brokers, N-R08). No single gathering point |
| W3 | 0.5 | The evidence is at hand at the shipper, but filing means many carrier portals and emails, and there is no claims API |
| W4 | 1 | Proven spend: contingency fees of 20-30% (vendor claims) and staff time. Software is weak: 28% use any (vendor), mostly licensed legacy tools and modules |
| W5 | Shipper 0.5; carrier 0. **Better: shipper** | Doing nothing is common, which signals low salience rather than a wish to change. Carriers resist: they deny 50-60% of LTL claims (N-K21, *assumed*) |
| W6 | 0.5 | Easy to start, and no network is needed. But the proof in cash takes up to 120 days per claim, and dock habits must change |

### 2.4 C-11 · LTL class, reweigh and reclass disputes

**Item 5: software penetration and why now**
- **How the job is done today:**
  - The shipping clerk picks an NMFC item and class, then books on a carrier portal or a broker's or 3PL's quote site.
  - Reweigh and reclass corrections appear on the invoice "2–6 weeks after delivery" (scan G chain C; N-G23, vendor).
  - Disputes go by email with photos and dimensions, or nobody disputes.
- **Penetration:**
  - No survey was found of how small shippers book LTL or dispute corrections.
  - Tools priced for small shippers exist (N-R22, *assumed*):
    - Freightview "starts at $149/month for the 0-50 Ships plan" (Capterra);
    - MyCarrier markets "quoting, booking, tracking, freight audit, and payment on one connected platform — with direct carrier rates and no broker markups" (vendor).
  - WWEX Group (Worldwide Express, GlobalTranz, Unishippers) claims "more than 121,000 customers", "200 franchises and 500 agents", and a focus on "small business and mid-market customers" (N-R12, company claim, *assumed*).
- **Plumbing:**
  - **Industry API standards.** NMFTA's Digital LTL Council publishes several (N-R26, N-R02, *verified*):
    - an eBOL (electronic bill of lading) standard, now at version 2.1;
    - pickup request and visibility;
    - in-transit visibility;
    - since 2025, the **Preliminary Freight Charges (PFC) API**. It "gives all parties visibility into freight bill charges as they evolve throughout the shipment lifecycle", with "real-time charge notifications for reclassifications, accessorials, and more".
    - How many carriers have adopted them: not found.
  - **Class data:** NMFTA's ClassIT+, which needs a licence (N-G20, N-R03).
  - **Invoices:** EDI 210 or PDF.
  - **Proof of the correction:** the carrier's dimensioner record (from its automatic measuring machine) and the W&R certificate, both held by the carrier.
- **Why now (named triggers):**
  - **Docket 2025-1,** effective 2025-07-19: "A 13-tier density scale replaced 11 classes", and "2,000+ commodities" were consolidated (N-G20, *verified*).
  - **Docket 2026-1** (N-R03, *verified*):
    - issued 2026-02-06, with a public meeting on 2026-03-10;
    - 22 subjects;
    - several subjects move items onto "FCDC's standard 13-subprovision density scale";
    - the amendments are "scheduled to be issued on April 24, 2026, with an effective date of May 23, 2026. ClassIT+ will be automatically updated on May 23, 2026".
  - **NMFTA's own reason for the PFC API:** the changes "introduce new considerations around reweighs, reclassifications, and accessorials", and cause "billing surprises that hit weeks after pickup" (N-R02, *verified*).
  - **Price rises:**
    - late-2025 GRIs of 4.9% (Old Dominion) and 5.9% (Saia, FedEx Freight, ABF) (N-R16, snippets, *assumed*);
    - carriers raise their class tariffs every year (the 2023 round, N-R17, *verified*).

**Item 6: addressable work**
- **Roles:**
  - 43-5071, shipping clerks: 816,870 nationally; manufacturing 230,110; wholesale 124,950 (N-F22 extended, *verified*);
  - logisticians;
  - AP clerks, for disputes.
- **Text- and number-heavy?** Yes. Density is arithmetic, the NMFC item is a lookup, and disputes are letters with photos and dimensions. The one physical step, measuring the pallet with a tape or a dimensioner, is short.
- **Human connection?** Not a key benefit. It passes R23.

**Item 7: budget holder and implementation**
- **Budget:** the shipping or logistics lead, from the outbound freight budget. Disputes are handled by logistics or AP.
- **Value on day one?** Yes, two ways:
  - checking past LTL invoices against their BOLs shows the corrections at once, as in an audit;
  - classing correctly before pickup prevents corrections from the first shipment.
- **Live in weeks?** Yes, for disputes and class checks built from invoices, BOLs and the item master. The ClassIT+ licence and each carrier's rules add setup time.

**Item 9: competitors, substitutes and the incumbent map**
- **Vendors: about 7 named:**
  - LTL tools: MyCarrier, Freightview, FreightPOP, FreightCenter and Freightquote (C.H. Robinson) (N-R22);
  - NMFTA's ClassIT+ for class lookup (N-R03);
  - SMC3 for base rates (*assumed*, from S1 leads).
  - Dimensioners are hardware and were not researched.
  - No standalone tool for reclass disputes was found. Disputes sit with audit firms and 3PLs.
- **Leader's share:** none published. **Dominance: none among the tools.** NMFTA controls the class data: a dependency, not a competitor.
- **Service firms:**
  - LTL-focused 3PLs and brokers, such as WWEX Group, C.H. Robinson/Freightquote and FreightCenter (N-R12, N-R22);
  - audit firms, which recover "3–8%" of LTL spend (N-A26).
- **The carrier side:** the top 10 LTL carriers hold about 82% of the market (N-G22). That side is ruled out on K10.
- **How it is done today:**
  - accept the correction (doing nothing);
  - ask the 3PL rep to dispute it;
  - general-purpose AI tools: none found.
- **How incumbents charge (evidence only):**
  - 3PL markup on carrier rates (*assumed*);
  - software subscriptions from $149 a month (N-R22);
  - audit contingency of 25-50% (N-A26).

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 1 | Class and density are arithmetic on data the shipper holds, and disputes are documents. The only physical step, measuring the pallet, is short |
| A3 | Shipper 1; carrier 0.5. **Better: shipper** | Two dated NMFC dockets (2025-07-19, 2026-05-23), plus NMFTA's own statement that they cause billing differences (N-R02) |
| A6 | 1 | The same rating and proof core serves C-09 (LTL bills), C-10 (LTL claims), C-14 (pooling LTL into multi-stop loads) and parcel size-based pricing (C-12) |
| W1 | Shipper 0.5; carrier side ruled out (K10) | LTL 3PL franchise networks gather many small shippers (WWEX claims 121,000+ customers, N-R12), and NASSTRAC is an LTL-minded shipper council (N-R18). But no single channel gathers most of them |
| W3 | 0.5 | BOLs, item masters and invoices are at hand. But class data needs a ClassIT+ licence, and the carrier's measurement proof sits with the carrier. The PFC API could help; its adoption is unknown |
| W4 | 1 | Proven spend: 3PL markups and audit contingencies. Dispute software is missing: no standalone tool was found |
| W5 | Shipper 1; carrier side ruled out. **Better: shipper** | The NMFC change itself says systems "should be updated … to ensure billing accuracy and prevent disputes" (N-G21) |
| W6 | 0.5 | Moderate. It needs the class-data licence, each carrier's rules, and a channel partner |

### 2.5 C-14 · Planning and consolidating shipments

**Item 5: software penetration and why now**
- **How the job is done today:**
  - A traffic manager or logistics analyst chooses modes and pools orders in spreadsheets.
  - Or the job goes to a managed-transportation 3PL or an intermodal marketing company, which moves long lanes by rail (card C-14; scan F, job (a)).
- **Penetration:**
  - The same weak TMS figures as C-01 (N-E20, N-F29, N-R23, N-F28).
  - A 3PL study snippet: "Sixty-two percent of shippers are outsourcing domestic transportation" (N-E23, *assumed*).
  - An analyst on smaller shippers (N-R10, secondary, *assumed*):
    - "Do we have the resources internally to effectively use and manage a TMS?"
    - "Do we have the skills and discipline to keep the TMS tuned?"
    - They may instead use "managed transportation services — the logistics equivalent of cloud computing".
- **Plumbing:**
  - order lines and ship-to data sit in the ERP;
  - rates for several modes (LTL tariffs, truckload quotes, intermodal quotes) come from carriers and brokers;
  - tenders go by EDI 204, API or email;
  - the optimisation engines live inside TMS products.
- **Why now (named drivers):**
  - The 2026 capacity squeeze widens the gap between pooled and unpooled freight: spend +28.1% year on year (N-D31).
  - LTL GRIs of 4.9-5.9% (N-R16, *assumed*).
  - **Walmart's "Prepaid Consolidation Program"** (May 2026; N-E28, scan E). Suppliers ship one national purchase order to one location; Walmart spreads it across "42 regional distribution centers" and charges a per-case rate. It shows a large buyer pushing consolidation onto its suppliers.
  - In the Descartes survey, route and load optimisation is the second most-cited AI use case, at 39% (N-F28, vendor).
  - **Reading [our call]:** these raise the value of planning, but none forces it.

**Item 6: addressable work**
- **Roles:**
  - 11-3071, transportation managers ($121,600; manufacturing 29,990; wholesale 34,350);
  - 13-1081, logisticians, as analysts (N-F22 extended; see C-01).
- **Number-heavy?** Yes, for the analysis. But the saving needs operational change: order cut-offs, delivery windows and dock schedules. That part is not office work.
- **Human connection?** Not key for the analysis. The trade-offs on delivery promises involve sales and customers.

**Item 7: budget holder and implementation**
- **Budget:** the transportation manager or the VP of operations. 3PL fees come from the freight budget, and gainshares from the savings.
- **Value on day one?** Only on paper.
  - A what-if run on past shipments can show potential savings within days.
  - Real savings come only after operations change, measured against a baseline. "Agreeing a baseline is the main reason gain sharing arrangements are not used" (N-A30, *assumed*).
- **Live in weeks?** No. It is an ERP-like integration (R28).

**Item 9: competitors, substitutes and the incumbent map**
- **Vendors:**
  - Gartner evaluated 17 TMS vendors in 2025 (N-D32).
  - Named: MercuryGate (now Körber, N-R11), Trimble/Transporeon, Descartes 3G, and S1's names (Oracle, Blue Yonder, e2open; *assumed*).
  - Kuebix: Trimble paid "$200 million" for it in January 2020, then decided "to shut down Kuebix". It is now offered by FreightWise (N-R10, *assumed*). This is a mid-market shipper TMS that failed.
- **Leader's share:** none published. **Dominance: none.**
- **Service firms:**
  - managed-transportation 3PLs (R33), e.g. C.H. Robinson's TMC (*assumed*);
  - intermodal marketing companies: 18.5M intermodal units moved in 2025 (N-F14);
  - brokers that offer consolidation.
- **How it is done today:**
  - spreadsheets;
  - doing nothing, i.e. shipping each order as it comes;
  - a 3PL.
- **How incumbents charge (evidence only):**
  - per shipment, a % of purchased transportation, or a gainshare (R33, *verified*); 50/50 splits (N-A30, *assumed*);
  - TMS licence or subscription.

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 0.5 | The analysis is number-heavy, but the saving needs physical changes to how orders ship |
| A3 | Shipper 0.5; carrier 0.5 | The 2026 rate rise and the GRIs raise the value, but nothing forces the change. It becomes 1 only if the founders count the rate rise as a forcing event for every rate-driven job |
| A6 | 1 | Planning data reach C-01, C-17, C-11, C-15 and C-04 |
| W1 | Shipper 0.5; carrier 0.5 | As C-01 |
| W3 | 0.5 | ERP order data plus rates for several modes: an ERP-like project (R28) |
| W4 | 1 | Proven spend: 3PL fees and gainshares (R33). Mid-market software is weak (N-R10's questions; the Kuebix shutdown, *assumed*) |
| W5 | Shipper 0.5; carrier 0.5 | No mandate. Outsourcing to a 3PL is the usual answer |
| W6 | 0 | Optimisation, rates for several modes, execution and operational change must all go right, and savings need an agreed baseline (N-A30) |

### 2.6 C-17 · Controlling inbound freight from suppliers

**Item 5: software penetration and why now**
- **How the job is done today:**
  - Purchasing sets the freight terms on each purchase order (collect or prepaid).
  - Most inbound freight is left to the suppliers' carriers. Its cost is priced into the goods, or added to the supplier's invoice ("prepaid and add") (card C-17, *assumed*).
- **Penetration** (all vendor, unsourced, *assumed*):
  - "Only about 35% of companies use a formal routing guide for inbound freight" (N-E31).
  - "Nearly every large retailer mandates FOB Origin, Freight Collect in its vendor routing guide" (N-E31).
  - For manufacturers, inbound is "40-60% of total freight spend", and "If suppliers are controlling inbound freight, companies are probably overpaying by 15-30%" (N-K28).
  - **No neutral source** was found after three attempts (scan E, check N's MIT search, and this check).
- **Plumbing:**
  - POs and freight terms sit in the ERP, along with suppliers' ship-from data.
  - Inbound freight bills are visible only on collect loads. On prepaid loads the cost is buried in the supplier's price (*assumed*).
  - Suppliers book through the buyer's portal, by email, or through a 3PL.
- **Why now (named drivers):**
  - The capacity squeeze raises the freight built into supplier prices (N-D31).
  - Cass estimates that tariffs added "approximately $600 million" to its 2025 dollar volumes (N-C15), so landed cost is under scrutiny.
  - Large buyers are restructuring inbound: Walmart's collect program (N-E27) and its 2026 prepaid consolidation program (N-E28).
  - **Reading [our call]:** none of these is a forcing event for a mid-sized buyer.

**Item 6: addressable work**
- **Roles** (N-F22 extended, *verified*):
  - 13-1020, buyers and purchasing agents: 491,430 nationally ($83,770); manufacturing 112,200 ($82,180); wholesale 70,490 ($77,210).
  - 11-3061, purchasing managers: 84,320 ($156,360); manufacturing 20,100; wholesale 10,070.
  - Wage bill across manufacturing and wholesale **[our calc]**: buyers $14.66B and purchasing managers $4.48B. Freight is a small part of their work.
  - Also receiving clerks (43-5071), and on the supplier side, shipping clerks.
- **Text- and number-heavy?** Partly. Routing-guide rules and booking are office work, but changing freight terms is a commercial negotiation with suppliers.
- **Human connection?** Partly fails R23: supplier relationships are the purchasing team's core job.

**Item 7: budget holder and implementation**
- **Budget:** purchasing, which owns supplier terms; inbound freight lands in the cost of goods. Logistics co-owns.
- **Attribution is hard.** The saving is split between a lower product price and a new freight bill (K4 is still open).
- **Value on day one?** No. A baseline needs the suppliers' freight costs, which are hidden in their prices.
- **Live in weeks?** No. Onboarding suppliers and changing terms take months (*assumed*).

**Item 9: competitors, substitutes and the incumbent map**
- **Vendors: about 6-7 named** (N-R25, N-E31, N-K28; vendor): Freehand, FreightPOP, Freightsuite, FreightSimple, BTX Global, and Kuebix/FreightWise, whose inbound pitch ran in Inbound Logistics. TMS products also have inbound modules.
- **Leader's share:** none published. **Dominance: none.**
- **Service firms:**
  - C.H. Robinson's TMC took over routing-guide management for clients (N-R25, *assumed*);
  - TLI sells "vendor routing guide compliance" (N-R25);
  - managed-transportation 3PLs (R33).
- **The large-retailer model:** Walmart's collect pickups, priced as a share of the cost of goods (N-E27).
- **How it is done today:**
  - doing nothing: suppliers ship as they choose;
  - a PDF routing guide that nobody enforces (*assumed*).
- **How incumbents charge (evidence only):** gainshare (R33; 50/50 *assumed*, N-A30), or per shipment.

**Suggested row scores [our call]**

| Row | Score | Reason |
|---|---|---|
| A2 | 0.5 | Booking and rule-checking are office work, but the saving needs suppliers to change and freight terms to be renegotiated |
| A3 | Buyer 0.5; supplier 0.5 | The rate rise and tariffs raise landed costs, but nothing forces a mid-sized buyer to act |
| A6 | 1 | Inbound control links to C-14 (consolidation), C-01 (buying), C-09 (audit), C-04 (dock appointments) and C-19 (compliance charges) |
| W1 | Buyer 0.5; supplier 0. **Better: buyer** | Purchasing staff gather in ISM ("over 50,000 members", *assumed*) and use ERP marketplaces (N-R21), but suppliers are dispersed |
| W3 | 0.5 | POs and terms are at hand. The freight cost of prepaid loads is hidden in supplier prices and must be surfaced |
| W4 | 1 | Proven spend: 3PL inbound programs and gainshares. Mid-market software is weak: routing guides are often absent (N-E31, *assumed*) |
| W5 | Buyer 0.5; supplier 0. **Better: buyer** | Suppliers must follow the guide, and some earn a margin on freight (*assumed*) |
| W6 | 0 | It needs supplier onboarding, changed terms, and a baseline that is hidden in prices |

---

## 3. For the coordinator (not a call)

### 3.1 Patterns across the six cards

1. **Two families with one buyer.**
   - **The "money back after shipping" trio: C-09, C-10 and C-11.**
     - They share one set of data: the BOL, the POD, the carrier invoice (EDI 210 or PDF), the rate agreement and the NMFC class.
     - One product, an audit-and-recovery desk, could serve all three. Incumbents already bundle them: Cass sells audit plus claims; Loop and nVision have claims modules; TLI sells claims, and LTL 3PLs handle disputes.
     - They share the same budget story: contingency fees paid from recoveries, so no budget line is needed.
     - They are the §7 "good fit": discrete recoveries that can be counted.
   - **The "buy and plan before shipping" trio: C-01, C-14 and C-17.**
     - They share lanes, rates, carriers and orders.
     - This is TMS territory: heavier integration, relationship-driven buying, and savings measured against moving benchmarks or agreed baselines. K7 is open on C-01, and the gainshare baseline problem applies to C-14 and C-17 (N-A30).
2. **The same buyer firm, but different desks.** Finance and AP (C-09); logistics (C-01, C-10, C-11, C-14); purchasing (C-17). A bundle would cross budget lines inside the customer.
3. **The mid-market gap is consistent, but the evidence is thin.**
   - The leaders serve enterprises: Cass says so (N-D30); the Gartner figures are for enterprises (N-R05); the procurement tools are tagged enterprise (N-F46).
   - But every penetration figure for mid-sized shippers comes from a vendor or is dated.
4. **Funded AI entrants are arriving in the first trio:** Loop ($95M Series C, April 2026), Freehand (in the 2026 Gartner guide), CorePiper and Ladingly. The "weak software" half of W4 may erode within the 5-year clock.
5. **Timing favours the first trio.**
   - The 2026 capacity squeeze raises overcharges and claim values in dollars.
   - The LTL class changes (2025-07-19, 2026-05-23) are dated forcing events for C-11, and for the LTL half of C-09.
   - The squeeze also strengthens brokers, who are C-01's incumbents.
6. **Two cards partly fail R23's human-connection screen:** C-01 (relationships with carriers) and C-17 (relationships with suppliers). Both, and C-14, need other people's behaviour to change, which is why their W6 is 0.

### 3.2 Points from the rows suggested here [our calc]

Weights are from `0_criteria.md` §4. This is a partial sum: the coordinator adds A1, A4 and A5 on Axis A, and W2 on Axis W.

| Card | A2 (10) | A3 (25) | A6 (15) | **A points, of 50** | W1 (20) | W3 (20) | W4 (15) | W5 (15) | W6 (25) | **W points, of 95** |
|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | 5 | 25 | 15 | **45** | 10 | 10 | 15 | 7.5 | 0 | **42.5** |
| C-09 | 10 | 25 | 15 | **50** | 10 | 20 | 15 | 7.5 | 25 | **77.5** (65 if payment is in from launch: W3 and W6 both 0.5) |
| C-10 | 10 | 25 | 15 | **50** | 10 | 10 | 15 | 7.5 | 12.5 | **55** |
| C-11 | 10 | 25 | 15 | **50** | 10 | 10 | 15 | 15 | 12.5 | **62.5** |
| C-14 | 5 | 12.5 | 15 | **32.5** | 10 | 10 | 15 | 7.5 | 0 | **42.5** |
| C-17 | 5 | 12.5 | 15 | **32.5** | 10 | 10 | 15 | 7.5 | 0 | **42.5** |

**Where the readings are most contestable:**
- **A3 on C-01, C-09 and C-10** is 1 on events that do not target the job directly: the rate rise, fraud and theft. If the founders read any of them as indirect, that card's A3 falls to 0.5 (-12.5 points).
- **A3 on C-14 and C-17** would rise to 1 if the 2026 rate rise counts as a forcing event for every rate-driven job.

### 3.3 Show-stopper candidates (W4 dominance, rule C10)

- **None found.** No vendor serves more than half of mid-sized shippers for any of the six jobs.
- **The nearest is C-09.** Two large legacy FAP leaders each handle about 5% of trucking dollars and serve large enterprises, and one AI entrant has raised $210M (*assumed*). None serves half the target customers.
- **Dependencies to note (not W4 show-stoppers):**
  - C-11 depends on NMFTA's class data (a ClassIT+ licence) and on concentrated LTL carriers' measurement records. Carriers have the buying power there (Porter, R43).
  - C-01's service incumbents are 25,081 brokers: fragmented, not dominant.

### 3.4 Biggest gaps

1. **No neutral data on mid-sized shippers' software use for any of the six jobs:** TMS, FAP, claims or LTL tools. The figures come from vendor surveys (Descartes, CorePiper) or from a dated Gartner study seen only through a vendor (N-E20).
2. **No market shares** for FAP, claims, LTL or procurement software. Gartner's 2026 FAP vendor list was not seen.
3. **How many carriers have adopted NMFTA's APIs** (PFC, eBOL) was not found. This decides C-11's W3.
4. **Inbound overpay and routing-guide use are vendor-only** (C-17's K4 is still open). Claims contingency rates are also vendor-only.
5. **The driver-supply trigger's size:** the FTR analysis and the out-of-service counts were seen only through blocked pages or snippets.

---

## 4. Sources

### 4.1 New sources (N-R)

| ID | Source | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-R01 | AFP, "Over 75% of US Firms Experienced Payments Fraud in 2025, While AI Adoption for Fraud Mitigation Lags" (2026 Payments Fraud and Control Survey) | 2026-04-14 | https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags | full release; *verified* (a trade association's survey) | 465 respondents; 76% hit by fraud; checks 58%, ACH 30%, wires 25%; business email compromise 74%; AI used by 17%; 72% of check users plan to continue |
| N-R02 | NMFTA, "The NMFC Changes Are Live. Now It's Time to Stay Ahead of Billing Curve with New API" | 2025-08-11 | https://nmfta.org/news/the-nmfc-changes-are-live-now-its-time-to-stay-ahead-of-billing-curve-with-new-api/ | full; *verified* (primary) | What the PFC API does and who it serves; billing differences after the NMFC changes. No adoption figures |
| N-R03 | NMFTA / FCDC, Docket 2026-1 (PDF) | issued 2026-02-06 | https://nmfta.org/wp-content/uploads/2026/04/Docket-2026-1.pdf | full text extracted locally; *verified* | Meeting 2026-03-10; 22 subjects; effective 2026-05-23; items moved onto the 13-subprovision density scale |
| N-R04 | Claims Journal, "Verisk: Cargo Theft Losses Reached $725 Million in 2025" | 2026-01-28 | https://www.claimsjournal.com/news/national/2026/01/28/335280.htm | full article; figures are Verisk CargoNet data (a vendor), so *assumed* | Losses about $725M (+60%); 3,594 events; confirmed thefts 2,646 (+18%); average $273,990 |
| N-R05 | Intelligent Audit, blog on the 2026 Gartner Market Guide for FAP providers | 2026 | https://www.intelligentaudit.com/blog/intelligent-audit-gartner-2026 | full; vendor quoting Gartner, *assumed* | "shifting from manual review processes to AI-enabled automation"; "51% of enterprise shippers are already outsourcing with 28% more ..." |
| N-R06 | Loop, "Loop Raises $95M Series C to Scale Its AI Platform Across the Supply Chain" | 2026-04-17 | https://www.loop.com/article/loop-raises-95m-series-c-to-scale-its-ai-platform-across-the-supply-chain | full (the Business Wire copy returned 403); company release | $95M led by Valor; named customers; "Automate 99% of freight and parcel audits" (claim). The $210M total is from a search summary, *assumed* |
| N-R07 | Freehand, "Best Freight Claims Management Software 2026" | 2026 | https://www.freehand.ai/articles/best-freight-claims-management-software | full; vendor, *assumed* | 7 vendors with their pricing models (iNymbus about $0.40-0.70 a claim). Search results added FreightClaims.com, Claimable, VTM and TLI |
| N-R08 | Ladingly, home page | 2026 | https://www.ladingly.com/ | full; vendor, *assumed* | "20% contingency on recovered funds"; "Typical claims BPOs charge 25–30%"; "30–50% ... never get filed" |
| N-R09 | 49 CFR 370.3, Filing of claims (Cornell LII) | current | https://www.law.cornell.edu/cfr/text/49/370.3 | full section; *verified* | The written-claim requirement, its minimum contents, and the documents that are not sufficient alone |
| N-R10 | Adrian Gonzalez, Talking Logistics, "Catching Up on Transportation Management Systems" | 2023-11-27 | https://talkinglogistics.com/2023/11/27/catching-up-on-transportation-management-systems/ | full; secondary, *assumed* | Trimble paid $200M for Kuebix and later shut it down; Transporeon bought Dec 2022; questions on smaller shippers' TMS use; Kuebix now offered by FreightWise |
| N-R11 | Infios (Körber Supply Chain Software), "Körber Supply Chain Software completes acquisition of MercuryGate" | 2024-10-01 | https://www.infios.com/en/knowledge-center/news/koerber-supply-chain-software-completes-acquisition-of-mercurygate | full; *verified* (the acquirer's own release) | Completion date; MercuryGate serves shippers, 3PLs, brokers and carriers; adds about 25% to Körber's net revenue |
| N-R12 | WWEX Group, "Introducing WWEX Group" | 2023-10-02 | https://wwexgroup.com/press-room/introducing-wwex-group/ | full; company claim, *assumed* | "more than 121,000 customers"; 200 franchises, 500 agents; small-business and mid-market focus; 75+ LTL carriers |
| N-R13 | FMCSA, "Restoring Integrity to the Issuance of Non-Domiciled Commercial Drivers Licenses", final rule, FR Doc 2026-02965 (govinfo copy) | 2026-02-13 | https://www.govinfo.gov/content/pkg/FR-2026-02-13/html/2026-02965.htm | summary read; *verified* | Effective 2026-03-16; eligibility limited to H-2A, H-2B and E-2 holders; "more than 30 States have issued tens of thousands non-domiciled CDLs". No count of affected drivers |
| N-R14 | Perry D. Wiggins, CFO.com, "Metric of the Month: Accounts Payable Cost" (APQC data) | 2018-02-05 | https://www.cfo.com/news/metric-of-the-month-accounts-payable-cost/659393/ | full; *verified*, but dated | 1,485 organisations; per invoice: median $5.83, top quartile $2.07 or less, bottom quartile $10+; distribution and transportation $1.14 |
| N-R15 | Search results on driver-supply enforcement and 2026 rate forecasts: truckdispatchexperts.com, Breakthrough, Argon & Co, Transportation Insight (the FTR/CCJ article returned 403) | 2026 | https://truckdispatchexperts.com/resources/english-language-proficiency-enforcement-2026/ ; https://www.breakthroughfuel.com/blog/how-english-language-proficiency-enforcement-will-shape-the-2026-freight-market/ ; https://www.argonandco.com/us/news-insights/articles/2026-truckload-rate-outlook-where-do-we-go-from-here/ | snippets, *assumed* | 14,000+ drivers out of service for English proficiency since June 2025; 2026 contract rates +7.6% (dry van), spot +8.1%; the interim rule's date (2025-09-29) |
| N-R16 | Search results on LTL GRIs for 2025-26 (FreightWaves "LTL's paper gains"; Argon & Co LTL outlook; ODFL 2026 GRI release) | 2025-26 | https://www.freightwaves.com/news/ltls-paper-gains ; https://www.odfl.com/us/en/about/ODFL-news/ODFL-press-releases/2026-General-Rate-Increase.html | snippets, *assumed* | ODFL 4.9%; Saia, FedEx Freight and ABF 5.9% (late 2025); ArcBest 5.9% (June 2026) |
| N-R17 | FreightWaves, "Annual LTL GRIs slightly ahead of schedule" | 2023-11-13 | https://www.freightwaves.com/news/annual-ltl-gris-slightly-ahead-of-schedule | full; *verified* (trade press) | The 2023 GRI round (ODFL 4.9%, Saia 7.5%, ArcBest 5.9%, FedEx Freight 5.9-6.9%): evidence that GRIs come every year |
| N-R18 | NASSTRAC description (search results; the about page returned 403) | n/a | https://www.nasstrac.org/about/about-us/ | snippet, *assumed* | Members are shipper executives at manufacturers, retailers, wholesalers and distributors; hands out LTL carrier awards. No member count |
| N-R19 | Transportation & Logistics Council, home page; "Freight Claims in Plain English" seminar page | current | https://tlcouncil.org/ ; https://tlcouncil.org/freight-claims-in-plain-english-summer-webinar/ | home page full, seminar page snippet; *verified* self-description | A not-for-profit serving shippers; claims seminars and publications. No member count |
| N-R20 | ISM membership (search results: Wikipedia, ismworld.org) | n/a | https://en.wikipedia.org/wiki/Institute_for_Supply_Management | snippet, *assumed* | "over 50,000 members"; another source says "200,000+ professionals" |
| N-R21 | NetSuite SuiteApp listings: Freightgate, Shipwell, FreightPOP | current | https://www.suiteapp.com/FREE-Freightgate-For-Net-Suite ; https://www.suiteapp.com/Shipwell-TMS-for-NetSuite ; https://www.freightpop.com/netsuite-tms-partner | snippets, *assumed* | Freight apps with invoice audit exist in an ERP marketplace |
| N-R22 | LTL booking tools for small shippers: Freightview (Capterra), MyCarrier, FreightCenter, Freightquote, FreightPOP | current | https://www.capterra.com/p/136895/Freightview/ ; https://go.mycarrier.io/ ; https://www.freightcenter.com/ | snippets, *assumed* | Freightview from $149 a month; MyCarrier's "no broker markups" claim |
| N-R23 | Modern Materials Handling / Peerless, "2025 Software/Automation Outlook Survey" | 2025 | https://www.mmh.com/article/2025_software_automation_outlook_survey_wms_reigns_ai_rises | snippet (page returned 403), *assumed* | "35% of respondents currently are using TMS, up from 25% last year" (a warehouse and DC readership) |
| N-R24 | Explainer pages on the X12 210 and 214 (Cleo, Infocon) | current | https://www.cleo.com/edi-transactions/edi-210 ; https://www.infoconn.com/EDIDOCS/EDI214.htm | snippets, *assumed* | What the 210 (freight invoice) and 214 (status message) contain |
| N-R25 | Inbound freight vendor and 3PL pages: C.H. Robinson inbound guide, TLI vendor routing compliance, FreightPOP, BTX Global, Freightsuite, the Kuebix article in Inbound Logistics | 2024-26 | https://www.chrobinson.com/en-us/resources/resource-center/guides/inbound-logistics/ ; https://shiptli.com/managed-freight/vendor-routing-guide-compliance-and-inbound-logistics-management/ ; https://www.inboundlogistics.com/articles/its-time-to-make-inbound-freight-management-a-priority/ | snippets, *assumed* | Named inbound tools and programs; TMC took over routing-guide management for clients |
| N-R26 | NMFTA Digital Standards Development Council pages: eBOL API standard; pickup and visibility release | current | https://dsdc.nmfta.org/apis/ebol-api-standard ; https://nmfta.org/digital-ltl-council-releases-new-api-standards-for-pickup-requests-and-visibility/ | eBOL page full, release snippet; *verified* that the standards exist | eBOL at version 2.1; pickup, visibility and PFC standards. No adopter list |

### 4.2 Earlier sources re-read here

| ID | What was re-read (2026-09-15) |
|---|---|
| N-D30 | The Cass FY2025 10-K, downloaded from EDGAR and searched. New quotes: serves "large manufacturing, distribution and retail enterprises"; per-item fees and discounts from carriers; the AI obsolescence risk; small carriers were the larger users of quick pay |
| N-D31 | U.S. Bank Freight Payment Index, Q2 2026: shipments -2.8% and spend +28.1% year on year; "trucking capacity continues to tighten" |
| N-F28 | The Descartes/SAPIO 2025 release: 616 respondents; 17% fully automated; 80% plan more TMS spending; AI use cases |
| N-F46 | Freehand, "Best Freight Procurement Software" (a snippet in S1), now read in full: 12 vendors, the main 7 tagged "Enterprise" |
| N-K21 | CorePiper's 2026 claims report, re-read: 28% of mid-market shippers use claims software, under 8% use AI; filing, denial and recovery rates |
| N-F22 | BLS OEWS May 2025 via API v2, extended with new series: SOC 13-1020, 11-3061, 13-1031, 43-3021 nationally, and 13-1081, 43-3031, 43-5071, 11-3071, 13-1020, 11-3061 for industries 31-33 (code "31--34") and 42 ("42--43"); data types 01 (employment) and 04 (mean annual wage) |

**Also cited without re-reading:** R22, R23, R27, R28, R30, R33, R34; N-A25, N-A26, N-A30, N-A32; N-C15; N-D32, N-D33; N-E20, N-E22, N-E23, N-E27, N-E28, N-E31; N-F03, N-F14, N-F17, N-F29, N-F35, N-F36, N-F41, N-F44, N-F50, N-F51, N-F56; N-G20 to N-G24, N-G44; N-K28.

---

## 5. Could not access, or not found

**Blocked pages (HTTP 403):**
- the Gartner Market Guide page (document 5678155) and the Gartner Peer Insights FAP list, so the guide's vendor list was not seen;
- the Business Wire copy of Loop's release (the loop.com copy was used instead);
- the CCJ/FTR capacity article;
- the FMCSA fact sheet PDF and the FMCSA rule page (the govinfo copy was used instead);
- the NASSTRAC about page;
- the MMH/Peerless 2025 survey page.

**Searched but not found:**
- **Neutral data on mid-sized shippers' TMS, FAP or claims software use.** Tried: a TMS-adoption search, the Descartes release, the Peerless survey, and the Gartner FAP guide. Only vendor or dated figures exist.
- **Market shares of FAP, claims, LTL or procurement vendors.** Tried: Gartner (blocked), vendor lists, and Cass's filing (which gives no shares).
- **A neutral inbound routing-guide or overpay rate (C-17).** Three attempts: scan E, check N's MIT search, and a new search this time. Only vendor snippets.
- **A neutral claims contingency rate (C-10).** Two searches. Only vendor claims (Ladingly; "typical ... 25–30%").
- **Carriers' adoption of the NMFTA APIs** (PFC, eBOL, pickup). Tried: NMFTA's news post, the DSDC eBOL page, and a search. No adopter counts.
- **The number of drivers affected by the non-domiciled CDL rule.** The final rule gives none. The "about 194,000" figure was searched for and not found at a primary source.
- **Member counts** for NITL, NASSTRAC and TLC. Their about pages do not state them, or were blocked.
- **The Kuebix shutdown.** Only secondary sources (N-R10); no Trimble statement was found.
