# Get input from users, and then only display the 3 most recent entries.

# Set up empty list
all_calculations = []

# Get data
get_item = ""
while get_item != "exit":
    get_item = input("Enter an item: ")

    if get_item == "exit":
        break

    all_calculations.append(get_item)

# If list is empty, print "This list is empty."
if len(all_calculations) == 0:
    print("\nThis list is empty.")

else:
    if len(all_calculations) < 3:
        print("\nThese are the most recently entered items:")
        for item in range(len(all_calculations)):
            print("- " + all_calculations[len(all_calculations) - item - 1])

    else:
        print("\nThese are the 3 most recently entered items:")
        for item in range(0, 3):
            print("- " + all_calculations[len(all_calculations) - item - 1])
