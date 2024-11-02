# Descripción

Este programa está diseñado para resolver un problema matemático específico: calcular la suma de todos los múltiplos de 3 o 5 que son menores que un número dado. La motivación detrás de este ejercicio proviene de un desafío de programación común que no solo pone a prueba la comprensión de los bucles y la lógica condicional, sino que también invita a reflexionar sobre la eficiencia y la optimización del código.

La función central, getSumMultiples, toma un solo argumento entero y devuelve la suma de todos los múltiplos de 3 y 5 menores que este número. Si el número dado es negativo, la función devuelve 0, siguiendo la regla de que solo los números naturales son considerados. Además, este programa trata de manera eficiente los casos en los que un número es múltiplo tanto de 3 como de 5, asegurando que se cuente una sola vez para evitar la duplicación en la suma final.

## Cómo Usar

Para utilizar este script, simplemente necesitas tener Python instalado en tu sistema. No requiere ninguna dependencia externa.

* Guarda el script en un archivo .py.
* Abre una terminal o consola de comandos.
* Navega hasta el directorio donde se encuentra el archivo.
* Ejecuta el script con Python:
  
```
python nombre_del_archivo.py
```

## Ejemplo de Uso

Supongamos que el archivo se llama sum_of_multiples.py. Para ejecutarlo:

```
python sum_of_multiples.py
```

Por defecto, el script ejecutará un ejemplo con el número 10, lo cual debería resultar en la impresión de 23 en la consola, ya que 3, 5, 6 y 9 son los múltiplos de 3 o 5 menores que 10, y su suma es 23.

## Personalización

Puedes modificar el valor de la variable value dentro de la sección if __name__ == "__main__": para probar la función con diferentes números y observar los resultados.
