# Road Accident Analysis: Data Cleaning and Visualization Project

## Project Overview

Road accidents are a major public safety concern worldwide. This project focuses on cleaning, preprocessing, analyzing, and visualizing a large road accident dataset to uncover meaningful patterns and insights that can contribute to better road safety awareness.

The project demonstrates the complete data analysis workflow, including:

* Data Cleaning
* Missing Value Treatment
* Duplicate Detection
* Outlier Analysis
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Visual Reporting
* Data Storytelling

---

## Dataset Information

### Dataset Size

* Total Records: 307,973
* Total Features: 21

### Key Attributes

* Accident Severity
* Accident Date
* Day of Week
* Weather Conditions
* Road Surface Conditions
* Speed Limit
* Number of Casualties
* Number of Vehicles
* Vehicle Type
* Urban or Rural Area
* Latitude
* Longitude

---

## Project Objectives

The primary objectives of this project are:

1. Clean and preprocess raw accident data.
2. Handle missing values and inconsistencies.
3. Perform duplicate and outlier analysis.
4. Explore accident trends using statistical analysis.
5. Visualize accident patterns and contributing factors.
6. Generate insights through visual reports.

---

## Data Cleaning Process

### Missing Values

The dataset contained missing values in multiple columns.

| Column                  | Missing Values |
| ----------------------- | -------------: |
| Carriageway_Hazards     |        302,549 |
| Weather_Conditions      |          6,057 |
| Road_Type               |          1,534 |
| Road_Surface_Conditions |            317 |
| Time                    |             17 |

Actions performed:

* Removed Carriageway_Hazards due to more than 98% missing values.
* Filled Road_Type using mode imputation.
* Filled Weather_Conditions using mode imputation.
* Filled Road_Surface_Conditions using mode imputation.
* Removed records with missing Time values.

### Duplicate Analysis

Duplicate records were identified and removed where applicable.

### Outlier Analysis

Outlier analysis was conducted on:

* Number_of_Casualties
* Number_of_Vehicles
* Speed_limit

Extreme values were retained because they represented genuine accident events and not data entry errors.

---

## Feature Engineering

Additional features were created:

* Year
* Month
* Day
* Hour

These features enabled temporal trend analysis.

---

## Exploratory Data Analysis

The following analyses were performed:

### Accident Overview

* Accident Severity Distribution
* Accidents by Day of Week
* Monthly Accident Trends
* Hourly Accident Trends

### Environmental Analysis

* Weather Conditions
* Road Surface Conditions
* Urban vs Rural Areas
* Speed Limit Distribution

### Vehicle and Casualty Analysis

* Vehicle Type Distribution
* Number of Casualties
* Number of Vehicles Involved
* Correlation Analysis

---

## Key Findings

* Slight accidents constitute the majority of recorded incidents.
* Accident frequency peaks during commuting hours.
* Urban areas experience a significantly higher number of accidents.
* Weather and road conditions influence accident occurrence.
* Cars are involved in the largest proportion of accidents.
* Most accidents involve one or two vehicles.
* Most accidents result in a single casualty.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

---


## Future Enhancements

* Power BI Interactive Dashboard
* Accident Severity Prediction using Machine Learning
* Geospatial Accident Hotspot Analysis
* Time Series Forecasting of Accident Trends

---

## Author

Rohit Mandal

Data Science Enthusiast | Python Developer | Aspiring Data Scientist
