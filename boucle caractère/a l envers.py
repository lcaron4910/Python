chaine=input("votre phrase\n")
long=len(chaine)
liste=[]
for car in chaine:
    liste.append(car)
chaine=""
for i in range (long-1,-1,-1):
    chaine=chaine+liste[i]
print (chaine)
