"""
About the problem:
    This is the 88th problem on leetcode. the name of this problem is 'Merge Sorted Array'
    you can open this problem by clicking the following link: https://leetcode.com/problems/merge-sorted-array

"""


from typing import List

class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Args:
            num1 (List[int]): 1st sorted array of integers.
            m (int): the number of elements in num1.
            
            num2 (List[int]): 2nd sorted array of integers.
            n (int): the number of elements in num2.
        """
        
        