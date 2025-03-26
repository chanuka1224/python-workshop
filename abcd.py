num1=int(input("Enter number 1 :   "))
num2=int(input("Enter number 2 :   "))
num3=int(input("Enter number 3 :   "))
max=0
if(num1<num2):
    if(num2<num3):
        max=num3
    else:
        max=num2
else:
    max=num1
print(max)