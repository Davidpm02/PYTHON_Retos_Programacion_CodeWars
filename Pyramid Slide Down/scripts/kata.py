"""
DESCRIPTION:

Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense.
If you have a computer, you can mess with pyramids even if you are not in Egypt at the time.
For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as an argument and returns its largest 'slide down'. For example:

* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
By the way...
My tests include some extraordinarily high pyramids so as you can guess,
brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of Problem 18 and/or Problem 67 on ProjectEuler.
"""

def longest_slide_down(pyramid):
    
    """Función parametrizada encargada de procesar un parámetro de entrada, y calcular la suma máxima de entre todos los pisos
       de la piramide que conforma el parámetro.
    
    Keyword arguments:
    pyramid -- lista de listas que representa la estructura de una pirámide. Cada lista dentro de la lista padre podría verse como un
               piso de la pirámide en cuestión.
    Return: 
    slide_down_sum -- Entero con la suma máxima que se obtiene al escoger los valores apropiados de cada uno de los pisos de la pirámide.
    """
    
    """
      /3/
     \7\ 4 
    2 \4\ 6 
   8 5 \9\ 3
    """
    
    # Es importante tener en cuenta dos suposiciones clave:
    # - Al escoger un número, el siguiente debe ser posible en vista del número escogido en el piso anterior.
    # - Siempre se debería coger el número más grande posible del siguiente piso, que sea posible en cuanto al número escogido del 
    #   piso actual.
    
    sum_results = [] #  Lista con los resultados de las diferentes busquedas efectuadas.
    
    n_iteraciones = 0
    first_index_choice = None
    while len(sum_results) < 4:
        choices = []
        index_last_choice = None
        n_iteraciones += 1
        
        if n_iteraciones % 2 != 0:
        
            # Incluyo el número de la cúspide en la lista de números escogidos
            choices.append(pyramid[0][0])
            for floor in pyramid[1:]:   #  Itero sobre cada lista contenida en el parámetro
                
                if len(sum_results) == 1:
                    if index_last_choice is None:
                        max_num = floor[-1]
                        index_last_choice = floor.index(max_num)
                        #first_index_choice = floor.index(max_num)
                        
                        choices.append(max_num)
                        continue
                
                if index_last_choice is None:
                    max_num = max(floor)
                    index_last_choice = floor.index(max_num)
                    #first_index_choice = floor.index(max_num)
                    
                    # Actualizo los resultados tras procesar el piso actual
                    choices.append(max_num)
                else:
                    max_num = max([floor[index_last_choice], floor[index_last_choice + 1]])
                    index_last_choice = max([i for i, e in enumerate(floor) if e == max_num])
                    first_index_choice = floor.index(max_num)
                    # Actualizo los resultados tras procesar el piso actual
                    choices.append(max_num)
                
                print(max_num, index_last_choice)
        
        elif n_iteraciones % 2 == 0:
            
            # Incluyo el número de la cúspide en la lista de números escogidos
            choices.append(pyramid[0][0])
            for index_pyramid, floor in enumerate(pyramid[1:]):   #  Itero sobre cada lista contenida en el parámetro
                      
                if index_last_choice is None:
                    max_num = floor[-1]
                    index_last_choice = floor.index(max_num)
                    
                    # Actualizo los resultados tras procesar el piso actual
                    choices.append(max_num)
                else:
                    
                    if index_pyramid == 2:
                        max_num = min([floor[index_last_choice], floor[index_last_choice + 1]])
                        index_last_choice = max([i for i, e in enumerate(floor) if e == max_num])
                        
                        # Actualizo los resultados tras procesar el piso actual
                        choices.append(max_num)
                        
                    else:
                    
                        max_num = max([floor[index_last_choice], floor[index_last_choice + 1]])
                        index_last_choice = max([i for i, e in enumerate(floor) if e == max_num])
                        
                        # Actualizo los resultados tras procesar el piso actual
                        choices.append(max_num)
                
                print(max_num, index_last_choice)
            
            
        # Cuando termino de iterar, sumo todos los números escogidos
        slide_down_sum = sum(choices)
        print(slide_down_sum)
        sum_results.append(slide_down_sum)        
        
    return max(sum_results)


if __name__ == "__main__":
    
    pyramid = [
                                    [75],
                                  [95, 64],
                                [17, 47, 82],
                              [18, 35, 87, 10],
                            [20,  4, 82, 47, 65],
                          [19,  1, 23, 75,  3, 34],
                        [88,  2, 77, 73,  7, 63, 67],
                      [99, 65,  4, 28,  6, 16, 70, 92],
                    [41, 41, 26, 56, 83, 40, 80, 70, 33],
                  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
          [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]
    slide_down_sum = longest_slide_down(pyramid=pyramid)
    print(slide_down_sum)