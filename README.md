# Ecommerce Logistics Data Analysis

## Logistics Data Analyst Internship Project

This repository contains my work completed during the **Logistics Data Analyst Internship at YuvaIntern**.

The project focuses on analyzing e-commerce logistics and delivery performance using the **Brazilian E-Commerce Public Dataset by Olist**, along with a synthetic logistics dataset developed for advanced predictive modeling and optimization.

---

## 👩‍💻 Intern

**Name:** Arati Balaso Deokate  
**Internship Role:** Logistics Data Analyst Intern  
**Organization:** YuvaIntern

---

## 📊 Project Overview

The objective of this project is to analyze logistics and delivery data to understand delivery performance, identify delays, examine factors affecting delivery time, preprocess data, perform advanced analysis, and build predictive models for logistics decision-making.

The project was completed week by week as part of the internship tasks, covering:

**Data Analysis → Data Cleaning → Preprocessing → Feature Engineering → Advanced Analysis → Predictive Modeling → Optimization**

---

## 🗂️ Datasets

### Brazilian E-Commerce Public Dataset by Olist

The main dataset used in Weeks 1–3 is the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset contains approximately 100,000 e-commerce orders and includes information related to:

- Orders
- Customers
- Sellers
- Products
- Payments
- Order Items
- Reviews
- Delivery information

The analysis primarily focuses on order and delivery-related data.

### Synthetic Logistics Dataset

For Week 4 predictive modeling and optimization, a synthetic logistics dataset containing **1,000 shipment records** was generated using Python.

The dataset includes:

- Shipment ID
- Shipment Date
- Transport Mode
- Region
- Distance
- Shipment Volume
- Transportation Cost
- Fuel Cost
- Delivery Time
- Delay Days
- Delivery Status

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

## Week 3 – Advanced Logistics Data Analysis

### Objective

Perform advanced logistics analysis using data visualization, descriptive statistics, and correlation analysis to identify patterns and factors associated with logistics performance.

### Work Completed

- Performed exploratory data analysis
- Analyzed delivery-time distribution
- Analyzed delivery status
- Examined transportation costs by transport mode
- Compared delivery time across transport modes
- Analyzed distance and transportation cost relationships
- Created correlation analysis and heatmaps
- Identified potential logistics bottlenecks
- Generated data-driven logistics insights
- Documented the findings in a Week 3 report

### Main Analysis Areas

- Delivery performance
- Transportation cost
- Delivery time
- Distance
- Fuel cost
- Shipment volume
- Transport modes
- Correlation between logistics variables
- Logistics bottleneck identification

### Files

- `Week_3_Logistics_Advanced_Analysis.ipynb`
- `Week_3_Logistics_Data_Analysis_Report.docx`

---

# Week 4 – Predictive Modeling and Optimization in Logistics

## Objective

Build predictive models to forecast delivery time and analyze logistics optimization strategies.

### Work Completed

- Generated a synthetic logistics dataset containing 1,000 shipment records
- Defined `delivery_time_days` as the prediction target
- Selected numerical and categorical logistics features
- Applied one-hot encoding to categorical variables
- Split the dataset into training and testing sets
- Implemented Linear Regression
- Implemented Random Forest Regression
- Evaluated models using MAE, RMSE, and R²
- Performed 5-fold cross-validation
- Compared actual and predicted delivery times
- Analyzed transport-mode performance
- Studied relationships between delivery time and logistics variables
- Developed logistics optimization recommendations

### Predictive Features

The following variables were used to predict delivery time:

- Shipment Volume
- Transportation Cost
- Distance
- Fuel Cost
- Transport Mode
- Region

### Model Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 1.1874 | 1.4269 | 0.6991 |
| Random Forest | 1.2495 | 1.5245 | 0.6566 |

Based on the test-set results, **Linear Regression performed better** than Random Forest for this synthetic dataset.

The Linear Regression model achieved an **R² of 0.6991**, indicating that the model explained approximately 69.91% of the variation in delivery time in the test data.

### Cross-Validation

Linear Regression was further evaluated using 5-fold cross-validation.

- Fold 1 RMSE: **1.5386**
- Fold 2 RMSE: **1.5470**
- Fold 3 RMSE: **1.6018**
- Fold 4 RMSE: **1.4680**
- Fold 5 RMSE: **1.5200**
- Mean CV RMSE: **1.5351**

### Transport Mode Optimization Analysis

| Transport Mode | Avg. Delivery Time | Avg. Transportation Cost | Avg. Fuel Cost |
|---|---:|---:|---:|
| Air | 3.82 days | 3867.67 | 187.90 |
| Road | 5.13 days | 2003.34 | 202.37 |
| Rail | 7.21 days | 1586.45 | 208.59 |
| Sea | 9.62 days | 1290.06 | 198.75 |

The analysis indicates that:

- **Air** provides the fastest delivery but has the highest transportation cost.
- **Sea** has the lowest transportation cost but the longest delivery time.
- **Road** provides a practical balance between delivery speed and transportation cost.
- **Rail** provides relatively low transportation cost but longer delivery time than Road.

### Correlation with Delivery Time

| Variable | Correlation |
|---|---:|
| Distance | 0.448 |
| Fuel Cost | 0.428 |
| Shipment Volume | 0.086 |
| Delay Days | 0.020 |
| Transportation Cost | -0.019 |

Distance showed the strongest positive linear relationship with delivery time in the generated dataset.

### Optimization Recommendations

- Use Air transportation for urgent shipments where delivery speed is the priority.
- Consider Sea transportation for low-cost shipments where longer delivery times are acceptable.
- Use Road transportation as a balanced option for many regular shipments.
- Monitor long-distance shipments because distance has a relatively strong relationship with delivery time.
- Use predictive models to estimate expected delivery time before shipment planning.
- Include additional operational variables such as traffic, weather, warehouse processing time, carrier performance, and seasonal effects in future models.
- Consider both transportation cost and delivery time when selecting logistics strategies.

### Week 4 Files

- `Week_4_Logistics_Predictive_Modeling.ipynb`
- `Week_4_Logistics_Predictive_Modeling_Report.docx`
- `week4_analysis.py`
- `Week_4_Logistics_Synthetic_Dataset.csv`
- `Week_4_Model_Comparison.csv`
- `Week_4_Transport_Mode_Summary.csv`

---

# 🔍 Key Features Created

## Delivery Time

Measures the number of days between order purchase and actual customer delivery.

```text
Delivery Time = Actual Delivery Date - Purchase Date
