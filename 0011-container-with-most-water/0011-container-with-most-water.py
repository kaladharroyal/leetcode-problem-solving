class Solution:
    def maxArea(self, height: List[int]) -> int:
        MaxWater = 0
        left = 0
        right = len(height)-1

        while left < right:
            MinHeight = min(height[left], height[right])
            width = right - left
            area = MinHeight*width
            
            MaxWater = max(area , MaxWater)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return MaxWater        

















        """ maxwater = 0
        left = 0 
        right = len(height)-1

        while left < right:
            MinHeight = min(height[left], height[right])
            Area = MinHeight*(right-left)
            maxwater = max(Area,maxwater)   
            if height[left]<height[right]:
                left+=1
            else:
                right-=1    
        return maxwater """         