# Groupe de bouzia_b 1026532

Solution Propose:
def open_closed(s: str) -> bool:
    temps = []
    ouvrant = "({<['\""
    fermant = ")}>]\"'"
    chaine_correspondance = {')': '(', ']': '[', '}': '{', '>': '<', "'": "'", '"': '"'}


La fonction open_closed prend une chaîne s en entrée et renvoie un booléen (True ou False) 

j'ai utilise  temps []  pour stocker les caractères ouvrants rencontrés jusqu'à présent dans la chaîne de caractères.


ouvrant et fermant sont des chaînes contenant les caractères ouvrants et fermants respectivement.

chaine_correspondance est un dictionnaire dans lequel j'ai inséré des paires clé-valeur correspondant à chaque caractère fermant avec son caractère ouvrant correspondant.



    for char in s:
        if char == '"':
            if not temps or temps[-1] != '"':
                temps.append('"')
            else:
                temps.pop()
        elif char in ouvrant:
            temps.append(char)
        elif char in fermant:
            if not temps or temps[-1] != chaine_correspondance[char]:
                return False
            temps.pop()


Ensuite j'ai fait une boucle for qui  parcourt chaque caractère de la chaîne s.

Si un guillemet double (") est rencontré, le code vérifie s'il correspond à un guillemet double précédent. Si oui, il le retire de la liste temps; sinon, il l'ajoute.

Si le caractère est un caractère ouvrant, il est ajouté à la liste temps.

Si le caractère est un caractère fermant, le code vérifie s'il correspond au dernier caractère ouvrant dans la liste temps. Si c'est le cas, il le retire de la liste temps; sinon, la fonction renvoie False.


  return len(temps) == 0

apres la fin de la boucle la fonction vérifie si la liste temps est vide. Si c'est le cas, cela signifie que tous les caractères ouvrants ont été correctement appariés et fermés, et la fonction renvoie True; sinon, elle renvoie False.