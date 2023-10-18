class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2) 
        nums_len = len(sorted_nums)

        if nums_len % 2 != 0:
            return sorted_nums[(int((nums_len + 1)/2)) - 1]
        elif nums_len % 2 == 0:
            return (sorted_nums[int(nums_len/2) - 1] + sorted_nums[int(nums_len/2)]) / 2
