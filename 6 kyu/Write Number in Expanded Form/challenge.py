"""
DESCRIPTION

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'


NOTE: All numbers will be whole numbers greater than 0.
"""

def expandedForm(ini_number):
    
    """
       Función auxiliar encargada de procesar un número de entrada, y retornar un string que represente la suma entre las 
       diferentes unidades que componen dicho número.
    
    Keyword arguments:
        - ini_number -- Número inicial, del cual queremos obtener la suma de las diferentes unidades que componen a dicho 
                        número. 
    Return: 
        - expanded_form_str -- Cadena de texto que representa la suma de las diferentes unidades que componen a dicho número.
        
    """
    
    # Para llevar a cabo el ejercicio, vamos a tener que tener en cuenta siempre la longitud de caracteres que componen
    # al numero
    n_characters = len(str(ini_number))
    units_number_list = []
    
    for character in str(ini_number):
        n_characters -=1
        
        if n_characters == 0:   # Si el número iterado se encuentra en la última posición el input recibido...
            if int(character) == 0:
                continue
            else:
                units_number_list.append(str(character))
        else:
            # Reviso si el primer digito es un cero
            if int(character) == 0:
                continue
            else:
                number_unit = int(character)*(10**n_characters)
                units_number_list.append(str(number_unit))
            
            
    # Ahora que tengo la lista con las unidades que componen dicho numero, genero el string que 
    # retornar la función
    expanded_form_str = " + ".join(units_number_list)
    return expanded_form_str


if __name__ == "__main__":
    
    n_proof = 412356
    expanded_form_str = expandedForm(n_proof)
    print(expanded_form_str)