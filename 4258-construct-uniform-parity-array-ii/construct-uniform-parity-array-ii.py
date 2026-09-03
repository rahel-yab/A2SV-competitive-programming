class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minn = min(nums1)
        if minn % 2 == 0:
            for num in nums1:
                if num % 2 == 1:
                    return False
        return True
