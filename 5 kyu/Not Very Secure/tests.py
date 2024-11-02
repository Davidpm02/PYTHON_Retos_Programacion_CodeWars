import sys
import os

from challenge import validating_string


tests = [("hello world_", False),
         ("PassW0rd", True),
         ("     ", False)]


def test_validating_strings():
    
    """Test encargado de validar el funcionamiento de la función 'validating_strings' definida en el archivo challenge.py.
       Para llevar a cabo esta validación, se ha definido una lista de tuplas, las cuales contienen la cadena que
       se proporciona a la función a modo de prueba, y la respuesta booleana esperada.
       En caso de que la respuesta entregada por la función no coincida con la esperada realmente, el test genera un error.
    """
    
    for example in tests:
        result = validating_string(example[0])
        assert result == example[-1]

