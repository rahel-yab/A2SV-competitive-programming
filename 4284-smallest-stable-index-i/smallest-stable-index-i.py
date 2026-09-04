class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = float("inf")
        for i in range(len(nums)):
            maxx = max(nums[:i+1])
            minn = min(nums[i:])
            if (maxx - minn) <= k:
                ans = min(ans, i)
                
        return ans if ans != float("inf") else -1
