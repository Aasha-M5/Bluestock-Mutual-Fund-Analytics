from sqlalchemy import create_engine
import os

engine = create_engine("sqlite:///bluestock_mf.db")

# Force creation of the file
with engine.connect() as conn:
    pass

print("Database created successfully!")
print(os.path.abspath("bluestock_mf.db"))