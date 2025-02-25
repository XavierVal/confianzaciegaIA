# IAvsHuman
 IA exercise vs a Human exercise

Codigo relacionado con el artículo originalmente publicado en el blog de Navegantes de la tecnología: 

 [De cuando la IA sugiere y los humanos no cuestionan](https://telefonicatech.com/blog/una-historia-de-programadores-humanos-ia-y-errores-evitables/)

## Esto es un sencillo ejemplo de un mismo ejercicio realizado con la ayuda de la IA de Copilot vs el mismo ejercicio realizado por un developer humano sin asistencia.

## En este caso, se trata de un ejercicio de programación en Python.

## Estos son los prompts de entrada que se le han dado a Copilot y al developer humano:

```shell
    Quiero crear en python una funcion que recibe 2 parametros (precio y descuento) y devuelve el importe del descuento.
    La función sería esta: calculate_discount(price, discount_percentage)
```

```shell
    Ahora quiero otra función (apply_discount) que recibe un elemento llamado cart_items que es una lista de elementos
    donde contiene un diccionario con el precio y el descuento a aplicar apply_discount(cart_items):
    donde cart_items tiene esta estructura:
    cart = [ {'price': 100, 'discount': 10}, {'price': 50, 'discount': 5}, {'price': 75, 'discount': 15} ]
    y la función devuelve la suma de todos los precios con sus descuentos correspondientes y debe usar la funcion calculate_discount
```

Diferencias entre el código generado por Copilot y el desarrollado por un humano:
Para empezar con respecto al tiempo de desarrollo, el código generado por Copilot es mucho más rápido que el desarrollado por un humano. 
En cuanto a la calidad del código, el código generado por Copilot es limpio y claro. El desarrollado por un humano tiene algo mas de complejidad.
Ambos tienen cadencias como por ejemplo no validar las entradas o los valores permitidos entre otras. Mejorando el prompt o iterando mas sobre la solución se podría mitigar este problema.
En cambio el código desarrollado por el humano tiene el sesgo de las preferencias del propio desarrollador dando su personalización/experiencia y en vez de usar un iterador "for" ha decidido usar una lambda para recorrer las distintas lineas a sumar. 
Lo que para ejemplos sencillos puede hacer mas dificil el mantenimiento para grandes volúmenes de datos puede ser más eficiente. 





