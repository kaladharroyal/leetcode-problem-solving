class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        return min(freq, key=freq.get)
