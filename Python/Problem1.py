#Median Of Two Sorted Array
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        mid = len(arr) // 2 
        arr.sort()
        if len(arr) % 2 == 0:
            return (arr[mid] + arr[mid - 1]) / 2    
        return arr[mid]
            