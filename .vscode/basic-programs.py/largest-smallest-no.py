#Finding the largest number

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
  if the_num > largest_so_far :
    largest_so_far = the_num
  print(largest_so_far, the_num)
print('After', largest_so_far)

#Finding the smallest number

smallest = None #where NONE is a FLAG valuep
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
  if smallest is None :
    smallest = value
  elif value < smallest :
    smallest = value
  print(smallest, value)
print('Afer', smallest)
