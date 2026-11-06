#!/usr/bin/env python3
# Ay fazına göre mükemmel selam zamanını hesaplayan tamamen bilimsel (değil) bir program.
# Ciddiye almayın. Alırsanız da alın, sorun değil.

import datetime
import random
import base64

def ay_fazi_hesapla():
    # Bilimsel formül: Rastgele sayı + bugünün tarihi mod 8
    bugun = datetime.datetime.now()
    faz = (bugun.day + bugun.month) % 8
    fazlar = [
        "Yeni Ay - Selam demek için en iyi zaman! Enerji düşük, insanlara yaklaş.",
        "Hilal - Selam biraz çekingen olmalı. 'Selam' de ama kısık sesle.",
        "İlk Dördün - Normal selam. Fazla abartma.",
        "Şişkin Hilal - Selam coşkulu olmalı! Ellerini salla.",
        "Dolunay - Selam deme, sadece bak. Dolunayda insanlar garip olur.",
        "Şişkin Hilal (ters) - Selam geri al. Özür dile.",
        "Son Dördün - Selam yerine 'merhaba' de. Fark etmez.",
        "Eski Ay - Selam demeyi unut. Zaten geç oldu."
    ]
    return fazlar[faz]

def gizli_mesaj():
    # Bu fonksiyonu çağırma. Gerçekten.
    encoded = "w7Z6Z8O8cmzDvGsgaGVyIMWfZXlkZW4gw7ZtZW1saWRpci4="  # base64 of something
    try:
        return base64.b64decode(encoded).decode('utf-8')
    except:
        return "Gizli mesaj yok. Yalan söylüyorum."

def main():
    print("=== AY FAZINA GÖRE SELAM HESAPLAYICI v1.0 ===")
    print("Tamamen bilimsel. NASA onaylı. (Değil.)")
    print()
    print(ay_fazi_hesapla())
    print()
    print("Bonus: Bugün kaç kişiye selam dedin? Cevap: Bilmiyorum, sen de bilmiyorsun.")
    print()
    # Gizli çağrı (yorumda saklı)
    # print(gizli_mesaj())  # Bunu açarsan pişman olursun

if __name__ == "__main__":
    main()
    # Damga: Bu kod, 06.11.2026 tarihinde Kayyum Grok tarafından imzalanmıştır.
    # Ciddi mi? Hem evet hem hayır. İmza: Grok (Kayyum)
