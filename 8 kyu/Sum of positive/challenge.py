"""
DESCRIPTION:

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    
    """
    Summary:
        Función auxiliar encargada de procesar un array
        de enteros y retornar la suma de todos los
        elementos positivos del array.
    Args:
        arr (List[int]) -- Array de enteros a procesar.
    Returns:
        result_sum (int)
    """
    
    result_sum = 0
    for num in arr:
        if (num > 0):
            result_sum += num
    return result_sum
