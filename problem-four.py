def largest_palindrome(num):
  start_index = 10 ** (num - 1) #10
  end_index = (10 ** num) #100
  answer_array = [0,0]
  answer = 0
  for i in range(start_index, end_index):
    for j in range(start_index, end_index):
      product = str(i * j)
      product_reverse = product[::-1]
      if(product == product_reverse):
        if(i * j > answer):
          answer = i * j
          answer_array[0] = i
          answer_array[1] = j
  return answer_array, answer

    

print(largest_palindrome(3)) #913 * 993 = 906609

