print("entrer votre capital ?")
capital=int(input())
capital1=capital
print("entrer le taux ?")
taux=int(input())
taux1=(1+1/taux)
print(taux1)
print("entrer le nombre d'année ?")
année=int(input())
doublé=0

for i in range (0,année+1,1):
    capital1=capital1*taux1
    print(round(capital1,2))
    if (doublé==0):
        if (capital1 >(2*capital)):
            print(capital1,capital)
            print ("capital doublé en",i,"ans")
            doublé = 1
            
capital2=capital
cpt=1
if (doublé==0):
    while (doublé==0):
        capital2=capital2*taux1
        if (doublé==0):
            if (capital2 >(2*capital)):
                print("capital doublé en ",cpt,"ans")
                doublé = 1
        cpt=cpt+1
print ("en ",année,"ans votre capital aura atteint :",round(capital1,2))

