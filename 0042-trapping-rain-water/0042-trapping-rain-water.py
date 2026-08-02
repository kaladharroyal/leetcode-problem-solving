class Solution:
    def trap(self, height: List[int]) -> int:
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

        return total        
        