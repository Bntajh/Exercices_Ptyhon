La fonction morning_sunshine prend une liste d'entiers numbers et renvoie une nouvelle liste contenant les éléments qui sont supérieurs à tous les éléments à leur droite dans la liste. Voici un résumé concis de son fonctionnement :

Les étapes :

1.Initialise une liste vide result pour stocker les éléments répondant au critère.

2.Initialise max_value à -inf pour garder une trace du maximum rencontré jusqu'à présent.

3.Parcourt la liste numbers en partant de la fin avec reversed(numbers).

4.À chaque itération, si l'élément actuel num est supérieur à max_value, il est ajouté à result et max_value est mis à jour.

5.Retourne result inversé pour retrouver l'ordre original.

Complexité :
Temporelle : O(n), où n est la taille de numbers, car chaque élément est visité une fois.
Mémoire : O(n), si tous les éléments de numbers répondent au critère, sont stockés dans result.

Conclusion :
morning_sunshine est une solution efficace pour extraire les éléments d'une liste qui sont plus grands que tous les éléments à leur droite. En parcourant la liste de droite à gauche et en gardant une trace du maximum rencontré, cette fonction garantit un traitement rapide et utilise un espace mémoire minimal pour stocker les résultats.