# Stock Portfolio Tracker - CodeAlpha

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 170,
    "NFLX": 500
}


def display_stocks():
    print("\nAvailable Stocks")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

    print("-" * 30)


def add_stock(portfolio):
    stock = input("Enter Stock Symbol: ").upper()

    if stock not in stock_prices:
        print("Invalid Stock Symbol!")
        return

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"{quantity} shares of {stock} added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_portfolio(portfolio):
    if not portfolio:
        print("\nPortfolio is empty.")
        return

    print("\nPortfolio Summary")
    print("-" * 50)

    total_value = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value

        print(
            f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${value}"
        )

    print("-" * 50)
    print(f"Total Portfolio Value: ${total_value}")


def save_portfolio(portfolio):
    if not portfolio:
        print("Nothing to save.")
        return

    total_value = 0

    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            total_value += value

            file.write(
                f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${value}\n"
            )

        file.write("\n")
        file.write(f"Total Portfolio Value: ${total_value}")

    print("Portfolio saved successfully as portfolio.txt")


def main():
    portfolio = {}

    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Save Portfolio")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3":
            view_portfolio(portfolio)

        elif choice == "4":
            save_portfolio(portfolio)

        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid Choice. Try Again.")


main()