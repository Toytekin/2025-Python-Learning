## SÖZLÜK-MAP-DİCTİONARy 
## Darttaki maplerin aynısı key ve valu değerleri var


print("Sözlük/Map")
print("\n")

sozluk={"sıfır":0, "bir":1, "iki":2}
print(type(sozluk))
print(sozluk)


print("\n")
print("Anahtara göre arama")
print(sozluk["bir"])


print("\n")
print("EKLEME")
print(sozluk)
sozluk["uc"]=3
print(sozluk)


print("\n")
print("DEĞİŞTİRME")
print(sozluk)
sozluk["uc"]=222222
print(sozluk)


print("\n")
print("İÇ İÇE SÖZLÜK")

ic_ice_sozluk={"sayılar":{"bir":1,"iki":2,"uc":3,"dort":4}}
print(ic_ice_sozluk)
print(ic_ice_sozluk["sayılar"]["bir"])


print("\n")
print("METOTLAR")
print("keys---> keyleri getirir")
print(sozluk.keys())
print("\n")
print("value---> valulaarı getirir")
print(sozluk.values())
print("\n")
print("items---> itemları getirir")
print(sozluk.items())

