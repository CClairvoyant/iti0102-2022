amount = int(input("Enter a sum: "))

coin1 = amount % 50
coin2 = coin1 % 20
coin3 = coin2 % 10
coin4 = coin3 % 5
coin5 = coin4 % 1

coins = ((amount-coin1)/50) + ((coin1-coin2)/20) + ((coin2-coin3)/10) + ((coin3-coin4)/5) + ((coin4-coin5)/1)

print(f"Amount of coins needed: {coins}")
