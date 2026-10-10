# 14_fuel_tables_and_index

Generated from `data/catalogue.csv` on 2026-10-09. One line per file; the catalogue row holds the full record.

| file_id | file | case / origin | doc no. | doc types | checks evidenced | real? | mode | dates | pages | text | URL | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14-071 | `doe_atlas_2025_fuel_surcharge_matrix.pdf` | DOE |  | fuel_table | B8|B9 | real | both | 2025-01–2025-12 | 1 | yes | https://atlas.doe.gov/RateRoute/FuelSurcharge/2025CurrentFSCMatrix.pdf | Weekly LTL % and TL $/mile |
| 14-072 | `gsa_fuel_surcharge_2021-10-01.pdf` | GSA |  | fuel_table | B8|B9 | template | both | 2021-10-01– | 2 | yes | https://www.gsa.gov/system/files/Fuel%20Surcharge%20(effective%2010-1-21).pdf |  |
| 14-073 | `fedex_freight_fuel_surcharge_2025-06-09.pdf` | FedEx Freight |  | fuel_table | B8|B9 | template | LTL | 2025-06-09– | 11 | yes | https://www.fedexfreight.com/content/dam/web/us/documents/fuel-surcharge-effective6-9-25.pdf |  |
| 14-074 | `eia_weekly_diesel_EMD_EPD2D_PTE_NUS_DPGw.xls` | EIA |  | other | B8 | real | both | 1994–2026 |  | na | https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2D_PTE_NUS_DPGw.xls | US on-highway diesel, weekly; the index most fuel tables key on |
| 14-075 | `FedExFreight_FTL_fuel_surcharge.pdf` |  |  | fuel_table | B8 fuel level|B9 fuel base | template | TL | – | 4 | yes | https://www.fedexfreight.com/content/dam/web/us/documents/fs-ftl-fuel-surcharge.pdf | Truckload fuel surcharge rule and DOE-index table (set Monday, effective Tuesday). Wayback captures for the historical LTL tables could not be fetched (archive.org offline/429 all session). |
| 14-076 | `estes_fuel_20230327172633.html` | Estes |  | fuel_table | B8 | template | both | 2023-03-27–2023-03-27 |  | na | https://web.archive.org/web/20230327172633id_/https://www.estes-express.com/resources/fees-and-surcharges/fuel-surcharge | Only archived carrier fuel page found for 2020-2024: Wayback availability API shows no 2023-24 snapshots for the ABF, SEFL, ODFL, XPO or Saia fuel pages (probed 2026-10-09); CDX API returned 429 all day |
