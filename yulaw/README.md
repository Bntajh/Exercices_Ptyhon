Solution Propose :

j'ai cree une fonction qui prend en paramettre une chaine de caractere 

def yulaw(s: str) -> str:


Ensuite j'ai Initialiser une chaîne vide pour stocker le résultat
    result = ''


j'ai cree une boucle pour parcourir chaque caractere de la chaine 
   for i in s:

dans la boucle j'ai fait une condition dans laquelle je dit si le caractère n'est pas déjà dans le résultat,  il va l'ajouter
  if i not in result:
            result += i


