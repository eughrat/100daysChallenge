# with open("weather_data.csv","r") as f:
#     rows = f.readlines()
#     print(rows)
#
#

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
[print(data_dict)]

data_list = data["temp"].to_list()
[print(data_list)]

avg_temp = data["temp"].mean()
avg_max = data["temp"].max()

print(avg_max)
print(avg_temp)

monday_data = data[data["day"] == "Monday"]
print(monday_data)

data_temp_max = data[data["temp"] == data["temp"].max()]
print(data_temp_max)

df = pandas.DataFrame(data_dict)
print(df)

