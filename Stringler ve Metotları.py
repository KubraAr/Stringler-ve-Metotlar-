#Görev1

metin =input("Bir metin giriniz:")

metin = metin.upper() #Tüm harfleri büyük yapma.

metin = metin.strip() #Baştaki ve sondaki boşlukları silme.

metin = metin.replace("A","E") #"A" harflerini "E" ile değiştir.

kelime = metin.split() #Kelimeleri boşluklara göre ayır ve liste halinde yazdır
print(kelime)

#Görev2
metin = "Python programlama dili"

ters = metin[::-1] #Ters yazdırma yöntemi

yeni = metin.replace("programlama", "kodlama")

print("Ters çevirilmiş metin:", ters)
print("Oluşturulan yeni metin:", yeni)