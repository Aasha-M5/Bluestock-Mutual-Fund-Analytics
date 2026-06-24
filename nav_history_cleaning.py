import pandas as pd
import os

# Create processed folder if it does not exist
os.makedirs("data/processed", exist_ok=True)

# Load NAV history
nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav.shape)
print(nav.head())
print(nav.dtypes)

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
print(nav.dtypes)

# Convert NAV to numeric
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

# Remove duplicate rows
nav = nav.drop_duplicates()

# Sort by AMFI code and date
nav = nav.sort_values(by=["amfi_code", "date"])

# Forward-fill missing NAV values within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
invalid_nav = nav[nav["nav"] <= 0]

print("\nInvalid NAV Records:", invalid_nav.shape[0])

# Remove invalid NAV records
nav = nav[nav["nav"] > 0]

# Final checks
print("\nCleaned Shape:", nav.shape)
print("\nMissing Values:")
print(nav.isnull().sum())

print("\nDuplicate Rows:", nav.duplicated().sum())

# Save cleaned file
nav.to_csv("data/processed/clean_nav_history.csv", index=False)

print("\nclean_nav_history.csv saved successfully!")