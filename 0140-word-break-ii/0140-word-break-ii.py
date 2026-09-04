class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            res = []

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word in words:
                    for rest in dfs(j):
                        res.append(word if not rest else word + " " + rest)

            memo[i] = res
            return res

        return dfs(0)