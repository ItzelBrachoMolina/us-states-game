import csv
import pandas
import turtle
import pandas as pd


screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()


data=pandas.read_csv('50_states.csv')
number_states=data['state'].count()



countries_found=[]
countries=data['state'].to_list()


while len(countries_found)<len(countries):
    answer_state=screen.textinput(title=f'{len(countries_found)}/50 states',prompt="what's another state").title()
    if answer_state=='Exit':
        missing_states=[]
        for state in countries:
            if state not in countries_found:
                missing_states.append(state)
            print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in countries:
        countries_found.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

