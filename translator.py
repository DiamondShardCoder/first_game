def translate(phrase):
    
    translation = ""
    
    for letter in phrase:
        if letter.lower() in "p":
            if letter.upper():
                translation = translation + 'F'
            else:
                translation = translation + 'f'
        
        elif letter.lower() in "f":
            if letter.upper():
                translation = translation + 'P'
            else:
                translation = translation + 'p'

        else:
            translation = translation + letter
            
    return translation

print(translate(input('Enter the phrase: ')))