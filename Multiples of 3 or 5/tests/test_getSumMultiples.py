import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scripts.challenge as challenge

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
        sumMultiple = challenge.getSumMultiples(key)
        assert sumMultiple == value