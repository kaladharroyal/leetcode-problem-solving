class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # No need to continue if the first number is positive
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res        


        """O(n^3)
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplets = sorted([nums[i], nums[j], nums[k]])

                        if triplets not in res:
                            res.append(triplets)


        return res"""                    



        