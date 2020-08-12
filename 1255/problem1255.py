# 1255: Maximum Score Words Formed by Letters

# Given a list of words, list of  single letters (might be repeating) 
# and score of every character.

# Return the maximum score of any valid set of words formed by using 
# the given letters (words[i] cannot be used two or more times).

# It is not necessary to use all characters in letters and 
# each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' 
# is given by score[0], score[1], ... , score[25] respectively.

# example: 
# Input: words = ["dog","cat","dad","good"], 
# letters = ["a","a","c","d","d","d","g","o","o"], 
# score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and 
# "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

# Constraints:

#    1 <= words.length <= 14
#   1 <= words[i].length <= 15
#    1 <= letters.length <= 100
#    letters[i].length == 1
#    score.length == 26
#    0 <= score[i] <= 10
#    words[i], letters[i] contains only lower case English letters.

# use dfs and backtracking to slove it

from typing import List
import collections

def dfs(i, curr_score, counter, max_score, words_score, words_counter):
        if curr_score + sum(words_score[i:]) <= max_score:
            return max_score
        max_score = max(max_score, curr_score)
        for j, wcnt in enumerate(words_counter[i:], i):
            if all(n <= counter.get(c,0) for c,n in wcnt.items()):
                    dfs(j+1, curr_score+words_score[j], counter-wcnt, max_score, words_score, words_counter)

def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    max_score = 0
    words_score = [sum(score[ord(c)-ord('a')] for c in word) for word in words]
    words_counter = [collections.Counter(word) for word in words]
    return dfs(0, 0, collections.Counter(letters), max_score, words_score, words_counter)

print(maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))