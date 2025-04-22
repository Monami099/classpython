n = int(input("Enter how many Fibonacci numbers to generate: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

Output:
Enter how many Fibonacci numbers to generate: 7
Fibonacci Series:
0 1 1 2 3 5 8
