# 15:08 Timestamp

def calculate_discount(price: int, discount_percentage: int):
    '''
    Quiero crear en python una funcion que recibe 2 parametros (precio y descuento) y devuelve el importe del descuento.
    La función sería esta: calculate_discount(price, discount_percentage)
    :param price: precio del producto
    :param discount_percentage: descuento del producto
    :return:
    '''
    discount = price * (discount_percentage / 100)
    print(f"El importe del descuento es {discount} €")
    return discount


def apply_discount(cart_items: list):
    '''
    Ahora quiero otra función (apply_discount) que recibe un elemento llamado cart_items que es una lista de elementos
    donde contiene un diccionario con el precio y el descuento a aplicar apply_discount(cart_items):
    donde cart_items tiene esta estructura:
    cart = [ {'price': 100, 'discount': 10}, {'price': 50, 'discount': 5}, {'price': 75, 'discount': 15} ]
    y la función devuelve la suma de todos los precios con sus descuentos correspondientes y debe usar la funcion calculate_discount
    :param cart_items:
    :return:
    '''
    total = 0
    total = sum(map(lambda x: x['price']-calculate_discount(price=x['price'], discount_percentage=x['discount']), cart_items))
    print(f"La suma total de los productos despues de su descuento es: {total}")


if __name__ == "__main__":
    calculate_discount(price=100, discount_percentage=25)
    apply_discount(cart_items=[{'price': 100, 'discount': 10}, {'price': 50, 'discount': 5}, {'price': 75, 'discount': 15}])

# 15:29 Timestamp