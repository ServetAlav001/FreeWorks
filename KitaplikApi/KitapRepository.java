package com.deneme.KitaplikApi.repository;

import com.deneme.KitaplikApi.model.Kitap;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

// JpaRepository<Entity Tipi, ID Tipi>
public interface KitapRepository extends JpaRepository<Kitap,Long> {
    // Spring Data JPA sayesinde, Kitap nesnesinin CRUD operasyonları
    // (kaydetme, bulma, silme) otomatik olarak sağlanmıştır.

    // Özel bir sorgu ekleyelim: Başlığa göre kitap bulma
    // Bu metodu yazmanız yeterlidir, Spring gerisini halleder!
    // List<Kitap> findByBaslik(String baslik);
    List<Kitap> findByBaslik(String baslik);
}
