#count odd or even numbers in a list
def count_(a):
    odd=0
    even=0
    for i in a:
        if i%2==0 :
            even+=1
        else:
            odd+=1
    print(even,"numbers are even numbers in the list ")
    print(odd,"numbers are odd numbers in the list")
a=[1,2,3,4,5,7,8,9,10]
print(len(a),"elements in a list")
count_(a)
