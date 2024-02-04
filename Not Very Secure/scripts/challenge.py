"""
DESCRIPTION:

In this example you have to validate if a user input string is alphanumeric. 
The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""

def validating_string(string):
    
    """Función parametrizada encargada de verificar que la cadena de texto recibida esté compuesta por caracteres
       alfanuméricos, de forma que cumpla las condiciones dictadas en el enunciado del ejercicio.
    
        Keyword arguments:
            string -- Cadena de texto que se quiere validar.
        Return: 
            Boolean -- La función entrega True o False en función del resultado obtenido tras el procesamiento de
                       la cadena.
    """
    
    # Compruebo que la cadena no contenga ningún caracter ' ':
    if ' ' in string:
        return False
    
    # Compruebo que la cadena tenga al menos un caracter:
    if len(string) == 0:
        return False
    
    # La validación anterior se podría resumir en:
    #if ' ' in string or len(string) == 0:
       # return False
    
    
    # Compruebo que los caracteres de la cadena sean alfanumericos:
    if string.isalnum():
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    
    example_string = "helloworld"
    result = validating_string(example_string)
    print(result)