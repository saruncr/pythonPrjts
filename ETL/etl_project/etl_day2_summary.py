import sqlite3
import pandas as pd

# Connect to the existing database
conn = sqlite3.connect("db/sales_data.db")

# === SQL JOIN: Total orders per customer ===
query = """
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_amount DESC;
"""

# Run the query
summary_df = pd.read_sql_query(query, conn)

# Save to new SQLite table
summary_df.to_sql("customer_summary", conn, if_exists="replace", index=False)

# Save to CSV
summary_df.to_csv("data/summary.csv", index=False)

print("✅ Summary table and CSV created successfully.")
