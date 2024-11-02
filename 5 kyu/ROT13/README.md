# Descripción

Este ejercicio se centra en la implementación de una función de cifrado y descifrado conocida como ROT13. ROT13 es un caso especial de cifrado César que consiste en sustituir cada letra por la letra que se encuentra 13 posiciones después en el abecedario. Si se aplica ROT13 a un texto cifrado por ROT13, se obtiene el texto original, lo que significa que la misma operación se utiliza tanto para cifrar como para descifrar.

El objetivo principal es practicar la manipulación de cadenas y entender los conceptos básicos de cifrado. Este ejercicio propone un enfoque práctico para familiarizarse con el cifrado ROT13, ampliamente utilizado para obfuscar spoilers, chistes, o información sensible en foros en línea como USENET.

## Implementación

La solución propuesta define una función principal rot13, encargada de realizar el cifrado ROT13 de una cadena de texto proporcionada como entrada. Dentro de esta función, se realiza un mapeo de cada letra del abecedario a su correspondiente letra cifrada, teniendo en cuenta la regla de ROT13.

Para mantener la fidelidad al texto original en términos de mayúsculas y minúsculas, se implementa una función auxiliar turnToUppercase, la cual ajusta el tamaño de las letras en la cadena cifrada basándose en el texto de entrada. Esto asegura que el texto cifrado mantenga la misma capitalización que el texto original.

La implementación utiliza listas para representar el abecedario en inglés y un diccionario para mapear cada letra a su correspondiente letra cifrada según ROT13. Luego, se procesa el texto de entrada carácter por carácter, aplicando el cifrado a las letras mientras se dejan sin cambios los caracteres que no son letras.

## Uso

Para usar esta función de cifrado ROT13, sigue estos pasos:

* Guarda el código proporcionado en un archivo con extensión .py.
* Abre una terminal o consola de comandos y navega hasta el directorio donde se encuentra el archivo.
* Ejecuta el script usando Python con el comando python nombre_del_archivo.py.
* Puedes modificar la variable input_text en la parte inferior del script para probar la función con diferentes cadenas de texto y observar los resultados del cifrado y descifrado.

## Conclusión

Este ejercicio ofrece una excelente oportunidad para comprender el funcionamiento de los cifrados César, específicamente ROT13, a través de una implementación práctica en Python. Además de reforzar habilidades en la manipulación de cadenas y estructuras de datos como listas y diccionarios, el ejercicio demuestra la importancia de los métodos de cifrado, incluso en sus formas más básicas, para la seguridad de la información y la privacidad en la comunicación digital.
