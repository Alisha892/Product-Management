# read.py

def load_products(file_name):
    #Load product details from the file into a dictionary.
    products = {}
    try:
        file = open(file_name, "r")
        data = file.readlines()
        p_id = 1
        for line in data:
            line = line.replace("\n", "").split(",")
            products[p_id] = {
                "Name": line[0],
                "Brand": line[1],
                "Quantity": int(line[2]),
                "Price": float(line[3]),
                "Origin": line[4]
            }
            p_id += 1
        file.close()
    except:
        print("Error: The file was not found. Ensure the file exists.")
    return products
