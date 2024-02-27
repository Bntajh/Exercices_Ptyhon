def open_closed(s: str) -> bool:
    temps = []
    ouvrant = "({<[\"'"
    fermant = ")}>]\"'"
    chaine_correspondance = {')': '(', ']': '[', '}': '{', '>': '<', "'": "'", '"': '"'}
    
    for char in s:
        if char in ouvrant:
            temps.append(char)
        elif char in fermant:
            if not temps or temps[-1] != chaine_correspondance[char]:
                return False
            temps.pop() 

    return not temps


tests = [
    "[(])",      
]

for test in tests:
    result = open_closed(test)
    print(f"result:{test}: {result}")
