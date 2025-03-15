a=int (input("Enter The First Integer : "))
b=int (input("Enter The Second Integer : "))
c=input("Enter The Operation(+,-,*,/) : ")
if(c=='+'):
    d=a+b
    print('The Sum IS : ',d)
elif (c=='-'):
    d=a-b
    print('The Differce is :')
elif (c=='*'):
    d=a*b
    print('The Product is :')
elif (c=='/'):
    d=a/b
    print('The Quotient is :')
else:
    print('invalid operator')


