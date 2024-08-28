import math
from functools import lru_cache
import random
from itertools import permutations

_primes=None

#Generates a list of all prime numbers up to a given number n using the Sieve of Eratosthenes algorithm.
def list_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
                
    primes = [x for x in range(n + 1) if sieve[x]]
    return primes

#Returns a cached list of all prime numbers up to 2,000,000, generating it if it hasn't been created yet.
def get_primes():
    global _primes
    if _primes is None:
        _primes = list_primes(2000000)
    return _primes

#Determines if a given number n is prime by checking divisibility up to its square root.
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
#Calculates the sum of all prime numbers up to a given number n.
def sum_primes(n):
    return sum(list_primes(n))


#Returns a list of the prime factors of a given number n.
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors


#Finds the next prime number greater than n using caching to speed up repeated calls.
@lru_cache(None)
def next_prime(n):
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1

#Finds the largest prime number smaller than n using caching to speed up repeated calls.
@lru_cache(None)
def previous_prime(n):
    i = n - 1
    while True:
        if is_prime(i):
            return i
        i -= 1

#Returns the count of all prime numbers up to a given number n.
def count_primes(n):
    return len(list_primes(n))

#Calculates the product of all prime numbers up to a given number n.
def prime_product(n):
    primes = list_primes(n)
    product = 1
    for prime in primes:
        product *= prime
    return product

def prime_sum_pairs(n):
    pass

#Generates a list of the first n primes that remain prime when their digits are reversed.
def mirror(n):
    mirrors=[]
    primes=get_primes()
    while len(mirrors)<=n:
        for i in primes:
            if is_prime(int(str(i)[::-1])):
                mirrors.append(i)
    return mirrors

#Returns a list of the first n twin prime pairs (pairs of primes that differ by 2).
def twin_primes(n):
    primes = list_primes(n)
    return [(primes[i], primes[i+1]) for i in range(len(primes) - 1) if primes[i+1] - primes[i] == 2]

# Finds the first n Sophie Germain primes, which are primes p such that 2p + 1 is also prime.
def sophie(n):
    sophie_germain_primes = []
    i = 2
    while len(sophie_germain_primes) < n:
        if is_prime(i) and is_prime(2 * i + 1):
            sophie_germain_primes.append(i)
        i += 1
    return sophie_germain_primes

# Generates the first n sexy prime pairs, where two primes differ by 6.
def sexy(n):
    primes = list_primes(2000000)
    sexy = [(prime, prime + 6) for prime in primes if is_prime(prime + 6)]
    return sexy[:n]

#Returns a random prime number from the cached list of primes.
def randprime():
    primes=get_primes()
    return random.choice(primes)

# Finds the first n Cuban primes of the first kind
def cuban_first(n):
    cuban_primes_first=[]
    i=1
    while len(cuban_primes_first)<=n:
        p= 3 * i * i + 3 * i + 1
        if is_prime(p):
            cuban_primes_first.append(int(p))
        i+=1
    return cuban_primes_first

#Finds the first n Cuban primes of the second kind
def cuban_second(n):
    cuban_primes_second=[]
    i=1
    while len(cuban_primes_second)<=n:
        p= 3*i**2+6*i+4
        if is_prime(p):
            cuban_primes_second.append(int(p))
        i+=1
    return cuban_primes_second

#Computes (base^exp) % mod efficiently using modular exponentiation.
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


#Performs the Lucas primality test k times on a number n to determine if it's prime, composite, or possibly composite.
def lucas_test(n,k):
    if n < 2:
        return "composite"
    if n == 2:
        return "prime"
    if n % 2 == 0:
        return "composite"
    
    factors = prime_factors(n - 1)

    for _ in range(k):
        a = random.randint(2, n - 1)
        if math.gcd(a, n) > 1:
            return "composite"
        
        # Check if a^(n-1) ≢ 1 (mod n)
        if mod_exp(a, n - 1, n) != 1:
            return "composite"
        
        # Check if a^((n-1)/q) ≢ 1 (mod n) for all prime factors q of n-1
        for q in factors:
            if mod_exp(a, (n - 1) // q, n) == 1:
                break
        else:
            return "prime"

    return "possibly composite"


#Checks if the sum of the digits of a prime number is also prime.
def prime_digit_sum(n):
    if is_prime(n):
        sum=0
        for digit in str(n):  
            sum += int(digit) 
        if is_prime(sum):
            return True
    return False

#provides an estimate of the number of prime numbers less than or equal to a given number n using the Prime Number Theorem (PNT).
def prime_count_estimate(n):
        if n < 2:
            return 0
        return int(n / math.log(n))

'''
returns the first n number of circular primes
def circular(n):
    p=get_primes()
    circulars=[]
    prime_set = set(p)  
    
    for prime in p:
        # Generate all permutations of the digits of the prime
        perms = {int(''.join(p)) for p in permutations(str(prime))}
        
        # Check if all permutations are prime and also in the primes list
        if all(perm in prime_set for perm in perms):
            if prime not in circulars:
                circulars.append(prime)
        
        # Stop when we've found n circular primes
        if len(circulars) >= n:
            break
    
    return circulars

print(circular(50))
'''

# Returns the first 8 mersenne primes
def mersenne():
    p=get_primes()
    mersenne_primes=[]
    for prime in p:
        if is_prime((2**prime)-1):
            mersenne_primes.append(2**prime-1)
            if len(mersenne_primes)>=8:
                break
    return mersenne_primes
