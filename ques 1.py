names = ["Anjali", ("Rahul",), "Sneha", ("Amit",), "Priya", ("Karan",), "Meena"]
boys_count = 0
girls_count = 0
for person in names:
    if isinstance(person, tuple):
        boys_count += 1
    else:
        girls_count += 1
print("Total number of boys:", boys_count)
print("Total number of girls:", girls_count)

Output:
Total number of boys: 3
Total number of girls: 4
