lst=['madam','python','malayalam', 12321]
def is_palindrome(s):
    s=str(s)
    return s==s[::-1]
for item in lst:
    if isinstance(item,str) and is_palindrome(item):
        print(f"'{item}' is a palindrome.")

output:
'madam' is a palindrome.
'malayalam' is a palindrome.
