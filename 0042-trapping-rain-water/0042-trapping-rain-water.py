class Solution:
    def trap(self, height: List[int]) -> int:

        left = lmax = rmax =  total = 0
        right = len(height)-1

        while left < right:

            if height[left] < height[right]:
                if lmax > height[left]:
                    total += lmax - height[left]
                else:
                    lmax = height[left]
                left +=1

            else:
                if rmax > height[right]:
                    total +=  rmax - height[right]
                else:
                    rmax = height[right]  
                right -= 1          
        return total                  



        """
        time: O(n)
        space: O(n)
        prefix_max = []
        suffix_max  = []
        curr_max = 0

        for h in height:
            curr_max = max(curr_max, h)
            prefix_max.append(curr_max)
        curr_max = 0
        for i in range(len(height)-1, -1, -1):
            curr_max = max(curr_max, height[i])
            suffix_max.append(curr_max)

        suffix_max.reverse()
        total = 0
        for i in range(len(height)):
            if height[i] < prefix_max[i] and height[i] <suffix_max[i]:
                total+= min(prefix_max[i], suffix_max[i]) - height[i]

        return total"""
        