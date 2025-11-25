
#include <iostream>
using namespace std;
struct kitap {
    string kitapadi;
    string yazaradi;
    int fiyat=0;
};
int main()
{
    int adet;
    cout << "kac kitap gireceksiniz?" << endl;
    cin >> adet;

    kitap* kitaplik = new kitap[adet];
    int pfiyat = 0;
    for (int i = 0; i < adet; i++) {
        cout <<i<< ".kitap adi:" << endl;
        cin >> kitaplik[i].kitapadi;
        cout << i << ".yazar adi:" << endl;
        cin >> kitaplik[i].yazaradi;
        cout << i << ".kitap fiyati:" << endl;
        cin >> kitaplik[i].fiyat;

    }
    for (int i = 0; i < adet; i++) {
        cout << kitaplik[i].kitapadi << " " << kitaplik[i].yazaradi << " " << kitaplik[i].fiyat << " " << endl;
        kitaplik[i].fiyat;
        if (kitaplik[i].fiyat > pfiyat) {
            pfiyat = kitaplik[i].fiyat;
        }
    }
    for (int i = 0; i < adet; i++) {
        if (kitaplik[i].fiyat == pfiyat) {
            cout << "en pahali kitap: " << kitaplik[i].kitapadi << " " << kitaplik[i].yazaradi << " " << kitaplik[i].fiyat << endl;
            break;
        }
    }
    //burada delete komutunu mutlaka calistirmalisin yoksa ramda surekli bir yer tutar
    delete[] kitaplik;
    kitaplik = nullptr;
    return 0;
}
