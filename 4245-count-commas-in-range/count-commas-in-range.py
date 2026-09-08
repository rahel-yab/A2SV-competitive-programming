class Solution:
    def countCommas(self, n: int) -> int:
        ans = n - 1000 + 1
        return ans if ans > 0 else 0