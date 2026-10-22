# S5 check BD: a real dispute walked through the method, then compared with what happened

Written 2026-10-20, with a founder, from `handoff_dispute_walkthrough.md`. The method under test is `data/doc-exploration.md` (§1-§4, §9.7) and the seven-stage pipeline in `data/doc-explanation.md` §4. Nothing in `data/` was edited. Changes are proposed in §8, and the founders decide what is applied.

Privacy: the source pages carry individuals' names, e-mail addresses and phone numbers. None is copied here; companies and roles only.

Page numbers are PDF pages of `data/sources/23_overcharge_claims_vs_yellow/yrc_globaltranz_16200__claim.pdf` (catalogue 23-002) unless another file is named.

**Case 2** (the ODFL chain in set 21) was not run in this session. On the founder's choice it goes to another agent, run blind from a kit outside the project: `~/Documents/personal/bio/freight_case2_blind/`, whose `HANDOFF.md` is copied at `handoff_case2_blind.md`. That agent appends its write-up here as §11 onward.

## 0. The result in five lines

1. **The method reached the real outcome's question, not its answer, and that was correct.** It found a trigger dispute worth $60.00 on Yellow PRO 7047922705, named the deciding fact (what GlobalTranz's EDI pickup request said) and who holds it, and gave **ask the reviewer**, with the carrier's records requested ("A attached with B", the founder, §5.3). Yellow's own agent later found "the mistake was made by Yellow's terminal and the TONU was invalid" (p. 4), which is the branch the card names for a request that said 3 units.
2. **The clock was met** on bounds alone: earliest deadline 2023-12-12; the dispute was filed between day 0 and day 146 (§4).
3. **The money was lost anyway, to two things the method does not model:** the invoice was paid before it was disputed, so the approval "was unable to make changes", and the refund then fell into the carrier's bankruptcy. The register lists the claim at $0.00 (§6-§7). The software's value on such a line is flagging it at receipt, before payment (BD-1).
4. **Main gaps, proposed as BD-1 to BD-11:**
   - payment state as the router between disputing an open invoice and claiming a refund;
   - an "approved, not credited" state;
   - the pickup request as a fact (F30);
   - the bucket policy for carrier-added trigger charges;
   - an LTL TONU and attempted pickup in P10, F22 and F28 (the method models TONU as truckload only);
   - a floor for an unknown receipt date;
   - a carrier in bankruptcy;
   - the PRO from dispute documents;
   - a 3PL as the customer;
   - "Units 0" on GlobalTranz's BOLs;
   - catalogue notes.
5. **Caveat:** the verdict was not truly blind. The outcome's gist was disclosed before the walk (§1.4), so the test is that every step of §2-§5 traces to an input with a page, which it does (§10).

## 1. The case and the documents

**Case 1: Yellow claim 16200**, a $60 TONU (truck ordered, not used: a fee for sending a truck that left without the freight) on Yellow PRO 7047922705 (PRO = the carrier's bill number).

### 1.1 What the file holds

| Pages | Document | What it gives the walk |
|---|---|---|
| 1-3 | Bankruptcy proof of claim (Official Form 410), *In re Yellow Corporation*, case 23-11069, claim 0000016200, filed 11/08/2023 15:15:57 | Creditor "Globaltranz" (p. 1); amount "60.00" (p. 2, item 7); signed by the creditor's "authorized agent" (p. 3) |
| 4 | The claimant's letter, headed "Overcharge Claim for PRO# 7047922705 – BOL# 27100405". **Undated** | The disputed line, the carrier's stated reason (as the claimant reports it), the claimant's evidence, and the outcome |
| 5 | The BOL (bill of lading, the shipper's pickup paper), "Straight Bill of Lading - Short Form", GTZ BOL NO 27100405, on a form headed with a relocation company's logo | The shipment facts |

**Not held:** Yellow's freight bill for PRO 7047922705; the EDI pickup request the 3PL sent to Yellow (EDI = the standard electronic message format; the letter says the BOL was "generated from our TMS immediately after the EDI request was sent"); any Yellow rules tariff; any delivery receipt or 214 status message; Yellow's answer to the online claim; any payment record. The text layer of pp. 4-5 was checked against the pages rendered at 150 dpi and matches.

### 1.2 Who is who

| Role | Company | Where |
|---|---|---|
| Carrier | YRC (Yellow) | p. 5 "Carrier: YRC"; p. 1 debtor "Yellow Corporation" |
| Payer and claimant: a 3PL (third-party logistics firm, which books freight for its clients and pays the carrier) | GlobalTranz, Scottsdale AZ | p. 5 "Third Party Billing Information: All charges prepaid to: GlobalTranz"; p. 1 creditor |
| Shipper (origin) | Executive Moving Systems, Woodbridge VA 22191 | p. 5 |
| Consignee (destination) | Stewart Moving, "2nd Warehouse", Jacksonville FL 32254 | p. 5 |

In C-09 terms the **customer** is the payer, GlobalTranz, and the reviewer is its staff (D-23). A 3PL as the customer is a case the method has not walked before: the five earlier LTL chains were seen from a shipper's or consignee's side.

### 1.3 The question (stage 1)

**What was billed:** a $60.00 TONU on PRO 7047922705 (p. 4: "I filed an OVC Claim online on Claim# 23026659 for PRO# 7047922705 in the amount of $60.00"; p. 2 item 7 "60.00"). The freight bill itself is not held, so the line is known only through the claimant.

**What is disputed, and why (p. 4, the input sentences only):** "This TONU was charged because YRC claimed the EDI Pickup Request was for 1 handling unit, which resulted in a truck being sent without enough space for the 3 units at the shipper. The EDI details clearly state 3 handling units at 11 linear feet per the attached BOL that was generated from our TMS immediately after the EDI request was sent." (A handling unit is a pallet, crate or skid the carrier moves as one piece; linear feet is how much trailer floor the freight takes up, end to end.)

**What kind of dispute:** a **trigger** difference, not a price difference (`data/doc-exploration.md` §0, last paragraph). Nobody says $60 is the wrong price for a TONU. The question is whether the charge applies at all. That depends on one fact: did the carrier send a truck too small because the pickup request was wrong (the shipper side's fault), or because Yellow's terminal misread a correct request (the carrier's fault)?

**Checks (AK §3.2):**
- **D5, truck ordered not used.** It names the charge. AK lists its data needed as "Cancellation time; rate confirmation terms", "Auto? No". Both are truckload notions: an LTL TONU has no rate confirmation and no cancellation; the truck came and left.
- **D2, accessorial ordered or performed.** It fits the question better: was the extra charge caused by the party who pays it? AK: "Partly: often a question for the shipper".
- **G1** (the shipper's dispute windows) and **G2** (the carrier's response deadlines) for the clocks.
- **A7** (the bill carries the reference needed to pick the contract or quote) is in catalogue row 23-002's tags. **It does not fit:** nothing here turns on a quote or agreement reference. The BOL's references (the PU#, and a PO that pairs a surname with a number) are join keys, not pricing references.

### 1.4 The blindness caveat

The handoff asks for the verdict to be written before the outcome is read. That was not fully possible. The outcome's gist was disclosed before the walk began: in the hand-off summary the founder pasted, in `handoff_dispute_walkthrough.md` §4, and in catalogue row 23-002's notes ("dispute approved but invoice already paid"). And p. 4 mixes inputs and outcome in one paragraph. So the rule applied is narrower: **§2-§5 use only the input sentences quoted in §1.3, the claim's number and amount, and pp. 1-3 and 5.** The outcome sentences of p. 4 are quoted for the first time in §6. The reader should treat §5's verdict as written with knowledge of the outcome's gist, and judge it on whether each step is traceable to an input with a page.

## 2. The facts

Every fact the disputed line needs, picked from `doc-exploration.md` §1's Checks column (D2, D5, G1, G2, and the keys every check uses), each followed down its §2 row in order: primary, then fallbacks, then "never", then "if none". "Owed by" follows §4.1. Pages are 23-002's unless a file id is given. Facts that turned out to be n/a are listed under the table.

### 2.1 The fact table

**Phase 1, price terms**

| ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by |
|---|---|---|---|---|
| P01 | Whose pricing applies | Yellow's rules-tariff payor item (§2.1 lists SEFL, ODFL, XPO, Estes, Saia, ABF, AAA Cooper, FedEx, TForce; **no Yellow item, and none held**) → the agreement's scope clause (not held) → never the bill-to | **NOT REPORTED.** On the BOL's terms the payor is GlobalTranz (F04), so its own Yellow pricing would apply if Yellow follows the common payor rule (*assumed*) | Carrier (public) |
| P02 | The agreement and its versions | The agreement header (not held) → the bill's authority reference (no bill held) | **NOT REPORTED** | Customer (GlobalTranz's own agreement with Yellow) |
| P09 | Accessorial exception prices, and any waiver | The agreement's exceptions page (not held) → a contract schedule (not held) | **NOT REPORTED.** Context only, not this account's terms: Yellow's contract with Home Depot (23-005, p. 1127) prices "Truck Ordered Not Used": "prior to dispatch … WAIVED", "after dispatch - Per Trailer $ 200.00", and makes the carrier "obtain approval via e-mail … before billing for TONU charges". So Yellow did agree TONU waivers and approval rules with some customers | Customer |
| P10 | The tariff item: price **and trigger wording** (what makes a TONU or attempted pickup apply at Yellow) | Yellow's rules tariff, edition in force on 06/15/2023 (not held; `data/sources/13_rules_tariffs/` has no Yellow file) → an archived copy (none held; not tried, since the session is offline) → a later edition (none) → **never** a different carrier's item | **NOT REPORTED.** The "never" list matters: AAA Cooper 190-AF "Charge Per Attempted Pickup … $75.00" (13, `aaa_cooper_190-AF.txt` l. 2312) and Central Transport and Dayton Item 985 "Vehicle furnished but not used … (dry run)" are not Yellow's | Carrier, on request (49 U.S.C. 13710(a)(1)) |
| P15 | TL accessorial terms, TONU included | Truckload only: the rate confirmation → master agreement → carrier tariff | **n/a by its own definition** ("must (TL)"). This is an LTL move. **The method has no price-term row for an LTL TONU or attempted pickup**: P10 is the nearest, and its examples are all delivery-side triggers | — |
| P16 | The shipper's claim-window rule | Statute 13710(a)(3)(B) plus the carrier's item; §2.1 names the "YRC form" | **Found:** YRC form F-154 (16-095, p. 1): "Overcharge claims must be filed within 180 days of pickup … We will acknowledge claims within 30 days of receipt." The form is edition "F-154 10/13" (p. 1), so applying it to 2023 is *assumed*. Plus the statute's 180 days from receipt of the bill | Public |
| P17 | The carrier's re-bill window | Statute 13710(a)(3)(A) | Found (statute). **Relevance unknown**: whether the TONU came on the original bill or on a later one is NOT REPORTED (M03) | Public |

**Phase 2, shipment facts**

| ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by |
|---|---|---|---|---|
| F01 | BOL number, PO, shipper reference | BOL header (primary) | **Found, p. 5:** "GTZ BOL NO : 27100405"; PO (a surname and "253772"); "Shipper Ref #: PU# BGAC0624775"; "Customer BOL NO:" blank. The letter's heading repeats "BOL# 27100405" (p. 4) | Shipper side |
| F02 | Ship or pickup date | BOL header (primary) | **Found, p. 5:** "Shipment Date: 06/15/2023". Caveat: on a TONU this is the *planned* pickup date. The date the truck came and left, and whether and when the crates moved later, are NOT REPORTED | Shipper side (planned date); carrier (attempt date) |
| F03 | Shipper and consignee | BOL ship-from and ship-to (primary) | **Found, p. 5:** Executive Moving Systems, Woodbridge VA 22191 → Stewart Moving, "2nd Warehouse", Jacksonville FL 32254. Shipper's pickup remark "Open 8am - 3pm"; consignee hours 9:00 AM to 4:00 PM | Shipper side |
| F04 | Freight terms and third-party bill-to | BOL terms boxes (primary) | **Found, p. 5:** "Third Party Billing Information : All charges prepaid to : GlobalTranz, PO Box 6348, Scottsdale AZ 85261" | Shipper side |
| F05 | Pieces and handling units | BOL carrier-information table (primary; sum the lines, check the total) | **Found, p. 5:** line 1 "Crates, Units 0, Pieces 2"; line 2 "Crates, Units 0, Pieces 1"; "Total: 0, 3". Lines sum to the totals. **The BOL states 0 handling units and 3 pieces**, not "3 handling units" as the letter says (§2.2) | Shipper side (its BOL) |
| F06 | Declared weight | BOL weight column with its header (primary) | **Found, p. 5:** 1,912 lb + 869 lb; "Total 2781 lbs". **Derived:** 1,912 + 869 = 2,781, which matches | Shipper side |
| F07 | Declared class and NMFC | BOL columns (primary) | **Found, p. 5:** class 150, NMFC 100240-1, "Household Goods/Personal Effects, RVNX .10 cents pound" (a released-value declaration: carrier liability limited to $0.10 a pound) | Shipper side |
| F08 | Declared dimensions | BOL description or cube (primary) | **Found, p. 5:** line 1 "87 In × 45 In × 87 In" (two crates); line 2 "45 In × 87 In × 87 In" (one crate). **Derived** (the letter's "11 linear feet"): the two 87 × 45 in crates side by side across the trailer (45 + 45 = 90 in wide, which fits a standard trailer width, *assumed*) take 87 in of floor; the third crate takes 45 in; 87 + 45 = 132 in = **11.0 ft**. So the letter's figure is reproducible from the BOL. Also derived: 3 × 87 × 45 × 87 in³ = 591.33 ft³, so 2,781 ÷ 591.33 = 4.70 lb/ft³ | Shipper side |
| F09 | Services requested | BOL tick boxes and special instructions (primary) → the bill's echo (no bill held) → 204 notes (not held) → never the DR | **Found, p. 5:** "Comments/Special Instructions:" blank. "Pickup Remarks: PU# BGAC0624775 \| Open 8am - 3pm." No liftgate, no equipment size, no appointment. The BOL asks for nothing that bears on truck size | Shipper side |
| F15 | Services performed | DR boxes (primary) → driver notes → the carrier's remark on the bill | **NOT REPORTED.** No DR or bill held. For a pickup that failed, the record would be the driver's or dispatcher's attempt record, which no §2 row names (§2.2) | Carrier |
| F22 | Cancellation time (the TONU part of this row) | The carrier's or broker's notice record → the invoice line's face value | **NOT REPORTED.** The row is built for truckload: "a broker's TONU confirmation held prints no cancellation time (set 22)", and its "if none" names "Customer, broker". For an LTL attempted pickup the record is the **carrier's** dispatch and driver record, so the row's "if none" points at the wrong party | Carrier (the row says customer or broker) |
| F23 | The customer's own record of the shipment | The customer's TMS, ERP or booking record (primary; not public) → a 204 tender → the customer's rate confirmation → the quote | **Partly found.** The BOL is a print from that record: "the attached BOL that was generated from our TMS immediately after the EDI request was sent" (p. 4). The TMS record itself and the EDI request it sent are NOT REPORTED | Customer's files (GlobalTranz) |
| F25 | Who requested the service, how and when | The BOL's request (F09) → the consignee's signed request on the DR → the carrier's record of a phoned or portal request → the bill's remark → the 214 | **Partly found, p. 4 (input sentence):** the pickup was requested by **EDI**, by the claimant, before the BOL was printed ("immediately after the EDI request was sent"). The request's content and timestamp are NOT REPORTED | Customer's files (the request it sent); carrier (what it received) |
| F28 | The recorded cause of a failed attempt | DR exception notes and the carrier's printed reason → a 214 reason code (none held) → a DR time stamp → the customer's dock record → never a 214 "NS" as proof of no fault | **Found only second-hand, p. 4:** "YRC claimed the EDI Pickup Request was for 1 handling unit, which resulted in a truck being sent without enough space for the 3 units at the shipper." The carrier's own words are not in the file, just as with the limited-access decline in §5.5 (G2) | Carrier |

**Phase 3, the money asked**

| ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by |
|---|---|---|---|---|
| M01 | PRO | 210 B3-02 → PDF bill header → the BOL's affixed PRO label → DR → 214 → statement row | **Not in any place the row lists.** The BOL's "Carrier PRO #:" is **blank** (p. 5). Found only in the dispute documents: "PRO# 7047922705" (p. 4, heading and body). The row says "Always present", which is true of a bill but not of a dispute packet without one | Carrier |
| M02 | Carrier | 210 → PDF letterhead | No bill held. **Found elsewhere:** "Carrier: YRC" (p. 5); debtor "Yellow Corporation" (p. 1); "YRC" and "Yellow's terminal" (p. 4) | — |
| M03 | Bill type, and whether the TONU had its own bill | PDF title plus a changed amount → 210 B3-08 → statement | **NOT REPORTED** | Carrier |
| M04 | Bill date; first bill date | First 210 → PDF bill date → "previously invoiced" → statement; else "unknown, no later than …" | **NOT REPORTED.** No bill, statement or reprint held, so not even a "no later than" bound exists from the money side | Carrier |
| M06 | Terms as billed, bill-to | 210 B3-04 + N1*BT → PDF terms box | **NOT REPORTED.** The BOL (F04) names GlobalTranz as payer, and GlobalTranz filed the claim | Carrier |
| M14 | The accessorial line | PDF (name, code) → 210 L1-08 (code TONU is seen in real 210s) | **Found only second-hand:** "TONU" "in the amount of $60.00" (p. 4); "60.00" (p. 2, item 7) | Carrier (its bill) |
| M16, M17 | Total; previously billed, paid, balance | 210 B3-07 / PDF total; XPO / SEFL balance lines → statement → A/R history | **NOT REPORTED** in the input documents. The payment state appears only in an outcome sentence, so it is not used before §6 | Carrier (bill); customer (its AP) |
| M18 | The carrier's reason | PDF remarks → 210 K1 or L5 | **NOT REPORTED from the carrier.** It exists only as the claimant reports it (F28) | Carrier |
| M19, M20 | The bill's echo of the BOL; printed references | PDF | **NOT REPORTED** (no bill) | Carrier |
| M27 | The intermediary's invoice for the same shipment | The intermediary's invoice to the shipper → the broker's statement | **NOT REPORTED.** Here the customer *is* the intermediary. The fact turns round: did GlobalTranz pass the $60 on to its own client? If it did, its dispute also recovers its client's money; if not, the $60 is its own loss. The row is written from a shipper's side only | Customer's files |

**Phase 4, the dispute**

| ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by |
|---|---|---|---|---|
| D01 | Window start dates and the earliest deadline | Derived from P16/P17 + D09 (else M04) + F02 | Derived in §4 | — |
| D02 | The claim's content | The claim letter (primary) | **Found, p. 4:** PRO, BOL, the carrier's claim number, $60.00, the nature of the error, the proof relied on (the BOL). **No date, no tariff authority.** This letter was written for the bankruptcy court. The online claim it refers to is NOT REPORTED | Customer |
| D03 | Proof attached | The claim's attachments | **Found, p. 5:** the BOL only. The EDI pickup request, the stated proof ("The EDI details clearly state …"), is **not attached** | Customer |
| D04 | Filing and acknowledgement dates | The claim letter's date → the carrier's acknowledgement → e-mail or portal records | **Online claim: date NOT REPORTED** (the letter is undated). Court proof of claim: filed "11/08/2023 15:15:57" (p. 1). Acknowledgement: NOT REPORTED | Customer; carrier |
| D05, D06 | The carrier's decision, reason, date; credit or refund | The carrier's answer → a re-bill or A/R history | **Held only in outcome sentences on p. 4**; quarantined until §6 | Carrier |
| D07 | The payer's payment record | The payer's AP export → A/R history → the 3PL's claim form | **NOT REPORTED in the input documents** (the payment state is in an outcome sentence; quarantined until §6) | Customer's files |
| D08 | Dispute log | The customer's worksheet | **NOT REPORTED** | Customer's files |
| D09 | The date the payer received the bill | 210 interchange date → e-mail or portal timestamp → received stamp → payment firm's date → the bill date as a bound | **NOT REPORTED**, and so is its bound (M04) | Customer's files |
| D10 | The carrier's claim number | The carrier's acknowledgement or status page → the form's carrier-number box → the claimant's statement of it | **Found, p. 4:** "Claim# 23026659" (eight digits, like Yellow's 23009972 and 23023786 in §5.5). The claimant's own number: NOT REPORTED. (16200 is the court register's number, not Yellow's) | Carrier |

**Checked and set aside as n/a:** P03-P08, P11-P14, P18-P22 (price lines and correction fees: the dispute is about whether the charge applies, not its price); F10-F14, F16-F21, F24, F26, F27, F29 (delivery, reweigh, guarantee and TL facts; no contract requiring approval is held, so F24 cannot be tested); M05, M07-M13, M15, M21-M26.

### 2.2 How the documents tie together, and where they disagree

**Keys (§2.5).** The PRO 7047922705 appears only in the letter (p. 4). The BOL's PRO field is blank (p. 5). So the letter joins the BOL on the **second** key, the BOL number 27100405, printed on both. The PU# BGAC0624775 (p. 5) is a third reference, probably the carrier's or 3PL's pickup confirmation number (*assumed*). It is the key that would open the missing EDI pickup request, and §2.5 lists no pickup-request key.

**Disagreements (§3.1).**

| Fact | Copy 1 | Copy 2 | Copy 3 | What §3.1 says | Our reading |
|---|---|---|---|---|---|
| Handling units the pickup request declared | BOL, printed from the same TMS record right after the request: "Units 0", "Pieces 3" (p. 5) | The claimant: "The EDI details clearly state 3 handling units at 11 linear feet" (p. 4) | Yellow, as the claimant reports it: "the EDI Pickup Request was for 1 handling unit" (p. 4) | The pieces row ranks "the carrier's count on the bill and DR". **That row decides how many pieces moved, not what a pickup request said.** No row covers this fact | **Not decidable from the held documents.** All three sides agree there were 3 crates at the shipper (Yellow's reported reason itself says "the 3 units at the shipper"), so the true count is not in dispute. The dispute is what the request said, and the only document that records it (the EDI message) is not held. The one sibling we hold, the BOL, prints **0** handling units, which supports neither the claimant's "3" nor Yellow's "1" as written. *[our reading, not a finding]* A blank or zero handling-unit field that a carrier's system defaults to 1 would produce exactly Yellow's reported reading. Whether that happened is for the EDI log to show |
| Linear feet | Not printed on the BOL | "11 linear feet" (p. 4) | — | — | Reproducible from the BOL's dimensions: 87 + 45 = 132 in = 11.0 ft (F08, derived). This supports the claimant's statement of the shipment's size, not of what the EDI said |
| Payer | BOL: third party, GlobalTranz (p. 5) | The claimant is GlobalTranz (p. 1) | — | The BOL as corrected by written authority | No conflict |

## 3. Price terms, expected against billed, and the trigger test

### 3.1 Stage 3: the price terms in force on the ship date

Following `doc-explanation.md` §4.4:

| Step | What the method asks | What this case gives |
|---|---|---|
| 1 Payor | The BOL's terms and payor pick the agreement | Third party, prepaid to GlobalTranz (p. 5). So GlobalTranz's own Yellow pricing applies, if Yellow follows the usual payor rule (*assumed*; Yellow's payor item is not held, P01) |
| 2 Agreement version | The latest version effective on or before 06/15/2023 | **NOT REPORTED** (P02). GlobalTranz holds it. It is the place a TONU waiver or price exception would sit (P09). Yellow did write such terms for other accounts: Home Depot's contract waives TONU "prior to dispatch", prices it at "$ 200.00" per trailer "after dispatch", and bars billing one without e-mailed approval (23-005, p. 1127; context only) |
| 3 Rules | The carrier's tariff item in the edition in force on the ship date | **NOT REPORTED** (P10). Yellow's rules tariff is "YRC Tariff 100" (named in a GlobalTranz appeal, 23-003 p. 5, "YRC Tariff 100-754"). No edition of it is in `data/`. **Who must supply it:** Yellow, on request: a motor carrier "shall provide to the shipper, on request of the shipper, a written or electronic copy of the rate, classification, rules, and practices, upon which any rate applicable to its shipment … is based" (49 U.S.C. 13710(a)(1), quoted in `doc-exploration.md` §2.1 P10). The proof of claim (p. 1) shows Yellow in bankruptcy (case 23-11069), so the practical route may be the estate rather than the carrier's pricing desk *[our reading]* |
| 4 Fuel, 5 Base rate | — | Not relevant: a TONU is a flat charge with no fuel or rate |

**What the tariff item would settle, and why it matters here.** Three tariffs in `data/` show three different trigger wordings for a truck sent and not used. None of them is Yellow's, so under P10's "never" rule none prices or triggers this line. They show only what the missing item could say:

| Carrier and item | Applies when (quoted) | Price | What it would make the deciding fact |
|---|---|---|---|
| AAA Cooper 190-AF, effective December 22, 2025 (13-066, l. 2309-2312) | "When a shipper requests that CARRIER provide pickup service, and through no fault of CARRIER the pickup cannot be accomplished" | "$75.00" per attempted pickup | **Fault.** Who caused the failure? |
| Central Transport 100-CC Item 985(2), effective August 17, 2026 | "When Carrier is requested to make a pickup of LTL shipment and arrived within the scheduled window for pickup and **no freight is given** to Carrier" | "$75.00" | **A fact, not fault.** Was freight handed over? Here three crates were waiting and the truck could not take them, so whether that counts as "no freight given" is itself unclear |
| Dayton (DAFG) 19-K Item 985(1)(a), effective 2026-06-01 | A vehicle requested "to pick-up a TL, Volume or Exclusive Use shipment" and "not used due to no fault of the carrier" | "$130.00 per day" | Truckload, volume or exclusive use only. Under this wording, an ordinary LTL pickup would carry **no** such charge |

So the trigger wording is a must-have (P10 says so: "price + trigger"), and in this case it is the missing half of the test. Under a fault wording the dispute is about the pickup request. Under a "no freight given" wording it may not be about fault at all.

**What the method can still check without the tariff:** that the line exists and its amount ($60.00, second-hand); who the payer is; the dates; and the trigger fact itself (§3.3). It cannot check the price or which trigger wording governs.

### 3.2 Stage 4: expected against billed

| | Value | Source |
|---|---|---|
| Billed | **$60.00**, "TONU" | p. 4 ("in the amount of $60.00"); p. 2 item 7 ("60.00"). Second-hand: the bill is not held |
| Expected price | **Not checkable.** Missing inputs: Yellow's tariff item in force on 06/15/2023 (P10, the carrier's), and GlobalTranz's agreement with any TONU exception (P02/P09, the customer's). Context, not a check: $60.00 is the amount on 12 of the 14 "Dispute relating to TONU" rows, and on the one "attempted pickup charge" row, in TQL's ledger against Yellow (23-010, pp. 13-15); the other two TONU rows are $195.00 | — |
| Expected if the trigger fails | **$0.00.** Billed − expected = $60.00 − $0.00 = **$60.00 owed back to the payer** | Derived |
| Expected if the trigger holds | **$60.00 as billed** (the price unverified), so the difference is $0.00 | Derived |

**Tolerance rule (founders, 2026-10-20: "any difference, so long as there is money that the carrier needs to pay").** If the trigger fails, the carrier owes $60.00 and the line qualifies, whatever the size. The amount is not a reason to drop it. Whether $60 is worth a reviewer's minutes is a product question, not a method one (see §8).

### 3.3 Stage 5: the trigger test

**The fact that makes the charge apply.** On a fault wording (the AAA Cooper type), the TONU stands only if the pickup failed through no fault of the carrier. Both sides agree on what happened physically. Yellow's reported reason itself says the truck was "sent without enough space for the 3 units at the shipper" (p. 4). So the fault turns on **one fact: what the EDI pickup request told Yellow about the freight's size.** The method has no row for that fact (§2.1; proposed in §8).

**Who owed it (§4.1).** The size of the freight is a shipper-owed fact of the same family as F05 pieces and F08 dimensions. Here the party that wrote the request is the payer itself: GlobalTranz sent the EDI request (F25, p. 4). How Yellow *read* the request, and what its driver found, are carrier-owed (F22, F28; §4.3).

**The test, by what the request actually said:**

| If GlobalTranz's EDI log shows … | Then (method section) | The line |
|---|---|---|
| **3 handling units and 11 linear feet**, or any size a truck for 1 unit could not hold | Yellow misread a complete request. The failure is the carrier's, so a fault-worded TONU does not apply (P10 trigger fails) | **Flag:** $60.00 owed back. Proof: the EDI message itself, plus the BOL's 3 crates and dimensions |
| **0 or blank handling units** (what the BOL, printed from the same TMS record, shows: "Units 0", p. 5) | The shipper side left the size out. §4.2: "the shipper's NOT REPORTED is not grounds for a dispute … the rule gives the carrier the right to fill the blank". Defaulting to 1 is Yellow's way of filling it | **No dispute** on the fault test. A residual question is left for the reviewer: did the request carry 3 pieces and 11 linear feet elsewhere, which a careful carrier should have read? That turns on the EDI fields and Yellow's tariff wording, both unseen |
| **1 handling unit** | The shipper side's error | **Matches:** the charge stands |

**What the held documents say about which row is true.** The claimant asserts the first row ("The EDI details clearly state 3 handling units at 11 linear feet", p. 4). The proof it attached does not show it. The attached BOL prints "Units 0" (p. 5). Its 11 linear feet is reproducible from the BOL's dimensions (§2.1 F08), but the BOL never states it. *[Our reading, not a finding]:* the BOL's zero sits closer to the second row than to the first. Only the EDI message can settle it, and it is in GlobalTranz's own files.

**What §4.2 and §4.3 say, and where they stop.**
- §4.2, shipper-owed and missing: it applies if the request left the size out. Then the omission is not a dispute.
- §4.3, carrier-owed and missing: Yellow's own record of the request it received, and of the driver's attempt, is NOT REPORTED. The carrier's reason exists only as the claimant quotes it (F28). On a reweigh, §4.6 puts this in the bucket "unsupported change, carrier's record requested". Here, though, the carrier's reason *is* stated (second-hand), and the record that settles it is one the customer already holds. Whether the bucket applies is left to stage 7 (§5).
- §4.6, the decision table: its nearest row is the first ("F06/F07/F09 … and the carrier billed on its own reading", owed by the shipper). It says: "Trigger in question, decided on the carrier's record … or the reviewer; the omission itself is not the dispute". That fits the shape, with "the pickup request" in place of the BOL. **No row names the pickup request**, and none covers a fact that sits in the *payer's* own outbound message rather than on the BOL.

**Stage 5 result: trigger in question.** The deciding fact is NOT REPORTED in the held documents. Its primary home is the customer's own EDI log; its secondary home is Yellow's record of the request it received. The trigger wording that would say whether fault even matters (P10) is Yellow's, and is not held.

## 4. The clocks

Following `doc-exploration.md` §4.4-§4.5 and `doc-explanation.md` §4.7. All date arithmetic is in `python3 -I`.

### 4.1 The start dates

| Start date | Fact | Value |
|---|---|---|
| Receipt of the bill | D09 | **NOT REPORTED** (customer's files) |
| Bill date, the fallback | M04 | **NOT REPORTED** (no bill, statement or reprint held) |
| Pickup | F02 | **Planned 06/15/2023** (a Thursday; p. 5). The date the truck actually came is NOT REPORTED and is taken as 06/15/2023 (*assumed*). Whether the crates moved later, and when, is NOT REPORTED |

**What the method does with this.** With both D09 and M04 missing, D01's "if none" gives **"unknown"** (§2.4 D01; §4.5 item 5). The method stops there. **A better bound exists and the method does not use it** *[our call]*: a TONU bill cannot be dated before the attempt it charges for. So receipt was no earlier than 06/15/2023, and every 180-day deadline that runs from receipt is **no earlier than 2023-12-12**. This floor comes from the ship date (F02), not from any bill. Proposed in §8.

### 4.2 Every window that applies

| Window | Source | Start | Deadline (derived) | Note |
|---|---|---|---|---|
| Yellow's own rule: "Overcharge claims must be filed within 180 days of pickup" | YRC F-154, edition 10/13 (16-095, p. 1); its use for 2023 is *assumed* | Pickup, 06/15/2023 (*assumed*, §4.1) | 06/15/2023 + 180 days = **2023-12-12**; with the founders' 10-day buffer, 2023-12-22 | "Pickup" is ambiguous on a TONU: the failed attempt, or the later pickup? The earlier date is used, so the deadline is the earliest possible |
| The statute: 180 days from receipt of the bill | 49 U.S.C. 13710(a)(3)(B) (§4.4) | Receipt (D09): NOT REPORTED | **No earlier than 2023-12-12** (floor from §4.1) | The method alone would say "unknown" |
| NMFC 300520-A(a): "All billing disputes must be filed within 180 days from the receipt of the original invoice. Receipt of original invoice shall be determined to be 5 business days from the invoice date." | `nmfc_100-AO_supplement1_2015` (15-081) l. 1232-1233. The 2015 edition, and Yellow's participation in it, are *assumed* (the back of Yellow's F-154 reprints the NMFC claim rules under older item numbers, 300203-300204) | Invoice date + 5 business days. The invoice date is NOT REPORTED; floor 06/15/2023 | Floor: 06/15/2023 + 5 business days = 06/22/2023 (weekends skipped, holidays not); + 180 days = **no earlier than 2023-12-19** | — |
| GlobalTranz's agreement with Yellow | P02 | — | **NOT REPORTED** (customer) | A contract can shorten or lengthen the window |
| The carrier's re-bill window | 13710(a)(3)(A) (P17) | — | Not applicable unless the TONU came on a later bill; M03 NOT REPORTED | — |

**Earliest deadline: 2023-12-12** (Yellow's own form, on the assumed pickup date). With the 10-day buffer, a filing up to 2023-12-22 would still have been shown, as "late: file now, may be refused".

### 4.3 Was the dispute inside them?

| Filing | Date | Days after 06/15/2023 | Verdict on the clock |
|---|---|---|---|
| The online claim with Yellow, "Claim# 23026659" (p. 4) | **NOT REPORTED** (the letter is undated). Bounded: after the TONU was billed, so no earlier than 06/15/2023; and no later than 11/08/2023, when the court filing cites it | 0 to 146 | **Inside every window**, whatever the true dates, because the latest it could have been filed (day 146) is inside the earliest deadline (day 180) |
| The proof of claim in Yellow's bankruptcy | 11/08/2023 15:15:57 (p. 1) | **146** (34 days to spare against 2023-12-12) | Inside |

So **the clock is not what decides this case.** The method reaches that only by an argument it does not yet make: bounding an unknown filing date between two known events. Its rules handle an unknown *start* date, but not an unknown *filing* date.

### 4.4 The carrier's clocks after filing (G2)

- **Yellow's own promise:** "We will acknowledge claims within 30 days of receipt" (F-154, p. 1).
- **Part 378:** acknowledge within 30 days; pay, decline or settle within 60 (§4.4).

Neither can be checked here: the online claim's filing date (D04) is NOT REPORTED, and so is any acknowledgement. The carrier's decision belongs to the outcome (§6).

### 4.5 A clock the method does not list

The proof of claim (p. 1) shows the carrier in bankruptcy (*In re Yellow Corporation*, case 23-11069, District of Delaware). TQL's addendum in the same case calls it "the Debtor's chapter 11 case" (23-010, p. 4). A carrier's bankruptcy adds two things the method's §4.4 has no row for:
- **a claims bar date:** the court's last day to file a proof of claim;
- **a change of channel:** from the carrier's claims desk to the court's claims register.

The bar date for case 23-11069 is **not in `data/`**, so it was not computed (the session is offline; fetching it needs the founder's go-ahead). Proposed in §8 as a row, not as a date.

## 5. The verdict, as the customer's reviewer would see it

Written and shown to the founder **before** the outcome sentences of p. 4 were used (with the caveat of §1.4).

### 5.1 The verdict the method gives

**Ask the reviewer: trigger in question.** By stage:

| Stage | Result |
|---|---|
| 1 Bill facts | No bill held. The line ($60.00 TONU, PRO 7047922705) is known only from the claim (p. 2, p. 4) |
| 2 Shipment facts | 3 crates, 2,781 lb, 11.0 linear ft (derived); the BOL prints "Units 0" and requests nothing about truck size (p. 5) |
| 3 Price terms | Yellow's TONU item and GlobalTranz's agreement: NOT REPORTED |
| 4-5 Expected against billed | Price **not checkable**. Expected is $0.00 if the trigger fails, so $60.00 would be owed back |
| 6 Trigger | **In question.** It turns on what the EDI pickup request said, which sits in the customer's own files (§3.3) |
| 7 Clock | Inside every window. The earliest deadline is **2023-12-12** (§4) |

The rule that gives it is `doc-explanation.md` §4.7: "**Ask the reviewer:** the trigger is in question." It is not a plain **flag**, because §4.7 requires that "the proof is in hand or is a document the carrier must produce". Here the proof is neither: it is a document the customer itself holds, and the one sibling document held (the BOL) points the other way.

### 5.2 The reviewer's card

> **Yellow PRO 7047922705 · TONU $60.00 · BOL 27100405 · PU# BGAC0624775**
> Planned pickup 06/15/2023, Woodbridge VA → Jacksonville FL; 3 crates, 2,781 lb, class 150; billed to you as third party.
>
> **Why it is here.** Yellow charged for a truck that left without the freight. Its stated reason, as recorded in your dispute, is that your EDI pickup request was for 1 handling unit. If your request said 3 units, the fault was Yellow's and the charge does not apply.
>
> **One question for you.** What handling-unit count did your EDI pickup request send? Note: the BOL your TMS printed from the same record reads **"Units 0"**, with "Pieces 3". It does not state 11 linear feet, although the dimensions give 11.0 ft (87 + 45 in).
> - **3 units, or a size a 1-unit truck could not hold:** dispute it. At stake: **$60.00.** Proof: the EDI message with its timestamp, plus the BOL.
> - **0 or blank:** no dispute. The size was left out, which the carrier may fill (`doc-exploration.md` §4.2). Consider fixing the handling-unit field in your TMS.
> - **1:** the charge stands.
>
> **Deadline.** File by **2023-12-12** (Yellow's form F-154: 180 days of pickup). After that the line is shown as "late: file now, may be refused" until 2023-12-22.
>
> **What to request from Yellow with the claim:**
> - the TONU or attempted-pickup item of its rules tariff in force on 06/15/2023 (49 U.S.C. 13710(a)(1)): its wording decides whether fault matters at all (§3.1);
> - its record of the pickup request it received;
> - the driver's attempt record.
>
> **How to file depends on whether you have paid** (your payment record; not shown here):
> - **unpaid:** dispute the line before paying. In the same bankruptcy case, TQL held its TONU disputes with Yellow, 12 of 14 of them at $60, as defences against what Yellow said it was owed (23-010, pp. 4, 13-15);
> - **paid:** file an overcharge claim. Yellow's form has no TONU box, so tick "OTHER (SPECIFY)" (F-154, p. 1).
>
> As of 11/08/2023 the carrier is in bankruptcy (p. 1), so a claim may have to go to the court's claims register.

**What the method itself does not yet tell the reviewer** (all for §8): the pickup request as a fact and a document; short-pay against claim by payment state; the bankruptcy route. The card above writes them in from the walk, not from the method.

### 5.3 The bucket question, for the founders

The founders asked (2026-10-20, in this session) whether this line belongs in the bucket they created that day, "unsupported change, carrier's record requested". Three readings:

| Reading | What it shows the reviewer | For | Against |
|---|---|---|---|
| **A. Ask the reviewer** (the method as written, §4.7) | The card above | The trigger is in question, and the deciding fact sits in the customer's own files, so one lookup settles it. The held evidence (the BOL's "Units 0") cuts against the claim, so counting it as a flag before that lookup risks a false positive | It depends on the reviewer finding an EDI log from months back. If the log is gone, the line stalls |
| **B. Unsupported-change bucket** (decision 1 of 2026-10-20) | A flag, with "Yellow's record of the request and the driver's attempt requested" | The TONU is a charge the carrier added, and the carrier's record behind it is NOT REPORTED (§3.3) | The bucket was built for a changed bill that prints no reason (a reweigh with no certificate). Here a reason was given ("1 handling unit"), even if only second-hand. And it would count $60 as flagged in Test 1 while the customer's own BOL shows 0 units |
| **C. Not checkable** | "Price not checkable: Yellow's tariff item missing" | The tariff item (P10) is missing | It hides a live $60. The trigger can be tested from the customer's own record without the tariff |

**Recommendation [our call]: A, with B's carrier requests attached** (the card already lists them), and B as the fallback if the reviewer cannot find the request.

**The founder's answer (2026-10-20, in this session, verbatim):** "The Verdict is good, it would be A attached with B." So for this case the verdict is **ask the reviewer**, with the carrier's records requested alongside. Applying it to the method as a general rule is proposed in §8.

## 6. The real outcome

Read after §5 was shown to the founder. Quoted from p. 4, with the one individual's name replaced by a role.

### 6.1 What the letter says happened

| # | Quotation (p. 4) | What it tells us |
|---|---|---|
| 1 | "This dispute was approved on YRC Case# CAS-925152-VMJKFM, but the agent handling the case was unable to make changes because the invoice was already paid in full." | **Yellow approved the dispute** through a customer-service case, separate from the online claim. But approval could only *change an open invoice*, and this one was **already paid**, so the approval moved no money |
| 2 | "The agent handling our case determined that the mistake was made by Yellow's terminal and the TONU was invalid." | **Who decided:** a Yellow case agent. **On what basis:** the carrier's own terminal made the mistake, so the charge did not apply. **This is a fault reading of the trigger.** The record the agent looked at is not stated |
| 3 | "I was told by [a Yellow employee] with YRC that any outstanding Overcharge Claims needed to be filed against the bankruptcy." | **The next channel:** with the invoice paid and the carrier in bankruptcy, the refund route became the court's claims register |
| 4 | "I filed an OVC Claim online on Claim# 23026659 for PRO# 7047922705 in the amount of $60.00." (already used as an input, §1.3) | The refund route GlobalTranz had opened with Yellow (an "OVC", overcharge, claim), still outstanding when the letter was written |
| 5 | "Please evaluate our case and dispute information and keep me informed on the progress of our claim." | As of the court filing (11/08/2023, p. 1), **the $60.00 had not been refunded** |

### 6.2 Did money move?

**No.** The charge was found invalid by the carrier, but it had been paid, and the approval could not reverse a paid invoice. The $60.00 then became an unsecured claim in Yellow's bankruptcy (p. 2: item 7 "60.00"; items 9 and 12 tick "No" to secured and priority; item 8 gives the basis as "ADR Claim-Alternative Dispute Resolution"). Item 11, "Is this claim subject to a right of setoff?", is ticked **"No"**: GlobalTranz held nothing back that it could offset the $60 against. The court register lists claim 16200 at **$0.00** (catalogue 23-002; set 23 `source.md`), against the form's $60.00. This is the same register-against-form mismatch as GlobalTranz's two other claims (`doc-exploration.md` §9.4 item 9). Whether anything was ever paid on the claim is NOT REPORTED in `data/`.

**Dates.** The decision date, the online claim's filing date and any acknowledgement are not printed anywhere in the file. That is the same gap §5.5 found: "What a stand-alone answer never carries: the decision date, the decision reason …". Here a reason is reported, but only second-hand.

## 7. The comparison

**The blindness caveat applies throughout:** the outcome's gist was known before §5 was written (§1.4). What can fairly be tested is whether each step of the verdict traces to an input with a page. Every step in §2-§5 cites one.

| Decision point | What the method said | What happened | Agree? | If not, why |
|---|---|---|---|---|
| Is there a dispute? | Yes: a carrier-added charge whose trigger is contested, with $60.00 owed back if it fails (§3.2, §5.1) | Yes: Yellow "determined that … the TONU was invalid" | **Agree** | — |
| What kind of dispute? | A **trigger** dispute, not a price dispute (§1.3) | Decided on whether the charge applied, not on its amount | **Agree** | — |
| Which trigger wording governed? | Unknown: Yellow's tariff item not held. Fault and "no freight given" wordings would decide differently (§3.1) | Decided on **fault**: "the mistake was made by Yellow's terminal" | **Agree, and settles one unknown** | The fault reading is the one the method's branches assumed. Yellow's tariff wording is still unseen |
| Who owed the deciding fact? | The pickup request's content was the payer's to state; how Yellow read it was the carrier's (§3.3) | The carrier's reading was at fault | **Agree** | The structure held. The fault fell on the carrier's side of the split |
| Where did the deciding fact live? | First the customer's EDI log; then Yellow's record of the request it received (§3.3, §5.2) | The agent decided on records the letter does not name. The claimant attached only the BOL (p. 5), not its EDI log, so the agent most likely used **Yellow's own record of the request** (*assumed*) | **Partly** | The method ranked the customer's log first. In practice the carrier's own copy of the request may be the faster proof, because the carrier can check it without the payer producing anything. That supports the founder's "A attached with B" |
| Does the BOL's "Units 0" count against the payer? | Flagged as cutting against the claim, a reason not to count it as a flag before the lookup (§3.3, §5.3) | Did not stop the approval | **Disagree, mildly** | The BOL is not the pickup request. Its units column is a known parse trap (§5.5, F05: "a naive parse reads zero handling units"), and the request apparently carried what the BOL did not. The warning was prudent; it was not decisive |
| The verdict | **Ask the reviewer**, with B's carrier requests attached (founder, §5.3) | A valid dispute, approved by the carrier | **Agree, conditionally** | The method reached the right question and named the branch that matches the outcome ("3 units → dispute"). It could not choose the branch from the documents, and should not have: the proof was not in the file |
| The price | Not checkable (§3.2) | Never at issue | **Agree** | — |
| The clock | Inside every window. Earliest deadline 2023-12-12; filed between day 0 and day 146 (§4) | Approved; the letter reports no timeliness objection | **Agree** | — |
| The next action | **Not in the method.** The walk wrote it into the card: unpaid → dispute before paying; paid → overcharge claim (§5.2) | Exactly this split: the dispute case could change only an unpaid invoice; with the invoice paid, the money needed the OVC claim, then the bankruptcy | **Agree with the card; the method has no rule** | Payment state (D07) decided what could be done, and the method treats D07 only as a check input (A2, A3, F1), not as the router between the two channels |
| Did the payment state change the outcome? | Card only: "How to file depends on whether you have paid" (§5.2) | **Yes, decisively.** A correct, approved dispute recovered nothing because the bill was paid first. GlobalTranz's proof of claim answers "No" to a right of setoff (p. 2, item 11). TQL, which held its TONU disputes unpaid, claimed them "as defenses" with rights of "recoupment and/or setoff" (23-010, p. 4) | **Agree with the card** | — |
| The carrier's channels | D10: claim number "23026659" (§2.1) | Two references: the online claim (23026659) and a customer-service case (CAS-925152-VMJKFM) that approved it | **Agree** | D10 already names "its channel reference: case number, portal ID" |
| The carrier's bankruptcy | Not in the method; noted by the walk as a missing clock and channel (§4.5) | "any outstanding Overcharge Claims needed to be filed against the bankruptcy" | **Agree with the walk; the method has no row** | — |
| Money recovered | n/a: the method stops at the verdict; D06 records a credit only if one is printed | **$0.00 as of 11/08/2023.** Approved but not refunded; the register lists the claim at $0.00 | **Gap** | The method has no state between "carrier approved" and "money received". An approved, unrefunded line looks closed when it is not |
| Decision date and reason | D05 (decision, reason, date): the carrier's answer only | No date; reason reported second-hand | **Agree** (the gap §5.5 predicted) | — |

**In one sentence:** the method found the right dispute, the right kind, the right deciding fact and a safe clock. The money was lost to two things it does not model: **paying before disputing**, and **the gap between approval and refund**, made final by the carrier's bankruptcy.

## 8. Proposed changes

None is applied. Each names the place in the method it touches, the wording proposed *[our call]* and the evidence. The founders decide. They are ordered by what they would have changed in this case.

### BD-1. The payment state picks the channel: dispute the open invoice, or claim a refund

- **Touches:** `doc-explanation.md` §4.7 (a new paragraph after "The verdict per line"); `doc-exploration.md` §1.4 D07 (Need column) and §4.6 (a new row).
- **Proposed wording (§4.7):** "**The next action depends on the payment state (D07).** If the line is **unpaid**, dispute it with the carrier before the due date, through the carrier's invoice-dispute channel, so the carrier can correct the open invoice. Do not deduct it on your own: nine of ten LTL rules tariffs read bar offsets or withholding (`research/s5_check_AO_c09_carriers_and_access.md` §AO1.1). If the line is **paid**, file an overcharge claim for a refund. A dispute approved on a paid invoice does not by itself move money."
- **D07's Need:** "must to choose the channel (dispute an open invoice, or claim a refund); must for A3, F1 …". Today it reads "must for A3, F1 and to file where payment is a precondition (XPO)".
- **Evidence:**
  - "This dispute was approved … but the agent handling the case was unable to make changes because the invoice was already paid in full" (23-002 p. 4);
  - GlobalTranz's proof of claim: "No" to setoff (p. 2, item 11);
  - TQL held its Yellow TONU disputes unpaid "as defenses to equal amounts alleged to be due" (23-010 p. 4; rows pp. 13-15).
- **For the founders, outside the method:** the software's value on a line like this lies in **timing**. Flagged when the bill arrives, before AP pays it, the same verdict keeps the money. Flagged after payment, it needs a refund that a failing carrier may never send. This bears on how bills reach the software (EDI or e-mail intake at receipt, not a monthly AP export; `software-initial-pitch.md`) and on the look-back design (`research/selection_runs/run-01/5_interview_kit.md` §6.1), where every line is already paid.

### BD-2. "Approved" is not "credited"

- **Touches:** `doc-exploration.md` §1.4 D05-D06 and §4.6 (the last row, "D05 carrier's answer"); `doc-explanation.md` §4.7 (the carrier's clocks).
- **Proposed wording (§4.6, a new row):** "| D06 credit or refund, after a D05 approval | Carrier | **Approved, not credited**: open, not closed | 'Approved on [date or case no.]; no credit or refund seen' | Part 378.8: pay, decline or settle within 60 days of receipt; then follow up, and if the invoice was paid, file or re-file as a refund claim |"
- **Evidence:** approved but no money moved (23-002 p. 4, quotations 1 and 5); the court register lists the claim at $0.00 (catalogue 23-002); §5.5's claim N, also approved, has a draft "Draft Date 06/20/23" but no proof it cleared (`doc-exploration.md` §5.5 D06).

### BD-3. A pickup request is a fact and a document

- **Touches:** `doc-exploration.md` §1.2 and §2.2 (a new row F30), §2.5 (a key), §4.1 (owed by); `doc-explanation.md` §4.3 (a new row) and §4.6's trigger table (a new row).
- **Proposed §1.2 row:** "| F30 | The pickup request, as sent and as received: channel (EDI, portal, API, phone), timestamp, confirmation number, and what it declared (handling units, pieces, weight, dimensions or linear feet, equipment, liftgate, hours) | D2, D5 | trigger + key | must on a TONU, attempted-pickup or dry-run charge |"
- **Proposed §2.2 row:**

  | Primary | Fallback | Never | If none |
  |---|---|---|---|
  | The requester's own outbound message (its EDI log or TMS record) | The carrier's record of the request received (pickup confirmation, dispatch record); the BOL printed from the same TMS record, as a sibling | The BOL's handling-unit column as the request's content | Customer (as sent); carrier (as received) |

- **§2.5:** add "for a pickup, the pickup or confirmation number (a 'PU#' on the BOL)".
- **Evidence:**
  - the dispute turns on what the EDI request said (23-002 p. 4);
  - no held document records it; the BOL was "generated from our TMS immediately after the EDI request was sent" and prints "Units 0" (p. 5);
  - the carrier, which held its own copy, decided that its "terminal" made the mistake (p. 4);
  - no §1 row today names a pickup request (§2.1 above).

### BD-4. The "unsupported change" bucket and "ask the reviewer" on a carrier-added trigger charge

- **Touches:** `doc-exploration.md` §4.3 (the reason bullet), §4.6, §7 item 1; `doc-explanation.md` §4.7.
- **Proposed rule, from the founder's answer on this case ("it would be A attached with B", §5.3):** "A carrier-added charge whose trigger is contested, where the carrier has stated a reason and the deciding fact is in the customer's own files, is **ask the reviewer**, with the carrier's records requested in the same step. It goes to the 'unsupported change, carrier's record requested' bucket only when the carrier states no reason, or when the reviewer cannot find its own record. In Test 1 it counts as flagged once the reviewer confirms."
- **Why it needs a founders' decision:** it narrows decision 1 of 2026-10-20 for one class of lines, and it sets how such lines are counted in Test 1.
- **Evidence:** §3.3 and §5.3; the outcome (§7, rows "Where did the deciding fact live?" and "Does the BOL's 'Units 0' count against the payer?").

### BD-5. An LTL TONU or attempted pickup in the price-term and trigger rows

- **Touches:** `doc-exploration.md` §1.1 and §2.1 P10 (examples), P15 (a pointer), §2.2 F22 and F28; `doc-explanation.md` §4.6 (the trigger table).
- **Proposed P10 addition:** "LTL attempted-pickup and dry-run items word the trigger differently, so the edition in force is a must:
  - AAA Cooper 190-AF: 'through no fault of CARRIER the pickup cannot be accomplished', $75.00 per attempt;
  - Central Transport 100-CC Item 985(2): 'arrived within the scheduled window for pickup and no freight is given to Carrier', $75.00;
  - Dayton (DAFG) 19-K Item 985: truckload, volume or exclusive use only."
- **P15:** add "TL; for an LTL TONU or attempted pickup see P10 and F30".
- **F22:** split off the LTL case. Its "if none" currently reads "Customer, broker". For an LTL attempted pickup it should read "Carrier (its dispatch and driver record: arrival time, equipment sent, why not loaded)".
- **F28:** read "a delay, failed delivery or pickup attempt, or wait", and add D5 to its checks.
- **`doc-explanation.md` §4.6, a trigger-table row:** "| TONU or attempted pickup (LTL) | per carrier: no fault of the carrier (AAA Cooper 190-AF), or no freight given in the window (Central 985(2)) | what the pickup request declared against what was there; the carrier's attempt record | the requester's EDI log or TMS; the carrier's record of the request and its driver's record |"
- **Evidence:** 13-066 l. 2309-2312; Central `CentralTransport_ctii_rules.txt` l. 3070-3076; Dayton l. 4638-4645; AK D5 ("Cancellation time; rate confirmation terms", TL only); the outcome was decided on fault (23-002 p. 4).

### BD-6. A floor for an unknown receipt date, and a bound for an unknown filing date

- **Touches:** `doc-exploration.md` §2.4 D01 ("if none") and §4.5 item 5; `doc-explanation.md` §4.7 (the clock).
- **Proposed wording:** "When both D09 and M04 are NOT REPORTED, the bill cannot predate the shipment or attempt it charges for, so receipt is **no earlier than F02** and each 180-day deadline is shown as 'no earlier than F02 + 180'. When a filing's own date is NOT REPORTED, bound it between the earliest event it must follow and the earliest document that cites it. If the latest possible filing date is inside the earliest deadline, the clock is met."
- **Evidence:** §4.1-§4.3. Here the floor is 2023-12-12, and the online claim fell between day 0 and day 146.
- **Also P16:** Yellow's form is edition "F-154 10/13" (16-095 p. 1), and "180 days of pickup" is ambiguous on a TONU (the attempt, or the later pickup). Use the earlier.

### BD-7. A carrier in bankruptcy

- **Touches:** `doc-exploration.md` §4.4 (a new row); `doc-explanation.md` §4.7 (a note under "the carrier's clocks").
- **Proposed §4.4 row:** "| Claimant | File a proof of claim when the carrier is in bankruptcy | By the court's claims bar date; claims become unsecured unless secured or offset; the carrier's own claims desk may stop paying | the case's bar-date notice (for *In re Yellow*, 23-11069, not held in `data/`) |"
- **Evidence:** p. 1 (the case); p. 4 ("any outstanding Overcharge Claims needed to be filed against the bankruptcy"); 23-010 p. 4.
- **Open:** fetching the bar date needs the founders' go-ahead (the session is offline).

### BD-8. When there is no bill: the PRO and the line from dispute documents

- **Touches:** `doc-exploration.md` §2.3 M01 (and M14).
- **Proposed wording:** add to M01's fallback "the dispute documents (claim letter, claim form, a 3PL's or broker's dispute ledger)". Change "Always present" to "Always present on a bill; a BOL's PRO field may be blank (23-002 p. 5)". M14 the same, with the amount marked second-hand.
- **Evidence:** p. 5 "Carrier PRO #:" blank; p. 4 the PRO and the amount; §5.5 already used claim statements for PROs.

### BD-9. When the customer is the intermediary

- **Touches:** `doc-exploration.md` §2.3 M27 and §4.1.
- **Proposed wording:** "When the customer is itself a 3PL or broker, M27 is its own invoice to its client. Whether the disputed charge was passed on decides whose money a recovery returns, and whether the client must be credited."
- **Evidence:** the payer here is GlobalTranz, a third-party billing 3PL (p. 5), on a BOL headed with a relocation company's logo. The five earlier LTL chains were all seen from a shipper's or consignee's side.

### BD-10. "Units 0" on a 3PL's BOL

- **Touches:** `doc-exploration.md` §2.2 F05 ("never").
- **Proposed wording:** "Never: a 'Units 0' total on GlobalTranz's BOL form as zero handling units, or as what a pickup request declared: all three GlobalTranz BOLs held print it (23-002 p. 5 '0 / 3'; 23-003 p. 4 '0 / 1'; 23-004 p. 5 '0 / 2')."
- **Evidence:** as quoted. The outcome treats the 3 crates as 3 units (p. 4).

### BD-11. Catalogue and register notes (data, not method; not applied)

- **Catalogue row 23-002** tags "A7|D2|D5". A7 does not fit (§1.3). Proposed: "D2|D5|G1|G2".
- **`doc-exploration.md` §9.4 item 9 and §7 item 6** list the register-against-form mismatch for claims 16595 and 16215. Add claim 16200: the register lists $0.00 (catalogue 23-002; set 23 `source.md`), and the form prints "60.00" (p. 2).

## 9. What the case confirmed

1. **§0's definition of a trigger dispute** carried a charge the method had never met: a charge that applies only if a fact holds, tested against that fact.
2. **§2's ordered lookup ending at a named party** turned "missing" into a concrete request for each fact: the customer's EDI log, Yellow's tariff item and request record, the payer's payment record.
3. **The "never" rule for another carrier's item (P10) mattered.** Three carriers' wordings would have given three different answers (§3.1).
4. **§2.5's second key worked.** With no PRO on the BOL, the BOL number joined the letter to the BOL.
5. **§4.2 gave the right "no dispute" branch** for a request that left the size out.
6. **The tolerance rule (founders, 2026-10-20) applied cleanly.** $60.00 qualifies; size is not a reason to drop a line.
7. **D10's "channel reference"** exists in practice: a claim number (23026659) and a separate case number (CAS-925152-VMJKFM).
8. **§5.5's lesson held on a third Yellow claim.** The carrier's answer survives only as the claimant reports it, with no decision date and no tariff authority (Part 378.8 asks for "reasons … citing tariff authority").
9. **The register-against-form mismatch** (§9.4 item 9) repeats on this claim.
10. **The founders' clock rule** (the receipt date first, the bill date as fallback) could not run here, because neither date was in the file. BD-6 is the floor that made the clock decidable anyway.

## 10. Claim ledger

*Verified* means re-opened at the source in this session: the rendered page image (pp. 2, 4, 5 of 23-002 and p. 1 of 16-095 at 100-150 dpi) or the PDF's own text layer (the 23-002 form pages and the tariffs are text-layer PDFs, not OCR). *Derived* values were recomputed in `python3 -I`. *Assumed* is marked.

| # | Claim | Value | File, page | Tag |
|---|---|---|---|---|
| 1 | Claim number, filing time | "0000016200", "11/08/2023 15:15:57" | 23-002 p. 1 | verified (text layer) |
| 2 | Creditor | "Globaltranz" | 23-002 p. 1 | verified (text layer) |
| 3 | Debtor and case | "Yellow Corporation", "23-11069", District of Delaware | 23-002 p. 1 | verified (text layer) |
| 4 | Amount claimed | "60.00" | 23-002 p. 2, item 7 | verified (image) |
| 5 | Not secured, no setoff, not priority | Items 9, 11, 12 ticked "No" | 23-002 p. 2 | verified (image) |
| 6 | Basis | "ADR Claim-Alternative Dispute Resolution" | 23-002 p. 2, item 8 | verified (image) |
| 7 | Signer's capacity | "I am the creditor's attorney or authorized agent" | 23-002 p. 3 | verified (text layer) |
| 8 | Letter heading | "Overcharge Claim for PRO# 7047922705 – BOL# 27100405" | 23-002 p. 4 | verified (image) |
| 9 | Online claim, PRO, amount | "Claim# 23026659 … PRO# 7047922705 … $60.00" | 23-002 p. 4 | verified (image) |
| 10 | The carrier's reason, as reported | "YRC claimed the EDI Pickup Request was for 1 handling unit … without enough space for the 3 units at the shipper" | 23-002 p. 4 | verified (image) |
| 11 | The claimant's evidence | "3 handling units at 11 linear feet per the attached BOL that was generated from our TMS immediately after the EDI request was sent" | 23-002 p. 4 | verified (image) |
| 12 | Outcome: approved, invoice paid | "approved on YRC Case# CAS-925152-VMJKFM, but … unable to make changes because the invoice was already paid in full" | 23-002 p. 4 | verified (image) |
| 13 | Outcome: basis | "the mistake was made by Yellow's terminal and the TONU was invalid" | 23-002 p. 4 | verified (image) |
| 14 | Outcome: channel | "any outstanding Overcharge Claims needed to be filed against the bankruptcy" | 23-002 p. 4 | verified (image) |
| 15 | Letter date | none printed | 23-002 p. 4 | verified (image) |
| 16 | BOL number, shipment date, carrier | "GTZ BOL NO : 27100405", "Shipment Date: 06/15/2023", "Carrier: YRC" | 23-002 p. 5 | verified (image) |
| 17 | Carrier PRO on the BOL | "Carrier PRO #:" blank | 23-002 p. 5 | verified (image) |
| 18 | Shipper, consignee, hours | Executive Moving Systems, Woodbridge VA 22191; Stewart Moving, "2nd Warehouse", Jacksonville FL 32254; "Open 8am - 3pm"; 9:00 AM - 4:00 PM | 23-002 p. 5 | verified (image) |
| 19 | Third-party billing | "All charges prepaid to : GlobalTranz" | 23-002 p. 5 | verified (image) |
| 20 | Units, pieces | "0 / 2", "0 / 1", "Total: 0, 3" | 23-002 p. 5 | verified (image) |
| 21 | Weights | 1,912 lb; 869 lb; "2781 lbs" | 23-002 p. 5 | verified (image); sum derived, 1,912 + 869 = 2,781 |
| 22 | Class, NMFC, released value | 150; 100240-1; "RVNX .10 cents pound" | 23-002 p. 5 | verified (image) |
| 23 | Dimensions | 87 × 45 × 87 in (2 pieces); 45 × 87 × 87 in (1 piece) | 23-002 p. 5 | verified (image) |
| 24 | Linear feet | 87 + 45 = 132 in = 11.0 ft | from #23 | derived; the crate layout across a trailer about 90 in wide is *assumed* |
| 25 | Cube and density | 591.33 ft³; 4.70 lb/ft³ | from #21, #23 | derived |
| 26 | Special instructions | blank, apart from the pickup remarks | 23-002 p. 5 | verified (image) |
| 27 | Yellow's claim window | "Overcharge claims must be filed within 180 days of pickup … We will acknowledge claims within 30 days of receipt"; edition "F-154 10/13" | 16-095 p. 1 | verified (image); its use for 2023 *assumed* |
| 28 | NMFC billing-dispute window | 300520-A(a), quoted in §4.2 | 15-081 l. 1232-1233 | verified (text); the 2015 edition and Yellow's participation *assumed* |
| 29 | Deadlines | 06/15/2023 + 180 = 2023-12-12; + 10 = 2023-12-22; + 5 business days + 180 = 2023-12-19 | from #16, #27, #28 | derived |
| 30 | Days to the court filing | 2023-11-08 − 2023-06-15 = 146; 180 − 146 = 34 | from #1, #16 | derived |
| 31 | Attempt date = planned date | 06/15/2023 | — | *assumed* |
| 32 | Home Depot-Yellow TONU terms | "prior to dispatch … WAIVED"; "after dispatch - Per Trailer $ 200.00"; approval by e-mail before billing | 23-005 p. 1127 (text l. 86635-86640) | verified (text layer); context only |
| 33 | TQL's TONU disputes with Yellow | 14 "Dispute relating to TONU" rows (12 at $60.00, 2 at $195.00) and 1 "attempted pickup charge" at $60.00 | 23-010 pp. 13-15 | verified (text layer; counted in `python3 -I`); context only |
| 34 | TQL's disputes held as defences | "claimed as defenses to equal amounts alleged to be due to the Debtor by TQL … recoupment and/or setoff"; "the Debtor's chapter 11 case" | 23-010 p. 4 | verified (text layer) |
| 35 | AAA Cooper attempted pickup | "through no fault of CARRIER the pickup cannot be accomplished … $75.00"; effective December 22, 2025 | 13-066 l. 2309-2312, l. 14-15 | verified (text) |
| 36 | Central Transport Item 985(2) | "arrived within the scheduled window for pickup and no freight is given to Carrier, a charge of $75.00"; 100-CC, effective August 17, 2026 | `CentralTransport_ctii_rules.txt` l. 3070-3076 | verified (text) |
| 37 | Dayton Item 985(1)(a) | TL, volume or exclusive use; "not used due to no fault of the carrier"; "$130.00 per day" | `Dayton_DAFG-19-K_rules_tariff_eff_2026-06-01.txt` l. 4638-4645 | verified (text) |
| 38 | Yellow's rules tariff name | "YRC Tariff 100-754" | 23-003 p. 5 (text l. 270) | verified (text layer) |
| 39 | GlobalTranz BOLs print "Units 0" | 23-003 p. 4 "Total: 0 1"; 23-004 p. 5 "Total: 0 2" | 23-003, 23-004 | verified (text layer) |
| 40 | Register amount | Claim 16200 listed at $0.00 | catalogue 23-002; set 23 `source.md` l. 8 | verified (the catalogue's record of the register; the register itself not re-opened, offline) |
| 41 | Short-pay rules | Nine of ten LTL rules tariffs read bar offsets or withholding | `research/s5_check_AO_c09_carriers_and_access.md` §0, §AO1.1 | verified (AO's own finding; not re-opened at the tariffs) |
| 42 | Approved claim's draft date | "Draft Date 06/20/23" (claim N) | `doc-exploration.md` §5.5 D06 (23-006 p. 5) | as recorded in §5.5; not re-opened |
