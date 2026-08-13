class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n

        for i in range(n):
            ans ^= i ^ nums[i]

        return ans