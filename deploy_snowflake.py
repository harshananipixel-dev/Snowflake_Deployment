import os
import snowflake.connector

def get_connection():
    return snowflake.connector.connect(
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        role=os.environ["SNOWFLAKE_ROLE"],
    )

def run_sql_file(cursor, file_path):
    print(f"🔹 Running {file_path}...")
    with open(file_path, "r") as f:
        sql = f.read()
    # Split by semicolon to allow multiple statements per file
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    for stmt in statements:
        cursor.execute(stmt)

def main():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Ensure warehouse is active
        cursor.execute(f"USE WAREHOUSE {os.environ['SNOWFLAKE_WAREHOUSE']}")
        
        sql_folder = "sql"
        for filename in sorted(os.listdir(sql_folder)):
            if filename.endswith(".sql"):
                run_sql_file(cursor, os.path.join(sql_folder, filename))

        print("✅ All SQL files executed successfully!")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
