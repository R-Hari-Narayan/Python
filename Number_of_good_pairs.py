#Leet code problem 1512: Number of Good pairs

def numIdenticalPairs(nums):
        frequency_map= {}
        count= 0
        for i in nums:
            if frequency_map.get(i):
                frequency_map[i]+= 1
            else:
                frequency_map.update({i: 1})
        for n in frequency_map.values():
            count+= (n*(n-1))/2
        return int(count)

input= [1,2,3,1,1,3]
print(numIdenticalPairs(input))