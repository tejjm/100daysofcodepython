

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
bidders = {}
condition = True
while condition:
    name = input("What is your name?: ")
    price = float(input("Enter your bid:"))
    bidders[name] = price
    more_bidders = (input("Are there any other bidders? Type 'yes or 'no'.\n")).lower()
    if more_bidders == "no":
        condition = False
    if more_bidders == "yes":
        print("\n" * 200)
max = 0
winner = ""
for name in bidders:
    if bidders[name] > max:
        max = bidders[name]
        winner = name
print(f"The winner is {winner} with a bid of ${max}")






