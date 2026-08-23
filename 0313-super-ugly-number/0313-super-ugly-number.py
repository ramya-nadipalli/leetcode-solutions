class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        indices = [0] * len(primes)

        for i in range(1, n):
            next_num = float('inf')

            for j in range(len(primes)):
                next_num = min(next_num, ugly[indices[j]] * primes[j])

            ugly[i] = next_num

            for j in range(len(primes)):
                if ugly[indices[j]] * primes[j] == next_num:
                    indices[j] += 1

        return ugly[n - 1]