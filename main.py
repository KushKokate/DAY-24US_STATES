import turtle
import pandas
screen = turtle.Screen()
screen.title("US 50 game")
# set the image of the US to a variable in gif format
image = "usmaps.gif"
# using addshape() function where we can add shape
screen.addshape(image)
turtle.shape(image)

# use to read csv data
data = pandas.read_csv("50_states.csv")
# convert th data to a list using "to.list()"
all_states = data.state.to_list()
#make list for the guessed states and missed states
guessed_states = []
missed_States = []
#using while loop
while len(guessed_states) < 50:
    #textinput func helps to take input and makes a field to take input
    #using to title() to cinvert the input string's first letter to capital even if we write in any manner ex: "angel" or "ANgeLA"-> "Angel"
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt= "What's the state of your game?").title()
    if answer_state == "Exit":
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:

                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('missing_states.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[answer_state == data.state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
