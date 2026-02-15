num1=0
num2=1
print(num1,num2)
for num in range(13):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)
