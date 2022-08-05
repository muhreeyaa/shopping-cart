# shopping_cart.py
from cgi import print_directory
import pandas 
from pandas import read_csv #to read the inventory of products



products_df = read_csv("products.csv") 

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the de
print("------------------------------")
print("Welcome to Whole Foods")

print("We have the following", len(products), "products for sale:")
print("------------------------------")

for item in products:
    print(item["id"],".",item["name"],to_usd(item["price"]))
    # print(products)
    # print all the products with prices 


total_price = 0 
# for user input
selected_ids = [] 
valid_ids = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','done','DONE','Done']

while True:
    selected_id = input("Please input the correct product ID and type DONE when done:")
    if selected_id.upper() == "DONE":
        break 
    else:
        try:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]
            selected_ids.append(matching_product)
        except: 
            print("Oops that's not a valid product ID, please try again.")

    if not valid_ids:
        print("Oops that's not a valid product ID, please try again.")
        exit()




    
    
    

    # https://www.programiz.com/python-programming/for-loop
    # https://www.programiz.com/python-programming/while-loop

# Receipt 
# After the clerk indicates there are no more items, the program should print a custom receipt on the screen. 
# The receipt should include the following components:
# 1. A grocery store name of your choice
print("Welcome to Whole Foods")

# 2. A grocery store phone number and/or website URL and/or address of choice
print("292 Ashland Pl, Brooklyn, NY 11217")
print("https://www.wholefoodsmarket.com/")

# 3. The date and time of the beginning of the checkout process, 
# #formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
print("(718) 290-1010")
import time 
import datetime
e = datetime.datetime.now()
#importing for timestamp # https://phoenixnap.com/kb/get-current-date-time-python
print (e.strftime("%Y-%m-%d %H:%M"))
print("------------------------------")
print("Selected items")
print("------------------------------")

# 4. The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
for selected_id in selected_ids:
    print("... " +selected_id["name"],"...", "(",to_usd(selected_id["price"]),")")
print("------------------------------")


# 5. The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), 
# calculated as the sum of their prices
subtotal = sum(item["price"] for item in selected_ids)
print("SUBTOTAL:", to_usd(subtotal))

# 6. The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount 
TAX_RATE = 0.0875
tax = subtotal * TAX_RATE
print("SALES TAX (8.75%):", to_usd(tax))
# of tax owed plus the total cost of all shopping cart items

price_total = tax + subtotal
print("TOTAL: " + to_usd(price_total))


# 7. A friendly message thanking the customer and/or encouraging the customer to shop again
print("------------------------------")
print("Thanks for shopping with us, see you again soon!")
print("------------------------------")
# 8. The program should be able to process multiple shopping cart items of the same kind, but need 
# not display any groupings or aggregations of those items (although it may optionally do so).

