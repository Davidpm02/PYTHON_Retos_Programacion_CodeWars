"""
INTRODUCTION

Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""

def final_reversed_sentence_array(input_str):
    
    """Función auxiliar encargada de procesar una cadena recibida como input, y generar un array que contenga
       las mismas palabras, pero invertidas en caso de que estas contengan más de 5 caracteres.
    
    Keyword arguments:
        - input_str -- Cadena de texto a procesar.
    Return: 
        - final_reversed_array -- Array con los elementos de cada input ya procesados.
    """
    
    final_reversed_array = []
    
    input_str_array = input_str.split(" ")
    for _ in input_str_array: 
        if len(_) >= 5:
            _ = _[::-1]
            final_reversed_array.append(_)
        else:
            final_reversed_array.append(_)
            
    return final_reversed_array


def create_final_reversed_sentence(final_reversed_array):
    
    """Función que se encarga de recibir un array con el contenido del la oración final ya procesado.
       La funcíon define una cadena a partir del contenido de este array, y lo retorna al ámbito global.
    
    Keyword arguments:
        - final_reversed_array -- Array con el contenido de la oración recibida ya procesado.
    Return: 
        - final_reversed_sentence -- Cadena con el texto final procesado.
    """
    
    final_reversed_sentence = " ".join(final_reversed_array)
    return final_reversed_sentence
    
     
     
     
if __name__ == "__main__":
    
    input_str_array = ["Hey fellow warriors",
                       "This is a test", 
                       "This is another test"]
    
    for input_str in input_str_array:
        final_reversed_array = final_reversed_sentence_array(input_str)
        final_reversed_sentence = create_final_reversed_sentence(final_reversed_array)
        
        print(final_reversed_sentence)