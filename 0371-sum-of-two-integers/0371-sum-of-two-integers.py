class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a = a & mask
        b = b & mask

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= 0x7FFFFFFF:
            return a

        return ~(a ^ mask)