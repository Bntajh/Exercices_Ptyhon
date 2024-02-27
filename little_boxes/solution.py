def little_boxes(s: str) -> str:
    chaine_ascii = sorted(s)
    return ''.join(chaine_ascii)
chaine_ascii = 'HelloWorld'
result = little_boxes(chaine_ascii)
#print(result) 
