"""Greets anyone."""

greeting = input("Enter a greeting: ")
recipient = input("Enter a recipient: ")
repeat = int(input("How many times to repeat: "))
print((f"{greeting} " + f"{recipient}! ") * repeat)
