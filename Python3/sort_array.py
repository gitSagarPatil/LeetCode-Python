"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = list()
        for i in A:
            B.append(i*i)
        return sorted(B)


A = [-4, -1, 0, 3, 10]
o = Solution()
print(o.sortedSquares(A=A))
