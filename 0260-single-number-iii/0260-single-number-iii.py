from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)

        for key, value in freq.items():
            if value == 1:
                res.append(key)
        return res                   