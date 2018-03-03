from data import products_string
def transform_products_to_list(products_string):
    # split the raw string by new lines
    split_products = products_string.split('\n') # Still a big list of lists
    
    # Have an empty list to rebuild list from parse to store the answers
    # This will clean up the empty lines (empty lines = '')
    product_list = []
    
    for product_line in split_products: # Loop through the split up string
        if product_line: # Checks to see if the product line is not empty; truthy|falsiness
        # if product_line != '': # If the line string is not empty
            # product_line type is string
            product = product_line.split(',') # Returns a list Split by the comma and store into variable
            product_list.append(product) # Append row list to results list 1 at a time
    
    return product_list
    

print(transform_products_to_list(products_string))
