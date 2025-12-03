# Simülasyon için global değişken
# Bunu True yaparsan kod çalışır, False yaparsan hata verir.
kullanici_giris_yapti = False 

# --- DEKORATÖR TANIMLAMASI ---
def yetki_kontrol(fonksiyon):
    # 'fonksiyon' parametresi, süslediğimiz 'gizli_sayfa' fonksiyonudur.
    
    print(">> Dekoratör devreye girdi ve sarmalayıcıyı hazırladı...")
    
    def sarmalayici():
        print(">> Kontrol yapılıyor...")
        
        if kullanici_giris_yapti:
            print(">> İZİN VERİLDİ.")
            # Asıl fonksiyon (gizli_sayfa) burada çalıştırılıyor!
            fonksiyon() 
        else:
            print(">> ERİŞİM ENGELİ: Lütfen önce giriş yapınız!")
            # Dikkat et: 'fonksiyon()' çağrılmadığı için asıl kod çalışmaz.
            
    # Oluşturduğumuz sarmalayıcıyı (wrapper) dışarı fırlatıyoruz.
    return sarmalayici

# --- DEKORATÖRÜN UYGULANMASI ---
# Python bunu görünce şunu yapar:
# gizli_sayfa = yetki_kontrol(gizli_sayfa)
@yetki_kontrol
def gizli_sayfa():
    print("-" * 30)
    print("TEBRİKLER! GİZLİ ADMİN PANELİNDESİNİZ.")
    print("-" * 30)

# --- TEST ---
print("\n1. Deneme (Giriş Yok):")
gizli_sayfa() # Aslında biz burada 'sarmalayici'yı çalıştırıyoruz.

print("\n\n2. Deneme (Giriş Yapıldı):")
kullanici_giris_yapti = True # Değişkeni değiştirdik
gizli_sayfa()
