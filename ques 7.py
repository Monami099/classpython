import pickle
from datetime import datetime
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj  
        self.salary = salary
    def __str__(self):
        return f"EmpCode: {self.empcode}, Name: {self.empname}, Date of Joining: {self.doj.strftime('%Y-%m-%d')}, Salary: {self.salary}"
def serialize_employee(emp, filename):
    with open(filename, 'wb') as file:
        pickle.dump(emp, file)
    print(f"Employee data has been serialized and saved to {filename}")
def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        emp = pickle.load(file)
    return emp
emp1 = Employee(empcode=101, empname="John Doe", doj=datetime(2020, 5, 15), salary=55000)
filename = "employee_data.pkl"
serialize_employee(emp1, filename)
emp2 = deserialize_employee(filename)
print("\nDeserialized Employee Data:")
print(emp2)
