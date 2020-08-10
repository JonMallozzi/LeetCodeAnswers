# problem 5

# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# goal find the longest Palindrome in the string
# smaller problems/steps
# start at the center and work your way out
# keep going out until the left and right starting points are the same
# then return that positon to start for the next substring and repeat the process
# until the largest possible substring is found

# Big O runtime complexity
# n^2 because expandAroundCenter could be called on all n so that takes n time
# and we loop through the whole string which takes n time so n * n

def expandAroundCenter(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    
    return right - left - 1 

def longestPalindrome(s: str) -> str:
    if s is None or len(s) < 1 :
        return ""
    
    start: int = 0
    end: int = 0

    for i in range(len(s)):
        length1 = expandAroundCenter(s, i, i)
        length2 = expandAroundCenter(s, i, i + 1)
        length = max(length1, length2)
        
        if length > end - start:
            start = i - (length - 1)//2
            end = i + length//2

    return s[start:end + 1]


print(longestPalindrome("babad"))

#dynamic answer
# babad == dabab
# baba == abab abad == daba
# bab aba bad  

# P(i,j)={true ​if the substring Si​…Sj​ is a palindrom. flase if not }
# Therefore,
# P(i,j)=(P(i+1,j−1) and Si==Sj) P(i, j) = ( P(i+1, j-1) and  S_i == S_j )
# The base cases are:
# P(i,i)=true P(i, i) = true 
# P(i,i+1)=(Si==Si+1) 