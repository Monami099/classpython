students = [
    (101, "Anjali", 18),
    (102, "Rahul", 19),
    (103, "Sneha", 18),
    (104, "Amit", 20)
]
roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]
print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

Output:
Roll Numbers: [101, 102, 103, 104]
Names: ['Anjali', 'Rahul', 'Sneha', 'Amit']
Ages: [18, 19, 18, 20]
