import datetime
import random
class musteri :
    def __init__(self,ad,soyad,parola):
        self.ad = ad
        self.soyad = soyad
        self.parola = parola
        self.hesap_bakiye = 0
        self.hesap_no = random.randint(1000,9999)

    def para_yatir(self,miktar):
        if miktar<0:
            print("lutfen 0 dan buyuk bir deger giriniz.")
        else:
            self.hesap_bakiye+=miktar
            print("para eklendi")

    def para_cek(self,miktar):
        if miktar<0:
            print("lutfen 0 dan buyuk bir deger giriniz.")
        else:
            sonuc =self.hesap_bakiye-miktar
            if sonuc<0:
                print("bakiye yetersiz.")
                print(f"bakiye: {self.hesap_bakiye}")
            else:
                self.hesap_bakiye=sonuc
                print("para cekildi")
                print(f"kalan para: {sonuc}")

    def bakiye_sorgula(self):
        print(f"bakiyeniz: {self.hesap_bakiye}")
    def makbuz(self):
        zaman = datetime.datetime.now()
        print(f"makbuz: [{zaman}], {self.ad}  {self.soyad} , {self.hesap_bakiye} , {self.hesap_no}")
        with open("makbuz.txt","a",encoding="utf-8") as file:
            file.write(zaman.strftime("%d/%m/%Y, %H:%M:%S")+"\n")
            file.write(self.ad + " ")
            file.write(self.soyad + " ")

            file.write("hesap bakiye:"+str(self.hesap_bakiye))
            file.write("hesap no:"+str(self.hesap_no)+"\n")


musteriler =[]
islemler_ana =("1.islem=giris yap\n"
           "2.islem=kayit ol\n"
            "q.islem=cikis yap")
islemler_musteri=("1.islem=para cek\n"
                  "2.islem para yatir\n"
                  "3.islem=bakiye sorgula\n"
                  "4.islem=islemler\n"
                  "5.islem=makbuz\n"
                  "q.islem=cikis yap")
print(islemler_ana)

while True:
    islem = input("lutfen bir islem giriniz:")
    if islem == "1":
            ad = input("adinizi giriniz:")
            soyad = input("soyadinizi giriniz:")
            parola = input("parola giriniz:")
            for x in musteriler:
                if x.ad==ad and x.soyad==soyad and x.parola==parola:
                    print("giris basarili")
                    print(islemler_musteri)
                    while True:
                        islem = input("yapmak istediginiz islemi giriniz:")
                        if islem=="q":
                            print("programdan cikiliyor...")
                            break
                        elif islem=="1":
                            miktar = int(input("cekmek istediginiz miktari giriniz:"))
                            x.para_cek(miktar)
                        elif islem=="2":
                            miktar = int(input("yatirmak istediginiz miktari giriniz:"))
                            x.para_yatir(miktar)
                        elif islem=="3":
                            x.bakiye_sorgula()
                        elif islem=="4":
                            print(islemler_musteri)
                        elif islem=="5":
                            x.makbuz()
                            break
                        else:
                            print("hatali bir islem girdiniz..")
    elif islem == "2":
        ad = input("adinizi giriniz:")
        soyad = input("soyadinizi giriniz:")
        parola = input("parola giriniz:")
        musteriler.append(musteri(ad,soyad,parola))
        print("kayit basarili")
    elif islem == "q":
        print("programdan cikiliyor...")
        break

    else:
        print("hatali bir islem girdiniz..")
