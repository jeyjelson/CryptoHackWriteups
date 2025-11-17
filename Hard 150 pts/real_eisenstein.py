## ATTEMPT AT HARD QUESTION 


import math
from decimal import *
getcontext().prec = 100

FLAG = "crypto{test_attempt}"
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

h = Decimal(0.0)

for i, c in enumerate(FLAG):
    h += ord(c) * Decimal(PRIMES[i]).sqrt()

ct = math.floor(h*16**64)
print(f"ciphertext: {ct}")

# ciphertext: 1350995397927355657956786955603012410260017344805998076702828160316695004588429433

#the code above creates ciphertexts generation by summing up each characters ASCII value multiplied by the square root of corresponding prime numbers
#the job is to reverse it butit is too hard 
