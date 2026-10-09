# S5 practice audit: a look-back run on public court invoices (C-09)

- **What this is:** a rehearsal of the C-09 savings assessment (`selection_runs/run-01/5_interview_kit.md` §6.1) on **real freight invoices that are public in court records**, found by check AC. It was run on 2026-09-17 at the founders' request, before any customer interview.
- **Why:** to test the method, time the work, produce a worked example to show interviewees, and see how far an audit gets **without** the shipper's own rate agreement.
- **What it cannot do:** it cannot measure our segment's overcharge rate. These shippers are not our customers, only one of the two sets has its pricing agreement attached, and a court exhibit is a selected pile, not a normal month.
- **Status: it decides nothing.** Readings are **[our call]**.
- **Labels:** *verified* = read or computed from the source document; *assumed* = a secondary claim; **[our calc]** = our arithmetic; **[our call]** = judgement.
- **Files:** the PDFs were downloaded to a scratch folder, not into this project. They are public at the URLs in §7.

**Words used here:**
- **PRO / freight bill number:** the carrier's shipment ID, and the invoice number.
- **Linehaul:** the base transport charge before discounts, fuel and extras.
- **Discount:** the negotiated percentage off the carrier's base rates.
- **AMC (absolute minimum charge):** the floor below which a bill cannot fall, whatever the discount works out to.
- **Deficit weight rating:** billing a light shipment as if it weighed the next weight break, when that is cheaper for the shipper.
- **FSC (fuel surcharge):** a percentage tied to a published diesel index.
- **Accessorial:** an extra-service charge (lumper, liftgate, detention, residential and so on).
- **FAK ("freight all kinds"):** an agreed class used in place of the published NMFC class.
- **W&R certificate:** the weight-and-research document a carrier issues when it re-weighs a shipment.

---

## 1. The data

| Set | What it is | Size | Agreement attached? |
|---|---|---|---|
| **ABF Freight (ArcBest)** invoices filed in a supplement maker's bankruptcy, as an exhibit to the debtors' objection to ArcBest's claim | 107 pages = **101 distinct freight bills**, shipped **9 May to 9 Aug 2024**, billed to the shipper's 3PL | **$45,652.49** | **No** |
| **Southeastern Freight Lines (SEFL)** bills filed with a clothing maker's overbilling complaint, with that shipper's **pricing agreement in three dated versions** and its own overcharge worksheet | 224 pages; about 75 bills, 2020-2023; worksheet of 3,645 invoices | claim $271,828.70 | **Yes** |

Both were downloaded from CourtListener (free). The ABF pages carry a machine text layer, so they parse cleanly; the SEFL pages are scans with OCR errors, so only pattern-level checks were run on them.

**One number worth keeping.** The ABF set averages **$452 a bill**, which is **2.21 invoices per $1,000 of freight spend** [our calc]. Check AA's cost model used 1.5 as its central figure and 2.1 as its LTL-heavy case, from Saia's $347.81 average LTL shipment. This real account sits at the LTL-heavy end, where an audit costs the most per dollar of fee.

---

## 2. Method

1. Download the PDF; extract the text layer (`pdftotext -layout`).
2. Split into pages; key each page by freight bill number; count repeated pages.
3. Parse each bill's charge column: every line that ends in an amount, with its charge code (linehaul, deficit weight, discount, AMC, fuel, and each accessorial).
4. **Check 1, does the bill add up:** sum the charge column and compare with "AMOUNT DUE".
5. **Check 2, discount:** is the same percentage applied on every bill, and to the right base?
6. **Check 3, minimum charge:** where an AMC adjustment appears, what net does it produce?
7. **Check 4, fuel base:** is fuel charged on net linehaul only, or also on accessorials?
8. **Check 5, fuel level:** map each shipment date to the diesel index published that week (EIA weekly series), look the index up in the carrier's **published** fuel table, and compare with the percentage billed.
9. **Check 6, accessorials:** count and total every extra charge, and mark which need a document to justify.
10. **Check 7, duplicates:** same PRO twice; same bill-of-lading and amount; same consignee, date and amount.
11. **Check 8, corrections:** reweighs, restored weights and corrected invoices.

Checks 1-4 and 6-8 need only the invoices. Check 5 needs the carrier's public tariff plus a public price index. **Everything else an audit would want needs the shipper's own documents.**

---

## 3. What the checks found (ABF, 101 bills, $45,652.49)

| # | Check | Result | Reading **[our call]** |
|---|---|---|---|
| 1 | **Does each bill add up?** | **101 of 101.** The script reconciled 99 to the cent; the other 2 were parser artifacts (a "READY 1.00 PM" time read as money; a page holding two bills) and both add up by hand | Carrier arithmetic is not where the money is. Any audit that finds "math errors" here would be finding its own parsing errors |
| 2 | **Discount** | **89.5% on all 101 bills**, applied to linehaul plus deficit-weight charges, never to accessorials | Internally consistent. **Whether 89.5% is the agreed figure cannot be checked without the agreement** |
| 3 | **Minimum charge** | 43 bills carry an AMC adjustment; on **38 of them the net linehaul is exactly $180.00** | **38% of this account's bills sit on the floor.** On those, the discount is irrelevant: only the AMC figure, the accessorials and fuel move the bill |
| 4 | **Fuel base** | Fuel = the printed percentage × net linehaul on **99 of 99** parsable bills; never on accessorials, and correctly on the AMC-adjusted net | Matches the contract language check AC found in a different carrier's contract. **No error found** |
| 5 | **Fuel level** | Billed 30.3-31.5% across 14 shipment dates. Against **ABF's published table** (Item 161) and the **EIA weekly diesel index**, the billed percentage runs **1.3-1.5 points below** the table every week: the implied index is 15-19¢ below the actual index, consistently | A **consistent** gap, in the shipper's favour, so it reads as either a negotiated fuel schedule or an older table version, **not** an error. **It cannot be settled without the 2024 table or the customer's agreement** |
| 6 | **Accessorials** | **$5,939.28, or 13.0% of everything billed**: California compliance $22.00 on all 101 bills ($2,222.00); lumper on 33 bills ($1,882.26); New York island delivery 5 ($500.00); high-cost delivery 5 ($330.00); sort and segregate 3 ($413.89); remote location 2 ($130.00); **detention 2 ($85.07)**; non-business-hours delivery 1 ($132.38); marking and tagging 1 ($107.00); limited-access delivery 1 ($180.00) | This is where a real audit would work. Every one needs either the agreement (is the price right? is the charge allowed?) or proof (was the service performed?) |
| 7 | **Duplicates** | 6 pages are the same bill filed twice — an exhibit artifact, not a double billing. **No true duplicate found.** Three bills share a date and an amount, and two more pairs do, but all have different consignees and bills of lading | **A warning for the real audit:** on an account where 38% of bills land on the same $180 floor and carry the same $22 surcharge, "same amount, same day" produces false duplicates. The test has to key on PRO plus bill-of-lading |
| 8 | **Corrections** | **26 bills carry "See W&R certificate"** (a reweigh), and **9 of those also say "restore original weight"**. Those 26 bills total **$12,265.03, 27% of the billed dollars**. 4 bills are corrected invoices. Detention appears on 2 bills **with no arrival or departure times printed** | The reweighs are the biggest flagged pool, and **not one of them can be resolved from the invoice**: it needs the original bill-of-lading weight and the carrier's certificate |

### 3.1 What the audit could and could not conclude

- **Recoverable dollars proven from public documents alone: $0.**
- **Dollars carrying at least one line that needs a document we don't have: $27,710.64 on 59 of 101 bills, 61% of everything billed** [our calc].
- The largest flagged pools are the reweighs ($12,265.03 of bills affected), the lumper charges ($1,882.26, which need a receipt and an authorisation) and the accessorials priced by an agreement we can't see.

**The blunt lesson:** an audit without the customer's rate agreement, fuel schedule, bills of lading and weight certificates can only check arithmetic and internal consistency, and those are exactly the things carriers' systems already get right. **The money is in the documents the customer has to hand over**, which is why the assessment (and the NDA that precedes it) is the gate.

### 3.2 A worked example to show interviewees

**ABF freight bill 150235531**, shipped 1 July 2024, 2 pallets, 1,837 lb, rated at exception class 70 against NMFC class 100:

| Line | Amount | Check |
|---|---|---|
| Linehaul, 18.37 cwt × $348.19 | $6,396.25 | 18.37 × 348.19 = 6,396.25 ✓ |
| Deficit weight, rated up to 2,000 lb | $567.55 | 1.63 × 348.19 = 567.55 ✓ (in the shipper's favour) |
| Discount 89.5% | −$6,232.60 | 89.5% × 6,963.80 ✓ |
| California compliance surcharge | $22.00 | needs the agreement |
| Lumper (unloading) | $149.10 | needs a receipt; the bill also promises a $11.02 refund allowance to the consignee |
| Fuel surcharge 30.3% | $221.55 | 30.3% × $731.20 net linehaul ✓, not charged on the extras |
| Dynamic discount | −$181.83 | a carrier programme; it appears in no public document |
| **Total** | **$942.02** | column sums exactly ✓ |
| Note on the bill | "W02/AUTH:Reweigh - See W&R certificate for details" | **unresolvable without the certificate and the original BOL weight** |

---

## 4. The SEFL set: what having the agreement changes

The SEFL exhibit is the only public set with bills **and** the pricing agreement they should follow. Even at OCR level, the bills show:

| What the bills show | Count in the OCR text | Why it matters |
|---|---|---|
| Four different discounts: **90.30%, 88.15%, 87.45%, 81.00%** | 9 / 6 / 5 / 1 lines | The agreement sets different discounts by lane type (direct to direct, direct to partnership, and so on) and has **three versions with effective dates**. Matching each bill to the right version and lane is the actual audit work |
| Two liftgate prices: **$55.00** and **$30.00** | 32 / 9 lines | The agreement's accessorial table gives $55 "direct to partnership" |
| Classes **70** and **150** on the same account | mixed | The agreement's FAK is 70 for classes 77.5-175, so a bill rated 150 is either outside the FAK or a candidate error |
| Fuel percentages from **21.50% to 36.00%** | 10+ values | Fuel moves weekly; the table version in force matters |

**Reading [our call]:** this is the shape of a real audit. The work is not arithmetic; it is **matching each bill to the right version of the right agreement**, then pricing the difference. Check AC's caution stands: the plaintiff's own worksheet claims 22-25% of base freight while ignoring a rate-increase clause and pallet exclusions in its own agreement, which is how a careless look-back overstates recoveries and loses credibility with a carrier.

---

## 5. Timings, and what they mean for the cost model

| Step | Effort here | Note |
|---|---|---|
| Find, download, extract 107 pages | minutes | Free, from a public docket |
| Write and debug the parser | about 6 iterations of work | One-off per invoice format. **Format-specific:** the SEFL scans need a different approach |
| Run all 8 checks over 101 bills | about 2 seconds of compute | Once written, the marginal cost per bill is machine-only |
| Resolve the exceptions | **not possible here** | 59 of 101 bills carry a line needing a document nobody outside the shipper has |

**What this says about check AA's cost model [our call]:**
- The **machine** side is confirmed cheap: parsing and checking 101 bills costs seconds and a fraction of a cent.
- The **human** side looks under-modelled. Check AA assumed a person looks at **15%** of packets. On this account, **58% of bills carry a line that needs a document or a judgement**. Even if loading the agreement clears the priced accessorials automatically, the reweighs (26%) and the proof-of-service extras stay manual.
- **2.21 invoices per $1,000 of spend** on this LTL-heavy account, against the model's 1.5 central, raises cost per dollar of fee by about half.
- Both push the same way: **an LTL-heavy small shipper is the most expensive kind of customer to serve**, which is the opposite of where the pain is easiest to find.

---

## 6. What to carry into the interviews and the assessment

1. **Ask for the agreement first, and every version with its effective dates.** Without it, an audit can only confirm the carrier's arithmetic.
2. **Ask specifically for the fuel schedule in force**, not just "the contract". Public tariff tables are re-issued, and negotiated fuel programmes are common: this account was billed 1.3-1.5 points below ABF's published table all summer.
3. **Ask how many bills land on the minimum charge.** On this account it was 38%. Those bills are nearly immune to a rate audit and cheap to check, which changes the economics of an account.
4. **Ask for weight certificates and original BOL weights** up front. Reweighs were 26% of bills and 27% of dollars here, and they are the single biggest flagged pool.
5. **Ask what proof exists for lumper, sort, detention and other services.** Detention was billed twice with no times on the bill.
6. **Use the worked example in §3.2 as the show-and-tell.** It is a real bill, it is public, and it walks through exactly what an audit does.
7. **Warn about naive duplicate tests.** Minimum-charge accounts generate identical amounts on the same day for different shipments.

---

## 7. Sources

| ID | Source | URL | Access | What was used |
|---|---|---|---|---|
| N-PA01 | *In re IN Holdings, Inc.*, Bankr. C.D. Cal. 1:24-bk-11323, Doc 920, Exhibit 2: 107 pages of ABF Freight invoices | https://storage.courtlistener.com/recap/gov.uscourts.cacb.1993985/gov.uscourts.cacb.1993985.920.0_1.pdf | full (text layer, parsed) | All 101 bills; every check in §3 |
| N-PA02 | *Exist, Inc. v. Southeastern Freight Lines*, S.D. Fla. 1:26-cv-20049, Doc 1-2: SEFL bills, pricing agreement versions, shipper worksheets | https://storage.courtlistener.com/recap/gov.uscourts.flsd.704429/gov.uscourts.flsd.704429.1.2_3.pdf | full (OCR) | §4 pattern checks |
| N-PA03 | ABF Freight, **ABF 111-AS Rules and Special Service Charges**, Item 161 "Computation and application of fuel surcharge", effective 2025-02-03 | https://arcb.com/sites/www/files/2025-01/ABF111-AS-02-03-2025.pdf | full (350 index bands parsed) | Check 5 |
| N-PA04 | EIA, **Weekly U.S. No 2 Diesel Retail Prices**, series EMD_EPD2D_PTE_NUS_DPG | https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2D_PTE_NUS_DPGw.xls | full (data file) | Check 5 |
| — | Earlier checks used here | `s5_check_AC_c09_example_invoices.md` (which found the court sets), `s5_check_AA_c09_cost_to_serve.md` (the cost model), `s5_check_T_ltl_carrier_position.md` (claim windows) | — | — |

## 8. Limits

- **One shipper, one carrier, three months, and a pile chosen for a court fight.** Nothing here is a rate for any population.
- The ABF account is billed **through a 3PL**, so it may not price like a direct account.
- The fuel comparison uses the **2025** version of ABF's table against **2024** shipments, because the 2024 version is not public. That is why the gap is read as a table-version or negotiated-schedule difference rather than an error.
- The SEFL findings are from OCR text at pattern level; individual bills were not re-rated line by line.
- No conclusion about our segment's overcharge rate can be drawn from any of it (H09-02 stands untested).
