import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv(
    "data/raw/HDFC_Top100_NAV.csv",
    index=False
)

print("NAV data saved successfully!")