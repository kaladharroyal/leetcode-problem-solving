class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums2.extend(nums1)
        nums2.sort()
        n = len(nums2)
        if len(nums2)%2 == 1:
            return nums2[n//2]
        else:
            return (nums2[n//2 - 1] +nums2[n//2])/2   
        