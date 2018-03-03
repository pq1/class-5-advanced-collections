# Import from step_1.py
from step_1 import transform_products_to_list
from data import products_string

# Group by customerID
def group_products_by_customer(products_string):
    # Create a dictionary of different users
    products_list = transform_products_to_list(products_string)
    customers = {}
    
    for product in products_list:
        # From the sample data, customer id is 7th or -2 of list
        # When looping through the products_string, set var to the customer id
        customer_id = product[-2]
        # Set the customers dictionary default if not in dictionary
        customers.setdefault(customer_id, []) # Create an emptry list; test says to return a list
        # Similar code
        # if customer_id not in customers:
            # customers[customer_id] = []
        # customers[customer_id].append(product)
        
        # Append the entire product list to customer by key
        customers[customer_id].append(product) 
    
    # Create a key for each user
    # Create a list of each product
    return customers

print(group_products_by_customer(products_string))