def mergeSort(arr, l, r):
    mid= int((l+r)/2)
    print("l: ", l, "r: ", r, "mid: ", mid)
    if l>r:
        return
    if l==r:
        print("LEFT == RIGHT")
        return arr[l:r+1]
    
    Left= mergeSort(arr, l, mid)
    Right= mergeSort(arr, mid+1, r)
    print("Left: ", Left)
    print("Right: ", Right)
    i=0
    j=0
    k=l
    while(i < len(Left) and j < len(Right)):
        if (Left[i] <= Right[j]):
            arr[k]= Left[i]
            i+=1
        else:
            arr[k]= Right[j]
            j+=1
        k+=1
    if i!= len(Left):
        Left= Left[i:]
        for element in Left:
            arr[k]=element
            k+=1
    else:
        Right= Right[j:]
        for element in Right:
            arr[k]=element
            k+=1
    print(arr)
    return arr[l:r+1]

arr= [4, 3, 7, 1, 2]
sorted_arr= mergeSort(arr, 0, len(arr)-1)