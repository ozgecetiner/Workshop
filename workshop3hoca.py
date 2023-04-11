
#Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

#Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

#2. geliştirdiğimiz programa kullanıcının alt limiti belirlemesi için gerekli desteği ekleyelim.
#döngüler -loops
#for loop
#i=0 , i =i+1
# 0,1,2,3,4,5,6,7,8,9 <10

biggestValue = 0
secondbiggestvalue = 0
for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi > biggestValue:
        secondbiggestvalue = biggestValue
        biggestValue = sayi

print(f"Girdiğiniz sayılar arasından en büyük olanı:{biggestValue}")
print(f"Girdiğiniz sayılar arasından 2. en büyük olanı:{secondbiggestvalue}")


sayilar = []
# 0 dan başlat, 10'dan küçük olana kadar döngüyü çalıştır, 
# döngü her çalıştığında i değerini 1 artır
for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: "))) #25
sayilar.sort(reverse=True)
enBuyukN = int(input("Sayılar arasından en büyük kaçıncı elemanı istiyorsun? "))
print(sayilar[enBuyukN - 1])

#end


## 3. ister => 2. isterdeki alt limit kullanıcı belirlemelidir
forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i)
##end
