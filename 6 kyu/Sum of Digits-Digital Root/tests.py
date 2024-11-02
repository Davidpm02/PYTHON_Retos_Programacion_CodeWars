import sys
import os
import random

from challenge import digital_root


example_values_hashmap = {
    16:7,
    942:6,
    132189:6,
    493193:2
    }


def test_digital_root():
    
    """Test de la función 'digital_root()' definida en el archivo challenge.py.
       Dicha función se encarga de llevar a cabo un procedimiento de suma recursiva, o 'digital root'
       con todos los números que componen el valor que recibe dicha función como argumento en su invocación.
       
       Para realizar el test, utilizo un hashmap definido arriba, e invoco a la función pasandole cada una de las
       claves. El valor resuelto es comparado con la clave del par clave-valor del hashmap.
       En caso de fallar en la comparación, el test generará un error.
    """
    
    for key, value in example_values_hashmap.items():
        recursive_sum_result = digital_root(key)
        assert recursive_sum_result == value