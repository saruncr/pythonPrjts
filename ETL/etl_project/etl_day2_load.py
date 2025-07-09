import pandas as pd
import sqlite3
import os

# Ensure 'db' folder exists
os.makedirs("db", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("db/sales_data.db")

# === EXTRACT ===
df_customers = pd.read_csv("data/customers.csv")
df_orders = pd.read_csv("data/orders.csv")

# === LOAD ===
df_customers.to_sql("customers", conn, if_exists="replace", index=False)
df_orders.to_sql("orders", conn, if_exists="replace", index=False)

print("✅ Customers and Orders loaded into SQLite successfully.")
