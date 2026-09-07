# Ecommerce Logistics Data Analysis

## Logistics Data Analyst Internship Project

This repository contains my work completed during the **Logistics Data Analyst Internship at YuvaIntern**.

The project focuses on analyzing e-commerce logistics and delivery performance using the **Brazilian E-Commerce Public Dataset by Olist**.

---

## 👩‍💻 Intern

**Name:** Arati Balaso Deokate
**Internship Role:** Logistics Data Analyst Intern
**Organization:** YuvaIntern

---

## 📊 Project Overview

The objective of this project is to analyze e-commerce order and delivery data to understand logistics performance, identify delivery delays, examine factors affecting delivery performance, and prepare the dataset for further analysis and predictive modeling.

The project was completed week by week as part of the internship tasks, covering data analysis, preprocessing, feature engineering, and advanced logistics analysis.

---

## 🗂️ Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

The dataset contains approximately 100,000 e-commerce orders and includes information related to:

* Orders
* Customers
* Sellers
* Products
* Payments
* Order Items
* Reviews
* Delivery information

The analysis primarily focuses on order and delivery-related data.

---

# 📅 Weekly Tasks

## Week 1 – Logistics Data Analysis

### Objective

Analyze the e-commerce logistics dataset and understand order and delivery performance.

### Work Completed

* Loaded the Olist dataset using Python
* Inspected the dataset structure
* Performed basic data analysis
* Examined order and delivery information
* Analyzed logistics-related variables
* Created Python analysis code
* Documented the findings in a Week 1 report

### Files

* `Week_1_Logistics_Data_Analysis_Report.docx`
* `week1_analysis.py`

---

## Week 2 – Data Collection, Cleaning and Preprocessing

### Objective

Clean and preprocess the logistics dataset and create useful delivery-performance features.

### Work Completed

* Loaded and inspected the Olist Orders Dataset
* Checked dataset dimensions and data types
* Identified missing values
* Checked duplicate records
* Converted date columns to datetime format
* Selected valid delivered orders
* Created delivery-time features
* Created delivery-delay features
* Classified late deliveries
* Performed IQR-based outlier detection
* Prepared the final preprocessed dataset
* Saved the processed dataset as a CSV file

### Key Results

* Original records: **99,441**
* Final delivery-analysis records: **96,470**
* Average delivery time: **12.56 days**
* Average delivery delay: **-11.18 days**
* Early/On-Time orders: **88,644**
* Late orders: **7,826**
* Late delivery rate: **8.11%**
* Potential delivery-time outliers: **4,896**

### Files

* `Week_2_Logistics_Data_Analysis_Report.docx`
* `Week_2_Logistics_Data_Preprocessing.ipynb`
* `Olist_Task2_Preprocessed_Data.csv`

---

## Week 3 – Advanced Logistics Data Analysis

### Objective

Perform advanced analysis of logistics and delivery performance using the preprocessed dataset and identify patterns, trends, and factors associated with delivery delays.

### Work Completed

* Used the preprocessed logistics dataset for advanced analysis
* Analyzed delivery-time and delivery-delay patterns
* Examined late-delivery performance
* Performed exploratory data analysis using visualizations
* Analyzed relationships between logistics variables
* Investigated factors associated with delivery performance
* Generated insights from the analyzed data
* Documented the advanced analysis and findings in a Week 3 report

### Analysis Areas

The Week 3 analysis focuses on:

* Delivery performance
* Delivery delays
* Late-delivery patterns
* Logistics trends
* Relationship between delivery-related variables
* Identification of factors affecting delivery performance
* Data-driven logistics insights

### Files

* `Week_3_Logistics_Advanced_Analysis.ipynb`
* `Week_3_Logistics_Data_Analysis_Report.docx`

---

## 🔍 Key Features Created

### Delivery Time

Measures the number of days between order purchase and actual customer delivery.

```text
Delivery Time = Actual Delivery Date - Purchase Date
```

### Estimated Delivery Time

Measures the expected delivery duration based on the estimated delivery date.

```text
Estimated Delivery Time = Estimated Delivery Date - Purchase Date
```

### Delivery Delay

Measures the difference between actual delivery and estimated delivery.

```text
Delivery Delay = Actual Delivery Date - Estimated Delivery Date
```

A negative delivery delay indicates that the order was delivered **before the estimated delivery date**, while a positive value indicates that the order was delivered **after the estimated delivery date**.

### Late Delivery Flag

Orders were classified based on whether the actual delivery occurred after the estimated delivery date.

```text
Late Delivery = 1  → Delivered after estimated date
Late Delivery = 0  → Delivered on or before estimated date
```

---

## 📈 Project Outcomes

Through the three weeks of analysis, the project covered the complete data-analysis workflow:

**Data Understanding → Data Cleaning → Preprocessing → Feature Engineering → Exploratory Analysis → Advanced Logistics Analysis → Insights**

The analysis helped identify delivery-performance patterns and provided a structured, cleaned dataset suitable for further logistics analysis and predictive modeling.

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Google Colab**
* **Jupyter Notebook**
* **GitHub**

---

## 📁 Repository Structure

```text
ecommerce-logistics-data-analysis/
│
├── Olist_Task2_Preprocessed_Data.csv
│
├── Week_1_Logistics_Data_Analysis_Report.docx
├── week1_analysis.py
│
├── Week_2_Logistics_Data_Analysis_Report.docx
├── Week_2_Logistics_Data_Preprocessing.ipynb
│
├── Week_3_Logistics_Advanced_Analysis.ipynb
├── Week_3_Logistics_Data_Analysis_Report.docx
│
└── README.md
```

---

## 🎯 Conclusion

This internship project provided practical experience in analyzing real-world e-commerce logistics data using Python.

The project progressed from basic data analysis to data cleaning, preprocessing, feature engineering, and advanced logistics analysis. The final analysis provides insights into delivery performance and delays and demonstrates the application of data analytics techniques to a real-world logistics dataset.

---

## 👩‍💻 Author

**Arati Balaso Deokate**

**Logistics Data Analyst Intern – YuvaIntern**
