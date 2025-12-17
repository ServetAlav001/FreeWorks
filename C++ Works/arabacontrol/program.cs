#include <iostream>
using namespace std;
class Araba {
protected:
    int hiz;
    string marka;
    int limit;
public:
    Araba(string gelenMarka, int maxhiz) {
        marka = gelenMarka;
        limit = maxhiz;
        hiz = 0;
    }
    void hizlan(int hizartis) {
        if (hiz < limit) {
            int gecicihiz = hiz + hizartis;
            if (gecicihiz >= limit) {
                hiz = limit;
                cout << "hiz limitinize ulastiniz. hiziniz: " << hiz << endl;
            }
            else {
                hiz = gecicihiz;
                cout << "su anki hiziniz: " << hiz << endl;
            }
        }
        else {
            cout << "hiz limitine ulastiniz. hizinizi arttiramazsiniz. hiziniz: " << hiz << endl;
        }
    }
    void frenyap(int hizazalis) {
        if (hizazalis < 0) {
            cout << "negatif bir frenleme yapamazsiniz.." << endl;
        }
        else {
            int gecicihiz = hiz - hizazalis;
            if (gecicihiz < 0) {
                hiz = 0;
                cout << "hizniz suan sifirlandi.hiziniz: " << hiz << endl;

            }
            else {
                hiz = gecicihiz;
                cout << "suanki hiziniz: " << hiz << endl;
            }
        }
    }
    void bilgiler() {
        cout << "marka: " << marka << endl;
        cout << "hiz: " << hiz << endl;
    }
};
class Kamyon : public Araba {
    int yuk=0;
    int yuklimit;
    public:
        Kamyon(string gelenMarka, int maxhiz,int yuklimiti):Araba(marka,maxhiz){
            yuklimit = yuklimiti;
        }
        void yukbindir(int yukyukle) {
            int geciciyuk = yukyukle + yuk;
            if (geciciyuk >= yuklimit) {
                yuk = yuklimit;
                cout << "yuk limitine ulastiniz. yukunuz: " << yuk << endl;
            }
            else {
                yuk = geciciyuk;
                cout << "yukunuz: " << yuk << endl;
            }
        }
        void yukindir(int indirilecekyuk) {
            if (indirilecekyuk < 0) {
                cout << "negatif bir yuk degeri giremezsiniz." << endl;
            }
            else {
                int geciciyuk = yuk - indirilecekyuk;
                if (geciciyuk < 0) {
                    yuk = 0;
                    cout << "yukunuz sifirlandi." << endl;
                }
                else {
                    yuk = geciciyuk;
                    cout << "yuk indirildi. yukunuz:" << yuk << endl;
                }
            }
        }
        void bilgiler() {
            cout << "marka: " << marka << endl;
            cout << "hiz: " << hiz << endl;
            cout << "yuk: " << yuk << endl;
        }
};
int main()
{
    cout << "--------------------------"<<endl;
    cout << "araba tanima sistemi" << endl;
    cout << "--------------------------"<<endl;
    string islemler1 = "1.islem: araba ekle\n2.islem: kamyon ekle\n";
    string islemler2 = "1.islem: bilgileri getir\n2.islem:hizlan\n3.islem: fren yap\n4.islem:islemler\nq.islem: cikis yap\n";
    string islemler3 = "1.islem: bilgileri getir\n2.islem:hizlan\n3.islem: fren yap\n4.islem:yuk bindir\n5.islem:yuk indir\n6.islem:islemler\nq.islem: cikis yap\n";
    cout << islemler1;
    
    string islem;
    cout << "yapmak istediginiz islemi giriniz:"<<endl;
    cin >> islem;
    if (islem == "1") {
        string markaadi;
        int hiz;
        int limit;
        cout << "bir marka adi giriniz: ";
        cin >> markaadi;
        cout << "hiz limit giriniz: " << endl;;
        cin >> limit;
        
        Araba araba = Araba(markaadi, limit);
        cout << islemler2;
        while (true) {
            string islem1;
            cout << "yapmak istediginiz islemi giriniz: "<<endl;
            cin >> islem1;
            if (islem1 == "q") {
                cout << "cikis yapiliyor..";
                break;
            }
            else if (islem1 == "1") {
                araba.bilgiler();
            }
            else if (islem1 == "2") {
                int hiz;
                cout << "ne kadar hizlanmak istersin?: " << endl;
                cin >> hiz;
                araba.hizlan(hiz);
            }
            else if (islem1 == "3") {
                int fren;
                cout << "ne kadar yavaslamak istersin?: "<<endl;
                cin >> fren;
                araba.frenyap(fren);
            }
            else if (islem1 == "4") {
                cout << islemler2;
            }
            else {
                cout << "yanlis bir islem girdiniz.." << endl;
            }
            
        }
    
    }
    else if (islem == "2") {
        string markaadi;
        int hiz;
        int limit;
        int yuklimit;
        cout << "bir marka adi giriniz: "<<endl;
        cin >> markaadi;
        cout << "hiz limit giriniz: "<<endl;
        cin >> limit;
        cout << "yuklimiti giriniz: "<<endl;
        cin >> yuklimit;
        Kamyon kamyon = Kamyon(markaadi, limit, yuklimit);
        cout << islemler3;
        while (true) {
            string islem2;
            cout << "yapmak istediginiz islemi giriniz: "<<endl;
            cin >> islem2;
            if (islem2 == "q") {
                cout << "cikis yapiliyor...";
                break;
            }
            else if (islem2 == "1") {
                kamyon.bilgiler();
            }
            else if (islem2 == "2") {
                int hiz;
                cout << "ne kadar hizlanmak istersin?: "<<endl;
                cin >> hiz;
                kamyon.hizlan(hiz);
            }
            else if (islem2 == "3") {
                int fren;
                cout << "ne kadar yavaslamak istersin?: " << endl;
                cin >> fren;
                kamyon.frenyap(fren);
            }
            else if (islem2 == "4") {
                int yuk;
                cout << "ne kadar yuk yuklemek istersin?: " << endl;
                cin >> yuk;
                kamyon.yukbindir(yuk);
            }
            else if (islem2 == "5") {
                int yuk;
                cout << "ne kadar yuk indirmek istersin?: " << endl;
                cin >> yuk;
                kamyon.yukindir(yuk);
            }
            else if (islem2 == "6") {
                cout << islemler3;
            }
            else {
                cout << "yanlis bir islem girdiniz.." << endl;
            }
        }
    }
    else {
        cout << "yanlis bir islem girdiniz.." << endl;
    }

}


