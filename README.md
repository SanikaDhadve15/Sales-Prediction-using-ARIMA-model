#Sales-Prediction-using-ARIMA-model

ARIMA Sales Forecasting for Multi-Store, Multi-Item Sales Data This repository contains a time series analysis project using the ARIMA (AutoRegressive Integrated Moving Average) model to forecast 3 months of future sales for a dataset containing 50 items across 10 different stores.

#Objective
To predict sales trends and future demand, helping businesses make data-driven decisions about inventory and supply chain management. The notebook walks through the end-to-end pipeline of:
1.Exploratory Data Analysis (EDA)
2.Time Series Stationarity checks
3.ARIMA model fitting
4.Visualization of forecasts

#Features
1.Interactive Plotly visualizations for intuitive EDA
2.Seasonal decomposition to extract trend, seasonality, and residuals
3.Statistical tests for stationarity (ADF Test)
4.ACF and PACF plots for optimal ARIMA parameter selection
5.Time series forecasting using statsmodels ARIMA
6.Matplotlib and Plotly for static and interactive plotting


#Understanding ARIMA
The ARIMA model is widely used for time series forecasting and is defined by three key parameters:
1.AR (AutoRegressive): Regression of the variable against its own previous values (lags).
2.I (Integrated): Differencing of raw observations to make the time series stationary.
3.MA (Moving Average): Modeling the error term as a linear combination of error terms from the past.

The model is written as:
ARIMA(p, d, q)
Where:
p: Number of autoregressive terms
d: Number of differences to make the series stationary
q: Number of lagged forecast errors in the prediction

#Working:
1. Data Collection & Filtering
-The dataset is read using pandas.
-Store-wise and item-wise data is filtered (e.g., Store 1 and Item 1) for modeling.
-This allows us to model one series at a time, ensuring accuracy.

2. Exploratory Data Analysis (EDA)
-Line plots show how sales behave over time.
-EDA reveals trends, seasonality, and outliers.
-Interactive plots (via plotly) improve interpretability.

3. Decomposition of Time Series
We decompose the series into:
-Trend: Long-term progression
-Seasonality: Repeating patterns
-Residual: Random noise

4. Stationarity Check (ADF Test)
A stationary time series has constant mean and variance over time—required for ARIMA.
We use the Augmented Dickey-Fuller Test:
1.H₀ (Null Hypothesis): Time series is non-stationary
2.H₁ (Alternative Hypothesis): Time series is stationary
If p-value ≤ 0.05, we reject H₀ → the series is stationary.
If not, we difference the series (subtract previous values) to make it stationary.

5. Autocorrelation (ACF) and Partial Autocorrelation (PACF)
Used to determine ARIMA parameters:
1.ACF tells us how correlated a series is with its past values → helps estimate q
2.PACF isolates the effect of past lags → helps estimate p

6. ARIMA Model Fitting

7. Forecasting & Visualization
Forecasted values are compared against actual values to evaluate performance.

We use:
-Matplotlib: Static plots
-Plotly: Interactive plots

Visual insights help validate the model's accuracy and applicability.

8. Model Evaluation (Optional)
Metrics like RMSE (Root Mean Squared Error) or MAE (Mean Absolute Error) can be used to evaluate prediction performance.



