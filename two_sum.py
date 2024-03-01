class Solution:
    def binSearch(nums, l: int, r: int, x: int):
        #l= leftmost_index;  r= rightmost_index
        if l>r:
            return -1
        m= int((l+r)/2)
        if nums[m]== x:
            return m
        
        if nums[m]> x:
            r= m-1
        else:
            l= m+1
        return Solution.binSearch(nums, l, r, x)

    def bubbleSort(lst: list[int], length: int):
        for i in range(length-1):
            flag= 0
            for j in range(0, length-i-1):
                if lst[j]> lst[j+1]:
                    x= lst[j]
                    lst[j]= lst[j+1]
                    lst[j+1]= x
                    flag= 1
            if flag == 0:
                return lst
        return lst
        
        
    def twoSum(self, nums, target: int):
        Len= len(nums)
        print(nums)
        nums= Solution.bubbleSort(nums, Len)
        print(nums)
        index1= 0
        for element in nums:
            print("element: ",element)
            x= target - element
            print("x: ",x)
            index2= Solution.binSearch(nums,0,Len-1,x)
            print("index1: ",index1)
            print("index2: ",index2)
            if index2 != -1:
                return [index1,index2]
            index += 1
            
        return [-1,-1]      
    
print(Solution.twoSum(Solution,[3,2,4],6))