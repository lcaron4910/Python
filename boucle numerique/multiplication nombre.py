print("entrer votre nbr ?")
nb=int(input())
somme=0
for i in range (0,nb+1,1):
    somme=somme+(i*i)
    print(somme,"=",i*i)
print(somme)
