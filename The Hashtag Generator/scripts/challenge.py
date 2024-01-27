"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.


" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

def turnToHashtag(string):
    
    """Función parametrizada que se encarga de procesar una cadena de entrada y devolver una nueva cadena, que
       conforma un hashtag en función del contenido de la cadena recibida como parámetro.
    
    Keyword arguments:
        - string -- Cadena de caracteres a convertir en Hashtag.
    Return: 
        - final_hashtag -- Cadena generada por la función, que conforma el Hashtag generado partir del parámetro
                           recibido.
                           El valor de final_hashtag es False si la longitud del parámetro 'string' es igual a 0,
                           o superior a  140.
    """
    
    # Me aseguro de que el valor introducido sea una cadena
    if not isinstance(string, str):
        return "No es posible generar un Hashtag con el valor proporcionado."

    if len(string) == 0:
        return False


    # Elimino los espacios iniciales y finales que pudiese tener la cadena
    without_spaces = string.strip()
    elements_string_array = without_spaces.split(" ")
    
    # Inicializo un array, cuyo primer elemento es una cadena que contiene el caracter '#'.
    final_hashtag_content = ["#"]
    
    for element_string in elements_string_array:
        capitalized_element_string = element_string.title()
        final_hashtag_content.append(capitalized_element_string)
        
    final_hashtag = "".join(final_hashtag_content)
    
    if len(final_hashtag) > 140:
        return False
    return final_hashtag
        
    
    
if __name__ == "__main__":
    string = " Hello there thanks for trying my Kata"
    final_hashtag = turnToHashtag(string)
    print(final_hashtag)