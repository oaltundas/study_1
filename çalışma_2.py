website="http://www.SaikTuran.com"
kursadı="Python Dersleri: Sıfırdan İleri Seviye Python Programlama"

# Hello World karakter dizisindeki baş ve sondaki boşluk karakterini silin
print(" hello world ".strip())

# website dizisindeki sadiktran hariç bütün karakterleri silin 
print(website.strip("http://www.").strip(".com"))

# kursadı altındaki bütün karakterleri küçük harf yapın
print(kursadı.lower())

# website içinde kaç tane a harfi var (count("a"))
print(website.count("a"))

# website www ile başlayıp com ile bitiyor mu ?
print(website.startswith("www"))
print(website.endswith("com"))

# website içinde .com var mı
print(website.find(".com"))

# kursadı altındakilerin tamamı alfabetik mi (isalpha)
print(website.isalpha())

# content ifadesini satırda 50 karakter içine alıp sağ ve soluna * ekle
print("content".center(50,"*"))

# kursadı karakter dizisindeki tüm boşlukları _ ile değiştir
print(kursadı.replace(" ","_"))

# Hello World karakter dizisindeki world ifadesini there olarak değiştir
print("Hello World".replace("World","There"))
