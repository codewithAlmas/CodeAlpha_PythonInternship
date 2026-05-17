# Dictionary containing stock names and their prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 200,
    "AMZN": 170
}

# Variable to store the total investment value
total = 0

# Display available stocks and their prices
print("Available Stocks:")

for stock in stocks:
    print(stock, ":", stocks[stock])

# Loop to continuously take user input
while True:

    # Take stock name input from the user
    # Convert input to uppercase for matching
    name = input("Enter stock name (or 'done'): ").upper()

    # Exit loop if user types DONE
    if name == "DONE":
        break

    # Check if the entered stock exists
    if name in stocks:

        # Take quantity input from the user
        qty = int(input("Enter quantity: "))

        # Calculate investment value for selected stock
        value = stocks[name] * qty

        # Add value to total investment
        total += value

        # Display added investment amount
        print("Added:", value)

    else:
        # Message for invalid stock name
        print("Stock not found")

# Display final investment value
print("Total Investment Value =", total)

# Save total investment value into a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

# Confirmation message after saving file
print("Saved to portfolio.txt")