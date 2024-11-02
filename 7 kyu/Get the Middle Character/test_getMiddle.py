import sys
import os

from challenge import getMiddle



example_values_hashmap = {
    "test":"es",
    "testing":"t",
    "middle":"dd",
    "A":"A",
    "of":"of",
}


def test_getMiddle():
    
    """Test que lanza una serie de ejemplos contra la función getMiddle() definida en el archivo challenge.py.
       Para comprobar que la función actúa de la manera esperada, cada resultado será validado con un valor
       predefinido que se esperaría obtener.
       En caso de fallar esta validación, el test fallará.
    """
    
    for key, value in example_values_hashmap.items():
        middle_on__character = getMiddle(key)
        assert middle_on__character == value