# Descripción

Este ejercicio presenta un desafío de programación que involucra el cálculo de la cantidad máxima de pasteles que Pete puede hornear, dada una receta con cantidades específicas de ingredientes y los ingredientes disponibles en su despensa. Pete, apasionado por la repostería pero no tanto por las matemáticas, necesita ayuda para determinar cuántos pasteles puede preparar sin quedarse corto en ninguno de los ingredientes necesarios.

## Implementación

La solución a este desafío se aborda mediante la implementación de la función cakes(), que recibe dos argumentos:

* **recipe**: Un diccionario que representa la receta, donde las claves son los nombres de los ingredientes y los valores son las cantidades necesarias para hornear un solo pastel.
* **available_ingredients**: Un diccionario que muestra los ingredientes disponibles, donde las claves son los nombres de los ingredientes y los valores son las cantidades disponibles en la despensa de Pete.

La función cakes() realiza las siguientes operaciones:

* Verifica si todos los ingredientes necesarios para la receta están disponibles. Si algún ingrediente necesario no está presente, la función retorna 0, indicando que no es posible hornear ningún pastel.

* Calcula cuántos pasteles se pueden hornear iterativamente, reduciendo la cantidad de los ingredientes disponibles según se van usando en la receta, hasta que alguno de los ingredientes se agote.

* Retorna el número total de pasteles que Pete puede hornear con los ingredientes disponibles.

## Uso

Para utilizar este script, sigue los pasos a continuación:

* Asegúrate de tener Python instalado en tu sistema.
* Copia el código en un archivo .py.
* Modifica las variables recipe y available en la parte inferior del script para experimentar con diferentes recetas e ingredientes disponibles.
* Ejecuta el script desde la línea de comando o terminal. El número impreso representa la cantidad máxima de pasteles que Pete puede hornear dada la receta y los ingredientes disponibles.

Ejemplo de cómo ejecutar el script:

```
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))  # Output: El número de pasteles que se pueden hornear
```

## Conclusión

Este ejercicio ilustra una aplicación práctica de la manipulación de diccionarios y el control de flujo en Python para resolver un problema realista. Ayuda a Pete y a muchos otros en su pasión por la repostería, asegurando que puedan maximizar la cantidad de pasteles horneados con los ingredientes disponibles, todo ello mientras se afinan habilidades esenciales en programación.
