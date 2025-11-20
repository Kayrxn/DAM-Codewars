import math

def roots(a,b,c):
    discriminante = b ** 2 - 4 * a * c
    
    if discriminante < 0:
        return None
    
    rootA = (-b - math.sqrt(discriminante)) / (2*a)
    rootB = (-b + math.sqrt(discriminante)) / (2*a)
    
    return round(rootA + rootB, 2)