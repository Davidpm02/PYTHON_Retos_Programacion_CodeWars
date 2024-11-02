import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scripts.challenge as challenge



example_test_hashmap = {
    0:"00:00:00",
    59:"00:00:59",
    60:"00:01:00",
    3599:"00:59:59",
    3600:"01:00:00",
    86399:"23:59:59",
    86400:"24:00:00",
    359999:"99:59:59"
    }


def test_set_strftime():
    
    """Test encargado de comprobar que el funcionamiento de la función 'set_strftime()' definida en el archivo
       challenge.py, revisando que el valor devuelto por esta corresponde al esperado para una serie de inputs
       de prueba.
    """
    
    for key, value in example_test_hashmap.items():
        strftime_string = challenge.set_strftime(key)
        assert strftime_string == value