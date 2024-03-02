import turtle
import pandas
screen = turtle.Screen()
screen.title("US 50 game")
image = "usmaps.gif"
screen.addshape(image)
turtle.shape(image)

#def get_mouse_click_coor(x, y):
#   print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missed_States = []
while len(guessed_states) < 50:
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
