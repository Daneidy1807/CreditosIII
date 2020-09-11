num1=int(input("numero1: "))
num2=int(input("numero2: "))
if num1<num2:
    for i in range(num1, num2 +1):
        if i %2!=0:
            print({i})
        