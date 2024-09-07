class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle=[None]*len(s)
        for char in range(len(s)):
            shuffle[indices[char]]=s[char]
        ans="".join(shuffle)
        return ans
            