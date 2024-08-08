# You have two lists named inventory1 and inventory2 representing the clothing items from these stores.
# Now, your prime mission is to figure out the clothes that are exclusive to each store.
# Note that the letter casing is not important, so items like "t-shirt" and "T-Shirt" are considered the same.
# Return all exclusive clothes sorted in alphabetical order.

def exclusive_products(inventory1, inventory2):
      
    upperCaseInventory1 = {item.upper() for item in inventory1}
    upperCaseInventory2 = {item.upper() for item in inventory2}
    
    exclusiveItems1 = upperCaseInventory1 - upperCaseInventory2
    exclusiveItems2 = upperCaseInventory2 - upperCaseInventory1
    
    exclusiveSorted1 = sorted(item for item in exclusiveItems1)
    exclusiveSorted2 = sorted(item for item in exclusiveItems2)
    
    return (exclusiveSorted1,exclusiveSorted2)
    
    

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
