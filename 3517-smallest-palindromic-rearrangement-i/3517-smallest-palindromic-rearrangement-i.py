class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        first = []
        middle = ""

        for i in range(26):
            first.append(chr(i + ord('a')) * (freq[i] // 2))
            if freq[i] % 2:
                middle = chr(i + ord('a'))

        first = "".join(first)
        return first + middle + first[::-1]