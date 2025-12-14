import requests

def hava_durumu_ogren():
    #API Ayarları
    api_key ="*****************"

    #Kullanıcıdan şehir adı alma
    sehir = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&lang=tr&units=metric"

    #sonucuya erişme
    cevap = requests.get(url)
    #JSON formatında veriyi alma
    if cevap.status_code == 200:
        veri=cevap.json()
        sehir_adi = veri['name']
        sicaklik = veri['main']['temp']
        hava_durumu = veri['weather'][0]['description']
        nem = veri['main']['humidity']
        rüzgar_hizi = veri['wind']['speed']
        print(f"{sehir_adi} için hava durumu:")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Hava Durumu: {hava_durumu}")
        print(f"Nem: {nem}%")
        print(f"Rüzgar Hızı: {rüzgar_hizi} m/s")
    else:
        if cevap.status_code == 404:
            print("Şehir bulunamadı. Lütfen geçerli bir şehir adı girin.")
        elif cevap.status_code == 401:
            print("Geçersiz API anahtarı. Lütfen API anahtarınızı kontrol edin.")
        else:
            print("Hava durumu verisi alınırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
if __name__ == "__main__":
    hava_durumu_ogren()
