"""
DESCRIPTION:

Create a Vector object that supports addition, subtraction, dot products, and norms. 
So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception

If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above,
a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal

Note: the test cases will utilize the user-provided equals method.
"""

from math import sqrt
class Vector():
    
    """Clase que trata de representar un Vector matemático.
       La clase implementa una serie de métodos que le permiten llevar a cabo operaciones aritméticas simples,
       como suma, resto, producto punto, ...
    """
    
    def __init__(self, contenido):
        self.contenido = contenido
        
        
    def add(self, sumand_vector):
        
        assert len(self.contenido) == len(sumand_vector.contenido)
        sum_result = [n + sumand_vector.contenido[i] for i, n in enumerate(self.contenido)] 
        return Vector(sum_result)
    
    def subtract(self, sumand_vector):
        
        assert len(self.contenido) == len(sumand_vector.contenido)
        subtract_result = [n - sumand_vector.contenido[i] for i, n in enumerate(self.contenido)] 
        return Vector(subtract_result)
    
    def dot(self, sumand_vector):
        
        assert len(self.contenido) == len(sumand_vector.contenido)
        dot_result = sum([n * sumand_vector.contenido[i] for i, n in enumerate(self.contenido)])
        return dot_result
    
    def norm(self):
        
        norm_result = sqrt(sum([n**2 for n in self.contenido])) 
        return norm_result
    
        
    def equals(self, vector):
        
        if self.contenido == vector.contenido:
            return True
        else:
            return False
        
        
    def __str__(self):
        tuple_return = tuple(self.contenido)
        return f"{tuple_return}".replace(" ", "")
    

if __name__ == "__main__":
    
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    c = Vector([5, 6, 7, 8])
    a.dot(b)
    
    a = Vector([1, 2])
    b = Vector([3, 4])
        
    a.add(b).equals(Vector([4, 6]))
