import pandas as pd
import sqlite3
import os
from datetime import datetime
#===Exctract===
#read the csv file
df = pd.read_csv("data/sample_sales.csv")
#=== Transform ====

#Clean coloumn names: remove spaces. Lowercase
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

#Drop rows with any missing / null values
df.dropna(inplace=True)

# Add a coloumn to track when ETL was run

df["etl_timestamp"] = datetime.now()

# ===Load =====
#connect to SQLlite database ( creaet fileif doenst exist)

# Create the folder if it doesn't exist
os.makedirs("db", exist_ok=True)

conn = sqlite3.connect("db/sales_data.db")
# Load the dataframe into a table named 'sales'
# if_exists="replace" will overwrite the table every run 

df.to_sql("sales", conn, if_exists="replace", index=False)  

# Confirmation message
print("✅ ETL pipeline completed successfully.")

# === OPTIONAL: Preview 5 rows from the database ===
print("\n🔍 Previewing 5 rows from 'sales' table:")
preview_df = pd.read_sql_query("SELECT * FROM sales LIMIT 5", conn)
print(preview_df)


