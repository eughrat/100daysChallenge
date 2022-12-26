import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
all_states = states["state"].to_list()
guessed_states= []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


to_learn = [i for i in all_states if i not in guessed_states]
states_to_learn =  {"states_to_learn":to_learn}
states_to_learn_df = pd.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")

print(states_to_learn)



screen.exitonclick()