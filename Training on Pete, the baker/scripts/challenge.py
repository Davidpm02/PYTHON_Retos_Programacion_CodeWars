"""
Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), 
which takes the recipe (object) and the available ingredients (also an object) 
and returns the maximum number of cakes Pete can bake (integer). 

For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})


"""

def cakes(recipe, available_ingredients):
    
    """Función que se encarga de procesar dos secuencias recibidas como parámetros, y retornar una salida de acuerdo
       al contenido de estas.
    
    Keyword arguments:
    recipe -- Hashmap que indica los ingredientes y cantidades que Pete necesita para cada uno para llevar a cabo
              la receta de una (1) unidad del postre que desea preparar.
    available_ingredients -- Diccionario que muestra el contenido de "materia prima" o ingredientes de los que Pete
              dispone para llevar a cabo la receta.

    Es posible que, de acuerdo a la cantidad de ingredientes de los que Pete dispone, y aquellos que demande una determinada 
    receta, el pastelero se anime y acabe cocinando más de la cuenta.
    
    Return: 
    cooked_cakes -- Entero que indica la cantidad de pasteles que Pete ha cocinado con los ingredientes de los que disponía.
    """
    
    # We need to make sure that, at least, we have the minimum ingredients.
    
    for key in recipe.keys():
        if key not in available_ingredients:
            cooked_cakes = 0
            return cooked_cakes
    
    # I start definning a copy of available_ingredients hashmap
    #spent_ingredients = available_ingredients.copy()
    
    cooked_cakes = 0
    while True:
        for ingredient, amount in recipe.items():
            
            # If Pete does not have the minimun required amount...
            if available_ingredients[ingredient] < amount:
                return cooked_cakes
            
            # Available amount - required amount
            available_ingredients[ingredient] -= amount
        cooked_cakes += 1
        
        
        
if __name__ == "__main__":
    
    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    example_result = cakes(recipe, available)
    
    print(example_result)