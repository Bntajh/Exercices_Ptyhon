def open_closed(chaine):
    temps = []
    ouvrant = "({<['\""
    fermant = ")}>]\"'"
    chaine_correspondance = {')': '(', ']': '[', '}': '{', '>': '<', "'": "'", '"': '"'}
    
    for char in chaine:
        if char == '"':
            if not temps or temps[-1] != '"':
                temps.append('"')
            else:
                temps.pop()
        elif char in ouvrant:
            temps.append(char)
        elif char in fermant:
            if not temps or temps[-1] != chaine_correspondance[char]:
                return False
            temps.pop() 

    return len(temps) == 0

tests = [
    "()",     
    "][",    
    "([])",  
    "(",     
    "(()",    
    "[(])",   
    "[)",    
    '""',    
    " ' "'"',    
]

for i, test in enumerate(tests, 1):
    result = open_closed(test)
    print(f"Test {i}: {test}\tRésultat: {result}")
