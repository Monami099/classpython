import random
random_numbers=random.sample(range(-15,16),10)
squared_numbers=[x**2 for x in random_numbers]
print("random numbers:",random_numbers)
print("squared numbers:",squared_numbers)

output:
random numbers: [5, -1, 0, 12, 3, -11, -7, -4, -6, 15]
squared numbers: [25, 1, 0, 144, 9, 121, 49, 16, 36, 225]
