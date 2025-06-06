# Basit Programlama Dili Derleyicisi

Bu proje, basit bir programlama dili için lexical analyzer (sözcük çözümleyici) ve parser (sözdizimi çözümleyici) içeren bir derleyici uygulamasıdır. Tkinter kullanılarak oluşturulmuş bir GUI arayüzü ile kullanıcı dostu bir deneyim sunar.

## Özellikler

- Basit programlama dili sözdizimi desteği
- Gerçek zamanlı sözcük analizi
- Sözdizimi hata kontrolü
- Hata mesajlarında satır numarası gösterimi
- Renkli kod vurgulama
- Kullanıcı dostu arayüz

## Desteklenen Dil Özellikleri

### Veri Tipleri
- `int`: Tam sayı değerler
- `float`: Ondalıklı sayı değerler

### Değişken Tanımlama
```c
int x = 5;
float y = 3.14;
```

### Operatörler
- Aritmetik: `+`, `-`, `*`, `/`
- Karşılaştırma: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Atama: `=`

### Kontrol Yapıları
```c
if (koşul) {
    // ifade
} else {
    // ifade
}
```

### Çıktı
```c
print("Merhaba Dünya");
```

## Kurulum

1. Python 3.x'in yüklü olduğundan emin olun
2. Gerekli dosyaları indirin:
   - `tkinterapp.py`
   - `lexical.py`
   - `topdown.py`
   - `tokenturleri.py`
## 📹 Uygulama Tanıtım Videosu

[Uygulama Videosunu İzlemek İçin Tıklayın](https://www.youtube.com/watch?v=60xQ5jwCgEs)
## Kullanım

1. `tkinterapp.py` dosyasını çalıştırın:
```bash
python tkinterapp.py
```

2. Açılan arayüzde kodunuzu yazın
3. "ÇALIŞTIR" butonuna tıklayın
4. Token'lar ve varsa hata mesajları alt kısımda görüntülenecektir

![ana](https://github.com/user-attachments/assets/72312ab9-fe23-48f6-89d7-27740803c36c)

## Token Desenleri

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

## Hata Mesajları

Program, kodunuzdaki hataları satır numarasıyla birlikte gösterir. Örnek hata mesajları:

- Eksik noktalı virgül: `HATA (Satır 1): 'x' tanımlaması sonunda ';' bekleniyordu.`
- Eksik parantez: `HATA (Satır 3): print ifadesinde '(' eksik.`
- Geçersiz ifade: `HATA (Satır 2): Geçersiz ifade başlangıcı: <ANAHTAR_KELIME: 'int'>`
![hatali](https://github.com/user-attachments/assets/2899f10e-fead-4d85-b100-57b01499a34b)
## DOĞRU ÖRNEK
![dogru](https://github.com/user-attachments/assets/d1d74c34-8c94-4de1-bfbd-b5991e629464)


## Örnek Kod

```c
int x = 3;
float y = 2.5;
x = x + 5;
if (x > 5) {
    print("merhaba");
} else {
    print("naber");
}
```

## Geliştirici

Bu proje Levent Kutay Sezer tarafından geliştirilmiştir.

## Lisans

Bu proje özel kullanım içindir. 


