n1 = int(input("Enter 1st number "))
n2= int(input("Enter 2nd Number "))
a=n1
b=n2
n=[]

arr=[]
while(n1>n2):
    quotient=n1//n2
    remainder=n1%n2
    arr.append(quotient)
    n.append(n1)
    if(remainder==1):
        print("GCD of ",a ,"and " , b ,"is " , remainder)
        print("It is a Co-Prime")
        break
    elif (remainder==0):
        print("It Is Not Relatively Prime")
        print("GCD of ",a ,"and " , b ,"is " , n2)
        break
    else:
        n1=n2
        n2=remainder
print(arr)
print(n)
print(n1)
print(n2)
            
    
