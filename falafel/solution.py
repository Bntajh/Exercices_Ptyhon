def falafel(s: str) -> bool:
    # Si la chaîne est vide ou ne contient qu'un seul caractère, elle est considérée comme une permutation palindrome
    if len(s) <= 1:
        return True

    # Compter les occurrences de chaque caractère dans la chaîne
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Compter le nombre de caractères ayant un nombre impair d'occurrences
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Si le nombre de caractères avec un nombre impair d'occurrences est supérieur à 1, la chaîne ne peut pas être une permutation palindrome
    if odd_count > 1:
        return False
    else:
        return True

print(falafel("falafel"))  # Output: False
