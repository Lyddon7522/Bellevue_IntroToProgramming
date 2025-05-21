import requests
import json
import re

API_KEY = "906b6939735602a519447e37a839d229"
BASE_URL = "https://api.openweathermap.org/data/2.5"

def validate_zip_code(zip_code):
    """
    Validates if the input is a valid 5-digit US zip code

    Args:
        zip_code (str): The zip code to validate

    Returns:
        bool: True if valid, False otherwise
    """
    # Handle None values
    if zip_code is None:
        return False

    # Pattern for 5-digit zip code only
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, zip_code))

def get_weather_data(zip_code):
    """
    Fetches weather data from OpenWeatherMap API

    Args:
        zip_code (str): The zip code to get weather for

    Returns:
        dict: Raw weather data response
    """
    print(f"Fetching weather data for zip code {zip_code}...")

    current_weather_url = BASE_URL + "/weather"
    params = {
        "zip": f"{zip_code},us",
        "appid": API_KEY,
        "units": "imperial"  # For Fahrenheit
    }

    try:
        response = requests.get(current_weather_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    """Main function to run the simplified weather application"""
    print("Welcome to the Weather Forecast Application!")

    while True:
        print("\nEnter a 5-digit US zip code to get the current weather data")
        print("Or type 'quit' to exit the program")

        user_input = input("Zip code: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the Weather Forecast Application. Goodbye!")
            break

        if not validate_zip_code(user_input):
            print(f"Invalid zip code! Please enter a valid US zip code (5-digit).")
            continue

        # Get and display the raw JSON response
        weather_data = get_weather_data(user_input)
        if weather_data:
            print("\n--- Raw JSON Response ---")
            print(json.dumps(weather_data, indent=2))
            print("-------------------------")

if __name__ == "__main__":
    main()
