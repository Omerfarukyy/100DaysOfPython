# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append( int(row[1]))
#
# print(temperatures)
#
import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
###
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Color":  [gray_count, red_count, black_count]

}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
