import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = data["Primary Fur Color"].value_counts()  # short method
# colors.to_csv("Squirrel_colour_data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

colors_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Color count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(colors_dict)
new_data.to_csv("squirrel_colors.csv")
