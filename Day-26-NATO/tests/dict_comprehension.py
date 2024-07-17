import random

names = ["Godrick", "Radagon", "Fukurou", "Merlim", "Erdtree"]

#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

students_scores = {student:random.randint(1, 100) for student in names}

print(students_scores)

passed_students = {student:grade for (student, grade) in students_scores.items() if grade >= 70}

print(passed_students)


