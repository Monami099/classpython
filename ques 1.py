dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
dict4 = {**dict1, **dict2, **dict3}
print("Fourth Dictionary (Concatenated):", dict4)

Output:
Fourth Dictionary (Concatenated): {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
