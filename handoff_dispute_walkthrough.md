# Hand-off: walk a real freight dispute through our method, and check it against what really happened

Written 2026-10-20 for a fresh Claude Code session. The founder will run this session with you. Read this whole file first, then the files in "Read first", then start.

## 1. The goal

The project has a method for finding disputes on freight bills. It lists every fact a dispute needs, where each fact lives, what to do when a fact is missing, which clock applies, and the verdict per bill line. The method was built from public documents and validated cell by cell (checks AZ, BA, BB, BC, 2026-10-18), but it has never been run end to end on a dispute whose real outcome we know and then compared with that outcome.

Your job: **walk the founder through one real dispute, stage by stage, using only the method, reach a verdict, and then compare it with what actually happened.** Where the method and reality agree, say so. Where they disagree, find out why: a missing fact, a wrong place to look, a wrong precedence, a wrong NOT REPORTED rule, a wrong clock, or a case the method does not cover. The deliverable is the comparison and a list of proposed changes. **You do not change the method yourself**: the founders decide (§7).

## 2. Who you are working with

The founders are building their first vertical SaaS and are new to freight. Explain in plain language, with the real numbers from the documents, one stage at a time. Define each freight term the first time you use it (PRO = the carrier's bill number; BOL = bill of lading; TONU = truck ordered, not used; and so on). C-09 is a **software company**: the software flags lines and the customer's own staff review them and file the disputes. We employ no analysts (decision D-23), so the method's output is what a reviewer at the customer would see.

## 3. Read first

- `data/doc-exploration.md`: the method, fact by fact. **§1** the 88 facts (IDs P01-P22 price terms, F01-F29 shipment facts, M01-M27 money facts, D01-D10 dispute facts); **§2** where each fact lives (primary → fallbacks → never use → who holds it if nothing does); **§2.5** the keys that link documents; **§3** which copy wins when two disagree; **§4** what NOT REPORTED means, the windows and the decision table (§4.6); **§9.7** the founders' decisions of 2026-10-20. **Do not read §5.4 if you run Case 2** (it holds Case 2's answers).
- `data/doc-explanation.md` §4: the seven-stage pipeline (bill facts → shipment facts → price terms → expected charge → compare → trigger test → clock and verdict), with the verdict rules in §4.7.
- `data/README.md` and `data/catalogue.csv`: what is in `data/` and where.
- `CLAUDE.md`: the project's rules and the Work Log.

The founders' decisions you must apply (2026-10-20, recorded in `data/doc-exploration.md` §9.7):
1. **A carrier-added charge whose supporting record is missing** (no certificate behind a reweigh, no reason for a change) is **flagged in its own bucket**, "unsupported change, carrier's record requested", counted apart from other flags.
2. **The 180-day clock starts at the date the customer received the bill**; if that date is unknown, the bill date is the fallback. Aim to file inside the earliest window that applies. Windows are not always enforced, so a line up to **10 days past** the deadline is still shown, as "late: file now, may be refused".
3. **Tolerance, for now: any difference, so long as the carrier owes money.** A line billed above the expected amount is flagged, by any amount; a line billed below it is not.

## 4. The case

### Case 1 (run this first): Yellow claim 16200, a $60 TONU charge

File: `data/sources/23_overcharge_claims_vs_yellow/yrc_globaltranz_16200__claim.pdf` (catalogue row 23-002; text in `data/derived/text/23_overcharge_claims_vs_yellow/yrc_globaltranz_16200__claim.txt`). Five pages: a bankruptcy proof-of-claim form (pp. 1-3), the claimant's letter (p. 4) and the BOL (p. 5). A 3PL (GlobalTranz) disputed a $60 TONU charge that Yellow (YRC) billed on PRO 7047922705. The shipment moved in June 2023.

Why this case: it is a real dispute between a shipper's agent and a carrier, about whether a charge should apply at all (a trigger question); it has a stated outcome; and none of the earlier walks used it. It is also thin: no carrier bill, no pickup request and no Yellow tariff are held. That is part of the test, because the method has to say what is missing, who holds it, and whether the dispute can still be decided.

**The outcome is stated in the same letter (p. 4).** Before you use the outcome sentences, write down the verdict the method gives from the facts alone, and show it to the founder. Then read the outcome and compare.

### Case 2 (optional, only if the founder wants a second run): ODFL's Winn-Dixie shipment, run blind

File: `data/sources/21_ltl_bills_and_corrections/winndixie_flmb715964__6929.0.pdf` (catalogue row 21-002; scanned, no text layer, so render pages with `pdftoppm -f N -l N -r 150 -png <pdf> <out>` and read them as images). A shipment billed collect to the consignee at class 250, disputed, then corrected. **Inputs:** pp. 6-12 (BOL, the consignee's debit memo, its statement and check stub, the carrier's e-mails and fax covers). **The outcome:** pp. 1-3 and 13-17 (the bankruptcy objection, the carrier's accounts-receivable history and the re-bill). Do not open the outcome pages, `data/doc-exploration.md` §5.4, or the research files that discuss this chain until your verdict is written down. The consignee's first payment was $2,412.67 by card on 1/27/05 (an input you would otherwise only find in the outcome pages).

## 5. How to run it

Work in this order, and after each stage give the founder a short plain-language summary with the real values.

1. **The question.** What was billed, what is disputed, and what kind of dispute it is: a price difference or a trigger difference (`data/doc-exploration.md` §0, last paragraph). Name the audit check(s) by code (A1-G2, from `research/s5_check_AK_c09_audit_workflow_and_products.md` §3.2).
2. **The facts.** List every fact ID the disputed line needs (§1's Checks column). For each, follow §2's row in order: primary, then each fallback, then the "never use" list, then "if none". Record a table:

   | ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by (shipper / carrier / nobody / customer's files, §4.1) |

   Use §2.5's keys to tie documents together. Where two documents disagree, apply §3.1 and say which copy wins and why.
3. **The price terms.** Which rule or tariff item prices or triggers the charge, in the edition in force on the ship date (§4, opening paragraph). If it is not held, say so, say who must supply it (the carrier, on request: 49 U.S.C. 13710(a)(1)), and say what the method can still check without it.
4. **Expected against billed.** The expected amount, or "not checkable" with the missing input named. Apply the tolerance rule (§3 above).
5. **The trigger test.** Does the fact that makes the charge apply hold? Who owed that fact, and what does §4.2 or §4.3 say when it is missing or contradicted?
6. **The clocks.** Every window that applies (§4.4), from the receipt date if known, else the bill date; the earliest deadline; whether the dispute was inside it, inside the 10-day buffer, or late. Show the dates and the arithmetic.
7. **The verdict.** One of: flag; flag in the "unsupported change, carrier's record requested" bucket; ask the reviewer; not checkable; matches (`data/doc-exploration.md` §4.6, `data/doc-explanation.md` §4.7). Add the reviewer's view: the dollars at stake, the deadline, the proof, and what to request from whom. **Show this to the founder before reading the outcome.**
8. **The real outcome.** What actually happened, quoted from the file, with the page. Who decided, on what basis, and whether money moved.
9. **The comparison.** A table:

   | Decision point | What the method said | What happened | Agree? | If not, why |

   Decision points include at least: is there a dispute; who owed the deciding fact; where the deciding fact lived; the verdict; the clock; the next action (short-pay, claim, refund request), and whether the payment state changed what could be done.
10. **What to change.** For each disagreement or gap: the section and row of `data/doc-exploration.md` (or `data/doc-explanation.md` §4) it touches, the proposed wording, and the evidence. Also list what the case confirmed.

Arithmetic in `python3 -I`, never by eye. Every value carries its page. A derived value is labelled derived, with its formula.

## 6. What to write

One file: `research/s5_check_BD_c09_dispute_walkthrough.md`, written section by section as you go so nothing is lost if the session is cut. Sections:
- §0 the result in five lines: did the method reach the real outcome, and the main gaps;
- §1 the case and the documents (file ids, pages);
- §2 the fact table (step 2);
- §3 price terms, expected against billed, the trigger test (steps 3-5);
- §4 the clocks (step 6);
- §5 the verdict as the reviewer would see it (step 7);
- §6 the real outcome (step 8);
- §7 the comparison (step 9);
- §8 proposed changes, each with the section it touches and the evidence (step 10);
- §9 what the case confirmed;
- §10 claim ledger: every number or quotation used, with file id, page and a *verified* (re-opened at the source) or *assumed* tag.

Repeat for Case 2 in the same file, as §11 onward, if it is run.

## 7. Rules

- **`data/` is read-only.** Do not edit `data/doc-exploration.md`, `data/doc-explanation.md` or anything else in `data/`. Propose changes in §8 of your file. The founders decide what is applied (`CLAUDE.md`: never finalize a decision for them; present the evidence for and against).
- **Companies only.** The source files are public court and bankruptcy records and carry individuals' names, signatures, e-mail addresses and phone numbers (the Case 1 letter names a carrier employee). Never copy a person's name, e-mail address or phone number into any project file or into chat; write "a Yellow employee", "the claimant's agent".
- **Work offline** on `data/` and `research/`. If a public legal text is truly needed, ask the founder first; if you then fetch it, never put the user's e-mail address in a request header, URL or payload.
- **No sub-agents** unless the founder asks. One adversarial reviewer may be added at the end if the founder wants the comparison checked; it must re-open every citation and may not object without a re-opened file or a recomputed number.
- **Do not commit.** The founders commit (git: `main`, no branches).
- When done, add one line to the Work Log in `CLAUDE.md` (dated, newest at the bottom, with a link to your file), and add your file to the Documents list, as the existing entries do. Do not touch the Answers block.
