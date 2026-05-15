import pandas as pd
import sqlite3

df = pd.read_csv("data/german_credit_segmented.csv")

conn = sqlite3.connect("data/credit_risk.db")

df.to_sql("credit_data", conn, if_exists="replace", index=False)

print(f"Załadowano {len(df)} wierszy do bazy danych")

# Szybka weryfikacja
result = pd.read_sql("SELECT risk_segment, COUNT(*) as n, ROUND(AVG(\"default\")*100,1) as default_rate FROM credit_data GROUP BY risk_segment", conn)
print(result)

conn.close()
print("\nBaza zapisana: data/credit_risk.db")