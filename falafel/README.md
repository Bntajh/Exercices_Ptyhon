# Fonction falafel

La fonction falafel prend une chaîne de caractères s en paramètre et détermine si la chaîne est une permutation palindrome.

Description

1. Cas de base : Si la longueur de la chaîne s est inférieure ou égale à 1, la fonction retourne True, car une chaîne de un ou aucun caractère est toujours un palindrome.

2. Initialisation des variables : La fonction initialise un dictionnaire char_count pour compter le nombre d'occurrences de chaque caractère dans la première moitié de la chaîne s. Elle détermine également l'indice médian middle de la chaîne.

3. Comptage des occurrences : La fonction parcourt les premiers caractères de la chaîne jusqu'à l'indice middle et met à jour le dictionnaire char_count avec le nombre d'occurrences de chaque caractère rencontré.

4. Vérification de la condition de permutation palindrome : La fonction parcourt le reste de la chaîne, en vérifiant si les caractères rencontrés ont déjà été rencontrés dans la première moitié de la chaîne. Si un caractère n'a pas été rencontré précédemment, il est ajouté au dictionnaire. Si un caractère a déjà été rencontré, son occurrence est décrémentée dans le dictionnaire. Si l'occurrence atteint 0, le caractère est supprimé du dictionnaire. Si à tout moment le nombre de caractères différents dans le dictionnaire dépasse 1, la fonction retourne False, indiquant que la chaîne n'est pas une permutation palindrome.

5. Retour du résultat : Si aucune condition d'échec n'est rencontrée, la fonction retourne True, indiquant que la chaîne est une permutation palindrome.

Complexité

- Complexité temporelle en O(n) : La fonction parcourt la chaîne s une seule fois avec deux boucles, ce qui maintient sa complexité temporelle en O(n), où n est la longueur de la chaîne s.

En résumé, la fonction falafel vérifie si une chaîne est une permutation palindrome en utilisant un dictionnaire pour compter les occurrences de chaque caractère. Si la chaîne répond aux conditions pour être une permutation palindrome, la fonction renvoie True, sinon elle renvoie False.
