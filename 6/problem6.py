# problem 6: ZigZag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern 
# on a given number of rows like this: (you may want to display 
# this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R

# example
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# problem smaller problems/steps
# place number of characters in row length first
# then determine based off of the number of rows the number of zig-zag characters
# then add those to string and repeat 

# zig-zig is numberRows/2 floored 
# 7/2 floored 3

#1          1 
#2         a2
#3       a  
#4     a
#5   a
#6 a 
#7

def convert(s: str, numRows: int) -> str:

    string_arr = [""] * numRows
        
    start = 0
    reverse = False
    cur_counter = 0
        
    while start < len(s):
            
       if not reverse: #puts in row + zigzag
            string_arr[cur_counter] += s[start]
            start += 1
            cur_counter += 1
                
            if cur_counter == numRows:
                reverse = True
                cur_counter -= 1
       else:
                
            while start < len(s) and cur_counter > 1: #removes zig-zag and adds to next row
                    
                cur_counter -= 1
                string_arr[cur_counter] += s[start]
                start += 1
            reverse = False
            cur_counter = 0
           
    return "".join(string_arr)

print(convert("PAYPALISHIRING", 3))