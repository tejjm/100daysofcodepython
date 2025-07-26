# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random
from random import choice


def draw():
    print("You both have the same cards.. It's a draw")
def user_looses():
    print("You loose!!")
def user_wins():
    print("You Win!!!!")
def black_jack():
    from art import logo
    import random as re
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    users_hand = [re.choice(cards),re.choice(cards)]
    computers_hand = [re.choice(cards),re.choice(cards)]
    print(f'Your hand {users_hand}')
    print(f'Computers hand {[random.choice(computers_hand)]}')
    if sum(users_hand) == 21 and sum(computers_hand) == 21:
        print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
        print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
        return draw
    user_choice = (input("Hit or Stand\n")).lower()
    if user_choice == 'hit':
        adder = re.choice(cards)
        if sum(users_hand) > 10 and adder == 11:
            adder = 1
        users_hand.append(adder)
    c_choice = re.choice(['hit','stand'])
    if c_choice == 'hit':
        computers_hand.append(re.choice(cards))
    if sum(users_hand) > 21 and sum(computers_hand) <= 21:
        print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
        print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
        print("You went over 21")
        return user_looses()
    if sum(users_hand) <=21 and sum(computers_hand) > 21:
        print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
        print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
        print("Computer went over 21")
        return user_wins()
    elif sum(users_hand) <= 21 and sum(computers_hand) <= 21:
        if sum(users_hand) > sum(computers_hand):
            print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
            print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
            return user_wins()
        elif sum(users_hand) == sum(computers_hand):
            print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
            print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
            return draw()
        else:
            print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
            print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
            return user_looses()
    elif sum(users_hand) > 21 and sum(computers_hand) > 21:
        print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
        print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
        return draw()
    else:
        print(f"Your hand is {users_hand} and total score is {sum(users_hand)}\n")
        print(f"Computers hand is {computers_hand} and total score is {sum(computers_hand)}\n")
        return user_looses()




game = (input("Do you want to play a game of Black Jack? Type y or n\n")).lower()
while game != 'n':
    black_jack()
    game = (input("Do you want to play another game of Black Jack? Type y or n\n")).lower()
    if game == 'y':
        print("\n"*100)