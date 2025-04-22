print("Pythagorean Triplets with side length ≤ 30:")
for a in range(1, 31):
    for b in range(a, 31): 
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= 30:
            print(f"({a}, {b}, {int(c)})")

Output:
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
(7, 24, 25)
(8, 15, 17)
(9, 12, 15)
(10, 24, 26)
(12, 16, 20)
(15, 20, 25)
(18, 24, 30)
