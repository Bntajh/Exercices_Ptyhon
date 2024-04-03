La fonction ying_yang vérifie la validité des paires de caractères ouvrants et fermants dans une chaîne de caractères.

Solution Propose:

Initialisation des Variables : La fonction initialise des compteurs et des listes pour suivre les caractères rencontrés.

Parcours de la Chaîne : Pour chaque caractère dans la chaîne :

Si le caractère est un caractère ouvrant, il est ajouté à une pile (temps) pour vérifier les correspondances avec les caractères fermants.
Si le caractère est un caractère fermant, il est comparé avec le dernier caractère ouvrant rencontré. S'ils ne correspondent pas, la fonction renvoie False.
Si le caractère est un guillemet simple ou double, le compteur correspondant est incrémenté.
Si le caractère n'est ni ouvrant, ni fermant, ni guillemet, la fonction renvoie False.
Vérification Finale : La fonction vérifie que le nombre total de caractères ouvrants est égal au nombre total de caractères fermants, ainsi que le nombre de guillemets simples et doubles. Si toutes ces conditions sont remplies, la fonction renvoie True, sinon elle renvoie False.

Complexité Temporelle :

La fonction a une complexité temporelle linéaire O(n), où n est la longueur de la chaîne reçue. Cela est dû à une seule itération sur la chaîne initiale, sans recours à des boucles imbriquées .

Conclusion :
La fonction ying_yang satisfait bien les contraintes du sujet en vérifiant les paires de caractères ouvrants et fermants dans une chaîne donnée.


