fruit = 'banana' # b=0, a=1, n=2, a=3, n=4, a=5 ; but in total there are 6 characters.
for letter in fruit :
  print(letter)

index = 0
while index < len(fruit) :
  letter = fruit[index]
  print(letter)
  index = index + 1
