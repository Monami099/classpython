from datetime import date
date1 = (24, 4, 2025)
date2 = (1, 1, 2025)
d1 = date(date1[2], date1[1], date1[0])  # year, month, day
d2 = date(date2[2], date2[1], date2[0])  # year, month, day
difference = abs((d1 - d2).days)
print(f"Date 1: {d1}")
print(f"Date 2: {d2}")
print(f"Number of days between the two dates: {difference}")

Output:
Date 1: 2025-04-24
Date 2: 2025-01-01
Number of days between the two dates: 113
