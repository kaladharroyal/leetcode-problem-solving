class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:].zfill(32)
        s = a[::-1]
        
        return int(s, 2)

        