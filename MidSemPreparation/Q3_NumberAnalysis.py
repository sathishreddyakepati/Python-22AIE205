print("----------Number Analysis---------")
a = int(input("Enter the number: "))

if a>0:
    print(a,"->Positive")
elif a<0:
    print(a,"->Negative")
elif a==0:
    print(a,"->Zero")

if a%2==0:
    print(a,"->Even Number")
elif a%2==1:
    print(a,"->Odd Number")

if a%5==0:
    print(a,"->Divisible by 5")
else:
    print(a,"->Not Divisible by 5")
