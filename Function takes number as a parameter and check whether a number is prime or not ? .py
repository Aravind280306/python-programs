#Function takes number as a parameter and check whether a number is prime or not ?
def isprime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag!=1):
        print("It is a Prime Number")
    else:
        print("Not a Prime Number ")
                        
n=int(input("Enter The Number : "))
if(n<0):
    print("Enter A Positive Number")
elif(n==0 or n==1):
    print("Neither Prime Nor Composite")
else:
    isprime(n)
