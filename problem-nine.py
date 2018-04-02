def pythagorean_triplet(num):
  largest_a = 0
  largest_b = 0
  largest_c = 0
  for a in range(0,num + 1):
    for b in range(0,num + 1):
      for c in range(0,num + 1):
        if(a < b and b < c):
          if(a + b + c == 1000):
            if(a**2 + b**2 == c**2):
              largest_a = a
              largest_b = b
              largest_c = c
return largest_a, largest_b, largest_c



pythagorean_triplet(5)