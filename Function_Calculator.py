num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
print("1. See your statistics")
print("2. Create a new number")
print("3. Exit")
while True:
    choice=int(input("Enter your choice"))
    def calculate():
        print("Your first number plus your second number is", num1+num2)
        print("Your first number minus your second number is", num1-num2)
        print("Your first number times your second number is", num1*num2)
        print("Your first number divided by your second number is", num1/num2)
    if(choice==1):
        calculate()
    elif(choice==2):
        num1=int(input("Enter a number"))
        num2=int(input("Enter a number"))
        print("1. See your statistics")
        print("2. Create a new number")
        print("3. Exit")
    elif(choice==3):
        break
    else:
        print("Invalid Input")

