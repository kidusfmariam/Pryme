import math
from functools import lru_cache
import random

_primes=None

def list_primes(n):
    return [x for x in range(2, n + 1) if is_prime(x)] #use sieve method

def get_primes():
    global _primes
    if _primes is None:
        _primes = list_primes(2000000)
    return _primes

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def sum_primes(n):
    return sum(list_primes(n))

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors

@lru_cache(None)
def next_prime(n):
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1

@lru_cache(None)
def previous_prime(n):
    i = n - 1
    while True:
        if is_prime(i):
            return i
        i -= 1

def count_primes(n):
    return len(list_primes(n))

def prime_product(n):
    primes = list_primes(n)
    product = 1
    for prime in primes:
        product *= prime
    return product

def twin_primes(n):
    primes = list_primes(n)
    return [(primes[i], primes[i+1]) for i in range(len(primes) - 1) if primes[i+1] - primes[i] == 2]

def sophie(n):
    sophie_germain_primes = []
    i = 2
    while len(sophie_germain_primes) < n:
        if is_prime(i) and is_prime(2 * i + 1):
            sophie_germain_primes.append(i)
        i += 1
    return sophie_germain_primes

def sexy(n):
    primes = list_primes(1000000)
    sexy = [(prime, prime + 6) for prime in primes if is_prime(prime + 6)]
    return sexy[:n]

def randprime():
    primes=get_primes()
    return random.choice(primes)

def cuban_first(n):
    cuban_primes_first=[]
    i=1
    while len(cuban_primes_first)<=n:
        p= 3 * i * i + 3 * i + 1
        if is_prime(p):
            cuban_primes_first.append(int(p))
        i+=1
    return cuban_primes_first

def cuban_second(n):
    cuban_primes_second=[]
    i=1
    while len(cuban_primes_second)<=n:
        p= 3*i**2+6*i+4
        if is_prime(p):
            cuban_primes_second.append(int(p))
        i+=1
    return cuban_primes_second
    
def lucas_test():
    pass

print(cuban_second(200))

