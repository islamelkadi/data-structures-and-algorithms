from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        
        if len(nums3)%2==0:
            return float((nums3[len(nums3)//2-1] + nums3[len(nums3)//2])/2)
        else:
            return float(nums3[len(nums3)//2])
