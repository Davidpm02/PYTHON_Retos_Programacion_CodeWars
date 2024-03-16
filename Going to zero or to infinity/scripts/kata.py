"""
DESCRIPTION:

Consider the following numbers (where n! is factorial(n)):

u1 = (1 / 1!) * (1!)
u2 = (1 / 2!) * (1! + 2!)
u3 = (1 / 3!) * (1! + 2! + 3!)
...
un = (1 / n!) * (1! + 2! + 3! + ... + n!)
Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?

Are these numbers going to 0 because of 1/n! or to infinity due to the sum of factorials or to another number?

### TASK ###

Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n, where n is an integer greater or equal to 1.
Your result should be within 10^-6 of the expected one.

### REMARK ###

Keep in mind that factorials grow rather rapidly, and you need to handle large inputs.

### HINT  ###

You could try to simplify the expression.
"""

def going(n):
    
    """Función parametrizada encargada de devolver un resultado acorde.
       En esencia, la función lleva a cabo el cálculo de un producto entre
       dos términos:
       (1 / n!)
       (1! + 2! + 3! + ... n!)
       
    
    Keyword arguments:
        n -- Parámetro que proporniona el límite del cálculo para el resultado.
    Return: 
        result -- Resultado del producto entre los dos miembros indicados anteriormente.
    """
    
    def factorial(n):
        
        """Función parametrizada que facilita el calculo del factorial de un número,
           permitiendo reducir la cantidad de operaciones que se llevan a cabo en el
           ámbito local de la función principal.
        
        Keyword arguments:
            n -- Entero para el que se quiere calcular el factorial.
        Return: 
            factorial_n -- Resultado del cálculo del factorial
        """
        
        factorial_actual = 1
        suma_factoriales = 0
        for i in range(1, n + 1):
            factorial_actual *= i  # Calculo iterativo del factorial
            suma_factoriales += factorial_actual
            
        return factorial_actual, suma_factoriales
    

    # El resultado de la función se calcula a partir del producto entre dos 
    # términos principales
    
    factorial_actual, suma_factoriales = factorial(n)

    # Retorno el resultado al ámbito global del programa
    result = suma_factoriales / factorial_actual
    return round(result, 6)



if __name__ == '__main__':

    n = 7
    result = going(n)
    print(result)



"""
@test.describe("Testing...")
def _():
    @test.it("Fixed tests")
    def _():
        test.assert_approx_equals(going(5), 1.275, 1e-6)
        test.assert_approx_equals(going(6), 1.2125, 1e-6)
        test.assert_approx_equals(going(7), 1.173214, 1e-6)
"""