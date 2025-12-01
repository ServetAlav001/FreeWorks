sinir = int(input("kaca kadarki fibonacci sayilarini blmak istiyorsunuz: "))
def fibonacci_generator(sinir):
    sayi_bir=1
    sayi_iki=1
    while sayi_bir<=sinir:
        yield sayi_bir
        sayi_bir,sayi_iki=sayi_iki,sayi_iki+sayi_bir

for fibonacci in fibonacci_generator(sinir):
    print(fibonacci)
