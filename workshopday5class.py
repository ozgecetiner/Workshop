# classlar-sınıflar -start
# fonksiyon ve değerleri- değişkenleri içerisinde tutabilen nesneler
# oop- nesne yönelimli programlamada bu fonksiyonları burada tanımlamak yerine programladığımız alanları nesne olarak ele alıp bu nesnelere atama yapacağız
# classlar da fonksiyonlar gibi tanımlanıyor tanımlanırken fonksiyonlarda kullanılan "def" kullanılmıyor "class" keyword ü tanımlanıyor.

class Human:  #":" kullanıldığı için alt satırda yine bir tab içeri girilerek işlem yapılıyor. 
#içerisine fonksiyon tanımladığımız için yine "def" ile devam ediyoruz.
    #name= "Özge"
    #built -in
    def __init__(self,name):
        self.name= name
        print("Bir human instance'ı üretildi.")  #yapıcı blok alanı oluşturuldu. Biz bir nesne ürettiğimizde nesnenin çalıştırdığı bir alan oluşur. initialize ediyomuşuz gibi düşünebiliriz. yeni bir obje üretilmiş.
    #bir yapı üretilirken her zaman üretilmesi gereken bir değişken olabilir o yüzden yapıyoruz.
    def __str__(self) -> str:
        return f"STR Fonksiyonundan dönen değer: {self.name}"  #return bir önceki elemana döndürür.
    def talk(self,sentence,):
        #name= "Ercan"
        print(f"{self.name}: {sentence}")
        #print(f"{name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek #nesnelere erişebilmemiz için o nesnelerden birer örnek-instance oluşturabilmemiz gerekiyor
# self => fonksiyonun kendisini ifade ediyor. Class içerisinde tanımlanan her fonksiyon için ilk parametre self parametresiyle rezerve edilmiştir. 
# self yerine humanobject yazılabilir. yani self yerine başka bir şey de yazabiliriz. self yazmak tercih edilebilir.

human1= Human("Enes")
human1.name= "Enes" #bu satırın talk satırının 1 satır üstünde yapılması çıktıyı doğru görebilmemiz açısından önemli! #self.name ile yazılan ismi değiştirecektir
human1.talk ("Merhaba")
human1.walk()
print(human1)

human2= Human("Cem")
human2.name= "Cem"
human2.talk("Selam")
human2.walk()
print(human2)

human3= Human("Özge")
human3.talk("Selam")
human3.walk()
print(human3)

Human("Melike").talk("Merhaba")

# classlar-sınıflar -end










#modules -end