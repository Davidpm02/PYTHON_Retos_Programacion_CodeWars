# Descripción

Este script de Python, denominado Generador de Hashtags, es una herramienta creada para automatizar y simplificar la generación de hashtags para el equipo de marketing. Dada la importancia de los hashtags en las estrategias de marketing digital de hoy en día, este script ofrece una solución eficiente para crear hashtags atractivos y formateados correctamente a partir de cadenas de texto.

## Implementación

La implementación del Generador de Hashtags sigue estos pasos clave:

* Validación de la Entrada: La función turnToHashtag(string) comienza verificando que el argumento string sea de tipo cadena. Si no es así, retorna un mensaje indicando que no es posible generar un hashtag.

* Procesamiento de la Cadena: La cadena de entrada se procesa eliminando espacios extra al principio y al final. Luego, se divide en palabras basándose en los espacios.

* Capitalización y Creación del Hashtag: Cada palabra se capitaliza (es decir, su primera letra se convierte en mayúscula) y se concatena con las demás, prefijando el resultado con el símbolo # para formar el hashtag.

* Validaciones Finales: Si el hashtag resultante supera los 140 caracteres, o si la cadena de entrada estaba vacía, la función retorna False.

## Uso

Para utilizar este script, sigue estos pasos:

* Asegúrate de que Python esté instalado en tu sistema.
* Guarda el código en un archivo .py.
* Modifica la variable string al final del script para probar el generador con diferentes frases.
* Ejecuta el script. Se imprimirá el hashtag generado o False si no cumple con las condiciones.

Ejemplo de ejecución:

```
string = " Hello there thanks for trying my Kata"
final_hashtag = turnToHashtag(string)
print(final_hashtag)
```

## Conclusión

El Generador de Hashtags es una herramienta práctica para automatizar la creación de hashtags a partir de cadenas de texto, ahorrando tiempo y esfuerzo al equipo de marketing. Su implementación en Python demuestra la versatilidad y potencia del lenguaje para realizar tareas de procesamiento de texto y automatización. Este ejercicio no solo es útil para entender mejor las operaciones con cadenas en Python, sino también para apreciar cómo la programación puede solucionar problemas cotidianos en el mundo del marketing digital.
