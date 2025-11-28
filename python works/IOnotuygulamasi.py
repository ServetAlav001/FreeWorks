#not ortalama hesaplam programı
def not_gir():
    ad = input("ogrenci adi:")
    soyad=input("ogrenci soyadi:")
    not1=input("not 1:")
    not2=input("not 2:")
    not3=input("not 3")

    with open("notlardosyasi.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
def not_hesapla(satir):
    satir=satir[:-1]
    liste = satir.split(":")
    ogrenci_adi=liste[0]
    ogrenci_notlari=liste[1]
    notlistesi=ogrenci_notlari.split(",")
    not1=notlistesi[0]
    not2=notlistesi[1]
    not3=notlistesi[2]
    ortalama = (int(not1)+int(not2)+int(not3))/3
    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama<90 and ortalama>=85:
        harf="BA"
    elif ortalama<85 and ortalama>=70:
        harf="BB"
    elif ortalama<70 and ortalama>=60:
        harf="CB"
    elif ortalama<60 and ortalama>=50:
        harf="CC"
    elif ortalama<50:
        harf="FF"
    return ogrenci_adi + ": "+harf+"\n"
def ortalama_oku():
    with open("notlardosyasi.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_kayit():
    with open("notlardosyasi.txt","r",encoding="utf-8") as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))
        with open("harf_notlari.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem =input("1-notları oku\n2-not gir\n3-notları kayit et\nq-cikis yap\n")

    if islem=="1":
        ortalama_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        not_kayit()
    elif islem=="q":
        break
    else:
        print("yanlis bir islem girdiniz...")
