# # import csv
# #
# # with open("weather_data.csv") as my_data:
# #     data = csv.reader(my_data)
# #     temperature = []
# #     for col in my_data:
# #         if col[1] != "temp":
# #             temperature.append(int(col[1]))
# #     print(temperature)
#
# # ------------------------------------------------------------------- #
#
# import pandas
#
#
# # temp_list = data['temp'].to_list()
# # print(temp_list)
#
# # avg = sum(temp_list) / len(temp_list)
# # print(round(avg,2))
# #
# # max_value = data['temp'].max()
# # print(max_value)
# #
# # min_value = data['temp'].min()
# # print(min_value)
#
# # monday = data[data.day == 'Monday']  #selecting the row
# #
# # monday_temp = monday.temp[0]
# # temp_in_f = monday_temp * 9/5 + 32
# #
# # print(f"monday temp in F:{temp_in_f}")
#
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# s_list = data['Primary Fur Color'].to_list()
# print(s_list)
#
# gray_s_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_s_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# white_s_count = len(data[data["Primary Fur Color"] == "Black"])
#
# counts = {'color': ["Gray", "Cinnamon", "Black"], 'count': [gray_s_count,cinnamon_s_count,white_s_count]}
#
# squirrel_data = pandas.DataFrame(counts)
#
# squirrel_data.to_csv("squirrel colors count")
# # s_list = data['Primary Fur Color'].to_list()
# # print(s_list)
# # #s_data = data[data.color == 'Primary Fur Color']
# #
# # df = pandas.DataFrame(s_list)
# # print(df)
import turtle
from turtle import Screen
import pandas as pd

state_data = pd.read_csv("50_states.csv")
screen = Screen()
screen.title("50 states of U.S")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_list = state_data["state"].to_list()
mylist = []

while len(mylist) < 50:
    user_guess = screen.textinput(title=f"{len(mylist)}/50 Correct" ,
                                  prompt="Guess a state name? ").title()

    if user_guess == "Exit":
        missing_state = []
        for state in state_list:
            if state not in mylist:
                missing_state.append(state)
        print(missing_state)
        break

    if user_guess in state_list:
        if user_guess in mylist:
            continue
        else:
            s_name = turtle.Turtle()
            s_name.penup()
            s_name.hideturtle()
            state = state_data[state_data.state == user_guess]
            s_name.goto(int(state.x) , int(state.y))
            s_name.write(user_guess)  # s_name.write(state.state.item())
            mylist.append(user_guess)
    else:
        continue

screen.exitonclick()
# problem break down

# creating user input
# cheking the user input is same as the csv data
# if same write it on the screen
# if not repeat the process
