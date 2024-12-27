## Listeler

list1=[1,2,3]
list2=["deneme"]
list3=list1+list2
list4=list("merhaba")



print("Liste Toplama")
print(list3)
print(list4)

print("\n")
print("Liste Index")
print("\n")


print(list4[5])
print(list4[2:9])
print(list4[::-1]) ##Ters Çevirme
print(list4[::2])


print("\n")
print("Listede belirli bir indexi değiştirme")
print("\n")


list1[0]="yeni Eleman"
print(list1)


print("\n")
print("Listede METHOTLAR")
## append ekleme
list1.append("deneme")
print(list1)
## pop son elemanı kaldırma
list1.pop()
print(list1)
list1.pop(2) ##2. indexdekini çıkarır
print(list1)
## sıralama sort
list4.sort()
print(list4)
