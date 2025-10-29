package com.deneme.KitaplikApi.service;

import com.deneme.KitaplikApi.model.Kitap;
import com.deneme.KitaplikApi.repository.KitapRepository;

import java.util.List;
import java.util.Optional;

public class KitapService {
    private final KitapRepository kitapRepository;

    public KitapService(KitapRepository kitapRepository) {
        this.kitapRepository = kitapRepository;
    }

    // --- CRUD Metotları ---

    // Tüm kitapları getir (READ)
    public List<Kitap> tumKitaplariGetir(){
        return kitapRepository.findAll();
    }
    // Yeni kitap kaydet (CREATE)
    public Kitap kitapKaydet(Kitap kitap){
        return kitapRepository.save(kitap);
    }
    // ID ile kitap bul (READ)
    public Optional<Kitap> idKitapBul(Long id){
        return kitapRepository.findById(id);
    }
    //Kitap sil (DELETE)
    public void kitapSil(Long id){
        kitapRepository.deleteById(id);
    }
}
