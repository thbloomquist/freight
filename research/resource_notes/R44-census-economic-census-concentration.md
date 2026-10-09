# R44 - 2017 Economic Census, NAICS Sector 48-49 Transportation and Warehousing tables (incl. EC1700SIZECONCEN "Concentration of Largest Firms")
- URL: https://census.gov/data/tables/2017/econ/economic-census/naics-sector-48-49.html | Author: U.S. Census Bureau | Year: 2017 data (page "Last Revised - July 19, 2024"). The 2022 edition of the same table was also found and used. | Type: primary (government dataset) | Access:
  - The sector page was read in full from a curl download.
  - The concentration table EC1700SIZECONCEN.zip (https://www2.census.gov/programs-surveys/economic-census/data/2017/sector00/EC1700SIZECONCEN.zip, a pipe-delimited .dat file) was downloaded and filtered locally for freight NAICS codes.
  - So was the 2022 edition, EC2200SIZECONCEN.zip (https://www2.census.gov/programs-surveys/economic-census/data/2022/sector00/EC2200SIZECONCEN.zip). Its field file confirms RCPTOT is in $1,000, VAL_PCT is the "revenue of largest firms as percent of total", and HHI is "based on sales, value of shipments, or revenue".
  - Accessed: 2026-09-14.
- Secondary sources consulted (not in study_links.md): the 2022 concentration file above (same publisher, later edition).
- Decision the resource addresses: desk evidence on the structure of the freight-company side, meaning firm counts, revenue and concentration or fragmentation (S3, S4). It is also the raw input to R20's screen and to R21's concentration threshold. It is data, not a method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context: the Economic Census "produces detailed statistics on the size of establishments and firms for every sector except Management of Companies and Enterprises (55). All data are available at the national level and includes only establishments and firms with payroll." *(verified)*
- Mechanism and steps: tables relevant to freight listed on the page *(verified)*:
  - EC1748BASIC (sector summary statistics).
  - EC1700NAPCSINDPRD and EC1700NAPCSPRDIND (products by industry).
  - EC1700SIZECONCEN ("Concentration of Largest Firms"), EC1700SIZEEMPFIRM and EC1700SIZEREVFIRM (firm size by employment and by revenue), EC1700SIZESUMU (single-unit versus multi-unit firms), EC1700SIZELFO (legal form).
  - EC1748PURMODE ("Cost of Purchased Transportation by Mode of Shipping for the U.S. and States: 2017").
  - EC1700FRAN (franchise status).
  - Each is available on data.census.gov (e.g. https://data.census.gov/table/ECNSIZE2017.EC1700SIZECONCEN?n=48-49) and as a zip file on the FTP.
- Criteria, inputs and data required: fields FIRM, ESTAB, RCPTOT ($1,000), PAYANN, EMP, VAL_PCT and HHI, each by concentration row (all firms, 4, 8, 20 and 50 largest).
- Output produced: extracted values for freight codes *(verified from the .dat files; revenue converted to $ billions; "Top-k" = revenue share of the k largest firms)*:

  | NAICS | Industry | Year | Firms | Revenue $B | Top-4 % | Top-8 % | Top-20 % | Top-50 % | HHI |
  |---|---|---|---|---|---|---|---|---|---|
  | 48-49 | Transportation and warehousing | 2017 | 184,735 | 895.2 | 17.9 | 26.4 | 34.2 | 42.8 | 112.8 |
  | 48-49 | | 2022 | 237,360 | 1,316.3 | 17.2 | 24.4 | 31.8 | 40.8 | 99.8 |
  | 484 | Truck transportation | 2017 | 112,134 | 290.5 | 8.1 | 13.3 | 20.9 | 29.2 | 31.3 |
  | 484 | | 2022 | 156,156 | 423.3 | 8.3 | 13.5 | 20.8 | 28.3 | 32.7 |
  | 4841 | General freight trucking | 2017 | 66,075 | 191.4 | 12.1 | 19.7 | 30.6 | 39.6 | 65.8 |
  | 4841 | | 2022 | 104,388 | 293.1 | 11.8 | 19.2 | 29.0 | 37.6 | 63.9 |
  | 48411 | General freight, local | 2017 | 29,977 | 32.7 | 2.0 | 3.3 | 5.8 | 10.2 | 2.6 |
  | 48411 | | 2022 | 43,243 | 54.7 | 2.3 | 3.7 | 6.4 | 10.5 | 3.1 |
  | 484121 | Long-distance truckload | 2017 | 31,908 | 112.4 | 15.4 | 21.9 | 29.7 | 39.0 | 86.5 |
  | 484121 | | 2022 | 53,705 | 172.7 | 16.7 | 22.1 | 29.4 | 37.4 | 98.0 |
  | 484122 | Long-distance LTL | 2017 | 4,410 | 46.2 | 40.3 | 60.5 | 77.4 | 85.3 | 571.9 |
  | 484122 | | 2022 | 7,675 | 65.7 | 40.8 | 58.9 | 76.3 | 82.9 | 572.3 |
  | 4842 | Specialized freight trucking | 2017 | 46,282 | 99.2 | 5.8 | 9.7 | 14.1 | 19.6 | 15.1 |
  | 4842 | | 2022 | 52,012 | 130.2 | 6.0 | 9.0 | 13.6 | 18.6 | 15.0 |
  | 48422 | Specialized, local | 2017 | 29,544 | 42.7 | 1.9 | 3.1 | 5.7 | 10.0 | 2.5 |
  | 48422 | | 2022 | 31,927 | 57.5 | 1.8 | 2.9 | 5.4 | 9.9 | 2.4 |
  | 484230 | Specialized, long-distance | 2017 | 9,222 | 40.8 | 13.0 | 18.9 | 27.3 | 38.1 | 63.9 |
  | 484230 | | 2022 | 10,701 | 52.6 | 14.3 | 19.2 | 27.7 | 38.1 | 74.0 |
  | 488510 | Freight transportation arrangement (brokers, forwarders) | 2017 | 15,097 | 64.9 | 12.2 | 16.8 | 23.9 | 32.8 | 59.2 |
  | 488510 | | 2022 | 17,130 | 134.9 | 9.9 | 15.5 | 23.4 | 34.3 | 43.4 |
  | 4884 | Support activities for road transportation | 2017 | 10,672 | 10.8 | 9.3 | 12.9 | 17.6 | 22.9 | 35.0 |
  | 4921 | Couriers and express delivery | 2017 | 4,215 | 84.7 | 91.2 | 92.4 | 93.6 | 94.9 | n/a |
  | 4921 | | 2022 | 6,553 | 132.3 | 87.7 | 88.8 | 89.9 | 90.9 | n/a |
  | 493 | Warehousing and storage | 2017 | 8,068 | 38.1 | 15.4 | 23.0 | 33.3 | 44.5 | 93.3 |
  | 493 | | 2022 | 9,473 | 60.3 | 18.5 | 27.8 | 39.0 | 48.2 | 147.9 |
  | 49312 | Refrigerated warehousing | 2017 | 655 | 5.8 | 42.3 | 55.9 | 64.5 | 74.9 | 583.8 |
  | 49312 | | 2022 | 719 | 7.6 | 51.3 | 58.5 | 64.7 | 73.9 | n/a |
  | 49313 | Farm product warehousing | 2017 | 374 | 0.8 | 16.5 | 25.6 | 43.9 | 67.3 | 146.3 |
  | 49313 | | 2022 | 411 | 1.0 | 13.2 | 21.4 | 41.2 | 64.5 | 118.0 |

  - For context, 2017: 481 air (top-4 61.8%, top-50 91.8%); 483 water (top-4 49.9%, top-50 87.1%).
  - The HHI value is carried on the 50-largest-firms row. "n/a" means that row reports 0.
  - Some 2022 "4 largest firms" rows show FIRM = 0 while still giving a revenue share (e.g. 48411, 4842, 48422). *Reader inference:* this is a disclosure or flag artefact, and the shares are still usable.
- Rationale and evidence base: official statistics, and a complete count of employer firms.
- Assumptions, limitations, critiques:
  - Stated: payroll firms only.
  - *Reader inference:*
    - One-truck owner-operators without payroll (nonemployers) are excluded, so trucking is even more fragmented than shown.
    - *Reader knowledge (unverified):* agriculture (crop and animal production) is outside the Economic Census, so the farm side cannot be screened with this table.
    - Revenue is not a software budget.
    - The census runs every five years.
- Key quotes: "includes only establishments and firms with payroll" (sector page, Establishment and Firm Size Statistics).

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:* this table turns the fragmentation debate (R20 and R41 versus R21) into numbers for every freight-company type.
- Applying R21's concentration test ("fewer than 50 companies represent over 80% of revenue"):
  - Concentrated: couriers (90.9% in 2022) and LTL (82.9%).
  - Just under the line: refrigerated warehousing (73.9%).
- Applying R20's "SMB heaven" filter (top 50 < 20%):
  - Passes: specialized freight trucking (18.6%), local general freight (10.5%), local specialized (9.9%).
  - Mid-range: truckload (37.4%), brokerage and forwarding (34.3%), warehousing (48.2%).
- Brokerage revenue roughly doubled between 2017 and 2022 ($64.9B to $134.9B) while its top-4 share fell (12.2% to 9.9%). Firm counts rose across trucking. Both are growth signals for S3, and they cover the 2021-22 freight boom, so treat them as cyclical.
- The same table exists for shipper industries (manufacturing, wholesale), so both sides of a candidate pair can be scored on the same scale.
- EC1748PURMODE, not extracted here, would give purchased transportation by mode, a proxy for the freight spend brokers and 3PLs manage.

## Read status: full (sector page; concentration rows for the listed codes extracted from the 2017 and 2022 files)
