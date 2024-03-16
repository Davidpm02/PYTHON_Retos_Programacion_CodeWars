# Descripción

Este script de Python implementa el concepto de raíz digital, un proceso fascinante que se encuentra en el cruce de las matemáticas y la programación. La raíz digital de un número se obtiene sumando sus dígitos repetidamente hasta que el resultado se reduce a un solo dígito. Este ejercicio no solo es interesante desde un punto de vista numérico, sino que también ofrece una excelente oportunidad para practicar la recursividad y la manipulación de números en Python.

## Implementación

El código consta de dos funciones principales:

* recursive_sum(more2digits_value): Una función auxiliar que realiza la suma de los dígitos de un número. Esta función se utiliza de manera iterativa o recursiva hasta que el número se reduce a un solo dígito.

* digital_root(input_value): La función principal que orquesta el proceso de calcular la raíz digital. Acepta un número entero no negativo como entrada y utiliza recursive_sum para sumar los dígitos del número repetidamente hasta que el resultado es un solo dígito.

El flujo de trabajo asegura que el número de entrada se procese adecuadamente, manejando casos donde el input no sea un entero mediante la conversión o redondeo cuando sea necesario.

## Uso

Para usar este script:

* Guarde el código en un archivo con extensión .py.
* Ejecute el script utilizando Python en una terminal o un entorno de desarrollo que soporte Python.
* Puede modificar el valor de example_value en el bloque if __name__ == '__main__': para probar con diferentes números y observar cómo el script calcula su raíz digital.

Este proceso imprimirá el resultado de la raíz digital del número de ejemplo proporcionado, demostrando el cálculo en acción.

## Conclusión

La implementación de la raíz digital en Python es un ejercicio práctico excelente para desarrollar habilidades en la manipulación de números y la implementación de funciones recursivas. A través de este ejercicio, se pueden explorar conceptos fundamentales de la programación y matemáticas de una manera entretenida y educativa. La simplicidad del código hace que sea fácilmente adaptable para otros propósitos educativos o proyectos que requieran el procesamiento de números de forma recursiva.
