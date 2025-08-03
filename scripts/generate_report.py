# scripts/generate_report.py

import pandas as pd
import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("❌ Could not connect:", e)
        exit()

def generate_time_summary(conn):
    query = """
    SELECT 
        e.name AS employee,
        t.name AS task,
        SUM(l.hours_logged) AS total_hours
    FROM time_logs l
    JOIN employees e ON l.employee_id = e.id
    JOIN tasks t ON l.task_id = t.id
    GROUP BY e.name, t.name
    ORDER BY e.name;
    """

    df = pd.read_sql_query(query, conn)
    df.to_csv("../reports/time_summary.csv", index=False)
    print("✅ Report saved to reports/time_summary.csv")

if __name__ == '__main__':
    conn = connect_db()
    generate_time_summary(conn)
    conn.close()
