def bubbleSort(arr):
    for j in range(len(arr)):
        flag = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag=1
        if flag == 0:
            break
    return arr

arr= [23, 12, 44, 3]
print(bubbleSort(arr))
