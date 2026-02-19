
USE DATABASE company;

USE SCHEMA employee_schema;

-- Insert Sample Data
INSERT INTO employees VALUES
(1, 'John Doe', 'IT', 85000, '2023-01-15'),
(2, 'Jane Smith', 'HR', 75000, '2022-03-10'),
(3, 'Mike Johnson', 'Finance', 95000, '2021-07-25');


-- Create Department Table
CREATE OR REPLACE TABLE departments (
    dept_id INT,
    dept_name STRING
);

INSERT INTO departments VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');
