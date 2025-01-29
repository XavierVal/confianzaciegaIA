def calculate_discount(price, discount_percentage):
    """
    Calcula el importe del descuento dado un precio y un porcentaje de descuento.

    :param price: El precio original del producto.
    :param discount_percentage: El porcentaje de descuento a aplicar.
    :return: El importe del descuento.
    """
    discount_amount = price * (discount_percentage / 100)
    return discount_amount

def apply_discount(cart_items):
    """
    Aplica los descuentos a los elementos del carrito y devuelve la suma total de los precios con descuento.

    :param cart_items: Lista de diccionarios con 'price' y 'discount'.
    :return: Suma total de los precios con descuento.
    """
    total = 0
    for item in cart_items:
        price = item['price']
        discount = item['discount']
        discount_amount = calculate_discount(price, discount)
        total += price - discount_amount
    return total

# Ejemplo de uso
cart = [
    {'price': 100, 'discount': 10},
    {'price': 50, 'discount': 5},
    {'price': 75, 'discount': 15}
]

total_con_descuento = apply_discount(cart)
print(f"Total con descuento: {total_con_descuento}")