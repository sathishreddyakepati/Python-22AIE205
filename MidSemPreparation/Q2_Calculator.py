print("-----------Calculator V1.0-----------")
a = int(input("Enter Number1: "))
b = int(input("Enter Number2: "))
c = input("Enter operator(+,-,/,*,%,//,**): ")

if c == '+':
    print("Result: ",a+b)
elif c == '-':
    print("Result: ",a-b)
elif c == '*':
    print("Result: ",a*b)
elif c == '/':
    print("Result: ",a/b)
elif c == '%':
    print("Result: ",a%b)
elif c == '//':
    print("Result: ",a//b)
elif c == '**':
    print("Result: ",a**b)
else:
    print("Invalid operator: ")



