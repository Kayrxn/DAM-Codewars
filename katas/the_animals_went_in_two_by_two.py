def two_by_two(animals):
    
    if animals == []:
        return False
    
    pairs = {}
    count = {}
    for animal in animals:
        
        if animal in count:
            count[animal] += 1
        else:
            count[animal] = 1
            
        if count[animal] == 2:
            pairs[animal] = 2
            
    return pairs