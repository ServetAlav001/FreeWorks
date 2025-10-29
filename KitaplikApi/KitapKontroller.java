package com.deneme.KitaplikApi.controller;

import com.deneme.KitaplikApi.model.Kitap;
import com.deneme.KitaplikApi.service.KitapService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController // Bu sınıfın REST API isteklerini karşılayacağını belirtir
@RequestMapping("/api/kitaplar") // Tüm metotların başlangıç yolu
public class KitapKontroller {
    private final KitapService kitapService;

    public KitapKontroller(KitapService kitapService) {
        this.kitapService = kitapService;
    }
    @GetMapping
    public List<Kitap> tumKitaplar(){
        return kitapService.tumKitaplariGetir();
    }
    // POST /api/kitaplar
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED) // Başarılıysa 201 Created döner
    public Kitap kitapEkle(@RequestBody Kitap kitap){
        return kitapService.kitapKaydet(kitap);
    }
    // GET /api/kitaplar/{id}
    @GetMapping("/{id}")
    public ResponseEntity<Kitap> idKitapGetir(@PathVariable Long id){
        // Hata yönetimi için ResponseEntity kullanıyoruz
        return kitapService.idKitapBul(id)
                .map(ResponseEntity::ok)// Bulunursa 200 OK ve kitabı döner
                .orElseGet(()-> ResponseEntity.notFound().build());// Bulunmazsa 404 Not Found döner
    }
    // DELETE /api/kitaplar/{id}
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)// Başarılı silme için 204 No Content döner
    public void kitapSil(@PathVariable Long id) {
        kitapService.kitapSil(id);
    }
}
