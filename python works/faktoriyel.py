sonuc=1
try:
    sayi = int(input("bir sayi giriniz: "))
    if sayi<0:
        print("0 dan kucuk deger girmeyin..")
    else:
        for i in range(1,sayi):
            sonuc *=i
    print("faktoriyel sonucu: ",sonuc)
except ValueError:
    print("bir sayi degeri girein string deger girmeyin..")
finally:
    print("sistemden cikildi")
