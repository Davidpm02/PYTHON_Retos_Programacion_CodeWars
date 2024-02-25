"""
Given a list of integers and a single sum value,
return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum,
the pair whose second element has the smallest index is the solution.

EXAMPLES ----

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]
"""

def get_summands(numbers_array, result_sum):
    
    """
    Función parametrizada que se encarga de procesar un array recibido como parámetro, y retornar un nuevo array
    con los enteros que se incluyen en dicho parámetro que, sumados, dan como resultado el valor del segundo 
    parametro.
    
    Keyword arguments:
    
    number_array -- Array de enteros.
    result_sum --  Valor entero que utiliza la función para retornar el resultado.
    Return:
    
    summands_array -- Array con los enteros del primer parámetro que, sumados, dan como resultado el valor del segundo
                      parámetros. 
    """
    if result_sum in numbers_array:
        numbers_array.remove(result_sum)
    
    
    solutions = []
    index_sols = []
    # Let's iterate over numbers_array to get a the first possible sum
    for index, number in enumerate(numbers_array):  # [1,2,3,4,5,5,6]       10
        for num in numbers_array:
            if numbers_array[index] == num:
                continue
            result = number + num
            if result == result_sum:
                sol = [number, num]
                solutions.append(sol)
                index_sol = [numbers_array.index(sol[0]), numbers_array.index(sol[-1])]
                index_sols.append(index_sol)
                
    # Returning the solution
    if len(solutions) == 1:
        summands_array = solutions[0]
        return summands_array
    elif len(solutions) > 1:
        second_elements_array = []
        for index, item in enumerate(index_sols):    # [1, 3] [2, 2]  
            second_elements_array.append(item[-1])
            
        # Getting the index-array of the lower second element
        lower_value_index = 0
        starter_value = 0
        for index, value in enumerate(second_elements_array):
            if value > starter_value:
                starter_value = value
                lower_value_index = index
          
        # Getting the index of array
        index_array = solutions[lower_value_index]
        return index_array

if __name__ == "__main__":
    
    numbers_array = [4, 3, 2, 3, 4]
    result_sum = 6
    summands_array_example = get_summands(numbers_array= numbers_array,
                                          result_sum= result_sum)  

    print(summands_array_example)