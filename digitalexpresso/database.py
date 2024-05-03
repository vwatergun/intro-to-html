products = {
    100: {"name":"Americano","price":125},
    200: {"name":"Brewed Coffee","price":100},
    300: {"name":"Cappuccino","price":120},
    400: {"name":"Espresso","price":120}
}




def get_product(code):
    return products[code]
