class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
    
    # Count the frequency of each character in the string
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Iterate through the string to find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        return -1