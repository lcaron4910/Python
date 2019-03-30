chaine=input("votre phrase\n").lower()
listeLettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longueur=len(listeLettre)
compteur=0
for car in chaine :
    cpt=0
    for i in listeLettre:
        if (car==i):
            compteur+=1
            listeLettre[cpt]=""
        cpt+=1
if (compteur==26):
    print("cette phrase est un pangramme")
else:
    print("cette phrase n'est pas un pangramme")

