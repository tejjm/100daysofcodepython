# 1) Display the art visuals
# 2) From the data take two options and show A & B
# 3) Take input from user to select A or B
# 4) If correct then Increase score and move B to A
# 5) Else end the game and display the score
#Displaying the logo
from calendar import day_name

def higher_lower():
    from art import logo
    from art import vs
    print(logo)
    from game_data import data
    import random as re
    game = True
    score = 0
    a = re.choice(data)
    b = re.choice(data)
    print("Welcome to Higher Lower 2025")
    print("Select which option you would think has higher follower count!")
    while game:
        a_name = a['name']
        a_descp = a['description']
        a_country = a['country']
        a_follower_count = a['follower_count']
        b_name = b['name']
        b_descp = b['description']
        b_country = b['country']
        b_follower_count = b['follower_count']
        print(f'A :{a_name}, {a_descp}, from {a_country}.')
        print(vs)
        print(f'B :{b_name}, {b_descp}, from {b_country}.')
        # Creating variables for comparision
        winner = ''
        loser = ''
        user_selected = ''
        # Taking user input and then assigning to variables based on selection
        user_input = input('Select A or B\n').upper()

        if user_input == 'A':
            user_selected = a
        elif user_input == 'B':
            user_selected = b
        else:
            print("You didn't select the right input")
        # Checking follower count between a and b to find the winner
        if a_follower_count > b_follower_count:
            winner, loser = a, b
        else:
            winner, loser = b, a
        # Check if user selected winner or loser
        if winner == user_selected:
            score += 1
            print(f'Score : {score}')
            a = b
            b = re.choice(data)
        elif loser == user_selected:
            print(f'You have lost now, Score : {score}')
            print(f"{a_name} has {a_follower_count} million followers and {b_name} has {b_follower_count}  million followers.")
            game = False


higher_lower()