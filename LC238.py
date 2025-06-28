# Product of array except self without using division operator
# Hint: Use prefix and postfix of List
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    L = len(nums)
    output = [1]

    #Save prefix in output
    for i in range(L-1):
        output.append(nums[i]*output[i])

    #Multiply with postfix in output
    postfix = 1
    for i in range(L-1,-1,-1):
        output[i] *= postfix
        postfix *= nums[i]

    return output



nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))



# def productExceptSelfWithDivision(nums: List[int]) -> List[int]:
#     product = 1
#     output = []
#     countZero = 0
#     for n in nums:
#         product *= n
#         if n== 0:
#             countZero+= 1

#     if product == 0:
#         for n in nums:
#             if n == 0:
#                 if countZero > 1:
#                     output.append(0)
#                 else: 
#                     p = 1
#                     for j in nums:
#                         if j != 0:
#                             p*= j
#                     output.append(p)
#             else:
#                 output.append(0)
#     else:
#         for n in nums:
#             output.append(int(product/n))
#     return output