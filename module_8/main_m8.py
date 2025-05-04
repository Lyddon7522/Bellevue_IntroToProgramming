def get_stock_price(ticker_symbol, stocks):
    """
    Look up a stock price by ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol to look up
        stocks (dict): Dictionary of stock ticker symbols and their data
        
    Returns:
        dict or None: The stock data if found, None otherwise
    """
    # Convert ticker to uppercase for case-insensitive comparison
    ticker_symbol = ticker_symbol.upper()
    
    # Look up the ticker symbol in the dictionary
    return stocks.get(ticker_symbol)

def display_stock_info(ticker_symbol, stock_data):
    """
    Display information about a stock.
    
    Args:
        ticker_symbol (str): The stock ticker symbol
        stock_data (dict): Dictionary containing stock price and company name
    """
    # Extract data
    price = stock_data['price']
    company_name = stock_data['name']
    last_updated = stock_data['last_updated']
    
    # Create visual indicators for price. In prod this would be based on if the price is up or down
    price_indicator = "↑" if price > 200 else "↓"
    
    # Box dimensions
    width = 40
    
    # Format the display with box border
    border = "+" + "-" * width + "+"
    
    print("\n" + border)
    print(f"|{' STOCK INFORMATION ':^{width}}|")
    print(border)
    print(f"| Ticker Symbol: {ticker_symbol}{' ' * (width - 16 - len(ticker_symbol))}|")
    
    # Handle company name by truncating if too long fo our display box
    if len(company_name) > width - 11:
        company_display = company_name[:width - 14] + "..."
    else:
        company_display = company_name
    print(f"| Company: {company_display}{' ' * (width - 10 - len(company_display))}|")
    
    # Format price with indicator
    price_str = f"${price:.2f} {price_indicator}"
    print(f"| Current Price: {price_str}{' ' * (width - 16 - len(price_str))}|")
    
    # Empty line
    print(f"|{' ' * width}|")
    
    # Last updated line
    print(f"|{f' Last Updated: {last_updated} ':^{width}}|")
    print(border)

def get_stock_data():
    """
    Create a dictionary of stock data.
    
    Returns:
        dict: A dictionary with stock ticker symbols as keys and 
             dictionaries with company information as values
    """
    
    return {
        "AAPL": {
            "name": "Apple Inc.",
            "price": 198.45,
            "last_updated": "2025-05-04"
        },
        "MSFT": {
            "name": "Microsoft Corporation",
            "price": 425.22,
            "last_updated": "2025-05-04"
        },
        "AMZN": {
            "name": "Amazon.com Inc.",
            "price": 182.15,
            "last_updated": "2025-05-04"
        },
        "GOOGL": {
            "name": "Alphabet Inc. (Google)",
            "price": 172.37,
            "last_updated": "2025-05-04"
        },
        "META": {
            "name": "Meta Platforms Inc.",
            "price": 475.89,
            "last_updated": "2025-05-04"
        },
        "TSLA": {
            "name": "Tesla Inc.",
            "price": 177.53,
            "last_updated": "2025-05-04"
        },
        "NVDA": {
            "name": "NVIDIA Corporation",
            "price": 887.20,
            "last_updated": "2025-05-04"
        },
        "JPM": {
            "name": "JPMorgan Chase & Co.",
            "price": 198.75,
            "last_updated": "2025-05-04"
        },
        "V": {
            "name": "Visa Inc.",
            "price": 275.94,
            "last_updated": "2025-05-04"
        },
        "WMT": {
            "name": "Walmart Inc.",
            "price": 62.44,
            "last_updated": "2025-05-04"
        },
        "JNJ": {
            "name": "Johnson & Johnson",
            "price": 147.89,
            "last_updated": "2025-05-04" 
        },
        "PG": {
            "name": "Procter & Gamble Co.",
            "price": 165.32,
            "last_updated": "2025-05-04"
        }
    }

def main():
    # Create a dictionary of stock data
    stocks = get_stock_data()
    
    print("Stock Ticker Lookup")
    print("===================")
    
    while True:
        # Get ticker symbol input from user
        ticker_symbol = input("Enter a stock ticker symbol (or 'quit' to exit): ")
        
        # Check if user wants to exit
        if ticker_symbol.lower() == 'quit':
            print("Thank you for using the Stock Ticker Lookup!")
            break
        
        # Look up the stock data
        stock_data = get_stock_price(ticker_symbol, stocks)
        
        # Display the result
        if stock_data is not None:
            display_stock_info(ticker_symbol.upper(), stock_data)
            
            # Ask if user wants to look up another ticker
            continue_choice = input("\nLook up another ticker? (y/n): ")
            if continue_choice.lower() != 'y':
                print("Thank you for using the Stock Ticker Lookup!")
                break
                
        else:
            print(f"\nTicker symbol '{ticker_symbol.upper()}' not found.")
            print("Available tickers:", ", ".join(sorted(stocks.keys())))
            # The loop will continue automatically, prompting for a new ticker

if __name__ == "__main__":
    main()