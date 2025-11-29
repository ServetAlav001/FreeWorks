import random

sayi =int(100*random.random())
print(sayi)
liste=[]

for x in range(0,sayi):
    sayi2=int(100*random.random())
    liste.append(sayi2)

def tekmiciftmi():
    tekliste=[]
    ciftliste=[]

    for x in liste:
        if x%2==0:
            ciftliste.append(x)
        elif x%2!=0:
            tekliste.append(x)
    print("tekler:",tekliste)
    print("ciftler: ",ciftliste)

tekmiciftmi()
