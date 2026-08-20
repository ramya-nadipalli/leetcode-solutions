class Solution:
    def sumOfGoodIntegers(self, n, k):
        total = 0

        for x in range(max(1, n - k), n + k + 1):
            if (n & x) == 0:
                total += x

        return total