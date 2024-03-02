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

answer_state = screen.textinput(title="Guess the states", prompt= "What's the state of your game?")

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[answer_state == data.state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())
screen.exitonclick()