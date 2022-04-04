# Source: https://www.pythontutorial.net/python-basics/python-write-text-file/

# Data to be put in text file
data = ['Scout 1', 'Soldier 2', 'Pyro 3', 'Demoman 4', 'Heavy 5']
print(data)

# Get filename, can't be blank or use invalid characters
# Assume the entered filename is valid for now
filename = input("Enter a filename: ")

# Add .txt extension
filename = filename + ".txt"
print(filename)

# Create new file to store data
f = open(filename, "w+")

# Add data to file
for item in data:
    f.write(item + "\n")

# Stop writing
f.close()