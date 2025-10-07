import sqlite3
from Python_SQLite_Tutorial_Employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                     WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John','Doe',8000)
emp_2 = Employee('Jane','Doe',1000)


c.execute("""CREATE TABLE employees(
        first text,
        last text,
        pay integer
        )""")

insert_emp(emp_1)
insert_emp(emp_2)

getemp = get_emp_by_name('Doe')
print(getemp)
# [('John', 'Doe', 8000), ('Jane', 'Doe', 1000)]

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emp_by_name('Doe')
print(emps)
# [('Jane', 'Doe', 95000)]

conn.close()

