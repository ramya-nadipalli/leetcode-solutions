class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))