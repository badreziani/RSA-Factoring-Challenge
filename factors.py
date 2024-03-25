#!/usr/bin/python3

def is_prime(number):
    """Defines if a number is prime or not."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        return True

for x in range(1, n):
    if is_prime(x):
        p = x
        q = n // x
        if p * q == n:
            print("{:d}={:d}*{:d}".formatn(n, q, p))
            break
