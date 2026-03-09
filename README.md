# ❤️ Heart Attack Risk Analysis


## 📊 Project Overview

This project analyzes cardiovascular health data to identify **key predictors of heart attack risk** using Python and machine learning. The analysis includes **data cleaning, exploratory data analysis (EDA), and predictive modeling using logistic regression**.

The goal of this project is to demonstrate **practical data science and healthcare analytics skills**, including building interpretable models that help understand the factors contributing to cardiovascular disease risk.

This project was completed as part of **DSC 680 – Data Science at Bellevue University**.

---

# 📁 Dataset

The dataset used in this project:

It contains multiple patient health indicators used to evaluate cardiovascular risk.

### Key Variables

* Age
* Blood Pressure
* Cholesterol Levels
* Body Measurements
* Lifestyle Indicators
* Medical History Variables
* Heart Attack Risk (Target Variable)

These variables help analyze relationships between **health indicators and cardiovascular outcomes**.

---

# ⚙️ Project Workflow

The project follows a standard **data science pipeline**:

```
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Scaling
        ↓
Train/Test Split
        ↓
Logistic Regression Model
        ↓
Model Evaluation
```

---

# 🔍 Exploratory Data Analysis

Exploratory analysis was conducted to understand:

* Feature distributions
* Correlations between health indicators
* Potential predictors of heart attack risk
* Data quality issues such as missing values or duplicates


Common visualizations include:

* Distribution plots
* Correlation heatmaps
* Feature comparisons

---

# 🧹 Data Preprocessing

Before modeling, the dataset was prepared through:

* Duplicate detection and removal
* Missing value inspection
* Feature scaling using **StandardScaler**
* Splitting the dataset into **training and testing sets**

---

# 🤖 Predictive Modeling

A **Logistic Regression model** was implemented to predict the probability of heart attack risk.

### Model Training

---

# 📈 Model Evaluation

Model performance was evaluated using:

* **Accuracy Score**
* **Confusion Matrix**


These metrics help assess how well the model correctly classifies individuals at risk for heart attack.

---

# 🧰 Technologies Used

| Tool             | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Core programming language             |
| Pandas           | Data manipulation and analysis        |
| NumPy            | Numerical computing                   |
| Matplotlib       | Data visualization                    |
| Seaborn          | Statistical visualization             |
| Scikit-learn     | Machine learning modeling             |
| Jupyter Notebook | Interactive data analysis environment |


# 💡 Key Questions Explored

This project investigates questions such as:

* Which health factors are most associated with heart attack risk?
* Can machine learning predict cardiovascular risk accurately?
* What patterns exist in patient health data?

---

# 🚀 Future Improvements

Potential improvements for the project include:

* Feature engineering for improved model performance
* Testing additional models such as Random Forest or Gradient Boosting
* ROC curves and precision-recall evaluation
* Model explainability using SHAP values
* Creating an interactive dashboard
* Deploying the model as a web application

---
