import random
random_numbers=set(random.sample(range(15,45),(10)))
count_less_than_30=sum(1 for num in random_numbers if num<30)
filtered_numbers={num for num in random_numbers if num<=35}
print("random numbers:",random_numbers)
print("count of numbers less than 30:",count_less_than_30)
print("numbers after deleting numbers greater than 35:",filtered_numbers)

output:
random numbers: {32, 33, 39, 16, 20, 21, 22, 23, 26, 29}
count of numbers less than 30: 7
numbers after deleting numbers greater than 35: {32, 33, 16, 20, 21, 22, 23, 26, 29}
