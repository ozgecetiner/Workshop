def sum(firstNum: float, secondNum: float):
    print(firstNum + secondNum)
def substract(firstNum: float, secondNum: float):
    print(firstNum-secondNum)
def multiplication(firstNum: float, secondNum: float):
    print(firstNum * secondNum)
def divide(firstNum:float, secondNum:float):
    if(secondNum != 0):
        print(firstNum / secondNum)
    elif (firstNum==0 and secondNum==0):
        print("Please use limit(differential) calculator!")
    else:
        print("Divider cannot be 0, please check!")
def mod (firstNum: float, secondNum: float):
    if (secondNum !=0):
        print(firstNum % secondNum)
    else:
        print("Divider cannot be 0, please check!")

def calculator(fNum: float, secNum: float, operation: str):  #fNum yazımı önemli unutulmamalı
    if operation=="+":
        sum(firstNum= fNum, secondNum= secNum)
    elif operation=="-":
        substract(firstNum= fNum, secondNum= secNum)
    elif operation=="*":
        multiplication(firstNum= fNum, secondNum= secNum)
    elif operation=="/":
        divide(firstNum= fNum, secondNum= secNum)
    elif operation=="%":
        mod(firstNum= fNum, secondNum= secNum)
    else:
        print("Please choose a valid operator!")

#\n bir aşağıdaki satıra geç demek.
while True:
    print("-----------------------\n")
    firstNum= float(input("Enter your first number:"))
    operation= str(input("Choose your valid operation!( +,-,*, /, %)"))
    secondNum= float(input("Enter your second number:"))
    
    calculator(firstNum, operation, secondNum)
    isContinue = input("Do you want to continue?(Quit for 'q', Continue for 'Enter'!)")
    if (isContinue=="q"):
        print("\nOperation terminated!")
        break
    else:
        pass


