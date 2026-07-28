from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq = Counter(nums)
        return min(freq, key = freq.get)

        