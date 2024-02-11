import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scripts.challenge as challenge




example_hashmap = {
    12:'10 + 2',
    42:'40 + 2',
    70304:'70000 + 300 + 4'
}


def test_expandedForm():
    
    """Test encarga de comprobar el correcto funcionamiento de la función 'expandedForm' definida en el archivo challenge.py.
       Para realizar el testeo, se ha definido un diccionario cuyos pares clave-valor serán empleados como método de validación.
       En concreto, se lanzará cada clave del hashmap a la función  a testear, y se comprobará que el resultado devuelto
       corresponde al valor para dicha clave dentro del hashmap.
       En caso de fallar en la verificación, el test retornaría un error.
    """
       
    for key, value in example_hashmap.items():
        expanded_form_str = challenge.expandedForm(key)
        assert expanded_form_str == value