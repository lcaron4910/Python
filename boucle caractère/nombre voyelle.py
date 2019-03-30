listeVoyelle=["a","e","i","o","u","y"]
chaine=input("votre phrase\n").lower()
compteur=0
for car in chaine :
    for i in listeVoyelle:
        if (car==i):
            compteur+=1
print(compteur)
