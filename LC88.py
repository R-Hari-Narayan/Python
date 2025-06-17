#Leet Code problem number 88
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3= nums1[0:m]

        i=0
        j=0
        k=0
        while i< m and j< n:
            if nums3[i]< nums2[j]:
                nums1[k]= nums3[i]
                i+= 1
            else:
                nums1[k]= nums2[j]
                j+= 1
            print(nums1)
            k+=1
        
        print("i: ", i)
        print("j: ", j)

        while (i< m):
                nums1[k]= nums3[i]
                k+=1
                i+=1
        while (j< n):
                nums1[k]= nums2[j]
                k+=1
                j+=1

        print(nums1)



# __main__

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m= 3
n= 3
merge(nums1, m, nums2, n)