from collections import deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        return self.idx < other.idx  # Heapq için karşılaştırma desteği eklendi

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            self.istasyonlar[idx] = Istasyon(idx, ad, hat)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[str]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        queue = deque([(baslangic, [baslangic.ad])])
        ziyaret_edilen = set()

        while queue:
            mevcut, rota = queue.popleft()
            if mevcut.idx == hedef.idx:
                return rota
            
            ziyaret_edilen.add(mevcut.idx)

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilen:
                    queue.append((komsu, rota + [komsu.ad]))

        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[str], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, baslangic, [baslangic.ad])]
        ziyaret_edilen = {}

        while pq:
            toplam_sure, mevcut, rota = heapq.heappop(pq)

            if mevcut.idx == hedef.idx:
                return rota, toplam_sure

            if mevcut.idx in ziyaret_edilen and ziyaret_edilen[mevcut.idx] <= toplam_sure:
                continue
            ziyaret_edilen[mevcut.idx] = toplam_sure

            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, komsu, rota + [komsu.ad]))

        return None

# Test Senaryoları
def test_senaryolari():
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    istasyonlar = [
        ("K1", "Kızılay", "Kırmızı"), ("K2", "Ulus", "Kırmızı"), ("K3", "Demetevler", "Kırmızı"), ("K4", "OSB", "Kırmızı"),
        ("M1", "AŞTİ", "Mavi"), ("M2", "Kızılay", "Mavi"), ("M3", "Sıhhiye", "Mavi"), ("M4", "Gar", "Mavi"),
        ("T1", "Batıkent", "Turuncu"), ("T2", "Demetevler", "Turuncu"), ("T3", "Gar", "Turuncu"), ("T4", "Keçiören", "Turuncu")
    ]
    for idx, ad, hat in istasyonlar:
        metro.istasyon_ekle(idx, ad, hat)

    # Bağlantılar ekleme
    baglantilar = [
        ("K1", "K2", 4), ("K2", "K3", 6), ("K3", "K4", 8),
        ("M1", "M2", 5), ("M2", "M3", 3), ("M3", "M4", 4),
        ("T1", "T2", 7), ("T2", "T3", 9), ("T3", "T4", 5),
        ("K1", "M2", 2), ("K3", "T2", 3), ("M4", "T3", 2)
    ]
    for ist1, ist2, sure in baglantilar:
        metro.baglanti_ekle(ist1, ist2, sure)

    print("\n==== Test Senaryoları ====")

    senaryolar = [
        ("M1", "K4", "1. AŞTİ'den OSB'ye"),
        ("T1", "T4", "2. Batıkent'ten Keçiören'e"),
        ("T4", "M1", "3. Keçiören'den AŞTİ'ye")
    ]

    for baslangic, hedef, aciklama in senaryolar:
        print(f"\n{aciklama}:\n")

        # En az aktarmalı rota
        rota_az_aktarma = metro.en_az_aktarma_bul(baslangic, hedef)
        if rota_az_aktarma:
            print("En az aktarmalı rota:", " -> ".join(rota_az_aktarma), end=" ")

        # En hızlı rota
        sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
        if sonuc:
            rota_hizli, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota_hizli))

# Çalıştır
test_senaryolari()
