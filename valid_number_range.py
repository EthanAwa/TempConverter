def int_check(num):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            if response < num:
                print("Too cold")
            else:
                return response

        except ValueError:
            print("Please enter a number")


number = int_check(-273)
print("You chose {}".format(number))

number = int_check(-459)
print("You chose {}".format(number))