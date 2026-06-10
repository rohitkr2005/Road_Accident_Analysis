# Road Accident Analysis and Severity Prediction Using Machine Learning

## Project Overview

Road accidents are a major public safety concern worldwide, resulting in significant human and economic losses. This project focuses on analyzing a large road accident dataset to uncover meaningful patterns, identify contributing factors, and develop machine learning models capable of predicting accident severity.

The project combines data preprocessing, exploratory data analysis (EDA), visual reporting, and predictive modeling to provide actionable insights into road safety.

---

## Project Objectives

The primary objectives of this project are:

* Clean and preprocess raw accident data.
* Handle missing values, inconsistencies, and duplicates.
* Perform outlier analysis and feature engineering.
* Analyze accident trends and contributing factors.
* Create visual reports and dashboards for data storytelling.
* Build machine learning models to predict accident severity.
* Evaluate model performance using standard classification metrics.

---

## Dataset Information

### Dataset Size

* Total Records: 307,973
* Total Features: 21

### Key Attributes

* Accident Severity
* Accident Date
* Day of Week
* Junction Control
* Junction Detail
* Light Conditions
* Weather Conditions
* Road Surface Conditions
* Road Type
* Speed Limit
* Number of Casualties
* Number of Vehicles
* Vehicle Type
* Urban or Rural Area
* Latitude
* Longitude

---

# Phase 1: Data Cleaning and Visualization

## Data Cleaning Process

### Missing Values

The dataset contained missing values in several columns.

| Column                  | Missing Values |
| ----------------------- | -------------: |
| Carriageway_Hazards     |        302,549 |
| Weather_Conditions      |          6,057 |
| Road_Type               |          1,534 |
| Road_Surface_Conditions |            317 |
| Time                    |             17 |

### Actions Performed

* Removed Carriageway_Hazards due to excessive missing values (>98%).
* Imputed missing values in Road_Type using mode.
* Imputed missing values in Weather_Conditions using mode.
* Imputed missing values in Road_Surface_Conditions using mode.
* Removed records containing missing Time values.

### Duplicate Analysis

Duplicate records were identified and removed where applicable.

### Outlier Analysis

Outlier analysis was conducted on:

* Number_of_Casualties
* Number_of_Vehicles
* Speed_limit

Extreme values were retained because they represented legitimate accident events rather than data entry errors.

---

## Feature Engineering

New features were created from date and time columns:

* Year
* Month
* Day
* Hour

These features enabled deeper temporal trend analysis.

---

## Exploratory Data Analysis (EDA)

### Accident Overview

* Accident Severity Distribution
* Day-wise Accident Analysis
* Monthly Accident Trends
* Hourly Accident Trends

### Environmental Analysis

* Weather Conditions Analysis
* Road Surface Condition Analysis
* Urban vs Rural Accident Distribution
* Speed Limit Distribution

### Vehicle and Casualty Analysis

* Vehicle Type Distribution
* Casualty Distribution
* Vehicles Involved Analysis
* Correlation Analysis

---

## Visual Reporting

Three visual reports were created:

### Visual Report 1: Accident Overview

* Severity Distribution
* Day-wise Trends
* Monthly Trends
* Hourly Trends

### Visual Report 2: Environmental Factors

* Weather Conditions
* Road Surface Conditions
* Urban vs Rural Analysis
* Speed Limit Analysis

### Visual Report 3: Vehicle and Casualty Analysis

* Vehicle Type Distribution
* Casualty Distribution
* Vehicles Involved
* Correlation Heatmap

---

## Key Findings

* Slight accidents constitute the majority of recorded incidents.
* Accident frequency peaks during commuting hours.
* Urban areas experience a higher number of accidents than rural areas.
* Weather and road surface conditions influence accident occurrence.
* Cars are involved in the largest proportion of accidents.
* Most accidents involve one or two vehicles.
* Most accidents result in a single casualty.

---

# Phase 2: Predictive Modeling Using Machine Learning

## Problem Statement

The objective is to predict accident severity using accident-related features such as road conditions, weather, speed limits, vehicle types, and casualty information.

### Target Variable

* Accident_Severity

### Input Features

* Day_of_Week
* Junction_Control
* Junction_Detail
* Light_Conditions
* Road_Surface_Conditions
* Road_Type
* Speed_limit
* Urban_or_Rural_Area
* Weather_Conditions
* Vehicle_Type
* Number_of_Casualties
* Number_of_Vehicles

---

## Machine Learning Workflow

1. Data Preprocessing
2. Label Encoding of Categorical Features
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis

---

## Machine Learning Models

### Decision Tree Classifier

Used as a baseline classification model.

### Random Forest Classifier

Used to improve predictive performance and reduce overfitting.

---

## Model Evaluation Metrics

The models are evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1 Score
* Feature Importance Analysis

---

## Technologies Used

### Programming & Analysis

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Development Environment

* Jupyter Notebook

### Version Control

* Git
* GitHub

### Business Intelligence (Future Scope)

* Power BI

---

## Future Enhancements

* Interactive Power BI Dashboard
* Accident Severity Prediction Web Application
* Geospatial Accident Hotspot Mapping
* Real-Time Accident Risk Prediction
* Time Series Forecasting of Accident Trends
* Hyperparameter Optimization
* Advanced Ensemble Learning Techniques

---

## Author

### Rohit Kumar Mandal

Data Science Enthusiast | Python Developer | Machine Learning Practitioner | Aspiring Data Scientist

---

## License

This project is intended for educational, research, and portfolio purposes.
