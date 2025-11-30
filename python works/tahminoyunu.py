import random
pcsayi=random.randint(1,50)
print(pcsayi)
tahmin_hakki=3
print("tahmin hakki",tahmin_hakki)

while True:
    sayi = int(input("sayiyi tahmin edin:"))
    if(pcsayi==sayi):
        print("sayiyi dogru tahmin ettiniz:",pcsayi)
        break
    else:
        tahmin_hakki -=1
        print("kalan tahmin hakki:",tahmin_hakki)
        if tahmin_hakki==0:
            print("tahmin hakkiniz bitmistir.")
            break
