from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ord(ch) - ord('a')] = freq[ch] // 2

        CAP = k

        def comb_limit(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > CAP:
                    return CAP + 1
            return res

        def count_perms(cnt):
            res = 1
            used = 0
            for c in cnt:
                if c:
                    res *= comb_limit(used + c, c)
                    if res > CAP:
                        return CAP + 1
                    used += c
            return res

        if count_perms(half) < k:
            return ""

        first = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perms(half)

                if ways >= k:
                    first.append(chr(i + ord('a')))
                    break

                k -= ways
                half[i] += 1

        left = "".join(first)
        return left + mid + left[::-1]