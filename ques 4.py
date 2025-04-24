input_string = input("Enter a string: ")
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1  # Increment count if character already exists
    else:
        char_frequency[char] = 1  # Initialize count if character is new
print("Character Frequency in the string:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")

Output:
Enter a string: hello world
Character Frequency in the string:
'h': 1
'e': 1
'l': 3
'o': 2
' ': 1
'w': 1
'r': 1
'd': 1
