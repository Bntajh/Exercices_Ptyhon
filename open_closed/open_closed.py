def open_closed(s: str) -> bool:
    temps = []
    ouvrant = "({<['\""
    fermant = ")}>]\"'"
    chaine_correspondance = {')': '(', ']': '[', '}': '{', '>': '<', "'": "'", '"': '"'}
    
    for char in s:
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
    " '\"",    
]

test_number = 1
for test in tests:
    result = open_closed(test)
    print(f"Test {test_number}: {test}\tRésultat: {result}")
    test_number += 1
