"""
DESCRIPTION

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""


# To make this challenge, I suppose I'm not be able to use any Python standard library that let me to reach the target at once.

def make_reversed_list(input):
    
    """Función auxiliar que me permite procesar un input recibido como parámetro, y crear una lista que contenga los caracteres que
       componen dicho input, pero invertidos.
       
    Keyword arguments:
        - input -- Cadena a procesar.
    Return: 
        - reversed_word_list -- Array con los componentes principales del parámetro 'input' (sus letras), dispuestos en el array 
                               inversamente a como lo estaban en la cadena original.
                            
    """
    
    # Primero, demos asegurarnos de que el input recibido es una cadena de texto.
    if not isinstance(input, str):
        return "Se esperaba un input de tipo cadena de texto."
    
    else:
        reversed_word_list = []
        for letter in input:
            reversed_word_list.insert(0, letter)
        
        # También sería posible:
        #for index, letter in enumerate(input):
        #    if index == 0:
        #        reversed_word_list.append(letter)
        #    else:
        #        reversed_word_list.insert(0, letter)

        
    return reversed_word_list


def build_a_result(reversed_word_list):
    
    """Función auxiliar encargada de procesar un array recibido como parámetro, y retornar un string compuesto por cada elemento
       que conforma la lista recibida.
    
    Keyword arguments:
        - reversed_word_list -- Array con las letras del input recibido como parámetro, dispuestos de manera inversa.
    Return: 
        - reversed_result -- String final compuesto por los elementos contenidos en la lista recibida como parámetro.
    """
    
    reversed_result = "".join(reversed_word_list)
    return reversed_result



if __name__ == '__main__':
    
    input_str = input("Proporcione la cadena a invertir:")
    reversed_word_list = make_reversed_list(input_str)
    reversed_result = build_a_result(reversed_word_list)
    
    print(f"{input_str} => {reversed_result}")
    
    
    
    
    