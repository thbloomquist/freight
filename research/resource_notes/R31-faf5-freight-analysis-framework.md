# R31 - Freight Analysis Framework Version 5 (FAF5)
- URL: https://faf.ornl.gov/faf5/ | Author: Bureau of Transportation Statistics (BTS) and Federal Highway Administration (FHWA); site developed by the National Transportation Research Center, Oak Ridge National Laboratory | Year: current version FAF5.7.1; page "Last modified: August 15, 2025" | Type: primary (government dataset) | Access:
  - The landing page and its file inventory were read in full from a curl download.
  - The "Summary Statistics" page (https://faf.ornl.gov/faf5/SummaryTable.aspx) returned only navigation, both to curl and to WebFetch, because its tables are rendered by the ASP.NET application and could not be driven.
  - The database files (327-706 MB zips) were not downloaded.
  - Accessed: 2026-09-14.
- Decision the resource addresses: candidate enumeration and sizing input (stages S1 and S3). It is data, not a method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context: "The Freight Analysis Framework (FAF) creates a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. The FAF integrates data from a variety of sources. Starting with data from the Commodity Flow Survey (CFS) and international trade data from the Census Bureau, FAF incorporates data from agriculture, extraction, utility, construction, service, and other sectors." *(verified)*
- Mechanism and steps (what it contains, verbatim): "The current version of FAF5 (FAF5.7.1) provides estimates for tonnage (unit: thousand tons), value (unit: million dollars), and ton-miles (unit: million ton-miles) by origin-destination pair of FAF regions, commodity type, and mode for the base year (2017), the recent years (2018 - 2024), the forecast year estimates (2030 - 2050), and the state level historical trend estimates (1997-2012)."
- Criteria, inputs and data required (access paths, *verified* as links on the page):
  - Data Tabulation Tool: https://faf.ornl.gov/faf5/dtt_total.aspx ("Create and download customizable FAF5 summary tables and charts").
  - Summary Statistics: https://faf.ornl.gov/faf5/SummaryTable.aspx.
  - Regional database files under https://faf.ornl.gov/faf5/Data/Download_Files/:

    | File | Contents | Size |
    |---|---|---|
    | FAF5.7.1.zip | 2017-2024 plus 2030-2050 mid-range | 505 MB (291 MB Access version) |
    | FAF5.7.1_HiLoForecasts.zip | adds high and low forecasts | 706 MB / 406 MB |
    | FAF5.7.1_2018-2024.zip | recent years only | 327 MB |

  - State-level equivalents (FAF5.7.1_State*.zip).
  - Metadata: data/FAF5_metadata.xlsx. User guide: "data/FAF5 User Guide.pdf". Zone crosswalk: "data/CFS area code - FAF5 zone id.xlsx".
  - Experimental county-level estimates: https://www.bts.gov/faf/county. Truck network flow assignment: FHWA FAF pages.
  - *Reader knowledge (unverified):* FAF commodities follow the 2-digit SCTG classes (about 42), and modes are truck, rail, water, air, multiple modes and mail, pipeline, and other/unknown. Check this against the metadata file before use.
- Output produced (for this project):
  - A ranked list of commodity × mode × origin-destination cells by value, tonnage and ton-miles, which is the raw material for enumerating candidate shipper groups (S1).
  - Growth outlook from the 2030-2050 forecasts (S3).
  - Geographic clustering of flows, which is useful for reachability (S4).
- Rationale and evidence base: official statistics, modelled from the CFS plus other sources, including the agriculture sector the CFS does not survey. *Reader inference:* this makes FAF the national source for farm-origin freight flows, because the CFS excludes farms (see R32).
- Assumptions, limitations, critiques:
  - *Reader inference:*
    - FAF gives freight flows (tons, value, ton-miles), not freight spend. Spend per candidate must be estimated as ton-miles or loads multiplied by rates from other sources (for example R34 for reefer produce).
    - It has no shipper-firm counts and no carrier-type split beyond mode.
    - Its figures are modelled estimates, not a survey of shippers.
  - No headline national totals could be retrieved here. The CFS headline numbers (R32) serve as the illustrative national scale.
- Key quotes: the two quoted passages above.

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- FAF is the widest enumeration base for the shipper side of a sub-market. It is the only federal flow dataset in the list that covers agricultural origins and imports alongside the CFS industries.
- It is the right tool to test, before interviews, whether a candidate commodity group (for example fresh produce by truck, grain by rail and barge) moves enough freight to matter.
- It says nothing about who the shippers are or which freight companies carry the flows. The shipper-industry pairing comes from R32, and the freight-company side from R33 and R44.
- Getting numbers out requires either driving the Data Tabulation Tool in a browser or downloading a zip of at least 300 MB and filtering it locally. The zips are standard CSV/Access files, so this is feasible.

## Read status: partial (landing page and file inventory read in full; summary tables app-rendered and not retrieved; data files not downloaded)
