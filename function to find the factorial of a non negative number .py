#To Calculate The Factorial Of A Number (a Non Negative Integer).
#The Function  Accepts The Number As An Argument.
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter A Number :"))

if(n<0):
    print("Enter A Postive Number")
else:
    print("Factorial of ",n,"is",fact(n))
