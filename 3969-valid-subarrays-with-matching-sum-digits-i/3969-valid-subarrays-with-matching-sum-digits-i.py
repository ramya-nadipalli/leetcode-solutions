class Solution:
    def countValidSubarrays(self, nums, x):
        n = len(nums)
        ans = 0

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                # Check last digit
                if total % 10 != x:
                    continue

                # Find first digit
                first = total
                while first >= 10:
                    first //= 10

                # Both first and last digits must be x
                if first == x:
                    ans += 1

        return ans