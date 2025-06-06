import tkinter as tk
from tkinter import scrolledtext
from lexical import tokenize
from topdown import Parser

def calistir():
    kod = giris_alani.get("1.0", tk.END)
    tokenler = tokenize(kod)

    token_alani.config(state='normal')
    token_alani.delete("1.0", tk.END)
    for t in tokenler:
        token_alani.insert(tk.END, str(t) + "\n")
    token_alani.config(state='disabled')

    parser = Parser(tokenler)
    parser.parse()

    sonuc_alani.config(state='normal')
    sonuc_alani.delete("1.0", tk.END)

    if parser.hata_mesajlari:  # ❗ Burayı değiştirdik
        sonuc_alani.insert(tk.END, "❌ Parsing işlemi sırasında hatalar oluştu. ❌\n")
        for hata in parser.hata_mesajlari:
            sonuc_alani.insert(tk.END, hata + "\n")
    else:
        sonuc_alani.insert(tk.END, "✅ Parsing işleminiz başarılı! ✅\n")

    sonuc_alani.config(state='disabled')

    renklendir_metni(giris_alani, tokenler)



pencere = tk.Tk()
pencere.title("Levent Kutay Sezer FB OZEL")
pencere.geometry("700x600")
pencere.configure(bg="#0a1d5e")

etiket = tk.Label(pencere, text="Kodunuzu giriniz:", bg="#0a1d5e", fg="#f7d100", font=("Arial", 12, "bold"))
etiket.pack()

giris_alani = scrolledtext.ScrolledText(pencere, height=10, bg="white", fg="black")
giris_alani.pack(padx=8, pady=5, fill="both")

tusa_bas = tk.Button(pencere, text="ÇALIŞTIR", command=calistir, bg="#f7d100", fg="#0a1d5e", font=("Arial", 12, "bold"))
tusa_bas.pack(pady=8)

etiket2 = tk.Label(pencere, text="Tokenler Şunlardır :", bg="#0a1d5e", fg="#f7d100", font=("Arial", 12, "bold"))
etiket2.pack()

token_alani = scrolledtext.ScrolledText(pencere, height=7, state='disabled', bg="white", fg="black")
token_alani.pack(padx=7, pady=5, fill="both")

etiket3 = tk.Label(pencere, text="Sonuç:", bg="#0a1d5e", fg="#f7d100", font=("Arial", 16, "bold"))
etiket3.pack()

sonuc_alani = scrolledtext.ScrolledText(pencere, height=7, state='disabled', bg="white", fg="black")
sonuc_alani.pack(padx=15, pady=15, fill="both")

def renklendir_metni(text_widget, tokenler):
    renkler = {
        'DEGISKEN': 'blue',
        'SAYI': 'green',
        'OPERATOR': 'purple',
        'STRING': 'red',
        'NOKTALAMA': 'red',
        'ANAHTAR_KELIME': 'orange'  # Anahtar kelimeler için turuncu renk
    }

    for tag in renkler:
        text_widget.tag_config(tag, foreground=renkler[tag])

    content = text_widget.get("1.0", "end-1c")

    for tag in renkler:
        text_widget.tag_remove(tag, "1.0", "end")

    for token in tokenler:
        tur = token.tur if hasattr(token, "tur") else token[0]
        deger = token.deger if hasattr(token, "deger") else token[1]

        index = "1.0"
        while True:
            index = text_widget.search(deger, index, nocase=False, stopindex="end")
            if not index:
                break
            end_index = f"{index}+{len(deger)}c"
            text_widget.tag_add(tur, index, end_index)
            index = end_index


pencere.mainloop()
