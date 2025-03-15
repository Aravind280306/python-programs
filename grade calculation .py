i=int(input("Enter Mark Of First Subject  : "))
j=int(input("Enter Mark Of Second Subject  : "))
k=int(input("Enter Mark Of Third Subject  : "))
avg=(i+j+k)/3
print("average = ",avg)
if(avg>=90  and avg <=100):
    print("Your Grade Is  O ")
elif(avg>=80  and avg <90):
    print("Your Grade Is  A+ ")
elif(avg>=70  and avg <80):
    print("Your Grade Is  A ")
elif(avg>=60  and avg <70):
    print("Your Grade Is  B+ ")
elif(avg>=50  and avg <60):
    print("Your Grade Is  B")
elif(avg>=45 and avg<50):
    print("You are just passed")
else:
    print("Sorry You Are Failed")
