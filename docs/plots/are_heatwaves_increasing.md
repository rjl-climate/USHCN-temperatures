The [New York Times](https://www.nytimes.com/interactive/2023/climate/extreme-summer-heat.html) and other
sources claim that recent US heatwaves are not just a result of
typical summer weather but are significantly influenced by climate change. Heatwaves are increasing
frequency and intensity, they claim, and these increases are being driven by rising global temperatures.
Climate change has made such extreme heat events more likely and more severe than they would have
been without human impact.

So. Are heatwaves increasing in the US?

In this analysis, we define a heatwave as a period of at least 3 consecutive days where the
temperature at a station is above 90th percentile of temperatures at that location. We then
count the number of heatwave measurements per year and express it as a fraction of the total
measurement in the year.

As a confounding factor control measure, we remove all stations with less than 100 years of data.

**The number of heatwaves was highest in the 1930's, and has remained constant since then
at around 3.5% of the total number of measurements each year.**

![are_heatwaves_increasing.png](..%2Fimages%2Fare_heatwaves_increasing.png)

```python
{{include_file('are_heatwaves_increasing.py')}}
```
