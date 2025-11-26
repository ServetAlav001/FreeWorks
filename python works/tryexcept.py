try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
#except ZeroDivisionError:
    #print("bir sayi sifira bolunemez...")
#except ValueError:
   #print("bir sayi giriniz bir harf degil")
except Exception as ex:
    print("bir hata olustu..." , ex)
else :
    print("hersey yolunda")
finally:
    print("blok kapandı")
