n = int(input("Enter a number: "))
print(f"\nFirst {n} natural numbers in reverse order:")
for i in range(n, 0, -1):
    print(i, end=' ')

Output:
Enter a number: 5
First 5 natural numbers in reverse order:
5 4 3 2 1
