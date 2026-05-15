# Credit Risk Analysis — Loan Default Prediction & Segmentation

## Project Overview
Analysis of 1,000 loan customers using German Credit Data (UCI ML Repository).
Goal: identify default risk factors and segment customers into risk tiers.

## Tech Stack
- **Python** (pandas) — data cleaning, feature engineering, segmentation
- **SQLite** — data storage and SQL analysis
- **Power BI** — interactive dashboard (3 pages)

## Project Structure
credit_risk/
├── data/
│   ├── german.data
│   ├── german_credit_clean.csv
│   ├── german_credit_features.csv
│   ├── german_credit_segmented.csv
│   └── credit_risk.db
├── 01_load_and_clean.py
├── 02_feature_engineering.py
├── 03_risk_segmentation.py
├── 04_load_to_sqlite.py
├── credit_analysis.sql
└── credit_risk_dashboard.pbix
## Business Questions
1. What is the overall default rate in the portfolio?
2. Which customer segments generate the highest risk?
3. Does loan amount correlate with default probability?
4. Which demographic features best predict default?
5. What actions can the bank take to reduce portfolio risk?

## Key Insights
- Overall default rate: **30%**
- High Risk segment default rate: **53.8%** vs Low Risk: **17.8%**
- Customers aged 18-24 have the highest default rate: **40.9%**
- High loan amounts (>5,000 DM) default rate: **41.5%**
- Credit history type A30/A31 = highest risk: **62.5% / 57.1%**

## How to Run
```bash
python 01_load_and_clean.py
python 02_feature_engineering.py
python 03_risk_segmentation.py
python 04_load_to_sqlite.py
```