import sys
import os

from challenge import sorting_odds


# Creo un array de arrays que actuen de prueba
sample_arrays_array = [[5, 3, 2, 8, 1, 4],
                       [5, 3, 1, 8, 0],
                       [],
                       [5, 3, 2, 8, 1, 4, 11],
                       [2, 22, 37, 11, 4, 1, 5, 0],
                       [1, 111, 11, 11, 2, 1, 5, 0],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                       [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]]

expected_returned_arrays_array = [[1, 3, 2, 8, 5, 4],
                                  [1, 3, 5, 8, 0],
                                  [],
                                  [1, 3, 2, 8, 5, 4, 11],
                                  [2, 22, 1, 5, 4, 11, 37, 0],
                                  [1, 1, 5, 11, 2, 11, 111, 0],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                  [0, 1, 2, 3, 4, 5, 8, 7, 6, 9]]


def test_sorting_odds():
    
    """Test que se encarga de verificar el correcto funcionamiento de la función 'sorting_odds()' del archivo
       challenge.py.
       Para llevar a cabo el test, se han definido dos arrays de arrays, que contienen una secuencia de valores
       que se va a lanzar contra la función.
       El resultado de la función se compara con el valor real esperado y, en caso de no ser correcto, el test
       genera un error.
    """
    
    for index, array in enumerate(sample_arrays_array):
        sorted_array = sorting_odds(array)
        assert sorted_array == expected_returned_arrays_array[index]