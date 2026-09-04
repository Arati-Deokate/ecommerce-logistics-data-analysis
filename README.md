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

The objective of this project is to analyze e-commerce order and delivery data to understand logistics performance, identify delivery delays, and prepare the dataset for further analysis and predictive modeling.

The project is being completed week by week as part of the internship tasks.

---

## 🗂️ Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

The dataset contains approximately 100,000 e-commerce orders and includes information related to:

- Orders
- Customers
- Sellers
- Products
- Payments
- Order Items
- Reviews
- Delivery information

The Week 1 and Week 2 analysis primarily focuses on the **Olist Orders Dataset**.

---

# 📅 Weekly Tasks

## Week 1 – Logistics Data Analysis

### Objective
Analyze the e-commerce logistics dataset and understand order and delivery performance.

### Work Completed

- Loaded the Olist dataset using Python
- Inspected the dataset structure
- Performed basic data analysis
- Examined order and delivery information
- Analyzed logistics-related variables
- Created Python analysis code
- Documented the findings in a Week 1 report

### Files

- `Week_1_Logistics_Data_Analysis_Report.docx`
- `week1_analysis.py`

---

## Week 2 – Data Collection, Cleaning and Preprocessing

### Objective
Clean and preprocess the logistics dataset and create useful delivery-performance features.

### Work Completed

- Loaded and inspected the Olist Orders Dataset
- Checked dataset dimensions and data types
- Identified missing values
- Checked duplicate records
- Converted date columns to datetime format
- Selected valid delivered orders
- Created delivery-time features
- Created delivery-delay features
- Classified late deliveries
- Performed IQR-based outlier detection
- Prepared the final preprocessed dataset
- Saved the processed dataset as a CSV file

### Key Results

- Original records: **99,441**
- Final delivery-analysis records: **96,470**
- Average delivery time: **12.56 days**
- Average delivery delay: **-11.18 days**
- Early/On-Time orders: **88,644**
- Late orders: **7,826**
- Late delivery rate: **8.11%**
- Potential delivery-time outliers: **4,896**

### Files

- `Week_2_Logistics_Data_Analysis_Report.docx`
- `Week_2_Logistics_Data_Preprocessing.ipynb`
- `Olist_Task2_Preprocessed_Data.csv`

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- GitHub

---

## 🔍 Key Features Created

### Delivery Time

Measures the number of days between order purchase and actual customer delivery.

```text
Delivery Time = Actual Delivery Date - Purchase Date
