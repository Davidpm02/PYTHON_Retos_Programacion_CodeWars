import sys
import os

# Agrego el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scripts.challenge as challenge






## Este archivo ira dedicado a realizar pruebas contra las funciones definidas en el archivo challenge.py

def test_make_reversed_list():
    
    # Esta función espera un string, por lo que voy a asegurarme de enviar varios strings
    
    array_strs = ["prueba", "hola", "probando123", "3", "esto_es_un_test", 532]
    for _ in array_strs:
        try:
            reversed_list = challenge.make_reversed_list(_)
            assert reversed_list  # En caso de que la variable sea == None, habrá ocurrido un error.
            print(f"{_} => {reversed_list}")
            
        except:
            print("El test ha fallado.")
        
        
def test_build_a_result():
    
    array_lsts = [["h","o","l","a","s","i"],
                  ["h","r","w","s","c","1"],
                  ["e","o","l","6","s","2"],
                  ["s","3","9","a","s","3"],
                  ["8","o","l","a","4","i"]]
    for _ in array_lsts:
        try:
            result = challenge.build_a_result(_)
            assert result 
            print(f"{_} => {result}")
        except:
            print("El test ha fallado.")

