import pandas as pd

df = pd.read_csv("data/german_credit_features.csv")

# Mapa ryzyka historii kredytowej
credit_hist_risk = {
    "A30": 4, "A31": 3, "A32": 2, "A33": 3, "A34": 1
}
df["credit_hist_score"] = df["credit_history"].map(credit_hist_risk)

# Mapa ryzyka konta bankowego
checking_risk = {
    "A11": 4, "A12": 2, "A13": 1, "A14": 3
}
df["checking_score"] = df["checking_status"].map(checking_risk)

# Composite score
df["risk_score"] = (
    df["credit_hist_score"] * 0.4 +
    df["checking_score"] * 0.3 +
    df["debt_burden"].clip(0, 20) / 20 * 5 * 0.3
).round(2)

# Segmentacja
def segment(score):
    if score < 2.0:   return "Low Risk"
    elif score < 3.0: return "Medium Risk"
    else:             return "High Risk"

df["risk_segment"] = df["risk_score"].apply(segment)

print(df["risk_segment"].value_counts())
print("\nDefault rate per segment:")
print(df.groupby("risk_segment")["default"].mean().round(3))

df.to_csv("data/german_credit_segmented.csv", index=False)
print("\nZapisano: data/german_credit_segmented.csv")