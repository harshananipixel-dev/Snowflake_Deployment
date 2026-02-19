-- Create Database
CREATE DATABASE IF NOT EXISTS company;

-- Use Database
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
