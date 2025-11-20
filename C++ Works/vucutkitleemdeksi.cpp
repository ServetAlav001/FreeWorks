#include <iostream>
int main() {
    double kilo;
    double boy;
    double kitlendeksi;
    std::cout<<"vucut kitle endeksine hosgeldiniz...\n";

    std::cout<<"kilonuzu giriniz(kg):";
    std::cin>>kilo;
    std::cout<<"boyunuzu giriniz(cm):";
    std::cin>>boy;
    kitlendeksi=kilo / ((boy*boy)/(100*100));

    std::cout<<"vucut kitle endeksiniz: "<<kitlendeksi<<"\n";

    if (kitlendeksi>24) {
        std::cout<<"asiri kilolsunuz";

    }else if (20<=kitlendeksi && kitlendeksi<=24) {
        std::cout<<"kilonuz idealdir.";
    }else if (kitlendeksi<20) {
        std::cout<<"kilonuz cok dusuk.";
    }
}
