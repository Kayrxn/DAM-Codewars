def to_camel_case(text):
    if text == "":
        return ""
    
    result = ""
    
    i = 0
    capitalize_next = False

    while i < len(text):
        character = text[i]
        
        if character == '-' or character == '_':
            capitalize_next = True
        else:
            if capitalize_next:
                result += character.upper()
                capitalize_next = False
            else:
                result += character
        i += 1
    
    return result