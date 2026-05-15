import pandas as pd

df = pd.read_csv("data/german_credit_clean.csv")

# Grupy wiekowe
def age_group(age):
    if age < 25:   return "18-24"
    elif age < 35: return "25-34"
    elif age < 45: return "35-44"
    elif age < 60: return "45-59"
    else:          return "60+"

df["age_group"] = df["age"].apply(age_group)

# Segmenty kwoty kredytu
df["amount_bucket"] = pd.cut(
    df["credit_amount"],
    bins=[0, 2000, 5000, 99999],
    labels=["Low", "Medium", "High"]
)

# Wskaźnik zadłużenia (kwota x rata / 1000)
df["debt_burden"] = (df["credit_amount"] * df["installment_commitment"] / 1000).round(2)

print(df[["age", "age_group", "credit_amount", "amount_bucket", "debt_burden"]].head(10))
print("\nShape:", df.shape)

df.to_csv("data/german_credit_features.csv", index=False)
print("Zapisano: data/german_credit_features.csv")