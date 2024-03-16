# Descripción

El objetivo de este ejercicio es implementar una función que valide si una cadena de caracteres ingresada por el usuario es alfanumérica. Se establece que la cadena dada no es nula, por lo tanto, no es necesario verificar este aspecto. Para ser considerada alfanumérica, la cadena debe cumplir con las siguientes condiciones:

* Contener al menos un carácter (una cadena vacía no es válida).
* Los caracteres permitidos son letras latinas en mayúsculas y minúsculas, y dígitos del 0 al 9.
* No se permiten espacios en blanco ni guiones bajos.

## Implementación

La solución se centra en la implementación de la función validating_string, la cual recibe una cadena de caracteres como argumento y retorna un valor booleano indicando si la cadena es alfanumérica o no, siguiendo las condiciones mencionadas.

Dentro de la función, se realizan las siguientes comprobaciones:

* Se verifica que la cadena no contenga espacios en blanco.
* Se comprueba que la longitud de la cadena sea al menos de un carácter.
* Finalmente, se valida si todos los caracteres de la cadena son alfanuméricos.
* Si la cadena cumple con todas estas condiciones, la función retorna True. En caso contrario, retorna False.

## Uso

Para utilizar esta función, sigue los pasos a continuación:

* Asegúrate de tener Python instalado en tu sistema.
* Guarda el código proporcionado en un archivo .py.
* Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra el archivo guardado.
* Ejecuta el script con el comando python nombre_del_archivo.py.
* Puedes modificar el valor de example_string en el bloque if __name__ == "__main__": para probar la función con diferentes cadenas y verificar su comportamiento.

## Conclusión

Este ejercicio ofrece una solución práctica y eficiente para validar cadenas de caracteres alfanuméricas, cumpliendo con criterios específicos. La implementación de la función validating_string demuestra la utilización de métodos básicos de cadenas en Python, proporcionando un ejemplo claro de cómo realizar validaciones de forma sencilla y efectiva. Este código puede ser útil en aplicaciones donde la validación de entrada de datos es crítica para el funcionamiento correcto del programa.
