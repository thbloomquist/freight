# S5 check AU, adversarial review (counts only)

- **What this is:** an adversarial check of check AU's sized prospect list for C-09 shipper interviews. The founders will pick whom to call by estimated truckload + LTL spend, so a wrong revenue, a wrong segment, a missed parent company or a missed audit-and-pay (FAP) provider sends them to the wrong firms. Each sized firm was tested on five points:
  1. Is the revenue or staff figure at the source, for the year stated?
  2. Is the segment right (SG1-SG6 as in check Y §3.1; auto parts, primary and fabricated metals and homebuilders excluded)?
  3. Is there a parent, a private-equity owner or a recent acquisition the list missed?
  4. Is there public evidence of an FAP provider, a TMS or a 3PL?
  5. Does any job posting cited say what is claimed?
- **Files checked:** `research/s5_check_AU_c09_prospect_sizes.md` (method and counts) and the private list `freight_private/c09_prospects.md` (76 firms; 51 sized). Neither was edited.
- **Names are kept outside the project.** This file holds **counts only**. The per-firm verdicts, with names, corrected figures and sources, are in `freight_private/c09_prospects_review.md`.
- **Date:** 2026-10-09. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.** The call order is the founders' choice; the changes below are suggestions **[our call]**.
- **Fetches:** for this review, the *Electrical Wholesaling* 2026 file (1), SEC XBRL revenue frames and company facts (7), SEC company profiles and filing lists (29), job postings (4), firm contact pages (3), and the fetch tool on four pages (one results release, one 10-K, one case study, one firm news page that returned 403). Web searches: 13 of the 14 run across this and the AT review. The AT review lists the rest. Total across both reviews: 75 downloads and API reads, 14 searches.
- **No identity was sent. Nobody was contacted.** Downloads used a generic browser user-agent with no name or contact. SEC's data API answered it; SEC's main site refused it, and no contact header was supplied. No LinkedIn page, people-search or data-broker site was opened. Search results that pointed to data-broker profiles were not opened or used.
- **Labels:** **KEEP-verified**, **KEEP-assumed**, **NARROW**, **DISCARD**, as in the AT review. *verified*, *assumed*, **[our calc]**, **[our call]** as in the project.

---

## §0 Result in one table

| Test | Firms tested | Result |
|---|---|---|
| **1. Figure** | 51 sized | **45 re-checked at the source; 0 discarded.** 44 KEEP-verified, 1 KEEP-assumed (two secondary sources agree), 6 not re-checked (all six rest on staff counts or an award band for private firms). **1 figure corrected**, by 0.5% (no band change). **5 labels upgraded** from *assumed* to *verified* (the SEC's own XBRL revenue now confirms them) |
| **2. Segment** | 51 sized | **5 reassigned**: 2 to the excluded fabricated-metals group (their SEC SIC codes are 3420 and 3430); 3 outside the segment as defined (a printer, SIC 2761; a crop grower, SIC 0100; a commercial-laundry equipment dealer, SIC 7200). **3 boundary notes** (kept): a miner selling fertilizer (SIC 1400), a clay-products maker (SIC 3990), an electronic-parts and fastener distributor (SIC 5065) |
| **3. Ownership** | 26 public firms (SEC filing lists scanned); 12 private firms searched | **1 new subsidiary flag**: a sized public firm was **acquired and deregistered in May 2026** (now owned by a private competitor). **1 subsidiary flag confirmed** (parent owns about 87%, per its 10-K). **6 ownership events that change no flag** (a family control transfer, a new 21% holder, a large holder's exit, a bolt-on acquisition, a ready-mix joint venture, a multi-subsidiary holding company). **No change found** at the 11 private firms searched (12th: page silent) |
| **4. Provider** | 51 sized | **1 new provider flag**: a maker's 10-K says it uses "a global transportation management company". **1 confirmed** (an outside 3PL handles "freight audit and payment"; the page carries no date, so AU's stated date is not shown). One search for case studies naming three first-call makers found none |
| **5. Job postings** | 4 sized firms with postings | **2 confirmed live**, quotes exact. **1 confirmed but expired**; its full text adds that the coordinator dispatches the company's own drivers as well as outside flatbed and heavy-haul carriers, so its freight is own fleet plus flatbed truckload, not LTL. **1 no longer available** ("temporarily unavailable"), so its in-house evidence cannot be re-read |
| **Privacy** | both private files | **No breach found.** No email address, personal phone, home address, guessed email, LinkedIn page or data-broker source. People are named by role only. 3 of 25 phone numbers spot-checked against the firm's own contact page: all 3 match |

**What changes in AU's counts [our calc]:**
- Public / private among the 51: **28 / 23 → 27 / 24** (one firm went private through the acquisition).
- Subsidiaries among the 51: **1 → 2**. Public provider evidence among the 51: **2 → 3**.
- Flagged FAP-size or subsidiary: **10 → 11 of 51**. Any provider flag (FAP-size, subsidiary or provider evidence): **12 → 14 of 51**.
- AU §5 item 1, "independent firms at $3-10M, unserved, in segment": **23 → 19** (one acquired, one with a transportation-management provider, two outside their segment).
- In-house job evidence among the 51: 4, of which **2 can still be read live**.

---

## §1 Narrowings and corrections (most important first)

| # | Where in AU | What was claimed | What the source says | Verdict | Why |
|---|---|---|---|---|---|
| 1 | One $6-15M firm (public, SG3) | Public; no subsidiary flag | SEC filing list: a deregistration form (15-12G) filed in May 2026; search summary: a merger agreement with a private competitor signed in March 2026, approved by stockholders, and a completion headline on the firm's news list | **NARROW** (ownership) | Now a subsidiary of a private group, which may impose its own freight arrangements. A search summary also says the firm sold its direct-ship business in 2023, leaving mostly route delivery on its own trucks (*assumed*). Move to contrast or drop |
| 2 | One $3-6M firm (public, SG3) | No provider evidence ("uses co-packers, *assumed*") | 10-K FY2025 (Item 1): the firm says it uses "a global transportation management company", alongside outside freight and warehouse providers and contract manufacturers | **NARROW** (provider) | A managed-transportation provider usually books and pays the freight. Move to contrast |
| 3 | Two firms in SG2 (one $3-6M, one $1-3M) | SG2 capital goods | SEC SIC 3420 (cutlery, hand tools and hardware) and 3430 (plumbing fixtures and heating equipment), both in the fabricated-metal major group | **NARROW** (segment) | The brief excludes fabricated metals. One is already a contrast firm (subsidiary); the other was not in the call order |
| 4 | Three firms placed in SG4, SG6 and SG1 | In segment | SIC 2761 (manifold business forms, i.e. printing); SIC 0100 (crop production); SIC 7200, a distributor of commercial laundry equipment | **NARROW** (segment) | Outside the NAICS codes in check Y §3.1 (322 etc.; 3111, 3112, 3253, 42491, 4245; 4237, 42361, 42384). The grower's packing and selling arm would fit SG3's grocery-wholesale variant at most |
| 5 | One $1-3M firm with an in-house posting (SG5) | Posting puts "freight invoice reconciliation" with a logistics coordinator | Posting (expired): the coordinator dispatches company drivers and outside flatbed, step-deck and heavy-haul carriers, and reports freight cost per load and trailer use (paraphrased to keep the firm unidentifiable) | **KEEP-verified**, caution added | The quote is exact. Its freight is own fleet plus flatbed and heavy-haul truckload; LTL error types (reweighs, reclasses) will be rare. The posting has expired |
| 6 | One $6-15M SG6 firm with a weak posting | Posting on freight vendor management and accruals | Posting URL now returns "This job posting is temporarily unavailable" | **KEEP-assumed** (was weak) | The quote cannot be re-read today |
| 7 | One SG3 firm's revenue | about $229.8M **[our calc]** from a percentage change | SEC XBRL: $230,986,000 for the fiscal year to 2025-10-31 | **Corrected** | 0.5% higher; same band. AU's coincidence note (data tables show $230.99M) was right |
| 8 | AU §1.2 sales per employee, "26 firms … lower quartile $0.88M, median $1.36M" | as stated | Re-computed from the same file: 27 firms give both figures; lower quartile $0.89M, median $1.34M, upper quartile $2.12M (AU: $2.21M) | **KEEP**, minor | One firm's inclusion differs. The staff-based estimates move by under 2% |
| 9 | One $1-3M SG6 firm with provider evidence | The outside firm's case study is dated 2021-04-15 | Case-study page: no date shown; the firm "relies on [the 3PL] for LTL, parcel, freight audit and payment, truckload and international" | **KEEP**, date not shown | The provider flag stands. The date is not on the page |

**Coincidences tested (AU §6 list):**
- **"Same executive at two firms" (AU coincidence 2):** confirmed. The two rows in the *Electrical Wholesaling* file carry the same senior-executive name. Common ownership or a data error is still untested; treat the two as possibly one buyer, as AU says.
- **One firm appears in both AT4 and AU** with revenue estimates about 3× apart ($135-315M against $50-100M), both from staff counts on different bases. Both *assumed*; ask on the call.
- **Electrical ranking figures** (17 firms): all 17 match the downloaded file exactly. The file's note marks acquisitions in 2026 with "#"; no row carries it.
- **Revenue labels:** the 5 upgraded firms' revenues equal the SEC XBRL values exactly. AU's search-summary figures were right in every case re-checked.

---

## §2 Effect of check AT's ratios on the bands [our calc]

AU's bands use a flat 2.5% of revenue. Check AT proposes segment centrals (SG1 1.14%, SG2 2.565%, SG3 3.83%, SG4 3.24%, SG5 3.475%, SG6 5.15%; the AT review flags SG6 as high). Re-banding the 51 sized firms on AT's centrals, using AU's own revenue figures:

| | $1M or less | $1-3M | $3-6M | $6-15M | $15M+ | FAP-size ($10M+) |
|---|---|---|---|---|---|---|
| AU (2.5%) | 0 | 18 | 13 | 20 | 0 | 9 |
| On AT's centrals | 6 | 13 | 15 | 12 | 5 | 10 |

- **33 of 51 firms change band.** The direction follows the segment: every SG1 distributor falls (to 1.14% of revenue), and every SG3, SG4, SG5 and SG6 firm rises.
- **No SG1 firm stays FAP-size;** five SG1 firms leave the FAP-size group, and six SG3-SG6 firms (five makers and one farm-supply retailer) join it.
- **Six small SG1 distributors fall below $1M of TL+LTL.**
- This is the coordinator's recompute to make; it is shown because it moves the call order (§3). The AT review's warning applies: every AT central rests on judgement inputs.

---

## §3 Call order: suggested changes [our call]

By count (the S-IDs are in the private review):
- **Move out of the first-call groups (to contrast, or drop): 4 firms.** One acquired (§1 #1), one using a transportation-management provider (§1 #2), two outside their segment (§1 #4).
- **Excluded: 1 more firm** (fabricated metals, §1 #3), not in the call order before. The other fabricated-metals firm was already a contrast firm.
- **Lower within the list if AT's ratios are adopted: 7 SG1 distributors** in AU's group 4, now $1.5-3.7M central.
- **Raise if AT's ratios are adopted: 6 makers** (4 food and beverage, 2 building-materials), now $3.2-8.9M central. One of the two building-materials firms is the expired-posting firm (§1 #5), whose freight is own-fleet plus flatbed.
- **Keep, with a note: AU's group 1 (3 makers) and group 2 (1 distributor) stand.** One group-1 maker is a holding company with several boiler subsidiaries, so ask which subsidiary books the freight. The group-2 distributor's posting and family ownership were confirmed; on AT's SG1 ratio its central falls from $8.3M to $3.8M.

---

## §4 Concerns, unproven

1. **Six private size figures were not re-checked** (staff counts and one award band). They were already *assumed* or **[our call]**.
2. **25 unsized leads were not re-checked.** Their postings come from check Y and were not re-fetched here.
3. **Provider status is unknown for most firms.** No per-firm provider search was run for 47 of the 51; one combined search found nothing for three first-call makers. Absence in a search is not evidence of no provider; screener Q7 remains the test.
4. **Material-agreement filings were not read.** About ten of the public firms filed 8-Ks with item 1.01 or 2.01 in 2025-26. They may be loans, asset sales or acquisitions. None of them is a change-of-control filing (item 5.01), apart from the family transfer counted in §0.
5. **Segment by code against segment by end market.** SIC codes are the SEC's, and a firm's freight follows its products, not its code. The five reassignments follow the brief's NAICS lists; the founders may prefer an end-market rule (as check AT does for one firm).

---

## §5 Sources by type (no firm names)

| Type | Used for | Count |
|---|---|---|
| *Electrical Wholesaling* 2026 Top 100 download | 17 SG1 figures, the sales-per-employee quartiles, the same-executive test | 1 file |
| SEC XBRL frames and company facts (data.sec.gov) | revenue of 26 public firms | 7 |
| SEC company profiles and filing lists (data.sec.gov) | SIC codes; deregistration, merger and 13D filings | 29 |
| Firm results releases and filings through the fetch tool | one revenue (an OTC firm not filing with the SEC), one 10-K's logistics text | 2 |
| Job postings (the four check Y URLs for sized firms) | test 5 | 4 |
| Firm contact pages | phone spot-check | 3 |
| Vendor case study | provider test | 1 |
| Web searches | ownership (11 private and 6 public firms), provider case studies, one revenue corroboration | 13 |

**Could not access:** one firm's own news page (HTTP 403); SEC's main site by direct download (refused; read through the fetch tool where needed).
