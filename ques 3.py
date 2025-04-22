import random
random_numbers = [random.randint(1, 30) for _ in range(50)]
print("List of 50 Random Numbers:", random_numbers)
unique_numbers = list(set(random_numbers))
print("\nList with duplicates removed:", unique_numbers)

Output:
List of 50 Random Numbers: [23, 5, 18, 15, 30, 9, 10, 24, 6, 19, 5, 7, 2, 22, 12, 26, 16, 11, 9, 17, 19, 24, 18, 22, 15, 14, 21, 8, 27, 8, 12, 26, 10, 14, 2, 23, 19, 25, 28, 30, 6, 29, 7, 21, 11, 13, 17, 27, 28, 6]
List with duplicates removed: [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
