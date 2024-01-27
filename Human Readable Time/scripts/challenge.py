"""
DESCRIPTION:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

def set_strftime(input_seconds):
    
    """Función encargada de procesar un valor de segundos recibido como parámetro, y retornar una cadena 
       que representa dicho tiempo en formato de HH-MM-SS.
    
    Keyword arguments:
        - input_seconds -- Tiempo a transformar, expresado en segundos.
    Return: 
        - strftime_string -- Cadena de texto que representa el tiempo indicado en el parámetro recibido, pero 
                             con el formato esperado.
    """
    
    # Compruebo que el input recibido por la función es un entero
    if isinstance(input_seconds, str):
        
        return "No es posible convertir el argumento de la función a formato HH-MM-SS. Prueba con un argumento numérico."
    
    if isinstance(input_seconds, float):
        
        input_seconds = int(round(input_seconds))
        
    if input_seconds > 359999:
        return "El valor recibido como parámetro es demasiado grande para la transformacion. Por favor, prueba asignando un valor más pequeño al parámetro."
    
    
    # Voy a tratar de hacer el challenge sin tener que usar librerias de python como time.
    HOUR = 3600 # 1 HOUR ==> 3600 SEC
    MIN = 60 # 1 MIN ==> 60 SEC
    
    
    
    hours_in_parameter = input_seconds//HOUR if input_seconds//HOUR != 0 else '00'  # Obtengo el número de horas transcurridas en los segundos expresados.
    rest_time_after_hours = input_seconds%HOUR                                      # Obtengo el tiempo restante tras restar las horas convertidas.
    
    
    mins_in_parameter = rest_time_after_hours//MIN  if rest_time_after_hours//MIN != 0 else '00'    # Obtengo el número de minutos transcurridas en los segundos restantes.
    rest_time_after_mins = rest_time_after_hours%MIN if rest_time_after_hours%MIN != 0 else '00'    # Obtengo el tiempo restante tras restar las horas y minutos convertidos.
                                                                                                    # rest_time_after_min == secs.
                                                                                                
    
    if hours_in_parameter != '00':                                                                                           
        hours_in_parameter = hours_in_parameter if hours_in_parameter >= 10 else f'0{hours_in_parameter}'
        
    if mins_in_parameter != '00':
        mins_in_parameter = mins_in_parameter if mins_in_parameter >= 10 else f'0{mins_in_parameter}'
        
    if rest_time_after_mins != '00':
        rest_time_after_mins = rest_time_after_mins if rest_time_after_mins >= 10 else f'0{rest_time_after_mins}'
        
        
    strftime_string = f"{hours_in_parameter}:{mins_in_parameter}:{rest_time_after_mins}"
    
    return strftime_string
    
    
if __name__ == "__main__":
    
    example = 359999
    strftime_string = set_strftime(example)
    print(strftime_string)