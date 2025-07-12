import random
# number = random.randint(1,2)
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")

#List
#example: Fruits = ["Apple", "Banana", "Orange"]
# It has a order
# names = ["Alice", "Bob", "Charlie", "David","Emmanuel"]
# payer = random.randint(0,len(names)-1)
# print(names[payer])
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

comp_options = [rock, paper, scissor]
user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if user_option > 2:
    print("You typed an invalid number, you lose!")
else:
    user_selects = comp_options[user_option]
    comp_selects = comp_options[random.randint(0, 2)]
    print(f"Computer chose:\n{comp_selects}")
    print(f"You chose: {user_selects} \n")
    if user_option == comp_selects:
        print("It's a tie")
    elif user_selects == rock and comp_selects == paper:  # rock vs paper
        print("You loose!")
    elif user_selects == paper and comp_selects == rock:
        print("You win!")
    elif user_selects == paper and comp_selects == scissor:
        print("You loose!")
    elif user_selects == scissor and comp_selects == paper:
        print("You win!")
    elif user_selects == scissor and comp_selects == rock:
        print("You loose!")
    elif user_selects == rock and comp_selects == scissor:
        print("You win!")