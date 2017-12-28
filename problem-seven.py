# def primes_upto(limit):
#     prime = [True] * limit
#     for n in range(2, limit):
#         if prime[n]:
#             yield n # n is a prime
#             for c in range(n*n, limit, n):
#                 prime[c] = False # mark composites


# #BROKEN
# print(primes_upto(100))

def prime_numbers_to(num, num2, prime_numbers):
  if len(prime_numbers) == num:
    return prime_numbers
  else:
    for n in range(2, num2):
      if num2 % n == 0:
        break
        return prime_numbers_to(num, num2 + 1, prime_numbers)
    prime_numbers.append(num2)
    return prime_numbers_to(num, num2 + 1, prime_numbers)

print(prime_numbers_to(5, 1, []))

