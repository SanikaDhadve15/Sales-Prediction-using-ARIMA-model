import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Load Historical Sales Data
@st.cache_data
def load_data():
    train_date = pd.date_range(start="2020-01-01", periods=2000, freq='D')
    test_date = train_date[1600:]
    train = np.sin(np.linspace(0, 50, 2000))  # Example train data
    test = np.sin(np.linspace(50, 100, 400))  # Example test data
    predictions = test + np.random.normal(scale=0.1, size=len(test))  # Example predictions
    return train_date, test_date, train, test, predictions

# Generate Future Sales Forecast (Example)
@st.cache_data
def generate_forecast():
    future_dates = pd.date_range(start="2025-01-01", periods=90, freq='D')
    store_ids = [f"Store {i+1}" for i in range(10)]
    item_ids = [f"Item {i+1}" for i in range(50)]

    # Create dummy forecasts (Replace with actual model predictions)
    forecast_data = []
    for store in store_ids:
        for item in item_ids:
            sales_forecast = np.abs(np.random.normal(loc=50, scale=10, size=90))  # Example sales data
            forecast_data.extend(zip([store] * 90, [item] * 90, future_dates, sales_forecast))

    forecast_df = pd.DataFrame(forecast_data, columns=["Store", "Item", "Date", "Predicted Sales"])
    return forecast_df

# Load Data
train_date, test_date, train, test, predictions = load_data()
forecast_df = generate_forecast()

# Streamlit UI
st.title(" Sales Forecasting and Prediction")

# Sidebar - Date Filter
st.sidebar.header("Filter Train Data by Date")
start_date = st.sidebar.date_input("Start Date", train_date[0].date())
end_date = st.sidebar.date_input("End Date", train_date[-1].date())

# Convert to pandas datetime for filtering
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter Train Data Based on Date Selection
filtered_indices = (train_date >= start_date) & (train_date <= end_date)
filtered_train_dates = train_date[filtered_indices]
filtered_train_values = train[filtered_indices]

# Sidebar Controls for Display Options
st.sidebar.header("Visualization Settings")
show_train = st.sidebar.checkbox("Show Train Data", True)
show_test = st.sidebar.checkbox("Show Actual Test Data", True)
show_predictions = st.sidebar.checkbox("Show Predictions", True)

# Store & Item Selection for Forecast
st.sidebar.header("Select Store & Item for Forecast")
selected_store = st.sidebar.selectbox("Select Store", forecast_df["Store"].unique())
selected_item = st.sidebar.selectbox("Select Item", forecast_df["Item"].unique())

# Filter forecast data for selected store & item
filtered_forecast = forecast_df[(forecast_df["Store"] == selected_store) & 
                                (forecast_df["Item"] == selected_item)]

# Create Plot
fig, ax = plt.subplots(figsize=(12, 6))

if show_train and len(filtered_train_dates) > 0:
    ax.plot(filtered_train_dates, filtered_train_values, color='green', label='Train Data')

if show_test:
    ax.plot(test_date, test, color='blue', label='Actual Test Data')

if show_predictions:
    ax.plot(test_date, predictions, color='red', linestyle='--', label='Predictions')

# Plot Forecasted Sales for Selected Store & Item
ax.plot(filtered_forecast["Date"], filtered_forecast["Predicted Sales"], 
        color='orange', linestyle='dotted', label=f'Forecast ({selected_store}, {selected_item})')

# Formatting
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Sales", fontsize=14)
ax.set_title("ARIMA Sales Forecasting", fontsize=16)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# Save the plot dynamically
plot_filename = "Arima.png"
plt.savefig(plot_filename, dpi=300, bbox_inches="tight")
st.pyplot(fig)

# Ensure the file exists before allowing download
if os.path.exists(plot_filename):
    with open(plot_filename, "rb") as file:
        st.sidebar.download_button("Download Plot", data=file, file_name=plot_filename, mime="image/png")

# Show Forecast Data
st.subheader(f"📊 3-Month Sales Forecast for {selected_store}, {selected_item}")
st.dataframe(filtered_forecast)
