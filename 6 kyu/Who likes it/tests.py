import sys
import os
import random

from challenge import process_people_array


example_trys_arrays = [[],
                       ['Peter'],
                       ['Jacob', 'Alex'],
                       ['Max', 'John', 'Mark'],
                       ['Alex', 'Jacob', 'Mark', 'Max']]

wanted_results = ['no one likes this',
                  'Peter likes this',
                  'Jacob and Alex like this',
                  'Max, John and Mark like this',
                  'Alex, Jacob and 2 others like this']



def test_process_people():
    
    """Test encargado de validar los resultados del procesamiento de los arrays contenido en el array padre
       definido arriba.
       El test comprueba si el valor resultante tras procesar el array es el esperado realmente. En caso de que
       no sea ahí, el test generará un error.
    """
    for index, _ in enumerate(example_trys_arrays):
        result_str = process_people_array(_)
        assert result_str == wanted_results[index]
        
       
       