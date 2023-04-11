#modules -start

# iki farklı dosyadan kodları almayı sağlayan yapıdır.

#alias #takma ad ile çağırma 

#import matematikforday5 as m  

# sadece takma adı bu dosyayla burada çağırabiliriz
#artık buradaki dosyadan bilgileri çağırabiliriz.

from matematikforday5 import topla as toplamaIslemi
from workshopday5class import Human
#built in modules
import random
#package 

#print(m.topla(10,20))   
#nesneleri de çağırabiliriz ama o da farklı bir dosyadaysa onu da tanımlamamız gerekiyor
print(toplamaIslemi(10,20))

print(random.randint(0,100))

human1= Human("Mirza")
human1.talk("Merhaba")

#modules -end
