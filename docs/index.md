# US Historical Climatology Network (USHCN) Data

**Is the weather getting worse?**

The [U.S. Historical Climatology Network](https://www.ncei.noaa.gov/products/land-based-station/us-historical-climatology-network#:~:text=U.S.%20Historical%20Climatology%20Network%20(USHCN)%20data%20are%20used%20to%20quantify,of%20long%2Dterm%20COOP%20stations) (
USHCN) is a dataset managed by the National
Climatic Data Center (NCDC), which is part of the National Oceanic and Atmospheric
Administration (NOAA). The USHCN provides high-quality, long-term temperature and
precipitation data from various weather stations across the United States. This data
is used to study climate trends and variations over time.

It's not easy to analyse, so I wrote a tool for doing so which you can obtain from
[GitHub](https://github.com/rjl-climate/US-Historical-Climate-Network-downloader)
or [crates.io](https://crates.io/crates/ushcn).

This repository contains python scripts for plotting processing USHCN datafiles
to evaluate the claim of an upward trend in temperature. I've created it to make the data available,
and to make the data source and methodology transparent.

In these pages, you can find information for [installing the data downloader](installation/downloader) tool,
and [installing the
plotting scripts](installation/scripts), so that you can recreate the analyses.