# 11: Container With Most answer

# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i 
# is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms 
# a container, such that the container contains the most answer.

# smaller problems/ steps
# find the max width must have same height as max height or more
# find the max height
# these are really hard to find and there is no greedy way of doing
# just use to pointers and brute force it
# also since we are finding an area on the bound square
# we can use height times width to calulate it

from typing import List

def maxArea(height: List[int]) -> int:
    answer = 0
    start = 0
    end = len(height) - 1

    for i in range(len(height)):
        
        width = abs(start - end)
        
        if height[start] < height[end]:   
            result = width * height[start]
            start += 1
        else:
            result = width * height[end]
            end -= 1

        if result > answer:
            answer = result

    return answer


print(maxArea([1,8,6,2,5,4,8,3,7]))