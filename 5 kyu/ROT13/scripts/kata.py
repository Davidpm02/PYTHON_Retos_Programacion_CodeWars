"""
DESCRIPTION:

How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""

def rot13(input_text):
    
    """Función parametrizada que se encarga de, tras haber recibido una entrada
       de una cadena de texto, procesarla y convertirla en una nueva cadena de texto,
       generada tras aplicar un cifrado césar conocido como 'ROT13'.
       
       El cifrado ROT13 consiste en la sustitución de caracteres de una cadena,
       por aquellos que se encuentran 13 registros por delante en el abecedario.
       
       Para el desarrollo de este Kata, voy a asimilar un abecedario en Inglés.
    """
    
    
    def turnToUppercase(input_text, output_text):
        
        """Función parametrizada que se encarga de procesar la cadena de salida generada para poder devolver los caracteres
           a su tamaño correspondiente (mayúscula)
        
        Keyword arguments:
            input_text -- cadena proporcionada como entrada.
            output_text -- cadena generada como salida tras aplicar la codificación ROT13
        Return: 
            output_text__processed -- cadena genera como salida, ahora correctamente procesada
        """
        
        input_text__list = [character for character in input_text]
        output_text__list = [character for character in output_text]
        
        # proceso la lista "output_text__list"
        output_text__processed = "".join([character.upper() if input_text__list[i].isupper() else character for i, character in enumerate(output_text__list)])
        return output_text__processed
    
    
    
    # Defino una lista que contenga el abecedario en ingles
    abc_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abc_list_rot13  = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

        
    # Diccionario que mapea cada par de letras
    dict_rot13 = {}
    zipped_list = zip(abc_list, abc_list_rot13)
    for letter_pair in zipped_list:
        dict_rot13[letter_pair[0]] = letter_pair[1]
        
    # Proceso el input recibido en la entrada
    output_text = "".join([dict_rot13[character.lower()] if character.lower() in dict_rot13.keys() else character for character in input_text])
    print(output_text)
    output_text = turnToUppercase(input_text = input_text, 
                                  output_text = output_text)
    return output_text
    
    
if __name__ == "__main__":
    
    input_text = "HOla!"
    output_text = rot13(input_text= input_text)
    
    print(output_text)