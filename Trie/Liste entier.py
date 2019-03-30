n= int(input("Entrez n : ?"))
liste = n*[1]
listePrems=[]
cpt=0
for k in range(2,n):
    for i in range (k+1,n):
        if (i%k==0):
            liste[i]=0
for j in range(0,n):
    if liste[j]==1:
        listePrems=listePrems+ [j]
for h in range (2,len(listePrems)):
    if h==(len(listePrems)-1):
        print(listePrems[h])
    else :
        print(listePrems[h],end="-")
cpt = (len(listePrems)-2)
pourcentage=(cpt/n)*100

print("il y a ",cpt," nombre premiers de 0 a n")
print("il y a ",pourcentage,"% de nbr premier")
