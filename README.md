# Yelp RV Establishment Data Analysis

## Overview

This project analyzes RV-related establishments using the **Yelp Academic Dataset** to identify trends in customer reviews, ratings, and geographic distribution. The analysis focuses on RV-specific businesses such as **RV Rentals, RV Dealers, RV Parks, RV Repair shops, and Campgrounds**.

The objective of the project is to determine whether **geographic location (state or postal code)** correlates with the **number of reviews and customer ratings** for RV establishments.

Through data cleaning, transformation, and visualization, the project reveals that **Arizona and Nevada account for the majority of RV-related reviews**, suggesting that tourism and travel activity strongly influence customer engagement.

---

## Research Question

Is there a relationship between **geographic location (state or postal code)** and the **number or quality of customer reviews** for RV establishments?

---

## Dataset

This project uses the **Yelp Academic Dataset**, including the following files:

- `yelp_academic_dataset_business.json`
- `yelp_academic_dataset_review.json`

These datasets contain information such as:

- Business names
- Addresses
- State and postal codes
- Star ratings
- Review counts
- Review text
- Business categories

The dataset originally included many different types of businesses, so filtering was applied to focus specifically on **RV-related establishments**.

---

## Technologies Used

- **Python**
- **Pandas** – Data manipulation and cleaning
- **Seaborn** – Statistical data visualization
- **Matplotlib** – Plotting and charts
- **Jupyter Notebook** – Interactive data analysis

---

## Project Workflow

### 1. Data Import

The Yelp dataset was imported into Python using Pandas.
