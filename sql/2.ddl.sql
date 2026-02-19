USE DATABASE company;
-- Create Schema
CREATE SCHEMA IF NOT EXISTS employee_schema;

-- Use Schema
USE SCHEMA employee_schema;

-- Create Employee Table
CREATE OR REPLACE TABLE employees (
    id INT,
    name STRING,
    department STRING,
    salary NUMBER(10,2),
    hire_date DATE
);
