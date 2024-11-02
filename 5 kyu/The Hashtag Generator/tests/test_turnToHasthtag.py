import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scripts.challenge as challenge



example_values_hashmap = {
    "Codewars       ":"#Codewars",
    " Codewars":"#Codewars",
    "     Codewars":"#Codewars",
    "Codewars Is Nice":"#CodewarsIsNice",
    "codewars is nice":"#CodewarsIsNice",
    "CoDeWaRs is niCe":"#CodewarsIsNice",
    "c i n":"#CIN",
    "codewars  is  nice        ":"#CodewarsIsNice",
    "":False,
    "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat": False
    }


def test_turnToHashtag():
    
    """Test encargado de verificar que la función 'turnToHashtag' del archivo challenge.py, retorna el valor esperado
       con respecto al parámetro recibido.
       Para ello, el test realiza una serie de comprobaciones en las que lanza una cadena a la función y compara el 
       resultado ofrecido con el real esperado.
    """
    
    for key, value in example_values_hashmap.items():
        final_hashtag = challenge.turnToHashtag(key)
        assert final_hashtag == value
    