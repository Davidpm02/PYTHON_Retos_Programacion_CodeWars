"""
INTRODUCTION:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

# Vamos a tener en cuenta que podriamos recibir, puesto que no parece aparecer ningún límite superior indicado
# en la instroducción, que los numeros posibles a recibir como parámetro pertenecen al conjunto de números reales.

# Teniendo esto en cuenta, escribo la función encargada de calcular la suma de todos los múltiplos de 3 y de 5
# del número recibido por la función.

def getSumMultiples(value):
    
    """Función parametrizada que se encarga de procesar la suma de números inferiores al número recibido
       como parámetros, cuyos valores sean múltiplos de 3 y 5.
    
    Keyword arguments:
        - value -- Entero en el que se basa la función para poder obtener la suma de múltiplos de 3 y 5, inferiores
                   a él.
    Return: 
        - sumMultiple -- Suma de los múltiplos de 3 y 5 de los números inferiores al argumento recibido en la invocación
                         de la función. 
                         El valor retornado es 0 siempre 'value' sea igual o inferior a 0.
    """
    
    # Primero de todo, me aseguro de que el input recibido sea un número:
    if not isinstance(value, int):
        return "No es posible obtener la suma de múltiples de 3 y 5 inferiores al parámetro proporcionado."
    
    
    
    # Retorno 0 si el valor recibido es negativo 0
    if value < 0 or value == 0:
        return 0
    
    # Defino un contador, que representará la suma total de múltiplos encontrados:
    sum_value = 0
    init_value = value
    
    # Itero sobre cada uno de los valores inferiores al valor recibido como parámetro, en busca de múltiplos de 3 y 5.
    while value > 0:
        if value == init_value:
            value -=1
            continue
        
        if value%3 == 0 or value%5 == 0:
            sum_value +=value
            value -= 1
            continue
        else:
            value -=1
            continue
        
        
    return sum_value


if __name__ == "__main__":
    
    value = 10
    sumMultiple = getSumMultiples(value)
    print(sumMultiple)