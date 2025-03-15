#function thatprints out the first n rows of a pascal triangle
def pascal_triangle(n):
    x = [1]
    y = [0]
    for trow in range(max(n, 0)):
        print(x)
        x= [l + r for l, r in zip(x + y, y + x)]
    return n >= 1
n=int(input("Enter The  Number Of Rows "))
pascal_triangle(n) 


    
