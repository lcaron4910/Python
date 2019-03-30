chaine=input("votre phrase\n")
chaine1=""
liste=[]
long=0
for car in chaine:
    if (car!=" "):
        liste.append(car)
        chaine1=chaine1+car
        long+=1
eniahc=""
for i in range (long-1,-1,-1):
    eniahc=eniahc+liste[i]
if (chaine1 == eniahc):
    print("palindromes")
else :
    print("non")
    print(chaine1)
print(eniahc)
