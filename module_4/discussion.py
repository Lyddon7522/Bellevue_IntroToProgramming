#Example Program that converts cups to fluid ounces

# Constants
CUPS_TO_OUNCES_RATIO = 8
GALLONS_TO_LITERS_RATIO = 3.785411784

def main():
    # display the intro screen.
    intro()

    try:
        # Ask user to select the conversion type.
        print("Select the conversion type:")
        print("1. Cups to Fluid Ounces")
        print("2. Gallons to Liters")
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            # Get the number of cups.
            cups_needed = int(input('Enter the number of cups: '))

            # Convert the cups to ounces and display result
            ounces = cups_to_ounces(cups_needed)
            display_result(ounces, "ounces")
        elif choice == 2:
            # Get the number of gallons.
            gallons_needed = int(input('Enter the number of gallons: '))

            # Convert the gallons to liters and display result
            liters = gallons_to_liters(gallons_needed)
            display_result(liters, "liters")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            print()
            main()

    except:
        print("An exception occurred, try again by entering only a number")
        print()
        main()

def display_result(value, unit):
    print(f"That converts to {value} {unit}.")

# The intro function displays an introductory screen.
def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces and gallons to liters. ')
    print('For your reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print(' 1 gallon = 3.785411784 liters')
    print()

def gallons_to_liters(gallons):
    return gallons * GALLONS_TO_LITERS_RATIO

# The cups_to_ounces function accepts a number of
# cups and returns the equivalent number of ounces.
def cups_to_ounces(cups):
    return cups * CUPS_TO_OUNCES_RATIO


# Call the main function.
if __name__ == "__main__":
    main()