# Descripción del Desafío

Basándome en el estilo y estructura previos, aquí tienes un documento README.md adaptado al ejercicio de factoriales y su suma:

Este ejercicio se centra en analizar y calcular una serie matemática relacionada con los factoriales. El objetivo es determinar el comportamiento de una secuencia dada por la fórmula:

    un = 1/n! ×(1!+2!+3!+...+n!)

La pregunta fundamental que este desafío plantea es qué término predomina a medida que n crece: ¿el término 1/n!  lleva la secuencia a 0, o la suma de factoriales lleva la secuencia hacia el infinito, o converge hacia otro número?

## Observación

Es importante recordar que los valores factoriales crecen rápidamente. Por lo tanto, es crucial diseñar un enfoque que maneje eficientemente entradas grandes.

## Sugerencia

Una manera eficaz de abordar este problema podría ser intentar simplificar la expresión antes de calcularla directamente.

## Implementación

El código proporciona una función going(n) que realiza el cálculo especificado. Se descompone en dos funciones principales:

* factorial(n): Calcula el factorial de n de manera iterativa, optimizando el proceso de cálculo y reduciendo el número de operaciones.
* going(n): Utiliza la función factorial para determinar el valor de la serie para un "n" dado, siguiendo la fórmula descrita anteriormente.


Esta implementación demuestra un manejo efectivo de conceptos matemáticos y de programación, tales como iteración y optimización de cálculos, que son esenciales en el desarrollo de algoritmos eficientes, especialmente relevantes en el campo del Machine Learning.

## Uso

Para calcular el valor de "un" para un "n" específico, simplemente ejecuta la función going con el valor deseado como argumento:

´´´
n = 5
resultado = going(n)
print(resultado)
´´´
