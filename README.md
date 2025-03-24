# jansetayan_metrosimulasyonu.py
Metro Rota Bulucu, bir metro ağında istasyonlar arasında en hızlı veya en az aktarmalı rotayı bulmanızı sağlayan bir Python programıdır. Program, bir graf veri yapısı kullanarak istasyonları ve bağlantıları yönetir.

📌 Proje Açıklaması
Bu proje, kullanıcıya iki metro istasyonu arasındaki en hızlı ve en az aktarmalı rotayı hesaplama imkanı sunar. Projede iki farklı algoritma kullanılmıştır:

Genişlik Öncelikli Arama (BFS - Breadth First Search): En az aktarmalı rotayı bulmak için kullanılır.

Dijkstra Algoritması (Min-Heap ile): En kısa sürede ulaşılacak rotayı belirlemek için kullanılır.

Metro ağında istasyonlar ve bağlantılar önceden tanımlanmıştır, ancak kullanıcı yeni istasyon ve bağlantılar ekleyerek ağı genişletebilir.

🛠 Kullanılan Teknolojiler
Bu projede Python 3 programlama dili ve aşağıdaki kütüphaneler kullanılmıştır:

collections.deque → BFS algoritması için (en az aktarmalı rota)

heapq → Dijkstra algoritması için (en hızlı rota)

typing → Tip ipuçları için (Kodun okunabilirliğini artırmak amacıyla)

📥 Kurulum ve Çalıştırma
1️⃣ Gerekli Kütüphaneleri Kontrol Edin
Bu proje için ekstra bir kütüphane yüklemenize gerek yoktur. Python 3 yüklü olduğundan emin olun.

2️⃣ Projeyi Çalıştırın
Terminal veya komut satırında şu komutu çalıştırarak programı başlatabilirsiniz:

bash
Kopyala
Düzenle
python metro_rota.py
Bu komut, metro ağı için tanımlanmış test senaryolarını çalıştırır ve en uygun rotaları terminalde görüntüler.

🚆 Kullanım
Metro Ağına İstasyon ve Bağlantı Ekleme
Programda bir metro ağı tanımlanır ve istasyonlar bir sınıf (class) yapısıyla oluşturulur.

İstasyon Ekleme: Yeni bir istasyon eklemek için istasyon_ekle() fonksiyonu kullanılır.

Bağlantı Ekleme: İki istasyon arasında bir bağlantı oluşturmak için baglanti_ekle() fonksiyonu kullanılır.

En Az Aktarmalı ve En Hızlı Rota Hesaplama
Program, aşağıdaki fonksiyonları kullanarak iki istasyon arasındaki en uygun rotaları belirler:

1️⃣ en_az_aktarmalı_rota_bul(baslangic_id, hedef_id)

En az aktarma yapılan rotayı belirler.

BFS (Breadth First Search) algoritması kullanılarak hesaplanır.

2️⃣ en_hizli_rota_bul(baslangic_id, hedef_id)

En kısa sürede ulaşılacak rotayı belirler.

Dijkstra Algoritması (Min-Heap ile) kullanılarak hesaplanır.
