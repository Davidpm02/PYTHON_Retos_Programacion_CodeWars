"""
DESCRIPTION:

We want to generate all the numbers of three digits where:

the sum of their digits is equal to 10
their digits are in increasing order (the numbers may have two or more equal contiguous digits)
The numbers that fulfill these constraints are: [118, 127, 136, 145, 226, 235, 244, 334].
There're 8 numbers in total with 118 being the lowest and 334 being the greatest.

### Task

Implement a function which receives two arguments:

* the sum of digits (sum)
* the number of digits (count)

This function should return three values:

* the total number of values which have count digits that add up to sum and are in increasing order
* the lowest such value
* the greatest such value

Note: if there're no values which satisfy these constaints,
you should return an empty value (refer to the examples to see what exactly is expected).

### Examples

find_all(10, 3)  =>  [8, 118, 334]
find_all(27, 3)  =>  [1, 999, 999]
find_all(84, 4)  =>  []

### Features of the random tests:

* Number of tests: 112
* Sum of digits value between 20 and 65
* Amount of digits between 2 and 17
"""
import numpy as np

def find_all(sum_, count):
    
    """
       Summary:
           Función parametrizada que se encarga de devolver un array de 3 elementos:
              - Indice 0 ==> representa el número de coincidencias encontradas para los argumentos recibidos.
              - Indice 1 ==> contiene el valor mínimo encontrado de entre todas las coincidencias.
              - Indice 2 ==> contiene el valor máximo encontrado de entre todas las coincidencias.
           La función procesa los números argumentos de entrada, y se encarga de encontrar todos los números
           de "count" dígitos, cuya suma entre los dígitos que la componen, de un valor de "sum".  
           
       Args:
           - sum ==> Entero que simboliza el valor que debemos obtener al sumar los dígitos de cada número 
                     encontrado.
           - count ==> Entero que representa el número de dígitos que deben componer cada uno de los resultados
                     encontrados.
       Returns:
           - array_result ==> Array de 3 elementos, los cuales son explicados en el docstring de la función.
    """
    
    def getValidNum(num):
        
        """
        Summary:
            Función auxiliar parametrizada que se encarga de validar el número recibido 
            como argumento en su invocación.
        
        Args:
            - num (int): Número que se desea validar.
        
        Returns:
            bool: True si el número es válido, Falso en caso contrario.
        """
    
        array_of_digits = np.array([int(n) for n in str(num)])
        
        # Valido el parámetro
        max_value = 0
        
        for index, n in enumerate(array_of_digits):
            if index == 0:
                max_value = n
            else:
                if n >= max_value:
                    max_value = n
                else:
                    return False
        return True
    
    
    
    # Comienzo generando una lista con todos los enteros que contienen "count" cantidad de dígitos
    exp = count + 1
    count_digits_array = np.asarray([num for num in range(int(10**exp)) if len(str(num)) == count])
    
    
    ## Proceso para buscar las coincidencias
    # Defino un array que contendrá todos los numeros de "count" dígitos, cuya suma entre ellos sea igual a "sum".
    nums_count_found_array = np.asarray([num for num in count_digits_array if sum([int(sub_num) for sub_num in str(num)]) == sum_])
    
    # Verifico que el array contenga, al menos, un resultado
    if len(nums_count_found_array) == 0:
        return []
    
    # Aplico la restricción de que ningún dígito de un número dado sea menor que el anterior a este.
    nums_count_array = np.asarray([num for num in nums_count_found_array if getValidNum(num) == True])
    
    ## Proceso para generar el array final
    result_array = [len(nums_count_array), min(nums_count_array), max(nums_count_array)]
    
    # Retorno el array como resultado de la función
    return result_array
    
          
if __name__ == "__main__":
    
    result_array = find_all(10, 3)
    print(result_array)
    