def get_initials(full_name):
    """
    Extract initials from a full name.
    
    Args:
        full_name (str): A string containing first, middle, and last names
    
    Returns:
        str: The initials in the format "F. M. L."
    """

    # Split the full name into parts
    name_parts = full_name.split()
    
    # Get the first letter of each part and format as initials
    initials = ""
    for name in name_parts:
        if name:  # Check if the name part is not empty
            initials += name[0].upper() + ". "
    
    # Return the formatted initials (removing trailing space)
    return initials.strip()

def validate_name(name):
    """
    Validate the input name based on the required criteria.
    
    Args:
        name (str): The input name to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Check if the name is empty or just whitespace
    if not name or name.isspace():
        print("Error: Name cannot be empty.")
        return False
    
    # Check if the name contains only digits
    if name.replace(" ", "").isdigit():
        print("Error: Name cannot contain only digits.")
        return False
    
    # Check if the name contains at least one alphanumeric character
    if not any(char.isalnum() for char in name):
        print("Error: Name must contain at least one alphanumeric character.")
        return False
    
    return True

def main():
    while True:
        # Get the full name from the user
        full_name = input("Please enter your full name (first middle last): ")
        
        # Validate the input
        if validate_name(full_name):
            # Get and display the initials
            initials = get_initials(full_name)
            print(f"Your initials are: {initials}")
            break
        else:
            print("Please try again.\n")

if __name__ == "__main__":
    main()