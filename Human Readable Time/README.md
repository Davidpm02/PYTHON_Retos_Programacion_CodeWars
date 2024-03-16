# Descripción

La función principal, set_strftime(input_seconds), toma un único argumento: input_seconds, que representa los segundos a convertir. El objetivo es traducir esta cantidad de tiempo en un formato más comprensible, específicamente en horas, minutos y segundos, siguiendo el formato HH:MM:SS.

Es importante destacar que:

* HH representa las horas, ajustadas a dos dígitos, en el rango de 00 a 99.
* MM representa los minutos, ajustados a dos dígitos, en el rango de 00 a 59.
* SS representa los segundos, ajustados a dos dígitos, en el rango de 00 a 59.
* El tiempo máximo que puede manejar esta función es de 359999 segundos, lo que equivale a 99:59:59.

## Implementación

La función set_strftime comienza verificando el tipo de dato del argumento proporcionado, asegurando que sea un entero. En caso de recibir un valor de tipo string o float, la función maneja estos casos adecuadamente, ya sea retornando un mensaje de error o convirtiendo el float a un entero, respectivamente.

Posteriormente, se lleva a cabo el cálculo de las horas, minutos y segundos mediante operaciones aritméticas básicas, sin recurrir a librerías externas como time para mantener la simplicidad y la portabilidad del código.

Finalmente, se formatea el resultado en el formato deseado HH:MM:SS, asegurando que cada componente del tiempo se ajuste a dos dígitos, y se retorna esta cadena de texto como resultado de la función.

## Uso

Para utilizar esta función, simplemente invócala con el número de segundos que deseas convertir como argumento. Aquí tienes un ejemplo de cómo hacerlo:

```
seconds_to_convert = 359999
time_string = set_strftime(seconds_to_convert)
print(time_string)
```

Este ejemplo imprimirá 99:59:59, demostrando la conversión de 359999 segundos al formato legible HH:MM:SS.

## Conclusión

Este código ofrece una solución simple y efectiva para convertir segundos en un formato de tiempo legible, siendo útil en una variedad de aplicaciones donde la representación del tiempo de manera comprensible es necesaria.
