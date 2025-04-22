import random
odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("List of 5 Odd Integers:", odd_integers)
even_integers = [random.choice(range(2, 100, 2)) for _ in range(4)]
print("List of 4 Even Integers:", even_integers)
odd_integers[2] = even_integers
print("\nAfter replacing the 3rd element of Odd Integers with Even Integers List:")
print(odd_integers)
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("\nFlattened List:", flattened_list)
flattened_list.sort()
print("\nSorted Flattened List:", flattened_list)

Output:
List of 5 Odd Integers: [85, 61, 97, 13, 9]
List of 4 Even Integers: [58, 34, 2, 80]
After replacing the 3rd element of Odd Integers with Even Integers List:
[85, 61, [58, 34, 2, 80], 13, 9]
Flattened List: [85, 61, 58, 34, 2, 80, 13, 9]
Sorted Flattened List: [2, 9, 13, 34, 58, 61, 80, 85]
