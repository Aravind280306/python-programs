#FUNCTION TO CHECK WHETHER A NUMBER IS PERFECT OR NOT ?

def perfect(num):
    x=0
    for i in range(1,num):
        if(num%i==0):
            x=x+i
        else:
            continue
    if(num== x):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")

num=int(input("Enter Any Number "))
perfect(num)
