# 15: 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array 
# which gives the sum of zero.

# example
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#  [-1, 0, 1],
#  [-1, -1, 2]
#]

# problem in smaller steps
# loop through array finding answers (unknown how many times)
# determine when three numbers = 0
# determine entry point into the array

# method of solving
# this problem is simular to two sum which you just sort then 
# loop through for answers

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    if nums is None or not nums or len(nums) < 3: # error handling
        return []
    
    nums.sort()
    answerSet = set() #hashset for O(1) lookup time for answer

    for i in range(len(nums) - 2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            sum = nums[i] + nums[start] + nums[end]
            print([nums[i],nums[start],nums[end]])
            if sum == 0:
                answerSet.add(tuple([nums[i],nums[start],nums[end]])) #can't hash a list so I have to convert it to a tuple
                end = end - 1
                start = start + 1
            elif sum > 0:
                end = end - 1
            elif sum < 0:
                start = start + 1

    #converting back to a list for the answer
    print(answerSet)
    answerList = []
    for i in answerSet:
        answerList.append(list(i))

    return answerList

print(threeSum([-2,0,1,1,2]))

# can save space by using 3 pointers 



