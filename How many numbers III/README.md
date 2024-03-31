# Descripción

El objetivo principal de este ejercicio es encontrar todos los números de una determinada cantidad de dígitos (count) cuya suma de dígitos sea igual a un valor específico (sum_). Además, este algoritmo se asegura de que en cada número válido encontrado, ningún dígito sea menor que el dígito que le precede. El resultado final es un array que contiene tres elementos:

* El número total de coincidencias encontradas.
* El valor mínimo encontrado.
* El valor máximo encontrado.

Este ejercicio ofrece una oportunidad para practicar y entender mejor el manejo de arrays, iteraciones, y el filtrado de datos basado en condiciones específicas utilizando Python y la librería NumPy.

## Implementación

El código se estructura principalmente alrededor de la función find_all(sum_, count), la cual realiza todo el proceso descrito anteriormente. Dentro de esta función, se define una función auxiliar getValidNum(num), utilizada para verificar si un número cumple con la condición de que cada dígito no sea menor que el dígito anterior.

La implementación hace uso intensivo de comprensiones de lista para filtrar y procesar los números que cumplen con las condiciones especificadas, y de la librería NumPy para la manipulación eficiente de los arrays.

A continuación se describen los pasos clave en la implementación:

* Generación de una lista de números que tienen una cantidad de dígitos igual a count.
* Filtrado de esta lista para encontrar aquellos números cuya suma de dígitos sea igual a sum_.
* Aplicación de la validación para asegurar que en los números filtrados, ningún dígito es menor que el que le precede.
* Creación de un array resultado que contiene el número total de coincidencias, el valor mínimo, y el valor máximo encontrados.

## Uso

Para utilizar este código, simplemente hay que ejecutar el script de Python. El punto de entrada del programa (if __name__ == "__main__":) ya contiene un llamado a la función find_all con un ejemplo de parámetros (sum_ = 10 y count = 3).

```python
    if __name__ == "__main__":
        result_array = find_all(10, 3)
        print(result_array)
```

Este llamado imprimirá el array resultante, el cual contiene el número total de coincidencias, y los valores mínimo y máximo, respectivamente, para números de 3 dígitos cuya suma de dígitos es 10.

## Conclusión

Este ejercicio demuestra la capacidad de Python y NumPy para realizar operaciones complejas de filtrado y procesamiento de datos de manera eficiente. La solución presentada ilustra conceptos importantes como la comprensión de listas, el uso de funciones auxiliares, y la manipulación de arrays, los cuales son esenciales en el ámbito del desarrollo de software y la ciencia de datos. Este ejercicio no solo es útil para entender mejor estos conceptos, sino también para practicar habilidades de programación en Python.
