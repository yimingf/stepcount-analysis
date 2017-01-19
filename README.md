# stepcount-analysis
step count analysis from apple health data.

this python script analysis step count features of me myself in Sweden (25/9 ~ 14/12/2016, 15 ~ 17/1/2017) and in China (23/5 ~ 24/9/2016, 15/12/2016 ~ 14/1/2017).

requirements
---

- numpy
- pandas
- python 2.7

procedures
---

- import data from my cell phone
- extract data from xml to csv-friendly form
- data cleanning. some meaningless data are dropped (thus effective steps are kept)
- mean/var analysis.

what is effective steps?
---

steps per minutes (spm) which are between 80 and 150.
why?

- less than 80 -> (random wandering at home) | (slow walks)
- greater than 150 -> overlapping data (i cannot achieve 150spm lol)

results
---

- spm in Sweden are 4% higher than what in China. (significance test passed)
- (effective) steps per day in Sweden are 10% less than what in China. (significance test not passed)
