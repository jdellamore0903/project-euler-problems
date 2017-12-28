def largest_prime_factors(num):
  prime_factors = []
  i = 2
  while i * i <= num:
    if num % i != 0:
      i += 1
    else:
      num //= i
      prime_factors.append(i)
  if num > 1:
    prime_factors.append(num)
  return prime_factors

print largest_prime_factors(600851475143) #returns largest prime factor which is 6857