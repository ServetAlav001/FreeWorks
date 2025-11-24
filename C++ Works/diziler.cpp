

#include <iostream>

int main()
{
    /*double toplam = 0;
    double ortalama;
    double dersler[5];
    for (int i = 0; i < 5; i++) {
        std::cout << (i + 1) << ".inci ogrenci notu:" << std::endl;
        std::cin >> dersler[i];
        toplam += dersler[i];
    }
    ortalama = toplam / 5;
    std::cout << "ogrencilerin not ortalamasi: "<<ortalama;*/

    //Pointer belirleme
    int a = 100;
    int b = 200;
    int* p1 = &a;
    int* p2 = &b;
    int toplam;
    toplam = *p1 + *p2;
    std::cout << "toplam: " << toplam;
    *p1 = 500;
    std::cout << "\na nin yeni degeri: " << a;
    
}




