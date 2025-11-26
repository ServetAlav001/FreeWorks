try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("bir sayi sifira bolunemez...")
except ValueError:
    print("bir sayi giriniz bir harf degil")
