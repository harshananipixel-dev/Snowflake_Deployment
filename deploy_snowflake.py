def main():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Explicitly set the warehouse first
        execute_sql(cursor, f"USE WAREHOUSE {os.environ['SNOWFLAKE_WAREHOUSE']}")

        # Create database and schema
        execute_sql(cursor, "CREATE DATABASE IF NOT EXISTS company")
        execute_sql(cursor, "USE DATABASE company")
        execute_sql(cursor, "CREATE SCHEMA IF NOT EXISTS employee_schema")
        execute_sql(cursor, "USE SCHEMA employee_schema")

        # Create tables
        execute_sql(cursor, """
        CREATE OR REPLACE TABLE employees (
            id INT,
            name STRING,
            department STRING,
            salary NUMBER(10,2),
            hire_date DATE
        )
        """)
        execute_sql(cursor, """
        CREATE OR REPLACE TABLE departments (
            dept_id INT,
            dept_name STRING
        )
        """)

        # Insert sample data
        execute_sql(cursor, """
        INSERT INTO employees VALUES
        (1, 'John Doe', 'IT', 85000, '2023-01-15'),
        (2, 'Jane Smith', 'HR', 75000, '2022-03-10'),
        (3, 'Mike Johnson', 'Finance', 95000, '2021-07-25')
        """)
        execute_sql(cursor, """
        INSERT INTO departments VALUES
        (1, 'IT'),
        (2, 'HR'),
        (3, 'Finance')
        """)

        print("✅ Snowflake deployment completed successfully!")

    finally:
        cursor.close()
        conn.close()
