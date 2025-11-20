def cookie(x):
    
    if isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    
    elif isinstance(x, int) or isinstance(x, float):
        return "Who ate the last cookie? It was Monica!"
    
    elif isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
        
    else:
        return "Who ate the last cookie? It was the dog!"
        

    #Espera que sea "dog" con "True" que es un boolean, pero python intepreta como int.
    #Entonces, primero se debe comprobar por boolean.