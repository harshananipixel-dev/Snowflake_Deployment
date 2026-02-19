def main():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # 1️⃣ Activate warehouse (must exist)
        cursor.execute(f"USE WAREHOUSE {os.environ['SNOWFLAKE_WAREHOUSE']}")

        # 2️⃣ Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS company")
        cursor.execute("USE DATABASE company")

        # 3️⃣ Create schema if it doesn't exist
        cursor.execute("CREATE SCHEMA IF NOT EXISTS employee_schema")
        cursor.execute("USE SCHEMA employee_schema")

        # Now run all SQL files
        sql_folder = "sql"
        for filename in sorted(os.listdir(sql_folder)):
            if filename.endswith(".sql"):
                print(f"Running {filename}...")
                with open(os.path.join(sql_folder, filename), "r") as f:
                    sql = f.read()
                    statements = [s.strip() for s in sql.split(";") if s.strip()]
                    for stmt in statements:
                        cursor.execute(stmt)

        print("✅ All SQL files executed successfully!")

    finally:
        cursor.close()
        conn.close()
