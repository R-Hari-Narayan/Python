def splitArr(arr, l, r):
    mid= int((l+r)/2)
    print("l: ", l, "r: ", r, "mid: ", mid)
    if l>r:
        return
    if l==r:
        print("LEFT == RIGHT")
        return
    
    splitArr(arr, l, mid)
    splitArr(arr, mid+1, r)
    return

arr= [3, 2, 4, 5]
splitArr(arr, 0, len(arr)-1)