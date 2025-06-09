# with open("weather.csv") as file_weather:
#     data = file_weather.readlines()
# print(data)
# import csv
# with open("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#
# #     print(temperatures)
# import pandas
# data = pandas.read_csv("weather.csv")
# print(data)
# data_to_dict = data.to_dict()
# print(data_to_dict)
#
# temp_list = data["temp"].to_list()
# temp_list = data.temp.tolist()
#
# total_temp = sum(temp_list)
#
#
#
# total_temp = total_temp / len(temp_list)
#
# print(total_temp)
#
# print(data["temp"].mean())
#
# #forma de acceder a las columnas
# print(data["temp"].max())
# #otra forma de hacerlo ya que pandas toma las columnas y filas como atributos
# print(data.temp.max())

# #como obtener datos que estan en una fila
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])

# max_value = data.temp.max()
# print(data[data.temp == max_value])
# print(data[data.temp == data.temp.max()])

# #obtener un valor de una lista
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
# print(monday.temp * 9/5 + 32)

# #crear un dataframe desde cero
# data_dict = {
#     "students" : ["Dani", "Lucas", "Aure"],
#     "score" : [40, 50, 60]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# import pandas
# data = pandas.read_csv("squirrel_data.csv")
# four_colors = data.Primary_Fur_Color.tolist()
# print(four_colors)
# #otra forma mas sencilla de hacer esto
# grey_squirrels_count = len(data[data["Primary_Fur_Color"] == "Gray"])
# print(grey_squirrels_count)
# gray_color = 0
# black_color = 0
# cinnamon_color = 0
#
# for colors in four_colors:
#     if colors == "Gray":
#         gray_color += 1
#     elif colors == "Black":
#         black_color += 1
#     elif colors == "Cinnamon":
#         cinnamon_color += 1
#     else:
#         pass
# #print(gray, black, cinnamon)
# data_dict = {
#     "Four color" : ["Gray", "Black", "Cinnamon"],
#     "count" : [gray_color, black_color, cinnamon_color]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")