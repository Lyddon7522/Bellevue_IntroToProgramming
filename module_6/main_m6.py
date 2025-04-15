import random

# Asks the user to enter a series of 20 numbers. Then, the program should store the numbers in a list and display the following data:
# The lowest number in the list.
# The highest number in the list.
# The total of the numbers in the list.
# The average of the numbers in the list.

def main():
    display_instructions()

    data_entered = get_numbers()

    statistics = calculate_statistics(data_entered)
    display_statistics(statistics)


def calculate_statistics(numbers):
    """Calculates statistics for a list of numbers and returns them as a dictionary."""
    statistics = {
        'lowest': find_lowest(numbers),
        'highest': find_highest(numbers),
        'total': calculate_total(numbers),
        'average': calculate_average(numbers)
    }
    
    return statistics


def display_statistics(statistics):
    """Displays the calculated statistics to the user."""
    print(f"\nLowest number: {statistics['lowest']:,.2f}")
    print(f"Highest number: {statistics['highest']:,.2f}")
    print(f"Total of numbers: {statistics['total']:,.2f}")
    print(f"Average of numbers: {statistics['average']:,.2f}")


def find_lowest(numbers):
    """Finds the lowest number in a list."""
    return min(numbers)


def find_highest(numbers):
    """Finds the highest number in a list."""
    return max(numbers)


def calculate_total(numbers):
    """Calculates the total of the numbers in a list."""
    return sum(numbers)


def calculate_average(numbers):
    """Calculates the average of the numbers in a list."""
    return sum(numbers) / len(numbers) if numbers else 0

def get_numbers():
    """Prompts the user to enter a series of numbers and calculates statistics."""
    numbers = []
    
    print("\nOptions:")
    print("1. Enter 20 numbers manually")
    print("2. Generate 20 random numbers")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ")
        if choice == "1":
            # Manual entry
            # Prompt the user to enter 20 numbers
            for i in range(20):
                while True:
                    try:
                        number = float(input(f"Enter number entry {i + 1}: "))
                        numbers.append(number)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            break
        elif choice == "2":
            # Generate random numbers
            print("\nGenerating 20 random numbers between 1 and 100...")
            numbers = [random.uniform(1, 100) for _ in range(20)]
            
            # Display the generated numbers for the user to see
            print("\nGenerated numbers:")
            for i, num in enumerate(numbers, 1):
                print(f"Number {i}: {num:.2f}")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    return numbers


def display_instructions():
    """Displays instructions to the user."""
    print("This program collects a series of 20 numbers and calculates statistics.")
    print("You can choose to either enter the numbers manually or have them randomly generated.")
    print("After entering or generating the numbers, the program will display the lowest, highest, total, and average of the numbers.")
    print()

if __name__ == '__main__':
    main()