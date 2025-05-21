import re
import requests
import json
import time
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored terminal output
init()

API_KEY = "906b6939735602a519447e37a839d229"
BASE_URL = "https://api.openweathermap.org/data/2.5"

# Weather condition ASCII art
WEATHER_ART = {
    "clear": [
        f"{Fore.YELLOW}    \\   /    {Style.RESET_ALL}",
        f"{Fore.YELLOW}     .-.     {Style.RESET_ALL}",
        f"{Fore.YELLOW}  ― (   ) ―  {Style.RESET_ALL}",
        f"{Fore.YELLOW}     `-'     {Style.RESET_ALL}",
        f"{Fore.YELLOW}    /   \\    {Style.RESET_ALL}"
    ],
    "clouds": [
        f"{Fore.WHITE}             {Style.RESET_ALL}",
        f"{Fore.WHITE}     .--.    {Style.RESET_ALL}",
        f"{Fore.WHITE}  .-(    ).  {Style.RESET_ALL}",
        f"{Fore.WHITE} (___.__)__) {Style.RESET_ALL}",
        f"{Fore.WHITE}             {Style.RESET_ALL}"
    ],
    "rain": [
        f"{Fore.CYAN}     .-.     {Style.RESET_ALL}",
        f"{Fore.CYAN}    (   ).   {Style.RESET_ALL}",
        f"{Fore.CYAN}   (___(__)  {Style.RESET_ALL}",
        f"{Fore.BLUE}  ' ' ' ' '  {Style.RESET_ALL}",
        f"{Fore.BLUE} ' ' ' ' '   {Style.RESET_ALL}"
    ],
    "drizzle": [
        f"{Fore.CYAN}     .-.     {Style.RESET_ALL}",
        f"{Fore.CYAN}    (   ).   {Style.RESET_ALL}",
        f"{Fore.CYAN}   (___(__)  {Style.RESET_ALL}",
        f"{Fore.BLUE}   ' ' ' '   {Style.RESET_ALL}",
        f"{Fore.BLUE}  ' ' ' '    {Style.RESET_ALL}"
    ],
    "thunderstorm": [
        f"{Fore.CYAN}     .-.     {Style.RESET_ALL}",
        f"{Fore.CYAN}    (   ).   {Style.RESET_ALL}",
        f"{Fore.CYAN}   (___(__)  {Style.RESET_ALL}",
        f"{Fore.YELLOW}    ⚡⚡⚡    {Style.RESET_ALL}",
        f"{Fore.BLUE}    ' ' '    {Style.RESET_ALL}"
    ],
    "snow": [
        f"{Fore.WHITE}     .-.     {Style.RESET_ALL}",
        f"{Fore.WHITE}    (   ).   {Style.RESET_ALL}",
        f"{Fore.WHITE}   (___(__)  {Style.RESET_ALL}",
        f"{Fore.WHITE}   * * * *   {Style.RESET_ALL}",
        f"{Fore.WHITE}  * * * *    {Style.RESET_ALL}"
    ],
    "mist": [
        f"{Fore.WHITE}             {Style.RESET_ALL}",
        f"{Fore.WHITE} _ - _ - _ - {Style.RESET_ALL}",
        f"{Fore.WHITE}  _ - _ - _  {Style.RESET_ALL}",
        f"{Fore.WHITE} _ - _ - _ - {Style.RESET_ALL}",
        f"{Fore.WHITE}             {Style.RESET_ALL}"
    ],
    "default": [
        f"{Fore.WHITE}    ?????    {Style.RESET_ALL}",
        f"{Fore.WHITE}   ???????   {Style.RESET_ALL}",
        f"{Fore.WHITE}  ?????????  {Style.RESET_ALL}",
        f"{Fore.WHITE}   ???????   {Style.RESET_ALL}",
        f"{Fore.WHITE}    ?????    {Style.RESET_ALL}"
    ]
}

def validate_zip_code(zip_code):
    """
    Validates if the input is a valid 5-digit US zip code

    Args:
        zip_code (str): The zip code to validate

    Returns:
        bool: True if valid, False otherwise
    """
    # Pattern for 5-digit zip code only
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, zip_code))

def get_compass_direction(degrees):
    """
    Convert wind direction in degrees to a compass direction

    Args:
        degrees: Wind direction in degrees

    Returns:
        str: Compass direction (N, NE, E, SE, S, SW, W, NW)
    """
    if degrees == "Unknown":
        return ""

    # Convert degrees to a value between 0 and 360
    degrees = float(degrees) % 360

    # Define compass directions based on degree ranges
    if 337.5 <= degrees or degrees < 22.5:
        return "(N)"
    elif 22.5 <= degrees < 67.5:
        return "(NE)"
    elif 67.5 <= degrees < 112.5:
        return "(E)"
    elif 112.5 <= degrees < 157.5:
        return "(SE)"
    elif 157.5 <= degrees < 202.5:
        return "(S)"
    elif 202.5 <= degrees < 247.5:
        return "(SW)"
    elif 247.5 <= degrees < 292.5:
        return "(W)"
    elif 292.5 <= degrees < 337.5:
        return "(NW)"

    return ""

def get_current_weather_data(zip_code):
    """
    Fetches current weather data from OpenWeatherMap API

    Args:
        zip_code (str): The zip code to get weather for

    Returns:
        dict: Weather data if successful, None otherwise
    """
    # Loading effect
    print(f"\n{Fore.CYAN}Fetching weather data for zip code {zip_code}...{Style.RESET_ALL}")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print("\n")

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
        print(f"{Fore.RED}Error fetching weather data: {e}{Style.RESET_ALL}")
        return None

def display_weather(weather_data):
    """
    Display weather information

    Args:
        weather_data (dict): Weather data from API
    """
    if not weather_data:
        print(f"{Fore.RED}Weather data is not available.{Style.RESET_ALL}")
        return

    # Extract data from weather_data
    city = weather_data.get("name", "Unknown")
    weather_desc = weather_data.get("weather", [{}])[0].get("description", "Unknown")
    weather_main = weather_data.get("weather", [{}])[0].get("main", "").lower()
    temp = weather_data.get("main", {}).get("temp", "Unknown")
    feels_like = weather_data.get("main", {}).get("feels_like", "Unknown")
    humidity = weather_data.get("main", {}).get("humidity", "Unknown")
    wind_speed = weather_data.get("wind", {}).get("speed", "Unknown")
    wind_direction = weather_data.get("wind", {}).get("deg", "Unknown")
    compass_direction = get_compass_direction(wind_direction)

    # Get appropriate ASCII art for the weather condition
    art_key = "default"
    for key in WEATHER_ART.keys():
        if key in weather_main:
            art_key = key
            break

    # Display header
    print(f"\n{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🌤️  CURRENT WEATHER FOR {city.upper()} 🌤️{Style.RESET_ALL}".center(60))
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")

    # Display weather art and conditions side by side
    art = WEATHER_ART[art_key]
    print(f"{art[0]}    {Fore.GREEN}Conditions:{Fore.YELLOW} {weather_desc.title()}{Style.RESET_ALL}")

    # Color temperature based on how hot/cold it is
    temp_color = Fore.BLUE
    if isinstance(temp, (int, float)):
        if temp > 80:
            temp_color = Fore.RED
        elif temp > 65:
            temp_color = Fore.YELLOW

    print(f"{art[1]}    {Fore.GREEN}Temperature:{temp_color} {temp}°F{Style.RESET_ALL}")
    print(f"{art[2]}    {Fore.GREEN}Feels like:{Fore.WHITE} {feels_like}°F{Style.RESET_ALL}")
    print(f"{art[3]}    {Fore.GREEN}Humidity:{Fore.CYAN} {humidity}%{Style.RESET_ALL}")
    print(f"{art[4]}    {Fore.GREEN}Wind:{Fore.WHITE} {wind_speed} mph {compass_direction}{Style.RESET_ALL}")

    # Display a fun weather tip
    tips = {
        "clear": "Perfect day for outdoor activities! Don't forget sunscreen!",
        "clouds": "Partly cloudy - nature's way of providing shade!",
        "rain": "Remember your umbrella! Splash in puddles at your own risk!",
        "drizzle": "Light rain - perfect for plants and poets!",
        "thunderstorm": "Thunder means stay indoors. Lightning is nature's light show!",
        "snow": "Bundle up! Great day for hot chocolate and snowmen!",
        "mist": "Drive carefully - it's a bit foggy out there!"
    }

    print(f"\n{Fore.MAGENTA}💡 TIP: {tips.get(art_key, 'Enjoy your day, whatever the weather!')}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")

def main():
    """Main function to run the weather application"""
    print(f"{Fore.CYAN}Welcome to the Weather Forecast Application!{Style.RESET_ALL}")

    while True:
        print(f"\n{Fore.GREEN}Enter a 5-digit US zip code to get the current weather")
        print(f"Or type '{Fore.RED}quit{Fore.GREEN}' to exit the program{Style.RESET_ALL}")

        user_input = input(f"{Fore.YELLOW}Zip code: {Style.RESET_ALL}").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print(f"\n{Fore.CYAN}Thank you for using the Weather Forecast Application!")
            print(f"{Fore.MAGENTA}Have a wonderful day! Goodbye!{Style.RESET_ALL}")
            break

        if not validate_zip_code(user_input):
            print(f"{Fore.RED}Invalid zip code! Please enter a valid US zip code (5-digit).{Style.RESET_ALL}")
            continue

        weather_data = get_current_weather_data(user_input)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
