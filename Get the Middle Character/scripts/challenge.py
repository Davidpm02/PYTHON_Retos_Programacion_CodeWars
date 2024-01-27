"""
DESCRIPTION:

You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"



#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases).
You do not need to test for this.
This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
"""

def getMiddle(string):
    
    """Función encargada de recibir una cadena de caracteres, y devolver, en forma de cadena, el caracter que
       se situe en el centro de la misma.
    
    Keyword arguments:
        - string -- Cadena de caracteres de la que queremos obtener su caracter situado en el medio.
    Return: 
        - middle_on__caracter -- Caracter en forma de cadena que se encuentra en el centro de la cadena recibida
                                 como parámetro de la función.
                            
    """
    
    
    # Defino una serie de posibilidades:
    # El input recibido contiene 1 solo caracter. En este caso, middle_on__caracter = string
    # El input recibido tiene 2 caracteres. Ocurre lo mismo que en el caso anterior.
    # El input recibido tiene 3 caracteres. En este caso, middle_on__caracter = string[1]
    # El input recibido tiene 4 caracteres. En este caso, middle_on__caracter = string[1:2]
    # El input recibido tiene 5 caracteres. En este caso, middle_on__caracter = string[2]
    
    # Podemos ver que siempre vamos a buscar el caracter central en base a lo longitud total de la cadena.
    # Voy a definir una serie de posibilidades
    n_characters = len(string)
    
    if n_characters == 1:
        middle_on__character = string
    elif n_characters == 2:
        middle_on__character = string
    elif n_characters == 3:
        middle_on__character = string[1]
    elif n_characters == 4:
        middle_on__character = string[1:3]
    elif n_characters == 5: 
        middle_on__character = string[2]
    else:
        
        if n_characters%2 == 0: # n_characters == ODD
            max_index = n_characters - 1
            back_steps = n_characters//2 # INT division
            starting_count_index = max_index - back_steps # Indice desde el que comienza el centro.
            ending_count_index = starting_count_index + 2
            
            middle_on__character = string[starting_count_index:ending_count_index]
        
        elif n_characters%2 == 1:
            max_index = n_characters - 1
            back_steps = n_characters//2
            
            middle_on__character = string[back_steps]
            
            
    return middle_on__character




if __name__ == "__main__":
    
    string = "test"
    middle_on__character = getMiddle(string)
    print(middle_on__character)