# Descripción

Este ejercicio consiste en escribir una función que formatea una duración, dada como un número de segundos, de una manera amigable para el ser humano. La función debe aceptar un entero no negativo. Si es cero, simplemente devuelve "now". De lo contrario, la duración se expresa como una combinación de años, días, horas, minutos y segundos.

# Ejemplo

* Para seconds = 62, tu función debería devolver "1 minute and 2 seconds".
* Para seconds = 3662, tu función debería devolver "1 hour, 1 minute and 2 seconds".
  
## Reglas Detalladas

* La expresión resultante está hecha de componentes como "4 seconds", "1 year", etc. En general, un entero positivo y una de las unidades de tiempo válidas, separadas por un espacio. La unidad de tiempo se usa en plural si el entero es mayor que 1.
* Los componentes se separan por una coma y un espacio (", "). Excepto el último componente, que se separa por " and ", justo como se escribiría en inglés.
* Una unidad de tiempo más significativa ocurrirá antes que una menos significativa.
* Diferentes componentes tienen diferentes unidades de tiempo. Así que no hay unidades repetidas.
* Un componente no aparecerá en absoluto si su valor resulta ser cero.
* Una unidad de tiempo debe usarse "tanto como sea posible". Esto significa que la función no debería devolver 61 segundos, sino 1 minuto y 1 segundo en su lugar.

## Uso

```
seconds = 15731070
readable_string = format_duration(seconds)
print(readable_string)
```

## Implementación

La implementación detalla la creación de una función format_duration que procesa un parámetro seconds, generando una cadena legible que facilita la representación del tiempo transcurrido. Este proceso se realiza a través de la conversión del tiempo expresado en segundos a una combinación más comprensible de años, días, horas, minutos y segundos.

La solución propuesta evita el uso de librerías externas para la conversión de tiempo, basándose en operaciones aritméticas y lógica condicional para calcular y construir la cadena de tiempo legible.
