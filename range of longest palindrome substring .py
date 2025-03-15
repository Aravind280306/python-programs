def palindrome(str,low,high):
    while(low<high):
        if str[low]!=str[high]:
            return False 
        low +=1
        high-=1
    return True
def longeststr(str):
    n=len(str)
    maxlen=1
    start=0
    for i in range(n):
        for j in range(i,n):
            if palindrome(str,i,j)and(j-i+1)>maxlen:
                start=i
                maxlen=j-i+1
    return (start,start+maxlen)
str=input("Enter A String : ")
a=longeststr(str)
print(a)


