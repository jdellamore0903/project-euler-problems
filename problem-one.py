def multiples_of_three_five(num):
  answer = 0
  for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
      answer += i
  return answer

print multiples_of_three_five(10) #returns 23
print multiples_of_three_five(1000) #returns 233168