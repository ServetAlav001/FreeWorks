cumle = input("bir cumle giriniz: ")
harf_sayilari ={}
for harf in cumle:
    if harf in harf_sayilari:
        harf_sayilari[harf] +=1
    else:
        harf_sayilari[harf]=1

print(harf_sayilari)
