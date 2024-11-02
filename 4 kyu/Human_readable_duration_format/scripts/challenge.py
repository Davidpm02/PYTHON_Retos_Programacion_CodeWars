"""
DESCRIPTION:    Human readable duration format

Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer.
If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
    
    
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

--------------------- Detailed rules -------------------
The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated by a space.
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", ").
Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times.
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero.
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible".
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid 
more significant unit of time.

"""

def format_duration(seconds):
    
    """Función parametrizada encargada de procesar el parámetro "seconds", y generar un string con la salida
       apropiada para el valor contenido en el parámetro.
       
       Este parámetro almacena un valor que representa cierta cantidad de tiempo, expresada en segundos. Sin
       embargo, no es facil representar la cantidad de tiempo transcurrido cuando este parámetro almacena un
       valor demasiado grande.
       La función actual se encarga de esto, generando un string como respuesta, que facilita la tarea de 
       representar la cantidad de tiempo transcurrido.
    
    Keyword arguments:
       seconds -- entero cuyo valor representa una cantidad de tiempo transcurrido.
    Return: 
       readable_string -- cadena generada tras procesar el parámetro "seconds".
    
    """
    
    # Defino como constantes la cantidad de segundos que representa una determinada cantidad de tiempo
    YEAR_SECS = 31536000
    DAY_SECS = 86400
    HOUR_SECS = 3600
    MINUTE_SECS = 60
    time_list = [YEAR_SECS, DAY_SECS, HOUR_SECS, MINUTE_SECS]
    
    
    # Saneo el parámetro de entrada...
    if seconds == 0:
        readable_string = "now"
        return readable_string
    if seconds < 0:
        return "Please, make sure to write a non negative input!"

    if not isinstance(seconds, int):
        return "Please, make sure to write a non negative INTEGER!"
    
    # Comienzo con la lógica de la función
    ## Diccionario para registrar los diferentes lapsos de tiempo transcurridos en el parametro
    time_hashmap = {
        "years": 0,
        "days": 0,
        "hours": 0,
        "minutes": 0,
        "seconds": 0
    }
    plur_time_lapse = [key for key in time_hashmap.keys()]
    
    sing_time_lapse = ["year", "day", "hour", "minute", "second"]
    
    # Itero sobre el parametro recibido, comenzando siempre a buscar el lapso de tiempo más grande
    for index, key in enumerate(time_hashmap.keys()):
    
        try:
            if seconds < time_list[index]:
                key_counts = 0
                time_hashmap[key] = key_counts
            else:
                key_counts = seconds // time_list[index]                
                time_hashmap[key] = key_counts
                seconds -= time_list[index] * key_counts
        except IndexError:
            if key == "seconds":
                time_hashmap[key] = seconds
    
    # Genero el string resultado
    contenido_hashmap = [(key, value) for  key, value in time_hashmap.items() if value != 0]
    
    if len(contenido_hashmap) == 1:   # Solo hay 1 tupla...
        if contenido_hashmap[0][-1] == 1:
            index_lapse = plur_time_lapse.index(contenido_hashmap[0][0])
            sing_time = sing_time_lapse[index_lapse]
            readable_string = f"{contenido_hashmap[0][-1]} {sing_time}"
            return readable_string
        else:
            readable_string = f"{contenido_hashmap[0][-1]} {contenido_hashmap[0][0]}"
            return readable_string
        
    ## Itero sobre el contenido de la lista
    readable_string = ""
    for tupla in contenido_hashmap:
        
        if tupla == contenido_hashmap[-1]:
            if tupla[-1] == 1:
                index_lapse = plur_time_lapse.index(tupla[0])
                sing_time = sing_time_lapse[index_lapse]
                readable_string += f"and {tupla[-1]} {sing_time}"
            else:
                readable_string += f"and {tupla[-1]} {tupla[0]}"        
        else:
            if tupla == contenido_hashmap[-2]:
                if tupla[-1] == 1:
                    index_lapse = plur_time_lapse.index(tupla[0])
                    sing_time = sing_time_lapse[index_lapse]
                    readable_string += f"{tupla[-1]} {sing_time} "
                else:
                    readable_string += f"{tupla[-1]} {tupla[0]} " 
            else:
                if tupla[-1] == 1:
                    index_lapse = plur_time_lapse.index(tupla[0])
                    sing_time = sing_time_lapse[index_lapse]
                    readable_string += f"{tupla[-1]} {sing_time}, "
                else:
                    readable_string += f"{tupla[-1]} {tupla[0]}, " 
        
    return readable_string

if __name__ == "__main__":
    
    seconds = 15731070
    readable_string = format_duration(seconds)
    print(readable_string)
    