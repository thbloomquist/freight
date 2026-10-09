# R33 - U.S. 3PL Market Size Estimates
- URL: https://www.3plogistics.com/3pl-market-info-resources/3pl-market-information/us-3pl-market-size-estimates/ | Author: Armstrong & Associates, Inc. (A&A) | Year: 2025 data; page "(updated April 20, 2026)"; series since 1994 | Type: primary (industry-analyst estimates) | Access: free summary page read in full from a curl download | Accessed: 2026-09-14
- Decision the resource addresses: candidate enumeration (a taxonomy of the freight-company, or intermediary, side) and sizing (S1 and S3). It also supplies a fee-model precedent (lens L-FEE). It is data, not a selection method.

## Strategies or frameworks described

### How the dataset serves the selection process
- Origin and intended context: "The U.S. Third-Party Logistics (3PL)/Contract Logistics market reached $323.4 billion in 2025, up 5.0% year-over-year. Since 1994, Armstrong & Associates has been estimating the size of the U.S. 3PL market and its segments." *(verified)*
- Mechanism and steps: segment gross revenues, 2025 (US$ billions, verbatim table):

  | Segment | 2025 gross revenue |
  |---|---|
  | Domestic Transportation Management (DTM) | 128.3 |
  | International Transportation Management (ITM) | 85.9 |
  | Value-Added Warehousing and Distribution (VAWD) | 72.7 |
  | Dedicated Contract Carriage (DCC) | 32.0 |
  | Contract Software/Systems | 4.5 |
  | **Total** | **323.4** |

  The four "main" segments sum to $318.9B. The $323.4B total includes the $4.5B software row.
- Criteria, inputs and data required: segment definitions (verbatim, shortened):
  - DCC: "Third-party logistics providers offering dedicated contract carriage services to customers through agreements typically having one to seven-year terms ... asset-based truckload transportation."
  - VAWD: "long-term contract warehousing and distribution center management, and various value-added services ... VAWD does not include short-term 'Public' warehousing."
  - ITM: "international air and ocean transportation management services ... freight forwarding, warehousing, container freight station operations, trade compliance, customs brokerage, and inland shipment management."
  - DTM: "non-asset-based transportation management services ... typically performed with freight brokerage ... The DTM ... sub-segments include Freight Brokerage, Intermodal, Managed Transportation, and Last-Mile Delivery."
  - DTM/Freight Brokerage: "Business is conducted via phone, email, or interfaces between a shipper's systems, freight broker's Transportation Management System (TMS), and carrier TMS ... The freight broker generates a gross profit or loss on each shipment managed, the difference between gross revenue from a shipper and purchased transportation paid to a carrier."
  - DTM/Managed Transportation: "manages transportation between shippers and carriers within North America using a systems-based TMS and automation/optimization approach for transportation planning, carrier selection, tendering, and routing (transportation execution), and in-transit visibility ... Revenues are typically generated via a management fee, such as a flat amount per shipment or a percent of the purchased transportation. They may include gainshares where transportation savings are shared between the shipper and 3PL."
  - DTM/Last-Mile Delivery: shipments "from the last warehouse or terminal to the final consignee", covering B2B or B2C, usually with "independent contractor drivers or freight brokerage-managed shipments".
- Output produced: a named, sized list of intermediary types that can fill the freight-company column of a candidate sub-market, plus an existing fee precedent. Gainsharing is already an established revenue model in managed transportation.
- Rationale and evidence base:
  - A long-running analyst series (since 1994).
  - The method is not disclosed on the page, and A&A sells the underlying research.
  - A use statement restricts reproduction: "Armstrong & Associates, Inc. must be predominantly displayed as the source".
- Assumptions, limitations, critiques:
  - *Reader inference:*
    - These are gross revenues, including purchased transportation passed through to carriers, so they overstate the intermediaries' own margin and any software budget.
    - There are no firm counts, so fragmentation must come from R44 (NAICS 488510 and 493).
    - The scope is 3PLs only. Asset carriers outside DCC and shippers' in-house logistics are not covered.
- Key quotes: the market total and the Managed Transportation definition above.

## Reader's judgement on relevance to a two-sided freight sub-market choice
*Judgement:*
- R33 is the cleanest taxonomy of the intermediary side: brokerage, intermodal, managed transportation, last-mile, forwarding and customs, warehousing and dedicated carriage. It can serve directly as the column headings of the S1 enumeration matrix.
- Its most important line for this project is the managed-transportation fee model: "a percent of the purchased transportation ... gainshares where transportation savings are shared between the shipper and 3PL". This shows that shippers already pay freight intermediaries out of measured transportation savings, which supports the project's fee constraint.
- It also shows who the incumbent collectors of that fee are. A software entrant would compete with, or sell to, managed-transportation 3PLs.

## Read status: full (free summary page)
