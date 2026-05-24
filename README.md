# Food Demand Forecasting System

## Overview

The Food Demand Forecasting System is a Machine Learning-based application developed to predict the number of food orders using historical food delivery data. The project uses regression algorithms to forecast food demand accurately and helps restaurants, food delivery services, and cloud kitchens optimize inventory, reduce food waste, and improve delivery planning.

This project also includes:
- REST API using FastAPI
- Web Application using Streamlit
- API Testing using Postman
- Deployment support for Hugging Face Spaces

---

# Project Objectives

The main objectives of this project are:

- Predict future food demand
- Reduce food wastage
- Improve inventory management
- Enhance delivery planning
- Analyze promotional impacts
- Increase operational efficiency

---

# Dataset Information

## Dataset Name
Food Demand Forecasting Dataset

## Source
https://www.kaggle.com/datasets/kannanaikkal/food-demand-forecasting

## Dataset Contains
- Historical food order data
- Meal information
- Fulfillment center details
- Pricing information
- Promotional data

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | API Development |
| Streamlit | Web Application |
| Scikit-learn | Machine Learning |
| Pandas | Data Analysis |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Joblib | Model Saving & Loading |
| Git & GitHub | Version Control |

---

# Machine Learning Model

## Algorithm Used
Random Forest Regressor

## Features Used
- week
- checkout_price
- base_price
- emailer_for_promotion
- homepage_featured

## Target Variable
- num_orders

---

# Project Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Optimization
8. API Development
9. Deployment

---

# Project Structure

```bash
food-demand/
│
├── api.py
├── app.py
├── food_demand_model.pkl
├── requirements.txt
├── README.md
