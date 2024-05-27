#Tip Calculator Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))

tip_percent = float("1." + tip)
bill_after_tip = (bill * tip_percent) / people
print(f"Each person should pay: {bill_after_tip:.2f}")
