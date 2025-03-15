# find the first non repeated element in a list
def repeat(string):
    new=sorted(string)
    for i in string:
        for j in string:
            if i==j+1:
                continue
            else:
                new.append(i)
    return new

OG_LST=[1,2,3,4,5,6,7,8,9]
print("Original List : ", OG_LST)
print("First non repeated element in the said list : ",repeat(OG_LST))
OG_LST=[1,2,3,1,2,4,5,6,7,8]
print("Original List : ", OG_LST)
print("First non repeated element in the said list : ",repeat(OG_LST))
OG_LST=[1,2,3,4,2,4,3,1,8,8]
print("Original List : ", OG_LST)
print("First non repeated element in the said list : ",repeat(OG_LST))

