"""
About the problem:
    This is the 88th problem on leetcode. the name of this problem is 'Merge Sorted Array'
    you can open this problem by clicking the following link: https://leetcode.com/problems/merge-sorted-array

"""


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Args:
            num1 (List[int]): 1st sorted array of integers.
            m (int): the number of elements in num1.
            
            num2 (List[int]): 2nd sorted array of integers.
            n (int): the number of elements in num2.
        """
        
        # Start merging from the end of nums1 (where extra space is allocated)
        i = m - 1  # Last element of nums1's initial portion
        j = n - 1  # Last element of nums2
        k = m + n - 1  # Last position in nums1

        # Merge in reverse order to avoid overwriting nums1's data
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, add them
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
