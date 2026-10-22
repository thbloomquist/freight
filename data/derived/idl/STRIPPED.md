# derived/ - stripped CSVs (check BE, collector K2)

One CSV per worksheet of every native spreadsheet/CSV kept (`<IDL id>__<sheet>.csv`). The original files in `files/` are unchanged (public records, kept as-is per the founders' rule).

**Rules applied (scripts/strip.py):**

- Columns dropped when the detected header row (or a row above it) names a person-identifying field: preparer / prepared by, created by, modified by, requester, approver, signer / signature, contact, buyer, planner, attention / attn, e-mail, phone, fax, POD name, employee, user / user name, owner, reviewer, coordinator, driver, picked/checked/processed by, inspector, analyst, assigned to, process owner, person responsible, and every address-line column (city / state / zip kept).
- JUUL workbooks only (consumer B2C shipments): also dropped Company, Ship To Company, ShipToCompany, Ship To Customer, Customer Name, Name, Consignee Name, Bill To Company, Ship To Attention.
- Cells matching an e-mail regex are blanked; header cells that were themselves e-mail addresses cause the column to be dropped.
- Report pre-ambles: the 1-3 cells to the right of, and the cell below, a label such as `User:`, `Prepared by / Date:`, `Reviewed by`, `Process Owner:` are blanked; cells shaped like a login id (`First.Last`, `first_last`) are blanked.
- Nothing else is changed (numbers, dates, SCACs, PRO/BOL numbers, company names kept).

**Known limits:** free-text comment columns are kept (e-mails blanked) and may still contain a first name; Mallinckrodt / Endo / Teva origin-destination and customer names are kept because they are businesses (pharmacies, wholesalers, clinics) - a few parcel rows may be to individuals. Review before publishing derived data outside the repo.

| IDL id | sheets written | rows (total) | columns dropped (header text) | cells blanked |
|---|---|---|---|---|
| ffhj0332 | 4 | 13847 | Company; Ship To Contact; Ship To Customer; Ship To Phone | 46 |
| fgcm0347 | 9 | 1798 | Created by x7 | 34 |
| fgky0254 | 1 | 83662 | Dest Address1; Dest Address2; Origin Address1; Origin Address2 | 8 |
| fgxk0247 | 1 | 3118 | (none) | 15 |
| fhkw0245 | 5 | 326 | (none) | 0 |
| fjcg0340 | 13 | 11649 | Customer Name x3; Prepared by:; User: x3 | 11 |
| fkbb0245 | 5 | 340 | (none) | 0 |
| fkhy0249 | 1 | 7944 | (none) | 30 |
| flcj0332 | 8 | 553 | User: x2 | 7 |
| fmmh0248 | 1 | 1834 | (none) | 10 |
| fngy0249 | 1 | 3226 | (none) | 31 |
| fthj0323 | 1 | 93 | (none) | 0 |
| gjmb0245 | 1 | 272 | (none) | 0 |
| gpgy0249 | 1 | 7686 | (none) | 59 |
| grfc0245 | 7 | 253 | (none) | 0 |
| gzpp0298 | 2 | 87 | (none) | 0 |
| hgky0254 | 2 | 83613 | Dest Address1; Dest Address2; Origin Address1; Origin Address2 | 6 |
| hjhy0249 | 1 | 6664 | (none) | 23 |
| hlkx0332 | 13 | 119684 | Company x2 | 7 |
| hqgy0249 | 1 | 6836 | (none) | 23 |
| jgmj0403 | 4 | 667 | (none) | 0 |
| jhxk0247 | 1 | 3611 | (none) | 10 |
| jjbk0323 | 3 | 96435 | Name; ShipToCompany | 11 |
| jkhy0249 | 1 | 7965 | (none) | 33 |
| jkvx0248 | 1 | 5768 | (none) | 97 |
| jlwc0253 | 21 | 2117 | Address; Address1 x2; Assigned To; Cell Phone; Contact Email x2; Contact First Name; Contact Name; Contact Phone; Contact name; Contact phone x2; Contact phone ext; Dest address; Fax Number; Mobile Phone; Office Phone; Origin Address; Person Responsible; Person Responsible for Process:; Process Owner:; User Email Address; User Name; User Phone Number; e-mail | 25 |
| jtgy0249 | 1 | 8693 | (none) | 15 |
| jxhy0249 | 1 | 9445 | (none) | 23 |
| kgxk0247 | 1 | 3231 | (none) | 10 |
| kjxw0443 | 1 | 91 | CONSIGNEE ADDRESS; POD NAME; SHIPPER ADDRESS | 0 |
| kkkx0332 | 12 | 8799 | Customer Name x3; User: x5 | 9 |
| klcv0245 | 29 | 1139 | (none) | 0 |
| klgx0408 | 6 | 230 | (none) | 0 |
| kmxw0421 | 1 | 42 | (none) | 0 |
| llgy0249 | 1 | 5882 | (none) | 20 |
| lmdg0349 | 1 | 100 | (none) | 0 |
| lqhn0318 | 5 | 190 | User: | 5 |
| lxhy0249 | 1 | 7579 | (none) | 5 |
| mkxw0443 | 1 | 12 | CONSIGNEE ADDRESS; POD NAME; SHIPPER ADDRESS | 0 |
| mygy0249 | 1 | 5925 | (none) | 70 |
| nghy0249 | 1 | 9749 | (none) | 135 |
| njgw0357 | 4 | 742 | User: | 12 |
| nkgy0249 | 1 | 5934 | (none) | 64 |
| nlgy0249 | 1 | 4429 | (none) | 49 |
| nnkk0247 | 1 | 8615 | (none) | 36 |
| nxhy0249 | 1 | 7785 | (none) | 5 |
| pghy0249 | 1 | 7755 | (none) | 497 |
| pjhy0249 | 1 | 6922 | (none) | 16 |
| pjvx0248 | 1 | 6826 | (none) | 43 |
| pkgy0249 | 1 | 4500 | (none) | 25 |
| plgy0249 | 1 | 5851 | (none) | 81 |
| pmkk0247 | 1 | 5550 | (none) | 28 |
| pnkk0247 | 1 | 8115 | (none) | 44 |
| ppbp0318 | 8 | 173277 | (none) | 0 |
| prvh0250 | 7 | 326 | (none) | 0 |
| psgn0318 | 3 | 1906 | User: | 14 |
| psgy0249 | 1 | 12090 | (none) | 126 |
| psww0360 | 1 | 12 | (none) | 0 |
| ptgy0249 | 1 | 6852 | (none) | 25 |
| pxhy0249 | 1 | 9534 | (none) | 35 |
| pycp0254 | 1 | 4902 | Dest Address1; Dest Address2; Origin Address1; Origin Address2 | 20 |
| qfnh0248 | 1 | 3772 | (none) | 20 |
| qhhy0249 | 1 | 8288 | (none) | 59 |
| qqgy0249 | 1 | 5276 | (none) | 77 |
| qslf0403 | 1 | 12 | (none) | 0 |
| qsww0360 | 1 | 7 | (none) | 0 |
| rkgy0249 | 1 | 4354 | (none) | 29 |
| rlmh0248 | 1 | 2981 | (none) | 20 |
| rmgy0249 | 1 | 5560 | (none) | 63 |
| rxhy0249 | 1 | 8477 | (none) | 51 |
| sfdx0318 | 1 | 59 | Signature Required | 0 |
| shhy0249 | 1 | 8345 | (none) | 70 |
| skbp0318 | 6 | 55338 | Company x3 | 1 |
| sygy0249 | 1 | 7305 | (none) | 20 |
| szyc0245 | 2 | 301 | (none) | 0 |
| tjhy0249 | 1 | 9621 | (none) | 44 |
| tkgy0249 | 1 | 5285 | (none) | 49 |
| tmgy0249 | 1 | 5081 | (none) | 2292 |
| tsmx0332 | 1 | 1303 | User: | 2 |
| tzlx0332 | 9 | 1052116 | Last Modified By; User: x2 | 12 |
| xfvw0253 | 4 | 46279 | Dest Address1; Dest Address2; Origin Address1; Origin Address2 | 7 |
| xhhy0249 | 1 | 6855 | (none) | 20 |
| xpgy0249 | 1 | 6368 | (none) | 52 |
| xqgg0299 | 27 | 279186 | Company x10; Consignee Address1 x2; Consignee Address2 x2; Consignee Attn x2; Consignee Contact x2; Contact Name x2; Created By x2; Name x2; Ship to Customer x2 | 59 |
| xrgy0249 | 1 | 6386 | (none) | 116 |
| ygxk0247 | 1 | 3661 | (none) | 15 |
| yhcj0332 | 6 | 593 | User: | 5 |
| yhhy0249 | 1 | 9859 | (none) | 51 |
| ylyh0248 | 9 | 1428 | (none) | 0 |
| yyfx0301 | 1 | 4357 | Bill To Address1; Bill To Address2; Bill To Attention; Bill To Company; Bill To Email; Bill To Phone; Ship To Address1; Ship To Address2; Ship To Attention; Ship To Company; Ship To Email; Ship To Phone | 3 |
| yygy0249 | 1 | 4835 | (none) | 13 |
| zghn0318 | 5 | 191 | User: | 5 |
| zjlg0340 | 6 | 103254 | User: x2 | 3 |
| zygy0249 | 1 | 6591 | (none) | 64 |
| zzmh0248 | 1 | 6650 | (none) | 50 |

Files: 309 CSVs from 95 source files.

## Coordinator fixes after the verification (2026-10-21, `research/s5_check_BE_adversarial.md` §5)

- `_tools/idl_strip.py` now also blanks phone numbers inside cells (the PHONE pattern was defined but not applied) and drops First Name / Last Name / Surname columns. Every CSV above was regenerated with it (B2C rule applied to all 61 JUUL ids), so the per-file counts in the table above are K2's first pass and may differ slightly.
- Blanked by hand after regeneration: a residential mis-delivery address in a comment (fgcm0347, Oct. 2015 sheet); consumer street addresses typed into the City column (skbp0318, both freight sheets; hlkx0332 B2C sheet, inside its zip); the First / Last Name columns of jlwc0253's Project Team sheet, which sit below the detected header row.
- skbp0318 (25-115) holds about 47,000 consumer recipient names in its original, so it was replaced in `sources/` by a stripped zip like the other five JUUL–DCL workbooks; the original is in `freight_private/idl_originals/`.
- Business addresses (JUUL's offices, a flavour lab, a pharmaceutical site) are kept.
