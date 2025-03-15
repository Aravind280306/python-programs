#pair of list whose sum is equal to the given value
def check(lst,n):
    for i in lst:
        for j in lst[i:]:
            if i+j==n:
                if i!=j:
                    new_lst.append((i,j))
lst=[0,1,2,3,4,5,6,7,8,9]
print('original list',lst)
new_lst=[]
n=int(input("List all pair of the said list whose sum is equals to : "))
check(lst,n)
print(new_lst)

