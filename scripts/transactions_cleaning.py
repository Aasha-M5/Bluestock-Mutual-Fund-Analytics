import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Load dataset
tx = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", tx.shape)

# Convert transaction date
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
tx["transaction_type"] = (
    tx["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

transaction_mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

tx["transaction_type"] = tx["transaction_type"].replace(transaction_mapping)

# Validate amount > 0
invalid_amounts = tx[tx["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amounts))

tx = tx[tx["amount_inr"] > 0]

# Standardize KYC status
tx["kyc_status"] = (
    tx["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = tx[
    ~tx["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicates
tx = tx.drop_duplicates()

# Missing values
print("\nMissing Values:")
print(tx.isnull().sum())

# Duplicate count
print("\nDuplicate Rows:", tx.duplicated().sum())

print("\nCleaned Shape:", tx.shape)

# Save cleaned dataset
tx.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nclean_investor_transactions.csv saved successfully!")