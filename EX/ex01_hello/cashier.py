"""Calculates the change needed to give."""
amount = int(input("Enter a sum: "))
coins = amount // 50 + amount % 50 // 20 + amount % 50 % 20 // 10 + amount % 50 % 20 % 10 // 5 +\
    amount % 50 % 20 % 10 % 5
print(f"Amount of coins needed: {coins}")
