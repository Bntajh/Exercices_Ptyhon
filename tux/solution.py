def tux(numbers: list[int]) -> int :
    longueur_n = len(numbers)

    if longueur_n == 0:
        return -1
    
    max_gauche = [0] * longueur_n
    min_droite = [0] * longueur_n
    

    max_val = numbers[0]
    for i in range(longueur_n):
        max_val = max(max_val, numbers[i])
        max_gauche[i] = max_val
    

    min_val = numbers[-1]
    for i in range(longueur_n - 1, -1, -1):
        min_val = min(min_val, numbers[i])
        min_droite[i] = min_val
    

    for i in range(1, longueur_n - 1):
        if max_gauche[i - 1] < numbers[i] <= min_droite[i + 1]:
            return i
    

    if numbers[0] <= min_droite[1]:
        return 0
    if max_gauche[longueur_n - 2] < numbers[-1]:
        return longueur_n - 1
    
    return -1
