# S5 check AN, adversarial review

- **What this is:** an adversarial check of check AN's web evidence. The founders asked for "adversarial agents for the web resources so we prune any coincidences and can settle the facts ourselves or throw away faulty web data". The aim was to break the claims without inventing objections. A claim that survived is a result too.
- **File checked:** `research/s5_check_AN_c09_service_and_customer.md` (57 claim rows, C-AN01 to C-AN57; §0 proposed verdicts; Coincidence watch). That file was not edited.
- **Date:** 2026-10-07.
- **Status:** input to S5. **It decides nothing.**
- **Searches used:** 7 web searches of the 10 allowed. All were counter-searches (listed in §6).
- **Fetches made:** about 75, all re-fetched independently. They include:
  - every cited PDF and page that was reachable;
  - 3 extra bankruptcy filings (Cycle Force, Imperial Toy, Sona) to rebuild check AD's broker shares;
  - CT Logistics' **current** federal price list;
  - the original JOC 2020 survey report;
  - about 20 lookups in FMCSA's public SAFER register (the government list of trucking companies and brokers);
  - 8 calls to the USAspending.gov API;
  - one Wayback Machine copy.
  Scripts and downloads are in the session scratchpad only.
- **No identity was sent. Nobody was contacted.** No logins, forms or sign-ups. SEC EDGAR was not fetched.
- **Rows checked:** 47 in full (all 26 load-bearing rows, plus 21 rows that feed a §0 number); 8 sampled (existence test: C-AN01 to C-AN08, which cover the tender and award rows); 2 not checked (C-AN22 and C-AN56, both blocked; §7).

**Words used here:**
- **GSA schedule / price list:** a federal catalogue price that agencies may pay without a new tender. It is a ceiling price, not proof that anyone bought the service.
- **Contingency fee:** the auditor keeps a share of the money actually recovered.
- **First and second audit (federal):** the first and the second post-payment check of the same paid bills. Federal bills were already checked before payment.
- **EDI:** bills sent machine-to-machine. **Hard copy or electronic copy:** a paper bill, or an image of one such as a PDF.
- **SOFA:** a bankrupt firm's sworn Statement of Financial Affairs. Item 3 lists payments made in the 90 days before filing.
- **Annualise:** multiply 90 days of payments by 365/90. **Run-rate:** part-year revenue scaled to a full year.
- **Broker / 3PL:** a middleman that books the truck and bills the shipper itself. **SAFER:** FMCSA's public register, which says whether a company is a carrier (has trucks) or a broker.

---

## §0 Result in one table

**Verdict counts (57 rows)**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|
| 23 | 16 | 15 | 1 | 2 |

**The §0 question verdicts**

| Question | Researcher's verdict | Ours | Why, and what must change in §0's wording |
|---|---|---|---|
| A09-04 fee share | Narrowed | **AGREE** | Keep the verdict, but update the prices. The 2019-20 CT Logistics list has been replaced by a current list (May 2026 to May 2027): **23.23%** first audit and **38.61%** second audit; **$2.79** per EDI bill and **$4.68** per hard-copy or PDF bill. Everything is still below 50%. The GMG list expired in 2016. Virginia's 13.5-40% was a general accounts-payable recovery audit (mostly duplicate payments), not a freight audit. |
| D-15 free looks, look-back vs ongoing | Narrowed | **AGREE** | The free offers are confirmed. The second-audit premium persists on the current federal list. One counter-search found no published price for a paid assessment. |
| A09-05 invoices per $1,000 | Narrowed | **AGREE** | The arithmetic is right. Two caveats: ABF's per-shipment figure includes U-Pack household moves, and carrier averages are skewed by heavy shipments. A shipper with light freight gets more bills per $1,000. |
| A09-06 share needing a person | Narrowed | **AGREE** | Add the counter-evidence. CarrierDirect (2016) put **valid** re-rates at 10-15% of LTL shipments, against Old Dominion's 25-30% "re-rated". AFS short-paid 3.5-4% of LTL invoices in 2023. |
| A09-07 minutes, dispute cost | Narrowed (review); Not answerable (dispute) | **AGREE** | The minutes must be recomputed at current prices: **at most about 4.6 to 7.6 minutes** of a $36.79/hour clerk, not 3.8-6.3. A PDF bill falls in the higher (hard-copy) price class. Ascent's own sheet contradicts itself (5 hours vs 50 hours a week). |
| A09-08 fixed cost | Narrowed | **AGREE** | Small reclassifications only: Bemak is a broker, and Agway paid one more trucking firm. 14-18 payees and 6-9 to reach 80% still hold. |
| A09-09 TL+LTL spend | Narrowed | **AGREE** | The filings re-add to the cent. Annualised, the three firms paid trucking firms **$1.51-1.91M** a year. But "2.9-4.1% of revenue" is a selection. Depending on which year's revenue is used, the range is **0.9-4.8%**. |
| A09-12 offshore review | Not answerable | **AGREE** | The two federal "point of production" lines are the contractors' own statements of where they work. They are not buyers' bans. The 2006 "76%" figure could not be found in the archived article. |
| A09-14 brokers, minimums, reweighs | Narrowed | **AGREE** | Correct the range. Rebuilt from the full payment lists, brokers took **0% to about 52%** of trucking dollars (up to 65% if one payee is a broker), **not 0-74.9%**. The median of the six is **about 15-17%**, so the researcher's 15.4% roughly survives. |

**Disagreements with a §0 verdict:** none. The changes are to the numbers quoted inside §0, not to the verdicts.

---

## §1 Discards and narrowings (most consequential first)

| Claim ID | What was claimed | What the source actually says (quote) | Verdict | Why |
|---|---|---|---|---|
| **C-AN51** (feeds C-AN50, §0 A09-14) | In check AD's lists, brokers took 11.9% (Cycle Force), 74.9% (Imperial Toy) and 16.7% (Sona) of trucking dollars | Imperial Toy's SOFA lists five more trucking payees than check AD extracted: "3.110. JB HUNT TRANSPORT 9/6/2019 $11,236.61"; "3.117. LANDSTAR GLOBAL 10/23/2019 $6,636.00"; "3.265. TQL 10/23/2019 $1,385.00" (plus Atlas Transportation and Gold Point Transport). Cycle Force also lists "Online Freight Services 1/21-4/21 $9,212.40" and "McGrew Trucking 1/21-4/21 $9,090.00" | **DISCARD** (as a broker share of trucking) | Check AD extracted LTL carriers plus one 3PL, so 74.9% is MODE's share of two payees out of seven. **Re-done on the full lists:** <br>• Imperial Toy: 45.4% (MODE + TQL), 51.2% if Landstar Global (registered as a carrier/freight forwarder) counts as a middleman, 65.1% if Atlas is a broker (several firms share that name). <br>• Cycle Force: 10.2%, or 17.5% if Online Freight Services counts as a broker. SAFER lists it as a "CARRIER/BROKER" with 0 trucks. <br>• Sona: 16.4% once a missed carrier (Southern Ag Carriers, $2,800) is added. <br>The §0 phrase "0% to 74.9%" and the reading "from none to three-quarters" are wrong. |
| **C-AN09** | CT Logistics' federal list price is $2.31 (electronic) to $3.88 (paper) per motor-freight bill | 2019-20 list: "Administrative Review of hard copy or electronic copy bills … Motor Freight $3.88"; "Bills transmitted via Electronic Commerce … Motor Freight $2.31". **Current list (contract 47QRAA19D007U, generated Jan 2026):** "Review Hard Copy Motor Freight bills … 4.57 \| 4.68"; "Review Electronic Commerce Motor Freight bills … 2.72 \| 2.79" (contract year 7 \| year 8) | **NARROW** | **Keep only this reading:** the 2019-20 prices of an expired contract (GS-23F-0095K ended in Feb 2020). The same firm's price from 7 May 2026 is **$2.79** per EDI bill and **$4.68** per hard-copy bill. A PDF is an "electronic copy", which sits in the **higher** class, so "paper" understates the price for our segment's PDF bills. |
| **C-AN10** | The same list charges 19.25% (first audit) and 32% (second) of motor-freight refunds | 2019-20: "1st AUDIT Motor Freight 19.25%"; "2nd AUDIT Motor Freight 32.00%". Current: "1st Audit Motor Freight \| P1 \| 22.66 \| 23.23"; "2nd Audit Motor Freight \| P1 \| 37.67 \| 38.61" (P1 = percent) | **NARROW** | **Keep only this reading:** the 2019-20 rates. The current federal ceiling is **23.23% / 38.61%** (from May 2026). Federal bills are checked before payment ("GSA REQUIRES THAT GBLS BE PRE-AUDITED BY AN OUTSIDE PARTY PRIOR TO PAYMENT", C-AN04), so even the "first" post-payment audit is a second look, at low yield. The shares may not carry over to unaudited private bills. |
| **C-AN17** (derived "3.8-6.3 minutes") | Federal per-bill prices imply at most 3.8-6.3 minutes of a $36.79/hour clerk per bill; the special audit equals 8.3 minutes of the list's rate auditor | Current prices $2.72-2.79 (EDI) and $4.57-4.68 (hard copy); special audit "15.38 \| 15.76"; rate auditor "111.51 \| 114.3" per hour | **NARROW** | The arithmetic was right on the old prices; we re-did it. **At current prices: at most 4.4-4.6 minutes (EDI) and 7.5-7.6 minutes (hard copy or PDF) of a $36.79/hour clerk, on average across all bills, before overhead and margin.** The special audit is still 8.3 minutes of the list's auditor. The bound depends on the wage: a $25/hour clerk would be 6.7-11.2 minutes. These are prices, not time studies. |
| **C-AN48** | Annualised, the three firms paid trucking firms about $1.5-1.9M a year, 2.9-4.1% of revenue | Latex: "$17,565,000.00 2014 YTD: Debtor Business Income" (150 days). UGL: "$8,724,214.00 YTD 2011 Sales". Agway: 2022 to filing "24,235,249.00" against 2021 "221,293,860.00" and 2020 "8,849,599.00" | **NARROW** | **Keep only this reading:** on 90 days of a distressed firm's payments, annualised trucking was $1.51-1.91M a year (corrected: §3). Its share of revenue ranges from **0.9% to 4.8%**, depending on which year's revenue is used: <br>• Latex Foam: 2.86% of 2013 revenue, 3.58% of its 2014 run-rate; <br>• UGL: 4.10% of 2010, 4.75% of its 2011 run-rate; <br>• Agway: 0.86% of 2021, 4.02% of 2022. <br>The body's "2.9-4.1% brackets Establish Davis's 3.68%" picks one denominator per firm. |
| **C-AN50** | Brokers took 51.3%, 0.0% and 14.0% of trucking dollars; median of six 15.4% | SAFER: Bemak Traffic Services Inc, Wallingford CT, "Entity Type: BROKER … Power Units: 0". Agway SOFA: "58498 NORTH EAST FRTWAYS DBA LAND AIR EXPRE 4/13/2022 4,483.26" (plus $2,529.72 on 5/5/2022) | **NARROW** | Latex Foam is **52.4%** (Bemak, $4,245, is a broker, not a carrier). Agway is **13.8%** once the missed trucking payee ($7,012.98) is added. With C-AN51 corrected, the six run **0% to 52.4%** (65% at most), with a **median of 15.1-16.9%** and a dollar-pooled share of 23.1-24.5%. The broker share remains a property of each firm. |
| **C-AN47** | Agway paid trucking firms $464,932.52 in 90 days; 257 rows to 85 vendors summing to $2,814,444.07 | The SOFA's pages 15-19 hold **276** payment rows, **$2,984,427.55**, 92 payee names. The researcher's parser required a numeric vendor ID, so 19 rows without one ($169,983.48) were dropped, including "PRECISION DELIVERY SOLUTIONS LLC" ($13,786.02). Its name pattern also missed "NORTH EAST FRTWAYS" ($7,012.98) | **NARROW** | Trucking payees are at least **$471,945.50** in 90 days (about $1.91M a year). Agway's revenue collapsed from $221.3M (2021) to a $47.6M run-rate (2022), so its 90-day payments are not a steady year. Its largest trucking payment (Hub Group Trucking, $102,842.57) was a single payment on the first day of the window. |
| **C-AN25** | ABF's billed revenue per shipment was $532.18 in 2025 | "Billed Revenue(1) / Shipment … $ 532.18 $ 548.81 (3.0%)"; "Billed revenue per shipment decreased 1.9 percent, due primarily to the seasonal step down in U-Pack moving shipments" | **NARROW** | The figure is right. But the asset-based segment includes U-Pack consumer household moves, so it is not a pure business-LTL bill and likely overstates one somewhat. Read it as "ABF network revenue per shipment, all services". |
| **C-AN26** | Carriers' averages imply 1.9-2.9 bills per $1,000 | Old Dominion "LTL weight per shipment (lbs.) 1,477"; LM 2012: "The less-than-500-pound shipment market makes up over 60 percent of LTL shipments according to Dynarates" | **NARROW** | The arithmetic is exact (2.03, 2.08, 1.88, 1.82, 2.88). But these are carrier-wide averages over all customers, including 3PL tenders (Old Dominion: "about one-quarter of its annual revenue from 3PLs", 2014). The averages are pulled up by heavy shipments. A shipper whose freight is lighter than the carrier average gets **more** bills per $1,000; the ABF practice account (2.21) is one example. |
| **C-AN34** | Ascent's savings and hours reconcile with its own inputs ("the sheet is consistent with itself") | Savings box: "CLIENT TIME 5 hours per week". Same sheet, later: "On average, we save clients 50 hours per week." | **NARROW** | The savings box reconciles (200 × 1.5 min = 5 h; 200 × 5% × $270 = $2,700). But the sheet as a whole does not: it claims to save ten times the hours it says the work takes. The 1.5 minutes is one figure from a sheet that also implies about 15 minutes of handling per bill. |
| **C-AN15** | Virginia's 2004 tender drew nine bids of 13.5-40%; the winner bid 20% flat | "The contingency fees quoted … ranged from a low of 13.5% to a high of 40%"; "Cost recovery auditors primarily examine payments to vendors"; "The majority of these recoveries represent duplicate payment claims." | **NARROW** | **Keep only this reading:** nine firms' bids for a state's general accounts-payable recovery audit (mostly duplicate payments) in 2004. It is a neighbouring market's price, not a freight-bill price. (The programme recovered 0.004% of the $22.3B examined.) |
| **C-AN13** | GMG's federal list charged 10% (first) and 25% (second), or $2.36 a transaction | "Contract Period: January 10, 2011 to January 9, 2016"; "First Pre and Post Audit Motor Freight % Commission Per Transaction 10%"; "Second Pre and Post Audit … Rate Per Transaction $ 2.36" | **NARROW** | **Keep only this reading:** an authorised 2011-16 list from a generalist accounting consultancy (its list also prices medical-records auditing). It expired in 2016, and no purchase under it was found (a USAspending search was inconclusive, §7). The same $2.36 applies to the first and second audit alike. |
| **C-AN39** | Three shippers paid 14-18 trucking firms: Latex 18 (4 brokers / 5 LTL / 9 other), UGL 14 (0/10/4), Agway 15 (2/6/7) | Bemak registered as a broker (above); Agway's missed payee (above) | **NARROW** | Latex Foam is **5/5/8**. Agway is **16 (2/7/7)**, 17 if Precision Delivery Solutions is trucking. UGL is unchanged. The 14-18 range survives (14-17). |
| **C-AN12** (used for A09-12) | The list names Cleveland as point of production | "Point of production Cleveland, Cuyahoga County, Ohio"; current list: "Predominant Work Site … Contractor_Facility … Domestic" | **NARROW** | **Keep only this reading:** the contractor's own statement of where it works. It is not a buyer's ban on offshore work, so it does not show that "public buyers often forbid it". Ohio's clause (C-AN16) does show such a ban. |
| **C-AN11** | The rate auditor costs $94.72 an hour; a special audit $13.06 a bill | Current: "Motor Freight - Rate Auditor - per hour … 111.51 \| 114.3"; special audit "15.38 \| 15.76" | **NARROW** | These are 2019-20 prices. The current ones are $114.30 an hour and $15.76 a bill (from May 2026). The 8.3-minute equivalence still holds. |
| **C-AN49** | A 2006 study found 76% saw offshore providers as a higher security risk | Archived article (Wayback, 2025-06-17): "surveyed 158 U.S.-based finance executives last year about outsourcing"; "The survey found that U.S. companies saw offshore outsourcing … as posing a significantly higher security risk." The "Seventy-six percent" sentence is **not in the archived text** | **NARROW** | **Keep only this reading:** a 2005 consultancy survey of 158 US finance executives (all finance outsourcing, not freight) found offshore work was seen as a higher security risk. The 76% figure is unconfirmed. |

---

## §2 Coincidences found

| Figure | Where it appears | Shared origin, or look-alike? | What to do |
|---|---|---|---|
| **20.8% invoices inaccurate** and **"two-thirds outsource"** | FreightWaves 2020 (C-AN23, C-AN32), the Stealth Agents compilation (N-AN35) | **One origin**: *JOC Freight Payment Benchmark Study*, IHS Markit, September 2020, "Sponsored by" a payment vendor. 77 shippers, "roughly three-quarters" with $1B+ revenue. Origin now read: "Nearly two-thirds of respondents said they've outsourced either audit or payment processes — if not both"; "Shippers reported an average invoice inaccuracy rate across all modes of 20.8 percent" | Count it once, as a sponsored survey of large shippers |
| **$2.31 vs $2.36 "agree within cents"** (§AN1 reading 1) | CT Logistics 2019-20 EDI price; GMG 2011 price | **Look-alike.** The prices are 8 years apart and measure different units. CT's EDI-only price escalated 2% a year, so it was about $1.97 in 2011 (hard copy about $3.31). GMG's $2.36 covers all bills and both audits. CT's EDI price is $2.79 today | Do not read the match as market agreement |
| **"20-30%" vs "25-30%" of LTL freight** | Old Dominion paper: "25 to 30 percent of their freight being re-rated"; CarrierDirect 2016: "roughly 20-to-30 percent of LTL shipments have dimensional exceptions" | **Look-alike, different measure.** CarrierDirect, a consultancy that works with carriers, adds that only half the exceptions are valid, so it collects on "10-to-15 percent of all LTL shipments" | The 25-30% band appears in the trade as exceptions flagged, not re-rates collected |
| **"About one-quarter"** of LTL through middlemen | SJ Consulting 2013 (revenue); Old Dominion CFO 2014; Southeastern Freight Lines 26%; a Logistics Management blog of about 2014, "25 percent of total LTL loads" (search summary only, not opened) | The blog likely recycles SJ Consulting's estimate (unproven). Nothing newer than 2014 was found (counter-search 2) | Treat it as one 2013-14 estimate, not three |
| **5.9% GRI** | ABF 2026 (C-AN41); the LM 2012 column's example: "a recent rate increase of a 5.9 percent 'average'" | **Look-alike**, 14 years apart | Coincidence only |
| **50% parcel fee** | Betachon (stated); Refund Retriever | On the fetched page, Refund Retriever's 50% appears only in a worked comparison; the exact sentence quoted in AN was not seen | Keep the parcel cluster as one parcel norm |
| **Two firms called "R & R Freight Services LLC"** | Latex Foam's payee list | **Name collision**: SAFER lists a carrier in Wallingford, CT (11 trucks) and a broker in London, KY. Latex Foam was in Shelton, CT, so the Connecticut carrier is the likely payee [our call] | The researcher's "carrier" class is probably right |
| **The 25% fee share** | The model (25%); CT Logistics' current first-audit ceiling 23.23%; a vendor page's "25%-50%" (search lead) | Different things: a model input, a federal ceiling and a vendor claim. They agree in size only | No merge needed |

The researcher's own Coincidence watch was checked row by row, and its merges stand:
- PRG counted twice at 20%;
- Texas and Virginia at 13.5%, possibly the same bidder;
- one federal design behind every first-audit vs second-audit split. CT Logistics' current list keeps the split: 23.23% vs 38.61%;
- Old Dominion as the origin of the "~25% re-weighed" stories;
- AFS's 8.7% vs 8.0% in one document.

---

## §3 Arithmetic re-done

All sums were re-done from our own parse of each PDF (scripts in the scratchpad).

| Item | Researcher | Re-done | Note |
|---|---|---|---|
| Old Dominion bills per $1,000 | 2.03 (2025), 2.08 (2024) | 2.032, 2.082 | Correct. $492.01 and $480.29 confirmed in the raw release HTML. 11,072k shipments × $492.01 ≈ $5.45B, against total revenue of $5.50B |
| ABF bills per $1,000 | 1.88, 1.82 | 1.879, 1.822 | Correct (U-Pack caveat, §1) |
| Saia | 2.88 | 2.875 | Correct ($347.81 not re-fetched; from check AA) |
| Latex Foam, all-vendor total | $13,095,284.95, 408 rows | 408 rows; the 3 monthly columns sum to **$13,095,284.95** exactly | Correct |
| Latex Foam brokers / LTL / other | $193,332.74 / $1,898.41 / $181,701.88 | Same sums. The "other" set includes Bemak Traffic Services ($4,245), which **SAFER lists as a broker** | Brokers **$197,577.74 (52.4%)** |
| Latex Foam annualised | $1,528,673; 2.86% | $1,528,673; 2.86% of 2013 revenue; **3.58%** of the 2014 run-rate ($17.565M × 365/150 = $42.74M) | The window was also distressed: "CH Robinson Worldwide Inc. V Latex International … Collections … Pending" (SOFA 4a) |
| UGL vendors | 122 vendors, $6,754,624.96 | 121 vendor blocks, 1,056 lines, **$6,754,624.96**. Every block's lines equal its stated vendor total | Correct (121 vs 122 is immaterial) |
| UGL trucking | $454,619.70 (LTL $356,506.00; other $98,113.70); 379 lines; $1,199.52 a line; 0.834 per $1,000 | All identical. Whalen: 21 lines of $1,015.00 (7) and $1,041.25 (14) | Correct. Window 12/23/2010-3/23/2011 |
| UGL annualised | $1,843,735; 4.10% | Same; **4.75%** of the 2011 run-rate ($8.724M × 365/82) | Net sales are net of returns and rebates |
| Agway trucking | $464,932.52 | **$471,945.50** with North East Freightways ($7,012.98); $485,731.52 if Precision Delivery Solutions ($13,786.02) is trucking | Rows dated 4/7-7/5/2022 |
| Agway annualised; % of revenue | $1,885,560; 0.85% / 3.96% | **$1,914,001**; 0.86% of 2021; **4.02%** of the 2022 run-rate ($24,235,249 × 365/186 = $47,558,419) | The 2022 run-rate is correct |
| Top-3 share; payees to 80% | 52.4%, 42.5%, 51.8%; 6, 9, 7 | Same; Agway with the added payee 51.1%, 7 | Correct |
| Broker shares, six firms | 0.0, 11.9, 14.0, 16.7, 51.3, 74.9; median 15.4% | 0.0; Cycle Force **10.2-17.5**; Agway **13.8**; Sona **16.4**; Latex **52.4**; Imperial Toy **45.4-51.2** (65.1 if Atlas is a broker). **Median 15.1-16.9%**; pooled by dollars **23.1-24.5%** | §1 C-AN51. Cycle Force full trucking $127,106.68; Imperial Toy $286,278.35; Sona $124,211.07 |
| Minutes per bill at $36.79/hour | 3.77 ($2.31), 6.33 ($3.88), 3.85 ($2.36) | Same on the old prices. **Current: 4.44 ($2.72), 4.55 ($2.79), 7.45 ($4.57), 7.63 ($4.68).** At $25/hour: 6.7 ($2.79), 11.2 ($4.68) | Prices rose about 20.7% from 2019-20 to May 2026 on all six motor-freight lines checked, including the contingency shares |
| Special audit in auditor minutes | 8.27 | 8.27 (2019-20); 8.28 / 8.27 (current) | Unchanged |
| Price ÷ the model's $0.65 per invoice | 3.55×, 5.97× | Current: 4.3× (EDI), 7.2× (hard copy) | — |
| Vee Technologies | $53.66 a bill; 12.41% claimed vs "1.20%" errors | Same. The page writes "USD 25, 98,541.00" and "USD 3,22,491" in Indian digit grouping (= $2,598,541 and $322,491), and states "USD 6.66 being the average amount per bill" (322,491 ÷ 48,424 = 6.66) | The inconsistency stands. A $53.66 average is also implausibly low for an ocean bill: an unreliable case |
| Ascent | $2,700/week; $140,400/year; 5 h/week | Same | But the same sheet says "we save clients 50 hours per week" (§1) |
| Bestorq (new, from the Old Dominion paper) | — | Up to 30 flagged invoices a month at up to 25% of shipments ≈ 120 shipments a month **[our calc]** | Lead (§6) |

---

## §4 Concerns, unproven (verdict unchanged)

1. **Catch-up payments.** Distressed firms' 90-day payments may include old debts or missed weeks. Evidence of the risk exists (a C.H. Robinson collections suit against Latex Foam; Agway's single $102,842.57 Hub Group payment on day one), but we could not prove which payments were catch-up. C-AN45 and C-AN47 remain *verified* as payments; only the annualised reading is narrowed (C-AN48).
2. **Seasonality.** UGL's window (December to March) may be off-season for a coatings maker. Not tested.
3. **UPS at Latex Foam ($175,665.36)** may include UPS Freight LTL bills (UPS Freight operated in 2014). The payee line reads "UPS - Plan3707AN", which does not say.
4. **Fracht FWO ($87,349) at Latex Foam** is a forwarder. Part of it may be domestic trucking; it was excluded by both checks.
5. **The UGL "floor" of 0.83 bills per $1,000** assumes each payment line covers at least one invoice. Partial payments would break this; no evidence either way.
6. **Douglas Dynamics (C-AN29)** may be far larger than our segment; this was not evidenced here. Bestorq, described as "an industrial equipment supplier", fits better.
7. **GMG may never have sold a freight audit** under its list. A USAspending keyword search returned nothing even for a contract known to have orders, so the test failed.
8. **Atlas Transportation and Precision Delivery Solutions** could not be classed. SAFER lists several firms under those names or none.
9. **ATRI's detention figure (C-AN31)** comes from the trucking industry's research arm, which has a stake in documenting detention. The label change to *assumed* rests on its being driver self-report (stated in the release), not on this concern.

---

## §5 Full verdict table

Claims are listed in ID order. "Tests" key: 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search, 7 arithmetic.

| Claim ID | Tests | Verdict | Reason | Evidence (URL + quote) | New label |
|---|---|---|---|---|---|
| C-AN01 | 1 (sample) | KEEP-verified | Table found as stated | pitt.edu RFP 041725SS: "Annual Avg Spend … $434,000 11,646 11,532 114 240+" | *verified* |
| C-AN02 | 1 (sample) | KEEP-verified | Both quotes found | same: "Apply basic audit checks to identify duplicate charges or other anomalies."; "The service fee should be added to each line item (shipment)" | *verified* |
| C-AN03 | 1 (sample) | KEEP-verified | Found; no offshore clause seen | same: "Contractor may be asked to complete a data security assessment in coordination with the Pitt IT Third Party" | *verified* |
| C-AN04 | 1 (sample) | KEEP-verified | API record matches | api.usaspending.gov …NRCHQ7N15T0001…: "GSA REQUIRES THAT GBLS BE PRE-AUDITED BY AN OUTSIDE PARTY PRIOR TO PAYMENT"; total_obligation 2697.98 | *verified* |
| C-AN05 | 1 (sample) | KEEP-verified | Matches | …HQ042315F0008…: "PRE-AUDIT OF TRANSPORTATION BILLS (ARMY, AIR FORCE, NAVY AND DLA)"; 108251.13 | *verified* |
| C-AN06 | 1 (sample) | KEEP-verified | Matches | …SS001431176…: "THIRD-PARTY PREPAYMENT AUDITOR WHO AUDITS ALL MOTOR FREIGHT BILLS"; 4920.0 | *verified* |
| C-AN07 | 1 (sample) | KEEP-verified | Matches | …70Z02325F13320001…: "TO PROVIDE TRANSPORTATION AUDITING SERVICES FOR USCG NATIONAL CAPITAL REGION"; 4248.0 | *verified* |
| C-AN08 | 1, 5 (sample) | KEEP-verified | Matches. Its parent, 47QRAA19D007U, is CT Logistics' current schedule, whose list gives the share ceiling (C-AN10) | …47QMCB25F0002…: offers "4"; "SMALL BUSINESS SET ASIDE - TOTAL"; total_obligation 0.0 | *verified* |
| C-AN09 | 1, 2, 4, 5, 6 | NARROW | Superseded prices; "paper" is really hard copy or electronic copy | §1; gsaadvantage GS-23F-0095K list; current list: catalog-library-prod.s3-fips.us-east-1.amazonaws.com/pricelist/47QRAA19D007U/pricelist_47QRAA19D007U.xlsx: "Review Electronic Commerce Motor Freight bills … 2.72 \| 2.79" | *verified* (2019-20 and 2026-27 prices) |
| C-AN10 | 1, 2, 4, 5, 6 | NARROW | Superseded; federal bills are already pre-audited | §1; current list: "1st Audit Motor Freight \| P1 \| 22.66 \| 23.23" | *verified*; fit partly |
| C-AN11 | 1, 5, 7 | NARROW | Superseded | current list: "Motor Freight - Rate Auditor - per hour \| HR \| 111.51 \| 114.3" | *verified* |
| C-AN12 | 1, 2, 5 | NARROW | A contractor's statement, not a buyer's rule | GS-23F-0095K: "Point of production Cleveland, Cuyahoga County, Ohio"; current: "Contractor_Facility … Domestic" | *verified* (what it says) |
| C-AN13 | 1, 2, 4, 5 | NARROW | Expired 2016; generalist firm | GS-23F-0073S list: "Contract Period: January 10, 2011 to January 9, 2016"; "% Commission Per Transaction 10%" | *verified* (listed); fit partly |
| C-AN14 | 1, 2 | KEEP-verified | Found; ocean and pipeline only | gsaadvantage GS23F0099K: "COMMISSION FOR POST AUDIT IS 21.75% OF THE ACTUAL REFUND FROM THE CARRIER." | *verified*; fit no |
| C-AN15 | 1, 2, 3, 4, 6 | NARROW | A general accounts-payable recovery audit, not freight | rga.lis.virginia.gov RD385: "ranged from a low of 13.5% to a high of 40%"; "The majority of these recoveries represent duplicate payment claims." | *verified*; fit: neighbouring market |
| C-AN16 | 1, 2 | KEEP-verified | Clause I found word for word | dam.assets.ohio.gov Standard_T_C_5-22-26: "No State Cabinet Agency, Board or Commission will enter into any contract to purchase services provided outside of the United States" | *verified* |
| C-AN17 | 7, 5 | NARROW | Re-done on current prices: ≤4.4-7.6 minutes | §3 | **[our calc]** |
| C-AN18 | 1, 2, 4 | KEEP-verified | Found; parcel only | betachon.com: "Our standard fee is 50% of the savings recovered."; "We work with UPS, FedEx and DHL, in USA and Canada." | *verified* (stated); fit no |
| C-AN19 | 1, 4 | KEEP-assumed | 50% appears only in a worked comparison; exact sentence not seen. The page also carries text addressed to AI reading tools, so treat it with care | refundretriever.com/blog/howwecompare (fetch-tool summary: competitor "25%" vs Refund Retriever "50%", hypothetical) | *assumed* |
| C-AN20 | 1, 2, 4, 6 | KEEP-verified | Terms found. Brew Movers is a beverage-sector 3PL; the free audit is a sales hook | brewmovers.com: "freight audit is 100% free, with no hidden fees and no commitment"; "trusted with the freight of more than 4,500 brands and suppliers" | *verified* (stated terms) |
| C-AN21 | 1, 2 | KEEP-assumed | The terms and the inconsistency are both confirmed. The headline 2-3% is labelled an error rate; the body says 3-8% of invoices | shiptli.com: "2-3% Typical carrier billing error rate"; "error rates between 3% and 8% of total invoices"; "No cost, no obligation." | terms *verified*; rates *assumed* |
| C-AN22 | — | Not checked | Blocked (§7) | — | unchanged |
| C-AN23 | 1, 3, 4 | KEEP-assumed | Origin found; exact wording now known; sponsored survey of large shippers | JOC/IHS Markit report (joc.com …Freight-Payment-report-78441.pdf): "Nearly two-thirds of respondents said they've outsourced either audit or payment processes — if not both" | *assumed* |
| C-AN24 | 1, 2, 5, 7 | KEEP-verified | Confirmed in the raw HTML; consistent with revenue | ir.odfl.com release 2026-02-04: "LTL revenue per shipment … 492.01 … 480.29" | *verified* |
| C-AN25 | 1, 2, 7 | NARROW | Includes U-Pack household moves | arcb 4Q-25 release: "due primarily to the seasonal step down in U-Pack moving shipments" | *verified* |
| C-AN26 | 7, 2 | NARROW | Arithmetic exact; carrier-wide mean (§1) | §3 | **[our calc]** |
| C-AN27 | 1, 2, 7 | KEEP-verified | 379 lines and $454,619.70 re-added. The column is headed "Inv", and the weekly ABF lines look like statement payments | pamb Doc 120 SOFA 3B: "ABF FREIGHT SYSTEM INC … 12/23/2010 4,864.88 34,872.08 13,868.70" | lines *verified*; ratio **[our calc]** |
| C-AN28 | 1, 3, 4, 6 | KEEP-assumed | Found (in the page source); carrier's own framing. Counter-evidence: CarrierDirect's 10-15% | odfl.com white paper: "In the past several years, some shippers report 25 to 30 percent of their freight being re-rated." | *assumed* |
| C-AN29 | 1, 3, 4 | KEEP-assumed | Quotes found; selected success stories | same: "As much as 25 percent of our shipments were coming back with a re-weigh or re-classification"; "as many as 30 cases a month" | *assumed* |
| C-AN30 | 1, 2, 4, 6 | KEEP-assumed | Both figures found; a vendor's book; a dollar share | scg-lm …afs-logistics-wp-ltl-072424.pdf: "an average of 8.7% of total LTL spend in 2023, according to AFS customer data"; "reaching 8.0% by the end of 2023" | *assumed* |
| C-AN31 | 1, 2, 4 | KEEP-assumed | Found; driver self-report, carrier-side institute | truckingresearch.org 2024-09-10: "In 2023, drivers reported being detained in 39.3 percent of all stops." | *assumed* (was *verified as published*) |
| C-AN32 | 1, 3, 4 | KEEP-assumed | Origin found | JOC report: "Shippers reported an average invoice inaccuracy rate across all modes of 20.8 percent" | *assumed* |
| C-AN33 | 1, 4, 3 | KEEP-assumed | Found; vendor; same sheet claims 50 hours a week | ascentlogistics.com PDF: "it takes, on average, 1 minute and 30 seconds to audit each freight bill"; "between 4-6% of carrier invoices are incorrect" | *assumed* |
| C-AN34 | 7, 3 | NARROW | Box reconciles; sheet does not (§1) | same: "CLIENT TIME 5 hours per week"; "we save clients 50 hours per week" | **[our calc]** |
| C-AN35 | 1, 2 | KEEP-assumed | Found; ocean | veetechnologies.com case: "Average bills per day was in the range of 300 - 400 per person" | *assumed*; fit no |
| C-AN36 | 7 | KEEP-verified | Arithmetic re-done; inconsistency stands (§3) | same: "USD 3,22,491 was the claimed amount, with USD 6.66 being the average amount per bill" | **[our calc]** |
| C-AN37 | 1, 3 | KEEP-assumed | Found in the secondary compilation | stealthagents.com: "A disputed ocean invoice could require six to ten calls, with each call taking 10 to 15 minutes" | *assumed* |
| C-AN38 | 1, 4, 5 | KEEP-assumed | Found; vendor survey; no newer survey found | supplychainbrain.com: "Most LTL/Freight shippers currently use between two and five carriers in their operations." | *assumed* |
| C-AN39 | 1, 2, 3 | NARROW | Bemak is a broker; one Agway payee missed (§1) | safer.fmcsa.dot.gov USDOT 2215380: "Entity Type: BROKER … Power Units: 0" | *verified* lists; classes **[our call]** |
| C-AN40 | 7 | KEEP-verified | Re-done; Agway 51.1%, 7 with the added payee | §3 | **[our calc]** |
| C-AN41 | 1, 5 | KEEP-verified | Found | investors.arcb.com 2026-06-08: "Rates will increase by about 5.9 percent, although the effect on specific lanes and shipments may vary." | *verified* |
| C-AN42 | 1 | KEEP-verified | Found | arcb 4Q-25 release: "Customer contract renewals and deferred pricing agreements averaged a 5.0 percent increase during the fourth quarter." | *verified* |
| C-AN43 | 1 | KEEP-verified | Found | fedexfreight.com fuel table: "drops below 31.00% or rises above 75.80%, this fuel surcharge table will be updated" | *verified* |
| C-AN44 | 1, 2 | KEEP-verified | Found; unit not stated, as AN said | smc3.com 2021-12-06: "The prices vary by module and service level."; "CzarLite $800" | *verified* (stated) |
| C-AN45 | 1, 2, 7 | KEEP-verified | Every total re-added to the cent | ctb Doc 88: "$53,468,000.00 2013: Debtor Business Income"; "See Attached $13,095,284.95" | *verified* |
| C-AN46 | 1, 2, 7 | KEEP-verified | Re-added to the cent | pamb Doc 120: "$45,005,407.00 2010 Sales (net of returns, allowances and volume rebates)" | *verified* |
| C-AN47 | 1, 2, 7 | NARROW | Incomplete parse; missed payee; revenue collapse (§1) | deb Doc 131 p.15: "58498 NORTH EAST FRTWAYS DBA LAND AIR EXPRE 4/13/2022 4,483.26"; p.1: "24,235,249.00" | *verified* |
| C-AN48 | 7, 2 | NARROW | Denominator choice (§1) | §3 | **[our calc]** |
| C-AN49 | 1, 2 | NARROW | 76% not found; population identified | web.archive.org/web/20250617045727/…/trusting-others-with-your-data: "surveyed 158 U.S.-based finance executives last year about outsourcing" | *assumed* |
| C-AN50 | 7, 2, 3 | NARROW | Corrected shares and median (§1) | §3 | **[our calc]** (classes **[our call]**) |
| C-AN51 | 1, 2, 7 | DISCARD | Partial denominators (§1) | canb Doc 75: "3.110. JB HUNT TRANSPORT 9/6/2019 $11,236.61"; iasb Doc 1: "Online Freight Services 1/21-4/21 $9,212.40" | replace with §3 values |
| C-AN52 | 1, 3, 5, 6 | KEEP-assumed | Found; nothing newer (counter-search 2) | ttnews.com 2013-04-08: "now account for almost one-quarter of total LTL revenue, compared with no more than 2% in 1998" | *assumed* |
| C-AN53 | 1, 3, 5, 6 | KEEP-assumed | Found; presented by a carrier executive at a 3PL conference | dcvelocity.com: "About 40 percent of all LTL shipments are today billed through a 3PL, according to data from the American Trucking Associations (ATA) and the Georgia Center" | *assumed* |
| C-AN54 | 1 | KEEP-assumed | Found | ttnews.com: "revenue from 3PLs currently makes up about 26% of Southeastern's total revenue" | *assumed* |
| C-AN55 | 1, 3 | KEEP-assumed | Found. The Dynarates attribution is in the article itself, not only in a search summary | logisticsmgmt.com 2012: "makes up over 60 percent of LTL shipments according to Dynarates, a freight transportation consultancy" | *assumed* |
| C-AN56 | — | Not checked | Blocked (§7) | — | unchanged |
| C-AN57 | 1, 7 | KEEP-verified | Five amounts found; sum $1,898.41 | ctb Doc 88 attachment: "Estes Express Lines … $ 280.44" | *verified* |

**Body numbers that do not trace to a ledger row:**
- **§AN8's Agway "257 rows … 85 vendors … $2,814,444.07":** wrong (276 rows, 92 payee names, $2,984,427.55).
- **§AN1 T6, "Schedule contract 2000-2020":** omits that the same firm has held a current schedule since 2019, with a public price list.
- **§AN7, "6-9 changes a year":** an inference labelled **[our calc]**, resting on one ABF rate release and one quarter of ABF renewals.
- **§AN8 parcel figures (UPS $175,665.36, UPS $13,600.96, FedEx $1,492.04) and §AN4's "$1,480-5,936 a line":** not in the ledger, but they match the filings.

---

## §6 Counter-evidence and leads

**Counter-evidence (tied to claims)**
1. **CT Logistics' current federal price list** (contract 47QRAA19D007U, generated January 2026, found via the GSA eLibrary page for that contract). It gives prices by contract year; year 8 runs from 7 May 2026 to 6 May 2027:
   - hard copy $4.68 a bill;
   - EDI $2.79 a bill;
   - first audit 23.23%; second audit 38.61%;
   - special audit $15.76;
   - rate auditor $114.30 an hour.
   It ties to C-AN09, C-AN10, C-AN11, C-AN17 and C-AN08. The contingency shares now escalate about 2.5% a year: 22.66 → 23.23 → 23.81 → 24.41.
2. **CarrierDirect white paper, via Logistics Management, 26 January 2016** (logisticsmgmt.com/article/carrierdirect_white_paper_takes_deep_dive_into_benefits_of_dimensional_ltl): "roughly 20-to-30 percent of LTL shipments have dimensional exceptions", of which "50 percent" yield valid adjustments, so "10-to-15 percent of all LTL shipments". It ties to C-AN28 and C-AN29. *Assumed* (consultancy estimate).
3. **AFS blog, 5 September 2023** (afs.net/blog/rising-ltl-accessorial-fees/): "Last year at this time we were short paying 2.5% of the LTL invoices we processed. Now we're short paying 3.5 to 4%." This is an audit firm's own share of LTL invoices paid short. It ties to C-AN30 and A09-06, and to the model's 5% disputes. *Assumed* (vendor).
4. **The full payment lists of Imperial Toy, Cycle Force and Sona**, re-fetched from CourtListener. They tie to C-AN51 (§1).
5. **FMCSA SAFER entries:**
   - Bemak Traffic Services: broker;
   - R & R Freight Services (Wallingford, CT): carrier, 11 trucks;
   - Pace Motor Lines: carrier, 65 trucks;
   - Online Freight Services: carrier/broker, 0 trucks;
   - Landstar Global Logistics: carrier/freight forwarder, 1 truck.
   They tie to C-AN39, C-AN50 and C-AN51.

**Leads (not findings)**
1. **JOC 2020, Fig. 3 "Cost to Process an Invoice"** (self-reported, all modes, sponsored): outsourced $6.26; large shippers $10.74; in-house $18.32; small and mid-sized shippers $19.49. This bears on A09-04 and A09-07. Note the founders' rule: these are costs of staff time.
2. **Bestorq** (Old Dominion paper): one small manufacturer's accounting team flagged "as many as 30 cases a month" at up to 25% of shipments, which is about 120 LTL shipments a month **[our calc]**. It is a rare first-hand figure for A09-06 and A09-07.
3. **TLI's page states "$634,608 Audit Savings Recovered in 2025"** (whole client base). This could size a small audit book.
4. **Search-summary leads, not opened:**
   - Auditec Solutions: contingency "25%–50%" and "$1–$5 per invoice";
   - apexanalytix: accounts-payable recovery audit "20 to 30 percent";
   - Inbound Logistics (undated): post-payment providers keep "about 30 percent";
   - Warp: first-audit recoveries "LTL 3 to 7 percent, truckload 1 to 3 percent".
   All are vendors or trade press, and all would be *assumed*.
5. **The GSA 2025 post-payment audit task order (C-AN08)** sits under the contract whose list caps motor-freight first audits at 22.66% for May 2025 to May 2026 (the January 2026 list does not show the earlier year's rate). The awarded share may be lower; it is a question for the contracting officer.

**Counter-searches used (7)**
1. Contingency fee for LTL/TL freight audits: no primary price found; vendor ranges only.
2. Current broker/3PL share of LTL: nothing newer than 2013-14.
3. Independent reweigh and reclass rate: found CarrierDirect 2016 (counter-evidence 2).
4. Offshore freight-audit processing and mid-market acceptance: nothing on mid-sized private shippers; agrees with "Not answerable".
5. AFS/TD Cowen per-shipment dollar values: index levels only, no dollars.
6. A published price for a paid one-off assessment or look-back: none; agrees with AN.
7. Accessorial share of LTL spend: AFS 8.7% is the only measured figure; vendors' "20-30% of spend" appear to include fuel. Found counter-evidence 3.

---

## §7 Could not access

- **Capterra UK (C-AN22):** blocked (403) by curl and by the fetch tool; no Wayback copy.
- **Inbound Logistics (C-AN56):** blocked (403); no Wayback copy.
- **Treasury & Risk (C-AN49):** blocked (403) live; read through the Wayback copy of 17 June 2025, which lacks the 76% sentence.
- **Whether GMG ever sold freight audits:** the USAspending keyword search on schedule numbers returned nothing, even for a contract known to have orders. The method failed; this is inconclusive.
- **SAFER** could not resolve "Atlas Transportation" (several firms), "Precision Delivery Solutions" or "North East Freightways" (not found by name). The last is classed as trucking on its name alone ("FRTWAYS … LAND AIR EXPRE[SS]") **[our call]**.
- **Not re-fetched (carried from earlier checks):** Saia's $347.81 (check AA); check AD's nine small-firm LTL totals; Establish Davis's 3.68% (check X). The three AD filings used for broker shares *were* re-fetched.
