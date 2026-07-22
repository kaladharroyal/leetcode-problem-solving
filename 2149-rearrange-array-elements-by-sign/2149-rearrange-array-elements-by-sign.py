class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n, res = [], [], []

        for i in range(len(nums)):
            if nums[i] <0:
                n.append(nums[i])
            else:
                p.append(nums[i])

        for i  in range(len(p)):
            res.append(p[i])
            res.append(n[i])
        return res