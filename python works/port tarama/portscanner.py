import socket
from datetime import datetime
import sys

#baslık
def baslik():
    print("-" * 50)
    print("Port Tarayıcı".center(50))
    print("Tarih ve Saat: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(50))
    print("-" * 50)

baslik()
# Kullanıcıdan hedef IP veya Site adresi alalım
hedefadress = input("Hedef IP adresi veya Site Adresi (örnek: www.ornek.com): ")

# Adresi IP'ye çevirelim (DNS Çözümleme)
try:
    hedef_ip = socket.gethostbyname(hedefadress)
    print("-" * 50)
    print(f"hedef taraniyor...{hedef_ip}")
    print("tarama basladi..."+ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("-" * 50)
except socket.gaierror:
    print("Hedef bulunamadi. Lütfen geçerli bir IP adresi veya site adı girin.")
    sys.exit()
# Port tarama fonksiyonu
try:
    for port in range(1,1025):
        # Socket oluşturuyoruz (IPv4 ve TCP kullanacağız)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Hızlanması için zaman aşımı süresi (0.5 saniye cevap bekle, gelmezse geç)
        sock.settimeout(0.3)
        # Bağlanmayı dene
        result = sock.connect_ex((hedef_ip, port))
        if result == 0:
            print(f"Port {port}: Açık")
        sock.close()
except KeyboardInterrupt:
    print("\nTarama kullanıcı tarafından iptal edildi.")
    sys.exit()
except socket.error:
    print("Bağlantı hatası. Hedefe bağlanılamıyor.")
    sys.exit()
print("-" * 50)
print("Tarama tamamlandı.".center(50))
