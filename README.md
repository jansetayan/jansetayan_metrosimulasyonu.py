# jansetayan_metrosimulasyonu.py
Metro Rota Bulucu
Bu proje, metro ağı üzerinde en hızlı ve en az aktarmalı rotayı hesaplayan bir Python programıdır. Genişlik Öncelikli Arama (BFS) ve Dijkstra Algoritması kullanılarak rotalar belirlenir.
📌 Proje Açıklaması
Bu proje, kullanıcıya iki metro istasyonu arasındaki en hızlı ve en az aktarmalı rotayı hesaplama imkanı sunar. Projede iki farklı algoritma kullanılmıştır:

Genişlik Öncelikli Arama (BFS - Breadth First Search): En az aktarmalı rotayı bulmak için kullanılır.

Dijkstra Algoritması (Min-Heap ile): En kısa sürede ulaşılacak rotayı belirlemek için kullanılır.

Metro ağında istasyonlar ve bağlantılar önceden tanımlanmıştır, ancak kullanıcı yeni istasyon ve bağlantılar ekleyerek ağı genişletebilir.
 Kurulum ve Çalıştırma
Gereksinimler
Python 3 yüklü olmalıdır.

Çalıştırma
Terminal veya komut satırında şu komutu çalıştırarak programı başlatabilirsiniz:

bash
Kopyala
Düzenle
python metro_rota.py
 Özellikler
 En az aktarmalı rota hesaplama (BFS Algoritması)
 En hızlı rota hesaplama (Dijkstra Algoritması)
 Metro ağına yeni istasyon ve bağlantı ekleme desteği


==== Test Senaryoları ====

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

