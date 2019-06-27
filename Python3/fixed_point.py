"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.
Return -1 if no such i exists.



Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation:
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
Example 2:

Input: [0,2,5,8,17]
Output: 0
Explanation:
A[0] = 0, thus the output is 0.

https://leetcode.com/problems/fixed-point/
"""


class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for items in A:
            i = A.index(items)
            if items == i:
                return i


A = [-10,-5,0,3,7]
B = [0,2,5,8,17]
s = Solution()
print(s.fixedPoint(A))