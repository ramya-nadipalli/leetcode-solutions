class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark numbers that exist
        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        # Positive positions represent missing numbers
        result = []

        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result