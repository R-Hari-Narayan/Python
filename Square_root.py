def squareRoot(x,l,r):
    if x==0 or x==1:
        return x
    
    if l==r:
        return l
    if l>r:
        return r
    
    mid= int((l+r+1)/2)
    midSq= mid*mid
    if midSq==x:
        return mid
    
    if midSq> x:
        r= mid-1
    else:
        l= mid+1
    return squareRoot(x,l,r)


x= int(input("Enter number to find SqRoot: "))
print("Square root is ",squareRoot(x,2,int(x/2)))