def falafel(s: str) -> bool:
    middle = len(s) // 2
    res = True

    for i in range(middle):
        if s[i] != s[len(s) - 1 - i]:
            res =  False
    
    return res

# Test de la fonction
print(falafel("lalal"))  # True
print(falafel("test"))  # False