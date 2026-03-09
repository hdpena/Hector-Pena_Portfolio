# 🏠 Home Price Prediction  
### Exploratory Data Analysis and Regression Modeling

This project demonstrates a complete data science workflow for predicting housing prices using exploratory data analysis (EDA), feature engineering, and multiple regression models. The goal is to understand which housing features most strongly influence price and to build predictive models that estimate home values.

---

# 📊 Project Overview

Housing prices are influenced by many factors such as property size, number of rooms, location characteristics, and the age of the home. This project analyzes a housing dataset and applies machine learning techniques to predict `House_Price`.

The notebook walks through the full analytical pipeline:

- Data inspection and cleaning  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Data preprocessing and scaling  
- Model training  
- Model evaluation and comparison  

The project is designed as a **portfolio-ready machine learning analysis for housing price prediction**.

---

# 📂 Dataset Features

The dataset contains several variables that describe housing characteristics:

| Feature | Description |
|------|-------------|
| Square_Footage | Total living space of the home |
| Num_Bedrooms | Number of bedrooms |
| Num_Bathrooms | Number of bathrooms |
| Year_Built | Year the home was constructed |
| Lot_Size | Size of the property lot |
| Garage_Size | Capacity of the garage |
| Neighborhood_Quality | Rating representing neighborhood desirability |
| House_Price | Target variable representing home price |


This feature helps capture how property age affects housing value.

---

# 🔍 Exploratory Data Analysis

Exploratory analysis was conducted to understand the structure and patterns within the dataset.

EDA steps included:

- Dataset preview (`head`)
- Data type inspection (`info`)
- Duplicate value detection
- Missing value analysis
- Distribution analysis using histograms
- Relationship analysis using regression plots
- Joint plots for continuous feature relationships
- Boxplots to identify potential outliers
- Correlation heatmap to identify key predictors


---

# ⚙️ Data Preprocessing

Several preprocessing steps were applied before training machine learning models:

- Standard scaling of numerical features
- Feature engineering using `Age`
- Dropping the original `Year_Built` column after deriving `Age`
- Train-test split of the dataset

Dataset split:

- **80% Training Data**
- **20% Testing Data**

---

# 🤖 Machine Learning Models

Multiple regression models were trained and compared.

## Linear Regression
A baseline regression model used to estimate housing prices based on input features.

## SGD Regressor
A stochastic gradient descent model used for efficient optimization on larger datasets.

## Lasso Regression
A regularized regression model that helps reduce overfitting and can perform feature selection.

## L2 Regularized Model
An SGD regression model with L2 penalty used to reduce variance and improve generalization.

---

# 📈 Model Evaluation

Models were evaluated using standard regression metrics:

- **R² Score**
- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**

Example performance results:

| Model | Train R² | Test R² |
|------|------|------|
| Linear Regression | 0.9985 | 0.9984 |
| SGD Regressor | 0.9984 | 0.9983 |
| Regularized L2 Model | 0.9816 | 0.9816 |

The high R² values indicate that the models capture most of the variance in housing prices for this dataset.

---

# 🧰 Technologies Used

This project was developed using the following tools and libraries:

- Python
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn


---

# 📊 Key Insights

Important findings from the analysis include:

- Square footage has a strong positive relationship with housing prices.
- Bedroom and bathroom counts also contribute to property value.
- Property age provides additional predictive information.
- Linear regression models performed very well for this dataset.
