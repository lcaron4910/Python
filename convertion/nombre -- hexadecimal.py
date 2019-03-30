n = int(input("Entrez un nombre:"))
alph, hex ='ABCDEF',''
while n:
    if n%16>=10:
        hex = alph[(n%16)%10]+hex
    else:
        hex = str(n%16)+hex
        
            
    n=n//16
print("L'écriture hexdecimal est :",hex)
