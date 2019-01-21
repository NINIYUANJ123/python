class Solution:
    def reverseBits(self,n):
        z=bin(n)[2:]
        z="0"*(32-len(z))+z
        z=z[::-1]
        return int(z,2)

