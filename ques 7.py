year=int(input("enter a year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
  print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

output:
enter a year:1567
1567 is not a leap year.
