# S4 check AD: C-11's money, from real documents (LTL class, reweigh and reclass disputes)

- **What this is:** new desk research for **S4 step 7 (C22)** in run 01, for card **C-11: LTL class, reweigh and reclass disputes, for small manufacturers and distributors**. It supplies inputs for the per-customer profit model and kill condition that the coordinator will build:

  > fee per customer = LTL spend × corrections as % of spend × share of corrections that are wrong and winnable × share actually credited × fee share
  > gross profit = fee − cost to serve (minutes per shipment checked and per dispute × loaded wage + fixed cost)

  It answers AD1-AD7 from the brief, in that order (§2-§8).
- **Date:** 2026-09-22. Everything new here was accessed on 2026-09-22.
- **Status:** input to S4 step 7. **It decides nothing.** It sets no price, picks no segment, re-scores nothing and does not write the kill condition. Every reading is **[our call]** and sits in §9.
- **Labels:**
  - *verified*: read at the source (court PDF, filing, government data, carrier tariff), with page or line given. A court complaint is *verified* **as what the complaint alleges**; allegations are not findings.
  - *assumed*: a vendor claim (always, even on the vendor's own page), a search snippet, a secondary summary, a blocked page, memory.
  - **[our calc]** = our arithmetic, shown. **[our call]** = our judgement.
  - **OCR:** one court exhibit (N-AD07) is a scanned image. We read it with open-source OCR (optical character recognition: software that turns a picture of text into text). OCR misreads some digits; counts from it carry that caveat.
- **New source IDs:** N-AD01 to N-AD41 (§10). Earlier IDs keep their meaning (N-T01-N-T50, N-X26, N-X29-N-X31, N-AA31-N-AA40, N-AB35, N-AB37, N-AB38).
- **Not redone here (cited by ID only):** check T's nine rules tariffs, windows and proof rules, the FedEx Freight dimensioner figure (N-T36), the NCWM letters (N-T32-N-T35); check AB's FedEx Freight revenue-adjustment figures (N-AB37) and the 10th Circuit *Southern Furniture* opinion (N-AB35); check AA's minutes per invoice and wages for bookkeeping and billing clerks (N-AA31-N-AA40); check X's contingency shares and SMB tool prices (N-X26-N-X31) and its freight-share-of-sales table (§7.2). **The 101 ABF Freight invoices from *In re IN Holdings* are the coordinator's and were not touched.**
- **Downloads** (court PDFs, filings, the OCR text) are in the session scratchpad (`…/scratchpad/c11/`), not in the project folder.

**Words used here:**
- **LTL (less than truckload):** freight from many shippers shares one trailer. The price is set per 100 lb (a **hundredweight**, "cwt") by **class**, weight band and lane, then a **discount** is taken off, then a **fuel surcharge** is added as a percentage.
- **Class:** one of 18 NMFC price levels (50 to 500). The **NMFC** (National Motor Freight Classification) is run by **NMFTA** (National Motor Freight Traffic Association), a carriers' body. Higher class = higher price per cwt.
- **BOL (bill of lading):** the shipping paper the shipper fills in at pickup, with its declared weight, description and class.
- **Correction (re-rate):** the carrier changes the bill after pickup. **Reweigh** = it weighs the freight and finds a different weight. **Reclass / inspection** = it re-describes the freight or re-measures it and applies a different class. **Dimensioner** = a machine that measures a pallet's size automatically, used for density-based class. Each correction usually adds a **fee** of $15-55 (check T §3.1) on top of the re-rated charge.
- **W&I / W&R certificate:** the carrier's weight-and-inspection (or weight-and-research) record of a correction.
- **Positive / negative correction:** a correction that raises / lowers the bill (heavier / lighter than declared).
- **Collect / prepaid:** who pays the carrier: the consignee (receiver) or the shipper.
- **SOFA (Statement of Financial Affairs, Official Form 207):** a sworn form every business bankruptcy debtor files. **Part 1** gives gross revenue; **Part 2 item 3** lists payments to creditors in the **90 days** before filing. Payments to one creditor that total less than a threshold ($6,425 in 2016-19, $6,825 in 2019-22, $7,575 in 2022-25, $8,575 from April 2025) may be left out, so small carriers can be missing.
- **Schedule E/F:** the debtor's list of unpaid creditors and what it owes each on the filing day.
- **3PL:** third-party logistics firm (a broker or reseller that books LTL for a shipper, often on the 3PL's own carrier contract).
- **Qui tam / False Claims Act:** a whistleblower suit on the government's behalf over false bills to the government; the Department of Justice (DOJ) may take it over ("intervene").

---

## 1. Summary inputs table

Low / central / high are the spread of what was found. **A "central" value is always [our call]**, not a measurement, unless the label says otherwise.

| Input | Low | Central | High | Label | Source IDs |
|---|---|---|---|---|---|
| **Share of LTL shipments that get a correction** | **5.0%** (Yellow, positive reweighs only, 13 Nov 2006-20 Jan 2007: 75,324 of "more than 1.5 million invoices") | ~15% **[our call]** | **~28%** (UPS Freight bills in a disputed, unpaid set: 48 of 169 legible bills) | Yellow: *verified* as the DOJ complaint's text; UPS set: *verified* bills, count **[our calc]** via OCR, **biased upward**; central **[our call]** | N-AD01, N-AD07 |
| Same, carrier or vendor claims | "as many as 25 percent" of named shippers' shipments before they bought a dimensioner; "one percent" after | — | — | *assumed* (carrier marketing quoting shippers) | N-AD27, N-AD28 |
| **$ added per correction** (re-rate + fee) | $15-55 (fee only; check T) | **$72** on one real 2008 UPS Freight bill (172 → 225 lb, class 100): +41% on the bill, $18 of it the fee | $145 (vendor's hypothetical reclass average) | fee *verified* (N-T17-N-T30); $72 **[our calc]** from a *verified* bill; $145 *assumed* | N-AD07, N-X26 |
| Fees printed on real corrected bills | UPS Freight 2008-10: **$18.00-$26.00** per reweighed bill | — | 2025-26 tariffs: $15 (SEFL) to $55 (ABF) | *verified* | N-AD07; check T |
| **Corrections as % of LTL spend** | **0.8%** of revenue (FedEx Freight: dimensioners added "over $150 million" over FY2024-25) | ~2% **[our call]** | **~5%** (28% of shipments × $72 on a $384 average bill) **[our calc]** | FedEx *verified* (N-T36); others **[our calc]** | N-T36, N-AD07 |
| Value of the *downward* corrections a carrier withheld | **0.18%** of revenue (Yellow, "$500,000 per month") | — | **0.36-0.54%** (Roadway, "$1 to $1.5 million in revenue per month") | complaint text *verified*; % **[our calc]** on 10-K revenue | N-AD01, N-AD08 |
| **Share of corrections that are wrong and winnable** | 10% **[our call]** | 25% **[our call]** | 50% **[our call]** | **Placeholders: not measured anywhere.** SJ Consulting's survey (*assumed*, primary not found): billing accuracy 94-99%, average 97%; about half of BOLs wrong on weight or description, so most corrections are the shipper's own error | known (brief); §3 |
| Direction of real weight corrections | UPS Freight 2008-10: of ~29 legible weight pairs, **22 up, 7 down** | — | Yellow 2006-07: 75,324 up, **42 down** (downward corrections deliberately suppressed) | *verified* bills / complaint text; counts **[our calc]** | N-AD07, N-AD01 |
| **Share credited when disputed** | 41-51% (claims aged, check AB) | 60-90% (disputed promptly, check AB) | 70-82% "with BOL + reweigh tickets" — **traced: a vendor's hypothetical**, not a measurement | all *assumed* | N-AB27, N-X26, N-AD29 |
| **LTL spend per small shipper (real bankruptcy filings)** | ~$31k a year (plastics molder, $6.4M revenue) | **median ~$94k a year** across 9 firms **[our calc]** | ~$389k a year (bicycle distributor, $14.3M revenue) | payments *verified*; annualised **[our calc]** | N-AD14-N-AD22 |
| Same, as % of the firm's revenue | 0.2% | **median ~0.7%** | 4.6% | **[our calc]** | N-AD14-N-AD22 |
| Average LTL revenue per carrier customer | **$64k** (FedEx Freight, excluding its top 25 customers) | $81k (FedEx Freight, all 108,000 active customers) | $147k (XPO, all segments, 55,000 customers) | inputs *verified*; averages **[our calc]** | N-AD11, N-AD12 |
| **Shipments (invoices) per $1,000 of LTL spend** | 2.2 (coordinator's ABF set, not redone) | **~2.6-2.9** (UPS set 2.61; Saia 2.88; FedEx Freight 2.55) **[our calc]** | 3.2 (industry: $52.8B over ~169M shipments) **[our calc]** | inputs *verified* | N-AD07, N-AD09, N-T36 |
| **Minutes per shipment checked** | — | 8-13 min for a full manual audit (vendor figures, check AA) | — | *assumed* | N-AA31, N-AA32, N-AA35 |
| **Minutes per dispute** | **not found** (check AA's 5 / 15 / 45 are [our call]) | — | Elapsed time: "between two weeks and two months" (FreightPros 2014); Estes 24-48 h (carrier claim) | *assumed* | N-AD34; check T |
| **Wages (BLS OEWS May 2025, mean hourly)** | 43-5071 shipping, receiving and inventory clerks **$22.50** (loaded $32.14) | 43-3021 billing and posting clerks $24.55 (loaded $35.07) | 43-3031 bookkeeping clerks $25.75 (loaded $36.79) | *verified*; loaded = wage ÷ 0.70 **[our calc]** | N-AD24, N-AA39, N-AA40 |
| **Prices charged today** | 3PL-bundled: LTLflow (Pinnacle) $0 free tier; a $3,400 handheld dimensioner "$0/month" at qualifying volume | Tools: $60-200/month (MyCarrier), $149/month (Freightview), $200-300/month (LTLflow Pro/Scale) | Contingency 25-50% of recoveries (general audit); LTLflow Enterprise $1,300/month + $7,000 dimensioner | prices *verified* as stated; contingency *assumed* | N-AD30, N-X29-N-X31; check X §5.1 |
| Shipper-side dimensioner (the prevention substitute) | $3,400 (handheld, retail value) | "$35,000-plus" (overhead) | $65-100k (laser, snippet) | $3,400 *verified* as stated; others *assumed* | N-AD30, N-T43, N-AD38 |
| **Prevention saving per corrected shipment** | the correction fee only, **$15-55**, when the carrier was right | fee + one class step: **+7-9%** of linehaul per class step (class 50-110) | fee + a penalty class: class 150 costs **~2×** class 70 (XPO bills improper descriptions at 150) | class table *verified* (2008 article); ratios **[our calc]** | N-AD31; check T §3.2 |
| **US LTL market** | 2025: **$51.8B** | 2024: **$52.8B**; **669,545** shipments a day | — | *verified* (SJ Consulting tables) | N-AD09, N-AD10 |
| Industry correction money **[our calc]** | fees alone: 5% of ~169M shipments × $15 = **~$127M** | 0.8% of $52.8B = **~$420M** (FedEx's dimensioner rate applied to all) | fees at 5% × $55 = ~$464M; or 5% of spend = ~$2.6B | **[our calc]** | N-AD09, N-T36 |
| Number of US LTL shippers; spend distribution | **not found.** Largest carrier: 108,000 active customers. A 3PL group serving SMBs: 130,000+ customers (all modes) | — | — | FedEx *verified*; 3PL *assumed* | N-AD11, N-AD36 |

**One-line reading [our call]:** real documents put corrections at roughly **5% of shipments at a 2006 carrier that reweighed selectively, and up to about a quarter of shipments for shippers whose paperwork is wrong**; a correction adds **tens of dollars, not hundreds**, on a small shipper's bill; and **real small manufacturers and distributors in bankruptcy files bought only about $30k-$390k of LTL a year (median ~$94k)**. Nobody has measured how many corrections are wrong.

---

## 2. AD1 · How often, and how many dollars: real documents

### 2.1 The Yellow and Roadway reweigh case (DOJ, W.D.N.Y.)

*United States ex rel. Hannum v. Roadway Express, Inc., Yellow Transportation, Inc., YRC Freight, Inc.*, W.D.N.Y. No. 1:08-cv-00811. The relator (a 30-year Roadway/YRC employee) filed in 2008; DOJ intervened in December 2018. Everything below is **what the United States alleges, quoting the carriers' internal emails** (*verified* as the complaint's text; not findings). The case settled in 2022 for about $6.85M (check T, N-T40, snippet).

| What | Quote and location | Number we take | Label |
|---|---|---|---|
| **Share of invoices with a positive reweigh** | "out of more than 1.5 million invoices between November 13, 2006, and January 20, 2007, Yellow made 42 negative reweigh corrections. In contrast, Yellow made 75,324 positive reweigh corrections during the same period" (Doc 72, ¶73, p. 18) | **75,324 ÷ 1,500,000 = 5.0%** of invoices raised by a reweigh in ~10 weeks; downward corrections **0.003%** **[our calc]** | *verified*, N-AD01 |
| Value of the downward corrections Roadway stopped crediting | elimination "was estimated to save Roadway $1 to $1.5 million in revenue per month by avoiding reduced charges to customers" (¶54, p. 13); "Roadway ... was retaining about $1.5 million per month" (¶61, p. 15) | Against Roadway's 2005 revenue of $3,321.1M ($276.8M a month): **0.36-0.54% of revenue** **[our calc]** | complaint *verified*; revenue *verified* via fetch tool (N-AD08) |
| Same, Yellow | stopping them would let Yellow "retain approximately $6 million per year ($500k per month)" (¶57, p. 14); work request: "add [about] $500,000 per month to top and bottom line (revenue and profit)" (¶65, p. 16) | Against Yellow's 2005 revenue of $3,421.3M ($285.1M a month): **0.18%** **[our calc]** | as above |
| Size of a "best practice" correction programme | the Defendants "could see $10-20 million in annualized revenue from a best practice weight correction program" (¶61, p. 15) | On combined 2005 revenue of $6,742M: **0.15-0.30%** of revenue, incremental **[our calc]** | as above |
| Effect of better scales | new procedures "caused a surge in reweigh corrections 'that turned into a 50% increase in revenue'" (¶50, p. 12); Yellow "spent approximately $2 million on new scales in 2007" and demanded terminals "realize the expected revenue increase" (¶70, p. 17) | Reweigh revenue rises with equipment | *verified* |
| Size of downward corrections | to halve negative corrections the carriers would have had to ignore weight changes under "70%", or set a dollar tolerance of "negative $800, meaning that a weight drop that reduced revenue by $799 or less for a shipment would not be disclosed" (¶59, pp. 14-15) | Downward corrections were often large (government shipments with estimated weights) | *verified* |
| Industry practice then | in 2005 "only two other freight companies were not 'entering negative weight corrections'" (¶63); in 2007 "all twelve companies that responded confirmed that they made negative reweigh corrections" (¶74) | Two-way correction was the norm | *verified* |
| Government shipments | "approximately 725 false claims per month" (June 2010-Oct 2012), "more than 13,000"; extrapolated "approximately 70,000" for Sept 2005-Oct 2013 (¶88-89, p. 21) | One customer (DOD): ~725 un-credited downward reweighs a month | *verified* |
| Real government bills (relator, 2008) | 4,310 lb declared, 3,345 lb on Roadway's scale: "overcharge of approximately $222.84"; 620 lb declared, 220 lb on the scale: "approximately $133.23" (Doc 1, ¶31-32, p. 8). Both carriers "automatically disregard minor weight corrections — both upward and downward — if they are less than about 30-40 pounds" (fn. 1, p. 7) | $133-223 per un-credited downward reweigh | *verified*, N-AD03 |
| Exhibit A: 200 DOD bills | e.g., actual 140 lb billed at 6,000 lb (−98%); 1,410 lb billed at 2,973 lb (−53%) (Doc 72-1, p. 2) | Government estimates; not a guide to private shippers | *verified*, N-AD02 |

### 2.2 The *Southern Furniture* class complaint (D. Kan., 2019)

*Southern Furniture Leasing, Inc. v. YRC, Inc.*, D. Kan. No. 2:19-cv-02129, Doc 1 (N-AD04). The plaintiff "is a small business in Tallahassee, Florida that rents furniture" (¶2). *Verified* as the complaint's allegations:
- YRC "in 2018 alone ... made over ten million shipments from which it recognized more than five billion dollars in revenue" (¶2). That is about **$500 per shipment** **[our calc]**.
- "YRC overcharged customers between $1 million and $1.5 million a month" (¶35), repeating the DOJ figure.
- Amount in controversy: "more than $45,000,000 at issue" (fn. 1, p. 3), class of "thousands of small businesses" (¶7).
- **The complaint gives no count of the plaintiff's own shipments, no invoice and no per-shipment dollar figure.** It was dismissed as time-barred; the 10th Circuit affirmed in 2021 (N-AB35).

### 2.3 The YRC securities complaint: what former staff said (N.D.N.Y., 2019)

*Lewis v. YRC Worldwide Inc.*, N.D.N.Y. No. 1:19-cv-00001, Doc 75 (amended complaint, 141 pp.; N-AD05). Confidential witnesses (CW) are former YRC weight-and-inspection staff. *Verified* as allegations:
- **Dispute volume at one terminal:** at Chicago Heights, customers "protested" invoices "at least 10 times a day"; the directive on weight protests was "stay your ground, [and] unless the evidence is overwhelming," do not credit (¶148, p. 43).
- **Incentives:** forklift operators got "$25 gift cards to Home Depot for every 30 reweighs achieved" (¶149).
- **Make-up codes:** when a customer won a weight or class credit, YRC kept "cheat codes" to "make-up the [revenue] loss another way" (CW 2, ¶134, p. 35).
- **Target list:** YRC "targeted certain customers which YRC knew would not identify or dispute invoices" (CW 6, ¶167).
- **Carrier-side reserve:** YRC's 10-K (quoted at Doc 1, ¶17): "the majority of rerating occurs in the same month as the original rating"; rerate reserve "$9.6 million and $11.9 million" at end-2013 and 2012. On YRC's roughly $4.9B of 2013 revenue (*assumed*, memory) that is about **0.2%** held back for later re-rates **[our calc]**.

### 2.4 A real set of LTL bills with reweighs: UPS Freight bills in the Delphi bankruptcy (2008-2010)

**Document (N-AD06, N-AD07):** *In re Delphi Corp.*, Bankr. S.D.N.Y. No. 05-44481. UPS answered Delphi's 47th omnibus claims objection (Doc 20038, 2010-05-12) with a declaration and **Exhibit A, "Delphi Open Invoices as of 4/30/10": 195 UPS Freight invoices dated 2008-01-15 to 2010-04-22, total $74,852.89, balance $74,758.98** (*verified*, parsed from the PDF). Exhibit B (Docs 20040 and 20041, 425 pages) holds copies of the freight bills, BOLs and delivery receipts. We read 855 PDF pages: two parts have a text layer, seven are scans we OCR'd.

**Who shipped:** mostly suppliers shipping inbound to Delphi plants (e.g., "DAWSON MFG" of Benton Harbor, MI, spring seats; "INTERMET", aluminium castings; "FUTABA"), billed to "DELPHI CORP". So the declared weights are **the suppliers' own**, many of them small manufacturers.

**Counts [our calc, OCR]:**

| Measure | Value |
|---|---|
| Invoices whose freight-bill copy we could match to exactly one open invoice (by PRO number or unique amount) | **169** of 195, $67,799.70 |
| …of which the bill prints "SHIPMENT REWEIGHED" / "WEIGHT DECLARED AS … ACTUAL WEIGHT IS …" | **48 (28%)**, carrying $27,460.04 of billed value (40%) |
| …of which the bill mentions an inspection | 4 |
| Legible declared/actual weight pairs | ~29 after dropping 3 garbled pairs: **22 up, 7 down** |
| Upward corrections: median weight increase | **+26% (+85 lb)**; mean +44% (22 bills) |
| "REWEIGH FEE" printed | $18.00 (15 bills), $19.00 (5), $18.60, $19.06, $19.09, $20.00, $26.00 |
| Average invoice | $74,852.89 ÷ 195 = **$383.86**, i.e. **2.61 invoices per $1,000** |

**Two strong biases, so do not read 28% as a rate [our call]:** these are the invoices Delphi **did not pay** and objected to in court, so disputed bills (and reweighed bills are a prime cause of disputes) are over-represented; and OCR can miss or mis-read lines in both directions.

**Worked bill (text layer, no OCR):** freight bill 174087550, 2008-11-17, Dawson Mfg (Benton Harbor, MI) to Delphi (El Paso, TX), one skid, "SPRING SEAT 225 … 100 242.33 545.23", "65.00% DISCOUNT", "LTL FUEL ADJUSTMENT 20.30 38.74", "REWEIGH FEE 18.00", "WEIGHT DECLARED AS 00172 LBS. ACTUAL WEIGHT IS 00225 LBS.", "AMOUNT DUE 247.57" (Doc 20040-1, p. 50; the text layer prints the discount as −351.41, but the bill only adds up at 65% = −354.40).

| Step | At the declared 172 lb **[our calc]** | As billed at 225 lb (*verified*) |
|---|---|---|
| Gross linehaul at class 100, $242.33/cwt | $416.81 | $545.23 |
| After 65% discount | $145.88 | $190.83 |
| Fuel 20.30% | $29.61 | $38.74 |
| Reweigh fee | — | $18.00 |
| **Total** | **$175.50** | **$247.57** |

**The correction added $72.07: $54.07 of re-rated linehaul and fuel plus the $18 fee, +41% on the bill.** The shipper's declared 172 lb looks simply wrong (the same 172 → 225 lb pair appears on a second Dawson bill, 174078752, $145.72): a legitimate correction, where only the $18 fee was avoidable [our call].

### 2.5 Carrier filings and trade press (numbers only; mostly already in check T)

| Figure | Source | Label |
|---|---|---|
| FedEx Freight: dimensioners on "over 90%" of shipments; "over $150 million of total incremental revenue over fiscal years 2024 and 2025" ≈ 0.8% of revenue, ≈ $3.30 a shipment | N-T36 (not redone) | *verified* |
| Triangulation: if $75M a year came from corrected shipments averaging $72 each, that is ~1.04M corrected shipments of ~22.7M, **~4.6%** | **[our calc]**, rough: DIM revenue also includes pricing effects, and $72 is one 2008 bill | **[our call]** |
| Saia "dimension 75 percent of our freight" (N-T37); SMC3: "a twenty to twenty-five dollar fee for rerating"; dimensioners "$35,000-plus" (N-T43) | check T; SMC3 re-read today | *verified* / *assumed* |
| ODFL's own page quotes shippers: "As much as 25 percent of our shipments were coming back with a re-weigh or re-classification" (Bestorq, industrial supplier); "Around 25 percent of our shipments had excessive length, incorrect weight, or incorrect classification" (Douglas Dynamics); after a dimensioner "our re-rates based on weight and length immediately dropped to one percent"; "Some shippers report 25 to 30 percent of their freight being re-rated" | ODFL "OD Outlook" page (undated) and the same text as sponsored content on FreightWaves (2026-04-29) | *assumed* (carrier marketing), N-AD27, N-AD28 |
| Search summaries with no traceable page: "Carriers issue weight and inspection adjustments on 5 to 10 percent of bills"; "15-25% of LTL shipments receive carrier adjustments, costing shippers an average of $125-300 per incident" | snippets | *assumed*, N-AD39 |

### 2.6 What AD1's goal numbers come to

- **(a) Share of shipments corrected:** 5.0% (Yellow reweighs only, 2006-07, *verified* allegation) to ~25-28% (shippers with bad paperwork, *assumed*; a biased real set, *verified*). The modern industry has more dimensioners than Yellow had scales in 2006, so 5% is a floor [our call].
- **(b) $ added per correction:** $72 on one real bill (+41%); fees $15-55; vendor averages $125-300 (*assumed*).
- **(c) Corrections as % of LTL spend:** 0.8% (FedEx dimensioners, all pricing effects) is the only filed figure. **Downward corrections a carrier withheld were worth 0.18-0.54% of revenue** at Yellow and Roadway.

---

## 3. AD2 · How many corrections are wrong, and how many disputes win

**Plainly: no neutral measurement of the share of corrections that are wrong, or of dispute win rates, was found.** What exists:

| Evidence | What it shows | Label |
|---|---|---|
| **SJ Consulting survey** (large shippers, 3PLs, audit firms; about 2016): billing accuracy 94-99% by carrier, average 97%; about 50% of BOLs wrong on weight or description; "what shippers perceive as a billing error actually is due to shippers providing an estimated weight or freight class" | Most corrections are legitimate. **The primary survey was not found** on jindel.com, in its published data lists, or in trade press (a 2010 Transport Topics article with Jindel quotes covers only billing costs: "$1" per paper bill; LTL carriers "fill out about 85% of their freight bills on paper") | *assumed*; N-AD35 |
| **Yellow/Roadway, 2005-2013** | A whole class of wrong bills: downward reweighs **not credited**, worth 0.18-0.54% of revenue (§2.1). Carriers **expected to concede when challenged**: if they had to have "the 'tolerance conversation' with the customer, then we're probably going to end up waiving it anyway" (Rawson, ¶60); exceptions were granted to customers told "YRC was cheating them" (¶76) | complaint *verified* |
| **UPS Freight, 2008-10** | About **1 in 4 legible weight corrections went down** (7 of ~29), and the $18 fee was still printed on at least two downward ones (e.g., 600 → 535 lb, bill 450288086) | *verified* bills; **[our calc]** OCR |
| **YRC staff statements** | "at least 10 times a day" protests at one terminal; credit only if "the evidence is overwhelming" | *verified* as allegations (N-AD05) |
| **Named shippers via ODFL** | ~25% re-rated with bad paperwork; ~1% after measuring at the dock: **the re-rates were mostly the shippers' own errors** | *assumed* |
| **The "70-82% recovery with BOL + reweigh" claim (check T could not trace it)** | **Traced:** it is EA Eller Audit's **worked example** of a hypothetical "US mid-market manufacturer [that] moves 32,000 LTL shipments per year ... Annual LTL spend: $12M": "roughly 4–6% of shipments touch a reclass dispute, with an average overcharge of $145 per affected shipment ... Recovery rate 70–82% with BOL + reweigh tickets + inspection records in hand" (page dated 2026-06-03). It is **not a measurement**. A second hit, Evos (2026-07-20), uses "82%" and "70%" for its own AI's "decision accuracy" and "end to end" clearance, not recoveries | *assumed* (vendor); N-AD29 (trace of N-X26), N-AD26 (Evos) |
| Vendor dispute success claims | "60–70% with proper documentation" (reweigh, with a calibration certificate); "70% of the time" when the shipper's math was right | *assumed*, snippets (N-AD39) |
| NMFTA, carriers to NCWM | "evidence of any pattern or practice of such errors is lacking" (NMFTA); ABF: disputes "most often resolved internally" | check T (N-T33, N-T34) |

**Reading [our call]:** the documents show two different "wrong" pools. (1) **Carrier-side errors** (a correction that should not have happened, or a downward one not credited): real, documented at one carrier as a policy, but of the order of a few tenths of a percent of revenue. (2) **Shipper-side errors** (the carrier was right): by far the larger share of corrections, on every source that speaks to it. **Only pool (1) can be disputed and won; only pool (2) can be prevented.**

---

## 4. AD3 · How much LTL does one small shipper buy

### 4.1 Real bankruptcy filings (SOFA Part 2 item 3: payments in the 90 days before filing)

Found through CourtListener's RECAP archive (free public court PDFs): ~90 filings that name an LTL carrier in a SOFA were screened; these 9 are manufacturers or distributors with legible payments. "LTL paid in 90 days" sums payments to asset-based LTL carriers only (*verified* from the filing). **Annualised = 90-day total × 4.06** (365 ÷ 90) **[our calc]**. Distressed firms pay irregularly, so this is rough in both directions.

| # | Firm (court, filed) | What it does (NAICS code from the petition, where given) | Revenue (SOFA Part 1) | LTL carriers paid in the 90 days | LTL paid in 90 days | **Annualised [our calc]** | % of revenue **[our calc]** | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | **Cycle Force Group, LLC** (Bankr. S.D. Iowa 21-00571, 2021-04-22) | Bicycle and accessory distributor (4239, durable-goods wholesale) | 2020: $14,349,516 | Central Transport $46,009.50; Estes $22,906.60; ArcBest $17,859.64; XPO $9,059.65 ("1/21-4/21") | **$95,835.39** (+ Freightquote, a 3PL, $12,968.89; UPS parcel $215,413.49) | **~$389k** | **2.7%** | N-AD14 |
| 2 | **Spokane Industries, LLC** (Bankr. E.D. Wash. 26-00116, 2026-01-23) | Steel castings (3311) | 2025: $20,922,485 | "SAIA LTL Freight … $33,000.00"; **Saia also owed $125,992.17** (listed top creditor, "Services") | $33,000 | **≥$134k** (arrears suggest more) | ≥0.6% | N-AD15 |
| 3 | **Imperial Toy LLC** (Bankr. N.D. Cal. 19-52335, Doc 75, 2019-12-09) | Toy maker and importer | 2018: $76,466,793 | ABF Freight: 7 payments, $3,343.48-$6,231.72 each | **$40,757.85** (ABF only; also MODE Transportation, a 3PL, $121,609.12) | **~$165k** | ≥0.2% | N-AD16 |
| 4 | **Sona BLW Precision Forge, Inc.** (Bankr. E.D.N.C. 16-04336, Doc 62, 2016-09-02) | Forgings (fabricated metal) | 2015: $8,200,689 | FedEx Freight East $2,878.18; "HOLLAND (HMES)" $2,677.66 (probably the LTL carrier); SEFL $1,694.15; XPO $315.15; R&L $253.58; ODFL $110.58. **Exhibit A lists every vendor payment, not only those above the threshold** | **$7,929.30** (truckload and expedite far larger: Bolt Express $68,030.77, Landstar $25,116, TQL $20,335) | **~$32k** | 0.4% | N-AD17 |
| 5 | **Old World Timber, LLC** (Bankr. E.D. Ky. 21-51160, 2021-10-19) | Reclaimed-wood products (3219) | 2021 to filing: $4,446,980 (~$5.6M a year) | Estes $10,608.60; Saia $12,570.01 ("8/4/21 - 9/23/21") | **$23,178.61** | **~$94k** | 1.7% | N-AD18 |
| 6 | **Electric Bike Company, LLC** (Bankr. C.D. Cal. 8:25-bk-12810, 2025-10-03) | E-bike maker | 2024: $9,512,898 | Estes $14,000.00 (June 2025); R&L $11,706.15 (July 2025). ODFL and Estes collection suits pending | $25,706.15 (these look like **collection settlements**, i.e. old bills) | ~$104k (equivalent) | ~1.1% | N-AD19 |
| 7 | **Instaset Plastics Company, LLC** (Bankr. E.D. Mich. 22-47794, 2022-10-05) | Plastic moulding | 2022 to filing: $4,937,544 (~$6.4M a year) | Dayton Freight: "2,775 2,782 2,172 7,729" (July-Sept 2022) | **$7,729** | **~$31k** | 0.5% | N-AD20 |
| 8 | **Loadcraft Industries, Ltd.** (Bankr. W.D. Tex. 21-11018, petition 2021-12-30; Doc 53) | Equipment manufacturer | 2020: $4,339,504 | FedEx Freight East $7,969.20 ("between 10/6/21 and 12/27/21"); **also owed $6,103.70** | $7,969.20 | **~$32k** (≈$57k with arrears) | 0.7% | N-AD21 |
| 9 | **Novalent, Ltd.** (Bankr. E.D.N.C. 24-02756, 2024-08-16) | Small chemical maker (3251) | 2023: $1,073,105 | Estes $12,289.00 ("various") | $12,289 | **~$50k** | 4.6% | N-AD22 |

**Distribution [our calc]:** annualised LTL-carrier spend, sorted: $31k, $32k, $32k, $50k, **$94k (median)**, $104k, ≥$134k, ≥$165k, $389k. As a share of revenue: 0.2% to 4.6%, **median ~0.7%**.

**Also seen (arrears, not spend):** Hamilton Scientific LLC (laboratory furniture maker; Bankr. D. Del. 17-10655) owed **Con-way Freight $179,781.95** on its Schedule F, next to small balances at ABF ($560.00), Estes ($1,157.17), ODFL ($591.11), Saia ($58.62), YRC ($1,279.34 + $176.36) (N-AD23, *verified*). One main LTL carrier and many small ones is the pattern in several filings.

**Caveats [our call]:** (a) SOFA thresholds hide carriers paid less than ~$6-8k in 90 days, so totals can be low; (b) LTL booked through a 3PL shows up under the 3PL's name (Freightquote, MODE); (c) much outbound freight of small suppliers is **collect** (the customer pays; the Delphi bills in §2.4 are an example), so it never appears in the supplier's books; (d) firms in distress ship less.

### 4.2 Carrier customer counts (10-Ks)

| Carrier | Customers and concentration (quote) | Revenue | Average per customer **[our calc]** | Label |
|---|---|---|---|---|
| **FedEx Freight** (FY ended 2026-05-31) | "We provide services to approximately 108,000 active customers across a broad range of sizes, end-markets, and geographies." "In 2026, our top five and top 25 customers accounted for just 9% and 21% of our revenue ... Our largest customer accounted for approximately 4%" | $8,795M (N-AB37) | **$81k**; the other ~107,975 customers average **$64k** | *verified* (fetch-tool extraction of the 10-K), N-AD11. A search snippet said "140,000"; the filing text read says 108,000 |
| **XPO** (2024) | "approximately 38,000 employees serving approximately 55,000 customers" (whole company, incl. Europe); North American LTL: "top five customers combined accounted for approximately 10% of revenue, with the largest customer accounting for less than 4%" | $8,072M total; NA LTL $4,899M | $147k (company-wide, mixed) | *verified*, N-AD12 |
| **Old Dominion** (2024; 2025) | "our largest customer accounted for approximately 5.3% of our revenue and our largest 5, 10 and 20 customers accounted for 14.7%, 21.5% and 31.1%" (2024); 4%, 11%, 16%, 23% (2025). **No customer count** | $5,815M (2024) | — | *verified*, N-AD13 |
| ArcBest | "serving more than 30,000 customers" (whole company) | — | — | *assumed*, snippet, N-AD37 |

**No carrier publishes how its customers are spread by spend** (share under $10k, $100k, $1M a year). A carrier "customer" is a billing account, and one small shipper uses several carriers (Cycle Force paid four).

### 4.3 Freight as a share of sales

Not redone: check X §7.2 (Establish Davis, transportation 3.68% of sales on average) and §7.3-7.4 (TL+LTL bands). **New from §4.1:** LTL paid to asset carriers by these nine small firms was **0.2-4.6% of revenue, median ~0.7%** **[our calc]**, i.e. roughly a fifth of all transportation cost if Establish Davis's 3.68% applies [our calc].

---

## 5. AD4 · Cost to serve a dispute

| Input | Value | Label | Source |
|---|---|---|---|
| Minutes to audit one LTL invoice by hand | 8-13 (Navix: 2,000 charge lines = 67-100 hours a week for 500 shipments → 8-12 min; Intelligent Audit 10; US Tech Automations 11-13) | *assumed* (vendors) | N-AA31, N-AA32, N-AA35 (not redone) |
| Minutes per reweigh or reclass dispute | **Not found** in any job posting, 3PL page or vendor page searched | — | §11 |
| What a dispute needs | "Spec Sheet – This is an official document from the manufacturer that includes basic information about the freight, including: Weight, Dimensions, and Product Description" plus "Packing Slip"; "These must be official documents and cannot be handwritten"; "Dispute claims filed within three days of being invoiced have a MUCH better chance of being successful"; "Disputes can take between two weeks and two months to complete depending on the carrier"; "A freight broker can file claims on your behalf" | *assumed* (broker guide, 2014) | N-AD34 |
| Elapsed time, carrier side | Estes: results "within 24 to 48 hours" | *assumed* (carrier claim) | check T (N-T23) |
| **BLS OEWS May 2025, 43-5071 shipping, receiving and inventory clerks** (816,870 employed) | Mean **$22.50/h** ($46,810/yr); 10th $16.66, 25th $18.37, median **$21.76**, 75th $24.79, 90th $29.90. **Loaded ÷ 0.70 = $32.14/h** | *verified* (BLS public API v1, series OEUN0000000000000435071xx); loaded **[our calc]** | N-AD24, N-AA40 |
| 43-3021 billing and posting clerks | Mean $24.55/h (loaded $35.07) | *verified* | N-AA39 (not redone) |
| 43-3031 bookkeeping clerks | Mean $25.75/h (loaded $36.79) | *verified* | brief; N-AA39 |

**Per-shipment human cost [our calc]:** 1 minute of a shipping clerk's loaded time = **$0.54**; 10 minutes = $5.36; a 15-minute dispute = $8.04.

---

## 6. AD5 · What is charged today

| Offer | Price as stated | What it includes | Label | Source |
|---|---|---|---|---|
| **LTLflow** (software of Pinnacle, a 3PL) | Free: "$0 per month", "75 shipments / month", 1 location. Pro: "$200 per month", unlimited shipments. Scale: "$300 per month + $2,000 one-time for the included scale". Enterprise: "$1,300 per month + $7,000 one-time for the included dimensioner" | "weight and dimension certificates, photo documentation, and custom checklists" (the shipper's own evidence at the dock). **Pinnacle credit: "$8 in credit per shipment"; "50 shipments per month with Pinnacle" = "$400/month in credits", which "Covers the Scale plan ($300/mo) in full, floor scale included"** | *verified* as stated (extraction) | N-AD30 |
| QBOID handheld pallet dimensioner (via LTLflow) | "$3,400 retail value"; add-on on paid plans, or "$0/month" at qualifying Pinnacle volumes; "Pallet dimensioning in under 30 seconds" | the prevention tool, bundled free by a 3PL | *verified* as stated | N-AD30 |
| Overhead or fixed dimensioners | "$35,000-plus" (SMC3); $20-35k infrared, $65-100k laser; $8-25k per station (search summaries) | — | *assumed* | N-T43, N-AD38 |
| SMB LTL tools with audit tabs | MyCarrier $0/$60/$200 a month; Freightview $149 a month (0-50 shipments); FreightPOP by quote | not redone | *verified* as stated | N-X29-N-X31 |
| Contingency for audit and disputes | 25-50% of recoveries (general freight audit); no **LTL reclass-specific** percentage found | not redone | *assumed* | check X §5.1 |
| 3PLs disputing inside their margin | A broker guide says a broker "can file claims on your behalf" (N-AD34). Unishippers' dispute guide is behind a download form (not opened). **No 3PL page found that states it disputes reweighs free, or at a price** | — | *assumed* / not found | N-AD34, N-AD40 |

**Reading [our call]:** the cheapest competing offer is **free evidence capture bundled by a 3PL** (Pinnacle pays for a scale or a dimensioner out of $8 a shipment of its margin). A standalone product would price against $0-300 a month.

---

## 7. AD6 · What prevention saves

**A real class-rate table** (a "major LTL carrier", Atlanta to Memphis, 2008; Ray Bohman, *Logistics Management*, 2008-10-01, Figure 4; N-AD31, *verified* as printed). Rate per cwt for a 500-999 lb shipment, and the step to the next class **[our calc]**:

| Class | 50 | 55 | 60 | 65 | 70 | 77.5 | 85 | 92.5 | 100 | 110 | 125 | 150 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $/cwt (500-999 lb) | 52.87 | 56.93 | 60.32 | 63.71 | 67.77 | 73.19 | 79.29 | 85.40 | 91.49 | 99.62 | 112.50 | 134.19 |
| Step up from the class to its left | — | +7.7% | +6.0% | +5.6% | +6.4% | +8.0% | +8.3% | +7.7% | +7.1% | +8.9% | +12.9% | +19.3% |

- **One class step costs about 6-9% of linehaul** in the common range (50-110) [our calc]. Class 70 → 85 is +17%; 70 → 100 is +35%.
- **Penalty class:** XPO bills improper descriptions at class 150, "subject to inspection" (check T §3.2). On this table class 150 is **1.98 × class 70** and 1.47 × class 100 [our calc].
- **The article also shows the weight-band effect:** each heavier band cuts the rate 7.8-9.2%; a class-70 shipment at 461 lb is cheaper billed as 500 lb (*verified*). This is why a reweigh that crosses a band can move the bill less than the weight does.

**What correct declaration at pickup saves [our calc, our call]:**
- When the **carrier was right** (the usual case, §3), declaring correctly saves **only the correction fee, $15-55**. The re-rated freight is owed either way. On bill 174087550 (§2.4), prevention saves $18 of the $72.
- When the carrier would **wrongly** re-rate, good evidence at pickup turns a dispute into a win. The saving is the whole correction (e.g., one class step ≈ 6-9% of linehaul, plus the fee).
- **The penalty case** (vague description billed at class 150): up to about **double** the linehaul of a class-70 shipment.
- **A catch the founders should see:** a shipper whose declared weights are *low* and not always caught pays less today than it would if it declared correctly. Declaring correctly **raises** the bill on every shipment the carrier would have missed. With dimensioners on 75-90% of freight at the big carriers (check T), few are missed, but the net saving of prevention can be smaller than the fees avoided.

---

## 8. AD7 · Market-level size

| Measure | Value | Label | Source |
|---|---|---|---|
| **US LTL market, 2024** | **$52,819M** (top 25 carriers $48,166M); average daily shipments **669,545** (top 25: 586,545); 3,216 terminals | *verified* (SJ Consulting table, © 2025 S&P Global) | N-AD09 |
| US LTL market, 2025 | **$51,807M** (top 25 $47,297M); FedEx Freight $8,782M, ODFL $5,446M, Estes $4,986M, XPO $4,832M, R+L $3,725M, Saia $3,234M, ABF $2,735M, TForce $2,012M | *verified* (SJ Consulting table in *Logistics Management*, April 2026) | N-AD10 |
| Shipments a year and revenue per shipment | 669,545 × ~252 working days ≈ **168.7M shipments**; $52.8B ÷ 168.7M ≈ **$313** | **[our calc]** (working days assumed) | N-AD09 |
| Cross-checks on revenue per shipment | Saia $347.81 (known); FedEx Freight $8,892M ÷ 22.7M = $392 (FY2025, check T data); YRC 2018 ~$500 (complaint, §2.2); UPS/Delphi set $384 | **[our calc]** | as cited |
| **Correction money, industry-wide** | FedEx's dimensioner rate (0.8%) applied to the market: **~$420M a year**. Fees alone at 5% of shipments: 8.4M × $15-55 = **$127-464M a year** | **[our calc]**, rough | N-T36, N-AD09 |
| Withheld downward corrections | If the Yellow/Roadway share (0.18-0.54% of revenue) held industry-wide it would be $95-285M a year; **there is no evidence it does** (2007: twelve carriers said they credited negatives) | **[our calc]**; **[our call]** that it does not generalise | N-AD01 |
| **How many US shippers use LTL** | **Not found.** Largest carrier: 108,000 active customers. WWEX Group (Worldwide Express, GlobalTranz, Unishippers; SMB focus): "130,000+ customers nationwide" across all modes including parcel. C.H. Robinson: ~75,000 customers, all modes | FedEx *verified*; others *assumed* (snippets) | N-AD11, N-AD36, N-AD37 |
| **Shippers spending above $100k / $250k / $500k / $1M / $2M on LTL** | **Not found** in any carrier, association or government source searched. The only distribution evidence is §4.1 (9 firms, median ~$94k) and FedEx's average ($64k outside its top 25) | — | §11 |

---

## 9. For the coordinator (not a call)

Everything below is **[our calc]** with inputs labelled above, or **[our call]**. It sets nothing.

**9.1 The chain with document-based inputs, for a median small shipper.**
Inputs: LTL spend $94k a year (§4.1 median); $313-384 a shipment → **~245-300 shipments** a year; corrections on 5-28% of shipments; $72 added per correction (§2.4).

| Case (corrected share, wrong-and-winnable share, credited share) | Shipments corrected | Correction $ a year ($72 each) | Wrong and winnable $ | Credited $ | **Fee at 30%** |
|---|---|---|---|---|---|
| Low (5%, 10%, 60%) | 15 | $1,080 | $108 | $65 | **$19** |
| Middle (15%, 25%, 75%) | 45 | $3,240 | $810 | $608 | **$182** |
| High (28%, 50%, 90%) | 84 | $6,048 | $3,024 | $2,722 | **$817** |

(300 shipments assumed for the arithmetic. "Wrong and winnable" and "credited" are placeholders, §1.)

**9.2 Cost to serve at the same shipper.** Checking every shipment for 1 minute at $32.14/h loaded = 300 × $0.54 = **$161 a year**; disputes at 15 minutes each = $8.04 each (middle case: 45 × 25% ≈ 11 disputes = **$90**). **Middle-case cost ~$250 against a fee of ~$182: a loss before any fixed cost.** The fee covers variable cost only in the high case.

**9.3 How many customers the revenue floor needs.** $2.5M ÷ $182 ≈ **13,700 median shippers** in the middle case; $2.5M ÷ $817 ≈ 3,100 in the high case. At the bicycle distributor's $389k of LTL (4× the median), the middle-case fee is ~$750 and the floor needs ~3,300 customers. For comparison, the largest LTL carrier has 108,000 active customers in total.

**9.4 Where the pool actually is [our call].**
- **Most corrections are the shipper's own error** (SJ Consulting, ODFL's named shippers, the Delphi bill). A dispute product earns only on the minority that are the carrier's error; **nobody has measured that minority**, so the S5 savings assessment is the only way to learn it.
- **The documented carrier-error pool** (Yellow/Roadway not crediting downward reweighs) was **0.18-0.54% of the carriers' revenue**, and a court held such claims time-barred after 180 days (N-AB35).
- **Prevention saves mostly fees** ($15-55 a correction), plus penalty classes, and the market already gives the tools away (a 3PL funds a scale or dimensioner out of $8 a shipment). It can also raise bills on shipments the carrier would have missed (§7).
- **Small shippers buy little LTL** in the real filings (median ~$94k a year, ~0.7% of revenue), and some of it runs through 3PLs or is paid by their customers (collect). The card's paying side may therefore be firms far above the median, or 3PLs.

**9.5 What the S5 assessment could measure that the web could not** (for the kill condition):
1. The shipper's own correction rate (share of its shipments re-rated) and $ per correction, from 3-12 months of its carrier invoices.
2. Of those, how many the shipper can prove wrong with its own spec sheets and packing slips (the carriers' stated proof, check T §3.2).
3. How many it disputed, how many were credited, and how long it took.
4. Its LTL spend and shipment count, and how much goes through a 3PL or is collect.

---

## 10. Sources

Access: full = whole document downloaded and searched; page extraction = read through the fetch tool; snippet = search result text only; blocked = could not be read.

| ID | Source | Date | URL | Access | What was used |
|---|---|---|---|---|---|
| N-AD01 | *U.S. ex rel. Hannum v. Roadway Express, Inc. et al.*, W.D.N.Y. 1:08-cv-00811, Doc 72, United States' Complaint in Intervention | 2018-12-12 | https://storage.courtlistener.com/recap/gov.uscourts.nywd.71195/gov.uscourts.nywd.71195.72.0_2_1.pdf | full (text layer) | ¶50-¶89: 75,324 positive vs 42 negative reweighs in 1.5M invoices; $1-1.5M and $500k a month; $10-20M; $800 and 70% tolerances; industry surveys; 725 claims a month |
| N-AD02 | Same case, Doc 72-1, Exhibit A (examples of false claims) | 2018-12-12 | https://storage.courtlistener.com/recap/gov.uscourts.nywd.71195/gov.uscourts.nywd.71195.72.1.pdf | full | Actual vs billed weights of DOD shipments |
| N-AD03 | Same case, Doc 1, relator's complaint | 2008-11-03 | https://storage.courtlistener.com/recap/gov.uscourts.nywd.71195/gov.uscourts.nywd.71195.1.0_2_1.pdf | full | Two bills: $222.84 and $133.23; 30-40 lb tolerance |
| N-AD04 | *Southern Furniture Leasing, Inc. v. YRC, Inc.*, D. Kan. 2:19-cv-02129, Doc 1, class action complaint (also Doc 16, order) | 2019-03-08 | https://storage.courtlistener.com/recap/gov.uscourts.ksd.125616/gov.uscourts.ksd.125616.1.0.pdf | full | 10M shipments and $5B (2018); $1-1.5M a month; $45M at issue; no plaintiff shipment data |
| N-AD05 | *Lewis v. YRC Worldwide Inc.*, N.D.N.Y. 1:19-cv-00001, Doc 75 (amended complaint) and Doc 1 | 2019-06-19; 2019-01-02 | https://storage.courtlistener.com/recap/gov.uscourts.nynd.117395/gov.uscourts.nynd.117395.75.0.pdf | full | CW statements (10 protests a day; $25 per 30 reweighs; "cheat codes"); rerate reserve $9.6M / $11.9M |
| N-AD06 | *In re Delphi Corp.*, Bankr. S.D.N.Y. 05-44481, Doc 20038 and 20038-1 (Witt declaration; Exhibit A, open invoices) | 2010-05-12 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.137477/gov.uscourts.nysb.137477.20038.1.pdf | full | 195 UPS Freight invoices, $74,852.89 |
| N-AD07 | Same case, Docs 20040 (and -1 to -4) and 20041 (-1, -2, -4): Exhibit B, UPS Freight freight bills, BOLs, delivery receipts | 2010-05-12 | https://storage.courtlistener.com/recap/gov.uscourts.nysb.137477/gov.uscourts.nysb.137477.20040.1.pdf (and sibling files) | full; 2 files text layer, 7 files OCR'd by us (tesseract) | 169 matched bills, 48 reweighed; weight pairs; $18-26 fees; worked bill 174087550 |
| N-AD08 | YRC Worldwide Inc., Form 10-K FY2006 (SEC) | 2007-02 | https://www.sec.gov/Archives/edgar/data/0000716006/000119312507044346/d10k.htm | page extraction (fetch tool) | Yellow Transportation revenue $3,421.3M (2005), $3,460.5M (2006); Roadway $3,321.1M (2005), $3,427.1M (2006) |
| N-AD09 | SJ Consulting Group, "Journal of Commerce Top 25 US LTL Carriers" (2024 data) | 2025 | https://jindel.com/wp-content/uploads/2025/06/top25_us_LTL_2025.pdf | full (PDF) | US LTL market $52,819M; 669,545 daily shipments; carrier revenues and shipments |
| N-AD10 | SJ Consulting Group, "2025 Top 25 U.S. LTL Carriers", *Logistics Management* | 2026-04 | https://jindel.com/wp-content/uploads/2026/04/2026-Top25-LTL-LM.pdf | full (PDF) | US LTL market $51,807M (2025); carrier revenues |
| N-AD11 | FedEx Freight Holding Company, Form 10-K FY2026 (same filing as N-T36; new facts read) | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/0002082247/000162828026053359/fdxf-20260531.htm | page extraction (fetch tool) | 108,000 active customers; top 5 / top 25 = 9% / 21%; largest 4% |
| N-AD12 | XPO, Inc., Form 10-K FY2024 (company IR copy) | 2025-02-07 | https://investors.xpo.com/static-files/bbd8e1d2-c612-49af-9509-569b2ff4aaca | full (PDF) | 55,000 customers; NA LTL revenue $4,899M; concentration; 51,508 shipments/day; 1,351 lb |
| N-AD13 | Old Dominion Freight Line, Form 10-K FY2024 (IR copy) and FY2025 (SEC) | 2025-02; 2026-02 | https://ir.odfl.com/sec-filings/all-sec-filings/content/0000950170-25-026661/odfl-20241231.htm ; https://www.sec.gov/Archives/edgar/data/878927/000119312526067161/odfl-20251231.htm | full (2024); page extraction (2025) | Customer concentration; no customer count; revenue $5,815M (2024) |
| N-AD14 | Cycle Force Group, LLC, Bankr. S.D. Iowa 21-00571, Doc 1 (petition, schedules, SOFA) | 2021-04-22 | https://storage.courtlistener.com/recap/gov.uscourts.iasb.152427/gov.uscourts.iasb.152427.1.0.pdf | full | SOFA 1 and 3 |
| N-AD15 | Spokane Industries, LLC, Bankr. E.D. Wash. 26-00116, Doc 1 | 2026-01-23 | https://storage.courtlistener.com/recap/gov.uscourts.waeb.219123/gov.uscourts.waeb.219123.1.0.pdf | full | Saia $33,000 paid; $125,992.17 owed; revenue |
| N-AD16 | Imperial Toy LLC, Bankr. N.D. Cal. 19-52335, Doc 75 (SOFA) | 2019-12-09 | https://storage.courtlistener.com/recap/gov.uscourts.canb.577878/gov.uscourts.canb.577878.75.0.pdf | full | 309 payments parsed; ABF $40,757.85; revenue |
| N-AD17 | Sona BLW Precision Forge, Inc., Bankr. E.D.N.C. 16-04336, Doc 62 (schedules, SOFA, Exhibit A) | 2016-09-02 | https://storage.courtlistener.com/recap/gov.uscourts.nceb.299023/gov.uscourts.nceb.299023.62.0_1.pdf | full | 247 vendor payments parsed; LTL $7,929.30; revenue |
| N-AD18 | Old World Timber, LLC, Bankr. E.D. Ky. 21-51160, Doc 1 | 2021-10-19 | https://storage.courtlistener.com/recap/gov.uscourts.kyeb.319351/gov.uscourts.kyeb.319351.1.0_1.pdf | full | Estes and Saia payments; revenue |
| N-AD19 | Electric Bike Company, LLC, Bankr. C.D. Cal. 8:25-bk-12810, Doc 1-13 (SOFA) | 2025-10-03 | https://storage.courtlistener.com/recap/gov.uscourts.cacb.2027343/gov.uscourts.cacb.2027343.1.13_1.pdf | full | Estes, R&L payments; carrier suits; revenue |
| N-AD20 | Instaset Plastics Company, LLC, Bankr. E.D. Mich. 22-47794, Doc 1 | 2022-10-05 | https://storage.courtlistener.com/recap/gov.uscourts.mieb.969487/gov.uscourts.mieb.969487.1.0.pdf | full | Dayton Freight by month; revenue |
| N-AD21 | Loadcraft Industries, Ltd., Bankr. W.D. Tex. 21-11018, Doc 53 (amended schedules and SOFA) | 2022-01-25 | https://storage.courtlistener.com/recap/gov.uscourts.txwb.352502/gov.uscourts.txwb.352502.53.0.pdf | full | FedEx Freight paid and owed; revenue |
| N-AD22 | Novalent, Ltd., Bankr. E.D.N.C. 24-02756, Doc 1 | 2024-08-16 | https://storage.courtlistener.com/recap/gov.uscourts.nceb.337514/gov.uscourts.nceb.337514.1.0.pdf | full | Estes payment; revenue; NAICS |
| N-AD23 | Hamilton Scientific LLC, Bankr. D. Del. 17-10655, Doc 2 (schedules) | 2017-03-29 | https://storage.courtlistener.com/recap/gov.uscourts.deb.167632/gov.uscourts.deb.167632.2.0.pdf | full | Schedule F balances owed to LTL carriers |
| N-AD24 | BLS OEWS May 2025, 43-5071 shipping, receiving and inventory clerks, public API v1 (series OEUN0000000000000435071 01, 03, 04, 06-10) | 2026 release | https://api.bls.gov/publicAPI/v1/timeseries/data/OEUN000000000000043507103 | full (API) | Employment, mean and percentile wages |
| N-AD25 | CourtListener RECAP search API (the queries behind §2 and §4.1; ~20 searches, ~100 filings screened) | 2026-09-22 | https://www.courtlistener.com/api/rest/v4/search/ | full | Finding the documents above |
| N-AD26 | Evos, "The Invoice You Didn't Audit: Why LTL Billing Became an Operations Problem" | 2026-07-20 | https://www.getevos.ai/resources/blog/ltl-invoice-audit-operations-problem | page extraction (vendor) | "82%" and "70%" are its AI metrics; class step "10–20%"; fees "$25–40" |
| N-AD27 | Old Dominion Freight Line, "How LTL Shipping Data Accuracy Impacts Pricing & Re-Rating" (OD Outlook) | undated | https://www.odfl.com/us/en/resources/OD-Outlook/Accurate-Freight-Data-in-LTL-Shipping.html | page extraction (carrier marketing) | Bestorq and Douglas Dynamics: 25% re-rated; 1% after a dimensioner |
| N-AD28 | FreightWaves, "How Accurate Shipping Data Is Transforming LTL Outcomes" (sponsored by ODFL) | 2026-04-29 | https://www.freightwaves.com/news/how-accurate-shipping-data-is-transforming-ltl-outcomes | page extraction | "one in four shipments"; sponsorship flag |
| N-AD29 | EA Eller Audit, "LTL Freight Audit" (same page as N-X26, re-read for the trace) | 2026-06-03 | https://www.elleraudit.com/ltl-freight-audit | page extraction (vendor) | Origin of 4-6% / $145 / 70-82%: a hypothetical $12M, 32,000-shipment manufacturer |
| N-AD30 | LTLflow (Pinnacle), pricing page and QBOID equipment page | current | https://ltlflow.com/pricing ; https://ltlflow.com/equipment-qboid | page extraction | Plans, $8 credit per shipment, $3,400 dimensioner |
| N-AD31 | Ray Bohman, "Understanding LTL carrier class rates", *Logistics Management* (copy hosted by shipsst.com) | 2008-10-01 | https://www.shipsst.com/documents/understanding_ltl_carrier_class_rates.pdf | full (PDF) | Class-rate table, weight-band steps, minimum charges |
| N-AD32 | GSA, "Section B – Table of Baseline Rates and Minimum Charges" (1000-D) | 2014 | https://www.gsa.gov/system/files/GSA%201000-D.pdf | full | Weight-band table only (no class ratios); not used for AD6 |
| N-AD33 | NIST OWM, 2026 L&R interim executive summary (Uniform Shipment Law item OTH-24.1) | 2025-12-17 | https://www.nist.gov/system/files/documents/2025/12/18/2026%20L%26R%20Interim%20Executive%20Summary-20251217-Final.pdf | full | No data; item "Assigned" to a task group |
| N-AD34 | FreightPros (now NTG), "How to Dispute a Reweigh" | 2014-07-12 | https://www.freightpros.com/whitepaper/dispute-reweigh/ | page extraction (broker) | Documents needed; 3-day advice; 2 weeks-2 months |
| N-AD35 | Transport Topics, "LTLs Can Reduce Expenses With E-Billing, Experts Say" | 2010-03-08 | https://www.ttnews.com/articles/ltls-can-reduce-expenses-e-billing-experts-say | page extraction | Jindel: $1 per paper bill; 85% paper. Not the accuracy survey |
| N-AD36 | WWEX Group, company pages and press release | 2023-26 | https://wwexgroup.com/ | snippet | "130,000+ customers", 70M+ shipments a year |
| N-AD37 | ArcBest and C.H. Robinson customer counts (search results) | 2025-26 | https://www.sec.gov/Archives/edgar/data/1043277/000104327726000009/chrw-20251231.htm (C.H. Robinson 10-K, not opened) | snippet | ~30,000 (ArcBest); ~75,000 (C.H. Robinson) |
| N-AD38 | Dimensioner price summaries (Optioryx, Cubiscan, Packizon pages via search) | 2025-26 | https://www.optioryx.com/blog/best-warehouse-dimensioning-systems ; https://cubiscan.com/pallet-dimensioner-ltl-shipping/ | snippet | $20-35k infrared, $65-100k laser, $8-25k per station |
| N-AD39 | Search summaries with no traceable page (adjustments on "5 to 10 percent of bills"; "15-25% ... $125-300 per incident"; "60–70%"; "70% of the time") | 2026-09-22 | (search results only) | snippet | Listed so they are not reused as facts |
| N-AD40 | Unishippers, "Guide to Dealing with Freight Shipping Disputes" landing page | 2021-12-07 | https://www.unishippers.com/shipping-resources/freight-resources/guide-to-dealing-with-freight-shipping-disputes | page extraction; guide behind a form (not opened) | No terms stated |
| N-AD41 | Rice Lake, "How to Determine Pallet Dimensioner ROI" | — | https://www.ricelake.com/resources/articles/how-to-determine-pallet-dimensioner-roi | **blocked (HTTP 403)** | — |

Earlier IDs used: N-T17-N-T30 (tariffs), N-T36, N-T37, N-T43, N-T40, N-T33, N-T34, N-T23 (check T); N-X26, N-X29-N-X31 (check X); N-AA31, N-AA32, N-AA35, N-AA39, N-AA40 (check AA); N-AB27, N-AB35, N-AB37 (check AB).

---

## 11. Could not access, or not found

- **A neutral share of corrections that are wrong, or a neutral dispute win rate.** Not in carrier filings, court findings, NCWM papers (check T), NIST, or academic work. The DOJ and class complaints are allegations about one carrier group, 2005-2013.
- **The original SJ Consulting billing-accuracy survey.** Only secondary quotes (a broker's page, an audit firm's blog) were found; jindel.com lists rankings, not the survey.
- **Minutes per reweigh or reclass dispute.** No job posting, 3PL or audit page stated one.
- **A distribution of US shippers by LTL spend** (how many spend over $100k, $250k, $500k, $1M, $2M), and **the number of distinct US LTL shippers.** No carrier, association or government source publishes either.
- **Industry-wide reweigh, reclass or dimensioner revenue.** Only FedEx Freight's own figure exists (N-T36); the industry totals in §8 are our extrapolations.
- **An LTL-specific contingency percentage** for reclass and reweigh disputes, and any 3PL's stated terms for disputing on a customer's behalf (Unishippers' guide is behind a form, not opened).
- **Real private-shipper bills with reclass (class change) corrections.** The UPS/Delphi set shows reweighs; only 4 bills mention an inspection, and none a legible class change. The coordinator's ABF set is the other real source.
- **Delphi Exhibit B completeness:** attachment 20041-3 was not in the archive; about 393 of the exhibit's 425 page numbers were seen. Seven of nine files were scans read by OCR, so counts may be off by a few bills.
- **SEC EDGAR full-text search** was not used (it requires a declared contact in the request header; not supplied, per the rules). Filings were read through company investor-relations copies or the fetch tool.
- **bls.gov web pages** redirect automated requests to an index; BLS figures came from the public API instead.
- **Rice Lake dimensioner ROI article** (HTTP 403).
- **The DOJ settlement press release** ($6.85M, 2022) was not re-opened; it stays a snippet from check T (N-T40).
