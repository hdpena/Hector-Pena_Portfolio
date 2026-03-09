# ⚡ EV Charging Station Utilization Analysis

A data analytics and predictive modeling project exploring **electric vehicle (EV) charging station usage patterns**, operational performance, and the factors influencing station utilization.

This project uses **Python, data visualization, and machine learning** to analyze EV charging infrastructure data and build an interpretable model for predicting station utilization.

---

## 📌 Project Overview

As electric vehicle adoption grows rapidly, efficient charging infrastructure is becoming critical for transportation systems. Understanding how charging stations are used can help operators improve service availability, pricing strategies, and infrastructure planning.

This project analyzes EV charging station data to identify patterns in:

- Charging demand
- Station utilization
- Pricing behavior
- Network performance
- Environmental and event impacts

The project combines **exploratory data analysis (EDA)** with **predictive modeling** to uncover insights and estimate utilization rates.

---

## 🎯 Objectives

The goals of this project are to:

- Analyze EV charging station usage patterns
- Understand utilization trends by **time of day, day of week, and month**
- Compare station performance across **charging networks**
- Explore how **pricing strategies affect utilization**
- Evaluate impacts of **weather conditions and local events**
- Build an **interpretable regression model** to predict station utilization

---

## 📊 Dataset Features

The dataset includes operational and contextual variables such as:

- `station_id`
- `station_name`
- `timestamp`
- `network`
- `city`
- `state`
- `location_type`
- `charger_type`
- `station_status`
- `pricing_type`
- `weather_condition`
- `local_event`
- `ports_total`
- `ports_available`
- `ports_occupied`
- `utilization_rate`
- `estimated_wait_time_mins`
- `avg_session_duration_mins`
- `current_price`
- `gas_price`
- `latitude`
- `longitude`
- `hour_of_day`
- `day_of_week`
- `month`

These features allow for analysis of both **operational performance** and **external influencing factors**.

---

## 🔎 Exploratory Data Analysis

The analysis includes:

- Data inspection and cleaning
- Missing value analysis
- Descriptive statistics
- Categorical feature exploration
- Utilization distribution analysis
- Network and charger type comparisons
- Temporal usage patterns
- Weather and event impact analysis
- Geographic visualization of stations
- Correlation analysis

---

## 📈 Key Visualizations

The notebook produces several visualizations including:

- Charging network distribution
- Charger type usage patterns
- Utilization rate histograms
- Hourly charging demand trends
- Hour vs. day heatmaps
- Price vs utilization scatter plots
- Utilization by weather condition
- Impact of local events on station demand
- Geographic station mapping
- Monthly and daily trend analysis
- Feature correlation matrix

These visualizations provide insight into **how EV infrastructure is used and what factors influence demand**.

---

## 🤖 Predictive Modeling

A regression model is built to predict **station utilization rate**.

### Model Approach

Two modeling approaches are implemented:

#### 1. Baseline Model
Uses only **numeric operational variables**.

#### 2. Enhanced Model
Includes both:

- Numeric variables
- Categorical variables (encoded)

### Model Pipeline

The model uses a **scikit-learn pipeline** including:

- Feature preprocessing
- One-hot encoding for categorical variables
- Standardization
- **SGDRegressor** for regression modeling

### Evaluation Metrics

Model performance is evaluated using:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

The project also includes:

- Residual analysis
- Predicted vs actual plots
- Feature importance interpretation

---

## 🛠 Tools and Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-Learn**
- **Jupyter Notebook**

---
