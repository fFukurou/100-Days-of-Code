with open("Day-24/tests/test_file.txt", 'a') as file:
    file.write("\nImma try to finish Hogwarts Legacy before it drops though.")

with open("Day-24/tests/test_file.txt", 'r') as file:
    contents = file.read()
    print(contents)