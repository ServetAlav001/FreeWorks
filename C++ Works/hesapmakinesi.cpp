#include <iostream>

int toplama(int sayi1,int sayi2) {
    int toplam = sayi1+sayi2;
    return toplam;
}
int cikarma(int sayi1,int sayi2) {
    int cikarma = sayi1-sayi2;
    return cikarma;
}
int carpma(int sayi1,int sayi2) {
    int carpma = sayi1*sayi2;
    return carpma;
}
double bolme(int sayi1,int sayi2) {
    if (sayi2==0) {
        std::cout<<"bir sayi sifira bolunemez...";
        return 0;
    }else {
        double bolme = (double)sayi1/sayi2;
        return bolme;
    }
}
int main() {
    std::cout<<"hesap makinesi\n";
    std::string islemler = "+ toplama\n"
                           "- cikarma\n"
                           "* carpma\n"
                           "/ bolme\n"
                           "q cikis\n";
    std::cout<<islemler;
    std::string islem;
    int sayi1,sayi2;
    while (true) {
        std::cout<<"yapmak istediginiz islemi seciniz:";
        std::cin>>islem;

        if (islem =="+") {
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi1;
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi2;
            std::cout<<toplama(sayi1,sayi2)<<"\n";

        }
        else if (islem =="-") {
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi1;
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi2;
            std::cout<<cikarma(sayi1,sayi2)<<"\n";
        }
        else if (islem =="*") {
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi1;
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi2;
            std::cout<<carpma(sayi1,sayi2)<<"\n";
        }
        else if (islem =="/") {
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi1;
            std::cout<<"bir sayi giriniz:";
            std::cin>>sayi2;
            std::cout<<bolme(sayi1,sayi2)<<"\n";
        }
        else if (islem =="q") {
            std::cout<<"sistemden cikiliyor...";
            break;
        }
        else {
            std::cout<<"yanlis bir islem girdiniz"<<"\n";
        }
    }

    return 0;
}
