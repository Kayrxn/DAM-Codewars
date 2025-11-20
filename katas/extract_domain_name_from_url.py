def domain_name(url):
    #Quitamos el "http://" y similares
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    
    #Separamos el texto por los puntos
    partes = url.split(".")
    
    #El dominio está en la primera parte
    dominio = partes[0]
    
    #Lo devolvemos
    return dominio