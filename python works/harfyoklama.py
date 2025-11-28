#dosya okuma
#hangi harften kac kelime oldugunu gosterir
with open("dosya.txt","r",encoding="utf-8") as file:
    satirdizisi=file.readlines()

    for satir in satirdizisi:
        yenisatirdizisi=satir.split(" ")
        for eleman in yenisatirdizisi:
            if eleman.find("a")>-1:
                print(eleman)
