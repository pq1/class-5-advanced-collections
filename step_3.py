# Will not use step_2 code to group
from data import products_string
from step_1 import transform_products_to_list


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    # Create a dictionary
    products = {}
    
    for product in products_list:
        # Pull out invoice
        invoice_id = product[0]
        # Pull out customer_id
        customer_id = product[-2]
        
        # Groups Customer_id and creates a new dictionary
        products.setdefault(customer_id, {})
        
        # Within new dictionary, groups the invoice and creates a list
        products[customer_id].setdefault(invoice_id, [])
        
        # Add each invoice to list
        products[customer_id][invoice_id].append(product)
        
    return products
    
