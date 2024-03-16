# Descripción

Este desafío consiste en escribir una función que reciba una palabra y devuelva el carácter o caracteres del medio. Si la longitud de la palabra es impar, se debe retornar el carácter central. Si la longitud es par, se deben retornar los dos caracteres centrales.

La función getMiddle es clave para lograr este objetivo. La determinación del carácter o caracteres centrales debe ser precisa y se espera que funcione para cualquier palabra proporcionada dentro de los límites especificados.

## Ejemplos:

* getMiddle("test") debería retornar "es".
* getMiddle("testing") debería retornar "t".
* getMiddle("middle") debería retornar "dd".
* getMiddle("A") debería retornar "A".

# Aspectos Importantes

Es crucial que la función maneje correctamente tanto palabras con longitud par como impar. La habilidad para trabajar con índices de cadenas de texto es fundamental para completar este desafío satisfactoriamente.

# Implementación

La solución se basa en una única función, getMiddle, que realiza lo siguiente:

* Determina la longitud de la palabra proporcionada.
* Utiliza la longitud para calcular el índice o índices del carácter o caracteres centrales.
* Maneja casos especiales donde la longitud de la palabra es muy corta directamente.
* En caso de palabras con longitud impar, retorna el carácter central.
* En caso de palabras con longitud par, retorna los dos caracteres centrales.
* Esta implementación demuestra un manejo efectivo de cadenas de texto y lógica condicional, habilidades esenciales en el desarrollo de software y particularmente útiles en la manipulación de datos, un aspecto crucial en el campo del Machine Learning.

# Uso

Para obtener el carácter o caracteres centrales de una palabra, simplemente se debe llamar a la función getMiddle con una cadena de texto como argumento:

´´´
middle_character = getMiddle("example")
print(middle_character)
´´´
