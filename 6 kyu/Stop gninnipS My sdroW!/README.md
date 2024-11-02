## Descripción

Este script de Python se centra en una tarea de procesamiento de texto que consiste en invertir las palabras de una oración que tienen cinco o más letras. El objetivo es recibir una cadena de texto que contenga una o más palabras y devolver la misma cadena, pero con las palabras de cinco o más letras invertidas. Este tipo de desafíos son útiles para mejorar las habilidades de manipulación de cadenas de texto y entender mejor cómo trabajar con estructuras de datos como listas y cadenas en Python.

## Implementación

El código se compone de dos funciones principales:

* final_reversed_sentence_array(input_str): Esta función toma una cadena de texto como entrada y la divide en palabras. Luego, verifica la longitud de cada palabra; si una palabra tiene cinco o más letras, la invierte. Las palabras modificadas (o no modificadas, según el caso) se almacenan en un array.

* create_final_reversed_sentence(final_reversed_array): Recibe el array procesado por la función anterior y une sus elementos en una cadena de texto, separando las palabras por espacios. Esta cadena es la versión final de la oración con las palabras necesarias invertidas.

El flujo del programa asegura que solo las palabras que cumplen con el criterio de longitud sean invertidas, manteniendo la estructura original de la oración y los espacios cuando hay más de una palabra.

## Uso

Para utilizar este script en su proyecto, siga estos pasos:

* Guarde el código en un archivo .py.
* Ejecute el script en un entorno que soporte Python. Puede hacer esto desde una terminal o utilizando un IDE compatible con Python.
* Modifique la variable input_str_array en el bloque if __name__ == "__main__" para incluir las oraciones que desea procesar.

Al ejecutar el script, este imprimirá en la consola la versión procesada de cada oración incluida en input_str_array, mostrando las palabras de cinco o más letras invertidas.

## Conclusión

Este ejercicio proporciona una introducción práctica a la manipulación de cadenas de texto en Python, demostrando cómo se pueden aplicar operaciones básicas de cadenas y listas para resolver problemas comunes de procesamiento de texto. Aunque el script se centra en un caso de uso específico, las técnicas y métodos utilizados aquí pueden adaptarse fácilmente para abordar desafíos similares en el ámbito del procesamiento de lenguaje natural o en cualquier otra situación que requiera manipulación avanzada de cadenas de texto.
