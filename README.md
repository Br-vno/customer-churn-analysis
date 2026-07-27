# Telecom Customer Churn Analysis

## Project Overview
This project analyzes customer churn for a telecommunications company using the IBM Telco Customer Churn dataset. The goal is to identify the key drivers of churn and provide actionable business recommendations.

## Objectives
- Clean and explore a real-world customer dataset
- Perform exploratory data analysis (EDA)
- Conduct statistical hypothesis testing
- Identify high-risk customer segments
- Provide clear business insights and recommendations

## Dataset
- **Source**: IBM Telco Customer Churn Dataset
- **Size**: 7,043 customers (7,032 after cleaning)
- **Target Variable**: `Churn` (Yes/No)

## Project Structure
customer-churn-analysis/
├── data/                  # Cleaned dataset
├── notebooks/             # Main analysis notebook
├── results/               # Saved visualizations
├── src/                   # Reusable functions
├── requirements.txt
└── README.md

## Key Findings
- Overall churn rate: **26.58%**
- **Tenure** is the strongest continuous predictor of churn
- **Month-to-month** contracts have a 42.7% churn rate
- **Fiber optic** customers churn at 41.9%
- **Electronic check** payment method has the highest churn rate (45.3%)

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- SciPy (hypothesis testing)
- Jupyter Notebook

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Open `notebooks/01_churn_analysis.ipynb` in Jupyter or Codespaces
4. Run all cells

## Author
Bruno Okoliachu
