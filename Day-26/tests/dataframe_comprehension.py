import pandas as pd

student_dict = {"Student": ["Fukurou", "Poppy", "Ominis", "Sebastian"], 
             "Score": [87, 79, 90, 89]
}

student_data_frame = pd.DataFrame(student_dict)

""" for (key, value) in student_data_frame.items():
    print(value) """

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row['Student'])
    if row['Student'] == "Fukurou": print("THE GOAT!")

#{new_key:new_value for (index, row) in dataframe.iterrows()}