def merge(*dicts):
    
    result={}
    for dict in dicts:                      #recorres diccionarios en dicts
        for key, value in dict.items():         #tomas key, y values de esos diccionarios
            if key in result:
                result[key].append(value)       #si existe, añadimos el valor
            else:
                result[key] = [value]       #si no existe, creamos una lista con el valor
    
    return result