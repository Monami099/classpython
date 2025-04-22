import random
random_integers = [random.randint(1, 100) for _ in range(20)]
print("List of 20 random integers:", random_integers)
user_number = int(input("\nEnter a number to find its positions in the list: "))
positions = [index for index, value in enumerate(random_integers) if value == user_number]
if positions:
    print(f"The number {user_number} is found at positions: {positions}")
else:
    print(f"The number {user_number} is not found in the list.")

Output:
List of 20 random integers: [47, 89, 23, 54, 77, 23, 12, 33, 89, 12, 56, 89, 23, 34, 23, 56, 12, 45, 89, 78]
Enter a number to find its positions in the list: 23
The number 23 is found at positions: [2, 5, 12, 14]
