# Descripción del Reto

Este desafío implica escribir una función que acepte un array de 10 enteros (entre 0 y 9) y retorne una cadena de texto que represente esos números en el formato de un número de teléfono.

La función create_phone_number es la clave para lograr este objetivo. La forma en que se presenta el número de teléfono es específica y debe seguir el formato: "(XXX) XXX-XXXX".

### Ejemplo:

Al llamar create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), la función retorna "(123) 456-7890".

##### Aspectos Importantes:

* El formato retornado debe ser correcto para completar este desafío con éxito.
  
* Es crucial no olvidar el espacio después del paréntesis de cierre.

---

### Implementación

La solución se divide en dos partes principales:

* **create_shape_number_array**: Esta función prepara el array que define la estructura del número de teléfono. Asegura que el array de entrada tenga exactamente 10 dígitos y que todos sean enteros válidos entre 0 y 9. Luego, organiza los elementos del array para reflejar la estructura de un número de teléfono, incluyendo paréntesis y guiones en las posiciones correctas.

* **create_phone_number**: Esta función toma el array estructurado generado por create_shape_number_array y lo convierte en una cadena de texto. Utiliza una expresión regular para validar que la cadena final cumpla con el formato requerido de un número de teléfono.

La combinación de estas funciones demuestra un manejo efectivo de arrays, cadenas de texto y expresiones regulares, habilidades esenciales en el desarrollo de software y especialmente útiles en la manipulación y validación de datos, un aspecto crucial en el campo del Machine Learning.

---

## Uso

Para generar un número de teléfono en el formato deseado, primero se debe llamar a create_shape_number_array con un array de 10 dígitos como argumento. Luego, el array resultante se pasa a create_phone_number para obtener la cadena final del número de teléfono.

Este reto no solo es un excelente ejercicio para practicar la manipulación de datos y el uso de expresiones regulares, sino que también ofrece una visión práctica de cómo las tareas comunes de procesamiento de datos pueden ser implementadas y automatizadas en proyectos de desarrollo de software y Machine Learning.
