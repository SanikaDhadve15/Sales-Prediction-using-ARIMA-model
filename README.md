
#  Sales Prediction using ARIMA Model

**ARIMA Sales Forecasting for Multi-Store, Multi-Item Sales Data**  
This repository contains a time series analysis project using the **ARIMA (AutoRegressive Integrated Moving Average)** model to forecast **3 months of future sales** for a dataset containing **50 items** across **10 different stores**.



##  Objective

To predict sales trends and future demand, helping businesses make data-driven decisions about inventory and supply chain management.

The notebook walks through the end-to-end pipeline of:
1. Exploratory Data Analysis (EDA)
2. Time Series Stationarity Checks
3. ARIMA Model Fitting
4. Visualization of Forecasts



##  Features

-  Interactive **Plotly** visualizations for intuitive EDA  
-  Seasonal decomposition to extract **trend**, **seasonality**, and **residuals**  
-  Statistical tests for stationarity (**ADF Test**)  
-  **ACF** and **PACF** plots for optimal ARIMA parameter selection  
-  Time series forecasting using `statsmodels` **ARIMA**  
-  **Matplotlib** and **Plotly** for static and interactive plotting  



##  Understanding ARIMA

The **ARIMA** model is widely used for time series forecasting and is defined by three key parameters:

- **AR (AutoRegressive)**: Regression of the variable against its own previous values (lags).
- **I (Integrated)**: Differencing of raw observations to make the time series stationary.
- **MA (Moving Average)**: Modeling the error term as a linear combination of past errors.

**Model notation:**
```
ARIMA(p, d, q)
```
Where:
- `p`: Number of autoregressive terms  
- `d`: Number of differences to make the series stationary  
- `q`: Number of lagged forecast errors in the prediction  



##  Working

### 1.  Data Collection & Filtering

- Dataset is loaded using **pandas**
- Data is filtered store-wise and item-wise (e.g., Store 1 and Item 1)
- This allows modeling one series at a time for higher accuracy



### 2.  Exploratory Data Analysis (EDA)

- Line plots visualize sales trends over time
- EDA helps detect **trends**, **seasonality**, and **outliers**
- **Interactive Plotly charts** improve interpretability



### 3.  Decomposition of Time Series

The series is decomposed into:
- **Trend**: Long-term movement
- **Seasonality**: Repeating short-term cycle
- **Residual**: Irregular or random component


### 4.  Stationarity Check (ADF Test)

To ensure the series is stationary—a requirement for ARIMA.

**Augmented Dickey-Fuller Test:**

- **H₀ (Null Hypothesis)**: Series is **non-stationary**
- **H₁ (Alternative Hypothesis)**: Series is **stationary**

If `p-value ≤ 0.05`: Reject H₀ → The series is stationary  
 Otherwise: Difference the series (e.g., subtract previous value) to make it stationary


### 5.  ACF and PACF Analysis

Used to determine ARIMA parameters:

- **ACF (AutoCorrelation Function)**:  
  Tells how the series is correlated with past lags → helps determine `q`

- **PACF (Partial ACF)**:  
  Shows influence of past values after removing earlier lags → helps determine `p`


### 6.  ARIMA Model Fitting

Using the determined parameters (`p`, `d`, `q`), the model is fitted:


### 7.  Forecasting & Visualization

- Forecasted values are generated for the next 3 months
- Predictions are visualized and compared with actual data

**Tools:**
- `matplotlib`: For static visualizations
- `plotly`: For interactive plots

These visualizations help validate model performance.


### 8.  Model Evaluation (Optional)

Evaluate performance using:
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**

These metrics give insight into forecast accuracy.

link: https://wj6fofmgbqm8d2gfvqdeiz.streamlit.app/

