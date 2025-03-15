#WRITE A FUNCTION TO CHECK WHETHER A NUMBER FALL WITHIN THE GIVEN RANGE?
def search(start,end,target):
    for i in range(start,end+1):
        if(target==i):
            return True
    else:
            print("Search Element Not Found In The Given Range ")  
start=int(input("Enter The Starting Value : "))
end=int(input("Enter The Ending Value : "))
target=int(input("Enter The Search Element : "))
x=search(start,end,target)
if(x):
            print("Search Element Found")
