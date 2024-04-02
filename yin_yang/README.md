La fonction yin_yang vérifie si une chaîne de caractères s contient des paires correctement appariées et imbriquées de parenthèses, crochets, accolades, et guillemets. Voici un aperçu simplifié :

Les étapes  :

1.Utilise une pile (stack) pour suivre les caractères ouvrants.

2.Définit des ensembles pour caractères ouvrants (opening_chars) et fermants (closing_chars), ainsi qu'un dictionnaire pour les paires correspondantes (matching_pairs).

3.Parcourt la chaîne s, ajoutant des caractères ouvrants à la pile et vérifiant la correspondance des caractères fermants avec le sommet de la pile.

4.Si un caractère fermant ne correspond pas ou s'il manque un caractère ouvrant, retourne False.

5.Retourne True si la pile est vide à la fin, indiquant que tous les caractères ouvrants ont été correctement fermés.

Complexité :
Temporelle : O(n), car elle examine chaque caractère une fois.
Mémoire : O(n), pour stocker tous les caractères ouvrants dans la pile.

Conclusion :
yin_yang est une solution efficace pour vérifier l'équilibrage des paires de délimiteurs dans une chaîne, utilisant une pile pour s'assurer que chaque caractère ouvrant est correctement apparié avec son fermant dans le bon ordre.