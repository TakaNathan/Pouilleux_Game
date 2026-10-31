#Question1

#Fonction qui retourne le nombre d'elements
# > 100 dans une liste
# (list)->(int)
def compte100(list) :
    compteur = 0
    for i in list :
        if i > 100 :
            compteur += 1
    return compteur
#compte100([1,99,-3.5,-7])

#Question2

# Fonction qui retourne la moiitie de la somme
#de ses elements
#(List)-> int
def sommeListeDiv2(list) :
    somme = 0
    for i in list :
        if i%2 == 0 :
            somme += i
    return somme
#print(sommeListeDiv2([46,0,2,1,100,35]))

#Question3
# Fonction qui retourne true s'il y'a une sequence
#consecutive de 3 memes caractere dans la chaine
#(str)-> bool
def triples(str) :
    resultat = False
    for i in range(len(str)) :
        if i+2 >= len(str): #condition pour arreter la boucle et eviter un outofrange
            break
        if str[i] == str[i+1] :
            if str[i] == str [i+2] :
                resultat = True
                break
    return resultat  
#print(triples("a23xxxxx"))

#Question4
#Fonction qui retourne un nouveau str avec les
# caracteres et le nbre d'occurences de chaque caractere du str parametre
#(str)-> str
def momo(string) :
    new_str = ""
    """for i in range(len(string)) :
        car = string[i]
        if car in new_str :
            continue
        new_str = new_str+car+str(string.count(car))
    return new_str"""
    n = 1
    for i in range(len(string)) :
        if i+1 == len(string) :
            new_str = new_str+string[i]+str(n)
            break
        if string[i] == string[i+1] :
            n+=1
        else :
            new_str = new_str+string[i]+str(n)
            n = 1
    return new_str
#print(momo("aaabcaax"))

#Question5
#Fonction qui retourne une nouvelle chaine contenant
# 1 fois chaque caractere de la chaine en parametre
#(str)->(str)
def noDup(string) :
    new_str = string[0]
    i=1
    while i<len(string) :
        if string[i] != string[i-1] :
            new_str = new_str+string[i]
        i+=1
    return new_str
#print(noDup("aabbbcccx"))   


