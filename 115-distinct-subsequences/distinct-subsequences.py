class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        ans = 0
        def dp(i, j):
            if (i , j) in memo:
                return memo[(i,j)]
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            skip , take = dp(i+1 , j) , 0
            if s[i] == t[j]:
                take = dp(i+1, j+1)
            
            memo[(i,j)] = skip + take
            return memo[(i,j)]

        return dp(0 , 0)

            
