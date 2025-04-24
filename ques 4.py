menu = [
    ("Burger", 120),
    ("Pizza", 250),
    ("Sandwich", 90),
    ("Pasta", 150),
    ("Fries", 70)
]
menu_sorted = sorted(menu, key=lambda x: x[1], reverse=True)
print("Menu sorted by price (high to low):")
for item in menu_sorted:
    print(f"{item[0]} - ${item[1]}")

Output:
Menu sorted by price (high to low):
Pizza - $250
Pasta - $150
Burger - $120
Sandwich - $90
Fries - $70
