isim="Oğuzhan Altundaş"
bölüm="Elektrik Elektronik Mühendisliği"

# isim karakter dizisinde kaç adet karakter bulunmaktadır
print(len(isim))

# isim kısmında oğuzhan kısmını alın
print(isim[0:7])

# isim kısmı:-ndaki altundaşı alın
print(isim[-8:16])

# bölüm kısmındaki ilk 5 ve son 5 harfi alınız 
print(bölüm[0:5],bölüm[-5:32])

# bölüm kısmmındaki karakterleri tersten yazınız
print(bölüm[::-1]) #:: işareti bütün karakterleri al demektir normalde birer birer giderken biz -1 er -1 er gitmesini istedik buraya farklı sayılarda yazılabilirdi.

# 'Hello world'ifadesindeki w harfini W yapınız
a="Hello world"
a=a[0:6]+"W"+a[7:]
print(a)
# 'abc' ifadesinden 3 taane yazınız
print("abc"*3)

# name,surname,age,job = mehmet oğuzhan, altundaş, 17, electrical-electronical engeenireng
# yukarıdaki ifadeyi ' hello my names mehmet oğuzhan altundaş ı am 17 an ı will be engeenir.' yazınız.
n="mehmet oğuzhan altundaş"
A=17
j="engineer"
print("hello my names {} ı am {} and ı am {}".format(n,A,j))
