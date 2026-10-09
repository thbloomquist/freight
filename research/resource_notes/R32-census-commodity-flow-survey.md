# R32 - About the Commodity Flow Survey (CFS)
- URL: https://www.census.gov/programs-surveys/cfs/about.html | Author: U.S. Census Bureau with the Bureau of Transportation Statistics (BTS) | Year: 2022 survey; page "Last Revised - June 26, 2025" | Type: primary (government dataset) | Access:
  - The about page was read in full from a curl download.
  - The 2022 headline results come from the Census press release "Census Bureau Reports Shipment of U.S. Goods Reached 12.2 Billion Tons and $18.0 Trillion" (https://www.census.gov/newsroom/press-releases/2025/cfs-shipments-of-goods.html; same agency), read via curl.
  - https://www.bts.gov/cfs returned "Access Denied" to curl.
  - Accessed: 2026-09-14.
- Secondary sources consulted (not in study_links.md): the Census press release above (same publisher, used only for headline totals).
- Decision the resource addresses: candidate enumeration and sizing of the shipper side (stages S1 and S3). It is data, not a method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context (verbatim): "The survey is the primary source of national and state-level data on domestic freight shipments by American businesses. As a shipper-based survey, the CFS collects information on how U.S. establishments transport raw materials and finished goods; the types of commodities shipped by mode of transportation; the value, weight, origin, and destinations of shipments (including exports). The CFS does not include imports or shipments originating in any U.S. territories. Industry coverage includes: Mining, Manufacturing, Wholesale Trade, Select Retail and Services, and some auxiliary establishments (e.g., warehouses) of in-scope, multi-unit, and retail companies." *(verified)*
- Mechanism and steps:
  - Sampling: "A sample of 165,000 establishments were selected for the 2022 CFS based on geographic location and industry. Each sampled establishment is asked to report either a sample of individual shipments or all of their shipments that occurred during a specified one-week period in each quarter of the calendar year."
  - Mixed shipments: "respondents are instructed to report the commodity that makes up the greatest percentage of the shipment's weight".
  - Dissemination: "disclosure avoidance is added in the form of noise infusion". Tables are published "with multiple variables including, but not limited to, SCTG, NAICS, Mode, Origin and Destination Geography at the U.S., Region, division, state, and CFS area".
  - An experimental "Public Use File (PUF) that provides shipment-level characteristics", which lets users "create customized tables and build models".
- Criteria, inputs and data required (for the project): the shipper industry (NAICS) × commodity (SCTG) × mode × geography cross-tabulations and the PUF.
  - Access: data tables via https://www.census.gov/programs-surveys/cfs.html → Data, and data.census.gov.
  - 2022 publication page: https://www.census.gov/library/publications/2022/econ/2022cfs.html (found by search, not opened).
- Output produced, 2022 headline figures *(verified, press release)*:
  - "Shipments of goods in the United States reached 12.2 billion tons in 2022, virtually unchanged from 2017". Value "increased $3.5 trillion (24.0%) to $18.0 trillion (not adjusted for inflation or seasonality)."
  - "Trucks as a single domestic mode of transportation hauled approximately 8.3 billion tons (68.1%) of the total tonnage. These shipments accounted for $13.2 trillion (73.5%) of the total value of commodities shipped in 2022."
  - "Customer Pickup – a newly tabulated mode estimate in 2022 – accounted for 1.4 billion tons of U.S. goods shipped (about 11.4% of the total tonnage) in 2022, valued at $1.0 trillion."
  - "Manufacturing establishments shipped 4.9 billion tons of commodities worth $7.1 trillion in 2022. Wholesale establishments shipped 4.1 billion tons of commodities worth $8.1 trillion."
  - "Hazardous material shipments weighed 2.6 billion tons and accounted for $2.1 trillion in 2022."
  - Caution: the same release says "The South region shipped 1.9 billion tons (40.4%)". That tonnage is inconsistent with the 12.2-billion-ton total (40.4% would be about 4.9 billion), so do not quote it without checking the tables.
- Rationale and evidence base: a legally mandated federal survey ("Response is required by law", Title 13 U.S.C. §131). Its stated uses include "analyzing trends in the movement of goods ... forecasting demands for the movement of goods".
- Assumptions, limitations, critiques:
  - Stated: excludes imports and territories; one-week-per-quarter sampling; noise infusion.
  - *Reader inference:*
    - Farms are not in the listed industry coverage, so farm-origin shipments (the origin hypothesis) cannot be sized from the CFS. Use FAF (R31) and USDA AMS (R34) instead.
    - Shipment value is not shipping cost.
    - Customer Pickup shows that 11.4% of tonnage moves with the buyer arranging transport, which moves the freight decision (and the software buyer) to the consignee.
- Key quotes: see above.

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- The CFS is the dataset that pairs a shipper industry with a transport mode. That pairing is exactly the project's two-sided unit, seen from the shipper side, so it should be the backbone of candidate enumeration (S1): rows are shipper NAICS or SCTG commodity, columns are mode and distance band.
- Truck's dominance (73.5% of value) says that most candidate cells will involve trucking. Pair them with R44's trucking and brokerage codes for the freight-company side.
- Its blind spot is the project's origin hypothesis: farms are outside the survey frame.

## Read status: full (about page); 2022 headline results from the Census press release; tables and PUF not queried
