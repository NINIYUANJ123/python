class Solution:
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        while num % 4 == 0:
            num //= 4
        return num == 1
