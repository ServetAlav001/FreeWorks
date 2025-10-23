sehirler = ["Adana","Adiyaman","Afyon","Ağri","Amasya","Ankara","Antalya","Artvin","Aydin","Balikesir","Bilecik","Bingöl",
    	"Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankiri","Çorum","Denizli","Diyarbakir","Edirne","Elâziğ","Erzincan",
        "Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkâri","Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu",
   	    "Kayseri","Kirklareli","Kirşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş",
    	"Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli",
        "Şanliurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kirikkale","Batman","Şirnak","Bartin","Ardahan",
        "Iğdir","Yalova","Karabük","Kilis","Osmaniye","Düzce"]

print("plakalar uygulamasina hosgeldiniz...")


while(True):
    try:
            cevap =input("lutfen bir plaka veya sehir adi giriniz:")
            if(cevap=="q"):
                print("sistemden cikiliyor..")
                break
            if(cevap!="q"):
                if(cevap in sehirler):
                    index =sehirler.index(cevap)
                    print(index+1)
                else:
                    cevap2 = int (cevap)
                    if(sehirler[cevap2-1]):
                        print(sehirler[cevap2-1])
    except: 
            print("cevap hatali..")   
