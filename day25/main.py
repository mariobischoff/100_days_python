with open("weather.csv") as data_file:
    data = data_file.readlines()
    print(data)


import csv

with open("weather.csv") as data_file:
    data = csv.reader(data_file)
    temp_min = []
    temp_max = []
    for row in data:
        temp_min.append(row[0])
        temp_max.append(row[1])

print(temp_min[1:])
print(temp_max[1:])



import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    print(data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)





import pandas as pd

data = pd.read_csv("weather_data.csv")

temperatures = data["temp"]
temperatures.max()

#Get Data in Columns
data["condition"]
data.condition

#Get Data in Row
data[data.temp == data.temp.max()]
data[data.condition == "rain"]

monday = data[data.day == "monday"]
temp_c = int(monday.temp)

# convert to Fº
temp_f = 1.8 * temp_c + 32
temp_f


# create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")





data = pd.read_csv("squirrel_data.csv")

colors = data[data["Primary Fur Color"]].dropna().unique()

new_data = {"fur color": [], "count": []}

for color in colors:
    new_data["fur color"].append(color)
    new_data["count"].append(len(data[data["Primary Fur Color"] == color]))

df = pd.DataFrame(new_data)
df.to_csv("squirrel_count.csv")






