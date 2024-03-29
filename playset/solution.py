def playset(s: str) -> bool:
    caracters = set()

    for caractere  in s:
        if caractere in caracters:
            return True
        else:
            caracters.add(caractere)
    
    return False

# s="abcdeab"
# print(playset(s))