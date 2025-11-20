def permute_a_palindrome(caracteres):
    diccionario = {}                                            #defino diccionario para contear las letras

    for letra in caracteres:                                        #recorre el input que damos, y le asigna a cada valor el nombre 'letra' (letra='a', letra='b'...)
        if letra in diccionario:                                    #si... 'letra' ya estaba dentro de 'diccionario'
            diccionario[letra] = diccionario[letra] + 1             #le subimos el valor +1 (le contamos una aparición más)
        else:                                                       #si no...
            diccionario[letra] = 1                                  #se establece su valor inicial: 1 (primera vez que aparece, su conteo es 1)

    letras_impares = 0                                              #iniciamos contador para las letras impares

    for letra in diccionario:                                       #ahora recorremos cada 'letra' en 'diccionario'
        if diccionario[letra] % 2 != 0:                             #si el valor de esa 'letra' en 'diccionario' lo divides entre dos, y el resultado NO es 0...
            letras_impares = letras_impares + 1                     #suma +1 a 'letras_impares' (efectivamente es impar, así que cuenta uno)

    if letras_impares > 1:                                          #si el conteo total de 'letras_impares' supera 1...
        return False                                                #devuelve False y termina, tiene más de una letra impar y NO es un palíndromo.
    else:                                                           #si no...
        return True                                                 #devuelve True y termina, SÍ es un palíndromo.