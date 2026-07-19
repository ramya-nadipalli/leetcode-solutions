class Solution:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(s, open_cnt, close_cnt):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if open_cnt < n:
                backtrack(s + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(s + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return ans