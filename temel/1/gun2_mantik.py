 ## MANTIKSAL DEĞERLER

print("\n\n") 
print("------------------------------------------------------------------------") 

a=None
print("None ile değişkenin değerinin sonradan atanacağını belirleriz")
print(a)
a="Yeni Değer"
print(a)


# and ------> iki şart sağlandığında true sağlanmadığında false olur
print("\n")

v="Ali"
c="Katip"
d="Ali"


sonuc = v==c and v==d  #-----> sonuc false çünkü iki değer birden sağlanmıyor
print(sonuc)


# or ------> iki şarttan sadece biri sağlansa bile True döner
print("\n")

v="Ali"
c="Katip"
d="Ali"


sonuc = v==c or v==d  #-----> sonuc true çünkü iki değer biri tutuyor
print(sonuc)
 