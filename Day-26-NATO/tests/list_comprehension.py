list = [1, 2, 3]

#   LIST COMPREHENSION
#new_list = [new_item for item in list]

new_list = [number + 1 for number in list]

print(list)
print(new_list)

name = "Fukurou"
new_name = [letter for letter in name]

print(new_name)

doubled_numbers = [number * 2 for number in range(1, 5)]
print(doubled_numbers)

#   CONDITIONAL LIST COMPREHENSION
#new_list = [new_item for item in list if test]

names = ["Fukurou", "Yuji", "Ookami", "Massao", "Erdtree"]
short_names = [name for name in names if len(name) < 7]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 7]
print(long_names)
