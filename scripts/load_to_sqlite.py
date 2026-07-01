import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/clean_nav_history.csv")
transactions = pd.read_csv("data/processed/clean_investor_transactions.csv")
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

# Load into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded successfully!")
print("NAV Rows:", len(nav))
print("Transaction Rows:", len(transactions))
print("Performance Rows:", len(performance))