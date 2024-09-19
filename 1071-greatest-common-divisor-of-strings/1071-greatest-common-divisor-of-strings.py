class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = len(str1)
        while len(str2) % gcd_length != 0 or len(str1) % gcd_length != 0:
            gcd_length -= 1
        return str1[:gcd_length]