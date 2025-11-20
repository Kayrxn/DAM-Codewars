def alphabet_position(texto):
    texto = texto.lower()                                # Convierte el texto a minúsculas para simplificar la comparación
    posiciones = []                                      # Crea una lista vacía donde se guardarán las posiciones numéricas

    for caracter in texto:                               # Recorre cada carácter del texto
        if caracter.isalpha():                           # Si el carácter es una letra del alfabeto
            posicion = ord(caracter) - 96                # Calcula su posición en el alfabeto (a=97 en ASCII, por eso se resta 96)
            posiciones.append(str(posicion))             # Convierte la posición a texto y la añade a la lista de posiciones
        else:                                            # Si el carácter no es una letra...
            continue                                     # Lo ignora y pasa al siguiente

    return ' '.join(posiciones)                          # Une todas las posiciones con espacios y devuelve el resultado