# C-09 reach-out: the questions, then the people to message for a first design partner

- **What this is:** the project-side twin of the founders' working file for finding C-09's first design partner. It holds the questions that decide whether the software is viable (§1), and the method and counts of the people search (§2). **No person and no prospect firm is named here** (kit §1.3). The names, LinkedIn links, emails and phones are in `~/Documents/personal/bio/freight_private/reachout.md`.
- **The founders' request (2026-10-20):** "Look up people I can reach out to on LinkedIn to get an initial design partner for this. So I can ask them our outstanding questions that determine the viability of this software in the space. Write the questions first, then the peoples names and their LinkedIn links. Any other contact info you can find as well, like Phone Number or Email."
- **Decided in chat the same day:**
  - the file is private, with this names-free pointer;
  - LinkedIn links for the 151 vetted targets of check AY (`data/leads.md`), plus a new search for people who check or pay the bills;
  - the ten questions plus the design-partner ask.
- **Status:** input to S5 (the interviews). **It decides nothing.** Grades and flags are **[our call]**.

## 1. The questions

These are the questions that decide whether C-09 is viable. They're the ten in `data/open-questions.md`, worded the way the evidence file says to ask them (`C09-open-questions-evidence.md` §0.2-§0.3), plus the design-partner ask that closes the conversation. The full list of about 40 questions, with what proves each answer, is the master list in `C09-open-questions-evidence.md` §0.3; this section doesn't copy it.

**Rules for asking** (kit §1.1):
- Ask about the last time it happened, with amounts. Never ask "would you".
- Get a number with its unit and period.
- Ask to see the document.
- What an interviewee says is a **claim**. Only the look-back **proves** a number.
- F1-F4 are the founders' own four questions.

**Who can answer which question** (role classes from the leads brief):
- **CHK:** people who check the bills (logistics, transportation or traffic staff; freight-bill clerks).
- **AP:** accounts payable.
- **BUD:** the budget voice (controller, CFO).
- **PUR:** purchasing.
- **REF:** a referral to the person who checks the bills.

### 1.0 The first message: no product, no pitch

The first message asks for 20 minutes of their experience and says plainly that it's research (kit §3.1). There are three versions:
- for a controller or CFO, `research/s5_check_Y_c09_reach.md` §13.2;
- for a logistics coordinator on LinkedIn (short), §13.3;
- for a truckload-heavy logistics manager, §13.4.

Emails need an accurate sender and subject, a postal address and a one-line opt-out (CAN-SPAM). **The design-partner ask comes at the end of the interview, not in the first message.**

### 1.1 The questions, in interview order

| # | Q (open-questions.md) | Question | Ask it this way | What it decides | Ask |
|---|---|---|---|---|---|
| 1 | Q2 | How much do you spend on freight, and how much goes through brokers? | "What did you pay carriers and brokers last year, split truckload, LTL and parcel? A band is fine: under $250k / $250k-1M / $1-3M / over $3M." Then: "What share was booked through a broker or 3PL?" | Which row of the Kill / Cover / Pass table applies, since the lines are read at the shipper's own spend. Also which claim deadline applies: broker terms give 5-30 days, not 180 | BUD, PUR, CHK |
| 2 | Q3 | **F2:** Who checks the bills, how long does it take, and with what tool? | "Who checks freight bills before they're paid? Walk me through the last one they checked: what did they compare it with, and how long did it take?" Then: "Does anyone else look at them: an outside firm, software, a booking tool's audit screen? What did it catch last time, and what did you pay for it?" | Whether the shipper's staff would work our flags (the band between Cover and Pass). Whether an incumbent already does the job (the show-stopper test) | CHK, AP |
| 3 | Q1 | **F1:** What share of freight dollars is billed wrong? | "Tell me about the last freight bill that turned out to be wrong. How much, what kind of error, who caught it, and did the money come back?" Then: "In the last 12 months, how many bills turned out wrong, for how many dollars, against roughly what freight spend?" | **Test 1: Kill, Cover or Pass.** Only the look-back proves it | CHK, AP |
| 4 | Q4 | **F4:** How many disputes did you file, and has an outside firm audited you? | (a) "In the last 12 months, how many disputes or overcharge claims did you file with carriers, for how many dollars? How many came back, for how much, and how many days did it take? Tell me about the last one a carrier refused." (b) "Have your freight bills ever been audited by an outside firm? When, what did it find in dollars against how much spend, and what happened to errors the year after?" | How much carriers credit, and whether customers would renew | CHK, BUD |
| 5 | Q5 | **F3:** How much do you think you're overcharged? | "How much a year do you think you're overcharged?" Always follow with: "What makes you say that?" | **Logged as a belief only.** It tells us whether the "scoop off the top" pitch lands. It's compared with the look-back later | CHK, BUD |
| 6 | Q10 | Do your contracts set a dispute deadline, and how soon do you notice a wrong bill? | "Do your truckload contracts or broker rate confirmations have a claims clause, like 'claims within 90 days'? Can you show me one?" Then: "The last wrong bill: how many days after paying did someone notice, and how many more before it was disputed?" | How much spend is still recoverable, which is what Test 1 divides by | CHK, AP |
| 7 | Q7 | How many hours did your team spend on freight bills last month? | "How many hours did your team actually spend on freight bills last month? Who did it, and what did it push aside?" Ask about last month's actual hours, never "how many could you give it" | **Test 3:** whether the flag queue fits their hours | CHK, AP |
| 8 | Q8 | Where do your rate agreements live, for how many carriers, and how often do they change? | "Who keeps your carrier rate agreements, and in what form: PDF, spreadsheet, email, a carrier's website? How many carriers have one? When did one, or a fuel table, last change, and who updated it where?" | Test 3: how long setup takes | CHK, PUR |
| 9 | Q9 | What do you pay today to check bills, and who signs off on software? | "Does anyone audit your freight bills today: staff, an outside firm, software? What did you pay last year, and what came back?" Then: "The last time you bought software for logistics or AP, who approved it, out of which budget, and up to what amount could they sign alone?" | Whether a subscription can be bought at all | BUD, AP, PUR |
| 10 | Q6 | Will you share last month's invoices and your rate agreements under an NDA? | "If I asked for last month's paid freight invoices and your rate agreements, what format would they be in, and how long would it take to pull?" Then ask for them, under a mutual NDA. If they hesitate: "Which of your carriers' agreements say the rates are confidential?" | **Test 2:** kill if 2 of the first 3 shippers say no. A "no" that names only a security certificate (SOC 2) is a cost question, not a refusal | BUD, CHK |

### 1.2 The design-partner ask (close of the interview)

Ask this once question 10 has been asked, and only of a shipper inside the spend band (about $1.5-10M of truckload and LTL a year):

> "We're building software that reads your freight bills against your rate agreements and flags the ones that look wrong, for your own team to review. Before we build further, we'd like to run it, free, on one shipper's real bills: 1-3 months of paid truckload and LTL invoices, the rate agreements behind them, and a sample of BOLs and delivery receipts, all under a mutual NDA, with the files deleted afterwards. Your reviewer would go through the flags on screen while we time it. Would you be open to that?"

What a "yes" sets in motion, in the adopted order (kit §6.1; `C09-open-questions-evidence.md` §0.5):

1. **Their capacity first.** "How many hours a month can your team give the flag queue?" This is recorded before anything is timed, and it is **Test 3's limit**. If they give no figure, it's 20 hours.
2. **The rules run as scripts** on the founders' local demo, against the in-window bills and agreements. Raw files stay outside the project folder (D-18, which must be settled before real data arrives).
3. **Their reviewer confirms the rules** read from each agreement, while timed.
4. **Their reviewer works every flag while timed:** accept or reject. This gives the **flagged rate (Test 1)**.
5. **The pilot:** at least one billing cycle on new bills. It shows whether flags turn into disputes (follow-through) and credits.

**What to tell them it costs them [our calc]:** three months at $1.5M of spend is about 560 bills. At about 10 minutes a flag, that's about 14 hours if 15% are flagged, and about 54 hours if 58% are.

**Price:** the look-back is free. The product will be a subscription; no amount is set yet (Q6, D-15). Ask what they would pay a month, and who approves a software subscription up to what amount, and record both. A spoken yes is only a claim; a signed agreement or letter of intent is the proof.

### 1.3 Log it
- Every wave goes in `research/selection_runs/run-01/5_log.md` §1: sent, reached, replies, booked, held, and days to the first meeting.
- The first outreach starts the first-customer clock (`5_log.md` §10.3, A-X1).
- Interview notes use pseudonymous IDs only (`5_log.md` header).

## 2. Method and counts (2026-10-20)

**How it was done:**
- **Three finders, then three adversarial reviewers, with no more than three agents running at once.** F1 searched call-list rows 1-75 and F2 rows 76-151, both of `c09_leads.md` §3.1. F3 searched for new people who check or pay the bills. R1 to R3 reviewed one finder file each.
- **The search method.** Check AY found 0 LinkedIn profiles because the search tool ignores `site:linkedin.com/in`. Restricting the search to linkedin.com through the tool's `allowed_domains` setting works: results come back with the profile URL and its headline.
  - No linkedin.com page was opened, because of the login wall.
  - The match rests on the result title, never on the tool's own summary.
  - A same-name person with no tie to the firm got no URL.
- **The searches.** The finders ran 376 searches (F1 113, F2 118, F3 145) and the reviewers 189 (R1 56, R2 69, R3 64). The coordinator re-checked every drop and every match moved down from exact in 9 more.
- **The cap.** The session's search cap (200) ran out midway. The founders raised it to 1000 (`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` in `~/.bashrc`), and the finders resumed.
- **Rules**, from the leads brief `c09_leads_brief_common.md` §1: contact nobody; no identity in any request; no data-broker or people-search sites (ContactOut, Datanyze and TheOrg came up in results and were ignored); professional details only.
- **One change, reversible:** the brief's 20% cap on people found only on LinkedIn was lifted for F3, because the founders asked for LinkedIn.

**The 151 targets already on the call list:**

| After review | Count |
|---|---|
| match (name, firm and role) | 36 |
| firm match | 39 |
| may have moved | 12 |
| several same-name people, none tied | 10 |
| not found | 54 |
| **with a LinkedIn link** | **87** |

**The reviews:**
- **R1 and R2 checked the 99 links F1 and F2 had recorded (75 + 12 + 12 extras):**
  - 91 kept and 7 moved to a different class;
  - 1 removed (a common name, with a second same-name person in the same town);
  - 1 added from a spot-check (an accented spelling);
  - 0 found to be the wrong person.
- **R3 reviewed F3's 44 new people:**
  - 18 kept, 17 retagged and 2 moved to contrast;
  - **7 dropped:** a dealer, a firm sold in 2021, a furniture importer that closed, a feed store, and three people whose role was never shown in a result title.
  - The coordinator re-checked all 7 drops. All stand, but two of the reasons were corrected: a contract aerosol filler and a candy maker may fit SG3. Their drops stand only because the person's role is unproven.

**What the private file holds:** 200 people (151 + 12 seen in passing + 37 new kept), with 135 LinkedIn links.

| Section | People | With a link |
|---|---|---|
| private §2.1 check or pay the bills | 59 | 35 |
| private §2.2 budget voice | 49 | 27 |
| private §2.3 purchasing and referrals | 78 | 59 |
| private §2.4 contrast (new this round) | 14 | — |
| private §3 may have left (also listed in private §2) | 12 | 12 |

**What the round shows:**
1. **The people who check or pay the bills are the least visible on LinkedIn.**
   - Of the 39 such people on the call list, 15 have a link. 3 of those may have moved, and 3 more show a different role today: purchasing, credit and sales.
   - None of the 8 AP people has a profile tied to the firm.
   - CFOs, controllers and plant leaders mostly have one.
   - To reach a checker, use the phone and email from the staff directory, or ask the CFO.
2. **The best new pattern is a quoted title plus an industry word,** such as "Traffic Manager" with Furniture, or "Logistics Coordinator" with Packaging. It found many of the 15 new checker targets that survived review (F3: 2 hits in 3 tries). A firm name plus a role word hit about 1 time in 5.
3. **12 call-list people may have left their firm.** One left about 2014 for a homebuilder, so that row is out of date.
4. **No AP person whose title mentions freight turned up at any manufacturer.** Freight-bill work sits with logistics staff, which matches what check Y found in job postings.

**Open points for the founders:**
- **The LI-ONLY cap** was lifted for this round. Reverse it if you want LinkedIn-only names kept to a minority.
- **Firms to confirm before you call:**
  - two rows may be at a distributor;
  - one row may be at a firm that no longer exists;
  - for two rows at subsidiaries, ask which entity books the freight.
- **One more named person, not added:** one new firm's own page lists a separate logistics and warehouse contact.
