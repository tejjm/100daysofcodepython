import turtle
import pandas as pd
from writer import Writer
screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_count = 0
state_list = pd.read_csv("50_states.csv")
only_states = state_list["state"].values #Creates a list of the states
correct_guesses = []
missed_states = []
for state in only_states:
    missed_states.append(state)
while state_count <50:
    answer_state = screen.textinput(title="Guess the states!",prompt=f"Guess another state {state_count}/50")
    titled_answer_state = answer_state.title()#Changing to Title case
    if titled_answer_state == "Exit":
        break
    if titled_answer_state in only_states:
        temp_x = state_list[state_list["state"]==titled_answer_state]["x"].values[0]
        print(temp_x),print(type(temp_x))
        temp_y = state_list[state_list["state"]==titled_answer_state]["y"].values[0]
        print(temp_y),print(type(temp_y))
        writer = Writer(x=temp_x,y=temp_y,answer=titled_answer_state)
        correct_guesses.append(titled_answer_state)
        print("You guessed correct, guess another")
        state_count+=1
        # Creating a csv that saves the states which user missed while guessing
    if titled_answer_state in missed_states:
        missed_states.remove(titled_answer_state)
    else:
        print("Incorrect guess")


missed_states_df = pd.DataFrame(missed_states)
missed_states_df.to_csv("missed_states.csv")