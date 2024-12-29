## INPUT
## Kullanıcıdan veri alma


# Kod başlangıcı

# Kullanıcıdan sürekli veri almak için bir while döngüsü başlatıyoruz.
# İlk olarak bir toplam değişkeni (total) oluşturuyoruz ve başlangıç değeri olarak sıfır veriyoruz.
total = 0

print("Sayı girin veya çıkmak için 'exit' yazın:")

# While döngüsü koşulu: Her zaman True olduğu için sonsuz bir döngü çalıştırıyoruz.
while True:
    # Kullanıcıdan girdi alıyoruz. input() fonksiyonu klavyeden veri alır.
    user_input = input("Bir sayı girin: ")

    # Kullanıcı çıkış yapmak isterse "exit" yazarak döngüden çıkabilir.
    if user_input.lower() == "exit":  # input'un küçük harf halini kontrol ediyoruz.
        print("Programdan çıkılıyor...")
        break  # break ifadesi döngüyü durdurur.

    # Kullanıcı "exit" yazmazsa, girdiği değerin bir sayı olup olmadığını kontrol ediyoruz.
    if user_input.isdigit():  # .isdigit() sadece pozitif tam sayılar için çalışır.
        number = int(user_input)  # Sayıyı tamsayıya çeviriyoruz.
        total += number  # Girilen sayıyı toplam değişkenine ekliyoruz.
        print(f"Güncel toplam: {total}")  # Toplamı ekrana yazdırıyoruz.
    else:
        # Kullanıcı geçersiz bir veri girerse uyarı mesajı veriyoruz.
        print("Lütfen geçerli bir sayı girin veya 'exit' yazın!")

# Döngü bittiğinde programın sonlandığını belirten bir mesaj yazıyoruz.
print("Program sona erdi.")

