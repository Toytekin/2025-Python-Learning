print("Oyuncu Kaydetme")

kayitli_oyuncukar =[]


while True:
         ad=input("Oyuncunun Adı:  ")
         soyad=input("Oyuncunun Soyadı:  ")
         yas=input("Oyuncunun Yaşı:  ")
         items=ad +"  "+soyad+ "  "+yas
         kayitli_oyuncukar.append(items)
         print("Oyuncu kaydediliyor.......")
         print("KAYDEDİLDİ")
         print("\n")
         print('Kaydedilen Oyuncu')
         print(items)
         print("\n")
         print('Toplam Oyuncu SAyısı')
         print(kayitli_oyuncukar.__len__())
         print("\n")
         print('Toplam Oyuncu Listesi')
         print(kayitli_oyuncukar)
         
         
         
         
         