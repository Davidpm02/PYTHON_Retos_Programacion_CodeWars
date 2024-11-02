"""
DESCRIPTION:

You will be given an array of numbers. 
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sorting_odds(number_array):
    
    """Función que recibe un array de números enteros.
       La función verifica que todos los elementos que componen el array son enteros. En caso de que alguno
       de los elementos sea flotante, la función lo convierte a entero.
       Finalmente, la función procesa la lista y devuelve un nuevo array donde cada entero impar se ha colocado
       de manera ordenada.
    
    Keyword arguments:
        - number_array -- Array de enteros que utilizará la función para revisar si tiene elementos impares, y, en
                          dicho caso, se procesa para devolver un nuevo array con los elementos impares ordenados.
    Return: 
        - ordered_array -- Array resultante tras aplicar el proceso de ordenación de los elementos (si aplica).
    """
    
    # Let's be sure that elements of array are all integer
    for _ in number_array:
        if isinstance(_, str):
            return "El array recibido contiene caracteres no válidos ({}).".format(_)
        elif isinstance(_, float):
            number_array[_] = int(round(_))
    
    
    odds_numbers = []
    for number in number_array:
        if number%2 != 0:
            odds_numbers.append(number)
    else:
        # Sorting the 'odds_numbers' array
        odds_numbers.sort()
            
    # Sorting the 'number_array' parameter        
    index_odds_iterated = 0
    for index, number in enumerate(number_array):
        if number%2 != 0:
            number_array[index] = odds_numbers[index_odds_iterated]
            index_odds_iterated +=1
            

    return number_array


if __name__ == "__main__":
    
    example_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    example_array__ordered = sorting_odds(example_array)
    
    print(example_array__ordered)
        