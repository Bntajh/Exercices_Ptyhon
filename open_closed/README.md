# Fonction open_closed

La fonction `open_closed` prend une chaîne de caractères en paramètre et vérifie si les parenthèses, crochets et guillemets dans la chaîne sont correctement équilibrés. Elle retourne `True` si c'est le cas, sinon elle retourne `False`. La fonction maintient une complexité temporelle en O(n) et une complexité mémoire constante.

## Algorithme

1. Initialisation des compteurs : Nous initialisons des compteurs pour les ouvrants et les fermants ainsi que pour les guillemets simples et doubles.

2. Parcours de la chaîne : Nous parcourons chaque caractère de la chaîne d'entrée.

3. Mise à jour des compteurs : Nous mettons à jour les compteurs en fonction du caractère rencontré : ouvrant, fermant, guillemet simple ou guillemet double.

4. Vérification de l'équilibre** : À chaque itération, nous vérifions si le nombre de parenthèses ouvrantes est inférieur au nombre de parenthèses fermantes. Si c'est le cas, nous retournons `False`.

5. Vérification finale** : En fin de parcours, nous vérifions si le nombre de parenthèses ouvrantes est égal au nombre de parenthèses fermantes et si le nombre de guillemets simples et doubles est pair. Si toutes ces conditions sont remplies, nous retournons `True`, sinon nous retournons `False`.

 Complexité

Complexité temporelle en O(n)** : La fonction parcourt la chaîne de caractères une seule fois, garantissant une complexité temporelle en O(n), où n est la longueur de la chaîne de caractères.
  
- Complexité mémoire constante: La fonction n'utilise pas de mémoire supplémentaire en dehors des compteurs, assurant une complexité mémoire constante.

## Conclusion

La fonction `open_closed` offre une solution efficace pour vérifier l'équilibre des parenthèses, crochets et guillemets dans une chaîne de caractères, tout en maintenant une complexité temporelle en O(n) et une complexité mémoire constante.
