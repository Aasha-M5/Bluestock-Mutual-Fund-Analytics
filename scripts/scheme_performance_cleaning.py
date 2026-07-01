import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Load dataset
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", perf.shape)

# Columns that should be numeric
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert to numeric
for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# Check missing values
print("\nMissing Values:")
print(perf.isnull().sum())

# Validate expense ratio
invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:", len(invalid_expense))

# Check return anomalies
return_anomalies = perf[
    (perf["return_1yr_pct"] < -100) |
    (perf["return_3yr_pct"] < -100) |
    (perf["return_5yr_pct"] < -100)
]

print("Return Anomalies:", len(return_anomalies))

# Remove duplicates
perf = perf.drop_duplicates()

print("\nDuplicate Rows:", perf.duplicated().sum())

print("\nCleaned Shape:", perf.shape)

# Save cleaned file
perf.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nclean_scheme_performance.csv saved successfully!")