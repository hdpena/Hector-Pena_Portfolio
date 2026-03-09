# 🎢 Theme Park Injury Analysis

---

# 🧠 Project Overview

This project analyzes **reported theme park injuries across the United States over a 20-year period**. The goal of the analysis is to explore patterns in injury reports and determine whether specific factors—such as **time of year, age group, gender, or ride type—are associated with higher injury rates**.

The analysis also introduces **categorical injury indicators** (such as hospitalization, seizures, chest pain, and sickness) to better understand the nature and severity of incidents.

The project is implemented in **Python using a Jupyter Notebook** and focuses on **exploratory data analysis (EDA), feature engineering, and visualization**.

---

# 🎯 Project Objectives

The main goals of this analysis are:

- Examine **injury trends over time**
- Analyze **age and gender distributions of injuries**
- Explore **seasonal patterns in injury reports**
- Investigate relationships between **ride type and injury occurrence**
- Create **indicator variables for different injury categories**
- Explore the possibility of building **predictive models for injury risk**

---

# 📊 Key Analyses

## Injury Trends Over Time

The dataset includes injury reports across **daily, monthly, and yearly time scales**.

Initial exploratory analysis shows:

- Injury occurrences fluctuate throughout the year
- Multiple peaks occur across different years
- The distribution appears **random with periodic spikes**

This suggests injuries may be influenced by **external factors such as park attendance or seasonal tourism**.

---

# 👥 Age and Gender Distribution

The analysis shows differences in injuries across demographics.

Key findings include:

- **Women report more injuries than men**
- The **40+ age group shows the highest number of injuries**
- Adults and seniors account for a large portion of injury cases

These findings suggest older age groups may be **more vulnerable to ride-related injuries**.

---

# 🎢 Ride Type vs Injury Analysis

Ride classifications were compared against injury reports.

The analysis shows:

- **Family-friendly rides have higher injury counts among seniors**
- **Thrill rides tend to show injury peaks among adults**
- Ride category and age group may have a **strong relationship with injury risk**

---

# 🩺 Injury Indicator Classification

To better categorize incidents, injury reports were processed into **binary indicator variables**.

Each report was categorized into indicators such as:

- Deceased
- Hospitalization
- Pre-existing condition
- Unconsciousness
- Chest pain
- Seizure
- Physical injury
- Sickness
