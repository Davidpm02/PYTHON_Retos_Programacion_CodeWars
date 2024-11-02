import sys
import os

from challenge import getSumMultiples

random_values_hashmap = {
    4:3,
    6:8,
    16:60,
    3:0,
    5:3,
    15:45,
    0:0,
    -1:0,
    10:23,
    20:78,
    200:9168
    }


def test_getSumMultiples():
    
    """Test que se encarga de comprobar que el resultado generado por la función getSumMultiples() tras haberle
       proporcionado un parámetro, es el correcto.
       Para comprobar esto, el test enfrenta los resultado generados frente a los valores reales esperados,
       tras invocar la función con una serie de parámetros.
    """
    
    for key, value in random_values_hashmap.items():
        sumMultiple = getSumMultiples(key)
        assert sumMultiple == value