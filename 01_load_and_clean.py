import pandas as pd

column_names = [
    "checking_status", "duration", "credit_history", "purpose",
    "credit_amount", "savings_status", "employment",
    "installment_commitment", "personal_status", "other_parties",
    "residence_since", "property_magnitude", "age",
    "other_payment_plans", "housing", "existing_credits", "job",
    "num_dependents", "own_telephone", "foreign_worker", "class"
]

df = pd.read_csv("data/german.data", sep=" ", header=None, names=column_names)

print(df.shape)
print(df.head())

# Sprawdź brakujące wartości
print("\nBrakujące wartości:")
print(df.isnull().sum())

# Sprawdź typy danych
print("\nTypy danych:")
print(df.dtypes)

# Zamień kolumnę class: 1=Good, 2=Bad → 0=Good, 1=Default
df["default"] = (df["class"] == 2).astype(int)

print("\nDefault rate:", df["default"].mean().round(3))
df.to_csv("data/german_credit_clean.csv", index=False)
print("Zapisano: data/german_credit_clean.csv")