# Accept a number and display:

# Whether it is even or odd.
# Whether it is prime.
# Its reverse.
# Whether it is a palindrome.

n = int(input("Enter Number: "))

def evenOrOdd(n):
    if(n%2==0):
        print(f"{n} is even number.")
    else:
        print(f"{n} is odd number.")

def primeOrNot(n):

    if(n<=1):
        return False
    c = 2
    while(c*c<=n):
        if(n%c == 0):
            return False
        c+=1
    return True
    
    
              

def reverseNum(n):
    rev = 0
    while n>0:
        d = n%10
        rev = rev*10+d
        n = n//10
    return rev
    # print(f"Reversed Number: {rev}")

def palindrome(n):

    reverse = reverseNum(n)

    if(n == reverse):
        return True
    else:
        return False

evenOrOdd(n)
isPrime = primeOrNot(n)
rev = reverseNum(n)
print(f"Reversed number is {rev}")
isPalin = palindrome(n)
if(isPrime):
    print(f"{n} is prime.")
else:
    print(f"{n} is not a prime.")
if(isPalin):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")

        