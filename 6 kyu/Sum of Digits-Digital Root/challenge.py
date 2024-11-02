"""
DESCRIPTION:

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n.
If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def recursive_sum(more2digits_value):
    
    """Función auxiliar que me permite llevar a cabo la suma recursiva del valor recibido como parámetro.
    
    Keyword arguments:
        - more2digits_value -- Valor a utilizar para llevar a cabo la suma recursiva.
    Return: 
        - recursive_sum -- Resultado de llevar a cabo la suma recursiva de los números que componen el valor de
                           'more2digits_value'.
    """

    recursive_sum = 0  # Valor inicial de la suma:
    for _ in str(more2digits_value):
        recursive_sum += int(_)
    return recursive_sum


def digital_root(input_value):
    
    """Función encargada de procesar un input numérico recibido para realizar una suma recursiva de todos
       los números que conforman dicho valor.
    
    Keyword arguments:
        - input_value -- Valor entero a utilizar para llevar a cabo la suma recursiva.
    Return: 
        - recursive_sum -- Entero que representa la suma recursiva de todos los números que conforman el valor
                           de 'input_value'.
    """
    
    # Me aseguro de que el valor recibido es un número
    if isinstance(input_value, str):
        return "No es posible realizar una suma recursiva con el valor proporcionado."
    
    
    if isinstance(input_value, float):
        input_value = int(round(input_value))
        
   
    previous_value = input_value  # Esta variable se actualiza iterativamente
    while previous_value >= 10: 
        recursive_sum_result = recursive_sum(previous_value)
        previous_value = recursive_sum_result
        continue
        
    return previous_value



if __name__ == '__main__':
    
    example_value = 493193
    recursive_sum_result = digital_root(example_value)
    print(recursive_sum_result)
    
    
    


