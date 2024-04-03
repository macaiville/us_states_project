import turtle
import pandas

data = pandas.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states = data.state.to_list()

def move(x,y):
    turtle.goto(x,y)

counter = 0
while counter < 50:
    answer_box = screen.textinput(title = f'{counter}/50 Guess The State', prompt="Whats another State name")
    answer_box = answer_box.title()
    if answer_box in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_box]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_box)
        # turtle.stamp()
        counter += 1

            


state_data = data[data.state == "Ohio"]
print(int(state_data.y))







turtle.mainloop()