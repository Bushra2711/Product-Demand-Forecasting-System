#!/usr/bin/env python3
"""
Simplified Forecasting Demo for TCS iON RIO Project
This demonstrates the core forecasting capabilities.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

def load_and_prepare_data():
    """Load and prepare data for forecasting."""
    print("Loading cleaned sales data...")
    
    try:
        # Load the cleaned data
        df = pd.read_csv('cleaned_sales_data.csv')
        print(f"Data loaded: {df.shape[0]:,} rows")
        
        # Create time series data for a few products
        products = ['Laptop Pro', 'Smartphone X', 'Wireless Headphones']
        
        time_series_data = []
        for product in products:
            product_data = df[df['Product_Name'] == product]
            
            for year in [2020, 2021, 2022, 2023]:
                for month in range(1, 13):
                    month_data = product_data[product_data['Year'] == year]
                    
                    if len(month_data) > 0:
                        avg_sales = month_data['Monthly_Sales'].mean()
                        time_series_data.append({
                            'Product_Name': product,
                            'Date': f"{year}-{month:02d}-01",
                            'Year': year,
                            'Month': month,
                            'Monthly_Sales': int(avg_sales)
                        })
        
        time_series_df = pd.DataFrame(time_series_data)
        time_series_df['Date'] = pd.to_datetime(time_series_df['Date'])
        
        print(f"Time series data created: {len(time_series_df)} records")
        return time_series_df, products
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def create_forecast_model(product_data):
    """Create a simple forecasting model for a product."""
    # Prepare features
    X = product_data[['Year', 'Month']].copy()
    X['Year_Normalized'] = (X['Year'] - 2020) / 3
    X['Sin_Month'] = np.sin(2 * np.pi * X['Month'] / 12)
    X['Cos_Month'] = np.cos(2 * np.pi * X['Month'] / 12)
    
    y = product_data['Monthly_Sales']
    
    # Fit model
    model = LinearRegression()
    model.fit(X, y)
    
    return model, ['Year', 'Month', 'Year_Normalized', 'Sin_Month', 'Cos_Month']

def make_predictions(model, features, product_data, months_ahead=12):
    """Make predictions for future months."""
    # Create future data points
    last_year = product_data['Year'].max()
    last_month = product_data['Month'].max()
    
    future_data = []
    for i in range(1, months_ahead + 1):
        month = (last_month + i) % 12
        if month == 0:
            month = 12
        year = last_year + ((last_month + i - 1) // 12)
        
        row = {'Year': year, 'Month': month}
        if 'Year_Normalized' in features:
            row['Year_Normalized'] = (year - 2020) / 3
        if 'Sin_Month' in features:
            row['Sin_Month'] = np.sin(2 * np.pi * month / 12)
        if 'Cos_Month' in features:
            row['Cos_Month'] = np.cos(2 * np.pi * month / 12)
        
        future_data.append(row)
    
    future_df = pd.DataFrame(future_data)
    predictions = model.predict(future_df[features])
    
    # Create forecast dates
    last_date = product_data['Date'].max()
    forecast_dates = pd.date_range(
        start=last_date + pd.DateOffset(months=1),
        periods=months_ahead,
        freq='ME'
    )
    
    return pd.DataFrame({
        'Date': forecast_dates,
        'Predicted_Sales': predictions
    })

def evaluate_model(model, features, product_data):
    """Evaluate model performance."""
    # Recompute engineered features to ensure columns exist
    base = product_data[['Year', 'Month']].copy()
    if 'Year_Normalized' in features:
        base['Year_Normalized'] = (product_data['Year'] - 2020) / 3
    if 'Sin_Month' in features:
        base['Sin_Month'] = np.sin(2 * np.pi * product_data['Month'] / 12)
    if 'Cos_Month' in features:
        base['Cos_Month'] = np.cos(2 * np.pi * product_data['Month'] / 12)

    # Make predictions on training data
    X = base[features]
    predicted = model.predict(X)
    actual = product_data['Monthly_Sales'].values
    
    # Calculate metrics
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    
    return mae, r2

def create_visualization(product_name, historical_data, predictions):
    """Create a simple visualization."""
    plt.figure(figsize=(10, 6))
    
    # Plot historical data
    plt.plot(historical_data['Date'], historical_data['Monthly_Sales'], 
            label='Historical Sales', color='blue', linewidth=2)
    
    # Plot predictions
    plt.plot(predictions['Date'], predictions['Predicted_Sales'], 
            label='Forecasted Sales', color='red', linewidth=2, linestyle='--')
    
    plt.title(f'Sales Forecast for {product_name}', fontsize=14, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Monthly Sales')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    filename = f'forecast_{product_name.replace(" ", "_")}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Forecast visualization saved as: {filename}")
    plt.show()

def main():
    """Main demo function."""
    print("=" * 60)
    print("TCS iON RIO - Simplified Forecasting Demo")
    print("=" * 60)
    
    # Load and prepare data
    time_series_data, products = load_and_prepare_data()
    
    if time_series_data is None:
        print("Failed to load data. Exiting.")
        return
    
    print(f"\nProducts to forecast: {products}")
    
    # Process each product
    for product in products:
        print(f"\n{'='*50}")
        print(f"Processing: {product}")
        print(f"{'='*50}")
        
        # Get product data
        product_data = time_series_data[time_series_data['Product_Name'] == product].copy()
        product_data = product_data.sort_values('Date')
        
        print(f"Data points: {len(product_data)}")
        print(f"Date range: {product_data['Date'].min()} to {product_data['Date'].max()}")
        
        # Create and fit model
        print("Creating forecasting model...")
        model, features = create_forecast_model(product_data)
        
        # Evaluate model
        mae, r2 = evaluate_model(model, features, product_data)
        print(f"Model Performance:")
        print(f"  Mean Absolute Error: {mae:.2f}")
        print(f"  R² Score: {r2:.3f}")
        
        # Make predictions
        print("Making predictions...")
        predictions = make_predictions(model, features, product_data, months_ahead=12)
        
        print(f"Forecast range: {predictions['Date'].min()} to {predictions['Date'].max()}")
        print(f"Predicted sales range: {predictions['Predicted_Sales'].min():.0f} - {predictions['Predicted_Sales'].max():.0f}")
        
        # Create visualization
        print("Creating visualization...")
        create_visualization(product, product_data, predictions)
        
        print(f"✅ {product}: Forecasting completed successfully!")
    
    print(f"\n🎉 FORECASTING COMPLETED FOR {len(products)} PRODUCTS!")
    print("✅ Milestone 2 achieved: Models fitted and predictions made")
    print("\n📊 Generated files:")
    for product in products:
        filename = f'forecast_{product.replace(" ", "_")}.png'
        print(f"  - {filename}")

if __name__ == "__main__":
    main()
