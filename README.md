# cpi_fah_fcst
CPI Food-at-Home Forecast

This forecasts CPI food-at-home

The dependent variable is CPI food-at-home
THe independent vars are...
1) West Texas Intermediate oil prices
2) ppi farm products
3) ppi food manufacture
4) ppi grocery
5) grocery units

* The code uses OLS regression to predict the CPI food-at-home six months forward
* Six months was selected because the ppi data is a about a six month leading indicator
* The code validates the model by holding out 24 months of data and then running six month rolling holdouts
* THe code then forecasts the next six months forward
