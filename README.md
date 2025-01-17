# US Historical Climatology Network data

**The climate catastrophe hypothesis predicts that an increasing atmospheric concentration of
CO2 will produce a catastrophic increase in the earth's temperature.**

![USHCN data](docs/images/are_hotter_days_increasing.png)

The [U.S. Historical Climatology Network](https://www.ncei.noaa.gov/products/land-based-station/us-historical-climatology-network#:~:text=U.S.%20Historical%20Climatology%20Network%20(USHCN)%20data%20are%20used%20to%20quantify,of%20long%2Dterm%20COOP%20stations) (
USHCN) is a dataset managed by the National
Climatic Data Center (NCDC), which is part of the National Oceanic and Atmospheric
Administration (NOAA). The USHCN provides high-quality, long-term temperature and
precipitation data from various weather stations across the United States. This data
is used to study climate trends and variations over time. We can use this data to evaluate the
climate catastrophe hypothesis.

This repository contains python scripts for processing and plotting USHCN datafiles
to evaluate the claim of an upward trend in temperature. The datafiles are generated by
a companion application [available here](https://crates.io/crates/ushcn) that downloads the latest USHCN datafiles
from the USHCN FTP site.

The individual scripts are located in the `plots` directory. The results are presented in
the [documentation](https://rjl-climate.github.io/USHCN-temperatures/
), which presents the plots and a brief analysis of the results, together
with the script that was used to produce it. The purpose of this is to ensure the maximum transparency
and reproducibility of the results.

I welcome any comments or suggestions for improvement. In particular, if you believe that there is
a material error in the analysis, please let me know. If I agree, I will correct it and update the plot
with the new data.

**Licence: MIT**

## Change log

- 2024-07-21 - Add "Are Heatwaves Increasing?" analysis
- 2024-07-20 - Initial release

