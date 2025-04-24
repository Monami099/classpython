prices = {
    "apple": 30,
    "banana": 20,
    "milk": 50,
    "bread": 40
}
quantity = {
    "apple": 3,
    "banana": 5,
    "milk": 2,
    "bread": 1
}
total_bill = 0
for item in prices:
    if item in quantity:  # Ensure item exists in both dictionaries
        total_bill += prices[item] * quantity[item]
print("Total Bill: $", total_bill)

Output:
Total Bill: $ 250
