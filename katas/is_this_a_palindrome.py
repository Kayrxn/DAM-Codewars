def is_palindrome(s):
    
    
    if s.lower() == s.lower()[::-1]:  #Si la palabra se lee igual del revés (::-1). lower() para pasar todo a minúscula.
        return True
    else:
        return False