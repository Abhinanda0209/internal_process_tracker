# scripts/ingest_data.py

import pandas as pd
import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Connected to the database.")
        return conn
    except Exception as e:
        print("❌ Failed to connect:", e)
        exit()

def load_csv_to_db(table_name, csv_path, conn):
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        values = tuple(row)
        placeholders = ','.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(query, values)

    conn.commit()
    cursor.close()
    print(f"✅ Loaded {len(df)} rows into {table_name}")

if __name__ == '__main__':
    conn = connect_db()

    load_csv_to_db('employees', '../data/sample_employees.csv', conn)
    load_csv_to_db('tasks', '../data/sample_tasks.csv', conn)
    load_csv_to_db('time_logs', '../data/sample_time_logs.csv', conn)

    conn.close()
    print("✅ Ingestion complete.")
