"""
DESCRIPTION:

The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"

"""

def get_planet_name(id):
    
    """
    Summary:
        Función parametrizada encargada de obtener el nombre
        de un planeta del Sistema Solar dado un entero.
        
        Para retornar un valor, la función se basa en el orden
        de los planetas, basándose en la cercanía de estos al
        Sol.
    Args:
        id (int) -- Número correspondiente al planeta que se 
        desea obtener.
    Returns:
        planet_name (str)
    """
    
    ids_array = [_ for _ in range(1, 9)]
    planets_array = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets_dict = dict(zip(ids_array, planets_array))
    
    return planets_dict[id]