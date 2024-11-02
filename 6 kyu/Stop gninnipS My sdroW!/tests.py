import sys
import os
import random

from challenge import final_reversed_sentence_array, create_final_reversed_sentence

def test_create_final_reversed_sentence():
    
    """Test encargado de proporcionar una serie de cadenas a las funciones definidas en el archivo
       challenge.py, para revisar el correcto funcionamiento de la finalidad del mismo.
    """
    
    # Defino un diccionario de cadenas, cada uno contenieno una cadena de ejemplo, y su resultado.
    
    example_strings_hashmap = {
        "Welcome":"emocleW",
        "to":"to",
        "CodeWars":"sraWedoC",
        "Hey fellow warriors":"Hey wollef sroirraw",
        "This sentence is a sentence":"This ecnetnes is a ecnetnes",
        "I'm so happy to be here":"I'm so yppah to be here"
    }
    
    for key, value in example_strings_hashmap.items():
        final_reversed_array = final_reversed_sentence_array(key)
        final_reversed_sentence = create_final_reversed_sentence(final_reversed_array)
        
        assert final_reversed_sentence == value
     