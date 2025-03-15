#WRITE A PYTHON FUNCTION TO FIND THE MAXIMUM OF THREE NUMBERS ?
def max_of_three(x,y,z):
    if(x>y):
        if(x>z):
            print(x,"Is Maximum")
    elif(y>z):
        if(y>x):
            print(y,"Is Maximum")
    else:
        print(z,"Is Maximum")
        
a=int(input("Enter The First Number : "))
b=int(input("Enter The Second Number : "))
c=int(input("Enter The Third Number : "))
max_of_three(a,b,c)
