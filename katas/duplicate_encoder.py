def duplicate_encode(texto):                       
    texto = texto.lower()                          # Convierte el texto a minúsculas para ignorar mayúsculas y minúsculas
    conteo_letras = {}                             # Crea un diccionario vacío para contar las apariciones de cada carácter

    for letra in texto:                            # Recorre cada letra del texto
        if letra in conteo_letras:                 # Si la letra ya está en el diccionario...
            conteo_letras[letra] += 1              # Aumenta su contador en 1
        else:                                      # Si no...
            conteo_letras[letra] = 1               # La agrega con un conteo inicial de 1

    resultado = []                                 # Crea una lista vacía para almacenar los paréntesis resultantes

    for letra in texto:                            # Recorre nuevamente cada letra del texto
        if conteo_letras[letra] == 1:              # Si la letra aparece una sola vez
            resultado.append('(')                  # Añade "(" a la lista resultado
        else:                                      # Si la letra aparece más de una vez
            resultado.append(')')                  # Añade ")" a la lista resultado

    return ''.join(resultado)                      # Une todos los paréntesis en una sola cadena y la devuelve