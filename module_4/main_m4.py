# Example Program that converts Miles to Kilometers

# Constants
KILOMETERS_TO_MILES_RATIO = 1.609344

def main():
    intro()

    # Get valid miles input
    miles = get_miles()

    # Convert the miles to kilometers and display result
    kilometers = miles_to_kilometers(miles)
    display_result(miles, kilometers)

# The get_miles function prompts the user for miles traveled and validates the input.
def get_miles():
    while True:
        try:
            miles =  float(input("Enter miles traveled: "))
            if miles <= 0:
                print("Miles traveled must be a positive number.")
                print()
                continue
            return miles
        except ValueError:
            print("Invalid entry. Please enter a number.")
            print()

# The display_result function takes the miles and kilometers and displays the result.
def display_result(miles, kilometers):
    print()
    print(f"{miles:,.2f} miles converts to {kilometers:,.2f} kilometers.")
    print()

    display_odometer(kilometers)

# The intro function displays an introductory screen.
def intro():
    print('This program converts miles to kilometers')
    print('Results are rounded to the nearest hundredth')
    print()
    print('For your reference the formula is:')
    print('1 mile = 1.609344 kilometers')
    print()

# This function takes a number of miles and returns a conversion to kilometers.
def miles_to_kilometers(miles):
    return miles * KILOMETERS_TO_MILES_RATIO


# The display_odometer function creates an ASCII art display for the kilometers.
def display_odometer(kilometers):
    # Format the kilometers with commas and 2 decimal places
    # Example: 1234.56 becomes "1,234.56"
    km_str = f"{kilometers:,.2f}"

    # Calculate the width of the box
    # Add 4 to accommodate 2 spaces on each side of the number
    # Ensure minimum width of 14 characters to fit "ODOMETER" header
    width = max(len(km_str) + 4, 14)

    # Create the horizontal border line using ═ repeated to match width
    border = "═" * width
    # Create spaces for padding the text lines
    spaces = " " * (width - 2)

    # Draw the Odometer art
    print(f"    ╔{border}╗")
    print(f"    ║   ODOMETER{spaces[11:]}  ║")
    print(f"    ╠{border}╣")
    print(f"    ║{km_str:>{width - 2}}  ║")
    print(f"    ║      KM{spaces[8:]}  ║")
    print(f"    ╚{border}╝")
    print()

# Call the main function.
if __name__ == "__main__":
    main()