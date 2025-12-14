import requests as req
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


url="https://www.tevhidkitap.net/?srsltid=AfmBOopC4hcSRdoaoeRj5ChvudDzNB1oZw61FXnWwDxEsLLN9F_rMKJY"

# Web sayfasına GET isteği gönderme
try:
    response = req.get(url)
    response.raise_for_status() # HTTP hatası varsa istisna fırlatır
    html_icerik = response.text# Web sayfasının HTML içeriği
except req.exceptions.RequestException as e:
    print(f"İstek sırasında bir hata oluştu: {e}")
    exit()

soup = BeautifulSoup(html_icerik, 'html.parser')
basliklar=soup.find_all('div', class_='caption')
# Başlıkları ekrana yazdırma ve dosyaya kaydetme
for baslik in basliklar:
    kitapbasligi=baslik.find('h4').text
    print(kitapbasligi)
    with open("kitapbaslıkları.txt","a",encoding="utf-8") as fileYAZ:
        with open("kitapbaslıkları.txt","r",encoding="utf-8") as fileOKU:
            if kitapbasligi+"\n" not in fileOKU.readlines():
                fileYAZ.write(kitapbasligi+"\n")
# Fiyatları ekrana yazdırma ve dosyaya kaydetme
fiyatlar=soup.find_all("span", class_="price-new")
for fiyat in fiyatlar:
    kitapfiyati=fiyat.text
    print(kitapfiyati)
    with open("kitapfiyatları.txt","a",encoding="utf-8") as fileYAZ:
        with open("kitapfiyatları.txt","r",encoding="utf-8") as fileOKU:
            if kitapfiyati+"\n" not in fileOKU.readlines():
                fileYAZ.write(kitapfiyati+"\n")
