# lexical.py

import re
from tokenturleri import ANAHTAR_KELIMELER, TOKEN_TURLERI

# Token'ı temsil eden sınıf
class Token:
    def __init__(self, tur, deger, konum, satir):
        self.tur = tur          # Örn: SAYI, DEGISKEN
        self.deger = deger      # Örn: "x", "42"
        self.konum = konum      # Metin içindeki pozisyon (başlangıç index'i)
        self.satir = satir      # Satır numarası

    def __repr__(self):
        return f"<{self.tur}: '{self.deger}' (Satır: {self.satir})>"

# Metni token'lara ayıran fonksiyon
def tokenize(metin):
    tokenler = []
    
    # Metni satırlara böl
    satirlar = metin.split('\n')
    
    # Tanımlar (regex desenleri)
    desenler = [
        (TOKEN_TURLERI["STRING"], r'"[^"\n]*"'),
        (TOKEN_TURLERI["SAYI"], r"\b\d+(\.\d+)?\b"),
        (TOKEN_TURLERI["DEGISKEN"], r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
        (TOKEN_TURLERI["OPERATOR"], r"(==|!=|<=|>=|[+\-*/=<>])"),
        (TOKEN_TURLERI["NOKTALAMA"], r"[{}();,]"),
        (TOKEN_TURLERI["BOSLUK"], r"\s+")
    ]

    # Her satır için token'ları bul
    for satir_no, satir in enumerate(satirlar, 1):
        konum = 0
        while konum < len(satir):
            eslesme_var = False
            for tur, desen in desenler:
                regex = re.compile(desen)
                eslesme = regex.match(satir, konum)
                if eslesme:
                    deger = eslesme.group(0)
                    # Eğer anahtar kelimeyse türünü düzelt
                    if tur == TOKEN_TURLERI["DEGISKEN"] and deger in ANAHTAR_KELIMELER:
                        tur = TOKEN_TURLERI["ANAHTAR_KELIME"]
                    tokenler.append(Token(tur, deger, konum, satir_no))
                    konum = eslesme.end()
                    eslesme_var = True
                    break
            if not eslesme_var:
                tokenler.append(Token(TOKEN_TURLERI["BILINMEYEN"], satir[konum], konum, satir_no))
                konum += 1

    return tokenler


