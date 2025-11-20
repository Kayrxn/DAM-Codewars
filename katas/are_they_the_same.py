def comp(number_list_a, number_list_b):

    if number_list_a is None:
        return False
    
    if number_list_b is None:
        return False
    
    if not number_list_a and not number_list_b:
        return True
    
    squared_a = []  #lista para convertir la lista a en su versión ** 2

    for num in number_list_a:
        squared_a.append(num ** 2) #todo en lista a pasa a estar elevado al cuadrado

    squared_a.sort()  #ordenamos las listas
    number_list_b.sort()

    if squared_a == number_list_b:
        return True
    else:
        return False