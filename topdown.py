from lexical import tokenize
from tokenturleri import TOKEN_TURLERI

class Parser:
    def __init__(self, tokenler):
        self.tokenler = tokenler
        self.index = 0
        self.current = self.tokenler[self.index] if self.tokenler else None
        self.has_error = False
        self.hata_mesajlari = []

    def advance(self):
        self.index += 1
        self.current = self.tokenler[self.index] if self.index < len(self.tokenler) else None

    def skip_whitespace(self):
        while self.current and self.current.tur == TOKEN_TURLERI["BOSLUK"]:
            self.advance()

    def parse(self):
      while self.current is not None:
        self.skip_whitespace()
        if self.current is None:
            break

        başlangıç_index = self.index
        self.parse_statement()

        # Eğer hata olduysa buradaki statement'ı atla
        if self.has_error:
            self.has_error = False  # Resetle ki diğer hataları da görebilelim
            while self.current and self.current.deger != ';':
                self.advance()
            if self.current and self.current.deger == ';':
                self.advance()
        else:
            # Normal durumda da statement sonrası ';' varsa geç
            if self.current and self.current.deger == ';':
                self.advance()



    def parse_statement(self):
        self.skip_whitespace()

        # Değişken tanımlama (int veya float)
        if self.current.tur == TOKEN_TURLERI["ANAHTAR_KELIME"] and self.current.deger in ["int", "float"]:
            tip = self.current.deger
            self.advance()
            self.skip_whitespace()

            if not self.current or self.current.tur != TOKEN_TURLERI["DEGISKEN"]:
                mesaj = f"HATA (Satır {self.current.satir}): {tip} tanımlamasından sonra değişken adı bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            degisken = self.current.deger
            self.advance()
            self.skip_whitespace()

            if not self.current or self.current.deger != '=':
                mesaj = f"HATA (Satır {self.current.satir}): '{degisken}' değişkeni için '=' bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            self.advance()
            self.skip_whitespace()
            self.parse_expression()
            self.skip_whitespace()

            if not self.current or self.current.deger != ';':
                mesaj = f"HATA (Satır {self.current.satir}): '{degisken}' tanımlaması sonunda ';' bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            self.advance()

        # PRINT ifadesi
        elif self.current.tur == TOKEN_TURLERI["ANAHTAR_KELIME"] and self.current.deger == "print":
            self.advance()
            self.skip_whitespace()

            if not self.current or self.current.deger != "(":
                mesaj = f"HATA (Satır {self.current.satir}): print ifadesinde '(' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            if self.current and self.current.tur in [TOKEN_TURLERI["SAYI"], TOKEN_TURLERI["DEGISKEN"], TOKEN_TURLERI["STRING"]]:
                self.advance()
            else:
                mesaj = f"HATA (Satır {self.current.satir}): print ifadesinde içerik eksik veya hatalı."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            self.skip_whitespace()
            if not self.current or self.current.deger != ")":
                mesaj = f"HATA (Satır {self.current.satir}): print ifadesinde ')' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            if not self.current or self.current.deger != ";":
                mesaj = f"HATA (Satır {self.current.satir}): print ifadesinden sonra ';' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

        # IF-ELSE ifadesi
        elif self.current.tur == TOKEN_TURLERI["ANAHTAR_KELIME"] and self.current.deger == "if":
            self.advance()
            self.skip_whitespace()

            if not self.current or self.current.deger != "(":
                mesaj = f"HATA (Satır {self.current.satir}): if ifadesinde '(' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            # Koşul ifadesini parse et
            self.parse_expression()
            self.skip_whitespace()

            if not self.current or self.current.deger != ")":
                mesaj = f"HATA (Satır {self.current.satir}): if ifadesinde ')' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            self.skip_whitespace()
            if not self.current or self.current.deger != "{":
                mesaj = f"HATA (Satır {self.current.satir}): if bloğunda '{{' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            # if bloğunu parse et
            while self.current and self.current.deger != "}":
                self.parse_statement()
                self.skip_whitespace()

            if not self.current or self.current.deger != "}":
                mesaj = f"HATA (Satır {self.current.satir}): if bloğunda '}}' eksik."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()

            # else bloğunu kontrol et
            self.skip_whitespace()
            if self.current and self.current.tur == TOKEN_TURLERI["ANAHTAR_KELIME"] and self.current.deger == "else":
                self.advance()
                self.skip_whitespace()

                if not self.current or self.current.deger != "{":
                    mesaj = f"HATA (Satır {self.current.satir}): else bloğunda '{{' eksik."
                    self.hata_mesajlari.append(mesaj)
                    self.has_error = True
                    return
                self.advance()

                # else bloğunu parse et
                while self.current and self.current.deger != "}":
                    self.parse_statement()
                    self.skip_whitespace()

                if not self.current or self.current.deger != "}":
                    mesaj = f"HATA (Satır {self.current.satir}): else bloğunda '}}' eksik."
                    self.hata_mesajlari.append(mesaj)
                    self.has_error = True
                    return
                self.advance()

        # DEĞİŞKEN atama ifadesi
        elif self.current.tur == TOKEN_TURLERI["DEGISKEN"]:
            degisken = self.current.deger
            self.advance()
            self.skip_whitespace()

            if not self.current or self.current.deger != '=':
                mesaj = f"HATA (Satır {self.current.satir}): '{degisken}' değişkeni için '=' bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            self.advance()
            self.skip_whitespace()
            self.parse_expression()
            self.skip_whitespace()

            if not self.current or self.current.deger != ';':
                mesaj = f"HATA (Satır {self.current.satir}): '{degisken}' ataması sonunda ';' bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return

            self.advance()

        else:
            mesaj = f"HATA (Satır {self.current.satir}): Geçersiz ifade başlangıcı: {self.current}"
            self.hata_mesajlari.append(mesaj)
            self.has_error = True
            self.advance()

    def parse_expression(self):
        self.skip_whitespace()
        self.parse_term()
        self.skip_whitespace()
        
        # Karşılaştırma operatörleri
        while self.current and not self.has_error and self.current.tur == TOKEN_TURLERI["OPERATOR"] and self.current.deger in ['>', '<', '>=', '<=', '==', '!=']:
            self.advance()
            self.skip_whitespace()
            self.parse_term()
            self.skip_whitespace()
            
        # Toplama ve çıkarma operatörleri
        while self.current and not self.has_error and self.current.tur == TOKEN_TURLERI["OPERATOR"] and self.current.deger in ['+', '-']:
            self.advance()
            self.skip_whitespace()
            self.parse_term()
            self.skip_whitespace()

    def parse_term(self):
        self.skip_whitespace()
        self.parse_factor()
        self.skip_whitespace()
        while self.current and not self.has_error and self.current.tur == TOKEN_TURLERI["OPERATOR"] and self.current.deger in ['*', '/']:
            self.advance()
            self.skip_whitespace()
            self.parse_factor()
            self.skip_whitespace()

    def parse_factor(self):
        self.skip_whitespace()

        if self.current is None:
            mesaj = f"HATA (Satır {self.current.satir}): Beklenmeyen ifade sonu"
            self.hata_mesajlari.append(mesaj)
            self.has_error = True
            return

        if self.current.tur in [TOKEN_TURLERI["SAYI"], TOKEN_TURLERI["DEGISKEN"]]:
            self.advance()
        elif self.current.deger == '(':
            self.advance()
            self.skip_whitespace()
            self.parse_expression()
            self.skip_whitespace()
            if not self.current or self.current.deger != ')':
                mesaj = f"HATA (Satır {self.current.satir}): Parantez kapatma ')' bekleniyordu."
                self.hata_mesajlari.append(mesaj)
                self.has_error = True
                return
            self.advance()
        else:
            mesaj = f"HATA (Satır {self.current.satir}): Geçersiz ifade: {self.current}"
            self.hata_mesajlari.append(mesaj)
            self.has_error = True
            self.advance()
