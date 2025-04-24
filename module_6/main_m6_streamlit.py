import pandas as pd
import streamlit as st
import random
import matplotlib.pyplot as plt

# To run this code, run the command: streamlit run {path to file}
# The enviroment file should include all dependencies needed.

def main():
    # Set Page Title and Instructions
    st.title("Number Statistics Calculator")
    st.write("This program collects a series of 20 numbers and calculates statistics.")
    st.write("You can choose to either enter the numbers manually or have them randomly generated.")

    data_entered = get_numbers()

    # Only calculate statistics if we have data
    if data_entered:
        statistics = calculate_statistics(data_entered)
        display_statistics(statistics)
    else:
        st.warning("Please enter numbers or generate random numbers to see statistics.")
    

def get_numbers():
    # Create Input Options
    input_option = st.radio("Select Input Method:",
                            ("Enter Numbers Manually", "Generate Random Numbers"))

    numbers = []

    if input_option == "Enter Numbers Manually":
        st.write("Please enter 20 numbers:")
        
        # Restructure inputs to create horizontal tab flow
        # We'll create 5 rows with 4 inputs each
        for row in range(5):
            # Create a row with 4 columns
            cols = st.columns(4)
            
            # Add inputs across the row (this creates horizontal tab order)
            for col in range(4):
                i = row * 4 + col  # Calculate the overall index
                with cols[col]:
                    number_str = st.text_input(
                        f"Number {i + 1}",
                        key=f"num_{i}",
                        placeholder=f"Enter #{i + 1}",
                        value=""
                    )
                    
                    # Convert to float if a value was entered, otherwise use 0
                    if number_str:
                        try:
                            number = float(number_str)
                        except ValueError:
                            st.error(f"Invalid number format for Number {i + 1}")
                            number = 0
                    else:
                        number = 0
                        
                    numbers.append(number)
                    
        # If numbers were entered manually and not all are zero, show visualization
        if numbers and any(num != 0 for num in numbers):
            display_visualizations(numbers)
            
    else:
        if st.button("Generate Random Numbers"):
            numbers = [random.uniform(1, 100) for _ in range(20)]
            
            # Display the generated numbers in a nicer format
            st.subheader("Generated Numbers")
            
            # Use columns to display numbers in a grid
            cols = st.columns(4)
            for i, num in enumerate(numbers):
                col_index = i % 4
                with cols[col_index]:
                    st.info(f"Number {i + 1}: {num:.2f}")
            
            # Display visualizations for the generated numbers
            display_visualizations(numbers)
        else:
            st.info("Click the button above to generate random numbers")
            return []

    return numbers

def display_visualizations(numbers):
    """Displays various visualizations of the data"""
    st.subheader("Data Visualizations")
    
    # Create dataframe for visualization
    chart_data = pd.DataFrame({
        'Number Index': list(range(1, len(numbers) + 1)),
        'Value': numbers
    })
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Bar Chart", "Line Chart", "Histogram", "Box Plot"])
    
    with tab1:
        st.caption("Bar Chart - Shows the value of each individual number")
        st.bar_chart(chart_data.set_index('Number Index'))
    
    with tab2:
        st.caption("Line Chart - Shows the trend or pattern in your numbers")
        st.line_chart(chart_data.set_index('Number Index'))
    
    with tab3:
        st.caption("Histogram - Shows how your numbers are distributed")
        fig, ax = plt.subplots()
        ax.hist(numbers, bins=10, edgecolor='black')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Numbers')
        st.pyplot(fig)
    
    with tab4:
        st.caption("Box Plot - Shows statistical summary (min, max, median, quartiles)")
        fig, ax = plt.subplots()
        ax.boxplot(numbers)
        ax.set_title('Box Plot of Numbers')
        ax.set_xticklabels(['Dataset'])
        st.pyplot(fig)

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
    st.header("Statistics Results")
    
    # Create metrics in a row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Lowest", value=f"{statistics['lowest']:,.2f}")
    
    with col2:
        st.metric(label="Highest", value=f"{statistics['highest']:,.2f}")
    
    with col3:
        st.metric(label="Total", value=f"{statistics['total']:,.2f}")
    
    with col4:
        st.metric(label="Average", value=f"{statistics['average']:,.2f}")
    
    # Add a divider
    st.divider()
    
    # Display the statistics in a table format
    st.subheader("Detailed Statistics")
    
    # Create a dataframe to display the statistics
    stats_df = pd.DataFrame({
        'Statistic': ['Lowest Number', 'Highest Number', 'Total', 'Average'],
        'Value': [
            f"{statistics['lowest']:,.2f}",
            f"{statistics['highest']:,.2f}",
            f"{statistics['total']:,.2f}",
            f"{statistics['average']:,.2f}"
        ]
    })
    
    # Display the dataframe without index
    st.dataframe(stats_df.set_index('Statistic'), use_container_width=True)
    

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


if __name__ == "__main__":
    main()