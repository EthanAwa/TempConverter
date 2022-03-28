# Get input from users, and then only display the 3 most recent entries.

# Set up empty list
all_calculations = []

# Get data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# Print the 3 most recent entries
print("\nThe 3 most recent entries are:")
for item in range(0, 3):
    print("- " + all_calculations[len(all_calculations) - item - 1])