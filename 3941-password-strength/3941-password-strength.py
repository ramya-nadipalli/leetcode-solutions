class Solution:
    def passwordStrength(self, password):
        seen = set()
        strength = 0

        for ch in password:
            if ch in seen:
                continue

            seen.add(ch)

            if 'a' <= ch <= 'z':
                strength += 1
            elif 'A' <= ch <= 'Z':
                strength += 2
            elif '0' <= ch <= '9':
                strength += 3
            else:
                strength += 5

        return strength