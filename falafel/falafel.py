def falafel(s: str) -> bool :
    tab_str1 = []
    tab_str2 = []
    
    for i in range (len(str)/2):
        tab_str1.append(str[i])
        i+=1
    for j in range (len(str)/2):
        tab_str2.append(str[j])
        j+=1
    
    print(tab_str1)
    
    return 0

falafel()