tuple_list = [("apple",), (), ("banana",), (), ("cherry",), ()]
filtered_list = [t for t in tuple_list if t]
print("Original list:", tuple_list)
print("List after removing empty tuples:", filtered_list)

Output:
Original list: [('apple',), (), ('banana',), (), ('cherry',), ()]
List after removing empty tuples: [('apple',), ('banana',), ('cherry',)]
