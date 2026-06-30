# SQL
# Table employees {
#   id integer [primary key]
#   name varchar(50)
#   department varchar(50)
#   salary integer
#   age integer [check: `age > 0`]
# }

# -- SELECT name, salary
# -- FROM employees

# -- SELECT name
# -- FROM employees
# -- WHERE salary > 55000

# SELECT *
# FROM  employees
# WHERE department = 'IT';

# -- SELECT name 
# -- FROM employees
# -- WHERE age > 29 and salary > 55000