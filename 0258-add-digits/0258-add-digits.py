class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        while num >= 10: #num = 38 -> num = 11
            r = num % 10 # r = 8 -> r = 1
            num //= 10 #num = 3 -> num = 1
            num = num + r #num = 3+8 = 11 -> 1+1 = 2(less than 10 so answer)  
        return num
                
        