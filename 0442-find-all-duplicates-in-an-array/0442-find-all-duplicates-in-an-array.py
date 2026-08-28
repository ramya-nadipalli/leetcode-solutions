class Solution:
    def findDuplicates(self, nums):
        result = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                # We have already seen this number
                result.append(abs(num))
            else:
                # Mark this number as seen
                nums[index] = -nums[index]

        return result