data = {
    101: [(1, 50000), (2, 60000), (3, 55000)],
    102: [(4, 70000), (5, 75000), (6, 72000)],
    103: [(7, 40000), (8, 45000), (9, 42000)]
}
for dept_no, employees in data.items():
    salaries = [salary for roll_no, salary in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)
    print(f"Department {dept_no} - Minimum Salary: {min_salary}, Maximum Salary: {max_salary}")

Output:
Department 101 - Minimum Salary: 50000, Maximum Salary: 60000
Department 102 - Minimum Salary: 70000, Maximum Salary: 75000
Department 103 - Minimum Salary: 40000, Maximum Salary: 45000
