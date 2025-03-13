import turtle
import pandas


screen=turtle.Screen()
screen.title("Indian States Game")

image="Politicalmap.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)

# turtle.mainloop()

data= pandas.read_csv("state_coordinates.csv")

all_states= data.State.to_list()
guessed_states=[]

while len(guessed_states) < 29:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/29 states correct", prompt="Enter state name").title()

    if answer_state=="Exit":
        break
    

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.State==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)



   


screen.exitonclick()


