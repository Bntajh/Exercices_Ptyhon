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

Complexité temporelle en O(n)\*\* : Pour garantir une complexité temporelle en O(n), nous devons nous assurer que le temps d'exécution de l'algorithme est proportionnel à la taille de l'entrée, qui dans ce cas est représentée par le paramètre n. Cela signifie que le temps d'exécution de l'algorithme doit croître linéairement avec n.

En résumé, la fonction roger_rabbit génère la représentation binaire de chaque nombre de 1 à n en utilisant une approche itérative sans utiliser de conversion de base.
