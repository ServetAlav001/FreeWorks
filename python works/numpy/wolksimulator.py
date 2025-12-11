import numpy as np
import matplotlib.pyplot as plt
N = 10000  # Number of simulation steps
adimlar_x=np.random.choice([-1,1],size=N)
adimlar_y=np.random.choice([-1,1],size=N)
#print("X yönündeki adımlar:\n",adimlar_x)
#print("Y yönündeki adımlar:\n",adimlar_y)

x_koordinat=np.cumsum(adimlar_x)
y_koordinat=np.cumsum(adimlar_y)

konumlar_x=np.insert(x_koordinat,0,0)
konumlar_y=np.insert(y_koordinat,0,0)
print("X koordinatları:\n",x_koordinat)
print("Y koordinatları:\n",y_koordinat)

plt.figure(figsize=(8,8))
plt.plot(konumlar_x, konumlar_y, linestyle='-', color='blue', linewidth=1, alpha=0.7)
plt.plot(konumlar_x[0], konumlar_y[0], 'go', label='Başlangıç (0,0)')
plt.plot(konumlar_x[-1], konumlar_y[-1], 'ro', label='Bitiş Noktası')
plt.title("2B Random Yürüyüş Simülasyonu",fontsize=16)
plt.xlabel("X Koordinatı",fontsize=14)
plt.ylabel("Y Koordinatı",fontsize=14)
plt.grid(True,which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis("equal")
plt.show()
plt.savefig("2B_Random_Yuruyus_Simulasyonu.png")
print("Final X Position:", konumlar_x[-1])
print("Final Y Position:", konumlar_y[-1])

x_sonkonum=konumlar_x[-1]
y_sonkonum=konumlar_y[-1]
uzaklik=np.sqrt(x_sonkonum**2 + y_sonkonum**2)
print("Başlangıç noktasından uzaklık:",uzaklik)
N_TEKRAR = 100
son_mesafeler = []

for _ in range(N_TEKRAR):
    # Yeni bir simülasyon için rastgele adımlar oluştur
    adımlar_x = np.random.choice([-1, 1], size=N)
    adımlar_y = np.random.choice([-1, 1], size=N)

    # Konumları hesapla
    konumlar_x = np.cumsum(adımlar_x)
    konumlar_y = np.cumsum(adımlar_y)

    # Son X ve Y konumlarını al
    son_x = konumlar_x[-1]
    son_y = konumlar_y[-1]

    # Mesafeyi hesapla ve listeye ekle
    mesafe = np.sqrt(son_x**2 + son_y**2)
    son_mesafeler.append(mesafe)

# NumPy dizisine çevirerek ortalama ve standart sapmayı hesapla
son_mesafeler_np = np.array(son_mesafeler)

print("\n--- Çoklu Simülasyon Analizi ---")
print(f"Toplam {N_TEKRAR} adet Rastgele Yürüyüş Simülasyonu çalıştırıldı.")
print(f"Ortalama Bitiş Mesafesi (Ortalama D): {np.mean(son_mesafeler_np):.2f} birim")
print(f"Mesafelerin Standart Sapması: {np.std(son_mesafeler_np):.2f}")
