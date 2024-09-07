class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels=['a','e','i','o','u','A','E','I','O','U']
        lst=list(s)
        while left<right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        ans="".join(lst)
        return ans