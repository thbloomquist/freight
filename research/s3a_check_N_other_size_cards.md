# S3a check N: sourced inputs for the 15 size cards that do not lean fail (evidence for K4 and K5)

- **What this is:** evidence for S3a ("settle the unknowns") in run 01. It covers the 15 cards whose K5 (size) or K4 (measurable) unknowns do not lean toward failing: C-02, C-04, C-05, C-06, C-08, C-10, C-11, C-12, C-17, C-18, C-19, C-20, C-21, C-22 and C-23.
  - For each card, it looks for neutral, sourced replacements for the judgement inputs and vendor inputs behind S2's savings pool (`research/selection_runs/run-01/2_knockouts.md` §4.1; `research/s2_check_K_savings_pools.md` §2).
  - It then re-runs the arithmetic.
- **Date:** 2026-09-15.
- **Status:** input to S3a; it decides nothing. Pass/fail calls are made in `research/selection_runs/run-01/3a_unknowns.md`.
- **Labels:**
  - *verified*: read at the source (a quote from the page, a value from a downloaded file or official table). Page extractions are marked as such.
  - *assumed*: a search snippet, secondary summary, vendor claim, memory, or blocked page. Vendor claims are always *assumed*.
  - **[our calc]** marks our own arithmetic; **[our call]** marks our own judgement.
  - **Affiliation flags.** A trade-association survey counts as a source, but it is always shown with who runs it. The associations used here:
    - OOIDA (owner-operators);
    - ATRI (research arm of the American Trucking Associations);
    - TIA (freight brokers);
    - CRF (credit managers).

**The K5 desk rule (C13), restated [our calc]:**
- **Pass:** 10% of the savings range's low end reaches $25M, i.e. a low end of $250M or more.
- **Fail:** 35% of the high end is clearly short of $25M, i.e. a high end well under about $71M.
- **Unknown:** anything in between.
- **The central fee pool** is 20% × the geometric mean of low and high. It only orders the work.

**How to read the numbers:**
- **Same method as check K.** Each savings pool = cost base × avoidable share × share software could remove. The low end multiplies all the low inputs; the high end multiplies all the high ones.
- **"Old"** is S2's range. **"New"** is the same formula with the sourced inputs swapped in.
- **Sensitivity lines.** Where a sourced input only bounds one end of a range, or a swap is debatable, a sensitivity line shows the other reading.
- **Dollars** are yearly, in current dollars, and not adjusted for inflation.

**Freight words used here** (others are in `1_candidates.md` and check K):
- **LTL (less-than-truckload):** carriers that combine many small shipments (a few pallets each) in one trailer, routing them through terminals.
- **Claims ratio:** cargo claims paid ÷ the carrier's revenue.
- **Reweigh / reclass:** an LTL carrier re-measures a shipment at its dock and bills a higher weight or freight class than the shipper declared.
- **Factoring:** a carrier sells an unpaid freight invoice to a finance firm (a "factor") for cash now, at a discount (the factor's fee).
- **Dispatch service:** an outside firm that finds and books loads for an owner-operator for a % of the load's gross pay.
- **Drayage:** short truck moves of containers between a port terminal and a nearby warehouse or rail yard.
- **Turn time:** minutes from joining the queue outside a port terminal to leaving through the exit gate.
- **TEU:** a twenty-foot equivalent unit, a standard container size. A typical box is about 1.8 TEU **[our call]**, as in check K.
- **Demurrage and detention (D&D):** daily charges for leaving a container at the terminal too long (demurrage) or keeping it out too long (detention).
- **Charge complaint:** since the Ocean Shipping Reform Act of 2022 (OSRA 2022), a shipper can send a disputed D&D invoice to the Federal Maritime Commission (FMC). The carrier must then prove the charge is lawful, or refund or waive it.
- **Entry summary (CBP Form 7501):** the customs declaration an importer or its broker files for a formal entry. Formal entries are the ones over $2,500 in value, plus some others.
- **Information collection request (ICR):** the burden estimate an agency files with the Office of Management and Budget (OMB) under the Paperwork Reduction Act. It gives responses per year and minutes per response.
- **Non-trade deduction:** money a retailer deducts from a supplier's invoice for shortages, late or early delivery, labelling or pricing problems. "Trade" deductions are for promotions.
- **OTIF (on time, in full):** a retailer's delivery rule, with fines for late or short cases.
- **Nonemployer:** a business with no paid employees, such as a one-truck owner-operator.

---

## 1. Summary table

| Card | Unknowns in this check | S2 range → new range (central fee pool) | Inputs replaced (old → new) | Still [our call] | K4 finding | Sources |
|---|---|---|---|---|---|---|
| C-22 Drayage dispatch | K4, K5 | $67-268M ($27M) → **$69-274M ($27M)**. Sensitivity with 0.25 h excess: $34-274M ($19M) | Container volume: 28.2M TEU imports (snippet) + 12M TEU exports [our call] → 30.2M + 11.0M loaded TEU in 2022 (USACE via BTS, *verified*) | Excess time 0.5 h; $75-100 an hour; removable 5-15%; 1.8 TEU a box; 2 moves; 20% on-dock rail | Partly settled: volume from named data. The time input is still a dated trade-press figure, and no current turn time at source was reachable | N-N01, N-N02, N-N03, N-N04 |
| C-10 Cargo claims | K4, K5 | $70-370M ($32M) → **$62-442M ($33M)** | LTL base $64B (*assumed*) → $65.7B Census 2022 receipts (*verified*). Claims ratio 0.35% (consultancy) → 0.3-0.5%, anchored on five carriers' filings of 0.09-0.54% (*verified*) | Filing and denial rates (vendor); truckload ratio 0.05-0.15%; small and mid-sized share 30-50%; removable 20-40% | Still ?: the step from claims paid to loss left unrecovered rests on one vendor survey | N-N07 to N-N13, N-K21 |
| C-21 Container D&D | K5 | $93-279M ($32M) → **unchanged** | None. New FMC data (*verified*): formal charge complaints refunded or waived "more than $5.8 million" in three years, about 0.06% of charges [our calc] | Removable 10-30%. The only sourced bound, 22.5% uncollected in 2020-22, sits inside it | ✓ (S2) | N-N18, N-N19, N-K01 |
| C-04 Dock appointments | K5 | $0.14-0.36B ($46M) → **$84-439M ($38M)** | Detention paid by facilities: 40% (vendor) → at most 47%, from ATRI's "paid for fewer than 50 percent" of invoices (*verified*; ATRI flag). Wait cut: 10-25% [our call] → 9.3-25.8%, a potential from a port-terminal study (*verified*) | Low end of the paid share (25%); applying a port study to warehouse docks | ✓ (S2) | N-C24, N-N02 |
| C-20 Import entries | K5 | $0.10-0.64B ($50M) → **$104-694M ($54M)**. Sensitivity with CBP's burden floor: $13-694M ($19M) | Entries: 31.9M formal (FY2023) → 34.7M (FY2025, *verified*). Cost per entry: $100 high end now sourced (World Bank documentary compliance cost, *verified*). CBP's burden estimate, 5 minutes an entry, gives a floor of about $5 (*verified*; [our calc]) | $40 low end; 25-40% small and mid-sized share; removable 30-50% | ✓ (S2) | N-H22, N-N05, N-N06 |
| C-06 Spot loads | K4, K5 | $0.06-1.2B ($55M) → **$51M-1.10B ($47M)** | Gross per one-truck carrier: $150-250k [our call] → $123k (Census nonemployer average, *verified*) to $222k (OOIDA own-authority average, *verified*; OOIDA flag) | Share using dispatch services, 10-30% (no source found); fee 5-10% (vendor); removable 30-60% | Still ?: the input that swings the pool most (dispatch use) has no source | N-D05, N-N17, N-F39 |
| C-08 Vetting and fraud | K4, K5 (K7 open for S5) | $0.15-0.59B ($59M) → **$91-690M ($50M)** | Theft: $734M (all 2024 crime events × average) → $454M (2024 confirmed thefts) to $725M (2025) (CargoNet, vendor, *assumed*). Fraud: 0 to "the same again" [our call] → 0 to $1.0B (TIA, *assumed*; TIA flag) | Share prevented by vetting 20-40%; the overlap of fraud and theft | Still ?: vendor theft data, an association fraud estimate with no stated method, and FMCSA says it lacks the data | N-N24 to N-N27 |
| C-12 Parcel audit | K4, K5 | $0.10-0.83B ($59M) → **$19-202M ($12M)** | Parcel spend: 5-10% of small sellers' receipts [our call] → Census retail survey line for e-commerce firms' purchased transportation, shipping and warehousing, about 1.8% of receipts (2017 share applied to 2022, *verified*; [our calc]) | Small-firm share of that spend 23.6-40%; parcel share 50-80%; recovery 2-5% (vendor); removable 50-80% | Partly: the cost base now comes from named Census data (probably a floor). The recovery rate is still vendor-only | N-N20, N-N21, N-J28, N-N30 |
| C-11 LTL disputes | K4, K5 | $0.10-0.90B ($60M) → **$105-920M ($62M)** | LTL base $64B (*assumed*) → $65.7B (Census 2022, *verified*) | Small shippers' share 20-40%; avoidable 2-5%; removable 40-70%. No neutral reweigh or reclass rate exists | Could now pass: the cost base is neutral, and the avoidable share is a K5 judgement, as on C-09 | N-N13, N-N12 |
| C-23 Intl quoting | K5 | $127-707M ($60M) → **unchanged** | None. O*NET task frequencies (*verified*) fit the 15-30% time share but do not measure it | Forwarding share 30-50%; time quoting 15-30%; removable 30-50% | ✓ (S2) | N-N28 |
| C-05 Carrier payment | K4, K5 | $0.07-1.4B ($62M) → **$99-798M ($56M)** | Factored share: 20-40% [our call] → 23-28% (OOIDA surveys, *verified*; OOIDA flag). Fee: 1-4% (vendor) → 1.29-3.2% (Triumph's filed discount rate, *verified*; OOIDA members' average fee) | Removable 15-40% | Could now pass: share and fee both come from named data | N-N14 to N-N17 |
| C-18 Warehouse bills | K4, K5 | Under 500 staff $110-900M ($63M); under 20 staff $28-225M ($16M) → **unchanged** | None. No neutral leakage rate found | Leakage 1-5%; removable 50-80% | Still ?: leakage is vendor-only | — |
| C-02 Load status | K5 | $0.18-0.73B ($73M) → **unchanged** | None. O*NET: tracking is a core daily task for 79% of cargo agents (*verified*). An equal split of core tasks gives about 22% of time [our call], which fits S2's low end | Time on status 20-40%; removable 30-60% | ✓ (S2) | N-N28 |
| C-19 OTIF and deductions | K4, K5 | $0.11-1.44B ($80M) → **$56-480M ($33M)** | Invalid deductions and avoidable fines: 0.5-1.5% of sales [our call] → non-trade deductions at a median of ¼-½% of sales (CRF survey, *verified*; CRF flag) | Removable 20-40%; treating all non-trade deductions as addressable | Could now pass: the rate comes from a named survey (association-flagged) | N-N29 |
| C-17 Inbound control | K4 only | K5 ✓ in S2 ($0.51-5.3B). Census-base sensitivity: low end $0.27-0.33B, still ≥ $250M | None for the overpay rate. Census trucking receipts give a neutral cross-check of the base | Overpay 15-30% (vendor); inbound share (vendor); uncontrolled share; mid-sized share; removable | Still ?: the overpay rate is vendor-only | N-N13, N-N22, N-N23 |

**What the table shows:**
- **No card's sourced inputs push its range across a K5 line.** All 14 K5 cards stay unknown; C-17 stays a pass.
- **Central fee pools that move below $25M:**
  - **C-12, from $59M to $12M.** The Census line puts e-commerce firms' spend on purchased transportation, shipping and warehousing at about 1.8% of receipts, not the 5-10% S2 assumed.
  - **Two sensitivity readings:** C-20 falls to $19M with CBP's 5-minute burden floor, and C-22 to $19M with a 0.25-hour excess.
- **Centrals that fall but stay above $25M:** C-19 ($80M → $33M), C-04 ($46M → $38M), C-08 ($59M → $50M), C-06 ($55M → $47M) and C-05 ($62M → $56M).
- **The removable share is still our judgement on all 15 cards.** No neutral source measured what software removes, as S2 found (`2_knockouts.md` §4.1).
- **A correction to S2's arithmetic for C-08** (§2.7): the 2024 theft figure multiplied all crime events by the average theft value.

---

## 2. Card by card

Cards are in the brief's order, closest to a K5 line first.

### 2.1 C-22 · Port drayage dispatch (K4, K5)

**S2's build** (check K):
- **Volume:** 28.2M TEU of imports in 2024 (N-K32, snippet, *assumed*), plus 12M TEU of loaded exports **[our call]**.
  - 22M boxes × 2 terminal moves × 80% (after on-dock rail) = 35.7M truck transactions.
- **Excess time:** 0.5 hour a transaction **[our call]**. It was anchored on the Harbor Trucking Association's 69-minute average against 35 minutes at the best terminal (Nov 2019, via Transport Topics, N-K19, *assumed*).
- **Cost:** $75-100 a truck hour **[our call]**.
- **Removable share:** 5-15% **[our call]**.
- **Pool:** $67-268M.

**Volume, now at source:**
- The BTS *Port Performance Freight Statistics: 2025 Annual Report* (N-N01, *verified*): "In 2022, 110 U.S. ports handled 45.7 million loaded TEUs … Ten percent of the TEUs were domestic movements, 66 percent were imports, and 24 percent were exports." The data are Army Corps of Engineers (USACE) data, special tabulation of July 2024.
- That is **30.2M TEU of loaded imports and 11.0M TEU of loaded exports** **[our calc]**. It replaces both the snippet and the export guess.
  - 41.1M TEU ÷ 1.8 = 22.85M boxes; × 2 moves × 0.8 = **36.6M truck transactions** **[our calc]**.
- **Caveats:**
  - 2022 was a high-import year.
  - The 28.2M TEU for 2024 came from another compiler and is not the same series.
  - The BTS 2026 report, which would carry newer USACE data, was blocked (§5).

**Turn time: nothing current at source.**
- **At source, none:**
  - The BTS 2025 report has no turn-time section (full text searched).
  - The 2026 report was blocked.
  - The Port Optimizer site (LA/LB) shows no public figures.
- **Secondary and snippets only:**
  - The Harbor Trucking Association measured a July 2017 combined LA/LB average of "90 minutes". Terminals ranged from 38 to 122 minutes, and "24% of the total truck trips took more than two hours" (via Transport Topics, 15 Aug 2017, N-N03, *assumed*).
  - Snippets for 2025-26 put Long Beach Container Terminal's gate turn time at "45 – 51 minutes, depending on the shift" (Hapag-Lloyd operational update; page returned 403). Pier 400 averages "roughly 30 minutes per stop" (N-N04, *assumed*).
- **So turn times may now be well below 2019's 69-minute average,** and the 0.5-hour excess may be high. The sensitivity line uses 0.25 hour at the low end.

**Removable share: a university study bounds it but does not replace it.**
- USC/METRANS (Giuliano and O'Brien, final report, Feb 2008; LA/LB data from 2004-05; N-N02, *verified*) found "there is no evidence that the appointment system affected queuing at marine terminal gates."
- It also modelled the potential if terminals gave appointment trucks priority entry and had the cargo ready. The saving per turn is 9.3% (queue only), 17.5% (plus 5 minutes off the transaction) and about 25% (plus 10 minutes), for container pick-ups.
  - But "15% of imports equals about 6% of all gate moves, so time savings are small relative to total turn time of all moves."
- **What this means for C-22:** these are terminal-side savings, beyond a drayage dispatcher's reach. The study supports a low end near zero for changes on the dispatch side alone. The 5-15% stays **[our call]**.

**Savings pool [our calc]:**
- **Old:** 35.7M × 0.5 h × $75 × 5% = **$67M**; 35.7M × 0.5 h × $100 × 15% = **$268M**. Central $27M.
- **New:** 36.6M × 0.5 h × $75 × 5% = **$69M**; 36.6M × 0.5 h × $100 × 15% = **$274M**. Central **$27M**.
- **Sensitivity** (excess 0.25-0.5 h): **$34-274M**, central **$19M**.
- **K5: unknown either way.**

**K4:**
- The count side now comes from named neutral data.
- The time side still rests on dated trade-press measurements.
- No current turn time at source was reachable, after three tries: the BTS 2026 report, Port Optimizer, and the Port of Long Beach's data platform.

*K11 is not in this check.*

### 2.2 C-10 · Cargo loss and damage claims (K4, K5)

**S2's build** (check K):
- **LTL claims paid:**
  - LTL spend: $64B (CSCMP via FreightWaves, N-K22, *assumed*).
  - Claims ratio: 0.35% (a consultancy index, N-K03, *assumed*).
  - So $224M paid.
- **Gross-up to the loss owed:** about 50% of eligible claims filed, and 50-60% of LTL claims denied (vendor survey, N-K21, *assumed*). That makes $1.0B eligible and $0.78B unrecovered.
- **Truckload:** $387B × 0.05-0.15% **[our call]** gives $0.36-1.08B unrecovered.
- **Shares:** small and mid-sized shippers 30-50%; removable 20-40% (both **[our call]**).
- **Pool:** $68-371M.

**LTL base, now neutral:**
- 2022 Economic Census receipts of LTL carriers (NAICS 484122): **$65.69B** (N-N13, *verified*; file EC2248BASIC).
- It replaces CSCMP's $64B; the two agree within 3%.

**LTL claims ratio, now from filings** (all *verified*):

| Carrier | Ratio | Period | Filing |
|---|---|---|---|
| Old Dominion | "a cargo claims ratio of 0.1%" | 2025 | FY2025 10-K (N-N07) |
| XPO | "a damage claims ratio of 0.3%" | 2025 | FY2025 10-K (N-N08) |
| Saia | "our cargo claims ratio was 0.54%" | Q3 2025 | 8-K (N-N09) |
| TFI International | "0.5% for US LTL" | Q4 2023 | 6-K (N-N10) |
| Forward Air | "0.09%" | Q4 2023 | 8-K (N-N11) |

- **The definitions differ.** Saia's CEO: "our cargo claims ratio is a GAAP [derived] number. So, I'm not exactly sure how everybody else calculates it" (N-N09).
- **We use 0.3-0.5%** **[our call, anchored on the filings]**. The best-in-class 0.1% belongs to the largest carrier and one niche carrier; small LTL carriers are unlikely to match it.
- **If the whole filed spread (0.09-0.54%) were used,** the pool would be $35-454M (central $25M).

**Truckload: no ratio exists in filings.**
- The FY2025 10-Ks of Werner and Knight-Swift mention cargo claims only as a self-insured category. EDGAR full-text search also covered Heartland, Schneider and Marten (N-N12). The 0.05-0.15% stays **[our call]**.
- Census 2022 receipts of truckload carriers (484121) are **$172.7B** (N-N13, *verified*), against CSCMP's $387B. CSCMP's figure covers more carrier types, and the census leaves out nonemployers.
- If the census figure were the low base, the truckload low would fall from $360M to $160M and the pool's low end to $50M (central $30M).

**Filing and denial rates:** still one vendor survey (N-K21). No neutral source was found (§5).

**Savings pool [our calc]:**
- **LTL paid:** $65.69B × 0.3-0.5% = $197-328M.
- **LTL unrecovered:** paid × (1 ÷ (0.5 × 0.45) − 1) = paid × 3.44, which is $679-1,131M.
- **Plus truckload:** $360-1,080M.
- **Total unrecovered:** $1.04-2.21B.
- **Pool:** × 30% × 20% = **$62M**; × 50% × 40% = **$442M**. Central **$33M**.
- **K5: unknown.**

**K4:** still ?. The base and the paid ratio are now neutral. The step from claims paid to loss left unrecovered, which makes most of the pool, rests on one vendor survey.

*K11 is not in this check.*

### 2.3 C-21 · Container demurrage and detention (K5)

**S2's build:**
- The FMC counts about $15.4B collected in five years (N-F31, *verified*), so $3.08B a year.
- × 30.2% for small and mid-sized importers (N-E18) = $0.93B.
- × 10-30% removable **[our call]** = **$93-279M**.

**New FMC evidence** (all *verified*):
- **Formal charge complaints** (FY2026 Congressional Budget Justification, May 2025, N-N18):
  - "From the start of FY 2025 to date, the FMC received 209 charge complaints. Of those, 118 were appropriate for the charge complaint process and assigned for investigation. The total amount of charge complaints refunded or cancelled during this period has been $2,564,931.36."
  - "In the three years since the enactment of OSRA 2022, more than $5.8 million in fees have been voluntarily waived or refunded under the new charge complaint process."
  - That is about $1.9M a year against about $3.08B collected: **roughly 0.06%** **[our calc]**. The formal channel is not where the savings are.
- **The 2024 billing final rule** (N-N19) restates only "approximately $8.9 billion … charged … and collected roughly $6.9 billion" for 2020-22. That is **22.5% uncollected** **[our calc]**, the same statistic as N-G01. The rule gives no dispute counts, waiver rates or small-entity counts.
- **The FMC D&D page** (N-K01, re-read): "Quarter 1 – 2025 saw declines in billings and collection, 24% and 19% respectively …, with D&D waived up-ticking slightly by 7%." The FMC collects waiver data from the carriers but publishes no dollar amounts.
- **The share borne by small and mid-sized importers:** no FMC figure was found. The 30.2% import-value share stays.

**Result:**
- **No input replaced.** The only sourced bound, 22.5% uncollected, comes from the 2020-22 crisis and sits inside the 10-30% range. Uncollected also includes charges that were simply unpaid.
- **The removable share would have to come from two places,** which only S5 can measure:
  - avoidance: getting the box out before the free days run out;
  - informal waivers.
- **Range unchanged: $93-279M, central $32M. K5: unknown.**

*K11 is not in this check.*

### 2.4 C-04 · Dock appointments (K5)

**S2's build:**
- Carriers' direct detention cost: $3.6B (ATRI via N-C24).
- × about 40% billed and collected (N-D34, vendor, *assumed*) = $1.44B.
- × 10-25% of waiting cut by appointments **[our call]** = **$0.14-0.36B**.

**Detention that facilities pay:**
- ATRI's release (10 Sep 2024; N-C24, re-read, *verified* page extraction; ATRI flag): "While 94.5 percent of fleets charge detention fees, they are paid for fewer than 50 percent of those invoices." Trade press repeats the sentence (TheTrucker, Supply Chain 24/7).
- **So facilities pay at most 94.5% × 50% ≈ 47% of the detention cost** **[our calc]**. This is an upper bound, because not every detention is invoiced.
- It replaces the vendor's 40%. The low end, 25%, is **[our call]**: about half invoiced and half of those paid.
- ATRI's full report, which might give an exact rate, sits behind a registration form (§5).

**Effect of appointments on waiting:**
- METRANS (N-N02, *verified*) modelled a potential of **9.3-25.8%** less time per appointment turn, if appointment trucks get priority and cargo is ready.
- At LA/LB it observed no effect, because terminals did not give appointments priority.
- This replaces the 10-25% **[our call]** with a sourced potential. Two caveats:
  - It is a port-terminal study from 2004-05, used as an analogy for warehouse docks **[our call]**.
  - It shows the saving depends on the facility actually honouring appointments.

**Savings per site** (detention paid per facility, overtime): no neutral figure was found.

**Savings pool [our calc]:**
- **Base:** $3.6B × 25-47% = $0.90-1.70B.
- **Pool:** × 9.3% = **$84M**; × 25.8% = **$439M**. Central **$38M**.
- **Keeping S2's 40%:** $134-372M, central $45M.
- **K5: unknown either way.**

*K11 is not in this check.*

### 2.5 C-20 · Import entries for small importers (K5)

**S2's build:**
- 31.9M formal entry summaries (FY2023, N-H22) × 25-40% from small and mid-sized importers **[our call]** = 8.0-12.8M.
- × $40-100 preparation cost **[our call]** × 30-50% removable **[our call]** = **$0.10-0.64B**.

**Volume** (CBP trade statistics, N-H22 re-read; page updated 24 Aug 2026; *verified* page extraction):

| Fiscal year | Total entry summaries | Informal | Formal **[our calc]** |
|---|---|---|---|
| FY2023 | 36,692,525 | 4,763,303 | 31,929,222 |
| FY2024 | 38,362,713 | 5,164,046 | 33,198,667 |
| FY2025 | 50,084,153 | 15,404,788 | **34,679,365** |
| FY2026 to date | 92,827,312 | 63,239,269 | 29,588,043 |

- The jump in informal entries follows the end of the $800 de minimis exemption on 29 Aug 2025. Low-value parcels now need entries.
- **We use FY2025's 34.7M formal entries.** × 25-40% = 8.7-13.9M.

**Cost per entry.** Two neutral figures now bracket S2's range:
- **World Bank, *Doing Business* 2016-2020 (DB2020 dataset, N-N06, *verified*):**
  - For the US (New York and Los Angeles alike): "Cost to import: Documentary compliance (USD)" = **100**; time 7.5 hours.
  - Border compliance: $175 and 1.5 hours.
  - "Documentary compliance" covers "obtaining documents, preparing documents, processing documents, presenting documents, and submitting documents" (archive page).
  - This sources the **$100 high end**. The World Bank ended the series in 2021 (*assumed*, memory), and it prices one standard shipment.
- **CBP's burden estimate** (ICR for Form 7501, OMB 1651-0022; Federal Register notice of 25 Mar 2024 via govinfo; N-N05, *verified*):
  - "7501 Formal Entry (Electronic submission) … Estimated Number of Total Annual Responses: 23,133,408 … Estimated Time per Response: 5 minutes." Paper filing takes 20 minutes; with the softwood-lumber form, 40 minutes.
  - At the cargo-and-freight-agent mean wage ($57,230; N-K09) that is $2.29 an entry for wages alone, or **about $3-5** with overhead **[our calc; our call on overhead]**.
  - It is CBP's estimate of the time to complete and file the form. It cannot include the classification and valuation work a broker does, so it is a floor, not a preparation cost **[our call]**.
- **Customs-broker fee levels:** no neutral source was found (§5). Vendor price guides say $100-250 an entry (*assumed*, not used).
- **The $40 low end stays [our call].**

**Savings pool [our calc]:**
- **New:** 8.67M × $40 × 30% = **$104M**; 13.87M × $100 × 50% = **$694M**. Central **$54M**.
- **Sensitivity** (CBP's floor of $5 as the low input): **$13-694M**, central **$19M**.
- **K5: unknown either way.**

*K11 is not in this check.*

### 2.6 C-06 · Matching spot loads with small carriers (K4, K5)

**S2's build:**
- 274,660 one-truck carriers (N-F02).
- × 10-30% using dispatch services **[our call]**.
- × $150-250k gross **[our call]**; unlabelled in S2.
- × fees of 5-10% (N-F39, vendor).
- × 30-60% removable **[our call]**.
- **Pool:** $0.06-1.2B.

**Gross revenue per carrier, now sourced:**
- **Low: $123,400** **[our calc]**. Census Nonemployer Statistics 2022 counts 914,821 truck-transportation nonemployers with $112.9B of receipts (N-D05, *verified*). This is a neutral average, and a low one: it includes part-timers and leased-on drivers who do not book their own loads.
- **High: $222,280.** The OOIDA Foundation's 2022 Owner-Operator Member Profile Survey (N-N17, *verified*; OOIDA flag; up to 488 responses): "For owner-operators under their own authority, the average gross income was $222,300." The members' overall average is $258,119.
- $123-222k replaces the $150-250k.

**Share using dispatch services: not found** after three tries (§5).
- The nearest data, OOIDA 2022: own-authority members get 32% of their business from brokers, 23% from load boards, 22% from shippers, 2% from digital matching and 21% from "other". None of it is dispatch-specific.

**Fees:** still vendor (N-F39).

**Savings pool [our calc]:**
- 274,660 × 10% × $123.4k × 5% × 30% = **$51M**.
- 274,660 × 30% × $222.3k × 10% × 60% = **$1,099M**.
- Central **$47M**. **K5: unknown.**

**K4:** still ?. The dispatch-use share swings the pool 3× and has no source.

*K11 is not in this check.*

### 2.7 C-08 · Carrier vetting and freight fraud (K4, K5; K7 noted)

**S2's build:**
- Cargo theft: $733.6M = 3,625 incidents × $202,364 (N-C23).
- Plus fraud of 0 to "the same again" **[our call]**. Total $0.73-1.47B.
- × 20-40% prevented by vetting **[our call]** = **$0.15-0.59B**.

**Theft** (Verisk CargoNet, *2025 Supply Chain Risk Trends Analysis*, 21 Jan 2026; N-N24; read at the source, but *assumed* because CargoNet is a vendor):
- **2024:** 3,607 "supply chain crime events", of which **2,243 confirmed cargo thefts**, averaging $202,364.
- **2025:** 3,594 events and **2,646 confirmed thefts**, averaging $273,990. Estimated losses were "~$725 million".
- **Correction to S2 [our calc].** S2 multiplied all crime events by the average theft value. Confirmed thefts × the average gives **about $454M for 2024**, not $734M. That matches the ~$455M for 2024 in coverage of the 2025 report (snippet).
- **We use $454M (2024) to $725M (2025).** Theft rose 60% in a year.

**Fraud beyond theft:**
- **TIA** (TIA flag): "Brokerage fraud is costing brokers, carriers, shippers and consumers $800 million or more." This was said by TIA's CEO in testimony to a House subcommittee (via Trucking Dive, 18 May 2023; N-N25, *assumed*: secondary, and no method is stated).
- **Snippets** attribute two more ranges to TIA (N-N26, *assumed*):
  - "$500 million to $1 billion" a year for fraud, including double brokering and shipment diversion;
  - "$700 million to $1 billion" for double brokering alone.
- **The regulator:** FMCSA's July 2024 report to Congress on unlawful brokerage says the agency lacks the data to quantify the problem (via Land Line, N-N27, *assumed*; FMCSA's PDF returned 403).
- **Not used:** NICB's "up to $35 billion" (snippet), because it covers all supply-chain crime. FBI cargo-theft data could not be reached in a usable form (§5).
- **Overlap:** TIA's "shipment diversion" is theft by fraud, which CargoNet also counts. So the low end is theft only, and the high end adds $1.0B of fraud **[our call]**.

**Savings pool [our calc]:**
- $454M × 20% = **$91M**.
- ($725M + $1,000M) × 40% = **$690M**.
- Central **$50M**. **K5: unknown.**

**K4:** still ?. Theft rests on a vendor; fraud rests on an association estimate with no method; and the regulator says it has no data.

**K7:** the saving is mostly risk avoided. It stays open for S5, noted only.

### 2.8 C-12 · Parcel invoice audit for e-commerce sellers (K4, K5)

**S2's build:**
- Receipts of e-commerce firms under 500 staff: $878.7B × 23.6% = $207B (SUSB, N-D04).
- × 5-10% spent on parcel **[our call]**.
- × 2-5% recoverable (N-F52, N-F53, vendor).
- × 50-80% removable **[our call]**.
- **Pool:** $0.10-0.83B.

**A neutral cost base** (Census Annual Retail Trade Survey, detailed operating expenses, collected only in years ending in 2 and 7):
- **2017** (N-N21, *verified*): electronic shopping and mail-order houses (NAICS 4541) spent **$8,095M** on "Purchased Transportation, Shipping, and Warehousing Services". That is **4.9%** of their $163,547M operating expenses. All retail: $21,393M (1.8%).
- **2022** (N-N20, *verified*): the 4541 line is suppressed for quality ("S"). Total 4541 operating expenses were **$318,582M**.
- **At the 2017 share, 2022 ≈ $15.8B** **[our calc]**. That is **about 1.8% of 454110 receipts** ($878.7B), against S2's 5-10%.
- **Caveats:**
  - Employer firms only.
  - Firms that book outbound shipping inside cost of goods sold would not report it on this line, so the figure may be low **[our call]**.

**Getting from that line to small sellers' parcel spend:**
- **Firms under 500 staff:** 23.6% (their receipts share, N-D04) to 40% **[our call]**. The higher bound allows for small sellers, which own no delivery network, spending more per dollar.
- **Parcel's share:** 50-80% **[our call]**. Parcel carries 65.3% of 4541 shipment value (CFS 2022, N-E02).
- **Result:** $1.86-5.05B of parcel spend **[our calc]**, against S2's $10.4-20.7B.

**Recovery rates:** still vendor (2-5%). No neutral source was found.

**Carriers' late-delivery guarantees:**
- **FedEx** reinstated its money-back guarantee from 12 Feb 2026 for listed express services only; "all other FedEx® services will remain suspended until further notice" (N-J28, *verified* in check J).
- **UPS** restored it in April 2021 for air and international express only. It "has not restored money-back guarantees on any of its other product lines" (FreightWaves, 5 Apr 2021, N-N30, *assumed*: trade press). UPS's current guarantee page returned "Access Denied", so the 2026 status is not confirmed.
- **Small sellers ship mostly by ground** (*assumed*). So late-delivery refunds are largely closed to them, and the recoverable share leans to its low end. Refunds for billing errors, such as address corrections, dimensional weight and duplicates, remain.

**Savings pool [our calc]:**
- **New:** $1.86B × 2% × 50% = **$19M**; $5.05B × 5% × 80% = **$202M**. Central **$12M**.
- **Strict sourced points** (23.6% and 65.3% as single values): $24-97M, central $10M.
- **K5: still unknown,** since the high end is over $71M. **The central is now under $25M.**

**K4:** partly settled. The cost base now rests on named Census data, probably a floor. The recovery rate, the reason for S2's "?", is still vendor-only.

### 2.9 C-11 · LTL class, reweigh and reclass disputes (K4, K5)

**S2's build:**
- LTL spend: $64B (N-K22, *assumed*).
- × 20-40% from small shippers **[our call]**.
- × 2-5% avoidable reweigh, reclass and extra-service overcharges **[our call]**. Vendors say 10-20% (N-G23).
- × 40-70% removable **[our call]**.
- **Pool:** $0.10-0.90B.

**LTL base:** Census 2022 receipts for 484122 are **$65.69B** (N-N13, *verified*). This replaces the assumed $64B.

**Correction rates** (how often reweighs and reclasses happen, and what they add): no neutral source.
- EDGAR full-text search for "reweigh" (2023-26) finds no LTL carrier filing (N-N12).
- ArcBest's 10-K explains space-based pricing, where "freight dimensions … determine applicable cubic minimum charges", but gives no rates.
- No NMFTA figure was found.
- Vendor snippets say 10-15% of shipments are reclassified (*assumed*, not used).

**Savings pool [our calc]:**
- $65.69B × 20% × 2% × 40% = **$105M**.
- $65.69B × 40% × 5% × 70% = **$920M**.
- Central **$62M**. **K5: unknown.**

**K4:** could now be settled pass. The cost base comes from named neutral data. The avoidable share is a judgement input to K5, as on C-09, where S2 passed K4 with an overpayment rate of our own. The coordinator decides.

*S2 note kept: the LTL carrier side fails K10 at S3 (small-firm pre-check). K11 is not in this check.*

### 2.10 C-23 · Quoting and booking international freight (K5)

**S2's build:**
- 164,684 staff at arrangement firms under 500 employees.
- × 30-50% in ocean and air forwarding **[our call]**.
- × $57,230 mean wage.
- × 15-30% of time on quoting and booking **[our call]**.
- × 30-50% removable **[our call]**.
- **Pool:** $127-707M.

**O*NET 30.0** (Department of Labor; task ratings dated Aug 2021, 33-43 respondents a task; N-N28, *verified* download), for cargo and freight agents (43-5011):
- "Estimate freight or postal rates and record shipment costs and weights" is a core task. **50.4%** do it daily or more, and **36.4%** several times a day or more.
- "Negotiate and arrange transport of goods with shipping or freight companies" is the most important core task, at 3.86 of 5. **59.8%** do it daily or more.
- O*NET measures how often a task is done, not the share of time it takes.
- **Cross-check:** split time equally across the 9 core tasks, and the two quoting tasks come to about 22% **[our call]**. That is inside S2's 15-30%.

**Quote volumes and time studies:** none neutral. The Freightos 2018 figure, 57 hours elapsed per manual quote, is a vendor figure (N-K35, *assumed*).

**Result:** no input replaced. **Unchanged: $127-707M, central $60M. K5: unknown.**

*K11 is not in this check.*

### 2.11 C-05 · Getting small carriers paid (K4, K5)

**S2's build:**
- Small carriers' revenue: $222.6B (Census, *verified*).
- × 20-40% factored **[our call]**.
- × fees of 1-4% (N-F40, vendor).
- × 15-40% removable **[our call]**.
- **Pool:** $0.07-1.4B.

**Share factored** (OOIDA Foundation; OOIDA flag):
- **2019 Freight Rate Survey** (707 responses; N-N16, *verified*): "A vast majority do not use a factoring service in their trucking business (77%)." So **23% use one**.
- **2022 Owner-Operator Member Profile Survey,** asked of owner-operators under their own authority (N-N17, *verified*): "Do you use a factoring service? (135) … Yes – 28%."
- **23-28% replaces 20-40%.** Two caveats:
  - OOIDA members are established operators.
  - Members were largely "not supportive" of factoring in 2018 (N-N16). Newer and smaller fleets may factor more.

**Fee level:**
- **Triumph Financial**, "#2 transportation factor in North America" (investor presentations filed as 8-K exhibits; N-N15, *verified*): "~1.29% Average Discount Rate" for the quarter to 30 Sep 2025, and "~1.37%" for the quarter to 30 Jun 2025.
- **Triumph's FY2025 10-K** (filed 11 Feb 2026; N-N14, *verified*): factoring revenue of $158.3M on $11.699B of invoices purchased. That is **1.35%** **[our calc]**.
- **OOIDA 2019:** "The average fee overall for those who do use such a service was 3.2 percent, a slight decline from the 4 percent fee in 2018" (N-N16).
- **1.29-3.2% replaces the vendor's 1-4%.** Triumph's rate is a large factor's average and sits at the low end.

**Cross-check [our calc]:**
- 23-28% of $222.6B is $51-62B factored a year.
- Triumph alone bought $11.7B in 2025, which is 19-23% of that, plausible for the second-largest factor.
- Its 10-K also gives 6,676,166 invoices purchased, an average transportation invoice of $1,717, and 33.6M invoices ($40.5B) processed through its payments network, where brokers pay carriers.

**Savings pool [our calc]:**
- $222.6B × 23% × 1.29% × 15% = **$99M**.
- $222.6B × 28% × 3.2% × 40% = **$798M**.
- Central **$56M**. **K5: unknown.**

**K4:** could now be settled pass. The factored share and the fee come from named data: an association survey (flagged) and a public filing.

*K11 is not in this check.*

### 2.12 C-18 · Warehouse storage and handling bills (K4, K5)

**S2's build:**
- Receipts of warehouses under 500 staff: $22.5B (SUSB, *verified*).
- × 1-5% leakage **[our call]**. Vendors say 3-15%.
- × 50-80% removable **[our call]**.
- **Pool:** $110-900M. For warehouses under 20 staff ($5.6B of receipts): $28-225M.

**Neutral leakage evidence: none found** after three tries (§5).
- Every figure found comes from vendors: "between 3 and 15%" and "5% and 12%" of revenue (vendor blogs). Extensiv's 2025 survey of 200+ 3PL warehouses names uncaptured charges as the top billing challenge, cited by 56% (vendor; all *assumed*, not used).
- No IWLA survey, academic study or public 3PL filing quantifies leakage.

**Results for both firm-size scopes** (unchanged):
- **Under 500 staff: $110-900M, central $63M.**
- **Under 20 staff: $28-225M, central $16M.**
- **K5: unknown** in both scopes. The high ends are $900M and $225M, both above $71M.

**K4:** still ?, because leakage is vendor-only. The coordinator decides which scope the card means.

### 2.13 C-02 · Load status for mid-sized shippers and receivers (K5)

**S2's build:**
- 53,390 cargo and freight agents at brokers and forwarders (N-F22) × $57,230 (N-K09) = $3.06B.
- × 20-40% of time on status **[our call]**.
- × 30-60% removable **[our call]**.
- **Pool:** $0.18-0.73B.

**O*NET** (N-N28, *verified*), for 43-5011:
- "Track delivery progress of shipments" is a core task. **79.0%** do it daily or more, 29.1% several times a day or more, and 14.7% hourly or more (43 respondents).
- "Notify consignees, passengers, or customers of freight or baggage arrival and arrange for delivery": 53.4% daily or more.
- **Cross-check:** an equal split across the 9 core tasks gives these two status tasks about 22% of time **[our call]**. That supports S2's low end of 20%. Nothing supports or rules out the 40% high end.
- **No neutral time-use study,** and no association survey of time spent on status, was found.

**Result:** no input replaced. **Unchanged: $0.18-0.73B, central $73M. K5: unknown.**

*K11 is not in this check.*

### 2.14 C-19 · Retailer OTIF fines and deductions (K4, K5)

**S2's build:**
- Small and mid-sized suppliers' sales to big-box stores: $112-240B (Census, with shares **[our call]**).
- × 0.5-1.5% of those sales in invalid deductions and avoidable fines **[our call]**. Vendors say 5-7% of revenue is deducted and 10-20% of that is invalid.
- × 20-40% removable **[our call]**.
- **Pool:** $0.11-1.44B.

**CRF 2018 Customer Deduction Survey** (run by Attain Consulting Group for the Credit Research Foundation, Jan 2018; CRF flag; N-N29, *verified* PDF):
- **The sample:** "203 companies responded", in 10 industry groups; 52% have sales of $500M or less.
- **Non-trade deductions:** "Non trade deductions as % of sales … Median is ¼ - ½ % of sales"; "6% reported > 5% of sales."
- **What they are:** shortages and pricing lead the non-trade reasons. The top compliance reasons are "Concealed shortages", "Early / late delivery", "EDI / ASN errors" and "Full carton shortage".
- **Invalid share:** "For all respondents, 6–10% of all deduction dollars are invalid or disallowed … (median)." "60% of all deduction dollars that are invalid or disallowed are ultimately recovered."
- **Replacement:** non-trade deductions at **0.25-0.5% of sales** replace S2's 0.5-1.5%. We treat all of them as addressable: valid ones by prevention, invalid ones by dispute **[our call]**.
  - This is generous, since pricing disputes are not logistics.
  - It is also low, since a median understates the average when 6% of firms are above 5%.
- **Suppliers' 10-Ks:** none quantify OTIF fines.
  - EDGAR full-text search finds "OTIF" in four 10-K filings, none with an amount.
  - Lifetime Brands mentions only "an allowance for anticipated customer deductions" (N-N12).

**Savings pool [our calc]:**
- $112B × 0.25% × 20% = **$56M**.
- $240B × 0.5% × 40% = **$480M**.
- Central **$33M**. **K5: unknown.**

**K4:** could now be settled pass, with the association flag. The deduction rate comes from a named survey.

### 2.15 C-17 · Controlling inbound freight from suppliers (K4 only)

**S2:**
- K5 passed at $0.51-5.3B.
- K4 was "?" because the overpay rate (15-30%), the inbound share (40-60%) and the uncontrolled share all rest on vendor snippets (N-K28, N-E31).

**Neutral overpay evidence: none found.**
- The MIT supply-chain master's capstone found (Servideo Fischer and Kandaswamy, published 11 Feb 2026) models "potential cost savings of up to 60%" from consolidating international inbound freight through hubs, for one representative network of 200 suppliers in China. It does not measure the cost of letting suppliers choose domestic carriers. Read, not used (§5).

**Neutral cross-checks of the cost base:**
- **Economic Census 2022 receipts, employer firms** (N-N13, *verified*):
  - long-distance general freight (truckload plus LTL, 484121 + 484122): **$238.4B**;
  - all general freight (4841): $293.1B;
  - all trucking (484): $423.3B.
- **Wholesale trade survey** (Census, Table 5.1): merchant wholesalers spent **$40.4B** on purchased transportation, shipping and warehousing in 2017, 5.0% of operating expenses (N-N23, *verified*). The 2022 total is suppressed (N-N22).
- **K5 sensitivity [our calc]:** if CSCMP's $451B base is replaced by the census $238-293B, C-17's low end becomes **$0.27-0.33B**. That is still ≥ $250M, so the K5 pass holds, but narrowly.

**K4:** still ?. The overpay rate and the inbound shares, which make the pool, are vendor-only.

*K11 is not in this check.*

### 2.16 Cross-card: the Census freight-spend lines

**What exists:**
- The Census retail and wholesale trade surveys publish "purchased transportation, shipping, and warehousing services" by industry. They do so only in years ending in 2 and 7, and as a share of operating expenses, not of sales.
- In 2022 many cells are suppressed. These surveys have since been folded into the Annual Integrated Economic Survey.

| Line (NAICS) | 2017 | 2022 | Cards it touches |
|---|---|---|---|
| E-commerce (4541) | $8,095M; 4.9% of operating expenses | suppressed (operating expenses $318,582M) | C-12; the customers of C-18 |
| All retail | $21,393M; 1.8% | suppressed | C-19 (the retailer side) |
| All merchant wholesalers (42) | $40,359M; 5.0% | suppressed (operating expenses $1,059,716M) | C-01, C-02, C-09, C-14, C-17 (the wholesale half) |
| Grocery wholesale (4244) | $4,599M; 5.8% | suppressed | C-04, C-15 |
| Hardware and plumbing (4237) | $1,882M; 5.6% | $2,437M; 5.2% | C-15 |
| Appliances and electrical (4236) | suppressed | $9,177M; 7.3% | C-13 (dropped) |
| Lumber (4233) | suppressed | $1,857M; 4.4% | C-16 (dropped) |
| Petroleum (4247) | $800M; 4.5% | $562M; 2.0% | C-38 |
| Beer, wine and spirits (4248) | suppressed | $683M; 2.0% | C-15 |
| Chemicals (4246) | $1,353M; 6.2% | suppressed | C-35 |

- **Sources:** N-N20 to N-N23, all *verified* downloads. The 2022 wholesale file uses 2012 NAICS codes.
- **Manufacturing has no equivalent Census line.** So the manufacturing half of C-01, C-09, C-14 and C-17 still rests on CSCMP's spend figures (N-K22, *assumed*).
  - **Untried lead:** the Bureau of Economic Analysis input-output use table, which shows each industry's purchases of truck transportation.
- **Carrier-side receipts** (Economic Census 2022, N-N13) are neutral bases for freight spend by mode:
  - LTL: $65.7B, close to CSCMP's $64B;
  - truckload: $172.7B, against CSCMP's $387B, which counts more carrier types, while the census leaves out nonemployers.

---

## 3. For the coordinator (not a call)

**1. No card crosses a K5 line.** With every sourced input swapped in, all 14 K5 cards remain unknown, and C-17's K5 pass holds.

| Card | Old central | New central | Moved by |
|---|---|---|---|
| C-12 | $59M | **$12M** | Census e-commerce shipping line |
| C-19 | $80M | $33M | CRF deduction rate |
| C-04 | $46M | $38M | ATRI's collection bound; METRANS |
| C-08 | $59M | $50M | theft corrected; TIA fraud range |
| C-06 | $55M | $47M | Census and OOIDA gross revenue |
| C-05 | $62M | $56M | OOIDA factored share; Triumph fee |
| C-20 | $50M | $54M ($19M with the CBP floor) | FY2025 entries; World Bank cost; CBP ICR |
| C-22 | $27M | $27M ($19M with 0.25 h) | USACE volume |
| C-10 | $32M | $33M | Census LTL base; carriers' claims ratios |
| C-11 | $60M | $62M | Census LTL base |
| C-02, C-18, C-21, C-23 | $73M, $63M ($16M under 20 staff), $32M, $60M | unchanged | none found |

**2. Cards whose central fee pool is now under $25M.**
- **C-12** ($12M) on the main reading.
- **C-20 and C-22** ($19M each) only on their sensitivity readings.
- **C-18's under-20-staff scope** ($16M, unchanged from S2).
- Under the S3a exit rule (`submarket_selection.md` §4 S3a, step 5), a card still unknown on K5 with a central under the floor goes to the reserve list. Which readings to adopt is your call.

**3. K4, as the evidence now stands:**
- **Could be settled pass:**
  - C-05 (OOIDA, flagged, and Triumph's filings);
  - C-11 (Census LTL base);
  - C-19 (CRF, flagged).
- **Partly settled:**
  - C-22: the volume is from named data, the turn time is not;
  - C-12: the cost base is from named data, the recovery rate is not.
- **Still ?:**
  - C-06: dispatch use has no source;
  - C-08: vendor theft data, association fraud estimate, no regulator data;
  - C-10: vendor filing and denial rates;
  - C-17: vendor overpay rate;
  - C-18: vendor leakage.

**4. A correction to S2 (evidence for the record, not an edit):**
- S2 built C-08's theft figure as 3,625 incidents × $202,364 = $733.6M (`2_knockouts.md` §4.1; N-C23).
- CargoNet's 2025 report shows only 2,243 of 2024's crime events were confirmed thefts, which gives about $454M.
- The latest year, 2025, is about $725M.
- If you log the fix, the C-08 row in §4.1 and N-C23's use should change.

**5. The removable share is still [our call] on all 15 cards.**
- Two sources bound it without replacing it:
  - FMC's charge-complaint refunds (C-21);
  - METRANS's appointment study (C-04, C-22).
- As S2 found, only S5's interviews and savings assessments can measure it.
- The inputs that swing each range most:
  - dispatch use (C-06);
  - filing and denial rates (C-10);
  - leakage (C-18);
  - fraud losses (C-08);
  - excess turn time (C-22);
  - the recovery rate after guarantee suspensions (C-12).

**6. The guarantee change leans C-12 lower.** FedEx's guarantee covers only express services from Feb 2026, and UPS restored air services only in 2021. Small sellers' ground parcels have little late-delivery refund left to audit. This supports the low end of C-12's recovery rate.

**7. Overlaps to watch if cards are combined later:**
- C-21 and C-22 share container per-diem (check K).
- C-08 and C-10: carriers' claims ratios include theft claims, so part of C-08's theft pool is also in C-10's claims.

---

## 4. Sources (new in this check)

- **Existing IDs** are cited in the text and listed in their own files. Re-read this session to verify figures they carry: N-C24 (ATRI), N-H22 (CBP trade statistics) and N-K01 (FMC D&D page).
- **Access date:** all sources were accessed on 2026-09-15.
- **Downloads** are in the session scratchpad (`…/scratchpad/checkN/`).

| ID | Source (author/org) | Date | URL | Access | What was read |
|---|---|---|---|---|---|
| N-N01 | BTS, *Port Performance Freight Statistics: 2025 Annual Report* (copy filed as Exhibit 36 on energy.gov; the bts.gov copy returned 403) | Jan 2025 (2022 USACE data) | https://www.energy.gov/sites/default/files/2026-02/Ex.%2036%20BTS_Port-Performance-2025_Annual-Report.pdf | full PDF text | §2.3: 45.7M loaded TEU in 2022; 66% imports, 24% exports, 10% domestic; top-25 table. No turn-time section |
| N-N02 | G. Giuliano and T. O'Brien (METRANS, USC/CSULB), *Evaluation of the Terminal Gate Appointment System at the Los Angeles/Long Beach Ports*, final report, project 04-06 | Feb 2008 | https://www.metrans.org/assets/research/04-06_Giuliano_final_0_0.pdf | full PDF text | Abstract ("no evidence that the appointment system affected queuing"); §7.3 and Table 24: savings of 9.3%, 17.5% and about 25% per turn; the "6% of all gate moves" caveat |
| N-N03 | Transport Topics, "Truck Turn Times Deteriorate at Ports of Los Angeles, Long Beach" (Harbor Trucking Association data) | 2017-08-15 | https://www.ttnews.com/articles/truck-turn-times-deteriorate-ports-los-angeles-long-beach | page extraction; secondary (*assumed*) | July 2017: 90-minute combined average; terminals 38-122 minutes; 24% of trips over 2 hours |
| N-N04 | Search snippets: Hapag-Lloyd North America operational updates (page returned 403); electrek on Pier 400 | 2025-26 | https://www.hapag-lloyd.com/en/services-information/operational-updates/north-america.html ; https://electrek.co/2026/04/04/port-of-la-turns-to-electric-terminal-trucks-to-to-slash-dwell-times/ | snippet (*assumed*) | Long Beach Container Terminal gate turn time 45-51 minutes; Pier 400 about 30 minutes |
| N-N05 | CBP, "Agency Information Collection Activities; Revision; Entry Summary (CBP Form 7501)", Federal Register notice 2024-06255 (OMB 1651-0022) | 2024-03-25 | https://www.govinfo.gov/content/pkg/FR-2024-03-25/html/2024-06255.htm | page extraction | Burden table: formal electronic 23,133,408 responses at 5 minutes; paper 20 minutes; softwood lumber 40 minutes; informal |
| N-N06 | World Bank, *Doing Business* historical dataset, DB2020 (DB16-20 methodology) | 2019 (DB2020) | https://archive.doingbusiness.org/content/dam/doingBusiness/excel/db2020/Historical-data---COMPLETE-dataset-with-scores.xlsx | download (xlsx) | US, New York and Los Angeles: import documentary compliance $100, 7.5 hours; border compliance $175, 1.5 hours. Definition from the archive page |
| N-N07 | Old Dominion Freight Line, Form 10-K FY2025 | filed 2026-02-24 | https://www.sec.gov/Archives/edgar/data/878927/000119312526067161/odfl-20251231.htm | full text (EDGAR) | "cargo claims ratio of 0.1%"; insurance and claims 1.4% of revenue; revenue $5,496M |
| N-N08 | XPO, Form 10-K FY2025 | filed 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1166003/000116600326000016/xpo-20251231.htm | full text (EDGAR) | "damage claims ratio of 0.3%" (2025); 1.2% in Q4 2021 |
| N-N09 | Saia, Form 8-K, Exhibit 99.1 (Q3 2025 results and call transcript) | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1177702/000119312525267032/saia-ex99_1.htm | full text (EDGAR) | "cargo claims ratio was 0.54%"; CEO on how the ratio is calculated |
| N-N10 | TFI International, Form 6-K, Exhibit 99.1 (Q4 2023) | 2024-02-08 | https://www.sec.gov/Archives/edgar/data/1588823/000095017024012763/tfii-ex99_1.htm | full text (EDGAR) | Claims ratio "0.5% for US LTL"; Canadian LTL 0.1% |
| N-N11 | Forward Air, Form 8-K, Exhibit 99.1 (Q4 2023) | 2024-02-29 | https://www.sec.gov/Archives/edgar/data/912728/000162828024007719/exhibit991pressreleaseye20.htm | full text (EDGAR) | "cargo claims ratio was 0.09%" |
| N-N12 | EDGAR full-text searches plus the filings they surfaced: Werner and Knight-Swift 10-Ks FY2025; ArcBest 10-K FY2023; Lifetime Brands 10-K FY2025 | searches 2023/24-2026 | https://efts.sec.gov/LATEST/search-index (queries: "cargo claims ratio", "damage claims ratio", "cargo claims" in truckload carriers' filings, "reweigh", "reclass" LTL, "OTIF", "on-time in-full" fines) | API plus full text | Truckload 10-Ks: cargo claims only as a self-insured category. "Reweigh": no LTL carrier filing. ArcBest: cubic minimum charges, no rates. OTIF: 4 hits, none quantified. Lifetime Brands: "allowance for anticipated customer deductions" |
| N-N13 | Census, 2022 Economic Census, sector 48-49 basic file (EC2248BASIC) | file dated 2024-11-20 | https://www2.census.gov/programs-surveys/economic-census/data/2022/sector48/EC2248BASIC.zip | download (parsed) | US receipts ($1,000s): 484 423,270,958; 4841 293,066,873; 484121 172,717,339; 484122 65,688,461; firms and establishments |
| N-N14 | Triumph Financial, Form 10-K FY2025 | filed 2026-02-11 | https://www.sec.gov/Archives/edgar/data/1539638/000153963826000007/tfin-20251231.htm | full text (EDGAR) | Factoring: $11.699B purchased; 6,676,166 invoices; average transportation invoice $1,717; factoring revenue $158.3M; yield on average net funds employed 14.87%. Payments: 33.6M invoices, $40.5B |
| N-N15 | Triumph Financial investor presentations (8-K exhibits) | Q2 and Q3 2025 | https://www.sec.gov/Archives/edgar/data/1539638/000153963825000019/tfin-investorpresentatio.htm ; https://www.sec.gov/Archives/edgar/data/1539638/000162828025035063/tfininvestordeck.htm | full text (EDGAR) | "#2 transportation factor in North America"; $11.0-11.3B purchased over the trailing 12 months; average discount rate ~1.37% (Q2) and ~1.29% (Q3); network of 57 factors and 173,000+ carriers |
| N-N16 | OOIDA Foundation, *2019 Freight Rate Survey* (OOIDA flag) | Dec 2019 | https://www.ooida.com/wp-content/uploads/2019/12/2019-Freight-Rate-Survey.pdf | full PDF text | 707 responses; 77% do not use factoring; average fee 3.2% (4% in 2018); members' views on factoring |
| N-N17 | OOIDA Foundation, *2022 Owner-Operator Member Profile Survey* (OOIDA flag) | May 2022 | https://www.ooida.com/wp-content/uploads/2022/05/2022-Owner-Operator-Survey.pdf | full PDF text | Up to 488 responses; own authority: 28% use factoring (n=135); gross income $222,280 own authority, $258,119 overall; load sources |
| N-N18 | FMC, *FY 2026 Congressional Budget Justification* | May 2025 | https://www.fmc.gov/wp-content/uploads/2025/05/FY2026CongressionalBudgetJustification2025.pdf | full PDF text | FY2025 to date: 209 charge complaints, 118 assigned, $2,564,931.36 refunded or cancelled; more than $5.8M waived or refunded in three years |
| N-N19 | FMC, "Demurrage and Detention Billing Requirements", final rule, Federal Register 2024-02926 | 2024-02-26 | https://www.govinfo.gov/content/pkg/FR-2024-02-26/html/2024-02926.htm | page extraction | Only statistic: $8.9B charged and $6.9B collected, 2020-22. No dispute, waiver or small-entity data |
| N-N20 | Census, Annual Retail Trade Survey, *Detailed Operating Expenses of U.S. Retail Firms by Kind of Business: 2022* | 2024 release | https://www2.census.gov/programs-surveys/arts/tables/2022/bes.xlsx | download | 4541 operating expenses $318,582M; purchased transportation line "S" (suppressed) for 4541 and all retail |
| N-N21 | Census, Annual Retail Trade Survey, *Detailed Operating Expenses … 2017* | 2019 release | https://www2.census.gov/programs-surveys/arts/tables/2017/bes.xlsx | download | 4541: $8,095M, 4.9% of $163,547M; nonstore $8,590M; all retail $21,393M (1.8%) |
| N-N22 | Census, Annual Wholesale Trade Survey 2022, Table 5.1 | Jan 2024 release | https://www2.census.gov/programs-surveys/awts/tables/2022/2022_awts_detailopex_table5.1.xlsx | download | Total suppressed; operating expenses $1,059,716M; 4233, 4236, 4237, 4247 and 4248 values |
| N-N23 | Census, Annual Wholesale Trade Survey 2017, Table 5.1 (revised) | 2019 | https://www2.census.gov/programs-surveys/awts/tables/2017/2017_awts_detailopex_table5.1_revised.xlsx | download | All merchant wholesalers $40,359M (5.0%); the kinds of business in §2.16 |
| N-N24 | Verisk CargoNet, *2025 Supply Chain Risk Trends Analysis* (vendor) | 2026-01-21 | https://www.cargonet.com/news-and-events/cargonet-in-the-media/2025-theft-trends/ | page extraction; vendor (*assumed*) | Events 3,594 (2025) and 3,607 (2024); confirmed thefts 2,646 and 2,243; ~$725M (2025); average $273,990 (2025) and $202,364 (2024) |
| N-N25 | Trucking Dive, "Brokerage fraud costs could surpass $800M, TIA president says" (TIA flag) | 2023-05-18 | https://www.truckingdive.com/news/brokerage-fraud-costs-could-surpass-800-million-dollars-transportation-intermediaries-association/650595/ | page extraction; secondary (*assumed*) | "$800 million or more"; testimony before a House subcommittee; no method stated |
| N-N26 | Search snippets attributing ranges to TIA (FleetOwner, Inbound Logistics and others) | 2023-25 | https://www.fleetowner.com/news/article/21268586/fmcsa-and-tia-target-double-brokering-more-aggressively | snippet (*assumed*) | "$500 million to $1 billion" (fraud); "$700 million to $1 billion" (double brokering) |
| N-N27 | Land Line, "Broker report: FMCSA blames lack of data, authority" (on FMCSA's July 2024 report to Congress; that PDF returned 403) | 2024 | https://landline.media/broker-report-fmcsa-blames-lack-of-data-authority/ | snippet and summary (*assumed*) | FMCSA says it lacks the data to quantify double brokering; it asks for penalty authority |
| N-N28 | O*NET 30.0 database: Task Statements and Task Ratings (US Dept. of Labor / National Center for O*NET Development) | 2025 release; 43-5011 ratings dated Aug 2021 | https://www.onetcenter.org/dl_files/database/db_30_0_text/Task%20Ratings.txt | download (parsed) | 43-5011.00: 9 core tasks with importance, relevance and frequency categories (§2.10, §2.13) |
| N-N29 | Credit Research Foundation / Attain Consulting Group, *2018 Customer Deduction Survey* (CRF flag) | Jan 2018 (PDF posted Oct 2018) | https://www.crfonline.org/wp-content/uploads/2018/10/Deduction-Survey-2018-Jessica-Butler-1.pdf | full PDF text | 203 companies; non-trade deductions, median ¼-½% of sales; 6% of firms over 5%; 6-10% invalid; 60% of invalid recovered; top compliance reasons |
| N-N30 | FreightWaves, "UPS partially reinstates money-back delivery guarantee - with a twist" | 2021-04-05 | https://www.freightwaves.com/news/ups-partially-reinstates-money-back-delivery-guarantee-with-a-twist | page extraction; trade press (*assumed*) | Air and international express reinstated 2021-04-05; "not restored … any of its other product lines" |

---

## 5. Could not access, or not found

**Blocked or unusable:**
- **BTS *Port Performance Freight Statistics: 2026 Annual Report*:** HTTP 403 at bts.gov (curl and WebFetch), and "Access Denied" on the ROSA P copy (rosap.ntl.bts.gov/view/dot/88517). The 2025 report was used instead (2022 data).
- **CBP's regulatory impact analysis for the low-value-shipments rule** (docket USCBP-2025-0002-0003, downloads.regulations.gov): HTTP 403 from CloudFront (curl and WebFetch). The Federal Register preamble (govinfo) holds no per-entry figures.
- **FMCSA, *Unlawful Brokerage Activities Report to Congress*** (July 2024, fmcsa.dot.gov): HTTP 403. Cited through Land Line (N-N27).
- **ATRI's full detention report:** behind a registration form. Only the release (N-C24) was read.
- **UPS's service-guarantee page:** "Access Denied".
- **Hapag-Lloyd operational updates:** HTTP 403. The Long Beach turn time is a snippet only.
- **Port Optimizer (track.portoptimizer.com):** an interactive app with no public turn-time figures.
- **MIT capstone PDF** (Hu, 2020, dspace.mit.edu): the download returned a 113-byte stub.
- **Verisk's newsroom release** on 2025 theft: the body did not extract. CargoNet's own page (N-N24) was used.
- **Census economic-census API (ecnbasic):** returned empty responses. The flat file (N-N13) was used.
- **World Bank API:** Doing Business indicators are archived. The DB2020 flat file (N-N06) was used.

**Searched, not found** (what was tried):
- **Current turn times at source (C-22):** the BTS 2025 report (none), the BTS 2026 report (blocked), Port Optimizer, and a search of the Port of Long Beach's Supply Chain Information Highway (figures only in snippets).
- **US loaded container TEU for 2023-25 at source (C-22):** only in the blocked BTS 2026 report.
- **Neutral cargo-claim filing and denial rates (C-10):**
  - a search of TLP&SA and Transportation & Logistics Council surveys;
  - an academic search on claim filing and recovery;
  - EDGAR, for truckload carriers' claims.
  - Only vendor figures surfaced.
- **A truckload cargo claims ratio (C-10):** EDGAR full text across Knight-Swift, Werner, Heartland, Schneider and Marten.
- **FMC dollar data on waived or refunded D&D outside the charge-complaint channel (C-21):** the FMC D&D page, the 2024 final rule, the 2026 charge-complaint procedures rule (Federal Register 2026-17876, no statistics), and the FY2026 budget justification. FMC Fact Finding 28's final report was not opened.
- **The share of owner-operators using dispatch services (C-06):** the OOIDA Foundation surveys of 2019, 2022 and 2023 (full text); an ATRI/FMCSA/OOIDA search; Overdrive's compensation-survey articles (no share given).
- **FBI cargo-theft data (C-08):** NIBRS carries a cargo-theft flag, but the Crime Data Explorer is interactive, with no downloadable totals found.
- **Customs-broker fee levels from neutral sources (C-20):** GAO and USITC searches. GAO-16-173R covers ACE filing costs for software vendors, not broker fees. Only vendor price guides were found.
- **E-commerce purchased transportation for 2022 (C-12):** the cell is suppressed in the retail survey (N-N20).
- **Neutral LTL correction rates (C-11):** an NMFTA search; EDGAR full text for "reweigh" and "reclass"; carriers' 10-Ks.
- **Neutral warehouse billing leakage (C-18):** an IWLA search; a WERC and academic search; public 3PL filings. Only vendor figures were found.
- **Neutral quote volumes or quoting time (C-23):** NCBFAA, FIATA and academic searches. Only Freightos (vendor) was found.
- **Neutral inbound-overpay rates (C-17):** an MIT CTL search; the 2026 capstone news item (scm.mit.edu, "From Chaos to Coordination: Rethinking Inbound Logistics", 11 Feb 2026) was read but is not applicable, so it has no ID.
- **A time-use study of status checking (C-02):** none beyond O*NET's frequencies.
- **Suppliers' 10-K disclosures of retailer fines (C-19):** EDGAR full text for "OTIF" and "on-time in-full" fines. None quantified.
- **Detention paid and overtime per dock site (C-04):** not found.

**Tooling:** the scholarly-search MCP server failed to connect in this session ("Connection closed"), so peer-reviewed databases were searched only through general web search.
