a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number :"))
for num in range(a,b + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
