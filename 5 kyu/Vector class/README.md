# Descripción

Este ejercicio propone la creación de un objeto Vector que es capaz de realizar operaciones matemáticas básicas entre vectores. Estas operaciones incluyen la suma, la resta, el producto punto y el cálculo de la norma del vector. Se busca proporcionar una herramienta útil para el manejo de vectores en un entorno de programación, simulando algunas de las operaciones más comunes en matemáticas y física.

## Implementación

La implementación se realiza a través de la clase Vector, que inicialmente almacena el vector como una lista de sus componentes. La clase define los siguientes métodos:

* **__init__(self, contenido)**: Constructor que inicializa el vector con los componentes proporcionados.
* **add(self, sumand_vector)**: Retorna un nuevo Vector que es el resultado de la suma del vector actual y otro vector proporcionado como argumento.
* **subtract(self, sumand_vector)**: Retorna un nuevo Vector que es el resultado de la resta del vector actual por otro vector.
* **dot(self, sumand_vector)**: Calcula y retorna el producto punto entre el vector actual y otro vector.
* **norm(self)**: Calcula y retorna la norma (o magnitud) del vector actual.
* **equals(self, vector)**: Comprueba si el vector actual es igual a otro vector, basándose en sus componentes.
* **__str__(self)**: Sobrecarga el método __str__ para ofrecer una representación en forma de cadena del vector, facilitando su visualización.

Cabe destacar que, para las operaciones de suma, resta y producto punto, se verifica que ambos vectores tengan la misma longitud. En caso contrario, se levanta una excepción.

## Uso

Para utilizar esta clase Vector en tus propios proyectos, sigue estos pasos:

* Asegúrate de tener un entorno de ejecución de Python listo.
* Incluye la clase Vector en tu código.
* Crea instancias de la clase Vector con los componentes deseados.
* Utiliza los métodos disponibles para realizar operaciones entre vectores.

Ejemplo de uso:

```
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.add(b))  # Debería imprimir: (4,6,8)
print(a.subtract(b))  # Debería imprimir: (-2,-2,-2)
print(a.dot(b))  # Debería imprimir: 26
print(a.norm())  # Debería imprimir: 3.7416573867739413
```

## Conclusión

La clase Vector proporciona una forma sencilla y eficaz de manejar operaciones vectoriales básicas en Python. A través de su implementación, se facilita la manipulación y el cálculo con vectores, elementos fundamentales en diversas áreas de las matemáticas y la física. Con esta herramienta, se espera que los usuarios puedan integrar y aplicar conceptos vectoriales en sus proyectos de programación de manera más intuitiva y eficiente.
