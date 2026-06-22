# Road Accident Analysis and Severity Prediction Using Machine Learning

## Project Overview

Road accidents are a significant public safety concern worldwide, leading to loss of life, injuries, and economic damage. Understanding the factors contributing to accidents can help improve road safety policies and accident prevention strategies.

This project presents a complete data science workflow using a large road accident dataset. The project covers data cleaning, exploratory data analysis (EDA), visualization, feature engineering, and machine learning-based accident severity prediction. Through statistical analysis and predictive modeling, the project aims to uncover meaningful patterns and identify key factors influencing accident severity.

---

## Project Objectives

The primary objectives of this project are:

* Clean and preprocess raw accident data.
* Handle missing values, duplicates, and inconsistencies.
* Perform outlier analysis and feature engineering.
* Conduct exploratory data analysis to identify patterns and trends.
* Generate visual reports for effective data storytelling.
* Build machine learning models to predict accident severity.
* Evaluate model performance using standard classification metrics.
* Provide insights that may support road safety improvements and decision-making.

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
* Police Force
* Latitude
* Longitude

---

# Phase 1: Data Cleaning and Visualization

## Data Cleaning Process

The dataset contained missing values, inconsistencies, and redundant information that required preprocessing before analysis.

### Missing Values Analysis

| Column                  | Missing Values |
| ----------------------- | -------------: |
| Carriageway_Hazards     |        302,549 |
| Weather_Conditions      |          6,057 |
| Road_Type               |          1,534 |
| Road_Surface_Conditions |            317 |
| Time                    |             17 |

### Data Cleaning Actions

* Removed `Carriageway_Hazards` due to excessive missing values (>98%).
* Filled missing values in `Road_Type` using mode imputation.
* Filled missing values in `Weather_Conditions` using mode imputation.
* Filled missing values in `Road_Surface_Conditions` using mode imputation.
* Removed records containing missing values in `Time`.
* Checked and handled duplicate records.
* Standardized data formats where required.

### Outlier Analysis

Outlier detection was performed on:

* Number_of_Casualties
* Number_of_Vehicles
* Speed_limit

Extreme values were retained because they represented genuine accident events rather than data entry errors.

---

## Feature Engineering

Additional features were extracted from date and time columns to enable deeper analysis.

### New Features Created

* Year
* Month
* Day
* Hour

These engineered features were used for trend analysis and predictive modeling.

---

## Visual Reporting

To communicate findings effectively, multiple visual reports were created.

### Visual Report 1: Accident Overview

* Accident Severity Distribution
* Day-wise Accident Analysis
* Monthly Accident Trends
* Hourly Accident Trends

### Visual Report 2: Environmental Factors

* Weather Conditions Analysis
* Road Surface Conditions Analysis
* Urban vs Rural Distribution
* Speed Limit Distribution

### Visual Report 3: Vehicle and Casualty Analysis

* Vehicle Type Distribution
* Casualty Distribution
* Vehicles Involved Analysis
* Correlation Heatmap

---

# Phase 2: Exploratory Data Analysis (EDA)

## Objective

The goal of Exploratory Data Analysis (EDA) is to understand the structure of the dataset, identify trends, detect relationships among variables, and generate insights that support informed decision-making.

---

## Statistical Summary

Descriptive statistical analysis was conducted on both numerical and categorical features.

### Numerical Features Analyzed

* Speed Limit
* Number of Casualties
* Number of Vehicles
* Latitude
* Longitude

### Statistical Measures Used

* Count
* Mean
* Standard Deviation
* Minimum
* Maximum
* Quartiles

---

## Univariate Analysis

Univariate analysis was performed to study the distribution of individual variables.

### Accident Severity Analysis

* Distribution of Fatal, Serious, and Slight accidents.
* Identification of dominant accident severity categories.

### Temporal Analysis

* Accidents by Day of Week
* Monthly Accident Distribution
* Hourly Accident Trends

### Environmental Analysis

* Weather Conditions Distribution
* Road Surface Conditions Distribution
* Urban vs Rural Accident Distribution

### Vehicle Analysis

* Vehicle Type Distribution
* Most Frequently Involved Vehicles

---

## Bivariate Analysis

Relationships between variables were explored to identify potential influencing factors.

### Speed Limit vs Casualties

Analyzed how road speed limits influence casualty counts.

### Number of Vehicles vs Casualties

Studied the relationship between vehicle involvement and accident impact.

### Weather Conditions vs Accident Severity

Examined the influence of weather on accident outcomes.

### Road Surface Conditions vs Accident Severity

Evaluated how road surface conditions affect accident severity.

---

## Correlation Analysis

A correlation matrix and heatmap were generated using numerical variables to identify relationships between key features.

### Variables Included

* Speed Limit
* Number of Casualties
* Number of Vehicles
* Latitude
* Longitude

The heatmap helped identify positive and negative relationships among numerical features.

---

## Geographic Analysis

Geographic analysis was performed using latitude and longitude coordinates.

### Analysis Performed

* Spatial Distribution of Accidents
* Accident Density Visualization
* Geographic Hotspot Identification

This analysis provided insights into accident-prone locations and regional patterns.

---

## Key EDA Findings

* Slight accidents constitute the majority of recorded incidents.
* Accident frequency peaks during commuting hours.
* Urban areas experience more accidents than rural areas.
* Cars are involved in the majority of accidents.
* Weather and road conditions significantly influence accident occurrence.
* Most accidents involve one or two vehicles.
* Most accidents result in a single casualty.
* Certain geographic regions exhibit higher accident concentration.

---

# Phase 3: Predictive Modeling Using Machine Learning

## Problem Statement

The objective of this phase is to build machine learning models capable of predicting accident severity using accident-related features.

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
2. Label Encoding
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis

---

## Machine Learning Models

### Decision Tree Classifier

A Decision Tree model was used as the baseline classification model due to its simplicity and interpretability.

### Random Forest Classifier

A Random Forest model was implemented to improve predictive accuracy and reduce overfitting through ensemble learning.

---

## Model Evaluation Metrics

The machine learning models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1 Score
* Feature Importance Analysis

---

## Technologies Used

### Programming and Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

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


## Key Outcomes

* Successfully cleaned and preprocessed a large accident dataset.
* Performed comprehensive exploratory data analysis.
* Generated visual reports for effective data storytelling.
* Identified key factors contributing to road accidents.
* Built machine learning models for accident severity prediction.
* Evaluated model performance using multiple classification metrics.
* Established a complete end-to-end data science workflow.

---

## Future Enhancements

* Interactive Power BI Dashboard
* Accident Severity Prediction Web Application
* Real-Time Accident Risk Prediction System
* Geospatial Accident Hotspot Mapping
* Time Series Forecasting of Accident Trends
* Hyperparameter Optimization
* Advanced Ensemble Learning Models
* Deep Learning-Based Severity Prediction

---

## Author

### Rohit Kumar Mandal

**Data Science Enthusiast | Python Developer | Machine Learning Practitioner | Aspiring Data Scientist**

---