# Descripción

El algoritmo de "Instant Runoff Voting" (IRV), también conocido como votación por eliminación instantánea, es un método electoral utilizado para elecciones con un solo ganador, donde los votantes clasifican a los candidatos por preferencia en lugar de votar por un único candidato. Este ejercicio implementa el algoritmo IRV para determinar el ganador de una elección basada en las preferencias de los votantes proporcionadas.

## Implementación

El código proporcionado en Python define una función runoff(voters) que recibe un arreglo de listas, donde cada lista contiene las preferencias de votación de un votante individual, ordenadas de la más preferida a la menos preferida. La función sigue los siguientes pasos para determinar el ganador de las elecciones:

* Verifica que todas las listas de votación tengan la misma longitud.
* Inicializa un conjunto con todos los candidatos y un diccionario para contar los votos.
* Implementa el algoritmo IRV, que incluye:
  * Contar los votos para cada candidato basado en las primeras preferencias.
  * Si un candidato tiene más de la mitad de los votos, este se declara ganador.
  * Si no hay un ganador claro, el candidato con menos votos se elimina, y los votos se recalculan basándose en las siguientes preferencias.
  * Este proceso se repite hasta que un candidato alcanza más de la mitad de los votos.

El código utiliza aserciones para garantizar que todas las votaciones tienen la misma longitud y emplea bucles y estructuras de control para implementar la lógica del IRV.

## Uso

Para utilizar este script, debes tener una lista de votaciones donde cada votación es una lista de candidatos ordenados por preferencia. Aquí un ejemplo de cómo llamar a la función:

```python
voters = [
    ['Candidato A', 'Candidato B', 'Candidato C'],
    ['Candidato B', 'Candidato C', 'Candidato A'],
    ['Candidato C', 'Candidato A', 'Candidato B']
]
winner = runoff(voters)
print(winner)
```

Este código imprimirá el nombre del ganador de las elecciones según el algoritmo de votación por eliminación instantánea.

## Conclusión

El ejercicio "Instant Runoff Voting" implementa de manera efectiva el algoritmo IRV en Python, ofreciendo una solución para determinar el ganador en elecciones donde se utiliza la votación por orden de preferencia. Es una excelente demostración de cómo los algoritmos de votación pueden ser implementados y simulados utilizando programación, proporcionando una herramienta útil para entender mejor estos procesos electorales.
