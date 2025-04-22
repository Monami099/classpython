print("24 Hours of the Day with Suffixes:")
for hour in range(24):
    if hour == 0:
        print("12:00 MIDNIGHT")
    elif hour == 12:
        print("12:00 NOON")
    elif hour < 12:
        print(f"{hour}:00 AM")
    else:
        print(f"{hour - 12}:00 PM")

Output:
12:00 MIDNIGHT
1:00 AM
2:00 AM
...
11:00 AM
12:00 NOON
1:00 PM
2:00 PM
...
11:00 PM
