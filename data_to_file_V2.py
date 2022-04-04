# Source: https://www.pythontutorial.net/python-basics/python-write-text-file/
import re

# Data to be put in text file
data = ['Scout 1', 'Soldier 2', 'Pyro 3', 'Demoman 4', 'Heavy 5']
print(data)

has_errors = "yes"
while has_errors == "yes":
    has_errors = "no"
    filename = input("Enter a filename (leave off the .txt): ")

    valid_chars = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_chars, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"

        else:
            problem = f"(no {letter}'s allowed)"
        has_errors = "yes"

    if filename == "":
        problem = "(can't be blank)"
        has_errors = "yes"

    if has_errors == "yes":
        print(f"Invalid filename - {problem}")
        print()

    else:
        print("You entered a valid filename.")

        filename = filename + ".txt"
        print(filename)

        # Create new file to store data
        f = open(filename, "w+")

        # Add data to file
        for item in data:
            f.write(item + "\n")

        # Stop writing
        f.close()
