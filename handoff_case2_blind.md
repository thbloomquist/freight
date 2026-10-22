# Hand-off: walk Case 2 through the dispute method, blind, then check it against what happened

Written 2026-10-20 for a fresh Claude Code session **started in this folder** (`~/Documents/personal/bio/freight_case2_blind/`). A founder will run the session with you. Read this whole file first, then the three files in `method/`, then start.

**Stop after every stage and confer with the founder before starting the next one** (§2, §6). Never run two stages in one turn. The founder asked for this pace in Case 1 and wants it kept.

This folder sits outside the project (`~/Documents/personal/bio/freight/`) on purpose. The project's own `CLAUDE.md`, its research files and its method files all describe this case's outcome, and a session started inside the project loads `CLAUDE.md` automatically. So the project's rules you would otherwise inherit are written out in §9 below.

## 1. The goal

The project is building C-09: software that reads a customer's freight bills, finds lines worth disputing, and shows them to the customer's own staff, who decide and file. It is a software company: no analysts, no manual review (decision D-23). The project has a **method** for finding disputes. It lists every fact a dispute needs, where each fact lives, what to do when a fact is missing, which clock applies, and the verdict per bill line.

The method was tested once against a real outcome (Case 1, §7 below). Your job is the second test: **walk the founder through one real dispute, stage by stage, using only the method, reach a verdict, and then compare it with what actually happened.**
- Where the method and reality agree, say so.
- Where they disagree, find out why: a missing fact, a wrong place to look, a wrong precedence, a wrong NOT REPORTED rule, a wrong clock, or a case the method does not cover.

The deliverable is the comparison and a list of proposed changes. **You do not change the method**: the founders decide.

## 2. Who you are working with

The founders are building their first vertical SaaS and are new to freight. Explain in plain language, with the real numbers from the documents, one stage at a time. Define each freight term the first time you use it:
- PRO = the carrier's bill number;
- BOL = bill of lading, the shipper's pickup paper;
- prepaid / collect / third party = who the carrier bills: the shipper, the consignee, or someone else named on the BOL;
- NMFC = the industry's commodity classification;
- class = the rating group it assigns.

The method's output is what a reviewer at the customer would see.

**Pace (chosen by the founder for Case 1, keep it):** after every stage, write the stage into your file, give a short plain summary with the real values, and wait for the founder's go before the next stage. Each stop looks like this:
1. what the stage found, with the real numbers and pages, in plain language;
2. what it shows about the method (a gap, or something that held);
3. what the next stage is, with a question such as "Go on?".

Then end your turn. If the founder asks a question instead of saying go, answer it, then stop again. The founder may also make a call at a stop (in Case 1: which verdict bucket applied). Record it verbatim in your file.

## 3. Blindness: what you may open, and when

**For obfuscation, read the whited-out copies. The non-whited-out originals exist for confirmation. If the task is to not know, use only the whited-out copies.**

| | Before your verdict is written and shown to the founder | After |
|---|---|---|
| **The case's pages** | Only `inputs/page_06.png` … `page_10.png`: the whited-out copies (§4) | The original PDF, every page, for confirmation (§8) |
| **The method** | Only `method/`: the redacted copies | The originals in the project, `data/doc-exploration.md` (including §5.4) and `data/doc-explanation.md` |
| **Reference files in the project** (allowed) | `data/sources/13_rules_tariffs/odfl_100-Q_a.pdf` and `odfl_100-Q_b.pdf` with their text in `data/derived/text/13_rules_tariffs/odfl_100-Q_*.txt`; everything in `data/sources/15_bol_forms_and_standards/` and `data/sources/16_claim_forms_and_dispute_letters/`, with their text under `data/derived/text/15_*` and `16_*`. These were checked and carry nothing about this case | Anything in the project |
| **Everything else in the project** | **Closed**: `CLAUDE.md`, `data/catalogue.csv`, every `source.md`, `data/README.md`, `data/derived/ocr/`, all of set 21, `research/`, every `handoff*.md`, and the original method files | Open |

If you open something closed by mistake, stop and tell the founder before going on: the run is then no longer blind, and the write-up must say so.

The redacted method copies replace each example that cited this case with "[removed: an example that cites the Case 2 chain]". Do not try to reconstruct it.

## 4. The case: Case 2, an ODFL shipment from December 2004

**Inputs: five pages, whited out** (`inputs/`; see `inputs/README.md`). Each is the original 300-dpi scan of one page of a court exhibit. The court's filing stamp, which was printed over each page, has been left off, so nothing on the scan is lost.

| File | Original page | What it is (by its own heading; the reading is yours) |
|---|---|---|
| `page_06.png` | p. 6 | A straight bill of lading, Old Dominion Freight Line (ODFL), with a PRO barcode |
| `page_07.png` | p. 7 | A fax cover and letter |
| `page_08.png` | p. 8 | A "Debit Memorandum" |
| `page_09.png` | p. 9 | A remittance advice and check |
| `page_10.png` | p. 10 | A statement of account |

**One input from outside these pages** (the founder's, from the original handoff): **the consignee's first payment was $2,412.67 by card on 1/27/05.**

**Not given, on purpose:** every other page of the exhibit. What they hold is part of the outcome. Do not guess at it, and do not treat its absence as a fact.

The scans have no text layer. Read them as images. Enlarge a region with Python's PIL (`python3 -I`) if a figure is hard to read, and write every value with its page.

## 5. The method you use

In `method/`:
- `doc-exploration_blind.md`:
  - **§1** the 88 facts (IDs P01-P22 price terms, F01-F29 shipment facts, M01-M27 money facts, D01-D10 dispute facts);
  - **§2** where each fact lives: primary → fallbacks → never use → who holds it if nothing does;
  - **§2.5** the keys that link documents;
  - **§3** which copy wins when two disagree;
  - **§4** what NOT REPORTED means, the windows, and the decision table (§4.6);
  - **§9.7** the founders' decisions of 2026-10-20.
- `doc-explanation_s4_blind.md`: the seven-stage pipeline (bill facts → shipment facts → price terms → expected charge → compare → trigger test → clock and verdict), with the verdict rules in §4.7.
- `checks_AK_3-2.md`: the 33 audit checks (A1-G2) the method's check codes refer to.

**The founders' decisions you must apply (2026-10-20):**
1. **A carrier-added charge whose supporting record is missing** (no certificate behind a reweigh, no reason for a change) is **flagged in its own bucket**, "unsupported change, carrier's record requested", counted apart from other flags.
2. **The 180-day clock starts at the date the customer received the bill.** If that date is unknown, the bill date is the fallback. Aim to file inside the earliest window that applies. Windows are not always enforced, so a line up to **10 days past** the deadline is still shown, as "late: file now, may be refused".
3. **Tolerance, for now: any difference, so long as the carrier owes money.** A line billed above the expected amount is flagged, by any amount; a line billed below it is not.

## 6. How to run it

Work in this order. **After each stage, stop for the founder (§2) and wait for their go.** The stops are after step 1, step 2, steps 3-5 (one stop, or one each if the founder prefers), step 6, step 7 (the verdict: the hard stop before anything closed is opened), steps 8-9, and step 10.

1. **The question.** What was billed, to whom, what is disputed, and what kind of dispute it is: a **price** difference or a **trigger** difference (`doc-exploration_blind.md` §0, last paragraph). Name the audit checks by code.
2. **The facts.** List every fact ID the disputed line needs (§1's Checks column). For each, follow §2's row in order: primary, each fallback, the "never use" list, then "if none". Record a table:

   | ID | Fact | Where we looked, in order | Found (value, page) or NOT REPORTED | Owed by (shipper / carrier / nobody / customer's files, §4.1) |

   Use §2.5's keys to tie documents together. Where two documents disagree, apply §3.1 and say which copy wins and why.
3. **The price terms.** Which agreement, rule or tariff item prices or triggers the charge, in the edition in force on the ship date (§4, opening paragraph). If it is not held, say so, say who must supply it (the carrier, on request: 49 U.S.C. 13710(a)(1)), and say what the method can still check without it.
4. **Expected against billed.** The expected amount, or "not checkable" with the missing input named. Apply the tolerance rule.
5. **The trigger test.** Does the fact that makes the charge apply hold? Who owed that fact, and what does §4.2 or §4.3 say when it is missing or contradicted?
6. **The clocks.** Every window that applies (§4.4), from the receipt date if known, else the bill date; the earliest deadline; whether the dispute was inside it, inside the 10-day buffer, or late. Show the dates and the arithmetic.
7. **The verdict.** One of: flag; flag in the "unsupported change, carrier's record requested" bucket; ask the reviewer; not checkable; matches (`doc-exploration_blind.md` §4.6, `doc-explanation_s4_blind.md` §4.7). Add the reviewer's view: the dollars at stake, the deadline, the proof, what to request from whom, and the next action. **Show this to the founder before opening anything closed in §3.**
8. **The real outcome.** Only now open the original PDF (§8). What actually happened, quoted, with the page. Who decided, on what basis, and whether money moved.
9. **The comparison.** A table:

   | Decision point | What the method said | What happened | Agree? | If not, why |

   The decision points include at least:
   - is there a dispute;
   - who owed the deciding fact;
   - where the deciding fact lived;
   - the verdict;
   - the clock;
   - the next action (short-pay, claim, refund request), and whether the payment state changed what could be done.
10. **What to change.** For each disagreement or gap: the section and row of the method it touches, the proposed wording, and the evidence. Also list what the case confirmed. Then check each proposal against Case 1's (§7, BD-1 to BD-11): say which of them this case supports, contradicts or leaves untested.

Do all arithmetic in `python3 -I`, never by eye. Every value carries its page. A derived value is labelled derived, with its formula.

## 7. What Case 1 taught (results and things to watch; not method changes)

Case 1 was Yellow claim 16200 (2026-10-20): a $60 TONU (truck ordered, not used) that a 3PL, GlobalTranz, disputed. The full write-up is `research/s5_check_BD_c09_dispute_walkthrough.md` in the project. It is closed to you until your verdict is written: open it then, and add to it (§8).

**Result.** The method reached the right question but could not give the answer, and that was correct. It found a **trigger** dispute and named the deciding fact: what the 3PL's EDI pickup request said about the freight's size. It named who held that fact (the customer's own EDI log, and the carrier's record of the request it received) and found the clock met. The verdict was **ask the reviewer**, with the carrier's records requested alongside. The founder's words: "it would be A attached with B", meaning "ask the reviewer" with the "unsupported change" bucket's carrier requests attached. Yellow's own agent later found the TONU invalid ("the mistake was made by Yellow's terminal"). **But no money moved.** The invoice had been paid before the dispute, so the approval "was unable to make changes", and the refund then fell into the carrier's bankruptcy.

**Gaps found, proposed as BD-1 to BD-11 (none applied; the founders decide):**
- **BD-1. The payment state decides the route.** If the line is unpaid, dispute it with the carrier before the due date. Do not deduct it on your own: most LTL tariffs bar offsets. If it is paid, file a refund claim. The method uses the payment record only as a check input, not as this router.
- **BD-2.** "Approved" is not "credited": the method has no state between the carrier's approval and the money arriving.
- **BD-3.** No fact or document covers an LTL **pickup request** (as sent, as received).
- **BD-4.** When a carrier-added charge has a stated reason and the deciding fact sits in the customer's files: "ask the reviewer" with the carrier's records requested, rather than the "unsupported change" bucket.
- **BD-5.** TONU is modelled as truckload only (P15, check D5). LTL attempted-pickup items word the trigger differently by carrier (fault, "no freight given", or no LTL charge at all).
- **BD-6. A floor for unknown dates.** When neither the receipt date nor the bill date is known, the bill cannot predate the shipment, so each deadline is "no earlier than ship date + 180". And an unknown filing date can be bounded between two known events.
- **BD-7.** A carrier in **bankruptcy** adds a bar date and a new channel (the court's claims register). The method has no row for it.
- **BD-8.** With no bill held, the PRO and the line come only from dispute documents (M01 says "always present").
- **BD-9.** When the customer is itself the intermediary (a 3PL), the intermediary-invoice fact (M27) turns round: did it pass the charge on to its own client?
- **BD-10.** A 3PL's BOL form printing "Units 0" beside its pieces is a parse trap.
- **BD-11.** Catalogue notes.

**Traps that cost time in Case 1:**
- The claim letter mixed inputs and outcome in one paragraph. Fence the outcome sentences before you use any.
- A BOL field (handling units) that disagreed with what the claimant said about it. The BOL is not the request.
- A tariff "never" rule that mattered: three carriers' wordings would have given three different answers.
- No bill date, no receipt date and an undated letter. The clock was settled only by bounding dates between known events.

**What held:**
- the trigger/price split;
- §2's ordered lookup ending in a named party, which turned "missing" into concrete requests;
- §2.5's fallback key (the BOL number when the PRO is missing);
- §4.2's "shipper's omission is the carrier's licence";
- the tolerance rule;
- the carrier's answer surviving only second-hand, with no decision date (as earlier walks found).

## 8. After the verdict: confirmation, and where to write

**While blind,** write as you go to `case2_walkthrough.md` in this folder, so nothing is lost if the session is cut. Use these sections:
- §11.0 the result in five lines;
- §11.1 the case and documents;
- §11.2 the fact table;
- §11.3 price terms, expected against billed, the trigger;
- §11.4 the clocks;
- §11.5 the verdict as the reviewer would see it;
- §11.6 the real outcome;
- §11.7 the comparison;
- §11.8 proposed changes;
- §11.9 what the case confirmed;
- §11.10 the claim ledger: every number or quotation used, with page and a *verified* (re-opened at the source) or *assumed* tag.

**After the founder has seen your verdict,** confirm against the non-whited-out originals:
- the original PDF, every page: `~/Documents/personal/bio/freight/data/sources/21_ltl_bills_and_corrections/winndixie_flmb715964__6929.0.pdf`, 18 pages, scanned; render with `pdftoppm -f N -l N -r 150 -png <pdf> <out>`. The court's stamp sits on every page there;
- `data/doc-exploration.md` §5.4 (this chain, as the earlier walks read it) and the original method files.

Re-open every value you used on the original page, and record any difference between the whited-out copy and the original.

**Then,** inside the project:
- append your write-up to `research/s5_check_BD_c09_dispute_walkthrough.md` as **§11 onward**, after Case 1's §10;
- add one dated line to the Work Log in the project's `CLAUDE.md` (newest at the bottom, with a link to the file), as the existing entries do;
- leave the Answers block alone.

## 9. Rules (the project's, written out because its `CLAUDE.md` is closed to you)

- **`data/` is read-only.** Do not edit anything in `data/`. Propose changes in your §11.8; the founders decide what is applied. Never finalize a decision for them: present the evidence for and against.
- **Companies only.** The pages carry individuals' names, signatures, e-mail addresses and phone numbers. Never copy a person's name, e-mail address or phone number into any file or into chat. Write "the consignee's accounts-receivable contact", "a carrier employee".
- **Work offline.** If a public legal text is truly needed, ask the founder first. If you then fetch it, never put the user's e-mail address in a request header, URL or payload.
- **No sub-agents** unless the founder asks. One adversarial reviewer may be added at the end if the founder wants the comparison checked. It must re-open every citation and may not object without a re-opened file or a recomputed number.
- **Do not commit.** The founders commit (git: `main`, no branches).
- **Supporting docs** (your write-up) label each factual claim *verified* (backed by a source or data) or *assumed*.
