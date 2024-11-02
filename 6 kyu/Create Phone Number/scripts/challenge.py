"""
INTRODUCTION

Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

"""

# IMPORTS 
import re


def create_shape_number_array(input_array):
    
    """Función encargada de procesar un array recibido como parámetro, y crear a partir de él un nuevo array
       que defina la estructura de la cadena de texto que componga un número de teléfono
       (no real, simplemente, con la estructura indicada).
    
    Keyword arguments:
        - input_array -- Array con los números a utilizar para generar el string que represente el número
                         de teléfono creado.
    Return: 
        - phone_shape_array -- Array cuyo orden de elementos representa la estructura final
                               de la cadena creada que conforma el número de teléfono.
    """
    
    if len(input_array) != 10:
        return "La lista recibida como parámetro no cumple las condiciones para generar un número de teléfono."
    
    valid_values_counter = 0  # Contador de elementos validos dentro de la lista recibida
    valid_values_array = list(range(0, 10))
    for _ in input_array:
        if _ in valid_values_array:
            valid_values_counter += 1
    
    if valid_values_counter == 10:
        phone_shape_array = []
        for index, _ in enumerate(input_array):
            if index == 0:
                phone_shape_array.append("(")
                phone_shape_array.append(str(_))
            elif index == 2:
                phone_shape_array.append(str(_))
                phone_shape_array.append(")")
                phone_shape_array.append(" ")
            elif index == 5:
                phone_shape_array.append(str(_))
                phone_shape_array.append("-")
            else:
                phone_shape_array.append(str(_))
                
        return phone_shape_array

    else:
        print("El array recibido no cumple con las condiciones necesarias para poder formar un número de teléfono válido.")
        return None


def create_phone_number(phone_shape_array):
    
    """Función encargada de procesar un array recibido como parámetro con la estructura que debe mantener
       la cadena con el número de teléfono generada finalmente.
    
    Keyword arguments:
        - phone_shape_array -- Array cuyo orden de elementos representa la estructura final
                               de la cadena creada que conforma el número de teléfono.
    Return: 
        - phone_number -- Cadena con el teléfono creado a partir de los elementos que componian el argumento
                          recibido por la función
    """
    
    phone_number = "".join(phone_shape_array)
    required_phone_shape = r'^\(\d{3}\) \d{3}-\d{4}$'  # REGEX con la estructura que debe tener cada cadena generada.
    try:
        if re.match(required_phone_shape, phone_number):
            return phone_number
        else:
            raise Exception
    except Exception:
        print("La cadena creada no contiene la estructura de teléfono esperada ==> {} .".format(phone_number))
        return None



if __name__ == "__main__":
    
    random_values = list(range(0,10))
    phone_shape_array = create_shape_number_array(random_values)
    phone_number = create_phone_number(phone_shape_array)
    
    if phone_number == None:
        print("No se ha podido generar un número de teléfono con el array proporcionado.")
    else:
        print(phone_number)
    