def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == n
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))
num = int(input("Enter a number: "))
print(f"\nChecking properties for: {num}")
print("Prime Number?     :", "Yes" if is_prime(num) else "No")
print("Perfect Number?   :", "Yes" if is_perfect(num) else "No")
print("Armstrong Number? :", "Yes" if is_armstrong(num) else "No")
print("Palindrome?        :", "Yes" if is_palindrome(num) else "No")
print("Automorphic?       :", "Yes" if is_automorphic(num) else "No")

Output:
Enter a number: 153
Checking properties for: 153
Prime Number?     : No
Perfect Number?   : No
Armstrong Number? : Yes
Palindrome?        : No
Automorphic?       : No
