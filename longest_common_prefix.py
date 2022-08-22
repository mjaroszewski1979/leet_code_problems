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

def longestCommonPrefix(words):
    """
    :type words: List[str]
    :rtype: str
    """
    result = ''
    for num in range(len(words[0])):
        for word in words:
            if num == len(word) or word[num] != words[0][num]:
                return result

        result += words[0][num]
    return result