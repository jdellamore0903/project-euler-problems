#Big O of N
def sum_of_square_difference(num):
  answer_one = 0
  answer_two = 0
  for i in range(1, num + 1):
    answer_one += i ** 2
    answer_two += i
  answer_two = answer_two ** 2
  return answer_two - answer_one

print(sum_of_square_difference(100)) #returns 25164150


#Constant time
def sum_of_square_difference_constant(num):
  answer_one = ((num / 2) * (num + 1)) ** 2
  answer_two = (num * (num + 1) * (2 * num + 1)) / 6
  return answer_one - answer_two

print(sum_of_square_difference_constant(100))
