import re
import os
import csv


class User:
    # This class represents a user with a name, address, and phone number.
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.address}, {self.phone}"


def main():
    # Display an intro message
    intro()

    # Prompt the user for the file name and ensure it has .csv extension
    file_name = get_filename()
    
    # Loop to allow multiple data entries
    continue_entry = True
    while continue_entry:
        # Get user input
        user_information = get_input()

        # Write the data to the CSV file
        write_to_csv(file_name, user_information)
        
        # Ask if the user wants to enter another record
        continue_entry = ask_continue()
    
    # After all entries are complete, read and display the file contents
    print("\nFile contents:")
    rows = read_csv_file(file_name)
    if rows:
        display_csv_data(rows)


def ask_continue():
    """Asks the user if they want to enter another record.
    
    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    while True:
        response = input("\nWould you like to enter another record? (y/n): ").lower()
        if response == 'y' or response == 'yes':
            return True
        elif response == 'n' or response == 'no':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def intro():
    # Display an introductory message
    print("This program collects user information and stores it in a CSV file.")
    print("It also reads the contents of the file and displays them.")
    print("Please follow the prompts to enter your information.")
    print()


def get_filename():
    """Gets a filename from the user and ensures it has a .csv extension.
    
    Returns:
        A string containing a filename with .csv extension.
    """
    file_name = ""

    while not file_name:
        file_name = input("Enter the file name: ")
        if not file_name:
            print("File name cannot be empty. Please try again.")
    
    # Add .csv extension if not already present
    if not file_name.lower().endswith('.csv'):
        file_name += '.csv'
        
    return file_name


def get_input():
    # Prompts the user for their information and ensures they enter values
    name = ""
    
    # Validate name
    while not name:
        name = input("Enter name: ")
        if not name:
            print("Name cannot be empty. Please try again.")

    # Validate address using a dedicated validation function
    address = get_address()

    # Validate phone number using a dedicated validation function
    phone = get_phone_number()

    user = User(name, address, phone)
    
    return user


def get_address():
    """Prompts the user for an address and validates its format.
    
    Returns:
        A string containing a valid address.
    """
    valid_address = False
    address = ""
    
    while not valid_address:
        address = input("Enter street address: ")
        
        if not address:
            print("Address cannot be empty. Please try again.")
            continue
        
        if is_valid_address_format(address):
            valid_address = True
        else:
            print("Invalid address format. Address should include a number and street name.")
            print("Example: 123 Main St, Springfield, IL 62701")
            
    return address


def is_valid_address_format(address):
    """Validates if the provided address matches basic address conventions. 
    Without a proper address validation library, this is a simple check.
    The address should contain at least one number followed by text.  

    Args:
        address (str): The address string to validate.
        
    Returns:
        bool: True if the address follows basic conventions, False otherwise.
    """
    # Check minimum length
    if len(address) < 5:
        return False
    
    # Basic pattern: should contain at least one number followed by text
    # This checks for a street number and name pattern
    pattern = re.compile(r'\d+\s+\w+')
    if not pattern.search(address):
        return False
    
    # Should contain some letters (for street name)
    if not re.search(r'[a-zA-Z]', address):
        return False
        
    return True


def get_phone_number():
    """Prompts the user for a phone number and validates its format.

    Returns:
        A string containing a valid phone number in XXX-XXX-XXXX format.
    """
    valid_phone = False
    phone = ""

    while not valid_phone:
        phone = input("Enter phone number (format: XXX-XXX-XXXX): ")

        if not phone:
            print("Phone number cannot be empty. Please try again.")
            continue

        if is_valid_phone_format(phone):
            valid_phone = True
        else:
            print("Invalid phone number format. Please use format XXX-XXX-XXXX.")

    return phone


def is_valid_phone_format(phone):
    """Validates if the provided phone number matches the required format.
    
    Args:
        phone (str): The phone number string to validate.
        
    Returns:
        bool: True if the phone number is in valid format, False otherwise.
    """
    # Regular expression pattern for XXX-XXX-XXXX format
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(phone))


def write_to_csv(file_name, user_data):
    """Writes user data to a CSV file with headers if the file doesn't exist."""
    try:
        # Check if file exists to determine if headers need to be written
        file_exists = os.path.isfile(file_name)
        
        # Open the file in append mode to add data without overwriting
        with open(file_name, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            
            # Write headers if file is new
            if not file_exists:
                csv_writer.writerow(['Name', 'Address', 'Phone Number'])
            
            # Write the user data
            csv_writer.writerow([user_data.name, user_data.address, user_data.phone])
            
        print(f"Data successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_csv_file(file_name):
    """Reads data from a CSV file.
    
    Args:
        file_name (str): The name of the CSV file to read.
        
    Returns:
        list: A list of rows from the CSV file or None if an error occurred.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_name):
            print(f"Error: File '{file_name}' not found.")
            return None
            
        # Open the file in read mode
        with open(file_name, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            
            # Read all rows from the file
            rows = list(csv_reader)
            
            if not rows:
                print("The file is empty.")
                return None
                
            return rows
                
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def display_csv_data(rows):
    """Displays CSV data in a formatted table.
    
    Args:
        rows (list): A list of rows from a CSV file, where the first row contains headers.
    """
    try:
        # Get headers and data rows
        headers = rows[0]
        data_rows = rows[1:]
        
        if not data_rows:
            print("No data records found in the file.")
            return
            
        # Get field widths for formatting (minimum width is the header length)
        # Add padding of 4 spaces between columns
        col_widths = [max(len(headers[i]), max(len(row[i]) for row in data_rows)) + 4 
                      for i in range(len(headers))]
        
        # Print the header row
        header_format = ''.join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers))
        print(header_format)
        
        # Print a separator line
        separator = '-' * sum(col_widths)
        print(separator)
        
        # Print data rows
        for row in data_rows:
            row_format = ''.join(f"{field:<{col_widths[i]}}" for i, field in enumerate(row))
            print(row_format)
                
    except Exception as e:
        print(f"Error displaying data: {e}")


# Call the main function.
if __name__ == "__main__":
    main()
