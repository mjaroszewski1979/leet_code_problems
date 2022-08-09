'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

words = ["flower","flow","flight"]
min_word = len(min(words, key=len))
first_word = words[0]
rest_words = words[1:]
result = ''
for x in range(min_word):
    for y in rest_words:
        print(y[x])