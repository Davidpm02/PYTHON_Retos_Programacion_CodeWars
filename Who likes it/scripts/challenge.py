"""
DESCRIPTION:

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""


def process_people_array(people_array):
    
    """Función auxiliar que procesa un array de nombres de personas, y retorna, una cadena correspondiente a
       la solución para el ejemplo recibido como parámetro.

    Keyword arguments:
        - people_array -- Array con los nombres de las personas que han dado like a la publicación de la red
                          social.
    Return: 
        - result_str -- Cadena con el resultado acorde a las posibles soluciones indicadas.
    """
    
    n_people = len(people_array)
    
    if n_people == 0:
        result_str = "no one likes this"
        return result_str

    elif n_people == 1:
        result_str = f"{people_array[0]} likes this"
        return result_str
    
    elif n_people == 2:
        result_str = f"{people_array[0]} and {people_array[-1]} like this"
        return result_str
    
    elif n_people == 3:
        result_str = f"{people_array[0]}, {people_array[1]} and {people_array[-1]} like this"
        return result_str
    
    elif n_people > 3:
        if n_people == 4:
            result_str = f"{people_array[0]}, {people_array[1]} and 2 others like this"
            return result_str
        else:
            n_people_minus_firsts = n_people - 2
            result_str = f"{people_array[0]}, {people_array[1]} and {n_people_minus_firsts} others like this"
            return result_str
        


if __name__ == "__main__":
    
    example_array = [[],
                     ["Peter"],
                     ["Jacob", "Alex"],
                     ["Max", "John", "Mark"],
                     ["Alex", "Jacob", "Mark", "Max"]]
    
    for _ in example_array:
        result = process_people_array(_)
        print(result)