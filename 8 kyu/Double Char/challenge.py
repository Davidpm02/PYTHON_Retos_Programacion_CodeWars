"""
DESCRIPTION:

Description:

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

"""

def double_char(s):
    
    """
    Summary:
        Función encargada de retornar una cadena de texto
        dada otra cadena original, donde cada carácter esté
        duplicado.
    Args:
        s (str)
    Returns:
        repeated_s (str)
    """
    
    return "".join([char*2 for char in s])