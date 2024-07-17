#FileNotFound and KeyError
try:
    file = open("Day-30/tests/a_file.txt")

    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

except FileNotFoundError:
    print("File does not exist yet.")
    file = open("Day-30/tests/a_file.txt", "w")
    file.write("Something")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")
    raise TypeError("This is an error that I made up")
