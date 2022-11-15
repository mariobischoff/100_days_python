import turtle
import pandas as pd

FONT = ("Verdana", 8, "normal")

screen = turtle.Screen()
screen.setup(750, 520)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV
data = pd.read_csv("states_to_learn.csv")
all_states = data["state"].to_list()

states_correct = []


while len(states_correct) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(states_correct)}/{len(all_states)} States Correct", 
        prompt="What's another state's names?").title()

    state_text = turtle.Turtle(visible=False)
    state_text.penup()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        states_correct.append(answer_state)
        state_data = data[data.state == answer_state]
        state_text.goto(int(state_data.x), int(state_data.y))
        state_text.write(answer_state, align="center", font=FONT)

# states_to_learn.csv
data_to_learn = data[~data.state.isin(states_correct)]
data_to_learn.to_csv("states_to_learn.csv")