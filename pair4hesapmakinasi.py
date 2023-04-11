# Toplama Fonksiyonu
def Sum(firstNum, secondNum):
   print(firstNum + secondNum)
 
# Çıkarma Fonksiyonu
def substraction(firstNum, secondNum):
   return firstNum - secondNum

# Çarpma Fonksiiyonu
def multiplication(firstNum, secondNum):
   return firstNum * secondNum
 
# Bölme Fonksiyonu
def divide(firstNum, secondNum):
   if (secondNum !=0):
        print (firstNum / secondNum)
   elif (firstNum==0 and secondNum==0):
        print("Please use limit(differential) calculator!")
   else:
        print("Divider cannot be 0, please check!")

# Mod Fonksiyonu
def mod(firstNum, secondNum):
   print(firstNum % secondNum)

# calculater

def calculater(firstNum, secim, secondNum):
    if secim == '1':
        print(firstNum,"+",secondNum,"=", Sum(firstNum,secondNum))
 
    elif secim == '2':
        print(firstNum,"-",secondNum,"=", substraction(firstNum,secondNum))
 
    elif secim == '3':
        print(firstNum,"*",secondNum,"=", multiplication(firstNum,secondNum))
 
    elif secim == '4':
        print(firstNum,"/",secondNum,"=", divide(firstNum,secondNum))

    elif secim == '5':
        print(firstNum, "%", secondNum),"=", mod(firstNum,secondNum)
    else:
        print("Geçersiz Giriş")

print("Choose the operation.")
print("1.Sum")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5. Mod")
 
# Kullanıcıdan Seçim İsteme
secim = str(input("Seçiminiz (1/2/3/4/5):"))
 
firstNum = float(input("1. Sayı: "))
secondNum = float(input("2. Sayı: "))
 
calculater(firstNum, secim, secondNum)
