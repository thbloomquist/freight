# S5 check AT, adversarial review

- **What this is:** an adversarial check of check AT (how much truckload plus LTL freight a C-09 customer buys, by revenue and segment), done so that faulty web data and coincidences are pruned before the founders use AT's table to choose whom to call. Each claim was tested to see whether it breaks. No objection was invented: a claim that survives is reported as a result too.
- **File checked:** `research/s5_check_AT_c09_freight_spend_by_size.md` (43 ledger rows N-AT01 to N-AT43; §0 verdicts; §AT1-§AT5; the Coincidence watch). Its private part (AT4, four named shippers) was checked too; those verdicts are in the private folder (`freight_private/c09_prospects_review.md`, §AT4), not here. Nothing reviewed was edited.
- **Date:** 2026-10-09. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.** It does not set a segment ratio; where it suggests one, the suggestion is **[our calc]** or **[our call]**.
- **Fetches:** 75 page, file and API downloads in all for this review and the sister review of check AU, plus 14 web searches. For check AT: the Census SUSB tables (2), BEA's input-output zip (1), the two court PDFs (2), the SEC XBRL frames for the freight tag (2) and for 2016-17 revenue (6), and the fetch tool on five filings or pages (American Vanguard's 2017 10-K and its index, Oil-Dri's FY2017 10-K in two passes, Supply Chain Digest). Six direct downloads from www.sec.gov, one EDGAR full-text query and two BTS requests failed (§7). The SEC company profiles (SIC codes) and the 2025 revenue frames used here were fetched for the AU review and are counted there. Downloads were kept in the session scratchpad, each in its own folder, outside the project.
- **No identity was sent. Nobody was contacted.** Downloads used a generic browser user-agent with no name, email or contact. SEC's data API (data.sec.gov) answered that request; SEC's main site (www.sec.gov) refused it as an "Undeclared Automated Tool", and no contact header was supplied, so filings on www.sec.gov were read through the fetch tool instead. EDGAR full-text search returned HTTP 500. No logins, forms or gated downloads. Data-broker pages that came up in searches were not opened or used.
- **What was checked:**
  - **Every AT1 firm-year from 2016-18 (29 rows plus the four context distributors):** the freight value, period and revenue were re-matched to the SEC's own XBRL frames, value by value. Filing text was re-read for American Vanguard and Oil-Dri, the two SG6 inputs that set the central and the high.
  - **Not re-checked:** the 2025 re-reads of Tootsie Roll, WD-40 and J&J Snack Foods (N-AT16 and the 2025 parts of N-AT17 and N-AT18), John B. Sanfilippo FY2018 (N-AT19; its FY2017 values were re-matched), EACO's FY2025 freight amount (its revenue was re-matched), and Intrepid Potash 2017 (N-AT31; not tagged).
  - **Recomputed in full:** the two bankruptcy payment lists (every payee total re-summed from the court PDFs), all BEA ratios in §AT2.3, the national mode split, every cell of the AT5.1 and AT5.2 tables, and every firm count in AT5.3.
- **Labels:** **KEEP-verified** = the row's figure is true as written, re-read at the source. **KEEP-assumed** = a secondary or vendor figure that survived. **NARROW** = true, but the source supports less than the row says. **DISCARD** = not supported.

**Words used here:**
- **SIC code:** the industry code the SEC records for each filer (an older system than NAICS). Codes starting 34 are fabricated metal products; 14 is mining of nonmetallic minerals; 01 is crop farming; 27 is printing.
- **O, s, I, p:** the four inputs of AT's formula, TL+LTL as % of revenue = O × s + I × p. O = outbound freight as % of revenue (from filings); s = the TL+LTL share of outbound (judgement); I = for-hire truck freight on purchased inputs as % of output (BEA); p = the share of that inbound freight the firm pays itself (judgement).
- **Freight, delivery and warehousing:** one income-statement line that mixes carrier bills with the cost of storing goods.

---

## §0 Result in one table

**Ledger verdicts (43 rows)**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not re-checked |
|---|---|---|---|---|
| 38 | 1 | **2** | **0** | 2 |

**No row is discarded, and every [our calc] reproduces.** Every 2016-17 freight value and revenue in AT1 matches the SEC's own XBRL frames to the dollar. Every BEA ratio matches the 2023 summary and 2017 detailed Use tables. Both payment lists re-sum exactly. The firm counts reproduce within 3%. What breaks is how some inputs are read:
- **SG6's central rests on one line that includes warehousing.** American Vanguard's 7.8%, used as SG6's central O, is the 10-K line "Freight, delivery and warehousing", on global sales (§1 #1).
- **WB Supply's "own fleet about 4×" is a reading.** The fleet payees are a vehicle-leasing firm and fuel cards; the list does not show that those vehicles carry goods (§1 #2).
- **The "quartiles" are not quartiles,** and three of the seven SG2 ratio firms are fabricated-metal makers by their SEC SIC code, a group the brief excludes. Neither changes a segment central by more than a rounding (§1, B1-B3).
- **Judgement does most of the work in AT5.** Every central TL+LTL figure depends on a judgement input: s multiplies 56-79% of it, and p (with SG1's I) the remaining 21-44% (§3.3).

**Verdicts on the §0 question rows**

| Question | AT's proposed verdict | This review | Reason |
|---|---|---|---|
| **AT1** freight ÷ revenue from filings | Answered for public firms | **AGREE**, with two narrowings | All values re-match. American Vanguard's figure is "Freight, delivery and warehousing" on global sales (72% domestic in 2017). Segment labels are loose: by SEC SIC code, Acme United (3420), Omega Flex (3430) and Watts (3490) are fabricated metals; only one of the three in-range SG1 firms (Hillman) is in SG1's NAICS codes. Medians barely move (§1 #1, B1-B3) |
| **AT2** payment lists and benchmarks | Narrowed | **AGREE** | Both lists re-sum exactly. WB Supply's fleet reading is narrowed (§1 #2). The BEA inbound reading is supported by a BTS description of the same tables (*assumed*, §6 #1) |
| **AT3** mode split | Narrowed | **AGREE** | National shares reproduce: 58.0% and 34.2%. Rail's $97.3B is a 2025 figure, but CSCMP says it was "the same as 2024", so the 2024 mix holds. The segment shares s are judgement (§3.3) |
| **AT4** four named shippers | See the private file | **AGREE**, two small corrections | Three revenues re-match the SEC frames exactly. Two small corrections are in the private review |
| **AT5** conversion table and counts | Proposed table | **AGREE as arithmetic; flag SG6** | Every cell reproduces. SG6's central (5.15%) leans on one firm's freight-plus-warehousing line; with O at the median of the two non-mineral SG6 firms, the central is **3.85%** and $1.5M of TL+LTL needs **~$39M** of revenue, not ~$29M **[our calc]**. The other five centrals stand as AT's judgement |

---

## §1 Discards and narrowings (most important first)

No row is discarded. Two ledger rows are narrowed, and several body statements need the same treatment. They are ordered by how much they move the AT5 table.

| # | Claim ID or place | What was claimed | What the source actually says (quote ≤40 words) | Verdict | Why, and the restricted reading |
|---|---|---|---|---|---|
| 1 | **N-AT34; §AT1.3 SG6 note; AT5.1 "O for SG6 uses American Vanguard's 7.8% as the central"** | American Vanguard tagged $27.75M of freight on $355.047M of sales in 2017 (7.82%), the closest SG6 case; AT5 uses it as SG6's central O | 2017 10-K: "Freight, delivery and warehousing costs for the year ended December 31, 2017 increased by $870 to $27,750, as compared to $26,880 in 2016." Also: "Domestic sales finished the year at $256,142"; "International sales … ($98,905 in 2017" | **NARROW** | The value and revenue are exact (XBRL frame and 10-K). But the line **includes warehousing**, and 28% of sales were international. The company itself calls the line "freight costs … 7.8%" of sales. **Restricted reading:** one ag-chemical maker's freight-delivery-and-warehousing line, on global sales, was 7.8% of sales in 2017. As SG6's only non-mineral maker above 3%, it sets the SG6 central on its own. **Effect [our calc]:** with O = 5.2% (median of Omega Protein 2.61% and American Vanguard 7.82%), SG6's central is 5.2 × 0.50 + 2.5 × 0.50 = **3.85%**, and the revenue for $1.5M of TL+LTL rises from **$29M to $39M** ($5M: $97M → $130M) |
| 2 | **N-AT36; §AT2.1 "Own fleet … about 4× its for-hire trucking"; §AT2.2 "WB Supply's for-hire trucking was about a fifth of its trucking cost"; §AT3 row "~80%"** | WB Supply spent ~$0.96M a year on its own fleet, about four times its for-hire trucking | SOFA: "Enterprise Fleet Management Total 149,715.92"; "Wex Fleet Total 86,181.46"; payees listed as "Services". Freight payees: Ally Global Logistics $20,761.95; Saia $15,963.03; Pradon Construction & Trucking $12,400.50; USA Logistics $8,250.00 | **NARROW** | Every amount re-sums ($57,375.48 and $235,897.38 in 90 days; ×365/90 = $232,690 and $956,695; ratio 4.1×). But the "fleet" is a vehicle-leasing company and fuel cards. Nothing in the list says whether those vehicles deliver goods or carry sales and service staff. **Restricted reading:** in 90 days the distributor paid for-hire carriers about $57k and paid a vehicle-leasing firm and a fuel-card firm about $236k; part of the latter may be delivery fleet. "Own fleets hide freight from C-09" stays a fair hypothesis, but this list does not measure it |

**Smaller body corrections (verdicts unchanged)**

- **B1. AT5.1 "O = outbound freight as % of revenue (AT1 quartiles, rounded)".** They are not quartiles. The rules differ by segment: SG1 is near the 7-firm quartiles (0.8 / 1.6 / 4.2); SG2 uses the lower quartile, the median without Virco and the maximum without Virco (2.5 / 3.1 / 5.1); SG4 and SG5 use minimum / median / maximum; SG6 uses the minimum, American Vanguard and Oil-Dri. Relabel it "from AT1, by segment rule **[our call]**".
- **B2. §AT1.3 SG3 "8 firms … median 4.31% (freight-out measures)", low 2.09%.** The median of all 8 tabled ratios is **5.26%** (2.30, 3.13, 3.15, 4.31, 6.20, 7.55, 8.53, 10.45). 4.31% is the median once Reed's (warehouse labour and rent included) is dropped. The 2.09% low is John B. Sanfilippo's FY2017, not the FY2018 row in the table. AT5's SG3 central (4.3) is a defensible choice, but the row should say so.
- **B3. Segment labels in AT1.** By the SIC code the SEC records:
  - three of the seven SG2 firms make fabricated metal products, a group the brief excludes: Acme United (3420, cutlery and hand tools), Omega Flex (3430, plumbing fixtures and heating equipment) and Watts (3490). Dropping them leaves AAON 2.81%, P&F 3.42%, Johnson Outdoors 2.21% and Virco 10.20%, median **3.12%**, so SG2's central (3.1%) is unchanged **[our calc]**;
  - of SG1's three in-range firms only Hillman (hardware wholesale) sits in SG1's NAICS codes. EACO's SIC is 5065 (electronic parts wholesale), and Transcat is half calibration services. Pool Corp, a context firm, distributes pool supplies, not an SG1 line;
  - in SG6, Intrepid's SIC is 1400 (mining) and Compass Minerals is a salt miner; Oil-Dri's is 3990 (miscellaneous manufacturing). AT already sets these three aside for the central;
  - Tredegar is listed "SG4 (partly metals)"; its aluminium share was not re-read (§4 #1).
- **B4. Myers (N-AT26).** The SEC frame now reports Myers' 2016 sales as $534.379M (a later, restated filing); AT's $558.062M is from the original filing, the same one as the freight tag. Using the restated figure gives 3.14% instead of 3.01%. AT's same-filing choice is the right one; noted only.
- **B5. AT5.3 SG4 "All firms 9,201".** That is the sum of the size classes; the table's own "Total" rows add to 9,205 (Census noise). Immaterial.
- **B6. Instant Brands (N-AT37).** The "unclear" 4.8% is three payees (US Transportation Services $96,585; Carry All Products $132,293; R.J. Glass $7,770 in 90 days). If all three were truckload, TL+LTL would rise from 4.7% to 9.4% of transport payees. The reading ("importers that sell through parcel and big retailers buy little TL or LTL") survives.
- **B7. KapStone (§AT1.3 SG4 note, "revenue not read").** Its 2017 sales in the SEC frame are $3,315.66M, so its tagged $299.872M is **9.0%** of sales **[our calc]**. That supports "large paper firms run higher".

---

## §2 Coincidences found

**Shared origins**

| Figures | Where | Single origin | Effect |
|---|---|---|---|
| American Vanguard 7.8% | AT5 SG6 central O; the company's own MD&A "freight costs … 7.8% in 2017" | One income-statement line, "Freight, delivery and warehousing" | The ratio is the firm's own, but it measures more than carrier bills (§1 #1) |
| All 2016-17 freight values | 29 AT1 firm-years and 4 context rows | One XBRL tag, chosen by the filer | Confirmed: every value equals the SEC frame entry. The American Vanguard case shows the tag can carry a freight-and-warehousing line; the other XBRL-only rows were not read in the filing (§4 #2) |
| Rail $97.3B | AT3's 2024 mix; N-AT41 | CSCMP 2026 via Supply Chain Digest: "At $97.3 billion in 2025 - the same as 2024" | The 2024 use is consistent |

**Look-alikes**

| Value | Where | What each measures |
|---|---|---|
| "Own fleet" | WB Supply (vehicle leasing and fuel cards); Advanced Drainage Systems ("approximately 700 tractors"); the private prospect file's own-fleet cautions | Leased cars or pick-ups, a delivery tractor fleet, or route trucks. Only the second is shown to carry goods |
| "Freight" lines | Tootsie Roll ("freight, delivery and warehousing"), American Vanguard (same words), Reed's ("delivery and handling" with warehouse labour), J&J 2025 ("Distribution") | Four different scopes, all wider than carrier bills |
| A firm's segment | AT1 puts Oil-Dri in "SG6 / SG3"; the SEC records it as SIC 3990 (miscellaneous manufacturing) | Segment by end market against segment by code. Neither AT nor its sister check AU states which rule it uses |

**Inside the private files:** one firm appears both in AT4 and in the check-AU prospect list, with revenue estimates about three times apart, both built from staff counts (AT4 on a 2018 total-staff figure, AU on a current headquarters figure). Both are *assumed*. Details are in the private review.

---

## §3 Arithmetic re-done

### 3.1 AT1, AT2 and AT3

| Item | Check AT | Recomputed | Result |
|---|---|---|---|
| AT1 ratios, 30 firms + 4 context + re-reads | as tabled | each freight value ÷ revenue from the SEC frames or the filing figures | ✓ every ratio to two decimals |
| AT1.3 SG1 median with the four larger firms | 1.62% | 0.63, 0.77, 1.10, 1.62, 1.76, 4.15, 4.68 | ✓ |
| AT1.3 SG2 median | 3.42% (3.1% without Virco) | 7 firms: 3.42; 6 firms: (2.81 + 3.42) ÷ 2 = 3.12 | ✓ |
| AT1.3 SG3 median | 4.31% | 7 firms without Reed's: 4.31; all 8: 5.26 | ✓ as defined (B2) |
| AT1.3 SG4 median | 3.93% | (3.50 + 4.35) ÷ 2 = 3.93 | ✓ |
| **new:** KapStone 2017 | — | 299.872 ÷ 3,315.66 = 9.04% | (B7) |
| WB Supply | $57,375.48; ~$0.23M; 0.24% / 0.50%; fleet ~$0.96M, ~4× | 20,761.95 + 15,963.03 + 12,400.50 + 8,250.00 = 57,375.48; ×365/90 = 232,690; ÷ 98.55M = 0.24%; 2021 run-rate 14.11M × 365/110 = 46.8M → 0.50%; fleet 235,897.38 × 365/90 = 956,695 → 4.1× | ✓ (reading narrowed, §1 #2) |
| Instant Brands | 32 payees $7,401,282; transport $4,966,623; ~$20.1M, 3.84%; parcel 45.0%, ocean 31.5%, drayage 8.0%, customs 5.1%, unclear 4.8%, LTL 2.4%, TL 2.3%, rail 1.1%; TL+LTL $0.94M (0.18%), $2.54M with drayage (0.48%) | 32 "Other FREIGHT" payee totals re-summed = 7,401,282; less Körber 2,333,831, BluJay 46,493 and two warehouses 54,335 = 4,966,623; UPS + UPS Mail Innovations + FedEx = 2,232,846 (44.96%); five ocean lines 1,562,985 (31.47%); four drayage firms 394,899 (7.95%); TForce + Old Dominion + Estes 119,786 (2.41%); Werner + Autumn + BNSF Logistics 111,778 (2.25%); TL+LTL 231,564 × 365/90 = 939,121 | ✓ |
| BEA 2023 ratios (N-AT39) | truck, rail, water, air, all transport, truck share for 14 industries | recomputed from the zip; "all purchased transport" = air + rail + water + truck + pipeline + "other transportation and support" (warehousing excluded) | ✓ every figure |
| BEA 2017 detail (N-AT40) | 24 truck and rail ratios | recomputed from the 2017 detailed table, row T008 output | ✓ every figure checked (24 of 24) |
| CSCMP mode split | 58% / 34%; parcel 30% / 17%; private 41%; rail 13% / 7% | 451 ÷ 777.8 = 58.0%; 451 ÷ 1,319.2 = 34.2%; 229.5 ÷ 777.8 = 29.5%; 541.4 ÷ 1,319.2 = 41.0%; 97.3 ÷ 777.8 = 12.5% | ✓ |

### 3.2 AT5 tables

| Item | Check AT | Recomputed | Result |
|---|---|---|---|
| AT5.1 TL+LTL % (low / central / high) | SG1 0.33 / 1.14 / 3.81; SG2 1.38 / 2.57 / 5.43; SG3 1.65 / 3.83 / 8.10; SG4 1.63 / 3.24 / 5.40; SG5 1.78 / 3.48 / 9.32; SG6 1.16 / 5.15 / 12.75 | O × s + I × p for each input set (e.g. SG2 central 3.1 × 0.65 + 1.1 × 0.50 = 2.565) | ✓ all 18 |
| AT5.2 revenue needed, 36 cells with ranges | as tabled | spend ÷ % (e.g. $1.5M ÷ 2.565% = $58.5M; ÷ 5.43% = $27.6M; ÷ 1.375% = $109.1M) | ✓ all 36 cells and ranges |
| AT5.3 firms by receipts band | SG1-SG6 rows | re-summed from SUSB 2022 by NAICS | ✓ every cell (SG4 total: B5) |
| AT5.3 large-size split | manufacturing 3,527 / 1,464 / 980 / 715 / 778; wholesale 5,424 / 2,159 / 1,215 / 847 / 931 | read from the large-receipts table | ✓ |
| AT5.3 firms at or above each line (central) | SG1 1,330 / 1,079 / 898 / 576 / 403 / 238; SG2 2,935 / 2,342 / 1,952 / 1,621 / 1,201 / 716; SG3 2,674 / 2,156 / 1,845 / 1,460 / 1,146 / 658 | SUSB's fine size classes, spread evenly within each, and the sector split above $100M | ✓ SG1-SG3 exactly, ranges too |
| same, SG4-SG6 | SG4 ≥$5M 592, ≥$10M 344; SG5 1,131 / 654; SG6 1,198 / 826 | with each NAICS code given its own sector's split: SG4 588 / 334; SG5 1,125 / 631; SG6 1,198 / 807 | ✓ within 3%; the rule AT used for mixed segments is not stated |
| Totals | ~14,200 / ~11,300 / ~9,600 / ~7,500 / ~5,700 / ~3,400; band $1.5-10M ~7,900 | 14,213 / 11,311 / 9,572 / 7,469 / 5,662 / 3,383; band 7,928 | ✓ |

### 3.3 How much of each central is judgement **[our calc]**

| Segment | Central | From I × p (p is judgement; SG1's I is too) | Central with p = 0 | Revenue for $1.5M with p = 0 (AT central) |
|---|---|---|---|---|
| SG1 | 1.14% | 0.50 points, **44%** | 0.64% | $234M ($132M) |
| SG2 | 2.565% | 0.55, 21% | 2.02% | $74M ($58M) |
| SG3 | 3.83% | 1.25, 33% | 2.58% | $58M ($39M) |
| SG4 | 3.24% | 0.90, 28% | 2.34% | $64M ($46M) |
| SG5 | 3.475% | 1.00, 29% | 2.48% | $61M ($43M) |
| SG6 | 5.15% | 1.25, 24% | 3.90% | $38M ($29M) |

The rest of each central is O × s, and s (the TL+LTL share of outbound freight) is also judgement. So **every central TL+LTL figure in AT5 is set by at least one judgement input**: s on 56-79% of it and p on the rest. The firm counts in AT5.3 inherit this. AT says so in its own reading; this table puts a number on it.

---

## §4 Concerns, unproven (verdicts unchanged)

1. **Tredegar's mix.** If most of its 2017 sales were aluminium extrusions (a metals line the brief excludes), it belongs in the contrast group, and SG4's median rises from 3.93% to 4.35% (AEP, Appvion, Myers). Its segment sales were not re-read.
2. **What the other nine XBRL-only values cover.** For Transcat, Watts, Johnson Outdoors, Appvion, Myers, Tredegar, Advanced Drainage Systems, Oil-Dri and Omega Protein, the value is the filer's own tag, but the note was not read. American Vanguard shows the tag can sit on a freight-and-warehousing line. Oil-Dri's FY2017 10-K, read in full in two passes, gives no amount in its main document; it discusses "packaging and freight costs per ton" under gross profit and "truck, rail and ocean vessel availability".
3. **BEA's convention.** AT reads BEA's truck purchase as freight on inputs. A BTS methodology document, seen only as a search summary, says an industry's for-hire transport use covers moving its intermediate inputs plus certain direct services and "does not include the cost of moving its own output". That supports AT, so O and I are not double-counted. The BTS PDF returned 403, so this is *assumed*.
4. **CSCMP's private-fleet figure.** Supply Chain Digest gives growth for "Private/dedicated fleet". If CSCMP's $541.4B includes dedicated contract carriage, which is billed by a carrier, the 34% understates billed truck freight. Not shown.
5. **SOFA thresholds.** Payees under the reporting threshold are missing from both lists; small LTL carriers are the likeliest to be left out. Direction known (lists understate), size unknown.
6. **Distress.** Both payment lists cover the 90 days before a bankruptcy filing; Instant Brands' revenue in 2023 ran below its 2022 pace ($153.8M in five months). Payments may be lower or lumpier than normal.

---

## §5 Full verdict table

**Source key:**
- [FR16] https://data.sec.gov/api/xbrl/frames/us-gaap/ShippingHandlingAndTransportationCosts/USD/CY2016.json · [FR17] …/CY2017.json
- [RV] https://data.sec.gov/api/xbrl/frames/us-gaap/{SalesRevenueNet, Revenues, SalesRevenueGoodsNet}/USD/{CY2016, CY2017}.json (six files)
- [SUB] https://data.sec.gov/submissions/CIK##########.json (SIC codes; one per firm)
- [AVD] https://www.sec.gov/Archives/edgar/data/5981/000156459018005662/avd-10k_20171231.htm · [ODC] https://www.sec.gov/Archives/edgar/data/74046/000007404617000041/odc10k7312017.htm
- [WB] https://storage.courtlistener.com/recap/gov.uscourts.deb.184860/gov.uscourts.deb.184860.18.0.pdf · [IB] https://storage.courtlistener.com/recap/gov.uscourts.txsb.464138/gov.uscourts.txsb.464138.432.0.pdf
- [BEA] https://apps.bea.gov/industry/iTables%20Static%20Files/AllTablesIO.zip · [SUSB6] https://www2.census.gov/programs-surveys/susb/tables/2022/us_6digitnaics_rcptsize_2022.xlsx · [SUSBL] https://www2.census.gov/programs-surveys/susb/tables/2022/us_naicssector_large_rcptsize_2022.xlsx
- [SCD] https://www.scdigest.com/firstthoughts/26-06-26.php?cid=23144

**Tests:** 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search, 7 arithmetic. "Value ✓" means the freight value, its period and the revenue equal the SEC frame entries; the filing quote was not re-read unless stated.

| Claim ID | Verdict | New label | Evidence (source + value or quote ≤40 words) | Note |
|---|---|---|---|---|
| N-AT01 | KEEP-verified | *verified* | [FR17]: label "Shipping, Handling and Transportation Costs (Deprecated 2018-01-31)"; "Includes freight-out costs." | Tests 1, 2 |
| N-AT02 | KEEP-verified | *verified* | [FR16] 345 entries; [FR17] 284 entries | Test 7 |
| N-AT03 | KEEP-verified | *verified* | [FR17] EACO 2,760,000 (2016-09-01 to 2017-08-31); [RV] 156,954,000 | Value ✓ |
| N-AT04 | KEEP-verified | *verified* (revenue); freight not re-read | 2025 frame: EACO 427,931,000 (2024-09-01 to 2025-08-31) | Revenue ✓ |
| N-AT05 | KEEP-verified | *verified* | [FR17] Hillman 39,205,000; [RV] 838,368,000 | Value ✓. SG1 by code (B3) |
| N-AT06 | KEEP-verified | *verified* (XBRL) | [FR16] Transcat 900,000, period ending 2017-03-25; [RV] 143,898,000 and goods 72,795,000 | Value ✓; half services (B3) |
| N-AT07 | KEEP-verified | *verified* (XBRL) | [FR17] MSC 119,979,000; Applied 20,060,000; Watsco 47,670,000; Pool 45,247,000; [RV] 2,887,744,000; 2,593,746,000; 4,341,955,000; 2,788,188,000 | Value ✓. Pool is not SG1 by code (B3) |
| N-AT08 | KEEP-verified | *verified* | [FR17] Acme United 6,595,544; [RV] 130,550,349 | Value ✓. SIC 3420 (B3) |
| N-AT09 | KEEP-verified | *verified* | [FR17] Omega Flex 2,562,000; [RV] 101,799,000 | Value ✓. SIC 3430 (B3) |
| N-AT10 | KEEP-verified | *verified* | [FR17] P&F 2,017,000; [RV] 58,974,000 | Value ✓ |
| N-AT11 | KEEP-verified | *verified* | [FR17] Virco 19,299,000 (2017-02-01 to 2018-01-31); [RV] 189,287,000 | Value ✓ |
| N-AT12 | KEEP-verified | *verified* (XBRL) | [FR17] Watts 52,100,000; [RV] 1,456,700,000 | Value ✓. SIC 3490 (B3) |
| N-AT13 | KEEP-verified | *verified* (XBRL) | [FR17] Johnson Outdoors 10,844,000; [RV] 490,565,000 | Value ✓ |
| N-AT14 | KEEP-verified | *verified*; meaning ambiguous, as AT says | [FR17] AAON 11,400,000; [RV] goods 405,232,000 | Value ✓ |
| N-AT15 | KEEP-verified | *verified* (XBRL) | [FR17] Tootsie 43,973,000; [RV] goods 515,674,000 (total 519,289,000) | Value ✓ |
| N-AT16 | not re-checked | unchanged | — | 2025 10-K not re-read |
| N-AT17 | KEEP-verified | *verified* (2017 part) | [FR17] WD-40 16,400,000; [RV] 380,506,000 | 2025 part not re-read |
| N-AT18 | KEEP-verified | *verified* (2017 part) | [FR17] J&J 81,824,000; [RV] 1,084,224,000 | 2025 part not re-read |
| N-AT19 | KEEP-verified | *verified* (FY2017 part) | [FR16] JBSS 17,682,000 (to 2017-06-29); [RV] goods 846,635,000 | FY2018 not re-read (B2) |
| N-AT20 | KEEP-verified | *verified* | [FR17] Coffee Holding 2,412,000; [RV] goods 77,127,595 | Value ✓ |
| N-AT21 | KEEP-verified | *verified* | [FR17] Scott's Liquid Gold 2,614,300; [RV] 42,186,200 | Value ✓ |
| N-AT22 | KEEP-verified | *verified* | [FR17] Ocean Bio-Chem 1,226,000; [RV] 38,933,458 | Value ✓ |
| N-AT23 | KEEP-verified | *verified* | [FR17] Reed's 3,942,000; [RV] 37,714,000 | Value ✓ |
| N-AT24 | KEEP-verified | *verified* | [FR16] AEP 47,690,000 (to 2016-10-31); [RV] 1,095,830,000 | Value ✓ |
| N-AT25 | KEEP-verified | *verified* (XBRL) | [FR16] Paperweight Development 36,000,000; [RV] 690,364,000 | Value ✓ |
| N-AT26 | KEEP-verified | *verified* (XBRL) | [FR16] Myers 16,800,000, accession 0001564590-17-003837 | Value ✓ (B4) |
| N-AT27 | KEEP-verified | *verified* (XBRL) | [FR17] Tredegar 33,683,000; [RV] goods 961,330,000 | Value ✓; mix (§4 #1) |
| N-AT28 | KEEP-verified | *verified* | [FR17] Huttig 34,000,000; [RV] goods 753,200,000 | Value ✓ |
| N-AT29 | KEEP-verified | *verified* | [FR17] PGT 20,600,000; [RV] goods 511,081,000 | Value ✓ |
| N-AT30 | KEEP-verified | *verified* (XBRL) | [FR17] ADS 133,800,000 (2017-04-01 to 2018-03-31); [RV] goods 1,330,354,000 | Value ✓; own fleet as AT says |
| N-AT31 | not re-checked | unchanged | — | Not tagged; 10-K not re-read. SIC 1400 (B3) |
| N-AT32 | KEEP-verified | *verified* | [FR17] Compass 267,500,000; [RV] goods 1,364,400,000 | Value ✓ |
| N-AT33 | KEEP-verified | *verified* (XBRL) | [FR17] Oil-Dri 39,226,000 (2016-08-01 to 2017-07-31); [RV] goods 262,307,000. [ODC]: "Our freight costs are influenced by diesel prices, as well as by truck, rail and ocean vessel availability" | Value ✓; no amount in the main 10-K text (§4 #2) |
| N-AT34 | **NARROW** | *verified* (value); scope wider than freight | [AVD]: "Freight, delivery and warehousing costs for the year ended December 31, 2017 increased by $870 to $27,750"; "Domestic sales finished the year at $256,142" | §1 #1 |
| N-AT35 | KEEP-verified | *verified* (XBRL) | [FR16] Omega Protein 10,200,000; [RV] Revenues 390,831,000 | Value ✓. Taken over in December 2017 ([SUB]: DEFM14A, 25-NSE); irrelevant to a 2016 ratio |
| N-AT36 | **NARROW** | *verified* (amounts); fleet reading **[our call]** | [WB]: "Enterprise Fleet Management Total 149,715.92"; "Wex Fleet Total 86,181.46"; "Operating a business $98,552,915.00" | §1 #2 |
| N-AT37 | KEEP-verified | *verified*; classes **[our call]** | [IB]: 32 payees with reason "Other FREIGHT" totalling $7,401,282; "Operating a business $524,423,763.92" | Tests 1, 2, 7 (B6) |
| N-AT38 | KEEP-verified | *verified* (definition); inbound reading *assumed* via BTS | BEA glossary wording, as quoted in a search summary; BTS: use of for-hire transport "does not include the cost of moving its own output" (summary) | §4 #3 |
| N-AT39 | KEEP-verified | *verified* | [BEA] 2023 summary: food 311FT truck 38,685 of output 1,179,810 (3.28%); machinery 4,500 of 451,962 (1.00%); paper 3,623 of 203,354 (1.78%) | Test 7, all 14 rows |
| N-AT40 | KEEP-verified | *verified* | [BEA] 2017 detail: 311119 truck 2.88%, rail 2.42%; 322210 2.01%; 333415 1.08%; 325310 1.20% | Test 7, 24 of 24 |
| N-AT41 | KEEP-assumed | *assumed* (secondary) | [SCD]: "Parcel shipping costs were estimated at $241.3 billion, up from $229.5 billion in 2024"; "At $97.3 billion in 2025 -the same as 2024" | Tests 1, 5 |
| N-AT42 | KEEP-verified | *verified* | [SUSB6]: manufacturing "18: 100,000+" 7,464; wholesale 10,576 | Test 7 (B5) |
| N-AT43 | KEEP-verified | *verified* | [SUSBL]: manufacturing 3,527 / 1,464 / 980 / 715 / 778; wholesale 5,424 / 2,159 / 1,215 / 847 / 931 | Test 7 |

---

## §6 Counter-evidence and leads

| # | Source | What it says | Ties to | Type |
|---|---|---|---|---|
| 1 | BTS, Transportation Satellite Accounts methodology (https://www.bts.gov/sites/bts.dot.gov/files/docs/explore-topics-and-geography/topics/transportation-and-economy/220231/tsa-methodology_0.pdf), seen as a search summary | An industry's for-hire transport use covers moving its intermediate inputs plus certain direct services, not moving its own output; the wheat hauled to a mill is credited to the mill | N-AT38, AT5's I | Corroboration (*assumed*; PDF not opened) |
| 2 | American Vanguard 2017 10-K [AVD] | "When expressed as a percentage of sales, freight costs decreased slightly year over year to 7.8% in 2017, as compared to 8.6% in 2016." | §1 #1 | Context: the firm calls its freight-delivery-and-warehousing line "freight costs" |
| 3 | SEC frames [FR17], [RV] | KapStone tagged $299.872M of freight on $3,315.66M of sales (9.0%) | §AT1.3 SG4 note | Corroboration (B7) |
| 4 | SEC company profiles [SUB] | SIC: Acme United 3420; Omega Flex 3430; Watts 3490; EACO 5065; Intrepid 1400; Oil-Dri 3990 | AT1 segment labels | Counter-evidence to some segment labels (B3) |
| 5 | Supply Chain Digest [SCD] | Five-year growth: "Truckload: 4.8%"; "LTL: -3.1%"; "Private/dedicated fleet: 6.8%" | AT3 national mix | Lead: TL is growing faster than LTL; "private" may include dedicated (§4 #4) |

---

## §7 Could not access, and searches

**Blocked or unusable:**
- **www.sec.gov by direct download** (HTTP 403, "Undeclared Automated Tool") for six filing indexes. No contact header was supplied; the fetch tool was used for the filings read instead.
- **EDGAR full-text search** (HTTP 500).
- **BTS TSA documents** (HTTP 403 to both download and fetch tool).

**Downloads and API reads for this review (all 2026-10-09):** Census SUSB (2); BEA zip (1); court PDFs (2); SEC XBRL frames (8); filings and pages through the fetch tool (5); failed requests (9). Total 27. The AU review's 48 (including the SEC company profiles and 2025 revenue frames also used here) are listed there.

**Searches for this review (1 of the 14 run across both reviews; the other 13 are listed in the AU review):**
1. BEA input-output transportation costs, producers' prices, freight paid by producer, intermediate input.

**What this review did not do:** re-read the filing notes for the nine XBRL-only firms other than American Vanguard and Oil-Dri; re-read the 2025 filings of Tootsie Roll, WD-40 and J&J; re-read Intrepid's 2017 10-K; re-read N-K22 (CSCMP via FreightWaves) or check X's mode inputs.
