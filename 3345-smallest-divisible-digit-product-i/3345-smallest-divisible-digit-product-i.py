class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod

        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1