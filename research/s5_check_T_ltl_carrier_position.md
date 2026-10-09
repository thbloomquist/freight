# S5 check T: the LTL carriers' documented position (card C-11)

- **What this is:** new desk research for S5 ("Validate with primary evidence") in run 01. It covers **one side of one card**:

  | Card | Side covered here | Why this side is counterparty-only (C21) |
  |---|---|---|
  | C-11 | LTL carriers | They hold the tariff and the reweigh and dimensioner record, and we would never sell to them. The small shipper pays us (`submarket_selection.md` S5, C21; `4_scorecard.md` §3.1) |

  Under rule C21 this side is covered by its **documented position** (rules, tariffs, dockets, dispute windows) plus 1-2 interviews with people who work against carriers daily. This file is the documented position, plus a brief for those interviews (§8).
- **The open S4 question it serves** (`4_scorecard.md` §7.1): "Will an LTL carrier grant a credit on evidence we produce, when the carrier holds the measurement record? And what is the real correction rate?"
- **Not covered here:**
  - the paying side (small shippers): interviews, commitments, the savings assessment (S5 steps 1-3);
  - parcel carriers, truckload, and Canada or Mexico rules;
  - individually negotiated carrier contracts (not public);
  - legal advice. Where the law is unclear, this file says so and marks it **[our call]**.
- **Date:** 2026-09-16.
- **Status:** input to S5; **it decides nothing.** Suggested directions for rows are labelled **[our call]**. The coordinator makes the calls.
- **Labels:**
  - *verified*: read at the source (a quote from the page or PDF, or a value from a downloaded file).
  - *assumed*: a search snippet, a secondary summary, a vendor claim, memory, or a blocked page. **Vendor figures are always *assumed*,** even when read on the vendor's own page.
  - **[our calc]** marks our arithmetic; **[our call]** marks our judgement.
  - **Affiliation flags.** A carrier's or association's statement counts as a source, but it is shown with who is speaking:
    - NMFTA (the carriers' classification body; its members are LTL carriers);
    - a named carrier (speaking for itself);
    - SMC3 (an LTL pricing-data company that also runs industry events);
    - New Hampshire Division of Weights and Measures (a state regulator that has taken shipper complaints).
- **New sources** are N-T01 to N-T50 (§10). Earlier sources keep their IDs. All were accessed on 2026-09-16. Downloads are in the session scratchpad (`…/scratchpad/checkT/`).

**Freight words used here:**
- **LTL (less than truckload):** freight from many shippers mixed in one trailer. Priced per 100 lb by **class**.
- **Class:** one of 18 price bands (50 to 500). A higher class costs more. Light, bulky freight gets a higher class.
- **Density:** pounds per cubic foot (pcf). Cube = length × width × height in inches ÷ 1,728.
- **Handling unit:** one pallet, crate or loose piece handled as a unit.
- **NMFC (National Motor Freight Classification):** the book of commodity **items** (numbered, with "subs") and **rules** (also numbered "Items") that assigns classes. Published by **NMFTA** (National Motor Freight Traffic Association). Changed through public **dockets** run by NMFTA's **FCDC** (Freight Classification Development Council).
- **BOL (bill of lading):** the shipping document the shipper fills in: description, NMFC item, class, pieces, weight.
- **Rules tariff:** a carrier's public rulebook of extra charges and procedures. It governs unless a written contract says otherwise.
- **Reweigh / reinspection / reclass:** the carrier re-weighs, re-measures or re-describes the freight after pickup, re-rates it and usually adds a fee.
- **W&R / W&I / SRV:** "weight and research", "weight and inspection", "shipment research validation": carrier names for the teams that do this. The **inspection certificate** (or W&R certificate) is their record of it.
- **Dimensioner:** a machine (overhead scanner or forklift-mounted) that measures a handling unit. **NTEP** (National Type Evaluation Program) approves device types. **NIST Handbook 44** sets device rules that states adopt into law. **Legal for trade** means approved and certified for commercial billing.
- **Bill-to party:** whoever pays the freight bill. For many small shippers this is a 3PL or broker. **PRO number:** the carrier's shipment number.
- **Overcharge claim / billing dispute:** a written request to the carrier for money back or a corrected bill.
- **STB (Surface Transportation Board):** the federal agency with residual authority over motor-carrier billing disputes.
- **ClassIT+:** NMFTA's paid NMFC lookup (web app and API). **PFC API:** NMFTA's "Preliminary Freight Charges" data standard for notifying billing changes before the final invoice.
- **Accessorial / extra-service charge:** a fee on top of the linehaul rate (liftgate, reweigh fee, over-length).

---

## 1. Summary table

The position in 12 rows. "Carrier" means the LTL carrier; "shipper" includes its authorized agent.

| # | Rule | What it lets the carrier do | What the shipper can do | Window | Evidence that counts | Label / source |
|---|---|---|---|---|---|---|
| 1 | NMFC Item 250100 ("formerly Item 360"), Sec. 3 Inspection, Sec. 4 Verification of weight; Uniform BOL terms Sec. 7(c)-(d) (Item 250150) | Inspect any shipment, reweigh it, correct the description; "freight charges must be paid based upon the articles actually shipped" | Nothing in these items. They grant the right, not a remedy | None stated | The carrier's own inspection | *verified* (2019 and 2022 NMFC text), N-T06, N-T08. Dec 2025 wording change *assumed*, N-T14 |
| 2 | NMFC Item 110 Sec. 8 (cube and density), Item 640 (mixed shipments), Item 995 (gross weight includes the pallet) | Compute density per handling unit, or on the whole shipment when only a total weight is shown | Show weight and dimensions **per handling unit** on the BOL, so the carrier must rate each unit | At tender | The BOL itself | *verified*, N-T09, N-T10, N-T11 |
| 3 | Carrier inspection and reweigh items (9 tariffs, §3) | Re-rate and add a fee of **$15 to $55** per correction | Pay, then dispute | Fee applies at correction | Carrier's scale, dimensioner or inspector | *verified*, N-T17 to N-T30 |
| 4 | Carrier "proof" rules (Estes, SEFL, TForce Item 170/360/361; ODFL, R+L, Saia corrected-BOL items) | Refuse a correction unless proof satisfies the carrier; Saia: "within Carrier's sole discretion" | Submit "an invoice or packing slip along with a pre-printed specification sheet or catalog page" listing weight and shipping dimensions | R+L and XPO: corrected BOL within 30 days of acceptance; FedEx: no dimension correction after tender for delivery (cube-rated freight) | **Shipper-origin documents.** TForce: a re-typed BOL "will NOT be accepted as proof" | *verified*, N-T19, N-T20, N-T22, N-T24, N-T26, N-T28, N-T30 |
| 5 | Carrier document portals and APIs | Hold the certificate, photos and dimensioner record | Download them as the bill-to party (ODFL: "Linked to the bill to party on the pro") | While kept online | Inspection certificate, weight certificate, W&R photos, cube certificate | *verified* for ODFL, XPO, TForce, R+L; *assumed* for Estes (page extraction), N-T18, N-T21, N-T23, N-T27, N-T29 |
| 6 | NIST Handbook 44 §5.58 (dimensioners used to calculate freight charges) | Use a dimensioner for billing | Ask for device ID, dimensions and volume: "available upon request by customer" | Kept "for at least 30 calendar days after the date of invoicing" | Device record | *verified* (2024 edition), N-T31. Whether each state enforces it on LTL terminals: not found |
| 7 | 49 U.S.C. 13710(a)(3) | Rebill extra charges only "within 180 days of the receipt of the original bill" | Contest "the original bill or subsequent bill within 180 days of receipt of the bill"; ask the STB to decide | 180 days each way | Any | *verified*, N-T01 |
| 8 | 49 CFR Part 378; NMFC Items 300500-300520 | Must acknowledge a written claim in 30 days and pay, decline or settle in 60 days, "citing tariff authority" | File in writing, as shipper "or its authorized agent"; one claim may cover many shipments on the same tariff issue | 30 / 60 days for the carrier | Freight bill plus "other documents or data" | *verified* (CFR current; NMFC text of 2015), N-T05, N-T07 |
| 9 | NMFC Item 300530 (arbitration) and carrier exceptions | Force binding arbitration of billing disputes | XPO: arbitration unless over $10,000; Saia and R+L exclude it and name courts | Start "within thirty (30) days" of impasse; XPO: never after 210 days from the original bill | Any | *verified*, N-T07, N-T20, N-T24, N-T26 |
| 10 | 49 U.S.C. 14705 | — | Sue to recover overcharges "within 18 months after the claim accrues" (on delivery); +6 months after a written disallowance of a timely claim | 18 months | Any | *verified*, N-T02. How it applies to non-tariff freight: **[our call]**, unclear |
| 11 | Carrier tariff overlays on the above | Start the 180-day clock at shipment or deemed receipt; bar offsets; set venue; waive class actions (TForce); $50 fee on some settled claims (ODFL) | Comply, or rely on the statute | 180 days, counted from earlier dates than the statute | — | *verified*, §3 |
| 12 | NMFTA interpretations | — | Buy a neutral classification opinion: "$50 for a single inquiry"; "aren't legally binding" | None | Product facts | *verified* (page extraction), N-T15 |

---

## 2. NMFC rules and dockets

### 2.1 The rules that let a carrier change a bill after pickup

**The numbering has moved.** Old guides cite "Item 360"; the current number is **Item 250100**.
- The 2019 NMFC supplement heads the item "ITEM 250100-A (FORMERLY ITEM 360)" (N-T06, *verified*).
- XPO, ODFL, ABF and the NMFTA cite Item 250100 in 2025-26 (N-T20, N-T17, N-T33, N-T34, *verified*).
- Some carriers still cite "item 360, section 2", for example Pitt Ohio's rules page (N-T49, *verified*). **Verify, don't guess**, as asked.

**Item 250100 (text as of 2019, NMF 100-AS; N-T06, *verified*):**
- Sec. 2(c): BOLs "must specify number of articles, packages, or pieces, and the applicable NMFC class", with "the gross weight" per commodity description.
- Sec. 3(a) Inspection of Property: "When carrier or its agent believes it is necessary to verify the stated description … the carrier or its agent will make or cause such inspection to be made, or require other sufficient evidence … If the stated description is found to be inaccurate, the carrier or agent shall correct the description accordingly. Freight charges must be assessed according to proper description."
- Sec. 4 Verification of Shipment Weight: "the carrier or agent shall weigh the shipment … If the stated weight is found to be inaccurate, the carrier or agent shall correct the weight accordingly."
- Sec. 1(f): if the payor requests "any material or information as a prerequisite to payment, such requests will be provided subject to the provisions of applicable carrier tariffs."
- **No NMFC requirement found** for an inspection certificate's content, photos, or dimensioner certification (N-T06, *verified* for the 2019 text).
- **Dec 2025 change:** NMFTA's help centre says Supplement 2025-2 (effective 2025-12-06) added "and/or Dimensions" to the Sec. 4 title "to clarify verification of dimensions is allowed", and tied Sec. 3(a) to "Section 7(d) of the Terms and Conditions to the Uniform Bill of Lading" (N-T14, snippet, *assumed*; the page returned 403).

**Uniform Straight Bill of Lading terms (Item 250150; NMF 100-AV, 2022; N-T08, *verified*):**
- Sec. 7(a): the shipper is liable for charges "as billed or corrected as specified in 49 U.S.C. §13710".
- Sec. 7(c): "the carrier has the right to inspect any shipment tendered to it for transportation."
- Sec. 7(d): "If the description of the articles, including weight or density of shipments, or other information on this bill of lading is found to be incorrect or incomplete, the freight charges must be paid based upon the articles actually shipped."

**Item 110 Sec. 8 (cube and density).** Quoted by NMFTA (N-T09, *verified*):
- Sec. 8(d): "Unless otherwise provided, where a shipment consists of multiple handling units the density shall be calculated on each handling unit, except that where shipping papers show only a total weight for all handling units tendered the density may be calculated by using the total weight and the total cube."
- Cube uses "the greatest straight-line dimensions … including all projections, if any, as tendered".
- FedEx Freight, XPO and TForce apply these methods by reference (N-T19, N-T20, N-T28, *verified*). XPO adds "a minimum vertical dimension of 96 inches" for articles 75 inches or taller (N-T20, *verified*).

**Item 170 (application of classes, the "inadvertence" rule) and Item 171 (bumping).**
- Every density-based NMFC item reads "subject to Item 170" (N-T10, N-T11, *verified*).
- Carriers publish exceptions to Item 170 that set what happens when the BOL lacks density or a valid item:
  - Estes: class 175;
  - TForce: class 100, or highest class up to 250;
  - XPO: class 150;
  - SEFL: a density table, else class 150.
  - All four: N-T22, N-T28, N-T20, N-T30, *verified*.
- TForce's Item 171 describes NMFC Item 171 "Bumping" as "the declaration on the original bill of lading of an artificially higher weight … to qualify for a lower classification rating", and says NMFC Item 171 "will not apply" on TForce (N-T28, *verified*).

**Item 640 (mixed shipments) and Item 995 (gross weight).**
- Carriers publish their own exceptions to Item 640 Sec. 3. When an inspection finds the BOL inaccurate, they rate the whole shipment on overall density:
  - ODFL Item 640;
  - FedEx 640;
  - Estes 645;
  - R+L;
  - all: N-T17, N-T19, N-T22, N-T26, *verified*.
- Docket 2025-2 proposed that Item 995 Sec. 1 read "density shall be computed on actual gross weights … A shipping carrier, container or package, or pallet, platform or skid constitutes part of the gross weight" (N-T10, *verified* as a proposal; its disposition was not read).

**Claims and disputes inside the NMFC (text as of 2015, NMF 100-AO Supplement 1; N-T07, *verified*; current wording not read):**
- Item 300510-A: "Claimant: Any shipper or receiver, or their authorized agent, filing a billing dispute with a carrier."
- Item 300520-A:
  - "All billing disputes must be filed within 180 days from the receipt of the original invoice. Receipt of original invoice shall be determined to be 5 business days from the invoice date."
  - A dispute "may include more than one shipment" on "the same tariff issue".
  - The carrier acknowledges "within 30 days", asks for missing information "in 5 business days", and must "pay, decline to pay, or settle each billing dispute within 60 days".
- Item 300530-A: disputes "shall be submitted to binding arbitration … Transportation Arbitration and Mediation, PLLC, Washington, DC, or another body … commenced within thirty (30) days after the parties are unable informally to resolve the dispute".
- NMFC provisions are for "participants in the NMFC" only (N-T07, *verified*). NMFTA calls the NMFC "a voluntary standard" (N-T41, *verified*).

### 2.2 What the dockets changed

| Docket | Effective | What it changed that bears on reclasses | Label / source |
|---|---|---|---|
| 2025-1 | 2025-07-19 | 13-sub density scale (sub 11 = 30-35 pcf class 60; sub 12 = 35-50 pcf class 55; sub 13 = 50+ pcf class 50). Items without handling, stowability or liability concerns "would be canceled and referenced within a 13-sub density item". **More freight is now rated on the measured density, so a carrier's tape or dimensioner decides more bills.** NMFTA, asked about "more reclass events": shippers must "capture accurate handling unit dimensions and weight … Doing so will help reduce classification changes." And: "NMFC rule changes are not within the current scope of Docket 2025-1" | *verified*, N-T09; N-G20, N-G21 |
| 2025-2 | 2025-12-06 | 17 subjects, including Item 110 Sec. 20 ("not taken" removed; class 0), Item 995 (density on gross weight including the pallet), Item 245 (crates). The Item 250100 change on verifying dimensions was published in the same supplement | subjects and dates *verified*, N-T10; Item 250100 *assumed*, N-T14 |
| 2026-1 | 2026-05-23 | 22 subjects; more items moved onto the 13-sub scale. **Subject 1, a rewrite of Item 640 (mixed shipments), was "DISAPPROVED"** at the 2026-03-10 meeting. It would have added "When the billed weight differs from the actual weight, and the dimensions are not verified, the density shall be recalculated … provided the shipper lists the separate dimensions for the handling unit(s)" | *verified*, N-T11, N-T12; N-R03 |
| 2026-2 | open (comments due 2026-09-23; meeting 2026-09-29) | "approximately 33 proposed changes". A revised Item 640 is reported to be back on this docket | dates *verified*, N-T13; Item 640 *assumed*, N-T14 |

**Carrier practice around the dockets:**
- FedEx Freight "delayed enforcement" of the 2025 changes for 150 days, to 2025-12-01 (N-T47, trade press, *assumed*).
- XPO's strategy chief said "the transition went very smoothly" (N-T47, *assumed*).

### 2.3 NMFTA tools a shipper can use

- **Interpretations.** "$50 for a single inquiry or $225 for a block of five". "While these interpretations aren't legally binding, they offer authoritative guidance". "Typically, about 80% of requests come from carriers" (N-T15, NMFTA, 2025-09-03, *verified* page extraction).
  - NMFTA told regulators such opinions "can be persuasive when shippers and carriers are working through differences" (N-T33, *verified*).
- **Preliminary Freight Charges (PFC) API standard** (launched August 2025).
  - It notifies "reweighs and reclassifications" and accessorial changes before the final invoice, with reason codes such as "RWE, RCL" (N-T16, *verified* page extraction; N-R02).
  - NMFTA's stated reason: "billing surprises that hit weeks after pickup" (N-R02, *verified*).
  - Not found: any carrier that has implemented it, whether it carries photos or certificate links, or any requirement to adopt it. Estes led the working team (N-T16, trade press, *assumed*).
- **No NMFTA or CCSB dispute or inspection-report process for shippers was found** beyond interpretations. The NMFC's own route is Items 300500-300530 above.
  - CCSB (Commodity Classification Standards Board) is the former name of today's FCDC (memory, *assumed*).
  - NMFTA's own list of routes is: carriers' internal procedures in their tariffs, 49 CFR 378, interpretations, then STB or court (N-T33, *verified*).

---

## 3. Carrier rules tariffs compared

**Nine carriers, nine public rules tariffs, all downloaded and searched** (N-T17 to N-T30). An empty cell means the tariff was searched and says nothing on the point. The two tables below are *verified* unless marked.

### 3.1 Fees, triggers and devices

| Carrier · tariff · effective | Reclass / inspection fee (item) | Reweigh fee and trigger (item) | Other correction fees | Device and certification stated |
|---|---|---|---|---|
| **Old Dominion** · ODFL 100-Q · 2025-04-14, pages revised to 2026-07-22 | $25 per shipment when inspection "results in a reclassification" (367.2); $25 "shipment verification fee" if BOL description, density or weight is wrong (162) | $25 if weight rises **20 lb** or more (367.6); $25 to weigh an unweighted shipment or on request (367.7) | Corrected BOL $40 (365) | Portable scales "for trade and meet all local and state laws regarding accurate weight within 1% tolerance" (367.5). Dimensioners not mentioned |
| **FedEx Freight** · 100-Y · 2026-01-05 (Item 438 revised 2026-06-01) | $40 "freight validation fee" per adjustment "due to an inspection" (981.4); one fee per shipment (981.5) | $40 if weight rises **50 lb** or more, or falls **200 lb** or more; under +50 lb "no changes in linehaul charges" (981.1-3) | Weighing on request: $155 carrier scale, $419 certified public scale (990) | "Carrier's legal for trade scale, or a public certified scale" (980.2, 990.2). DIM systems "used on over 90% of shipments" (Form 10, N-T36) |
| **XPO** · CNWY 199-AK.1 · 2026-02-16 | $47.85 "correction fee" when an inspection raises linehaul by **$1.00** or more (26.4) | $47.85 if weight rises **25 lb** or more (239 §2) | Shipper-requested correction $49.80 (205) | None stated |
| **Estes** · EXLA 105 FF · 2026-01-02 (993 revised 2026-08-03) | $20 "commodity inspection service charge" when the BOL description is inaccurate, vague or missing (993-10) | $25 if weight rises **100 lb** or more, or falls **500 lb** or more (992.2); $20 weighing service (993) | Letter of authority after 30 days $20 (360-03) | Scales "that are NTEP certified legal for trade" (992.1). FAQ: invoices change on "shipment dimensioner scanning results" (N-T23, *assumed*) |
| **Saia** · 170-D · 2025-10-01 | $39 "per occurrence" when inspection or reweigh changes weight or NMFC class (850) | Same $39 (850); $33 weight determination | — | None stated |
| **ABF (ArcBest)** · ABF 111-AU · 2026-06-22 | $55 "reclassification fee" when net charges change **$10** or more (420) | $55 when charges change **$10** or more (992.2); weighing on request $91.48 (992.4) | "Measure or verify cube/dimensions" at "sole discretion" (991) | Scales "with a manufacturer's specified tolerance of plus or minus 1% … regularly verified" (992.1). ABF to NCWM: "NTEP-approved forklift scales … tested annually as regulated and weekly independently" (N-T34) |
| **R+L** · Rules tariff · updated 2026-09-07 | $40 "Inspection Fee" when a reclass changes charges **$10** or more (991, eff. 2025-08-04) | $40 when a reweigh raises charges **$10** or more, "not subject to discounts" (992.3) | Corrected BOL $45.90 (364) | "Dimensioning Machinery" may verify density (359; 640 exception); 96-inch height rules restricted to freight "physically inspected or verified by Dimensioning Machinery" (490.3). No certification stated |
| **TForce Freight** · UPGF 102-T · 2026-03-16 | $40 when inspection raises net charges **$15** or more (365.2) | $40 when a weight error raises charges **$15** or more (990.2); certified public scale $220 (990.3) | Freight bill correction $50 before delivery, $48 after (361.5) | Scales "with a manufacturer's specified tolerance of plus or minus 1%. The accuracy of such scales will be regularly verified" (990.1) |
| **Southeastern (SEFL)** · 1090 · contents eff. 2026-06-01; Item 996 eff. 2025-12-01 | $15 "correction fee" if "any adjustments are made to weights, dimensions, and/or NMFC classes" (996) | Same $15 (996) | Corrected BOL $35 (360-5) | "scales and/or dimensioners that are NTEP-certified and legal for trade" (996) |

**Notes on 3.1:**
- **Fee range: $15 (SEFL) to $55 (ABF), on top of the re-rated linehaul, fuel and accessorials** [our calc from the table].
- **Triggers differ widely:** ODFL +20 lb, XPO +25 lb, FedEx +50 lb, Estes +100 lb; ABF and R+L on $10 of charges, TForce on $15, XPO on $1 of linehaul.
- **Asymmetries in the carriers' own text** (*verified*):
  - R+L corrects weight "Only when the tendered weight on the Bill of Lading is found to be at least 50lbs less than the actual weight" (992.2). Downward reweighs are not credited.
  - ABF "will not process reductions freight charges" unless they exceed "a $55.00 reweigh fee and other processing and administration charges" (992.3).
  - R+L: a corrected weight changes density-based classes only where the handling units' dimensions were "documented by the carrier thru physical inspections or by Dimensioning Machinery" (992.2).
  - Saia is the exception in the shipper's favour on mixed pallets: the increased weight is charged "at the lowest rated commodity" (850). Estes and TForce put it on the highest-classed item (992.4a, 990.2a).
- **Only three of nine tariffs state that devices are NTEP-approved or legal for trade:**
  - Estes and SEFL say NTEP;
  - FedEx and ODFL say legal for trade, or "for trade";
  - ABF and TForce state a ±1% manufacturer tolerance;
  - XPO, Saia and R+L state nothing.
  - Only SEFL names **dimensioners** as certified.

### 3.2 Evidence, proof, windows and dispute routes

| Carrier | Can the shipper get the record? | What the carrier accepts as proof for a correction | Shipper's window (as the tariff states it) | Carrier's rebill window stated | Dispute route and conditions |
|---|---|---|---|---|---|
| **ODFL** | Yes, to the bill-to party. Document API types include "Inspection Certificate", "Weight Certificate", "Weight Verification", "Research Verification", "Pickup Photo"; each "Linked to the bill to party on the pro" (N-T18, updated 2026-06-04) | Corrected BOLs changing description, density or weight need "conclusive documentary proof"; carrier may refuse corrections "not … verified to the satisfaction of Carrier" (365.5-6) | Overcharge claims "no more than 180 days after Carrier's receipt of the shipment" (396.1) | — (statute applies) | Claim "deemed closed 30 days after the date of the initial ruling"; no new claim on a closed invoice (396.2-3); "a charge of $50.00 on settled overcharge claims that were through no fault of Carrier" (396 Note A); no offset (395); exclusive venue Guilford County, NC (437); 49 CFR 378 applies (396) |
| **FedEx Freight** | "Carrier will make a copy of the written or electronic weight verification available to Shipper or Consignee upon request" (980.2). Portal or API document list: not found | Weight corrections stand unless "Shipper provides documentation that the weight was in error" (980.3). Cube-rated freight: corrected BOL to change dimensions "will not be accepted after shipment has been tendered for delivery" (191.6) | Actions to recover overcharges "commenced not more than 180 days from the receipt of the original invoice plus 7 days"; expiry "a complete and absolute defense" (438.1) | None stated (statute applies). Balance-due bills are payable "30 days from presentation of the subsequently issued freight bill" (435.2) | Disputes "with detailed supporting information" by email (fxfrevsoltn@fedexfreight.com) or phone; undisputed invoices due on terms (438.2-3) |
| **XPO** | Yes, via login. Document Finder types: "Weights and Corrections, Weights and Research Photos, … Inspection Report, NMFC Certificate" (N-T21, page extraction) | Improper descriptions are billed at class 150 and "subject to inspection" (26.3); "Upon submission of satisfactory proof of a higher actual density or lower class, freight charges will be adjusted" plus the $49.80 fee (28); shipper changes "within thirty days (30) days after the shipment has been accepted" (205) | "Debtor must contest the original bill within 180 days of the date of the original bill" (23.5; BOL terms para 9) | "Carrier must issue any bill for charges in addition to those originally billed within 180 days of the date of the original bill" (23.5) | Overcharge claims with freight bill and "tariff authority" (23); no withholding or offset; NMFC arbitration applies except disputes over $10,000 (31); arbitration "no later than thirty (30) days" after impasse and never "after 210 days of the date of the original bill" (BOL terms para 9) |
| **Estes** | Yes, via My Estes. "retrieve weight and research certificates through our Document Viewing and Weight and Research Inquiry tools" (N-T23, page extraction, *assumed*) | "'Proof' is described as an invoice or packing slip along with a pre-printed specification sheet or catalog page, which lists the commodity description, weight and shipping dimensions" (170 Note C); weight shifted between items "Upon submission of satisfactory proof" (992.4) | None stated in the tariff | — | Online "Rating and Billing Discrepancies" tool; results "within 24 to 48 hours" (N-T23, carrier claim, *assumed*); no offset; loss and damage claims need a paid freight bill (825) |
| **Saia** | Not found (Saia's rules web pages returned 404; no document-type list found) | Corrected BOLs need "conclusive documentary proof … Any decision on whether to accept corrections … shall be within Carrier's sole discretion" (360.10) | "Shipper or Payor must contest the original bill or file a claim for overcharge within 180 days of the date of the original bill" (1030.6) | "within 180 days of the date of the original bill" (1030.5) | Incorporates 49 CFR 378 "as the minimum requirements" (1030.7); no short payment or credit-taking; NMFC arbitration items 300530, 300160 and 400150 "shall not apply" (1041) |
| **ABF** | ABF to NCWM: "The inspection process includes measurements of the handling units, photos of the shipment and any documents accompanying the shipments and a detailed report is completed" (N-T34). Retrieval of "weight confirmations" in the portal (N-T50, snippet, *assumed*) | Reclass fee applies to corrections "caused by incorrect description(s) on the original or corrected bill of lading supplied by the shipper" (420); proof standard not stated | "all overcharge and undercharge claims … shall be filed within 180 days of the initial shipment date"; lawsuits "within 18 months of the initial shipment date" (428) | Same 180 days, for undercharge claims (428) | ABF to NCWM: "billing disputes based upon changes made due to SRV (W&R) corrections are most often resolved internally. However, when needed, we get input from NMFTA's interpretations department" (N-T34) |
| **R+L** | Yes. Document Retrieval API returns "BillOfLading, DeliveryReceipt, Invoice, WeightCertificate, NmfcCertificate, LetterOfAuthorization, DeliveryPhoto" for documents "you have access to" (N-T27) | Corrected BOLs need "conclusive documentary proof", may be refused if "not been verified to the satisfaction of the carrier", and "can be submitted by the Shipper within thirty (30) days after the shipment has been accepted" (364) | No overcharge-claim item found. Refund programmes: "Any discrepancies in amounts paid must be presented to Carrier in writing within 180 days of the date of the shipment" (161, refund context) | — | Exception to NMFC arbitration items; Ohio law; exclusive courts: S.D. Ohio or Clinton County, OH (169) |
| **TForce** | Yes. Documents API types include "WRC Weighing And Research Certificate", "REWE Reweigh Ticket", "CMC Cube Measurement Certificate" (N-T29, manual dated 2024-09-06) | Proof is "an invoice or packing slip along with a spec sheet or catalog page that lists the commodity description, weight and shipping dimensions … A bill of lading covering the same shipment or a copy of the original bill of lading with typed or hand-written description, weight, density or class changes is NOT acceptable" (360 Note); after delivery, weight, cube or density changes need "a pre-printed spec sheet or catalog page" (361.5d) | Overcharge claims "within 180 days of receipt of Carrier's freight bill … receipt shall mean 10 days after the shipment has been tendered"; civil action within 18 months (813) | — | Claims "extinguished" unless every notice period is met and pleaded (812.2); no set-off; class-action waiver (812 Part 2); processed per "NMFC series items 300500 and 49 CFR Part 370" (813; Part 370 is the loss-and-damage part, so this citation looks like a slip, **[our call]**) |
| **SEFL** | Not found. Glossary defines W&I as "a process used to audit freight" (N-T50, snippet, *assumed*) | "'Proof' is described as an invoice or packing slip along with a pre-printed specification sheet or catalog page" (170 Note 3); corrected BOLs need "documentary proof" (360-5.5) | Allowances: "Any discrepancies in payment must be presented to the carrier in writing within 180 days of the date of shipment" (202.7, allowance context). No overcharge-claim window found | — | Not stated in the tariff |

**Notes on 3.2:**
- **The proof carriers name is the shipper's own paperwork, made before pickup:**
  - an invoice or packing slip;
  - **plus** a *pre-printed* spec sheet or catalog page with weight and shipping dimensions.
  - Three carriers define it that way (Estes, SEFL, TForce). Three more demand "conclusive documentary proof" at the carrier's satisfaction or sole discretion (ODFL, R+L, Saia).
  - **No tariff names** a shipper's own dimension scan, a scale photo or ticket, or a third party's measurement as proof (all nine searched, *verified*). Vendors call a scale photo "the single best piece of evidence" (N-T46, *assumed*).
- **Windows are shorter than the statute in practice.** The statute counts 180 days from receipt of *the bill*, including a later balance-due bill (N-T01). Several tariffs count from the shipment date or a deemed receipt:
  - ABF: "initial shipment date";
  - ODFL: "Carrier's receipt of the shipment";
  - TForce: receipt deemed 10 days after tender;
  - FedEx: invoice receipt + 7 days.
  - Correction routes are shorter still: XPO and R+L allow 30 days from acceptance; FedEx allows no dimension change after tender for delivery on cube-rated freight (*verified*).
  - Whether a tariff can shorten the statutory window for tariff (non-contract) freight is a legal question. **[our call]:** a lawyer is needed; the product should simply beat the shortest clock.
- **Contracts override all of this.** Tariffs apply "Unless otherwise agreed to in writing" (ODFL 360.4, *verified*). The statute lets parties "expressly waive any or all rights and remedies under this part" in a written contract (49 U.S.C. 14101(b), N-T03, *verified*).
  - NMFTA told NCWM that "a large percentage of the freight … moves pursuant to individually-negotiated transportation contracts … that include terms and conditions for making and processing class and price adjustments" (N-T33, *verified*).
  - Small shippers booked through a 3PL may be on the 3PL's contract, with terms we cannot see (**[our call]**; not verified).
- **The record sits with the bill-to party.** ODFL publishes inspection certificates and photos only to "the bill to party on the pro" (N-T18, *verified*). When a 3PL is the bill-to party, the shipper sees the carrier's evidence only through the 3PL (**[our call]**).
- **Carriers are only liable for their own adjustments.** NMFTA asked that a state law make clear a carrier "is potentially liabile only for price adjustments that it has made, not adjustments independently made and passed on by an intermediary" (N-T33, *verified*). A 3PL may pass on (and mark up) corrections separately (**[our call]**).

---

## 4. Federal law and windows

**49 U.S.C. 13710 (additional billing and collecting practices)** (N-T01, law.cornell.edu, *verified*):
- (a)(1): a motor carrier "shall provide to the shipper, on request of the shipper, a written or electronic copy of the rate, classification, rules, and practices, upon which any rate applicable to its shipment … is based."
- (a)(3)(A), carrier-initiated: "A carrier must issue any bill for charges in addition to those originally billed within 180 days of the receipt of the original bill in order to have the right to collect such charges."
- (a)(3)(B), shipper-initiated: "If a shipper seeks to contest the charges originally billed or additional charges subsequently billed, the shipper may request that the Board determine whether the charges billed must be paid. A shipper must contest the original bill or subsequent bill within 180 days of receipt of the bill in order to have the right to contest such charges."
- Both apply to motor carriers other than household-goods and noncontiguous-trade carriers, which covers ordinary LTL (*verified*, text of (a)(3)(A)).

**49 U.S.C. 14705 (limitation on actions)** (N-T02, *verified*):
- (a): a carrier "must begin a civil action to recover charges … within 18 months after the claim accrues."
- (b): "A person must begin a civil action to recover overcharges within 18 months after the claim accrues." If the person elects a complaint to the Board under 14704(c)(1), "the complaint must be filed within 3 years".
- (d): the periods "are extended for 6 months from the time written notice is given to the claimant by the carrier of disallowance of any part of the claim … if a written claim is given to the carrier within those limitation periods."
- (g): "A claim related to a shipment of property accrues under this section on delivery or tender of delivery by the carrier."
- **Caveat.** 14704(b) defines the overcharge liability as amounts "that exceed the applicable rate … contained in a tariff in effect under section 13702" (N-T04, *verified*). NMFTA notes the STB "no longer has authority over the rates set for the movement of general cargo, except for household goods, goods moving in the nonontiguous domestic trade, and goods moving pursuant to collectively-made rates", but that "its broad dispute resolution authority … has not been eliminated" (N-T33, *verified*). **How 14705(b) applies to ordinary LTL freight is unclear to us [our call].** In practice 13710(a)(3), the tariffs and contract law decide.

**49 U.S.C. 14101(b) (contracts with shippers)** (N-T03, *verified*): "If the shipper and carrier, in writing, expressly waive any or all rights and remedies under this part for the transportation covered by the contract, the transportation provided under the contract shall not be subject to the waived rights and remedies".

**49 CFR Part 378 (overcharge, duplicate payment and overcollection claims)** (N-T05, ecfr.gov, current, *verified*):
- 378.1: governs such claims for "motor carriers and household goods freight forwarders subject to 49 U.S.C. subtitle IV, part B."
- 378.2(f): "Claimant means any shipper or receiver, or its authorized agent".
- 378.3(a): a claim "shall not be paid unless filed in writing with the carrier that collected the transportation charges."
- 378.3(b): "A single claim may include more than one shipment provided the claim on each shipment involves: (1) The same tariff issue or authority or circumstances".
- 378.4(b): claims "shall be accompanied by the freight bill". They may add "The rate, classification, or commodity description or weight claimed to have been applicable", "Complete tariff authority", payment information, and "Other documents or data which is believed by claimant to substantiate the basis for its claim."
- 378.4(d): failure to send enough documentation "shall not constitute grounds for disallowance of the claim". The carrier must ask for it (378.5(c)).
- 378.7: acknowledge "within 30 days after the date of receipt".
- 378.8: "pay, decline to pay, or settle each written claim within 60 days after its receipt". A decline must give "the reason(s) for its action, citing tariff authority or other pertinent information developed as a result of its investigation."
- 378.9(b): an overpayment the carrier finds itself must be refunded "within 30 days from the date of such discovery".

**What the law does not do** (searched, *verified* by absence in the texts above):
- No federal rule sets what an inspection certificate must contain.
- No federal rule says how long a carrier keeps the inspection record.
- No federal rule makes a carrier share photos.
- The only record rule found is the state-adopted Handbook 44 code (§1 row 6).

**Handbook 44 §5.58, Multiple Dimension Measuring Devices** (N-T31, 2024 edition, *verified*):
- A.1: the code "applies to dimension and volume measuring devices used for determining the dimensions and/or volume of objects for the purpose of calculating freight, storage, or postal charges".
- Table S.1.6: device identification, dimensions and volume must be printed or recorded "and AVAILABLE UPON REQUEST BY CUSTOMER".
- Note 5: that information "shall be retained by the party having issued the invoice for at least 30 calendar days after the date of invoicing."

**A state model law is pending, not adopted.** NCWM item OTH-24.1, the "Uniform Shipment Law", was drafted by New Hampshire's Division of Weights and Measures.
- It would require NTEP devices, and certificates carrying "employee identifier", "unique identifier of the weighing or measuring device", "indicated reweigh or remeasure value … for each handling unit". Certificates would be kept "for the period of two years" (N-T32, 2025 task-group text, *verified*).
- It is still marked "DRAFT" on 2026-07-14 (N-T32, *verified*).
- NIST raised "Commerce Clause considerations" (N-T32, *verified*).
- NMFTA, XPO, ABF and Lynden asked NCWM to reject or table it, citing federal preemption under 49 U.S.C. 14501(c)(1) (N-T33, N-T34, *verified*).

---

## 5. Correction and win rates

**Plainly: no neutral correction rate and no neutral dispute win rate was found.** This repeats S3a's result. What was found is one carrier-filed **size bound** and several carriers' **statements** without numbers.

### 5.1 Primary or carrier-filed evidence (neutral in the sense of audited or public filings, but speaking for the carrier)

| Figure | Source | What it is, and what it is not | Label |
|---|---|---|---|
| FedEx Freight's "DIM systems, used on over 90% of shipments, automate shipment measurement and pricing verification"; "Over $150 million of added total revenue over fiscal years 2024 and 2025 is estimated to be due to DIM technology" | FedEx Freight Form 10 (10-12B/A, filed 2026-04-10) | The largest LTL carrier's own estimate of revenue added by dimensioners. Against revenue of $9,424M (FY2024) + $8,892M (FY2025) that is **about 0.8% of revenue**, or about $3.30 per shipment (assuming FY2024 volume similar to FY2025's 22.7M shipments) **[our calc]**. It covers all dimensioner-driven re-rating and pricing, right or wrong. **It is not a rate of wrong corrections** | *verified*, N-T36 |
| "we dimension 75 percent of our freight every day. … We've invested heavily in dimensioners" | Saia Q2 2025 earnings call, filed as 8-K exhibit 2025-07-31 | Share of freight measured, not corrected | *verified*, N-T37 |
| ArcBest's "Vaux Vision … Captures NTEP certified dimensions" and "arrival/departure photo" | ArcBest Q1 2025 earnings presentation (8-K, 2025-04-29) | Device capability, no rate | *verified*, N-T38 |
| FedEx Freight "allowance for revenue adjustments": provision of $101M in FY2026 | FedEx Freight 10-K FY2026 | All billing credits of every kind, mixed with factoring effects. Not broken out; **not usable** as a correction or win rate | *verified*, N-T36 |
| ABF: "31 inspectors"; W&R billing disputes "most often resolved internally"; escalation "rare" | ABF letter to NCWM, 2025-10-24 | The carrier's own statement. No count | *verified*, N-T34 |
| Lynden: "Lynden Transport has never had a customer have to take" a dispute to the STB or court | Lynden letter to NCWM, 2024-07-17 | The carrier's own statement | *verified*, N-T34 |
| NMFTA: "evidence of any pattern or practice of such errors is lacking" | NMFTA letter to NCWM, 2024-06-28 | Carrier association's position, no data | *verified*, N-T33 |
| New Hampshire W&M: complaints "substantiated"; on one remeasure, "Investigations … confirmed the length of the pallet in question was accurately provided by the Shipper" | NH W&M presentation to NCWM (2023-12-22); task-group report (2025-07) | A regulator's findings, no count | *verified*, N-T32 |
| YRC, Roadway and Yellow paid about $6.85M (2022) to settle allegations that, 2005-2013, they billed the Defense Department higher reweighed weights but concealed lower ones | DOJ press release (page blocked); NH W&M slides | Allegations settled, one carrier, government freight | *assumed* (snippet), N-T40; slide text *verified*, N-T32 |
| One small NH importer: extra reweigh, reclass and length fees "about every third or fourth invoice", "$25 up to $350+"; "Each dispute took months"; a supplier invoice "never seemed enough proof" | Shipper's letter to NCWM, 2025-01-10 | One shipper's own account, through a logistics company | *verified* as the letter's text, N-T35 |
| Dayton Freight: "60+ dimensioners"; "15% of bills still handwritten" | Transport Topics, 2026-08-14 | Trade press summary | *assumed*, N-T47 |

### 5.2 Vendor and secondary figures (all *assumed*)

| Claim | Who says it | Why it is weak |
|---|---|---|
| "70 to 80 percent of freight that comes across docks is now inspected by dimensioners" | SMC3 blog, 2023-08-23 (N-T43) | No method; SMC3 flag |
| "39% of the shipments that are tendered to them have weight discrepancies" | TranzAct blog, 2019, quoting an unnamed LTL carrier CEO (N-T44) | One unnamed carrier, 2019 |
| "Historically, 15% of LTL shipments face reclassification" | search snippet, source page not identified (N-T50) | Untraceable |
| "up to 25% of freight shipments undergo reclassification or reweighing" | MyFreightWorld, 2025-02-17 (N-T46) | Broker marketing, no source |
| "5-15% of LTL spend on reclass + reweigh"; "Most carriers honor disputes when the shipper has documented proof at origin" | Warp, undated (N-T46) | No source. It also states a "typically 200 lbs or 5%" reweigh tolerance that no tariff in §3 matches (triggers are 20-100 lb) |
| "Roughly 4–6% of shipments touch a reclass dispute … recovery rate of 70–82% with BOL + reweigh" | search snippet; a trace search failed to find the page (N-T50) | Untraceable |
| Accessorials averaged "8.7% of total LTL spend in 2023, according to AFS customer data" | AFS Logistics white paper, 2024 (N-T45) | All accessorials, not reclass; audit firm's customers |
| Audit firms recover 3-8% of LTL spend | D'Arrigo Consulting (N-A26) | Consultant; all error types |

**Reading [our call]:**
- The vendor frequency claims span 4% to 39% of shipments. They are not usable for K4.
- The one carrier-filed figure (FedEx, about 0.8% of revenue from dimensioners over two years) is a ceiling on the *dimensioner* part at that carrier, not a floor on overcharges. It suggests reclass and reweigh money is of the order of 1% of LTL revenue at a large carrier.
- Extra-service charges are a separate, larger pool (AFS: 8.7%, *assumed*).

### 5.3 What was searched and not found

- **SEC EDGAR full-text search** (2023-2026 filings) for "reweigh", "reweighs", "dimensioners", "dimensioning", "NMFTA", "NMFC", "density-based" LTL, "weight and inspection", "accessorial revenue" LTL, and "reclassification" "less-than-truckload" (N-T39).
  - Hits: FedEx Freight Form 10 and 10-K, the Saia call, the ArcBest deck and 10-K, and XPO earnings releases.
  - None disclose a correction count, a reweigh or reclass revenue line, or a dispute rate.
  - "reweigh" and "reweighs" returned no LTL filer.
- **NMFTA:** the 2025 changes FAQ, the Q1 2025 industry performance page and the interpretation-services page. No inspection or reclass counts. The only NMFTA number found is "about 80%" of interpretation requests coming from carriers.
- **ATRI:** no ATRI publication on reweighs or reclasses turned up in the searches above. The ATRI issue list held from S2 (R38) was not re-read for this (*assumed*).
- **GAO or STB:** no STB decision under 13710(a)(3) on a reweigh or reclass was found in a site-limited search; no GAO report found.
- **Academic:** a search for studies of LTL reweigh, reclass or dimensioner accuracy returned only vendor pages.
- **NCWM task-group papers:** the July 2025 report cites "substantiated consumer complaints" but gives no count.
- **Trade press after the 2025 changes:** Transport Topics (2026-08-14) quotes carriers but gives no reclass rate.

---

## 6. How disputes work in practice

**The steps, pieced together from carrier tariffs (*verified*) and 3PL or audit guides (*assumed*):**
1. **Catch it early.**
   - Corrections arrive as a changed invoice or balance-due bill "weeks after pickup" (N-R02, *verified*).
   - The PFC API is meant to flag them before the invoice; no adopter was found (§2.3).
2. **Pull the carrier's record the same week.**
   - Certificates, W&R photos and cube certificates are online for the bill-to party at ODFL, XPO, TForce and R+L (§3.2, *verified*), and at Estes (*assumed*).
   - Dimensioner data must be kept only 30 days after invoicing where Handbook 44 applies (§4, *verified*).
3. **Match it against origin evidence.** In the order carriers name it:
   - invoice or packing slip plus a pre-printed spec sheet or catalog page (Estes, SEFL, TForce, *verified*);
   - per-handling-unit weights and dimensions on the BOL (NMFC Item 110 Sec. 8(d), *verified*).
   - Vendors add: a photo of each pallet on a certified scale, the scale's certification, dock photos (Warp; FreightPros; Eniture; N-T46, *assumed*).
   - The NH importer did all of this, including a state-licensed NTEP scale, and "the extra fees continued" (N-T35, *verified* as the letter's text).
4. **Pick the route:**
   - a corrected BOL (30 days at XPO and R+L; never after tender for delivery for FedEx cube-rated freight);
   - a billing dispute (FedEx email; Estes online tool);
   - a formal overcharge claim (49 CFR 378);
   - an NMFTA interpretation for "wrong item" disputes ($50, not binding);
   - arbitration (NMFC 300530; XPO; excluded by Saia and R+L);
   - STB or court.
   - All *verified* (§2-4).
5. **Expect these timelines:**
   - carriers must acknowledge in 30 days and decide in 60 (378.7-8, *verified*);
   - Estes promises results "within 24 to 48 hours" (*assumed*);
   - a broker says "from a couple days to a couple months" (FreightPros, *assumed*); another says "1-4 weeks" (MyFreightWorld, *assumed*);
   - the NH importer: "months" per dispute, then "another few months" to get the 3PL's invoice corrected (N-T35).
6. **Know what loses:**
   - a re-typed or hand-corrected BOL (TForce, *verified*);
   - an NMFC item that is in fact correct: "We cannot dispute NMFC coding itself" (FreightPros, *assumed*);
   - late filing (§3.2);
   - withholding payment: no offset at ODFL, Estes, XPO, Saia or TForce (*verified*);
   - small downward corrections (ABF threshold; R+L upward-only weight rule, *verified*).

**Who does the work today:**
- The bill-to party files. For small shippers booked through a 3PL, the 3PL rep does. WWEX says "we can walk you through your options" (N-T46, *assumed*).
- The NH importer describes "the logistics company's disinterest in helping settle our billing disputes" (N-T35).
- Success rates: **none published by a 3PL, audit firm, NASSTRAC or SMC3** was found. NASSTRAC guidance on reclass disputes was not found. The Unishippers dispute e-guide sits behind a download form, which was not submitted.

---

## 7. The NMFTA dependency

**What NMFC data is needed for** **[our call]:**
- finding the item and sub for a product;
- knowing whether an item is density-rated or flagged for handling, stowability or liability;
- reading the rule texts (Items 110, 170, 640, 250100).
- The density→class tables for full-density items are public in carrier tariffs (ODFL 170 and 640; XPO 26; R+L Table 1; SEFL Table 1; FedEx 640; *verified*). Which items use them is not public.

**Prices** (classitplus.nmfta.org/pricing, N-T41, *verified*; "NMFTA members save 15%"):

| Plan | Member | Non-member |
|---|---|---|
| Web app, 1 seat ("Small") | $321 seat/year | $371 seat/year |
| Web app, 2-15 seats | $269 | $312 |
| API, shipper under $50M revenue | $2,967 /year | $3,412 /year |
| API, 3&4PL under $50M revenue | $3,412 /year | $3,924 /year |
| API, carrier under $50M revenue | $2,580 /year | $2,967 /year |

- "Is there a free version of ClassIT+? No." "Is there an option to pay monthly? No, not yet." (N-T41, *verified*).
- The API "includes a complimentary ClassIT+ Web App user" (N-T41, *verified* page extraction). A bundle saves "30% on your license costs" (N-T41, *assumed*, snippet).
- No concurrent logins: "each user of ClassIT+ to have their own login credentials" (ClassIT FAQ, 2025-01-06, N-T41, *verified*).
- Users may "print or email individual NMFC numbers and their details so you can easily share with customers" (N-T41, *verified*).

**Terms for a software provider serving many shippers: not found.**
- No "technology partner", "software vendor" or reseller tier appears on the pricing page (N-T41, *verified* by absence).
- NMFTA's FAQ (January 2025): "We do not have any details available regarding native integration with TMS providers" (N-T41, *verified*).
- Subscribers must "agree to our new license agreement" (N-T41, *verified*). The agreement is not public.
- NMFTA's terms of use "restrict your rights to reproduce, distribute, adapt, modify, create derivative works, publicly display, or sell any content, without express permission" (N-T42, *verified* page extraction).
- The help-centre API FAQ returned 403.
- NMFTA's developer article (2026-02-17) has no licensing terms (N-T42, *verified*).
- The rules forbid contacting NMFTA, so the question is open.

**Cost or gate: three scenarios** **[our calc]** with **[our call]** readings. The per-shipper fee is from `3_factsheets.md` C-11 item 3: saving $446-3,904 a year, 20% fee $89-781.

| Scenario | Annual NMFC cost | Per customer | Reading |
|---|---|---|---|
| A. One API licence (3&4PL small tier, non-member) covers use for all our customers | $3,924 | $3.92 each at 1,000 customers | **A cost.** Negligible |
| B. Each customer needs its own web seat (bring-your-own licence) | $371 per customer | $321-371 = **41-417%** of the per-shipper 20% fee ($321 member or $371 non-member, against $89-781) | **Close to a gate** for the smaller half of shippers |
| C. The licence bars use for third parties, or display to them | n/a | n/a | **A gate**, unless NMFTA agrees a partner licence |

**Reading [our call]:** which scenario applies decides whether NMFTA is a cost or a gate. It is a question for the founders to put to NMFTA (classitplus@nmfta.org) before any build. It is not a desk question.

---

## 8. Who works against LTL carriers daily (for the 1-2 C21 interviews)

**Firm types, with named public firms or bodies (no individuals):**

| Type | Why they fit C21 | Named examples | Label |
|---|---|---|---|
| LTL 3PLs and brokers booking for small shippers | Bill-to party on many small-shipper loads; file reclass disputes with carriers | WWEX Group (Worldwide Express, Unishippers, GlobalTranz; franchise and agent network); C.H. Robinson (Freightquote); FreightCenter; FreightPros; Warp | WWEX *assumed* (company claim, N-R12); others *verified* as publishers of dispute guides, N-T46 |
| Freight audit and payment firms | Check LTL bills against tariffs and file overcharge claims on contingency | AFS Logistics; TranzAct; Cass Information Systems; D'Arrigo Consulting | AFS, TranzAct *verified* as publishers (N-T45, N-T44); Cass (N-D30); D'Arrigo (N-A26) |
| Audit and dispute software for brokers or shippers | Build dispute packets from carrier documents | Lighthouz; MyCarrier; Freightview | *assumed*, N-T46, N-R22 |
| Shipper and pricing associations | Convene shipping managers and LTL pricing staff | NASSTRAC (shipper council, N-R18); SMC3 (N-T43); Transportation & Logistics Council; Transportation Intermediaries Association | NASSTRAC *assumed* (N-R18); SMC3 *verified*; TLC, TIA *assumed* (memory) |
| Regulators who have investigated | Have seen carrier certificates from the outside | New Hampshire Division of Weights and Measures; NCWM Uniform Shipment Law task group | *verified*, N-T32 |
| Former carrier W&R, SRV or pricing staff | Know how certificates are made and how disputes are decided inside | Alumni of the nine carriers in §3 (ABF says its SRV department has "a management staff that handles disputes") | *verified* quote, N-T34 |
| NMFTA interpretations department | Neutral-ish opinions; sees both sides (80% of requests from carriers) | NMFTA FCDC | *verified*, N-T15 |

**Suggested pair [our call]:**
- (1) an LTL 3PL or franchise rep who files reclass and reweigh disputes for small shippers every week;
- (2) either a freight-audit LTL analyst or a weights-and-measures investigator who has handled these complaints (a public official, reached through the agency).

**What the interviews must settle** (about specific past disputes, not our idea; R35):
1. **Win rate by type.** Of the last 20 reclass, reweigh or remeasure corrections you disputed, how many got a full credit, a partial one, or none? Split them into "wrong item or description" and "disputed measurement".
2. **Evidence that worked, per carrier.** Which carriers credited on packing slip plus spec sheet? Did any accept a scale photo or ticket, a shipper's own dimension scan, or a third party's measurement? Which refused all of these?
3. **Agent filing.** Has any carrier refused a dispute filed by an agent or a software platform on the shipper's behalf, or insisted the bill-to party file?
4. **Access to the record.** For which carriers do you get certificates and photos, how fast, and for how long? Do certificates show the device ID, the per-unit measurements and the inspector?
5. **Rates.** What share of your small-shipper LTL shipments get a correction? What share of those do you think are wrong? Did either change after 2025-07-19?
6. **Clocks.** Has a 30-day corrected-BOL limit, a "180 days from shipment" clause or a closed-claim rule (ODFL 396) ever cost you a credit?
7. **Pass-through.** When the 3PL is the bill-to party, does the correction reach the shipper at cost or marked up? Who disputes it?
8. **Cost per dispute.** Hours per dispute, and the smallest correction worth disputing.
9. **Escalation.** Any use of NMFTA interpretations, NMFC arbitration or the STB? With what outcome?
10. **NMFC data.** How do 3PLs and TMS vendors license NMFC data for many customers? What did NMFTA require?

---

## 9. For the coordinator (not a call)

### 9.1 A desk reading of the S4 question

**"Will an LTL carrier grant a credit on evidence we produce, when the carrier holds the measurement record?"**

**1. We may file: yes.** The claimant can be the shipper "or its authorized agent" (49 CFR 378.2(f); NMFC 300510-A) (*verified*). Nothing in the nine tariffs bars an agent (*verified* by absence). Carriers must answer in writing within 60 days, citing tariff authority (*verified*).

**2. "Evidence we produce": mostly no, as written. Evidence we *collect from the shipper's own records*: yes, on the carriers' own terms.**
- The proof carriers name is shipper-origin, pre-existing paperwork: an invoice or packing slip plus a *pre-printed* spec sheet or catalog page (Estes, SEFL, TForce, *verified*).
- Or "conclusive documentary proof" judged at the carrier's satisfaction or "sole discretion" (ODFL, R+L, Saia, *verified*).
- No tariff names a scan, photo or third-party measurement as proof (*verified*). TForce expressly rejects re-typed BOLs.
- **[our call]:** the product cannot win by measuring after the fact (the freight is gone). It can win by:
  - (a) putting per-handling-unit weights and dimensions on the BOL at tender;
  - (b) keeping the spec-sheet and packing-slip pair ready for every SKU;
  - (c) pulling the carrier's certificate within days;
  - (d) filing a tariff-cited claim before the shortest clock.

**3. The dispute splits into two kinds, with different odds [our call]:**
- **"Wrong item or description" reclasses** are decided on documents and the NMFC text. They can be backed by an NMFTA interpretation ($50). Both sides can see the evidence, so outcomes can be measured.
- **"Disputed measurement" reweighs and remeasures** turn on the carrier's certificate against the shipper's origin records. The outcome is at carrier discretion. Escalation (arbitration, STB, court) costs far more than a $25-$350 correction.
  - The only public evidence on this kind is one-sided: the NH importer lost repeatedly despite a licensed scale (N-T35), and the regulator confirmed one pallet length was right (N-T32).
  - Carriers state they resolve disputes internally (N-T34).
- Carrier asymmetries reduce what is winnable on this kind: R+L's upward-only weight correction and ABF's reduction threshold (*verified*).

**4. "The real correction rate": still not documented.**
- The best new fact is FedEx Freight's own estimate: dimensioners on over 90% of shipments added over $150M over two fiscal years, about 0.8% of revenue **[our calc]**.
- That bounds the *dimensioner* part of corrections at one carrier. It says nothing about how many were wrong.
- **Only a savings assessment on real invoices, or the C21 interviews (§8 Q1, Q5), can give the rate.**

### 9.2 Where the documented position makes the saving measurable, and where not

| Part of the saving | Measurable? | Why | Label |
|---|---|---|---|
| Corrections billed (count, fee, re-rated amount) per shipment | **Yes** | Each correction carries a fee line ($15-$55) and usually a certificate. The PFC API standard codes RWE and RCL | *verified* (§3.1, §2.3) |
| Credits won | **Yes** | Credit memos; 378.8 written decisions "citing tariff authority" | *verified* |
| Corrections avoided by better BOLs (the prevention half) | **Yes, as a before-and-after correction rate per account** | Same data as row 1, over time | **[our call]** |
| Which corrections were wrong (the disputable pool) | **Not from carrier data** | Needs shipper-origin evidence the carrier judges at discretion; no neutral rate exists | **[our call]** on *verified* rules |
| Attribution of a credit to us | **Yes when we file** (claim number, 378.6); weak for the prevention half | — | **[our call]** |

### 9.3 Rows this evidence bears on (direction only, **[our call]**)

| Row | Current | Direction | Why |
|---|---|---|---|
| **F3** measurable in real time | 0.5 | **Hold at 0.5** | Up: corrections and credits are countable from carrier documents and APIs. Down: whether a correction was wrong rests on shipper-origin proof judged at carrier discretion. The two roughly cancel |
| **F4** predictable | 0.5 | **Hold, with a downward risk on size** | No neutral rate. Vendor frequency claims span 4-39% and are unusable. The one carrier-filed bound (about 0.8% of revenue from dimensioners at FedEx) suggests the reclass and reweigh part of the card's "2-5% avoidable" band may sit at or below its low end. Extra-service charges are a separate pool |
| **W3** whole product and time to value | 0.5 | **Hold; leans down** | The carrier record is per-carrier (nine portals or APIs), visible only to the bill-to party at least at ODFL, with dimensioner data kept 30 days under Handbook 44. For 3PL-booked shippers the 3PL gates the evidence. NMFC data costs $3.4-3.9k a year for an API, and multi-customer terms are unknown (§7) |
| **W6** time and resources to win | 0.5 | **Hold; leans down** | Every dispute races short clocks (30-day corrected BOLs, 180 days from shipment, closed-claim rules). Carriers keep discretion and add asymmetries. Carriers and NMFTA actively oppose outside standards (NCWM letters), and the state model law is still a draft (2026-07-14), so no regulatory tailwind is near |
| **K4** neutral correction rate | open | **Stays open** | New partial evidence (FedEx Form 10, the Saia call) is a size bound, not a correction-error rate |
| **The NMFTA dependency** (recorded single-point dependency) | — | **Undecided between cost and gate** | Scenario A is a cost ($3.9k a year); B is near a gate for small shippers (a seat is 41-417% of the per-shipper fee); C is a gate. Only NMFTA's licence terms decide which (§7) |

**One thing for the card's framing [our call]:** the documented position makes C-11 a **"capture evidence at origin, then file fast"** product more than a "dispute after the fact" product. The carriers' own proof rules reward documents that exist before pickup. Their windows and discretion punish late or improvised evidence.

---

## 10. Sources

**Existing IDs cited** (listed in their own files): N-R02 (NMFTA PFC API article), N-R03 (Docket 2026-1 PDF), N-G20, N-G21 (Docket 2025-1), N-R12 (WWEX Group), N-R18 (NASSTRAC), N-R22 (LTL tools), N-D30 (Cass), N-A26 (D'Arrigo audit rates), R35, R38.

**New sources.** All accessed on 2026-09-16.

| ID | Source | Date | URL | Access | What it gives |
|---|---|---|---|---|---|
| N-T01 | 49 U.S.C. 13710, LII (Cornell) | current | https://www.law.cornell.edu/uscode/text/49/13710 | full text download (*verified*) | (a)(1) copy of rules on request; (a)(3) 180-day rebill and contest rules |
| N-T02 | 49 U.S.C. 14705, LII | current | https://www.law.cornell.edu/uscode/text/49/14705 | full text download (*verified*) | 18-month limits; 6-month extension; accrual on delivery |
| N-T03 | 49 U.S.C. 14101, LII | current | https://www.law.cornell.edu/uscode/text/49/14101 | full text download (*verified*) | (b) written waiver of rights in contracts |
| N-T04 | 49 U.S.C. 14704, LII | current | https://www.law.cornell.edu/uscode/text/49/14704 | full text download (*verified*) | (b) overcharge liability tied to tariffs under 13702 |
| N-T05 | 49 CFR Part 378, eCFR renderer | current | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-49?part=378 | full text download (*verified*) | Claimant incl. agent; filing, documentation, 30-day acknowledgement, 60-day disposition with reasons |
| N-T06 | NMFTA, Supplement 1 to NMF 100-AS (Item 250100-A "FORMERLY ITEM 360"), copy hosted by a 3PL | issued 2019-03-28, eff. 2019-04-27 | https://cdn2.hubspot.net/hubfs/4849193/Supplement%201%20to%20NMFC%20-%20Effective%20April%2027%202019.pdf | PDF text extracted (*verified*; current wording not read) | Item 250100 Secs. 1(f), 2(c), 3, 4 |
| N-T07 | NMFTA, Supplement 1 to NMF 100-AO (Items 300160-A, 300500-A to 300530-A), copy hosted by a manufacturer | issued 2015-03-19, eff. 2015-04-18 | https://uscooler.com/blog/literature/NMF100AO-supplement1.pdf | PDF text extracted (*verified*; current wording not read) | NMFC billing-dispute procedure: 180 days, 30/60 days, agent claimant, arbitration |
| N-T08 | NMFTA, Item 250150 Uniform Straight Bill of Lading Terms and Conditions (NMF 100-AV) | 2022 | https://nmfta.org/wp-content/media/2022/10/Uniform_Bill_of_Lading_Terms_and_Conditions.pdf | PDF via fetch tool, text extracted (*verified*) | Sec. 7(a)-(d) liability for corrected charges; right to inspect |
| N-T09 | NMFTA, "2025 NMFC Changes – Frequently Asked Questions" | 2024 | https://nmfta.org/wp-content/media/2024/11/1106-FAQ_Doc-3.pdf | PDF via fetch tool, text extracted (*verified*) | Item 110 Sec. 8(d) quote; 13-sub scale; reclass-events answer; rule changes out of scope |
| N-T10 | NMFTA / FCDC, Docket 2025-2 | issued 2025-08-28; meeting 2025-09-29; eff. 2025-12-06 | https://nmfta.org/wp-content/media/2025/09/Docket-2025-2-1.pdf | PDF via fetch tool, text extracted (*verified*) | 17 subjects; Item 995 and Item 110 Sec. 20 proposals |
| N-T11 | NMFTA, Disposition Bulletin 1373 (Docket 2026-1) | 2026-03-20 | https://nmfta.org/wp-content/uploads/2026/04/Disposition-Bulletin-1373.pdf | PDF via fetch tool, text extracted (*verified*) | Subject 1 (Item 640) disapproved; outcomes of 22 subjects; effective 2026-05-23 |
| N-T12 | NMFTA, "Item (Rule) 640 Proposed Modification" (header: Docket 2026-1 Subject 1) | 2026-03 | https://nmfta.org/wp-content/media/2026/03/Item-Rule-640-Proposed-Modification.pdf | PDF via fetch tool, text extracted (*verified*) | Revised Item 640 text incl. "dimensions are not verified" note |
| N-T13 | NMFTA news, "NMFTA Opens Public Comment Period for Docket 2026-2" | 2026-08-28 | https://nmfta.org/news/nmfta-opens-public-comment-period-for-docket-2026-2-proposed-changes-to-nmfc-freight-classification/ | page extraction (*verified*) | About 33 proposals; comments by 2026-09-23; meeting 2026-09-29 |
| N-T14 | Snippets: NMFTA help centre "What are the updates to Item 250100?"; vmeasure.ai and shiptli.com on Docket 2026-2 Item 640 | 2025-26 | https://help.nmfta.org/hc/en-us/articles/44022688897051-NMFC-Changes-FAQ-What-are-the-updates-to-Item-250100 ; https://vmeasure.ai/handling-unit-density-freight-class-nmfc-2026-2/ ; https://shiptli.com/news/nmfta-proposes-changes-to-mixed-freight-classification-rules/ | snippet; help centre returned 403 (*assumed*) | "and/or Dimensions" added to Item 250100 Sec. 4; Item 640 on Docket 2026-2 |
| N-T15 | NMFTA news, "Unlocking LTL Precision: NMFTA's Interpretation Services" | 2025-09-03 | https://nmfta.org/news/unlocking-ltl-precision-nmftas-interpretation-services/ | page extraction (*verified*) | $50 / $225 prices; not legally binding; about 80% of requests from carriers |
| N-T16 | NMFTA DSDC, "Preliminary Freight Charges API Standard"; Transport Topics, "NMFTA Debuts Freight Charges API Standard" | page undated; article 2025-08-18 | https://dsdc.nmfta.org/apis/preliminary-freight-charges-api-standard ; https://www.ttnews.com/articles/nmfta-freight-standard | page extraction; DSDC *verified*, TT *assumed* | Events and reason codes (RWE, RCL); no adopters listed; Estes-led team |
| N-T17 | Old Dominion Freight Line, Tariff ODFL 100-Q (complete file) | eff. 2025-04-14; pages revised to 2026-07-22 | https://www.odfl.com/content/dam/odfl/us/en/documents/rates-and-tariffs/Complete%20ODFL%20100-Q%20Tariff.pdf | PDF download, text extracted (*verified*) | Items 162, 170, 360, 365, 367, 395, 396, 437, 490, 640, 995 |
| N-T18 | ODFL, "Document API Development Guide" v1.0 | last update 2026-06-04 | https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Document%20API%20Development%20Guide.pdf | PDF download (*verified*) | Document types (Inspection Certificate, Weight Certificate, photos); bill-to-party permissions |
| N-T19 | FedEx Freight, 100-Y Rules Tariff | eff. 2026-01-05; Item 438 revised 2026-06-01 | https://www.fedexfreight.com/content/dam/web/us/documents/fxf-100-series-rules-tariff.pdf | PDF download, text extracted (*verified*) | Items 191, 192, 435, 438, 640, 980, 981, 990 |
| N-T20 | XPO, Tariff CNWY 199-AK.1 (incl. BOL terms) | eff. 2026-02-16 | https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AK.1_Eff_02.16.2026.pdf | PDF download, text extracted (*verified*) | Items 23, 26, 28, 31, 205, 239; BOL terms para 9 |
| N-T21 | XPO LTL Help Center, "Document Finder" | undated | https://www.xpo.com/help-center/document-finder/ | page extraction (*verified*) | Document types incl. W&R photos, Inspection Report, NMFC Certificate; login |
| N-T22 | Estes Express Lines, EXLA 105 FF Rules Tariff | eff. 2026-01-02; items revised 2026-08-03 | https://www.estes-express.com/dA/ea677fdb-3bfa-45fb-9ef8-511174177f84/EstesRulesTariff.pdf | PDF download, text extracted (*verified*) | Items 170 (proof), 360-03, 645, 825, 992, 993, 993-10 |
| N-T23 | Estes, "Freight Shipping FAQs" | undated | https://www.estes-express.com/resources/frequently-asked-questions | page extraction; carrier claims (*assumed*) | W&R certificate tools; dimensioner scanning; discrepancy tool; 24-48 h |
| N-T24 | Saia, SAIA 170-D Rules Tariff | eff. 2025-10-01 | https://assets.ctfassets.net/kjv8gs2ccggb/3Y5vAsxznsXornATV1AG5D/ffe12c504b75b780d9462fa25f9f0329/Saia_170D_10012025.pdf | PDF download, text extracted (*verified*) | Items 360.10, 850, 1030, 1041 |
| N-T25 | ABF Freight (ArcBest), ABF 111-AU Rules Tariff | 2026-06-22 | https://arcb.com/sites/www/files/2026-06/ABF111-AU-06-22-2026-3.pdf | PDF download, text extracted (*verified*) | Items 420, 428, 991, 992 |
| N-T26 | R+L Carriers, Rules Tariff | updated 2026-09-07 (items eff. 2014-2025) | https://rl-cdn.com/docs/rlc/rules/rl-rules.pdf | PDF download, text extracted (*verified*) | Items 161, 169, 359, 364, 490, 640 exception, 991, 992 |
| N-T27 | R+L Carriers Developer, "Document Retrieval" API | undated | https://technology.rlcarriers.com/api-documentation/document-retrieval/ | page download (*verified*) | Document types incl. WeightCertificate, NmfcCertificate, DeliveryPhoto |
| N-T28 | TForce Freight, Tariff UPGF 102-T "Rules and Charges" | eff. 2026-03-16 | https://www.tforcefreight.com/downloads/UPGF-102-T-20260316.pdf | PDF download, text extracted (*verified*) | Items 171, 360, 361, 362, 365, 812, 813, 990 |
| N-T29 | TForce Freight, "Documents API Manual" | 2024-09-06 | https://www.tforcefreight.com/downloads/documents-API-User-Manual-V1.pdf | PDF download (*verified*) | Types WRC, REWE, CMC |
| N-T30 | Southeastern Freight Lines, SEFL 1090 Rules & Special Services Tariff | contents eff. 2026-06-01; Items 170 and 996 eff. 2025-12-01 | https://www.sefl.com/vsmisc/RT1090%20Full.pdf | PDF download, text extracted (*verified*) | Items 170 (proof), 202, 360-5, 996 (NTEP dimensioners, $15) |
| N-T31 | NIST Handbook 44 (2024), Section 5.58 Multiple Dimension Measuring Devices | 2024 | https://www.nist.gov/system/files/documents/2024/01/14/NIST%20HB%2044%202024%20Section%205.58%20Multiple%20Dimension%20Measuring%20Devices.pdf | PDF download (*verified*) | Scope (freight charges); customer information; 30-day retention |
| N-T32 | NCWM, OTH-24.1 "Uniform Shipment Law" file: NH Division of W&M presentation (submitted 2023-12-22); task-group changes (2025-01-07); "Full Report" (July 2025); 2026 interim presentation (2026-01-08); updated proposal DRAFT (2026-07-14); interim and annual archive pages (state regulator flag) | 2023-2026 | https://www.ncwm.com/interim-archive ; https://cdn.ncwm.com/userfiles/files/Meetings/Annual/Pub%2016%20Archive/2025/LR%20Supporting%20Files/Full%20Report%20on%20the%20Uniform%20Shipping%20Law%20Proposal%20%E2%80%93%20NCWM_25-7-8.pdf ; https://cdn.ncwm.com/userfiles/files/Exams/OTH-24_1_Updated%20Proposal-USL%20Task%20Group-2026-07-14.pdf ; https://cdn.ncwm.com/userfiles/files/Meetings/Interim/Pub%2015%20Archive/2024/OTH-24_1%20Uniform%20Shipping%20Law%20Presentation%20(Submitted%2012-22-23).pdf | PDF downloads, text extracted (*verified*) | Proposed certificate contents and 2-year retention; complaint findings; draft status; NIST Commerce Clause note |
| N-T33 | NMFTA letters to NCWM on OTH-24.1 (NMFTA flag) | 2024-06-28; 2025-02-11 | https://cdn.ncwm.com/userfiles/files/Meetings/Annual/Pub%2016%20Archive/2024/LR%20Supporting%20Files/OTH-24_1-NMFTA-Letter-2024-06-28.pdf ; https://cdn.ncwm.com/userfiles/files/Meetings/Annual/Pub%2016%20Archive/2025/LR%20Supporting%20Files/OTH-24_1-Letter-NMFTA-02-11-2025.pdf | PDF download (*verified*) | Carriers' position: preemption; internal dispute resolution; interpretations; contracts; intermediaries |
| N-T34 | Carrier letters to NCWM on OTH-24.1: XPO (2025-07-02), ABF Freight (2025-10-24, scanned), Lynden Transport (2024-07-17) | 2024-2025 | https://cdn.ncwm.com/userfiles/files/Meetings/Interim/Pub%2015%20Archive/2025/LR%20Supporting%20Docs/OTH-24_1-Letter-XPO-25-07-02.pdf ; https://cdn.ncwm.com/userfiles/files/Meetings/Interim/Pub%2015%20Archive/2026/L%26R%20Supporting%20Documents/OTH-24_1-Letter-ABF%20Freight-25-10-24.pdf ; https://cdn.ncwm.com/userfiles/files/Meetings/Annual/Pub%2016%20Archive/2024/LR%20Supporting%20Files/OTH-24_1-Lynden%20Transport%20Letter-2024-07-17.pdf | PDF download; ABF read as page images (*verified*) | W&R programmes; ABF inspection photos, report, 31 inspectors, internal resolution; Lynden no STB or court cases |
| N-T35 | Letter to NCWM from a small New Hampshire importer (Heatlines LLC), scanned | 2025-01-10 | https://cdn.ncwm.com/userfiles/files/Meetings/Interim/Pub%2015%20Archive/2025/LR%20Supporting%20Docs/OTH-24_1-Letter-Heatlines%20LLC-01-10-2025.pdf | pages 1-2 read as images (*verified* as text; one party's account) | Fee frequency and size; months per dispute; evidence rejected; 3PL disinterest |
| N-T36 | FedEx Freight Holding Company: Form 10 (10-12B/A, Ex. 99.1) and Form 10-K FY2026 (SEC) | 2026-04-10; 2026-08-05 | https://www.sec.gov/Archives/edgar/data/2082247/000110465926041977/tm2520565d10_ex99-1.htm ; https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/fdxf-20260531.htm | HTML download, text searched (*verified*) | DIM on over 90% of shipments; over $150M added revenue FY2024-25; revenue $9,424M / $8,892M / $8,795M; revenue-adjustment allowance |
| N-T37 | Saia Q2 2025 earnings call transcript, 8-K Ex. 99.1 (SEC) | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1177702/000095017025100954/saia-ex99_1.htm | HTML download (*verified*) | "we dimension 75 percent of our freight every day" |
| N-T38 | ArcBest Q1 2025 earnings presentation, 8-K Ex. 99.3; ArcBest 10-K FY2025 (SEC) | 2025-04-29; 2026-02-25 | https://www.sec.gov/Archives/edgar/data/894405/000155837025005733/arcb-20250429xex99d3.htm ; https://www.sec.gov/Archives/edgar/data/894405/000110465926019699/arcb-20251231x10k.htm | HTML download (*verified*) | Vaux Vision NTEP-certified dimensions and photos; no rates |
| N-T39 | SEC EDGAR full-text search queries (efts.sec.gov) | run 2026-09-16 | https://efts.sec.gov/LATEST/search-index?q=%22dimensioners%22 (and 9 other queries, §5.3) | API JSON (*verified* as search results) | Which filers mention the terms; no correction rates |
| N-T40 | DOJ, "Freight Carriers Agree To Pay $6.85 Million To Resolve Allegations …" | 2022-03 | https://www.justice.gov/usao-wdny/pr/freight-carriers-agree-pay-685-million-resolve-allegations-knowingly-presenting-false | snippet; page returned a bot page (*assumed*) | Settlement amount; reweigh allegations 2005-2013 |
| N-T41 | NMFTA ClassIT+: pricing page; "Frequently Asked Questions (FAQs) ClassIT" PDF; API product page | pricing current; FAQ 2025-01-06 | https://classitplus.nmfta.org/pricing ; https://nmfta.org/wp-content/media/2025/01/ClassITFAQ_1.6.2025.pdf ; https://classitplus.nmfta.org/products/api | pricing HTML download (*verified*); FAQ PDF text (*verified*); API page extraction (*verified*); bundle 30% snippet (*assumed*) | Seat and API prices; no free or monthly plan; no concurrent logins; licence agreement; no TMS details; "voluntary standard" |
| N-T42 | NMFTA terms of use; terms of sale; "Integrating NMFC Data into Your TMS" | article 2026-02-17 | https://nmfta.org/terms-of-use/ ; https://nmfta.org/terms-of-sale/ ; https://nmfta.org/integrating-nmfc-data-into-your-tms-what-every-developer-should-know/ | page extraction (*verified*) | General content restrictions; no data-licence scope published |
| N-T43 | SMC3 Insider Blog, "Weighing and Inspection Process – How to Navigate It and Prevent Issues" (SMC3 flag) | 2023-08-23 | https://smc3blog.com/weighing-and-inspection-process-how-to-navigate-it-and-prevent-issues/ | page extraction; figures *assumed* | 70-80% of freight inspected by dimensioners; dispute evidence |
| N-T44 | TranzAct blog, "What's Up With Your Weight (and Inspection) Issues!" | 2019-06-12 | https://blog.tranzact.com/2-minute-warning/whats-up-with-your-weight-and-inspection-issues | page extraction; vendor (*assumed*) | "39%" weight discrepancies (unnamed carrier CEO) |
| N-T45 | AFS Logistics, white paper "How did LTL rules tariffs and accessorial charges get so complicated?" | 2024-07 | https://scg-lm.s3.amazonaws.com/pdfs/afs-logistics-wp-ltl-072424.pdf | PDF download; vendor (*assumed*) | Accessorials 8.7% of LTL spend (2023); reclass case of $70,000 |
| N-T46 | Vendor and broker dispute guides: FreightPros ("How to Dispute a Reclass", 2014); Warp (undated); MyFreightWorld (2025-02-17); Eniture (2021-02-23); Worldwide Express (2022-06-28); Unishippers disputes guide (landing page); Lighthouz LTL page | 2014-2026 | https://www.freightpros.com/whitepaper/dispute-reclass/ ; https://www.wearewarp.com/avoid-ltl-reclass-reweigh-fees ; https://www.myfreightworld.com/can-you-fight-freight-reclassification-fees/ ; https://blog.eniture.com/what-to-do-when-your-ltl-freight-shipment-is-reclassed ; https://www.wwex.com/shipping-resources/freight-reclassification ; https://www.unishippers.com/shipping-resources/freight-resources/guide-to-dealing-with-freight-shipping-disputes ; https://lighthouz.ai/shipment-types/ltl | page extraction; vendor (*assumed*) | Evidence advice; timelines; frequency claims; no win rates |
| N-T47 | Transport Topics, "LTL carriers urge more shipper education on NMFC changes" | 2026-08-14 | https://www.ttnews.com/articles/ltl-carriers-nmfc-changes | page extraction; trade press (*assumed*) | FedEx 150-day enforcement delay; Dayton Freight dimensioners; carrier quotes |
| N-T48 | PARCEL Industry (B. Primus, JD), "Revisions to the NMFC Which Shippers Need to Know — and then Avoid" | 2015-10-26 | https://parcelindustry.com/article-4466-Revisions-to-the-NMFC-Which-Shippers-Need-to-Know---and-then-Avoid.html | page extraction; secondary (*assumed*) | Commentary on NMFC arbitration items; "get a contract" |
| N-T49 | Pitt Ohio, rules item 1014 "Determination of Freight Classes for Rating Purposes" | undated | https://pittohio.com/myPittOhio/RulesTariff/1014 | page download (*verified*) | Still cites "item 360, section 2"; "class change certifications as support" |
| N-T50 | Search snippets on reclass frequency and carrier document tools (15% of shipments; 4-6% disputes and 70-82% recovery; ABF "weight confirmations"; SEFL W&I glossary) | 2025-26 | https://support.arcb.com/en/articles/1509576-document-retrieval ; https://www.sefl.com/seflWebsite/servlet?action=TRANSPORTATIONGLOSSARY_GETGLOSSARY ; (frequency snippets: source pages not traced) | snippet (*assumed*) | Untraceable vendor rates; ABF and SEFL document hints |

---

## 11. Could not access, or not found

**Blocked or unusable:**
- **help.nmfta.org** (the NMFTA help centre): HTTP 403 (a Cloudflare challenge) for the Item 250100 update FAQ, the ClassIT+ API FAQs and the ClassIT+ pricing FAQ. The Item 250100 change is therefore a snippet only (N-T14).
- **nmfta.org PDFs** blocked command-line downloads (403). They were fetched through the web-fetch tool and their text extracted locally (N-T08 to N-T12).
- **The current NMFC text** of Items 110, 170, 250100 and 300500-300530 is licensed and was not read. The quotes are from the 2015, 2019 and 2022 NMFC supplements and from NMFTA's FAQ (N-T06 to N-T09). Wording may have changed since.
- **Docket 2026-2 PDF:** not found by search. Only NMFTA's announcement was read (N-T13).
- **Disposition bulletin for Docket 2025-2:** not read, so the outcome of the Item 995 proposal is unknown.
- **DOJ press release on the YRC settlement:** returned a bot page. Snippet only (N-T40).
- **Saia rules web pages** (saiasecure.com item pages): HTTP 404. The PDF tariff was used instead (N-T24).
- **XPO tariff library page:** HTTP 404. A search found no version later than AK.1.
- **Scanned letters:** OCR was not available (no English language data for tesseract). The ABF and Heatlines letters were read as page images instead. Heatlines page 3 was not read.
- **Unishippers dispute e-guide:** behind a download form, not submitted (rule: no sign-ups).

**Searched, not found:**
- **Neutral correction or win rates:** see §5.3 (EDGAR, NMFTA, ATRI, GAO and STB, academic, NCWM, trade press).
- **Document access for shippers at FedEx Freight, Saia and SEFL:** portal or API document-type lists were not found. FedEx's tariff promises a copy on request.
- **Whether states enforce Handbook 44 §5.58 on LTL terminal dimensioners:** not searched state by state. The NH importer says rules differ by state (N-T35, one party's view).
- **PFC API adopters:** none named in NMFTA or trade-press pages.
- **ClassIT+ licence agreement text, and any software-vendor, partner or reseller terms:** not public. Contacting NMFTA is outside this check's rules (§7).
- **NASSTRAC or SMC3 published dispute-success figures:** none found. A NASSTRAC guide on reclass disputes was not found.
- **An estimate of how much small-shipper LTL moves on 3PL contracts rather than carrier tariffs:** not found. It matters for which windows apply (§3.2 note).
- **STB decisions under 13710(a)(3) on reweighs or reclasses:** none found in a site-limited search.
