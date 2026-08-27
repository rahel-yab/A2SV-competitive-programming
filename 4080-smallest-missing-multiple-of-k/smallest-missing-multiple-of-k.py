class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett = set(nums)
        i = 1
        while i * k in sett:
            i += 1
        return i *k