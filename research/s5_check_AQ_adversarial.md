# S5 check AQ, adversarial review

- **What this is:** an adversarial check of check AQ's web evidence on the customer's side of C-09 (minutes per exception, follow-through, who files, buying friction, security demands). Each claim was tested to see whether it breaks. No objection was invented: a claim that survives is reported as a result too.
- **File checked:** `research/s5_check_AQ_c09_customer_review.md` (84 ledger rows C-AQ01 to C-AQ85, C-AQ43 dropped by the researcher; the §0 table; body sections; the Coincidence watch). It was not edited. No other project file was read except `research/s5_check_AM_adversarial.md`, for format.
- **Date:** 2026-10-08. Everything was fetched on that date.
- **Status:** input to S5. **It decides nothing.**
- **Searches used:** 10 of the 10 allowed. **Fetches made:** about 75: page and PDF downloads (curl), Wayback raw copies, one WebFetch extraction (Ardent's 2026 post, which refuses curl) and one failed WebFetch (Gartner, 403). Downloads are kept in the session scratchpad, outside the project.
- **No identity was sent. Nobody was contacted.** A generic browser user-agent was used. No logins, forms, API keys or PACER. SEC EDGAR was not fetched.
- **Rows checked in full (all seven tests):** 33 of the 35 load-bearing (Y) rows, plus 7 N rows that feed a §0 number or reading (C-AQ32, 45, 51, 52, 58, 64, 59).
  - **Y rows not fully checked:** C-AQ21 (CRF minutes per deduction) and C-AQ34 (CRF write-off thresholds) rest on check AH's CRF sources, whose URLs are not in AQ. One search did not find them. C-AQ34 was tested for meaning against CRF's own 2012 deck; C-AQ21 was not checked.
  - **Sampled:** 38 N rows, at least the existence test, covering every question AQ1-AQ5.
  - **Not checked:** 5 rows. C-AQ21 (above); C-AQ40, 53 and 54 (pages gone, timed out or script-rendered); C-AQ62 (no URL given).
- **How labels are used here:** **KEEP-verified** means the row's own sentence is true as written about its own population (an Australian calculator, a large-firm AP survey, one vendor's page). Where that population is not our segment, the note says so. **KEEP-assumed** means the number itself is a vendor figure, a self-report, a snippet or a relay. **NARROW** gives the smaller reading that survives. **DISCARD** means the only readable copy contradicts the number.

**Words used here:**
- **AP exception:** an invoice held for a person to look at, for any reason (coding error, missing PO, approval bottleneck). **Not** the same unit as a freight-bill flag (a suspected overcharge with the proof on screen).
- **Supplier-facing time:** AP staff time spent dealing with suppliers about invoice and payment problems. Ardent tracks it as a share of staff time.
- **Implied n:** the smallest number of respondents for which every percentage in a chart rounds correctly. It shows how many people answered a question.
- **Look-alike:** two equal-looking numbers that measure different things.
- **Self-serve dispute channel:** a portal button or form through which a shipper files a billing dispute without contacting a person.

---

## §0 Result in one table

**Row verdicts**

| KEEP-verified | KEEP-assumed | NARROW | DISCARD | Not checked |
|---|---|---|---|---|
| 45 | 18 | 15 | **1** | 5 |

**One row is discarded:** C-AQ83, the Gartner Peer Community poll. The only readable copy (Wayback, 2023-10-01) shows 263 participants: 8% do no reviews, 38% call them box-checking, 28% say they delay purchases without changing outcomes. The snippet's 288 votes with 5% and 39% cannot follow from it, because votes cannot fall.

All of check AQ's own **[our calc]** reproduce. What breaks is how some numbers are read:
- D2's "10-12 minutes per exception" divides **supplier-facing time** (Ardent's own words) by invoice exceptions. Other denominators and the 2025 edition give 7-14 minutes;
- JOC's $19.49 for "small/medium" shippers rests on **at most 15 respondents**. The "77 shippers" behind several JOC figures were in fact 41-72 answers per question;
- the workload table treats generic AP exception rates as freight-flag rates;
- Freightview's self-serve trial and card billing are shown only for its **0-50 shipments a month** tier. A $2M customer sits in the "Call now" tier;
- a truckload shipper platform (Transfix) does have a self-serve "Dispute" button;
- FreightPOP describes itself as built for **mid-market and enterprise** shippers, not SMB;
- Pittsburgh's security trigger includes data sharing and integrations, not only personal data;
- G2's 1-250-employee column sums to **107%**.

**Verdicts on the §0 question rows**

| Question | Proposed verdict | This review | Reason |
|---|---|---|---|
| AQ1 minutes; exception rates | Narrowed | **AGREE**, with three corrections | ATO's 15 and 20 minutes are exact (Table 4 calls them "Generic" defaults). D2 is not a "neutral AP benchmark" of handling time. Ardent's own 2018 text defines the 24% as time "working directly with suppliers to fix invoice processing, and payment errors". The range is 7-14 minutes depending on the denominator and edition (§1 #1). The ocean 60-150 minutes is one NVO executive's experience, not a shipper's (§1 #6). JOC's small/medium $19.49 rests on ≤15 respondents (§1 #3). A counter-search found no neutral timed figure; vendor pages put exceptions at 15-60 minutes. The "only measurable in the timed look-back" verdict stands. |
| AQ2 work the queues; hours | Narrowed / not answerable | **AGREE**, with wording fixes | Tolerance behaviour is corroborated by a second TMS vendor (UltraShip's $50 example). The "only perform spot checks" line is CTSI's own claim, not Gartner's (B1). CRF's write-off threshold applies only to firms that auto-write-off: 17% yes, 19% by type, 65% no in CRF's 2012 survey (§1 #7). Ascent's 5 hours a week sits beside its own "50 hours per week" claim. The public buyer in AQ5 (Pittsburgh) itself "completes a spot audit" before payment. Follow-through remains not answerable from the web: two counter-searches found no measurement. |
| AQ3 who files; channels | Narrowed | **AGREE**, with two corrections | The 2016 survey counted shippers **and 3PLs**, and it measured who owns freight payment, not who files disputes (§1 #8). JOC's decision-maker split has an implied n of 43, not 77 (§1 #9). **A truckload shipper platform has a self-serve dispute button for accessorials** (Transfix Shipper App, updated 2026-07-10), so "no public self-serve channel for TL" is too broad. The 11 named firms still publish none (§1 #4). |
| AQ4 buying friction | Narrowed | **AGREE**, with two corrections | G2's "76% involve four or fewer" comes from a column summing to 107%; normalised it is 71% (§1 #10). Freightview's trial and monthly billing cover the 0-50 shipments tier, and a $2M customer (≈313-368 bills a month) is in the "Call now" tier (§1 #5). The inference "bought like the TMS, not through a procurement cycle" is therefore unsupported at our reference size. |
| AQ5 SOC 2 before upload | Narrowed | **AGREE**, with three corrections | FreightPOP calls itself "built for mid-market and enterprise shippers" (§1 #11). Pittsburgh's trigger lists "data moving between the University and Contractor systems, system integrations … the University data being shared", not only personal data (§1 #12). The Gartner poll numbers are replaced (DISCARD, §1 #2). JOC's security confidence rests on 41 answers (§1 #9). Whistic, read in full, says its respondents "worked primarily for mid-sized enterprises" averaging 1,332 employees, far above our segment. |

---

## §1 Discards and narrowings (most important first)

One row is discarded and fifteen are narrowed. Eight body statements need the same treatment (B1-B8 below the table).

| # | Claim ID | What was claimed | What the source actually says (quote ≤40 words) | Verdict | Why, and the restricted reading |
|---|---|---|---|---|---|
| 1 | **C-AQ15** (and C-AQ14, §0 AQ1, §AQ1.4 #1) | APQC invoices per FTE × Ardent 2018's "24% of their day" on exceptions gives ~10-12 minutes per AP exception, read as a neutral benchmark of review time | Ardent's own 2018 post (CPO Rising mirror, 2018-06-22): "24% of the average AP staff's time is spent working directly with suppliers to fix invoice processing, and payment errors." Same series (2018-06-08): "fully 12% of all payments are contested by suppliers." | **NARROW** | The arithmetic is right (§3). But the 24% is supplier-facing time on invoice **and payment** errors, and Ardent's later editions track it as "staff time dealing with suppliers" (21.9% in 2025). Adding the 12% contested payments to the denominator gives **7.1-7.8 minutes**; the 2025 pair (21.9% ÷ 18.4%) gives **12.4-13.7** **[our calc]**. **Restricted reading:** a ratio of an Ardent time-share (a sponsored analyst survey, mostly firms over $250M) to an APQC snippet value: **7-14 minutes of supplier-facing time per AP problem**. It is not a timed review of one exception, and not neutral. |
| 2 | **C-AQ83** | Gartner peer poll (288 votes): 5% do no vendor security reviews, about a third call them box-checking, 39% say reviews delay purchases without changing the outcome | Wayback copy of 2023-10-01: "None, we don't perform vendor security reviews 8 % … mostly a box-checking exercises 38 % … delay purchases but they don't change outcomes 28 % … 263 PARTICIPANTS" | **DISCARD** (the numbers) | 8% of 263 is 21 votes; 5% of 288 is 14. Votes cannot fall, so the snippet's figures cannot be a later state of this poll. The live page refuses access (403). **Replacement, if used at all:** in a self-selected poll of 263 (by Oct 2023), 8% did no reviews, 38% called them box-checking and 28% said they delay purchases without changing outcomes. The poll is mostly large-firm readers; the one visible comment is from a 10,001+ employee firm. |
| 3 | **C-AQ19** (and C-AQ20, §AQ1.4 #3) | Shippers reported $18.32 in-house and $19.49 at small and medium shippers per freight invoice (77 shippers) | JOC p. 3: "roughly three-quarters of them belonging to organizations with $1 billion or more in annual revenue"; Fig. 7 company size: 38.6%, 35.1%, 21.1%, 5.3% | **NARROW** | The figures are exact. Fig. 7 fits only **n = 57** answers (22 large, 20 very large, 12 and 3 in the two bands under $1B) **[our calc]**. So "small/medium" is **at most 15 shippers**, of which 3 are $500M-$1B. The survey does not define what the cost includes. **Restricted reading:** about 15 self-reporting shippers under $1B revenue, all modes including ocean, put an undefined per-invoice cost at $19.49 in mid-2020. "Freight invoices cost about twice a generic invoice" sets that against Ardent's 212 mostly large AP teams, a different survey, year and definition: a hint, not a ratio. |
| 4 | **C-AQ55** (and §AQ3.3 #2, §0 AQ3) | No public self-serve dispute portal or window for TL carriers or large brokers; "for TL and broker freight there is no public self-serve channel to target" | Transfix Help Center (updated 2026-07-10): "If you click on Dispute you'll have the opportunity to Edit or Remove an accessorial that was added on by the carrier, and you'll be prompted for an explanation" | **NARROW** | For the 11 named firms the absence holds: a counter-search also found no shipper dispute feature at J.B. Hunt 360, Navisphere, Uber Freight or Schneider, and RXO, Uber Freight, TQL and Arrive terms were re-read. But a truckload shipper platform has a dispute button, though only for carrier-added accessorials. **Restricted reading:** the large TL carriers and brokers searched publish no self-serve dispute channel; at least one TL shipper app (Transfix) offers in-app accessorial disputes. Whether customers' carriers sit on such platforms is an interview question. |
| 5 | **C-AQ64** (and §AQ4.4 #2, §0 AQ4) | Freightview sells on a 14-day free trial with monthly billing, so a small subscription is bought like the TMS, not through a procurement cycle | Freightview pricing: "0-50 ships per month $149 / mo 51-500 ships per month Call now 501-1000 ships per month Call now"; FAQ: "Can I pay for a whole year at once? Sure! Talk to your Freightview consultant" | **NARROW** | The trial and monthly-billing quotes are exact. But the only posted price is for 0-50 shipments a month. A $2M TL+LTL customer gets about 313-368 bills a month (AQ's own table), which is the "Call now" tier. The Invoice Matching add-on also needs a support request ("Contact our Support Team to get started"). **Restricted reading:** the smallest Freightview tier is self-serve; at our reference size, pricing is sales-led. The inference about procurement cycles does not reach a $2M shipper. |
| 6 | **C-AQ22** (and D6, §AQ1.4 #2) | Resolving one disputed ocean invoice takes 6-10 calls of 10-15 minutes, 60-150 minutes (NVO and shipper panelists) | FreightWaves 2017, an NVO's sea-freight VP: "An NVO doesn't have a lot of time to vet the invoice … It's usually six to 10 phone calls in our experience to resolve that." Later: "Each phone call can take 10 to 15 minutes." | **NARROW** | Both statements come from one speaker at a forwarder (NVO) disputing ocean carriers' bills, not from a shipper. "Can take" is an upper description, not an average. **Restricted reading:** one NVO executive's experience of ocean disputes in 2017: up to 60-150 minutes of calls. Not a shipper's TL or LTL dispute. |
| 7 | **C-AQ34** (and §AQ2.2, §AQ2.4 #1) | Suppliers of $500M or less write off retail deductions under a median $10-25 "without looking" | CRF 2012 deduction survey (493 companies): "Do you automatically write off chargebacks below a certain value without investigation 17% 19% 65% Yes Depends on type No"; median "< $25.00" | **NARROW** | The 2021 and 2023 figures could not be re-read (check AH's sources; no URL in AQ). CRF's own 2012 deck shows the median threshold applies only to the firms that have one. Then 17% wrote off automatically, 19% did for some deduction types and 65% did not. **Restricted reading:** among suppliers that auto-write-off (a minority in 2012), the median threshold is about $10-25. It does not show that most suppliers let small deductions go. |
| 8 | **C-AQ44** (and §0 AQ3, §AQ3.3 #1) | Over three quarters of larger shippers see freight payment as a logistics duty, against barely half of smaller shippers (208 freight payers) | American Shipper 2016: "based on a benchmark survey of 208 freight payers (shippers and 3PLs), who were asked about their transportation invoice processing and payment practices" | **NARROW** | The quote is exact. But the 208 include 3PLs. "Larger" means $1B+ revenue ("Large shippers (those with $1 billion or more in revenue)"), so "smaller" is everything below, far above our segment. The question was who is responsible for freight payment, not who files disputes. **Restricted reading:** in 2016, freight payers under $1B split about half and half between logistics and other functions for **payment ownership**. Who files disputes is not measured. |
| 9 | **C-AQ46** and **C-AQ80** | JOC 2020 (77 shippers): decision-maker on audit-and-pay technology 11.6 / 60.5 / 27.9%; confidence in the provider's security 26.8 / 63.4 / 7.3 / 2.4% | JOC Fig. 1 area: "Finance Combination of logistics and finance Logistics 11.6% 60.5% 27.9%"; Fig. 5: "7.3% 63.4% 26.8%", "Uncertain 2.4%" | **NARROW** | The percentages are exact. They fit only **n = 43** (5 / 26 / 12) and **n = 41** (11 / 26 / 3 / 1) **[our calc]**. **Restricted reading:** 43 and 41 respondents, three-quarters from $1B+ firms. The security question covers only shippers using an outside provider. |
| 10 | **C-AQ58** (and §AQ4.4 #2) | At firms of 1-250 employees, 76% of software purchases involve four people or fewer | G2 2025 heat map, 1-250 column: 1 person 12%, 2 people 22%, 3 people 24%, 4 people 18%, 5-8 13%, 8-12 7%, 12-20 8%, 20+ 1%, don't know 2% | **NARROW** | 12+22+24+18 = 76% is right. But the column sums to **107%**, while the other three columns sum to 99-101% **[our calc]**. G2 says "Generative AI was extensively used to … analyze results." Normalised, the share is **71%**. **Restricted reading:** roughly seven in ten (71-76%) purchases at 1-250 employees involve four people or fewer, on a chart that does not add up. |
| 11 | **C-AQ69** (and §AQ5.4 #2: "one SMB tool now has it") | FreightPOP, an "SMB TMS with an audit module", states SOC 2 Type II | FreightPOP security page: "FreightPOP is an AI supply chain software platform built for mid-market and enterprise shippers." Heading: "Built for the security standards enterprise shippers require" | **NARROW** | The SOC 2 statement is exact (Prescient Assurance, report dated 21 May 2026, on request). But the company positions itself for mid-market and enterprise. **Restricted reading:** a TMS sold to mid-market and enterprise shippers states SOC 2 Type II. It is evidence for "SOC 2 is a selling point upmarket", not for an SMB tool holding it. |
| 12 | **C-AQ78** (and §AQ5.4 #3) | Pittsburgh asks for a security assessment only if data criteria are met; "the trigger is the *kind* of data (personal, health, student), which freight bills mostly are not" | RFP §1.13: "based on criteria such as data moving between the University and Contractor systems, system integrations, Contractor access to the University networks, and/or the University data being shared with the Contractor, whether the data is personal identifiable information" | **NARROW** | No SOC, SSAE or ISO 27001 appears in the RFP (text search), as AQ says. But the criteria list data sharing and integrations **before** the data type. Uploading the University's invoices to a vendor is "University data being shared". **Restricted reading:** an assessment "may" be required; data sharing, integrations and personal data are all named criteria. Whether freight bills alone trigger it is not stated. Context: the programme is $434,000 a year, 99% parcel shipments (11,532 of 11,646). |
| 13 | **C-AQ14** | Ardent 2018 put the exception rate at 23.2% and time on exceptions at 24% of the staff day | FleetOwner (a procurement-firm CEO's column) quotes "correcting and managing invoice exceptions, which comprises 24% of their day"; Ardent's own post: "working directly with suppliers to fix invoice processing, and payment errors" | **NARROW** | The relay is accurate to its own text. Ardent's original wording is supplier-facing time on invoice and payment errors. Ardent's 2018 split also fails to reproduce its own average: "10.7% vs. 22.9%" (best-in-class vs others) cannot give 23.2%. **Restricted reading:** in 2018, Ardent reported 23.2% of invoices held as exceptions, and 24% of AP staff time spent with suppliers on invoice and payment errors. |
| 14 | **C-AQ41** (and the §AQ2.3 table, §0 AQ2) | A $2M customer would see 44-214 flags a month, or 4-53 reviewer hours at 6-15 minutes a flag | Ardent p. 17 defines its exceptions as "Invoices flagged due to coding errors, missing information, approval bottlenecks, lack of purchase order data, etc." | **NARROW** | Every cell reproduces (§3). But the 14% and 18.4% rows are generic AP holds (coding, approvals, PO data), a different unit from a freight overcharge flag. AQ's own §AQ1.4 #4 says so. The only freight-bill rate is the ABF set's 58% (one LTL account; "needs a document"). The minutes are the generic AP ones (see #1). **Restricted reading:** at 58% of bills needing a look, 182-214 items a month and 18-53 hours at 6-15 minutes. The Ardent rows are a sensitivity, not the bottom of a range. |
| 15 | **C-AQ51** | TQL's customer credit packet sets net 30 and a nine-month cargo window and has no invoice-dispute clause; "text search for 'dispute': none" | TQL packet: "exclusive venue with respect to any claim, counterclaim, dispute or lawsuit arising in connection with any transactions, loads"; PDF creation date 2015-09-11 | **NARROW** | No invoice-dispute clause, as AQ says. But "dispute" occurs once, in the venue clause, and the copy (hosted by a customer) was made in **2015**. **Restricted reading:** TQL's 2015 credit packet had no invoice-dispute clause. Current terms are not shown. The same packet asks "may we exclude bills of lading from your invoice?" (§6). |

**Body statements (not ledger rows) that need the same treatment**

- **B1. §0 AQ2: "Gartner (2018, via a vendor): 30% of shippers had no audit-and-pay system, and in-house shippers 'only perform spot checks'".** In CTSI's 2021 post (read on Wayback, live 403) the spot-check sentence comes before Gartner is mentioned, as CTSI's own inference: "This explains why many shippers that choose to handle their own auditing ultimately only perform spot checks". Only the 15-20%, 30% and 25% are attributed to Gartner. The ledger (C-AQ24) has it right; §0 and the §AQ2.2 table merge them.
- **B2. §AQ1.4 #1: "Reviewing one exception takes about 10-15 minutes in the neutral AP benchmarks (D1, D2)".** Only D1 (ATO) is from a neutral body. Its Table 4 heads the column "Generic time to correct", and the page attributes its "average cost data" to Deloitte Access Economics estimates from 2016. D2 is a derived ratio of supplier-facing time (§1 #1). **Better wording:** "one neutral calculator default (15 minutes) and one derived ratio (7-14 minutes); neither times a flag".
- **B3. §AQ1.4 #4 and the Coincidence watch, "the 2025 split does not reproduce its own average".** This is confirmed, and it is a recurring Ardent pattern. In 2018 the split was 10.7% / 22.9% against an average of 23.2%. Ardent called that "114% lower", which no ratio gives. Note also that MTM 2025's split implies 19.4%, close to the State of ePayables 2025 figure of 18.4%. **The 14% is the outlier**, not the 18.4%.
- **B4. §AQ4.4 #2, "a small subscription is bought like the TMS the shipper already uses, not through a procurement cycle".** See §1 #5 and #10: the posted self-serve price stops at 50 shipments a month, and the 1-250 G2 column does not add up.
- **B5. §AQ3.3 #2, "For TL and broker freight there is no public self-serve channel to target".** See §1 #4.
- **B6. §AQ5.4 #2 and #3.** See §1 #11 and #12.
- **B7. Upgrades.** C-AQ52 (Arrive): the page loaded here (HTTP 200) and both quotes are verbatim, so the row is *verified*, not snippet-based. C-AQ42 (alert fatigue): the SC World article was read on Wayback (150 practitioners, 54%), so it is *verified* (that reported), still a security analogue.
- **B8. §AQ2.3 hours, Ascent's "5 hours a week" (C-AQ36).** The same vendor's 2020 blog says "On average, we save clients 50 hours per week". The two figures differ tenfold. The 5 hours is a "streamlined process" example on its own brochure, with 4-6% of invoices wrong at $270 each.

---

## §2 Coincidences found

**Shared origins (merge them into one source)**

| Figures | Rows | Single origin | Effect |
|---|---|---|---|
| 24% (2018), 21.9% (2025), 26.9% / 13.4% (MTM 2025) | C-AQ14, 15, 13 | **Ardent's supplier-facing time series** | D2's "time on exceptions" is this series under another name. Use it as supplier-contact time. |
| 14%, 18.4%, 9.0 / 22.0%, 23.2%, 10.7 / 22.9% | C-AQ08, 09, 13, 14 | **One publisher (Ardent), annual surveys** | The splits fail to reproduce the averages in two editions (2018 and MTM 2025). Treat Ardent's best-in-class splits as not combinable with its averages. |
| "12.5 min" and "4.8 min" | C-AQ17, 18 | **Nexus AP's own bottom-up model** ("Estimate, not survey data") | ImageToTable labels the same two numbers "IOFM 2024" and "Ardent basic automation". One model, relabelled. AQ's orphan flag is confirmed. |
| "15-45 minutes per exception" | C-AQ17; a Hyperbots glossary (search summary) | **AI-tool vendors, no traceable origin** | Two mouths, no source. Stays an orphan. |
| $50 TL tolerance | C-AQ25 (Freightview); UltraShipTMS in *Inbound Logistics* (§6) | **Illustrative round numbers from two TMS vendors** | Independent vendors, same pattern: tolerance features are standard. Both are examples, not customer settings. |
| SoE 2025 sample n=204 | C-AQ13 | A vendor page (Nexus AP) | Confirmed on Nexus's page: "(Ardent Partners, State of ePayables 2025, n = 204)". The Ardent post itself states no sample. |
| American Shipper 2016, FreightWaves 2017, JOC 2020 | C-AQ44, 47, 46 | Probably one research lineage (AQ's watch) | Confirmed in FreightWaves 2017: "American Shipper tracks this discipline annually through its Freight Payment Benchmark Study". |
| Ascent 5 h / week and 50 h / week | C-AQ36; §6 | **One vendor, two marketing pages** | Not two data points; a tenfold internal spread. |
| "85% … require SOC 2" | C-AQ85 | Compliance-vendor blogs | Bright Defense's version says "85% of **enterprise** buyers require SOC 2 reports before signing contracts", with no source. The qualifier drops out in other mouths. |

**Look-alike numbers (equal values that measure different things)**

| Value | Where it appears | What each measures |
|---|---|---|
| "77 shippers" | C-AQ19, 32, 46, 80 | The survey total. The answers behind each chart are 72 (Fig. 1, role), 57 (company size), 43 (decision-maker) and 41 (security confidence) **[our calc]**. |
| ~10-15 minutes | ATO "processing exception" 15; D2 7-14; model's 6-minute flag | A calculator default for an AP investigation; a supplier-facing time ratio; our design assumption for a pre-explained flag. Three different things. |
| 4.8 | Whistic 4.8 **days** to return an assessment; Nexus 4.8 **minutes** per invoice with OCR; ImageToTable "Ardent basic automation 4.8 min" | A security-review delay; a vendor model; a misattribution (already flagged by AQ). |
| $50 | Freightview TL tolerance example; UltraShip example | Settings shown for illustration, not measured tolerances. |
| 30 days | TQL net 30; Arrive due in 30 days; C.H. Robinson's 30-day ocean dispute window (snippet); Uber Freight's notice before arbitration | Payment due dates, a dispute window and a pre-arbitration notice: different clocks. |
| "mid-sized" | Whistic's "mid-sized enterprises" (mean 1,332 employees); Ardent's "Mid-market ($250M-$1B)"; our "mid-sized shipper" ($0.5-5M of freight spend) | Three different size bands. None of the surveys reaches ours. |
| 24% | ATO: exceptions on 24% of invoices; Ardent 2018: 24% of staff time with suppliers | Already flagged by AQ; confirmed. |

**Circular or indirect citations**
- C-AQ21, C-AQ34 and C-AQ36 cite earlier checks (AH, AN) instead of a verbatim passage. C-AQ36 was re-read at the source (Ascent's 2020 brochure). C-AQ21 and C-AQ34 could not be, because their URLs are not in AQ (§7).
- C-AQ13 was re-read through the fetch tool (curl 403 here too). Its quotes match.

---

## §3 Arithmetic re-done

All **[our calc]** in check AQ reproduce. Rows marked "new" are calculations added here, on the same or newly read sources.

| Item | Check AQ | Recomputed | Result |
|---|---|---|---|
| C-AQ03: ATO base steps | 21 min | 7 + 2 + 7 + 5 = 21 | ✓ |
| New: ATO per purchase invoice with expected exception time | — | 21 + 0.10×20 + 0.24×15 + 0.48×5 + 0.036×5 = **29.2 min** | Implies about AUD 34 an hour against 60% of AUD 27.67, so the minutes and costs plausibly come from one model (§4.1) |
| D2 / C-AQ15 | 10.8; 11.9; 9.7-10.8 at 1,880 h | 0.24 × 124,800 = 29,952; ÷ 2,784 = 10.76; ÷ 2,518 = 11.90; at 1,880 h 9.72 and 10.75 | ✓ |
| D2, **new**: 11,111 invoices per FTE (another APQC average quoted by Stampli, search summary) | — | 29,952 ÷ (11,111 × 0.232) = 11.62 | Inside AQ's range |
| D2, **new**: denominator includes 2018's 12% contested payments | — | 29,952 ÷ (12,000 × 0.352) = **7.09**; ÷ (10,853 × 0.352) = **7.84** | Lower bound of the restricted reading |
| D2, **new**: 2025 pair (21.9% supplier time; 18.4% exceptions) | — | 0.219 × 124,800 = 27,331; ÷ 2,208 = **12.38**; ÷ 1,997 = **13.69** | Upper bound of the restricted reading |
| D3 / C-AQ16: OB10 | 88.5 | 9,600,000 ÷ 108,500 = 88.48 | ✓. The 31% is of PO-backed invoices only; if not all 350,000 are PO-backed, minutes per exception are higher (§4.3) |
| D4: Ardent cost as minutes | 15.3; 16.0; 18.9 | 15.33; 16.05; 18.87 | ✓ |
| D5: JOC cost as minutes | 29.9; 31.8; 17.5; 10.2 | 29.88; 31.79; 17.52; 10.21 | ✓ |
| C-AQ24: CTSI $15 | 24.5 | 24.46 | ✓ |
| D6: ocean calls | 60-150 | 6 × 10 = 60; 10 × 15 = 150 | ✓ (meaning narrowed, §1 #6) |
| C-AQ09: Ardent MTM split | 19.4% vs 14% | 0.2 × 9.0 + 0.8 × 22.0 = 19.4; cost 10.86 vs 9.40; days 14.54 vs 9.2; "59% lower" = 1 − 9/22 = 59.1% ✓ | ✓. A 14% average would need best-in-class to be 61.5% of firms |
| New: Ardent 2018 split | — | 0.2 × 10.7 + 0.8 × 22.9 = **20.46** vs a stated average of 23.2%; "114% lower" matches no ratio (22.9 ÷ 10.7 = 2.14×) | The same pattern as 2025 |
| New: SoE 2025, vendor-attributed split 11.1 / 20.9 | — | 0.2 × 11.1 + 0.8 × 20.9 = 18.94 vs 18.4; 1 − 11.1/20.9 = 46.9% ("47% lower" ✓) | Roughly consistent |
| C-AQ41: $2M customer workload | 313-368 bills a month; table cells | 2,000 × 1.88 = 3,760 and × 2.21 = 4,420 a year → 313.3 and 368.3 a month. 58%: 181.7-213.6 flags, 18.2-21.4 / 30.3-35.6 / 45.4-53.4 h. 18.4%: 57.7-67.8, 5.8-6.8 / 9.6-11.3 / 14.4-16.9 h. 14%: 43.9-51.6, 4.4-5.2 / 7.3-8.6 / 11.0-12.9 h. Disputes 15.7-18.4; 5.2-6.1 h at 20 min, 15.7-18.4 h at 60 min. Glance 7.8-9.2 h | ✓ every cell (meaning narrowed, §1 #14) |
| §AQ2.4 #2: Freightview 3% of an average LTL bill | ~$10 | 0.03 × $347.81 = $10.43 | ✓ |
| C-AQ58: G2 small business | 76% | 12 + 22 + 24 + 18 = 76 ✓; column total 107; other columns 100, 101, 99; normalised 76 ÷ 107 = **71.0%** | Narrowed (§1 #10) |
| C-AQ60: Vendr | ≈48 days | 41 × 1.17 = 47.97; 32 × 1.5 = 48.0 | ✓ |
| C-AQ82: Whistic | 23 × 3.5 | 80.5 hours a month (as the report says); "unlikely" 6% + "very unlikely" 1% = the 7% in C-AQ81 | ✓ |
| New: implied n behind JOC charts | "77" | Fig. 1: 72 (1/19/26/26); decision-maker: 43 (5/26/12); security: 41 (11/26/3/1); company size: 57 (12/3/22/20); role: 72 (10/16/41/5) | Smallest n ≤ 77 at which every percentage rounds exactly (script in scratchpad) |
| New: Gartner poll votes | — | Archive: 263 × 8% = 21 "none"; snippet: 288 × 5% = 14 | Votes cannot fall: DISCARD (§1 #2) |
| New: Pittsburgh programme | — | $434,000 ÷ 11,646 shipments = $37 each; parcel 11,532 ÷ 11,646 = 99.0% | Context for C-AQ78/79 |
| New: Ascent | 5 h a week | 200 × 1.5 ÷ 60 = 5.0 ✓; its blog's 50 h a week is 10× | B8 |

---

## §4 Concerns, unproven (verdicts unchanged)

1. **C-AQ01/02, ATO minutes.** The page ties its "average cost data" to Deloitte Access Economics' 2016 estimates. It does not say outright that the Table 3-4 minute defaults come from the same source. The implied wage (about AUD 34 an hour, §3) makes one model plausible, but this is not stated.
2. **C-AQ08/09, Ardent's "average".** Ardent never says whether its "average AP organization" is a mean or a median. If 14% were a median and 22.0% a mean of a skewed distribution, the figures would not strictly contradict each other. AQ's "internally inconsistent" holds for means only.
3. **C-AQ16, OB10.** The 31% is of "PO-backed invoices". Applying it to all 350,000 invoices may understate minutes per exception. The press release does not give the PO-backed share.
4. **C-AQ79, Pittsburgh's $10M cyber cover.** It sits in the RFP's standard contractor-insurance schedule (§2.3), beside general liability and workers' compensation. It is probably a university-wide template rather than a judgement about freight data. Not confirmed.
5. **C-AQ55, Transfix.** The dispute button covers carrier-added accessorials. Whether it covers linehaul rate errors, and whether the platform still brokers freight or now runs as software for shippers' own carriers, the page does not say.
6. **C-AQ58, G2's 107% column.** It may be a chart-rendering error or a multi-select question. G2 states that generative AI was used in the analysis. Cause unknown.
7. **C-AQ83.** The snippet could come from a different Gartner poll with similar wording. None was found, and the URL is the same.
8. **C-AQ19, JOC "cost to process an invoice".** Not defined in the report. It may include payment processing and bank fees, not only audit.
9. **C-AQ37, Intelligent Audit's 15-20 hours.** The quote (a G2 review reposted by the vendor) is about rating invoices by hand because the TMS "could not ingest the variable rates" of a consolidator's tariff. That is a full re-rating job, not reviewing flags.
10. **C-AQ25, Freightview Invoice Matching.** It is a paid add-on, enabled through support, "only visible to Full Access users", and "does not apply retroactively". Adoption may be low; the share of customers with a tolerance set is unknown.
11. **C-AQ66, Apex Analytix.** The same sentence that says "You do not budget" also says the audit requires "minimal internal effort". Under D-23 our customers' own staff work the flags, so that half of the contingency pitch does not transfer.

---

## §5 Full verdict table

**Source key** (the URLs behind the short names in the Evidence column):
- [ATO] https://web.archive.org/web/20260415171116id_/https://www.ato.gov.au/businesses-and-organisations/einvoicing/value-assessment-report/cost-calculations (live 403)
- [APQ1] https://web.archive.org/web/2025id_/https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/number-invoices-processed-fte-1
- [APQ2] https://web.archive.org/web/2025id_/https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/cycle-time-days-resolve-invoice-error
- [ARD] https://www.datocms-assets.com/80283/1744404602-ardent-partners-ap-metrics-that-matter-in-2025-pagero-final.pdf
- [SOE] https://payablesplace.ardentpartners.com/2026/01/state-of-epayables-part-nine-ap-benchmarks-and-best-in-class-performance/ (fetch tool; curl 403)
- [A18a] https://cporising.com/2018/06/22/payables-place-first-thing-exceptions-are-meant-for-learning-not-repeating/
- [A18b] https://cporising.com/2018/06/08/payables-place-first-thing-how-much-time-is-too-much-time-to-spend-with-your-suppliers/
- [A18c] https://cporising.com/2018/08/03/how-do-we-know-the-best-ap-departments-really-are-better/
- [FO] https://www.fleetowner.com/industry-perspectives/ideaxchange/article/21702872/use-these-kpis-to-evaluate-accounts-payable-performance
- [OB10] https://www.prnewswire.co.uk/news-releases/eliminating-invoice-exceptions-is-one-of-the-most-effective-ways-for-accounts-payable-to-cut-costs-192054921.html
- [ITT] https://imagetotable.ai/references/invoice-processing-time-benchmark ; https://imagetotable.ai/references/document-automation-exception-rates
- [NEX] https://www.nexusap.com/research/invoice-processing-time-benchmarks
- [STA] https://stampli.com/blog/accounts-payable/accounts-payable-benchmarking
- [JOC] https://www.joc.com/sites/default/files/u45421/Whitepapers/Freight-Payment-report-78441.pdf
- [AS16] https://www.freightwaves.com/?p=220008
- [FW17] https://www.freightwaves.com/news/special-coverage-ocean-freight-invoicing-errors
- [CT21] https://web.archive.org/web/2024id_/https://ctsi-global.com/2021/freight-auditing-how-many-shippers-outsource-and-why/ (live 403)
- [CT19] https://web.archive.org/web/2024id_/https://ctsi-global.com/2019/what-to-look-for-in-a-freight-audit-and-payment-provider/ (live 403)
- [FVM] https://blog.freightview.com/automated-invoice-matching/
- [FVP] https://www.freightview.com/pricing ; [FVH] https://www.freightview.com/ ; [FVT] https://www.freightview.com/terms
- [FP] https://www.freightpop.com/security
- [MC] https://mycarrier.io/ ; [MCT] https://trust.mycarrier.io/ ; [LT] https://trust.loop.com
- [CTLP] https://www.ctlogistics.com/freight-audit-services/freight-payment ; [CTLA] https://www.ctlogistics.com/freight-audit-services/post-audit
- [IT] https://www.intellitrans.com/resources/how-does-your-freight-invoice-audit-provider-measure-up
- [TRX] https://www.traxtech.com/blog/trax-audit-optimizer-real-time-exception-management
- [WH] https://lp.whistic.com/hubfs/Marketing%20Collateral/The%20State%20of%20Vendor%20Security%20Report%202022.pdf
- [G24] https://learn.g2.com/hubfs/2024-buyer-behavior-report.pdf ; [G25] https://learn.g2.com/hubfs/G2-2025-Buyer-Behavior-Report-AI-Always-Included.pdf
- [VQ1] https://www.vendr.com/insights/saas-trends-report-q1-2024 ; [VQ2] https://www.vendr.com/insights/saas-trends-report-q2-2024
- [SF] https://spendflo.com/blog/insights-from-the-state-of-saas-buying-survey-2024
- [APX] https://www.apexanalytix.com/resources/blog/recovery-audit-cost/
- [DOE] https://www.energy.gov/femp/energy-savings-performance-contracts-federal-agencies
- [IA1] https://www.intelligentaudit.com/blog/how-automated-freight-auditing-recovered-15-20-hours-weekly-for-one-retail-team ; [IA2] https://www.intelligentaudit.com/blog/40-hours-saved-weekly-inside-three-companies-logistics-audit-results
- [RXA] https://rxo.com/resources/research/freight-accessorials/ ; [RXT] https://rxo.com/terms-and-conditions/
- [WWX] https://www.wwex.com/shipping-resources/how-to-dispute-accessorial-fees
- [UBR] https://www.uberfreight.com/terms/
- [TQL] https://www.uchealth.com/wp-content/uploads/supplychain/customer%20packet.pdf
- [ARR] https://www.arrivelogistics.com/credit-application-terms-and-conditions
- [GSA] https://gsaig.gov/sites/default/files/audit-reports/A120060_1.pdf
- [PITT] https://www.purchasepaytravel.pitt.edu/sites/default/files/inbound_freight_management_services_rfp_041725ss_-_university_of_pittsburgh.pdf
- [SCW] https://web.archive.org/web/2024id_/https://www.scworld.com/news/more-than-half-of-organizations-suffer-from-alert-fatigue-study-says (live 403)
- [BD] https://www.brightdefense.com/resources/soc-2-type-ii/
- [GP] https://web.archive.org/web/20231001064013id_/https://www.gartner.com/peer-community/poll/how-vendor-security-reviews-influence-technology-purchases (live 403)
- [VAN] https://www.vanta.com/downloads/the-state-of-trust-top-security-compliance-trends-for-2025
- [ASC] https://ascentlogistics.com/wp-content/uploads/2021/10/Ascent_Freight_Audit_and_Pay_6.10.20.pdf ; [ASB] https://ascentlogistics.com/blog/how-freight-audit-and-pay-improves-workforce-management/
- [IL] https://web.archive.org/web/2025id_/https://www.inboundlogistics.com/articles/can-exception-management-be-automated (live 403)
- [TFX] https://support.transfix.io/en/articles/5968564-freight-audit-managing-invoices-in-your-shipper-app
- [CRF12] the Minneapolis Fed Remittance Coalition's copy of the "CRF 2012 Deduction Survey" deck (VCF Fall 2012), on minneapolisfed.org. The file name carries the presenter's surname, so it is withheld under the no-names rule; it is reachable from a search for that title.
- [SRCH] search-engine summaries (10 searches; listed in §6 and §7)

**Tests:** 1 existence, 2 meaning, 3 independence, 4 interest, 5 currency, 6 counter-search or counter-fetch, 7 arithmetic.

| Claim ID | Test(s) run | Verdict | New label | Evidence (source + quote ≤40 words) | Note |
|---|---|---|---|---|---|
| C-AQ01 | 1-7 | KEEP-verified | *verified* (Australian calculator default); *assumed* as a stand-in | [ATO] Table 4: "Processing exception: Exceptions in processing invoices requiring investigation by the finance department or reviewer … 24% 15 min" | Column headed "Generic time to correct"; minute origin §4.1 |
| C-AQ02 | 1-6 | KEEP-verified | as C-AQ01 | [ATO]: "Contested payment: Invoices requiring clarification with the supplier prior to payment. … 10% 20 min" | — |
| C-AQ03 | 1, 7 | KEEP-verified | *verified*; sum ✓ | [ATO] Table 3: "Receipt – 7 minutes Validation – 2 minutes Review – 7 minutes Approval – 5 minutes" | — |
| C-AQ04 | 1, 5 | KEEP-verified | *verified* | [ATO]: "While these DAE estimates date back to 2016, they closely align with the findings of the 2024 APEC report" | 40% AR / 60% AP split exact |
| C-AQ05 | 1-6 | KEEP-assumed | definition *verified*; 12,000 *assumed* | [APQ1]: "Total Sample Size: 3,596 All Companies Performers: 25th Median 75th - - -"; [SRCH] repeats median 12,000, sample 3,665 | Other APQC-attributed averages: 10,853 and 11,111 (Stampli) |
| C-AQ06 | 1, 2 | KEEP-assumed | *assumed* (snippet) | [APQ2]: "Cycle time in calendar days from discovering an invoice error to its resolution" | Elapsed days; [SRCH] repeats 4.0 / 2,861 |
| C-AQ07 | 1 | KEEP-assumed | *assumed* (snippet) | [SRCH]: visible figure 5.0 days, 461 companies | — |
| C-AQ08 | 1-6 | KEEP-verified | *verified* (Ardent's statement; AP holds, mostly large firms) | [ARD] p. 17: "Invoice exception rates have dropped dramatically to 14% in 2024." | The outlier among Ardent figures (B3) |
| C-AQ09 | 1-7 | KEEP-verified | *verified*; inconsistency [our calc] ✓ | [ARD] p. 25: "the 20% of enterprises with the lowest average invoice processing costs and the shortest average invoice cycle times" | Same pattern in 2018 (§3); §4.2 |
| C-AQ10 | 1, 7 | KEEP-verified | *verified* | [ARD] p. 18: "The average AP organization spends $9.40 to process a single invoice (the all-inclusive staff and operating costs" | — |
| C-AQ11 | 1, 2 | KEEP-verified | *verified* | [ARD] p. 15: "Automation Levels Within AP Fully Automated Somewhat Automated … Exception management 5% 60%" | Legend confirmed |
| C-AQ12 | 1 | KEEP-verified | *verified* | [ARD] p. 22: "invoice exceptions (53%) sit as the top challenge in the AP industry." | — |
| C-AQ13 | 1-5 | KEEP-verified | *verified* (fetch tool) | [SOE]: "The invoice exception rate for AP departments is, on average, 18.4%." | n=204 per [NEX]; posted 2026-01-22 |
| C-AQ14 | 1-6 | **NARROW** | *assumed* (relay); meaning per Ardent's own text | [A18a]: "24% of the average AP staff's time is spent working directly with suppliers to fix invoice processing, and payment errors." | §1 #13 |
| C-AQ15 | 1-7 | **NARROW** | **[our calc]** on *assumed* inputs; 7-14 min supplier-facing time | [A18b]: "fully 12% of all payments are contested by suppliers." | §1 #1 |
| C-AQ16 | 1-4, 7 | KEEP-assumed | *assumed* (vendor) | [OB10]: "31% - or nearly one third - of PO-backed invoices require expensive manual rework before payment can be approved." | 88.48 ✓; §4.3 |
| C-AQ17 | 1-3, 6 | KEEP-assumed | *assumed*; **orphan** | [ITT]: "Each exception adds 15–45 minutes of human work (IOFM) on top of normal handling" | Counter-search found no IOFM origin |
| C-AQ18 | 1, 3 | KEEP-verified | *verified* (what the page says) | [NEX]: "Excludes exception handling. Estimate, not survey data — no transparent public source publishes per-invoice touch time." | ImageToTable relabels it (§2) |
| C-AQ19 | 1-7 | **NARROW** | *verified* (figure); ≤15 respondents under $1B | [JOC] p. 4: "Small/Medium Shippers $19.49"; p. 3: "roughly three-quarters of them belonging to organizations with $1 billion or more" | §1 #3 |
| C-AQ20 | 1, 7 | KEEP-verified | **[our calc]** ✓ (upper bounds; input narrowed) | (calculation; inputs C-AQ10, 13, 19) | Carries C-AQ19's n |
| C-AQ21 | — | not checked | unchanged | — | Rests on check AH; URL not in AQ; search did not find it |
| C-AQ22 | 1-6 | **NARROW** | *verified* (that reported); one NVO executive | [FW17]: "An NVO doesn't have a lot of time to vet the invoice … It's usually six to 10 phone calls in our experience to resolve that." | §1 #6 |
| C-AQ23 | 1, 2, 4 | KEEP-assumed | *assumed* (hypothetical) | [TRX]: "Companies processing tens of thousands of invoices monthly might face exception rates of 15-20%" | Now read at source; "might face" |
| C-AQ24 | 1, 4 | KEEP-assumed | *assumed* (vendor) | [CT21]: "costing as much as $15 per invoice. This explains why many shippers that choose to handle their own auditing ultimately only perform spot checks" | Spot checks are CTSI's own claim (B1) |
| C-AQ25 | 1-6 | KEEP-verified | *verified* (page says); an example setting | [FVM]: "Let's say you choose to set a 3% overage limit for your LTL invoices and a $50 overage limit for your Truckload (TL) invoices." | Corroborated by UltraShip [IL]; §4.10 |
| C-AQ26 | 1 | KEEP-verified | *verified* | [FVM]: "it will remain in the Outstanding queue in Audit, waiting for your review." | — |
| C-AQ27 | 1-5 | KEEP-verified | *verified* (journalist's summary); ocean 2017 | [FW17]: "Many shippers use a percentage or dollar threshold under which they won't dispute inaccurate bills." | A reporter's line, not a panelist's count |
| C-AQ28 | 1-5 | KEEP-verified | *verified* (that reported); ocean | [FW17]: "We have customers who found complaints they just abandoned because they didn't have the resources to tackle it." | Speaker runs an ocean audit firm (interest) |
| C-AQ29 | 1 | KEEP-verified | *verified* (that reported) | [FW17]: "The two invoice auditors are required to determine if an invoice needs to be disputed within 48 hours of receipt." | — |
| C-AQ30 | 1 | KEEP-verified | *verified* (that reported) | [FW17]: "Guitar Center's rate of invoice discrepancy is around 3 to 4 percent" | Same passage: pre-change, AP paid unreviewed (§6) |
| C-AQ31 | 1-4 | KEEP-assumed | *assumed* (vendor relay) | [CT21]: "Shockingly, 30% of shippers had no system in place at all to audit and pay freight bills." | Gartner report not opened |
| C-AQ32 | 1, 2, 7 | KEEP-verified | *verified*; implied n = 72 | [JOC] Fig. 1: "Payment Only 1.4% Audit Only 26.4% Both 36.1% Neither 36.1%" | — |
| C-AQ33 | 1 | KEEP-assumed | *assumed* | [OB10]: "only 43% of participants have formal tracking methods." | — |
| C-AQ34 | 2, 6 | **NARROW** | 2021 figure not re-read; meaning narrowed | [CRF12]: "Do you automatically write off chargebacks below a certain value without investigation 17% 19% 65% Yes Depends on type No" | §1 #7 |
| C-AQ35 | 1, 2 | KEEP-verified | *verified* | [GSA] p. 3: "The response rate was a mere 6 percent and only 13 prepayment audit programs were submitted." | — |
| C-AQ36 | 1-4, 7 | KEEP-assumed | *assumed* (vendor) | [ASC]: "On average, shippers receive 200 carrier bills per week." "With a streamlined process, it takes, on average, 1 minute and 30 seconds to audit each freight bill." | Same vendor: 50 h a week (B8) |
| C-AQ37 | 1-4 | KEEP-assumed | *assumed* (a G2 review reposted by the vendor) | [IA1]: "This left us having to manually rate the invoices, which was adding 15-20 hrs of research each week." | §4.9 |
| C-AQ38 | 1 | KEEP-assumed | *assumed* | [IA2]: "Their Bill Payment and GL Reporting services have saved us 40+ labor hours per week" | Payment, not audit |
| C-AQ39 | 1, 4 | KEEP-assumed | *assumed* (no sample shown) | [RXA]: "61% of shippers agree that managing accessorial requests is one of the biggest time-wasters for their accounting team." | — |
| C-AQ40 | 1 | not checked | unchanged | German page script-rendered; Alberta posting HTTP 410 | §7 |
| C-AQ41 | 2, 7 | **NARROW** | **[our calc]** ✓; Ardent rows are sensitivity only | [ARD] p. 17: "Invoices flagged due to coding errors, missing information, approval bottlenecks, lack of purchase order data, etc." | §1 #14 |
| C-AQ42 | 1 | KEEP-verified | *verified* (that reported); security analogue | [SCW]: "54 percent indicated that they have no choice but to ignore some alerts that may require an investigation due to their limited staff." | Upgraded (B7) |
| C-AQ44 | 1-6 | **NARROW** | *verified*; payment ownership, shippers + 3PLs | [AS16]: "based on a benchmark survey of 208 freight payers (shippers and 3PLs)" | §1 #8 |
| C-AQ45 | 1, 2 | KEEP-verified | *verified* (2016; "smaller" = under $1B) | [AS16]: "smaller shippers are three times as likely to have to pay within 30 days and five times more likely to have to pay within 15 days." | — |
| C-AQ46 | 1, 2, 7 | **NARROW** | *verified*; n = 43 | [JOC]: "Decision-maker on freight audit and payment technology … Finance … Combination of logistics and finance … Logistics … 11.6% 60.5% 27.9%" | §1 #9 |
| C-AQ47 | 1 | KEEP-verified | *verified* (that reported); ocean | [FW17]: "their accounts payable (AP) departments don't have an innate understanding of those same ocean contracts." | — |
| C-AQ48 | 1 | KEEP-verified | *verified* (page says) | [WWX]: "you will need to provide documentation that the request was not on the bill of lading (BOL) or delivery receipt." | — |
| C-AQ49 | 1, 6 | KEEP-verified | *verified* (absence: "invoice" 0 hits) | [RXT]: "If there is a conflict between the terms of the Agreement and these Terms, the Agreement will control." | "dispute" only in the venue clause |
| C-AQ50 | 1 | KEEP-verified | *verified* | [UBR]: "Prior to initiating an arbitration, you and Uber Freight each agree to notify the other party in writing of any dispute" | "invoice" 0 hits |
| C-AQ51 | 1, 2, 5 | **NARROW** | *verified* for the 2015 form | [TQL]: "exclusive venue with respect to any claim, counterclaim, dispute or lawsuit arising in connection with any transactions, loads" | §1 #15 |
| C-AQ52 | 1, 6 | KEEP-verified | ***verified*** (upgraded from snippet) | [ARR]: "In the absence of such express terms and conditions, all invoices or amounts owed are due and payable thirty (30) days from the date of invoice." | "dispute" 0 hits; "may cancel credit at any time without notice" exact |
| C-AQ53 | 1 | not checked | unchanged | sitecore host timed out; Wayback 404 | §7 |
| C-AQ54 | 1 | not checked | unchanged | Page loads; content script-rendered | §7 |
| C-AQ55 | 1-6 | **NARROW** | absence *verified* for the 11 named firms only | [TFX]: "If you click on Dispute you'll have the opportunity to Edit or Remove an accessorial that was added on by the carrier" | §1 #4 |
| C-AQ56 | 1-5 | KEEP-verified | *verified* (G2 sells to vendors) | [G24] p. 11: "49% of buyers took 4 months or more to make a purchase decision on a $20,000+ piece of software, rising from 41% last year." | n = 1,940, March 2024 ✓ |
| C-AQ57 | 1 | KEEP-verified | *verified*; 41/42 mismatch confirmed | [G24] p. 16: "42% of buyers identified a C-suite or the CFO / highest-ranking financial officer as the person ultimately responsible for making a purchase decision." | p. 11 says 41% |
| C-AQ58 | 1-7 | **NARROW** | *verified*; 71-76% | [G25] heat map, 1-250 column: "12% … 22% … 24% … 18% … 13% … 7% … 8% … 1% … 2%" | §1 #10 |
| C-AQ59 | 1, 2 | KEEP-verified | *verified* (for generative and agentic AI tools) | [G25]: "Bundled with core product 28% … Usage-based 28% … Add-on subscription fee 25% … Outcome-based 10% … One-time implementation fee 8%" | — |
| C-AQ60 | 1, 7 | KEEP-assumed | *assumed* (Vendr's transactions) | [VQ2]: "Net new purchases took 50% longer this quarter than they did a year ago, when the buying cycle was 32 days." | [VQ1] 41 days × 1.17 ✓ |
| C-AQ61 | 1 | KEEP-assumed | *assumed* (press release via search) | [SRCH]: "Most successful buyers (57%) take 3 months or less to evaluate their software options, while most regretful buyers (54%) take 5 months or more." | All buyers, not split by size |
| C-AQ62 | — | not checked | unchanged | No URL in AQ | — |
| C-AQ63 | 1 | KEEP-assumed | *assumed* | [SF]: "Buying is decentralized: Department heads are the main decision-makers—approving the majority of SaaS purchases." | — |
| C-AQ64 | 1-6 | **NARROW** | *verified* for the 0-50 shipments tier | [FVP]: "0-50 ships per month $149 / mo 51-500 ships per month Call now" | §1 #5 |
| C-AQ65 | 1 | KEEP-verified | *verified* (page says) | [IA1] navigation: "Built for smaller shipping volumes, Catalyst is quick and easy to get started. Try free for 90 days." | — |
| C-AQ66 | 1, 4 | KEEP-verified | page *verified*; claim *assumed* | [APX]: "while requiring minimal internal effort. In short: You do not budget for an AP recovery audit. It funds itself" | §4.11 |
| C-AQ67 | 1 | KEEP-verified | *verified* (page says) | [CTLA]: "Always a Refund from our "No Cure - No Cost" Post Auditing Plan" | — |
| C-AQ68 | 1 | KEEP-verified | *verified*; analogue | [DOE]: "allow federal agencies to procure energy savings and facility improvements with no up-front capital costs or special appropriations from Congress." | — |
| C-AQ69 | 1-6 | **NARROW** | *verified* (page says); mid-market/enterprise tool | [FP]: "FreightPOP is an AI supply chain software platform built for mid-market and enterprise shippers." | §1 #11 |
| C-AQ70 | 1-4 | KEEP-verified | trust page *verified*; customers *assumed* | [MCT]: "controls continuously monitored and validated through our Vanta-powered Trust Center." [MC]: "MONTHLY CUSTOMERS 7k+" | MyCarrier is "built specifically for LTL shippers" |
| C-AQ71 | 1 | KEEP-verified | *verified* (page source) | [LT]: og:title "Loop Trust Center"; og:image on app.vanta.com | Contents not readable |
| C-AQ72 | 1, 6 | KEEP-verified | absence *verified* on 3 pages | [FVH][FVP][FVT]: 0 hits for SOC or ISO | Terms mention "security" only as the user's password duty |
| C-AQ73 | 1, 2 | KEEP-verified | *verified* | [FVT]: "true, accurate, complete, current, not confidential, and not in violation of any contractual restrictions or other third party rights." | Data-use clause ("improving machine learning") also exact |
| C-AQ74 | 1 | KEEP-verified | *verified* | [FVT]: "YOU grant FREIGHTVIEW a limited power of attorney, and appoint FREIGHTVIEW as YOUR attorney-in-fact and agent, to access Transportation Providers' websites" | — |
| C-AQ75 | 1 | KEEP-verified | *verified* (page says) | [CTLP]: "We are also SOC II compliant for financial security of your funds." | Report type not stated |
| C-AQ76 | 1, 4 | KEEP-verified | *verified* (page says); demand *assumed* | [IT]: "SOC 1&2 compliance should be table stakes when it comes to demonstrating your commitment to freight invoice audit processing integrity" | Seller's advice |
| C-AQ77 | 1 | KEEP-verified | *verified* (Wayback) | [CT19]: "they will ideally follow the auditing standard outlined in the Statement on Standards for Attestation Engagement no. 16 (SSAE 16)." | — |
| C-AQ78 | 1-6 | **NARROW** | *verified*; trigger broader than data type | [PITT] §1.13: "data moving between the University and Contractor systems, system integrations, Contractor access to the University networks, and/or the University data being shared with the Contractor" | §1 #12 |
| C-AQ79 | 1, 2 | KEEP-verified | *verified* | [PITT] p. 11 of 18: "E. CYBER LIABILITY $10,000,000" | §4.4 |
| C-AQ80 | 1, 2, 7 | **NARROW** | *verified*; n = 41 | [JOC] p. 5: "most shippers responding to the survey said they were at least somewhat confident in their provider's system security. But only a quarter were very confident" | §1 #9 |
| C-AQ81 | 1-4 | KEEP-verified | *verified* (that reported); not our segment | [WH] p. 3: "only seven percent of respondents said they would require no additional security documentation." | Respondents "worked primarily for mid-sized enterprises" (mean 1,332 employees) |
| C-AQ82 | 1, 7 | KEEP-verified | *verified* (that reported) | [WH] p. 4: "it typically takes 4.8 days to receive completed assessments back from vendors." | — |
| C-AQ83 | 1, 6, 7 | **DISCARD** | numbers replaced (Oct 2023 archive) | [GP]: "None, we don't perform vendor security reviews 8 % … box-checking exercises 38 % … delay purchases but they don't change outcomes 28 % … 263 PARTICIPANTS" | §1 #2 |
| C-AQ84 | 1 | KEEP-assumed | *assumed*; not on the cited page | [VAN]: no "65%" or sample size on the page fetched | Stays unused, as AQ says |
| C-AQ85 | 1, 3, 4 | KEEP-assumed | *assumed*; **orphan** | [BD]: "85% of enterprise buyers require SOC 2 reports before signing contracts" (no source given) | "enterprise" qualifier (§2); uzado page 404 |

---

## §6 Counter-evidence and leads

These are logged, not new findings. Each is tied to the claim it bears on.

| # | Source | What it says (quote ≤40 words) | Ties to | Type |
|---|---|---|---|---|
| 1 | [A18a] Ardent's 2018 post (CPO Rising mirror) | "Nearly a quarter of AP's time is spent handling exceptions such as disputed payments, missing invoice data, incorrect posting information, and matching failures." | C-AQ14, 15 (the 24% includes payment disputes) | Counter-evidence (meaning) |
| 2 | [A18c] Ardent 2018 best-in-class post | "Invoice exception rates are 114% lower (10.7% vs. 22.9%) for Best-In-Class" | C-AQ09 (the pattern recurs) | Corroboration of AQ's flag |
| 3 | [CRF12] CRF 2012 deduction survey, 493 companies | "Do you automatically write off chargebacks below a certain value without investigation 17% 19% 65%"; median "< $25.00" all industries | C-AQ34 | Counter-evidence (meaning) |
| 4 | [IL] UltraShipTMS Q&A in *Inbound Logistics* (Wayback) | "a shipper can opt to allow the automatic approval/payment of invoices up to say, $50 above the approved rate." Tolerances "can be assigned by carrier, by lane and by line item." | C-AQ25 (a second TMS vendor) | Corroboration (vendor) |
| 5 | [TFX] Transfix Help Center, 2026-07-10 | "The Freight Audit function lets you easily communicate with your carriers to accept invoices via the Transfix Shipper App and dispute them when necessary." | C-AQ55 | Counter-evidence |
| 6 | [FVP] Freightview pricing | "Can I pay for a whole year at once? Sure! Talk to your Freightview consultant" | C-AQ64, §AQ4.4 | Counter-evidence (the buying route at our size) |
| 7 | [FP] FreightPOP | "Built for the security standards enterprise shippers require" | C-AQ69 | Counter-evidence (positioning) |
| 8 | [PITT] RFP, current invoicing process | "the Payment Processing team performs an open payable import process, receives the Excel and PDF invoice copies via a shared mailbox, and completes a spot audit and invoice validation prior to payment." | AQ2 behaviour (a public buyer spot-audits) | Lead |
| 9 | [FW17] the retailer's logistics director (2017) | "No one from the logistics process was looking at it. It was going to AP and they were paying it." | A09-15 (without an owner, bills are paid as billed) | Lead |
| 10 | [ASB] Ascent blog, 2020-04-14 | "On average, we save clients 50 hours per week." | C-AQ36 | Counter-evidence (same vendor) |
| 11 | [ITT] and [SRCH] (search summaries, not fetched beyond ImageToTable) | ImageToTable: "45–60 min per exception under traditional automation (APQC 2025, via Peakflo)". Search summaries add a fintech blog's "45 to 60 minutes" and Peakflo's AR guide (simple 10-20 minutes, medium 30-60, complex 2-4 hours). | AQ1 minutes (vendor figures above 10-15) | Counter-evidence (vendor, unverified) |
| 12 | [TQL] TQL credit packet (2015) | "To process payment, may we exclude bills of lading from your invoice? (Check one) YES NO" | AQ3 / design: broker invoices may arrive without the BOL a flag needs | Lead |
| 13 | [WH] Whistic 2022 | "The respondents worked primarily for mid-sized enterprises, with an average company size of 1,332 employees." | C-AQ81 | Context (size) |
| 14 | [NEX] Nexus AP | "Touch time — the minutes a person actually spends — is not published by any transparent survey" | AQ1 | Corroboration of AQ's "not answerable" |
| 15 | [STA] and [SRCH] | Stampli: APQC average "10,853 invoices in a year"; a second Stampli page (search summary) gives 11,111 | C-AQ05, D2 | Lead (range of APQC-attributed values) |
| 16 | [JOC] p. 4 | "If we assume an average invoice of $2,500 across modes, that's roughly 40,000 invoices over the course of the year." | C-AQ19 (JOC's population is large, multimodal) | Context |
| 17 | [SRCH] U.S. Bank / project44 release (Business Wire, 2019; 403 to curl) | Getting the paperwork to resolve audit exceptions "could take as long as 72 hours" of emailing or calling carriers (search summary) | AQ2 (elapsed time per exception) | Lead (*assumed*) |
| 18 | [SRCH] two follow-through counter-searches | No survey splits LTL or truckload discrepancies into disputed, not disputed and written off. No study reports the share of audit exceptions a shipper resolves. | A09-15 | Absence confirmed (not proof) |

---

## §7 Could not access

- **Gartner Peer Community** (403 to curl and the fetch tool). The Wayback copy of 2023-10-01 was used. The Wayback CDX index was "Temporarily Offline", so later captures could not be listed.
- **APQC** measure pages (403). The Wayback copies show dashes for values; values come from search summaries only.
- **Ardent's 2026 State of ePayables post** (403 to curl; Wayback 404). Read through the fetch tool's extraction.
- **CTSI-Global** (403). Read on Wayback copies.
- **Capterra** (403). Only press-release lines via search.
- **C.H. Robinson** dispute page (sitecore host timed out; Wayback 404): C-AQ53 not checked.
- **J.B. Hunt** blog: loads, but the content is script-rendered: C-AQ54 not checked.
- **Job postings** (C-AQ40): the German page is script-rendered; the Alberta posting returns HTTP 410 Gone.
- **MyCarrier and Loop** trust centers: scripted Vanta pages; report lists not readable.
- **Vanta** State of Trust download page: loads, but carries no "65%" figure.
- **uzado.com** SOC 2 blog: HTTP 404.
- **Inbound Logistics** (403): read on Wayback.
- **Business Wire** (U.S. Bank / project44): 403.
- **CRF 2021 and 2023 deduction surveys** and every source behind C-AQ21 and C-AQ34: URLs not in AQ, and check AH could not be read under this review's rules. One search found only the 2012 deck.
- **SEC EDGAR** (by rule): not needed.
- **Not searched (budget):** Hackett and Levvel originals; the Gartner 2018 freight audit-and-pay research behind C-AQ31; NASSTRAC or SMC3 member surveys on who files claims; the third-party risk profile behind "Freightview SOC 2: Not verified"; the Panaseer report behind the SOC 2 percentages; RateLinx's "$3 to $5 variance" remark seen only in a search summary.
