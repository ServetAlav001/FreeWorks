#include <iostream>
using namespace std;
void degistir(int &sayi1, int &sayi2) {
    int gecici = sayi1;

    sayi1 = sayi2;
    sayi2 = gecici;
    cout << "fonk. ici---> x: " << sayi1 << " y: " << sayi2 << endl;

}
int main()
{
    int x = 10;
    int y = 20;
    cout<< "Baslangic - x: " << x << " y: " << y << endl;
    degistir(x, y);
    cout << "Bitis - x: " << x << " y: " << y << endl;
    return 0;
}
