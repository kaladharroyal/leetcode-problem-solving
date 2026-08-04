class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missv = []
        low, high = min(nums),max(nums)

        for i in range(low, high+1):
            if i not in nums:
                missv.append(i)

        return missv        
        