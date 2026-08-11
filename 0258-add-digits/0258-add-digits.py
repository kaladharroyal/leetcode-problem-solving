class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        while num >= 10:
            r = num % 10
            num //= 10
            num = num + r
        return num
                
        