# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main Routine goes here

# Introduction / Heading print statements

print()
print("*** Fence Cost Calculator ***")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    length = num_check("Length: ")
    cost_per_m = num_check("Cost Per Meter: ")

    # Calculate Perimeter (length + width) x 2
    perimeter = 2 * (length + width)

    # Calculate price of fencing (perimeter x cost/m)
    cost_per_m = (perimeter * cost_per_m)

    print()

    # Output area and perimeter
    print("The Perimeter is: {:.2f} m".format(perimeter))
    print("The Cost of This Fencing is: ${:.2f}".format(cost_per_m))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit.")
    print()

print()
print("Thanks for using the Fencing Calculator.")
print()
