import duckdb
import os

# Ensure db folder exists
os.makedirs("db", exist_ok=True)

db_path = "db/netflix.db"
csv_path = "data/logs.csv"

print("Loading data into DuckDB...")

con = duckdb.connect(database=db_path)

# Drop the table if it exists (so reruns don't fail)
con.execute("DROP TABLE IF EXISTS logs;")

# Load CSV into DuckDB
con.execute(f"""
    CREATE TABLE logs AS
    SELECT * FROM read_csv_auto('{csv_path}');
""")

print("Done! DuckDB table 'logs' created in db/netflix.db")
