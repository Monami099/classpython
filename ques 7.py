def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
def nPr(n, r):
    return factorial(n) // factorial(n - r)
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
if r > n:
    print("r should not be greater than n")
else:
    print(f"\nnCr ({n}C{r}) = {nCr(n, r)}")
    print(f"nPr ({n}P{r}) = {nPr(n, r)}")

Output:
Enter value of n: 5
Enter value of r: 2
nCr (5C2) = 10
nPr (5P2) = 20
