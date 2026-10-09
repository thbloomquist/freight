# R39 - Food Dollar Series - Summary Findings
- URL: https://www.ers.usda.gov/data-products/food-dollar/summary-findings | Author: USDA Economic Research Service (ERS) | Year: "March 2026 Food Dollar update, which released the 2024 Food Dollar data and revised data for previous years" | Type: primary (government statistics) | Access: the summary page was read in full from a curl download. The 2024 industry-group-bill chart image (https://www.ers.usda.gov/media/29099/113892-chart-image-file.png) was downloaded and viewed, because the page text does not print the transportation figure. | Accessed: 2026-09-14
- Decision the resource addresses: evidence on the origin hypothesis (L-FARM). It is also a source of cost shares along the food chain for desk sizing (S3). It is data, not a method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context: "The Food Dollar measures costs of food along the domestic food supply chain, attributing the shares of value to different sources along three bills that conceptualize the food supply chain in different ways. These bills are the marketing bill, the industry group bill, and the primary factor bill." The 2026 update comprehensively revised the model (ERS report "A More Detailed Food Dollar: Enhanced Accounting of U.S. Food Costs"). *(verified)*
- Mechanism and steps (the three bills and their 2024 values, *verified*):
  1. Marketing bill.
     - "The farm share was 11.8 cents per dollar spent by U.S. consumers on domestically produced food in 2024. The marketing share, which captures the share of value added by post-farm activities that transform farm commodities into finished food products, was 88.2 cents. This includes transporting, processing, storing, wholesaling, and retailing food."
     - By channel: food-at-home farm share 18.5 cents; food-away-from-home 7.1 cents. "Farmers receive a lower share of food-away-from-home spending as the food in that channel receives additional processing and transportation along the supply chain to the final point of sale."
     - Definition change: "The broader definition of food used in the new methodology reduces the farm share reported by the Food Dollar from 12.3 cents to 11.8 cents in 2024".
     - Totals: consumers spent "$2.58 trillion on food"; domestically produced food "$2.17 trillion"; "Domestic farm establishments received $256.7 billion in 2024".
  2. Industry group bill. The 2024 chart, viewed, shows cents per food dollar:

     | Industry group | ¢ per food dollar |
     |---|---|
     | Food services | 38.6 |
     | Food processing | 16.1 |
     | Food retail | 13.8 |
     | Food wholesale | 6.3 |
     | Finance and insurance | 4.7 |
     | Transportation and storage | 4.1 |
     | Livestock | 3.3 |
     | Energy | 3.1 |
     | Agribusiness | 3.0 |
     | Crops | 2.5 |
     | Other | 4.5 |

     "Other" is forestry, fishing and agricultural services 0.9, legal and accounting 1.4, and advertising 2.2. Page text: value added by "transportation (-1.5 percent) decreased between 2023 and 2024."
  3. Returns to farm production.
     - "separating the total value added by farms (6.7 cents per food dollar in 2024) into crops (2.5 cents); livestock (3.3 cents); and forestry, fishing, and agricultural services (0.9 cents)."
     - "the gross return to farms (i.e., farm share) was 11.8 cents per food dollar, implying that farms purchased 5.1 cents (11.8 cent farm shares less 6.7 cents farm value added) of inputs per food dollar. Agribusiness, which represents all farm inputs not elsewhere classified into an industry group, was 3.0 cents, implying that all other industry groups collectively sold 2.1 cents of inputs to farms."
  4. Primary factor bill. Labour "received $1.17 trillion ... which was 54.1 cents per food dollar"; property income 32.7 cents; output taxes 7.2 cents.
- Criteria, inputs and data required (access paths, *verified* links):
  - Documentation / user's guide: /data-products/food-dollar/documentation.
  - Underlying data (Ag-FEDS): /data-products/food-dollar/underlying-data-ag-feds.
  - Update history.
  - 28 food-at-home product accounts with farm shares by account (chart on the page).
- Output produced (for the project):
  - *Reader computation:* all non-agribusiness industry groups together, transportation included, sold farms 2.1 cents of inputs per food dollar, against a farm gross share of 11.8 cents. So farm-purchased transportation is at most about 18% of farm gross receipts, and in reality a fraction of that, since energy, finance and others share the 2.1 cents.
  - Transportation and storage for the whole chain is 4.1 cents of the food dollar, most of it post-farm.
- Rationale and evidence base: official national input-output accounting (value-added basis).
- Assumptions, limitations, critiques:
  - Stated: "Values may not sum to 100 cents due to rounding"; the series was revised in 2026.
  - *Reader inference:*
    - These are national averages on a value-added basis. They show neither the freight cost per farm nor commodity-level transport shares (which need Ag-FEDS).
    - Transport performed with a farm's own trucks and labour sits inside farm value added and labour, not in "transportation".
    - *Reader knowledge (unverified):* grain buyers often embed freight in the basis they pay, which would not appear as a farm purchase of transportation.
- Key quotes: see above.

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- This is the first quantitative test of the origin hypothesis, and at national level it points against it. Transportation and storage are 4.1 cents of the whole food dollar. Farms buy at most 2.1 cents of all non-agribusiness inputs combined per 11.8 cents of gross receipts.
- Farmers' low share of the consumer dollar is driven by processing, food service and retail, not freight.
- The hypothesis could still hold for specific commodities, channels or regions: long-haul perishables, export grain, or produce sold into food service, where "additional processing and transportation" lower the farm share. So the next check is commodity-level Ag-FEDS data plus R34 (produce trucking) and the USDA Grain Transportation Report (rejected list in study_links.md).
- Methodologically, the three-bill idea (value by chain stage, by industry group, by factor) is a reusable way to locate where the cost pool sits in any candidate chain before choosing which node to serve.

## Read status: full (summary page and the industry-group-bill chart)
