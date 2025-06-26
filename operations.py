def display_products(products):
    # Display all products in a readable format.
    print("*" * 80)
    print("ID\tName\t\tBrand\t\tQuantity\tPrice\tOrigin")
    print("*" * 80)
    for key, value in products.items():
        line = str(key) + "\t" + \
               str(value["Name"]) + "\t\t" + \
               str(value["Brand"]) + "\t\t" + \
               str(value["Quantity"]) + "\t\t" + \
               str(value["Price"]) + "\t" + \
               str(value["Origin"])
        print(line)
    print("*" * 80)

def restock_products(products):
    # Handle restocking of products
    supplier_name = input("Enter supplier's name: ")
    phone_number = input("Enter supplier's phone number: ")

    restocked_items = {}
    total_restocked = 0
    index = 0

    while True:
        product_id_input = input("Enter the product ID to restock: ")
        try:
            product_id = int(product_id_input)
        except:
            print("Invalid product ID. Please enter a number.")
            continue

        if product_id not in products:
            print("Invalid product ID. Please try again.")
            continue

        quantity_input = input("Enter quantity to add: ")
        price_input = input("Enter unit price: ")

        try:
            quantity = int(quantity_input)
            unit_price = int(price_input)
        except:
            print("An error occurred. Please enter a valid number.")
            continue

        current_stock = products[product_id]["Quantity"]
        new_stock = current_stock + quantity
        products[product_id]["Quantity"] = new_stock

        total_price = quantity * unit_price

        restocked_items[index] = {
            "ID": product_id,
            "Name": products[product_id]["Name"],
            "Quantity": quantity,
            "Total": total_price
        }

        print("Added " + str(quantity) + " items to " + products[product_id]["Name"])
        print("New stock level: " + str(products[product_id]["Quantity"]))

        index = index + 1
        total_restocked = total_restocked + quantity

        more = input("Do you want to restock more products? (yes/no): ")
        if more == "no" or more == "No":
            break

    # Convert restocked_items dict to list manually
    restocked_items_list = []
    i = 0
    while i < index:
        restocked_items_list = restocked_items_list + [restocked_items[i]]
        i = i + 1

    return supplier_name, phone_number, restocked_items_list, total_restocked





def sell_products(products):
    #Handle selling of products.
    customer_name = input("Enter customer's name: ")
    phone_number = input("Enter customer's phone number: ")

    # Initialize the sold items list as an empty dictionary
    sold_items = {}
    total_cost = 0
    index = 0  # Manual index for adding items to sold_items

    while True:
        display_products(products)
        try:
            product_id = int(input("Enter the product ID to sell: "))
            if product_id not in products:
                print("Invalid product ID. Please try again.")
                continue
            quantity = int(input("Enter quantity to sell: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        stock_qty = int(products[product_id][2])
        free_items = quantity // 3
        total_deducted = quantity + free_items

        if total_deducted > stock_qty:
            print("Not enough stock available.")
            continue

        products[product_id][2] = str(stock_qty - total_deducted)
        selling_price = float(products[product_id][3]) * 2
        total_price = selling_price * quantity
        total_cost += total_price

        # Add item to sold_items without using append
        sold_items[index] = {
            "ID": product_id,
            "Name": products[product_id][0],
            "Quantity": quantity,
            "Free": free_items,
            "Total": total_price
        }
        index += 1  # Increment index for next item

        print("You received " + str(free_items) + " free item(s).")
        more = input("Do you want to sell more products? (yes/no): ").lower()
        if more == "no":
            break

    # Convert dictionary of sold_items back to a list for compatibility
    sold_items_list = [sold_items[key] for key in sold_items]
    return customer_name, phone_number, sold_items_list, total_cost

def sell_products(products):
    # Handle selling of products
    customer_name = input("Enter customer's name: ")
    phone_number = input("Enter customer's phone number: ")

    sold_items = {}  # Dictionary to hold sold items
    total_cost = 0
    index = 0

    while True:
        # Display products
        print("*" * 80)
        print("ID\tName\t\tBrand\t\tQuantity\tPrice\tOrigin")
        print("*" * 80)
        for key in products:
            product = products[key]
            line = str(key) + "\t" + product["Name"] + "\t\t" + product["Brand"] + "\t\t" + str(product["Quantity"]) + "\t\t" + str(product["Price"]) + "\t" + product["Origin"]
            print(line)
        print("*" * 80)

        # Input product ID
        product_id_input = input("Enter the product ID to sell: ")
        try:
            product_id = int(product_id_input)
        except:
            print("Invalid product ID. Please enter a number.")
            continue

        if product_id not in products:
            print("Invalid product ID. Please try again.")
            continue

        # Input quantity
        quantity_input = input("Enter quantity to sell: ")
        try:
            quantity = int(quantity_input)
        except:
            print("Invalid quantity. Please enter a number.")
            continue

        current_stock = products[product_id]["Quantity"]
        free_items = quantity // 3
        total_deduct = quantity + free_items

        if total_deduct > current_stock:
            print("Not enough stock available.")
            continue

        # Deduct stock
        products[product_id]["Quantity"] = current_stock - total_deduct

        base_price = products[product_id]["Price"]
        sell_price = base_price * 2
        total_price = sell_price * quantity
        total_cost = total_cost + total_price

        sold_items[index] = {
            "ID": product_id,
            "Name": products[product_id]["Name"],
            "Quantity": quantity,
            "Free": free_items,
            "Total": total_price
        }
        index = index + 1

        print("You received " + str(free_items) + " free item(s).")
        more = input("Do you want to sell more products? (yes/no): ")

        if more == "no" or more == "No":
            break

    # Convert dict to list manually
    sold_items_list = []
    i = 0
    while i < index:
        sold_items_list = sold_items_list + [sold_items[i]]
        i = i + 1

    return customer_name, phone_number, sold_items_list, total_cost
