class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = list(range(n))

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r] = 0 if l == 0 else min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r] = 0 if l == 0 else min(dp[r], dp[l - 1] + 1)
                l -= 1
                r += 1

        return dp[-1]