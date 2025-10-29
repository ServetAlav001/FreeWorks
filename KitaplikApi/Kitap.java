package com.deneme.KitaplikApi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity// Bu sınıfın bir veritabanı tablosunu temsil ettiğini belirtir
@Data // Lombok: Getter, Setter, toString, equals/hashCode oluşturur
@NoArgsConstructor // Lombok: Parametresiz yapıcı metot oluşturur
@AllArgsConstructor // Lombok: Tüm alanları içeren yapıcı metot oluşturur
public class Kitap {
    @Id // Birincil anahtarı (Primary Key) belirtir
    @GeneratedValue(strategy = GenerationType.IDENTITY)// ID'nin otomatik oluşturulacağını belirtir
    private long id;
    private String baslik;
    private String yazar;
    private int yayinyili;
}
