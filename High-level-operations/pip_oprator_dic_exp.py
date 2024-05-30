store = {
    "Muffin": 6.8, 
    "Cake":   11.2,
    "Chips":  1.4, 
    "Egg":    2.8,
    "Bread":  1.2,
    "Milk":   2.6
}

new_products = {
    "Milk Shake": 2.8,
    "Curd": 4.5, 
    "Egg": 2.8,
}


store |= new_products


print(store)