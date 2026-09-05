class Solution:
    def largestPrimeFactor(self, n):
        largest = 1

        # Remove all factors of 2
        while n % 2 == 0:
            largest = 2
            n //= 2

        # Check odd factors
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                largest = factor
                n //= factor
            factor += 2

        # If n is still > 1, it is itself a prime factor
        if n > 1:
            largest = n

        return largest
                
        