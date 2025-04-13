import streamlit as st
import re
import os
import csv
import pandas as pd


class User:
    # This class represents a user with a name, address, and phone number.
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.address}, {self.phone}"


def is_valid_address_format(address):
    """Validates if the provided address matches basic address conventions.
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
            
        return True
    except Exception as e:
        st.error(f"Error writing to file: {e}")
        return False


def read_csv_file(file_name):
    """Reads data from a CSV file.
    
    Args:
        file_name (str): The name of the CSV file to read.
        
    Returns:
        DataFrame: A pandas DataFrame with the CSV data or None if an error occurred.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_name):
            st.warning(f"File '{file_name}' not found.")
            return None
            
        # Read the CSV into a pandas DataFrame
        df = pd.read_csv(file_name)
        return df
                
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None


def main():
    st.title("User Information Manager")
    
    # Display an intro message
    st.write("This application collects user information and stores it in a CSV file.")
    st.write("You can also view the contents of existing CSV files.")
    
    # File name input with .csv extension check
    file_name = st.text_input("Enter a file name:")
    if file_name and not file_name.lower().endswith('.csv'):
        file_name += '.csv'

    # Create tabs for adding users and viewing data
    add_tab, view_tab = st.tabs(["Add User", "View Data"])
    
    with add_tab:
        st.subheader("Add User Information")
        
        # Create a form for user input
        with st.form("user_form"):
            # Name input
            name = st.text_input("Name:")
            
            # Address input with validation
            address = st.text_input("Street Address:")
            if address and not is_valid_address_format(address):
                st.warning("Invalid address format. Address should include a number and street name.")
                st.markdown("Example: 123 Main St, Springfield, IL 62701")
            
            # Phone input with validation
            phone = st.text_input("Phone Number (format: XXX-XXX-XXXX):")
            if phone and not is_valid_phone_format(phone):
                st.warning("Invalid phone number format. Please use format XXX-XXX-XXXX.")
            
            # Submit button
            submit_button = st.form_submit_button("Save User Information")
            
            if submit_button:
                # Validate all inputs
                if not name:
                    st.error("Name cannot be empty.")
                elif not address:
                    st.error("Address cannot be empty.")
                elif not is_valid_address_format(address):
                    st.error("Address format is invalid.")
                elif not phone:
                    st.error("Phone number cannot be empty.")
                elif not is_valid_phone_format(phone):
                    st.error("Phone number format is invalid.")
                elif not file_name:
                    st.error("File name cannot be empty.")
                else:
                    # Create User object and save to CSV
                    user = User(name, address, phone)
                    if write_to_csv(file_name, user):
                        st.success(f"Data successfully written to {file_name}")
                        
                        # Clear the form by rerunning the app
                        st.rerun()
    
    with view_tab:
        st.subheader("View CSV Data")
        
        # Button to display data from the current file
        if file_name:
            if st.button(f"View data from {file_name}"):
                df = read_csv_file(file_name)
                if df is not None and not df.empty:
                    st.dataframe(df, use_container_width=True)
                elif df is not None and df.empty:
                    st.info("The file exists but contains no data.")
        else:
            st.info("Enter a file name to view its contents.")
        
        # Option to browse for any CSV file
        st.write("--- OR ---")
        uploaded_file = st.file_uploader("Choose a CSV file to view", type="csv")
        if uploaded_file is not None:
            # Read the uploaded file
            try:
                df = pd.read_csv(uploaded_file)
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error(f"Error reading uploaded file: {e}")


if __name__ == "__main__":
    main()