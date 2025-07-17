import sqlite3
import pandas as pd
import os

# Connect to the existing SQLite database
conn = sqlite3.connect("db/sales_data.db")

# ─────────────────────────────────────────────
# STEP 2 – Read orders table from DB
# ─────────────────────────────────────────────

df_orders = pd.read_sql_query("SELECT * from orders",conn);


#Filter: only include order with value more than 100
df_orders = df_orders[df_orders["amount"] > 100];

#print After Filter



# Drop rows with any missing values (nulls)
df_orders.dropna(inplace=True)


# Persist cleaned data
df_orders.to_sql("orders_cleaned", conn, if_exists="replace", index=False)

# ─────────────────────────────────────────────
# STEP 4 – Monthly revenue summary
# ─────────────────────────────────────────────
query = """
SELECT 
    strftime('%Y-%m', order_date) AS order_month,
    SUM(amount) AS total_revenue
FROM orders_cleaned
GROUP BY order_month
ORDER BY order_month;
"""

summary_df = pd.read_sql_query(query, conn)

print("\n📊 Monthly Revenue Summary:")
print(summary_df)

# ─────────────────────────────────────────────
# STEP 5 – Save summary to database and CSV
# ─────────────────────────────────────────────

# Save to new SQLite table
summary_df.to_sql("customer_summary", conn,
                  if_exists="replace", index=False)

# Save to CSV
summary_df.to_csv("data/summary.csv", index=False)

print("✅ Summary table and CSV created successfully.")