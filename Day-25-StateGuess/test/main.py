import csv
import pandas

""" temperatures = []

with open(f"Day-25-StateGuess/test/weather_data.csv") as file:

    data = csv.reader(file)
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except ValueError:
            pass

print(temperatures) """

data = pandas.read_csv("Day-25-StateGuess/test/weather_data.csv")
#transform dataframe to dict
dict = data.to_dict()
print(dict['day'][1])

#transform column values into list
temp_list = data['temp'].tolist()

avarage_temp = sum(temp_list) / len(temp_list)
print(f"{avarage_temp:.2f}")


#gets the avarage and the highest value of the column 'temp'
print(data['temp'].mean())
print(data['temp'].max())


#prints the row in which the data.temp is equals to 24 (the highest number of them)
print(data[data.temp == data.temp.max()])

#gets a row, then gets a specific number in a row
#gets the row in which the data.day is monday, then gets the temperature in this day
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday_temp)


#create a dataframe and save it to a file
data_dict = {
    'games': ['Hogwarts Legacy', 'Sekiro', 'Path of Exile', 'Enden Ring'],
    'scores': [8, 10, 9, 9],
}

game_data = pandas.DataFrame(data_dict)
game_data.to_csv(f"Day-25/test/game_data.csv")