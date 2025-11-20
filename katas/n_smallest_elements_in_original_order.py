def first_n_smallest(arr, n):                     
    
    smallest = sorted(arr)[:n]            #copia de la lista arr, pero ordenada "hasta n". Si n es 3, pues los primeros 3.

    finals = []                           #creamos finals para luego meter el resultado final
    for num in arr:                       #recorremos los numeros en arr
        if num in smallest:               #si ese mismo num está también en 'smallest'
            finals.append(num)             
            smallest.remove(num)          #lo añadimos a finals, y lo quitamos de smallest (evita duplicados)

    return finals                         #devolvemos la finals