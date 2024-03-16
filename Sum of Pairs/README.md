# Descripción

Este script de Python está diseñado para abordar un problema común pero interesante en la manipulación de listas y aritmética básica: dado un array de enteros y un valor de suma específico, el objetivo es encontrar el primer par de valores que, sumados, igualen al valor de suma dado. Este desafío no solo pone a prueba la habilidad de trabajar con estructuras de datos y control de flujo en Python, sino que también invita a pensar en maneras eficientes de alcanzar el resultado deseado.

## Implementación

La solución implementada en este script sigue estos pasos:

* Definición de la Función get_summands(numbers_array, result_sum): Esta función es el núcleo del script, donde numbers_array es la lista de números enteros a evaluar y result_sum es el valor de suma objetivo. La función intenta encontrar y devolver el primer par de valores que sumados resultan en result_sum.

* Lógica de Procesamiento: La función itera a través del numbers_array usando dos bucles anidados para explorar todas las combinaciones posibles de pares de números y determina si suman el result_sum. Si se encuentra más de una combinación válida, la función selecciona el par cuyo segundo valor tenga el índice más pequeño en la lista original.

* Retorno de Resultados: Dependiendo de las combinaciones encontradas, la función devuelve el par de valores que cumple con la condición deseada o None si no se encuentra tal par.

## Uso

Para utilizar este script, sigue estos pasos:

* Asegúrate de tener Python instalado en tu sistema.
* Guarda el script en un archivo .py.
* Modifica la variable numbers_array y result_sum en la parte inferior del script para probar diferentes listas y valores de suma.
* Ejecuta el script desde una terminal o a través de tu entorno de desarrollo integrado (IDE) de preferencia.

El script imprimirá el primer par de valores que sumados igualan al result_sum especificado, si existe.

## Conclusión

El problema de encontrar pares de números que sumen un valor específico es una pregunta clásica en entrevistas de programación y ejercicios de algoritmia. Este script ofrece una solución directa y efectiva al problema, demostrando habilidades fundamentales en el manejo de listas y lógica de programación en Python. A través de este ejercicio, se pueden reforzar conceptos clave de programación y pensamiento computacional, útiles tanto para principiantes como para desarrolladores más experimentados.
