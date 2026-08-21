class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        freq = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                freq[int(s)] += 1

        cows = 0

        for s, g in zip(secret, guess):
            if s != g and freq[int(g)] > 0:
                cows += 1
                freq[int(g)] -= 1

        return str(bulls) + "A" + str(cows) + "B"