#liste=["1","2","5a","10b","ABC","10","50"]
#for eleman in liste:
 #   try:
  #      x=int(eleman)
   # except Exception as ex:
    #    continue
    #else:
     #   if isinstance(x,int):
      #      print(x)

# while True:
#         x = input("bir sayi giriniz: ")
#         if x=="q":
#             break
#         else:
#             try:
#                 y=int(x)
#             except ValueError:
#                 print("lutfen bir sayi giriniz..")



parola = input("parolanizi giriniz:")
turkce_karakterler="ÇçıİöÖüÜğĞŞş"

for x in parola:
    if x in turkce_karakterler:
        raise TypeError("turkce karakter iceremez")
    else:
        pass
