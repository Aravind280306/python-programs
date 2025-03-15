#check the longest  sublist in a list
a=[[1,2],[3,4,5],[6,7,[8,9],10,11]]
print(max(a,key=len),'is the biggest sublist')
print(min(a,key=len),'is the smallest sublist')
