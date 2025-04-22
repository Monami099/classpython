import random
random_numbers = [random.randint(-50, 50) for _ in range(30)]
print("List of 30 Random Numbers:", random_numbers)
positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]
print("\nList of Positive Numbers:", positive_numbers)
print("List of Negative Numbers:", negative_numbers)

Output:
List of 30 Random Numbers: [-29, 47, 12, 20, -36, -27, 9, -15, -16, -6, -1, -47, -4, -25, 33, -38, 12, -7, -23, 4, 30, -17, -48, 26, -5, 15, -10, 1, 34, -8]
List of Positive Numbers: [47, 12, 20, 9, 33, 12, 4, 30, 26, 15, 1, 34]
List of Negative Numbers: [-29, -36, -27, -15, -16, -6, -1, -47, -4, -25, -38, -7, -23, -17, -48, -5, -10, -8]
