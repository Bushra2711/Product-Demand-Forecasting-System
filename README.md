# 🚀 TCS iON RIO - Sales Forecasting System

## 📋 Project Overview

This project implements a comprehensive **Demand Forecasting System** for retail outlets based on historical sales data. The system predicts product demand using advanced forecasting models and machine learning techniques.

## 🎯 Project Objectives

- ✅ Create a dataset of 200,000 entries containing sales data for 4 years (2020-2023)
- ✅ Clean and sanitize the dataset
- ✅ Choose appropriate forecasting models for different products
- ✅ Fit models to the dataset
- ✅ Make predictions for all products

## 📊 Dataset Structure

The system works with sales data containing:
- **Product Name**: 20 different technology products
- **Cost**: Product pricing information
- **Year**: Sales year (2020-2023)
- **Monthly Sales**: Monthly sales volume

## 🏗️ Project Architecture

### 1. Data Generation (`sales_dataset_generator.py`)
- Generates 200,000 synthetic sales records
- Implements realistic business patterns (seasonality, trends)
- Creates balanced dataset across products and time periods

### 2. Data Cleaning (`data_cleaner.py`)
- **Milestone 1 Implementation**
- Loads and explores raw data
- Removes missing values and outliers
- Sanitizes data for analysis
- Converts to time series format

### 3. Forecasting System (`forecasting_system.py`)
- **Milestone 2 Implementation**
- Chooses appropriate forecasting models
- Fits models to cleaned dataset
- Makes predictions for future periods
- Evaluates model performance

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- Working internet connection
- Any decent IDE (VS Code, PyCharm, etc.)

### Installation Steps

1. **Clone or download the project files**
2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Required Packages
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning models
- `matplotlib` & `seaborn` - Data visualization
- `statsmodels` - Time series analysis
- `prophet` - Advanced forecasting
- `xgboost` & `lightgbm` - Gradient boosting models

## 🚀 Usage Instructions

### Step 1: Generate Dataset (if needed)
```bash
python sales_dataset_generator.py
```
This creates `sales_dataset_200k.csv` with 200,000 entries.

### Step 2: Clean and Sanitize Data
```bash
python data_cleaner.py
```
This implements **Milestone 1**:
- Loads the dataset
- Explores data structure
- Cleans and sanitizes data
- Saves cleaned data as `cleaned_sales_data.csv`

### Step 3: Run Forecasting System
```bash
python forecasting_system.py
```
This implements **Milestone 2**:
- Chooses appropriate forecasting models
- Fits models to the dataset
- Makes predictions for all products
- Generates visualizations

## 📈 Forecasting Models

The system automatically selects the most appropriate model for each product:

### 1. **Holt-Winters Exponential Smoothing**
- Used for products with strong seasonality
- Captures trend and seasonal patterns
- Best for products with clear business cycles

### 2. **Linear Regression with Seasonal Features**
- Used for products with moderate seasonality
- Incorporates sine/cosine seasonal components
- Good for products with gradual trends

### 3. **Simple Linear Regression**
- Used for products with minimal seasonality
- Captures basic trend patterns
- Efficient for stable products

## 📊 Model Selection Logic

The system automatically analyzes each product's data to determine:
- **Seasonal Strength**: Measures how much sales vary by month
- **Trend Patterns**: Identifies long-term growth/decline
- **Data Quality**: Ensures sufficient data for modeling

## 🎯 Project Milestones

### ✅ Milestone 1 (Day 5): Data Preparation
- [x] Dataset creation with 200,000 entries
- [x] Data cleaning and sanitization
- [x] Time series data preparation

### ✅ Milestone 2 (Day 15): Forecasting Implementation
- [x] Model selection and fitting
- [x] Predictions for all products
- [x] Performance evaluation

## 📁 Project Deliverables

1. **Source Code Repository** ✅
   - Complete Python implementation
   - Modular, well-documented code
   - Professional coding standards

2. **Dataset** ✅
   - 200,000 sales records
   - 4 years of historical data
   - 20 different products

3. **Forecasting System** ✅
   - Multiple forecasting models
   - Automatic model selection
   - Comprehensive predictions

4. **Visualizations** ✅
   - Data analysis plots
   - Forecast visualizations
   - Performance metrics

## 🔍 Key Features

### Intelligent Model Selection
- Automatically analyzes data characteristics
- Chooses best forecasting approach
- Handles different product patterns

### Comprehensive Data Processing
- Robust outlier detection
- Missing value handling
- Data type validation

### Professional Output
- High-quality visualizations
- Detailed performance metrics
- Exportable results

## 📊 Sample Output

The system generates:
- Cleaned dataset files
- Forecast visualizations for each product
- Model performance reports
- Prediction summaries

## 🎓 Learning Outcomes

This project demonstrates:
- **Data Science Workflow**: From raw data to predictions
- **Time Series Analysis**: Understanding temporal patterns
- **Model Selection**: Choosing appropriate algorithms
- **Business Intelligence**: Converting data to actionable insights

## 🔮 Future Enhancements

Potential improvements:
- Real-time data integration
- Advanced ensemble methods
- Interactive dashboards
- API endpoints for predictions

## 📞 Support & Contact

For questions or issues:
- Review the code documentation
- Check error messages for troubleshooting
- Ensure all dependencies are installed

## 📜 License

This project is created for educational purposes as part of the TCS iON RIO program.

---

**🎉 Congratulations! You've successfully implemented a complete Sales Forecasting System that meets all TCS iON RIO project requirements!**
