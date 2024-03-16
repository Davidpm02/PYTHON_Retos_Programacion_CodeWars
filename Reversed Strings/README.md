# Descripción

Este ejercicio se enfoca en desarrollar una solución que invierte una cadena de texto proporcionada por el usuario. La tarea consiste en tomar un string de entrada y devolverlo en orden inverso. Este tipo de algoritmos es fundamental para comprender cómo trabajar con cadenas de texto y listas en programación, además de ser una base para problemas más complejos de manipulación de strings.

## Implementación

La implementación de esta solución se realiza a través de dos funciones principales:

* make_reversed_list(input): Esta función toma una cadena de texto como entrada y retorna una lista donde cada elemento corresponde a un carácter de la cadena original, pero en orden inverso. Se realiza una comprobación para asegurar que el input es de tipo str. Si no es así, la función retorna un mensaje indicando que se esperaba una cadena de texto.

* build_a_result(reversed_word_list): Esta función toma la lista generada por make_reversed_list y une sus elementos para formar una nueva cadena de texto, que es la versión invertida de la cadena original.

La implementación evita el uso de métodos directos de Python que permitirían invertir la cadena con una única operación, como input[::-1], para ilustrar cómo se puede lograr el mismo resultado mediante un enfoque más manual y educativo.

## Uso

Para utilizar este script, sigue los pasos a continuación:

* Guarde el código en un archivo .py.
* Abra una terminal o línea de comandos y navegue hasta el directorio donde se encuentra el archivo guardado.
* Ejecute el script con Python mediante el comando python nombre_del_archivo.py.
* Cuando se le solicite, introduzca la cadena de texto que desea invertir y presione Enter.
* El script procesará la entrada y mostrará la cadena original junto con su versión invertida.

## Conclusión

Este ejercicio ofrece una valiosa oportunidad para practicar y entender el manejo de cadenas de texto y listas en Python. Aunque Python ofrece herramientas que simplifican este tipo de operaciones, implementar la solución desde un enfoque más básico permite a los desarrolladores principiantes entender mejor los fundamentos del lenguaje y las estructuras de datos. Además, este tipo de problemas fomenta el pensamiento lógico y la resolución de problemas, habilidades esenciales en el desarrollo de software.
