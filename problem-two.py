def even_fibonacci(limit):
  a = 0
  b = 1
  answer = 0
  while(True):
    temp = a
    a = b
    b = temp + b
    if b < limit:
      if b % 2 == 0:
        answer += b
    else:
      break
  return answer


print(even_fibonacci(4000000)) #returns 4613732

