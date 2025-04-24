import csv
data = [
    ["Name", "Age", "Department", "Salary"],
    ["Alice", 30, "HR", 50000],
    ["Bob", 28, "IT", 60000],
    ["Charlie", 35, "Finance", 70000],
    ["David", 40, "Marketing", 65000]
]
filename = "employee_data.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f"CSV file '{filename}' has been created successfully.")
