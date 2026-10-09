# R34 - Agricultural Refrigerated Truck Quarterly (AgRTQ)
- URL: https://www.ams.usda.gov/services/transportation-analysis/agrtq | Author: USDA Agricultural Marketing Service; the PDF credits the "AMS Transportation Economics Division"; page contacts Kranti Mulik, Peter Caffarelli and Jesse Gastelle | Year: latest issue "Quarter 1, January-March 2026", "Published May 2026" | Type: primary (government report and dataset) | Access:
  - The landing page loads with curl and a browser user-agent.
  - The latest issue (https://www.ams.usda.gov/sites/default/files/media/RTQ1stQuarter2026.pdf) was downloaded and text-extracted. The table of contents and the national summary (pp. 1-3) were read.
  - Regional sections (U.S.-Mexico border, PNW, Arizona, California, Florida) and the truck-availability section were not read.
  - Accessed: 2026-09-14.
- Decision the resource addresses: sizing and cost data for one candidate sub-market (fresh fruit and vegetable shippers × refrigerated truckload carriers). It gives a price-volatility input for fee feasibility (L-FEE, CAMP "predictability") and evidence for the origin hypothesis (L-FARM). It is data, not a method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context (landing page, verbatim): "The Agricultural Refrigerated Truck Quarterly report (AgRTQ) provides a view of U.S. regional refrigerated truckload movements (with a rotating regional focus), in terms of volume and rates, to gauge the vital component of truck transportation applied to fresh fruit and vegetable markets." *(verified)*
- Mechanism and steps (report contents, verified from the table of contents):
  - National Summary: Quarterly Overview, U.S. Truck Rates, Truck Rates for Select Routes, U.S. Diesel Fuel Prices, Relationship Between Diesel Fuel and Truck Rates.
  - Quarterly Truck Availability.
  - Reported U.S. Shipments, and Reported Shipments by Select Commodities.
  - Regional Markets: U.S.-Mexico Border, PNW, Arizona, California, Florida.
  - Source line: "AMS Transportation Economics Division analysis of AMS Specialty Crops Program Market News data."
- Criteria, inputs and data required (access paths, *verified*):
  - Latest PDF (above).
  - Datasets: https://www.ams.usda.gov/services/transportation-analysis/agricultural-refrigerated-truck-quarterly-datasets.
  - Archive: https://www.ams.usda.gov/services/transportation-analysis/agrtq/archive.
  - AgTransport dashboards: https://agtransport.usda.gov/browse?q=refrigerated%20truck.
- Output produced: Q1 2026 figures *(verified, p. 2)*:
  - Volume: "USDA reported first quarter 2026 U.S. truck shipments of fresh produce were 7.76 million tons—up 1 percent from the previous quarter and down 10 percent from first quarter 2025."
  - Origins: Mexico 3.49 million tons (45%); PNW 1.63 million tons (21%); Arizona 635,000 (8%); California 470,000 tons (6%); Florida 447,000 tons (6%).
  - Commodities: "These top five commodities accounted for 42 percent of reported truck movements": potatoes 15%, apples 9%, dry onions 8%, avocados 6%, cucumbers 5%.
  - Average U.S. truck rates, Q1 2026 ($/mile): 0-500 miles 2.76; 501-1,500 miles 2.56; 1,501-2,500 miles 2.49; 2,501+ miles 1.50.
  - Table 1, the 501-1,500-mile series ($/mile): 2022 Q1 3.62 (peak quarters 3.62-3.68); 2023 Q1 2.84; 2024 Q1 2.69; 2025 Q4 2.23; 2026 Q1 2.56; 2017 Q1 1.85.
  - Methodological note: "Starting in 2025 Q1, 0-500 mile rates from regions in California to Los Angeles have not been reported, which significantly lowered the national average."
  - Diesel: "During first quarter 2025 [sic, context is 2026], the U.S. diesel fuel price averaged $4.06 per gallon".
- Rationale and evidence base: official USDA analysis of Market News rate and volume reports.
- Assumptions, limitations, critiques:
  - Stated: weighted regional rates; series breaks (the Los Angeles routes).
  - *Reader inference:*
    - These are corridor rate quotes, not what individual growers or shippers pay after contracts, accessorials or detention.
    - Fresh produce only.
    - Nothing on shipper margins, so the share of grower profit lost to freight cannot be computed from AgRTQ alone.
    - The rate series swings by roughly ±40% over a few years, which bears on any fee tied to "rate savings".
- Key quotes: see above.

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- AgRTQ is the most directly usable dataset for testing the farm lead quantitatively before committing. It gives volume by origin and commodity, a rate per mile by distance band, and a volatility history for the produce × reefer truckload sub-market. A candidate's annual freight bill can therefore be estimated as loads × miles × rate.
- The 45% Mexico share says much of this sub-market is cross-border. The shipper side is often an importer or distributor at the border, not a US grower.
- For fee design, the rate volatility means savings measured against "last year's rate" would be unpredictable and hard to attribute (R25 CAMP), which points to savings measured per shipment against a same-day benchmark instead.
- It does not show that farmers lose most of their profit to shipping. It only prices the truck leg.

## Read status: partial (landing page in full; Q1 2026 PDF table of contents and national summary pp. 1-3; regional and availability sections not read)
