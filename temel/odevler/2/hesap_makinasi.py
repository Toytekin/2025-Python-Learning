print(""" 
      
      BASİT HESAP MAKİNASI
      
      1.TOPLAMA
      2.ÇIKARMA
      3.ÇARPMA
      4.BÖLME
      
      """)
while True:
    try:
        # Kullanıcıdan ilk sayıyı al
        sayi1 = float(input("1. Sayıyı giriniz: "))
        # Kullanıcıdan ikinci sayıyı al
        sayi2 = float(input("2. Sayıyı giriniz: "))
        # İşlem seçimi
        islem = int(input("İşlem giriniz (1-4): "))
        
        if islem == 1:
            print("{} ile {}'in TOPLAMI {}".format(sayi1, sayi2, sayi1 + sayi2))
        elif islem == 2:
            print("{} ile {}'in FARKI {}".format(sayi1, sayi2, sayi1 - sayi2))
        elif islem == 3:
            print("{} ile {}'in ÇARPIMI {}".format(sayi1, sayi2, sayi1 * sayi2))
        elif islem == 4:
            # Sıfıra bölmeyi kontrol ediyoruz
            if sayi2 == 0:
                print("Bir sayı sıfıra bölünemez! Lütfen başka bir sayı giriniz.")
            else:
                print("{} ile {}'in BÖLÜMÜ {}".format(sayi1, sayi2, sayi1 / sayi2))
        else:
            print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİN (1, 2, 3 veya 4)")
    
    except ValueError:
        print("Lütfen geçerli bir sayı veya işlem giriniz!")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")