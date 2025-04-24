list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 10, 11]
list3 = [num for num in list1 if num not in list2]
print("First List:", list1)
print("Second List:", list2)
print("Third List (Elements in first list but not in second):", list3)

Output:
First List: [1, 2, 3, 4, 5, 6, 7]
Second List: [4, 5, 6, 10, 11]
Third List (Elements in first list but not in second): [1, 2, 3, 7]
