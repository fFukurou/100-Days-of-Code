#Raising Own Exceptions

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 4:
    raise ValueError("Human height should not be over 4 meters.")

bmi = weight / height ** 2
print(bmi)