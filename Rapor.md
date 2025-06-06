# Basit Programlama Dili Derleyicisi Projesi Raporu

## 1. Giriş

### 1.1 Projenin Amacı
Bu proje, basit bir programlama dili için lexical analyzer (sözcük çözümleyici) ve parser (sözdizimi çözümleyici) geliştirmeyi amaçlamaktadır. Proje, kullanıcıların basit programlama yapılarını (değişken tanımlama, kontrol yapıları, aritmetik işlemler) kullanarak kod yazabilmelerini ve bu kodların sözdizimi analizini gerçekleştirebilmelerini sağlar.

### 1.2 Kullanılan Teknolojiler
- **Python 3.x**: Ana programlama dili
- **Tkinter**: Grafiksel kullanıcı arayüzü için
- **Regular Expressions (re)**: Lexical analiz için
- **Top-down Parsing**: Sözdizimi analizi için

### 1.3 Projenin Kapsamı
Proje, aşağıdaki temel bileşenleri içermektedir:
- Lexical analyzer (Sözcük çözümleyici)
- Parser (Sözdizimi çözümleyici)
- Grafiksel kullanıcı arayüzü
- Hata yakalama ve raporlama sistemi
- Kod vurgulama sistemi

## 2. Tasarım ve Mimari

### 2.1 Lexical Analyzer (lexical.py)
Lexical analyzer, kaynak kodu token'lara ayıran bileşendir.

#### 2.1.1 Token Sınıfı
```python
class Token:
    def __init__(self, tur, deger, konum, satir):
        self.tur = tur          # Token türü
        self.deger = deger      # Token değeri
        self.konum = konum      # Metin içindeki konumu
        self.satir = satir      # Satır numarası
```

#### 2.1.2 Token Türleri
- ANAHTAR_KELIME: if, else, while, return, int, float, print
- DEGISKEN: Değişken isimleri
- SAYI: Sayısal değerler
- OPERATOR: +, -, *, /, =, >, <, >=, <=, ==, !=
- NOKTALAMA: {, }, (, ), ;, ,
- STRING: Metin değerleri
- BOSLUK: Boşluk karakterleri
- BILINMEYEN: Tanımlanamayan karakterler

#### 2.1.3 Regex Desenleri
```python
desenler = [
    (TOKEN_TURLERI["STRING"], r'"[^"\n]*"'),
    (TOKEN_TURLERI["SAYI"], r"\b\d+(\.\d+)?\b"),
    (TOKEN_TURLERI["DEGISKEN"], r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    (TOKEN_TURLERI["OPERATOR"], r"(==|!=|<=|>=|[+\-*/=<>])"),
    (TOKEN_TURLERI["NOKTALAMA"], r"[{}();,]"),
    (TOKEN_TURLERI["BOSLUK"], r"\s+")
]
```

### 2.2 Parser (topdown.py)
Parser, token'ları alıp sözdizimi analizini gerçekleştiren bileşendir.

#### 2.2.1 Parser Sınıfı
```python
class Parser:
    def __init__(self, tokenler):
        self.tokenler = tokenler
        self.index = 0
        self.current = self.tokenler[self.index] if self.tokenler else None
        self.has_error = False
        self.hata_mesajlari = []
```

#### 2.2.2 Sözdizimi Analizi
Parser aşağıdaki yapıları analiz edebilir:
- Değişken tanımlamaları
- Atama ifadeleri
- Aritmetik ifadeler
- Karşılaştırma ifadeleri
- If-else yapıları
- Print ifadeleri

#### 2.2.3 Hata Yönetimi
- Satır numarası ile hata raporlama
- Detaylı hata mesajları
- Hata durumunda kurtarma mekanizması

### 2.3 GUI (tkinterapp.py)
Kullanıcı arayüzü, Tkinter kullanılarak geliştirilmiştir.

#### 2.3.1 Arayüz Bileşenleri
- Kod giriş alanı
- Token gösterim alanı
- Sonuç gösterim alanı
- Çalıştır butonu

#### 2.3.2 Kod Vurgulama
- Anahtar kelimeler: Turuncu
- Değişkenler: Mavi
- Sayılar: Yeşil
- Operatörler: Mor
- Stringler ve noktalama: Kırmızı

## 3. Uygulama Detayları

### 3.1 Desteklenen Dil Özellikleri

#### 3.1.1 Veri Tipleri
- int: Tam sayı değerler
- float: Ondalıklı sayı değerler

#### 3.1.2 Operatörler
- Aritmetik: +, -, *, /
- Karşılaştırma: >, <, >=, <=, ==, !=
- Atama: =

#### 3.1.3 Kontrol Yapıları
- if-else yapısı
- Blok yapısı ({ })

### 3.2 Hata Yakalama ve Raporlama
- Sözdizimi hataları
- Eksik noktalı virgül
- Eksik parantez
- Geçersiz ifadeler
- Satır numarası ile hata gösterimi

### 3.3 Kod Vurgulama Sistemi
- Gerçek zamanlı renklendirme
- Token türüne göre renk atama
- Görsel geri bildirim

## 4. Test ve Sonuçlar

### 4.1 Test Senaryoları

#### 4.1.1 Değişken Tanımlama
```c
int x = 5;
float y = 3.14;
```
Sonuç: Başarılı

#### 4.1.2 If-Else Yapısı
```c
if (x > 5) {
    print("merhaba");
} else {
    print("naber");
}
```
Sonuç: Başarılı

#### 4.1.3 Hatalı Kod
```c
int x = 5  // Eksik noktalı virgül
```
Sonuç: Hata mesajı - "HATA (Satır 1): 'x' tanımlaması sonunda ';' bekleniyordu."

### 4.2 Performans
- Lexical analiz: O(n) karmaşıklığı
- Parsing: O(n) karmaşıklığı
- GUI güncellemeleri: Gerçek zamanlı

## 5. Zorluklar ve Çözümler

### 5.1 Karşılaşılan Zorluklar
1. Satır numarası takibi
2. Hata mesajlarının doğru konumlandırılması
3. Kod vurgulama sisteminin implementasyonu

### 5.2 Uygulanan Çözümler
1. Token sınıfına satır numarası eklendi
2. Hata mesajları satır numarası ile birlikte gösteriliyor
3. Tkinter'ın tag sistemi kullanılarak kod vurgulama implementasyonu yapıldı

### 5.3 Öğrenilen Dersler
- Lexical analiz ve parsing teknikleri
- GUI geliştirme
- Hata yönetimi
- Kod organizasyonu

## 6. Sonuç ve Gelecek Planları

### 6.1 Projenin Başarısı
- Temel programlama yapılarının analizi
- Kullanıcı dostu arayüz
- Doğru hata raporlama
- Etkili kod vurgulama

### 6.2 Geliştirilebilecek Alanlar
1. Daha fazla veri tipi desteği
2. Fonksiyon tanımlama
3. Döngü yapıları
4. Daha gelişmiş hata düzeltme önerileri

### 6.3 Gelecek Özellikler
1. While döngüsü desteği
2. For döngüsü desteği
3. Fonksiyon tanımlama ve çağırma
4. Dizi ve liste desteği
5. Otomatik kod tamamlama

## 7. Kaynakça

1. Python Documentation: https://docs.python.org/
2. Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
3. Regular Expressions: https://docs.python.org/3/library/re.html
4. Compiler Design Principles: Aho, Lam, Sethi, Ullman

## 8. Ekler

### 8.1 Proje Yapısı
```
proje/
├── tkinterapp.py    # GUI uygulaması
├── lexical.py       # Lexical analyzer
├── topdown.py       # Parser
├── tokenturleri.py  # Token tanımlamaları
└── README.md        # Proje dokümantasyonu
```

### 8.2 Kullanım Örnekleri
Detaylı kullanım örnekleri README.md dosyasında bulunmaktadır. 