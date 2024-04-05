Fonction roger_rabbit

La fonction roger_rabbit prend un entier naturel (n) en paramètre et renvoie un tableau de chaînes de caractères, dans l'ordre croissant.

1. Initialisation d'un tableau vide nommé 'tab' : Nous commençons par initialiser un tableau vide pour stocker le résultat final.

2. Boucle qui parcours tous les nombre compris entre 1 et n (inclus) :

- Initialisation d'un string 'binary' à chaque début d'un nouveau nombre de la boucle: Nous commençons par initialiser binary en une string vide, cette variable va contenir la représentation binaire du nombre actuel.

- Pour déterminer la représentation binaire du nombre i, nous utilisons une boucle while :  
  → A chaque itération de cette boucle, on divise le nombre i par 2 et on ajoute le reste (0 ou 1) au début de la chaîne binaire. Cela équivaut à répéter la division par 2 jusqu'à ce que i devienne 0. Le reste de chaque division est constitué des chiffres binaires de ce nombre.

  → Une fois que i devient 0, cela signifie que nous avons déterminé tous les chiffres binaires du nombre. Nous ajoutons alors la chaîne binary à la liste tab.

- Une fois que toutes les représentations binaires ont été générées et ajoutées à la liste tab,

- Puis nous retournons cette liste.

Complexité de convertion : nous ne pouvons pas utiliser de conversion d'une base vers une autre.

Complexité temporelle :

a. Boucle Principale (for) :

    - La boucle principale itère de 1 à n. Cela signifie que le nombre d'itérations est proportionnel à n. Cette boucle a une complexité temporelle de O(n).

b. Boucle Interne (While) :

    - La boucle interne itère jusqu'à ce que i devienne 0. À chaque itération, i est divisé par 2, ce qui réduit sa valeur. Cette division répétée par 2 se poursuit jusqu'à ce que i atteigne 0.

    - Cette boucle itère jusqu'à ce que i devienne 0 en divisant i par 2 à chaque itération. Cela signifie que le temps d'exécution de cette boucle est logarithmique par rapport à i, soit O(log i).

    - Comme cette boucle interne est exécutée pour chaque valeur de i dans la plage de 1 à n, le pire des cas se produit lorsque i est maximal, c'est-à-dire lorsque i = n. Donc, la complexité temporelle totale due à cette boucle interne est O(log n).

En résumé, la fonction roger_rabbit a une complexité temporelle de O(n log n), où la boucle principale contribue pour O(n) et la boucle interne pour O(log n) à chaque itération de la boucle principale.
