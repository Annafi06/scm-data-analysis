import pandas as pd
import sqlite3

DB_PATH = "database/scm.db"
OUTPUT_PATH = "dashboard/dashboard_data.csv"

# connect to database
conn = sqlite3.connect(DB_PATH)

# query data
query = """
SELECT *
FROM orders
"""

df = pd.read_sql(query, conn)

conn.close()

print("Data loaded from database.")

orders_by_status = df.groupby("status").size().reset_index(name="total_orders")

revenue_by_city = df.groupby("city")["price"].sum().reset_index()

avg_distance = df["distance_km"].mean()

orders_by_date = df.groupby("order_date").size().reset_index(name="orders")

summary = pd.DataFrame({
    "metric": [
        "total_orders",
        "average_distance"
    ],
    "value": [
        len(df),
        avg_distance
    ]
})

orders_by_status.to_csv("dashboard/orders_by_status.csv", index=False)
revenue_by_city.to_csv("dashboard/revenue_by_city.csv", index=False)
orders_by_date.to_csv("dashboard/orders_by_date.csv", index=False)
summary.to_csv("dashboard/summary_metrics.csv", index=False)

print("Dashboard data generated.")

