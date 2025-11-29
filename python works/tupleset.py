yasakli_karakterler = ('?', '!', '/', '@')
sifre = input("sifreyi giriniz:")
sifreseti=set(sifre)
yeniset = sifreseti.difference(yasakli_karakterler)
if yeniset==sifreseti:
    print(f"sifre dogru: {sifre}")
    print(f"sifre karakterleri: {sifreseti}")

elif yeniset!=sifreseti:
    print("sifre karakter hatasi")
