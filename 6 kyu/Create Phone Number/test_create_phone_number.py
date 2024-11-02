import sys
import os
import random

from challenge import create_shape_number_array

def generate_random_lists_array():
    
    """Función auxiliar que me permite generar un array de arrays con numeros aleatorios que arrojar
       a los test de las funciones definidas en el archivo challenge.py
    
    Keyword arguments:

    Return: 
        - random_lists_array -- Array de arrays con números aleatorios con los que probar los tests.
    """
    
    
    father_array = []
    while len(father_array) != 10:
        random_array = list(random.randint(0, 9) for _ in range(10))
        father_array.append(random_array)
        continue

    return father_array




def test_create_shape_number_array():
    
    """Test encargado de probar el funcionamiento de la función auxiliar 'create_shape_number_array' definida en el archivo challenge.py de
       este reto.
       
       El test hace una invocación a la función 'generate_random_lists_array' para obtener un array de arrays
       conformados por números aleatorios del 0 al 9, con los que comprobar la correcta estructura de los 
       valores retornados.
       Prueba a generar los arrays con la estructura necesaria para definir la cadena con el número de teléfono.
    """
    
    random_lists_array = generate_random_lists_array()
    
    for array in random_lists_array:
        shape_number_array = create_shape_number_array(array)
        assert shape_number_array is not None



def test_create_shape_number():
    
    """Test encargado de probar el funcionamiento de la función auxiliar 'create_shape_number' definida en el archivo challenge.py de
       este reto.
       
       El test hace una invocación a la función 'generate_random_lists_array' para obtener un array de arrays
       conformados por números aleatorios del 0 al 9, con los que comprobar la correcta estructura de los 
       valores retornados.
       Prueba a generar los arrays con la estructura necesaria para definir la cadena con el número de teléfono.
       Se envía cada uno de los arrays generados a la función 'create_phone_number' para generar la cadena final.
       En caso de no haber formado una cadena válida, el test falla.
    """
    
    random_lists_array = generate_random_lists_array()
    
    for array in random_lists_array:
        shape_number_array = challenge.create_shape_number_array(array)
        phone_number = challenge.create_phone_number(shape_number_array)
        assert phone_number is not None