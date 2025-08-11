#!/usr/bin/env python3
"""
TCS iON RIO Sales Forecasting System - Demo Script
This script demonstrates the complete workflow of the forecasting system.
"""

import os
import sys
import pandas as pd

def check_files():
    """Check if all required files exist."""
    print("🔍 Checking project files...")
    
    required_files = [
        'sales_dataset_generator.py',
        'data_cleaner.py', 
        'forecasting_system.py',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️ Missing files: {missing_files}")
        return False
    
    print("\n✅ All required files found!")
    return True

def check_dataset():
    """Check if the dataset exists and show its properties."""
    print("\n📊 Checking dataset...")
    
    if os.path.exists('sales_dataset_200k.csv'):
        try:
            df = pd.read_csv('sales_dataset_200k.csv')
            print(f"✅ Dataset found: {df.shape[0]:,} rows × {df.shape[1]} columns")
            print(f"📅 Year range: {df['Year'].min()} - {df['Year'].max()}")
            print(f"🏷️ Products: {df['Product_Name'].nunique()}")
            print(f"💰 Cost range: ${df['Cost'].min():.2f} - ${df['Cost'].max():.2f}")
            print(f"📈 Sales range: {df['Monthly_Sales'].min():,} - {df['Monthly_Sales'].max():,}")
            
            # Show sample data
            print(f"\n📋 Sample data:")
            print(df.head(3).to_string(index=False))
            
            return True
        except Exception as e:
            print(f"❌ Error reading dataset: {e}")
            return False
    else:
        print("❌ Dataset not found. Run sales_dataset_generator.py first.")
        return False

def run_data_generation():
    """Run the data generation process."""
    print("\n🚀 Running data generation...")
    
    try:
        import sales_dataset_generator
        print("✅ Data generation completed!")
        return True
    except Exception as e:
        print(f"❌ Error in data generation: {e}")
        return False

def run_data_cleaning():
    """Run the data cleaning process."""
    print("\n🧹 Running data cleaning...")
    
    try:
        import data_cleaner
        print("✅ Data cleaning completed!")
        return True
    except Exception as e:
        print(f"❌ Error in data cleaning: {e}")
        return False

def run_forecasting():
    """Run the forecasting system."""
    print("\n🔮 Running forecasting system...")
    
    try:
        import forecasting_system
        print("✅ Forecasting completed!")
        return True
    except Exception as e:
        print(f"❌ Error in forecasting: {e}")
        return False

def main():
    """Main demo function."""
    print("🚀 TCS iON RIO - Sales Forecasting System Demo")
    print("=" * 60)
    
    # Check project structure
    if not check_files():
        print("\n❌ Project setup incomplete. Please ensure all files are present.")
        return
    
    # Check dataset
    if not check_dataset():
        print("\n📊 Generating dataset...")
        if not run_data_generation():
            print("❌ Failed to generate dataset.")
            return
    
    # Check if cleaned data exists
    if not os.path.exists('cleaned_sales_data.csv'):
        print("\n🧹 Cleaning data...")
        if not run_data_cleaning():
            print("❌ Failed to clean data.")
            return
    
    # Run forecasting
    print("\n🔮 Running forecasting system...")
    if not run_forecasting():
        print("❌ Failed to run forecasting.")
        return
    
    print("\n🎉 Demo completed successfully!")
    print("\n📋 Project Status:")
    print("   ✅ Milestone 1: Dataset created, cleaned, and sanitized")
    print("   ✅ Milestone 2: Models chosen, fitted, and predictions made")
    print("\n🎊 All TCS iON RIO project requirements have been met!")

if __name__ == "__main__":
    main()
