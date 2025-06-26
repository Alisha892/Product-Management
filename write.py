# write.py
import os
import datetime

def generate_unique_file_name(prefix):
    """Generate a unique file name using the current date and time."""
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    # Ensure two-digit formatting for month, day, hour, minute, and second
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second

    unique_number = year + month + day + hour + minute + second
    return prefix + "_" + unique_number + ".txt"


def save_products(file_name, products):
    """Save updated product details to the text file."""
    try:
        file = open(file_name, "w")
        for p_id in products:
            details = products[p_id]
            line = details["Name"] + "," + details["Brand"] + "," + str(details["Quantity"]) + "," + str(details["Price"]) + "," + details["Origin"] + "\n"
            
            
            file.write(line)
        file.close()
        print("Products saved successfully.")
    except Exception as e:
        print("Error while saving products:", str(e))

def generate_invoice(prefix, name, items, total, products, is_restock=False):
    """Generate and save an invoice with proper content."""
    file_name = generate_unique_file_name(prefix)
    try:
        # Initialize invoice content
        invoice_content = ""

        # Add invoice header
        if is_restock:
            invoice_content += "--- RESTOCK INVOICE ---\n"
            invoice_content += "Supplier: " + name + "\n"
        else:
            invoice_content += "--- SALES INVOICE ---\n"
            invoice_content += "Customer: " + name + "\n"

        # Add current date and time
        now = datetime.datetime.now()
        date_time = (
            str(now.year) + "-" + str(now.month) + "-" + str(now.day) +
            " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        )
        invoice_content += "Date: " + date_time + "\n"
        invoice_content += "============================\n"

        # Add product details in the invoice
        total_quantity = 0
        subtotal = 0
        for item in items:
            total_quantity += item["Quantity"]
            subtotal += item["Total"]

            invoice_content += "ID: " + str(item["ID"]) + "\n"
            invoice_content += "Name: " + item["Name"] + "\n"
            invoice_content += "Qty: " + str(item["Quantity"]) + "\n"

            if not is_restock:
                invoice_content += "Free: " + str(item["Free"]) + "\n"
                price_per_item = item["Total"] / item["Quantity"] if item["Quantity"] > 0 else 0
                invoice_content += "Price: " + str(price_per_item) + "\n"
                invoice_content += "Item Total: " + str(item["Total"]) + "\n"
            invoice_content += "\n"

        # Calculate VAT and total
        vat_rate = 0.13
        vat_amount = subtotal * vat_rate
        total_with_vat = subtotal + vat_amount

        # Add totals to the invoice
        invoice_content += "============================\n"
        invoice_content += "Total Quantity: " + str(total_quantity) + "\n"
        invoice_content += "Subtotal: " + str(subtotal) + "\n"
        invoice_content += "VAT (13%): " + str(vat_amount) + "\n"
        invoice_content += "Total (incl. VAT): " + str(total_with_vat) + "\n"
        invoice_content += "============================\n"

        # Add updated product information
        invoice_content += "\n--- Updated Product Stock ---\n"
        for p_id in products:
            product = products[p_id]
            invoice_content += (
                "ID: " + str(p_id) + ", Name: " + product["Name"] +
                ", Stock: " + str(product["Quantity"]) + "\n"
            )

        # Save invoice to file
        with open(file_name, "w") as file:
            file.write(invoice_content)

        # Print confirmation
        print("Invoice saved as:", file_name)

        # Print the invoice content in the terminal
        print("\n==================================================")
        print("INVOICE DETAILS:")
        print("==================================================")
        print(invoice_content)
        print("==================================================")

    except Exception as e:
        print("Error while generating invoice:", str(e))
