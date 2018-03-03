from data import products_string
from step_1 import transform_products_to_list


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    
    products = {}
    
    # Loop through list
    for product in products_list:
        # 1. Group customer
        customer_id = product[-2]
        # Group by customer
        products.setdefault(customer_id, {})
        
        # 2. Group a invoice
        invoice_id = product[0] # Pull invoice
        unit = int(product[3]) # Pull the unit
        unitprice = float(product[-3]) # Pull unitprice
        total = unit * unitprice # Get total of unit and unitprice
        # Group by invoice
        products[customer_id].setdefault(invoice_id, 0)
        # Add each total to the invoice group
        products[customer_id][invoice_id] += round(total, 2)
    return products
    
    
    # a_dict = {}

    # # For loop to add keys to a_dict
    # for product in products_list:
    #     invoice_id = product[0]
        
        
    #     unit = int(product[3])
    #     unitprice = float(product[-3])
    #     total = unit * unitprice
    #     a_dict.setdefault(invoice_id, 0)
    #     a_dict[invoice_id] += round(total,2)
    # print(a_dict)
    #     # if type(value) != int:
    #     #     a_dict[key] = None
    #     # else:
    #     #     a_dict[key] += value

##### Reference from Quiz 2