#Squirrel Sorting Project

import pandas

data = pandas.read_csv("Day-25/squirrels/squirrel_data.csv")

color_list = data['Primary Fur Color'].tolist()
num_gray_squirrels = color_list.count('Gray')
num_black_squirrels = color_list.count('Black')
num_cinnamon_squirrels = color_list.count('Cinnamon')

colors_dict = {
    'colors': ['Gray', 'Black', 'Cinnamon'],
    'number': [num_gray_squirrels, num_black_squirrels, num_cinnamon_squirrels],
}

pandas.DataFrame(colors_dict).to_csv(f"Day-25/squirrels/squirrel_data_filtered.csv")

