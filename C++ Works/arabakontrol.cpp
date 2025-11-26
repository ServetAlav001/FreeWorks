

#include <iostream>
using namespace std;
class Araba {
    private:
        int hiz;
        string marka;
    public:
        void BilgileriGetir(string markaAdi) {
            marka = markaAdi;
            hiz = 0;
        }
        void hizlan(int artis) {
            if (hiz < 200) {
                int gecicihiz = hiz;
                gecicihiz += artis;
                if (gecicihiz <= 200) {
                    hiz = gecicihiz;
                    cout << "aracin hizi arttirildi. hiziniz: " << hiz << endl;
                }
                else {
                    hiz = 200;
                    cout << "hiz sinirini astiniz hiziniz daha fazla arttirilamaz. hiziniz: " << hiz << endl;
                }
                
            }
            else {
                cout << "hiziniz arttirilamaz. hiziniz: " << hiz << endl;
            }
        }
        void frenYap(int azalis) {
            if (hiz <= 200 && 0 <= hiz) {
                int gecicihiz = hiz;
                gecicihiz -= azalis;
                if (gecicihiz < 0) {
                    hiz = 0;
                    cout << "su an durdunuz. hiziniz: " << hiz << endl;
                }
                else
                {
                    hiz = gecicihiz;
                    cout << "aracin hizi azalttildi. hiziniz: " << hiz << endl;
                }
            }
        }
        void bilgiler() {
            cout << "marka: " << marka << endl;
            cout << "hiz: " << hiz << endl;
        }
};
 

int main()
{
    Araba araba;
    string markaadi;
    cout << "arabaninizin markasi nedir?: ";
    cin >> markaadi;
    araba.BilgileriGetir(markaadi);
    string islemler = "1.islem=hizlan\n 2.islem=yavasla\n 3.islem=arac bilgileri\n q.islem=cikis yap\n";
    cout << islemler;
    string islem;
    while (true) {
        cout << "yapmak istediginiz islemi giriniz: ";
        cin >> islem;
        if (islem == "q") {
            cout << "sistemden cikiliyor..";
            break;
        }
        else if (islem == "1") {
            int hiz;
            cout << "ne kadar hiz yapacaksiniz: ";
            cin >> hiz;
            araba.hizlan(hiz);
        }
        else if (islem == "2") {
            int fren;
            cout << "ne kadar yavaslayacaksiniz: ";
            cin >> fren;
            araba.frenYap(fren);
        }
        else if (islem == "3") {
            araba.bilgiler();
        }
        else {
            cout << "yanlis bir islem girdiniz...\n";
        }
    }
}

