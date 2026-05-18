# Credit Risk Analysis — Loan Default Prediction & Segmentation

**Python • SQL • Power BI**

End-to-end credit risk analysis of 1,000 loan customers using the German Credit Dataset (UCI ML Repository). The project focuses on identifying default risk factors and segmenting customers into actionable risk tiers.

---

## Business Problem

A lending portfolio with a 30% default rate requires better customer segmentation and risk visibility to support data-driven credit decisions.

The goal of this analysis was to:
- identify the key drivers of loan default
- segment customers into High / Medium / Low risk tiers
- support portfolio risk management with an interactive dashboard

---

## Key KPIs

- Overall Default Rate
- Default Rate by Risk Segment
- Total Portfolio Value (DM)
- Average Credit Amount

---

## Key Findings

- Overall default rate: **30%**
- High Risk segment: **53.8%** default rate vs Low Risk: **17.8%**
- Customers aged 18–24 have the highest default rate: **40.9%**
- High loan amounts (>5,000 DM) default rate: **41.5%**
- Credit history A30/A31 shows the highest risk: **62.5% / 57.1%**

---

## Dashboards (Power BI)

**Page 1 – Portfolio Overview**
KPIs, customer distribution by risk segment, default rate by risk tier.

<img width="2129" height="1227" alt="Zrzut ekranu 2026-05-18 120604" src="https://github.com/user-attachments/assets/312efa3a-44cd-4388-8e80-07586fdbd493" />


**Page 2 – Risk Segmentation**
Customer count by segment and default status, age group distribution by risk segment.

<img width="2131" height="1230" alt="Zrzut ekranu 2026-05-18 120613" src="https://github.com/user-attachments/assets/0e136569-cef1-4f00-9028-9684caa3a9d8" />

**Page 3 – Default Risk Drivers**
Default rate by credit history, age group, and loan amount.

<img width="2128" height="1230" alt="Zrzut ekranu 2026-05-18 120623" src="https://github.com/user-attachments/assets/f1527025-c8c4-46f4-a6e6-1e54f096b2cd" />


---

## Project Structure

├── data/
├── 01_load_and_clean.py
├── 02_feature_engineering.py
├── 03_risk_segmentation.py
├── 04_load_to_sqlite.py
├── credit_risk.pbix
└── README.md

---

## Dataset

- **Source:** [German Credit Data – UCI ML Repository](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)
- **Scale:** 1,000 loan customers
- **Total Portfolio:** 3M DM

---

## Tools & Technologies

- **Python (pandas)** – data cleaning, feature engineering, risk segmentation
- **SQLite + SQL** – data storage and analytical queries
- **Power BI** – interactive dashboard and risk visualisation
- **AI-assisted workflow** – analytical reasoning and insight validation

---

## Author

**Oliwia Tomiczek**
Data Analyst | SQL • Power BI • Business Analytics
