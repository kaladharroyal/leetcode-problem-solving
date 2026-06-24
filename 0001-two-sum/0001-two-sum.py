class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return        
                           
        """ for fst in range(0,len(nums)):
            for sec in range(fst+1,len(nums)):
                curr_sum = nums[fst]+nums[sec]
                if(curr_sum == target):
                    return [fst,sec] """"""(complexity o(n^2)"""