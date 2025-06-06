from lexical import tokenize
from topdown import Parser

ornek_kodlar = [
    "x = 3 + 4 * (2 - 1);",
    "y = x / 5;",
    "z = y + 2;",
    "a = 1 + (2 * 3;"
]

for i, kod in enumerate(ornek_kodlar, start=1):
    print(f"\n--- Örnek {i} ---")
    print(f"Kod: {kod}")
    
    tokenler = tokenize(kod)
    for t in tokenler:
        print(t)
    
    parser = Parser(tokenler)
    parser.parse()
    
    if parser.has_error:
        print("❌ Parsing sırasında hata oluştu.")
    else:
        print("✅ Parsing başarılı.")
