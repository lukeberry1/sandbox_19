products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plants", 24.5, True]]

on_sale = [product for product in products if product[2]]
print(on_sale)