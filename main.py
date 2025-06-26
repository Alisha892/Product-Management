from read import load_products
from write import save_products, generate_invoice
from operations import display_products, restock_products, sell_products

def main():
    file_name = "24046561_Alisha_Maharjan.txt"
    products = load_products(file_name)

    while True:
        print("\n1. Display Products")
        print("2. Restock Products")
        print("3. Sell Products")
        print("4. Exit System")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                display_products(products)
            elif choice == 2:
                name, phone, items, total = restock_products(products)
                save_products(file_name, products)
                generate_invoice("Restock", name, items, total,products, is_restock=True)
            elif choice == 3:
                name, phone, items, total = sell_products(products)
                save_products(file_name, products)
                generate_invoice("Sales", name, items, total,products, is_restock=False)
            elif choice == 4:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print("An error occurred: " + str(e))

# Calling the main function
main()
