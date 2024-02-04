import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import scripts.challenge as challenge



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
        result = challenge.validating_string(example[0])
        assert result == example[-1]

