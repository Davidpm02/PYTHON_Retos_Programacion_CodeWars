"""DESCRIPTION:

Your task is to implement a function that calculates an election winner from a list of voter selections
using an Instant Runoff Voting algorithm. 
If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

- Each voter selects several candidates in order of preference.
- The votes are tallied from the each voter's first choice.
- If the first-place candidate has more than half the total votes, they win.
- Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
- In case of a tie for least, remove all of the tying candidates.
- In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
- Start over.
- Continue until somebody has more than half the votes; they are the winner.

Your function will be given a list of voter ballots;
each ballot will be a list of candidates (symbols) in descending order of preference.

You should return the symbol corresponding to the winning candidate. 

See the default test for an example!

voters = [["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]

        test.assert_equals(runoff(voters), "ind")
        
        
voters = [["a", "c", "d", "e", "b"],
                 ["e", "b", "d", "c", "a"],
                 ["d", "e", "c", "a", "b"],
                 ["c", "e", "d", "b", "a"],
                 ["b", "e", "a", "c", "d"]];
        test.assert_equals(runoff(voters), None)"""
        
        
        
def runoff(voters):
    
    """
       Summary
           Función parametrizada que se encarga de evaluar los resultados de unas elecciones dadas, y encontrar al ganador
           de estas, mediante una implementación del algoritmo 'Instant Runoff Voting', o 'IRV'.
           Las condiciones de acción de la función se detallan en la DESCRIPTION del problema.
             
       Args
           voters -- Array  de listas que contienen las votaciones de len(voters) personas. Cada elemento de 'voters' contiene
                     los candidatos votados por una persona en cuestión, y estos aparecen en la lista por orden de preferencia 
                     de esta persona.
        
       Returns
           winner -- Ganador de las elecciones / candidato más votado.
                     En caso de no haberse definido un ganador, la función retorna None.
    """
    
    
    # Primero, verifico que todos los elementos del array padre (parámetro) tienen la misma longitud
    num_voters = len(voters)
    estimated_length = len(voters[0])
    for vote in voters:
            assert len(vote) == estimated_length
            
    # Ahora, defino un conjunto que reuna todas los diferentes cantidatos votados
    set_cantidates = set(voters[0])   # Tomo como referencia las votaciones del primer usuario


    # Defino un diccionario que mapee cada uno de los candidatos
    dict_candidates = {cantidate:0 for cantidate in set_cantidates}  # Asigno 0 como valor inicial para todos los candidatos


    
    ## Buscando al ganador (IRV algorithm)======================
    
    while True:
                  
        # Analizo el primer cantidato de todas las votaciones, y actualizo su valor en el diccionario
        prefered_candidates = [vote[0] for vote in voters]
        
        # Actualizo los valores del diccionario
        for candidate in prefered_candidates:
                dict_candidates[candidate] += 1
                
        times_prefered_candidates = [value for key, value in dict_candidates.items() if key in prefered_candidates]
        # Verifico si existe algún ganador en el diccionario
        dicts_keys = list(dict_candidates.keys())
        dicts_values = list(dict_candidates.values()) 
        if len(set(dicts_values)) == 1:   # Compruebo que no todos los cantidatos tengan el mismo número de votaciones
            return None
        
        max_votes_candidate = max(dicts_values)
        most_voted_cantidates = [key for key in dict_candidates.keys() if dict_candidates[key] == max_votes_candidate]
        
        if len(most_voted_cantidates) > 1:       
            # Elimino a los candidatos menos votados de todas las votaciones
            voters_ = []
            for vote in voters:
                new_vote_list = []
                for candidate in vote:
                    if candidate not in most_voted_cantidates:
                        continue
                    else:
                        new_vote_list.append(candidate)
                voters_.append(new_vote_list)
            voters = voters_
            
            # Si alguno de los candidatos no aparece como primer votado, elimino este candidato de todos los votos
            non_voted_candidates = [key for key, value in dict_candidates.items() if value == 0]
        
            # Elimino al candidato perdedor de todas las votaciones
            voters_ = []
            for vote in voters:
                new_vote_list = []
                for candidate in vote:
                    if candidate in non_voted_candidates:
                        continue
                    else:
                        new_vote_list.append(candidate)
                voters_.append(new_vote_list)
            voters = voters_
        
        
            
            
            for _ in voters:
                print(_)
            continue
        
        # ¿Tiene el candidato más votado, más de la mitad de los votos?
        if max_votes_candidate == (num_voters // 2) or max_votes_candidate > (num_voters // 2):
            is_candidate_half_voted = True
        else:
            is_candidate_half_voted = False
            
        if is_candidate_half_voted == True:
            index_max_votes_candidate = dicts_values.index(max_votes_candidate)
                
            winner = dicts_keys[index_max_votes_candidate]
            break
        
        else:
            
            # Continuo aplicando la lógica del algoritmo.
            # Busco al usuario menos votado, y lo elimino de todas las votaciones
            min_votes_candidate = min(dicts_values)
            indexes_min_votes_candidate = []
            for i, value in enumerate(dicts_values):
                if value == min_votes_candidate:
                    indexes_min_votes_candidate.append(i)
            losers = []
            for i, key in enumerate(dicts_keys):
                if i in indexes_min_votes_candidate:
                    losers.append(key)
            
            # Elimino al candidato perdedor de todas las votaciones
            voters_ = []
            for vote in voters:
                new_vote_list = []
                for candidate in vote:
                    if candidate in losers:
                        continue
                    else:
                        new_vote_list.append(candidate)
                voters_.append(new_vote_list)
            voters = voters_
            for _ in voters:
                print(_)
                
                
            if len(set(times_prefered_candidates)) == 1:   # Compruebo que no todos los cantidatos tengan el mismo número de votaciones
                voters_ = []
                for vote in voters:
                    new_vote_list = []
                    for candidate in vote:
                        if candidate  in prefered_candidates:
                            continue
                        else:
                            new_vote_list.append(candidate)
                    voters_.append(new_vote_list)
                voters = voters_
            continue
  
        
    return winner


if __name__ == "__main__":
    
    # Example ...
    voters = [['Brian J. Mason', 'Abelt Dessler', 'Drake Luft', 'Johan Liebert', 'Gihren Zabi'], 
                ['Abelt Dessler', 'Brian J. Mason', 'Johan Liebert', 'Gihren Zabi', 'Drake Luft'],
                ['Gihren Zabi', 'Abelt Dessler', 'Drake Luft', 'Brian J. Mason', 'Johan Liebert'],
                ['Gihren Zabi', 'Abelt Dessler', 'Drake Luft', 'Brian J. Mason', 'Johan Liebert'],
                ['Abelt Dessler', 'Gihren Zabi', 'Brian J. Mason', 'Drake Luft', 'Johan Liebert'],
                ['Gihren Zabi', 'Abelt Dessler', 'Brian J. Mason', 'Drake Luft', 'Johan Liebert']]
    
    winner = runoff(voters)
    print(winner)
    
            