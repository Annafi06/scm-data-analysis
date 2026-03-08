import sqlite3
import pandas as pd

conn = sqlite3.connect("database/scm.db")

query = """
SELECT 
    status,
    COUNT(*) as total_orders
FROM orders
GROUP BY status
ORDER BY total_orders DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

print(df)