import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the cpi fah forecast dataset
df = pd.read_pickle("cpi_fah_dataset.pkl")

# function for drawing the input charts
def plot_yoy_history(series, selected_value, title):
    fig, ax = plt.subplots(figsize=(5, 2))
    ax.plot(series.index, series, color='steelblue', linewidth=2)
    ax.axhline(selected_value, color='red', linestyle='--', label=f"Selected: {selected_value}%")
    ax.set_title(title, fontsize=10)
    ax.set_ylabel("% YoY", fontsize=8)
    ax.tick_params(labelsize=8)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend(fontsize=7)
    return fig

# --- Simulate pretrained model posterior (placeholder) ---
# Replace these with real posterior samples
np.random.seed(42)
num_samples = 4000
intercept_samples = np.random.normal(0.3, 0.1, num_samples)
coefs_samples = np.random.normal(
    loc=np.array([0.01, 0.05, 0.25, 0.2, -0.05]).reshape(5, 1),
    scale=np.array([0.005, 0.01, 0.02, 0.015, 0.01]).reshape(5, 1),
    size=(5, num_samples)
)

# --- User Interface ---
st.title("🛒 CPI Food-at-Home Scenario Explorer")
st.write("Adjust Year-over-Year (%) changes for key drivers and view CPI FAH forecast distribution.")

st.info("""
    ***How to Use and Interpret This Dashboard***
    
    • All input values are set to 0 initially.  As a result, the initial CPI Food-at-Home is the value if all input values grew at 0 percent, which is the model's y-intercept.
    
    • The **dropdown values** represent **Year-over-Year (%) changes** for each driver. It holds that change steady across **each of the next six forecast months**.
    
    • For example, selecting **10% for Oil Prices YoY** means you are assuming oil prices are 10% higher than the same month last year, consistently for the next 6 months.
    
    • The histogram below shows the forecasted CPI FAH distribution based on your selections.
    
    • The four time series charts below show the trend for each input into the model.
    
    """)

latest_values = df[["Oil Prices YoY (%)", "PPI Farm Products YoY (%)", "PPI Food Mfg YoY (%)", "PPI Grocery YoY (%)"]].iloc[-1]

col1, col2 = st.columns(2)
with col1:
    oil_yoy = st.slider("Oil Prices YoY (%)", min_value=-20, max_value=100, value=float(latest_values["Oil Prices YoY (%)"]), step=1)
    farm_yoy = st.slider("PPI Farm Products YoY (%)", min_value=-20, max_value=40, value=float(latest_values["PPI Farm Products YoY (%)"]), step=1)

with col2:
    food_mfg_yoy = st.slider("PPI Food Mfg YoY (%)", min_value=-5, max_value=15, value=float(latest_values["PPI Food Mfg YoY (%)"]), step=1)
    grocery_yoy = st.slider("PPI Grocery YoY (%)", min_value=-3, max_value=20, value=float(latest_values["PPI Grocery YoY (%)"]), step=1)

# Control variable (held constant)
grocery_units_yoy = 0.0  # used but not exposed to user

# --- Build X_future row ---
X_input = np.array([oil_yoy, farm_yoy, food_mfg_yoy, grocery_yoy, grocery_units_yoy])

# --- Forecast using Bayesian posterior ---
pred_samples = intercept_samples + np.dot(X_input, coefs_samples)

# --- Display Results ---
st.subheader("📈 Forecast Distribution")
threshold = 4
col_chart, col_metric = st.columns([4, 1])  # wider chart, narrower metric
st.write(f"Mean CPI FAH: **{pred_samples.mean():.2f}%**, 90% CI: [{np.percentile(pred_samples, 5):.2f}%, {np.percentile(pred_samples, 95):.2f}%]")

with col_chart:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(pred_samples, bins=50, color='skyblue', edgecolor='gray', alpha=0.8)
    ax.axvline(threshold, color='red', linestyle='--', label=f'{threshold}% Threshold')
    ax.axvline(pred_samples.mean(), color='black', linestyle='-', label='Mean Forecast')
    ax.set_title("Posterior Predictive Distribution")
    ax.set_xlabel("CPI FAH YoY (%)")
    ax.legend()
    st.pyplot(fig)

with col_metric:
    st.markdown("###")  
    st.metric(label=f"P(CPI ≤ {threshold}%)", value=f"{(pred_samples <= threshold).mean():.1%}")

# ------Insert Input Charts with function call -------------------
# Filter df to only the last 5 years
ten_years_ago = pd.Timestamp.today() - pd.DateOffset(years=10)

# Filter the DataFrame to the last 10 years
recent_df = df[df.index >= ten_years_ago]

st.subheader("📉 Historical Trends (Last 10 Years)")

col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_yoy_history(recent_df['oil_prices_yoy_lag6'], oil_yoy, "Oil Prices YoY (%)"))
    st.pyplot(plot_yoy_history(recent_df['ppi_farm_products_yoy_lag2'], farm_yoy, "PPI Farm Products YoY (%)"))

with col2:
    st.pyplot(plot_yoy_history(recent_df['ppi_food_mfg_yoy_lag5'], food_mfg_yoy, "PPI Food Mfg YoY (%)"))
    st.pyplot(plot_yoy_history(recent_df['ppi_grocery_yoy_lag1'], grocery_yoy, "PPI Grocery YoY (%)"))

