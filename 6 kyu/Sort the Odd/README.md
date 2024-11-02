# Descripción

Este ejercicio aborda un problema común en la manipulación de arreglos o listas: se proporciona un array de números, y el objetivo es ordenar los números impares en orden ascendente mientras se dejan los números pares en sus posiciones originales. Este tipo de algoritmos es crucial para comprender cómo trabajar con arrays y realizar operaciones condicionales y de ordenación en programación.

## Implementación

La solución a este problema se implementa a través de la función sorting_odds(number_array), la cual realiza los siguientes pasos:

* Verificación de tipos: La función primero asegura que todos los elementos del array sean números enteros. En caso de encontrar números flotantes, estos se redondean al entero más cercano. Si se encuentra un tipo de dato no válido (por ejemplo, un str), la función retorna un mensaje de error indicando el problema.

* Extracción y ordenación de impares: La función extrae todos los números impares del array original y los ordena en orden ascendente.

* Reincorporación de impares ordenados: Finalmente, la función coloca los números impares ordenados de vuelta en sus posiciones originales en el array, manteniendo los números pares en sus lugares.

Es importante destacar que la función es cuidadosa en preservar la integridad del array original y manejar adecuadamente los tipos de datos.

## Uso

Para utilizar esta solución en su proyecto, siga estos pasos:

* Guarde el código proporcionado en un archivo con extensión .py.
* Ejecute el script en un entorno que soporte Python. Esto se puede hacer desde una terminal o un IDE que permita la ejecución de código Python.
* Puede modificar la variable example_array en la sección if __name__ == "__main__": del script para probar con diferentes arrays de números.

La ejecución del script mostrará el array original y su versión modificada con los números impares ordenados manteniendo los pares en sus posiciones.

## Conclusión

Este ejercicio proporciona una excelente oportunidad para practicar algoritmos de ordenación y manipulación de arrays en Python. Aunque el enfoque es específico para números impares, los conceptos y técnicas empleadas pueden adaptarse fácilmente para resolver problemas similares o más complejos relacionados con la ordenación y filtrado de datos en listas.
