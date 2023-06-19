account_balance = 0
warehouse = {}


# Function to display available commands
def display_commands():
    print("valid commands:")
    print("- balance")
    print("- sale")
    print("- purchase")
    print("- account")
    print("- list")
    print("- warehouse")
    print("- review")
    print("- end")


# - 'balance': The program should prompt for an amount to add or subtract from the account.
def handle_balance():
    global account_balance
    amount = float(input("Enter the amount to add or subtract: "))
    account_balance += amount


# - 'sale': The program should prompt for the name of the product, its price, and quantity.
# Perform necessary calculations and update the account and warehouse accordingly.
def handle_sale():
    global account_balance, warehouse
    product = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    if product not in warehouse:
        # break
        warehouse[product] = {'price': price, 'quantity': quantity}
    else:
        warehouse[product]['quantity'] += quantity

    total_price = price * quantity
    account_balance += total_price


# - 'purchase': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly.
# Ensure that the account balance is not negative after a purchase operation.
def handle_purchase():
    global account_balance, warehouse
    product = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    if product not in warehouse:
        warehouse[product] = {'price': price, 'quantity': quantity}
    else:
        if account_balance < price * quantity:
            print("Insufficient funds. Purchase cannot be completed.")
            return

        warehouse[product]['quantity'] += quantity
        account_balance -= price * quantity


#  - 'account': Display the current account balance.
def handle_account():
    print("Current account balance:", account_balance)


#  - 'list': Display the total inventory in the warehouse along with product prices and quantities.
def handle_list():
    print("Warehouse inventory:")
    for product, details in warehouse.items():
        print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")


# - 'warehouse': Prompt for a product name and display its status in the warehouse.
def handle_warehouse():
    product = input("Enter the product name: ")
    if product in warehouse:
        print("Product status in warehouse:")
        print(f"Price: {warehouse[product]['price']}, Quantity: {warehouse[product]['quantity']}")
    else:
        print("Product not found in warehouse.")


#- 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. If ‘from’ and ‘to’ are empty, display all recorder operations.
# Handle cases where 'from' and 'to' values are out of range.
def handle_review():
    start = int(input("Enter the starting index (0 for the first operation): "))
    end = int(input("Enter the ending index (leave empty for the latest operation): "))

    if start < 0 or start >= len(commands) or (end is not None and (end < start or end >= len(commands))):
        print("Invalid index range.")
        return

    if end is None:
        end = len(commands)

    print("Recorded operations:")
    for i in range(start, end + 1):
        print(f"{i}. {commands[i]}")


#   - 'end': Terminate the program.
commands = []
while True:
    display_commands()
    command = input("Enter a command: ")

    if command == 'balance':
        handle_balance()
        commands.append('balance')
    elif command == 'sale':
        handle_sale()
        commands.append('sale')
    elif command == 'purchase':
        handle_purchase()
        commands.append('purchase')
    elif command == 'account':
        handle_account()
    elif command == 'list':
        handle_list()
    elif command == 'warehouse':
        handle_warehouse()
    elif command == 'review':
        handle_review()