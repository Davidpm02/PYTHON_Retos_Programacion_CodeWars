# Descripción del Reto

Este reto consiste en desarrollar una función capaz de tomar un número entero positivo y devolver una cadena que represente este número en su forma expandida. Es decir, desglosar el número en cada uno de sus dígitos significativos multiplicados por su valor posicional, exceptuando los ceros, y luego unir estos componentes con el signo "+" para reflejar la suma que representan juntos.

Por ejemplo, al aplicar la función a diferentes números, obtenemos los siguientes resultados:

* expanded_form(12) retorna '10 + 2'.
* expanded_form(42) retorna '40 + 2'.
* expanded_form(70304) retorna '70000 + 300 + 4'.

  
### Nota Importante:

Todos los números de entrada serán enteros mayores que 0.

---

## Implementación

La función expandedForm es el núcleo de esta solución. A continuación, describo el enfoque general y algunos puntos clave de la implementación:

* **Descomposición del Número**: La función procesa el número de entrada, descomponiéndolo en sus dígitos constituyentes, considerando su posición y valor posicional.
* **Iteración y Construcción**: Se itera sobre cada dígito del número, construyendo la parte correspondiente de su forma expandida, omitiendo aquellos dígitos que son cero, ya que no aportan valor en la forma expandida.
* **Generación del Resultado**: Los componentes generados se unen en una cadena, utilizando el signo "+" para simbolizar la suma que representan, conformando así la representación en forma expandida del número.

Este enfoque no solo demuestra habilidades en manipulación de cadenas y lógica matemática, sino que también resalta la capacidad de pensar en términos de representación numérica y procesamiento de datos a un nivel más detallado.

---

## Uso

Para utilizar la función, simplemente llámela con un número entero positivo como argumento. La función devolverá una cadena que representa la forma expandida de dicho número, facilitando su comprensión y visualización en términos de sus componentes valor-posicionales.

Este reto no solo es un ejercicio fascinante de programación, sino también una oportunidad para profundizar en el entendimiento de los números y su representación, algo esencial en el campo del desarrollo de Machine Learning y la ciencia de datos en general.
