def isArmstrong(x):
  x = 153
  sum = 0
  temp = x
  #sum of cube of each digit
  while temp > 0:       
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if x == sum:
   print(x,"True, is an Armstrong number")
  else:
   print(x,"False, is not an Armstrong number")
print(isArmstrong(sum))



  
