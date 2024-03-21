import csv
import pandas


# with open("weather_data.csv", mode="r") as data:
#     weather_csv = data.readlines()
#     print(weather_csv)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # # series = pandas.Series(temp_list)
# # # temp_total = series.sum()
#
# #Get Data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp[0]*9/5+32)

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
#

#Fur, Colour, Count
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240304.csv")

total_grey = (data["Primary Fur Color"] == "Gray").sum()
print(total_grey)
total_red = (data["Primary Fur Color"] == "Cinnamon").sum()
print(total_red)
total_black = (data["Primary Fur Color"] == "Black").sum()
print(total_black)

# squirrel_data = [
#     ["Fur Colour", "Count"],
#     ["grey", total_grey],
#     ["red", total_red],
#     ["black", total_black]
# ]

# with open(squirrel_path, mode="w") as file:
#     writer = csv.writer(file)
#     writer.writerows(data_dict)

squirrel_path = "squirrel_data.csv"

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [total_grey, total_red, total_black]
}

with open(squirrel_path, mode="w") as file:
    writer = csv.writer(file)
    writer.writerows(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")




