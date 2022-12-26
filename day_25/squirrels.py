import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data.head())
# print(data.columns)
# print(data["Primary Fur Color"].value_counts())

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# print(gray_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, gray_count, black_count]
}

color_df = pd.DataFrame(data_dict)
color_df.to_csv("color_of_squirrels.csv")
