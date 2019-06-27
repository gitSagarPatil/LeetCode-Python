"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

"""


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = {}
        if N in dic:
            return dic[N]
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 1
        else:
            value = self.fib(N-1) + self.fib(N-2)
        dic[N] = value
        return value


N = 4
o = Solution()
print(o.fib(N))
