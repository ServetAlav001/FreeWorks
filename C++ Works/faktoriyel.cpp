#include <iostream>
int main() {
    int sayi;
    int sonuc=1;
    std::cout<<"faktoriyel hesaplama programi\n";
    std::cout<<"hesaplamak istediginiz sayiyi giriniz:  ";
    std::cin>>sayi;
    if (sayi<0) {
        std::cout<<"0 dan kucuk bir deger girmeyiniz.";

    }else {
        for (int i = 1; i <= sayi; i++) {
            sonuc*=i;
        }
        std::cout<<"sonuc: "<< sonuc;
    }
    return 0;
}
