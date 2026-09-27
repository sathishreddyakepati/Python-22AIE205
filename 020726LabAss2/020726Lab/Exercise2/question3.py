#3.validate PAN number
#CH.SC.U4AIE25001
# ex:AAAAA9999A

pan = input("Enter your PAN number: ")

if len(pan)!=10:
    print("PAN number must contain only 10 Characters")
else:
    valid = True

    for i in range(0,5):
        if not pan[i].isalpha or not pan[i].isupper():
            valid = False
    for i in range(5,9):
        if not pan[i].isdigit():
            valid = False
    if not pan[9].isalpha() or not pan[9].isupper():
        valid = False
    if valid:
        print("Valid PAN number")
    else:
        print("Invalid PAN Number") 



